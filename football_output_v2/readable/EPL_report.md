# Premier League — football model report

Fixtures in this report: **14**.

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
| Live odds matched | 14.00 |
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

## 2026-10-11 — Crystal Palace vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **35.9%**. Expected goals are 1.25 for Crystal Palace and 1.23 for Nottingham Forest (2.48 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.2%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 35.1% | 2.85 |
| Draw | 29.0% | 3.45 |
| Nottingham Forest win | 35.9% | 2.78 |

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
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.81% |
| 2 | 0-0 | 9.47% |
| 3 | 0-1 | 9.30% |
| 4 | 1-0 | 9.04% |
| 5 | 1-2 | 8.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 35.1% | 34.8% | 2.92 | +2.5% |
| Draw | 29.0% | 28.1% | 3.50 | +1.4% |
| Nottingham Forest win | 35.9% | 37.1% | 2.70 | -3.0% |
| Over 2.5 | 45.3% | 49.4% | 1.96 | -11.1% |
| Under 2.5 | 54.7% | 50.6% | 2.04 | +11.5% |

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
| Market best home last update utc | 2026-10-11T06:31:05Z |
| Market best draw last update utc | 2026-10-11T06:31:20Z |
| Market best away last update utc | 2026-10-11T06:31:21Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.56 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.60 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.20 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.38 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 35.4% |
| Unadjusted draw probability | 29.9% |
| Unadjusted away-win probability | 34.7% |
| Raw p over 1 5 | 72.1% |
| Raw p under 3 5 | 76.3% |
| Raw p btts yes | 51.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.63 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.87 |
| Home probability edge | +0.3% |
| Draw probability edge | +0.9% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | 0.0063 |
| Raw ev home | 0.0345 |
| Raw edge prob draw | 0.0176 |
| Raw ev draw | 0.0448 |
| Raw edge prob away | -0.0239 |
| Raw ev away | -0.0626 |

</details>


---

## 2026-10-11 — Hull City vs Everton

