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

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **70.8%**. Expected goals are 2.30 for Borussia Dortmund and 0.97 for Werder Bremen (3.27 combined). The most likely exact score is 2-0 at 10.7%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 64.9%; Under 4.5 goals: 75.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 70.8% | 1.41 |
| Draw | 17.0% | 5.87 |
| Werder Bremen win | 12.2% | 8.19 |

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
| Over 4.5 | 24.1% |
| Under 4.5 | 75.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.71% |
| 2 | 2-1 | 10.40% |
| 3 | 1-0 | 8.36% |
| 4 | 3-0 | 8.22% |
| 5 | 3-1 | 7.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 70.8% | 75.2% | 1.37 | -3.0% |
| Draw | 17.0% | 14.0% | 6.25 | +6.4% |
| Werder Bremen win | 12.2% | 10.9% | 10.00 | +22.0% |
| Over 2.5 | 64.9% | 69.5% | 1.40 | -9.1% |
| Under 2.5 | 35.1% | 30.5% | 3.00 | +5.2% |

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
| Market best home last update utc | 2026-10-09T08:10:39Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:10:08Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | GTbets |
| Best draw bookmaker | Unibet (SE) |
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
| Fair Under 0.5 odds | 25.29 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.74 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.85 |
| Fair Over 3.5 odds | 2.38 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.29 |
| Reference draw odds | 5.80 |
| Reference away odds | 7.25 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -4.4% |
| Draw probability edge | +3.1% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.0882 |
| Raw ev home | -0.0909 |
| Raw edge prob draw | 0.0615 |
| Raw ev draw | 0.2565 |
| Raw edge prob away | 0.0267 |
| Raw ev away | 0.3541 |

</details>


---

## 2026-10-10 — Augsburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **79.3%**. Expected goals are 1.04 for Augsburg and 2.87 for Bayern Munich (3.92 combined). The most likely exact score is 1-2 at 9.1%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 76.5%; Under 4.5 goals: 63.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 8.8% | 11.36 |
| Draw | 11.9% | 8.37 |
| Bayern Munich win | 79.3% | 1.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.04 |
| Bayern Munich expected goals | 2.87 |
| Expected total goals | 3.92 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 91.3% |
| Under 1.5 | 8.7% |
| Over 2.5 | 76.5% |
| Under 2.5 | 23.5% |
| Over 3.5 | 56.0% |
| Under 3.5 | 44.0% |
| Over 4.5 | 36.7% |
| Under 4.5 | 63.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.15% |
| 2 | 1-3 | 8.76% |
| 3 | 0-2 | 8.76% |
| 4 | 0-3 | 8.39% |
| 5 | 1-4 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 8.8% | 7.4% | 14.50 | +27.6% |
| Draw | 11.9% | 8.4% | 9.50 | +13.4% |
| Bayern Munich win | 79.3% | 84.2% | 1.23 | -2.5% |
| Over 2.5 | 76.5% | 85.5% | 1.15 | -12.0% |
| Under 2.5 | 23.5% | 14.5% | 5.55 | +30.3% |

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
| Market best home last update utc | 2026-10-09T08:09:50Z |
| Market best draw last update utc | 2026-10-09T08:10:54Z |
| Market best away last update utc | 2026-10-09T08:10:39Z |
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Nordic Bet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Augsburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 49.67 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.50 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.26 |
| Fair Over 3.5 odds | 1.79 |
| Fair Under 3.5 odds | 2.27 |
| Fair Over 4.5 odds | 2.72 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 10.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 74.3% |
| Raw p over 1 5 | 90.8% |
| Raw p under 3 5 | 45.0% |
| Raw p btts yes | 61.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 9.50 |
| Reference draw odds | 8.50 |
| Reference away odds | 1.16 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.55 |
| Home probability edge | +1.4% |
| Draw probability edge | +3.5% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -8.9% |
| Under 2.5 probability edge | +8.9% |
| Raw edge prob home | 0.0283 |
| Raw ev home | 0.4818 |
| Raw edge prob draw | 0.0708 |
| Raw ev draw | 0.4708 |
| Raw edge prob away | -0.0992 |
| Raw ev away | -0.0861 |

</details>


---

