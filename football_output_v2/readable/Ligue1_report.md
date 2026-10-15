# Ligue 1 — football model report

Fixtures in this report: **12**.

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
| Live odds matched | 12.00 |
| Additional event odds calls used before this league | 21.00 |
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

## 2026-10-16 — Le Mans FC vs Toulouse

The model's most likely 1X2 outcome is **Le Mans FC win** at **38.9%**. Expected goals are 1.86 for Le Mans FC and 1.48 for Toulouse (3.34 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 64.1%; Under 3.5 goals: 57.5%; Double Chance 1X: 64.0%; Double Chance X2: 61.1%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 76.0%; BTTS Yes (both teams score): 66.2%; BTTS No (at least one team does not score): 33.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 38.9% | 2.57 |
| Draw | 25.1% | 3.98 |
| Toulouse win | 36.0% | 2.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Mans FC expected goals | 1.86 |
| Toulouse expected goals | 1.48 |
| Expected total goals | 3.34 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 64.1% |
| Under 2.5 | 35.9% |
| Over 3.5 | 42.5% |
| Under 3.5 | 57.5% |
| Over 4.5 | 24.0% |
| Under 4.5 | 76.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.97% |
| 2 | 1-2 | 8.53% |
| 3 | 2-1 | 7.64% |
| 4 | 2-2 | 7.23% |
| 5 | 0-1 | 5.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 38.9% | 31.7% | 3.12 | +21.5% |
| Draw | 25.1% | 26.9% | 3.61 | -9.3% |
| Toulouse win | 36.0% | 41.4% | 2.39 | -14.1% |
| Over 2.5 | 64.1% | 54.1% | 1.76 | +12.8% |
| Under 2.5 | 35.9% | 45.9% | 2.23 | -19.9% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Mans |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.2% |
| P btts no | 33.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.36 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.58 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.78 |
| Fair Over 3.5 odds | 2.36 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.17 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 46.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 30.5% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.2% |
| Raw p btts yes | 65.6% |
| P home draw | 64.0% |
| P draw away | 61.1% |
| P home away | 74.9% |
| Raw p home draw | 69.5% |
| Raw p draw away | 53.8% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 3.05 |
| Reference draw odds | 3.57 |
| Reference away odds | 2.35 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.06 |
| Home probability edge | +7.3% |
| Draw probability edge | -1.8% |
| Away probability edge | -5.5% |
| Over 2.5 probability edge | +10.0% |
| Under 2.5 probability edge | -10.0% |
| Raw edge prob home | 0.1454 |
| Raw ev home | 0.4413 |
| Raw edge prob draw | -0.0359 |
| Raw ev draw | -0.1580 |
| Raw edge prob away | -0.1095 |
| Raw ev away | -0.2715 |
| Market p home draw | 58.8% |
| Market home draw odds | 1.65 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:54:07Z |
| Market reference home draw last update utc | 2026-10-15T06:54:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.3% |
| Market draw away odds | 1.42 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:54:07Z |
| Market reference draw away last update utc | 2026-10-15T06:54:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.9% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:54:07Z |
| Market reference home away last update utc | 2026-10-15T06:54:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.65 |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 78.9% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.4% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.81 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.1% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:54:07Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.32 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **54.5%**. Expected goals are 1.75 for Lille and 0.96 for Brest (2.72 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 51.1%; Under 3.5 goals: 71.1%; Double Chance 1X: 78.7%; Double Chance X2: 45.5%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 54.5% | 1.83 |
| Draw | 24.2% | 4.14 |
| Brest win | 21.3% | 4.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.75 |
| Brest expected goals | 0.96 |
| Expected total goals | 2.72 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.52% |
| 2 | 1-0 | 10.91% |
| 3 | 2-0 | 9.99% |
| 4 | 2-1 | 9.61% |
| 5 | 0-0 | 7.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 54.5% | 53.5% | 1.86 | +1.4% |
| Draw | 24.2% | 23.9% | 4.04 | -2.4% |
| Brest win | 21.3% | 22.6% | 4.36 | -7.1% |
| Over 2.5 | 51.1% | 57.0% | 1.75 | -10.6% |
| Under 2.5 | 48.9% | 43.0% | 2.25 | +10.1% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
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
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.25 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.17 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 55.5% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 20.1% |
| Raw p over 1 5 | 75.9% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 51.6% |
| P home draw | 78.7% |
| P draw away | 45.5% |
| P home away | 75.8% |
| Raw p home draw | 79.9% |
| Raw p draw away | 44.5% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.83 |
| Reference draw odds | 3.99 |
| Reference away odds | 4.22 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | +1.0% |
| Draw probability edge | +0.3% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | 0.0199 |
| Raw ev home | 0.0326 |
| Raw edge prob draw | 0.0052 |
| Raw ev draw | -0.0131 |
| Raw edge prob away | -0.0251 |
| Raw ev away | -0.1256 |
| Market p home draw | 77.0% |
| Market home draw odds | 1.26 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:54:07Z |
| Market reference home draw last update utc | 2026-10-15T06:54:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.3% |
| Market draw away odds | 2.05 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:54:07Z |
| Market reference draw away last update utc | 2026-10-15T06:54:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:54:07Z |
| Market reference home away last update utc | 2026-10-15T06:54:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.26 |
| Market reference dc draw away odds | 2.05 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 78.9% |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.9% |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.78 |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.7% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:54:07Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.25 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **63.0%**. Expected goals are 1.22 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.7%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 65.6%; Under 3.5 goals: 56.9%; Double Chance 1X: 37.0%; Double Chance X2: 82.2%; Double Chance 12 (either team wins): 80.8%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 61.5%; BTTS No (at least one team does not score): 38.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 17.8% | 5.61 |
| Draw | 19.2% | 5.22 |
| Paris Saint Germain win | 63.0% | 1.59 |

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
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.71% |
| 2 | 0-2 | 8.75% |
| 3 | 1-1 | 8.56% |
| 4 | 0-1 | 7.89% |
| 5 | 1-3 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 17.8% | 14.4% | 6.73 | +20.0% |
| Draw | 19.2% | 16.7% | 5.50 | +5.4% |
| Paris Saint Germain win | 63.0% | 68.8% | 1.46 | -8.0% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Strasbourg |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.5% |
| P btts no | 38.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.20 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.02 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 57.2% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.4% |
| P home draw | 37.0% |
| P draw away | 82.2% |
| P home away | 80.8% |
| Raw p home draw | 42.8% |
| Raw p draw away | 78.7% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 6.40 |
| Reference draw odds | 5.54 |
| Reference away odds | 1.43 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.42 |
| Home probability edge | +3.4% |
| Draw probability edge | +2.4% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -8.2% |
| Under 2.5 probability edge | +8.2% |
| Raw edge prob home | 0.0686 |
| Raw ev home | 0.4309 |
| Raw edge prob draw | 0.0484 |
| Raw ev draw | 0.1872 |
| Raw edge prob away | -0.1169 |
| Raw ev away | -0.1656 |
| Market p home draw | 32.8% |
| Market home draw odds | 2.94 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:54:07Z |
| Market reference home draw last update utc | 2026-10-15T06:54:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 86.1% |
| Market draw away odds | 1.12 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:54:07Z |
| Market reference draw away last update utc | 2026-10-15T06:54:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.1% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:54:07Z |
| Market reference home away last update utc | 2026-10-15T06:54:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.94 |
| Market reference dc draw away odds | 1.12 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 89.6% |
| Market over 1 5 odds | 1.03 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.10 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 47.5% |
| Market under 3 5 odds | 2.06 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:32Z |
| Market reference under 3 5 odds | 2.00 |
| Market reference under 3 5 opposite odds | 1.82 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.8% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:54:07Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 2.59 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **63.1%**. Expected goals are 0.64 for Troyes and 2.21 for RC Lens (2.84 combined). The most likely exact score is 0-2 at 12.3%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 51.8%; Under 3.5 goals: 70.2%; Double Chance 1X: 36.9%; Double Chance X2: 83.9%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 43.7%; BTTS No (at least one team does not score): 56.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 16.1% | 6.21 |
| Draw | 20.8% | 4.81 |
| RC Lens win | 63.1% | 1.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.64 |
| RC Lens expected goals | 2.21 |
| Expected total goals | 2.84 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 51.8% |
| Under 2.5 | 48.2% |
| Over 3.5 | 29.8% |
| Under 3.5 | 70.2% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.27% |
| 2 | 0-1 | 10.82% |
| 3 | 1-1 | 9.81% |
| 4 | 0-3 | 9.02% |
| 5 | 1-2 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 16.1% | 23.3% | 4.30 | -30.8% |
| Draw | 20.8% | 23.5% | 4.04 | -16.0% |
| RC Lens win | 63.1% | 53.2% | 1.87 | +18.0% |
| Over 2.5 | 51.8% | 61.2% | 1.64 | -15.1% |
| Under 2.5 | 48.2% | 38.8% | 2.46 | +18.7% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 43.7% |
| P btts no | 56.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.05 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.16 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.36 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.79 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 8.9% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 73.0% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 42.2% |
| P home draw | 36.9% |
| P draw away | 83.9% |
| P home away | 79.2% |
| Raw p home draw | 27.0% |
| Raw p draw away | 91.1% |
| Raw p home away | 81.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 4.08 |
| Reference draw odds | 4.05 |
| Reference away odds | 1.84 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.41 |
| Home probability edge | -7.2% |
| Draw probability edge | -2.7% |
| Away probability edge | +9.9% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.1443 |
| Raw ev home | -0.6179 |
| Raw edge prob draw | -0.0541 |
| Raw ev draw | -0.2694 |
| Raw edge prob away | 0.1984 |
| Raw ev away | 0.3656 |
| Market p home draw | 47.5% |
| Market home draw odds | 2.04 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-15T06:54:07Z |
| Market reference home draw last update utc | 2026-10-15T06:54:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 76.9% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-15T06:54:07Z |
| Market reference draw away last update utc | 2026-10-15T06:54:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.7% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-15T06:54:07Z |
| Market reference home away last update utc | 2026-10-15T06:54:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.04 |
| Market reference dc draw away odds | 1.26 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 82.5% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-15T06:53:34Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.9% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-15T06:53:34Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.45 |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.0% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-15T06:54:07Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.37 |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **50.9%**. Expected goals are 0.95 for Angers and 1.71 for Marseille (2.66 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.7%; Double Chance 1X: 49.1%; Double Chance X2: 75.8%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 24.2% | 4.13 |
| Draw | 24.9% | 4.02 |
| Marseille win | 50.9% | 1.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.95 |
| Marseille expected goals | 1.71 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
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
| 1 | 1-1 | 11.84% |
| 2 | 0-1 | 10.68% |
| 3 | 0-2 | 9.53% |
| 4 | 1-2 | 9.01% |
| 5 | 0-0 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 24.2% | 28.2% | 3.37 | -18.3% |
| Draw | 24.9% | 24.8% | 3.79 | -5.8% |
| Marseille win | 50.9% | 46.9% | 2.20 | +12.0% |
| Over 2.5 | 49.3% | 61.1% | 1.67 | -17.6% |
| Under 2.5 | 50.7% | 38.9% | 2.40 | +21.6% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
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
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.32 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.91 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.67 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.75 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 54.9% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.4% |
| Raw p btts yes | 50.6% |
| P home draw | 49.1% |
| P draw away | 75.8% |
| P home away | 75.1% |
| Raw p home draw | 45.1% |
| Raw p draw away | 79.8% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 3.40 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.08 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | -4.0% |
| Draw probability edge | +0.0% |
| Away probability edge | +4.0% |
| Over 2.5 probability edge | -11.8% |
| Under 2.5 probability edge | +11.8% |
| Raw edge prob home | -0.0801 |
| Raw ev home | -0.3182 |
| Raw edge prob draw | 0.0003 |
| Raw ev draw | -0.0576 |
| Raw edge prob away | 0.0798 |
| Raw ev away | 0.2079 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **38.3%**. Expected goals are 1.17 for Le Havre and 1.17 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.7%; Under 3.5 goals: 79.1%; Double Chance 1X: 66.9%; Double Chance X2: 61.7%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 48.0%; BTTS No (at least one team does not score): 52.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 38.3% | 2.61 |
| Draw | 28.6% | 3.50 |
| Auxerre win | 33.1% | 3.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.17 |
| Auxerre expected goals | 1.17 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
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
| 1 | 1-1 | 13.46% |
| 2 | 1-0 | 11.55% |
| 3 | 0-1 | 10.02% |
| 4 | 0-0 | 9.97% |
| 5 | 2-1 | 8.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 38.3% | 41.0% | 2.42 | -7.3% |
| Draw | 28.6% | 27.9% | 3.51 | +0.3% |
| Auxerre win | 33.1% | 31.0% | 3.14 | +4.0% |
| Over 2.5 | 41.7% | 50.7% | 1.95 | -18.7% |
| Under 2.5 | 58.3% | 49.3% | 1.99 | +16.0% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
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
| P btts yes | 48.0% |
| P btts no | 52.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.03 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.40 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.78 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.21 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 35.6% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 68.4% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 48.2% |
| P home draw | 66.9% |
| P draw away | 61.7% |
| P home away | 71.4% |
| Raw p home draw | 64.8% |
| Raw p draw away | 64.4% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.37 |
| Reference draw odds | 3.44 |
| Reference away odds | 3.11 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.93 |
| Home probability edge | -2.7% |
| Draw probability edge | +0.6% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.0548 |
| Raw ev home | -0.1394 |
| Raw edge prob draw | 0.0127 |
| Raw ev draw | 0.0254 |
| Raw edge prob away | 0.0421 |
| Raw ev away | 0.1060 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **47.2%**. Expected goals are 1.37 for Lorient and 1.80 for AS Monaco (3.17 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 60.7%; Under 3.5 goals: 60.9%; Double Chance 1X: 52.8%; Double Chance X2: 73.3%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 78.9%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 26.7% | 3.75 |
| Draw | 26.1% | 3.83 |
| AS Monaco win | 47.2% | 2.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.37 |
| AS Monaco expected goals | 1.80 |
| Expected total goals | 3.17 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 60.7% |
| Under 2.5 | 39.3% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.1% |
| Under 4.5 | 78.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.81% |
| 2 | 1-2 | 9.31% |
| 3 | 0-1 | 7.08% |
| 4 | 2-2 | 7.00% |
| 5 | 0-2 | 6.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 26.7% | 24.5% | 3.87 | +3.3% |
| Draw | 26.1% | 28.4% | 3.58 | -6.5% |
| AS Monaco win | 47.2% | 47.1% | 2.10 | -0.9% |
| Over 2.5 | 60.7% | 49.3% | 1.97 | +19.6% |
| Under 2.5 | 39.3% | 50.7% | 1.97 | -22.6% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
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
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.73 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.73 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 28.9% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 47.2% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 62.8% |
| P home draw | 52.8% |
| P draw away | 73.3% |
| P home away | 73.9% |
| Raw p home draw | 52.8% |
| Raw p draw away | 71.1% |
| Raw p home away | 76.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 3.90 |
| Reference draw odds | 3.38 |
| Reference away odds | 2.07 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +2.2% |
| Draw probability edge | -2.3% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | +11.4% |
| Under 2.5 probability edge | -11.4% |
| Raw edge prob home | 0.0443 |
| Raw ev home | 0.1190 |
| Raw edge prob draw | -0.0451 |
| Raw ev draw | -0.1454 |
| Raw edge prob away | 0.0008 |
| Raw ev away | -0.0085 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **55.5%**. Expected goals are 1.77 for Lyon and 1.09 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 54.9%; Under 3.5 goals: 67.7%; Double Chance 1X: 78.8%; Double Chance X2: 44.5%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 83.7%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 55.5% | 1.80 |
| Draw | 23.4% | 4.28 |
| Nice win | 21.2% | 4.73 |

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
| Over 2.5 | 54.9% |
| Under 2.5 | 45.1% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.3% |
| Under 4.5 | 83.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.07% |
| 2 | 2-1 | 10.25% |
| 3 | 1-0 | 10.15% |
| 4 | 2-0 | 9.43% |
| 5 | 3-1 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 55.5% | 58.0% | 1.71 | -5.2% |
| Draw | 23.4% | 22.4% | 4.21 | -1.5% |
| Nice win | 21.2% | 19.6% | 5.18 | +9.6% |
| Over 2.5 | 54.9% | 56.4% | 1.72 | -5.7% |
| Under 2.5 | 45.1% | 43.6% | 2.31 | +4.3% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
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
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.74 |
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
| P home draw | 78.8% |
| P draw away | 44.5% |
| P home away | 76.6% |
| Raw p home draw | 77.3% |
| Raw p draw away | 47.1% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.69 |
| Reference draw odds | 4.22 |
| Reference away odds | 4.81 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -2.5% |
| Draw probability edge | +1.0% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | -0.0507 |
| Raw ev home | -0.0949 |
| Raw edge prob draw | 0.0192 |
| Raw ev draw | 0.0248 |
| Raw edge prob away | 0.0315 |
| Raw ev away | 0.1774 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **41.7%**. Expected goals are 1.57 for Paris FC and 1.37 for Rennes (2.94 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 55.6%; Under 3.5 goals: 66.1%; Double Chance 1X: 69.1%; Double Chance X2: 58.3%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 60.0%; BTTS No (at least one team does not score): 40.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 41.7% | 2.40 |
| Draw | 27.4% | 3.65 |
| Rennes win | 30.9% | 3.24 |

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
| Over 2.5 | 55.6% |
| Under 2.5 | 44.4% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.79% |
| 2 | 2-1 | 8.91% |
| 3 | 1-0 | 7.80% |
| 4 | 1-2 | 7.33% |
| 5 | 2-2 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 41.7% | 41.6% | 2.37 | -1.1% |
| Draw | 27.4% | 29.4% | 3.45 | -5.4% |
| Rennes win | 30.9% | 29.0% | 3.29 | +1.5% |
| Over 2.5 | 55.6% | 58.0% | 1.72 | -4.3% |
| Under 2.5 | 44.4% | 42.0% | 2.30 | +2.0% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
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
| P btts yes | 60.0% |
| P btts no | 40.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.04 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.82 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 41.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.1% |
| Raw p btts yes | 59.5% |
| P home draw | 69.1% |
| P draw away | 58.3% |
| P home away | 72.6% |
| Raw p home draw | 67.3% |
| Raw p draw away | 58.1% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.34 |
| Reference draw odds | 3.27 |
| Reference away odds | 3.31 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +0.2% |
| Draw probability edge | -2.0% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | 0.0034 |
| Raw ev home | -0.0072 |
| Raw edge prob draw | -0.0398 |
| Raw ev draw | -0.1229 |
| Raw edge prob away | 0.0365 |
| Raw ev away | 0.0754 |

</details>


---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **43.7%**. Expected goals are 1.56 for Brest and 1.28 for Nice (2.84 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 54.0%; Under 3.5 goals: 68.4%; Double Chance 1X: 69.2%; Double Chance X2: 56.3%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 84.1%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 43.7% | 2.29 |
| Draw | 25.4% | 3.93 |
| Nice win | 30.8% | 3.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Nice expected goals | 1.28 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 54.0% |
| Under 2.5 | 46.0% |
| Over 3.5 | 31.6% |
| Under 3.5 | 68.4% |
| Over 4.5 | 15.9% |
| Under 4.5 | 84.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.01% |
| 2 | 2-1 | 9.17% |
| 3 | 1-0 | 8.70% |
| 4 | 1-2 | 7.47% |
| 5 | 2-0 | 7.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 43.7% | 44.1% | 2.31 | +1.0% |
| Draw | 25.4% | 25.1% | 3.49 | -11.2% |
| Nice win | 30.8% | 30.9% | 3.37 | +3.8% |
| Over 2.5 | 54.0% | 57.4% | 1.76 | -4.9% |
| Under 2.5 | 46.0% | 42.6% | 2.23 | +2.5% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
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
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.93 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.55 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.16 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.31 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.5% |
| P home draw | 69.2% |
| P draw away | 56.3% |
| P home away | 74.6% |
| Raw p home draw | 69.2% |
| Raw p draw away | 56.6% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | -0.3% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | -0.0067 |
| Raw ev home | 0.0025 |
| Raw edge prob draw | 0.0076 |
| Raw ev draw | -0.0986 |
| Raw edge prob away | -0.0009 |
| Raw ev away | 0.0370 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **48.6%**. Expected goals are 1.59 for RC Lens and 1.00 for Paris FC (2.58 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.1%; Under 3.5 goals: 74.1%; Double Chance 1X: 73.6%; Double Chance X2: 51.4%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 50.5%; BTTS No (at least one team does not score): 49.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 48.6% | 2.06 |
| Draw | 25.0% | 4.00 |
| Paris FC win | 26.4% | 3.79 |

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
| Over 2.5 | 48.1% |
| Under 2.5 | 51.9% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.90% |
| 2 | 1-0 | 11.02% |
| 3 | 2-0 | 9.13% |
| 4 | 2-1 | 9.12% |
| 5 | 0-1 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 48.6% | 46.8% | 2.09 | +1.6% |
| Draw | 25.0% | 23.8% | 3.90 | -2.5% |
| Paris FC win | 26.4% | 29.4% | 3.58 | -5.6% |
| Over 2.5 | 48.1% | 60.7% | 1.68 | -19.3% |
| Under 2.5 | 51.9% | 39.3% | 2.38 | +23.6% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
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
| P btts yes | 50.5% |
| P btts no | 49.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.99 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.75 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.27 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 50.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.3% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.9% |
| Raw p btts yes | 50.7% |
| P home draw | 73.6% |
| P draw away | 51.4% |
| P home away | 75.0% |
| Raw p home draw | 76.7% |
| Raw p draw away | 49.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | +1.9% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -12.6% |
| Under 2.5 probability edge | +12.6% |
| Raw edge prob home | 0.0375 |
| Raw ev home | 0.0555 |
| Raw edge prob draw | 0.0237 |
| Raw ev draw | 0.0209 |
| Raw edge prob away | -0.0611 |
| Raw ev away | -0.1651 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **66.0%**. Expected goals are 2.29 for Toulouse and 0.62 for Troyes (2.91 combined). The most likely exact score is 2-0 at 12.6%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.7%; Under 3.5 goals: 68.5%; Double Chance 1X: 85.4%; Double Chance X2: 34.0%; Double Chance 12 (either team wins): 80.6%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 43.4%; BTTS No (at least one team does not score): 56.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 66.0% | 1.52 |
| Draw | 19.4% | 5.16 |
| Troyes win | 14.6% | 6.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 2.29 |
| Troyes expected goals | 0.62 |
| Expected total goals | 2.91 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 53.7% |
| Under 2.5 | 46.3% |
| Over 3.5 | 31.5% |
| Under 3.5 | 68.5% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.55% |
| 2 | 1-0 | 10.66% |
| 3 | 3-0 | 9.58% |
| 4 | 1-1 | 9.17% |
| 5 | 2-1 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 66.0% | 57.2% | 1.75 | +15.5% |
| Draw | 19.4% | 21.7% | 4.21 | -18.3% |
| Troyes win | 14.6% | 21.1% | 4.88 | -28.6% |
| Over 2.5 | 53.7% | 59.6% | 1.69 | -9.2% |
| Under 2.5 | 46.3% | 40.4% | 2.36 | +9.3% |

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
| Market best home last update utc | 2026-10-15T06:54:07Z |
| Market best draw last update utc | 2026-10-15T06:54:07Z |
| Market best away last update utc | 2026-10-15T06:54:07Z |
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
| P btts yes | 43.4% |
| P btts no | 56.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.31 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.17 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.27 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 74.8% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 66.6% |
| Raw p btts yes | 42.1% |
| P home draw | 85.4% |
| P draw away | 34.0% |
| P home away | 80.6% |
| Raw p home draw | 91.9% |
| Raw p draw away | 25.2% |
| Raw p home away | 82.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.66 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +8.8% |
| Draw probability edge | -2.3% |
| Away probability edge | -6.5% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | 0.1757 |
| Raw ev home | 0.3083 |
| Raw edge prob draw | -0.0459 |
| Raw ev draw | -0.2801 |
| Raw edge prob away | -0.1297 |
| Raw ev away | -0.6028 |

</details>


---
