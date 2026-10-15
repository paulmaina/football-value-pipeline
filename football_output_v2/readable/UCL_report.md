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
| Training data health | {'completed_matches': 36, 'latest_completed_utc': '2026-10-14T19:00:00+00:00', 'latest_completed_date': '2026-10-14', 'next_fixture_utc': '2026-10-20T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-15T09:51:31.659725+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'f5f38255aec6d88e6c074d41d73adc99ffbb9a98768a2ad902be176e17dbe29f', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0005588772222222222, 'training_end': '2026-10-14', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 25.00 |
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

The model's most likely 1X2 outcome is **AS Roma win** at **84.7%**. Expected goals are 3.76 for AS Roma and 1.32 for ŠK Slovan Bratislava (5.08 combined). The most likely exact score is 3-1 at 7.6%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 88.6%; Under 3.5 goals: 24.8%; Double Chance 1X: 93.9%; Double Chance X2: 15.3%; Double Chance 12 (either team wins): 90.8%; Under 4.5 goals: 42.1%; BTTS Yes (both teams score): 70.7%; BTTS No (at least one team does not score): 29.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 84.7% | 1.18 |
| Draw | 9.2% | 10.88 |
| ŠK Slovan Bratislava win | 6.1% | 16.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 3.76 |
| ŠK Slovan Bratislava expected goals | 1.32 |
| Expected total goals | 5.08 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 96.3% |
| Under 1.5 | 3.7% |
| Over 2.5 | 88.6% |
| Under 2.5 | 11.4% |
| Over 3.5 | 75.2% |
| Under 3.5 | 24.8% |
| Over 4.5 | 57.9% |
| Under 4.5 | 42.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.62% |
| 2 | 4-1 | 7.16% |
| 3 | 2-1 | 6.08% |
| 4 | 3-0 | 5.79% |
| 5 | 4-0 | 5.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 84.7% | 88.3% | 1.13 | -4.3% |
| Draw | 9.2% | 8.2% | 11.10 | +2.1% |
| ŠK Slovan Bratislava win | 6.1% | 3.4% | 25.00 | +52.3% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.7% |
| P btts no | 29.3% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 234.13 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.83 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.78 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.02 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.38 |
| Unadjusted home-win probability | 81.1% |
| Unadjusted draw probability | 10.1% |
| Unadjusted away-win probability | 8.8% |
| Raw p over 1 5 | 96.0% |
| Raw p under 3 5 | 25.5% |
| Raw p btts yes | 71.3% |
| P home draw | 93.9% |
| P draw away | 15.3% |
| P home away | 90.8% |
| Raw p home draw | 91.2% |
| Raw p draw away | 18.9% |
| Raw p home away | 89.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.12 |
| Reference draw odds | 9.80 |
| Reference away odds | 22.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.65 |
| Home probability edge | -3.6% |
| Draw probability edge | +0.9% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | +12.9% |
| Under 2.5 probability edge | -12.9% |
| Raw edge prob home | -0.0726 |
| Raw ev home | -0.0838 |
| Raw edge prob draw | 0.0190 |
| Raw ev draw | 0.1258 |
| Raw edge prob away | 0.0537 |
| Raw ev away | 1.1938 |

</details>


---

## 2026-10-20 — Fenerbahce vs Slavia Praha

The model's most likely 1X2 outcome is **Fenerbahce win** at **43.2%**. Expected goals are 0.78 for Fenerbahce and 1.07 for Slavia Praha (1.84 combined). The most likely exact score is 1-0 at 20.9%. Goal-market probabilities: at least one goal: 87.0%; Over 2.5 goals: 28.7%; Under 3.5 goals: 88.8%; Double Chance 1X: 69.4%; Double Chance X2: 56.8%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 33.9%; BTTS No (at least one team does not score): 66.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 43.2% | 2.31 |
| Draw | 26.2% | 3.82 |
| Slavia Praha win | 30.6% | 3.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 0.78 |
| Slavia Praha expected goals | 1.07 |
| Expected total goals | 1.84 |
| Over 0.5 | 87.0% |
| Under 0.5 | 13.0% |
| Over 1.5 | 53.5% |
| Under 1.5 | 46.5% |
| Over 2.5 | 28.7% |
| Under 2.5 | 71.3% |
| Over 3.5 | 11.2% |
| Under 3.5 | 88.8% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.85% |
| 2 | 0-0 | 13.00% |
| 3 | 0-1 | 12.62% |
| 4 | 1-1 | 10.65% |
| 5 | 2-1 | 8.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 43.2% | 59.6% | 1.68 | -27.4% |
| Draw | 26.2% | 21.8% | 4.42 | +15.8% |
| Slavia Praha win | 30.6% | 18.6% | 5.13 | +56.9% |
| Over 2.5 | 28.7% | 58.5% | 1.70 | -51.2% |
| Under 2.5 | 71.3% | 41.5% | 2.34 | +66.8% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| P btts yes | 33.9% |
| P btts no | 66.1% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.69 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.48 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.91 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.98 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 42.6% |
| Raw p over 1 5 | 54.3% |
| Raw p under 3 5 | 88.4% |
| Raw p btts yes | 34.7% |
| P home draw | 69.4% |
| P draw away | 56.8% |
| P home away | 73.8% |
| Raw p home draw | 57.4% |
| Raw p draw away | 73.2% |
| Raw p home away | 69.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.64 |
| Reference draw odds | 4.30 |
| Reference away odds | 5.00 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.27 |
| Home probability edge | -16.4% |
| Draw probability edge | +4.4% |
| Away probability edge | +12.0% |
| Over 2.5 probability edge | -29.7% |
| Under 2.5 probability edge | +29.7% |
| Raw edge prob home | -0.3281 |
| Raw ev home | -0.5495 |
| Raw edge prob draw | 0.0884 |
| Raw ev draw | 0.3532 |
| Raw edge prob away | 0.2397 |
| Raw ev away | 1.1837 |

</details>


---

## 2026-10-20 — Liverpool vs Villarreal

The model's most likely 1X2 outcome is **Liverpool win** at **76.9%**. Expected goals are 3.36 for Liverpool and 0.51 for Villarreal (3.86 combined). The most likely exact score is 3-0 at 11.4%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 68.7%; Under 3.5 goals: 50.8%; Double Chance 1X: 90.6%; Double Chance X2: 23.1%; Double Chance 12 (either team wins): 86.3%; Under 4.5 goals: 69.4%; BTTS Yes (both teams score): 41.4%; BTTS No (at least one team does not score): 58.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 76.9% | 1.30 |
| Draw | 13.7% | 7.32 |
| Villarreal win | 9.4% | 10.64 |

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
| Over 3.5 | 49.2% |
| Under 3.5 | 50.8% |
| Over 4.5 | 30.6% |
| Under 4.5 | 69.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 11.36% |
| 2 | 2-0 | 10.15% |
| 3 | 4-0 | 9.52% |
| 4 | 1-1 | 6.48% |
| 5 | 5-0 | 6.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 76.9% | 64.0% | 1.57 | +20.8% |
| Draw | 13.7% | 20.2% | 4.72 | -35.5% |
| Villarreal win | 9.4% | 15.8% | 5.96 | -44.0% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool FC |
| Matched away-team name | Villarreal CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.4% |
| P btts no | 58.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.16 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.24 |
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
| Raw p under 3 5 | 46.2% |
| Raw p btts yes | 38.1% |
| P home draw | 90.6% |
| P draw away | 23.1% |
| P home away | 86.3% |
| Raw p home draw | 97.0% |
| Raw p draw away | 10.1% |
| Raw p home away | 92.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.53 |
| Reference draw odds | 4.60 |
| Reference away odds | 5.80 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | +12.9% |
| Draw probability edge | -6.5% |
| Away probability edge | -6.4% |
| Over 2.5 probability edge | +6.2% |
| Under 2.5 probability edge | -6.2% |
| Raw edge prob home | 0.2586 |
| Raw ev home | 0.4109 |
| Raw edge prob draw | -0.1302 |
| Raw ev draw | -0.6622 |
| Raw edge prob away | -0.1284 |
| Raw ev away | -0.8226 |

</details>


---

## 2026-10-20 — Manchester City vs AEK Athens

The model's most likely 1X2 outcome is **Manchester City win** at **79.8%**. Expected goals are 2.34 for Manchester City and 1.07 for AEK Athens (3.40 combined). The most likely exact score is 2-1 at 11.7%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 69.0%; Under 3.5 goals: 54.0%; Double Chance 1X: 91.0%; Double Chance X2: 20.2%; Double Chance 12 (either team wins): 88.7%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 56.4%; BTTS No (at least one team does not score): 43.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 79.8% | 1.25 |
| Draw | 11.3% | 8.89 |
| AEK Athens win | 9.0% | 11.16 |

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
| 3 | 1-0 | 9.90% |
| 4 | 3-1 | 9.10% |
| 5 | 3-0 | 8.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 79.8% | 93.5% | 1.07 | -14.6% |
| Draw | 11.3% | 4.9% | 17.00 | +91.3% |
| AEK Athens win | 9.0% | 1.7% | 42.00 | +276.3% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Manchester City FC |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 67/100 |
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 53.70 |
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
| P home draw | 91.0% |
| P draw away | 20.2% |
| P home away | 88.7% |
| Raw p home draw | 83.7% |
| Raw p draw away | 33.9% |
| Raw p home away | 82.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.06 |
| Reference draw odds | 13.50 |
| Reference away odds | 34.00 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.80 |
| Home probability edge | -13.7% |
| Draw probability edge | +6.4% |
| Away probability edge | +7.3% |
| Over 2.5 probability edge | -8.3% |
| Under 2.5 probability edge | +8.3% |
| Raw edge prob home | -0.2734 |
| Raw ev home | -0.2925 |
| Raw edge prob draw | 0.1276 |
| Raw ev draw | 1.9971 |
| Raw edge prob away | 0.1458 |
| Raw ev away | 5.8255 |

</details>


---

## 2026-10-20 — Napoli vs Bodø/Glimt

The model's most likely 1X2 outcome is **Napoli win** at **43.3%**. Expected goals are 1.17 for Napoli and 1.78 for Bodø/Glimt (2.94 combined). The most likely exact score is 1-0 at 11.4%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 55.8%; Under 3.5 goals: 67.3%; Double Chance 1X: 64.7%; Double Chance X2: 56.7%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 56.9%; BTTS No (at least one team does not score): 43.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 43.3% | 2.31 |
| Draw | 21.4% | 4.68 |
| Bodø/Glimt win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.17 |
| Bodø/Glimt expected goals | 1.78 |
| Expected total goals | 2.94 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 55.8% |
| Under 2.5 | 44.2% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.36% |
| 2 | 2-1 | 10.81% |
| 3 | 1-1 | 9.96% |
| 4 | 0-1 | 6.69% |
| 5 | 1-2 | 6.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 43.3% | 61.1% | 1.64 | -28.9% |
| Draw | 21.4% | 20.5% | 4.67 | -0.3% |
| Bodø/Glimt win | 35.3% | 18.4% | 5.18 | +82.9% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | SSC Napoli |
| Matched away-team name | FK Bodø/Glimt |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 56.9% |
| P btts no | 43.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.06 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.43 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.88 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 25.5% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 52.3% |
| Raw p over 1 5 | 78.7% |
| Raw p under 3 5 | 66.0% |
| Raw p btts yes | 56.7% |
| P home draw | 64.7% |
| P draw away | 56.7% |
| P home away | 78.6% |
| Raw p home draw | 47.7% |
| Raw p draw away | 74.5% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.60 |
| Reference draw odds | 4.55 |
| Reference away odds | 5.05 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.65 |
| Home probability edge | -17.8% |
| Draw probability edge | +0.9% |
| Away probability edge | +17.0% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | -0.3565 |
| Raw ev home | -0.5818 |
| Raw edge prob draw | 0.0175 |
| Raw ev draw | 0.0382 |
| Raw edge prob away | 0.3390 |
| Raw ev away | 1.7075 |

</details>


---

## 2026-10-20 — Paris Saint Germain vs Barcelona

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **55.5%**. Expected goals are 3.22 for Paris Saint Germain and 1.52 for Barcelona (4.75 combined). The most likely exact score is 2-2 at 6.7%. Goal-market probabilities: at least one goal: 99.2%; Over 2.5 goals: 83.6%; Under 3.5 goals: 32.2%; Double Chance 1X: 73.3%; Double Chance X2: 44.5%; Double Chance 12 (either team wins): 82.2%; Under 4.5 goals: 51.0%; BTTS Yes (both teams score): 76.7%; BTTS No (at least one team does not score): 23.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 55.5% | 1.80 |
| Draw | 17.8% | 5.61 |
| Barcelona win | 26.7% | 3.75 |

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
| 1 | 2-2 | 6.72% |
| 2 | 3-1 | 5.77% |
| 3 | 1-2 | 5.73% |
| 4 | 2-1 | 5.37% |
| 5 | 1-1 | 5.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 55.5% | 40.0% | 2.48 | +37.7% |
| Draw | 17.8% | 21.8% | 4.45 | -20.7% |
| Barcelona win | 26.7% | 38.2% | 2.59 | -30.9% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris Saint-Germain FC |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 76.7% |
| P btts no | 23.3% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 118.77 |
| Fair Over 1.5 odds | 1.06 |
| Fair Under 1.5 odds | 16.93 |
| Fair Over 2.5 odds | 1.20 |
| Fair Under 2.5 odds | 6.09 |
| Fair Over 3.5 odds | 1.48 |
| Fair Under 3.5 odds | 3.10 |
| Fair Over 4.5 odds | 2.04 |
| Fair Under 4.5 odds | 1.96 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 94.8% |
| Raw p under 3 5 | 30.3% |
| Raw p btts yes | 74.9% |
| P home draw | 73.3% |
| P draw away | 44.5% |
| P home away | 82.2% |
| Raw p home draw | 84.9% |
| Raw p draw away | 29.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.41 |
| Reference draw odds | 4.33 |
| Reference away odds | 2.52 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.00 |
| Home probability edge | +15.5% |
| Draw probability edge | -3.9% |
| Away probability edge | -11.5% |
| Over 2.5 probability edge | +5.3% |
| Under 2.5 probability edge | -5.3% |
| Raw edge prob home | 0.3098 |
| Raw ev home | 0.7610 |
| Raw edge prob draw | -0.0788 |
| Raw ev draw | -0.3827 |
| Raw edge prob away | -0.2309 |
| Raw ev away | -0.6084 |

</details>


---

## 2026-10-20 — Porto vs PSV Eindhoven

The model's most likely 1X2 outcome is **Porto win** at **58.1%**. Expected goals are 2.11 for Porto and 1.17 for PSV Eindhoven (3.28 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 63.2%; Under 3.5 goals: 58.6%; Double Chance 1X: 78.9%; Double Chance X2: 41.9%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 76.9%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 58.1% | 1.72 |
| Draw | 20.8% | 4.82 |
| PSV Eindhoven win | 21.1% | 4.74 |

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
| 1 | 2-1 | 9.58% |
| 2 | 1-1 | 9.31% |
| 3 | 1-0 | 8.23% |
| 4 | 2-0 | 8.21% |
| 5 | 3-1 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 58.1% | 56.8% | 1.76 | +2.3% |
| Draw | 20.8% | 21.9% | 4.41 | -8.4% |
| PSV Eindhoven win | 21.1% | 21.3% | 4.51 | -4.9% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Porto |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.67 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.01 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.72 |
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
| P home draw | 78.9% |
| P draw away | 41.9% |
| P home away | 79.2% |
| Raw p home draw | 79.2% |
| Raw p draw away | 40.5% |
| Raw p home away | 80.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.72 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.40 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.42 |
| Home probability edge | +1.3% |
| Draw probability edge | -1.1% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | 0.0267 |
| Raw ev home | 0.0468 |
| Raw edge prob draw | -0.0217 |
| Raw ev draw | -0.1321 |
| Raw edge prob away | -0.0049 |
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
| Draw | 15.3% | 6.53 |
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
| 1 | 0-2 | 12.00% |
| 2 | 0-1 | 10.06% |
| 3 | 0-3 | 9.90% |
| 4 | 1-2 | 9.05% |
| 5 | 1-3 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 10.0% | 10.3% | 8.75 | -12.4% |
| Draw | 15.3% | 15.8% | 5.89 | -9.7% |
| Borussia Dortmund win | 74.7% | 73.9% | 1.37 | +2.3% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.03 |
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
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 8.50 |
| Reference draw odds | 5.70 |
| Reference away odds | 1.33 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.82 |
| Home probability edge | -0.3% |
| Draw probability edge | -0.5% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | -0.0062 |
| Raw ev home | -0.1507 |
| Raw edge prob draw | -0.0091 |
| Raw ev draw | -0.1243 |
| Raw edge prob away | 0.0153 |
| Raw ev away | 0.0334 |

</details>


---

## 2026-10-20 — VfB Stuttgart vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **48.2%**. Expected goals are 1.41 for VfB Stuttgart and 2.10 for Atlético Madrid (3.51 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 67.3%; Under 3.5 goals: 53.8%; Double Chance 1X: 51.8%; Double Chance X2: 70.6%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 72.9%; BTTS Yes (both teams score): 66.7%; BTTS No (at least one team does not score): 33.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 29.4% | 3.40 |
| Draw | 22.4% | 4.47 |
| Atlético Madrid win | 48.2% | 2.07 |

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
| Over 4.5 | 27.1% |
| Under 4.5 | 72.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.34% |
| 2 | 1-2 | 8.34% |
| 3 | 2-2 | 7.29% |
| 4 | 2-1 | 7.04% |
| 5 | 0-1 | 6.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 29.4% | 32.6% | 3.01 | -11.4% |
| Draw | 22.4% | 24.6% | 3.96 | -11.5% |
| Atlético Madrid win | 48.2% | 42.8% | 2.32 | +11.9% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | VfB Stuttgart |
| Matched away-team name | Club Atlético de Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.7% |
| P btts no | 33.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.38 |
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
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.93 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.26 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -3.2% |
| Draw probability edge | -2.2% |
| Away probability edge | +5.4% |
| Over 2.5 probability edge | +4.0% |
| Under 2.5 probability edge | -4.0% |
| Raw edge prob home | -0.0645 |
| Raw ev home | -0.2115 |
| Raw edge prob draw | -0.0442 |
| Raw ev draw | -0.2022 |
| Raw edge prob away | 0.1087 |
| Raw ev away | 0.2448 |

</details>


---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **81.6%**. Expected goals are 4.01 for Aston Villa and 1.16 for Viking FK (5.17 combined). The most likely exact score is 4-1 at 6.8%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.8%; Under 3.5 goals: 24.9%; Double Chance 1X: 93.6%; Double Chance X2: 18.4%; Double Chance 12 (either team wins): 88.0%; Under 4.5 goals: 42.7%; BTTS Yes (both teams score): 68.6%; BTTS No (at least one team does not score): 31.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 81.6% | 1.23 |
| Draw | 12.0% | 8.31 |
| Viking FK win | 6.4% | 15.59 |

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
| Over 2.5 | 87.8% |
| Under 2.5 | 12.2% |
| Over 3.5 | 75.1% |
| Under 3.5 | 24.9% |
| Over 4.5 | 57.3% |
| Under 4.5 | 42.7% |

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
| Aston Villa win | 81.6% | 77.5% | 1.30 | +6.0% |
| Draw | 12.0% | 15.8% | 5.90 | -29.0% |
| Viking FK win | 6.4% | 6.7% | 13.30 | -14.7% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 68.6% |
| P btts no | 31.4% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 156.54 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.52 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.18 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.02 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.34 |
| Unadjusted home-win probability | 85.6% |
| Unadjusted draw probability | 8.2% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 96.3% |
| Raw p under 3 5 | 24.3% |
| Raw p btts yes | 67.4% |
| P home draw | 93.6% |
| P draw away | 18.4% |
| P home away | 88.0% |
| Raw p home draw | 93.8% |
| Raw p draw away | 14.4% |
| Raw p home away | 91.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.27 |
| Reference draw odds | 5.65 |
| Reference away odds | 12.75 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.25 |
| Home probability edge | +4.0% |
| Draw probability edge | -3.8% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +15.2% |
| Under 2.5 probability edge | -15.2% |
| Raw edge prob home | 0.0806 |
| Raw ev home | 0.1126 |
| Raw edge prob draw | -0.0758 |
| Raw ev draw | -0.5139 |
| Raw edge prob away | -0.0048 |
| Raw ev away | -0.1787 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **37.2%**. Expected goals are 1.02 for Bayern Munich and 1.31 for Arsenal (2.33 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.6%; Double Chance 1X: 62.8%; Double Chance X2: 62.9%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 37.1% | 2.69 |
| Draw | 25.6% | 3.90 |
| Arsenal win | 37.2% | 2.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 1.02 |
| Arsenal expected goals | 1.31 |
| Expected total goals | 2.33 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 66.6% |
| Under 1.5 | 33.4% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.4% |
| Under 3.5 | 79.6% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.26% |
| 2 | 1-1 | 11.95% |
| 3 | 0-1 | 11.38% |
| 4 | 0-0 | 8.80% |
| 5 | 2-1 | 8.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 37.1% | 44.6% | 2.23 | -17.2% |
| Draw | 25.6% | 24.8% | 3.92 | +0.5% |
| Arsenal win | 37.2% | 30.6% | 3.21 | +19.6% |
| Over 2.5 | 41.2% | 59.2% | 1.68 | -30.8% |
| Under 2.5 | 58.8% | 40.8% | 2.38 | +40.0% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.36 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.90 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.53 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 29.6% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 43.9% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 79.4% |
| Raw p btts yes | 46.0% |
| P home draw | 62.8% |
| P draw away | 62.9% |
| P home away | 74.4% |
| Raw p home draw | 56.1% |
| Raw p draw away | 70.4% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.17 |
| Reference draw odds | 3.82 |
| Reference away odds | 3.12 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.31 |
| Home probability edge | -7.5% |
| Draw probability edge | +0.9% |
| Away probability edge | +6.7% |
| Over 2.5 probability edge | -18.1% |
| Under 2.5 probability edge | +18.1% |
| Raw edge prob home | -0.1503 |
| Raw ev home | -0.3397 |
| Raw edge prob draw | 0.0171 |
| Raw ev draw | 0.0381 |
| Raw edge prob away | 0.1332 |
| Raw ev away | 0.4094 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **59.7%**. Expected goals are 3.05 for Club Brugge and 1.27 for RC Lens (4.32 combined). The most likely exact score is 2-2 at 7.1%. Goal-market probabilities: at least one goal: 98.5%; Over 2.5 goals: 78.2%; Under 3.5 goals: 39.3%; Double Chance 1X: 79.1%; Double Chance X2: 40.3%; Double Chance 12 (either team wins): 80.6%; Under 4.5 goals: 59.2%; BTTS Yes (both teams score): 70.6%; BTTS No (at least one team does not score): 29.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 59.7% | 1.67 |
| Draw | 19.4% | 5.16 |
| RC Lens win | 20.9% | 4.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Club Brugge expected goals | 3.05 |
| RC Lens expected goals | 1.27 |
| Expected total goals | 4.32 |
| Over 0.5 | 98.5% |
| Under 0.5 | 1.5% |
| Over 1.5 | 91.9% |
| Under 1.5 | 8.1% |
| Over 2.5 | 78.2% |
| Under 2.5 | 21.8% |
| Over 3.5 | 60.7% |
| Under 3.5 | 39.3% |
| Over 4.5 | 40.8% |
| Under 4.5 | 59.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.05% |
| 2 | 1-1 | 6.90% |
| 3 | 3-1 | 6.51% |
| 4 | 2-1 | 6.40% |
| 5 | 1-2 | 5.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 59.7% | 46.2% | 2.16 | +29.0% |
| Draw | 19.4% | 25.0% | 3.88 | -24.8% |
| RC Lens win | 20.9% | 28.8% | 3.39 | -29.1% |
| Over 2.5 | 78.2% | 59.6% | 1.67 | +30.6% |
| Under 2.5 | 21.8% | 40.4% | 2.40 | -47.7% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| P btts yes | 70.6% |
| P btts no | 29.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 66.33 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.29 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.59 |
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
| P home draw | 79.1% |
| P draw away | 40.3% |
| P home away | 80.6% |
| Raw p home draw | 87.0% |
| Raw p draw away | 26.7% |
| Raw p home away | 86.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.10 |
| Reference draw odds | 3.78 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.33 |
| Home probability edge | +13.6% |
| Draw probability edge | -5.6% |
| Away probability edge | -7.9% |
| Over 2.5 probability edge | +18.6% |
| Under 2.5 probability edge | -18.6% |
| Raw edge prob home | 0.2710 |
| Raw ev home | 0.5824 |
| Raw edge prob draw | -0.1130 |
| Raw ev draw | -0.4676 |
| Raw edge prob away | -0.1581 |
| Raw ev away | -0.5588 |

</details>


---

## 2026-10-21 — Como vs Manchester United

The model's most likely 1X2 outcome is **Como win** at **50.9%**. Expected goals are 2.99 for Como and 1.94 for Manchester United (4.93 combined). The most likely exact score is 2-2 at 7.8%. Goal-market probabilities: at least one goal: 99.3%; Over 2.5 goals: 86.0%; Under 3.5 goals: 27.9%; Double Chance 1X: 71.9%; Double Chance X2: 49.1%; Double Chance 12 (either team wins): 79.0%; Under 4.5 goals: 46.6%; BTTS Yes (both teams score): 82.3%; BTTS No (at least one team does not score): 17.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 50.9% | 1.96 |
| Draw | 21.0% | 4.77 |
| Manchester United win | 28.1% | 3.56 |

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
| 1 | 2-2 | 7.81% |
| 2 | 2-1 | 5.34% |
| 3 | 3-1 | 5.33% |
| 4 | 3-2 | 5.17% |
| 5 | 1-1 | 5.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 50.9% | 42.2% | 2.35 | +19.7% |
| Draw | 21.0% | 25.6% | 3.80 | -20.4% |
| Manchester United win | 28.1% | 32.2% | 3.05 | -14.2% |
| Over 2.5 | 86.0% | 57.0% | 1.74 | +49.6% |
| Under 2.5 | 14.0% | 43.0% | 2.27 | -68.2% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
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
| P btts yes | 82.3% |
| P btts no | 17.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 152.30 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 21.96 |
| Fair Over 2.5 odds | 1.16 |
| Fair Under 2.5 odds | 7.14 |
| Fair Over 3.5 odds | 1.39 |
| Fair Under 3.5 odds | 3.59 |
| Fair Over 4.5 odds | 1.87 |
| Fair Under 4.5 odds | 2.14 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 95.5% |
| Raw p under 3 5 | 27.4% |
| Raw p btts yes | 81.1% |
| P home draw | 71.9% |
| P draw away | 49.1% |
| P home away | 79.0% |
| Raw p home draw | 76.0% |
| Raw p draw away | 40.3% |
| Raw p home away | 83.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.29 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.97 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.20 |
| Home probability edge | +8.7% |
| Draw probability edge | -4.7% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | +29.0% |
| Under 2.5 probability edge | -29.0% |
| Raw edge prob home | 0.1746 |
| Raw ev home | 0.4019 |
| Raw edge prob draw | -0.0931 |
| Raw ev draw | -0.3805 |
| Raw edge prob away | -0.0815 |
| Raw ev away | -0.2667 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **73.1%**. Expected goals are 2.05 for Inter Milan and 0.92 for Shakhtar Donetsk (2.97 combined). The most likely exact score is 1-0 at 12.5%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 59.1%; Under 3.5 goals: 64.2%; Double Chance 1X: 88.6%; Double Chance X2: 26.9%; Double Chance 12 (either team wins): 84.6%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 50.5%; BTTS No (at least one team does not score): 49.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 73.1% | 1.37 |
| Draw | 15.4% | 6.47 |
| Shakhtar Donetsk win | 11.4% | 8.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.05 |
| Shakhtar Donetsk expected goals | 0.92 |
| Expected total goals | 2.97 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 80.2% |
| Under 1.5 | 19.8% |
| Over 2.5 | 59.1% |
| Under 2.5 | 40.9% |
| Over 3.5 | 35.8% |
| Under 3.5 | 64.2% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.55% |
| 2 | 2-0 | 12.30% |
| 3 | 2-1 | 11.33% |
| 4 | 3-0 | 8.41% |
| 5 | 3-1 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 73.1% | 82.3% | 1.22 | -10.8% |
| Draw | 15.4% | 11.4% | 8.10 | +25.1% |
| Shakhtar Donetsk win | 11.4% | 6.3% | 14.10 | +60.9% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | FK Shakhtar Donetsk |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.5% |
| P btts no | 49.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.21 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.05 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.24 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 64.0% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 16.5% |
| Raw p over 1 5 | 79.2% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 52.0% |
| P home draw | 88.6% |
| P draw away | 26.9% |
| P home away | 84.6% |
| Raw p home draw | 83.5% |
| Raw p draw away | 36.0% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.20 |
| Reference draw odds | 7.60 |
| Reference away odds | 13.25 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.40 |
| Home probability edge | -9.1% |
| Draw probability edge | +4.0% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -14.7% |
| Under 2.5 probability edge | +14.7% |
| Raw edge prob home | -0.1828 |
| Raw ev home | -0.2192 |
| Raw edge prob draw | 0.0805 |
| Raw ev draw | 0.5773 |
| Raw edge prob away | 0.1022 |
| Raw ev away | 1.3300 |

</details>


---

## 2026-10-21 — Lille vs Galatasaray

The model's most likely 1X2 outcome is **Lille win** at **57.6%**. Expected goals are 2.57 for Lille and 1.04 for Galatasaray (3.61 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.2%; Under 3.5 goals: 53.5%; Double Chance 1X: 78.1%; Double Chance X2: 42.4%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 72.6%; BTTS Yes (both teams score): 61.4%; BTTS No (at least one team does not score): 38.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 57.6% | 1.74 |
| Draw | 20.5% | 4.87 |
| Galatasaray win | 21.9% | 4.58 |

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
| Over 2.5 | 67.2% |
| Under 2.5 | 32.8% |
| Over 3.5 | 46.5% |
| Under 3.5 | 53.5% |
| Over 4.5 | 27.4% |
| Under 4.5 | 72.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.97% |
| 2 | 2-1 | 7.57% |
| 3 | 2-0 | 7.30% |
| 4 | 3-1 | 6.48% |
| 5 | 2-2 | 6.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 57.6% | 44.4% | 2.24 | +29.0% |
| Draw | 20.5% | 25.3% | 3.84 | -21.1% |
| Galatasaray win | 21.9% | 30.2% | 3.25 | -29.0% |
| Over 2.5 | 67.2% | 57.7% | 1.72 | +15.5% |
| Under 2.5 | 32.8% | 42.3% | 2.30 | -24.5% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille OSC |
| Matched away-team name | Galatasaray SK |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 61.4% |
| P btts no | 38.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.54 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.05 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.05 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.65 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 70.8% |
| Unadjusted draw probability | 15.7% |
| Unadjusted away-win probability | 13.5% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 51.4% |
| Raw p btts yes | 59.2% |
| P home draw | 78.1% |
| P draw away | 42.4% |
| P home away | 79.5% |
| Raw p home draw | 86.5% |
| Raw p draw away | 29.2% |
| Raw p home away | 84.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.18 |
| Reference draw odds | 3.74 |
| Reference away odds | 3.16 |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | +13.2% |
| Draw probability edge | -4.8% |
| Away probability edge | -8.4% |
| Over 2.5 probability edge | +9.5% |
| Under 2.5 probability edge | -9.5% |
| Raw edge prob home | 0.2632 |
| Raw ev home | 0.5851 |
| Raw edge prob draw | -0.0961 |
| Raw ev draw | -0.3957 |
| Raw edge prob away | -0.1670 |
| Raw ev away | -0.5612 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **77.4%**. Expected goals are 5.75 for Real Betis and 1.65 for Feyenoord (7.40 combined). The most likely exact score is 5-1 at 4.6%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.7%; Under 3.5 goals: 7.9%; Double Chance 1X: 89.8%; Double Chance X2: 22.6%; Double Chance 12 (either team wins): 87.6%; Under 4.5 goals: 17.6%; BTTS Yes (both teams score): 82.8%; BTTS No (at least one team does not score): 17.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 77.4% | 1.29 |
| Draw | 12.4% | 8.06 |
| Feyenoord win | 10.2% | 9.84 |

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
| Over 3.5 | 92.1% |
| Under 3.5 | 7.9% |
| Over 4.5 | 82.4% |
| Under 4.5 | 17.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-1 | 4.64% |
| 2 | 6-1 | 4.45% |
| 3 | 4-1 | 4.03% |
| 4 | 3-3 | 3.83% |
| 5 | 5-2 | 3.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 77.4% | 63.6% | 1.58 | +22.3% |
| Draw | 12.4% | 20.0% | 4.78 | -40.7% |
| Feyenoord win | 10.2% | 16.4% | 5.75 | -41.6% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 82.8% |
| P btts no | 17.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1170.72 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 129.89 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 29.93 |
| Fair Over 3.5 odds | 1.09 |
| Fair Under 3.5 odds | 12.63 |
| Fair Over 4.5 odds | 1.21 |
| Fair Under 4.5 odds | 5.69 |
| Unadjusted home-win probability | 91.3% |
| Unadjusted draw probability | 4.8% |
| Unadjusted away-win probability | 3.9% |
| Raw p over 1 5 | 99.4% |
| Raw p under 3 5 | 6.5% |
| Raw p btts yes | 80.4% |
| P home draw | 89.8% |
| P draw away | 22.6% |
| P home away | 87.6% |
| Raw p home draw | 96.1% |
| Raw p draw away | 8.7% |
| Raw p home away | 95.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.54 |
| Reference draw odds | 4.65 |
| Reference away odds | 5.60 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.78 |
| Home probability edge | +13.8% |
| Draw probability edge | -7.6% |
| Away probability edge | -6.3% |
| Over 2.5 probability edge | +29.5% |
| Under 2.5 probability edge | -29.5% |
| Raw edge prob home | 0.2768 |
| Raw ev home | 0.4421 |
| Raw edge prob draw | -0.1513 |
| Raw ev draw | -0.7688 |
| Raw edge prob away | -0.1254 |
| Raw ev away | -0.7763 |

</details>


---

## 2026-10-21 — Real Madrid vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid win** at **76.6%**. Expected goals are 2.80 for Real Madrid and 0.88 for RB Leipzig (3.68 combined). The most likely exact score is 2-0 at 9.8%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 70.8%; Under 3.5 goals: 50.0%; Double Chance 1X: 90.4%; Double Chance X2: 23.4%; Double Chance 12 (either team wins): 86.2%; Under 4.5 goals: 69.4%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 76.6% | 1.30 |
| Draw | 13.8% | 7.25 |
| RB Leipzig win | 9.6% | 10.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.80 |
| RB Leipzig expected goals | 0.88 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 87.8% |
| Under 1.5 | 12.2% |
| Over 2.5 | 70.8% |
| Under 2.5 | 29.2% |
| Over 3.5 | 50.0% |
| Under 3.5 | 50.0% |
| Over 4.5 | 30.6% |
| Under 4.5 | 69.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.80% |
| 2 | 3-0 | 9.15% |
| 3 | 2-1 | 8.59% |
| 4 | 3-1 | 8.02% |
| 5 | 1-0 | 7.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 76.6% | 75.7% | 1.33 | +1.9% |
| Draw | 13.8% | 14.4% | 6.44 | -11.2% |
| RB Leipzig win | 9.6% | 9.8% | 9.20 | -11.9% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.99 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.18 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.42 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.26 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 77.6% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 9.3% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 49.9% |
| Raw p btts yes | 54.5% |
| P home draw | 90.4% |
| P draw away | 23.4% |
| P home away | 86.2% |
| Raw p home draw | 90.7% |
| Raw p draw away | 22.4% |
| Raw p home away | 86.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.30 |
| Reference draw odds | 6.20 |
| Reference away odds | 8.90 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.75 |
| Home probability edge | +0.9% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | 0.0184 |
| Raw ev home | 0.0314 |
| Raw edge prob draw | -0.0130 |
| Raw ev draw | -0.1535 |
| Raw edge prob away | -0.0054 |
| Raw ev away | -0.1440 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **85.9%**. Expected goals are 6.10 for Sporting Lisbon and 1.32 for LASK (7.42 combined). The most likely exact score is 6-1 at 5.4%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.7%; Under 3.5 goals: 7.9%; Double Chance 1X: 94.3%; Double Chance X2: 14.1%; Double Chance 12 (either team wins): 91.6%; Under 4.5 goals: 17.2%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 85.9% | 1.16 |
| Draw | 8.4% | 11.87 |
| LASK win | 5.7% | 17.69 |

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
| Over 3.5 | 92.1% |
| Under 3.5 | 7.9% |
| Over 4.5 | 82.8% |
| Under 4.5 | 17.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 6-1 | 5.38% |
| 2 | 5-1 | 5.29% |
| 3 | 7-1 | 4.69% |
| 4 | 4-1 | 4.33% |
| 5 | 6-0 | 4.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 85.9% | 76.9% | 1.31 | +12.6% |
| Draw | 8.4% | 13.8% | 6.75 | -43.1% |
| LASK win | 5.7% | 9.3% | 9.70 | -45.2% |

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
| Market best home last update utc | 2026-10-15T09:51:13Z |
| Market best draw last update utc | 2026-10-15T09:51:13Z |
| Market best away last update utc | 2026-10-15T09:51:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 75.1% |
| P btts no | 24.9% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 969.46 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 127.70 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 30.17 |
| Fair Over 3.5 odds | 1.09 |
| Fair Under 3.5 odds | 12.68 |
| Fair Over 4.5 odds | 1.21 |
| Fair Under 4.5 odds | 5.80 |
| Unadjusted home-win probability | 94.9% |
| Unadjusted draw probability | 3.1% |
| Unadjusted away-win probability | 2.0% |
| Raw p over 1 5 | 99.4% |
| Raw p under 3 5 | 6.5% |
| Raw p btts yes | 73.0% |
| P home draw | 94.3% |
| P draw away | 14.1% |
| P home away | 91.6% |
| Raw p home draw | 98.0% |
| Raw p draw away | 5.1% |
| Raw p home away | 96.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.28 |
| Reference draw odds | 6.45 |
| Reference away odds | 9.30 |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.30 |
| Home probability edge | +9.0% |
| Draw probability edge | -5.3% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | +24.0% |
| Under 2.5 probability edge | -24.0% |
| Raw edge prob home | 0.1804 |
| Raw ev home | 0.2438 |
| Raw edge prob draw | -0.1069 |
| Raw ev draw | -0.7923 |
| Raw edge prob away | -0.0735 |
| Raw ev away | -0.8083 |

</details>


---
