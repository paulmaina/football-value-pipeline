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
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.0%**. Expected goals are 2.04 for Deportivo La Coruña and 1.32 for Levante (3.36 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.0%; Double Chance 1X: 74.3%; Double Chance X2: 50.0%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.0% | 2.00 |
| Draw | 24.3% | 4.12 |
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
| 1 | 1-1 | 10.66% |
| 2 | 2-1 | 8.85% |
| 3 | 2-2 | 7.04% |
| 4 | 2-0 | 6.70% |
| 5 | 1-2 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.0% | 46.1% | 2.17 | +8.4% |
| Draw | 24.3% | 26.8% | 3.60 | -12.6% |
| Levante win | 25.7% | 27.1% | 3.62 | -6.8% |
| Over 2.5 | 64.3% | 48.0% | 1.98 | +27.4% |
| Under 2.5 | 35.7% | 52.0% | 1.96 | -30.1% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| Fair Under 0.5 odds | 24.48 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.62 |
| Fair Over 2.5 odds | 1.55 |
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
| P home draw | 74.3% |
| P draw away | 50.0% |
| P home away | 75.7% |
| Raw p home draw | 75.6% |
| Raw p draw away | 46.1% |
| Raw p home away | 78.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.38 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.87 |
| Home probability edge | +3.9% |
| Draw probability edge | -2.6% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | +16.4% |
| Under 2.5 probability edge | -16.4% |
| Raw edge prob home | 0.0783 |
| Raw ev home | 0.1693 |
| Raw edge prob draw | -0.0511 |
| Raw ev draw | -0.2177 |
| Raw edge prob away | -0.0272 |
| Raw ev away | -0.1174 |
| Market p home draw | 72.0% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:50:24Z |
| Market reference home draw last update utc | 2026-10-15T09:50:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.5% |
| Market draw away odds | 1.77 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:50:24Z |
| Market reference draw away last update utc | 2026-10-15T09:50:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.5% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:50:24Z |
| Market reference home away last update utc | 2026-10-15T09:50:39Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.32 |
| Market reference dc draw away odds | 1.71 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 74.2% |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.53 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 74.1% |
| Market reference under 3 5 odds | 1.32 |
| Market reference under 3 5 opposite odds | 3.50 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 54.7% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:50:24Z |
| Market reference btts yes odds | 1.81 |
| Market reference btts yes opposite odds | 2.18 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **53.8%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 0-1 at 12.2%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 49.0%; Under 3.5 goals: 73.1%; Double Chance 1X: 46.2%; Double Chance X2: 78.2%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 21.8% | 4.58 |
| Draw | 24.4% | 4.10 |
| Atlético Madrid win | 53.8% | 1.86 |

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
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.24% |
| 2 | 1-1 | 11.60% |
| 3 | 1-2 | 10.16% |
| 4 | 0-2 | 9.91% |
| 5 | 0-0 | 7.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 21.8% | 19.4% | 4.88 | +6.5% |
| Draw | 24.4% | 23.2% | 3.94 | -4.0% |
| Atlético Madrid win | 53.8% | 57.4% | 1.80 | -3.1% |
| Over 2.5 | 49.0% | 53.3% | 1.87 | -8.4% |
| Under 2.5 | 51.0% | 46.7% | 2.08 | +6.1% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.85 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.91 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.2% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 50.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.2% |
| P home draw | 46.2% |
| P draw away | 78.2% |
| P home away | 75.6% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 4.40 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.65 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.04 |
| Home probability edge | +2.4% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | 0.0485 |
| Raw ev home | 0.1834 |
| Raw edge prob draw | 0.0243 |
| Raw ev draw | 0.0080 |
| Raw edge prob away | -0.0728 |
| Raw ev away | -0.0970 |
| Market p home draw | 45.1% |
| Market home draw odds | 2.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:50:24Z |
| Market reference home draw last update utc | 2026-10-15T09:50:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 79.7% |
| Market draw away odds | 1.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:50:24Z |
| Market reference draw away last update utc | 2026-10-15T09:50:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.3% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:50:24Z |
| Market reference home away last update utc | 2026-10-15T09:50:39Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.12 |
| Market reference dc draw away odds | 1.20 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 78.2% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 3.60 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 70.3% |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.11 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 54.0% |
| Market btts yes odds | 1.73 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:50:24Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.08 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **62.0%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 67.7%; Under 3.5 goals: 54.7%; Double Chance 1X: 38.0%; Double Chance X2: 80.5%; Double Chance 12 (either team wins): 81.5%; Under 4.5 goals: 73.1%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.5% | 5.13 |
| Draw | 18.5% | 5.41 |
| Barcelona win | 62.0% | 1.61 |

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
| Over 2.5 | 67.7% |
| Under 2.5 | 32.3% |
| Over 3.5 | 45.3% |
| Under 3.5 | 54.7% |
| Over 4.5 | 26.9% |
| Under 4.5 | 73.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.89% |
| 2 | 0-2 | 8.06% |
| 3 | 1-1 | 8.00% |
| 4 | 0-1 | 7.57% |
| 5 | 1-3 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.5% | 14.4% | 6.32 | +23.2% |
| Draw | 18.5% | 15.5% | 5.65 | +4.5% |
| Barcelona win | 62.0% | 70.2% | 1.47 | -8.8% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| Fair Under 0.5 odds | 33.79 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.21 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.10 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.72 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 24.6% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 55.3% |
| Raw p btts yes | 65.0% |
| P home draw | 38.0% |
| P draw away | 80.5% |
| P home away | 81.5% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Raw p home away | 78.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 5.60 |
| Reference draw odds | 5.25 |
| Reference away odds | 1.37 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.02 |
| Home probability edge | +5.1% |
| Draw probability edge | +3.0% |
| Away probability edge | -8.1% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | 0.1022 |
| Raw ev home | 0.5546 |
| Raw edge prob draw | 0.0607 |
| Raw ev draw | 0.2163 |
| Raw edge prob away | -0.1629 |
| Raw ev away | -0.2080 |
| Market p home draw | 33.0% |
| Market home draw odds | 2.90 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:50:24Z |
| Market reference home draw last update utc | 2026-10-15T09:50:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.9% |
| Market draw away odds | 1.14 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:50:24Z |
| Market reference draw away last update utc | 2026-10-15T09:50:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.1% |
| Market home away odds | 1.18 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:50:24Z |
| Market reference home away last update utc | 2026-10-15T09:50:39Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.90 |
| Market reference dc draw away odds | 1.14 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 92.4% |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 6.80 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 42.6% |
| Market reference under 3 5 odds | 2.24 |
| Market reference under 3 5 opposite odds | 1.69 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 68.8% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:50:24Z |
| Market reference btts yes odds | 1.42 |
| Market reference btts yes opposite odds | 2.99 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **40.6%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.1%; Double Chance 1X: 59.4%; Double Chance X2: 69.4%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.6% | 3.26 |
| Draw | 28.7% | 3.48 |
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
| 1 | 1-1 | 13.32% |
| 2 | 0-1 | 13.11% |
| 3 | 0-0 | 10.69% |
| 4 | 1-0 | 10.35% |
| 5 | 1-2 | 8.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.6% | 28.2% | 3.47 | +6.3% |
| Draw | 28.7% | 28.1% | 3.51 | +0.8% |
| Athletic Bilbao win | 40.6% | 43.6% | 2.26 | -8.2% |
| Over 2.5 | 39.0% | 45.6% | 2.10 | -18.0% |
| Under 2.5 | 61.0% | 54.4% | 1.86 | +13.4% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| Fair Under 0.5 odds | 9.36 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.29 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.90 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 45.6% |
| P home draw | 59.4% |
| P draw away | 69.4% |
| P home away | 71.3% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.17 |
| Reference draw odds | 3.18 |
| Reference away odds | 2.13 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +2.4% |
| Draw probability edge | +0.6% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | 0.0484 |
| Raw ev home | 0.1475 |
| Raw edge prob draw | 0.0118 |
| Raw ev draw | 0.0287 |
| Raw edge prob away | -0.0602 |
| Raw ev away | -0.1497 |
| Market p home draw | 57.8% |
| Market home draw odds | 1.72 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:50:24Z |
| Market reference home draw last update utc | 2026-10-15T09:50:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.1% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:50:24Z |
| Market reference draw away last update utc | 2026-10-15T09:50:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.1% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:50:24Z |
| Market reference home away last update utc | 2026-10-15T09:50:39Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.65 |
| Market reference dc draw away odds | 1.34 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 72.5% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T09:50:15Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.35 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.9% |
| Market under 3 5 odds | 1.25 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T09:50:15Z |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.73 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.1% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:50:24Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 2.00 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **66.7%**. Expected goals are 2.41 for Villarreal and 1.19 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 70.0%; Under 3.5 goals: 51.2%; Double Chance 1X: 84.8%; Double Chance X2: 33.3%; Double Chance 12 (either team wins): 81.9%; Under 4.5 goals: 70.4%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 66.7% | 1.50 |
| Draw | 18.1% | 5.53 |
| Elche CF win | 15.2% | 6.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.41 |
| Elche CF expected goals | 1.19 |
| Expected total goals | 3.60 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 87.8% |
| Under 1.5 | 12.2% |
| Over 2.5 | 70.0% |
| Under 2.5 | 30.0% |
| Over 3.5 | 48.8% |
| Under 3.5 | 51.2% |
| Over 4.5 | 29.6% |
| Under 4.5 | 70.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.79% |
| 2 | 2-0 | 8.26% |
| 3 | 3-1 | 7.88% |
| 4 | 1-1 | 7.76% |
| 5 | 1-0 | 6.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 66.7% | 69.1% | 1.51 | +0.7% |
| Draw | 18.1% | 17.6% | 4.88 | -11.7% |
| Elche CF win | 15.2% | 13.4% | 6.73 | +2.3% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.59 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.17 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.34 |
| Fair Over 3.5 odds | 2.05 |
| Fair Under 3.5 odds | 1.95 |
| Fair Over 4.5 odds | 3.38 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 87.6% |
| Raw p under 3 5 | 51.5% |
| Raw p btts yes | 63.4% |
| P home draw | 84.8% |
| P draw away | 33.3% |
| P home away | 81.9% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.7% |
| Raw p home away | 81.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.39 |
| Reference draw odds | 4.70 |
| Reference away odds | 6.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Home probability edge | -2.4% |
| Draw probability edge | +0.5% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +4.1% |
| Under 2.5 probability edge | -4.1% |
| Raw edge prob home | -0.0473 |
| Raw ev home | -0.0284 |
| Raw edge prob draw | 0.0103 |
| Raw ev draw | -0.0924 |
| Raw edge prob away | 0.0370 |
| Raw ev away | 0.1480 |
| Market p home draw | 85.2% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T09:50:24Z |
| Market reference home draw last update utc | 2026-10-15T09:50:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.0% |
| Market draw away odds | 2.75 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T09:50:24Z |
| Market reference draw away last update utc | 2026-10-15T09:50:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.9% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T09:50:24Z |
| Market reference home away last update utc | 2026-10-15T09:50:39Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.12 |
| Market reference dc draw away odds | 2.81 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 86.0% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.0% |
| Market reference under 3 5 odds | 1.70 |
| Market reference under 3 5 opposite odds | 2.22 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.3% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T09:50:24Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.36 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **55.9%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.33 combined). The most likely exact score is 2-2 at 7.5%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.3%; Under 3.5 goals: 38.0%; Double Chance 1X: 77.1%; Double Chance X2: 44.1%; Double Chance 12 (either team wins): 78.8%; Under 4.5 goals: 57.9%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 55.9% | 1.79 |
| Draw | 21.2% | 4.72 |
| Real Racing Club de Santander win | 22.9% | 4.37 |

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
| Over 2.5 | 79.3% |
| Under 2.5 | 20.7% |
| Over 3.5 | 62.0% |
| Under 3.5 | 38.0% |
| Over 4.5 | 42.1% |
| Under 4.5 | 57.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.53% |
| 2 | 1-1 | 7.15% |
| 3 | 2-1 | 6.98% |
| 4 | 3-1 | 6.46% |
| 5 | 1-2 | 5.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 55.9% | 48.5% | 2.04 | +14.0% |
| Draw | 21.2% | 25.2% | 3.72 | -21.1% |
| Real Racing Club de Santander win | 22.9% | 26.3% | 3.88 | -11.1% |
| Over 2.5 | 79.3% | 55.4% | 1.74 | +38.0% |
| Under 2.5 | 20.7% | 44.6% | 2.27 | -53.0% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| P btts yes | 75.1% |
| P btts no | 24.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 56.47 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.91 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.83 |
| Fair Over 3.5 odds | 1.61 |
| Fair Under 3.5 odds | 2.63 |
| Fair Over 4.5 odds | 2.38 |
| Fair Under 4.5 odds | 1.73 |
| Unadjusted home-win probability | 63.3% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 19.5% |
| Raw p over 1 5 | 93.1% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 73.9% |
| P home draw | 77.1% |
| P draw away | 44.1% |
| P home away | 78.8% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Raw p home away | 82.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.93 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.37 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | +7.4% |
| Draw probability edge | -4.0% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | +23.8% |
| Under 2.5 probability edge | -23.8% |
| Raw edge prob home | 0.1475 |
| Raw ev home | 0.2905 |
| Raw edge prob draw | -0.0800 |
| Raw ev draw | -0.3599 |
| Raw edge prob away | -0.0675 |
| Raw ev away | -0.2422 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **47.9%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 43.6%; Under 3.5 goals: 77.3%; Double Chance 1X: 75.3%; Double Chance X2: 52.1%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 47.9% | 2.09 |
| Draw | 27.3% | 3.66 |
| Alavés win | 24.7% | 4.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.49 |
| Alavés expected goals | 0.94 |
| Expected total goals | 2.44 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
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
| 1 | 1-1 | 12.90% |
| 2 | 1-0 | 12.36% |
| 3 | 2-0 | 9.40% |
| 4 | 0-0 | 9.24% |
| 5 | 2-1 | 8.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 47.9% | 46.2% | 2.16 | +3.5% |
| Draw | 27.3% | 28.0% | 3.48 | -4.8% |
| Alavés win | 24.7% | 25.8% | 3.78 | -6.6% |
| Over 2.5 | 43.6% | 41.5% | 2.30 | +0.4% |
| Under 2.5 | 56.4% | 58.5% | 1.72 | -3.1% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.83 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.29 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.07 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 47.6% |
| P home draw | 75.3% |
| P draw away | 52.1% |
| P home away | 72.7% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.02 |
| Reference draw odds | 3.18 |
| Reference away odds | 3.43 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.25 |
| Reference Under 2.5 odds | 1.64 |
| Home probability edge | +1.8% |
| Draw probability edge | -0.7% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | 0.0354 |
| Raw ev home | 0.0737 |
| Raw edge prob draw | -0.0138 |
| Raw ev draw | -0.0724 |
| Raw edge prob away | -0.0216 |
| Raw ev away | -0.1065 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.3%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.6%. Goal-market probabilities: at least one goal: 85.6%; Over 2.5 goals: 29.6%; Under 3.5 goals: 87.9%; Double Chance 1X: 51.7%; Double Chance X2: 76.6%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.3%; BTTS No (at least one team does not score): 66.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.4% | 4.27 |
| Draw | 28.2% | 3.54 |
| Real Sociedad win | 48.3% | 2.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.63 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.89 |
| Over 0.5 | 85.6% |
| Under 0.5 | 14.4% |
| Over 1.5 | 56.1% |
| Under 1.5 | 43.9% |
| Over 2.5 | 29.6% |
| Under 2.5 | 70.4% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.64% |
| 2 | 0-0 | 14.40% |
| 3 | 1-0 | 11.88% |
| 4 | 1-1 | 11.43% |
| 5 | 0-2 | 11.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.4% | 28.7% | 3.29 | -22.9% |
| Draw | 28.2% | 26.3% | 3.63 | +2.5% |
| Real Sociedad win | 48.3% | 45.0% | 2.29 | +10.7% |
| Over 2.5 | 29.6% | 54.5% | 1.86 | -45.0% |
| Under 2.5 | 70.4% | 45.5% | 2.10 | +47.9% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| P btts yes | 33.3% |
| P btts no | 66.7% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.95 |
| Fair Over 1.5 odds | 1.78 |
| Fair Under 1.5 odds | 2.28 |
| Fair Over 2.5 odds | 3.38 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.25 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.19 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 51.7% |
| P draw away | 76.6% |
| P home away | 71.8% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Raw p home away | 69.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.12 |
| Reference draw odds | 3.37 |
| Reference away odds | 2.07 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.07 |
| Home probability edge | -5.2% |
| Draw probability edge | +1.9% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | -25.0% |
| Under 2.5 probability edge | +25.0% |
| Raw edge prob home | -0.1047 |
| Raw ev home | -0.4013 |
| Raw edge prob draw | 0.0379 |
| Raw ev draw | 0.0939 |
| Raw edge prob away | 0.0668 |
| Raw ev away | 0.1832 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.8%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.1%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 65.9%; Under 3.5 goals: 56.3%; Double Chance 1X: 92.2%; Double Chance X2: 21.2%; Double Chance 12 (either team wins): 86.5%; Under 4.5 goals: 74.7%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.8% | 1.27 |
| Draw | 13.5% | 7.43 |
| Sevilla win | 7.8% | 12.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.63 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.9% |
| Under 2.5 | 34.1% |
| Over 3.5 | 43.7% |
| Under 3.5 | 56.3% |
| Over 4.5 | 25.3% |
| Under 4.5 | 74.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.09% |
| 2 | 3-0 | 10.58% |
| 3 | 1-0 | 9.07% |
| 4 | 2-1 | 8.97% |
| 5 | 3-1 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 78.8% | 80.1% | 1.29 | +1.6% |
| Draw | 13.5% | 12.4% | 6.71 | -9.7% |
| Sevilla win | 7.8% | 7.5% | 11.20 | -12.9% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.09 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.79 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.96 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.7% |
| P home draw | 92.2% |
| P draw away | 21.2% |
| P home away | 86.5% |
| Raw p home draw | 91.9% |
| Raw p draw away | 22.6% |
| Raw p home away | 85.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.21 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.25 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | -1.3% |
| Draw probability edge | +1.0% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0265 |
| Raw ev home | -0.0009 |
| Raw edge prob draw | 0.0209 |
| Raw ev draw | -0.0269 |
| Raw edge prob away | 0.0055 |
| Raw ev away | -0.0982 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **34.8%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.4%. Goal-market probabilities: at least one goal: 81.6%; Over 2.5 goals: 23.2%; Under 3.5 goals: 91.5%; Double Chance 1X: 67.9%; Double Chance X2: 65.2%; Double Chance 12 (either team wins): 67.0%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 30.9%; BTTS No (at least one team does not score): 69.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 34.8% | 2.87 |
| Draw | 33.0% | 3.03 |
| Rayo Vallecano win | 32.1% | 3.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.91 |
| Rayo Vallecano expected goals | 0.74 |
| Expected total goals | 1.64 |
| Over 0.5 | 81.6% |
| Under 0.5 | 18.4% |
| Over 1.5 | 49.1% |
| Under 1.5 | 50.9% |
| Over 2.5 | 23.2% |
| Under 2.5 | 76.8% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.44% |
| 2 | 0-1 | 16.27% |
| 3 | 1-0 | 16.15% |
| 4 | 1-1 | 12.39% |
| 5 | 2-0 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 34.8% | 32.4% | 2.99 | +4.2% |
| Draw | 33.0% | 30.9% | 3.16 | +4.3% |
| Rayo Vallecano win | 32.1% | 36.7% | 2.74 | -11.9% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| Fair Under 0.5 odds | 5.42 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.30 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.78 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.53 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.1% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.3% |
| P home draw | 67.9% |
| P draw away | 65.2% |
| P home away | 67.0% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.7% |
| Raw p home away | 64.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.80 |
| Reference draw odds | 2.92 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.50 |
| Reference Under 2.5 odds | 1.53 |
| Home probability edge | +2.4% |
| Draw probability edge | +2.1% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -13.8% |
| Under 2.5 probability edge | +13.8% |
| Raw edge prob home | 0.0490 |
| Raw ev home | 0.1149 |
| Raw edge prob draw | 0.0415 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0905 |
| Raw ev away | -0.2431 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.6%**. Expected goals are 1.29 for Levante and 1.39 for Athletic Bilbao (2.68 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 50.1%; Under 3.5 goals: 71.8%; Double Chance 1X: 57.4%; Double Chance X2: 69.4%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 30.6% | 3.26 |
| Draw | 26.8% | 3.73 |
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
| 1 | 1-1 | 12.74% |
| 2 | 0-1 | 10.08% |
| 3 | 1-2 | 9.29% |
| 4 | 1-0 | 7.62% |
| 5 | 0-2 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 30.6% | 26.8% | 3.52 | +7.8% |
| Draw | 26.8% | 27.2% | 3.52 | -5.7% |
| Athletic Bilbao win | 42.6% | 46.0% | 2.24 | -4.7% |
| Over 2.5 | 50.1% | 49.0% | 2.02 | +1.2% |
| Under 2.5 | 49.9% | 51.0% | 1.92 | -4.2% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.89 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.02 |
| Fair Over 2.5 odds | 2.00 |
| Fair Under 2.5 odds | 2.00 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.45 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 39.2% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 54.7% |
| P home draw | 57.4% |
| P draw away | 69.4% |
| P home away | 73.2% |
| Raw p home draw | 60.8% |
| Raw p draw away | 65.5% |
| Raw p home away | 73.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.32 |
| Reference draw odds | 3.27 |
| Reference away odds | 2.03 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +3.8% |
| Draw probability edge | -0.4% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | 0.0769 |
| Raw ev home | 0.2136 |
| Raw edge prob draw | -0.0087 |
| Raw ev draw | -0.0719 |
| Raw edge prob away | -0.0681 |
| Raw ev away | -0.1229 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **56.8%**. Expected goals are 1.38 for Alavés and 0.44 for Málaga (1.82 combined). The most likely exact score is 1-0 at 20.9%. Goal-market probabilities: at least one goal: 84.1%; Over 2.5 goals: 27.2%; Under 3.5 goals: 89.2%; Double Chance 1X: 83.9%; Double Chance X2: 43.2%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 96.3%; BTTS Yes (both teams score): 26.7%; BTTS No (at least one team does not score): 73.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 56.8% | 1.76 |
| Draw | 27.1% | 3.70 |
| Málaga win | 16.1% | 6.21 |

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
| Over 2.5 | 27.2% |
| Under 2.5 | 72.8% |
| Over 3.5 | 10.8% |
| Under 3.5 | 89.2% |
| Over 4.5 | 3.7% |
| Under 4.5 | 96.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.90% |
| 2 | 0-0 | 15.88% |
| 3 | 2-0 | 14.53% |
| 4 | 0-1 | 9.70% |
| 5 | 1-1 | 9.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 56.8% | 53.2% | 1.89 | +7.4% |
| Draw | 27.1% | 26.1% | 3.73 | +0.9% |
| Málaga win | 16.1% | 20.7% | 4.57 | -26.5% |
| Over 2.5 | 27.2% | 47.4% | 2.07 | -43.8% |
| Under 2.5 | 72.8% | 52.6% | 1.88 | +37.0% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| Fair Under 0.5 odds | 6.30 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.68 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.27 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 27.25 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 11.5% |
| Raw p over 1 5 | 54.4% |
| Raw p under 3 5 | 88.9% |
| Raw p btts yes | 26.7% |
| P home draw | 83.9% |
| P draw away | 43.2% |
| P home away | 72.9% |
| Raw p home draw | 88.5% |
| Raw p draw away | 39.5% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.75 |
| Reference draw odds | 3.30 |
| Reference away odds | 4.05 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +3.6% |
| Draw probability edge | +1.0% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -20.2% |
| Under 2.5 probability edge | +20.2% |
| Raw edge prob home | 0.0721 |
| Raw ev home | 0.1426 |
| Raw edge prob draw | 0.0199 |
| Raw ev draw | 0.0465 |
| Raw edge prob away | -0.0920 |
| Raw ev away | -0.4749 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **74.4%**. Expected goals are 2.31 for Atlético Madrid and 0.98 for Deportivo La Coruña (3.29 combined). The most likely exact score is 2-0 at 11.0%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 65.6%; Under 3.5 goals: 57.1%; Double Chance 1X: 89.8%; Double Chance X2: 25.6%; Double Chance 12 (either team wins): 84.6%; Under 4.5 goals: 75.3%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 74.4% | 1.34 |
| Draw | 15.4% | 6.50 |
| Deportivo La Coruña win | 10.2% | 9.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.31 |
| Deportivo La Coruña expected goals | 0.98 |
| Expected total goals | 3.29 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 42.9% |
| Under 3.5 | 57.1% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.03% |
| 2 | 2-1 | 10.83% |
| 3 | 1-0 | 9.36% |
| 4 | 3-0 | 8.50% |
| 5 | 3-1 | 8.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 74.4% | 81.9% | 1.24 | -7.7% |
| Draw | 15.4% | 12.1% | 6.92 | +6.4% |
| Deportivo La Coruña win | 10.2% | 6.0% | 14.90 | +51.9% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.21 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.65 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
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
| P home draw | 89.8% |
| P draw away | 25.6% |
| P home away | 84.6% |
| Raw p home draw | 85.6% |
| Raw p draw away | 33.0% |
| Raw p home away | 81.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.18 |
| Reference draw odds | 5.75 |
| Reference away odds | 10.25 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.48 |
| Home probability edge | -7.5% |
| Draw probability edge | +3.3% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | +2.2% |
| Under 2.5 probability edge | -2.2% |
| Raw edge prob home | -0.1492 |
| Raw ev home | -0.1696 |
| Raw edge prob draw | 0.0656 |
| Raw ev draw | 0.2910 |
| Raw edge prob away | 0.0836 |
| Raw ev away | 1.1422 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **49.8%**. Expected goals are 1.39 for Rayo Vallecano and 1.06 for Elche CF (2.46 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.4%; Double Chance 1X: 75.6%; Double Chance X2: 50.2%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 89.4%; BTTS Yes (both teams score): 49.0%; BTTS No (at least one team does not score): 51.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 49.8% | 2.01 |
| Draw | 25.8% | 3.88 |
| Elche CF win | 24.4% | 4.09 |

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
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.16% |
| 2 | 1-1 | 12.20% |
| 3 | 2-1 | 9.97% |
| 4 | 2-0 | 9.37% |
| 5 | 0-0 | 8.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 49.8% | 55.4% | 1.81 | -9.8% |
| Draw | 25.8% | 24.2% | 3.94 | +1.5% |
| Elche CF win | 24.4% | 20.4% | 4.78 | +16.8% |
| Over 2.5 | 45.2% | 52.5% | 1.88 | -15.0% |
| Under 2.5 | 54.8% | 47.5% | 2.07 | +13.4% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| Fair Under 0.5 odds | 12.04 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.44 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.47 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 44.2% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 28.5% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 49.5% |
| P home draw | 75.6% |
| P draw away | 50.2% |
| P home away | 74.2% |
| Raw p home draw | 71.5% |
| Raw p draw away | 55.8% |
| Raw p home away | 72.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.69 |
| Reference draw odds | 3.53 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.01 |
| Home probability edge | -5.6% |
| Draw probability edge | +1.6% |
| Away probability edge | +4.0% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.1117 |
| Raw ev home | -0.1995 |
| Raw edge prob draw | 0.0315 |
| Raw ev draw | 0.0766 |
| Raw edge prob away | 0.0802 |
| Raw ev away | 0.3599 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **39.6%**. Expected goals are 1.96 for Real Racing Club de Santander and 1.99 for Espanyol (3.95 combined). The most likely exact score is 1-1 at 8.5%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 74.8%; Under 3.5 goals: 44.3%; Double Chance 1X: 63.2%; Double Chance X2: 60.4%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 64.3%; BTTS Yes (both teams score): 74.9%; BTTS No (at least one team does not score): 25.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 39.6% | 2.52 |
| Draw | 23.6% | 4.24 |
| Espanyol win | 36.8% | 2.72 |

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
| 1 | 1-1 | 8.53% |
| 2 | 2-2 | 8.17% |
| 3 | 2-1 | 7.51% |
| 4 | 1-2 | 6.86% |
| 5 | 3-1 | 4.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 39.6% | 40.5% | 2.47 | -2.1% |
| Draw | 23.6% | 26.0% | 3.72 | -12.3% |
| Espanyol win | 36.8% | 33.5% | 2.93 | +7.9% |
| Over 2.5 | 74.8% | 56.6% | 1.78 | +33.2% |
| Under 2.5 | 25.2% | 43.4% | 2.21 | -44.4% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| Fair Under 0.5 odds | 43.36 |
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
| P home draw | 63.2% |
| P draw away | 60.4% |
| P home away | 76.4% |
| Raw p home draw | 59.9% |
| Raw p draw away | 61.3% |
| Raw p home away | 78.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.25 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.67 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | -0.9% |
| Draw probability edge | -2.4% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | +18.2% |
| Under 2.5 probability edge | -18.2% |
| Raw edge prob home | -0.0178 |
| Raw ev home | -0.0433 |
| Raw edge prob draw | -0.0487 |
| Raw ev draw | -0.2140 |
| Raw edge prob away | 0.0666 |
| Raw ev away | 0.1760 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **45.1%**. Expected goals are 1.33 for Valencia and 1.62 for Villarreal (2.95 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 56.5%; Under 3.5 goals: 65.8%; Double Chance 1X: 54.9%; Double Chance X2: 70.2%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 82.4%; BTTS Yes (both teams score): 59.3%; BTTS No (at least one team does not score): 40.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.8% | 3.36 |
| Draw | 25.1% | 3.99 |
| Villarreal win | 45.1% | 2.22 |

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
| Over 2.5 | 56.5% |
| Under 2.5 | 43.5% |
| Over 3.5 | 34.2% |
| Under 3.5 | 65.8% |
| Over 4.5 | 17.6% |
| Under 4.5 | 82.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.67% |
| 2 | 1-2 | 9.34% |
| 3 | 0-1 | 8.44% |
| 4 | 2-1 | 7.17% |
| 5 | 0-2 | 7.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.8% | 28.5% | 3.45 | +2.8% |
| Draw | 25.1% | 25.4% | 3.78 | -5.3% |
| Villarreal win | 45.1% | 46.1% | 2.17 | -2.1% |
| Over 2.5 | 56.5% | 56.6% | 1.78 | +0.5% |
| Under 2.5 | 43.5% | 43.4% | 2.20 | -4.2% |

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
| Market best home last update utc | 2026-10-15T09:50:24Z |
| Market best draw last update utc | 2026-10-15T09:50:24Z |
| Market best away last update utc | 2026-10-15T09:50:24Z |
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
| Fair Under 0.5 odds | 18.06 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.90 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
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
| P draw away | 70.2% |
| P home away | 74.9% |
| Raw p home draw | 55.8% |
| Raw p draw away | 68.9% |
| Raw p home away | 75.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.07 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | +1.3% |
| Draw probability edge | -0.4% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0258 |
| Raw ev home | 0.0727 |
| Raw edge prob draw | -0.0075 |
| Raw ev draw | -0.0669 |
| Raw edge prob away | -0.0183 |
| Raw ev away | -0.0404 |

</details>


---
