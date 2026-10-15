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

The model's most likely 1X2 outcome is **Brentford win** at **39.3%**. Expected goals are 1.58 for Brentford and 1.48 for Liverpool (3.06 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 59.1%; Under 3.5 goals: 63.4%; Double Chance 1X: 65.6%; Double Chance X2: 60.7%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 80.5%; BTTS Yes (both teams score): 62.5%; BTTS No (at least one team does not score): 37.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 39.3% | 2.54 |
| Draw | 26.3% | 3.80 |
| Liverpool win | 34.4% | 2.91 |

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
| 1 | 1-1 | 12.12% |
| 2 | 2-1 | 8.75% |
| 3 | 1-2 | 8.07% |
| 4 | 2-2 | 6.35% |
| 5 | 1-0 | 6.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 39.3% | 39.7% | 2.51 | -1.2% |
| Draw | 26.3% | 26.1% | 3.74 | -1.7% |
| Liverpool win | 34.4% | 34.2% | 2.87 | -1.4% |

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
| Market best home last update utc | 2026-10-15T09:50:35Z |
| Market best draw last update utc | 2026-10-15T09:50:35Z |
| Market best away last update utc | 2026-10-15T09:50:35Z |
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
| Fair Under 0.5 odds | 16.94 |
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
| P home draw | 65.6% |
| P draw away | 60.7% |
| P home away | 73.7% |
| Raw p home draw | 65.5% |
| Raw p draw away | 61.0% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.50 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.52 |
| Home probability edge | -0.4% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | -0.0077 |
| Raw ev home | -0.0222 |
| Raw edge prob draw | 0.0047 |
| Raw ev draw | -0.0078 |
| Raw edge prob away | 0.0030 |
| Raw ev away | -0.0095 |
| Market p home draw | 66.4% |
| Market home draw odds | 1.48 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:50:35Z |
| Market reference home draw last update utc | 2026-10-15T09:50:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.4% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:50:35Z |
| Market reference draw away last update utc | 2026-10-15T09:50:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.2% |
| Market home away odds | 1.32 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:50:35Z |
| Market reference home away last update utc | 2026-10-15T09:50:54Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.61 |
| Market reference dc home draw odds | 1.44 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T09:50:33Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.0% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T09:50:33Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.28 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.3% |
| Market btts yes odds | 1.46 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:50:35Z |
| Market reference btts yes odds | 1.54 |
| Market reference btts yes opposite odds | 2.74 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **40.0%**. Expected goals are 1.40 for Everton and 1.37 for Chelsea (2.76 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.9%; Double Chance 1X: 60.0%; Double Chance X2: 66.9%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 33.1% | 3.03 |
| Draw | 27.0% | 3.71 |
| Chelsea win | 40.0% | 2.50 |

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
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.82% |
| 2 | 1-2 | 9.35% |
| 3 | 0-1 | 8.22% |
| 4 | 2-1 | 7.60% |
| 5 | 0-0 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 33.1% | 29.6% | 3.23 | +6.8% |
| Draw | 27.0% | 25.7% | 3.88 | +4.6% |
| Chelsea win | 40.0% | 44.8% | 2.23 | -10.9% |
| Over 2.5 | 52.6% | 57.5% | 1.73 | -8.9% |
| Under 2.5 | 47.4% | 42.5% | 2.28 | +8.0% |

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
| Market best home last update utc | 2026-10-15T09:50:35Z |
| Market best draw last update utc | 2026-10-15T09:50:35Z |
| Market best away last update utc | 2026-10-15T09:50:35Z |
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
| Fair Under 0.5 odds | 13.60 |
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
| P home away | 73.0% |
| Raw p home draw | 64.8% |
| Raw p draw away | 63.4% |
| Raw p home away | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.35 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.22 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.11 |
| Home probability edge | +3.5% |
| Draw probability edge | +1.3% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | 0.0700 |
| Raw ev home | 0.1808 |
| Raw edge prob draw | 0.0256 |
| Raw ev draw | 0.0962 |
| Raw edge prob away | -0.0956 |
| Raw ev away | -0.2153 |
| Market p home draw | 56.0% |
| Market home draw odds | 1.73 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:50:35Z |
| Market reference home draw last update utc | 2026-10-15T09:50:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.5% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:50:35Z |
| Market reference draw away last update utc | 2026-10-15T09:50:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.4% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:50:35Z |
| Market reference home away last update utc | 2026-10-15T09:50:54Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.37 |
| Market reference dc home draw odds | 1.70 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T09:50:57Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.8% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T09:50:57Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.61 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.0% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:50:35Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **41.7%**. Expected goals are 0.94 for Fulham and 1.22 for Hull City (2.16 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 88.6%; Over 2.5 goals: 37.8%; Under 3.5 goals: 82.9%; Double Chance 1X: 69.9%; Double Chance X2: 58.3%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 93.0%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 41.7% | 2.40 |
| Draw | 28.1% | 3.56 |
| Hull City win | 30.1% | 3.32 |

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
| 1 | 1-0 | 14.45% |
| 2 | 1-1 | 12.92% |
| 3 | 0-0 | 11.42% |
| 4 | 2-1 | 9.66% |
| 5 | 0-1 | 9.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 41.7% | 56.6% | 1.77 | -26.1% |
| Draw | 28.1% | 24.1% | 4.05 | +13.9% |
| Hull City win | 30.1% | 19.3% | 4.93 | +48.6% |
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
| Market best home last update utc | 2026-10-15T09:50:35Z |
| Market best draw last update utc | 2026-10-15T09:50:35Z |
| Market best away last update utc | 2026-10-15T09:50:35Z |
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
| Fair Under 0.5 odds | 8.75 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.85 |
| Fair Over 2.5 odds | 2.65 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.84 |
| Fair Under 3.5 odds | 1.21 |
| Fair Over 4.5 odds | 14.29 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 32.1% |
| Unadjusted away-win probability | 40.9% |
| Raw p over 1 5 | 65.1% |
| Raw p under 3 5 | 82.7% |
| Raw p btts yes | 44.5% |
| P home draw | 69.9% |
| P draw away | 58.3% |
| P home away | 71.9% |
| Raw p home draw | 59.1% |
| Raw p draw away | 73.1% |
| Raw p home away | 67.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.76 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.10 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.01 |
| Home probability edge | -14.8% |
| Draw probability edge | +4.0% |
| Away probability edge | +10.8% |
| Over 2.5 probability edge | -17.2% |
| Under 2.5 probability edge | +17.2% |
| Raw edge prob home | -0.2961 |
| Raw ev home | -0.5231 |
| Raw edge prob draw | 0.0802 |
| Raw ev draw | 0.3011 |
| Raw edge prob away | 0.2159 |
| Raw ev away | 1.0179 |
| Market p home draw | 79.1% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:50:35Z |
| Market reference home draw last update utc | 2026-10-15T09:50:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.9% |
| Market draw away odds | 2.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:50:35Z |
| Market reference draw away last update utc | 2026-10-15T09:50:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.0% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:50:35Z |
| Market reference home away last update utc | 2026-10-15T09:50:54Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.13 |
| Market reference dc home draw odds | 1.21 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 79.5% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T09:50:12Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.7% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T09:50:12Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 2.65 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.0% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:50:35Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.18 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **83.7%**. Expected goals are 3.47 for Manchester City and 0.73 for Ipswich Town (4.20 combined). The most likely exact score is 3-0 at 10.1%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 78.0%; Under 3.5 goals: 40.6%; Double Chance 1X: 94.5%; Double Chance X2: 16.3%; Double Chance 12 (either team wins): 89.2%; Under 4.5 goals: 60.0%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 83.7% | 1.20 |
| Draw | 10.8% | 9.24 |
| Ipswich Town win | 5.5% | 18.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.47 |
| Ipswich Town expected goals | 0.73 |
| Expected total goals | 4.20 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 92.2% |
| Under 1.5 | 7.8% |
| Over 2.5 | 78.0% |
| Under 2.5 | 22.0% |
| Over 3.5 | 59.4% |
| Under 3.5 | 40.6% |
| Over 4.5 | 40.0% |
| Under 4.5 | 60.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.11% |
| 2 | 4-0 | 8.77% |
| 3 | 2-0 | 8.74% |
| 4 | 3-1 | 7.34% |
| 5 | 4-1 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 83.7% | 80.5% | 1.26 | +5.4% |
| Draw | 10.8% | 12.3% | 7.26 | -21.5% |
| Ipswich Town win | 5.5% | 7.2% | 11.50 | -36.4% |

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
| Market best home last update utc | 2026-10-15T09:50:35Z |
| Market best draw last update utc | 2026-10-15T09:50:35Z |
| Market best away last update utc | 2026-10-15T09:50:35Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man City |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.49 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 12.80 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.54 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.46 |
| Fair Over 4.5 odds | 2.50 |
| Fair Under 4.5 odds | 1.67 |
| Unadjusted home-win probability | 86.8% |
| Unadjusted draw probability | 9.4% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 92.6% |
| Raw p under 3 5 | 39.7% |
| Raw p btts yes | 50.5% |
| P home draw | 94.5% |
| P draw away | 16.3% |
| P home away | 89.2% |
| Raw p home draw | 96.2% |
| Raw p draw away | 13.2% |
| Raw p home away | 90.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.24 |
| Reference draw odds | 8.00 |
| Reference away odds | 13.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | +3.2% |
| Draw probability edge | -1.5% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | +7.1% |
| Under 2.5 probability edge | -7.1% |
| Raw edge prob home | 0.0632 |
| Raw ev home | 0.0938 |
| Raw edge prob draw | -0.0290 |
| Raw ev draw | -0.3199 |
| Raw edge prob away | -0.0342 |
| Raw ev away | -0.5606 |
| Market p home draw | 91.3% |
| Market home draw odds | 1.05 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:50:35Z |
| Market reference home draw last update utc | 2026-10-15T09:50:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.4% |
| Market draw away odds | 4.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:50:35Z |
| Market reference draw away last update utc | 2026-10-15T09:50:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.3% |
| Market home away odds | 1.13 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:50:35Z |
| Market reference home away last update utc | 2026-10-15T09:50:54Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.28 |
| Market reference dc home draw odds | 1.05 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 92.1% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T09:50:57Z |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 6.05 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 50.5% |
| Market under 3 5 odds | 1.95 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T09:50:57Z |
| Market reference under 3 5 odds | 1.95 |
| Market reference under 3 5 opposite odds | 1.99 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.6% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:50:35Z |
| Market reference btts yes odds | 1.88 |
| Market reference btts yes opposite odds | 2.08 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **42.0%**. Expected goals are 1.76 for Newcastle United and 1.52 for Aston Villa (3.28 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.4%; Double Chance 1X: 67.5%; Double Chance X2: 58.0%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 66.0%; BTTS No (at least one team does not score): 34.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 42.0% | 2.38 |
| Draw | 25.5% | 3.92 |
| Aston Villa win | 32.5% | 3.08 |

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
| 1 | 1-1 | 11.32% |
| 2 | 2-1 | 8.79% |
| 3 | 1-2 | 7.68% |
| 4 | 2-2 | 6.80% |
| 5 | 2-0 | 5.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 42.0% | 41.8% | 2.26 | -5.0% |
| Draw | 25.5% | 25.7% | 3.85 | -1.9% |
| Aston Villa win | 32.5% | 32.5% | 3.19 | +3.6% |
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
| Market best home last update utc | 2026-10-15T09:50:36Z |
| Market best draw last update utc | 2026-10-15T09:50:36Z |
| Market best away last update utc | 2026-10-15T09:50:36Z |
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
| Fair Under 0.5 odds | 20.17 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.70 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.41 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.28 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 32.5% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 58.4% |
| Raw p btts yes | 65.9% |
| P home draw | 67.5% |
| P draw away | 58.0% |
| P home away | 74.5% |
| Raw p home draw | 67.5% |
| Raw p draw away | 57.7% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.38 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.24 |
| Home probability edge | +0.3% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | +3.2% |
| Under 2.5 probability edge | -3.2% |
| Raw edge prob home | 0.0053 |
| Raw ev home | -0.0444 |
| Raw edge prob draw | -0.0047 |
| Raw ev draw | -0.0277 |
| Raw edge prob away | -0.0006 |
| Raw ev away | 0.0355 |
| Market p home draw | 67.8% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:50:36Z |
| Market reference home draw last update utc | 2026-10-15T09:51:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.0% |
| Market draw away odds | 1.71 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:50:36Z |
| Market reference draw away last update utc | 2026-10-15T09:51:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.2% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:50:36Z |
| Market reference home away last update utc | 2026-10-15T09:51:02Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.48 |
| Market reference dc home draw odds | 1.31 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 83.3% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T09:50:35Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.2% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T09:50:35Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.33 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.3% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:50:36Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.43 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.2%**. Expected goals are 1.59 for Bournemouth and 1.06 for Sunderland (2.65 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 49.5%; Under 3.5 goals: 72.6%; Double Chance 1X: 74.5%; Double Chance X2: 52.8%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 53.3%; BTTS No (at least one team does not score): 46.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.2% | 2.12 |
| Draw | 27.3% | 3.66 |
| Sunderland win | 25.5% | 3.92 |

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
| 1 | 1-1 | 13.04% |
| 2 | 1-0 | 9.65% |
| 3 | 2-1 | 9.25% |
| 4 | 2-0 | 8.74% |
| 5 | 0-0 | 8.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.2% | 46.1% | 2.04 | -3.7% |
| Draw | 27.3% | 26.8% | 3.75 | +2.3% |
| Sunderland win | 25.5% | 27.2% | 3.85 | -1.7% |
| Over 2.5 | 49.5% | 53.1% | 1.88 | -6.9% |
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
| Market best home last update utc | 2026-10-15T09:50:36Z |
| Market best draw last update utc | 2026-10-15T09:50:36Z |
| Market best away last update utc | 2026-10-15T09:50:36Z |
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
| Fair Under 0.5 odds | 12.05 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.09 |
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
| P home draw | 74.5% |
| P draw away | 52.8% |
| P home away | 72.7% |
| Raw p home draw | 76.1% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.16 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.65 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 1.94 |
| Home probability edge | +1.1% |
| Draw probability edge | +0.5% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | 0.0227 |
| Raw ev home | -0.0142 |
| Raw edge prob draw | 0.0100 |
| Raw ev draw | 0.0420 |
| Raw edge prob away | -0.0327 |
| Raw ev away | -0.0803 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **61.1%**. Expected goals are 2.00 for Brighton and Hove Albion and 1.02 for Crystal Palace (3.02 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 58.8%; Under 3.5 goals: 64.0%; Double Chance 1X: 83.2%; Double Chance X2: 38.9%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 56.0%; BTTS No (at least one team does not score): 44.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 61.1% | 1.64 |
| Draw | 22.1% | 4.53 |
| Crystal Palace win | 16.8% | 5.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 2.00 |
| Crystal Palace expected goals | 1.02 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.43% |
| 2 | 2-1 | 10.31% |
| 3 | 2-0 | 10.11% |
| 4 | 1-0 | 8.91% |
| 5 | 3-1 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 61.1% | 63.2% | 1.63 | -0.4% |
| Draw | 22.1% | 20.7% | 4.57 | +1.0% |
| Crystal Palace win | 16.8% | 16.1% | 5.44 | -8.5% |
| Over 2.5 | 58.8% | 61.5% | 1.63 | -4.2% |
| Under 2.5 | 41.2% | 38.5% | 2.49 | +2.6% |

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
| Market best home last update utc | 2026-10-15T09:50:36Z |
| Market best draw last update utc | 2026-10-15T09:50:36Z |
| Market best away last update utc | 2026-10-15T09:50:36Z |
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
| Fair Under 0.5 odds | 17.67 |
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
| P home draw | 83.2% |
| P draw away | 38.9% |
| P home away | 77.9% |
| Raw p home draw | 82.5% |
| Raw p draw away | 41.0% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.57 |
| Reference draw odds | 4.70 |
| Reference away odds | 6.00 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -2.1% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | -0.0420 |
| Raw ev home | -0.0386 |
| Raw edge prob draw | 0.0282 |
| Raw ev draw | 0.0742 |
| Raw edge prob away | 0.0138 |
| Raw ev away | -0.0472 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **39.5%**. Expected goals are 1.42 for Leeds United and 1.28 for Manchester United (2.70 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.4%; Double Chance 1X: 67.2%; Double Chance X2: 60.5%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 39.5% | 2.53 |
| Draw | 27.6% | 3.62 |
| Manchester United win | 32.8% | 3.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.28 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 76.6% |
| Under 1.5 | 23.4% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.6% |
| Under 3.5 | 71.4% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.19% |
| 2 | 2-1 | 8.82% |
| 3 | 1-0 | 8.29% |
| 4 | 1-2 | 7.88% |
| 5 | 0-0 | 7.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 39.5% | 40.3% | 2.51 | -0.8% |
| Draw | 27.6% | 26.7% | 3.75 | +3.7% |
| Manchester United win | 32.8% | 33.0% | 2.86 | -6.1% |
| Over 2.5 | 50.9% | 58.5% | 1.70 | -13.4% |
| Under 2.5 | 49.1% | 41.5% | 2.34 | +14.8% |

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
| Market best home last update utc | 2026-10-15T09:50:36Z |
| Market best draw last update utc | 2026-10-15T09:50:36Z |
| Market best away last update utc | 2026-10-15T09:50:36Z |
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
| Fair Under 0.5 odds | 12.69 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.27 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.25 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 76.5% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 56.1% |
| P home draw | 67.2% |
| P draw away | 60.5% |
| P home away | 72.4% |
| Raw p home draw | 67.4% |
| Raw p draw away | 61.2% |
| Raw p home away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.46 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.00 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | -0.8% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | -0.0155 |
| Raw ev home | -0.0270 |
| Raw edge prob draw | 0.0189 |
| Raw ev draw | 0.0721 |
| Raw edge prob away | -0.0035 |
| Raw ev away | -0.0663 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **57.2%**. Expected goals are 0.76 for Nottingham Forest and 1.53 for Arsenal (2.29 combined). The most likely exact score is 0-1 at 14.9%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 41.1%; Under 3.5 goals: 79.8%; Double Chance 1X: 42.8%; Double Chance X2: 83.5%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 42.6%; BTTS No (at least one team does not score): 57.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.5% | 6.05 |
| Draw | 26.3% | 3.81 |
| Arsenal win | 57.2% | 1.75 |

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
| 1 | 0-1 | 14.88% |
| 2 | 0-2 | 12.47% |
| 3 | 1-1 | 12.10% |
| 4 | 0-0 | 10.55% |
| 5 | 1-2 | 9.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.5% | 15.8% | 6.11 | +1.0% |
| Draw | 26.3% | 24.0% | 3.98 | +4.5% |
| Arsenal win | 57.2% | 60.2% | 1.66 | -5.0% |
| Over 2.5 | 41.1% | 49.8% | 1.97 | -19.0% |
| Under 2.5 | 58.9% | 50.2% | 1.97 | +16.0% |

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
| Market best home last update utc | 2026-10-15T09:50:36Z |
| Market best draw last update utc | 2026-10-15T09:50:36Z |
| Market best away last update utc | 2026-10-15T09:50:36Z |
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
| P btts yes | 42.6% |
| P btts no | 57.4% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.48 |
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
| P home draw | 42.8% |
| P draw away | 83.5% |
| P home away | 73.7% |
| Raw p home draw | 45.8% |
| Raw p draw away | 82.7% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 6.20 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.65 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | +0.8% |
| Draw probability edge | +2.3% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | 0.0152 |
| Raw ev home | 0.0567 |
| Raw edge prob draw | 0.0456 |
| Raw ev draw | 0.1360 |
| Raw edge prob away | -0.0608 |
| Raw ev away | -0.1009 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **54.8%**. Expected goals are 1.43 for Tottenham Hotspur and 1.06 for Coventry City (2.49 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 47.2%; Under 3.5 goals: 75.4%; Double Chance 1X: 79.6%; Double Chance X2: 45.2%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 49.8%; BTTS No (at least one team does not score): 50.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 54.8% | 1.82 |
| Draw | 24.8% | 4.04 |
| Coventry City win | 20.4% | 4.89 |

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
| 1 | 1-0 | 12.98% |
| 2 | 1-1 | 11.80% |
| 3 | 2-1 | 11.16% |
| 4 | 2-0 | 10.56% |
| 5 | 0-0 | 8.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 54.8% | 65.5% | 1.54 | -15.6% |
| Draw | 24.8% | 20.1% | 4.72 | +16.8% |
| Coventry City win | 20.4% | 14.4% | 6.47 | +32.3% |
| Over 2.5 | 47.2% | 60.9% | 1.64 | -22.6% |
| Under 2.5 | 52.8% | 39.1% | 2.46 | +30.0% |

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
| Market best home last update utc | 2026-10-15T09:50:36Z |
| Market best draw last update utc | 2026-10-15T09:50:36Z |
| Market best away last update utc | 2026-10-15T09:50:36Z |
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
| P btts yes | 49.8% |
| P btts no | 50.2% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.16 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.72 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 4.07 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.82 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 44.1% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 26.5% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 76.1% |
| Raw p btts yes | 51.1% |
| P home draw | 79.6% |
| P draw away | 45.2% |
| P home away | 75.2% |
| Raw p home draw | 73.5% |
| Raw p draw away | 55.9% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.52 |
| Reference draw odds | 4.90 |
| Reference away odds | 6.80 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | -10.7% |
| Draw probability edge | +4.7% |
| Away probability edge | +6.0% |
| Over 2.5 probability edge | -13.8% |
| Under 2.5 probability edge | +13.8% |
| Raw edge prob home | -0.2141 |
| Raw ev home | -0.3210 |
| Raw edge prob draw | 0.0935 |
| Raw ev draw | 0.3891 |
| Raw edge prob away | 0.1206 |
| Raw ev away | 0.7131 |

</details>


---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **45.5%**. Expected goals are 1.22 for Ipswich Town and 1.76 for Nottingham Forest (2.98 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 56.9%; Under 3.5 goals: 65.4%; Double Chance 1X: 54.5%; Double Chance X2: 72.1%; Double Chance 12 (either team wins): 73.4%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 59.9%; BTTS No (at least one team does not score): 40.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 27.9% | 3.58 |
| Draw | 26.6% | 3.77 |
| Nottingham Forest win | 45.5% | 2.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.22 |
| Nottingham Forest expected goals | 1.76 |
| Expected total goals | 2.98 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 56.9% |
| Under 2.5 | 43.1% |
| Over 3.5 | 34.6% |
| Under 3.5 | 65.4% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.44% |
| 2 | 1-2 | 8.93% |
| 3 | 2-1 | 7.37% |
| 4 | 0-2 | 7.34% |
| 5 | 0-1 | 7.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 27.9% | 30.7% | 3.10 | -13.4% |
| Draw | 26.6% | 27.2% | 3.63 | -3.6% |
| Nottingham Forest win | 45.5% | 42.1% | 2.39 | +8.8% |
| Over 2.5 | 56.9% | 53.2% | 1.84 | +4.7% |
| Under 2.5 | 43.1% | 46.8% | 2.12 | -8.7% |

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
| Market best home last update utc | 2026-10-15T09:50:36Z |
| Market best draw last update utc | 2026-10-15T09:50:36Z |
| Market best away last update utc | 2026-10-15T09:50:36Z |
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
| P btts yes | 59.9% |
| P btts no | 40.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.42 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.23 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.57 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 25.1% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 49.0% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 59.6% |
| P home draw | 54.5% |
| P draw away | 72.1% |
| P home away | 73.4% |
| Raw p home draw | 51.0% |
| Raw p draw away | 74.9% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.15 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.32 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.00 |
| Home probability edge | -2.8% |
| Draw probability edge | -0.6% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | +3.7% |
| Under 2.5 probability edge | -3.7% |
| Raw edge prob home | -0.0562 |
| Raw ev home | -0.2216 |
| Raw edge prob draw | -0.0125 |
| Raw ev draw | -0.0588 |
| Raw edge prob away | 0.0687 |
| Raw ev away | 0.1702 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **66.7%**. Expected goals are 1.67 for Arsenal and 0.61 for Everton (2.28 combined). The most likely exact score is 1-0 at 17.1%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.8%; Double Chance 1X: 89.4%; Double Chance X2: 33.3%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 37.2%; BTTS No (at least one team does not score): 62.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 66.7% | 1.50 |
| Draw | 22.7% | 4.40 |
| Everton win | 10.6% | 9.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.67 |
| Everton expected goals | 0.61 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 68.4% |
| Under 1.5 | 31.6% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.10% |
| 2 | 2-0 | 15.38% |
| 3 | 1-1 | 10.13% |
| 4 | 0-0 | 10.01% |
| 5 | 2-1 | 9.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 66.7% | 71.2% | 1.43 | -4.7% |
| Draw | 22.7% | 19.4% | 4.93 | +12.0% |
| Everton win | 10.6% | 9.3% | 8.90 | -5.5% |
| Over 2.5 | 41.2% | 53.2% | 1.83 | -24.5% |
| Under 2.5 | 58.8% | 46.8% | 2.14 | +25.7% |

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
| Market best home last update utc | 2026-10-15T09:50:36Z |
| Market best draw last update utc | 2026-10-15T09:50:36Z |
| Market best away last update utc | 2026-10-15T09:50:36Z |
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
| P btts yes | 37.2% |
| P btts no | 62.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.99 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.95 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.75 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 62.1% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 11.9% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 38.1% |
| P home draw | 89.4% |
| P draw away | 33.3% |
| P home away | 77.3% |
| Raw p home draw | 88.1% |
| Raw p draw away | 37.9% |
| Raw p home away | 74.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.39 |
| Reference draw odds | 4.90 |
| Reference away odds | 10.00 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.00 |
| Home probability edge | -4.6% |
| Draw probability edge | +3.3% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -11.9% |
| Under 2.5 probability edge | +11.9% |
| Raw edge prob home | -0.0910 |
| Raw ev home | -0.1116 |
| Raw edge prob draw | 0.0653 |
| Raw ev draw | 0.2805 |
| Raw edge prob away | 0.0258 |
| Raw ev away | 0.0594 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **56.5%**. Expected goals are 1.09 for Aston Villa and 1.92 for Manchester City (3.00 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.3%; Under 3.5 goals: 64.5%; Double Chance 1X: 43.5%; Double Chance X2: 79.6%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 81.2%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 20.4% | 4.90 |
| Draw | 23.1% | 4.32 |
| Manchester City win | 56.5% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.09 |
| Manchester City expected goals | 1.92 |
| Expected total goals | 3.00 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 81.5% |
| Under 1.5 | 18.5% |
| Over 2.5 | 58.3% |
| Under 2.5 | 41.7% |
| Over 3.5 | 35.5% |
| Under 3.5 | 64.5% |
| Over 4.5 | 18.8% |
| Under 4.5 | 81.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.89% |
| 2 | 1-2 | 10.08% |
| 3 | 0-2 | 9.26% |
| 4 | 0-1 | 8.45% |
| 5 | 1-3 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 20.4% | 20.8% | 4.72 | -3.7% |
| Draw | 23.1% | 21.8% | 4.26 | -1.4% |
| Manchester City win | 56.5% | 57.4% | 1.76 | -0.6% |

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
| Market best home last update utc | 2026-10-15T09:50:36Z |
| Market best draw last update utc | 2026-10-15T09:50:36Z |
| Market best away last update utc | 2026-10-15T09:50:36Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.21 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.39 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.40 |
| Fair Over 3.5 odds | 2.82 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.33 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 20.0% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 55.5% |
| Raw p over 1 5 | 81.3% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 57.8% |
| P home draw | 43.5% |
| P draw away | 79.6% |
| P home away | 76.9% |
| Raw p home draw | 44.5% |
| Raw p draw away | 80.0% |
| Raw p home away | 75.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 4.50 |
| Reference draw odds | 4.30 |
| Reference away odds | 1.70 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -0.4% |
| Draw probability edge | +1.4% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0073 |
| Raw ev home | -0.0540 |
| Raw edge prob draw | 0.0271 |
| Raw ev draw | 0.0435 |
| Raw edge prob away | -0.0198 |
| Raw ev away | -0.0239 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **55.6%**. Expected goals are 2.11 for Chelsea and 1.17 for Tottenham Hotspur (3.28 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 63.3%; Under 3.5 goals: 58.8%; Double Chance 1X: 79.1%; Double Chance X2: 44.4%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 76.9%; BTTS Yes (both teams score): 61.9%; BTTS No (at least one team does not score): 38.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 55.6% | 1.80 |
| Draw | 23.5% | 4.26 |
| Tottenham Hotspur win | 20.9% | 4.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.11 |
| Tottenham Hotspur expected goals | 1.17 |
| Expected total goals | 3.28 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 63.3% |
| Under 2.5 | 36.7% |
| Over 3.5 | 41.2% |
| Under 3.5 | 58.8% |
| Over 4.5 | 23.1% |
| Under 4.5 | 76.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.67% |
| 2 | 2-1 | 9.44% |
| 3 | 2-0 | 8.06% |
| 4 | 3-1 | 6.63% |
| 5 | 1-0 | 6.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 55.6% | 53.5% | 1.90 | +5.7% |
| Draw | 23.5% | 24.1% | 4.11 | -3.6% |
| Tottenham Hotspur win | 20.9% | 22.4% | 4.06 | -15.1% |
| Over 2.5 | 63.3% | 59.5% | 1.66 | +5.1% |
| Under 2.5 | 36.7% | 40.5% | 2.42 | -11.2% |

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
| Market best home last update utc | 2026-10-15T09:50:36Z |
| Market best draw last update utc | 2026-10-15T09:50:36Z |
| Market best away last update utc | 2026-10-15T09:50:36Z |
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
| P btts yes | 61.9% |
| P btts no | 38.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.06 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.58 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.72 |
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
| P home draw | 79.1% |
| P draw away | 44.4% |
| P home away | 76.5% |
| Raw p home draw | 80.6% |
| Raw p draw away | 42.2% |
| Raw p home away | 77.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.84 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.30 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | +2.1% |
| Draw probability edge | -0.7% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | +3.8% |
| Under 2.5 probability edge | -3.8% |
| Raw edge prob home | 0.0429 |
| Raw ev home | 0.0978 |
| Raw edge prob draw | -0.0132 |
| Raw ev draw | -0.0632 |
| Raw edge prob away | -0.0297 |
| Raw ev away | -0.2113 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **38.0%**. Expected goals are 1.13 for Coventry City and 1.17 for Fulham (2.30 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.7%; Double Chance 1X: 62.0%; Double Chance X2: 67.1%; Double Chance 12 (either team wins): 70.9%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 32.9% | 3.04 |
| Draw | 29.1% | 3.44 |
| Fulham win | 38.0% | 2.63 |

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
| 1 | 1-1 | 13.70% |
| 2 | 0-1 | 10.96% |
| 3 | 0-0 | 10.68% |
| 4 | 1-0 | 9.66% |
| 5 | 1-2 | 8.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 32.9% | 32.5% | 3.12 | +2.5% |
| Draw | 29.1% | 26.8% | 3.61 | +5.0% |
| Fulham win | 38.0% | 40.7% | 2.39 | -9.1% |
| Over 2.5 | 41.3% | 54.9% | 1.81 | -25.3% |
| Under 2.5 | 58.7% | 45.1% | 2.15 | +26.2% |

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
| Market best home last update utc | 2026-10-15T09:50:36Z |
| Market best draw last update utc | 2026-10-15T09:50:36Z |
| Market best away last update utc | 2026-10-15T09:50:36Z |
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
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.36 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.94 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.60 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 31.4% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.9% |
| Raw p btts yes | 48.3% |
| P home draw | 62.0% |
| P draw away | 67.1% |
| P home away | 70.9% |
| Raw p home draw | 64.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 68.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.98 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.07 |
| Home probability edge | +0.3% |
| Draw probability edge | +2.3% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -13.6% |
| Under 2.5 probability edge | +13.6% |
| Raw edge prob home | 0.0065 |
| Raw ev home | 0.0356 |
| Raw edge prob draw | 0.0460 |
| Raw ev draw | 0.1335 |
| Raw edge prob away | -0.0525 |
| Raw ev away | -0.1537 |

</details>


---
