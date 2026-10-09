# UEFA Champions League — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 521 |
| Training data through | 2026-09-10 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1560.624 |
| Base scoring parameter | 0.154 |
| Home-advantage parameter | 0.271 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0 |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 24.00 |
| Additional event odds calls budget | 24.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-13 — Arsenal vs Lille

The model's most likely 1X2 outcome is **Arsenal win** at **73.2%**. Expected goals are 2.01 for Arsenal and 0.77 for Lille (2.78 combined). The most likely exact score is 1-0 at 14.1%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 54.4%; Under 4.5 goals: 84.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 73.2% | 1.37 |
| Draw | 15.9% | 6.28 |
| Lille win | 10.9% | 9.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 2.01 |
| Lille expected goals | 0.77 |
| Expected total goals | 2.78 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 77.0% |
| Under 1.5 | 23.0% |
| Over 2.5 | 54.4% |
| Under 2.5 | 45.6% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.14% |
| 2 | 2-0 | 13.70% |
| 3 | 2-1 | 10.57% |
| 4 | 3-0 | 9.19% |
| 5 | 1-1 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 73.2% | 79.5% | 1.30 | -4.8% |
| Draw | 15.9% | 12.6% | 6.80 | +8.4% |
| Lille win | 10.9% | 7.8% | 15.00 | +62.8% |
| Over 2.5 | 54.4% | 60.5% | 1.67 | -9.2% |
| Under 2.5 | 45.6% | 39.5% | 2.44 | +11.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 93177465a42a0fb7802f1c8b06d6ee3a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:11Z |
| Market best draw last update utc | 2026-10-09T08:10:57Z |
| Market best away last update utc | 2026-10-09T08:10:27Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Arsenal FC |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 44.9% |
| P btts no | 55.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.19 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.35 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.36 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 19.2% |
| Unadjusted away-win probability | 13.9% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 46.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.23 |
| Reference draw odds | 6.50 |
| Reference away odds | 10.00 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.44 |
| Home probability edge | -6.3% |
| Draw probability edge | +3.3% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | -0.1266 |
| Raw ev home | -0.1305 |
| Raw edge prob draw | 0.0663 |
| Raw ev draw | 0.3089 |
| Raw edge prob away | 0.0603 |
| Raw ev away | 1.0803 |

</details>


---

## 2026-10-13 — Atlético Madrid vs Manchester United

The model's most likely 1X2 outcome is **Atlético Madrid win** at **61.3%**. Expected goals are 3.87 for Atlético Madrid and 1.70 for Manchester United (5.57 combined). The most likely exact score is 2-2 at 6.2%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 90.1%; Under 4.5 goals: 37.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 61.3% | 1.63 |
| Draw | 17.3% | 5.79 |
| Manchester United win | 21.4% | 4.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 3.87 |
| Manchester United expected goals | 1.70 |
| Expected total goals | 5.57 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.0% |
| Under 1.5 | 3.0% |
| Over 2.5 | 90.1% |
| Under 2.5 | 9.9% |
| Over 3.5 | 79.0% |
| Under 3.5 | 21.0% |
| Over 4.5 | 62.5% |
| Under 4.5 | 37.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.24% |
| 2 | 3-1 | 5.05% |
| 3 | 4-1 | 4.88% |
| 4 | 3-3 | 4.57% |
| 5 | 3-2 | 4.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 61.3% | 46.5% | 2.24 | +37.4% |
| Draw | 17.3% | 23.1% | 4.20 | -27.5% |
| Manchester United win | 21.4% | 30.4% | 3.40 | -27.2% |
| Over 2.5 | 90.1% | 64.9% | 1.50 | +35.2% |
| Under 2.5 | 9.9% | 35.1% | 2.63 | -74.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | a9c22e08b395ee5753c8a65bc0eb97cf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:11Z |
| Market best draw last update utc | 2026-10-09T08:10:11Z |
| Market best away last update utc | 2026-10-09T08:10:57Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 82.0% |
| P btts no | 18.0% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 259.29 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 33.17 |
| Fair Over 2.5 odds | 1.11 |
| Fair Under 2.5 odds | 10.13 |
| Fair Over 3.5 odds | 1.27 |
| Fair Under 3.5 odds | 4.77 |
| Fair Over 4.5 odds | 1.60 |
| Fair Under 4.5 odds | 2.67 |
| Unadjusted home-win probability | 76.2% |
| Unadjusted draw probability | 11.5% |
| Unadjusted away-win probability | 12.4% |
| Raw p over 1 5 | 97.4% |
| Raw p under 3 5 | 19.4% |
| Raw p btts yes | 80.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | +14.8% |
| Draw probability edge | -5.8% |
| Away probability edge | -9.0% |
| Over 2.5 probability edge | +25.3% |
| Under 2.5 probability edge | -25.3% |
| Raw edge prob home | 0.2966 |
| Raw ev home | 0.7058 |
| Raw edge prob draw | -0.1163 |
| Raw ev draw | -0.5188 |
| Raw edge prob away | -0.1803 |
| Raw ev away | -0.5787 |

</details>


---

## 2026-10-13 — Galatasaray vs Barcelona

