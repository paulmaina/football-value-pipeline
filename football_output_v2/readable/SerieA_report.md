# Serie A — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 2,000 |
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
| Training sha256 | 2c1e31ba3ab872f975373aba7d6e633a80818474aa6b5c50a381b0615bc8ddaf |
| Training as of utc | 2026-11-03T13:55:50.541698+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 100, 'bbs_added_results': 2, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 100, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 183, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-03T13:55:50.541698+00:00', 'observations': 660, 'observations_sha256': '471508faed1b3aed1039c7c802d11aec044c71d1d74caba0daa0a4c055b9856b', 'eligible_training_matches': 244, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 229, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 36, 'retrospective_eligible_training_matches': 244, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'd7d7f455a37651e8da3d5c95ba167841f01f79bdd8d0979af1f31c53f7c92a4a', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 183, 'tuning_matches': 20, 'audit_matches': 41, 'tuning_origin_utc': '2025-10-05T00:00:00+00:00', 'audit_origin_utc': '2026-10-11T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 24, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-03', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-11-04', 'audit_start_date': '2026-05-05', 'training_shot_matches': 1620, 'tuning_matches': 250, 'audit_matches': 129, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8311557681916149, 'audit_candidate_poisson_score': 0.8301742738669686, 'audit_gain': 0.000981494324646226, 'audit_gain_lower95': -0.0035199828773113204, 'audit_baseline_briers': [0.54705617518533, 0.15450301883980205, 0.20910159992114527, 0.23872498517836405], 'audit_candidate_briers': [0.549756238966395, 0.1536856602309083, 0.20921667068560446, 0.23948410674304796], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1830.795 |
| Base scoring parameter | 0.153 |
| Home-advantage parameter | 0.106 |
| Dixon-Coles low-score adjustment | -0.022 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 2000, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
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
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261103T135550541698Z_b69e6218052063a73f098f6029c3c543a745a517949956c851fa832a14e553b2.json |
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

## 2026-11-06 — Venezia FC vs Udinese Calcio

The model's most likely 1X2 outcome is **Udinese Calcio win** at **44.9%**. Expected goals are 0.95 for Venezia FC and 1.32 for Udinese Calcio (2.27 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.5%; Under 3.5 goals: 80.6%; Double Chance 1X: 55.1%; Double Chance X2: 73.5%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 45.1%; BTTS No (at least one team does not score): 54.9%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia FC win | 26.5% | 3.77 |
| Draw | 28.6% | 3.50 |
| Udinese Calcio win | 44.9% | 2.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia FC expected goals | 0.95 |
| Udinese Calcio expected goals | 1.32 |
| Expected total goals | 2.27 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 66.4% |
| Under 1.5 | 33.6% |
| Over 2.5 | 39.5% |
| Under 2.5 | 60.5% |
| Over 3.5 | 19.4% |
| Under 3.5 | 80.6% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.40% |
| 2 | 1-1 | 13.24% |
| 3 | 0-0 | 10.67% |
| 4 | 1-0 | 9.54% |
| 5 | 0-2 | 9.03% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:45:00+00:00 |
| Fixture id | fdorg:558537 |
| Matched home-team name | Venezia |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9463 |
| Dc lambda away | 1.3188 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-03T13:55:50.541698+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 45.1% |
| P btts no | 54.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.37 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.98 |
| Fair Over 2.5 odds | 2.53 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.17 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.54 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.23920938346748688, "-10": 5.097476276311147e-07, "-11": 6.054610756805419e-08, "-12": 6.60086486381134e-09, "-13": 6.62856023372856e-10, "-14": 5.7330615280734854e-11, "-2": 0.13421386983315237, "-3": 0.05372896023872843, "-4": 0.01671216190050686, "-5": 0.004236740834191765, "-6": 0.0009049247695841412, "-7": 0.0001668326498458738, "-8": 2.7040054392583487e-05, "-9": 3.908677803943773e-06, "0": 0.285638195610444, "1": 0.17082817373242468, "10": 1.8442397834546482e-08, "11": 1.571790351350883e-09, "12": 1.2295762031956275e-10, "13": 8.859720718463758e-12, "14": 5.498365994560919e-13, "2": 0.06910187526883943, "3": 0.019849386493862736, "4": 0.004430140536364821, "5": 0.0008058662822111446, "6": 0.00012350649007350975, "7": 1.6338213577783245e-05, "8": 1.9001036810072308e-06, "9": 1.9708148605207594e-07} |
| Raw goal margin distribution | {"-1": 0.23920938346748688, "-10": 5.097476276311147e-07, "-11": 6.054610756805419e-08, "-12": 6.60086486381134e-09, "-13": 6.62856023372856e-10, "-14": 5.7330615280734854e-11, "-2": 0.13421386983315237, "-3": 0.05372896023872843, "-4": 0.01671216190050686, "-5": 0.004236740834191765, "-6": 0.0009049247695841412, "-7": 0.0001668326498458738, "-8": 2.7040054392583487e-05, "-9": 3.908677803943773e-06, "0": 0.285638195610444, "1": 0.17082817373242468, "10": 1.8442397834546482e-08, "11": 1.571790351350883e-09, "12": 1.2295762031956275e-10, "13": 8.859720718463758e-12, "14": 5.498365994560919e-13, "2": 0.06910187526883943, "3": 0.019849386493862736, "4": 0.004430140536364821, "5": 0.0008058662822111446, "6": 0.00012350649007350975, "7": 1.6338213577783245e-05, "8": 1.9001036810072308e-06, "9": 1.9708148605207594e-07} |
| Unadjusted home-win probability | 26.5% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 44.9% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 45.1% |
| P home draw | 55.1% |
| P draw away | 73.5% |
| P home away | 71.4% |
| Raw p home draw | 55.1% |
| Raw p draw away | 73.5% |
| Raw p home away | 71.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.3947 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.02175182809361759, "mu": 9.549611485246825, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,353.0341 |
| Elo away rating | 1,444.2839 |
| Elo rating diff | -31.2498 |
| Elo home expectancy | 0.4551 |

</details>


---
