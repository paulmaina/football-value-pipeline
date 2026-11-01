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
| Training as of utc | 2026-11-01T08:58:27.598231+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 104, 'bbs_added_results': 5, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 104, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 96, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-01T08:58:27.598231+00:00', 'observations': 519, 'observations_sha256': '607d727d878090cff21e293a0c106ba3db271a095df300c5ec7253a2a505be40', 'eligible_training_matches': 159, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 170, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 25, 'retrospective_eligible_training_matches': 159, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'a89c80aa493ee5c28b0fa6f6068c73904c961404b4f23d552b288bf02cafa168', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 98, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2026-09-07T00:00:00+00:00', 'audit_origin_utc': '2026-09-20T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 16, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8156631659695053, 'audit_candidate_poisson_score': 0.8171163607566578, 'audit_gain': -0.0014531947871525563, 'audit_gain_lower95': -0.033785815694565825, 'audit_baseline_briers': [0.5338582914589329, 0.1892500148938406, 0.2176064121126562, 0.2581747697518089], 'audit_candidate_briers': [0.5192218714763052, 0.19736596127012723, 0.22444002091164453, 0.2576791518687599], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1625, 'tuning_matches': 230, 'audit_matches': 126, 'audit_matchdays': 54, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8491508811070271, 'audit_candidate_poisson_score': 0.8475055841753513, 'audit_gain': 0.0016452969316758104, 'audit_gain_lower95': -0.007031596726785112, 'audit_baseline_briers': [0.5766305873660732, 0.1857599971269825, 0.19740716289800384, 0.2438403998097597], 'audit_candidate_briers': [0.5791454762942307, 0.18239875322836724, 0.19920013986525945, 0.2419138132640937], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1844.637 |
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
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261101T085827598231Z_132acb7e848809b711ff4f09e1a11af89ac39e8320219a21c9d46c8c2770fbe7.json |
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

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **47.3%**. Expected goals are 1.54 for Athletic Bilbao and 1.04 for Real Sociedad (2.58 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 52.0%; Under 3.5 goals: 69.7%; Double Chance 1X: 74.1%; Double Chance X2: 52.7%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 55.5%; BTTS No (at least one team does not score): 44.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 47.3% | 2.11 |
| Draw | 26.8% | 3.73 |
| Real Sociedad win | 25.9% | 3.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.54 |
| Real Sociedad expected goals | 1.04 |
| Expected total goals | 2.58 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 52.0% |
| Under 2.5 | 48.0% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.70% |
| 2 | 1-0 | 9.48% |
| 3 | 2-1 | 9.11% |
| 4 | 2-0 | 8.13% |
| 5 | 0-0 | 6.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 47.3% | 46.8% | 2.10 | -0.6% |
| Draw | 26.8% | 27.1% | 3.58 | -4.1% |
| Real Sociedad win | 25.9% | 26.2% | 3.70 | -4.3% |

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
| Market best home last update utc | 2026-11-01T08:59:15Z |
| Market best draw last update utc | 2026-11-01T08:59:15Z |
| Market best away last update utc | 2026-11-01T08:59:15Z |
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
| Dc lambda away | 1.0388 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T08:58:27.598231+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.5% |
| P btts no | 44.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.38 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.79 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.15751465784298999, "-10": 6.400905859168248e-08, "-11": 6.428927571847548e-09, "-12": 5.931385192815917e-10, "-13": 5.0584241534473577e-11, "-14": 3.986743102111632e-12, "-15": 2.647992801371206e-13, "-2": 0.07068609625512981, "-3": 0.023094508032560676, "-4": 0.005944460980779779, "-5": 0.0012568980314311832, "-6": 0.00022499144629959075, "-7": 3.4873387495470664e-05, "-8": 4.762404324271435e-06, "-9": 5.809406330642857e-07, "0": 0.26782461792462, "1": 0.21909694110731126, "10": 3.1462367503700007e-06, "11": 4.6991264845008824e-07, "12": 6.447084652245268e-08, "13": 8.176192890287646e-09, "14": 9.582587195451992e-10, "15": 9.464767945641916e-11, "2": 0.14529638879685414, "3": 0.07059243782767993, "4": 0.027020326198137913, "5": 0.00849584919954093, "6": 0.002261525029528903, "7": 0.0005212645239088086, "8": 0.00010585684339203415, "9": 1.9202292077139574e-05} |
| Raw goal margin distribution | {"-1": 0.1575248258338836, "-10": 3.518927534915338e-08, "-11": 3.2835384352624526e-09, "-12": 2.813661658191858e-10, "-13": 2.2283605780250284e-11, "-14": 1.6330793305762161e-12, "-15": 1.021640668965948e-13, "-2": 0.06740064207812992, "-3": 0.020758877603594877, "-4": 0.005008777109115952, "-5": 0.000989561472347379, "-6": 0.00016518247417599284, "-7": 2.384380085132302e-05, "-8": 3.0296743407031823e-06, "-9": 3.436419128676858e-07, "0": 0.261103079855392, "1": 0.23576613664045015, "10": 1.860787349406537e-06, "11": 2.582005527767349e-07, "12": 3.290149090121658e-08, "13": 3.874876046851214e-09, "14": 4.2228754447192854e-10, "15": 3.9285094732703706e-11, "2": 0.14904634072803583, "3": 0.06826369538390015, "4": 0.02449324205897246, "5": 0.00719591440433774, "6": 0.0017862235860142484, "7": 0.00038342107524554656, "8": 7.244778062965855e-05, "9": 1.2219794628988923e-05} |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 25.2% |
| Raw p over 1 5 | 73.3% |
| Raw p under 3 5 | 74.0% |
| Raw p btts yes | 51.1% |
| P home draw | 74.1% |
| P draw away | 52.7% |
| P home away | 73.2% |
| Raw p home draw | 74.8% |
| Raw p draw away | 51.3% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0784 |
| Totals anchor target over 2 5 | 0.5201 |
| Totals anchor reference over odds | 1.87 |
| Totals anchor reference under odds | 2.02 |
| Totals anchor reference last update utc | 2026-11-01T08:59:15Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4747 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.8, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.65, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.84, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.01, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:50Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.74, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:50Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.54, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 7.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.75, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.65, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.75, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.10 |
| Reference draw odds | 3.58 |
| Reference away odds | 3.70 |
| Market reference 1x2 last update utc | 2026-11-01T08:59:15Z |
| Market reference home last update utc | 2026-11-01T08:59:15Z |
| Market reference draw last update utc | 2026-11-01T08:59:15Z |
| Market reference away last update utc | 2026-11-01T08:59:15Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-11-01T08:58:50Z |
| Market reference under 2 5 last update utc | 2026-11-01T08:58:50Z |
| Home probability edge | +0.6% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Market p over 1 5 | 78.2% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 3.60 |
| Market reference over 1 5 last update utc | 2026-11-01T08:59:19Z |
| Market over 1 5 bookmakers | 0 |
| Raw edge prob home | 0.0194 |
| Raw ev home | 0.0227 |
| Raw edge prob draw | -0.0096 |
| Raw ev draw | -0.0653 |
| Raw edge prob away | -0.0098 |
| Raw ev away | -0.0681 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10776461258249265, 0.09648314792827299, 0.0441987621574616, 0.013144317524273868, 0.0029317520685887425, 0.0005231261448638321, 7.778652407552395e-05, 9.914150678011884e-06, 1.1056424840957077e-06, 1.0960273674261323e-07, 9.778462809491339e-09, 7.930984352993741e-10, 5.896509965845194e-11, 4.046698742724347e-12, 2.5788259316573583e-13], [0.14162477242511132, 0.12768663789831747, 0.05891317682996274, 0.01752025316586825, 0.00390777523187308, 0.0006972824932731018, 0.00010368279617251357, 1.321471651019996e-05, 1.473727045662371e-06, 1.4609109159577118e-07, 1.3033856164759674e-08, 1.057132509636831e-09, 7.859544415744019e-11, 5.3939039685856935e-12, 3.437354819670559e-13], [0.09607299930273572, 0.08571375848800643, 0.03722859350591198, 0.011676500907302672, 0.002604365394068191, 0.00046470901922872744, 6.910015809238087e-05, 8.807044502170622e-06, 9.82176171935492e-07, 9.736347685260881e-08, 8.686508801708104e-09, 7.045336954354391e-10, 5.238050879322026e-11, 3.5948067637396576e-12, 2.290850268579179e-13], [0.04268570219487806, 0.03808304097276746, 0.016988334912615203, 0.004919099927950232, 0.0011571322476103378, 0.00020647248390325283, 3.070153728266473e-05, 3.913012829464026e-06, 4.363856638433264e-07, 4.325906766470669e-08, 3.859458229824837e-09, 3.130277573082671e-10, 2.327291554745833e-11, 1.5971901791220016e-12, 1.017835948157421e-13], [0.014224099266394511, 0.012690360643236951, 0.005661000047851841, 0.0016835309067888078, 0.00036560926092308644, 6.880254876470823e-05, 1.023063207314265e-05, 1.3039280146514773e-06, 1.4541620921685933e-07, 1.441516107255929e-08, 1.2860820872736857e-09, 1.0430981954477276e-10, 7.75520242010181e-12, 5.322295402667132e-13, 3.391721072643652e-14], [0.003791902010027559, 0.003383033479297583, 0.0015091259599776853, 0.0004488005960755745, 0.00010010196980547404, 1.739116617340039e-05, 2.7273118385537894e-06, 3.476049461613092e-07, 3.876547862139362e-08, 3.842835825467625e-09, 3.428475266138704e-10, 2.7807216962546856e-11, 2.0674045571680435e-12, 1.4188330844269703e-13, 9.041749295996221e-15], [0.0008423802791987306, 0.0007515491379505979, 0.0003352560124576679, 9.9702146950773e-05, 2.2237896720454883e-05, 3.968011246889476e-06, 5.744837248347762e-07, 7.722128652688871e-08, 8.611845616792362e-09, 8.536953505158684e-10, 7.616441417205487e-11, 6.177441064327414e-12, 4.592789643504758e-13, 3.1519722994827635e-14, 2.0086466570772138e-15], [0.00016040300007144674, 0.00014310726331705312, 6.38382349612361e-05, 1.898492151274039e-05, 4.234459705814685e-06, 7.555743219959195e-07, 1.123505310637491e-07, 1.394225992895351e-08, 1.6398364339673098e-09, 1.6255757494708092e-10, 1.4502951735174273e-11, 1.1762859411015534e-12, 8.745423601511392e-14, 6.001871428662164e-15, 3.824792173258572e-16], [2.672543824191224e-05, 2.38437206663555e-05, 1.0636364688748123e-05, 3.1631599607881206e-06, 7.055216629689535e-07, 1.2588950874162122e-07, 1.8719208356781627e-08, 2.3858252367986685e-09, 2.590626040781776e-10, 2.7084421289303428e-11, 2.416399573269765e-12, 1.959860929018573e-13, 1.4571128860273716e-14, 9.999977814078395e-16, 6.372651818796452e-17], [3.958080855534711e-06, 3.5312937973160934e-06, 1.5752629036779107e-06, 4.6846913305821106e-07, 1.0448890536743616e-07, 1.864444092375818e-08, 2.772345192512037e-09, 3.533445965954232e-10, 3.940557393262278e-11, 3.803393267397476e-12, 3.5787270553648227e-13, 2.902585900534831e-14, 2.1580078748692606e-15, 1.4810129728613006e-16, 9.438000954240638e-18], [5.275783890025534e-07, 4.7069131750494525e-07, 2.09969097477066e-07, 6.244293624539534e-08, 1.3927479092628348e-08, 2.485144812707669e-09, 3.695299474186416e-10, 4.709781832119414e-11, 5.252426610745829e-12, 5.206749372952267e-13, 4.522960124772151e-14, 3.8688992196922105e-15, 2.8764402740442293e-16, 1.9740638628477232e-17, 1.2580049575996266e-18], [6.39288140576604e-08, 5.7035576783610825e-08, 2.5442807496046164e-08, 7.566463948596084e-09, 1.6876491527409422e-09, 3.0113508049166686e-10, 4.47774431055193e-11, 5.707033746529217e-12, 6.3645784427355e-13, 6.309229480335943e-14, 5.628925669519774e-15, 4.44517552209157e-16, 3.4854993923272567e-17, 2.3920532807367914e-18, 1.5243756509824025e-19], [7.100970976086029e-09, 6.3352962402751745e-09, 2.826090867517335e-09, 8.404542096169837e-10, 1.8745768755573543e-10, 3.3448946268954355e-11, 4.973709094444487e-12, 6.339157325380015e-13, 7.069533114774253e-14, 7.008053579865122e-15, 6.252397826393896e-16, 5.0711108991170297e-17, 3.670945591017036e-18, 2.6570023502145593e-19, 1.6932188425261763e-20], [7.280760092995272e-10, 6.495699278146108e-10, 2.8976445160377066e-10, 8.617336262852914e-11, 1.9220391905238508e-11, 3.429583840969012e-12, 5.099638177786062e-13, 6.499658121865037e-14, 7.248526258098788e-15, 7.185490126024771e-16, 6.410701963610949e-17, 5.1995060937138715e-18, 3.8657168056930674e-19, 2.5831092142173414e-20, 1.7360893628334806e-21], [6.931879761167749e-11, 6.184437584220537e-11, 2.7587948399927505e-11, 8.20440971446329e-12, 1.829938687003538e-12, 3.265244632811511e-13, 4.8552731064279194e-14, 6.1882067275932566e-15, 6.901190511022187e-16, 6.841174951854598e-17, 6.1035131811562544e-18, 4.950355539631016e-19, 3.6804789260355613e-20, 2.5258652200847615e-21, 1.5672497989325348e-22]] |
| Legacy trial inputs | {"lambda_home": 1.332914632769123, "lambda_away": 0.8921732340000514, "rho": -0.019671678951725675, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4672 |
| Legacy p draw | 0.2780 |
| Legacy p away | 0.2548 |
| Legacy p over 1 5 | 0.6541 |
| Legacy p under 3 5 | 0.8143 |
| Legacy p btts yes | 0.4354 |
| Legacy p over 2 5 | 0.3862 |
| Legacy goal margin distribution | {"-1": 0.16830156666232116, "-10": 1.088960693531124e-08, "-11": 8.753904698153697e-10, "-12": 6.458808865389554e-11, "-13": 4.3904342246914026e-12, "-14": 2.5788259316573583e-13, "-2": 0.06454044021516951, "-3": 0.01754884687454808, "-4": 0.003702197069184152, "-5": 0.0006360671354768635, "-6": 9.20279901799729e-05, "-7": 1.1489207067882992e-05, "-8": 1.2607410113448706e-06, "-9": 1.2336494078964537e-07, "0": 0.2779825330306653, "1": 0.24611458148986232, "10": 5.875280599549971e-07, "11": 7.05620791592538e-08, "12": 7.778128852300567e-09, "13": 7.899203851417325e-10, "14": 6.931879761167749e-11, "2": 0.14028885346834216, "3": 0.056989254114344565, "4": 0.0179620982210748, "5": 0.004610559562369038, "6": 0.000996606609991159, "7": 0.00018588614819197658, "8": 3.0474458536478122e-05, "9": 4.455074981661687e-06} |
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
| Market p home draw | 73.6% |
| Market home draw odds | 1.32 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T08:58:47Z |
| Market reference home draw last update utc | 2026-11-01T08:59:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.7% |
| Market draw away odds | 1.81 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T08:58:47Z |
| Market reference draw away last update utc | 2026-11-01T08:59:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.6% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T08:58:47Z |
| Market reference home away last update utc | 2026-11-01T08:59:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.31 |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home away odds | 1.31 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:58:47Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.1, "price": 1.72, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:58:47Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.72, "price": 2.1, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:58:47Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.16, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:58:47Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.16, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p under 3 5 | 69.3% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T08:59:15Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market reference under 3 5 last update utc | 2026-11-01T08:59:19Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.3% |
| Market btts yes odds | 1.71 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T08:58:47Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.26 |
| Market reference btts yes last update utc | 2026-11-01T08:59:15Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 10.303234661826316, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,505.1233 |
| Elo away rating | 1,510.6645 |
| Elo rating diff | 54.4588 |
| Elo home expectancy | 0.5777 |

</details>


---

## 2026-11-01 — Elche CF vs Valencia

The model's most likely 1X2 outcome is **Elche CF win** at **42.7%**. Expected goals are 1.49 for Elche CF and 1.06 for Valencia (2.56 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 48.8%; Under 3.5 goals: 72.5%; Double Chance 1X: 70.8%; Double Chance X2: 57.3%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 53.7%; BTTS No (at least one team does not score): 46.3%.

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
| Over 3.5 | 27.5% |
| Under 3.5 | 72.5% |
| Over 4.5 | 12.8% |
| Under 4.5 | 87.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.37% |
| 2 | 1-0 | 9.52% |
| 3 | 2-1 | 8.43% |
| 4 | 0-1 | 8.10% |
| 5 | 0-0 | 7.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 42.7% | 41.0% | 2.39 | +2.1% |
| Draw | 28.1% | 28.7% | 3.38 | -5.1% |
| Valencia win | 29.2% | 30.3% | 3.21 | -6.2% |
| Over 2.5 | 48.8% | 48.8% | 2.00 | -2.4% |
| Under 2.5 | 51.2% | 51.2% | 1.91 | -2.2% |

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
| Market best home last update utc | 2026-11-01T08:59:15Z |
| Market best draw last update utc | 2026-11-01T08:59:15Z |
| Market best away last update utc | 2026-11-01T08:59:15Z |
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
| Bbs statistics cutoff utc | 2026-11-01T08:58:27.598231+00:00 |
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
| Fair Under 0.5 odds | 12.64 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.92 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.82 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.17767927240606582, "-10": 6.793964972736224e-08, "-11": 6.751483115197665e-09, "-12": 6.162081042313444e-10, "-13": 5.198360305150951e-11, "-14": 4.055771621455757e-12, "-15": 2.6857433563319156e-13, "-2": 0.07998351798620394, "-3": 0.026064903002475333, "-4": 0.006671074543696112, "-5": 0.001400053378209939, "-6": 0.00024847939016242837, "-7": 3.8157574307469996e-05, "-8": 5.160069075337788e-06, "-9": 6.230828770858504e-07, "0": 0.28077156971590633, "1": 0.2074919751876299, "10": 1.663657669698885e-06, "11": 2.3197648329296976e-07, "12": 2.97081967642117e-08, "13": 3.5165708768719232e-09, "14": 3.8497329206303367e-10, "15": 3.577055926853405e-11, "2": 0.1303491710660103, "3": 0.05960298303579231, "4": 0.021404830246053008, "5": 0.006303252426424002, "6": 0.0015696925237311966, "7": 0.0003382276338043975, "8": 6.417826253874329e-05, "9": 1.0873825722839785e-05} |
| Raw goal margin distribution | {"-1": 0.16469105360544203, "-10": 4.596356194578968e-08, "-11": 4.394718164464535e-09, "-12": 3.8586835355266967e-10, "-13": 3.1313196216165594e-11, "-14": 2.3515512711129365e-12, "-15": 1.5086262282546122e-13, "-2": 0.07227716104280307, "-3": 0.022829899261350012, "-4": 0.00564739215121849, "-5": 0.0011436459037304383, "-6": 0.00019565629478833957, "-7": 2.8943604146265733e-05, "-8": 3.7687476189425894e-06, "-9": 4.380407672602904e-07, "0": 0.2654669623136831, "1": 0.23236270229820505, "10": 1.3597366118260697e-06, "11": 1.8242159750911785e-07, "12": 2.2474420342416975e-08, "13": 2.5590622368636795e-09, "14": 2.696571948096963e-10, "15": 2.4274110550610873e-11, "2": 0.14230144447834897, "3": 0.06306905582823805, "4": 0.021890939044298063, "5": 0.006220311531496497, "6": 0.0014932017613106723, "7": 0.00030994268425298013, "8": 5.662783352250218e-05, "9": 9.235311191971083e-06} |
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
| Totals anchor target over 2 5 | 0.4881 |
| Totals anchor reference over odds | 2.00 |
| Totals anchor reference under odds | 1.91 |
| Totals anchor reference last update utc | 2026-11-01T08:59:15Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4645 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:50Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:50Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.34, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.06, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.34, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.39 |
| Reference draw odds | 3.38 |
| Reference away odds | 3.21 |
| Market reference 1x2 last update utc | 2026-11-01T08:59:15Z |
| Market reference home last update utc | 2026-11-01T08:59:15Z |
| Market reference draw last update utc | 2026-11-01T08:59:15Z |
| Market reference away last update utc | 2026-11-01T08:59:15Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-11-01T08:59:15Z |
| Market reference under 2 5 last update utc | 2026-11-01T08:59:15Z |
| Market best over 2 5 last update utc | 2026-11-01T08:59:15Z |
| Market best under 2 5 last update utc | 2026-11-01T08:59:15Z |
| Home probability edge | +1.7% |
| Draw probability edge | -0.7% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Market p over 1 5 | 75.5% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T08:59:15Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.30 |
| Market reference over 1 5 last update utc | 2026-11-01T08:59:19Z |
| Market over 1 5 bookmakers | 1 |
| Raw edge prob home | 0.0580 |
| Raw ev home | 0.1178 |
| Raw edge prob draw | -0.0219 |
| Raw ev draw | -0.1027 |
| Raw edge prob away | -0.0361 |
| Raw ev away | -0.1435 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09428552170385192, 0.0966764127999645, 0.05657053305259085, 0.021521760472905282, 0.006140822998200851, 0.0014017331767150539, 0.0002666385134478094, 4.347440197688725e-05, 6.202294831521721e-06, 7.865361260443674e-07, 8.976922009349062e-08, 9.314156786901814e-09, 8.858722048298175e-10, 7.777436974486967e-11, 6.340408536761004e-12], [0.1147510531858326, 0.13434307381605629, 0.0712191312973705, 0.027094690506901664, 0.007730952066090688, 0.0017647035261899053, 0.0003356829478789139, 5.473183608837844e-05, 7.808341659791339e-06, 9.902049107227475e-07, 1.1301441806032364e-07, 1.1726001494699977e-08, 1.1152634678165967e-09, 9.791357357868195e-11, 7.982219075764394e-12], [0.07389156810134809, 0.08433418657198337, 0.04732712366427008, 0.01705534857589849, 0.004866417731442731, 0.0011108314289332614, 0.00021130301103095082, 3.445215742355342e-05, 4.91513231249231e-06, 6.233062492314149e-07, 7.113940990136635e-08, 7.381189419479522e-09, 7.020271072198535e-10, 6.163385137287059e-11, 5.024583274412011e-12], [0.03100844795815177, 0.035390671799299625, 0.020196103527917363, 0.007555840464817938, 0.002042182414657889, 0.00046615817527531904, 8.867288364982564e-05, 1.4457778579675561e-05, 2.0626253906305635e-06, 2.615692140241707e-07, 2.9853510304106e-08, 3.097501296349069e-09, 2.9460426377176187e-10, 2.5864521783254066e-11, 2.108556266694821e-12], [0.009759474620851876, 0.01113871818758225, 0.00635644067341946, 0.002418251804457781, 0.0006785439384254329, 0.0001467167556093724, 2.7908547977188278e-05, 4.55038327982958e-06, 6.49182447936472e-07, 8.232524598813305e-08, 9.395974172892087e-09, 9.74895142464794e-10, 9.272256513307394e-11, 8.140495914687631e-12, 6.636385477666725e-13], [0.0024573263390311024, 0.0028046044125069384, 0.001600480527497783, 0.0006088887039889549, 0.00017373475378593584, 3.899897069708647e-05, 7.027059620804851e-06, 1.1457355155492931e-06, 1.634568652643041e-07, 2.072857435395388e-08, 2.365800999837872e-09, 2.454676716156171e-10, 2.3346502796084042e-11, 2.049685644060922e-12, 1.6709674919786296e-13], [0.0005156060282516275, 0.0005884733008314486, 0.0003358192174029991, 0.0001277594600783923, 3.645372002326753e-05, 8.321097805011943e-06, 1.5565598438309361e-06, 2.4040280251589517e-07, 3.4297172398607704e-08, 4.349352271287982e-09, 4.964018159839108e-10, 5.150500737960844e-11, 4.898656474337351e-12, 4.30073229311223e-13, 3.506090738507239e-14], [9.273129980340678e-05, 0.00010583641597586224, 6.039679682244804e-05, 2.2977428784965684e-05, 6.556170128362737e-06, 1.496542268651408e-06, 2.84673154958178e-07, 4.5644128627664056e-08, 6.168316896699083e-09, 7.822272574800156e-10, 8.927743877830484e-11, 9.263131187372948e-12, 8.810191449778548e-13, 7.734829963084792e-14, 6.305673975785917e-15], [1.4592938805117474e-05, 1.6655264672910086e-05, 9.504522873329958e-06, 3.6159119182930978e-06, 1.0317313537281154e-06, 2.355078575626667e-07, 4.479844387570848e-08, 7.304216978290289e-09, 1.0247551860452956e-09, 1.230975358298749e-10, 1.4049411617560019e-11, 1.4577203905012281e-12, 1.386442171743011e-13, 1.2172146897388647e-14, 9.923112762222395e-16], [2.0412991410798612e-06, 2.3297827754438686e-06, 1.329517970081432e-06, 5.058033883102215e-07, 1.4432132926177994e-07, 3.294346627367769e-08, 6.2665256276637934e-09, 1.0217333220650672e-09, 1.4576603735703458e-10, 1.8178175176810472e-11, 1.9652691106705306e-12, 2.0390981013510823e-13, 1.9393922308119506e-14, 1.7026723224539231e-15, 1.3880714384452684e-16], [2.56988123853498e-07, 2.93306596960005e-07, 1.6737886274717794e-07, 6.367781242087966e-08, 1.8169246678567406e-08, 4.1473978117802e-09, 7.889204633090952e-10, 1.286305001711804e-10, 1.8351127332629233e-11, 2.3271748591177163e-12, 2.6119536293110704e-13, 2.5671102528472738e-14, 2.4415861486560763e-15, 2.1435690481564408e-16, 1.747504163216223e-17], [2.9412149829073996e-08, 3.356877915713093e-08, 1.9156419041941648e-08, 7.2878907072696946e-09, 2.07946031738056e-09, 4.746674049046429e-10, 9.02915143397734e-11, 1.4721690196782175e-11, 2.1002764584849093e-12, 2.663438862795245e-13, 3.0398454891356854e-14, 3.1016677218124905e-15, 2.794381956179519e-16, 2.4533030191420107e-17, 2.000008930558466e-18], [3.0856873820206676e-09, 3.5217676666601723e-09, 2.0097381818716524e-09, 7.645871698483655e-10, 2.1816033510107766e-10, 4.979830547860586e-11, 9.472663104223985e-12, 1.5444819214583172e-12, 2.2034419803939843e-13, 2.794266906524022e-14, 3.1891626160037642e-15, 3.308969443362574e-16, 3.094909518368787e-17, 2.5738091960066856e-18, 2.098249314251915e-19], [2.98823654899124e-10, 3.4105447362843167e-10, 1.9462675071896993e-10, 7.404403113365538e-11, 2.1127049055186826e-11, 4.822559711526992e-12, 9.17350158971267e-13, 1.4957047670641343e-13, 2.1338538368339612e-14, 2.706019587844251e-15, 3.088443873266981e-16, 3.204467013659718e-17, 3.0477780475922327e-18, 2.6313367444233677e-19, 2.0319833195926073e-20], [2.6871588395468794e-11, 3.066917657128003e-11, 1.7501726688381398e-11, 6.658377592083647e-12, 1.899840782060934e-12, 4.336666038853939e-13, 8.24923177340671e-14, 1.3450060663790433e-14, 1.9188588674096336e-15, 2.433376453385986e-16, 2.777269844080908e-17, 2.8816031531034405e-18, 2.7407012755831217e-19, 2.4061745385541988e-20, 1.9290147002886997e-21]] |
| Legacy trial inputs | {"lambda_home": 1.2589439670147984, "lambda_away": 1.1413235466367744, "rho": -0.019671678951725675, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-11-01T08:59:15Z", "over": 2.0, "under": 1.91, "bookmaker": "pinnacle", "event_id": "5262991e389930615bec34b642428c93", "kickoff_utc": "2026-11-01T17:30:00Z", "home_team": "Elche CF", "away_team": "Valencia"}} |
| Legacy p home | 0.3988 |
| Legacy p draw | 0.2842 |
| Legacy p away | 0.3169 |
| Legacy p over 1 5 | 0.6943 |
| Legacy p under 3 5 | 0.7786 |
| Legacy p btts yes | 0.4906 |
| Legacy p over 2 5 | 0.4295 |
| Legacy goal margin distribution | {"-1": 0.1871470655993297, "-10": 1.0222377685574146e-07, "-11": 1.0493162662357976e-08, "-12": 9.888103616829113e-10, "-13": 8.575658882063406e-11, "-14": 6.340408536761004e-12, "-2": 0.08902688884335876, "-3": 0.030456935131831193, "-4": 0.008131957730828986, "-5": 0.0017740156508534771, "-6": 0.0003265566974815459, "-7": 5.193690207423827e-05, "-8": 7.266831460753868e-06, "-9": 9.072346453806062e-07, "0": 0.28423070580528886, "1": 0.22188194306727793, "10": 2.9264258506441634e-07, "11": 3.313520262404523e-08, "12": 3.4442435823374804e-09, "13": 3.29492831470404e-10, "14": 2.6871588395468794e-11, "2": 0.11628556537914593, "3": 0.04388220420858078, "4": 0.012923941158232012, "5": 0.0031099609091879434, "6": 0.0006314714240273658, "7": 0.00011078189044824226, "8": 1.709761139940292e-05, "9": 2.3545483049673154e-06} |
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
| Market p home draw | 67.9% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T08:53:21Z |
| Market reference home draw last update utc | 2026-11-01T08:59:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.2% |
| Market draw away odds | 1.64 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T08:53:21Z |
| Market reference draw away last update utc | 2026-11-01T08:59:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T08:53:21Z |
| Market reference home away last update utc | 2026-11-01T08:59:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.42 |
| Market reference dc draw away odds | 1.60 |
| Market reference dc home away odds | 1.34 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:53:21Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.23, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:53:21Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.23, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:53:21Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.06, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:53:21Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.06, "price": 1.76, "quote_source": "The Odds API", "side": "Under"}] |
| Market p under 3 5 | 73.1% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T08:59:15Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.10 |
| Market reference under 3 5 last update utc | 2026-11-01T08:59:19Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.1% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T08:53:21Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-11-01T08:59:15Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 9.23453524708649, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,471.9746 |
| Elo away rating | 1,446.4037 |
| Elo rating diff | 85.5709 |
| Elo home expectancy | 0.6207 |