The model's most likely 1X2 outcome is **Barcelona win** at **67.0%**. Expected goals are 1.61 for Galatasaray and 2.47 for Barcelona (4.09 combined). The most likely exact score is 1-2 at 9.7%. Goal-market probabilities: at least one goal: 98.9%; Over 2.5 goals: 78.6%; Under 4.5 goals: 60.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 18.0% | 5.57 |
| Draw | 15.1% | 6.63 |
| Barcelona win | 67.0% | 1.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.61 |
| Barcelona expected goals | 2.47 |
| Expected total goals | 4.09 |
| Over 0.5 | 98.9% |
| Under 0.5 | 1.1% |
| Over 1.5 | 91.4% |
| Under 1.5 | 8.6% |
| Over 2.5 | 78.6% |
| Under 2.5 | 21.4% |
| Over 3.5 | 59.1% |
| Under 3.5 | 40.9% |
| Over 4.5 | 40.0% |
| Under 4.5 | 60.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.74% |
| 2 | 1-3 | 8.04% |
| 3 | 2-3 | 6.49% |
| 4 | 0-2 | 6.03% |
| 5 | 2-2 | 5.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 18.0% | 11.1% | 9.50 | +70.6% |
| Draw | 15.1% | 11.9% | 7.40 | +11.6% |
| Barcelona win | 67.0% | 77.0% | 1.34 | -10.3% |
| Over 2.5 | 78.6% | 80.9% | 1.21 | -5.0% |
| Under 2.5 | 21.4% | 19.1% | 4.50 | -3.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | dd431688ed5c8f383b6434fd4f01e883 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:09:56Z |
| Market best draw last update utc | 2026-10-09T08:10:57Z |
| Market best away last update utc | 2026-10-09T08:10:12Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (NL) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 71.9% |
| P btts no | 28.1% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 90.18 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.66 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.66 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.44 |
| Fair Over 4.5 odds | 2.50 |
| Fair Under 4.5 odds | 1.67 |
| Unadjusted home-win probability | 24.9% |
| Unadjusted draw probability | 18.2% |
| Unadjusted away-win probability | 56.9% |
| Raw p over 1 5 | 91.1% |
| Raw p under 3 5 | 41.6% |
| Raw p btts yes | 73.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 7.50 |
| Reference draw odds | 7.00 |
| Reference away odds | 1.27 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.21 |
| Reference Under 2.5 odds | 4.45 |
| Home probability edge | +6.9% |
| Draw probability edge | +3.2% |
| Away probability edge | -10.0% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | 0.1379 |
| Raw ev home | 1.3611 |
| Raw edge prob draw | 0.0630 |
| Raw ev draw | 0.3490 |
| Raw edge prob away | -0.2010 |
| Raw ev away | -0.2373 |

</details>


---

## 2026-10-13 — Inter Milan vs Club Brugge

The model's most likely 1X2 outcome is **Inter Milan win** at **69.0%**. Expected goals are 1.98 for Inter Milan and 1.01 for Club Brugge (2.99 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 59.1%; Under 4.5 goals: 80.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 69.0% | 1.45 |
| Draw | 16.8% | 5.96 |
| Club Brugge win | 14.2% | 7.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.98 |
| Club Brugge expected goals | 1.01 |
| Expected total goals | 2.99 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 59.1% |
| Under 2.5 | 40.9% |
| Over 3.5 | 35.9% |
| Under 3.5 | 64.1% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.97% |
| 2 | 2-1 | 11.35% |
| 3 | 2-0 | 11.29% |
| 4 | 1-1 | 7.87% |
| 5 | 3-1 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 69.0% | 77.4% | 1.31 | -9.6% |
| Draw | 16.8% | 13.2% | 6.25 | +4.8% |
| Club Brugge win | 14.2% | 9.4% | 11.50 | +63.8% |
| Over 2.5 | 59.1% | 65.3% | 1.50 | -11.4% |
| Under 2.5 | 40.9% | 34.7% | 2.66 | +8.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | ca3f4b075d835413f9cb7bd3c439fdd0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:12Z |
| Market best draw last update utc | 2026-10-09T08:11:01Z |
| Market best away last update utc | 2026-10-09T08:10:57Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | Club Brugge KV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 52.8% |
| P btts no | 47.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.69 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.03 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 60.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 65.0% |
| Raw p btts yes | 54.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.26 |
| Reference draw odds | 6.25 |
| Reference away odds | 8.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.65 |
| Home probability edge | -8.5% |
| Draw probability edge | +3.6% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.1691 |
| Raw ev home | -0.2070 |
| Raw edge prob draw | 0.0718 |
| Raw ev draw | 0.2725 |
| Raw edge prob away | 0.0973 |
| Raw ev away | 1.1970 |

</details>


---

## 2026-10-13 — RB Leipzig vs PSV Eindhoven

