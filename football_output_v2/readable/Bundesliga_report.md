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

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **69.5%**. Expected goals are 2.30 for Borussia Dortmund and 0.97 for Werder Bremen (3.27 combined). The most likely exact score is 2-0 at 10.5%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 64.5%; Under 4.5 goals: 76.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 69.5% | 1.44 |
| Draw | 18.1% | 5.53 |
| Werder Bremen win | 12.4% | 8.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.30 |
| Werder Bremen expected goals | 0.97 |
| Expected total goals | 3.27 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 64.5% |
| Under 2.5 | 35.5% |
| Over 3.5 | 41.9% |
| Under 3.5 | 58.1% |
| Over 4.5 | 23.8% |
| Under 4.5 | 76.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.52% |
| 2 | 2-1 | 10.21% |
| 3 | 1-1 | 8.42% |
| 4 | 1-0 | 8.21% |
| 5 | 3-0 | 8.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 69.5% | 72.6% | 1.38 | -4.1% |
| Draw | 18.1% | 16.1% | 6.25 | +13.1% |
| Werder Bremen win | 12.4% | 11.3% | 9.00 | +11.6% |
| Over 2.5 | 64.5% | 70.8% | 1.40 | -9.7% |
| Under 2.5 | 35.5% | 29.2% | 3.00 | +6.6% |

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
| Market best home last update utc | 2026-10-09T15:20:31Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
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
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.79 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.68 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.39 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.20 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 66.4% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 13.5% |
| Raw p over 1 5 | 84.7% |
| Raw p under 3 5 | 58.6% |
| Raw p btts yes | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.36 |
| Reference draw odds | 5.80 |
| Reference away odds | 8.18 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -3.1% |
| Draw probability edge | +2.0% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | -0.0629 |
| Raw ev home | -0.0843 |
| Raw edge prob draw | 0.0401 |
| Raw ev draw | 0.2565 |
| Raw edge prob away | 0.0228 |
| Raw ev away | 0.2187 |

</details>


---

