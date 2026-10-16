# Ligue 1 — football model report

Fixtures in this report: **17**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 972 |
| Training data through | 2026-10-11 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | 21816ad59a5f20d30794e9f3fdc3620b3a6131cc562159502cf39100a8d3631b |
| Optimizer objective | 1681.020 |
| Base scoring parameter | 0.195 |
| Home-advantage parameter | 0.201 |
| Dixon-Coles low-score adjustment | -0.043 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-11', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 17.00 |
| Additional event odds calls used before this league | 36.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **53.9%**. Expected goals are 1.75 for Lille and 0.96 for Brest (2.72 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.2%; Double Chance 1X: 78.2%; Double Chance X2: 46.1%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 53.9% | 1.85 |
| Draw | 24.3% | 4.12 |
| Brest win | 21.8% | 4.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.75 |
| Brest expected goals | 0.96 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.57% |
| 2 | 1-0 | 10.79% |
| 3 | 2-0 | 9.88% |
| 4 | 2-1 | 9.51% |
| 5 | 0-0 | 7.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 53.9% | 52.3% | 1.93 | +4.1% |
| Draw | 24.3% | 24.1% | 3.98 | -3.3% |
| Brest win | 21.8% | 23.5% | 4.05 | -11.8% |
| Over 2.5 | 51.0% | 56.9% | 1.73 | -11.8% |
| Under 2.5 | 49.0% | 43.1% | 2.28 | +11.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | ad25a350c89b64715e15c59cde5653d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.18 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.47 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.19 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 55.5% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 20.1% |
| Raw p over 1 5 | 75.9% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 51.6% |
| P home draw | 78.2% |
| P draw away | 46.1% |
| P home away | 75.7% |
| Raw p home draw | 79.9% |
| Raw p draw away | 44.5% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.87 |
| Reference draw odds | 3.95 |
| Reference away odds | 4.05 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:07Z |
| Market reference home last update utc | 2026-10-16T22:16:07Z |
| Market reference draw last update utc | 2026-10-16T22:16:07Z |
| Market reference away last update utc | 2026-10-16T22:16:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | +1.6% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | 0.0319 |
| Raw ev home | 0.0715 |
| Raw edge prob draw | 0.0029 |
| Raw ev draw | -0.0277 |
| Raw edge prob away | -0.0347 |
| Raw ev away | -0.1878 |
| Market p home draw | 75.3% |
| Market home draw odds | 1.28 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:16:05Z |
| Market reference home draw last update utc | 2026-10-16T22:16:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.3% |
| Market draw away odds | 1.97 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:16:05Z |
| Market reference draw away last update utc | 2026-10-16T22:16:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.3% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:16:05Z |
| Market reference home away last update utc | 2026-10-16T22:16:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.91 |
| Market reference dc home draw odds | 1.25 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 80.3% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:15:32Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.65 |
| Market reference over 1 5 last update utc | 2026-10-16T22:16:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.9% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:15:32Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.72 |
| Market reference under 3 5 last update utc | 2026-10-16T22:16:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.59 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:16:05Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-16T22:16:05Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **63.6%**. Expected goals are 1.22 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.7%; Under 3.5 goals: 56.8%; Double Chance 1X: 36.4%; Double Chance X2: 82.7%; Double Chance 12 (either team wins): 80.8%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 61.5%; BTTS No (at least one team does not score): 38.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.3% | 5.79 |
| Draw | 19.2% | 5.22 |
| Paris Saint Germain win | 63.6% | 1.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.22 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.7% |
| Under 2.5 | 34.3% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.81% |
| 2 | 0-2 | 8.84% |
| 3 | 1-1 | 8.56% |
| 4 | 0-1 | 7.96% |
| 5 | 1-3 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.3% | 13.3% | 6.81 | +17.6% |
| Draw | 19.2% | 16.7% | 5.54 | +6.1% |
| Paris Saint Germain win | 63.6% | 70.0% | 1.45 | -7.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T15:15:00+00:00 |
| Fixture id | f3034246520a2ee4ff0ac0d5074966f8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Strasbourg |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.5% |
| P btts no | 38.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.22 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.78 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.01 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 57.2% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.4% |
| P home draw | 36.4% |
| P draw away | 82.7% |
| P home away | 80.8% |
| Raw p home draw | 42.8% |
| Raw p draw away | 78.7% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 7.00 |
| Reference draw odds | 5.60 |
| Reference away odds | 1.41 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:07Z |
| Market reference home last update utc | 2026-10-16T22:16:07Z |
| Market reference draw last update utc | 2026-10-16T22:16:07Z |
| Market reference away last update utc | 2026-10-16T22:16:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | +4.0% |
| Draw probability edge | +2.4% |
| Away probability edge | -6.4% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | 0.0799 |
| Raw ev home | 0.4479 |
| Raw edge prob draw | 0.0486 |
| Raw ev draw | 0.1958 |
| Raw edge prob away | -0.1285 |
| Raw ev away | -0.1713 |
| Market p home draw | 30.8% |
| Market home draw odds | 2.96 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:16:05Z |
| Market reference home draw last update utc | 2026-10-16T22:16:12Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 86.1% |
| Market draw away odds | 1.13 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:16:05Z |
| Market reference draw away last update utc | 2026-10-16T22:16:12Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.1% |
| Market home away odds | 1.18 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:16:05Z |
| Market reference home away last update utc | 2026-10-16T22:16:12Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.13 |
| Market reference dc home draw odds | 3.16 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 89.2% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 7.60 |
| Market reference over 1 5 last update utc | 2026-10-16T22:16:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.3% |
| Market under 3 5 odds | 2.06 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 3 5 odds | 1.97 |
| Market reference under 3 5 opposite odds | 1.92 |
| Market reference under 3 5 last update utc | 2026-10-16T22:16:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.6% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:16:05Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.59 |
| Market reference btts yes last update utc | 2026-10-16T22:16:12Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **62.8%**. Expected goals are 0.64 for Troyes and 2.21 for RC Lens (2.84 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 51.7%; Under 3.5 goals: 70.3%; Double Chance 1X: 37.2%; Double Chance X2: 83.6%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 43.7%; BTTS No (at least one team does not score): 56.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 16.4% | 6.11 |
| Draw | 20.8% | 4.81 |
| RC Lens win | 62.8% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.64 |
| RC Lens expected goals | 2.21 |
| Expected total goals | 2.84 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 51.7% |
| Under 2.5 | 48.3% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.21% |
| 2 | 0-1 | 10.77% |
| 3 | 1-1 | 9.82% |
| 4 | 0-3 | 8.98% |
| 5 | 1-2 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 16.4% | 23.8% | 4.30 | -29.6% |
| Draw | 20.8% | 23.5% | 4.04 | -15.9% |
| RC Lens win | 62.8% | 52.6% | 1.87 | +17.5% |
| Over 2.5 | 51.7% | 61.3% | 1.64 | -15.2% |
| Under 2.5 | 48.3% | 38.7% | 2.46 | +18.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | b077aa049133c0358bcd643bfee48da3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 43.7% |
| P btts no | 56.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.04 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.15 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.36 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.81 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 8.9% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 73.0% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 42.2% |
| P home draw | 37.2% |
| P draw away | 83.6% |
| P home away | 79.2% |
| Raw p home draw | 27.0% |
| Raw p draw away | 91.1% |
| Raw p home away | 81.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 4.00 |
| Reference draw odds | 4.05 |
| Reference away odds | 1.86 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:07Z |
| Market reference home last update utc | 2026-10-16T22:16:07Z |
| Market reference draw last update utc | 2026-10-16T22:16:07Z |
| Market reference away last update utc | 2026-10-16T22:16:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | -7.5% |
| Draw probability edge | -2.7% |
| Away probability edge | +10.2% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | -0.1495 |
| Raw ev home | -0.6179 |
| Raw edge prob draw | -0.0545 |
| Raw ev draw | -0.2694 |
| Raw edge prob away | 0.2040 |
| Raw ev away | 0.3656 |
| Market p home draw | 48.1% |
| Market home draw odds | 2.04 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:16:05Z |
| Market reference home draw last update utc | 2026-10-16T22:16:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 76.9% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:16:05Z |
| Market reference draw away last update utc | 2026-10-16T22:16:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:16:05Z |
| Market reference home away last update utc | 2026-10-16T22:16:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.22 |
| Market reference dc home draw odds | 1.95 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.4% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:14:43Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 5.10 |
| Market reference over 1 5 last update utc | 2026-10-16T22:16:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.9% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:14:43Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.51 |
| Market reference under 3 5 last update utc | 2026-10-16T22:16:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:16:05Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-16T22:16:05Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **51.0%**. Expected goals are 0.95 for Angers and 1.71 for Marseille (2.66 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.7%; Double Chance 1X: 49.0%; Double Chance X2: 76.1%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 23.9% | 4.18 |
| Draw | 25.1% | 3.99 |
| Marseille win | 51.0% | 1.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.95 |
| Marseille expected goals | 1.71 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 74.5% |
| Under 1.5 | 25.5% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 27.3% |
| Under 3.5 | 72.7% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.95% |
| 2 | 0-1 | 10.70% |
| 3 | 0-2 | 9.54% |
| 4 | 1-2 | 9.02% |
| 5 | 0-0 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 23.9% | 27.6% | 3.56 | -14.8% |
| Draw | 25.1% | 25.3% | 3.82 | -4.2% |
| Marseille win | 51.0% | 47.1% | 2.12 | +8.1% |
| Over 2.5 | 49.3% | 58.9% | 1.67 | -17.8% |
| Under 2.5 | 50.7% | 41.1% | 2.40 | +21.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | c7a60aa94470fe959fbf6b0c68060fc1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.19 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.91 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.67 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.76 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 54.9% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.4% |
| Raw p btts yes | 50.6% |
| P home draw | 49.0% |
| P draw away | 76.1% |
| P home away | 74.9% |
| Raw p home draw | 45.1% |
| Raw p draw away | 79.8% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.49 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.08 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:07Z |
| Market reference home last update utc | 2026-10-16T22:16:07Z |
| Market reference draw last update utc | 2026-10-16T22:16:07Z |
| Market reference away last update utc | 2026-10-16T22:16:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | -3.7% |
| Draw probability edge | -0.2% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.0740 |
| Raw ev home | -0.2798 |
| Raw edge prob draw | -0.0045 |
| Raw ev draw | -0.0501 |
| Raw edge prob away | 0.0784 |
| Raw ev away | 0.1640 |
| Market p home draw | 54.9% |
| Market home draw odds | 1.81 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:16:05Z |
| Market reference home draw last update utc | 2026-10-16T22:16:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.4% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:16:05Z |
| Market reference draw away last update utc | 2026-10-16T22:16:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.6% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:16:05Z |
| Market reference home away last update utc | 2026-10-16T22:16:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home draw odds | 1.73 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.7% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:15:07Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.95 |
| Market reference over 1 5 last update utc | 2026-10-16T22:16:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:15:07Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market reference under 3 5 last update utc | 2026-10-16T22:16:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.7% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:16:05Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.45 |
| Market reference btts yes last update utc | 2026-10-16T22:16:05Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **38.1%**. Expected goals are 1.17 for Le Havre and 1.17 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.6%; Under 3.5 goals: 79.1%; Double Chance 1X: 66.8%; Double Chance X2: 61.9%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 38.1% | 2.63 |
| Draw | 28.8% | 3.48 |
| Auxerre win | 33.2% | 3.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.17 |
| Auxerre expected goals | 1.17 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 68.4% |
| Under 1.5 | 31.6% |
| Over 2.5 | 41.6% |
| Under 2.5 | 58.4% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.54% |
| 2 | 1-0 | 11.48% |
| 3 | 0-1 | 10.04% |
| 4 | 0-0 | 10.03% |
| 5 | 2-1 | 8.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 38.1% | 40.5% | 2.42 | -7.9% |
| Draw | 28.8% | 28.3% | 3.51 | +1.0% |
| Auxerre win | 33.2% | 31.1% | 3.14 | +4.2% |
| Over 2.5 | 41.6% | 51.0% | 1.95 | -18.8% |
| Under 2.5 | 58.4% | 49.0% | 1.99 | +16.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | d637845b9760bb02b55bbbaa32b5c21e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Havre |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.97 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.40 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.78 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.23 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 35.6% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 68.4% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 48.2% |
| P home draw | 66.8% |
| P draw away | 61.9% |
| P home away | 71.2% |
| Raw p home draw | 64.8% |
| Raw p draw away | 64.4% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.40 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:07Z |
| Market reference home last update utc | 2026-10-16T22:16:07Z |
| Market reference draw last update utc | 2026-10-16T22:16:07Z |
| Market reference away last update utc | 2026-10-16T22:16:07Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.94 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:07Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:07Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | -2.5% |
| Draw probability edge | +0.5% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.0498 |
| Raw ev home | -0.1394 |
| Raw edge prob draw | 0.0090 |
| Raw ev draw | 0.0254 |
| Raw edge prob away | 0.0408 |
| Raw ev away | 0.1060 |
| Market p home draw | 68.7% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:16:05Z |
| Market reference home draw last update utc | 2026-10-16T22:16:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.5% |
| Market draw away odds | 1.63 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:16:05Z |
| Market reference draw away last update utc | 2026-10-16T22:16:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.8% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:16:05Z |
| Market reference home away last update utc | 2026-10-16T22:16:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.63 |
| Market reference dc home draw odds | 1.41 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 75.1% |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.56 |
| Market reference over 1 5 last update utc | 2026-10-16T22:16:07Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 72.1% |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.23 |
| Market reference under 3 5 last update utc | 2026-10-16T22:16:07Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 56.8% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:16:05Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-16T22:16:05Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **47.4%**. Expected goals are 1.37 for Lorient and 1.80 for AS Monaco (3.17 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.8%; Under 3.5 goals: 60.9%; Double Chance 1X: 52.6%; Double Chance X2: 73.3%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 78.8%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 26.7% | 3.74 |
| Draw | 25.9% | 3.87 |
| AS Monaco win | 47.4% | 2.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.37 |
| AS Monaco expected goals | 1.80 |
| Expected total goals | 3.17 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 60.8% |
| Under 2.5 | 39.2% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.2% |
| Under 4.5 | 78.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.69% |
| 2 | 1-2 | 9.36% |
| 3 | 0-1 | 7.12% |
| 4 | 2-2 | 6.92% |
| 5 | 0-2 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 26.7% | 24.5% | 3.87 | +3.4% |
| Draw | 25.9% | 27.8% | 3.58 | -7.4% |
| AS Monaco win | 47.4% | 47.6% | 2.10 | -0.4% |
| Over 2.5 | 60.8% | 49.6% | 1.97 | +19.8% |
| Under 2.5 | 39.2% | 50.4% | 1.97 | -22.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:15:00+00:00 |
| Fixture id | 53f5fe7ed0ba0fbf6345c73270e4cd00 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lorient |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.94 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.72 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 28.9% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 47.2% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 62.8% |
| P home draw | 52.6% |
| P draw away | 73.3% |
| P home away | 74.1% |
| Raw p home draw | 52.8% |
| Raw p draw away | 71.1% |
| Raw p home away | 76.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.90 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:07Z |
| Market reference home last update utc | 2026-10-16T22:16:07Z |
| Market reference draw last update utc | 2026-10-16T22:16:07Z |
| Market reference away last update utc | 2026-10-16T22:16:07Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.89 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:07Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:07Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | +2.2% |
| Draw probability edge | -2.0% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +11.3% |
| Under 2.5 probability edge | -11.3% |
| Raw edge prob home | 0.0439 |
| Raw ev home | 0.1190 |
| Raw edge prob draw | -0.0396 |
| Raw ev draw | -0.1454 |
| Raw edge prob away | -0.0043 |
| Raw ev away | -0.0085 |
| Market p home draw | 54.2% |
| Market home draw odds | 1.82 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:16:05Z |
| Market reference home draw last update utc | 2026-10-16T22:16:10Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.3% |
| Market draw away odds | 1.30 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:16:05Z |
| Market reference draw away last update utc | 2026-10-16T22:16:10Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.5% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:16:05Z |
| Market reference home away last update utc | 2026-10-16T22:16:10Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home draw odds | 1.78 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 73.9% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:15:59Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.42 |
| Market reference over 1 5 last update utc | 2026-10-16T22:16:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.3% |
| Market under 3 5 odds | 1.30 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:15:59Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.35 |
| Market reference under 3 5 last update utc | 2026-10-16T22:16:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.9% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:16:05Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-16T22:16:10Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **55.5%**. Expected goals are 1.77 for Lyon and 1.09 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 54.8%; Under 3.5 goals: 67.7%; Double Chance 1X: 79.1%; Double Chance X2: 44.5%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 83.7%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 55.5% | 1.80 |
| Draw | 23.6% | 4.23 |
| Nice win | 20.9% | 4.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.77 |
| Nice expected goals | 1.09 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 54.8% |
| Under 2.5 | 45.2% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.3% |
| Under 4.5 | 83.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.18% |
| 2 | 2-1 | 10.25% |
| 3 | 1-0 | 10.15% |
| 4 | 2-0 | 9.43% |
| 5 | 3-1 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 55.5% | 58.0% | 1.71 | -5.2% |
| Draw | 23.6% | 22.9% | 4.21 | -0.6% |
| Nice win | 20.9% | 19.1% | 5.18 | +8.4% |
| Over 2.5 | 54.8% | 59.3% | 1.72 | -5.8% |
| Under 2.5 | 45.2% | 40.7% | 2.31 | +4.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T18:45:00+00:00 |
| Fixture id | 471f891b1f6516a864ad94c8eb649f5e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lyon |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.57 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.65 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.10 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.13 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 52.9% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| P home draw | 79.1% |
| P draw away | 44.5% |
| P home away | 76.4% |
| Raw p home draw | 77.3% |
| Raw p draw away | 47.1% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.70 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.00 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:07Z |
| Market reference home last update utc | 2026-10-16T22:16:07Z |
| Market reference draw last update utc | 2026-10-16T22:16:07Z |
| Market reference away last update utc | 2026-10-16T22:16:07Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | -2.5% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.0505 |
| Raw ev home | -0.0949 |
| Raw edge prob draw | 0.0145 |
| Raw ev draw | 0.0248 |
| Raw edge prob away | 0.0359 |
| Raw ev away | 0.1774 |
| Market p home draw | 80.9% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:16:05Z |
| Market reference home draw last update utc | 2026-10-16T22:16:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.7% |
| Market draw away odds | 2.27 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:16:05Z |
| Market reference draw away last update utc | 2026-10-16T22:16:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.4% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:16:05Z |
| Market reference home away last update utc | 2026-10-16T22:16:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.27 |
| Market reference dc home draw odds | 1.20 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-16T22:16:07Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.9% |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market reference under 3 5 last update utc | 2026-10-16T22:16:07Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.1% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:16:05Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.13 |
| Market reference btts yes last update utc | 2026-10-16T22:16:05Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **41.5%**. Expected goals are 1.57 for Paris FC and 1.37 for Rennes (2.94 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 55.7%; Under 3.5 goals: 66.1%; Double Chance 1X: 68.6%; Double Chance X2: 58.5%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 59.9%; BTTS No (at least one team does not score): 40.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 41.5% | 2.41 |
| Draw | 27.1% | 3.69 |
| Rennes win | 31.4% | 3.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.57 |
| Rennes expected goals | 1.37 |
| Expected total goals | 2.94 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 55.7% |
| Under 2.5 | 44.3% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.64% |
| 2 | 2-1 | 8.86% |
| 3 | 1-0 | 7.75% |
| 4 | 1-2 | 7.46% |
| 5 | 2-2 | 6.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 41.5% | 41.1% | 2.37 | -1.7% |
| Draw | 27.1% | 28.8% | 3.45 | -6.5% |
| Rennes win | 31.4% | 30.2% | 3.29 | +3.4% |
| Over 2.5 | 55.7% | 59.3% | 1.72 | -4.1% |
| Under 2.5 | 44.3% | 40.7% | 2.30 | +1.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | 27f7222d2abde93fc6e8d17b5b05b272 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paris FC |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.9% |
| P btts no | 40.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.23 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.80 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 41.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.1% |
| Raw p btts yes | 59.5% |
| P home draw | 68.6% |
| P draw away | 58.5% |
| P home away | 72.9% |
| Raw p home draw | 67.3% |
| Raw p draw away | 58.1% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.37 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:07Z |
| Market reference home last update utc | 2026-10-16T22:16:07Z |
| Market reference draw last update utc | 2026-10-16T22:16:07Z |
| Market reference away last update utc | 2026-10-16T22:16:07Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | +0.4% |
| Draw probability edge | -1.7% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | 0.0080 |
| Raw ev home | -0.0072 |
| Raw edge prob draw | -0.0334 |
| Raw ev draw | -0.1229 |
| Raw edge prob away | 0.0254 |
| Raw ev away | 0.0754 |
| Market p home draw | 69.9% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:16:05Z |
| Market reference home draw last update utc | 2026-10-16T22:16:05Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.6% |
| Market draw away odds | 1.66 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:16:05Z |
| Market reference draw away last update utc | 2026-10-16T22:16:05Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.5% |
| Market home away odds | 1.36 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:16:05Z |
| Market reference home away last update utc | 2026-10-16T22:16:05Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.66 |
| Market reference dc home draw odds | 1.39 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-16T22:16:07Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.9% |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market reference under 3 5 last update utc | 2026-10-16T22:16:07Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 62.9% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:16:05Z |
| Market reference btts yes odds | 1.51 |
| Market reference btts yes opposite odds | 2.42 |
| Market reference btts yes last update utc | 2026-10-16T22:16:05Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **43.3%**. Expected goals are 1.56 for Brest and 1.28 for Nice (2.84 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 53.5%; Under 3.5 goals: 68.4%; Double Chance 1X: 70.2%; Double Chance X2: 56.7%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 43.3% | 2.31 |
| Draw | 26.9% | 3.72 |
| Nice win | 29.8% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Nice expected goals | 1.28 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.5% |
| Under 2.5 | 46.5% |
| Over 3.5 | 31.6% |
| Under 3.5 | 68.4% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.69% |
| 2 | 2-1 | 9.07% |
| 3 | 1-0 | 8.61% |
| 4 | 1-2 | 7.23% |
| 5 | 2-0 | 7.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 43.3% | 43.1% | 2.31 | -0.1% |
| Draw | 26.9% | 28.0% | 3.49 | -6.1% |
| Nice win | 29.8% | 28.9% | 3.37 | +0.6% |
| Over 2.5 | 53.5% | 58.9% | 1.76 | -5.8% |
| Under 2.5 | 46.5% | 41.1% | 2.23 | +3.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 8aa36b30d655d6c81ed98bf9ec1b4039 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brest |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.07 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.17 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.39 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.5% |
| P home draw | 70.2% |
| P draw away | 56.7% |
| P home away | 73.1% |
| Raw p home draw | 69.2% |
| Raw p draw away | 56.6% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.20 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:05Z |
| Market reference home last update utc | 2026-10-16T22:16:05Z |
| Market reference draw last update utc | 2026-10-16T22:16:05Z |
| Market reference away last update utc | 2026-10-16T22:16:05Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | +0.1% |
| Draw probability edge | -1.1% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | 0.0028 |
| Raw ev home | 0.0025 |
| Raw edge prob draw | -0.0215 |
| Raw ev draw | -0.0986 |
| Raw edge prob away | 0.0186 |
| Raw ev away | 0.0370 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **48.9%**. Expected goals are 1.59 for RC Lens and 1.00 for Paris FC (2.58 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 47.8%; Under 3.5 goals: 74.0%; Double Chance 1X: 74.6%; Double Chance X2: 51.1%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 48.9% | 2.04 |
| Draw | 25.7% | 3.89 |
| Paris FC win | 25.4% | 3.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.59 |
| Paris FC expected goals | 1.00 |
| Expected total goals | 2.58 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 73.4% |
| Under 1.5 | 26.6% |
| Over 2.5 | 47.8% |
| Under 2.5 | 52.2% |
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.23% |
| 2 | 1-0 | 11.09% |
| 3 | 2-0 | 9.19% |
| 4 | 2-1 | 9.18% |
| 5 | 0-0 | 7.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 48.9% | 47.4% | 2.09 | +2.3% |
| Draw | 25.7% | 25.2% | 3.90 | +0.1% |
| Paris FC win | 25.4% | 27.5% | 3.58 | -9.1% |
| Over 2.5 | 47.8% | 58.8% | 1.68 | -19.6% |
| Under 2.5 | 52.2% | 41.2% | 2.38 | +24.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | fc6c50376190b578cfeb38c029db8487 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.64 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.75 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.31 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 50.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.3% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.9% |
| Raw p btts yes | 50.7% |
| P home draw | 74.6% |
| P draw away | 51.1% |
| P home away | 74.3% |
| Raw p home draw | 76.7% |
| Raw p draw away | 49.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.09 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.58 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:05Z |
| Market reference home last update utc | 2026-10-16T22:16:05Z |
| Market reference draw last update utc | 2026-10-16T22:16:05Z |
| Market reference away last update utc | 2026-10-16T22:16:05Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | +1.6% |
| Draw probability edge | +0.5% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.0313 |
| Raw ev home | 0.0555 |
| Raw edge prob draw | 0.0100 |
| Raw ev draw | 0.0209 |
| Raw edge prob away | -0.0413 |
| Raw ev away | -0.1651 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **65.7%**. Expected goals are 2.29 for Toulouse and 0.62 for Troyes (2.91 combined). The most likely exact score is 2-0 at 12.5%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 53.4%; Under 3.5 goals: 68.5%; Double Chance 1X: 85.9%; Double Chance X2: 34.3%; Double Chance 12 (either team wins): 79.8%; Under 4.5 goals: 84.1%; BTTS Yes (both teams score): 43.6%; BTTS No (at least one team does not score): 56.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 65.7% | 1.52 |
| Draw | 20.2% | 4.95 |
| Troyes win | 14.1% | 7.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 2.29 |
| Troyes expected goals | 0.62 |
| Expected total goals | 2.91 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 53.4% |
| Under 2.5 | 46.6% |
| Over 3.5 | 31.5% |
| Under 3.5 | 68.5% |
| Over 4.5 | 15.9% |
| Under 4.5 | 84.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.50% |
| 2 | 1-0 | 10.62% |
| 3 | 1-1 | 9.55% |
| 4 | 3-0 | 9.55% |
| 5 | 2-1 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 65.7% | 56.7% | 1.75 | +15.0% |
| Draw | 20.2% | 23.3% | 4.21 | -15.0% |
| Troyes win | 14.1% | 20.0% | 4.88 | -31.3% |
| Over 2.5 | 53.4% | 58.5% | 1.69 | -9.7% |
| Under 2.5 | 46.6% | 41.5% | 2.36 | +9.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T15:15:00+00:00 |
| Fixture id | 0bbce95e5764e706e6c428bb52dc5536 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 43.6% |
| P btts no | 56.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.71 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.17 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.30 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 74.8% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 66.6% |
| Raw p btts yes | 42.1% |
| P home draw | 85.9% |
| P draw away | 34.3% |
| P home away | 79.8% |
| Raw p home draw | 91.9% |
| Raw p draw away | 25.2% |
| Raw p home away | 82.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.75 |
| Reference draw odds | 4.21 |
| Reference away odds | 4.88 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:05Z |
| Market reference home last update utc | 2026-10-16T22:16:05Z |
| Market reference draw last update utc | 2026-10-16T22:16:05Z |
| Market reference away last update utc | 2026-10-16T22:16:05Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | +9.0% |
| Draw probability edge | -3.1% |
| Away probability edge | -5.9% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | 0.1807 |
| Raw ev home | 0.3083 |
| Raw edge prob draw | -0.0617 |
| Raw ev draw | -0.2801 |
| Raw edge prob away | -0.1190 |
| Raw ev away | -0.6028 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **43.4%**. Expected goals are 1.47 for AS Monaco and 1.26 for Lille (2.73 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 51.3%; Under 3.5 goals: 70.7%; Double Chance 1X: 70.3%; Double Chance X2: 56.6%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.8%; BTTS No (at least one team does not score): 44.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 43.4% | 2.30 |
| Draw | 26.9% | 3.71 |
| Lille win | 29.7% | 3.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.47 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.73 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 76.2% |
| Under 1.5 | 23.8% |
| Over 2.5 | 51.3% |
| Under 2.5 | 48.7% |
| Over 3.5 | 29.3% |
| Under 3.5 | 70.7% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.79% |
| 2 | 1-0 | 9.49% |
| 3 | 2-1 | 9.29% |
| 4 | 2-0 | 7.36% |
| 5 | 0-0 | 7.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 43.4% | 45.4% | 2.18 | -5.4% |
| Draw | 26.9% | 27.3% | 3.60 | -3.1% |
| Lille win | 29.7% | 27.3% | 3.60 | +6.8% |
| Over 2.5 | 51.3% | 55.8% | 1.77 | -9.3% |
| Under 2.5 | 48.7% | 44.2% | 2.22 | +8.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | c177a3c900d7febf9870ca8de90a9e35 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monaco |
| Matched away-team name | Lille |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.8% |
| P btts no | 44.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.99 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.21 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.42 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.08 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 41.4% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 32.0% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.8% |
| Raw p btts yes | 55.7% |
| P home draw | 70.3% |
| P draw away | 56.6% |
| P home away | 73.1% |
| Raw p home draw | 68.0% |
| Raw p draw away | 58.6% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.18 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:05Z |
| Market reference home last update utc | 2026-10-16T22:16:05Z |
| Market reference draw last update utc | 2026-10-16T22:16:05Z |
| Market reference away last update utc | 2026-10-16T22:16:05Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | -2.0% |
| Draw probability edge | -0.4% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | -0.0399 |
| Raw ev home | -0.0973 |
| Raw edge prob draw | -0.0075 |
| Raw ev draw | -0.0442 |
| Raw edge prob away | 0.0474 |
| Raw ev away | 0.1536 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **36.8%**. Expected goals are 1.09 for Angers and 1.24 for Lorient (2.33 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.3%; Double Chance 1X: 63.2%; Double Chance X2: 65.8%; Double Chance 12 (either team wins): 71.0%; Under 4.5 goals: 91.2%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 34.2% | 2.92 |
| Draw | 29.0% | 3.45 |
| Lorient win | 36.8% | 2.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.09 |
| Lorient expected goals | 1.24 |
| Expected total goals | 2.33 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 68.2% |
| Under 1.5 | 31.8% |
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
| Over 3.5 | 20.7% |
| Under 3.5 | 79.3% |
| Over 4.5 | 8.8% |
| Under 4.5 | 91.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.64% |
| 2 | 0-1 | 10.79% |
| 3 | 1-0 | 10.78% |
| 4 | 0-0 | 10.21% |
| 5 | 2-1 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 34.2% | 36.6% | 2.69 | -8.0% |
| Draw | 29.0% | 28.9% | 3.40 | -1.4% |
| Lorient win | 36.8% | 34.5% | 2.85 | +4.8% |
| Over 2.5 | 41.3% | 44.9% | 2.19 | -9.5% |
| Under 2.5 | 58.7% | 55.1% | 1.79 | +5.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 1a83b5ebabe7cb572ae6e029b3149c42 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Lorient |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.79 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.15 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.83 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.40 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 31.8% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 68.3% |
| Raw p under 3 5 | 79.2% |
| Raw p btts yes | 47.8% |
| P home draw | 63.2% |
| P draw away | 65.8% |
| P home away | 71.0% |
| Raw p home draw | 61.0% |
| Raw p draw away | 68.2% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.69 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.85 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:05Z |
| Market reference home last update utc | 2026-10-16T22:16:05Z |
| Market reference draw last update utc | 2026-10-16T22:16:05Z |
| Market reference away last update utc | 2026-10-16T22:16:05Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.19 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | -2.4% |
| Draw probability edge | +0.2% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | -0.0482 |
| Raw ev home | -0.1447 |
| Raw edge prob draw | 0.0030 |
| Raw ev draw | -0.0084 |
| Raw edge prob away | 0.0451 |
| Raw ev away | 0.1126 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **42.1%**. Expected goals are 1.64 for Auxerre and 1.66 for Le Mans FC (3.30 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 63.8%; Under 3.5 goals: 58.2%; Double Chance 1X: 66.4%; Double Chance X2: 57.9%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 76.4%; BTTS Yes (both teams score): 65.7%; BTTS No (at least one team does not score): 34.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 42.1% | 2.38 |
| Draw | 24.3% | 4.11 |
| Le Mans FC win | 33.6% | 2.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.64 |
| Le Mans FC expected goals | 1.66 |
| Expected total goals | 3.30 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 84.5% |
| Under 1.5 | 15.5% |
| Over 2.5 | 63.8% |
| Under 2.5 | 36.2% |
| Over 3.5 | 41.8% |
| Under 3.5 | 58.2% |
| Over 4.5 | 23.6% |
| Under 4.5 | 76.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.67% |
| 2 | 2-1 | 9.20% |
| 3 | 1-2 | 7.29% |
| 4 | 2-2 | 6.94% |
| 5 | 1-0 | 6.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 42.1% | 46.4% | 2.23 | -6.2% |
| Draw | 24.3% | 24.7% | 3.70 | -10.0% |
| Le Mans FC win | 33.6% | 28.9% | 3.37 | +13.3% |
| Over 2.5 | 63.8% | 56.9% | 1.78 | +13.6% |
| Under 2.5 | 36.2% | 43.1% | 2.20 | -20.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 8eab078a37a63df32ffa443302a2a7ba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 65.7% |
| P btts no | 34.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.75 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.45 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.76 |
| Fair Over 3.5 odds | 2.39 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.24 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 37.7% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 84.5% |
| Raw p under 3 5 | 58.1% |
| Raw p btts yes | 65.6% |
| P home draw | 66.4% |
| P draw away | 57.9% |
| P home away | 75.7% |
| Raw p home draw | 61.6% |
| Raw p draw away | 62.3% |
| Raw p home away | 76.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.05 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:05Z |
| Market reference home last update utc | 2026-10-16T22:16:05Z |
| Market reference draw last update utc | 2026-10-16T22:16:05Z |
| Market reference away last update utc | 2026-10-16T22:16:05Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | -4.4% |
| Draw probability edge | -0.4% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | +6.9% |
| Under 2.5 probability edge | -6.9% |
| Raw edge prob home | -0.0872 |
| Raw ev home | -0.1590 |
| Raw edge prob draw | -0.0079 |
| Raw ev draw | -0.1152 |
| Raw edge prob away | 0.0952 |
| Raw ev away | 0.2931 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **63.4%**. Expected goals are 2.14 for Marseille and 0.86 for Le Havre (2.99 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 57.1%; Under 3.5 goals: 65.3%; Double Chance 1X: 84.1%; Double Chance X2: 36.6%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 63.4% | 1.58 |
| Draw | 20.7% | 4.82 |
| Le Havre win | 15.9% | 6.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.14 |
| Le Havre expected goals | 0.86 |
| Expected total goals | 2.99 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 80.0% |
| Under 1.5 | 20.0% |
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.92% |
| 2 | 1-1 | 9.86% |
| 3 | 1-0 | 9.85% |
| 4 | 2-1 | 9.37% |
| 5 | 3-0 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 63.4% | 60.5% | 1.64 | +3.9% |
| Draw | 20.7% | 21.3% | 4.57 | -5.2% |
| Le Havre win | 15.9% | 18.2% | 5.33 | -15.4% |
| Over 2.5 | 57.1% | 59.5% | 1.66 | -5.3% |
| Under 2.5 | 42.9% | 40.5% | 2.42 | +3.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | fcc34b753fc61a0cc0e11d7cb0a0c36b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.97 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.00 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.53 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 66.3% |
| Unadjusted draw probability | 20.2% |
| Unadjusted away-win probability | 13.5% |
| Raw p over 1 5 | 80.4% |
| Raw p under 3 5 | 64.9% |
| Raw p btts yes | 51.2% |
| P home draw | 84.1% |
| P draw away | 36.6% |
| P home away | 79.3% |
| Raw p home draw | 86.5% |
| Raw p draw away | 33.7% |
| Raw p home away | 79.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.64 |
| Reference draw odds | 4.57 |
| Reference away odds | 5.33 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:05Z |
| Market reference home last update utc | 2026-10-16T22:16:05Z |
| Market reference draw last update utc | 2026-10-16T22:16:05Z |
| Market reference away last update utc | 2026-10-16T22:16:05Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | +2.9% |
| Draw probability edge | -0.6% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | 0.0585 |
| Raw ev home | 0.0874 |
| Raw edge prob draw | -0.0115 |
| Raw ev draw | -0.0785 |
| Raw edge prob away | -0.0470 |
| Raw ev away | -0.2787 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **69.2%**. Expected goals are 2.31 for Paris Saint Germain and 1.06 for Lyon (3.37 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 66.4%; Under 3.5 goals: 55.9%; Double Chance 1X: 86.3%; Double Chance X2: 30.8%; Double Chance 12 (either team wins): 82.9%; Under 4.5 goals: 74.4%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 69.2% | 1.45 |
| Draw | 17.1% | 5.84 |
| Lyon win | 13.7% | 7.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.31 |
| Lyon expected goals | 1.06 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 85.7% |
| Under 1.5 | 14.3% |
| Over 2.5 | 66.4% |
| Under 2.5 | 33.6% |
| Over 3.5 | 44.1% |
| Under 3.5 | 55.9% |
| Over 4.5 | 25.6% |
| Under 4.5 | 74.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.33% |
| 2 | 2-0 | 9.78% |
| 3 | 1-0 | 8.07% |
| 4 | 3-1 | 7.96% |
| 5 | 1-1 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 69.2% | 73.2% | 1.43 | -1.1% |
| Draw | 17.1% | 14.9% | 5.44 | -6.9% |
| Lyon win | 13.7% | 11.9% | 7.60 | +4.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 8664b2167f22c59026d86615421463b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.68 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.98 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.98 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.90 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 65.1% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 15.5% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 56.5% |
| Raw p btts yes | 59.1% |
| P home draw | 86.3% |
| P draw away | 30.8% |
| P home away | 82.9% |
| Raw p home draw | 84.5% |
| Raw p draw away | 34.9% |
| Raw p home away | 80.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.33 |
| Reference draw odds | 5.70 |
| Reference away odds | 7.00 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:05Z |
| Market reference home last update utc | 2026-10-16T22:16:05Z |
| Market reference draw last update utc | 2026-10-16T22:16:05Z |
| Market reference away last update utc | 2026-10-16T22:16:05Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | -4.0% |
| Draw probability edge | +2.2% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | -0.0810 |
| Raw ev home | -0.0690 |
| Raw edge prob draw | 0.0445 |
| Raw ev draw | 0.0525 |
| Raw edge prob away | 0.0365 |
| Raw ev away | 0.1817 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **53.3%**. Expected goals are 1.86 for Rennes and 1.48 for Strasbourg (3.34 combined). The most likely exact score is 2-1 at 10.4%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 65.7%; Under 3.5 goals: 56.7%; Double Chance 1X: 74.6%; Double Chance X2: 46.7%; Double Chance 12 (either team wins): 78.7%; Under 4.5 goals: 75.0%; BTTS Yes (both teams score): 65.1%; BTTS No (at least one team does not score): 34.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 53.3% | 1.88 |
| Draw | 21.3% | 4.69 |
| Strasbourg win | 25.4% | 3.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.86 |
| Strasbourg expected goals | 1.48 |
| Expected total goals | 3.34 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.7% |
| Under 2.5 | 34.3% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.44% |
| 2 | 1-1 | 9.31% |
| 3 | 1-0 | 7.08% |
| 4 | 2-0 | 7.05% |
| 5 | 3-1 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 53.3% | 60.3% | 1.70 | -9.4% |
| Draw | 21.3% | 19.4% | 4.57 | -2.5% |
| Strasbourg win | 25.4% | 20.3% | 4.83 | +22.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 31dcb6d13ed240fc4a5c7a696149967e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.1% |
| P btts no | 34.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.63 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.80 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.92 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 3.99 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 46.3% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 57.1% |
| Raw p btts yes | 65.7% |
| P home draw | 74.6% |
| P draw away | 46.7% |
| P home away | 78.7% |
| Raw p home draw | 69.6% |
| Raw p draw away | 53.7% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.60 |
| Reference draw odds | 4.60 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:05Z |
| Market reference home last update utc | 2026-10-16T22:16:05Z |
| Market reference draw last update utc | 2026-10-16T22:16:05Z |
| Market reference away last update utc | 2026-10-16T22:16:05Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | -7.0% |
| Draw probability edge | +2.0% |
| Away probability edge | +5.0% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | -0.1399 |
| Raw ev home | -0.2124 |
| Raw edge prob draw | 0.0392 |
| Raw ev draw | 0.0641 |
| Raw edge prob away | 0.1007 |
| Raw ev away | 0.4676 |

</details>


---