The model's most likely 1X2 outcome is **RB Leipzig win** at **41.6%**. Expected goals are 1.58 for RB Leipzig and 1.78 for PSV Eindhoven (3.36 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 65.1%; Under 4.5 goals: 75.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 41.6% | 2.40 |
| Draw | 21.7% | 4.61 |
| PSV Eindhoven win | 36.7% | 2.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 1.58 |
| PSV Eindhoven expected goals | 1.78 |
| Expected total goals | 3.36 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 84.2% |
| Under 1.5 | 15.8% |
| Over 2.5 | 65.1% |
| Under 2.5 | 34.9% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.28% |
| 2 | 2-1 | 9.19% |
| 3 | 1-2 | 7.36% |
| 4 | 1-0 | 7.12% |
| 5 | 2-2 | 6.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 41.6% | 48.3% | 2.08 | -13.5% |
| Draw | 21.7% | 21.7% | 4.30 | -6.7% |
| PSV Eindhoven win | 36.7% | 30.0% | 3.50 | +28.4% |
| Over 2.5 | 65.1% | 69.8% | 1.39 | -9.5% |
| Under 2.5 | 34.9% | 30.2% | 3.03 | +5.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | da9e9e9eb9a238ed97827c4a8fbe6044 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:12Z |
| Market best draw last update utc | 2026-10-09T08:10:11Z |
| Market best away last update utc | 2026-10-09T08:10:27Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | RB Leipzig |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.6% |
| P btts no | 34.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.48 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.35 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.87 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.04 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 34.9% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 43.4% |
| Raw p over 1 5 | 84.4% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 65.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.98 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -6.7% |
| Draw probability edge | +0.0% |
| Away probability edge | +6.7% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | -0.1344 |
| Raw ev home | -0.2744 |
| Raw edge prob draw | 0.0000 |
| Raw ev draw | -0.0669 |
| Raw edge prob away | 0.1343 |
| Raw ev away | 0.5195 |

</details>


---

## 2026-10-13 — RC Lens vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **42.6%**. Expected goals are 1.25 for RC Lens and 1.66 for Sporting Lisbon (2.91 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 55.4%; Under 4.5 goals: 83.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 34.0% | 2.94 |
| Draw | 23.4% | 4.27 |
| Sporting Lisbon win | 42.6% | 2.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.25 |
| Sporting Lisbon expected goals | 1.66 |
| Expected total goals | 2.91 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 77.9% |
| Under 1.5 | 22.1% |
| Over 2.5 | 55.4% |
| Under 2.5 | 44.6% |
| Over 3.5 | 33.0% |
| Under 3.5 | 67.0% |
| Over 4.5 | 16.8% |
| Under 4.5 | 83.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.92% |
| 2 | 0-1 | 8.60% |
| 3 | 1-0 | 8.51% |
| 4 | 1-2 | 8.41% |
| 5 | 2-1 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 34.0% | 38.5% | 2.63 | -10.6% |
| Draw | 23.4% | 23.8% | 3.90 | -8.7% |
| Sporting Lisbon win | 42.6% | 37.7% | 2.70 | +15.0% |
| Over 2.5 | 55.4% | 60.7% | 1.64 | -9.2% |
| Under 2.5 | 44.6% | 39.3% | 2.46 | +9.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T16:45:00+00:00 |
| Fixture id | 2b0a946cac613732fcbf57ce931490a1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:27Z |
| Market best draw last update utc | 2026-10-09T08:10:57Z |
| Market best away last update utc | 2026-10-09T08:10:11Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Racing Club de Lens |
| Matched away-team name | Sporting Clube de Portugal |
| Home-name matching confidence | 86/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.18 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.53 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.03 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.94 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 47.5% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 66.7% |
| Raw p btts yes | 57.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.45 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.50 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.33 |
| Home probability edge | -4.5% |
| Draw probability edge | -0.4% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | -0.0902 |
| Raw ev home | -0.2244 |
| Raw edge prob draw | -0.0077 |
| Raw ev draw | -0.1018 |
| Raw edge prob away | 0.0979 |
| Raw ev away | 0.2819 |

</details>


---

## 2026-10-13 — Sabah FK vs Slavia Praha

The model's most likely 1X2 outcome is **Slavia Praha win** at **54.6%**. Expected goals are 0.37 for Sabah FK and 1.26 for Slavia Praha (1.63 combined). The most likely exact score is 0-1 at 23.0%. Goal-market probabilities: at least one goal: 82.6%; Over 2.5 goals: 22.3%; Under 4.5 goals: 97.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 19.0% | 5.25 |
| Draw | 26.3% | 3.80 |
| Slavia Praha win | 54.6% | 1.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.37 |
| Slavia Praha expected goals | 1.26 |
| Expected total goals | 1.63 |
| Over 0.5 | 82.6% |
| Under 0.5 | 17.4% |
| Over 1.5 | 46.7% |
| Under 1.5 | 53.3% |
| Over 2.5 | 22.3% |
| Under 2.5 | 77.7% |
| Over 3.5 | 7.9% |
| Under 3.5 | 92.1% |
| Over 4.5 | 2.5% |
| Under 4.5 | 97.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 23.01% |
| 2 | 0-0 | 17.36% |
| 3 | 0-2 | 14.18% |
| 4 | 1-0 | 12.93% |
| 5 | 1-1 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 19.0% | 26.6% | 3.74 | -28.8% |
| Draw | 26.3% | 23.6% | 4.00 | +5.3% |
| Slavia Praha win | 54.6% | 49.8% | 2.04 | +11.4% |
| Over 2.5 | 22.3% | 58.3% | 1.71 | -61.9% |
| Under 2.5 | 77.7% | 41.7% | 2.32 | +80.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T16:45:00+00:00 |
| Fixture id | 46f726554e6876fb828c767bfbfdfdad |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:11Z |
| Market best draw last update utc | 2026-10-09T08:10:11Z |
| Market best away last update utc | 2026-10-09T08:10:57Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 21.5% |
| P btts no | 78.5% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.76 |
| Fair Over 1.5 odds | 2.14 |
| Fair Under 1.5 odds | 1.88 |
| Fair Over 2.5 odds | 4.49 |
| Fair Under 2.5 odds | 1.29 |
| Fair Over 3.5 odds | 12.64 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 40.66 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 11.5% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 59.5% |
| Raw p over 1 5 | 48.0% |
| Raw p under 3 5 | 91.7% |
| Raw p btts yes | 21.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.45 |
| Reference draw odds | 3.85 |
| Reference away odds | 1.92 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -7.6% |
| Draw probability edge | +2.7% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -36.0% |
| Under 2.5 probability edge | +36.0% |
| Raw edge prob home | -0.1511 |
| Raw ev home | -0.5708 |
| Raw edge prob draw | 0.0538 |
| Raw ev draw | 0.1611 |
| Raw edge prob away | 0.0973 |
| Raw ev away | 0.2137 |

