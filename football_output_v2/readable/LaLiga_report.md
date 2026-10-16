# La Liga — football model report

Fixtures in this report: **20**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,218 |
| Training data through | 2026-10-12 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | 933866e5cdf52ddb62e284f2a6deed7c9cafdfbe21045f67a142005996f4f3fe |
| Optimizer objective | 1999.336 |
| Base scoring parameter | 0.091 |
| Home-advantage parameter | 0.282 |
| Dixon-Coles low-score adjustment | -0.020 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 10.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
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

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **53.7%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 0-1 at 12.2%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 49.0%; Under 3.5 goals: 73.1%; Double Chance 1X: 46.3%; Double Chance X2: 77.9%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 22.1% | 4.53 |
| Draw | 24.2% | 4.13 |
| Atlético Madrid win | 53.7% | 1.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.02 |
| Atlético Madrid expected goals | 1.59 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 74.0% |
| Under 1.5 | 26.0% |
| Over 2.5 | 49.0% |
| Under 2.5 | 51.0% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.22% |
| 2 | 1-1 | 11.53% |
| 3 | 1-2 | 10.14% |
| 4 | 0-2 | 9.90% |
| 5 | 0-0 | 7.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 22.1% | 19.9% | 4.88 | +7.7% |
| Draw | 24.2% | 22.9% | 3.98 | -3.6% |
| Atlético Madrid win | 53.7% | 57.3% | 1.79 | -3.8% |
| Over 2.5 | 49.0% | 54.8% | 1.87 | -8.3% |
| Under 2.5 | 51.0% | 45.2% | 2.08 | +6.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T12:00:00+00:00 |
| Fixture id | 6436925dd15916d7041ba32b60000d48 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Espanol |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 93/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.93 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.90 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.2% |
| P home draw | 46.3% |
| P draw away | 77.9% |
| P home away | 75.8% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.50 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.68 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:12Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:12Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | +2.2% |
| Draw probability edge | +1.4% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.0438 |
| Raw ev home | 0.1834 |
| Raw edge prob draw | 0.0273 |
| Raw ev draw | 0.0182 |
| Raw edge prob away | -0.0710 |
| Raw ev away | -0.1020 |
| Market p home draw | 43.0% |
| Market home draw odds | 2.14 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:28Z |
| Market reference home draw last update utc | 2026-10-16T22:14:55Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.7% |
| Market draw away odds | 1.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:28Z |
| Market reference draw away last update utc | 2026-10-16T22:14:55Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:28Z |
| Market reference home away last update utc | 2026-10-16T22:14:55Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.20 |
| Market reference dc home draw odds | 2.25 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 77.7% |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 4.15 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:45Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 69.3% |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 3.02 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:08Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 54.6% |
| Market btts yes odds | 1.73 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:28Z |
| Market reference btts yes odds | 1.77 |
| Market reference btts yes opposite odds | 2.11 |
| Market reference btts yes last update utc | 2026-10-16T22:14:55Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **62.3%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 67.9%; Under 3.5 goals: 54.7%; Double Chance 1X: 37.7%; Double Chance X2: 80.1%; Double Chance 12 (either team wins): 82.2%; Under 4.5 goals: 73.0%; BTTS Yes (both teams score): 63.8%; BTTS No (at least one team does not score): 36.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.9% | 5.03 |
| Draw | 17.8% | 5.62 |
| Barcelona win | 62.3% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.35 |
| Barcelona expected goals | 2.07 |
| Expected total goals | 3.42 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 67.9% |
| Under 2.5 | 32.1% |
| Over 3.5 | 45.3% |
| Under 3.5 | 54.7% |
| Over 4.5 | 27.0% |
| Under 4.5 | 73.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.94% |
| 2 | 0-2 | 8.10% |
| 3 | 1-1 | 7.69% |
| 4 | 0-1 | 7.61% |
| 5 | 1-3 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.9% | 15.1% | 6.81 | +35.3% |
| Draw | 17.8% | 14.0% | 5.69 | +1.2% |
| Barcelona win | 62.3% | 70.8% | 1.44 | -10.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | 846e496fc232b2fc20214754836727d0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.8% |
| P btts no | 36.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.15 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.21 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.12 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.71 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 24.6% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 55.3% |
| Raw p btts yes | 65.0% |
| P home draw | 37.7% |
| P draw away | 80.1% |
| P home away | 82.2% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Raw p home away | 78.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 5.60 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.37 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.20 |
| Market reference over 2 5 last update utc | 2026-10-16T22:14:45Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:14:45Z |
| Home probability edge | +4.7% |
| Draw probability edge | +3.7% |
| Away probability edge | -8.5% |
| Over 2.5 probability edge | -12.1% |
| Under 2.5 probability edge | +12.1% |
| Raw edge prob home | 0.0946 |
| Raw ev home | 0.6751 |
| Raw edge prob draw | 0.0749 |
| Raw ev draw | 0.2249 |
| Raw edge prob away | -0.1695 |
| Raw ev away | -0.2242 |
| Market p home draw | 31.2% |
| Market home draw odds | 3.00 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:28Z |
| Market reference home draw last update utc | 2026-10-16T22:14:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 85.1% |
| Market draw away odds | 1.13 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:28Z |
| Market reference draw away last update utc | 2026-10-16T22:14:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.7% |
| Market home away odds | 1.18 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:28Z |
| Market reference home away last update utc | 2026-10-16T22:14:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.14 |
| Market reference dc home draw odds | 3.11 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 92.7% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 10.50 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:45Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 40.1% |
| Market reference under 3 5 odds | 2.36 |
| Market reference under 3 5 opposite odds | 1.62 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:08Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 69.2% |
| Market btts yes odds | 1.35 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:28Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 3.20 |
| Market reference btts yes last update utc | 2026-10-16T22:15:26Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **39.9%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.1%; Double Chance 1X: 60.1%; Double Chance X2: 68.5%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 31.5% | 3.18 |
| Draw | 28.6% | 3.49 |
| Athletic Bilbao win | 39.9% | 2.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.07 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 65.8% |
| Under 1.5 | 34.2% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.9% |
| Under 3.5 | 81.1% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.29% |
| 2 | 0-1 | 12.86% |
| 3 | 0-0 | 10.66% |
| 4 | 1-0 | 10.64% |
| 5 | 1-2 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 31.5% | 29.9% | 3.35 | +5.5% |
| Draw | 28.6% | 28.0% | 3.43 | -1.8% |
| Athletic Bilbao win | 39.9% | 42.1% | 2.35 | -6.3% |
| Over 2.5 | 39.0% | 44.7% | 2.15 | -16.1% |
| Under 2.5 | 61.0% | 55.3% | 1.81 | +10.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T19:00:00+00:00 |
| Fixture id | f00cd1ea41fa39149729d14ebc07aa6c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.4% |
| P btts no | 54.6% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.38 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.29 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.89 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 45.6% |
| P home draw | 60.1% |
| P draw away | 68.5% |
| P home away | 71.4% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.22 |
| Reference Under 2.5 odds | 1.80 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:26Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:26Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | +1.6% |
| Draw probability edge | +0.7% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | 0.0315 |
| Raw ev home | 0.1077 |
| Raw edge prob draw | 0.0132 |
| Raw ev draw | 0.0052 |
| Raw edge prob away | -0.0448 |
| Raw ev away | -0.1157 |
| Market p home draw | 58.5% |
| Market home draw odds | 1.67 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:28Z |
| Market reference home draw last update utc | 2026-10-16T22:14:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.5% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:28Z |
| Market reference draw away last update utc | 2026-10-16T22:14:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.0% |
| Market home away odds | 1.36 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:28Z |
| Market reference home away last update utc | 2026-10-16T22:14:54Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.37 |
| Market reference dc home draw odds | 1.65 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 71.8% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-16T22:13:52Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 3.24 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.8% |
| Market under 3 5 odds | 1.23 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-16T22:13:52Z |
| Market reference under 3 5 odds | 1.30 |
| Market reference under 3 5 opposite odds | 3.85 |
| Market reference under 3 5 last update utc | 2026-10-16T22:14:45Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 51.9% |
| Market btts yes odds | 1.80 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:28Z |
| Market reference btts yes odds | 1.91 |
| Market reference btts yes opposite odds | 2.06 |
| Market reference btts yes last update utc | 2026-10-16T22:15:26Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **66.1%**. Expected goals are 2.42 for Villarreal and 1.18 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 70.1%; Under 3.5 goals: 51.3%; Double Chance 1X: 84.0%; Double Chance X2: 33.9%; Double Chance 12 (either team wins): 82.1%; Under 4.5 goals: 70.4%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 66.1% | 1.51 |
| Draw | 17.9% | 5.59 |
| Elche CF win | 16.0% | 6.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.42 |
| Elche CF expected goals | 1.18 |
| Expected total goals | 3.60 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 70.1% |
| Under 2.5 | 29.9% |
| Over 3.5 | 48.7% |
| Under 3.5 | 51.3% |
| Over 4.5 | 29.6% |
| Under 4.5 | 70.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.70% |
| 2 | 2-0 | 8.19% |
| 3 | 3-1 | 7.81% |
| 4 | 1-1 | 7.67% |
| 5 | 1-0 | 6.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 66.1% | 67.9% | 1.51 | -0.1% |
| Draw | 17.9% | 17.2% | 4.88 | -12.8% |
| Elche CF win | 16.0% | 14.9% | 6.73 | +7.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:15:00+00:00 |
| Fixture id | aef660734585649651415961a9d177c6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.02 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.34 |
| Fair Over 3.5 odds | 2.05 |
| Fair Under 3.5 odds | 1.95 |
| Fair Over 4.5 odds | 3.38 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 64.4% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 63.4% |
| P home draw | 84.0% |
| P draw away | 33.9% |
| P home away | 82.1% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.6% |
| Raw p home away | 81.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.43 |
| Reference draw odds | 5.10 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-16T22:14:45Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:14:45Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +3.3% |
| Under 2.5 probability edge | -3.3% |
| Raw edge prob home | -0.0356 |
| Raw ev home | -0.0282 |
| Raw edge prob draw | 0.0143 |
| Raw ev draw | -0.0927 |
| Raw edge prob away | 0.0212 |
| Raw ev away | 0.1476 |
| Market p home draw | 85.1% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:28Z |
| Market reference home draw last update utc | 2026-10-16T22:14:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.3% |
| Market draw away odds | 2.75 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:28Z |
| Market reference draw away last update utc | 2026-10-16T22:14:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.5% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:28Z |
| Market reference home away last update utc | 2026-10-16T22:14:54Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.91 |
| Market reference dc home draw odds | 1.14 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 85.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 6.10 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:45Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.0% |
| Market reference under 3 5 odds | 1.70 |
| Market reference under 3 5 opposite odds | 2.22 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:08Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:28Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-16T22:15:26Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **55.6%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.32 combined). The most likely exact score is 2-2 at 7.4%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 79.3%; Under 3.5 goals: 38.0%; Double Chance 1X: 76.4%; Double Chance X2: 44.4%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 57.9%; BTTS Yes (both teams score): 75.0%; BTTS No (at least one team does not score): 25.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 55.6% | 1.80 |
| Draw | 20.9% | 4.79 |
| Real Racing Club de Santander win | 23.6% | 4.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 2.78 |
| Real Racing Club de Santander expected goals | 1.55 |
| Expected total goals | 4.32 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 92.8% |
| Under 1.5 | 7.2% |
| Over 2.5 | 79.3% |
| Under 2.5 | 20.7% |
| Over 3.5 | 62.0% |
| Under 3.5 | 38.0% |
| Over 4.5 | 42.1% |
| Under 4.5 | 57.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.41% |
| 2 | 1-1 | 7.04% |
| 3 | 2-1 | 6.94% |
| 4 | 3-1 | 6.42% |
| 5 | 1-2 | 5.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 55.6% | 47.8% | 2.04 | +13.3% |
| Draw | 20.9% | 24.5% | 3.78 | -21.1% |
| Real Racing Club de Santander win | 23.6% | 27.6% | 3.82 | -9.9% |
| Over 2.5 | 79.3% | 60.9% | 1.68 | +33.3% |
| Under 2.5 | 20.7% | 39.1% | 2.38 | -50.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T12:00:00+00:00 |
| Fixture id | 1f566f17c50fe5162724ec2863d2207b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Osasuna |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 75.0% |
| P btts no | 25.0% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 57.34 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.86 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.84 |
| Fair Over 3.5 odds | 1.61 |
| Fair Under 3.5 odds | 2.63 |
| Fair Over 4.5 odds | 2.37 |
| Fair Under 4.5 odds | 1.73 |
| Unadjusted home-win probability | 63.3% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 19.5% |
| Raw p over 1 5 | 93.1% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 73.9% |
| P home draw | 76.4% |
| P draw away | 44.4% |
| P home away | 79.1% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Raw p home away | 82.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.35 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | +7.7% |
| Draw probability edge | -3.7% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | +18.4% |
| Under 2.5 probability edge | -18.4% |
| Raw edge prob home | 0.1544 |
| Raw ev home | 0.2909 |
| Raw edge prob draw | -0.0731 |
| Raw ev draw | -0.3497 |
| Raw edge prob away | -0.0812 |
| Raw ev away | -0.2544 |
| Market p home draw | 74.1% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:28Z |
| Market reference home draw last update utc | 2026-10-16T22:14:51Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.8% |
| Market draw away odds | 1.86 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:28Z |
| Market reference draw away last update utc | 2026-10-16T22:14:51Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:28Z |
| Market reference home away last update utc | 2026-10-16T22:14:51Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.86 |
| Market reference dc home draw odds | 1.30 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.5% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:46Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.5% |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.57 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:08Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 61.9% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:28Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.58 |
| Market reference btts yes last update utc | 2026-10-16T22:15:26Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **46.9%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 43.6%; Under 3.5 goals: 77.3%; Double Chance 1X: 74.2%; Double Chance X2: 53.1%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 46.9% | 2.13 |
| Draw | 27.3% | 3.66 |
| Alavés win | 25.8% | 3.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.49 |
| Alavés expected goals | 0.94 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 69.9% |
| Under 1.5 | 30.1% |
| Over 2.5 | 43.6% |
| Under 2.5 | 56.4% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.87% |
| 2 | 1-0 | 12.10% |
| 3 | 0-0 | 9.22% |
| 4 | 2-0 | 9.20% |
| 5 | 0-1 | 8.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 46.9% | 44.1% | 2.23 | +4.6% |
| Draw | 27.3% | 27.9% | 3.42 | -6.7% |
| Alavés win | 25.8% | 27.9% | 3.64 | -6.2% |
| Over 2.5 | 43.6% | 41.9% | 2.30 | +0.3% |
| Under 2.5 | 56.4% | 58.1% | 1.72 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T14:15:00+00:00 |
| Fixture id | aabe899ecc4c19a1fafe5440151b62e4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.85 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.29 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.41 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.09 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 47.6% |
| P home draw | 74.2% |
| P draw away | 53.1% |
| P home away | 72.7% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.36 |
| Reference Under 2.5 odds | 1.71 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:26Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:26Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | +2.8% |
| Draw probability edge | -0.6% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | +1.7% |
| Under 2.5 probability edge | -1.7% |
| Raw edge prob home | 0.0557 |
| Raw ev home | 0.1085 |
| Raw edge prob draw | -0.0128 |
| Raw ev draw | -0.0885 |
| Raw edge prob away | -0.0429 |
| Raw ev away | -0.1396 |
| Market p home draw | 72.5% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:28Z |
| Market reference home draw last update utc | 2026-10-16T22:14:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.1% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:28Z |
| Market reference draw away last update utc | 2026-10-16T22:14:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.4% |
| Market home away odds | 1.36 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:28Z |
| Market reference home away last update utc | 2026-10-16T22:14:54Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.69 |
| Market reference dc home draw odds | 1.33 |
| Market reference dc home away odds | 1.37 |
| Market p over 1 5 | 68.8% |
| Market reference over 1 5 odds | 1.42 |
| Market reference over 1 5 opposite odds | 2.98 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:08Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 78.2% |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 4.20 |
| Market reference under 3 5 last update utc | 2026-10-16T22:14:45Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 49.4% |
| Market btts yes odds | 1.90 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:28Z |
| Market reference btts yes odds | 2.00 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-10-16T22:15:26Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.0%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.5%. Goal-market probabilities: at least one goal: 85.7%; Over 2.5 goals: 29.5%; Under 3.5 goals: 87.9%; Double Chance 1X: 52.0%; Double Chance X2: 76.1%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.3%; BTTS No (at least one team does not score): 66.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.9% | 4.19 |
| Draw | 28.1% | 3.56 |
| Real Sociedad win | 48.0% | 2.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.7% |
| Under 0.5 | 14.3% |
| Over 1.5 | 56.0% |
| Under 1.5 | 44.0% |
| Over 2.5 | 29.5% |
| Under 2.5 | 70.5% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.54% |
| 2 | 0-0 | 14.33% |
| 3 | 1-0 | 12.12% |
| 4 | 1-1 | 11.36% |
| 5 | 0-2 | 11.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.9% | 29.6% | 3.29 | -21.4% |
| Draw | 28.1% | 26.1% | 3.63 | +2.0% |
| Real Sociedad win | 48.0% | 44.4% | 2.29 | +10.0% |
| Over 2.5 | 29.5% | 54.8% | 1.86 | -45.0% |
| Under 2.5 | 70.5% | 45.2% | 2.10 | +48.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T16:30:00+00:00 |
| Fixture id | 1051298b4aca6f07113309bff598a5c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 33.3% |
| P btts no | 66.7% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.98 |
| Fair Over 1.5 odds | 1.79 |
| Fair Under 1.5 odds | 2.27 |
| Fair Over 2.5 odds | 3.38 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.27 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.23 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 52.0% |
| P draw away | 76.1% |
| P home away | 71.9% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Raw p home away | 69.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.15 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.15 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | -5.7% |
| Draw probability edge | +2.0% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -25.3% |
| Under 2.5 probability edge | +25.3% |
| Raw edge prob home | -0.1139 |
| Raw ev home | -0.4016 |
| Raw edge prob draw | 0.0409 |
| Raw ev draw | 0.0941 |
| Raw edge prob away | 0.0730 |
| Raw ev away | 0.1833 |
| Market p home draw | 55.0% |
| Market home draw odds | 1.70 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:28Z |
| Market reference home draw last update utc | 2026-10-16T22:14:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.2% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:28Z |
| Market reference draw away last update utc | 2026-10-16T22:14:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.8% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:28Z |
| Market reference home away last update utc | 2026-10-16T22:14:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.34 |
| Market reference dc home draw odds | 1.76 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 77.8% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:46Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 68.4% |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:08Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.1% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:28Z |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.36 |
| Market reference btts yes last update utc | 2026-10-16T22:15:26Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.5%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 65.9%; Under 3.5 goals: 56.3%; Double Chance 1X: 91.8%; Double Chance X2: 21.5%; Double Chance 12 (either team wins): 86.7%; Under 4.5 goals: 74.8%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.5% | 1.27 |
| Draw | 13.3% | 7.51 |
| Sevilla win | 8.2% | 12.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.63 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 65.9% |
| Under 2.5 | 34.1% |
| Over 3.5 | 43.7% |
| Under 3.5 | 56.3% |
| Over 4.5 | 25.2% |
| Under 4.5 | 74.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.05% |
| 2 | 3-0 | 10.54% |
| 3 | 1-0 | 9.04% |
| 4 | 2-1 | 8.94% |
| 5 | 3-1 | 7.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 78.5% | 79.6% | 1.26 | -1.1% |
| Draw | 13.3% | 12.1% | 6.89 | -8.3% |
| Sevilla win | 8.2% | 8.3% | 12.60 | +3.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T19:00:00+00:00 |
| Fixture id | eccd63bf768e2f2a358b871d3f33a63d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.41 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.76 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.96 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.7% |
| P home draw | 91.8% |
| P draw away | 21.5% |
| P home away | 86.7% |
| Raw p home draw | 91.9% |
| Raw p draw away | 22.6% |
| Raw p home away | 85.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.23 |
| Reference draw odds | 6.75 |
| Reference away odds | 9.50 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-16T22:14:46Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:14:46Z |
| Home probability edge | -1.1% |
| Draw probability edge | +1.2% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -2.6% |
| Under 2.5 probability edge | +2.6% |
| Raw edge prob home | -0.0211 |
| Raw ev home | -0.0242 |
| Raw edge prob draw | 0.0237 |
| Raw ev draw | -0.0009 |
| Raw edge prob away | -0.0026 |
| Raw ev away | 0.0144 |
| Market p home draw | 91.1% |
| Market home draw odds | 1.04 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:28Z |
| Market reference home draw last update utc | 2026-10-16T22:14:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.6% |
| Market draw away odds | 4.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:28Z |
| Market reference draw away last update utc | 2026-10-16T22:14:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.3% |
| Market home away odds | 1.14 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:28Z |
| Market reference home away last update utc | 2026-10-16T22:14:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 4.31 |
| Market reference dc home draw odds | 1.07 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 87.6% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-16T22:14:46Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 54.2% |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.09 |
| Market reference under 3 5 last update utc | 2026-10-16T22:15:08Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 50.6% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:28Z |
| Market reference btts yes odds | 1.95 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-16T22:15:26Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.0%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.3%. Goal-market probabilities: at least one goal: 81.7%; Over 2.5 goals: 23.3%; Under 3.5 goals: 91.5%; Double Chance 1X: 67.8%; Double Chance X2: 65.0%; Double Chance 12 (either team wins): 67.2%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 30.9%; BTTS No (at least one team does not score): 69.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.0% | 2.86 |
| Draw | 32.8% | 3.05 |
| Rayo Vallecano win | 32.2% | 3.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.7% |
| Under 0.5 | 18.3% |
| Over 1.5 | 49.2% |
| Under 1.5 | 50.8% |
| Over 2.5 | 23.3% |
| Under 2.5 | 76.7% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.30% |
| 2 | 0-1 | 16.31% |
| 3 | 1-0 | 16.22% |
| 4 | 1-1 | 12.30% |
| 5 | 2-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.0% | 32.7% | 2.99 | +4.7% |
| Draw | 32.8% | 30.4% | 3.16 | +3.5% |
| Rayo Vallecano win | 32.2% | 36.8% | 2.74 | -11.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T19:00:00+00:00 |
| Fixture id | 4a88bc4de574d43ef34677fd8d78722f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 30.9% |
| P btts no | 69.1% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.46 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.29 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.77 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.41 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.1% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.3% |
| P home draw | 67.8% |
| P draw away | 65.0% |
| P home away | 67.2% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.7% |
| Raw p home away | 64.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.05 |
| Reference away odds | 2.55 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 2.50 |
| Reference Under 2.5 odds | 1.50 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Home probability edge | +2.3% |
| Draw probability edge | +2.3% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -12.9% |
| Under 2.5 probability edge | +12.9% |
| Raw edge prob home | 0.0457 |
| Raw ev home | 0.1149 |
| Raw edge prob draw | 0.0465 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0922 |
| Raw ev away | -0.2431 |
| Market p home draw | 64.3% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-16T22:14:28Z |
| Market reference home draw last update utc | 2026-10-16T22:14:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.4% |
| Market draw away odds | 1.45 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-16T22:14:28Z |
| Market reference draw away last update utc | 2026-10-16T22:14:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 67.4% |
| Market home away odds | 1.41 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-16T22:14:28Z |
| Market reference home away last update utc | 2026-10-16T22:14:54Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home draw odds | 1.50 |
| Market reference dc home away odds | 1.43 |
| Market p over 1 5 | 63.5% |
| Market reference over 1 5 odds | 1.54 |
| Market reference over 1 5 opposite odds | 2.60 |
| Market reference over 1 5 last update utc | 2026-10-16T22:15:08Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 83.8% |
| Market reference under 3 5 odds | 1.18 |
| Market reference under 3 5 opposite odds | 5.50 |
| Market reference under 3 5 last update utc | 2026-10-16T22:14:45Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 45.7% |
| Market btts yes odds | 2.07 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-16T22:14:28Z |
| Market reference btts yes odds | 2.16 |
| Market reference btts yes opposite odds | 1.82 |
| Market reference btts yes last update utc | 2026-10-16T22:15:26Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.6%**. Expected goals are 1.29 for Levante and 1.39 for Athletic Bilbao (2.68 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 50.1%; Under 3.5 goals: 71.8%; Double Chance 1X: 57.4%; Double Chance X2: 69.5%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 30.5% | 3.28 |
| Draw | 26.9% | 3.72 |
| Athletic Bilbao win | 42.6% | 2.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.29 |
| Athletic Bilbao expected goals | 1.39 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 50.1% |
| Under 2.5 | 49.9% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.79% |
| 2 | 0-1 | 10.08% |
| 3 | 1-2 | 9.29% |
| 4 | 1-0 | 7.60% |
| 5 | 0-0 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 30.5% | 26.6% | 3.52 | +7.5% |
| Draw | 26.9% | 27.5% | 3.52 | -5.3% |
| Athletic Bilbao win | 42.6% | 46.0% | 2.24 | -4.7% |
| Over 2.5 | 50.1% | 49.2% | 2.02 | +1.1% |
| Under 2.5 | 49.9% | 50.8% | 1.92 | -4.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T18:00:00+00:00 |
| Fixture id | a362cccad837f1ffae61ff43a3536688 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.83 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.46 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 54.7% |
| P home draw | 57.4% |
| P draw away | 69.5% |
| P home away | 73.1% |
| Raw p home draw | 60.8% |
| Raw p draw away | 65.5% |
| Raw p home away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.40 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.94 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:26Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:26Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | +3.9% |
| Draw probability edge | -0.5% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.0790 |
| Raw ev home | 0.2136 |
| Raw edge prob draw | -0.0109 |
| Raw ev draw | -0.0720 |
| Raw edge prob away | -0.0681 |
| Raw ev away | -0.1228 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **56.6%**. Expected goals are 1.38 for Alavés and 0.44 for Málaga (1.82 combined). The most likely exact score is 1-0 at 20.8%. Goal-market probabilities: at least one goal: 84.2%; Over 2.5 goals: 27.2%; Under 3.5 goals: 89.2%; Double Chance 1X: 83.5%; Double Chance X2: 43.4%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 96.3%; BTTS Yes (both teams score): 26.6%; BTTS No (at least one team does not score): 73.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 56.6% | 1.77 |
| Draw | 26.8% | 3.73 |
| Málaga win | 16.5% | 6.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.38 |
| Málaga expected goals | 0.44 |
| Expected total goals | 1.82 |
| Over 0.5 | 84.2% |
| Under 0.5 | 15.8% |
| Over 1.5 | 53.4% |
| Under 1.5 | 46.6% |
| Over 2.5 | 27.2% |
| Under 2.5 | 72.8% |
| Over 3.5 | 10.8% |
| Under 3.5 | 89.2% |
| Over 4.5 | 3.7% |
| Under 4.5 | 96.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.83% |
| 2 | 0-0 | 15.76% |
| 3 | 2-0 | 14.48% |
| 4 | 0-1 | 9.97% |
| 5 | 1-1 | 9.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 56.6% | 52.8% | 1.89 | +7.0% |
| Draw | 26.8% | 25.6% | 3.73 | +0.1% |
| Málaga win | 16.5% | 21.6% | 4.57 | -24.5% |
| Over 2.5 | 27.2% | 45.0% | 2.07 | -43.8% |
| Under 2.5 | 72.8% | 55.0% | 1.88 | +36.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T19:00:00+00:00 |
| Fixture id | 903eb4941471ffe20d525b02dd3b77aa |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 26.6% |
| P btts no | 73.4% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.34 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.68 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.29 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 27.30 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 54.4% |
| Raw p under 3 5 | 88.9% |
| Raw p btts yes | 26.7% |
| P home draw | 83.5% |
| P draw away | 43.4% |
| P home away | 73.2% |
| Raw p home draw | 88.5% |
| Raw p draw away | 39.5% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.80 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:26Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:26Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | +3.8% |
| Draw probability edge | +1.2% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -17.8% |
| Under 2.5 probability edge | +17.8% |
| Raw edge prob home | 0.0766 |
| Raw ev home | 0.1426 |
| Raw edge prob draw | 0.0243 |
| Raw ev draw | 0.0467 |
| Raw edge prob away | -0.1010 |
| Raw ev away | -0.4752 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **74.1%**. Expected goals are 2.31 for Atlético Madrid and 0.98 for Deportivo La Coruña (3.29 combined). The most likely exact score is 2-0 at 11.0%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 65.6%; Under 3.5 goals: 57.2%; Double Chance 1X: 89.2%; Double Chance X2: 25.9%; Double Chance 12 (either team wins): 84.8%; Under 4.5 goals: 75.4%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 74.1% | 1.35 |
| Draw | 15.2% | 6.59 |
| Deportivo La Coruña win | 10.8% | 9.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.31 |
| Deportivo La Coruña expected goals | 0.98 |
| Expected total goals | 3.29 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 84.9% |
| Under 1.5 | 15.1% |
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.6% |
| Under 4.5 | 75.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.98% |
| 2 | 2-1 | 10.77% |
| 3 | 1-0 | 9.32% |
| 4 | 3-0 | 8.46% |
| 5 | 3-1 | 8.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 74.1% | 81.1% | 1.24 | -8.2% |
| Draw | 15.2% | 11.7% | 6.92 | +5.0% |
| Deportivo La Coruña win | 10.8% | 7.1% | 14.90 | +60.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:00:00+00:00 |
| Fixture id | 70df1835c3b5ddff1c99e0189532136b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.62 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.63 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.06 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 67.0% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 14.4% |
| Raw p over 1 5 | 84.2% |
| Raw p under 3 5 | 58.2% |
| Raw p btts yes | 56.5% |
| P home draw | 89.2% |
| P draw away | 25.9% |
| P home away | 84.8% |
| Raw p home draw | 85.6% |
| Raw p draw away | 33.0% |
| Raw p home away | 81.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.20 |
| Reference draw odds | 6.50 |
| Reference away odds | 10.00 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:09Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:09Z |
| Home probability edge | -7.1% |
| Draw probability edge | +3.5% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | +1.9% |
| Under 2.5 probability edge | -1.9% |
| Raw edge prob home | -0.1417 |
| Raw ev home | -0.1695 |
| Raw edge prob draw | 0.0694 |
| Raw ev draw | 0.2907 |
| Raw edge prob away | 0.0722 |
| Raw ev away | 1.1410 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **49.5%**. Expected goals are 1.39 for Rayo Vallecano and 1.06 for Elche CF (2.46 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.4%; Double Chance 1X: 75.0%; Double Chance X2: 50.5%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 89.4%; BTTS Yes (both teams score): 49.0%; BTTS No (at least one team does not score): 51.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 49.5% | 2.02 |
| Draw | 25.5% | 3.92 |
| Elche CF win | 25.0% | 4.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.39 |
| Elche CF expected goals | 1.06 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 70.9% |
| Under 1.5 | 29.1% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.07% |
| 2 | 1-1 | 12.10% |
| 3 | 2-1 | 9.90% |
| 4 | 2-0 | 9.31% |
| 5 | 0-0 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 49.5% | 54.7% | 1.81 | -10.4% |
| Draw | 25.5% | 23.7% | 3.94 | +0.6% |
| Elche CF win | 25.0% | 21.5% | 4.78 | +19.5% |
| Over 2.5 | 45.3% | 53.4% | 1.88 | -14.9% |
| Under 2.5 | 54.7% | 46.6% | 2.07 | +13.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T12:00:00+00:00 |
| Fixture id | 734ad601156f5f4e6bc42317e5141516 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Vallecano |
| Matched away-team name | Elche |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.0% |
| P btts no | 51.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.14 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.44 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.46 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 44.2% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 28.4% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 49.5% |
| P home draw | 75.0% |
| P draw away | 50.5% |
| P home away | 74.5% |
| Raw p home draw | 71.6% |
| Raw p draw away | 55.8% |
| Raw p home away | 72.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.74 |
| Reference draw odds | 3.75 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | -5.3% |
| Draw probability edge | +1.8% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | -0.1050 |
| Raw ev home | -0.1995 |
| Raw edge prob draw | 0.0359 |
| Raw ev draw | 0.0765 |
| Raw edge prob away | 0.0691 |
| Raw ev away | 0.3598 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **39.1%**. Expected goals are 1.96 for Real Racing Club de Santander and 1.99 for Espanyol (3.95 combined). The most likely exact score is 1-1 at 8.4%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 74.9%; Under 3.5 goals: 44.3%; Double Chance 1X: 62.2%; Double Chance X2: 60.9%; Double Chance 12 (either team wins): 76.8%; Under 4.5 goals: 64.3%; BTTS Yes (both teams score): 74.8%; BTTS No (at least one team does not score): 25.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 39.1% | 2.56 |
| Draw | 23.2% | 4.32 |
| Espanyol win | 37.8% | 2.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.96 |
| Espanyol expected goals | 1.99 |
| Expected total goals | 3.95 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 90.6% |
| Under 1.5 | 9.4% |
| Over 2.5 | 74.9% |
| Under 2.5 | 25.1% |
| Over 3.5 | 55.7% |
| Under 3.5 | 44.3% |
| Over 4.5 | 35.7% |
| Under 4.5 | 64.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.39% |
| 2 | 2-2 | 8.03% |
| 3 | 2-1 | 7.41% |
| 4 | 1-2 | 7.03% |
| 5 | 3-1 | 4.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 39.1% | 39.5% | 2.47 | -3.5% |
| Draw | 23.2% | 25.2% | 3.72 | -13.8% |
| Espanyol win | 37.8% | 35.4% | 2.93 | +10.6% |
| Over 2.5 | 74.9% | 56.9% | 1.78 | +33.4% |
| Under 2.5 | 25.1% | 43.1% | 2.21 | -44.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:15:00+00:00 |
| Fixture id | 5960b1b6c20acfd78e78764fed47d505 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Espanol |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 93/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 74.8% |
| P btts no | 25.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.07 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 10.66 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 3.99 |
| Fair Over 3.5 odds | 1.80 |
| Fair Under 3.5 odds | 2.26 |
| Fair Over 4.5 odds | 2.80 |
| Fair Under 4.5 odds | 1.56 |
| Unadjusted home-win probability | 38.7% |
| Unadjusted draw probability | 21.1% |
| Unadjusted away-win probability | 40.2% |
| Raw p over 1 5 | 90.6% |
| Raw p under 3 5 | 44.3% |
| Raw p btts yes | 74.3% |
| P home draw | 62.2% |
| P draw away | 60.9% |
| P home away | 76.8% |
| Raw p home draw | 59.8% |
| Raw p draw away | 61.3% |
| Raw p home away | 78.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.35 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | -0.4% |
| Draw probability edge | -2.0% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | +18.0% |
| Under 2.5 probability edge | -18.0% |
| Raw edge prob home | -0.0075 |
| Raw ev home | -0.0437 |
| Raw edge prob draw | -0.0406 |
| Raw ev draw | -0.2139 |
| Raw edge prob away | 0.0480 |
| Raw ev away | 0.1765 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **45.0%**. Expected goals are 1.33 for Valencia and 1.62 for Villarreal (2.95 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 56.6%; Under 3.5 goals: 65.8%; Double Chance 1X: 55.0%; Double Chance X2: 69.7%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.3% | 3.30 |
| Draw | 24.7% | 4.05 |
| Villarreal win | 45.0% | 2.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.33 |
| Villarreal expected goals | 1.62 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 56.6% |
| Under 2.5 | 43.4% |
| Over 3.5 | 34.2% |
| Under 3.5 | 65.8% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.50% |
| 2 | 1-2 | 9.30% |
| 3 | 0-1 | 8.41% |
| 4 | 2-1 | 7.30% |
| 5 | 0-2 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.3% | 29.6% | 3.45 | +4.7% |
| Draw | 24.7% | 24.7% | 3.78 | -6.6% |
| Villarreal win | 45.0% | 45.7% | 2.17 | -2.4% |
| Over 2.5 | 56.6% | 56.9% | 1.78 | +0.7% |
| Under 2.5 | 43.4% | 43.1% | 2.20 | -4.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0dae715cc56fe201f9e667917c126691 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.32 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.90 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.66 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 24.7% |
| Unadjusted away-win probability | 44.2% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 59.2% |
| P home draw | 55.0% |
| P draw away | 69.7% |
| P home away | 75.3% |
| Raw p home draw | 55.8% |
| Raw p draw away | 68.9% |
| Raw p home away | 75.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.05 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:14Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:14Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.0% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.0148 |
| Raw ev home | 0.0725 |
| Raw edge prob draw | -0.0002 |
| Raw ev draw | -0.0670 |
| Raw edge prob away | -0.0145 |
| Raw ev away | -0.0402 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **55.1%**. Expected goals are 1.21 for Athletic Bilbao and 0.62 for Getafe (1.83 combined). The most likely exact score is 1-0 at 21.0%. Goal-market probabilities: at least one goal: 85.8%; Over 2.5 goals: 29.0%; Under 3.5 goals: 88.3%; Double Chance 1X: 82.1%; Double Chance X2: 44.9%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 95.9%; BTTS Yes (both teams score): 31.7%; BTTS No (at least one team does not score): 68.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 55.1% | 1.82 |
| Draw | 27.0% | 3.70 |
| Getafe win | 17.9% | 5.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.21 |
| Getafe expected goals | 0.62 |
| Expected total goals | 1.83 |
| Over 0.5 | 85.8% |
| Under 0.5 | 14.2% |
| Over 1.5 | 55.5% |
| Under 1.5 | 44.5% |
| Over 2.5 | 29.0% |
| Under 2.5 | 71.0% |
| Over 3.5 | 11.7% |
| Under 3.5 | 88.3% |
| Over 4.5 | 4.1% |
| Under 4.5 | 95.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.99% |
| 2 | 0-0 | 14.21% |
| 3 | 2-0 | 12.90% |
| 4 | 1-1 | 10.70% |
| 5 | 0-1 | 9.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 55.1% | 59.7% | 1.70 | -6.4% |
| Draw | 27.0% | 23.1% | 4.04 | +9.3% |
| Getafe win | 17.9% | 17.1% | 5.60 | +0.1% |
| Over 2.5 | 29.0% | 44.2% | 2.27 | -34.1% |
| Under 2.5 | 71.0% | 55.8% | 1.74 | +23.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T13:00:00+00:00 |
| Fixture id | 9c4254cba9944a839b421db27260504d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 31.7% |
| P btts no | 68.3% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 7.04 |
| Fair Over 1.5 odds | 1.80 |
| Fair Under 1.5 odds | 2.25 |
| Fair Over 2.5 odds | 3.45 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.56 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.47 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 50.4% |
| Unadjusted draw probability | 31.0% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 54.9% |
| Raw p under 3 5 | 88.6% |
| Raw p btts yes | 32.6% |
| P home draw | 82.1% |
| P draw away | 44.9% |
| P home away | 73.0% |
| Raw p home draw | 81.4% |
| Raw p draw away | 49.6% |
| Raw p home away | 69.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.60 |
| Reference draw odds | 3.80 |
| Reference away odds | 5.00 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | -4.7% |
| Draw probability edge | +3.9% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -15.2% |
| Under 2.5 probability edge | +15.2% |
| Raw edge prob home | -0.0930 |
| Raw ev home | -0.1427 |
| Raw edge prob draw | 0.0781 |
| Raw ev draw | 0.2505 |
| Raw edge prob away | 0.0149 |
| Raw ev away | 0.0426 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **58.3%**. Expected goals are 2.04 for Barcelona and 1.41 for Real Madrid (3.46 combined). The most likely exact score is 2-1 at 10.4%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 68.1%; Under 3.5 goals: 54.2%; Double Chance 1X: 77.4%; Double Chance X2: 41.7%; Double Chance 12 (either team wins): 80.9%; Under 4.5 goals: 72.7%; BTTS Yes (both teams score): 65.2%; BTTS No (at least one team does not score): 34.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 58.3% | 1.72 |
| Draw | 19.1% | 5.22 |
| Real Madrid win | 22.6% | 4.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.04 |
| Real Madrid expected goals | 1.41 |
| Expected total goals | 3.46 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 86.4% |
| Under 1.5 | 13.6% |
| Over 2.5 | 68.1% |
| Under 2.5 | 31.9% |
| Over 3.5 | 45.8% |
| Under 3.5 | 54.2% |
| Over 4.5 | 27.3% |
| Under 4.5 | 72.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.44% |
| 2 | 1-1 | 8.19% |
| 3 | 2-0 | 7.39% |
| 4 | 3-1 | 7.11% |
| 5 | 1-0 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 58.3% | 64.6% | 1.57 | -8.5% |
| Draw | 19.1% | 16.6% | 5.18 | -0.8% |
| Real Madrid win | 22.6% | 18.9% | 5.38 | +21.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T20:00:00+00:00 |
| Fixture id | 72089d103a5fe6a922c35e17efba6ffc |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 65.2% |
| P btts no | 34.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.01 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.33 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.13 |
| Fair Over 3.5 odds | 2.18 |
| Fair Under 3.5 odds | 1.85 |
| Fair Over 4.5 odds | 3.66 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 66.0% |
| P home draw | 77.4% |
| P draw away | 41.7% |
| P home away | 80.9% |
| Raw p home draw | 73.7% |
| Raw p draw away | 48.0% |
| Raw p home away | 78.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.50 |
| Reference draw odds | 5.30 |
| Reference away odds | 4.70 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.00 |
| Market reference over 2 5 last update utc | 2026-10-16T22:14:46Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:14:46Z |
| Home probability edge | -6.3% |
| Draw probability edge | +2.6% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | -0.1263 |
| Raw ev home | -0.1843 |
| Raw edge prob draw | 0.0518 |
| Raw ev draw | 0.1260 |
| Raw edge prob away | 0.0745 |
| Raw ev away | 0.4153 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **37.8%**. Expected goals are 1.44 for Celta Vigo and 1.30 for Real Betis (2.73 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 51.4%; Under 3.5 goals: 70.7%; Double Chance 1X: 63.9%; Double Chance X2: 62.2%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 85.8%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 37.8% | 2.64 |
| Draw | 26.0% | 3.84 |
| Real Betis win | 36.1% | 2.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.44 |
| Real Betis expected goals | 1.30 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 51.4% |
| Under 2.5 | 48.6% |
| Over 3.5 | 29.3% |
| Under 3.5 | 70.7% |
| Over 4.5 | 14.2% |
| Under 4.5 | 85.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.34% |
| 2 | 0-1 | 8.77% |
| 3 | 1-0 | 8.55% |
| 4 | 1-2 | 8.41% |
| 5 | 2-1 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 37.8% | 35.4% | 2.77 | +4.8% |
| Draw | 26.0% | 26.0% | 3.57 | -7.1% |
| Real Betis win | 36.1% | 38.6% | 2.67 | -3.5% |
| Over 2.5 | 51.4% | 53.4% | 1.91 | -1.7% |
| Under 2.5 | 48.6% | 46.6% | 2.03 | -1.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T15:15:00+00:00 |
| Fixture id | 2013e3955186ebe5258e85eb741a7553 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.85 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.16 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.41 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.04 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 40.3% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 33.7% |
| Raw p over 1 5 | 76.0% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 55.6% |
| P home draw | 63.9% |
| P draw away | 62.2% |
| P home away | 74.0% |
| Raw p home draw | 66.3% |
| Raw p draw away | 59.7% |
| Raw p home away | 74.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.40 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | +2.4% |
| Draw probability edge | +0.0% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.0490 |
| Raw ev home | 0.1157 |
| Raw edge prob draw | 0.0002 |
| Raw ev draw | -0.0705 |
| Raw edge prob away | -0.0492 |
| Raw ev away | -0.1006 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **54.9%**. Expected goals are 1.89 for Real Sociedad and 1.21 for Levante (3.10 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 60.0%; Under 3.5 goals: 62.4%; Double Chance 1X: 77.3%; Double Chance X2: 45.1%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 79.8%; BTTS Yes (both teams score): 59.5%; BTTS No (at least one team does not score): 40.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 54.9% | 1.82 |
| Draw | 22.4% | 4.47 |
| Levante win | 22.7% | 4.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.89 |
| Levante expected goals | 1.21 |
| Expected total goals | 3.10 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 60.0% |
| Under 2.5 | 40.0% |
| Over 3.5 | 37.6% |
| Under 3.5 | 62.4% |
| Over 4.5 | 20.2% |
| Under 4.5 | 79.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.31% |
| 2 | 2-1 | 10.07% |
| 3 | 1-0 | 8.63% |
| 4 | 2-0 | 8.35% |
| 5 | 3-1 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 54.9% | 56.7% | 1.76 | -3.3% |
| Draw | 22.4% | 21.9% | 4.26 | -4.6% |
| Levante win | 22.7% | 21.4% | 4.72 | +7.1% |
| Over 2.5 | 60.0% | 60.9% | 1.71 | +2.6% |
| Under 2.5 | 40.0% | 39.1% | 2.32 | -7.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:30:00+00:00 |
| Fixture id | 3cb8660cd2375b60e81144a7572cfb89 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.5% |
| P btts no | 40.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.55 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.49 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.66 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.94 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 53.1% |
| Unadjusted draw probability | 22.8% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 62.6% |
| Raw p btts yes | 59.7% |
| P home draw | 77.3% |
| P draw away | 45.1% |
| P home away | 77.6% |
| Raw p home draw | 76.0% |
| Raw p draw away | 46.9% |
| Raw p home away | 77.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.68 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:14Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:14Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.4% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0354 |
| Raw ev home | -0.0646 |
| Raw edge prob draw | 0.0089 |
| Raw ev draw | -0.0270 |
| Raw edge prob away | 0.0265 |
| Raw ev away | 0.1332 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **48.2%**. Expected goals are 1.54 for Sevilla and 1.13 for CA Osasuna (2.67 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 49.9%; Under 3.5 goals: 71.9%; Double Chance 1X: 74.5%; Double Chance X2: 51.8%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 86.7%; BTTS Yes (both teams score): 53.6%; BTTS No (at least one team does not score): 46.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 48.2% | 2.07 |
| Draw | 26.3% | 3.80 |
| CA Osasuna win | 25.5% | 3.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.54 |
| CA Osasuna expected goals | 1.13 |
| Expected total goals | 2.67 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 75.0% |
| Under 1.5 | 25.0% |
| Over 2.5 | 49.9% |
| Under 2.5 | 50.1% |
| Over 3.5 | 28.1% |
| Under 3.5 | 71.9% |
| Over 4.5 | 13.3% |
| Under 4.5 | 86.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.52% |
| 2 | 1-0 | 10.76% |
| 3 | 2-1 | 9.60% |
| 4 | 2-0 | 8.50% |
| 5 | 0-0 | 7.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 48.2% | 49.7% | 2.02 | -2.6% |
| Draw | 26.3% | 26.8% | 3.60 | -5.3% |
| CA Osasuna win | 25.5% | 23.4% | 4.11 | +4.8% |
| Over 2.5 | 49.9% | 44.2% | 2.19 | +9.3% |
| Under 2.5 | 50.1% | 55.8% | 1.79 | -10.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T20:00:00+00:00 |
| Fixture id | 85e464708d03287f24590e1478aeca31 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:14:28Z |
| Market best draw last update utc | 2026-10-16T22:14:28Z |
| Market best away last update utc | 2026-10-16T22:14:28Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.6% |
| P btts no | 46.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.74 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.00 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.56 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.51 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 46.6% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 74.9% |
| Raw p under 3 5 | 72.0% |
| Raw p btts yes | 53.5% |
| P home draw | 74.5% |
| P draw away | 51.8% |
| P home away | 73.7% |
| Raw p home draw | 72.4% |
| Raw p draw away | 53.4% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.90 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.80 |
| Market reference 1x2 last update utc | 2026-10-16T22:15:26Z |
| Market reference home last update utc | 2026-10-16T22:15:26Z |
| Market reference draw last update utc | 2026-10-16T22:15:26Z |
| Market reference away last update utc | 2026-10-16T22:15:26Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:15:13Z |
| Market best over 2 5 last update utc | 2026-10-16T22:14:28Z |
| Market best under 2 5 last update utc | 2026-10-16T22:14:28Z |
| Home probability edge | -1.6% |
| Draw probability edge | -0.5% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +5.7% |
| Under 2.5 probability edge | -5.7% |
| Raw edge prob home | -0.0311 |
| Raw ev home | -0.0578 |
| Raw edge prob draw | -0.0106 |
| Raw ev draw | -0.0716 |
| Raw edge prob away | 0.0416 |
| Raw ev away | 0.1331 |

</details>


---
