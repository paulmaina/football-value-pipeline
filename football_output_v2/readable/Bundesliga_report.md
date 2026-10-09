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

## 2026-10-09 — Borussia Dortmund vs Werder Bremen

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **71.0%**. Expected goals are 2.30 for Borussia Dortmund and 0.97 for Werder Bremen (3.27 combined). The most likely exact score is 2-0 at 10.7%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 64.9%; Under 4.5 goals: 76.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 71.0% | 1.41 |
| Draw | 17.2% | 5.82 |
| Werder Bremen win | 11.9% | 8.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.30 |
| Werder Bremen expected goals | 0.97 |
| Expected total goals | 3.27 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 64.9% |
| Under 2.5 | 35.1% |
| Over 3.5 | 42.1% |
| Under 3.5 | 57.9% |
| Over 4.5 | 24.0% |
| Under 4.5 | 76.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.74% |
| 2 | 2-1 | 10.42% |
| 3 | 1-0 | 8.38% |
| 4 | 3-0 | 8.24% |
| 5 | 3-1 | 8.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 71.0% | 75.6% | 1.37 | -2.8% |
| Draw | 17.2% | 14.3% | 6.25 | +7.4% |
| Werder Bremen win | 11.9% | 10.2% | 10.00 | +18.6% |
| Over 2.5 | 64.9% | 69.6% | 1.40 | -9.1% |
| Under 2.5 | 35.1% | 30.4% | 3.00 | +5.3% |

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
| Market best home last update utc | 2026-10-09T07:42:35Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:41:50Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Coolbet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Dortmund |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 55.8% |
| P btts no | 44.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.07 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.75 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.85 |
| Fair Over 3.5 odds | 2.37 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.16 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 66.4% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 13.5% |
| Raw p over 1 5 | 84.7% |
| Raw p under 3 5 | 58.6% |
| Raw p btts yes | 56.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.30 |
| Reference draw odds | 6.20 |
| Reference away odds | 8.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | -4.6% |
| Draw probability edge | +2.9% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | -0.0921 |
| Raw ev home | -0.0909 |
| Raw edge prob draw | 0.0585 |
| Raw ev draw | 0.2565 |
| Raw edge prob away | 0.0336 |
| Raw ev away | 0.3541 |

</details>


---

## 2026-10-10 — Augsburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **78.9%**. Expected goals are 1.04 for Augsburg and 2.87 for Bayern Munich (3.92 combined). The most likely exact score is 1-2 at 9.1%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 76.4%; Under 4.5 goals: 63.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 8.8% | 11.38 |
| Draw | 12.3% | 8.12 |
| Bayern Munich win | 78.9% | 1.27 |

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
| Over 2.5 | 76.4% |
| Under 2.5 | 23.6% |
| Over 3.5 | 55.9% |
| Under 3.5 | 44.1% |
| Over 4.5 | 36.6% |
| Under 4.5 | 63.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.10% |
| 2 | 1-3 | 8.72% |
| 3 | 0-2 | 8.72% |
| 4 | 0-3 | 8.35% |
| 5 | 1-4 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 8.8% | 7.3% | 14.50 | +27.4% |
| Draw | 12.3% | 9.1% | 9.60 | +18.2% |
| Bayern Munich win | 78.9% | 83.5% | 1.23 | -2.9% |
| Over 2.5 | 76.4% | 85.9% | 1.15 | -12.2% |
| Under 2.5 | 23.6% | 14.1% | 5.55 | +31.1% |

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
| Market best home last update utc | 2026-10-09T07:42:20Z |
| Market best draw last update utc | 2026-10-09T07:42:34Z |
| Market best away last update utc | 2026-10-09T07:42:35Z |
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
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 48.17 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.45 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.23 |
| Fair Over 3.5 odds | 1.79 |
| Fair Under 3.5 odds | 2.27 |
| Fair Over 4.5 odds | 2.73 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 10.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 74.3% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 45.0% |
| Raw p btts yes | 61.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 11.00 |
| Reference draw odds | 9.00 |
| Reference away odds | 1.18 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.14 |
| Reference Under 2.5 odds | 5.40 |
| Home probability edge | +1.4% |
| Draw probability edge | +3.2% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | 0.0287 |
| Raw ev home | 0.4818 |
| Raw edge prob draw | 0.0634 |
| Raw ev draw | 0.4863 |
| Raw edge prob away | -0.0921 |
| Raw ev away | -0.0861 |

</details>


---