</details>


---

## 2026-10-13 — Viking FK vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **92.6%**. Expected goals are 0.69 for Viking FK and 4.47 for Bayern Munich (5.16 combined). The most likely exact score is 0-4 at 9.5%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 88.3%; Under 4.5 goals: 42.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viking FK win | 3.0% | 33.69 |
| Draw | 4.4% | 22.53 |
| Bayern Munich win | 92.6% | 1.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viking FK expected goals | 0.69 |
| Bayern Munich expected goals | 4.47 |
| Expected total goals | 5.16 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 96.1% |
| Under 1.5 | 3.9% |
| Over 2.5 | 88.3% |
| Under 2.5 | 11.7% |
| Over 3.5 | 74.9% |
| Under 3.5 | 25.1% |
| Over 4.5 | 57.9% |
| Under 4.5 | 42.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-4 | 9.48% |
| 2 | 0-3 | 8.49% |
| 3 | 0-5 | 8.47% |
| 4 | 1-4 | 6.54% |
| 5 | 0-6 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viking FK win | 3.0% | 4.0% | 27.00 | -19.8% |
| Draw | 4.4% | 4.7% | 15.50 | -31.2% |
| Bayern Munich win | 92.6% | 91.3% | 1.11 | +2.8% |
| Over 2.5 | 88.3% | 85.6% | 1.15 | +1.6% |
| Under 2.5 | 11.7% | 14.4% | 5.70 | -33.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 8a9d20b23417357011c10585a99335e9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:11Z |
| Market best draw last update utc | 2026-10-09T08:10:12Z |
| Market best away last update utc | 2026-10-09T08:10:27Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Viking FK |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 189.93 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 25.53 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.58 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 3.99 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.38 |
| Unadjusted home-win probability | 1.9% |
| Unadjusted draw probability | 4.1% |
| Unadjusted away-win probability | 93.9% |
| Raw p over 1 5 | 96.3% |
| Raw p under 3 5 | 24.5% |
| Raw p btts yes | 49.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 15.00 |
| Reference draw odds | 13.00 |
| Reference away odds | 1.08 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.70 |
| Home probability edge | -1.0% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | +2.8% |
| Under 2.5 probability edge | -2.8% |
| Raw edge prob home | -0.0206 |
| Raw ev home | -0.4769 |
| Raw edge prob draw | -0.0061 |
| Raw ev draw | -0.3593 |
| Raw edge prob away | 0.0267 |
| Raw ev away | 0.0426 |

</details>


---

## 2026-10-13 — Villarreal vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **41.0%**. Expected goals are 0.87 for Villarreal and 1.43 for Napoli (2.31 combined). The most likely exact score is 1-0 at 13.4%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 40.1%; Under 4.5 goals: 91.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 33.8% | 2.96 |
| Draw | 25.1% | 3.98 |
| Napoli win | 41.0% | 2.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 0.87 |
| Napoli expected goals | 1.43 |
| Expected total goals | 2.31 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 40.1% |
| Under 2.5 | 59.9% |
| Over 3.5 | 19.5% |
| Under 3.5 | 80.5% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.37% |
| 2 | 0-1 | 12.05% |
| 3 | 1-1 | 11.60% |
| 4 | 0-0 | 9.14% |
| 5 | 0-2 | 8.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 33.8% | 44.0% | 2.33 | -21.2% |
| Draw | 25.1% | 24.6% | 3.85 | -3.2% |
| Napoli win | 41.0% | 31.4% | 3.25 | +33.4% |
| Over 2.5 | 40.1% | 56.0% | 1.77 | -29.0% |
| Under 2.5 | 59.9% | 44.0% | 2.22 | +32.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-13T19:00:00+00:00 |
| Fixture id | 09e41b63d1d59bd4d971c54ffce154d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:11Z |
| Market best draw last update utc | 2026-10-09T08:10:11Z |
| Market best away last update utc | 2026-10-09T08:10:27Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal CF |
| Matched away-team name | SSC Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 43.8% |
| P btts no | 56.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.94 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.12 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.16 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 23.6% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 50.7% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 79.8% |
| Raw p btts yes | 43.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.95 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | -10.2% |
| Draw probability edge | +0.5% |
| Away probability edge | +9.7% |
| Over 2.5 probability edge | -15.9% |
| Under 2.5 probability edge | +15.9% |
| Raw edge prob home | -0.2043 |
| Raw ev home | -0.4502 |
| Raw edge prob draw | 0.0107 |
| Raw ev draw | -0.0113 |
| Raw edge prob away | 0.1935 |
| Raw ev away | 0.6485 |

