# Premier League — football model report

Fixtures in this report: **15**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,190 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 365 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1333.746 |
| Base scoring parameter | 0.174 |
| Home-advantage parameter | 0.164 |
| Dixon-Coles low-score adjustment | -0.105 |
| Xi per day | 0.0019 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 15.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 5.00 |
| Additional event odds calls this league | 5.00 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-10 — Manchester United vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Manchester United win** at **55.4%**. Expected goals are 1.93 for Manchester United and 1.19 for Tottenham Hotspur (3.12 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.7%; Under 3.5 goals: 61.8%; Under 4.5 goals: 79.2%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 55.4% | 1.81 |
| Draw | 23.4% | 4.27 |
| Tottenham Hotspur win | 21.2% | 4.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.93 |
| Tottenham Hotspur expected goals | 1.19 |
| Expected total goals | 3.12 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 60.7% |
| Under 2.5 | 39.3% |
| Over 3.5 | 38.2% |
| Under 3.5 | 61.8% |
| Over 4.5 | 20.8% |
| Under 4.5 | 79.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.82% |
| 2 | 2-1 | 10.11% |
| 3 | 2-0 | 8.50% |
| 4 | 1-0 | 7.70% |
| 5 | 3-1 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 55.4% | 57.2% | 1.76 | -2.5% |
| Draw | 23.4% | 22.6% | 4.40 | +2.9% |
| Tottenham Hotspur win | 21.2% | 20.2% | 4.80 | +1.8% |
| Over 2.5 | 60.7% | 65.3% | 1.49 | -9.5% |
| Under 2.5 | 39.3% | 34.7% | 2.66 | +4.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T16:30:00+00:00 |
| Fixture id | 22c9b2c43cbe1334381269550dab78e6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:46:10Z |
| Market best draw last update utc | 2026-10-10T15:46:10Z |
| Market best away last update utc | 2026-10-10T15:46:11Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Man United |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.93 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.89 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.62 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.81 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 53.6% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 22.2% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 60.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.70 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.55 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.65 |
| Home probability edge | -1.8% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.0353 |
| Raw ev home | -0.0562 |
| Raw edge prob draw | 0.0160 |
| Raw ev draw | 0.0646 |
| Raw edge prob away | 0.0193 |
| Raw ev away | 0.0646 |

</details>


---

## 2026-10-11 — Crystal Palace vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **35.8%**. Expected goals are 1.25 for Crystal Palace and 1.23 for Nottingham Forest (2.48 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.2%; Under 4.5 goals: 89.4%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 35.0% | 2.86 |
| Draw | 29.2% | 3.43 |
| Nottingham Forest win | 35.8% | 2.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.25 |
| Nottingham Forest expected goals | 1.23 |
| Expected total goals | 2.48 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 72.2% |
| Under 1.5 | 27.8% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 23.8% |
| Under 3.5 | 76.2% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.92% |
| 2 | 0-0 | 9.53% |
| 3 | 0-1 | 9.28% |
| 4 | 1-0 | 9.00% |
| 5 | 1-2 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 35.0% | 34.5% | 2.90 | +1.5% |
| Draw | 29.2% | 28.5% | 3.50 | +2.2% |
| Nottingham Forest win | 35.8% | 36.9% | 2.72 | -2.5% |
| Over 2.5 | 45.3% | 50.0% | 1.96 | -11.3% |
| Under 2.5 | 54.7% | 50.0% | 2.02 | +10.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | 86effab5c6e7bfd58c8e88b1fb7c6ba9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:46:10Z |
| Market best draw last update utc | 2026-10-10T15:45:37Z |
| Market best away last update utc | 2026-10-10T15:46:10Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.49 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.59 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.21 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.40 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 35.4% |
| Unadjusted draw probability | 29.9% |
| Unadjusted away-win probability | 34.7% |
| Raw p over 1 5 | 72.1% |
| Raw p under 3 5 | 76.3% |
| Raw p btts yes | 51.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.75 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.58 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.90 |
| Home probability edge | +0.4% |
| Draw probability edge | +0.7% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | 0.0088 |
| Raw ev home | 0.0274 |
| Raw edge prob draw | 0.0133 |
| Raw ev draw | 0.0448 |
| Raw edge prob away | -0.0222 |
| Raw ev away | -0.0556 |

</details>


---

## 2026-10-11 — Hull City vs Everton

The model's most likely 1X2 outcome is **Hull City win** at **35.0%**. Expected goals are 1.09 for Hull City and 0.66 for Everton (1.74 combined). The most likely exact score is 0-0 at 17.0%. Goal-market probabilities: at least one goal: 83.0%; Over 2.5 goals: 26.0%; Under 3.5 goals: 90.3%; Under 4.5 goals: 96.7%; BTTS Yes (both teams score): 32.9%; BTTS No (at least one team does not score): 67.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 35.0% | 2.86 |
| Draw | 31.6% | 3.16 |
| Everton win | 33.4% | 3.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.09 |
| Everton expected goals | 0.66 |
| Expected total goals | 1.74 |
| Over 0.5 | 83.0% |
| Under 0.5 | 17.0% |
| Over 1.5 | 52.7% |
| Under 1.5 | 47.3% |
| Over 2.5 | 26.0% |
| Under 2.5 | 74.0% |
| Over 3.5 | 9.7% |
| Under 3.5 | 90.3% |
| Over 4.5 | 3.3% |
| Under 4.5 | 96.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 16.96% |
| 2 | 0-1 | 16.38% |
| 3 | 1-0 | 13.99% |
| 4 | 1-1 | 12.46% |
| 5 | 2-0 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 35.0% | 25.8% | 3.80 | +33.0% |
| Draw | 31.6% | 28.2% | 3.52 | +11.3% |
| Everton win | 33.4% | 46.0% | 2.20 | -26.5% |
| Over 2.5 | 26.0% | 47.7% | 2.08 | -46.0% |
| Under 2.5 | 74.0% | 52.3% | 1.89 | +39.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:00:00+00:00 |
| Fixture id | 0bdae4d304810578e47386606bff7106 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:46:11Z |
| Market best draw last update utc | 2026-10-10T15:45:37Z |
| Market best away last update utc | 2026-10-10T15:46:10Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Everton |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.9% |
| P btts no | 67.1% |
| Fair Over 0.5 odds | 1.20 |
| Fair Under 0.5 odds | 5.90 |
| Fair Over 1.5 odds | 1.90 |
| Fair Under 1.5 odds | 2.11 |
| Fair Over 2.5 odds | 3.85 |
| Fair Under 2.5 odds | 1.35 |
| Fair Over 3.5 odds | 10.32 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.72 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 44.2% |
| Unadjusted draw probability | 35.0% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 53.4% |
| Raw p under 3 5 | 90.0% |
| Raw p btts yes | 33.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 3.65 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.98 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +9.2% |
| Draw probability edge | +3.4% |
| Away probability edge | -12.6% |
| Over 2.5 probability edge | -21.8% |
| Under 2.5 probability edge | +21.8% |
| Raw edge prob home | 0.1843 |
| Raw ev home | 0.6804 |
| Raw edge prob draw | 0.0679 |
| Raw ev draw | 0.2321 |
| Raw edge prob away | -0.2522 |
| Raw ev away | -0.5429 |
| Market p over 1 5 | 74.9% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-10T15:45:37Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.63 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 74.7% |
| Market under 3 5 odds | 1.32 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-10T15:45:37Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.57 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 52.9% |
| Market btts yes odds | 1.87 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-10T15:46:10Z |
| Market reference btts yes odds | 1.87 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-11 — Liverpool vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **42.2%**. Expected goals are 1.40 for Liverpool and 1.65 for Manchester City (3.05 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 58.8%; Under 3.5 goals: 63.6%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 62.0%; BTTS No (at least one team does not score): 38.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 31.7% | 3.15 |
| Draw | 26.1% | 3.84 |
| Manchester City win | 42.2% | 2.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.40 |
| Manchester City expected goals | 1.65 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 81.9% |
| Under 1.5 | 18.1% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 36.4% |
| Under 3.5 | 63.6% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.04% |
| 2 | 1-2 | 8.99% |
| 3 | 2-1 | 7.72% |
| 4 | 0-1 | 6.65% |
| 5 | 0-2 | 6.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 31.7% | 32.0% | 3.15 | -0.1% |
| Draw | 26.1% | 26.0% | 3.90 | +1.7% |
| Manchester City win | 42.2% | 42.0% | 2.36 | -0.3% |
| Over 2.5 | 58.8% | 60.2% | 1.67 | -1.8% |
| Under 2.5 | 41.2% | 39.8% | 2.48 | +2.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T15:30:00+00:00 |
| Fixture id | 6dbab232dd8d2aed0cb1d6f7978fb7b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:46:10Z |
| Market best draw last update utc | 2026-10-10T15:46:10Z |
| Market best away last update utc | 2026-10-10T15:45:37Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Unibet (NL) |
| Matched home-team name | Liverpool |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 62.0% |
| P btts no | 38.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.05 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.54 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.75 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.18 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 31.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 62.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.95 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.28 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | -0.3% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -1.4% |
| Under 2.5 probability edge | +1.4% |
| Raw edge prob home | -0.0064 |
| Raw ev home | -0.0114 |
| Raw edge prob draw | 0.0019 |
| Raw ev draw | 0.0204 |
| Raw edge prob away | 0.0045 |
| Raw ev away | 0.0018 |

</details>


---

## 2026-10-12 — Coventry City vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **58.5%**. Expected goals are 0.36 for Coventry City and 1.82 for Newcastle United (2.18 combined). The most likely exact score is 0-1 at 15.9%. Goal-market probabilities: at least one goal: 86.5%; Over 2.5 goals: 34.4%; Under 3.5 goals: 84.5%; Under 4.5 goals: 93.9%; BTTS Yes (both teams score): 27.9%; BTTS No (at least one team does not score): 72.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 17.3% | 5.77 |
| Draw | 24.1% | 4.14 |
| Newcastle United win | 58.5% | 1.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 0.36 |
| Newcastle United expected goals | 1.82 |
| Expected total goals | 2.18 |
| Over 0.5 | 86.5% |
| Under 0.5 | 13.5% |
| Over 1.5 | 60.8% |
| Under 1.5 | 39.2% |
| Over 2.5 | 34.4% |
| Under 2.5 | 65.6% |
| Over 3.5 | 15.5% |
| Under 3.5 | 84.5% |
| Over 4.5 | 6.1% |
| Under 4.5 | 93.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.92% |
| 2 | 0-2 | 15.05% |
| 3 | 0-0 | 13.45% |
| 4 | 1-0 | 9.80% |
| 5 | 1-1 | 9.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 17.3% | 28.8% | 3.45 | -40.2% |
| Draw | 24.1% | 26.6% | 3.80 | -8.3% |
| Newcastle United win | 58.5% | 44.6% | 2.28 | +33.4% |
| Over 2.5 | 34.4% | 58.0% | 1.73 | -40.5% |
| Under 2.5 | 65.6% | 42.0% | 2.30 | +50.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-12T19:00:00+00:00 |
| Fixture id | acd5bd945dd953ad1e300df5bfe696f9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:37Z |
| Market best draw last update utc | 2026-10-10T15:46:11Z |
| Market best away last update utc | 2026-10-10T15:46:10Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 27.9% |
| P btts no | 72.1% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.43 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.55 |
| Fair Over 2.5 odds | 2.91 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.45 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 16.29 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 72.5% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 26.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 3.25 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.22 |
| Home probability edge | -11.5% |
| Draw probability edge | -2.5% |
| Away probability edge | +14.0% |
| Over 2.5 probability edge | -23.6% |
| Under 2.5 probability edge | +23.6% |
| Raw edge prob home | -0.2292 |
| Raw ev home | -0.7972 |
| Raw edge prob draw | -0.0501 |
| Raw ev draw | -0.1782 |
| Raw edge prob away | 0.2793 |
| Raw ev away | 0.6528 |
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-10T15:45:37Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 65.0% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-10T15:46:00Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.69 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 61.3% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-10T15:46:10Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.52 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **39.4%**. Expected goals are 1.48 for Brentford and 1.63 for Liverpool (3.11 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 60.1%; Under 3.5 goals: 62.2%; Under 4.5 goals: 79.6%; BTTS Yes (both teams score): 63.4%; BTTS No (at least one team does not score): 36.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 34.4% | 2.91 |
| Draw | 26.2% | 3.81 |
| Liverpool win | 39.4% | 2.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.48 |
| Liverpool expected goals | 1.63 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 60.1% |
| Under 2.5 | 39.9% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.4% |
| Under 4.5 | 79.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.98% |
| 2 | 1-2 | 8.58% |
| 3 | 2-1 | 8.11% |
| 4 | 2-2 | 6.56% |
| 5 | 0-1 | 6.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 34.4% | 35.0% | 2.88 | -0.9% |
| Draw | 26.2% | 26.5% | 3.80 | -0.4% |
| Liverpool win | 39.4% | 38.6% | 2.50 | -1.6% |
| Over 2.5 | 60.1% | 61.9% | 1.57 | -5.7% |
| Under 2.5 | 39.9% | 38.1% | 2.43 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | 8f1945e7272bc7e89016439f5ab321c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:37Z |
| Market best draw last update utc | 2026-10-10T15:46:10Z |
| Market best away last update utc | 2026-10-10T15:45:37Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Brentford |
| Matched away-team name | Liverpool |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.4% |
| P btts no | 36.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.79 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.82 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.51 |
| Fair Over 3.5 odds | 2.65 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.91 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 40.2% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.72 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.48 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | -0.6% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | -0.0117 |
| Raw ev home | -0.0260 |
| Raw edge prob draw | -0.0048 |
| Raw ev draw | -0.0130 |
| Raw edge prob away | 0.0166 |
| Raw ev away | 0.0052 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **39.4%**. Expected goals are 1.28 for Everton and 1.29 for Chelsea (2.57 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 48.1%; Under 3.5 goals: 74.1%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 53.3%; BTTS No (at least one team does not score): 46.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 33.1% | 3.02 |
| Draw | 27.4% | 3.64 |
| Chelsea win | 39.4% | 2.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.28 |
| Chelsea expected goals | 1.29 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 48.1% |
| Under 2.5 | 51.9% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.11% |
| 2 | 0-1 | 9.44% |
| 3 | 1-2 | 9.03% |
| 4 | 0-0 | 8.41% |
| 5 | 1-0 | 7.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 33.1% | 31.0% | 3.10 | +2.7% |
| Draw | 27.4% | 25.7% | 3.85 | +5.6% |
| Chelsea win | 39.4% | 43.3% | 2.32 | -8.6% |
| Over 2.5 | 48.1% | 58.0% | 1.72 | -17.2% |
| Under 2.5 | 51.9% | 42.0% | 2.30 | +19.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T11:30:00+00:00 |
| Fixture id | 764e6513cb3f348881503df70ccb90e0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:37Z |
| Market best draw last update utc | 2026-10-10T15:45:54Z |
| Market best away last update utc | 2026-10-10T15:46:10Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Everton |
| Matched away-team name | Chelsea |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 53.3% |
| P btts no | 46.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.89 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.87 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.27 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 53.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 3.05 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.22 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.22 |
| Home probability edge | +2.1% |
| Draw probability edge | +1.8% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | 0.0425 |
| Raw ev home | 0.0934 |
| Raw edge prob draw | 0.0350 |
| Raw ev draw | 0.1239 |
| Raw edge prob away | -0.0776 |
| Raw ev away | -0.1756 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.9%**. Expected goals are 0.85 for Fulham and 1.07 for Hull City (1.92 combined). The most likely exact score is 1-0 at 17.5%. Goal-market probabilities: at least one goal: 86.4%; Over 2.5 goals: 31.5%; Under 3.5 goals: 87.2%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 38.1%; BTTS No (at least one team does not score): 61.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.9% | 2.33 |
| Draw | 28.9% | 3.46 |
| Hull City win | 28.2% | 3.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.85 |
| Hull City expected goals | 1.07 |
| Expected total goals | 1.92 |
| Over 0.5 | 86.4% |
| Under 0.5 | 13.6% |
| Over 1.5 | 58.5% |
| Under 1.5 | 41.5% |
| Over 2.5 | 31.5% |
| Under 2.5 | 68.5% |
| Over 3.5 | 12.8% |
| Under 3.5 | 87.2% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.55% |
| 2 | 0-0 | 13.59% |
| 3 | 1-1 | 12.47% |
| 4 | 0-1 | 10.38% |
| 5 | 2-1 | 8.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 42.9% | 58.9% | 1.73 | -25.8% |
| Draw | 28.9% | 23.7% | 4.11 | +18.8% |
| Hull City win | 28.2% | 17.5% | 5.20 | +46.7% |
| Over 2.5 | 31.5% | 54.6% | 1.81 | -42.9% |
| Under 2.5 | 68.5% | 45.4% | 2.23 | +52.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | 7895f97f2f9577f3b13287a3d086859d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:37Z |
| Market best draw last update utc | 2026-10-10T15:45:37Z |
| Market best away last update utc | 2026-10-10T15:46:14Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | LeoVegas (SE) |
| Matched home-team name | Fulham |
| Matched away-team name | Hull |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 38.1% |
| P btts no | 61.9% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.36 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.41 |
| Fair Over 2.5 odds | 3.17 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.81 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 21.01 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 34.1% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 87.1% |
| Raw p btts yes | 39.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.65 |
| Reference draw odds | 3.90 |
| Reference away odds | 5.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | -16.0% |
| Draw probability edge | +5.2% |
| Away probability edge | +10.8% |
| Over 2.5 probability edge | -23.1% |
| Under 2.5 probability edge | +23.1% |
| Raw edge prob home | -0.3195 |
| Raw ev home | -0.5345 |
| Raw edge prob draw | 0.1044 |
| Raw ev draw | 0.4023 |
| Raw edge prob away | 0.2151 |
| Raw ev away | 1.0267 |
| Market p over 1 5 | 79.7% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Codere (IT) |
| Market best over 1 5 last update utc | 2026-10-10T15:45:58Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 68.2% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-10T15:46:00Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.86 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 54.4% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-10T15:46:10Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **82.9%**. Expected goals are 3.46 for Manchester City and 0.70 for Ipswich Town (4.15 combined). The most likely exact score is 3-0 at 10.3%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 76.8%; Under 3.5 goals: 41.8%; Under 4.5 goals: 61.2%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 82.9% | 1.21 |
| Draw | 11.7% | 8.56 |
| Ipswich Town win | 5.4% | 18.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.46 |
| Ipswich Town expected goals | 0.70 |
| Expected total goals | 4.15 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 91.7% |
| Under 1.5 | 8.3% |
| Over 2.5 | 76.8% |
| Under 2.5 | 23.2% |
| Over 3.5 | 58.2% |
| Under 3.5 | 41.8% |
| Over 4.5 | 38.8% |
| Under 4.5 | 61.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.28% |
| 2 | 2-0 | 8.92% |
| 3 | 4-0 | 8.89% |
| 4 | 3-1 | 7.17% |
| 5 | 2-1 | 6.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 82.9% | 78.6% | 1.29 | +6.9% |
| Draw | 11.7% | 14.2% | 7.00 | -18.2% |
| Ipswich Town win | 5.4% | 7.2% | 13.00 | -29.6% |
| Over 2.5 | 76.8% | 70.4% | 1.38 | +6.0% |
| Under 2.5 | 23.2% | 29.6% | 3.08 | -28.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T14:00:00+00:00 |
| Fixture id | bf2142d1ca76ba2fc9e61afce80f86c0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:37Z |
| Market best draw last update utc | 2026-10-10T15:46:10Z |
| Market best away last update utc | 2026-10-10T15:46:10Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Nordic Bet |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Man City |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.80 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.00 |
| Fair Over 2.5 odds | 1.30 |
| Fair Under 2.5 odds | 4.32 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.39 |
| Fair Over 4.5 odds | 2.58 |
| Fair Under 4.5 odds | 1.63 |
| Unadjusted home-win probability | 87.2% |
| Unadjusted draw probability | 9.1% |
| Unadjusted away-win probability | 3.7% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.4% |
| Raw p btts yes | 49.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.25 |
| Reference draw odds | 6.10 |
| Reference away odds | 11.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | +4.3% |
| Draw probability edge | -2.5% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +6.5% |
| Under 2.5 probability edge | -6.5% |
| Raw edge prob home | 0.0859 |
| Raw ev home | 0.1249 |
| Raw edge prob draw | -0.0507 |
| Raw ev draw | -0.3597 |
| Raw edge prob away | -0.0352 |
| Raw ev away | -0.5250 |
| Market p over 1 5 | 88.7% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-10T15:45:22Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 51.7% |
| Market under 3 5 odds | 1.92 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-10T15:44:34Z |
| Market reference under 3 5 odds | 1.85 |
| Market reference under 3 5 opposite odds | 1.97 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 54.6% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-10T15:46:02Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.14 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **45.2%**. Expected goals are 1.77 for Newcastle United and 1.44 for Aston Villa (3.21 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 62.2%; Under 3.5 goals: 60.0%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 64.3%; BTTS No (at least one team does not score): 35.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 45.2% | 2.21 |
| Draw | 25.1% | 3.98 |
| Aston Villa win | 29.7% | 3.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.77 |
| Aston Villa expected goals | 1.44 |
| Expected total goals | 3.21 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.2% |
| Under 2.5 | 37.8% |
| Over 3.5 | 40.0% |
| Under 3.5 | 60.0% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.32% |
| 2 | 2-1 | 9.26% |
| 3 | 1-2 | 7.25% |
| 4 | 2-2 | 6.52% |
| 5 | 2-0 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 45.2% | 45.9% | 2.17 | -2.0% |
| Draw | 25.1% | 25.0% | 3.95 | -0.8% |
| Aston Villa win | 29.7% | 29.1% | 3.35 | -0.5% |
| Over 2.5 | 62.2% | 60.2% | 1.65 | +2.7% |
| Under 2.5 | 37.8% | 39.8% | 2.45 | -7.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | d1bbbdcd3d430e70091b518369b559cf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:37Z |
| Market best draw last update utc | 2026-10-10T15:46:11Z |
| Market best away last update utc | 2026-10-10T15:45:37Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Newcastle |
| Matched away-team name | Aston Villa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.3% |
| P btts no | 35.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.60 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.28 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.65 |
| Fair Over 3.5 odds | 2.50 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.52 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 44.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 64.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.10 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | -0.8% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | -0.0153 |
| Raw ev home | -0.0364 |
| Raw edge prob draw | 0.0022 |
| Raw ev draw | -0.0036 |
| Raw edge prob away | 0.0131 |
| Raw ev away | 0.0173 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.9%**. Expected goals are 1.53 for Bournemouth and 1.04 for Sunderland (2.57 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 47.8%; Under 3.5 goals: 74.1%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.9% | 2.09 |
| Draw | 27.2% | 3.68 |
| Sunderland win | 24.8% | 4.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.53 |
| Sunderland expected goals | 1.04 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 47.8% |
| Under 2.5 | 52.2% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.99% |
| 2 | 1-0 | 10.55% |
| 3 | 2-1 | 9.45% |
| 4 | 2-0 | 9.06% |
| 5 | 0-0 | 8.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.9% | 48.6% | 2.04 | -2.2% |
| Draw | 27.2% | 26.3% | 3.80 | +3.4% |
| Sunderland win | 24.8% | 25.1% | 3.85 | -4.3% |
| Over 2.5 | 47.8% | 52.3% | 1.88 | -10.0% |
| Under 2.5 | 52.2% | 47.7% | 2.07 | +8.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | dfd5d6648be46426e418801584d46a68 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:37Z |
| Market best draw last update utc | 2026-10-10T15:46:10Z |
| Market best away last update utc | 2026-10-10T15:45:37Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bournemouth |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.63 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.33 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 74.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 52.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.98 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.98 |
| Home probability edge | -0.7% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | -0.0135 |
| Raw ev home | -0.0357 |
| Raw edge prob draw | 0.0191 |
| Raw ev draw | 0.0703 |
| Raw edge prob away | -0.0056 |
| Raw ev away | -0.0543 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **57.1%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 56.6%; Under 3.5 goals: 66.0%; Under 4.5 goals: 82.4%; BTTS Yes (both teams score): 56.4%; BTTS No (at least one team does not score): 43.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 57.1% | 1.75 |
| Draw | 23.7% | 4.22 |
| Crystal Palace win | 19.2% | 5.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 1.85 |
| Crystal Palace expected goals | 1.08 |
| Expected total goals | 2.93 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 80.3% |
| Under 1.5 | 19.7% |
| Over 2.5 | 56.6% |
| Under 2.5 | 43.4% |
| Over 3.5 | 34.0% |
| Under 3.5 | 66.0% |
| Over 4.5 | 17.6% |
| Under 4.5 | 82.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.20% |
| 2 | 2-1 | 10.39% |
| 3 | 2-0 | 9.62% |
| 4 | 1-0 | 9.23% |
| 5 | 3-1 | 6.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 57.1% | 60.0% | 1.67 | -4.7% |
| Draw | 23.7% | 22.4% | 4.45 | +5.4% |
| Crystal Palace win | 19.2% | 17.6% | 5.20 | +0.1% |
| Over 2.5 | 56.6% | 60.9% | 1.65 | -6.6% |
| Under 2.5 | 43.4% | 39.1% | 2.45 | +6.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 9fc08b390a49c4434f7cf631a0bb88fb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:37Z |
| Market best draw last update utc | 2026-10-10T15:45:37Z |
| Market best away last update utc | 2026-10-10T15:46:11Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.29 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.08 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 2.94 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.69 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 80.1% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.62 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.15 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -2.9% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.0580 |
| Raw ev home | -0.0953 |
| Raw edge prob draw | 0.0253 |
| Raw ev draw | 0.1100 |
| Raw edge prob away | 0.0328 |
| Raw ev away | 0.0860 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **36.4%**. Expected goals are 1.42 for Leeds United and 1.30 for Manchester United (2.72 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 51.5%; Under 3.5 goals: 71.0%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 36.4% | 2.75 |
| Draw | 27.2% | 3.68 |
| Manchester United win | 36.4% | 2.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.30 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 29.0% |
| Under 3.5 | 71.0% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.94% |
| 2 | 1-2 | 8.68% |
| 3 | 2-1 | 8.14% |
| 4 | 0-1 | 8.01% |
| 5 | 1-0 | 7.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 36.4% | 34.3% | 2.94 | +7.1% |
| Draw | 27.2% | 26.1% | 3.85 | +4.6% |
| Manchester United win | 36.4% | 39.6% | 2.52 | -8.3% |
| Over 2.5 | 51.5% | 60.0% | 1.69 | -13.0% |
| Under 2.5 | 48.5% | 40.0% | 2.36 | +14.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 676b3b0b609e9cf565da450786618d26 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:37Z |
| Market best draw last update utc | 2026-10-10T15:46:10Z |
| Market best away last update utc | 2026-10-10T15:46:10Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.19 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.45 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.09 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.6% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 56.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.78 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.42 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | +2.2% |
| Draw probability edge | +1.0% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -8.5% |
| Under 2.5 probability edge | +8.5% |
| Raw edge prob home | 0.0433 |
| Raw ev home | 0.1344 |
| Raw edge prob draw | 0.0209 |
| Raw ev draw | 0.0862 |
| Raw edge prob away | -0.0641 |
| Raw ev away | -0.1633 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **57.8%**. Expected goals are 0.77 for Nottingham Forest and 1.55 for Arsenal (2.32 combined). The most likely exact score is 0-1 at 14.8%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 41.9%; Under 3.5 goals: 79.2%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 43.0%; BTTS No (at least one team does not score): 57.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.3% | 6.12 |
| Draw | 25.9% | 3.86 |
| Arsenal win | 57.8% | 1.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.77 |
| Arsenal expected goals | 1.55 |
| Expected total goals | 2.32 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 69.1% |
| Under 1.5 | 30.9% |
| Over 2.5 | 41.9% |
| Under 2.5 | 58.1% |
| Over 3.5 | 20.8% |
| Under 3.5 | 79.2% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.78% |
| 2 | 0-2 | 12.47% |
| 3 | 1-1 | 11.97% |
| 4 | 0-0 | 10.20% |
| 5 | 1-2 | 9.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.3% | 15.4% | 6.20 | +1.3% |
| Draw | 25.9% | 23.8% | 4.10 | +6.1% |
| Arsenal win | 57.8% | 60.9% | 1.66 | -4.1% |
| Over 2.5 | 41.9% | 49.4% | 1.97 | -17.5% |
| Under 2.5 | 58.1% | 50.6% | 1.97 | +14.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | f696a248965373d9071dc0662e5c58a8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:37Z |
| Market best draw last update utc | 2026-10-10T15:45:54Z |
| Market best away last update utc | 2026-10-10T15:45:37Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 43.0% |
| P btts no | 57.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.80 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.23 |
| Fair Over 2.5 odds | 2.39 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.80 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.25 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 43.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 5.90 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +1.0% |
| Draw probability edge | +2.1% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | 0.0196 |
| Raw ev home | 0.0734 |
| Raw edge prob draw | 0.0423 |
| Raw ev draw | 0.1477 |
| Raw edge prob away | -0.0619 |
| Raw ev away | -0.0921 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **68.0%**. Expected goals are 1.71 for Tottenham Hotspur and 0.34 for Coventry City (2.04 combined). The most likely exact score is 1-0 at 20.5%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 33.2%; Under 3.5 goals: 85.4%; Under 4.5 goals: 94.5%; BTTS Yes (both teams score): 24.2%; BTTS No (at least one team does not score): 75.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 68.0% | 1.47 |
| Draw | 22.2% | 4.51 |
| Coventry City win | 9.8% | 10.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.71 |
| Coventry City expected goals | 0.34 |
| Expected total goals | 2.04 |
| Over 0.5 | 86.8% |
| Under 0.5 | 13.2% |
| Over 1.5 | 60.4% |
| Under 1.5 | 39.6% |
| Over 2.5 | 33.2% |
| Under 2.5 | 66.8% |
| Over 3.5 | 14.6% |
| Under 3.5 | 85.4% |
| Over 4.5 | 5.5% |
| Under 4.5 | 94.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.49% |
| 2 | 2-0 | 18.11% |
| 3 | 0-0 | 13.22% |
| 4 | 3-0 | 10.29% |
| 5 | 1-1 | 7.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 68.0% | 65.0% | 1.54 | +4.7% |
| Draw | 22.2% | 21.3% | 4.72 | +4.7% |
| Coventry City win | 9.8% | 13.7% | 6.52 | -36.0% |
| Over 2.5 | 33.2% | 60.9% | 1.64 | -45.6% |
| Under 2.5 | 66.8% | 39.1% | 2.46 | +64.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T19:00:00+00:00 |
| Fixture id | 9baaf4e48b041cfef04e70e42532502e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-10T15:45:37Z |
| Market best draw last update utc | 2026-10-10T15:45:37Z |
| Market best away last update utc | 2026-10-10T15:45:56Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betsson |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 24.2% |
| P btts no | 75.8% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.56 |
| Fair Over 1.5 odds | 1.66 |
| Fair Under 1.5 odds | 2.52 |
| Fair Over 2.5 odds | 3.01 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 6.84 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.15 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 5.9% |
| Raw p over 1 5 | 61.3% |
| Raw p under 3 5 | 85.0% |
| Raw p btts yes | 24.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.50 |
| Reference draw odds | 4.30 |
| Reference away odds | 6.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | +3.0% |
| Draw probability edge | +0.9% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | -27.7% |
| Under 2.5 probability edge | +27.7% |
| Raw edge prob home | 0.0593 |
| Raw ev home | 0.0927 |
| Raw edge prob draw | 0.0185 |
| Raw ev draw | 0.0909 |
| Raw edge prob away | -0.0778 |
| Raw ev away | -0.6133 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-10T15:45:22Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 61.9% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-10T15:46:00Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 55.9% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-10T15:45:37Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.08 |
| Market btts yes bookmakers | 2 |

</details>


---
