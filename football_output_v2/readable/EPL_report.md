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
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 4.00 |
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

The model's most likely 1X2 outcome is **Nottingham Forest win** at **36.2%**. Expected goals are 1.25 for Crystal Palace and 1.23 for Nottingham Forest (2.48 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 45.5%; Under 3.5 goals: 76.2%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 35.4% | 2.83 |
| Draw | 28.5% | 3.51 |
| Nottingham Forest win | 36.2% | 2.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.25 |
| Nottingham Forest expected goals | 1.23 |
| Expected total goals | 2.48 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 72.2% |
| Under 1.5 | 27.8% |
| Over 2.5 | 45.5% |
| Under 2.5 | 54.5% |
| Over 3.5 | 23.8% |
| Under 3.5 | 76.2% |
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.57% |
| 2 | 0-1 | 9.37% |
| 3 | 0-0 | 9.30% |
| 4 | 1-0 | 9.11% |
| 5 | 1-2 | 8.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 35.4% | 35.3% | 2.92 | +3.3% |
| Draw | 28.5% | 27.1% | 3.50 | -0.4% |
| Nottingham Forest win | 36.2% | 37.6% | 2.70 | -2.4% |
| Over 2.5 | 45.5% | 51.0% | 1.96 | -10.8% |
| Under 2.5 | 54.5% | 49.0% | 2.04 | +11.1% |

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
| Market best home last update utc | 2026-10-11T08:22:18Z |
| Market best draw last update utc | 2026-10-11T08:22:52Z |
| Market best away last update utc | 2026-10-11T08:22:19Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.75 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.60 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.20 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.33 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 35.4% |
| Unadjusted draw probability | 29.9% |
| Unadjusted away-win probability | 34.7% |
| Raw p over 1 5 | 72.1% |
| Raw p under 3 5 | 76.3% |
| Raw p btts yes | 51.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +0.0% |
| Draw probability edge | +1.4% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | 0.0010 |
| Raw ev home | 0.0345 |
| Raw edge prob draw | 0.0278 |
| Raw ev draw | 0.0448 |
| Raw edge prob away | -0.0288 |
| Raw ev away | -0.0626 |

</details>


---

## 2026-10-11 — Hull City vs Everton

