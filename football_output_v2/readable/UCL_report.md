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
| Training sha256 | 69681f50534010abc80aed2668b760ed900e1ae77b384daae0a91fec7f9a1851 |
| Training as of utc | 2026-10-17T09:46:08.436394+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 36, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 27, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-17T09:46:08.436394+00:00', 'observations': 36, 'observations_sha256': '96abc7ff010eab6c78efed87a87e63f37f9f974a2555387c520682be6c8465c7', 'eligible_training_matches': 0, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 27, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 0, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': 'd79830c5086bda43682fc8825e0b02bb4182c5cc89f61b19e957edc892610489', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 968.105 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.306 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0009 |
| Training data health | {'completed_matches': 36, 'latest_completed_utc': '2026-10-14T19:00:00+00:00', 'latest_completed_date': '2026-10-14', 'next_fixture_utc': '2026-10-20T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-17T09:46:01.982404+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '1107dc7c46d6e7b4db47bd6e12b654b35cd0cc81b6c7f0fbe37933c6c273e13e', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.001792775, 'training_end': '2026-10-14', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 44.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261017T094608436394Z_16aeb420ceeb20c46ee5f686435f5be6fc81c5a40e148dfc42f94faedf719422.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
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

The model's most likely 1X2 outcome is **AS Roma win** at **82.8%**. Expected goals are 3.76 for AS Roma and 1.32 for ŠK Slovan Bratislava (5.07 combined). The most likely exact score is 3-1 at 7.4%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 88.2%; Under 3.5 goals: 25.1%; Double Chance 1X: 93.3%; Double Chance X2: 17.2%; Double Chance 12 (either team wins): 89.6%; Under 4.5 goals: 42.5%; BTTS Yes (both teams score): 71.2%; BTTS No (at least one team does not score): 28.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 82.8% | 1.21 |
| Draw | 10.4% | 9.57 |
| ŠK Slovan Bratislava win | 6.7% | 14.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 3.76 |
| ŠK Slovan Bratislava expected goals | 1.32 |
| Expected total goals | 5.07 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 88.2% |
| Under 2.5 | 11.8% |
| Over 3.5 | 74.9% |
| Under 3.5 | 25.1% |
| Over 4.5 | 57.5% |
| Under 4.5 | 42.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.44% |
| 2 | 4-1 | 6.99% |
| 3 | 2-1 | 5.94% |
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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.7594 |
| Dc lambda away | 1.3153 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 71.2% |
| P btts no | 28.8% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 205.99 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.36 |
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
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.40 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | -1.7% |
| Draw probability edge | -0.3% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +13.7% |
| Under 2.5 probability edge | -13.7% |
| Raw edge prob home | -0.0345 |
| Raw ev home | -0.0023 |
| Raw edge prob draw | -0.0064 |
| Raw ev draw | -0.2952 |
| Raw edge prob away | 0.0408 |
| Raw ev away | 0.4457 |

</details>


---

## 2026-10-20 — Fenerbahce vs Slavia Praha

The model's most likely 1X2 outcome is **Fenerbahce win** at **43.0%**. Expected goals are 0.78 for Fenerbahce and 1.07 for Slavia Praha (1.84 combined). The most likely exact score is 1-0 at 20.7%. Goal-market probabilities: at least one goal: 86.9%; Over 2.5 goals: 28.7%; Under 3.5 goals: 88.8%; Double Chance 1X: 69.5%; Double Chance X2: 57.0%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 33.9%; BTTS No (at least one team does not score): 66.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 43.0% | 2.32 |
| Draw | 26.4% | 3.78 |
| Slavia Praha win | 30.5% | 3.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 0.78 |
| Slavia Praha expected goals | 1.07 |
| Expected total goals | 1.84 |
| Over 0.5 | 86.9% |
| Under 0.5 | 13.1% |
| Over 1.5 | 53.6% |
| Under 1.5 | 46.4% |
| Over 2.5 | 28.7% |
| Under 2.5 | 71.3% |
| Over 3.5 | 11.2% |
| Under 3.5 | 88.8% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.74% |
| 2 | 0-0 | 13.10% |
| 3 | 0-1 | 12.60% |
| 4 | 1-1 | 10.76% |
| 5 | 2-1 | 8.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 43.0% | 59.2% | 1.74 | -25.1% |
| Draw | 26.4% | 22.3% | 4.31 | +13.9% |
| Slavia Praha win | 30.5% | 18.5% | 4.83 | +47.5% |
| Over 2.5 | 28.7% | 58.0% | 1.69 | -51.5% |
| Under 2.5 | 71.3% | 42.0% | 2.36 | +68.3% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fenerbahçe SK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7762 |
| Dc lambda away | 1.0672 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 33.9% |
| P btts no | 66.1% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.63 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.48 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.90 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.98 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 54.3% |
| Raw p under 3 5 | 88.4% |
| Raw p btts yes | 34.8% |
| P home draw | 69.5% |
| P draw away | 57.0% |
| P home away | 73.6% |
| Raw p home draw | 57.5% |
| Raw p draw away | 73.1% |
| Raw p home away | 69.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.65 |
| Reference draw odds | 4.20 |
| Reference away odds | 5.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | -16.2% |
| Draw probability edge | +4.2% |
| Away probability edge | +12.0% |
| Over 2.5 probability edge | -29.3% |
| Under 2.5 probability edge | +29.3% |
| Raw edge prob home | -0.3235 |
| Raw ev home | -0.5328 |
| Raw edge prob draw | 0.0835 |
| Raw ev draw | 0.3192 |
| Raw edge prob away | 0.2400 |
| Raw ev away | 1.0547 |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool FC |
| Matched away-team name | Villarreal CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.3553 |
| Dc lambda away | 0.5056 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 41.4% |
| P btts no | 58.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.71 |
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
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
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
| Raw ev away | -0.8227 |

</details>


---

## 2026-10-20 — Manchester City vs AEK Athens

The model's most likely 1X2 outcome is **Manchester City win** at **84.5%**. Expected goals are 1.97 for Manchester City and 0.39 for AEK Athens (2.36 combined). The most likely exact score is 1-0 at 21.1%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 45.3%; Under 3.5 goals: 77.1%; Double Chance 1X: 95.7%; Double Chance X2: 15.5%; Double Chance 12 (either team wins): 88.8%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 25.8%; BTTS No (at least one team does not score): 74.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 84.5% | 1.18 |
| Draw | 11.2% | 8.92 |
| AEK Athens win | 4.3% | 23.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.97 |
| AEK Athens expected goals | 0.39 |
| Expected total goals | 2.36 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 70.5% |
| Under 1.5 | 29.5% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 22.9% |
| Under 3.5 | 77.1% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 21.06% |
| 2 | 2-0 | 20.39% |
| 3 | 3-0 | 13.42% |
| 4 | 2-1 | 7.96% |
| 5 | 4-0 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 84.5% | 93.1% | 1.07 | -9.6% |
| Draw | 11.2% | 5.0% | 17.00 | +90.6% |
| AEK Athens win | 4.3% | 1.9% | 42.00 | +80.5% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Manchester City FC |
| Matched away-team name | PAE AEK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9744 |
| Dc lambda away | 0.3903 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 25.8% |
| P btts no | 74.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.21 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.37 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.98 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 75.9% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 6.7% |
| Raw p over 1 5 | 68.0% |
| Raw p under 3 5 | 78.6% |
| Raw p btts yes | 27.5% |
| P home draw | 95.7% |
| P draw away | 15.5% |
| P home away | 88.8% |
| Raw p home draw | 93.3% |
| Raw p draw away | 24.1% |
| Raw p home away | 82.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.07 |
| Reference draw odds | 17.00 |
| Reference away odds | 42.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.75 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | -8.6% |
| Draw probability edge | +6.2% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -32.4% |
| Under 2.5 probability edge | +32.4% |
| Raw edge prob home | -0.1721 |
| Raw ev home | -0.1880 |
| Raw edge prob draw | 0.1245 |
| Raw ev draw | 1.9642 |
| Raw edge prob away | 0.0476 |
| Raw ev away | 1.8053 |

</details>


---

## 2026-10-20 — Napoli vs Bodø/Glimt

The model's most likely 1X2 outcome is **Napoli win** at **43.0%**. Expected goals are 1.17 for Napoli and 1.78 for Bodø/Glimt (2.94 combined). The most likely exact score is 1-0 at 11.3%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 55.7%; Under 3.5 goals: 67.3%; Double Chance 1X: 64.5%; Double Chance X2: 57.0%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 43.0% | 2.33 |
| Draw | 21.5% | 4.64 |
| Bodø/Glimt win | 35.5% | 2.82 |

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
| 1 | 1-0 | 11.26% |
| 2 | 2-1 | 10.72% |
| 3 | 1-1 | 10.04% |
| 4 | 0-1 | 6.73% |
| 5 | 1-2 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 43.0% | 60.4% | 1.64 | -29.5% |
| Draw | 21.5% | 20.8% | 4.67 | +0.5% |
| Bodø/Glimt win | 35.5% | 18.7% | 5.18 | +83.9% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | SSC Napoli |
| Matched away-team name | FK Bodø/Glimt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.1659 |
| Dc lambda away | 1.7782 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.88 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.43 |
| Fair Over 2.5 odds | 1.79 |
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
| P home draw | 64.5% |
| P draw away | 57.0% |
| P home away | 78.5% |
| Raw p home draw | 47.7% |
| Raw p draw away | 74.5% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.64 |
| Reference draw odds | 4.67 |
| Reference away odds | 5.18 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | -17.5% |
| Draw probability edge | +0.7% |
| Away probability edge | +16.8% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | -0.3493 |
| Raw ev home | -0.5818 |
| Raw edge prob draw | 0.0141 |
| Raw ev draw | 0.0383 |
| Raw edge prob away | 0.3352 |
| Raw ev away | 1.7073 |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris Saint-Germain FC |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.2231 |
| Dc lambda away | 1.5228 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 76.8% |
| P btts no | 23.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 118.37 |
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
| Raw p under 3 5 | 30.3% |
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
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.00 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | +15.7% |
| Draw probability edge | -4.0% |
| Away probability edge | -11.7% |
| Over 2.5 probability edge | +4.0% |
| Under 2.5 probability edge | -4.0% |
| Raw edge prob home | 0.3145 |
| Raw ev home | 0.7684 |
| Raw edge prob draw | -0.0801 |
| Raw ev draw | -0.3664 |
| Raw edge prob away | -0.2344 |
| Raw ev away | -0.6161 |

</details>


---

## 2026-10-20 — Porto vs PSV Eindhoven

The model's most likely 1X2 outcome is **Porto win** at **57.9%**. Expected goals are 2.11 for Porto and 1.17 for PSV Eindhoven (3.28 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 63.2%; Under 3.5 goals: 58.6%; Double Chance 1X: 78.8%; Double Chance X2: 42.1%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 76.9%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 57.9% | 1.73 |
| Draw | 20.9% | 4.79 |
| PSV Eindhoven win | 21.2% | 4.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Porto expected goals | 2.11 |
| PSV Eindhoven expected goals | 1.17 |
| Expected total goals | 3.28 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 63.2% |
| Under 2.5 | 36.8% |
| Over 3.5 | 41.4% |
| Under 3.5 | 58.6% |
| Over 4.5 | 23.1% |
| Under 4.5 | 76.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.54% |
| 2 | 1-1 | 9.37% |
| 3 | 1-0 | 8.20% |
| 4 | 2-0 | 8.17% |
| 5 | 3-1 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 57.9% | 56.3% | 1.76 | +1.9% |
| Draw | 20.9% | 22.1% | 4.41 | -7.8% |
| PSV Eindhoven win | 21.2% | 21.6% | 4.51 | -4.2% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Porto |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1111 |
| Dc lambda away | 1.1671 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.50 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.00 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.72 |
| Fair Over 3.5 odds | 2.42 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.33 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 59.5% |
| Unadjusted draw probability | 19.7% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 60.1% |
| P home draw | 78.8% |
| P draw away | 42.1% |
| P home away | 79.1% |
| Raw p home draw | 79.1% |
| Raw p draw away | 40.5% |
| Raw p home away | 80.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.76 |
| Reference draw odds | 4.41 |
| Reference away odds | 4.51 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | +1.6% |
| Draw probability edge | -1.2% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | 0.0319 |
| Raw ev home | 0.0466 |
| Raw edge prob draw | -0.0243 |
| Raw ev draw | -0.1320 |
| Raw edge prob away | -0.0076 |
| Raw ev away | -0.0596 |

</details>


---

## 2026-10-20 — Sabah FK vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **75.9%**. Expected goals are 0.75 for Sabah FK and 2.47 for Borussia Dortmund (3.23 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 62.7%; Under 3.5 goals: 59.5%; Double Chance 1X: 24.1%; Double Chance X2: 90.8%; Double Chance 12 (either team wins): 85.1%; Under 4.5 goals: 77.5%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 9.2% | 10.87 |
| Draw | 14.9% | 6.71 |
| Borussia Dortmund win | 75.9% | 1.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.75 |
| Borussia Dortmund expected goals | 2.47 |
| Expected total goals | 3.23 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 62.7% |
| Under 2.5 | 37.3% |
| Over 3.5 | 40.5% |
| Under 3.5 | 59.5% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.20% |
| 2 | 0-1 | 10.23% |
| 3 | 0-3 | 10.06% |
| 4 | 1-2 | 9.20% |
| 5 | 1-3 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 9.2% | 8.7% | 9.40 | -13.5% |
| Draw | 14.9% | 15.0% | 6.11 | -8.9% |
| Borussia Dortmund win | 75.9% | 76.3% | 1.34 | +1.7% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7543 |
| Dc lambda away | 2.4749 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.77 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.88 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.47 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.44 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 9.7% |
| Unadjusted draw probability | 14.9% |
| Unadjusted away-win probability | 75.4% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 59.6% |
| Raw p btts yes | 48.1% |
| P home draw | 24.1% |
| P draw away | 90.8% |
| P home away | 85.1% |
| Raw p home draw | 24.6% |
| Raw p draw away | 90.3% |
| Raw p home away | 85.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 10.00 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.29 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | +0.5% |
| Draw probability edge | -0.0% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | 0.0100 |
| Raw ev home | -0.0878 |
| Raw edge prob draw | -0.0009 |
| Raw ev draw | -0.0917 |
| Raw edge prob away | -0.0091 |
| Raw ev away | 0.0108 |

</details>


---

## 2026-10-20 — VfB Stuttgart vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **48.1%**. Expected goals are 1.41 for VfB Stuttgart and 2.10 for Atlético Madrid (3.51 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 67.3%; Under 3.5 goals: 53.8%; Double Chance 1X: 51.9%; Double Chance X2: 70.6%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 73.0%; BTTS Yes (both teams score): 66.7%; BTTS No (at least one team does not score): 33.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 29.4% | 3.40 |
| Draw | 22.4% | 4.46 |
| Atlético Madrid win | 48.1% | 2.08 |

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
| 2 | 1-2 | 8.33% |
| 3 | 2-2 | 7.32% |
| 4 | 2-1 | 7.04% |
| 5 | 0-1 | 6.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 29.4% | 32.7% | 3.01 | -11.4% |
| Draw | 22.4% | 24.7% | 3.96 | -11.1% |
| Atlético Madrid win | 48.1% | 42.6% | 2.32 | +11.6% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | VfB Stuttgart |
| Matched away-team name | Club Atlético de Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4143 |
| Dc lambda away | 2.0957 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
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
| Raw p under 3 5 | 53.4% |
| Raw p btts yes | 65.9% |
| P home draw | 51.9% |
| P draw away | 70.6% |
| P home away | 77.6% |
| Raw p home draw | 46.3% |
| Raw p draw away | 73.8% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 3.01 |
| Reference draw odds | 3.96 |
| Reference away odds | 2.32 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | -3.2% |
| Draw probability edge | -2.3% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | +3.5% |
| Under 2.5 probability edge | -3.5% |
| Raw edge prob home | -0.0649 |
| Raw ev home | -0.2115 |
| Raw edge prob draw | -0.0460 |
| Raw ev draw | -0.2022 |
| Raw edge prob away | 0.1109 |
| Raw ev away | 0.2449 |

</details>


---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **80.8%**. Expected goals are 4.01 for Aston Villa and 1.16 for Viking FK (5.17 combined). The most likely exact score is 4-1 at 6.7%. Goal-market probabilities: at least one goal: 99.3%; Over 2.5 goals: 87.7%; Under 3.5 goals: 25.0%; Double Chance 1X: 93.1%; Double Chance X2: 19.2%; Double Chance 12 (either team wins): 87.7%; Under 4.5 goals: 42.8%; BTTS Yes (both teams score): 68.8%; BTTS No (at least one team does not score): 31.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 80.8% | 1.24 |
| Draw | 12.3% | 8.10 |
| Viking FK win | 6.9% | 14.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 4.01 |
| Viking FK expected goals | 1.16 |
| Expected total goals | 5.17 |
| Over 0.5 | 99.3% |
| Under 0.5 | 0.7% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 87.7% |
| Under 2.5 | 12.3% |
| Over 3.5 | 75.0% |
| Under 3.5 | 25.0% |
| Over 4.5 | 57.2% |
| Under 4.5 | 42.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-1 | 6.70% |
| 2 | 3-1 | 6.69% |
| 3 | 4-0 | 5.75% |
| 4 | 3-0 | 5.74% |
| 5 | 5-1 | 5.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 80.8% | 75.9% | 1.31 | +5.8% |
| Draw | 12.3% | 16.5% | 5.85 | -27.8% |
| Viking FK win | 6.9% | 7.6% | 12.50 | -14.1% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.0061 |
| Dc lambda away | 1.1641 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 23 |
| Score grid omitted mass | 0 |
| P btts yes | 68.8% |
| P btts no | 31.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 152.57 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.21 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.11 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.00 |
| Fair Over 4.5 odds | 1.75 |
| Fair Under 4.5 odds | 2.34 |
| Unadjusted home-win probability | 85.6% |
| Unadjusted draw probability | 8.2% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.2% |
| Raw p btts yes | 67.4% |
| P home draw | 93.1% |
| P draw away | 19.2% |
| P home away | 87.7% |
| Raw p home draw | 93.8% |
| Raw p draw away | 14.4% |
| Raw p home away | 91.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.31 |
| Reference draw odds | 5.85 |
| Reference away odds | 12.50 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | +4.9% |
| Draw probability edge | -4.1% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +13.4% |
| Under 2.5 probability edge | -13.4% |
| Raw edge prob home | 0.0972 |
| Raw ev home | 0.1218 |
| Raw edge prob draw | -0.0828 |
| Raw ev draw | -0.5196 |
| Raw edge prob away | -0.0144 |
| Raw ev away | -0.2307 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **37.3%**. Expected goals are 1.02 for Bayern Munich and 1.31 for Arsenal (2.33 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 41.1%; Under 3.5 goals: 79.6%; Double Chance 1X: 62.7%; Double Chance X2: 63.0%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 45.9%; BTTS No (at least one team does not score): 54.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 37.0% | 2.70 |
| Draw | 25.8% | 3.88 |
| Arsenal win | 37.3% | 2.68 |

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
| Over 2.5 | 41.1% |
| Under 2.5 | 58.9% |
| Over 3.5 | 20.4% |
| Under 3.5 | 79.6% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.20% |
| 2 | 1-1 | 12.01% |
| 3 | 0-1 | 11.39% |
| 4 | 0-0 | 8.84% |
| 5 | 2-1 | 8.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 37.0% | 44.3% | 2.23 | -17.5% |
| Draw | 25.8% | 25.0% | 3.92 | +0.9% |
| Arsenal win | 37.3% | 30.6% | 3.21 | +19.7% |
| Over 2.5 | 41.1% | 58.8% | 1.68 | -30.9% |
| Under 2.5 | 58.9% | 41.2% | 2.38 | +40.1% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
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
| Dc lambda home | 1.0183 |
| Dc lambda away | 1.3102 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 45.9% |
| P btts no | 54.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.31 |
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
| P home draw | 62.7% |
| P draw away | 63.0% |
| P home away | 74.2% |
| Raw p home draw | 56.1% |
| Raw p draw away | 70.4% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.23 |
| Reference draw odds | 3.92 |
| Reference away odds | 3.21 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | -7.4% |
| Draw probability edge | +0.7% |
| Away probability edge | +6.6% |
| Over 2.5 probability edge | -17.7% |
| Under 2.5 probability edge | +17.7% |
| Raw edge prob home | -0.1472 |
| Raw ev home | -0.3396 |
| Raw edge prob draw | 0.0146 |
| Raw ev draw | 0.0380 |
| Raw edge prob away | 0.1326 |
| Raw ev away | 0.4094 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **59.5%**. Expected goals are 3.05 for Club Brugge and 1.27 for RC Lens (4.32 combined). The most likely exact score is 2-2 at 7.1%. Goal-market probabilities: at least one goal: 98.5%; Over 2.5 goals: 78.2%; Under 3.5 goals: 39.3%; Double Chance 1X: 79.0%; Double Chance X2: 40.5%; Double Chance 12 (either team wins): 80.5%; Under 4.5 goals: 59.3%; BTTS Yes (both teams score): 70.7%; BTTS No (at least one team does not score): 29.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 59.5% | 1.68 |
| Draw | 19.5% | 5.13 |
| RC Lens win | 21.0% | 4.76 |

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
| Over 4.5 | 40.7% |
| Under 4.5 | 59.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.10% |
| 2 | 1-1 | 6.94% |
| 3 | 3-1 | 6.48% |
| 4 | 2-1 | 6.38% |
| 5 | 1-2 | 5.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 59.5% | 45.8% | 2.16 | +28.6% |
| Draw | 19.5% | 25.3% | 3.88 | -24.4% |
| RC Lens win | 21.0% | 29.0% | 3.39 | -28.8% |
| Over 2.5 | 78.2% | 59.2% | 1.67 | +30.5% |
| Under 2.5 | 21.8% | 40.8% | 2.40 | -47.6% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
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
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.0510 |
| Dc lambda away | 1.2727 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 70.7% |
| P btts no | 29.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 65.93 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.28 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.58 |
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
| P home draw | 79.0% |
| P draw away | 40.5% |
| P home away | 80.5% |
| Raw p home draw | 87.0% |
| Raw p draw away | 26.7% |
| Raw p home away | 86.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.16 |
| Reference draw odds | 3.88 |
| Reference away odds | 3.39 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | +13.7% |
| Draw probability edge | -5.8% |
| Away probability edge | -8.0% |
| Over 2.5 probability edge | +19.0% |
| Under 2.5 probability edge | -19.0% |
| Raw edge prob home | 0.2750 |
| Raw ev home | 0.5826 |
| Raw edge prob draw | -0.1154 |
| Raw ev draw | -0.4677 |
| Raw edge prob away | -0.1595 |
| Raw ev away | -0.5588 |

</details>


---

## 2026-10-21 — Como vs Manchester United

The model's most likely 1X2 outcome is **Como win** at **50.6%**. Expected goals are 2.99 for Como and 1.94 for Manchester United (4.93 combined). The most likely exact score is 2-2 at 7.8%. Goal-market probabilities: at least one goal: 99.3%; Over 2.5 goals: 86.0%; Under 3.5 goals: 27.9%; Double Chance 1X: 71.4%; Double Chance X2: 49.4%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 46.6%; BTTS Yes (both teams score): 82.3%; BTTS No (at least one team does not score): 17.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 50.6% | 1.98 |
| Draw | 20.9% | 4.79 |
| Manchester United win | 28.6% | 3.50 |

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
| 1 | 2-2 | 7.78% |
| 2 | 2-1 | 5.30% |
| 3 | 3-1 | 5.29% |
| 4 | 3-2 | 5.13% |
| 5 | 1-1 | 5.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 50.6% | 41.5% | 2.38 | +20.4% |
| Draw | 20.9% | 25.4% | 3.85 | -19.7% |
| Manchester United win | 28.6% | 33.1% | 2.97 | -15.2% |
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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Como 1907 |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.9924 |
| Dc lambda away | 1.9419 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 82.3% |
| P btts no | 17.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 152.99 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 21.91 |
| Fair Over 2.5 odds | 1.16 |
| Fair Under 2.5 odds | 7.15 |
| Fair Over 3.5 odds | 1.39 |
| Fair Under 3.5 odds | 3.59 |
| Fair Over 4.5 odds | 1.87 |
| Fair Under 4.5 odds | 2.14 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 95.5% |
| Raw p under 3 5 | 27.4% |
| Raw p btts yes | 81.2% |
| P home draw | 71.4% |
| P draw away | 49.4% |
| P home away | 79.1% |
| Raw p home draw | 76.0% |
| Raw p draw away | 40.3% |
| Raw p home away | 83.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.38 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.97 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.34 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | +9.1% |
| Draw probability edge | -4.6% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | +27.9% |
| Under 2.5 probability edge | -27.9% |
| Raw edge prob home | 0.1822 |
| Raw ev home | 0.4203 |
| Raw edge prob draw | -0.0914 |
| Raw ev draw | -0.3727 |
| Raw edge prob away | -0.0908 |
| Raw ev away | -0.2864 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **72.1%**. Expected goals are 2.05 for Inter Milan and 0.92 for Shakhtar Donetsk (2.97 combined). The most likely exact score is 1-0 at 12.4%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 58.8%; Under 3.5 goals: 64.3%; Double Chance 1X: 88.1%; Double Chance X2: 27.9%; Double Chance 12 (either team wins): 84.0%; Under 4.5 goals: 81.1%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 72.1% | 1.39 |
| Draw | 16.0% | 6.23 |
| Shakhtar Donetsk win | 11.9% | 8.42 |

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
| 1 | 1-0 | 12.37% |
| 2 | 2-0 | 12.12% |
| 3 | 2-1 | 11.17% |
| 4 | 3-0 | 8.29% |
| 5 | 3-1 | 7.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 72.1% | 80.2% | 1.24 | -10.6% |
| Draw | 16.0% | 12.6% | 7.50 | +20.3% |
| Shakhtar Donetsk win | 11.9% | 7.2% | 12.90 | +53.2% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | FK Shakhtar Donetsk |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0512 |
| Dc lambda away | 0.9214 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.20 |
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
| P home draw | 88.1% |
| P draw away | 27.9% |
| P home away | 84.0% |
| Raw p home draw | 83.5% |
| Raw p draw away | 36.0% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.24 |
| Reference draw odds | 7.50 |
| Reference away odds | 12.90 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | -8.1% |
| Draw probability edge | +3.4% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -15.4% |
| Under 2.5 probability edge | +15.4% |
| Raw edge prob home | -0.1616 |
| Raw ev home | -0.2064 |
| Raw edge prob draw | 0.0686 |
| Raw ev draw | 0.4604 |
| Raw edge prob away | 0.0930 |
| Raw ev away | 1.1316 |

</details>


---

## 2026-10-21 — Lille vs Galatasaray

The model's most likely 1X2 outcome is **Lille win** at **57.5%**. Expected goals are 2.57 for Lille and 1.04 for Galatasaray (3.61 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.1%; Under 3.5 goals: 53.5%; Double Chance 1X: 78.1%; Double Chance X2: 42.5%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 72.6%; BTTS Yes (both teams score): 61.4%; BTTS No (at least one team does not score): 38.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 57.5% | 1.74 |
| Draw | 20.7% | 4.84 |
| Galatasaray win | 21.9% | 4.57 |

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
| 1 | 1-1 | 9.02% |
| 2 | 2-1 | 7.55% |
| 3 | 2-0 | 7.28% |
| 4 | 3-1 | 6.46% |
| 5 | 2-2 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 57.5% | 44.2% | 2.24 | +28.7% |
| Draw | 20.7% | 25.6% | 3.84 | -20.7% |
| Galatasaray win | 21.9% | 30.3% | 3.25 | -28.9% |
| Over 2.5 | 67.1% | 57.4% | 1.72 | +15.5% |
| Under 2.5 | 32.9% | 42.6% | 2.30 | -24.4% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille OSC |
| Matched away-team name | Galatasaray SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5691 |
| Dc lambda away | 1.0368 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 61.4% |
| P btts no | 38.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.36 |
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
| P home draw | 78.1% |
| P draw away | 42.5% |
| P home away | 79.3% |
| Raw p home draw | 86.5% |
| Raw p draw away | 29.2% |
| Raw p home away | 84.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 2.24 |
| Reference draw odds | 3.84 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market best over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market best under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | +13.3% |
| Draw probability edge | -4.9% |
| Away probability edge | -8.4% |
| Over 2.5 probability edge | +9.7% |
| Under 2.5 probability edge | -9.7% |
| Raw edge prob home | 0.2661 |
| Raw ev home | 0.5850 |
| Raw edge prob draw | -0.0983 |
| Raw ev draw | -0.3957 |
| Raw edge prob away | -0.1677 |
| Raw ev away | -0.5611 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **78.0%**. Expected goals are 5.75 for Real Betis and 1.65 for Feyenoord (7.40 combined). The most likely exact score is 5-1 at 4.5%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.7%; Under 3.5 goals: 7.7%; Double Chance 1X: 90.1%; Double Chance X2: 22.0%; Double Chance 12 (either team wins): 87.9%; Under 4.5 goals: 17.1%; BTTS Yes (both teams score): 82.8%; BTTS No (at least one team does not score): 17.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 78.0% | 1.28 |
| Draw | 12.1% | 8.26 |
| Feyenoord win | 9.9% | 10.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 5.75 |
| Feyenoord expected goals | 1.65 |
| Expected total goals | 7.40 |
| Over 0.5 | 99.9% |
| Under 0.5 | 0.1% |
| Over 1.5 | 99.3% |
| Under 1.5 | 0.7% |
| Over 2.5 | 96.7% |
| Under 2.5 | 3.3% |
| Over 3.5 | 92.3% |
| Under 3.5 | 7.7% |
| Over 4.5 | 82.9% |
| Under 4.5 | 17.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-1 | 4.51% |
| 2 | 6-1 | 4.32% |
| 3 | 4-1 | 3.92% |
| 4 | 3-3 | 3.73% |
| 5 | 5-2 | 3.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 78.0% | 64.5% | 1.56 | +21.7% |
| Draw | 12.1% | 19.5% | 4.93 | -40.3% |
| Feyenoord win | 9.9% | 16.0% | 5.80 | -42.7% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 5.7516 |
| Dc lambda away | 1.6457 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 27 |
| Score grid omitted mass | 0 |
| P btts yes | 82.8% |
| P btts no | 17.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1197.83 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 133.47 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 30.71 |
| Fair Over 3.5 odds | 1.08 |
| Fair Under 3.5 odds | 12.98 |
| Fair Over 4.5 odds | 1.21 |
| Fair Under 4.5 odds | 5.85 |
| Unadjusted home-win probability | 91.6% |
| Unadjusted draw probability | 4.7% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.3% |
| Raw p btts yes | 80.4% |
| P home draw | 90.1% |
| P draw away | 22.0% |
| P home away | 87.9% |
| Raw p home draw | 96.2% |
| Raw p draw away | 8.4% |
| Raw p home away | 95.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.52 |
| Reference draw odds | 4.75 |
| Reference away odds | 5.75 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | +13.5% |
| Draw probability edge | -7.4% |
| Away probability edge | -6.1% |
| Over 2.5 probability edge | +27.8% |
| Under 2.5 probability edge | -27.8% |
| Raw edge prob home | 0.2707 |
| Raw ev home | 0.4282 |
| Raw edge prob draw | -0.1485 |
| Raw ev draw | -0.7692 |
| Raw edge prob away | -0.1222 |
| Raw ev away | -0.7816 |

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
| 5 | 1-0 | 7.26% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8009 |
| Dc lambda away | 0.8771 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.25 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.14 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.41 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.27 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 77.5% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 9.3% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 49.9% |
| Raw p btts yes | 54.5% |
| P home draw | 90.2% |
| P draw away | 23.9% |
| P home away | 86.0% |
| Raw p home draw | 90.7% |
| Raw p draw away | 22.5% |
| Raw p home away | 86.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.33 |
| Reference draw odds | 6.44 |
| Reference away odds | 9.22 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | +1.4% |
| Draw probability edge | -0.9% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | 0.0281 |
| Raw ev home | 0.0159 |
| Raw edge prob draw | -0.0178 |
| Raw ev draw | -0.1061 |
| Raw edge prob away | -0.0104 |
| Raw ev away | -0.1065 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **86.7%**. Expected goals are 6.10 for Sporting Lisbon and 1.31 for LASK (7.41 combined). The most likely exact score is 6-1 at 5.2%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.8%; Under 3.5 goals: 7.5%; Double Chance 1X: 94.8%; Double Chance X2: 13.3%; Double Chance 12 (either team wins): 91.9%; Under 4.5 goals: 16.5%; BTTS Yes (both teams score): 75.0%; BTTS No (at least one team does not score): 25.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 86.7% | 1.15 |
| Draw | 8.1% | 12.34 |
| LASK win | 5.2% | 19.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 6.10 |
| LASK expected goals | 1.31 |
| Expected total goals | 7.41 |
| Over 0.5 | 99.9% |
| Under 0.5 | 0.1% |
| Over 1.5 | 99.3% |
| Under 1.5 | 0.7% |
| Over 2.5 | 96.8% |
| Under 2.5 | 3.2% |
| Over 3.5 | 92.5% |
| Under 3.5 | 7.5% |
| Over 4.5 | 83.5% |
| Under 4.5 | 16.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 6-1 | 5.16% |
| 2 | 5-1 | 5.08% |
| 3 | 7-1 | 4.50% |
| 4 | 4-1 | 4.16% |
| 5 | 6-0 | 3.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 86.7% | 78.2% | 1.27 | +10.1% |
| Draw | 8.1% | 13.3% | 7.13 | -42.2% |
| LASK win | 5.2% | 8.5% | 11.00 | -42.9% |

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
| Market best home last update utc | 2026-10-17T09:10:51Z |
| Market best draw last update utc | 2026-10-17T09:10:51Z |
| Market best away last update utc | 2026-10-17T09:10:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 6.0999 |
| Dc lambda away | 1.3148 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T09:46:08.436394+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 28 |
| Score grid omitted mass | 0 |
| P btts yes | 75.0% |
| P btts no | 25.0% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1003.41 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 134.92 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 31.51 |
| Fair Over 3.5 odds | 1.08 |
| Fair Under 3.5 odds | 13.28 |
| Fair Over 4.5 odds | 1.20 |
| Fair Under 4.5 odds | 6.06 |
| Unadjusted home-win probability | 95.2% |
| Unadjusted draw probability | 2.9% |
| Unadjusted away-win probability | 1.9% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.3% |
| Raw p btts yes | 73.0% |
| P home draw | 94.8% |
| P draw away | 13.3% |
| P home away | 91.9% |
| Raw p home draw | 98.1% |
| Raw p draw away | 4.8% |
| Raw p home away | 97.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / 1xBet |
| Reference home odds | 1.27 |
| Reference draw odds | 7.13 |
| Reference away odds | 11.00 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:51Z |
| Market reference home last update utc | 2026-10-17T09:10:51Z |
| Market reference draw last update utc | 2026-10-17T09:10:51Z |
| Market reference away last update utc | 2026-10-17T09:10:51Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:51Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:51Z |
| Home probability edge | +8.5% |
| Draw probability edge | -5.2% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | +25.2% |
| Under 2.5 probability edge | -25.2% |
| Raw edge prob home | 0.1696 |
| Raw ev home | 0.2088 |
| Raw edge prob draw | -0.1034 |
| Raw ev draw | -0.7907 |
| Raw edge prob away | -0.0662 |
| Raw ev away | -0.7927 |

</details>


---
