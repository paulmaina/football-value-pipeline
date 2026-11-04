# Ligue 1 — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,761 |
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
| Training sha256 | 9c5dd7e6cbf57c2158cd2baccd61f898534fd4b01927da37f2f7cfe43aeb3a23 |
| Training as of utc | 2026-11-04T10:19:42.171114+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 81, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 81, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 139, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_CHRONOLOGICAL_PARTITIONS', 'cutoff_utc': '2026-11-04T10:19:42.171114+00:00', 'observations': 500, 'observations_sha256': '81a767a27d6d948c13f8a4f0bdbe50c914e1a76d9292173d115fc833d158bedb', 'eligible_training_matches': 183, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 180, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 23, 'retrospective_eligible_training_matches': 183, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'ac890ef39cf8deef9c097c9abe7011823f93510b6f7a80d7ba7ae5d8609967ef', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 123, 'tuning_matches': 17, 'audit_matches': 43, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-05T00:00:00+00:00', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1759, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1471, 'tuning_matches': 187, 'audit_matches': 96, 'audit_matchdays': 34, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8547715623172535, 'audit_candidate_poisson_score': 0.8530350185434455, 'audit_gain': 0.0017365437738079414, 'audit_gain_lower95': -0.004922528465493255, 'audit_baseline_briers': [0.5824611765258155, 0.17370333581411498, 0.21287609805690424, 0.24660314645935366], 'audit_candidate_briers': [0.5816251545925518, 0.17326144719684378, 0.2118685084312232, 0.2457311201596737], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1599.903 |
| Base scoring parameter | 0.200 |
| Home-advantage parameter | 0.202 |
| Dixon-Coles low-score adjustment | -0.054 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1761, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261104T101942171114Z_aedaa0e4f9af90cb3acfe88362b83bd480dc160e590c67907104abfc91558b46.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
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

## 2026-11-06 — Toulouse vs Strasbourg

The model's most likely 1X2 outcome is **Toulouse win** at **44.8%**. Expected goals are 1.50 for Toulouse and 1.39 for Strasbourg (2.89 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 55.5%; Under 3.5 goals: 67.0%; Double Chance 1X: 70.1%; Double Chance X2: 55.2%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 83.2%; BTTS Yes (both teams score): 58.8%; BTTS No (at least one team does not score): 41.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 44.8% | 2.23 |
| Draw | 25.3% | 3.95 |
| Strasbourg win | 29.9% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.50 |
| Strasbourg expected goals | 1.39 |
| Expected total goals | 2.89 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.5% |
| Under 2.5 | 44.5% |
| Over 3.5 | 33.0% |
| Under 3.5 | 67.0% |
| Over 4.5 | 16.8% |
| Under 4.5 | 83.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.86% |
| 2 | 2-1 | 9.86% |
| 3 | 1-0 | 8.73% |
| 4 | 2-0 | 7.10% |
| 5 | 1-2 | 6.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 44.8% | 47.1% | 2.08 | -6.8% |
| Draw | 25.3% | 25.0% | 3.98 | +0.6% |
| Strasbourg win | 29.9% | 28.0% | 3.51 | +4.9% |
| Over 2.5 | 55.5% | 59.5% | 1.66 | -7.8% |
| Under 2.5 | 44.5% | 40.5% | 2.42 | +7.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:45:00+00:00 |
| Fixture id | 5e7d141f719835de18877ed95bedcb32 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T10:20:05Z |
| Market best draw last update utc | 2026-11-04T10:19:45Z |
| Market best away last update utc | 2026-11-04T10:19:45Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5044 |
| Dc lambda away | 1.3887 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_CHRONOLOGICAL_PARTITIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T10:19:42.171114+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.8% |
| P btts no | 41.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.68 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.79 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 3.03 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.94 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.16026086616642535, "-10": 4.2713082698334587e-07, "-11": 5.3092757601727954e-08, "-12": 6.063633544687e-09, "-13": 6.401940912914846e-10, "-14": 6.238741434911698e-11, "-15": 5.069629530714904e-12, "-2": 0.0884632239016248, "-3": 0.0353444302293079, "-4": 0.011175787812771188, "-5": 0.0029104971118414607, "-6": 0.0006427666800571408, "-7": 0.00012304902408121922, "-8": 2.0770055916403106e-05, "-9": 3.1333486542716776e-06, "0": 0.2528744503142903, "1": 0.2268747368439151, "10": 1.2395011544892847e-06, "11": 1.6691041040696474e-07, "12": 2.065110106176472e-08, "13": 2.36202260578578e-09, "14": 2.493627036051936e-10, "15": 2.195193753691959e-11, "2": 0.13531682433378803, "3": 0.0585695844349438, "4": 0.020062794658821465, "5": 0.005660340751194285, "6": 0.001354225172904715, "7": 0.00028085219565726085, "8": 5.1356975403954906e-05, "9": 8.393297528750981e-06} |
| Raw goal margin distribution | {"-1": 0.1844540909301044, "-10": 4.916111480242484e-07, "-11": 6.110772125884586e-08, "-12": 6.979008911988803e-09, "-13": 7.368387676462852e-10, "-14": 7.180551356371596e-11, "-15": 5.8349485361532125e-12, "-2": 0.10181776709340526, "-3": 0.04068007931904783, "-4": 0.012862901784717279, "-5": 0.0033498701945233965, "-6": 0.0007397997183353532, "-7": 0.00014162469241347963, "-8": 2.3905535233093553e-05, "-9": 3.606363745660516e-06, "0": 0.2601501978585849, "1": 0.20034668287855625, "10": 1.0945685190895218e-06, "11": 1.4739387702712703e-07, "12": 1.8236405044783898e-08, "13": 2.085835560787503e-09, "14": 2.2020517222814384e-10, "15": 1.938513705606998e-11, "2": 0.1194944720160095, "3": 0.051721148517251604, "4": 0.017716888248927577, "5": 0.004998487311719852, "6": 0.0011958780648581313, "7": 0.00024801265474437773, "8": 4.5351896857236744e-05, "9": 7.411884380299804e-06} |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 34.4% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.1% |
| Raw p btts yes | 59.0% |
| P home draw | 70.1% |
| P draw away | 55.2% |
| P home away | 74.7% |
| Raw p home draw | 65.6% |
| Raw p draw away | 60.4% |
| Raw p home away | 74.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5553 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:45Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:45Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.45, "draw": 3.85, "home": 2.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:45Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.51, "draw": 3.98, "home": 2.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:45Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.66, "under": 2.42}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:05Z |
| Market reference home last update utc | 2026-11-04T10:20:05Z |
| Market reference draw last update utc | 2026-11-04T10:20:05Z |
| Market reference away last update utc | 2026-11-04T10:20:05Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:45Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:45Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:45Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:45Z |
| Home probability edge | -2.2% |
| Draw probability edge | +0.3% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | -0.0749 |
| Raw ev home | -0.1768 |
| Raw edge prob draw | 0.0104 |
| Raw ev draw | 0.0354 |
| Raw edge prob away | 0.0645 |
| Raw ev away | 0.2077 |
| Count model | {"corners": {"alpha": 0.015416351116715491, "mu": 9.118242101605375, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,453.8748 |
| Elo away rating | 1,507.0944 |
| Elo rating diff | 6.7804 |
| Elo home expectancy | 0.5098 |

</details>


---