The model's most likely 1X2 outcome is **Hull City win** at **35.4%**. Expected goals are 1.09 for Hull City and 0.66 for Everton (1.74 combined). The most likely exact score is 0-0 at 16.9%. Goal-market probabilities: at least one goal: 83.1%; Over 2.5 goals: 26.0%; Under 3.5 goals: 90.3%; Under 4.5 goals: 96.7%; BTTS Yes (both teams score): 32.9%; BTTS No (at least one team does not score): 67.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 35.4% | 2.82 |
| Draw | 31.6% | 3.17 |
| Everton win | 33.0% | 3.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.09 |
| Everton expected goals | 0.66 |
| Expected total goals | 1.74 |
| Over 0.5 | 83.1% |
| Under 0.5 | 16.9% |
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
| 1 | 0-0 | 16.94% |
| 2 | 0-1 | 16.20% |
| 3 | 1-0 | 14.14% |
| 4 | 1-1 | 12.45% |
| 5 | 2-0 | 8.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 35.4% | 26.6% | 3.95 | +39.8% |
| Draw | 31.6% | 28.2% | 3.52 | +11.2% |
| Everton win | 33.0% | 45.3% | 2.18 | -28.0% |
| Over 2.5 | 26.0% | 47.0% | 2.12 | -44.9% |
| Under 2.5 | 74.0% | 53.0% | 1.89 | +39.9% |

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
| Market best home last update utc | 2026-10-11T06:31:20Z |
| Market best draw last update utc | 2026-10-11T06:31:05Z |
| Market best away last update utc | 2026-10-11T06:31:05Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
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
| Fair Over 3.5 odds | 10.30 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.66 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 44.2% |
| Unadjusted draw probability | 35.0% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 53.4% |
| Raw p under 3 5 | 90.0% |
| Raw p btts yes | 33.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 3.65 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.17 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.79 |
| Home probability edge | +8.8% |
| Draw probability edge | +3.4% |
| Away probability edge | -12.2% |
| Over 2.5 probability edge | -21.0% |
| Under 2.5 probability edge | +21.0% |
| Raw edge prob home | 0.1764 |
| Raw ev home | 0.7468 |
| Raw edge prob draw | 0.0684 |
| Raw ev draw | 0.2321 |
| Raw edge prob away | -0.2448 |
| Raw ev away | -0.5471 |
| Market p over 1 5 | 74.2% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T06:31:23Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.30 |
| Market over 1 5 bookmakers | 5 |
| Market p under 3 5 | 74.4% |
| Market under 3 5 odds | 1.32 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T06:31:23Z |
| Market reference under 3 5 odds | 1.32 |
| Market reference under 3 5 opposite odds | 3.60 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 52.4% |
| Market btts yes odds | 1.88 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T06:31:20Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 1.95 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-11 — Liverpool vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **42.7%**. Expected goals are 1.40 for Liverpool and 1.65 for Manchester City (3.05 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.8%; Under 3.5 goals: 63.6%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 61.9%; BTTS No (at least one team does not score): 38.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 31.4% | 3.19 |
| Draw | 26.0% | 3.85 |
| Manchester City win | 42.7% | 2.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.40 |
| Manchester City expected goals | 1.65 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 82.0% |
| Under 1.5 | 18.0% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 36.4% |
| Under 3.5 | 63.6% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.99% |
| 2 | 1-2 | 9.09% |
| 3 | 2-1 | 7.64% |
| 4 | 0-1 | 6.72% |
| 5 | 0-2 | 6.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 31.4% | 31.3% | 3.20 | +0.3% |
| Draw | 26.0% | 25.8% | 3.85 | -0.0% |
| Manchester City win | 42.7% | 42.9% | 2.36 | +0.7% |
| Over 2.5 | 58.8% | 59.3% | 1.67 | -1.7% |
| Under 2.5 | 41.2% | 40.7% | 2.41 | -0.8% |

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
| Market best home last update utc | 2026-10-11T06:31:20Z |
| Market best draw last update utc | 2026-10-11T06:31:20Z |
| Market best away last update utc | 2026-10-11T06:31:05Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.9% |
| P btts no | 38.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.12 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.54 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.75 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.17 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 31.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 62.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.28 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | +0.0% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0007 |
| Raw ev home | 0.0043 |
| Raw edge prob draw | 0.0040 |
| Raw ev draw | 0.0073 |
| Raw edge prob away | -0.0047 |
| Raw ev away | 0.0018 |

</details>


---

## 2026-10-12 — Coventry City vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **59.3%**. Expected goals are 0.36 for Coventry City and 1.82 for Newcastle United (2.18 combined). The most likely exact score is 0-1 at 16.1%. Goal-market probabilities: at least one goal: 86.9%; Over 2.5 goals: 34.7%; Under 3.5 goals: 84.4%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 27.7%; BTTS No (at least one team does not score): 72.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 17.2% | 5.83 |
| Draw | 23.5% | 4.26 |
| Newcastle United win | 59.3% | 1.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 0.36 |
| Newcastle United expected goals | 1.82 |
| Expected total goals | 2.18 |
| Over 0.5 | 86.9% |
| Under 0.5 | 13.1% |
| Over 1.5 | 61.1% |
| Under 1.5 | 38.9% |
| Over 2.5 | 34.7% |
| Under 2.5 | 65.3% |
| Over 3.5 | 15.6% |
| Under 3.5 | 84.4% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.15% |
| 2 | 0-2 | 15.26% |
| 3 | 0-0 | 13.10% |
| 4 | 1-0 | 9.69% |
| 5 | 0-3 | 9.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 17.2% | 28.4% | 3.40 | -41.7% |
| Draw | 23.5% | 25.4% | 3.80 | -10.7% |
| Newcastle United win | 59.3% | 46.2% | 2.30 | +36.5% |
| Over 2.5 | 34.7% | 56.2% | 1.75 | -39.3% |
| Under 2.5 | 65.3% | 43.8% | 2.25 | +47.0% |

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
| Market best home last update utc | 2026-10-11T06:31:36Z |
| Market best draw last update utc | 2026-10-11T06:31:20Z |
| Market best away last update utc | 2026-10-11T06:31:20Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 27.7% |
| P btts no | 72.3% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.64 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.57 |
| Fair Over 2.5 odds | 2.88 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.40 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.11 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 72.5% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 26.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 3.40 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.12 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | -11.3% |
| Draw probability edge | -1.9% |
| Away probability edge | +13.1% |
| Over 2.5 probability edge | -21.5% |
| Under 2.5 probability edge | +21.5% |
| Raw edge prob home | -0.2256 |
| Raw ev home | -0.8001 |
| Raw edge prob draw | -0.0374 |
| Raw ev draw | -0.1782 |
| Raw edge prob away | 0.2629 |
| Raw ev away | 0.6673 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T06:31:23Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 65.3% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-11T06:31:23Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 59.3% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T06:31:20Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.25 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **39.6%**. Expected goals are 1.48 for Brentford and 1.63 for Liverpool (3.11 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 60.3%; Under 3.5 goals: 62.2%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 34.7% | 2.88 |
| Draw | 25.7% | 3.90 |
| Liverpool win | 39.6% | 2.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.48 |
| Liverpool expected goals | 1.63 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.73% |
| 2 | 1-2 | 8.63% |
| 3 | 2-1 | 8.19% |
| 4 | 2-2 | 6.42% |
| 5 | 0-1 | 6.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 34.7% | 35.7% | 2.88 | +0.1% |
| Draw | 25.7% | 25.4% | 3.85 | -1.2% |
| Liverpool win | 39.6% | 39.0% | 2.52 | -0.2% |
| Over 2.5 | 60.3% | 61.0% | 1.55 | -6.6% |
| Under 2.5 | 39.7% | 39.0% | 2.45 | -2.7% |

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
| Market best home last update utc | 2026-10-11T06:31:05Z |
| Market best draw last update utc | 2026-10-11T06:31:20Z |
| Market best away last update utc | 2026-10-11T06:31:20Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Nordic Bet |
| Matched home-team name | Brentford |
| Matched away-team name | Liverpool |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.17 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.83 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.89 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 40.2% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.48 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -0.9% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -0.7% |
| Under 2.5 probability edge | +0.7% |
| Raw edge prob home | -0.0185 |
| Raw ev home | -0.0260 |
| Raw edge prob draw | 0.0061 |
| Raw ev draw | 0.0000 |
| Raw edge prob away | 0.0125 |
| Raw ev away | 0.0132 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **39.1%**. Expected goals are 1.28 for Everton and 1.29 for Chelsea (2.57 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 48.3%; Under 3.5 goals: 74.0%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 53.2%; BTTS No (at least one team does not score): 46.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 34.0% | 2.95 |
| Draw | 27.0% | 3.71 |
| Chelsea win | 39.1% | 2.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.28 |
| Chelsea expected goals | 1.29 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 48.3% |
| Under 2.5 | 51.7% |
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.89% |
| 2 | 0-1 | 9.36% |
| 3 | 1-2 | 8.95% |
| 4 | 0-0 | 8.27% |
| 5 | 1-0 | 8.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 34.0% | 32.6% | 3.20 | +8.6% |
| Draw | 27.0% | 24.8% | 3.85 | +3.9% |
| Chelsea win | 39.1% | 42.6% | 2.31 | -9.7% |
| Over 2.5 | 48.3% | 59.2% | 1.72 | -16.9% |
| Under 2.5 | 51.7% | 40.8% | 2.32 | +19.9% |

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
| Market best home last update utc | 2026-10-11T06:31:20Z |
| Market best draw last update utc | 2026-10-11T06:31:37Z |
| Market best away last update utc | 2026-10-11T06:31:05Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Everton |
| Matched away-team name | Chelsea |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 53.2% |
| P btts no | 46.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.09 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.88 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.23 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 53.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.28 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +1.3% |
| Draw probability edge | +2.2% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | 0.0264 |
| Raw ev home | 0.1287 |
| Raw edge prob draw | 0.0443 |
| Raw ev draw | 0.1239 |
| Raw edge prob away | -0.0707 |
| Raw ev away | -0.1791 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.1%**. Expected goals are 0.85 for Fulham and 1.07 for Hull City (1.92 combined). The most likely exact score is 1-0 at 17.2%. Goal-market probabilities: at least one goal: 86.5%; Over 2.5 goals: 31.6%; Under 3.5 goals: 87.2%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 38.0%; BTTS No (at least one team does not score): 62.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.1% | 2.38 |
| Draw | 28.6% | 3.50 |
| Hull City win | 29.3% | 3.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.85 |
| Hull City expected goals | 1.07 |
| Expected total goals | 1.92 |
| Over 0.5 | 86.5% |
| Under 0.5 | 13.5% |
| Over 1.5 | 58.5% |
| Under 1.5 | 41.5% |
| Over 2.5 | 31.6% |
| Under 2.5 | 68.4% |
| Over 3.5 | 12.8% |
| Under 3.5 | 87.2% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.23% |
| 2 | 0-0 | 13.46% |
| 3 | 1-1 | 12.34% |
| 4 | 0-1 | 10.78% |
| 5 | 2-1 | 8.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 42.1% | 57.3% | 1.73 | -27.2% |
| Draw | 28.6% | 23.1% | 4.11 | +17.6% |
| Hull City win | 29.3% | 19.6% | 5.18 | +51.7% |
| Over 2.5 | 31.6% | 58.3% | 1.81 | -42.8% |
| Under 2.5 | 68.4% | 41.7% | 2.23 | +52.5% |

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
| Market best home last update utc | 2026-10-11T06:31:05Z |
| Market best draw last update utc | 2026-10-11T06:31:05Z |
| Market best away last update utc | 2026-10-11T06:31:05Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | LeoVegas (SE) |
| Matched home-team name | Fulham |
| Matched away-team name | Hull |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 38.0% |
| P btts no | 62.0% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.43 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.41 |
| Fair Over 2.5 odds | 3.16 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.79 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.91 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 34.1% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 87.1% |
| Raw p btts yes | 39.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.71 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -15.2% |
| Draw probability edge | +5.5% |
| Away probability edge | +9.7% |
| Over 2.5 probability edge | -26.7% |
| Under 2.5 probability edge | +26.7% |
| Raw edge prob home | -0.3038 |
| Raw ev home | -0.5345 |
| Raw edge prob draw | 0.1102 |
| Raw ev draw | 0.4023 |
| Raw edge prob away | 0.1936 |
| Raw ev away | 1.0189 |
| Market p over 1 5 | 81.0% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Codere (IT) |
| Market best over 1 5 last update utc | 2026-10-11T06:31:05Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 68.2% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T06:31:20Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.86 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 55.8% |
| Market btts yes odds | 1.79 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T06:31:21Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **82.6%**. Expected goals are 3.46 for Manchester City and 0.70 for Ipswich Town (4.15 combined). The most likely exact score is 3-0 at 10.3%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 76.9%; Under 3.5 goals: 41.9%; Under 4.5 goals: 61.2%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 82.6% | 1.21 |
| Draw | 11.4% | 8.75 |
| Ipswich Town win | 5.9% | 16.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.46 |
| Ipswich Town expected goals | 0.70 |
| Expected total goals | 4.15 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 91.6% |
| Under 1.5 | 8.4% |
| Over 2.5 | 76.9% |
| Under 2.5 | 23.1% |
| Over 3.5 | 58.1% |
| Under 3.5 | 41.9% |
| Over 4.5 | 38.8% |
| Under 4.5 | 61.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.25% |
| 2 | 2-0 | 8.90% |
| 3 | 4-0 | 8.86% |
| 4 | 3-1 | 7.15% |
| 5 | 2-1 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 82.6% | 78.1% | 1.29 | +6.6% |
| Draw | 11.4% | 13.7% | 7.20 | -17.8% |
| Ipswich Town win | 5.9% | 8.2% | 13.50 | -19.8% |
| Over 2.5 | 76.9% | 71.2% | 1.39 | +6.9% |
| Under 2.5 | 23.1% | 28.8% | 3.00 | -30.7% |

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
| Market best home last update utc | 2026-10-11T06:31:05Z |
| Market best draw last update utc | 2026-10-11T06:31:20Z |
| Market best away last update utc | 2026-10-11T06:31:20Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Nordic Bet |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Man City |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.70 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.96 |
| Fair Over 2.5 odds | 1.30 |
| Fair Under 2.5 odds | 4.33 |
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
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.25 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +4.6% |
| Draw probability edge | -2.3% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | +5.7% |
| Under 2.5 probability edge | -5.7% |
| Raw edge prob home | 0.0913 |
| Raw ev home | 0.1249 |
| Raw edge prob draw | -0.0455 |
| Raw ev draw | -0.3414 |
| Raw edge prob away | -0.0457 |
| Raw ev away | -0.5067 |
| Market p over 1 5 | 88.6% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T06:31:37Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 51.3% |
| Market under 3 5 odds | 1.92 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T06:31:22Z |
| Market reference under 3 5 odds | 1.92 |
| Market reference under 3 5 opposite odds | 2.02 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 53.7% |
| Market btts yes odds | 1.88 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T06:31:21Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **44.9%**. Expected goals are 1.77 for Newcastle United and 1.44 for Aston Villa (3.21 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 62.1%; Under 3.5 goals: 60.1%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 64.4%; BTTS No (at least one team does not score): 35.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 44.9% | 2.23 |
| Draw | 25.4% | 3.94 |
| Aston Villa win | 29.7% | 3.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.77 |
| Aston Villa expected goals | 1.44 |
| Expected total goals | 3.21 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 39.9% |
| Under 3.5 | 60.1% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.45% |
| 2 | 2-1 | 9.21% |
| 3 | 1-2 | 7.24% |
| 4 | 2-2 | 6.60% |
| 5 | 2-0 | 6.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 44.9% | 45.4% | 2.17 | -2.6% |
| Draw | 25.4% | 25.6% | 3.95 | +0.4% |
| Aston Villa win | 29.7% | 29.0% | 3.35 | -0.6% |
| Over 2.5 | 62.1% | 59.3% | 1.65 | +2.5% |
| Under 2.5 | 37.9% | 40.7% | 2.45 | -7.2% |

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
| Market best home last update utc | 2026-10-11T06:31:05Z |
| Market best draw last update utc | 2026-10-11T06:31:36Z |
| Market best away last update utc | 2026-10-11T06:31:05Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Newcastle |
| Matched away-team name | Aston Villa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.4% |
| P btts no | 35.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.38 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.27 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.50 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.53 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 44.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 64.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.10 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -0.5% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | +2.8% |
| Under 2.5 probability edge | -2.8% |
| Raw edge prob home | -0.0100 |
| Raw ev home | -0.0364 |
| Raw edge prob draw | -0.0036 |
| Raw ev draw | -0.0036 |
| Raw edge prob away | 0.0136 |
| Raw ev away | 0.0173 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **48.0%**. Expected goals are 1.53 for Bournemouth and 1.04 for Sunderland (2.57 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 47.9%; Under 3.5 goals: 74.1%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 48.0% | 2.08 |
| Draw | 27.1% | 3.69 |
| Sunderland win | 24.9% | 4.02 |

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
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.93% |
| 2 | 1-0 | 10.56% |
| 3 | 2-1 | 9.46% |
| 4 | 2-0 | 9.07% |
| 5 | 0-0 | 8.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 48.0% | 48.8% | 2.10 | +0.8% |
| Draw | 27.1% | 26.0% | 3.75 | +1.6% |
| Sunderland win | 24.9% | 25.2% | 3.85 | -4.2% |
| Over 2.5 | 47.9% | 53.1% | 1.88 | -10.0% |
| Under 2.5 | 52.1% | 46.9% | 2.07 | +7.9% |

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
| Market best home last update utc | 2026-10-11T06:31:20Z |
| Market best draw last update utc | 2026-10-11T06:31:05Z |
| Market best away last update utc | 2026-10-11T06:31:05Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
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
| Fair Under 0.5 odds | 11.68 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.32 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 74.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 52.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.95 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | -0.7% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.0150 |
| Raw ev home | -0.0073 |
| Raw edge prob draw | 0.0216 |
| Raw ev draw | 0.0562 |
| Raw edge prob away | -0.0066 |
| Raw ev away | -0.0543 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **56.8%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 56.6%; Under 3.5 goals: 66.1%; Under 4.5 goals: 82.4%; BTTS Yes (both teams score): 56.4%; BTTS No (at least one team does not score): 43.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 56.8% | 1.76 |
| Draw | 23.6% | 4.23 |
| Crystal Palace win | 19.6% | 5.10 |

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
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.6% |
| Under 4.5 | 82.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.18% |
| 2 | 2-1 | 10.34% |
| 3 | 2-0 | 9.56% |
| 4 | 1-0 | 9.18% |
| 5 | 3-1 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 56.8% | 59.3% | 1.64 | -6.9% |
| Draw | 23.6% | 22.3% | 4.57 | +8.0% |
| Crystal Palace win | 19.6% | 18.3% | 5.55 | +8.8% |
| Over 2.5 | 56.6% | 61.6% | 1.63 | -7.7% |
| Under 2.5 | 43.4% | 38.4% | 2.49 | +8.0% |

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
| Market best home last update utc | 2026-10-11T06:31:36Z |
| Market best draw last update utc | 2026-10-11T06:31:05Z |
| Market best away last update utc | 2026-10-11T06:26:54Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.32 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.08 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.70 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 80.1% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.62 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -2.6% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | -0.0517 |
| Raw ev home | -0.1116 |
| Raw edge prob draw | 0.0262 |
| Raw ev draw | 0.1399 |
| Raw edge prob away | 0.0256 |
| Raw ev away | 0.1591 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **38.9%**. Expected goals are 1.42 for Leeds United and 1.30 for Manchester United (2.72 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 51.5%; Under 3.5 goals: 70.9%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 38.9% | 2.57 |
| Draw | 27.2% | 3.68 |
| Manchester United win | 33.9% | 2.95 |

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
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.96% |
| 2 | 2-1 | 8.70% |
| 3 | 1-0 | 8.15% |
| 4 | 1-2 | 8.08% |
| 5 | 0-0 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 38.9% | 39.2% | 2.60 | +1.1% |
| Draw | 27.2% | 26.2% | 3.75 | +2.0% |
| Manchester United win | 33.9% | 34.6% | 2.85 | -3.4% |
| Over 2.5 | 51.5% | 58.4% | 1.70 | -12.5% |
| Under 2.5 | 48.5% | 41.6% | 2.34 | +13.6% |

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
| Market best home last update utc | 2026-10-11T06:31:37Z |
| Market best draw last update utc | 2026-10-11T06:31:05Z |
| Market best away last update utc | 2026-10-11T06:31:05Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.17 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.44 |
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
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.40 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | -0.3% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | -0.0063 |
| Raw ev home | 0.0032 |
| Raw edge prob draw | 0.0201 |
| Raw ev draw | 0.0580 |
| Raw edge prob away | -0.0138 |
| Raw ev away | -0.0538 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **58.0%**. Expected goals are 0.77 for Nottingham Forest and 1.55 for Arsenal (2.32 combined). The most likely exact score is 0-1 at 14.8%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 42.0%; Under 3.5 goals: 79.1%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 42.9%; BTTS No (at least one team does not score): 57.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.4% | 6.09 |
| Draw | 25.5% | 3.92 |
| Arsenal win | 58.0% | 1.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.77 |
| Arsenal expected goals | 1.55 |
| Expected total goals | 2.32 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 69.1% |
| Under 1.5 | 30.9% |
| Over 2.5 | 42.0% |
| Under 2.5 | 58.0% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.84% |
| 2 | 0-2 | 12.52% |
| 3 | 1-1 | 11.82% |
| 4 | 0-0 | 10.07% |
| 5 | 1-2 | 9.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.4% | 15.5% | 6.80 | +11.7% |
| Draw | 25.5% | 23.1% | 4.10 | +4.7% |
| Arsenal win | 58.0% | 61.4% | 1.66 | -3.7% |
| Over 2.5 | 42.0% | 52.3% | 1.97 | -17.3% |
| Under 2.5 | 58.0% | 47.7% | 1.97 | +14.3% |

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
| Market best home last update utc | 2026-10-11T06:31:20Z |
| Market best draw last update utc | 2026-10-11T06:31:05Z |
| Market best away last update utc | 2026-10-11T06:31:05Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Codere (IT) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.9% |
| P btts no | 57.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.93 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.23 |
| Fair Over 2.5 odds | 2.38 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.79 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.21 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 43.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 6.00 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +0.9% |
| Draw probability edge | +2.5% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -10.3% |
| Under 2.5 probability edge | +10.3% |
| Raw edge prob home | 0.0177 |
| Raw ev home | 0.1773 |
| Raw edge prob draw | 0.0491 |
| Raw ev draw | 0.1477 |
| Raw edge prob away | -0.0667 |
| Raw ev away | -0.0921 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **67.9%**. Expected goals are 1.71 for Tottenham Hotspur and 0.34 for Coventry City (2.04 combined). The most likely exact score is 1-0 at 20.5%. Goal-market probabilities: at least one goal: 86.9%; Over 2.5 goals: 33.2%; Under 3.5 goals: 85.4%; Under 4.5 goals: 94.5%; BTTS Yes (both teams score): 24.2%; BTTS No (at least one team does not score): 75.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 67.9% | 1.47 |
| Draw | 22.1% | 4.53 |
| Coventry City win | 10.1% | 9.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.71 |
| Coventry City expected goals | 0.34 |
| Expected total goals | 2.04 |
| Over 0.5 | 86.9% |
| Under 0.5 | 13.1% |
| Over 1.5 | 60.3% |
| Under 1.5 | 39.7% |
| Over 2.5 | 33.2% |
| Under 2.5 | 66.8% |
| Over 3.5 | 14.6% |
| Under 3.5 | 85.4% |
| Over 4.5 | 5.5% |
| Under 4.5 | 94.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.45% |
| 2 | 2-0 | 18.08% |
| 3 | 0-0 | 13.15% |
| 4 | 3-0 | 10.28% |
| 5 | 1-1 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 67.9% | 64.8% | 1.54 | +4.5% |
| Draw | 22.1% | 21.0% | 4.80 | +5.9% |
| Coventry City win | 10.1% | 14.2% | 6.70 | -32.7% |
| Over 2.5 | 33.2% | 60.7% | 1.64 | -45.6% |
| Under 2.5 | 66.8% | 39.3% | 2.46 | +64.4% |

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
| Market best home last update utc | 2026-10-11T06:31:05Z |
| Market best draw last update utc | 2026-10-11T06:31:20Z |
| Market best away last update utc | 2026-10-11T06:26:54Z |
| Odds bookmakers 1x2 | 16.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 24.2% |
| P btts no | 75.8% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.61 |
| Fair Over 1.5 odds | 1.66 |
| Fair Under 1.5 odds | 2.52 |
| Fair Over 2.5 odds | 3.01 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 6.85 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.16 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 5.9% |
| Raw p over 1 5 | 61.3% |
| Raw p under 3 5 | 85.0% |
| Raw p btts yes | 24.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 1.51 |
| Reference draw odds | 4.40 |
| Reference away odds | 6.40 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.33 |
| Home probability edge | +3.1% |
| Draw probability edge | +1.0% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -27.6% |
| Under 2.5 probability edge | +27.6% |
| Raw edge prob home | 0.0615 |
| Raw ev home | 0.0927 |
| Raw edge prob draw | 0.0209 |
| Raw ev draw | 0.1094 |
| Raw edge prob away | -0.0824 |
| Raw ev away | -0.6026 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T06:37:53Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 62.0% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T06:38:06Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 55.9% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T06:38:21Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.08 |
| Market btts yes bookmakers | 2 |

</details>


---