## 2026-10-10 — FSV Mainz 05 vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **49.1%**. Expected goals are 1.08 for FSV Mainz 05 and 1.81 for Bayer Leverkusen (2.89 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 55.0%; Under 4.5 goals: 83.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 25.7% | 3.88 |
| Draw | 25.2% | 3.97 |
| Bayer Leverkusen win | 49.1% | 2.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.08 |
| Bayer Leverkusen expected goals | 1.81 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.0% |
| Under 2.5 | 45.0% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.5% |
| Under 4.5 | 83.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.95% |
| 2 | 1-2 | 9.02% |
| 3 | 0-2 | 8.38% |
| 4 | 0-1 | 8.20% |
| 5 | 2-1 | 7.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 25.7% | 30.3% | 3.10 | -20.2% |
| Draw | 25.2% | 25.1% | 4.10 | +3.3% |
| Bayer Leverkusen win | 49.1% | 44.6% | 2.31 | +13.3% |
| Over 2.5 | 55.0% | 67.0% | 1.45 | -20.2% |
| Under 2.5 | 45.0% | 33.0% | 2.80 | +26.0% |

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
| Market best home last update utc | 2026-10-09T07:42:37Z |
| Market best draw last update utc | 2026-10-09T07:42:35Z |
| Market best away last update utc | 2026-10-09T07:41:18Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Unibet (SE) |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Mainz |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.99 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.08 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.06 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 21.2% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 53.6% |
| Raw p over 1 5 | 79.5% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 56.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.10 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Home probability edge | -4.5% |
| Draw probability edge | +0.1% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | -12.0% |
| Under 2.5 probability edge | +12.0% |
| Raw edge prob home | -0.0910 |
| Raw ev home | -0.3429 |
| Raw edge prob draw | 0.0012 |
| Raw ev draw | 0.0354 |
| Raw edge prob away | 0.0898 |
| Raw ev away | 0.2370 |

</details>


---

## 2026-10-10 — RB Leipzig vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **RB Leipzig win** at **58.7%**. Expected goals are 2.13 for RB Leipzig and 1.35 for Eintracht Frankfurt (3.48 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 68.4%; Under 4.5 goals: 72.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 58.7% | 1.70 |
| Draw | 20.4% | 4.91 |
| Eintracht Frankfurt win | 20.9% | 4.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.13 |
| Eintracht Frankfurt expected goals | 1.35 |
| Expected total goals | 3.48 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 87.3% |
| Under 1.5 | 12.7% |
| Over 2.5 | 68.4% |
| Under 2.5 | 31.6% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.17% |
| 2 | 1-1 | 8.83% |
| 3 | 2-0 | 7.55% |
| 4 | 3-1 | 7.22% |
| 5 | 1-0 | 6.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 58.7% | 62.9% | 1.62 | -4.9% |
| Draw | 20.4% | 18.2% | 5.20 | +6.0% |
| Eintracht Frankfurt win | 20.9% | 19.0% | 5.40 | +13.1% |
| Over 2.5 | 68.4% | 75.4% | 1.30 | -11.1% |
| Under 2.5 | 31.6% | 24.6% | 3.60 | +13.7% |

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
| Market best home last update utc | 2026-10-09T07:42:34Z |
| Market best draw last update utc | 2026-10-09T07:42:22Z |
| Market best away last update utc | 2026-10-09T07:42:35Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Winamax (DE) |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 81/100 |
| P btts yes | 65.5% |
| P btts no | 34.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.63 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.90 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.16 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.62 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 54.5% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 22.9% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 54.1% |
| Raw p btts yes | 66.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.55 |
| Reference draw odds | 5.00 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.55 |
| Home probability edge | -4.2% |
| Draw probability edge | +2.2% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | -0.0835 |
| Raw ev home | -0.1170 |
| Raw edge prob draw | 0.0442 |
| Raw ev draw | 0.1746 |
| Raw edge prob away | 0.0393 |
| Raw ev away | 0.2369 |

</details>


---

