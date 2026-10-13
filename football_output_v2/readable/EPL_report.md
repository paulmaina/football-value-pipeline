# Premier League — football model report

Fixtures in this report: **10**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,200 |
| Training data through | 2026-10-12 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 897.623 |
| Base scoring parameter | 0.217 |
| Home-advantage parameter | 0.179 |
| Dixon-Coles low-score adjustment | -0.115 |
| Xi per day | 0.0029 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 10.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Brentford win** at **38.6%**. Expected goals are 1.58 for Brentford and 1.48 for Liverpool (3.06 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 59.1%; Under 3.5 goals: 63.4%; Double Chance 1X: 64.9%; Double Chance X2: 61.4%; Under 4.5 goals: 80.5%; BTTS Yes (both teams score): 62.5%; BTTS No (at least one team does not score): 37.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 38.6% | 2.59 |
| Draw | 26.3% | 3.80 |
| Liverpool win | 35.1% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.58 |
| Liverpool expected goals | 1.48 |
| Expected total goals | 3.06 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 82.2% |
| Under 1.5 | 17.8% |
| Over 2.5 | 59.1% |
| Under 2.5 | 40.9% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.5% |
| Under 4.5 | 80.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.14% |
| 2 | 2-1 | 8.59% |
| 3 | 1-2 | 8.24% |
| 4 | 2-2 | 6.36% |
| 5 | 1-0 | 6.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 38.6% | 38.3% | 2.61 | +0.8% |
| Draw | 26.3% | 26.1% | 3.85 | +1.3% |
| Liverpool win | 35.1% | 35.6% | 2.84 | -0.4% |
| Over 2.5 | 59.1% | 61.0% | 1.56 | -7.8% |
| Under 2.5 | 40.9% | 39.0% | 2.45 | +0.3% |

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
| Market best home last update utc | 2026-10-13T07:42:11Z |
| Market best draw last update utc | 2026-10-13T07:42:10Z |
| Market best away last update utc | 2026-10-13T07:42:10Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Nordic Bet |
| Matched home-team name | Brentford |
| Matched away-team name | Liverpool |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 62.5% |
| P btts no | 37.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.92 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.63 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.12 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 34.5% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 62.6% |
| P home draw | 64.9% |
| P draw away | 61.4% |
| Raw p home draw | 65.5% |
| Raw p draw away | 61.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.45 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.62 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +0.3% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.0069 |
| Raw ev home | 0.0168 |
| Raw edge prob draw | 0.0042 |
| Raw ev draw | 0.0214 |
| Raw edge prob away | -0.0110 |
| Raw ev away | -0.0198 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **40.1%**. Expected goals are 1.40 for Everton and 1.37 for Chelsea (2.76 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 52.7%; Under 3.5 goals: 69.9%; Double Chance 1X: 59.9%; Double Chance X2: 66.9%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 33.1% | 3.02 |
| Draw | 26.8% | 3.74 |
| Chelsea win | 40.1% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.40 |
| Chelsea expected goals | 1.37 |
| Expected total goals | 2.76 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.72% |
| 2 | 1-2 | 9.38% |
| 3 | 0-1 | 8.25% |
| 4 | 2-1 | 7.62% |
| 5 | 0-0 | 7.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 33.1% | 29.7% | 3.35 | +10.9% |
| Draw | 26.8% | 25.3% | 3.90 | +4.4% |
| Chelsea win | 40.1% | 45.1% | 2.23 | -10.5% |
| Over 2.5 | 52.7% | 57.3% | 1.73 | -8.8% |
| Under 2.5 | 47.3% | 42.7% | 2.32 | +9.7% |

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
| Market best home last update utc | 2026-10-13T07:42:10Z |
| Market best draw last update utc | 2026-10-13T07:41:42Z |
| Market best away last update utc | 2026-10-13T07:42:11Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Everton |
| Matched away-team name | Chelsea |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.71 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.73 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 36.6% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 70.0% |
| Raw p btts yes | 57.5% |
| P home draw | 59.9% |
| P draw away | 66.9% |
| Raw p home draw | 64.8% |
| Raw p draw away | 63.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 3.10 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +3.4% |
| Draw probability edge | +1.5% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | 0.0689 |
| Raw ev home | 0.2247 |
| Raw edge prob draw | 0.0299 |
| Raw ev draw | 0.1018 |
| Raw edge prob away | -0.0988 |
| Raw ev away | -0.2153 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.3%**. Expected goals are 0.94 for Fulham and 1.22 for Hull City (2.16 combined). The most likely exact score is 1-0 at 14.6%. Goal-market probabilities: at least one goal: 88.6%; Over 2.5 goals: 37.8%; Under 3.5 goals: 82.9%; Double Chance 1X: 70.3%; Double Chance X2: 57.7%; Under 4.5 goals: 93.0%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.3% | 2.36 |
| Draw | 28.0% | 3.57 |
| Hull City win | 29.7% | 3.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.94 |
| Hull City expected goals | 1.22 |
| Expected total goals | 2.16 |
| Over 0.5 | 88.6% |
| Under 0.5 | 11.4% |
| Over 1.5 | 64.9% |
| Under 1.5 | 35.1% |
| Over 2.5 | 37.8% |
| Under 2.5 | 62.2% |
| Over 3.5 | 17.1% |
| Under 3.5 | 82.9% |
| Over 4.5 | 7.0% |
| Under 4.5 | 93.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.64% |
| 2 | 1-1 | 12.85% |
| 3 | 0-0 | 11.37% |
| 4 | 2-1 | 9.78% |
| 5 | 0-1 | 9.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 42.3% | 57.6% | 1.78 | -24.7% |
| Draw | 28.0% | 23.8% | 4.30 | +20.3% |
| Hull City win | 29.7% | 18.5% | 5.18 | +54.0% |
| Over 2.5 | 37.8% | 56.4% | 1.81 | -31.6% |
| Under 2.5 | 62.2% | 43.6% | 2.20 | +36.8% |

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
| Market best home last update utc | 2026-10-13T07:42:10Z |
| Market best draw last update utc | 2026-10-13T07:42:11Z |
| Market best away last update utc | 2026-10-13T07:42:12Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Fulham |
| Matched away-team name | Hull |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 43.9% |
| P btts no | 56.1% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.80 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.85 |
| Fair Over 2.5 odds | 2.65 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.84 |
| Fair Under 3.5 odds | 1.21 |
| Fair Over 4.5 odds | 14.28 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 32.1% |
| Unadjusted away-win probability | 40.9% |
| Raw p over 1 5 | 65.1% |
| Raw p under 3 5 | 82.7% |
| Raw p btts yes | 44.5% |
| P home draw | 70.3% |
| P draw away | 57.7% |
| Raw p home draw | 59.1% |
| Raw p draw away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.67 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | -15.3% |
| Draw probability edge | +4.2% |
| Away probability edge | +11.2% |
| Over 2.5 probability edge | -18.6% |
| Under 2.5 probability edge | +18.6% |
| Raw edge prob home | -0.3070 |
| Raw ev home | -0.5204 |
| Raw edge prob draw | 0.0830 |
| Raw ev draw | 0.3815 |
| Raw edge prob away | 0.2239 |
| Raw ev away | 1.1202 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **83.4%**. Expected goals are 3.47 for Manchester City and 0.73 for Ipswich Town (4.20 combined). The most likely exact score is 3-0 at 10.1%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 77.9%; Under 3.5 goals: 40.7%; Double Chance 1X: 94.3%; Double Chance X2: 16.6%; Under 4.5 goals: 60.1%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 83.4% | 1.20 |
| Draw | 10.8% | 9.22 |
| Ipswich Town win | 5.7% | 17.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.47 |
| Ipswich Town expected goals | 0.73 |
| Expected total goals | 4.20 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 92.2% |
| Under 1.5 | 7.8% |
| Over 2.5 | 77.9% |
| Under 2.5 | 22.1% |
| Over 3.5 | 59.3% |
| Under 3.5 | 40.7% |
| Over 4.5 | 39.9% |
| Under 4.5 | 60.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.08% |
| 2 | 4-0 | 8.74% |
| 3 | 2-0 | 8.72% |
| 4 | 3-1 | 7.33% |
| 5 | 4-1 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 83.4% | 80.1% | 1.26 | +5.1% |
| Draw | 10.8% | 12.3% | 7.80 | -15.4% |
| Ipswich Town win | 5.7% | 7.6% | 14.00 | -20.0% |
| Over 2.5 | 77.9% | 71.2% | 1.38 | +7.6% |
| Under 2.5 | 22.1% | 28.8% | 3.08 | -32.1% |

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
| Market best home last update utc | 2026-10-13T07:42:12Z |
| Market best draw last update utc | 2026-10-13T07:42:10Z |
| Market best away last update utc | 2026-10-13T07:42:10Z |
| Odds bookmakers 1x2 | 25.00 |
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
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.38 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.75 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.53 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.46 |
| Fair Over 4.5 odds | 2.50 |
| Fair Under 4.5 odds | 1.67 |
| Unadjusted home-win probability | 86.8% |
| Unadjusted draw probability | 9.4% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 92.6% |
| Raw p under 3 5 | 39.7% |
| Raw p btts yes | 50.5% |
| P home draw | 94.3% |
| P draw away | 16.6% |
| Raw p home draw | 96.2% |
| Raw p draw away | 13.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.22 |
| Reference draw odds | 6.50 |
| Reference away odds | 10.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +3.4% |
| Draw probability edge | -1.5% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +6.8% |
| Under 2.5 probability edge | -6.8% |
| Raw edge prob home | 0.0675 |
| Raw ev home | 0.0938 |
| Raw edge prob draw | -0.0296 |
| Raw ev draw | -0.2694 |
| Raw edge prob away | -0.0379 |
| Raw ev away | -0.4651 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **43.3%**. Expected goals are 1.76 for Newcastle United and 1.52 for Aston Villa (3.28 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 63.7%; Under 3.5 goals: 58.4%; Double Chance 1X: 68.7%; Double Chance X2: 56.7%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 65.9%; BTTS No (at least one team does not score): 34.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 43.3% | 2.31 |
| Draw | 25.4% | 3.93 |
| Aston Villa win | 31.3% | 3.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.76 |
| Aston Villa expected goals | 1.52 |
| Expected total goals | 3.28 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 63.7% |
| Under 2.5 | 36.3% |
| Over 3.5 | 41.6% |
| Under 3.5 | 58.4% |
| Over 4.5 | 23.4% |
| Under 4.5 | 76.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.30% |
| 2 | 2-1 | 9.05% |
| 3 | 1-2 | 7.38% |
| 4 | 2-2 | 6.79% |
| 5 | 2-0 | 5.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 43.3% | 44.3% | 2.30 | -0.4% |
| Draw | 25.4% | 25.6% | 3.95 | +0.5% |
| Aston Villa win | 31.3% | 30.0% | 3.30 | +3.1% |
| Over 2.5 | 63.7% | 59.3% | 1.67 | +6.3% |
| Under 2.5 | 36.3% | 40.7% | 2.46 | -10.6% |

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
| Market best home last update utc | 2026-10-13T07:42:10Z |
| Market best draw last update utc | 2026-10-13T07:42:11Z |
| Market best away last update utc | 2026-10-13T07:42:11Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Newcastle |
| Matched away-team name | Aston Villa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.9% |
| P btts no | 34.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.21 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.71 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.40 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.27 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 32.5% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 58.4% |
| Raw p btts yes | 65.9% |
| P home draw | 68.7% |
| P draw away | 56.7% |
| Raw p home draw | 67.5% |
| Raw p draw away | 57.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.15 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -1.0% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | +4.3% |
| Under 2.5 probability edge | -4.3% |
| Raw edge prob home | -0.0204 |
| Raw ev home | -0.0274 |
| Raw edge prob draw | -0.0037 |
| Raw ev draw | -0.0024 |
| Raw edge prob away | 0.0242 |
| Raw ev away | 0.0712 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **48.0%**. Expected goals are 1.59 for Bournemouth and 1.06 for Sunderland (2.65 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 49.6%; Under 3.5 goals: 72.5%; Double Chance 1X: 75.0%; Double Chance X2: 52.0%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 53.2%; BTTS No (at least one team does not score): 46.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 48.0% | 2.08 |
| Draw | 27.0% | 3.71 |
| Sunderland win | 25.0% | 3.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.59 |
| Sunderland expected goals | 1.06 |
| Expected total goals | 2.65 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 75.6% |
| Under 1.5 | 24.4% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 27.5% |
| Under 3.5 | 72.5% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.90% |
| 2 | 1-0 | 9.81% |
| 3 | 2-1 | 9.40% |
| 4 | 2-0 | 8.88% |
| 5 | 0-0 | 8.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 48.0% | 47.6% | 2.14 | +2.7% |
| Draw | 27.0% | 26.2% | 3.75 | +1.2% |
| Sunderland win | 25.0% | 26.2% | 3.85 | -3.6% |
| Over 2.5 | 49.6% | 53.1% | 1.88 | -6.7% |
| Under 2.5 | 50.4% | 46.9% | 2.08 | +4.7% |

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
| Market best home last update utc | 2026-10-13T07:42:10Z |
| Market best draw last update utc | 2026-10-13T07:42:12Z |
| Market best away last update utc | 2026-10-13T07:42:12Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Bournemouth |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 53.2% |
| P btts no | 46.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.18 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.09 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.68 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 53.4% |
| P home draw | 75.0% |
| P draw away | 52.0% |
| Raw p home draw | 76.1% |
| Raw p draw away | 51.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.00 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 1.95 |
| Home probability edge | +0.3% |
| Draw probability edge | +0.8% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0069 |
| Raw ev home | 0.0342 |
| Raw edge prob draw | 0.0161 |
| Raw ev draw | 0.0420 |
| Raw edge prob away | -0.0229 |
| Raw ev away | -0.0803 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **59.7%**. Expected goals are 2.00 for Brighton and Hove Albion and 1.02 for Crystal Palace (3.02 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.6%; Under 3.5 goals: 64.1%; Double Chance 1X: 82.3%; Double Chance X2: 40.3%; Under 4.5 goals: 81.0%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 59.7% | 1.67 |
| Draw | 22.5% | 4.44 |
| Crystal Palace win | 17.7% | 5.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 2.00 |
| Crystal Palace expected goals | 1.02 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 58.6% |
| Under 2.5 | 41.4% |
| Over 3.5 | 35.9% |
| Under 3.5 | 64.1% |
| Over 4.5 | 19.0% |
| Under 4.5 | 81.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.64% |
| 2 | 2-1 | 10.09% |
| 3 | 2-0 | 9.89% |
| 4 | 1-0 | 8.72% |
| 5 | 3-1 | 6.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 59.7% | 60.5% | 1.63 | -2.6% |
| Draw | 22.5% | 21.6% | 4.65 | +4.8% |
| Crystal Palace win | 17.7% | 17.9% | 5.90 | +4.5% |
| Over 2.5 | 58.6% | 61.6% | 1.63 | -4.6% |
| Under 2.5 | 41.4% | 38.4% | 2.50 | +3.6% |

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
| Market best home last update utc | 2026-10-13T07:42:12Z |
| Market best draw last update utc | 2026-10-13T07:42:11Z |
| Market best away last update utc | 2026-10-13T07:42:10Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.32 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.45 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.26 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 59.0% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 17.5% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 56.5% |
| P home draw | 82.3% |
| P draw away | 40.3% |
| Raw p home draw | 82.5% |
| Raw p draw away | 41.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.60 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -0.8% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | -0.0154 |
| Raw ev home | -0.0386 |
| Raw edge prob draw | 0.0193 |
| Raw ev draw | 0.0930 |
| Raw edge prob away | -0.0039 |
| Raw ev away | 0.0334 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **38.4%**. Expected goals are 1.42 for Leeds United and 1.28 for Manchester United (2.70 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.4%; Double Chance 1X: 66.0%; Double Chance X2: 61.6%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 38.4% | 2.61 |
| Draw | 27.6% | 3.62 |
| Manchester United win | 34.0% | 2.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.28 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 76.6% |
| Under 1.5 | 23.4% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.6% |
| Under 3.5 | 71.4% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.18% |
| 2 | 2-1 | 8.56% |
| 3 | 1-2 | 8.16% |
| 4 | 1-0 | 8.04% |
| 5 | 0-0 | 7.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 38.4% | 38.0% | 2.62 | +0.6% |
| Draw | 27.6% | 26.7% | 3.80 | +5.0% |
| Manchester United win | 34.0% | 35.3% | 2.86 | -2.8% |
| Over 2.5 | 50.9% | 58.4% | 1.73 | -11.9% |
| Under 2.5 | 49.1% | 41.6% | 2.34 | +14.8% |

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
| Market best home last update utc | 2026-10-13T07:42:12Z |
| Market best draw last update utc | 2026-10-13T07:41:42Z |
| Market best away last update utc | 2026-10-13T07:42:10Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.70 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.27 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.25 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 76.5% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 56.1% |
| P home draw | 66.0% |
| P draw away | 61.6% |
| Raw p home draw | 67.4% |
| Raw p draw away | 61.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.45 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.62 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +0.4% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | 0.0077 |
| Raw ev home | 0.0156 |
| Raw edge prob draw | 0.0192 |
| Raw ev draw | 0.0864 |
| Raw edge prob away | -0.0269 |
| Raw ev away | -0.0663 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **57.0%**. Expected goals are 0.76 for Nottingham Forest and 1.53 for Arsenal (2.29 combined). The most likely exact score is 0-1 at 14.8%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 41.0%; Under 3.5 goals: 79.8%; Double Chance 1X: 43.0%; Double Chance X2: 83.7%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 42.7%; BTTS No (at least one team does not score): 57.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.3% | 6.12 |
| Draw | 26.7% | 3.75 |
| Arsenal win | 57.0% | 1.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.76 |
| Arsenal expected goals | 1.53 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 68.5% |
| Under 1.5 | 31.5% |
| Over 2.5 | 41.0% |
| Under 2.5 | 59.0% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.82% |
| 2 | 0-2 | 12.43% |
| 3 | 1-1 | 12.30% |
| 4 | 0-0 | 10.72% |
| 5 | 1-2 | 9.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.3% | 15.4% | 6.80 | +11.1% |
| Draw | 26.7% | 24.8% | 4.20 | +12.1% |
| Arsenal win | 57.0% | 59.8% | 1.66 | -5.4% |
| Over 2.5 | 41.0% | 50.0% | 1.97 | -19.3% |
| Under 2.5 | 59.0% | 50.0% | 2.00 | +18.1% |

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
| Market best home last update utc | 2026-10-13T07:42:25Z |
| Market best draw last update utc | 2026-10-13T07:42:10Z |
| Market best away last update utc | 2026-10-13T07:42:12Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Matchbook |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.7% |
| P btts no | 57.3% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.33 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.95 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.77 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 54.2% |
| Raw p over 1 5 | 68.1% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 43.2% |
| P home draw | 43.0% |
| P draw away | 83.7% |
| Raw p home draw | 45.8% |
| Raw p draw away | 82.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 5.80 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.62 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | +1.0% |
| Draw probability edge | +1.9% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | 0.0192 |
| Raw ev home | 0.1760 |
| Raw edge prob draw | 0.0373 |
| Raw ev draw | 0.1988 |
| Raw edge prob away | -0.0565 |
| Raw ev away | -0.1009 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **55.5%**. Expected goals are 1.43 for Tottenham Hotspur and 1.06 for Coventry City (2.49 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 47.4%; Under 3.5 goals: 75.4%; Double Chance 1X: 79.5%; Double Chance X2: 44.5%; Under 4.5 goals: 88.6%; BTTS Yes (both teams score): 49.6%; BTTS No (at least one team does not score): 50.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 55.5% | 1.80 |
| Draw | 24.1% | 4.16 |
| Coventry City win | 20.5% | 4.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.43 |
| Coventry City expected goals | 1.06 |
| Expected total goals | 2.49 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 73.2% |
| Under 1.5 | 26.8% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 11.4% |
| Under 4.5 | 88.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.14% |
| 2 | 1-1 | 11.46% |
| 3 | 2-1 | 11.30% |
| 4 | 2-0 | 10.69% |
| 5 | 0-0 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 55.5% | 66.9% | 1.54 | -14.5% |
| Draw | 24.1% | 18.7% | 4.80 | +15.5% |
| Coventry City win | 20.5% | 14.4% | 6.76 | +38.2% |
| Over 2.5 | 47.4% | 60.5% | 1.64 | -22.2% |
| Under 2.5 | 52.6% | 39.5% | 2.48 | +30.4% |

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
| Market best home last update utc | 2026-10-13T07:42:13Z |
| Market best draw last update utc | 2026-10-13T07:41:30Z |
| Market best away last update utc | 2026-10-13T07:42:10Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Betsson |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 49.6% |
| P btts no | 50.4% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.51 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.73 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 4.06 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.76 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 44.1% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 26.5% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 76.1% |
| Raw p btts yes | 51.1% |
| P home draw | 79.5% |
| P draw away | 44.5% |
| Raw p home draw | 73.5% |
| Raw p draw away | 55.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.43 |
| Reference draw odds | 4.45 |
| Reference away odds | 5.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | -11.4% |
| Draw probability edge | +5.4% |
| Away probability edge | +6.0% |
| Over 2.5 probability edge | -13.0% |
| Under 2.5 probability edge | +13.0% |
| Raw edge prob home | -0.2281 |
| Raw ev home | -0.3210 |
| Raw edge prob draw | 0.1075 |
| Raw ev draw | 0.4127 |
| Raw edge prob away | 0.1205 |
| Raw ev away | 0.7899 |

</details>


---