## 2026-10-10 — Augsburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **79.1%**. Expected goals are 1.04 for Augsburg and 2.87 for Bayern Munich (3.92 combined). The most likely exact score is 1-2 at 9.1%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 76.2%; Under 4.5 goals: 63.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 8.2% | 12.27 |
| Draw | 12.7% | 7.84 |
| Bayern Munich win | 79.1% | 1.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.04 |
| Bayern Munich expected goals | 2.87 |
| Expected total goals | 3.92 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 91.3% |
| Under 1.5 | 8.7% |
| Over 2.5 | 76.2% |
| Under 2.5 | 23.8% |
| Over 3.5 | 56.0% |
| Under 3.5 | 44.0% |
| Over 4.5 | 36.6% |
| Under 4.5 | 63.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.13% |
| 2 | 1-3 | 8.74% |
| 3 | 0-2 | 8.74% |
| 4 | 0-3 | 8.38% |
| 5 | 1-4 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 8.2% | 6.1% | 15.00 | +22.3% |
| Draw | 12.7% | 10.0% | 10.20 | +30.0% |
| Bayern Munich win | 79.1% | 83.9% | 1.20 | -5.1% |
| Over 2.5 | 76.2% | 85.9% | 1.15 | -12.3% |
| Under 2.5 | 23.8% | 14.1% | 5.55 | +31.9% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:20:45Z |
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
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.52 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.46 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.21 |
| Fair Over 3.5 odds | 1.79 |
| Fair Under 3.5 odds | 2.27 |
| Fair Over 4.5 odds | 2.74 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 10.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 74.3% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 45.0% |
| Raw p btts yes | 61.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 14.00 |
| Reference draw odds | 8.75 |
| Reference away odds | 1.18 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.40 |
| Home probability edge | +2.1% |
| Draw probability edge | +2.7% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | 0.0413 |
| Raw ev home | 0.5329 |
| Raw edge prob draw | 0.0546 |
| Raw ev draw | 0.5792 |
| Raw edge prob away | -0.0960 |
| Raw ev away | -0.1084 |
| Market p over 1 5 | 95.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-09T15:19:23Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 13.00 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 30.0% |
| Market under 3 5 odds | 3.03 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T15:20:49Z |
| Market reference under 3 5 odds | 3.03 |
| Market reference under 3 5 opposite odds | 1.39 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 64.9% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T15:20:30Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.80 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-10 — FSV Mainz 05 vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **49.0%**. Expected goals are 1.08 for FSV Mainz 05 and 1.81 for Bayer Leverkusen (2.89 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 55.2%; Under 4.5 goals: 83.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 26.4% | 3.78 |
| Draw | 24.6% | 4.06 |
| Bayer Leverkusen win | 49.0% | 2.04 |

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
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 32.5% |
| Under 3.5 | 67.5% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.67% |
| 2 | 1-2 | 9.00% |
| 3 | 0-2 | 8.36% |
| 4 | 0-1 | 8.18% |
| 5 | 2-1 | 7.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 26.4% | 31.7% | 3.10 | -18.0% |
| Draw | 24.6% | 24.0% | 4.10 | +0.9% |
| Bayer Leverkusen win | 49.0% | 44.4% | 2.31 | +13.1% |
| Over 2.5 | 55.2% | 67.7% | 1.44 | -20.5% |
| Under 2.5 | 44.8% | 32.3% | 2.84 | +27.2% |

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
| Market best home last update utc | 2026-10-09T15:20:15Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
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
| Fair Under 0.5 odds | 15.35 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.08 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.04 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 21.2% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 53.6% |
| Raw p over 1 5 | 79.5% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 56.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.05 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.82 |
| Home probability edge | -5.2% |
| Draw probability edge | +0.6% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -12.5% |
| Under 2.5 probability edge | +12.5% |
| Raw edge prob home | -0.1048 |
| Raw ev home | -0.3429 |
| Raw edge prob draw | 0.0130 |
| Raw ev draw | 0.0354 |
| Raw edge prob away | 0.0919 |
| Raw ev away | 0.2370 |

</details>


---

## 2026-10-10 — RB Leipzig vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **RB Leipzig win** at **58.0%**. Expected goals are 2.13 for RB Leipzig and 1.35 for Eintracht Frankfurt (3.48 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 68.2%; Under 4.5 goals: 72.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 58.0% | 1.72 |
| Draw | 20.8% | 4.81 |
| Eintracht Frankfurt win | 21.2% | 4.71 |

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
| Over 2.5 | 68.2% |
| Under 2.5 | 31.8% |
| Over 3.5 | 46.2% |
| Under 3.5 | 53.8% |
| Over 4.5 | 27.5% |
| Under 4.5 | 72.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.05% |
| 2 | 1-1 | 9.00% |
| 3 | 2-0 | 7.46% |
| 4 | 3-1 | 7.14% |
| 5 | 1-0 | 6.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 58.0% | 61.5% | 1.62 | -6.0% |
| Draw | 20.8% | 19.0% | 5.10 | +5.9% |
| Eintracht Frankfurt win | 21.2% | 19.5% | 5.30 | +12.4% |
| Over 2.5 | 68.2% | 75.4% | 1.30 | -11.3% |
| Under 2.5 | 31.8% | 24.6% | 3.60 | +14.3% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:20:31Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
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
| Fair Under 0.5 odds | 27.11 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.87 |
| Fair Over 2.5 odds | 1.47 |
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
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.60 |
| Reference draw odds | 5.00 |
| Reference away odds | 4.86 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.55 |
| Home probability edge | -3.5% |
| Draw probability edge | +1.8% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -7.2% |
| Under 2.5 probability edge | +7.2% |
| Raw edge prob home | -0.0702 |
| Raw ev home | -0.1170 |
| Raw edge prob draw | 0.0364 |
| Raw ev draw | 0.1520 |
| Raw edge prob away | 0.0339 |
| Raw ev away | 0.2140 |

</details>


---

## 2026-10-10 — SC Paderborn vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **56.2%**. Expected goals are 0.76 for SC Paderborn and 1.42 for VfB Stuttgart (2.18 combined). The most likely exact score is 0-1 at 16.1%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.0%; Under 4.5 goals: 92.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 18.9% | 5.29 |
| Draw | 24.9% | 4.01 |
| VfB Stuttgart win | 56.2% | 1.78 |

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
| Over 3.5 | 18.2% |
| Under 3.5 | 81.8% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.11% |
| 2 | 0-2 | 12.45% |
| 3 | 1-1 | 11.28% |
| 4 | 0-0 | 10.52% |
| 5 | 1-2 | 9.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 18.9% | 19.1% | 5.30 | +0.1% |
| Draw | 24.9% | 20.1% | 5.03 | +25.3% |
| VfB Stuttgart win | 56.2% | 60.8% | 1.64 | -7.8% |
| Over 2.5 | 39.0% | 72.4% | 1.35 | -47.3% |
| Under 2.5 | 61.0% | 27.6% | 3.26 | +98.9% |

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
| Market best home last update utc | 2026-10-09T15:20:31Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:20:31Z |
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
| Fair Under 0.5 odds | 9.51 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.51 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.38 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 18.7% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 51.6% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 41.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 5.00 |
| Reference draw odds | 4.75 |
| Reference away odds | 1.62 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.20 |
| Home probability edge | -0.2% |
| Draw probability edge | +4.8% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -33.4% |
| Under 2.5 probability edge | +33.4% |
| Raw edge prob home | -0.0034 |
| Raw ev home | -0.0077 |
| Raw edge prob draw | 0.0963 |
| Raw ev draw | 0.4952 |
| Raw edge prob away | -0.0929 |
| Raw ev away | -0.1546 |

</details>


---

## 2026-10-10 — TSG Hoffenheim vs Hamburger SV

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **62.3%**. Expected goals are 2.09 for TSG Hoffenheim and 1.21 for Hamburger SV (3.30 combined). The most likely exact score is 2-1 at 10.7%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 65.0%; Under 4.5 goals: 75.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 62.3% | 1.61 |
| Draw | 20.9% | 4.80 |
| Hamburger SV win | 16.9% | 5.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 2.09 |
| Hamburger SV expected goals | 1.21 |
| Expected total goals | 3.30 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 65.0% |
| Under 2.5 | 35.0% |
| Over 3.5 | 42.6% |
| Under 3.5 | 57.4% |
| Over 4.5 | 24.4% |
| Under 4.5 | 75.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.72% |
| 2 | 1-1 | 9.41% |
| 3 | 2-0 | 8.85% |
| 4 | 3-1 | 7.47% |
| 5 | 1-0 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 62.3% | 67.9% | 1.49 | -7.2% |
| Draw | 20.9% | 18.9% | 5.40 | +12.6% |
| Hamburger SV win | 16.9% | 13.2% | 7.60 | +28.3% |
| Over 2.5 | 65.0% | 69.6% | 1.40 | -9.0% |
| Under 2.5 | 35.0% | 30.4% | 3.00 | +5.0% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:20:31Z |
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
| P btts yes | 61.8% |
| P btts no | 38.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.49 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.89 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.10 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 56.6% |
| Unadjusted draw probability | 22.8% |
| Unadjusted away-win probability | 20.6% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 58.0% |
| Raw p btts yes | 62.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.45 |
| Reference draw odds | 4.95 |
| Reference away odds | 7.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | -5.6% |
| Draw probability edge | +1.9% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.1128 |
| Raw ev home | -0.1562 |
| Raw edge prob draw | 0.0389 |
| Raw ev draw | 0.2310 |
| Raw edge prob away | 0.0739 |
| Raw ev away | 0.5637 |

</details>


---

## 2026-10-10 — Union Berlin vs Elversberg

The model's most likely 1X2 outcome is **Elversberg win** at **49.6%**. Expected goals are 1.17 for Union Berlin and 2.48 for Elversberg (3.65 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 68.7%; Under 4.5 goals: 71.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 28.3% | 3.53 |
| Draw | 22.1% | 4.51 |
| Elversberg win | 49.6% | 2.02 |

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
| Over 2.5 | 68.7% |
| Under 2.5 | 31.3% |
| Over 3.5 | 47.3% |
| Under 3.5 | 52.7% |
| Over 4.5 | 28.5% |
| Under 4.5 | 71.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.56% |
| 2 | 2-1 | 8.08% |
| 3 | 1-2 | 7.10% |
| 4 | 2-2 | 6.26% |
| 5 | 0-2 | 6.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 28.3% | 41.2% | 2.48 | -29.8% |
| Draw | 22.1% | 25.0% | 3.90 | -13.6% |
| Elversberg win | 49.6% | 33.8% | 2.90 | +43.7% |
| Over 2.5 | 68.7% | 62.7% | 1.54 | +5.9% |
| Under 2.5 | 31.3% | 37.3% | 2.56 | -20.0% |

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
| Market best home last update utc | 2026-10-09T15:20:31Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | LeoVegas (SE) |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Union Berlin |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.9% |
| P btts no | 34.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.65 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.10 |
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
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.37 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.87 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -12.9% |
| Draw probability edge | -2.9% |
| Away probability edge | +15.7% |
| Over 2.5 probability edge | +6.1% |
| Under 2.5 probability edge | -6.1% |
| Raw edge prob home | -0.2577 |
| Raw ev home | -0.6179 |
| Raw edge prob draw | -0.0571 |
| Raw ev draw | -0.2475 |
| Raw edge prob away | 0.3148 |
| Raw ev away | 0.8936 |

</details>


---

## 2026-10-11 — 1. FC Köln vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **1. FC Köln win** at **40.2%**. Expected goals are 1.43 for 1. FC Köln and 1.55 for Borussia Monchengladbach (2.97 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 57.7%; Under 4.5 goals: 81.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 40.2% | 2.49 |
| Draw | 25.1% | 3.99 |
| Borussia Monchengladbach win | 34.7% | 2.88 |

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
| 1 | 1-1 | 11.70% |
| 2 | 2-1 | 9.53% |
| 3 | 1-2 | 7.70% |
| 4 | 1-0 | 7.24% |
| 5 | 2-0 | 6.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 40.2% | 46.5% | 2.18 | -12.4% |
| Draw | 25.1% | 23.5% | 4.10 | +2.9% |
| Borussia Monchengladbach win | 34.7% | 30.1% | 3.45 | +19.8% |
| Over 2.5 | 57.7% | 64.6% | 1.51 | -12.9% |
| Under 2.5 | 42.3% | 35.4% | 2.61 | +10.5% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:20:45Z |
| Market best away last update utc | 2026-10-09T15:20:31Z |
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
| Fair Under 0.5 odds | 16.94 |
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
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.10 |
| Reference draw odds | 4.07 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Home probability edge | -6.3% |
| Draw probability edge | +1.6% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | -0.1255 |
| Raw ev home | -0.2606 |
| Raw edge prob draw | 0.0327 |
| Raw ev draw | 0.0957 |
| Raw edge prob away | 0.0928 |
| Raw ev away | 0.3578 |

</details>


---

## 2026-10-11 — SC Freiburg vs FC Schalke 04

The model's most likely 1X2 outcome is **SC Freiburg win** at **46.7%**. Expected goals are 0.90 for SC Freiburg and 0.80 for FC Schalke 04 (1.70 combined). The most likely exact score is 1-0 at 20.5%. Goal-market probabilities: at least one goal: 83.7%; Over 2.5 goals: 26.1%; Under 4.5 goals: 96.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 46.7% | 2.14 |
| Draw | 30.5% | 3.28 |
| FC Schalke 04 win | 22.8% | 4.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 0.90 |
| FC Schalke 04 expected goals | 0.80 |
| Expected total goals | 1.70 |
| Over 0.5 | 83.7% |
| Under 0.5 | 16.3% |
| Over 1.5 | 52.8% |
| Under 1.5 | 47.2% |
| Over 2.5 | 26.1% |
| Under 2.5 | 73.9% |
| Over 3.5 | 9.7% |
| Under 3.5 | 90.3% |
| Over 4.5 | 3.2% |
| Under 4.5 | 96.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.46% |
| 2 | 0-0 | 16.26% |
| 3 | 1-1 | 12.06% |
| 4 | 0-1 | 10.43% |
| 5 | 2-0 | 10.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 46.7% | 59.3% | 1.71 | -20.1% |
| Draw | 30.5% | 24.2% | 4.20 | +27.9% |
| FC Schalke 04 win | 22.8% | 16.5% | 6.00 | +36.8% |
| Over 2.5 | 26.1% | 59.1% | 1.69 | -55.8% |
| Under 2.5 | 73.9% | 40.9% | 2.38 | +75.8% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:20:31Z |
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
| P btts yes | 32.8% |
| P btts no | 67.2% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.15 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.12 |
| Fair Over 2.5 odds | 3.83 |
| Fair Under 2.5 odds | 1.35 |
| Fair Over 3.5 odds | 10.35 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.86 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 34.2% |
| Unadjusted draw probability | 36.7% |
| Unadjusted away-win probability | 29.1% |
| Raw p over 1 5 | 52.1% |
| Raw p under 3 5 | 90.6% |
| Raw p btts yes | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.66 |
| Reference draw odds | 3.95 |
| Reference away odds | 5.71 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -12.5% |
| Draw probability edge | +6.3% |
| Away probability edge | +6.3% |
| Over 2.5 probability edge | -33.0% |
| Under 2.5 probability edge | +33.0% |
| Raw edge prob home | -0.2502 |
| Raw ev home | -0.4146 |
| Raw edge prob draw | 0.1251 |
| Raw ev draw | 0.5420 |
| Raw edge prob away | 0.1251 |
| Raw ev away | 0.7432 |
| Market p over 1 5 | 83.8% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Coolbet |
| Market best over 1 5 last update utc | 2026-10-09T15:20:49Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market over 1 5 bookmakers | 4 |
| Market p under 3 5 | 62.8% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T15:20:55Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.51 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 58.0% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T15:20:30Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.28 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-16 — Eintracht Frankfurt vs 1. FC Köln

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **56.4%**. Expected goals are 2.20 for Eintracht Frankfurt and 1.06 for 1. FC Köln (3.26 combined). The most likely exact score is 1-1 at 9.9%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 62.9%; Under 4.5 goals: 77.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 56.4% | 1.77 |
| Draw | 21.5% | 4.66 |
| 1. FC Köln win | 22.1% | 4.52 |

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
| Over 2.5 | 62.9% |
| Under 2.5 | 37.1% |
| Over 3.5 | 40.3% |
| Under 3.5 | 59.7% |
| Over 4.5 | 22.6% |
| Under 4.5 | 77.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.90% |
| 2 | 2-1 | 8.91% |
| 3 | 2-0 | 8.42% |
| 4 | 1-0 | 6.81% |
| 5 | 3-1 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 56.4% | 50.5% | 2.00 | +12.8% |
| Draw | 21.5% | 21.5% | 4.30 | -7.7% |
| 1. FC Köln win | 22.1% | 28.0% | 3.65 | -19.3% |
| Over 2.5 | 62.9% | 69.6% | 1.40 | -12.0% |
| Under 2.5 | 37.1% | 30.4% | 3.00 | +11.4% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
| Odds bookmakers 1x2 | 14.00 |
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
| P btts yes | 59.5% |
| P btts no | 40.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.89 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.30 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.69 |
| Fair Over 3.5 odds | 2.48 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.43 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 62.3% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 16.2% |
| Raw p over 1 5 | 84.6% |
| Raw p under 3 5 | 59.0% |
| Raw p btts yes | 59.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.82 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | +5.9% |
| Draw probability edge | -0.0% |
| Away probability edge | -5.9% |
| Over 2.5 probability edge | -6.7% |
| Under 2.5 probability edge | +6.7% |
| Raw edge prob home | 0.1183 |
| Raw ev home | 0.2465 |
| Raw edge prob draw | -0.0003 |
| Raw ev draw | -0.0776 |
| Raw edge prob away | -0.1180 |
| Raw ev away | -0.4078 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **75.3%**. Expected goals are 2.79 for Bayern Munich and 1.24 for RB Leipzig (4.02 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 78.0%; Under 4.5 goals: 61.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 75.3% | 1.33 |
| Draw | 13.4% | 7.45 |
| RB Leipzig win | 11.3% | 8.82 |

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
| Over 4.5 | 38.8% |
| Under 4.5 | 61.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.36% |
| 2 | 3-1 | 8.69% |
| 3 | 2-0 | 7.57% |
| 4 | 3-0 | 7.03% |
| 5 | 4-1 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 75.3% | 81.4% | 1.27 | -4.4% |
| Draw | 13.4% | 9.7% | 8.20 | +10.0% |
| RB Leipzig win | 11.3% | 8.9% | 11.20 | +26.9% |
| Over 2.5 | 78.0% | 83.6% | 1.18 | -7.9% |
| Under 2.5 | 22.0% | 16.4% | 5.01 | +10.1% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:20:15Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
| Odds bookmakers 1x2 | 13.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Tipico |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Bayern Munich |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.0% |
| P btts no | 34.0% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 52.32 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.60 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.55 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.38 |
| Fair Over 4.5 odds | 2.57 |
| Fair Under 4.5 odds | 1.63 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 13.8% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 42.9% |
| Raw p btts yes | 67.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.18 |
| Reference draw odds | 6.50 |
| Reference away odds | 7.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.17 |
| Reference Under 2.5 odds | 4.90 |
| Home probability edge | -6.1% |
| Draw probability edge | +3.7% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | -0.1227 |
| Raw ev home | -0.1222 |
| Raw edge prob draw | 0.0736 |
| Raw ev draw | 0.4018 |
| Raw edge prob away | 0.0491 |
| Raw ev away | 0.5445 |
| Market p over 1 5 | 95.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-09T15:20:06Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 13.00 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 30.6% |
| Market under 3 5 odds | 2.78 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T15:20:44Z |
| Market reference under 3 5 odds | 2.78 |
| Market reference under 3 5 opposite odds | 1.37 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 70.8% |
| Market btts yes odds | 1.38 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-09T15:19:56Z |
| Market reference btts yes odds | 1.36 |
| Market reference btts yes opposite odds | 3.00 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **56.3%**. Expected goals are 2.96 for Elversberg and 1.17 for Augsburg (4.13 combined). The most likely exact score is 1-1 at 7.7%. Goal-market probabilities: at least one goal: 97.3%; Over 2.5 goals: 75.8%; Under 4.5 goals: 63.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 56.3% | 1.78 |
| Draw | 19.2% | 5.20 |
| Augsburg win | 24.5% | 4.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.96 |
| Augsburg expected goals | 1.17 |
| Expected total goals | 4.13 |
| Over 0.5 | 97.3% |
| Under 0.5 | 2.7% |
| Over 1.5 | 91.3% |
| Under 1.5 | 8.7% |
| Over 2.5 | 75.8% |
| Under 2.5 | 24.2% |
| Over 3.5 | 56.2% |
| Under 3.5 | 43.8% |
| Over 4.5 | 37.0% |
| Under 4.5 | 63.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.65% |
| 2 | 1-2 | 6.99% |
| 3 | 2-1 | 6.35% |
| 4 | 3-1 | 6.26% |
| 5 | 2-2 | 5.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 56.3% | 39.5% | 2.55 | +43.6% |
| Draw | 19.2% | 23.0% | 4.00 | -23.0% |
| Augsburg win | 24.5% | 37.5% | 2.80 | -31.5% |
| Over 2.5 | 75.8% | 66.1% | 1.47 | +11.4% |
| Under 2.5 | 24.2% | 33.9% | 2.71 | -34.4% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
| Odds bookmakers 1x2 | 14.00 |
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
| Fair Under 0.5 odds | 36.66 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.43 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.13 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.28 |
| Fair Over 4.5 odds | 2.70 |
| Fair Under 4.5 odds | 1.59 |
| Unadjusted home-win probability | 73.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.9% |
| Raw p btts yes | 65.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.25 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.35 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.68 |
| Home probability edge | +16.9% |
| Draw probability edge | -3.8% |
| Away probability edge | -13.1% |
| Over 2.5 probability edge | +9.7% |
| Under 2.5 probability edge | -9.7% |
| Raw edge prob home | 0.3370 |
| Raw ev home | 0.8655 |
| Raw edge prob draw | -0.0755 |
| Raw ev draw | -0.3813 |
| Raw edge prob away | -0.2616 |
| Raw ev away | -0.6814 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T15:20:28Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 55.3% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T15:15:45Z |
| Market reference under 3 5 odds | 1.74 |
| Market reference under 3 5 opposite odds | 2.12 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T15:20:28Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.80 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FC Schalke 04 win** at **35.0%**. Expected goals are 0.87 for FC Schalke 04 and 0.69 for FSV Mainz 05 (1.56 combined). The most likely exact score is 0-0 at 18.3%. Goal-market probabilities: at least one goal: 81.7%; Over 2.5 goals: 22.3%; Under 4.5 goals: 97.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 35.0% | 2.86 |
| Draw | 31.3% | 3.19 |
| FSV Mainz 05 win | 33.6% | 2.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| FSV Mainz 05 expected goals | 0.69 |
| Expected total goals | 1.56 |
| Over 0.5 | 81.7% |
| Under 0.5 | 18.3% |
| Over 1.5 | 47.9% |
| Under 1.5 | 52.1% |
| Over 2.5 | 22.3% |
| Under 2.5 | 77.7% |
| Over 3.5 | 7.5% |
| Under 3.5 | 92.5% |
| Over 4.5 | 2.3% |
| Under 4.5 | 97.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.29% |
| 2 | 0-1 | 17.32% |
| 3 | 1-0 | 16.45% |
| 4 | 1-1 | 11.40% |
| 5 | 2-0 | 7.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 35.0% | 33.7% | 3.05 | +6.8% |
| Draw | 31.3% | 24.4% | 3.80 | +19.1% |
| FSV Mainz 05 win | 33.6% | 41.9% | 2.44 | -17.9% |
| Over 2.5 | 22.3% | 59.8% | 1.66 | -63.0% |
| Under 2.5 | 77.7% | 40.2% | 2.42 | +88.1% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
| Odds bookmakers 1x2 | 14.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Schalke 04 |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 29.0% |
| P btts no | 71.0% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.47 |
| Fair Over 1.5 odds | 2.09 |
| Fair Under 1.5 odds | 1.92 |
| Fair Over 2.5 odds | 4.49 |
| Fair Under 2.5 odds | 1.29 |
| Fair Over 3.5 odds | 13.36 |
| Fair Under 3.5 odds | 1.08 |
| Fair Over 4.5 odds | 42.85 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 36.3% |
| Unadjusted draw probability | 38.3% |
| Unadjusted away-win probability | 25.4% |
| Raw p over 1 5 | 47.5% |
| Raw p under 3 5 | 92.7% |
| Raw p btts yes | 30.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +1.3% |
| Draw probability edge | +6.9% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | -37.5% |
| Under 2.5 probability edge | +37.5% |
| Raw edge prob home | 0.0258 |
| Raw ev home | 0.1070 |
| Raw edge prob draw | 0.1383 |
| Raw ev draw | 0.4539 |
| Raw edge prob away | -0.1641 |
| Raw ev away | -0.3791 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T15:20:28Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 61.8% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T15:20:44Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.43 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T15:20:28Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **55.6%**. Expected goals are 1.11 for Hamburger SV and 2.02 for VfB Stuttgart (3.13 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 60.8%; Under 4.5 goals: 79.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 22.2% | 4.50 |
| Draw | 22.2% | 4.50 |
| VfB Stuttgart win | 55.6% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.11 |
| VfB Stuttgart expected goals | 2.02 |
| Expected total goals | 3.13 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 60.8% |
| Under 2.5 | 39.2% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.8% |
| Under 4.5 | 79.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.32% |
| 2 | 1-2 | 9.59% |
| 3 | 0-2 | 8.64% |
| 4 | 0-1 | 7.57% |
| 5 | 1-3 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 22.2% | 25.1% | 4.20 | -6.6% |
| Draw | 22.2% | 21.1% | 4.40 | -2.3% |
| VfB Stuttgart win | 55.6% | 53.8% | 1.90 | +5.6% |
| Over 2.5 | 60.8% | 70.7% | 1.38 | -16.1% |
| Under 2.5 | 39.2% | 29.3% | 3.10 | +21.4% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
| Odds bookmakers 1x2 | 14.00 |
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
| Fair Under 0.5 odds | 19.44 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.84 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
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
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.35 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.72 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | -2.9% |
| Draw probability edge | +1.1% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | -0.0575 |
| Raw ev home | -0.1869 |
| Raw edge prob draw | 0.0221 |
| Raw ev draw | 0.0257 |
| Raw edge prob away | 0.0353 |
| Raw ev away | 0.0893 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **60.0%**. Expected goals are 0.94 for Union Berlin and 1.92 for Borussia Dortmund (2.87 combined). The most likely exact score is 0-2 at 10.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 55.2%; Under 4.5 goals: 83.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.7% | 5.66 |
| Draw | 22.3% | 4.48 |
| Borussia Dortmund win | 60.0% | 1.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.92 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
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
| 1 | 0-2 | 10.67% |
| 2 | 1-1 | 10.64% |
| 3 | 1-2 | 10.04% |
| 4 | 0-1 | 10.00% |
| 5 | 0-3 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.7% | 18.5% | 5.40 | -4.5% |
| Draw | 22.3% | 20.7% | 4.50 | +0.4% |
| Borussia Dortmund win | 60.0% | 60.7% | 1.73 | +3.8% |
| Over 2.5 | 55.2% | 65.4% | 1.49 | -17.8% |
| Under 2.5 | 44.8% | 34.6% | 2.70 | +21.0% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:20:15Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Tipico |
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
| Fair Under 0.5 odds | 15.80 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.30 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.54 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -0.9% |
| Draw probability edge | +1.6% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -10.2% |
| Under 2.5 probability edge | +10.2% |
| Raw edge prob home | -0.0171 |
| Raw ev home | -0.0916 |
| Raw edge prob draw | 0.0314 |
| Raw ev draw | 0.0751 |
| Raw edge prob away | -0.0143 |
| Raw ev away | 0.0257 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **49.5%**. Expected goals are 1.16 for Werder Bremen and 0.74 for SC Paderborn (1.91 combined). The most likely exact score is 1-0 at 17.8%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 31.6%; Under 4.5 goals: 95.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 49.5% | 2.02 |
| Draw | 27.7% | 3.61 |
| SC Paderborn win | 22.8% | 4.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.16 |
| SC Paderborn expected goals | 0.74 |
| Expected total goals | 1.91 |
| Over 0.5 | 86.6% |
| Under 0.5 | 13.4% |
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
| 1 | 1-0 | 17.77% |
| 2 | 0-0 | 13.45% |
| 3 | 1-1 | 11.76% |
| 4 | 2-0 | 11.22% |
| 5 | 0-1 | 9.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 49.5% | 54.5% | 1.91 | -5.5% |
| Draw | 27.7% | 22.0% | 4.26 | +18.2% |
| SC Paderborn win | 22.8% | 23.5% | 4.25 | -3.2% |
| Over 2.5 | 31.6% | 62.7% | 1.56 | -50.7% |
| Under 2.5 | 68.4% | 37.3% | 2.47 | +68.9% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:20:29Z |
| Odds bookmakers 1x2 | 14.00 |
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
| P btts yes | 36.1% |
| P btts no | 63.9% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.44 |
| Fair Over 1.5 odds | 1.70 |
| Fair Under 1.5 odds | 2.43 |
| Fair Over 2.5 odds | 3.16 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.70 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.90 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 44.5% |
| Unadjusted draw probability | 33.4% |
| Unadjusted away-win probability | 22.1% |
| Raw p over 1 5 | 58.1% |
| Raw p under 3 5 | 87.4% |
| Raw p btts yes | 37.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.70 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.55 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | -5.0% |
| Draw probability edge | +5.7% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -31.1% |
| Under 2.5 probability edge | +31.1% |
| Raw edge prob home | -0.0999 |
| Raw ev home | -0.1500 |
| Raw edge prob draw | 0.1139 |
| Raw ev draw | 0.4242 |
| Raw edge prob away | -0.0140 |
| Raw ev away | -0.0621 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **64.1%**. Expected goals are 2.44 for Bayer Leverkusen and 0.96 for SC Freiburg (3.41 combined). The most likely exact score is 2-0 at 9.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 65.5%; Under 4.5 goals: 74.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 64.1% | 1.56 |
| Draw | 19.5% | 5.12 |
| SC Freiburg win | 16.4% | 6.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.44 |
| SC Freiburg expected goals | 0.96 |
| Expected total goals | 3.41 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 85.7% |
| Under 1.5 | 14.3% |
| Over 2.5 | 65.5% |
| Under 2.5 | 34.5% |
| Over 3.5 | 43.4% |
| Under 3.5 | 56.6% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.19% |
| 2 | 1-1 | 8.98% |
| 3 | 2-1 | 8.85% |
| 4 | 3-0 | 7.48% |
| 5 | 3-1 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 64.1% | 59.1% | 1.70 | +8.9% |
| Draw | 19.5% | 20.3% | 4.60 | -10.2% |
| SC Freiburg win | 16.4% | 20.6% | 4.83 | -20.8% |
| Over 2.5 | 65.5% | 65.4% | 1.49 | -2.4% |
| Under 2.5 | 34.5% | 34.6% | 2.67 | -7.8% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:20:15Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
| Odds bookmakers 1x2 | 14.00 |
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
| P btts yes | 58.0% |
| P btts no | 42.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.22 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.00 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.98 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.7% |
| Raw p btts yes | 57.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.95 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | +5.0% |
| Draw probability edge | -0.8% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.0998 |
| Raw ev home | 0.1743 |
| Raw edge prob draw | -0.0157 |
| Raw ev draw | -0.1381 |
| Raw edge prob away | -0.0842 |
| Raw ev away | -0.4114 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **42.6%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-2 at 9.0%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 72.1%; Under 4.5 goals: 68.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 34.9% | 2.87 |
| Draw | 22.5% | 4.45 |
| TSG Hoffenheim win | 42.6% | 2.34 |

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
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 51.1% |
| Under 3.5 | 48.9% |
| Over 4.5 | 31.9% |
| Under 4.5 | 68.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.98% |
| 2 | 1-1 | 8.93% |
| 3 | 2-2 | 7.00% |
| 4 | 2-1 | 6.83% |
| 5 | 1-3 | 5.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 34.9% | 28.5% | 3.58 | +24.9% |
| Draw | 22.5% | 21.7% | 4.26 | -4.3% |
| TSG Hoffenheim win | 42.6% | 49.8% | 2.00 | -14.7% |
| Over 2.5 | 72.1% | 69.6% | 1.40 | +0.9% |
| Under 2.5 | 27.9% | 30.4% | 3.00 | -16.3% |

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
| Market best home last update utc | 2026-10-09T15:19:56Z |
| Market best draw last update utc | 2026-10-09T15:19:56Z |
| Market best away last update utc | 2026-10-09T15:19:56Z |
| Odds bookmakers 1x2 | 14.00 |
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
| P btts yes | 72.1% |
| P btts no | 27.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.48 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.51 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.59 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.14 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 41.3% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.9% |
| Raw p btts yes | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.84 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | +6.4% |
| Draw probability edge | +0.7% |
| Away probability edge | -7.1% |
| Over 2.5 probability edge | +2.5% |
| Under 2.5 probability edge | -2.5% |
| Raw edge prob home | 0.1281 |
| Raw ev home | 0.4780 |
| Raw edge prob draw | 0.0148 |
| Raw ev draw | -0.0111 |
| Raw edge prob away | -0.1429 |
| Raw ev away | -0.2899 |

</details>


---