</details>


---

## 2026-11-01 — Getafe vs Sevilla

The model's most likely 1X2 outcome is **Sevilla win** at **37.4%**. Expected goals are 1.03 for Getafe and 0.92 for Sevilla (1.94 combined). The most likely exact score is 1-1 at 14.4%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 34.1%; Under 3.5 goals: 84.3%; Double Chance 1X: 62.6%; Double Chance X2: 69.5%; Double Chance 12 (either team wins): 68.0%; Under 4.5 goals: 94.1%; BTTS Yes (both teams score): 42.4%; BTTS No (at least one team does not score): 57.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 30.5% | 3.27 |
| Draw | 32.0% | 3.12 |
| Sevilla win | 37.4% | 2.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 1.03 |
| Sevilla expected goals | 0.92 |
| Expected total goals | 1.94 |
| Over 0.5 | 86.6% |
| Under 0.5 | 13.4% |
| Over 1.5 | 61.7% |
| Under 1.5 | 38.3% |
| Over 2.5 | 34.1% |
| Under 2.5 | 65.9% |
| Over 3.5 | 15.7% |
| Under 3.5 | 84.3% |
| Over 4.5 | 5.9% |
| Under 4.5 | 94.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.41% |
| 2 | 0-1 | 14.08% |
| 3 | 0-0 | 13.35% |
| 4 | 1-0 | 10.83% |
| 5 | 1-2 | 7.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 30.5% | 27.8% | 3.49 | +6.6% |
| Draw | 32.0% | 32.0% | 3.04 | -2.6% |
| Sevilla win | 37.4% | 40.1% | 2.44 | -8.7% |

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
| Market best home last update utc | 2026-11-01T08:59:15Z |
| Market best draw last update utc | 2026-11-01T08:59:15Z |
| Market best away last update utc | 2026-11-01T08:59:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Getafe |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0251 |
| Dc lambda away | 0.9158 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T08:58:27.598231+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 42.4% |
| P btts no | 57.6% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.49 |
| Fair Over 1.5 odds | 1.62 |
| Fair Under 1.5 odds | 2.61 |
| Fair Over 2.5 odds | 2.93 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.38 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.87 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.23455859981858054, "-10": 3.767330721152968e-08, "-11": 3.3385632122699053e-09, "-12": 2.707655737086117e-10, "-13": 1.8898603825648838e-11, "-2": 0.10058315807494447, "-3": 0.030352806003347742, "-4": 0.007087714268745897, "-5": 0.0013458837851225325, "-6": 0.0002150288498682089, "-7": 2.9627107923944026e-05, "-8": 3.586550363326985e-06, "-9": 3.87055467520989e-07, "0": 0.32044359109484366, "1": 0.18026276682841053, "10": 7.968701870125096e-08, "11": 7.904213404047975e-09, "12": 7.175261290197662e-10, "13": 5.605562741073359e-11, "2": 0.08636093308158906, "3": 0.029169979673675593, "4": 0.00762410209326744, "5": 0.0016204486917608468, "6": 0.0002897808468747187, "7": 4.4689698682934186e-05, "8": 6.055364944515756e-06, "9": 7.314452381674598e-07} |
| Raw goal margin distribution | {"-1": 0.2001930255412092, "-10": 1.7880055382214594e-08, "-11": 1.4780993060177798e-09, "-12": 1.1188389683077576e-10, "-13": 7.35113901468181e-12, "-2": 0.08140693496862081, "-3": 0.023121428964111287, "-4": 0.005063188973265814, "-5": 0.0008998453017064427, "-6": 0.0001343949318897298, "-7": 1.7296891948953273e-05, "-8": 1.9548860489482546e-06, "-9": 1.968893099261665e-07, "0": 0.32042583871806224, "1": 0.22448877833737146, "10": 5.518500372889821e-08, "11": 5.106237977233027e-09, "12": 4.326236369569345e-10, "13": 3.1815775767908214e-11, "2": 0.10198865086633016, "3": 0.03242278646564179, "4": 0.007947033129090961, "5": 0.0015808620055217325, "6": 0.00026427386814933945, "7": 3.8070153162407155e-05, "8": 4.81596387455731e-06, "9": 5.429116134178517e-07} |
| Unadjusted home-win probability | 36.9% |
| Unadjusted draw probability | 32.0% |
| Unadjusted away-win probability | 31.1% |
| Raw p over 1 5 | 58.1% |
| Raw p under 3 5 | 86.8% |
| Raw p btts yes | 38.8% |
| P home draw | 62.6% |
| P draw away | 69.5% |
| P home away | 68.0% |
| Raw p home draw | 68.9% |
| Raw p draw away | 63.1% |
| Raw p home away | 68.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0732 |
| Totals anchor target over 2 5 | 0.3410 |
| Totals anchor reference over odds | 2.75 |
| Totals anchor reference under odds | 1.48 |
| Totals anchor reference last update utc | 2026-11-01T08:59:15Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3066 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:50Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:50Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.9, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.59, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.3, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 3.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.9, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.49 |
| Reference draw odds | 3.04 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-11-01T08:59:15Z |
| Market reference home last update utc | 2026-11-01T08:59:15Z |
| Market reference draw last update utc | 2026-11-01T08:59:15Z |
| Market reference away last update utc | 2026-11-01T08:59:15Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.65 |
| Reference Under 2.5 odds | 1.49 |
| Market reference over 2 5 last update utc | 2026-11-01T08:58:51Z |
| Market reference under 2 5 last update utc | 2026-11-01T08:58:51Z |
| Home probability edge | +2.7% |
| Draw probability edge | -0.0% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Market p over 1 5 | 62.7% |
| Market over 1 5 odds | 1.55 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T08:59:15Z |
| Market reference over 1 5 odds | 1.50 |
| Market reference over 1 5 opposite odds | 2.35 |
| Market reference over 1 5 last update utc | 2026-11-01T08:59:19Z |
| Market over 1 5 bookmakers | 1 |
| Raw edge prob home | 0.0905 |
| Raw ev home | 0.2869 |
| Raw edge prob draw | -0.0000 |
| Raw ev draw | -0.0259 |
| Raw edge prob away | -0.0905 |
| Raw ev away | -0.2416 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.14035724615429696, 0.14341759885004568, 0.0699307550213929, 0.022268269866835236, 0.005318216313164068, 0.00101609779018271, 0.00016177960466722867, 2.2078280321181514e-05, 2.6364210437737977e-06, 2.798412766428668e-07, 2.6733220882242925e-08, 2.3216573055344223e-09, 1.8482315614258167e-10, 1.358165027466492e-11], [0.12234205403368917, 0.13914835752228932, 0.07256018358704383, 0.02310556706000251, 0.005518183693580116, 0.001054303534624964, 0.00016786259224145966, 2.290843382001338e-05, 2.735551688101339e-06, 2.903634374064376e-07, 2.7738402288022432e-08, 2.408952688473687e-09, 1.9177259185518624e-10, 1.4092326574240979e-11], [0.06468670047162148, 0.061795167339029, 0.033816402572542925, 0.011987173506446873, 0.0028628349697548405, 0.0005469729163188211, 8.70871514737064e-05, 1.1884900736187606e-05, 1.4192048451340118e-06, 1.5064061812811076e-07, 1.4390689488583869e-08, 1.249765208989102e-09, 9.949166477409482e-11, 7.311102268827863e-12], [0.02237298339109452, 0.021372898021480218, 0.010208758524766545, 0.0037243849630438264, 0.0009901596272926133, 0.00018917978321599755, 3.0120556146680306e-05, 4.110592824133685e-06, 4.908558667739419e-07, 5.210159156105048e-08, 4.977262011620653e-09, 4.3225231863151883e-10, 3.4410865716047723e-11, 2.5286676927174403e-12], [0.005803554465238801, 0.005544132205319931, 0.0026481531356491606, 0.0008432597167769987, 0.00023073009819110234, 4.907325752778825e-05, 7.813275729249565e-06, 1.0662882514262908e-06, 1.2732806830485065e-07, 1.3515158844239866e-08, 1.29110233835432e-09, 1.1212630117547552e-10, 8.9261825250625e-12, 6.559366903663294e-13], [0.001204354156697756, 0.00115051882544609, 0.0005495449824058871, 0.00017499333402643658, 4.1792757555018264e-05, 9.148163359399612e-06, 1.6214116983496274e-06, 2.2127623606103173e-07, 2.6423132451972747e-08, 2.8046670070875216e-09, 2.6792967606882553e-10, 2.326846033834404e-11, 1.8523622190318415e-12, 1.3612004234731555e-13], [0.00020827307119038727, 0.00019896314377744093, 9.50346877672338e-05, 3.026219398408886e-05, 7.227364078159062e-06, 1.3808593400922028e-06, 2.51884288860463e-07, 3.826605405858692e-08, 4.56944239834914e-09, 4.850206295082885e-10, 4.63339925283324e-11, 4.0238941922420145e-12, 3.203353151307484e-13, 2.3539703095287865e-14], [3.0872033499809635e-05, 2.9492035647324222e-05, 1.4086862250722906e-05, 4.485723771752058e-06, 1.071302327569199e-06, 2.0468289809239182e-07, 3.258890891749256e-08, 5.095357595141486e-09, 6.773222192912863e-10, 7.189394690680366e-11, 6.8680245666854485e-12, 5.964563521946013e-13, 4.748286719625125e-14, 3.489258108980346e-15], [4.004104520547287e-06, 3.825118719708594e-06, 1.8270668441323866e-06, 5.817986311951104e-07, 1.3894797350226734e-07, 2.6547383655032617e-08, 4.226783360967795e-09, 5.768348123504618e-10, 7.891587268176409e-11, 9.32464904883231e-12, 8.907831813173109e-13, 7.736042318515475e-14, 6.158530606356995e-15, 4.525569774213489e-16], [4.616289658784501e-07, 4.4099388262223197e-07, 2.1064059979442197e-07, 6.70749474919769e-08, 1.6019164582145044e-08, 3.0606197217289763e-09, 4.873013733540374e-10, 6.650267407895671e-11, 7.941245733744225e-12, 9.657150810532185e-13, 1.0269744875621307e-13, 8.918801188037197e-15, 7.10010465649579e-16, 5.217481422276655e-17], [4.7898642740222916e-08, 4.575754555208721e-08, 2.1856078326757113e-08, 6.959699638049496e-09, 1.6621492541242134e-09, 3.175700431531789e-10, 5.056241292113997e-11, 6.900320522382827e-12, 8.239840227293908e-13, 8.746127307641899e-14, 9.572352490390607e-15, 9.254152216465413e-16, 7.367071858511403e-17, 5.413661124444748e-18], [4.518150340599048e-09, 4.316186392637169e-09, 2.0616251753052815e-09, 6.564897769788885e-10, 1.5678607553406466e-10, 2.9955529354314896e-11, 4.769416628361338e-12, 6.508887044572963e-13, 7.77242001017427e-14, 8.249987017014373e-15, 7.881207799196319e-16, 7.841569235085746e-17, 6.949161045600862e-18, 5.106561157892222e-19], [3.9066957269306485e-10, 3.732064155819161e-10, 1.782619358750669e-10, 5.676450788835485e-11, 1.3556775342937014e-11, 2.5901559201089206e-12, 4.123957406760567e-13, 5.6280201602888666e-14, 6.720555482364085e-15, 7.133491937395353e-16, 6.81462069898508e-17, 5.9181847185326504e-18, 5.39771758748766e-19, 4.415475172568624e-20], [3.118145602945591e-11, 2.9787626809936476e-11, 1.4228051283587363e-11, 4.530683038745548e-12, 1.0820397179718896e-12, 2.0673438265376579e-13, 3.291553925221686e-14, 4.49202792915779e-15, 5.3640395852250255e-16, 5.693626551180858e-17, 5.439118132953985e-18, 4.723623990038977e-19, 3.7603960420371115e-20, 3.165870328987059e-21]] |
| Legacy trial inputs | {"lambda_home": 1.0376004601243982, "lambda_away": 0.9552994184042356, "rho": -0.019671678951725675, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3214 |
| Legacy p draw | 0.3173 |
| Legacy p away | 0.3613 |
| Legacy p over 1 5 | 0.5939 |
| Legacy p under 3 5 | 0.8589 |
| Legacy p btts yes | 0.4009 |
| Legacy p over 2 5 | 0.3201 |
| Legacy goal margin distribution | {"-1": 0.22900584919285966, "-10": 2.9244193903183425e-08, "-11": 2.5207409996584365e-09, "-12": 1.9891548271682263e-10, "-13": 1.358165027466492e-11, "-2": 0.09609637602856769, "-3": 0.028364640236231465, "-4": 0.006463847771758843, "-5": 0.001196349926187481, "-6": 0.0001861606596185604, "-7": 2.4969563891625686e-05, "-8": 2.941616485290018e-06, "-9": 3.0886451094228474e-07, "0": 0.3172865265332612, "1": 0.19523244640493, "10": 5.23976217517739e-08, "11": 4.905584807464552e-09, "12": 4.204571995030013e-10, "13": 3.118145602945591e-11, "2": 0.08889018130387188, "3": 0.02849802111679579, "4": 0.00705373576203718, "5": 0.0014180023029179737, "6": 0.0002396609411510071, "7": 3.49149119280977e-05, "8": 4.4676247347829815e-06, "9": 5.09505983153449e-07} |
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
| Market p home draw | 60.1% |
| Market home draw odds | 1.61 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T08:59:13Z |
| Market reference home draw last update utc | 2026-11-01T08:59:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.2% |
| Market draw away odds | 1.35 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T08:59:13Z |
| Market reference draw away last update utc | 2026-11-01T08:59:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 68.7% |
| Market home away odds | 1.43 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T08:59:13Z |
| Market reference home away last update utc | 2026-11-01T08:59:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.60 |
| Market reference dc draw away odds | 1.35 |
| Market reference dc home away odds | 1.40 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:59:13Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 2.61, "price": 1.48, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:59:13Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 1.48, "price": 2.61, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:59:13Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.0, "price": 1.84, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:59:13Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.84, "price": 2.0, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:59:13Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.3, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:59:13Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.3, "price": 1.61, "quote_source": "The Odds API", "side": "Under"}] |
| Market p under 3 5 | 85.1% |
| Market reference under 3 5 odds | 1.14 |
| Market reference under 3 5 opposite odds | 4.70 |
| Market reference under 3 5 last update utc | 2026-11-01T08:59:19Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 44.4% |
| Market btts yes odds | 2.24 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T08:59:13Z |
| Market reference btts yes odds | 2.22 |
| Market reference btts yes opposite odds | 1.78 |
| Market reference btts yes last update utc | 2026-11-01T08:59:15Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 8.569662180849814, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,449.4205 |
| Elo away rating | 1,481.9065 |
| Elo rating diff | 27.5140 |
| Elo home expectancy | 0.5395 |

