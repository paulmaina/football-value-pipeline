# Bundesliga — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 963 |
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
| Optimizer objective | 1719.052 |
| Base scoring parameter | 0.238 |
| Home-advantage parameter | 0.200 |
| Dixon-Coles low-score adjustment | -0.084 |
| Xi per day | 0.0009 |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Additional event odds calls used before this league | 0.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
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

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **54.6%**. Expected goals are 2.24 for Eintracht Frankfurt and 1.24 for 1. FC Köln (3.48 combined). The most likely exact score is 1-1 at 9.7%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 67.0%; Under 3.5 goals: 54.6%; Double Chance 1X: 76.8%; Double Chance X2: 45.4%; Under 4.5 goals: 73.3%; BTTS Yes (both teams score): 64.8%; BTTS No (at least one team does not score): 35.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 54.6% | 1.83 |
| Draw | 22.2% | 4.50 |
| 1. FC Köln win | 23.2% | 4.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 2.24 |
| 1. FC Köln expected goals | 1.24 |
| Expected total goals | 3.48 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 67.0% |
| Under 2.5 | 33.0% |
| Over 3.5 | 45.4% |
| Under 3.5 | 54.6% |
| Over 4.5 | 26.7% |
| Under 4.5 | 73.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.71% |
| 2 | 2-1 | 8.84% |
| 3 | 2-0 | 7.12% |
| 4 | 3-1 | 6.60% |
| 5 | 1-2 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 54.6% | 50.0% | 2.04 | +11.4% |
| Draw | 22.2% | 23.2% | 4.30 | -4.4% |
| 1. FC Köln win | 23.2% | 26.7% | 3.65 | -15.4% |
| Over 2.5 | 67.0% | 71.3% | 1.37 | -8.2% |
| Under 2.5 | 33.0% | 28.7% | 3.15 | +3.9% |

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
| Market best home last update utc | 2026-10-13T07:42:40Z |
| Market best draw last update utc | 2026-10-13T07:40:57Z |
| Market best away last update utc | 2026-10-13T07:41:42Z |
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
| P btts yes | 64.8% |
| P btts no | 35.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.16 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.50 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.03 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.75 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 59.2% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 19.6% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.1% |
| Raw p btts yes | 64.3% |
| P home draw | 76.8% |
| P draw away | 45.4% |
| Raw p home draw | 80.4% |
| Raw p draw away | 40.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.93 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | +4.6% |
| Draw probability edge | -1.0% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | 0.0915 |
| Raw ev home | 0.2074 |
| Raw edge prob draw | -0.0201 |
| Raw ev draw | -0.0876 |
| Raw edge prob away | -0.0714 |
| Raw ev away | -0.2848 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **76.2%**. Expected goals are 2.86 for Bayern Munich and 1.24 for RB Leipzig (4.10 combined). The most likely exact score is 2-1 at 9.1%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 78.9%; Under 3.5 goals: 40.5%; Double Chance 1X: 89.2%; Double Chance X2: 23.8%; Under 4.5 goals: 59.7%; BTTS Yes (both teams score): 66.3%; BTTS No (at least one team does not score): 33.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 76.2% | 1.31 |
| Draw | 13.0% | 7.67 |
| RB Leipzig win | 10.8% | 9.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.86 |
| RB Leipzig expected goals | 1.24 |
| Expected total goals | 4.10 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 92.4% |
| Under 1.5 | 7.6% |
| Over 2.5 | 78.9% |
| Under 2.5 | 21.1% |
| Over 3.5 | 59.5% |
| Under 3.5 | 40.5% |
| Over 4.5 | 40.3% |
| Under 4.5 | 59.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.10% |
| 2 | 3-1 | 8.68% |
| 3 | 2-0 | 7.35% |
| 4 | 3-0 | 7.01% |
| 5 | 4-1 | 6.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 76.2% | 82.0% | 1.26 | -4.0% |
| Draw | 13.0% | 9.8% | 8.50 | +10.8% |
| RB Leipzig win | 10.8% | 8.2% | 11.30 | +21.6% |
| Over 2.5 | 78.9% | 85.4% | 1.15 | -9.2% |
| Under 2.5 | 21.1% | 14.6% | 5.83 | +22.8% |

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
| Market best home last update utc | 2026-10-13T07:40:57Z |
| Market best draw last update utc | 2026-10-13T07:42:40Z |
| Market best away last update utc | 2026-10-13T07:40:57Z |
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
| P btts yes | 66.3% |
| P btts no | 33.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 58.09 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.18 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.75 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.47 |
| Fair Over 4.5 odds | 2.48 |
| Fair Under 4.5 odds | 1.67 |
| Unadjusted home-win probability | 70.4% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 92.0% |
| Raw p under 3 5 | 41.4% |
| Raw p btts yes | 67.4% |
| P home draw | 89.2% |
| P draw away | 23.8% |
| Raw p home draw | 86.7% |
| Raw p draw away | 29.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.20 |
| Reference draw odds | 8.50 |
| Reference away odds | 10.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.50 |
| Home probability edge | -5.8% |
| Draw probability edge | +3.3% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.1166 |
| Raw ev home | -0.1133 |
| Raw edge prob draw | 0.0652 |
| Raw ev draw | 0.3856 |
| Raw edge prob away | 0.0513 |
| Raw ev away | 0.5059 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **47.8%**. Expected goals are 2.05 for Elversberg and 1.15 for Augsburg (3.20 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 61.0%; Under 3.5 goals: 61.2%; Double Chance 1X: 72.1%; Double Chance X2: 52.2%; Under 4.5 goals: 78.8%; BTTS Yes (both teams score): 61.3%; BTTS No (at least one team does not score): 38.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 47.8% | 2.09 |
| Draw | 24.3% | 4.11 |
| Augsburg win | 27.9% | 3.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.05 |
| Augsburg expected goals | 1.15 |
| Expected total goals | 3.20 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 61.0% |
| Under 2.5 | 39.0% |
| Over 3.5 | 38.8% |
| Under 3.5 | 61.2% |
| Over 4.5 | 21.2% |
| Under 4.5 | 78.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.16% |
| 2 | 2-1 | 8.20% |
| 3 | 1-2 | 7.71% |
| 4 | 2-0 | 7.13% |
| 5 | 1-0 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 47.8% | 38.1% | 2.55 | +21.8% |
| Draw | 24.3% | 26.0% | 4.00 | -2.7% |
| Augsburg win | 27.9% | 35.9% | 2.75 | -23.3% |
| Over 2.5 | 61.0% | 66.7% | 1.45 | -11.5% |
| Under 2.5 | 39.0% | 33.3% | 2.79 | +8.7% |

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
| Market best home last update utc | 2026-10-13T07:40:57Z |
| Market best draw last update utc | 2026-10-13T07:41:42Z |
| Market best away last update utc | 2026-10-13T07:41:42Z |
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
| P btts yes | 61.3% |
| P btts no | 38.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.13 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.91 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.57 |
| Fair Over 3.5 odds | 2.58 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.71 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 57.4% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 19.9% |
| Raw p over 1 5 | 83.7% |
| Raw p under 3 5 | 60.2% |
| Raw p btts yes | 60.4% |
| P home draw | 72.1% |
| P draw away | 52.2% |
| Raw p home draw | 80.1% |
| Raw p draw away | 42.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.50 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | +9.6% |
| Draw probability edge | -1.7% |
| Away probability edge | -8.0% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | 0.1928 |
| Raw ev home | 0.4643 |
| Raw edge prob draw | -0.0334 |
| Raw ev draw | -0.0940 |
| Raw edge prob away | -0.1594 |
| Raw ev away | -0.4519 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **37.2%**. Expected goals are 0.95 for FC Schalke 04 and 0.92 for FSV Mainz 05 (1.87 combined). The most likely exact score is 0-1 at 15.2%. Goal-market probabilities: at least one goal: 85.4%; Over 2.5 goals: 29.9%; Under 3.5 goals: 87.9%; Double Chance 1X: 62.8%; Double Chance X2: 67.4%; Under 4.5 goals: 95.7%; BTTS Yes (both teams score): 37.0%; BTTS No (at least one team does not score): 63.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 32.6% | 3.07 |
| Draw | 30.2% | 3.31 |
| FSV Mainz 05 win | 37.2% | 2.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.95 |
| FSV Mainz 05 expected goals | 0.92 |
| Expected total goals | 1.87 |
| Over 0.5 | 85.4% |
| Under 0.5 | 14.6% |
| Over 1.5 | 57.1% |
| Under 1.5 | 42.9% |
| Over 2.5 | 29.9% |
| Under 2.5 | 70.1% |
| Over 3.5 | 12.1% |
| Under 3.5 | 87.9% |
| Over 4.5 | 4.3% |
| Under 4.5 | 95.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.24% |
| 2 | 0-0 | 14.57% |
| 3 | 1-0 | 13.12% |
| 4 | 1-1 | 12.80% |
| 5 | 0-2 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 32.6% | 31.5% | 3.10 | +1.0% |
| Draw | 30.2% | 26.0% | 3.85 | +16.3% |
| FSV Mainz 05 win | 37.2% | 42.6% | 2.44 | -9.2% |
| Over 2.5 | 29.9% | 59.5% | 1.66 | -50.3% |
| Under 2.5 | 70.1% | 40.5% | 2.42 | +69.6% |

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
| Market best home last update utc | 2026-10-13T07:42:40Z |
| Market best draw last update utc | 2026-10-13T07:42:40Z |
| Market best away last update utc | 2026-10-13T07:40:57Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Schalke 04 |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 37.0% |
| P btts no | 63.0% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.86 |
| Fair Over 1.5 odds | 1.75 |
| Fair Under 1.5 odds | 2.33 |
| Fair Over 2.5 odds | 3.34 |
| Fair Under 2.5 odds | 1.43 |
| Fair Over 3.5 odds | 8.27 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.04 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 34.4% |
| Unadjusted away-win probability | 31.9% |
| Raw p over 1 5 | 56.8% |
| Raw p under 3 5 | 88.1% |
| Raw p btts yes | 37.9% |
| P home draw | 62.8% |
| P draw away | 67.4% |
| Raw p home draw | 68.1% |
| Raw p draw away | 66.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.00 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.25 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.36 |
| Home probability edge | +1.1% |
| Draw probability edge | +4.2% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | -29.5% |
| Under 2.5 probability edge | +29.5% |
| Raw edge prob home | 0.0222 |
| Raw ev home | 0.0440 |
| Raw edge prob draw | 0.0848 |
| Raw ev draw | 0.3258 |
| Raw edge prob away | -0.1070 |
| Raw ev away | -0.2220 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **54.8%**. Expected goals are 1.17 for Hamburger SV and 2.00 for VfB Stuttgart (3.17 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.5%; Under 3.5 goals: 60.9%; Double Chance 1X: 45.2%; Double Chance X2: 77.6%; Under 4.5 goals: 78.5%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 22.4% | 4.47 |
| Draw | 22.8% | 4.38 |
| VfB Stuttgart win | 54.8% | 1.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.17 |
| VfB Stuttgart expected goals | 2.00 |
| Expected total goals | 3.17 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.5% |
| Under 4.5 | 78.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.49% |
| 2 | 1-2 | 9.64% |
| 3 | 0-2 | 8.24% |
| 4 | 0-1 | 7.42% |
| 5 | 1-3 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 22.4% | 23.7% | 4.20 | -6.0% |
| Draw | 22.8% | 22.5% | 4.40 | +0.4% |
| VfB Stuttgart win | 54.8% | 53.7% | 1.90 | +4.1% |
| Over 2.5 | 61.5% | 70.8% | 1.40 | -13.9% |
| Under 2.5 | 38.5% | 29.2% | 3.00 | +15.4% |

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
| Market best home last update utc | 2026-10-13T07:41:42Z |
| Market best draw last update utc | 2026-10-13T07:41:42Z |
| Market best away last update utc | 2026-10-13T07:40:57Z |
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
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.24 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.99 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.66 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 55.8% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 60.5% |
| P home draw | 45.2% |
| P draw away | 77.6% |
| Raw p home draw | 44.2% |
| Raw p draw away | 79.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.90 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -1.4% |
| Draw probability edge | +0.3% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.0271 |
| Raw ev home | -0.1166 |
| Raw edge prob draw | 0.0062 |
| Raw ev draw | 0.0180 |
| Raw edge prob away | 0.0209 |
| Raw ev away | 0.0608 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **60.0%**. Expected goals are 0.94 for Union Berlin and 1.94 for Borussia Dortmund (2.88 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 55.3%; Under 3.5 goals: 67.4%; Double Chance 1X: 40.0%; Double Chance X2: 82.3%; Under 4.5 goals: 83.4%; BTTS Yes (both teams score): 52.8%; BTTS No (at least one team does not score): 47.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.7% | 5.65 |
| Draw | 22.3% | 4.48 |
| Borussia Dortmund win | 60.0% | 1.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.94 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.3% |
| Under 2.5 | 44.7% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.64% |
| 2 | 0-2 | 10.58% |
| 3 | 0-1 | 10.05% |
| 4 | 1-2 | 9.94% |
| 5 | 0-3 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.7% | 18.6% | 5.40 | -4.4% |
| Draw | 22.3% | 21.4% | 4.52 | +0.9% |
| Borussia Dortmund win | 60.0% | 60.0% | 1.69 | +1.3% |
| Over 2.5 | 55.3% | 63.8% | 1.51 | -16.6% |
| Under 2.5 | 44.7% | 36.2% | 2.61 | +16.8% |

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
| Market best home last update utc | 2026-10-13T07:41:42Z |
| Market best draw last update utc | 2026-10-13T07:40:57Z |
| Market best away last update utc | 2026-10-13T07:40:57Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | 1xBet |
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
| Fair Under 0.5 odds | 16.11 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.78 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.02 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 16.8% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 59.9% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 53.0% |
| P home draw | 40.0% |
| P draw away | 82.3% |
| Raw p home draw | 40.1% |
| Raw p draw away | 83.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 4.90 |
| Reference draw odds | 4.30 |
| Reference away odds | 1.62 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -0.9% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -8.5% |
| Under 2.5 probability edge | +8.5% |
| Raw edge prob home | -0.0181 |
| Raw ev home | -0.0927 |
| Raw edge prob draw | 0.0192 |
| Raw ev draw | 0.0527 |
| Raw edge prob away | -0.0012 |
| Raw ev away | 0.0124 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **53.2%**. Expected goals are 1.24 for Werder Bremen and 0.61 for SC Paderborn (1.85 combined). The most likely exact score is 1-0 at 19.4%. Goal-market probabilities: at least one goal: 85.9%; Over 2.5 goals: 29.7%; Under 3.5 goals: 88.1%; Double Chance 1X: 80.2%; Double Chance X2: 46.8%; Under 4.5 goals: 95.8%; BTTS Yes (both teams score): 32.3%; BTTS No (at least one team does not score): 67.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 53.2% | 1.88 |
| Draw | 27.0% | 3.70 |
| SC Paderborn win | 19.8% | 5.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.24 |
| SC Paderborn expected goals | 0.61 |
| Expected total goals | 1.85 |
| Over 0.5 | 85.9% |
| Under 0.5 | 14.1% |
| Over 1.5 | 56.6% |
| Under 1.5 | 43.4% |
| Over 2.5 | 29.7% |
| Under 2.5 | 70.3% |
| Over 3.5 | 11.9% |
| Under 3.5 | 88.1% |
| Over 4.5 | 4.2% |
| Under 4.5 | 95.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.41% |
| 2 | 0-0 | 14.13% |
| 3 | 2-0 | 12.71% |
| 4 | 1-1 | 10.84% |
| 5 | 0-1 | 9.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 53.2% | 55.4% | 1.85 | -1.7% |
| Draw | 27.0% | 22.0% | 4.29 | +15.9% |
| SC Paderborn win | 19.8% | 22.6% | 4.21 | -16.5% |
| Over 2.5 | 29.7% | 61.8% | 1.55 | -54.0% |
| Under 2.5 | 70.3% | 38.2% | 2.56 | +80.0% |

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
| Market best home last update utc | 2026-10-13T07:41:42Z |
| Market best draw last update utc | 2026-10-13T07:42:11Z |
| Market best away last update utc | 2026-10-13T07:40:57Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.3% |
| P btts no | 67.7% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.08 |
| Fair Over 1.5 odds | 1.77 |
| Fair Under 1.5 odds | 2.30 |
| Fair Over 2.5 odds | 3.37 |
| Fair Under 2.5 odds | 1.42 |
| Fair Over 3.5 odds | 8.42 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 23.69 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 50.9% |
| Unadjusted draw probability | 32.0% |
| Unadjusted away-win probability | 17.1% |
| Raw p over 1 5 | 56.1% |
| Raw p under 3 5 | 88.3% |
| Raw p btts yes | 33.3% |
| P home draw | 80.2% |
| P draw away | 46.8% |
| Raw p home draw | 82.9% |
| Raw p draw away | 49.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.75 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -2.3% |
| Draw probability edge | +5.0% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | -32.1% |
| Under 2.5 probability edge | +32.1% |
| Raw edge prob home | -0.0451 |
| Raw ev home | -0.0583 |
| Raw edge prob draw | 0.1000 |
| Raw ev draw | 0.3731 |
| Raw edge prob away | -0.0549 |
| Raw ev away | -0.2806 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **61.5%**. Expected goals are 2.40 for Bayer Leverkusen and 1.08 for SC Freiburg (3.48 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 66.7%; Under 3.5 goals: 54.8%; Double Chance 1X: 82.2%; Double Chance X2: 38.5%; Under 4.5 goals: 73.6%; BTTS Yes (both teams score): 61.3%; BTTS No (at least one team does not score): 38.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 61.5% | 1.63 |
| Draw | 20.7% | 4.84 |
| SC Freiburg win | 17.8% | 5.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.40 |
| SC Freiburg expected goals | 1.08 |
| Expected total goals | 3.48 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 86.5% |
| Under 1.5 | 13.5% |
| Over 2.5 | 66.7% |
| Under 2.5 | 33.3% |
| Over 3.5 | 45.2% |
| Under 3.5 | 54.8% |
| Over 4.5 | 26.4% |
| Under 4.5 | 73.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.25% |
| 2 | 2-1 | 8.94% |
| 3 | 2-0 | 8.31% |
| 4 | 3-1 | 7.15% |
| 5 | 3-0 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 61.5% | 57.1% | 1.77 | +8.9% |
| Draw | 20.7% | 22.0% | 4.42 | -8.7% |
| SC Freiburg win | 17.8% | 20.9% | 4.62 | -17.7% |
| Over 2.5 | 66.7% | 66.3% | 1.48 | -1.2% |
| Under 2.5 | 33.3% | 33.7% | 2.69 | -10.5% |

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
| Market best home last update utc | 2026-10-13T07:42:25Z |
| Market best draw last update utc | 2026-10-13T07:40:57Z |
| Market best away last update utc | 2026-10-13T07:40:57Z |
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
| P btts yes | 61.3% |
| P btts no | 38.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.88 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.39 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 3.01 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.82 |
| Fair Over 4.5 odds | 3.78 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 65.9% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 14.7% |
| Raw p over 1 5 | 86.8% |
| Raw p under 3 5 | 54.2% |
| Raw p btts yes | 60.6% |
| P home draw | 82.2% |
| P draw away | 38.5% |
| Raw p home draw | 85.3% |
| Raw p draw away | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.70 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | +4.4% |
| Draw probability edge | -1.3% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0884 |
| Raw ev home | 0.1672 |
| Raw edge prob draw | -0.0265 |
| Raw ev draw | -0.1457 |
| Raw edge prob away | -0.0619 |
| Raw ev away | -0.3196 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **41.7%**. Expected goals are 1.87 for Borussia Monchengladbach and 1.78 for TSG Hoffenheim (3.65 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.5%; Double Chance 1X: 58.3%; Double Chance X2: 64.8%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 71.1%; BTTS No (at least one team does not score): 28.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 35.2% | 2.84 |
| Draw | 23.1% | 4.32 |
| TSG Hoffenheim win | 41.7% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.87 |
| TSG Hoffenheim expected goals | 1.78 |
| Expected total goals | 3.65 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 70.6% |
| Under 2.5 | 29.4% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.35% |
| 2 | 1-2 | 8.77% |
| 3 | 2-2 | 7.17% |
| 4 | 2-1 | 7.08% |
| 5 | 1-3 | 5.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 35.2% | 30.2% | 3.45 | +21.3% |
| Draw | 23.1% | 23.0% | 4.30 | -0.6% |
| TSG Hoffenheim win | 41.7% | 46.8% | 2.10 | -12.4% |
| Over 2.5 | 70.6% | 68.5% | 1.40 | -1.2% |
| Under 2.5 | 29.4% | 31.5% | 2.99 | -12.1% |

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
| Market best home last update utc | 2026-10-13T07:41:42Z |
| Market best draw last update utc | 2026-10-13T07:42:26Z |
| Market best away last update utc | 2026-10-13T07:42:40Z |
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
| P btts yes | 71.1% |
| P btts no | 28.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.14 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.78 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.40 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 36.6% |
| Raw p over 1 5 | 88.6% |
| Raw p under 3 5 | 50.5% |
| Raw p btts yes | 71.0% |
| P home draw | 58.3% |
| P draw away | 64.8% |
| Raw p home draw | 63.4% |
| Raw p draw away | 59.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.10 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.05 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | +5.0% |
| Draw probability edge | +0.1% |
| Away probability edge | -5.1% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | 0.0997 |
| Raw ev home | 0.3855 |
| Raw edge prob draw | 0.0016 |
| Raw ev draw | -0.0021 |
| Raw edge prob away | -0.1013 |
| Raw ev away | -0.2307 |

</details>


---