## 2026-10-10 — SC Paderborn vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **56.8%**. Expected goals are 0.76 for SC Paderborn and 1.42 for VfB Stuttgart (2.18 combined). The most likely exact score is 0-1 at 16.3%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.1%; Under 4.5 goals: 92.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 18.4% | 5.42 |
| Draw | 24.8% | 4.03 |
| VfB Stuttgart win | 56.8% | 1.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.76 |
| VfB Stuttgart expected goals | 1.42 |
| Expected total goals | 2.18 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 18.2% |
| Under 3.5 | 81.8% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.28% |
| 2 | 0-2 | 12.57% |
| 3 | 1-1 | 11.22% |
| 4 | 0-0 | 10.47% |
| 5 | 1-2 | 9.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 18.4% | 18.2% | 5.30 | -2.3% |
| Draw | 24.8% | 19.8% | 4.90 | +21.4% |
| VfB Stuttgart win | 56.8% | 62.0% | 1.64 | -6.9% |
| Over 2.5 | 39.1% | 70.7% | 1.38 | -46.1% |
| Under 2.5 | 60.9% | 29.3% | 3.10 | +88.9% |

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
| Market best home last update utc | 2026-10-09T07:42:34Z |
| Market best draw last update utc | 2026-10-09T07:42:34Z |
| Market best away last update utc | 2026-10-09T07:41:18Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Paderborn |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 40.4% |
| P btts no | 59.6% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.55 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.50 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.34 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 18.7% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 51.6% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 41.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 5.00 |
| Reference draw odds | 4.60 |
| Reference away odds | 1.57 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | +0.3% |
| Draw probability edge | +4.9% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | -31.6% |
| Under 2.5 probability edge | +31.6% |
| Raw edge prob home | 0.0056 |
| Raw ev home | -0.0077 |
| Raw edge prob draw | 0.0989 |
| Raw ev draw | 0.4566 |
| Raw edge prob away | -0.1045 |
| Raw ev away | -0.1546 |

</details>


---

## 2026-10-10 — TSG Hoffenheim vs Hamburger SV

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **63.2%**. Expected goals are 2.09 for TSG Hoffenheim and 1.21 for Hamburger SV (3.30 combined). The most likely exact score is 2-1 at 10.9%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 65.4%; Under 4.5 goals: 75.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 63.2% | 1.58 |
| Draw | 20.0% | 5.01 |
| Hamburger SV win | 16.8% | 5.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 2.09 |
| Hamburger SV expected goals | 1.21 |
| Expected total goals | 3.30 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 85.6% |
| Under 1.5 | 14.4% |
| Over 2.5 | 65.4% |
| Under 2.5 | 34.6% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.6% |
| Under 4.5 | 75.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.88% |
| 2 | 1-1 | 9.02% |
| 3 | 2-0 | 8.98% |
| 4 | 3-1 | 7.58% |
| 5 | 1-0 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 63.2% | 69.8% | 1.49 | -5.8% |
| Draw | 20.0% | 17.1% | 5.40 | +7.9% |
| Hamburger SV win | 16.8% | 13.1% | 7.40 | +24.5% |
| Over 2.5 | 65.4% | 69.6% | 1.40 | -8.5% |
| Under 2.5 | 34.6% | 30.4% | 3.00 | +3.9% |

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
| Market best home last update utc | 2026-10-09T07:41:18Z |
| Market best draw last update utc | 2026-10-09T07:42:34Z |
| Market best away last update utc | 2026-10-09T07:42:34Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
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
| Fair Under 0.5 odds | 24.53 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.93 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.89 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.07 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 56.6% |
| Unadjusted draw probability | 22.8% |
| Unadjusted away-win probability | 20.6% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 58.0% |
| Raw p btts yes | 62.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.40 |
| Reference draw odds | 5.20 |
| Reference away odds | 6.70 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | -6.6% |
| Draw probability edge | +2.8% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | -0.1315 |
| Raw ev home | -0.1562 |
| Raw edge prob draw | 0.0565 |
| Raw ev draw | 0.2310 |
| Raw edge prob away | 0.0750 |
| Raw ev away | 0.5225 |

</details>


---

## 2026-10-10 — Union Berlin vs Elversberg

The model's most likely 1X2 outcome is **Elversberg win** at **50.5%**. Expected goals are 1.17 for Union Berlin and 2.48 for Elversberg (3.65 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 68.9%; Under 4.5 goals: 71.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 27.6% | 3.63 |
| Draw | 21.9% | 4.57 |
| Elversberg win | 50.5% | 1.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 1.17 |
| Elversberg expected goals | 2.48 |
| Expected total goals | 3.65 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 68.9% |
| Under 2.5 | 31.1% |
| Over 3.5 | 47.4% |
| Under 3.5 | 52.6% |
| Over 4.5 | 28.6% |
| Under 4.5 | 71.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.45% |
| 2 | 2-1 | 7.87% |
| 3 | 1-2 | 7.24% |
| 4 | 0-2 | 6.21% |
| 5 | 2-2 | 6.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 27.6% | 39.7% | 2.42 | -33.3% |
| Draw | 21.9% | 24.5% | 3.96 | -13.3% |
| Elversberg win | 50.5% | 35.8% | 2.96 | +49.6% |
| Over 2.5 | 68.9% | 61.3% | 1.57 | +8.1% |
| Under 2.5 | 31.1% | 38.7% | 2.52 | -21.6% |

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
| Market best home last update utc | 2026-10-09T07:42:34Z |
| Market best draw last update utc | 2026-10-09T07:41:18Z |
| Market best away last update utc | 2026-10-09T07:42:34Z |
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
| P btts yes | 65.8% |
| P btts no | 34.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.96 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.21 |
| Fair Over 3.5 odds | 2.11 |
| Fair Under 3.5 odds | 1.90 |
| Fair Over 4.5 odds | 3.49 |
| Fair Under 4.5 odds | 1.40 |
| Unadjusted home-win probability | 15.4% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 65.3% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.5% |
| Raw p btts yes | 63.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.40 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -12.2% |
| Draw probability edge | -2.6% |
| Away probability edge | +14.8% |
| Over 2.5 probability edge | +7.6% |
| Under 2.5 probability edge | -7.6% |
| Raw edge prob home | -0.2433 |
| Raw ev home | -0.6272 |
| Raw edge prob draw | -0.0518 |
| Raw ev draw | -0.2359 |
| Raw edge prob away | 0.2951 |
| Raw ev away | 0.9328 |