</details>


---

## 2026-10-14 — AS Roma vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **51.5%**. Expected goals are 1.26 for AS Roma and 1.83 for Real Madrid (3.09 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 59.7%; Under 4.5 goals: 79.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 26.4% | 3.78 |
| Draw | 22.1% | 4.53 |
| Real Madrid win | 51.5% | 1.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.26 |
| Real Madrid expected goals | 1.83 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 59.7% |
| Under 2.5 | 40.3% |
| Over 3.5 | 37.4% |
| Under 3.5 | 62.6% |
| Over 4.5 | 20.1% |
| Under 4.5 | 79.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.06% |
| 2 | 1-2 | 9.63% |
| 3 | 0-1 | 8.86% |
| 4 | 0-2 | 7.64% |
| 5 | 2-1 | 6.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 26.4% | 26.0% | 4.10 | +8.3% |
| Draw | 22.1% | 22.3% | 4.30 | -5.1% |
| Real Madrid win | 51.5% | 51.7% | 1.94 | -0.1% |
| Over 2.5 | 59.7% | 69.1% | 1.44 | -14.0% |
| Under 2.5 | 40.3% | 30.9% | 2.95 | +18.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | d4ef112438afa4c2cdbbfc9376a009c9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:11Z |
| Market best draw last update utc | 2026-10-09T08:10:57Z |
| Market best away last update utc | 2026-10-09T08:10:12Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.7% |
| P btts no | 40.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.68 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.25 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.48 |
| Fair Over 3.5 odds | 2.67 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.99 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 51.3% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 62.6% |
| Raw p btts yes | 59.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.55 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.86 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.92 |
| Home probability edge | +0.4% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | 0.0085 |
| Raw ev home | 0.1008 |
| Raw edge prob draw | -0.0049 |
| Raw ev draw | -0.0620 |
| Raw edge prob away | -0.0036 |
| Raw ev away | -0.0040 |

</details>


---

## 2026-10-14 — Aston Villa vs Fenerbahce

The model's most likely 1X2 outcome is **Aston Villa win** at **66.5%**. Expected goals are 2.22 for Aston Villa and 0.60 for Fenerbahce (2.83 combined). The most likely exact score is 2-0 at 13.0%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.4%; Under 4.5 goals: 85.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 66.5% | 1.50 |
| Draw | 19.1% | 5.24 |
| Fenerbahce win | 14.4% | 6.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 2.22 |
| Fenerbahce expected goals | 0.60 |
| Expected total goals | 2.83 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 75.0% |
| Under 1.5 | 25.0% |
| Over 2.5 | 51.4% |
| Under 2.5 | 48.6% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.6% |
| Under 4.5 | 85.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.00% |
| 2 | 1-0 | 12.05% |
| 3 | 3-0 | 9.63% |
| 4 | 1-1 | 8.91% |
| 5 | 2-1 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 66.5% | 58.1% | 1.77 | +17.6% |
| Draw | 19.1% | 22.0% | 4.25 | -18.9% |
| Fenerbahce win | 14.4% | 19.9% | 5.40 | -22.0% |
| Over 2.5 | 51.4% | 59.2% | 1.74 | -10.6% |
| Under 2.5 | 48.6% | 40.8% | 2.28 | +10.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 3f3cb74e560dfcc3e795b667ed9ebdef |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:11Z |
| Market best draw last update utc | 2026-10-09T08:09:57Z |
| Market best away last update utc | 2026-10-09T08:10:57Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Unibet (NL) |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 41.3% |
| P btts no | 58.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.32 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.00 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.86 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 16.2% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 76.9% |
| Raw p under 3 5 | 68.6% |
| Raw p btts yes | 40.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.66 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.50 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | +8.4% |
| Draw probability edge | -2.9% |
| Away probability edge | -5.5% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | 0.1681 |
| Raw ev home | 0.3252 |
| Raw edge prob draw | -0.0585 |
| Raw ev draw | -0.3129 |
| Raw edge prob away | -0.1096 |
| Raw ev away | -0.5162 |

</details>


---

## 2026-10-14 — Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **47.4%**. Expected goals are 1.67 for Bodø/Glimt and 2.04 for Borussia Dortmund (3.70 combined). The most likely exact score is 1-2 at 8.6%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 71.3%; Under 4.5 goals: 68.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 31.2% | 3.20 |
| Draw | 21.3% | 4.69 |
| Borussia Dortmund win | 47.4% | 2.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 1.67 |
| Borussia Dortmund expected goals | 2.04 |
| Expected total goals | 3.70 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 88.0% |
| Under 1.5 | 12.0% |
| Over 2.5 | 71.3% |
| Under 2.5 | 28.7% |
| Over 3.5 | 50.7% |
| Under 3.5 | 49.3% |
| Over 4.5 | 31.2% |
| Under 4.5 | 68.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.58% |
| 2 | 1-1 | 8.30% |
| 3 | 2-2 | 7.42% |
| 4 | 2-1 | 6.71% |
| 5 | 1-3 | 5.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bodø/Glimt win | 31.2% | 30.0% | 3.30 | +3.1% |
| Draw | 21.3% | 22.2% | 4.30 | -8.3% |
| Borussia Dortmund win | 47.4% | 47.8% | 2.14 | +1.5% |
| Over 2.5 | 71.3% | 69.8% | 1.40 | -0.2% |
| Under 2.5 | 28.7% | 30.2% | 3.03 | -13.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | ca87a3874b0eae31b4173ae4a9324957 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:57Z |
| Market best draw last update utc | 2026-10-09T08:10:11Z |
| Market best away last update utc | 2026-10-09T08:10:12Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Coolbet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.3% |
| P btts no | 29.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.81 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.36 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.48 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.21 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 32.5% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 47.1% |
| Raw p over 1 5 | 88.0% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 70.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.10 |
| Reference draw odds | 4.10 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +1.3% |
| Draw probability edge | -0.9% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +1.5% |
| Under 2.5 probability edge | -1.5% |
| Raw edge prob home | 0.0253 |
| Raw ev home | 0.0723 |
| Raw edge prob draw | -0.0182 |
| Raw ev draw | -0.1217 |
| Raw edge prob away | -0.0071 |
| Raw ev away | 0.0075 |

