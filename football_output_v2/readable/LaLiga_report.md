# La Liga — football model report

Fixtures in this report: **16**.

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
| Live odds matched | 16.00 |
| Additional event odds calls used before this league | 5.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
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

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **49.9%**. Expected goals are 2.04 for Deportivo La Coruña and 1.32 for Levante (3.36 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.0%; Double Chance 1X: 74.3%; Double Chance X2: 50.1%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 49.9% | 2.00 |
| Draw | 24.3% | 4.11 |
| Levante win | 25.7% | 3.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 2.04 |
| Levante expected goals | 1.32 |
| Expected total goals | 3.36 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 84.9% |
| Under 1.5 | 15.1% |
| Over 2.5 | 64.3% |
| Under 2.5 | 35.7% |
| Over 3.5 | 43.0% |
| Under 3.5 | 57.0% |
| Over 4.5 | 24.3% |
| Under 4.5 | 75.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.68% |
| 2 | 2-1 | 8.83% |
| 3 | 2-2 | 7.06% |
| 4 | 2-0 | 6.69% |
| 5 | 1-2 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 49.9% | 45.9% | 2.17 | +8.3% |
| Draw | 24.3% | 27.0% | 3.62 | -11.9% |
| Levante win | 25.7% | 27.1% | 3.60 | -7.3% |
| Over 2.5 | 64.3% | 49.7% | 1.98 | +27.4% |
| Under 2.5 | 35.7% | 50.3% | 1.96 | -30.1% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
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
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.43 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.61 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.12 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 53.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 64.0% |
| P home draw | 74.3% |
| P draw away | 50.1% |
| Raw p home draw | 75.6% |
| Raw p draw away | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.11 |
| Reference draw odds | 3.52 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.90 |
| Home probability edge | +4.0% |
| Draw probability edge | -2.6% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | +14.6% |
| Under 2.5 probability edge | -14.6% |
| Raw edge prob home | 0.0795 |
| Raw ev home | 0.1693 |
| Raw edge prob draw | -0.0522 |
| Raw ev draw | -0.2133 |
| Raw edge prob away | -0.0273 |
| Raw ev away | -0.1223 |
| Market p home draw | 72.4% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:06:34Z |
| Market reference home draw last update utc | 2026-10-14T19:07:09Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.7% |
| Market draw away odds | 1.77 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:06:34Z |
| Market reference draw away last update utc | 2026-10-14T19:07:09Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.76 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 75.3% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:06:10Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.5% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:06:10Z |
| Market reference under 3 5 odds | 1.30 |
| Market reference under 3 5 opposite odds | 3.10 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.7% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:06:34Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **53.0%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 0-1 at 12.0%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 48.7%; Under 3.5 goals: 73.2%; Double Chance 1X: 47.0%; Double Chance X2: 78.0%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 22.0% | 4.55 |
| Draw | 25.1% | 3.99 |
| Atlético Madrid win | 53.0% | 1.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.02 |
| Atlético Madrid expected goals | 1.59 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.7% |
| Under 2.5 | 51.3% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.05% |
| 2 | 1-1 | 11.93% |
| 3 | 1-2 | 10.00% |
| 4 | 0-2 | 9.76% |
| 5 | 0-0 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 22.0% | 19.7% | 4.88 | +7.2% |
| Draw | 25.1% | 24.6% | 3.94 | -1.2% |
| Atlético Madrid win | 53.0% | 55.8% | 1.80 | -4.7% |
| Over 2.5 | 48.7% | 52.9% | 1.87 | -8.9% |
| Under 2.5 | 51.3% | 47.1% | 2.08 | +6.6% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
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
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.46 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.97 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.2% |
| P home draw | 47.0% |
| P draw away | 78.0% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.75 |
| Reference draw odds | 3.84 |
| Reference away odds | 1.75 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.02 |
| Home probability edge | +2.3% |
| Draw probability edge | +0.5% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | 0.0458 |
| Raw ev home | 0.1834 |
| Raw edge prob draw | 0.0102 |
| Raw ev draw | 0.0080 |
| Raw edge prob away | -0.0560 |
| Raw ev away | -0.0970 |
| Market p home draw | 45.2% |
| Market home draw odds | 2.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:06:34Z |
| Market reference home draw last update utc | 2026-10-14T19:07:09Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 79.6% |
| Market draw away odds | 1.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:06:34Z |
| Market reference draw away last update utc | 2026-10-14T19:07:09Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.13 |
| Market reference dc draw away odds | 1.21 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 77.8% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:06:59Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.0% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:06:59Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 2.83 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.7% |
| Market btts yes odds | 1.73 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:06:34Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.05 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **60.8%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.4%; Under 3.5 goals: 54.8%; Double Chance 1X: 39.2%; Double Chance X2: 80.2%; Under 4.5 goals: 73.3%; BTTS Yes (both teams score): 64.2%; BTTS No (at least one team does not score): 35.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.8% | 5.04 |
| Draw | 19.4% | 5.15 |
| Barcelona win | 60.8% | 1.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.35 |
| Barcelona expected goals | 2.07 |
| Expected total goals | 3.42 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 45.2% |
| Under 3.5 | 54.8% |
| Over 4.5 | 26.7% |
| Under 4.5 | 73.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.67% |
| 2 | 1-1 | 8.40% |
| 3 | 0-2 | 7.89% |
| 4 | 0-1 | 7.42% |
| 5 | 1-3 | 7.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.8% | 15.1% | 6.21 | +23.1% |
| Draw | 19.4% | 17.3% | 5.44 | +5.6% |
| Barcelona win | 60.8% | 67.6% | 1.49 | -9.5% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.2% |
| P btts no | 35.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.19 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.18 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.75 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 24.6% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 55.3% |
| Raw p btts yes | 65.0% |
| P home draw | 39.2% |
| P draw away | 80.2% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 6.05 |
| Reference draw odds | 5.30 |
| Reference away odds | 1.45 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Home probability edge | +4.8% |
| Draw probability edge | +2.1% |
| Away probability edge | -6.9% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | 0.0955 |
| Raw ev home | 0.5275 |
| Raw edge prob draw | 0.0423 |
| Raw ev draw | 0.1711 |
| Raw edge prob away | -0.1377 |
| Raw ev away | -0.1973 |
| Market p home draw | 33.8% |
| Market home draw odds | 2.82 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:06:34Z |
| Market reference home draw last update utc | 2026-10-14T19:07:09Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.2% |
| Market draw away odds | 1.15 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:06:34Z |
| Market reference draw away last update utc | 2026-10-14T19:07:09Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.84 |
| Market reference dc draw away odds | 1.14 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 92.4% |
| Market over 1 5 odds | 1.02 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:05:20Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 9.00 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 43.1% |
| Market under 3 5 odds | 2.19 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:05:20Z |
| Market reference under 3 5 odds | 2.09 |
| Market reference under 3 5 opposite odds | 1.64 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:06:34Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.90 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **40.8%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 39.1%; Under 3.5 goals: 81.1%; Double Chance 1X: 59.2%; Double Chance X2: 69.4%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.6% | 3.27 |
| Draw | 28.6% | 3.50 |
| Athletic Bilbao win | 40.8% | 2.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.07 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 18.9% |
| Under 3.5 | 81.1% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.25% |
| 2 | 0-1 | 13.17% |
| 3 | 0-0 | 10.63% |
| 4 | 1-0 | 10.34% |
| 5 | 1-2 | 8.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.6% | 28.2% | 3.47 | +6.2% |
| Draw | 28.6% | 27.8% | 3.51 | +0.3% |
| Athletic Bilbao win | 40.8% | 44.0% | 2.26 | -7.7% |
| Over 2.5 | 39.1% | 46.8% | 2.10 | -17.9% |
| Under 2.5 | 60.9% | 53.2% | 1.86 | +13.3% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
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
| Fair Under 0.5 odds | 9.41 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.28 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.88 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 45.6% |
| P home draw | 59.2% |
| P draw away | 69.4% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.38 |
| Reference draw odds | 3.42 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.80 |
| Home probability edge | +2.5% |
| Draw probability edge | +0.7% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.0491 |
| Raw ev home | 0.1475 |
| Raw edge prob draw | 0.0149 |
| Raw ev draw | 0.0287 |
| Raw edge prob away | -0.0640 |
| Raw ev away | -0.1497 |
| Market p home draw | 56.2% |
| Market home draw odds | 1.72 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:06:34Z |
| Market reference home draw last update utc | 2026-10-14T19:07:09Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.7% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:06:34Z |
| Market reference draw away last update utc | 2026-10-14T19:07:09Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.71 |
| Market reference dc draw away odds | 1.34 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 72.9% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:06:38Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.25 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.1% |
| Market under 3 5 odds | 1.25 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:06:38Z |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 3.35 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.2% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:06:34Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 1.95 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.5%**. Expected goals are 2.41 for Villarreal and 1.19 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 69.7%; Under 3.5 goals: 51.4%; Double Chance 1X: 84.5%; Double Chance X2: 34.5%; Under 4.5 goals: 70.6%; BTTS Yes (both teams score): 63.4%; BTTS No (at least one team does not score): 36.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.5% | 1.53 |
| Draw | 19.0% | 5.26 |
| Elche CF win | 15.5% | 6.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.41 |
| Elche CF expected goals | 1.19 |
| Expected total goals | 3.60 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 69.7% |
| Under 2.5 | 30.3% |
| Over 3.5 | 48.6% |
| Under 3.5 | 51.4% |
| Over 4.5 | 29.4% |
| Under 4.5 | 70.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.62% |
| 2 | 1-1 | 8.16% |
| 3 | 2-0 | 8.11% |
| 4 | 3-1 | 7.74% |
| 5 | 1-0 | 6.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.5% | 66.7% | 1.51 | -1.1% |
| Draw | 19.0% | 19.4% | 4.88 | -7.2% |
| Elche CF win | 15.5% | 13.9% | 6.73 | +4.1% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.4% |
| P btts no | 36.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.85 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.12 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.30 |
| Fair Over 3.5 odds | 2.06 |
| Fair Under 3.5 odds | 1.95 |
| Fair Over 4.5 odds | 3.40 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 63.4% |
| P home draw | 84.5% |
| P draw away | 34.5% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.47 |
| Reference draw odds | 4.75 |
| Reference away odds | 6.55 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | -1.2% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | +2.9% |
| Under 2.5 probability edge | -2.9% |
| Raw edge prob home | -0.0235 |
| Raw ev home | -0.0284 |
| Raw edge prob draw | -0.0084 |
| Raw ev draw | -0.0924 |
| Raw edge prob away | 0.0319 |
| Raw ev away | 0.1480 |
| Market p home draw | 85.8% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-14T19:06:34Z |
| Market reference home draw last update utc | 2026-10-14T19:07:09Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.7% |
| Market draw away odds | 2.75 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-14T19:06:34Z |
| Market reference draw away last update utc | 2026-10-14T19:07:09Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.12 |
| Market reference dc draw away odds | 2.77 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 87.5% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-14T19:06:39Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.4% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-14T19:06:39Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.07 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-14T19:06:34Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **56.0%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.33 combined). The most likely exact score is 2-2 at 7.7%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.2%; Under 3.5 goals: 38.0%; Double Chance 1X: 77.7%; Double Chance X2: 44.0%; Under 4.5 goals: 58.0%; BTTS Yes (both teams score): 75.2%; BTTS No (at least one team does not score): 24.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 56.0% | 1.78 |
| Draw | 21.7% | 4.61 |
| Real Racing Club de Santander win | 22.3% | 4.49 |

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
| 1 | 2-2 | 7.70% |
| 2 | 1-1 | 7.31% |
| 3 | 2-1 | 7.00% |
| 4 | 3-1 | 6.48% |
| 5 | 1-2 | 5.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 56.0% | 48.8% | 2.04 | +14.3% |
| Draw | 21.7% | 26.2% | 3.72 | -19.3% |
| Real Racing Club de Santander win | 22.3% | 25.0% | 3.88 | -13.6% |
| Over 2.5 | 79.2% | 57.0% | 1.74 | +37.8% |
| Under 2.5 | 20.8% | 43.0% | 2.27 | -52.7% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
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
| Fair Under 0.5 odds | 55.22 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.94 |
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
| P home draw | 77.7% |
| P draw away | 44.0% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.99 |
| Reference draw odds | 3.62 |
| Reference away odds | 3.78 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +7.2% |
| Draw probability edge | -4.5% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | +22.2% |
| Under 2.5 probability edge | -22.2% |
| Raw edge prob home | 0.1445 |
| Raw ev home | 0.2905 |
| Raw edge prob draw | -0.0896 |
| Raw ev draw | -0.3599 |
| Raw edge prob away | -0.0548 |
| Raw ev away | -0.2422 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **47.9%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 43.6%; Under 3.5 goals: 77.3%; Double Chance 1X: 75.3%; Double Chance X2: 52.1%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 47.9% | 2.09 |
| Draw | 27.4% | 3.65 |
| Alavés win | 24.7% | 4.05 |

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
| 1 | 1-1 | 12.92% |
| 2 | 1-0 | 12.36% |
| 3 | 2-0 | 9.40% |
| 4 | 0-0 | 9.25% |
| 5 | 2-1 | 8.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 47.9% | 46.2% | 2.16 | +3.5% |
| Draw | 27.4% | 28.1% | 3.48 | -4.7% |
| Alavés win | 24.7% | 25.7% | 3.78 | -6.7% |
| Over 2.5 | 43.6% | 42.3% | 2.30 | +0.4% |
| Under 2.5 | 56.4% | 57.7% | 1.72 | -3.0% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
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
| Fair Under 0.5 odds | 10.81 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.29 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.08 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 47.6% |
| P home draw | 75.3% |
| P draw away | 52.1% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.10 |
| Reference draw odds | 3.38 |
| Reference away odds | 3.68 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.23 |
| Reference Under 2.5 odds | 1.67 |
| Home probability edge | +1.8% |
| Draw probability edge | -0.7% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | 0.0355 |
| Raw ev home | 0.0737 |
| Raw edge prob draw | -0.0146 |
| Raw ev draw | -0.0724 |
| Raw edge prob away | -0.0209 |
| Raw ev away | -0.1065 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **47.5%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.4%. Goal-market probabilities: at least one goal: 85.5%; Over 2.5 goals: 29.4%; Under 3.5 goals: 87.9%; Double Chance 1X: 52.5%; Double Chance X2: 76.0%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.4%; BTTS No (at least one team does not score): 66.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 24.0% | 4.17 |
| Draw | 28.5% | 3.51 |
| Real Sociedad win | 47.5% | 2.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.5% |
| Under 0.5 | 14.5% |
| Over 1.5 | 56.0% |
| Under 1.5 | 44.0% |
| Over 2.5 | 29.4% |
| Under 2.5 | 70.6% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.35% |
| 2 | 0-0 | 14.52% |
| 3 | 1-0 | 12.17% |
| 4 | 1-1 | 11.52% |
| 5 | 0-2 | 11.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 24.0% | 29.8% | 3.29 | -21.1% |
| Draw | 28.5% | 26.8% | 3.63 | +3.4% |
| Real Sociedad win | 47.5% | 43.4% | 2.29 | +8.8% |
| Over 2.5 | 29.4% | 53.2% | 1.86 | -45.2% |
| Under 2.5 | 70.6% | 46.8% | 2.10 | +48.2% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
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
| Fair Under 0.5 odds | 6.89 |
| Fair Over 1.5 odds | 1.79 |
| Fair Under 1.5 odds | 2.27 |
| Fair Over 2.5 odds | 3.40 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.28 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.33 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 52.5% |
| P draw away | 76.0% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.20 |
| Reference draw odds | 3.54 |
| Reference away odds | 2.23 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.03 |
| Home probability edge | -5.8% |
| Draw probability edge | +1.7% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -23.8% |
| Under 2.5 probability edge | +23.8% |
| Raw edge prob home | -0.1160 |
| Raw ev home | -0.4013 |
| Raw edge prob draw | 0.0332 |
| Raw ev draw | 0.0939 |
| Raw edge prob away | 0.0828 |
| Raw ev away | 0.1832 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **77.5%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.5%; Under 3.5 goals: 56.6%; Double Chance 1X: 91.8%; Double Chance X2: 22.5%; Under 4.5 goals: 75.0%; BTTS Yes (both teams score): 48.7%; BTTS No (at least one team does not score): 51.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.5% | 1.29 |
| Draw | 14.3% | 7.00 |
| Sevilla win | 8.2% | 12.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.63 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 65.5% |
| Under 2.5 | 34.5% |
| Over 3.5 | 43.4% |
| Under 3.5 | 56.6% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.89% |
| 2 | 3-0 | 10.41% |
| 3 | 1-0 | 8.92% |
| 4 | 2-1 | 8.82% |
| 5 | 3-1 | 7.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.5% | 77.5% | 1.30 | +0.7% |
| Draw | 14.3% | 14.1% | 6.61 | -5.5% |
| Sevilla win | 8.2% | 8.4% | 10.70 | -12.1% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.7% |
| P btts no | 51.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.33 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.70 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 4.00 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.7% |
| P home draw | 91.8% |
| P draw away | 22.5% |
| Raw p home draw | 91.9% |
| Raw p draw away | 22.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.27 |
| Reference draw odds | 6.30 |
| Reference away odds | 10.25 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | -0.0% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0008 |
| Raw ev home | 0.0068 |
| Raw edge prob draw | 0.0042 |
| Raw ev draw | -0.0414 |
| Raw edge prob away | -0.0034 |
| Raw ev away | -0.1385 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.1%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.5%. Goal-market probabilities: at least one goal: 81.5%; Over 2.5 goals: 23.2%; Under 3.5 goals: 91.5%; Double Chance 1X: 68.2%; Double Chance X2: 64.9%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 30.9%; BTTS No (at least one team does not score): 69.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.1% | 2.85 |
| Draw | 33.1% | 3.02 |
| Rayo Vallecano win | 31.8% | 3.14 |

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
| 1 | 0-0 | 18.47% |
| 2 | 1-0 | 16.27% |
| 3 | 0-1 | 16.10% |
| 4 | 1-1 | 12.41% |
| 5 | 2-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.1% | 32.9% | 2.99 | +5.0% |
| Draw | 33.1% | 31.0% | 3.16 | +4.5% |
| Rayo Vallecano win | 31.8% | 36.0% | 2.74 | -12.8% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 30.9% |
| P btts no | 69.1% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.41 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.31 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.78 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.54 |
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
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.91 |
| Reference draw odds | 3.08 |
| Reference away odds | 2.67 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.60 |
| Reference Under 2.5 odds | 1.51 |
| Home probability edge | +2.2% |
| Draw probability edge | +2.0% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | 0.0435 |
| Raw ev home | 0.1149 |
| Raw edge prob draw | 0.0404 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0839 |
| Raw ev away | -0.2431 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.8%**. Expected goals are 1.29 for Levante and 1.39 for Athletic Bilbao (2.68 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 50.0%; Under 3.5 goals: 71.8%; Double Chance 1X: 58.2%; Double Chance X2: 68.9%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 31.1% | 3.21 |
| Draw | 27.1% | 3.69 |
| Athletic Bilbao win | 41.8% | 2.39 |

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
| 1 | 1-1 | 12.87% |
| 2 | 0-1 | 9.90% |
| 3 | 1-2 | 9.12% |
| 4 | 1-0 | 7.75% |
| 5 | 0-0 | 7.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 31.1% | 27.8% | 3.52 | +9.6% |
| Draw | 27.1% | 27.8% | 3.52 | -4.7% |
| Athletic Bilbao win | 41.8% | 44.4% | 2.24 | -6.4% |
| Over 2.5 | 50.0% | 48.6% | 2.02 | +1.0% |
| Under 2.5 | 50.0% | 51.4% | 1.92 | -4.0% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
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
| Fair Under 0.5 odds | 13.75 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.47 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 54.7% |
| P home draw | 58.2% |
| P draw away | 68.9% |
| Raw p home draw | 60.8% |
| Raw p draw away | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.42 |
| Reference draw odds | 3.42 |
| Reference away odds | 2.18 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.86 |
| Home probability edge | +3.3% |
| Draw probability edge | -0.7% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | +1.4% |
| Under 2.5 probability edge | -1.4% |
| Raw edge prob home | 0.0669 |
| Raw ev home | 0.2136 |
| Raw edge prob draw | -0.0143 |
| Raw ev draw | -0.0719 |
| Raw edge prob away | -0.0526 |
| Raw ev away | -0.1229 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **56.7%**. Expected goals are 1.38 for Alavés and 0.44 for Málaga (1.82 combined). The most likely exact score is 1-0 at 20.8%. Goal-market probabilities: at least one goal: 84.1%; Over 2.5 goals: 27.1%; Under 3.5 goals: 89.2%; Double Chance 1X: 83.7%; Double Chance X2: 43.3%; Under 4.5 goals: 96.3%; BTTS Yes (both teams score): 26.7%; BTTS No (at least one team does not score): 73.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 56.7% | 1.76 |
| Draw | 27.0% | 3.70 |
| Málaga win | 16.3% | 6.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.38 |
| Málaga expected goals | 0.44 |
| Expected total goals | 1.82 |
| Over 0.5 | 84.1% |
| Under 0.5 | 15.9% |
| Over 1.5 | 53.5% |
| Under 1.5 | 46.5% |
| Over 2.5 | 27.1% |
| Under 2.5 | 72.9% |
| Over 3.5 | 10.8% |
| Under 3.5 | 89.2% |
| Over 4.5 | 3.7% |
| Under 4.5 | 96.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.85% |
| 2 | 0-0 | 15.86% |
| 3 | 2-0 | 14.49% |
| 4 | 0-1 | 9.81% |
| 5 | 1-1 | 9.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 56.7% | 52.9% | 1.89 | +7.2% |
| Draw | 27.0% | 26.0% | 3.73 | +0.8% |
| Málaga win | 16.3% | 21.1% | 4.57 | -25.6% |
| Over 2.5 | 27.1% | 47.3% | 2.07 | -43.8% |
| Under 2.5 | 72.9% | 52.7% | 1.88 | +37.0% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
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
| Fair Under 0.5 odds | 6.31 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.68 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.28 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 27.27 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 54.4% |
| Raw p under 3 5 | 88.9% |
| Raw p btts yes | 26.7% |
| P home draw | 83.7% |
| P draw away | 43.3% |
| Raw p home draw | 88.5% |
| Raw p draw away | 39.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.84 |
| Reference draw odds | 3.64 |
| Reference away odds | 4.45 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.01 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +3.8% |
| Draw probability edge | +1.0% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -20.2% |
| Under 2.5 probability edge | +20.2% |
| Raw edge prob home | 0.0751 |
| Raw ev home | 0.1426 |
| Raw edge prob draw | 0.0207 |
| Raw ev draw | 0.0465 |
| Raw edge prob away | -0.0958 |
| Raw ev away | -0.4749 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **73.9%**. Expected goals are 2.31 for Atlético Madrid and 0.98 for Deportivo La Coruña (3.29 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 65.3%; Under 3.5 goals: 57.2%; Double Chance 1X: 89.9%; Double Chance X2: 26.1%; Under 4.5 goals: 75.5%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 73.9% | 1.35 |
| Draw | 16.0% | 6.24 |
| Deportivo La Coruña win | 10.1% | 9.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.31 |
| Deportivo La Coruña expected goals | 0.98 |
| Expected total goals | 3.29 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 84.9% |
| Under 1.5 | 15.1% |
| Over 2.5 | 65.3% |
| Under 2.5 | 34.7% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.5% |
| Under 4.5 | 75.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.95% |
| 2 | 2-1 | 10.74% |
| 3 | 1-0 | 9.29% |
| 4 | 3-0 | 8.43% |
| 5 | 3-1 | 8.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 73.9% | 80.8% | 1.24 | -8.4% |
| Draw | 16.0% | 13.4% | 6.92 | +10.8% |
| Deportivo La Coruña win | 10.1% | 5.9% | 14.90 | +50.8% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 55.4% |
| P btts no | 44.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.97 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.63 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.88 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.08 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 67.0% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 14.4% |
| Raw p over 1 5 | 84.2% |
| Raw p under 3 5 | 58.2% |
| Raw p btts yes | 56.5% |
| P home draw | 89.9% |
| P draw away | 26.1% |
| Raw p home draw | 85.6% |
| Raw p draw away | 33.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.22 |
| Reference draw odds | 6.50 |
| Reference away odds | 14.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -6.9% |
| Draw probability edge | +2.6% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | +2.7% |
| Under 2.5 probability edge | -2.7% |
| Raw edge prob home | -0.1379 |
| Raw ev home | -0.1696 |
| Raw edge prob draw | 0.0528 |
| Raw ev draw | 0.2910 |
| Raw edge prob away | 0.0851 |
| Raw ev away | 1.1422 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **49.8%**. Expected goals are 1.39 for Rayo Vallecano and 1.06 for Elche CF (2.46 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 45.1%; Under 3.5 goals: 76.4%; Double Chance 1X: 75.7%; Double Chance X2: 50.2%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 49.1%; BTTS No (at least one team does not score): 50.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 49.8% | 2.01 |
| Draw | 25.9% | 3.86 |
| Elche CF win | 24.3% | 4.12 |

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
| 1 | 1-0 | 13.16% |
| 2 | 1-1 | 12.29% |
| 3 | 2-1 | 9.97% |
| 4 | 2-0 | 9.37% |
| 5 | 0-0 | 8.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 49.8% | 55.4% | 1.81 | -9.8% |
| Draw | 25.9% | 24.5% | 3.94 | +2.1% |
| Elche CF win | 24.3% | 20.1% | 4.78 | +16.0% |
| Over 2.5 | 45.1% | 52.7% | 1.88 | -15.1% |
| Under 2.5 | 54.9% | 47.3% | 2.07 | +13.6% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
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
| Fair Under 0.5 odds | 11.96 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.44 |
| Fair Over 2.5 odds | 2.22 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.48 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 44.2% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 28.5% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 49.5% |
| P home draw | 75.7% |
| P draw away | 50.2% |
| Raw p home draw | 71.5% |
| Raw p draw away | 55.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.76 |
| Reference draw odds | 3.84 |
| Reference away odds | 4.65 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.01 |
| Home probability edge | -5.6% |
| Draw probability edge | +1.4% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | -0.1118 |
| Raw ev home | -0.1995 |
| Raw edge prob draw | 0.0280 |
| Raw ev draw | 0.0766 |
| Raw edge prob away | 0.0837 |
| Raw ev away | 0.3599 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **39.5%**. Expected goals are 1.96 for Real Racing Club de Santander and 1.99 for Espanyol (3.95 combined). The most likely exact score is 1-1 at 8.6%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 74.8%; Under 3.5 goals: 44.3%; Double Chance 1X: 63.1%; Double Chance X2: 60.5%; Under 4.5 goals: 64.3%; BTTS Yes (both teams score): 74.9%; BTTS No (at least one team does not score): 25.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 39.5% | 2.53 |
| Draw | 23.7% | 4.23 |
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
| Over 4.5 | 35.7% |
| Under 4.5 | 64.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.56% |
| 2 | 2-2 | 8.20% |
| 3 | 2-1 | 7.48% |
| 4 | 1-2 | 6.87% |
| 5 | 3-1 | 4.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 39.5% | 40.2% | 2.47 | -2.5% |
| Draw | 23.7% | 26.2% | 3.72 | -12.0% |
| Espanyol win | 36.9% | 33.6% | 2.93 | +8.0% |
| Over 2.5 | 74.8% | 55.7% | 1.78 | +33.2% |
| Under 2.5 | 25.2% | 44.3% | 2.21 | -44.3% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
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
| Fair Under 0.5 odds | 43.17 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 10.67 |
| Fair Over 2.5 odds | 1.34 |
| Fair Under 2.5 odds | 3.97 |
| Fair Over 3.5 odds | 1.80 |
| Fair Under 3.5 odds | 2.26 |
| Fair Over 4.5 odds | 2.80 |
| Fair Under 4.5 odds | 1.55 |
| Unadjusted home-win probability | 38.7% |
| Unadjusted draw probability | 21.1% |
| Unadjusted away-win probability | 40.1% |
| Raw p over 1 5 | 90.6% |
| Raw p under 3 5 | 44.3% |
| Raw p btts yes | 74.4% |
| P home draw | 63.1% |
| P draw away | 60.5% |
| Raw p home draw | 59.9% |
| Raw p draw away | 61.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.40 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.85 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | -0.7% |
| Draw probability edge | -2.5% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | +19.1% |
| Under 2.5 probability edge | -19.1% |
| Raw edge prob home | -0.0146 |
| Raw ev home | -0.0433 |
| Raw edge prob draw | -0.0507 |
| Raw ev draw | -0.2140 |
| Raw edge prob away | 0.0653 |
| Raw ev away | 0.1760 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **45.1%**. Expected goals are 1.33 for Valencia and 1.62 for Villarreal (2.95 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.4%; Under 3.5 goals: 65.8%; Double Chance 1X: 54.9%; Double Chance X2: 70.3%; Under 4.5 goals: 82.4%; BTTS Yes (both teams score): 59.3%; BTTS No (at least one team does not score): 40.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.7% | 3.37 |
| Draw | 25.2% | 3.97 |
| Villarreal win | 45.1% | 2.22 |

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
| 1 | 1-1 | 11.74% |
| 2 | 1-2 | 9.33% |
| 3 | 0-1 | 8.43% |
| 4 | 2-1 | 7.14% |
| 5 | 0-2 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.7% | 28.3% | 3.45 | +2.5% |
| Draw | 25.2% | 25.7% | 3.78 | -4.7% |
| Villarreal win | 45.1% | 45.9% | 2.17 | -2.2% |
| Over 2.5 | 56.4% | 55.6% | 1.78 | +0.4% |
| Under 2.5 | 43.6% | 44.4% | 2.20 | -4.1% |

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
| Market best home last update utc | 2026-10-14T19:06:34Z |
| Market best draw last update utc | 2026-10-14T19:06:34Z |
| Market best away last update utc | 2026-10-14T19:06:34Z |
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
| Fair Under 0.5 odds | 17.94 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.90 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.68 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 24.7% |
| Unadjusted away-win probability | 44.2% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 59.2% |
| P home draw | 54.9% |
| P draw away | 70.3% |
| Raw p home draw | 55.8% |
| Raw p draw away | 68.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.36 |
| Reference draw odds | 3.68 |
| Reference away odds | 2.11 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.13 |
| Home probability edge | +1.4% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | 0.0279 |
| Raw ev home | 0.0727 |
| Raw edge prob draw | -0.0106 |
| Raw ev draw | -0.0669 |
| Raw edge prob away | -0.0173 |
| Raw ev away | -0.0404 |

</details>


---
