# La Liga — football model report

Fixtures in this report: **12**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,209 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 2013.044 |
| Base scoring parameter | 0.081 |
| Home-advantage parameter | 0.279 |
| Dixon-Coles low-score adjustment | -0.014 |
| Xi per day | 0.0009 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 12.00 |
| Additional event odds calls used before this league | 1.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 1.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-12 — Levante vs Sevilla

The model's most likely 1X2 outcome is **Levante win** at **40.3%**. Expected goals are 1.61 for Levante and 1.27 for Sevilla (2.88 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 54.0%; Under 3.5 goals: 67.7%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 40.3% | 2.48 |
| Draw | 27.2% | 3.67 |
| Sevilla win | 32.5% | 3.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.61 |
| Sevilla expected goals | 1.27 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.0% |
| Under 2.5 | 46.0% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.77% |
| 2 | 2-1 | 8.22% |
| 3 | 1-2 | 7.91% |
| 4 | 1-0 | 7.90% |
| 5 | 0-1 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 40.3% | 35.2% | 2.84 | +14.4% |
| Draw | 27.2% | 29.6% | 3.35 | -8.8% |
| Sevilla win | 32.5% | 35.2% | 2.86 | -7.0% |
| Over 2.5 | 54.0% | 42.4% | 2.30 | +24.3% |
| Under 2.5 | 46.0% | 57.6% | 1.76 | -19.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-12T19:00:00+00:00 |
| Fixture id | 529fc26c7774d5b469932e275c668921 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T16:30:40Z |
| Market best draw last update utc | 2026-10-12T16:29:58Z |
| Market best away last update utc | 2026-10-12T16:30:40Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Unibet (SE) |
| Matched home-team name | Levante |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.77 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.59 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.21 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 45.4% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 29.9% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 57.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.68 |
| Reference draw odds | 3.15 |
| Reference away odds | 2.68 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.18 |
| Reference Under 2.5 odds | 1.65 |
| Home probability edge | +5.1% |
| Draw probability edge | -2.4% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | +11.6% |
| Under 2.5 probability edge | -11.6% |
| Raw edge prob home | 0.1018 |
| Raw ev home | 0.2882 |
| Raw edge prob draw | -0.0486 |
| Raw ev draw | -0.1698 |
| Raw edge prob away | -0.0532 |
| Raw ev away | -0.1460 |
| Market p over 1 5 | 69.1% |
| Market over 1 5 odds | 1.42 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-12T16:30:41Z |
| Market reference over 1 5 odds | 1.42 |
| Market reference over 1 5 opposite odds | 3.05 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 78.3% |
| Market under 3 5 odds | 1.26 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-12T16:30:41Z |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 4.25 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 52.3% |
| Market btts yes odds | 1.90 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-12T16:30:39Z |
| Market reference btts yes odds | 1.90 |
| Market reference btts yes opposite odds | 2.08 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-16 — Deportivo La Coruña vs Levante

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **50.2%**. Expected goals are 1.84 for Deportivo La Coruña and 1.11 for Levante (2.95 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 55.7%; Under 3.5 goals: 66.1%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 50.2% | 1.99 |
| Draw | 25.2% | 3.96 |
| Levante win | 24.6% | 4.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 1.84 |
| Levante expected goals | 1.11 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.7% |
| Under 2.5 | 44.3% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.84% |
| 2 | 2-1 | 9.09% |
| 3 | 1-0 | 8.75% |
| 4 | 2-0 | 8.19% |
| 5 | 1-2 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 50.2% | 46.1% | 2.17 | +9.0% |
| Draw | 25.2% | 27.4% | 3.62 | -8.7% |
| Levante win | 24.6% | 26.6% | 3.75 | -7.9% |
| Over 2.5 | 55.7% | 50.7% | 1.98 | +10.3% |
| Under 2.5 | 44.3% | 49.3% | 1.98 | -12.3% |

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
| Market best home last update utc | 2026-10-12T16:29:42Z |
| Market best draw last update utc | 2026-10-12T16:29:42Z |
| Market best away last update utc | 2026-10-12T16:30:40Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | La Coruna |
| Matched away-team name | Levante |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.02 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.80 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.4% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 79.5% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.08 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.90 |
| Home probability edge | +4.2% |
| Draw probability edge | -2.2% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +5.0% |
| Under 2.5 probability edge | -5.0% |
| Raw edge prob home | 0.0832 |
| Raw ev home | 0.1801 |
| Raw edge prob draw | -0.0432 |
| Raw ev draw | -0.1650 |
| Raw edge prob away | -0.0400 |
| Raw ev away | -0.1543 |

</details>


---

## 2026-10-17 — Espanyol vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **51.8%**. Expected goals are 1.03 for Espanyol and 1.58 for Atlético Madrid (2.60 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.4%; Under 3.5 goals: 73.4%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 22.9% | 4.38 |
| Draw | 25.4% | 3.94 |
| Atlético Madrid win | 51.8% | 1.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.03 |
| Atlético Madrid expected goals | 1.58 |
| Expected total goals | 2.60 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.4% |
| Under 2.5 | 51.6% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.08% |
| 2 | 0-1 | 11.90% |
| 3 | 1-2 | 9.79% |
| 4 | 0-2 | 9.53% |
| 5 | 0-0 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 22.9% | 21.2% | 4.60 | +5.1% |
| Draw | 25.4% | 25.3% | 3.90 | -1.0% |
| Atlético Madrid win | 51.8% | 53.5% | 1.91 | -1.1% |
| Over 2.5 | 48.4% | 53.9% | 1.87 | -9.5% |
| Under 2.5 | 51.6% | 46.1% | 2.09 | +7.8% |

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
| Market best home last update utc | 2026-10-12T16:30:11Z |
| Market best draw last update utc | 2026-10-12T16:29:58Z |
| Market best away last update utc | 2026-10-12T16:29:42Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Coolbet |
| Matched home-team name | Espanol |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 93/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.30 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.07 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 50.0% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.5% |
| Raw p btts yes | 51.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 4.30 |
| Reference draw odds | 3.65 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.02 |
| Home probability edge | +1.6% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | 0.0329 |
| Raw ev home | 0.1270 |
| Raw edge prob draw | 0.0027 |
| Raw ev draw | -0.0045 |
| Raw edge prob away | -0.0356 |
| Raw ev away | -0.0455 |

</details>


---

## 2026-10-17 — Real Betis vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **61.6%**. Expected goals are 1.32 for Real Betis and 2.05 for Barcelona (3.37 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 66.7%; Under 3.5 goals: 55.8%; Under 4.5 goals: 74.1%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 19.7% | 5.09 |
| Draw | 18.7% | 5.34 |
| Barcelona win | 61.6% | 1.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 1.32 |
| Barcelona expected goals | 2.05 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 66.7% |
| Under 2.5 | 33.3% |
| Over 3.5 | 44.2% |
| Under 3.5 | 55.8% |
| Over 4.5 | 25.9% |
| Under 4.5 | 74.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.87% |
| 2 | 0-2 | 8.20% |
| 3 | 1-1 | 8.20% |
| 4 | 0-1 | 7.86% |
| 5 | 1-3 | 7.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 19.7% | 14.9% | 6.40 | +25.8% |
| Draw | 18.7% | 15.9% | 6.00 | +12.5% |
| Barcelona win | 61.6% | 69.2% | 1.49 | -8.2% |
| Over 2.5 | 66.7% | 77.9% | 1.26 | -16.0% |
| Under 2.5 | 33.3% | 22.1% | 3.92 | +30.7% |

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
| Market best home last update utc | 2026-10-12T16:30:40Z |
| Market best draw last update utc | 2026-10-12T16:30:40Z |
| Market best away last update utc | 2026-10-12T16:29:42Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Betis |
| Matched away-team name | Barcelona |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.32 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.89 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 3.00 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.87 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 54.0% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 64.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 5.90 |
| Reference draw odds | 5.55 |
| Reference away odds | 1.41 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.85 |
| Home probability edge | +4.8% |
| Draw probability edge | +2.8% |
| Away probability edge | -7.6% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | 0.0951 |
| Raw ev home | 0.5627 |
| Raw edge prob draw | 0.0566 |
| Raw ev draw | 0.2943 |
| Raw edge prob away | -0.1517 |
| Raw ev away | -0.1952 |

</details>


---

## 2026-10-17 — Valencia vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **42.0%**. Expected goals are 1.08 for Valencia and 1.17 for Athletic Bilbao (2.25 combined). The most likely exact score is 0-1 at 13.5%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 39.2%; Under 3.5 goals: 81.0%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 45.5%; BTTS No (at least one team does not score): 54.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.5% | 3.39 |
| Draw | 28.5% | 3.51 |
| Athletic Bilbao win | 42.0% | 2.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.08 |
| Athletic Bilbao expected goals | 1.17 |
| Expected total goals | 2.25 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.2% |
| Under 2.5 | 60.8% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.55% |
| 2 | 1-1 | 13.24% |
| 3 | 0-0 | 10.55% |
| 4 | 1-0 | 9.98% |
| 5 | 1-2 | 8.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 29.5% | 25.9% | 3.70 | +9.1% |
| Draw | 28.5% | 27.9% | 3.58 | +2.1% |
| Athletic Bilbao win | 42.0% | 46.2% | 2.18 | -8.5% |
| Over 2.5 | 39.2% | 45.2% | 2.10 | -17.7% |
| Under 2.5 | 60.8% | 54.8% | 1.86 | +13.1% |

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
| Market best home last update utc | 2026-10-12T16:30:40Z |
| Market best draw last update utc | 2026-10-12T16:29:42Z |
| Market best away last update utc | 2026-10-12T16:29:42Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
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
| Fair Under 0.5 odds | 9.47 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.79 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 29.1% |
| Unadjusted away-win probability | 37.8% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 45.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 3.60 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.08 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.72 |
| Home probability edge | +3.6% |
| Draw probability edge | +0.6% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | 0.0720 |
| Raw ev home | 0.2243 |
| Raw edge prob draw | 0.0118 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | -0.0838 |
| Raw ev away | -0.1760 |

</details>


---

## 2026-10-17 — Villarreal vs Elche CF

The model's most likely 1X2 outcome is **Villarreal win** at **65.3%**. Expected goals are 2.51 for Villarreal and 1.25 for Elche CF (3.76 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 72.3%; Under 3.5 goals: 48.0%; Under 4.5 goals: 67.6%; BTTS Yes (both teams score): 65.9%; BTTS No (at least one team does not score): 34.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 65.3% | 1.53 |
| Draw | 18.9% | 5.28 |
| Elche CF win | 15.7% | 6.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.51 |
| Elche CF expected goals | 1.25 |
| Expected total goals | 3.76 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 89.1% |
| Under 1.5 | 10.9% |
| Over 2.5 | 72.3% |
| Under 2.5 | 27.7% |
| Over 3.5 | 52.0% |
| Under 3.5 | 48.0% |
| Over 4.5 | 32.4% |
| Under 4.5 | 67.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.27% |
| 2 | 1-1 | 7.78% |
| 3 | 3-1 | 7.75% |
| 4 | 2-0 | 7.39% |
| 5 | 3-0 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 65.3% | 66.1% | 1.51 | -1.3% |
| Draw | 18.9% | 19.8% | 5.02 | -4.9% |
| Elche CF win | 15.7% | 14.1% | 6.73 | +5.8% |
| Over 2.5 | 72.3% | 65.6% | 1.48 | +7.0% |
| Under 2.5 | 27.7% | 34.4% | 2.70 | -25.2% |

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
| Market best home last update utc | 2026-10-12T16:29:42Z |
| Market best draw last update utc | 2026-10-12T16:30:39Z |
| Market best away last update utc | 2026-10-12T16:29:42Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Villarreal |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.9% |
| P btts no | 34.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.25 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.19 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.61 |
| Fair Over 3.5 odds | 1.92 |
| Fair Under 3.5 odds | 2.08 |
| Fair Over 4.5 odds | 3.09 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 64.6% |
| Unadjusted draw probability | 18.0% |
| Unadjusted away-win probability | 17.4% |
| Raw p over 1 5 | 89.0% |
| Raw p under 3 5 | 48.1% |
| Raw p btts yes | 65.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.47 |
| Reference draw odds | 4.50 |
| Reference away odds | 6.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.65 |
| Home probability edge | -0.7% |
| Draw probability edge | -0.9% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | +6.7% |
| Under 2.5 probability edge | -6.7% |
| Raw edge prob home | -0.0150 |
| Raw ev home | -0.0247 |
| Raw edge prob draw | -0.0181 |
| Raw ev draw | -0.0942 |
| Raw edge prob away | 0.0330 |
| Raw ev away | 0.1687 |

</details>


---

## 2026-10-18 — CA Osasuna vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **CA Osasuna win** at **56.0%**. Expected goals are 2.71 for CA Osasuna and 1.48 for Real Racing Club de Santander (4.19 combined). The most likely exact score is 1-1 at 7.7%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 77.4%; Under 3.5 goals: 40.4%; Under 4.5 goals: 60.6%; BTTS Yes (both teams score): 73.5%; BTTS No (at least one team does not score): 26.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 56.0% | 1.78 |
| Draw | 21.8% | 4.58 |
| Real Racing Club de Santander win | 22.2% | 4.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 2.71 |
| Real Racing Club de Santander expected goals | 1.48 |
| Expected total goals | 4.19 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 77.4% |
| Under 2.5 | 22.6% |
| Over 3.5 | 59.6% |
| Under 3.5 | 40.4% |
| Over 4.5 | 39.4% |
| Under 4.5 | 60.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.73% |
| 2 | 2-2 | 7.65% |
| 3 | 2-1 | 7.27% |
| 4 | 3-1 | 6.56% |
| 5 | 1-2 | 5.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 56.0% | 48.6% | 2.02 | +13.2% |
| Draw | 21.8% | 26.3% | 3.75 | -18.2% |
| Real Racing Club de Santander win | 22.2% | 25.1% | 4.08 | -9.6% |
| Over 2.5 | 77.4% | 57.6% | 1.74 | +34.7% |
| Under 2.5 | 22.6% | 42.4% | 2.36 | -46.7% |

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
| Market best home last update utc | 2026-10-12T16:30:40Z |
| Market best draw last update utc | 2026-10-12T16:30:12Z |
| Market best away last update utc | 2026-10-12T16:29:42Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Osasuna |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 73.5% |
| P btts no | 26.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 49.85 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.44 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.43 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.47 |
| Fair Over 4.5 odds | 2.54 |
| Fair Under 4.5 odds | 1.65 |
| Unadjusted home-win probability | 63.4% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 19.2% |
| Raw p over 1 5 | 92.2% |
| Raw p under 3 5 | 39.7% |
| Raw p btts yes | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.98 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | +7.4% |
| Draw probability edge | -4.4% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | +19.8% |
| Under 2.5 probability edge | -19.8% |
| Raw edge prob home | 0.1482 |
| Raw ev home | 0.2814 |
| Raw edge prob draw | -0.0887 |
| Raw ev draw | -0.3483 |
| Raw edge prob away | -0.0594 |
| Raw ev away | -0.2172 |

</details>


---

## 2026-10-18 — Celta Vigo vs Alavés

The model's most likely 1X2 outcome is **Celta Vigo win** at **48.9%**. Expected goals are 1.51 for Celta Vigo and 0.96 for Alavés (2.47 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.5%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 48.9% | 2.04 |
| Draw | 27.0% | 3.71 |
| Alavés win | 24.1% | 4.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.51 |
| Alavés expected goals | 0.96 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 70.7% |
| Under 1.5 | 29.3% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.75% |
| 2 | 1-0 | 12.39% |
| 3 | 2-0 | 9.46% |
| 4 | 2-1 | 9.11% |
| 5 | 0-0 | 8.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 48.9% | 48.2% | 2.08 | +1.8% |
| Draw | 27.0% | 27.6% | 3.58 | -3.5% |
| Alavés win | 24.1% | 24.2% | 4.00 | -3.6% |
| Over 2.5 | 44.6% | 44.2% | 2.19 | -2.3% |
| Under 2.5 | 55.4% | 55.8% | 1.79 | -0.8% |

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
| Market best home last update utc | 2026-10-12T16:29:42Z |
| Market best draw last update utc | 2026-10-12T16:29:42Z |
| Market best away last update utc | 2026-10-12T16:30:11Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Tipico |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Celta |
| Matched away-team name | Alaves |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.30 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.62 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 49.7% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 70.8% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.00 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.85 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.70 |
| Home probability edge | +0.7% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.0147 |
| Raw ev home | 0.0334 |
| Raw edge prob draw | -0.0125 |
| Raw ev draw | -0.0573 |
| Raw edge prob away | -0.0021 |
| Raw ev away | -0.0405 |

</details>


---

## 2026-10-18 — Málaga vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **48.5%**. Expected goals are 0.57 for Málaga and 1.26 for Real Sociedad (1.83 combined). The most likely exact score is 0-1 at 18.3%. Goal-market probabilities: at least one goal: 84.7%; Over 2.5 goals: 27.7%; Under 3.5 goals: 89.0%; Under 4.5 goals: 96.2%; BTTS Yes (both teams score): 31.0%; BTTS No (at least one team does not score): 69.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 23.1% | 4.33 |
| Draw | 28.5% | 3.51 |
| Real Sociedad win | 48.5% | 2.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 0.57 |
| Real Sociedad expected goals | 1.26 |
| Expected total goals | 1.83 |
| Over 0.5 | 84.7% |
| Under 0.5 | 15.3% |
| Over 1.5 | 53.9% |
| Under 1.5 | 46.1% |
| Over 2.5 | 27.7% |
| Under 2.5 | 72.3% |
| Over 3.5 | 11.0% |
| Under 3.5 | 89.0% |
| Over 4.5 | 3.8% |
| Under 4.5 | 96.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.28% |
| 2 | 0-0 | 15.34% |
| 3 | 1-0 | 12.46% |
| 4 | 0-2 | 11.60% |
| 5 | 1-1 | 11.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 23.1% | 29.5% | 3.30 | -23.9% |
| Draw | 28.5% | 26.8% | 3.65 | +3.9% |
| Real Sociedad win | 48.5% | 43.7% | 2.29 | +11.0% |
| Over 2.5 | 27.7% | 53.9% | 1.86 | -48.5% |
| Under 2.5 | 72.3% | 46.1% | 2.10 | +51.9% |

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
| Market best home last update utc | 2026-10-12T16:30:11Z |
| Market best draw last update utc | 2026-10-12T16:30:40Z |
| Market best away last update utc | 2026-10-12T16:29:42Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 31.0% |
| P btts no | 69.0% |
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.52 |
| Fair Over 1.5 odds | 1.85 |
| Fair Under 1.5 odds | 2.17 |
| Fair Over 2.5 odds | 3.61 |
| Fair Under 2.5 odds | 1.38 |
| Fair Over 3.5 odds | 9.10 |
| Fair Under 3.5 odds | 1.12 |
| Fair Over 4.5 odds | 26.40 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 16.6% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 53.2% |
| Raw p over 1 5 | 54.7% |
| Raw p under 3 5 | 88.7% |
| Raw p btts yes | 31.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 3.15 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.18 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.02 |
| Home probability edge | -6.5% |
| Draw probability edge | +1.7% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -26.3% |
| Under 2.5 probability edge | +26.3% |
| Raw edge prob home | -0.1291 |
| Raw ev home | -0.4517 |
| Raw edge prob draw | 0.0334 |
| Raw ev draw | 0.1001 |
| Raw edge prob away | 0.0958 |
| Raw ev away | 0.2193 |

</details>


---

## 2026-10-18 — Real Madrid vs Sevilla

The model's most likely 1X2 outcome is **Real Madrid win** at **77.6%**. Expected goals are 2.62 for Real Madrid and 0.74 for Sevilla (3.37 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 65.3%; Under 3.5 goals: 56.5%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 48.8%; BTTS No (at least one team does not score): 51.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.6% | 1.29 |
| Draw | 14.8% | 6.74 |
| Sevilla win | 7.6% | 13.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.62 |
| Sevilla expected goals | 0.74 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 65.3% |
| Under 2.5 | 34.7% |
| Over 3.5 | 43.5% |
| Under 3.5 | 56.5% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.90% |
| 2 | 3-0 | 10.40% |
| 3 | 1-0 | 8.98% |
| 4 | 2-1 | 8.86% |
| 5 | 3-1 | 7.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.6% | 77.8% | 1.30 | +0.8% |
| Draw | 14.8% | 15.2% | 7.20 | +6.9% |
| Sevilla win | 7.6% | 7.0% | 12.50 | -5.2% |
| Over 2.5 | 65.3% | 70.5% | 1.39 | -9.3% |
| Under 2.5 | 34.7% | 29.5% | 3.07 | +6.6% |

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
| Market best home last update utc | 2026-10-12T16:29:42Z |
| Market best draw last update utc | 2026-10-12T16:30:40Z |
| Market best away last update utc | 2026-10-12T16:29:59Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Real Madrid |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.8% |
| P btts no | 51.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.49 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.70 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.88 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 4.01 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 77.4% |
| Unadjusted draw probability | 14.5% |
| Unadjusted away-win probability | 8.1% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 48.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.26 |
| Reference draw odds | 5.65 |
| Reference away odds | 11.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -0.2% |
| Draw probability edge | -0.4% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.0040 |
| Raw ev home | 0.0059 |
| Raw edge prob draw | -0.0073 |
| Raw ev draw | 0.0421 |
| Raw edge prob away | 0.0113 |
| Raw ev away | 0.0186 |

</details>


---

## 2026-10-19 — Getafe vs Rayo Vallecano

The model's most likely 1X2 outcome is **Getafe win** at **35.1%**. Expected goals are 0.92 for Getafe and 0.73 for Rayo Vallecano (1.65 combined). The most likely exact score is 0-0 at 18.6%. Goal-market probabilities: at least one goal: 81.4%; Over 2.5 goals: 23.3%; Under 3.5 goals: 91.4%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 31.2%; BTTS No (at least one team does not score): 68.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 35.1% | 2.85 |
| Draw | 33.5% | 2.98 |
| Rayo Vallecano win | 31.4% | 3.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 0.92 |
| Rayo Vallecano expected goals | 0.73 |
| Expected total goals | 1.65 |
| Over 0.5 | 81.4% |
| Under 0.5 | 18.6% |
| Over 1.5 | 49.3% |
| Under 1.5 | 50.7% |
| Over 2.5 | 23.3% |
| Under 2.5 | 76.7% |
| Over 3.5 | 8.6% |
| Under 3.5 | 91.4% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.62% |
| 2 | 1-0 | 16.17% |
| 3 | 0-1 | 15.87% |
| 4 | 1-1 | 12.62% |
| 5 | 2-0 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 35.1% | 32.5% | 3.05 | +7.2% |
| Draw | 33.5% | 32.2% | 3.16 | +5.9% |
| Rayo Vallecano win | 31.4% | 35.3% | 2.82 | -11.6% |
| Over 2.5 | 23.3% | 35.4% | 2.61 | -39.2% |
| Under 2.5 | 76.7% | 64.6% | 1.53 | +17.4% |

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
| Market best home last update utc | 2026-10-12T16:30:40Z |
| Market best draw last update utc | 2026-10-12T16:29:42Z |
| Market best away last update utc | 2026-10-12T16:30:40Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Unibet (SE) |
| Matched home-team name | Getafe |
| Matched away-team name | Vallecano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 31.2% |
| P btts no | 68.8% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.37 |
| Fair Over 1.5 odds | 2.03 |
| Fair Under 1.5 odds | 1.97 |
| Fair Over 2.5 odds | 4.29 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.61 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.05 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 37.8% |
| Unadjusted draw probability | 34.8% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 49.4% |
| Raw p under 3 5 | 91.4% |
| Raw p btts yes | 31.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.90 |
| Reference draw odds | 2.92 |
| Reference away odds | 2.68 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.58 |
| Reference Under 2.5 odds | 1.49 |
| Home probability edge | +2.7% |
| Draw probability edge | +1.3% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | -12.1% |
| Under 2.5 probability edge | +12.1% |
| Raw edge prob home | 0.0532 |
| Raw ev home | 0.1527 |
| Raw edge prob draw | 0.0254 |
| Raw ev draw | 0.0989 |
| Raw edge prob away | -0.0786 |
| Raw ev away | -0.2265 |

</details>


---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **41.0%**. Expected goals are 1.25 for Levante and 1.36 for Athletic Bilbao (2.61 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 47.4%; Under 3.5 goals: 73.5%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 53.8%; BTTS No (at least one team does not score): 46.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 29.6% | 3.38 |
| Draw | 29.4% | 3.40 |
| Athletic Bilbao win | 41.0% | 2.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.25 |
| Athletic Bilbao expected goals | 1.36 |
| Expected total goals | 2.61 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 73.5% |
| Under 1.5 | 26.5% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 26.5% |
| Under 3.5 | 73.5% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.01% |
| 2 | 0-1 | 10.30% |
| 3 | 1-2 | 8.89% |
| 4 | 0-0 | 8.35% |
| 5 | 1-0 | 7.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 29.6% | 24.9% | 3.75 | +10.9% |
| Draw | 29.4% | 32.2% | 3.52 | +3.6% |
| Athletic Bilbao win | 41.0% | 42.9% | 2.26 | -7.4% |
| Over 2.5 | 47.4% | 47.6% | 2.02 | -4.2% |
| Under 2.5 | 52.6% | 52.4% | 1.92 | +1.0% |

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
| Market best home last update utc | 2026-10-12T16:30:40Z |
| Market best draw last update utc | 2026-10-12T16:29:42Z |
| Market best away last update utc | 2026-10-12T16:30:39Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 53.8% |
| P btts no | 46.2% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.98 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.78 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.78 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.30 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 34.2% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 39.1% |
| Raw p over 1 5 | 73.6% |
| Raw p under 3 5 | 73.5% |
| Raw p btts yes | 53.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.75 |
| Reference draw odds | 2.94 |
| Reference away odds | 2.24 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.71 |
| Home probability edge | +4.6% |
| Draw probability edge | -2.8% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.0927 |
| Raw ev home | 0.2828 |
| Raw edge prob draw | -0.0554 |
| Raw ev draw | -0.0614 |
| Raw edge prob away | -0.0373 |
| Raw ev away | -0.1158 |

</details>


---