</details>


---

## 2026-10-14 — Feyenoord vs Como

The model's most likely 1X2 outcome is **Como win** at **63.8%**. Expected goals are 1.84 for Feyenoord and 3.93 for Como (5.77 combined). The most likely exact score is 2-2 at 5.7%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 91.7%; Under 4.5 goals: 33.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 19.7% | 5.07 |
| Draw | 16.4% | 6.08 |
| Como win | 63.8% | 1.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 1.84 |
| Como expected goals | 3.93 |
| Expected total goals | 5.77 |
| Over 0.5 | 99.7% |
| Under 0.5 | 0.3% |
| Over 1.5 | 97.6% |
| Under 1.5 | 2.4% |
| Over 2.5 | 91.7% |
| Under 2.5 | 8.3% |
| Over 3.5 | 81.7% |
| Under 3.5 | 18.3% |
| Over 4.5 | 66.3% |
| Under 4.5 | 33.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 5.73% |
| 2 | 1-3 | 4.97% |
| 3 | 1-4 | 4.89% |
| 4 | 3-3 | 4.60% |
| 5 | 2-3 | 4.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 19.7% | 26.0% | 3.85 | -24.0% |
| Draw | 16.4% | 21.2% | 4.33 | -28.8% |
| Como win | 63.8% | 52.9% | 1.95 | +24.4% |
| Over 2.5 | 91.7% | 67.9% | 1.43 | +31.2% |
| Under 2.5 | 8.3% | 32.1% | 2.87 | -76.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T16:45:00+00:00 |
| Fixture id | 5d6f9accd6f79ae4216dfd29ccc342b2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:11Z |
| Market best draw last update utc | 2026-10-09T08:10:57Z |
| Market best away last update utc | 2026-10-09T08:10:11Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | BetOnline.ag |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | Como 1907 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 83.7% |
| P btts no | 16.3% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 356.44 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 41.10 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 12.07 |
| Fair Over 3.5 odds | 1.22 |
| Fair Under 3.5 odds | 5.47 |
| Fair Over 4.5 odds | 1.51 |
| Fair Under 4.5 odds | 2.96 |
| Unadjusted home-win probability | 13.5% |
| Unadjusted draw probability | 11.7% |
| Unadjusted away-win probability | 74.8% |
| Raw p over 1 5 | 97.8% |
| Raw p under 3 5 | 17.3% |
| Raw p btts yes | 82.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.55 |
| Reference draw odds | 4.30 |
| Reference away odds | 1.82 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.85 |
| Home probability edge | -6.2% |
| Draw probability edge | -4.7% |
| Away probability edge | +10.9% |
| Over 2.5 probability edge | +23.9% |
| Under 2.5 probability edge | -23.9% |
| Raw edge prob home | -0.1244 |
| Raw ev home | -0.4795 |
| Raw edge prob draw | -0.0945 |
| Raw ev draw | -0.4924 |
| Raw edge prob away | 0.2189 |
| Raw ev away | 0.4578 |

</details>


---

## 2026-10-14 — LASK vs Liverpool

