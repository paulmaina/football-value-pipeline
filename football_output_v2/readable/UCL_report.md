# UEFA Champions League — football model report

Fixtures in this report: **25**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 532 |
| Training data through | 2026-10-14 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Optimizer objective | 1575.026 |
| Base scoring parameter | 0.177 |
| Home-advantage parameter | 0.290 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0 |
| Training data health | {'completed_matches': 29, 'latest_completed_utc': '2026-10-14T16:45:00+00:00', 'latest_completed_date': '2026-10-14', 'next_fixture_utc': '2026-10-20T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-14T19:07:41.482732+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 2, 'corrected_scores': 0, 'sha256': '994ad05058e9e8add3afb2e70d047cbb3bceb2fe96023dd8a6a6ad58ab26bcc9', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.001401648611111111, 'training_end': '2026-10-14', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
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
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-14 — AS Roma vs Real Madrid CF

The model's most likely 1X2 outcome is **Real Madrid CF win** at **47.4%**. Expected goals are 1.22 for AS Roma and 1.63 for Real Madrid CF (2.85 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 54.2%; Under 3.5 goals: 68.1%; Double Chance 1X: 52.6%; Double Chance X2: 70.7%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 29.3% | 3.41 |
| Draw | 23.3% | 4.29 |
| Real Madrid CF win | 47.4% | 2.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.22 |
| Real Madrid CF expected goals | 1.63 |
| Expected total goals | 2.85 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 54.2% |
| Under 2.5 | 45.8% |
| Over 3.5 | 31.9% |
| Under 3.5 | 68.1% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.94% |
| 2 | 0-1 | 9.99% |
| 3 | 1-2 | 9.36% |
| 4 | 0-2 | 7.66% |
| 5 | 1-0 | 7.66% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | fdorg:575352 |
| Matched home-team name | AS Roma |
| Matched away-team name | Real Madrid CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.17 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.37 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.14 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.25 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 29.3% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 47.4% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 68.1% |
| Raw p btts yes | 56.1% |
| P home draw | 52.6% |
| P draw away | 70.7% |
| Raw p home draw | 52.6% |
| Raw p draw away | 70.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-14 — Aston Villa FC vs Fenerbahçe SK

The model's most likely 1X2 outcome is **Aston Villa FC win** at **74.5%**. Expected goals are 2.19 for Aston Villa FC and 0.60 for Fenerbahçe SK (2.79 combined). The most likely exact score is 2-0 at 14.8%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 52.8%; Under 3.5 goals: 69.4%; Double Chance 1X: 91.0%; Double Chance X2: 25.5%; Under 4.5 goals: 84.9%; BTTS Yes (both teams score): 39.5%; BTTS No (at least one team does not score): 60.5%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa FC win | 74.5% | 1.34 |
| Draw | 16.4% | 6.09 |
| Fenerbahçe SK win | 9.0% | 11.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa FC expected goals | 2.19 |
| Fenerbahçe SK expected goals | 0.60 |
| Expected total goals | 2.79 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 76.3% |
| Under 1.5 | 23.7% |
| Over 2.5 | 52.8% |
| Under 2.5 | 47.2% |
| Over 3.5 | 30.6% |
| Under 3.5 | 69.4% |
| Over 4.5 | 15.1% |
| Under 4.5 | 84.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.77% |
| 2 | 1-0 | 13.86% |
| 3 | 3-0 | 10.80% |
| 4 | 2-1 | 8.82% |
| 5 | 1-1 | 7.63% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | fdorg:575355 |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Fenerbahçe SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 39.5% |
| P btts no | 60.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.45 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.23 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.27 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.62 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 74.5% |
| Unadjusted draw probability | 16.4% |
| Unadjusted away-win probability | 9.0% |
| Raw p over 1 5 | 76.3% |
| Raw p under 3 5 | 69.4% |
| Raw p btts yes | 39.5% |
| P home draw | 91.0% |
| P draw away | 25.5% |
| Raw p home draw | 91.0% |
| Raw p draw away | 25.5% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-14 — FK Bodø/Glimt vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **44.0%**. Expected goals are 1.72 for FK Bodø/Glimt and 1.93 for Borussia Dortmund (3.65 combined). The most likely exact score is 1-2 at 8.3%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.5%; Double Chance 1X: 56.0%; Double Chance X2: 64.8%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 69.7%; BTTS No (at least one team does not score): 30.3%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FK Bodø/Glimt win | 35.2% | 2.84 |
| Draw | 20.8% | 4.81 |
| Borussia Dortmund win | 44.0% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FK Bodø/Glimt expected goals | 1.72 |
| Borussia Dortmund expected goals | 1.93 |
| Expected total goals | 3.65 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 87.5% |
| Under 1.5 | 12.5% |
| Over 2.5 | 70.6% |
| Under 2.5 | 29.4% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.34% |
| 2 | 1-1 | 8.19% |
| 3 | 2-1 | 7.40% |
| 4 | 2-2 | 7.16% |
| 5 | 0-1 | 5.46% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | fdorg:575354 |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 69.7% |
| P btts no | 30.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.16 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.99 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.40 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 35.2% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 50.5% |
| Raw p btts yes | 69.7% |
| P home draw | 56.0% |
| P draw away | 64.8% |
| Raw p home draw | 56.0% |
| Raw p draw away | 64.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-14 — FK Shakhtar Donetsk vs PAE AEK

The model's most likely 1X2 outcome is **Draw** at **60.3%**. Expected goals are 0.26 for FK Shakhtar Donetsk and 0.32 for PAE AEK (0.58 combined). The most likely exact score is 0-0 at 55.7%. Goal-market probabilities: at least one goal: 44.3%; Over 2.5 goals: 2.1%; Under 3.5 goals: 99.7%; Double Chance 1X: 78.0%; Double Chance X2: 82.3%; Under 4.5 goals: 100.0%; BTTS Yes (both teams score): 6.1%; BTTS No (at least one team does not score): 93.9%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FK Shakhtar Donetsk win | 17.7% | 5.65 |
| Draw | 60.3% | 1.66 |
| PAE AEK win | 22.0% | 4.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FK Shakhtar Donetsk expected goals | 0.26 |
| PAE AEK expected goals | 0.32 |
| Expected total goals | 0.58 |
| Over 0.5 | 44.3% |
| Under 0.5 | 55.7% |
| Over 1.5 | 11.3% |
| Under 1.5 | 88.7% |
| Over 2.5 | 2.1% |
| Under 2.5 | 97.9% |
| Over 3.5 | 0.3% |
| Under 3.5 | 99.7% |
| Over 4.5 | 0.0% |
| Under 4.5 | 100.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 55.73% |
| 2 | 0-1 | 18.04% |
| 3 | 1-0 | 14.92% |
| 4 | 1-1 | 4.44% |
| 5 | 0-2 | 2.83% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | fdorg:575357 |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | PAE AEK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 6.1% |
| P btts no | 93.9% |
| Fair Over 0.5 odds | 2.26 |
| Fair Under 0.5 odds | 1.79 |
| Fair Over 1.5 odds | 8.83 |
| Fair Under 1.5 odds | 1.13 |
| Fair Over 2.5 odds | 47.10 |
| Fair Under 2.5 odds | 1.02 |
| Fair Over 3.5 odds | 334.72 |
| Fair Under 3.5 odds | 1.00 |
| Fair Over 4.5 odds | 2942.85 |
| Fair Under 4.5 odds | 1.00 |
| Unadjusted home-win probability | 17.7% |
| Unadjusted draw probability | 60.3% |
| Unadjusted away-win probability | 22.0% |
| Raw p over 1 5 | 11.3% |
| Raw p under 3 5 | 99.7% |
| Raw p btts yes | 6.1% |
| P home draw | 78.0% |
| P draw away | 82.3% |
| Raw p home draw | 78.0% |
| Raw p draw away | 82.3% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-14 — Manchester City FC vs Paris Saint-Germain FC

The model's most likely 1X2 outcome is **Paris Saint-Germain FC win** at **56.0%**. Expected goals are 1.40 for Manchester City FC and 2.20 for Paris Saint-Germain FC (3.61 combined). The most likely exact score is 1-2 at 9.2%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 69.8%; Under 3.5 goals: 51.4%; Double Chance 1X: 44.0%; Double Chance X2: 75.5%; Under 4.5 goals: 70.5%; BTTS Yes (both teams score): 66.7%; BTTS No (at least one team does not score): 33.3%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City FC win | 24.5% | 4.08 |
| Draw | 19.5% | 5.13 |
| Paris Saint-Germain FC win | 56.0% | 1.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City FC expected goals | 1.40 |
| Paris Saint-Germain FC expected goals | 2.20 |
| Expected total goals | 3.61 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
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
| 1 | 1-2 | 9.24% |
| 2 | 1-1 | 7.98% |
| 3 | 1-3 | 6.78% |
| 4 | 0-2 | 6.58% |
| 5 | 2-2 | 6.49% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | fdorg:575353 |
| Matched home-team name | Manchester City FC |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.7% |
| P btts no | 33.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.53 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.73 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.31 |
| Fair Over 3.5 odds | 2.06 |
| Fair Under 3.5 odds | 1.95 |
| Fair Over 4.5 odds | 3.39 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 56.0% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 51.4% |
| Raw p btts yes | 66.7% |
| P home draw | 44.0% |
| P draw away | 75.5% |
| Raw p home draw | 44.0% |
| Raw p draw away | 75.5% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-14 — Real Betis Balompié vs FC Porto

The model's most likely 1X2 outcome is **Real Betis Balompié win** at **73.4%**. Expected goals are 3.12 for Real Betis Balompié and 1.31 for FC Porto (4.43 combined). The most likely exact score is 3-1 at 7.9%. Goal-market probabilities: at least one goal: 99.1%; Over 2.5 goals: 81.8%; Under 3.5 goals: 35.5%; Double Chance 1X: 86.9%; Double Chance X2: 26.6%; Under 4.5 goals: 54.6%; BTTS Yes (both teams score): 69.6%; BTTS No (at least one team does not score): 30.4%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis Balompié win | 73.4% | 1.36 |
| Draw | 13.5% | 7.39 |
| FC Porto win | 13.1% | 7.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis Balompié expected goals | 3.12 |
| FC Porto expected goals | 1.31 |
| Expected total goals | 4.43 |
| Over 0.5 | 99.1% |
| Under 0.5 | 0.9% |
| Over 1.5 | 93.3% |
| Under 1.5 | 6.7% |
| Over 2.5 | 81.8% |
| Under 2.5 | 18.2% |
| Over 3.5 | 64.5% |
| Under 3.5 | 35.5% |
| Over 4.5 | 45.4% |
| Under 4.5 | 54.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.90% |
| 2 | 2-1 | 7.60% |
| 3 | 4-1 | 6.16% |
| 4 | 3-0 | 6.02% |
| 5 | 2-0 | 5.79% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | fdorg:575356 |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | FC Porto |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 69.6% |
| P btts no | 30.4% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 105.36 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.88 |
| Fair Over 2.5 odds | 1.22 |
| Fair Under 2.5 odds | 5.50 |
| Fair Over 3.5 odds | 1.55 |
| Fair Under 3.5 odds | 2.82 |
| Fair Over 4.5 odds | 2.20 |
| Fair Under 4.5 odds | 1.83 |
| Unadjusted home-win probability | 73.4% |
| Unadjusted draw probability | 13.5% |
| Unadjusted away-win probability | 13.1% |
| Raw p over 1 5 | 93.3% |
| Raw p under 3 5 | 35.5% |
| Raw p btts yes | 69.6% |
| P home draw | 86.9% |
| P draw away | 26.6% |
| Raw p home draw | 86.9% |
| Raw p draw away | 26.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-14 — ŠK Slovan Bratislava vs VfB Stuttgart

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **59.0%**. Expected goals are 1.37 for ŠK Slovan Bratislava and 2.32 for VfB Stuttgart (3.70 combined). The most likely exact score is 1-2 at 9.2%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 71.4%; Under 3.5 goals: 49.5%; Double Chance 1X: 41.0%; Double Chance X2: 77.7%; Under 4.5 goals: 68.8%; BTTS Yes (both teams score): 67.0%; BTTS No (at least one team does not score): 33.0%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ŠK Slovan Bratislava win | 22.3% | 4.48 |
| Draw | 18.7% | 5.35 |
| VfB Stuttgart win | 59.0% | 1.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ŠK Slovan Bratislava expected goals | 1.37 |
| VfB Stuttgart expected goals | 2.32 |
| Expected total goals | 3.70 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 87.9% |
| Under 1.5 | 12.1% |
| Over 2.5 | 71.4% |
| Under 2.5 | 28.6% |
| Over 3.5 | 50.5% |
| Under 3.5 | 49.5% |
| Over 4.5 | 31.2% |
| Under 4.5 | 68.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.19% |
| 2 | 1-1 | 7.53% |
| 3 | 1-3 | 7.11% |
| 4 | 0-2 | 6.69% |
| 5 | 2-2 | 6.32% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-14T19:00:00+00:00 |
| Fixture id | fdorg:575358 |
| Matched home-team name | ŠK Slovan Bratislava |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 67.0% |
| P btts no | 33.0% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 47.90 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.29 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.49 |
| Fair Over 3.5 odds | 1.98 |
| Fair Under 3.5 odds | 2.02 |
| Fair Over 4.5 odds | 3.21 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 59.0% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 49.5% |
| Raw p btts yes | 67.0% |
| P home draw | 41.0% |
| P draw away | 77.7% |
| Raw p home draw | 41.0% |
| Raw p draw away | 77.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — AS Roma vs ŠK Slovan Bratislava

The model's most likely 1X2 outcome is **AS Roma win** at **85.1%**. Expected goals are 3.05 for AS Roma and 0.63 for ŠK Slovan Bratislava (3.68 combined). The most likely exact score is 3-0 at 11.9%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 71.1%; Under 3.5 goals: 49.9%; Double Chance 1X: 94.9%; Double Chance X2: 14.9%; Under 4.5 goals: 69.2%; BTTS Yes (both teams score): 44.3%; BTTS No (at least one team does not score): 55.7%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 85.1% | 1.17 |
| Draw | 9.8% | 10.20 |
| ŠK Slovan Bratislava win | 5.1% | 19.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 3.05 |
| ŠK Slovan Bratislava expected goals | 0.63 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
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
| 1 | 3-0 | 11.92% |
| 2 | 2-0 | 11.73% |
| 3 | 4-0 | 9.08% |
| 4 | 1-0 | 7.94% |
| 5 | 3-1 | 7.52% |

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
| P btts yes | 44.3% |
| P btts no | 55.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.79 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.29 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.46 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.24 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 85.1% |
| Unadjusted draw probability | 9.8% |
| Unadjusted away-win probability | 5.1% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 49.9% |
| Raw p btts yes | 44.3% |
| P home draw | 94.9% |
| P draw away | 14.9% |
| Raw p home draw | 94.9% |
| Raw p draw away | 14.9% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — FC Porto vs PSV

The model's most likely 1X2 outcome is **FC Porto win** at **65.0%**. Expected goals are 2.34 for FC Porto and 1.12 for PSV (3.45 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 67.0%; Under 3.5 goals: 54.7%; Double Chance 1X: 82.8%; Double Chance X2: 35.0%; Under 4.5 goals: 73.5%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Porto win | 65.0% | 1.54 |
| Draw | 17.8% | 5.61 |
| PSV win | 17.2% | 5.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Porto expected goals | 2.34 |
| PSV expected goals | 1.12 |
| Expected total goals | 3.45 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 67.0% |
| Under 2.5 | 33.0% |
| Over 3.5 | 45.3% |
| Under 3.5 | 54.7% |
| Over 4.5 | 26.5% |
| Under 4.5 | 73.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.65% |
| 2 | 2-0 | 8.65% |
| 3 | 1-1 | 7.84% |
| 4 | 1-0 | 7.82% |
| 5 | 3-1 | 7.51% |

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
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.29 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.89 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.03 |
| Fair Over 3.5 odds | 2.21 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.77 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 65.0% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 17.2% |
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 54.7% |
| Raw p btts yes | 60.3% |
| P home draw | 82.8% |
| P draw away | 35.0% |
| Raw p home draw | 82.8% |
| Raw p draw away | 35.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — Fenerbahçe SK vs SK Slavia Praha

The model's most likely 1X2 outcome is **Fenerbahçe SK win** at **69.6%**. Expected goals are 1.93 for Fenerbahçe SK and 0.60 for SK Slavia Praha (2.52 combined). The most likely exact score is 1-0 at 15.9%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 46.2%; Under 3.5 goals: 75.3%; Double Chance 1X: 88.9%; Double Chance X2: 30.4%; Under 4.5 goals: 88.8%; BTTS Yes (both teams score): 37.9%; BTTS No (at least one team does not score): 62.1%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahçe SK win | 69.6% | 1.44 |
| Draw | 19.3% | 5.17 |
| SK Slavia Praha win | 11.1% | 9.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahçe SK expected goals | 1.93 |
| SK Slavia Praha expected goals | 0.60 |
| Expected total goals | 2.52 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 71.3% |
| Under 1.5 | 28.7% |
| Over 2.5 | 46.2% |
| Under 2.5 | 53.8% |
| Over 3.5 | 24.7% |
| Under 3.5 | 75.3% |
| Over 4.5 | 11.2% |
| Under 4.5 | 88.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.93% |
| 2 | 2-0 | 14.90% |
| 3 | 3-0 | 9.57% |
| 4 | 2-1 | 8.87% |
| 5 | 1-1 | 8.75% |

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
| P btts yes | 37.9% |
| P btts no | 62.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.21 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.48 |
| Fair Over 2.5 odds | 2.17 |
| Fair Under 2.5 odds | 1.86 |
| Fair Over 3.5 odds | 4.05 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.95 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 69.6% |
| Unadjusted draw probability | 19.3% |
| Unadjusted away-win probability | 11.1% |
| Raw p over 1 5 | 71.3% |
| Raw p under 3 5 | 75.3% |
| Raw p btts yes | 37.9% |
| P home draw | 88.9% |
| P draw away | 30.4% |
| Raw p home draw | 88.9% |
| Raw p draw away | 30.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — Liverpool FC vs Villarreal CF

The model's most likely 1X2 outcome is **Liverpool FC win** at **90.6%**. Expected goals are 3.32 for Liverpool FC and 0.44 for Villarreal CF (3.76 combined). The most likely exact score is 3-0 at 14.2%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 72.5%; Under 3.5 goals: 48.1%; Double Chance 1X: 97.5%; Double Chance X2: 9.4%; Under 4.5 goals: 67.6%; BTTS Yes (both teams score): 34.1%; BTTS No (at least one team does not score): 65.9%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool FC win | 90.6% | 1.10 |
| Draw | 6.8% | 14.64 |
| Villarreal CF win | 2.5% | 39.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool FC expected goals | 3.32 |
| Villarreal CF expected goals | 0.44 |
| Expected total goals | 3.76 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 72.5% |
| Under 2.5 | 27.5% |
| Over 3.5 | 51.9% |
| Under 3.5 | 48.1% |
| Over 4.5 | 32.4% |
| Under 4.5 | 67.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 14.22% |
| 2 | 2-0 | 12.84% |
| 3 | 4-0 | 11.82% |
| 4 | 1-0 | 7.89% |
| 5 | 5-0 | 7.86% |

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
| P btts yes | 34.1% |
| P btts no | 65.9% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.42 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.90 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.63 |
| Fair Over 3.5 odds | 1.93 |
| Fair Under 3.5 odds | 2.08 |
| Fair Over 4.5 odds | 3.08 |
| Fair Under 4.5 odds | 1.48 |
| Unadjusted home-win probability | 90.6% |
| Unadjusted draw probability | 6.8% |
| Unadjusted away-win probability | 2.5% |
| Raw p over 1 5 | 88.8% |
| Raw p under 3 5 | 48.1% |
| Raw p btts yes | 34.1% |
| P home draw | 97.5% |
| P draw away | 9.4% |
| Raw p home draw | 97.5% |
| Raw p draw away | 9.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — Manchester City FC vs PAE AEK

The model's most likely 1X2 outcome is **Draw** at **56.9%**. Expected goals are 0.39 for Manchester City FC and 0.26 for PAE AEK (0.66 combined). The most likely exact score is 0-0 at 51.7%. Goal-market probabilities: at least one goal: 48.3%; Over 2.5 goals: 2.9%; Under 3.5 goals: 99.5%; Double Chance 1X: 83.3%; Double Chance X2: 73.6%; Under 4.5 goals: 99.9%; BTTS Yes (both teams score): 7.2%; BTTS No (at least one team does not score): 92.8%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City FC win | 26.4% | 3.79 |
| Draw | 56.9% | 1.76 |
| PAE AEK win | 16.7% | 5.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City FC expected goals | 0.39 |
| PAE AEK expected goals | 0.26 |
| Expected total goals | 0.66 |
| Over 0.5 | 48.3% |
| Under 0.5 | 51.7% |
| Over 1.5 | 13.8% |
| Under 1.5 | 86.2% |
| Over 2.5 | 2.9% |
| Under 2.5 | 97.1% |
| Over 3.5 | 0.5% |
| Under 3.5 | 99.5% |
| Over 4.5 | 0.1% |
| Under 4.5 | 99.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 51.68% |
| 2 | 1-0 | 20.59% |
| 3 | 0-1 | 13.97% |
| 4 | 1-1 | 5.09% |
| 5 | 2-0 | 3.98% |

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
| P btts yes | 7.2% |
| P btts no | 92.8% |
| Fair Over 0.5 odds | 2.07 |
| Fair Under 0.5 odds | 1.94 |
| Fair Over 1.5 odds | 7.26 |
| Fair Under 1.5 odds | 1.16 |
| Fair Over 2.5 odds | 34.60 |
| Fair Under 2.5 odds | 1.03 |
| Fair Over 3.5 odds | 218.87 |
| Fair Under 3.5 odds | 1.00 |
| Fair Over 4.5 odds | 1710.24 |
| Fair Under 4.5 odds | 1.00 |
| Unadjusted home-win probability | 26.4% |
| Unadjusted draw probability | 56.9% |
| Unadjusted away-win probability | 16.7% |
| Raw p over 1 5 | 13.8% |
| Raw p under 3 5 | 99.5% |
| Raw p btts yes | 7.2% |
| P home draw | 83.3% |
| P draw away | 73.6% |
| Raw p home draw | 83.3% |
| Raw p draw away | 73.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — Paris Saint-Germain FC vs FC Barcelona

The model's most likely 1X2 outcome is **Paris Saint-Germain FC win** at **68.9%**. Expected goals are 3.03 for Paris Saint-Germain FC and 1.48 for FC Barcelona (4.51 combined). The most likely exact score is 3-1 at 7.5%. Goal-market probabilities: at least one goal: 99.1%; Over 2.5 goals: 82.8%; Under 3.5 goals: 34.0%; Double Chance 1X: 83.7%; Double Chance X2: 31.1%; Under 4.5 goals: 53.0%; BTTS Yes (both teams score): 73.3%; BTTS No (at least one team does not score): 26.7%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint-Germain FC win | 68.9% | 1.45 |
| Draw | 14.8% | 6.77 |
| FC Barcelona win | 16.3% | 6.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint-Germain FC expected goals | 3.03 |
| FC Barcelona expected goals | 1.48 |
| Expected total goals | 4.51 |
| Over 0.5 | 99.1% |
| Under 0.5 | 0.9% |
| Over 1.5 | 93.7% |
| Under 1.5 | 6.3% |
| Over 2.5 | 82.8% |
| Under 2.5 | 17.2% |
| Over 3.5 | 66.0% |
| Under 3.5 | 34.0% |
| Over 4.5 | 47.0% |
| Under 4.5 | 53.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.54% |
| 2 | 2-1 | 7.47% |
| 3 | 4-1 | 5.71% |
| 4 | 3-2 | 5.59% |
| 5 | 2-2 | 5.54% |

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
| P btts yes | 73.3% |
| P btts no | 26.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 117.63 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.89 |
| Fair Over 2.5 odds | 1.21 |
| Fair Under 2.5 odds | 5.81 |
| Fair Over 3.5 odds | 1.52 |
| Fair Under 3.5 odds | 2.94 |
| Fair Over 4.5 odds | 2.13 |
| Fair Under 4.5 odds | 1.89 |
| Unadjusted home-win probability | 68.9% |
| Unadjusted draw probability | 14.8% |
| Unadjusted away-win probability | 16.3% |
| Raw p over 1 5 | 93.7% |
| Raw p under 3 5 | 34.0% |
| Raw p btts yes | 73.3% |
| P home draw | 83.7% |
| P draw away | 31.1% |
| Raw p home draw | 83.7% |
| Raw p draw away | 31.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — SSC Napoli vs FK Bodø/Glimt

The model's most likely 1X2 outcome is **FK Bodø/Glimt win** at **47.8%**. Expected goals are 1.40 for SSC Napoli and 1.81 for FK Bodø/Glimt (3.21 combined). The most likely exact score is 1-1 at 9.7%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 62.3%; Under 3.5 goals: 59.9%; Double Chance 1X: 52.2%; Double Chance X2: 69.6%; Under 4.5 goals: 77.8%; BTTS Yes (both teams score): 62.6%; BTTS No (at least one team does not score): 37.4%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SSC Napoli win | 30.4% | 3.29 |
| Draw | 21.8% | 4.58 |
| FK Bodø/Glimt win | 47.8% | 2.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SSC Napoli expected goals | 1.40 |
| FK Bodø/Glimt expected goals | 1.81 |
| Expected total goals | 3.21 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 82.5% |
| Under 1.5 | 17.5% |
| Over 2.5 | 62.3% |
| Under 2.5 | 37.7% |
| Over 3.5 | 40.1% |
| Under 3.5 | 59.9% |
| Over 4.5 | 22.2% |
| Under 4.5 | 77.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.70% |
| 2 | 1-2 | 9.25% |
| 3 | 0-1 | 7.80% |
| 4 | 2-1 | 7.15% |
| 5 | 0-2 | 6.61% |

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
| P btts yes | 62.6% |
| P btts no | 37.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.49 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.73 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.65 |
| Fair Over 3.5 odds | 2.50 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.51 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 30.4% |
| Unadjusted draw probability | 21.8% |
| Unadjusted away-win probability | 47.8% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 59.9% |
| Raw p btts yes | 62.6% |
| P home draw | 52.2% |
| P draw away | 69.6% |
| Raw p home draw | 52.2% |
| Raw p draw away | 69.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — Sabah FK vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **77.8%**. Expected goals are 0.65 for Sabah FK and 2.48 for Borussia Dortmund (3.14 combined). The most likely exact score is 0-2 at 13.4%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 60.7%; Under 3.5 goals: 61.6%; Double Chance 1X: 22.2%; Double Chance X2: 91.9%; Under 4.5 goals: 79.2%; BTTS Yes (both teams score): 43.7%; BTTS No (at least one team does not score): 56.3%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 8.1% | 12.33 |
| Draw | 14.1% | 7.08 |
| Borussia Dortmund win | 77.8% | 1.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.65 |
| Borussia Dortmund expected goals | 2.48 |
| Expected total goals | 3.14 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 60.7% |
| Under 2.5 | 39.3% |
| Over 3.5 | 38.4% |
| Under 3.5 | 61.6% |
| Over 4.5 | 20.8% |
| Under 4.5 | 79.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 13.38% |
| 2 | 0-1 | 11.13% |
| 3 | 0-3 | 11.08% |
| 4 | 1-2 | 8.75% |
| 5 | 1-3 | 7.25% |

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
| P btts yes | 43.7% |
| P btts no | 56.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.09 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.46 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.61 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.80 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 8.1% |
| Unadjusted draw probability | 14.1% |
| Unadjusted away-win probability | 77.8% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 61.6% |
| Raw p btts yes | 43.7% |
| P home draw | 22.2% |
| P draw away | 91.9% |
| Raw p home draw | 22.2% |
| Raw p draw away | 91.9% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-20 — VfB Stuttgart vs Club Atlético de Madrid

The model's most likely 1X2 outcome is **Club Atlético de Madrid win** at **65.3%**. Expected goals are 1.28 for VfB Stuttgart and 2.55 for Club Atlético de Madrid (3.83 combined). The most likely exact score is 1-2 at 9.0%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 73.6%; Under 3.5 goals: 46.7%; Double Chance 1X: 34.7%; Double Chance X2: 82.2%; Under 4.5 goals: 66.1%; BTTS Yes (both teams score): 66.3%; BTTS No (at least one team does not score): 33.7%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 17.8% | 5.61 |
| Draw | 16.9% | 5.92 |
| Club Atlético de Madrid win | 65.3% | 1.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 1.28 |
| Club Atlético de Madrid expected goals | 2.55 |
| Expected total goals | 3.83 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 89.2% |
| Under 1.5 | 10.8% |
| Over 2.5 | 73.6% |
| Under 2.5 | 26.4% |
| Over 3.5 | 53.3% |
| Under 3.5 | 46.7% |
| Over 4.5 | 33.9% |
| Under 4.5 | 66.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.03% |
| 2 | 1-3 | 7.68% |
| 3 | 0-2 | 7.05% |
| 4 | 1-1 | 6.72% |
| 5 | 0-3 | 6.00% |

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
| P btts yes | 66.3% |
| P btts no | 33.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.27 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.25 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.79 |
| Fair Over 3.5 odds | 1.87 |
| Fair Under 3.5 odds | 2.14 |
| Fair Over 4.5 odds | 2.95 |
| Fair Under 4.5 odds | 1.51 |
| Unadjusted home-win probability | 17.8% |
| Unadjusted draw probability | 16.9% |
| Unadjusted away-win probability | 65.3% |
| Raw p over 1 5 | 89.2% |
| Raw p under 3 5 | 46.7% |
| Raw p btts yes | 66.3% |
| P home draw | 34.7% |
| P draw away | 82.2% |
| Raw p home draw | 34.7% |
| Raw p draw away | 82.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Aston Villa FC vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa FC win** at **85.3%**. Expected goals are 3.82 for Aston Villa FC and 1.08 for Viking FK (4.90 combined). The most likely exact score is 3-1 at 7.5%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 86.7%; Under 3.5 goals: 28.0%; Double Chance 1X: 93.8%; Double Chance X2: 14.7%; Under 4.5 goals: 45.9%; BTTS Yes (both teams score): 64.4%; BTTS No (at least one team does not score): 35.6%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa FC win | 85.3% | 1.17 |
| Draw | 8.6% | 11.68 |
| Viking FK win | 6.2% | 16.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa FC expected goals | 3.82 |
| Viking FK expected goals | 1.08 |
| Expected total goals | 4.90 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 95.4% |
| Under 1.5 | 4.6% |
| Over 2.5 | 86.7% |
| Under 2.5 | 13.3% |
| Over 3.5 | 72.0% |
| Under 3.5 | 28.0% |
| Over 4.5 | 54.1% |
| Under 4.5 | 45.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.48% |
| 2 | 4-1 | 7.15% |
| 3 | 3-0 | 6.94% |
| 4 | 4-0 | 6.64% |
| 5 | 2-1 | 5.87% |

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
| P btts yes | 64.4% |
| P btts no | 35.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 169.05 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 21.98 |
| Fair Over 2.5 odds | 1.15 |
| Fair Under 2.5 odds | 7.49 |
| Fair Over 3.5 odds | 1.39 |
| Fair Under 3.5 odds | 3.58 |
| Fair Over 4.5 odds | 1.85 |
| Fair Under 4.5 odds | 2.18 |
| Unadjusted home-win probability | 85.3% |
| Unadjusted draw probability | 8.6% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 95.4% |
| Raw p under 3 5 | 28.0% |
| Raw p btts yes | 64.4% |
| P home draw | 93.8% |
| P draw away | 14.7% |
| Raw p home draw | 93.8% |
| Raw p draw away | 14.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Club Brugge KV vs Racing Club de Lens

The model's most likely 1X2 outcome is **Club Brugge KV win** at **64.2%**. Expected goals are 2.44 for Club Brugge KV and 1.23 for Racing Club de Lens (3.67 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 70.9%; Under 3.5 goals: 50.1%; Double Chance 1X: 81.7%; Double Chance X2: 35.8%; Under 4.5 goals: 69.3%; BTTS Yes (both teams score): 64.3%; BTTS No (at least one team does not score): 35.7%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge KV win | 64.2% | 1.56 |
| Draw | 17.5% | 5.70 |
| Racing Club de Lens win | 18.3% | 5.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Club Brugge KV expected goals | 2.44 |
| Racing Club de Lens expected goals | 1.23 |
| Expected total goals | 3.67 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 70.9% |
| Under 2.5 | 29.1% |
| Over 3.5 | 49.9% |
| Under 3.5 | 50.1% |
| Over 4.5 | 30.7% |
| Under 4.5 | 69.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.33% |
| 2 | 3-1 | 7.57% |
| 3 | 2-0 | 7.56% |
| 4 | 1-1 | 7.28% |
| 5 | 1-0 | 6.59% |

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
| P btts yes | 64.3% |
| P btts no | 35.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.18 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.44 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.26 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 64.2% |
| Unadjusted draw probability | 17.5% |
| Unadjusted away-win probability | 18.3% |
| Raw p over 1 5 | 87.7% |
| Raw p under 3 5 | 50.1% |
| Raw p btts yes | 64.3% |
| P home draw | 81.7% |
| P draw away | 35.8% |
| Raw p home draw | 81.7% |
| Raw p draw away | 35.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Como 1907 vs Manchester United FC

The model's most likely 1X2 outcome is **Como 1907 win** at **65.6%**. Expected goals are 3.52 for Como 1907 and 2.07 for Manchester United FC (5.59 combined). The most likely exact score is 3-2 at 5.8%. Goal-market probabilities: at least one goal: 99.8%; Over 2.5 goals: 91.7%; Under 3.5 goals: 19.2%; Double Chance 1X: 79.9%; Double Chance X2: 34.4%; Under 4.5 goals: 34.4%; BTTS Yes (both teams score): 84.6%; BTTS No (at least one team does not score): 15.4%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como 1907 win | 65.6% | 1.52 |
| Draw | 14.3% | 7.01 |
| Manchester United FC win | 20.1% | 4.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como 1907 expected goals | 3.52 |
| Manchester United FC expected goals | 2.07 |
| Expected total goals | 5.59 |
| Over 0.5 | 99.8% |
| Under 0.5 | 0.2% |
| Over 1.5 | 97.4% |
| Under 1.5 | 2.6% |
| Over 2.5 | 91.7% |
| Under 2.5 | 8.3% |
| Over 3.5 | 80.8% |
| Under 3.5 | 19.2% |
| Over 4.5 | 65.6% |
| Under 4.5 | 34.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-2 | 5.82% |
| 2 | 3-1 | 5.63% |
| 3 | 4-2 | 5.13% |
| 4 | 4-1 | 4.96% |
| 5 | 2-2 | 4.96% |

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
| P btts yes | 84.6% |
| P btts no | 15.4% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 420.39 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 38.45 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 12.04 |
| Fair Over 3.5 odds | 1.24 |
| Fair Under 3.5 odds | 5.21 |
| Fair Over 4.5 odds | 1.52 |
| Fair Under 4.5 odds | 2.91 |
| Unadjusted home-win probability | 65.6% |
| Unadjusted draw probability | 14.3% |
| Unadjusted away-win probability | 20.1% |
| Raw p over 1 5 | 97.4% |
| Raw p under 3 5 | 19.2% |
| Raw p btts yes | 84.6% |
| P home draw | 79.9% |
| P draw away | 34.4% |
| Raw p home draw | 79.9% |
| Raw p draw away | 34.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — FC Bayern München vs Arsenal FC

The model's most likely 1X2 outcome is **Arsenal FC win** at **45.5%**. Expected goals are 1.00 for FC Bayern München and 1.35 for Arsenal FC (2.36 combined). The most likely exact score is 0-1 at 13.5%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 41.9%; Under 3.5 goals: 78.8%; Double Chance 1X: 54.5%; Double Chance X2: 71.7%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 46.3%; BTTS No (at least one team does not score): 53.7%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Bayern München win | 28.3% | 3.53 |
| Draw | 26.1% | 3.83 |
| Arsenal FC win | 45.5% | 2.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Bayern München expected goals | 1.00 |
| Arsenal FC expected goals | 1.35 |
| Expected total goals | 2.36 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 67.5% |
| Under 1.5 | 32.5% |
| Over 2.5 | 41.9% |
| Under 2.5 | 58.1% |
| Over 3.5 | 21.2% |
| Under 3.5 | 78.8% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.48% |
| 2 | 1-1 | 12.22% |
| 3 | 1-0 | 10.13% |
| 4 | 0-0 | 8.83% |
| 5 | 1-2 | 8.71% |

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
| P btts yes | 46.3% |
| P btts no | 53.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.32 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.08 |
| Fair Over 2.5 odds | 2.39 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.71 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.05 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 28.3% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 45.5% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 78.8% |
| Raw p btts yes | 46.3% |
| P home draw | 54.5% |
| P draw away | 71.7% |
| Raw p home draw | 54.5% |
| Raw p draw away | 71.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — FC Internazionale Milano vs FK Shakhtar Donetsk

The model's most likely 1X2 outcome is **FC Internazionale Milano win** at **65.4%**. Expected goals are 1.93 for FC Internazionale Milano and 0.77 for FK Shakhtar Donetsk (2.70 combined). The most likely exact score is 1-0 at 13.5%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 50.5%; Under 3.5 goals: 71.5%; Double Chance 1X: 85.4%; Double Chance X2: 34.6%; Under 4.5 goals: 86.3%; BTTS Yes (both teams score): 45.2%; BTTS No (at least one team does not score): 54.8%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Internazionale Milano win | 65.4% | 1.53 |
| Draw | 20.1% | 4.98 |
| FK Shakhtar Donetsk win | 14.6% | 6.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Internazionale Milano expected goals | 1.93 |
| FK Shakhtar Donetsk expected goals | 0.77 |
| Expected total goals | 2.70 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.5% |
| Under 3.5 | 71.5% |
| Over 4.5 | 13.7% |
| Under 4.5 | 86.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.52% |
| 2 | 2-0 | 12.57% |
| 3 | 2-1 | 9.63% |
| 4 | 1-1 | 9.47% |
| 5 | 3-0 | 8.09% |

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
| P btts yes | 45.2% |
| P btts no | 54.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.01 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.93 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.51 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.33 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 65.4% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 14.6% |
| Raw p over 1 5 | 74.6% |
| Raw p under 3 5 | 71.5% |
| Raw p btts yes | 45.2% |
| P home draw | 85.4% |
| P draw away | 34.6% |
| Raw p home draw | 85.4% |
| Raw p draw away | 34.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Lille OSC vs Galatasaray SK

The model's most likely 1X2 outcome is **Lille OSC win** at **74.4%**. Expected goals are 2.75 for Lille OSC and 1.00 for Galatasaray SK (3.75 combined). The most likely exact score is 2-0 at 8.9%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 72.3%; Under 3.5 goals: 48.4%; Double Chance 1X: 88.6%; Double Chance X2: 25.6%; Under 4.5 goals: 67.8%; BTTS Yes (both teams score): 58.8%; BTTS No (at least one team does not score): 41.2%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille OSC win | 74.4% | 1.34 |
| Draw | 14.2% | 7.03 |
| Galatasaray SK win | 11.4% | 8.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille OSC expected goals | 2.75 |
| Galatasaray SK expected goals | 1.00 |
| Expected total goals | 3.75 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 88.5% |
| Under 1.5 | 11.5% |
| Over 2.5 | 72.3% |
| Under 2.5 | 27.7% |
| Over 3.5 | 51.6% |
| Under 3.5 | 48.4% |
| Over 4.5 | 32.2% |
| Under 4.5 | 67.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 8.91% |
| 2 | 2-1 | 8.89% |
| 3 | 3-0 | 8.17% |
| 4 | 3-1 | 8.15% |
| 5 | 1-0 | 6.80% |

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
| P btts yes | 58.8% |
| P btts no | 41.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 49.19 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.69 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.60 |
| Fair Over 3.5 odds | 1.94 |
| Fair Under 3.5 odds | 2.07 |
| Fair Over 4.5 odds | 3.11 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 74.4% |
| Unadjusted draw probability | 14.2% |
| Unadjusted away-win probability | 11.4% |
| Raw p over 1 5 | 88.5% |
| Raw p under 3 5 | 48.4% |
| Raw p btts yes | 58.8% |
| P home draw | 88.6% |
| P draw away | 25.6% |
| Raw p home draw | 88.6% |
| Raw p draw away | 25.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Real Betis Balompié vs Feyenoord Rotterdam

The model's most likely 1X2 outcome is **Real Betis Balompié win** at **95.8%**. Expected goals are 6.31 for Real Betis Balompié and 1.27 for Feyenoord Rotterdam (7.58 combined). The most likely exact score is 6-1 at 6.0%. Goal-market probabilities: at least one goal: 100.0%; Over 2.5 goals: 98.0%; Under 3.5 goals: 6.0%; Double Chance 1X: 98.4%; Double Chance X2: 4.2%; Under 4.5 goals: 13.4%; BTTS Yes (both teams score): 71.6%; BTTS No (at least one team does not score): 28.4%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis Balompié win | 95.8% | 1.04 |
| Draw | 2.6% | 38.15 |
| Feyenoord Rotterdam win | 1.6% | 62.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis Balompié expected goals | 6.31 |
| Feyenoord Rotterdam expected goals | 1.27 |
| Expected total goals | 7.58 |
| Over 0.5 | 100.0% |
| Under 0.5 | 0.0% |
| Over 1.5 | 99.5% |
| Under 1.5 | 0.5% |
| Over 2.5 | 98.0% |
| Under 2.5 | 2.0% |
| Over 3.5 | 94.0% |
| Under 3.5 | 6.0% |
| Over 4.5 | 86.6% |
| Under 4.5 | 13.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 6-1 | 6.03% |
| 2 | 5-1 | 5.74% |
| 3 | 7-1 | 5.44% |
| 4 | 6-0 | 4.76% |
| 5 | 4-1 | 4.55% |

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
| P btts yes | 71.6% |
| P btts no | 28.4% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 3062.82 |
| Fair Over 1.5 odds | 1.00 |
| Fair Under 1.5 odds | 204.96 |
| Fair Over 2.5 odds | 1.02 |
| Fair Under 2.5 odds | 49.36 |
| Fair Over 3.5 odds | 1.06 |
| Fair Under 3.5 odds | 16.76 |
| Fair Over 4.5 odds | 1.16 |
| Fair Under 4.5 odds | 7.45 |
| Unadjusted home-win probability | 95.8% |
| Unadjusted draw probability | 2.6% |
| Unadjusted away-win probability | 1.6% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.0% |
| Raw p btts yes | 71.6% |
| P home draw | 98.4% |
| P draw away | 4.2% |
| Raw p home draw | 98.4% |
| Raw p draw away | 4.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Real Madrid CF vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid CF win** at **77.6%**. Expected goals are 2.83 for Real Madrid CF and 0.89 for RB Leipzig (3.72 combined). The most likely exact score is 2-0 at 9.7%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 71.8%; Under 3.5 goals: 49.0%; Double Chance 1X: 90.7%; Double Chance X2: 22.4%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 55.3%; BTTS No (at least one team does not score): 44.7%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid CF win | 77.6% | 1.29 |
| Draw | 13.0% | 7.66 |
| RB Leipzig win | 9.3% | 10.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid CF expected goals | 2.83 |
| RB Leipzig expected goals | 0.89 |
| Expected total goals | 3.72 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 88.3% |
| Under 1.5 | 11.7% |
| Over 2.5 | 71.8% |
| Under 2.5 | 28.2% |
| Over 3.5 | 51.0% |
| Under 3.5 | 49.0% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.68% |
| 2 | 3-0 | 9.13% |
| 3 | 2-1 | 8.64% |
| 4 | 3-1 | 8.15% |
| 5 | 1-0 | 7.15% |

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
| P btts yes | 55.3% |
| P btts no | 44.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 47.33 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.53 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.55 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 77.6% |
| Unadjusted draw probability | 13.0% |
| Unadjusted away-win probability | 9.3% |
| Raw p over 1 5 | 88.3% |
| Raw p under 3 5 | 49.0% |
| Raw p btts yes | 55.3% |
| P home draw | 90.7% |
| P draw away | 22.4% |
| Raw p home draw | 90.7% |
| Raw p draw away | 22.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---

## 2026-10-21 — Sporting Clube de Portugal vs LASK Linz

The model's most likely 1X2 outcome is **Sporting Clube de Portugal win** at **86.9%**. Expected goals are 6.35 for Sporting Clube de Portugal and 2.48 for LASK Linz (8.84 combined). The most likely exact score is 6-2 at 4.3%. Goal-market probabilities: at least one goal: 100.0%; Over 2.5 goals: 99.2%; Under 3.5 goals: 2.5%; Double Chance 1X: 93.1%; Double Chance X2: 13.1%; Under 4.5 goals: 6.5%; BTTS Yes (both teams score): 91.5%; BTTS No (at least one team does not score): 8.5%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Clube de Portugal win | 86.9% | 1.15 |
| Draw | 6.2% | 16.01 |
| LASK Linz win | 6.9% | 14.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Clube de Portugal expected goals | 6.35 |
| LASK Linz expected goals | 2.48 |
| Expected total goals | 8.84 |
| Over 0.5 | 100.0% |
| Under 0.5 | 0.0% |
| Over 1.5 | 99.8% |
| Under 1.5 | 0.2% |
| Over 2.5 | 99.2% |
| Under 2.5 | 0.8% |
| Over 3.5 | 97.5% |
| Under 3.5 | 2.5% |
| Over 4.5 | 93.5% |
| Under 4.5 | 6.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 6-2 | 4.35% |
| 2 | 5-2 | 4.11% |
| 3 | 7-2 | 3.95% |
| 4 | 6-3 | 3.60% |
| 5 | 6-1 | 3.50% |

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
| P btts yes | 91.5% |
| P btts no | 8.5% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 30652.42 |
| Fair Over 1.5 odds | 1.00 |
| Fair Under 1.5 odds | 609.12 |
| Fair Over 2.5 odds | 1.01 |
| Fair Under 2.5 odds | 132.42 |
| Fair Over 3.5 odds | 1.03 |
| Fair Under 3.5 odds | 39.50 |
| Fair Over 4.5 odds | 1.07 |
| Fair Under 4.5 odds | 15.49 |
| Unadjusted home-win probability | 86.9% |
| Unadjusted draw probability | 6.2% |
| Unadjusted away-win probability | 6.9% |
| Raw p over 1 5 | 99.8% |
| Raw p under 3 5 | 2.5% |
| Raw p btts yes | 91.5% |
| P home draw | 93.1% |
| P draw away | 13.1% |
| Raw p home draw | 93.1% |
| Raw p draw away | 13.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |

</details>


---
