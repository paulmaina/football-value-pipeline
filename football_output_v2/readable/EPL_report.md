# Premier League — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,990 |
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
| Training sha256 | ce2e66bbbf4c960c0620414c73c05d6418e1f9b9968e65c6c5ae36324337f056 |
| Training as of utc | 2026-11-03T13:17:06.986183+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 90, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 90, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 226, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-03T13:17:06.986183+00:00', 'observations': 620, 'observations_sha256': '2d3e942920cb3793ec4dd4894c56c7fca9f020cb7d8750615ae91daf2e8ba533', 'eligible_training_matches': 291, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 262, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 28, 'retrospective_eligible_training_matches': 291, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'f2a93b4213fd40bb54660c3ef491d189391672e40d64982e3f4ce2b5d0a80a78', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 230, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-04T00:00:00+00:00', 'audit_origin_utc': '2025-11-02T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 12, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-03', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1989, 'tune_start_date': '2025-11-04', 'audit_start_date': '2026-05-05', 'training_shot_matches': 1619, 'tuning_matches': 249, 'audit_matches': 112, 'audit_matchdays': 37, 'selected_shrinkage': 15.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9372226592215835, 'audit_candidate_poisson_score': 0.9280344708252098, 'audit_gain': 0.009188188396373698, 'audit_gain_lower95': 0.00034981535005215036, 'audit_baseline_briers': [0.6265871414121692, 0.16782854596135227, 0.2144747150786869, 0.26036107546433057], 'audit_candidate_briers': [0.6267031563435422, 0.16714096229498757, 0.21206984635706191, 0.2571193278989171], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'market_brier_worse']} |
| Optimizer objective | 1883.366 |
| Base scoring parameter | 0.214 |
| Home-advantage parameter | 0.178 |
| Dixon-Coles low-score adjustment | -0.061 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1990, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
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
| Bbs statistics model artifact | bbs/feature_models/EPL/20261103T131706986183Z_1902d4c543c848b8810c64e65d8cf79caa16ec2baf05b1140214e085be9b4ef1.json |
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

## 2026-11-06 — Everton FC vs Coventry City FC

The model's most likely 1X2 outcome is **Everton FC win** at **49.0%**. Expected goals are 1.44 for Everton FC and 0.90 for Coventry City FC (2.33 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.2%; Double Chance 1X: 77.3%; Double Chance X2: 51.0%; Double Chance 12 (either team wins): 71.7%; Under 4.5 goals: 91.2%; BTTS Yes (both teams score): 45.9%; BTTS No (at least one team does not score): 54.1%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton FC win | 49.0% | 2.04 |
| Draw | 28.3% | 3.53 |
| Coventry City FC win | 22.7% | 4.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton FC expected goals | 1.44 |
| Coventry City FC expected goals | 0.90 |
| Expected total goals | 2.33 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 68.5% |
| Under 1.5 | 31.5% |
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
| Over 3.5 | 20.8% |
| Under 3.5 | 79.2% |
| Over 4.5 | 8.8% |
| Under 4.5 | 91.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.24% |
| 2 | 1-0 | 13.18% |
| 3 | 0-0 | 10.45% |
| 4 | 2-0 | 10.03% |
| 5 | 2-1 | 8.98% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:00:00+00:00 |
| Fixture id | fdorg:560634 |
| Matched home-team name | Everton |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.4393 |
| Dc lambda away | 0.8952 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:17:06.986183+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 45.9% |
| P btts no | 54.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.57 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.81 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.38 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.14832622886551236, "-10": 9.914492407883607e-09, "-11": 7.99135838137303e-10, "-12": 5.912478409722042e-11, "-13": 4.028561672788712e-12, "-14": 2.3589217743168443e-13, "-2": 0.05840769671611363, "-3": 0.015828586926073373, "-4": 0.0033361772998345383, "-5": 0.0005734102905033268, "-6": 8.30626081754091e-05, "-7": 1.0387862938454557e-05, "-8": 1.142268435703662e-06, "-9": 1.1203433714009246e-07, "0": 0.28331941621731627, "1": 0.24310474383552125, "10": 1.1444234724895505e-06, "11": 1.4830934161067915e-07, "12": 1.764205186477559e-08, "13": 1.9326854202980805e-09, "14": 1.8195178491391112e-10, "2": 0.1509848371149783, "3": 0.06578653722564162, "4": 0.02229336527014065, "5": 0.006160608612990355, "6": 0.0014348130802648116, "7": 0.00028850118496751156, "8": 5.1005991462016514e-05, "9": 8.043328272725245e-06} |
| Raw goal margin distribution | {"-1": 0.14832622886551236, "-10": 9.914492407883607e-09, "-11": 7.99135838137303e-10, "-12": 5.912478409722042e-11, "-13": 4.028561672788712e-12, "-14": 2.3589217743168443e-13, "-2": 0.05840769671611363, "-3": 0.015828586926073373, "-4": 0.0033361772998345383, "-5": 0.0005734102905033268, "-6": 8.30626081754091e-05, "-7": 1.0387862938454557e-05, "-8": 1.142268435703662e-06, "-9": 1.1203433714009246e-07, "0": 0.28331941621731627, "1": 0.24310474383552125, "10": 1.1444234724895505e-06, "11": 1.4830934161067915e-07, "12": 1.764205186477559e-08, "13": 1.9326854202980805e-09, "14": 1.8195178491391112e-10, "2": 0.1509848371149783, "3": 0.06578653722564162, "4": 0.02229336527014065, "5": 0.006160608612990355, "6": 0.0014348130802648116, "7": 0.00028850118496751156, "8": 5.1005991462016514e-05, "9": 8.043328272725245e-06} |
| Unadjusted home-win probability | 49.0% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.2% |
| Raw p btts yes | 45.9% |
| P home draw | 77.3% |
| P draw away | 51.0% |
| P home away | 71.7% |
| Raw p home draw | 77.3% |
| Raw p draw away | 51.0% |
| Raw p home away | 71.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4131 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.009276350512908198, "mu": 9.755607159937354, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,448.4574 |
| Elo away rating | 1,377.6232 |
| Elo rating diff | 130.8342 |
| Elo home expectancy | 0.6799 |

</details>


---
