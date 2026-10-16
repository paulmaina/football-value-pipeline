# Bundesliga — football model report

Fixtures in this report: **17**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 964 |
| Training data through | 2026-10-16 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | 54f566b5dfa1cca1a8776de709b4bfb97dce599e23b6f33ce4d7f946c9dd9d29 |
| Optimizer objective | 2920.827 |
| Base scoring parameter | 0.233 |
| Home-advantage parameter | 0.194 |
| Dixon-Coles low-score adjustment | -0.099 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-16', 'days_since_latest_result': 0, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 17.00 |
| Additional event odds calls used before this league | 19.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **74.4%**. Expected goals are 2.75 for Bayern Munich and 1.27 for RB Leipzig (4.02 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 77.9%; Under 3.5 goals: 42.0%; Double Chance 1X: 88.5%; Double Chance X2: 25.6%; Double Chance 12 (either team wins): 86.0%; Under 4.5 goals: 61.2%; BTTS Yes (both teams score): 66.7%; BTTS No (at least one team does not score): 33.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 74.4% | 1.34 |
| Draw | 14.0% | 7.12 |
| RB Leipzig win | 11.5% | 8.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.75 |
| RB Leipzig expected goals | 1.27 |
| Expected total goals | 4.02 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 77.9% |
| Under 2.5 | 22.1% |
| Over 3.5 | 58.0% |
| Under 3.5 | 42.0% |
| Over 4.5 | 38.8% |
| Under 4.5 | 61.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.44% |
| 2 | 3-1 | 8.66% |
| 3 | 2-0 | 7.45% |
| 4 | 3-0 | 6.83% |
| 5 | 4-1 | 5.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 74.4% | 80.9% | 1.26 | -6.2% |
| Draw | 14.0% | 10.7% | 7.60 | +6.7% |
| RB Leipzig win | 11.5% | 8.4% | 11.10 | +28.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | 9a64448205fdc4b95f45641bb946706c |
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
| Matched home-team name | Bayern Munich |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 66.7% |
| P btts no | 33.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 51.36 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.52 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.52 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.38 |
| Fair Over 4.5 odds | 2.58 |
| Fair Under 4.5 odds | 1.63 |
| Unadjusted home-win probability | 67.9% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 14.6% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 43.0% |
| Raw p btts yes | 67.9% |
| P home draw | 88.5% |
| P draw away | 25.6% |
| P home away | 86.0% |
| Raw p home draw | 85.4% |
| Raw p draw away | 32.1% |
| Raw p home away | 82.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.22 |
| Reference draw odds | 8.17 |
| Reference away odds | 10.18 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.80 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | -6.5% |
| Draw probability edge | +3.4% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | -0.1295 |
| Raw ev home | -0.1438 |
| Raw edge prob draw | 0.0675 |
| Raw ev draw | 0.3235 |
| Raw edge prob away | 0.0620 |
| Raw ev away | 0.6246 |
| Market p home draw | 90.4% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 20.9% |
| Market draw away odds | 4.32 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.7% |
| Market home away odds | 1.12 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.67 |
| Market reference dc home draw odds | 1.08 |
| Market reference dc home away odds | 1.10 |
| Market p over 1 5 | 96.4% |
| Market over 1 5 odds | 1.03 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:15:30Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 15.00 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 29.0% |
| Market under 3 5 odds | 2.94 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:15:30Z |
| Market reference under 3 5 odds | 3.13 |
| Market reference under 3 5 opposite odds | 1.37 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.36 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 3.15 |
| Market reference btts yes last update utc | 2026-10-16T22:15:48Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **49.1%**. Expected goals are 2.11 for Elversberg and 1.14 for Augsburg (3.25 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 62.1%; Under 3.5 goals: 60.1%; Double Chance 1X: 72.9%; Double Chance X2: 50.9%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 61.7%; BTTS No (at least one team does not score): 38.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 49.1% | 2.04 |
| Draw | 23.9% | 4.19 |
| Augsburg win | 27.1% | 3.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.11 |
| Augsburg expected goals | 1.14 |
| Expected total goals | 3.25 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 83.8% |
| Under 1.5 | 16.2% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 39.9% |
| Under 3.5 | 60.1% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.91% |
| 2 | 2-1 | 8.22% |
| 3 | 1-2 | 7.61% |
| 4 | 2-0 | 7.21% |
| 5 | 1-0 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 49.1% | 39.4% | 2.55 | +25.2% |
| Draw | 23.9% | 25.3% | 3.92 | -6.5% |
| Augsburg win | 27.1% | 35.3% | 2.71 | -26.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 0bf757f3bd903496ce2fa27bd0481869 |
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
| Matched home-team name | Elversberg |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.7% |
| P btts no | 38.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.59 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.19 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.52 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 18.8% |
| Raw p over 1 5 | 84.5% |
| Raw p under 3 5 | 59.1% |
| Raw p btts yes | 60.7% |
| P home draw | 72.9% |
| P draw away | 50.9% |
| P home away | 76.1% |
| Raw p home draw | 81.2% |
| Raw p draw away | 41.2% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.47 |
| Reference draw odds | 3.79 |
| Reference away odds | 2.75 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | +9.7% |
| Draw probability edge | -1.5% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | 0.1940 |
| Raw ev home | 0.4991 |
| Raw edge prob draw | -0.0298 |
| Raw ev draw | -0.1233 |
| Raw edge prob away | -0.1642 |
| Raw ev away | -0.4893 |
| Market p home draw | 64.9% |
| Market home draw odds | 1.52 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.8% |
| Market draw away odds | 1.58 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.3% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.59 |
| Market reference dc home draw odds | 1.49 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 87.6% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:35Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 54.4% |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:35Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 70.3% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.39 |
| Market reference btts yes opposite odds | 3.12 |
| Market reference btts yes last update utc | 2026-10-16T22:15:46Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **36.9%**. Expected goals are 0.94 for FC Schalke 04 and 0.90 for FSV Mainz 05 (1.84 combined). The most likely exact score is 0-1 at 15.2%. Goal-market probabilities: at least one goal: 84.9%; Over 2.5 goals: 29.3%; Under 3.5 goals: 88.3%; Double Chance 1X: 63.1%; Double Chance X2: 67.7%; Double Chance 12 (either team wins): 69.2%; Under 4.5 goals: 95.9%; BTTS Yes (both teams score): 36.6%; BTTS No (at least one team does not score): 63.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 32.3% | 3.10 |
| Draw | 30.8% | 3.25 |
| FSV Mainz 05 win | 36.9% | 2.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.94 |
| FSV Mainz 05 expected goals | 0.90 |
| Expected total goals | 1.84 |
| Over 0.5 | 84.9% |
| Under 0.5 | 15.1% |
| Over 1.5 | 56.5% |
| Under 1.5 | 43.5% |
| Over 2.5 | 29.3% |
| Under 2.5 | 70.7% |
| Over 3.5 | 11.7% |
| Under 3.5 | 88.3% |
| Over 4.5 | 4.1% |
| Under 4.5 | 95.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.25% |
| 2 | 0-0 | 15.10% |
| 3 | 1-0 | 13.12% |
| 4 | 1-1 | 12.94% |
| 5 | 0-2 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 32.3% | 31.2% | 3.16 | +2.1% |
| Draw | 30.8% | 26.4% | 3.67 | +12.9% |
| FSV Mainz 05 win | 36.9% | 42.3% | 2.34 | -13.6% |
| Over 2.5 | 29.3% | 58.9% | 1.70 | -50.3% |
| Under 2.5 | 70.7% | 41.1% | 2.34 | +65.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 606d65d57a9a6d8f9b53faee1ad10009 |
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
| Matched home-team name | Schalke 04 |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 36.6% |
| P btts no | 63.4% |
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.62 |
| Fair Over 1.5 odds | 1.77 |
| Fair Under 1.5 odds | 2.30 |
| Fair Over 2.5 odds | 3.42 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.57 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.17 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 33.4% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 31.5% |
| Raw p over 1 5 | 56.2% |
| Raw p under 3 5 | 88.5% |
| Raw p btts yes | 37.5% |
| P home draw | 63.1% |
| P draw away | 67.7% |
| P home away | 69.2% |
| Raw p home draw | 68.5% |
| Raw p draw away | 66.6% |
| Raw p home away | 64.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.09 |
| Reference draw odds | 3.63 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | +1.1% |
| Draw probability edge | +4.3% |
| Away probability edge | -5.4% |
| Over 2.5 probability edge | -29.7% |
| Under 2.5 probability edge | +29.7% |
| Raw edge prob home | 0.0217 |
| Raw ev home | 0.0552 |
| Raw edge prob draw | 0.0867 |
| Raw ev draw | 0.2886 |
| Raw edge prob away | -0.1085 |
| Raw ev away | -0.2630 |
| Market p home draw | 58.0% |
| Market home draw odds | 1.67 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.7% |
| Market draw away odds | 1.41 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.4% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home draw odds | 1.67 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 83.0% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:35Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.7% |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:35Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 63.6% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.58 |
| Market reference btts yes last update utc | 2026-10-16T22:15:46Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **55.3%**. Expected goals are 1.15 for Hamburger SV and 2.01 for VfB Stuttgart (3.16 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 61.2%; Under 3.5 goals: 61.2%; Double Chance 1X: 44.7%; Double Chance X2: 78.7%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 78.8%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 21.3% | 4.70 |
| Draw | 23.4% | 4.28 |
| VfB Stuttgart win | 55.3% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.15 |
| VfB Stuttgart expected goals | 2.01 |
| Expected total goals | 3.16 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 61.2% |
| Under 2.5 | 38.8% |
| Over 3.5 | 38.8% |
| Under 3.5 | 61.2% |
| Over 4.5 | 21.2% |
| Under 4.5 | 78.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.79% |
| 2 | 1-2 | 9.69% |
| 3 | 0-2 | 8.41% |
| 4 | 0-1 | 7.42% |
| 5 | 1-3 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 21.3% | 22.2% | 4.45 | -5.3% |
| Draw | 23.4% | 23.4% | 4.11 | -3.9% |
| VfB Stuttgart win | 55.3% | 54.4% | 1.83 | +1.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 221916b8b36706ec52aa655a64e5f1d2 |
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
| Matched home-team name | Hamburg |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 88/100 |
| Away-name matching confidence | 95/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.18 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.99 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.57 |
| Fair Over 3.5 odds | 2.58 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.71 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 20.4% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 56.3% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 60.2% |
| P home draw | 44.7% |
| P draw away | 78.7% |
| P home away | 76.6% |
| Raw p home draw | 43.7% |
| Raw p draw away | 79.6% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.28 |
| Reference draw odds | 4.06 |
| Reference away odds | 1.80 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | -0.9% |
| Draw probability edge | -0.0% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.0180 |
| Raw ev home | -0.0931 |
| Raw edge prob draw | -0.0008 |
| Raw ev draw | -0.0407 |
| Raw edge prob away | 0.0188 |
| Raw ev away | 0.0299 |
| Market p home draw | 46.2% |
| Market home draw odds | 2.09 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 77.5% |
| Market draw away odds | 1.25 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.25 |
| Market reference dc home draw odds | 2.10 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.0% |
| Market under 3 5 odds | 1.90 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:15:06Z |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 2.02 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.2% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 3.10 |
| Market reference btts yes last update utc | 2026-10-16T22:15:48Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **59.5%**. Expected goals are 0.94 for Union Berlin and 1.89 for Borussia Dortmund (2.84 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 54.5%; Under 3.5 goals: 68.2%; Double Chance 1X: 40.5%; Double Chance X2: 82.1%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 52.6%; BTTS No (at least one team does not score): 47.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.9% | 5.59 |
| Draw | 22.6% | 4.43 |
| Borussia Dortmund win | 59.5% | 1.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.89 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 78.7% |
| Under 1.5 | 21.3% |
| Over 2.5 | 54.5% |
| Under 2.5 | 45.5% |
| Over 3.5 | 31.8% |
| Under 3.5 | 68.2% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.77% |
| 2 | 0-2 | 10.67% |
| 3 | 0-1 | 10.23% |
| 4 | 1-2 | 10.08% |
| 5 | 0-3 | 6.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.9% | 18.5% | 5.34 | -4.4% |
| Draw | 22.6% | 21.0% | 4.62 | +4.3% |
| Borussia Dortmund win | 59.5% | 60.5% | 1.63 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | d8eac776adb07b0e7f01d8736d097291 |
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
| Matched home-team name | Union Berlin |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 52.6% |
| P btts no | 47.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.50 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.69 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.24 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 58.5% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 52.9% |
| P home draw | 40.5% |
| P draw away | 82.1% |
| P home away | 77.4% |
| Raw p home draw | 41.5% |
| Raw p draw away | 82.7% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.07 |
| Reference draw odds | 4.48 |
| Reference away odds | 1.62 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | -0.6% |
| Draw probability edge | +1.6% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.0114 |
| Raw ev home | -0.0747 |
| Raw edge prob draw | 0.0314 |
| Raw ev draw | 0.1152 |
| Raw edge prob away | -0.0200 |
| Raw ev away | -0.0459 |
| Market p home draw | 40.4% |
| Market home draw odds | 2.42 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.8% |
| Market draw away odds | 1.19 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.8% |
| Market home away odds | 1.24 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.20 |
| Market reference dc home draw odds | 2.40 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 85.4% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:14:14Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.4% |
| Market under 3 5 odds | 1.72 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:14:14Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.7% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-16T22:15:48Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **53.1%**. Expected goals are 1.27 for Werder Bremen and 0.60 for SC Paderborn (1.87 combined). The most likely exact score is 1-0 at 18.9%. Goal-market probabilities: at least one goal: 85.9%; Over 2.5 goals: 30.2%; Under 3.5 goals: 87.8%; Double Chance 1X: 80.2%; Double Chance X2: 46.9%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 95.6%; BTTS Yes (both teams score): 32.7%; BTTS No (at least one team does not score): 67.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 53.1% | 1.88 |
| Draw | 27.1% | 3.69 |
| SC Paderborn win | 19.8% | 5.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.27 |
| SC Paderborn expected goals | 0.60 |
| Expected total goals | 1.87 |
| Over 0.5 | 85.9% |
| Under 0.5 | 14.1% |
| Over 1.5 | 57.3% |
| Under 1.5 | 42.7% |
| Over 2.5 | 30.2% |
| Under 2.5 | 69.8% |
| Over 3.5 | 12.2% |
| Under 3.5 | 87.8% |
| Over 4.5 | 4.4% |
| Under 4.5 | 95.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 18.89% |
| 2 | 0-0 | 14.07% |
| 3 | 2-0 | 12.77% |
| 4 | 1-1 | 10.96% |
| 5 | 0-1 | 9.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 53.1% | 54.4% | 1.84 | -2.4% |
| Draw | 27.1% | 22.3% | 4.26 | +15.5% |
| SC Paderborn win | 19.8% | 23.3% | 4.21 | -16.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 9a422e1aad1053828eaf629a58d901de |
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
| Matched home-team name | Werder Bremen |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 32.7% |
| P btts no | 67.3% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.10 |
| Fair Over 1.5 odds | 1.75 |
| Fair Under 1.5 odds | 2.34 |
| Fair Over 2.5 odds | 3.31 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 8.20 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 22.85 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 51.7% |
| Unadjusted draw probability | 31.9% |
| Unadjusted away-win probability | 16.4% |
| Raw p over 1 5 | 57.0% |
| Raw p under 3 5 | 88.0% |
| Raw p btts yes | 33.6% |
| P home draw | 80.2% |
| P draw away | 46.9% |
| P home away | 72.9% |
| Raw p home draw | 83.6% |
| Raw p draw away | 48.3% |
| Raw p home away | 68.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.80 |
| Reference draw odds | 4.25 |
| Reference away odds | 4.08 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | -1.3% |
| Draw probability edge | +4.8% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -33.6% |
| Under 2.5 probability edge | +33.6% |
| Raw edge prob home | -0.0266 |
| Raw ev home | -0.0482 |
| Raw edge prob draw | 0.0957 |
| Raw ev draw | 0.3587 |
| Raw edge prob away | -0.0691 |
| Raw ev away | -0.3104 |
| Market p home draw | 76.2% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.3% |
| Market draw away odds | 2.07 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.4% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.09 |
| Market reference dc home draw odds | 1.27 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 84.9% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:15:32Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.0% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:15:32Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.38 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.4% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.52 |
| Market reference btts yes last update utc | 2026-10-16T22:15:46Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **63.2%**. Expected goals are 2.47 for Bayer Leverkusen and 0.98 for SC Freiburg (3.46 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 66.0%; Under 3.5 goals: 55.7%; Double Chance 1X: 83.4%; Double Chance X2: 36.8%; Double Chance 12 (either team wins): 79.8%; Under 4.5 goals: 74.2%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 63.2% | 1.58 |
| Draw | 20.2% | 4.95 |
| SC Freiburg win | 16.6% | 6.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.47 |
| SC Freiburg expected goals | 0.98 |
| Expected total goals | 3.46 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 66.0% |
| Under 2.5 | 34.0% |
| Over 3.5 | 44.3% |
| Under 3.5 | 55.7% |
| Over 4.5 | 25.8% |
| Under 4.5 | 74.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.21% |
| 2 | 2-0 | 8.81% |
| 3 | 2-1 | 8.66% |
| 4 | 3-0 | 7.26% |
| 5 | 3-1 | 7.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 63.2% | 57.2% | 1.75 | +10.5% |
| Draw | 20.2% | 21.9% | 4.42 | -10.8% |
| SC Freiburg win | 16.6% | 21.0% | 4.62 | -23.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:30:00+00:00 |
| Fixture id | 096d800bcc95c547ef592cbef624d080 |
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
| Matched home-team name | Leverkusen |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.37 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.21 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.94 |
| Fair Over 3.5 odds | 2.25 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.88 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 69.2% |
| Unadjusted draw probability | 18.5% |
| Unadjusted away-win probability | 12.3% |
| Raw p over 1 5 | 86.7% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 58.1% |
| P home draw | 83.4% |
| P draw away | 36.8% |
| P home away | 79.8% |
| Raw p home draw | 87.7% |
| Raw p draw away | 30.8% |
| Raw p home away | 81.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.74 |
| Reference draw odds | 4.50 |
| Reference away odds | 4.70 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:36Z |
| Market reference home last update utc | 2026-10-16T22:15:36Z |
| Market reference draw last update utc | 2026-10-16T22:15:36Z |
| Market reference away last update utc | 2026-10-16T22:15:36Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | +6.0% |
| Draw probability edge | -1.7% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.1203 |
| Raw ev home | 0.2107 |
| Raw edge prob draw | -0.0341 |
| Raw ev draw | -0.1829 |
| Raw edge prob away | -0.0862 |
| Raw ev away | -0.4305 |
| Market p home draw | 78.1% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.2% |
| Market draw away odds | 2.21 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.7% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.24 |
| Market reference dc home draw odds | 1.24 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 86.3% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:14:40Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:35Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.4% |
| Market under 3 5 odds | 1.74 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:14:40Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.19 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:35Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.7% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.72 |
| Market reference btts yes last update utc | 2026-10-16T22:15:48Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **40.7%**. Expected goals are 1.95 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.74 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 72.0%; Under 3.5 goals: 48.7%; Double Chance 1X: 59.3%; Double Chance X2: 64.0%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 68.0%; BTTS Yes (both teams score): 72.4%; BTTS No (at least one team does not score): 27.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 36.0% | 2.78 |
| Draw | 23.3% | 4.29 |
| TSG Hoffenheim win | 40.7% | 2.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.95 |
| TSG Hoffenheim expected goals | 1.79 |
| Expected total goals | 3.74 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 89.5% |
| Under 1.5 | 10.5% |
| Over 2.5 | 72.0% |
| Under 2.5 | 28.0% |
| Over 3.5 | 51.3% |
| Under 3.5 | 48.7% |
| Over 4.5 | 32.0% |
| Under 4.5 | 68.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.20% |
| 2 | 1-2 | 8.54% |
| 3 | 2-2 | 7.31% |
| 4 | 2-1 | 7.00% |
| 5 | 1-3 | 5.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 36.0% | 30.5% | 3.21 | +15.6% |
| Draw | 23.3% | 23.5% | 4.21 | -1.9% |
| TSG Hoffenheim win | 40.7% | 46.0% | 2.15 | -12.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | fd9b8c185737a15615aa0c9daaa3dfbf |
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
| Matched home-team name | M'gladbach |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 72.4% |
| P btts no | 27.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.00 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.55 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.58 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.13 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 41.5% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 48.6% |
| Raw p btts yes | 72.3% |
| P home draw | 59.3% |
| P draw away | 64.0% |
| P home away | 76.7% |
| Raw p home draw | 64.6% |
| Raw p draw away | 58.5% |
| Raw p home away | 76.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.25 |
| Reference draw odds | 4.20 |
| Reference away odds | 2.16 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:36Z |
| Market reference home last update utc | 2026-10-16T22:15:36Z |
| Market reference draw last update utc | 2026-10-16T22:15:36Z |
| Market reference away last update utc | 2026-10-16T22:15:36Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | +5.5% |
| Draw probability edge | -0.2% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | +3.5% |
| Under 2.5 probability edge | -3.5% |
| Raw edge prob home | 0.1107 |
| Raw ev home | 0.3334 |
| Raw edge prob draw | -0.0047 |
| Raw ev draw | -0.0293 |
| Raw edge prob away | -0.1060 |
| Raw ev away | -0.2388 |
| Market p home draw | 53.9% |
| Market home draw odds | 1.79 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:52Z |
| Market reference home draw last update utc | 2026-10-16T22:15:47Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.5% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:52Z |
| Market reference draw away last update utc | 2026-10-16T22:15:47Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.6% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:52Z |
| Market reference home away last update utc | 2026-10-16T22:15:47Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home draw odds | 1.79 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 88.6% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:35Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.3% |
| Market reference under 3 5 odds | 1.86 |
| Market reference under 3 5 opposite odds | 2.03 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:35Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.35 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:52Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 3.15 |
| Market reference btts yes last update utc | 2026-10-16T22:15:48Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **68.0%**. Expected goals are 2.55 for VfB Stuttgart and 1.20 for Borussia Monchengladbach (3.75 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 72.8%; Under 3.5 goals: 48.1%; Double Chance 1X: 85.3%; Double Chance X2: 32.0%; Double Chance 12 (either team wins): 82.6%; Under 4.5 goals: 67.4%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 68.0% | 1.47 |
| Draw | 17.4% | 5.76 |
| Borussia Monchengladbach win | 14.7% | 6.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.55 |
| Borussia Monchengladbach expected goals | 1.20 |
| Expected total goals | 3.75 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 89.7% |
| Under 1.5 | 10.3% |
| Over 2.5 | 72.8% |
| Under 2.5 | 27.2% |
| Over 3.5 | 51.9% |
| Under 3.5 | 48.1% |
| Over 4.5 | 32.6% |
| Under 4.5 | 67.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.49% |
| 2 | 3-1 | 8.05% |
| 3 | 2-0 | 7.90% |
| 4 | 1-1 | 7.33% |
| 5 | 3-0 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 68.0% | 70.2% | 1.43 | -2.8% |
| Draw | 17.4% | 15.9% | 5.80 | +0.8% |
| Borussia Monchengladbach win | 14.7% | 13.9% | 6.98 | +2.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:30:00+00:00 |
| Fixture id | d4d56a31d8ccd432e3a6183180e093f3 |
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
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.21 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.69 |
| Fair Over 2.5 odds | 1.37 |
| Fair Under 2.5 odds | 3.68 |
| Fair Over 3.5 odds | 1.93 |
| Fair Under 3.5 odds | 2.08 |
| Fair Over 4.5 odds | 3.07 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 65.8% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 15.4% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.4% |
| Raw p btts yes | 65.2% |
| P home draw | 85.3% |
| P draw away | 32.0% |
| P home away | 82.6% |
| Raw p home draw | 84.6% |
| Raw p draw away | 34.2% |
| Raw p home away | 81.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.39 |
| Reference draw odds | 5.52 |
| Reference away odds | 6.29 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | -2.2% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | -0.0444 |
| Raw ev home | -0.0597 |
| Raw edge prob draw | 0.0286 |
| Raw ev draw | 0.0905 |
| Raw edge prob away | 0.0158 |
| Raw ev away | 0.0778 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **39.8%**. Expected goals are 0.90 for 1. FC Köln and 0.93 for FC Schalke 04 (1.83 combined). The most likely exact score is 1-0 at 16.5%. Goal-market probabilities: at least one goal: 85.5%; Over 2.5 goals: 29.5%; Under 3.5 goals: 88.4%; Double Chance 1X: 69.2%; Double Chance X2: 60.2%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 95.8%; BTTS Yes (both teams score): 36.2%; BTTS No (at least one team does not score): 63.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 39.8% | 2.52 |
| Draw | 29.4% | 3.40 |
| FC Schalke 04 win | 30.8% | 3.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 0.90 |
| FC Schalke 04 expected goals | 0.93 |
| Expected total goals | 1.83 |
| Over 0.5 | 85.5% |
| Under 0.5 | 14.5% |
| Over 1.5 | 56.5% |
| Under 1.5 | 43.5% |
| Over 2.5 | 29.5% |
| Under 2.5 | 70.5% |
| Over 3.5 | 11.6% |
| Under 3.5 | 88.4% |
| Over 4.5 | 4.2% |
| Under 4.5 | 95.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.49% |
| 2 | 0-0 | 14.49% |
| 3 | 0-1 | 12.56% |
| 4 | 1-1 | 12.35% |
| 5 | 2-0 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 39.8% | 48.1% | 2.12 | -15.7% |
| Draw | 29.4% | 23.7% | 3.98 | +17.1% |
| FC Schalke 04 win | 30.8% | 28.2% | 3.43 | +5.7% |
| Over 2.5 | 29.5% | 60.5% | 1.64 | -51.6% |
| Under 2.5 | 70.5% | 39.5% | 2.46 | +73.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 983440c6e348b558c6a3e10e2061ba55 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:52Z |
| Market best draw last update utc | 2026-10-16T22:14:52Z |
| Market best away last update utc | 2026-10-16T22:14:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Koln |
| Matched away-team name | Schalke 04 |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 36.2% |
| P btts no | 63.8% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.90 |
| Fair Over 1.5 odds | 1.77 |
| Fair Under 1.5 odds | 2.30 |
| Fair Over 2.5 odds | 3.39 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.61 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.08 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 31.4% |
| Unadjusted draw probability | 35.2% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 56.0% |
| Raw p under 3 5 | 88.6% |
| Raw p btts yes | 37.3% |
| P home draw | 69.2% |
| P draw away | 60.2% |
| P home away | 70.6% |
| Raw p home draw | 66.6% |
| Raw p draw away | 68.6% |
| Raw p home away | 64.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.01 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.34 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | -8.3% |
| Draw probability edge | +5.7% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -31.0% |
| Under 2.5 probability edge | +31.0% |
| Raw edge prob home | -0.1667 |
| Raw ev home | -0.3338 |
| Raw edge prob draw | 0.1150 |
| Raw ev draw | 0.4000 |
| Raw edge prob away | 0.0517 |
| Raw ev away | 0.1456 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **50.0%**. Expected goals are 1.53 for Augsburg and 1.03 for Union Berlin (2.56 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 48.1%; Under 3.5 goals: 74.2%; Double Chance 1X: 75.8%; Double Chance X2: 50.0%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 50.0% | 2.00 |
| Draw | 25.8% | 3.88 |
| Union Berlin win | 24.2% | 4.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.53 |
| Union Berlin expected goals | 1.03 |
| Expected total goals | 2.56 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.1% |
| Under 2.5 | 51.9% |
| Over 3.5 | 25.8% |
| Under 3.5 | 74.2% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.30% |
| 2 | 1-0 | 11.13% |
| 3 | 2-1 | 9.77% |
| 4 | 2-0 | 9.50% |
| 5 | 0-0 | 8.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 50.0% | 52.3% | 1.96 | -2.0% |
| Draw | 25.8% | 23.5% | 4.16 | +7.2% |
| Union Berlin win | 24.2% | 24.2% | 3.77 | -8.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04bb232a2940fcf03abf05b308e27577 |
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
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.20 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.88 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.33 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.8% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 74.4% |
| Raw p btts yes | 51.6% |
| P home draw | 75.8% |
| P draw away | 50.0% |
| P home away | 74.2% |
| Raw p home draw | 75.8% |
| Raw p draw away | 52.2% |
| Raw p home away | 72.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.85 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.84 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | -2.3% |
| Draw probability edge | +2.3% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -13.7% |
| Under 2.5 probability edge | +13.7% |
| Raw edge prob home | -0.0453 |
| Raw ev home | -0.0639 |
| Raw edge prob draw | 0.0452 |
| Raw ev draw | 0.1657 |
| Raw edge prob away | 0.0001 |
| Raw ev away | -0.0869 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **63.5%**. Expected goals are 2.27 for Borussia Dortmund and 1.24 for Eintracht Frankfurt (3.51 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 69.0%; Under 3.5 goals: 52.9%; Double Chance 1X: 82.7%; Double Chance X2: 36.5%; Double Chance 12 (either team wins): 80.7%; Under 4.5 goals: 71.7%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 63.5% | 1.58 |
| Draw | 19.3% | 5.19 |
| Eintracht Frankfurt win | 17.3% | 5.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.27 |
| Eintracht Frankfurt expected goals | 1.24 |
| Expected total goals | 3.51 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 87.6% |
| Under 1.5 | 12.4% |
| Over 2.5 | 69.0% |
| Under 2.5 | 31.0% |
| Over 3.5 | 47.1% |
| Under 3.5 | 52.9% |
| Over 4.5 | 28.3% |
| Under 4.5 | 71.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.15% |
| 2 | 1-1 | 8.40% |
| 3 | 2-0 | 8.16% |
| 4 | 3-1 | 7.68% |
| 5 | 1-0 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 63.5% | 67.2% | 1.48 | -6.1% |
| Draw | 19.3% | 17.4% | 5.39 | +3.9% |
| Eintracht Frankfurt win | 17.3% | 15.4% | 6.42 | +10.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 3ed4d1e775910625c50518a384e9c547 |
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
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 81/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.0% |
| P btts no | 36.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.87 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.09 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.23 |
| Fair Over 3.5 odds | 2.12 |
| Fair Under 3.5 odds | 1.89 |
| Fair Over 4.5 odds | 3.54 |
| Fair Under 4.5 odds | 1.39 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 87.4% |
| Raw p under 3 5 | 53.4% |
| Raw p btts yes | 64.6% |
| P home draw | 82.7% |
| P draw away | 36.5% |
| P home away | 80.7% |
| Raw p home draw | 80.9% |
| Raw p draw away | 40.3% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.45 |
| Reference draw odds | 5.15 |
| Reference away odds | 5.76 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | -3.8% |
| Draw probability edge | +1.9% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0756 |
| Raw ev home | -0.1167 |
| Raw edge prob draw | 0.0385 |
| Raw ev draw | 0.1432 |
| Raw edge prob away | 0.0371 |
| Raw ev away | 0.2269 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **52.2%**. Expected goals are 1.59 for FSV Mainz 05 and 1.15 for Werder Bremen (2.74 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 52.7%; Under 3.5 goals: 70.2%; Double Chance 1X: 76.8%; Double Chance X2: 47.8%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 52.2% | 1.91 |
| Draw | 24.5% | 4.08 |
| Werder Bremen win | 23.2% | 4.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.59 |
| Werder Bremen expected goals | 1.15 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 29.8% |
| Under 3.5 | 70.2% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.69% |
| 2 | 2-1 | 10.58% |
| 3 | 1-0 | 10.27% |
| 4 | 2-0 | 9.20% |
| 5 | 0-0 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 52.2% | 58.2% | 1.73 | -9.7% |
| Draw | 24.5% | 21.8% | 4.41 | +8.2% |
| Werder Bremen win | 23.2% | 20.0% | 4.72 | +9.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 4e5820453145833132980b8d190998c7 |
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
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.54 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.35 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.79 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 46.3% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 26.5% |
| Raw p over 1 5 | 77.0% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 55.5% |
| P home draw | 76.8% |
| P draw away | 47.8% |
| P home away | 75.5% |
| Raw p home draw | 73.5% |
| Raw p draw away | 53.7% |
| Raw p home away | 72.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.67 |
| Reference draw odds | 4.23 |
| Reference away odds | 4.59 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | -6.0% |
| Draw probability edge | +2.7% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -11.1% |
| Under 2.5 probability edge | +11.1% |
| Raw edge prob home | -0.1193 |
| Raw ev home | -0.1997 |
| Raw edge prob draw | 0.0545 |
| Raw ev draw | 0.2023 |
| Raw edge prob away | 0.0647 |
| Raw ev away | 0.2498 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **62.2%**. Expected goals are 2.00 for RB Leipzig and 1.39 for Elversberg (3.40 combined). The most likely exact score is 2-1 at 11.5%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 67.6%; Under 3.5 goals: 55.1%; Double Chance 1X: 81.8%; Double Chance X2: 37.8%; Double Chance 12 (either team wins): 80.4%; Under 4.5 goals: 73.4%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 62.2% | 1.61 |
| Draw | 19.6% | 5.09 |
| Elversberg win | 18.2% | 5.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.00 |
| Elversberg expected goals | 1.39 |
| Expected total goals | 3.40 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 67.6% |
| Under 2.5 | 32.4% |
| Over 3.5 | 44.9% |
| Under 3.5 | 55.1% |
| Over 4.5 | 26.6% |
| Under 4.5 | 73.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.46% |
| 2 | 1-1 | 8.59% |
| 3 | 2-0 | 8.23% |
| 4 | 3-1 | 7.66% |
| 5 | 1-0 | 7.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 62.2% | 73.5% | 1.39 | -13.6% |
| Draw | 19.6% | 15.8% | 6.09 | +19.6% |
| Elversberg win | 18.2% | 10.7% | 7.70 | +40.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04dac5e98ab5fc5564980542ca3fc746 |
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
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.97 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.52 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.08 |
| Fair Over 3.5 odds | 2.22 |
| Fair Under 3.5 odds | 1.82 |
| Fair Over 4.5 odds | 3.76 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 50.8% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 25.7% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.9% |
| Raw p btts yes | 65.9% |
| P home draw | 81.8% |
| P draw away | 37.8% |
| P home away | 80.4% |
| Raw p home draw | 74.3% |
| Raw p draw away | 49.2% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.33 |
| Reference draw odds | 5.54 |
| Reference away odds | 7.95 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | -11.3% |
| Draw probability edge | +3.8% |
| Away probability edge | +7.5% |
| Over 2.5 probability edge | -10.2% |
| Under 2.5 probability edge | +10.2% |
| Raw edge prob home | -0.2268 |
| Raw ev home | -0.2933 |
| Raw edge prob draw | 0.0770 |
| Raw ev draw | 0.4299 |
| Raw edge prob away | 0.1499 |
| Raw ev away | 0.9772 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **Hamburger SV win** at **34.7%**. Expected goals are 0.76 for SC Paderborn and 0.90 for Hamburger SV (1.66 combined). The most likely exact score is 0-0 at 17.2%. Goal-market probabilities: at least one goal: 82.8%; Over 2.5 goals: 24.7%; Under 3.5 goals: 91.1%; Double Chance 1X: 65.3%; Double Chance X2: 66.2%; Double Chance 12 (either team wins): 68.5%; Under 4.5 goals: 97.1%; BTTS Yes (both teams score): 31.9%; BTTS No (at least one team does not score): 68.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 33.8% | 2.96 |
| Draw | 31.5% | 3.18 |
| Hamburger SV win | 34.7% | 2.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.76 |
| Hamburger SV expected goals | 0.90 |
| Expected total goals | 1.66 |
| Over 0.5 | 82.8% |
| Under 0.5 | 17.2% |
| Over 1.5 | 51.2% |
| Under 1.5 | 48.8% |
| Over 2.5 | 24.7% |
| Under 2.5 | 75.3% |
| Over 3.5 | 8.9% |
| Under 3.5 | 91.1% |
| Over 4.5 | 2.9% |
| Under 4.5 | 97.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 17.23% |
| 2 | 1-0 | 16.11% |
| 3 | 0-1 | 15.48% |
| 4 | 1-1 | 12.17% |
| 5 | 0-2 | 7.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 33.8% | 40.0% | 2.40 | -18.8% |
| Draw | 31.5% | 25.9% | 3.92 | +23.3% |
| Hamburger SV win | 34.7% | 34.0% | 2.91 | +1.0% |
| Over 2.5 | 24.7% | 60.5% | 1.64 | -59.5% |
| Under 2.5 | 75.3% | 39.5% | 2.47 | +85.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 7630f897583f3acc0f483fa2d17d1ac5 |
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
| Matched home-team name | Paderborn |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 88/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 31.9% |
| P btts no | 68.1% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.80 |
| Fair Over 1.5 odds | 1.95 |
| Fair Under 1.5 odds | 2.05 |
| Fair Over 2.5 odds | 4.05 |
| Fair Under 2.5 odds | 1.33 |
| Fair Over 3.5 odds | 11.21 |
| Fair Under 3.5 odds | 1.10 |
| Fair Over 4.5 odds | 34.30 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 27.6% |
| Unadjusted draw probability | 37.0% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 50.8% |
| Raw p under 3 5 | 91.2% |
| Raw p btts yes | 33.0% |
| P home draw | 65.3% |
| P draw away | 66.2% |
| P home away | 68.5% |
| Raw p home draw | 64.6% |
| Raw p draw away | 72.4% |
| Raw p home away | 63.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.40 |
| Reference draw odds | 3.63 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:52Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:52Z |
| Home probability edge | -6.2% |
| Draw probability edge | +5.5% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -35.8% |
| Under 2.5 probability edge | +35.8% |
| Raw edge prob home | -0.1237 |
| Raw ev home | -0.3366 |
| Raw edge prob draw | 0.1102 |
| Raw ev draw | 0.4490 |
| Raw edge prob away | 0.0135 |
| Raw ev away | 0.0300 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **67.9%**. Expected goals are 1.18 for SC Freiburg and 2.77 for Bayern Munich (3.95 combined). The most likely exact score is 1-2 at 8.5%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 75.9%; Under 3.5 goals: 44.7%; Double Chance 1X: 32.1%; Double Chance X2: 83.0%; Double Chance 12 (either team wins): 84.9%; Under 4.5 goals: 63.8%; BTTS Yes (both teams score): 65.5%; BTTS No (at least one team does not score): 34.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 17.0% | 5.90 |
| Draw | 15.1% | 6.62 |
| Bayern Munich win | 67.9% | 1.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.18 |
| Bayern Munich expected goals | 2.77 |
| Expected total goals | 3.95 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 91.0% |
| Under 1.5 | 9.0% |
| Over 2.5 | 75.9% |
| Under 2.5 | 24.1% |
| Over 3.5 | 55.3% |
| Under 3.5 | 44.7% |
| Over 4.5 | 36.2% |
| Under 4.5 | 63.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.46% |
| 2 | 1-3 | 7.81% |
| 3 | 0-2 | 7.18% |
| 4 | 0-3 | 6.63% |
| 5 | 1-1 | 6.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 17.0% | 20.9% | 6.26 | +6.2% |
| Draw | 15.1% | 13.3% | 5.70 | -13.8% |
| Bayern Munich win | 67.9% | 65.8% | 1.47 | -0.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | f2bd909f25eea6b4ce42d2f52275e5c4 |
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
| Matched home-team name | Freiburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 65.5% |
| P btts no | 34.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.79 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.10 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.15 |
| Fair Over 3.5 odds | 1.81 |
| Fair Under 3.5 odds | 2.24 |
| Fair Over 4.5 odds | 2.76 |
| Fair Under 4.5 odds | 1.57 |
| Unadjusted home-win probability | 13.0% |
| Unadjusted draw probability | 16.9% |
| Unadjusted away-win probability | 70.0% |
| Raw p over 1 5 | 91.1% |
| Raw p under 3 5 | 44.4% |
| Raw p btts yes | 65.5% |
| P home draw | 32.1% |
| P draw away | 83.0% |
| P home away | 84.9% |
| Raw p home draw | 30.0% |
| Raw p draw away | 87.0% |
| Raw p home away | 83.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.34 |
| Reference draw odds | 6.61 |
| Reference away odds | 1.48 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.00 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | -3.9% |
| Draw probability edge | +1.8% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | -0.0782 |
| Raw ev home | -0.1832 |
| Raw edge prob draw | 0.0359 |
| Raw ev draw | -0.0362 |
| Raw edge prob away | 0.0424 |
| Raw ev away | 0.0296 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **50.0%**. Expected goals are 1.40 for TSG Hoffenheim and 2.37 for Bayer Leverkusen (3.77 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 71.9%; Under 3.5 goals: 48.8%; Double Chance 1X: 50.0%; Double Chance X2: 72.1%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 68.1%; BTTS Yes (both teams score): 69.8%; BTTS No (at least one team does not score): 30.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 27.9% | 3.58 |
| Draw | 22.1% | 4.53 |
| Bayer Leverkusen win | 50.0% | 2.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.40 |
| Bayer Leverkusen expected goals | 2.37 |
| Expected total goals | 3.77 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 71.9% |
| Under 2.5 | 28.1% |
| Over 3.5 | 51.2% |
| Under 3.5 | 48.8% |
| Over 4.5 | 31.9% |
| Under 4.5 | 68.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.97% |
| 2 | 1-2 | 7.76% |
| 3 | 2-1 | 7.13% |
| 4 | 2-2 | 6.76% |
| 5 | 1-3 | 6.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 27.9% | 34.9% | 2.76 | -23.0% |
| Draw | 22.1% | 23.5% | 4.25 | -6.2% |
| Bayer Leverkusen win | 50.0% | 41.6% | 2.39 | +19.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:30:00+00:00 |
| Fixture id | 2fd479cbb110c8f057e363bb06195f2b |
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
| Matched home-team name | Hoffenheim |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 69.8% |
| P btts no | 30.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.56 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.43 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.55 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.14 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 20.9% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 58.4% |
| Raw p over 1 5 | 89.8% |
| Raw p under 3 5 | 48.0% |
| Raw p btts yes | 69.0% |
| P home draw | 50.0% |
| P draw away | 72.1% |
| P home away | 77.9% |
| Raw p home draw | 41.6% |
| Raw p draw away | 79.1% |
| Raw p home away | 79.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.73 |
| Reference draw odds | 3.99 |
| Reference away odds | 2.31 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:35Z |
| Market reference home last update utc | 2026-10-16T22:15:35Z |
| Market reference draw last update utc | 2026-10-16T22:15:35Z |
| Market reference away last update utc | 2026-10-16T22:15:35Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:35Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:35Z |
| Home probability edge | -7.0% |
| Draw probability edge | -1.4% |
| Away probability edge | +8.4% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.1402 |
| Raw ev home | -0.4231 |
| Raw edge prob draw | -0.0279 |
| Raw ev draw | -0.1210 |
| Raw edge prob away | 0.1681 |
| Raw ev away | 0.3961 |

</details>


---
