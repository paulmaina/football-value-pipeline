# Bundesliga — football model report

Fixtures in this report: **18**.

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
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 10.00 |
| Additional event odds calls budget | 24.00 |
| Additional event odds league quota | 5.00 |
| Additional event odds calls this league | 5.00 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-09 — Borussia Dortmund vs Werder Bremen

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **70.4%**. Expected goals are 2.30 for Borussia Dortmund and 0.97 for Werder Bremen (3.27 combined). The most likely exact score is 2-0 at 10.7%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.7%; Under 4.5 goals: 76.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 70.4% | 1.42 |
| Draw | 17.6% | 5.68 |
| Werder Bremen win | 12.0% | 8.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.30 |
| Werder Bremen expected goals | 0.97 |
| Expected total goals | 3.27 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 64.7% |
| Under 2.5 | 35.3% |
| Over 3.5 | 42.0% |
| Under 3.5 | 58.0% |
| Over 4.5 | 23.9% |
| Under 4.5 | 76.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.66% |
| 2 | 2-1 | 10.35% |
| 3 | 1-0 | 8.32% |
| 4 | 1-1 | 8.19% |
| 5 | 3-0 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 70.4% | 74.5% | 1.38 | -2.8% |
| Draw | 17.6% | 15.1% | 6.25 | +10.0% |
| Werder Bremen win | 12.0% | 10.4% | 9.00 | +7.6% |
| Over 2.5 | 64.7% | 72.0% | 1.38 | -10.7% |
| Under 2.5 | 35.3% | 28.0% | 3.20 | +12.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-09T18:30:00+00:00 |
| Fixture id | 3fb63658405d468954f57745cd115118 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:38:07Z |
| Market best draw last update utc | 2026-10-09T14:38:23Z |
| Market best away last update utc | 2026-10-09T14:38:23Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Dortmund |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.0% |
| P btts no | 44.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.46 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.72 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.83 |
| Fair Over 3.5 odds | 2.38 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.18 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 66.4% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 13.5% |
| Raw p over 1 5 | 84.7% |
| Raw p under 3 5 | 58.6% |
| Raw p btts yes | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.33 |
| Reference draw odds | 6.25 |
| Reference away odds | 9.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.20 |
| Home probability edge | -4.1% |
| Draw probability edge | +2.5% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.0816 |
| Raw ev home | -0.0843 |
| Raw edge prob draw | 0.0500 |
| Raw ev draw | 0.2565 |
| Raw edge prob away | 0.0317 |
| Raw ev away | 0.2187 |

</details>


---

