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

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **71.1%**. Expected goals are 2.30 for Borussia Dortmund and 0.97 for Werder Bremen (3.27 combined). The most likely exact score is 2-0 at 10.8%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 64.9%; Under 4.5 goals: 76.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 71.1% | 1.41 |
| Draw | 17.3% | 5.78 |
| Werder Bremen win | 11.6% | 8.60 |

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
| 1 | 2-0 | 10.76% |
| 2 | 2-1 | 10.44% |
| 3 | 1-0 | 8.39% |
| 4 | 3-0 | 8.26% |
| 5 | 1-1 | 8.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 71.1% | 75.8% | 1.37 | -2.6% |
| Draw | 17.3% | 14.5% | 6.25 | +8.1% |
| Werder Bremen win | 11.6% | 9.7% | 10.00 | +16.2% |
| Over 2.5 | 64.9% | 70.8% | 1.40 | -9.2% |
| Under 2.5 | 35.1% | 29.2% | 3.00 | +5.4% |

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
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.90 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.28 |
| Reference draw odds | 5.60 |
| Reference away odds | 8.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -4.7% |
| Draw probability edge | +2.8% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | -0.0946 |
| Raw ev home | -0.0909 |
| Raw edge prob draw | 0.0562 |
| Raw ev draw | 0.2565 |
| Raw edge prob away | 0.0384 |
| Raw ev away | 0.3541 |

</details>


---

## 2026-10-10 — Augsburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **78.5%**. Expected goals are 1.04 for Augsburg and 2.87 for Bayern Munich (3.92 combined). The most likely exact score is 1-2 at 9.1%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 76.1%; Under 4.5 goals: 63.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 8.5% | 11.83 |
| Draw | 13.1% | 7.65 |
| Bayern Munich win | 78.5% | 1.27 |

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
| 1 | 1-2 | 9.06% |
| 2 | 1-3 | 8.68% |
| 3 | 0-2 | 8.67% |
| 4 | 0-3 | 8.31% |
| 5 | 1-4 | 6.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 8.5% | 6.7% | 13.80 | +16.6% |
| Draw | 13.1% | 10.7% | 9.80 | +28.1% |
| Bayern Munich win | 78.5% | 82.7% | 1.23 | -3.5% |
| Over 2.5 | 76.1% | 85.4% | 1.16 | -11.7% |
| Under 2.5 | 23.9% | 14.6% | 5.50 | +31.5% |

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
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | GTbets |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Augsburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.38 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.39 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.18 |
| Fair Over 3.5 odds | 1.79 |
| Fair Under 3.5 odds | 2.26 |
| Fair Over 4.5 odds | 2.74 |
| Fair Under 4.5 odds | 1.57 |
| Unadjusted home-win probability | 10.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 10.50 |
| Reference draw odds | 7.00 |
| Reference away odds | 1.18 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.50 |
| Home probability edge | +1.8% |
| Draw probability edge | +2.4% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | 0.0354 |
| Raw ev home | 0.4103 |
| Raw edge prob draw | 0.0483 |
| Raw ev draw | 0.5173 |
| Raw edge prob away | -0.0836 |
| Raw ev away | -0.0861 |

</details>


---

## 2026-10-10 — FSV Mainz 05 vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **48.6%**. Expected goals are 1.08 for FSV Mainz 05 and 1.81 for Bayer Leverkusen (2.89 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 55.3%; Under 4.5 goals: 83.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 27.0% | 3.70 |
| Draw | 24.4% | 4.10 |
| Bayer Leverkusen win | 48.6% | 2.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.08 |
| Bayer Leverkusen expected goals | 1.81 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.3% |
| Under 2.5 | 44.7% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.57% |
| 2 | 1-2 | 8.93% |
| 3 | 0-2 | 8.30% |
| 4 | 0-1 | 8.12% |
| 5 | 2-1 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 27.0% | 32.8% | 3.10 | -16.3% |
| Draw | 24.4% | 23.6% | 4.20 | +2.5% |
| Bayer Leverkusen win | 48.6% | 43.7% | 2.31 | +12.3% |
| Over 2.5 | 55.3% | 66.7% | 1.45 | -19.8% |
| Under 2.5 | 44.7% | 33.3% | 2.80 | +25.2% |

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
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Tipico |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Mainz |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.15 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | -5.8% |
| Draw probability edge | +0.8% |
| Away probability edge | +5.0% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | -0.1160 |
| Raw ev home | -0.3429 |
| Raw edge prob draw | 0.0169 |
| Raw ev draw | 0.0606 |
| Raw edge prob away | 0.0990 |
| Raw ev away | 0.2370 |