</details>


---

## 2026-10-11 — 1. FC Köln vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **1. FC Köln win** at **40.4%**. Expected goals are 1.43 for 1. FC Köln and 1.55 for Borussia Monchengladbach (2.97 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 57.6%; Under 4.5 goals: 81.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 40.4% | 2.47 |
| Draw | 25.3% | 3.96 |
| Borussia Monchengladbach win | 34.3% | 2.91 |

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
| Over 2.5 | 57.6% |
| Under 2.5 | 42.4% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.2% |
| Under 4.5 | 81.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.77% |
| 2 | 2-1 | 9.58% |
| 3 | 1-2 | 7.62% |
| 4 | 1-0 | 7.27% |
| 5 | 2-0 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 40.4% | 46.9% | 2.10 | -15.1% |
| Draw | 25.3% | 23.8% | 4.15 | +4.8% |
| Borussia Monchengladbach win | 34.3% | 29.3% | 3.50 | +20.2% |
| Over 2.5 | 57.6% | 65.4% | 1.50 | -13.6% |
| Under 2.5 | 42.4% | 34.6% | 2.67 | +13.2% |

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
| Market best home last update utc | 2026-10-09T07:41:50Z |
| Market best draw last update utc | 2026-10-09T07:41:18Z |
| Market best away last update utc | 2026-10-09T07:42:34Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Coolbet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Betfair |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Koln |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.83 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.49 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 33.9% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 39.4% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 61.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.05 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.20 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -6.5% |
| Draw probability edge | +1.5% |
| Away probability edge | +5.0% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | -0.1297 |
| Raw ev home | -0.2877 |
| Raw edge prob draw | 0.0293 |
| Raw ev draw | 0.1091 |
| Raw edge prob away | 0.1004 |
| Raw ev away | 0.3775 |

</details>


---

## 2026-10-11 — SC Freiburg vs FC Schalke 04

The model's most likely 1X2 outcome is **SC Freiburg win** at **47.1%**. Expected goals are 0.90 for SC Freiburg and 0.80 for FC Schalke 04 (1.70 combined). The most likely exact score is 1-0 at 20.6%. Goal-market probabilities: at least one goal: 84.1%; Over 2.5 goals: 26.3%; Under 4.5 goals: 96.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 47.1% | 2.12 |
| Draw | 29.9% | 3.35 |
| FC Schalke 04 win | 23.1% | 4.34 |

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
| 1 | 1-0 | 20.61% |
| 2 | 0-0 | 15.94% |
| 3 | 1-1 | 11.82% |
| 4 | 0-1 | 10.55% |
| 5 | 2-0 | 10.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 47.1% | 60.0% | 1.71 | -19.5% |
| Draw | 29.9% | 23.0% | 4.40 | +31.3% |
| FC Schalke 04 win | 23.1% | 17.1% | 5.60 | +29.1% |
| Over 2.5 | 26.3% | 61.8% | 1.69 | -55.6% |
| Under 2.5 | 73.7% | 38.2% | 2.48 | +82.8% |

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
| Market best home last update utc | 2026-10-09T07:41:18Z |
| Market best draw last update utc | 2026-10-09T07:42:35Z |
| Market best away last update utc | 2026-10-09T07:42:34Z |
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
| Fair Under 0.5 odds | 6.28 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.12 |
| Fair Over 2.5 odds | 3.80 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 10.32 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.64 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 34.2% |
| Unadjusted draw probability | 36.7% |
| Unadjusted away-win probability | 29.1% |
| Raw p over 1 5 | 52.1% |
| Raw p under 3 5 | 90.6% |
| Raw p btts yes | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.62 |
| Reference draw odds | 4.00 |
| Reference away odds | 5.30 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -12.9% |
| Draw probability edge | +6.9% |
| Away probability edge | +6.0% |
| Over 2.5 probability edge | -35.5% |
| Under 2.5 probability edge | +35.5% |
| Raw edge prob home | -0.2572 |
| Raw ev home | -0.4146 |
| Raw edge prob draw | 0.1373 |
| Raw ev draw | 0.6155 |
| Raw edge prob away | 0.1199 |
| Raw ev away | 0.6269 |