## 2026-10-10 — Augsburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **78.4%**. Expected goals are 1.04 for Augsburg and 2.87 for Bayern Munich (3.92 combined). The most likely exact score is 1-2 at 9.1%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 76.1%; Under 4.5 goals: 63.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 8.5% | 11.76 |
| Draw | 13.0% | 7.67 |
| Bayern Munich win | 78.4% | 1.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.04 |
| Bayern Munich expected goals | 2.87 |
| Expected total goals | 3.92 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 76.1% |
| Under 2.5 | 23.9% |
| Over 3.5 | 55.8% |
| Under 3.5 | 44.2% |
| Over 4.5 | 36.4% |
| Under 4.5 | 63.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.05% |
| 2 | 1-3 | 8.67% |
| 3 | 0-2 | 8.67% |
| 4 | 0-3 | 8.31% |
| 5 | 1-4 | 6.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 8.5% | 6.8% | 15.00 | +27.6% |
| Draw | 13.0% | 10.6% | 10.20 | +33.1% |
| Bayern Munich win | 78.4% | 82.6% | 1.20 | -5.9% |
| Over 2.5 | 76.1% | 85.4% | 1.15 | -12.5% |
| Under 2.5 | 23.9% | 14.6% | 5.55 | +32.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T13:30:00+00:00 |
| Fixture id | 3b71160ad20dba786c4f92e33c987d80 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:37:18Z |
| Market best draw last update utc | 2026-10-09T14:37:18Z |
| Market best away last update utc | 2026-10-09T14:38:07Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (NL) |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Augsburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.47 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.38 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.18 |
| Fair Over 3.5 odds | 1.79 |
| Fair Under 3.5 odds | 2.26 |
| Fair Over 4.5 odds | 2.74 |
| Fair Under 4.5 odds | 1.57 |
| Unadjusted home-win probability | 10.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 74.3% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 45.0% |
| Raw p btts yes | 61.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 13.00 |
| Reference draw odds | 8.50 |
| Reference away odds | 1.20 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.50 |
| Home probability edge | +1.7% |
| Draw probability edge | +2.4% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | 0.0343 |
| Raw ev home | 0.5329 |
| Raw edge prob draw | 0.0488 |
| Raw ev draw | 0.5792 |
| Raw edge prob away | -0.0830 |
| Raw ev away | -0.1084 |
| Market p over 1 5 | 95.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-09T14:33:59Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 13.00 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 29.9% |
| Market under 3 5 odds | 3.03 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T14:37:34Z |
| Market reference under 3 5 odds | 2.98 |
| Market reference under 3 5 opposite odds | 1.38 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 64.9% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T14:38:23Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.80 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-10 — FSV Mainz 05 vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **48.8%**. Expected goals are 1.08 for FSV Mainz 05 and 1.81 for Bayer Leverkusen (2.89 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 55.3%; Under 4.5 goals: 83.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 26.8% | 3.73 |
| Draw | 24.4% | 4.10 |
| Bayer Leverkusen win | 48.8% | 2.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.08 |
| Bayer Leverkusen expected goals | 1.81 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 79.3% |
| Under 1.5 | 20.7% |
| Over 2.5 | 55.3% |
| Under 2.5 | 44.7% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.58% |
| 2 | 1-2 | 8.96% |
| 3 | 0-2 | 8.33% |
| 4 | 0-1 | 8.15% |
| 5 | 2-1 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 26.8% | 32.5% | 3.10 | -16.8% |
| Draw | 24.4% | 23.6% | 4.10 | +0.1% |
| Bayer Leverkusen win | 48.8% | 44.0% | 2.31 | +12.6% |
| Over 2.5 | 55.3% | 66.7% | 1.44 | -20.4% |
| Under 2.5 | 44.7% | 33.3% | 2.84 | +27.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T13:30:00+00:00 |
| Fixture id | 418f8c26d46eaabd829f2e265673b855 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:37:33Z |
| Market best draw last update utc | 2026-10-09T14:38:23Z |
| Market best away last update utc | 2026-10-09T14:37:18Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Mainz |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.47 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.08 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.03 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 21.2% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 53.6% |
| Raw p over 1 5 | 79.5% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 56.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.00 |
| Reference draw odds | 4.10 |
| Reference away odds | 2.23 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | -5.6% |
| Draw probability edge | +0.8% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | -0.1126 |
| Raw ev home | -0.3429 |
| Raw edge prob draw | 0.0168 |
| Raw ev draw | 0.0354 |
| Raw edge prob away | 0.0957 |
| Raw ev away | 0.2370 |

</details>


---

## 2026-10-10 — RB Leipzig vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **RB Leipzig win** at **58.8%**. Expected goals are 2.13 for RB Leipzig and 1.35 for Eintracht Frankfurt (3.48 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 68.3%; Under 4.5 goals: 72.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 58.8% | 1.70 |
| Draw | 20.8% | 4.81 |
| Eintracht Frankfurt win | 20.4% | 4.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.13 |
| Eintracht Frankfurt expected goals | 1.35 |
| Expected total goals | 3.48 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 87.3% |
| Under 1.5 | 12.7% |
| Over 2.5 | 68.3% |
| Under 2.5 | 31.7% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.19% |
| 2 | 1-1 | 9.00% |
| 3 | 2-0 | 7.57% |
| 4 | 3-1 | 7.24% |
| 5 | 1-0 | 6.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 58.8% | 63.2% | 1.62 | -4.7% |
| Draw | 20.8% | 19.0% | 5.10 | +6.0% |
| Eintracht Frankfurt win | 20.4% | 17.9% | 5.30 | +8.0% |
| Over 2.5 | 68.3% | 75.6% | 1.30 | -11.2% |
| Under 2.5 | 31.7% | 24.4% | 3.60 | +14.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T16:30:00+00:00 |
| Fixture id | 01cb7a67c8ae71201ec27297455fc0e8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:37:18Z |
| Market best draw last update utc | 2026-10-09T14:38:07Z |
| Market best away last update utc | 2026-10-09T14:38:23Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 81/100 |
| P btts yes | 65.6% |
| P btts no | 34.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.10 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.89 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.15 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.63 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 54.5% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 22.9% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 54.1% |
| Raw p btts yes | 66.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.56 |
| Reference draw odds | 5.00 |
| Reference away odds | 5.30 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.60 |
| Home probability edge | -4.3% |
| Draw probability edge | +1.8% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.0867 |
| Raw ev home | -0.1170 |
| Raw edge prob draw | 0.0362 |
| Raw ev draw | 0.1520 |
| Raw edge prob away | 0.0505 |
| Raw ev away | 0.2140 |

</details>


---

## 2026-10-10 — SC Paderborn vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **56.1%**. Expected goals are 0.76 for SC Paderborn and 1.42 for VfB Stuttgart (2.18 combined). The most likely exact score is 0-1 at 16.1%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.0%; Under 4.5 goals: 92.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 19.0% | 5.28 |
| Draw | 25.0% | 4.00 |
| VfB Stuttgart win | 56.1% | 1.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.76 |
| VfB Stuttgart expected goals | 1.42 |
| Expected total goals | 2.18 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 66.0% |
| Under 1.5 | 34.0% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.1% |
| Under 3.5 | 81.9% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.07% |
| 2 | 0-2 | 12.42% |
| 3 | 1-1 | 11.31% |
| 4 | 0-0 | 10.55% |
| 5 | 1-2 | 9.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 19.0% | 19.2% | 5.20 | -1.4% |
| Draw | 25.0% | 20.2% | 5.03 | +25.6% |
| VfB Stuttgart win | 56.1% | 60.6% | 1.65 | -7.5% |
| Over 2.5 | 39.0% | 71.6% | 1.35 | -47.4% |
| Under 2.5 | 61.0% | 28.4% | 3.26 | +98.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T13:30:00+00:00 |
| Fixture id | 9aade3e736c3d113dab19e641c43e272 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:38:07Z |
| Market best draw last update utc | 2026-10-09T14:37:18Z |
| Market best away last update utc | 2026-10-09T14:38:07Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Paderborn |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 40.5% |
| P btts no | 59.5% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.48 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.51 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.40 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 18.7% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 51.6% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 41.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 5.00 |
| Reference draw odds | 4.75 |
| Reference away odds | 1.63 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -0.2% |
| Draw probability edge | +4.8% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -32.6% |
| Under 2.5 probability edge | +32.6% |
| Raw edge prob home | -0.0047 |
| Raw ev home | -0.0264 |
| Raw edge prob draw | 0.0950 |
| Raw ev draw | 0.4952 |
| Raw edge prob away | -0.0903 |
| Raw ev away | -0.1494 |

</details>


---

## 2026-10-10 — TSG Hoffenheim vs Hamburger SV

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **62.9%**. Expected goals are 2.09 for TSG Hoffenheim and 1.21 for Hamburger SV (3.30 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 65.3%; Under 4.5 goals: 75.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 62.9% | 1.59 |
| Draw | 20.2% | 4.96 |
| Hamburger SV win | 17.0% | 5.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 2.09 |
| Hamburger SV expected goals | 1.21 |
| Expected total goals | 3.30 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 65.3% |
| Under 2.5 | 34.7% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.5% |
| Under 4.5 | 75.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.82% |
| 2 | 1-1 | 9.10% |
| 3 | 2-0 | 8.94% |
| 4 | 3-1 | 7.54% |
| 5 | 1-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 62.9% | 69.1% | 1.49 | -6.3% |
| Draw | 20.2% | 17.5% | 5.40 | +8.8% |
| Hamburger SV win | 17.0% | 13.4% | 7.60 | +29.1% |
| Over 2.5 | 65.3% | 70.8% | 1.40 | -8.6% |
| Under 2.5 | 34.7% | 29.2% | 3.00 | +4.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T13:30:00+00:00 |
| Fixture id | f03c08c0ae5fd66c2d2df2053115bb94 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:37:18Z |
| Market best draw last update utc | 2026-10-09T14:38:23Z |
| Market best away last update utc | 2026-10-09T14:38:07Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Hoffenheim |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 88/100 |
| P btts yes | 61.6% |
| P btts no | 38.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.31 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.92 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.88 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.08 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 56.6% |
| Unadjusted draw probability | 22.8% |
| Unadjusted away-win probability | 20.6% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 58.0% |
| Raw p btts yes | 62.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.43 |
| Reference draw odds | 5.40 |
| Reference away odds | 7.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -6.2% |
| Draw probability edge | +2.6% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | -0.1247 |
| Raw ev home | -0.1562 |
| Raw edge prob draw | 0.0529 |
| Raw ev draw | 0.2310 |
| Raw edge prob away | 0.0719 |
| Raw ev away | 0.5637 |

</details>


---

## 2026-10-10 — Union Berlin vs Elversberg

The model's most likely 1X2 outcome is **Elversberg win** at **49.4%**. Expected goals are 1.17 for Union Berlin and 2.48 for Elversberg (3.65 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 68.8%; Under 4.5 goals: 71.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 28.6% | 3.49 |
| Draw | 22.0% | 4.55 |
| Elversberg win | 49.4% | 2.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 1.17 |
| Elversberg expected goals | 2.48 |
| Expected total goals | 3.65 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 87.6% |
| Under 1.5 | 12.4% |
| Over 2.5 | 68.8% |
| Under 2.5 | 31.2% |
| Over 3.5 | 47.2% |
| Under 3.5 | 52.8% |
| Over 4.5 | 28.5% |
| Under 4.5 | 71.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.49% |
| 2 | 2-1 | 8.18% |
| 3 | 1-2 | 7.07% |
| 4 | 2-2 | 6.22% |
| 5 | 0-2 | 6.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 28.6% | 41.9% | 2.46 | -29.5% |
| Draw | 22.0% | 24.7% | 3.90 | -14.3% |
| Elversberg win | 49.4% | 33.4% | 2.92 | +44.2% |
| Over 2.5 | 68.8% | 62.6% | 1.54 | +5.9% |
| Under 2.5 | 31.2% | 37.4% | 2.56 | -20.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-10T13:30:00+00:00 |
| Fixture id | 2fd48be0a24ed906187067d4170bf010 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:38:07Z |
| Market best draw last update utc | 2026-10-09T14:37:18Z |
| Market best away last update utc | 2026-10-09T14:38:07Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | LeoVegas (SE) |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Union Berlin |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.9% |
| P btts no | 34.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.85 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.09 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.12 |
| Fair Under 3.5 odds | 1.90 |
| Fair Over 4.5 odds | 3.51 |
| Fair Under 4.5 odds | 1.40 |
| Unadjusted home-win probability | 15.4% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 65.3% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.5% |
| Raw p btts yes | 63.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.33 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.48 |
| Home probability edge | -13.2% |
| Draw probability edge | -2.7% |
| Away probability edge | +15.9% |
| Over 2.5 probability edge | +6.2% |
| Under 2.5 probability edge | -6.2% |
| Raw edge prob home | -0.2648 |
| Raw ev home | -0.6210 |
| Raw edge prob draw | -0.0537 |
| Raw ev draw | -0.2475 |
| Raw edge prob away | 0.3185 |
| Raw ev away | 0.9067 |

</details>


---

## 2026-10-11 — 1. FC Köln vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **1. FC Köln win** at **40.8%**. Expected goals are 1.43 for 1. FC Köln and 1.55 for Borussia Monchengladbach (2.97 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 57.7%; Under 4.5 goals: 81.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 40.8% | 2.45 |
| Draw | 25.1% | 3.99 |
| Borussia Monchengladbach win | 34.1% | 2.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.43 |
| Borussia Monchengladbach expected goals | 1.55 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.3% |
| Under 4.5 | 81.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.68% |
| 2 | 2-1 | 9.68% |
| 3 | 1-2 | 7.56% |
| 4 | 1-0 | 7.35% |
| 5 | 2-0 | 6.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 40.8% | 47.8% | 2.18 | -11.0% |
| Draw | 25.1% | 23.4% | 4.10 | +2.8% |
| Borussia Monchengladbach win | 34.1% | 28.8% | 3.45 | +17.6% |
| Over 2.5 | 57.7% | 63.8% | 1.51 | -12.9% |
| Under 2.5 | 42.3% | 36.2% | 2.61 | +10.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T13:30:00+00:00 |
| Fixture id | a8801462cb97a43570956e4b3ef4aedf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:37:18Z |
| Market best draw last update utc | 2026-10-09T14:38:07Z |
| Market best away last update utc | 2026-10-09T14:38:07Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Koln |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.96 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.48 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 33.9% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 39.4% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 61.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.05 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.35 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -6.9% |
| Draw probability edge | +1.7% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.1385 |
| Raw ev home | -0.2606 |
| Raw edge prob draw | 0.0332 |
| Raw ev draw | 0.0957 |
| Raw edge prob away | 0.1054 |
| Raw ev away | 0.3578 |

</details>


---

## 2026-10-11 — SC Freiburg vs FC Schalke 04

The model's most likely 1X2 outcome is **SC Freiburg win** at **47.4%**. Expected goals are 0.90 for SC Freiburg and 0.80 for FC Schalke 04 (1.70 combined). The most likely exact score is 1-0 at 20.7%. Goal-market probabilities: at least one goal: 84.1%; Over 2.5 goals: 26.3%; Under 4.5 goals: 96.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 47.4% | 2.11 |
| Draw | 29.8% | 3.36 |
| FC Schalke 04 win | 22.8% | 4.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 0.90 |
| FC Schalke 04 expected goals | 0.80 |
| Expected total goals | 1.70 |
| Over 0.5 | 84.1% |
| Under 0.5 | 15.9% |
| Over 1.5 | 52.9% |
| Under 1.5 | 47.1% |
| Over 2.5 | 26.3% |
| Under 2.5 | 73.7% |
| Over 3.5 | 9.7% |
| Under 3.5 | 90.3% |
| Over 4.5 | 3.3% |
| Under 4.5 | 96.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.74% |
| 2 | 0-0 | 15.91% |
| 3 | 1-1 | 11.80% |
| 4 | 0-1 | 10.44% |
| 5 | 2-0 | 10.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 47.4% | 60.5% | 1.71 | -19.0% |
| Draw | 29.8% | 22.9% | 4.20 | +25.2% |
| FC Schalke 04 win | 22.8% | 16.6% | 6.00 | +36.9% |
| Over 2.5 | 26.3% | 59.0% | 1.69 | -55.5% |
| Under 2.5 | 73.7% | 41.0% | 2.38 | +75.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-11T15:30:00+00:00 |
| Fixture id | eaf509fb37413b7d055cd394667792b3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-09T14:37:18Z |
| Market best draw last update utc | 2026-10-09T14:38:23Z |
| Market best away last update utc | 2026-10-09T14:38:07Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Matchbook |
| Matched home-team name | Freiburg |
| Matched away-team name | Schalke 04 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 32.7% |
| P btts no | 67.3% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.29 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.12 |
| Fair Over 2.5 odds | 3.80 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 10.32 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.62 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 34.2% |
| Unadjusted draw probability | 36.7% |
| Unadjusted away-win probability | 29.1% |
| Raw p over 1 5 | 52.1% |
| Raw p under 3 5 | 90.6% |
| Raw p btts yes | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.63 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.75 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.28 |
| Home probability edge | -13.2% |
| Draw probability edge | +6.9% |
| Away probability edge | +6.2% |
| Over 2.5 probability edge | -32.7% |
| Under 2.5 probability edge | +32.7% |
| Raw edge prob home | -0.2630 |
| Raw ev home | -0.4146 |
| Raw edge prob draw | 0.1382 |
| Raw ev draw | 0.5420 |
| Raw edge prob away | 0.1248 |
| Raw ev away | 0.7432 |
| Market p over 1 5 | 82.7% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T14:37:34Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 63.9% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T14:37:46Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 57.9% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T14:38:23Z |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-16 — Eintracht Frankfurt vs 1. FC Köln

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **56.6%**. Expected goals are 2.20 for Eintracht Frankfurt and 1.06 for 1. FC Köln (3.26 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 62.6%; Under 4.5 goals: 77.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 56.6% | 1.77 |
| Draw | 22.1% | 4.52 |
| 1. FC Köln win | 21.3% | 4.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 2.20 |
| 1. FC Köln expected goals | 1.06 |
| Expected total goals | 3.26 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.6% |
| Under 2.5 | 37.4% |
| Over 3.5 | 40.3% |
| Under 3.5 | 59.7% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.21% |
| 2 | 2-1 | 8.94% |
| 3 | 2-0 | 8.45% |
| 4 | 1-0 | 6.83% |
| 5 | 3-1 | 6.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 56.6% | 50.8% | 2.00 | +13.1% |
| Draw | 22.1% | 22.8% | 4.30 | -4.8% |
| 1. FC Köln win | 21.3% | 26.4% | 3.65 | -22.3% |
| Over 2.5 | 62.6% | 69.0% | 1.40 | -12.3% |
| Under 2.5 | 37.4% | 31.0% | 3.00 | +12.1% |

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
| Market best home last update utc | 2026-10-09T14:37:18Z |
| Market best draw last update utc | 2026-10-09T14:37:18Z |
| Market best away last update utc | 2026-10-09T14:38:23Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 81/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 59.6% |
| P btts no | 40.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.26 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.29 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.48 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.45 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 62.3% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 16.2% |
| Raw p over 1 5 | 84.6% |
| Raw p under 3 5 | 59.0% |
| Raw p btts yes | 59.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.93 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.65 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +5.8% |
| Draw probability edge | -0.7% |
| Away probability edge | -5.1% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.1151 |
| Raw ev home | 0.2465 |
| Raw edge prob draw | -0.0137 |
| Raw ev draw | -0.0776 |
| Raw edge prob away | -0.1014 |
| Raw ev away | -0.4078 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **74.6%**. Expected goals are 2.79 for Bayern Munich and 1.24 for RB Leipzig (4.02 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 77.7%; Under 4.5 goals: 61.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 74.6% | 1.34 |
| Draw | 14.4% | 6.97 |
| RB Leipzig win | 11.1% | 9.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.79 |
| RB Leipzig expected goals | 1.24 |
| Expected total goals | 4.02 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 77.7% |
| Under 2.5 | 22.3% |
| Over 3.5 | 57.9% |
| Under 3.5 | 42.1% |
| Over 4.5 | 38.6% |
| Under 4.5 | 61.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.27% |
| 2 | 3-1 | 8.61% |
| 3 | 2-0 | 7.51% |
| 4 | 3-0 | 6.97% |
| 5 | 4-1 | 6.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 74.6% | 80.0% | 1.27 | -5.3% |
| Draw | 14.4% | 11.6% | 8.00 | +14.8% |
| RB Leipzig win | 11.1% | 8.4% | 11.20 | +24.0% |
| Over 2.5 | 77.7% | 83.8% | 1.18 | -8.3% |
| Under 2.5 | 22.3% | 16.2% | 5.01 | +11.8% |

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
| Market best home last update utc | 2026-10-09T14:37:18Z |
| Market best draw last update utc | 2026-10-09T14:38:07Z |
| Market best away last update utc | 2026-10-09T14:37:18Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Bayern Munich |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.2% |
| P btts no | 33.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 48.89 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.50 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.48 |
| Fair Over 3.5 odds | 1.73 |
| Fair Under 3.5 odds | 2.38 |
| Fair Over 4.5 odds | 2.59 |
| Fair Under 4.5 odds | 1.63 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 13.8% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 42.9% |
| Raw p btts yes | 67.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.24 |
| Reference draw odds | 8.00 |
| Reference away odds | 11.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.17 |
| Reference Under 2.5 odds | 5.00 |
| Home probability edge | -5.5% |
| Draw probability edge | +2.7% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.1092 |
| Raw ev home | -0.1222 |
| Raw edge prob draw | 0.0548 |
| Raw ev draw | 0.3676 |
| Raw edge prob away | 0.0544 |
| Raw ev away | 0.5445 |
| Market p over 1 5 | 95.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-09T14:36:29Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 13.00 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 30.6% |
| Market under 3 5 odds | 2.78 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T14:38:07Z |
| Market reference under 3 5 odds | 2.78 |
| Market reference under 3 5 opposite odds | 1.37 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 70.8% |
| Market btts yes odds | 1.38 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-09T14:37:18Z |
| Market reference btts yes odds | 1.36 |
| Market reference btts yes opposite odds | 3.00 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **57.1%**. Expected goals are 2.96 for Elversberg and 1.17 for Augsburg (4.13 combined). The most likely exact score is 1-1 at 7.9%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 75.7%; Under 4.5 goals: 63.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 57.1% | 1.75 |
| Draw | 19.8% | 5.05 |
| Augsburg win | 23.1% | 4.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.96 |
| Augsburg expected goals | 1.17 |
| Expected total goals | 4.13 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 91.3% |
| Under 1.5 | 8.7% |
| Over 2.5 | 75.7% |
| Under 2.5 | 24.3% |
| Over 3.5 | 56.3% |
| Under 3.5 | 43.7% |
| Over 4.5 | 37.0% |
| Under 4.5 | 63.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.87% |
| 2 | 1-2 | 6.60% |
| 3 | 2-1 | 6.44% |
| 4 | 3-1 | 6.36% |
| 5 | 2-2 | 6.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 57.1% | 41.1% | 2.55 | +45.7% |
| Draw | 19.8% | 24.1% | 4.00 | -20.8% |
| Augsburg win | 23.1% | 34.8% | 2.80 | -35.4% |
| Over 2.5 | 75.7% | 66.7% | 1.47 | +11.2% |
| Under 2.5 | 24.3% | 33.3% | 2.71 | -34.1% |

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
| Market best home last update utc | 2026-10-09T14:37:18Z |
| Market best draw last update utc | 2026-10-09T14:38:23Z |
| Market best away last update utc | 2026-10-09T14:38:23Z |
| Odds bookmakers 1x2 | 15.00 |
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
| P btts yes | 68.5% |
| P btts no | 31.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.63 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.47 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.11 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.29 |
| Fair Over 4.5 odds | 2.71 |
| Fair Under 4.5 odds | 1.59 |
| Unadjusted home-win probability | 73.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.9% |
| Raw p btts yes | 65.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.38 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.80 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | +16.0% |
| Draw probability edge | -4.3% |
| Away probability edge | -11.7% |
| Over 2.5 probability edge | +8.9% |
| Under 2.5 probability edge | -8.9% |
| Raw edge prob home | 0.3206 |
| Raw ev home | 0.8655 |
| Raw edge prob draw | -0.0866 |
| Raw ev draw | -0.3813 |
| Raw edge prob away | -0.2340 |
| Raw ev away | -0.6814 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T14:37:52Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 55.3% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T14:36:29Z |
| Market reference under 3 5 odds | 1.74 |
| Market reference under 3 5 opposite odds | 2.12 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T14:37:52Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.80 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FC Schalke 04 win** at **34.1%**. Expected goals are 0.87 for FC Schalke 04 and 0.69 for FSV Mainz 05 (1.56 combined). The most likely exact score is 0-0 at 18.6%. Goal-market probabilities: at least one goal: 81.4%; Over 2.5 goals: 22.1%; Under 4.5 goals: 97.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 34.1% | 2.93 |
| Draw | 31.9% | 3.14 |
| FSV Mainz 05 win | 34.0% | 2.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| FSV Mainz 05 expected goals | 0.69 |
| Expected total goals | 1.56 |
| Over 0.5 | 81.4% |
| Under 0.5 | 18.6% |
| Over 1.5 | 47.9% |
| Under 1.5 | 52.1% |
| Over 2.5 | 22.1% |
| Under 2.5 | 77.9% |
| Over 3.5 | 7.5% |
| Under 3.5 | 92.5% |
| Over 4.5 | 2.3% |
| Under 4.5 | 97.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.60% |
| 2 | 0-1 | 17.52% |
| 3 | 1-0 | 16.02% |
| 4 | 1-1 | 11.59% |
| 5 | 2-0 | 7.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 34.1% | 31.9% | 3.05 | +4.0% |
| Draw | 31.9% | 25.5% | 3.80 | +21.1% |
| FSV Mainz 05 win | 34.0% | 42.6% | 2.44 | -17.0% |
| Over 2.5 | 22.1% | 60.1% | 1.66 | -63.3% |
| Under 2.5 | 77.9% | 39.9% | 2.42 | +88.5% |

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
| Market best home last update utc | 2026-10-09T14:38:23Z |
| Market best draw last update utc | 2026-10-09T14:38:23Z |
| Market best away last update utc | 2026-10-09T14:37:18Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Schalke 04 |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 29.1% |
| P btts no | 70.9% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.38 |
| Fair Over 1.5 odds | 2.09 |
| Fair Under 1.5 odds | 1.92 |
| Fair Over 2.5 odds | 4.52 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 13.41 |
| Fair Under 3.5 odds | 1.08 |
| Fair Over 4.5 odds | 43.18 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 36.3% |
| Unadjusted draw probability | 38.3% |
| Unadjusted away-win probability | 25.4% |
| Raw p over 1 5 | 47.5% |
| Raw p under 3 5 | 92.7% |
| Raw p btts yes | 30.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.05 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.30 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.33 |
| Home probability edge | +2.2% |
| Draw probability edge | +6.4% |
| Away probability edge | -8.6% |
| Over 2.5 probability edge | -37.9% |
| Under 2.5 probability edge | +37.9% |
| Raw edge prob home | 0.0438 |
| Raw ev home | 0.1070 |
| Raw edge prob draw | 0.1278 |
| Raw ev draw | 0.4539 |
| Raw edge prob away | -0.1716 |
| Raw ev away | -0.3791 |
| Market p over 1 5 | 84.4% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T14:37:52Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 62.4% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T14:38:07Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.35 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T14:37:52Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **56.5%**. Expected goals are 1.11 for Hamburger SV and 2.02 for VfB Stuttgart (3.13 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.8%; Under 4.5 goals: 79.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 21.0% | 4.76 |
| Draw | 22.5% | 4.45 |
| VfB Stuttgart win | 56.5% | 1.77 |

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
| Over 2.5 | 60.8% |
| Under 2.5 | 39.2% |
| Over 3.5 | 38.1% |
| Under 3.5 | 61.9% |
| Over 4.5 | 20.8% |
| Under 4.5 | 79.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.44% |
| 2 | 1-2 | 9.76% |
| 3 | 0-2 | 8.79% |
| 4 | 0-1 | 7.70% |
| 5 | 1-3 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 21.0% | 22.7% | 4.20 | -11.7% |
| Draw | 22.5% | 21.6% | 4.40 | -1.2% |
| VfB Stuttgart win | 56.5% | 55.7% | 1.90 | +7.4% |
| Over 2.5 | 60.8% | 70.8% | 1.38 | -16.1% |
| Under 2.5 | 39.2% | 29.2% | 3.10 | +21.6% |

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
| Market best home last update utc | 2026-10-09T14:38:23Z |
| Market best draw last update utc | 2026-10-09T14:38:23Z |
| Market best away last update utc | 2026-10-09T14:37:18Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Hamburg |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 88/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 59.1% |
| P btts no | 40.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.22 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.86 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.62 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.82 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 19.4% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 57.3% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 61.8% |
| Raw p btts yes | 59.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 4.20 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.76 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -1.7% |
| Draw probability edge | +0.9% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | -0.0331 |
| Raw ev home | -0.1869 |
| Raw edge prob draw | 0.0171 |
| Raw ev draw | 0.0257 |
| Raw edge prob away | 0.0160 |
| Raw ev away | 0.0893 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **60.4%**. Expected goals are 0.94 for Union Berlin and 1.92 for Borussia Dortmund (2.87 combined). The most likely exact score is 0-2 at 10.7%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 55.2%; Under 4.5 goals: 83.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.1% | 5.84 |
| Draw | 22.5% | 4.45 |
| Borussia Dortmund win | 60.4% | 1.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.92 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.5% |
| Under 4.5 | 83.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 10.74% |
| 2 | 1-1 | 10.72% |
| 3 | 1-2 | 10.11% |
| 4 | 0-1 | 10.07% |
| 5 | 0-3 | 6.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.1% | 17.5% | 5.40 | -7.5% |
| Draw | 22.5% | 21.1% | 4.50 | +1.2% |
| Borussia Dortmund win | 60.4% | 61.5% | 1.73 | +4.5% |
| Over 2.5 | 55.2% | 66.7% | 1.49 | -17.8% |
| Under 2.5 | 44.8% | 33.3% | 2.70 | +21.1% |

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
| Market best home last update utc | 2026-10-09T14:38:23Z |
| Market best draw last update utc | 2026-10-09T14:38:07Z |
| Market best away last update utc | 2026-10-09T14:37:18Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Unibet (NL) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Union Berlin |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 52.8% |
| P btts no | 47.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.69 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 5.40 |
| Reference draw odds | 4.50 |
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | -0.3% |
| Draw probability edge | +1.4% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -11.6% |
| Under 2.5 probability edge | +11.6% |
| Raw edge prob home | -0.0063 |
| Raw ev home | -0.0916 |
| Raw edge prob draw | 0.0281 |
| Raw ev draw | 0.0751 |
| Raw edge prob away | -0.0219 |
| Raw ev away | 0.0257 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **48.0%**. Expected goals are 1.16 for Werder Bremen and 0.74 for SC Paderborn (1.91 combined). The most likely exact score is 1-0 at 17.2%. Goal-market probabilities: at least one goal: 86.2%; Over 2.5 goals: 31.3%; Under 4.5 goals: 95.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 48.0% | 2.08 |
| Draw | 28.5% | 3.51 |
| SC Paderborn win | 23.5% | 4.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.16 |
| SC Paderborn expected goals | 0.74 |
| Expected total goals | 1.91 |
| Over 0.5 | 86.2% |
| Under 0.5 | 13.8% |
| Over 1.5 | 58.6% |
| Under 1.5 | 41.4% |
| Over 2.5 | 31.3% |
| Under 2.5 | 68.7% |
| Over 3.5 | 12.9% |
| Under 3.5 | 87.1% |
| Over 4.5 | 4.7% |
| Under 4.5 | 95.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.25% |
| 2 | 0-0 | 13.82% |
| 3 | 1-1 | 12.09% |
| 4 | 2-0 | 10.89% |
| 5 | 0-1 | 10.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 48.0% | 51.6% | 1.91 | -8.3% |
| Draw | 28.5% | 23.6% | 4.26 | +21.5% |
| SC Paderborn win | 23.5% | 24.8% | 4.25 | -0.3% |
| Over 2.5 | 31.3% | 61.8% | 1.56 | -51.1% |
| Under 2.5 | 68.7% | 38.2% | 2.47 | +69.6% |

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
| Market best home last update utc | 2026-10-09T14:38:23Z |
| Market best draw last update utc | 2026-10-09T14:37:18Z |
| Market best away last update utc | 2026-10-09T14:37:51Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Nordic Bet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 36.3% |
| P btts no | 63.7% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.23 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.42 |
| Fair Over 2.5 odds | 3.19 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.75 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 21.15 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 44.5% |
| Unadjusted draw probability | 33.4% |
| Unadjusted away-win probability | 22.1% |
| Raw p over 1 5 | 58.1% |
| Raw p under 3 5 | 87.4% |
| Raw p btts yes | 37.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.91 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.90 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -3.5% |
| Draw probability edge | +4.9% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -30.5% |
| Under 2.5 probability edge | +30.5% |
| Raw edge prob home | -0.0707 |
| Raw ev home | -0.1500 |
| Raw edge prob draw | 0.0984 |
| Raw ev draw | 0.4242 |
| Raw edge prob away | -0.0277 |
| Raw ev away | -0.0621 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **63.3%**. Expected goals are 2.44 for Bayer Leverkusen and 0.96 for SC Freiburg (3.41 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 65.3%; Under 4.5 goals: 75.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 63.3% | 1.58 |
| Draw | 19.8% | 5.04 |
| SC Freiburg win | 16.8% | 5.95 |

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
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.13% |
| 2 | 2-0 | 9.08% |
| 3 | 2-1 | 8.74% |
| 4 | 3-0 | 7.39% |
| 5 | 3-1 | 7.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 63.3% | 57.6% | 1.70 | +7.7% |
| Draw | 19.8% | 20.9% | 4.60 | -8.7% |
| SC Freiburg win | 16.8% | 21.4% | 4.83 | -18.8% |
| Over 2.5 | 65.3% | 66.3% | 1.49 | -2.7% |
| Under 2.5 | 34.7% | 33.7% | 2.67 | -7.4% |

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
| Market best home last update utc | 2026-10-09T14:37:18Z |
| Market best draw last update utc | 2026-10-09T14:37:33Z |
| Market best away last update utc | 2026-10-09T14:37:18Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Leverkusen |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.84 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.97 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.88 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.00 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.7% |
| Raw p btts yes | 57.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.70 |
| Reference draw odds | 4.50 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | +5.7% |
| Draw probability edge | -1.1% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | 0.1147 |
| Raw ev home | 0.1743 |
| Raw edge prob draw | -0.0221 |
| Raw ev draw | -0.1381 |
| Raw edge prob away | -0.0926 |
| Raw ev away | -0.4114 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **42.1%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 72.0%; Under 4.5 goals: 68.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 34.9% | 2.86 |
| Draw | 22.9% | 4.36 |
| TSG Hoffenheim win | 42.1% | 2.37 |

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
| Over 3.5 | 51.0% |
| Under 3.5 | 49.0% |
| Over 4.5 | 31.8% |
| Under 4.5 | 68.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.10% |
| 2 | 1-2 | 8.87% |
| 3 | 2-2 | 7.14% |
| 4 | 2-1 | 6.84% |
| 5 | 1-3 | 5.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 34.9% | 28.6% | 3.58 | +25.1% |
| Draw | 22.9% | 22.6% | 4.26 | -2.4% |
| TSG Hoffenheim win | 42.1% | 48.8% | 2.00 | -15.7% |
| Over 2.5 | 72.0% | 68.5% | 1.40 | +0.7% |
| Under 2.5 | 28.0% | 31.5% | 3.00 | -15.9% |

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
| Market best home last update utc | 2026-10-09T14:37:18Z |
| Market best draw last update utc | 2026-10-09T14:37:18Z |
| Market best away last update utc | 2026-10-09T14:38:23Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | M'gladbach |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 72.2% |
| P btts no | 27.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.87 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.35 |
| Reference draw odds | 4.20 |
| Reference away odds | 2.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | +6.3% |
| Draw probability edge | +0.3% |
| Away probability edge | -6.6% |
| Over 2.5 probability edge | +3.4% |
| Under 2.5 probability edge | -3.4% |
| Raw edge prob home | 0.1269 |
| Raw ev home | 0.4780 |
| Raw edge prob draw | 0.0059 |
| Raw ev draw | -0.0111 |
| Raw edge prob away | -0.1328 |
| Raw ev away | -0.2899 |

</details>


---
