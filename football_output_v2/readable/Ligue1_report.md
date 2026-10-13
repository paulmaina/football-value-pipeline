# Ligue 1 — football model report

Fixtures in this report: **9**.

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

The model's most likely 1X2 outcome is **Le Mans FC win** at **39.2%**. Expected goals are 1.86 for Le Mans FC and 1.48 for Toulouse (3.34 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.5%; Double Chance 1X: 63.5%; Double Chance X2: 60.8%; Under 4.5 goals: 75.9%; BTTS Yes (both teams score): 66.0%; BTTS No (at least one team does not score): 34.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Mans FC win | 39.2% | 2.55 |
| Draw | 24.3% | 4.11 |
| Toulouse win | 36.5% | 2.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Mans FC expected goals | 1.86 |
| Toulouse expected goals | 1.48 |
| Expected total goals | 3.34 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 64.3% |
| Under 2.5 | 35.7% |
| Over 3.5 | 42.5% |
| Under 3.5 | 57.5% |
| Over 4.5 | 24.1% |
| Under 4.5 | 75.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.63% |
| 2 | 1-2 | 8.66% |
| 3 | 2-1 | 7.69% |
| 4 | 2-2 | 7.00% |
| 5 | 0-1 | 5.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Mans FC win | 39.2% | 32.1% | 3.20 | +25.3% |
| Draw | 24.3% | 25.3% | 3.60 | -12.4% |
| Toulouse win | 36.5% | 42.5% | 2.45 | -10.5% |
| Over 2.5 | 64.3% | 55.8% | 1.84 | +18.4% |
| Under 2.5 | 35.7% | 44.2% | 2.15 | -23.3% |

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
| Market best home last update utc | 2026-10-13T07:41:44Z |
| Market best draw last update utc | 2026-10-13T07:42:27Z |
| Market best away last update utc | 2026-10-13T07:41:44Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | LeoVegas (SE) |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Tipico |
| Matched home-team name | Le Mans |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.0% |
| P btts no | 34.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.12 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.59 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.15 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 46.2% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 30.5% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.2% |
| Raw p btts yes | 65.6% |
| P home draw | 63.5% |
| P draw away | 60.8% |
| Raw p home draw | 69.5% |
| Raw p draw away | 53.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Home probability edge | +7.0% |
| Draw probability edge | -1.0% |
| Away probability edge | -6.0% |
| Over 2.5 probability edge | +8.6% |
| Under 2.5 probability edge | -8.6% |
| Raw edge prob home | 0.1406 |
| Raw ev home | 0.4783 |
| Raw edge prob draw | -0.0200 |
| Raw ev draw | -0.1604 |
| Raw edge prob away | -0.1206 |
| Raw ev away | -0.2532 |

</details>


---

## 2026-10-17 — Lille vs Brest

