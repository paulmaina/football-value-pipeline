# Premier League — football model report

Fixtures in this report: **10**.

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
| Live odds matched | 10.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 0.00 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **37.6%**. Expected goals are 1.48 for Brentford and 1.63 for Liverpool (3.11 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 60.1%; Under 3.5 goals: 62.2%; Double Chance 1X: 62.4%; Double Chance X2: 63.8%; Under 4.5 goals: 79.6%; BTTS Yes (both teams score): 63.4%; BTTS No (at least one team does not score): 36.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 36.2% | 2.76 |
| Draw | 26.1% | 3.82 |
| Liverpool win | 37.6% | 2.66 |

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
| 1 | 1-1 | 11.95% |
| 2 | 2-1 | 8.54% |
| 3 | 1-2 | 8.20% |
| 4 | 2-2 | 6.54% |
| 5 | 1-0 | 5.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 36.2% | 38.6% | 2.61 | -5.4% |
| Draw | 26.1% | 26.3% | 3.85 | +0.7% |
| Liverpool win | 37.6% | 35.0% | 2.86 | +7.6% |
| Over 2.5 | 60.1% | 62.2% | 1.56 | -6.2% |
| Under 2.5 | 39.9% | 37.8% | 2.45 | -2.2% |

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
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:34Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
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
| P btts yes | 63.4% |
| P btts no | 36.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.84 |
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
| P home draw | 62.4% |
| P draw away | 63.8% |
| Raw p home draw | 59.8% |
| Raw p draw away | 66.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.51 |
| Reference draw odds | 3.64 |
| Reference away odds | 2.76 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -2.4% |
| Draw probability edge | -0.2% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.0483 |
| Raw ev home | -0.1173 |
| Raw edge prob draw | -0.0035 |
| Raw ev draw | 0.0000 |
| Raw edge prob away | 0.0517 |
| Raw ev away | 0.1499 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **39.8%**. Expected goals are 1.28 for Everton and 1.29 for Chelsea (2.57 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 48.1%; Under 3.5 goals: 74.1%; Double Chance 1X: 60.2%; Double Chance X2: 67.3%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 53.3%; BTTS No (at least one team does not score): 46.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 32.7% | 3.06 |
| Draw | 27.5% | 3.64 |
| Chelsea win | 39.8% | 2.51 |

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
| 1 | 1-1 | 13.14% |
| 2 | 0-1 | 9.53% |
| 3 | 1-2 | 9.12% |
| 4 | 0-0 | 8.43% |
| 5 | 1-0 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 32.7% | 30.1% | 3.30 | +7.9% |
| Draw | 27.5% | 25.8% | 4.00 | +10.0% |
| Chelsea win | 39.8% | 44.1% | 2.26 | -10.1% |
| Over 2.5 | 48.1% | 57.0% | 1.73 | -16.8% |
| Under 2.5 | 51.9% | 43.0% | 2.33 | +20.9% |

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
| Market best home last update utc | 2026-10-12T21:08:04Z |
| Market best draw last update utc | 2026-10-12T21:07:50Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | LeoVegas (SE) |
| Matched home-team name | Everton |
| Matched away-team name | Chelsea |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 53.3% |
| P btts no | 46.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.87 |
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
| P home draw | 60.2% |
| P draw away | 67.3% |
| Raw p home draw | 64.5% |
| Raw p draw away | 64.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 3.19 |
| Reference draw odds | 3.71 |
| Reference away odds | 2.21 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +2.6% |
| Draw probability edge | +1.7% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | 0.0512 |
| Raw ev home | 0.1639 |
| Raw edge prob draw | 0.0340 |
| Raw ev draw | 0.1677 |
| Raw edge prob away | -0.0852 |
| Raw ev away | -0.1969 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.6%**. Expected goals are 0.85 for Fulham and 1.07 for Hull City (1.92 combined). The most likely exact score is 1-0 at 17.4%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 31.7%; Under 3.5 goals: 87.2%; Double Chance 1X: 71.1%; Double Chance X2: 57.4%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 38.0%; BTTS No (at least one team does not score): 62.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.6% | 2.35 |
| Draw | 28.5% | 3.51 |
| Hull City win | 28.9% | 3.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.85 |
| Hull City expected goals | 1.07 |
| Expected total goals | 1.92 |
| Over 0.5 | 86.6% |
| Under 0.5 | 13.4% |
| Over 1.5 | 58.5% |
| Under 1.5 | 41.5% |
| Over 2.5 | 31.7% |
| Under 2.5 | 68.3% |
| Over 3.5 | 12.8% |
| Under 3.5 | 87.2% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.44% |
| 2 | 0-0 | 13.38% |
| 3 | 1-1 | 12.27% |
| 4 | 0-1 | 10.65% |
| 5 | 2-1 | 8.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 42.6% | 58.3% | 1.76 | -25.0% |
| Draw | 28.5% | 22.8% | 4.30 | +22.3% |
| Hull City win | 28.9% | 18.9% | 5.18 | +49.9% |
| Over 2.5 | 31.7% | 55.3% | 1.81 | -42.7% |
| Under 2.5 | 68.3% | 44.7% | 2.20 | +50.3% |

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
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:34Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
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
| P btts yes | 38.0% |
| P btts no | 62.0% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.47 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.41 |
| Fair Over 2.5 odds | 3.16 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.79 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.89 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 34.1% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 87.1% |
| Raw p btts yes | 39.0% |
| P home draw | 71.1% |
| P draw away | 57.4% |
| Raw p home draw | 61.0% |
| Raw p draw away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.68 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.97 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.11 |
| Home probability edge | -15.7% |
| Draw probability edge | +5.7% |
| Away probability edge | +10.0% |
| Over 2.5 probability edge | -23.7% |
| Under 2.5 probability edge | +23.7% |
| Raw edge prob home | -0.3142 |
| Raw ev home | -0.5264 |
| Raw edge prob draw | 0.1133 |
| Raw ev draw | 0.4671 |
| Raw edge prob away | 0.2008 |
| Raw ev away | 1.0189 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **83.8%**. Expected goals are 3.46 for Manchester City and 0.70 for Ipswich Town (4.15 combined). The most likely exact score is 3-0 at 10.4%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 77.4%; Under 3.5 goals: 41.5%; Double Chance 1X: 94.2%; Double Chance X2: 16.2%; Under 4.5 goals: 60.8%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 83.8% | 1.19 |
| Draw | 10.4% | 9.60 |
| Ipswich Town win | 5.8% | 17.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.46 |
| Ipswich Town expected goals | 0.70 |
| Expected total goals | 4.15 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 91.8% |
| Under 1.5 | 8.2% |
| Over 2.5 | 77.4% |
| Under 2.5 | 22.6% |
| Over 3.5 | 58.5% |
| Under 3.5 | 41.5% |
| Over 4.5 | 39.2% |
| Under 4.5 | 60.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.39% |
| 2 | 2-0 | 9.02% |
| 3 | 4-0 | 8.98% |
| 4 | 3-1 | 7.25% |
| 5 | 2-1 | 6.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 83.8% | 80.3% | 1.26 | +5.5% |
| Draw | 10.4% | 11.7% | 8.20 | -14.6% |
| Ipswich Town win | 5.8% | 8.0% | 13.50 | -21.3% |
| Over 2.5 | 77.4% | 70.4% | 1.38 | +6.8% |
| Under 2.5 | 22.6% | 29.6% | 3.08 | -30.5% |

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
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:34Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
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
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.66 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.21 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.43 |
| Fair Over 3.5 odds | 1.71 |
| Fair Under 3.5 odds | 2.41 |
| Fair Over 4.5 odds | 2.55 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 87.2% |
| Unadjusted draw probability | 9.1% |
| Unadjusted away-win probability | 3.7% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.4% |
| Raw p btts yes | 49.0% |
| P home draw | 94.2% |
| P draw away | 16.2% |
| Raw p home draw | 96.3% |
| Raw p draw away | 12.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.23 |
| Reference draw odds | 7.60 |
| Reference away odds | 10.85 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | +3.4% |
| Draw probability edge | -1.3% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +7.1% |
| Under 2.5 probability edge | -7.1% |
| Raw edge prob home | 0.0688 |
| Raw ev home | 0.0987 |
| Raw edge prob draw | -0.0253 |
| Raw ev draw | -0.2500 |
| Raw edge prob away | -0.0436 |
| Raw ev away | -0.5067 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **45.0%**. Expected goals are 1.77 for Newcastle United and 1.44 for Aston Villa (3.21 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 62.2%; Under 3.5 goals: 60.1%; Double Chance 1X: 70.1%; Double Chance X2: 55.0%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 64.3%; BTTS No (at least one team does not score): 35.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 45.0% | 2.22 |
| Draw | 25.1% | 3.98 |
| Aston Villa win | 29.9% | 3.35 |

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
| Over 3.5 | 39.9% |
| Under 3.5 | 60.1% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.33% |
| 2 | 2-1 | 9.23% |
| 3 | 1-2 | 7.28% |
| 4 | 2-2 | 6.53% |
| 5 | 2-0 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 45.0% | 45.6% | 2.28 | +2.6% |
| Draw | 25.1% | 25.0% | 3.95 | -0.7% |
| Aston Villa win | 29.9% | 29.4% | 3.35 | +0.0% |
| Over 2.5 | 62.2% | 60.0% | 1.65 | +2.7% |
| Under 2.5 | 37.8% | 40.0% | 2.46 | -7.0% |

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
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:34Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Newcastle |
| Matched away-team name | Aston Villa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.3% |
| P btts no | 35.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.59 |
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
| P home draw | 70.1% |
| P draw away | 55.0% |
| Raw p home draw | 69.6% |
| Raw p draw away | 55.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.17 |
| Reference draw odds | 3.92 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -0.6% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | -0.0119 |
| Raw ev home | 0.0125 |
| Raw edge prob draw | 0.0019 |
| Raw ev draw | -0.0036 |
| Raw edge prob away | 0.0101 |
| Raw ev away | 0.0173 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.7%**. Expected goals are 1.53 for Bournemouth and 1.04 for Sunderland (2.57 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 47.9%; Under 3.5 goals: 74.1%; Double Chance 1X: 74.8%; Double Chance X2: 52.3%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.7% | 2.10 |
| Draw | 27.1% | 3.69 |
| Sunderland win | 25.2% | 3.97 |

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
| 1 | 1-1 | 12.94% |
| 2 | 1-0 | 10.49% |
| 3 | 2-1 | 9.40% |
| 4 | 2-0 | 9.01% |
| 5 | 0-0 | 8.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.7% | 48.1% | 2.12 | +1.1% |
| Draw | 27.1% | 26.0% | 3.75 | +1.6% |
| Sunderland win | 25.2% | 25.9% | 3.85 | -2.9% |
| Over 2.5 | 47.9% | 52.8% | 1.88 | -10.0% |
| Under 2.5 | 52.1% | 47.2% | 2.08 | +8.4% |

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
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:34Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
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
| Fair Over 4.5 odds | 8.33 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 74.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 52.0% |
| P home draw | 74.8% |
| P draw away | 52.3% |
| Raw p home draw | 75.4% |
| Raw p draw away | 52.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.03 |
| Reference draw odds | 3.68 |
| Reference away odds | 3.70 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.01 |
| Home probability edge | -0.4% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0084 |
| Raw ev home | 0.0021 |
| Raw edge prob draw | 0.0215 |
| Raw ev draw | 0.0562 |
| Raw edge prob away | -0.0131 |
| Raw ev away | -0.0543 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **58.2%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 57.1%; Under 3.5 goals: 65.9%; Double Chance 1X: 80.8%; Double Chance X2: 41.8%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 58.2% | 1.72 |
| Draw | 22.6% | 4.42 |
| Crystal Palace win | 19.2% | 5.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 1.85 |
| Crystal Palace expected goals | 1.08 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.1% |
| Under 3.5 | 65.9% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.70% |
| 2 | 2-1 | 10.60% |
| 3 | 2-0 | 9.80% |
| 4 | 1-0 | 9.41% |
| 5 | 3-1 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 58.2% | 62.2% | 1.63 | -5.1% |
| Draw | 22.6% | 20.3% | 4.65 | +5.2% |
| Crystal Palace win | 19.2% | 17.5% | 5.90 | +13.1% |
| Over 2.5 | 57.1% | 60.7% | 1.63 | -7.0% |
| Under 2.5 | 42.9% | 39.3% | 2.50 | +7.4% |

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
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:35Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.04 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.11 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.93 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.63 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 54.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 80.1% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 56.8% |
| P home draw | 80.8% |
| P draw away | 41.8% |
| Raw p home draw | 79.1% |
| Raw p draw away | 45.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.58 |
| Reference draw odds | 4.65 |
| Reference away odds | 5.38 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.49 |
| Home probability edge | -4.0% |
| Draw probability edge | +2.3% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | -0.0805 |
| Raw ev home | -0.1170 |
| Raw edge prob draw | 0.0463 |
| Raw ev draw | 0.1599 |
| Raw edge prob away | 0.0342 |
| Raw ev away | 0.2322 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **38.1%**. Expected goals are 1.42 for Leeds United and 1.30 for Manchester United (2.72 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 51.5%; Under 3.5 goals: 71.0%; Double Chance 1X: 65.3%; Double Chance X2: 61.9%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 38.1% | 2.62 |
| Draw | 27.2% | 3.68 |
| Manchester United win | 34.7% | 2.89 |

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
| 1 | 1-1 | 12.95% |
| 2 | 2-1 | 8.53% |
| 3 | 1-2 | 8.26% |
| 4 | 1-0 | 7.99% |
| 5 | 0-1 | 7.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 38.1% | 37.7% | 2.62 | -0.1% |
| Draw | 27.2% | 26.2% | 3.75 | +2.0% |
| Manchester United win | 34.7% | 36.1% | 2.86 | -0.9% |
| Over 2.5 | 51.5% | 58.1% | 1.73 | -11.0% |
| Under 2.5 | 48.5% | 41.9% | 2.34 | +13.6% |

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
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:07:50Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
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
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.18 |
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
| P home draw | 65.3% |
| P draw away | 61.9% |
| Raw p home draw | 66.8% |
| Raw p draw away | 61.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.57 |
| Reference draw odds | 3.66 |
| Reference away odds | 2.68 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.34 |
| Home probability edge | +0.4% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | 0.0087 |
| Raw ev home | 0.0109 |
| Raw edge prob draw | 0.0204 |
| Raw ev draw | 0.0580 |
| Raw edge prob away | -0.0291 |
| Raw ev away | -0.0505 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **58.5%**. Expected goals are 0.77 for Nottingham Forest and 1.55 for Arsenal (2.32 combined). The most likely exact score is 0-1 at 15.0%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 41.9%; Under 3.5 goals: 79.1%; Double Chance 1X: 41.5%; Double Chance X2: 84.2%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 42.9%; BTTS No (at least one team does not score): 57.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 15.8% | 6.34 |
| Draw | 25.8% | 3.88 |
| Arsenal win | 58.5% | 1.71 |

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
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.95% |
| 2 | 0-2 | 12.62% |
| 3 | 1-1 | 11.92% |
| 4 | 0-0 | 10.15% |
| 5 | 1-2 | 9.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 15.8% | 14.2% | 6.80 | +7.3% |
| Draw | 25.8% | 23.5% | 4.20 | +8.2% |
| Arsenal win | 58.5% | 62.2% | 1.66 | -2.9% |
| Over 2.5 | 41.9% | 49.4% | 1.97 | -17.4% |
| Under 2.5 | 58.1% | 50.6% | 2.00 | +16.1% |

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
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:34Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.9% |
| P btts no | 57.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.85 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.24 |
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
| P home draw | 41.5% |
| P draw away | 84.2% |
| Raw p home draw | 45.3% |
| Raw p draw away | 82.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 6.55 |
| Reference draw odds | 4.04 |
| Reference away odds | 1.58 |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.89 |
| Home probability edge | +1.5% |
| Draw probability edge | +2.2% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | 0.0306 |
| Raw ev home | 0.1773 |
| Raw edge prob draw | 0.0448 |
| Raw ev draw | 0.1757 |
| Raw edge prob away | -0.0754 |
| Raw ev away | -0.0921 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **67.7%**. Expected goals are 1.71 for Tottenham Hotspur and 0.34 for Coventry City (2.04 combined). The most likely exact score is 1-0 at 20.4%. Goal-market probabilities: at least one goal: 87.0%; Over 2.5 goals: 33.2%; Under 3.5 goals: 85.4%; Double Chance 1X: 89.6%; Double Chance X2: 32.3%; Under 4.5 goals: 94.5%; BTTS Yes (both teams score): 24.1%; BTTS No (at least one team does not score): 75.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 67.7% | 1.48 |
| Draw | 21.9% | 4.57 |
| Coventry City win | 10.4% | 9.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.71 |
| Coventry City expected goals | 0.34 |
| Expected total goals | 2.04 |
| Over 0.5 | 87.0% |
| Under 0.5 | 13.0% |
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
| 1 | 1-0 | 20.40% |
| 2 | 2-0 | 18.03% |
| 3 | 0-0 | 13.03% |
| 4 | 3-0 | 10.25% |
| 5 | 1-1 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 67.7% | 64.4% | 1.54 | +4.3% |
| Draw | 21.9% | 20.6% | 4.90 | +7.1% |
| Coventry City win | 10.4% | 15.0% | 6.76 | -29.4% |
| Over 2.5 | 33.2% | 60.2% | 1.64 | -45.6% |
| Under 2.5 | 66.8% | 39.8% | 2.48 | +65.7% |

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
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:05Z |
| Market best away last update utc | 2026-10-12T21:08:07Z |
| Odds bookmakers 1x2 | 22.00 |
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
| P btts yes | 24.1% |
| P btts no | 75.9% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.68 |
| Fair Over 1.5 odds | 1.66 |
| Fair Under 1.5 odds | 2.52 |
| Fair Over 2.5 odds | 3.01 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 6.86 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.18 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 5.9% |
| Raw p over 1 5 | 61.3% |
| Raw p under 3 5 | 85.0% |
| Raw p btts yes | 24.1% |
| P home draw | 89.6% |
| P draw away | 32.3% |
| Raw p home draw | 94.1% |
| Raw p draw away | 29.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.54 |
| Reference draw odds | 4.72 |
| Reference away odds | 6.47 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Home probability edge | +3.3% |
| Draw probability edge | +1.3% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -27.0% |
| Under 2.5 probability edge | +27.0% |
| Raw edge prob home | 0.0652 |
| Raw ev home | 0.0927 |
| Raw edge prob draw | 0.0250 |
| Raw ev draw | 0.1325 |
| Raw edge prob away | -0.0902 |
| Raw ev away | -0.5991 |

</details>


---
