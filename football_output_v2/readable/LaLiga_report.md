# La Liga — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,999 |
| Training data through | 2026-10-26 |
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
| Training sha256 | fcacc610bde583b60a7e53f929b271b168c6c6a6ce31bb3421dd99c3274e9309 |
| Training as of utc | 2026-10-29T11:52:59.394319+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 99, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 99, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 89, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-10-29T11:52:59.394319+00:00', 'observations': 399, 'observations_sha256': 'bd790a5a2c6d3b70ab38e60cbc6daa2d0932d05780e915a529531d55eae59ed0', 'eligible_training_matches': 146, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 158, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 20, 'retrospective_eligible_training_matches': 146, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'ca8c6cbd50780303a93d4bb1797607cf82c3dc96bf1a279f54240aff4979a3b1', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 86, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-20T00:00:00+00:00', 'audit_origin_utc': '2026-09-18T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 16, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.817502522631521, 'audit_candidate_poisson_score': 0.809197371286247, 'audit_gain': 0.008305151345273987, 'audit_gain_lower95': -0.03007730499333999, 'audit_baseline_briers': [0.5521078342824518, 0.18074894030573588, 0.22581628123747038, 0.25215851249634236], 'audit_candidate_briers': [0.5295194447555117, 0.1898167447857306, 0.23341590827406827, 0.2546994560406538], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-29', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-10-30', 'audit_start_date': '2026-04-30', 'training_shot_matches': 1620, 'tuning_matches': 230, 'audit_matches': 133, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8308121235664122, 'audit_candidate_poisson_score': 0.8310522825824208, 'audit_gain': -0.0002401590160086009, 'audit_gain_lower95': -0.009001597025616807, 'audit_baseline_briers': [0.5655184868471271, 0.18297456599271653, 0.20296699475433386, 0.24773770838115103], 'audit_candidate_briers': [0.5703662010647587, 0.17993635768459515, 0.20503652253394755, 0.244872337454086], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1836.611 |
| Base scoring parameter | 0.091 |
| Home-advantage parameter | 0.288 |
| Dixon-Coles low-score adjustment | -0.033 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1999, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261029T115259394319Z_dc62af34df6d1b686d84cfba5f44da539d429b6614bb6534f923a9a87fbf6eb5.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 4} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 5} |
| Legacy comparison status | {'AVAILABLE': 5} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Villarreal vs Espanyol

