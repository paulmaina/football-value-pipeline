# La Liga — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 2,004 |
| Training data through | 2026-10-31 |
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
| Training sha256 | 8e0750cb21f26836fd5b8ef1907e968cc25a81d205ddb367baeb890b340dfcf8 |
| Training as of utc | 2026-11-01T07:04:15.227758+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 104, 'bbs_added_results': 5, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 104, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 96, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-01T07:04:15.227758+00:00', 'observations': 519, 'observations_sha256': '607d727d878090cff21e293a0c106ba3db271a095df300c5ec7253a2a505be40', 'eligible_training_matches': 159, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 170, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 25, 'retrospective_eligible_training_matches': 159, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'a89c80aa493ee5c28b0fa6f6068c73904c961404b4f23d552b288bf02cafa168', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 98, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2026-09-07T00:00:00+00:00', 'audit_origin_utc': '2026-09-20T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 16, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.81566316597144, 'audit_candidate_poisson_score': 0.8171150995388455, 'audit_gain': -0.0014519335674055833, 'audit_gain_lower95': -0.033780820348136155, 'audit_baseline_briers': [0.5338582914629132, 0.1892500148937949, 0.21760641211297527, 0.2581747697513749], 'audit_candidate_briers': [0.5192216002025969, 0.1973653006738318, 0.22443935135744503, 0.2576780810889695], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1625, 'tuning_matches': 230, 'audit_matches': 126, 'audit_matchdays': 54, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8491525262315384, 'audit_candidate_poisson_score': 0.8475058774342524, 'audit_gain': 0.0016466487972859323, 'audit_gain_lower95': -0.007030154984636702, 'audit_baseline_briers': [0.5766350587773638, 0.1857604561983157, 0.1974067419906521, 0.24384262372212184], 'audit_candidate_briers': [0.5791487086963687, 0.18239887047145073, 0.19919949348313332, 0.2419152365030378], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1844.848 |
| Base scoring parameter | 0.091 |
| Home-advantage parameter | 0.289 |
| Dixon-Coles low-score adjustment | -0.026 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 2004, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-31'} |
| Training data health | {'training_end': '2026-10-31', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 2.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261101T070415227758Z_1b59a95250d70525562f483cac7897f61e5f58e84885718d48b478357eaabb59.json |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 3, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1, 'ANCHORED_MAIN': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 5} |
| Legacy comparison status | {'AVAILABLE': 5} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-01 — Athletic Bilbao vs Real Sociedad

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **47.7%**. Expected goals are 1.54 for Athletic Bilbao and 1.04 for Real Sociedad (2.58 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.9%; Under 3.5 goals: 67.9%; Double Chance 1X: 74.0%; Double Chance X2: 52.3%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 56.9%; BTTS No (at least one team does not score): 43.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 47.7% | 2.10 |
| Draw | 26.4% | 3.79 |
| Real Sociedad win | 26.0% | 3.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.54 |
| Real Sociedad expected goals | 1.04 |
| Expected total goals | 2.58 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.45% |
| 2 | 2-1 | 9.14% |
| 3 | 1-0 | 8.97% |
| 4 | 2-0 | 7.93% |
| 5 | 1-2 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 47.7% | 47.2% | 2.07 | -1.4% |
| Draw | 26.4% | 26.5% | 3.62 | -4.5% |
| Real Sociedad win | 26.0% | 26.3% | 3.65 | -5.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T20:00:00+00:00 |
| Fixture id | 3757bcd765c7da1538cdf2785e784038 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:04:27Z |
| Market best draw last update utc | 2026-11-01T07:04:27Z |
| Market best away last update utc | 2026-11-01T07:04:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5447 |
| Dc lambda away | 1.0387 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:04:15.227758+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.9% |
| P btts no | 43.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.50 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.58 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.26 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.15636664786787094, "-10": 7.962224729354138e-08, "-11": 8.22409764329726e-09, "-12": 7.804029992194352e-10, "-13": 6.847717689181908e-11, "-14": 5.58579905494155e-12, "-15": 4.2318649231627737e-13, "-16": 2.7141860523279403e-14, "-2": 0.0714062313119758, "-3": 0.023848733305129117, "-4": 0.006289471821120888, "-5": 0.0013643385510400089, "-6": 0.00025076557199855574, "-7": 3.993132537956386e-05, "-8": 5.604391482273006e-06, "-9": 7.028057079878087e-07, "0": 0.26392015736882446, "1": 0.21668850593972142, "10": 3.900620463983639e-06, "11": 5.991441650037927e-07, "12": 8.454848272802667e-08, "13": 1.1032566358744363e-08, "14": 1.3383195482535199e-09, "15": 1.5078221635858528e-10, "16": 1.4381419430262834e-11, "2": 0.14624629651217494, "3": 0.07263699915958732, "4": 0.028487252501453456, "5": 0.00918972155376882, "6": 0.0025118397299584245, "7": 0.000594814506751431, "8": 0.00012414810741121548, "9": 2.3152118220668655e-05} |
| Raw goal margin distribution | {"-1": 0.15751724515281793, "-10": 3.518183777026401e-08, "-11": 3.282775489754179e-09, "-12": 2.8129487824592483e-10, "-13": 2.2277491695179488e-11, "-14": 1.6325970245938756e-12, "-15": 1.0213181219221085e-13, "-2": 0.067397602379649, "-3": 0.02075751920257934, "-4": 0.005008346194268176, "-5": 0.0009894558143028714, "-6": 0.00016516139640024232, "-7": 2.3840260235212616e-05, "-8": 3.0291610485326354e-06, "-9": 3.435764903837594e-07, "0": 0.2611084597587277, "1": 0.23576492366115515, "10": 1.8610440194278975e-06, "11": 2.5823976543995453e-07, "12": 3.2906945617979175e-08, "13": 3.875572375204343e-09, "14": 4.2236932952597813e-10, "15": 3.929327465735719e-11, "2": 0.14905003141353768, "3": 0.06826638183457866, "4": 0.024494557079652476, "5": 0.007196402849853355, "6": 0.0017863700156827414, "7": 0.00038345789030511346, "8": 7.245575110204418e-05, "9": 1.2221309727570762e-05} |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 25.2% |
| Raw p over 1 5 | 73.3% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 51.1% |
| P home draw | 74.0% |
| P draw away | 52.3% |
| P home away | 73.6% |
| Raw p home draw | 74.8% |
| Raw p draw away | 51.3% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1100 |
| Totals anchor target over 2 5 | 0.5392 |
| Totals anchor reference over odds | 1.80 |
| Totals anchor reference under odds | 2.09 |
| Totals anchor reference last update utc | 2026-11-01T07:04:27Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4761 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.68, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.05, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.08, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.23, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.29, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 6.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:42Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.05, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.07 |
| Reference draw odds | 3.62 |
| Reference away odds | 3.65 |
| Market reference 1x2 last update utc | 2026-11-01T07:04:27Z |
| Market reference home last update utc | 2026-11-01T07:04:27Z |
| Market reference draw last update utc | 2026-11-01T07:04:27Z |
| Market reference away last update utc | 2026-11-01T07:04:27Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-01T07:04:05Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:04:05Z |
| Home probability edge | +0.5% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Market p over 1 5 | 80.7% |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.29 |
| Market reference over 1 5 last update utc | 2026-11-01T07:04:42Z |
| Market over 1 5 bookmakers | 0 |
| Raw edge prob home | 0.0150 |
| Raw ev home | 0.0081 |
| Raw edge prob draw | -0.0040 |
| Raw ev draw | -0.0548 |
| Raw edge prob away | -0.0110 |
| Raw ev away | -0.0807 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.1066742059320717, 0.09669976820201141, 0.04430048325912437, 0.0131754441504201, 0.002938889981382174, 0.0005244346512534456, 7.798627633155299e-05, 9.940270425127835e-06, 1.1086290841931975e-06, 1.0990610416054105e-07, 9.80618018557985e-09, 7.953993635710883e-10, 5.91400991650137e-11, 4.058978504597429e-12, 2.586823341452121e-13], [0.1422865566354065, 0.12640562971364877, 0.059049998934142554, 0.017562110067476936, 0.003917371493513811, 0.0006990412591303976, 0.00010395122570829882, 1.3249809366086121e-05, 1.4777388737962425e-06, 1.464985222751267e-07, 1.307107478082047e-08, 1.0602216525802024e-09, 7.883035433794883e-11, 5.41038514113318e-12, 3.448086890205677e-13], [0.09652336888814957, 0.08612129004716515, 0.036858608574277765, 0.011704641851194842, 0.002610815565640436, 0.0004658909177708542, 6.92805057156298e-05, 8.83061731368167e-06, 9.84870508208694e-07, 9.763705661628348e-08, 8.711495847131334e-09, 7.06607274333978e-10, 5.253816659748516e-11, 3.6058662718020395e-12, 2.2980508587289464e-13], [0.04288670168393808, 0.03826491053341315, 0.017070599050969755, 0.004870638670984028, 0.0011600223821979568, 0.00020700194199446155, 3.078231122021442e-05, 3.923568507598789e-06, 4.3759193415430406e-07, 4.338152893578098e-08, 3.870641150639073e-09, 3.1395563303616126e-10, 2.3343452511467573e-11, 1.6021375226775166e-12, 1.0210565873123602e-13], [0.014291377330538677, 0.012751231814992211, 0.005688531939193471, 0.0016918310896143016, 0.000362039049065197, 6.89804238852224e-05, 1.0257763070619118e-05, 1.3074728487528646e-06, 1.458212266797277e-07, 1.4456271404735317e-08, 1.2898355672712088e-09, 1.046212051893077e-10, 7.778870254408895e-12, 5.338893170368041e-13, 3.4025244171617326e-14], [0.0038099169762980997, 0.0033993318794291547, 0.0015164972489415231, 0.00045102272791977874, 0.00010060428789543556, 1.72228449731815e-05, 2.7346017642459395e-06, 3.485572375076753e-07, 3.887426342347979e-08, 3.8538758417064236e-09, 3.4385534093196047e-10, 2.7890811117257527e-11, 2.0737574240211933e-12, 1.4232875708180945e-13, 9.070739117294484e-15], [0.0008464000722581924, 0.0007551856815457526, 0.0003369006172755575, 0.0001001978971920565, 2.2349955937076075e-05, 3.988271565673883e-06, 5.689732873508536e-07, 7.743446191818779e-08, 8.636193275420828e-09, 8.561658459192621e-10, 7.638990225292641e-11, 6.1961414623590735e-12, 4.60699916679803e-13, 3.1619342633422396e-14, 2.0151290151663805e-15], [0.0001611718095790759, 0.00014380273212666732, 6.415273806598346e-05, 1.9079720023388322e-05, 4.255886737793572e-06, 7.5944812199443e-07, 1.129340537658598e-07, 1.3809733027794968e-08, 1.6445070643255124e-09, 1.6303141175124367e-10, 1.4546192968562458e-11, 1.1798715106816762e-12, 8.772664568199962e-14, 6.020966723612168e-15, 3.837215999322276e-16], [2.6854095270783647e-05, 2.3960097481153105e-05, 1.0688989249452503e-05, 3.1790213225630156e-06, 7.091065628465255e-07, 1.265375891386891e-07, 1.8816825641311947e-08, 2.398426290055379e-09, 2.566225371536869e-10, 2.716393812746913e-11, 2.4236549358424045e-12, 1.965876168908051e-13, 1.4616822303374715e-14, 1.0032003390690372e-15, 6.393485578494955e-17], [3.977218457168693e-06, 3.5486037037069902e-06, 1.5830898379828244e-06, 4.708280860828825e-07, 1.0502203412233414e-07, 1.8740815133532394e-08, 2.7868608303990375e-09, 3.552182716557599e-10, 3.961716234589776e-11, 3.767899071779022e-12, 3.5895475336038455e-13, 2.911555539164144e-14, 2.164820481343308e-15, 1.485787126525984e-16, 9.46905438147347e-18], [5.301403695371452e-07, 4.7300848547387526e-07, 2.110167798819297e-07, 6.275867876821012e-08, 1.3998833752469282e-08, 2.4980429833846533e-09, 3.714725369971491e-10, 4.7348554732391785e-11, 5.2807401233420595e-12, 5.235164603886927e-13, 4.4811424178830725e-14, 3.880936252516574e-15, 2.885581323531116e-16, 1.9804688748999468e-17, 1.2621705453251021e-18], [6.424060488953666e-08, 5.73175577088292e-08, 2.5570294888677704e-08, 7.604883004208667e-09, 1.6963310090718875e-09, 3.027043430644624e-10, 4.5013777195240724e-11, 5.737536643945503e-12, 6.399021075948659e-13, 6.343794213287573e-14, 5.660139588322431e-15, 4.404461944891802e-16, 3.496649195823981e-17, 2.399864749020181e-18, 1.5294552907984063e-19], [7.135752951924631e-09, 6.366750940797973e-09, 2.84031116374473e-09, 8.447393426577505e-10, 1.8842598114136963e-10, 3.362395813826565e-11, 5.000064897435829e-12, 6.373172250511972e-13, 7.107939536161787e-14, 7.046594340403274e-15, 6.287200726881041e-16, 5.099677307743819e-17, 3.637641161635999e-18, 2.6657348567136344e-19, 1.6988966907951837e-20], [7.316575927465823e-10, 6.528087082533972e-10, 2.912285841056486e-10, 8.661453922400706e-11, 1.932007746086885e-11, 3.4476003353535303e-12, 5.126768641069436e-13, 6.534671110931923e-14, 7.28805770807089e-15, 7.225157999297853e-16, 6.446521032799529e-17, 5.22890527167402e-18, 3.887832835355626e-19, 2.5598978550102965e-20, 1.7419474461725562e-21], [6.966125245040409e-11, 6.215403581988524e-11, 2.772792644985791e-11, 8.246586029551136e-12, 1.8394680882223833e-12, 3.2824665484247017e-13, 4.881205745705305e-14, 6.2216722473986455e-15, 6.938972996496812e-16, 6.879086069396842e-17, 6.137744397716225e-18, 4.978450217429716e-19, 3.701612712197793e-20, 2.5405379164537875e-21, 1.5533025337935388e-22]] |
| Legacy trial inputs | {"lambda_home": 1.3329425457673825, "lambda_away": 0.8922325343509482, "rho": -0.019663736715803168, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4694 |
| Legacy p draw | 0.2752 |
| Legacy p away | 0.2554 |
| Legacy p over 1 5 | 0.6543 |
| Legacy p under 3 5 | 0.8141 |
| Legacy p btts yes | 0.4348 |
| Legacy p over 2 5 | 0.3871 |
| Legacy goal margin distribution | {"-1": 0.16868622550169202, "-10": 1.0920576167524386e-08, "-11": 8.779376898395704e-10, "-12": 6.478028939201978e-11, "-13": 4.403787193617996e-12, "-14": 2.586823341452121e-13, "-2": 0.06469102595622209, "-3": 0.01759083609094797, "-4": 0.003711285067422862, "-5": 0.0006376688926212069, "-6": 9.226565592794679e-05, "-7": 1.1519623723656678e-05, "-8": 1.2641609811626321e-06, "-9": 1.2370767262826312e-07, "0": 0.2751889278284767, "1": 0.24727498475524332, "10": 5.903866924170313e-07, "11": 7.090683100046984e-08, "12": 7.816289586627886e-09, "13": 7.938116285664676e-10, "14": 6.966125245040409e-11, "2": 0.14095096267012378, "3": 0.0572590139042472, "4": 0.01804741777192664, "5": 0.004632541982967956, "6": 0.001001376928324596, "7": 0.00018677948605084577, "8": 3.0621512559770306e-05, "9": 4.476661625198019e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4668 |
| Legacy raw p draw | 0.2853 |
| Legacy raw p away | 0.2480 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3329 |
| Legacy lambda away | 0.8922 |
| Legacy model home team | Ath Bilbao |
| Legacy model away team | Sociedad |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 71.4% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:04:11Z |
| Market reference home draw last update utc | 2026-11-01T07:04:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.9% |
| Market draw away odds | 1.82 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:04:11Z |
| Market reference draw away last update utc | 2026-11-01T07:04:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.6% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:04:11Z |
| Market reference home away last update utc | 2026-11-01T07:04:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home away odds | 1.29 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:11Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.1, "price": 1.72, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:11Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.72, "price": 2.1, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:11Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.16, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:11Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.16, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p under 3 5 | 66.5% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:04:27Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.76 |
| Market reference under 3 5 last update utc | 2026-11-01T07:04:42Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.6% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:04:11Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.32 |
| Market reference btts yes last update utc | 2026-11-01T07:04:28Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 10.303210650139496, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,505.1233 |
| Elo away rating | 1,510.6645 |
| Elo rating diff | 54.4588 |
| Elo home expectancy | 0.5777 |

</details>


---

## 2026-11-01 — Elche CF vs Valencia

The model's most likely 1X2 outcome is **Elche CF win** at **42.7%**. Expected goals are 1.49 for Elche CF and 1.06 for Valencia (2.56 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 48.8%; Under 3.5 goals: 72.6%; Double Chance 1X: 70.8%; Double Chance X2: 57.3%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 53.7%; BTTS No (at least one team does not score): 46.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 42.7% | 2.34 |
| Draw | 28.1% | 3.56 |
| Valencia win | 29.2% | 3.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elche CF expected goals | 1.49 |
| Valencia expected goals | 1.06 |
| Expected total goals | 2.56 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 74.5% |
| Under 1.5 | 25.5% |
| Over 2.5 | 48.8% |
| Under 2.5 | 51.2% |
| Over 3.5 | 27.4% |
| Under 3.5 | 72.6% |
| Over 4.5 | 12.8% |
| Under 4.5 | 87.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.39% |
| 2 | 1-0 | 9.52% |
| 3 | 2-1 | 8.43% |
| 4 | 0-1 | 8.10% |
| 5 | 0-0 | 7.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 42.7% | 40.9% | 2.38 | +1.6% |
| Draw | 28.1% | 28.8% | 3.35 | -5.8% |
| Valencia win | 29.2% | 30.3% | 3.19 | -6.9% |
| Over 2.5 | 48.8% | 48.8% | 1.99 | -2.9% |
| Under 2.5 | 51.2% | 51.2% | 1.90 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T17:30:00+00:00 |
| Fixture id | 5262991e389930615bec34b642428c93 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:04:27Z |
| Market best draw last update utc | 2026-11-01T07:04:27Z |
| Market best away last update utc | 2026-11-01T07:04:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Elche |
| Matched away-team name | Valencia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4933 |
| Dc lambda away | 1.0643 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:04:15.227758+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.7% |
| P btts no | 46.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.62 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.92 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.82 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.17760782527819127, "-10": 6.79153830483673e-08, "-11": 6.7490657369164644e-09, "-12": 6.159868465789626e-10, "-13": 5.196488158539046e-11, "-14": 4.054309192552198e-12, "-15": 2.6847909061237046e-13, "-2": 0.07995398984382181, "-3": 0.026055446816134732, "-4": 0.006668678225135779, "-5": 0.0013995532342735975, "-6": 0.00024839086976093805, "-7": 3.814399327550118e-05, "-8": 5.158231868021928e-06, "-9": 6.228607534720153e-07, "0": 0.2811523494885788, "1": 0.20737100625611715, "10": 1.6616780460193906e-06, "11": 2.3168358576023023e-07, "12": 2.9668523041475844e-08, "13": 3.5116183560961063e-09, "14": 3.8440330677400864e-10, "15": 3.571524201312963e-11, "2": 0.13026742410783154, "3": 0.05956170075730981, "4": 0.021388543336847584, "5": 0.006298015832665675, "6": 0.001568277220871986, "7": 0.0003378984843166982, "8": 6.411118837581496e-05, "9": 1.0861675254742499e-05} |
| Raw goal margin distribution | {"-1": 0.16469532743093415, "-10": 4.5986482003766835e-08, "-11": 4.3971363768449995e-09, "-12": 3.8610061132159703e-10, "-13": 3.1333662389759896e-11, "-14": 2.3532092351953163e-12, "-15": 1.5097636820440563e-13, "-2": 0.07228391967077487, "-3": 0.022833145398064917, "-4": 0.005648476435332043, "-5": 0.0011439231814399087, "-6": 0.00019571368115139617, "-7": 2.895357275944017e-05, "-8": 3.7702389482204515e-06, "-9": 4.3823663045675965e-07, "0": 0.26547562377480355, "1": 0.2323532218817304, "10": 1.359436700654824e-06, "11": 1.8237765157266563e-07, "12": 2.246855036132803e-08, "13": 2.5583420201743816e-09, "14": 2.6957577894944974e-10, "15": 2.4266222705221727e-11, "2": 0.1422942841831581, "3": 0.06306441670255508, "4": 0.021888844833075276, "5": 0.006219582926094985, "6": 0.0014929953930055066, "7": 0.0003098933979241955, "8": 5.661766028300559e-05, "9": 9.233462690884495e-06} |
| Unadjusted home-win probability | 46.8% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 72.7% |
| Raw p under 3 5 | 74.5% |
| Raw p btts yes | 51.1% |
| P home draw | 70.8% |
| P draw away | 57.3% |
| P home away | 71.9% |
| Raw p home draw | 73.3% |
| Raw p draw away | 53.2% |
| Raw p home away | 73.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0403 |
| Totals anchor target over 2 5 | 0.4879 |
| Totals anchor reference over odds | 1.99 |
| Totals anchor reference under odds | 1.90 |
| Totals anchor reference last update utc | 2026-11-01T07:04:27Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4644 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:05Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:05Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.23, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:28Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.26, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:28Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.68, "price": 2.26, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.38 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.19 |
| Market reference 1x2 last update utc | 2026-11-01T07:04:27Z |
| Market reference home last update utc | 2026-11-01T07:04:27Z |
| Market reference draw last update utc | 2026-11-01T07:04:27Z |
| Market reference away last update utc | 2026-11-01T07:04:27Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.90 |
| Market reference over 2 5 last update utc | 2026-11-01T07:04:27Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:04:27Z |
| Market best over 2 5 last update utc | 2026-11-01T07:04:27Z |
| Market best under 2 5 last update utc | 2026-11-01T07:04:27Z |
| Home probability edge | +1.7% |
| Draw probability edge | -0.7% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Market p over 1 5 | 75.5% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:04:27Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.59 |
| Market reference over 1 5 last update utc | 2026-11-01T07:04:27Z |
| Market over 1 5 bookmakers | 1 |
| Raw edge prob home | 0.0583 |
| Raw ev home | 0.1131 |
| Raw edge prob draw | -0.0224 |
| Raw ev draw | -0.1107 |
| Raw edge prob away | -0.0359 |
| Raw ev away | -0.1488 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09437974616653579, 0.0966554423316362, 0.05655583870904873, 0.021515481507407383, 0.0061388349336978865, 0.0014012345233441407, 0.00026653512849176446, 4.345615457753276e-05, 6.199493135045317e-06, 7.86155670496231e-07, 8.97229261024052e-08, 9.309055526896862e-09, 8.853586853815542e-10, 7.772679800609812e-11, 6.336327537917799e-12], [0.11470350520054931, 0.1344705480218991, 0.07119897623726996, 0.027086155762980915, 0.007728269486328873, 0.0017640347275843604, 0.00033554498904189326, 5.4707591430941876e-05, 7.804632987161196e-06, 9.897029233429197e-07, 1.1295350982888691e-07, 1.171930676619798e-08, 1.1145910562167335e-09, 9.785140792810544e-11, 7.976895827231149e-12], [0.07385849384225673, 0.08429374020619654, 0.04736978223390967, 0.017049579712261585, 0.004864615997855503, 0.0011103846173790605, 0.00021121125817117782, 3.443609529272792e-05, 4.9126835643991275e-06, 6.229757751764619e-07, 7.109941648638692e-08, 7.376803730702217e-09, 7.015875278068495e-10, 6.159328750916311e-11, 5.02111567447535e-12], [0.030993847661768315, 0.03537287598053873, 0.020185302076547437, 0.007562233062247784, 0.002041378849297256, 0.0004659598359874429, 8.863231863608072e-05, 1.4450702093227723e-05, 2.0615498378650285e-06, 2.6142445192599296e-07, 2.983603332239794e-08, 3.0955888641387282e-09, 2.944129486946187e-10, 2.5846898179695798e-11, 2.1070520966644584e-12], [0.009754652541377385, 0.011132858312555272, 0.00635289333380655, 0.00241682489663401, 0.0006790804914516557, 0.00014665092078585036, 2.789513201673546e-05, 4.548050291680014e-06, 6.488288445036159e-07, 8.22777708075172e-08, 9.390255170930412e-09, 9.74270574926984e-10, 9.26601966151149e-11, 8.13475996161321e-12, 6.631497100276399e-13], [0.0024560550788374495, 0.002803063777468818, 0.0015995501502101641, 0.0006085152737998595, 0.00017362264559151152, 3.9027652076781817e-05, 7.023518303079423e-06, 1.1451214659165675e-06, 1.6336403291452598e-07, 2.0716138889626935e-08, 2.3643060382022282e-09, 2.4530470804175067e-10, 2.3330256566011408e-11, 2.0481937653950006e-12, 1.669697825149788e-13], [0.0005153273036204824, 0.0005881363617476314, 0.0003356161972978685, 0.00012767813635824218, 3.642934988350474e-05, 8.315268820724062e-06, 1.557618522603579e-06, 2.4026837282006023e-07, 3.427689684803771e-08, 4.346641932994455e-09, 4.960766010903523e-10, 5.1469616805336895e-11, 4.895133790984669e-12, 4.297502036936789e-13, 3.503345203897892e-14], [9.267901620365619e-05, 0.00010577335805306172, 6.03588802088505e-05, 2.2962268805211107e-05, 6.551634823968997e-06, 1.4954591545205521e-06, 2.844580198845324e-07, 4.5672649081170716e-08, 6.164527002686989e-09, 7.817216268365276e-10, 8.921687445570872e-11, 9.256550965540956e-12, 8.803651208588925e-13, 7.728840643961559e-14, 6.300589637652355e-15], [1.4584371885819824e-05, 1.664495430193151e-05, 9.498335131688615e-06, 3.6134421934460175e-06, 1.0309936666017613e-06, 2.3533193750842823e-07, 4.47635475411562e-08, 7.298293671062296e-09, 1.0253388360501513e-09, 1.230151050796569e-10, 1.403955424702948e-11, 1.4566510003174599e-12, 1.3853807305956578e-13, 1.216243879305742e-14, 9.914881074432428e-16], [2.040053336935041e-06, 2.3282863898857477e-06, 1.3286215157177095e-06, 5.054461626646216e-07, 1.4421478596241825e-07, 3.291809261036753e-08, 6.261498626702958e-09, 1.0208810138788902e-09, 1.4563978103374126e-10, 1.818752349498762e-11, 1.963844566976564e-12, 2.0375548273262886e-13, 1.9378623944203584e-14, 1.7012747644737005e-15, 1.3868877164930408e-16], [2.568253117179247e-07, 2.931113942096157e-07, 1.6726211454941362e-07, 6.363135999081174e-08, 1.815541127702938e-08, 4.144107040122133e-09, 7.882692611558663e-10, 1.2852021065795576e-10, 1.8334806000080532e-11, 2.3250306743514547e-12, 2.6131524467125784e-13, 2.5651077067260965e-14, 2.4396034383158875e-15, 2.1417597951641677e-16, 1.7459733216643228e-17], [2.939283255037831e-08, 3.3545658217962434e-08, 1.9142612120618273e-08, 7.282404902585917e-09, 2.0778285441548643e-09, 4.742797486991328e-10, 9.021488669781974e-11, 1.470872557669708e-11, 2.098359694374416e-12, 2.660922976344463e-13, 3.036876849340121e-14, 3.102919832320278e-15, 2.792047827065536e-16, 2.4511753378706904e-17, 1.9982104231794656e-18], [3.083589060047562e-09, 3.5192601637051876e-09, 2.0082429692579126e-09, 7.639938767371925e-10, 2.1798407337669218e-10, 4.975647862396744e-11, 9.464403854171817e-12, 1.5430858933995839e-12, 2.201379872636472e-13, 2.7915625230816272e-14, 3.1859740680951743e-15, 3.30555531295322e-16, 3.095987811070122e-17, 2.5715172034412058e-18, 2.0963137152665828e-19], [2.9861350538794033e-10, 3.40803717159359e-10, 1.94477429074658e-10, 7.398485504546971e-11, 2.1109488651757005e-11, 4.818397071830924e-12, 9.165290044380257e-13, 1.4943180779595322e-13, 2.131807279301657e-14, 2.7033377479752444e-15, 3.085284277582378e-16, 3.201086266791549e-17, 3.0444651670310234e-18, 2.63210806964035e-19, 2.0300616415434928e-20], [2.6852066356706298e-11, 3.0645914744835415e-11, 1.7487892329618854e-11, 6.65290149717549e-12, 1.8982175280274832e-12, 4.332822044926455e-13, 8.241655920097491e-14, 1.3437278443004964e-14, 1.9169739308726326e-15, 2.4309082905984274e-16, 2.774364074502119e-17, 2.8784960927255933e-18, 2.7376585188132447e-19, 2.403426252149626e-20, 1.9294735274375654e-21]] |
| Legacy trial inputs | {"lambda_home": 1.2589146914353582, "lambda_away": 1.141287018203037, "rho": -0.019663736715803168, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-11-01T07:04:27Z", "over": 1.99, "under": 1.9, "bookmaker": "pinnacle", "event_id": "5262991e389930615bec34b642428c93", "kickoff_utc": "2026-11-01T17:30:00Z", "home_team": "Elche CF", "away_team": "Valencia"}} |
| Legacy p home | 0.3987 |
| Legacy p draw | 0.2845 |
| Legacy p away | 0.3168 |
| Legacy p over 1 5 | 0.6943 |
| Legacy p under 3 5 | 0.7786 |
| Legacy p btts yes | 0.4906 |
| Legacy p over 2 5 | 0.4294 |
| Legacy goal margin distribution | {"-1": 0.18709929812745862, "-10": 1.0217033044429975e-07, "-11": 1.0487346922719422e-08, "-12": 9.88231208984135e-10, "-13": 8.570369383332927e-11, "-14": 6.336327537917799e-12, "-2": 0.08900164563221949, "-3": 0.030447483781411048, "-4": 0.008129201672003455, "-5": 0.0017733618519557557, "-6": 0.0003264264684723241, "-7": 5.19145974100751e-05, "-8": 7.2634858071625955e-06, "-9": 9.067886987342589e-07, "0": 0.2845020219630832, "1": 0.2217816021986486, "10": 2.9245509597771854e-07, "11": 3.311322304465533e-08, "12": 3.4418806695365402e-09, "13": 3.2925942013277573e-10, "14": 2.6852066356706298e-11, "2": 0.11623074904247258, "3": 0.04386072761979889, "4": 0.01291735949990935, "5": 0.0031083122136599138, "6": 0.0006311230822746757, "7": 0.00011071835189628527, "8": 1.708742568004458e-05, "9": 2.3530928799128682e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3879 |
| Legacy raw p draw | 0.2811 |
| Legacy raw p away | 0.3309 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2589 |
| Legacy lambda away | 1.1413 |
| Legacy model home team | Elche |
| Legacy model away team | Valencia |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 69.6% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:04:28Z |
| Market reference home draw last update utc | 2026-11-01T07:04:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.3% |
| Market draw away odds | 1.63 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:04:28Z |
| Market reference draw away last update utc | 2026-11-01T07:04:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.1% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:04:28Z |
| Market reference home away last update utc | 2026-11-01T07:04:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.39 |
| Market reference dc draw away odds | 1.63 |
| Market reference dc home away odds | 1.36 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:28Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.24, "price": 1.64, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:28Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.64, "price": 2.24, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:28Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.06, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:28Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.06, "price": 1.76, "quote_source": "The Odds API", "side": "Under"}] |
| Market p under 3 5 | 73.2% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:04:27Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.32 |
| Market reference under 3 5 last update utc | 2026-11-01T07:04:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.4% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:04:28Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.15 |
| Market reference btts yes last update utc | 2026-11-01T07:04:28Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 9.234617494310402, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,471.9746 |
| Elo away rating | 1,446.4037 |
| Elo rating diff | 85.5709 |
| Elo home expectancy | 0.6207 |

