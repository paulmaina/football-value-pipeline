# UEFA Champions League — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 548 |
| Training data through | 2026-10-20 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 4 |
| Training seasons loaded | ['2023', '2024', '2025', '2026'] |
| Training sha256 | 24e0e7222acdd9df3acd82f4c85a768ad452ba37bfca16f73afb3e4abd24b6fc |
| Training as of utc | 2026-10-21T10:38:44.687090+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 18, 'bbs_added_results': 0, 'bbs_result_conflicts': 18, 'bbs_rows_with_statistics': 11, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 139, 'added_results': 0, 'conflicts': 1, 'unmapped': 78, 'ambiguous': 0, 'excluded_phase': 460, 'statistics_observations': 2, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T10:38:44.687090+00:00', 'observations': 92, 'observations_sha256': '72347b6bcae0e0ce159d7750251ed2c3abbfa07a9b60e23346c26fb208ecc5a8', 'eligible_training_matches': 0, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 13, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 0, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': 'c7d3aae6c4753ebcd1b05154046ade2fa85fdc1bd67957524899113a0bc2bbf9', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 465.987 |
| Base scoring parameter | 0.213 |
| Home-advantage parameter | 0.327 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0029 |
| Training data health | {'completed_matches': 45, 'latest_completed_utc': '2026-10-20T19:00:00+00:00', 'latest_completed_date': '2026-10-20', 'next_fixture_utc': '2026-10-21T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-21T10:38:40.143762+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'f6cc44b4326bf411cae39d63597f271b3c4ce2c69cc1c4359f759ddcc1a9bb83', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0012620355555555554, 'training_end': '2026-10-20', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261021T103844687090Z_4cf81ee986186d5617341fee14439797d6bdaed1db588e40f9e893f88406b7f9.json |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'UNRELIABLE_AUDIT', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **81.1%**. Expected goals are 3.97 for Aston Villa and 1.34 for Viking FK (5.31 combined). The most likely exact score is 3-1 at 6.8%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 89.5%; Under 3.5 goals: 22.6%; Double Chance 1X: 92.5%; Double Chance X2: 18.9%; Double Chance 12 (either team wins): 88.6%; Under 4.5 goals: 39.4%; BTTS Yes (both teams score): 72.9%; BTTS No (at least one team does not score): 27.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 81.1% | 1.23 |
| Draw | 11.4% | 8.79 |
| Viking FK win | 7.5% | 13.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 3.97 |
| Viking FK expected goals | 1.34 |
| Expected total goals | 5.31 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 96.8% |
| Under 1.5 | 3.2% |
| Over 2.5 | 89.5% |
| Under 2.5 | 10.5% |
| Over 3.5 | 77.4% |
| Under 3.5 | 22.6% |
| Over 4.5 | 60.6% |
| Under 4.5 | 39.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 6.77% |
| 2 | 4-1 | 6.71% |
| 3 | 5-1 | 5.33% |
| 4 | 2-1 | 5.12% |
| 5 | 3-0 | 5.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 81.1% | 79.5% | 1.26 | +2.2% |
| Draw | 11.4% | 13.5% | 6.89 | -21.6% |
| Viking FK win | 7.5% | 7.1% | 12.60 | -5.6% |

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
| Market best home last update utc | 2026-10-21T10:38:37Z |
| Market best draw last update utc | 2026-10-21T10:38:37Z |
| Market best away last update utc | 2026-10-21T10:38:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.9679 |
| Dc lambda away | 1.3425 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:44.687090+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 23 |
| Score grid omitted mass | 0 |
| P btts yes | 72.9% |
| P btts no | 27.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 225.55 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 30.82 |
| Fair Over 2.5 odds | 1.12 |
| Fair Under 2.5 odds | 9.49 |
| Fair Over 3.5 odds | 1.29 |
| Fair Under 3.5 odds | 4.43 |
| Fair Over 4.5 odds | 1.65 |
| Fair Under 4.5 odds | 2.54 |
| Unadjusted home-win probability | 82.8% |
| Unadjusted draw probability | 9.3% |
| Unadjusted away-win probability | 7.9% |
| Raw p over 1 5 | 96.8% |
| Raw p under 3 5 | 22.4% |
| Raw p btts yes | 72.4% |
| P home draw | 92.5% |
| P draw away | 18.9% |
| P home away | 88.6% |
| Raw p home draw | 92.1% |
| Raw p draw away | 17.2% |
| Raw p home away | 90.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.24 |
| Reference draw odds | 6.55 |
| Reference away odds | 12.00 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:41Z |
| Market reference home last update utc | 2026-10-21T10:38:41Z |
| Market reference draw last update utc | 2026-10-21T10:38:41Z |
| Market reference away last update utc | 2026-10-21T10:38:41Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.66 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:15Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:15Z |
| Home probability edge | +1.6% |
| Draw probability edge | -2.1% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | +13.7% |
| Under 2.5 probability edge | -13.7% |
| Raw edge prob home | 0.0327 |
| Raw ev home | 0.0428 |
| Raw edge prob draw | -0.0415 |
| Raw ev draw | -0.3590 |
| Raw edge prob away | 0.0088 |
| Raw ev away | -0.0003 |
| Market p home draw | 92.0% |
| Market home draw odds | 1.07 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T10:38:28Z |
| Market reference home draw last update utc | 2026-10-21T10:38:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.5% |
| Market draw away odds | 4.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-21T10:38:37Z |
| Market reference draw away last update utc | 2026-10-21T10:38:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 85.5% |
| Market home away odds | 1.14 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-21T10:38:37Z |
| Market reference home away last update utc | 2026-10-21T10:38:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.04 |
| Market reference dc draw away odds | 4.25 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 91.4% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 6.40 |
| Market reference over 1 5 last update utc | 2026-10-21T10:38:36Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 45.1% |
| Market under 3 5 odds | 2.12 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market reference under 3 5 odds | 2.12 |
| Market reference under 3 5 opposite odds | 1.76 |
| Market reference under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.1% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T10:38:28Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.13 |
| Market reference btts yes last update utc | 2026-10-21T10:38:37Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Bayern Munich win** at **37.2%**. Expected goals are 1.01 for Bayern Munich and 1.21 for Arsenal (2.22 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 38.6%; Under 3.5 goals: 81.6%; Double Chance 1X: 63.4%; Double Chance X2: 62.8%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 43.8%; BTTS No (at least one team does not score): 56.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 37.2% | 2.69 |
| Draw | 26.2% | 3.81 |
| Arsenal win | 36.6% | 2.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 1.01 |
| Arsenal expected goals | 1.21 |
| Expected total goals | 2.22 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 64.3% |
| Under 1.5 | 35.7% |
| Over 2.5 | 38.6% |
| Under 2.5 | 61.4% |
| Over 3.5 | 18.4% |
| Under 3.5 | 81.6% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.81% |
| 2 | 0-1 | 12.19% |
| 3 | 1-1 | 12.05% |
| 4 | 0-0 | 9.70% |
| 5 | 2-1 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 37.2% | 43.2% | 2.30 | -14.4% |
| Draw | 26.2% | 25.0% | 3.90 | +2.2% |
| Arsenal win | 36.6% | 31.8% | 3.09 | +13.0% |
| Over 2.5 | 38.6% | 60.3% | 1.64 | -36.7% |
| Under 2.5 | 61.4% | 39.7% | 2.47 | +51.6% |

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
| Market best home last update utc | 2026-10-21T10:38:37Z |
| Market best draw last update utc | 2026-10-21T10:38:37Z |
| Market best away last update utc | 2026-10-21T10:38:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Bayern München |
| Matched away-team name | Arsenal FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0114 |
| Dc lambda away | 1.2129 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:44.687090+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.8% |
| P btts no | 56.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.30 |
| Fair Over 1.5 odds | 1.56 |
| Fair Under 1.5 odds | 2.80 |
| Fair Over 2.5 odds | 2.59 |
| Fair Under 2.5 odds | 1.63 |
| Fair Over 3.5 odds | 5.42 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.24 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 41.3% |
| Raw p over 1 5 | 64.5% |
| Raw p under 3 5 | 81.5% |
| Raw p btts yes | 44.0% |
| P home draw | 63.4% |
| P draw away | 62.8% |
| P home away | 73.8% |
| Raw p home draw | 58.7% |
| Raw p draw away | 68.8% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.26 |
| Reference draw odds | 3.84 |
| Reference away odds | 3.04 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:41Z |
| Market reference home last update utc | 2026-10-21T10:38:41Z |
| Market reference draw last update utc | 2026-10-21T10:38:41Z |
| Market reference away last update utc | 2026-10-21T10:38:41Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.47 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:37Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:37Z |
| Market best over 2 5 last update utc | 2026-10-21T10:38:37Z |
| Market best under 2 5 last update utc | 2026-10-21T10:38:37Z |
| Home probability edge | -6.0% |
| Draw probability edge | +1.2% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -21.7% |
| Under 2.5 probability edge | +21.7% |
| Raw edge prob home | -0.1193 |
| Raw ev home | -0.2813 |
| Raw edge prob draw | 0.0241 |
| Raw ev draw | 0.0694 |
| Raw edge prob away | 0.0952 |
| Raw ev away | 0.2771 |
| Market p home draw | 68.0% |
| Market home draw odds | 1.43 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T10:38:28Z |
| Market reference home draw last update utc | 2026-10-21T10:38:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.1% |
| Market draw away odds | 1.69 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-21T10:38:37Z |
| Market reference draw away last update utc | 2026-10-21T10:38:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.9% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-21T10:38:37Z |
| Market reference home away last update utc | 2026-10-21T10:38:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.42 |
| Market reference dc draw away odds | 1.69 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-21T10:35:34Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-21T10:38:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.0% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-21T10:35:34Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.28 |
| Market reference under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 64.3% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T10:38:28Z |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-21T10:38:37Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **69.1%**. Expected goals are 4.47 for Club Brugge and 1.36 for RC Lens (5.82 combined). The most likely exact score is 2-2 at 5.4%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 90.6%; Under 3.5 goals: 19.8%; Double Chance 1X: 83.9%; Double Chance X2: 30.9%; Double Chance 12 (either team wins): 85.3%; Under 4.5 goals: 35.5%; BTTS Yes (both teams score): 76.6%; BTTS No (at least one team does not score): 23.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 69.1% | 1.45 |
| Draw | 14.7% | 6.80 |
| RC Lens win | 16.1% | 6.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Club Brugge expected goals | 4.47 |
| RC Lens expected goals | 1.36 |
| Expected total goals | 5.82 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.1% |
| Under 1.5 | 2.9% |
| Over 2.5 | 90.6% |
| Under 2.5 | 9.4% |
| Over 3.5 | 80.2% |
| Under 3.5 | 19.8% |
| Over 4.5 | 64.5% |
| Under 4.5 | 35.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 5.44% |
| 2 | 4-1 | 5.30% |
| 3 | 3-1 | 4.75% |
| 4 | 5-1 | 4.74% |
| 5 | 4-0 | 3.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 69.1% | 51.5% | 1.94 | +34.1% |
| Draw | 14.7% | 22.1% | 4.37 | -35.7% |
| RC Lens win | 16.1% | 26.4% | 3.68 | -40.6% |

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
| Market best home last update utc | 2026-10-21T10:38:37Z |
| Market best draw last update utc | 2026-10-21T10:38:37Z |
| Market best away last update utc | 2026-10-21T10:38:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Club Brugge KV |
| Matched away-team name | Racing Club de Lens |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.4680 |
| Dc lambda away | 1.3550 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:44.687090+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 24 |
| Score grid omitted mass | 0 |
| P btts yes | 76.6% |
| P btts no | 23.4% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 241.52 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 34.61 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.63 |
| Fair Over 3.5 odds | 1.25 |
| Fair Under 3.5 odds | 5.06 |
| Fair Over 4.5 odds | 1.55 |
| Fair Under 4.5 odds | 2.82 |
| Unadjusted home-win probability | 86.8% |
| Unadjusted draw probability | 7.3% |
| Unadjusted away-win probability | 5.9% |
| Raw p over 1 5 | 97.9% |
| Raw p under 3 5 | 16.8% |
| Raw p btts yes | 73.3% |
| P home draw | 83.9% |
| P draw away | 30.9% |
| P home away | 85.3% |
| Raw p home draw | 94.1% |
| Raw p draw away | 13.2% |
| Raw p home away | 92.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.89 |
| Reference draw odds | 4.25 |
| Reference away odds | 3.58 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:41Z |
| Market reference home last update utc | 2026-10-21T10:38:41Z |
| Market reference draw last update utc | 2026-10-21T10:38:41Z |
| Market reference away last update utc | 2026-10-21T10:38:41Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.26 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:15Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:15Z |
| Home probability edge | +17.7% |
| Draw probability edge | -7.4% |
| Away probability edge | -10.3% |
| Over 2.5 probability edge | +18.4% |
| Under 2.5 probability edge | -18.4% |
| Raw edge prob home | 0.3534 |
| Raw ev home | 0.6841 |
| Raw edge prob draw | -0.1477 |
| Raw ev draw | -0.6796 |
| Raw edge prob away | -0.2057 |
| Raw ev away | -0.7843 |
| Market p home draw | 73.0% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-21T10:38:37Z |
| Market reference home draw last update utc | 2026-10-21T10:38:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.4% |
| Market draw away odds | 1.97 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-21T10:38:28Z |
| Market reference draw away last update utc | 2026-10-21T10:38:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.7% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-21T10:38:28Z |
| Market reference home away last update utc | 2026-10-21T10:38:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.32 |
| Market reference dc draw away odds | 1.95 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 90.4% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-21T10:38:36Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 48.3% |
| Market under 3 5 odds | 2.00 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market reference under 3 5 odds | 1.89 |
| Market reference under 3 5 opposite odds | 1.78 |
| Market reference under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 72.3% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T10:38:28Z |
| Market reference btts yes odds | 1.33 |
| Market reference btts yes opposite odds | 3.10 |
| Market reference btts yes last update utc | 2026-10-21T10:38:37Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Como vs Manchester United

The model's most likely 1X2 outcome is **Como win** at **43.7%**. Expected goals are 2.25 for Como and 2.04 for Manchester United (4.29 combined). The most likely exact score is 2-2 at 8.2%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 79.6%; Under 3.5 goals: 37.9%; Double Chance 1X: 65.5%; Double Chance X2: 56.3%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 57.8%; BTTS Yes (both teams score): 78.0%; BTTS No (at least one team does not score): 22.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 43.7% | 2.29 |
| Draw | 21.9% | 4.58 |
| Manchester United win | 34.5% | 2.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.25 |
| Manchester United expected goals | 2.04 |
| Expected total goals | 4.29 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 92.5% |
| Under 1.5 | 7.5% |
| Over 2.5 | 79.6% |
| Under 2.5 | 20.4% |
| Over 3.5 | 62.1% |
| Under 3.5 | 37.9% |
| Over 4.5 | 42.2% |
| Under 4.5 | 57.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 8.21% |
| 2 | 2-1 | 6.97% |
| 3 | 1-1 | 6.80% |
| 4 | 1-2 | 6.07% |
| 5 | 3-2 | 5.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 43.7% | 43.0% | 2.37 | +3.5% |
| Draw | 21.9% | 24.5% | 3.96 | -13.5% |
| Manchester United win | 34.5% | 32.5% | 3.02 | +4.1% |

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
| Market best home last update utc | 2026-10-21T10:38:36Z |
| Market best draw last update utc | 2026-10-21T10:38:37Z |
| Market best away last update utc | 2026-10-21T10:38:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como 1907 |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2517 |
| Dc lambda away | 2.0365 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:44.687090+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 78.0% |
| P btts no | 22.0% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 83.07 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.33 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.90 |
| Fair Over 3.5 odds | 1.61 |
| Fair Under 3.5 odds | 2.64 |
| Fair Over 4.5 odds | 2.37 |
| Fair Under 4.5 odds | 1.73 |
| Unadjusted home-win probability | 44.4% |
| Unadjusted draw probability | 19.2% |
| Unadjusted away-win probability | 36.4% |
| Raw p over 1 5 | 92.4% |
| Raw p under 3 5 | 37.9% |
| Raw p btts yes | 77.5% |
| P home draw | 65.5% |
| P draw away | 56.3% |
| P home away | 78.1% |
| Raw p home draw | 63.6% |
| Raw p draw away | 55.6% |
| Raw p home away | 80.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.25 |
| Reference draw odds | 3.86 |
| Reference away odds | 2.94 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:41Z |
| Market reference home last update utc | 2026-10-21T10:38:41Z |
| Market reference draw last update utc | 2026-10-21T10:38:41Z |
| Market reference away last update utc | 2026-10-21T10:38:41Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.57 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:15Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:15Z |
| Home probability edge | +0.7% |
| Draw probability edge | -2.6% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +15.8% |
| Under 2.5 probability edge | -15.8% |
| Raw edge prob home | 0.0143 |
| Raw ev home | 0.0525 |
| Raw edge prob draw | -0.0529 |
| Raw ev draw | -0.2393 |
| Raw edge prob away | 0.0386 |
| Raw ev away | 0.0988 |
| Market p home draw | 67.4% |
| Market home draw odds | 1.45 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T10:38:28Z |
| Market reference home draw last update utc | 2026-10-21T10:38:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.4% |
| Market draw away odds | 1.69 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-21T10:38:37Z |
| Market reference draw away last update utc | 2026-10-21T10:38:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.3% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-21T10:38:28Z |
| Market reference home away last update utc | 2026-10-21T10:38:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.43 |
| Market reference dc draw away odds | 1.68 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-21T10:38:06Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-21T10:38:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.8% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-21T10:38:06Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.17 |
| Market reference under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 66.8% |
| Market btts yes odds | 1.47 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T10:38:28Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 2.66 |
| Market reference btts yes last update utc | 2026-10-21T10:38:37Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **71.3%**. Expected goals are 2.01 for Inter Milan and 1.00 for Shakhtar Donetsk (3.01 combined). The most likely exact score is 1-0 at 12.1%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 59.9%; Under 3.5 goals: 63.4%; Double Chance 1X: 87.2%; Double Chance X2: 28.7%; Double Chance 12 (either team wins): 84.1%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 52.6%; BTTS No (at least one team does not score): 47.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 71.3% | 1.40 |
| Draw | 15.9% | 6.27 |
| Shakhtar Donetsk win | 12.8% | 7.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.01 |
| Shakhtar Donetsk expected goals | 1.00 |
| Expected total goals | 3.01 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 80.7% |
| Under 1.5 | 19.3% |
| Over 2.5 | 59.9% |
| Under 2.5 | 40.1% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.08% |
| 2 | 2-0 | 11.59% |
| 3 | 2-1 | 11.55% |
| 4 | 3-0 | 7.78% |
| 5 | 3-1 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 71.3% | 81.1% | 1.24 | -11.6% |
| Draw | 15.9% | 11.8% | 7.70 | +22.8% |
| Shakhtar Donetsk win | 12.8% | 7.0% | 12.60 | +60.9% |

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
| Market best home last update utc | 2026-10-21T10:38:37Z |
| Market best draw last update utc | 2026-10-21T10:38:37Z |
| Market best away last update utc | 2026-10-21T10:38:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | FK Shakhtar Donetsk |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0140 |
| Dc lambda away | 0.9967 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:44.687090+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 52.6% |
| P btts no | 47.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.36 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.17 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.07 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 61.4% |
| Unadjusted draw probability | 20.0% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 64.5% |
| Raw p btts yes | 54.2% |
| P home draw | 87.2% |
| P draw away | 28.7% |
| P home away | 84.1% |
| Raw p home draw | 81.5% |
| Raw p draw away | 38.6% |
| Raw p home away | 80.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.22 |
| Reference draw odds | 7.60 |
| Reference away odds | 12.50 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:41Z |
| Market reference home last update utc | 2026-10-21T10:38:41Z |
| Market reference draw last update utc | 2026-10-21T10:38:41Z |
| Market reference away last update utc | 2026-10-21T10:38:41Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.75 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:15Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:15Z |
| Home probability edge | -9.8% |
| Draw probability edge | +4.1% |
| Away probability edge | +5.7% |
| Over 2.5 probability edge | -16.5% |
| Under 2.5 probability edge | +16.5% |
| Raw edge prob home | -0.1969 |
| Raw ev home | -0.2381 |
| Raw edge prob draw | 0.0819 |
| Raw ev draw | 0.5434 |
| Raw edge prob away | 0.1150 |
| Raw ev away | 1.3331 |
| Market p home draw | 92.1% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T10:38:29Z |
| Market reference home draw last update utc | 2026-10-21T10:38:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 20.8% |
| Market draw away odds | 4.92 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-21T10:38:29Z |
| Market reference draw away last update utc | 2026-10-21T10:38:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.1% |
| Market home away odds | 1.12 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-21T10:38:37Z |
| Market reference home away last update utc | 2026-10-21T10:38:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 4.65 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 91.5% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 6.60 |
| Market reference over 1 5 last update utc | 2026-10-21T10:38:36Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 44.6% |
| Market under 3 5 odds | 2.15 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market reference under 3 5 odds | 2.03 |
| Market reference under 3 5 opposite odds | 1.68 |
| Market reference under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.8% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T10:38:29Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-21T10:38:37Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Lille vs Galatasaray

The model's most likely 1X2 outcome is **Lille win** at **48.2%**. Expected goals are 1.77 for Lille and 1.15 for Galatasaray (2.91 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 55.0%; Under 3.5 goals: 66.9%; Double Chance 1X: 72.3%; Double Chance X2: 51.8%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 56.6%; BTTS No (at least one team does not score): 43.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 48.2% | 2.08 |
| Draw | 24.1% | 4.15 |
| Galatasaray win | 27.7% | 3.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.77 |
| Galatasaray expected goals | 1.15 |
| Expected total goals | 2.91 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 55.0% |
| Under 2.5 | 45.0% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.27% |
| 2 | 1-0 | 9.32% |
| 3 | 2-1 | 8.93% |
| 4 | 2-0 | 7.78% |
| 5 | 0-1 | 7.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 48.2% | 44.0% | 2.26 | +8.9% |
| Draw | 24.1% | 25.8% | 3.78 | -9.0% |
| Galatasaray win | 27.7% | 30.2% | 3.25 | -9.9% |
| Over 2.5 | 55.0% | 58.5% | 1.70 | -6.5% |
| Under 2.5 | 45.0% | 41.5% | 2.34 | +5.3% |

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
| Market best home last update utc | 2026-10-21T10:38:37Z |
| Market best draw last update utc | 2026-10-21T10:38:37Z |
| Market best away last update utc | 2026-10-21T10:38:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille OSC |
| Matched away-team name | Galatasaray SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7659 |
| Dc lambda away | 1.1484 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:44.687090+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 56.6% |
| P btts no | 43.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.02 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.99 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 52.4% |
| Unadjusted draw probability | 22.3% |
| Unadjusted away-win probability | 25.3% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 66.6% |
| Raw p btts yes | 56.1% |
| P home draw | 72.3% |
| P draw away | 51.8% |
| P home away | 75.9% |
| Raw p home draw | 74.7% |
| Raw p draw away | 47.6% |
| Raw p home away | 77.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.22 |
| Reference draw odds | 3.72 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:41Z |
| Market reference home last update utc | 2026-10-21T10:38:41Z |
| Market reference draw last update utc | 2026-10-21T10:38:41Z |
| Market reference away last update utc | 2026-10-21T10:38:41Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.27 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:41Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:41Z |
| Market best over 2 5 last update utc | 2026-10-21T10:38:37Z |
| Market best under 2 5 last update utc | 2026-10-21T10:38:37Z |
| Home probability edge | +4.2% |
| Draw probability edge | -1.8% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0841 |
| Raw ev home | 0.1839 |
| Raw edge prob draw | -0.0351 |
| Raw ev draw | -0.1559 |
| Raw edge prob away | -0.0490 |
| Raw ev away | -0.1783 |
| Market p home draw | 69.6% |
| Market home draw odds | 1.40 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T10:38:29Z |
| Market reference home draw last update utc | 2026-10-21T10:38:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.6% |
| Market draw away odds | 1.72 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-21T10:38:37Z |
| Market reference draw away last update utc | 2026-10-21T10:38:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.8% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-21T10:38:29Z |
| Market reference home away last update utc | 2026-10-21T10:38:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.39 |
| Market reference dc draw away odds | 1.71 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 82.0% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-21T10:38:36Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.3% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.66 |
| Market reference under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.5% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T10:38:29Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-21T10:38:37Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **64.4%**. Expected goals are 4.60 for Real Betis and 2.70 for Feyenoord (7.30 combined). The most likely exact score is 3-3 at 4.9%. Goal-market probabilities: at least one goal: 100.0%; Over 2.5 goals: 97.4%; Under 3.5 goals: 6.8%; Double Chance 1X: 80.5%; Double Chance X2: 35.6%; Double Chance 12 (either team wins): 83.8%; Under 4.5 goals: 15.5%; BTTS Yes (both teams score): 92.7%; BTTS No (at least one team does not score): 7.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 64.4% | 1.55 |
| Draw | 16.2% | 6.18 |
| Feyenoord win | 19.5% | 5.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 4.60 |
| Feyenoord expected goals | 2.70 |
| Expected total goals | 7.30 |
| Over 0.5 | 100.0% |
| Under 0.5 | 0.0% |
| Over 1.5 | 99.4% |
| Under 1.5 | 0.6% |
| Over 2.5 | 97.4% |
| Under 2.5 | 2.6% |
| Over 3.5 | 93.2% |
| Under 3.5 | 6.8% |
| Over 4.5 | 84.5% |
| Under 4.5 | 15.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-3 | 4.92% |
| 2 | 4-2 | 4.24% |
| 3 | 5-2 | 3.90% |
| 4 | 4-4 | 3.82% |
| 5 | 4-3 | 3.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 64.4% | 58.9% | 1.70 | +9.4% |
| Draw | 16.2% | 20.5% | 4.67 | -24.4% |
| Feyenoord win | 19.5% | 20.5% | 4.67 | -9.1% |

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
| Market best home last update utc | 2026-10-21T10:38:37Z |
| Market best draw last update utc | 2026-10-21T10:38:37Z |
| Market best away last update utc | 2026-10-21T10:38:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.6005 |
| Dc lambda away | 2.6981 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:44.687090+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 24 |
| Score grid omitted mass | 0 |
| P btts yes | 92.7% |
| P btts no | 7.3% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 2845.96 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 167.06 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 38.29 |
| Fair Over 3.5 odds | 1.07 |
| Fair Under 3.5 odds | 14.62 |
| Fair Over 4.5 odds | 1.18 |
| Fair Under 4.5 odds | 6.44 |
| Unadjusted home-win probability | 69.8% |
| Unadjusted draw probability | 11.8% |
| Unadjusted away-win probability | 18.4% |
| Raw p over 1 5 | 99.4% |
| Raw p under 3 5 | 6.7% |
| Raw p btts yes | 92.3% |
| P home draw | 80.5% |
| P draw away | 35.6% |
| P home away | 83.8% |
| Raw p home draw | 81.6% |
| Raw p draw away | 30.2% |
| Raw p home away | 88.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.66 |
| Reference draw odds | 4.55 |
| Reference away odds | 4.55 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:41Z |
| Market reference home last update utc | 2026-10-21T10:38:41Z |
| Market reference draw last update utc | 2026-10-21T10:38:41Z |
| Market reference away last update utc | 2026-10-21T10:38:41Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.18 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:15Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:15Z |
| Home probability edge | +5.5% |
| Draw probability edge | -4.4% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +25.8% |
| Under 2.5 probability edge | -25.8% |
| Raw edge prob home | 0.1091 |
| Raw ev home | 0.1869 |
| Raw edge prob draw | -0.0873 |
| Raw ev draw | -0.4480 |
| Raw edge prob away | -0.0218 |
| Raw ev away | -0.1424 |
| Market p home draw | 78.9% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T10:38:28Z |
| Market reference home draw last update utc | 2026-10-21T10:38:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.2% |
| Market draw away odds | 2.29 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-21T10:38:28Z |
| Market reference draw away last update utc | 2026-10-21T10:38:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.9% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-21T10:38:28Z |
| Market reference home away last update utc | 2026-10-21T10:38:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.28 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 89.5% |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-21T10:38:36Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 50.5% |
| Market under 3 5 odds | 1.92 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market reference under 3 5 odds | 1.82 |
| Market reference under 3 5 opposite odds | 1.85 |
| Market reference under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.8% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T10:38:28Z |
| Market reference btts yes odds | 1.41 |
| Market reference btts yes opposite odds | 2.73 |
| Market reference btts yes last update utc | 2026-10-21T10:38:37Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Real Madrid vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid win** at **79.9%**. Expected goals are 2.82 for Real Madrid and 0.76 for RB Leipzig (3.58 combined). The most likely exact score is 2-0 at 11.0%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 69.4%; Under 3.5 goals: 52.0%; Double Chance 1X: 92.1%; Double Chance X2: 20.1%; Double Chance 12 (either team wins): 87.8%; Under 4.5 goals: 71.0%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 79.9% | 1.25 |
| Draw | 12.2% | 8.20 |
| RB Leipzig win | 7.9% | 12.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.82 |
| RB Leipzig expected goals | 0.76 |
| Expected total goals | 3.58 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 86.9% |
| Under 1.5 | 13.1% |
| Over 2.5 | 69.4% |
| Under 2.5 | 30.6% |
| Over 3.5 | 48.0% |
| Under 3.5 | 52.0% |
| Over 4.5 | 29.0% |
| Under 4.5 | 71.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.03% |
| 2 | 3-0 | 10.36% |
| 3 | 2-1 | 8.44% |
| 4 | 1-0 | 8.14% |
| 5 | 3-1 | 7.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 79.9% | 79.8% | 1.26 | +0.7% |
| Draw | 12.2% | 12.1% | 7.60 | -7.3% |
| RB Leipzig win | 7.9% | 8.1% | 11.10 | -12.3% |

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
| Market best home last update utc | 2026-10-21T10:38:37Z |
| Market best draw last update utc | 2026-10-21T10:38:37Z |
| Market best away last update utc | 2026-10-21T10:38:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8155 |
| Dc lambda away | 0.7647 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:44.687090+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.55 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.64 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.27 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.92 |
| Fair Over 4.5 odds | 3.45 |
| Fair Under 4.5 odds | 1.41 |
| Unadjusted home-win probability | 80.0% |
| Unadjusted draw probability | 12.3% |
| Unadjusted away-win probability | 7.7% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 51.9% |
| Raw p btts yes | 50.0% |
| P home draw | 92.1% |
| P draw away | 20.1% |
| P home away | 87.8% |
| Raw p home draw | 92.3% |
| Raw p draw away | 20.0% |
| Raw p home away | 87.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.24 |
| Reference draw odds | 7.50 |
| Reference away odds | 11.00 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:41Z |
| Market reference home last update utc | 2026-10-21T10:38:41Z |
| Market reference draw last update utc | 2026-10-21T10:38:41Z |
| Market reference away last update utc | 2026-10-21T10:38:41Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.18 |
| Reference Under 2.5 odds | 4.95 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:15Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:15Z |
| Home probability edge | +0.1% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -13.8% |
| Under 2.5 probability edge | +13.8% |
| Raw edge prob home | 0.0018 |
| Raw ev home | 0.0078 |
| Raw edge prob draw | 0.0021 |
| Raw ev draw | -0.0650 |
| Raw edge prob away | -0.0038 |
| Raw ev away | -0.1440 |
| Market p home draw | 91.0% |
| Market home draw odds | 1.07 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T10:38:28Z |
| Market reference home draw last update utc | 2026-10-21T10:38:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.2% |
| Market draw away odds | 4.57 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-21T10:38:28Z |
| Market reference draw away last update utc | 2026-10-21T10:38:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.9% |
| Market home away odds | 1.12 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-21T10:38:37Z |
| Market reference home away last update utc | 2026-10-21T10:38:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.06 |
| Market reference dc draw away odds | 4.35 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 94.6% |
| Market over 1 5 odds | 1.01 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-21T10:38:04Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 7.80 |
| Market reference over 1 5 last update utc | 2026-10-21T10:38:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 35.9% |
| Market under 3 5 odds | 2.67 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market reference under 3 5 odds | 2.43 |
| Market reference under 3 5 opposite odds | 1.47 |
| Market reference under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 64.8% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T10:38:28Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.53 |
| Market reference btts yes last update utc | 2026-10-21T10:38:37Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **88.1%**. Expected goals are 5.51 for Sporting Lisbon and 0.76 for LASK (6.27 combined). The most likely exact score is 5-0 at 7.3%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 92.4%; Under 3.5 goals: 15.8%; Double Chance 1X: 95.6%; Double Chance X2: 11.9%; Double Chance 12 (either team wins): 92.5%; Under 4.5 goals: 29.2%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 88.1% | 1.14 |
| Draw | 7.5% | 13.29 |
| LASK win | 4.4% | 22.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 5.51 |
| LASK expected goals | 0.76 |
| Expected total goals | 6.27 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 97.7% |
| Under 1.5 | 2.3% |
| Over 2.5 | 92.4% |
| Under 2.5 | 7.6% |
| Over 3.5 | 84.2% |
| Under 3.5 | 15.8% |
| Over 4.5 | 70.8% |
| Under 4.5 | 29.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-0 | 7.28% |
| 2 | 6-0 | 6.68% |
| 3 | 4-0 | 6.60% |
| 4 | 5-1 | 5.55% |
| 5 | 7-0 | 5.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 88.1% | 79.5% | 1.26 | +11.0% |
| Draw | 7.5% | 12.8% | 7.24 | -45.5% |
| LASK win | 4.4% | 7.7% | 11.60 | -49.3% |

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
| Market best home last update utc | 2026-10-21T10:38:37Z |
| Market best draw last update utc | 2026-10-21T10:38:37Z |
| Market best away last update utc | 2026-10-21T10:38:37Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 5.5097 |
| Dc lambda away | 0.7626 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:38:44.687090+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 26 |
| Score grid omitted mass | 0 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 200.14 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 44.04 |
| Fair Over 2.5 odds | 1.08 |
| Fair Under 2.5 odds | 13.09 |
| Fair Over 3.5 odds | 1.19 |
| Fair Under 3.5 odds | 6.34 |
| Fair Over 4.5 odds | 1.41 |
| Fair Under 4.5 odds | 3.43 |
| Unadjusted home-win probability | 96.7% |
| Unadjusted draw probability | 2.2% |
| Unadjusted away-win probability | 1.0% |
| Raw p over 1 5 | 98.6% |
| Raw p under 3 5 | 12.9% |
| Raw p btts yes | 53.1% |
| P home draw | 95.6% |
| P draw away | 11.9% |
| P home away | 92.5% |
| Raw p home draw | 99.0% |
| Raw p draw away | 3.3% |
| Raw p home away | 97.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.24 |
| Reference draw odds | 6.85 |
| Reference away odds | 11.00 |
| Market reference 1x2 last update utc | 2026-10-21T10:38:41Z |
| Market reference home last update utc | 2026-10-21T10:38:41Z |
| Market reference draw last update utc | 2026-10-21T10:38:41Z |
| Market reference away last update utc | 2026-10-21T10:38:41Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.21 |
| Market reference over 2 5 last update utc | 2026-10-21T10:38:15Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:38:15Z |
| Home probability edge | +8.6% |
| Draw probability edge | -5.3% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | +20.7% |
| Under 2.5 probability edge | -20.7% |
| Raw edge prob home | 0.1726 |
| Raw ev home | 0.2189 |
| Raw edge prob draw | -0.1056 |
| Raw ev draw | -0.8374 |
| Raw edge prob away | -0.0670 |
| Raw ev away | -0.8818 |
| Market p home draw | 91.6% |
| Market home draw odds | 1.08 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T10:38:28Z |
| Market reference home draw last update utc | 2026-10-21T10:38:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.6% |
| Market draw away odds | 4.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-21T10:38:37Z |
| Market reference draw away last update utc | 2026-10-21T10:38:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 85.8% |
| Market home away odds | 1.13 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-21T10:38:37Z |
| Market reference home away last update utc | 2026-10-21T10:38:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 4.25 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 89.5% |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-21T10:38:36Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 49.5% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market reference under 3 5 odds | 1.85 |
| Market reference under 3 5 opposite odds | 1.82 |
| Market reference under 3 5 last update utc | 2026-10-21T10:38:36Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.2% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T10:38:28Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.05 |
| Market reference btts yes last update utc | 2026-10-21T10:38:37Z |
| Market btts yes bookmakers | 2 |

</details>


---