The model's most likely 1X2 outcome is **Lille win** at **55.1%**. Expected goals are 1.75 for Lille and 0.96 for Brest (2.72 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 51.3%; Under 3.5 goals: 71.1%; Double Chance 1X: 78.6%; Double Chance X2: 44.9%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 55.1% | 1.82 |
| Draw | 23.5% | 4.25 |
| Brest win | 21.4% | 4.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.75 |
| Brest expected goals | 0.96 |
| Expected total goals | 2.72 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 51.3% |
| Under 2.5 | 48.7% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.22% |
| 2 | 1-0 | 11.03% |
| 3 | 2-0 | 10.09% |
| 4 | 2-1 | 9.71% |
| 5 | 0-0 | 6.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 55.1% | 54.7% | 1.89 | +4.1% |
| Draw | 23.5% | 22.7% | 4.04 | -4.9% |
| Brest win | 21.4% | 22.7% | 4.40 | -6.0% |
| Over 2.5 | 51.3% | 56.7% | 1.75 | -10.2% |
| Under 2.5 | 48.7% | 43.3% | 2.25 | +9.6% |

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
| Market best home last update utc | 2026-10-13T07:42:42Z |
| Market best draw last update utc | 2026-10-13T07:41:44Z |
| Market best away last update utc | 2026-10-13T07:41:44Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | LeoVegas (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.63 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.15 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.13 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 55.5% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 20.1% |
| Raw p over 1 5 | 75.9% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 51.6% |
| P home draw | 78.6% |
| P draw away | 44.9% |
| Raw p home draw | 79.9% |
| Raw p draw away | 44.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.74 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.90 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.15 |
| Home probability edge | +0.4% |
| Draw probability edge | +0.9% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | 0.0086 |
| Raw ev home | 0.0493 |
| Raw edge prob draw | 0.0176 |
| Raw ev draw | -0.0131 |
| Raw edge prob away | -0.0262 |
| Raw ev away | -0.1176 |

</details>


---

## 2026-10-17 — Strasbourg vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **63.6%**. Expected goals are 1.22 for Strasbourg and 2.10 for Paris Saint Germain (3.33 combined). The most likely exact score is 1-2 at 10.8%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 65.9%; Under 3.5 goals: 56.8%; Double Chance 1X: 36.4%; Double Chance X2: 81.9%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 61.3%; BTTS No (at least one team does not score): 38.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 18.1% | 5.54 |
| Draw | 18.4% | 5.44 |
| Paris Saint Germain win | 63.6% | 1.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.22 |
| Paris Saint Germain expected goals | 2.10 |
| Expected total goals | 3.33 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.9% |
| Under 2.5 | 34.1% |
| Over 3.5 | 43.2% |
| Under 3.5 | 56.8% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.81% |
| 2 | 0-2 | 8.84% |
| 3 | 1-1 | 8.21% |
| 4 | 0-1 | 7.96% |
| 5 | 1-3 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 18.1% | 14.8% | 7.00 | +26.4% |
| Draw | 18.4% | 15.1% | 5.70 | +4.7% |
| Paris Saint Germain win | 63.6% | 70.0% | 1.46 | -7.2% |
| Over 2.5 | 65.9% | 74.7% | 1.33 | -12.3% |
| Under 2.5 | 34.1% | 25.3% | 3.51 | +19.6% |

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
| Market best home last update utc | 2026-10-13T07:42:28Z |
| Market best draw last update utc | 2026-10-13T07:41:59Z |
| Market best away last update utc | 2026-10-13T07:41:44Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Strasbourg |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 61.3% |
| P btts no | 38.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.43 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.78 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 3.99 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 57.2% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.4% |
| P home draw | 36.4% |
| P draw away | 81.9% |
| Raw p home draw | 42.8% |
| Raw p draw away | 78.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 5.60 |
| Reference draw odds | 5.50 |
| Reference away odds | 1.38 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.45 |
| Home probability edge | +3.2% |
| Draw probability edge | +3.2% |
| Away probability edge | -6.4% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | 0.0641 |
| Raw ev home | 0.4883 |
| Raw edge prob draw | 0.0644 |
| Raw ev draw | 0.2303 |
| Raw edge prob away | -0.1285 |
| Raw ev away | -0.1656 |

</details>


---

## 2026-10-17 — Troyes vs RC Lens

The model's most likely 1X2 outcome is **RC Lens win** at **63.5%**. Expected goals are 0.64 for Troyes and 2.21 for RC Lens (2.84 combined). The most likely exact score is 0-2 at 12.3%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 52.0%; Under 3.5 goals: 70.1%; Double Chance 1X: 36.5%; Double Chance X2: 83.7%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 43.6%; BTTS No (at least one team does not score): 56.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 16.3% | 6.15 |
| Draw | 20.2% | 4.95 |
| RC Lens win | 63.5% | 1.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 0.64 |
| RC Lens expected goals | 2.21 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 52.0% |
| Under 2.5 | 48.0% |
| Over 3.5 | 29.9% |
| Under 3.5 | 70.1% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.34% |
| 2 | 0-1 | 10.89% |
| 3 | 1-1 | 9.55% |
| 4 | 0-3 | 9.07% |
| 5 | 1-2 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 16.3% | 23.7% | 4.30 | -30.0% |
| Draw | 20.2% | 22.4% | 4.20 | -15.1% |
| RC Lens win | 63.5% | 54.0% | 1.87 | +18.8% |
| Over 2.5 | 52.0% | 61.6% | 1.64 | -14.7% |
| Under 2.5 | 48.0% | 38.4% | 2.46 | +18.1% |

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
| Market best home last update utc | 2026-10-13T07:41:44Z |
| Market best draw last update utc | 2026-10-13T07:42:28Z |
| Market best away last update utc | 2026-10-13T07:41:44Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Troyes |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 43.6% |
| P btts no | 56.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.44 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.17 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.35 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.76 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 8.9% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 73.0% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 42.2% |
| P home draw | 36.5% |
| P draw away | 83.7% |
| Raw p home draw | 27.0% |
| Raw p draw away | 91.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.75 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.76 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -7.4% |
| Draw probability edge | -2.1% |
| Away probability edge | +9.5% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | -0.1477 |
| Raw ev home | -0.6179 |
| Raw edge prob draw | -0.0427 |
| Raw ev draw | -0.2404 |
| Raw edge prob away | 0.1904 |
| Raw ev away | 0.3656 |

</details>


---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **50.9%**. Expected goals are 0.95 for Angers and 1.71 for Marseille (2.66 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.5%; Under 3.5 goals: 72.7%; Double Chance 1X: 49.1%; Double Chance X2: 75.3%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 24.7% | 4.06 |
| Draw | 24.4% | 4.09 |
| Marseille win | 50.9% | 1.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.95 |
| Marseille expected goals | 1.71 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.4% |
| Under 1.5 | 25.6% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 27.3% |
| Under 3.5 | 72.7% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.64% |
| 2 | 0-1 | 10.68% |
| 3 | 0-2 | 9.53% |
| 4 | 1-2 | 9.01% |
| 5 | 1-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 24.7% | 29.1% | 3.40 | -16.2% |
| Draw | 24.4% | 24.0% | 3.85 | -6.0% |
| Marseille win | 50.9% | 46.9% | 2.20 | +12.0% |
| Over 2.5 | 49.5% | 60.4% | 1.67 | -17.4% |
| Under 2.5 | 50.5% | 39.6% | 2.40 | +21.3% |

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
| Market best home last update utc | 2026-10-13T07:42:14Z |
| Market best draw last update utc | 2026-10-13T07:40:30Z |
| Market best away last update utc | 2026-10-13T07:41:44Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.55 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.91 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.67 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.72 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.2% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 54.9% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.4% |
| Raw p btts yes | 50.6% |
| P home draw | 49.1% |
| P draw away | 75.3% |
| Raw p home draw | 45.1% |
| Raw p draw away | 79.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.32 |
| Home probability edge | -4.4% |
| Draw probability edge | +0.4% |
| Away probability edge | +4.0% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | -0.0886 |
| Raw ev home | -0.3122 |
| Raw edge prob draw | 0.0089 |
| Raw ev draw | -0.0427 |
| Raw edge prob away | 0.0797 |
| Raw ev away | 0.2079 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **38.0%**. Expected goals are 1.17 for Le Havre and 1.17 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 42.0%; Under 3.5 goals: 79.0%; Double Chance 1X: 65.8%; Double Chance X2: 62.0%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 38.0% | 2.63 |
| Draw | 27.8% | 3.60 |
| Auxerre win | 34.2% | 2.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.17 |
| Auxerre expected goals | 1.17 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 68.5% |
| Under 1.5 | 31.5% |
| Over 2.5 | 42.0% |
| Under 2.5 | 58.0% |
| Over 3.5 | 21.0% |
| Under 3.5 | 79.0% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.09% |
| 2 | 1-0 | 11.45% |
| 3 | 0-1 | 10.36% |
| 4 | 0-0 | 9.70% |
| 5 | 2-1 | 8.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 38.0% | 40.4% | 2.52 | -4.3% |
| Draw | 27.8% | 26.4% | 3.60 | +0.1% |
| Auxerre win | 34.2% | 33.2% | 3.00 | +2.7% |
| Over 2.5 | 42.0% | 51.2% | 1.94 | -18.6% |
| Under 2.5 | 58.0% | 48.8% | 2.00 | +16.1% |

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
| Market best home last update utc | 2026-10-13T07:41:44Z |
| Market best draw last update utc | 2026-10-13T07:41:44Z |
| Market best away last update utc | 2026-10-13T07:41:44Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Havre |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.31 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.38 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.77 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.12 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 35.6% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 35.2% |
| Raw p over 1 5 | 68.4% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 48.2% |
| P home draw | 65.8% |
| P draw away | 62.0% |
| Raw p home draw | 64.8% |
| Raw p draw away | 64.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.75 |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.99 |
| Home probability edge | -2.4% |
| Draw probability edge | +1.4% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -9.2% |
| Under 2.5 probability edge | +9.2% |
| Raw edge prob home | -0.0482 |
| Raw ev home | -0.1038 |
| Raw edge prob draw | 0.0283 |
| Raw ev draw | 0.0517 |
| Raw edge prob away | 0.0198 |
| Raw ev away | 0.0567 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **47.2%**. Expected goals are 1.37 for Lorient and 1.80 for AS Monaco (3.17 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.0%; Under 3.5 goals: 60.9%; Double Chance 1X: 52.8%; Double Chance X2: 72.7%; Under 4.5 goals: 78.8%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 27.3% | 3.66 |
| Draw | 25.4% | 3.93 |
| AS Monaco win | 47.2% | 2.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.37 |
| AS Monaco expected goals | 1.80 |
| Expected total goals | 3.17 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.0% |
| Under 2.5 | 39.0% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.2% |
| Under 4.5 | 78.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.50% |
| 2 | 1-2 | 9.32% |
| 3 | 0-1 | 7.09% |
| 4 | 2-2 | 6.81% |
| 5 | 0-2 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 27.3% | 25.8% | 3.95 | +8.0% |
| Draw | 25.4% | 27.0% | 3.60 | -8.4% |
| AS Monaco win | 47.2% | 47.2% | 2.10 | -0.8% |
| Over 2.5 | 61.0% | 50.0% | 1.97 | +20.1% |
| Under 2.5 | 39.0% | 50.0% | 1.97 | -23.1% |

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
| Market best home last update utc | 2026-10-13T07:40:30Z |
| Market best draw last update utc | 2026-10-13T07:41:44Z |
| Market best away last update utc | 2026-10-13T07:41:44Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | BetOnline.ag |
| Best draw bookmaker | LeoVegas (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lorient |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.26 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.71 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 28.9% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 47.2% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 62.8% |
| P home draw | 52.8% |
| P draw away | 72.7% |
| Raw p home draw | 52.8% |
| Raw p draw away | 71.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.50 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.88 |
| Home probability edge | +1.6% |
| Draw probability edge | -1.6% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | +11.0% |
| Under 2.5 probability edge | -11.0% |
| Raw edge prob home | 0.0315 |
| Raw ev home | 0.1422 |
| Raw edge prob draw | -0.0314 |
| Raw ev draw | -0.1406 |
| Raw edge prob away | -0.0001 |
| Raw ev away | -0.0085 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **55.9%**. Expected goals are 1.77 for Lyon and 1.09 for Nice (2.86 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 55.1%; Under 3.5 goals: 67.7%; Double Chance 1X: 78.8%; Double Chance X2: 44.1%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 55.0%; BTTS No (at least one team does not score): 45.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 55.9% | 1.79 |
| Draw | 22.8% | 4.38 |
| Nice win | 21.2% | 4.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.77 |
| Nice expected goals | 1.09 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.81% |
| 2 | 2-1 | 10.34% |
| 3 | 1-0 | 10.24% |
| 4 | 2-0 | 9.52% |
| 5 | 3-1 | 6.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 55.9% | 59.0% | 1.71 | -4.3% |
| Draw | 22.8% | 21.3% | 4.26 | -2.7% |
| Nice win | 21.2% | 19.7% | 5.25 | +11.5% |
| Over 2.5 | 55.1% | 56.3% | 1.72 | -5.3% |
| Under 2.5 | 44.9% | 43.7% | 2.31 | +3.8% |

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
| Market best home last update utc | 2026-10-13T07:41:44Z |
| Market best draw last update utc | 2026-10-13T07:40:30Z |
| Market best away last update utc | 2026-10-13T07:42:27Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lyon |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.0% |
| P btts no | 45.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.14 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.66 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.09 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 52.9% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| P home draw | 78.8% |
| P draw away | 44.1% |
| Raw p home draw | 77.3% |
| Raw p draw away | 47.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.62 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.17 |
| Home probability edge | -3.0% |
| Draw probability edge | +1.5% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -1.3% |
| Under 2.5 probability edge | +1.3% |
| Raw edge prob home | -0.0602 |
| Raw ev home | -0.0949 |
| Raw edge prob draw | 0.0303 |
| Raw ev draw | 0.0370 |
| Raw edge prob away | 0.0300 |
| Raw ev away | 0.1933 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **42.2%**. Expected goals are 1.57 for Paris FC and 1.37 for Rennes (2.94 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 56.0%; Under 3.5 goals: 66.1%; Double Chance 1X: 68.5%; Double Chance X2: 57.8%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 42.2% | 2.37 |
| Draw | 26.4% | 3.79 |
| Rennes win | 31.5% | 3.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.57 |
| Rennes expected goals | 1.37 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 56.0% |
| Under 2.5 | 44.0% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.30% |
| 2 | 2-1 | 9.00% |
| 3 | 1-0 | 7.88% |
| 4 | 1-2 | 7.48% |
| 5 | 2-0 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 42.2% | 42.4% | 2.39 | +0.8% |
| Draw | 26.4% | 27.3% | 3.60 | -5.1% |
| Rennes win | 31.5% | 30.3% | 3.29 | +3.6% |
| Over 2.5 | 56.0% | 57.6% | 1.72 | -3.7% |
| Under 2.5 | 44.0% | 42.4% | 2.30 | +1.2% |

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
| Market best home last update utc | 2026-10-13T07:42:27Z |
| Market best draw last update utc | 2026-10-13T07:42:13Z |
| Market best away last update utc | 2026-10-13T07:41:44Z |
| Odds bookmakers 1x2 | 22.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Codere (IT) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paris FC |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.68 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.77 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 41.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.1% |
| Raw p btts yes | 59.5% |
| P home draw | 68.5% |
| P draw away | 57.8% |
| Raw p home draw | 67.3% |
| Raw p draw away | 58.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.18 |
| Home probability edge | -0.3% |
| Draw probability edge | -0.9% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | -0.0053 |
| Raw ev home | 0.0012 |
| Raw edge prob draw | -0.0187 |
| Raw ev draw | -0.0848 |
| Raw edge prob away | 0.0241 |
| Raw ev away | 0.0754 |

</details>


---