</details>


---

## 2026-11-01 — Real Racing Club de Santander vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **80.7%**. Expected goals are 1.19 for Real Racing Club de Santander and 3.48 for Real Madrid (4.67 combined). The most likely exact score is 1-3 at 7.9%. Goal-market probabilities: at least one goal: 99.0%; Over 2.5 goals: 84.6%; Under 3.5 goals: 31.3%; Double Chance 1X: 19.3%; Double Chance X2: 91.9%; Double Chance 12 (either team wins): 88.8%; Under 4.5 goals: 49.9%; BTTS Yes (both teams score): 67.3%; BTTS No (at least one team does not score): 32.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 8.1% | 12.32 |
| Draw | 11.2% | 8.94 |
| Real Madrid win | 80.7% | 1.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.19 |
| Real Madrid expected goals | 3.48 |
| Expected total goals | 4.67 |
| Over 0.5 | 99.0% |
| Under 0.5 | 1.0% |
| Over 1.5 | 94.8% |
| Under 1.5 | 5.2% |
| Over 2.5 | 84.6% |
| Under 2.5 | 15.4% |
| Over 3.5 | 68.7% |
| Under 3.5 | 31.3% |
| Over 4.5 | 50.1% |
| Under 4.5 | 49.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-3 | 7.91% |
| 2 | 1-4 | 6.89% |
| 3 | 1-2 | 6.81% |
| 4 | 0-3 | 6.66% |
| 5 | 0-4 | 5.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 8.1% | 7.9% | 11.04 | -10.4% |
| Draw | 11.2% | 11.1% | 8.00 | -10.5% |
| Real Madrid win | 80.7% | 81.0% | 1.22 | -1.5% |

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
| Market best home last update utc | 2026-11-01T08:59:15Z |
| Market best draw last update utc | 2026-11-01T08:59:15Z |
| Market best away last update utc | 2026-11-01T08:59:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santander |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1869 |
| Dc lambda away | 3.4829 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T08:58:27.598231+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 67.3% |
| P btts no | 32.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 98.45 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 19.37 |
| Fair Over 2.5 odds | 1.18 |
| Fair Under 2.5 odds | 6.49 |
| Fair Over 3.5 odds | 1.46 |
| Fair Under 3.5 odds | 3.20 |
| Fair Over 4.5 odds | 1.99 |
| Fair Under 4.5 odds | 2.01 |
| Goal margin distribution | {"-1": 0.167066001426709, "-10": 0.000991872615797386, "-11": 0.0003047467968542685, "-12": 8.621415984612078e-05, "-13": 2.2594320686786887e-05, "-14": 5.514167800051468e-06, "-15": 1.2589702652006998e-06, "-16": 2.7000089798288245e-07, "-17": 5.4587187600648865e-08, "-18": 1.0436776542030196e-08, "-19": 1.8908071425032074e-09, "-2": 0.19084174401203874, "-20": 3.2116953635811035e-10, "-21": 4.4505081597234006e-11, "-3": 0.17160797797618016, "-4": 0.1262500302550849, "-5": 0.07808819680773721, "-6": 0.041509807461443025, "-7": 0.0193025640669247, "-8": 0.007965558755306395, "-9": 0.002951730599079465, "0": 0.11185426731602645, "1": 0.052267263869301264, "10": 1.9466321457034087e-08, "11": 2.0382425297784708e-09, "12": 1.9650971658406558e-10, "13": 1.755065933829707e-11, "14": 1.4596974355717312e-12, "15": 1.1357612811848495e-13, "16": 8.300906346003772e-15, "17": 5.71925873407648e-16, "18": 3.7265257693041434e-17, "19": 2.300772601735425e-18, "2": 0.020586931254596978, "20": 1.3318322491786735e-19, "21": 6.289462075607202e-21, "3": 0.00630876616946346, "4": 0.0015817111157491418, "5": 0.0003334032195340164, "6": 6.039817735827525e-05, "7": 9.57143018363702e-06, "8": 1.346067373502299e-06, "9": 1.699871094317375e-07} |
| Raw goal margin distribution | {"-1": 0.1654661390118947, "-10": 0.0009823742157354562, "-11": 0.0003018284715088445, "-12": 8.538855324283401e-05, "-13": 2.2377952280609934e-05, "-14": 5.461362862260747e-06, "-15": 1.2469140766796197e-06, "-16": 2.6741530734828255e-07, "-17": 5.406444815021069e-08, "-18": 1.0336831571905707e-08, "-19": 1.872700338873981e-09, "-2": 0.18901419962350302, "-20": 3.1809394308590223e-10, "-21": 4.407889071035331e-11, "-3": 0.16996462055036168, "-4": 0.1250410309581041, "-5": 0.07734040629353058, "-6": 0.04111230000788207, "-7": 0.019117718278454876, "-8": 0.007889278734495572, "-9": 0.002923464148671862, "0": 0.11420186187269239, "1": 0.05573269207901767, "10": 2.0756979022069455e-08, "11": 2.173382245119236e-09, "12": 2.095387191550949e-10, "13": 1.8714304523974753e-11, "14": 1.5564784089077401e-12, "15": 1.2110646143220823e-13, "16": 8.85127368663189e-15, "17": 6.09845747318202e-16, "18": 3.9736021718010167e-17, "19": 2.4533186064035504e-18, "2": 0.02195188757791956, "20": 1.4201354949436507e-19, "21": 6.706466481180309e-21, "3": 0.006727050476574551, "4": 0.0016865818496342284, "5": 0.00035550854582529874, "6": 6.440270202894115e-05, "7": 1.0206035894941308e-05, "8": 1.4353144375915579e-06, "9": 1.8125760803265786e-07} |
| Unadjusted home-win probability | 8.7% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 79.9% |
| Raw p over 1 5 | 94.8% |
| Raw p under 3 5 | 31.4% |
| Raw p btts yes | 67.4% |
| P home draw | 19.3% |
| P draw away | 91.9% |
| P home away | 88.8% |
| Raw p home draw | 20.1% |
| Raw p draw away | 91.3% |
| Raw p home away | 88.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8459 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:56:51Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 9.46, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:56:51Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.08, "price": 9.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:50Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:50Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.68, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.77, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 11.04 |
| Reference draw odds | 8.00 |
| Reference away odds | 1.22 |
| Market reference 1x2 last update utc | 2026-11-01T08:59:15Z |
| Market reference home last update utc | 2026-11-01T08:59:15Z |
| Market reference draw last update utc | 2026-11-01T08:59:15Z |
| Market reference away last update utc | 2026-11-01T08:59:15Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.21 |
| Reference Under 2.5 odds | 4.51 |
| Market reference over 2 5 last update utc | 2026-11-01T08:58:51Z |
| Market reference under 2 5 last update utc | 2026-11-01T08:58:51Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Market p over 1 5 | 93.6% |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 7.60 |
| Market reference over 1 5 last update utc | 2026-11-01T08:59:19Z |
| Market over 1 5 bookmakers | 0 |
| Raw edge prob home | 0.0077 |
| Raw ev home | -0.0447 |
| Raw edge prob draw | 0.0034 |
| Raw ev draw | -0.0864 |
| Raw edge prob away | -0.0110 |
| Raw ev away | -0.0249 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.009085734203664455, 0.028641555497161058, 0.05358459843606725, 0.06530429652731677, 0.05969044188157835, 0.0436473437918769, 0.026596812935113068, 0.013891674174691187, 0.006348741308432692, 0.0025790998227210172, 0.0009429554639518796, 0.0003134162615271123, 9.54911909234036e-05, 2.685610258492826e-05, 7.0135513533534915e-06, 1.7095025460923285e-06, 3.906364810592923e-07, 8.401308015636465e-08, 1.706465184285625e-08, 3.2837256165890853e-09, 6.002883224997954e-10, 1.0451139148868924e-10, 1.7368566628854538e-11], [0.008933655493946436, 0.03634954093920632, 0.0623131591036705, 0.07594191499848865, 0.0694136022382064, 0.050757194371828254, 0.030929249904777287, 0.01615453186789645, 0.007382907380232048, 0.0029992173551363142, 0.0010965563906019519, 0.000364469603957527, 0.00011104604581684985, 3.1230776046139464e-05, 8.156010385796132e-06, 1.987968693464735e-06, 4.5426846344641886e-07, 9.769823015132022e-08, 1.9844365664162818e-08, 3.818621819914339e-09, 6.980711405840769e-10, 1.2153557469971132e-10, 2.0197786067909322e-11], [0.005596992508533139, 0.02046339820244313, 0.03789146534744101, 0.044156163991639255, 0.04036029910151276, 0.029512595231270655, 0.017983705453844805, 0.009392996718362898, 0.004292765978091255, 0.0017438845647045544, 0.0006375889231982554, 0.00021191959147509853, 6.456733952270617e-05, 1.8159026786550452e-05, 4.742284048537546e-06, 1.1558975256368058e-06, 2.641328279457958e-07, 5.680629823912744e-08, 1.1538437825728615e-08, 2.2203244585752836e-09, 4.058910518924182e-10, 7.066643983583214e-11, 1.1743932897931263e-11], [0.0021695679658300607, 0.007932248103666047, 0.014500711885751102, 0.017900357718252446, 0.015644904274654953, 0.011439997660288942, 0.006971042251727185, 0.0036410169840745228, 0.0016640092936827614, 0.0006759837684113813, 0.0002471492504287006, 8.21466093254902e-05, 2.5028304264078703e-05, 7.039002240343376e-06, 1.838256445919456e-06, 4.480617473724455e-07, 1.0238607991017089e-07, 2.2019883844600607e-08, 4.47265652835105e-09, 8.606666547667737e-10, 1.5733596613900905e-10, 2.739250479491167e-11, 4.552312794659624e-12], [0.000630743897438627, 0.002306089121500413, 0.004215694402988658, 0.005137725491958102, 0.00475668668315198, 0.003325873549289222, 0.002026644211342561, 0.0010585283703231476, 0.0004837662261804307, 0.0001965242128424946, 7.185203870983242e-05, 2.3881931031141723e-05, 7.27631050349005e-06, 2.046401761585179e-06, 5.344239283821248e-07, 1.3026197716868137e-07, 2.9766016139206915e-08, 6.401692676161659e-09, 1.3003053396011628e-09, 2.502158258109079e-10, 4.5741226849200114e-11, 7.963638617026947e-12, 1.3234632699624991e-12], [0.00014669754362965423, 0.0005363470195890321, 0.000980480375827802, 0.0011949250917438264, 0.0010922038906236297, 0.0008089605736932695, 0.0004713541087318089, 0.0002461910648985964, 0.0001125136800527859, 4.5707329717844e-05, 1.671124782390917e-05, 5.554426501196863e-06, 1.6923142370196374e-06, 4.7594929245138417e-07, 1.2429557839391754e-07, 3.029615055585538e-08, 6.922938880573441e-09, 1.4888968319447604e-09, 3.024232181438973e-10, 5.8194850830557904e-11, 1.0638431300934397e-11, 1.852172059398772e-12, 3.0780925757027987e-13], [2.8432259900260948e-05, 0.00010395237357337102, 0.00019003230853693954, 0.00023159502149247896, 0.0002116860590432534, 0.00015479084931786937, 9.554053608308249e-05, 4.7715647918346836e-05, 2.1806896792162436e-05, 8.858789627490131e-06, 3.238899095587915e-06, 1.0765340303012583e-06, 3.2799675461046824e-07, 9.2246357011172e-08, 2.4090411481400844e-08, 5.871864008549017e-09, 1.3417729612637936e-09, 2.885713055795928e-10, 5.861431163324837e-11, 1.127906495727354e-11, 2.061893036483633e-12, 3.5897968070804273e-13, 5.965820963600269e-14], [4.7233826417911165e-06, 1.7269356661478038e-05, 3.156960827846949e-05, 3.847432136172812e-05, 3.5166893532261766e-05, 2.5715029805612392e-05, 1.5669632512391644e-05, 8.289997745194158e-06, 3.6227270762421905e-06, 1.471689317013525e-06, 5.380704812167427e-07, 1.78841997430381e-07, 5.4489308367523994e-08, 1.5324664413011963e-08, 4.0020818543449586e-09, 9.754785806767292e-10, 2.229055001850169e-10, 4.7939653776207156e-11, 9.737453973065274e-12, 1.873763809901419e-12, 3.42537308392689e-13, 5.963642702198725e-14, 9.910874226091482e-15], [6.865986278142357e-07, 2.5103019353327703e-06, 4.589009904226314e-06, 5.592690293460812e-06, 5.111917173533122e-06, 3.7379787998798435e-06, 2.277763416025448e-06, 1.1896894300701513e-06, 5.507281264792324e-07, 2.139271666644368e-07, 7.821480538165106e-08, 2.599676531492978e-08, 7.920655003614509e-09, 2.2276182887647106e-09, 5.817491653717727e-10, 1.4179716227708477e-10, 3.240190815903132e-11, 6.9685864976104985e-12, 1.4154522390706957e-12, 2.7237337270614103e-13, 4.97917835063261e-14, 8.668848591422468e-15, 1.4406608907495785e-15], [8.871564422128355e-08, 3.2435697416400237e-07, 5.929475438762988e-07, 7.226334312580867e-07, 6.60512571514392e-07, 4.829855229576167e-07, 2.9431059231746887e-07, 1.5372017935416096e-07, 7.025284644117698e-08, 2.8907801031438554e-08, 1.0106161833100623e-08, 3.3590509639170237e-09, 1.0234305500102325e-09, 2.8783132322301017e-10, 7.51680092129668e-11, 1.8321659977982032e-11, 4.186661667936014e-12, 9.004134517648905e-13, 1.8289106934770868e-13, 3.519345691859838e-14, 6.433613426745059e-15, 1.1201049001409977e-15, 1.8614828787836835e-16], [1.0316680939470309e-08, 3.7719248305241155e-08, 6.895345998678746e-08, 8.403454218163452e-08, 7.681055034471865e-08, 5.6166052588293444e-08, 3.422517533065961e-08, 1.7876013393977753e-08, 8.16965494851635e-09, 3.318824095324813e-09, 1.2290735581467441e-09, 3.9062171456157125e-10, 1.1901403118740065e-10, 3.34717056066302e-11, 8.741235829512229e-12, 2.130613173510115e-12, 4.8686399122427e-13, 1.0470845787125499e-13, 2.1268276026182368e-14, 4.092622776660939e-15, 7.48160457991664e-16, 1.3025622453541978e-16, 2.1647055717474785e-17], [1.0906542679762962e-09, 3.9875866463581e-09, 7.289591087245907e-09, 8.883926199285902e-09, 8.12022345661266e-09, 5.937737662937601e-09, 3.6182018001360687e-09, 1.889808400291992e-09, 8.636759331582572e-10, 3.508579634735145e-10, 1.2827864622135144e-10, 4.3187227440976386e-11, 1.2581872195639215e-11, 3.5385468243618753e-12, 9.241020654588857e-13, 2.2524321191371811e-13, 5.1470069983572376e-14, 1.1069521984884014e-14, 2.248430106208626e-15, 4.3266206687704634e-16, 7.909369315841263e-17, 1.3770369371074913e-17, 2.2884737684440536e-18], [1.0569285906625937e-10, 3.864280788173511e-10, 7.064179236785298e-10, 8.60921363722735e-10, 7.869126437095172e-10, 5.754128401713858e-10, 3.5063182180054405e-10, 1.8313709374182327e-10, 8.369689769022175e-11, 3.400085836044874e-11, 1.243119591091034e-11, 4.131837714137759e-12, 1.2751334848172096e-12, 3.4291263674289094e-13, 8.955265865196059e-14, 2.1827814506792546e-14, 4.9878490486248704e-15, 1.0727225496032565e-15, 2.178903189704547e-16, 4.19283105567474e-17, 7.664792418163218e-18, 1.3344556125268723e-18, 2.217708604705572e-19], [9.454576552189398e-12, 3.4567272428534816e-11, 6.319142462661859e-11, 7.701226942521354e-11, 7.039194412531926e-11, 5.1472585703283404e-11, 3.136517859516543e-11, 1.6382220025310112e-11, 7.486964903625929e-12, 3.0414894728837286e-12, 1.1120116762219897e-12, 3.6960657810428607e-13, 1.1261117130404262e-13, 3.207980830335132e-14, 8.010782130004242e-15, 1.9525703538030353e-15, 4.461796291405581e-16, 9.595858749667867e-17, 1.9491011208199672e-17, 3.750626346612736e-18, 6.856410860144759e-19, 1.1937147746400375e-19, 1.9838138507061617e-20], [7.853329796638281e-13, 2.8712887251271076e-12, 5.248919347924959e-12, 6.3969311247864446e-12, 5.847021801464521e-12, 4.275508149754262e-12, 2.6053106691621566e-12, 1.3607693157877031e-12, 6.218956950580172e-13, 2.526376487800314e-13, 9.236790651466597e-14, 3.0700923905341256e-14, 9.353910903937644e-15, 2.6307095804044507e-15, 6.958866607933251e-16, 1.6218789762723948e-16, 3.706137188525004e-17, 7.970684147207824e-18, 1.6189972998052346e-18, 3.1154124652033737e-19, 5.695194851799059e-20, 9.915447568296513e-21, 1.6478310095365053e-21], [6.088388621535072e-14, 2.2260012066078032e-13, 4.0692880167774703e-13, 4.959297989696689e-13, 4.5329741558978805e-13, 3.314639247849644e-13, 2.0197985115155598e-13, 1.0549528204357812e-13, 4.821321365102568e-14, 1.9586038356139638e-14, 7.160933331230251e-15, 2.3801261454205948e-15, 7.251732219212932e-16, 2.0394893237202323e-16, 5.326187246006248e-17, 1.3149789848812955e-17, 2.8732275445916703e-18, 6.179368996891406e-19, 1.2551471787991951e-19, 2.4152610797845482e-20, 4.415268482416389e-21, 7.68707028935495e-22, 1.277500859949789e-22], [4.425090650247019e-15, 1.6178758845908255e-14, 2.95759181542917e-14, 3.604458343603986e-14, 3.294602694073367e-14, 2.409106917505394e-14, 1.4680060791580767e-14, 7.667483389036827e-15, 3.5041758042659914e-15, 1.423529288169532e-15, 5.204624918157697e-16, 1.7298951507884587e-16, 5.270618292635111e-17, 1.482317522529886e-17, 3.871116456068917e-18, 9.435567096411886e-19, 2.183944842213818e-19, 4.491215931232084e-20, 9.12251236056589e-21, 1.7554315084711874e-21, 3.2090532478107443e-22, 5.587025562872126e-23, 9.284980743592921e-24], [3.027004310334764e-16, 1.1067156954106056e-15, 2.023154751194795e-15, 2.4656468770650626e-15, 2.2536886459589042e-15, 1.6479610475186647e-15, 1.0041965420439649e-15, 5.244978488008844e-16, 2.397048128966991e-16, 9.737719815833405e-17, 3.560248434698082e-17, 1.1833430073509489e-17, 3.60539151645292e-18, 1.0139863529648235e-18, 2.6480556274421924e-19, 6.454444559163389e-20, 1.474897779794068e-20, 3.212969785554364e-21, 6.240297977844509e-22, 1.2008112743053343e-22, 2.1951681402672845e-23, 3.821831414870648e-24, 6.351435248148449e-25], [1.955601326402642e-17, 7.149955731831277e-17, 1.307062596986124e-16, 1.592935393836856e-16, 1.4559994150944536e-16, 1.0646680612195675e-16, 6.487628983167657e-17, 3.3885273480066695e-17, 1.5486170549722143e-17, 6.291070588490531e-18, 2.3001046075314333e-18, 7.645007794881136e-19, 2.329269372925474e-19, 6.55087622453001e-20, 1.7107808798730202e-20, 4.169904977669591e-21, 9.528602402798057e-22, 2.0492894961412852e-22, 4.216231513115391e-23, 7.757861833143715e-24, 1.4181921420220121e-24, 2.4691007405211654e-25, 4.1033556356138596e-26], [1.1969238230868617e-18, 4.376123207682515e-18, 7.999863466427028e-18, 9.749545041620757e-18, 8.911429762286203e-18, 6.516290150495778e-18, 3.970746787938806e-18, 2.0739447520580537e-18, 9.478295094760142e-19, 3.850443420355427e-19, 1.407776709484292e-19, 4.679119324494657e-20, 1.425626974783038e-20, 4.009457198342536e-21, 1.0470817152534088e-21, 2.5521861436667914e-22, 5.831971508022749e-23, 1.2542655730578879e-23, 2.5476515422214226e-24, 4.96569529317561e-25, 8.680030728058718e-26, 1.5112106225493106e-26, 2.5114546858579614e-27], [6.959472199084716e-20, 2.5444817135556097e-19, 4.651492961973739e-19, 5.668839266303069e-19, 5.181520033980157e-19, 3.788874385220909e-19, 2.3087769954311966e-19, 1.2058880077398387e-19, 5.511121922244268e-20, 2.238827018164177e-20, 8.185469019162371e-21, 2.7206577584058505e-21, 8.289258769768659e-22, 2.331285029762498e-22, 6.088220442202032e-23, 1.4839598119060308e-23, 3.390979675821277e-24, 7.2928838223415975e-25, 1.4813231835689339e-25, 2.85048820751003e-26, 5.278164167535985e-27, 8.786881931608266e-28, 1.4602766465465449e-28], [3.85386767196826e-21, 1.409028664426022e-20, 2.5758042908621827e-20, 3.139168569257723e-20, 2.869311347092994e-20, 2.0981218242774004e-20, 1.278505146646968e-20, 6.6777087056314056e-21, 3.0518312315704133e-21, 1.239769744258302e-21, 4.532773970560064e-22, 1.5065876666608278e-22, 4.590248438896302e-23, 1.2909691645189498e-23, 3.37140450752925e-24, 8.217555271442698e-25, 1.8777842018921686e-25, 4.038497230011059e-26, 8.202954714934019e-27, 1.578482396078027e-27, 2.885577725648656e-28, 5.088703222680906e-29, 8.086407703440624e-30], [2.0371073067535573e-22, 7.447953152635114e-22, 1.361538638144951e-21, 1.6593261040278618e-21, 1.5166828775749852e-21, 1.1090415298332531e-21, 6.758021804693704e-22, 3.529755132891239e-22, 1.6131606557304748e-22, 6.5532712061977e-23, 2.3959688710781164e-23, 7.96363810398325e-24, 2.4263491719512207e-24, 6.823905078432456e-25, 1.7820831800387451e-25, 4.3436991905219215e-26, 9.925737580468845e-27, 2.134700232547914e-27, 4.335981514961123e-28, 8.343664848747028e-29, 1.525281086291694e-29, 2.655544723507073e-30, 4.470175564368225e-31]] |
| Legacy trial inputs | {"lambda_home": 1.16289308723695, "lambda_away": 3.656141788870499, "rho": -0.019671678951725675, "max_goals": 22, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0770 |
| Legacy p draw | 0.1069 |
| Legacy p away | 0.8161 |
| Legacy p over 1 5 | 0.9533 |
| Legacy p under 3 5 | 0.2924 |
| Legacy p btts yes | 0.6717 |
| Legacy p over 2 5 | 0.8578 |
| Legacy goal margin distribution | {"-1": 0.15460457333702454, "-10": 0.0013795975209154171, "-11": 0.0004445970740801804, "-12": 0.0001319436282174332, "-13": 3.627711232262294e-05, "-14": 9.289033381769178e-06, "-15": 2.225311187453893e-06, "-16": 5.007814687482261e-07, "-17": 1.0624337769311635e-07, "-18": 2.131788068272788e-08, "-19": 4.057015509803654e-09, "-2": 0.1836230057552084, "-20": 7.33567830097438e-10, "-21": 1.2470917755659855e-10, "-22": 1.7368566628854538e-11, "-3": 0.1723820022136196, "-4": 0.13260525820577512, "-5": 0.0858479684976744, "-6": 0.04779784493671119, "-7": 0.02329128600985434, "-8": 0.010075471555102782, "-9": 0.0039147809083272846, "0": 0.10689715690873398, "1": 0.05029941884017904, "10": 1.50938914850966e-08, "11": 1.5471491300823117e-09, "12": 1.460396416362866e-10, "13": 1.2771202912335327e-11, "14": 1.0401270193043494e-12, "15": 7.925439680706523e-14, "16": 5.6728019594216796e-15, "17": 3.8279653789984727e-16, "18": 2.4430194136476463e-17, "19": 1.4787893634550724e-18, "2": 0.019179701212699192, "20": 8.504654727325232e-20, "21": 4.598662987231772e-21, "22": 2.0371073067535573e-22, "3": 0.005726950442408852, "4": 0.0014012286514397377, "5": 0.00028853270348489223, "6": 5.1096375841287136e-05, "7": 7.919395075099639e-06, "8": 1.0896340878035763e-06, "9": 1.3466028232324236e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0751 |
| Legacy raw p draw | 0.1029 |
| Legacy raw p away | 0.8220 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1629 |
| Legacy lambda away | 3.6561 |
| Legacy model home team | Santander |
| Legacy model away team | Real Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 22.2% |
| Market home draw odds | 4.74 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T08:56:51Z |
| Market reference home draw last update utc | 2026-11-01T08:59:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 91.0% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T08:56:51Z |
| Market reference draw away last update utc | 2026-11-01T08:59:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.9% |
| Market home away odds | 1.11 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T08:56:51Z |
| Market reference home away last update utc | 2026-11-01T08:59:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 4.35 |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home away odds | 1.11 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:56:51Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.09, "price": 1.75, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:56:51Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.09, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:56:51Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.71, "price": 2.15, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:56:51Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.15, "price": 1.71, "quote_source": "The Odds API", "side": "Under"}] |
| Market p under 3 5 | 38.1% |
| Market under 3 5 odds | 2.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T08:59:15Z |
| Market reference under 3 5 odds | 2.32 |
| Market reference under 3 5 opposite odds | 1.52 |
| Market reference under 3 5 last update utc | 2026-11-01T08:59:19Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.1% |
| Market btts yes odds | 1.52 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T08:56:51Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.66 |
| Market reference btts yes last update utc | 2026-11-01T08:59:15Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 10.724069412838478, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,438.0702 |
| Elo away rating | 1,670.4419 |
| Elo rating diff | -172.3717 |
| Elo home expectancy | 0.2705 |

