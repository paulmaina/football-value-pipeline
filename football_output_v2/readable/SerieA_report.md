# Serie A — football model report

Fixtures in this report: **10**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,190 |
| Training data through | 2026-09-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 879.078 |
| Base scoring parameter | 0.134 |
| Home-advantage parameter | 0.091 |
| Dixon-Coles low-score adjustment | 0.005 |
| Xi per day | 0.0029 |
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
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-16 — Frosinone vs Sassuolo

The model's most likely 1X2 outcome is **Frosinone win** at **46.0%**. Expected goals are 1.84 for Frosinone and 1.12 for Sassuolo (2.95 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 55.6%; Under 3.5 goals: 66.5%; Double Chance 1X: 70.7%; Double Chance X2: 54.0%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 46.0% | 2.17 |
| Draw | 24.6% | 4.06 |
| Sassuolo win | 29.3% | 3.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.84 |
| Sassuolo expected goals | 1.12 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 78.7% |
| Under 1.5 | 21.3% |
| Over 2.5 | 55.6% |
| Under 2.5 | 44.4% |
| Over 3.5 | 33.5% |
| Under 3.5 | 66.5% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.54% |
| 2 | 2-1 | 8.33% |
| 3 | 1-0 | 8.18% |
| 4 | 1-2 | 7.61% |
| 5 | 0-1 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 46.0% | 37.8% | 2.68 | +23.3% |
| Draw | 24.6% | 26.6% | 3.80 | -6.4% |
| Sassuolo win | 29.3% | 35.7% | 2.80 | -17.8% |
| Over 2.5 | 55.6% | 63.5% | 1.51 | -16.1% |
| Under 2.5 | 44.4% | 36.5% | 2.71 | +20.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-16T18:45:00+00:00 |
| Fixture id | 7d3160040958fe21778fd5ee485666c3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:24Z |
| Market best away last update utc | 2026-10-12T21:08:22Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Unibet (SE) |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Frosinone |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.85 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.70 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 2.99 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.85 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 54.3% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 23.0% |
| Raw p over 1 5 | 79.3% |
| Raw p under 3 5 | 65.8% |
| Raw p btts yes | 56.5% |
| P home draw | 70.7% |
| P draw away | 54.0% |
| Raw p home draw | 77.0% |
| Raw p draw away | 45.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.57 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.72 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | +8.2% |
| Draw probability edge | -1.9% |
| Away probability edge | -6.3% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | 0.1646 |
| Raw ev home | 0.4540 |
| Raw edge prob draw | -0.0383 |
| Raw ev draw | -0.1367 |
| Raw edge prob away | -0.1262 |
| Raw ev away | -0.3552 |

</details>