The model's most likely 1X2 outcome is **Villarreal win** at **67.9%**. Expected goals are 2.16 for Villarreal and 0.95 for Espanyol (3.12 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 64.2%; Under 3.5 goals: 58.0%; Double Chance 1X: 86.4%; Double Chance X2: 32.1%; Double Chance 12 (either team wins): 81.5%; Under 4.5 goals: 76.2%; BTTS Yes (both teams score): 56.9%; BTTS No (at least one team does not score): 43.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 67.9% | 1.47 |
| Draw | 18.5% | 5.39 |
| Espanyol win | 13.6% | 7.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.16 |
| Espanyol expected goals | 0.95 |
| Expected total goals | 3.12 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 84.5% |
| Under 1.5 | 15.5% |
| Over 2.5 | 64.2% |
| Under 2.5 | 35.8% |
| Over 3.5 | 42.0% |
| Under 3.5 | 58.0% |
| Over 4.5 | 23.8% |
| Under 4.5 | 76.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.08% |
| 2 | 2-0 | 10.04% |
| 3 | 1-1 | 8.53% |
| 4 | 1-0 | 8.50% |
| 5 | 3-1 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 67.9% | 69.3% | 1.42 | -3.6% |
| Draw | 18.5% | 17.9% | 5.17 | -4.1% |
| Espanyol win | 13.6% | 12.9% | 7.08 | -4.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:00:00+00:00 |
| Fixture id | 00b03cb40c27ed23e2ecb18f062a5122 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:53:11Z |
| Market best draw last update utc | 2026-10-29T11:53:11Z |
| Market best away last update utc | 2026-10-29T11:53:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Villarreal |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1638 |
| Dc lambda away | 0.9515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:52:59.394319+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 56.9% |
| P btts no | 43.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.82 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.44 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.79 |
| Fair Over 3.5 odds | 2.38 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.20 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.08847776090377506, "-10": 1.1971196281627428e-08, "-11": 1.0746659331520712e-09, "-12": 8.86614829971827e-11, "-13": 6.765732205754344e-12, "-14": 4.80194720877364e-13, "-15": 3.1851458526688544e-14, "-16": 1.9822728218894836e-15, "-17": 1.1546846148960493e-16, "-18": 5.714789591385762e-18, "-2": 0.03446480344206714, "-3": 0.009839480232526222, "-4": 0.002232009850142342, "-5": 0.00041799663200610914, "-6": 6.648001728211244e-05, "-7": 9.174401754037824e-06, "-8": 1.1171163820831164e-06, "-9": 1.216317394039477e-07, "0": 0.1854594494169886, "1": 0.23267261407048687, "10": 5.038012470768643e-05, "11": 1.0284518990524356e-05, "12": 1.9294534694039843e-06, "13": 3.348134825800937e-07, "14": 5.403738588208292e-08, "15": 8.150703409493123e-09, "16": 1.1535010880727946e-09, "17": 1.5279416769798155e-10, "18": 1.7196198862007623e-11, "2": 0.20285558324227193, "3": 0.13169586309316314, "4": 0.0679336419724014, "5": 0.02893013029136502, "6": 0.010463031833716345, "7": 0.0032834695504887655, "8": 0.0009091645122238098, "9": 0.00022510222518514042} |
| Raw goal margin distribution | {"-1": 0.10045178498967902, "-10": 8.957992189701592e-09, "-11": 7.631505660382004e-10, "-12": 5.973451545446572e-11, "-13": 4.323856543150679e-12, "-14": 2.9104883675191186e-13, "-15": 1.830238651051934e-14, "-16": 1.073755130800191e-15, "-17": 5.360860609306238e-17, "-2": 0.037946842717160034, "-3": 0.010407612960761968, "-4": 0.0022576919877690463, "-5": 0.00040323400585831235, "-6": 6.105913305814008e-05, "-7": 8.013437646399021e-06, "-8": 9.272083718774659e-07, "-9": 9.587720198027623e-08, "0": 0.20093043518504441, "1": 0.2322148726299864, "10": 3.3120649015264574e-05, "11": 6.416337584451725e-06, "12": 1.1420658249287385e-06, "13": 1.879861628229469e-07, "14": 2.87745996847348e-08, "15": 4.1147169062678294e-09, "16": 5.489418054857569e-10, "17": 6.23224309738977e-11, "2": 0.1962245216361693, "3": 0.12238200977271611, "4": 0.06036983033699668, "5": 0.024518913964934726, "6": 0.008442742216386934, "7": 0.002519652061509468, "8": 0.000662960832866756, "9": 0.00015588872120263358} |
| Unadjusted home-win probability | 64.8% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 15.2% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 54.6% |
| P home draw | 86.4% |
| P draw away | 32.1% |
| P home away | 81.5% |
| Raw p home draw | 84.8% |
| Raw p draw away | 35.2% |
| Raw p home away | 79.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0555 |
| Totals anchor target over 2 5 | 0.6420 |
| Totals anchor reference over odds | 1.52 |
| Totals anchor reference under odds | 2.64 |
| Totals anchor reference last update utc | 2026-10-29T11:53:11Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6098 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:52:48Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.27, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:52:48Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.74, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:52:50Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.74, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:52:50Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.16, "price": 5.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.87, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.42 |
| Reference draw odds | 5.17 |
| Reference away odds | 7.08 |
| Market reference 1x2 last update utc | 2026-10-29T11:53:11Z |
| Market reference home last update utc | 2026-10-29T11:53:11Z |
| Market reference draw last update utc | 2026-10-29T11:53:11Z |
| Market reference away last update utc | 2026-10-29T11:53:11Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Market reference over 2 5 last update utc | 2026-10-29T11:52:51Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:52:51Z |
| Home probability edge | -1.3% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0450 |
| Raw ev home | -0.0805 |
| Raw edge prob draw | 0.0221 |
| Raw ev draw | 0.0388 |
| Raw edge prob away | 0.0229 |
| Raw ev away | 0.0729 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.04069538290328034, 0.034852169933267986, 0.017938944816708824, 0.005855795142067883, 0.0014336268282315655, 0.00028078658255787416, 4.582846769696179e-05, 6.411321160675214e-06, 7.84815878745624e-07, 8.539560264242866e-08, 8.362685100213759e-09, 7.44497586647293e-10, 6.075643517100604e-11, 4.5767708390735635e-12, 3.20141052087356e-13, 2.090067656424816e-14, 1.2792357794178106e-15, 7.369056940783405e-17], [0.09074614085102058, 0.08663060400291649, 0.03998165805427995, 0.013051180066511044, 0.0031952145574587042, 0.0006258067709535667, 0.00010214079720591416, 1.428931595148941e-05, 1.749168661823979e-06, 1.903265670904242e-07, 1.863844387218037e-08, 1.659308740603496e-09, 1.3541170009852646e-10, 1.020053791069139e-11, 7.135185600087269e-13, 4.65826564512608e-14, 2.851113486666421e-15, 1.642388210673889e-16], [0.10333748113140451, 0.10119710933708578, 0.046259000568404124, 0.014543994196861946, 0.0035606881327652448, 0.0006973875158201491, 0.00011382381932171094, 1.5923749976361033e-05, 1.9492412745249587e-06, 2.1209641374688195e-07, 2.0770337864780926e-08, 1.8491030367486906e-09, 1.5090029946592126e-10, 1.13672911891427e-11, 7.951319147567622e-13, 5.1910852631632206e-14, 3.177228250116118e-15, 1.8302471104761305e-16], [0.07677158786838889, 0.07518146065143444, 0.03681213442773228, 0.011218321409717557, 0.0026453100933330367, 0.0005181038512156382, 8.456210903244787e-05, 1.1830088725986358e-05, 1.4481323344198036e-06, 1.5757088605472575e-07, 1.543072078962799e-08, 1.3737375317184431e-09, 1.1210700583153177e-10, 8.444999672898168e-12, 5.907202207017779e-13, 3.8565664079470224e-14, 2.3604296825422514e-15, 1.3597290675598006e-16], [0.042776420321822065, 0.041890416110026675, 0.020511381605440002, 0.006695513587307653, 0.0015303192396994483, 0.0002886826849009395, 4.711722682449771e-05, 6.591616271566128e-06, 8.068859735577969e-07, 8.779704366560643e-08, 8.597855231252715e-09, 7.65433875998372e-10, 6.246498914014451e-11, 4.705475888356443e-12, 3.2914385588399884e-13, 2.1488432146039882e-14, 1.3152096373677794e-15, 7.57628489037501e-17], [0.01906770133436442, 0.018672762637661808, 0.009143002043305315, 0.002984542708400318, 0.0007306813836480335, 0.0001336029883182041, 2.100262719586906e-05, 2.938230207936343e-06, 3.596715349002488e-07, 3.913576204042281e-08, 3.832516475951965e-09, 3.411941539039049e-10, 2.7843932423933566e-11, 2.0974781947675606e-12, 1.4671673536075464e-13, 9.578524879404665e-15, 5.862581386833154e-16, 3.377148822339213e-17], [0.00708289815279078, 0.006936194021218344, 0.003396264245380165, 0.001108639770760204, 0.0002714192828892333, 5.315950523664921e-05, 8.100052129509612e-06, 1.091436505498427e-06, 1.3360377349550682e-07, 1.4537390312727482e-08, 1.4236285429507033e-09, 1.2674015603934542e-10, 1.0342921470900212e-11, 7.791303299083951e-13, 5.449947403976482e-14, 3.5580437822636615e-15, 2.1777174997255781e-16, 1.2544774399385299e-17], [0.0022551574232297796, 0.002208447601318292, 0.0010813526269894402, 0.00035298505707476977, 8.641846845901392e-05, 1.6925706153549007e-05, 2.7625222353575577e-06, 3.607994578748661e-07, 4.25387369788998e-08, 4.628628418893555e-09, 4.532758211823334e-10, 4.0353397373194325e-11, 3.2931316573841846e-12, 2.480709886339496e-13, 1.7352345154711524e-14, 1.132862378458299e-15, 6.933737686554874e-17, 3.994190019288891e-18], [0.0006282764529589423, 0.0006152633120905485, 0.00030125985258703435, 9.834000825043493e-05, 2.407578658336588e-05, 4.7154236402474e-06, 7.696259486687776e-07, 1.076693020402249e-07, 1.2304388773813436e-08, 1.2895145213067e-09, 1.2628055239559725e-10, 1.12422703201638e-11, 9.174512854472809e-13, 6.911143284965944e-14, 4.834283297486069e-15, 3.156102316835423e-16, 1.9317073276496366e-17, 1.1127629104352524e-18], [0.00015558659641491508, 0.0001523640177445769, 7.460409327729303e-05, 2.4352953390248604e-05, 5.962136051536164e-06, 1.1677291284517807e-06, 1.905904340390749e-07, 2.6663262905864146e-08, 3.263875195652741e-09, 3.3155010392853254e-10, 3.127215933064786e-11, 2.784039680069006e-12, 2.2719795116777888e-13, 1.711477894769862e-14, 1.1971635747591555e-15, 7.81578260813383e-17, 4.783686655186469e-18, 2.755649890044343e-19], [3.467656631563044e-05, 3.395832987660384e-05, 1.6627484934811076e-05, 5.427696361236543e-06, 1.3288188760332403e-06, 2.6025915788700754e-07, 4.2478092440919336e-08, 5.942609618380037e-09, 7.274404561570815e-10, 7.915259849138668e-11, 7.236412428357523e-12, 6.204964875882116e-13, 5.063704073476085e-14, 3.814478758662104e-15, 2.6681939863306525e-16, 1.7419527784819034e-17, 1.0661704244072529e-18, 6.141690759784627e-20], [7.025986458228243e-06, 6.8804611069441865e-06, 3.368974970676902e-06, 1.0997317550507694e-06, 2.692384056560786e-07, 5.273236404954465e-08, 8.606691318417545e-09, 1.2040608151694377e-09, 1.4739022161554838e-10, 1.6037489988833956e-11, 1.5705314375030064e-12, 1.3053052446775512e-13, 1.0259815209178201e-14, 7.728699508370562e-16, 5.406156608832154e-17, 3.529454595096465e-18, 2.1602193527080273e-19, 1.244397606040418e-20], [1.3049382732052524e-06, 1.2779098122565685e-06, 6.257205883962746e-07, 2.0425346190986257e-07, 5.000571837793956e-08, 9.793995546953574e-09, 1.5985229937233069e-09, 2.236305250974727e-10, 2.737482379532435e-11, 2.9786471432871147e-12, 2.91695208104137e-13, 2.596849885744938e-14, 1.978443869389466e-15, 1.4354533488694826e-16, 1.0040868583719977e-17, 6.555265103432832e-19, 4.0121809636653386e-20, 2.3112228764765163e-21], [2.2372294277711575e-07, 2.190890938462209e-07, 1.0727561162597943e-07, 3.501789050806732e-08, 8.573146102702037e-09, 1.6791150587747211e-09, 2.7405608034948985e-10, 3.8339958446240516e-11, 4.693230525342772e-12, 5.106691389731553e-13, 5.000919330134185e-14, 4.4521255167285095e-15, 3.633259263450709e-16, 2.5551192341987412e-17, 1.7214397904588042e-18, 1.123856376763235e-19, 6.878616027873592e-21, 3.962437104929534e-22], [3.5616102636731275e-08, 3.4878406104238045e-08, 1.7077994534943258e-08, 5.574755842987765e-09, 1.3648222561497675e-09, 2.673106903111894e-10, 4.362900543317062e-11, 6.103620299996299e-12, 7.471499257676774e-13, 8.129718052743006e-14, 7.961331722581448e-15, 7.087666440780987e-16, 5.784052955258708e-17, 4.357116217035447e-18, 2.845307720755232e-19, 1.7891497209395115e-20, 1.0950575359250557e-21, 6.30809540000375e-23], [5.291990327552904e-09, 5.1823802740767735e-09, 2.537520256349293e-09, 8.283206700200549e-10, 2.0279103112547553e-10, 3.971814664862871e-11, 6.482581126520523e-12, 9.069015753937189e-13, 1.1101467840888096e-13, 1.207947701062574e-14, 1.182928151911003e-15, 1.0531152897917594e-16, 8.594189152441211e-18, 6.473986531248287e-19, 4.5284960339695214e-20, 2.7600748938605204e-21, 1.6270825439088975e-22, 9.37283345754771e-24], [7.371620441747798e-10, 7.218936165924614e-10, 3.5347071773094734e-10, 1.15383158424358e-10, 2.824832280332101e-11, 5.532646199653152e-12, 9.030085958158704e-13, 1.2632929725926048e-13, 1.5464088595025566e-14, 1.6826432806109677e-15, 1.6477916258358693e-16, 1.466965303645197e-17, 1.1971507224140798e-18, 9.018113885219058e-20, 6.308090504356621e-21, 4.1182896885584997e-22, 2.3531794323455185e-23, 1.305614077807773e-24], [9.66446796650919e-11, 9.464293214655993e-11, 4.6341322855735636e-11, 1.5127160266575944e-11, 3.703459951548699e-12, 7.253504489156665e-13, 1.1838777805651298e-13, 1.656223968992448e-14, 2.0273994034132586e-15, 2.2060077852666782e-16, 2.16031597248068e-17, 1.923245953463386e-18, 1.569509024410788e-19, 1.1823081973733166e-20, 8.270140750049363e-22, 5.399230615086033e-23, 3.304624595722765e-24, 1.7771796988518047e-25]] |
| Legacy trial inputs | {"lambda_home": 2.2287630885089715, "lambda_away": 0.9792875559682256, "rho": -0.0218549380431621, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6736 |
| Legacy p draw | 0.1865 |
| Legacy p away | 0.1400 |
| Legacy p over 1 5 | 0.8337 |
| Legacy p under 3 5 | 0.5980 |
| Legacy p btts yes | 0.5560 |
| Legacy p over 2 5 | 0.6258 |
| Legacy goal margin distribution | {"-1": 0.0923339528864998, "-10": 1.0181678084102778e-08, "-11": 8.918893853907232e-10, "-12": 7.179201964165924e-11, "-13": 5.344636444245368e-12, "-14": 3.700369096954889e-13, "-15": 2.3934814761962193e-14, "-16": 1.4434746004851995e-15, "-17": 7.369056940783405e-17, "-2": 0.03511911068575111, "-3": 0.009839925614325123, "-4": 0.0021859349938852047, "-5": 0.0004003910217383246, "-6": 6.223354545432202e-05, "-7": 8.388811031647253e-06, "-8": 9.973511393518116e-07, "-9": 1.0600011237830689e-07, "0": 0.18647570460723137, "1": 0.23623761262819304, "10": 4.2219171361452606e-05, "11": 8.416955080018882e-06, "12": 1.541962655929689e-06, "13": 2.6125795575607896e-07, "14": 4.116708078880557e-08, "15": 6.0602252670011e-09, "16": 8.318049763213398e-10, "17": 9.66446796650919e-11, "2": 0.20230400811870777, "3": 0.1290049763680436, "4": 0.06522371948769745, "5": 0.02718981922112963, "6": 0.009618341748948786, "7": 0.00295073183763248, "8": 0.0007984194167784094, "9": 0.00019312700179183653} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6546 |
| Legacy raw p draw | 0.1941 |
| Legacy raw p away | 0.1513 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2288 |
| Legacy lambda away | 0.9793 |
| Legacy model home team | Villarreal |
| Legacy model away team | Espanol |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 86.2% |
| Market home draw odds | 1.13 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-29T11:52:50Z |
| Market reference home draw last update utc | 2026-10-29T11:52:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 32.0% |
| Market draw away odds | 3.04 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-29T11:52:50Z |
| Market reference draw away last update utc | 2026-10-29T11:52:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.8% |
| Market home away odds | 1.19 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-29T11:52:50Z |
| Market reference home away last update utc | 2026-10-29T11:52:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.04 |
| Market reference dc home draw odds | 1.13 |
| Market reference dc home away odds | 1.19 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:52:50Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.06, "price": 1.75, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:52:50Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.06, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:52:50Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.22, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:52:50Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.22, "price": 1.65, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 84.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-29T11:52:50Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 58.6% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-29T11:53:11Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.31 |
| Market reference under 3 5 last update utc | 2026-10-29T11:53:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.0% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-29T11:52:50Z |
| Market reference btts yes odds | 1.77 |
| Market reference btts yes opposite odds | 2.24 |
| Market reference btts yes last update utc | 2026-10-29T11:53:11Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 10.16398044941085, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,563.5990 |
| Elo away rating | 1,432.0064 |
| Elo rating diff | 191.5927 |
| Elo home expectancy | 0.7508 |

</details>


---

## 2026-10-31 — Barcelona vs Alavés

The model's most likely 1X2 outcome is **Barcelona win** at **88.1%**. Expected goals are 2.93 for Barcelona and 0.72 for Alavés (3.65 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 72.9%; Under 3.5 goals: 48.8%; Double Chance 1X: 96.1%; Double Chance X2: 11.9%; Double Chance 12 (either team wins): 92.1%; Under 4.5 goals: 68.1%; BTTS Yes (both teams score): 47.2%; BTTS No (at least one team does not score): 52.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 88.1% | 1.13 |
| Draw | 7.9% | 12.64 |
| Alavés win | 3.9% | 25.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.93 |
| Alavés expected goals | 0.72 |
| Expected total goals | 3.65 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 89.1% |
| Under 1.5 | 10.9% |
| Over 2.5 | 72.9% |
| Under 2.5 | 27.1% |
| Over 3.5 | 51.2% |
| Under 3.5 | 48.8% |
| Over 4.5 | 31.9% |
| Under 4.5 | 68.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.01% |
| 2 | 3-0 | 11.72% |
| 3 | 2-1 | 8.68% |
| 4 | 4-0 | 8.58% |
| 5 | 3-1 | 8.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 88.1% | 90.9% | 1.09 | -3.9% |
| Draw | 7.9% | 6.1% | 12.54 | -0.8% |
| Alavés win | 3.9% | 3.0% | 23.90 | -5.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:00:00+00:00 |
| Fixture id | 2db2b55e71574a19ff0557898d3e9933 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:53:11Z |
| Market best draw last update utc | 2026-10-29T11:53:11Z |
| Market best away last update utc | 2026-10-29T11:53:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.9276 |
| Dc lambda away | 0.7228 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:52:59.394319+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 47.2% |
| P btts no | 52.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.26 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.17 |
| Fair Over 2.5 odds | 1.37 |
| Fair Under 2.5 odds | 3.70 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.14 |
| Fair Under 4.5 odds | 1.47 |
| Goal margin distribution | {"-1": 0.028968917996143276, "-10": 2.1605929926289593e-10, "-11": 1.3976798907064384e-11, "-12": 8.307778548221767e-13, "-13": 4.566824992513614e-14, "-14": 2.3346050587083716e-15, "-15": 1.115276905178817e-16, "-16": 4.99992865273602e-18, "-17": 2.1114550168727406e-19, "-18": 8.425827323737144e-21, "-19": 3.172669381470759e-22, "-2": 0.008347173528731872, "-20": 1.036951465276349e-23, "-3": 0.0017331586936393305, "-4": 0.0002849503170247818, "-5": 3.8598344422655597e-05, "-6": 4.434569584287479e-06, "-7": 4.4170282369625e-07, "-8": 3.879568187310936e-08, "-9": 3.0456284034053213e-09, "0": 0.07913974580105577, "1": 0.203584181383654, "10": 0.00043235995714826397, "11": 0.0001132786335621761, "12": 2.727049238001808e-05, "13": 6.071419204525749e-06, "14": 1.2570630359944263e-06, "15": 2.4321711124778115e-07, "16": 4.4161417707220456e-08, "17": 7.553162293226825e-09, "18": 1.2207516514308019e-09, "19": 1.861690001214276e-10, "2": 0.23071173226043784, "20": 2.464386162110989e-11, "3": 0.19401546584007207, "4": 0.1291917997624027, "5": 0.07087650013221755, "6": 0.03298016650072361, "7": 0.013304523608847702, "8": 0.00473282368094368, "9": 0.0015048098764632832} |
| Raw goal margin distribution | {"-1": 0.04524415516133234, "-10": 3.3744513554840513e-10, "-11": 2.1829205305291368e-11, "-12": 1.2975231651101912e-12, "-13": 7.132545944016433e-14, "-14": 3.646226397917088e-15, "-15": 1.7418586828986432e-16, "-16": 7.808974701440245e-18, "-17": 3.297706818469444e-19, "-18": 1.315960226227676e-20, "-19": 4.955129694177114e-22, "-2": 0.013036759410302794, "-20": 1.6195286615806685e-23, "-3": 0.002706877104097212, "-4": 0.00044504031384453045, "-5": 6.028355923620184e-05, "-6": 6.925987169142437e-06, "-7": 6.898590790713119e-07, "-8": 6.059176426576697e-08, "-9": 4.756714906154815e-09, "0": 0.12144804515957942, "1": 0.18870333117119728, "10": 0.00040075689390209324, "11": 0.00010499860725141941, "12": 2.5277173893439564e-05, "13": 5.6276328595084984e-06, "14": 1.1651788502039918e-06, "15": 2.2543931841050697e-07, "16": 4.093346827812181e-08, "17": 7.00106892353583e-09, "18": 1.1315216221225939e-09, "19": 1.7256110099006497e-10, "2": 0.2138480117754255, "20": 2.2842534961308354e-11, "3": 0.17983403452038932, "4": 0.11974861116161892, "5": 0.0656958295374668, "6": 0.030569503185216333, "7": 0.012332038312466747, "8": 0.004386881084620988, "9": 0.0013948168002935967} |
| Unadjusted home-win probability | 81.7% |
| Unadjusted draw probability | 12.1% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 88.1% |
| Raw p under 3 5 | 50.5% |
| Raw p btts yes | 48.9% |
| P home draw | 96.1% |
| P draw away | 11.9% |
| P home away | 92.1% |
| Raw p home draw | 93.8% |
| Raw p draw away | 18.3% |
| Raw p home away | 87.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7295 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:52:48Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.86, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 2.75, "market_key": "spreads", "opposite_price": 1.89, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -2.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:52:48Z", "line": -2.5, "market_key": "spreads", "opposite_price": 2.09, "price": 1.86, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.09 |
| Reference draw odds | 12.54 |
| Reference away odds | 23.90 |
| Market reference 1x2 last update utc | 2026-10-29T11:53:11Z |
| Market reference home last update utc | 2026-10-29T11:53:11Z |
| Market reference draw last update utc | 2026-10-29T11:53:11Z |
| Market reference away last update utc | 2026-10-29T11:53:11Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.66 |
| Market reference over 2 5 last update utc | 2026-10-29T11:52:51Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:52:51Z |
| Home probability edge | -2.8% |
| Draw probability edge | +1.8% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | -0.0920 |
| Raw ev home | -0.1094 |
| Raw edge prob draw | 0.0604 |
| Raw ev draw | 0.5230 |
| Raw edge prob away | 0.0316 |
| Raw ev away | 0.4699 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.02671844937981116, 0.015748791870353326, 0.005409835066347104, 0.0011657696600087823, 0.0001884094732366737, 2.4360304319502344e-05, 2.624710673798068e-06, 2.424004243294727e-07, 1.9588147567641324e-08, 1.4070218315392649e-09, 9.096007597618045e-11, 5.345743390324446e-12, 2.879896234452447e-13, 1.4321333757117097e-14, 6.613104854459562e-16, 2.8501264468276474e-17, 1.1515800267538816e-18, 4.3792040405192896e-20, 1.5727969345999687e-21, 5.351419926733456e-23], [0.09979127731302816, 0.04590868437043173, 0.014607936285391513, 0.003147875805454025, 0.0005087536952330658, 6.577904298888763e-05, 7.08738913852298e-06, 6.545430518176189e-07, 5.289300100791499e-08, 3.799318281464535e-09, 2.456154352357406e-10, 1.4434872391893721e-11, 7.776455323586579e-13, 3.867125863913912e-14, 1.7857072013803304e-15, 7.69606929415697e-17, 3.109560171805581e-18, 1.1824969304994034e-19, 4.246953396678894e-21, 1.4450200489916585e-22], [0.13666180905251385, 0.08834808569288395, 0.019606515972805615, 0.004250034302011332, 0.0006868824533259142, 8.881010761983616e-05, 9.568880353613793e-06, 8.8371670113168e-07, 7.141230547611636e-08, 5.129564829878688e-09, 3.3161220116966465e-10, 1.9488920974713046e-11, 1.0499207693022277e-12, 5.221113724802372e-14, 2.4109327458426957e-15, 1.0390676288483889e-16, 4.198303303911902e-18, 1.596521853860341e-19, 5.7339293957073676e-21, 1.9509615864349065e-22], [0.12300726207003461, 0.07952079813340178, 0.025704000029579142, 0.0038028810184360076, 0.0006182526818088748, 7.993665719925738e-05, 8.612806910242828e-06, 7.954202611938236e-07, 6.427715420736582e-08, 4.617045023102698e-09, 2.984792109639328e-10, 1.7541687955246815e-11, 9.45018071381632e-13, 4.699446822026437e-14, 2.170044712251272e-15, 9.35249321053036e-17, 3.778830372100098e-18, 1.4370055792461652e-19, 5.161024581474888e-21, 1.7560315117660493e-22], [0.0830377555379352, 0.05368161590185902, 0.017351841142420048, 0.003739162044876202, 0.00041490395509315864, 5.3962347322651796e-05, 5.814194566016664e-06, 5.369594614773846e-07, 4.339118299134665e-08, 3.1168001749177893e-09, 2.0149252439313207e-10, 1.1841759353372116e-11, 6.37947534720678e-13, 3.1724266502962906e-14, 1.4649187315437933e-15, 6.313530045437912e-17, 2.550951768027466e-18, 9.700705144396556e-20, 3.484021108264194e-21, 1.1854333877289183e-22], [0.04484462935758733, 0.028990814513711917, 0.009370880506856616, 0.0020193384915591513, 0.00032636164289807706, 2.8970926598843686e-05, 3.1399620406021286e-06, 2.899855357844101e-07, 2.3433455131686884e-08, 1.6832312930471482e-09, 1.0881625492161412e-10, 6.395154899160467e-12, 3.445242535615716e-13, 1.7132724310169503e-14, 7.911309395285458e-16, 3.409628704334497e-17, 1.3776442511625043e-18, 5.238876266458894e-20, 1.8815493538085993e-21, 6.40194578435186e-23], [0.020181992006642634, 0.013047100514898125, 0.004217295096287499, 0.0009087882736276269, 0.00014687663077160316, 1.8990337171236192e-05, 1.4048006668045457e-06, 1.3050583423436758e-07, 1.0546052245957676e-08, 7.57525728013642e-10, 4.897194643998629e-11, 2.8780919121201522e-12, 1.5505057865525068e-13, 7.710455187904258e-15, 3.560425969954277e-16, 1.534478046585873e-17, 6.199985519616008e-19, 2.3577173108149332e-20, 8.467772966941467e-22, 2.881148099507896e-23], [0.007785218950554984, 0.005032929065919194, 0.0016268248294268293, 0.00035056577604228897, 5.665777337045793e-05, 7.325537180585336e-06, 7.892929159260905e-07, 5.004646932951901e-08, 4.0681477711293034e-09, 2.922161326455625e-10, 1.8890966032721605e-11, 1.1102261703553352e-12, 5.981088005802755e-14, 2.9743140234383166e-15, 1.373437058354443e-16, 5.9192608755166386e-18, 2.3916491862941073e-19, 9.094912673717507e-21, 3.2664499396061633e-22, 1.1114050969924914e-23], [0.0026277599271229053, 0.00169877422837694, 0.0005491053138475487, 0.00011832714069512461, 1.912380722603662e-05, 2.472602655114639e-06, 2.6641155610462503e-07, 2.4603959168036113e-08, 1.3650491536943746e-09, 9.863227332483708e-11, 6.376304101490563e-12, 3.747367747820252e-13, 2.0188081391241446e-14, 1.0039259333758037e-15, 4.63578852090228e-17, 1.997939508915192e-18, 8.07257950148177e-20, 3.0698233686765354e-21, 1.1025311310786223e-22, 3.751347001575109e-24], [0.0007884025445824849, 0.0005096804736610494, 0.00016474717580276246, 3.550149991036173e-05, 5.737684833187956e-06, 7.418509601705379e-07, 7.993102664025895e-08, 7.381885922935744e-09, 5.965231751798481e-10, 2.941833511435469e-11, 1.9130721671941265e-12, 1.124316661264634e-13, 6.0569972830507485e-15, 3.0120626784670885e-16, 1.390868103399115e-17, 5.994385470651648e-19, 2.422002921431627e-20, 9.210341212308763e-22, 3.30790625221044e-23, 1.1255105503081062e-24], [0.00021288882188192225, 0.00013762674450953495, 4.448594490977648e-05, 9.586311641041831e-06, 1.5493214384715394e-06, 2.0031870521969803e-07, 2.1583418534333463e-08, 1.9932977236048476e-09, 1.6107649177686665e-10, 1.1570167096974577e-11, 5.135383844839397e-13, 3.035942122251766e-14, 1.6355439547871346e-15, 8.133338476132707e-17, 3.7556990900199e-18, 1.6186371664096376e-19, 6.540026438032476e-21, 2.4870273482657256e-22, 8.93219168009989e-24, 3.039165927573921e-25], [5.225947166399503e-05, 3.3784305306988364e-05, 1.0920310220646313e-05, 2.3532263325930514e-06, 3.8032396016138055e-07, 4.9173787550965513e-08, 5.298249289635084e-09, 4.893102652538986e-10, 3.9540696798152074e-11, 2.8402187311055585e-12, 1.836122978189361e-13, 7.408705981278404e-15, 4.0148967054655237e-16, 1.996553731049751e-17, 9.219406093676799e-19, 3.973394299640148e-20, 1.6054310569190063e-21, 6.105099088122204e-23, 2.192654428152437e-24, 7.46047651869294e-26], [1.1759493327328294e-05, 7.60218770255322e-06, 2.45730220920929e-06, 5.295260069551523e-07, 8.558098521348366e-08, 1.106514873137224e-08, 1.1922188492179393e-09, 1.1010522334099281e-10, 8.897498297445183e-12, 6.391096609497447e-13, 4.1316674705397e-14, 2.428189932189587e-15, 8.981206613421015e-17, 4.492670807865783e-18, 2.0745625814509844e-19, 8.94098280477921e-21, 3.612561551082745e-22, 1.3737772255151582e-23, 4.933939111129603e-25, 1.6787659929731548e-26], [2.442587324287603e-06, 1.5790652541090722e-06, 5.104110407724687e-07, 1.0998888102291583e-07, 1.7776193570917457e-08, 2.298363652266933e-09, 2.4763810547083386e-10, 2.2870170966087614e-11, 1.8481167474030755e-12, 1.32750715801483e-13, 8.581967190932152e-15, 5.043640728589598e-16, 2.7171453774766038e-17, 9.27689844901078e-19, 4.309114452335688e-20, 1.857148999342889e-21, 7.503722147940749e-23, 2.8534995037925567e-24, 1.0248381283269179e-25, 3.486997628845071e-27], [4.711149701964575e-07, 3.045628185861592e-07, 9.844572591958279e-08, 2.121414775627954e-08, 3.4285901761206243e-09, 4.4329777395130034e-10, 4.776329489568015e-11, 4.411093026620329e-12, 3.5645622889912935e-13, 2.560434539903891e-14, 1.655250224702681e-15, 9.727941465610215e-17, 5.240704603683633e-18, 2.606131389524988e-19, 8.262311242305107e-21, 3.581983279680637e-22, 1.4472832970754257e-23, 5.503698149571453e-25, 1.9766604840780702e-26, 6.725560096270419e-28], [8.480871577194465e-08, 5.4826492788808725e-08, 1.772190678847471e-08, 3.818907785197519e-09, 6.17204606391177e-10, 7.980114683618323e-11, 8.598206292298737e-12, 7.94071847435137e-13, 6.416819017497828e-14, 4.609218107775846e-15, 2.97973222501756e-16, 1.751195090359824e-17, 9.434160561554345e-19, 4.691480217374544e-20, 2.1663660051705986e-21, 6.410233543859198e-23, 2.605356347134724e-24, 9.90759372106008e-26, 3.5583254147476066e-27, 1.210715325759817e-28], [1.4312824481345285e-08, 9.252845784437099e-09, 2.9908546430567395e-09, 6.445016451723806e-10, 1.0416312898912037e-10, 1.3467717293912788e-11, 1.4510845541748091e-12, 1.3401229902453574e-13, 1.0829406328115532e-14, 7.778791268368408e-16, 5.0287737468833585e-17, 2.955421236222197e-18, 1.5921651803979557e-19, 7.917621708781805e-21, 3.6560884234751273e-22, 1.5757068029338593e-23, 4.371079514328066e-25, 1.6720645828824346e-26, 6.005242108104243e-28, 2.0432753634747906e-29], [2.2734283189052633e-09, 1.4697086283856468e-09, 4.750630214264592e-10, 1.023717082275156e-10, 1.654512060413321e-11, 2.1391927167763095e-12, 2.304881697450228e-13, 2.1286319557755353e-14, 1.7201272226427563e-15, 1.235571943148676e-16, 7.987631414353368e-18, 4.694348303843674e-19, 2.5289721216167675e-20, 1.2576235693090658e-21, 5.807277920010385e-23, 2.5028298731326356e-24, 1.0112564989776355e-25, 2.6402538448856462e-27, 9.538639622277622e-29, 3.2455090053674866e-30], [3.410465037255591e-10, 2.2047714679984996e-10, 7.126619351025415e-11, 1.5357208705933315e-11, 2.4820028363482687e-12, 3.2090925884263276e-13, 3.45764956774601e-14, 3.19324994854169e-15, 2.5804348893127103e-16, 1.853533220326754e-17, 1.1982580423848317e-18, 7.042188499995583e-20, 3.793816998426988e-21, 1.886613788299469e-22, 8.711740829092358e-24, 3.75459991658237e-25, 1.5170282277127027e-26, 5.7689226888624395e-28, 1.4225105408402018e-29, 4.8687239878466685e-31], [4.846908732627069e-11, 3.133392650255181e-11, 1.0128259105212884e-11, 2.1825466079389167e-12, 3.5273902797672956e-13, 4.560720816879815e-14, 4.913966776143314e-15, 4.538205462297408e-16, 3.6672806383758904e-17, 2.6342174025174837e-18, 1.7029488078990085e-19, 1.0008267073425647e-20, 5.391723573997369e-22, 2.681231077202811e-23, 1.2381013216570046e-24, 5.335988765288176e-26, 2.1559808660168402e-27, 8.198718196213625e-29, 2.9445805053478813e-30, 6.878648396824175e-32]] |
| Legacy trial inputs | {"lambda_home": 2.7002553878699422, "lambda_away": 0.6464723854118982, "rho": -0.0218549380431621, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8568 |
| Legacy p draw | 0.0965 |
| Legacy p away | 0.0467 |
| Legacy p over 1 5 | 0.8577 |
| Legacy p under 3 5 | 0.5574 |
| Legacy p btts yes | 0.4317 |
| Legacy p over 2 5 | 0.6698 |
| Legacy goal margin distribution | {"-1": 0.035282252123486416, "-10": 1.064933632498201e-10, "-11": 6.177834641495654e-12, "-12": 3.2916794396075387e-13, "-13": 1.6214825469166646e-14, "-14": 7.426167302899285e-16, "-15": 3.1775756393388333e-17, "-16": 1.275739252350706e-18, "-17": 4.823408996051528e-20, "-18": 1.7172989394991345e-21, "-19": 5.351419926733456e-23, "-2": 0.009330645007186871, "-3": 0.0017725074394861061, "-4": 0.000264597941357319, "-5": 3.2398915868715e-05, "-6": 3.355491121866054e-06, "-7": 3.0073366351165853e-07, "-8": 2.373727518053331e-08, "-9": 1.6731037368055913e-09, "0": 0.09648186186530118, "1": 0.21792869156559128, "10": 0.00024924392814309733, "11": 6.039391546111877e-05, "12": 1.3440929552494167e-05, "13": 2.765533422251239e-06, "14": 5.290372169465949e-07, "15": 9.455233452554213e-08, "16": 1.5855981849849124e-08, "17": 2.5040337248103263e-09, "18": 3.723804302281109e-10, "19": 4.846908732627069e-11, "2": 0.23570826294524758, "3": 0.18702775909291627, "4": 0.11661631866392383, "5": 0.059642825256374356, "6": 0.025801127596995897, "7": 0.009658718307598773, "8": 0.003184367499943511, "9": 0.0009374973535449236} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.8046 |
| Legacy raw p draw | 0.1320 |
| Legacy raw p away | 0.0635 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.7003 |
| Legacy lambda away | 0.6465 |
| Legacy model home team | Barcelona |
| Legacy model away team | Alaves |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 10.265784456508303, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,725.4846 |
| Elo away rating | 1,438.3571 |
| Elo rating diff | 347.1275 |
| Elo home expectancy | 0.8806 |

</details>


---

## 2026-10-31 — Levante vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **59.2%**. Expected goals are 1.22 for Levante and 1.87 for Atlético Madrid (3.09 combined). The most likely exact score is 1-2 at 11.0%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 60.9%; Under 3.5 goals: 62.1%; Double Chance 1X: 40.8%; Double Chance X2: 79.7%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 79.3%; BTTS Yes (both teams score): 59.1%; BTTS No (at least one team does not score): 40.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 20.3% | 4.94 |
| Draw | 20.6% | 4.86 |
| Atlético Madrid win | 59.2% | 1.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.22 |
| Atlético Madrid expected goals | 1.87 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 60.9% |
| Under 2.5 | 39.1% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.7% |
| Under 4.5 | 79.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.00% |
| 2 | 1-1 | 9.48% |
| 3 | 0-1 | 9.25% |
| 4 | 0-2 | 9.00% |
| 5 | 1-3 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 20.3% | 18.4% | 5.09 | +3.1% |
| Draw | 20.6% | 19.4% | 4.84 | -0.4% |
| Atlético Madrid win | 59.2% | 62.2% | 1.58 | -6.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T13:00:00+00:00 |
| Fixture id | 005711684f3e51024ac40c1ee69978e9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:53:11Z |
| Market best draw last update utc | 2026-10-29T11:53:11Z |
| Market best away last update utc | 2026-10-29T11:53:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Levante |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2217 |
| Dc lambda away | 1.8697 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:52:59.394319+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.1% |
| P btts no | 40.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.17 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.60 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.84 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.2532697896973912, "-10": 9.105396905555638e-06, "-11": 1.5217462710838662e-06, "-12": 2.337256517426147e-07, "-13": 3.320306534137326e-08, "-14": 4.385277536400475e-09, "-15": 5.370413958047073e-10, "-16": 5.4917760302832414e-11, "-2": 0.1814239231874984, "-3": 0.09647530503218886, "-4": 0.040755332911068365, "-5": 0.014212071576522203, "-6": 0.004208637590988747, "-7": 0.0010813682247918293, "-8": 0.00024514639054913206, "-9": 4.969296995463254e-05, "0": 0.2057032391387343, "1": 0.11959754921989826, "10": 9.408654381764716e-08, "11": 1.0274194212843278e-08, "12": 1.0310715293045655e-09, "13": 9.570562998079434e-11, "14": 8.2591105894169e-12, "15": 6.608773242264258e-13, "16": 4.415732900310786e-14, "2": 0.05642974161782448, "3": 0.019606792775873225, "4": 0.005411924562001032, "5": 0.0012331092797977115, "6": 0.0002385956935205456, "7": 4.005636774819495e-05, "8": 5.9333553016678975e-06, "9": 7.858627375006304e-07} |
| Raw goal margin distribution | {"-1": 0.22344506132834746, "-10": 8.03315694466256e-06, "-11": 1.3425473653007933e-06, "-12": 2.062024162061933e-07, "-13": 2.9293114588820988e-08, "-14": 3.868872830168901e-09, "-15": 4.738000839532429e-10, "-16": 4.845071468469842e-11, "-2": 0.16005967269722704, "-3": 0.08511449579258883, "-4": 0.03595603673320652, "-5": 0.012538476100182024, "-6": 0.0037130337801080243, "-7": 0.0009540276777417219, "-8": 0.00021627826333382085, "-9": 4.384118900389709e-05, "0": 0.23265305619892343, "1": 0.14482713003100842, "10": 1.1393447612034729e-07, "11": 1.244157652839028e-08, "12": 1.2485801876366412e-09, "13": 1.1589511497800798e-10, "14": 1.000140296415831e-11, "15": 8.002920360374831e-13, "16": 5.347249396889072e-14, "2": 0.06833382105409522, "3": 0.023742924042878172, "4": 0.0065535916694898855, "5": 0.00149323860875565, "6": 0.0002889284082803723, "7": 4.850641855353778e-05, "8": 7.18502030685308e-06, "9": 9.516436215700647e-07} |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 52.2% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 60.0% |
| P home draw | 40.8% |
| P draw away | 79.7% |
| P home away | 79.4% |
| Raw p home draw | 47.8% |
| Raw p draw away | 75.5% |
| Raw p home away | 76.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6085 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:52:48Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.59, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:52:48Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.6, "price": 1.59, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.09 |
| Reference draw odds | 4.84 |
| Reference away odds | 1.58 |
| Market reference 1x2 last update utc | 2026-10-29T11:53:11Z |
| Market reference home last update utc | 2026-10-29T11:53:11Z |
| Market reference draw last update utc | 2026-10-29T11:53:11Z |
| Market reference away last update utc | 2026-10-29T11:53:11Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Market reference over 2 5 last update utc | 2026-10-29T11:52:51Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:52:51Z |
| Home probability edge | +1.8% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | 0.0610 |
| Raw ev home | 0.2486 |
| Raw edge prob draw | 0.0385 |
| Raw ev draw | 0.1260 |
| Raw edge prob away | -0.0995 |
| Raw ev away | -0.1752 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.036681381202627164, 0.0771823789626676, 0.08321324096557503, 0.058218459415619005, 0.03054852488677482, 0.012823594195040294, 0.004485884034460172, 0.001345053406883893, 0.0003528897697283471, 8.229739441593683e-05, 1.727331177545715e-05, 3.295888061160877e-06, 5.764753394429699e-07, 9.307368477206849e-08, 1.3953668422123257e-08, 1.952480324780188e-09, 2.5612749972770507e-10, 3.1622544699467045e-11], [0.03922650937575786, 0.09073466923537281, 0.10133213825230329, 0.07089497909088978, 0.037200177655755645, 0.015615810714557204, 0.0054626429146266454, 0.0016379260824545432, 0.0004297281841087012, 0.00010021687476648107, 2.103441227135801e-05, 4.013536557431235e-06, 7.019973999047188e-07, 1.133396005676098e-07, 1.6991947931247385e-08, 2.377614474688918e-09, 3.118968437169948e-10, 3.850805513874496e-11], [0.025032105750214837, 0.05253961806304087, 0.05673725461382657, 0.04316584559904452, 0.022650082495781723, 0.00950800300461759, 0.00332604090782205, 0.0009972845085014794, 0.00026164871874794935, 6.1019076358604904e-05, 1.2807228438674631e-05, 2.4437231178541983e-06, 4.274253517497932e-07, 6.900911405991954e-08, 1.0345892053750276e-08, 1.447658785213799e-09, 1.8990471781445507e-10, 2.344641022190752e-11], [0.01016087011791953, 0.02132654122312804, 0.022381024226442222, 0.016112766160959763, 0.009193974677812536, 0.0038594269525199193, 0.0013500849672216238, 0.00040481126368722617, 0.00010620675201067147, 2.4768467973968893e-05, 5.198627156438145e-06, 9.91940248752775e-07, 1.7349772838022007e-07, 2.8011732289422718e-08, 4.199537444478481e-09, 5.87624270942381e-10, 7.708489216798218e-11, 9.517214866920195e-12], [0.003093325904643799, 0.006492548537315953, 0.006813570216788638, 0.004766976463585679, 0.002573916287591351, 0.0011749451799660223, 0.00041101330438341675, 0.00012323877324707728, 3.2333067289512595e-05, 7.540391985436169e-06, 1.5826447799224e-06, 3.019814673070573e-07, 5.2818805020339755e-08, 8.527755607465651e-09, 1.2784867647916317e-09, 1.7889347648463753e-10, 2.3467349846286222e-11, 2.8973746289686095e-12], [0.0007533736808988628, 0.0015812479320815337, 0.00165943215571914, 0.001160988113065743, 0.0006091963720998695, 0.0002631471712046112, 0.00010010151389379569, 3.0014570430884525e-05, 7.874657462403944e-06, 1.8364482245340635e-06, 3.854501465932044e-07, 7.354701593091752e-08, 1.286392018995323e-08, 2.076918769586328e-09, 3.113730365512397e-10, 4.356916827473596e-11, 5.7154287261153804e-12, 7.056501178528136e-13], [0.00015290228074013723, 0.00032092495578346273, 0.00033679297243334596, 0.00023563038489497138, 0.00012364052139643566, 5.190155263888027e-05, 1.8682737049920067e-05, 6.091659943365901e-06, 1.5982149583621346e-06, 3.727195800859544e-07, 7.82297125848668e-08, 1.4926864002006672e-08, 2.610819552331824e-09, 4.2152470259228623e-10, 6.319526240001214e-11, 8.842657193983233e-12, 1.1599848916782856e-12, 1.4321646104694005e-13], [2.659932974825801e-05, 5.582904768985977e-05, 5.858949446199412e-05, 4.0990953674408045e-05, 2.1508868166981086e-05, 9.02894650364591e-06, 3.158459816543883e-06, 9.745154250415665e-07, 2.7803016724336874e-07, 6.483939262611726e-08, 1.3609070519313004e-08, 2.5967210938571207e-09, 4.541858358784037e-10, 7.332967505137656e-11, 1.0993633417165637e-11, 1.5382946115323907e-12, 2.0179437800006997e-13, 2.4914356112453422e-14], [4.048885321904693e-06, 8.498161941174252e-06, 8.918350439282023e-06, 6.23954333563819e-06, 3.274027632887107e-06, 1.374364291012586e-06, 4.807730763166247e-07, 1.4415563560495502e-07, 3.89182263921417e-08, 9.869694746811968e-09, 2.0715396362203782e-09, 3.9526657331231975e-10, 6.913506399256224e-11, 1.116206490109035e-11, 1.673424157617278e-12, 2.341554667860183e-13, 3.071664973741974e-14, 3.79240273056224e-15], [5.478324288648305e-07, 1.149839604479107e-06, 1.2066930016978649e-06, 8.442383295168315e-07, 4.429906919298358e-07, 1.859576816407148e-07, 6.505076365251348e-08, 1.950490708165207e-08, 5.117330013358468e-09, 1.2280394474573095e-09, 2.8028864741136046e-10, 5.348134849245402e-11, 9.354285689907813e-12, 1.510277678853741e-12, 2.2642182919552098e-13, 3.168228979155614e-14, 4.1561011227467455e-15, 5.131291785118217e-16], [6.671177660751318e-08, 1.4002063183340323e-07, 1.469439005827452e-07, 1.0280632520957105e-07, 5.394477311331744e-08, 2.264482104823939e-08, 7.921495304552995e-09, 2.3751916378475803e-09, 6.231580291540656e-10, 1.4532663315297694e-10, 3.13874919207716e-11, 6.512640700533384e-12, 1.1391093049403259e-12, 1.839126379133421e-13, 2.7572304399093975e-14, 3.85808091603552e-15, 5.06105288862565e-16, 6.248582107234762e-17], [7.385239625774878e-09, 1.5500800176945438e-08, 1.62672315524482e-08, 1.1381039230673332e-08, 5.971885269130119e-09, 2.5068651777623926e-09, 8.769387354613758e-10, 2.629424712497546e-10, 6.89858913082833e-11, 1.6088194085374436e-11, 3.3767337874177445e-12, 6.630030709049521e-13, 1.2610359976512352e-13, 2.0359807072585655e-14, 3.052355751520833e-15, 4.271037815134794e-16, 5.602772140385646e-17, 6.917410767630624e-18], [7.494421501731564e-10, 1.572996084442629e-09, 1.6507722985023988e-09, 1.154929419280141e-09, 6.060172402618128e-10, 2.54392616112214e-10, 8.899032188212114e-11, 2.6682975910153135e-11, 7.000576465149823e-12, 1.6326038664562634e-12, 3.4266547308397945e-13, 6.538335302406951e-14, 1.1767855968490959e-14, 2.066080230672038e-15, 3.0974811562368995e-16, 4.334179966854677e-17, 5.685602380681467e-18, 7.01967635719078e-19], [7.020200769478242e-11, 1.473462403981283e-10, 1.5463172117424083e-10, 1.0818495324889603e-10, 5.6767059277625366e-11, 2.3829554275375665e-11, 8.335932613459775e-12, 2.499457069143318e-12, 6.557604516383439e-13, 1.5292984144141527e-13, 3.209828026435364e-14, 6.124612354730632e-15, 1.0712402607831198e-15, 1.7797333390967955e-16, 2.901483402212503e-17, 4.059928245474364e-18, 5.325837384324505e-19, 6.575495834181869e-20], [6.106273701818866e-12, 1.2816392327649083e-11, 1.3450094142299456e-11, 9.410086073725428e-12, 4.937682162932205e-12, 2.07272961808194e-12, 7.250716577652343e-13, 2.1740644564599025e-13, 5.703900688911049e-14, 1.3302062144391456e-14, 2.791955544975125e-15, 5.327277749394927e-16, 9.317805070745451e-17, 1.5043877727018343e-17, 2.320829098509898e-18, 3.5313851969014625e-19, 4.6324915523009374e-20, 5.719462819817393e-21], [4.9572380851832e-13, 1.0404693805707898e-12, 1.0919150072104672e-12, 7.63936229318197e-13, 4.0085438789496573e-13, 1.6826979439166669e-13, 5.886327753847809e-14, 1.764964305480756e-14, 4.630580794429528e-15, 1.079897369389275e-15, 2.2665849969297134e-16, 4.32482810945459e-17, 7.564446079980623e-18, 1.2213026676973344e-18, 1.83098504263983e-19, 2.6363613691472594e-20, 3.760781889864401e-21, 4.643214553049381e-22], [3.7728936612772506e-14, 7.918886007193917e-14, 8.310432419357214e-14, 5.814225800107308e-14, 3.050854030401481e-14, 1.2806809552728665e-14, 4.480012516863414e-15, 1.3432928832755186e-15, 3.524278767153403e-16, 8.218967638404646e-17, 1.7250702953368842e-17, 3.2915741144339015e-18, 5.757207980697123e-19, 9.295186178829622e-20, 1.3935404639767217e-20, 1.949924747664015e-21, 2.63214172858252e-22, 3.5338941673008e-23], [2.7025915422024197e-15, 5.672440378153208e-15, 5.952912110699733e-15, 4.164834443413804e-15, 2.1853815769262703e-15, 9.173747867594147e-16, 3.209113487957992e-16, 9.622248361519195e-17, 2.5245042250270934e-17, 5.887394244148433e-18, 1.235698858340947e-18, 2.357813699734639e-19, 4.123991554552573e-20, 6.6583089282186226e-21, 9.982180813400793e-22, 1.3967661439956764e-22, 1.832285916664467e-23, 2.3278539221333112e-24]] |
| Legacy trial inputs | {"lambda_home": 1.2177405551866918, "lambda_away": 2.098889265941598, "rho": -0.0218549380431621, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1991 |
| Legacy p draw | 0.2031 |
| Legacy p away | 0.5978 |
| Legacy p over 1 5 | 0.8469 |
| Legacy p under 3 5 | 0.5743 |
| Legacy p btts yes | 0.6166 |
| Legacy p over 2 5 | 0.6479 |
| Legacy goal margin distribution | {"-1": 0.23215576403242258, "-10": 2.1743608657759913e-05, "-11": 4.071278864691666e-06, "-12": 7.007726293352364e-07, "-13": 1.1159327375532663e-07, "-14": 1.6530704829493548e-08, "-15": 2.2878235787190904e-09, "-16": 2.9463555486645e-10, "-17": 3.1622544699467045e-11, "-2": 0.1810604225601125, "-3": 0.1064082252073818, "-4": 0.04992943818546239, "-5": 0.019397669604753358, "-6": 0.006411886181287333, "-7": 0.0018413145726518443, "-8": 0.0004669607736708323, "-9": 0.00010595787571041724, "0": 0.2031228321023855, "1": 0.11957853393511736, "10": 8.397664456440224e-08, "11": 9.122691499574271e-09, "12": 9.11033846857993e-10, "13": 8.417064266921997e-11, "14": 7.234012241026642e-12, "15": 5.808655807009589e-13, "16": 4.3401376990925715e-14, "17": 2.7025915422024197e-15, "2": 0.05446637568867584, "3": 0.018571431924914013, "4": 0.005055825939741733, "5": 0.0011395942142839398, "6": 0.00021855046038500226, "7": 3.6413225852278e-05, "8": 5.357680456071372e-06, "9": 7.053341216906733e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2139 |
| Legacy raw p draw | 0.2121 |
| Legacy raw p away | 0.5740 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2177 |
| Legacy lambda away | 2.0989 |
| Legacy model home team | Levante |
| Legacy model away team | Ath Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 9.763905865240275, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,476.0819 |
| Elo away rating | 1,586.5836 |
| Elo rating diff | -50.5017 |
| Elo home expectancy | 0.4278 |

</details>


---

## 2026-10-31 — Rayo Vallecano vs Celta Vigo

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **38.9%**. Expected goals are 1.17 for Rayo Vallecano and 1.10 for Celta Vigo (2.27 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 39.8%; Under 3.5 goals: 80.4%; Double Chance 1X: 68.1%; Double Chance X2: 61.1%; Double Chance 12 (either team wins): 70.9%; Under 4.5 goals: 91.9%; BTTS Yes (both teams score): 46.4%; BTTS No (at least one team does not score): 53.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 38.9% | 2.57 |
| Draw | 29.1% | 3.43 |
| Celta Vigo win | 31.9% | 3.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.17 |
| Celta Vigo expected goals | 1.10 |
| Expected total goals | 2.27 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 66.8% |
| Under 1.5 | 33.2% |
| Over 2.5 | 39.8% |
| Under 2.5 | 60.2% |
| Over 3.5 | 19.6% |
| Under 3.5 | 80.4% |
| Over 4.5 | 8.1% |
| Under 4.5 | 91.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.60% |
| 2 | 1-0 | 12.22% |
| 3 | 0-0 | 10.63% |
| 4 | 0-1 | 10.39% |
| 5 | 2-1 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 38.9% | 39.7% | 2.45 | -4.6% |
| Draw | 29.1% | 29.0% | 3.32 | -3.2% |
| Celta Vigo win | 31.9% | 31.3% | 3.09 | -1.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:15:00+00:00 |
| Fixture id | 77383723574e3d39c7aba22eec6c4ce3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:53:11Z |
| Market best draw last update utc | 2026-10-29T11:53:11Z |
| Market best away last update utc | 2026-10-29T11:53:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Vallecano |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1743 |
| Dc lambda away | 1.0992 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:52:59.394319+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.4% |
| P btts no | 53.6% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.41 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.01 |
| Fair Over 2.5 odds | 2.51 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.11 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.35 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.19031459967926367, "-10": 7.838468318365392e-08, "-11": 7.756633859746478e-09, "-12": 7.018374083618137e-10, "-13": 5.398438117244359e-11, "-2": 0.08940402916169582, "-3": 0.02974553753852221, "-4": 0.007697433318110641, "-5": 0.0016244002526508096, "-6": 0.0002889163814179826, "-7": 4.436466831137975e-05, "-8": 5.9900068474125315e-06, "-9": 7.21374845500148e-07, "0": 0.2914285990879207, "1": 0.22353990620656009, "10": 1.6666759083767833e-07, "11": 1.761966318244534e-08, "12": 1.703198175318238e-09, "13": 1.3995910541569302e-10, "2": 0.11203201873987309, "3": 0.039820916542277936, "4": 0.011008793504733246, "5": 0.0024819395443669177, "6": 0.0004716009563743091, "7": 7.73649250701508e-05, "8": 1.115934101410977e-05, "9": 1.4357425939203903e-06} |
| Raw goal margin distribution | {"-1": 0.19938775921792393, "-10": 8.2121636297662e-08, "-11": 8.126427751602696e-09, "-12": 7.352971785896275e-10, "-13": 5.6558061298923093e-11, "-2": 0.09366632444198521, "-3": 0.031163642130104016, "-4": 0.008064404851829637, "-5": 0.0017018427750415215, "-6": 0.00030269033478969216, "-7": 4.6479733125888305e-05, "-8": 6.275577622622808e-06, "-9": 7.557660539068055e-07, "0": 0.29404191712175404, "1": 0.2133069967580546, "10": 1.5903810582095572e-07, "11": 1.6813093917391947e-08, "12": 1.62523145789112e-09, "13": 1.335522455555604e-10, "2": 0.10690356752705447, "3": 0.037998048133461956, "4": 0.010504847748546268, "5": 0.002368324650967511, "6": 0.00045001264149889883, "7": 7.382341748804716e-05, "8": 1.0648503696334124e-05, "9": 1.3700190987097683e-06} |
| Unadjusted home-win probability | 37.2% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 66.7% |
| Raw p under 3 5 | 80.5% |
| Raw p btts yes | 46.5% |
| P home draw | 68.1% |
| P draw away | 61.1% |
| P home away | 70.9% |
| Raw p home draw | 66.6% |
| Raw p draw away | 62.8% |
| Raw p home away | 70.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3979 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:52:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.74, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.11, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.82, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:52:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.27, "price": 1.74, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.45 |
| Reference draw odds | 3.32 |
| Reference away odds | 3.09 |
| Market reference 1x2 last update utc | 2026-10-29T11:53:11Z |
| Market reference home last update utc | 2026-10-29T11:53:11Z |
| Market reference draw last update utc | 2026-10-29T11:53:11Z |
| Market reference away last update utc | 2026-10-29T11:53:11Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.24 |
| Reference Under 2.5 odds | 1.77 |
| Market reference over 2 5 last update utc | 2026-10-29T11:53:11Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:53:11Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.0255 |
| Raw ev home | -0.0895 |
| Raw edge prob draw | 0.0037 |
| Raw ev draw | -0.0238 |
| Raw edge prob away | 0.0217 |
| Raw ev away | 0.0331 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10492693111921364, 0.10515323234041285, 0.058070916569629934, 0.02081543718108047, 0.005595947816494077, 0.0012035157058680386, 0.00021569924371610022, 3.313589405214914e-05, 4.454067727610367e-06, 5.321847404353355e-07, 5.722825824513379e-08, 5.594560229204114e-09, 5.013405327739931e-10, 4.147033813696635e-11, 3.185353613529466e-12], [0.12169008730845148, 0.13541524149526213, 0.07013872278597569, 0.025141125099379467, 0.006758850312879866, 0.0014536201501354079, 0.00026052403429878515, 4.002191500460347e-05, 5.379674371804306e-06, 6.427788673795733e-07, 6.912095034296177e-08, 6.7571743689474974e-09, 6.055248776286458e-10, 5.008835269444574e-11, 3.847306832272251e-12], [0.07525803066601505, 0.08092840111221167, 0.04302942990977369, 0.015182870428423041, 0.004081708680097788, 0.0008778495912339052, 0.00015733196667265005, 2.4169465264991358e-05, 3.2488163760113056e-06, 3.8817786471272333e-07, 4.174254051074883e-08, 4.080696567892393e-09, 3.656799654701755e-10, 3.024864503584583e-11, 2.3234107822095056e-12], [0.030299172472293127, 0.03258208541341915, 0.01751850303598403, 0.006209696374830812, 0.0016433116065550555, 0.0003534256202845243, 6.334245463816512e-05, 9.730719634120976e-06, 1.307985962912377e-06, 1.5628190066589808e-07, 1.6805707286970012e-08, 1.6429041262901427e-09, 1.4722415993867413e-10, 1.2178220781003541e-11, 9.354141131670789e-13], [0.009148922490875781, 0.009838254635866819, 0.005289762503545359, 0.0018961078212595024, 0.0005040779100722165, 0.00010671788509173397, 1.9126436815933552e-05, 2.9382188505123292e-06, 3.949501328718364e-07, 4.718977052018599e-08, 5.074531771896883e-09, 4.960796379872527e-10, 4.445475959103936e-11, 3.67724887879559e-12, 2.824509885893004e-13], [0.002210034820471592, 0.0023765514834797117, 0.0012778072321105811, 0.0004580281790048146, 0.0001231346603915867, 2.6188157264775432e-05, 4.620226195698883e-06, 7.097629230408606e-07, 9.540506511746461e-08, 1.1399269818241912e-08, 1.225815600106584e-09, 1.1983414164587838e-10, 1.0738594269420444e-11, 8.882847213738319e-13, 6.822951232579785e-14], [0.00044488425755127343, 0.00047840438189776453, 0.0002572250520604279, 9.220195286816205e-05, 2.478724382969214e-05, 5.330971308611147e-06, 9.448214023028319e-07, 1.4287664073413802e-07, 1.920522299841281e-08, 2.294694926405292e-09, 2.467590365982635e-10, 2.4122843061832212e-11, 2.161699668458633e-12, 1.7881342189812645e-13, 1.3734731983847589e-14], [7.676233389767406e-05, 8.254604715275671e-05, 4.438276922134854e-05, 1.5908940296157266e-05, 4.276902711125032e-06, 9.198298043696597e-07, 1.6485584042043127e-07, 2.5043840280327507e-08, 3.3137556911946816e-09, 3.9593699966720115e-10, 4.257691576654904e-11, 4.162264009668043e-12, 3.729893987484787e-13, 3.0853273327046617e-14, 2.369852528255984e-15], [1.1589304026219748e-05, 1.2462508473116599e-05, 6.70075256853729e-06, 2.4018751966676674e-06, 6.45711552698027e-07, 1.3887263080651633e-07, 2.4889348175332585e-08, 3.82352200200743e-09, 5.082392884722092e-10, 5.97771593355827e-11, 6.428111239752668e-12, 6.284038094742851e-13, 5.6312612203991464e-14, 4.658117420815345e-15, 3.577919020007328e-16], [1.5552994518401796e-06, 1.672484607612305e-06, 8.99249581612893e-07, 3.2233472936029727e-07, 8.665531784186798e-08, 1.8636885017454374e-08, 3.3401824204607454e-09, 5.13121552456222e-10, 6.897288310795875e-11, 8.149491261084867e-12, 8.626607659041712e-13, 8.433259652162518e-14, 7.557224721554289e-15, 6.251253271819143e-16, 4.801613175352239e-17], [1.8785086157715073e-07, 2.020046198452456e-07, 1.0861240160472502e-07, 3.893196037260076e-08, 1.0466329231696712e-08, 2.250984467011083e-09, 4.0343108509812574e-10, 6.197541290756618e-11, 8.330624370734727e-12, 9.953668061491965e-13, 1.0584681182648321e-13, 1.0185788271758109e-14, 9.127703178937374e-16, 7.55033579969961e-17, 5.799443771956037e-18], [2.0626221560523407e-08, 2.2180319058404275e-08, 1.1925755574985881e-08, 4.274770068600293e-09, 1.1492139234596824e-09, 2.471604546077564e-10, 4.429715613637874e-11, 6.80496531772027e-12, 9.14711290465387e-13, 1.092923189452176e-13, 1.1752702731931155e-14, 1.1361605196781288e-15, 1.0022313793335104e-16, 8.29034787242619e-18, 6.367850068072985e-19], [2.0760490242147986e-09, 2.232470431041205e-09, 1.2003387606317053e-09, 4.302597159455248e-10, 1.1566948592168575e-10, 2.4876937305617582e-11, 4.4585513397387354e-12, 6.849262995752584e-13, 9.206657052707122e-14, 1.1000376944202367e-14, 1.1829208256547553e-15, 1.1564080418379885e-16, 1.0247654737503097e-17, 8.3443148132822e-19, 6.409302295807195e-20], [1.9288276579087413e-10, 2.0741565650090356e-10, 1.1152176915677628e-10, 3.997481902016115e-11, 1.0746687627293218e-11, 2.311280907120447e-12, 4.142376715572383e-13, 6.363552954870679e-14, 8.553774286162879e-15, 1.022029395737616e-15, 1.0990349356042308e-16, 1.0744022847768846e-17, 9.627949146956747e-19, 7.875625620448847e-20, 5.9547917182382654e-21], [1.664043065070637e-11, 1.7894215865901476e-11, 9.621234214929649e-12, 3.4487176754855612e-12, 9.27140947266725e-13, 1.9939940974788317e-13, 3.573721694727191e-14, 5.489980465773328e-15, 7.379533740459418e-16, 8.817277797226495e-17, 9.48162193425527e-18, 9.269110507350528e-19, 8.306248587401863e-20, 6.87083758544893e-21, 5.218867546433834e-22]] |
| Legacy trial inputs | {"lambda_home": 1.2078115333667214, "lambda_away": 1.0753457192011968, "rho": -0.0218549380431621, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3925 |
| Legacy p draw | 0.2901 |
| Legacy p away | 0.3174 |
| Legacy p over 1 5 | 0.6682 |
| Legacy p under 3 5 | 0.8027 |
| Legacy p btts yes | 0.4648 |
| Legacy p over 2 5 | 0.3995 |
| Legacy goal margin distribution | {"-1": 0.19222962152370063, "-10": 6.436357325132106e-08, "-11": 6.231269165981773e-09, "-12": 5.537522962506485e-10, "-13": 4.53176449692386e-11, "-14": 3.185353613529466e-12, "-2": 0.08766703177680406, "-3": 0.028518515501655912, "-4": 0.00721703725331719, "-5": 0.0014895656314813863, "-6": 0.00025913145355620514, "-7": 3.892105899536868e-05, "-8": 5.140277396406022e-06, "-9": 6.055373569845194e-07, "0": 0.29011253534815556, "1": 0.2221617336589494, "10": 2.1127242135615415e-07, "11": 2.2973662478396872e-08, "12": 2.2930859149306315e-09, "13": 2.107769816567756e-10, "14": 1.664043065070637e-11, "2": 0.11361363924652927, "3": 0.041511855471564274, "4": 0.011799272725478942, "5": 0.002735312798080406, "6": 0.0005344641100145389, "7": 9.016419842336457e-05, "8": 1.3374793822009422e-05, "9": 1.7696710330633935e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3878 |
| Legacy raw p draw | 0.2899 |
| Legacy raw p away | 0.3222 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2078 |
| Legacy lambda away | 1.0753 |
| Legacy model home team | Vallecano |
| Legacy model away team | Celta |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 9.258036261887293, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.5850 |
| Elo away rating | 1,513.4884 |
| Elo rating diff | 21.0966 |
| Elo home expectancy | 0.5303 |

</details>


---

## 2026-10-31 — Real Betis vs Málaga

The model's most likely 1X2 outcome is **Real Betis win** at **74.0%**. Expected goals are 2.36 for Real Betis and 0.60 for Málaga (2.96 combined). The most likely exact score is 2-0 at 14.0%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 56.3%; Under 3.5 goals: 66.3%; Double Chance 1X: 90.1%; Double Chance X2: 26.0%; Double Chance 12 (either team wins): 84.0%; Under 4.5 goals: 82.5%; BTTS Yes (both teams score): 41.2%; BTTS No (at least one team does not score): 58.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 74.0% | 1.35 |
| Draw | 16.0% | 6.23 |
| Málaga win | 9.9% | 10.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 2.36 |
| Málaga expected goals | 0.60 |
| Expected total goals | 2.96 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 56.3% |
| Under 2.5 | 43.7% |
| Over 3.5 | 33.7% |
| Under 3.5 | 66.3% |
| Over 4.5 | 17.5% |
| Under 4.5 | 82.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.98% |
| 2 | 1-0 | 11.61% |
| 3 | 3-0 | 11.01% |
| 4 | 2-1 | 8.33% |
| 5 | 1-1 | 7.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 74.0% | 72.9% | 1.35 | -0.1% |
| Draw | 16.0% | 16.1% | 5.67 | -9.0% |
| Málaga win | 9.9% | 11.0% | 8.10 | -19.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:30:00+00:00 |
| Fixture id | 8f0b7ef29a47f675429758e83a426d7e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:53:11Z |
| Market best draw last update utc | 2026-10-29T11:53:11Z |
| Market best away last update utc | 2026-10-29T11:53:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Betis |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3627 |
| Dc lambda away | 0.5959 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:52:59.394319+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.35 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.78 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 2.96 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.72 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.07581741118333041, "-10": 1.23997193567552e-10, "-11": 6.646922879497203e-12, "-12": 3.2714138306436574e-13, "-13": 1.488113127012153e-14, "-14": 6.292035307949019e-16, "-15": 2.485079730772735e-17, "-16": 9.207143745718033e-19, "-17": 3.204040658011574e-20, "-18": 9.83757547783507e-22, "-2": 0.019438416803403132, "-3": 0.0034786868609541777, "-4": 0.00048553789505408605, "-5": 5.535044660213987e-05, "-6": 5.323019730330072e-06, "-7": 4.4222787897611504e-07, "-8": 3.231774017834085e-08, "-9": 2.107217366921641e-09, "0": 0.1604437095116555, "1": 0.22142136684643773, "10": 8.49933160324037e-05, "11": 1.806447479901083e-05, "12": 3.5251042637893176e-06, "13": 6.357761190771758e-07, "14": 1.0658379905522354e-07, "15": 1.6690607873598072e-08, "16": 2.451819711914043e-09, "17": 3.38293309729095e-10, "18": 4.1182741119393575e-11, "2": 0.21816222454065326, "3": 0.1547981556235056, "4": 0.08566538243544433, "5": 0.038719981225786106, "6": 0.014763994217532382, "7": 0.004863217467523447, "8": 0.0014091276580224, "9": 0.00036429270362460005} |
| Raw goal margin distribution | {"-1": 0.05606472545028891, "-10": 9.169224463706833e-11, "-11": 4.915202201076851e-12, "-12": 2.4191134382815776e-13, "-13": 1.1004154929949748e-14, "-14": 4.652773374320193e-16, "-15": 1.837642708360952e-17, "-16": 6.808409549052495e-19, "-17": 2.3692929766306373e-20, "-18": 7.2745951049115e-22, "-2": 0.014374132330050986, "-3": 0.002572385692718085, "-4": 0.00035904086353061326, "-5": 4.093001256394961e-05, "-6": 3.936215113251472e-06, "-7": 3.2701439200169736e-07, "-8": 2.389800973144835e-08, "-9": 1.5582247045454045e-09, "0": 0.15982567164178646, "1": 0.22934283483402507, "10": 8.80339974341065e-05, "11": 1.871074105990057e-05, "12": 3.651216756798544e-06, "13": 6.585213502455624e-07, "14": 1.1039689155047918e-07, "15": 1.728772330941676e-08, "16": 2.5395348752511586e-09, "17": 3.503959340674792e-10, "18": 4.265607573955524e-11, "2": 0.22596709496672265, "3": 0.16033614254759315, "4": 0.08873010737266064, "5": 0.040105209291751244, "6": 0.015292184017951314, "7": 0.005037201677061726, "8": 0.001459539954687472, "9": 0.0003773254702043279} |
| Unadjusted home-win probability | 76.7% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 7.3% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.7% |
| Raw p btts yes | 40.9% |
| P home draw | 90.1% |
| P draw away | 26.0% |
| P home away | 84.0% |
| Raw p home draw | 92.7% |
| Raw p draw away | 23.3% |
| Raw p home away | 84.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5628 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.78, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:52:48Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.08, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:52:48Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:53:11Z", "line": -1.25, "market_key": "spreads", "opposite_price": 2.16, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.35 |
| Reference draw odds | 5.67 |
| Reference away odds | 8.10 |
| Market reference 1x2 last update utc | 2026-10-29T11:53:11Z |
| Market reference home last update utc | 2026-10-29T11:53:11Z |
| Market reference draw last update utc | 2026-10-29T11:53:11Z |
| Market reference away last update utc | 2026-10-29T11:53:11Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Market reference over 2 5 last update utc | 2026-10-29T11:52:51Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:52:51Z |
| Home probability edge | +1.1% |
| Draw probability edge | -0.0% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | 0.0378 |
| Raw ev home | 0.0351 |
| Raw edge prob draw | -0.0009 |
| Raw ev draw | -0.0938 |
| Raw edge prob away | -0.0370 |
| Raw ev away | -0.4053 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.06019119749518163, 0.03928779099337349, 0.011551136505660716, 0.0021520623834586305, 0.0003007088847942364, 3.3614577008262385e-05, 3.1313224754942406e-06, 2.500236840648532e-07, 1.7467974856392866e-08, 1.0848044139847757e-09, 6.063213186691473e-11, 3.0807861158568367e-12, 1.4349332440509245e-13, 6.169354695996829e-15, 2.462992555808967e-16, 9.177475528053152e-18, 3.205934517139783e-19, 1.0540400695821112e-20], [0.13008373392721306, 0.07575937515401382, 0.026160052662456124, 0.0048738117895654135, 0.0006810204570286756, 7.612749657415916e-05, 7.0915585511363775e-06, 5.662328324829831e-07, 3.956001575479252e-08, 2.4567747584317343e-09, 1.3731460639376695e-10, 6.977108009509115e-12, 3.2497173947416753e-13, 1.3971841096463317e-14, 5.57798056802676e-16, 2.078438281848876e-17, 7.260533693776606e-19, 2.387102231463912e-20], [0.14912297608252365, 0.08334814860321235, 0.02346131969569065, 0.005518901669088962, 0.000771159227983734, 8.620360942254486e-05, 8.030185820490713e-06, 6.411784983108577e-07, 4.4796115731374575e-08, 2.781949508988637e-09, 1.5548934656018547e-10, 7.900586789488502e-12, 3.679844755660225e-13, 1.5821131483288733e-14, 6.316273093051393e-16, 2.353537025650506e-17, 8.221526240887796e-19, 2.7030552385542324e-20], [0.11257376869624502, 0.0629199835505288, 0.017583689237059646, 0.0032997058045784564, 0.0005821524143333513, 6.507558689376436e-05, 6.062032189080824e-06, 4.840292345151988e-07, 3.381683831231543e-08, 2.1001092439049133e-09, 1.1737977737722988e-10, 5.964197155724014e-12, 2.7779353875860094e-13, 1.1943460645038411e-14, 4.768189885145501e-16, 1.7766982641025682e-17, 6.206476142614205e-19, 2.04055151789476e-20], [0.06373692571423036, 0.03562398562245536, 0.009955519013568965, 0.0018547870130709234, 0.0002610480965104179, 3.684444338760199e-05, 3.432196503567935e-06, 2.7404728224968846e-07, 1.914639028580449e-08, 1.1890381606723334e-09, 6.645798783935484e-11, 3.376804343160319e-12, 1.5728092209051805e-13, 6.762138930941188e-15, 2.699649909748473e-16, 1.005929592543566e-17, 3.5139776648708685e-19, 1.1553178153167438e-20], [0.028869217023107963, 0.01613564759577235, 0.004509286191006723, 0.0008401134540449222, 0.0001173895244897481, 1.3217393351304474e-05, 1.5545906021842012e-06, 1.2412789567747847e-07, 8.67223026802824e-09, 5.385669347014445e-10, 3.0101704033475954e-11, 1.5295010911626612e-12, 7.123934865926458e-14, 3.0628658999497803e-15, 1.2227884896798808e-16, 4.556291253724999e-18, 1.591632835828192e-19, 5.23293528316434e-21], [0.010896766698790165, 0.006090445308727561, 0.0017020426831162638, 0.00031710317262552293, 4.430900430111453e-05, 4.953057633326673e-06, 4.6473845171960733e-07, 4.6852421349930725e-08, 3.273357566755261e-09, 2.0328359561766872e-10, 1.136197236753135e-11, 5.77314464143726e-13, 2.688949137388848e-14, 1.1560872993097774e-15, 4.615449349853264e-17, 1.7197848754899978e-18, 6.007662649205591e-20, 1.9751860566522026e-21], [0.00352544148301095, 0.0019704476690118994, 0.0005506635176083516, 0.00010259269653745281, 1.4335335072503954e-05, 1.602467532888688e-06, 1.4927579189084486e-07, 1.2005432754296774e-08, 1.0590325436487538e-09, 6.576853855976575e-11, 3.675949923546262e-12, 1.867791076834288e-13, 8.699583185266929e-15, 3.74030043556067e-16, 1.4932407979804866e-17, 5.564036662894158e-19, 1.9436649150060603e-20, 6.390338577735739e-22], [0.0009980158100544696, 0.0005578132373024967, 0.00015588711349818647, 2.904292515814262e-05, 4.0581842341539285e-06, 4.536418887191395e-07, 4.225842382674467e-08, 3.3741675891330952e-09, 2.3744505979476016e-10, 1.8618389101941412e-11, 1.0406231838897022e-12, 5.287522239533063e-14, 2.4627615013950436e-15, 1.0588401444278271e-16, 4.227209363095389e-18, 1.5751208987727885e-19, 5.502313182539358e-21, 1.8090383751694944e-22], [0.0002511359056525572, 0.00014036544423810443, 3.9226684621151816e-05, 7.308222213425165e-06, 1.0211819919902398e-06, 1.1415226634455806e-07, 1.0633706833361597e-08, 8.490593283028226e-10, 5.931976826056382e-11, 3.71059377844879e-12, 2.618574205902857e-13, 1.330526703991493e-14, 6.197174772465179e-16, 2.664414490564572e-17, 1.0637146637246057e-18, 3.9635585873532884e-20, 1.3845756653951291e-21, 4.552177291496275e-23], [5.6875169937477264e-05, 3.17887976776864e-05, 8.88373308513847e-06, 1.6551053472395816e-06, 2.3126879918114587e-07, 2.5852255296688183e-08, 2.408233428992338e-09, 1.9228789072890427e-10, 1.3434247451413699e-11, 8.342999720155733e-13, 4.6968717826585684e-14, 3.01326615161758e-15, 1.4034845690438015e-16, 6.03414420335374e-18, 2.409012447149745e-19, 8.976337637866168e-21, 3.13567174140325e-22, 1.0309392293651869e-23], [1.17096501521451e-05, 6.5447839535640605e-06, 1.8290126708432344e-06, 3.407586228300556e-07, 4.761439363600849e-08, 5.3225487589916485e-09, 4.958151504285747e-10, 3.958887386894103e-11, 2.765887783479719e-12, 1.717684677687336e-13, 9.600521766016624e-15, 4.913473602705733e-16, 2.889540957064963e-17, 1.2423297840963015e-18, 4.9597553729151385e-20, 1.8480784057874864e-21, 6.455825824197667e-23, 2.12253215546592e-24], [2.209920098114276e-06, 1.2351735029545228e-06, 3.4518297374253164e-07, 6.431014756319857e-08, 8.986093016319838e-09, 1.0045054568546673e-09, 9.357340754377157e-11, 7.471465576506299e-12, 5.219960393710688e-13, 3.241724425685598e-14, 1.8118718943295712e-15, 9.206322792696827e-17, 4.319081784876407e-18, 2.344604256052384e-19, 9.360367677874251e-21, 3.48781181228765e-22, 1.2183847556031401e-23, 4.0057784889488522e-25], [3.8498793282680757e-07, 2.1517831979114335e-07, 6.013397480820395e-08, 1.1203405404235796e-08, 1.5654581256102468e-09, 1.749938740670835e-10, 1.6301328165021365e-11, 1.3015964196806317e-12, 9.093639915430864e-14, 5.647375153987729e-15, 3.1564436005634404e-16, 1.6038241309814975e-17, 7.470108201641156e-19, 3.234968200201769e-20, 1.6306601337662157e-21, 6.07608148750412e-23, 2.122535691890398e-24, 6.978425967248546e-26], [6.227775937411539e-08, 3.480842509551548e-08, 9.727601553161377e-09, 1.8123243001736928e-09, 2.532370917216966e-10, 2.8307968774690927e-11, 2.63699224410859e-12, 2.1055337509382856e-13, 1.4710370642781335e-14, 9.135503763792659e-16, 5.106036274708096e-17, 2.594433871583166e-18, 1.2084056704439628e-19, 5.1954216187621365e-21, 2.0891962482395534e-22, 9.829002640104293e-24, 3.433530139813184e-25, 1.1288684557131167e-26], [9.402765774768744e-09, 5.255414957940005e-09, 1.4686841638793673e-09, 2.736267501225749e-10, 3.823401938144254e-11, 4.273968791152691e-12, 3.981360387788851e-13, 3.178958409857562e-14, 2.2209882148007505e-15, 1.3792885773145368e-16, 7.709150684137784e-18, 3.917105280888162e-19, 1.8244643985713988e-20, 7.844105676463115e-22, 3.131603683063297e-23, 1.175335927669207e-24, 5.183982212868577e-26, 1.704378222060291e-27], [1.3309125887750748e-09, 7.438766522854506e-10, 2.0788460432427608e-10, 3.873044326393458e-11, 5.411826576684411e-12, 6.049580521766008e-13, 5.6354085462571435e-14, 4.499650281861754e-15, 3.143693297701121e-16, 1.952311240196482e-17, 1.0911901817032447e-18, 5.544458784542679e-20, 2.582434460237675e-21, 1.110292358924951e-22, 4.432622129147782e-24, 1.6516607417028604e-25, 5.811487918343929e-27, 2.412458723433331e-28], [1.773023571389277e-10, 9.909823153165363e-11, 2.7694103031597792e-11, 5.159616748423162e-12, 7.209561443523178e-13, 8.05916853786803e-14, 7.507414289407626e-15, 5.994372643279263e-16, 4.1879852704470575e-17, 2.600842366922408e-18, 1.4536686551361244e-19, 7.386252259164606e-21, 3.440283913599038e-22, 1.4791163147079017e-23, 5.905078653793499e-25, 2.200319879514172e-26, 7.686298295125759e-28, 2.545392670601354e-29]] |
| Legacy trial inputs | {"lambda_home": 2.264716779135647, "lambda_away": 0.5589222452017591, "rho": -0.0218549380431621, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7448 |
| Legacy p draw | 0.1630 |
| Legacy p away | 0.0922 |
| Legacy p over 1 5 | 0.7704 |
| Legacy p under 3 5 | 0.6902 |
| Legacy p btts yes | 0.3864 |
| Legacy p over 2 5 | 0.5340 |
| Legacy goal margin distribution | {"-1": 0.0715873447035789, "-10": 6.798944239463279e-11, "-11": 3.4220660262372024e-12, "-12": 1.5811491642420372e-13, "-13": 6.751320323848424e-15, "-14": 2.679261965386532e-16, "-15": 9.930559449816355e-18, "-16": 3.4446447402861743e-19, "-17": 1.0540400695821112e-20, "-2": 0.017264742774683046, "-3": 0.0029256314086244964, "-4": 0.00038537029293186307, "-5": 4.138235062200765e-05, "-6": 3.7445195477092226e-06, "-7": 2.92486478320882e-07, "-8": 2.008636354904495e-08, "-9": 1.2303042868639722e-09, "0": 0.16298634062441386, "1": 0.2329928540728023, "10": 6.377659783820213e-05, "11": 1.300680880069285e-05, "12": 2.4351051386269653e-06, "13": 4.213044934856107e-07, "14": 6.774621855312809e-08, "15": 1.0174336530085792e-08, "16": 1.4300108203067285e-09, "17": 1.773023571389277e-10, "2": 0.22288454669359137, "3": 0.1530389434880872, "4": 0.08168138347450692, "5": 0.03554041631222778, "6": 0.01303064638975147, "7": 0.004124185145695054, "8": 0.0011476149097565318, "9": 0.000284819620317422} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7607 |
| Legacy raw p draw | 0.1653 |
| Legacy raw p away | 0.0741 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2647 |
| Legacy lambda away | 0.5589 |
| Legacy model home team | Betis |
| Legacy model away team | Malaga |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 10.07970162881688, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,565.5196 |
| Elo away rating | 1,404.7246 |
| Elo rating diff | 220.7950 |
| Elo home expectancy | 0.7809 |

</details>


---
