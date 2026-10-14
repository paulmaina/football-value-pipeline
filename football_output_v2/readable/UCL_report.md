# UEFA Champions League — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 539 |
| Training data through | 2026-10-14 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 970.507 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.306 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0009 |
| Training data health | {'completed_matches': 36, 'latest_completed_utc': '2026-10-14T19:00:00+00:00', 'latest_completed_date': '2026-10-14', 'next_fixture_utc': '2026-10-20T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-14T21:07:48.255627+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 7, 'corrected_scores': 0, 'sha256': '17597199dea25e2bfba2d1c32219acb359fc52418ff0fda824435d605e822720', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0006044163888888888, 'training_end': '2026-10-14', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Additional event odds calls used before this league | 25.00 |
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

## 2026-10-20 — AS Roma vs ŠK Slovan Bratislava

The model's most likely 1X2 outcome is **AS Roma win** at **81.1%**. Expected goals are 3.76 for AS Roma and 1.32 for ŠK Slovan Bratislava (5.08 combined). The most likely exact score is 3-1 at 7.3%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 88.1%; Under 3.5 goals: 25.5%; Double Chance 1X: 91.2%; Double Chance X2: 18.9%; Under 4.5 goals: 42.8%; BTTS Yes (both teams score): 71.3%; BTTS No (at least one team does not score): 28.7%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 81.1% | 1.23 |
| Draw | 10.1% | 9.86 |
| ŠK Slovan Bratislava win | 8.8% | 11.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 3.76 |
| ŠK Slovan Bratislava expected goals | 1.32 |
| Expected total goals | 5.08 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 96.0% |
| Under 1.5 | 4.0% |
| Over 2.5 | 88.1% |
| Under 2.5 | 11.9% |
| Over 3.5 | 74.5% |
| Under 3.5 | 25.5% |
| Over 4.5 | 57.2% |
| Under 4.5 | 42.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.29% |
| 2 | 4-1 | 6.86% |
| 3 | 2-1 | 5.82% |
| 4 | 3-0 | 5.55% |
| 5 | 4-0 | 5.21% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | fdorg:575364 |
| Matched home-team name | AS Roma |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 71.3% |
| P btts no | 28.7% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 212.25 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 25.27 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.43 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.92 |
| Fair Over 4.5 odds | 1.75 |
| Fair Under 4.5 odds | 2.34 |
| Unadjusted home-win probability | 81.1% |
| Unadjusted draw probability | 10.1% |
| Unadjusted away-win probability | 8.8% |
| Raw p over 1 5 | 96.0% |
| Raw p under 3 5 | 25.5% |
| Raw p btts yes | 71.3% |
| P home draw | 91.2% |
| P draw away | 18.9% |
| Raw p home draw | 91.2% |
| Raw p draw away | 18.9% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — FC Porto vs PSV

The model's most likely 1X2 outcome is **FC Porto win** at **59.5%**. Expected goals are 2.11 for FC Porto and 1.17 for PSV (3.28 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.5%; Double Chance 1X: 79.2%; Double Chance X2: 40.5%; Under 4.5 goals: 76.7%; BTTS Yes (both teams score): 60.1%; BTTS No (at least one team does not score): 39.9%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Porto win | 59.5% | 1.68 |
| Draw | 19.7% | 5.08 |
| PSV win | 20.8% | 4.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Porto expected goals | 2.11 |
| PSV expected goals | 1.17 |
| Expected total goals | 3.28 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 63.6% |
| Under 2.5 | 36.4% |
| Over 3.5 | 41.5% |
| Under 3.5 | 58.5% |
| Over 4.5 | 23.3% |
| Under 4.5 | 76.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.80% |
| 2 | 1-1 | 8.82% |
| 3 | 1-0 | 8.42% |
| 4 | 2-0 | 8.40% |
| 5 | 3-1 | 6.90% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | fdorg:575365 |
| Matched home-team name | FC Porto |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.1% |
| P btts no | 39.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.25 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.03 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.41 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.28 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 59.5% |
| Unadjusted draw probability | 19.7% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 60.1% |
| P home draw | 79.2% |
| P draw away | 40.5% |
| Raw p home draw | 79.2% |
| Raw p draw away | 40.5% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — Fenerbahçe SK vs SK Slavia Praha

The model's most likely 1X2 outcome is **SK Slavia Praha win** at **42.6%**. Expected goals are 0.78 for Fenerbahçe SK and 1.07 for SK Slavia Praha (1.84 combined). The most likely exact score is 0-1 at 17.6%. Goal-market probabilities: at least one goal: 84.8%; Over 2.5 goals: 28.1%; Under 3.5 goals: 88.4%; Double Chance 1X: 57.4%; Double Chance X2: 73.2%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 34.7%; BTTS No (at least one team does not score): 65.3%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahçe SK win | 26.8% | 3.73 |
| Draw | 30.6% | 3.27 |
| SK Slavia Praha win | 42.6% | 2.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahçe SK expected goals | 0.78 |
| SK Slavia Praha expected goals | 1.07 |
| Expected total goals | 1.84 |
| Over 0.5 | 84.8% |
| Under 0.5 | 15.2% |
| Over 1.5 | 54.3% |
| Under 1.5 | 45.7% |
| Over 2.5 | 28.1% |
| Under 2.5 | 71.9% |
| Over 3.5 | 11.6% |
| Under 3.5 | 88.4% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.57% |
| 2 | 0-0 | 15.19% |
| 3 | 1-0 | 12.94% |
| 4 | 1-1 | 12.45% |
| 5 | 0-2 | 9.02% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T16:45:00+00:00 |
| Fixture id | fdorg:575360 |
| Matched home-team name | Fenerbahçe SK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 34.7% |
| P btts no | 65.3% |
| Fair Over 0.5 odds | 1.18 |
| Fair Under 0.5 odds | 6.58 |
| Fair Over 1.5 odds | 1.84 |
| Fair Under 1.5 odds | 2.19 |
| Fair Over 2.5 odds | 3.56 |
| Fair Under 2.5 odds | 1.39 |
| Fair Over 3.5 odds | 8.65 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 25.29 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 42.6% |
| Raw p over 1 5 | 54.3% |
| Raw p under 3 5 | 88.4% |
| Raw p btts yes | 34.7% |
| P home draw | 57.4% |
| P draw away | 73.2% |
| Raw p home draw | 57.4% |
| Raw p draw away | 73.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — Liverpool FC vs Villarreal CF

The model's most likely 1X2 outcome is **Liverpool FC win** at **89.9%**. Expected goals are 3.36 for Liverpool FC and 0.51 for Villarreal CF (3.86 combined). The most likely exact score is 3-0 at 13.3%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 74.1%; Under 3.5 goals: 46.2%; Double Chance 1X: 97.0%; Double Chance X2: 10.1%; Under 4.5 goals: 65.7%; BTTS Yes (both teams score): 38.1%; BTTS No (at least one team does not score): 61.9%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool FC win | 89.9% | 1.11 |
| Draw | 7.2% | 13.97 |
| Villarreal CF win | 3.0% | 33.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool FC expected goals | 3.36 |
| Villarreal CF expected goals | 0.51 |
| Expected total goals | 3.86 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 89.6% |
| Under 1.5 | 10.4% |
| Over 2.5 | 74.1% |
| Under 2.5 | 25.9% |
| Over 3.5 | 53.8% |
| Under 3.5 | 46.2% |
| Over 4.5 | 34.3% |
| Under 4.5 | 65.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 13.26% |
| 2 | 2-0 | 11.86% |
| 3 | 4-0 | 11.13% |
| 4 | 5-0 | 7.47% |
| 5 | 1-0 | 7.25% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | fdorg:575363 |
| Matched home-team name | Liverpool FC |
| Matched away-team name | Villarreal CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 38.1% |
| P btts no | 61.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 51.85 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.60 |
| Fair Over 2.5 odds | 1.35 |
| Fair Under 2.5 odds | 3.85 |
| Fair Over 3.5 odds | 1.86 |
| Fair Under 3.5 odds | 2.17 |
| Fair Over 4.5 odds | 2.91 |
| Fair Under 4.5 odds | 1.52 |
| Unadjusted home-win probability | 89.9% |
| Unadjusted draw probability | 7.2% |
| Unadjusted away-win probability | 3.0% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 46.2% |
| Raw p btts yes | 38.1% |
| P home draw | 97.0% |
| P draw away | 10.1% |
| Raw p home draw | 97.0% |
| Raw p draw away | 10.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — Manchester City FC vs PAE AEK

The model's most likely 1X2 outcome is **Manchester City FC win** at **75.9%**. Expected goals are 1.97 for Manchester City FC and 0.39 for PAE AEK (2.36 combined). The most likely exact score is 1-0 at 18.9%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 42.1%; Under 3.5 goals: 78.6%; Double Chance 1X: 93.3%; Double Chance X2: 24.1%; Under 4.5 goals: 90.9%; BTTS Yes (both teams score): 27.4%; BTTS No (at least one team does not score): 72.6%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City FC win | 75.9% | 1.32 |
| Draw | 17.4% | 5.73 |
| PAE AEK win | 6.7% | 14.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City FC expected goals | 1.97 |
| PAE AEK expected goals | 0.39 |
| Expected total goals | 2.36 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 68.0% |
| Under 1.5 | 32.0% |
| Over 2.5 | 42.1% |
| Under 2.5 | 57.9% |
| Over 3.5 | 21.4% |
| Under 3.5 | 78.6% |
| Over 4.5 | 9.1% |
| Under 4.5 | 90.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 18.94% |
| 2 | 2-0 | 18.33% |
| 3 | 3-0 | 12.05% |
| 4 | 0-0 | 9.05% |
| 5 | 2-1 | 7.14% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | fdorg:575361 |
| Matched home-team name | Manchester City FC |
| Matched away-team name | PAE AEK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 27.4% |
| P btts no | 72.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.05 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.12 |
| Fair Over 2.5 odds | 2.38 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.68 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.96 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 75.9% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 6.7% |
| Raw p over 1 5 | 68.0% |
| Raw p under 3 5 | 78.6% |
| Raw p btts yes | 27.4% |
| P home draw | 93.3% |
| P draw away | 24.1% |
| Raw p home draw | 93.3% |
| Raw p draw away | 24.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — Paris Saint-Germain FC vs FC Barcelona

The model's most likely 1X2 outcome is **Paris Saint-Germain FC win** at **71.0%**. Expected goals are 3.22 for Paris Saint-Germain FC and 1.52 for FC Barcelona (4.75 combined). The most likely exact score is 3-1 at 7.4%. Goal-market probabilities: at least one goal: 99.3%; Over 2.5 goals: 85.2%; Under 3.5 goals: 30.3%; Double Chance 1X: 84.9%; Double Chance X2: 29.0%; Under 4.5 goals: 48.6%; BTTS Yes (both teams score): 74.9%; BTTS No (at least one team does not score): 25.1%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint-Germain FC win | 71.0% | 1.41 |
| Draw | 13.9% | 7.21 |
| FC Barcelona win | 15.1% | 6.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint-Germain FC expected goals | 3.22 |
| FC Barcelona expected goals | 1.52 |
| Expected total goals | 4.75 |
| Over 0.5 | 99.3% |
| Under 0.5 | 0.7% |
| Over 1.5 | 94.8% |
| Under 1.5 | 5.2% |
| Over 2.5 | 85.2% |
| Under 2.5 | 14.8% |
| Over 3.5 | 69.7% |
| Under 3.5 | 30.3% |
| Over 4.5 | 51.4% |
| Under 4.5 | 48.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.39% |
| 2 | 2-1 | 6.87% |
| 3 | 4-1 | 5.95% |
| 4 | 3-2 | 5.62% |
| 5 | 2-2 | 5.23% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | fdorg:575367 |
| Matched home-team name | Paris Saint-Germain FC |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 74.9% |
| P btts no | 25.1% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 152.53 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 19.21 |
| Fair Over 2.5 odds | 1.17 |
| Fair Under 2.5 odds | 6.77 |
| Fair Over 3.5 odds | 1.43 |
| Fair Under 3.5 odds | 3.30 |
| Fair Over 4.5 odds | 1.95 |
| Fair Under 4.5 odds | 2.06 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 94.8% |
| Raw p under 3 5 | 30.3% |
| Raw p btts yes | 74.9% |
| P home draw | 84.9% |
| P draw away | 29.0% |
| Raw p home draw | 84.9% |
| Raw p draw away | 29.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — SSC Napoli vs FK Bodø/Glimt

The model's most likely 1X2 outcome is **FK Bodø/Glimt win** at **52.3%**. Expected goals are 1.17 for SSC Napoli and 1.78 for FK Bodø/Glimt (2.94 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 56.4%; Under 3.5 goals: 66.0%; Double Chance 1X: 47.7%; Double Chance X2: 74.5%; Under 4.5 goals: 82.5%; BTTS Yes (both teams score): 56.7%; BTTS No (at least one team does not score): 43.3%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SSC Napoli win | 25.5% | 3.92 |
| Draw | 22.2% | 4.50 |
| FK Bodø/Glimt win | 52.3% | 1.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SSC Napoli expected goals | 1.17 |
| FK Bodø/Glimt expected goals | 1.78 |
| Expected total goals | 2.94 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 78.7% |
| Under 1.5 | 21.3% |
| Over 2.5 | 56.4% |
| Under 2.5 | 43.6% |
| Over 3.5 | 34.0% |
| Under 3.5 | 66.0% |
| Over 4.5 | 17.5% |
| Under 4.5 | 82.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.37% |
| 2 | 0-1 | 9.91% |
| 3 | 1-2 | 9.71% |
| 4 | 0-2 | 8.32% |
| 5 | 1-0 | 6.68% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | fdorg:575366 |
| Matched home-team name | SSC Napoli |
| Matched away-team name | FK Bodø/Glimt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.19 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.69 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 2.94 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.70 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 25.5% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 52.3% |
| Raw p over 1 5 | 78.7% |
| Raw p under 3 5 | 66.0% |
| Raw p btts yes | 56.7% |
| P home draw | 47.7% |
| P draw away | 74.5% |
| Raw p home draw | 47.7% |
| Raw p draw away | 74.5% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — Sabah FK vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **75.4%**. Expected goals are 0.75 for Sabah FK and 2.47 for Borussia Dortmund (3.23 combined). The most likely exact score is 0-2 at 12.1%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 62.6%; Under 3.5 goals: 59.6%; Double Chance 1X: 24.6%; Double Chance X2: 90.3%; Under 4.5 goals: 77.5%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 9.7% | 10.30 |
| Draw | 14.9% | 6.73 |
| Borussia Dortmund win | 75.4% | 1.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.75 |
| Borussia Dortmund expected goals | 2.47 |
| Expected total goals | 3.23 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 62.6% |
| Under 2.5 | 37.4% |
| Over 3.5 | 40.4% |
| Under 3.5 | 59.6% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.12% |
| 2 | 0-1 | 10.17% |
| 3 | 0-3 | 10.00% |
| 4 | 1-2 | 9.15% |
| 5 | 1-3 | 7.55% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T16:45:00+00:00 |
| Fixture id | fdorg:575359 |
| Matched home-team name | Sabah FK |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.86 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.84 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.48 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.45 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 9.7% |
| Unadjusted draw probability | 14.9% |
| Unadjusted away-win probability | 75.4% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 59.6% |
| Raw p btts yes | 48.1% |
| P home draw | 24.6% |
| P draw away | 90.3% |
| Raw p home draw | 24.6% |
| Raw p draw away | 90.3% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — VfB Stuttgart vs Club Atlético de Madrid

The model's most likely 1X2 outcome is **Club Atlético de Madrid win** at **53.7%**. Expected goals are 1.41 for VfB Stuttgart and 2.10 for Club Atlético de Madrid (3.51 combined). The most likely exact score is 1-2 at 9.3%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 68.1%; Under 3.5 goals: 53.5%; Double Chance 1X: 46.3%; Double Chance X2: 73.8%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 65.9%; BTTS No (at least one team does not score): 34.1%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 26.2% | 3.82 |
| Draw | 20.1% | 4.96 |
| Club Atlético de Madrid win | 53.7% | 1.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 1.41 |
| Club Atlético de Madrid expected goals | 2.10 |
| Expected total goals | 3.51 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 68.1% |
| Under 2.5 | 31.9% |
| Over 3.5 | 46.5% |
| Under 3.5 | 53.5% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.29% |
| 2 | 1-1 | 8.42% |
| 3 | 0-1 | 6.71% |
| 4 | 2-2 | 6.57% |
| 5 | 0-2 | 6.57% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | fdorg:575362 |
| Matched home-team name | VfB Stuttgart |
| Matched away-team name | Club Atlético de Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 65.9% |
| P btts no | 34.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.26 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.18 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.13 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.62 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 26.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 53.7% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 65.9% |
| P home draw | 46.3% |
| P draw away | 73.8% |
| Raw p home draw | 46.3% |
| Raw p draw away | 73.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Aston Villa FC vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa FC win** at **85.6%**. Expected goals are 4.01 for Aston Villa FC and 1.16 for Viking FK (5.17 combined). The most likely exact score is 4-1 at 7.1%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 88.9%; Under 3.5 goals: 24.3%; Double Chance 1X: 93.8%; Double Chance X2: 14.4%; Under 4.5 goals: 41.2%; BTTS Yes (both teams score): 67.4%; BTTS No (at least one team does not score): 32.6%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa FC win | 85.6% | 1.17 |
| Draw | 8.2% | 12.14 |
| Viking FK win | 6.2% | 16.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa FC expected goals | 4.01 |
| Viking FK expected goals | 1.16 |
| Expected total goals | 5.17 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 96.3% |
| Under 1.5 | 3.7% |
| Over 2.5 | 88.9% |
| Under 2.5 | 11.1% |
| Over 3.5 | 75.7% |
| Under 3.5 | 24.3% |
| Over 4.5 | 58.8% |
| Under 4.5 | 41.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-1 | 7.12% |
| 2 | 3-1 | 7.11% |
| 3 | 4-0 | 6.12% |
| 4 | 3-0 | 6.11% |
| 5 | 5-1 | 5.70% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | fdorg:575374 |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.4% |
| P btts no | 32.6% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 228.56 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 27.38 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.98 |
| Fair Over 3.5 odds | 1.32 |
| Fair Under 3.5 odds | 4.12 |
| Fair Over 4.5 odds | 1.70 |
| Fair Under 4.5 odds | 2.42 |
| Unadjusted home-win probability | 85.6% |
| Unadjusted draw probability | 8.2% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 96.3% |
| Raw p under 3 5 | 24.3% |
| Raw p btts yes | 67.4% |
| P home draw | 93.8% |
| P draw away | 14.4% |
| Raw p home draw | 93.8% |
| Raw p draw away | 14.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Club Brugge KV vs Racing Club de Lens

The model's most likely 1X2 outcome is **Club Brugge KV win** at **73.3%**. Expected goals are 3.05 for Club Brugge KV and 1.27 for Racing Club de Lens (4.32 combined). The most likely exact score is 3-1 at 8.0%. Goal-market probabilities: at least one goal: 98.9%; Over 2.5 goals: 80.6%; Under 3.5 goals: 37.3%; Double Chance 1X: 87.0%; Double Chance X2: 26.7%; Under 4.5 goals: 56.6%; BTTS Yes (both teams score): 68.3%; BTTS No (at least one team does not score): 31.7%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge KV win | 73.3% | 1.36 |
| Draw | 13.7% | 7.29 |
| Racing Club de Lens win | 13.0% | 7.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Club Brugge KV expected goals | 3.05 |
| Racing Club de Lens expected goals | 1.27 |
| Expected total goals | 4.32 |
| Over 0.5 | 98.9% |
| Under 0.5 | 1.1% |
| Over 1.5 | 92.7% |
| Under 1.5 | 7.3% |
| Over 2.5 | 80.6% |
| Under 2.5 | 19.4% |
| Over 3.5 | 62.7% |
| Under 3.5 | 37.3% |
| Over 4.5 | 43.4% |
| Under 4.5 | 56.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.99% |
| 2 | 2-1 | 7.85% |
| 3 | 3-0 | 6.27% |
| 4 | 2-0 | 6.17% |
| 5 | 4-1 | 6.09% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | fdorg:575373 |
| Matched home-team name | Club Brugge KV |
| Matched away-team name | Racing Club de Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 68.3% |
| P btts no | 31.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 93.63 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.67 |
| Fair Over 2.5 odds | 1.24 |
| Fair Under 2.5 odds | 5.14 |
| Fair Over 3.5 odds | 1.59 |
| Fair Under 3.5 odds | 2.68 |
| Fair Over 4.5 odds | 2.30 |
| Fair Under 4.5 odds | 1.77 |
| Unadjusted home-win probability | 73.3% |
| Unadjusted draw probability | 13.7% |
| Unadjusted away-win probability | 13.0% |
| Raw p over 1 5 | 92.7% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 68.3% |
| P home draw | 87.0% |
| P draw away | 26.7% |
| Raw p home draw | 87.0% |
| Raw p draw away | 26.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Como 1907 vs Manchester United FC

The model's most likely 1X2 outcome is **Como 1907 win** at **59.7%**. Expected goals are 2.99 for Como 1907 and 1.94 for Manchester United FC (4.93 combined). The most likely exact score is 2-1 at 6.3%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 87.0%; Under 3.5 goals: 27.4%; Double Chance 1X: 76.0%; Double Chance X2: 40.3%; Under 4.5 goals: 45.2%; BTTS Yes (both teams score): 81.1%; BTTS No (at least one team does not score): 18.9%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como 1907 win | 59.7% | 1.68 |
| Draw | 16.3% | 6.13 |
| Manchester United FC win | 24.0% | 4.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como 1907 expected goals | 2.99 |
| Manchester United FC expected goals | 1.94 |
| Expected total goals | 4.93 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 95.5% |
| Under 1.5 | 4.5% |
| Over 2.5 | 87.0% |
| Under 2.5 | 13.0% |
| Over 3.5 | 72.6% |
| Under 3.5 | 27.4% |
| Over 4.5 | 54.8% |
| Under 4.5 | 45.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 6.26% |
| 2 | 3-1 | 6.24% |
| 3 | 2-2 | 6.08% |
| 4 | 3-2 | 6.06% |
| 5 | 4-1 | 4.67% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T16:45:00+00:00 |
| Fixture id | fdorg:575368 |
| Matched home-team name | Como 1907 |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 81.1% |
| P btts no | 18.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 195.77 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 22.31 |
| Fair Over 2.5 odds | 1.15 |
| Fair Under 2.5 odds | 7.67 |
| Fair Over 3.5 odds | 1.38 |
| Fair Under 3.5 odds | 3.64 |
| Fair Over 4.5 odds | 1.83 |
| Fair Under 4.5 odds | 2.21 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 95.5% |
| Raw p under 3 5 | 27.4% |
| Raw p btts yes | 81.1% |
| P home draw | 76.0% |
| P draw away | 40.3% |
| Raw p home draw | 76.0% |
| Raw p draw away | 40.3% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — FC Bayern München vs Arsenal FC

The model's most likely 1X2 outcome is **Arsenal FC win** at **43.9%**. Expected goals are 1.02 for FC Bayern München and 1.31 for Arsenal FC (2.33 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 41.1%; Under 3.5 goals: 79.4%; Double Chance 1X: 56.1%; Double Chance X2: 70.4%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 46.0%; BTTS No (at least one team does not score): 54.0%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Bayern München win | 29.6% | 3.38 |
| Draw | 26.5% | 3.78 |
| Arsenal FC win | 43.9% | 2.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Bayern München expected goals | 1.02 |
| Arsenal FC expected goals | 1.31 |
| Expected total goals | 2.33 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 41.1% |
| Under 2.5 | 58.9% |
| Over 3.5 | 20.6% |
| Under 3.5 | 79.4% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.42% |
| 2 | 1-1 | 12.35% |
| 3 | 1-0 | 10.57% |
| 4 | 0-0 | 9.10% |
| 5 | 1-2 | 8.52% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | fdorg:575372 |
| Matched home-team name | FC Bayern München |
| Matched away-team name | Arsenal FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 46.0% |
| P btts no | 54.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.99 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.84 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.48 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 29.6% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 43.9% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 79.4% |
| Raw p btts yes | 46.0% |
| P home draw | 56.1% |
| P draw away | 70.4% |
| Raw p home draw | 56.1% |
| Raw p draw away | 70.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — FC Internazionale Milano vs FK Shakhtar Donetsk

The model's most likely 1X2 outcome is **FC Internazionale Milano win** at **64.0%**. Expected goals are 2.05 for FC Internazionale Milano and 0.92 for FK Shakhtar Donetsk (2.97 combined). The most likely exact score is 1-0 at 11.0%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 57.1%; Under 3.5 goals: 65.3%; Double Chance 1X: 83.5%; Double Chance X2: 36.0%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 52.0%; BTTS No (at least one team does not score): 48.0%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Internazionale Milano win | 64.0% | 1.56 |
| Draw | 19.5% | 5.14 |
| FK Shakhtar Donetsk win | 16.5% | 6.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Internazionale Milano expected goals | 2.05 |
| FK Shakhtar Donetsk expected goals | 0.92 |
| Expected total goals | 2.97 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 10.98% |
| 2 | 2-0 | 10.76% |
| 3 | 2-1 | 9.92% |
| 4 | 1-1 | 9.19% |
| 5 | 3-0 | 7.36% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | fdorg:575371 |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | FK Shakhtar Donetsk |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 52.0% |
| P btts no | 48.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.58 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.81 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.55 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 64.0% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 16.5% |
| Raw p over 1 5 | 79.2% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 52.0% |
| P home draw | 83.5% |
| P draw away | 36.0% |
| Raw p home draw | 83.5% |
| Raw p draw away | 36.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Lille OSC vs Galatasaray SK

The model's most likely 1X2 outcome is **Lille OSC win** at **70.8%**. Expected goals are 2.57 for Lille OSC and 1.04 for Galatasaray SK (3.61 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 69.8%; Under 3.5 goals: 51.4%; Double Chance 1X: 86.5%; Double Chance X2: 29.2%; Under 4.5 goals: 70.5%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille OSC win | 70.8% | 1.41 |
| Draw | 15.7% | 6.35 |
| Galatasaray SK win | 13.5% | 7.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille OSC expected goals | 2.57 |
| Galatasaray SK expected goals | 1.04 |
| Expected total goals | 3.61 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 87.1% |
| Under 1.5 | 12.9% |
| Over 2.5 | 69.8% |
| Under 2.5 | 30.2% |
| Over 3.5 | 48.6% |
| Under 3.5 | 51.4% |
| Over 4.5 | 29.5% |
| Under 4.5 | 70.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.29% |
| 2 | 2-0 | 8.97% |
| 3 | 3-1 | 7.96% |
| 4 | 3-0 | 7.68% |
| 5 | 1-0 | 7.34% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T16:45:00+00:00 |
| Fixture id | fdorg:575369 |
| Matched home-team name | Lille OSC |
| Matched away-team name | Galatasaray SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.47 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.77 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.31 |
| Fair Over 3.5 odds | 2.06 |
| Fair Under 3.5 odds | 1.95 |
| Fair Over 4.5 odds | 3.39 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 70.8% |
| Unadjusted draw probability | 15.7% |
| Unadjusted away-win probability | 13.5% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 51.4% |
| Raw p btts yes | 59.2% |
| P home draw | 86.5% |
| P draw away | 29.2% |
| Raw p home draw | 86.5% |
| Raw p draw away | 29.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Real Betis Balompié vs Feyenoord Rotterdam

The model's most likely 1X2 outcome is **Real Betis Balompié win** at **91.3%**. Expected goals are 5.75 for Real Betis Balompié and 1.65 for Feyenoord Rotterdam (7.40 combined). The most likely exact score is 5-1 at 5.5%. Goal-market probabilities: at least one goal: 100.0%; Over 2.5 goals: 97.7%; Under 3.5 goals: 6.5%; Double Chance 1X: 96.1%; Double Chance X2: 8.7%; Under 4.5 goals: 14.4%; BTTS Yes (both teams score): 80.4%; BTTS No (at least one team does not score): 19.6%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis Balompié win | 91.3% | 1.10 |
| Draw | 4.8% | 20.67 |
| Feyenoord Rotterdam win | 3.9% | 25.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis Balompié expected goals | 5.75 |
| Feyenoord Rotterdam expected goals | 1.65 |
| Expected total goals | 7.40 |
| Over 0.5 | 100.0% |
| Under 0.5 | 0.0% |
| Over 1.5 | 99.4% |
| Under 1.5 | 0.6% |
| Over 2.5 | 97.7% |
| Under 2.5 | 2.3% |
| Over 3.5 | 93.5% |
| Under 3.5 | 6.5% |
| Over 4.5 | 85.6% |
| Under 4.5 | 14.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-1 | 5.47% |
| 2 | 6-1 | 5.25% |
| 3 | 4-1 | 4.75% |
| 4 | 5-2 | 4.50% |
| 5 | 6-2 | 4.32% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | fdorg:575376 |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 80.4% |
| P btts no | 19.6% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 3001.65 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 178.14 |
| Fair Over 2.5 odds | 1.02 |
| Fair Under 2.5 odds | 44.18 |
| Fair Over 3.5 odds | 1.07 |
| Fair Under 3.5 odds | 15.30 |
| Fair Over 4.5 odds | 1.17 |
| Fair Under 4.5 odds | 6.93 |
| Unadjusted home-win probability | 91.3% |
| Unadjusted draw probability | 4.8% |
| Unadjusted away-win probability | 3.9% |
| Raw p over 1 5 | 99.4% |
| Raw p under 3 5 | 6.5% |
| Raw p btts yes | 80.4% |
| P home draw | 96.1% |
| P draw away | 8.7% |
| Raw p home draw | 96.1% |
| Raw p draw away | 8.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Real Madrid CF vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid CF win** at **77.6%**. Expected goals are 2.80 for Real Madrid CF and 0.88 for RB Leipzig (3.68 combined). The most likely exact score is 2-0 at 9.9%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 71.1%; Under 3.5 goals: 49.9%; Double Chance 1X: 90.7%; Double Chance X2: 22.4%; Under 4.5 goals: 69.2%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid CF win | 77.6% | 1.29 |
| Draw | 13.1% | 7.61 |
| RB Leipzig win | 9.3% | 10.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid CF expected goals | 2.80 |
| RB Leipzig expected goals | 0.88 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 87.9% |
| Under 1.5 | 12.1% |
| Over 2.5 | 71.1% |
| Under 2.5 | 28.9% |
| Over 3.5 | 50.1% |
| Under 3.5 | 49.9% |
| Over 4.5 | 30.8% |
| Under 4.5 | 69.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.92% |
| 2 | 3-0 | 9.26% |
| 3 | 2-1 | 8.70% |
| 4 | 3-1 | 8.12% |
| 5 | 1-0 | 7.39% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | fdorg:575370 |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.11 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.24 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.46 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.24 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 77.6% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 9.3% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 49.9% |
| Raw p btts yes | 54.5% |
| P home draw | 90.7% |
| P draw away | 22.4% |
| Raw p home draw | 90.7% |
| Raw p draw away | 22.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Sporting Clube de Portugal vs LASK Linz

The model's most likely 1X2 outcome is **Sporting Clube de Portugal win** at **94.9%**. Expected goals are 6.10 for Sporting Clube de Portugal and 1.32 for LASK Linz (7.42 combined). The most likely exact score is 6-1 at 5.9%. Goal-market probabilities: at least one goal: 100.0%; Over 2.5 goals: 97.7%; Under 3.5 goals: 6.5%; Double Chance 1X: 98.0%; Double Chance X2: 5.1%; Under 4.5 goals: 14.5%; BTTS Yes (both teams score): 73.0%; BTTS No (at least one team does not score): 27.0%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Clube de Portugal win | 94.9% | 1.05 |
| Draw | 3.1% | 32.49 |
| LASK Linz win | 2.0% | 50.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Clube de Portugal expected goals | 6.10 |
| LASK Linz expected goals | 1.32 |
| Expected total goals | 7.42 |
| Over 0.5 | 100.0% |
| Under 0.5 | 0.0% |
| Over 1.5 | 99.4% |
| Under 1.5 | 0.6% |
| Over 2.5 | 97.7% |
| Under 2.5 | 2.3% |
| Over 3.5 | 93.5% |
| Under 3.5 | 6.5% |
| Over 4.5 | 85.5% |
| Under 4.5 | 14.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 6-1 | 5.94% |
| 2 | 5-1 | 5.84% |
| 3 | 7-1 | 5.18% |
| 4 | 4-1 | 4.79% |
| 5 | 6-0 | 4.52% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | fdorg:575375 |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 73.0% |
| P btts no | 27.0% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 2652.96 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 180.04 |
| Fair Over 2.5 odds | 1.02 |
| Fair Under 2.5 odds | 44.19 |
| Fair Over 3.5 odds | 1.07 |
| Fair Under 3.5 odds | 15.27 |
| Fair Over 4.5 odds | 1.17 |
| Fair Under 4.5 odds | 6.90 |
| Unadjusted home-win probability | 94.9% |
| Unadjusted draw probability | 3.1% |
| Unadjusted away-win probability | 2.0% |
| Raw p over 1 5 | 99.4% |
| Raw p under 3 5 | 6.5% |
| Raw p btts yes | 73.0% |
| P home draw | 98.0% |
| P draw away | 5.1% |
| Raw p home draw | 98.0% |
| Raw p draw away | 5.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---