---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **69.9%**. Expected goals are 2.01 for AS Roma and 0.66 for Genoa (2.67 combined). The most likely exact score is 1-0 at 14.1%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 50.2%; Under 3.5 goals: 72.0%; Double Chance 1X: 88.6%; Double Chance X2: 30.1%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 41.6%; BTTS No (at least one team does not score): 58.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 69.9% | 1.43 |
| Draw | 18.7% | 5.35 |
| Genoa win | 11.4% | 8.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 2.01 |
| Genoa expected goals | 0.66 |
| Expected total goals | 2.67 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 50.2% |
| Under 2.5 | 49.8% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.14% |
| 2 | 2-0 | 14.14% |
| 3 | 3-0 | 9.45% |
| 4 | 2-1 | 9.35% |
| 5 | 1-1 | 8.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 69.9% | 70.8% | 1.41 | -1.4% |
| Draw | 18.7% | 17.8% | 5.30 | -0.9% |
| Genoa win | 11.4% | 11.4% | 10.00 | +13.6% |
| Over 2.5 | 50.2% | 56.8% | 1.74 | -12.6% |
| Under 2.5 | 49.8% | 43.2% | 2.27 | +13.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | 18d478f469da3bcc654dd4555b85c7e3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:24Z |
| Market best away last update utc | 2026-10-12T21:08:37Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.6% |
| P btts no | 58.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.21 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.48 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 19.6% |
| Unadjusted away-win probability | 11.3% |
| Raw p over 1 5 | 74.5% |
| Raw p under 3 5 | 72.1% |
| Raw p btts yes | 41.8% |
| P home draw | 88.6% |
| P draw away | 30.1% |
| Raw p home draw | 88.7% |
| Raw p draw away | 30.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.39 |
| Reference draw odds | 5.18 |
| Reference away odds | 7.91 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.08 |
| Home probability edge | -0.8% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.0168 |
| Raw ev home | -0.0257 |
| Raw edge prob draw | 0.0180 |
| Raw ev draw | 0.0388 |
| Raw edge prob away | -0.0012 |
| Raw ev away | 0.1301 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.5%**. Expected goals are 1.07 for Bologna and 2.13 for Inter Milan (3.21 combined). The most likely exact score is 1-1 at 9.9%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.1%; Double Chance 1X: 38.5%; Double Chance X2: 83.1%; Under 4.5 goals: 78.2%; BTTS Yes (both teams score): 58.3%; BTTS No (at least one team does not score): 41.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 16.9% | 5.92 |
| Draw | 21.6% | 4.63 |
| Inter Milan win | 61.5% | 1.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.07 |
| Inter Milan expected goals | 2.13 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.7% |
| Under 2.5 | 38.3% |
| Over 3.5 | 39.9% |
| Under 3.5 | 60.1% |
| Over 4.5 | 21.8% |
| Under 4.5 | 78.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.91% |
| 2 | 1-2 | 9.87% |
| 3 | 0-2 | 9.20% |
| 4 | 0-1 | 8.67% |
| 5 | 1-3 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 16.9% | 15.6% | 6.15 | +4.0% |
| Draw | 21.6% | 23.1% | 4.30 | -7.2% |
| Inter Milan win | 61.5% | 61.4% | 1.65 | +1.5% |
| Over 2.5 | 61.7% | 58.7% | 1.71 | +5.5% |
| Under 2.5 | 38.3% | 41.3% | 2.33 | -10.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:00:00+00:00 |
| Fixture id | bfefc309177723410230fee52f650315 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:22Z |
| Market best draw last update utc | 2026-10-12T21:08:52Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | BetOnline.ag |
| Best draw bookmaker | Codere (IT) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bologna |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.3% |
| P btts no | 41.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.25 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.58 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 61.7% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 60.1% |
| Raw p btts yes | 57.9% |
| P home draw | 38.5% |
| P draw away | 83.1% |
| Raw p home draw | 38.3% |
| Raw p draw away | 81.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.99 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.16 |
| Home probability edge | +1.3% |
| Draw probability edge | -1.5% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | 0.0268 |
| Raw ev home | 0.1220 |
| Raw edge prob draw | -0.0299 |
| Raw ev draw | -0.1361 |
| Raw edge prob away | 0.0031 |
| Raw ev away | 0.0175 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **65.2%**. Expected goals are 0.67 for Venezia and 2.18 for Napoli (2.85 combined). The most likely exact score is 0-2 at 12.4%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 52.5%; Under 3.5 goals: 69.5%; Double Chance 1X: 34.8%; Double Chance X2: 85.1%; Under 4.5 goals: 84.9%; BTTS Yes (both teams score): 44.3%; BTTS No (at least one team does not score): 55.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 14.9% | 6.71 |
| Draw | 19.9% | 5.02 |
| Napoli win | 65.2% | 1.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Napoli expected goals | 2.18 |
| Expected total goals | 2.85 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 76.3% |
| Under 1.5 | 23.7% |
| Over 2.5 | 52.5% |
| Under 2.5 | 47.5% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.1% |
| Under 4.5 | 84.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.43% |
| 2 | 0-1 | 11.47% |
| 3 | 1-1 | 9.42% |
| 4 | 0-3 | 9.01% |
| 5 | 1-2 | 8.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 14.9% | 19.7% | 5.20 | -22.5% |
| Draw | 19.9% | 22.0% | 4.28 | -14.7% |
| Napoli win | 65.2% | 58.3% | 1.76 | +14.7% |
| Over 2.5 | 52.5% | 56.9% | 1.75 | -8.1% |
| Under 2.5 | 47.5% | 43.1% | 2.26 | +7.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:00:00+00:00 |
| Fixture id | 907639dade64cca45d1ab639195d201e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:51Z |
| Market best draw last update utc | 2026-10-12T21:08:52Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Matchbook |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Venezia |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 44.3% |
| P btts no | 55.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.52 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.22 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.27 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.61 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 10.1% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 72.1% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 43.2% |
| P home draw | 34.8% |
| P draw away | 85.1% |
| Raw p home draw | 27.9% |
| Raw p draw away | 89.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.76 |
| Reference draw odds | 4.28 |
| Reference away odds | 1.68 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.09 |
| Home probability edge | -4.8% |
| Draw probability edge | -2.1% |
| Away probability edge | +6.9% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | -0.0959 |
| Raw ev home | -0.4740 |
| Raw edge prob draw | -0.0419 |
| Raw ev draw | -0.2370 |
| Raw edge prob away | 0.1378 |
| Raw ev away | 0.2682 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **45.5%**. Expected goals are 1.28 for AC Milan and 1.16 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 44.4%; Under 3.5 goals: 76.9%; Double Chance 1X: 71.9%; Double Chance X2: 54.5%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 45.5% | 2.20 |
| Draw | 26.4% | 3.79 |
| Atalanta BC win | 28.1% | 3.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.28 |
| Atalanta BC expected goals | 1.16 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.4% |
| Under 2.5 | 55.6% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.98% |
| 2 | 1-1 | 12.50% |
| 3 | 2-1 | 9.57% |
| 4 | 0-1 | 8.55% |
| 5 | 0-0 | 8.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 45.5% | 51.5% | 1.93 | -12.2% |
| Draw | 26.4% | 25.6% | 3.90 | +3.0% |
| Atalanta BC win | 28.1% | 22.9% | 4.30 | +20.8% |
| Over 2.5 | 44.4% | 53.7% | 1.83 | -18.8% |
| Under 2.5 | 55.6% | 46.3% | 2.15 | +19.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T16:00:00+00:00 |
| Fixture id | f9403dd597edbfaa73abdc974e55344c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:37Z |
| Market best away last update utc | 2026-10-12T21:08:37Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | BetAnything |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.90 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.80 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 33.3% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.5% |
| P home draw | 71.9% |
| P draw away | 54.5% |
| Raw p home draw | 66.7% |
| Raw p draw away | 60.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.90 |
| Reference draw odds | 3.73 |
| Reference away odds | 4.17 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 1.96 |
| Home probability edge | -6.0% |
| Draw probability edge | +0.8% |
| Away probability edge | +5.2% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.1202 |
| Raw ev home | -0.2379 |
| Raw edge prob draw | 0.0154 |
| Raw ev draw | 0.0602 |
| Raw edge prob away | 0.1048 |
| Raw ev away | 0.4332 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.5%**. Expected goals are 1.00 for Fiorentina and 1.73 for Como (2.73 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 50.8%; Under 3.5 goals: 71.1%; Double Chance 1X: 49.5%; Double Chance X2: 75.1%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 52.3%; BTTS No (at least one team does not score): 47.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.9% | 4.01 |
| Draw | 24.6% | 4.07 |
| Como win | 50.5% | 1.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.00 |
| Como expected goals | 1.73 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 50.8% |
| Under 2.5 | 49.2% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.68% |
| 2 | 0-1 | 10.48% |
| 3 | 0-2 | 9.03% |
| 4 | 1-2 | 9.02% |
| 5 | 1-0 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.9% | 28.1% | 3.65 | -9.0% |
| Draw | 24.6% | 25.6% | 3.85 | -5.4% |
| Como win | 50.5% | 46.3% | 2.12 | +7.0% |
| Over 2.5 | 50.8% | 57.9% | 1.73 | -12.1% |
| Under 2.5 | 49.2% | 42.1% | 2.29 | +12.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 3ea32a0aa44a5f0ef7fd088155430087 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:37Z |
| Market best draw last update utc | 2026-10-12T21:08:52Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 52.3% |
| P btts no | 47.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.86 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.04 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.19 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 21.8% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 54.7% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 51.9% |
| P home draw | 49.5% |
| P draw away | 75.1% |
| Raw p home draw | 45.3% |
| Raw p draw away | 78.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.42 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.11 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.13 |
| Home probability edge | -3.2% |
| Draw probability edge | -1.0% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | -0.0638 |
| Raw ev home | -0.2061 |
| Raw edge prob draw | -0.0199 |
| Raw ev draw | -0.0919 |
| Raw edge prob away | 0.0837 |
| Raw ev away | 0.1588 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **54.1%**. Expected goals are 1.37 for Juventus and 0.85 for Lazio (2.22 combined). The most likely exact score is 1-0 at 16.5%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.3%; Double Chance 1X: 79.8%; Double Chance X2: 45.9%; Under 4.5 goals: 92.3%; BTTS Yes (both teams score): 42.1%; BTTS No (at least one team does not score): 57.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 54.1% | 1.85 |
| Draw | 25.7% | 3.89 |
| Lazio win | 20.2% | 4.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.85 |
| Expected total goals | 2.22 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.7% |
| Under 3.5 | 81.3% |
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.49% |
| 2 | 1-1 | 11.73% |
| 3 | 2-0 | 11.23% |
| 4 | 0-0 | 10.08% |
| 5 | 2-1 | 9.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 54.1% | 59.1% | 1.72 | -7.0% |
| Draw | 25.7% | 23.8% | 4.04 | +3.9% |
| Lazio win | 20.2% | 17.1% | 5.80 | +17.3% |
| Over 2.5 | 39.0% | 48.9% | 2.03 | -20.8% |
| Under 2.5 | 61.0% | 51.1% | 1.92 | +17.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T18:45:00+00:00 |
| Fixture id | 4c4026e2782f09d6f0ff2bde2a390513 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:52Z |
| Odds bookmakers 1x2 | 24.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Matchbook |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Juventus |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.1% |
| P btts no | 57.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.92 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.34 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.02 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 23.4% |
| Raw p over 1 5 | 64.9% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 42.6% |
| P home draw | 79.8% |
| P draw away | 45.9% |
| Raw p home draw | 76.6% |
| Raw p draw away | 50.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.66 |
| Reference draw odds | 3.98 |
| Reference away odds | 5.49 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.98 |
| Reference Under 2.5 odds | 1.90 |
| Home probability edge | -5.0% |
| Draw probability edge | +1.9% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | -0.1003 |
| Raw ev home | -0.1562 |
| Raw edge prob draw | 0.0375 |
| Raw ev draw | 0.1144 |
| Raw edge prob away | 0.0629 |
| Raw ev away | 0.3549 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.5%**. Expected goals are 1.44 for Udinese and 0.82 for Lecce (2.26 combined). The most likely exact score is 1-0 at 15.0%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 39.4%; Under 3.5 goals: 80.7%; Double Chance 1X: 78.2%; Double Chance X2: 48.5%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.7%; BTTS No (at least one team does not score): 57.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.5% | 1.94 |
| Draw | 26.6% | 3.75 |
| Lecce win | 21.8% | 4.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.44 |
| Lecce expected goals | 0.82 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.7% |
| Under 0.5 | 10.3% |
| Over 1.5 | 65.9% |
| Under 1.5 | 34.1% |
| Over 2.5 | 39.4% |
| Under 2.5 | 60.6% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.03% |
| 2 | 1-1 | 12.20% |
| 3 | 2-0 | 10.75% |
| 4 | 0-0 | 10.30% |
| 5 | 2-1 | 8.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.5% | 51.5% | 1.95 | +0.5% |
| Draw | 26.6% | 26.5% | 3.70 | -1.4% |
| Lecce win | 21.8% | 22.0% | 4.40 | -4.0% |
| Over 2.5 | 39.4% | 46.7% | 2.08 | -18.1% |
| Under 2.5 | 60.6% | 53.3% | 1.87 | +13.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T10:30:00+00:00 |
| Fixture id | 367da93aa21a1e13eeafb94fd2263c75 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:52Z |
| Market best away last update utc | 2026-10-12T21:08:37Z |
| Odds bookmakers 1x2 | 23.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Tipico |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.7% |
| P btts no | 57.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.71 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.54 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.19 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.61 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 21.6% |
| Raw p over 1 5 | 65.9% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 42.7% |
| P home draw | 78.2% |
| P draw away | 48.5% |
| Raw p home draw | 78.4% |
| Raw p draw away | 48.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.90 |
| Reference draw odds | 3.61 |
| Reference away odds | 4.31 |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.83 |
| Home probability edge | +0.1% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | 0.0013 |
| Raw ev home | 0.0061 |
| Raw edge prob draw | 0.0032 |
| Raw ev draw | -0.0081 |
| Raw edge prob away | -0.0045 |
| Raw ev away | -0.0498 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **38.8%**. Expected goals are 1.13 for Monza and 1.57 for Cagliari (2.70 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 49.5%; Under 3.5 goals: 72.0%; Double Chance 1X: 61.2%; Double Chance X2: 66.1%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 54.3%; BTTS No (at least one team does not score): 45.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 33.9% | 2.95 |
| Draw | 27.3% | 3.66 |
| Cagliari win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.13 |
| Cagliari expected goals | 1.57 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.98% |
| 2 | 1-0 | 9.48% |
| 3 | 0-1 | 8.67% |
| 4 | 2-1 | 8.31% |
| 5 | 1-2 | 7.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.9% | 40.4% | 2.48 | -16.0% |
| Draw | 27.3% | 29.7% | 3.27 | -10.7% |
| Cagliari win | 38.8% | 30.0% | 3.55 | +37.8% |
| Over 2.5 | 49.5% | 45.1% | 2.14 | +6.0% |
| Under 2.5 | 50.5% | 54.9% | 1.83 | -7.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T16:30:00+00:00 |
| Fixture id | ce94aca384a20f6af459366da6e1dd21 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:36Z |
| Market best away last update utc | 2026-10-12T21:08:37Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | LeoVegas (SE) |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.3% |
| P btts no | 45.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.69 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.93 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.57 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 27.4% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 47.7% |
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 53.5% |
| P home draw | 61.2% |
| P draw away | 66.1% |
| Raw p home draw | 52.3% |
| Raw p draw away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.40 |
| Reference draw odds | 3.23 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 2.01 |
| Reference Under 2.5 odds | 1.69 |
| Home probability edge | -6.5% |
| Draw probability edge | -2.4% |
| Away probability edge | +8.8% |
| Over 2.5 probability edge | +4.4% |
| Under 2.5 probability edge | -4.4% |
| Raw edge prob home | -0.1299 |
| Raw ev home | -0.3211 |
| Raw edge prob draw | -0.0470 |
| Raw ev draw | -0.1834 |
| Raw edge prob away | 0.1769 |
| Raw ev away | 0.6917 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **37.5%**. Expected goals are 1.02 for Parma and 1.08 for Torino (2.10 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 87.5%; Over 2.5 goals: 34.8%; Under 3.5 goals: 83.9%; Double Chance 1X: 62.5%; Double Chance X2: 68.2%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 42.4%; BTTS No (at least one team does not score): 57.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.8% | 3.14 |
| Draw | 30.7% | 3.26 |
| Torino win | 37.5% | 2.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.02 |
| Torino expected goals | 1.08 |
| Expected total goals | 2.10 |
| Over 0.5 | 87.5% |
| Under 0.5 | 12.5% |
| Over 1.5 | 61.9% |
| Under 1.5 | 38.1% |
| Over 2.5 | 34.8% |
| Under 2.5 | 65.2% |
| Over 3.5 | 16.1% |
| Under 3.5 | 83.9% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.83% |
| 2 | 0-1 | 13.63% |
| 3 | 0-0 | 12.54% |
| 4 | 1-0 | 11.88% |
| 5 | 1-2 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.8% | 29.9% | 3.25 | +3.4% |
| Draw | 30.7% | 31.6% | 3.25 | -0.2% |
| Torino win | 37.5% | 38.5% | 2.54 | -4.7% |
| Over 2.5 | 34.8% | 39.4% | 2.48 | -13.7% |
| Under 2.5 | 65.2% | 60.6% | 1.64 | +7.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T18:45:00+00:00 |
| Fixture id | 07014d9adc65ca39710bd9f0c7c0d3f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-12T21:08:36Z |
| Market best draw last update utc | 2026-10-12T21:08:37Z |
| Market best away last update utc | 2026-10-12T21:08:36Z |
| Odds bookmakers 1x2 | 20.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Parma |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 42.4% |
| P btts no | 57.6% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 7.97 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.63 |
| Fair Over 2.5 odds | 2.88 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.20 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.24 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 33.7% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 36.5% |
| Raw p over 1 5 | 62.0% |
| Raw p under 3 5 | 83.9% |
| Raw p btts yes | 42.2% |
| P home draw | 62.5% |
| P draw away | 68.2% |
| Raw p home draw | 63.5% |
| Raw p draw away | 66.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.21 |
| Reference draw odds | 3.04 |
| Reference away odds | 2.51 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 2.26 |
| Reference Under 2.5 odds | 1.55 |
| Home probability edge | +1.9% |
| Draw probability edge | -0.9% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | 0.0387 |
| Raw ev home | 0.0964 |
| Raw edge prob draw | -0.0180 |
| Raw ev draw | -0.0317 |
| Raw edge prob away | -0.0207 |
| Raw ev away | -0.0736 |

</details>


---