## 2026-10-10 — FSV Mainz 05 vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **49.2%**. Expected goals are 1.08 for FSV Mainz 05 and 1.81 for Bayer Leverkusen (2.89 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 55.4%; Under 4.5 goals: 83.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 26.7% | 3.74 |
| Draw | 24.1% | 4.15 |
| Bayer Leverkusen win | 49.2% | 2.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.08 |
| Bayer Leverkusen expected goals | 1.81 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 79.3% |
| Under 1.5 | 20.7% |
| Over 2.5 | 55.4% |
| Under 2.5 | 44.6% |
| Over 3.5 | 32.5% |
| Under 3.5 | 67.5% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.43% |
| 2 | 1-2 | 9.04% |
| 3 | 0-2 | 8.40% |
| 4 | 0-1 | 8.22% |
| 5 | 2-1 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 26.7% | 32.2% | 3.10 | -17.2% |
| Draw | 24.1% | 23.0% | 4.10 | -1.2% |
| Bayer Leverkusen win | 49.2% | 44.8% | 2.31 | +13.6% |
| Over 2.5 | 55.4% | 67.0% | 1.45 | -19.7% |
| Under 2.5 | 44.6% | 33.0% | 2.80 | +24.8% |

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
| Market best home last update utc | 2026-10-09T08:10:23Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:10:54Z |
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
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.67 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.83 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.08 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.01 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 21.2% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 53.6% |
| Raw p over 1 5 | 79.5% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 56.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | -5.5% |
| Draw probability edge | +1.2% |
| Away probability edge | +4.4% |
| Over 2.5 probability edge | -11.6% |
| Under 2.5 probability edge | +11.6% |
| Raw edge prob home | -0.1102 |
| Raw ev home | -0.3429 |
| Raw edge prob draw | 0.0230 |
| Raw ev draw | 0.0354 |
| Raw edge prob away | 0.0872 |
| Raw ev away | 0.2370 |

</details>


---

## 2026-10-10 — RB Leipzig vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **RB Leipzig win** at **59.2%**. Expected goals are 2.13 for RB Leipzig and 1.35 for Eintracht Frankfurt (3.48 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 68.7%; Under 4.5 goals: 72.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 59.2% | 1.69 |
| Draw | 19.7% | 5.08 |
| Eintracht Frankfurt win | 21.1% | 4.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.13 |
| Eintracht Frankfurt expected goals | 1.35 |
| Expected total goals | 3.48 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.7% |
| Under 2.5 | 31.3% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.8% |
| Under 4.5 | 72.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.25% |
| 2 | 1-1 | 8.53% |
| 3 | 2-0 | 7.61% |
| 4 | 3-1 | 7.28% |
| 5 | 1-0 | 6.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 59.2% | 63.8% | 1.62 | -4.2% |
| Draw | 19.7% | 16.8% | 5.20 | +2.4% |
| Eintracht Frankfurt win | 21.1% | 19.4% | 5.40 | +14.2% |
| Over 2.5 | 68.7% | 75.2% | 1.30 | -10.8% |
| Under 2.5 | 31.3% | 24.8% | 3.60 | +12.8% |

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
| Market best home last update utc | 2026-10-09T08:10:55Z |
| Market best draw last update utc | 2026-10-09T08:10:09Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
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
| P btts yes | 65.4% |
| P btts no | 34.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.58 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.92 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.19 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.60 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 54.5% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 22.9% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 54.1% |
| Raw p btts yes | 66.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.50 |
| Reference draw odds | 5.00 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.60 |
| Home probability edge | -4.7% |
| Draw probability edge | +2.9% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.0931 |
| Raw ev home | -0.1170 |
| Raw edge prob draw | 0.0578 |
| Raw ev draw | 0.1746 |
| Raw edge prob away | 0.0353 |
| Raw ev away | 0.2369 |

</details>


---

