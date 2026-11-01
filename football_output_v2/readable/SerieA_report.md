# Serie A — football model report

Fixtures in this report: **10**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,990 |
| Training data through | 2026-10-29 |
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
| Training sha256 | 4f31a6edf1745c63b971e3242fa8f509b250913a09f59337c0edc0545b59a2fa |
| Training as of utc | 2026-10-31T11:44:26.750844+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 90, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 90, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 171, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-31T11:44:26.750844+00:00', 'observations': 567, 'observations_sha256': '07294b4a9d02566c3f83f43c9b410e6f241b91ea16dbbe1083a9a860bfad8623', 'eligible_training_matches': 221, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 211, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 26, 'retrospective_eligible_training_matches': 221, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'bd2bbb32c2e1cfee6e2266b90ed5c57ac45b54800a3d090cc9132f2df9bfdaaf', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 161, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-27T00:00:00+00:00', 'audit_origin_utc': '2025-10-29T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 14, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-31', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1989, 'tune_start_date': '2025-11-01', 'audit_start_date': '2026-05-02', 'training_shot_matches': 1610, 'tuning_matches': 251, 'audit_matches': 128, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8431748666026699, 'audit_candidate_poisson_score': 0.8422724620733035, 'audit_gain': 0.0009024045293664074, 'audit_gain_lower95': -0.005324687163822864, 'audit_baseline_briers': [0.5588489115053373, 0.16200217125762034, 0.20624759689052116, 0.24154468600069465], 'audit_candidate_briers': [0.5619675133684585, 0.16034568530573262, 0.20570629441367932, 0.24194321831349277], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1805.954 |
| Base scoring parameter | 0.150 |
| Home-advantage parameter | 0.110 |
| Dixon-Coles low-score adjustment | -0.026 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1990, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-29'} |
| Training data health | {'training_end': '2026-10-29', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 10.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 25.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261031T114426750844Z_66f450a2286b493a537ea5edd44685b13e2e530caa061a17477c37a347a7c348.json |
| Over 1 5 in window quote fixtures | 4 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 3, 'ANCHORED_ALTERNATE': 5, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 10} |
| Legacy comparison status | {'AVAILABLE': 10} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-31 — AC Milan vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **48.5%**. Expected goals are 1.25 for AC Milan and 1.80 for Inter Milan (3.05 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 55.2%; Under 3.5 goals: 66.9%; Double Chance 1X: 51.5%; Double Chance X2: 74.0%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 83.2%; BTTS Yes (both teams score): 57.6%; BTTS No (at least one team does not score): 42.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 26.0% | 3.84 |
| Draw | 25.4% | 3.93 |
| Inter Milan win | 48.5% | 2.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.25 |
| Inter Milan expected goals | 1.80 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.9% |
| Under 1.5 | 21.1% |
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 16.8% |
| Under 4.5 | 83.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.95% |
| 2 | 1-2 | 9.42% |
| 3 | 0-1 | 8.94% |
| 4 | 0-2 | 7.91% |
| 5 | 2-1 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 26.0% | 25.9% | 3.73 | -2.9% |
| Draw | 25.4% | 26.2% | 3.69 | -6.1% |
| Inter Milan win | 48.5% | 47.9% | 2.05 | -0.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T19:45:00+00:00 |
| Fixture id | e82f25e981f2ebc731cfaf5716231af5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:45:07Z |
| Market best draw last update utc | 2026-10-31T11:45:07Z |
| Market best away last update utc | 2026-10-31T11:45:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Milan |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2514 |
| Dc lambda away | 1.8000 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:44:26.750844+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.6% |
| P btts no | 42.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.66 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.73 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.97 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.22176749428592013, "-10": 3.900414492909284e-06, "-11": 5.985757013802817e-07, "-12": 8.439855204890702e-08, "-13": 1.100451832281688e-08, "-14": 1.3339152666662375e-09, "-15": 1.501230539104457e-10, "-16": 1.4260678191208726e-11, "-2": 0.14865776648589898, "-3": 0.07351158916733937, "-4": 0.0287420136292537, "-5": 0.009250658090550649, "-6": 0.0025239213741838867, "-7": 0.0005967856555074832, "-8": 0.00012440178007270788, "-9": 2.3173765499525574e-05, "0": 0.2543924544263201, "1": 0.15448702328705077, "10": 1.0371865357330543e-07, "11": 1.106656353363639e-08, "12": 1.0848664639059894e-09, "13": 9.834672810020912e-11, "14": 8.288285661281511e-12, "15": 6.485320569468739e-13, "16": 4.283234253437597e-14, "2": 0.072402405307624, "3": 0.02489251583069733, "4": 0.006766713068779763, "5": 0.0015141914500282308, "6": 0.00028723117271748955, "7": 4.721953601902498e-05, "8": 6.843488221000699e-06, "9": 8.863293422492882e-07} |
| Raw goal margin distribution | {"-1": 0.2218405822083473, "-10": 5.699814344518327e-06, "-11": 9.172470528042457e-07, "-12": 1.3564942282249956e-07, "-13": 1.8554355121775226e-08, "-14": 2.3594894214223805e-09, "-15": 2.7826558698111917e-10, "-16": 2.7441014147212495e-11, "-2": 0.15300624182970748, "-3": 0.07847283847343323, "-4": 0.0319531354592812, "-5": 0.010736342264786517, "-6": 0.0030627510325848665, "-7": 0.0007579647828285157, "-8": 0.00016548558662806385, "-9": 3.2303947625474576e-05, "0": 0.23659930078422886, "1": 0.15340550244869786, "10": 1.5043074538829947e-07, "11": 1.6830995823569994e-08, "12": 1.7305694276893993e-09, "13": 1.6457525294392887e-10, "14": 1.4550713546170169e-11, "15": 1.1930903878029974e-12, "16": 8.180156144725157e-14, "2": 0.07396126449254957, "3": 0.026373157670059256, "4": 0.0074662725512607605, "5": 0.001744192026076722, "6": 0.0003459371741167421, "7": 5.952263597329498e-05, "8": 9.035264938945317e-06, "9": 1.2262637925747266e-06} |
| Unadjusted home-win probability | 26.3% |
| Unadjusted draw probability | 23.7% |
| Unadjusted away-win probability | 50.0% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 59.9% |
| P home draw | 51.5% |
| P draw away | 74.0% |
| P home away | 74.6% |
| Raw p home draw | 50.0% |
| Raw p draw away | 73.7% |
| Raw p home away | 76.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9522 |
| Totals anchor target over 2 5 | 0.5517 |
| Totals anchor reference over odds | 1.77 |
| Totals anchor reference under odds | 2.16 |
| Totals anchor reference last update utc | 2026-10-31T11:45:07Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5820 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.42, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.23, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.55, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.61, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:24Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.66, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:24Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.56, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.69, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.75, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.73 |
| Reference draw odds | 3.69 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-31T11:45:07Z |
| Market reference home last update utc | 2026-10-31T11:45:07Z |
| Market reference draw last update utc | 2026-10-31T11:45:07Z |
| Market reference away last update utc | 2026-10-31T11:45:07Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-31T11:44:24Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:44:24Z |
| Home probability edge | +0.1% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | 0.0042 |
| Raw ev home | -0.0176 |
| Raw edge prob draw | -0.0254 |
| Raw ev draw | -0.1269 |
| Raw edge prob away | 0.0212 |
| Raw ev away | 0.0251 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.05522582185123732, 0.08227497552445967, 0.07535567061549185, 0.04410006225401257, 0.019356361720254824, 0.006796702224813864, 0.00198880182996246, 0.0004988132590565082, 0.00010946934516264133, 2.135475183728687e-05, 3.749203786860329e-06, 5.983990287889589e-07, 8.754959715303952e-08, 1.1823752162635768e-08, 1.4827632048770062e-09, 1.7355017640727309e-10, 1.9043623860460467e-11], [0.05710851073007685, 0.11692374065635502, 0.09437092934729181, 0.05522827711825848, 0.024240748299402138, 0.008511782858722604, 0.002490656316215798, 0.0006246838551555083, 0.00013709285251738046, 2.6743412412167487e-05, 4.695278308699127e-06, 7.493991096633053e-07, 1.0964187273273101e-07, 1.4807359165490531e-08, 1.8569238453229922e-09, 2.1734384820899917e-10, 2.3849094131509847e-11], [0.037971852416223244, 0.06666629233519267, 0.062205976098230406, 0.03458229351108937, 0.015178830779445462, 0.005329823570137951, 0.001559574411097244, 0.00039115832609387473, 8.584343947352956e-05, 1.6745924113209962e-05, 2.940042692984963e-06, 4.692512842983049e-07, 6.865445785733707e-08, 9.271924954106919e-09, 1.1627501127582774e-09, 1.3609421013621287e-10, 1.4933588666245174e-11], [0.015851224697881815, 0.027829624111999563, 0.024429909769643265, 0.015196949162569258, 0.006336352904219084, 0.002224917290951756, 0.0006510392000998917, 0.00016328775460826026, 3.583506100831082e-05, 6.9905308538163215e-06, 1.2273111366028391e-06, 1.958874027437261e-07, 2.865957725946908e-08, 3.870534526955385e-09, 4.853862040437178e-10, 5.6812079676897166e-11, 6.2339773919814915e-12], [0.0049627811477678035, 0.00871303867839004, 0.007648639014161178, 0.00447617881876607, 0.0020883497706124725, 0.0006965882950579516, 0.0002038306269890505, 5.112295142339993e-05, 1.1219421123020155e-05, 2.188630556656277e-06, 3.8425274306987547e-07, 6.132941321257467e-08, 8.972884583819836e-09, 1.2118064154831763e-09, 1.519671538778094e-10, 1.7787011625900664e-11, 1.9517649939484264e-12], [0.0012430179845437774, 0.002182337575400795, 0.0019157394954161617, 0.0011211396610271134, 0.0004920896640183347, 0.0001836665385511561, 5.1053054246041944e-05, 1.2804664592317664e-05, 2.8101062321390305e-06, 5.481819694324945e-07, 9.624302503465577e-08, 1.5361056902345164e-08, 2.247420665716913e-09, 3.035187576040161e-10, 3.806291265030145e-11, 4.455077643757953e-12, 4.888547201345136e-13], [0.00025944688134431717, 0.00045550481571356085, 0.0003998595706049128, 0.00023400802902435024, 0.00010271060455990805, 3.6065320777396264e-05, 1.1217455396967824e-05, 2.67263252539032e-06, 5.865347945406372e-07, 1.1441837861311945e-07, 2.0088166870368468e-08, 3.2062112994517913e-09, 4.690891765359545e-10, 6.335145272959676e-11, 7.944618746305903e-12, 9.298787428598807e-13, 1.0203539622630596e-13], [4.6416533958676635e-05, 8.149242202241002e-05, 7.153716877040937e-05, 4.186537748895416e-05, 1.8375515788698854e-05, 6.452292576887614e-06, 1.8880231706368031e-06, 5.033442158017541e-07, 1.0493443616541366e-07, 2.047010366389554e-08, 3.5938881780913883e-09, 5.736095762207029e-10, 8.3922742025304e-11, 1.1333937959548475e-11, 1.4213378242047774e-12, 1.663606362187347e-13, 1.8254717148208625e-14], [7.26616094545762e-06, 1.2757028665198257e-05, 1.1198608287532266e-05, 6.553711467295268e-06, 2.876549448852691e-06, 1.0100581049973677e-06, 2.955558947769252e-07, 7.412865217939951e-08, 1.729226646684053e-08, 3.204441501911474e-09, 5.625962926322301e-10, 8.979428546702711e-11, 1.3137477069762762e-11, 1.7742431486424307e-12, 2.22499797113953e-13, 2.604251232610812e-14, 2.8576393259086575e-15], [1.0110783164234337e-06, 1.775126529978315e-06, 1.5582740457630392e-06, 9.119417538941575e-07, 4.0026869700332017e-07, 1.405484761425505e-07, 4.112627820154276e-08, 1.031492054840044e-08, 2.263708065767657e-09, 4.693898683860678e-10, 7.828465631995935e-11, 1.2494776217584748e-11, 1.8280655076943995e-12, 2.468839857967421e-13, 3.0960602436306617e-14, 3.6237869923014214e-15, 3.9763737416129513e-16], [1.2662139369795282e-07, 2.2230621660561172e-07, 1.9514891006250295e-07, 1.1420612426730652e-07, 5.012725467944704e-08, 1.760144950417488e-08, 5.150408805036844e-09, 1.291778880534446e-09, 2.8349324236991865e-10, 5.530249431348074e-11, 1.0320494867601547e-11, 1.5647709508904544e-12, 2.2893597715973696e-13, 3.091827196321481e-14, 3.87732044742179e-15, 4.538213825540645e-16, 4.9797723563890074e-17], [1.4415731907734351e-08, 2.530936302639223e-08, 2.22175280763245e-08, 1.3002264637729247e-08, 5.70694290771587e-09, 2.0039092117796766e-09, 5.863694149959904e-10, 1.4706786493188668e-10, 3.227545093531203e-11, 6.296139290283543e-12, 1.1053984354205566e-12, 1.8753484023778635e-13, 2.6064155308877485e-14, 3.520017484054357e-15, 4.4142944930571243e-16, 5.1667156661556466e-17, 5.669426086281589e-18], [1.5044499485380256e-09, 2.6413275542504395e-09, 2.318658475684832e-09, 1.3569381346925936e-09, 5.955861290134092e-10, 2.0913132471056254e-10, 6.119449514330175e-11, 1.5348248930022447e-11, 3.368320166430119e-12, 6.570756512316425e-13, 1.1536123381916013e-13, 1.8412456137811198e-14, 2.8634280941148914e-15, 3.6735492562103454e-16, 4.6068317345360697e-17, 5.392071084429681e-18, 5.916708106350317e-19], [1.449294634165001e-10, 2.5444926600365207e-10, 2.2336530972909878e-10, 1.3071908170922675e-10, 5.7375107879198466e-11, 2.01464267411071e-11, 5.895101630852414e-12, 1.4785559891657655e-12, 3.2448326699740307e-13, 6.329863060555142e-14, 1.11131923881705e-14, 1.7737428824574642e-15, 2.595099044971701e-16, 3.725344052257953e-17, 4.437938609956631e-18, 5.194389947830608e-19, 5.699793016568634e-20], [1.2964355796894359e-11, 2.276121596648649e-11, 1.9980667006884555e-11, 1.1693196433436753e-11, 5.132367807734816e-12, 1.8021556014264772e-12, 5.273337332491762e-13, 1.3226107002195485e-13, 2.902595803728113e-14, 5.662243889416951e-15, 9.941069038911354e-16, 1.58666383482722e-16, 2.3213904580953255e-17, 3.1350852935676502e-18, 4.179045768887928e-19, 4.646530653188129e-20, 5.098628180461253e-21], [1.0823855236099048e-12, 1.900318924275845e-12, 1.6681727236692032e-12, 9.762572658882761e-13, 4.2849800668571805e-13, 1.5046078377020455e-13, 4.40267459426566e-14, 1.104238959279516e-14, 2.4233581120928306e-15, 4.72737011623956e-16, 8.299733041499738e-17, 1.3246951815868572e-17, 1.9381135984330623e-18, 2.6174620553478043e-19, 3.282440609755043e-20, 4.0837713725480045e-21, 4.256811074348007e-22], [8.47196758226798e-14, 1.487403514853143e-13, 1.3056997648503884e-13, 7.641288365512062e-14, 3.353907773637404e-14, 1.1776754720928906e-14, 3.446028760020288e-15, 8.643017170899443e-16, 1.896792863360199e-16, 3.700172027485297e-17, 6.49630540461718e-18, 1.0368555740990466e-18, 1.5169858815106747e-19, 2.048720460226247e-20, 2.569207535575561e-21, 3.0071316819803327e-22, 3.507423972840921e-23]] |
| Legacy trial inputs | {"lambda_home": 1.2523401168948094, "lambda_away": 1.7556765891860966, "rho": -0.03318338004165527, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2644 |
| Legacy p draw | 0.2518 |
| Legacy p away | 0.4837 |
| Legacy p over 1 5 | 0.8054 |
| Legacy p under 3 5 | 0.6458 |
| Legacy p btts yes | 0.5968 |
| Legacy p over 2 5 | 0.5751 |
| Legacy goal margin distribution | {"-1": 0.21831497348764287, "-10": 4.571284413174844e-06, "-11": 7.178164885461866e-07, "-12": 1.0357847027595918e-07, "-13": 1.3823004195486954e-08, "-14": 1.7150406417522507e-09, "-15": 1.9739927053878292e-10, "-16": 1.9043623860460467e-11, "-2": 0.1482049386759507, "-3": 0.0743757244852286, "-4": 0.02960279502294012, "-5": 0.009716640093653245, "-6": 0.002706719749894574, "-7": 0.0006539429884568106, "-8": 0.00013935797218771594, "-9": 2.6549191825005366e-05, "0": 0.2518362426493357, "1": 0.15321101111043203, "10": 1.5438542055635935e-07, "11": 1.7292558242908733e-08, "12": 1.7798896778921868e-09, "13": 1.694352649903109e-10, "14": 1.499524469765524e-11, "15": 1.2311258750952191e-12, "16": 8.47196758226798e-14, "2": 0.07468072426126977, "3": 0.026733438925606947, "4": 0.007589866070096756, "5": 0.001777032152689444, "6": 0.00035310204727460117, "7": 6.085196489796073e-05, "8": 9.250054921257723e-06, "9": 1.2570182213945908e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2697 |
| Legacy raw p draw | 0.2417 |
| Legacy raw p away | 0.4886 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2523 |
| Legacy lambda away | 1.7557 |
| Legacy model home team | Milan |
| Legacy model away team | Inter |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 54.1% |
| Market home draw odds | 1.82 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:44:41Z |
| Market reference home draw last update utc | 2026-10-31T11:45:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.7% |
| Market draw away odds | 1.32 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:44:41Z |
| Market reference draw away last update utc | 2026-10-31T11:45:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.2% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:44:41Z |
| Market reference home away last update utc | 2026-10-31T11:45:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.76 |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home away odds | 1.30 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 2.69, "price": 1.44, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 1.44, "price": 2.69, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.03, "price": 1.79, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.79, "price": 2.03, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.28, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.28, "price": 1.61, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 80.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market reference over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.0% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market reference under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.8% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:44:41Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.46 |
| Market reference btts yes last update utc | 2026-10-31T11:45:07Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021565944172805756, "mu": 8.170323559289312, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,536.0077 |
| Elo away rating | 1,691.0397 |
| Elo rating diff | -95.0319 |
| Elo home expectancy | 0.3665 |

</details>


---

## 2026-10-31 — Bologna vs Monza

The model's most likely 1X2 outcome is **Bologna win** at **58.3%**. Expected goals are 2.00 for Bologna and 0.98 for Monza (2.98 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 52.8%; Under 3.5 goals: 69.2%; Double Chance 1X: 81.9%; Double Chance X2: 41.7%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 84.8%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 58.3% | 1.72 |
| Draw | 23.6% | 4.24 |
| Monza win | 18.1% | 5.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 2.00 |
| Monza expected goals | 0.98 |
| Expected total goals | 2.98 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 52.8% |
| Under 2.5 | 47.2% |
| Over 3.5 | 30.8% |
| Under 3.5 | 69.2% |
| Over 4.5 | 15.2% |
| Under 4.5 | 84.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.22% |
| 2 | 1-0 | 10.85% |
| 3 | 2-0 | 10.48% |
| 4 | 2-1 | 9.65% |
| 5 | 3-0 | 6.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 58.3% | 57.2% | 1.72 | +0.2% |
| Draw | 23.6% | 24.4% | 3.92 | -7.6% |
| Monza win | 18.1% | 18.4% | 5.16 | -6.4% |
| Over 2.5 | 52.8% | 52.8% | 1.85 | -2.3% |
| Under 2.5 | 47.2% | 47.2% | 2.06 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:00:00+00:00 |
| Fixture id | 04aa939b89001eedf55668e66c74836e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:45:07Z |
| Market best draw last update utc | 2026-10-31T11:45:07Z |
| Market best away last update utc | 2026-10-31T11:45:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Bologna |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0050 |
| Dc lambda away | 0.9795 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:44:26.750844+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.19 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.37 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.25 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.60 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.12068364292273269, "-10": 8.79066822604341e-09, "-11": 7.265928006011805e-10, "-12": 5.515988389750336e-11, "-13": 3.871356238009174e-12, "-14": 2.525678971556464e-13, "-15": 1.532144025951444e-14, "-16": 7.956290700042438e-16, "-2": 0.04528781765034765, "-3": 0.012264141158168075, "-4": 0.0026093275221702604, "-5": 0.00045531938544667835, "-6": 6.719772500118037e-05, "-7": 8.581695519745618e-06, "-8": 9.65162684186427e-07, "-9": 9.693064233111558e-08, "0": 0.23579508263304708, "1": 0.23738053860468086, "10": 1.0779530447831296e-05, "11": 1.823734441469173e-06, "12": 2.833912313604898e-07, "13": 4.0711654917544956e-08, "14": 5.4365867703149586e-09, "15": 6.750568104177754e-10, "16": 7.175363860294859e-11, "2": 0.18022660615157152, "3": 0.0999003954245716, "4": 0.04350620652586098, "5": 0.015539295248789341, "6": 0.004694207715298537, "7": 0.0012270814468425667, "8": 0.00028248368243902807, "9": 5.8069286452052016e-05} |
| Raw goal margin distribution | {"-1": 0.11442029014669994, "-10": 1.3527975363410408e-08, "-11": 1.1871964334315104e-09, "-12": 9.571570612414806e-11, "-13": 7.135742655897685e-12, "-14": 4.946702615936471e-13, "-15": 3.203538325545887e-14, "-16": 1.936386841432143e-15, "-17": 1.0001879242527361e-16, "-2": 0.04459094091743792, "-3": 0.012662359330773372, "-4": 0.0028384900526784197, "-5": 0.0005233018767069394, "-6": 8.173594585939857e-05, "-7": 1.1059772043238258e-05, "-8": 1.3189517627858049e-06, "-9": 1.4053673045092906e-07, "0": 0.21576748345813768, "1": 0.23686749745565808, "10": 1.7464588496496286e-05, "11": 3.1371890615731273e-06, "12": 5.177187236479115e-07, "13": 7.900278454414653e-08, "14": 1.121015396186504e-08, "15": 1.4859981005660495e-09, "16": 1.8385396841159642e-10, "17": 1.9438155308201768e-11, "2": 0.18682360463137085, "3": 0.10859061675377134, "4": 0.049826180620385206, "5": 0.01880247712529262, "6": 0.006011300309937958, "7": 0.001664922655868024, "8": 0.0004064146508559362, "9": 8.863859096734528e-05} |
| Unadjusted home-win probability | 60.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 17.5% |
| Raw p over 1 5 | 80.1% |
| Raw p under 3 5 | 65.1% |
| Raw p btts yes | 54.3% |
| P home draw | 81.9% |
| P draw away | 41.7% |
| P home away | 76.4% |
| Raw p home draw | 82.5% |
| Raw p draw away | 39.1% |
| Raw p home away | 78.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9403 |
| Totals anchor target over 2 5 | 0.5279 |
| Totals anchor reference over odds | 1.85 |
| Totals anchor reference under odds | 2.06 |
| Totals anchor reference last update utc | 2026-10-31T11:45:07Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5651 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.97, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.5, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.67, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.5, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.72 |
| Reference draw odds | 3.92 |
| Reference away odds | 5.16 |
| Market reference 1x2 last update utc | 2026-10-31T11:45:07Z |
| Market reference home last update utc | 2026-10-31T11:45:07Z |
| Market reference draw last update utc | 2026-10-31T11:45:07Z |
| Market reference away last update utc | 2026-10-31T11:45:07Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:45:07Z |
| Market best over 2 5 last update utc | 2026-10-31T11:45:07Z |
| Market best under 2 5 last update utc | 2026-10-31T11:45:07Z |
| Home probability edge | +1.1% |
| Draw probability edge | -0.9% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0375 |
| Raw ev home | 0.0477 |
| Raw edge prob draw | -0.0286 |
| Raw ev draw | -0.1542 |
| Raw edge prob away | -0.0089 |
| Raw ev away | -0.0963 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06382510805498882, 0.05198837664677976, 0.026163787195056867, 0.008222852466602157, 0.0019382315196788415, 0.0003654927716759986, 5.743421463978751e-05, 7.735988077128461e-06, 9.117356773607519e-07, 9.55145612468453e-08, 9.00560159379484e-09, 7.719038190947585e-10, 6.064920165707282e-11, 4.398705447271509e-12, 2.962374701935872e-13, 1.8620523048295848e-14, 1.0972738727740632e-15], [0.10472384469752337, 0.11185724711384444, 0.04987847193256376, 0.01567599189304356, 0.003695031829007405, 0.00069677301751791, 0.00010949220927086267, 1.4747836821138811e-05, 1.7381269024289823e-06, 1.8208833173822793e-07, 1.716821968406822e-08, 1.4715523669536176e-09, 1.1562123938831903e-10, 8.385663151732052e-12, 5.647451659909595e-13, 3.549804274549185e-14, 2.0918356986115856e-15], [0.10304643731122032, 0.09715745410655456, 0.048649950295080624, 0.014942303952846585, 0.0035220921955804604, 0.0006641617503333179, 0.00010436761402766125, 1.4057589588715573e-05, 1.6567768509907715e-06, 1.7356599937428936e-07, 1.6364690579001327e-08, 1.4026788798806053e-09, 1.102097853923852e-10, 7.993186556505552e-12, 5.383132361711962e-13, 3.3836617679654606e-14, 1.9939309130378e-15], [0.0654823502532979, 0.06174011062904918, 0.029105867808213365, 0.009716180367123881, 0.002238164470246017, 0.00042205119842056075, 6.632191112264848e-05, 8.933098796858212e-06, 1.0528228328794505e-06, 1.1029502678258394e-07, 1.0399179517915536e-08, 8.913525989048835e-10, 7.00344034855745e-11, 5.079386103880919e-12, 3.420789383575352e-13, 2.1501968511480178e-14, 1.2670722621305254e-15], [0.03120878052589903, 0.029425235270471677, 0.013871808768754641, 0.004359683714746694, 0.0010915189059610727, 0.00020114890762547988, 3.160891385661093e-05, 4.2575002071383305e-06, 5.017736320839405e-07, 5.256642852067543e-08, 4.956231869635822e-09, 4.2481718390996823e-10, 3.337828161617449e-11, 2.4208270703346866e-12, 1.6303425989501935e-13, 1.0247802859149521e-14, 6.038845579965178e-16], [0.011899242811489425, 0.011219215021169392, 0.005289025011309847, 0.0016622544754677723, 0.0003918146447555297, 7.847782001918572e-05, 1.2051805121803333e-05, 1.6232940820184815e-06, 1.9131559080352024e-07, 2.004245876192566e-08, 1.8897055717347657e-09, 1.6197373741158867e-10, 1.2726427335138324e-11, 9.230097629298257e-13, 6.216148828604135e-14, 3.907268802255867e-15, 2.302483103992585e-16], [0.0037807730469015676, 0.0035647062953009087, 0.0016804937527487563, 0.0005281518343227599, 0.00012449214389025464, 2.3475512734348555e-05, 3.9183218559330945e-06, 5.157728613256269e-07, 6.078713079655703e-08, 6.3681352739149475e-09, 6.004203801351152e-10, 5.1464278056445025e-11, 4.043596236693626e-12, 2.932699575087742e-13, 1.9750708779572794e-14, 1.2414652603193061e-15, 7.315731091827179e-17], [0.001029662983624621, 0.0009708189500485942, 0.0004576688920367428, 0.00014383788362574726, 3.3904429259755704e-05, 6.3933661672647955e-06, 1.0046654631160667e-06, 1.4373406341356106e-07, 1.6554883799030784e-08, 1.7343101754383545e-09, 1.6351963801307951e-10, 1.4015880201302632e-11, 1.101240755262834e-12, 7.986970275918075e-14, 5.378945913545967e-15, 3.3810303029278184e-16, 1.9923802381048593e-17], [0.0002453678429934237, 0.00023134535814041271, 0.00010906212093683006, 3.4276449486170284e-05, 8.079397635626972e-06, 1.5235339046633126e-06, 2.394109543950044e-07, 3.224698553552907e-08, 4.036783018596604e-09, 4.132846898417722e-10, 3.8966595385507235e-11, 3.339972736071102e-12, 2.624247671642036e-13, 1.9032884543988446e-14, 1.2817983916825207e-15, 8.056967432241327e-17, 4.7478257373651165e-18], [5.197418256284246e-05, 4.900391890137881e-05, 2.310170116470206e-05, 7.2604886665935655e-06, 1.7113900606899356e-06, 3.2271722461925674e-07, 5.071238553294781e-08, 6.83060458484712e-09, 8.050304416007737e-10, 8.957896993095076e-11, 8.25396236813741e-12, 7.074780078012443e-13, 5.5587205687622654e-14, 4.031573998933801e-15, 2.715124476186993e-16, 1.706638861545562e-17, 1.0056915308865082e-18], [9.908324000848246e-06, 9.342074888798367e-06, 4.404093125156461e-06, 1.3841347870380312e-06, 3.262582762633035e-07, 6.152259957750917e-08, 9.667775844455645e-09, 1.3021819682591922e-09, 1.53470474235587e-10, 1.607775737524121e-11, 1.6101329627349332e-12, 1.3487314237782597e-13, 1.0597108354495258e-14, 7.685766171797366e-16, 5.176095454732019e-17, 3.253525107814108e-18, 1.917243724013201e-19], [1.7171967042934573e-06, 1.6190609238185855e-06, 7.632667441307641e-07, 2.398823145464514e-07, 5.6543330304887714e-08, 1.0662389040267602e-08, 1.6755076657289252e-09, 2.2567919499742043e-10, 2.6597736664762118e-11, 2.786411907284265e-12, 2.6271717302200244e-13, 2.391839575669542e-14, 1.8365688828728302e-15, 1.3320085555388288e-16, 8.970613047386457e-18, 5.63863534538849e-19, 3.3227462120949336e-20], [2.728043758192827e-07, 2.5721392524885675e-07, 1.2125722533452143e-07, 3.810917230758097e-08, 8.982819435887034e-09, 1.6938923651553196e-09, 2.6618140006137e-10, 3.585277782838571e-11, 4.2254791957695744e-12, 4.426664453999543e-13, 4.173685764949261e-14, 3.577422283354852e-15, 2.9855560727032676e-16, 2.1161102957580318e-17, 1.4251264790980886e-18, 8.957881132809217e-20, 5.278717948444983e-21], [4.000557453099038e-08, 3.771930280095015e-08, 1.7781844411303648e-08, 5.588544276413044e-09, 1.3172913790754774e-09, 2.4840194391378547e-10, 3.90343439577842e-11, 5.257653845357205e-12, 6.19648135730382e-13, 6.491510783370917e-14, 6.1205285449387295e-15, 5.246134097217892e-16, 4.121936398181686e-17, 3.175369027920632e-18, 2.0898859633180646e-19, 1.3136342854549668e-20, 7.74101015353529e-22], [5.44759745192251e-09, 5.136273637754522e-09, 2.4213708074723697e-09, 7.609974339091224e-10, 1.793768304597676e-10, 3.3825130936916856e-11, 5.315344053293558e-12, 7.159397665660631e-13, 8.437808092665819e-14, 8.839552491672076e-15, 8.334382419629703e-16, 7.143711114137193e-17, 5.612880325547297e-18, 4.070854452869576e-19, 2.9120163554807755e-20, 1.788788405140639e-21, 1.0541007767564525e-22], [6.923509316647103e-10, 6.527838867993542e-10, 3.0773902610362594e-10, 9.671736706160155e-11, 2.279752070227848e-11, 4.298933818905884e-12, 6.755424643422462e-13, 9.099085767119195e-14, 1.0723854590437001e-14, 1.123444317815451e-15, 1.0592407908268272e-16, 9.079149274642083e-18, 7.133572105890016e-19, 5.173766780658553e-20, 3.484351477602601e-21, 2.3263066844059585e-22, 1.3396871947619194e-23], [8.249332907892016e-11, 7.77789319379932e-11, 3.666697853609139e-11, 1.1523834552335421e-11, 2.7163152260872606e-12, 5.122161984512832e-13, 8.049060710263803e-14, 1.0841523311010543e-14, 1.2777428689181313e-15, 1.3385792893866451e-16, 1.2620810507381444e-17, 1.0817769062126391e-18, 8.499621858303125e-20, 6.1645218644862215e-21, 4.151590471285617e-22, 2.609554625454424e-23, 1.6333628745744666e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9063934269419267, "lambda_away": 0.9428511711969247, "rho": -0.03318338004165527, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T11:45:07Z", "over": 1.85, "under": 2.06, "bookmaker": "pinnacle", "event_id": "04aa939b89001eedf55668e66c74836e", "kickoff_utc": "2026-10-31T14:00:00Z", "home_team": "Bologna", "away_team": "Monza"}} |
| Legacy p home | 0.5837 |
| Legacy p draw | 0.2352 |
| Legacy p away | 0.1811 |
| Legacy p over 1 5 | 0.7795 |
| Legacy p under 3 5 | 0.6823 |
| Legacy p btts yes | 0.5259 |
| Legacy p over 2 5 | 0.5384 |
| Legacy goal margin distribution | {"-1": 0.1192610504646039, "-10": 1.0592610146930733e-08, "-11": 8.958708020291102e-10, "-12": 6.959528389804555e-11, "-13": 4.998554303204253e-12, "-14": 3.337294438521169e-13, "-15": 2.0712358746907432e-14, "-16": 1.0972738727740632e-15, "-2": 0.045817217251165845, "-3": 0.012652823307914719, "-4": 0.0027488276808148855, "-5": 0.000490149902087375, "-6": 7.395424566907172e-05, "-7": 9.658518000791373e-06, "-8": 1.1111143736618247e-06, "-9": 1.1415797846422737e-07, "0": 0.23522254874093373, "1": 0.23576317821835108, "10": 1.1654414450532652e-05, "11": 1.9929767811244276e-06, "12": 3.1304448310999285e-07, "13": 4.546111102940087e-08, "14": 6.137048317257956e-09, "15": 7.701298636027035e-10, "16": 8.249332907892016e-11, "2": 0.18045174309240758, "3": 0.1007602423741807, "4": 0.04426073919604944, "5": 0.015957669072962553, "6": 0.0048682517987434564, "7": 0.001285552454700585, "8": 0.0002990249739634978, "9": 6.211898517097317e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5959 |
| Legacy raw p draw | 0.2261 |
| Legacy raw p away | 0.1781 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9064 |
| Legacy lambda away | 0.9429 |
| Legacy model home team | Bologna |
| Legacy model away team | Monza |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 80.2% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:44:41Z |
| Market reference home draw last update utc | 2026-10-31T11:45:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.6% |
| Market draw away odds | 2.24 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:44:41Z |
| Market reference draw away last update utc | 2026-10-31T11:45:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:44:41Z |
| Market reference home away last update utc | 2026-10-31T11:45:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.14 |
| Market reference dc home away odds | 1.27 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.1, "price": 1.75, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.1, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.2, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.2, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 77.4% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 4.02 |
| Market reference over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.9% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 3.08 |
| Market reference under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.9% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:44:41Z |
| Market reference btts yes odds | 1.81 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-31T11:45:07Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021565944172805756, "mu": 8.813933594337694, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,462.4109 |
| Elo away rating | 1,358.1569 |
| Elo rating diff | 164.2540 |
| Elo home expectancy | 0.7202 |

</details>


---

## 2026-10-31 — Udinese vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **60.1%**. Expected goals are 0.86 for Udinese and 1.73 for AS Roma (2.60 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 61.2%; Under 3.5 goals: 60.6%; Double Chance 1X: 39.9%; Double Chance X2: 82.4%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 78.5%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 17.6% | 5.68 |
| Draw | 22.3% | 4.48 |
| AS Roma win | 60.1% | 1.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 0.86 |
| AS Roma expected goals | 1.73 |
| Expected total goals | 2.60 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 61.2% |
| Under 2.5 | 38.8% |
| Over 3.5 | 39.4% |
| Under 3.5 | 60.6% |
| Over 4.5 | 21.5% |
| Under 4.5 | 78.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.30% |
| 2 | 1-2 | 9.67% |
| 3 | 0-2 | 9.09% |
| 4 | 0-1 | 8.31% |
| 5 | 1-3 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 17.6% | 17.3% | 5.46 | -3.9% |
| Draw | 22.3% | 21.5% | 4.42 | -1.4% |
| AS Roma win | 60.1% | 61.1% | 1.61 | -3.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:00:00+00:00 |
| Fixture id | 34cd26b96f78bd7aa3dbff3d1daca7a7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:45:07Z |
| Market best draw last update utc | 2026-10-31T11:45:07Z |
| Market best away last update utc | 2026-10-31T11:45:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Udinese |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8643 |
| Dc lambda away | 1.7318 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:44:26.750844+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.31 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.85 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.65 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.2239353800713578, "-10": 2.6003376212002775e-05, "-11": 4.950534508905234e-06, "-12": 8.661353637930216e-07, "-13": 1.4016070158373726e-07, "-14": 2.1094788309740652e-08, "-15": 2.9661164703030056e-09, "-16": 3.8870265064661254e-10, "-17": 4.2971292259248e-11, "-2": 0.18220320261173245, "-3": 0.11048903968738019, "-4": 0.0532055621637626, "-5": 0.021144500326878597, "-6": 0.00713484187923286, "-7": 0.002088699713787471, "-8": 0.0005394576305398974, "-9": 0.00012457601167006066, "0": 0.22317303077707643, "1": 0.11195059790162964, "10": 2.5243108837128953e-08, "11": 2.3985546303016313e-09, "12": 2.0944389951817598e-10, "13": 1.6915803392121692e-11, "14": 1.2706500546748164e-12, "15": 8.917095344613511e-14, "16": 5.832263457863878e-15, "17": 3.2179735332930404e-16, "2": 0.04594028994021971, "3": 0.013904050812892399, "4": 0.0033416703514225037, "5": 0.0006628090317882224, "6": 0.0001116245614829463, "7": 1.630931955292024e-05, "8": 2.1023334346815084e-06, "9": 2.423054046913072e-07} |
| Raw goal margin distribution | {"-1": 0.2502622545181205, "-10": 5.7074739032342265e-06, "-11": 8.885693831641159e-07, "-12": 1.2702449632901855e-07, "-13": 1.6784238469089758e-08, "-14": 2.061320977577625e-09, "-15": 2.3563316032695695e-10, "-16": 2.332215480755239e-11, "-2": 0.17914379669501068, "-3": 0.0926282186851688, "-4": 0.03743033611779784, "-5": 0.012367809989651429, "-6": 0.0034498976337139975, "-7": 0.0008317068117818787, "-8": 0.00017643236141532578, "-9": 3.340087014940505e-05, "0": 0.2412902306898078, "1": 0.1234730573698335, "10": 5.47379026894684e-09, "11": 4.253240940503675e-10, "12": 3.034593645543126e-11, "13": 2.0012397738109177e-12, "14": 1.2266693932350615e-13, "15": 6.998464053109028e-15, "16": 3.4571595568511407e-16, "2": 0.044624217940161456, "3": 0.011515865342408779, "4": 0.002322530438884302, "5": 0.0003830142338368177, "6": 5.332277467311232e-05, "7": 6.415953556915427e-06, "8": 6.792874983588296e-07, "9": 6.418264017270707e-08} |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 57.6% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 47.9% |
| P home draw | 39.9% |
| P draw away | 82.4% |
| P home away | 77.7% |
| Raw p home draw | 42.4% |
| Raw p draw away | 81.8% |
| Raw p home away | 75.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2297 |
| Totals anchor target over 2 5 | 0.6124 |
| Totals anchor reference over odds | 1.60 |
| Totals anchor reference under odds | 2.48 |
| Totals anchor reference last update utc | 2026-10-31T11:45:07Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4880 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:24Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:24Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.27, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.11, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.27, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.46 |
| Reference draw odds | 4.42 |
| Reference away odds | 1.61 |
| Market reference 1x2 last update utc | 2026-10-31T11:45:07Z |
| Market reference home last update utc | 2026-10-31T11:45:07Z |
| Market reference draw last update utc | 2026-10-31T11:45:07Z |
| Market reference away last update utc | 2026-10-31T11:45:07Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-31T11:44:24Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:44:24Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.8% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | 0.0092 |
| Raw ev home | -0.0042 |
| Raw edge prob draw | 0.0259 |
| Raw ev draw | 0.0665 |
| Raw edge prob away | -0.0351 |
| Raw ev away | -0.0721 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07492405889122002, 0.13098327566460558, 0.11228950968264757, 0.06225296611977812, 0.025884642752891485, 0.008610220809793038, 0.0023867402479124263, 0.0005670864034911352, 0.00011789662307935047, 2.178717763555328e-05, 3.623623707214246e-06, 5.47888929364747e-07, 7.593699325417904e-08, 9.71520933491923e-09, 1.154160601624247e-09, 1.279726325865327e-10], [0.06119712866828139, 0.11073116105541383, 0.10138837950541807, 0.05620941236744369, 0.023371746748288527, 0.007774335621875532, 0.0021550341320405266, 0.000512033329311143, 0.00010645115110894105, 1.9672065900976954e-05, 3.271840233786703e-06, 4.946995570133332e-07, 6.856498627800887e-08, 8.77205122550809e-09, 1.0421140266655204e-09, 1.1554897581849416e-10], [0.029241907711855798, 0.04863487680751219, 0.0402368121262984, 0.02537628514450447, 0.010551402066484325, 0.0035097993243576073, 0.0009729110895753554, 0.00023116241961667114, 4.805840606983157e-05, 8.881145214992709e-06, 1.477104051134372e-06, 2.2333691975939276e-07, 3.09543289893482e-08, 3.960227723882479e-09, 4.704724988206571e-10, 5.216570739714551e-11], [0.008801028831429076, 0.014637791665773347, 0.012172721448510023, 0.006713858286348217, 0.0031756886286006076, 0.0010563553291592417, 0.0002928201071607296, 6.957367965990735e-05, 1.446428945679314e-05, 2.6729861766703007e-06, 4.4456864679124834e-07, 6.721841438300042e-08, 9.316421643118067e-09, 1.19192217964573e-09, 1.4159958602277886e-10, 1.5700476840915173e-11], [0.0019866549727595574, 0.0033041866081814767, 0.002747746662451579, 0.0015233424775543854, 0.0006301490730197362, 0.0002384509365747075, 6.609824068947978e-05, 1.5704856706746177e-05, 3.265021979493477e-06, 6.033727853539306e-07, 1.0035241672278552e-07, 1.5173203014415834e-08, 2.1029945180420385e-09, 2.6905242224403713e-10, 3.196325419458607e-11, 3.5440663799797664e-12], [0.00035875787309738125, 0.0005966828544070016, 0.0004961987672485813, 0.0002750911027530749, 0.00011438225940209523, 3.7852485987444694e-05, 1.1936277094103412e-05, 2.8360440371712735e-06, 5.896103536046914e-07, 1.0895940167090972e-07, 1.8122029279014576e-08, 2.740035947945864e-09, 3.7976692016139333e-10, 4.8586531672327566e-11, 5.772048619087765e-12, 6.400012755266487e-13], [5.3988242076150086e-05, 8.979275662521639e-05, 7.467125092703424e-05, 4.139751671567287e-05, 1.7212993979761635e-05, 5.725699225531327e-06, 1.5790032390487506e-06, 4.2678654184089145e-07, 8.872844023237382e-08, 1.6396926715765188e-08, 2.727122042450475e-09, 4.1233861372263355e-10, 5.714982152495354e-11, 7.311620539277027e-12, 8.686158032775248e-13, 9.631159727273383e-14], [6.963861783854296e-06, 1.1582232024656148e-05, 9.631731849129504e-06, 5.3398031407675246e-06, 2.220278089297698e-06, 7.385492931272176e-07, 2.0472475235119701e-07, 4.83924996021768e-08, 1.1444947461035946e-08, 2.1150148057704517e-09, 3.5176735231609165e-10, 5.318693485259839e-11, 7.371669140668896e-12, 9.431148874915606e-13, 1.1204144022256349e-13, 1.2423087431584412e-14], [7.859757596236587e-07, 1.3072277848510288e-06, 1.0870847227557988e-06, 6.026764976203565e-07, 2.505915269394778e-07, 8.335631287671842e-08, 2.3106244457071807e-08, 5.490013870930714e-09, 1.1355053780114173e-09, 2.3871099401123574e-10, 3.970219693165987e-11, 6.002939578689911e-12, 8.320029076344954e-13, 1.0644459397904532e-13, 1.264554909639783e-14, 1.4021308699074236e-15], [7.885253120754977e-08, 1.3114681774625956e-07, 1.0906110141029844e-07, 6.046314629273136e-08, 2.5140439710003405e-08, 8.362670453863537e-09, 2.318119661874728e-09, 5.507822407840252e-10, 1.1450700605896179e-10, 2.105209353350174e-11, 3.983098313440353e-12, 6.022411946805205e-13, 8.347017631998531e-14, 1.0678987953300975e-14, 1.2686568797462161e-15, 1.4066791096634222e-16], [7.1197482130152214e-09, 1.1841500925745347e-08, 9.847338696479272e-09, 5.459334927852455e-09, 2.2699791364792087e-09, 7.550817596864844e-10, 2.0930752719587807e-10, 4.9731198409609505e-11, 1.0339060005824631e-11, 1.910647913807802e-12, 3.1614506376425625e-13, 5.4377527315448444e-14, 7.53668435994837e-15, 9.642265661352165e-16, 1.1454949402610637e-16, 1.2701178927218868e-17], [5.844144510870561e-10, 9.719928368977473e-10, 8.083048538782584e-10, 4.481217775832129e-10, 1.8632802331400791e-10, 6.197981711015344e-11, 1.7180712007618104e-11, 4.08211500616325e-12, 8.486671013189126e-13, 1.568328286845034e-13, 2.608429442293869e-14, 3.923667066020643e-15, 6.186380643607473e-16, 7.914717241564125e-17, 9.402633024464209e-18, 1.0425582884153083e-18], [4.397326334009697e-11, 7.313593444188403e-11, 6.081951281757842e-11, 3.3718154808536067e-11, 1.401993263784998e-11, 4.6635650683966984e-12, 1.292733217113443e-12, 3.071517444797729e-13, 6.385650092149108e-14, 1.180061729015778e-14, 1.9626680099490624e-15, 2.9675379166125207e-16, 4.091860048670591e-17, 5.9552932833596335e-18, 7.07485000252785e-19, 7.84455108504118e-20], [3.054177972784335e-12, 5.0796812204683834e-12, 4.224239964322669e-12, 2.3419059191192605e-12, 9.737591934278116e-13, 3.2390949919688764e-13, 8.978722561157546e-14, 2.1333328960304903e-14, 4.4351750068015435e-15, 8.196158905494226e-16, 1.3631777467852752e-16, 2.0611135608068086e-17, 2.8566878827895923e-18, 3.636010938538395e-19, 4.913861150434715e-20, 5.44845965718163e-21], [1.9697690133865373e-13, 3.2761020330581335e-13, 2.7243916566021937e-13, 1.51039453262188e-13, 6.280186363749315e-14, 2.089029848113025e-14, 5.790759293781209e-15, 1.3758769368662958e-15, 2.8604326189215833e-16, 5.2860507752652363e-17, 8.791711908352896e-18, 1.3292996221326369e-18, 1.8423992716134597e-19, 2.3571244837564622e-20, 2.785866006245977e-21, 3.513942900196813e-22], [1.1856951365072417e-14, 1.9720374424106396e-14, 1.6399374318618298e-14, 9.091763751821499e-15, 3.7803348398980125e-15, 1.2574837527104562e-15, 3.485726034199283e-16, 8.282040083827416e-17, 1.7218267835023778e-17, 3.181918617344193e-18, 5.292138306808271e-19, 8.001669668941471e-20, 1.1090253938459556e-20, 1.418862322200485e-21, 1.6855992855726794e-22, 1.8593828469294292e-23]] |
| Legacy trial inputs | {"lambda_home": 0.9029194249040872, "lambda_away": 1.6631909684809565, "rho": -0.03318338004165527, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1864 |
| Legacy p draw | 0.2333 |
| Legacy p away | 0.5803 |
| Legacy p over 1 5 | 0.7329 |
| Legacy p under 3 5 | 0.7404 |
| Legacy p btts yes | 0.4803 |
| Legacy p over 2 5 | 0.4806 |
| Legacy goal margin distribution | {"-1": 0.2611744546310359, "-10": 4.150502118652044e-06, "-11": 6.205592870190411e-07, "-12": 8.519521745534871e-08, "-13": 1.0809489068981896e-08, "-14": 1.269709577442741e-09, "-15": 1.279726325865327e-10, "-2": 0.18017570461422858, "-3": 0.08944364352142678, "-4": 0.034704839906535216, "-5": 0.011011503565539668, "-6": 0.0029496081200284644, "-7": 0.0006828788288568588, "-8": 0.0001391151639079334, "-9": 2.5291946131524955e-05, "0": 0.23327552047090389, "1": 0.12364838769169588, "10": 8.154966527997058e-09, "11": 6.619294452813648e-10, "12": 4.9334475489977396e-11, "13": 3.398187550408767e-12, "14": 2.1669727576276013e-13, "15": 1.1856951365072417e-14, "2": 0.04692051235363127, "3": 0.012645117726688448, "4": 0.0026636080488860814, "5": 0.0004588109510831696, "6": 6.672035524316412e-05, "7": 8.385801087812178e-06, "8": 9.274323875596975e-07, "9": 9.153705014004643e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1997 |
| Legacy raw p draw | 0.2511 |
| Legacy raw p away | 0.5492 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9029 |
| Legacy lambda away | 1.6632 |
| Legacy model home team | Udinese |
| Legacy model away team | Roma |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 40.4% |
| Market home draw odds | 2.46 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:44:42Z |
| Market reference home draw last update utc | 2026-10-31T11:45:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.8% |
| Market draw away odds | 1.18 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:44:42Z |
| Market reference draw away last update utc | 2026-10-31T11:45:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.8% |
| Market home away odds | 1.25 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:44:42Z |
| Market reference home away last update utc | 2026-10-31T11:45:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.35 |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home away odds | 1.22 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:42Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.39, "price": 1.56, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:42Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.56, "price": 2.39, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:42Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.9, "price": 1.94, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:42Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.94, "price": 1.9, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:42Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.54, "price": 2.45, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:42Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.45, "price": 1.54, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.1% |
| Market under 3 5 odds | 1.60 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market reference under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:44:42Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-31T11:45:07Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021565944172805756, "mu": 8.940812762248761, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,376.7934 |
| Elo away rating | 1,594.6836 |
| Elo rating diff | -157.8902 |
| Elo home expectancy | 0.2872 |

</details>


---

## 2026-11-01 — Como vs Venezia

The model's most likely 1X2 outcome is **Como win** at **75.2%**. Expected goals are 2.14 for Como and 0.58 for Venezia (2.72 combined). The most likely exact score is 2-0 at 9.6%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 70.5%; Under 3.5 goals: 49.7%; Double Chance 1X: 90.7%; Double Chance X2: 24.8%; Double Chance 12 (either team wins): 84.5%; Under 4.5 goals: 69.1%; BTTS Yes (both teams score): 53.6%; BTTS No (at least one team does not score): 46.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 75.2% | 1.33 |
| Draw | 15.5% | 6.45 |
| Venezia win | 9.3% | 10.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.14 |
| Venezia expected goals | 0.58 |
| Expected total goals | 2.72 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 88.2% |
| Under 1.5 | 11.8% |
| Over 2.5 | 70.5% |
| Under 2.5 | 29.5% |
| Over 3.5 | 50.3% |
| Under 3.5 | 49.7% |
| Over 4.5 | 30.9% |
| Under 4.5 | 69.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.57% |
| 2 | 3-0 | 9.40% |
| 3 | 2-1 | 7.64% |
| 4 | 3-1 | 7.51% |
| 5 | 1-1 | 7.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 75.2% | 75.9% | 1.30 | -2.3% |
| Draw | 15.5% | 14.4% | 6.32 | -2.0% |
| Venezia win | 9.3% | 9.7% | 9.20 | -14.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T11:30:00+00:00 |
| Fixture id | 9507f4bcbcfd4e4953720628a2b86a17 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:45:07Z |
| Market best draw last update utc | 2026-10-31T11:45:07Z |
| Market best away last update utc | 2026-10-31T11:45:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Como |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1416 |
| Dc lambda away | 0.5798 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:44:26.750844+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 53.6% |
| P btts no | 46.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.13 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.48 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.39 |
| Fair Over 3.5 odds | 1.99 |
| Fair Under 3.5 odds | 2.01 |
| Fair Over 4.5 odds | 3.23 |
| Fair Under 4.5 odds | 1.45 |
| Goal margin distribution | {"-1": 0.06709026459880066, "-10": 1.1293009976278008e-09, "-11": 8.054211906937183e-11, "-12": 5.279464343152356e-12, "-13": 3.201084555905383e-13, "-14": 1.8052827528661016e-14, "-15": 9.515285735952243e-16, "-16": 4.70715500657461e-17, "-17": 2.1936707180684014e-18, "-18": 9.66061958839156e-20, "-19": 4.010639312831773e-21, "-2": 0.02065288426356945, "-20": 1.4322879176024519e-22, "-3": 0.004670133933348348, "-4": 0.0008400337735464723, "-5": 0.00012482721324978203, "-6": 1.575973846762928e-05, "-7": 1.7269554640936265e-06, "-8": 1.6700673604974003e-07, "-9": 1.4443664805088406e-08, "0": 0.15503073189087116, "1": 0.1765403076129433, "10": 0.0003725577669464665, "11": 9.81432848497907e-05, "12": 2.3761892507851287e-05, "13": 5.32159647502405e-06, "14": 1.1085203105195273e-06, "15": 2.1581115245420325e-07, "16": 3.94333957549917e-08, "17": 6.7878266654108425e-09, "18": 1.104124163313577e-09, "19": 1.6930904801337678e-10, "2": 0.1966688589373238, "20": 2.2333177494713638e-11, "3": 0.16426228141479593, "4": 0.10913370258182042, "5": 0.05989975492702887, "6": 0.027933052941972014, "7": 0.011305874599699338, "8": 0.004038412175062771, "9": 0.0012900533869423829} |
| Raw goal margin distribution | {"-1": 0.06517055376304225, "-10": 8.70798502274678e-11, "-11": 4.5474291869815186e-12, "-12": 2.179917698116008e-13, "-13": 9.656871096976429e-15, "-14": 3.975904870471134e-16, "-15": 1.5288434494669074e-17, "-16": 5.502170157681785e-19, "-17": 1.7488190714467067e-20, "-2": 0.016406208807223526, "-3": 0.002888688075167687, "-4": 0.00039513020003807415, "-5": 4.4047195408626855e-05, "-6": 4.136712954686762e-06, "-7": 3.353251051542549e-07, "-8": 2.389597823830007e-08, "-9": 1.5187011192668123e-09, "0": 0.18079401549117902, "1": 0.24635171875416084, "10": 4.115797059441041e-05, "11": 7.938818114278418e-06, "12": 1.4056708289670874e-06, "13": 2.3000305112459982e-07, "14": 3.497733974723431e-08, "15": 4.967838118366435e-09, "16": 6.603771896115363e-10, "17": 7.752763846081946e-11, "2": 0.22382855474340413, "3": 0.1455665309702583, "4": 0.07354526818868669, "5": 0.030282128681418198, "6": 0.010504542774576676, "7": 0.003145150738631749, "8": 0.0008278541636803132, "9": 0.00019433676285797157} |
| Unadjusted home-win probability | 73.4% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 8.5% |
| Raw p over 1 5 | 75.7% |
| Raw p under 3 5 | 70.9% |
| Raw p btts yes | 39.0% |
| P home draw | 90.7% |
| P draw away | 24.8% |
| P home away | 84.5% |
| Raw p home draw | 91.5% |
| Raw p draw away | 26.6% |
| Raw p home away | 81.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.3769 |
| Totals anchor target over 2 5 | 0.7054 |
| Totals anchor reference over odds | 1.38 |
| Totals anchor reference under odds | 3.09 |
| Totals anchor reference last update utc | 2026-10-31T11:45:07Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5217 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.88, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:44:41Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 7.63, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:44:41Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.11, "price": 7.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.82, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.30 |
| Reference draw odds | 6.32 |
| Reference away odds | 9.20 |
| Market reference 1x2 last update utc | 2026-10-31T11:45:07Z |
| Market reference home last update utc | 2026-10-31T11:45:07Z |
| Market reference draw last update utc | 2026-10-31T11:45:07Z |
| Market reference away last update utc | 2026-10-31T11:45:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-31T11:44:45Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:44:45Z |
| Home probability edge | -0.7% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | -0.0247 |
| Raw ev home | -0.0454 |
| Raw edge prob draw | 0.0368 |
| Raw ev draw | 0.1426 |
| Raw edge prob away | -0.0121 |
| Raw ev away | -0.2188 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06017321336118706, 0.038078127473301485, 0.012430428005356252, 0.002514348348243992, 0.00038143985952815776, 4.629314519238342e-05, 4.681942291099434e-06, 4.058715732921202e-07, 3.078642543924775e-08, 2.075761132766426e-09, 1.2596154951232727e-10, 6.948737854227248e-12, 3.5138668472695317e-13, 1.6402217513052126e-14, 7.109436013508325e-16, 2.8761034921417636e-17, 1.090800040492782e-18, 3.893649394139956e-20], [0.13870265271911789, 0.07692837613354234, 0.026432625643674424, 0.005346624315613806, 0.0008111110098653913, 9.843984263544816e-05, 9.95589434350872e-06, 8.630637136240998e-07, 6.546565075570045e-08, 4.4139925772839064e-09, 2.6785034934612336e-10, 1.4776111194053315e-11, 7.472045765083218e-13, 3.487841891379845e-14, 1.511782704519488e-15, 6.115876853756744e-17, 2.3195266574913308e-18, 8.279632590178984e-20], [0.15050237634457073, 0.09132800605233586, 0.024019502265378953, 0.005684652166887973, 0.00086239161153567, 0.0001046634720736814, 1.058533254110584e-05, 9.176289038090709e-07, 6.960456382512827e-08, 4.693056962279527e-09, 2.847845629186195e-10, 1.571029635879882e-11, 7.944448429923034e-13, 3.708352559519394e-14, 1.607361639757152e-15, 6.502538902462045e-17, 2.4661733200808886e-18, 8.803093048327234e-20], [0.10667835869328743, 0.0647346708073774, 0.019641179597578513, 0.0034437874224357255, 0.0006112762064225255, 7.418705064429262e-05, 7.50304366704807e-06, 6.504292339129141e-07, 4.933676667952968e-08, 3.3265096947297865e-09, 2.018596017632882e-10, 1.113569546772307e-11, 5.631145100907418e-13, 2.6285363335384403e-14, 1.139322220157289e-15, 4.609097838201182e-17, 1.748060917238104e-18, 6.239765381975082e-20], [0.056711424546408304, 0.03441368468729701, 0.010441473682146343, 0.0021120352488768015, 0.0002777353718632898, 3.943867693944103e-05, 3.988703050968272e-06, 3.457755525456114e-07, 2.622798433705145e-08, 1.7684102555229375e-09, 1.0731085212212849e-10, 5.919861919747508e-12, 2.99358055759141e-13, 1.3973597060632118e-14, 6.056766050203782e-16, 2.450248649116191e-17, 9.29288995676233e-19, 3.3171299969525767e-20], [0.024118748833246433, 0.014635763852488569, 0.004440644600323126, 0.0008982255004533977, 0.0001362655293793466, 1.4335274941816451e-05, 1.696351799062686e-06, 1.4705456213148118e-07, 1.1154474987839622e-08, 7.520855476340902e-10, 4.563813217735835e-11, 2.517652552583127e-12, 1.2731370823096303e-13, 5.942818056467274e-15, 2.575876382492509e-16, 1.0420639618860987e-17, 3.95216449938999e-19, 1.410739121501995e-20], [0.008547866823629688, 0.005187025294641966, 0.0015737979991030542, 0.00031833790419842054, 4.829353321099581e-05, 5.8611062502889374e-06, 5.138287108986293e-07, 5.211724793843226e-08, 3.953230216989144e-09, 2.6654480071085366e-10, 1.6174498877550544e-11, 8.922750875860914e-13, 4.5120940157584315e-14, 2.1061796221253864e-15, 9.129100528352434e-17, 3.693153417489001e-18, 1.4006769604605368e-19, 4.999766039630113e-21], [0.0025966530758650074, 0.0015757036771663626, 0.0004780850590540484, 9.670402161813786e-05, 1.4670508343679576e-05, 1.7804745776703412e-06, 1.800715675890975e-07, 1.353122540733038e-08, 1.200903993282905e-09, 8.09704211474561e-11, 4.9134553833786135e-12, 2.710534567868131e-13, 1.3706744672510122e-14, 6.398108331540161e-16, 2.773219032998609e-17, 1.1218984079927488e-18, 4.2549471262453395e-20, 1.5188184529877946e-21], [0.0006902051024636897, 0.0004188309667007519, 0.0001270777179430623, 2.5704476955344967e-05, 3.899504253632602e-06, 4.732602324650469e-07, 4.786404310757898e-08, 4.149272518186696e-09, 2.728173562476213e-10, 2.1522396789948926e-11, 1.3060242848212917e-12, 7.204754483898777e-14, 3.64333040831108e-15, 1.7006534517798008e-16, 7.371373344463547e-18, 2.9820695449835332e-19, 1.1309890583937296e-20, 4.037105517528447e-22], [0.00016307593558962654, 9.895790614243688e-05, 3.0024868944300174e-05, 6.073240567727324e-06, 9.21342514314894e-07, 1.1181800150580866e-07, 1.1308919019881178e-08, 9.803556877576378e-10, 7.436255522968138e-11, 4.3461210519102596e-12, 3.0857658309069e-13, 1.702279617988133e-14, 8.608158833898536e-16, 4.018162887709295e-17, 1.7416469400732467e-18, 7.045786524985955e-20, 2.6722071190264934e-21, 9.538537993923765e-23], [3.467720624804833e-05, 2.104285778750167e-05, 6.3846242499702635e-06, 1.2914414073396327e-06, 1.9591844914747406e-07, 2.3777486766773212e-08, 2.404779809338357e-09, 2.0846727788438576e-10, 1.581279086646295e-11, 1.066170437550146e-12, 5.608111760447399e-14, 3.619804552485941e-15, 1.8304779195027177e-16, 8.544403727720338e-18, 3.703517010884106e-19, 1.4982479887253194e-20, 5.682302362328393e-22, 2.028317961961644e-23], [6.703562132360609e-06, 4.067862434243382e-06, 1.2342322228988885e-06, 2.4965268691135384e-07, 3.787362474766091e-08, 4.59650234659308e-09, 4.6487570974531013e-10, 4.0299479141019795e-11, 3.0568213973501575e-12, 2.0610483211016304e-13, 1.2506874516903042e-14, 5.980618925657965e-16, 3.5385556660843344e-17, 1.651746131537645e-18, 7.159387700707095e-20, 2.896311314776045e-21, 1.0984641227512863e-22, 3.921006607318077e-24], [1.187896535336837e-06, 7.208405913831611e-07, 2.1871061272111787e-07, 4.423939928712162e-08, 6.711349388590064e-09, 8.145175810077566e-10, 8.237773202741174e-11, 7.141219951763006e-12, 5.416803000193966e-13, 3.652255489629179e-14, 2.2162654142939924e-15, 1.2226149518597457e-16, 5.359181678446075e-18, 2.9269565466362768e-19, 1.2686705481177194e-20, 5.132373069939447e-22, 1.946519924547301e-23, 6.948171840432838e-25], [1.943074650764956e-07, 1.1790985483107554e-07, 3.577508939456347e-08, 7.236358787383831e-09, 1.097793661440259e-09, 1.3323285464502057e-10, 1.347474953654817e-11, 1.1681087578787336e-12, 8.860411900165988e-14, 5.974093575416746e-15, 3.6252055779088927e-16, 1.9998645083439533e-17, 1.0112998565093061e-18, 4.0919151232810606e-20, 2.0751988989686043e-21, 8.395162132230862e-23, 3.1839755484464763e-24, 1.1365313535892824e-25], [2.9513157332987433e-08, 1.790920433946923e-08, 5.433840853658283e-09, 1.0991229561145637e-09, 1.667427292949739e-10, 2.023659873033456e-11, 2.046665592277604e-12, 1.7742281563780126e-13, 1.3457986822159678e-14, 9.07398815294368e-16, 5.506286778180556e-17, 3.0375732531005202e-18, 1.5360527586645546e-19, 7.170070055078336e-21, 2.693924293562053e-22, 1.2751323823144196e-23, 4.836107108324002e-25, 1.7262655677767443e-26], [4.183874382065104e-09, 2.5388629347129836e-09, 7.703177022821906e-10, 1.5581499217257427e-10, 2.3637953256634536e-11, 2.868801397719097e-12, 2.901415000628667e-13, 2.515199457535358e-14, 1.9078448864049098e-15, 1.2863559851602093e-16, 7.805878554980574e-18, 4.30615564912417e-19, 2.1775548152870336e-20, 1.016450801335453e-21, 4.4057408257287385e-23, 1.5449616726713014e-24, 6.855811599941621e-26, 2.4472062423458457e-27], [5.560487601152675e-10, 3.3742207772809677e-10, 1.0237740527894002e-10, 2.0708253951488228e-11, 3.141550964426101e-12, 3.8127183432101147e-13, 3.856062745562384e-14, 3.3427713456225054e-15, 2.535579911589219e-16, 1.7096035523469443e-17, 1.0374233774114693e-18, 5.723002869835186e-20, 2.8940320491308297e-21, 1.350891915454153e-22, 5.855354391224549e-24, 2.368768096418681e-25, 7.787401849313524e-27, 3.2524064360916464e-28], [6.955337011547912e-11, 4.220644724122977e-11, 1.2805879756574618e-11, 2.590292353560175e-12, 3.9296096428678896e-13, 4.769139490867613e-14, 4.823356845090588e-15, 4.181306196336151e-16, 3.17163063202551e-17, 2.1384579403157988e-18, 1.2976612360504586e-19, 7.158619267401659e-21, 3.620000558899334e-22, 1.689763418627419e-23, 7.324171194010269e-25, 2.962974040150615e-26, 1.1237468372768998e-27, 3.477039180681272e-29]] |
| Legacy trial inputs | {"lambda_home": 2.1264453349703363, "lambda_away": 0.6068210234982807, "rho": -0.03318338004165527, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7416 |
| Legacy p draw | 0.1649 |
| Legacy p away | 0.0936 |
| Legacy p over 1 5 | 0.7630 |
| Legacy p under 3 5 | 0.7038 |
| Legacy p btts yes | 0.3976 |
| Legacy p over 2 5 | 0.5232 |
| Legacy goal margin distribution | {"-1": 0.07084786985901147, "-10": 1.4155900715153944e-10, "-11": 7.734190181253627e-12, "-12": 3.879194996552777e-13, "-13": 1.7980806838813442e-14, "-14": 7.746309408623007e-16, "-15": 3.1168592509392243e-17, "-16": 1.1735963663945719e-18, "-17": 3.893649394139956e-20, "-2": 0.01871777077628699, "-3": 0.0034379830754088193, "-4": 0.0004911424604577456, "-5": 5.7217820160922085e-05, "-6": 5.618046952516261e-06, "-7": 4.762381899217041e-07, "-8": 3.549664366821611e-08, "-9": 2.3598991279022445e-09, "0": 0.16485747746650564, "1": 0.2519261845498202, "10": 3.8971185304309674e-05, "11": 7.461300960142896e-06, "12": 1.3113992352561029e-06, "13": 2.1300808833316283e-07, "14": 3.215698796533292e-08, "15": 4.534102339549775e-09, "16": 5.982552073564973e-10, "17": 6.955337011547912e-11, "2": 0.22662686920275646, "3": 0.14586618117416217, "4": 0.07302170418750019, "5": 0.02981050925600532, "6": 0.010256922057817764, "7": 0.0030468390547138246, "8": 0.0007958041321973248, "9": 0.0001853983833230904} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7242 |
| Legacy raw p draw | 0.1857 |
| Legacy raw p away | 0.0901 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1264 |
| Legacy lambda away | 0.6068 |
| Legacy model home team | Como |
| Legacy model away team | Venezia |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 88.3% |
| Market home draw odds | 1.09 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:44:41Z |
| Market reference home draw last update utc | 2026-10-31T11:45:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 27.3% |
| Market draw away odds | 3.81 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:44:41Z |
| Market reference draw away last update utc | 2026-10-31T11:45:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.4% |
| Market home away odds | 1.15 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:44:41Z |
| Market reference home away last update utc | 2026-10-31T11:45:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.08 |
| Market reference dc draw away odds | 3.50 |
| Market reference dc home away odds | 1.13 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.45, "price": 1.53, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.53, "price": 2.45, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.93, "price": 1.89, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.89, "price": 1.93, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.56, "price": 2.37, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.37, "price": 1.56, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 87.8% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.6% |
| Market under 3 5 odds | 1.85 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 3 5 odds | 1.85 |
| Market reference under 3 5 opposite odds | 2.04 |
| Market reference under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.6% |
| Market btts yes odds | 1.71 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:44:41Z |
| Market reference btts yes odds | 1.77 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-31T11:45:07Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021565944172805756, "mu": 9.837638593142305, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,565.5304 |
| Elo away rating | 1,354.7810 |
| Elo rating diff | 270.7494 |
| Elo home expectancy | 0.8261 |

</details>


---

## 2026-11-01 — Frosinone vs Torino

The model's most likely 1X2 outcome is **Frosinone win** at **46.5%**. Expected goals are 1.99 for Frosinone and 1.43 for Torino (3.41 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 69.4%; Under 3.5 goals: 51.2%; Double Chance 1X: 70.1%; Double Chance X2: 53.5%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 70.7%; BTTS Yes (both teams score): 69.4%; BTTS No (at least one team does not score): 30.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 46.5% | 2.15 |
| Draw | 23.6% | 4.23 |
| Torino win | 29.9% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.99 |
| Torino expected goals | 1.43 |
| Expected total goals | 3.41 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 87.8% |
| Under 1.5 | 12.2% |
| Over 2.5 | 69.4% |
| Under 2.5 | 30.6% |
| Over 3.5 | 48.8% |
| Under 3.5 | 51.2% |
| Over 4.5 | 29.3% |
| Under 4.5 | 70.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.65% |
| 2 | 2-1 | 8.16% |
| 3 | 2-2 | 7.53% |
| 4 | 1-2 | 7.02% |
| 5 | 3-1 | 5.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 46.5% | 44.8% | 2.18 | +1.4% |
| Draw | 23.6% | 24.3% | 3.96 | -6.4% |
| Torino win | 29.9% | 30.9% | 3.13 | -6.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:00:00+00:00 |
| Fixture id | b7b781db85506536dce5e7ce59a59863 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:45:07Z |
| Market best draw last update utc | 2026-10-31T11:45:07Z |
| Market best away last update utc | 2026-10-31T11:45:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Frosinone |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9866 |
| Dc lambda away | 1.4267 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:44:26.750844+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 69.4% |
| P btts no | 30.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.45 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.18 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.27 |
| Fair Over 3.5 odds | 2.05 |
| Fair Under 3.5 odds | 1.95 |
| Fair Over 4.5 odds | 3.41 |
| Fair Under 4.5 odds | 1.41 |
| Goal margin distribution | {"-1": 0.160855270288943, "-10": 6.824334575631758e-07, "-11": 9.188557833236902e-08, "-12": 1.1380888023145488e-08, "-13": 1.3048297271532945e-09, "-14": 1.392203676766108e-10, "-15": 1.3877545573319916e-11, "-16": 1.2821269973388735e-12, "-17": 9.623523829307422e-14, "-2": 0.0863704001469578, "-3": 0.03540848789882561, "-4": 0.011716709261875858, "-5": 0.0032315874420708077, "-6": 0.0007616356437266914, "-7": 0.00015640760857558948, "-8": 2.842344484698551e-05, "-9": 4.628608984581293e-06, "0": 0.2364552448181993, "1": 0.1879113354503078, "10": 1.561968909793101e-05, "11": 2.928366881732252e-06, "12": 5.050336813351121e-07, "13": 8.062395410705193e-08, "14": 1.1977855976303021e-08, "15": 1.6624746492772054e-09, "16": 2.1386488050121515e-10, "17": 2.235159982262382e-11, "2": 0.139909928369687, "3": 0.07986510048221089, "4": 0.03679775927843364, "5": 0.014131806796502016, "6": 0.004637619344282821, "7": 0.0013260862542784752, "8": 0.00033554955609215993, "9": 7.608455580682786e-05} |
| Raw goal margin distribution | {"-1": 0.1512213340352005, "-10": 4.092668479906453e-07, "-11": 5.198646640094564e-08, "-12": 6.072241366728013e-09, "-13": 6.563327039894235e-10, "-14": 6.600394105524774e-11, "-15": 6.201467223482489e-12, "-16": 5.413036947725929e-13, "-17": 3.8937300580754655e-14, "-2": 0.07879435530704315, "-3": 0.03099509999049696, "-4": 0.009782155361592028, "-5": 0.0025637311725806664, "-6": 0.0005727701834033133, "-7": 0.00011131466114686414, "-8": 1.9121718977765628e-05, "-9": 2.9409473753242934e-06, "0": 0.22216234857686915, "1": 0.21149972215026616, "10": 1.1211588683874208e-05, "11": 1.982973669601037e-06, "12": 3.2250892218805714e-07, "13": 4.853810443212413e-08, "14": 6.796646673285756e-09, "15": 8.891710972470097e-10, "16": 1.0806820430748214e-10, "17": 1.0824026389799923e-11, "2": 0.15276618191896857, "3": 0.0836741325406812, "4": 0.03677043705928007, "5": 0.013418463183662195, "6": 0.004174233659861388, "7": 0.0011295742445989502, "8": 0.0002701813722609763, "9": 5.7860446970421794e-05} |
| Unadjusted home-win probability | 50.4% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 85.7% |
| Raw p under 3 5 | 55.5% |
| Raw p btts yes | 65.8% |
| P home draw | 70.1% |
| P draw away | 53.5% |
| P home away | 76.4% |
| Raw p home draw | 72.6% |
| Raw p draw away | 49.6% |
| Raw p home away | 77.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0628 |
| Totals anchor target over 2 5 | 0.6942 |
| Totals anchor reference over odds | 1.40 |
| Totals anchor reference under odds | 2.98 |
| Totals anchor reference last update utc | 2026-10-31T11:45:07Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6573 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.05, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.38, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.68, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.99, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:55Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.83, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.18 |
| Reference draw odds | 3.96 |
| Reference away odds | 3.13 |
| Market reference 1x2 last update utc | 2026-10-31T11:45:07Z |
| Market reference home last update utc | 2026-10-31T11:45:07Z |
| Market reference draw last update utc | 2026-10-31T11:45:07Z |
| Market reference away last update utc | 2026-10-31T11:45:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.95 |
| Market reference over 2 5 last update utc | 2026-10-31T11:44:45Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:44:45Z |
| Home probability edge | +1.7% |
| Draw probability edge | -0.6% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0554 |
| Raw ev home | 0.0982 |
| Raw edge prob draw | -0.0204 |
| Raw ev draw | -0.1202 |
| Raw edge prob away | -0.0350 |
| Raw ev away | -0.1422 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.04632448201473014, 0.05659645650259991, 0.04231732714041737, 0.019870016797006358, 0.006997445151779631, 0.001971381872592731, 0.00046282921877075135, 9.313737393740713e-05, 1.639967576187418e-05, 2.5668117126319097e-06, 3.6157240041776623e-07, 4.6302436775938593e-08, 5.435304275169506e-09, 5.889545336617954e-10, 5.925909213281521e-11, 5.56499777099472e-12, 4.899438066677719e-13], [0.0705607201416639, 0.10897295805129652, 0.07398874833878064, 0.03474126963176974, 0.012234520545957557, 0.003446816874017224, 0.0008092230040388561, 0.00016284387948992175, 2.867363240491615e-05, 4.487882356292972e-06, 6.321828704348332e-07, 8.095642077580971e-08, 9.503231591773181e-09, 1.0297438831496268e-09, 1.0361018407544523e-10, 9.729991174011148e-12, 8.566308758443107e-13], [0.06470989829354293, 0.0911532121411241, 0.0649426563878159, 0.030371283224309292, 0.010695581726095362, 0.00301325347670585, 0.0007074335885760347, 0.00014236030052312642, 2.5066873492817696e-05, 3.923366864972318e-06, 5.526627325667799e-07, 7.077318734373566e-08, 8.307852340434003e-09, 9.002158946729381e-10, 9.057741063673007e-11, 8.506088604363672e-12, 7.488781850725464e-13], [0.03771350652639396, 0.05312490595166162, 0.037417040900157676, 0.01777199781298406, 0.006233480531848208, 0.0017561510318548123, 0.000412298612164792, 8.296885429371892e-05, 1.4609197696142951e-05, 2.28657324102665e-06, 3.2209677531871156e-07, 4.1247245524538454e-08, 4.841890525619008e-09, 5.246538615298544e-10, 5.278932369351367e-11, 4.957424390307922e-12, 4.3645289306575455e-13], [0.01648482626333711, 0.023221252159524457, 0.016355239152731623, 0.007679570016449487, 0.002735678014354078, 0.0007676253766550746, 0.00018021848446775755, 3.626624183945553e-05, 6.385778148184533e-06, 9.994764764273465e-07, 1.4079065751666618e-07, 1.802944724424808e-08, 2.1164227740283594e-09, 2.2932971638836222e-10, 2.307456690715325e-11, 2.1669233999936412e-12, 1.9077648240649453e-13], [0.0057645023645250095, 0.008120131862021363, 0.005719187649431004, 0.0026854331863244547, 0.0009457048588356144, 0.0002695092547986729, 6.301976516161343e-05, 1.2681773741281562e-05, 2.233013114394211e-06, 3.4950228893017377e-07, 4.923243140043619e-08, 6.304633704371703e-09, 7.400820542679666e-10, 8.019324385096372e-11, 8.068838177112146e-12, 7.577413837104798e-13, 6.671174244485956e-14], [0.0016798017249211197, 0.0023662426773129394, 0.0016665968146329976, 0.000782547219740787, 0.000275582618009603, 7.763956212041314e-05, 1.8438258277650252e-05, 3.6955254865993045e-06, 6.507099909291056e-07, 1.0184652736406008e-07, 1.4346550310649039e-08, 1.8371984087948357e-09, 2.1566321474567286e-10, 2.33686692847716e-11, 2.351295468527266e-12, 2.2080922218614827e-13, 1.9440099586220293e-14], [0.00041957290474092535, 0.0005910288688915083, 0.0004162746449021394, 0.00019546093161619725, 6.88337187770346e-05, 1.9392441452103486e-05, 4.552841157827174e-06, 9.267711924819877e-07, 1.6253125412815403e-07, 2.5438742376527467e-08, 3.583413266904166e-09, 4.5888670164310747e-10, 5.3867334527744335e-11, 5.836915337256294e-12, 5.872954260006407e-13, 5.5152679850103775e-14, 4.855655837730684e-15], [9.169906323371497e-05, 0.00012917133830388423, 9.097821750201834e-05, 4.271864108827959e-05, 1.5043839722311256e-05, 4.23828301322409e-06, 9.950386798271529e-07, 2.0023647135197274e-07, 3.566492076874699e-08, 5.559722325758286e-09, 7.831669682227861e-10, 1.0029122518544216e-10, 1.1772886331021216e-11, 1.2756773913496662e-12, 1.283553818589834e-13, 1.2053802855087458e-14, 1.0612198420681108e-15], [1.781434428079355e-05, 2.509406978227672e-05, 1.7674305837815618e-05, 8.298935155037302e-06, 2.9225613726858255e-06, 8.233697280481391e-07, 1.9330580913317229e-07, 3.889986781155894e-08, 6.849508337201596e-09, 1.0844385718402265e-09, 1.5214556735118782e-10, 1.9483540516029748e-11, 2.2871144249852086e-12, 2.478253914416449e-13, 2.4935554214996067e-14, 2.341687977837382e-15, 2.06162799897174e-16], [3.114707673852926e-06, 4.387514380943379e-06, 3.0902229773576392e-06, 1.451008053104218e-06, 5.109884591500209e-07, 1.4396016883622822e-07, 3.3798105482702636e-08, 6.801357090373345e-09, 1.1975863856523077e-09, 1.8744143519759195e-10, 2.670875646165934e-11, 3.4065544149458293e-12, 3.998852126239375e-13, 4.33304552966971e-14, 4.359799094539798e-15, 4.09426998792365e-16, 3.604605618827351e-17], [4.950762119581177e-07, 6.973861521143126e-07, 4.911844211189358e-07, 2.306346680563256e-07, 8.122053727031501e-08, 2.2882165045083556e-08, 5.372137544143546e-09, 1.0810613569752028e-09, 1.9035382879701797e-10, 2.9793420577034434e-11, 4.196832413410148e-12, 5.436470171070052e-13, 6.356091069022537e-14, 6.887284431470631e-15, 6.929808658265482e-16, 6.507755746617656e-17, 5.729444565064044e-18], [7.213370922809818e-08, 1.0161071912009329e-07, 7.15666666152855e-08, 3.360398597560035e-08, 1.1834013586785804e-08, 3.3339825263328226e-09, 7.827324322651611e-10, 1.575130529365437e-10, 2.7734977777645433e-11, 4.3409678851547174e-12, 6.114878511141141e-13, 7.83062466403744e-14, 9.298293040791111e-15, 1.0034927159718565e-15, 1.0096885907415959e-16, 9.481945393767282e-18, 8.347928628204826e-19], [9.701577652379059e-09, 1.3666069475790535e-08, 9.625313614396284e-09, 4.519546864571226e-09, 1.5916081812522404e-09, 4.4840187364569224e-10, 1.0527310398864127e-10, 2.1184618546302655e-11, 3.73019831471557e-12, 5.83835733320469e-13, 8.224167222998066e-14, 1.053174917216119e-14, 1.236290469494416e-15, 1.3550809383285707e-16, 1.3579742914405835e-17, 1.2752682555442263e-18, 1.122749387071587e-19], [1.211607017598897e-09, 1.7067229963161195e-09, 1.2020825828191889e-09, 5.644354860303328e-10, 1.9877216992641818e-10, 5.5999846239481236e-11, 1.3147308213914876e-11, 2.645696753204029e-12, 4.65855618239232e-13, 7.291385967957615e-14, 1.0270967339881844e-14, 1.3152851692582937e-15, 1.543973838381584e-16, 1.6730073348868394e-17, 1.7027773966137557e-18, 1.5926522706949488e-19, 1.4021750741202484e-20], [1.4122707768248821e-10, 1.9893868034942381e-10, 1.401168925556463e-10, 6.579160823146372e-11, 2.3169239097794878e-11, 6.527442083278515e-12, 1.532473724130287e-12, 3.083871382897085e-13, 5.430096279590538e-14, 8.498969695227127e-15, 1.197202295228034e-15, 1.5331198819034873e-16, 1.799683478599918e-17, 1.95008722643149e-18, 1.9621276688310509e-19, 1.8639062737381778e-20, 1.634400306707247e-21], [1.5432825356913607e-11, 2.1739357359429474e-11, 1.5311508018499834e-11, 7.189488138169979e-12, 2.5318573924806223e-12, 7.132971619301356e-13, 1.6746363188037772e-13, 3.36995208400717e-14, 5.933828620496783e-15, 9.287391424683244e-16, 1.3082628517379126e-16, 1.6753424185284515e-17, 1.9666342516410524e-18, 2.1309904651519224e-19, 2.1441478601657994e-20, 2.0135607268100946e-21, 1.793216872527431e-22]] |
| Legacy trial inputs | {"lambda_home": 1.7484267872890726, "lambda_away": 1.4086440335236907, "rho": -0.03318338004165527, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4507 |
| Legacy p draw | 0.2410 |
| Legacy p away | 0.3083 |
| Legacy p over 1 5 | 0.8265 |
| Legacy p under 3 5 | 0.6122 |
| Legacy p btts yes | 0.6279 |
| Legacy p over 2 5 | 0.6105 |
| Legacy goal margin distribution | {"-1": 0.1680244775114345, "-10": 4.513851791439302e-07, "-11": 5.676090722122066e-08, "-12": 6.560773769828577e-09, "-13": 7.015072592346701e-10, "-14": 6.97379614918989e-11, "-15": 6.421628646839031e-12, "-16": 4.899438066677719e-13, "-2": 0.08970390674013698, "-3": 0.03556869421935142, "-4": 0.011241414566565874, "-5": 0.0029386249761254556, "-6": 0.0006531738619166016, "-7": 0.00012607526348013752, "-8": 2.1483667119785718e-05, "-9": 3.274847285155541e-06, "0": 0.2410366833420707, "1": 0.20783864773920652, "10": 3.888385506522737e-06, "11": 6.069005627148975e-07, "12": 8.707018475233185e-08, "13": 1.1555607029388994e-08, "14": 1.4258572059668208e-09, "15": 1.6296643504191769e-10, "16": 1.5432825356913607e-11, "2": 0.13717148681027194, "3": 0.06750976585882505, "4": 0.026482917988554105, "5": 0.008592810382824813, "6": 0.0023706424214854148, "7": 0.0005679542194295565, "8": 0.00012012628653849525, "9": 2.27282962430322e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4530 |
| Legacy raw p draw | 0.2395 |
| Legacy raw p away | 0.3075 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7484 |
| Legacy lambda away | 1.4086 |
| Legacy model home team | Frosinone |
| Legacy model away team | Torino |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 68.7% |
| Market home draw odds | 1.40 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:44:42Z |
| Market reference home draw last update utc | 2026-10-31T11:45:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.2% |
| Market draw away odds | 1.74 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:44:42Z |
| Market reference draw away last update utc | 2026-10-31T11:45:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:44:42Z |
| Market reference home away last update utc | 2026-10-31T11:45:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.39 |
| Market reference dc draw away odds | 1.70 |
| Market reference dc home away odds | 1.27 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:42Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.05, "price": 1.76, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:42Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.05, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:42Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.67, "price": 2.2, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:44:42Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.2, "price": 1.67, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 87.8% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.7% |
| Market under 3 5 odds | 1.83 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 3 5 odds | 1.83 |
| Market reference under 3 5 opposite odds | 2.03 |
| Market reference under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.2% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:44:42Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 3.15 |
| Market reference btts yes last update utc | 2026-10-31T11:45:07Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021565944172805756, "mu": 9.798603727791674, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.7336 |
| Elo away rating | 1,449.1597 |
| Elo rating diff | 85.5739 |
| Elo home expectancy | 0.6207 |

</details>


---

## 2026-11-01 — Juventus vs Napoli

The model's most likely 1X2 outcome is **Juventus win** at **40.7%**. Expected goals are 1.13 for Juventus and 1.10 for Napoli (2.23 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 47.9%; Under 3.5 goals: 73.2%; Double Chance 1X: 70.0%; Double Chance X2: 59.3%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 87.7%; BTTS Yes (both teams score): 54.2%; BTTS No (at least one team does not score): 45.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 40.7% | 2.46 |
| Draw | 29.3% | 3.41 |
| Napoli win | 30.0% | 3.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.13 |
| Napoli expected goals | 1.10 |
| Expected total goals | 2.23 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.3% |
| Under 4.5 | 87.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.95% |
| 2 | 1-0 | 10.15% |
| 3 | 2-1 | 9.01% |
| 4 | 0-0 | 8.28% |
| 5 | 0-1 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 40.7% | 42.6% | 2.29 | -6.9% |
| Draw | 29.3% | 29.2% | 3.31 | -3.0% |
| Napoli win | 30.0% | 28.2% | 3.42 | +2.7% |
| Over 2.5 | 47.9% | 47.9% | 2.03 | -2.8% |
| Under 2.5 | 52.1% | 52.1% | 1.87 | -2.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T19:45:00+00:00 |
| Fixture id | aeadf1388a1075328536501576b3d550 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:45:07Z |
| Market best draw last update utc | 2026-10-31T11:45:07Z |
| Market best away last update utc | 2026-10-31T11:45:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Juventus |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1306 |
| Dc lambda away | 1.0954 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:44:26.750844+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 54.2% |
| P btts no | 45.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.08 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.83 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.74 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.15 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.16700241934867338, "-10": 2.5090731329773966e-07, "-11": 2.9033311862746642e-08, "-12": 3.0847555851202606e-09, "-13": 3.0121936368462777e-10, "-14": 2.4710603061671433e-11, "-2": 0.08733780716856056, "-3": 0.03314995671091858, "-4": 0.009881066800821032, "-5": 0.002414952950235674, "-6": 0.0004991084345453071, "-7": 8.925149399762353e-05, "-8": 1.405443419723577e-05, "-9": 1.976158134781584e-06, "0": 0.29302241706599935, "1": 0.22138868616189164, "10": 4.4184199904931494e-07, "11": 5.276875726927005e-08, "12": 5.7866559096859734e-09, "13": 5.831985004059444e-10, "14": 4.9379133940320256e-11, "2": 0.11943814801285278, "3": 0.04678971015030249, "4": 0.014394541523868544, "5": 0.003631025406558616, "6": 0.0007745369396306578, "7": 0.0001429517027839419, "8": 2.323345603669966e-05, "9": 3.3716986905079504e-06} |
| Raw goal margin distribution | {"-1": 0.20484221816370016, "-10": 8.277441837949865e-08, "-11": 8.165730754497452e-09, "-12": 7.367471194724869e-10, "-13": 5.667981092369723e-11, "-2": 0.09600963315465559, "-3": 0.03194472500123339, "-4": 0.008256514616299268, "-5": 0.001739057800936679, "-6": 0.00030858794581737486, "-7": 4.726177675389191e-05, "-8": 6.363325232276025e-06, "-9": 7.640878568751487e-07, "0": 0.29607083243013593, "1": 0.21152997679237753, "10": 1.1354349558740502e-07, "11": 1.1560797413269167e-08, "12": 1.0765588950123395e-09, "13": 8.548193652594009e-11, "2": 0.10227465773843254, "3": 0.03512197994725517, "4": 0.00936921495817219, "5": 0.00203679386488347, "6": 0.00037302559436807106, "7": 5.896527525945236e-05, "8": 8.194019985096734e-06, "9": 1.0155067351625111e-06} |
| Unadjusted home-win probability | 36.1% |
| Unadjusted draw probability | 29.6% |
| Unadjusted away-win probability | 34.3% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.4% |
| Raw p btts yes | 45.4% |
| P home draw | 70.0% |
| P draw away | 59.3% |
| P home away | 70.7% |
| Raw p home draw | 65.7% |
| Raw p draw away | 63.9% |
| Raw p home away | 70.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1769 |
| Totals anchor target over 2 5 | 0.4787 |
| Totals anchor reference over odds | 2.03 |
| Totals anchor reference under odds | 1.87 |
| Totals anchor reference last update utc | 2026-10-31T11:45:07Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3854 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.4, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.38, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:22Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.41, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:22Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.61, "price": 2.41, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.29 |
| Reference draw odds | 3.31 |
| Reference away odds | 3.42 |
| Market reference 1x2 last update utc | 2026-10-31T11:45:07Z |
| Market reference home last update utc | 2026-10-31T11:45:07Z |
| Market reference draw last update utc | 2026-10-31T11:45:07Z |
| Market reference away last update utc | 2026-10-31T11:45:07Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:45:07Z |
| Market best over 2 5 last update utc | 2026-10-31T11:45:07Z |
| Market best under 2 5 last update utc | 2026-10-31T11:45:07Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.1% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0654 |
| Raw ev home | -0.1738 |
| Raw edge prob draw | 0.0044 |
| Raw ev draw | -0.0200 |
| Raw edge prob away | 0.0611 |
| Raw ev away | 0.1736 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.1123534609088198, 0.10455097136443296, 0.059022043631706995, 0.02138256436310058, 0.005809872429974462, 0.001262883799319299, 0.0002287593961551287, 3.551793444550075e-05, 4.82530216208905e-06, 5.827050804729629e-07, 6.333089192404062e-08, 6.257339505165481e-09, 5.667287867303542e-10, 4.738039974834771e-11], [0.12954328066750945, 0.13660282442732147, 0.06650315930814131, 0.024092830352149174, 0.0065462808130047, 0.0014229558538817596, 0.0002577549273059413, 4.0019875751241284e-05, 5.436915068507363e-06, 6.565636567612698e-07, 7.13581593519849e-08, 7.050464883150827e-09, 6.385623483933636e-10, 5.338592293092133e-11], [0.07571209023817575, 0.08228715288229939, 0.04047781961918401, 0.013573312922633715, 0.003688014926250441, 0.0008016586178347317, 0.0001452128386137148, 2.2546221791167145e-05, 3.0630253266217013e-06, 3.698919486250575e-07, 4.0201446335309983e-08, 3.972059932780363e-09, 3.5975045059750767e-10, 3.0076326733457566e-11], [0.0284362298606058, 0.030905716465823137, 0.016794830308871033, 0.005507689337197618, 0.0013851584316625194, 0.00030108994025619483, 5.453958072667973e-05, 8.467994257257424e-06, 1.1504225016462904e-06, 1.3892540070682057e-07, 1.5099009486113318e-08, 1.491841116964601e-09, 1.351164189690944e-10, 1.1296179218732523e-11], [0.008010139128454722, 0.008705763385981554, 0.004730898859388358, 0.0017139147195141785, 0.0004215453350196206, 8.481336391823851e-05, 1.536313469717414e-05, 2.385330702139097e-06, 3.240599875533361e-07, 3.91335909715511e-08, 4.25320681674391e-09, 4.20233447366752e-10, 3.8060647272386615e-11, 3.18199591174914e-12], [0.0018050867972786747, 0.0019618458925942514, 0.0010661092065188764, 0.00038623109814241895, 0.00010494313827806086, 2.064900423795893e-05, 3.46208613383134e-06, 5.375348528316257e-07, 7.302699686961186e-08, 8.818764226193692e-09, 9.58461188736079e-10, 9.46997093873155e-11, 8.576976103100407e-12, 7.17063551229622e-13], [0.0003389806233343127, 0.0003684187068234323, 0.00020020664043028048, 7.253105977883939e-05, 1.9707468073993163e-05, 4.2837846194081875e-06, 7.02411231231774e-07, 1.009446746558037e-07, 1.3713876228231158e-08, 1.656092216141762e-09, 1.7999121797872379e-10, 1.7783835417823716e-11, 1.6106863726086095e-12, 1.3465870446373175e-13], [5.456383268946371e-05, 5.9302317876018614e-05, 3.222615359044825e-05, 1.167492280719246e-05, 3.1722019392884387e-06, 6.895370742786242e-07, 1.2490308674762782e-07, 1.7554570230704907e-08, 2.2074466696087263e-09, 2.665719878353161e-10, 2.8972189049514215e-11, 2.8625654492295283e-12, 2.5926326078980733e-13, 2.1675265530716438e-14], [7.684983089650333e-06, 8.352369831642613e-06, 4.53885720961995e-06, 1.644341680630736e-06, 4.467852982236547e-07, 9.711709193297645e-08, 1.759183807639673e-08, 2.731366501551743e-09, 3.3589617786944774e-10, 3.754503886022772e-11, 4.0805561475644514e-12, 4.031748868439405e-13, 3.651564922641538e-14, 3.0528289685083292e-15], [9.621182249964124e-07, 1.0456714274044305e-06, 5.682403189556546e-07, 2.0586266496626016e-07, 5.593509745783893e-08, 1.2158533469410684e-08, 2.2024027674545257e-09, 3.4195228013275863e-10, 4.6456053889837e-11, 5.078259360206921e-12, 5.108635102893298e-13, 5.047531035114756e-14, 4.5715613435278114e-15, 3.821976384508225e-16], [1.0840678779179031e-07, 1.1782115501553174e-07, 6.402654691630498e-08, 2.3195600764482975e-08, 6.30249389595303e-09, 1.369964234574913e-09, 2.481559991698367e-10, 3.8529514673115166e-11, 5.234441511279253e-12, 6.321128832148574e-13, 6.218844708925921e-14, 5.687311720949901e-15, 5.151012293180696e-16, 4.3064165306936367e-17], [1.1104316339821267e-08, 1.2068648130487853e-08, 6.558362678087769e-09, 2.3759701198389803e-09, 6.455766043439118e-10, 1.4032807857178282e-10, 2.541909757255046e-11, 3.946652493493187e-12, 5.361739388051379e-13, 6.474854167965522e-14, 7.03714972250658e-15, 6.293890405252815e-16, 5.276281230991173e-17, 4.411145503148944e-18], [1.0426501596069536e-09, 1.1331969942506034e-09, 6.158035923874414e-10, 2.230939347240661e-10, 6.061701855015138e-11, 1.3176236072770378e-11, 2.3867499204828184e-12, 3.7057462398626936e-13, 5.034455303362371e-14, 6.079624827915939e-15, 6.607597493451465e-16, 6.52856442944098e-17, 5.3524364393618245e-18, 4.141886291922562e-19], [9.036979484592562e-11, 9.821777606503292e-11, 5.337364963375194e-11, 1.9336258597019946e-11, 5.253869171816808e-12, 1.142026153035466e-12, 2.0686718231920667e-13, 3.21188774932614e-14, 4.3635220187118785e-15, 5.269403580641769e-16, 5.727014228173709e-17, 5.658513766011359e-18, 5.124929914161366e-19, 3.878462963305082e-20]] |
| Legacy trial inputs | {"lambda_home": 1.1267512138874063, "lambda_away": 1.086842968189621, "rho": -0.03318338004165527, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T11:45:07Z", "over": 2.03, "under": 1.87, "bookmaker": "pinnacle", "event_id": "aeadf1388a1075328536501576b3d550", "kickoff_utc": "2026-11-01T19:45:00Z", "home_team": "Juventus", "away_team": "Napoli"}} |
| Legacy p home | 0.3934 |
| Legacy p draw | 0.2954 |
| Legacy p away | 0.3113 |
| Legacy p over 1 5 | 0.6536 |
| Legacy p under 3 5 | 0.8164 |
| Legacy p btts yes | 0.4514 |
| Legacy p over 2 5 | 0.3822 |
| Legacy goal margin distribution | {"-1": 0.18610098066710556, "-10": 7.075240343700769e-08, "-11": 6.925978180292302e-09, "-12": 6.201147096612756e-10, "-13": 4.738039974834771e-11, "-2": 0.08711989350449258, "-3": 0.028787503417837895, "-4": 0.007386842178369655, "-5": 0.0015443754810163656, "-6": 0.00027198557217258625, "-7": 4.134026941720145e-05, "-8": 5.523597884013418e-06, "-9": 6.581735981726091e-07, "0": 0.29538470893861923, "1": 0.23044853318264005, "10": 1.211105757732626e-07, "11": 1.2290886983705622e-08, "12": 1.1408679356719864e-09, "13": 9.036979484592562e-11, "2": 0.11175535160576816, "3": 0.038283905073390884, "4": 0.010184325780271664, "5": 0.002207433330228914, "6": 0.00040303410632576084, "7": 6.350829740053405e-05, "8": 8.79711879313561e-06, "9": 1.0867260904939277e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3605 |
| Legacy raw p draw | 0.2991 |
| Legacy raw p away | 0.3405 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1268 |
| Legacy lambda away | 1.0868 |
| Legacy model home team | Juventus |
| Legacy model away team | Napoli |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 71.5% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:45:22Z |
| Market reference home draw last update utc | 2026-10-31T11:45:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.5% |
| Market draw away odds | 1.68 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:45:22Z |
| Market reference draw away last update utc | 2026-10-31T11:45:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.0% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:45:22Z |
| Market reference home away last update utc | 2026-10-31T11:45:22Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.35 |
| Market reference dc draw away odds | 1.68 |
| Market reference dc home away odds | 1.36 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.4, "price": 1.55, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.55, "price": 2.4, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.88, "price": 1.94, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.94, "price": 1.88, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.53, "price": 2.45, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.45, "price": 1.53, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 74.2% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.54 |
| Market reference over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.7% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.47 |
| Market reference under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.0% |
| Market btts yes odds | 1.79 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:45:22Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.08 |
| Market reference btts yes last update utc | 2026-10-31T11:45:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021565944172805756, "mu": 9.111187506624981, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,551.0647 |
| Elo away rating | 1,587.2609 |
| Elo rating diff | 23.8038 |
| Elo home expectancy | 0.5342 |

</details>


---

## 2026-11-01 — Lazio vs Cagliari

The model's most likely 1X2 outcome is **Lazio win** at **64.8%**. Expected goals are 1.76 for Lazio and 0.84 for Cagliari (2.60 combined). The most likely exact score is 1-0 at 12.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 53.6%; Under 3.5 goals: 68.9%; Double Chance 1X: 85.9%; Double Chance X2: 35.2%; Double Chance 12 (either team wins): 78.9%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 64.8% | 1.54 |
| Draw | 21.1% | 4.74 |
| Cagliari win | 14.1% | 7.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.76 |
| Cagliari expected goals | 0.84 |
| Expected total goals | 2.60 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 77.5% |
| Under 1.5 | 22.5% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.1% |
| Under 3.5 | 68.9% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.21% |
| 2 | 2-0 | 11.79% |
| 3 | 2-1 | 10.63% |
| 4 | 1-1 | 10.04% |
| 5 | 3-0 | 7.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 64.8% | 67.4% | 1.46 | -5.3% |
| Draw | 21.1% | 19.9% | 4.71 | -0.7% |
| Cagliari win | 14.1% | 12.7% | 7.28 | +2.4% |
| Over 2.5 | 53.6% | 53.6% | 1.82 | -2.5% |
| Under 2.5 | 46.4% | 46.4% | 2.09 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:00:00+00:00 |
| Fixture id | 3f9f4bc9a19bf36dcb74be2f29610d55 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:45:07Z |
| Market best draw last update utc | 2026-10-31T11:45:07Z |
| Market best away last update utc | 2026-10-31T11:45:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lazio |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7562 |
| Dc lambda away | 0.8405 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:44:26.750844+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.65 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.44 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.22 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.47 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.09433242571260281, "-10": 5.773980812485959e-09, "-11": 4.676478916908903e-10, "-12": 3.478635342722449e-11, "-13": 2.3921767147168e-12, "-14": 1.5291378708819791e-13, "-15": 9.090232146329689e-15, "-16": 4.6335406705556275e-16, "-2": 0.03481784455061028, "-3": 0.009257374967675595, "-4": 0.0019323206544438326, "-5": 0.00033065666586999827, "-6": 4.784195757263973e-05, "-7": 5.988850580249385e-06, "-8": 6.601362287621132e-07, "-9": 6.49708456277914e-08, "0": 0.21081793561647238, "1": 0.26330569671653153, "10": 1.2093023266799822e-05, "11": 2.0465971836571697e-06, "12": 3.181091313617891e-07, "13": 4.571032705871956e-08, "14": 6.105504470468263e-09, "15": 7.584094276466027e-10, "16": 8.077845962349568e-11, "2": 0.2006460986058481, "3": 0.11147321635014194, "4": 0.04862008483982824, "5": 0.01738471750167246, "6": 0.005255973131855492, "7": 0.0013748062946527147, "8": 0.00031665433748499127, "9": 6.512147551139616e-05} |
| Raw goal margin distribution | {"-1": 0.11891776153011009, "-10": 4.127446332449154e-09, "-11": 3.1190696403711977e-10, "-12": 2.164250225923764e-11, "-13": 1.3880339206772671e-12, "-14": 8.274051310054324e-14, "-15": 4.591118722264017e-15, "-16": 2.2079879649516621e-16, "-2": 0.04190979286776007, "-3": 0.010531166119522272, "-4": 0.0020671453772126134, "-5": 0.00033169461455917075, "-6": 4.4924069081242875e-05, "-7": 5.2580403990125225e-06, "-8": 5.414778948301219e-07, "-9": 4.976067057091873e-08, "0": 0.23804974785003358, "1": 0.25155491931338264, "10": 6.549676169541142e-06, "11": 1.0342304109877056e-06, "12": 1.4995244215648376e-07, "13": 2.0095554323916692e-08, "14": 2.5030640341924365e-09, "15": 2.9021918149238874e-10, "16": 2.916474145114814e-11, "2": 0.18298824545353445, "3": 0.09608110327782442, "4": 0.03940817996322197, "5": 0.013213188077871191, "6": 0.0037394017093330682, "7": 0.000914535974516809, "8": 0.00019679381557498644, "9": 3.778946800047633e-05} |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 17.4% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 47.3% |
| P home draw | 85.9% |
| P draw away | 35.2% |
| P home away | 78.9% |
| Raw p home draw | 82.6% |
| Raw p draw away | 41.2% |
| Raw p home away | 76.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0735 |
| Totals anchor target over 2 5 | 0.5360 |
| Totals anchor reference over odds | 1.82 |
| Totals anchor reference under odds | 2.09 |
| Totals anchor reference last update utc | 2026-10-31T11:45:07Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4940 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:03Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 7.7, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:03Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.5, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:03Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.2, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:03Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:03Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:03Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:03Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:34:03Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:22Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.74, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:22Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.16, "price": 5.74, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.46 |
| Reference draw odds | 4.71 |
| Reference away odds | 7.28 |
| Market reference 1x2 last update utc | 2026-10-31T11:45:07Z |
| Market reference home last update utc | 2026-10-31T11:45:07Z |
| Market reference draw last update utc | 2026-10-31T11:45:07Z |
| Market reference away last update utc | 2026-10-31T11:45:07Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:45:07Z |
| Market best over 2 5 last update utc | 2026-10-31T11:45:07Z |
| Market best under 2 5 last update utc | 2026-10-31T11:45:07Z |
| Home probability edge | -2.6% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0862 |
| Raw ev home | -0.1413 |
| Raw edge prob draw | 0.0389 |
| Raw ev draw | 0.1212 |
| Raw edge prob away | 0.0473 |
| Raw ev away | 0.2653 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06852028582874596, 0.04901714801737549, 0.02197945322584351, 0.0061757279403451765, 0.0013014296307078518, 0.0002194033286498319, 3.082368003027295e-05, 3.711752192856288e-06, 3.910943238019348e-07, 3.662954545162975e-08, 3.087621493083231e-09, 2.3660498815681214e-10, 1.662015907733066e-11, 1.077666418710957e-12, 6.488567700043304e-14, 3.646280771976825e-15, 1.9209791478709834e-16], [0.13168437778828546, 0.10282565448346341, 0.03979078194281894, 0.01118030741199289, 0.002356059639760768, 0.0003971995990131851, 5.5802040121621085e-05, 6.719617663557985e-06, 7.080225698780905e-07, 6.631276223089209e-08, 5.58971473452206e-09, 4.2834084149377916e-10, 3.0088515801814135e-11, 1.950967070627875e-12, 1.1746660839136178e-13, 6.601090646305432e-15, 3.477668966749421e-16], [0.12262831925280758, 0.10336733080284367, 0.03796839114981093, 0.010120205669202182, 0.0021326612269809866, 0.00035953766614915927, 5.051096557381821e-05, 6.082472535653557e-06, 6.408888200978483e-07, 6.002507511999683e-08, 5.0597054858127274e-09, 3.8772613781497825e-10, 2.7235563117769528e-11, 1.7659789915450628e-12, 1.0632858224533478e-13, 5.9751840910919865e-15, 3.1479210629891376e-16], [0.07400057774057137, 0.062377452822636306, 0.02628997461533992, 0.006437804747792817, 0.0012869634345730099, 0.00021696452480673875, 3.0481055742033092e-05, 3.670493769074601e-06, 3.867470682440104e-07, 3.622238537448815e-08, 3.0533006684645374e-09, 2.339749772177676e-10, 1.6435415718694996e-11, 1.0656874892220643e-12, 6.416443252613924e-14, 3.6057501035753155e-15, 1.8996262752543298e-16], [0.033491971140750386, 0.028231453233963952, 0.011898597254130389, 0.0033432360103865764, 0.0006140106915917321, 9.819611988529061e-05, 1.3795441473858607e-05, 1.661231238181972e-06, 1.7503811515915614e-07, 1.639391370516791e-08, 1.3818953985839325e-09, 1.0589489195756507e-10, 7.438515829788953e-12, 4.823202159206349e-13, 2.90402235771989e-14, 1.6319288591647382e-15, 8.597531307400564e-17], [0.012126522955810601, 0.010221833892034312, 0.004308155293033743, 0.0012104939436460155, 0.0002550910113383774, 3.7479521709889894e-05, 4.994950491723728e-06, 6.014862087413112e-07, 6.337649440515344e-08, 5.935785924508071e-09, 5.003463726584846e-10, 3.834163217297355e-11, 2.693282297062056e-12, 1.7463490416354345e-13, 1.051466742195708e-14, 5.908766220341256e-16, 3.112929971316027e-17], [0.0036589007750497237, 0.0030842044406531872, 0.0012998872634931685, 0.00036523884420448365, 7.696787467399936e-05, 1.297573645483518e-05, 1.588728383676421e-06, 1.814846979109348e-07, 1.9122406756162337e-08, 1.790987556685002e-09, 1.5096806705307325e-10, 1.1568710023935027e-11, 8.126362948437871e-13, 5.269208564756401e-14, 3.172560256537044e-15, 1.7828349793239707e-16, 9.392553765187971e-18], [0.0009462767755635971, 0.000797646947187455, 0.00033618105652995944, 9.44592534897853e-05, 1.990568117210158e-05, 3.3558270114273844e-06, 4.7145564597278075e-07, 4.9477949138283543e-08, 4.945498803801514e-09, 4.631910058264362e-10, 3.9043850731948214e-11, 2.991937276224915e-12, 2.101666320208634e-13, 1.3627397945389802e-14, 8.20497814619281e-16, 4.6108255984989154e-17, 2.429132692484401e-18], [0.0002141380204452282, 0.0001805037835607555, 7.607620499154123e-05, 2.13756884638634e-05, 4.504562800105628e-06, 7.59407999584145e-07, 1.0668821360030571e-07, 1.2847272304732267e-08, 1.1797495792084165e-09, 1.0481796408522458e-10, 8.835441302380835e-12, 6.770614498548814e-13, 4.755972851366227e-14, 3.0838165906662056e-15, 1.856748282737499e-16, 1.043408325954825e-17, 5.497013977306869e-19], [4.3074164613098795e-05, 3.630859046057085e-05, 1.5302835853867715e-05, 4.299749860843952e-06, 9.060991558545755e-07, 1.5275598940617952e-07, 2.146048452928724e-08, 2.5842469307074167e-09, 2.722930447370451e-10, 2.2226082779304957e-11, 1.7772614704144422e-12, 1.3619186487105859e-13, 9.566706419964145e-15, 6.203140534631821e-16, 3.7348753392525236e-17, 2.0988305531829485e-18, 1.1057321088834105e-19], [7.797986027576085e-06, 6.57317172917181e-06, 2.770368299480898e-06, 7.78410670017663e-07, 1.64036810009399e-07, 2.765437430342431e-08, 3.885126038021969e-09, 4.678424210538175e-10, 4.9294916740414814e-11, 4.616917923339075e-12, 3.3917282038415227e-13, 2.4655667007668103e-14, 1.7319208314980701e-15, 1.122993414977105e-16, 6.761478944938828e-18, 3.7996445142881164e-19, 2.0017761488270365e-20], [1.2833802652295916e-06, 1.0818022560379438e-06, 4.559428537571533e-07, 1.2810960273743137e-07, 2.699691997303012e-08, 4.5513133907626536e-09, 6.394079275718961e-10, 7.699676920353965e-11, 8.112879799612715e-12, 7.598450841082052e-13, 6.40497714121032e-14, 4.277537127486183e-15, 2.850368041471797e-16, 1.8482048847840666e-17, 1.1127935611853374e-18, 6.253395129564006e-20, 3.2944916748080785e-21], [1.936153118352051e-07, 1.6320453634943846e-07, 6.878516072041365e-08, 1.9327070358725425e-08, 4.072851375997442e-09, 6.866273272907245e-10, 9.64633543469579e-11, 1.1616006481897792e-11, 1.2239379043299734e-12, 1.1463293218065734e-13, 9.662776342216444e-15, 7.404602821730705e-16, 4.53303853452978e-17, 2.7882676303955792e-18, 1.6787999488099003e-19, 9.434094327628522e-21, 4.970187326687167e-22], [2.6962610436015457e-08, 2.272764634816607e-08, 9.578929862023435e-09, 2.691462075041433e-09, 5.67179857697809e-10, 9.561880703019905e-11, 1.3433358239879772e-11, 1.6176295904748365e-12, 1.7044396230609341e-13, 1.5963629447633607e-14, 1.3456253628704767e-15, 1.0311551262313122e-16, 7.243280188163676e-18, 4.093179794307054e-19, 2.3378744475690547e-20, 1.3137794101169807e-21, 6.92141666964587e-23], [3.4865788433171295e-09, 2.9389487751550216e-09, 1.2386669413113805e-09, 3.4803732193137923e-10, 7.334294640712241e-11, 1.2364622869356805e-11, 1.7370893202277838e-12, 2.091783034086219e-13, 2.204038493816508e-14, 2.0642827899307384e-15, 1.740049960054413e-16, 1.333403401657943e-17, 9.366402975038373e-19, 6.073261936512355e-20, 3.1868591220093312e-21, 1.6988694425451353e-22, 8.950196044050413e-24], [4.2079814893591694e-10, 3.54704212920111e-10, 1.4949576059379924e-10, 4.200491869273274e-11, 8.85182222245708e-12, 1.4922967899288656e-12, 2.096507789833208e-13, 2.52459063246537e-14, 2.6600726960733586e-15, 2.49140035524536e-16, 2.100081011075858e-17, 1.609295841044837e-18, 1.130439095515821e-19, 7.329871188158614e-21, 4.413273403643123e-22, 2.161416500927577e-23, 1.080206729060168e-24], [4.7612329155222695e-11, 4.013395444110765e-11, 1.691509665311363e-11, 4.752758585070035e-12, 1.0015630400107217e-12, 1.6884990140533101e-13, 2.3721496688719653e-14, 2.8565154214458883e-15, 3.0098102166688294e-16, 2.8189613968441104e-17, 2.376192685372387e-18, 1.8208807117073722e-19, 1.2790654721684182e-20, 8.293578300154048e-22, 4.9935159286607597e-23, 2.8061294814130107e-24, 1.2884174929809363e-25]] |
| Legacy trial inputs | {"lambda_home": 1.8103626843652696, "lambda_away": 0.842931970630243, "rho": -0.03318338004165527, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T11:45:07Z", "over": 1.82, "under": 2.09, "bookmaker": "pinnacle", "event_id": "3f9f4bc9a19bf36dcb74be2f29610d55", "kickoff_utc": "2026-11-01T14:00:00Z", "home_team": "Lazio", "away_team": "Cagliari"}} |
| Legacy p home | 0.6368 |
| Legacy p draw | 0.2164 |
| Legacy p away | 0.1468 |
| Legacy p over 1 5 | 0.7508 |
| Legacy p under 3 5 | 0.7200 |
| Legacy p btts yes | 0.4739 |
| Legacy p over 2 5 | 0.5033 |
| Legacy goal margin distribution | {"-1": 0.10031847667116353, "-10": 3.544293225676755e-09, "-11": 2.6852531044085635e-10, "-12": 1.868114645562052e-11, "-13": 1.2012981738209361e-12, "-14": 7.180155975303739e-14, "-15": 3.994047668651767e-15, "-16": 1.9209791478709834e-16, "-2": 0.035523802911877865, "-3": 0.008923532740447873, "-4": 0.0017529918169732048, "-5": 0.0002816914944174266, "-6": 3.8221829962785515e-05, "-7": 4.4829617802202234e-06, "-8": 4.6270838286580955e-07, "-9": 4.2623914755281456e-08, "0": 0.2164052658317667, "1": 0.2649534705445419, "10": 8.951339765374175e-06, "11": 1.4565207894351088e-06, "12": 2.176246316064153e-07, "13": 3.0055807730349344e-08, "14": 3.858198152890354e-09, "15": 4.609321033770246e-10, "16": 4.7612329155222695e-11, "2": 0.19819529629743077, "3": 0.10692611213750106, "4": 0.04511281283192005, "5": 0.015569218546184233, "6": 0.00453709236331624, "7": 0.001142889502840763, "8": 0.00025334925904083657, "9": 5.0123186023374345e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5992 |
| Legacy raw p draw | 0.2337 |
| Legacy raw p away | 0.1671 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8104 |
| Legacy lambda away | 0.8429 |
| Legacy model home team | Lazio |
| Legacy model away team | Cagliari |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 86.8% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:45:22Z |
| Market reference home draw last update utc | 2026-10-31T11:45:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.5% |
| Market draw away odds | 2.90 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:45:22Z |
| Market reference draw away last update utc | 2026-10-31T11:45:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.7% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:45:22Z |
| Market reference home away last update utc | 2026-10-31T11:45:22Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.12 |
| Market reference dc draw away odds | 2.90 |
| Market reference dc home away odds | 1.22 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.23, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.23, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.07, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.75, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 77.3% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.98 |
| Market reference over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.8% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 3.06 |
| Market reference under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 46.7% |
| Market btts yes odds | 2.05 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:45:22Z |
| Market reference btts yes odds | 2.05 |
| Market reference btts yes opposite odds | 1.81 |
| Market reference btts yes last update utc | 2026-10-31T11:45:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021565944172805756, "mu": 9.342641851211273, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,538.3289 |
| Elo away rating | 1,414.0618 |
| Elo rating diff | 184.2671 |
| Elo home expectancy | 0.7428 |

</details>


---

## 2026-11-01 — Lecce vs Genoa

The model's most likely 1X2 outcome is **Genoa win** at **40.1%**. Expected goals are 0.86 for Lecce and 1.09 for Genoa (1.95 combined). The most likely exact score is 1-1 at 14.7%. Goal-market probabilities: at least one goal: 88.2%; Over 2.5 goals: 38.3%; Under 3.5 goals: 81.0%; Double Chance 1X: 59.9%; Double Chance X2: 71.8%; Double Chance 12 (either team wins): 68.3%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 46.1%; BTTS No (at least one team does not score): 53.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 28.2% | 3.55 |
| Draw | 31.7% | 3.15 |
| Genoa win | 40.1% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.86 |
| Genoa expected goals | 1.09 |
| Expected total goals | 1.95 |
| Over 0.5 | 88.2% |
| Under 0.5 | 11.8% |
| Over 1.5 | 66.0% |
| Under 1.5 | 34.0% |
| Over 2.5 | 38.3% |
| Under 2.5 | 61.7% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.73% |
| 2 | 0-1 | 12.25% |
| 3 | 0-0 | 11.84% |
| 4 | 1-0 | 9.88% |
| 5 | 0-2 | 7.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 28.2% | 28.3% | 3.41 | -4.0% |
| Draw | 31.7% | 31.7% | 3.05 | -3.2% |
| Genoa win | 40.1% | 39.9% | 2.44 | -2.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T17:00:00+00:00 |
| Fixture id | 940b9e69539033539039f9af694e2925 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:45:07Z |
| Market best draw last update utc | 2026-10-31T11:45:07Z |
| Market best away last update utc | 2026-10-31T11:45:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lecce |
| Matched away-team name | Genoa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8554 |
| Dc lambda away | 1.0949 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:44:26.750844+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.1% |
| P btts no | 53.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.45 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.61 |
| Fair Under 2.5 odds | 1.62 |
| Fair Over 3.5 odds | 5.26 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.10 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.21942265493627572, "-10": 3.239669117023335e-07, "-11": 3.693688701996556e-08, "-12": 3.865494682693147e-09, "-13": 3.726030544925014e-10, "-14": 3.0927067493408347e-11, "-2": 0.11841012303029966, "-3": 0.04549053666671138, "-4": 0.013580298841596623, "-5": 0.003304429193747323, "-6": 0.000677453255811374, "-7": 0.00011988355126618929, "-8": 1.8651090506217577e-05, "-9": 2.58791042229701e-06, "0": 0.31731928627623784, "1": 0.1775117135235307, "10": 2.8530507538431555e-08, "11": 2.5413090860046027e-09, "12": 2.0777372929482338e-10, "13": 1.564661231970619e-11, "14": 1.0146143723190773e-12, "2": 0.07514339654590001, "3": 0.022553367996394146, "4": 0.0052600276769855505, "5": 0.0009999159806108556, "6": 0.00016015287884863432, "7": 2.21413130029664e-05, "8": 2.691140412948508e-06, "9": 2.917223643176661e-07} |
| Raw goal margin distribution | {"-1": 0.23755996611936855, "-10": 1.0563725877636081e-07, "-11": 1.0440471460542233e-08, "-12": 9.448339936798638e-10, "-13": 7.422890401954984e-11, "-2": 0.11518859521272776, "-3": 0.03911943197020624, "-4": 0.010242514434312696, "-5": 0.002176412521615474, "-6": 0.0003886323843031413, "-7": 5.980006196831401e-05, "-8": 8.080326187597448e-06, "-9": 9.729733012561096e-07, "0": 0.3169012691547188, "1": 0.18484662357712062, "10": 8.947479013753621e-09, "11": 6.908631565030561e-10, "12": 4.884451353838962e-11, "13": 2.9979313478715164e-12, "2": 0.07030499714487767, "3": 0.018653383094602776, "4": 0.0038155751426960888, "5": 0.000633407204176723, "6": 8.836273024517686e-05, "7": 1.0622338327539312e-05, "8": 1.1213359481409894e-06, "9": 1.0548631765373694e-07} |
| Unadjusted home-win probability | 27.8% |
| Unadjusted draw probability | 31.7% |
| Unadjusted away-win probability | 40.5% |
| Raw p over 1 5 | 58.4% |
| Raw p under 3 5 | 86.6% |
| Raw p btts yes | 38.6% |
| P home draw | 59.9% |
| P draw away | 71.8% |
| P home away | 68.3% |
| Raw p home draw | 59.5% |
| Raw p draw away | 72.2% |
| Raw p home away | 68.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1562 |
| Totals anchor target over 2 5 | 0.3831 |
| Totals anchor reference over odds | 2.45 |
| Totals anchor reference under odds | 1.57 |
| Totals anchor reference last update utc | 2026-10-31T11:45:07Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3097 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.76, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:22Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.32, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:22Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.65, "price": 2.32, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.41 |
| Reference draw odds | 3.05 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-10-31T11:45:07Z |
| Market reference home last update utc | 2026-10-31T11:45:07Z |
| Market reference draw last update utc | 2026-10-31T11:45:07Z |
| Market reference away last update utc | 2026-10-31T11:45:07Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.52 |
| Reference Under 2.5 odds | 1.63 |
| Market reference over 2 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:45:07Z |
| Home probability edge | -0.1% |
| Draw probability edge | -0.0% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.0047 |
| Raw ev home | -0.0508 |
| Raw edge prob draw | -0.0006 |
| Raw ev draw | -0.0335 |
| Raw edge prob away | 0.0053 |
| Raw ev away | -0.0124 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.14946442494592463, 0.152317334388266, 0.08345775707778763, 0.029617212389155236, 0.00788284367221923, 0.0016784624709218054, 0.000297823600999626, 4.529599415231715e-05, 6.027934637954241e-06, 7.130578258644674e-07, 7.591427980035417e-08, 7.347329498098605e-09, 6.518489888107981e-10, 5.338292538160595e-11], [0.12083402456770964, 0.13695376076852583, 0.07163075097557124, 0.025420083638969762, 0.006765746310888774, 0.001440603384109409, 0.000255618278573772, 3.8876986285306144e-05, 5.173701044300419e-06, 6.120086298038566e-07, 6.515627860452391e-08, 6.306121180841606e-09, 5.594738491194302e-10, 4.581789839850658e-11], [0.0537541969281538, 0.057228334056918954, 0.030280851317448704, 0.010908870215767273, 0.002903477796003158, 0.0006182259497192432, 0.00010969698862297434, 1.6683815985420464e-05, 2.2202615077524685e-06, 2.6263968318439456e-07, 2.7961410242941758e-08, 2.706232540527165e-09, 2.4009470998762536e-10, 1.966246509206122e-11], [0.015378852043929034, 0.01637278821890362, 0.008715481275694175, 0.00307437678693469, 0.0008306729146609042, 0.00017687187147744616, 3.138385194279992e-05, 4.773170324000069e-06, 6.352075777858476e-07, 7.51401203882877e-08, 7.999643109551932e-09, 7.742418679021434e-10, 6.869009737723109e-11, 5.625349437810205e-12], [0.0032998691781941846, 0.0035131399307524436, 0.0018700971927319526, 0.0006636538973109613, 0.00017557740690766238, 3.795172978521186e-05, 6.7340920780844355e-06, 1.0241881246693436e-06, 1.3629768344889968e-07, 1.6122956811525664e-08, 1.7164984524436404e-09, 1.6613053230890201e-10, 1.4738963255177546e-11, 1.2070417982680176e-12], [0.0005664473037176823, 0.0006030568285881733, 0.0003210162146769458, 0.00011392117094146324, 3.0320975846347455e-05, 6.41741526489322e-06, 1.1559574318352152e-06, 1.758095761954111e-07, 2.3396520020483106e-08, 2.7676265090130547e-09, 2.9464983843824906e-10, 2.8517552366442072e-11, 2.530053630810334e-12, 2.0719778123980718e-13], [8.102910816619612e-05, 8.626602452394883e-05, 4.5920701557660355e-05, 1.6296186462626797e-05, 4.337352504696218e-06, 9.235351739814166e-07, 1.6288802712045387e-07, 2.514919406040836e-08, 3.3468235068114404e-09, 3.959032133979776e-10, 4.2149046298337606e-11, 4.0793765283544855e-12, 3.619189074989117e-13, 2.963921148125696e-14], [9.935181705014447e-06, 1.0577293123561955e-05, 5.630452121740452e-06, 1.998116198846897e-06, 5.31813643616453e-07, 1.1323695857120825e-07, 2.009257838776774e-08, 3.0375581744877136e-09, 4.1036240466308327e-10, 4.854268363216353e-11, 5.168000032878914e-12, 5.001825636442206e-13, 4.4375782849626335e-14, 3.634137883582018e-15], [1.0659053027653641e-06, 1.1347948295316977e-06, 6.040683453731476e-07, 2.1436977351076873e-07, 5.7056126364316215e-08, 1.214873348004834e-08, 2.1556511481758803e-09, 3.278530024970487e-10, 4.336867474037543e-11, 5.2079474165902364e-12, 5.544537385719813e-13, 5.366255623387954e-14, 4.7608975515674526e-15, 3.8989189690768085e-16], [1.0165035712453303e-07, 1.0822002609960084e-07, 5.760714659688949e-08, 2.0443433368369e-08, 5.441173438229833e-09, 1.158567363961718e-09, 2.0557427426198197e-10, 3.1265793219823675e-11, 4.160812925291513e-12, 4.892407838286665e-13, 5.2875635751744534e-14, 5.11754467421948e-15, 4.54024325701921e-16, 3.7182149725501127e-17], [8.724523247106558e-09, 9.28838973336547e-09, 4.944349473050085e-09, 1.7546343635025238e-09, 4.670091231968505e-10, 9.943839044106464e-11, 1.764418331170679e-11, 2.6835039984305548e-12, 3.5711737883118636e-13, 4.224421083208769e-14, 4.4704801854169895e-15, 4.392324704145924e-16, 3.8968341050542934e-17, 3.191297491066454e-18], [6.807408529188199e-10, 7.247371770635839e-10, 3.857884932026617e-10, 1.3690734259519706e-10, 3.643891818975072e-11, 7.758793552894091e-12, 1.3767074780447986e-12, 2.0938345270711707e-13, 2.7864489803302358e-14, 3.296152614672102e-15, 3.509183165496143e-16, 3.375983574671441e-17, 3.040549147757237e-18, 2.490046177258738e-19], [4.8689281282023275e-11, 5.183607259398078e-11, 2.7593120613186306e-11, 9.792155244701914e-12, 2.6062557135306575e-12, 5.549396368474732e-13, 9.846757008071277e-14, 1.4975933618418797e-14, 1.9929786437759866e-15, 2.357538865430558e-16, 2.5099067505995262e-17, 2.42920198342851e-18, 2.1422460654743082e-19, 1.780979622567701e-20], [3.214569405031185e-12, 3.4223272278843094e-12, 1.8217562259485075e-12, 6.464988151418115e-13, 1.7207051855778034e-13, 3.6638289399183233e-14, 6.501037391284942e-15, 9.887428352597473e-16, 1.3158066836218058e-16, 1.5564970581693665e-17, 1.6570935609471371e-18, 1.6038105654793236e-19, 1.4228874526755855e-20, 1.1582816343300657e-21]] |
| Legacy trial inputs | {"lambda_home": 0.8582875155488194, "lambda_away": 1.0646300629029688, "rho": -0.03318338004165527, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2835 |
| Legacy p draw | 0.3200 |
| Legacy p away | 0.3965 |
| Legacy p over 1 5 | 0.5774 |
| Legacy p under 3 5 | 0.8706 |
| Legacy p btts yes | 0.3813 |
| Legacy p over 2 5 | 0.3032 |
| Legacy goal margin distribution | {"-1": 0.23572676174630022, "-10": 8.246612104062122e-08, "-11": 7.926465812310096e-09, "-12": 6.976668872093047e-10, "-13": 5.338292538160595e-11, "-2": 0.1119651036818181, "-3": 0.03703361648747607, "-4": 0.009438056323239597, "-5": 0.001951416194789576, "-6": 0.0003389977342946308, "-7": 5.0740503213136666e-05, "-8": 6.668693866029977e-06, "-9": 7.80990234148694e-07, "0": 0.31995557461045415, "1": 0.1874727587332889, "10": 9.477500043598472e-09, "11": 7.343986817387492e-10, "12": 5.2111608509907584e-11, "13": 3.214569405031185e-12, "2": 0.0721154562874715, "3": 0.019229848546484025, "4": 0.003950903057088169, "5": 0.000658563692140526, "6": 9.223138793587265e-05, "7": 1.1129375315865402e-05, "8": 1.179209228574613e-06, "9": 1.1133449957686442e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2840 |
| Legacy raw p draw | 0.3224 |
| Legacy raw p away | 0.3936 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.8583 |
| Legacy lambda away | 1.0646 |
| Legacy model home team | Lecce |
| Legacy model away team | Genoa |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 60.2% |
| Market home draw odds | 1.60 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:45:22Z |
| Market reference home draw last update utc | 2026-10-31T11:45:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.4% |
| Market draw away odds | 1.35 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:45:22Z |
| Market reference draw away last update utc | 2026-10-31T11:45:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 68.4% |
| Market home away odds | 1.41 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:45:22Z |
| Market reference home away last update utc | 2026-10-31T11:45:22Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.60 |
| Market reference dc draw away odds | 1.35 |
| Market reference dc home away odds | 1.41 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 2.53, "price": 1.49, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 1.49, "price": 2.53, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.97, "price": 1.86, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.86, "price": 1.97, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.57, "price": 2.35, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:45:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.35, "price": 1.57, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 67.2% |
| Market over 1 5 odds | 1.45 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference over 1 5 odds | 1.45 |
| Market reference over 1 5 opposite odds | 2.84 |
| Market reference over 1 5 last update utc | 2026-10-31T11:45:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 81.9% |
| Market reference under 3 5 odds | 1.18 |
| Market reference under 3 5 opposite odds | 4.10 |
| Market reference under 3 5 last update utc | 2026-10-31T11:45:07Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 47.8% |
| Market btts yes odds | 2.01 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:45:22Z |
| Market reference btts yes odds | 2.01 |
| Market reference btts yes opposite odds | 1.85 |
| Market reference btts yes last update utc | 2026-10-31T11:45:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021565944172805756, "mu": 8.985279315822341, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,357.9326 |
| Elo away rating | 1,431.0354 |
| Elo rating diff | -13.1028 |
| Elo home expectancy | 0.4812 |

</details>


---

## 2026-11-02 — Atalanta BC vs Parma

The model's most likely 1X2 outcome is **Atalanta BC win** at **64.3%**. Expected goals are 1.82 for Atalanta BC and 0.71 for Parma (2.53 combined). The most likely exact score is 1-0 at 14.4%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 47.0%; Under 3.5 goals: 75.0%; Double Chance 1X: 85.3%; Double Chance X2: 35.7%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 88.5%; BTTS Yes (both teams score): 42.6%; BTTS No (at least one team does not score): 57.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 64.3% | 1.55 |
| Draw | 20.9% | 4.78 |
| Parma win | 14.7% | 6.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 1.82 |
| Parma expected goals | 0.71 |
| Expected total goals | 2.53 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 72.3% |
| Under 1.5 | 27.7% |
| Over 2.5 | 47.0% |
| Under 2.5 | 53.0% |
| Over 3.5 | 25.0% |
| Under 3.5 | 75.0% |
| Over 4.5 | 11.5% |
| Under 4.5 | 88.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.37% |
| 2 | 2-0 | 13.31% |
| 3 | 1-1 | 9.77% |
| 4 | 2-1 | 9.50% |
| 5 | 3-0 | 8.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 64.3% | 64.7% | 1.52 | -2.2% |
| Draw | 20.9% | 20.2% | 4.65 | -2.6% |
| Parma win | 14.7% | 15.1% | 6.14 | -9.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T19:45:00+00:00 |
| Fixture id | 2e488800d615a94e5377c195810303c0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:45:07Z |
| Market best draw last update utc | 2026-10-31T11:45:07Z |
| Market best away last update utc | 2026-10-31T11:45:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Atalanta |
| Matched away-team name | Parma |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8191 |
| Dc lambda away | 0.7135 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:44:26.750844+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 42.6% |
| P btts no | 57.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.18 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.61 |
| Fair Over 2.5 odds | 2.13 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 3.99 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.71 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.10635942367547065, "-10": 8.983789510334336e-10, "-11": 5.7711846421658845e-11, "-12": 3.4034819732641008e-12, "-13": 1.8549186136817202e-13, "-14": 9.395344758813416e-15, "-15": 4.4326837456795893e-16, "-16": 1.828455462098708e-17, "-2": 0.03255810235931554, "-3": 0.007028116792468994, "-4": 0.0011801892939434441, "-5": 0.0001616323341623894, "-6": 1.8657854187799148e-05, "-7": 1.85950468660744e-06, "-8": 1.6295547300027623e-07, "-9": 1.2737733987372829e-08, "0": 0.20936193199006134, "1": 0.26156999954105753, "10": 9.892770052847349e-06, "11": 1.6201893916884077e-06, "12": 2.435940847948293e-07, "13": 3.3846254141851885e-08, "14": 4.370598790748442e-09, "15": 5.256993449652049e-10, "16": 5.528375621972752e-11, "2": 0.20089895767830368, "3": 0.11056051108868956, "4": 0.047332038243980086, "5": 0.016526247374302434, "6": 0.004863513969746296, "7": 0.0012357431695775652, "8": 0.0002760847135396091, "9": 5.5018412244501665e-05} |
| Raw goal margin distribution | {"-1": 0.09971838896069674, "-10": 8.422845722312367e-10, "-11": 5.410834461339991e-11, "-12": 3.1909700852294257e-12, "-13": 1.7390983273277092e-13, "-14": 8.808703645648574e-15, "-15": 4.1559089605463623e-16, "-16": 1.714287523061483e-17, "-2": 0.030525189049488692, "-3": 0.006589284331880584, "-4": 0.0011064988037147868, "-5": 0.00015154008370532035, "-6": 1.7492866139890605e-05, "-7": 1.7433980479166848e-06, "-8": 1.5278060634756398e-07, "-9": 1.1942395589754116e-08, "0": 0.22655970332012024, "1": 0.2583173324599648, "10": 9.769751787953919e-06, "11": 1.600042063215238e-06, "12": 2.405649512468259e-07, "13": 3.342537026044859e-08, "14": 4.316249657299367e-09, "15": 5.191621849051043e-10, "16": 5.459629338266452e-11, "2": 0.19840074524028475, "3": 0.10918567247754171, "4": 0.04674345636170253, "5": 0.016320740699596988, "6": 0.004803035352872862, "7": 0.0012203764947470318, "8": 0.00027265155354076054, "9": 5.4334249004544216e-05} |
| Unadjusted home-win probability | 63.5% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 13.8% |
| Raw p over 1 5 | 72.2% |
| Raw p under 3 5 | 75.1% |
| Raw p btts yes | 43.0% |
| P home draw | 85.3% |
| P draw away | 35.7% |
| P home away | 79.1% |
| Raw p home draw | 86.2% |
| Raw p draw away | 36.5% |
| Raw p home away | 77.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4704 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.15, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.79, "price": 2.15, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.52 |
| Reference draw odds | 4.65 |
| Reference away odds | 6.14 |
| Market reference 1x2 last update utc | 2026-10-31T11:45:07Z |
| Market reference home last update utc | 2026-10-31T11:45:07Z |
| Market reference draw last update utc | 2026-10-31T11:45:07Z |
| Market reference away last update utc | 2026-10-31T11:45:07Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-10-31T11:45:07Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:45:07Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -12.4% |
| Under 2.5 probability edge | +12.4% |
| Raw edge prob home | -0.0114 |
| Raw ev home | -0.0343 |
| Raw edge prob draw | 0.0246 |
| Raw ev draw | 0.0535 |
| Raw edge prob away | -0.0131 |
| Raw ev away | -0.1520 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.074039781287717, 0.053828996968724833, 0.0210302883685714, 0.005138439430776657, 0.0009416261674953649, 0.00013804344315145416, 1.6864435214061502e-05, 1.76596068142262e-06, 1.6180737467057652e-07, 1.3178411689308717e-08, 9.659849033817897e-10, 6.437020950770306e-11, 3.931976786348335e-12, 2.217046803284945e-13, 1.1607911660778346e-14, 5.672442521126247e-16, 2.598707440003108e-17], [0.1361407310022723, 0.10005992792407503, 0.03923082417729169, 0.009585470742080729, 0.0017565508361242258, 0.0002575123056893462, 3.145965861889494e-05, 3.2943006668627658e-06, 3.0184258793983247e-07, 2.4583588339752086e-08, 1.8019906925823777e-09, 1.2007901780491248e-10, 7.334882302657773e-12, 4.1357765432489237e-13, 2.165390856504285e-14, 1.0581623575578856e-15, 4.847743068484952e-17], [0.13014709762330473, 0.09539854611239787, 0.033106422701225505, 0.008940579195792732, 0.001638373563946174, 0.00024018738618642135, 2.934311489993433e-05, 3.0726666221554798e-06, 2.8153521457135096e-07, 2.2929653053284466e-08, 1.6807563165767846e-09, 1.120003385670742e-10, 6.8414059030861185e-12, 3.857529662960761e-13, 2.0197076349553965e-14, 9.869712833424606e-16, 4.521596486062278e-17], [0.08092737190224782, 0.059320213521145165, 0.021741023151256655, 0.005029898474934881, 0.0010187646835432863, 0.00014935203537460012, 1.8245978709033907e-05, 1.9106291189260712e-06, 1.750627207925924e-07, 1.4257994178276519e-08, 1.0451189000184466e-09, 6.964345127871882e-11, 4.254086414249345e-12, 2.398668455611245e-13, 1.2558837952800934e-14, 6.137132026952839e-16, 2.811594934514586e-17], [0.03774136905050732, 0.027664633337663704, 0.010139165019201745, 0.002477354775965763, 0.0004298616579407365, 6.965196265517975e-05, 8.509212642876156e-06, 8.91042882044111e-07, 8.164242328788184e-08, 6.649372240239182e-09, 4.874026819368499e-10, 3.247898868921686e-11, 1.9839399397137026e-12, 1.1186453888850419e-13, 5.856952065547213e-15, 2.862118950565867e-16, 1.3112181892206554e-17], [0.014080881702444398, 0.010321364570740338, 0.0037828088060579516, 0.0009242732951387372, 0.00016937436596158446, 2.351138285763687e-05, 3.174691846629576e-06, 3.3243811047441564e-07, 3.045987289647891e-08, 2.480806241687384e-09, 1.8184447672320625e-10, 1.2117546582262753e-11, 7.401857510382974e-13, 4.1735405429505614e-14, 2.1851631577405403e-15, 1.0678244953782499e-16, 4.892008073104392e-18], [0.004377849260778387, 0.0032089878468615912, 0.0011761029660800227, 0.0002873633375655655, 5.265973100896155e-05, 7.719975118408374e-06, 8.93028143258589e-07, 1.0335744358553467e-07, 9.470197595659431e-09, 7.713008319230574e-10, 5.65367797856808e-11, 3.7674339908982794e-12, 2.301291717023074e-13, 1.2975843251074917e-14, 6.793832316007532e-16, 3.319944572022928e-17, 1.520961142855431e-18], [0.001166661773141509, 0.0008551695657843285, 0.0003134220230232284, 7.658002844997357e-05, 1.403339665037863e-05, 2.0573115527164723e-06, 2.513368009653397e-07, 2.4920602528526507e-08, 2.5237318283060396e-09, 2.0554549565210044e-10, 1.5066599104589942e-11, 1.0039909915110885e-12, 6.13275815399053e-14, 3.4579583246348945e-15, 1.8105019118018146e-16, 8.847386445734151e-18, 4.053239657428393e-19], [0.00027204276811582627, 0.0001994088614542784, 7.308390203109816e-05, 1.7856968833239227e-05, 3.272314357704858e-06, 4.797249233345477e-07, 5.8606839306882904e-08, 6.137019862492236e-09, 5.324367665260475e-10, 4.792920013172878e-11, 3.5132370159581146e-12, 2.341111149622803e-13, 1.4300395734266724e-14, 8.063284289582522e-16, 4.2217372944285196e-17, 2.0630379384137255e-18, 9.451364239650272e-20], [5.6386726175403784e-05, 4.133178376932306e-05, 1.5148213643756952e-05, 3.7012416058561753e-06, 6.78257668548594e-07, 9.94333283657249e-08, 1.2147530415497368e-08, 1.2720296184165771e-09, 1.165505977706108e-10, 8.988195110852139e-12, 7.281940813209888e-13, 4.8524573637539784e-14, 2.9640651874439595e-15, 1.6712894316585756e-16, 8.750460321153534e-18, 4.276090709137172e-19, 1.9589989142378515e-20], [1.0518627713285247e-05, 7.710212592288377e-06, 2.8258143475882785e-06, 6.90445875644852e-07, 1.2652516634767e-07, 1.8548730070236544e-08, 2.266053710565704e-09, 2.372899954286174e-10, 2.174186073325669e-11, 1.7707671990711448e-12, 1.2290285289850111e-13, 9.0519872257067e-15, 5.529297467571727e-16, 3.1176967568713e-17, 1.6323493254736624e-18, 7.97680753759947e-20, 3.6544026701423245e-21], [1.7838100378852996e-06, 1.3075426748854908e-06, 4.792180249959546e-07, 1.1708982551366704e-07, 2.1456873265988983e-08, 3.1456014787482925e-09, 3.842905619892734e-10, 4.0241016915230564e-11, 3.687111139916412e-12, 3.002969960113357e-13, 2.201193675814421e-14, 1.3888842935713124e-15, 9.376904092394835e-17, 5.287171408267765e-18, 2.768232883114165e-19, 1.3527533955667423e-20, 6.197348497505421e-22], [2.7729980340540654e-07, 2.0326229754809814e-07, 7.449619707109762e-08, 1.8202042205236768e-08, 3.3355495327334038e-09, 4.889952703050914e-10, 5.973937528488715e-11, 6.25561345795308e-12, 5.731749303557e-13, 4.6682267836039614e-14, 3.4218361854504347e-15, 2.28020449788984e-16, 1.318842844548102e-17, 8.219101591229026e-19, 4.303319400410835e-20, 2.1029046965749508e-21, 9.63400521072495e-23], [3.9791326172912585e-08, 2.9167263305150574e-08, 1.0689883079231297e-08, 2.6119145758744376e-09, 4.786369762724228e-10, 7.016871291926087e-11, 8.572342778951392e-12, 8.976535592892502e-13, 8.224813118448621e-14, 6.698704157533859e-15, 4.910187389006946e-16, 3.2719951403581845e-17, 1.9986588571524475e-18, 1.0670771388015147e-19, 6.175077796129139e-21, 3.0175775699930473e-22, 1.3824382094171426e-23], [5.302034901526984e-09, 3.886421059552642e-09, 1.4243841216307586e-09, 3.480271600125878e-10, 6.377646078770976e-11, 9.349700064694195e-12, 1.142230354533727e-12, 1.1960874287400406e-13, 1.0959234186629679e-14, 8.925755096452654e-16, 6.542628108553663e-17, 4.359802524906887e-18, 2.663132907613935e-19, 1.501608636156722e-20, 7.444391714889539e-22, 4.0208012984144857e-23, 1.8420435658974802e-24], [6.593765948688181e-10, 4.833267098517689e-10, 1.771405826913005e-10, 4.3281677309380784e-11, 7.931427523208797e-12, 1.162756093877714e-12, 1.4205111352838167e-13, 1.4874893707336226e-14, 1.3629224730807898e-15, 1.110033055504208e-16, 8.136604009280819e-18, 5.421978158509766e-19, 3.311950111455964e-20, 1.867444495790613e-21, 9.777479982121132e-23, 4.524141417689879e-24, 2.2908193488724324e-25], [7.687687992719698e-11, 5.6351180384669035e-11, 2.0652864253548603e-11, 5.046221439241296e-12, 9.247270923747231e-13, 1.3556601994864163e-13, 1.656177438390671e-14, 1.73426752840114e-15, 1.5890346750017036e-16, 1.2941902789284475e-17, 9.48648669522576e-19, 6.321497716226438e-20, 3.861410808703659e-21, 2.1772581464187634e-22, 1.1399588041574941e-23, 5.5706409404235665e-25, 2.416493767540333e-26]] |
| Legacy trial inputs | {"lambda_home": 1.8654439487344345, "lambda_away": 0.7330055595132641, "rho": -0.03318338004165527, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6432 |
| Legacy p draw | 0.2127 |
| Legacy p away | 0.1441 |
| Legacy p over 1 5 | 0.7360 |
| Legacy p under 3 5 | 0.7359 |
| Legacy p btts yes | 0.4399 |
| Legacy p over 2 5 | 0.4848 |
| Legacy goal margin distribution | {"-1": 0.10309209760969631, "-10": 1.0931511591908255e-09, "-11": 7.210369471851285e-11, "-12": 4.36637834240737e-12, "-13": 2.4437367612622493e-13, "-14": 1.2711289983196854e-14, "-15": 6.157216827974742e-16, "-16": 2.598707440003108e-17, "-2": 0.03241233604003167, "-3": 0.007154345921155817, "-4": 0.0012304763979883412, "-5": 0.00017275766615959087, "-6": 2.045502884353219e-05, "-7": 2.0918112736491713e-06, "-8": 1.8814338914185438e-07, "-9": 1.5096770890179233e-08, "0": 0.21269032191904583, "1": 0.25593500697513705, "10": 1.1903343455596365e-05, "11": 1.9981183126661845e-06, "12": 3.079356572365896e-07, "13": 4.385993403659577e-08, "14": 5.806014475632302e-09, "15": 7.157277752534872e-10, "16": 7.687687992719698e-11, "2": 0.20058552640226657, "3": 0.11267670289366344, "4": 0.04931879067033838, "5": 0.017621845738190398, "6": 0.005309933701615596, "7": 0.0013819312486770528, "8": 0.00031632086293376105, "9": 6.459484696535508e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6397 |
| Legacy raw p draw | 0.2234 |
| Legacy raw p away | 0.1369 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8654 |
| Legacy lambda away | 0.7330 |
| Legacy model home team | Atalanta |
| Legacy model away team | Parma |
| Legacy home name match score | 95/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021565944172805756, "mu": 9.571684489886431, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,508.6715 |
| Elo away rating | 1,398.3138 |
| Elo rating diff | 170.3577 |
| Elo home expectancy | 0.7272 |

</details>


---

## 2026-11-02 — Sassuolo vs Fiorentina

The model's most likely 1X2 outcome is **Fiorentina win** at **41.6%**. Expected goals are 1.41 for Sassuolo and 1.62 for Fiorentina (3.02 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 58.1%; Under 3.5 goals: 64.2%; Double Chance 1X: 58.4%; Double Chance X2: 66.6%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 81.2%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 33.4% | 3.00 |
| Draw | 25.0% | 4.00 |
| Fiorentina win | 41.6% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.41 |
| Fiorentina expected goals | 1.62 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 80.7% |
| Under 1.5 | 19.3% |
| Over 2.5 | 58.1% |
| Under 2.5 | 41.9% |
| Over 3.5 | 35.8% |
| Under 3.5 | 64.2% |
| Over 4.5 | 18.8% |
| Under 4.5 | 81.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.53% |
| 2 | 1-2 | 8.80% |
| 3 | 2-1 | 7.84% |
| 4 | 0-1 | 7.46% |
| 5 | 1-0 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 33.4% | 33.5% | 2.90 | -3.3% |
| Draw | 25.0% | 25.2% | 3.82 | -4.4% |
| Fiorentina win | 41.6% | 41.3% | 2.36 | -1.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T17:30:00+00:00 |
| Fixture id | 66608b64d462d1d3deabe573c8456d86 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:45:07Z |
| Market best draw last update utc | 2026-10-31T11:45:07Z |
| Market best away last update utc | 2026-10-31T11:45:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sassuolo |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4078 |
| Dc lambda away | 1.6160 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:44:26.750844+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.12 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.18 |
| Fair Over 2.5 odds | 1.72 |
| Fair Under 2.5 odds | 2.38 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.32 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.20313021361296857, "-10": 1.9680009880389773e-06, "-11": 2.842895852993513e-07, "-12": 3.77402191554337e-08, "-13": 4.631852162865396e-09, "-14": 5.241147992407513e-10, "-15": 4.9029067558927254e-11, "-2": 0.12569857716925018, "-3": 0.05780295384382515, "-4": 0.021112516674759572, "-5": 0.006364866371467244, "-6": 0.0016293750133260193, "-7": 0.00036189413986565733, "-8": 7.0916693733438e-05, "-9": 1.2425768891224987e-05, "0": 0.2502349305155062, "1": 0.18046236254838494, "10": 5.062277823922051e-07, "11": 6.37049666533099e-08, "12": 7.3673014313653505e-09, "13": 7.87681036007379e-10, "14": 7.764505500772493e-11, "15": 6.327507836749065e-12, "2": 0.09748046573587159, "3": 0.03905071093114764, "4": 0.012425406247216208, "5": 0.003263259118546285, "6": 0.0007277379128539558, "7": 0.00014080795082548503, "8": 2.403730566885789e-05, "9": 3.669038399341239e-06} |
| Raw goal margin distribution | {"-1": 0.20619669601742802, "-10": 1.9977102090083344e-06, "-11": 2.8858126104559237e-07, "-12": 3.830995083602498e-08, "-13": 4.70177525753878e-09, "-14": 5.320269103009543e-10, "-15": 4.976921728999073e-11, "-2": 0.12759614064983368, "-3": 0.05867555540188582, "-4": 0.021431234209416245, "-5": 0.0064609512934869105, "-6": 0.001653972288737495, "-7": 0.00036735734493218407, "-8": 7.198726216167967e-05, "-9": 1.2613350054012625e-05, "0": 0.24616966139476476, "1": 0.17926270251806664, "10": 5.028625308893618e-07, "11": 6.32814750113547e-08, "12": 7.31832580601219e-09, "13": 7.824447671134461e-10, "14": 7.712889381084565e-11, "15": 6.285444449480496e-12, "2": 0.096832444637019, "3": 0.0387911134372544, "4": 0.012342805847749218, "5": 0.0032415659439817435, "6": 0.0007229001279869641, "7": 0.00013987190151209392, "8": 2.3877512820973944e-05, "9": 3.6446477249909986e-06} |
| Unadjusted home-win probability | 33.1% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 42.2% |
| Raw p over 1 5 | 80.7% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 60.8% |
| P home draw | 58.4% |
| P draw away | 66.6% |
| P home away | 75.0% |
| Raw p home draw | 57.8% |
| Raw p draw away | 66.9% |
| Raw p home away | 75.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5807 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.17, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:44:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.8, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:45:07Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.90 |
| Reference draw odds | 3.82 |
| Reference away odds | 2.36 |
| Market reference 1x2 last update utc | 2026-10-31T11:45:07Z |
| Market reference home last update utc | 2026-10-31T11:45:07Z |
| Market reference draw last update utc | 2026-10-31T11:45:07Z |
| Market reference away last update utc | 2026-10-31T11:45:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-31T11:44:45Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:44:45Z |
| Home probability edge | -0.1% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.0032 |
| Raw ev home | -0.0391 |
| Raw edge prob draw | -0.0058 |
| Raw ev draw | -0.0596 |
| Raw edge prob away | 0.0090 |
| Raw ev away | -0.0030 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.05197748875304412, 0.07346362421165943, 0.06377454550685707, 0.03521125771332215, 0.014580652749857866, 0.004830169631379058, 0.0013334187357812188, 0.0003155178496746108, 6.532649642825418e-05, 1.2022707403412506e-05, 1.9913963106859316e-06, 2.998613096450782e-07, 4.138992198318335e-08, 5.273593809500268e-09, 6.239274033659077e-10, 6.889666847397214e-11], [0.06411853403143582, 0.11456612589324286, 0.0883980188207505, 0.048806391285217056, 0.02021027050772443, 0.006695107312621375, 0.001848254245714003, 0.00043733989152176854, 9.054918094457608e-05, 1.6664697598024653e-05, 2.7602782137061355e-06, 4.156383316094421e-07, 5.737064958095925e-08, 7.3097384092698e-09, 8.648269604616987e-10, 9.549780320730565e-11], [0.04702190959809992, 0.07788533327234191, 0.06364574941057277, 0.033825315892997185, 0.014006747194475824, 0.0046400504897711435, 0.0012809343626023295, 0.00030309882771057566, 6.275519596201233e-05, 1.1549484517721159e-05, 1.9130134409148174e-06, 2.880585409760882e-07, 3.9760783249102346e-08, 5.066021155791055e-09, 5.99369147361198e-10, 6.618484332712385e-11], [0.02172571944185025, 0.035985669526664224, 0.029802658888888, 0.016235941391586996, 0.006471592975296805, 0.002143860936282801, 0.0005918351854099948, 0.00014004195385250288, 2.8995032159308693e-05, 5.3362541520462274e-06, 8.838771896129739e-07, 1.3309283050316833e-07, 1.837083242772264e-08, 2.3406738530593795e-09, 2.7692890503529386e-10, 3.057964573786708e-11], [0.007528515259699221, 0.01246995124313878, 0.010327380541994873, 0.005701962356260639, 0.0023297433035698147, 0.0007429024303051374, 0.00020508596902909303, 4.8528104645673956e-05, 1.0047517305518274e-05, 1.8491480073118335e-06, 3.062859633952187e-07, 4.6120056372887194e-08, 6.365961441952073e-09, 8.111031198714481e-10, 9.596292049109011e-11, 1.0596626279277874e-11], [0.0020870578640114143, 0.003456924626977707, 0.0028629603622095834, 0.0015807001733308913, 0.0006545531692342193, 0.0002139531294771834, 5.685401034541709e-05, 1.3452979629129296e-05, 2.785376569338384e-06, 5.12621513971054e-07, 8.490871127833008e-08, 1.2785419570967242e-08, 1.7647742524400916e-09, 2.2485431542042594e-10, 2.6602877321182884e-11, 2.93760076791562e-12], [0.0004821458124517702, 0.0007986083000378103, 0.0006613924671938109, 0.0003651685861016016, 0.00015121289879655572, 5.0092678576892804e-05, 1.3644785798378529e-05, 3.107866775057553e-06, 6.434692933843999e-07, 1.184242759128784e-07, 1.9615354365325516e-08, 2.9536490640141888e-09, 4.076928246259875e-10, 5.1945165709634085e-11, 6.145716475212375e-12, 6.786356685786047e-13], [9.547188966274745e-05, 0.0001581360690809505, 0.00013096533666984042, 7.23086959592354e-05, 2.9942355230831915e-05, 9.919079578199134e-06, 2.7382654359282543e-06, 6.393243152003642e-07, 1.2741628734047494e-07, 2.344973058223141e-08, 3.884125713213323e-09, 5.848655121737635e-10, 8.07291142301058e-11, 1.028589899790824e-11, 1.2169413278450857e-12, 1.3437974156049006e-13], [1.654172098010627e-05, 2.739908826428707e-05, 2.2691412780357834e-05, 1.2528402624251448e-05, 5.187894441654791e-06, 1.7186068835721678e-06, 4.744393660856628e-07, 1.1226337576592662e-07, 2.2934634743742073e-08, 4.0629645199249975e-09, 6.729742547947186e-10, 1.0133539984848907e-10, 1.398734734677197e-11, 1.7821630204868871e-12, 2.1085058613046562e-13, 2.328300191946204e-14], [2.54761232349497e-06, 4.219769817092858e-06, 3.494734490218652e-06, 1.9295158561575895e-06, 7.989944836118188e-07, 2.646849188846378e-07, 7.306903418601919e-08, 1.7289830962714242e-08, 3.579778709178235e-09, 6.500659055708093e-10, 1.0364565494556264e-10, 1.560679894013316e-11, 2.154209862232364e-12, 2.7447328357972604e-13, 3.2473377606122624e-14, 3.585845915870203e-15], [3.5312502869357154e-07, 5.84903096911136e-07, 4.844058123576243e-07, 2.674505597993098e-07, 1.1074877733530714e-07, 3.6688026947392785e-08, 1.0128112725625434e-08, 2.3965467581188374e-09, 4.961938077222905e-10, 9.131965269531985e-11, 1.492478105315066e-11, 2.1632613693706706e-12, 2.985954387162001e-13, 3.8044794039441666e-14, 4.5011410461415435e-15, 4.970347843957947e-16], [4.4497024898688e-08, 7.370320864216992e-08, 6.103961980064198e-08, 3.370124814597878e-08, 1.3955371899919162e-08, 4.623031266295488e-09, 1.2762360283443654e-09, 3.019870926776515e-10, 6.252501641834345e-11, 1.15071222075547e-11, 1.9059967062187974e-12, 2.8318691231330246e-13, 3.762579140975883e-14, 4.793996488726688e-15, 5.671854695308742e-16, 6.263098726985341e-17], [5.1397842367985456e-09, 8.513346473005855e-09, 7.050594424814372e-09, 3.892780346001183e-09, 1.6119639610328369e-09, 5.33999369234975e-10, 1.4741609884826615e-10, 3.488207362616236e-11, 7.22217034788875e-12, 1.3291703314539574e-12, 2.2015880496096199e-13, 3.315116495457901e-14, 4.515036504562206e-15, 5.537473042327267e-16, 6.551473817122375e-17, 7.234410881124199e-18], [5.480203620041282e-10, 9.077204413758161e-10, 7.51757103219916e-10, 4.150607877942601e-10, 1.7187279324648592e-10, 5.693673394749495e-11, 1.5717979614331743e-11, 3.719239122763473e-12, 7.700510811657646e-13, 1.4172042495353003e-13, 2.3474041406114304e-14, 3.534684061092629e-15, 4.878932120218829e-16, 6.133736868094279e-17, 6.985392552501996e-18, 7.713562062733105e-19], [5.4258004718676844e-11, 8.987093072836851e-11, 7.442942503931593e-11, 4.1094039097965206e-11, 1.7016657543300833e-11, 5.637151086670676e-12, 1.556194388404958e-12, 3.6823174440965e-13, 7.624066201248106e-14, 1.4031353612009758e-14, 2.3241009599015062e-15, 3.499594499818073e-16, 4.830497922245871e-17, 6.154658602620659e-18, 7.184882160773034e-19, 7.636987889775284e-20], [5.013808235640818e-12, 8.3046845339577e-12, 6.877784507023676e-12, 3.797368383400962e-12, 1.5724547589991392e-12, 5.209110561740219e-13, 1.4380293343439182e-13, 3.402711475141969e-14, 7.045155107911743e-15, 1.296592395202229e-15, 2.1476271738396255e-16, 3.233863061416877e-17, 4.463708238144152e-18, 5.687322663148898e-19, 6.728763324414684e-20, 7.331413440683999e-21]] |
| Legacy trial inputs | {"lambda_home": 1.386101901913921, "lambda_away": 1.6563626177251023, "rho": -0.03318338004165527, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3263 |
| Legacy p draw | 0.2490 |
| Legacy p away | 0.4247 |
| Legacy p over 1 5 | 0.8104 |
| Legacy p under 3 5 | 0.6381 |
| Legacy p btts yes | 0.6114 |
| Legacy p over 2 5 | 0.5851 |
| Legacy goal margin distribution | {"-1": 0.2029615477932285, "-10": 2.449234999918794e-06, "-11": 3.625855059131431e-07, "-12": 4.932960918555222e-08, "-13": 6.204605613289091e-09, "-14": 7.194252065732133e-10, "-15": 6.889666847397214e-11, "-2": 0.12895075147939944, "-3": 0.060704849789372586, "-4": 0.022707316732239823, "-5": 0.007012454829874846, "-6": 0.0018391695669931721, "-7": 0.0004185483303425364, "-8": 8.404389739355042e-05, "-9": 1.5090253375155314e-05, "0": 0.24898330959152054, "1": 0.17821598859858717, "10": 4.3431143011694955e-07, "11": 5.380479496877073e-08, "12": 6.125731471597079e-09, "13": 6.447690772395204e-10, "14": 6.256268925263454e-11, "15": 5.013808235640818e-12, "2": 0.09507728405558638, "3": 0.03745553612487358, "4": 0.011724604066656581, "5": 0.0030299968977562748, "6": 0.0006650183331907128, "7": 0.00012664766844157813, "8": 2.1281268348619216e-05, "9": 3.1976254743000152e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3181 |
| Legacy raw p draw | 0.2460 |
| Legacy raw p away | 0.4359 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3861 |
| Legacy lambda away | 1.6564 |
| Legacy model home team | Sassuolo |
| Legacy model away team | Fiorentina |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021565944172805756, "mu": 9.144264930102306, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,428.6172 |
| Elo away rating | 1,446.0432 |
| Elo rating diff | 42.5740 |
| Elo home expectancy | 0.5610 |

</details>


---
