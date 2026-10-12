# Bundesliga — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 954 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 2887.213 |
| Base scoring parameter | 0.239 |
| Home-advantage parameter | 0.190 |
| Dixon-Coles low-score adjustment | -0.104 |
| Xi per day | 0 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 4.00 |
| Additional event odds calls this league | 0.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-16 — Eintracht Frankfurt vs 1. FC Köln

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **56.1%**. Expected goals are 2.20 for Eintracht Frankfurt and 1.06 for 1. FC Köln (3.26 combined). The most likely exact score is 1-1 at 9.9%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 62.8%; Under 3.5 goals: 59.8%; Double Chance 1X: 77.7%; Double Chance X2: 43.9%; Under 4.5 goals: 77.5%; BTTS Yes (both teams score): 59.6%; BTTS No (at least one team does not score): 40.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 56.1% | 1.78 |
| Draw | 21.6% | 4.64 |
| 1. FC Köln win | 22.3% | 4.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 2.20 |
| 1. FC Köln expected goals | 1.06 |
| Expected total goals | 3.26 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.8% |
| Under 2.5 | 37.2% |
| Over 3.5 | 40.2% |
| Under 3.5 | 59.8% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.94% |
| 2 | 2-1 | 8.87% |
| 3 | 2-0 | 8.38% |
| 4 | 1-0 | 6.78% |
| 5 | 1-2 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 56.1% | 49.9% | 2.04 | +14.5% |
| Draw | 21.6% | 21.7% | 4.30 | -7.3% |
| 1. FC Köln win | 22.3% | 28.5% | 3.65 | -18.4% |
| Over 2.5 | 62.8% | 71.3% | 1.37 | -13.9% |
| Under 2.5 | 37.2% | 28.7% | 3.15 | +17.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-16T18:30:00+00:00 |
| Fixture id | 947bd5d924835af090d9cdc7bbdf10f6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:34Z |
| Market best away last update utc | 2026-10-12T21:08:05Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 81/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 59.6% |
| P btts no | 40.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.81 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.29 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.69 |
| Fair Over 3.5 odds | 2.49 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.44 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 62.3% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 16.2% |
| Raw p over 1 5 | 84.6% |
| Raw p under 3 5 | 59.0% |
| Raw p btts yes | 59.0% |
| P home draw | 77.7% |
| P draw away | 43.9% |
| Raw p home draw | 83.8% |
| Raw p draw away | 37.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.92 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.25 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | +6.2% |
| Draw probability edge | -0.1% |
| Away probability edge | -6.1% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | 0.1244 |
| Raw ev home | 0.2714 |
| Raw edge prob draw | -0.0020 |
| Raw ev draw | -0.0776 |
| Raw edge prob away | -0.1224 |
| Raw ev away | -0.4078 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **75.3%**. Expected goals are 2.79 for Bayern Munich and 1.24 for RB Leipzig (4.02 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 78.0%; Under 3.5 goals: 42.0%; Double Chance 1X: 88.6%; Double Chance X2: 24.7%; Under 4.5 goals: 61.1%; BTTS Yes (both teams score): 66.0%; BTTS No (at least one team does not score): 34.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 75.3% | 1.33 |
| Draw | 13.3% | 7.49 |
| RB Leipzig win | 11.4% | 8.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.79 |
| RB Leipzig expected goals | 1.24 |
| Expected total goals | 4.02 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 92.1% |
| Under 1.5 | 7.9% |
| Over 2.5 | 78.0% |
| Under 2.5 | 22.0% |
| Over 3.5 | 58.0% |
| Under 3.5 | 42.0% |
| Over 4.5 | 38.9% |
| Under 4.5 | 61.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.36% |
| 2 | 3-1 | 8.69% |
| 3 | 2-0 | 7.58% |
| 4 | 3-0 | 7.04% |
| 5 | 4-1 | 6.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 75.3% | 81.4% | 1.26 | -5.2% |
| Draw | 13.3% | 9.6% | 8.50 | +13.5% |
| RB Leipzig win | 11.4% | 9.0% | 11.30 | +28.6% |
| Over 2.5 | 78.0% | 86.7% | 1.15 | -10.3% |
| Under 2.5 | 22.0% | 13.3% | 5.77 | +26.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:30:00+00:00 |
| Fixture id | 9a64448205fdc4b95f45641bb946706c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:19Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Bayern Munich |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.0% |
| P btts no | 34.0% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 52.58 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.60 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.55 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.38 |
| Fair Over 4.5 odds | 2.57 |
| Fair Under 4.5 odds | 1.64 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 13.8% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 42.9% |
| Raw p btts yes | 67.2% |
| P home draw | 88.6% |
| P draw away | 24.7% |
| Raw p home draw | 86.2% |
| Raw p draw away | 30.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.20 |
| Reference draw odds | 8.00 |
| Reference away odds | 8.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.13 |
| Reference Under 2.5 odds | 5.60 |
| Home probability edge | -6.2% |
| Draw probability edge | +3.7% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -8.6% |
| Under 2.5 probability edge | +8.6% |
| Raw edge prob home | -0.1231 |
| Raw ev home | -0.1291 |
| Raw edge prob draw | 0.0749 |
| Raw ev draw | 0.4530 |
| Raw edge prob away | 0.0482 |
| Raw ev away | 0.5582 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **56.2%**. Expected goals are 2.96 for Elversberg and 1.17 for Augsburg (4.13 combined). The most likely exact score is 1-1 at 7.8%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 75.7%; Under 3.5 goals: 43.8%; Double Chance 1X: 75.9%; Double Chance X2: 43.8%; Under 4.5 goals: 63.1%; BTTS Yes (both teams score): 68.6%; BTTS No (at least one team does not score): 31.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 56.2% | 1.78 |
| Draw | 19.6% | 5.10 |
| Augsburg win | 24.1% | 4.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.96 |
| Augsburg expected goals | 1.17 |
| Expected total goals | 4.13 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 75.7% |
| Under 2.5 | 24.3% |
| Over 3.5 | 56.2% |
| Under 3.5 | 43.8% |
| Over 4.5 | 36.9% |
| Under 4.5 | 63.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.80% |
| 2 | 1-2 | 6.90% |
| 3 | 2-1 | 6.34% |
| 4 | 3-1 | 6.26% |
| 5 | 2-2 | 6.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 56.2% | 39.3% | 2.55 | +43.4% |
| Draw | 19.6% | 23.8% | 4.00 | -21.5% |
| Augsburg win | 24.1% | 36.9% | 2.75 | -33.6% |
| Over 2.5 | 75.7% | 67.0% | 1.45 | +9.7% |
| Under 2.5 | 24.3% | 33.0% | 2.79 | -32.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 0bf757f3bd903496ce2fa27bd0481869 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:05Z |
| Market best away last update utc | 2026-10-12T21:08:05Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Elversberg |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 68.6% |
| P btts no | 31.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.94 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.41 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.11 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.28 |
| Fair Over 4.5 odds | 2.71 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 73.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.9% |
| Raw p btts yes | 65.9% |
| P home draw | 75.9% |
| P draw away | 43.8% |
| Raw p home draw | 88.6% |
| Raw p draw away | 26.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.40 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.55 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | +16.9% |
| Draw probability edge | -4.2% |
| Away probability edge | -12.8% |
| Over 2.5 probability edge | +8.6% |
| Under 2.5 probability edge | -8.6% |
| Raw edge prob home | 0.3381 |
| Raw ev home | 0.8655 |
| Raw edge prob draw | -0.0831 |
| Raw ev draw | -0.3813 |
| Raw edge prob away | -0.2550 |
| Raw ev away | -0.6871 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FC Schalke 04 win** at **34.8%**. Expected goals are 0.87 for FC Schalke 04 and 0.69 for FSV Mainz 05 (1.56 combined). The most likely exact score is 0-0 at 18.4%. Goal-market probabilities: at least one goal: 81.6%; Over 2.5 goals: 22.2%; Under 3.5 goals: 92.5%; Double Chance 1X: 66.3%; Double Chance X2: 65.2%; Under 4.5 goals: 97.7%; BTTS Yes (both teams score): 29.0%; BTTS No (at least one team does not score): 71.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 34.8% | 2.88 |
| Draw | 31.5% | 3.18 |
| FSV Mainz 05 win | 33.7% | 2.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| FSV Mainz 05 expected goals | 0.69 |
| Expected total goals | 1.56 |
| Over 0.5 | 81.6% |
| Under 0.5 | 18.4% |
| Over 1.5 | 47.9% |
| Under 1.5 | 52.1% |
| Over 2.5 | 22.2% |
| Under 2.5 | 77.8% |
| Over 3.5 | 7.5% |
| Under 3.5 | 92.5% |
| Over 4.5 | 2.3% |
| Under 4.5 | 97.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.37% |
| 2 | 0-1 | 17.37% |
| 3 | 1-0 | 16.34% |
| 4 | 1-1 | 11.45% |
| 5 | 2-0 | 7.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 34.8% | 33.3% | 3.08 | +7.1% |
| Draw | 31.5% | 24.7% | 3.85 | +21.2% |
| FSV Mainz 05 win | 33.7% | 42.0% | 2.44 | -17.7% |
| Over 2.5 | 22.2% | 59.5% | 1.66 | -63.1% |
| Under 2.5 | 77.8% | 40.5% | 2.42 | +88.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 606d65d57a9a6d8f9b53faee1ad10009 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:18Z |
| Market best draw last update utc | 2026-10-12T21:08:34Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Schalke 04 |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 29.0% |
| P btts no | 71.0% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.44 |
| Fair Over 1.5 odds | 2.09 |
| Fair Under 1.5 odds | 1.92 |
| Fair Over 2.5 odds | 4.50 |
| Fair Under 2.5 odds | 1.29 |
| Fair Over 3.5 odds | 13.37 |
| Fair Under 3.5 odds | 1.08 |
| Fair Over 4.5 odds | 42.93 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 36.3% |
| Unadjusted draw probability | 38.3% |
| Unadjusted away-win probability | 25.4% |
| Raw p over 1 5 | 47.5% |
| Raw p under 3 5 | 92.7% |
| Raw p btts yes | 30.2% |
| P home draw | 66.3% |
| P draw away | 65.2% |
| Raw p home draw | 74.6% |
| Raw p draw away | 63.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.25 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | +1.5% |
| Draw probability edge | +6.8% |
| Away probability edge | -8.3% |
| Over 2.5 probability edge | -37.3% |
| Under 2.5 probability edge | +37.3% |
| Raw edge prob home | 0.0302 |
| Raw ev home | 0.1179 |
| Raw edge prob draw | 0.1356 |
| Raw ev draw | 0.4730 |
| Raw edge prob away | -0.1659 |
| Raw ev away | -0.3791 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **55.3%**. Expected goals are 1.11 for Hamburger SV and 2.02 for VfB Stuttgart (3.13 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.7%; Under 3.5 goals: 62.0%; Double Chance 1X: 44.7%; Double Chance X2: 77.8%; Under 4.5 goals: 79.3%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 22.2% | 4.50 |
| Draw | 22.4% | 4.46 |
| VfB Stuttgart win | 55.3% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.11 |
| VfB Stuttgart expected goals | 2.02 |
| Expected total goals | 3.13 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 60.7% |
| Under 2.5 | 39.3% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.7% |
| Under 4.5 | 79.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.43% |
| 2 | 1-2 | 9.56% |
| 3 | 0-2 | 8.60% |
| 4 | 0-1 | 7.54% |
| 5 | 1-3 | 6.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 22.2% | 25.1% | 4.20 | -6.7% |
| Draw | 22.4% | 21.6% | 4.40 | -1.2% |
| VfB Stuttgart win | 55.3% | 53.4% | 1.90 | +5.2% |
| Over 2.5 | 60.7% | 69.6% | 1.40 | -15.0% |
| Under 2.5 | 39.3% | 30.4% | 3.00 | +17.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 221916b8b36706ec52aa655a64e5f1d2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:05Z |
| Market best draw last update utc | 2026-10-12T21:08:05Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Hamburg |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 88/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.24 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.83 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.83 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 19.4% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 57.3% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 61.8% |
| Raw p btts yes | 59.2% |
| P home draw | 44.7% |
| P draw away | 77.8% |
| Raw p home draw | 42.7% |
| Raw p draw away | 80.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.65 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | -2.9% |
| Draw probability edge | +0.9% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | -0.0571 |
| Raw ev home | -0.1869 |
| Raw edge prob draw | 0.0174 |
| Raw ev draw | 0.0257 |
| Raw edge prob away | 0.0397 |
| Raw ev away | 0.0893 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **59.8%**. Expected goals are 0.94 for Union Berlin and 1.92 for Borussia Dortmund (2.87 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 55.2%; Under 3.5 goals: 67.7%; Double Chance 1X: 40.2%; Double Chance X2: 82.1%; Under 4.5 goals: 83.5%; BTTS Yes (both teams score): 52.8%; BTTS No (at least one team does not score): 47.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.9% | 5.60 |
| Draw | 22.3% | 4.48 |
| Borussia Dortmund win | 59.8% | 1.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.92 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.5% |
| Under 4.5 | 83.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.66% |
| 2 | 0-2 | 10.64% |
| 3 | 1-2 | 10.01% |
| 4 | 0-1 | 9.97% |
| 5 | 0-3 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.9% | 18.9% | 5.40 | -3.5% |
| Draw | 22.3% | 20.8% | 4.50 | +0.6% |
| Borussia Dortmund win | 59.8% | 60.3% | 1.73 | +3.4% |
| Over 2.5 | 55.2% | 64.6% | 1.51 | -16.7% |
| Under 2.5 | 44.8% | 35.4% | 2.61 | +17.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | d8eac776adb07b0e7f01d8736d097291 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:05Z |
| Market best draw last update utc | 2026-10-12T21:08:34Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Union Berlin |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 52.8% |
| P btts no | 47.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.78 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.80 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.07 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 16.8% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 59.3% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 53.2% |
| P home draw | 40.2% |
| P draw away | 82.1% |
| Raw p home draw | 40.7% |
| Raw p draw away | 83.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.70 |
| Reference draw odds | 4.30 |
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Home probability edge | -1.0% |
| Draw probability edge | +1.5% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.0208 |
| Raw ev home | -0.0916 |
| Raw edge prob draw | 0.0309 |
| Raw ev draw | 0.0751 |
| Raw edge prob away | -0.0101 |
| Raw ev away | 0.0257 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **49.3%**. Expected goals are 1.16 for Werder Bremen and 0.74 for SC Paderborn (1.91 combined). The most likely exact score is 1-0 at 17.7%. Goal-market probabilities: at least one goal: 86.5%; Over 2.5 goals: 31.6%; Under 3.5 goals: 87.0%; Double Chance 1X: 77.2%; Double Chance X2: 50.7%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 36.1%; BTTS No (at least one team does not score): 63.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 49.3% | 2.03 |
| Draw | 27.9% | 3.59 |
| SC Paderborn win | 22.8% | 4.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.16 |
| SC Paderborn expected goals | 0.74 |
| Expected total goals | 1.91 |
| Over 0.5 | 86.5% |
| Under 0.5 | 13.5% |
| Over 1.5 | 58.8% |
| Under 1.5 | 41.2% |
| Over 2.5 | 31.6% |
| Under 2.5 | 68.4% |
| Over 3.5 | 13.0% |
| Under 3.5 | 87.0% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.71% |
| 2 | 0-0 | 13.51% |
| 3 | 1-1 | 11.82% |
| 4 | 2-0 | 11.18% |
| 5 | 0-1 | 10.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 49.3% | 54.2% | 1.87 | -7.7% |
| Draw | 27.9% | 22.3% | 4.29 | +19.6% |
| SC Paderborn win | 22.8% | 23.5% | 4.21 | -4.0% |
| Over 2.5 | 31.6% | 63.9% | 1.55 | -51.1% |
| Under 2.5 | 68.4% | 36.1% | 2.56 | +75.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:30:00+00:00 |
| Fixture id | 9a422e1aad1053828eaf629a58d901de |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:34Z |
| Market best draw last update utc | 2026-10-12T21:08:19Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 36.1% |
| P btts no | 63.9% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.40 |
| Fair Over 1.5 odds | 1.70 |
| Fair Under 1.5 odds | 2.43 |
| Fair Over 2.5 odds | 3.17 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.71 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.94 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 44.5% |
| Unadjusted draw probability | 33.4% |
| Unadjusted away-win probability | 22.1% |
| Raw p over 1 5 | 58.1% |
| Raw p under 3 5 | 87.4% |
| Raw p btts yes | 37.4% |
| P home draw | 77.2% |
| P draw away | 50.7% |
| Raw p home draw | 77.9% |
| Raw p draw away | 55.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.78 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.90 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.52 |
| Home probability edge | -4.8% |
| Draw probability edge | +5.6% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -32.4% |
| Under 2.5 probability edge | +32.4% |
| Raw edge prob home | -0.0967 |
| Raw ev home | -0.1678 |
| Raw edge prob draw | 0.1112 |
| Raw ev draw | 0.4342 |
| Raw edge prob away | -0.0146 |
| Raw ev away | -0.0710 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **62.9%**. Expected goals are 2.44 for Bayer Leverkusen and 0.96 for SC Freiburg (3.41 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 65.3%; Under 3.5 goals: 56.8%; Double Chance 1X: 82.8%; Double Chance X2: 37.1%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 58.2%; BTTS No (at least one team does not score): 41.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 62.9% | 1.59 |
| Draw | 19.9% | 5.02 |
| SC Freiburg win | 17.2% | 5.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.44 |
| SC Freiburg expected goals | 0.96 |
| Expected total goals | 3.41 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 85.6% |
| Under 1.5 | 14.4% |
| Over 2.5 | 65.3% |
| Under 2.5 | 34.7% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.16% |
| 2 | 2-0 | 9.02% |
| 3 | 2-1 | 8.68% |
| 4 | 3-0 | 7.34% |
| 5 | 3-1 | 7.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 62.9% | 56.8% | 1.77 | +11.4% |
| Draw | 19.9% | 21.1% | 4.42 | -12.0% |
| SC Freiburg win | 17.2% | 22.2% | 4.62 | -20.6% |
| Over 2.5 | 65.3% | 65.1% | 1.49 | -2.8% |
| Under 2.5 | 34.7% | 34.9% | 2.65 | -7.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:30:00+00:00 |
| Fixture id | 096d800bcc95c547ef592cbef624d080 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:19Z |
| Market best draw last update utc | 2026-10-12T21:08:34Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Matchbook |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Leverkusen |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.2% |
| P btts no | 41.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.77 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.95 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.88 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.01 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.7% |
| Raw p btts yes | 57.3% |
| P home draw | 82.8% |
| P draw away | 37.1% |
| Raw p home draw | 87.8% |
| Raw p draw away | 30.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.70 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | +6.2% |
| Draw probability edge | -1.2% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.1232 |
| Raw ev home | 0.2227 |
| Raw edge prob draw | -0.0234 |
| Raw ev draw | -0.1718 |
| Raw edge prob away | -0.0999 |
| Raw ev away | -0.4370 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **41.5%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 72.0%; Under 3.5 goals: 48.9%; Double Chance 1X: 58.5%; Double Chance X2: 64.5%; Under 4.5 goals: 68.2%; BTTS Yes (both teams score): 72.2%; BTTS No (at least one team does not score): 27.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 35.5% | 2.82 |
| Draw | 22.9% | 4.36 |
| TSG Hoffenheim win | 41.5% | 2.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.94 |
| TSG Hoffenheim expected goals | 1.79 |
| Expected total goals | 3.73 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 89.5% |
| Under 1.5 | 10.5% |
| Over 2.5 | 72.0% |
| Under 2.5 | 28.0% |
| Over 3.5 | 51.1% |
| Under 3.5 | 48.9% |
| Over 4.5 | 31.8% |
| Under 4.5 | 68.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.11% |
| 2 | 1-2 | 8.75% |
| 3 | 2-2 | 7.14% |
| 4 | 2-1 | 6.95% |
| 5 | 1-3 | 5.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 35.5% | 29.8% | 3.45 | +22.6% |
| Draw | 22.9% | 22.6% | 4.30 | -1.4% |
| TSG Hoffenheim win | 41.5% | 47.6% | 2.12 | -11.9% |
| Over 2.5 | 72.0% | 70.2% | 1.40 | +0.7% |
| Under 2.5 | 28.0% | 29.8% | 3.05 | -14.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | fd9b8c185737a15615aa0c9daaa3dfbf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:05Z |
| Market best draw last update utc | 2026-10-12T21:07:35Z |
| Market best away last update utc | 2026-10-12T21:08:34Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | M'gladbach |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 72.2% |
| P btts no | 27.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.85 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.49 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.57 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 41.3% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.9% |
| Raw p btts yes | 72.2% |
| P home draw | 58.5% |
| P draw away | 64.5% |
| Raw p home draw | 64.5% |
| Raw p draw away | 58.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.10 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +5.8% |
| Draw probability edge | +0.3% |
| Away probability edge | -6.0% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | 0.1152 |
| Raw ev home | 0.4243 |
| Raw edge prob draw | 0.0056 |
| Raw ev draw | -0.0018 |
| Raw edge prob away | -0.1209 |
| Raw ev away | -0.2473 |

</details>


---
