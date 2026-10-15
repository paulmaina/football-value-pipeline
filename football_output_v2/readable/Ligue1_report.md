# Ligue 1 — football model report

Fixtures in this report: **13**.

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
| Training sha256 | 5a01317f5065d02765373a5bcd5bbfff9a42a42f06910b25b9dbc0bda50c2129 |
| Optimizer objective | 1681.020 |
| Base scoring parameter | 0.195 |
| Home-advantage parameter | 0.201 |
| Dixon-Coles low-score adjustment | -0.043 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-11', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 13.00 |
| Additional event odds calls used before this league | 31.00 |
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

## 2026-10-16 — Le Mans FC vs Toulouse

The model's most likely 1X2 outcome is **Le Mans FC win** at **39.5%**. Expected goals are 1.86 for Le Mans FC and 1.48 for Toulouse (3.34 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 64.2%; Under 3.5 goals: 57.5%; Double Chance 1X: 64.4%; Double Chance X2: 60.5%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 76.0%; BTTS Yes (both teams score): 66.1%; BTTS No (at least one team does not score): 33.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 39.5% | 2.53 |
| Draw | 24.9% | 4.02 |
| Toulouse win | 35.6% | 2.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Mans FC expected goals | 1.86 |
| Toulouse expected goals | 1.48 |
| Expected total goals | 3.34 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 64.2% |
| Under 2.5 | 35.8% |
| Over 3.5 | 42.5% |
| Under 3.5 | 57.5% |
| Over 4.5 | 24.0% |
| Under 4.5 | 76.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.88% |
| 2 | 1-2 | 8.45% |
| 3 | 2-1 | 7.75% |
| 4 | 2-2 | 7.17% |
| 5 | 0-1 | 5.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 39.5% | 32.7% | 3.11 | +22.7% |
| Draw | 24.9% | 26.5% | 3.60 | -10.4% |
| Toulouse win | 35.6% | 40.8% | 2.40 | -14.5% |
| Over 2.5 | 64.2% | 56.3% | 1.76 | +12.9% |
| Under 2.5 | 35.8% | 43.7% | 2.23 | -20.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-16T18:45:00+00:00 |
| Fixture id | 66c168c030f3faad3983fcadc3060009 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Mans |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 66.1% |
| P btts no | 33.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.56 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.59 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.79 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.16 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 46.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 30.5% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.2% |
| Raw p btts yes | 65.6% |
| P home draw | 64.4% |
| P draw away | 60.5% |
| P home away | 75.1% |
| Raw p home draw | 69.5% |
| Raw p draw away | 53.8% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:44Z |
| Market reference home last update utc | 2026-10-15T15:32:44Z |
| Market reference draw last update utc | 2026-10-15T15:32:44Z |
| Market reference away last update utc | 2026-10-15T15:32:44Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | +6.7% |
| Draw probability edge | -1.6% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | +7.8% |
| Under 2.5 probability edge | -7.8% |
| Raw edge prob home | 0.1347 |
| Raw ev home | 0.4367 |
| Raw edge prob draw | -0.0315 |
| Raw ev draw | -0.1604 |
| Raw edge prob away | -0.1032 |
| Raw ev away | -0.2685 |
| Market p home draw | 59.4% |
| Market home draw odds | 1.64 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:02Z |
| Market reference home draw last update utc | 2026-10-15T15:32:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.4% |
| Market draw away odds | 1.42 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:02Z |
| Market reference draw away last update utc | 2026-10-15T15:32:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.1% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:02Z |
| Market reference home away last update utc | 2026-10-15T15:32:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.60 |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 80.5% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:30:35Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.95 |
| Market reference over 1 5 last update utc | 2026-10-15T15:32:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.1% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:30:35Z |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.9% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:02Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.48 |
| Market reference btts yes last update utc | 2026-10-15T15:32:42Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **53.6%**. Expected goals are 1.75 for Lille and 0.96 for Brest (2.72 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.2%; Double Chance 1X: 78.1%; Double Chance X2: 46.4%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 53.6% | 1.87 |
| Draw | 24.6% | 4.07 |
| Brest win | 21.9% | 4.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.75 |
| Brest expected goals | 0.96 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.7% |
| Under 1.5 | 24.3% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.70% |
| 2 | 1-0 | 10.72% |
| 3 | 2-0 | 9.81% |
| 4 | 2-1 | 9.44% |
| 5 | 0-0 | 7.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 53.6% | 51.6% | 1.93 | +3.4% |
| Draw | 24.6% | 24.7% | 3.98 | -2.3% |
| Brest win | 21.9% | 23.7% | 4.05 | -11.4% |
| Over 2.5 | 50.9% | 57.2% | 1.73 | -12.0% |
| Under 2.5 | 49.1% | 42.8% | 2.28 | +12.0% |

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
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
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
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.02 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.48 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.21 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 55.5% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 20.1% |
| Raw p over 1 5 | 75.9% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 51.6% |
| P home draw | 78.1% |
| P draw away | 46.4% |
| P home away | 75.4% |
| Raw p home draw | 79.9% |
| Raw p draw away | 44.5% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.95 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:44Z |
| Market reference home last update utc | 2026-10-15T15:32:44Z |
| Market reference draw last update utc | 2026-10-15T15:32:44Z |
| Market reference away last update utc | 2026-10-15T15:32:44Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | +2.0% |
| Draw probability edge | -0.1% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | 0.0391 |
| Raw ev home | 0.0715 |
| Raw edge prob draw | -0.0026 |
| Raw ev draw | -0.0277 |
| Raw edge prob away | -0.0365 |
| Raw ev away | -0.1878 |
| Market p home draw | 75.7% |
| Market home draw odds | 1.28 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:02Z |
| Market reference home draw last update utc | 2026-10-15T15:32:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.2% |
| Market draw away odds | 1.97 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:02Z |
| Market reference draw away last update utc | 2026-10-15T15:32:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.1% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:02Z |
| Market reference home away last update utc | 2026-10-15T15:32:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.26 |
| Market reference dc draw away odds | 1.94 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 81.1% |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-15T15:32:44Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.5% |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:44Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 59.2% |
| Market btts yes odds | 1.59 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:02Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.33 |
| Market reference btts yes last update utc | 2026-10-15T15:32:40Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **63.3%**. Expected goals are 1.22 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.7%; Under 3.5 goals: 56.8%; Double Chance 1X: 36.7%; Double Chance X2: 82.4%; Double Chance 12 (either team wins): 80.9%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 61.5%; BTTS No (at least one team does not score): 38.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.6% | 5.69 |
| Draw | 19.1% | 5.23 |
| Paris Saint Germain win | 63.3% | 1.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.22 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 65.7% |
| Under 2.5 | 34.3% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.76% |
| 2 | 0-2 | 8.79% |
| 3 | 1-1 | 8.54% |
| 4 | 0-1 | 7.92% |
| 5 | 1-3 | 7.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.6% | 13.9% | 6.73 | +18.4% |
| Draw | 19.1% | 16.7% | 5.50 | +5.2% |
| Paris Saint Germain win | 63.3% | 69.4% | 1.46 | -7.6% |

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
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
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
| Fair Under 0.5 odds | 28.26 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
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
| P home draw | 36.7% |
| P draw away | 82.4% |
| P home away | 80.9% |
| Raw p home draw | 42.8% |
| Raw p draw away | 78.7% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 6.40 |
| Reference draw odds | 5.40 |
| Reference away odds | 1.41 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:44Z |
| Market reference home last update utc | 2026-10-15T15:32:44Z |
| Market reference draw last update utc | 2026-10-15T15:32:44Z |
| Market reference away last update utc | 2026-10-15T15:32:44Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:05Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:05Z |
| Home probability edge | +3.7% |
| Draw probability edge | +2.5% |
| Away probability edge | -6.1% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.0735 |
| Raw ev home | 0.4309 |
| Raw edge prob draw | 0.0492 |
| Raw ev draw | 0.1871 |
| Raw edge prob away | -0.1226 |
| Raw ev away | -0.1656 |
| Market p home draw | 32.6% |
| Market home draw odds | 2.94 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:02Z |
| Market reference home draw last update utc | 2026-10-15T15:32:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 85.2% |
| Market draw away odds | 1.12 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:02Z |
| Market reference draw away last update utc | 2026-10-15T15:32:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.2% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:02Z |
| Market reference home away last update utc | 2026-10-15T15:32:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.93 |
| Market reference dc draw away odds | 1.12 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 90.4% |
| Market over 1 5 odds | 1.03 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:32:09Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-15T15:32:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 48.1% |
| Market under 3 5 odds | 2.06 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:32:09Z |
| Market reference under 3 5 odds | 1.90 |
| Market reference under 3 5 opposite odds | 1.78 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.0% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:02Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.61 |
| Market reference btts yes last update utc | 2026-10-15T15:32:42Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **62.9%**. Expected goals are 0.64 for Troyes and 2.21 for RC Lens (2.84 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 51.7%; Under 3.5 goals: 70.3%; Double Chance 1X: 37.1%; Double Chance X2: 83.7%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 43.8%; BTTS No (at least one team does not score): 56.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 16.3% | 6.15 |
| Draw | 20.9% | 4.79 |
| RC Lens win | 62.9% | 1.59 |

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
| 1 | 0-2 | 12.22% |
| 2 | 0-1 | 10.78% |
| 3 | 1-1 | 9.85% |
| 4 | 0-3 | 8.98% |
| 5 | 1-2 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 16.3% | 23.6% | 4.30 | -30.1% |
| Draw | 20.9% | 23.6% | 4.04 | -15.7% |
| RC Lens win | 62.9% | 52.7% | 1.87 | +17.6% |
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
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
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
| P btts yes | 43.8% |
| P btts no | 56.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.00 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.16 |
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
| P home draw | 37.1% |
| P draw away | 83.7% |
| P home away | 79.1% |
| Raw p home draw | 27.0% |
| Raw p draw away | 91.1% |
| Raw p home away | 81.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.95 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.84 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:44Z |
| Market reference home last update utc | 2026-10-15T15:32:44Z |
| Market reference draw last update utc | 2026-10-15T15:32:44Z |
| Market reference away last update utc | 2026-10-15T15:32:44Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | -7.4% |
| Draw probability edge | -2.8% |
| Away probability edge | +10.2% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | -0.1475 |
| Raw ev home | -0.6179 |
| Raw edge prob draw | -0.0556 |
| Raw ev draw | -0.2694 |
| Raw edge prob away | 0.2031 |
| Raw ev away | 0.3656 |
| Market p home draw | 48.3% |
| Market home draw odds | 2.04 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:02Z |
| Market reference home draw last update utc | 2026-10-15T15:32:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.9% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:02Z |
| Market reference draw away last update utc | 2026-10-15T15:32:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.9% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:02Z |
| Market reference home away last update utc | 2026-10-15T15:32:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.98 |
| Market reference dc draw away odds | 1.26 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:32:07Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-15T15:32:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.4% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:32:07Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.5% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:02Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.46 |
| Market reference btts yes last update utc | 2026-10-15T15:32:40Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **50.1%**. Expected goals are 0.95 for Angers and 1.71 for Marseille (2.66 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 49.2%; Under 3.5 goals: 72.8%; Double Chance 1X: 49.9%; Double Chance X2: 75.1%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 24.9% | 4.02 |
| Draw | 25.1% | 3.99 |
| Marseille win | 50.1% | 2.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.95 |
| Marseille expected goals | 1.71 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 74.4% |
| Under 1.5 | 25.6% |
| Over 2.5 | 49.2% |
| Under 2.5 | 50.8% |
| Over 3.5 | 27.2% |
| Under 3.5 | 72.8% |
| Over 4.5 | 12.8% |
| Under 4.5 | 87.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.95% |
| 2 | 0-1 | 10.50% |
| 3 | 0-2 | 9.37% |
| 4 | 1-2 | 8.86% |
| 5 | 0-0 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 24.9% | 29.5% | 3.37 | -16.2% |
| Draw | 25.1% | 25.3% | 3.79 | -4.9% |
| Marseille win | 50.1% | 45.2% | 2.20 | +10.1% |
| Over 2.5 | 49.2% | 60.0% | 1.67 | -17.8% |
| Under 2.5 | 50.8% | 40.0% | 2.40 | +21.9% |

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
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
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
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.19 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.90 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.68 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.78 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 54.9% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.4% |
| Raw p btts yes | 50.6% |
| P home draw | 49.9% |
| P draw away | 75.1% |
| P home away | 74.9% |
| Raw p home draw | 45.1% |
| Raw p draw away | 79.8% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.20 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.13 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:44Z |
| Market reference home last update utc | 2026-10-15T15:32:44Z |
| Market reference draw last update utc | 2026-10-15T15:32:44Z |
| Market reference away last update utc | 2026-10-15T15:32:44Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | -4.6% |
| Draw probability edge | -0.2% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -10.8% |
| Under 2.5 probability edge | +10.8% |
| Raw edge prob home | -0.0925 |
| Raw ev home | -0.3182 |
| Raw edge prob draw | -0.0045 |
| Raw ev draw | -0.0576 |
| Raw edge prob away | 0.0970 |
| Raw ev away | 0.2079 |
| Market p home draw | 55.3% |
| Market home draw odds | 1.75 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:02Z |
| Market reference home draw last update utc | 2026-10-15T15:32:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.4% |
| Market draw away odds | 1.37 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:02Z |
| Market reference draw away last update utc | 2026-10-15T15:32:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.3% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:02Z |
| Market reference home away last update utc | 2026-10-15T15:32:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.72 |
| Market reference dc draw away odds | 1.35 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:41Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-15T15:32:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:41Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.35 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.9% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:02Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.55 |
| Market reference btts yes last update utc | 2026-10-15T15:32:41Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **38.4%**. Expected goals are 1.17 for Le Havre and 1.17 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 41.7%; Under 3.5 goals: 79.1%; Double Chance 1X: 66.9%; Double Chance X2: 61.6%; Double Chance 12 (either team wins): 71.5%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 38.4% | 2.61 |
| Draw | 28.5% | 3.51 |
| Auxerre win | 33.1% | 3.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.17 |
| Auxerre expected goals | 1.17 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 68.5% |
| Under 1.5 | 31.5% |
| Over 2.5 | 41.7% |
| Under 2.5 | 58.3% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.40% |
| 2 | 1-0 | 11.57% |
| 3 | 0-1 | 10.03% |
| 4 | 0-0 | 9.93% |
| 5 | 2-1 | 8.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 38.4% | 41.2% | 2.42 | -7.1% |
| Draw | 28.5% | 27.7% | 3.51 | -0.1% |
| Auxerre win | 33.1% | 31.1% | 3.14 | +4.1% |
| Over 2.5 | 41.7% | 50.5% | 1.95 | -18.6% |
| Under 2.5 | 58.3% | 49.5% | 1.99 | +15.9% |

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
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
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
| Fair Under 0.5 odds | 10.07 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.40 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.78 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.20 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 35.6% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 68.4% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 48.2% |
| P home draw | 66.9% |
| P draw away | 61.6% |
| P home away | 71.5% |
| Raw p home draw | 64.8% |
| Raw p draw away | 64.4% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.33 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:44Z |
| Market reference home last update utc | 2026-10-15T15:32:44Z |
| Market reference draw last update utc | 2026-10-15T15:32:44Z |
| Market reference away last update utc | 2026-10-15T15:32:44Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | -2.8% |
| Draw probability edge | +0.7% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.0564 |
| Raw ev home | -0.1394 |
| Raw edge prob draw | 0.0149 |
| Raw ev draw | 0.0254 |
| Raw edge prob away | 0.0415 |
| Raw ev away | 0.1060 |
| Market p home draw | 68.9% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:02Z |
| Market reference home draw last update utc | 2026-10-15T15:32:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.1% |
| Market draw away odds | 1.63 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:02Z |
| Market reference draw away last update utc | 2026-10-15T15:32:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.0% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:02Z |
| Market reference home away last update utc | 2026-10-15T15:32:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.38 |
| Market reference dc draw away odds | 1.61 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 76.2% |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-10-15T15:32:44Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 71.7% |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:44Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.3% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:02Z |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.23 |
| Market reference btts yes last update utc | 2026-10-15T15:32:41Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **46.9%**. Expected goals are 1.37 for Lorient and 1.80 for AS Monaco (3.17 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.9%; Under 3.5 goals: 60.9%; Double Chance 1X: 53.1%; Double Chance X2: 72.5%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 78.8%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 27.5% | 3.64 |
| Draw | 25.6% | 3.91 |
| AS Monaco win | 46.9% | 2.13 |

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
| Over 2.5 | 60.9% |
| Under 2.5 | 39.1% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.2% |
| Under 4.5 | 78.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.56% |
| 2 | 1-2 | 9.26% |
| 3 | 0-1 | 7.04% |
| 4 | 2-2 | 6.85% |
| 5 | 2-1 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 27.5% | 26.1% | 3.87 | +6.4% |
| Draw | 25.6% | 27.3% | 3.58 | -8.4% |
| AS Monaco win | 46.9% | 46.6% | 2.10 | -1.5% |
| Over 2.5 | 60.9% | 49.2% | 1.97 | +20.0% |
| Under 2.5 | 39.1% | 50.8% | 1.97 | -23.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | 53f5fe7ed0ba0fbf6345c73270e4cd00 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
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
| Fair Under 0.5 odds | 20.15 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.71 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 28.9% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 47.2% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 62.8% |
| P home draw | 53.1% |
| P draw away | 72.5% |
| P home away | 74.4% |
| Raw p home draw | 52.8% |
| Raw p draw away | 71.1% |
| Raw p home away | 76.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.60 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.07 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:44Z |
| Market reference home last update utc | 2026-10-15T15:32:44Z |
| Market reference draw last update utc | 2026-10-15T15:32:44Z |
| Market reference away last update utc | 2026-10-15T15:32:44Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | +1.4% |
| Draw probability edge | -1.7% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +11.7% |
| Under 2.5 probability edge | -11.7% |
| Raw edge prob home | 0.0282 |
| Raw ev home | 0.1190 |
| Raw edge prob draw | -0.0341 |
| Raw ev draw | -0.1454 |
| Raw edge prob away | 0.0059 |
| Raw ev away | -0.0085 |
| Market p home draw | 53.9% |
| Market home draw odds | 1.82 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:02Z |
| Market reference home draw last update utc | 2026-10-15T15:32:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.6% |
| Market draw away odds | 1.30 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:02Z |
| Market reference draw away last update utc | 2026-10-15T15:32:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.5% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:02Z |
| Market reference home away last update utc | 2026-10-15T15:32:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.76 |
| Market reference dc draw away odds | 1.29 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 75.5% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T15:31:20Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.30 |
| Market reference over 1 5 last update utc | 2026-10-15T15:32:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.9% |
| Market under 3 5 odds | 1.30 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T15:31:20Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.05 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.0% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:02Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.08 |
| Market reference btts yes last update utc | 2026-10-15T15:32:40Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **55.2%**. Expected goals are 1.77 for Lyon and 1.09 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 54.8%; Under 3.5 goals: 67.7%; Double Chance 1X: 78.6%; Double Chance X2: 44.8%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 83.7%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 55.2% | 1.81 |
| Draw | 23.4% | 4.26 |
| Nice win | 21.4% | 4.68 |

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
| 1 | 1-1 | 11.10% |
| 2 | 2-1 | 10.20% |
| 3 | 1-0 | 10.10% |
| 4 | 2-0 | 9.39% |
| 5 | 3-1 | 6.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 55.2% | 57.5% | 1.71 | -5.6% |
| Draw | 23.4% | 22.6% | 4.21 | -1.3% |
| Nice win | 21.4% | 20.0% | 5.18 | +10.6% |
| Over 2.5 | 54.8% | 58.4% | 1.72 | -5.7% |
| Under 2.5 | 45.2% | 41.6% | 2.31 | +4.4% |

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
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
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
| Fair Under 0.5 odds | 16.69 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.65 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.10 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.12 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 52.9% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| P home draw | 78.6% |
| P draw away | 44.8% |
| P home away | 76.6% |
| Raw p home draw | 77.3% |
| Raw p draw away | 47.1% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.69 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:44Z |
| Market reference home last update utc | 2026-10-15T15:32:44Z |
| Market reference draw last update utc | 2026-10-15T15:32:44Z |
| Market reference away last update utc | 2026-10-15T15:32:44Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | -2.3% |
| Draw probability edge | +0.9% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | -0.0455 |
| Raw ev home | -0.0949 |
| Raw edge prob draw | 0.0179 |
| Raw ev draw | 0.0248 |
| Raw edge prob away | 0.0276 |
| Raw ev away | 0.1774 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **41.6%**. Expected goals are 1.57 for Paris FC and 1.37 for Rennes (2.94 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 56.1%; Under 3.5 goals: 66.1%; Double Chance 1X: 67.5%; Double Chance X2: 58.4%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 82.6%; BTTS Yes (both teams score): 59.7%; BTTS No (at least one team does not score): 40.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 41.6% | 2.41 |
| Draw | 26.0% | 3.85 |
| Rennes win | 32.5% | 3.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.57 |
| Rennes expected goals | 1.37 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 56.1% |
| Under 2.5 | 43.9% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.4% |
| Under 4.5 | 82.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.12% |
| 2 | 2-1 | 8.88% |
| 3 | 1-0 | 7.77% |
| 4 | 1-2 | 7.71% |
| 5 | 0-1 | 6.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 41.6% | 41.2% | 2.37 | -1.5% |
| Draw | 26.0% | 26.5% | 3.45 | -10.4% |
| Rennes win | 32.5% | 32.2% | 3.29 | +6.8% |
| Over 2.5 | 56.1% | 58.4% | 1.72 | -3.5% |
| Under 2.5 | 43.9% | 41.6% | 2.30 | +0.9% |

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
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
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
| P btts yes | 59.7% |
| P btts no | 40.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.93 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.75 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 41.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.1% |
| Raw p btts yes | 59.5% |
| P home draw | 67.5% |
| P draw away | 58.4% |
| P home away | 74.0% |
| Raw p home draw | 67.3% |
| Raw p draw away | 58.1% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.33 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:44Z |
| Market reference home last update utc | 2026-10-15T15:32:44Z |
| Market reference draw last update utc | 2026-10-15T15:32:44Z |
| Market reference away last update utc | 2026-10-15T15:32:44Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:44Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | +0.3% |
| Draw probability edge | -0.6% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | 0.0065 |
| Raw ev home | -0.0072 |
| Raw edge prob draw | -0.0112 |
| Raw ev draw | -0.1229 |
| Raw edge prob away | 0.0047 |
| Raw ev away | 0.0754 |
| Market p home draw | 67.6% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T15:32:02Z |
| Market reference home draw last update utc | 2026-10-15T15:32:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.2% |
| Market draw away odds | 1.66 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T15:32:02Z |
| Market reference draw away last update utc | 2026-10-15T15:32:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.3% |
| Market home away odds | 1.36 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T15:32:02Z |
| Market reference home away last update utc | 2026-10-15T15:32:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.41 |
| Market reference dc draw away odds | 1.61 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 82.0% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-15T15:32:44Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.8% |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.42 |
| Market reference under 3 5 last update utc | 2026-10-15T15:32:44Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 64.1% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T15:32:02Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.63 |
| Market reference btts yes last update utc | 2026-10-15T15:32:17Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **44.0%**. Expected goals are 1.56 for Brest and 1.28 for Nice (2.84 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.1%; Under 3.5 goals: 68.4%; Double Chance 1X: 69.3%; Double Chance X2: 56.0%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 84.1%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 44.0% | 2.28 |
| Draw | 25.3% | 3.95 |
| Nice win | 30.7% | 3.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Nice expected goals | 1.28 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 31.6% |
| Under 3.5 | 68.4% |
| Over 4.5 | 15.9% |
| Under 4.5 | 84.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.94% |
| 2 | 2-1 | 9.22% |
| 3 | 1-0 | 8.75% |
| 4 | 1-2 | 7.45% |
| 5 | 2-0 | 7.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 44.0% | 44.5% | 2.31 | +1.5% |
| Draw | 25.3% | 24.8% | 3.49 | -11.6% |
| Nice win | 30.7% | 30.7% | 3.37 | +3.6% |
| Over 2.5 | 54.1% | 56.2% | 1.76 | -4.8% |
| Under 2.5 | 45.9% | 43.8% | 2.23 | +2.4% |

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
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
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
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.01 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.55 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.16 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.30 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.5% |
| P home draw | 69.3% |
| P draw away | 56.0% |
| P home away | 74.7% |
| Raw p home draw | 69.2% |
| Raw p draw away | 56.6% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.75 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:42Z |
| Market reference home last update utc | 2026-10-15T15:32:42Z |
| Market reference draw last update utc | 2026-10-15T15:32:42Z |
| Market reference away last update utc | 2026-10-15T15:32:42Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:42Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:42Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | -0.6% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.0111 |
| Raw ev home | 0.0025 |
| Raw edge prob draw | 0.0103 |
| Raw ev draw | -0.0986 |
| Raw edge prob away | 0.0008 |
| Raw ev away | 0.0370 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **48.5%**. Expected goals are 1.59 for RC Lens and 1.00 for Paris FC (2.58 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.0%; Under 3.5 goals: 74.1%; Double Chance 1X: 73.5%; Double Chance X2: 51.5%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 48.5% | 2.06 |
| Draw | 25.0% | 4.00 |
| Paris FC win | 26.5% | 3.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.59 |
| Paris FC expected goals | 1.00 |
| Expected total goals | 2.58 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 73.3% |
| Under 1.5 | 26.7% |
| Over 2.5 | 48.0% |
| Under 2.5 | 52.0% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.91% |
| 2 | 1-0 | 10.99% |
| 3 | 2-0 | 9.10% |
| 4 | 2-1 | 9.09% |
| 5 | 0-1 | 7.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 48.5% | 46.4% | 2.09 | +1.3% |
| Draw | 25.0% | 23.8% | 3.90 | -2.5% |
| Paris FC win | 26.5% | 29.7% | 3.58 | -5.0% |
| Over 2.5 | 48.0% | 59.2% | 1.68 | -19.3% |
| Under 2.5 | 52.0% | 40.8% | 2.38 | +23.7% |

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
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
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
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.98 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.75 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.28 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 50.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.3% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.9% |
| Raw p btts yes | 50.7% |
| P home draw | 73.5% |
| P draw away | 51.5% |
| P home away | 75.0% |
| Raw p home draw | 76.7% |
| Raw p draw away | 49.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.94 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.85 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:42Z |
| Market reference home last update utc | 2026-10-15T15:32:42Z |
| Market reference draw last update utc | 2026-10-15T15:32:42Z |
| Market reference away last update utc | 2026-10-15T15:32:42Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:42Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:42Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | +2.0% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | 0.0408 |
| Raw ev home | 0.0555 |
| Raw edge prob draw | 0.0234 |
| Raw ev draw | 0.0209 |
| Raw edge prob away | -0.0642 |
| Raw ev away | -0.1651 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **66.2%**. Expected goals are 2.29 for Toulouse and 0.62 for Troyes (2.91 combined). The most likely exact score is 2-0 at 12.6%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.7%; Under 3.5 goals: 68.4%; Double Chance 1X: 85.6%; Double Chance X2: 33.8%; Double Chance 12 (either team wins): 80.6%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 43.4%; BTTS No (at least one team does not score): 56.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 66.2% | 1.51 |
| Draw | 19.4% | 5.16 |
| Troyes win | 14.4% | 6.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 2.29 |
| Troyes expected goals | 0.62 |
| Expected total goals | 2.91 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 53.7% |
| Under 2.5 | 46.3% |
| Over 3.5 | 31.6% |
| Under 3.5 | 68.4% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.60% |
| 2 | 1-0 | 10.71% |
| 3 | 3-0 | 9.62% |
| 4 | 1-1 | 9.16% |
| 5 | 2-1 | 7.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 66.2% | 57.7% | 1.75 | +15.9% |
| Draw | 19.4% | 21.6% | 4.21 | -18.5% |
| Troyes win | 14.4% | 20.7% | 4.88 | -29.7% |
| Over 2.5 | 53.7% | 58.9% | 1.69 | -9.2% |
| Under 2.5 | 46.3% | 41.1% | 2.36 | +9.2% |

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
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
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
| P btts yes | 43.4% |
| P btts no | 56.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.33 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.42 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.17 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.25 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 74.8% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 66.6% |
| Raw p btts yes | 42.1% |
| P home draw | 85.6% |
| P draw away | 33.8% |
| P home away | 80.6% |
| Raw p home draw | 91.9% |
| Raw p draw away | 25.2% |
| Raw p home away | 82.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.60 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:42Z |
| Market reference home last update utc | 2026-10-15T15:32:42Z |
| Market reference draw last update utc | 2026-10-15T15:32:42Z |
| Market reference away last update utc | 2026-10-15T15:32:42Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.29 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:42Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:42Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | +8.5% |
| Draw probability edge | -2.3% |
| Away probability edge | -6.3% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | 0.1706 |
| Raw ev home | 0.3083 |
| Raw edge prob draw | -0.0454 |
| Raw ev draw | -0.2801 |
| Raw edge prob away | -0.1252 |
| Raw ev away | -0.6028 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **44.2%**. Expected goals are 1.47 for AS Monaco and 1.26 for Lille (2.73 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 51.6%; Under 3.5 goals: 70.7%; Double Chance 1X: 70.0%; Double Chance X2: 55.8%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 55.5%; BTTS No (at least one team does not score): 44.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 44.2% | 2.26 |
| Draw | 25.8% | 3.88 |
| Lille win | 30.0% | 3.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.47 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 76.3% |
| Under 1.5 | 23.7% |
| Over 2.5 | 51.6% |
| Under 2.5 | 48.4% |
| Over 3.5 | 29.3% |
| Under 3.5 | 70.7% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.26% |
| 2 | 1-0 | 9.66% |
| 3 | 2-1 | 9.46% |
| 4 | 2-0 | 7.49% |
| 5 | 0-1 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 44.2% | 46.9% | 2.18 | -3.7% |
| Draw | 25.8% | 25.1% | 3.60 | -7.1% |
| Lille win | 30.0% | 28.0% | 3.60 | +8.1% |
| Over 2.5 | 51.6% | 55.9% | 1.77 | -8.6% |
| Under 2.5 | 48.4% | 44.1% | 2.22 | +7.3% |

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
| Market best home last update utc | 2026-10-15T15:32:02Z |
| Market best draw last update utc | 2026-10-15T15:32:02Z |
| Market best away last update utc | 2026-10-15T15:32:02Z |
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
| P btts yes | 55.5% |
| P btts no | 44.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.59 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.21 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.41 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.01 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 41.4% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 32.0% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.8% |
| Raw p btts yes | 55.7% |
| P home draw | 70.0% |
| P draw away | 55.8% |
| P home away | 74.2% |
| Raw p home draw | 68.0% |
| Raw p draw away | 58.6% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.92 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.00 |
| Market reference 1x2 last update utc | 2026-10-15T15:32:42Z |
| Market reference home last update utc | 2026-10-15T15:32:42Z |
| Market reference draw last update utc | 2026-10-15T15:32:42Z |
| Market reference away last update utc | 2026-10-15T15:32:42Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-15T15:32:42Z |
| Market reference under 2 5 last update utc | 2026-10-15T15:32:42Z |
| Market best over 2 5 last update utc | 2026-10-15T15:32:02Z |
| Market best under 2 5 last update utc | 2026-10-15T15:32:02Z |
| Home probability edge | -2.8% |
| Draw probability edge | +0.7% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.0554 |
| Raw ev home | -0.0973 |
| Raw edge prob draw | 0.0149 |
| Raw ev draw | -0.0442 |
| Raw edge prob away | 0.0406 |
| Raw ev away | 0.1536 |

</details>


---