</details>


---

## 2026-10-10 — RB Leipzig vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **RB Leipzig win** at **59.3%**. Expected goals are 2.13 for RB Leipzig and 1.35 for Eintracht Frankfurt (3.48 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 68.3%; Under 4.5 goals: 72.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 59.3% | 1.69 |
| Draw | 20.7% | 4.84 |
| Eintracht Frankfurt win | 20.0% | 5.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.13 |
| Eintracht Frankfurt expected goals | 1.35 |
| Expected total goals | 3.48 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.3% |
| Under 2.5 | 31.7% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.27% |
| 2 | 1-1 | 8.96% |
| 3 | 2-0 | 7.63% |
| 4 | 3-1 | 7.30% |
| 5 | 1-0 | 6.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 59.3% | 64.1% | 1.61 | -4.5% |
| Draw | 20.7% | 18.8% | 5.20 | +7.5% |
| Eintracht Frankfurt win | 20.0% | 17.1% | 5.40 | +8.1% |
| Over 2.5 | 68.3% | 75.6% | 1.30 | -11.2% |
| Under 2.5 | 31.7% | 24.4% | 3.60 | +14.1% |

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
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.23 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.91 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.16 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.62 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 54.5% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 22.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.50 |
| Reference draw odds | 4.60 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.60 |
| Home probability edge | -4.8% |
| Draw probability edge | +1.9% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | -7.2% |
| Under 2.5 probability edge | +7.2% |
| Raw edge prob home | -0.0961 |
| Raw ev home | -0.1225 |
| Raw edge prob draw | 0.0382 |
| Raw ev draw | 0.1746 |
| Raw edge prob away | 0.0578 |
| Raw ev away | 0.2369 |

</details>


---

## 2026-10-10 — SC Paderborn vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **56.4%**. Expected goals are 0.76 for SC Paderborn and 1.42 for VfB Stuttgart (2.18 combined). The most likely exact score is 0-1 at 16.2%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 39.0%; Under 4.5 goals: 92.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 18.6% | 5.37 |
| Draw | 25.0% | 4.00 |
| VfB Stuttgart win | 56.4% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.76 |
| VfB Stuttgart expected goals | 1.42 |
| Expected total goals | 2.18 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
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
| 1 | 0-1 | 16.16% |
| 2 | 0-2 | 12.49% |
| 3 | 1-1 | 11.31% |
| 4 | 0-0 | 10.55% |
| 5 | 1-2 | 9.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 18.6% | 18.5% | 5.30 | -1.2% |
| Draw | 25.0% | 20.2% | 4.90 | +22.4% |
| VfB Stuttgart win | 56.4% | 61.2% | 1.64 | -7.5% |
| Over 2.5 | 39.0% | 70.8% | 1.38 | -46.2% |
| Under 2.5 | 61.0% | 29.2% | 3.10 | +89.1% |

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
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.48 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 4.60 |
| Reference draw odds | 4.25 |
| Reference away odds | 1.56 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | +0.1% |
| Draw probability edge | +4.7% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -31.8% |
| Under 2.5 probability edge | +31.8% |
| Raw edge prob home | 0.0017 |
| Raw ev home | -0.0077 |
| Raw edge prob draw | 0.0948 |
| Raw ev draw | 0.4566 |
| Raw edge prob away | -0.0966 |
| Raw ev away | -0.1546 |