The model's most likely 1X2 outcome is **Liverpool win** at **74.0%**. Expected goals are 0.33 for LASK and 1.48 for Liverpool (1.80 combined). The most likely exact score is 0-1 at 27.3%. Goal-market probabilities: at least one goal: 88.4%; Over 2.5 goals: 29.3%; Under 4.5 goals: 96.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 8.2% | 12.15 |
| Draw | 17.8% | 5.61 |
| Liverpool win | 74.0% | 1.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 0.33 |
| Liverpool expected goals | 1.48 |
| Expected total goals | 1.80 |
| Over 0.5 | 88.4% |
| Under 0.5 | 11.6% |
| Over 1.5 | 55.4% |
| Under 1.5 | 44.6% |
| Over 2.5 | 29.3% |
| Under 2.5 | 70.7% |
| Over 3.5 | 11.6% |
| Under 3.5 | 88.4% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 27.27% |
| 2 | 0-2 | 19.82% |
| 3 | 0-0 | 11.62% |
| 4 | 0-3 | 9.76% |
| 5 | 1-2 | 6.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| LASK win | 8.2% | 8.1% | 13.00 | +7.0% |
| Draw | 17.8% | 11.0% | 7.25 | +29.2% |
| Liverpool win | 74.0% | 80.9% | 1.29 | -4.6% |
| Over 2.5 | 29.3% | 70.4% | 1.38 | -59.6% |
| Under 2.5 | 70.7% | 29.6% | 3.10 | +119.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T16:45:00+00:00 |
| Fixture id | 2903ee092f7e08c549b130a3d394ac3c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:11Z |
| Market best draw last update utc | 2026-10-09T08:11:01Z |
| Market best away last update utc | 2026-10-09T08:10:12Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | LASK Linz |
| Matched away-team name | Liverpool FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 19.9% |
| P btts no | 80.1% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.60 |
| Fair Over 1.5 odds | 1.81 |
| Fair Under 1.5 odds | 2.24 |
| Fair Over 2.5 odds | 3.42 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.59 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.93 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 8.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 67.0% |
| Raw p over 1 5 | 53.4% |
| Raw p under 3 5 | 89.1% |
| Raw p btts yes | 21.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 9.50 |
| Reference draw odds | 7.25 |
| Reference away odds | 1.21 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | +0.1% |
| Draw probability edge | +6.8% |
| Away probability edge | -6.9% |
| Over 2.5 probability edge | -41.1% |
| Under 2.5 probability edge | +41.1% |
| Raw edge prob home | 0.0019 |
| Raw ev home | 0.0827 |
| Raw edge prob draw | 0.1363 |
| Raw ev draw | 0.7856 |
| Raw edge prob away | -0.1382 |
| Raw ev away | -0.1352 |

</details>


---

## 2026-10-14 — Manchester City vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **47.0%**. Expected goals are 1.53 for Manchester City and 2.51 for Paris Saint Germain (4.04 combined). The most likely exact score is 2-2 at 7.4%. Goal-market probabilities: at least one goal: 98.4%; Over 2.5 goals: 75.6%; Under 4.5 goals: 63.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 32.6% | 3.07 |
| Draw | 20.4% | 4.90 |
| Paris Saint Germain win | 47.0% | 2.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.53 |
| Paris Saint Germain expected goals | 2.51 |
| Expected total goals | 4.04 |
| Over 0.5 | 98.4% |
| Under 0.5 | 1.6% |
| Over 1.5 | 90.3% |
| Under 1.5 | 9.7% |
| Over 2.5 | 75.6% |
| Under 2.5 | 24.4% |
| Over 3.5 | 56.3% |
| Under 3.5 | 43.7% |
| Over 4.5 | 36.6% |
| Under 4.5 | 63.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.41% |
| 2 | 2-1 | 7.38% |
| 3 | 1-1 | 7.33% |
| 4 | 1-2 | 6.74% |
| 5 | 1-3 | 5.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 32.6% | 42.3% | 2.34 | -23.8% |
| Draw | 20.4% | 22.9% | 4.30 | -12.2% |
| Paris Saint Germain win | 47.0% | 34.8% | 2.97 | +39.6% |
| Over 2.5 | 75.6% | 67.9% | 1.44 | +8.9% |
| Under 2.5 | 24.4% | 32.1% | 2.87 | -30.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 5a1a6a04c5561897741105e30d5d7ec4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:12Z |
| Market best draw last update utc | 2026-10-09T08:10:57Z |
| Market best away last update utc | 2026-10-09T08:10:12Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 72.8% |
| P btts no | 27.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 61.58 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.28 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.10 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.29 |
| Fair Over 4.5 odds | 2.73 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 59.2% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 42.6% |
| Raw p btts yes | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.25 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.70 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.85 |
| Home probability edge | -9.7% |
| Draw probability edge | -2.5% |
| Away probability edge | +12.2% |
| Over 2.5 probability edge | +7.7% |
| Under 2.5 probability edge | -7.7% |
| Raw edge prob home | -0.1935 |
| Raw ev home | -0.4641 |
| Raw edge prob draw | -0.0503 |
| Raw ev draw | -0.2301 |
| Raw edge prob away | 0.2438 |
| Raw ev away | 0.7580 |

</details>


---

## 2026-10-14 — Real Betis vs Porto

