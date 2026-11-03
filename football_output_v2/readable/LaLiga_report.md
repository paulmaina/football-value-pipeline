# La Liga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 2,009 |
| Training data through | 2026-11-02 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 480 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 70.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | dc45d19f69e44fc0016826c1a587f5a401b1b6dd4838785fd1d2086993b07fa0 |
| Training as of utc | 2026-11-03T13:54:18.739128+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 109, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 109, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 104, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-03T13:54:18.739128+00:00', 'observations': 560, 'observations_sha256': 'bf055c762d52b8f94b2c3c643af5e3b882921f66a3a127d9db591a60039aff21', 'eligible_training_matches': 173, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 180, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 30, 'retrospective_eligible_training_matches': 173, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '3022e4a7c64dc9e365379041e969485771ef74e9a77bfd095c88cdb21e8cbc93', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 111, 'tuning_matches': 22, 'audit_matches': 40, 'tuning_origin_utc': '2026-09-13T00:00:00+00:00', 'audit_origin_utc': '2026-10-09T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 17, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8357146014438204, 'audit_candidate_poisson_score': 0.841617559215144, 'audit_gain': -0.005902957771323658, 'audit_gain_lower95': -0.034372513775192494, 'audit_baseline_briers': [0.5199253099278909, 0.20340070445316755, 0.22970209423243637, 0.28429820925953975], 'audit_candidate_briers': [0.5194276011008528, 0.21275443836559557, 0.23114059283543514, 0.2883280409411213], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-03', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2009, 'tune_start_date': '2025-11-04', 'audit_start_date': '2026-05-05', 'training_shot_matches': 1630, 'tuning_matches': 230, 'audit_matches': 129, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8430706605028037, 'audit_candidate_poisson_score': 0.8398581573253481, 'audit_gain': 0.0032125031774555834, 'audit_gain_lower95': -0.005357872607811902, 'audit_baseline_briers': [0.5720996902978099, 0.18496050558986687, 0.2035823824601455, 0.2524561512845763], 'audit_candidate_briers': [0.5744553679747051, 0.18171299017538922, 0.20415589408037946, 0.2486532130775865], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1852.309 |
| Base scoring parameter | 0.089 |
| Home-advantage parameter | 0.289 |
| Dixon-Coles low-score adjustment | -0.021 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 2009, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261103T135418739128Z_4cf4e4c7eb043426d4f83d2a28d5ae93737b4417a3c0c65d5a8a25a0fdb411ad.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'None': 1} |
| Bbs statistics applied fixtures | 0 |
| Goal market validation | SKIPPED: not required by 48h-ah-price-edge-cagey-v28 |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-06 — Sevilla FC vs Deportivo Alavés

The model's most likely 1X2 outcome is **Sevilla FC win** at **47.8%**. Expected goals are 1.52 for Sevilla FC and 1.05 for Deportivo Alavés (2.57 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 47.5%; Under 3.5 goals: 74.2%; Double Chance 1X: 74.0%; Double Chance X2: 52.2%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 88.1%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla FC win | 47.8% | 2.09 |
| Draw | 26.2% | 3.82 |
| Deportivo Alavés win | 26.0% | 3.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla FC expected goals | 1.52 |
| Deportivo Alavés expected goals | 1.05 |
| Expected total goals | 2.57 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 73.0% |
| Under 1.5 | 27.0% |
| Over 2.5 | 47.5% |
| Under 2.5 | 52.5% |
| Over 3.5 | 25.8% |
| Under 3.5 | 74.2% |
| Over 4.5 | 11.9% |
| Under 4.5 | 88.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.46% |
| 2 | 1-0 | 11.34% |
| 3 | 2-1 | 9.28% |
| 4 | 2-0 | 8.81% |
| 5 | 0-0 | 7.87% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:00:00+00:00 |
| Fixture id | fdorg:564740 |
| Matched home-team name | Sevilla |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.5208 |
| Dc lambda away | 1.0533 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:54:18.739128+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.70 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.70 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.41 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.1617325450692781, "-10": 4.0805156098930415e-08, "-11": 3.8609148807615325e-09, "-12": 3.354765117118282e-10, "-13": 2.6941215001641288e-11, "-14": 2.0021006733230364e-12, "-15": 1.2702303363352372e-13, "-2": 0.06989518776529846, "-3": 0.021832199985908213, "-4": 0.0053420710799110364, "-5": 0.0010702623108497543, "-6": 0.00018116394823084378, "-7": 2.6517809924171313e-05, "-8": 3.41671173811198e-06, "-9": 3.929757753942303e-07, "0": 0.2618577297871939, "1": 0.23463128401824496, "10": 1.6068019692756585e-06, "11": 2.1951402348203498e-07, "12": 2.7539680193217732e-08, "13": 3.1932923680082953e-09, "14": 3.4263533472770535e-10, "15": 3.138726312731884e-11, "2": 0.14571247610304366, "3": 0.065716086774185, "4": 0.02321713287994448, "5": 0.006716049492923604, "6": 0.0016414216751971672, "7": 0.00034690516942388784, "8": 6.453661597170154e-05, "9": 1.0717373351893664e-05} |
| Raw goal margin distribution | {"-1": 0.1617325450692781, "-10": 4.0805156098930415e-08, "-11": 3.8609148807615325e-09, "-12": 3.354765117118282e-10, "-13": 2.6941215001641288e-11, "-14": 2.0021006733230364e-12, "-15": 1.2702303363352372e-13, "-2": 0.06989518776529846, "-3": 0.021832199985908213, "-4": 0.0053420710799110364, "-5": 0.0010702623108497543, "-6": 0.00018116394823084378, "-7": 2.6517809924171313e-05, "-8": 3.41671173811198e-06, "-9": 3.929757753942303e-07, "0": 0.2618577297871939, "1": 0.23463128401824496, "10": 1.6068019692756585e-06, "11": 2.1951402348203498e-07, "12": 2.7539680193217732e-08, "13": 3.1932923680082953e-09, "14": 3.4263533472770535e-10, "15": 3.138726312731884e-11, "2": 0.14571247610304366, "3": 0.065716086774185, "4": 0.02321713287994448, "5": 0.006716049492923604, "6": 0.0016414216751971672, "7": 0.00034690516942388784, "8": 6.453661597170154e-05, "9": 1.0717373351893664e-05} |
| Unadjusted home-win probability | 47.8% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 26.0% |
| Raw p over 1 5 | 73.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 51.1% |
| P home draw | 74.0% |
| P draw away | 52.2% |
| P home away | 73.8% |
| Raw p home draw | 74.0% |
| Raw p draw away | 52.2% |
| Raw p home away | 73.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4751 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.014493407444055235, "mu": 8.663289582047497, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,445.5951 |
| Elo away rating | 1,433.5816 |
| Elo rating diff | 72.0135 |
| Elo home expectancy | 0.6022 |

</details>


---
