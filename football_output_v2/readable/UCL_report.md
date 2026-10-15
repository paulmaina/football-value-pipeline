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
| Training data health | {'completed_matches': 36, 'latest_completed_utc': '2026-10-14T19:00:00+00:00', 'latest_completed_date': '2026-10-14', 'next_fixture_utc': '2026-10-20T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-15T13:16:05.522736+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'f5f38255aec6d88e6c074d41d73adc99ffbb9a98768a2ad902be176e17dbe29f', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0005541702777777778, 'training_end': '2026-10-14', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 32.00 |
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

The model's most likely 1X2 outcome is **AS Roma win** at **83.7%**. Expected goals are 3.76 for AS Roma and 1.32 for ŠK Slovan Bratislava (5.08 combined). The most likely exact score is 3-1 at 7.5%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 88.4%; Under 3.5 goals: 25.0%; Double Chance 1X: 93.4%; Double Chance X2: 16.3%; Double Chance 12 (either team wins): 90.3%; Under 4.5 goals: 42.3%; BTTS Yes (both teams score): 70.9%; BTTS No (at least one team does not score): 29.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 83.7% | 1.19 |
| Draw | 9.7% | 10.33 |
| ŠK Slovan Bratislava win | 6.6% | 15.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 3.76 |
| ŠK Slovan Bratislava expected goals | 1.32 |
| Expected total goals | 5.08 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 88.4% |
| Under 2.5 | 11.6% |
| Over 3.5 | 75.0% |
| Under 3.5 | 25.0% |
| Over 4.5 | 57.7% |
| Under 4.5 | 42.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.53% |
| 2 | 4-1 | 7.08% |
| 3 | 2-1 | 6.01% |
| 4 | 3-0 | 5.72% |
| 5 | 4-0 | 5.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 83.7% | 86.3% | 1.16 | -2.9% |
| Draw | 9.7% | 9.2% | 9.65 | -6.6% |
| ŠK Slovan Bratislava win | 6.6% | 4.5% | 20.00 | +32.6% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 70.9% |
| P btts no | 29.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 222.43 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.47 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.65 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.00 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 81.1% |
| Unadjusted draw probability | 10.1% |
| Unadjusted away-win probability | 8.8% |
| Raw p over 1 5 | 96.0% |
| Raw p under 3 5 | 25.5% |
| Raw p btts yes | 71.3% |
| P home draw | 93.4% |
| P draw away | 16.3% |
| P home away | 90.3% |
| Raw p home draw | 91.2% |
| Raw p draw away | 18.9% |
| Raw p home away | 89.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.15 |
| Reference draw odds | 9.60 |
| Reference away odds | 19.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.40 |
| Home probability edge | -2.6% |
| Draw probability edge | +0.5% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +13.9% |
| Under 2.5 probability edge | -13.9% |
| Raw edge prob home | -0.0522 |
| Raw ev home | -0.0594 |
| Raw edge prob draw | 0.0093 |
| Raw ev draw | -0.0212 |
| Raw edge prob away | 0.0429 |
| Raw ev away | 0.7550 |

</details>


---

## 2026-10-20 — Fenerbahce vs Slavia Praha

The model's most likely 1X2 outcome is **Fenerbahce win** at **42.9%**. Expected goals are 0.78 for Fenerbahce and 1.07 for Slavia Praha (1.84 combined). The most likely exact score is 1-0 at 20.7%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 28.6%; Under 3.5 goals: 88.8%; Double Chance 1X: 69.6%; Double Chance X2: 57.1%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 34.0%; BTTS No (at least one team does not score): 66.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 42.9% | 2.33 |
| Draw | 26.7% | 3.75 |
| Slavia Praha win | 30.4% | 3.29 |

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
| 1 | 1-0 | 20.69% |
| 2 | 0-0 | 13.25% |
| 3 | 0-1 | 12.55% |
| 4 | 1-1 | 10.86% |
| 5 | 2-1 | 8.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 42.9% | 58.9% | 1.68 | -28.0% |
| Draw | 26.7% | 22.8% | 4.42 | +18.0% |
| Slavia Praha win | 30.4% | 18.3% | 5.13 | +56.1% |
| Over 2.5 | 28.6% | 57.7% | 1.70 | -51.4% |
| Under 2.5 | 71.4% | 42.3% | 2.34 | +67.1% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
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
| P btts yes | 34.0% |
| P btts no | 66.0% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.55 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.50 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.92 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 25.12 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 42.6% |
| Raw p over 1 5 | 54.3% |
| Raw p under 3 5 | 88.4% |
| Raw p btts yes | 34.7% |
| P home draw | 69.6% |
| P draw away | 57.1% |
| P home away | 73.3% |
| Raw p home draw | 57.4% |
| Raw p draw away | 73.2% |
| Raw p home away | 69.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.67 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.20 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Home probability edge | -16.1% |
| Draw probability edge | +3.9% |
| Away probability edge | +12.1% |
| Over 2.5 probability edge | -29.1% |
| Under 2.5 probability edge | +29.1% |
| Raw edge prob home | -0.3213 |
| Raw ev home | -0.5495 |
| Raw edge prob draw | 0.0784 |
| Raw ev draw | 0.3532 |
| Raw edge prob away | 0.2429 |
| Raw ev away | 1.1837 |

</details>


---

## 2026-10-20 — Liverpool vs Villarreal

The model's most likely 1X2 outcome is **Liverpool win** at **78.0%**. Expected goals are 3.36 for Liverpool and 0.51 for Villarreal (3.86 combined). The most likely exact score is 3-0 at 11.5%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 69.0%; Under 3.5 goals: 50.4%; Double Chance 1X: 91.6%; Double Chance X2: 22.0%; Double Chance 12 (either team wins): 86.4%; Under 4.5 goals: 69.2%; BTTS Yes (both teams score): 41.2%; BTTS No (at least one team does not score): 58.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 78.0% | 1.28 |
| Draw | 13.6% | 7.34 |
| Villarreal win | 8.4% | 11.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 3.36 |
| Villarreal expected goals | 0.51 |
| Expected total goals | 3.86 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 86.5% |
| Under 1.5 | 13.5% |
| Over 2.5 | 69.0% |
| Under 2.5 | 31.0% |
| Over 3.5 | 49.6% |
| Under 3.5 | 50.4% |
| Over 4.5 | 30.8% |
| Under 4.5 | 69.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 11.52% |
| 2 | 2-0 | 10.30% |
| 3 | 4-0 | 9.66% |
| 4 | 5-0 | 6.48% |
| 5 | 1-1 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 78.0% | 66.2% | 1.57 | +22.5% |
| Draw | 13.6% | 20.1% | 4.72 | -35.7% |
| Villarreal win | 8.4% | 13.7% | 5.96 | -50.2% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool FC |
| Matched away-team name | Villarreal CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.25 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.43 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.23 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.24 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 89.9% |
| Unadjusted draw probability | 7.2% |
| Unadjusted away-win probability | 3.0% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 46.2% |
| Raw p btts yes | 38.1% |
| P home draw | 91.6% |
| P draw away | 22.0% |
| P home away | 86.4% |
| Raw p home draw | 97.0% |
| Raw p draw away | 10.1% |
| Raw p home away | 92.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.48 |
| Reference draw odds | 4.60 |
| Reference away odds | 6.60 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Home probability edge | +11.8% |
| Draw probability edge | -6.5% |
| Away probability edge | -5.4% |
| Over 2.5 probability edge | +6.9% |
| Under 2.5 probability edge | -6.9% |
| Raw edge prob home | 0.2367 |
| Raw ev home | 0.4109 |
| Raw edge prob draw | -0.1292 |
| Raw ev draw | -0.6622 |
| Raw edge prob away | -0.1075 |
| Raw ev away | -0.8226 |

</details>


---

## 2026-10-20 — Manchester City vs AEK Athens

The model's most likely 1X2 outcome is **Manchester City win** at **79.3%**. Expected goals are 2.34 for Manchester City and 1.07 for AEK Athens (3.40 combined). The most likely exact score is 2-1 at 11.6%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 68.9%; Under 3.5 goals: 54.1%; Double Chance 1X: 90.7%; Double Chance X2: 20.7%; Double Chance 12 (either team wins): 88.6%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 56.4%; BTTS No (at least one team does not score): 43.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 79.3% | 1.26 |
| Draw | 11.4% | 8.77 |
| AEK Athens win | 9.3% | 10.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 2.34 |
| AEK Athens expected goals | 1.07 |
| Expected total goals | 3.40 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 86.0% |
| Under 1.5 | 14.0% |
| Over 2.5 | 68.9% |
| Under 2.5 | 31.1% |
| Over 3.5 | 45.9% |
| Under 3.5 | 54.1% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.62% |
| 2 | 2-0 | 10.91% |
| 3 | 1-0 | 9.84% |
| 4 | 3-1 | 9.05% |
| 5 | 3-0 | 8.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 79.3% | 92.5% | 1.07 | -15.1% |
| Draw | 11.4% | 5.2% | 17.00 | +93.9% |
| AEK Athens win | 9.3% | 2.3% | 42.00 | +290.2% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
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
| Fair Under 0.5 odds | 52.97 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.15 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.22 |
| Fair Over 3.5 odds | 2.18 |
| Fair Under 3.5 odds | 1.85 |
| Fair Over 4.5 odds | 3.63 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 66.1% |
| Unadjusted draw probability | 17.6% |
| Unadjusted away-win probability | 16.3% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 55.8% |
| Raw p btts yes | 58.8% |
| P home draw | 90.7% |
| P draw away | 20.7% |
| P home away | 88.6% |
| Raw p home draw | 83.7% |
| Raw p draw away | 33.9% |
| Raw p home away | 82.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.07 |
| Reference draw odds | 13.00 |
| Reference away odds | 26.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.75 |
| Home probability edge | -13.2% |
| Draw probability edge | +6.2% |
| Away probability edge | +7.0% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.2637 |
| Raw ev home | -0.2925 |
| Raw edge prob draw | 0.1245 |
| Raw ev draw | 1.9971 |
| Raw edge prob away | 0.1392 |
| Raw ev away | 5.8255 |

</details>


---

## 2026-10-20 — Napoli vs Bodø/Glimt

The model's most likely 1X2 outcome is **Napoli win** at **43.0%**. Expected goals are 1.17 for Napoli and 1.78 for Bodø/Glimt (2.94 combined). The most likely exact score is 1-0 at 11.3%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 55.7%; Under 3.5 goals: 67.3%; Double Chance 1X: 64.7%; Double Chance X2: 57.0%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 43.0% | 2.32 |
| Draw | 21.6% | 4.63 |
| Bodø/Glimt win | 35.3% | 2.83 |

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
| 1 | 1-0 | 11.28% |
| 2 | 2-1 | 10.74% |
| 3 | 1-1 | 10.08% |
| 4 | 0-1 | 6.70% |
| 5 | 1-2 | 6.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 43.0% | 60.6% | 1.64 | -29.4% |
| Draw | 21.6% | 21.0% | 4.67 | +0.9% |
| Bodø/Glimt win | 35.3% | 18.4% | 5.18 | +83.1% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | SSC Napoli |
| Matched away-team name | FK Bodø/Glimt |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.81 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.43 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.89 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 25.5% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 52.3% |
| Raw p over 1 5 | 78.7% |
| Raw p under 3 5 | 66.0% |
| Raw p btts yes | 56.7% |
| P home draw | 64.7% |
| P draw away | 57.0% |
| P home away | 78.4% |
| Raw p home draw | 47.7% |
| Raw p draw away | 74.5% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.62 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.10 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Home probability edge | -17.5% |
| Draw probability edge | +0.6% |
| Away probability edge | +16.9% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | -0.3510 |
| Raw ev home | -0.5818 |
| Raw edge prob draw | 0.0125 |
| Raw ev draw | 0.0382 |
| Raw edge prob away | 0.3385 |
| Raw ev away | 1.7075 |

</details>


---

## 2026-10-20 — Paris Saint Germain vs Barcelona

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **55.6%**. Expected goals are 3.22 for Paris Saint Germain and 1.52 for Barcelona (4.75 combined). The most likely exact score is 2-2 at 6.7%. Goal-market probabilities: at least one goal: 99.2%; Over 2.5 goals: 83.6%; Under 3.5 goals: 32.2%; Double Chance 1X: 73.4%; Double Chance X2: 44.4%; Double Chance 12 (either team wins): 82.3%; Under 4.5 goals: 51.0%; BTTS Yes (both teams score): 76.7%; BTTS No (at least one team does not score): 23.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 55.6% | 1.80 |
| Draw | 17.7% | 5.64 |
| Barcelona win | 26.6% | 3.76 |

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
| 1 | 2-2 | 6.70% |
| 2 | 3-1 | 5.79% |
| 3 | 1-2 | 5.72% |
| 4 | 2-1 | 5.39% |
| 5 | 1-1 | 5.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 55.6% | 40.3% | 2.49 | +38.6% |
| Draw | 17.7% | 21.6% | 4.51 | -20.0% |
| Barcelona win | 26.6% | 38.1% | 2.54 | -32.4% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
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
| Fair Under 0.5 odds | 119.24 |
| Fair Over 1.5 odds | 1.06 |
| Fair Under 1.5 odds | 16.94 |
| Fair Over 2.5 odds | 1.20 |
| Fair Under 2.5 odds | 6.10 |
| Fair Over 3.5 odds | 1.47 |
| Fair Under 3.5 odds | 3.11 |
| Fair Over 4.5 odds | 2.04 |
| Fair Under 4.5 odds | 1.96 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 94.8% |
| Raw p under 3 5 | 30.3% |
| Raw p btts yes | 74.9% |
| P home draw | 73.4% |
| P draw away | 44.4% |
| P home away | 82.3% |
| Raw p home draw | 84.9% |
| Raw p draw away | 29.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.38 |
| Reference draw odds | 4.31 |
| Reference away odds | 2.51 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.00 |
| Home probability edge | +15.4% |
| Draw probability edge | -3.9% |
| Away probability edge | -11.5% |
| Over 2.5 probability edge | +4.0% |
| Under 2.5 probability edge | -4.0% |
| Raw edge prob home | 0.3072 |
| Raw ev home | 0.7681 |
| Raw edge prob draw | -0.0774 |
| Raw ev draw | -0.3744 |
| Raw edge prob away | -0.2298 |
| Raw ev away | -0.6159 |

</details>


---

## 2026-10-20 — Porto vs PSV Eindhoven

The model's most likely 1X2 outcome is **Porto win** at **58.5%**. Expected goals are 2.11 for Porto and 1.17 for PSV Eindhoven (3.28 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 63.4%; Under 3.5 goals: 58.6%; Double Chance 1X: 78.9%; Double Chance X2: 41.5%; Double Chance 12 (either team wins): 79.6%; Under 4.5 goals: 76.8%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 58.5% | 1.71 |
| Draw | 20.4% | 4.90 |
| PSV Eindhoven win | 21.1% | 4.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Porto expected goals | 2.11 |
| PSV Eindhoven expected goals | 1.17 |
| Expected total goals | 3.28 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 63.4% |
| Under 2.5 | 36.6% |
| Over 3.5 | 41.4% |
| Under 3.5 | 58.6% |
| Over 4.5 | 23.2% |
| Under 4.5 | 76.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.65% |
| 2 | 1-1 | 9.15% |
| 3 | 1-0 | 8.29% |
| 4 | 2-0 | 8.27% |
| 5 | 3-1 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 58.5% | 57.6% | 1.76 | +3.0% |
| Draw | 20.4% | 21.1% | 4.41 | -10.0% |
| PSV Eindhoven win | 21.1% | 21.3% | 4.51 | -5.0% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Porto |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.17 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.01 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.73 |
| Fair Over 3.5 odds | 2.42 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.31 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 59.5% |
| Unadjusted draw probability | 19.7% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 60.1% |
| P home draw | 78.9% |
| P draw away | 41.5% |
| P home away | 79.6% |
| Raw p home draw | 79.2% |
| Raw p draw away | 40.5% |
| Raw p home away | 80.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.69 |
| Reference draw odds | 4.38 |
| Reference away odds | 4.35 |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.29 |
| Home probability edge | +1.0% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | 0.0190 |
| Raw ev home | 0.0468 |
| Raw edge prob draw | -0.0146 |
| Raw ev draw | -0.1321 |
| Raw edge prob away | -0.0045 |
| Raw ev away | -0.0600 |

</details>


---

## 2026-10-20 — Sabah FK vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **74.8%**. Expected goals are 0.75 for Sabah FK and 2.47 for Borussia Dortmund (3.23 combined). The most likely exact score is 0-2 at 12.0%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 62.4%; Under 3.5 goals: 59.7%; Double Chance 1X: 25.2%; Double Chance X2: 90.2%; Double Chance 12 (either team wins): 84.6%; Under 4.5 goals: 77.7%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 9.8% | 10.21 |
| Draw | 15.4% | 6.48 |
| Borussia Dortmund win | 74.8% | 1.34 |

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
| 1 | 0-2 | 12.02% |
| 2 | 0-1 | 10.08% |
| 3 | 0-3 | 9.92% |
| 4 | 1-2 | 9.07% |
| 5 | 1-3 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 9.8% | 9.9% | 9.40 | -7.9% |
| Draw | 15.4% | 16.0% | 6.11 | -5.7% |
| Borussia Dortmund win | 74.8% | 74.1% | 1.34 | +0.2% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
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
| Fair Under 0.5 odds | 26.85 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.82 |
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
| P home draw | 25.2% |
| P draw away | 90.2% |
| P home away | 84.6% |
| Raw p home draw | 24.6% |
| Raw p draw away | 90.3% |
| Raw p home away | 85.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 9.60 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.34 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Home probability edge | -0.1% |
| Draw probability edge | -0.6% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | -0.0018 |
| Raw ev home | -0.0876 |
| Raw edge prob draw | -0.0112 |
| Raw ev draw | -0.0916 |
| Raw edge prob away | 0.0130 |
| Raw ev away | 0.0107 |

</details>


---

## 2026-10-20 — VfB Stuttgart vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **48.4%**. Expected goals are 1.41 for VfB Stuttgart and 2.10 for Atlético Madrid (3.51 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 67.4%; Under 3.5 goals: 53.8%; Double Chance 1X: 51.6%; Double Chance X2: 70.5%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 72.9%; BTTS Yes (both teams score): 66.6%; BTTS No (at least one team does not score): 33.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 29.5% | 3.39 |
| Draw | 22.1% | 4.53 |
| Atlético Madrid win | 48.4% | 2.06 |

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
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 46.2% |
| Under 3.5 | 53.8% |
| Over 4.5 | 27.1% |
| Under 4.5 | 72.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.23% |
| 2 | 1-2 | 8.38% |
| 3 | 2-2 | 7.20% |
| 4 | 2-1 | 7.05% |
| 5 | 0-1 | 6.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 29.5% | 32.7% | 3.01 | -11.3% |
| Draw | 22.1% | 24.0% | 3.96 | -12.5% |
| Atlético Madrid win | 48.4% | 43.2% | 2.32 | +12.4% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | VfB Stuttgart |
| Matched away-team name | Club Atlético de Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 66.6% |
| P btts no | 33.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.81 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.09 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.06 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.69 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 26.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 53.7% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 65.9% |
| P home draw | 51.6% |
| P draw away | 70.5% |
| P home away | 77.9% |
| Raw p home draw | 46.3% |
| Raw p draw away | 73.8% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.96 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.26 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Home probability edge | -3.3% |
| Draw probability edge | -1.9% |
| Away probability edge | +5.2% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Raw edge prob home | -0.0655 |
| Raw ev home | -0.2115 |
| Raw edge prob draw | -0.0388 |
| Raw ev draw | -0.2022 |
| Raw edge prob away | 0.1043 |
| Raw ev away | 0.2448 |

</details>


---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **82.0%**. Expected goals are 4.01 for Aston Villa and 1.16 for Viking FK (5.17 combined). The most likely exact score is 4-1 at 6.8%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.8%; Under 3.5 goals: 24.8%; Double Chance 1X: 93.9%; Double Chance X2: 18.0%; Double Chance 12 (either team wins): 88.1%; Under 4.5 goals: 42.6%; BTTS Yes (both teams score): 68.5%; BTTS No (at least one team does not score): 31.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 82.0% | 1.22 |
| Draw | 11.9% | 8.38 |
| Viking FK win | 6.1% | 16.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 4.01 |
| Viking FK expected goals | 1.16 |
| Expected total goals | 5.17 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.3% |
| Under 1.5 | 3.7% |
| Over 2.5 | 87.8% |
| Under 2.5 | 12.2% |
| Over 3.5 | 75.2% |
| Under 3.5 | 24.8% |
| Over 4.5 | 57.4% |
| Under 4.5 | 42.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-1 | 6.82% |
| 2 | 3-1 | 6.81% |
| 3 | 4-0 | 5.86% |
| 4 | 3-0 | 5.85% |
| 5 | 5-1 | 5.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 82.0% | 78.4% | 1.33 | +9.1% |
| Draw | 11.9% | 15.6% | 5.56 | -33.7% |
| Viking FK win | 6.1% | 6.0% | 11.90 | -27.8% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 68.5% |
| P btts no | 31.5% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 157.80 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.78 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.23 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.04 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.35 |
| Unadjusted home-win probability | 85.6% |
| Unadjusted draw probability | 8.2% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 96.3% |
| Raw p under 3 5 | 24.3% |
| Raw p btts yes | 67.4% |
| P home draw | 93.9% |
| P draw away | 18.0% |
| P home away | 88.1% |
| Raw p home draw | 93.8% |
| Raw p draw away | 14.4% |
| Raw p home away | 91.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.27 |
| Reference draw odds | 6.20 |
| Reference away odds | 16.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Home probability edge | +3.6% |
| Draw probability edge | -3.7% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +13.6% |
| Under 2.5 probability edge | -13.6% |
| Raw edge prob home | 0.0717 |
| Raw ev home | 0.1383 |
| Raw edge prob draw | -0.0739 |
| Raw ev draw | -0.5419 |
| Raw edge prob away | 0.0022 |
| Raw ev away | -0.2651 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **37.2%**. Expected goals are 1.02 for Bayern Munich and 1.31 for Arsenal (2.33 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.6%; Double Chance 1X: 62.8%; Double Chance X2: 62.9%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 45.9%; BTTS No (at least one team does not score): 54.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 37.1% | 2.69 |
| Draw | 25.6% | 3.90 |
| Arsenal win | 37.2% | 2.69 |

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
| 2 | 1-1 | 11.96% |
| 3 | 0-1 | 11.37% |
| 4 | 0-0 | 8.81% |
| 5 | 2-1 | 8.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 37.1% | 44.7% | 2.23 | -17.2% |
| Draw | 25.6% | 24.8% | 3.92 | +0.5% |
| Arsenal win | 37.2% | 30.5% | 3.21 | +19.5% |
| Over 2.5 | 41.2% | 58.1% | 1.68 | -30.8% |
| Under 2.5 | 58.8% | 41.9% | 2.38 | +40.0% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
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
| P btts yes | 45.9% |
| P btts no | 54.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.35 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.90 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.53 |
| Fair Under 4.5 odds | 1.09 |
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
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.18 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | -7.5% |
| Draw probability edge | +0.8% |
| Away probability edge | +6.7% |
| Over 2.5 probability edge | -16.9% |
| Under 2.5 probability edge | +16.9% |
| Raw edge prob home | -0.1506 |
| Raw ev home | -0.3397 |
| Raw edge prob draw | 0.0168 |
| Raw ev draw | 0.0381 |
| Raw edge prob away | 0.1338 |
| Raw ev away | 0.4094 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **59.7%**. Expected goals are 3.05 for Club Brugge and 1.27 for RC Lens (4.32 combined). The most likely exact score is 2-2 at 7.0%. Goal-market probabilities: at least one goal: 98.5%; Over 2.5 goals: 78.2%; Under 3.5 goals: 39.3%; Double Chance 1X: 78.9%; Double Chance X2: 40.3%; Double Chance 12 (either team wins): 80.8%; Under 4.5 goals: 59.2%; BTTS Yes (both teams score): 70.6%; BTTS No (at least one team does not score): 29.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 59.7% | 1.68 |
| Draw | 19.2% | 5.22 |
| RC Lens win | 21.1% | 4.73 |

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
| Over 2.5 | 78.2% |
| Under 2.5 | 21.8% |
| Over 3.5 | 60.7% |
| Under 3.5 | 39.3% |
| Over 4.5 | 40.8% |
| Under 4.5 | 59.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.98% |
| 2 | 1-1 | 6.83% |
| 3 | 3-1 | 6.51% |
| 4 | 2-1 | 6.40% |
| 5 | 1-2 | 5.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 59.7% | 46.1% | 2.16 | +28.9% |
| Draw | 19.2% | 24.6% | 3.88 | -25.6% |
| RC Lens win | 21.1% | 29.2% | 3.39 | -28.4% |
| Over 2.5 | 78.2% | 58.9% | 1.67 | +30.7% |
| Under 2.5 | 21.8% | 41.1% | 2.40 | -47.8% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
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
| Fair Under 0.5 odds | 67.01 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.27 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.60 |
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
| P home draw | 78.9% |
| P draw away | 40.3% |
| P home away | 80.8% |
| Raw p home draw | 87.0% |
| Raw p draw away | 26.7% |
| Raw p home away | 86.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.12 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.30 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.30 |
| Home probability edge | +13.6% |
| Draw probability edge | -5.5% |
| Away probability edge | -8.1% |
| Over 2.5 probability edge | +19.3% |
| Under 2.5 probability edge | -19.3% |
| Raw edge prob home | 0.2713 |
| Raw ev home | 0.5824 |
| Raw edge prob draw | -0.1090 |
| Raw ev draw | -0.4676 |
| Raw edge prob away | -0.1623 |
| Raw ev away | -0.5588 |

</details>


---

## 2026-10-21 — Como vs Manchester United

The model's most likely 1X2 outcome is **Como win** at **50.7%**. Expected goals are 2.99 for Como and 1.94 for Manchester United (4.93 combined). The most likely exact score is 2-2 at 7.7%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 86.0%; Under 3.5 goals: 27.9%; Double Chance 1X: 71.3%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 46.6%; BTTS Yes (both teams score): 82.2%; BTTS No (at least one team does not score): 17.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 50.7% | 1.97 |
| Draw | 20.6% | 4.85 |
| Manchester United win | 28.7% | 3.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.99 |
| Manchester United expected goals | 1.94 |
| Expected total goals | 4.93 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
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
| 1 | 2-2 | 7.69% |
| 2 | 2-1 | 5.31% |
| 3 | 3-1 | 5.30% |
| 4 | 3-2 | 5.15% |
| 5 | 1-1 | 5.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 50.7% | 41.7% | 2.38 | +20.6% |
| Draw | 20.6% | 24.9% | 3.85 | -20.6% |
| Manchester United win | 28.7% | 33.4% | 2.97 | -14.7% |
| Over 2.5 | 86.0% | 57.9% | 1.70 | +46.3% |
| Under 2.5 | 14.0% | 42.1% | 2.34 | -67.3% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
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
| P btts yes | 82.2% |
| P btts no | 17.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 154.75 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 21.87 |
| Fair Over 2.5 odds | 1.16 |
| Fair Under 2.5 odds | 7.16 |
| Fair Over 3.5 odds | 1.39 |
| Fair Under 3.5 odds | 3.58 |
| Fair Over 4.5 odds | 1.87 |
| Fair Under 4.5 odds | 2.15 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 95.5% |
| Raw p under 3 5 | 27.4% |
| Raw p btts yes | 81.1% |
| P home draw | 71.3% |
| P draw away | 49.3% |
| P home away | 79.4% |
| Raw p home draw | 76.0% |
| Raw p draw away | 40.3% |
| Raw p home away | 83.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.34 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.90 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.25 |
| Home probability edge | +9.0% |
| Draw probability edge | -4.3% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | +28.2% |
| Under 2.5 probability edge | -28.2% |
| Raw edge prob home | 0.1800 |
| Raw ev home | 0.4198 |
| Raw edge prob draw | -0.0864 |
| Raw ev draw | -0.3724 |
| Raw edge prob away | -0.0936 |
| Raw ev away | -0.2860 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **72.6%**. Expected goals are 2.05 for Inter Milan and 0.92 for Shakhtar Donetsk (2.97 combined). The most likely exact score is 1-0 at 12.5%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 59.0%; Under 3.5 goals: 64.3%; Double Chance 1X: 88.3%; Double Chance X2: 27.4%; Double Chance 12 (either team wins): 84.3%; Under 4.5 goals: 81.0%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 72.6% | 1.38 |
| Draw | 15.7% | 6.36 |
| Shakhtar Donetsk win | 11.7% | 8.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.05 |
| Shakhtar Donetsk expected goals | 0.92 |
| Expected total goals | 2.97 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 59.0% |
| Under 2.5 | 41.0% |
| Over 3.5 | 35.7% |
| Under 3.5 | 64.3% |
| Over 4.5 | 19.0% |
| Under 4.5 | 81.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.45% |
| 2 | 2-0 | 12.21% |
| 3 | 2-1 | 11.25% |
| 4 | 3-0 | 8.35% |
| 5 | 3-1 | 7.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 72.6% | 81.2% | 1.22 | -11.4% |
| Draw | 15.7% | 12.0% | 8.10 | +27.3% |
| Shakhtar Donetsk win | 11.7% | 6.8% | 14.10 | +64.6% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | FK Shakhtar Donetsk |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.74 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.03 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.80 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.26 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 64.0% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 16.5% |
| Raw p over 1 5 | 79.2% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 52.0% |
| P home draw | 88.3% |
| P draw away | 27.4% |
| P home away | 84.3% |
| Raw p home draw | 83.5% |
| Raw p draw away | 36.0% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.22 |
| Reference draw odds | 7.60 |
| Reference away odds | 13.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.50 |
| Home probability edge | -8.6% |
| Draw probability edge | +3.8% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -15.9% |
| Under 2.5 probability edge | +15.9% |
| Raw edge prob home | -0.1721 |
| Raw ev home | -0.2192 |
| Raw edge prob draw | 0.0750 |
| Raw ev draw | 0.5773 |
| Raw edge prob away | 0.0970 |
| Raw ev away | 1.3300 |

</details>


---

## 2026-10-21 — Lille vs Galatasaray

The model's most likely 1X2 outcome is **Lille win** at **57.5%**. Expected goals are 2.57 for Lille and 1.04 for Galatasaray (3.61 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.2%; Under 3.5 goals: 53.6%; Double Chance 1X: 78.0%; Double Chance X2: 42.5%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 72.6%; BTTS Yes (both teams score): 61.4%; BTTS No (at least one team does not score): 38.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 57.5% | 1.74 |
| Draw | 20.6% | 4.86 |
| Galatasaray win | 22.0% | 4.55 |

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
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.4% |
| Under 4.5 | 72.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.98% |
| 2 | 2-1 | 7.55% |
| 3 | 2-0 | 7.28% |
| 4 | 3-1 | 6.46% |
| 5 | 2-2 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 57.5% | 44.2% | 2.24 | +28.7% |
| Draw | 20.6% | 25.4% | 3.84 | -21.0% |
| Galatasaray win | 22.0% | 30.4% | 3.25 | -28.6% |
| Over 2.5 | 67.2% | 55.3% | 1.72 | +15.5% |
| Under 2.5 | 32.8% | 44.7% | 2.30 | -24.4% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
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
| P btts yes | 61.4% |
| P btts no | 38.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.49 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.04 |
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
| P home draw | 78.0% |
| P draw away | 42.5% |
| P home away | 79.4% |
| Raw p home draw | 86.5% |
| Raw p draw away | 29.2% |
| Raw p home away | 84.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.20 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.15 |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Home probability edge | +13.3% |
| Draw probability edge | -4.8% |
| Away probability edge | -8.5% |
| Over 2.5 probability edge | +11.9% |
| Under 2.5 probability edge | -11.9% |
| Raw edge prob home | 0.2660 |
| Raw ev home | 0.5851 |
| Raw edge prob draw | -0.0967 |
| Raw ev draw | -0.3957 |
| Raw edge prob away | -0.1694 |
| Raw ev away | -0.5612 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **76.9%**. Expected goals are 5.75 for Real Betis and 1.65 for Feyenoord (7.40 combined). The most likely exact score is 5-1 at 4.6%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.6%; Under 3.5 goals: 8.0%; Double Chance 1X: 89.5%; Double Chance X2: 23.1%; Double Chance 12 (either team wins): 87.4%; Under 4.5 goals: 17.7%; BTTS Yes (both teams score): 82.9%; BTTS No (at least one team does not score): 17.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 76.9% | 1.30 |
| Draw | 12.6% | 7.94 |
| Feyenoord win | 10.5% | 9.48 |

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
| Over 2.5 | 96.6% |
| Under 2.5 | 3.4% |
| Over 3.5 | 92.0% |
| Under 3.5 | 8.0% |
| Over 4.5 | 82.3% |
| Under 4.5 | 17.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-1 | 4.61% |
| 2 | 6-1 | 4.42% |
| 3 | 4-1 | 4.00% |
| 4 | 3-3 | 3.88% |
| 5 | 5-2 | 3.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 76.9% | 62.5% | 1.58 | +21.4% |
| Draw | 12.6% | 20.3% | 4.78 | -39.8% |
| Feyenoord win | 10.5% | 17.2% | 5.75 | -39.3% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 82.9% |
| P btts no | 17.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1153.48 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 127.88 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 29.61 |
| Fair Over 3.5 odds | 1.09 |
| Fair Under 3.5 odds | 12.52 |
| Fair Over 4.5 odds | 1.21 |
| Fair Under 4.5 odds | 5.66 |
| Unadjusted home-win probability | 91.3% |
| Unadjusted draw probability | 4.8% |
| Unadjusted away-win probability | 3.9% |
| Raw p over 1 5 | 99.4% |
| Raw p under 3 5 | 6.5% |
| Raw p btts yes | 80.4% |
| P home draw | 89.5% |
| P draw away | 23.1% |
| P home away | 87.4% |
| Raw p home draw | 96.1% |
| Raw p draw away | 8.7% |
| Raw p home away | 95.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.57 |
| Reference draw odds | 4.60 |
| Reference away odds | 5.40 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Home probability edge | +14.4% |
| Draw probability edge | -7.8% |
| Away probability edge | -6.7% |
| Over 2.5 probability edge | +29.9% |
| Under 2.5 probability edge | -29.9% |
| Raw edge prob home | 0.2882 |
| Raw ev home | 0.4421 |
| Raw edge prob draw | -0.1550 |
| Raw ev draw | -0.7688 |
| Raw edge prob away | -0.1332 |
| Raw ev away | -0.7763 |

</details>


---

## 2026-10-21 — Real Madrid vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid win** at **76.9%**. Expected goals are 2.80 for Real Madrid and 0.88 for RB Leipzig (3.68 combined). The most likely exact score is 2-0 at 9.8%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 70.8%; Under 3.5 goals: 50.0%; Double Chance 1X: 90.6%; Double Chance X2: 23.1%; Double Chance 12 (either team wins): 86.3%; Under 4.5 goals: 69.3%; BTTS Yes (both teams score): 54.7%; BTTS No (at least one team does not score): 45.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 76.9% | 1.30 |
| Draw | 13.7% | 7.30 |
| RB Leipzig win | 9.4% | 10.60 |

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
| Over 4.5 | 30.7% |
| Under 4.5 | 69.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.83% |
| 2 | 3-0 | 9.18% |
| 3 | 2-1 | 8.62% |
| 4 | 3-1 | 8.05% |
| 5 | 1-0 | 7.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 76.9% | 76.2% | 1.33 | +2.2% |
| Draw | 13.7% | 14.2% | 6.44 | -11.8% |
| RB Leipzig win | 9.4% | 9.6% | 9.20 | -13.2% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| P btts yes | 54.7% |
| P btts no | 45.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.30 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.20 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.43 |
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
| P home draw | 90.6% |
| P draw away | 23.1% |
| P home away | 86.3% |
| Raw p home draw | 90.7% |
| Raw p draw away | 22.4% |
| Raw p home away | 86.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.29 |
| Reference draw odds | 6.20 |
| Reference away odds | 9.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.50 |
| Home probability edge | +0.7% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | 0.0136 |
| Raw ev home | 0.0314 |
| Raw edge prob draw | -0.0110 |
| Raw ev draw | -0.1535 |
| Raw edge prob away | -0.0026 |
| Raw ev away | -0.1440 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **86.1%**. Expected goals are 6.10 for Sporting Lisbon and 1.32 for LASK (7.42 combined). The most likely exact score is 6-1 at 5.4%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.7%; Under 3.5 goals: 7.9%; Double Chance 1X: 94.5%; Double Chance X2: 13.9%; Double Chance 12 (either team wins): 91.5%; Under 4.5 goals: 17.2%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 86.1% | 1.16 |
| Draw | 8.5% | 11.82 |
| LASK win | 5.5% | 18.30 |

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
| 1 | 6-1 | 5.39% |
| 2 | 5-1 | 5.30% |
| 3 | 7-1 | 4.70% |
| 4 | 4-1 | 4.34% |
| 5 | 6-0 | 4.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 86.1% | 77.2% | 1.31 | +12.8% |
| Draw | 8.5% | 13.8% | 6.75 | -42.9% |
| LASK win | 5.5% | 9.0% | 9.70 | -47.0% |

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
| Market best home last update utc | 2026-10-15T13:12:18Z |
| Market best draw last update utc | 2026-10-15T13:12:18Z |
| Market best away last update utc | 2026-10-15T13:12:18Z |
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
| Fair Under 0.5 odds | 965.26 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 129.21 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 30.23 |
| Fair Over 3.5 odds | 1.09 |
| Fair Under 3.5 odds | 12.73 |
| Fair Over 4.5 odds | 1.21 |
| Fair Under 4.5 odds | 5.81 |
| Unadjusted home-win probability | 94.9% |
| Unadjusted draw probability | 3.1% |
| Unadjusted away-win probability | 2.0% |
| Raw p over 1 5 | 99.4% |
| Raw p under 3 5 | 6.5% |
| Raw p btts yes | 73.0% |
| P home draw | 94.5% |
| P draw away | 13.9% |
| P home away | 91.5% |
| Raw p home draw | 98.0% |
| Raw p draw away | 5.1% |
| Raw p home away | 96.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.28 |
| Reference draw odds | 6.60 |
| Reference away odds | 10.00 |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Home probability edge | +8.9% |
| Draw probability edge | -5.4% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | +25.1% |
| Under 2.5 probability edge | -25.1% |
| Raw edge prob home | 0.1774 |
| Raw ev home | 0.2438 |
| Raw edge prob draw | -0.1076 |
| Raw ev draw | -0.7923 |
| Raw edge prob away | -0.0698 |
| Raw ev away | -0.8083 |

</details>


---
