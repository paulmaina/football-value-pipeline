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
| Training seasons requested | 4 |
| Training seasons loaded | ['2023', '2024', '2025', '2026'] |
| Training sha256 | 2c73884bab97bdb405e9f8058c656817e215c06f01488766d48339f95bfab846 |
| Training as of utc | 2026-10-19T16:28:28.687092+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 36, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 27, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-19T16:28:28.687092+00:00', 'observations': 72, 'observations_sha256': '61cbc313444366e1c4e1403cb207fdec9c5604378c50f0632bb17910c0c683a3', 'eligible_training_matches': 0, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 27, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 0, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': 'c04fa61a8a77a7f4e2926d6978de98c106c73c7d87f97ab2cdd331435bbcf1b2', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 966.016 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.306 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0009 |
| Training data health | {'completed_matches': 36, 'latest_completed_utc': '2026-10-14T19:00:00+00:00', 'latest_completed_date': '2026-10-14', 'next_fixture_utc': '2026-10-20T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-19T16:28:17.953007+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '11271982db58bf0e54aca919510c8ba50df847df963cfb1b90e039aa6d6fd0f4', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0029816902777777777, 'training_end': '2026-10-14', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 3.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261019T162828687092Z_1e4231ddc9bc322a530059d3c606e4b2917d2b178ad7f750bd46913cf0db5a46.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
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

The model's most likely 1X2 outcome is **AS Roma win** at **83.1%**. Expected goals are 3.76 for AS Roma and 1.31 for ŠK Slovan Bratislava (5.08 combined). The most likely exact score is 3-1 at 7.5%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 88.3%; Under 3.5 goals: 25.1%; Double Chance 1X: 93.2%; Double Chance X2: 16.9%; Double Chance 12 (either team wins): 90.0%; Under 4.5 goals: 42.4%; BTTS Yes (both teams score): 71.1%; BTTS No (at least one team does not score): 28.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 83.1% | 1.20 |
| Draw | 10.0% | 9.96 |
| ŠK Slovan Bratislava win | 6.8% | 14.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 3.76 |
| ŠK Slovan Bratislava expected goals | 1.31 |
| Expected total goals | 5.08 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 88.3% |
| Under 2.5 | 11.7% |
| Over 3.5 | 74.9% |
| Under 3.5 | 25.1% |
| Over 4.5 | 57.6% |
| Under 4.5 | 42.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.46% |
| 2 | 4-1 | 7.02% |
| 3 | 2-1 | 5.95% |
| 4 | 3-0 | 5.68% |
| 5 | 4-0 | 5.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 83.1% | 85.1% | 1.17 | -2.7% |
| Draw | 10.0% | 10.0% | 9.15 | -8.1% |
| ŠK Slovan Bratislava win | 6.8% | 4.9% | 20.00 | +36.5% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.7605 |
| Dc lambda away | 1.3148 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 71.1% |
| P btts no | 28.9% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 214.18 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.35 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.58 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 3.99 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 81.1% |
| Unadjusted draw probability | 10.1% |
| Unadjusted away-win probability | 8.8% |
| Raw p over 1 5 | 96.0% |
| Raw p under 3 5 | 25.5% |
| Raw p btts yes | 71.3% |
| P home draw | 93.2% |
| P draw away | 16.9% |
| P home away | 90.0% |
| Raw p home draw | 91.2% |
| Raw p draw away | 18.9% |
| Raw p home away | 89.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 8.39 |
| Reference away odds | 16.16 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.60 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.1% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +12.8% |
| Under 2.5 probability edge | -12.8% |
| Raw edge prob home | -0.0401 |
| Raw ev home | -0.0508 |
| Raw edge prob draw | 0.0015 |
| Raw ev draw | -0.0741 |
| Raw edge prob away | 0.0385 |
| Raw ev away | 0.7500 |
| Market p home draw | 94.8% |
| Market home draw odds | 1.02 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-19T16:28:25Z |
| Market reference home draw last update utc | 2026-10-19T16:28:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 16.4% |
| Market draw away odds | 5.90 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-19T16:28:25Z |
| Market reference draw away last update utc | 2026-10-19T16:28:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.8% |
| Market home away odds | 1.09 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-19T16:28:25Z |
| Market reference home away last update utc | 2026-10-19T16:28:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.02 |
| Market reference dc draw away odds | 5.90 |
| Market reference dc home away odds | 1.09 |
| Market p over 1 5 | 91.4% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 6.40 |
| Market reference over 1 5 last update utc | 2026-10-19T16:27:48Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 43.8% |
| Market reference under 3 5 odds | 2.17 |
| Market reference under 3 5 opposite odds | 1.72 |
| Market reference under 3 5 last update utc | 2026-10-19T16:28:27Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 50.3% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-19T16:28:25Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 1.87 |
| Market reference btts yes last update utc | 2026-10-19T16:28:25Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Fenerbahce vs Slavia Praha

The model's most likely 1X2 outcome is **Fenerbahce win** at **43.1%**. Expected goals are 0.78 for Fenerbahce and 1.07 for Slavia Praha (1.84 combined). The most likely exact score is 1-0 at 20.8%. Goal-market probabilities: at least one goal: 87.1%; Over 2.5 goals: 28.8%; Under 3.5 goals: 88.7%; Double Chance 1X: 69.2%; Double Chance X2: 56.9%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 33.9%; BTTS No (at least one team does not score): 66.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 43.1% | 2.32 |
| Draw | 26.0% | 3.84 |
| Slavia Praha win | 30.8% | 3.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 0.78 |
| Slavia Praha expected goals | 1.07 |
| Expected total goals | 1.84 |
| Over 0.5 | 87.1% |
| Under 0.5 | 12.9% |
| Over 1.5 | 53.6% |
| Under 1.5 | 46.4% |
| Over 2.5 | 28.8% |
| Under 2.5 | 71.2% |
| Over 3.5 | 11.3% |
| Under 3.5 | 88.7% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.76% |
| 2 | 0-0 | 12.90% |
| 3 | 0-1 | 12.71% |
| 4 | 1-1 | 10.61% |
| 5 | 2-1 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 43.1% | 59.4% | 1.71 | -26.2% |
| Draw | 26.0% | 21.5% | 4.42 | +15.1% |
| Slavia Praha win | 30.8% | 19.1% | 4.93 | +52.0% |
| Over 2.5 | 28.8% | 60.2% | 1.64 | -52.7% |
| Under 2.5 | 71.2% | 39.8% | 2.46 | +75.1% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
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
| Dc lambda home | 0.7772 |
| Dc lambda away | 1.0675 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 33.9% |
| P btts no | 66.1% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.75 |
| Fair Over 1.5 odds | 1.86 |
| Fair Under 1.5 odds | 2.16 |
| Fair Over 2.5 odds | 3.47 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.87 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.81 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 54.4% |
| Raw p under 3 5 | 88.4% |
| Raw p btts yes | 34.8% |
| P home draw | 69.2% |
| P draw away | 56.9% |
| P home away | 74.0% |
| Raw p home draw | 57.5% |
| Raw p draw away | 73.1% |
| Raw p home away | 69.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.65 |
| Reference draw odds | 4.38 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Market reference over 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market best under 2 5 last update utc | 2026-10-19T16:28:25Z |
| Home probability edge | -16.3% |
| Draw probability edge | +4.6% |
| Away probability edge | +11.7% |
| Over 2.5 probability edge | -31.4% |
| Under 2.5 probability edge | +31.4% |
| Raw edge prob home | -0.3250 |
| Raw ev home | -0.5404 |
| Raw edge prob draw | 0.0910 |
| Raw ev draw | 0.3523 |
| Raw edge prob away | 0.2340 |
| Raw ev away | 1.0965 |
| Market p home draw | 79.6% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-19T16:28:25Z |
| Market reference home draw last update utc | 2026-10-19T16:28:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.6% |
| Market draw away odds | 2.28 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-19T16:28:25Z |
| Market reference draw away last update utc | 2026-10-19T16:28:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.7% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-19T16:28:25Z |
| Market reference home away last update utc | 2026-10-19T16:28:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.28 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-19T16:27:48Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.9% |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.45 |
| Market reference under 3 5 last update utc | 2026-10-19T16:28:27Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 59.9% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-19T16:28:25Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.26 |
| Market reference btts yes last update utc | 2026-10-19T16:28:25Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Liverpool vs Villarreal

The model's most likely 1X2 outcome is **Liverpool win** at **76.4%**. Expected goals are 3.36 for Liverpool and 0.51 for Villarreal (3.86 combined). The most likely exact score is 3-0 at 11.3%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 68.5%; Under 3.5 goals: 50.9%; Double Chance 1X: 90.3%; Double Chance X2: 23.6%; Double Chance 12 (either team wins): 86.1%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 41.5%; BTTS No (at least one team does not score): 58.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 76.4% | 1.31 |
| Draw | 13.9% | 7.18 |
| Villarreal win | 9.7% | 10.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 3.36 |
| Villarreal expected goals | 0.51 |
| Expected total goals | 3.86 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 68.5% |
| Under 2.5 | 31.5% |
| Over 3.5 | 49.1% |
| Under 3.5 | 50.9% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 11.27% |
| 2 | 2-0 | 10.07% |
| 3 | 4-0 | 9.45% |
| 4 | 1-1 | 6.61% |
| 5 | 5-0 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 76.4% | 62.9% | 1.55 | +18.4% |
| Draw | 13.9% | 20.7% | 4.83 | -32.7% |
| Villarreal win | 9.7% | 16.4% | 6.04 | -41.6% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool FC |
| Matched away-team name | Villarreal CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.3554 |
| Dc lambda away | 0.5055 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 41.5% |
| P btts no | 58.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.66 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.17 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.17 |
| Fair Over 3.5 odds | 2.04 |
| Fair Under 3.5 odds | 1.96 |
| Fair Over 4.5 odds | 3.28 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 89.9% |
| Unadjusted draw probability | 7.1% |
| Unadjusted away-win probability | 3.0% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 46.1% |
| Raw p btts yes | 38.1% |
| P home draw | 90.3% |
| P draw away | 23.6% |
| P home away | 86.1% |
| Raw p home draw | 97.0% |
| Raw p draw away | 10.1% |
| Raw p home away | 92.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.56 |
| Reference draw odds | 4.54 |
| Reference away odds | 5.69 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +13.5% |
| Draw probability edge | -6.8% |
| Away probability edge | -6.7% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | 0.2694 |
| Raw ev home | 0.3931 |
| Raw edge prob draw | -0.1355 |
| Raw ev draw | -0.6547 |
| Raw edge prob away | -0.1339 |
| Raw ev away | -0.8204 |
| Market p home draw | 83.5% |
| Market home draw odds | 1.16 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-19T16:28:25Z |
| Market reference home draw last update utc | 2026-10-19T16:28:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 37.1% |
| Market draw away odds | 2.61 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-19T16:28:25Z |
| Market reference draw away last update utc | 2026-10-19T16:28:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.4% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-19T16:28:25Z |
| Market reference home away last update utc | 2026-10-19T16:28:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.16 |
| Market reference dc draw away odds | 2.61 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 86.7% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-19T16:27:48Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 55.4% |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.15 |
| Market reference under 3 5 last update utc | 2026-10-19T16:28:27Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 61.6% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-19T16:28:25Z |
| Market reference btts yes odds | 1.54 |
| Market reference btts yes opposite odds | 2.35 |
| Market reference btts yes last update utc | 2026-10-19T16:28:25Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Manchester City vs AEK Athens

The model's most likely 1X2 outcome is **Manchester City win** at **82.9%**. Expected goals are 1.97 for Manchester City and 0.39 for AEK Athens (2.36 combined). The most likely exact score is 1-0 at 20.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 44.7%; Under 3.5 goals: 77.4%; Double Chance 1X: 95.1%; Double Chance X2: 17.1%; Double Chance 12 (either team wins): 87.8%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 26.0%; BTTS No (at least one team does not score): 74.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 82.9% | 1.21 |
| Draw | 12.2% | 8.21 |
| AEK Athens win | 4.9% | 20.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.97 |
| AEK Athens expected goals | 0.39 |
| Expected total goals | 2.36 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.7% |
| Under 2.5 | 55.3% |
| Over 3.5 | 22.6% |
| Under 3.5 | 77.4% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.66% |
| 2 | 2-0 | 20.01% |
| 3 | 3-0 | 13.17% |
| 4 | 2-1 | 7.81% |
| 5 | 4-0 | 6.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 82.9% | 89.9% | 1.11 | -8.0% |
| Draw | 12.2% | 6.9% | 12.80 | +55.8% |
| AEK Athens win | 4.9% | 3.2% | 27.00 | +32.9% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
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
| Dc lambda away | 0.3904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 26.0% |
| P btts no | 74.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.85 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.42 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.14 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 75.9% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 6.7% |
| Raw p over 1 5 | 68.0% |
| Raw p under 3 5 | 78.6% |
| Raw p btts yes | 27.5% |
| P home draw | 95.1% |
| P draw away | 17.1% |
| P home away | 87.8% |
| Raw p home draw | 93.3% |
| Raw p draw away | 24.1% |
| Raw p home away | 82.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.10 |
| Reference draw odds | 10.99 |
| Reference away odds | 22.14 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -7.0% |
| Draw probability edge | +5.3% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -33.1% |
| Under 2.5 probability edge | +33.1% |
| Raw edge prob home | -0.1404 |
| Raw ev home | -0.1577 |
| Raw edge prob draw | 0.1052 |
| Raw ev draw | 1.2319 |
| Raw edge prob away | 0.0351 |
| Raw ev away | 0.8039 |
| Market p home draw | 95.8% |
| Market home draw odds | 1.01 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-19T16:28:25Z |
| Market reference home draw last update utc | 2026-10-19T16:28:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 12.1% |
| Market draw away odds | 8.00 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-19T16:28:25Z |
| Market reference draw away last update utc | 2026-10-19T16:28:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 92.1% |
| Market home away odds | 1.05 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-19T16:28:25Z |
| Market reference home away last update utc | 2026-10-19T16:28:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.01 |
| Market reference dc draw away odds | 8.00 |
| Market reference dc home away odds | 1.05 |
| Market p over 1 5 | 92.4% |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 6.60 |
| Market reference over 1 5 last update utc | 2026-10-19T16:27:48Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 41.9% |
| Market reference under 3 5 odds | 2.25 |
| Market reference under 3 5 opposite odds | 1.66 |
| Market reference under 3 5 last update utc | 2026-10-19T16:28:27Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 42.8% |
| Market btts yes odds | 2.14 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-19T16:28:25Z |
| Market reference btts yes odds | 2.14 |
| Market reference btts yes opposite odds | 1.65 |
| Market reference btts yes last update utc | 2026-10-19T16:28:25Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Napoli vs Bodø/Glimt

The model's most likely 1X2 outcome is **Napoli win** at **43.0%**. Expected goals are 1.17 for Napoli and 1.78 for Bodø/Glimt (2.94 combined). The most likely exact score is 1-0 at 11.3%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 55.7%; Under 3.5 goals: 67.3%; Double Chance 1X: 64.5%; Double Chance X2: 57.0%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 56.9%; BTTS No (at least one team does not score): 43.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 43.0% | 2.32 |
| Draw | 21.5% | 4.66 |
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
| 1 | 1-0 | 11.27% |
| 2 | 2-1 | 10.73% |
| 3 | 1-1 | 10.02% |
| 4 | 0-1 | 6.73% |
| 5 | 1-2 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 43.0% | 60.5% | 1.64 | -29.4% |
| Draw | 21.5% | 20.7% | 4.67 | +0.3% |
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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
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
| Dc lambda away | 1.7783 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 56.9% |
| P btts no | 43.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.94 |
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
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.62 |
| Reference draw odds | 4.54 |
| Reference away odds | 5.00 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -17.5% |
| Draw probability edge | +0.8% |
| Away probability edge | +16.8% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | -0.3504 |
| Raw ev home | -0.5818 |
| Raw edge prob draw | 0.0151 |
| Raw ev draw | 0.0382 |
| Raw edge prob away | 0.3353 |
| Raw ev away | 1.7074 |
| Market p home draw | 80.8% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-19T16:28:25Z |
| Market reference home draw last update utc | 2026-10-19T16:28:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.4% |
| Market draw away odds | 2.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-19T16:28:25Z |
| Market reference draw away last update utc | 2026-10-19T16:28:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.8% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-19T16:28:25Z |
| Market reference home away last update utc | 2026-10-19T16:28:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.40 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 86.0% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-19T16:27:48Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 56.6% |
| Market reference under 3 5 odds | 1.71 |
| Market reference under 3 5 opposite odds | 2.20 |
| Market reference under 3 5 last update utc | 2026-10-19T16:28:27Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 62.0% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-19T16:28:25Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.37 |
| Market reference btts yes last update utc | 2026-10-19T16:28:25Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Paris Saint Germain vs Barcelona

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **55.2%**. Expected goals are 3.22 for Paris Saint Germain and 1.52 for Barcelona (4.75 combined). The most likely exact score is 2-2 at 6.7%. Goal-market probabilities: at least one goal: 99.2%; Over 2.5 goals: 83.6%; Under 3.5 goals: 32.3%; Double Chance 1X: 72.9%; Double Chance X2: 44.8%; Double Chance 12 (either team wins): 82.4%; Under 4.5 goals: 51.0%; BTTS Yes (both teams score): 76.7%; BTTS No (at least one team does not score): 23.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 55.2% | 1.81 |
| Draw | 17.6% | 5.67 |
| Barcelona win | 27.1% | 3.69 |

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
| Over 3.5 | 67.7% |
| Under 3.5 | 32.3% |
| Over 4.5 | 49.0% |
| Under 4.5 | 51.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.65% |
| 2 | 1-2 | 5.83% |
| 3 | 3-1 | 5.74% |
| 4 | 2-1 | 5.35% |
| 5 | 1-1 | 5.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 55.2% | 39.5% | 2.48 | +37.0% |
| Draw | 17.6% | 21.4% | 4.82 | -15.0% |
| Barcelona win | 27.1% | 39.1% | 2.48 | -32.7% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris Saint-Germain FC |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.2228 |
| Dc lambda away | 1.5229 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 76.7% |
| P btts no | 23.3% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 119.95 |
| Fair Over 1.5 odds | 1.06 |
| Fair Under 1.5 odds | 16.85 |
| Fair Over 2.5 odds | 1.20 |
| Fair Under 2.5 odds | 6.10 |
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
| P home draw | 72.9% |
| P draw away | 44.8% |
| P home away | 82.4% |
| Raw p home draw | 84.9% |
| Raw p draw away | 29.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.46 |
| Reference draw odds | 4.45 |
| Reference away odds | 2.48 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.15 |
| Reference Under 2.5 odds | 5.00 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +15.8% |
| Draw probability edge | -3.8% |
| Away probability edge | -12.0% |
| Over 2.5 probability edge | -1.3% |
| Under 2.5 probability edge | +1.3% |
| Raw edge prob home | 0.3155 |
| Raw ev home | 0.7612 |
| Raw edge prob draw | -0.0753 |
| Raw ev draw | -0.3316 |
| Raw edge prob away | -0.2402 |
| Raw ev away | -0.6251 |
| Market p home draw | 60.2% |
| Market home draw odds | 1.61 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-19T16:28:25Z |
| Market reference home draw last update utc | 2026-10-19T16:28:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.2% |
| Market draw away odds | 1.61 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-19T16:28:25Z |
| Market reference draw away last update utc | 2026-10-19T16:28:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.5% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-19T16:28:25Z |
| Market reference home away last update utc | 2026-10-19T16:28:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.61 |
| Market reference dc draw away odds | 1.61 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 95.5% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-19T16:28:24Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 14.50 |
| Market reference over 1 5 last update utc | 2026-10-19T16:28:24Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 33.0% |
| Market under 3 5 odds | 2.70 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-19T16:28:24Z |
| Market reference under 3 5 odds | 2.80 |
| Market reference under 3 5 opposite odds | 1.45 |
| Market reference under 3 5 last update utc | 2026-10-19T16:28:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 84.7% |
| Market btts yes odds | 1.15 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-19T16:28:25Z |
| Market reference btts yes odds | 1.15 |
| Market reference btts yes opposite odds | 4.82 |
| Market reference btts yes last update utc | 2026-10-19T16:28:25Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Porto vs PSV Eindhoven

The model's most likely 1X2 outcome is **Porto win** at **60.4%**. Expected goals are 2.11 for Porto and 1.17 for PSV Eindhoven (3.28 combined). The most likely exact score is 2-1 at 10.0%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.4%; Double Chance 1X: 80.5%; Double Chance X2: 39.6%; Double Chance 12 (either team wins): 80.0%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 60.1%; BTTS No (at least one team does not score): 39.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 60.4% | 1.65 |
| Draw | 20.0% | 4.99 |
| PSV Eindhoven win | 19.5% | 5.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Porto expected goals | 2.11 |
| PSV Eindhoven expected goals | 1.17 |
| Expected total goals | 3.28 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 83.5% |
| Under 1.5 | 16.5% |
| Over 2.5 | 63.6% |
| Under 2.5 | 36.4% |
| Over 3.5 | 41.6% |
| Under 3.5 | 58.4% |
| Over 4.5 | 23.4% |
| Under 4.5 | 76.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.96% |
| 2 | 1-1 | 8.98% |
| 3 | 1-0 | 8.56% |
| 4 | 2-0 | 8.54% |
| 5 | 3-1 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 60.4% | 61.4% | 1.63 | -1.5% |
| Draw | 20.0% | 20.4% | 4.77 | -4.5% |
| PSV Eindhoven win | 19.5% | 18.2% | 5.18 | +1.2% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Porto |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1113 |
| Dc lambda away | 1.1671 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.1% |
| P btts no | 39.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.74 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.07 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.40 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.28 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 59.5% |
| Unadjusted draw probability | 19.7% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 60.1% |
| P home draw | 80.5% |
| P draw away | 39.6% |
| P home away | 80.0% |
| Raw p home draw | 79.2% |
| Raw p draw away | 40.5% |
| Raw p home away | 80.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.60 |
| Reference draw odds | 4.63 |
| Reference away odds | 5.15 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -1.0% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.0192 |
| Raw ev home | -0.0306 |
| Raw edge prob draw | -0.0069 |
| Raw ev draw | -0.0612 |
| Raw edge prob away | 0.0261 |
| Raw ev away | 0.0800 |
| Market p home draw | 80.9% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-19T16:28:25Z |
| Market reference home draw last update utc | 2026-10-19T16:28:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.1% |
| Market draw away odds | 2.42 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-19T16:28:25Z |
| Market reference draw away last update utc | 2026-10-19T16:28:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.9% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-19T16:28:25Z |
| Market reference home away last update utc | 2026-10-19T16:28:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.42 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 85.1% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-19T16:27:48Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.7% |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.25 |
| Market reference under 3 5 last update utc | 2026-10-19T16:28:27Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 60.7% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-19T16:28:25Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-19T16:28:25Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Sabah FK vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **75.6%**. Expected goals are 0.75 for Sabah FK and 2.47 for Borussia Dortmund (3.23 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 62.7%; Under 3.5 goals: 59.6%; Double Chance 1X: 24.4%; Double Chance X2: 90.4%; Double Chance 12 (either team wins): 85.2%; Under 4.5 goals: 77.5%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 9.6% | 10.40 |
| Draw | 14.8% | 6.77 |
| Borussia Dortmund win | 75.6% | 1.32 |

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
| Over 2.5 | 62.7% |
| Under 2.5 | 37.3% |
| Over 3.5 | 40.4% |
| Under 3.5 | 59.6% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.15% |
| 2 | 0-1 | 10.19% |
| 3 | 0-3 | 10.02% |
| 4 | 1-2 | 9.17% |
| 5 | 1-3 | 7.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 9.6% | 9.5% | 10.40 | -0.0% |
| Draw | 14.8% | 14.7% | 6.40 | -5.5% |
| Borussia Dortmund win | 75.6% | 75.8% | 1.31 | -0.9% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7547 |
| Dc lambda away | 2.4747 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.06 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.85 |
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
| Raw p btts yes | 48.2% |
| P home draw | 24.4% |
| P draw away | 90.4% |
| P home away | 85.2% |
| Raw p home draw | 24.6% |
| Raw p draw away | 90.3% |
| Raw p home away | 85.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 9.29 |
| Reference draw odds | 6.17 |
| Reference away odds | 1.30 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +0.1% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -8.2% |
| Under 2.5 probability edge | +8.2% |
| Raw edge prob home | 0.0019 |
| Raw ev home | 0.0099 |
| Raw edge prob draw | 0.0021 |
| Raw ev draw | -0.0484 |
| Raw edge prob away | -0.0040 |
| Raw ev away | -0.0120 |
| Market p home draw | 25.4% |
| Market home draw odds | 3.80 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-19T16:28:25Z |
| Market reference home draw last update utc | 2026-10-19T16:28:25Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.9% |
| Market draw away odds | 1.06 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-19T16:28:25Z |
| Market reference draw away last update utc | 2026-10-19T16:28:25Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.8% |
| Market home away odds | 1.15 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-19T16:28:25Z |
| Market reference home away last update utc | 2026-10-19T16:28:25Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.80 |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 88.5% |
| Market over 1 5 odds | 1.06 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-19T16:14:43Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-19T16:27:48Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.9% |
| Market under 3 5 odds | 1.87 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-19T16:14:43Z |
| Market reference under 3 5 odds | 1.86 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market reference under 3 5 last update utc | 2026-10-19T16:28:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.9% |
| Market btts yes odds | 1.71 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-19T16:28:25Z |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.04 |
| Market reference btts yes last update utc | 2026-10-19T16:28:25Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — VfB Stuttgart vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **49.8%**. Expected goals are 1.41 for VfB Stuttgart and 2.10 for Atlético Madrid (3.51 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 67.4%; Under 3.5 goals: 53.7%; Double Chance 1X: 50.2%; Double Chance X2: 72.1%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 72.9%; BTTS Yes (both teams score): 66.6%; BTTS No (at least one team does not score): 33.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 27.9% | 3.59 |
| Draw | 22.3% | 4.49 |
| Atlético Madrid win | 49.8% | 2.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 1.41 |
| Atlético Madrid expected goals | 2.10 |
| Expected total goals | 3.51 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 86.0% |
| Under 1.5 | 14.0% |
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.1% |
| Under 4.5 | 72.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.31% |
| 2 | 1-2 | 8.63% |
| 3 | 2-2 | 7.26% |
| 4 | 2-1 | 6.67% |
| 5 | 0-1 | 6.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 27.9% | 29.5% | 3.33 | -7.2% |
| Draw | 22.3% | 24.4% | 3.94 | -12.2% |
| Atlético Madrid win | 49.8% | 46.0% | 2.17 | +8.2% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
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
| Dc lambda away | 2.0953 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 66.6% |
| P btts no | 33.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.49 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.13 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
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
| P home draw | 50.2% |
| P draw away | 72.1% |
| P home away | 77.7% |
| Raw p home draw | 46.3% |
| Raw p draw away | 73.8% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.26 |
| Reference draw odds | 3.92 |
| Reference away odds | 2.12 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -1.7% |
| Draw probability edge | -2.1% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Raw edge prob home | -0.0333 |
| Raw ev home | -0.1275 |
| Raw edge prob draw | -0.0427 |
| Raw ev draw | -0.2062 |
| Raw edge prob away | 0.0760 |
| Raw ev away | 0.1642 |
| Market p home draw | 54.7% |
| Market home draw odds | 1.77 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-19T16:28:25Z |
| Market reference home draw last update utc | 2026-10-19T16:28:31Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.2% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-19T16:28:25Z |
| Market reference draw away last update utc | 2026-10-19T16:28:31Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.1% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-19T16:28:25Z |
| Market reference home away last update utc | 2026-10-19T16:28:31Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.77 |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 88.3% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-19T16:28:02Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.15 |
| Market reference over 1 5 last update utc | 2026-10-19T16:28:02Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.4% |
| Market under 3 5 odds | 1.73 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-19T16:28:02Z |
| Market reference under 3 5 odds | 1.72 |
| Market reference under 3 5 opposite odds | 2.19 |
| Market reference under 3 5 last update utc | 2026-10-19T16:28:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.9% |
| Market btts yes odds | 1.42 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-19T16:28:25Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.92 |
| Market reference btts yes last update utc | 2026-10-19T16:28:31Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **82.6%**. Expected goals are 4.01 for Aston Villa and 1.16 for Viking FK (5.17 combined). The most likely exact score is 4-1 at 6.8%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.1%; Under 3.5 goals: 24.7%; Double Chance 1X: 93.3%; Double Chance X2: 17.4%; Double Chance 12 (either team wins): 89.3%; Under 4.5 goals: 42.2%; BTTS Yes (both teams score): 68.2%; BTTS No (at least one team does not score): 31.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 82.6% | 1.21 |
| Draw | 10.7% | 9.32 |
| Viking FK win | 6.7% | 14.95 |

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
| Over 2.5 | 88.1% |
| Under 2.5 | 11.9% |
| Over 3.5 | 75.3% |
| Under 3.5 | 24.7% |
| Over 4.5 | 57.8% |
| Under 4.5 | 42.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-1 | 6.85% |
| 2 | 3-1 | 6.84% |
| 3 | 4-0 | 5.88% |
| 4 | 3-0 | 5.88% |
| 5 | 5-1 | 5.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 82.6% | 79.5% | 1.29 | +6.5% |
| Draw | 10.7% | 13.3% | 6.31 | -32.3% |
| Viking FK win | 6.7% | 7.2% | 12.60 | -15.7% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.0051 |
| Dc lambda away | 1.1637 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 23 |
| Score grid omitted mass | 0 |
| P btts yes | 68.2% |
| P btts no | 31.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 175.31 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.60 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.42 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.05 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.37 |
| Unadjusted home-win probability | 85.6% |
| Unadjusted draw probability | 8.2% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.2% |
| Raw p btts yes | 67.4% |
| P home draw | 93.3% |
| P draw away | 17.4% |
| P home away | 89.3% |
| Raw p home draw | 93.8% |
| Raw p draw away | 14.4% |
| Raw p home away | 91.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.24 |
| Reference draw odds | 6.67 |
| Reference away odds | 11.80 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +3.1% |
| Draw probability edge | -2.5% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +13.9% |
| Under 2.5 probability edge | -13.9% |
| Raw edge prob home | 0.0611 |
| Raw ev home | 0.1046 |
| Raw edge prob draw | -0.0504 |
| Raw ev draw | -0.4817 |
| Raw edge prob away | -0.0106 |
| Raw ev away | -0.2245 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Bayern Munich win** at **38.7%**. Expected goals are 1.02 for Bayern Munich and 1.31 for Arsenal (2.33 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.6%; Double Chance 1X: 63.9%; Double Chance X2: 61.3%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 45.7%; BTTS No (at least one team does not score): 54.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 38.7% | 2.58 |
| Draw | 25.2% | 3.97 |
| Arsenal win | 36.1% | 2.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 1.02 |
| Arsenal expected goals | 1.31 |
| Expected total goals | 2.33 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
| Over 3.5 | 20.4% |
| Under 3.5 | 79.6% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.83% |
| 2 | 1-1 | 11.74% |
| 3 | 0-1 | 11.03% |
| 4 | 2-1 | 8.66% |
| 5 | 0-0 | 8.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 38.7% | 47.8% | 2.14 | -17.1% |
| Draw | 25.2% | 23.9% | 3.96 | -0.3% |
| Arsenal win | 36.1% | 28.3% | 3.39 | +22.4% |
| Over 2.5 | 41.3% | 60.0% | 1.65 | -31.9% |
| Under 2.5 | 58.7% | 40.0% | 2.45 | +43.9% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
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
| Dc lambda away | 1.3101 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 45.7% |
| P btts no | 54.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.57 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.98 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.91 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.50 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 29.6% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 43.9% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 79.4% |
| Raw p btts yes | 46.0% |
| P home draw | 63.9% |
| P draw away | 61.3% |
| P home away | 74.8% |
| Raw p home draw | 56.1% |
| Raw p draw away | 70.4% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.04 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.39 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market best under 2 5 last update utc | 2026-10-19T16:28:25Z |
| Home probability edge | -9.1% |
| Draw probability edge | +1.3% |
| Away probability edge | +7.8% |
| Over 2.5 probability edge | -18.7% |
| Under 2.5 probability edge | +18.7% |
| Raw edge prob home | -0.1823 |
| Raw ev home | -0.3662 |
| Raw edge prob draw | 0.0263 |
| Raw ev draw | 0.0487 |
| Raw edge prob away | 0.1560 |
| Raw ev away | 0.4883 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **60.3%**. Expected goals are 3.05 for Club Brugge and 1.27 for RC Lens (4.32 combined). The most likely exact score is 2-2 at 6.8%. Goal-market probabilities: at least one goal: 98.5%; Over 2.5 goals: 78.4%; Under 3.5 goals: 39.2%; Double Chance 1X: 79.0%; Double Chance X2: 39.7%; Double Chance 12 (either team wins): 81.3%; Under 4.5 goals: 59.0%; BTTS Yes (both teams score): 70.5%; BTTS No (at least one team does not score): 29.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 60.3% | 1.66 |
| Draw | 18.7% | 5.35 |
| RC Lens win | 21.0% | 4.77 |

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
| Over 2.5 | 78.4% |
| Under 2.5 | 21.6% |
| Over 3.5 | 60.8% |
| Under 3.5 | 39.2% |
| Over 4.5 | 41.0% |
| Under 4.5 | 59.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.80% |
| 2 | 1-1 | 6.66% |
| 3 | 3-1 | 6.57% |
| 4 | 2-1 | 6.46% |
| 5 | 1-2 | 5.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 60.3% | 47.4% | 2.12 | +27.9% |
| Draw | 18.7% | 23.6% | 4.03 | -24.7% |
| RC Lens win | 21.0% | 29.0% | 3.39 | -28.9% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Club Brugge KV |
| Matched away-team name | Racing Club de Lens |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.0512 |
| Dc lambda away | 1.2726 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 70.5% |
| P btts no | 29.5% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 68.78 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.30 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.63 |
| Fair Over 3.5 odds | 1.65 |
| Fair Under 3.5 odds | 2.55 |
| Fair Over 4.5 odds | 2.44 |
| Fair Under 4.5 odds | 1.69 |
| Unadjusted home-win probability | 73.3% |
| Unadjusted draw probability | 13.7% |
| Unadjusted away-win probability | 13.0% |
| Raw p over 1 5 | 92.7% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 68.3% |
| P home draw | 79.0% |
| P draw away | 39.7% |
| P home away | 81.3% |
| Raw p home draw | 87.0% |
| Raw p draw away | 26.7% |
| Raw p home away | 86.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.06 |
| Reference draw odds | 4.04 |
| Reference away odds | 3.32 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.60 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +12.9% |
| Draw probability edge | -5.0% |
| Away probability edge | -8.0% |
| Over 2.5 probability edge | +13.9% |
| Under 2.5 probability edge | -13.9% |
| Raw edge prob home | 0.2587 |
| Raw ev home | 0.5533 |
| Raw edge prob draw | -0.0992 |
| Raw ev draw | -0.4472 |
| Raw edge prob away | -0.1594 |
| Raw ev away | -0.5589 |

</details>


---

## 2026-10-21 — Como vs Manchester United

The model's most likely 1X2 outcome is **Como win** at **51.2%**. Expected goals are 2.99 for Como and 1.94 for Manchester United (4.93 combined). The most likely exact score is 2-2 at 7.7%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 86.0%; Under 3.5 goals: 27.9%; Double Chance 1X: 71.8%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 46.6%; BTTS Yes (both teams score): 82.2%; BTTS No (at least one team does not score): 17.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 51.2% | 1.95 |
| Draw | 20.7% | 4.84 |
| Manchester United win | 28.2% | 3.55 |

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
| 1 | 2-2 | 7.70% |
| 2 | 2-1 | 5.37% |
| 3 | 3-1 | 5.35% |
| 4 | 3-2 | 5.20% |
| 5 | 1-1 | 5.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 51.2% | 42.7% | 2.29 | +17.2% |
| Draw | 20.7% | 25.0% | 3.90 | -19.5% |
| Manchester United win | 28.2% | 32.3% | 3.10 | -12.7% |
| Over 2.5 | 86.0% | 58.8% | 1.68 | +44.6% |
| Under 2.5 | 14.0% | 41.2% | 2.38 | -66.8% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
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
| Dc lambda home | 2.9911 |
| Dc lambda away | 1.9422 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 82.2% |
| P btts no | 17.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 154.43 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 21.93 |
| Fair Over 2.5 odds | 1.16 |
| Fair Under 2.5 odds | 7.17 |
| Fair Over 3.5 odds | 1.39 |
| Fair Under 3.5 odds | 3.59 |
| Fair Over 4.5 odds | 1.87 |
| Fair Under 4.5 odds | 2.15 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 95.5% |
| Raw p under 3 5 | 27.5% |
| Raw p btts yes | 81.1% |
| P home draw | 71.8% |
| P draw away | 48.8% |
| P home away | 79.3% |
| Raw p home draw | 76.0% |
| Raw p draw away | 40.3% |
| Raw p home away | 83.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.28 |
| Reference draw odds | 3.83 |
| Reference away odds | 2.99 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market best under 2 5 last update utc | 2026-10-19T16:28:25Z |
| Home probability edge | +8.5% |
| Draw probability edge | -4.4% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | +27.2% |
| Under 2.5 probability edge | -27.2% |
| Raw edge prob home | 0.1694 |
| Raw ev home | 0.3660 |
| Raw edge prob draw | -0.0870 |
| Raw ev draw | -0.3643 |
| Raw edge prob away | -0.0824 |
| Raw ev away | -0.2545 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **73.5%**. Expected goals are 2.05 for Inter Milan and 0.92 for Shakhtar Donetsk (2.97 combined). The most likely exact score is 1-0 at 12.6%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 59.2%; Under 3.5 goals: 64.2%; Double Chance 1X: 88.6%; Double Chance X2: 26.5%; Double Chance 12 (either team wins): 84.9%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 73.5% | 1.36 |
| Draw | 15.1% | 6.63 |
| Shakhtar Donetsk win | 11.4% | 8.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.05 |
| Shakhtar Donetsk expected goals | 0.92 |
| Expected total goals | 2.97 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 80.2% |
| Under 1.5 | 19.8% |
| Over 2.5 | 59.2% |
| Under 2.5 | 40.8% |
| Over 3.5 | 35.8% |
| Under 3.5 | 64.2% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.61% |
| 2 | 2-0 | 12.36% |
| 3 | 2-1 | 11.39% |
| 4 | 3-0 | 8.45% |
| 5 | 3-1 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 73.5% | 83.0% | 1.22 | -10.3% |
| Draw | 15.1% | 10.7% | 8.25 | +24.5% |
| Shakhtar Donetsk win | 11.4% | 6.3% | 13.90 | +58.6% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
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
| Dc lambda away | 0.9213 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.85 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.05 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 64.0% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 16.5% |
| Raw p over 1 5 | 79.2% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 52.0% |
| P home draw | 88.6% |
| P draw away | 26.5% |
| P home away | 84.9% |
| Raw p home draw | 83.5% |
| Raw p draw away | 36.0% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.19 |
| Reference draw odds | 8.05 |
| Reference away odds | 13.21 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.50 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -9.5% |
| Draw probability edge | +4.4% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -15.7% |
| Under 2.5 probability edge | +15.7% |
| Raw edge prob home | -0.1899 |
| Raw ev home | -0.2191 |
| Raw edge prob draw | 0.0877 |
| Raw ev draw | 0.6065 |
| Raw edge prob away | 0.1022 |
| Raw ev away | 1.2966 |

</details>


---

## 2026-10-21 — Lille vs Galatasaray

The model's most likely 1X2 outcome is **Lille win** at **57.7%**. Expected goals are 2.57 for Lille and 1.04 for Galatasaray (3.61 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.2%; Under 3.5 goals: 53.5%; Double Chance 1X: 78.3%; Double Chance X2: 42.3%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 72.6%; BTTS Yes (both teams score): 61.4%; BTTS No (at least one team does not score): 38.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 57.7% | 1.73 |
| Draw | 20.6% | 4.85 |
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
| Over 2.5 | 67.2% |
| Under 2.5 | 32.8% |
| Over 3.5 | 46.5% |
| Under 3.5 | 53.5% |
| Over 4.5 | 27.4% |
| Under 4.5 | 72.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.01% |
| 2 | 2-1 | 7.57% |
| 3 | 2-0 | 7.30% |
| 4 | 3-1 | 6.49% |
| 5 | 2-2 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 57.7% | 44.6% | 2.23 | +28.6% |
| Draw | 20.6% | 25.5% | 3.84 | -20.8% |
| Galatasaray win | 21.7% | 29.9% | 3.27 | -29.0% |
| Over 2.5 | 67.2% | 59.3% | 1.67 | +12.2% |
| Under 2.5 | 32.8% | 40.7% | 2.41 | -20.9% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
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
| Dc lambda away | 1.0367 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 61.4% |
| P btts no | 38.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.40 |
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
| P home draw | 78.3% |
| P draw away | 42.3% |
| P home away | 79.4% |
| Raw p home draw | 86.5% |
| Raw p draw away | 29.2% |
| Raw p home away | 84.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.19 |
| Reference draw odds | 3.76 |
| Reference away odds | 3.22 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.41 |
| Market reference over 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:28:25Z |
| Market best under 2 5 last update utc | 2026-10-19T16:28:25Z |
| Home probability edge | +13.1% |
| Draw probability edge | -4.9% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | +7.9% |
| Under 2.5 probability edge | -7.9% |
| Raw edge prob home | 0.2621 |
| Raw ev home | 0.5780 |
| Raw edge prob draw | -0.0978 |
| Raw ev draw | -0.3957 |
| Raw edge prob away | -0.1643 |
| Raw ev away | -0.5585 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **76.5%**. Expected goals are 5.75 for Real Betis and 1.65 for Feyenoord (7.40 combined). The most likely exact score is 5-1 at 4.4%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.7%; Under 3.5 goals: 7.9%; Double Chance 1X: 88.8%; Double Chance X2: 23.5%; Double Chance 12 (either team wins): 87.7%; Under 4.5 goals: 17.4%; BTTS Yes (both teams score): 83.0%; BTTS No (at least one team does not score): 17.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 76.5% | 1.31 |
| Draw | 12.3% | 8.11 |
| Feyenoord win | 11.2% | 8.92 |

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
| Over 4.5 | 82.6% |
| Under 4.5 | 17.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-1 | 4.42% |
| 2 | 6-1 | 4.24% |
| 3 | 4-1 | 3.84% |
| 4 | 3-3 | 3.80% |
| 5 | 5-2 | 3.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 76.5% | 61.4% | 1.61 | +23.1% |
| Draw | 12.3% | 20.0% | 4.88 | -39.9% |
| Feyenoord win | 11.2% | 18.7% | 5.24 | -41.3% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 5.7521 |
| Dc lambda away | 1.6459 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 27 |
| Score grid omitted mass | 0 |
| P btts yes | 83.0% |
| P btts no | 17.0% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1177.74 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 126.63 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 30.00 |
| Fair Over 3.5 odds | 1.09 |
| Fair Under 3.5 odds | 12.65 |
| Fair Over 4.5 odds | 1.21 |
| Fair Under 4.5 odds | 5.76 |
| Unadjusted home-win probability | 91.6% |
| Unadjusted draw probability | 4.7% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.3% |
| Raw p btts yes | 80.4% |
| P home draw | 88.8% |
| P draw away | 23.5% |
| P home away | 87.7% |
| Raw p home draw | 96.2% |
| Raw p draw away | 8.4% |
| Raw p home away | 95.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.60 |
| Reference draw odds | 4.72 |
| Reference away odds | 5.04 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +15.1% |
| Draw probability edge | -7.6% |
| Away probability edge | -7.4% |
| Over 2.5 probability edge | +25.8% |
| Under 2.5 probability edge | -25.8% |
| Raw edge prob home | 0.3017 |
| Raw ev home | 0.4740 |
| Raw edge prob draw | -0.1528 |
| Raw ev draw | -0.7716 |
| Raw edge prob away | -0.1488 |
| Raw ev away | -0.8027 |

</details>


---

## 2026-10-21 — Real Madrid vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid win** at **78.5%**. Expected goals are 2.80 for Real Madrid and 0.88 for RB Leipzig (3.68 combined). The most likely exact score is 2-0 at 10.0%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 71.4%; Under 3.5 goals: 49.7%; Double Chance 1X: 91.0%; Double Chance X2: 21.5%; Double Chance 12 (either team wins): 87.5%; Under 4.5 goals: 68.9%; BTTS Yes (both teams score): 54.3%; BTTS No (at least one team does not score): 45.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 78.5% | 1.27 |
| Draw | 12.5% | 7.97 |
| RB Leipzig win | 9.0% | 11.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.80 |
| RB Leipzig expected goals | 0.88 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 88.0% |
| Under 1.5 | 12.0% |
| Over 2.5 | 71.4% |
| Under 2.5 | 28.6% |
| Over 3.5 | 50.3% |
| Under 3.5 | 49.7% |
| Over 4.5 | 31.1% |
| Under 4.5 | 68.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.03% |
| 2 | 3-0 | 9.37% |
| 3 | 2-1 | 8.80% |
| 4 | 3-1 | 8.22% |
| 5 | 1-0 | 7.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 78.5% | 79.4% | 1.29 | +1.2% |
| Draw | 12.5% | 11.9% | 7.15 | -10.3% |
| RB Leipzig win | 9.0% | 8.7% | 10.20 | -8.4% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8015 |
| Dc lambda away | 0.8770 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 54.3% |
| P btts no | 45.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 47.29 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.31 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.49 |
| Fair Over 3.5 odds | 1.99 |
| Fair Under 3.5 odds | 2.01 |
| Fair Over 4.5 odds | 3.22 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 77.6% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 9.3% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 49.9% |
| Raw p btts yes | 54.5% |
| P home draw | 91.0% |
| P draw away | 21.5% |
| P home away | 87.5% |
| Raw p home draw | 90.7% |
| Raw p draw away | 22.4% |
| Raw p home away | 86.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.24 |
| Reference draw odds | 7.26 |
| Reference away odds | 9.80 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.20 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | -0.9% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -8.6% |
| Under 2.5 probability edge | +8.6% |
| Raw edge prob home | -0.0185 |
| Raw ev home | 0.0005 |
| Raw edge prob draw | 0.0120 |
| Raw ev draw | -0.0604 |
| Raw edge prob away | 0.0065 |
| Raw ev away | -0.0512 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **88.0%**. Expected goals are 6.10 for Sporting Lisbon and 1.31 for LASK (7.41 combined). The most likely exact score is 6-1 at 5.2%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 97.0%; Under 3.5 goals: 7.3%; Double Chance 1X: 95.2%; Double Chance X2: 12.0%; Double Chance 12 (either team wins): 92.8%; Under 4.5 goals: 16.1%; BTTS Yes (both teams score): 74.6%; BTTS No (at least one team does not score): 25.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 88.0% | 1.14 |
| Draw | 7.2% | 13.98 |
| LASK win | 4.8% | 20.82 |

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
| Over 2.5 | 97.0% |
| Under 2.5 | 3.0% |
| Over 3.5 | 92.7% |
| Under 3.5 | 7.3% |
| Over 4.5 | 83.9% |
| Under 4.5 | 16.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 6-1 | 5.24% |
| 2 | 5-1 | 5.16% |
| 3 | 7-1 | 4.57% |
| 4 | 4-1 | 4.23% |
| 5 | 6-0 | 3.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 88.0% | 80.9% | 1.24 | +9.2% |
| Draw | 7.2% | 11.4% | 7.75 | -44.6% |
| LASK win | 4.8% | 7.7% | 12.20 | -41.4% |

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
| Market best home last update utc | 2026-10-19T16:28:25Z |
| Market best draw last update utc | 2026-10-19T16:28:25Z |
| Market best away last update utc | 2026-10-19T16:28:25Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 6.0992 |
| Dc lambda away | 1.3147 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:28:28.687092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 28 |
| Score grid omitted mass | 0 |
| P btts yes | 74.6% |
| P btts no | 25.4% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1136.72 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 140.06 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 33.30 |
| Fair Over 3.5 odds | 1.08 |
| Fair Under 3.5 odds | 13.62 |
| Fair Over 4.5 odds | 1.19 |
| Fair Under 4.5 odds | 6.22 |
| Unadjusted home-win probability | 95.2% |
| Unadjusted draw probability | 2.9% |
| Unadjusted away-win probability | 1.9% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.3% |
| Raw p btts yes | 73.0% |
| P home draw | 95.2% |
| P draw away | 12.0% |
| P home away | 92.8% |
| Raw p home draw | 98.1% |
| Raw p draw away | 4.8% |
| Raw p home away | 97.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.22 |
| Reference draw odds | 7.70 |
| Reference away odds | 11.07 |
| Market reference 1x2 last update utc | 2026-10-19T16:28:27Z |
| Market reference home last update utc | 2026-10-19T16:28:27Z |
| Market reference draw last update utc | 2026-10-19T16:28:27Z |
| Market reference away last update utc | 2026-10-19T16:28:27Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:26Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:26Z |
| Home probability edge | +7.1% |
| Draw probability edge | -4.2% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | +23.9% |
| Under 2.5 probability edge | -23.9% |
| Raw edge prob home | 0.1427 |
| Raw ev home | 0.1802 |
| Raw edge prob draw | -0.0843 |
| Raw ev draw | -0.7725 |
| Raw edge prob away | -0.0584 |
| Raw ev away | -0.7700 |

</details>


---