</details>


---

## 2026-10-10 — TSG Hoffenheim vs Hamburger SV

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **62.8%**. Expected goals are 2.09 for TSG Hoffenheim and 1.21 for Hamburger SV (3.30 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 65.3%; Under 4.5 goals: 75.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 62.8% | 1.59 |
| Draw | 20.1% | 4.98 |
| Hamburger SV win | 17.1% | 5.85 |

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
| 1 | 2-1 | 10.81% |
| 2 | 1-1 | 9.06% |
| 3 | 2-0 | 8.93% |
| 4 | 3-1 | 7.54% |
| 5 | 1-0 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 62.8% | 69.0% | 1.49 | -6.4% |
| Draw | 20.1% | 17.4% | 5.40 | +8.4% |
| Hamburger SV win | 17.1% | 13.6% | 7.40 | +26.6% |
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
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.40 |
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
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.40 |
| Reference draw odds | 4.90 |
| Reference away odds | 6.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -6.2% |
| Draw probability edge | +2.7% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | -0.1239 |
| Raw ev home | -0.1562 |
| Raw edge prob draw | 0.0544 |
| Raw ev draw | 0.2310 |
| Raw edge prob away | 0.0694 |
| Raw ev away | 0.5225 |

</details>


---

## 2026-10-10 — Union Berlin vs Elversberg

The model's most likely 1X2 outcome is **Elversberg win** at **49.0%**. Expected goals are 1.17 for Union Berlin and 2.48 for Elversberg (3.65 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 68.7%; Under 4.5 goals: 71.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 28.9% | 3.46 |
| Draw | 22.1% | 4.53 |
| Elversberg win | 49.0% | 2.04 |

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
| Over 3.5 | 47.2% |
| Under 3.5 | 52.8% |
| Over 4.5 | 28.5% |
| Under 4.5 | 71.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.54% |
| 2 | 2-1 | 8.26% |
| 3 | 1-2 | 7.02% |
| 4 | 2-2 | 6.24% |
| 5 | 0-2 | 6.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 28.9% | 42.5% | 2.42 | -30.0% |
| Draw | 22.1% | 24.9% | 3.96 | -12.6% |
| Elversberg win | 49.0% | 32.7% | 2.96 | +45.0% |
| Over 2.5 | 68.7% | 61.3% | 1.57 | +7.9% |
| Under 2.5 | 31.3% | 38.7% | 2.52 | -21.2% |

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
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.73 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.08 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.12 |
| Fair Under 3.5 odds | 1.89 |
| Fair Over 4.5 odds | 3.51 |
| Fair Under 4.5 odds | 1.40 |
| Unadjusted home-win probability | 15.4% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 65.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.80 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -13.5% |
| Draw probability edge | -2.8% |
| Away probability edge | +16.3% |
| Over 2.5 probability edge | +7.4% |
| Under 2.5 probability edge | -7.4% |
| Raw edge prob home | -0.2705 |
| Raw ev home | -0.6272 |
| Raw edge prob draw | -0.0557 |
| Raw ev draw | -0.2359 |
| Raw edge prob away | 0.3262 |
| Raw ev away | 0.9328 |

</details>


---

## 2026-10-11 — 1. FC Köln vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **1. FC Köln win** at **40.9%**. Expected goals are 1.43 for 1. FC Köln and 1.55 for Borussia Monchengladbach (2.97 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.8%; Under 4.5 goals: 81.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 40.9% | 2.44 |
| Draw | 24.8% | 4.03 |
| Borussia Monchengladbach win | 34.2% | 2.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.43 |
| Borussia Monchengladbach expected goals | 1.55 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 57.8% |
| Under 2.5 | 42.2% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.3% |
| Under 4.5 | 81.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.58% |
| 2 | 2-1 | 9.70% |
| 3 | 1-2 | 7.59% |
| 4 | 1-0 | 7.37% |
| 5 | 2-0 | 6.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 40.9% | 48.0% | 2.12 | -13.2% |
| Draw | 24.8% | 23.0% | 4.15 | +3.1% |
| Borussia Monchengladbach win | 34.2% | 29.1% | 3.42 | +17.0% |
| Over 2.5 | 57.8% | 63.8% | 1.51 | -12.8% |
| Under 2.5 | 42.2% | 36.2% | 2.61 | +10.3% |

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
| Odds bookmakers 1x2 | 21.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Betfair |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | FC Koln |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.11 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.47 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 33.9% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 39.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.96 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -7.0% |
| Draw probability edge | +1.9% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | -0.1405 |
| Raw ev home | -0.2809 |
| Raw edge prob draw | 0.0377 |
| Raw ev draw | 0.1091 |
| Raw edge prob away | 0.1028 |
| Raw ev away | 0.3460 |

</details>


---

## 2026-10-11 — SC Freiburg vs FC Schalke 04

The model's most likely 1X2 outcome is **SC Freiburg win** at **47.0%**. Expected goals are 0.90 for SC Freiburg and 0.80 for FC Schalke 04 (1.70 combined). The most likely exact score is 1-0 at 20.6%. Goal-market probabilities: at least one goal: 84.5%; Over 2.5 goals: 26.5%; Under 4.5 goals: 96.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 47.0% | 2.13 |
| Draw | 29.0% | 3.44 |
| FC Schalke 04 win | 23.9% | 4.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 0.90 |
| FC Schalke 04 expected goals | 0.80 |
| Expected total goals | 1.70 |
| Over 0.5 | 84.5% |
| Under 0.5 | 15.5% |
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
| 1 | 1-0 | 20.58% |
| 2 | 0-0 | 15.50% |
| 3 | 1-1 | 11.50% |
| 4 | 0-1 | 10.96% |
| 5 | 2-0 | 10.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 47.0% | 59.8% | 1.71 | -19.6% |
| Draw | 29.0% | 21.4% | 4.40 | +27.8% |
| FC Schalke 04 win | 23.9% | 18.8% | 5.60 | +34.1% |
| Over 2.5 | 26.5% | 61.2% | 1.69 | -55.2% |
| Under 2.5 | 73.5% | 38.8% | 2.46 | +80.8% |

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
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.45 |
| Fair Over 1.5 odds | 1.89 |
| Fair Under 1.5 odds | 2.13 |
| Fair Over 2.5 odds | 3.77 |
| Fair Under 2.5 odds | 1.36 |
| Fair Over 3.5 odds | 10.30 |
| Fair Under 3.5 odds | 1.11 |
| Fair Over 4.5 odds | 30.36 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 34.2% |
| Unadjusted draw probability | 36.7% |
| Unadjusted away-win probability | 29.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.60 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.60 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.38 |
| Home probability edge | -12.8% |
| Draw probability edge | +7.7% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -34.6% |
| Under 2.5 probability edge | +34.6% |
| Raw edge prob home | -0.2557 |
| Raw ev home | -0.4146 |
| Raw edge prob draw | 0.1535 |
| Raw ev draw | 0.6155 |
| Raw edge prob away | 0.1022 |
| Raw ev away | 0.6269 |

</details>


---

## 2026-10-16 — Eintracht Frankfurt vs 1. FC Köln

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **56.8%**. Expected goals are 2.20 for Eintracht Frankfurt and 1.06 for 1. FC Köln (3.26 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 62.7%; Under 4.5 goals: 77.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 56.8% | 1.76 |
| Draw | 22.1% | 4.52 |
| 1. FC Köln win | 21.1% | 4.74 |

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
| 1 | 1-1 | 10.19% |
| 2 | 2-1 | 8.97% |
| 3 | 2-0 | 8.48% |
| 4 | 1-0 | 6.86% |
| 5 | 3-1 | 6.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 56.8% | 51.2% | 2.00 | +13.5% |
| Draw | 22.1% | 22.8% | 4.40 | -2.7% |
| 1. FC Köln win | 21.1% | 26.0% | 3.65 | -22.9% |
| Over 2.5 | 62.7% | 69.0% | 1.40 | -12.3% |
| Under 2.5 | 37.3% | 31.0% | 3.00 | +12.0% |

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
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Betfair |
| Best away bookmaker | Unibet (SE) |
| Best over 2 5 bookmaker | William Hill |
| Best under 2 5 bookmaker | Betsson |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 81/100 |
| Away-name matching confidence | 90/100 |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.29 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.30 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.48 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.44 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 62.3% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 16.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.85 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.45 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Home probability edge | +5.6% |
| Draw probability edge | -0.7% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.1110 |
| Raw ev home | 0.2465 |
| Raw edge prob draw | -0.0131 |
| Raw ev draw | -0.0562 |
| Raw edge prob away | -0.0979 |
| Raw ev away | -0.4078 |

</details>


---

## 2026-10-17 — Bayern Munich vs RB Leipzig

The model's most likely 1X2 outcome is **Bayern Munich win** at **75.5%**. Expected goals are 2.79 for Bayern Munich and 1.24 for RB Leipzig (4.02 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 77.9%; Under 4.5 goals: 61.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 75.5% | 1.32 |
| Draw | 13.9% | 7.21 |
| RB Leipzig win | 10.6% | 9.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.79 |
| RB Leipzig expected goals | 1.24 |
| Expected total goals | 4.02 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 92.1% |
| Under 1.5 | 7.9% |
| Over 2.5 | 77.9% |
| Under 2.5 | 22.1% |
| Over 3.5 | 58.1% |
| Under 3.5 | 41.9% |
| Over 4.5 | 38.8% |
| Under 4.5 | 61.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.39% |
| 2 | 3-1 | 8.72% |
| 3 | 2-0 | 7.60% |
| 4 | 3-0 | 7.06% |
| 5 | 4-1 | 6.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 75.5% | 81.9% | 1.27 | -4.1% |
| Draw | 13.9% | 10.7% | 8.00 | +11.0% |
| RB Leipzig win | 10.6% | 7.5% | 11.20 | +19.2% |
| Over 2.5 | 77.9% | 83.8% | 1.18 | -8.1% |
| Under 2.5 | 22.1% | 16.2% | 5.01 | +10.8% |

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
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 50.59 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.60 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.52 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.38 |
| Fair Over 4.5 odds | 2.58 |
| Fair Under 4.5 odds | 1.63 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 13.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.19 |
| Reference draw odds | 7.00 |
| Reference away odds | 9.50 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.17 |
| Reference Under 2.5 odds | 5.00 |
| Home probability edge | -6.4% |
| Draw probability edge | +3.2% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.1274 |
| Raw ev home | -0.1222 |
| Raw edge prob draw | 0.0644 |
| Raw ev draw | 0.3676 |
| Raw edge prob away | 0.0630 |
| Raw ev away | 0.5445 |

</details>


---

## 2026-10-17 — Elversberg vs Augsburg

The model's most likely 1X2 outcome is **Elversberg win** at **57.3%**. Expected goals are 2.96 for Elversberg and 1.17 for Augsburg (4.13 combined). The most likely exact score is 1-1 at 7.8%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 75.7%; Under 4.5 goals: 63.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 57.3% | 1.75 |
| Draw | 19.6% | 5.10 |
| Augsburg win | 23.1% | 4.32 |

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
| 1 | 1-1 | 7.79% |
| 2 | 1-2 | 6.61% |
| 3 | 2-1 | 6.45% |
| 4 | 3-1 | 6.37% |
| 5 | 2-2 | 6.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 57.3% | 41.4% | 2.55 | +46.0% |
| Draw | 19.6% | 23.7% | 4.00 | -21.6% |
| Augsburg win | 23.1% | 34.9% | 2.80 | -35.2% |
| Over 2.5 | 75.7% | 66.7% | 1.47 | +11.3% |
| Under 2.5 | 24.3% | 33.3% | 2.71 | -34.3% |

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
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.99 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.49 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.12 |
| Fair Over 3.5 odds | 1.77 |
| Fair Under 3.5 odds | 2.29 |
| Fair Over 4.5 odds | 2.70 |
| Fair Under 4.5 odds | 1.59 |
| Unadjusted home-win probability | 73.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 11.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.25 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.63 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | +15.9% |
| Draw probability edge | -4.1% |
| Away probability edge | -11.8% |
| Over 2.5 probability edge | +9.0% |
| Under 2.5 probability edge | -9.0% |
| Raw edge prob home | 0.3179 |
| Raw ev home | 0.8655 |
| Raw edge prob draw | -0.0826 |
| Raw ev draw | -0.3813 |
| Raw edge prob away | -0.2353 |
| Raw ev away | -0.6814 |

</details>


---

## 2026-10-17 — FC Schalke 04 vs FSV Mainz 05

The model's most likely 1X2 outcome is **FC Schalke 04 win** at **34.2%**. Expected goals are 0.87 for FC Schalke 04 and 0.69 for FSV Mainz 05 (1.56 combined). The most likely exact score is 0-0 at 18.6%. Goal-market probabilities: at least one goal: 81.4%; Over 2.5 goals: 22.1%; Under 4.5 goals: 97.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 34.2% | 2.92 |
| Draw | 31.8% | 3.15 |
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
| 1 | 0-0 | 18.55% |
| 2 | 0-1 | 17.50% |
| 3 | 1-0 | 16.07% |
| 4 | 1-1 | 11.56% |
| 5 | 2-0 | 7.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 34.2% | 32.1% | 3.00 | +2.6% |
| Draw | 31.8% | 25.3% | 3.80 | +20.8% |
| FSV Mainz 05 win | 34.0% | 42.5% | 2.44 | -17.1% |
| Over 2.5 | 22.1% | 60.2% | 1.66 | -63.2% |
| Under 2.5 | 77.9% | 39.8% | 2.42 | +88.4% |

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
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.39 |
| Fair Over 1.5 odds | 2.09 |
| Fair Under 1.5 odds | 1.92 |
| Fair Over 2.5 odds | 4.52 |
| Fair Under 2.5 odds | 1.28 |
| Fair Over 3.5 odds | 13.40 |
| Fair Under 3.5 odds | 1.08 |
| Fair Over 4.5 odds | 43.13 |
| Fair Under 4.5 odds | 1.02 |
| Unadjusted home-win probability | 36.3% |
| Unadjusted draw probability | 38.3% |
| Unadjusted away-win probability | 25.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.20 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.35 |
| Home probability edge | +2.1% |
| Draw probability edge | +6.5% |
| Away probability edge | -8.5% |
| Over 2.5 probability edge | -38.1% |
| Under 2.5 probability edge | +38.1% |
| Raw edge prob home | 0.0416 |
| Raw ev home | 0.0888 |
| Raw edge prob draw | 0.1294 |
| Raw ev draw | 0.4539 |
| Raw edge prob away | -0.1710 |
| Raw ev away | -0.3791 |

</details>


---

## 2026-10-17 — Hamburger SV vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **56.8%**. Expected goals are 1.11 for Hamburger SV and 2.02 for VfB Stuttgart (3.13 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.8%; Under 4.5 goals: 79.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 20.8% | 4.81 |
| Draw | 22.5% | 4.45 |
| VfB Stuttgart win | 56.8% | 1.76 |

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
| 2 | 1-2 | 9.80% |
| 3 | 0-2 | 8.83% |
| 4 | 0-1 | 7.73% |
| 5 | 1-3 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 20.8% | 22.2% | 4.25 | -11.7% |
| Draw | 22.5% | 21.6% | 4.35 | -2.3% |
| VfB Stuttgart win | 56.8% | 56.2% | 1.90 | +7.9% |
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
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.22 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.86 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.62 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.81 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 19.4% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 57.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 4.00 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.70 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Home probability edge | -1.4% |
| Draw probability edge | +0.9% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | -0.0283 |
| Raw ev home | -0.1772 |
| Raw edge prob draw | 0.0171 |
| Raw ev draw | 0.0140 |
| Raw edge prob away | 0.0113 |
| Raw ev away | 0.0893 |

</details>


---

## 2026-10-17 — Union Berlin vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **60.7%**. Expected goals are 0.94 for Union Berlin and 1.92 for Borussia Dortmund (2.87 combined). The most likely exact score is 0-2 at 10.8%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 55.3%; Under 4.5 goals: 83.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 17.1% | 5.86 |
| Draw | 22.2% | 4.50 |
| Borussia Dortmund win | 60.7% | 1.65 |

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
| Over 3.5 | 32.5% |
| Under 3.5 | 67.5% |
| Over 4.5 | 16.5% |
| Under 4.5 | 83.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 10.80% |
| 2 | 1-1 | 10.60% |
| 3 | 1-2 | 10.16% |
| 4 | 0-1 | 10.12% |
| 5 | 0-3 | 6.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 17.1% | 17.3% | 5.40 | -7.8% |
| Draw | 22.2% | 20.5% | 4.60 | +2.2% |
| Borussia Dortmund win | 60.7% | 62.1% | 1.73 | +5.0% |
| Over 2.5 | 55.3% | 66.7% | 1.49 | -17.6% |
| Under 2.5 | 44.7% | 33.3% | 2.70 | +20.8% |

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
| Odds bookmakers 1x2 | 15.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Unibet (SE) |
| Best draw bookmaker | Betfair |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Betsson |
| Best under 2 5 bookmaker | William Hill |
| Matched home-team name | Union Berlin |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.87 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.08 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.05 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 16.8% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 59.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 4.90 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.54 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | -0.3% |
| Draw probability edge | +1.7% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | -0.0051 |
| Raw ev home | -0.0916 |
| Raw edge prob draw | 0.0334 |
| Raw ev draw | 0.0989 |
| Raw edge prob away | -0.0283 |
| Raw ev away | 0.0257 |

</details>


---

## 2026-10-17 — Werder Bremen vs SC Paderborn

The model's most likely 1X2 outcome is **Werder Bremen win** at **48.3%**. Expected goals are 1.16 for Werder Bremen and 0.74 for SC Paderborn (1.91 combined). The most likely exact score is 1-0 at 17.3%. Goal-market probabilities: at least one goal: 86.3%; Over 2.5 goals: 31.4%; Under 4.5 goals: 95.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 48.3% | 2.07 |
| Draw | 28.4% | 3.53 |
| SC Paderborn win | 23.4% | 4.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.16 |
| SC Paderborn expected goals | 0.74 |
| Expected total goals | 1.91 |
| Over 0.5 | 86.3% |
| Under 0.5 | 13.7% |
| Over 1.5 | 58.7% |
| Under 1.5 | 41.3% |
| Over 2.5 | 31.4% |
| Under 2.5 | 68.6% |
| Over 3.5 | 12.9% |
| Under 3.5 | 87.1% |
| Over 4.5 | 4.7% |
| Under 4.5 | 95.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.33% |
| 2 | 0-0 | 13.75% |
| 3 | 1-1 | 12.02% |
| 4 | 2-0 | 10.94% |
| 5 | 0-1 | 10.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 48.3% | 52.0% | 1.91 | -7.8% |
| Draw | 28.4% | 23.3% | 4.26 | +20.8% |
| SC Paderborn win | 23.4% | 24.7% | 4.25 | -0.6% |
| Over 2.5 | 31.4% | 61.8% | 1.56 | -51.0% |
| Under 2.5 | 68.6% | 38.2% | 2.47 | +69.5% |

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
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.27 |
| Fair Over 1.5 odds | 1.70 |
| Fair Under 1.5 odds | 2.42 |
| Fair Over 2.5 odds | 3.19 |
| Fair Under 2.5 odds | 1.46 |
| Fair Over 3.5 odds | 7.74 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 21.10 |
| Fair Under 4.5 odds | 1.05 |
| Unadjusted home-win probability | 44.5% |
| Unadjusted draw probability | 33.4% |
| Unadjusted away-win probability | 22.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.82 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Home probability edge | -3.8% |
| Draw probability edge | +5.1% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -30.4% |
| Under 2.5 probability edge | +30.4% |
| Raw edge prob home | -0.0751 |
| Raw ev home | -0.1500 |
| Raw edge prob draw | 0.1015 |
| Raw ev draw | 0.4242 |
| Raw edge prob away | -0.0263 |
| Raw ev away | -0.0621 |

</details>


---

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **63.5%**. Expected goals are 2.44 for Bayer Leverkusen and 0.96 for SC Freiburg (3.41 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 65.3%; Under 4.5 goals: 75.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 63.5% | 1.58 |
| Draw | 19.8% | 5.06 |
| SC Freiburg win | 16.8% | 5.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.44 |
| SC Freiburg expected goals | 0.96 |
| Expected total goals | 3.41 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 85.7% |
| Under 1.5 | 14.3% |
| Over 2.5 | 65.3% |
| Under 2.5 | 34.7% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.10% |
| 2 | 2-0 | 9.10% |
| 3 | 2-1 | 8.76% |
| 4 | 3-0 | 7.41% |
| 5 | 3-1 | 7.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 63.5% | 57.8% | 1.70 | +7.9% |
| Draw | 19.8% | 20.8% | 4.60 | -9.0% |
| SC Freiburg win | 16.8% | 21.4% | 4.83 | -19.0% |
| Over 2.5 | 65.3% | 66.3% | 1.49 | -2.6% |
| Under 2.5 | 34.7% | 33.7% | 2.67 | -7.5% |

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
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.92 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.97 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.89 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.00 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 69.1% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 12.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.65 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | +5.6% |
| Draw probability edge | -1.0% |
| Away probability edge | -4.6% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | 0.1125 |
| Raw ev home | 0.1743 |
| Raw edge prob draw | -0.0207 |
| Raw ev draw | -0.1381 |
| Raw edge prob away | -0.0918 |
| Raw ev away | -0.4114 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **42.2%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 72.0%; Under 4.5 goals: 68.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 35.0% | 2.86 |
| Draw | 22.8% | 4.38 |
| TSG Hoffenheim win | 42.2% | 2.37 |

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
| 1 | 1-1 | 9.06% |
| 2 | 1-2 | 8.88% |
| 3 | 2-2 | 7.11% |
| 4 | 2-1 | 6.85% |
| 5 | 1-3 | 5.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 35.0% | 28.7% | 3.58 | +25.2% |
| Draw | 22.8% | 22.4% | 4.26 | -2.8% |
| TSG Hoffenheim win | 42.2% | 48.9% | 2.00 | -15.6% |
| Over 2.5 | 72.0% | 68.5% | 1.40 | +0.8% |
| Under 2.5 | 28.0% | 31.5% | 3.00 | -16.0% |

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
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.01 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.50 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.57 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.14 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 41.3% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 35.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.15 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.93 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Home probability edge | +6.3% |
| Draw probability edge | +0.4% |
| Away probability edge | -6.7% |
| Over 2.5 probability edge | +3.5% |
| Under 2.5 probability edge | -3.5% |
| Raw edge prob home | 0.1260 |
| Raw ev home | 0.4780 |
| Raw edge prob draw | 0.0079 |
| Raw ev draw | -0.0111 |
| Raw edge prob away | -0.1339 |
| Raw ev away | -0.2899 |

</details>


---