The model's most likely 1X2 outcome is **Hull City win** at **35.1%**. Expected goals are 1.09 for Hull City and 0.66 for Everton (1.74 combined). The most likely exact score is 0-1 at 16.8%. Goal-market probabilities: at least one goal: 83.5%; Over 2.5 goals: 26.2%; Under 3.5 goals: 90.3%; Under 4.5 goals: 96.7%; BTTS Yes (both teams score): 32.7%; BTTS No (at least one team does not score): 67.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 35.1% | 2.85 |
| Draw | 30.7% | 3.25 |
| Everton win | 34.1% | 2.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.09 |
| Everton expected goals | 0.66 |
| Expected total goals | 1.74 |
| Over 0.5 | 83.5% |
| Under 0.5 | 16.5% |
| Over 1.5 | 52.7% |
| Under 1.5 | 47.3% |
| Over 2.5 | 26.2% |
| Under 2.5 | 73.8% |
| Over 3.5 | 9.7% |
| Under 3.5 | 90.3% |
| Over 4.5 | 3.3% |
| Under 4.5 | 96.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.75% |
| 2 | 0-0 | 16.49% |
| 3 | 1-0 | 14.04% |
| 4 | 1-1 | 12.12% |
| 5 | 2-0 | 8.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 35.1% | 26.0% | 3.95 | +38.8% |
| Draw | 30.7% | 26.5% | 3.52 | +8.2% |
| Everton win | 34.1% | 47.5% | 2.18 | -25.6% |
| Over 2.5 | 26.2% | 46.7% | 2.12 | -44.5% |
| Under 2.5 | 73.8% | 53.3% | 1.89 | +39.5% |

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
| Market best home last update utc | 2026-10-11T08:22:52Z |
| Market best draw last update utc | 2026-10-11T08:22:18Z |
| Market best away last update utc | 2026-10-11T08:22:18Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Matchbook |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Everton |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.7% |
| P btts no | 67.3% |
| Fair Over 0.5 odds | 1.20 |
| Fair Under 0.5 odds | 6.07 |
| Fair Over 1.5 odds | 1.90 |
| Fair Under 1.5 odds | 2.12 |
| Fair Over 2.5 odds | 3.82 |
| Fair Under 2.5 odds | 1.35 |
| Fair Over 3.5 odds | 10.29 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.42 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 44.2% |
| Unadjusted draw probability | 35.0% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 53.4% |
| Raw p under 3 5 | 90.0% |
| Raw p btts yes | 33.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.82 |
| Home probability edge | +9.1% |
| Draw probability edge | +4.3% |
| Away probability edge | -13.4% |
| Over 2.5 probability edge | -20.6% |
| Under 2.5 probability edge | +20.6% |
| Raw edge prob home | 0.1818 |
| Raw ev home | 0.7468 |
| Raw edge prob draw | 0.0855 |
| Raw ev draw | 0.2321 |
| Raw edge prob away | -0.2673 |
| Raw ev away | -0.5471 |
| Market p over 1 5 | 72.7% |
| Market over 1 5 odds | 1.35 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-11T08:22:52Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 75.1% |
| Market under 3 5 odds | 1.32 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:22:34Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.70 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 52.7% |
| Market btts yes odds | 1.89 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:22:51Z |
| Market reference btts yes odds | 1.89 |
| Market reference btts yes opposite odds | 2.10 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-11 — Liverpool vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **43.2%**. Expected goals are 1.40 for Liverpool and 1.65 for Manchester City (3.05 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 59.1%; Under 3.5 goals: 63.6%; Under 4.5 goals: 80.6%; BTTS Yes (both teams score): 61.8%; BTTS No (at least one team does not score): 38.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 31.4% | 3.19 |
| Draw | 25.4% | 3.94 |
| Manchester City win | 43.2% | 2.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.40 |
| Manchester City expected goals | 1.65 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 82.0% |
| Under 1.5 | 18.0% |
| Over 2.5 | 59.1% |
| Under 2.5 | 40.9% |
| Over 3.5 | 36.4% |
| Under 3.5 | 63.6% |
| Over 4.5 | 19.4% |
| Under 4.5 | 80.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.73% |
| 2 | 1-2 | 9.20% |
| 3 | 2-1 | 7.64% |
| 4 | 0-1 | 6.81% |
| 5 | 0-2 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 31.4% | 31.4% | 3.20 | +0.4% |
| Draw | 25.4% | 24.6% | 3.85 | -2.3% |
| Manchester City win | 43.2% | 44.0% | 2.36 | +2.0% |
| Over 2.5 | 59.1% | 60.9% | 1.67 | -1.4% |
| Under 2.5 | 40.9% | 39.1% | 2.41 | -1.3% |

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
| Market best home last update utc | 2026-10-11T08:22:52Z |
| Market best draw last update utc | 2026-10-11T08:22:52Z |
| Market best away last update utc | 2026-10-11T08:22:18Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.8% |
| P btts no | 38.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.51 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.56 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.74 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.15 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 31.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 62.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | +0.0% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.0002 |
| Raw ev home | 0.0043 |
| Raw edge prob draw | 0.0156 |
| Raw ev draw | 0.0073 |
| Raw edge prob away | -0.0158 |
| Raw ev away | 0.0018 |

</details>


---

## 2026-10-12 — Coventry City vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **58.4%**. Expected goals are 0.36 for Coventry City and 1.82 for Newcastle United (2.18 combined). The most likely exact score is 0-1 at 15.9%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 34.5%; Under 3.5 goals: 84.5%; Under 4.5 goals: 93.9%; BTTS Yes (both teams score): 27.8%; BTTS No (at least one team does not score): 72.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 18.0% | 5.57 |
| Draw | 23.6% | 4.23 |
| Newcastle United win | 58.4% | 1.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 0.36 |
| Newcastle United expected goals | 1.82 |
| Expected total goals | 2.18 |
| Over 0.5 | 86.8% |
| Under 0.5 | 13.2% |
| Over 1.5 | 60.8% |
| Under 1.5 | 39.2% |
| Over 2.5 | 34.5% |
| Under 2.5 | 65.5% |
| Over 3.5 | 15.5% |
| Under 3.5 | 84.5% |
| Over 4.5 | 6.1% |
| Under 4.5 | 93.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.89% |
| 2 | 0-2 | 15.02% |
| 3 | 0-0 | 13.17% |
| 4 | 1-0 | 10.15% |
| 5 | 0-3 | 9.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 18.0% | 30.0% | 3.35 | -39.8% |
| Draw | 23.6% | 25.6% | 3.80 | -10.2% |
| Newcastle United win | 58.4% | 44.3% | 2.30 | +34.3% |
| Over 2.5 | 34.5% | 56.0% | 1.75 | -39.7% |
| Under 2.5 | 65.5% | 44.0% | 2.25 | +47.4% |

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
| Market best home last update utc | 2026-10-11T08:22:52Z |
| Market best draw last update utc | 2026-10-11T08:22:52Z |
| Market best away last update utc | 2026-10-11T08:22:52Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 27.8% |
| P btts no | 72.2% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.59 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.55 |
| Fair Over 2.5 odds | 2.90 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.46 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 16.27 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 72.5% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 26.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -12.1% |
| Draw probability edge | -2.0% |
| Away probability edge | +14.1% |
| Over 2.5 probability edge | -21.5% |
| Under 2.5 probability edge | +21.5% |
| Raw edge prob home | -0.2416 |
| Raw ev home | -0.8030 |
| Raw edge prob draw | -0.0400 |
| Raw ev draw | -0.1782 |
| Raw edge prob away | 0.2817 |
| Raw ev away | 0.6673 |

</details>


---

## 2026-10-17 — Brentford vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **40.3%**. Expected goals are 1.48 for Brentford and 1.63 for Liverpool (3.11 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 60.5%; Under 3.5 goals: 62.1%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 34.6% | 2.89 |
| Draw | 25.1% | 3.99 |
| Liverpool win | 40.3% | 2.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.48 |
| Liverpool expected goals | 1.63 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 60.5% |
| Under 2.5 | 39.5% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.45% |
| 2 | 1-2 | 8.79% |
| 3 | 2-1 | 8.16% |
| 4 | 2-2 | 6.27% |
| 5 | 0-1 | 6.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 34.6% | 35.4% | 2.88 | -0.3% |
| Draw | 25.1% | 24.1% | 3.85 | -3.5% |
| Liverpool win | 40.3% | 40.5% | 2.52 | +1.6% |
| Over 2.5 | 60.5% | 62.2% | 1.56 | -5.6% |
| Under 2.5 | 39.5% | 37.8% | 2.45 | -3.3% |

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
| Market best home last update utc | 2026-10-11T08:22:18Z |
| Market best draw last update utc | 2026-10-11T08:22:52Z |
| Market best away last update utc | 2026-10-11T08:22:52Z |
| Odds bookmakers 1x2 | 20.00 |
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
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.61 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.85 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.53 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 40.2% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.30 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -0.8% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0159 |
| Raw ev home | -0.0260 |
| Raw edge prob draw | 0.0184 |
| Raw ev draw | 0.0000 |
| Raw edge prob away | -0.0025 |
| Raw ev away | 0.0132 |

</details>


---

## 2026-10-17 — Everton vs Chelsea

The model's most likely 1X2 outcome is **Chelsea win** at **40.1%**. Expected goals are 1.28 for Everton and 1.29 for Chelsea (2.57 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 48.5%; Under 3.5 goals: 74.0%; Under 4.5 goals: 87.8%; BTTS Yes (both teams score): 53.1%; BTTS No (at least one team does not score): 46.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 33.4% | 3.00 |
| Draw | 26.5% | 3.77 |
| Chelsea win | 40.1% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.28 |
| Chelsea expected goals | 1.29 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 74.3% |
| Under 1.5 | 25.7% |
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 12.2% |
| Under 4.5 | 87.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.67% |
| 2 | 0-1 | 9.61% |
| 3 | 1-2 | 9.19% |
| 4 | 0-0 | 8.12% |
| 5 | 1-0 | 8.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 33.4% | 31.5% | 3.30 | +10.1% |
| Draw | 26.5% | 23.8% | 3.85 | +2.1% |
| Chelsea win | 40.1% | 44.7% | 2.31 | -7.3% |
| Over 2.5 | 48.5% | 59.0% | 1.72 | -16.6% |
| Under 2.5 | 51.5% | 41.0% | 2.30 | +18.5% |

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
| Market best home last update utc | 2026-10-11T08:22:52Z |
| Market best draw last update utc | 2026-10-11T08:22:19Z |
| Market best away last update utc | 2026-10-11T08:22:18Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Everton |
| Matched away-team name | Chelsea |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 53.1% |
| P btts no | 46.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.31 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.88 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.20 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 53.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +1.9% |
| Draw probability edge | +2.7% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | 0.0379 |
| Raw ev home | 0.1639 |
| Raw edge prob draw | 0.0537 |
| Raw ev draw | 0.1239 |
| Raw edge prob away | -0.0916 |
| Raw ev away | -0.1791 |

</details>


---

## 2026-10-17 — Fulham vs Hull City

The model's most likely 1X2 outcome is **Fulham win** at **42.6%**. Expected goals are 0.85 for Fulham and 1.07 for Hull City (1.92 combined). The most likely exact score is 1-0 at 17.4%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 31.8%; Under 3.5 goals: 87.1%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 37.9%; BTTS No (at least one team does not score): 62.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 42.6% | 2.35 |
| Draw | 28.0% | 3.57 |
| Hull City win | 29.4% | 3.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 0.85 |
| Hull City expected goals | 1.07 |
| Expected total goals | 1.92 |
| Over 0.5 | 86.8% |
| Under 0.5 | 13.2% |
| Over 1.5 | 58.6% |
| Under 1.5 | 41.4% |
| Over 2.5 | 31.8% |
| Under 2.5 | 68.2% |
| Over 3.5 | 12.9% |
| Under 3.5 | 87.1% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.42% |
| 2 | 0-0 | 13.19% |
| 3 | 1-1 | 12.10% |
| 4 | 0-1 | 10.81% |
| 5 | 2-1 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 42.6% | 58.2% | 1.73 | -26.4% |
| Draw | 28.0% | 22.0% | 4.11 | +15.3% |
| Hull City win | 29.4% | 19.8% | 5.20 | +52.8% |
| Over 2.5 | 31.8% | 58.1% | 1.81 | -42.4% |
| Under 2.5 | 68.2% | 41.9% | 2.23 | +52.1% |

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
| Market best home last update utc | 2026-10-11T08:22:18Z |
| Market best draw last update utc | 2026-10-11T08:22:18Z |
| Market best away last update utc | 2026-10-11T08:22:51Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | LeoVegas (SE) |
| Matched home-team name | Fulham |
| Matched away-team name | Hull |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 37.9% |
| P btts no | 62.1% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.58 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.41 |
| Fair Over 2.5 odds | 3.14 |
| Fair Under 2.5 odds | 1.47 |
| Fair Over 3.5 odds | 7.78 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.78 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 34.1% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 58.6% |
| Raw p under 3 5 | 87.1% |
| Raw p btts yes | 39.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.64 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -15.7% |
| Draw probability edge | +6.1% |
| Away probability edge | +9.6% |
| Over 2.5 probability edge | -26.3% |
| Under 2.5 probability edge | +26.3% |
| Raw edge prob home | -0.3132 |
| Raw ev home | -0.5345 |
| Raw edge prob draw | 0.1215 |
| Raw ev draw | 0.4023 |
| Raw edge prob away | 0.1918 |
| Raw ev away | 1.0267 |
| Market p over 1 5 | 79.5% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Codere (IT) |
| Market best over 1 5 last update utc | 2026-10-11T08:22:35Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 67.7% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:22:34Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 2.65 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 55.3% |
| Market btts yes odds | 1.74 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:22:51Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.12 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-17 — Manchester City vs Ipswich Town

The model's most likely 1X2 outcome is **Manchester City win** at **83.1%**. Expected goals are 3.46 for Manchester City and 0.70 for Ipswich Town (4.15 combined). The most likely exact score is 3-0 at 10.3%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 77.3%; Under 3.5 goals: 41.7%; Under 4.5 goals: 61.0%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 83.1% | 1.20 |
| Draw | 10.5% | 9.56 |
| Ipswich Town win | 6.5% | 15.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 3.46 |
| Ipswich Town expected goals | 0.70 |
| Expected total goals | 4.15 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 91.7% |
| Under 1.5 | 8.3% |
| Over 2.5 | 77.3% |
| Under 2.5 | 22.7% |
| Over 3.5 | 58.3% |
| Under 3.5 | 41.7% |
| Over 4.5 | 39.0% |
| Under 4.5 | 61.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.30% |
| 2 | 2-0 | 8.94% |
| 3 | 4-0 | 8.91% |
| 4 | 3-1 | 7.19% |
| 5 | 2-1 | 6.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 83.1% | 78.9% | 1.29 | +7.2% |
| Draw | 10.5% | 11.8% | 7.20 | -24.7% |
| Ipswich Town win | 6.5% | 9.3% | 13.50 | -12.6% |
| Over 2.5 | 77.3% | 69.8% | 1.39 | +7.5% |
| Under 2.5 | 22.7% | 30.2% | 3.03 | -31.3% |

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
| Market best home last update utc | 2026-10-11T08:22:18Z |
| Market best draw last update utc | 2026-10-11T08:22:52Z |
| Market best away last update utc | 2026-10-11T08:22:52Z |
| Odds bookmakers 1x2 | 20.00 |
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
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.44 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.07 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.41 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.40 |
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
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.23 |
| Reference draw odds | 6.50 |
| Reference away odds | 8.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +4.1% |
| Draw probability edge | -1.3% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | +7.5% |
| Under 2.5 probability edge | -7.5% |
| Raw edge prob home | 0.0827 |
| Raw ev home | 0.1249 |
| Raw edge prob draw | -0.0263 |
| Raw ev draw | -0.3414 |
| Raw edge prob away | -0.0564 |
| Raw ev away | -0.5067 |
| Market p over 1 5 | 88.7% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:22:03Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.92 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-11T08:21:54Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 1.89 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 52.6% |
| Market btts yes odds | 1.88 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-11T08:22:51Z |
| Market reference btts yes odds | 1.88 |
| Market reference btts yes opposite odds | 2.08 |
| Market btts yes bookmakers | 5 |

</details>


---

## 2026-10-17 — Newcastle United vs Aston Villa

The model's most likely 1X2 outcome is **Newcastle United win** at **45.7%**. Expected goals are 1.77 for Newcastle United and 1.44 for Aston Villa (3.21 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 62.4%; Under 3.5 goals: 60.0%; Under 4.5 goals: 77.8%; BTTS Yes (both teams score): 64.2%; BTTS No (at least one team does not score): 35.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 45.7% | 2.19 |
| Draw | 24.6% | 4.06 |
| Aston Villa win | 29.7% | 3.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.77 |
| Aston Villa expected goals | 1.44 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.4% |
| Under 2.5 | 37.6% |
| Over 3.5 | 40.0% |
| Under 3.5 | 60.0% |
| Over 4.5 | 22.2% |
| Under 4.5 | 77.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.09% |
| 2 | 2-1 | 9.36% |
| 3 | 1-2 | 7.25% |
| 4 | 2-0 | 6.51% |
| 5 | 2-2 | 6.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 45.7% | 46.9% | 2.17 | -0.9% |
| Draw | 24.6% | 24.0% | 3.95 | -2.8% |
| Aston Villa win | 29.7% | 29.1% | 3.35 | -0.4% |
| Over 2.5 | 62.4% | 60.0% | 1.65 | +3.0% |
| Under 2.5 | 37.6% | 40.0% | 2.45 | -7.9% |

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
| Market best home last update utc | 2026-10-11T08:22:18Z |
| Market best draw last update utc | 2026-10-11T08:22:18Z |
| Market best away last update utc | 2026-10-11T08:22:18Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Newcastle |
| Matched away-team name | Aston Villa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 64.2% |
| P btts no | 35.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.01 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.29 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.66 |
| Fair Over 3.5 odds | 2.50 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.50 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 44.4% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 30.4% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 64.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | -1.3% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | +2.4% |
| Under 2.5 probability edge | -2.4% |
| Raw edge prob home | -0.0252 |
| Raw ev home | -0.0364 |
| Raw edge prob draw | 0.0124 |
| Raw ev draw | -0.0036 |
| Raw edge prob away | 0.0128 |
| Raw ev away | 0.0173 |

</details>


---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.7%**. Expected goals are 1.53 for Bournemouth and 1.04 for Sunderland (2.57 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 48.1%; Under 3.5 goals: 74.1%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.7% | 2.10 |
| Draw | 26.5% | 3.77 |
| Sunderland win | 25.7% | 3.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.53 |
| Sunderland expected goals | 1.04 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 48.1% |
| Under 2.5 | 51.9% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.67% |
| 2 | 1-0 | 10.50% |
| 3 | 2-1 | 9.41% |
| 4 | 2-0 | 9.02% |
| 5 | 0-0 | 8.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.7% | 48.2% | 2.10 | +0.2% |
| Draw | 26.5% | 24.9% | 3.75 | -0.5% |
| Sunderland win | 25.7% | 26.9% | 3.85 | -0.9% |
| Over 2.5 | 48.1% | 52.0% | 1.88 | -9.6% |
| Under 2.5 | 51.9% | 48.0% | 2.07 | +7.5% |

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
| Market best home last update utc | 2026-10-11T08:22:52Z |
| Market best draw last update utc | 2026-10-11T08:22:18Z |
| Market best away last update utc | 2026-10-11T08:22:18Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bournemouth |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.92 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.29 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 74.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 52.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.96 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | -0.5% |
| Draw probability edge | +1.6% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0090 |
| Raw ev home | -0.0073 |
| Raw edge prob draw | 0.0326 |
| Raw ev draw | 0.0562 |
| Raw edge prob away | -0.0236 |
| Raw ev away | -0.0543 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **58.2%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.1%; Under 3.5 goals: 65.9%; Under 4.5 goals: 82.2%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 58.2% | 1.72 |
| Draw | 22.5% | 4.44 |
| Crystal Palace win | 19.3% | 5.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 1.85 |
| Crystal Palace expected goals | 1.08 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.1% |
| Under 3.5 | 65.9% |
| Over 4.5 | 17.8% |
| Under 4.5 | 82.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.65% |
| 2 | 2-1 | 10.59% |
| 3 | 2-0 | 9.80% |
| 4 | 1-0 | 9.41% |
| 5 | 3-1 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 58.2% | 62.2% | 1.63 | -5.2% |
| Draw | 22.5% | 20.1% | 4.57 | +2.8% |
| Crystal Palace win | 19.3% | 17.8% | 5.55 | +7.3% |
| Over 2.5 | 57.1% | 61.5% | 1.63 | -6.9% |
| Under 2.5 | 42.9% | 38.5% | 2.49 | +6.8% |

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
| Market best home last update utc | 2026-10-11T08:22:18Z |
| Market best draw last update utc | 2026-10-11T08:22:18Z |
| Market best away last update utc | 2026-10-11T08:22:51Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.14 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.54 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -4.0% |
| Draw probability edge | +2.4% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | -0.0799 |
| Raw ev home | -0.1170 |
| Raw edge prob draw | 0.0488 |
| Raw ev draw | 0.1399 |
| Raw edge prob away | 0.0311 |
| Raw ev away | 0.1591 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **39.0%**. Expected goals are 1.42 for Leeds United and 1.30 for Manchester United (2.72 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 51.7%; Under 3.5 goals: 70.9%; Under 4.5 goals: 85.8%; BTTS Yes (both teams score): 56.0%; BTTS No (at least one team does not score): 44.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 39.0% | 2.57 |
| Draw | 26.5% | 3.78 |
| Manchester United win | 34.6% | 2.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.30 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 51.7% |
| Under 2.5 | 48.3% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.2% |
| Under 4.5 | 85.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.60% |
| 2 | 2-1 | 8.71% |
| 3 | 1-2 | 8.24% |
| 4 | 1-0 | 8.16% |
| 5 | 0-1 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 39.0% | 39.3% | 2.60 | +1.3% |
| Draw | 26.5% | 24.7% | 3.75 | -0.8% |
| Manchester United win | 34.6% | 36.0% | 2.86 | -1.1% |
| Over 2.5 | 51.7% | 57.6% | 1.70 | -12.0% |
| Under 2.5 | 48.3% | 42.4% | 2.34 | +12.9% |

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
| Market best home last update utc | 2026-10-11T08:22:19Z |
| Market best draw last update utc | 2026-10-11T08:22:18Z |
| Market best away last update utc | 2026-10-11T08:22:52Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.0% |
| P btts no | 44.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.55 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.32 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.04 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 38.6% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 56.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.35 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.55 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | -0.4% |
| Draw probability edge | +1.8% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0075 |
| Raw ev home | 0.0032 |
| Raw edge prob draw | 0.0353 |
| Raw ev draw | 0.0580 |
| Raw edge prob away | -0.0278 |
| Raw ev away | -0.0505 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **58.9%**. Expected goals are 0.77 for Nottingham Forest and 1.55 for Arsenal (2.32 combined). The most likely exact score is 0-1 at 15.1%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 42.2%; Under 3.5 goals: 79.1%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 42.7%; BTTS No (at least one team does not score): 57.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 16.2% | 6.19 |
| Draw | 25.0% | 4.01 |
| Arsenal win | 58.9% | 1.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.77 |
| Arsenal expected goals | 1.55 |
| Expected total goals | 2.32 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 69.2% |
| Under 1.5 | 30.8% |
| Over 2.5 | 42.2% |
| Under 2.5 | 57.8% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.06% |
| 2 | 0-2 | 12.71% |
| 3 | 1-1 | 11.55% |
| 4 | 0-0 | 9.84% |
| 5 | 1-2 | 9.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 16.2% | 15.0% | 6.80 | +9.9% |
| Draw | 25.0% | 21.9% | 4.10 | +2.3% |
| Arsenal win | 58.9% | 63.1% | 1.66 | -2.3% |
| Over 2.5 | 42.2% | 52.6% | 1.97 | -16.8% |
| Under 2.5 | 57.8% | 47.4% | 1.97 | +13.8% |

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
| Market best home last update utc | 2026-10-11T08:22:52Z |
| Market best draw last update utc | 2026-10-11T08:22:35Z |
| Market best away last update utc | 2026-10-11T08:22:18Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Codere (IT) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.7% |
| P btts no | 57.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.17 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.25 |
| Fair Over 2.5 odds | 2.37 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.77 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.12 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.3% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 43.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 5.30 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.50 |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 1.85 |
| Home probability edge | +1.1% |
| Draw probability edge | +3.0% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -10.3% |
| Under 2.5 probability edge | +10.3% |
| Raw edge prob home | 0.0230 |
| Raw ev home | 0.1773 |
| Raw edge prob draw | 0.0607 |
| Raw ev draw | 0.1477 |
| Raw edge prob away | -0.0837 |
| Raw ev away | -0.0921 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **68.9%**. Expected goals are 1.71 for Tottenham Hotspur and 0.34 for Coventry City (2.04 combined). The most likely exact score is 1-0 at 20.8%. Goal-market probabilities: at least one goal: 87.7%; Over 2.5 goals: 33.7%; Under 3.5 goals: 85.3%; Under 4.5 goals: 94.4%; BTTS Yes (both teams score): 23.9%; BTTS No (at least one team does not score): 76.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 68.9% | 1.45 |
| Draw | 20.6% | 4.85 |
| Coventry City win | 10.4% | 9.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.71 |
| Coventry City expected goals | 0.34 |
| Expected total goals | 2.04 |
| Over 0.5 | 87.7% |
| Under 0.5 | 12.3% |
| Over 1.5 | 60.6% |
| Under 1.5 | 39.4% |
| Over 2.5 | 33.7% |
| Under 2.5 | 66.3% |
| Over 3.5 | 14.7% |
| Under 3.5 | 85.3% |
| Over 4.5 | 5.6% |
| Under 4.5 | 94.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.77% |
| 2 | 2-0 | 18.35% |
| 3 | 0-0 | 12.29% |
| 4 | 3-0 | 10.43% |
| 5 | 1-1 | 7.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 68.9% | 66.9% | 1.54 | +6.1% |
| Draw | 20.6% | 18.1% | 4.80 | -1.0% |
| Coventry City win | 10.4% | 15.0% | 6.76 | -29.4% |
| Over 2.5 | 33.7% | 60.7% | 1.64 | -44.8% |
| Under 2.5 | 66.3% | 39.3% | 2.46 | +63.2% |

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
| Market best home last update utc | 2026-10-11T08:22:18Z |
| Market best draw last update utc | 2026-10-11T08:22:35Z |
| Market best away last update utc | 2026-10-11T08:22:03Z |
| Odds bookmakers 1x2 | 18.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Codere (IT) |
| Best away bookmaker | Betsson |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 23.9% |
| P btts no | 76.1% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.13 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.54 |
| Fair Over 2.5 odds | 2.97 |
| Fair Under 2.5 odds | 1.51 |
| Fair Over 3.5 odds | 6.78 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 17.89 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 5.9% |
| Raw p over 1 5 | 61.3% |
| Raw p under 3 5 | 85.0% |
| Raw p btts yes | 24.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.44 |
| Reference draw odds | 4.70 |
| Reference away odds | 5.60 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.33 |
| Home probability edge | +2.0% |
| Draw probability edge | +2.5% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -27.1% |
| Under 2.5 probability edge | +27.1% |
| Raw edge prob home | 0.0407 |
| Raw ev home | 0.0927 |
| Raw edge prob draw | 0.0496 |
| Raw ev draw | 0.1094 |
| Raw edge prob away | -0.0903 |
| Raw ev away | -0.5991 |
| Market p over 1 5 | 85.2% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-11T08:22:03Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 62.9% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-11T08:22:34Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.38 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 55.9% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-11T08:22:18Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.08 |
| Market btts yes bookmakers | 2 |

</details>


---