</details>


---

## 2026-11-01 — Getafe vs Sevilla

The model's most likely 1X2 outcome is **Sevilla win** at **37.3%**. Expected goals are 1.03 for Getafe and 0.92 for Sevilla (1.94 combined). The most likely exact score is 1-1 at 14.4%. Goal-market probabilities: at least one goal: 86.7%; Over 2.5 goals: 34.3%; Under 3.5 goals: 84.2%; Double Chance 1X: 62.7%; Double Chance X2: 69.4%; Double Chance 12 (either team wins): 68.0%; Under 4.5 goals: 94.0%; BTTS Yes (both teams score): 42.6%; BTTS No (at least one team does not score): 57.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 30.6% | 3.26 |
| Draw | 32.0% | 3.12 |
| Sevilla win | 37.3% | 2.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 1.03 |
| Sevilla expected goals | 0.92 |
| Expected total goals | 1.94 |
| Over 0.5 | 86.7% |
| Under 0.5 | 13.3% |
| Over 1.5 | 61.9% |
| Under 1.5 | 38.1% |
| Over 2.5 | 34.3% |
| Under 2.5 | 65.7% |
| Over 3.5 | 15.8% |
| Under 3.5 | 84.2% |
| Over 4.5 | 6.0% |
| Under 4.5 | 94.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.41% |
| 2 | 0-1 | 13.99% |
| 3 | 0-0 | 13.28% |
| 4 | 1-0 | 10.82% |
| 5 | 1-2 | 7.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 30.6% | 28.0% | 3.44 | +5.4% |
| Draw | 32.0% | 32.0% | 3.02 | -3.3% |
| Sevilla win | 37.3% | 40.0% | 2.43 | -9.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:00:00+00:00 |
| Fixture id | ddcc9a51a2d7368e055d1abefacdb74e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:04:27Z |
| Market best draw last update utc | 2026-11-01T07:04:27Z |
| Market best away last update utc | 2026-11-01T07:04:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Getafe |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0250 |
| Dc lambda away | 0.9158 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:04:15.227758+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 42.6% |
| P btts no | 57.4% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.53 |
| Fair Over 1.5 odds | 1.62 |
| Fair Under 1.5 odds | 2.63 |
| Fair Over 2.5 odds | 2.92 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.33 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.69 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.23382592446967623, "-10": 3.8563778396153997e-08, "-11": 3.4282440881496404e-09, "-12": 2.7890761355363225e-10, "-13": 1.951976015509018e-11, "-2": 0.1005086980906681, "-3": 0.030413036080735027, "-4": 0.007122364459760901, "-5": 0.0013565114151545502, "-6": 0.00021738778689570716, "-7": 3.0044577649573186e-05, "-8": 3.64840523022142e-06, "-9": 3.949629508126754e-07, "0": 0.3200894673933501, "1": 0.1806324871936832, "10": 8.193416353935094e-08, "11": 8.152057791561103e-09, "12": 7.422769113579435e-10, "13": 5.814202152230036e-11, "2": 0.08673782895928761, "3": 0.02937478830510534, "4": 0.0076992643257321105, "5": 0.0016411888488553363, "6": 0.0002943610302086861, "7": 4.553248408712303e-05, "8": 6.188257530974841e-06, "9": 7.497763483292338e-07} |
| Raw goal margin distribution | {"-1": 0.2001986109584164, "-10": 1.788501186170544e-08, "-11": 1.4785455108800985e-09, "-12": 1.1192044343996889e-10, "-13": 7.353735810903752e-12, "-2": 0.08141304700020931, "-3": 0.02312377936694298, "-4": 0.005063834267501651, "-5": 0.0008999828146341665, "-6": 0.00013441884551347268, "-7": 1.730040131060865e-05, "-8": 1.9553312419366353e-06, "-9": 1.969390242665481e-07, "0": 0.3204381945403721, "1": 0.2244770501970183, "10": 5.515563827426915e-08, "11": 5.103233586614654e-09, "12": 4.323448009421542e-10, "13": 3.179354174641209e-11, "2": 0.10197979757548359, "3": 0.03241820928227455, "4": 0.007945473000980719, "5": 0.001580463817290538, "6": 0.0002641925522126875, "7": 3.805630814475893e-05, "8": 4.813942351621925e-06, "9": 5.426532343455203e-07} |
| Unadjusted home-win probability | 36.9% |
| Unadjusted draw probability | 32.0% |
| Unadjusted away-win probability | 31.1% |
| Raw p over 1 5 | 58.1% |
| Raw p under 3 5 | 86.8% |
| Raw p btts yes | 38.8% |
| P home draw | 62.7% |
| P draw away | 69.4% |
| P home away | 68.0% |
| Raw p home draw | 68.9% |
| Raw p draw away | 63.1% |
| Raw p home away | 68.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0766 |
| Totals anchor target over 2 5 | 0.3427 |
| Totals anchor reference over odds | 2.72 |
| Totals anchor reference under odds | 1.48 |
| Totals anchor reference last update utc | 2026-11-01T07:04:27Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3067 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:05Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:05Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.77, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.44, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.2, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.77, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.44 |
| Reference draw odds | 3.02 |
| Reference away odds | 2.43 |
| Market reference 1x2 last update utc | 2026-11-01T07:04:27Z |
| Market reference home last update utc | 2026-11-01T07:04:27Z |
| Market reference draw last update utc | 2026-11-01T07:04:27Z |
| Market reference away last update utc | 2026-11-01T07:04:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.65 |
| Reference Under 2.5 odds | 1.49 |
| Market reference over 2 5 last update utc | 2026-11-01T07:04:06Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:04:06Z |
| Home probability edge | +2.7% |
| Draw probability edge | +0.0% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | -0.7% |
| Under 2.5 probability edge | +0.7% |
| Market p over 1 5 | 61.1% |
| Market over 1 5 odds | 1.53 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:04:27Z |
| Market reference over 1 5 odds | 1.56 |
| Market reference over 1 5 opposite odds | 2.35 |
| Market reference over 1 5 last update utc | 2026-11-01T07:04:27Z |
| Market over 1 5 bookmakers | 1 |
| Raw edge prob home | 0.0890 |
| Raw ev home | 0.2684 |
| Raw edge prob draw | 0.0005 |
| Raw ev draw | -0.0323 |
| Raw edge prob away | -0.0895 |
| Raw ev away | -0.2446 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.1402348941854505, 0.14321319714891875, 0.06983370516593272, 0.022238372491222364, 0.0053113164683507115, 0.001014825437899584, 0.00016158433845057002, 2.2052630185667076e-05, 2.63347729070131e-06, 2.7954146591838234e-07, 2.6705788692139853e-08, 2.3193799217070828e-09, 1.8465021483904676e-10, 1.3569555918871985e-11], [0.12262583423554735, 0.13903731550179535, 0.07246165937632187, 0.02307523807756991, 0.005511189816650733, 0.0010530149450437537, 0.0001676650159909517, 2.2882505991467085e-05, 2.7325792604109004e-06, 2.9006105915195085e-07, 2.7710770307657923e-08, 2.4066619041861624e-09, 1.91598898263226e-10, 1.408020004874277e-11], [0.06483824620082936, 0.061942742430700935, 0.03379222346710882, 0.011971798128363496, 0.0028592923596385076, 0.0005463207922637913, 8.698725958470795e-05, 1.1871805676717928e-05, 1.4177052980090975e-06, 1.504882607665021e-07, 1.4376785495756272e-08, 1.2486142237529572e-09, 9.94045358887911e-11, 7.305030267677921e-12], [0.022426071095606993, 0.021424582356917642, 0.010233908721939754, 0.003722002146963157, 0.0009889640373949356, 0.0001889599063239223, 3.0086909843556635e-05, 4.106186914967812e-06, 4.903519399228297e-07, 5.205045837530152e-08, 4.972602322639589e-09, 4.318671924921958e-10, 3.43817626121931e-11, 2.526643420167194e-12], [0.005817500020290333, 0.005557705929171666, 0.002654756775884667, 0.00084540079772998, 0.0002305998374880176, 4.9017692585876645e-05, 7.804782116277631e-06, 1.0651773268399421e-06, 1.2720116726149424e-07, 1.3502300129323743e-08, 1.2899323287402868e-09, 1.1202976171685403e-10, 8.918900856121497e-12, 6.554312650408213e-13], [0.0012072843733277043, 0.0011533702615277035, 0.0005509319053429833, 0.00017544291684372756, 4.190202560260987e-05, 9.143686942644045e-06, 1.6196977143696275e-06, 2.2105233124737658e-07, 2.6397590196515628e-08, 2.8020826632158153e-09, 2.6769490979058784e-10, 2.324912422804498e-11, 1.8509066769744825e-12, 1.3601923873043692e-13], [0.00020878606976044414, 0.00019946223872607035, 9.527739260398071e-05, 3.0340852482124755e-05, 7.2464776599868395e-06, 1.3845738449867324e-06, 2.517799876708724e-07, 3.822848077235564e-08, 4.56516230147651e-09, 4.845882538710759e-10, 4.629478302282512e-11, 4.020671003606405e-12, 3.2009321011394405e-13, 2.3522976768147836e-14], [3.094900343927068e-05, 2.9566903191485453e-05, 1.412326193394345e-05, 4.497518196003642e-06, 1.0741677463388914e-06, 2.0523965386955642e-07, 3.267903272406712e-08, 5.093631095735969e-09, 6.767080961451822e-10, 7.183201232196132e-11, 6.862418554253343e-12, 5.959964707490543e-13, 4.7448404350300734e-14, 3.486883438797402e-15], [4.014208003005742e-06, 3.834944141198293e-06, 1.8318428635360979e-06, 5.833458764346957e-07, 1.3932379995321204e-07, 2.6620393859011977e-08, 4.238599635327323e-09, 5.78473577076102e-10, 7.889507155839467e-11, 9.316895754030754e-12, 8.900827948955766e-13, 7.73030966033719e-14, 6.154245478261449e-15, 4.522625561444752e-16], [4.628076757305938e-07, 4.4213991482645684e-07, 2.1119756060025072e-07, 6.725534626447247e-08, 1.6062975307213558e-08, 3.0691291033492273e-09, 4.886783256148012e-10, 6.669360717673063e-11, 7.964405989496312e-12, 9.655332091781255e-13, 1.0261978183615898e-13, 8.912459553415158e-15, 7.095377328571441e-16, 5.214243563673707e-17], [4.802238700617797e-08, 4.5877834820169346e-08, 2.1914526317860544e-08, 6.978627269844783e-09, 1.666745080353251e-09, 3.1846253487540765e-10, 5.0706807395013404e-11, 6.9203394468836545e-12, 8.264119347159537e-13, 8.772295265224144e-14, 9.571270185641337e-15, 9.247849685625216e-16, 7.36238774539829e-17, 5.410463903044093e-18], [4.529958760811219e-09, 4.327662840748419e-09, 2.0672004594409124e-09, 6.582949268099172e-10, 1.5722430619314868e-10, 3.004061729924861e-11, 4.783180527079125e-12, 6.527966279803025e-13, 7.79555581696486e-14, 8.274918900639545e-15, 7.905383012822712e-16, 7.841272847075662e-17, 6.944951083640548e-18, 5.103698480147271e-19], [3.917023638928293e-10, 3.742099772556751e-10, 1.7874937706018835e-10, 5.692230163347561e-11, 1.3595075727850057e-11, 2.59759115484934e-12, 4.13598272812427e-13, 5.644686758149683e-14, 6.7407625600918445e-15, 7.155264463867907e-16, 6.835729367757745e-17, 5.936785327170347e-18, 5.397919879433722e-19, 4.413132359094422e-20], [3.12648270320956e-11, 2.986862294194413e-11, 1.4267384808049489e-11, 4.54341377252017e-12, 1.0851292468476583e-12, 2.0733405167472058e-13, 3.3012510651561935e-14, 4.505465665052654e-15, 5.38032942694619e-16, 5.711175791957627e-17, 5.456129858323649e-18, 4.73861236210073e-19, 3.7724987722445495e-20, 3.1662273040350286e-21]] |
| Legacy trial inputs | {"lambda_home": 1.0376316021632368, "lambda_away": 0.9553426574623886, "rho": -0.019663736715803168, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3221 |
| Legacy p draw | 0.3170 |
| Legacy p away | 0.3608 |
| Legacy p over 1 5 | 0.5939 |
| Legacy p under 3 5 | 0.8589 |
| Legacy p btts yes | 0.4008 |
| Legacy p over 2 5 | 0.3202 |
| Legacy goal margin distribution | {"-1": 0.2286862949959086, "-10": 2.9214381775634974e-08, "-11": 2.5182838502379866e-09, "-12": 1.9873041488778952e-10, "-13": 1.3569555918871985e-11, "-2": 0.09596522598180596, "-3": 0.028327062076426174, "-4": 0.006455554910041052, "-5": 0.0011948663855707873, "-6": 0.0001859379137034546, "-7": 2.494078421335848e-05, "-8": 2.938356057461604e-06, "-9": 3.0853588764367044e-07, "0": 0.3170264357792375, "1": 0.19569120605092485, "10": 5.2533342637759106e-08, "11": 4.918436122874944e-09, "12": 4.215709868347734e-10, "13": 3.12648270320956e-11, "2": 0.08910048427391724, "3": 0.028566151066421307, "4": 0.00707078763691348, "5": 0.0014214696061421604, "6": 0.00024025376836553155, "7": 3.500228362324893e-05, "8": 4.478934541486649e-06, "9": 5.108107184410843e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3645 |
| Legacy raw p draw | 0.3141 |
| Legacy raw p away | 0.3214 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0376 |
| Legacy lambda away | 0.9553 |
| Legacy model home team | Getafe |
| Legacy model away team | Sevilla |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 61.5% |
| Market home draw odds | 1.61 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:04:20Z |
| Market reference home draw last update utc | 2026-11-01T07:04:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.2% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:04:20Z |
| Market reference draw away last update utc | 2026-11-01T07:04:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.2% |
| Market home away odds | 1.42 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:04:20Z |
| Market reference home away last update utc | 2026-11-01T07:04:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.53 |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home away odds | 1.36 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:20Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 2.61, "price": 1.48, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:20Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 1.48, "price": 2.61, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:20Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:20Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:20Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.3, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:20Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.3, "price": 1.61, "quote_source": "The Odds API", "side": "Under"}] |
| Market p under 3 5 | 85.1% |
| Market reference under 3 5 odds | 1.14 |
| Market reference under 3 5 opposite odds | 4.70 |
| Market reference under 3 5 last update utc | 2026-11-01T07:04:07Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 44.6% |
| Market btts yes odds | 2.21 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:04:20Z |
| Market reference btts yes odds | 2.22 |
| Market reference btts yes opposite odds | 1.79 |
| Market reference btts yes last update utc | 2026-11-01T07:04:28Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 8.569664528102011, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,449.4205 |
| Elo away rating | 1,481.9065 |
| Elo rating diff | 27.5140 |
| Elo home expectancy | 0.5395 |

