# La Liga — football model report

Fixtures in this report: **15**.

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
| Optimizer objective | 1999.336 |
| Base scoring parameter | 0.091 |
| Home-advantage parameter | 0.282 |
| Dixon-Coles low-score adjustment | -0.020 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 15.00 |
| Additional event odds calls used before this league | 5.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **49.6%**. Expected goals are 2.04 for Deportivo La Coruña and 1.32 for Levante (3.36 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 64.1%; Under 3.5 goals: 57.0%; Double Chance 1X: 74.5%; Double Chance X2: 50.4%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 64.8%; BTTS No (at least one team does not score): 35.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 49.6% | 2.01 |
| Draw | 24.9% | 4.02 |
| Levante win | 25.5% | 3.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 2.04 |
| Levante expected goals | 1.32 |
| Expected total goals | 3.36 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 84.9% |
| Under 1.5 | 15.1% |
| Over 2.5 | 64.1% |
| Under 2.5 | 35.9% |
| Over 3.5 | 43.0% |
| Under 3.5 | 57.0% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.93% |
| 2 | 2-1 | 8.79% |
| 3 | 2-2 | 7.22% |
| 4 | 2-0 | 6.65% |
| 5 | 1-2 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 49.6% | 45.4% | 2.17 | +7.7% |
| Draw | 24.9% | 28.1% | 3.62 | -9.8% |
| Levante win | 25.5% | 26.5% | 3.60 | -8.3% |
| Over 2.5 | 64.1% | 49.2% | 1.98 | +27.0% |
| Under 2.5 | 35.9% | 50.8% | 1.96 | -29.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-16T19:00:00+00:00 |
| Fixture id | 19ee731602634e5c9e3106630e087464 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-14T18:12:57Z |
| Market best draw last update utc | 2026-10-14T18:12:57Z |
| Market best away last update utc | 2026-10-14T18:12:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | La Coruna |
| Matched away-team name | Levante |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.8% |
| P btts no | 35.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.88 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.61 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.79 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.13 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 53.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 64.0% |
| P home draw | 74.5% |
| P draw away | 50.4% |
| Raw p home draw | 75.6% |
| Raw p draw away | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 2.18 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.94 |
| Home probability edge | +4.3% |
| Draw probability edge | -3.2% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +14.9% |
| Under 2.5 probability edge | -14.9% |
| Raw edge prob home | 0.0851 |
| Raw ev home | 0.1693 |
| Raw edge prob draw | -0.0635 |
| Raw ev draw | -0.2133 |
| Raw edge prob away | -0.0216 |
| Raw ev away | -0.1223 |
| Market p home draw | 72.3% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:12:57Z |
| Market reference home draw last update utc | 2026-10-14T18:12:57Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.8% |
| Market draw away odds | 1.77 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:12:57Z |
| Market reference draw away last update utc | 2026-10-14T18:12:57Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.77 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 74.7% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T18:11:36Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.4% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T18:11:36Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.7% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:12:57Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.07 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **52.6%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.7%; Under 3.5 goals: 73.2%; Double Chance 1X: 47.4%; Double Chance X2: 77.9%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 22.1% | 4.52 |
| Draw | 25.2% | 3.96 |
| Atlético Madrid win | 52.6% | 1.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.02 |
| Atlético Madrid expected goals | 1.59 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.7% |
| Under 2.5 | 51.3% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.01% |
| 2 | 0-1 | 11.97% |
| 3 | 1-2 | 9.94% |
| 4 | 0-2 | 9.69% |
| 5 | 0-0 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 22.1% | 20.0% | 4.88 | +8.0% |
| Draw | 25.2% | 24.9% | 3.94 | -0.6% |
| Atlético Madrid win | 52.6% | 55.1% | 1.80 | -5.3% |
| Over 2.5 | 48.7% | 52.7% | 1.87 | -9.0% |
| Under 2.5 | 51.3% | 47.3% | 2.08 | +6.8% |

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
| Market best home last update utc | 2026-10-14T18:12:57Z |
| Market best draw last update utc | 2026-10-14T18:12:57Z |
| Market best away last update utc | 2026-10-14T18:12:57Z |
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
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.37 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.98 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.2% |
| P home draw | 47.4% |
| P draw away | 77.9% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 4.88 |
| Reference draw odds | 3.94 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | +2.1% |
| Draw probability edge | +0.4% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | 0.0422 |
| Raw ev home | 0.1834 |
| Raw edge prob draw | 0.0070 |
| Raw ev draw | 0.0080 |
| Raw edge prob away | -0.0492 |
| Raw ev away | -0.0970 |
| Market p home draw | 45.5% |
| Market home draw odds | 2.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:12:57Z |
| Market reference home draw last update utc | 2026-10-14T18:12:57Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 79.4% |
| Market draw away odds | 1.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:12:57Z |
| Market reference draw away last update utc | 2026-10-14T18:12:57Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.13 |
| Market reference dc draw away odds | 1.22 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 77.7% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T18:12:50Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 4.15 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 68.8% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T18:12:50Z |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 3.05 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.0% |
| Market btts yes odds | 1.73 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:12:57Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.08 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **61.5%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 67.5%; Under 3.5 goals: 54.7%; Double Chance 1X: 38.5%; Double Chance X2: 80.5%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.5% | 5.12 |
| Draw | 19.0% | 5.28 |
| Barcelona win | 61.5% | 1.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.35 |
| Barcelona expected goals | 2.07 |
| Expected total goals | 3.42 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 67.5% |
| Under 2.5 | 32.5% |
| Over 3.5 | 45.3% |
| Under 3.5 | 54.7% |
| Over 4.5 | 26.8% |
| Under 4.5 | 73.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.80% |
| 2 | 1-1 | 8.20% |
| 3 | 0-2 | 7.99% |
| 4 | 0-1 | 7.51% |
| 5 | 1-3 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.5% | 14.4% | 6.21 | +21.2% |
| Draw | 19.0% | 16.4% | 5.44 | +3.1% |
| Barcelona win | 61.5% | 69.2% | 1.49 | -8.3% |

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
| Market best home last update utc | 2026-10-14T18:12:57Z |
| Market best draw last update utc | 2026-10-14T18:12:57Z |
| Market best away last update utc | 2026-10-14T18:12:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.98 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.20 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.08 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.74 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 24.6% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 55.3% |
| Raw p btts yes | 65.0% |
| P home draw | 38.5% |
| P draw away | 80.5% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 6.80 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.44 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Home probability edge | +5.1% |
| Draw probability edge | +2.6% |
| Away probability edge | -7.7% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | 0.1017 |
| Raw ev home | 0.5275 |
| Raw edge prob draw | 0.0515 |
| Raw ev draw | 0.1711 |
| Raw edge prob away | -0.1532 |
| Raw ev away | -0.1973 |
| Market p home draw | 34.4% |
| Market home draw odds | 2.82 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:12:57Z |
| Market reference home draw last update utc | 2026-10-14T18:12:57Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.2% |
| Market draw away odds | 1.15 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:12:57Z |
| Market reference draw away last update utc | 2026-10-14T18:12:57Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.82 |
| Market reference dc draw away odds | 1.15 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 91.9% |
| Market over 1 5 odds | 1.02 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T18:12:50Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 9.70 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 42.2% |
| Market under 3 5 odds | 2.19 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T18:12:50Z |
| Market reference under 3 5 odds | 2.28 |
| Market reference under 3 5 opposite odds | 1.69 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.5% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:12:57Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 3.00 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **40.6%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.1%; Double Chance 1X: 59.4%; Double Chance X2: 69.3%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.7% | 3.25 |
| Draw | 28.6% | 3.49 |
| Athletic Bilbao win | 40.6% | 2.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.07 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
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
| 2 | 0-1 | 13.11% |
| 3 | 0-0 | 10.66% |
| 4 | 1-0 | 10.38% |
| 5 | 1-2 | 8.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.7% | 28.4% | 3.47 | +6.6% |
| Draw | 28.6% | 28.0% | 3.51 | +0.5% |
| Athletic Bilbao win | 40.6% | 43.6% | 2.26 | -8.2% |
| Over 2.5 | 39.0% | 46.1% | 2.10 | -18.0% |
| Under 2.5 | 61.0% | 53.9% | 1.86 | +13.4% |

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
| Market best home last update utc | 2026-10-14T18:12:57Z |
| Market best draw last update utc | 2026-10-14T18:12:57Z |
| Market best away last update utc | 2026-10-14T18:12:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
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
| P home draw | 59.4% |
| P draw away | 69.3% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 3.45 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.26 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +2.3% |
| Draw probability edge | +0.7% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | 0.0468 |
| Raw ev home | 0.1475 |
| Raw edge prob draw | 0.0133 |
| Raw ev draw | 0.0287 |
| Raw edge prob away | -0.0602 |
| Raw ev away | -0.1497 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **66.1%**. Expected goals are 2.41 for Villarreal and 1.19 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 69.8%; Under 3.5 goals: 51.3%; Double Chance 1X: 84.7%; Double Chance X2: 33.9%; Under 4.5 goals: 70.5%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 66.1% | 1.51 |
| Draw | 18.6% | 5.38 |
| Elche CF win | 15.3% | 6.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.41 |
| Elche CF expected goals | 1.19 |
| Expected total goals | 3.60 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 69.8% |
| Under 2.5 | 30.2% |
| Over 3.5 | 48.7% |
| Under 3.5 | 51.3% |
| Over 4.5 | 29.5% |
| Under 4.5 | 70.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.70% |
| 2 | 2-0 | 8.18% |
| 3 | 1-1 | 7.97% |
| 4 | 3-1 | 7.80% |
| 5 | 1-0 | 6.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 66.1% | 67.8% | 1.51 | -0.2% |
| Draw | 18.6% | 18.6% | 4.88 | -9.3% |
| Elche CF win | 15.3% | 13.6% | 6.73 | +3.3% |

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
| Market best home last update utc | 2026-10-14T18:12:57Z |
| Market best draw last update utc | 2026-10-14T18:12:57Z |
| Market best away last update utc | 2026-10-14T18:12:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.63 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.32 |
| Fair Over 3.5 odds | 2.05 |
| Fair Under 3.5 odds | 1.95 |
| Fair Over 4.5 odds | 3.39 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 63.4% |
| P home draw | 84.7% |
| P draw away | 33.9% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.47 |
| Reference draw odds | 5.30 |
| Reference away odds | 7.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | -1.7% |
| Draw probability edge | +0.0% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | +3.1% |
| Under 2.5 probability edge | -3.1% |
| Raw edge prob home | -0.0344 |
| Raw ev home | -0.0284 |
| Raw edge prob draw | 0.0002 |
| Raw ev draw | -0.0924 |
| Raw edge prob away | 0.0342 |
| Raw ev away | 0.1480 |
| Market p home draw | 85.1% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T18:12:57Z |
| Market reference home draw last update utc | 2026-10-14T18:12:57Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 35.3% |
| Market draw away odds | 2.75 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T18:12:57Z |
| Market reference draw away last update utc | 2026-10-14T18:12:57Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.14 |
| Market reference dc draw away odds | 2.75 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 85.3% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T18:12:26Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.8% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T18:12:26Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.24 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T18:12:57Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.29 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **55.9%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.33 combined). The most likely exact score is 2-2 at 7.7%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.2%; Under 3.5 goals: 38.0%; Double Chance 1X: 77.6%; Double Chance X2: 44.1%; Under 4.5 goals: 58.0%; BTTS Yes (both teams score): 75.2%; BTTS No (at least one team does not score): 24.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 55.9% | 1.79 |
| Draw | 21.8% | 4.59 |
| Real Racing Club de Santander win | 22.4% | 4.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 2.78 |
| Real Racing Club de Santander expected goals | 1.55 |
| Expected total goals | 4.33 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 92.8% |
| Under 1.5 | 7.2% |
| Over 2.5 | 79.2% |
| Under 2.5 | 20.8% |
| Over 3.5 | 62.0% |
| Under 3.5 | 38.0% |
| Over 4.5 | 42.0% |
| Under 4.5 | 58.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.73% |
| 2 | 1-1 | 7.34% |
| 3 | 2-1 | 6.98% |
| 4 | 3-1 | 6.46% |
| 5 | 1-2 | 5.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 55.9% | 48.5% | 2.04 | +14.0% |
| Draw | 21.8% | 26.3% | 3.72 | -19.0% |
| Real Racing Club de Santander win | 22.4% | 25.2% | 3.88 | -13.2% |
| Over 2.5 | 79.2% | 56.8% | 1.74 | +37.7% |
| Under 2.5 | 20.8% | 43.2% | 2.27 | -52.7% |

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
| Market best home last update utc | 2026-10-14T18:12:58Z |
| Market best draw last update utc | 2026-10-14T18:12:58Z |
| Market best away last update utc | 2026-10-14T18:12:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Osasuna |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 75.2% |
| P btts no | 24.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.03 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.93 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.80 |
| Fair Over 3.5 odds | 1.61 |
| Fair Under 3.5 odds | 2.63 |
| Fair Over 4.5 odds | 2.38 |
| Fair Under 4.5 odds | 1.72 |
| Unadjusted home-win probability | 63.3% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 19.5% |
| Raw p over 1 5 | 93.1% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 73.9% |
| P home draw | 77.6% |
| P draw away | 44.1% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.04 |
| Reference draw odds | 3.72 |
| Reference away odds | 3.88 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | +7.4% |
| Draw probability edge | -4.6% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | +22.4% |
| Under 2.5 probability edge | -22.4% |
| Raw edge prob home | 0.1480 |
| Raw ev home | 0.2905 |
| Raw edge prob draw | -0.0911 |
| Raw ev draw | -0.3599 |
| Raw edge prob away | -0.0569 |
| Raw ev away | -0.2422 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **47.8%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 43.6%; Under 3.5 goals: 77.3%; Double Chance 1X: 75.2%; Double Chance X2: 52.2%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 47.8% | 2.09 |
| Draw | 27.4% | 3.64 |
| Alavés win | 24.8% | 4.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.49 |
| Alavés expected goals | 0.94 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 43.6% |
| Under 2.5 | 56.4% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.95% |
| 2 | 1-0 | 12.31% |
| 3 | 2-0 | 9.36% |
| 4 | 0-0 | 9.27% |
| 5 | 2-1 | 8.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 47.8% | 45.8% | 2.16 | +3.1% |
| Draw | 27.4% | 28.2% | 3.48 | -4.5% |
| Alavés win | 24.8% | 26.0% | 3.78 | -6.3% |
| Over 2.5 | 43.6% | 42.6% | 2.30 | +0.3% |
| Under 2.5 | 56.4% | 57.4% | 1.72 | -3.0% |

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
| Market best home last update utc | 2026-10-14T18:12:58Z |
| Market best draw last update utc | 2026-10-14T18:12:58Z |
| Market best away last update utc | 2026-10-14T18:12:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.79 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.29 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.09 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 47.6% |
| P home draw | 75.2% |
| P draw away | 52.2% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.16 |
| Reference draw odds | 3.48 |
| Reference away odds | 3.78 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.30 |
| Reference Under 2.5 odds | 1.72 |
| Home probability edge | +2.0% |
| Draw probability edge | -0.8% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | 0.0391 |
| Raw ev home | 0.0737 |
| Raw edge prob draw | -0.0158 |
| Raw ev draw | -0.0724 |
| Raw edge prob away | -0.0233 |
| Raw ev away | -0.1065 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **47.4%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.3%. Goal-market probabilities: at least one goal: 85.4%; Over 2.5 goals: 29.4%; Under 3.5 goals: 87.9%; Double Chance 1X: 52.6%; Double Chance X2: 76.0%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.4%; BTTS No (at least one team does not score): 66.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 24.0% | 4.16 |
| Draw | 28.6% | 3.50 |
| Real Sociedad win | 47.4% | 2.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.4% |
| Under 0.5 | 14.6% |
| Over 1.5 | 55.9% |
| Under 1.5 | 44.1% |
| Over 2.5 | 29.4% |
| Under 2.5 | 70.6% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.31% |
| 2 | 0-0 | 14.57% |
| 3 | 1-0 | 12.18% |
| 4 | 1-1 | 11.56% |
| 5 | 0-2 | 11.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 24.0% | 29.9% | 3.29 | -21.0% |
| Draw | 28.6% | 27.0% | 3.63 | +3.7% |
| Real Sociedad win | 47.4% | 43.1% | 2.29 | +8.5% |
| Over 2.5 | 29.4% | 53.1% | 1.86 | -45.3% |
| Under 2.5 | 70.6% | 46.9% | 2.10 | +48.3% |

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
| Market best home last update utc | 2026-10-14T18:12:58Z |
| Market best draw last update utc | 2026-10-14T18:12:58Z |
| Market best away last update utc | 2026-10-14T18:12:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 33.4% |
| P btts no | 66.6% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.86 |
| Fair Over 1.5 odds | 1.79 |
| Fair Under 1.5 odds | 2.27 |
| Fair Over 2.5 odds | 3.40 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.29 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.37 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 52.6% |
| P draw away | 76.0% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.29 |
| Reference draw odds | 3.63 |
| Reference away odds | 2.29 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -5.8% |
| Draw probability edge | +1.6% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -23.7% |
| Under 2.5 probability edge | +23.7% |
| Raw edge prob home | -0.1166 |
| Raw ev home | -0.4013 |
| Raw edge prob draw | 0.0312 |
| Raw ev draw | 0.0939 |
| Raw edge prob away | 0.0854 |
| Raw ev away | 0.1832 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **77.0%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 11.8%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 65.3%; Under 3.5 goals: 56.7%; Double Chance 1X: 91.5%; Double Chance X2: 23.0%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 48.8%; BTTS No (at least one team does not score): 51.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.0% | 1.30 |
| Draw | 14.5% | 6.88 |
| Sevilla win | 8.5% | 11.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.63 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 65.3% |
| Under 2.5 | 34.7% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.81% |
| 2 | 3-0 | 10.34% |
| 3 | 1-0 | 8.87% |
| 4 | 2-1 | 8.76% |
| 5 | 3-1 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.0% | 76.5% | 1.30 | +0.1% |
| Draw | 14.5% | 14.6% | 6.61 | -3.9% |
| Sevilla win | 8.5% | 8.9% | 10.70 | -9.2% |

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
| Market best home last update utc | 2026-10-14T18:12:58Z |
| Market best draw last update utc | 2026-10-14T18:12:58Z |
| Market best away last update utc | 2026-10-14T18:12:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.8% |
| P btts no | 51.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.86 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.66 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.88 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.02 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.7% |
| P home draw | 91.5% |
| P draw away | 23.0% |
| Raw p home draw | 91.9% |
| Raw p draw away | 22.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.30 |
| Reference draw odds | 6.61 |
| Reference away odds | 10.70 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +0.5% |
| Draw probability edge | -0.0% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | 0.0093 |
| Raw ev home | 0.0068 |
| Raw edge prob draw | -0.0006 |
| Raw ev draw | -0.0414 |
| Raw edge prob away | -0.0086 |
| Raw ev away | -0.1385 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.1%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.5%. Goal-market probabilities: at least one goal: 81.5%; Over 2.5 goals: 23.2%; Under 3.5 goals: 91.5%; Double Chance 1X: 68.2%; Double Chance X2: 64.9%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 31.0%; BTTS No (at least one team does not score): 69.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.1% | 2.85 |
| Draw | 33.1% | 3.02 |
| Rayo Vallecano win | 31.8% | 3.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.5% |
| Under 0.5 | 18.5% |
| Over 1.5 | 49.2% |
| Under 1.5 | 50.8% |
| Over 2.5 | 23.2% |
| Under 2.5 | 76.8% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.49% |
| 2 | 1-0 | 16.27% |
| 3 | 0-1 | 16.09% |
| 4 | 1-1 | 12.42% |
| 5 | 2-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.1% | 32.9% | 2.99 | +5.0% |
| Draw | 33.1% | 31.1% | 3.16 | +4.6% |
| Rayo Vallecano win | 31.8% | 36.0% | 2.74 | -12.9% |

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
| Market best home last update utc | 2026-10-14T18:12:58Z |
| Market best draw last update utc | 2026-10-14T18:12:58Z |
| Market best away last update utc | 2026-10-14T18:12:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 31.0% |
| P btts no | 69.0% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.41 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.31 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.78 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.55 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.1% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.3% |
| P home draw | 68.2% |
| P draw away | 64.9% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.99 |
| Reference draw odds | 3.16 |
| Reference away odds | 2.74 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 2.45 |
| Reference Under 2.5 odds | 1.51 |
| Home probability edge | +2.2% |
| Draw probability edge | +2.0% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -13.6% |
| Under 2.5 probability edge | +13.6% |
| Raw edge prob home | 0.0437 |
| Raw ev home | 0.1149 |
| Raw edge prob draw | 0.0397 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0834 |
| Raw ev away | -0.2431 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.7%**. Expected goals are 1.29 for Levante and 1.39 for Athletic Bilbao (2.68 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 50.0%; Under 3.5 goals: 71.8%; Double Chance 1X: 58.3%; Double Chance X2: 68.8%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 31.2% | 3.21 |
| Draw | 27.1% | 3.68 |
| Athletic Bilbao win | 41.7% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.29 |
| Athletic Bilbao expected goals | 1.39 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 50.0% |
| Under 2.5 | 50.0% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.90% |
| 2 | 0-1 | 9.87% |
| 3 | 1-2 | 9.10% |
| 4 | 1-0 | 7.77% |
| 5 | 0-0 | 7.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 31.2% | 27.9% | 3.52 | +9.8% |
| Draw | 27.1% | 27.9% | 3.52 | -4.5% |
| Athletic Bilbao win | 41.7% | 44.2% | 2.24 | -6.7% |
| Over 2.5 | 50.0% | 48.7% | 2.02 | +0.9% |
| Under 2.5 | 50.0% | 51.3% | 1.92 | -3.9% |

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
| Market best home last update utc | 2026-10-14T18:12:58Z |
| Market best draw last update utc | 2026-10-14T18:12:58Z |
| Market best away last update utc | 2026-10-14T18:12:58Z |
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
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.71 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.48 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 54.7% |
| P home draw | 58.3% |
| P draw away | 68.8% |
| Raw p home draw | 60.8% |
| Raw p draw away | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.52 |
| Reference draw odds | 3.52 |
| Reference away odds | 2.24 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.92 |
| Home probability edge | +3.3% |
| Draw probability edge | -0.8% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | 0.0655 |
| Raw ev home | 0.2136 |
| Raw edge prob draw | -0.0156 |
| Raw ev draw | -0.0719 |
| Raw edge prob away | -0.0500 |
| Raw ev away | -0.1229 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **56.4%**. Expected goals are 1.38 for Alavés and 0.44 for Málaga (1.82 combined). The most likely exact score is 1-0 at 20.7%. Goal-market probabilities: at least one goal: 84.1%; Over 2.5 goals: 27.1%; Under 3.5 goals: 89.2%; Double Chance 1X: 83.6%; Double Chance X2: 43.6%; Under 4.5 goals: 96.3%; BTTS Yes (both teams score): 26.7%; BTTS No (at least one team does not score): 73.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 56.4% | 1.77 |
| Draw | 27.2% | 3.68 |
| Málaga win | 16.4% | 6.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.38 |
| Málaga expected goals | 0.44 |
| Expected total goals | 1.82 |
| Over 0.5 | 84.1% |
| Under 0.5 | 15.9% |
| Over 1.5 | 53.4% |
| Under 1.5 | 46.6% |
| Over 2.5 | 27.1% |
| Under 2.5 | 72.9% |
| Over 3.5 | 10.8% |
| Under 3.5 | 89.2% |
| Over 4.5 | 3.7% |
| Under 4.5 | 96.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.74% |
| 2 | 0-0 | 15.94% |
| 3 | 2-0 | 14.42% |
| 4 | 0-1 | 9.90% |
| 5 | 1-1 | 9.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 56.4% | 52.4% | 1.89 | +6.6% |
| Draw | 27.2% | 26.3% | 3.73 | +1.3% |
| Málaga win | 16.4% | 21.4% | 4.57 | -24.9% |
| Over 2.5 | 27.1% | 47.5% | 2.07 | -43.9% |
| Under 2.5 | 72.9% | 52.5% | 1.88 | +37.1% |

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
| Market best home last update utc | 2026-10-14T18:12:58Z |
| Market best draw last update utc | 2026-10-14T18:12:58Z |
| Market best away last update utc | 2026-10-14T18:12:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 26.7% |
| P btts no | 73.3% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.27 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.69 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.30 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 27.36 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 54.4% |
| Raw p under 3 5 | 88.9% |
| Raw p btts yes | 26.7% |
| P home draw | 83.6% |
| P draw away | 43.6% |
| Raw p home draw | 88.5% |
| Raw p draw away | 39.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.89 |
| Reference draw odds | 3.73 |
| Reference away odds | 4.57 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.07 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +4.0% |
| Draw probability edge | +0.9% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -20.5% |
| Under 2.5 probability edge | +20.5% |
| Raw edge prob home | 0.0807 |
| Raw ev home | 0.1426 |
| Raw edge prob draw | 0.0180 |
| Raw ev draw | 0.0465 |
| Raw edge prob away | -0.0987 |
| Raw ev away | -0.4749 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **49.5%**. Expected goals are 1.39 for Rayo Vallecano and 1.06 for Elche CF (2.46 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 45.1%; Under 3.5 goals: 76.4%; Double Chance 1X: 75.6%; Double Chance X2: 50.5%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 49.1%; BTTS No (at least one team does not score): 50.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 49.5% | 2.02 |
| Draw | 26.1% | 3.83 |
| Elche CF win | 24.4% | 4.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.39 |
| Elche CF expected goals | 1.06 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 70.9% |
| Under 1.5 | 29.1% |
| Over 2.5 | 45.1% |
| Under 2.5 | 54.9% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.07% |
| 2 | 1-1 | 12.36% |
| 3 | 2-1 | 9.90% |
| 4 | 2-0 | 9.31% |
| 5 | 0-0 | 8.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 49.5% | 54.7% | 1.81 | -10.4% |
| Draw | 26.1% | 24.8% | 3.94 | +2.8% |
| Elche CF win | 24.4% | 20.4% | 4.78 | +16.8% |
| Over 2.5 | 45.1% | 52.5% | 1.88 | -15.3% |
| Under 2.5 | 54.9% | 47.5% | 2.07 | +13.7% |

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
| Market best home last update utc | 2026-10-14T18:12:58Z |
| Market best draw last update utc | 2026-10-14T18:12:58Z |
| Market best away last update utc | 2026-10-14T18:12:58Z |
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
| P btts yes | 49.1% |
| P btts no | 50.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.88 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.44 |
| Fair Over 2.5 odds | 2.22 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.50 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 44.2% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 28.5% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 49.5% |
| P home draw | 75.6% |
| P draw away | 50.5% |
| Raw p home draw | 71.5% |
| Raw p draw away | 55.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.81 |
| Reference draw odds | 3.94 |
| Reference away odds | 4.78 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 2.07 |
| Home probability edge | -5.3% |
| Draw probability edge | +1.2% |
| Away probability edge | +4.0% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.1051 |
| Raw ev home | -0.1995 |
| Raw edge prob draw | 0.0248 |
| Raw ev draw | 0.0766 |
| Raw edge prob away | 0.0803 |
| Raw ev away | 0.3599 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **39.4%**. Expected goals are 1.96 for Real Racing Club de Santander and 1.99 for Espanyol (3.95 combined). The most likely exact score is 1-1 at 8.6%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 74.8%; Under 3.5 goals: 44.3%; Double Chance 1X: 63.1%; Double Chance X2: 60.6%; Under 4.5 goals: 64.4%; BTTS Yes (both teams score): 74.9%; BTTS No (at least one team does not score): 25.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 39.4% | 2.54 |
| Draw | 23.8% | 4.21 |
| Espanyol win | 36.9% | 2.71 |

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
| Over 2.5 | 74.8% |
| Under 2.5 | 25.2% |
| Over 3.5 | 55.7% |
| Under 3.5 | 44.3% |
| Over 4.5 | 35.6% |
| Under 4.5 | 64.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.60% |
| 2 | 2-2 | 8.24% |
| 3 | 2-1 | 7.46% |
| 4 | 1-2 | 6.87% |
| 5 | 3-1 | 4.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 39.4% | 40.0% | 2.47 | -2.8% |
| Draw | 23.8% | 26.4% | 3.72 | -11.6% |
| Espanyol win | 36.9% | 33.6% | 2.93 | +8.1% |
| Over 2.5 | 74.8% | 55.5% | 1.78 | +33.1% |
| Under 2.5 | 25.2% | 44.5% | 2.21 | -44.3% |

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
| Market best home last update utc | 2026-10-14T18:12:58Z |
| Market best draw last update utc | 2026-10-14T18:12:58Z |
| Market best away last update utc | 2026-10-14T18:12:58Z |
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
| P btts yes | 74.9% |
| P btts no | 25.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.00 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 10.67 |
| Fair Over 2.5 odds | 1.34 |
| Fair Under 2.5 odds | 3.97 |
| Fair Over 3.5 odds | 1.80 |
| Fair Under 3.5 odds | 2.26 |
| Fair Over 4.5 odds | 2.81 |
| Fair Under 4.5 odds | 1.55 |
| Unadjusted home-win probability | 38.7% |
| Unadjusted draw probability | 21.1% |
| Unadjusted away-win probability | 40.1% |
| Raw p over 1 5 | 90.6% |
| Raw p under 3 5 | 44.3% |
| Raw p btts yes | 74.4% |
| P home draw | 63.1% |
| P draw away | 60.6% |
| Raw p home draw | 59.9% |
| Raw p draw away | 61.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.47 |
| Reference draw odds | 3.72 |
| Reference away odds | 2.93 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.21 |
| Home probability edge | -0.6% |
| Draw probability edge | -2.6% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | +19.3% |
| Under 2.5 probability edge | -19.3% |
| Raw edge prob home | -0.0125 |
| Raw ev home | -0.0433 |
| Raw edge prob draw | -0.0527 |
| Raw ev draw | -0.2140 |
| Raw edge prob away | 0.0651 |
| Raw ev away | 0.1760 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **44.9%**. Expected goals are 1.33 for Valencia and 1.62 for Villarreal (2.95 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.4%; Under 3.5 goals: 65.8%; Double Chance 1X: 55.1%; Double Chance X2: 70.2%; Under 4.5 goals: 82.4%; BTTS Yes (both teams score): 59.3%; BTTS No (at least one team does not score): 40.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.8% | 3.36 |
| Draw | 25.3% | 3.95 |
| Villarreal win | 44.9% | 2.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.33 |
| Villarreal expected goals | 1.62 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 56.4% |
| Under 2.5 | 43.6% |
| Over 3.5 | 34.2% |
| Under 3.5 | 65.8% |
| Over 4.5 | 17.6% |
| Under 4.5 | 82.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.79% |
| 2 | 1-2 | 9.29% |
| 3 | 0-1 | 8.40% |
| 4 | 2-1 | 7.16% |
| 5 | 0-2 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.8% | 28.5% | 3.45 | +2.8% |
| Draw | 25.3% | 26.0% | 3.78 | -4.3% |
| Villarreal win | 44.9% | 45.6% | 2.17 | -2.6% |
| Over 2.5 | 56.4% | 55.4% | 1.78 | +0.3% |
| Under 2.5 | 43.6% | 44.6% | 2.20 | -4.0% |

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
| Market best home last update utc | 2026-10-14T18:12:58Z |
| Market best draw last update utc | 2026-10-14T18:12:58Z |
| Market best away last update utc | 2026-10-14T18:12:58Z |
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
| P btts yes | 59.3% |
| P btts no | 40.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.87 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.90 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 2.93 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.69 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 24.7% |
| Unadjusted away-win probability | 44.2% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 59.2% |
| P home draw | 55.1% |
| P draw away | 70.2% |
| Raw p home draw | 55.8% |
| Raw p draw away | 68.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.45 |
| Reference draw odds | 3.78 |
| Reference away odds | 2.17 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +1.3% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | 0.0262 |
| Raw ev home | 0.0727 |
| Raw edge prob draw | -0.0127 |
| Raw ev draw | -0.0669 |
| Raw edge prob away | -0.0135 |
| Raw ev away | -0.0404 |

</details>


---
