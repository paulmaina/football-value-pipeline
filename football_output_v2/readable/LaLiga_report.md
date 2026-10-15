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
| Training data health | {'training_end': '2026-10-12', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
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

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.0%**. Expected goals are 2.04 for Deportivo La Coruña and 1.32 for Levante (3.36 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.0%; Double Chance 1X: 74.5%; Double Chance X2: 50.0%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.0% | 2.00 |
| Draw | 24.5% | 4.08 |
| Levante win | 25.5% | 3.91 |

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
| 1 | 1-1 | 10.75% |
| 2 | 2-1 | 8.84% |
| 3 | 2-2 | 7.10% |
| 4 | 2-0 | 6.69% |
| 5 | 1-2 | 6.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.0% | 46.0% | 2.17 | +8.4% |
| Draw | 24.5% | 27.3% | 3.62 | -11.3% |
| Levante win | 25.5% | 26.7% | 3.60 | -8.0% |
| Over 2.5 | 64.3% | 48.8% | 1.98 | +27.3% |
| Under 2.5 | 35.7% | 51.2% | 1.96 | -30.0% |

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
| Market best home last update utc | 2026-10-15T06:53:33Z |
| Market best draw last update utc | 2026-10-15T06:53:33Z |
| Market best away last update utc | 2026-10-15T06:53:33Z |
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
| Fair Under 0.5 odds | 24.27 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.62 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.12 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 53.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 64.0% |
| P home draw | 74.5% |
| P draw away | 50.0% |
| P home away | 75.5% |
| Raw p home draw | 75.6% |
| Raw p draw away | 46.1% |
| Raw p home away | 78.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.12 |
| Reference draw odds | 3.52 |
| Reference away odds | 3.59 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.90 |
| Home probability edge | +3.9% |
| Draw probability edge | -2.8% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +15.5% |
| Under 2.5 probability edge | -15.5% |
| Raw edge prob home | 0.0786 |
| Raw ev home | 0.1693 |
| Raw edge prob draw | -0.0553 |
| Raw ev draw | -0.2133 |
| Raw edge prob away | -0.0233 |
| Raw ev away | -0.1223 |
| Market p home draw | 72.9% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:33Z |
| Market reference home draw last update utc | 2026-10-15T06:53:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.8% |
| Market draw away odds | 1.77 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:33Z |
| Market reference draw away last update utc | 2026-10-15T06:53:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.3% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:33Z |
| Market reference home away last update utc | 2026-10-15T06:53:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.30 |
| Market reference dc draw away odds | 1.70 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 75.3% |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 73.1% |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.41 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 53.7% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:33Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **52.9%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 0-1 at 12.0%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 48.8%; Under 3.5 goals: 73.2%; Double Chance 1X: 47.1%; Double Chance X2: 77.8%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 22.2% | 4.51 |
| Draw | 24.9% | 4.01 |
| Atlético Madrid win | 52.9% | 1.89 |

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
| Over 2.5 | 48.8% |
| Under 2.5 | 51.2% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.03% |
| 2 | 1-1 | 11.86% |
| 3 | 1-2 | 9.98% |
| 4 | 0-2 | 9.74% |
| 5 | 0-0 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 22.2% | 20.1% | 4.88 | +8.3% |
| Draw | 24.9% | 24.3% | 3.94 | -1.8% |
| Atlético Madrid win | 52.9% | 55.6% | 1.80 | -4.8% |
| Over 2.5 | 48.8% | 52.7% | 1.87 | -8.8% |
| Under 2.5 | 51.2% | 47.3% | 2.08 | +6.5% |

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
| Market best home last update utc | 2026-10-15T06:53:33Z |
| Market best draw last update utc | 2026-10-15T06:53:33Z |
| Market best away last update utc | 2026-10-15T06:53:33Z |
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
| Fair Under 0.5 odds | 13.54 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.96 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.2% |
| P home draw | 47.1% |
| P draw away | 77.8% |
| P home away | 75.1% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.68 |
| Reference draw odds | 3.91 |
| Reference away odds | 1.76 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | +2.1% |
| Draw probability edge | +0.7% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | 0.0411 |
| Raw ev home | 0.1834 |
| Raw edge prob draw | 0.0132 |
| Raw ev draw | 0.0080 |
| Raw edge prob away | -0.0543 |
| Raw ev away | -0.0970 |
| Market p home draw | 46.0% |
| Market home draw odds | 2.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:33Z |
| Market reference home draw last update utc | 2026-10-15T06:53:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 78.6% |
| Market draw away odds | 1.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:33Z |
| Market reference draw away last update utc | 2026-10-15T06:53:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:33Z |
| Market reference home away last update utc | 2026-10-15T06:53:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.05 |
| Market reference dc draw away odds | 1.20 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 77.8% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 70.3% |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.11 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 54.7% |
| Market btts yes odds | 1.73 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:33Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.05 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **61.6%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 67.6%; Under 3.5 goals: 54.7%; Double Chance 1X: 38.4%; Double Chance X2: 80.4%; Double Chance 12 (either team wins): 81.2%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.6% | 5.10 |
| Draw | 18.8% | 5.31 |
| Barcelona win | 61.6% | 1.62 |

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
| Over 2.5 | 67.6% |
| Under 2.5 | 32.4% |
| Over 3.5 | 45.3% |
| Under 3.5 | 54.7% |
| Over 4.5 | 26.8% |
| Under 4.5 | 73.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.81% |
| 2 | 1-1 | 8.15% |
| 3 | 0-2 | 8.00% |
| 4 | 0-1 | 7.52% |
| 5 | 1-3 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.6% | 14.6% | 6.32 | +23.8% |
| Draw | 18.8% | 16.1% | 5.65 | +6.4% |
| Barcelona win | 61.6% | 69.3% | 1.47 | -9.5% |

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
| Market best home last update utc | 2026-10-15T06:53:33Z |
| Market best draw last update utc | 2026-10-15T06:53:33Z |
| Market best away last update utc | 2026-10-15T06:53:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.0% |
| P btts no | 36.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.18 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.20 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.08 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.73 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 24.6% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 55.3% |
| Raw p btts yes | 65.0% |
| P home draw | 38.4% |
| P draw away | 80.4% |
| P home away | 81.2% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Raw p home away | 78.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.29 |
| Reference draw odds | 5.71 |
| Reference away odds | 1.42 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.24 |
| Reference Under 2.5 odds | 3.95 |
| Home probability edge | +5.0% |
| Draw probability edge | +2.7% |
| Away probability edge | -7.7% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | 0.1001 |
| Raw ev home | 0.5546 |
| Raw edge prob draw | 0.0539 |
| Raw ev draw | 0.2163 |
| Raw edge prob away | -0.1540 |
| Raw ev away | -0.2080 |
| Market p home draw | 34.4% |
| Market home draw odds | 2.90 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:33Z |
| Market reference home draw last update utc | 2026-10-15T06:53:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.6% |
| Market draw away odds | 1.14 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:33Z |
| Market reference draw away last update utc | 2026-10-15T06:53:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.0% |
| Market home away odds | 1.18 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:33Z |
| Market reference home away last update utc | 2026-10-15T06:53:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.75 |
| Market reference dc draw away odds | 1.12 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 92.4% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 9.00 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 42.6% |
| Market reference under 3 5 odds | 2.24 |
| Market reference under 3 5 opposite odds | 1.69 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:33Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.90 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **40.5%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.1%; Double Chance 1X: 59.5%; Double Chance X2: 69.3%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 92.3%; BTTS Yes (both teams score): 45.5%; BTTS No (at least one team does not score): 54.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.7% | 3.26 |
| Draw | 28.8% | 3.47 |
| Athletic Bilbao win | 40.5% | 2.47 |

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
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.38% |
| 2 | 0-1 | 13.06% |
| 3 | 0-0 | 10.73% |
| 4 | 1-0 | 10.36% |
| 5 | 1-2 | 8.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.7% | 28.3% | 3.47 | +6.5% |
| Draw | 28.8% | 28.4% | 3.51 | +1.2% |
| Athletic Bilbao win | 40.5% | 43.3% | 2.26 | -8.5% |
| Over 2.5 | 39.0% | 45.6% | 2.10 | -18.1% |
| Under 2.5 | 61.0% | 54.4% | 1.86 | +13.5% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
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
| P btts yes | 45.5% |
| P btts no | 54.5% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.32 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.29 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.92 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 45.6% |
| P home draw | 59.5% |
| P draw away | 69.3% |
| P home away | 71.2% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.40 |
| Reference draw odds | 3.39 |
| Reference away odds | 2.25 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +2.4% |
| Draw probability edge | +0.5% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | 0.0477 |
| Raw ev home | 0.1475 |
| Raw edge prob draw | 0.0092 |
| Raw ev draw | 0.0287 |
| Raw edge prob away | -0.0570 |
| Raw ev away | -0.1497 |
| Market p home draw | 56.0% |
| Market home draw odds | 1.72 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:34Z |
| Market reference home draw last update utc | 2026-10-15T06:53:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.0% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:34Z |
| Market reference draw away last update utc | 2026-10-15T06:53:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.0% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:34Z |
| Market reference home away last update utc | 2026-10-15T06:53:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.67 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 72.9% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:33Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.25 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.9% |
| Market under 3 5 odds | 1.25 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:33Z |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.73 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.2% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:34Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 1.95 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **66.1%**. Expected goals are 2.41 for Villarreal and 1.19 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 69.9%; Under 3.5 goals: 51.3%; Double Chance 1X: 84.5%; Double Chance X2: 33.9%; Double Chance 12 (either team wins): 81.6%; Under 4.5 goals: 70.5%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 66.1% | 1.51 |
| Draw | 18.4% | 5.42 |
| Elche CF win | 15.5% | 6.46 |

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
| Over 2.5 | 69.9% |
| Under 2.5 | 30.1% |
| Over 3.5 | 48.7% |
| Under 3.5 | 51.3% |
| Over 4.5 | 29.5% |
| Under 4.5 | 70.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.70% |
| 2 | 2-0 | 8.18% |
| 3 | 1-1 | 7.91% |
| 4 | 3-1 | 7.81% |
| 5 | 1-0 | 6.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 66.1% | 67.8% | 1.51 | -0.2% |
| Draw | 18.4% | 18.3% | 4.88 | -10.0% |
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
| Market best home last update utc | 2026-10-15T06:53:33Z |
| Market best draw last update utc | 2026-10-15T06:53:33Z |
| Market best away last update utc | 2026-10-15T06:53:33Z |
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
| Fair Under 0.5 odds | 34.90 |
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
| P home draw | 84.5% |
| P draw away | 33.9% |
| P home away | 81.6% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.7% |
| Raw p home away | 81.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.45 |
| Reference draw odds | 5.08 |
| Reference away odds | 6.61 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.68 |
| Home probability edge | -1.7% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | +3.8% |
| Under 2.5 probability edge | -3.8% |
| Raw edge prob home | -0.0347 |
| Raw ev home | -0.0284 |
| Raw edge prob draw | 0.0031 |
| Raw ev draw | -0.0924 |
| Raw edge prob away | 0.0317 |
| Raw ev away | 0.1480 |
| Market p home draw | 84.7% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:53:33Z |
| Market reference home draw last update utc | 2026-10-15T06:53:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.2% |
| Market draw away odds | 2.75 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:53:33Z |
| Market reference draw away last update utc | 2026-10-15T06:53:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.1% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:53:33Z |
| Market reference home away last update utc | 2026-10-15T06:53:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.12 |
| Market reference dc draw away odds | 2.62 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 87.5% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.3% |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.23 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:53:33Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **55.6%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.33 combined). The most likely exact score is 2-2 at 7.8%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.1%; Under 3.5 goals: 38.0%; Double Chance 1X: 77.5%; Double Chance X2: 44.4%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 58.1%; BTTS Yes (both teams score): 75.2%; BTTS No (at least one team does not score): 24.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 55.6% | 1.80 |
| Draw | 21.9% | 4.57 |
| Real Racing Club de Santander win | 22.5% | 4.44 |

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
| Over 2.5 | 79.1% |
| Under 2.5 | 20.9% |
| Over 3.5 | 62.0% |
| Under 3.5 | 38.0% |
| Over 4.5 | 41.9% |
| Under 4.5 | 58.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.78% |
| 2 | 1-1 | 7.38% |
| 3 | 2-1 | 6.94% |
| 4 | 3-1 | 6.43% |
| 5 | 1-2 | 5.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 55.6% | 47.9% | 2.04 | +13.4% |
| Draw | 21.9% | 26.6% | 3.72 | -18.5% |
| Real Racing Club de Santander win | 22.5% | 25.5% | 3.88 | -12.6% |
| Over 2.5 | 79.1% | 56.8% | 1.74 | +37.7% |
| Under 2.5 | 20.9% | 43.2% | 2.27 | -52.6% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
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
| Fair Under 0.5 odds | 54.69 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.91 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.79 |
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
| P home draw | 77.5% |
| P draw away | 44.4% |
| P home away | 78.1% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Raw p home away | 82.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.04 |
| Reference draw odds | 3.61 |
| Reference away odds | 3.76 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | +7.7% |
| Draw probability edge | -4.7% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | +22.4% |
| Under 2.5 probability edge | -22.4% |
| Raw edge prob home | 0.1535 |
| Raw ev home | 0.2905 |
| Raw edge prob draw | -0.0938 |
| Raw ev draw | -0.3599 |
| Raw edge prob away | -0.0596 |
| Raw ev away | -0.2422 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **47.2%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 43.4%; Under 3.5 goals: 77.3%; Double Chance 1X: 75.3%; Double Chance X2: 52.8%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 47.2% | 2.12 |
| Draw | 28.1% | 3.56 |
| Alavés win | 24.7% | 4.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.49 |
| Alavés expected goals | 0.94 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 43.4% |
| Under 2.5 | 56.6% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.23% |
| 2 | 1-0 | 12.18% |
| 3 | 0-0 | 9.48% |
| 4 | 2-0 | 9.26% |
| 5 | 2-1 | 8.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 47.2% | 44.8% | 2.16 | +2.0% |
| Draw | 28.1% | 29.5% | 3.48 | -2.4% |
| Alavés win | 24.7% | 25.8% | 3.78 | -6.6% |
| Over 2.5 | 43.4% | 42.6% | 2.30 | -0.2% |
| Under 2.5 | 56.6% | 57.4% | 1.72 | -2.6% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
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
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.55 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.30 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.41 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.15 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 47.6% |
| P home draw | 75.3% |
| P draw away | 52.8% |
| P home away | 71.9% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.18 |
| Reference draw odds | 3.27 |
| Reference away odds | 3.72 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.30 |
| Reference Under 2.5 odds | 1.72 |
| Home probability edge | +2.5% |
| Draw probability edge | -1.4% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | 0.0495 |
| Raw ev home | 0.0737 |
| Raw edge prob draw | -0.0280 |
| Raw ev draw | -0.0724 |
| Raw edge prob away | -0.0215 |
| Raw ev away | -0.1065 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.1%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.6%. Goal-market probabilities: at least one goal: 85.4%; Over 2.5 goals: 29.5%; Under 3.5 goals: 87.9%; Double Chance 1X: 51.9%; Double Chance X2: 76.7%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.4%; BTTS No (at least one team does not score): 66.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.3% | 4.29 |
| Draw | 28.6% | 3.50 |
| Real Sociedad win | 48.1% | 2.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.4% |
| Under 0.5 | 14.6% |
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
| 1 | 0-1 | 17.56% |
| 2 | 0-0 | 14.56% |
| 3 | 1-0 | 11.83% |
| 4 | 1-1 | 11.56% |
| 5 | 0-2 | 11.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.3% | 28.5% | 3.29 | -23.2% |
| Draw | 28.6% | 27.0% | 3.63 | +3.7% |
| Real Sociedad win | 48.1% | 44.5% | 2.29 | +10.2% |
| Over 2.5 | 29.5% | 53.1% | 1.86 | -45.2% |
| Under 2.5 | 70.5% | 46.9% | 2.10 | +48.1% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
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
| Fair Under 0.5 odds | 6.87 |
| Fair Over 1.5 odds | 1.78 |
| Fair Under 1.5 odds | 2.28 |
| Fair Over 2.5 odds | 3.39 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.26 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.28 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 51.9% |
| P draw away | 76.7% |
| P home away | 71.4% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Raw p home away | 69.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.38 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.19 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -5.1% |
| Draw probability edge | +1.6% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -23.6% |
| Under 2.5 probability edge | +23.6% |
| Raw edge prob home | -0.1027 |
| Raw ev home | -0.4013 |
| Raw edge prob draw | 0.0315 |
| Raw ev draw | 0.0939 |
| Raw edge prob away | 0.0712 |
| Raw ev away | 0.1832 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **77.5%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.5%; Under 3.5 goals: 56.5%; Double Chance 1X: 91.7%; Double Chance X2: 22.5%; Double Chance 12 (either team wins): 85.8%; Under 4.5 goals: 75.0%; BTTS Yes (both teams score): 48.7%; BTTS No (at least one team does not score): 51.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.5% | 1.29 |
| Draw | 14.2% | 7.03 |
| Sevilla win | 8.3% | 12.10 |

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
| Over 3.5 | 43.5% |
| Under 3.5 | 56.5% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.90% |
| 2 | 3-0 | 10.41% |
| 3 | 1-0 | 8.93% |
| 4 | 2-1 | 8.82% |
| 5 | 3-1 | 7.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.5% | 77.6% | 1.29 | -0.0% |
| Draw | 14.2% | 13.9% | 6.71 | -4.5% |
| Sevilla win | 8.3% | 8.5% | 11.20 | -7.5% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
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
| Fair Under 0.5 odds | 28.46 |
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
| P home draw | 91.7% |
| P draw away | 22.5% |
| P home away | 85.8% |
| Raw p home draw | 91.9% |
| Raw p draw away | 22.6% |
| Raw p home away | 85.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.27 |
| Reference draw odds | 6.39 |
| Reference away odds | 10.22 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.85 |
| Home probability edge | -0.1% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | -0.0014 |
| Raw ev home | -0.0009 |
| Raw edge prob draw | 0.0055 |
| Raw ev draw | -0.0269 |
| Raw edge prob away | -0.0042 |
| Raw ev away | -0.0982 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.0%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.9%. Goal-market probabilities: at least one goal: 81.1%; Over 2.5 goals: 23.0%; Under 3.5 goals: 91.5%; Double Chance 1X: 68.8%; Double Chance X2: 65.0%; Double Chance 12 (either team wins): 66.2%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 31.1%; BTTS No (at least one team does not score): 68.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.0% | 2.86 |
| Draw | 33.8% | 2.96 |
| Rayo Vallecano win | 31.2% | 3.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.1% |
| Under 0.5 | 18.9% |
| Over 1.5 | 49.1% |
| Under 1.5 | 50.9% |
| Over 2.5 | 23.0% |
| Under 2.5 | 77.0% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.90% |
| 2 | 1-0 | 16.22% |
| 3 | 0-1 | 15.78% |
| 4 | 1-1 | 12.70% |
| 5 | 2-0 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.0% | 32.7% | 2.99 | +4.6% |
| Draw | 33.8% | 32.6% | 3.16 | +6.9% |
| Rayo Vallecano win | 31.2% | 34.7% | 2.74 | -14.6% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 31.1% |
| P btts no | 68.9% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.29 |
| Fair Over 1.5 odds | 2.04 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.34 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.80 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.87 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.1% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.3% |
| P home draw | 68.8% |
| P draw away | 65.0% |
| P home away | 66.2% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.7% |
| Raw p home away | 64.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.96 |
| Reference draw odds | 2.97 |
| Reference away odds | 2.79 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.50 |
| Reference Under 2.5 odds | 1.53 |
| Home probability edge | +2.3% |
| Draw probability edge | +1.3% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -13.9% |
| Under 2.5 probability edge | +13.9% |
| Raw edge prob home | 0.0460 |
| Raw ev home | 0.1149 |
| Raw edge prob draw | 0.0251 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0712 |
| Raw ev away | -0.2431 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.8%**. Expected goals are 1.29 for Levante and 1.39 for Athletic Bilbao (2.68 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 49.5%; Under 3.5 goals: 71.8%; Double Chance 1X: 58.2%; Double Chance X2: 70.3%; Double Chance 12 (either team wins): 71.5%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 29.7% | 3.37 |
| Draw | 28.5% | 3.51 |
| Athletic Bilbao win | 41.8% | 2.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.29 |
| Athletic Bilbao expected goals | 1.39 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.55% |
| 2 | 0-1 | 9.90% |
| 3 | 1-2 | 9.12% |
| 4 | 0-0 | 7.66% |
| 5 | 1-0 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 29.7% | 24.9% | 3.52 | +4.5% |
| Draw | 28.5% | 30.7% | 3.52 | +0.4% |
| Athletic Bilbao win | 41.8% | 44.4% | 2.24 | -6.4% |
| Over 2.5 | 49.5% | 49.0% | 2.02 | +0.0% |
| Under 2.5 | 50.5% | 51.0% | 1.92 | -3.1% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
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
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.05 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.57 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 54.7% |
| P home draw | 58.2% |
| P draw away | 70.3% |
| P home away | 71.5% |
| Raw p home draw | 60.8% |
| Raw p draw away | 65.5% |
| Raw p home away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.77 |
| Reference draw odds | 3.09 |
| Reference away odds | 2.17 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +4.8% |
| Draw probability edge | -2.2% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0957 |
| Raw ev home | 0.2136 |
| Raw edge prob draw | -0.0431 |
| Raw ev draw | -0.0719 |
| Raw edge prob away | -0.0526 |
| Raw ev away | -0.1229 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **56.4%**. Expected goals are 1.38 for Alavés and 0.44 for Málaga (1.82 combined). The most likely exact score is 1-0 at 20.7%. Goal-market probabilities: at least one goal: 83.9%; Over 2.5 goals: 27.0%; Under 3.5 goals: 89.3%; Double Chance 1X: 83.7%; Double Chance X2: 43.6%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 96.4%; BTTS Yes (both teams score): 26.7%; BTTS No (at least one team does not score): 73.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 56.4% | 1.77 |
| Draw | 27.4% | 3.65 |
| Málaga win | 16.3% | 6.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.38 |
| Málaga expected goals | 0.44 |
| Expected total goals | 1.82 |
| Over 0.5 | 83.9% |
| Under 0.5 | 16.1% |
| Over 1.5 | 53.4% |
| Under 1.5 | 46.6% |
| Over 2.5 | 27.0% |
| Under 2.5 | 73.0% |
| Over 3.5 | 10.7% |
| Under 3.5 | 89.3% |
| Over 4.5 | 3.6% |
| Under 4.5 | 96.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.72% |
| 2 | 0-0 | 16.07% |
| 3 | 2-0 | 14.41% |
| 4 | 0-1 | 9.80% |
| 5 | 1-1 | 9.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 56.4% | 52.3% | 1.89 | +6.5% |
| Draw | 27.4% | 26.7% | 3.73 | +2.1% |
| Málaga win | 16.3% | 21.0% | 4.57 | -25.7% |
| Over 2.5 | 27.0% | 47.5% | 2.07 | -44.0% |
| Under 2.5 | 73.0% | 52.5% | 1.88 | +37.2% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
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
| Fair Under 0.5 odds | 6.22 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.70 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.30 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 27.41 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 54.4% |
| Raw p under 3 5 | 88.9% |
| Raw p btts yes | 26.7% |
| P home draw | 83.7% |
| P draw away | 43.6% |
| P home away | 72.6% |
| Raw p home draw | 88.5% |
| Raw p draw away | 39.5% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.85 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.39 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.07 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +4.1% |
| Draw probability edge | +0.7% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -20.5% |
| Under 2.5 probability edge | +20.5% |
| Raw edge prob home | 0.0817 |
| Raw ev home | 0.1426 |
| Raw edge prob draw | 0.0136 |
| Raw ev draw | 0.0465 |
| Raw edge prob away | -0.0953 |
| Raw ev away | -0.4749 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **73.6%**. Expected goals are 2.31 for Atlético Madrid and 0.98 for Deportivo La Coruña (3.29 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 65.3%; Under 3.5 goals: 57.2%; Double Chance 1X: 89.7%; Double Chance X2: 26.4%; Double Chance 12 (either team wins): 83.8%; Under 4.5 goals: 75.5%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 73.6% | 1.36 |
| Draw | 16.2% | 6.19 |
| Deportivo La Coruña win | 10.3% | 9.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.31 |
| Deportivo La Coruña expected goals | 0.98 |
| Expected total goals | 3.29 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
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
| 1 | 2-0 | 10.90% |
| 2 | 2-1 | 10.70% |
| 3 | 1-0 | 9.25% |
| 4 | 3-0 | 8.40% |
| 5 | 3-1 | 8.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 73.6% | 80.1% | 1.24 | -8.8% |
| Draw | 16.2% | 13.7% | 6.92 | +11.8% |
| Deportivo La Coruña win | 10.3% | 6.2% | 14.90 | +53.3% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
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
| Fair Under 0.5 odds | 29.71 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.62 |
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
| P home draw | 89.7% |
| P draw away | 26.4% |
| P home away | 83.8% |
| Raw p home draw | 85.6% |
| Raw p draw away | 33.0% |
| Raw p home away | 81.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.24 |
| Reference draw odds | 6.92 |
| Reference away odds | 14.90 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.48 |
| Home probability edge | -6.6% |
| Draw probability edge | +2.5% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | +1.9% |
| Under 2.5 probability edge | -1.9% |
| Raw edge prob home | -0.1317 |
| Raw ev home | -0.1696 |
| Raw edge prob draw | 0.0500 |
| Raw ev draw | 0.2910 |
| Raw edge prob away | 0.0817 |
| Raw ev away | 1.1422 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **49.6%**. Expected goals are 1.39 for Rayo Vallecano and 1.06 for Elche CF (2.46 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.4%; Double Chance 1X: 75.5%; Double Chance X2: 50.4%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 49.0%; BTTS No (at least one team does not score): 51.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 49.6% | 2.01 |
| Draw | 25.8% | 3.87 |
| Elche CF win | 24.5% | 4.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.39 |
| Elche CF expected goals | 1.06 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 70.9% |
| Under 1.5 | 29.1% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.11% |
| 2 | 1-1 | 12.24% |
| 3 | 2-1 | 9.93% |
| 4 | 2-0 | 9.34% |
| 5 | 0-0 | 8.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 49.6% | 55.0% | 1.81 | -10.2% |
| Draw | 25.8% | 24.3% | 3.94 | +1.8% |
| Elche CF win | 24.5% | 20.6% | 4.78 | +17.3% |
| Over 2.5 | 45.2% | 52.5% | 1.88 | -15.1% |
| Under 2.5 | 54.8% | 47.5% | 2.07 | +13.5% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
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
| P btts yes | 49.0% |
| P btts no | 51.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.00 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.44 |
| Fair Over 2.5 odds | 2.21 |
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
| P home draw | 75.5% |
| P draw away | 50.4% |
| P home away | 74.2% |
| Raw p home draw | 71.5% |
| Raw p draw away | 55.8% |
| Raw p home away | 72.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.76 |
| Reference draw odds | 3.81 |
| Reference away odds | 4.46 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.01 |
| Home probability edge | -5.4% |
| Draw probability edge | +1.5% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.1082 |
| Raw ev home | -0.1995 |
| Raw edge prob draw | 0.0298 |
| Raw ev draw | 0.0766 |
| Raw edge prob away | 0.0784 |
| Raw ev away | 0.3599 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **39.5%**. Expected goals are 1.96 for Real Racing Club de Santander and 1.99 for Espanyol (3.95 combined). The most likely exact score is 1-1 at 8.5%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 74.8%; Under 3.5 goals: 44.3%; Double Chance 1X: 63.1%; Double Chance X2: 60.5%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 64.3%; BTTS Yes (both teams score): 74.9%; BTTS No (at least one team does not score): 25.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 39.5% | 2.53 |
| Draw | 23.5% | 4.25 |
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
| 1 | 1-1 | 8.52% |
| 2 | 2-2 | 8.16% |
| 3 | 2-1 | 7.49% |
| 4 | 1-2 | 6.88% |
| 5 | 3-1 | 4.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 39.5% | 40.3% | 2.47 | -2.4% |
| Draw | 23.5% | 26.0% | 3.72 | -12.4% |
| Espanyol win | 36.9% | 33.7% | 2.93 | +8.2% |
| Over 2.5 | 74.8% | 55.5% | 1.78 | +33.2% |
| Under 2.5 | 25.2% | 44.5% | 2.21 | -44.4% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
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
| Fair Under 0.5 odds | 43.39 |
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
| P home away | 76.5% |
| Raw p home draw | 59.9% |
| Raw p draw away | 61.3% |
| Raw p home away | 78.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.38 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.82 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.21 |
| Home probability edge | -0.8% |
| Draw probability edge | -2.4% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | +19.3% |
| Under 2.5 probability edge | -19.3% |
| Raw edge prob home | -0.0157 |
| Raw ev home | -0.0433 |
| Raw edge prob draw | -0.0484 |
| Raw ev draw | -0.2140 |
| Raw edge prob away | 0.0640 |
| Raw ev away | 0.1760 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **44.5%**. Expected goals are 1.33 for Valencia and 1.62 for Villarreal (2.95 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 56.6%; Under 3.5 goals: 65.8%; Double Chance 1X: 55.5%; Double Chance X2: 69.0%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 31.0% | 3.23 |
| Draw | 24.5% | 4.08 |
| Villarreal win | 44.5% | 2.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.33 |
| Villarreal expected goals | 1.62 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
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
| 1 | 1-1 | 11.41% |
| 2 | 1-2 | 9.21% |
| 3 | 0-1 | 8.33% |
| 4 | 2-1 | 7.45% |
| 5 | 0-2 | 6.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 31.0% | 30.9% | 3.45 | +6.9% |
| Draw | 24.5% | 24.3% | 3.78 | -7.4% |
| Villarreal win | 44.5% | 44.8% | 2.17 | -3.4% |
| Over 2.5 | 56.6% | 55.4% | 1.78 | +0.8% |
| Under 2.5 | 43.4% | 44.6% | 2.20 | -4.6% |

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
| Market best home last update utc | 2026-10-15T06:53:34Z |
| Market best draw last update utc | 2026-10-15T06:53:34Z |
| Market best away last update utc | 2026-10-15T06:53:34Z |
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
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.46 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.89 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 2.93 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.66 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 24.7% |
| Unadjusted away-win probability | 44.2% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 59.2% |
| P home draw | 55.5% |
| P draw away | 69.0% |
| P home away | 75.5% |
| Raw p home draw | 55.8% |
| Raw p draw away | 68.9% |
| Raw p home away | 75.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.07 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +0.1% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | 0.0024 |
| Raw ev home | 0.0727 |
| Raw edge prob draw | 0.0035 |
| Raw ev draw | -0.0669 |
| Raw edge prob away | -0.0060 |
| Raw ev away | -0.0404 |

</details>


---