</details>


---

## 2026-10-16 — Eintracht Frankfurt vs 1. FC Köln

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **56.6%**. Expected goals are 2.20 for Eintracht Frankfurt and 1.06 for 1. FC Köln (3.26 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 62.7%; Under 4.5 goals: 77.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 56.6% | 1.77 |
| Draw | 22.0% | 4.54 |
| 1. FC Köln win | 21.4% | 4.66 |

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
| 1 | 1-1 | 10.15% |
| 2 | 2-1 | 8.94% |
| 3 | 2-0 | 8.45% |
| 4 | 1-0 | 6.83% |
| 5 | 3-1 | 6.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 56.6% | 50.8% | 2.00 | +13.1% |
| Draw | 22.0% | 22.6% | 4.30 | -5.4% |
| 1. FC Köln win | 21.4% | 26.7% | 3.65 | -21.7% |
| Over 2.5 | 62.7% | 69.6% | 1.40 | -12.3% |
| Under 2.5 | 37.3% | 30.4% | 3.00 | +12.0% |

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
| Market best home last update utc | 2026-10-09T07:41:18Z |
| Market best draw last update utc | 2026-10-09T07:41:18Z |
| Market best away last update utc | 2026-10-09T07:42:35Z |
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
| Fair Under 0.5 odds | 20.38 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.30 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.48 |
| Fair Under 3.5 odds | 1.67 |
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
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.90 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | +5.8% |
| Draw probability edge | -0.6% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | 0.1153 |
| Raw ev home | 0.2465 |
| Raw edge prob draw | -0.0110 |
| Raw ev draw | -0.0776 |
| Raw edge prob away | -0.1043 |
| Raw ev away | -0.4078 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **74.8%**. Expected goals are 2.79 for Bayern Munich and 1.24 for RB Leipzig (4.02 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 77.8%; Under 4.5 goals: 61.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 74.8% | 1.34 |
| Draw | 13.9% | 7.18 |
| RB Leipzig win | 11.2% | 8.90 |

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
| Over 2.5 | 77.8% |
| Under 2.5 | 22.2% |
| Over 3.5 | 58.0% |
| Under 3.5 | 42.0% |
| Over 4.5 | 38.7% |
| Under 4.5 | 61.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.31% |
| 2 | 3-1 | 8.65% |
| 3 | 2-0 | 7.53% |
| 4 | 3-0 | 7.00% |
| 5 | 4-1 | 6.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 74.8% | 80.6% | 1.27 | -4.9% |
| Draw | 13.9% | 10.7% | 8.00 | +11.4% |
| RB Leipzig win | 11.2% | 8.7% | 11.20 | +25.8% |
| Over 2.5 | 77.8% | 83.6% | 1.18 | -8.2% |
| Under 2.5 | 22.2% | 16.4% | 5.01 | +11.1% |

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
| Market best home last update utc | 2026-10-09T07:41:18Z |
| Market best draw last update utc | 2026-10-09T07:41:51Z |
| Market best away last update utc | 2026-10-09T07:41:18Z |
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
| P btts yes | 66.1% |
| P btts no | 33.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 50.42 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.54 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.51 |
| Fair Over 3.5 odds | 1.73 |
| Fair Under 3.5 odds | 2.38 |
| Fair Over 4.5 odds | 2.58 |
| Fair Under 4.5 odds | 1.63 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 13.8% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 42.9% |
| Raw p btts yes | 67.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.22 |
| Reference draw odds | 7.80 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.17 |
| Reference Under 2.5 odds | 4.90 |
| Home probability edge | -5.7% |
| Draw probability edge | +3.2% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.1146 |
| Raw ev home | -0.1222 |
| Raw edge prob draw | 0.0635 |
| Raw ev draw | 0.3676 |
| Raw edge prob away | 0.0511 |
| Raw ev away | 0.5445 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **56.0%**. Expected goals are 2.96 for Elversberg and 1.17 for Augsburg (4.13 combined). The most likely exact score is 1-1 at 8.1%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 75.4%; Under 4.5 goals: 63.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 56.0% | 1.78 |
| Draw | 20.3% | 4.92 |
| Augsburg win | 23.6% | 4.24 |

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
| Over 2.5 | 75.4% |
| Under 2.5 | 24.6% |
| Over 3.5 | 56.1% |
| Under 3.5 | 43.9% |
| Over 4.5 | 36.7% |
| Under 4.5 | 63.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.09% |
| 2 | 1-2 | 6.75% |
| 3 | 2-2 | 6.33% |
| 4 | 2-1 | 6.32% |
| 5 | 3-1 | 6.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 56.0% | 38.9% | 2.55 | +42.9% |
| Draw | 20.3% | 25.2% | 4.00 | -18.6% |
| Augsburg win | 23.6% | 35.8% | 2.80 | -33.9% |
| Over 2.5 | 75.4% | 66.1% | 1.47 | +10.9% |
| Under 2.5 | 24.6% | 33.9% | 2.71 | -33.4% |

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
| Market best home last update utc | 2026-10-09T07:41:18Z |
| Market best draw last update utc | 2026-10-09T07:42:36Z |
| Market best away last update utc | 2026-10-09T07:42:36Z |
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
| Fair Under 0.5 odds | 34.66 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.37 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 4.07 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.28 |
| Fair Over 4.5 odds | 2.72 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 73.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 92.3% |
| Raw p under 3 5 | 40.9% |
| Raw p btts yes | 65.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.45 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.68 |
| Home probability edge | +17.1% |
| Draw probability edge | -4.9% |
| Away probability edge | -12.2% |
| Over 2.5 probability edge | +9.4% |
| Under 2.5 probability edge | -9.4% |
| Raw edge prob home | 0.3422 |
| Raw ev home | 0.8655 |
| Raw edge prob draw | -0.0976 |
| Raw ev draw | -0.3813 |
| Raw edge prob away | -0.2447 |
| Raw ev away | -0.6814 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FC Schalke 04 win** at **34.4%**. Expected goals are 0.87 for FC Schalke 04 and 0.69 for FSV Mainz 05 (1.56 combined). The most likely exact score is 0-0 at 19.0%. Goal-market probabilities: at least one goal: 81.0%; Over 2.5 goals: 22.0%; Under 4.5 goals: 97.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 34.4% | 2.90 |
| Draw | 32.5% | 3.08 |
| FSV Mainz 05 win | 33.1% | 3.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| FSV Mainz 05 expected goals | 0.69 |
| Expected total goals | 1.56 |
| Over 0.5 | 81.0% |
| Under 0.5 | 19.0% |
| Over 1.5 | 47.8% |
| Under 1.5 | 52.2% |
| Over 2.5 | 22.0% |
| Under 2.5 | 78.0% |
| Over 3.5 | 7.4% |
| Under 3.5 | 92.6% |
| Over 4.5 | 2.3% |
| Under 4.5 | 97.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 18.97% |
| 2 | 0-1 | 17.02% |
| 3 | 1-0 | 16.18% |
| 4 | 1-1 | 11.82% |
| 5 | 2-0 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 34.4% | 32.6% | 3.00 | +3.3% |
| Draw | 32.5% | 26.7% | 3.80 | +23.5% |
| FSV Mainz 05 win | 33.1% | 40.7% | 2.44 | -19.3% |
| Over 2.5 | 22.0% | 61.8% | 1.66 | -63.5% |
| Under 2.5 | 78.0% | 38.2% | 2.42 | +88.8% |

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
| Market best home last update utc | 2026-10-09T07:42:35Z |
| Market best draw last update utc | 2026-10-09T07:42:35Z |
| Market best away last update utc | 2026-10-09T07:41:18Z |
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
| Fair Under 0.5 odds | 5.27 |
| Fair Over 1.5 odds | 2.09 |
| Fair Under 1.5 odds | 1.92 |
| Fair Over 2.5 odds | 4.55 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 13.43 |
| Fair Under 3.5 odds | 1.08 |
| Fair Over 4.5 odds | 43.47 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 36.3% |
| Unadjusted draw probability | 38.3% |
| Unadjusted away-win probability | 25.4% |
| Raw p over 1 5 | 47.5% |
| Raw p under 3 5 | 92.7% |
| Raw p btts yes | 30.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.90 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.35 |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | +1.9% |
| Draw probability edge | +5.8% |
| Away probability edge | -7.6% |
| Over 2.5 probability edge | -39.8% |
| Under 2.5 probability edge | +39.8% |
| Raw edge prob home | 0.0370 |
| Raw ev home | 0.0888 |
| Raw edge prob draw | 0.1152 |
| Raw ev draw | 0.4539 |
| Raw edge prob away | -0.1523 |
| Raw ev away | -0.3791 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **55.5%**. Expected goals are 1.11 for Hamburger SV and 2.02 for VfB Stuttgart (3.13 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.6%; Under 4.5 goals: 79.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 21.6% | 4.64 |
| Draw | 22.9% | 4.36 |
| VfB Stuttgart win | 55.5% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.11 |
| VfB Stuttgart expected goals | 2.02 |
| Expected total goals | 3.13 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 60.6% |
| Under 2.5 | 39.4% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.7% |
| Under 4.5 | 79.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.65% |
| 2 | 1-2 | 9.59% |
| 3 | 0-2 | 8.63% |
| 4 | 0-1 | 7.56% |
| 5 | 1-3 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 21.6% | 23.7% | 4.25 | -8.4% |
| Draw | 22.9% | 22.5% | 4.35 | -0.3% |
| VfB Stuttgart win | 55.5% | 53.7% | 1.90 | +5.5% |
| Over 2.5 | 60.6% | 70.7% | 1.38 | -16.4% |
| Under 2.5 | 39.4% | 29.3% | 3.10 | +22.2% |

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
| Market best home last update utc | 2026-10-09T07:42:35Z |
| Market best draw last update utc | 2026-10-09T07:42:35Z |
| Market best away last update utc | 2026-10-09T07:41:18Z |
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
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.84 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.83 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.84 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 19.4% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 57.3% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 61.8% |
| Raw p btts yes | 59.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.90 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.80 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.05 |
| Home probability edge | -2.2% |
| Draw probability edge | +0.4% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | -0.0438 |
| Raw ev home | -0.1772 |
| Raw edge prob draw | 0.0079 |
| Raw ev draw | 0.0140 |
| Raw edge prob away | 0.0359 |
| Raw ev away | 0.0893 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **60.0%**. Expected goals are 0.94 for Union Berlin and 1.92 for Borussia Dortmund (2.87 combined). The most likely exact score is 0-2 at 10.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 55.3%; Under 4.5 goals: 83.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.9% | 5.59 |
| Draw | 22.1% | 4.53 |
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
| Over 2.5 | 55.3% |
| Under 2.5 | 44.7% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.5% |
| Under 4.5 | 83.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 10.68% |
| 2 | 1-1 | 10.54% |
| 3 | 1-2 | 10.05% |
| 4 | 0-1 | 10.01% |
| 5 | 0-3 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.9% | 19.0% | 5.40 | -3.4% |
| Draw | 22.1% | 20.3% | 4.50 | -0.6% |
| Borussia Dortmund win | 60.0% | 60.8% | 1.73 | +3.8% |
| Over 2.5 | 55.3% | 65.4% | 1.49 | -17.6% |
| Under 2.5 | 44.7% | 34.6% | 2.70 | +20.7% |

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
| Market best home last update utc | 2026-10-09T07:42:35Z |
| Market best draw last update utc | 2026-10-09T07:42:37Z |
| Market best away last update utc | 2026-10-09T07:41:18Z |
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
| Fair Under 0.5 odds | 15.96 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.80 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.09 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.06 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 16.8% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 59.3% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 53.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 4.80 |
| Reference draw odds | 4.50 |
| Reference away odds | 1.60 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -1.1% |
| Draw probability edge | +1.8% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | -0.0213 |
| Raw ev home | -0.0916 |
| Raw edge prob draw | 0.0360 |
| Raw ev draw | 0.0751 |
| Raw edge prob away | -0.0147 |
| Raw ev away | 0.0257 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **50.0%**. Expected goals are 1.16 for Werder Bremen and 0.74 for SC Paderborn (1.91 combined). The most likely exact score is 1-0 at 17.9%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 31.6%; Under 4.5 goals: 95.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 50.0% | 2.00 |
| Draw | 27.7% | 3.61 |
| SC Paderborn win | 22.3% | 4.48 |

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
| 1 | 1-0 | 17.94% |
| 2 | 0-0 | 13.44% |
| 3 | 1-1 | 11.75% |
| 4 | 2-0 | 11.32% |
| 5 | 0-1 | 9.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 50.0% | 55.4% | 1.91 | -4.6% |
| Draw | 27.7% | 22.0% | 4.26 | +18.1% |
| SC Paderborn win | 22.3% | 22.6% | 4.25 | -5.1% |
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
| Market best home last update utc | 2026-10-09T07:42:35Z |
| Market best draw last update utc | 2026-10-09T07:41:18Z |
| Market best away last update utc | 2026-10-09T07:42:20Z |
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
| Fair Under 0.5 odds | 7.44 |
| Fair Over 1.5 odds | 1.70 |
| Fair Under 1.5 odds | 2.43 |
| Fair Over 2.5 odds | 3.16 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.69 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.87 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 44.5% |
| Unadjusted draw probability | 33.4% |
| Unadjusted away-win probability | 22.1% |
| Raw p over 1 5 | 58.1% |
| Raw p under 3 5 | 87.4% |
| Raw p btts yes | 37.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.75 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | -5.5% |
| Draw probability edge | +5.7% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -31.1% |
| Under 2.5 probability edge | +31.1% |
| Raw edge prob home | -0.1092 |
| Raw ev home | -0.1500 |
| Raw edge prob draw | 0.1142 |
| Raw ev draw | 0.4242 |
| Raw edge prob away | -0.0051 |
| Raw ev away | -0.0621 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **64.5%**. Expected goals are 2.44 for Bayer Leverkusen and 0.96 for SC Freiburg (3.41 combined). The most likely exact score is 2-0 at 9.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 65.6%; Under 4.5 goals: 74.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 64.5% | 1.55 |
| Draw | 19.3% | 5.19 |
| SC Freiburg win | 16.2% | 6.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.44 |
| SC Freiburg expected goals | 0.96 |
| Expected total goals | 3.41 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 85.8% |
| Under 1.5 | 14.2% |
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.5% |
| Under 3.5 | 56.5% |
| Over 4.5 | 25.2% |
| Under 4.5 | 74.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.25% |
| 2 | 2-1 | 8.90% |
| 3 | 1-1 | 8.87% |
| 4 | 3-0 | 7.53% |
| 5 | 3-1 | 7.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 64.5% | 59.9% | 1.70 | +9.7% |
| Draw | 19.3% | 19.8% | 4.60 | -11.4% |
| SC Freiburg win | 16.2% | 20.3% | 4.83 | -21.6% |
| Over 2.5 | 65.6% | 65.4% | 1.49 | -2.2% |
| Under 2.5 | 34.4% | 34.6% | 2.67 | -8.2% |

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
| Market best home last update utc | 2026-10-09T07:41:18Z |
| Market best draw last update utc | 2026-10-09T07:42:37Z |
| Market best away last update utc | 2026-10-09T07:41:18Z |
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
| P btts yes | 57.9% |
| P btts no | 42.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.52 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.03 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.97 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.7% |
| Raw p btts yes | 57.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.62 |
| Reference draw odds | 4.60 |
| Reference away odds | 4.50 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | +4.6% |
| Draw probability edge | -0.5% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0914 |
| Raw ev home | 0.1743 |
| Raw edge prob draw | -0.0106 |
| Raw ev draw | -0.1381 |
| Raw edge prob away | -0.0808 |
| Raw ev away | -0.4114 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **42.7%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 72.0%; Under 4.5 goals: 68.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 34.4% | 2.91 |
| Draw | 22.9% | 4.37 |
| TSG Hoffenheim win | 42.7% | 2.34 |

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
| 1 | 1-1 | 9.09% |
| 2 | 1-2 | 9.00% |
| 3 | 2-2 | 7.13% |
| 4 | 2-1 | 6.73% |
| 5 | 1-3 | 5.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 34.4% | 27.5% | 3.58 | +23.1% |
| Draw | 22.9% | 22.6% | 4.26 | -2.5% |
| TSG Hoffenheim win | 42.7% | 50.0% | 2.00 | -14.5% |
| Over 2.5 | 72.0% | 69.6% | 1.40 | +0.8% |
| Under 2.5 | 28.0% | 30.4% | 3.00 | -15.9% |

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
| Market best home last update utc | 2026-10-09T07:41:18Z |
| Market best draw last update utc | 2026-10-09T07:41:18Z |
| Market best away last update utc | 2026-10-09T07:42:36Z |
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
| Fair Under 0.5 odds | 30.92 |
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
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.40 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.93 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.95 |
| Home probability edge | +6.9% |
| Draw probability edge | +0.3% |
| Away probability edge | -7.2% |
| Over 2.5 probability edge | +2.4% |
| Under 2.5 probability edge | -2.4% |
| Raw edge prob home | 0.1380 |
| Raw ev home | 0.4780 |
| Raw edge prob draw | 0.0066 |
| Raw ev draw | -0.0111 |
| Raw edge prob away | -0.1446 |
| Raw ev away | -0.2899 |

</details>


---