</details>


---

## 2026-11-01 — Real Racing Club de Santander vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **81.0%**. Expected goals are 1.19 for Real Racing Club de Santander and 3.48 for Real Madrid (4.67 combined). The most likely exact score is 1-3 at 7.9%. Goal-market probabilities: at least one goal: 99.0%; Over 2.5 goals: 84.7%; Under 3.5 goals: 31.2%; Double Chance 1X: 19.0%; Double Chance X2: 91.9%; Double Chance 12 (either team wins): 89.1%; Under 4.5 goals: 49.8%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 8.1% | 12.40 |
| Draw | 10.9% | 9.15 |
| Real Madrid win | 81.0% | 1.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.19 |
| Real Madrid expected goals | 3.48 |
| Expected total goals | 4.67 |
| Over 0.5 | 99.0% |
| Under 0.5 | 1.0% |
| Over 1.5 | 94.9% |
| Under 1.5 | 5.1% |
| Over 2.5 | 84.7% |
| Under 2.5 | 15.3% |
| Over 3.5 | 68.8% |
| Under 3.5 | 31.2% |
| Over 4.5 | 50.2% |
| Under 4.5 | 49.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-3 | 7.94% |
| 2 | 1-4 | 6.91% |
| 3 | 1-2 | 6.84% |
| 4 | 0-3 | 6.69% |
| 5 | 0-4 | 5.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 8.1% | 7.8% | 10.72 | -13.6% |
| Draw | 10.9% | 10.7% | 7.99 | -12.7% |
| Real Madrid win | 81.0% | 81.5% | 1.21 | -2.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T15:15:00+00:00 |
| Fixture id | 6c520ed959578ca3aebe351ee3765d53 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:04:27Z |
| Market best draw last update utc | 2026-11-01T07:04:27Z |
| Market best away last update utc | 2026-11-01T07:04:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santander |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1867 |
| Dc lambda away | 3.4828 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:04:15.227758+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 67.2% |
| P btts no | 32.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 100.75 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 19.43 |
| Fair Over 2.5 odds | 1.18 |
| Fair Under 2.5 odds | 6.52 |
| Fair Over 3.5 odds | 1.45 |
| Fair Under 3.5 odds | 3.20 |
| Fair Over 4.5 odds | 1.99 |
| Fair Under 4.5 odds | 2.01 |
| Goal margin distribution | {"-1": 0.16770117908909815, "-10": 0.0009957358713303171, "-11": 0.0003059323939566118, "-12": 8.654912173354165e-05, "-13": 2.2681974145620925e-05, "-14": 5.535525219581314e-06, "-15": 1.2638381296973137e-06, "-16": 2.710429867337317e-07, "-17": 5.4797475755529963e-08, "-18": 1.047690489114869e-08, "-19": 1.8980635445776804e-09, "-2": 0.19157621632591504, "-20": 3.2240112061720176e-10, "-21": 4.467659645262582e-11, "-3": 0.17227259765705843, "-4": 0.12674084128126187, "-5": 0.07839243451661222, "-6": 0.041671709447406204, "-7": 0.019377875791799986, "-8": 0.00799663112185605, "-9": 0.0029632378294866288, "0": 0.10925481056439333, "1": 0.051938059759780504, "10": 1.9318937472434495e-08, "11": 2.0224888225808753e-09, "12": 1.9495972841638001e-10, "13": 1.740943504738603e-11, "14": 1.4477188919414978e-12, "15": 1.1262594365209117e-13, "16": 8.230130931251657e-15, "17": 5.669577603843532e-16, "18": 3.6935563865924207e-17, "19": 2.280048372690987e-18, "2": 0.020455402409926958, "20": 1.3196277411627507e-19, "21": 6.230982841822049e-21, "3": 0.006267642537674688, "4": 0.0015711808731478404, "5": 0.00033113518609107656, "6": 5.997828953498508e-05, "7": 9.503432816151854e-06, "8": 1.336296973600018e-06, "9": 1.687267776282034e-07} |
| Raw goal margin distribution | {"-1": 0.16546234986001546, "-10": 0.0009824426876729971, "-11": 0.0003018481627697255, "-12": 8.539368141677713e-05, "-13": 2.2379167290199035e-05, "-14": 5.461625347635044e-06, "-15": 1.2469657513338187e-06, "-16": 2.674245329796591e-07, "-17": 5.406592341303719e-08, "-18": 1.0337037055823803e-08, "-19": 1.87272418700525e-09, "-2": 0.1890186527176136, "-20": 3.180970301137992e-10, "-21": 4.4080158964604766e-11, "-3": 0.16997273948611671, "-4": 0.1250488370775928, "-5": 0.07734588687342901, "-6": 0.04111538753217908, "-7": 0.019119179013662453, "-8": 0.0078898752147894, "-9": 0.0029236782777803554, "0": 0.1141955025769569, "1": 0.05572184904958677, "10": 2.0726359872052893e-08, "11": 2.169831091064313e-09, "12": 2.0916292614339029e-10, "13": 1.8677746458681526e-11, "14": 1.5531880462247764e-12, "15": 1.2083096404207325e-13, "16": 8.829712074933271e-15, "17": 6.082617426939905e-16, "18": 3.9626391971849395e-17, "19": 2.4461543584118678e-18, "2": 0.021945618504161855, "20": 1.4157652044533886e-19, "21": 6.684922135105201e-21, "3": 0.006724252561539159, "4": 0.0016856444743617025, "5": 0.00035525903238807797, "6": 6.434782529764206e-05, "7": 1.019577649384146e-05, "8": 1.4336488230933205e-06, "9": 1.8101885355568155e-07} |
| Unadjusted home-win probability | 8.7% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 79.9% |
| Raw p over 1 5 | 94.8% |
| Raw p under 3 5 | 31.5% |
| Raw p btts yes | 67.4% |
| P home draw | 19.0% |
| P draw away | 91.9% |
| P home away | 89.1% |
| Raw p home draw | 20.1% |
| Raw p draw away | 91.3% |
| Raw p home away | 88.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8467 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:05Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:05Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.68, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 9.25, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.08, "price": 9.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.84, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.72 |
| Reference draw odds | 7.99 |
| Reference away odds | 1.21 |
| Market reference 1x2 last update utc | 2026-11-01T07:04:27Z |
| Market reference home last update utc | 2026-11-01T07:04:27Z |
| Market reference draw last update utc | 2026-11-01T07:04:27Z |
| Market reference away last update utc | 2026-11-01T07:04:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.21 |
| Reference Under 2.5 odds | 4.51 |
| Market reference over 2 5 last update utc | 2026-11-01T07:04:06Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:04:06Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Market p over 1 5 | 94.2% |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 10.00 |
| Market reference over 1 5 last update utc | 2026-11-01T07:04:27Z |
| Market over 1 5 bookmakers | 0 |
| Raw edge prob home | 0.0084 |
| Raw ev home | -0.0726 |
| Raw edge prob draw | 0.0071 |
| Raw ev draw | -0.0876 |
| Raw edge prob away | -0.0155 |
| Raw ev away | -0.0329 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.008923922015995461, 0.028713961268815924, 0.05371206465050558, 0.06544960441882984, 0.059814085715018984, 0.0437310493371823, 0.026643733568636613, 0.013914047326674882, 0.006357991211946289, 0.0025824614539765515, 0.0009440397517174028, 0.0003137285417967641, 9.557167970130014e-05, 2.6874618053164224e-05, 7.0173105904010805e-06, 1.710156573627421e-06, 3.907260127443356e-07, 8.401945076189662e-08, 1.706332910378925e-08, 3.2829676276095546e-09, 6.000577354780006e-10, 1.0445522720092181e-10, 1.735657108356836e-11], [0.008890031750067619, 0.03571758978997713, 0.06249861377623662, 0.07615625232424225, 0.06959884088995817, 0.05088484273203932, 0.03100227899817841, 0.016190192568327304, 0.007398070428566134, 0.0030049163452252384, 0.0010984715671592585, 0.00036505018177798357, 0.00011120588151774811, 3.127093298344802e-05, 8.165245316691507e-06, 1.989914479875171e-06, 4.546433714982371e-07, 9.776386808117007e-08, 1.985465318329565e-08, 3.820015617216197e-09, 6.98218861946684e-10, 1.2154265422895092e-10, 2.0195865485530633e-11], [0.005572740749650279, 0.02037160626573703, 0.03724947462113694, 0.04430717969629974, 0.04049212317901744, 0.029604448773915566, 0.018036911017086057, 0.009419341807793089, 0.004304146092808965, 0.0017482394999348157, 0.0006390831433010056, 0.0002123836652746546, 6.469881100128452e-05, 1.8193212043438926e-05, 4.750483124756627e-06, 1.1577184505445043e-06, 2.6450836200472636e-07, 5.6878340762297284e-08, 1.1551299591983212e-08, 2.2224586062094345e-09, 4.062188939117474e-10, 7.071267371140216e-11, 1.1749814544181055e-11], [0.002161454625720416, 0.007901372874594175, 0.014442055031010429, 0.017604861568508337, 0.015705357719362892, 0.011482442054800158, 0.006995833200034433, 0.0036534051800227304, 0.0016694149073168754, 0.0006780757483179875, 0.00024787609515023465, 8.237556282591602e-05, 2.5094213170801707e-05, 7.056456435815941e-06, 1.8425321014720384e-06, 4.490350462415337e-07, 1.0259275431621777e-07, 2.2060949587810056e-08, 4.480310686934671e-09, 8.620073408519846e-10, 1.575568910783583e-10, 2.742676226238596e-11, 4.557307102339356e-12], [0.0006287596591508462, 0.0022984819835381513, 0.004201143753230216, 0.0051192073614129375, 0.004680234395900485, 0.00334020259629052, 0.0020350636307545577, 0.0010627629043868528, 0.0004856270104472105, 0.00019724988501610148, 7.210629695562437e-05, 2.39627657173321e-05, 7.299819636358568e-06, 2.0526987199269234e-06, 5.359862022132054e-07, 1.3062273862330486e-07, 2.98438766502959e-08, 6.417453773174725e-09, 1.3033068503429786e-09, 2.5075494778844745e-10, 4.5832753532023317e-11, 7.978350082626117e-12, 1.325704840719275e-12], [0.00014632320448317395, 0.0005348963540891817, 0.000977678525523271, 0.0011913277428571276, 0.001088748822222604, 0.0007963107296135713, 0.000473594365423068, 0.00024732323633126335, 0.00011301377134815821, 4.590344631599402e-05, 1.678037749465576e-05, 5.576548394938254e-06, 1.6987937851860924e-06, 4.776983544775375e-07, 1.247332228224062e-07, 3.039816154799552e-08, 6.945184224397278e-09, 1.4934520480873916e-09, 3.033019564655389e-10, 5.835499616812085e-11, 1.06660713191274e-11, 1.856699509245031e-12, 3.085143546818448e-13], [2.8376608691175745e-05, 0.00010373299699071796, 0.00018960219633332178, 0.00023103540755140965, 0.00021114217256458452, 0.00015436947092318807, 9.408817374574353e-05, 4.796364816090723e-05, 2.1916876257514365e-05, 8.90210228983293e-06, 3.2542357689467802e-06, 1.0814657334050101e-06, 3.2944881612929907e-07, 9.264053042924177e-08, 2.4189641467479398e-08, 5.895146557412948e-09, 1.346886679525333e-09, 2.896266830493325e-10, 5.881965860637177e-11, 1.1316844086942086e-11, 2.0684821191833266e-12, 3.6007163468732574e-13, 5.98305043232157e-14], [4.7169469238004e-06, 1.7243182452740434e-05, 3.151692672205665e-05, 3.8404228172532904e-05, 3.509744353886654e-05, 2.566031088930865e-05, 1.56338916395912e-05, 8.167590044721326e-06, 3.643167623280673e-06, 1.479766115407645e-06, 5.409405178296779e-07, 1.797683620300487e-07, 5.476315357846215e-08, 1.5399319551646668e-08, 4.020961636030296e-09, 9.799301150453784e-10, 2.2388838105486521e-10, 4.8143656154545855e-11, 9.777391327547651e-12, 1.881160412224667e-12, 3.438367309921721e-13, 5.985348031085637e-14, 9.94542076497604e-15], [6.860717557401545e-07, 2.5079910058364783e-06, 4.584082373840629e-06, 5.585828434326915e-06, 5.10486233991808e-06, 3.732247750305859e-06, 2.2739224459163172e-06, 1.187501160382117e-06, 5.428363595783444e-07, 2.1522941709603822e-07, 7.867886088474028e-08, 2.6146996724126403e-08, 7.965205785095474e-09, 2.2398043422311315e-09, 5.848419017554846e-10, 1.425291370440451e-10, 3.256417703262499e-11, 7.00241135617604e-12, 1.4221046246678155e-12, 2.736115219638758e-13, 5.001045666413708e-14, 8.705584986939661e-15, 1.4465442151518325e-15], [8.870039816068056e-08, 3.2425150713441806e-07, 5.926638552877881e-07, 7.22176947289611e-07, 6.599941162389051e-07, 4.825324154749462e-07, 2.9398940366184926e-07, 1.5352887633237268e-07, 7.015465907104161e-08, 2.8506170778780447e-08, 1.0172181304528817e-08, 3.38047587694956e-09, 1.0298003359830976e-09, 2.8957836450152344e-10, 7.561265875286772e-11, 1.842721420832435e-11, 4.2101361036974556e-12, 9.053231971451835e-13, 1.838601361720474e-13, 3.5374508185901024e-14, 6.465719337944162e-15, 1.1255219998528157e-15, 1.870198660234499e-16], [1.0321055357887068e-08, 3.77294558357027e-08, 6.896154454643205e-08, 8.40315083779414e-08, 7.679600036565642e-08, 5.6146802893378034e-08, 3.4208199430283974e-08, 1.7864407201308766e-08, 8.163098868781438e-09, 3.3156522981689424e-09, 1.2125338033936314e-09, 3.933474864317401e-10, 1.1982613940467916e-10, 3.369493702894661e-11, 8.79818414491979e-12, 2.144165098235896e-12, 4.898856001952247e-13, 1.0534215210159835e-13, 2.139371054572723e-14, 4.1161287301476585e-15, 7.523421382460524e-16, 1.3096417950635663e-16, 2.1761372330663273e-17], [1.091766993256244e-09, 3.991042885305499e-09, 7.294790651639139e-09, 8.888899832366908e-09, 8.12352375857061e-09, 5.939240131001827e-09, 3.6185624184421447e-09, 1.8897069592378273e-09, 8.634971520439034e-10, 3.507315497042478e-10, 1.282127656125954e-10, 4.2624908204394985e-11, 1.2675275870057154e-11, 3.56426923531031e-12, 9.306768268298768e-13, 2.2681098019274838e-13, 5.182037206650191e-14, 1.1143151613387788e-14, 2.2630386357974792e-15, 4.3540639321684004e-16, 7.958317107030998e-17, 1.3853463965258429e-17, 2.3019301045045145e-18], [1.0586374477992133e-10, 3.8699351420723653e-10, 7.073431057526296e-10, 8.619167176151432e-10, 7.877016352417814e-10, 5.759014563535836e-10, 3.5087575526865585e-10, 1.8323640161068813e-10, 8.37294429001936e-11, 3.40088640648639e-11, 1.243221637966664e-11, 4.131543305246561e-12, 1.259087570934051e-12, 3.4561118900327046e-13, 9.024355441837463e-14, 2.1992842674969357e-14, 5.024788875954919e-15, 1.080501394281281e-15, 2.1943669853273937e-16, 4.2219403564836616e-17, 7.7168228779625e-18, 1.3433082174080168e-18, 2.2320782968320415e-19], [9.475506596655956e-12, 3.46384836882252e-11, 6.331189472459859e-11, 7.714725717013699e-11, 7.050451555862419e-11, 5.154699618879484e-11, 3.140570495183705e-11, 1.6400872043767747e-11, 7.494339919530118e-12, 3.0440186719383217e-12, 1.1127657401642224e-12, 3.6980050086664465e-13, 1.1265297961032328e-13, 3.16901433997595e-14, 8.077396062029094e-15, 1.968505141010407e-15, 4.497518979693671e-16, 9.671203404425652e-17, 1.9641038476562014e-17, 3.778916359109988e-18, 6.907067782021986e-19, 1.2023498603656022e-19, 1.9978579701533505e-20], [7.87540579266709e-13, 2.878918528574773e-12, 5.2620602114803905e-12, 6.411962778016464e-12, 5.859862631888539e-12, 4.284240723584005e-12, 2.610231634346372e-12, 1.3631305237428034e-12, 6.228792879033303e-13, 2.5299842322341075e-13, 9.248562772425865e-14, 3.0735338284542675e-14, 9.362960377205046e-15, 2.6328509111771213e-15, 6.87738132868623e-16, 1.6360894937141892e-16, 3.738036237324754e-17, 8.038055858686761e-18, 1.6324314337652712e-18, 3.140781918197613e-19, 5.740691652315168e-20, 9.993125917381003e-21, 1.6604855973214717e-21], [6.109141998415714e-14, 2.2332464581456252e-13, 4.0819068734311295e-13, 4.973913996397739e-13, 4.545636612496827e-13, 3.32338874018912e-13, 2.0248195614029856e-13, 1.0574131862098441e-13, 4.8318246930420294e-14, 1.9625697183581664e-14, 7.174332948102772e-15, 2.3842142347058016e-15, 7.263073926062966e-16, 2.0423658793576986e-16, 5.332881638108769e-17, 1.3001562838329139e-17, 2.8996847616796625e-18, 6.235313573001886e-19, 1.2663163897960893e-19, 2.4363801979818568e-20, 4.4531928127142306e-21, 7.751908516786895e-22, 1.288078680314654e-22], [4.442820583554597e-15, 1.6241091359429582e-14, 2.968531404595901e-14, 3.617235855666298e-14, 3.305774839183242e-14, 2.4169056646407743e-14, 1.4725324812744717e-14, 7.68994577345469e-15, 3.5139026409832225e-15, 1.4272618223056199e-15, 5.217471471995723e-16, 1.7338991433333514e-16, 5.282007579290095e-17, 1.4852928889708403e-17, 3.8782919627002155e-18, 9.451607434236542e-19, 2.1602825929507383e-19, 4.534577767914742e-20, 9.209176220388411e-21, 1.7718363881156656e-21, 3.238545886802919e-22, 5.637508299716133e-23, 9.367440592515049e-24], [3.0409437863721215e-16, 1.111641690780251e-15, 2.031848227873747e-15, 2.4758620548053237e-15, 2.2626786896527495e-15, 1.6542811317527124e-15, 1.0078931649272391e-15, 5.263478994377047e-16, 2.405134351265032e-16, 9.769070995421371e-17, 3.5711632182646355e-17, 1.1867888263669078e-17, 3.615335759285063e-18, 1.01662718462623e-18, 2.654545152997e-19, 6.469270220985271e-20, 1.4780589086353067e-20, 3.179564911692882e-21, 6.303335162499454e-22, 1.212755445235085e-22, 2.216662997332876e-23, 3.858662647350718e-24, 6.411661179715645e-25], [1.9657777949513483e-17, 7.186060332555525e-17, 1.3134613493893407e-16, 1.6004882012321909e-16, 1.462678641138384e-16, 1.0693881057518916e-16, 6.515391741788522e-17, 3.402506214586469e-17, 1.554767214961255e-17, 6.3150864301286414e-18, 2.3085311172380094e-18, 7.671839027816059e-19, 2.3370858707568593e-19, 6.571851654207445e-20, 1.7159955211413677e-20, 4.181973967077025e-21, 9.554715859090721e-22, 2.054590563418851e-22, 4.174242328081129e-23, 7.839696792927608e-24, 1.4329324068978506e-24, 2.4943813116057426e-25, 4.144733366108412e-26], [1.2038693627035834e-18, 4.400842198503533e-18, 8.04381798230796e-18, 9.801609906167898e-18, 8.957645203185289e-18, 6.549079863760412e-18, 3.9901155278566286e-18, 2.0837416104044314e-18, 9.52160829690395e-19, 3.867445799612958e-19, 1.4137762121580462e-19, 4.6983397538122975e-20, 1.4312635360097977e-20, 4.0246923548798226e-21, 1.0508992622382278e-21, 2.561098384323034e-22, 5.851439425981537e-23, 1.2582595238141172e-23, 2.5553721380138165e-24, 4.918417917506864e-25, 8.77547517282909e-26, 1.5275934277286177e-26, 2.5382917280112546e-27], [7.004028501439066e-20, 2.560379484982699e-19, 4.679837543331921e-19, 5.702508699832294e-19, 5.211495885898412e-19, 3.810209267305085e-19, 2.321421555108009e-19, 1.2123064246880956e-19, 5.539605704499873e-20, 2.2500531575475838e-20, 8.225252001075816e-21, 2.733461500444211e-21, 8.326992039045135e-22, 2.3415381133877137e-22, 6.114059060634256e-23, 1.490029286774429e-23, 3.4043268965646e-24, 7.320466688519866e-25, 1.4866977963653744e-25, 2.8603918425403345e-26, 5.230225440024141e-27, 8.887432671593469e-28, 1.4767605322252235e-28], [3.8808526010071246e-21, 1.418677177258605e-20, 2.593044802515997e-20, 3.159695269010242e-20, 2.8876306485290997e-20, 2.1111936569595974e-20, 1.2862733037599563e-20, 6.717252136398056e-21, 3.0694325704764217e-21, 1.2467288856803926e-21, 4.557518664545065e-22, 1.514579955174679e-22, 4.613891663441153e-23, 1.2974196601043175e-23, 3.387730647198033e-24, 8.256082955640786e-25, 1.8862988476555648e-25, 4.056187404561706e-26, 8.237623545864606e-27, 1.5849106153325091e-27, 2.896884717270131e-28, 5.0447168077595083e-29, 8.182562294504369e-30], [2.0525937651494143e-22, 7.503423160274355e-22, 1.371468628573059e-21, 1.6711716408037367e-21, 1.5272759041884336e-21, 1.1166162137087323e-21, 6.803135380330252e-22, 3.552773390705215e-22, 1.6234314477884182e-22, 6.593983850134259e-23, 2.4104843335120814e-23, 8.010655627593415e-24, 2.4403001698638296e-24, 6.862088769929827e-25, 1.791780188363693e-25, 4.366665303110675e-26, 9.976687217910725e-27, 2.1453288317933874e-27, 4.356902069793055e-28, 8.382636450831434e-29, 1.53217040695702e-29, 2.667130152763306e-30, 4.433496828007769e-31]] |
| Legacy trial inputs | {"lambda_home": 1.163586136241522, "lambda_away": 3.6555811908198788, "rho": -0.019663736715803168, "max_goals": 22, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0766 |
| Legacy p draw | 0.1051 |
| Legacy p away | 0.8183 |
| Legacy p over 1 5 | 0.9535 |
| Legacy p under 3 5 | 0.2920 |
| Legacy p btts yes | 0.6713 |
| Legacy p over 2 5 | 0.8585 |
| Legacy goal margin distribution | {"-1": 0.15509074204618797, "-10": 0.0013814129817848293, "-11": 0.0004451080350665557, "-12": 0.00013207352893642146, "-13": 3.630690700001952e-05, "-14": 9.295158173497442e-06, "-15": 2.2264203876110533e-06, "-16": 5.009509370418866e-07, "-17": 1.0626240630691738e-07, "-18": 2.1318316082020302e-08, "-19": 4.05645647036998e-09, "-2": 0.1841487479008436, "-20": 7.333502042511326e-10, "-21": 1.2465109268645244e-10, "-22": 1.735657108356836e-11, "-3": 0.17283397421272578, "-4": 0.13292421736887555, "-5": 0.08603725385948251, "-6": 0.047894176275347485, "-7": 0.02333399171816757, "-8": 0.010092168984352204, "-9": 0.003920594457749424, "0": 0.10507522148390293, "1": 0.0500829136969448, "10": 1.5102796075236753e-08, "11": 1.5489641405773438e-09, "12": 1.4629645940311622e-10, "13": 1.2801161903112277e-11, "14": 1.043179457147764e-12, "15": 7.953376027572398e-14, "16": 5.696152961018648e-15, "17": 3.845990437377576e-16, "18": 2.45597281309445e-17, "19": 1.4875089308678171e-18, "2": 0.019105823581749948, "20": 8.559852541554976e-20, "21": 4.63119491703456e-21, "22": 2.0525937651494143e-22, "3": 0.0057077929860835435, "4": 0.0013972860172760506, "5": 0.0002878789071029176, "6": 5.1009153625209226e-05, "7": 7.91036553713501e-06, "8": 1.0890156754717047e-06, "9": 1.3466156054079434e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0752 |
| Legacy raw p draw | 0.1030 |
| Legacy raw p away | 0.8218 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1636 |
| Legacy lambda away | 3.6556 |
| Legacy model home team | Santander |
| Legacy model away team | Real Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 23.8% |
| Market home draw odds | 4.72 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:04:11Z |
| Market reference home draw last update utc | 2026-11-01T07:04:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.7% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:04:11Z |
| Market reference draw away last update utc | 2026-11-01T07:04:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.5% |
| Market home away odds | 1.10 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:04:11Z |
| Market reference home away last update utc | 2026-11-01T07:04:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 4.00 |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home away odds | 1.10 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:11Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.05, "price": 1.76, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:11Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.05, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:11Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.17, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:11Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.17, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p under 3 5 | 37.6% |
| Market under 3 5 odds | 2.45 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:04:27Z |
| Market reference under 3 5 odds | 2.45 |
| Market reference under 3 5 opposite odds | 1.54 |
| Market reference under 3 5 last update utc | 2026-11-01T07:04:27Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.1% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:04:11Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.60 |
| Market reference btts yes last update utc | 2026-11-01T07:04:28Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 10.724162471624577, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,438.0702 |
| Elo away rating | 1,670.4419 |
| Elo rating diff | -172.3717 |
| Elo home expectancy | 0.2705 |

</details>


---

## 2026-11-02 — Deportivo La Coruña vs CA Osasuna

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **46.1%**. Expected goals are 1.50 for Deportivo La Coruña and 0.97 for CA Osasuna (2.48 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 42.7%; Under 3.5 goals: 77.9%; Double Chance 1X: 74.5%; Double Chance X2: 53.9%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 90.5%; BTTS Yes (both teams score): 47.7%; BTTS No (at least one team does not score): 52.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 46.1% | 2.17 |
| Draw | 28.4% | 3.52 |
| CA Osasuna win | 25.5% | 3.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 1.50 |
| CA Osasuna expected goals | 0.97 |
| Expected total goals | 2.48 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 69.4% |
| Under 1.5 | 30.6% |
| Over 2.5 | 42.7% |
| Under 2.5 | 57.3% |
| Over 3.5 | 22.1% |
| Under 3.5 | 77.9% |
| Over 4.5 | 9.5% |
| Under 4.5 | 90.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.37% |
| 2 | 1-0 | 12.13% |
| 3 | 0-0 | 9.76% |
| 4 | 2-0 | 9.08% |
| 5 | 0-1 | 8.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 46.1% | 44.7% | 2.18 | +0.4% |
| Draw | 28.4% | 29.2% | 3.30 | -6.3% |
| CA Osasuna win | 25.5% | 26.1% | 3.67 | -6.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T20:00:00+00:00 |
| Fixture id | 7a2cd2744fdf15ea675423a6c23df46b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:04:27Z |
| Market best draw last update utc | 2026-11-01T07:04:27Z |
| Market best away last update utc | 2026-11-01T07:04:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | La Coruna |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.5031 |
| Dc lambda away | 0.9750 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:04:15.227758+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.7% |
| P btts no | 52.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.24 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.27 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.75 |
| Fair Over 3.5 odds | 4.53 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.52 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.16538666762771753, "-10": 1.726475206677895e-08, "-11": 1.4710871797923872e-09, "-12": 1.1508243639500348e-10, "-13": 8.319663166745704e-12, "-14": 5.570947585931446e-13, "-15": 3.220349476657138e-14, "-2": 0.06615902145692687, "-3": 0.0188477353664322, "-4": 0.004185307596169409, "-5": 0.0007588268505621199, "-6": 0.00011604047293160212, "-7": 1.5327464886338966e-05, "-8": 1.7807331116400857e-06, "-9": 1.8457498373702668e-07, "0": 0.28395008580759407, "1": 0.22953787814428717, "10": 1.1701607617841428e-06, "11": 1.5371164609382614e-07, "12": 1.853790225895704e-08, "13": 2.066048258570084e-09, "14": 2.1327844610010254e-10, "15": 1.9006584358041364e-11, "2": 0.1405428763330129, "3": 0.06172514480509836, "4": 0.02113068136828597, "5": 0.005906252190409806, "6": 0.0013923934285114334, "7": 0.0002835345467437776, "8": 5.078291943289634e-05, "9": 8.114744428181398e-06} |
| Raw goal margin distribution | {"-1": 0.15515215649310102, "-10": 2.0487871177543843e-08, "-11": 1.7961573970516815e-09, "-12": 1.4458525302660245e-10, "-13": 1.0756032750121026e-11, "-14": 7.408964582669586e-13, "-15": 4.3870797255577045e-14, "-2": 0.06330049948817447, "-3": 0.018464590005512684, "-4": 0.004206304336670172, "-5": 0.0007832047467166901, "-6": 0.00012307982511867188, "-7": 1.671394030290282e-05, "-8": 1.9969467273707278e-06, "-9": 2.1290757493232364e-07, "0": 0.2662977115180033, "1": 0.24090308175442543, "10": 1.5535620740070692e-06, "11": 2.0997101353712423e-07, "12": 2.6056863046915754e-08, "13": 2.988363508326123e-09, "14": 3.1733794489483966e-10, "15": 2.8968312081937535e-11, "2": 0.15044352202235362, "3": 0.06765333366332024, "4": 0.023759286917600517, "5": 0.006820107165005011, "6": 0.001652288712431499, "7": 0.00034590838506821264, "8": 6.371356410872365e-05, "9": 1.0472243009616288e-05} |
| Unadjusted home-win probability | 49.2% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 76.2% |
| Raw p btts yes | 48.7% |
| P home draw | 74.5% |
| P draw away | 53.9% |
| P home away | 71.6% |
| Raw p home draw | 75.8% |
| Raw p draw away | 50.8% |
| Raw p home away | 73.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9713 |
| Totals anchor target over 2 5 | 0.4270 |
| Totals anchor reference over odds | 2.25 |
| Totals anchor reference under odds | 1.70 |
| Totals anchor reference last update utc | 2026-11-01T07:04:27Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4436 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:05Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.49, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:04:05Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.63, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.81, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.93, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:27Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:28Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.59, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:04:28Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.53, "price": 2.59, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.18 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.67 |
| Market reference 1x2 last update utc | 2026-11-01T07:04:27Z |
| Market reference home last update utc | 2026-11-01T07:04:27Z |
| Market reference draw last update utc | 2026-11-01T07:04:27Z |
| Market reference away last update utc | 2026-11-01T07:04:27Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.34 |
| Reference Under 2.5 odds | 1.72 |
| Market reference over 2 5 last update utc | 2026-11-01T07:04:28Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:04:28Z |
| Home probability edge | +1.3% |
| Draw probability edge | -0.8% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Market p over 1 5 | 70.4% |
| Market over 1 5 odds | 1.39 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:04:27Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 2.90 |
| Market reference over 1 5 last update utc | 2026-11-01T07:04:27Z |
| Market over 1 5 bookmakers | 1 |
| Raw edge prob home | 0.0444 |
| Raw ev home | 0.0718 |
| Raw edge prob draw | -0.0252 |
| Raw ev draw | -0.1212 |
| Raw edge prob away | -0.0192 |
| Raw ev away | -0.1117 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09463847307894312, 0.08553481561925602, 0.04287075824587571, 0.013916458239200225, 0.003388110296755166, 0.0006598972920074289, 0.0001071060261368968, 1.4900631581543329e-05, 1.8138589008004486e-06, 1.9626813767415693e-07, 1.9113429200129247e-08, 1.6921339445365389e-09, 1.373226899744731e-10, 1.0286976799667479e-11, 7.155640859264592e-13, 4.6456457159700756e-14], [0.12187226339870323, 0.1325491433403225, 0.06214640753337931, 0.020173608318154564, 0.004911480269664734, 0.0009566018357795755, 0.00015526328485745213, 2.1600287950596716e-05, 2.6294103269805484e-06, 2.84514670810353e-07, 2.7707253359483015e-08, 2.45295511488531e-09, 1.9906603484333084e-10, 1.4912231055303424e-11, 1.0372976620844794e-12, 6.734431667024428e-14], [0.0900589495200796, 0.08770325004804413, 0.045877910935722, 0.014622056329962567, 0.0035598956832084993, 0.0006933556807250485, 0.00011253656070627866, 1.5656129641062114e-05, 1.9058259340296325e-06, 2.0621940694396824e-07, 2.008252628788851e-08, 1.7779292280818837e-09, 1.4428528248176796e-10, 1.0808551403262812e-11, 7.518449157302374e-13, 4.881191189624666e-14], [0.0435171540999537, 0.042378862597731694, 0.020635172867144513, 0.007196226079979766, 0.0017201680660443844, 0.0003350346208231405, 5.437850297201194e-05, 7.565158263888558e-06, 9.209092633305055e-07, 9.964675091375409e-08, 9.70402603898419e-09, 8.591086239574722e-10, 6.97197214221836e-11, 5.222772412065358e-12, 3.632970541123686e-13, 2.3586278800961645e-14], [0.015770859345885048, 0.015358336157100087, 0.007478301731732634, 0.002427563169116747, 0.0006349338639250395, 0.0001214184151120604, 1.9707072752082952e-05, 2.741655546571538e-06, 3.337426530454912e-07, 3.61125382722794e-08, 3.516793156972287e-09, 3.113457566675888e-10, 2.5266815878125546e-11, 1.8927618501215184e-12, 1.316608785588452e-13, 8.547798980797602e-15], [0.004572357906243775, 0.0044527573428006706, 0.0021681426039276692, 0.0007038099450245428, 0.00017135004328755002, 3.585354942021849e-05, 5.7135624591325015e-06, 7.948730084790423e-07, 9.676015902719264e-08, 1.0469908218848635e-08, 1.0196043629101205e-09, 9.026675090130349e-11, 7.325467992084848e-12, 5.487579605037712e-13, 3.817170934180021e-14, 2.478216018141722e-15], [0.0011046986705179594, 0.0010758027297062445, 0.0005238313144256616, 0.0001700430995360664, 4.1398807550578334e-05, 8.06318525731793e-06, 1.4059611811831902e-06, 1.9204427424597e-07, 2.3377614182494653e-08, 2.529568753577467e-09, 2.4634020504454133e-10, 2.180878263630165e-11, 1.7698603035268492e-12, 1.3258196358094603e-13, 9.222426902255813e-15, 5.987462041759754e-16], [0.00022877083384252288, 0.00022278680521047907, 0.00010847965132228803, 3.521403864077575e-05, 8.573233566934002e-06, 1.6697961751673636e-06, 2.7101980103102557e-07, 4.0506146047551363e-08, 4.841244433896642e-09, 5.238456137062041e-10, 5.1014322385808994e-11, 4.516356832816475e-12, 3.6651842554746284e-13, 2.74562531578596e-14, 1.909862253651076e-15, 1.2399369352473255e-16], [4.145391303259772e-05, 4.036959035767109e-05, 1.965681532120546e-05, 6.380881998035189e-06, 1.5534938292722637e-06, 3.0257172326084326e-07, 4.910954370077481e-08, 6.832138622038404e-09, 8.934795661240557e-10, 9.492228597651069e-11, 9.243937472614792e-12, 8.183764522213011e-13, 6.641416076643702e-14, 4.975149635509789e-15, 3.460723661198493e-16, 2.2468003030067345e-17], [6.676946344954587e-06, 6.5022954183844095e-06, 3.1661064447441254e-06, 1.027763210215278e-06, 2.502199234391298e-07, 4.873496888277952e-08, 7.910032234048135e-09, 1.1004467289920337e-09, 1.339577509393195e-10, 1.5571960023975033e-11, 1.4889131086908225e-12, 1.3181519576111052e-13, 1.0697272115999794e-14, 8.0134309994565e-16, 5.574158025170423e-17, 3.6189020465225764e-18], [9.67905037396846e-07, 9.425872494620904e-07, 4.5896585332277385e-07, 1.4898684773320388e-07, 3.6272438303596126e-08, 7.064729809408356e-09, 1.1466559187033111e-09, 1.5952321276074527e-10, 1.941881441513984e-11, 2.1012078389436253e-12, 2.1982999726849084e-13, 1.9108224836798207e-14, 1.5507004298911197e-15, 1.1616448344035243e-16, 8.080423824111474e-18, 5.246041138733728e-19], [1.275542486064905e-07, 1.2421777313459754e-07, 6.048428543576243e-08, 1.9634059830878564e-08, 4.780121431523778e-09, 9.310172668080527e-10, 1.5111072726075522e-10, 2.1022582539414403e-11, 2.5590860527120965e-12, 2.7690525072929553e-13, 2.696621554408989e-14, 2.564751299674591e-15, 2.0435726699025865e-16, 1.5308602422243726e-17, 1.0648693306510137e-18, 6.913434787048862e-20], [1.5408790359793317e-08, 1.5005737920155688e-08, 7.306614123193855e-09, 2.3718309280232984e-09, 5.774475553529866e-10, 1.1246861662640903e-10, 1.8254456773605283e-11, 2.5395670525301885e-12, 3.0914235260451526e-13, 3.345066906533922e-14, 3.257568968931528e-15, 2.8839634014814357e-16, 2.5143541051323107e-17, 1.8493076318727567e-18, 1.2863819477464254e-19, 8.351557746099073e-21], [1.7182250962909584e-09, 1.6732809572160488e-09, 8.147562178627779e-10, 2.644814634718263e-10, 6.439083524611417e-11, 1.2541308897086882e-11, 2.035543674434661e-12, 2.8318561947321856e-13, 3.447228083247357e-14, 3.730064316129771e-15, 3.6324958835976334e-16, 3.2158905258001755e-17, 2.6098095785629855e-18, 2.100310050590917e-19, 1.4344368989540848e-20, 9.312772630039895e-22], [1.7791267360869e-10, 1.7325895742032867e-10, 8.436348495443281e-11, 2.7385587830014812e-11, 6.667313659463005e-12, 1.2985829395983546e-12, 2.1076925144888135e-13, 2.932229938718219e-14, 3.569413379849981e-15, 3.8622746032958725e-16, 3.76124790586797e-17, 3.329876176951611e-18, 2.702312989922033e-19, 2.0243290484577235e-20, 1.5127634175287062e-21, 9.642859255733175e-23], [1.7193745374606868e-11, 1.674400332101737e-11, 8.153012653900929e-12, 2.6465839365600345e-12, 6.443391078793047e-13, 1.2549698657427195e-13, 2.036905392237076e-14, 2.833750621780191e-15, 3.4495341756731285e-16, 3.73255961753117e-17, 3.634925914637507e-18, 3.218041860323035e-19, 2.611555463069752e-20, 1.9563416988581664e-21, 1.360835050729881e-22, 9.491441380852464e-24]] |
| Legacy trial inputs | {"lambda_home": 1.449622308449792, "lambda_away": 0.9738426943175676, "rho": -0.019663736715803168, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4629 |
| Legacy p draw | 0.2809 |
| Legacy p away | 0.2561 |
| Legacy p over 1 5 | 0.6980 |
| Legacy p under 3 5 | 0.7748 |
| Legacy p btts yes | 0.4817 |
| Legacy p over 2 5 | 0.4325 |
| Legacy goal margin distribution | {"-1": 0.16415077650816265, "-10": 2.171602650900297e-08, "-11": 1.9023803756362263e-09, "-12": 1.5301035222430772e-10, "-13": 1.1373086373648205e-11, "-14": 7.829084025967034e-13, "-15": 4.6456457159700756e-14, "-2": 0.06695982272465958, "-3": 0.01957851368967988, "-4": 0.004465158314989958, "-5": 0.0008317747700922415, "-6": 0.00013071539563001106, "-7": 1.774628414724578e-05, "-8": 2.1193410314429064e-06, "-9": 2.258249715154497e-07, "0": 0.28093398822491383, "1": 0.23281794069957934, "10": 1.0997006989287553e-06, "11": 1.4340277267144685e-07, "12": 1.7169081385900358e-08, "13": 1.899637066365188e-09, "14": 1.9465667692970737e-10, "15": 1.7193745374606868e-11, "2": 0.14066304262798368, "3": 0.06122255983795606, "4": 0.020784265438541723, "5": 0.005763278607608747, "6": 0.0013482072762566785, "7": 0.00027246041214793034, "8": 4.8435398566603034e-05, "9": 7.682455420567701e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4786 |
| Legacy raw p draw | 0.2704 |
| Legacy raw p away | 0.2511 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4496 |
| Legacy lambda away | 0.9738 |
| Legacy model home team | La Coruna |
| Legacy model away team | Osasuna |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 95/100 |
| Market p home draw | 73.5% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:04:28Z |
| Market reference home draw last update utc | 2026-11-01T07:04:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.7% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:04:28Z |
| Market reference draw away last update utc | 2026-11-01T07:04:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.8% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:04:28Z |
| Market reference home away last update utc | 2026-11-01T07:04:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.31 |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home away odds | 1.36 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:28Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.34, "price": 1.57, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:28Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.57, "price": 2.34, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:28Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.85, "price": 1.97, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:28Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.97, "price": 1.85, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:28Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.5, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:04:28Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.5, "price": 1.51, "quote_source": "The Odds API", "side": "Under"}] |
| Market p under 3 5 | 78.9% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 3.70 |
| Market reference under 3 5 last update utc | 2026-11-01T07:04:07Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 49.6% |
| Market btts yes odds | 1.94 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:04:28Z |
| Market reference btts yes odds | 1.94 |
| Market reference btts yes opposite odds | 1.91 |
| Market reference btts yes last update utc | 2026-11-01T07:04:28Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 9.68670138083881, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,438.5249 |
| Elo away rating | 1,412.0509 |
| Elo rating diff | 86.4740 |
| Elo home expectancy | 0.6219 |

</details>


---
