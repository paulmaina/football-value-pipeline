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
| Training as of utc | 2026-10-21T09:21:51.625006+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 18, 'bbs_added_results': 0, 'bbs_result_conflicts': 18, 'bbs_rows_with_statistics': 11, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 139, 'added_results': 0, 'conflicts': 1, 'unmapped': 78, 'ambiguous': 0, 'excluded_phase': 460, 'statistics_observations': 2, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T09:21:51.625006+00:00', 'observations': 92, 'observations_sha256': '72347b6bcae0e0ce159d7750251ed2c3abbfa07a9b60e23346c26fb208ecc5a8', 'eligible_training_matches': 0, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 13, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 0, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': 'c7d3aae6c4753ebcd1b05154046ade2fa85fdc1bd67957524899113a0bc2bbf9', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 466.059 |
| Base scoring parameter | 0.213 |
| Home-advantage parameter | 0.327 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0029 |
| Training data health | {'completed_matches': 45, 'latest_completed_utc': '2026-10-20T19:00:00+00:00', 'latest_completed_date': '2026-10-20', 'next_fixture_utc': '2026-10-21T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-21T09:21:40.767492+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'f6cc44b4326bf411cae39d63597f271b3c4ce2c69cc1c4359f759ddcc1a9bb83', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0030159761111111113, 'training_end': '2026-10-20', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261021T092151625006Z_8261bb846179c6b5b0292fa22da1ed1fff23dd3ede34f3920e3049064976a9a1.json |
| Over 1 5 in window quote fixtures | 7 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **80.8%**. Expected goals are 3.97 for Aston Villa and 1.34 for Viking FK (5.31 combined). The most likely exact score is 3-1 at 6.7%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 89.4%; Under 3.5 goals: 22.6%; Double Chance 1X: 92.2%; Double Chance X2: 19.2%; Double Chance 12 (either team wins): 88.6%; Under 4.5 goals: 39.5%; BTTS Yes (both teams score): 72.9%; BTTS No (at least one team does not score): 27.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 80.8% | 1.24 |
| Draw | 11.4% | 8.78 |
| Viking FK win | 7.8% | 12.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 3.97 |
| Viking FK expected goals | 1.34 |
| Expected total goals | 5.31 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 96.7% |
| Under 1.5 | 3.3% |
| Over 2.5 | 89.4% |
| Under 2.5 | 10.6% |
| Over 3.5 | 77.4% |
| Under 3.5 | 22.6% |
| Over 4.5 | 60.5% |
| Under 4.5 | 39.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 6.74% |
| 2 | 4-1 | 6.69% |
| 3 | 5-1 | 5.31% |
| 4 | 2-1 | 5.10% |
| 5 | 3-0 | 5.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 80.8% | 78.8% | 1.26 | +1.8% |
| Draw | 11.4% | 13.5% | 6.89 | -21.6% |
| Viking FK win | 7.8% | 7.7% | 12.60 | -1.3% |

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
| Market best home last update utc | 2026-10-21T09:20:35Z |
| Market best draw last update utc | 2026-10-21T09:20:35Z |
| Market best away last update utc | 2026-10-21T09:20:35Z |
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
| Bbs statistics cutoff utc | 2026-10-21T09:21:51.625006+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 23 |
| Score grid omitted mass | 0 |
| P btts yes | 72.9% |
| P btts no | 27.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 225.48 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 30.58 |
| Fair Over 2.5 odds | 1.12 |
| Fair Under 2.5 odds | 9.47 |
| Fair Over 3.5 odds | 1.29 |
| Fair Under 3.5 odds | 4.42 |
| Fair Over 4.5 odds | 1.65 |
| Fair Under 4.5 odds | 2.53 |
| Unadjusted home-win probability | 82.8% |
| Unadjusted draw probability | 9.3% |
| Unadjusted away-win probability | 7.9% |
| Raw p over 1 5 | 96.8% |
| Raw p under 3 5 | 22.4% |
| Raw p btts yes | 72.4% |
| P home draw | 92.2% |
| P draw away | 19.2% |
| P home away | 88.6% |
| Raw p home draw | 92.1% |
| Raw p draw away | 17.2% |
| Raw p home away | 90.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.26 |
| Reference draw odds | 7.00 |
| Reference away odds | 12.00 |
| Market reference 1x2 last update utc | 2026-10-21T09:21:45Z |
| Market reference home last update utc | 2026-10-21T09:21:45Z |
| Market reference draw last update utc | 2026-10-21T09:21:45Z |
| Market reference away last update utc | 2026-10-21T09:21:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-21T09:21:43Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:21:43Z |
| Home probability edge | +2.0% |
| Draw probability edge | -2.1% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +15.2% |
| Under 2.5 probability edge | -15.2% |
| Raw edge prob home | 0.0395 |
| Raw ev home | 0.0428 |
| Raw edge prob draw | -0.0416 |
| Raw ev draw | -0.3590 |
| Raw edge prob away | 0.0021 |
| Raw ev away | -0.0004 |
| Market p home draw | 91.1% |
| Market home draw odds | 1.07 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T09:21:43Z |
| Market reference home draw last update utc | 2026-10-21T09:21:43Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.7% |
| Market draw away odds | 4.30 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-21T09:21:43Z |
| Market reference draw away last update utc | 2026-10-21T09:21:43Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.2% |
| Market home away odds | 1.14 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-21T09:20:35Z |
| Market reference home away last update utc | 2026-10-21T09:21:43Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.07 |
| Market reference dc draw away odds | 4.30 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 90.1% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 8.20 |
| Market reference over 1 5 last update utc | 2026-10-21T09:21:45Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 46.2% |
| Market under 3 5 odds | 2.04 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T09:21:40Z |
| Market reference under 3 5 odds | 2.08 |
| Market reference under 3 5 opposite odds | 1.80 |
| Market reference under 3 5 last update utc | 2026-10-21T09:21:45Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.4% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T09:21:43Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.19 |
| Market reference btts yes last update utc | 2026-10-21T09:21:43Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Bayern Munich win** at **38.5%**. Expected goals are 1.01 for Bayern Munich and 1.21 for Arsenal (2.22 combined). The most likely exact score is 1-0 at 14.3%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 38.6%; Under 3.5 goals: 81.6%; Double Chance 1X: 64.5%; Double Chance X2: 61.5%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 43.7%; BTTS No (at least one team does not score): 56.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 38.5% | 2.60 |
| Draw | 26.0% | 3.84 |
| Arsenal win | 35.5% | 2.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 1.01 |
| Arsenal expected goals | 1.21 |
| Expected total goals | 2.22 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 64.2% |
| Under 1.5 | 35.8% |
| Over 2.5 | 38.6% |
| Under 2.5 | 61.4% |
| Over 3.5 | 18.4% |
| Under 3.5 | 81.6% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.30% |
| 2 | 1-1 | 11.96% |
| 3 | 0-1 | 11.82% |
| 4 | 0-0 | 9.63% |
| 5 | 2-1 | 8.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 38.5% | 45.8% | 2.11 | -18.7% |
| Draw | 26.0% | 24.6% | 4.04 | +5.1% |
| Arsenal win | 35.5% | 29.6% | 3.39 | +20.2% |

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
| Market best home last update utc | 2026-10-21T09:20:35Z |
| Market best draw last update utc | 2026-10-21T09:20:35Z |
| Market best away last update utc | 2026-10-21T09:20:35Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Bayern München |
| Matched away-team name | Arsenal FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0114 |
| Dc lambda away | 1.2130 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:21:51.625006+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.7% |
| P btts no | 56.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.38 |
| Fair Over 1.5 odds | 1.56 |
| Fair Under 1.5 odds | 2.80 |
| Fair Over 2.5 odds | 2.59 |
| Fair Under 2.5 odds | 1.63 |
| Fair Over 3.5 odds | 5.43 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.23 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 41.3% |
| Raw p over 1 5 | 64.5% |
| Raw p under 3 5 | 81.5% |
| Raw p btts yes | 44.0% |
| P home draw | 64.5% |
| P draw away | 61.5% |
| P home away | 74.0% |
| Raw p home draw | 58.7% |
| Raw p draw away | 68.8% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.15 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-21T09:21:45Z |
| Market reference home last update utc | 2026-10-21T09:21:45Z |
| Market reference draw last update utc | 2026-10-21T09:21:45Z |
| Market reference away last update utc | 2026-10-21T09:21:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T09:21:43Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:21:43Z |
| Home probability edge | -7.3% |
| Draw probability edge | +1.4% |
| Away probability edge | +5.9% |
| Over 2.5 probability edge | -25.1% |
| Under 2.5 probability edge | +25.1% |
| Raw edge prob home | -0.1455 |
| Raw ev home | -0.3407 |
| Raw edge prob draw | 0.0280 |
| Raw ev draw | 0.1078 |
| Raw edge prob away | 0.1175 |
| Raw ev away | 0.4011 |
| Market p home draw | 70.4% |
| Market home draw odds | 1.37 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-21T09:20:35Z |
| Market reference home draw last update utc | 2026-10-21T09:21:44Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.2% |
| Market draw away odds | 1.81 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-21T09:20:35Z |
| Market reference draw away last update utc | 2026-10-21T09:21:44Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-21T09:20:35Z |
| Market reference home away last update utc | 2026-10-21T09:21:44Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.37 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 83.6% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-21T09:20:03Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-10-21T09:21:45Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.1% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-21T09:20:03Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.39 |
| Market reference under 3 5 last update utc | 2026-10-21T09:21:45Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 64.6% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T09:21:44Z |
| Market reference btts yes odds | 1.51 |
| Market reference btts yes opposite odds | 2.67 |
| Market reference btts yes last update utc | 2026-10-21T09:21:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **68.8%**. Expected goals are 4.47 for Club Brugge and 1.36 for RC Lens (5.82 combined). The most likely exact score is 2-2 at 5.6%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 90.5%; Under 3.5 goals: 19.8%; Double Chance 1X: 83.8%; Double Chance X2: 31.2%; Double Chance 12 (either team wins): 85.0%; Under 4.5 goals: 35.6%; BTTS Yes (both teams score): 76.7%; BTTS No (at least one team does not score): 23.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 68.8% | 1.45 |
| Draw | 15.0% | 6.65 |
| RC Lens win | 16.2% | 6.17 |

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
| Over 2.5 | 90.5% |
| Under 2.5 | 9.5% |
| Over 3.5 | 80.2% |
| Under 3.5 | 19.8% |
| Over 4.5 | 64.4% |
| Under 4.5 | 35.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 5.56% |
| 2 | 4-1 | 5.27% |
| 3 | 3-1 | 4.72% |
| 4 | 5-1 | 4.71% |
| 5 | 4-0 | 3.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 68.8% | 50.7% | 1.94 | +33.4% |
| Draw | 15.0% | 22.7% | 4.37 | -34.3% |
| RC Lens win | 16.2% | 26.6% | 3.68 | -40.4% |

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
| Market best home last update utc | 2026-10-21T09:20:35Z |
| Market best draw last update utc | 2026-10-21T09:20:35Z |
| Market best away last update utc | 2026-10-21T09:20:35Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Club Brugge KV |
| Matched away-team name | Racing Club de Lens |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.4679 |
| Dc lambda away | 1.3550 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:21:51.625006+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 24 |
| Score grid omitted mass | 0 |
| P btts yes | 76.7% |
| P btts no | 23.3% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 236.51 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 34.51 |
| Fair Over 2.5 odds | 1.10 |
| Fair Under 2.5 odds | 10.55 |
| Fair Over 3.5 odds | 1.25 |
| Fair Under 3.5 odds | 5.04 |
| Fair Over 4.5 odds | 1.55 |
| Fair Under 4.5 odds | 2.81 |
| Unadjusted home-win probability | 86.8% |
| Unadjusted draw probability | 7.3% |
| Unadjusted away-win probability | 5.9% |
| Raw p over 1 5 | 97.9% |
| Raw p under 3 5 | 16.8% |
| Raw p btts yes | 73.3% |
| P home draw | 83.8% |
| P draw away | 31.2% |
| P home away | 85.0% |
| Raw p home draw | 94.1% |
| Raw p draw away | 13.2% |
| Raw p home away | 92.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.94 |
| Reference draw odds | 4.25 |
| Reference away odds | 3.65 |
| Market reference 1x2 last update utc | 2026-10-21T09:21:45Z |
| Market reference home last update utc | 2026-10-21T09:21:45Z |
| Market reference draw last update utc | 2026-10-21T09:21:45Z |
| Market reference away last update utc | 2026-10-21T09:21:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-21T09:21:43Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:21:43Z |
| Home probability edge | +18.0% |
| Draw probability edge | -7.7% |
| Away probability edge | -10.3% |
| Over 2.5 probability edge | +18.9% |
| Under 2.5 probability edge | -18.9% |
| Raw edge prob home | 0.3608 |
| Raw ev home | 0.6841 |
| Raw edge prob draw | -0.1539 |
| Raw ev draw | -0.6796 |
| Raw edge prob away | -0.2069 |
| Raw ev away | -0.7843 |
| Market p home draw | 73.6% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-21T09:20:35Z |
| Market reference home draw last update utc | 2026-10-21T09:21:43Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.3% |
| Market draw away odds | 1.97 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-21T09:21:43Z |
| Market reference draw away last update utc | 2026-10-21T09:21:43Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.1% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-21T09:21:43Z |
| Market reference home away last update utc | 2026-10-21T09:21:43Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.32 |
| Market reference dc draw away odds | 1.97 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 89.1% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-21T09:07:21Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 7.40 |
| Market reference over 1 5 last update utc | 2026-10-21T09:21:45Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.6% |
| Market under 3 5 odds | 2.00 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T09:21:40Z |
| Market reference under 3 5 odds | 1.95 |
| Market reference under 3 5 opposite odds | 1.92 |
| Market reference under 3 5 last update utc | 2026-10-21T09:21:45Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 71.7% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T09:21:43Z |
| Market reference btts yes odds | 1.37 |
| Market reference btts yes opposite odds | 3.31 |
| Market reference btts yes last update utc | 2026-10-21T09:21:43Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Como vs Manchester United

The model's most likely 1X2 outcome is **Como win** at **43.1%**. Expected goals are 2.25 for Como and 2.04 for Manchester United (4.29 combined). The most likely exact score is 2-2 at 8.3%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 79.5%; Under 3.5 goals: 37.9%; Double Chance 1X: 65.2%; Double Chance X2: 56.9%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 57.9%; BTTS Yes (both teams score): 78.1%; BTTS No (at least one team does not score): 21.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 43.1% | 2.32 |
| Draw | 22.1% | 4.53 |
| Manchester United win | 34.8% | 2.87 |

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
| Over 2.5 | 79.5% |
| Under 2.5 | 20.5% |
| Over 3.5 | 62.1% |
| Under 3.5 | 37.9% |
| Over 4.5 | 42.1% |
| Under 4.5 | 57.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 8.30% |
| 2 | 2-1 | 6.88% |
| 3 | 1-1 | 6.88% |
| 4 | 1-2 | 6.13% |
| 5 | 3-2 | 5.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 43.1% | 41.8% | 2.36 | +1.8% |
| Draw | 22.1% | 25.0% | 3.96 | -12.5% |
| Manchester United win | 34.8% | 33.2% | 3.02 | +5.1% |

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
| Market best home last update utc | 2026-10-21T09:21:40Z |
| Market best draw last update utc | 2026-10-21T09:20:35Z |
| Market best away last update utc | 2026-10-21T09:20:35Z |
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
| Dc lambda away | 2.0367 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:21:51.625006+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 78.1% |
| P btts no | 21.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 82.21 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.34 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.88 |
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
| P home draw | 65.2% |
| P draw away | 56.9% |
| P home away | 77.9% |
| Raw p home draw | 63.6% |
| Raw p draw away | 55.6% |
| Raw p home away | 80.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.35 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-21T09:21:45Z |
| Market reference home last update utc | 2026-10-21T09:21:45Z |
| Market reference draw last update utc | 2026-10-21T09:21:45Z |
| Market reference away last update utc | 2026-10-21T09:21:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T09:21:43Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:21:43Z |
| Home probability edge | +1.3% |
| Draw probability edge | -2.9% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | +16.5% |
| Under 2.5 probability edge | -16.5% |
| Raw edge prob home | 0.0256 |
| Raw ev home | 0.0480 |
| Raw edge prob draw | -0.0576 |
| Raw ev draw | -0.2394 |
| Raw edge prob away | 0.0320 |
| Raw ev away | 0.0989 |
| Market p home draw | 66.8% |
| Market home draw odds | 1.45 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T09:21:43Z |
| Market reference home draw last update utc | 2026-10-21T09:21:43Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.7% |
| Market draw away odds | 1.69 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-21T09:20:35Z |
| Market reference draw away last update utc | 2026-10-21T09:21:43Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.5% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-21T09:21:43Z |
| Market reference home away last update utc | 2026-10-21T09:21:43Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.45 |
| Market reference dc draw away odds | 1.65 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 84.3% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-21T09:20:40Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-10-21T09:21:45Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.3% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-21T09:20:40Z |
| Market reference under 3 5 odds | 1.64 |
| Market reference under 3 5 opposite odds | 2.34 |
| Market reference under 3 5 last update utc | 2026-10-21T09:21:45Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 66.2% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T09:21:43Z |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.80 |
| Market reference btts yes last update utc | 2026-10-21T09:21:43Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **71.4%**. Expected goals are 2.01 for Inter Milan and 1.00 for Shakhtar Donetsk (3.01 combined). The most likely exact score is 1-0 at 12.1%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 59.9%; Under 3.5 goals: 63.4%; Double Chance 1X: 87.3%; Double Chance X2: 28.6%; Double Chance 12 (either team wins): 84.1%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 52.6%; BTTS No (at least one team does not score): 47.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 71.4% | 1.40 |
| Draw | 15.9% | 6.29 |
| Shakhtar Donetsk win | 12.7% | 7.86 |

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
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.10% |
| 2 | 2-0 | 11.60% |
| 3 | 2-1 | 11.57% |
| 4 | 3-0 | 7.79% |
| 5 | 3-1 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 71.4% | 81.3% | 1.24 | -11.5% |
| Draw | 15.9% | 11.7% | 7.70 | +22.3% |
| Shakhtar Donetsk win | 12.7% | 6.9% | 12.60 | +60.4% |

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
| Market best home last update utc | 2026-10-21T09:20:35Z |
| Market best draw last update utc | 2026-10-21T09:20:35Z |
| Market best away last update utc | 2026-10-21T09:20:35Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | FK Shakhtar Donetsk |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0143 |
| Dc lambda away | 0.9968 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:21:51.625006+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 52.6% |
| P btts no | 47.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.48 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.18 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.06 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 61.4% |
| Unadjusted draw probability | 20.0% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 79.8% |
| Raw p under 3 5 | 64.5% |
| Raw p btts yes | 54.2% |
| P home draw | 87.3% |
| P draw away | 28.6% |
| P home away | 84.1% |
| Raw p home draw | 81.5% |
| Raw p draw away | 38.6% |
| Raw p home away | 80.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.22 |
| Reference draw odds | 7.85 |
| Reference away odds | 13.00 |
| Market reference 1x2 last update utc | 2026-10-21T09:21:45Z |
| Market reference home last update utc | 2026-10-21T09:21:45Z |
| Market reference draw last update utc | 2026-10-21T09:21:45Z |
| Market reference away last update utc | 2026-10-21T09:21:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.50 |
| Market reference over 2 5 last update utc | 2026-10-21T09:21:43Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:21:43Z |
| Home probability edge | -9.9% |
| Draw probability edge | +4.2% |
| Away probability edge | +5.8% |
| Over 2.5 probability edge | -15.3% |
| Under 2.5 probability edge | +15.3% |
| Raw edge prob home | -0.1988 |
| Raw ev home | -0.2381 |
| Raw edge prob draw | 0.0831 |
| Raw ev draw | 0.5432 |
| Raw edge prob away | 0.1157 |
| Raw ev away | 1.3329 |
| Market p home draw | 92.1% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T09:21:44Z |
| Market reference home draw last update utc | 2026-10-21T09:21:44Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 19.9% |
| Market draw away odds | 4.92 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-21T09:21:44Z |
| Market reference draw away last update utc | 2026-10-21T09:21:44Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.0% |
| Market home away odds | 1.12 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-21T09:20:35Z |
| Market reference home away last update utc | 2026-10-21T09:21:44Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.06 |
| Market reference dc draw away odds | 4.92 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 90.8% |
| Market over 1 5 odds | 1.03 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-21T09:10:24Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 8.40 |
| Market reference over 1 5 last update utc | 2026-10-21T09:21:45Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 45.5% |
| Market under 3 5 odds | 2.17 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-21T09:10:24Z |
| Market reference under 3 5 odds | 2.11 |
| Market reference under 3 5 opposite odds | 1.78 |
| Market reference under 3 5 last update utc | 2026-10-21T09:21:45Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 55.0% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T09:21:44Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.13 |
| Market reference btts yes last update utc | 2026-10-21T09:21:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Lille vs Galatasaray

The model's most likely 1X2 outcome is **Lille win** at **48.1%**. Expected goals are 1.77 for Lille and 1.15 for Galatasaray (2.91 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 55.1%; Under 3.5 goals: 66.9%; Double Chance 1X: 72.0%; Double Chance X2: 51.9%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 56.6%; BTTS No (at least one team does not score): 43.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 48.1% | 2.08 |
| Draw | 23.9% | 4.18 |
| Galatasaray win | 28.0% | 3.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.77 |
| Galatasaray expected goals | 1.15 |
| Expected total goals | 2.91 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.20% |
| 2 | 1-0 | 9.30% |
| 3 | 2-1 | 8.92% |
| 4 | 2-0 | 7.77% |
| 5 | 0-1 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 48.1% | 43.8% | 2.26 | +8.7% |
| Draw | 23.9% | 25.5% | 3.78 | -9.5% |
| Galatasaray win | 28.0% | 30.6% | 3.25 | -9.1% |
| Over 2.5 | 55.1% | 58.9% | 1.70 | -6.4% |
| Under 2.5 | 44.9% | 41.1% | 2.34 | +5.2% |

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
| Market best home last update utc | 2026-10-21T09:20:35Z |
| Market best draw last update utc | 2026-10-21T09:20:35Z |
| Market best away last update utc | 2026-10-21T09:20:35Z |
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
| Dc lambda home | 1.7662 |
| Dc lambda away | 1.1483 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:21:51.625006+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 56.6% |
| P btts no | 43.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.15 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.98 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 52.4% |
| Unadjusted draw probability | 22.3% |
| Unadjusted away-win probability | 25.3% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 66.6% |
| Raw p btts yes | 56.1% |
| P home draw | 72.0% |
| P draw away | 51.9% |
| P home away | 76.1% |
| Raw p home draw | 74.7% |
| Raw p draw away | 47.6% |
| Raw p home away | 77.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.24 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.18 |
| Market reference 1x2 last update utc | 2026-10-21T09:21:45Z |
| Market reference home last update utc | 2026-10-21T09:21:45Z |
| Market reference draw last update utc | 2026-10-21T09:21:45Z |
| Market reference away last update utc | 2026-10-21T09:21:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-21T09:21:43Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:21:43Z |
| Market best over 2 5 last update utc | 2026-10-21T09:20:35Z |
| Market best under 2 5 last update utc | 2026-10-21T09:20:35Z |
| Home probability edge | +4.3% |
| Draw probability edge | -1.6% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | 0.0856 |
| Raw ev home | 0.1841 |
| Raw edge prob draw | -0.0320 |
| Raw ev draw | -0.1560 |
| Raw edge prob away | -0.0536 |
| Raw ev away | -0.1785 |
| Market p home draw | 69.9% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T09:21:43Z |
| Market reference home draw last update utc | 2026-10-21T09:21:43Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.9% |
| Market draw away odds | 1.74 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-21T09:21:43Z |
| Market reference draw away last update utc | 2026-10-21T09:21:43Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.2% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-21T09:21:43Z |
| Market reference home away last update utc | 2026-10-21T09:21:43Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.39 |
| Market reference dc draw away odds | 1.74 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 80.8% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-21T09:14:03Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.65 |
| Market reference over 1 5 last update utc | 2026-10-21T09:21:45Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T09:21:40Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.67 |
| Market reference under 3 5 last update utc | 2026-10-21T09:21:45Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 62.1% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T09:21:43Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.51 |
| Market reference btts yes last update utc | 2026-10-21T09:21:43Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **64.7%**. Expected goals are 4.60 for Real Betis and 2.70 for Feyenoord (7.30 combined). The most likely exact score is 3-3 at 4.9%. Goal-market probabilities: at least one goal: 100.0%; Over 2.5 goals: 97.4%; Under 3.5 goals: 6.8%; Double Chance 1X: 80.9%; Double Chance X2: 35.3%; Double Chance 12 (either team wins): 83.7%; Under 4.5 goals: 15.5%; BTTS Yes (both teams score): 92.7%; BTTS No (at least one team does not score): 7.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 64.7% | 1.55 |
| Draw | 16.3% | 6.15 |
| Feyenoord win | 19.1% | 5.24 |

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
| 1 | 3-3 | 4.94% |
| 2 | 4-2 | 4.26% |
| 3 | 5-2 | 3.92% |
| 4 | 4-4 | 3.83% |
| 5 | 4-3 | 3.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 64.7% | 59.5% | 1.70 | +9.9% |
| Draw | 16.3% | 20.7% | 4.67 | -24.1% |
| Feyenoord win | 19.1% | 19.8% | 4.67 | -10.8% |

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
| Market best home last update utc | 2026-10-21T09:20:35Z |
| Market best draw last update utc | 2026-10-21T09:20:35Z |
| Market best away last update utc | 2026-10-21T09:20:35Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.6004 |
| Dc lambda away | 2.6977 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:21:51.625006+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 24 |
| Score grid omitted mass | 0 |
| P btts yes | 92.7% |
| P btts no | 7.3% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 2830.60 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 167.77 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 38.27 |
| Fair Over 3.5 odds | 1.07 |
| Fair Under 3.5 odds | 14.65 |
| Fair Over 4.5 odds | 1.18 |
| Fair Under 4.5 odds | 6.44 |
| Unadjusted home-win probability | 69.8% |
| Unadjusted draw probability | 11.8% |
| Unadjusted away-win probability | 18.4% |
| Raw p over 1 5 | 99.4% |
| Raw p under 3 5 | 6.7% |
| Raw p btts yes | 92.3% |
| P home draw | 80.9% |
| P draw away | 35.3% |
| P home away | 83.7% |
| Raw p home draw | 81.6% |
| Raw p draw away | 30.2% |
| Raw p home away | 88.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.66 |
| Reference draw odds | 4.65 |
| Reference away odds | 4.85 |
| Market reference 1x2 last update utc | 2026-10-21T09:21:45Z |
| Market reference home last update utc | 2026-10-21T09:21:45Z |
| Market reference draw last update utc | 2026-10-21T09:21:45Z |
| Market reference away last update utc | 2026-10-21T09:21:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-21T09:21:43Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:21:43Z |
| Home probability edge | +5.2% |
| Draw probability edge | -4.4% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +26.6% |
| Under 2.5 probability edge | -26.6% |
| Raw edge prob home | 0.1034 |
| Raw ev home | 0.1869 |
| Raw edge prob draw | -0.0888 |
| Raw ev draw | -0.4480 |
| Raw edge prob away | -0.0146 |
| Raw ev away | -0.1426 |
| Market p home draw | 78.8% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T09:21:43Z |
| Market reference home draw last update utc | 2026-10-21T09:22:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.4% |
| Market draw away odds | 2.29 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-21T09:21:43Z |
| Market reference draw away last update utc | 2026-10-21T09:22:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.8% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-21T09:21:43Z |
| Market reference home away last update utc | 2026-10-21T09:22:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.21 |
| Market reference dc draw away odds | 2.25 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 89.5% |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-21T09:22:03Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 50.5% |
| Market under 3 5 odds | 1.91 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T09:21:40Z |
| Market reference under 3 5 odds | 1.82 |
| Market reference under 3 5 opposite odds | 1.85 |
| Market reference under 3 5 last update utc | 2026-10-21T09:22:03Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T09:21:43Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.80 |
| Market reference btts yes last update utc | 2026-10-21T09:21:43Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Real Madrid vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid win** at **79.7%**. Expected goals are 2.82 for Real Madrid and 0.76 for RB Leipzig (3.58 combined). The most likely exact score is 2-0 at 11.0%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 69.3%; Under 3.5 goals: 52.0%; Double Chance 1X: 92.0%; Double Chance X2: 20.3%; Double Chance 12 (either team wins): 87.7%; Under 4.5 goals: 71.1%; BTTS Yes (both teams score): 50.0%; BTTS No (at least one team does not score): 50.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 79.7% | 1.26 |
| Draw | 12.3% | 8.11 |
| RB Leipzig win | 8.0% | 12.48 |

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
| Over 2.5 | 69.3% |
| Under 2.5 | 30.7% |
| Over 3.5 | 48.0% |
| Under 3.5 | 52.0% |
| Over 4.5 | 28.9% |
| Under 4.5 | 71.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.00% |
| 2 | 3-0 | 10.32% |
| 3 | 2-1 | 8.41% |
| 4 | 1-0 | 8.11% |
| 5 | 3-1 | 7.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 79.7% | 79.3% | 1.26 | +0.4% |
| Draw | 12.3% | 12.4% | 7.60 | -6.3% |
| RB Leipzig win | 8.0% | 8.3% | 11.10 | -11.1% |

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
| Market best home last update utc | 2026-10-21T09:20:35Z |
| Market best draw last update utc | 2026-10-21T09:20:35Z |
| Market best away last update utc | 2026-10-21T09:20:35Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8156 |
| Dc lambda away | 0.7647 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:21:51.625006+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.12 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.62 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.26 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.92 |
| Fair Over 4.5 odds | 3.46 |
| Fair Under 4.5 odds | 1.41 |
| Unadjusted home-win probability | 80.0% |
| Unadjusted draw probability | 12.3% |
| Unadjusted away-win probability | 7.7% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 51.9% |
| Raw p btts yes | 50.0% |
| P home draw | 92.0% |
| P draw away | 20.3% |
| P home away | 87.7% |
| Raw p home draw | 92.3% |
| Raw p draw away | 20.0% |
| Raw p home away | 87.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.25 |
| Reference draw odds | 7.50 |
| Reference away odds | 11.00 |
| Market reference 1x2 last update utc | 2026-10-21T09:21:45Z |
| Market reference home last update utc | 2026-10-21T09:21:45Z |
| Market reference draw last update utc | 2026-10-21T09:21:45Z |
| Market reference away last update utc | 2026-10-21T09:21:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.18 |
| Reference Under 2.5 odds | 4.80 |
| Market reference over 2 5 last update utc | 2026-10-21T09:21:43Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:21:43Z |
| Home probability edge | +0.3% |
| Draw probability edge | -0.0% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -13.7% |
| Under 2.5 probability edge | +13.7% |
| Raw edge prob home | 0.0065 |
| Raw ev home | 0.0078 |
| Raw edge prob draw | -0.0006 |
| Raw ev draw | -0.0650 |
| Raw edge prob away | -0.0060 |
| Raw ev away | -0.1440 |
| Market p home draw | 90.8% |
| Market home draw odds | 1.07 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T09:21:44Z |
| Market reference home draw last update utc | 2026-10-21T09:22:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.4% |
| Market draw away odds | 4.57 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-21T09:21:44Z |
| Market reference draw away last update utc | 2026-10-21T09:22:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.7% |
| Market home away odds | 1.12 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-21T09:20:35Z |
| Market reference home away last update utc | 2026-10-21T09:22:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 4.25 |
| Market reference dc home away odds | 1.10 |
| Market p over 1 5 | 94.6% |
| Market over 1 5 odds | 1.01 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-21T09:20:42Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 7.80 |
| Market reference over 1 5 last update utc | 2026-10-21T09:22:03Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 35.9% |
| Market under 3 5 odds | 2.65 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-21T09:21:40Z |
| Market reference under 3 5 odds | 2.43 |
| Market reference under 3 5 opposite odds | 1.47 |
| Market reference under 3 5 last update utc | 2026-10-21T09:22:03Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 65.4% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T09:21:44Z |
| Market reference btts yes odds | 1.49 |
| Market reference btts yes opposite odds | 2.71 |
| Market reference btts yes last update utc | 2026-10-21T09:21:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **88.4%**. Expected goals are 5.51 for Sporting Lisbon and 0.76 for LASK (6.27 combined). The most likely exact score is 5-0 at 7.3%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 92.4%; Under 3.5 goals: 15.7%; Double Chance 1X: 95.7%; Double Chance X2: 11.6%; Double Chance 12 (either team wins): 92.7%; Under 4.5 goals: 29.0%; BTTS Yes (both teams score): 56.0%; BTTS No (at least one team does not score): 44.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 88.4% | 1.13 |
| Draw | 7.3% | 13.62 |
| LASK win | 4.3% | 23.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 5.51 |
| LASK expected goals | 0.76 |
| Expected total goals | 6.27 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 97.8% |
| Under 1.5 | 2.2% |
| Over 2.5 | 92.4% |
| Under 2.5 | 7.6% |
| Over 3.5 | 84.3% |
| Under 3.5 | 15.7% |
| Over 4.5 | 71.0% |
| Under 4.5 | 29.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-0 | 7.30% |
| 2 | 6-0 | 6.70% |
| 3 | 4-0 | 6.62% |
| 4 | 5-1 | 5.56% |
| 5 | 7-0 | 5.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 88.4% | 80.0% | 1.24 | +9.6% |
| Draw | 7.3% | 12.4% | 7.75 | -43.1% |
| LASK win | 4.3% | 7.6% | 12.20 | -47.5% |

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
| Market best home last update utc | 2026-10-21T09:20:35Z |
| Market best draw last update utc | 2026-10-21T09:20:35Z |
| Market best away last update utc | 2026-10-21T09:20:35Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 5.5101 |
| Dc lambda away | 0.7626 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:21:51.625006+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 26 |
| Score grid omitted mass | 0 |
| P btts yes | 56.0% |
| P btts no | 44.0% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 205.29 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 44.49 |
| Fair Over 2.5 odds | 1.08 |
| Fair Under 2.5 odds | 13.23 |
| Fair Over 3.5 odds | 1.19 |
| Fair Under 3.5 odds | 6.37 |
| Fair Over 4.5 odds | 1.41 |
| Fair Under 4.5 odds | 3.44 |
| Unadjusted home-win probability | 96.7% |
| Unadjusted draw probability | 2.2% |
| Unadjusted away-win probability | 1.0% |
| Raw p over 1 5 | 98.6% |
| Raw p under 3 5 | 12.8% |
| Raw p btts yes | 53.1% |
| P home draw | 95.7% |
| P draw away | 11.6% |
| P home away | 92.7% |
| Raw p home draw | 99.0% |
| Raw p draw away | 3.3% |
| Raw p home away | 97.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.24 |
| Reference draw odds | 7.45 |
| Reference away odds | 12.00 |
| Market reference 1x2 last update utc | 2026-10-21T09:21:45Z |
| Market reference home last update utc | 2026-10-21T09:21:45Z |
| Market reference draw last update utc | 2026-10-21T09:21:45Z |
| Market reference away last update utc | 2026-10-21T09:21:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-21T09:21:43Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:21:43Z |
| Home probability edge | +8.4% |
| Draw probability edge | -5.1% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | +19.7% |
| Under 2.5 probability edge | -19.7% |
| Raw edge prob home | 0.1675 |
| Raw ev home | 0.1995 |
| Raw edge prob draw | -0.1019 |
| Raw ev draw | -0.8259 |
| Raw edge prob away | -0.0656 |
| Raw ev away | -0.8757 |
| Market p home draw | 91.2% |
| Market home draw odds | 1.07 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-21T09:21:42Z |
| Market reference home draw last update utc | 2026-10-21T09:21:43Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 21.8% |
| Market draw away odds | 4.52 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-21T09:20:35Z |
| Market reference draw away last update utc | 2026-10-21T09:21:43Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.0% |
| Market home away odds | 1.12 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-21T09:21:42Z |
| Market reference home away last update utc | 2026-10-21T09:21:43Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 4.40 |
| Market reference dc home away odds | 1.10 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-21T09:08:18Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-21T09:22:03Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.9% |
| Market under 3 5 odds | 1.99 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-21T09:08:18Z |
| Market reference under 3 5 odds | 1.94 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market reference under 3 5 last update utc | 2026-10-21T09:22:05Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 52.9% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T09:21:42Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-21T09:21:43Z |
| Market btts yes bookmakers | 2 |

</details>


---
