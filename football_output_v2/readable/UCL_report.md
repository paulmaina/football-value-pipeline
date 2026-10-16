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
| Training sha256 | 151908a7d85ae07b135d92320a2fb933f75258db10cf07dc00616cda78960fcd |
| Optimizer objective | 970.507 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.306 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0009 |
| Training data health | {'completed_matches': 36, 'latest_completed_utc': '2026-10-14T19:00:00+00:00', 'latest_completed_date': '2026-10-14', 'next_fixture_utc': '2026-10-20T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-16T22:16:18.798275+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '3ab6771d715639eadc5fec362472afa8830202d73e32478a8fa89583a4928546', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0011546202777777779, 'training_end': '2026-10-14', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 44.00 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-20 — AS Roma vs ŠK Slovan Bratislava

The model's most likely 1X2 outcome is **AS Roma win** at **82.8%**. Expected goals are 3.76 for AS Roma and 1.32 for ŠK Slovan Bratislava (5.08 combined). The most likely exact score is 3-1 at 7.4%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 88.3%; Under 3.5 goals: 25.1%; Double Chance 1X: 93.3%; Double Chance X2: 17.2%; Double Chance 12 (either team wins): 89.6%; Under 4.5 goals: 42.5%; BTTS Yes (both teams score): 71.2%; BTTS No (at least one team does not score): 28.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 82.8% | 1.21 |
| Draw | 10.4% | 9.58 |
| ŠK Slovan Bratislava win | 6.7% | 14.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 3.76 |
| ŠK Slovan Bratislava expected goals | 1.32 |
| Expected total goals | 5.08 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 88.3% |
| Under 2.5 | 11.7% |
| Over 3.5 | 74.9% |
| Under 3.5 | 25.1% |
| Over 4.5 | 57.5% |
| Under 4.5 | 42.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.44% |
| 2 | 4-1 | 6.99% |
| 3 | 2-1 | 5.93% |
| 4 | 3-0 | 5.65% |
| 5 | 4-0 | 5.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 82.8% | 84.6% | 1.23 | +1.9% |
| Draw | 10.4% | 10.8% | 6.96 | -27.3% |
| ŠK Slovan Bratislava win | 6.7% | 4.7% | 16.50 | +10.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | e3b50e57c4cf46191ab068d1e880e595 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:04Z |
| Market best draw last update utc | 2026-10-16T22:16:04Z |
| Market best away last update utc | 2026-10-16T22:16:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 71.2% |
| P btts no | 28.8% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 206.14 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.38 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.51 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 3.99 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.35 |
| Unadjusted home-win probability | 81.1% |
| Unadjusted draw probability | 10.1% |
| Unadjusted away-win probability | 8.8% |
| Raw p over 1 5 | 96.0% |
| Raw p under 3 5 | 25.5% |
| Raw p btts yes | 71.3% |
| P home draw | 93.3% |
| P draw away | 17.2% |
| P home away | 89.6% |
| Raw p home draw | 91.2% |
| Raw p draw away | 18.9% |
| Raw p home away | 89.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.16 |
| Reference draw odds | 7.19 |
| Reference away odds | 15.03 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.40 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | -1.7% |
| Draw probability edge | -0.3% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +13.7% |
| Under 2.5 probability edge | -13.7% |
| Raw edge prob home | -0.0344 |
| Raw ev home | -0.0023 |
| Raw edge prob draw | -0.0064 |
| Raw ev draw | -0.2953 |
| Raw edge prob away | 0.0408 |
| Raw ev away | 0.4453 |

</details>


---

## 2026-10-20 — Fenerbahce vs Slavia Praha

The model's most likely 1X2 outcome is **Fenerbahce win** at **42.6%**. Expected goals are 0.78 for Fenerbahce and 1.07 for Slavia Praha (1.84 combined). The most likely exact score is 1-0 at 20.6%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 28.6%; Under 3.5 goals: 88.8%; Double Chance 1X: 69.3%; Double Chance X2: 57.4%; Double Chance 12 (either team wins): 73.4%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 34.0%; BTTS No (at least one team does not score): 66.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 42.6% | 2.34 |
| Draw | 26.6% | 3.76 |
| Slavia Praha win | 30.7% | 3.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 0.78 |
| Slavia Praha expected goals | 1.07 |
| Expected total goals | 1.84 |
| Over 0.5 | 86.8% |
| Under 0.5 | 13.2% |
| Over 1.5 | 53.5% |
| Under 1.5 | 46.5% |
| Over 2.5 | 28.6% |
| Under 2.5 | 71.4% |
| Over 3.5 | 11.2% |
| Under 3.5 | 88.8% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.58% |
| 2 | 0-0 | 13.21% |
| 3 | 0-1 | 12.68% |
| 4 | 1-1 | 10.83% |
| 5 | 2-1 | 8.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 42.6% | 58.5% | 1.74 | -25.8% |
| Draw | 26.6% | 22.6% | 4.31 | +14.8% |
| Slavia Praha win | 30.7% | 18.9% | 4.83 | +48.4% |
| Over 2.5 | 28.6% | 58.0% | 1.69 | -51.6% |
| Under 2.5 | 71.4% | 42.0% | 2.36 | +68.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T16:45:00+00:00 |
| Fixture id | 16e237246e9bef441e69998d1ef9536d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:04Z |
| Market best draw last update utc | 2026-10-16T22:16:04Z |
| Market best away last update utc | 2026-10-16T22:16:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fenerbahçe SK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 34.0% |
| P btts no | 66.0% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.57 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.49 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.91 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 25.08 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 42.6% |
| Raw p over 1 5 | 54.3% |
| Raw p under 3 5 | 88.4% |
| Raw p btts yes | 34.7% |
| P home draw | 69.3% |
| P draw away | 57.4% |
| P home away | 73.4% |
| Raw p home draw | 57.4% |
| Raw p draw away | 73.2% |
| Raw p home away | 69.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.66 |
| Reference draw odds | 4.07 |
| Reference away odds | 4.83 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:23Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:23Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:04Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:04Z |
| Home probability edge | -15.8% |
| Draw probability edge | +4.0% |
| Away probability edge | +11.8% |
| Over 2.5 probability edge | -29.4% |
| Under 2.5 probability edge | +29.4% |
| Raw edge prob home | -0.3167 |
| Raw ev home | -0.5334 |
| Raw edge prob draw | 0.0798 |
| Raw ev draw | 0.3195 |
| Raw edge prob away | 0.2368 |
| Raw ev away | 1.0560 |

</details>


---

## 2026-10-20 — Liverpool vs Villarreal

The model's most likely 1X2 outcome is **Liverpool win** at **77.0%**. Expected goals are 3.36 for Liverpool and 0.51 for Villarreal (3.86 combined). The most likely exact score is 3-0 at 11.4%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 68.7%; Under 3.5 goals: 50.7%; Double Chance 1X: 90.9%; Double Chance X2: 23.0%; Double Chance 12 (either team wins): 86.1%; Under 4.5 goals: 69.4%; BTTS Yes (both teams score): 41.4%; BTTS No (at least one team does not score): 58.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 77.0% | 1.30 |
| Draw | 13.9% | 7.20 |
| Villarreal win | 9.1% | 10.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 3.36 |
| Villarreal expected goals | 0.51 |
| Expected total goals | 3.86 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 86.2% |
| Under 1.5 | 13.8% |
| Over 2.5 | 68.7% |
| Under 2.5 | 31.3% |
| Over 3.5 | 49.3% |
| Under 3.5 | 50.7% |
| Over 4.5 | 30.6% |
| Under 4.5 | 69.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 11.35% |
| 2 | 2-0 | 10.15% |
| 3 | 4-0 | 9.52% |
| 4 | 1-1 | 6.59% |
| 5 | 5-0 | 6.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 77.0% | 64.1% | 1.57 | +20.9% |
| Draw | 13.9% | 20.6% | 4.72 | -34.4% |
| Villarreal win | 9.1% | 15.2% | 5.96 | -45.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | b9567e9c3df909f8f6f21425b4b38d3f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:04Z |
| Market best draw last update utc | 2026-10-16T22:16:04Z |
| Market best away last update utc | 2026-10-16T22:16:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool FC |
| Matched away-team name | Villarreal CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 41.4% |
| P btts no | 58.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.70 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.27 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.19 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.97 |
| Fair Over 4.5 odds | 3.27 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 89.9% |
| Unadjusted draw probability | 7.2% |
| Unadjusted away-win probability | 3.0% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 46.1% |
| Raw p btts yes | 38.1% |
| P home draw | 90.9% |
| P draw away | 23.0% |
| P home away | 86.1% |
| Raw p home draw | 97.0% |
| Raw p draw away | 10.1% |
| Raw p home away | 92.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.52 |
| Reference draw odds | 4.42 |
| Reference away odds | 5.88 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | +12.9% |
| Draw probability edge | -6.7% |
| Away probability edge | -6.1% |
| Over 2.5 probability edge | +4.9% |
| Under 2.5 probability edge | -4.9% |
| Raw edge prob home | 0.2576 |
| Raw ev home | 0.4110 |
| Raw edge prob draw | -0.1349 |
| Raw ev draw | -0.6625 |
| Raw edge prob away | -0.1227 |
| Raw ev away | -0.8228 |

</details>


---

## 2026-10-20 — Manchester City vs AEK Athens

The model's most likely 1X2 outcome is **Manchester City win** at **79.8%**. Expected goals are 2.34 for Manchester City and 1.07 for AEK Athens (3.40 combined). The most likely exact score is 2-1 at 11.7%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 69.0%; Under 3.5 goals: 54.0%; Double Chance 1X: 91.1%; Double Chance X2: 20.2%; Double Chance 12 (either team wins): 88.7%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 56.4%; BTTS No (at least one team does not score): 43.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 79.8% | 1.25 |
| Draw | 11.3% | 8.85 |
| AEK Athens win | 8.9% | 11.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 2.34 |
| AEK Athens expected goals | 1.07 |
| Expected total goals | 3.40 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 69.0% |
| Under 2.5 | 31.0% |
| Over 3.5 | 46.0% |
| Under 3.5 | 54.0% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.69% |
| 2 | 2-0 | 10.97% |
| 3 | 1-0 | 9.89% |
| 4 | 3-1 | 9.10% |
| 5 | 3-0 | 8.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 79.8% | 93.4% | 1.07 | -14.7% |
| Draw | 11.3% | 5.0% | 17.00 | +92.1% |
| AEK Athens win | 8.9% | 1.6% | 42.00 | +275.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | 00625830dd764a06f12f78c0d0a72ff8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:04Z |
| Market best draw last update utc | 2026-10-16T22:16:04Z |
| Market best away last update utc | 2026-10-16T22:16:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Manchester City FC |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 67/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 53.46 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.17 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.23 |
| Fair Over 3.5 odds | 2.18 |
| Fair Under 3.5 odds | 1.85 |
| Fair Over 4.5 odds | 3.62 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 66.1% |
| Unadjusted draw probability | 17.6% |
| Unadjusted away-win probability | 16.3% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 55.8% |
| Raw p btts yes | 58.8% |
| P home draw | 91.1% |
| P draw away | 20.2% |
| P home away | 88.7% |
| Raw p home draw | 83.7% |
| Raw p draw away | 33.9% |
| Raw p home away | 82.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.06 |
| Reference draw odds | 13.00 |
| Reference away odds | 34.00 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:22Z |
| Market reference home last update utc | 2026-10-16T22:16:22Z |
| Market reference draw last update utc | 2026-10-16T22:16:22Z |
| Market reference away last update utc | 2026-10-16T22:16:22Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.75 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | -13.6% |
| Draw probability edge | +6.3% |
| Away probability edge | +7.3% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.2729 |
| Raw ev home | -0.2925 |
| Raw edge prob draw | 0.1266 |
| Raw ev draw | 1.9970 |
| Raw edge prob away | 0.1464 |
| Raw ev away | 5.8253 |

</details>


---

## 2026-10-20 — Napoli vs Bodø/Glimt

The model's most likely 1X2 outcome is **Napoli win** at **43.7%**. Expected goals are 1.17 for Napoli and 1.78 for Bodø/Glimt (2.94 combined). The most likely exact score is 1-0 at 11.4%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 55.7%; Under 3.5 goals: 67.3%; Double Chance 1X: 65.1%; Double Chance X2: 56.3%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 43.7% | 2.29 |
| Draw | 21.4% | 4.66 |
| Bodø/Glimt win | 34.9% | 2.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.17 |
| Bodø/Glimt expected goals | 1.78 |
| Expected total goals | 2.94 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 55.7% |
| Under 2.5 | 44.3% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.44% |
| 2 | 2-1 | 10.89% |
| 3 | 1-1 | 10.00% |
| 4 | 0-1 | 6.61% |
| 5 | 1-2 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 43.7% | 61.8% | 1.64 | -28.4% |
| Draw | 21.4% | 20.7% | 4.67 | +0.2% |
| Bodø/Glimt win | 34.9% | 17.5% | 5.18 | +80.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | 49dba87d5ac664efdf2a64c72db31702 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:04Z |
| Market best draw last update utc | 2026-10-16T22:16:04Z |
| Market best away last update utc | 2026-10-16T22:16:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | SSC Napoli |
| Matched away-team name | FK Bodø/Glimt |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.97 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.42 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 5.89 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 25.5% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 52.3% |
| Raw p over 1 5 | 78.7% |
| Raw p under 3 5 | 66.0% |
| Raw p btts yes | 56.7% |
| P home draw | 65.1% |
| P draw away | 56.3% |
| P home away | 78.6% |
| Raw p home draw | 47.7% |
| Raw p draw away | 74.5% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.57 |
| Reference draw odds | 4.39 |
| Reference away odds | 5.13 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | -18.2% |
| Draw probability edge | +0.8% |
| Away probability edge | +17.4% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | -0.3633 |
| Raw ev home | -0.5818 |
| Raw edge prob draw | 0.0157 |
| Raw ev draw | 0.0382 |
| Raw edge prob away | 0.3477 |
| Raw ev away | 1.7076 |

</details>


---

## 2026-10-20 — Paris Saint Germain vs Barcelona

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **55.3%**. Expected goals are 3.22 for Paris Saint Germain and 1.52 for Barcelona (4.75 combined). The most likely exact score is 2-2 at 6.7%. Goal-market probabilities: at least one goal: 99.2%; Over 2.5 goals: 83.6%; Under 3.5 goals: 32.2%; Double Chance 1X: 73.2%; Double Chance X2: 44.7%; Double Chance 12 (either team wins): 82.1%; Under 4.5 goals: 51.0%; BTTS Yes (both teams score): 76.8%; BTTS No (at least one team does not score): 23.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 55.3% | 1.81 |
| Draw | 17.9% | 5.60 |
| Barcelona win | 26.8% | 3.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 3.22 |
| Barcelona expected goals | 1.52 |
| Expected total goals | 4.75 |
| Over 0.5 | 99.2% |
| Under 0.5 | 0.8% |
| Over 1.5 | 94.1% |
| Under 1.5 | 5.9% |
| Over 2.5 | 83.6% |
| Under 2.5 | 16.4% |
| Over 3.5 | 67.8% |
| Under 3.5 | 32.2% |
| Over 4.5 | 49.0% |
| Under 4.5 | 51.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.74% |
| 2 | 1-2 | 5.76% |
| 3 | 3-1 | 5.75% |
| 4 | 2-1 | 5.35% |
| 5 | 1-1 | 5.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 55.3% | 39.6% | 2.49 | +37.7% |
| Draw | 17.9% | 21.9% | 4.57 | -18.3% |
| Barcelona win | 26.8% | 38.6% | 2.54 | -31.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | 46b790335fa98338b7e1ed0b614078fb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:04Z |
| Market best draw last update utc | 2026-10-16T22:16:04Z |
| Market best away last update utc | 2026-10-16T22:16:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris Saint-Germain FC |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 76.8% |
| P btts no | 23.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 118.41 |
| Fair Over 1.5 odds | 1.06 |
| Fair Under 1.5 odds | 16.90 |
| Fair Over 2.5 odds | 1.20 |
| Fair Under 2.5 odds | 6.08 |
| Fair Over 3.5 odds | 1.48 |
| Fair Under 3.5 odds | 3.10 |
| Fair Over 4.5 odds | 2.04 |
| Fair Under 4.5 odds | 1.96 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 94.8% |
| Raw p under 3 5 | 30.2% |
| Raw p btts yes | 74.9% |
| P home draw | 73.2% |
| P draw away | 44.7% |
| P home away | 82.1% |
| Raw p home draw | 84.9% |
| Raw p draw away | 29.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.41 |
| Reference draw odds | 4.23 |
| Reference away odds | 2.47 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.00 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | +15.7% |
| Draw probability edge | -4.0% |
| Away probability edge | -11.7% |
| Over 2.5 probability edge | +4.0% |
| Under 2.5 probability edge | -4.0% |
| Raw edge prob home | 0.3145 |
| Raw ev home | 0.7685 |
| Raw edge prob draw | -0.0801 |
| Raw ev draw | -0.3664 |
| Raw edge prob away | -0.2344 |
| Raw ev away | -0.6161 |

</details>


---

## 2026-10-20 — Porto vs PSV Eindhoven

The model's most likely 1X2 outcome is **Porto win** at **58.2%**. Expected goals are 2.11 for Porto and 1.17 for PSV Eindhoven (3.28 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 63.2%; Under 3.5 goals: 58.6%; Double Chance 1X: 79.2%; Double Chance X2: 41.8%; Double Chance 12 (either team wins): 78.9%; Under 4.5 goals: 76.9%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 58.2% | 1.72 |
| Draw | 21.1% | 4.75 |
| PSV Eindhoven win | 20.8% | 4.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Porto expected goals | 2.11 |
| PSV Eindhoven expected goals | 1.17 |
| Expected total goals | 3.28 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 63.2% |
| Under 2.5 | 36.8% |
| Over 3.5 | 41.4% |
| Under 3.5 | 58.6% |
| Over 4.5 | 23.1% |
| Under 4.5 | 76.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.59% |
| 2 | 1-1 | 9.44% |
| 3 | 1-0 | 8.24% |
| 4 | 2-0 | 8.22% |
| 5 | 3-1 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 58.2% | 56.8% | 1.76 | +2.4% |
| Draw | 21.1% | 22.4% | 4.41 | -7.1% |
| PSV Eindhoven win | 20.8% | 20.7% | 4.51 | -6.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | 0686ce05e8489734fd66e5ee97fbbfa2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:04Z |
| Market best draw last update utc | 2026-10-16T22:16:04Z |
| Market best away last update utc | 2026-10-16T22:16:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Porto |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.27 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.02 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.71 |
| Fair Over 3.5 odds | 2.42 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.33 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 59.5% |
| Unadjusted draw probability | 19.7% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 60.1% |
| P home draw | 79.2% |
| P draw away | 41.8% |
| P home away | 78.9% |
| Raw p home draw | 79.2% |
| Raw p draw away | 40.5% |
| Raw p home away | 80.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.70 |
| Reference draw odds | 4.07 |
| Reference away odds | 4.39 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | +1.3% |
| Draw probability edge | -1.4% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | 0.0263 |
| Raw ev home | 0.0468 |
| Raw edge prob draw | -0.0277 |
| Raw ev draw | -0.1321 |
| Raw edge prob away | 0.0013 |
| Raw ev away | -0.0600 |

</details>


---

## 2026-10-20 — Sabah FK vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **74.7%**. Expected goals are 0.75 for Sabah FK and 2.47 for Borussia Dortmund (3.23 combined). The most likely exact score is 0-2 at 12.0%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 62.4%; Under 3.5 goals: 59.7%; Double Chance 1X: 25.3%; Double Chance X2: 90.0%; Double Chance 12 (either team wins): 84.7%; Under 4.5 goals: 77.7%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 10.0% | 9.98 |
| Draw | 15.3% | 6.55 |
| Borussia Dortmund win | 74.7% | 1.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.75 |
| Borussia Dortmund expected goals | 2.47 |
| Expected total goals | 3.23 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 62.4% |
| Under 2.5 | 37.6% |
| Over 3.5 | 40.3% |
| Under 3.5 | 59.7% |
| Over 4.5 | 22.3% |
| Under 4.5 | 77.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.01% |
| 2 | 0-1 | 10.07% |
| 3 | 0-3 | 9.91% |
| 4 | 1-2 | 9.06% |
| 5 | 1-3 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 10.0% | 10.3% | 9.40 | -5.8% |
| Draw | 15.3% | 15.7% | 6.11 | -6.7% |
| Borussia Dortmund win | 74.7% | 74.0% | 1.34 | +0.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T16:45:00+00:00 |
| Fixture id | 464c74a35c648d4910cc16976ce2f7cd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:04Z |
| Market best draw last update utc | 2026-10-16T22:16:04Z |
| Market best away last update utc | 2026-10-16T22:16:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.13 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.81 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.66 |
| Fair Over 3.5 odds | 2.48 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.48 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 9.7% |
| Unadjusted draw probability | 14.9% |
| Unadjusted away-win probability | 75.4% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 59.6% |
| Raw p btts yes | 48.1% |
| P home draw | 25.3% |
| P draw away | 90.0% |
| P home away | 84.7% |
| Raw p home draw | 24.6% |
| Raw p draw away | 90.3% |
| Raw p home away | 85.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 8.57 |
| Reference draw odds | 5.78 |
| Reference away odds | 1.33 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | -0.3% |
| Draw probability edge | -0.4% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.0063 |
| Raw ev home | -0.0877 |
| Raw edge prob draw | -0.0081 |
| Raw ev draw | -0.0917 |
| Raw edge prob away | 0.0144 |
| Raw ev away | 0.0107 |

</details>


---

## 2026-10-20 — VfB Stuttgart vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **48.2%**. Expected goals are 1.41 for VfB Stuttgart and 2.10 for Atlético Madrid (3.51 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 67.3%; Under 3.5 goals: 53.8%; Double Chance 1X: 51.8%; Double Chance X2: 70.6%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 73.0%; BTTS Yes (both teams score): 66.7%; BTTS No (at least one team does not score): 33.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 29.4% | 3.40 |
| Draw | 22.4% | 4.46 |
| Atlético Madrid win | 48.2% | 2.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 1.41 |
| Atlético Madrid expected goals | 2.10 |
| Expected total goals | 3.51 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 85.9% |
| Under 1.5 | 14.1% |
| Over 2.5 | 67.3% |
| Under 2.5 | 32.7% |
| Over 3.5 | 46.2% |
| Under 3.5 | 53.8% |
| Over 4.5 | 27.0% |
| Under 4.5 | 73.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.38% |
| 2 | 1-2 | 8.34% |
| 3 | 2-2 | 7.32% |
| 4 | 2-1 | 7.03% |
| 5 | 0-1 | 6.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 29.4% | 32.6% | 3.01 | -11.6% |
| Draw | 22.4% | 24.7% | 3.96 | -11.1% |
| Atlético Madrid win | 48.2% | 42.7% | 2.32 | +11.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | 56989e10c299aba1a0fce210bb214775 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | VfB Stuttgart |
| Matched away-team name | Club Atlético de Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 66.7% |
| P btts no | 33.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.24 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.09 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.06 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.70 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 26.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 53.7% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 65.9% |
| P home draw | 51.8% |
| P draw away | 70.6% |
| P home away | 77.6% |
| Raw p home draw | 46.3% |
| Raw p draw away | 73.8% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.88 |
| Reference draw odds | 3.73 |
| Reference away odds | 2.23 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | -3.2% |
| Draw probability edge | -2.3% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | +3.5% |
| Under 2.5 probability edge | -3.5% |
| Raw edge prob home | -0.0636 |
| Raw ev home | -0.2115 |
| Raw edge prob draw | -0.0460 |
| Raw ev draw | -0.2022 |
| Raw edge prob away | 0.1095 |
| Raw ev away | 0.2449 |

</details>


---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **81.9%**. Expected goals are 4.01 for Aston Villa and 1.16 for Viking FK (5.17 combined). The most likely exact score is 4-1 at 6.8%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.9%; Under 3.5 goals: 24.8%; Double Chance 1X: 93.2%; Double Chance X2: 18.1%; Double Chance 12 (either team wins): 88.6%; Under 4.5 goals: 42.4%; BTTS Yes (both teams score): 68.4%; BTTS No (at least one team does not score): 31.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 81.9% | 1.22 |
| Draw | 11.4% | 8.79 |
| Viking FK win | 6.8% | 14.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 4.01 |
| Viking FK expected goals | 1.16 |
| Expected total goals | 5.17 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 87.9% |
| Under 2.5 | 12.1% |
| Over 3.5 | 75.2% |
| Under 3.5 | 24.8% |
| Over 4.5 | 57.6% |
| Under 4.5 | 42.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-1 | 6.79% |
| 2 | 3-1 | 6.78% |
| 3 | 4-0 | 5.83% |
| 4 | 3-0 | 5.82% |
| 5 | 5-1 | 5.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 81.9% | 78.1% | 1.31 | +7.2% |
| Draw | 11.4% | 14.5% | 5.85 | -33.4% |
| Viking FK win | 6.8% | 7.4% | 12.50 | -15.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | d3b3e714b6af9e5430e3030ed639e6dd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 23 |
| Score grid omitted mass | 0 |
| P btts yes | 68.4% |
| P btts no | 31.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 165.46 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.44 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.29 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.03 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 85.6% |
| Unadjusted draw probability | 8.2% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.2% |
| Raw p btts yes | 67.4% |
| P home draw | 93.2% |
| P draw away | 18.1% |
| P home away | 88.6% |
| Raw p home draw | 93.8% |
| Raw p draw away | 14.4% |
| Raw p home away | 91.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.26 |
| Reference draw odds | 6.05 |
| Reference away odds | 11.40 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | +3.8% |
| Draw probability edge | -3.2% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | +13.7% |
| Under 2.5 probability edge | -13.7% |
| Raw edge prob home | 0.0755 |
| Raw ev home | 0.1217 |
| Raw edge prob draw | -0.0633 |
| Raw ev draw | -0.5194 |
| Raw edge prob away | -0.0122 |
| Raw ev away | -0.2303 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Bayern Munich win** at **37.2%**. Expected goals are 1.02 for Bayern Munich and 1.31 for Arsenal (2.33 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 41.1%; Under 3.5 goals: 79.6%; Double Chance 1X: 63.2%; Double Chance X2: 62.8%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 45.9%; BTTS No (at least one team does not score): 54.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 37.2% | 2.69 |
| Draw | 26.0% | 3.85 |
| Arsenal win | 36.8% | 2.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 1.02 |
| Arsenal expected goals | 1.31 |
| Expected total goals | 2.33 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 41.1% |
| Under 2.5 | 58.9% |
| Over 3.5 | 20.4% |
| Under 3.5 | 79.6% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.28% |
| 2 | 1-1 | 12.12% |
| 3 | 0-1 | 11.25% |
| 4 | 0-0 | 8.93% |
| 5 | 2-1 | 8.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 37.2% | 44.8% | 2.23 | -17.1% |
| Draw | 26.0% | 25.5% | 3.92 | +1.9% |
| Arsenal win | 36.8% | 29.7% | 3.21 | +18.2% |
| Over 2.5 | 41.1% | 58.5% | 1.68 | -31.0% |
| Under 2.5 | 58.9% | 41.5% | 2.38 | +40.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 2ebbccdeea2dab59717d5c3d802c3fed |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Bayern München |
| Matched away-team name | Arsenal FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 45.9% |
| P btts no | 54.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.20 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.90 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.57 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 29.6% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 43.9% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 79.4% |
| Raw p btts yes | 46.0% |
| P home draw | 63.2% |
| P draw away | 62.8% |
| P home away | 74.0% |
| Raw p home draw | 56.1% |
| Raw p draw away | 70.4% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.18 |
| Reference draw odds | 3.76 |
| Reference away odds | 3.24 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:23Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:23Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | -7.6% |
| Draw probability edge | +0.5% |
| Away probability edge | +7.1% |
| Over 2.5 probability edge | -17.5% |
| Under 2.5 probability edge | +17.5% |
| Raw edge prob home | -0.1514 |
| Raw ev home | -0.3397 |
| Raw edge prob draw | 0.0098 |
| Raw ev draw | 0.0381 |
| Raw edge prob away | 0.1417 |
| Raw ev away | 0.4094 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **59.7%**. Expected goals are 3.05 for Club Brugge and 1.27 for RC Lens (4.32 combined). The most likely exact score is 2-2 at 6.9%. Goal-market probabilities: at least one goal: 98.5%; Over 2.5 goals: 78.3%; Under 3.5 goals: 39.3%; Double Chance 1X: 78.6%; Double Chance X2: 40.3%; Double Chance 12 (either team wins): 81.1%; Under 4.5 goals: 59.1%; BTTS Yes (both teams score): 70.6%; BTTS No (at least one team does not score): 29.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 59.7% | 1.67 |
| Draw | 18.9% | 5.29 |
| RC Lens win | 21.4% | 4.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Club Brugge expected goals | 3.05 |
| RC Lens expected goals | 1.27 |
| Expected total goals | 4.32 |
| Over 0.5 | 98.5% |
| Under 0.5 | 1.5% |
| Over 1.5 | 91.8% |
| Under 1.5 | 8.2% |
| Over 2.5 | 78.3% |
| Under 2.5 | 21.7% |
| Over 3.5 | 60.7% |
| Under 3.5 | 39.3% |
| Over 4.5 | 40.9% |
| Under 4.5 | 59.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.89% |
| 2 | 1-1 | 6.74% |
| 3 | 3-1 | 6.50% |
| 4 | 2-1 | 6.40% |
| 5 | 1-2 | 5.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 59.7% | 46.1% | 2.16 | +29.0% |
| Draw | 18.9% | 24.1% | 3.88 | -26.6% |
| RC Lens win | 21.4% | 29.7% | 3.39 | -27.5% |
| Over 2.5 | 78.3% | 59.5% | 1.67 | +30.8% |
| Under 2.5 | 21.7% | 40.5% | 2.40 | -47.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | d306a78e402e5f505e8644fdf3f75dcd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Club Brugge KV |
| Matched away-team name | Racing Club de Lens |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 86/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 70.6% |
| P btts no | 29.4% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 67.90 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.24 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.61 |
| Fair Over 3.5 odds | 1.65 |
| Fair Under 3.5 odds | 2.54 |
| Fair Over 4.5 odds | 2.45 |
| Fair Under 4.5 odds | 1.69 |
| Unadjusted home-win probability | 73.3% |
| Unadjusted draw probability | 13.7% |
| Unadjusted away-win probability | 13.0% |
| Raw p over 1 5 | 92.7% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 68.3% |
| P home draw | 78.6% |
| P draw away | 40.3% |
| P home away | 81.1% |
| Raw p home draw | 87.0% |
| Raw p draw away | 26.7% |
| Raw p home away | 86.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.07 |
| Reference draw odds | 3.81 |
| Reference away odds | 3.13 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.29 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:23Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:23Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | +13.6% |
| Draw probability edge | -5.2% |
| Away probability edge | -8.4% |
| Over 2.5 probability edge | +18.8% |
| Under 2.5 probability edge | -18.8% |
| Raw edge prob home | 0.2713 |
| Raw ev home | 0.5826 |
| Raw edge prob draw | -0.1041 |
| Raw ev draw | -0.4678 |
| Raw edge prob away | -0.1672 |
| Raw ev away | -0.5589 |

</details>


---

## 2026-10-21 — Como vs Manchester United

The model's most likely 1X2 outcome is **Como win** at **50.9%**. Expected goals are 2.99 for Como and 1.94 for Manchester United (4.93 combined). The most likely exact score is 2-2 at 7.8%. Goal-market probabilities: at least one goal: 99.3%; Over 2.5 goals: 86.0%; Under 3.5 goals: 27.9%; Double Chance 1X: 71.9%; Double Chance X2: 49.1%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 46.6%; BTTS Yes (both teams score): 82.3%; BTTS No (at least one team does not score): 17.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 50.9% | 1.96 |
| Draw | 20.9% | 4.78 |
| Manchester United win | 28.1% | 3.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.99 |
| Manchester United expected goals | 1.94 |
| Expected total goals | 4.93 |
| Over 0.5 | 99.3% |
| Under 0.5 | 0.7% |
| Over 1.5 | 95.4% |
| Under 1.5 | 4.6% |
| Over 2.5 | 86.0% |
| Under 2.5 | 14.0% |
| Over 3.5 | 72.1% |
| Under 3.5 | 27.9% |
| Over 4.5 | 53.4% |
| Under 4.5 | 46.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.80% |
| 2 | 2-1 | 5.34% |
| 3 | 3-1 | 5.33% |
| 4 | 3-2 | 5.17% |
| 5 | 1-1 | 5.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 50.9% | 42.2% | 2.38 | +21.2% |
| Draw | 20.9% | 25.6% | 3.85 | -19.4% |
| Manchester United win | 28.1% | 32.2% | 2.97 | -16.5% |
| Over 2.5 | 86.0% | 58.1% | 1.70 | +46.2% |
| Under 2.5 | 14.0% | 41.9% | 2.34 | -67.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T16:45:00+00:00 |
| Fixture id | 8af9379136075f45b290208b35a706c8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Como 1907 |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 82.3% |
| P btts no | 17.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 152.46 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 21.96 |
| Fair Over 2.5 odds | 1.16 |
| Fair Under 2.5 odds | 7.15 |
| Fair Over 3.5 odds | 1.39 |
| Fair Under 3.5 odds | 3.59 |
| Fair Over 4.5 odds | 1.87 |
| Fair Under 4.5 odds | 2.15 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 95.5% |
| Raw p under 3 5 | 27.4% |
| Raw p btts yes | 81.2% |
| P home draw | 71.9% |
| P draw away | 49.1% |
| P home away | 79.1% |
| Raw p home draw | 76.0% |
| Raw p draw away | 40.3% |
| Raw p home away | 83.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.28 |
| Reference draw odds | 3.68 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:23Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:23Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | +8.7% |
| Draw probability edge | -4.6% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | +27.9% |
| Under 2.5 probability edge | -27.9% |
| Raw edge prob home | 0.1747 |
| Raw ev home | 0.4201 |
| Raw edge prob draw | -0.0927 |
| Raw ev draw | -0.3726 |
| Raw edge prob away | -0.0819 |
| Raw ev away | -0.2862 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **71.9%**. Expected goals are 2.05 for Inter Milan and 0.92 for Shakhtar Donetsk (2.97 combined). The most likely exact score is 1-0 at 12.3%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 58.8%; Under 3.5 goals: 64.3%; Double Chance 1X: 88.0%; Double Chance X2: 28.1%; Double Chance 12 (either team wins): 83.9%; Under 4.5 goals: 81.1%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 71.9% | 1.39 |
| Draw | 16.1% | 6.22 |
| Shakhtar Donetsk win | 12.0% | 8.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.05 |
| Shakhtar Donetsk expected goals | 0.92 |
| Expected total goals | 2.97 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 35.7% |
| Under 3.5 | 64.3% |
| Over 4.5 | 18.9% |
| Under 4.5 | 81.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.33% |
| 2 | 2-0 | 12.09% |
| 3 | 2-1 | 11.14% |
| 4 | 3-0 | 8.27% |
| 5 | 3-1 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 71.9% | 79.8% | 1.24 | -10.8% |
| Draw | 16.1% | 12.7% | 7.50 | +20.6% |
| Shakhtar Donetsk win | 12.0% | 7.5% | 12.90 | +54.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | a889456204e8ef1b64294efbee8dc3e5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | FK Shakhtar Donetsk |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.13 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.02 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.80 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.28 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 64.0% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 16.5% |
| Raw p over 1 5 | 79.2% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 52.0% |
| P home draw | 88.0% |
| P draw away | 28.1% |
| P home away | 83.9% |
| Raw p home draw | 83.5% |
| Raw p draw away | 36.0% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.24 |
| Reference draw odds | 7.16 |
| Reference away odds | 11.85 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | -7.9% |
| Draw probability edge | +3.4% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | -15.4% |
| Under 2.5 probability edge | +15.4% |
| Raw edge prob home | -0.1581 |
| Raw ev home | -0.2064 |
| Raw edge prob draw | 0.0677 |
| Raw ev draw | 0.4604 |
| Raw edge prob away | 0.0904 |
| Raw ev away | 1.1317 |

</details>


---

## 2026-10-21 — Lille vs Galatasaray

The model's most likely 1X2 outcome is **Lille win** at **57.6%**. Expected goals are 2.57 for Lille and 1.04 for Galatasaray (3.61 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.1%; Under 3.5 goals: 53.5%; Double Chance 1X: 78.3%; Double Chance X2: 42.4%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 72.6%; BTTS Yes (both teams score): 61.4%; BTTS No (at least one team does not score): 38.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 57.6% | 1.74 |
| Draw | 20.7% | 4.83 |
| Galatasaray win | 21.7% | 4.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 2.57 |
| Galatasaray expected goals | 1.04 |
| Expected total goals | 3.61 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 85.8% |
| Under 1.5 | 14.2% |
| Over 2.5 | 67.1% |
| Under 2.5 | 32.9% |
| Over 3.5 | 46.5% |
| Under 3.5 | 53.5% |
| Over 4.5 | 27.4% |
| Under 4.5 | 72.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.04% |
| 2 | 2-1 | 7.56% |
| 3 | 2-0 | 7.29% |
| 4 | 3-1 | 6.48% |
| 5 | 2-2 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 57.6% | 44.4% | 2.24 | +29.0% |
| Draw | 20.7% | 25.7% | 3.84 | -20.5% |
| Galatasaray win | 21.7% | 29.9% | 3.25 | -29.4% |
| Over 2.5 | 67.1% | 57.3% | 1.72 | +15.5% |
| Under 2.5 | 32.9% | 42.7% | 2.30 | -24.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T16:45:00+00:00 |
| Fixture id | 015d619d774655965e17ba67a025634e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille OSC |
| Matched away-team name | Galatasaray SK |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 61.4% |
| P btts no | 38.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.29 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.05 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.04 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.66 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 70.8% |
| Unadjusted draw probability | 15.7% |
| Unadjusted away-win probability | 13.5% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 51.4% |
| Raw p btts yes | 59.2% |
| P home draw | 78.3% |
| P draw away | 42.4% |
| P home away | 79.3% |
| Raw p home draw | 86.5% |
| Raw p draw away | 29.2% |
| Raw p home away | 84.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.17 |
| Reference draw odds | 3.66 |
| Reference away odds | 3.16 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:23Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:23Z |
| Market best over 2 5 last update utc | 2026-10-16T22:16:05Z |
| Market best under 2 5 last update utc | 2026-10-16T22:16:05Z |
| Home probability edge | +13.2% |
| Draw probability edge | -5.0% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | +9.8% |
| Under 2.5 probability edge | -9.8% |
| Raw edge prob home | 0.2637 |
| Raw ev home | 0.5851 |
| Raw edge prob draw | -0.0993 |
| Raw ev draw | -0.3958 |
| Raw edge prob away | -0.1644 |
| Raw ev away | -0.5613 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **77.9%**. Expected goals are 5.75 for Real Betis and 1.65 for Feyenoord (7.40 combined). The most likely exact score is 5-1 at 4.5%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.7%; Under 3.5 goals: 7.7%; Double Chance 1X: 89.9%; Double Chance X2: 22.1%; Double Chance 12 (either team wins): 88.0%; Under 4.5 goals: 17.1%; BTTS Yes (both teams score): 82.8%; BTTS No (at least one team does not score): 17.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 77.9% | 1.28 |
| Draw | 12.0% | 8.30 |
| Feyenoord win | 10.1% | 9.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 5.75 |
| Feyenoord expected goals | 1.65 |
| Expected total goals | 7.40 |
| Over 0.5 | 99.9% |
| Under 0.5 | 0.1% |
| Over 1.5 | 99.2% |
| Under 1.5 | 0.8% |
| Over 2.5 | 96.7% |
| Under 2.5 | 3.3% |
| Over 3.5 | 92.3% |
| Under 3.5 | 7.7% |
| Over 4.5 | 82.9% |
| Under 4.5 | 17.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-1 | 4.50% |
| 2 | 6-1 | 4.31% |
| 3 | 4-1 | 3.91% |
| 4 | 3-3 | 3.72% |
| 5 | 5-2 | 3.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 77.9% | 64.1% | 1.56 | +21.5% |
| Draw | 12.0% | 19.4% | 4.93 | -40.6% |
| Feyenoord win | 10.1% | 16.4% | 5.80 | -41.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | f5905225efa837b0dc89b7dcdbb6c625 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 27 |
| Score grid omitted mass | 0 |
| P btts yes | 82.8% |
| P btts no | 17.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1205.18 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 132.48 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 30.72 |
| Fair Over 3.5 odds | 1.08 |
| Fair Under 3.5 odds | 12.95 |
| Fair Over 4.5 odds | 1.21 |
| Fair Under 4.5 odds | 5.85 |
| Unadjusted home-win probability | 91.6% |
| Unadjusted draw probability | 4.7% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.3% |
| Raw p btts yes | 80.4% |
| P home draw | 89.9% |
| P draw away | 22.1% |
| P home away | 88.0% |
| Raw p home draw | 96.2% |
| Raw p draw away | 8.4% |
| Raw p home away | 95.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.52 |
| Reference draw odds | 4.69 |
| Reference away odds | 5.49 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | +13.7% |
| Draw probability edge | -7.4% |
| Away probability edge | -6.3% |
| Over 2.5 probability edge | +27.8% |
| Under 2.5 probability edge | -27.8% |
| Raw edge prob home | 0.2742 |
| Raw ev home | 0.4284 |
| Raw edge prob draw | -0.1474 |
| Raw ev draw | -0.7694 |
| Raw edge prob away | -0.1267 |
| Raw ev away | -0.7819 |

</details>


---

## 2026-10-21 — Real Madrid vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid win** at **76.1%**. Expected goals are 2.80 for Real Madrid and 0.88 for RB Leipzig (3.68 combined). The most likely exact score is 2-0 at 9.7%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.1%; Double Chance 1X: 90.2%; Double Chance X2: 23.9%; Double Chance 12 (either team wins): 86.0%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 76.1% | 1.31 |
| Draw | 14.0% | 7.13 |
| RB Leipzig win | 9.8% | 10.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.80 |
| RB Leipzig expected goals | 0.88 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 87.7% |
| Under 1.5 | 12.3% |
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 49.9% |
| Under 3.5 | 50.1% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.73% |
| 2 | 3-0 | 9.09% |
| 3 | 2-1 | 8.54% |
| 4 | 3-1 | 7.97% |
| 5 | 1-0 | 7.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 76.1% | 74.7% | 1.31 | -0.3% |
| Draw | 14.0% | 14.9% | 6.80 | -4.6% |
| RB Leipzig win | 9.8% | 10.3% | 9.60 | -5.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 30f27b8e9719e9ae71c25b4c8aa265f7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.26 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.41 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.27 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 77.6% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 9.3% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 49.9% |
| Raw p btts yes | 54.5% |
| P home draw | 90.2% |
| P draw away | 23.9% |
| P home away | 86.0% |
| Raw p home draw | 90.7% |
| Raw p draw away | 22.4% |
| Raw p home away | 86.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.33 |
| Reference draw odds | 6.44 |
| Reference away odds | 9.22 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | +1.4% |
| Draw probability edge | -0.9% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | 0.0282 |
| Raw ev home | 0.0160 |
| Raw edge prob draw | -0.0178 |
| Raw ev draw | -0.1063 |
| Raw edge prob away | -0.0104 |
| Raw ev away | -0.1069 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **85.9%**. Expected goals are 6.10 for Sporting Lisbon and 1.32 for LASK (7.42 combined). The most likely exact score is 6-1 at 5.1%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.7%; Under 3.5 goals: 7.6%; Double Chance 1X: 94.4%; Double Chance X2: 14.1%; Double Chance 12 (either team wins): 91.5%; Under 4.5 goals: 16.7%; BTTS Yes (both teams score): 75.2%; BTTS No (at least one team does not score): 24.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 85.9% | 1.16 |
| Draw | 8.5% | 11.74 |
| LASK win | 5.6% | 17.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 6.10 |
| LASK expected goals | 1.32 |
| Expected total goals | 7.42 |
| Over 0.5 | 99.9% |
| Under 0.5 | 0.1% |
| Over 1.5 | 99.2% |
| Under 1.5 | 0.8% |
| Over 2.5 | 96.7% |
| Under 2.5 | 3.3% |
| Over 3.5 | 92.4% |
| Under 3.5 | 7.6% |
| Over 4.5 | 83.3% |
| Under 4.5 | 16.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 6-1 | 5.11% |
| 2 | 5-1 | 5.02% |
| 3 | 7-1 | 4.45% |
| 4 | 4-1 | 4.12% |
| 5 | 6-0 | 3.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 85.9% | 76.5% | 1.27 | +9.0% |
| Draw | 8.5% | 14.1% | 7.13 | -39.3% |
| LASK win | 5.6% | 9.4% | 11.00 | -38.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 8fdcaee14b3e8966e09d468a0b17ce18 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-16T22:16:05Z |
| Market best draw last update utc | 2026-10-16T22:16:05Z |
| Market best away last update utc | 2026-10-16T22:16:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 28 |
| Score grid omitted mass | 0 |
| P btts yes | 75.2% |
| P btts no | 24.8% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 958.89 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 130.79 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 30.70 |
| Fair Over 3.5 odds | 1.08 |
| Fair Under 3.5 odds | 13.07 |
| Fair Over 4.5 odds | 1.20 |
| Fair Under 4.5 odds | 5.98 |
| Unadjusted home-win probability | 95.2% |
| Unadjusted draw probability | 2.9% |
| Unadjusted away-win probability | 1.9% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.2% |
| Raw p btts yes | 73.0% |
| P home draw | 94.4% |
| P draw away | 14.1% |
| P home away | 91.5% |
| Raw p home draw | 98.1% |
| Raw p draw away | 4.8% |
| Raw p home away | 97.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.29 |
| Reference draw odds | 6.45 |
| Reference away odds | 9.50 |
| Market reference 1x2 last update utc | 2026-10-16T22:16:23Z |
| Market reference home last update utc | 2026-10-16T22:16:23Z |
| Market reference draw last update utc | 2026-10-16T22:16:23Z |
| Market reference away last update utc | 2026-10-16T22:16:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-16T22:16:22Z |
| Market reference under 2 5 last update utc | 2026-10-16T22:16:22Z |
| Home probability edge | +9.3% |
| Draw probability edge | -5.6% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | +25.1% |
| Under 2.5 probability edge | -25.1% |
| Raw edge prob home | 0.1866 |
| Raw ev home | 0.2088 |
| Raw edge prob draw | -0.1116 |
| Raw ev draw | -0.7909 |
| Raw edge prob away | -0.0750 |
| Raw ev away | -0.7928 |

</details>


---
