# Serie A — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,980 |
| Training data through | 2026-10-25 |
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
| Training sha256 | 477537d170c98109e108969f68d3e67b2d5ac4084c8e9017f02c86c070e0ad2c |
| Training as of utc | 2026-10-26T11:42:05.183279+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 80, 'bbs_added_results': 10, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 80, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 100, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-26T11:42:05.183279+00:00', 'observations': 332, 'observations_sha256': '28f87dedc542ea6ed15da20839551d0aea7043fd2d7ffcccdcb9c604302faa58', 'eligible_training_matches': 140, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 142, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 16, 'retrospective_eligible_training_matches': 140, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'a6ef49289829d48ed55f634e912846675525b445504d495c2cea78433e0e46f9', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 79, 'tuning_matches': 20, 'audit_matches': 41, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-05T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 32, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-26', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1970, 'tune_start_date': '2025-10-27', 'audit_start_date': '2026-04-27', 'training_shot_matches': 1600, 'tuning_matches': 258, 'audit_matches': 112, 'audit_matchdays': 38, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8795837161089624, 'audit_candidate_poisson_score': 0.876579055323487, 'audit_gain': 0.0030046607854753438, 'audit_gain_lower95': -0.001746877171994197, 'audit_baseline_briers': [0.5874897559022755, 0.16922511059665027, 0.1953962342079745, 0.24317108165476647], 'audit_candidate_briers': [0.5867226447788666, 0.16762451913172724, 0.19525382295262814, 0.24305711753920162], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1781.330 |
| Base scoring parameter | 0.142 |
| Home-advantage parameter | 0.114 |
| Dixon-Coles low-score adjustment | -0.024 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1980, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261026T114205183279Z_19a646af00db45aaf2a96caf6606e9f41139b1dde1b78b7d7fb61abc12833a41.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE': 7} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 7} |
| Legacy comparison status | {'AVAILABLE': 7} |
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

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **58.3%**. Expected goals are 1.57 for Lazio and 0.69 for Parma (2.26 combined). The most likely exact score is 1-0 at 16.1%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 39.3%; Under 3.5 goals: 80.8%; Double Chance 1X: 84.0%; Double Chance X2: 41.7%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 39.7%; BTTS No (at least one team does not score): 60.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 58.3% | 1.72 |
| Draw | 25.7% | 3.89 |
| Parma win | 16.0% | 6.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.57 |
| Parma expected goals | 0.69 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 66.2% |
| Under 1.5 | 33.8% |
| Over 2.5 | 39.3% |
| Under 2.5 | 60.7% |
| Over 3.5 | 19.2% |
| Under 3.5 | 80.8% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.13% |
| 2 | 2-0 | 12.87% |
| 3 | 1-1 | 11.57% |
| 4 | 0-0 | 10.71% |
| 5 | 2-1 | 8.87% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | b27cb3ea731fa3f18d05e6a627bdf984 |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5700 |
| Dc lambda away | 0.6892 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:42:05.183279+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 39.7% |
| P btts no | 60.3% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.33 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.54 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.20 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.65 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.11590272187827642, "-10": 7.67200725323396e-10, "-11": 4.76783863114671e-11, "-12": 2.719455683531001e-12, "-13": 1.4331074773744095e-13, "-14": 7.002817506943804e-15, "-15": 3.0009557043941154e-16, "-2": 0.03504820448646522, "-3": 0.007415939634436169, "-4": 0.0012142530146628738, "-5": 0.00016167803801335451, "-6": 1.8112716660957495e-05, "-7": 1.749932896888953e-06, "-8": 1.4854417587180126e-07, "-9": 1.1240856235616534e-08, "0": 0.25734667627880775, "1": 0.2674892586992102, "10": 2.887939985546768e-06, "11": 4.0885435040716293e-07, "12": 5.3124759488025563e-08, "13": 6.3776644944040825e-09, "14": 7.099432454935478e-10, "15": 6.930719521345785e-11, "2": 0.18188697738526236, "3": 0.08767382087081312, "4": 0.03270249244779507, "5": 0.009919518914747388, "6": 0.0025315766945301385, "7": 0.0005571816523055814, "8": 0.00010774545412222754, "9": 1.8574222202528965e-05} |
| Raw goal margin distribution | {"-1": 0.11590272187827642, "-10": 7.67200725323396e-10, "-11": 4.76783863114671e-11, "-12": 2.719455683531001e-12, "-13": 1.4331074773744095e-13, "-14": 7.002817506943804e-15, "-15": 3.0009557043941154e-16, "-2": 0.03504820448646522, "-3": 0.007415939634436169, "-4": 0.0012142530146628738, "-5": 0.00016167803801335451, "-6": 1.8112716660957495e-05, "-7": 1.749932896888953e-06, "-8": 1.4854417587180126e-07, "-9": 1.1240856235616534e-08, "0": 0.25734667627880775, "1": 0.2674892586992102, "10": 2.887939985546768e-06, "11": 4.0885435040716293e-07, "12": 5.3124759488025563e-08, "13": 6.3776644944040825e-09, "14": 7.099432454935478e-10, "15": 6.930719521345785e-11, "2": 0.18188697738526236, "3": 0.08767382087081312, "4": 0.03270249244779507, "5": 0.009919518914747388, "6": 0.0025315766945301385, "7": 0.0005571816523055814, "8": 0.00010774545412222754, "9": 1.8574222202528965e-05} |
| Unadjusted home-win probability | 58.3% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 16.0% |
| Raw p over 1 5 | 66.2% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 39.7% |
| P home draw | 84.0% |
| P draw away | 41.7% |
| P home away | 74.3% |
| Raw p home draw | 84.0% |
| Raw p draw away | 41.7% |
| Raw p home away | 74.3% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.3931 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.1013947549930944, 0.06618825587926379, 0.024898612805196136, 0.005922334134741249, 0.0010565058948646046, 0.00015077902468701914, 1.7931998294310022e-05, 1.8279725019233282e-06, 1.6304920323587688e-07, 1.2927518887915448e-08, 9.224741191778715e-10, 5.98412304459681e-11, 3.558428781834725e-12, 1.9532324711223892e-13, 9.955542010642495e-15, 4.736010535267584e-16], [0.15398189687424416, 0.11604187971940393, 0.04011872937837867, 0.00954256055543922, 0.0017023307448633968, 0.00024294778727961935, 2.8893536857315875e-05, 2.945382326700352e-06, 2.627185261748914e-07, 2.0829900679845246e-08, 1.4863675271954062e-09, 9.642120019754558e-11, 5.73363835277073e-12, 3.1472116754097887e-13, 1.6041202731450715e-14, 7.631056657015786e-16], [0.12695247409085283, 0.09058998306618983, 0.03232132768857893, 0.0076878862187166165, 0.0013714689047137543, 0.00019572890681108322, 2.327784272626135e-05, 2.372923291053602e-06, 2.1165704163441115e-07, 1.678143989167983e-08, 1.1974798967097047e-09, 7.768095490557853e-11, 4.619259057281641e-12, 2.5355254626050726e-13, 1.2923464377751918e-14, 6.147898665864644e-16], [0.0681854847606028, 0.04865538819985874, 0.017359609667590082, 0.004129121959706022, 0.0007366085046525153, 0.00010512493346939945, 1.2502402980625045e-05, 1.2744842198539929e-06, 1.1367984822815881e-07, 9.013220279395503e-09, 6.431599528323874e-10, 4.172201924251461e-11, 2.480978967216896e-12, 1.3618169636209976e-13, 6.941122571213349e-15, 3.3020030038252557e-16], [0.027466540325424327, 0.019599408682546417, 0.006992814095881977, 0.0016632967443591426, 0.0002967213222597607, 4.2346523376382066e-05, 5.0362295851925435e-06, 5.133889176214048e-07, 4.579262208825627e-08, 3.6307137675288465e-09, 2.5907828978838226e-10, 1.6806502557048426e-11, 9.99390252761914e-13, 5.485683746103555e-14, 2.796029443441021e-15, 1.3301159180383432e-16], [0.008851277835414681, 0.006316041612946646, 0.0022534814971495428, 0.0005360085920044259, 9.562044698369498e-05, 1.3646452714005934e-05, 1.6229589447132442e-06, 1.6544304064693562e-07, 1.4756981262038204e-08, 1.1700219946345402e-09, 8.34897259309495e-11, 5.416008780557793e-12, 3.2206024815629367e-13, 1.7677985788780205e-14, 9.01039342657511e-16, 4.286388239791228e-17], [0.0023769866411843888, 0.0016961558340277219, 0.0006051663403275949, 0.0001439436527070538, 2.567861153278041e-05, 3.6647178411869233e-06, 4.3584122004835467e-07, 4.4429279569244006e-08, 3.962947268893384e-09, 3.1420623133201194e-10, 2.2420939315675126e-11, 1.454454459492186e-12, 8.648840560185332e-14, 4.747375107224772e-15, 2.4197167013661203e-16, 1.1510979289507611e-17], [0.0005471428384946388, 0.0003904268965923813, 0.00013929923857008655, 3.313343767307881e-05, 5.910789803869476e-06, 8.435571690507517e-07, 1.00323408696736e-07, 1.0226882101312703e-08, 9.122046291461264e-10, 7.232505488463288e-11, 5.160927775673988e-12, 3.3479125529759694e-13, 1.9908194231287136e-14, 1.0927668866794687e-15, 5.569785885202384e-17, 2.6496362130062266e-18], [0.00011020029328854527, 7.863606262414517e-05, 2.8056324354951765e-05, 6.673421074608103e-06, 1.190494920385843e-06, 1.6990124131170308e-07, 2.0206184353074065e-08, 2.0598010751502824e-09, 1.8372755814121255e-10, 1.4567022904522172e-11, 1.0394648609219541e-12, 6.74304622641916e-14, 4.009718648916693e-15, 2.2009468631520422e-16, 1.121813162706171e-17, 5.336644606088501e-19], [1.9729326459765498e-05, 1.4078334138005308e-05, 5.022966508905378e-06, 1.194752745708962e-06, 2.1313611998731637e-07, 3.0417678172426545e-08, 3.6175439802521998e-09, 3.6876932575314697e-10, 3.289302474660755e-11, 2.607956311674107e-12, 1.860969782619959e-13, 1.2072178427508941e-14, 7.178660407840335e-16, 3.9403887129433865e-17, 2.0083992023451947e-18, 9.554276172167943e-20], [3.1789542463660214e-06, 2.2684190553103977e-06, 8.093424144712974e-07, 1.9250856444970152e-07, 3.434227595500543e-08, 4.901150953532335e-09, 5.828889709383043e-10, 5.941920097592805e-11, 5.29999951631869e-12, 4.2021575385457984e-13, 2.998550307778163e-14, 1.945170452386238e-15, 1.1566858621992162e-16, 6.3490841701511425e-18, 3.2361009311258935e-19, 1.5394649619897862e-20], [4.656542920831113e-07, 3.322787896541441e-07, 1.1855275032482338e-07, 2.8198719563590858e-08, 5.030468185137147e-09, 7.179222476285965e-10, 8.538177340413275e-11, 8.703744634959472e-12, 7.763457198647749e-13, 6.155334560319918e-14, 4.392286622055612e-15, 2.849292250815895e-16, 1.6943173590517402e-17, 9.300159944130923e-19, 4.7402515777492626e-20, 2.2550134777232947e-21], [6.252509819899228e-08, 4.4616283594481605e-08, 1.5918509679488124e-08, 3.786344805095613e-09, 6.75459289456025e-10, 9.639803561438555e-11, 1.1464521764881913e-11, 1.16868350029653e-12, 1.0424276807105788e-13, 8.26499195594148e-15, 5.897683260549243e-16, 3.8258485062582536e-17, 2.2750216427954523e-18, 1.2487663566286511e-19, 6.36490848308988e-21, 3.027888747765154e-22], [7.74966712349541e-09, 5.5299608653837235e-09, 1.9730181106722488e-09, 4.692981330613892e-10, 8.371973494703432e-11, 1.1948045007346883e-11, 1.4209690183155102e-12, 1.4485236106619225e-13, 1.2920359597219382e-14, 1.0244036120193735e-15, 7.309877694810932e-17, 4.741944154019972e-18, 2.819773329151939e-19, 1.5477822278811192e-20, 7.888979535621693e-22, 3.752913719139987e-23], [8.919223174988235e-10, 6.364525639787981e-10, 2.2707799673132432e-10, 5.401231714442855e-11, 9.635446119738142e-12, 1.375120740376584e-12, 1.6354173149805595e-13, 1.6671303620982042e-14, 1.4870260736660275e-15, 1.1790034708927926e-16, 8.413062071300959e-18, 5.457583857351336e-19, 3.245324892644158e-20, 1.781368786137692e-21, 9.079560190114093e-23, 4.319291975264475e-24], [9.580932710918998e-11, 6.836704351419905e-11, 2.4392471901746894e-11, 5.801944473962209e-12, 1.0350291623128766e-12, 1.4771397715311169e-13, 1.7567475262912936e-14, 1.790813337240436e-15, 1.5973472657494166e-16, 1.2664727296252108e-17, 9.037219948028221e-19, 5.862477334137327e-20, 3.486092769680596e-21, 1.9135270122152982e-22, 9.753164992010279e-24, 4.639736551258113e-25]] |
| Legacy trial inputs | {"lambda_home": 1.6112837165774236, "lambda_away": 0.7135739867610584, "rho": -0.03199263817223977, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5857 |
| Legacy p draw | 0.2542 |
| Legacy p away | 0.1601 |
| Legacy p over 1 5 | 0.6784 |
| Legacy p under 3 5 | 0.7943 |
| Legacy p btts yes | 0.4119 |
| Legacy p over 2 5 | 0.4105 |
| Legacy goal margin distribution | {"-1": 0.11477549481957197, "-10": 1.0236535990223867e-09, "-11": 6.583549547916237e-11, "-12": 3.886403614053839e-12, "-13": 2.119792397102761e-13, "-14": 1.0718647676344073e-14, "-15": 4.736010535267584e-16, "-2": 0.03592297290776833, "-3": 0.007833424654730551, "-4": 0.0013240529944942023, "-5": 0.000182162880361695, "-6": 2.1098315464815234e-05, "-7": 2.1081327613091437e-06, "-8": 1.8511932314453422e-07, "-9": 1.4494104118371434e-08, "0": 0.254197898390225, "1": 0.26369417393373557, "10": 3.527630626992812e-06, "11": 5.122986411345719e-07, "12": 6.82879390055813e-08, "13": 8.410512159375954e-09, "14": 9.602893610130225e-10, "15": 9.580932710918998e-11, "2": 0.18316322772761565, "3": 0.09018840296179886, "4": 0.034422103220668195, "5": 0.010693624452921534, "6": 0.002796699686686507, "7": 0.0006309995044961598, "8": 0.0001251168561332525, "9": 2.212016972262898e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.5857 |
| Legacy raw p draw | 0.2542 |
| Legacy raw p away | 0.1601 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.6113 |
| Legacy lambda away | 0.7136 |
| Legacy model home team | Lazio |
| Legacy model away team | Parma |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.984675821011816, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,530.9463 |
| Elo away rating | 1,398.0944 |
| Elo rating diff | 192.8519 |
| Elo home expectancy | 0.7522 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **36.5%**. Expected goals are 1.18 for Napoli and 1.15 for AS Roma (2.33 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.3%; Double Chance 1X: 65.2%; Double Chance X2: 63.5%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 47.7%; BTTS No (at least one team does not score): 52.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 36.5% | 2.74 |
| Draw | 28.8% | 3.48 |
| AS Roma win | 34.8% | 2.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.18 |
| AS Roma expected goals | 1.15 |
| Expected total goals | 2.33 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 67.9% |
| Under 1.5 | 32.1% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.7% |
| Under 3.5 | 79.3% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.52% |
| 2 | 1-0 | 11.18% |
| 3 | 0-1 | 10.85% |
| 4 | 0-0 | 10.04% |
| 5 | 2-1 | 7.81% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:00:00+00:00 |
| Fixture id | 0b4894e9fb123ef3045269f97e339eba |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1826 |
| Dc lambda away | 1.1485 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:42:05.183279+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 47.7% |
| P btts no | 52.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.96 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.12 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.83 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.44 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.203506657323829, "-10": 1.2088375431123852e-07, "-11": 1.2491297982755501e-08, "-12": 1.1798577198491414e-09, "-13": 9.437249280508465e-11, "-2": 0.09851471045600257, "-3": 0.03409058106217335, "-4": 0.00919003876709441, "-5": 0.002022126490078262, "-6": 0.0003752026422383206, "-7": 6.012597732259231e-05, "-8": 8.473993035227268e-06, "-9": 1.0654482840196794e-06, "0": 0.2877051374791582, "1": 0.2096456983505402, "10": 1.6199366181450074e-07, "11": 1.7236562564293085e-08, "12": 1.6764312128450166e-09, "13": 1.3807483563643703e-10, "2": 0.10445448733093504, "3": 0.037219748021458623, "4": 0.010331642655478647, "5": 0.002340848786008285, "6": 0.00044724339750315425, "7": 7.379946388067429e-05, "8": 1.0710066543771437e-05, "9": 1.3865944228674031e-06} |
| Raw goal margin distribution | {"-1": 0.203506657323829, "-10": 1.2088375431123852e-07, "-11": 1.2491297982755501e-08, "-12": 1.1798577198491414e-09, "-13": 9.437249280508465e-11, "-2": 0.09851471045600257, "-3": 0.03409058106217335, "-4": 0.00919003876709441, "-5": 0.002022126490078262, "-6": 0.0003752026422383206, "-7": 6.012597732259231e-05, "-8": 8.473993035227268e-06, "-9": 1.0654482840196794e-06, "0": 0.2877051374791582, "1": 0.2096456983505402, "10": 1.6199366181450074e-07, "11": 1.7236562564293085e-08, "12": 1.6764312128450166e-09, "13": 1.3807483563643703e-10, "2": 0.10445448733093504, "3": 0.037219748021458623, "4": 0.010331642655478647, "5": 0.002340848786008285, "6": 0.00044724339750315425, "7": 7.379946388067429e-05, "8": 1.0710066543771437e-05, "9": 1.3865944228674031e-06} |
| Unadjusted home-win probability | 36.5% |
| Unadjusted draw probability | 28.8% |
| Unadjusted away-win probability | 34.8% |
| Raw p over 1 5 | 67.9% |
| Raw p under 3 5 | 79.3% |
| Raw p btts yes | 47.7% |
| P home draw | 65.2% |
| P draw away | 63.5% |
| P home away | 71.2% |
| Raw p home draw | 65.2% |
| Raw p draw away | 63.5% |
| Raw p home away | 71.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.4122 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.10044045254214493, 0.1017504599922798, 0.05832551853150364, 0.021404743553023405, 0.005891457008520555, 0.0012972550910414751, 0.0002380382827766772, 3.74387589337549e-05, 5.152335466299637e-06, 6.302811195510286e-07, 6.939161144198962e-08, 6.945235285639642e-09, 6.372038515363957e-10, 5.396444502616425e-11, 4.2437750448399265e-12], [0.11512868221697599, 0.13558315470883098, 0.0723222310408921, 0.02654136384191175, 0.007305264070778285, 0.0016085649090731946, 0.0002951617082367367, 4.6423154764218455e-05, 6.388771251002858e-06, 7.81533330462557e-07, 8.604391836305217e-08, 8.611923624649466e-09, 7.901173505396259e-10, 6.691460546669152e-11, 5.262178322730343e-12], [0.07398431739335343, 0.08145398689742571, 0.044838907860776246, 0.016455324326678008, 0.004529175301340735, 0.0009972907736381857, 0.00018299668648459193, 2.87817940503301e-05, 3.960960846262076e-06, 4.845412052474194e-07, 5.334618791391559e-08, 5.3392884090006134e-09, 4.898631937946633e-10, 4.148624545839461e-11, 3.262486866956165e-12], [0.03057958752099618, 0.033666990641014895, 0.018533053430559488, 0.0068014012720922085, 0.001872022577283734, 0.00041220547233285204, 7.563715375862353e-05, 1.1896242625230002e-05, 1.6371651876103105e-06, 2.0027312159432813e-07, 2.2049327204736002e-08, 2.206862791404801e-09, 2.0247283391580456e-10, 1.714731335787764e-11, 1.3484682456926926e-12], [0.009479487064628981, 0.01043656334695024, 0.005745134401909136, 0.0021083932324424256, 0.0005803156695253051, 0.0001277812017662316, 2.3447059911057548e-05, 3.6877632180658677e-06, 5.075113000774462e-07, 6.20834556464434e-08, 6.835157991505105e-09, 6.84114109458443e-10, 6.276535315349852e-11, 5.3155633658411626e-12, 4.180169952694769e-13], [0.002350866896337805, 0.002588217180592575, 0.0014247655161485568, 0.0005228713136922827, 0.00014391547639783025, 3.168911937517929e-05, 5.814757337137819e-06, 9.145474234815611e-07, 1.258603452629034e-07, 1.539639641833221e-08, 1.6950860889324983e-09, 1.6965698695285017e-10, 1.5565503698620893e-11, 1.3182339790060187e-12, 1.0366619096431797e-13], [0.0004858363403190148, 0.0005348877747731098, 0.00029444579157444646, 0.0001080579618938799, 2.9741951140368782e-05, 6.548956816378268e-06, 1.2016930558335789e-06, 1.890027776411463e-07, 2.6010630218611115e-08, 3.18185980739101e-09, 3.503109526343427e-10, 3.5061759463764866e-11, 3.21680796302872e-12, 2.724297037157433e-13, 2.1423927875872075e-14], [8.606075727418078e-05, 9.474969888717818e-05, 5.215795051982588e-05, 1.91413224131927e-05, 5.268471346279082e-06, 1.1600782736905595e-06, 2.128671855387648e-07, 3.3479838416451286e-08, 4.607507401201195e-09, 5.636327335755538e-10, 6.205387156785166e-11, 6.2108189947986106e-12, 5.698234288568955e-13, 4.8258033951026683e-14, 3.795021705404569e-15], [1.3339156958749477e-05, 1.468591661613811e-05, 8.084324501283203e-06, 2.966847052648564e-06, 8.165971163464854e-07, 1.7980862204004827e-07, 3.2993769625133245e-08, 5.189273644987984e-09, 7.141497049278396e-10, 8.736136815878263e-11, 9.618162318796933e-12, 9.626581503351053e-13, 8.832090719442601e-14, 7.479849234216882e-15, 5.882168806506653e-16], [1.837803523989489e-06, 2.0233534543164006e-06, 1.1138185196769506e-06, 4.0875761379499663e-07, 1.1250673957448641e-07, 2.4773148726774873e-08, 4.545719513930343e-09, 7.149526331534195e-10, 9.839203844974315e-11, 1.2036220186871948e-11, 1.3251431599801071e-12, 1.326303113873035e-13, 1.216842076195808e-14, 1.0305368865561782e-15, 8.10416325014322e-17], [2.2788318803876885e-07, 2.5089093022193706e-07, 1.3811080011948948e-07, 5.0684954594339116e-08, 1.3950563352074689e-08, 3.071810471535647e-09, 5.636582154961708e-10, 8.865239576102013e-11, 1.220037458133029e-11, 1.492462166013701e-12, 1.6431454394455837e-13, 1.6445837541927695e-14, 1.5088547172945848e-15, 1.2778407921983728e-16, 1.0048966245424558e-17], [2.5688148781383866e-08, 2.8281698175753395e-08, 1.5568549888734398e-08, 5.713465156436044e-09, 1.5725782584332145e-09, 3.4627005660284227e-10, 6.353841293045125e-11, 9.993347695959822e-12, 1.3752881032211471e-12, 1.682379051350817e-13, 1.852236879832909e-14, 1.8538582211673947e-15, 1.700857566586358e-16, 1.4404469531700942e-17, 1.1327704436347197e-18], [2.6543902194036848e-09, 2.9223850914570515e-09, 1.608718748347605e-09, 5.903798735835013e-10, 1.6249658097032913e-10, 3.57805406431249e-11, 6.565507825197851e-12, 1.0326257687544849e-12, 1.4211032959673616e-13, 1.7384244140128667e-14, 1.9139407435269486e-15, 1.9156160968648632e-16, 1.7575185069845906e-17, 1.4884327931156416e-18, 1.1705066067635841e-19], [2.531830472964854e-10, 2.787451360467771e-10, 1.5344402340404024e-10, 5.631205779908443e-11, 1.5499371284818296e-11, 3.412846478908908e-12, 6.262362127773161e-13, 9.849468888898718e-14, 1.3554874500589655e-14, 1.6581570690584559e-15, 1.8255693765324204e-16, 1.827167374672599e-17, 1.6763695406408353e-18, 1.4197081781807377e-19, 1.1164614283714832e-20], [2.2424346401313573e-11, 2.468837291888056e-11, 1.3590491033130201e-11, 4.9875420338816256e-12, 1.3727746561416903e-12, 3.0227478685781277e-13, 5.5465553141559747e-14, 8.72364499092953e-15, 1.2005511604084962e-15, 1.4686247322401117e-16, 1.6169013097884976e-17, 1.6183166519382449e-18, 1.4847554635804727e-19, 1.2574312662814927e-20, 9.888465314263169e-22]] |
| Legacy trial inputs | {"lambda_home": 1.2399757921025316, "lambda_away": 1.1009628765560975, "rho": -0.03199263817223977, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3899 |
| Legacy p draw | 0.2883 |
| Legacy p away | 0.3218 |
| Legacy p over 1 5 | 0.6827 |
| Legacy p under 3 5 | 0.7910 |
| Legacy p btts yes | 0.4785 |
| Legacy p over 2 5 | 0.4148 |
| Legacy goal margin distribution | {"-1": 0.1925338275952252, "-10": 7.85109635907869e-08, "-11": 7.778187349883356e-09, "-12": 7.073809438700434e-10, "-13": 5.922662334889459e-11, "-14": 4.2437750448399265e-12, "-2": 0.08983265133843879, "-3": 0.02978675241965046, "-4": 0.007695438111011201, "-5": 0.0016228995726970314, "-6": 0.00028862967958938476, "-7": 4.4334820673047795e-05, "-8": 5.989485952478575e-06, "-9": 7.21872218386554e-07, "0": 0.28827715707199114, "1": 0.21737479836698023, "10": 2.5783128979532507e-07, "11": 2.8768965438278838e-08, "12": 2.946725846483592e-09, "13": 2.77871420215366e-10, "14": 2.2424346401313573e-11, "2": 0.1139502495004766, "3": 0.042554427261721935, "4": 0.012382133303269618, "5": 0.0029409951118181754, "6": 0.000589093424819883, "7": 0.0001019127863583491, "8": 1.5506500643234806e-05, "9": 2.104869185619816e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3899 |
| Legacy raw p draw | 0.2883 |
| Legacy raw p away | 0.3218 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.2400 |
| Legacy lambda away | 1.1010 |
| Legacy model home team | Napoli |
| Legacy model away team | Roma |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.268180376022777, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,561.4974 |
| Elo away rating | 1,592.1486 |
| Elo rating diff | 29.3488 |
| Elo home expectancy | 0.5421 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **58.6%**. Expected goals are 2.30 for Atalanta BC and 1.35 for Frosinone (3.66 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.3%; Double Chance 1X: 78.5%; Double Chance X2: 41.4%; Double Chance 12 (either team wins): 80.1%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 67.0%; BTTS No (at least one team does not score): 33.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 58.6% | 1.71 |
| Draw | 19.9% | 5.02 |
| Frosinone win | 21.5% | 4.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.30 |
| Frosinone expected goals | 1.35 |
| Expected total goals | 3.66 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 88.2% |
| Under 1.5 | 11.8% |
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 49.7% |
| Under 3.5 | 50.3% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.27% |
| 2 | 1-1 | 8.23% |
| 3 | 3-1 | 7.12% |
| 4 | 2-0 | 6.84% |
| 5 | 2-2 | 6.27% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 63aa6e3f679ee4c68de5b4bd8d3361bb |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3043 |
| Dc lambda away | 1.3540 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:42:05.183279+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 67.0% |
| P btts no | 33.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.10 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.46 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.42 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.28 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.12437750946630784, "-10": 1.9473089957175854e-07, "-11": 2.3426602186959803e-08, "-12": 2.5923206836099594e-09, "-13": 2.655146866196079e-10, "-14": 2.5307834801786447e-11, "-15": 2.2553873744417874e-12, "-16": 1.8858379192743052e-13, "-17": 1.469330291298465e-14, "-18": 9.41988351432074e-16, "-2": 0.060064224143051445, "-3": 0.022082384581356557, "-4": 0.006544383480149782, "-5": 0.0016152977994594, "-6": 0.00034050863420428257, "-7": 6.252105224757887e-05, "-8": 1.0155975386086683e-05, "-9": 1.478055513697273e-06, "0": 0.1993447426109059, "1": 0.21301674211219343, "10": 3.967742455942512e-05, "11": 8.123230331034219e-06, "12": 1.5297450281998682e-06, "13": 2.666427221357611e-07, "14": 4.3252083940789316e-08, "15": 6.559701113925844e-09, "16": 9.334222117557545e-10, "17": 1.2376677070484764e-10, "18": 1.3503334326539739e-11, "2": 0.17395527088415794, "3": 0.10883749825766376, "4": 0.054892395209706075, "5": 0.023057217890268232, "6": 0.008271671743748994, "7": 0.002584653334856373, "8": 0.0007145103485248064, "9": 0.00017696545207503145} |
| Raw goal margin distribution | {"-1": 0.12437750946630784, "-10": 1.9473089957175854e-07, "-11": 2.3426602186959803e-08, "-12": 2.5923206836099594e-09, "-13": 2.655146866196079e-10, "-14": 2.5307834801786447e-11, "-15": 2.2553873744417874e-12, "-16": 1.8858379192743052e-13, "-17": 1.469330291298465e-14, "-18": 9.41988351432074e-16, "-2": 0.060064224143051445, "-3": 0.022082384581356557, "-4": 0.006544383480149782, "-5": 0.0016152977994594, "-6": 0.00034050863420428257, "-7": 6.252105224757887e-05, "-8": 1.0155975386086683e-05, "-9": 1.478055513697273e-06, "0": 0.1993447426109059, "1": 0.21301674211219343, "10": 3.967742455942512e-05, "11": 8.123230331034219e-06, "12": 1.5297450281998682e-06, "13": 2.666427221357611e-07, "14": 4.3252083940789316e-08, "15": 6.559701113925844e-09, "16": 9.334222117557545e-10, "17": 1.2376677070484764e-10, "18": 1.3503334326539739e-11, "2": 0.17395527088415794, "3": 0.10883749825766376, "4": 0.054892395209706075, "5": 0.023057217890268232, "6": 0.008271671743748994, "7": 0.002584653334856373, "8": 0.0007145103485248064, "9": 0.00017696545207503145} |
| Unadjusted home-win probability | 58.6% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 21.5% |
| Raw p over 1 5 | 88.2% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 67.0% |
| P home draw | 78.5% |
| P draw away | 41.4% |
| P home away | 80.1% |
| Raw p home draw | 78.5% |
| Raw p draw away | 41.4% |
| Raw p home away | 80.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.7074 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.02915482150013908, 0.03074704437095393, 0.02079483623537921, 0.008663239551089184, 0.002706863809963562, 0.0006766163297210697, 0.00014094098367025377, 2.5164327685162884e-05, 3.9313473621116496e-06, 5.459400845319966e-07, 6.823246424219279e-08, 7.752547658733658e-09, 8.074381632371252e-10, 7.762685540298888e-11, 6.929948889457913e-12, 5.774107247263301e-13, 4.510357196719877e-14, 3.3159508854995407e-15, 2.302404671971283e-16], [0.060734083735523435, 0.08159754592451729, 0.04941019594054898, 0.020584550840124675, 0.006431725151416734, 0.001607694576176281, 0.00033488706236372824, 5.9792457490993344e-05, 9.341196115880577e-06, 1.2971973543428059e-06, 1.6212579842188733e-07, 1.8420673984667663e-08, 1.9185377275319428e-09, 1.8444762403008168e-10, 1.646611344327623e-11, 1.3719741153028654e-12, 1.0716969844303772e-13, 7.878964812572924e-15, 5.470697854450399e-16], [0.07515978004684276, 0.09393589424549242, 0.0587012909178345, 0.024455270501922397, 0.00764114697442489, 0.0019100055206561065, 0.00039785923731379923, 7.103583329429023e-05, 1.1097714961070421e-05, 1.5411223903411267e-06, 1.9261193924226441e-07, 2.188449816668644e-08, 2.2792996290927553e-09, 2.1913116172056384e-10, 1.956240199255288e-11, 1.6299601760542481e-12, 1.2732189229629383e-13, 9.360525632213994e-15, 6.499408070837492e-16], [0.05952855181494281, 0.07439973539558917, 0.04649298914696774, 0.019369226949770498, 0.006051992346294169, 0.0015127753504911975, 0.00031511513483311503, 5.6262275918600546e-05, 8.789686447669398e-06, 1.2206100657747209e-06, 1.5255379670102432e-07, 1.733310664623665e-08, 1.8052661408490602e-09, 1.735577287030547e-10, 1.5493944499473592e-11, 1.2909719631439306e-12, 1.0084233692558389e-13, 7.413786133555325e-15, 5.147704661591272e-16], [0.03536115139283049, 0.04419493212414353, 0.027617766228246535, 0.011505708532304652, 0.0035950045996556578, 0.0008986188402223748, 0.0001871846979185022, 3.3420918127617426e-05, 5.221249697754749e-06, 7.250668126725393e-07, 9.062000899107862e-08, 1.0296212313900037e-08, 1.0723642246390133e-09, 1.0309676504718807e-10, 9.203713183233691e-12, 7.668631881814573e-13, 5.990236674861092e-14, 4.4039373690409534e-15, 3.0578396133335054e-16], [0.01680418541628693, 0.021002139484205214, 0.013124404783301758, 0.005467696947271989, 0.001708403756255133, 0.00042703806337955266, 8.895316603157667e-05, 1.5882155497710843e-05, 2.481221469603844e-06, 3.445633606211104e-07, 4.306407946378189e-08, 4.8929249753816785e-09, 5.096046524175219e-10, 4.899323374474665e-11, 4.3737518931790496e-12, 3.644256675912113e-13, 2.8466563957025733e-14, 2.0928215625377944e-15, 1.4531343525805443e-16], [0.006654681677074461, 0.008317127509759683, 0.005197439439658663, 0.0021652809576560073, 0.0006765506861628225, 0.0001691127719306729, 3.522664083046606e-05, 6.28954552480874e-06, 9.825968139183337e-07, 1.3645168901160326e-07, 1.7053950158747437e-08, 1.9376635864428076e-09, 2.0181024304265963e-10, 1.9401974378704075e-11, 1.7320641175143395e-12, 1.4431742763468762e-13, 1.1273139213905756e-14, 8.287852675148559e-16, 5.754605957318657e-17], [0.0022588652151387216, 0.0028231658452412653, 0.0017642188954703434, 0.0007349829899604806, 0.00022964837168939966, 5.740364099847095e-05, 1.1957331316425464e-05, 2.1349233959553836e-06, 3.335326723609749e-07, 4.6317162685193944e-08, 5.78879301274699e-09, 6.577205471953973e-10, 6.850247092031629e-11, 6.585806377493682e-12, 5.879318614024383e-13, 4.898710908221972e-14, 3.826554487712583e-15, 2.813228795087564e-16, 1.953343503807046e-17], [0.0006709055773507707, 0.000838508512444488, 0.0005239906696097318, 0.0002182973042914158, 6.820786488868887e-05, 1.7049455916186835e-05, 3.5514470791158802e-06, 6.340936165485873e-07, 9.906254194185869e-08, 1.375666089517044e-08, 1.719329463463635e-09, 1.9534958548843458e-10, 2.0345919488572393e-11, 1.956050409914095e-12, 1.7462164730926294e-13, 1.4549661697957244e-14, 1.136524981941135e-15, 8.355571090912236e-17, 5.801625711897832e-18], [0.00017712504125375048, 0.00022137370722840106, 0.00013833819855499444, 5.7632430454492675e-05, 1.80074831542543e-05, 4.501208045450041e-06, 9.376136249796365e-07, 1.6740635609768845e-07, 2.6153392400521463e-08, 3.6318808649536135e-09, 4.539182746807958e-10, 5.157402853196342e-11, 5.3715037561458595e-12, 5.1641471057455e-13, 4.610166844280078e-14, 3.841240131964793e-15, 3.000527065330862e-16, 2.2059451048544407e-17, 1.5316808031563797e-18], [4.2086328044439286e-05, 5.2600165379670005e-05, 3.287026365245233e-05, 1.369392693962042e-05, 4.278722183606625e-06, 1.0695230728312876e-06, 2.2278450477985878e-07, 3.9777090633718355e-08, 6.214255444922786e-09, 8.629639740311036e-10, 1.078546165937865e-10, 1.2254402133123139e-11, 1.2763123021618813e-12, 1.2270427017193134e-13, 1.0954125558678482e-14, 9.1270941221538e-16, 7.129492559825133e-17, 5.24150219945048e-18, 3.6393962301840645e-19], [9.090953208312835e-06, 1.1362018604026864e-05, 7.100216214962296e-06, 2.9579878984617747e-06, 9.242351369182313e-07, 2.310247689000955e-07, 4.812307470379188e-08, 8.5921411184203e-09, 1.3423244103083632e-09, 1.8640649999431368e-10, 2.3297382269113972e-11, 2.6470400618091192e-12, 2.756927476755897e-13, 2.6505015534150186e-14, 2.366170856882045e-15, 1.9715187674428239e-16, 1.5400222892324386e-17, 1.1322026285153419e-18, 7.861360772595348e-20], [1.800069394731435e-06, 2.2497554967917005e-06, 1.4058901868334962e-06, 5.857013411022904e-07, 1.8300472407894894e-07, 4.574444575753604e-08, 9.528689893097223e-09, 1.7013012726035452e-09, 2.657891899154804e-10, 3.6909730798300116e-11, 4.6130371413245696e-12, 5.24131594642197e-13, 5.4589003602664646e-14, 5.2481699307700594e-15, 4.685176179637702e-16, 3.903738709343874e-17, 3.0493468908372375e-18, 2.24183675080557e-19, 1.5566018879902917e-20], [3.2900838566741773e-07, 4.11199938353638e-07, 2.569621272099701e-07, 1.0705179104945367e-07, 3.344875981723435e-08, 8.360958914132943e-09, 1.741610011496858e-09, 3.1095600362492004e-10, 4.8579722847290404e-11, 6.7461904418298715e-12, 8.431496626370209e-13, 9.579835662738249e-14, 9.977526423743878e-15, 9.592363059361707e-16, 8.563349034996629e-17, 7.135073650981438e-18, 5.573455672490906e-19, 4.097525864676316e-20, 2.8450851716800032e-21], [5.583930486362436e-08, 6.978885559726394e-08, 4.3611613517314394e-08, 1.81688305131836e-08, 5.67692368374082e-09, 1.4190219887904277e-09, 2.955860598757506e-10, 5.2775454492939193e-11, 8.244950804999698e-12, 1.1449634755820524e-12, 1.4309936496646914e-13, 1.6258897566696193e-14, 1.6933858346197056e-15, 1.628015906487308e-16, 1.453371641117275e-17, 1.2109647357873463e-18, 9.459269246550901e-20, 6.95432110279205e-21, 4.828678695898349e-22], [8.84524396109986e-09, 1.1054927260133195e-08, 6.90831238032013e-09, 2.8780397386657777e-09, 8.992550149732298e-10, 2.247806577762931e-10, 4.682240972531304e-11, 8.359913707523034e-12, 1.3060442191320544e-12, 1.8136832635732625e-13, 2.2667703276360776e-14, 2.5754961647032617e-15, 2.682413555122791e-16, 2.578864099508545e-17, 2.302218260636127e-18, 1.9182327828915377e-19, 1.498398742316314e-20, 1.1016015849096316e-21, 7.648884809597571e-23], [1.313562993214199e-09, 1.6417120212227756e-09, 1.0259189603204171e-09, 4.274033040057773e-10, 1.3354386994027413e-10, 3.3381052568342e-11, 6.953362161492727e-12, 1.2414890217794404e-12, 1.93954102486946e-13, 2.6934104100680495e-14, 3.366267374414548e-15, 3.824740692283447e-16, 3.9835183676124435e-17, 3.8297422440136584e-18, 3.4189093288700488e-19, 2.8486716783143385e-20, 2.2251971179556566e-21, 1.6359334819561849e-22, 1.1358976721763901e-23], [1.835959322964448e-10, 2.2946113026611884e-10, 1.4339209383459838e-10, 5.973791015040091e-11, 1.8665348697260154e-11, 4.665650219275022e-12, 9.718673677843988e-13, 1.7352219540812636e-13, 2.710885161409565e-14, 3.764563997676179e-15, 4.7050122465193675e-16, 5.345817724916845e-17, 5.567740354288117e-18, 5.352808364555605e-19, 4.7785895987749716e-20, 3.981571765407631e-21, 3.11014501417072e-22, 2.2865346720812923e-23, 1.5876375415105709e-24], [2.42354797603854e-11, 3.028988991640839e-11, 1.8928394243051468e-11, 7.885669874428901e-12, 2.4639090578682943e-12, 6.158865833459813e-13, 1.2829081574469029e-13, 2.290570167971375e-14, 3.578489002468104e-15, 4.969391937564366e-16, 6.210825460379421e-17, 7.05671719707488e-18, 7.349664939719564e-19, 7.06594515236551e-20, 6.307950838328112e-21, 5.2558518442146975e-22, 4.105529768551285e-23, 3.018327479999332e-24, 2.0957521783205957e-25]] |
| Legacy trial inputs | {"lambda_home": 2.3760800701322737, "lambda_away": 1.2498159811929679, "rho": -0.03199263817223977, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6212 |
| Legacy p draw | 0.1929 |
| Legacy p away | 0.1859 |
| Legacy p over 1 5 | 0.8794 |
| Legacy p under 3 5 | 0.5097 |
| Legacy p btts yes | 0.6497 |
| Legacy p over 2 5 | 0.7018 |
| Legacy goal margin distribution | {"-1": 0.1116587124672852, "-10": 8.911557528377082e-08, "-11": 9.906506670556479e-09, "-12": 1.0128012139572743e-09, "-13": 9.582832061004925e-11, "-14": 8.43696446715196e-12, "-15": 6.94455719267741e-13, "-16": 5.363247758685545e-14, "-17": 3.8630206709445806e-15, "-18": 2.302404671971283e-16, "-2": 0.050737406940019575, "-3": 0.017356129938920585, "-4": 0.004774263444974814, "-5": 0.0010920990508880317, "-6": 0.00021314748769664347, "-7": 3.621002580981321e-05, "-8": 5.439612902011515e-06, "-9": 7.318632660074292e-07, "0": 0.19288239232450302, "1": 0.21455881065359506, "10": 5.496719746115347e-05, "11": 1.16167732936683e-05, "12": 2.257897324152028e-06, "13": 4.061522381842882e-07, "14": 6.798235290328624e-08, "15": 1.0638233746031664e-08, "16": 1.5619525177233692e-09, "17": 2.138858222128532e-10, "18": 2.42354797603854e-11, "2": 0.18338265820391944, "3": 0.11926084627845913, "4": 0.06236865402891599, "5": 0.02712295600615918, "6": 0.010063990217408095, "7": 0.0032503776283794223, "8": 0.0009282992059568332, "9": 0.00023744604006279563} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.6212 |
| Legacy raw p draw | 0.1929 |
| Legacy raw p away | 0.1859 |
| Legacy market weight | 0 |
| Legacy lambda home | 2.3761 |
| Legacy lambda away | 1.2498 |
| Legacy model home team | Atalanta |
| Legacy model away team | Frosinone |
| Legacy home name match score | 95/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 10.22359017061284, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,509.3950 |
| Elo away rating | 1,444.8076 |
| Elo rating diff | 124.5874 |
| Elo home expectancy | 0.6720 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **49.9%**. Expected goals are 1.38 for Genoa and 0.82 for Venezia (2.20 combined). The most likely exact score is 1-0 at 15.0%. Goal-market probabilities: at least one goal: 88.6%; Over 2.5 goals: 37.7%; Under 3.5 goals: 81.9%; Double Chance 1X: 78.1%; Double Chance X2: 50.1%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 92.7%; BTTS Yes (both teams score): 42.2%; BTTS No (at least one team does not score): 57.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 49.9% | 2.01 |
| Draw | 28.2% | 3.54 |
| Venezia win | 21.9% | 4.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.38 |
| Venezia expected goals | 0.82 |
| Expected total goals | 2.20 |
| Over 0.5 | 88.6% |
| Under 0.5 | 11.4% |
| Over 1.5 | 64.8% |
| Under 1.5 | 35.2% |
| Over 2.5 | 37.7% |
| Under 2.5 | 62.3% |
| Over 3.5 | 18.1% |
| Under 3.5 | 81.9% |
| Over 4.5 | 7.3% |
| Under 4.5 | 92.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.01% |
| 2 | 1-1 | 12.83% |
| 3 | 0-0 | 11.38% |
| 4 | 2-0 | 10.58% |
| 5 | 0-1 | 8.77% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 95cfaecfe96bb7ced1fb6af974a4110b |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3818 |
| Dc lambda away | 0.8184 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:42:05.183279+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 42.2% |
| P btts no | 57.8% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.79 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.84 |
| Fair Over 2.5 odds | 2.65 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.53 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.79 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.14954679284577008, "-10": 4.555915990142659e-09, "-11": 3.3608214951261175e-10, "-12": 2.27537616980128e-11, "-13": 1.4195818288261257e-12, "-14": 7.677838699932425e-14, "-2": 0.053210992502778345, "-3": 0.013324444604899193, "-4": 0.0025850446678192603, "-5": 0.00040810885176632735, "-6": 5.423127304993382e-05, "-7": 6.216445209600817e-06, "-8": 6.261929343480126e-07, "-9": 5.623915254270465e-08, "0": 0.28224484972595615, "1": 0.25458272911249225, "10": 8.585308668968107e-07, "11": 1.0694086034677939e-07, "12": 1.2225579484712436e-08, "13": 1.2879372390786284e-09, "14": 1.1762273500476447e-10, "2": 0.15171810196405658, "3": 0.06415096263402537, "4": 0.021015519712031368, "5": 0.005602296861232153, "6": 0.0012570655465536638, "7": 0.0002433146479668936, "8": 4.138589279266728e-05, "9": 6.276260398243076e-06} |
| Raw goal margin distribution | {"-1": 0.14954679284577008, "-10": 4.555915990142659e-09, "-11": 3.3608214951261175e-10, "-12": 2.27537616980128e-11, "-13": 1.4195818288261257e-12, "-14": 7.677838699932425e-14, "-2": 0.053210992502778345, "-3": 0.013324444604899193, "-4": 0.0025850446678192603, "-5": 0.00040810885176632735, "-6": 5.423127304993382e-05, "-7": 6.216445209600817e-06, "-8": 6.261929343480126e-07, "-9": 5.623915254270465e-08, "0": 0.28224484972595615, "1": 0.25458272911249225, "10": 8.585308668968107e-07, "11": 1.0694086034677939e-07, "12": 1.2225579484712436e-08, "13": 1.2879372390786284e-09, "14": 1.1762273500476447e-10, "2": 0.15171810196405658, "3": 0.06415096263402537, "4": 0.021015519712031368, "5": 0.005602296861232153, "6": 0.0012570655465536638, "7": 0.0002433146479668936, "8": 4.138589279266728e-05, "9": 6.276260398243076e-06} |
| Unadjusted home-win probability | 49.9% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 21.9% |
| Raw p over 1 5 | 64.8% |
| Raw p under 3 5 | 81.9% |
| Raw p btts yes | 42.2% |
| P home draw | 78.1% |
| P draw away | 50.1% |
| P home away | 71.8% |
| Raw p home draw | 78.1% |
| Raw p draw away | 50.1% |
| Raw p home away | 71.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.3773 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.11554702778473104, 0.08786448075521386, 0.037858039607358354, 0.010398078756897546, 0.002141950090839404, 0.00035298445406396056, 4.847530658460388e-05, 5.706091880454832e-06, 5.877126105421475e-07, 5.3806994711644754e-08, 4.433584315139022e-09, 3.321073772317335e-10, 2.2804130245633765e-11, 1.4453944956306322e-12, 8.506964036604491e-14], [0.1487086734007859, 0.12987671409145085, 0.051849065519521814, 0.014240850089837708, 0.0029335409797049267, 0.00048343533568963884, 6.639010823728737e-05, 7.81486666606502e-06, 8.049109242499229e-07, 7.369220443391314e-08, 6.07208418677038e-09, 4.54842811201925e-10, 3.123175038867463e-11, 1.9795624570835542e-12, 1.1650844583626854e-13], [0.10459026748354909, 0.08618020239121484, 0.0355053460655837, 0.009751888595126405, 0.0020088382816230064, 0.000331048182296161, 4.5462801396274556e-05, 5.351485945885796e-06, 5.511891223324388e-07, 5.046315096608048e-08, 4.1580585538126595e-09, 3.114685145306402e-10, 2.138696415591731e-11, 1.3555702382085476e-12, 7.978297482377036e-14], [0.04774774119052916, 0.03934314442947935, 0.016208965858953518, 0.004451950109336964, 0.0009170785453785117, 0.00015113072478142818, 2.0754761672324626e-05, 2.4430702021973494e-06, 2.5162987143429713e-07, 2.3037530450584235e-08, 1.8982445351690177e-09, 1.4219217885781554e-10, 9.763616194293453e-12, 6.188474172297752e-13, 3.6422670339714716e-14], [0.016348414940876438, 0.01347075346759103, 0.005549810169391492, 0.0015243093362908107, 0.000313999787621307, 5.1745857237164175e-05, 7.1062514656811395e-06, 8.364861750389021e-07, 8.615589862800146e-08, 7.887851815154175e-09, 6.499425636986932e-10, 4.868537617389904e-11, 3.3429780108515587e-12, 2.118880204529719e-13, 1.2470808317242828e-14], [0.004478045066258934, 0.0036898158826095067, 0.0015201657247870721, 0.00041752830029793443, 8.600865618159834e-05, 1.417386832535336e-05, 1.94649538995508e-06, 2.2912452385588574e-07, 2.3599229538490263e-08, 2.1605859670172474e-09, 1.7802778442119633e-10, 1.3335562460515886e-11, 9.156854803505119e-13, 5.803890517950944e-14, 3.415917803606732e-15], [0.0010221626830473906, 0.0008422407650465849, 0.0003469944256776237, 9.530539361840257e-05, 1.963241491924718e-05, 3.235340212577905e-06, 4.44308826931492e-07, 5.2300174426816674e-08, 5.386781826889195e-09, 4.931773388439568e-10, 4.0636785715284776e-11, 3.0439877452985842e-12, 2.0901520944374012e-13, 1.3248013845689624e-14, 7.797205377660466e-16], [0.00019998839451880438, 0.00016478627247258518, 6.789022848237278e-05, 1.8646711501835714e-05, 3.841125493372401e-06, 6.330014835863306e-07, 8.693000678096828e-08, 1.0232645047742917e-08, 1.0539358040061568e-09, 9.649123945164264e-11, 7.950677194921328e-12, 5.955629492384384e-13, 4.0894289001085764e-14, 2.5920032725744915e-15, 1.5255405143169443e-16], [3.4237151071783255e-05, 2.8210699519713638e-05, 1.162251446860995e-05, 3.1922366306124813e-06, 6.575841269124414e-07, 1.083671253742194e-07, 1.4882042440474241e-08, 1.7517847233408725e-09, 1.8042926655090114e-10, 1.6518884259050712e-11, 1.3611216635868757e-12, 1.019578096763807e-13, 7.000925998091801e-15, 4.437397871772264e-16, 2.611659600571676e-17], [5.21000238297725e-06, 4.292933469113785e-06, 1.7686438906872364e-06, 4.857752450736269e-07, 1.0006717150731051e-07, 1.6490653099386826e-08, 2.2646591246997968e-09, 2.6657599412794005e-10, 2.7456633489103866e-11, 2.5137438034296398e-12, 2.0712725471641353e-13, 1.551532223762848e-14, 1.0653585357213505e-15, 6.752563447139506e-17, 3.974265473775921e-18], [7.1354395978641e-07, 5.879453638369738e-07, 2.422273681364118e-07, 6.653010237933378e-08, 1.3704854730056644e-08, 2.258502980813683e-09, 3.1015990408843046e-10, 3.650932887392495e-11, 3.760365839031301e-12, 3.4427368272387375e-13, 2.8367434531878492e-14, 2.1249250293956936e-15, 1.4590783118537842e-16, 9.248078036439417e-18, 5.4430169411553345e-19], [8.884047280969486e-08, 7.32026995578243e-08, 3.0158750021692354e-08, 8.283393994711507e-09, 1.7063360390169538e-09, 2.811970725919307e-10, 3.86167553489962e-11, 4.5456288917294436e-12, 4.681879434267316e-13, 4.2864123968310475e-14, 3.5319145536100285e-15, 2.6456582205976043e-16, 1.8166393999083558e-17, 1.1514407964215248e-18, 6.776880273896039e-20], [1.013940399289248e-08, 8.354657744528742e-09, 3.442032000951076e-09, 9.453875636680994e-10, 1.9474491636583023e-10, 3.209315113322045e-11, 4.407348036259387e-12, 5.187947145862027e-13, 5.3434505162686175e-14, 4.892102168874289e-15, 4.0309903127305955e-16, 3.019501886625349e-17, 2.0733388963984118e-18, 1.3141446729830618e-19, 7.734484603170336e-21], [1.0681983118001905e-09, 8.801731644808547e-10, 3.626221792874132e-10, 9.959770813107472e-11, 2.051660936278615e-11, 3.3810517743336134e-12, 4.643193756899637e-13, 5.4655642351395534e-14, 5.629388891760395e-15, 5.153888021040192e-16, 4.246696403417885e-17, 3.181081274630784e-18, 2.1842872721857615e-19, 1.3844670970066217e-20, 8.148371838761519e-22], [1.0449768366016177e-10, 8.61039152487336e-11, 3.547391655719317e-11, 9.743256174987256e-12, 2.0070600480152885e-12, 3.3075513680368994e-13, 4.542255749905126e-14, 5.346748783991153e-15, 5.507012069882786e-16, 5.041848073462375e-17, 4.15437781976309e-18, 3.1119280105716097e-19, 2.1368032309199224e-20, 1.35437028071209e-21, 7.971235053885246e-23]] |
| Legacy trial inputs | {"lambda_home": 1.3695655152054957, "lambda_away": 0.8239791757370738, "rho": -0.03199263817223977, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4927 |
| Legacy p draw | 0.2857 |
| Legacy p away | 0.2215 |
| Legacy p over 1 5 | 0.6479 |
| Legacy p under 3 5 | 0.8206 |
| Legacy p btts yes | 0.4226 |
| Legacy p over 2 5 | 0.3756 |
| Legacy goal margin distribution | {"-1": 0.15043625913870615, "-10": 4.9104454087224114e-09, "-11": 3.647311205289564e-10, "-12": 2.4863475677541092e-11, "-13": 1.5619029414669007e-12, "-14": 8.506964036604491e-14, "-2": 0.05426619956423988, "-3": 0.013684283267206583, "-4": 0.002673379655851527, "-5": 0.00042498574708349734, "-6": 5.686506339321141e-05, "-7": 6.563413814668227e-06, "-8": 6.657084675053677e-07, "-9": 6.020052633307834e-08, "0": 0.28570966643149287, "1": 0.25271148369323526, "10": 7.902902961133645e-07, "11": 9.756749598968599e-08, "12": 1.105505107393053e-08, "13": 1.154302227048924e-09, "14": 1.0449768366016177e-10, "2": 0.14992103095154274, "3": 0.062837917570786, "4": 0.0204045463502049, "5": 0.005391470661234222, "6": 0.0011990712357480165, "7": 0.00023003600693044087, "8": 3.878079347441886e-05, "9": 5.829072731764084e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.4927 |
| Legacy raw p draw | 0.2857 |
| Legacy raw p away | 0.2215 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.3696 |
| Legacy lambda away | 0.8240 |
| Legacy model home team | Genoa |
| Legacy model away team | Venezia |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 9.218525691843759, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,403.5919 |
| Elo away rating | 1,357.5227 |
| Elo rating diff | 106.0692 |
| Elo home expectancy | 0.6481 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **70.6%**. Expected goals are 2.47 for Inter Milan and 0.94 for Fiorentina (3.41 combined). The most likely exact score is 2-0 at 10.1%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 66.1%; Under 3.5 goals: 55.7%; Double Chance 1X: 87.8%; Double Chance X2: 29.4%; Double Chance 12 (either team wins): 82.8%; Under 4.5 goals: 74.3%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.6% | 1.42 |
| Draw | 17.2% | 5.83 |
| Fiorentina win | 12.2% | 8.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.47 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.41 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.6% |
| Under 1.5 | 14.4% |
| Over 2.5 | 66.1% |
| Under 2.5 | 33.9% |
| Over 3.5 | 44.3% |
| Under 3.5 | 55.7% |
| Over 4.5 | 25.7% |
| Under 4.5 | 74.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.09% |
| 2 | 2-1 | 9.48% |
| 3 | 3-0 | 8.29% |
| 4 | 1-0 | 8.00% |
| 5 | 1-1 | 7.88% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T11:30:00+00:00 |
| Fixture id | c9b6c7048d8dc33dae618f67f462f67a |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4653 |
| Dc lambda away | 0.9398 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:42:05.183279+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.54 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.92 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.95 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.89 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.0825052022908577, "-10": 6.061165316942015e-09, "-11": 5.090517146239095e-10, "-12": 3.92919835647063e-11, "-13": 2.8052579786827036e-12, "-14": 1.862821663719527e-13, "-15": 1.156071151124604e-14, "-16": 6.731643012799006e-16, "-17": 3.6683930274007125e-17, "-18": 1.6969290697260034e-18, "-2": 0.029826311123476605, "-3": 0.007957131581114227, "-4": 0.0016874468586216304, "-5": 0.00029550767370443564, "-6": 4.3956220169734804e-05, "-7": 5.673980607223612e-06, "-8": 6.462828813372369e-07, "-9": 6.582780205130862e-08, "0": 0.17166529955511697, "1": 0.21941319794074926, "10": 9.350859962285632e-05, "11": 2.0600932095354685e-05, "12": 4.171175491642356e-06, "13": 7.811903268708738e-07, "14": 1.3607704602835847e-07, "15": 2.2152752697618688e-08, "16": 3.3837148282058447e-09, "17": 4.837022187072276e-10, "18": 5.869423574557552e-11, "2": 0.20523840385414321, "3": 0.14363000209543722, "4": 0.07990027504110235, "5": 0.036704260190977306, "6": 0.014321799656298716, "7": 0.004849474093886057, "8": 0.0014489686576586488, "9": 0.0003871464094357415} |
| Raw goal margin distribution | {"-1": 0.0825052022908577, "-10": 6.061165316942015e-09, "-11": 5.090517146239095e-10, "-12": 3.92919835647063e-11, "-13": 2.8052579786827036e-12, "-14": 1.862821663719527e-13, "-15": 1.156071151124604e-14, "-16": 6.731643012799006e-16, "-17": 3.6683930274007125e-17, "-18": 1.6969290697260034e-18, "-2": 0.029826311123476605, "-3": 0.007957131581114227, "-4": 0.0016874468586216304, "-5": 0.00029550767370443564, "-6": 4.3956220169734804e-05, "-7": 5.673980607223612e-06, "-8": 6.462828813372369e-07, "-9": 6.582780205130862e-08, "0": 0.17166529955511697, "1": 0.21941319794074926, "10": 9.350859962285632e-05, "11": 2.0600932095354685e-05, "12": 4.171175491642356e-06, "13": 7.811903268708738e-07, "14": 1.3607704602835847e-07, "15": 2.2152752697618688e-08, "16": 3.3837148282058447e-09, "17": 4.837022187072276e-10, "18": 5.869423574557552e-11, "2": 0.20523840385414321, "3": 0.14363000209543722, "4": 0.07990027504110235, "5": 0.036704260190977306, "6": 0.014321799656298716, "7": 0.004849474093886057, "8": 0.0014489686576586488, "9": 0.0003871464094357415} |
| Unadjusted home-win probability | 70.6% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 85.6% |
| Raw p under 3 5 | 55.7% |
| Raw p btts yes | 55.9% |
| P home draw | 87.8% |
| P draw away | 29.4% |
| P home away | 82.8% |
| Raw p home draw | 87.8% |
| Raw p draw away | 29.4% |
| Raw p home away | 82.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.6613 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.03890409995097198, 0.03145665438081873, 0.015960692087208135, 0.004988097970711102, 0.0011691749281357976, 0.0002192370752311382, 3.425841448760029e-05, 4.5885316300377725e-06, 5.377597002203061e-07, 5.602092220777321e-08, 5.2523633722484136e-09, 4.4767886235301295e-10, 3.497758763579932e-11, 2.5226152179154514e-12, 1.6893805348185626e-13, 1.0559436359581205e-14, 6.187643225614068e-16, 3.4125643817206464e-17, 1.7775132989611494e-18], [0.08376359545571069, 0.08355311070705197, 0.03795426091535153, 0.011861614196757598, 0.002780278576623778, 0.0005213421266556548, 8.146594113238621e-05, 1.091145206944846e-05, 1.2787836429900645e-06, 1.332168233416724e-07, 1.2490032936123284e-08, 1.0645729054350887e-09, 8.31761229441096e-11, 5.998737125348995e-12, 4.0173188764921313e-13, 2.5110164429009977e-14, 1.4714112906437473e-15, 8.115021468152184e-17, 4.2268971270580806e-18], [0.10267396598552919, 0.09626420932982195, 0.04512730130246373, 0.014103360858073073, 0.003305728158214201, 0.0006198714627516555, 9.686232804188216e-05, 1.2973625972683006e-05, 1.520463140794119e-06, 1.5839369758522025e-07, 1.4850545524867608e-08, 1.2657683512571577e-09, 9.889572002576924e-11, 7.13244866745397e-12, 4.776558810402444e-13, 2.9855777154232734e-14, 1.7494958155243642e-15, 9.648693191154804e-17, 5.0257456113475645e-18], [0.08138566241230283, 0.0763048974265622, 0.03577065786957346, 0.011179186024973387, 0.002620322233867763, 0.0004913480172143812, 7.677900288372428e-05, 1.0283689088479123e-05, 1.2052120388966006e-06, 1.2555252810360875e-07, 1.1771450271003967e-08, 1.0033253779454775e-09, 7.839079368155751e-11, 5.6536148560220265e-12, 3.786192528013513e-13, 2.3665514205166558e-14, 1.386757338798716e-15, 7.648144096098174e-17, 3.983713220475899e-18], [0.04838343865490827, 0.0453629449497366, 0.02126550769975171, 0.006645979712138378, 0.0015577706969583888, 0.00029210435775121386, 4.5644798677071885e-05, 6.113610498590283e-06, 7.164935569940842e-07, 7.464045707086746e-08, 6.998078349244075e-09, 5.964727746370147e-10, 4.6603001619457964e-11, 3.361050576439976e-12, 2.2508757499173674e-13, 1.4069050012541854e-14, 8.244214845988499e-16, 4.546789934851307e-17, 2.3683009821212185e-18], [0.023011002839432776, 0.021574466058284763, 0.01011380488169013, 0.003160805893057681, 0.000740870573225747, 0.00013892386305085395, 2.170851475553169e-05, 2.907612862029923e-06, 3.407619576611802e-07, 3.549875365090558e-08, 3.328262836248255e-09, 2.836804719216523e-10, 2.2164232894650812e-11, 1.5985044988134915e-12, 1.0705090359943768e-13, 6.691193490727228e-15, 3.920921218167495e-16, 2.1624382021998754e-17, 1.1263560866956761e-18], [0.009119963814013789, 0.008550620376311937, 0.004008410028308164, 0.0012527239933415332, 0.0002936296547279475, 5.5059773481737856e-05, 8.603747972563964e-06, 1.1523758556681669e-06, 1.350543800610416e-07, 1.4069241179878503e-08, 1.3190922986674668e-09, 1.1243124242435657e-10, 8.784363001259453e-12, 6.335361951603083e-13, 4.242754537456813e-14, 2.651924513408176e-15, 1.5539809315050207e-16, 8.570403598537832e-18, 4.464093470431278e-19], [0.0030981603719612296, 0.0029047476224486053, 0.0013617046468094212, 0.00042556526674064, 9.97494923075152e-05, 1.8704461088777747e-05, 2.9227956999105646e-06, 3.914758087252462e-07, 4.5879582079258174e-08, 4.77948886377004e-09, 4.4811137083801303e-10, 3.819423266946102e-11, 2.984152777185932e-12, 2.1521979407777016e-13, 1.4413142687813217e-14, 9.008903548771642e-16, 5.2790583811026665e-17, 2.9114682187557733e-18, 1.5165057415654514e-19], [0.0009209217438107009, 0.0008634302052291669, 0.00040476388157435235, 0.00012649839275555763, 2.9650329670286847e-05, 5.559862258522286e-06, 8.687949588162049e-07, 1.1636537207489322e-07, 1.3637610601477718e-08, 1.4206931502905461e-09, 1.3320017542936634e-10, 1.1353156431732916e-11, 8.870332227585554e-13, 6.397363734247658e-14, 4.284276765650755e-15, 2.6778778920037826e-16, 1.5691891530218053e-17, 8.654278885404176e-19, 4.507781858746441e-20], [0.00024332629156284977, 0.00022813585548800918, 0.00010694686592427402, 3.342345319212892e-05, 7.8342213231202e-06, 1.469028909414657e-06, 2.2955333271042864e-07, 3.074610263424856e-08, 3.603334632652442e-09, 3.753760816619391e-10, 3.5194200745694363e-11, 2.9997352876427836e-12, 2.343722537093759e-13, 1.6903138661835328e-14, 1.1319932278946863e-15, 7.075499097492919e-17, 4.1461175168422425e-18, 2.2866368412829327e-19, 1.1910478281513197e-20], [5.7862588333139994e-05, 5.425032784310434e-05, 2.5431787238237687e-05, 7.948041702795594e-06, 1.8629648297308005e-06, 3.493326368021617e-07, 5.458740157428918e-08, 7.3113721832006694e-09, 8.568669959031558e-10, 8.926380928179195e-11, 8.369122532474074e-12, 7.133320733342741e-13, 5.5733332990829056e-14, 4.0195383229893735e-15, 2.6918611104815313e-16, 1.6825419435778025e-17, 9.859398650141232e-19, 5.437584461783112e-20, 2.8322919698794405e-21], [1.2508752256845955e-05, 1.1727852665958315e-05, 5.497851637406497e-06, 1.7182101155749489e-06, 4.027363135598466e-07, 7.551883755753619e-08, 1.1800721369504832e-08, 1.5805747017520104e-09, 1.8523777241194781e-10, 1.9297077921569174e-11, 1.8092394996776736e-12, 1.5420834842070555e-13, 1.2048449177848038e-14, 8.689450388857786e-16, 5.819273681119903e-17, 3.63732438182561e-18, 2.131407852100236e-19, 1.1754986921171652e-20, 6.122857547660891e-22], [2.4788004403138585e-06, 2.3240532513067532e-06, 1.0894833297321834e-06, 3.404895950919431e-07, 7.980835585229244e-08, 1.496521187292364e-08, 2.3384932986214126e-09, 3.1321503425791915e-10, 3.670769573089877e-11, 3.8240109218389476e-12, 3.585284588220838e-13, 3.055874112113093e-14, 2.3875843500540646e-15, 1.7219474019239398e-16, 1.1531780202275778e-17, 7.207914182087306e-19, 4.223710417945921e-20, 2.3294303186904002e-21, 1.2133378032820493e-22], [4.5342663933227513e-07, 4.251200049148938e-07, 1.9929025216182868e-07, 6.228296974588194e-08, 1.4598688138104955e-08, 2.7374634989075815e-09, 4.2776140436730644e-10, 5.7293857973467814e-11, 6.714637791005751e-12, 6.994949625068675e-13, 6.558267117626207e-14, 5.589859943313942e-15, 4.367412278780594e-16, 3.1498171892468064e-17, 2.109413996220814e-18, 1.318484639193252e-19, 7.726087139469154e-21, 4.26103587761491e-22, 2.219459354490534e-23], [7.701721597909206e-08, 7.220916548656892e-08, 3.385063660105676e-08, 1.0579133462034335e-08, 2.4796741519192138e-09, 4.6497448372402926e-10, 7.265782291969436e-11, 9.7317031048641e-12, 1.14052123124662e-12, 1.1881338662195271e-13, 1.1139607407950588e-14, 9.494710129538718e-16, 7.41830994402805e-17, 5.3501521462462135e-18, 3.5829653408873726e-19, 2.2395247083718013e-20, 1.3123219287910637e-21, 7.237623289275675e-23, 3.769883937859016e-24], [1.220971076639472e-08, 1.1447479814293493e-08, 5.366416805684572e-09, 1.6771335874513135e-09, 3.931082655345243e-10, 7.37134404022771e-11, 1.151860647632633e-11, 1.542788565702929e-12, 1.8080937072866891e-13, 1.883575077841935e-14, 1.7659867702720887e-15, 1.5052175415415805e-16, 1.1760411959923465e-17, 8.481715345255499e-19, 5.68015474749538e-20, 3.5503683943648745e-21, 2.0804531791029602e-22, 1.1473965382255324e-23, 5.976480961948993e-25], [1.814655598879567e-09, 1.7013698142009654e-09, 7.97578131757203e-10, 2.492622399306974e-10, 5.842530823755947e-11, 1.0955583625030078e-11, 1.711940940573815e-12, 2.2929535041450214e-13, 2.6872605191085422e-14, 2.7994439232119186e-15, 2.6246795206990473e-16, 2.2371139591676904e-17, 1.7478790297754886e-18, 1.2605861460480278e-19, 8.442071079533401e-21, 5.276698202099733e-22, 3.0920519592134064e-23, 1.7053062042687566e-24, 8.882482842302632e-26], [2.5383652352275314e-10, 2.379899519941841e-10, 1.1156632714660754e-10, 3.486714529664412e-11, 8.172612554097997e-12, 1.5324821207161733e-12, 2.3946865570515856e-13, 3.207414930143529e-14, 3.758977011349314e-15, 3.9159007015092063e-16, 3.6714378491818075e-17, 3.1293058058507996e-18, 2.4449572510093585e-19, 1.7633252563811324e-20, 1.1808885253399272e-21, 7.381118092748635e-23, 4.325204850788541e-24, 2.385405796563446e-25, 1.2424939290588994e-26], [3.353439113969595e-11, 3.144089757743255e-11, 1.4739048583834922e-11, 4.606305160799547e-12, 1.0796853904979733e-12, 2.0245650286051281e-13, 3.1636249404409074e-14, 4.2373219315341124e-15, 4.965991640380072e-16, 5.173303824295741e-17, 4.850343487646713e-18, 4.1341318196754963e-19, 3.2300376493233146e-20, 2.3295323318076054e-21, 1.5600740646598952e-22, 9.751209074856882e-24, 5.714036310170784e-25, 3.151364110204032e-26, 1.6414610800491803e-27]] |
| Legacy trial inputs | {"lambda_home": 2.3779834049784325, "lambda_away": 0.9375717437796195, "rho": -0.03199263817223977, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6908 |
| Legacy p draw | 0.1805 |
| Legacy p away | 0.1288 |
| Legacy p over 1 5 | 0.8459 |
| Legacy p under 3 5 | 0.5769 |
| Legacy p btts yes | 0.5546 |
| Legacy p over 2 5 | 0.6437 |
| Legacy goal margin distribution | {"-1": 0.0864496109726685, "-10": 6.421717549688416e-09, "-11": 5.383805230815663e-10, "-12": 4.14784926486697e-11, "-13": 2.955636234313131e-12, "-14": 1.958765634683337e-13, "-15": 1.2131318295356977e-14, "-16": 7.049402828542763e-16, "-17": 3.8352540944264546e-17, "-18": 1.7775132989611494e-18, "-2": 0.031668074841058866, "-3": 0.008471495914370668, "-4": 0.0017984164224231992, "-5": 0.000314959938575529, "-6": 4.682317298870647e-05, "-7": 6.03809970611292e-06, "-8": 6.868786393152691e-07, "-9": 6.985858509590768e-08, "0": 0.18046940179076404, "1": 0.22324341556946262, "10": 7.07447624306804e-05, "11": 1.504307920133171e-05, "12": 2.939508204843868e-06, "13": 5.312598589335163e-07, "14": 8.929822075582989e-08, "15": 1.4027253212903093e-08, "16": 2.067384599457586e-09, "17": 2.852774211001857e-10, "18": 3.353439113969595e-11, "2": 0.20371841153830722, "3": 0.13822068264547036, "4": 0.0744230555722163, "5": 0.03305802193004125, "6": 0.012464839651842944, "7": 0.004076903624019652, "8": 0.0011762902166997543, "9": 0.00030343003605278694} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.6908 |
| Legacy raw p draw | 0.1805 |
| Legacy raw p away | 0.1288 |
| Legacy market weight | 0 |
| Legacy lambda home | 2.3780 |
| Legacy lambda away | 0.9376 |
| Legacy model home team | Inter |
| Legacy model away team | Fiorentina |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 9.182142600418587, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,674.7175 |
| Elo away rating | 1,445.4790 |
| Elo rating diff | 289.2385 |
| Elo home expectancy | 0.8409 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **58.9%**. Expected goals are 0.62 for Lecce and 1.52 for Juventus (2.14 combined). The most likely exact score is 0-1 at 17.7%. Goal-market probabilities: at least one goal: 87.9%; Over 2.5 goals: 36.0%; Under 3.5 goals: 83.2%; Double Chance 1X: 41.1%; Double Chance X2: 85.2%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 93.4%; BTTS Yes (both teams score): 36.3%; BTTS No (at least one team does not score): 63.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 14.8% | 6.76 |
| Draw | 26.3% | 3.80 |
| Juventus win | 58.9% | 1.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.62 |
| Juventus expected goals | 1.52 |
| Expected total goals | 2.14 |
| Over 0.5 | 87.9% |
| Under 0.5 | 12.1% |
| Over 1.5 | 63.2% |
| Under 1.5 | 36.8% |
| Over 2.5 | 36.0% |
| Under 2.5 | 64.0% |
| Over 3.5 | 16.8% |
| Under 3.5 | 83.2% |
| Over 4.5 | 6.6% |
| Under 4.5 | 93.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.65% |
| 2 | 0-2 | 13.60% |
| 3 | 0-0 | 12.07% |
| 4 | 1-1 | 11.35% |
| 5 | 1-2 | 8.41% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:00:00+00:00 |
| Fixture id | 63af660d4d0d52f8ac7685172ef939c4 |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6188 |
| Dc lambda away | 1.5175 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:42:05.183279+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 36.3% |
| P btts no | 63.7% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.28 |
| Fair Over 1.5 odds | 1.58 |
| Fair Under 1.5 odds | 2.72 |
| Fair Over 2.5 odds | 2.78 |
| Fair Under 2.5 odds | 1.56 |
| Fair Over 3.5 odds | 5.94 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.20 |
| Fair Under 4.5 odds | 1.07 |
| Goal margin distribution | {"-1": 0.2749323455656261, "-10": 2.294987631285484e-06, "-11": 3.143902220164923e-07, "-12": 3.9521746804409356e-08, "-13": 4.589790182718384e-09, "-14": 4.944576198973039e-10, "-15": 4.7076751212788295e-11, "-2": 0.18385105276438782, "-3": 0.08652444068412109, "-4": 0.03139579433663436, "-5": 0.009245714091742555, "-6": 0.002288136860430599, "-7": 0.00048797151549848794, "-8": 9.138516060512443e-05, "-9": 1.5251220318277567e-05, "0": 0.2631946135628172, "1": 0.11054523199032734, "10": 2.9187311086228574e-10, "11": 1.6305125348221638e-11, "12": 8.358582180842092e-13, "13": 3.958500386592471e-14, "14": 1.7390349361218553e-15, "15": 6.751916936855767e-17, "2": 0.030573761161530693, "3": 0.005867632722752183, "4": 0.0008682343634383769, "5": 0.00010426710809754883, "6": 1.052277392562726e-05, "7": 9.151327292159741e-07, "8": 6.98886529044886e-08, "9": 4.756384540142577e-09} |
| Raw goal margin distribution | {"-1": 0.2749323455656261, "-10": 2.294987631285484e-06, "-11": 3.143902220164923e-07, "-12": 3.9521746804409356e-08, "-13": 4.589790182718384e-09, "-14": 4.944576198973039e-10, "-15": 4.7076751212788295e-11, "-2": 0.18385105276438782, "-3": 0.08652444068412109, "-4": 0.03139579433663436, "-5": 0.009245714091742555, "-6": 0.002288136860430599, "-7": 0.00048797151549848794, "-8": 9.138516060512443e-05, "-9": 1.5251220318277567e-05, "0": 0.2631946135628172, "1": 0.11054523199032734, "10": 2.9187311086228574e-10, "11": 1.6305125348221638e-11, "12": 8.358582180842092e-13, "13": 3.958500386592471e-14, "14": 1.7390349361218553e-15, "15": 6.751916936855767e-17, "2": 0.030573761161530693, "3": 0.005867632722752183, "4": 0.0008682343634383769, "5": 0.00010426710809754883, "6": 1.052277392562726e-05, "7": 9.151327292159741e-07, "8": 6.98886529044886e-08, "9": 4.756384540142577e-09} |
| Unadjusted home-win probability | 14.8% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 58.9% |
| Raw p over 1 5 | 63.2% |
| Raw p under 3 5 | 83.2% |
| Raw p btts yes | 36.3% |
| P home draw | 41.1% |
| P draw away | 85.2% |
| P home away | 73.7% |
| Raw p home draw | 41.1% |
| Raw p draw away | 85.2% |
| Raw p home away | 73.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.3602 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.12568404396972754, 0.17872102891165728, 0.13603053530368356, 0.06767752727133484, 0.02525304899743847, 0.007538295317561186, 0.0018752156851940562, 0.0003998365736393572, 7.459708556284136e-05, 1.237111035712337e-05, 1.8464519529422964e-06, 2.505386057519142e-07, 3.1161814671691335e-08, 3.5777395198458318e-09, 3.8142575339039804e-10, 3.795317245416891e-11], [0.07095712453295454, 0.11477604542457191, 0.08299921645135437, 0.041293535472353995, 0.015408182251991006, 0.004599501158616328, 0.001144165405222673, 0.00024396083016635936, 4.5515513391520214e-05, 7.5482498395098936e-06, 1.1266151747999018e-06, 1.5286647164771225e-07, 1.901342367857801e-08, 2.1829626425516812e-09, 2.327274431074983e-10, 2.315717988249249e-11], [0.022732799289033507, 0.03392987406252645, 0.025321042500345996, 0.012597653464570249, 0.004700661697022258, 0.0014031959492771123, 0.0003490570404366288, 7.442651645612344e-05, 1.3885676254392452e-05, 2.3027874618729733e-06, 3.4370289193468094e-07, 4.663584297495493e-08, 5.8005331812322515e-09, 6.659688152732766e-10, 7.099948324663564e-11, 7.06469242798715e-12], [0.004623482819558271, 0.006900786295753037, 0.005149889526809431, 0.0025621584750579827, 0.0009560383796298427, 0.0002853873067487199, 7.099254293258767e-05, 1.5137146806221047e-05, 2.824121428420056e-06, 4.6834963577055125e-07, 6.990359593150008e-08, 9.48497437683965e-09, 1.179734407836106e-09, 1.3544725999771404e-10, 1.4440143812235783e-11, 1.4368439034263208e-12], [0.0007052560854129845, 0.0010526310400952967, 0.0007855530278219889, 0.0003908261210971114, 0.00014583202997318242, 4.353236351019606e-05, 1.0829049198658759e-05, 2.3089876868834273e-06, 4.3078538432392085e-07, 7.14410420929592e-08, 1.0662943574569379e-08, 1.4468175097256e-09, 1.799541390697735e-10, 2.06608325571823e-11, 2.202668355279175e-12, 2.1917306632855068e-13], [8.606259227922358e-05, 0.0001284528526558229, 9.586125004162735e-05, 4.769261805427009e-05, 1.779592235561366e-05, 5.312266181347544e-06, 1.321471824536011e-06, 2.817663966098651e-07, 5.2568857834396575e-08, 8.717969833679363e-09, 1.301201909966016e-09, 1.7655553495726477e-10, 2.1959852626654803e-11, 2.5212470268538736e-12, 2.6879221960308587e-13, 2.674574900686706e-14], [8.75186798929758e-06, 1.3062613843248709e-05, 9.748312053295017e-06, 4.849952647495688e-06, 1.809701045244015e-06, 5.402144080476112e-07, 1.3438297236495608e-07, 2.8653358464371047e-08, 5.3458267050812255e-09, 8.865468619803549e-10, 1.3232168636632644e-10, 1.795426670059555e-11, 2.233138999919588e-12, 2.5639038475443397e-13, 2.7333989834796036e-14, 2.719825866080676e-15], [7.628520253881964e-07, 1.138595947673331e-06, 8.497065544254307e-07, 4.227436022462073e-07, 1.5774165119946397e-07, 4.708750815562529e-08, 1.1713421954222198e-08, 2.497555100859537e-09, 4.659662067952222e-10, 7.727539653138019e-11, 1.1533751031296729e-11, 1.5649743270417443e-12, 1.9465040047967576e-13, 2.234813465412847e-14, 2.3825530198711414e-15, 2.3707220826229273e-16], [5.8181900330501125e-08, 8.683948359517226e-08, 6.480620148395935e-08, 3.224219811008503e-08, 1.203078542445447e-08, 3.5913134069849446e-09, 8.933700455509133e-10, 1.904858309502401e-10, 3.553873949190248e-11, 5.893711059757357e-12, 8.796667382487939e-13, 1.1935890223192515e-13, 1.484577588194453e-14, 1.7044681009497907e-15, 1.8171474640017662e-16, 1.8081241359003337e-17], [3.944418417446322e-09, 5.887247692299206e-09, 4.3935102367919635e-09, 2.1858467894989257e-09, 8.156222353515252e-10, 2.4347164092038355e-10, 6.056566116350383e-11, 1.291390992034691e-11, 2.4093344801115008e-12, 3.9956175922681095e-13, 5.96366509834415e-14, 8.091888535358974e-15, 1.0064633756784351e-15, 1.1555372600663567e-16, 1.2319277788296861e-17, 1.2258104500130313e-18], [2.4066922715070084e-10, 3.592112200580655e-10, 2.680706256949233e-10, 1.333697396735944e-10, 4.9765301815029854e-11, 1.4855455342731544e-11, 3.695422067704623e-12, 7.879439732552043e-13, 1.4700587156556686e-13, 2.4379315177812176e-14, 3.638738384994439e-15, 4.937276814702844e-16, 6.1409499993369e-17, 7.050526335998e-18, 7.516624127020746e-19, 7.479299161899926e-20], [1.3349514258870315e-11, 1.9924837757129034e-11, 1.4869423409324496e-11, 7.397793488403139e-12, 2.7603969732313623e-12, 8.240069379357228e-13, 2.0497880086047063e-13, 4.37059171656157e-14, 8.154166620451869e-15, 1.3522793065018966e-15, 2.0183465302095042e-16, 2.7386237957457742e-17, 3.4062809171620705e-18, 3.910807499955521e-19, 4.169344047438176e-20, 4.148640521690772e-21], [6.787686927662049e-13, 1.0130972420212745e-12, 7.560499126796313e-13, 3.7614781467731614e-13, 1.403549978450375e-13, 4.189741298798724e-14, 1.0422341218325338e-14, 2.222268742170958e-15, 4.146063227644593e-16, 6.875792177375877e-17, 1.0262474044321102e-17, 1.3924792001938262e-18, 1.7319557854326187e-19, 1.9884871036721267e-20, 2.119942459248443e-21, 2.1094155555464008e-22], [3.185781866805705e-14, 4.7549435578548844e-14, 3.5484991100560784e-14, 1.7654392431595805e-14, 6.587522550989065e-15, 1.966443355235508e-15, 4.891696687967176e-16, 1.0430156159862665e-16, 1.94594317475535e-17, 3.2271338192307385e-18, 4.816663477174174e-19, 6.53556216301447e-20, 8.12888601690556e-21, 9.33290858103505e-22, 9.949890614167463e-23, 9.90048288619624e-24], [1.3884351046597389e-15, 2.072310921595197e-15, 1.5465154047711773e-15, 7.694179711068637e-16, 2.870989899789241e-16, 8.570200659944854e-17, 2.1319109992082903e-17, 4.545695708274161e-18, 8.480856281012061e-19, 1.406457211882888e-19, 2.099209845069073e-20, 2.848344398706016e-21, 3.542750627482839e-22, 4.0674906331493247e-23, 4.336385224668959e-24, 4.314852229999268e-25], [5.647703805278974e-17, 8.429488881644631e-17, 6.290723208550117e-17, 3.1297428224671625e-17, 1.1678255993052589e-17, 3.486079739465872e-18, 8.67192267203261e-19, 1.8490416198135416e-19, 3.4497373431100346e-20, 5.72101189378936e-21, 8.538904980352788e-22, 1.1586141437456186e-22, 1.4410760814703484e-23, 1.6545233010658947e-24, 1.7639009019813185e-25, 1.755141977957652e-26]] |
| Legacy trial inputs | {"lambda_home": 0.6101513624574176, "lambda_away": 1.4925515169130317, "rho": -0.03199263817223977, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1476 |
| Legacy p draw | 0.2685 |
| Legacy p away | 0.5839 |
| Legacy p over 1 5 | 0.6246 |
| Legacy p under 3 5 | 0.8381 |
| Legacy p btts yes | 0.3576 |
| Legacy p over 2 5 | 0.3511 |
| Legacy goal margin distribution | {"-1": 0.275318820167825, "-10": 2.005256634445343e-06, "-11": 2.702326575626441e-07, "-12": 3.3417213641393073e-08, "-13": 3.817531655381317e-09, "-14": 4.045829332728905e-10, "-15": 3.795317245416891e-11, "-2": 0.18232123601939373, "-3": 0.08456226047028127, "-4": 0.030217183980553425, "-5": 0.008759784121063041, "-6": 0.002133541383005358, "-7": 0.00044772624712483526, "-8": 8.249870577161995e-05, "-9": 1.3545562041650666e-05, "0": 0.2684945715823274, "1": 0.11044606228649288, "10": 2.6136805979801086e-10, "11": 1.4398877588219248e-11, "12": 7.278959411777495e-13, "13": 3.399303682173774e-14, "14": 1.4727299934761852e-15, "15": 5.647703805278974e-17, "2": 0.030468688925648527, "3": 0.005776986456669126, "4": 0.0008438922717209599, "5": 0.00010000798555991916, "6": 9.95750658508062e-06, "7": 8.542211917479703e-07, "8": 6.434475878492887e-08, "9": 4.3188818828201395e-09} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.1476 |
| Legacy raw p draw | 0.2685 |
| Legacy raw p away | 0.5839 |
| Legacy market weight | 0 |
| Legacy lambda home | 0.6102 |
| Legacy lambda away | 1.4926 |
| Legacy model home team | Lecce |
| Legacy model away team | Juventus |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.277761217417119, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,364.6827 |
| Elo away rating | 1,567.4383 |
| Elo rating diff | -142.7556 |
| Elo home expectancy | 0.3054 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **53.4%**. Expected goals are 1.00 for Udinese and 1.69 for AC Milan (2.69 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 50.5%; Under 3.5 goals: 71.6%; Double Chance 1X: 46.6%; Double Chance X2: 78.0%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 51.9%; BTTS No (at least one team does not score): 48.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 22.0% | 4.55 |
| Draw | 24.6% | 4.06 |
| AC Milan win | 53.4% | 1.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.00 |
| AC Milan expected goals | 1.69 |
| Expected total goals | 2.69 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.4% |
| Under 3.5 | 71.6% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.73% |
| 2 | 0-1 | 11.19% |
| 3 | 0-2 | 9.70% |
| 4 | 1-2 | 9.70% |
| 5 | 0-0 | 7.04% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 3564688383b255192409c9deb8e526ed |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9996 |
| Dc lambda away | 1.6937 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:42:05.183279+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.9% |
| P btts no | 48.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.21 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.05 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.52 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.35 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.2404372245467016, "-10": 4.2214399863639725e-06, "-11": 6.418603885067739e-07, "-12": 8.963138826945101e-08, "-13": 1.1568692962530069e-08, "-14": 1.3811294256893692e-09, "-15": 1.4013584628732296e-10, "-2": 0.16480864497868727, "-3": 0.08230001583307124, "-4": 0.03225884697165372, "-5": 0.01036479679787513, "-6": 0.002815653816866052, "-7": 0.0006617330057964185, "-8": 0.00013693977179327776, "-9": 2.5302442373575365e-05, "0": 0.2463125566786332, "1": 0.14076899749067767, "10": 2.16280515914212e-08, "11": 1.9406759760787952e-09, "12": 1.5992938083796623e-10, "13": 1.2181705764571838e-11, "14": 8.582501074660549e-13, "15": 5.1390685001811407e-14, "2": 0.05739728423996245, "3": 0.0169148033061047, "4": 0.003912654961919436, "5": 0.0007418894253198731, "6": 0.00011893599875303118, "7": 1.649576803767018e-05, "8": 2.014535948763772e-06, "9": 2.1966635516040585e-07} |
| Raw goal margin distribution | {"-1": 0.2404372245467016, "-10": 4.2214399863639725e-06, "-11": 6.418603885067739e-07, "-12": 8.963138826945101e-08, "-13": 1.1568692962530069e-08, "-14": 1.3811294256893692e-09, "-15": 1.4013584628732296e-10, "-2": 0.16480864497868727, "-3": 0.08230001583307124, "-4": 0.03225884697165372, "-5": 0.01036479679787513, "-6": 0.002815653816866052, "-7": 0.0006617330057964185, "-8": 0.00013693977179327776, "-9": 2.5302442373575365e-05, "0": 0.2463125566786332, "1": 0.14076899749067767, "10": 2.16280515914212e-08, "11": 1.9406759760787952e-09, "12": 1.5992938083796623e-10, "13": 1.2181705764571838e-11, "14": 8.582501074660549e-13, "15": 5.1390685001811407e-14, "2": 0.05739728423996245, "3": 0.0169148033061047, "4": 0.003912654961919436, "5": 0.0007418894253198731, "6": 0.00011893599875303118, "7": 1.649576803767018e-05, "8": 2.014535948763772e-06, "9": 2.1966635516040585e-07} |
| Unadjusted home-win probability | 22.0% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 53.4% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 71.6% |
| Raw p btts yes | 51.9% |
| P home draw | 46.6% |
| P draw away | 78.0% |
| P home away | 75.4% |
| Raw p home draw | 46.6% |
| Raw p draw away | 78.0% |
| Raw p home away | 75.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.5047 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06980180386148219, 0.10858144777940172, 0.09523297763181271, 0.05386836057527161, 0.022852905132450627, 0.007756022532195356, 0.0021935900188353582, 0.0005317715160713703, 0.00011279834655388716, 2.1268059851952903e-05, 3.6090718110406133e-06, 5.567631559812256e-07, 7.873301661683017e-08, 1.0277350993714246e-08, 1.2457210491016538e-09, 1.4092796910887952e-10], [0.06374007837272208, 0.11803172056774179, 0.09704201209114015, 0.05489163762668231, 0.02328701623459613, 0.007903355025381776, 0.002235259197227028, 0.0005418729853416176, 0.00011494105069845415, 2.1672065419267736e-05, 3.677629315328695e-06, 5.673393635082857e-07, 8.022861975440408e-08, 1.0472578346261305e-08, 1.2693846198580681e-09, 1.436050202600748e-10], [0.03433973367250669, 0.05827262367079815, 0.049442705378305724, 0.027967176364396093, 0.01186468683012889, 0.0040267431146533235, 0.0011388599592189852, 0.0002760831704679239, 5.856222869966052e-05, 1.104187271444727e-05, 1.8737445649585616e-06, 2.8905823771575203e-07, 4.087631659677096e-08, 5.3357571073353286e-09, 6.467488505128097e-10, 7.316646218027816e-11], [0.011664015740211175, 0.019793187862251017, 0.01679397106777516, 0.0094994791874216, 0.004030022342604779, 0.0013677448846584146, 0.000386831203087104, 9.377587131735617e-05, 1.9891556639577893e-05, 3.7505409439397038e-06, 6.364459988899044e-07, 9.81830513511994e-08, 1.3884266102165963e-08, 1.8123715075790183e-09, 2.1967813857521492e-10, 2.4852107901162814e-11], [0.0029713960033596323, 0.005042294233613084, 0.004278246842491054, 0.0024199825446215924, 0.0010266440434389416, 0.00034843160146627285, 9.854485079827308e-05, 2.3889306689062687e-05, 5.067353578380322e-06, 9.554464448156969e-07, 1.6213396308580874e-07, 2.501203126611397e-08, 3.5370024976330012e-09, 4.6169977597489656e-10, 5.5962779674374745e-11, 6.331048906081171e-12], [0.0006055680585782021, 0.0010276154125457289, 0.0008719031834182843, 0.0004931904497692993, 0.0002092292106246566, 7.101007344987238e-05, 2.008335944226758e-05, 4.868621030693376e-06, 1.0327224863732433e-06, 1.9471919865554846e-07, 3.3042768161649117e-08, 5.0974313749471405e-09, 7.208381963414225e-10, 9.40940341398412e-11, 1.1405168413006415e-11, 1.290262553521785e-12], [0.00010284522638392474, 0.00017452264570725815, 0.0001480776256496331, 8.375983960581212e-05, 3.553395068977841e-05, 1.2059828744332863e-05, 3.410810096621055e-06, 8.268507973402888e-07, 1.7538999357428951e-07, 3.3069676947698816e-08, 5.61174078420699e-09, 8.657102637874007e-10, 1.2242185901114522e-10, 1.5980238893724648e-11, 1.936969942134023e-12, 2.191287049108989e-13], [1.4971266032370916e-05, 2.5405408198556663e-05, 2.1555784405264368e-05, 1.2192990240365073e-05, 5.172707063445923e-06, 1.755559404986268e-06, 4.965144920950084e-07, 1.2036536542637604e-07, 2.5531668756450337e-08, 4.813980663918775e-09, 8.169058218748848e-10, 1.260221706132684e-10, 1.782105289545784e-11, 2.3262568050138256e-12, 2.8196634224072483e-13, 3.189874972225984e-14], [1.9069573054697953e-06, 3.236000793648817e-06, 2.7456569443005916e-06, 1.5530758563845973e-06, 6.588708999202314e-07, 2.236134756597203e-07, 6.324327788477998e-08, 1.5331476471600694e-08, 3.2520831672268055e-09, 6.131783094095783e-10, 1.04052958616648e-10, 1.605200912083954e-11, 2.269947440428666e-12, 2.963057632619881e-13, 3.591531772062129e-14, 4.063086828240857e-15], [2.1590907138881467e-07, 3.6638572052249336e-07, 3.1086812457510514e-07, 1.7584198921840925e-07, 7.459852601778296e-08, 2.5317912331456884e-08, 7.160515529383406e-09, 1.735856822021125e-09, 3.6820659524002987e-10, 6.94251302851113e-11, 1.1781059599886818e-11, 1.8174368001130601e-12, 2.5700745504820257e-13, 3.354826141599903e-14, 4.0663956531440075e-15, 4.600298609420036e-16], [2.2001045475344938e-08, 3.733455406427169e-08, 3.167733389624687e-08, 1.7918226299544713e-08, 7.601559085747479e-09, 2.579884842087446e-09, 7.296535841478283e-10, 1.7688309543604017e-10, 3.7520100448255174e-11, 7.074392190700748e-12, 1.2004851224527416e-12, 1.8519606161357566e-13, 2.6188953848240702e-14, 3.418554025008846e-15, 4.143640427430464e-16, 4.6876853415645604e-17], [2.0380886137711732e-09, 3.45852335171465e-09, 2.9344611646259125e-09, 1.659872620189869e-09, 7.041779463131558e-10, 2.38990184688795e-10, 6.759218163134588e-11, 1.6385740540411348e-11, 3.4757116245604533e-12, 6.553433194516339e-13, 1.1120812698716834e-13, 1.7155820386484406e-14, 2.426039649092689e-15, 3.166811341642803e-16, 3.838502303979962e-17, 4.342483692555058e-18], [1.730669921444745e-10, 2.936850879290982e-10, 2.491836536915162e-10, 1.4095028046286982e-10, 5.979620232379853e-11, 2.029416784759392e-11, 5.73967956465578e-12, 1.3914168452869645e-12, 2.951446528672868e-13, 5.5649345348927914e-14, 9.443385292299605e-15, 1.4568091946531377e-15, 2.0601036778023468e-16, 2.6891397649928804e-17, 3.259515035807142e-18, 3.687477502346295e-19], [1.3565734800229235e-11, 2.302029964386453e-11, 1.9532085931841835e-11, 1.1048288879840403e-11, 4.6870833816094625e-12, 1.590744113597214e-12, 4.499007572016756e-13, 1.0906523355983103e-13, 2.3134706617891384e-14, 4.36203490599596e-15, 7.402131331015436e-16, 1.1419096700254842e-16, 1.614797819489104e-17, 2.1078633447440363e-18, 2.5549480004949133e-19, 2.890403378414444e-20], [9.87387707527901e-13, 1.6755421823207582e-12, 1.421651081602552e-12, 8.041543484240362e-13, 3.411513333639166e-13, 1.1578297871204988e-13, 3.2746215653642484e-14, 7.938358852025979e-15, 1.6838693419971858e-15, 3.174925434864945e-16, 5.387672391788372e-17, 8.311437514401002e-18, 1.1753373780235308e-18, 1.5342171923586015e-19, 1.8596296376212783e-20, 2.103792243966992e-21], [6.70762672310251e-14, 1.1382470565649244e-13, 9.657710657305713e-14, 5.462866466600946e-14, 2.3175453601939825e-14, 7.865491905239353e-15, 2.224550594707939e-15, 5.392769989687379e-16, 1.1439039508474136e-16, 2.1568239637170278e-17, 3.66001065589123e-18, 5.646213736909168e-19, 7.984426325531402e-20, 1.0422406679816869e-20, 1.2633032958868847e-21, 1.4291704229151586e-22]] |
| Legacy trial inputs | {"lambda_home": 1.0189958825641416, "lambda_away": 1.696944543208638, "rho": -0.03199263817223977, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2232 |
| Legacy p draw | 0.2479 |
| Legacy p away | 0.5290 |
| Legacy p over 1 5 | 0.7579 |
| Legacy p under 3 5 | 0.7106 |
| Legacy p btts yes | 0.5256 |
| Legacy p over 2 5 | 0.5103 |
| Legacy goal margin distribution | {"-1": 0.23799002654606438, "-10": 4.219157115695477e-06, "-11": 6.425535420304464e-07, "-12": 8.987719592150546e-08, "-13": 1.1619902075752593e-08, "-14": 1.3893260693617285e-09, "-15": 1.4092796910887952e-10, "-2": 0.16346064075498243, "-3": 0.08159390705967885, "-4": 0.03199416380121266, "-5": 0.0102882458295746, "-6": 0.0027979431299995283, "-7": 0.0006584166346188924, "-8": 0.00013644597265486514, "-9": 2.524910499517261e-05, "0": 0.24787689761002832, "1": 0.1414484569166482, "10": 2.5720149786456214e-08, "11": 2.352133117434139e-09, "12": 1.975635715346076e-10, "13": 1.533785408912305e-11, "14": 1.1012124131843933e-12, "15": 6.70762672310251e-14, "2": 0.05894171335443253, "3": 0.017667376658318194, "4": 0.004159966966946497, "5": 0.0008032768119650234, "6": 0.0001311799799157211, "7": 1.8536778106962048e-05, "8": 2.306741652740655e-06, "9": 2.563238419890861e-07} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.2232 |
| Legacy raw p draw | 0.2479 |
| Legacy raw p away | 0.5290 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.0190 |
| Legacy lambda away | 1.6969 |
| Legacy model home team | Udinese |
| Legacy model away team | Milan |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.366566753941214, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,377.1775 |
| Elo away rating | 1,589.9424 |
| Elo rating diff | -152.7650 |
| Elo home expectancy | 0.2933 |

</details>


---