The model's most likely 1X2 outcome is **Real Betis win** at **64.9%**. Expected goals are 4.51 for Real Betis and 1.48 for Porto (5.98 combined). The most likely exact score is 2-2 at 5.9%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 91.3%; Under 4.5 goals: 33.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 64.9% | 1.54 |
| Draw | 16.5% | 6.06 |
| Porto win | 18.6% | 5.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 4.51 |
| Porto expected goals | 1.48 |
| Expected total goals | 5.98 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.4% |
| Under 1.5 | 2.6% |
| Over 2.5 | 91.3% |
| Under 2.5 | 8.7% |
| Over 3.5 | 81.6% |
| Under 3.5 | 18.4% |
| Over 4.5 | 66.2% |
| Under 4.5 | 33.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 5.94% |
| 2 | 4-1 | 4.89% |
| 3 | 5-1 | 4.41% |
| 4 | 3-3 | 4.39% |
| 5 | 3-1 | 4.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 64.9% | 44.3% | 2.27 | +47.3% |
| Draw | 16.5% | 25.2% | 3.80 | -37.3% |
| Porto win | 18.6% | 30.5% | 3.30 | -38.6% |
| Over 2.5 | 91.3% | 56.2% | 1.78 | +62.5% |
| Under 2.5 | 8.7% | 43.8% | 2.21 | -80.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 4c7f87780ae5ab8bec9e83d6d6ec9909 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:12Z |
| Market best draw last update utc | 2026-10-09T08:10:39Z |
| Market best away last update utc | 2026-10-09T08:10:57Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Matchbook |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 79.8% |
| P btts no | 20.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 278.41 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 38.88 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 11.50 |
| Fair Over 3.5 odds | 1.23 |
| Fair Under 3.5 odds | 5.44 |
| Fair Over 4.5 odds | 1.51 |
| Fair Under 4.5 odds | 2.96 |
| Unadjusted home-win probability | 85.5% |
| Unadjusted draw probability | 7.8% |
| Unadjusted away-win probability | 6.7% |
| Raw p over 1 5 | 98.1% |
| Raw p under 3 5 | 15.4% |
| Raw p btts yes | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.14 |
| Home probability edge | +20.6% |
| Draw probability edge | -8.7% |
| Away probability edge | -11.9% |
| Over 2.5 probability edge | +35.1% |
| Under 2.5 probability edge | -35.1% |
| Raw edge prob home | 0.4125 |
| Raw ev home | 0.9415 |
| Raw edge prob draw | -0.1741 |
| Raw ev draw | -0.7037 |
| Raw edge prob away | -0.2384 |
| Raw ev away | -0.7797 |

</details>


---

## 2026-10-14 — Shakhtar Donetsk vs AEK Athens

The model's most likely 1X2 outcome is **Shakhtar Donetsk win** at **39.6%**. Expected goals are 1.45 for Shakhtar Donetsk and 1.25 for AEK Athens (2.71 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 50.5%; Under 4.5 goals: 86.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 39.6% | 2.52 |
| Draw | 25.4% | 3.94 |
| AEK Athens win | 35.0% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.45 |
| AEK Athens expected goals | 1.25 |
| Expected total goals | 2.71 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.7% |
| Under 3.5 | 71.3% |
| Over 4.5 | 13.7% |
| Under 4.5 | 86.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.99% |
| 2 | 1-0 | 9.63% |
| 3 | 0-1 | 9.46% |
| 4 | 2-1 | 8.26% |
| 5 | 1-2 | 8.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Shakhtar Donetsk win | 39.6% | 36.9% | 2.81 | +11.3% |
| Draw | 25.4% | 26.3% | 3.65 | -7.5% |
| AEK Athens win | 35.0% | 36.9% | 2.65 | -7.1% |
| Over 2.5 | 50.5% | 52.3% | 1.91 | -3.5% |
| Under 2.5 | 49.5% | 47.7% | 2.03 | +0.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | 0f961390e790ad2c80ecb3f302cad4a6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:12Z |
| Market best draw last update utc | 2026-10-09T08:10:27Z |
| Market best away last update utc | 2026-10-09T08:10:11Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 67/100 |
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.89 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.30 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 42.4% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 33.2% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 54.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.55 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.55 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 1.97 |
| Home probability edge | +2.8% |
| Draw probability edge | -0.9% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | 0.0551 |
| Raw ev home | 0.1903 |
| Raw edge prob draw | -0.0188 |
| Raw ev draw | -0.1089 |
| Raw edge prob away | -0.0363 |
| Raw ev away | -0.1195 |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **65.9%**. Expected goals are 1.40 for ŠK Slovan Bratislava and 2.20 for VfB Stuttgart (3.60 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 70.9%; Under 4.5 goals: 69.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 17.6% | 5.70 |
| Draw | 16.5% | 6.05 |
| VfB Stuttgart win | 65.9% | 1.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.40 |
| VfB Stuttgart expected goals | 2.20 |
| Expected total goals | 3.60 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 70.9% |
| Under 2.5 | 29.1% |
| Over 3.5 | 49.1% |
| Under 3.5 | 50.9% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.89% |
| 2 | 1-3 | 7.98% |
| 3 | 0-2 | 7.79% |
| 4 | 0-1 | 7.58% |
| 5 | 1-1 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ŠK Slovan Bratislava win | 17.6% | 10.7% | 9.90 | +73.8% |
| Draw | 16.5% | 13.5% | 6.25 | +3.3% |
| VfB Stuttgart win | 65.9% | 75.7% | 1.35 | -11.0% |
| Over 2.5 | 70.9% | 70.4% | 1.38 | -2.2% |
| Under 2.5 | 29.1% | 29.6% | 3.08 | -10.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | d7576351b8cb2396e32cc3de0446f3de |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T08:10:11Z |
| Market best draw last update utc | 2026-10-09T08:11:01Z |
| Market best away last update utc | 2026-10-09T08:10:12Z |
| Odds bookmakers 1x2 | 19.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.4% |
| P btts no | 34.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 50.80 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.93 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.43 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.97 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 24.4% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 56.1% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 51.6% |
| Raw p btts yes | 66.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 7.75 |
| Reference draw odds | 6.25 |
| Reference away odds | 1.29 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | +6.8% |
| Draw probability edge | +3.0% |
| Away probability edge | -9.8% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.1369 |
| Raw ev home | 1.4158 |
| Raw edge prob draw | 0.0596 |
| Raw ev draw | 0.2189 |
| Raw edge prob away | -0.1965 |
| Raw ev away | -0.2427 |

</details>


---
