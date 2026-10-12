# Premier League — football model report

Fixtures in this report: **11**.

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
| Live odds matched | 11.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 1.00 |
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

## 2026-10-12 — Coventry City vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **59.1%**. Expected goals are 0.36 for Coventry City and 1.82 for Newcastle United (2.18 combined). The most likely exact score is 0-1 at 16.1%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 34.6%; Under 3.5 goals: 84.4%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 27.8%; BTTS No (at least one team does not score): 72.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 17.2% | 5.80 |
| Draw | 23.7% | 4.22 |
| Newcastle United win | 59.1% | 1.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 0.36 |
| Newcastle United expected goals | 1.82 |
| Expected total goals | 2.18 |
| Over 0.5 | 86.8% |
| Under 0.5 | 13.2% |
| Over 1.5 | 61.0% |
| Under 1.5 | 39.0% |
| Over 2.5 | 34.6% |
| Under 2.5 | 65.4% |
| Over 3.5 | 15.6% |
| Under 3.5 | 84.4% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.08% |
| 2 | 0-2 | 15.20% |
| 3 | 0-0 | 13.19% |
| 4 | 1-0 | 9.73% |
| 5 | 0-3 | 9.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 17.2% | 28.6% | 3.60 | -38.0% |
| Draw | 23.7% | 25.7% | 3.80 | -10.0% |
| Newcastle United win | 59.1% | 45.7% | 2.19 | +29.4% |
| Over 2.5 | 34.6% | 59.7% | 1.72 | -40.5% |
| Under 2.5 | 65.4% | 40.3% | 2.35 | +53.7% |

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
| Market best home last update utc | 2026-10-12T16:30:08Z |
| Market best draw last update utc | 2026-10-12T16:30:23Z |
| Market best away last update utc | 2026-10-12T16:30:08Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Tipico |
| Matched home-team name | Coventry |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 27.8% |
| P btts no | 72.2% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.58 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.56 |
| Fair Over 2.5 odds | 2.89 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.41 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 16.16 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 72.5% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 26.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.11 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.21 |
| Home probability edge | -11.4% |
| Draw probability edge | -2.0% |
| Away probability edge | +13.4% |
| Over 2.5 probability edge | -25.1% |
| Under 2.5 probability edge | +25.1% |
| Raw edge prob home | -0.2271 |
| Raw ev home | -0.7883 |
| Raw edge prob draw | -0.0409 |
| Raw ev draw | -0.1782 |
| Raw edge prob away | 0.2680 |
| Raw ev away | 0.5876 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-12T16:29:40Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-12T16:29:40Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 62.3% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-12T16:30:23Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.40 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **37.7%**. Expected goals are 1.48 for Brentford and 1.63 for Liverpool (3.11 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 60.3%; Under 3.5 goals: 62.2%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 36.6% | 2.73 |
| Draw | 25.7% | 3.90 |
| Liverpool win | 37.7% | 2.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.48 |
| Liverpool expected goals | 1.63 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
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
| 2 | 2-1 | 8.62% |
| 3 | 1-2 | 8.22% |
| 4 | 2-2 | 6.42% |
| 5 | 1-0 | 5.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 36.6% | 39.4% | 2.61 | -4.5% |
| Draw | 25.7% | 25.3% | 3.85 | -1.2% |
| Liverpool win | 37.7% | 35.3% | 2.88 | +8.7% |
| Over 2.5 | 60.3% | 61.9% | 1.56 | -6.0% |
| Under 2.5 | 39.7% | 38.1% | 2.45 | -2.7% |

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
| Market best home last update utc | 2026-10-12T16:30:08Z |
| Market best draw last update utc | 2026-10-12T16:30:08Z |
| Market best away last update utc | 2026-10-12T16:30:23Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Nordic Bet |
| Matched home-team name | Brentford |
| Matched away-team name | Liverpool |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.18 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.83 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.65 |
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
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.43 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -2.8% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0557 |
| Raw ev home | -0.1173 |
| Raw edge prob draw | 0.0063 |
| Raw ev draw | 0.0000 |
| Raw edge prob away | 0.0494 |
| Raw ev away | 0.1580 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **40.0%**. Expected goals are 1.28 for Everton and 1.29 for Chelsea (2.57 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 48.2%; Under 3.5 goals: 74.1%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 53.3%; BTTS No (at least one team does not score): 46.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 32.7% | 3.06 |
| Draw | 27.3% | 3.66 |
| Chelsea win | 40.0% | 2.50 |

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
| Over 2.5 | 48.2% |
| Under 2.5 | 51.8% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.05% |
| 2 | 0-1 | 9.58% |
| 3 | 1-2 | 9.16% |
| 4 | 0-0 | 8.37% |
| 5 | 1-0 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 32.7% | 30.1% | 3.25 | +6.2% |
| Draw | 27.3% | 25.4% | 4.00 | +9.3% |
| Chelsea win | 40.0% | 44.5% | 2.26 | -9.6% |
| Over 2.5 | 48.2% | 57.9% | 1.73 | -16.6% |
| Under 2.5 | 51.8% | 42.1% | 2.33 | +20.7% |

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
| Market best home last update utc | 2026-10-12T16:30:08Z |
| Market best draw last update utc | 2026-10-12T16:30:23Z |
| Market best away last update utc | 2026-10-12T16:30:08Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
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
| Fair Under 0.5 odds | 11.94 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.88 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.26 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 53.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.15 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.17 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.13 |
| Home probability edge | +2.6% |
| Draw probability edge | +1.9% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -9.8% |
| Under 2.5 probability edge | +9.8% |
| Raw edge prob home | 0.0517 |
| Raw ev home | 0.1463 |
| Raw edge prob draw | 0.0376 |
| Raw ev draw | 0.1677 |
| Raw edge prob away | -0.0892 |
| Raw ev away | -0.1969 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.2%**. Expected goals are 0.85 for Fulham and 1.07 for Hull City (1.92 combined). The most likely exact score is 1-0 at 17.3%. Goal-market probabilities: at least one goal: 86.4%; Over 2.5 goals: 31.5%; Under 3.5 goals: 87.2%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 38.1%; BTTS No (at least one team does not score): 61.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.2% | 2.37 |
| Draw | 28.9% | 3.46 |
| Hull City win | 28.8% | 3.47 |

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
| 1 | 1-0 | 17.28% |
| 2 | 0-0 | 13.61% |
| 3 | 1-1 | 12.48% |
| 4 | 0-1 | 10.61% |
| 5 | 2-1 | 8.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 42.2% | 57.6% | 1.74 | -26.5% |
| Draw | 28.9% | 23.8% | 4.30 | +24.4% |
| Hull City win | 28.8% | 18.7% | 5.18 | +49.3% |
| Over 2.5 | 31.5% | 55.4% | 1.81 | -42.9% |
| Under 2.5 | 68.5% | 44.6% | 2.18 | +49.3% |

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
| Market best home last update utc | 2026-10-12T16:30:08Z |
| Market best draw last update utc | 2026-10-12T16:30:23Z |
| Market best away last update utc | 2026-10-12T16:30:08Z |
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
| P btts yes | 38.1% |
| P btts no | 61.9% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.35 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.41 |
| Fair Over 2.5 odds | 3.17 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.80 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 21.00 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 34.1% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 87.1% |
| Raw p btts yes | 39.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.67 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.75 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.03 |
| Home probability edge | -15.3% |
| Draw probability edge | +5.2% |
| Away probability edge | +10.1% |
| Over 2.5 probability edge | -23.8% |
| Under 2.5 probability edge | +23.8% |
| Raw edge prob home | -0.3066 |
| Raw ev home | -0.5318 |
| Raw edge prob draw | 0.1037 |
| Raw ev draw | 0.4671 |
| Raw edge prob away | 0.2030 |
| Raw ev away | 1.0189 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **83.6%**. Expected goals are 3.46 for Manchester City and 0.70 for Ipswich Town (4.15 combined). The most likely exact score is 3-0 at 10.4%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 77.3%; Under 3.5 goals: 41.5%; Under 4.5 goals: 60.9%; BTTS Yes (both teams score): 50.0%; BTTS No (at least one team does not score): 50.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 83.6% | 1.20 |
| Draw | 10.7% | 9.31 |
| Ipswich Town win | 5.6% | 17.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.46 |
| Ipswich Town expected goals | 0.70 |
| Expected total goals | 4.15 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 91.8% |
| Under 1.5 | 8.2% |
| Over 2.5 | 77.3% |
| Under 2.5 | 22.7% |
| Over 3.5 | 58.5% |
| Under 3.5 | 41.5% |
| Over 4.5 | 39.1% |
| Under 4.5 | 60.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.37% |
| 2 | 2-0 | 9.00% |
| 3 | 4-0 | 8.97% |
| 4 | 3-1 | 7.23% |
| 5 | 2-1 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 83.6% | 80.1% | 1.26 | +5.4% |
| Draw | 10.7% | 12.3% | 8.20 | -12.0% |
| Ipswich Town win | 5.6% | 7.6% | 13.50 | -23.9% |
| Over 2.5 | 77.3% | 70.5% | 1.38 | +6.7% |
| Under 2.5 | 22.7% | 29.5% | 3.08 | -30.0% |

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
| Market best home last update utc | 2026-10-12T16:30:08Z |
| Market best draw last update utc | 2026-10-12T16:30:08Z |
| Market best away last update utc | 2026-10-12T16:30:08Z |
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
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.30 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.17 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.40 |
| Fair Over 3.5 odds | 1.71 |
| Fair Under 3.5 odds | 2.41 |
| Fair Over 4.5 odds | 2.56 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 87.2% |
| Unadjusted draw probability | 9.1% |
| Unadjusted away-win probability | 3.7% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.4% |
| Raw p btts yes | 49.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.22 |
| Reference draw odds | 6.50 |
| Reference away odds | 10.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.08 |
| Home probability edge | +3.6% |
| Draw probability edge | -1.6% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +6.8% |
| Under 2.5 probability edge | -6.8% |
| Raw edge prob home | 0.0714 |
| Raw ev home | 0.0987 |
| Raw edge prob draw | -0.0318 |
| Raw ev draw | -0.2500 |
| Raw edge prob away | -0.0396 |
| Raw ev away | -0.5067 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **45.1%**. Expected goals are 1.77 for Newcastle United and 1.44 for Aston Villa (3.21 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 62.2%; Under 3.5 goals: 60.0%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 64.3%; BTTS No (at least one team does not score): 35.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 45.1% | 2.22 |
| Draw | 25.1% | 3.99 |
| Aston Villa win | 29.8% | 3.35 |

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
| 1 | 1-1 | 11.29% |
| 2 | 2-1 | 9.25% |
| 3 | 1-2 | 7.27% |
| 4 | 2-2 | 6.51% |
| 5 | 2-0 | 6.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 45.1% | 45.9% | 2.22 | +0.2% |
| Draw | 25.1% | 24.9% | 3.95 | -1.0% |
| Aston Villa win | 29.8% | 29.3% | 3.35 | -0.1% |
| Over 2.5 | 62.2% | 60.5% | 1.65 | +2.7% |
| Under 2.5 | 37.8% | 39.5% | 2.45 | -7.5% |

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
| Market best home last update utc | 2026-10-12T16:30:23Z |
| Market best draw last update utc | 2026-10-12T16:30:23Z |
| Market best away last update utc | 2026-10-12T16:30:08Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Matchbook |
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
| Fair Under 0.5 odds | 19.65 |
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
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.05 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / MyBookie.ag |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | -0.7% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | -0.0145 |
| Raw ev home | -0.0142 |
| Raw edge prob draw | 0.0035 |
| Raw ev draw | -0.0036 |
| Raw edge prob away | 0.0110 |
| Raw ev away | 0.0173 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.3%**. Expected goals are 1.53 for Bournemouth and 1.04 for Sunderland (2.57 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 47.7%; Under 3.5 goals: 74.1%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 51.9%; BTTS No (at least one team does not score): 48.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.3% | 2.11 |
| Draw | 27.4% | 3.64 |
| Sunderland win | 25.2% | 3.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.53 |
| Sunderland expected goals | 1.04 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 47.7% |
| Under 2.5 | 52.3% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.11% |
| 2 | 1-0 | 10.41% |
| 3 | 2-1 | 9.33% |
| 4 | 2-0 | 8.94% |
| 5 | 0-0 | 8.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.3% | 47.4% | 2.12 | +0.3% |
| Draw | 27.4% | 26.7% | 3.75 | +2.9% |
| Sunderland win | 25.2% | 25.9% | 3.85 | -2.8% |
| Over 2.5 | 47.7% | 53.1% | 1.88 | -10.2% |
| Under 2.5 | 52.3% | 46.9% | 2.07 | +8.2% |

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
| Market best home last update utc | 2026-10-12T16:30:08Z |
| Market best draw last update utc | 2026-10-12T16:30:08Z |
| Market best away last update utc | 2026-10-12T16:30:08Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bournemouth |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.9% |
| P btts no | 48.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.53 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.85 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.36 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 74.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 52.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.00 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 1.94 |
| Home probability edge | -0.0% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | -0.0009 |
| Raw ev home | 0.0021 |
| Raw edge prob draw | 0.0144 |
| Raw ev draw | 0.0562 |
| Raw edge prob away | -0.0134 |
| Raw ev away | -0.0543 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **57.8%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 56.9%; Under 3.5 goals: 66.0%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 57.8% | 1.73 |
| Draw | 23.0% | 4.34 |
| Crystal Palace win | 19.2% | 5.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 1.85 |
| Crystal Palace expected goals | 1.08 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 56.9% |
| Under 2.5 | 43.1% |
| Over 3.5 | 34.0% |
| Under 3.5 | 66.0% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.90% |
| 2 | 2-1 | 10.52% |
| 3 | 2-0 | 9.73% |
| 4 | 1-0 | 9.34% |
| 5 | 3-1 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 57.8% | 61.4% | 1.63 | -5.8% |
| Draw | 23.0% | 21.1% | 4.65 | +7.1% |
| Crystal Palace win | 19.2% | 17.5% | 5.90 | +13.2% |
| Over 2.5 | 56.9% | 60.9% | 1.63 | -7.3% |
| Under 2.5 | 43.1% | 39.1% | 2.50 | +7.8% |

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
| Market best home last update utc | 2026-10-12T16:30:08Z |
| Market best draw last update utc | 2026-10-12T16:30:22Z |
| Market best away last update utc | 2026-10-12T16:30:23Z |
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
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.74 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.10 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.94 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.66 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 80.1% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.57 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | -3.6% |
| Draw probability edge | +1.9% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | -0.0719 |
| Raw ev home | -0.1170 |
| Raw edge prob draw | 0.0380 |
| Raw ev draw | 0.1599 |
| Raw edge prob away | 0.0338 |
| Raw ev away | 0.2322 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **38.8%**. Expected goals are 1.42 for Leeds United and 1.30 for Manchester United (2.72 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 51.4%; Under 3.5 goals: 71.0%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 38.8% | 2.58 |
| Draw | 27.5% | 3.64 |
| Manchester United win | 33.8% | 2.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.30 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 51.4% |
| Under 2.5 | 48.6% |
| Over 3.5 | 29.0% |
| Under 3.5 | 71.0% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.09% |
| 2 | 2-1 | 8.66% |
| 3 | 1-0 | 8.12% |
| 4 | 1-2 | 8.04% |
| 5 | 0-0 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 38.8% | 38.9% | 2.62 | +1.6% |
| Draw | 27.5% | 26.8% | 3.75 | +3.1% |
| Manchester United win | 33.8% | 34.3% | 2.88 | -2.8% |
| Over 2.5 | 51.4% | 58.8% | 1.73 | -11.2% |
| Under 2.5 | 48.6% | 41.2% | 2.34 | +13.8% |

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
| Market best home last update utc | 2026-10-12T16:30:08Z |
| Market best draw last update utc | 2026-10-12T16:30:08Z |
| Market best away last update utc | 2026-10-12T16:30:23Z |
| Odds bookmakers 1x2 | 25.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.04 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.10 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 38.6% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 56.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 2.40 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / MyBookie.ag |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.19 |
| Home probability edge | -0.2% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.0036 |
| Raw ev home | 0.0109 |
| Raw edge prob draw | 0.0146 |
| Raw ev draw | 0.0580 |
| Raw edge prob away | -0.0110 |
| Raw ev away | -0.0438 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **58.4%**. Expected goals are 0.77 for Nottingham Forest and 1.55 for Arsenal (2.32 combined). The most likely exact score is 0-1 at 14.9%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 42.1%; Under 3.5 goals: 79.1%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 42.8%; BTTS No (at least one team does not score): 57.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.5% | 6.08 |
| Draw | 25.2% | 3.97 |
| Arsenal win | 58.4% | 1.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.77 |
| Arsenal expected goals | 1.55 |
| Expected total goals | 2.32 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 69.1% |
| Under 1.5 | 30.9% |
| Over 2.5 | 42.1% |
| Under 2.5 | 57.9% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.92% |
| 2 | 0-2 | 12.60% |
| 3 | 1-1 | 11.65% |
| 4 | 0-0 | 9.93% |
| 5 | 1-2 | 9.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.5% | 15.6% | 6.80 | +11.9% |
| Draw | 25.2% | 22.4% | 4.20 | +5.8% |
| Arsenal win | 58.4% | 62.0% | 1.66 | -3.1% |
| Over 2.5 | 42.1% | 50.0% | 1.97 | -17.0% |
| Under 2.5 | 57.9% | 50.0% | 1.98 | +14.6% |

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
| Market best home last update utc | 2026-10-12T16:30:08Z |
| Market best draw last update utc | 2026-10-12T16:30:08Z |
| Market best away last update utc | 2026-10-12T16:30:08Z |
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
| P btts yes | 42.8% |
| P btts no | 57.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.07 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.24 |
| Fair Over 2.5 odds | 2.37 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.79 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.17 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 43.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / MyBookie.ag |
| Reference home odds | 5.50 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.55 |
| O/U 2.5 market source | The Odds API / MyBookie.ag |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | +0.9% |
| Draw probability edge | +2.8% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | -7.9% |
| Under 2.5 probability edge | +7.9% |
| Raw edge prob home | 0.0171 |
| Raw ev home | 0.1773 |
| Raw edge prob draw | 0.0562 |
| Raw ev draw | 0.1757 |
| Raw edge prob away | -0.0733 |
| Raw ev away | -0.0921 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **68.5%**. Expected goals are 1.71 for Tottenham Hotspur and 0.34 for Coventry City (2.04 combined). The most likely exact score is 1-0 at 20.6%. Goal-market probabilities: at least one goal: 87.3%; Over 2.5 goals: 33.5%; Under 3.5 goals: 85.3%; Under 4.5 goals: 94.4%; BTTS Yes (both teams score): 24.0%; BTTS No (at least one team does not score): 76.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 68.5% | 1.46 |
| Draw | 21.3% | 4.70 |
| Coventry City win | 10.2% | 9.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.71 |
| Coventry City expected goals | 0.34 |
| Expected total goals | 2.04 |
| Over 0.5 | 87.3% |
| Under 0.5 | 12.7% |
| Over 1.5 | 60.5% |
| Under 1.5 | 39.5% |
| Over 2.5 | 33.5% |
| Under 2.5 | 66.5% |
| Over 3.5 | 14.7% |
| Under 3.5 | 85.3% |
| Over 4.5 | 5.6% |
| Under 4.5 | 94.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.64% |
| 2 | 2-0 | 18.24% |
| 3 | 0-0 | 12.68% |
| 4 | 3-0 | 10.37% |
| 5 | 1-1 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 68.5% | 66.0% | 1.54 | +5.5% |
| Draw | 21.3% | 19.4% | 4.80 | +2.1% |
| Coventry City win | 10.2% | 14.5% | 6.80 | -30.5% |
| Over 2.5 | 33.5% | 60.9% | 1.64 | -45.1% |
| Under 2.5 | 66.5% | 39.1% | 2.46 | +63.7% |

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
| Market best home last update utc | 2026-10-12T16:30:08Z |
| Market best draw last update utc | 2026-10-12T16:30:09Z |
| Market best away last update utc | 2026-10-12T16:30:08Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 24.0% |
| P btts no | 76.0% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.89 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.53 |
| Fair Over 2.5 odds | 2.99 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 6.81 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.00 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 5.9% |
| Raw p over 1 5 | 61.3% |
| Raw p under 3 5 | 85.0% |
| Raw p btts yes | 24.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.48 |
| Reference draw odds | 4.70 |
| Reference away odds | 6.20 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | +2.5% |
| Draw probability edge | +1.8% |
| Away probability edge | -4.3% |
| Over 2.5 probability edge | -27.5% |
| Under 2.5 probability edge | +27.5% |
| Raw edge prob home | 0.0491 |
| Raw ev home | 0.0927 |
| Raw edge prob draw | 0.0366 |
| Raw ev draw | 0.1094 |
| Raw edge prob away | -0.0858 |
| Raw ev away | -0.5967 |

</details>


---
