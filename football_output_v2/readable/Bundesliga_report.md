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
| Goal market reliability | {'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-09 — Borussia Dortmund vs Werder Bremen

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **69.3%**. Expected goals are 2.30 for Borussia Dortmund and 0.97 for Werder Bremen (3.27 combined). The most likely exact score is 2-0 at 10.5%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 64.4%; Under 4.5 goals: 76.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 69.3% | 1.44 |
| Draw | 18.4% | 5.44 |
| Werder Bremen win | 12.3% | 8.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.30 |
| Werder Bremen expected goals | 0.97 |
| Expected total goals | 3.27 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 64.4% |
| Under 2.5 | 35.6% |
| Over 3.5 | 41.9% |
| Under 3.5 | 58.1% |
| Over 4.5 | 23.7% |
| Under 4.5 | 76.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.48% |
| 2 | 2-1 | 10.18% |
| 3 | 1-1 | 8.54% |
| 4 | 1-0 | 8.18% |
| 5 | 3-0 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 69.3% | 72.2% | 1.38 | -4.4% |
| Draw | 18.4% | 16.7% | 6.25 | +14.9% |
| Werder Bremen win | 12.3% | 11.1% | 9.00 | +11.0% |
| Over 2.5 | 64.4% | 70.7% | 1.38 | -11.2% |
| Under 2.5 | 35.6% | 29.3% | 3.20 | +14.1% |

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
| Market best home last update utc | 2026-10-09T13:49:06Z |
| Market best draw last update utc | 2026-10-09T13:48:19Z |
| Market best away last update utc | 2026-10-09T13:48:19Z |
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
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.43 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.67 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.39 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.21 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 66.4% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 13.5% |
| Raw p over 1 5 | 84.7% |
| Raw p under 3 5 | 58.6% |
| Raw p btts yes | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.38 |
| Reference draw odds | 5.90 |
| Reference away odds | 8.80 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | -2.9% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | -0.0588 |
| Raw ev home | -0.0843 |
| Raw edge prob draw | 0.0345 |
| Raw ev draw | 0.2565 |
| Raw edge prob away | 0.0242 |
| Raw ev away | 0.2187 |

</details>


---

## 2026-10-10 — Augsburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **78.8%**. Expected goals are 1.04 for Augsburg and 2.87 for Bayern Munich (3.92 combined). The most likely exact score is 1-2 at 9.1%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 76.3%; Under 4.5 goals: 63.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 8.6% | 11.62 |
| Draw | 12.6% | 7.91 |
| Bayern Munich win | 78.8% | 1.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.04 |
| Bayern Munich expected goals | 2.87 |
| Expected total goals | 3.92 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 76.3% |
| Under 2.5 | 23.7% |
| Over 3.5 | 55.9% |
| Under 3.5 | 44.1% |
| Over 4.5 | 36.5% |
| Under 4.5 | 63.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.09% |
| 2 | 1-3 | 8.71% |
| 3 | 0-2 | 8.70% |
| 4 | 0-3 | 8.34% |
| 5 | 1-4 | 6.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 8.6% | 7.0% | 14.50 | +24.7% |
| Draw | 12.6% | 9.8% | 10.00 | +26.5% |
| Bayern Munich win | 78.8% | 83.2% | 1.23 | -3.1% |
| Over 2.5 | 76.3% | 85.9% | 1.15 | -12.3% |
| Under 2.5 | 23.7% | 14.1% | 5.55 | +31.8% |

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
| Market best home last update utc | 2026-10-09T13:48:50Z |
| Market best draw last update utc | 2026-10-09T13:49:06Z |
| Market best away last update utc | 2026-10-09T13:48:51Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Augsburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.90 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.43 |
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
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 14.00 |
| Reference draw odds | 10.00 |
| Reference away odds | 1.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.40 |
| Home probability edge | +1.6% |
| Draw probability edge | +2.8% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | 0.0323 |
| Raw ev home | 0.4818 |
| Raw edge prob draw | 0.0567 |
| Raw ev draw | 0.5482 |
| Raw edge prob away | -0.0891 |
| Raw ev away | -0.0861 |
| Market p over 1 5 | 95.8% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-09T13:47:59Z |
| Market reference over 1 5 odds | 1.03 |
| Market reference over 1 5 opposite odds | 8.60 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 30.0% |
| Market under 3 5 odds | 3.03 |
| Best under 3 5 bookmaker | Coolbet |
| Market best under 3 5 last update utc | 2026-10-09T13:49:07Z |
| Market reference under 3 5 odds | 3.03 |
| Market reference under 3 5 opposite odds | 1.39 |
| Market under 3 5 bookmakers | 4 |
| Market p btts yes | 65.3% |
| Market btts yes odds | 1.52 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T13:49:08Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.82 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-10 — FSV Mainz 05 vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **48.8%**. Expected goals are 1.08 for FSV Mainz 05 and 1.81 for Bayer Leverkusen (2.89 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 55.2%; Under 4.5 goals: 83.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 26.4% | 3.79 |
| Draw | 24.8% | 4.04 |
| Bayer Leverkusen win | 48.8% | 2.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.08 |
| Bayer Leverkusen expected goals | 1.81 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
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
| 1 | 1-1 | 11.74% |
| 2 | 1-2 | 8.97% |
| 3 | 0-2 | 8.34% |
| 4 | 0-1 | 8.16% |
| 5 | 2-1 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 26.4% | 31.6% | 3.15 | -16.8% |
| Draw | 24.8% | 24.3% | 4.10 | +1.5% |
| Bayer Leverkusen win | 48.8% | 44.1% | 2.31 | +12.8% |
| Over 2.5 | 55.2% | 67.7% | 1.44 | -20.6% |
| Under 2.5 | 44.8% | 32.3% | 2.84 | +27.3% |

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
| Market best home last update utc | 2026-10-09T13:49:06Z |
| Market best draw last update utc | 2026-10-09T13:48:19Z |
| Market best away last update utc | 2026-10-09T13:47:13Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Mainz |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.25 |
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
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 3.15 |
| Reference draw odds | 4.10 |
| Reference away odds | 2.26 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.82 |
| Home probability edge | -5.2% |
| Draw probability edge | +0.5% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -12.5% |
| Under 2.5 probability edge | +12.5% |
| Raw edge prob home | -0.1042 |
| Raw ev home | -0.3323 |
| Raw edge prob draw | 0.0099 |
| Raw ev draw | 0.0354 |
| Raw edge prob away | 0.0943 |
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
| Draw | 21.0% | 4.76 |
| Eintracht Frankfurt win | 21.0% | 4.77 |

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
| 2 | 1-1 | 9.10% |
| 3 | 2-0 | 7.47% |
| 4 | 3-1 | 7.14% |
| 5 | 1-0 | 6.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 58.0% | 61.5% | 1.62 | -6.0% |
| Draw | 21.0% | 19.4% | 5.10 | +7.1% |
| Eintracht Frankfurt win | 21.0% | 19.0% | 5.30 | +11.2% |
| Over 2.5 | 68.2% | 75.4% | 1.30 | -11.4% |
| Under 2.5 | 31.8% | 24.6% | 3.60 | +14.6% |

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
| Market best home last update utc | 2026-10-09T13:47:13Z |
| Market best draw last update utc | 2026-10-09T13:49:02Z |
| Market best away last update utc | 2026-10-09T13:48:19Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 81/100 |
| P btts yes | 65.7% |
| P btts no | 34.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.81 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.87 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.14 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.64 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 54.5% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 22.9% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 54.1% |
| Raw p btts yes | 66.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.62 |
| Reference draw odds | 5.10 |
| Reference away odds | 5.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.55 |
| Home probability edge | -3.5% |
| Draw probability edge | +1.6% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.0704 |
| Raw ev home | -0.1170 |
| Raw edge prob draw | 0.0317 |
| Raw ev draw | 0.1520 |
| Raw edge prob away | 0.0387 |
| Raw ev away | 0.2140 |

</details>


---

## 2026-10-10 — SC Paderborn vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **56.0%**. Expected goals are 0.76 for SC Paderborn and 1.42 for VfB Stuttgart (2.18 combined). The most likely exact score is 0-1 at 16.1%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 38.9%; Under 4.5 goals: 92.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 18.7% | 5.33 |
| Draw | 25.2% | 3.96 |
| VfB Stuttgart win | 56.0% | 1.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.76 |
| VfB Stuttgart expected goals | 1.42 |
| Expected total goals | 2.18 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 66.0% |
| Under 1.5 | 34.0% |
| Over 2.5 | 38.9% |
| Under 2.5 | 61.1% |
| Over 3.5 | 18.1% |
| Under 3.5 | 81.9% |
| Over 4.5 | 7.4% |
| Under 4.5 | 92.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.06% |
| 2 | 0-2 | 12.41% |
| 3 | 1-1 | 11.42% |
| 4 | 0-0 | 10.65% |
| 5 | 1-2 | 9.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 18.7% | 18.8% | 5.30 | -0.7% |
| Draw | 25.2% | 20.7% | 4.85 | +22.3% |
| VfB Stuttgart win | 56.0% | 60.5% | 1.65 | -7.6% |
| Over 2.5 | 38.9% | 72.4% | 1.35 | -47.5% |
| Under 2.5 | 61.1% | 27.6% | 3.26 | +99.2% |

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
| Market best home last update utc | 2026-10-09T13:49:06Z |
| Market best draw last update utc | 2026-10-09T13:49:06Z |
| Market best away last update utc | 2026-10-09T13:49:06Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Paderborn |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 40.6% |
| P btts no | 59.4% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.39 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.52 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.43 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 18.7% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 51.6% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 41.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 5.30 |
| Reference draw odds | 4.80 |
| Reference away odds | 1.65 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.20 |
| Home probability edge | -0.0% |
| Draw probability edge | +4.5% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | -33.5% |
| Under 2.5 probability edge | +33.5% |
| Raw edge prob home | -0.0004 |
| Raw ev home | -0.0077 |
| Raw edge prob draw | 0.0900 |
| Raw ev draw | 0.4417 |
| Raw edge prob away | -0.0896 |
| Raw ev away | -0.1494 |

</details>


---

## 2026-10-10 — TSG Hoffenheim vs Hamburger SV

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **62.5%**. Expected goals are 2.09 for TSG Hoffenheim and 1.21 for Hamburger SV (3.30 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 65.1%; Under 4.5 goals: 75.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 62.5% | 1.60 |
| Draw | 20.6% | 4.85 |
| Hamburger SV win | 16.8% | 5.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 2.09 |
| Hamburger SV expected goals | 1.21 |
| Expected total goals | 3.30 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 65.1% |
| Under 2.5 | 34.9% |
| Over 3.5 | 42.6% |
| Under 3.5 | 57.4% |
| Over 4.5 | 24.4% |
| Under 4.5 | 75.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.76% |
| 2 | 1-1 | 9.31% |
| 3 | 2-0 | 8.89% |
| 4 | 3-1 | 7.50% |
| 5 | 1-0 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 62.5% | 68.4% | 1.49 | -6.8% |
| Draw | 20.6% | 18.5% | 5.40 | +11.4% |
| Hamburger SV win | 16.8% | 13.1% | 7.60 | +28.0% |
| Over 2.5 | 65.1% | 69.6% | 1.40 | -8.9% |
| Under 2.5 | 34.9% | 30.4% | 3.00 | +4.7% |

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
| Market best home last update utc | 2026-10-09T13:47:13Z |
| Market best draw last update utc | 2026-10-09T13:48:19Z |
| Market best away last update utc | 2026-10-09T13:49:06Z |
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
| P btts yes | 61.7% |
| P btts no | 38.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.75 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.90 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.87 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.09 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 56.6% |
| Unadjusted draw probability | 22.8% |
| Unadjusted away-win probability | 20.6% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 58.0% |
| Raw p btts yes | 62.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.46 |
| Reference draw odds | 5.40 |
| Reference away odds | 7.60 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | -5.9% |
| Draw probability edge | +2.2% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -4.5% |
| Under 2.5 probability edge | +4.5% |
| Raw edge prob home | -0.1181 |
| Raw ev home | -0.1562 |
| Raw edge prob draw | 0.0434 |
| Raw ev draw | 0.2310 |
| Raw edge prob away | 0.0747 |
| Raw ev away | 0.5637 |

</details>


---

## 2026-10-10 — Union Berlin vs Elversberg

The model's most likely 1X2 outcome is **Elversberg win** at **49.7%**. Expected goals are 1.17 for Union Berlin and 2.48 for Elversberg (3.65 combined). The most likely exact score is 1-1 at 9.7%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 68.7%; Under 4.5 goals: 71.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 27.9% | 3.58 |
| Draw | 22.4% | 4.47 |
| Elversberg win | 49.7% | 2.01 |

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
| 1 | 1-1 | 9.67% |
| 2 | 2-1 | 7.98% |
| 3 | 1-2 | 7.12% |
| 4 | 2-2 | 6.33% |
| 5 | 0-2 | 6.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 27.9% | 40.5% | 2.46 | -31.3% |
| Draw | 22.4% | 25.5% | 3.90 | -12.7% |
| Elversberg win | 49.7% | 34.1% | 2.92 | +45.1% |
| Over 2.5 | 68.7% | 62.7% | 1.54 | +5.7% |
| Under 2.5 | 31.3% | 37.3% | 2.56 | -19.8% |

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
| Market best home last update utc | 2026-10-09T13:49:06Z |
| Market best draw last update utc | 2026-10-09T13:47:13Z |
| Market best away last update utc | 2026-10-09T13:49:06Z |
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
| Fair Under 0.5 odds | 25.39 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.10 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.19 |
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
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 2.46 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.92 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | -12.5% |
| Draw probability edge | -3.1% |
| Away probability edge | +15.6% |
| Over 2.5 probability edge | +6.0% |
| Under 2.5 probability edge | -6.0% |
| Raw edge prob home | -0.2506 |
| Raw ev home | -0.6210 |
| Raw edge prob draw | -0.0617 |
| Raw ev draw | -0.2475 |
| Raw edge prob away | 0.3123 |
| Raw ev away | 0.9067 |

</details>


---

## 2026-10-11 — 1. FC Köln vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **1. FC Köln win** at **40.4%**. Expected goals are 1.43 for 1. FC Köln and 1.55 for Borussia Monchengladbach (2.97 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.4%; Under 4.5 goals: 81.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 40.4% | 2.48 |
| Draw | 25.7% | 3.90 |
| Borussia Monchengladbach win | 34.0% | 2.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.43 |
| Borussia Monchengladbach expected goals | 1.55 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 57.4% |
| Under 2.5 | 42.6% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.2% |
| Under 4.5 | 81.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.97% |
| 2 | 2-1 | 9.56% |
| 3 | 1-2 | 7.54% |
| 4 | 1-0 | 7.26% |
| 5 | 2-0 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 40.4% | 46.8% | 2.13 | -14.1% |
| Draw | 25.7% | 24.6% | 4.15 | +6.5% |
| Borussia Monchengladbach win | 34.0% | 28.6% | 3.45 | +17.2% |
| Over 2.5 | 57.4% | 64.6% | 1.51 | -13.3% |
| Under 2.5 | 42.6% | 35.4% | 2.61 | +11.1% |

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
| Market best home last update utc | 2026-10-09T13:49:06Z |
| Market best draw last update utc | 2026-10-09T13:47:13Z |
| Market best away last update utc | 2026-10-09T13:49:06Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Koln |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.56 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.23 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.51 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 33.9% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 39.4% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 61.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 2.12 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.45 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Home probability edge | -6.4% |
| Draw probability edge | +1.1% |
| Away probability edge | +5.4% |
| Over 2.5 probability edge | -7.2% |
| Under 2.5 probability edge | +7.2% |
| Raw edge prob home | -0.1286 |
| Raw ev home | -0.2775 |
| Raw edge prob draw | 0.0210 |
| Raw ev draw | 0.1091 |
| Raw edge prob away | 0.1076 |
| Raw ev away | 0.3578 |

</details>


---

## 2026-10-11 — SC Freiburg vs FC Schalke 04

The model's most likely 1X2 outcome is **SC Freiburg win** at **47.0%**. Expected goals are 0.90 for SC Freiburg and 0.80 for FC Schalke 04 (1.70 combined). The most likely exact score is 1-0 at 20.6%. Goal-market probabilities: at least one goal: 83.9%; Over 2.5 goals: 26.2%; Under 4.5 goals: 96.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 47.0% | 2.13 |
| Draw | 30.1% | 3.32 |
| FC Schalke 04 win | 22.9% | 4.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 0.90 |
| FC Schalke 04 expected goals | 0.80 |
| Expected total goals | 1.70 |
| Over 0.5 | 83.9% |
| Under 0.5 | 16.1% |
| Over 1.5 | 52.9% |
| Under 1.5 | 47.1% |
| Over 2.5 | 26.2% |
| Under 2.5 | 73.8% |
| Over 3.5 | 9.7% |
| Under 3.5 | 90.3% |
| Over 4.5 | 3.3% |
| Under 4.5 | 96.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.55% |
| 2 | 0-0 | 16.09% |
| 3 | 1-1 | 11.94% |
| 4 | 0-1 | 10.48% |
| 5 | 2-0 | 10.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 47.0% | 59.7% | 1.71 | -19.7% |
| Draw | 30.1% | 23.6% | 4.20 | +26.6% |
| FC Schalke 04 win | 22.9% | 16.7% | 5.90 | +35.1% |
| Over 2.5 | 26.2% | 59.0% | 1.69 | -55.7% |
| Under 2.5 | 73.8% | 41.0% | 2.38 | +75.6% |

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
| Market best home last update utc | 2026-10-09T13:47:13Z |
| Market best draw last update utc | 2026-10-09T13:48:19Z |
| Market best away last update utc | 2026-10-09T13:49:06Z |
| Odds bookmakers 1x2 | 20.00 |
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
| Fair Under 0.5 odds | 6.21 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.12 |
| Fair Over 2.5 odds | 3.81 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 10.33 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.75 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 34.2% |
| Unadjusted draw probability | 36.7% |
| Unadjusted away-win probability | 29.1% |
| Raw p over 1 5 | 52.1% |
| Raw p under 3 5 | 90.6% |
| Raw p btts yes | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.67 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.90 |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -12.7% |
| Draw probability edge | +6.6% |
| Away probability edge | +6.2% |
| Over 2.5 probability edge | -32.8% |
| Under 2.5 probability edge | +32.8% |
| Raw edge prob home | -0.2544 |
| Raw ev home | -0.4146 |
| Raw edge prob draw | 0.1314 |
| Raw ev draw | 0.5420 |
| Raw edge prob away | 0.1231 |
| Raw ev away | 0.7141 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T13:48:18Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market over 1 5 bookmakers | 3 |
| Market p under 3 5 | 63.9% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T13:46:16Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market under 3 5 bookmakers | 3 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | Matchbook |
| Market best btts yes last update utc | 2026-10-09T13:49:08Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.30 |
| Market btts yes bookmakers | 4 |

</details>


---

## 2026-10-16 — Eintracht Frankfurt vs 1. FC Köln

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **56.9%**. Expected goals are 2.20 for Eintracht Frankfurt and 1.06 for 1. FC Köln (3.26 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 62.7%; Under 4.5 goals: 77.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 56.9% | 1.76 |
| Draw | 21.9% | 4.58 |
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
| Over 2.5 | 62.7% |
| Under 2.5 | 37.3% |
| Over 3.5 | 40.3% |
| Under 3.5 | 59.7% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.08% |
| 2 | 2-1 | 8.99% |
| 3 | 2-0 | 8.50% |
| 4 | 1-0 | 6.87% |
| 5 | 3-1 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 56.9% | 51.5% | 2.00 | +13.8% |
| Draw | 21.9% | 22.3% | 4.30 | -6.0% |
| 1. FC Köln win | 21.3% | 26.3% | 3.65 | -22.4% |
| Over 2.5 | 62.7% | 69.6% | 1.40 | -12.2% |
| Under 2.5 | 37.3% | 30.4% | 3.00 | +11.8% |

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
| Market best home last update utc | 2026-10-09T13:47:13Z |
| Market best draw last update utc | 2026-10-09T13:47:13Z |
| Market best away last update utc | 2026-10-09T13:48:19Z |
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
| Fair Under 0.5 odds | 20.52 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.31 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.48 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.44 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 62.3% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 16.2% |
| Raw p over 1 5 | 84.6% |
| Raw p under 3 5 | 59.0% |
| Raw p btts yes | 59.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.88 |
| Reference draw odds | 4.17 |
| Reference away odds | 3.56 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | +5.4% |
| Draw probability edge | -0.4% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
| Raw edge prob home | 0.1086 |
| Raw ev home | 0.2465 |
| Raw edge prob draw | -0.0080 |
| Raw ev draw | -0.0776 |
| Raw edge prob away | -0.1006 |
| Raw ev away | -0.4078 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **73.6%**. Expected goals are 2.79 for Bayern Munich and 1.24 for RB Leipzig (4.02 combined). The most likely exact score is 2-1 at 9.2%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 77.3%; Under 4.5 goals: 61.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 73.6% | 1.36 |
| Draw | 15.4% | 6.49 |
| RB Leipzig win | 11.0% | 9.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.79 |
| RB Leipzig expected goals | 1.24 |
| Expected total goals | 4.02 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 91.9% |
| Under 1.5 | 8.1% |
| Over 2.5 | 77.3% |
| Under 2.5 | 22.7% |
| Over 3.5 | 57.8% |
| Under 3.5 | 42.2% |
| Over 4.5 | 38.3% |
| Under 4.5 | 61.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.15% |
| 2 | 3-1 | 8.50% |
| 3 | 2-0 | 7.41% |
| 4 | 3-0 | 6.88% |
| 5 | 1-1 | 6.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 73.6% | 78.1% | 1.27 | -6.5% |
| Draw | 15.4% | 13.7% | 8.00 | +23.2% |
| RB Leipzig win | 11.0% | 8.2% | 11.20 | +23.3% |
| Over 2.5 | 77.3% | 83.6% | 1.18 | -8.8% |
| Under 2.5 | 22.7% | 16.4% | 5.01 | +13.8% |

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
| Market best home last update utc | 2026-10-09T13:47:13Z |
| Market best draw last update utc | 2026-10-09T13:48:34Z |
| Market best away last update utc | 2026-10-09T13:47:13Z |
| Odds bookmakers 1x2 | 14.00 |
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
| P btts yes | 66.5% |
| P btts no | 33.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.58 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.38 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.40 |
| Fair Over 3.5 odds | 1.73 |
| Fair Under 3.5 odds | 2.37 |
| Fair Over 4.5 odds | 2.61 |
| Fair Under 4.5 odds | 1.62 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 13.8% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 42.9% |
| Raw p btts yes | 67.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 888sport |
| Reference home odds | 1.25 |
| Reference draw odds | 6.00 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.17 |
| Reference Under 2.5 odds | 4.90 |
| Home probability edge | -4.5% |
| Draw probability edge | +1.7% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.0896 |
| Raw ev home | -0.1222 |
| Raw edge prob draw | 0.0339 |
| Raw ev draw | 0.3676 |
| Raw edge prob away | 0.0556 |
| Raw ev away | 0.5445 |
| Market p over 1 5 | 95.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-09T13:47:58Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 13.00 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 30.6% |
| Market under 3 5 odds | 2.78 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T13:49:06Z |
| Market reference under 3 5 odds | 2.78 |
| Market reference under 3 5 opposite odds | 1.37 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 70.8% |
| Market btts yes odds | 1.38 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-09T13:47:13Z |
| Market reference btts yes odds | 1.36 |
| Market reference btts yes opposite odds | 3.00 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **55.8%**. Expected goals are 2.96 for Elversberg and 1.17 for Augsburg (4.13 combined). The most likely exact score is 1-1 at 8.2%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 75.3%; Under 4.5 goals: 63.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 55.8% | 1.79 |
| Draw | 20.6% | 4.86 |
| Augsburg win | 23.7% | 4.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.96 |
| Augsburg expected goals | 1.17 |
| Expected total goals | 4.13 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 75.3% |
| Under 2.5 | 24.7% |
| Over 3.5 | 56.1% |
| Under 3.5 | 43.9% |
| Over 4.5 | 36.7% |
| Under 4.5 | 63.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.18% |
| 2 | 1-2 | 6.76% |
| 3 | 2-2 | 6.40% |
| 4 | 2-1 | 6.29% |
| 5 | 3-1 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 55.8% | 38.4% | 2.55 | +42.2% |
| Draw | 20.6% | 25.7% | 4.00 | -17.7% |
| Augsburg win | 23.7% | 36.0% | 2.80 | -33.7% |
| Over 2.5 | 75.3% | 66.1% | 1.47 | +10.7% |
| Under 2.5 | 24.7% | 33.9% | 2.71 | -33.2% |

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
| Market best home last update utc | 2026-10-09T13:47:13Z |
| Market best draw last update utc | 2026-10-09T13:48:19Z |
| Market best away last update utc | 2026-10-09T13:48:19Z |
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
| P btts yes | 68.8% |
| P btts no | 31.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.28 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.34 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 4.05 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.28 |
| Fair Over 4.5 odds | 2.73 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 73.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.9% |
| Raw p btts yes | 65.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.50 |
| Reference draw odds | 3.67 |
| Reference away odds | 2.66 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.68 |
| Home probability edge | +17.4% |
| Draw probability edge | -5.1% |
| Away probability edge | -12.3% |
| Over 2.5 probability edge | +9.3% |
| Under 2.5 probability edge | -9.3% |
| Raw edge prob home | 0.3479 |
| Raw ev home | 0.8655 |
| Raw edge prob draw | -0.1021 |
| Raw ev draw | -0.3813 |
| Raw edge prob away | -0.2458 |
| Raw ev away | -0.6814 |
| Market p over 1 5 | 91.0% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T13:48:18Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 5.70 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 55.3% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-09T13:48:20Z |
| Market reference under 3 5 odds | 1.74 |
| Market reference under 3 5 opposite odds | 2.12 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.40 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T13:48:18Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.80 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FC Schalke 04 win** at **34.8%**. Expected goals are 0.87 for FC Schalke 04 and 0.69 for FSV Mainz 05 (1.56 combined). The most likely exact score is 0-0 at 18.9%. Goal-market probabilities: at least one goal: 81.1%; Over 2.5 goals: 22.0%; Under 4.5 goals: 97.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 34.8% | 2.87 |
| Draw | 32.4% | 3.09 |
| FSV Mainz 05 win | 32.8% | 3.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| FSV Mainz 05 expected goals | 0.69 |
| Expected total goals | 1.56 |
| Over 0.5 | 81.1% |
| Under 0.5 | 18.9% |
| Over 1.5 | 47.9% |
| Under 1.5 | 52.1% |
| Over 2.5 | 22.0% |
| Under 2.5 | 78.0% |
| Over 3.5 | 7.5% |
| Under 3.5 | 92.5% |
| Over 4.5 | 2.3% |
| Under 4.5 | 97.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.88% |
| 2 | 0-1 | 16.89% |
| 3 | 1-0 | 16.37% |
| 4 | 1-1 | 11.77% |
| 5 | 2-0 | 7.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 34.8% | 33.4% | 3.05 | +6.3% |
| Draw | 32.4% | 26.5% | 3.80 | +23.0% |
| FSV Mainz 05 win | 32.8% | 40.2% | 2.44 | -20.0% |
| Over 2.5 | 22.0% | 59.8% | 1.66 | -63.5% |
| Under 2.5 | 78.0% | 40.2% | 2.42 | +88.7% |

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
| Market best home last update utc | 2026-10-09T13:48:19Z |
| Market best draw last update utc | 2026-10-09T13:48:19Z |
| Market best away last update utc | 2026-10-09T13:47:13Z |
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
| P btts yes | 29.2% |
| P btts no | 70.8% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.30 |
| Fair Over 1.5 odds | 2.09 |
| Fair Under 1.5 odds | 1.92 |
| Fair Over 2.5 odds | 4.54 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 13.41 |
| Fair Under 3.5 odds | 1.08 |
| Fair Over 4.5 odds | 43.36 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 36.3% |
| Unadjusted draw probability | 38.3% |
| Unadjusted away-win probability | 25.4% |
| Raw p over 1 5 | 47.5% |
| Raw p under 3 5 | 92.7% |
| Raw p btts yes | 30.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.85 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.39 |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +1.5% |
| Draw probability edge | +5.9% |
| Away probability edge | -7.4% |
| Over 2.5 probability edge | -37.8% |
| Under 2.5 probability edge | +37.8% |
| Raw edge prob home | 0.0290 |
| Raw ev home | 0.1070 |
| Raw edge prob draw | 0.1181 |
| Raw ev draw | 0.4539 |
| Raw edge prob away | -0.1471 |
| Raw ev away | -0.3791 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | William Hill |
| Market best over 1 5 last update utc | 2026-10-09T13:48:18Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 61.8% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-09T13:49:06Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.43 |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | William Hill |
| Market best btts yes last update utc | 2026-10-09T13:48:18Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.50 |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **55.3%**. Expected goals are 1.11 for Hamburger SV and 2.02 for VfB Stuttgart (3.13 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 60.3%; Under 4.5 goals: 79.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 21.2% | 4.72 |
| Draw | 23.5% | 4.25 |
| VfB Stuttgart win | 55.3% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.11 |
| VfB Stuttgart expected goals | 2.02 |
| Expected total goals | 3.13 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.94% |
| 2 | 1-2 | 9.55% |
| 3 | 0-2 | 8.60% |
| 4 | 0-1 | 7.53% |
| 5 | 1-3 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 21.2% | 23.0% | 4.20 | -11.0% |
| Draw | 23.5% | 23.7% | 4.40 | +3.5% |
| VfB Stuttgart win | 55.3% | 53.2% | 1.90 | +5.0% |
| Over 2.5 | 60.3% | 70.7% | 1.38 | -16.7% |
| Under 2.5 | 39.7% | 29.3% | 3.10 | +23.0% |

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
| Market best home last update utc | 2026-10-09T13:48:19Z |
| Market best draw last update utc | 2026-10-09T13:48:19Z |
| Market best away last update utc | 2026-10-09T13:47:13Z |
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
| P btts yes | 59.4% |
| P btts no | 40.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.35 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.82 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.87 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 19.4% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 57.3% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 61.8% |
| Raw p btts yes | 59.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.04 |
| Reference draw odds | 3.92 |
| Reference away odds | 1.82 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | -1.8% |
| Draw probability edge | -0.2% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -10.4% |
| Under 2.5 probability edge | +10.4% |
| Raw edge prob home | -0.0365 |
| Raw ev home | -0.1869 |
| Raw edge prob draw | -0.0044 |
| Raw ev draw | 0.0257 |
| Raw edge prob away | 0.0408 |
| Raw ev away | 0.0893 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **59.0%**. Expected goals are 0.94 for Union Berlin and 1.92 for Borussia Dortmund (2.87 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 55.0%; Under 4.5 goals: 83.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 18.3% | 5.45 |
| Draw | 22.6% | 4.42 |
| Borussia Dortmund win | 59.0% | 1.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 0.94 |
| Borussia Dortmund expected goals | 1.92 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.0% |
| Under 2.5 | 45.0% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.78% |
| 2 | 0-2 | 10.50% |
| 3 | 1-2 | 9.88% |
| 4 | 0-1 | 9.84% |
| 5 | 0-3 | 6.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 18.3% | 19.9% | 5.40 | -0.9% |
| Draw | 22.6% | 21.3% | 4.50 | +1.8% |
| Borussia Dortmund win | 59.0% | 58.8% | 1.73 | +2.1% |
| Over 2.5 | 55.0% | 65.4% | 1.49 | -18.0% |
| Under 2.5 | 45.0% | 34.6% | 2.70 | +21.4% |

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
| Market best home last update utc | 2026-10-09T13:48:19Z |
| Market best draw last update utc | 2026-10-09T13:49:06Z |
| Market best away last update utc | 2026-10-09T13:47:13Z |
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
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.60 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.78 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.10 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.10 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 16.8% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 59.3% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 53.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.59 |
| Reference draw odds | 4.29 |
| Reference away odds | 1.65 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -1.5% |
| Draw probability edge | +1.3% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -10.4% |
| Under 2.5 probability edge | +10.4% |
| Raw edge prob home | -0.0304 |
| Raw ev home | -0.0916 |
| Raw edge prob draw | 0.0255 |
| Raw ev draw | 0.0751 |
| Raw edge prob away | 0.0049 |
| Raw ev away | 0.0257 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **49.6%**. Expected goals are 1.16 for Werder Bremen and 0.74 for SC Paderborn (1.91 combined). The most likely exact score is 1-0 at 17.8%. Goal-market probabilities: at least one goal: 86.5%; Over 2.5 goals: 31.6%; Under 4.5 goals: 95.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 49.6% | 2.01 |
| Draw | 27.8% | 3.60 |
| SC Paderborn win | 22.6% | 4.43 |

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
| 1 | 1-0 | 17.82% |
| 2 | 0-0 | 13.48% |
| 3 | 1-1 | 11.79% |
| 4 | 2-0 | 11.25% |
| 5 | 0-1 | 9.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 49.6% | 54.8% | 1.91 | -5.2% |
| Draw | 27.8% | 22.2% | 4.26 | +18.5% |
| SC Paderborn win | 22.6% | 23.1% | 4.25 | -4.1% |
| Over 2.5 | 31.6% | 62.7% | 1.56 | -50.7% |
| Under 2.5 | 68.4% | 37.3% | 2.47 | +69.0% |

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
| Market best home last update utc | 2026-10-09T13:48:19Z |
| Market best draw last update utc | 2026-10-09T13:47:13Z |
| Market best away last update utc | 2026-10-09T13:48:50Z |
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
| P btts yes | 36.1% |
| P btts no | 63.9% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.42 |
| Fair Over 1.5 odds | 1.70 |
| Fair Under 1.5 odds | 2.43 |
| Fair Over 2.5 odds | 3.17 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.70 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.91 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 44.5% |
| Unadjusted draw probability | 33.4% |
| Unadjusted away-win probability | 22.1% |
| Raw p over 1 5 | 58.1% |
| Raw p under 3 5 | 87.4% |
| Raw p btts yes | 37.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.77 |
| Reference draw odds | 4.17 |
| Reference away odds | 4.02 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | -5.1% |
| Draw probability edge | +5.6% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -31.1% |
| Under 2.5 probability edge | +31.1% |
| Raw edge prob home | -0.1026 |
| Raw ev home | -0.1500 |
| Raw edge prob draw | 0.1125 |
| Raw ev draw | 0.4242 |
| Raw edge prob away | -0.0099 |
| Raw ev away | -0.0621 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **64.0%**. Expected goals are 2.44 for Bayer Leverkusen and 0.96 for SC Freiburg (3.41 combined). The most likely exact score is 2-0 at 9.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 65.4%; Under 4.5 goals: 74.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 64.0% | 1.56 |
| Draw | 19.7% | 5.08 |
| SC Freiburg win | 16.3% | 6.12 |

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
| Over 2.5 | 65.4% |
| Under 2.5 | 34.6% |
| Over 3.5 | 43.4% |
| Under 3.5 | 56.6% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.17% |
| 2 | 1-1 | 9.06% |
| 3 | 2-1 | 8.83% |
| 4 | 3-0 | 7.46% |
| 5 | 3-1 | 7.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 64.0% | 58.8% | 1.70 | +8.7% |
| Draw | 19.7% | 20.7% | 4.60 | -9.4% |
| SC Freiburg win | 16.3% | 20.5% | 4.83 | -21.0% |
| Over 2.5 | 65.4% | 65.4% | 1.49 | -2.5% |
| Under 2.5 | 34.6% | 34.6% | 2.67 | -7.7% |

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
| Market best home last update utc | 2026-10-09T13:47:13Z |
| Market best draw last update utc | 2026-10-09T13:48:34Z |
| Market best away last update utc | 2026-10-09T13:47:13Z |
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
| P btts yes | 58.0% |
| P btts no | 42.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.01 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.00 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.89 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.99 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.7% |
| Raw p btts yes | 57.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.65 |
| Reference draw odds | 4.43 |
| Reference away odds | 4.46 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | +5.1% |
| Draw probability edge | -1.0% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1025 |
| Raw ev home | 0.1743 |
| Raw edge prob draw | -0.0192 |
| Raw ev draw | -0.1381 |
| Raw edge prob away | -0.0833 |
| Raw ev away | -0.4114 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **42.1%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 72.0%; Under 4.5 goals: 68.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 35.2% | 2.84 |
| Draw | 22.7% | 4.41 |
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
| Over 3.5 | 51.1% |
| Under 3.5 | 48.9% |
| Over 4.5 | 31.8% |
| Under 4.5 | 68.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.01% |
| 2 | 1-2 | 8.87% |
| 3 | 2-2 | 7.06% |
| 4 | 2-1 | 6.89% |
| 5 | 1-3 | 5.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 35.2% | 29.1% | 3.58 | +25.9% |
| Draw | 22.7% | 22.1% | 4.26 | -3.4% |
| TSG Hoffenheim win | 42.1% | 48.8% | 2.00 | -15.7% |
| Over 2.5 | 72.0% | 69.6% | 1.40 | +0.9% |
| Under 2.5 | 28.0% | 30.4% | 3.00 | -16.1% |

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
| Market best home last update utc | 2026-10-09T13:47:13Z |
| Market best draw last update utc | 2026-10-09T13:47:13Z |
| Market best away last update utc | 2026-10-09T13:48:19Z |
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
| P btts yes | 72.1% |
| P btts no | 27.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.20 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.50 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.58 |
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
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.24 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.98 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | +6.1% |
| Draw probability edge | +0.5% |
| Away probability edge | -6.6% |
| Over 2.5 probability edge | +2.4% |
| Under 2.5 probability edge | -2.4% |
| Raw edge prob home | 0.1221 |
| Raw ev home | 0.4780 |
| Raw edge prob draw | 0.0108 |
| Raw ev draw | -0.0111 |
| Raw edge prob away | -0.1328 |
| Raw ev away | -0.2899 |

</details>


---