## 2026-10-10 — SC Paderborn vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **56.8%**. Expected goals are 0.76 for SC Paderborn and 1.42 for VfB Stuttgart (2.18 combined). The most likely exact score is 0-1 at 16.3%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 39.3%; Under 4.5 goals: 92.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 19.1% | 5.24 |
| Draw | 24.1% | 4.15 |
| VfB Stuttgart win | 56.8% | 1.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.76 |
| VfB Stuttgart expected goals | 1.42 |
| Expected total goals | 2.18 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 39.3% |
| Under 2.5 | 60.7% |
| Over 3.5 | 18.2% |
| Under 3.5 | 81.8% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.28% |
| 2 | 0-2 | 12.58% |
| 3 | 1-1 | 10.92% |
| 4 | 0-0 | 10.19% |
| 5 | 1-2 | 9.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 19.1% | 19.4% | 5.30 | +1.1% |
| Draw | 24.1% | 18.5% | 4.90 | +18.2% |
| VfB Stuttgart win | 56.8% | 62.0% | 1.64 | -6.8% |
| Over 2.5 | 39.3% | 70.6% | 1.38 | -45.8% |
| Under 2.5 | 60.7% | 29.4% | 3.10 | +88.2% |

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
| Market best home last update utc | 2026-10-09T08:10:55Z |
| Market best draw last update utc | 2026-10-09T08:10:55Z |
| Market best away last update utc | 2026-10-09T08:10:54Z |
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
| P btts yes | 40.3% |
| P btts no | 59.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.82 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.49 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.27 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 18.7% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 51.6% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 41.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.40 |
| Reference draw odds | 4.60 |
| Reference away odds | 1.54 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -0.4% |
| Draw probability edge | +5.6% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | -31.3% |
| Under 2.5 probability edge | +31.3% |
| Raw edge prob home | -0.0072 |
| Raw ev home | -0.0077 |
| Raw edge prob draw | 0.1122 |
| Raw ev draw | 0.4566 |
| Raw edge prob away | -0.1050 |
| Raw ev away | -0.1546 |

</details>


---

