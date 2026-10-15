# La Liga — football model report

Fixtures in this report: **18**.

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
| Training sha256 | 24e4ff685bc9d043dfd999f14263b1239924c80c9adfc23f087cb89f852fb86d |
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
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 9.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
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

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.3%**. Expected goals are 2.04 for Deportivo La Coruña and 1.32 for Levante (3.36 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.4%; Under 3.5 goals: 57.0%; Double Chance 1X: 74.4%; Double Chance X2: 49.7%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 64.6%; BTTS No (at least one team does not score): 35.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.3% | 1.99 |
| Draw | 24.1% | 4.15 |
| Levante win | 25.6% | 3.90 |

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
| Over 2.5 | 64.4% |
| Under 2.5 | 35.6% |
| Over 3.5 | 43.0% |
| Under 3.5 | 57.0% |
| Over 4.5 | 24.3% |
| Under 4.5 | 75.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.57% |
| 2 | 2-1 | 8.90% |
| 3 | 2-2 | 6.99% |
| 4 | 2-0 | 6.74% |
| 5 | 1-2 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.3% | 46.7% | 2.17 | +9.1% |
| Draw | 24.1% | 26.5% | 3.60 | -13.3% |
| Levante win | 25.6% | 26.9% | 3.62 | -7.2% |
| Over 2.5 | 64.4% | 50.0% | 1.98 | +27.5% |
| Under 2.5 | 35.6% | 50.0% | 1.96 | -30.2% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.6% |
| P btts no | 35.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.68 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.62 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.11 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 53.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 64.0% |
| P home draw | 74.4% |
| P draw away | 49.7% |
| P home away | 75.9% |
| Raw p home draw | 75.6% |
| Raw p draw away | 46.1% |
| Raw p home away | 78.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | +3.6% |
| Draw probability edge | -2.4% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +14.4% |
| Under 2.5 probability edge | -14.4% |
| Raw edge prob home | 0.0721 |
| Raw ev home | 0.1694 |
| Raw edge prob draw | -0.0473 |
| Raw ev draw | -0.2177 |
| Raw edge prob away | -0.0248 |
| Raw ev away | -0.1174 |
| Market p home draw | 72.7% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:30Z |
| Market reference home draw last update utc | 2026-10-15T15:31:51Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.6% |
| Market draw away odds | 1.77 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:30Z |
| Market reference draw away last update utc | 2026-10-15T15:31:51Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.7% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:30Z |
| Market reference home away last update utc | 2026-10-15T15:31:51Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.77 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 74.7% |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 72.4% |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:47Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 54.9% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:30Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.18 |
| Market reference btts yes last update utc | 2026-10-15T15:32:03Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **53.4%**. Expected goals are 1.02 for Espanyol and 1.59 for Atlético Madrid (2.61 combined). The most likely exact score is 0-1 at 12.1%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 49.0%; Under 3.5 goals: 73.1%; Double Chance 1X: 46.6%; Double Chance X2: 77.7%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 22.3% | 4.48 |
| Draw | 24.3% | 4.12 |
| Atlético Madrid win | 53.4% | 1.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.02 |
| Atlético Madrid expected goals | 1.59 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 49.0% |
| Under 2.5 | 51.0% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.15% |
| 2 | 1-1 | 11.55% |
| 3 | 1-2 | 10.08% |
| 4 | 0-2 | 9.84% |
| 5 | 0-0 | 7.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 22.3% | 20.4% | 4.88 | +9.0% |
| Draw | 24.3% | 22.9% | 3.94 | -4.4% |
| Atlético Madrid win | 53.4% | 56.6% | 1.80 | -3.9% |
| Over 2.5 | 49.0% | 52.6% | 1.87 | -8.4% |
| Under 2.5 | 51.0% | 47.4% | 2.08 | +6.1% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Fair Under 0.5 odds | 13.91 |
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
| P home draw | 46.6% |
| P draw away | 77.7% |
| P home away | 75.7% |
| Raw p home draw | 49.8% |
| Raw p draw away | 75.8% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.40 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | +1.9% |
| Draw probability edge | +1.3% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | 0.0381 |
| Raw ev home | 0.1834 |
| Raw edge prob draw | 0.0264 |
| Raw ev draw | 0.0080 |
| Raw edge prob away | -0.0646 |
| Raw ev away | -0.0970 |
| Market p home draw | 45.2% |
| Market home draw odds | 2.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:30Z |
| Market reference home draw last update utc | 2026-10-15T15:31:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 79.6% |
| Market draw away odds | 1.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:30Z |
| Market reference draw away last update utc | 2026-10-15T15:31:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:30Z |
| Market reference home away last update utc | 2026-10-15T15:31:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.13 |
| Market reference dc draw away odds | 1.21 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 77.7% |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 4.15 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 68.8% |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 3.05 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:47Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 54.2% |
| Market btts yes odds | 1.73 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:30Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 2.09 |
| Market reference btts yes last update utc | 2026-10-15T15:31:55Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **62.3%**. Expected goals are 1.35 for Real Betis and 2.07 for Barcelona (3.42 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 68.0%; Under 3.5 goals: 54.7%; Double Chance 1X: 37.7%; Double Chance X2: 79.8%; Double Chance 12 (either team wins): 82.5%; Under 4.5 goals: 73.0%; BTTS Yes (both teams score): 63.7%; BTTS No (at least one team does not score): 36.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 20.2% | 4.96 |
| Draw | 17.5% | 5.72 |
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
| Over 2.5 | 68.0% |
| Under 2.5 | 32.0% |
| Over 3.5 | 45.3% |
| Under 3.5 | 54.7% |
| Over 4.5 | 27.0% |
| Under 4.5 | 73.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.94% |
| 2 | 0-2 | 8.10% |
| 3 | 0-1 | 7.61% |
| 4 | 1-1 | 7.56% |
| 5 | 1-3 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 20.2% | 15.8% | 6.32 | +27.5% |
| Draw | 17.5% | 13.4% | 5.65 | -1.3% |
| Barcelona win | 62.3% | 70.8% | 1.47 | -8.3% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| P btts yes | 63.7% |
| P btts no | 36.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.76 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.21 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.13 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.70 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 24.6% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 55.3% |
| Raw p btts yes | 65.0% |
| P home draw | 37.7% |
| P draw away | 79.8% |
| P home away | 82.5% |
| Raw p home draw | 46.1% |
| Raw p draw away | 75.4% |
| Raw p home away | 78.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 5.40 |
| Reference draw odds | 6.25 |
| Reference away odds | 1.37 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.24 |
| Reference Under 2.5 odds | 3.95 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Home probability edge | +4.4% |
| Draw probability edge | +4.1% |
| Away probability edge | -8.5% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | 0.0884 |
| Raw ev home | 0.5546 |
| Raw edge prob draw | 0.0810 |
| Raw ev draw | 0.2163 |
| Raw edge prob away | -0.1695 |
| Raw ev away | -0.2080 |
| Market p home draw | 32.9% |
| Market home draw odds | 2.90 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:30Z |
| Market reference home draw last update utc | 2026-10-15T15:31:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.3% |
| Market draw away odds | 1.14 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:30Z |
| Market reference draw away last update utc | 2026-10-15T15:31:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.8% |
| Market home away odds | 1.18 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:30Z |
| Market reference home away last update utc | 2026-10-15T15:31:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.92 |
| Market reference dc draw away odds | 1.14 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 92.7% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 10.50 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 40.8% |
| Market reference under 3 5 odds | 2.36 |
| Market reference under 3 5 opposite odds | 1.65 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:47Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 68.2% |
| Market btts yes odds | 1.39 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:30Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 3.05 |
| Market reference btts yes last update utc | 2026-10-15T15:32:03Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **40.5%**. Expected goals are 1.07 for Valencia and 1.17 for Athletic Bilbao (2.24 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.1%; Double Chance 1X: 59.5%; Double Chance X2: 69.2%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.4%; BTTS No (at least one team does not score): 54.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.8% | 3.24 |
| Draw | 28.7% | 3.48 |
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
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.32% |
| 2 | 0-1 | 13.05% |
| 3 | 0-0 | 10.69% |
| 4 | 1-0 | 10.41% |
| 5 | 1-2 | 8.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.8% | 28.6% | 3.47 | +7.0% |
| Draw | 28.7% | 28.1% | 3.51 | +0.8% |
| Athletic Bilbao win | 40.5% | 43.3% | 2.26 | -8.6% |
| Over 2.5 | 39.0% | 45.2% | 2.10 | -18.1% |
| Under 2.5 | 61.0% | 54.8% | 1.86 | +13.4% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
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
| P home draw | 59.5% |
| P draw away | 69.2% |
| P home away | 71.3% |
| Raw p home draw | 62.4% |
| Raw p draw away | 66.9% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.25 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.72 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | +2.2% |
| Draw probability edge | +0.6% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | 0.0448 |
| Raw ev home | 0.1475 |
| Raw edge prob draw | 0.0118 |
| Raw ev draw | 0.0287 |
| Raw edge prob away | -0.0565 |
| Raw ev away | -0.1497 |
| Market p home draw | 56.2% |
| Market home draw odds | 1.72 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:30Z |
| Market reference home draw last update utc | 2026-10-15T15:31:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.7% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:30Z |
| Market reference draw away last update utc | 2026-10-15T15:31:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.2% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:30Z |
| Market reference home away last update utc | 2026-10-15T15:31:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.71 |
| Market reference dc draw away odds | 1.34 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 71.7% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:30:59Z |
| Market reference over 1 5 odds | 1.37 |
| Market reference over 1 5 opposite odds | 3.30 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.8% |
| Market under 3 5 odds | 1.25 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:30:59Z |
| Market reference under 3 5 odds | 1.30 |
| Market reference under 3 5 opposite odds | 3.85 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.3% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:30Z |
| Market reference btts yes odds | 1.88 |
| Market reference btts yes opposite odds | 2.06 |
| Market reference btts yes last update utc | 2026-10-15T15:32:03Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.9%**. Expected goals are 2.41 for Villarreal and 1.19 for Elche CF (3.60 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 70.0%; Under 3.5 goals: 51.3%; Double Chance 1X: 83.8%; Double Chance X2: 34.1%; Double Chance 12 (either team wins): 82.1%; Under 4.5 goals: 70.4%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.9% | 1.52 |
| Draw | 17.9% | 5.58 |
| Elche CF win | 16.2% | 6.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.41 |
| Elche CF expected goals | 1.19 |
| Expected total goals | 3.60 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 70.0% |
| Under 2.5 | 30.0% |
| Over 3.5 | 48.7% |
| Under 3.5 | 51.3% |
| Over 4.5 | 29.6% |
| Under 4.5 | 70.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.67% |
| 2 | 2-0 | 8.16% |
| 3 | 3-1 | 7.78% |
| 4 | 1-1 | 7.69% |
| 5 | 1-0 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.9% | 67.5% | 1.51 | -0.5% |
| Draw | 17.9% | 17.2% | 4.88 | -12.6% |
| Elche CF win | 16.2% | 15.3% | 6.73 | +8.8% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Fair Under 0.5 odds | 35.92 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.12 |
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
| P home draw | 83.8% |
| P draw away | 34.1% |
| P home away | 82.1% |
| Raw p home draw | 82.9% |
| Raw p draw away | 35.7% |
| Raw p home away | 81.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.44 |
| Reference draw odds | 5.10 |
| Reference away odds | 5.70 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.68 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Home probability edge | -1.6% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | +4.0% |
| Under 2.5 probability edge | -4.0% |
| Raw edge prob home | -0.0313 |
| Raw ev home | -0.0284 |
| Raw edge prob draw | 0.0136 |
| Raw ev draw | -0.0925 |
| Raw edge prob away | 0.0177 |
| Raw ev away | 0.1479 |
| Market p home draw | 85.8% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:30Z |
| Market reference home draw last update utc | 2026-10-15T15:31:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.7% |
| Market draw away odds | 2.75 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:30Z |
| Market reference draw away last update utc | 2026-10-15T15:31:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.5% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:30Z |
| Market reference home away last update utc | 2026-10-15T15:31:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.12 |
| Market reference dc draw away odds | 2.77 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 85.3% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 56.8% |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.24 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:47Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.8% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:30Z |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-15T15:32:03Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **55.5%**. Expected goals are 2.78 for CA Osasuna and 1.55 for Real Racing Club de Santander (4.33 combined). The most likely exact score is 2-2 at 7.5%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.3%; Under 3.5 goals: 38.0%; Double Chance 1X: 76.5%; Double Chance X2: 44.5%; Double Chance 12 (either team wins): 79.0%; Under 4.5 goals: 57.9%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 55.5% | 1.80 |
| Draw | 21.0% | 4.77 |
| Real Racing Club de Santander win | 23.5% | 4.25 |

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
| 1 | 2-2 | 7.45% |
| 2 | 1-1 | 7.07% |
| 3 | 2-1 | 6.93% |
| 4 | 3-1 | 6.42% |
| 5 | 1-2 | 5.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 55.5% | 47.7% | 2.04 | +13.2% |
| Draw | 21.0% | 24.8% | 3.72 | -22.0% |
| Real Racing Club de Santander win | 23.5% | 27.5% | 3.88 | -8.7% |
| Over 2.5 | 79.3% | 57.6% | 1.74 | +38.0% |
| Under 2.5 | 20.7% | 42.4% | 2.27 | -53.1% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| P btts yes | 75.1% |
| P btts no | 24.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 57.09 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.88 |
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
| P home draw | 76.5% |
| P draw away | 44.5% |
| P home away | 79.0% |
| Raw p home draw | 80.5% |
| Raw p draw away | 36.7% |
| Raw p home away | 82.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.35 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | +7.8% |
| Draw probability edge | -3.8% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | +21.7% |
| Under 2.5 probability edge | -21.7% |
| Raw edge prob home | 0.1554 |
| Raw ev home | 0.2907 |
| Raw edge prob draw | -0.0755 |
| Raw ev draw | -0.3600 |
| Raw edge prob away | -0.0799 |
| Raw ev away | -0.2423 |
| Market p home draw | 74.7% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:30Z |
| Market reference home draw last update utc | 2026-10-15T15:31:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.8% |
| Market draw away odds | 1.86 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:30Z |
| Market reference draw away last update utc | 2026-10-15T15:31:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.5% |
| Market home away odds | 1.32 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:30Z |
| Market reference home away last update utc | 2026-10-15T15:31:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 1.86 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.9% |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.72 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:47Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 61.1% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:30Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.52 |
| Market reference btts yes last update utc | 2026-10-15T15:32:03Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **47.6%**. Expected goals are 1.49 for Celta Vigo and 0.94 for Alavés (2.44 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 43.7%; Under 3.5 goals: 77.3%; Double Chance 1X: 74.8%; Double Chance X2: 52.4%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 47.6% | 2.10 |
| Draw | 27.2% | 3.68 |
| Alavés win | 25.2% | 3.96 |

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
| Over 2.5 | 43.7% |
| Under 2.5 | 56.3% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.82% |
| 2 | 1-0 | 12.27% |
| 3 | 2-0 | 9.33% |
| 4 | 0-0 | 9.18% |
| 5 | 2-1 | 8.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 47.6% | 45.5% | 2.16 | +2.8% |
| Draw | 27.2% | 27.7% | 3.48 | -5.4% |
| Alavés win | 25.2% | 26.8% | 3.78 | -4.6% |
| Over 2.5 | 43.7% | 41.4% | 2.30 | +0.5% |
| Under 2.5 | 56.3% | 58.6% | 1.72 | -3.1% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Fair Under 0.5 odds | 10.89 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.29 |
| Fair Under 2.5 odds | 1.78 |
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
| P home draw | 74.8% |
| P draw away | 52.4% |
| P home away | 72.8% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.3% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.22 |
| Reference Under 2.5 odds | 1.62 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | +2.1% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | 0.0424 |
| Raw ev home | 0.0737 |
| Raw edge prob draw | -0.0103 |
| Raw ev draw | -0.0724 |
| Raw edge prob away | -0.0320 |
| Raw ev away | -0.1065 |
| Market p home draw | 73.9% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:31:30Z |
| Market reference home draw last update utc | 2026-10-15T15:31:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.3% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:31:30Z |
| Market reference draw away last update utc | 2026-10-15T15:31:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.7% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:31:30Z |
| Market reference home away last update utc | 2026-10-15T15:31:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.30 |
| Market reference dc draw away odds | 1.77 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 69.6% |
| Market reference over 1 5 odds | 1.41 |
| Market reference over 1 5 opposite odds | 3.10 |
| Market reference over 1 5 last update utc | 2026-10-15T15:31:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 78.2% |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 4.20 |
| Market reference under 3 5 last update utc | 2026-10-15T15:31:47Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 48.6% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:31:30Z |
| Market reference btts yes odds | 2.02 |
| Market reference btts yes opposite odds | 1.91 |
| Market reference btts yes last update utc | 2026-10-15T15:32:03Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **47.9%**. Expected goals are 0.63 for Málaga and 1.26 for Real Sociedad (1.89 combined). The most likely exact score is 0-1 at 17.5%. Goal-market probabilities: at least one goal: 85.7%; Over 2.5 goals: 29.6%; Under 3.5 goals: 87.9%; Double Chance 1X: 52.1%; Double Chance X2: 75.9%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 33.3%; BTTS No (at least one team does not score): 66.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 24.1% | 4.16 |
| Draw | 28.0% | 3.57 |
| Real Sociedad win | 47.9% | 2.09 |

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
| Over 2.5 | 29.6% |
| Under 2.5 | 70.4% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.50% |
| 2 | 0-0 | 14.28% |
| 3 | 1-0 | 12.20% |
| 4 | 1-1 | 11.33% |
| 5 | 0-2 | 11.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 24.1% | 29.9% | 3.29 | -20.9% |
| Draw | 28.0% | 25.9% | 3.63 | +1.7% |
| Real Sociedad win | 47.9% | 44.2% | 2.29 | +9.8% |
| Over 2.5 | 29.6% | 53.9% | 1.86 | -45.0% |
| Under 2.5 | 70.4% | 46.1% | 2.10 | +47.9% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 33.3% |
| P btts no | 66.7% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 7.00 |
| Fair Over 1.5 odds | 1.79 |
| Fair Under 1.5 odds | 2.27 |
| Fair Over 2.5 odds | 3.38 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.26 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.20 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 56.5% |
| Raw p under 3 5 | 87.7% |
| Raw p btts yes | 33.6% |
| P home draw | 52.1% |
| P draw away | 75.9% |
| P home away | 72.0% |
| Raw p home draw | 48.3% |
| Raw p draw away | 81.8% |
| Raw p home away | 69.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.15 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | -5.9% |
| Draw probability edge | +2.1% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -24.4% |
| Under 2.5 probability edge | +24.4% |
| Raw edge prob home | -0.1172 |
| Raw ev home | -0.4013 |
| Raw edge prob draw | 0.0425 |
| Raw ev draw | 0.0939 |
| Raw edge prob away | 0.0747 |
| Raw ev away | 0.1832 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **78.5%**. Expected goals are 2.63 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 65.8%; Under 3.5 goals: 56.3%; Double Chance 1X: 92.1%; Double Chance X2: 21.5%; Double Chance 12 (either team wins): 86.4%; Under 4.5 goals: 74.8%; BTTS Yes (both teams score): 48.4%; BTTS No (at least one team does not score): 51.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.5% | 1.27 |
| Draw | 13.6% | 7.37 |
| Sevilla win | 7.9% | 12.59 |

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
| Over 2.5 | 65.8% |
| Under 2.5 | 34.2% |
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
| Real Madrid win | 78.5% | 79.5% | 1.29 | +1.3% |
| Draw | 13.6% | 12.6% | 6.71 | -9.0% |
| Sevilla win | 7.9% | 7.8% | 11.20 | -11.0% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.86 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
| Fair Over 3.5 odds | 2.29 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.97 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.5% |
| Raw p btts yes | 48.7% |
| P home draw | 92.1% |
| P draw away | 21.5% |
| P home away | 86.4% |
| Raw p home draw | 91.9% |
| Raw p draw away | 22.6% |
| Raw p home away | 85.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.23 |
| Reference draw odds | 6.50 |
| Reference away odds | 10.00 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Home probability edge | -1.0% |
| Draw probability edge | +0.9% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | -0.0209 |
| Raw ev home | -0.0009 |
| Raw edge prob draw | 0.0188 |
| Raw ev draw | -0.0270 |
| Raw edge prob away | 0.0021 |
| Raw ev away | -0.0983 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.3%**. Expected goals are 0.91 for Getafe and 0.74 for Rayo Vallecano (1.64 combined). The most likely exact score is 0-0 at 18.3%. Goal-market probabilities: at least one goal: 81.7%; Over 2.5 goals: 23.3%; Under 3.5 goals: 91.5%; Double Chance 1X: 68.1%; Double Chance X2: 64.7%; Double Chance 12 (either team wins): 67.2%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 30.9%; BTTS No (at least one team does not score): 69.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.3% | 2.83 |
| Draw | 32.8% | 3.05 |
| Rayo Vallecano win | 31.9% | 3.14 |

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
| 1 | 0-0 | 18.31% |
| 2 | 1-0 | 16.38% |
| 3 | 0-1 | 16.13% |
| 4 | 1-1 | 12.30% |
| 5 | 2-0 | 7.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.3% | 33.4% | 2.99 | +5.7% |
| Draw | 32.8% | 30.5% | 3.16 | +3.6% |
| Rayo Vallecano win | 31.9% | 36.1% | 2.74 | -12.7% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Fair Over 4.5 odds | 37.40 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.3% |
| Unadjusted draw probability | 35.1% |
| Unadjusted away-win probability | 27.6% |
| Raw p over 1 5 | 49.1% |
| Raw p under 3 5 | 91.5% |
| Raw p btts yes | 31.3% |
| P home draw | 68.1% |
| P draw away | 64.7% |
| P home away | 67.2% |
| Raw p home draw | 72.4% |
| Raw p draw away | 62.7% |
| Raw p home away | 64.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.05 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.58 |
| Reference Under 2.5 odds | 1.49 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Home probability edge | +2.0% |
| Draw probability edge | +2.3% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -12.1% |
| Under 2.5 probability edge | +12.1% |
| Raw edge prob home | 0.0390 |
| Raw ev home | 0.1149 |
| Raw edge prob draw | 0.0461 |
| Raw ev draw | 0.1087 |
| Raw edge prob away | -0.0851 |
| Raw ev away | -0.2431 |

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
| Over 2.5 | 50.1% | 47.5% | 2.02 | +1.1% |
| Under 2.5 | 49.9% | 52.5% | 1.92 | -4.1% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.80 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:03Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:03Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | +3.9% |
| Draw probability edge | -0.5% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | +2.5% |
| Under 2.5 probability edge | -2.5% |
| Raw edge prob home | 0.0790 |
| Raw ev home | 0.2136 |
| Raw edge prob draw | -0.0109 |
| Raw ev draw | -0.0719 |
| Raw edge prob away | -0.0681 |
| Raw ev away | -0.1229 |

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
| 1 | 1-0 | 20.82% |
| 2 | 0-0 | 15.75% |
| 3 | 2-0 | 14.47% |
| 4 | 0-1 | 9.97% |
| 5 | 1-1 | 9.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 56.6% | 52.8% | 1.89 | +7.0% |
| Draw | 26.8% | 25.6% | 3.73 | +0.1% |
| Málaga win | 16.5% | 21.6% | 4.57 | -24.4% |
| Over 2.5 | 27.2% | 44.2% | 2.07 | -43.8% |
| Under 2.5 | 72.8% | 55.8% | 1.88 | +36.9% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 26.6% |
| P btts no | 73.4% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.35 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.68 |
| Fair Under 2.5 odds | 1.37 |
| Fair Over 3.5 odds | 9.28 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 27.26 |
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
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | +3.8% |
| Draw probability edge | +1.2% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -17.0% |
| Under 2.5 probability edge | +17.0% |
| Raw edge prob home | 0.0766 |
| Raw ev home | 0.1426 |
| Raw edge prob draw | 0.0243 |
| Raw ev draw | 0.0465 |
| Raw edge prob away | -0.1009 |
| Raw ev away | -0.4749 |

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
| Deportivo La Coruña win | 10.8% | 9.29 |

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
| 4 | 3-0 | 8.45% |
| 5 | 3-1 | 8.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 74.1% | 81.1% | 1.24 | -8.2% |
| Draw | 15.2% | 11.7% | 6.92 | +5.1% |
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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Fair Under 0.5 odds | 31.61 |
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
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.55 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Home probability edge | -7.1% |
| Draw probability edge | +3.5% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | -0.1418 |
| Raw ev home | -0.1696 |
| Raw edge prob draw | 0.0695 |
| Raw ev draw | 0.2910 |
| Raw edge prob away | 0.0723 |
| Raw ev away | 1.1421 |

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
| Over 2.5 | 45.3% | 52.6% | 1.88 | -14.9% |
| Under 2.5 | 54.7% | 47.4% | 2.07 | +13.3% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Unadjusted away-win probability | 28.5% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 49.5% |
| P home draw | 75.0% |
| P draw away | 50.5% |
| P home away | 74.5% |
| Raw p home draw | 71.5% |
| Raw p draw away | 55.8% |
| Raw p home away | 72.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.74 |
| Reference draw odds | 3.75 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | -5.3% |
| Draw probability edge | +1.8% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.1051 |
| Raw ev home | -0.1995 |
| Raw edge prob draw | 0.0359 |
| Raw ev draw | 0.0766 |
| Raw edge prob away | 0.0691 |
| Raw ev away | 0.3599 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Real Racing Club de Santander win** at **40.0%**. Expected goals are 1.96 for Real Racing Club de Santander and 1.99 for Espanyol (3.95 combined). The most likely exact score is 1-1 at 8.4%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 75.0%; Under 3.5 goals: 44.3%; Double Chance 1X: 63.1%; Double Chance X2: 60.0%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 64.2%; BTTS Yes (both teams score): 74.8%; BTTS No (at least one team does not score): 25.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 40.0% | 2.50 |
| Draw | 23.1% | 4.33 |
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
| Over 2.5 | 75.0% |
| Under 2.5 | 25.0% |
| Over 3.5 | 55.7% |
| Under 3.5 | 44.3% |
| Over 4.5 | 35.8% |
| Under 4.5 | 64.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.35% |
| 2 | 2-2 | 8.00% |
| 3 | 2-1 | 7.58% |
| 4 | 1-2 | 6.88% |
| 5 | 3-1 | 4.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 40.0% | 41.2% | 2.47 | -1.3% |
| Draw | 23.1% | 25.0% | 3.72 | -14.1% |
| Espanyol win | 36.9% | 33.8% | 2.93 | +8.3% |
| Over 2.5 | 75.0% | 55.8% | 1.78 | +33.4% |
| Under 2.5 | 25.0% | 44.2% | 2.21 | -44.7% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Fair Under 0.5 odds | 44.27 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 10.67 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 3.99 |
| Fair Over 3.5 odds | 1.80 |
| Fair Under 3.5 odds | 2.26 |
| Fair Over 4.5 odds | 2.79 |
| Fair Under 4.5 odds | 1.56 |
| Unadjusted home-win probability | 38.7% |
| Unadjusted draw probability | 21.1% |
| Unadjusted away-win probability | 40.1% |
| Raw p over 1 5 | 90.6% |
| Raw p under 3 5 | 44.3% |
| Raw p btts yes | 74.4% |
| P home draw | 63.1% |
| P draw away | 60.0% |
| P home away | 76.9% |
| Raw p home draw | 59.9% |
| Raw p draw away | 61.3% |
| Raw p home away | 78.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.25 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | -1.2% |
| Draw probability edge | -2.0% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | +19.2% |
| Under 2.5 probability edge | -19.2% |
| Raw edge prob home | -0.0247 |
| Raw ev home | -0.0433 |
| Raw edge prob draw | -0.0390 |
| Raw ev draw | -0.2140 |
| Raw edge prob away | 0.0638 |
| Raw ev away | 0.1760 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **45.0%**. Expected goals are 1.33 for Valencia and 1.62 for Villarreal (2.95 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 56.6%; Under 3.5 goals: 65.8%; Double Chance 1X: 55.0%; Double Chance X2: 69.8%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.2% | 3.31 |
| Draw | 24.8% | 4.04 |
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
| 1 | 1-1 | 11.54% |
| 2 | 1-2 | 9.32% |
| 3 | 0-1 | 8.42% |
| 4 | 2-1 | 7.26% |
| 5 | 0-2 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.2% | 29.3% | 3.45 | +4.1% |
| Draw | 24.8% | 24.9% | 3.78 | -6.3% |
| Villarreal win | 45.0% | 45.9% | 2.17 | -2.3% |
| Over 2.5 | 56.6% | 55.8% | 1.78 | +0.7% |
| Under 2.5 | 43.4% | 44.2% | 2.20 | -4.4% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Fair Under 0.5 odds | 18.26 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.90 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.67 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 24.7% |
| Unadjusted away-win probability | 44.2% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 59.2% |
| P home draw | 55.0% |
| P draw away | 69.8% |
| P home away | 75.2% |
| Raw p home draw | 55.8% |
| Raw p draw away | 68.9% |
| Raw p home away | 75.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:04Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | 0.0183 |
| Raw ev home | 0.0727 |
| Raw edge prob draw | -0.0019 |
| Raw ev draw | -0.0669 |
| Raw edge prob away | -0.0163 |
| Raw ev away | -0.0404 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **54.7%**. Expected goals are 1.21 for Athletic Bilbao and 0.62 for Getafe (1.83 combined). The most likely exact score is 1-0 at 20.8%. Goal-market probabilities: at least one goal: 85.7%; Over 2.5 goals: 28.9%; Under 3.5 goals: 88.3%; Double Chance 1X: 81.9%; Double Chance X2: 45.3%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 95.9%; BTTS Yes (both teams score): 31.8%; BTTS No (at least one team does not score): 68.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 54.7% | 1.83 |
| Draw | 27.2% | 3.67 |
| Getafe win | 18.1% | 5.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.21 |
| Getafe expected goals | 0.62 |
| Expected total goals | 1.83 |
| Over 0.5 | 85.7% |
| Under 0.5 | 14.3% |
| Over 1.5 | 55.5% |
| Under 1.5 | 44.5% |
| Over 2.5 | 28.9% |
| Under 2.5 | 71.1% |
| Over 3.5 | 11.7% |
| Under 3.5 | 88.3% |
| Over 4.5 | 4.1% |
| Under 4.5 | 95.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.84% |
| 2 | 0-0 | 14.31% |
| 3 | 2-0 | 12.80% |
| 4 | 1-1 | 10.77% |
| 5 | 0-1 | 9.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 54.7% | 59.0% | 1.70 | -7.0% |
| Draw | 27.2% | 23.5% | 3.94 | +7.3% |
| Getafe win | 18.1% | 17.5% | 5.80 | +4.9% |
| Over 2.5 | 28.9% | 42.4% | 2.28 | -34.0% |
| Under 2.5 | 71.1% | 57.6% | 1.73 | +22.9% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| P btts yes | 31.8% |
| P btts no | 68.2% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.99 |
| Fair Over 1.5 odds | 1.80 |
| Fair Under 1.5 odds | 2.25 |
| Fair Over 2.5 odds | 3.46 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.58 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.55 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 50.4% |
| Unadjusted draw probability | 31.0% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 54.9% |
| Raw p under 3 5 | 88.6% |
| Raw p btts yes | 32.6% |
| P home draw | 81.9% |
| P draw away | 45.3% |
| P home away | 72.8% |
| Raw p home draw | 81.4% |
| Raw p draw away | 49.6% |
| Raw p home away | 69.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.62 |
| Reference draw odds | 3.75 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.18 |
| Reference Under 2.5 odds | 1.65 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | -4.3% |
| Draw probability edge | +3.7% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -13.4% |
| Under 2.5 probability edge | +13.4% |
| Raw edge prob home | -0.0853 |
| Raw ev home | -0.1427 |
| Raw edge prob draw | 0.0744 |
| Raw ev draw | 0.2196 |
| Raw edge prob away | 0.0108 |
| Raw ev away | 0.0799 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **37.9%**. Expected goals are 1.44 for Celta Vigo and 1.30 for Real Betis (2.73 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 51.4%; Under 3.5 goals: 70.7%; Double Chance 1X: 64.2%; Double Chance X2: 62.1%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 85.8%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 37.9% | 2.64 |
| Draw | 26.3% | 3.80 |
| Real Betis win | 35.8% | 2.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.44 |
| Real Betis expected goals | 1.30 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
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
| 1 | 1-1 | 12.47% |
| 2 | 0-1 | 8.68% |
| 3 | 1-0 | 8.57% |
| 4 | 1-2 | 8.33% |
| 5 | 2-1 | 8.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 37.9% | 35.5% | 2.77 | +5.0% |
| Draw | 26.3% | 26.6% | 3.57 | -6.1% |
| Real Betis win | 35.8% | 37.9% | 2.67 | -4.4% |
| Over 2.5 | 51.4% | 53.2% | 1.91 | -1.9% |
| Under 2.5 | 48.6% | 46.8% | 2.03 | -1.3% |

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
| Market best home last update utc | 2026-10-15T15:31:30Z |
| Market best draw last update utc | 2026-10-15T15:31:30Z |
| Market best away last update utc | 2026-10-15T15:31:30Z |
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
| Fair Under 0.5 odds | 14.69 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.16 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.41 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.06 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 40.3% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 33.7% |
| Raw p over 1 5 | 76.0% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 55.6% |
| P home draw | 64.2% |
| P draw away | 62.1% |
| P home away | 73.7% |
| Raw p home draw | 66.3% |
| Raw p draw away | 59.7% |
| Raw p home away | 74.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:21Z |
| Market reference home last update utc | 2026-10-15T15:32:21Z |
| Market reference draw last update utc | 2026-10-15T15:32:21Z |
| Market reference away last update utc | 2026-10-15T15:32:21Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market best over 2 5 last update utc | 2026-10-15T15:31:30Z |
| Market best under 2 5 last update utc | 2026-10-15T15:31:30Z |
| Home probability edge | +2.4% |
| Draw probability edge | -0.3% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | 0.0474 |
| Raw ev home | 0.1156 |
| Raw edge prob draw | -0.0054 |
| Raw ev draw | -0.0705 |
| Raw edge prob away | -0.0420 |
| Raw ev away | -0.1005 |

</details>


---