</details>


---

## 2026-11-02 — Deportivo La Coruña vs CA Osasuna

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **46.1%**. Expected goals are 1.50 for Deportivo La Coruña and 0.98 for CA Osasuna (2.48 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 42.7%; Under 3.5 goals: 77.9%; Double Chance 1X: 74.5%; Double Chance X2: 53.9%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 90.5%; BTTS Yes (both teams score): 47.7%; BTTS No (at least one team does not score): 52.3%.

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
| CA Osasuna expected goals | 0.98 |
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
| Market best home last update utc | 2026-11-01T08:59:15Z |
| Market best draw last update utc | 2026-11-01T08:59:15Z |
| Market best away last update utc | 2026-11-01T08:59:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | La Coruna |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.5033 |
| Dc lambda away | 0.9751 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T08:58:27.598231+00:00 |
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
| Goal margin distribution | {"-1": 0.1653892816179654, "-10": 1.726346299883125e-08, "-11": 1.4709660346911686e-09, "-12": 1.1507207382570249e-10, "-13": 8.31884997456869e-12, "-14": 5.570360339263451e-13, "-15": 3.219986530364777e-14, "-2": 0.06615807603945179, "-3": 0.018847329320803283, "-4": 0.004185186356224307, "-5": 0.0007587991622323828, "-6": 0.00011603535935352038, "-7": 1.5326672698743242e-05, "-8": 1.780627465491504e-06, "-9": 1.8456261921648e-07, "0": 0.28393989859573143, "1": 0.2295435788256002, "10": 1.1702005603134428e-06, "11": 1.537172557261235e-07, "12": 1.8538624677284154e-08, "13": 2.06613387643376e-09, "14": 2.1328781769438278e-10, "15": 1.9007474212172305e-11, "2": 0.14054470746778003, "3": 0.06172612903746395, "4": 0.021131076313803242, "5": 0.005906378229549706, "6": 0.0013924267494915344, "7": 0.00028354205567447503, "8": 5.078439262891386e-05, "9": 8.115000183256904e-06} |
| Raw goal margin distribution | {"-1": 0.1551481134613533, "-10": 2.0511043357132835e-08, "-11": 1.7984473133153266e-09, "-12": 1.447904606735451e-10, "-13": 1.0772854810230342e-11, "-14": 7.421609918978464e-13, "-15": 4.3950944180458014e-14, "-2": 0.06330352450047196, "-3": 0.018467647250974897, "-4": 0.004207539160423448, "-5": 0.0007835394229379826, "-6": 0.00012314931683081302, "-7": 1.6725710565080818e-05, "-8": 1.9986350093095563e-06, "-9": 2.1311788440506846e-07, "0": 0.26626375414512826, "1": 0.24089725395881395, "10": 1.5554773648822204e-06, "11": 2.1026222544895425e-07, "12": 2.6097029803391535e-08, "13": 2.9934329353386217e-09, "14": 3.1792482746977283e-10, "15": 2.90256613442807e-11, "2": 0.15045377159712828, "3": 0.06766659970856152, "4": 0.023767228631994024, "5": 0.006823368463710706, "6": 0.001653322487363721, "7": 0.0003461766232050156, "8": 6.37726178362889e-05, "9": 1.0483546963533765e-05} |
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
| Totals anchor scale | 0.9712 |
| Totals anchor target over 2 5 | 0.4270 |
| Totals anchor reference over odds | 2.25 |
| Totals anchor reference under odds | 1.70 |
| Totals anchor reference last update utc | 2026-11-01T08:59:15Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4437 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:50Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.49, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:58:50Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.63, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.81, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.93, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:59:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.81, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.18 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.67 |
| Market reference 1x2 last update utc | 2026-11-01T08:59:15Z |
| Market reference home last update utc | 2026-11-01T08:59:15Z |
| Market reference draw last update utc | 2026-11-01T08:59:15Z |
| Market reference away last update utc | 2026-11-01T08:59:15Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.34 |
| Reference Under 2.5 odds | 1.71 |
| Market reference over 2 5 last update utc | 2026-11-01T08:59:16Z |
| Market reference under 2 5 last update utc | 2026-11-01T08:59:16Z |
| Home probability edge | +1.3% |
| Draw probability edge | -0.8% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Market p over 1 5 | 69.9% |
| Market over 1 5 odds | 1.39 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T08:59:15Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 2.80 |
| Market reference over 1 5 last update utc | 2026-11-01T08:59:20Z |
| Market over 1 5 bookmakers | 1 |
| Raw edge prob home | 0.0444 |
| Raw ev home | 0.0719 |
| Raw edge prob draw | -0.0253 |
| Raw ev draw | -0.1213 |
| Raw edge prob away | -0.0192 |
| Raw ev away | -0.1117 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09461735151980076, 0.08552750076505942, 0.042885654986444824, 0.01392721303665215, 0.003392170348621276, 0.0006609689759915625, 0.00010732558173778558, 1.493752472992812e-05, 1.8191230484271893e-06, 1.969214355657893e-07, 1.918520390192233e-08, 1.6992104107674875e-09, 1.3795560189261496e-10, 1.0338782860350825e-11, 7.194735036757569e-13, 4.673012811899913e-14], [0.12184628512416258, 0.13255638442774503, 0.06215952707707483, 0.02018644640343257, 0.004916695447506194, 0.0009580247514755257, 0.00015556034777133146, 2.1650817113739373e-05, 2.636681855995471e-06, 2.854227902075201e-07, 2.780750817021866e-08, 2.4628775186279383e-09, 1.999562551624453e-10, 1.4985287116521887e-11, 1.0428226582316803e-12, 6.773180134583974e-14], [0.09002893537489973, 0.08771129853272837, 0.04589331000282879, 0.014629366885042256, 0.003563189881273717, 0.0006942923630136155, 0.00011273650422813388, 1.569061441462951e-05, 1.9108358875850895e-06, 2.0684941925133655e-07, 2.0152444419923476e-08, 1.7848777388973174e-09, 1.4491076632651508e-10, 1.0860022548001214e-11, 7.557464527640751e-13, 4.908607249984313e-14], [0.0434967205073205, 0.04237697382208421, 0.02064302652444081, 0.007200720481328313, 0.0017215251267259364, 0.0003354414970988318, 5.446769080366854e-05, 7.580787964883052e-06, 9.232042364106309e-07, 9.993755161949195e-08, 9.736483485254125e-09, 8.623486196439015e-10, 7.001241406619352e-11, 5.246928262636179e-12, 3.651325220429386e-13, 2.371552176460606e-14], [0.01576130513217843, 0.015355558009845742, 0.0074801280673242035, 0.002429188435340288, 0.0006355138949217572, 0.00012154929677697495, 1.9736703930524746e-05, 2.7469453067561422e-06, 3.3452875296515343e-07, 3.6212988631465866e-08, 3.5280748832473254e-09, 3.1247734463642884e-10, 2.5369430344799908e-11, 1.9012568393550847e-12, 1.3230802291478644e-13, 8.59346568065669e-15], [0.00456896495316837, 0.004451344973969936, 0.0021683764572922575, 0.0007041851377556361, 0.00017151428199942728, 3.589666665703377e-05, 5.7213731853666835e-06, 7.962980685663861e-07, 9.697484664543465e-08, 1.0497599946139981e-08, 1.0227357670273504e-09, 9.058247552026358e-11, 7.35421572992644e-12, 5.511457200489089e-13, 3.8354102953471906e-14, 2.4911162617501376e-15], [0.0011037284332427813, 0.0010753148829771549, 0.0005238163948331606, 0.0001701105538725805, 4.143283909821061e-05, 8.073244683097421e-06, 1.4080585100136925e-06, 1.9236234653180148e-07, 2.3426289465779646e-08, 2.535913420243654e-09, 2.4706307825356907e-10, 2.1882079379029293e-11, 1.776563639362634e-12, 1.3314070217505342e-13, 9.265230614630169e-15, 6.017809015366663e-16], [0.00022853874849153167, 0.0002226554197465893, 0.00010846177348426074, 3.522320519823855e-05, 8.579111408896005e-06, 1.6716514502758588e-06, 2.714362865435908e-07, 4.057828630567219e-08, 4.850663184040655e-09, 5.250879309529238e-10, 5.1157046427303605e-11, 4.530918009408285e-12, 3.678564568302542e-13, 2.7568202949137412e-14, 1.9184648554643487e-15, 1.2460515645069332e-16], [4.1406213014323495e-05, 4.0340282773371806e-05, 1.9650896517301155e-05, 6.3816728984123864e-06, 1.5543469841112024e-06, 3.028666101161824e-07, 4.917830685004092e-08, 6.8446139573996075e-09, 8.953293231641579e-10, 9.513442627910768e-11, 9.268535753931719e-12, 8.209030524858488e-13, 6.66475287483785e-14, 4.994754243070435e-15, 3.475837904520318e-16, 2.257572374372082e-17], [6.668354150994962e-06, 6.4966890836181785e-06, 3.164721615970717e-06, 1.0277504718361784e-06, 2.503232101906768e-07, 4.877581574695995e-08, 7.920028004225642e-09, 1.1023058273644792e-09, 1.3424111244862023e-10, 1.5608704900911867e-11, 1.492671615416641e-12, 1.32204127813254e-13, 1.0733397058771494e-14, 8.043911231016645e-16, 5.597739187299204e-17, 3.635756814709896e-18], [9.66527713146296e-07, 9.41646154482524e-07, 4.5870256392612786e-07, 1.4896469064718674e-07, 3.628246407052852e-08, 7.0696871496724896e-09, 1.147948411503709e-09, 1.5977092793601244e-10, 1.945723824608512e-11, 2.1062606462368847e-12, 2.2041236283473607e-13, 1.916199266422878e-14, 1.5557250677751875e-15, 1.1659043522315466e-16, 8.11350137227256e-18, 5.269755684996568e-19], [1.2735537532633924e-07, 1.2407683483626503e-07, 6.044134730684524e-08, 1.9628463653657206e-08, 4.780790831568394e-09, 9.315435534232392e-10, 1.512604334193582e-10, 2.1052357026878647e-11, 2.563800133136069e-12, 2.7753328899736817e-13, 2.7038868184600343e-14, 2.5722884062514546e-15, 2.0499148365455528e-16, 1.5362641376283655e-17, 1.0690826537325971e-18, 6.94373998812866e-20], [1.5382668757013683e-08, 1.4986668963239462e-08, 7.300431744372027e-09, 2.3708316497799636e-09, 5.774496880884697e-10, 1.1251685198463356e-10, 1.8270050536697608e-11, 2.5428171670731805e-12, 3.0966960056583703e-13, 3.352196672304983e-14, 3.2659002557408477e-15, 2.8925685353424883e-16, 2.5224713865752755e-17, 1.855582639669624e-18, 1.2912956594174102e-19, 8.387023468660965e-21], [1.7150784504685792e-09, 1.670926767596093e-09, 8.139558461323804e-10, 2.6433399408490355e-10, 6.438229490047234e-11, 1.2544977155893143e-11, 2.0370047915239064e-12, 2.83509382904727e-13, 3.452636646378559e-14, 3.73750508784855e-15, 3.6412895827631107e-16, 3.225046342629863e-17, 2.618352656679663e-18, 2.107699169011533e-19, 1.439719852018942e-20, 9.351045284724167e-22], [1.7756264622235493e-10, 1.7299160771162851e-10, 8.426912128009928e-11, 2.7366586912345834e-11, 6.665520547630092e-12, 1.2987856852791744e-12, 2.1089178809971154e-13, 2.935182133719688e-14, 3.574526280169629e-15, 3.8694515314246365e-16, 3.76983929685937e-17, 3.3389012766770635e-18, 2.7107892722712023e-19, 2.031542125269847e-20, 1.5185239057563245e-21, 9.681168492596115e-23], [1.715757886753216e-11, 1.671588712986734e-11, 8.142782985168782e-12, 2.6443871122294188e-12, 6.440780024527543e-13, 1.2549946906791318e-13, 2.0378117604220127e-14, 2.836216964620035e-15, 3.4540044244032757e-16, 3.738985717827899e-17, 3.642732096523763e-18, 3.226323959699926e-19, 2.6193899292315023e-20, 1.9630448733784936e-21, 1.3660783788570948e-22, 9.530335631831512e-24]] |
| Legacy trial inputs | {"lambda_home": 1.4494246875026635, "lambda_away": 0.9742567560915809, "rho": -0.019671678951725675, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4629 |
| Legacy p draw | 0.2809 |
| Legacy p away | 0.2562 |
| Legacy p over 1 5 | 0.6980 |
| Legacy p under 3 5 | 0.7748 |
| Legacy p btts yes | 0.4818 |
| Legacy p over 2 5 | 0.4325 |
| Legacy goal margin distribution | {"-1": 0.16416538783352094, "-10": 2.17983739142786e-08, "-11": 1.9104004144656573e-09, "-12": 1.5372035098366555e-10, "-13": 1.1430691591082348e-11, "-14": 7.872053050215966e-13, "-15": 4.673012811899913e-14, "-2": 0.06699128973102875, "-3": 0.019595515046031253, "-4": 0.004470857670304185, "-5": 0.0008331804003933196, "-6": 0.00013099079275257137, "-7": 1.7791112455302292e-05, "-8": 2.1255865616401776e-06, "-9": 2.2658577410169469e-07, "0": 0.280940626541239, "1": 0.23280966456062976, "10": 1.0981761047410347e-06, "11": 1.4318401080062587e-07, "12": 1.7140509033002104e-08, "13": 1.896212841165376e-09, "14": 1.9427853335222227e-10, "15": 1.715757886753216e-11, "2": 0.140633377192963, "3": 0.06119965558874671, "4": 0.020773293998293838, "5": 0.005759380829263705, "6": 0.0013470997325433036, "7": 0.00027219761294590693, "8": 4.83818233339147e-05, "9": 7.672878185892814e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4784 |
| Legacy raw p draw | 0.2704 |
| Legacy raw p away | 0.2512 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4494 |
| Legacy lambda away | 0.9743 |
| Legacy model home team | La Coruna |
| Legacy model away team | Osasuna |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 95/100 |
| Market p home draw | 72.1% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T08:58:47Z |
| Market reference home draw last update utc | 2026-11-01T08:59:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.8% |
| Market draw away odds | 1.73 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T08:58:47Z |
| Market reference draw away last update utc | 2026-11-01T08:59:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.1% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T08:58:47Z |
| Market reference home away last update utc | 2026-11-01T08:59:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.69 |
| Market reference dc home away odds | 1.35 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:58:47Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.34, "price": 1.57, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:58:47Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.57, "price": 2.34, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:58:47Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.85, "price": 1.97, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:58:47Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.97, "price": 1.85, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:58:47Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.5, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:58:47Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.5, "price": 1.51, "quote_source": "The Odds API", "side": "Under"}] |
| Market p under 3 5 | 78.9% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 3.70 |
| Market reference under 3 5 last update utc | 2026-11-01T08:59:20Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 49.6% |
| Market btts yes odds | 1.94 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T08:58:47Z |
| Market reference btts yes odds | 1.97 |
| Market reference btts yes opposite odds | 1.94 |
| Market reference btts yes last update utc | 2026-11-01T08:59:16Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 9.68675382627685, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,438.5249 |
| Elo away rating | 1,412.0509 |
| Elo rating diff | 86.4740 |
| Elo home expectancy | 0.6219 |

</details>


---