## 2026-10-10 — TSG Hoffenheim vs Hamburger SV

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **63.0%**. Expected goals are 2.09 for TSG Hoffenheim and 1.21 for Hamburger SV (3.30 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 65.4%; Under 4.5 goals: 75.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 63.0% | 1.59 |
| Draw | 19.9% | 5.02 |
| Hamburger SV win | 17.1% | 5.85 |

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
| 1 | 2-1 | 10.84% |
| 2 | 1-1 | 9.00% |
| 3 | 2-0 | 8.95% |
| 4 | 3-1 | 7.55% |
| 5 | 1-0 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 63.0% | 69.3% | 1.49 | -6.2% |
| Draw | 19.9% | 17.1% | 5.40 | +7.6% |
| Hamburger SV win | 17.1% | 13.6% | 7.40 | +26.5% |
| Over 2.5 | 65.4% | 69.5% | 1.40 | -8.5% |
| Under 2.5 | 34.6% | 30.5% | 3.00 | +3.9% |

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
| Market best home last update utc | 2026-10-09T08:10:54Z |
| Market best draw last update utc | 2026-10-09T08:10:55Z |
| Market best away last update utc | 2026-10-09T08:10:55Z |
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
| Fair Under 0.5 odds | 24.58 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.92 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.39 |
| Reference draw odds | 4.90 |
| Reference away odds | 6.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -6.3% |
| Draw probability edge | +2.9% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | -0.1269 |
| Raw ev home | -0.1562 |
| Raw edge prob draw | 0.0574 |
| Raw ev draw | 0.2310 |
| Raw edge prob away | 0.0696 |
| Raw ev away | 0.5225 |

</details>


---

## 2026-10-10 — Union Berlin vs Elversberg

The model's most likely 1X2 outcome is **Elversberg win** at **49.9%**. Expected goals are 1.17 for Union Berlin and 2.48 for Elversberg (3.65 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 68.9%; Under 4.5 goals: 71.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 28.4% | 3.52 |
| Draw | 21.7% | 4.61 |
| Elversberg win | 49.9% | 2.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 1.17 |
| Elversberg expected goals | 2.48 |
| Expected total goals | 3.65 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 68.9% |
| Under 2.5 | 31.1% |
| Over 3.5 | 47.3% |
| Under 3.5 | 52.7% |
| Over 4.5 | 28.6% |
| Under 4.5 | 71.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.36% |
| 2 | 2-1 | 8.10% |
| 3 | 1-2 | 7.16% |
| 4 | 0-2 | 6.14% |
| 5 | 2-2 | 6.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 28.4% | 41.3% | 2.42 | -31.3% |
| Draw | 21.7% | 24.1% | 3.96 | -14.2% |
| Elversberg win | 49.9% | 34.6% | 2.98 | +48.8% |
| Over 2.5 | 68.9% | 61.3% | 1.57 | +8.2% |
| Under 2.5 | 31.1% | 38.7% | 2.52 | -21.7% |

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
| Market best home last update utc | 2026-10-09T08:10:55Z |
| Market best draw last update utc | 2026-10-09T08:10:54Z |
| Market best away last update utc | 2026-10-09T08:10:55Z |
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
| Fair Under 0.5 odds | 26.22 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.12 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.22 |
| Fair Over 3.5 odds | 2.11 |
| Fair Under 3.5 odds | 1.90 |
| Fair Over 4.5 odds | 3.50 |
| Fair Under 4.5 odds | 1.40 |
| Unadjusted home-win probability | 15.4% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 65.3% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.5% |
| Raw p btts yes | 63.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.25 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.65 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -13.0% |
| Draw probability edge | -2.4% |
| Away probability edge | +15.3% |
| Over 2.5 probability edge | +7.6% |
| Under 2.5 probability edge | -7.6% |
| Raw edge prob home | -0.2594 |
| Raw ev home | -0.6272 |
| Raw edge prob draw | -0.0476 |
| Raw ev draw | -0.2359 |
| Raw edge prob away | 0.3070 |
| Raw ev away | 0.9459 |

</details>


---

## 2026-10-11 — 1. FC Köln vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **1. FC Köln win** at **41.0%**. Expected goals are 1.43 for 1. FC Köln and 1.55 for Borussia Monchengladbach (2.97 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.9%; Under 4.5 goals: 81.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 41.0% | 2.44 |
| Draw | 24.4% | 4.09 |
| Borussia Monchengladbach win | 34.6% | 2.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.43 |
| Borussia Monchengladbach expected goals | 1.55 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 57.9% |
| Under 2.5 | 42.1% |
| Over 3.5 | 34.8% |
| Under 3.5 | 65.2% |
| Over 4.5 | 18.4% |
| Under 4.5 | 81.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.39% |
| 2 | 2-1 | 9.72% |
| 3 | 1-2 | 7.67% |
| 4 | 1-0 | 7.38% |
| 5 | 2-0 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 41.0% | 48.1% | 2.10 | -13.9% |
| Draw | 24.4% | 22.1% | 4.15 | +1.4% |
| Borussia Monchengladbach win | 34.6% | 29.7% | 3.50 | +20.9% |
| Over 2.5 | 57.9% | 65.2% | 1.50 | -13.1% |
| Under 2.5 | 42.1% | 34.8% | 2.67 | +12.4% |

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
| Market best home last update utc | 2026-10-09T08:10:08Z |
| Market best draw last update utc | 2026-10-09T08:10:54Z |
| Market best away last update utc | 2026-10-09T08:10:55Z |
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
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.40 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.25 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.38 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.45 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 33.9% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 39.4% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 61.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.96 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.05 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.67 |
| Home probability edge | -7.1% |
| Draw probability edge | +2.3% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.1419 |
| Raw ev home | -0.2877 |
| Raw edge prob draw | 0.0458 |
| Raw ev draw | 0.1091 |
| Raw edge prob away | 0.0961 |
| Raw ev away | 0.3775 |

</details>


---

## 2026-10-11 — SC Freiburg vs FC Schalke 04

The model's most likely 1X2 outcome is **SC Freiburg win** at **47.3%**. Expected goals are 0.90 for SC Freiburg and 0.80 for FC Schalke 04 (1.70 combined). The most likely exact score is 1-0 at 20.7%. Goal-market probabilities: at least one goal: 84.4%; Over 2.5 goals: 26.5%; Under 4.5 goals: 96.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 47.3% | 2.11 |
| Draw | 29.2% | 3.42 |
| FC Schalke 04 win | 23.4% | 4.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 0.90 |
| FC Schalke 04 expected goals | 0.80 |
| Expected total goals | 1.70 |
| Over 0.5 | 84.4% |
| Under 0.5 | 15.6% |
| Over 1.5 | 53.0% |
| Under 1.5 | 47.0% |
| Over 2.5 | 26.5% |
| Under 2.5 | 73.5% |
| Over 3.5 | 9.7% |
| Under 3.5 | 90.3% |
| Over 4.5 | 3.3% |
| Under 4.5 | 96.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.72% |
| 2 | 0-0 | 15.61% |
| 3 | 1-1 | 11.58% |
| 4 | 0-1 | 10.72% |
| 5 | 2-0 | 10.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 47.3% | 60.5% | 1.71 | -19.0% |
| Draw | 29.2% | 21.8% | 4.40 | +28.6% |
| FC Schalke 04 win | 23.4% | 17.8% | 5.60 | +31.2% |
| Over 2.5 | 26.5% | 58.5% | 1.69 | -55.3% |
| Under 2.5 | 73.5% | 41.5% | 2.48 | +82.4% |

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
| Market best home last update utc | 2026-10-09T08:10:54Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:10:55Z |
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
| P btts yes | 32.6% |
| P btts no | 67.4% |
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.41 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.13 |
| Fair Over 2.5 odds | 3.78 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 10.30 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.42 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 34.2% |
| Unadjusted draw probability | 36.7% |
| Unadjusted away-win probability | 29.1% |
| Raw p over 1 5 | 52.1% |
| Raw p under 3 5 | 90.6% |
| Raw p btts yes | 34.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.80 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.36 |
| Home probability edge | -13.1% |
| Draw probability edge | +7.5% |
| Away probability edge | +5.6% |
| Over 2.5 probability edge | -32.0% |
| Under 2.5 probability edge | +32.0% |
| Raw edge prob home | -0.2622 |
| Raw ev home | -0.4146 |
| Raw edge prob draw | 0.1496 |
| Raw ev draw | 0.6155 |
| Raw edge prob away | 0.1125 |
| Raw ev away | 0.6269 |

</details>


---

## 2026-10-16 — Eintracht Frankfurt vs 1. FC Köln

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **56.4%**. Expected goals are 2.20 for Eintracht Frankfurt and 1.06 for 1. FC Köln (3.26 combined). The most likely exact score is 1-1 at 9.9%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 62.8%; Under 4.5 goals: 77.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 56.4% | 1.77 |
| Draw | 21.5% | 4.65 |
| 1. FC Köln win | 22.1% | 4.53 |

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
| Over 3.5 | 40.3% |
| Under 3.5 | 59.7% |
| Over 4.5 | 22.6% |
| Under 4.5 | 77.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.91% |
| 2 | 2-1 | 8.92% |
| 3 | 2-0 | 8.43% |
| 4 | 1-0 | 6.82% |
| 5 | 3-1 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 56.4% | 50.5% | 2.00 | +12.9% |
| Draw | 21.5% | 21.5% | 4.30 | -7.6% |
| 1. FC Köln win | 22.1% | 27.9% | 3.65 | -19.4% |
| Over 2.5 | 62.8% | 69.5% | 1.40 | -12.0% |
| Under 2.5 | 37.2% | 30.5% | 3.00 | +11.5% |

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
| Market best home last update utc | 2026-10-09T08:10:54Z |
| Market best draw last update utc | 2026-10-09T08:10:54Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
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
| P btts yes | 59.5% |
| P btts no | 40.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.86 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.80 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.00 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +5.9% |
| Draw probability edge | -0.0% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -6.7% |
| Under 2.5 probability edge | +6.7% |
| Raw edge prob home | 0.1179 |
| Raw ev home | 0.2465 |
| Raw edge prob draw | -0.0010 |
| Raw ev draw | -0.0776 |
| Raw edge prob away | -0.1170 |
| Raw ev away | -0.4078 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **75.4%**. Expected goals are 2.79 for Bayern Munich and 1.24 for RB Leipzig (4.02 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 78.1%; Under 4.5 goals: 61.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 75.4% | 1.33 |
| Draw | 13.3% | 7.50 |
| RB Leipzig win | 11.2% | 8.91 |

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
| Over 2.5 | 78.1% |
| Under 2.5 | 21.9% |
| Over 3.5 | 58.1% |
| Under 3.5 | 41.9% |
| Over 4.5 | 38.9% |
| Under 4.5 | 61.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.38% |
| 2 | 3-1 | 8.71% |
| 3 | 2-0 | 7.59% |
| 4 | 3-0 | 7.05% |
| 5 | 4-1 | 6.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 75.4% | 81.8% | 1.27 | -4.2% |
| Draw | 13.3% | 9.6% | 8.00 | +6.6% |
| RB Leipzig win | 11.2% | 8.7% | 11.20 | +25.7% |
| Over 2.5 | 78.1% | 83.2% | 1.18 | -7.9% |
| Under 2.5 | 21.9% | 16.8% | 5.01 | +9.9% |

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
| Market best home last update utc | 2026-10-09T08:10:54Z |
| Market best draw last update utc | 2026-10-09T08:10:06Z |
| Market best away last update utc | 2026-10-09T08:10:54Z |
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
| P btts yes | 66.0% |
| P btts no | 34.0% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 52.66 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.62 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.56 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.17 |
| Reference draw odds | 6.25 |
| Reference away odds | 6.75 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.18 |
| Reference Under 2.5 odds | 5.01 |
| Home probability edge | -6.3% |
| Draw probability edge | +3.8% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.1266 |
| Raw ev home | -0.1222 |
| Raw edge prob draw | 0.0754 |
| Raw ev draw | 0.3676 |
| Raw edge prob away | 0.0513 |
| Raw ev away | 0.5445 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **56.1%**. Expected goals are 2.96 for Elversberg and 1.17 for Augsburg (4.13 combined). The most likely exact score is 1-1 at 7.6%. Goal-market probabilities: at least one goal: 97.3%; Over 2.5 goals: 75.8%; Under 4.5 goals: 63.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 56.1% | 1.78 |
| Draw | 19.2% | 5.20 |
| Augsburg win | 24.7% | 4.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 2.96 |
| Augsburg expected goals | 1.17 |
| Expected total goals | 4.13 |
| Over 0.5 | 97.3% |
| Under 0.5 | 2.7% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 75.8% |
| Under 2.5 | 24.2% |
| Over 3.5 | 56.1% |
| Under 3.5 | 43.9% |
| Over 4.5 | 36.9% |
| Under 4.5 | 63.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.64% |
| 2 | 1-2 | 7.06% |
| 3 | 2-1 | 6.32% |
| 4 | 3-1 | 6.24% |
| 5 | 2-2 | 5.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 56.1% | 39.0% | 2.55 | +43.0% |
| Draw | 19.2% | 23.0% | 4.00 | -23.1% |
| Augsburg win | 24.7% | 38.0% | 2.80 | -30.8% |
| Over 2.5 | 75.8% | 65.9% | 1.47 | +11.4% |
| Under 2.5 | 24.2% | 34.1% | 2.71 | -34.4% |

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
| Market best home last update utc | 2026-10-09T08:10:54Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
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
| P btts yes | 68.6% |
| P btts no | 31.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.69 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.42 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.13 |
| Fair Over 3.5 odds | 1.78 |
| Fair Under 3.5 odds | 2.28 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.25 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.30 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Home probability edge | +17.1% |
| Draw probability edge | -3.8% |
| Away probability edge | -13.3% |
| Over 2.5 probability edge | +9.8% |
| Under 2.5 probability edge | -9.8% |
| Raw edge prob home | 0.3415 |
| Raw ev home | 0.8655 |
| Raw edge prob draw | -0.0751 |
| Raw ev draw | -0.3813 |
| Raw edge prob away | -0.2664 |
| Raw ev away | -0.6814 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FC Schalke 04 win** at **35.0%**. Expected goals are 0.87 for FC Schalke 04 and 0.69 for FSV Mainz 05 (1.56 combined). The most likely exact score is 0-0 at 18.2%. Goal-market probabilities: at least one goal: 81.8%; Over 2.5 goals: 22.3%; Under 4.5 goals: 97.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 35.0% | 2.86 |
| Draw | 31.2% | 3.21 |
| FSV Mainz 05 win | 33.8% | 2.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| FSV Mainz 05 expected goals | 0.69 |
| Expected total goals | 1.56 |
| Over 0.5 | 81.8% |
| Under 0.5 | 18.2% |
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
| 1 | 0-0 | 18.20% |
| 2 | 0-1 | 17.41% |
| 3 | 1-0 | 16.44% |
| 4 | 1-1 | 11.34% |
| 5 | 2-0 | 7.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 35.0% | 33.7% | 3.00 | +5.0% |
| Draw | 31.2% | 24.1% | 3.80 | +18.5% |
| FSV Mainz 05 win | 33.8% | 42.2% | 2.44 | -17.5% |
| Over 2.5 | 22.3% | 59.5% | 1.66 | -63.0% |
| Under 2.5 | 77.7% | 40.5% | 2.42 | +88.0% |

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
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:10:54Z |
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
| P btts yes | 29.0% |
| P btts no | 71.0% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.50 |
| Fair Over 1.5 odds | 2.09 |
| Fair Under 1.5 odds | 1.92 |
| Fair Over 2.5 odds | 4.48 |
| Fair Under 2.5 odds | 1.29 |
| Fair Over 3.5 odds | 13.36 |
| Fair Under 3.5 odds | 1.08 |
| Fair Over 4.5 odds | 42.77 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 36.3% |
| Unadjusted draw probability | 38.3% |
| Unadjusted away-win probability | 25.4% |
| Raw p over 1 5 | 47.5% |
| Raw p under 3 5 | 92.7% |
| Raw p btts yes | 30.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.55 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.10 |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | +1.3% |
| Draw probability edge | +7.1% |
| Away probability edge | -8.4% |
| Over 2.5 probability edge | -37.2% |
| Under 2.5 probability edge | +37.2% |
| Raw edge prob home | 0.0261 |
| Raw ev home | 0.0888 |
| Raw edge prob draw | 0.1415 |
| Raw ev draw | 0.4539 |
| Raw edge prob away | -0.1677 |
| Raw ev away | -0.3791 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **55.6%**. Expected goals are 1.11 for Hamburger SV and 2.02 for VfB Stuttgart (3.13 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 60.8%; Under 4.5 goals: 79.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 22.3% | 4.49 |
| Draw | 22.2% | 4.51 |
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
| 1 | 1-1 | 10.30% |
| 2 | 1-2 | 9.59% |
| 3 | 0-2 | 8.64% |
| 4 | 0-1 | 7.57% |
| 5 | 1-3 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 22.3% | 25.2% | 4.25 | -5.3% |
| Draw | 22.2% | 21.0% | 4.35 | -3.6% |
| VfB Stuttgart win | 55.6% | 53.8% | 1.90 | +5.6% |
| Over 2.5 | 60.8% | 70.6% | 1.38 | -16.0% |
| Under 2.5 | 39.2% | 29.4% | 3.10 | +21.4% |

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
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:10:37Z |
| Market best away last update utc | 2026-10-09T08:10:54Z |
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
| Fair Under 0.5 odds | 19.48 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.25 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.70 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | -2.9% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.0586 |
| Raw ev home | -0.1772 |
| Raw edge prob draw | 0.0231 |
| Raw ev draw | 0.0140 |
| Raw edge prob away | 0.0355 |
| Raw ev away | 0.0893 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **60.0%**. Expected goals are 0.94 for Union Berlin and 1.92 for Borussia Dortmund (2.87 combined). The most likely exact score is 0-2 at 10.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 55.2%; Under 4.5 goals: 83.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.8% | 5.63 |
| Draw | 22.2% | 4.51 |
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
| 1 | 0-2 | 10.68% |
| 2 | 1-1 | 10.58% |
| 3 | 1-2 | 10.05% |
| 4 | 0-1 | 10.01% |
| 5 | 0-3 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.8% | 18.7% | 5.40 | -4.1% |
| Draw | 22.2% | 20.5% | 4.50 | -0.2% |
| Borussia Dortmund win | 60.0% | 60.8% | 1.73 | +3.9% |
| Over 2.5 | 55.2% | 65.2% | 1.49 | -17.7% |
| Under 2.5 | 44.8% | 34.8% | 2.70 | +20.8% |

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
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:10:06Z |
| Market best away last update utc | 2026-10-09T08:10:54Z |
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
| Fair Under 0.5 odds | 15.90 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.80 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.10 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.52 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.67 |
| Home probability edge | -0.9% |
| Draw probability edge | +1.7% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | -0.0189 |
| Raw ev home | -0.0916 |
| Raw edge prob draw | 0.0341 |
| Raw ev draw | 0.0751 |
| Raw edge prob away | -0.0152 |
| Raw ev away | 0.0257 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **49.2%**. Expected goals are 1.16 for Werder Bremen and 0.74 for SC Paderborn (1.91 combined). The most likely exact score is 1-0 at 17.7%. Goal-market probabilities: at least one goal: 86.5%; Over 2.5 goals: 31.6%; Under 4.5 goals: 95.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 49.2% | 2.03 |
| Draw | 27.8% | 3.60 |
| SC Paderborn win | 23.0% | 4.34 |

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
| 1 | 1-0 | 17.66% |
| 2 | 0-0 | 13.46% |
| 3 | 1-1 | 11.77% |
| 4 | 2-0 | 11.15% |
| 5 | 0-1 | 10.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 49.2% | 53.9% | 1.91 | -6.1% |
| Draw | 27.8% | 22.1% | 4.26 | +18.3% |
| SC Paderborn win | 23.0% | 24.0% | 4.25 | -2.1% |
| Over 2.5 | 31.6% | 62.1% | 1.56 | -50.7% |
| Under 2.5 | 68.4% | 37.9% | 2.47 | +69.0% |

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
| Market best home last update utc | 2026-10-09T08:10:37Z |
| Market best draw last update utc | 2026-10-09T08:10:54Z |
| Market best away last update utc | 2026-10-09T08:09:50Z |
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
| Fair Under 0.5 odds | 7.43 |
| Fair Over 1.5 odds | 1.70 |
| Fair Under 1.5 odds | 2.43 |
| Fair Over 2.5 odds | 3.17 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.71 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.93 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 44.5% |
| Unadjusted draw probability | 33.4% |
| Unadjusted away-win probability | 22.1% |
| Raw p over 1 5 | 58.1% |
| Raw p under 3 5 | 87.4% |
| Raw p btts yes | 37.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.70 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.40 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.47 |
| Home probability edge | -4.7% |
| Draw probability edge | +5.7% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -30.5% |
| Under 2.5 probability edge | +30.5% |
| Raw edge prob home | -0.0937 |
| Raw ev home | -0.1500 |
| Raw edge prob draw | 0.1132 |
| Raw ev draw | 0.4242 |
| Raw edge prob away | -0.0195 |
| Raw ev away | -0.0621 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **64.2%**. Expected goals are 2.44 for Bayer Leverkusen and 0.96 for SC Freiburg (3.41 combined). The most likely exact score is 2-0 at 9.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 65.6%; Under 4.5 goals: 74.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 64.2% | 1.56 |
| Draw | 19.4% | 5.16 |
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
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.5% |
| Under 3.5 | 56.5% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.21% |
| 2 | 1-1 | 8.91% |
| 3 | 2-1 | 8.87% |
| 4 | 3-0 | 7.50% |
| 5 | 3-1 | 7.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 64.2% | 59.4% | 1.70 | +9.2% |
| Draw | 19.4% | 20.0% | 4.60 | -10.9% |
| SC Freiburg win | 16.4% | 20.6% | 4.83 | -20.8% |
| Over 2.5 | 65.6% | 65.2% | 1.49 | -2.3% |
| Under 2.5 | 34.4% | 34.8% | 2.67 | -8.0% |

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
| Market best home last update utc | 2026-10-09T08:10:54Z |
| Market best draw last update utc | 2026-10-09T08:10:23Z |
| Market best away last update utc | 2026-10-09T08:10:54Z |
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
| Fair Under 0.5 odds | 23.40 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.01 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.85 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.67 |
| Home probability edge | +4.8% |
| Draw probability edge | -0.6% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.0968 |
| Raw ev home | 0.1743 |
| Raw edge prob draw | -0.0126 |
| Raw ev draw | -0.1381 |
| Raw edge prob away | -0.0842 |
| Raw ev away | -0.4114 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **42.7%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-2 at 9.0%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 72.1%; Under 4.5 goals: 68.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 34.9% | 2.87 |
| Draw | 22.4% | 4.47 |
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
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 51.1% |
| Under 3.5 | 48.9% |
| Over 4.5 | 31.9% |
| Under 4.5 | 68.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.99% |
| 2 | 1-1 | 8.90% |
| 3 | 2-2 | 6.98% |
| 4 | 2-1 | 6.83% |
| 5 | 1-3 | 5.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 34.9% | 28.5% | 3.58 | +24.9% |
| Draw | 22.4% | 21.6% | 4.26 | -4.6% |
| TSG Hoffenheim win | 42.7% | 49.9% | 2.00 | -14.6% |
| Over 2.5 | 72.1% | 69.5% | 1.40 | +1.0% |
| Under 2.5 | 27.9% | 30.5% | 3.00 | -16.4% |

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
| Market best home last update utc | 2026-10-09T08:10:54Z |
| Market best draw last update utc | 2026-10-09T08:10:54Z |
| Market best away last update utc | 2026-10-09T08:10:37Z |
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
| Fair Under 0.5 odds | 31.59 |
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
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.82 |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +6.4% |
| Draw probability edge | +0.8% |
| Away probability edge | -7.2% |
| Over 2.5 probability edge | +2.6% |
| Under 2.5 probability edge | -2.6% |
| Raw edge prob home | 0.1278 |
| Raw ev home | 0.4780 |
| Raw edge prob draw | 0.0164 |
| Raw ev draw | -0.0111 |
| Raw edge prob away | -0.1442 |
| Raw ev away | -0.2899 |

</details>


---
