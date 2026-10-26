# Serie A — football model report

Fixtures in this report: **8**.

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
| Training as of utc | 2026-10-26T10:49:44.033835+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 80, 'bbs_added_results': 10, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 80, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 100, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-26T10:49:44.033835+00:00', 'observations': 332, 'observations_sha256': '28f87dedc542ea6ed15da20839551d0aea7043fd2d7ffcccdcb9c604302faa58', 'eligible_training_matches': 140, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 142, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 16, 'retrospective_eligible_training_matches': 140, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'a6ef49289829d48ed55f634e912846675525b445504d495c2cea78433e0e46f9', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 79, 'tuning_matches': 20, 'audit_matches': 41, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-05T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 32, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-26', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1970, 'tune_start_date': '2025-10-27', 'audit_start_date': '2026-04-27', 'training_shot_matches': 1600, 'tuning_matches': 258, 'audit_matches': 112, 'audit_matchdays': 38, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8795837161089624, 'audit_candidate_poisson_score': 0.876579055323487, 'audit_gain': 0.0030046607854753438, 'audit_gain_lower95': -0.001746877171994197, 'audit_baseline_briers': [0.5874897559022755, 0.16922511059665027, 0.1953962342079745, 0.24317108165476647], 'audit_candidate_briers': [0.5867226447788666, 0.16762451913172724, 0.19525382295262814, 0.24305711753920162], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1781.423 |
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
| Live odds matched | 8.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261026T104944033835Z_a010d17a5b0b9fb8de16caa0f2d769e080129a5f00940795410921efb85f0ea5.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 3.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 3.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE': 7, 'ANCHORED': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 8} |
| Legacy comparison status | {'AVAILABLE': 8} |
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

## 2026-10-27 — AS Roma vs Cagliari

The model's most likely 1X2 outcome is **AS Roma win** at **71.7%**. Expected goals are 1.95 for AS Roma and 0.70 for Cagliari (2.64 combined). The most likely exact score is 1-0 at 14.6%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.9%; Double Chance 1X: 88.9%; Double Chance X2: 28.3%; Double Chance 12 (either team wins): 82.8%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 42.0%; BTTS No (at least one team does not score): 58.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 71.7% | 1.39 |
| Draw | 17.2% | 5.81 |
| Cagliari win | 11.1% | 9.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.95 |
| Cagliari expected goals | 0.70 |
| Expected total goals | 2.64 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.1% |
| Under 3.5 | 71.9% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.64% |
| 2 | 2-0 | 14.49% |
| 3 | 2-1 | 10.08% |
| 4 | 3-0 | 9.41% |
| 5 | 1-1 | 8.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 71.7% | 73.9% | 1.35 | -3.2% |
| Draw | 17.2% | 15.6% | 5.02 | -13.6% |
| Cagliari win | 11.1% | 10.6% | 10.28 | +13.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7eecf109ae6a5f87441a79b0e4111982 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T10:50:11Z |
| Market best draw last update utc | 2026-10-26T10:50:11Z |
| Market best away last update utc | 2026-10-26T10:50:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Roma |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9473 |
| Dc lambda away | 0.6955 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:49:44.033835+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 42.0% |
| P btts no | 58.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.62 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.56 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.41 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.08072688716286604, "-10": 5.317007826408188e-10, "-11": 3.328172257172384e-11, "-12": 1.912601957512077e-12, "-13": 1.0157988225169539e-13, "-14": 5.014066332529845e-15, "-15": 2.3049014662502393e-16, "-16": 9.237813669292697e-18, "-2": 0.023919422460097452, "-3": 0.0050142338720939065, "-4": 0.0008187859234316822, "-5": 0.0001091247057381157, "-6": 1.2263926113902954e-05, "-7": 1.1903269525557648e-06, "-8": 1.0160777728107607e-07, "-9": 7.737522089944532e-09, "0": 0.172112215755527, "1": 0.2727094351981787, "10": 1.86672925208221e-05, "11": 3.2712953548137054e-06, "12": 5.263061976489941e-07, "13": 7.825669828984803e-08, "14": 1.0814434588505926e-08, "15": 1.3917653972539918e-09, "16": 1.5616467293573526e-10, "2": 0.2225180797658514, "3": 0.13059276823523955, "4": 0.05970144415622437, "5": 0.022276013993459538, "6": 0.0070088029351742746, "7": 0.0019044979900935935, "8": 0.00045513593853234566, "9": 9.703222898791576e-05} |
| Raw goal margin distribution | {"-1": 0.08918636463632104, "-10": 5.874184121871418e-10, "-11": 3.676935838016593e-11, "-12": 2.113026050944753e-12, "-13": 1.1222457271189817e-13, "-14": 5.539496987435075e-15, "-15": 2.546435145022463e-16, "-16": 1.0205856404319689e-17, "-2": 0.026425970434268885, "-3": 0.005539682083692055, "-4": 0.0009045875852854111, "-5": 0.00012056002824877524, "-6": 1.3549079181769558e-05, "-7": 1.3150628911641318e-06, "-8": 1.1225539089837013e-07, "-9": 8.548347282401046e-09, "0": 0.21014423598725604, "1": 0.25384327367024634, "10": 1.7375880818359133e-05, "11": 3.04498566910503e-06, "12": 4.898960979002189e-07, "13": 7.284286466320421e-08, "14": 1.0066287133938596e-08, "15": 1.295482440360698e-09, "16": 1.4536113054116694e-10, "2": 0.20712417880786974, "3": 0.12155830172286741, "4": 0.05557127136596632, "5": 0.020734949314514042, "6": 0.00652393079205846, "7": 0.0017727439615444255, "8": 0.0004236494293571924, "9": 9.031949569296755e-05} |
| Unadjusted home-win probability | 66.8% |
| Unadjusted draw probability | 21.0% |
| Unadjusted away-win probability | 12.2% |
| Raw p over 1 5 | 74.3% |
| Raw p under 3 5 | 72.7% |
| Raw p btts yes | 43.2% |
| P home draw | 88.9% |
| P draw away | 28.3% |
| P home away | 82.8% |
| Raw p home draw | 87.8% |
| Raw p draw away | 33.2% |
| Raw p home away | 79.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.5094 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.9, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:49:58Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 8.36, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:49:58Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.1, "price": 8.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.53, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.30 |
| Reference draw odds | 5.00 |
| Reference away odds | 7.00 |
| Market reference 1x2 last update utc | 2026-10-26T10:50:12Z |
| Market reference home last update utc | 2026-10-26T10:50:12Z |
| Market reference draw last update utc | 2026-10-26T10:50:12Z |
| Market reference away last update utc | 2026-10-26T10:50:12Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.19 |
| Market reference over 2 5 last update utc | 2026-10-26T10:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-26T10:50:12Z |
| Home probability edge | -2.1% |
| Draw probability edge | +1.6% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | -0.0709 |
| Raw ev home | -0.0987 |
| Raw edge prob draw | 0.0543 |
| Raw ev draw | 0.0549 |
| Raw edge prob away | 0.0166 |
| Raw ev away | 0.2561 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06299170936073982, 0.043051735659603574, 0.016445877960645217, 0.003927775983442042, 0.0007035542985157915, 0.00010081810226382073, 1.2039214984923275e-05, 1.2322846297178594e-06, 1.1036514708167985e-07, 8.78618490610646e-09, 6.295224762618638e-10, 4.10043051939868e-11, 2.448268884520388e-12, 1.349356366936891e-13, 6.9057289577043624e-15, 3.2985963307205917e-16, 1.4771346668765106e-17], [0.14020863631950173, 0.08687401307632325, 0.0320435245866718, 0.007652968518770781, 0.0013708212791374089, 0.00019643629524693297, 2.3457481704338357e-05, 2.4010115437213676e-06, 2.150379756244228e-07, 1.7119203531461778e-08, 1.2265759842211635e-09, 7.989372563672858e-11, 4.77026306431589e-12, 2.629116792888328e-13, 1.3455280172613515e-14, 6.427060499773028e-16, 2.8780829536221205e-17], [0.13978975491957168, 0.10015813872963975, 0.029381814148862543, 0.007455609407995262, 0.001335469759263893, 0.0001913704841882722, 2.2852546806351243e-05, 2.339092890578036e-06, 2.094924538379278e-07, 1.6677723760851527e-08, 1.1949443441653154e-09, 7.783338073794406e-11, 4.647244803593983e-12, 2.5613156316661517e-13, 1.3108287744304272e-14, 6.261315803185749e-16, 2.803861311252648e-17], [0.0907898514032749, 0.06505013573651701, 0.0233039271126434, 0.0045575371377496844, 0.00086735326967914, 0.00012429020876689035, 1.4842141542695616e-05, 1.5191806872844279e-06, 1.3605996208374473e-07, 1.083175274800186e-08, 7.760856259056468e-10, 5.055077945789499e-11, 3.0182660052283036e-12, 1.6635086436030187e-13, 8.513495836239792e-15, 4.066563616820688e-16, 1.8210358259121513e-17], [0.04422425550376306, 0.03168629289399219, 0.011351476083960615, 0.0027110778303165756, 0.00039765308123627485, 6.054247103795502e-05, 7.229691971756113e-06, 7.400015952490641e-07, 6.627558514548682e-08, 5.276208669551175e-09, 3.7803574388944503e-10, 2.462357358346426e-11, 1.4702146212426111e-12, 8.103045676398646e-14, 4.146972478451601e-15, 1.9808463791152084e-16, 8.870369584473208e-18], [0.017233510086274426, 0.01234765949058871, 0.004423495101469651, 0.0010564652044726933, 0.00018923702343832916, 2.2205392884776255e-05, 2.8172994230578848e-06, 2.8836720506236143e-07, 2.5826573043865017e-08, 2.0560571181636206e-09, 1.473146971289692e-10, 9.595426737588461e-12, 5.729199557020634e-13, 3.15763188781948e-14, 1.6160111961368564e-15, 7.719052738137645e-17, 3.4566461766664055e-18], [0.005596360837709117, 0.0040097436717511205, 0.0014364731634897347, 0.0003430734926961988, 6.145229043376229e-05, 8.80600589658397e-06, 8.610930405620317e-07, 9.364354244791636e-08, 8.386847556379966e-09, 6.676781154030961e-10, 4.783855393963849e-11, 3.115991469324395e-12, 1.8604838986264856e-13, 1.0254003594409164e-14, 5.247788596800522e-16, 2.506663136625327e-17, 1.1225014054635222e-18], [0.0015577253420335734, 0.0011160966052186007, 0.0003998367358376189, 9.549317659288074e-05, 1.710500679113901e-05, 2.4511176003477918e-06, 2.927007261721293e-07, 2.453285644569133e-08, 2.3344465014327708e-09, 1.858456148282193e-10, 1.3315676018582027e-11, 8.673241447586817e-13, 5.178584800693893e-14, 2.854162145636959e-15, 1.4607016101944697e-16, 6.97719965723481e-18, 3.124439142624342e-19], [0.00037938845843454324, 0.0002718285175775138, 9.738137959346656e-05, 2.325763604211159e-05, 4.165973283538425e-06, 5.969766959197888e-07, 7.128809828576449e-08, 7.296757131538465e-09, 5.351336512626447e-10, 4.5263230566982955e-11, 3.243070945426508e-12, 2.1123927393611268e-13, 1.2612591266204539e-14, 6.951393466718703e-16, 3.557580512884735e-17, 1.699316914683209e-18, 7.609660816362624e-20], [8.213434950987064e-05, 5.884854421135104e-05, 2.108223402548009e-05, 5.035078861751241e-06, 9.018975092990705e-07, 1.292403379750767e-07, 1.5433262268064495e-08, 1.5796853784201833e-09, 1.4147884744130871e-10, 9.222982007897364e-12, 7.020970633004231e-13, 4.573149227383106e-14, 2.7305179065227583e-15, 1.504917105101162e-16, 7.70185688991363e-18, 3.678875471714078e-19, 1.647426344284879e-20], [1.6003244425307528e-05, 1.1466184887415323e-05, 4.107710673483172e-06, 9.810462760847793e-07, 1.7572777253388422e-07, 2.518148290656334e-08, 3.0070521021905775e-09, 3.077895104398986e-10, 2.7566062069341197e-11, 2.1945380845203773e-12, 1.2875540811721813e-13, 8.910428501101472e-15, 5.320203511261915e-16, 2.9322148913915524e-17, 1.5006474035959133e-18, 7.168005071621543e-20, 3.2098831509115908e-21], [2.834644298854841e-06, 2.0309978874863555e-06, 7.275961256656551e-07, 1.7377209017808596e-07, 3.11265463005676e-08, 4.460379724308854e-09, 5.326371872664929e-10, 5.451855622701426e-11, 4.882758683805775e-12, 3.8871710664295303e-13, 2.785124125593422e-14, 1.4855053759370218e-15, 9.423641951064113e-17, 5.1938132068745206e-18, 2.6580870066994124e-19, 1.2696640862588171e-20, 5.685645192879009e-22], [4.6025714620903856e-07, 3.297702262074629e-07, 1.1813874373123819e-07, 2.8215126091289957e-08, 5.053972866165379e-09, 7.242254852746092e-10, 8.648353935452243e-11, 8.852100108158071e-12, 7.928065536630952e-13, 6.311544141831033e-14, 4.522166264040368e-15, 2.9455387634408997e-16, 1.44014378351062e-17, 8.43312032308466e-19, 4.315897908506673e-20, 2.06153544281259e-21, 9.231700894143254e-23], [6.898273427557655e-08, 4.9425526738338447e-08, 1.770647915754708e-08, 4.2288459000337836e-09, 7.574827900756098e-10, 1.0854596092161175e-10, 1.2962038859457106e-11, 1.3267410936940252e-12, 1.1882480103511083e-13, 9.45965914903489e-15, 6.777763176774057e-16, 4.414734664968547e-17, 2.6359323643023402e-18, 1.1896337258294244e-19, 6.4686108849206984e-21, 3.0898021426186645e-22, 1.383635159035757e-23], [9.600538319453711e-09, 6.878701872195923e-09, 2.464264912659819e-09, 5.885414304998527e-10, 1.0542119892487867e-10, 1.5106673694417703e-11, 1.8039666312926231e-12, 1.8464661982111546e-13, 1.6537211341634805e-14, 1.3165297244738895e-15, 9.432820514022427e-17, 6.144121390134174e-18, 3.6685077703469046e-19, 2.021887525660717e-20, 8.473275257130442e-22, 4.3001722360319905e-23, 1.9256474107564197e-24], [1.2470605559272179e-09, 8.935079987562984e-10, 3.2009533941512937e-10, 7.644850518622891e-11, 1.3693671600828914e-11, 1.9622792252594842e-12, 2.343259883183237e-13, 2.3984646350258456e-14, 2.148098708943904e-15, 1.7101044081771207e-16, 1.2252748755080044e-17, 7.980897717932364e-19, 4.765202936841616e-20, 2.626327918158067e-21, 1.3441007284104532e-22, 5.2573018762005515e-24, 2.501316958145689e-25], [1.5186258100869787e-10, 1.088082132003277e-10, 3.898006731220339e-11, 9.309625949323287e-12, 1.6675664248246465e-12, 2.3895935637711354e-13, 2.853538203441622e-14, 2.9207645787681177e-15, 2.6158778950323233e-16, 2.08250407717399e-17, 1.492095986480839e-18, 9.718852227753179e-20, 5.802893961961136e-21, 3.198248347532226e-22, 1.636797866646624e-23, 7.818342524185389e-25, 2.8669298610101804e-26]] |
| Legacy trial inputs | {"lambda_home": 1.9484228609352179, "lambda_away": 0.7164912678133379, "rho": -0.031918512138755184, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7002 |
| Legacy p draw | 0.1842 |
| Legacy p away | 0.1156 |
| Legacy p over 1 5 | 0.7537 |
| Legacy p under 3 5 | 0.7163 |
| Legacy p btts yes | 0.4329 |
| Legacy p over 2 5 | 0.5106 |
| Legacy goal margin distribution | {"-1": 0.08348167871837406, "-10": 7.142340228520538e-10, "-11": 4.603941485858963e-11, "-12": 2.724704378284792e-12, "-13": 1.490352588048803e-13, "-14": 7.576473620794192e-15, "-15": 3.586404626082804e-16, "-16": 1.4771346668765106e-17, "-2": 0.02556613308260611, "-3": 0.005505576397686502, "-4": 0.0009244307016172665, "-5": 0.0001267561635126678, "-6": 1.4660938555339697e-05, "-7": 1.4648016216243683e-06, "-8": 1.2873134805953713e-07, "-9": 1.009369520891783e-08, "0": 0.18422581836818025, "1": 0.2665801231626212, "10": 1.8156717314438686e-05, "11": 3.182723478281308e-06, "12": 5.122250539316479e-07, "13": 7.619084111313692e-08, "14": 1.0533026385522213e-08, "15": 1.3558687691275456e-09, "16": 1.5186258100869787e-10, "2": 0.21731180824829915, "3": 0.12726043062091832, "4": 0.058108179610428926, "5": 0.021667275750506924, "6": 0.006815054177362183, "7": 0.0018516490038332923, "8": 0.00044252364975659543, "9": 9.435711847575344e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6618 |
| Legacy raw p draw | 0.2126 |
| Legacy raw p away | 0.1256 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9484 |
| Legacy lambda away | 0.7165 |
| Legacy model home team | Roma |
| Legacy model away team | Cagliari |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 90.4% |
| Market home draw odds | 1.08 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-26T10:49:58Z |
| Market reference home draw last update utc | 2026-10-26T10:49:58Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 28.2% |
| Market draw away odds | 3.46 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-26T10:49:58Z |
| Market reference draw away last update utc | 2026-10-26T10:49:58Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.4% |
| Market home away odds | 1.20 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-26T10:49:58Z |
| Market reference home away last update utc | 2026-10-26T10:49:58Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.46 |
| Market reference dc home draw odds | 1.08 |
| Market reference dc home away odds | 1.20 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:58Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.39, "price": 1.55, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:58Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.55, "price": 2.39, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:58Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.87, "price": 1.96, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:58Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.96, "price": 1.87, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:58Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.49, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:58Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.49, "price": 1.51, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 80.3% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.65 |
| Market reference over 1 5 last update utc | 2026-10-26T10:50:15Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.5% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-26T10:50:11Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.69 |
| Market reference under 3 5 last update utc | 2026-10-26T10:50:15Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 47.3% |
| Market btts yes odds | 2.06 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-26T10:49:58Z |
| Market reference btts yes odds | 2.08 |
| Market reference btts yes opposite odds | 1.87 |
| Market reference btts yes last update utc | 2026-10-26T10:50:11Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 9.256348126020107, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,629.5131 |
| Elo away rating | 1,419.3708 |
| Elo rating diff | 270.1423 |
| Elo home expectancy | 0.8256 |

</details>


---

## 2026-10-27 — Sassuolo vs Lazio

The model's most likely 1X2 outcome is **Lazio win** at **46.0%**. Expected goals are 1.13 for Sassuolo and 1.61 for Lazio (2.74 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 51.6%; Under 3.5 goals: 70.6%; Double Chance 1X: 54.0%; Double Chance X2: 71.4%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 28.6% | 3.49 |
| Draw | 25.3% | 3.95 |
| Lazio win | 46.0% | 2.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.13 |
| Lazio expected goals | 1.61 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 51.6% |
| Under 2.5 | 48.4% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.03% |
| 2 | 0-1 | 9.65% |
| 3 | 1-2 | 9.03% |
| 4 | 0-2 | 7.98% |
| 5 | 1-0 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 28.6% | 29.6% | 3.32 | -4.9% |
| Draw | 25.3% | 25.3% | 3.62 | -8.3% |
| Lazio win | 46.0% | 45.1% | 2.19 | +0.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T17:30:00+00:00 |
| Fixture id | c7445242bf16a8f37afef7863af45a78 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T10:50:11Z |
| Market best draw last update utc | 2026-10-26T10:50:11Z |
| Market best away last update utc | 2026-10-26T10:50:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sassuolo |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1311 |
| Dc lambda away | 1.6100 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:49:44.033835+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.85 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.17 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.01 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.21877082420449503, "-10": 2.3419224899858707e-06, "-11": 3.3816630721337206e-07, "-12": 4.4852603816485214e-08, "-13": 5.498919945095765e-09, "-14": 6.231801794237181e-10, "-15": 5.964765368904357e-11, "-2": 0.1407854261364862, "-3": 0.06629284312662868, "-4": 0.024569357157288287, "-5": 0.00747596603505104, "-6": 0.0019251802279042116, "-7": 0.0004291804910672817, "-8": 8.428396233173338e-05, "-9": 1.478341143302295e-05, "0": 0.25322561287954126, "1": 0.17316035568165683, "10": 7.76708320460406e-08, "11": 7.879128469657085e-09, "12": 7.341721622078336e-10, "13": 6.323391289942966e-11, "14": 5.034411350274393e-12, "15": 3.3852507051485754e-13, "2": 0.07869441091605511, "3": 0.02603246184809072, "4": 0.006778050424490575, "5": 0.00144890772479862, "6": 0.00026212425392812226, "7": 4.105236611663894e-05, "8": 5.663769517916859e-06, "9": 6.979072304006761e-07} |
| Raw goal margin distribution | {"-1": 0.22906048066761894, "-10": 2.4520723601655122e-06, "-11": 3.5407160510344294e-07, "-12": 4.6962199035255484e-08, "-13": 5.757555882309979e-09, "-14": 6.524908061227523e-10, "-15": 6.245311857460775e-11, "-2": 0.14740712112358764, "-3": 0.06941085753379275, "-4": 0.025724951124571502, "-5": 0.007827590263329087, "-6": 0.0020157290624975136, "-7": 0.00044936654571974856, "-8": 8.824817017753713e-05, "-9": 1.5478733698009415e-05, "0": 0.2532030929931689, "1": 0.16008397432540825, "10": 7.180543972749878e-08, "11": 7.284128025019944e-09, "12": 6.787304005160252e-10, "13": 5.845873929536933e-11, "14": 4.65423262829578e-12, "15": 3.1296100359389694e-13, "2": 0.07275172199229543, "3": 0.02406659386735357, "4": 0.006266199014543915, "5": 0.0013394919761135515, "6": 0.0002423296728094063, "7": 3.795225470369864e-05, "8": 5.236064170242856e-06, "9": 6.452040521236566e-07} |
| Unadjusted home-win probability | 26.5% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 48.2% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 54.5% |
| P home draw | 54.0% |
| P draw away | 71.4% |
| P home away | 74.7% |
| Raw p home draw | 51.8% |
| Raw p draw away | 73.5% |
| Raw p home away | 74.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.5156 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.48, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.64, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.16, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.16, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-26T10:50:12Z |
| Market reference home last update utc | 2026-10-26T10:50:12Z |
| Market reference draw last update utc | 2026-10-26T10:50:12Z |
| Market reference away last update utc | 2026-10-26T10:50:12Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-26T10:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-26T10:50:12Z |
| Home probability edge | -0.9% |
| Draw probability edge | -0.0% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0309 |
| Raw ev home | -0.1209 |
| Raw edge prob draw | -0.0000 |
| Raw ev draw | -0.0834 |
| Raw edge prob away | 0.0309 |
| Raw ev away | 0.0556 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06358838180701314, 0.09177693281281289, 0.07953019169507078, 0.04425451907976442, 0.01846904694845547, 0.006166252889463205, 0.0017156035357847313, 0.00040913416180789913, 8.537340592299214e-05, 1.5835323838647728e-05, 2.6434664346286947e-06, 4.0116955451858015e-07, 5.580762892139328e-08, 7.166334404948191e-09, 8.54507512617846e-10, 9.509802055033214e-11], [0.06940926135977482, 0.11896970382577642, 0.09168276315134935, 0.051016808895965306, 0.021291200497777045, 0.0071084841007747505, 0.0019777554822958867, 0.0004716517042732631, 9.84188468282898e-05, 1.8255032635783762e-05, 3.0474000107260627e-06, 4.624700691214219e-07, 6.433528595097826e-08, 8.261382575706193e-09, 9.850801088317546e-10, 1.0962942636561811e-10], [0.042259364515845124, 0.07054558074381329, 0.055466849778787825, 0.029406203525071724, 0.012272295909520423, 0.00409734624226272, 0.0011399827134193554, 0.00027186110438795784, 5.6728844927116435e-05, 1.0522241917156404e-05, 1.7565282281856602e-06, 2.6656878921162873e-07, 3.7083003689550106e-08, 4.761879519259981e-09, 5.678023928912827e-10, 6.31906482159292e-11], [0.016238928576491375, 0.027108421061475093, 0.022626692672017525, 0.011860240808820697, 0.00471585266431411, 0.0015744797335111801, 0.00043805906865236106, 0.0001044675684895075, 2.1799089303694796e-05, 4.043362623051252e-06, 6.749778840001906e-07, 1.0243390023307961e-07, 1.4249817885703895e-08, 1.8298387183301325e-09, 2.1818838521022277e-10, 2.4282154614414813e-11], [0.004680077498802299, 0.007812677470700451, 0.006521038302977988, 0.003628627164706059, 0.0014265140050295113, 0.00045376683187050583, 0.00012624911678681494, 3.0107670856445666e-05, 6.2825220804466956e-06, 1.165301660297653e-06, 1.945293861118152e-07, 2.9521565375280166e-08, 4.106813558220762e-09, 5.273615787984705e-10, 6.28821382711569e-11, 6.998144298625584e-12], [0.0010790428834820604, 0.0018012979545439923, 0.0015034964646510808, 0.0008366195474087297, 0.0003491522678449509, 0.00010980915423069857, 2.910811007928202e-05, 6.941651710721019e-06, 1.4485039495520726e-06, 2.686730003885196e-07, 4.4850870475073557e-08, 6.806518703076741e-09, 9.46870633001231e-10, 1.2158896060374653e-10, 1.4498162437906476e-11, 1.6134984527382248e-12], [0.00020732091592700643, 0.0003460907323612523, 0.00028887291591100174, 0.00016074313032999956, 6.708405113058709e-05, 2.2397323764206115e-05, 5.870006217150804e-06, 1.3337278923232703e-06, 2.783069794000589e-07, 5.16212408033836e-08, 8.61738091169235e-09, 1.3077642356923346e-09, 1.8192612166137625e-10, 2.336138356024895e-11, 2.7855911585141954e-12, 3.1000804712138006e-13], [3.4142926507592e-05, 5.6996422127178435e-05, 4.7573428343600864e-05, 2.6472200650462876e-05, 1.1047828036750523e-05, 3.688533671717293e-06, 1.0262409801376319e-06, 2.3053931406356127e-07, 4.583336274450801e-08, 8.501314125011763e-09, 1.419165074784003e-09, 2.153709286342402e-10, 2.9960750336847597e-11, 3.847301168079328e-12, 4.587488617831206e-13, 5.105409612098193e-14], [4.920014930134223e-06, 8.213216514044155e-06, 6.855357805258463e-06, 3.8146590159699804e-06, 1.5919982393507363e-06, 5.315197785144924e-07, 1.4788190294906353e-07, 3.5266620257895055e-08, 6.932143400852815e-09, 1.2250441511367898e-09, 2.0450248617996363e-10, 3.103507205692271e-11, 4.317360989619234e-12, 5.543982641167018e-13, 6.610596923064455e-14, 7.356923991383253e-15], [6.302017076456837e-07, 1.0520258873021649e-06, 8.780985945662948e-07, 4.886173436641789e-07, 2.0391808221207674e-07, 6.808204381976343e-08, 1.8942102634198838e-08, 4.517279850776996e-09, 9.426139451762892e-10, 1.6469675207060756e-10, 2.6194598560879763e-11, 3.975263426008742e-12, 5.530081324583852e-13, 7.101253506818458e-14, 8.46747322646614e-15, 9.423439010301418e-16], [7.264993666956806e-08, 1.2127801806944516e-07, 1.0122760143446745e-07, 5.632802742707436e-08, 2.3507768352186588e-08, 7.848528672380929e-09, 2.1836541222714493e-09, 5.207540555605354e-10, 1.0866496010736118e-10, 2.0155513471793932e-11, 3.169476602692428e-12, 4.582701580154362e-13, 6.375102655774749e-14, 8.186357023249533e-15, 9.76134126884798e-16, 1.0863382929657859e-16], [7.613743106602748e-09, 1.2709985946147028e-08, 1.0608694073954371e-08, 5.903200335631727e-09, 2.4636237476315348e-09, 8.225290181339617e-10, 2.2884784602452663e-10, 5.457523822481571e-11, 1.1388132307804843e-11, 2.1123060637187243e-12, 3.526173658334191e-13, 5.040860688637914e-14, 6.6811336835785364e-15, 8.579335676153961e-16, 1.0229925613688784e-16, 1.1384869786089554e-17], [7.314297784903851e-10, 1.2210107531923689e-09, 1.0191458587374117e-09, 5.671029943380994e-10, 2.3667304593598556e-10, 7.901792969793032e-11, 2.1984735626365117e-11, 5.242881700489675e-12, 1.0940241842535148e-12, 2.0292299525444117e-13, 3.3874907279145435e-14, 5.140818617748705e-15, 6.736661389798686e-16, 8.241914003851829e-17, 9.827586931721659e-18, 1.0937107634429987e-18], [6.486119558826241e-11, 1.0827589962448175e-10, 9.037507197610477e-11, 5.028914506375443e-11, 2.0987519478092415e-11, 7.007094247235931e-12, 1.949546326047831e-12, 4.64924433516283e-13, 9.701507742768129e-14, 1.7994657138132055e-14, 3.0039342821148062e-15, 4.558737580219573e-16, 6.341765778617209e-17, 7.671150962932935e-18, 8.714835748889729e-19, 9.698728412599989e-20], [5.3408770269572895e-12, 8.915781764932154e-12, 7.441770712813344e-12, 4.140968064809054e-12, 1.7281790694226278e-12, 5.769864146253787e-13, 1.605318417482594e-13, 3.828335576792237e-14, 7.988529869094049e-15, 1.4817372705725225e-15, 2.473534977628401e-16, 3.7538094377229826e-17, 5.222011535582908e-18, 6.705656852613302e-19, 7.531942112367027e-20, 7.986241280283636e-21], [4.104658059591208e-13, 6.852102247303389e-13, 5.719271194562814e-13, 3.182484422677612e-13, 1.32816840940516e-13, 4.4343502483073255e-14, 1.2337455341644636e-14, 2.942214995924054e-15, 6.139475473027814e-16, 1.1387689323596214e-16, 1.9010015078717083e-17, 2.884938950091726e-18, 4.0133056104120734e-19, 5.1535409458047274e-20, 6.1450376244417734e-21, 6.442092714263603e-22]] |
| Legacy trial inputs | {"lambda_home": 1.1528045035132461, "lambda_away": 1.6693478842390606, "rho": -0.031918512138755184, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2777 |
| Legacy p draw | 0.2514 |
| Legacy p away | 0.4709 |
| Legacy p over 1 5 | 0.7752 |
| Legacy p under 3 5 | 0.6883 |
| Legacy p btts yes | 0.5601 |
| Legacy p over 2 5 | 0.5345 |
| Legacy goal margin distribution | {"-1": 0.21806600790845673, "-10": 3.1449138417947205e-06, "-11": 4.7049190651832726e-07, "-12": 6.466109604460518e-08, "-13": 8.214605161995874e-09, "-14": 9.64136938983464e-10, "-15": 9.509802055033214e-11, "-2": 0.1445272540194011, "-3": 0.07011273413526478, "-4": 0.02682854136336112, "-5": 0.008438880056269478, "-6": 0.002248228969353448, "-7": 0.0005187807207008432, "-8": 0.00010549163192635873, "-9": 1.9164084626220407e-05, "0": 0.25142760702525024, "1": 0.16658277400264848, "10": 8.643113014208815e-08, "11": 8.929402716676971e-09, "12": 8.474656972699479e-10, "13": 7.434890447265084e-11, "14": 6.0260872516876284e-12, "15": 4.104658059591208e-13, "2": 0.07679636852250366, "3": 0.02572744446443896, "4": 0.006798382889532556, "5": 0.0014767337040030115, "6": 0.0002716856659582403, "7": 4.329311427375049e-05, "8": 6.079415462820726e-06, "9": 7.626770996267694e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2597 |
| Legacy raw p draw | 0.2496 |
| Legacy raw p away | 0.4907 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1528 |
| Legacy lambda away | 1.6693 |
| Legacy model home team | Sassuolo |
| Legacy model away team | Lazio |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 55.8% |
| Market home draw odds | 1.73 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-26T10:49:50Z |
| Market reference home draw last update utc | 2026-10-26T10:49:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.0% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-26T10:49:50Z |
| Market reference draw away last update utc | 2026-10-26T10:49:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.2% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-26T10:49:50Z |
| Market reference home away last update utc | 2026-10-26T10:49:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home draw odds | 1.73 |
| Market reference dc home away odds | 1.32 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:50Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.19, "price": 1.67, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:50Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.67, "price": 2.19, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:50Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.73, "price": 2.1, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:50Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.1, "price": 1.73, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 79.7% |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.55 |
| Market reference over 1 5 last update utc | 2026-10-26T10:50:15Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.6% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-26T10:50:11Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market reference under 3 5 last update utc | 2026-10-26T10:50:15Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.6% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-26T10:49:50Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.48 |
| Market reference btts yes last update utc | 2026-10-26T10:50:11Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 9.18124820101368, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,443.6151 |
| Elo away rating | 1,575.6104 |
| Elo rating diff | -71.9952 |
| Elo home expectancy | 0.3978 |

</details>


---

## 2026-10-27 — Torino vs Como

The model's most likely 1X2 outcome is **Como win** at **55.0%**. Expected goals are 0.92 for Torino and 1.57 for Como (2.49 combined). The most likely exact score is 0-1 at 13.3%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 46.3%; Under 3.5 goals: 75.6%; Double Chance 1X: 45.0%; Double Chance X2: 78.9%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 88.9%; BTTS Yes (both teams score): 47.4%; BTTS No (at least one team does not score): 52.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 21.1% | 4.74 |
| Draw | 23.9% | 4.19 |
| Como win | 55.0% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 0.92 |
| Como expected goals | 1.57 |
| Expected total goals | 2.49 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 71.7% |
| Under 1.5 | 28.3% |
| Over 2.5 | 46.3% |
| Under 2.5 | 53.7% |
| Over 3.5 | 24.4% |
| Under 3.5 | 75.6% |
| Over 4.5 | 11.1% |
| Under 4.5 | 88.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.35% |
| 2 | 1-1 | 11.29% |
| 3 | 0-2 | 10.74% |
| 4 | 1-2 | 9.89% |
| 5 | 0-0 | 7.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 21.1% | 20.8% | 5.05 | +6.6% |
| Draw | 23.9% | 23.0% | 3.75 | -10.5% |
| Como win | 55.0% | 56.2% | 1.75 | -3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7d989a0a7bae47eb957731e97c5bd9c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T10:50:11Z |
| Market best draw last update utc | 2026-10-26T10:50:11Z |
| Market best away last update utc | 2026-10-26T10:50:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Torino |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9206 |
| Dc lambda away | 1.5743 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:49:44.033835+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.4% |
| P btts no | 52.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.70 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.53 |
| Fair Over 2.5 odds | 2.16 |
| Fair Under 2.5 odds | 1.86 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.03 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.25937966992411515, "-10": 2.5471697781649573e-06, "-11": 3.606251433709435e-07, "-12": 4.687901375349449e-08, "-13": 5.631772911064988e-09, "-14": 6.264968705533752e-10, "-15": 5.996015571642434e-11, "-2": 0.16970935471452325, "-3": 0.08001994064034149, "-4": 0.02945494503126589, "-5": 0.00886015212245722, "-6": 0.0022490833318657604, "-7": 0.0004933033198833548, "-8": 9.519042053764662e-05, "-9": 1.6390477869876964e-05, "0": 0.23864809035710868, "1": 0.13888676164956937, "10": 1.0991291549595898e-08, "11": 9.099351046154869e-10, "12": 6.916660603200267e-11, "13": 4.858774192344154e-12, "14": 3.1605602213180575e-13, "15": 1.7687705480291952e-14, "2": 0.053578180189363805, "3": 0.014772159339442554, "4": 0.003179563900353109, "5": 0.0005592604421178704, "6": 8.301222460878625e-05, "7": 1.0646678162643281e-05, "8": 1.201315043453503e-06, "9": 1.2095361925076443e-07} |
| Raw goal margin distribution | {"-1": 0.24683906700899064, "-10": 2.424018088000814e-06, "-11": 3.4318947955986703e-07, "-12": 4.461248647821795e-08, "-13": 5.359485465381666e-09, "-14": 5.962067229736648e-10, "-15": 5.7061175608273623e-11, "-2": 0.16150417182922044, "-3": 0.07615110118520634, "-4": 0.02803084433119177, "-5": 0.008431777571869503, "-6": 0.0021403436569475015, "-7": 0.000469452872956733, "-8": 9.058811201579685e-05, "-9": 1.5598023802002655e-05, "0": 0.2587781127379047, "1": 0.14314751164550554, "10": 1.13284809610924e-08, "11": 9.378499753147898e-10, "12": 7.128849016890368e-11, "13": 5.0078310345831514e-12, "14": 3.25751947639893e-13, "15": 1.8230326606727494e-14, "2": 0.05522184462730418, "3": 0.015225337720866016, "4": 0.0032771061478258394, "5": 0.0005764173611660176, "6": 8.55588628301954e-05, "7": 1.0973295569510847e-05, "8": 1.2381688299895248e-06, "9": 1.2466421863842573e-07} |
| Unadjusted home-win probability | 21.8% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 52.4% |
| Raw p over 1 5 | 71.5% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 48.0% |
| P home draw | 45.0% |
| P draw away | 78.9% |
| P home away | 76.1% |
| Raw p home draw | 47.6% |
| Raw p draw away | 78.2% |
| Raw p home away | 74.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.4626 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.35, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.1, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.34, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.75, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:48:27Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.38, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.38, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.10 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.68 |
| Market reference 1x2 last update utc | 2026-10-26T10:50:13Z |
| Market reference home last update utc | 2026-10-26T10:50:13Z |
| Market reference draw last update utc | 2026-10-26T10:50:13Z |
| Market reference away last update utc | 2026-10-26T10:50:13Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-10-26T10:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-26T10:50:12Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.9% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | 0.0093 |
| Raw ev home | 0.0986 |
| Raw edge prob draw | 0.0288 |
| Raw ev draw | -0.0296 |
| Raw edge prob away | -0.0380 |
| Raw ev away | -0.0836 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.0862653913484595, 0.13703519358111294, 0.10502195911998316, 0.05206730480923003, 0.019360267029965093, 0.005759006591101426, 0.0014275869260573875, 0.0003033267827722258, 5.639323499964885e-05, 9.319459728578367e-06, 1.3861076895095862e-06, 1.8741766572055925e-07, 2.3229267501471475e-08, 2.657653756697762e-09, 2.823427242948996e-10, 2.7995715962098722e-11], [0.0749837419233787, 0.11779687146448349, 0.0975590668783216, 0.04836738635064268, 0.017984520587743837, 0.005349769837487762, 0.0013261421664657335, 0.00028177228966614276, 5.238591463076992e-05, 8.65721609603075e-06, 1.2876104570371798e-06, 1.7409970959808439e-07, 2.157858871325577e-08, 2.468800075352671e-09, 2.622793647433725e-10, 2.600633190181267e-11], [0.036563473828501426, 0.0543818136511219, 0.03942957722418027, 0.022465192609485977, 0.008353267552311366, 0.00248480678580194, 0.0006159530511165993, 0.00013087473268610185, 2.4331677830855092e-05, 4.021015848351475e-06, 5.980562338767795e-07, 8.086406573681997e-08, 1.0022603829982013e-08, 1.1466831969177571e-09, 1.218208568008595e-10, 1.2079157037863764e-11], [0.011321754099264994, 0.016839141830941536, 0.012522648660112372, 0.006053037578124146, 0.002586560609536991, 0.0007694118875298236, 0.00019072774688049814, 4.052491150674163e-05, 7.534220476850392e-06, 1.2450937478702002e-06, 1.8518605888610464e-07, 2.5039280239981474e-08, 3.103464854834299e-09, 3.55066513815271e-10, 3.77214099330461e-11, 3.7402694927333915e-12], [0.0026293067054867438, 0.003910636827345617, 0.0029081963628432438, 0.0014418122432496249, 0.0005226935566427808, 0.00017868431140848672, 4.429364384692193e-05, 9.411299753529358e-06, 1.7497091216355169e-06, 2.8915425220613726e-07, 4.300667035539202e-08, 5.814995349512057e-09, 7.207329254384716e-10, 8.245884493542406e-11, 8.760228777960405e-12, 8.686212022755246e-13], [0.0004884934748382398, 0.0007265491578574919, 0.0005403078095958513, 0.00026787132566147016, 9.960301216815554e-05, 2.888689726488543e-05, 8.229224818420255e-06, 1.7485059881953755e-06, 3.2507485224157974e-07, 5.372137268340484e-08, 7.990120665378601e-09, 1.0803560035517013e-09, 1.3390348506816448e-10, 1.531985888508052e-11, 1.627544853247399e-12, 1.6137934328174548e-13], [7.563016341328738e-05, 0.00011248672575359236, 8.36522288178797e-05, 4.147271801372484e-05, 1.542086532318111e-05, 4.587171494031172e-06, 1.1086441129308742e-06, 2.7070943713243624e-07, 5.03291557880526e-08, 8.317319276736361e-09, 1.237056711585707e-09, 1.6726426309010162e-10, 2.0731377140027263e-11, 2.3718708450114233e-12, 2.519818371254934e-13, 2.4985279707101588e-14], [1.003655158309154e-05, 1.4927626418967282e-05, 1.1101125155359927e-05, 5.503664871926349e-06, 2.046436280009717e-06, 6.087436710766427e-07, 1.509000714623229e-07, 3.1260061939240014e-08, 6.678964389378725e-09, 1.103755435484622e-09, 1.6416444096771881e-10, 2.2196916266568063e-11, 2.7511713139820155e-12, 3.1476071199663346e-13, 3.3439418773857394e-14, 3.3156883084856402e-15], [1.165418898256204e-06, 1.733358095232776e-06, 1.289034479707092e-06, 6.390715972822273e-07, 2.3762698722321668e-07, 7.06857701664948e-08, 1.7522133331798448e-08, 3.7230183562403628e-09, 6.748443547974229e-10, 1.2816527996865598e-10, 1.9062358255375245e-11, 2.577449583744448e-12, 3.1945903083451035e-13, 3.654921505185565e-14, 3.882900442758704e-15, 3.8500931155938325e-16], [1.202893197965949e-07, 1.7890946041071887e-07, 1.3304836654900048e-07, 6.596210843450969e-08, 2.4526793499886267e-08, 7.295868657483248e-09, 1.8085561363566627e-09, 3.842732826217974e-10, 7.144246654688006e-11, 1.1510981593416948e-11, 1.9675312556618628e-12, 2.66032803915007e-13, 3.2973130588032414e-14, 3.772446306015425e-15, 4.0077559562163657e-16, 3.973893702267063e-17], [1.1174152427852417e-08, 1.6619609993594728e-08, 1.235939093021122e-08, 6.127482101953041e-09, 2.2783912121011693e-09, 6.777422019690943e-10, 1.6800395892295382e-10, 3.56966706705804e-11, 6.636574322362934e-12, 1.096750117870765e-12, 1.5903990898737508e-13, 2.4712843224834757e-14, 3.063004993603656e-15, 3.5043751282812076e-16, 3.722963603428973e-17, 3.691507611507164e-18], [9.436467063668395e-10, 1.4035104973569102e-09, 1.0437389877484892e-09, 5.174601242611682e-10, 1.924080038281375e-10, 5.7234694155399276e-11, 1.4187776971707608e-11, 3.0145504031780022e-12, 5.604524854383198e-13, 9.261952019345226e-14, 1.3775544170779555e-14, 1.8159944096934606e-15, 2.586679027748669e-16, 2.9594119724318013e-17, 3.1440078923055928e-18, 3.1174436017572303e-19], [7.304924045358805e-11, 1.0864805134041711e-10, 8.079754824808793e-11, 4.005743758470023e-11, 1.4894619397285927e-11, 4.430631620325924e-12, 1.0982991033778364e-12, 2.333612948314626e-13, 4.3385546831633126e-14, 7.169829085036058e-15, 1.0663874856138224e-15, 1.4418782524615439e-16, 1.742391622195244e-17, 2.2909293840247617e-18, 2.4338281155800205e-19, 2.4132642622368818e-20], [5.219872253046059e-12, 7.763652914361148e-12, 5.77354230647074e-12, 2.8623803023571444e-12, 1.0643233253187862e-12, 3.1659919959197633e-13, 7.848104894273052e-14, 1.667527465394503e-14, 3.1001966712242312e-15, 5.123337582659842e-16, 7.620074367080888e-17, 1.0303214976035894e-17, 1.2770201564689014e-18, 1.4244684303795735e-19, 1.739138117017275e-20, 1.7244438249459215e-21], [3.463533249198331e-13, 5.151403846796036e-13, 3.8309090289413603e-13, 1.8992704933112205e-13, 7.062087052011272e-14, 2.100725460889383e-14, 5.207440130100636e-15, 1.1064517559744804e-15, 2.057068397329678e-16, 3.399479758159742e-17, 5.056135409510701e-18, 6.836475283914122e-19, 8.473390836807261e-20, 9.694381877509786e-21, 1.0041313268339504e-21, 1.1442173743983084e-22], [2.144942351264492e-14, 3.1902290188832866e-14, 2.3724556482660527e-14, 1.1762051709921273e-14, 4.3735020039671004e-15, 1.3009648486799427e-15, 3.2249319042375173e-16, 6.8521797259199e-17, 1.2739283290846043e-17, 2.1052744642283823e-18, 3.131229930042609e-19, 4.233782185643644e-20, 5.247512744071718e-21, 6.003664108960025e-22, 6.378147928425036e-23, 6.1659749686285675e-24]] |
| Legacy trial inputs | {"lambda_home": 0.9289396969529434, "lambda_away": 1.4873262290721125, "rho": -0.031918512138755184, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2200 |
| Legacy p draw | 0.2501 |
| Legacy p away | 0.5299 |
| Legacy p over 1 5 | 0.7017 |
| Legacy p under 3 5 | 0.7730 |
| Legacy p btts yes | 0.4666 |
| Legacy p over 2 5 | 0.4423 |
| Legacy goal margin distribution | {"-1": 0.25983320473324373, "-10": 1.5705939910595891e-06, "-11": 2.1018152766186808e-07, "-12": 2.582362870311774e-08, "-13": 2.9320122784789984e-09, "-14": 3.0834905619671223e-10, "-15": 2.7995715962098722e-11, "-2": 0.16255811851254484, "-3": 0.07273710478835656, "-4": 0.025368319520147415, "-5": 0.007223855025155371, "-6": 0.001734980095378675, "-7": 0.00035992485061476316, "-8": 6.56742829178782e-05, "-9": 1.0691121827582268e-05, "0": 0.25009759865984615, "1": 0.14343436135716775, "10": 1.2661394775595141e-08, "11": 1.0582626005650624e-09, "12": 8.120774632255326e-11, "13": 5.758737194208323e-12, "14": 3.7825561510866596e-13, "15": 2.144942351264492e-14, "2": 0.05659473087007882, "3": 0.015816290421090867, "4": 0.0034452568509523345, "5": 0.000612745616304449, "6": 9.19151231614847e-05, "7": 1.1909282445210958e-05, "8": 1.357220426215954e-06, "9": 1.379938118685959e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2317 |
| Legacy raw p draw | 0.2702 |
| Legacy raw p away | 0.4981 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9289 |
| Legacy lambda away | 1.4873 |
| Legacy model home team | Torino |
| Legacy model away team | Como |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 46.1% |
| Market home draw odds | 2.16 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-26T10:49:48Z |
| Market reference home draw last update utc | 2026-10-26T10:49:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 79.4% |
| Market draw away odds | 1.20 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-26T10:49:48Z |
| Market reference draw away last update utc | 2026-10-26T10:49:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.5% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-26T10:49:48Z |
| Market reference home away last update utc | 2026-10-26T10:49:49Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.22 |
| Market reference dc home draw odds | 2.10 |
| Market reference dc home away odds | 1.30 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:48Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.75, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:48Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.07, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:48Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.66, "price": 2.2, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:49:48Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.2, "price": 1.66, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 79.7% |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.55 |
| Market reference over 1 5 last update utc | 2026-10-26T10:50:15Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.4% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-26T10:50:11Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.75 |
| Market reference under 3 5 last update utc | 2026-10-26T10:50:15Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.5% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-26T10:49:48Z |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.36 |
| Market reference btts yes last update utc | 2026-10-26T10:50:11Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.659272328120286, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,450.2772 |
| Elo away rating | 1,583.3267 |
| Elo rating diff | -73.0494 |
| Elo home expectancy | 0.3964 |

</details>


---

## 2026-10-28 — AC Milan vs Bologna

The model's most likely 1X2 outcome is **AC Milan win** at **57.5%**. Expected goals are 1.57 for AC Milan and 1.03 for Bologna (2.60 combined). The most likely exact score is 1-0 at 12.2%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 51.7%; Under 3.5 goals: 70.7%; Double Chance 1X: 80.8%; Double Chance X2: 42.5%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 85.8%; BTTS Yes (both teams score): 52.5%; BTTS No (at least one team does not score): 47.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 57.5% | 1.74 |
| Draw | 23.3% | 4.30 |
| Bologna win | 19.2% | 5.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.57 |
| Bologna expected goals | 1.03 |
| Expected total goals | 2.60 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 51.7% |
| Under 2.5 | 48.3% |
| Over 3.5 | 29.3% |
| Under 3.5 | 70.7% |
| Over 4.5 | 14.2% |
| Under 4.5 | 85.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.17% |
| 2 | 1-1 | 11.08% |
| 3 | 2-1 | 10.94% |
| 4 | 2-0 | 10.22% |
| 5 | 0-0 | 6.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 57.5% | 60.9% | 1.62 | -6.9% |
| Draw | 23.3% | 22.2% | 4.14 | -3.6% |
| Bologna win | 19.2% | 17.0% | 5.57 | +7.1% |
| Over 2.5 | 51.7% | 52.6% | 1.88 | -2.7% |
| Under 2.5 | 48.3% | 47.4% | 2.01 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 3d0b0fbec194258530882514714c74be |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T10:50:11Z |
| Market best draw last update utc | 2026-10-26T10:50:11Z |
| Market best away last update utc | 2026-10-26T10:50:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Milan |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5707 |
| Dc lambda away | 1.0281 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:49:44.033835+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.5% |
| P btts no | 47.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.55 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.17 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.42 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.02 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.11924686439691752, "-10": 3.346880048933412e-08, "-11": 3.21664653038423e-09, "-12": 2.8394489931256526e-10, "-13": 2.3167688956024732e-11, "-14": 1.7479516307478484e-12, "-15": 1.1175541307749455e-13, "-2": 0.05172177794731651, "-3": 0.01627163131893989, "-4": 0.004023236568049883, "-5": 0.0008160239436870079, "-6": 0.00014000222260961498, "-7": 2.0786554653507558e-05, "-8": 2.718087777853032e-06, "-9": 3.173914189595054e-07, "0": 0.2328285209503071, "1": 0.2681649756479383, "10": 3.3902322096702496e-06, "11": 4.977771719764464e-07, "12": 6.712867046355036e-08, "13": 8.367563677504366e-09, "14": 9.644685289360414e-10, "15": 9.420404614679899e-11, "2": 0.17657289553627953, "3": 0.08486410335840508, "4": 0.032056111468911394, "5": 0.009933001695687647, "6": 0.002603483778754645, "7": 0.0005905338478718758, "8": 0.00011796905475507327, "9": 2.1044671011187407e-05} |
| Raw goal margin distribution | {"-1": 0.1543498315152876, "-10": 3.128627163236802e-08, "-11": 2.889155613431795e-09, "-12": 2.450139725479661e-10, "-13": 1.920423710395109e-11, "-14": 1.3928069161372986e-12, "-15": 8.618529417813643e-14, "-2": 0.0652197726140151, "-3": 0.01986794396208158, "-4": 0.0047425553574093355, "-5": 0.0009270663013835894, "-6": 0.00015312765489998014, "-7": 2.1873049345727105e-05, "-8": 2.750359782279962e-06, "-9": 3.087240997650065e-07, "0": 0.25831881979597954, "1": 0.23732055939324448, "10": 2.1665922848790827e-06, "11": 3.0565862343525765e-07, "12": 3.960033945129795e-08, "13": 4.741846096924475e-09, "14": 5.253922323191617e-10, "15": 4.966703556852417e-11, "2": 0.15221727974896512, "3": 0.07084022641815226, "4": 0.025833411458192575, "5": 0.007714761157762673, "6": 0.0019467386885486406, "7": 0.000424820728382724, "8": 8.160715043646444e-05, "9": 1.399431275299556e-05} |
| Unadjusted home-win probability | 49.6% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.6% |
| Raw p btts yes | 51.2% |
| P home draw | 80.8% |
| P draw away | 42.5% |
| P home away | 76.7% |
| Raw p home draw | 75.5% |
| Raw p draw away | 50.4% |
| Raw p home away | 74.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED |
| Totals anchor scale | 1.0418 |
| Totals anchor target over 2 5 | 0.5174 |
| Totals anchor reference over odds | 1.88 |
| Totals anchor reference under odds | 2.01 |
| Totals anchor reference last update utc | 2026-10-26T10:50:11Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4929 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.8, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.13, "price": 1.8, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 3.85 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-26T10:50:12Z |
| Market reference home last update utc | 2026-10-26T10:50:12Z |
| Market reference draw last update utc | 2026-10-26T10:50:12Z |
| Market reference away last update utc | 2026-10-26T10:50:12Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-26T10:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-26T10:50:12Z |
| Market best over 2 5 last update utc | 2026-10-26T10:50:11Z |
| Market best under 2 5 last update utc | 2026-10-26T10:50:11Z |
| Home probability edge | -3.4% |
| Draw probability edge | +1.1% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.1122 |
| Raw ev home | -0.1958 |
| Raw edge prob draw | 0.0364 |
| Raw ev draw | 0.0694 |
| Raw edge prob away | 0.0758 |
| Raw ev away | 0.3662 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07048265335504174, 0.06008954554950424, 0.03278370648935979, 0.01131652307053387, 0.0029297410540085533, 0.0006067858539266492, 0.00010472742179202886, 1.5493109383620335e-05, 2.0055099226381126e-06, 2.3075893218566547e-07, 2.3896524152859813e-08, 2.2496671435009892e-09, 1.941391994428222e-10, 1.5464863715169876e-11, 1.1439163737731942e-12, 7.897310841754401e-14], [0.12308189519940707, 0.11421174677172904, 0.05233557442622311, 0.01806558192546709, 0.004677008715637152, 0.0009686667439285521, 0.00016718578722763023, 2.473304168652323e-05, 3.201575570865404e-06, 3.68381204054469e-07, 3.814816725302057e-08, 3.591345666211886e-09, 3.0992183647034627e-10, 2.468795058970392e-11, 1.8261364234825837e-12, 1.2607186422310098e-13], [0.10160164129908576, 0.10521482537110743, 0.045742567357778756, 0.014419855297938542, 0.0037331644884138647, 0.0007731848515593202, 0.0001334468421576759, 1.9741787652839506e-05, 2.5554812819073066e-06, 2.940399970984312e-07, 3.0449672417950156e-08, 2.866593782880046e-09, 2.4737802823133895e-10, 1.970579616947394e-11, 1.4576127738123244e-12, 1.0062991863415814e-13], [0.05406527438419776, 0.055987957775496706, 0.02898950806755732, 0.008402203274883438, 0.001986528562007148, 0.00041143480178834483, 7.101105892296642e-05, 1.0505196103509596e-05, 1.3598480784703934e-06, 1.5646748339683014e-07, 1.620318208580187e-08, 1.5254003521775753e-09, 1.3163725311856265e-10, 1.0486043957946065e-11, 7.756393849002126e-13, 5.354819166946085e-14], [0.02157731304975159, 0.022344651085156823, 0.011569638697973754, 0.003993693735815234, 0.0008681371853848692, 0.00016420257954603815, 2.8340332419047946e-05, 4.1925969590697125e-06, 5.427118982278745e-07, 6.244577336958816e-08, 6.466648625197052e-09, 6.087833882288962e-10, 5.2536091824196907e-11, 4.184953386645348e-12, 3.0955569933443867e-13, 2.1370946657726867e-14], [0.006889160463901179, 0.007134154585447847, 0.003693930625927472, 0.00127509838348593, 0.0003301109412064703, 5.740682231963591e-05, 9.048443482510893e-06, 1.3386037985775943e-06, 1.7327594700690858e-07, 1.9937559048412312e-08, 2.0646583724270213e-09, 1.9437111746008607e-10, 1.677361615362512e-11, 1.3361633743770704e-12, 9.88343117751933e-14, 6.823272223519412e-15], [0.0018329642414986048, 0.001898148594007954, 0.0009828255247327244, 0.0003392590074754732, 8.783095619988855e-05, 1.8190884715229137e-05, 2.636186698496879e-06, 3.5615557355409673e-07, 4.6102658871095e-08, 5.3046859613736145e-09, 5.493332587330085e-10, 5.171534467099814e-11, 4.46287160406883e-12, 3.555062621732561e-13, 2.6296347757657986e-14, 1.8154336890912584e-15], [0.00041801791523085, 0.0004328835773778394, 0.0002241389480400032, 7.736994525994556e-05, 2.0030348859065533e-05, 4.148534670075071e-06, 7.160109903688153e-07, 8.893961430227276e-08, 1.0513973437985833e-08, 1.2097637893441923e-09, 1.2527857248038742e-10, 1.1793978341411055e-11, 1.0177832396504125e-12, 8.107522405547682e-14, 5.997031594492235e-15, 4.1401997309741647e-16], [8.341494166148965e-05, 8.638136557675593e-05, 4.472664111656407e-05, 1.543907386516412e-05, 3.997030559361369e-06, 8.278348005584251e-07, 1.428790796146058e-07, 2.1137168959396394e-08, 2.2973672471242973e-09, 2.414068207019302e-10, 2.4999179303392202e-11, 2.3534733308317097e-12, 2.030973469464726e-13, 1.6178457521479686e-14, 1.1967000034446415e-15, 8.261715740948649e-17], [1.4795862386365042e-05, 1.532203670424705e-05, 7.933461485240584e-06, 2.7385311040426603e-06, 7.089798653867496e-07, 1.4683855846129795e-07, 2.534341159701591e-08, 3.7492400873422935e-09, 4.853214426709566e-10, 4.6887876416969075e-11, 4.434270520095818e-12, 4.1745120046091614e-13, 3.6024725745785296e-14, 2.8696804954067146e-15, 2.122666301270573e-16, 1.4654354093347827e-17], [2.361996369669438e-06, 2.445994300725887e-06, 1.266489694059273e-06, 4.371763103133807e-07, 1.1318082207600452e-07, 2.3441157599079757e-08, 4.045796360092817e-09, 5.985248608072001e-10, 7.747621975505251e-11, 8.914605476965252e-12, 7.751320977054706e-13, 6.664148356174808e-14, 5.7509504487076045e-15, 4.581128652905155e-16, 3.388602817934487e-17, 2.3394061302054107e-18], [3.427878996687915e-07, 3.549782123776098e-07, 1.838010200834924e-07, 6.344579996888327e-08, 1.642551901451501e-08, 3.401929521304993e-09, 5.871516377300564e-10, 8.68617253481931e-11, 1.124384058550817e-11, 1.2937441086128707e-12, 1.339752574093772e-13, 1.0590232826822373e-14, 8.346144180093155e-16, 6.648424566637459e-17, 4.917755411004605e-18, 3.3950946078618955e-19], [4.560192535822471e-08, 4.72236329236845e-08, 2.4451506038315612e-08, 8.440352291517253e-09, 2.1851275753716716e-09, 4.5256713044534386e-10, 7.811024013273573e-11, 1.155543098120492e-11, 1.4957960290183567e-12, 1.7210999084451753e-13, 1.7823061123611747e-14, 1.6778990429702596e-15, 1.215788898600346e-16, 8.84456426643205e-18, 6.5422121200696205e-19, 4.5165786494045516e-20], [5.599880630522333e-09, 5.799025046308539e-09, 3.002625743879206e-09, 1.0364686346193406e-09, 2.683319506450862e-10, 5.557488829437918e-11, 9.591876161559146e-12, 1.4189978519693418e-12, 1.8368257796819935e-13, 2.1134971746883952e-14, 2.1886579125485977e-15, 2.0604468510684185e-16, 1.7781008329009756e-17, 1.1892868757730222e-18, 8.0337851185353e-20, 5.546323120427104e-21], [6.38542305876821e-10, 6.612503139306919e-10, 3.4238293504533064e-10, 1.1818628209885637e-10, 3.059731337333108e-11, 6.337084602646175e-12, 1.0937409430664221e-12, 1.6180526340009558e-13, 2.0944928048273904e-14, 2.4099752270322826e-15, 2.4956793947301933e-16, 2.3494830876334973e-17, 2.0275300150749468e-18, 1.6151027433686915e-19, 1.0031034228941195e-20, 6.324352585574857e-22], [6.79574946462195e-11, 7.037421679844745e-11, 3.6438441527143584e-11, 1.2578091630061821e-11, 3.2563492514432718e-12, 6.744304785970486e-13, 1.1640245853518403e-13, 1.7220284732963813e-14, 2.2290846238473084e-15, 2.564839903030033e-16, 2.656051408734293e-17, 2.5004605470892178e-18, 2.1578188144527546e-19, 1.718889023098579e-20, 1.2714404306665281e-21, 7.370184361507604e-23]] |
| Legacy trial inputs | {"lambda_home": 1.5963897933020181, "lambda_away": 1.035562260863341, "rho": -0.031918512138755184, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-26T10:50:11Z", "over": 1.88, "under": 2.01, "bookmaker": "pinnacle", "event_id": "3d0b0fbec194258530882514714c74be", "kickoff_utc": "2026-10-28T17:30:00Z", "home_team": "AC Milan", "away_team": "Bologna"}} |
| Legacy p home | 0.5544 |
| Legacy p draw | 0.2398 |
| Legacy p away | 0.2059 |
| Legacy p over 1 5 | 0.7463 |
| Legacy p under 3 5 | 0.7252 |
| Legacy p btts yes | 0.5121 |
| Legacy p over 2 5 | 0.4977 |
| Legacy goal margin distribution | {"-1": 0.12900512177415713, "-10": 2.7746050270232546e-08, "-11": 2.5800917864723673e-09, "-12": 2.203383109980079e-10, "-13": 1.7391630057286618e-11, "-14": 1.2699882379962952e-12, "-15": 7.897310841754401e-14, "-2": 0.05502361397909182, "-3": 0.016842099001913878, "-4": 0.0040429230469888056, "-5": 0.0007951378400668524, "-6": 0.00013217907780875706, "-7": 1.9005554052260267e-05, "-8": 2.405920098428276e-06, "-9": 2.719096160778168e-07, "0": 0.23976744223849125, "1": 0.26162896184233975, "10": 2.742493828463835e-06, "11": 3.931356009677055e-07, "12": 5.175591143120864e-08, "13": 6.297569385980168e-09, "14": 7.089165226752684e-10, "15": 6.79574946462195e-11, "2": 0.1705264623540198, "3": 0.0804639992397718, "4": 0.0297758111084852, "5": 0.009027620099730472, "6": 0.0023134296533990875, "7": 0.0005127868064452154, "8": 0.00010006915567318975, "9": 1.7434372844903646e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5002 |
| Legacy raw p draw | 0.2576 |
| Legacy raw p away | 0.2422 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5964 |
| Legacy lambda away | 1.0356 |
| Legacy model home team | Milan |
| Legacy model away team | Bologna |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.48822513904177, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,555.5771 |
| Elo away rating | 1,508.2638 |
| Elo rating diff | 107.3133 |
| Elo home expectancy | 0.6497 |

</details>


---

## 2026-10-28 — Genoa vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **56.5%**. Expected goals are 0.78 for Genoa and 1.43 for Juventus (2.21 combined). The most likely exact score is 0-1 at 16.7%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.4%; Double Chance 1X: 43.5%; Double Chance X2: 81.6%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 40.7%; BTTS No (at least one team does not score): 59.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 18.4% | 5.42 |
| Draw | 25.0% | 4.00 |
| Juventus win | 56.5% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 0.78 |
| Juventus expected goals | 1.43 |
| Expected total goals | 2.21 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 65.6% |
| Under 1.5 | 34.4% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.6% |
| Under 3.5 | 81.4% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.65% |
| 2 | 0-2 | 12.16% |
| 3 | 1-1 | 11.33% |
| 4 | 0-0 | 10.19% |
| 5 | 1-2 | 9.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 18.4% | 17.8% | 5.43 | +0.1% |
| Draw | 25.0% | 23.9% | 3.80 | -4.9% |
| Juventus win | 56.5% | 58.3% | 1.70 | -3.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | 34848497b90b1392f6a767fc183d3ac1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T10:50:11Z |
| Market best draw last update utc | 2026-10-26T10:50:11Z |
| Market best away last update utc | 2026-10-26T10:50:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Genoa |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7775 |
| Dc lambda away | 1.4336 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:49:44.033835+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 40.7% |
| P btts no | 59.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.81 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.91 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.37 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.08 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.28037948880265656, "-10": 1.3233472446934165e-06, "-11": 1.7103957217709795e-07, "-12": 2.028854594106989e-08, "-13": 2.2178401229470063e-09, "-14": 2.103658083861024e-10, "-2": 0.1736088704631456, "-3": 0.07624411066307471, "-4": 0.0259320709715831, "-5": 0.007175647808340585, "-6": 0.001671063196515907, "-7": 0.00033566467010990626, "-8": 5.924702043452307e-05, "-9": 9.323387004155107e-06, "0": 0.2502059574079192, "1": 0.12828865215861532, "10": 2.480169793487716e-09, "11": 1.7384022485843219e-10, "12": 1.1182802976333965e-11, "13": 6.629428085362025e-13, "14": 3.4100995587568024e-14, "2": 0.04349215134322081, "3": 0.01035836855463629, "4": 0.0019105936718078853, "5": 0.00028670701905842333, "6": 3.620896925821161e-05, "7": 3.944345936905508e-06, "8": 3.7755650425949174e-07, "9": 3.2220719260200475e-08} |
| Raw goal margin distribution | {"-1": 0.2595835056633636, "-10": 1.2251934635249087e-06, "-11": 1.5835342286447713e-07, "-12": 1.8783727378510116e-08, "-13": 2.053341050638204e-09, "-14": 1.9476279896853315e-10, "-2": 0.1607321541298606, "-3": 0.07058902067560534, "-4": 0.02400866739810858, "-5": 0.006643423958896356, "-6": 0.001547119029958498, "-7": 0.00031076813844893624, "-8": 5.485261896360489e-05, "-9": 8.6318635272863e-06, "0": 0.27612361432247445, "1": 0.139435150948026, "10": 2.6956620380119113e-09, "11": 1.8894452148429136e-10, "12": 1.2154432950930697e-11, "13": 7.205433140248794e-13, "14": 3.706389760297437e-14, "2": 0.04727101411977169, "3": 0.011258366649649161, "4": 0.002076597676772654, "5": 0.00031161786960582017, "6": 3.935502485402106e-05, "7": 4.287054714891383e-06, "8": 4.103609109381064e-07, "9": 3.50202514260207e-08} |
| Unadjusted home-win probability | 20.0% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 52.3% |
| Raw p over 1 5 | 65.1% |
| Raw p under 3 5 | 81.7% |
| Raw p btts yes | 41.5% |
| P home draw | 43.5% |
| P draw away | 81.6% |
| P home away | 75.0% |
| Raw p home draw | 47.7% |
| Raw p draw away | 80.0% |
| Raw p home away | 72.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.3904 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.70 |
| Reference draw odds | 3.60 |
| Reference away odds | 1.62 |
| Market reference 1x2 last update utc | 2026-10-26T10:50:12Z |
| Market reference home last update utc | 2026-10-26T10:50:12Z |
| Market reference draw last update utc | 2026-10-26T10:50:12Z |
| Market reference away last update utc | 2026-10-26T10:50:12Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.75 |
| Market reference over 2 5 last update utc | 2026-10-26T10:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-26T10:50:12Z |
| Home probability edge | +0.7% |
| Draw probability edge | +1.1% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
| Raw edge prob home | 0.0229 |
| Raw ev home | 0.0882 |
| Raw edge prob draw | 0.0370 |
| Raw ev draw | 0.0493 |
| Raw edge prob away | -0.0599 |
| Raw ev away | -0.1101 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.10752238212589126, 0.1645203738278328, 0.11984072122720252, 0.05677063635807888, 0.020169929216240796, 0.00573290800578134, 0.001357889172969427, 0.00027568103371046444, 4.8973089724833256e-05, 7.7331351136456e-06, 1.0989962266974758e-06, 1.419855405632154e-07, 1.6815255717915993e-08, 1.8382337139876811e-09, 1.8660071107473128e-10], [0.07776576767680855, 0.11697628977565784, 0.09199904284338391, 0.04358154851764642, 0.01548400379362665, 0.0044010253262839775, 0.0010424211647036131, 0.00021163416718223484, 3.759554626866786e-05, 5.936554965195492e-06, 8.436748369777686e-07, 1.0899912563653052e-07, 1.2908695937185837e-08, 1.4111709315290568e-09, 1.4324919473927006e-10], [0.03126786438639312, 0.04443639542376324, 0.030918039344781878, 0.016728290301485038, 0.005943361796430961, 0.0016892843826431826, 0.00040012171326389345, 8.123340970557672e-05, 1.4430630241845109e-05, 2.27868027241625e-06, 3.2383515669039715e-07, 4.183809612725508e-08, 4.954858659127487e-09, 5.416621898617651e-10, 5.49846023502857e-11], [0.00800121351587221, 0.01137094248803188, 0.008079920177710313, 0.0037479081066290492, 0.001520861999005475, 0.00043227528645795174, 0.00010238816506938005, 2.0787024263783476e-05, 3.692690754532354e-06, 5.83097302991451e-07, 8.286700366250026e-08, 1.0706057058294973e-08, 1.2679114116248893e-09, 1.3860731839571704e-10, 1.4070150044574699e-11], [0.0015355881905329812, 0.002182304592323836, 0.00155069352676668, 0.0007345905249017756, 0.0002555573931529032, 8.296201865220841e-05, 1.9650276401071942e-05, 3.98943346686941e-06, 7.086990370525155e-07, 1.1190769133070645e-07, 1.5903786588941852e-08, 2.054700171827361e-09, 2.433368121561672e-10, 2.660143499828925e-11, 2.7003349185240128e-12], [0.00023576734566342194, 0.00033506129073752883, 0.0002380865514577414, 0.00011278574508018246, 4.007142848495702e-05, 1.1152389753350456e-05, 3.017015588681558e-06, 6.125197790549315e-07, 1.088104817881549e-07, 1.7181806624342826e-08, 2.441796292253925e-09, 3.154694784920002e-10, 3.736084625940345e-11, 4.084265403348716e-12, 4.145973510786681e-13], [3.016555351225717e-05, 4.2869843858945305e-05, 3.0462287253300154e-05, 1.4430515892955912e-05, 5.126989986141633e-06, 1.457246657734688e-06, 3.3797527956703375e-07, 7.83696237509285e-08, 1.3921895764822648e-08, 2.1983481457342447e-09, 3.1241873853544675e-10, 4.036314447260073e-11, 4.780181088818602e-12, 5.225665421829058e-13, 5.304618646323405e-14], [3.3082030185562627e-06, 4.7014601207822e-06, 3.3407452842709303e-06, 1.5825692115015575e-06, 5.622679438442814e-07, 1.5981366925490217e-07, 3.785325893157645e-08, 7.525032049027025e-09, 1.526789739644519e-09, 2.410889615733563e-10, 3.426241170932085e-11, 4.42655482281879e-12, 5.242340241112976e-13, 5.730895047371009e-14, 5.817481655334565e-15], [3.174541884867314e-07, 4.511507301619557e-07, 3.205769347317541e-07, 1.518628759913784e-07, 5.395506648896246e-08, 1.533567268932079e-08, 3.6323875917826635e-09, 7.374536788962638e-10, 1.282767292533122e-10, 2.3134825831450695e-11, 3.2878109486543755e-12, 4.2477089863826546e-13, 5.03053427398217e-14, 5.499350028885934e-15, 5.582438283175978e-16], [2.7078053814847098e-08, 3.848203675675742e-08, 2.7344416313561995e-08, 1.2953526139233376e-08, 4.602233162952404e-09, 1.3080947910872049e-09, 3.0983363979393466e-10, 6.290296719126336e-11, 1.1174336568439272e-11, 1.7277557900711454e-12, 2.8044210796238314e-13, 3.623190264754896e-14, 4.290920791993753e-15, 4.6908089869187e-16, 4.7616812041596316e-17], [2.078721662818326e-09, 2.9541799415355963e-09, 2.0991697164349966e-09, 9.944132462261269e-10, 3.5330315238255927e-10, 1.004195130804359e-10, 2.3785235944702956e-11, 4.82892018200858e-12, 8.57828839962695e-13, 1.3545615277872842e-13, 1.8849587691200867e-14, 2.781442175777358e-15, 3.2940439755180207e-16, 3.601029203917271e-17, 3.655436220860975e-18], [1.4507165037570306e-10, 2.061689004791126e-10, 1.4649869707377777e-10, 6.939898369553509e-11, 2.465663023378799e-11, 7.0081650434873736e-12, 1.6599449049832324e-12, 3.370049164671404e-13, 5.986691137116384e-14, 9.45333278073936e-15, 1.343462502991285e-15, 1.6995579710406317e-16, 2.298876297323245e-17, 2.5131178406786034e-18, 2.551087886795027e-19], [9.280688596221256e-12, 1.3189271360853244e-11, 9.37198125045658e-12, 4.43967070688518e-12, 1.5773619893296912e-12, 4.483343039876443e-13, 1.0619188318418411e-13, 2.1559261764977553e-14, 3.8298741360869155e-15, 6.047593551688589e-16, 8.594551105382816e-17, 1.110378684613879e-17, 1.2876356393262596e-18, 1.6077203247184103e-19, 1.6320109544229784e-20], [5.480443985191761e-13, 7.788545230154693e-13, 5.53435423900632e-13, 2.6217199693229384e-13, 9.314657998989201e-14, 2.6475094107183447e-14, 6.270856536549535e-15, 1.273120256541674e-15, 2.2616221259384916e-16, 3.5712326043059985e-17, 5.075265205008234e-18, 6.557022272953975e-19, 7.765439060233201e-20, 8.312387527046145e-21, 9.637371759867254e-22], [3.005153100783132e-14, 4.270780052169456e-14, 3.0347143127675227e-14, 1.437597011571356e-14, 5.1076105228028095e-15, 1.4517384241989237e-15, 3.4385688488555235e-16, 6.981042588800694e-17, 1.2401405365930376e-17, 1.95825388662785e-18, 2.7829768918974855e-19, 3.5954853053355724e-20, 4.258109987777882e-21, 4.654940411676993e-22, 4.6268903620026355e-23]] |
| Legacy trial inputs | {"lambda_home": 0.7676776466403736, "lambda_away": 1.4211522371544085, "rho": -0.031918512138755184, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1880 |
| Legacy p draw | 0.2594 |
| Legacy p away | 0.5525 |
| Legacy p over 1 5 | 0.6502 |
| Legacy p under 3 5 | 0.8191 |
| Legacy p btts yes | 0.4049 |
| Legacy p over 2 5 | 0.3821 |
| Legacy goal margin distribution | {"-1": 0.27485462792577964, "-10": 1.213091518646448e-06, "-11": 1.554499688403076e-07, "-12": 1.8281411251795336e-08, "-13": 1.9814829087269513e-09, "-14": 1.8660071107473128e-10, "-2": 0.16981818379022706, "-3": 0.07405041317640641, "-4": 0.024992589477792197, "-5": 0.00686036966132561, "-6": 0.001584553291790614, "-7": 0.00031564021984461317, "-8": 5.524443337790118e-05, "-9": 8.619942974194597e-06, "0": 0.2594316747662014, "1": 0.1310582410803503, "10": 2.29452982415535e-09, "11": 1.5882873313057265e-10, "12": 1.00898902623644e-11, "13": 5.907521990408707e-13, "14": 3.005153100783132e-14, "2": 0.04430757664608517, "3": 0.010436613093886313, "4": 0.0019027496250226985, "5": 0.0002821345020170378, "6": 3.520090451270519e-05, "7": 3.787717689583211e-06, "8": 3.5810639812455967e-07, "9": 3.0183266722481773e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1985 |
| Legacy raw p draw | 0.2798 |
| Legacy raw p away | 0.5217 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.7677 |
| Legacy lambda away | 1.4212 |
| Legacy model home team | Genoa |
| Legacy model away team | Juventus |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.377265699704468, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,403.5919 |
| Elo away rating | 1,567.4383 |
| Elo rating diff | -103.8464 |
| Elo home expectancy | 0.3548 |

</details>


---

## 2026-10-28 — Monza vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **57.3%**. Expected goals are 0.88 for Monza and 2.01 for Napoli (2.88 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.1%; Under 3.5 goals: 68.1%; Double Chance 1X: 42.7%; Double Chance X2: 79.8%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 20.2% | 4.94 |
| Draw | 22.4% | 4.46 |
| Napoli win | 57.3% | 1.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 0.88 |
| Napoli expected goals | 2.01 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 31.9% |
| Under 3.5 | 68.1% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.68% |
| 2 | 0-2 | 10.17% |
| 3 | 0-1 | 9.92% |
| 4 | 1-2 | 8.93% |
| 5 | 0-3 | 6.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 20.2% | 22.3% | 4.19 | -15.2% |
| Draw | 22.4% | 23.0% | 4.06 | -8.9% |
| Napoli win | 57.3% | 54.7% | 1.81 | +3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | abec89862e33762414fcb8b2232aba08 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T10:50:11Z |
| Market best draw last update utc | 2026-10-26T10:50:11Z |
| Market best away last update utc | 2026-10-26T10:50:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Monza |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8781 |
| Dc lambda away | 2.0065 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:49:44.033835+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.21 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.14 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.24 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.21888603895653436, "-10": 1.7260649653444136e-05, "-11": 3.1074989654110433e-06, "-12": 5.138543949654398e-07, "-13": 7.855769042136863e-08, "-14": 1.1166007724274922e-08, "-15": 1.4825863365523726e-09, "-16": 1.8389652196428994e-10, "-17": 1.9667040839294675e-11, "-2": 0.17617756807272447, "-3": 0.1037708935340904, "-4": 0.04804777502004644, "-5": 0.01825169729275616, "-6": 0.005865007615424762, "-7": 0.0016310589386222287, "-8": 0.00039950118720475124, "-9": 8.738306169400986e-05, "0": 0.22444619834018523, "1": 0.1376180594207745, "10": 6.4684638562268885e-09, "11": 5.096193087340364e-10, "12": 3.6877869282346e-11, "13": 2.46720544884277e-12, "14": 1.534636050707051e-13, "15": 8.916991015971722e-15, "16": 4.840193395446476e-16, "17": 2.26526535188617e-17, "2": 0.049087139063016, "3": 0.012652709296426716, "4": 0.0025637290146761824, "5": 0.00042617989494419606, "6": 5.9930671599494026e-05, "7": 7.2935855660144575e-06, "8": 7.817724568475807e-07, "9": 7.483080409756624e-08} |
| Raw goal margin distribution | {"-1": 0.24219093254795065, "-10": 1.9098398673024642e-05, "-11": 3.438355757692442e-06, "-12": 5.685647001691866e-07, "-13": 8.692176254211711e-08, "-14": 1.2354857516137769e-08, "-15": 1.6404379609782765e-09, "-16": 2.034760661720425e-10, "-17": 2.1760999395092815e-11, "-2": 0.19493527183812842, "-3": 0.11481942656628802, "-4": 0.05316344292415085, "-5": 0.020194963593787304, "-6": 0.00648945757597004, "-7": 0.0018047185068026717, "-8": 0.00044203625568986374, "-9": 9.668677500610214e-05, "0": 0.21190071278953776, "1": 0.10465979110755377, "10": 4.9193258416000526e-09, "11": 3.8757013883912257e-10, "12": 2.8045956408824093e-11, "13": 1.8763322777702445e-12, "14": 1.1671047329771835e-13, "15": 6.781453109915401e-15, "16": 3.6810112845634155e-16, "17": 1.722754989639074e-17, "2": 0.03733121758892612, "3": 0.009622500981936686, "4": 0.001949739331172977, "5": 0.00032411370256806184, "6": 4.557782312102267e-05, "7": 5.54683843804376e-06, "8": 5.945450936576388e-07, "9": 5.690950997438127e-08} |
| Unadjusted home-win probability | 15.4% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 63.4% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 67.3% |
| Raw p btts yes | 50.8% |
| P home draw | 42.7% |
| P draw away | 79.8% |
| P home away | 77.6% |
| Raw p home draw | 36.6% |
| Raw p draw away | 84.6% |
| Raw p home away | 78.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.5409 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:50Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:50Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.85 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.72 |
| Market reference 1x2 last update utc | 2026-10-26T10:50:12Z |
| Market reference home last update utc | 2026-10-26T10:50:12Z |
| Market reference draw last update utc | 2026-10-26T10:50:12Z |
| Market reference away last update utc | 2026-10-26T10:50:12Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-26T10:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-26T10:50:12Z |
| Home probability edge | -2.1% |
| Draw probability edge | -0.5% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | -0.0693 |
| Raw ev home | -0.3550 |
| Raw edge prob draw | -0.0179 |
| Raw ev draw | -0.1397 |
| Raw edge prob away | 0.0872 |
| Raw ev away | 0.1478 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06676052526955026, 0.1093901532367938, 0.10877120671397555, 0.07015890240931431, 0.03394008214110798, 0.013135087764340246, 0.004236154808043146, 0.0011710188257151547, 0.0002832461296335765, 6.0899197398303176e-05, 1.1784242290264504e-05, 2.072998903229433e-06, 3.3427809652037917e-07, 4.975705440633786e-08, 6.8772802296229335e-09, 8.871877899459364e-10, 1.0729652770820541e-10], [0.060270810119185496, 0.10706894932678071, 0.09192188358844999, 0.05929086064955637, 0.028682556476193843, 0.011100382581694978, 0.003579948599371041, 0.0009896208696142136, 0.00023936957713011488, 5.146554040351198e-05, 9.958791307999744e-06, 1.751878733521093e-06, 2.8249638119135533e-07, 4.2049383297463215e-08, 5.811947589539087e-09, 7.497569918751883e-10, 9.067564135216416e-11], [0.02714374285591752, 0.05252424599074953, 0.04241829504984532, 0.025053172411790788, 0.012119726796618654, 0.004690432818976536, 0.0015126963667386525, 0.0004181612814712403, 0.0001011448850679332, 2.1746607198302124e-05, 4.208056906561837e-06, 7.402510180256936e-07, 1.1936798464649973e-07, 1.776783871948576e-08, 2.455820735503257e-09, 3.168075311879499e-10, 3.831471581720872e-11], [0.007646337195092418, 0.014795973344394414, 0.014315404985575188, 0.007707362076085778, 0.003414102406261945, 0.0013212853921876781, 0.00042612349207962394, 0.00011779518311211821, 2.8492308554996546e-05, 6.125975049575429e-06, 1.185401078049731e-06, 2.0852720727867213e-07, 3.362571866933122e-08, 5.0051640556117705e-09, 6.917997099380874e-10, 8.924403765045685e-11, 1.0793177574206571e-11], [0.0016154682354806778, 0.003125996714639928, 0.0030244653671670737, 0.0019508211496945898, 0.0007877362688061952, 0.00027915255718172975, 9.00285912434724e-05, 2.4886997755264038e-05, 6.019669058755781e-06, 1.2942560406946145e-06, 2.504438058424843e-07, 4.405626785703353e-08, 7.104222455737202e-09, 1.0574584064118993e-09, 1.46158929197762e-10, 1.885489801873852e-11, 2.280312139807793e-12], [0.0002730444711773411, 0.0005283521527100764, 0.0005111914481726706, 0.00032972541179148606, 0.00015950801930915016, 5.152712312758252e-05, 1.5216522706557999e-05, 4.2063700121320145e-06, 1.0174371236222512e-06, 2.1875357771698316e-07, 4.232970665966382e-08, 7.4463366687564245e-09, 1.2007470162208316e-09, 1.7873033033352034e-10, 2.470360397942141e-11, 3.1868318705117195e-12, 3.8541557714245565e-13], [3.8458036295139925e-05, 7.441786379311848e-05, 7.200079599788345e-05, 4.644148918097281e-05, 2.2466542426244324e-05, 8.694734600319952e-06, 2.340606772482595e-06, 5.924629416586619e-07, 1.4330498493365736e-07, 3.081121912213106e-08, 5.962096167194146e-09, 1.048808952761651e-09, 1.6912399702504538e-10, 2.5173985400145657e-11, 3.4794775164822783e-12, 4.4886203047505286e-13, 5.4285392377821975e-14], [4.642950283522606e-06, 8.984297563863668e-06, 8.692490527252232e-06, 5.606774191620884e-06, 2.7123340028904664e-06, 1.0496953138195183e-06, 3.3853385149728086e-07, 7.811374143939568e-08, 1.7300881285818823e-08, 3.7197676309035532e-09, 7.197901597841421e-10, 1.2662029301795474e-10, 2.0417951242017617e-11, 3.03919736707334e-12, 4.2006931913222763e-13, 5.419008073275046e-14, 6.553750586677671e-15], [4.904661219204914e-07, 9.49071886461107e-07, 9.182463430337206e-07, 5.922813354274859e-07, 2.8652211600712334e-07, 1.1088638868141471e-07, 3.5761611721740176e-08, 9.88573894527203e-09, 1.9959172352524035e-09, 3.9294411806418317e-10, 7.603628441138792e-11, 1.3375754699194195e-11, 2.1568857626526646e-12, 3.2105089551992654e-13, 4.437475254123337e-14, 5.724463352079107e-15, 6.923168326160027e-16], [4.605443657101503e-08, 8.91172071685763e-08, 8.622270952420327e-08, 5.561481614231264e-08, 2.690423258220919e-08, 1.0412156774703777e-08, 3.3579911131622247e-09, 9.282641896445781e-10, 2.2452861834539877e-10, 4.0295131009217364e-11, 7.139755593736188e-12, 1.2559743045481052e-12, 2.0253011188225434e-13, 3.014646158616218e-14, 4.166759200946429e-15, 5.375232305936209e-16, 6.500808155701411e-17], [3.892032354062832e-09, 7.531240840803422e-09, 7.286628609725806e-09, 4.6999742024282035e-09, 2.2736602913320967e-09, 8.799250204751436e-10, 2.8378178152131056e-10, 7.844704068073213e-11, 1.8974776635597816e-11, 4.079662692707811e-12, 6.589426750975297e-13, 1.0614162267809181e-13, 1.7115696267442712e-14, 2.547659087587217e-15, 3.521302794936152e-16, 4.542576047597145e-17, 5.493793335313359e-18], [2.9901207379216625e-10, 5.786005195167846e-10, 5.598077645148653e-10, 3.6108359468561915e-10, 1.7467785901122435e-10, 6.760175178894197e-11, 2.180202302494854e-11, 6.026828706168939e-12, 1.4577698218851063e-12, 3.134270969884652e-13, 6.064941754633397e-14, 8.90547988251421e-15, 1.3149427778991848e-15, 1.9572828738170707e-16, 2.7053013833887875e-17, 3.48991210962764e-18, 4.220701136933842e-19], [2.1057773367466163e-11, 4.074764759750594e-11, 3.942417737517708e-11, 2.542912868757536e-11, 1.2301599466278597e-11, 4.7608190209894295e-12, 1.535396393828406e-12, 4.244363493738283e-13, 1.026626990070135e-13, 2.2072944051728952e-14, 4.2712044144653066e-15, 7.513594721291627e-16, 1.0113230304751089e-16, 1.3784065188454791e-17, 1.905194753496481e-18, 2.4577528708086534e-19, 2.972407330117922e-20], [1.368907375252366e-12, 2.6488914258422428e-12, 2.5628563015839516e-12, 1.653077046619011e-12, 7.996928233070652e-13, 3.0948762513243676e-13, 9.981185620958643e-14, 2.7591428535396748e-14, 6.6738169977239586e-15, 1.4349008025999291e-15, 2.7765913908093146e-16, 4.884379297444674e-17, 7.876227101180699e-18, 9.785843258758618e-19, 1.2385142074815984e-19, 1.5977168966001068e-20, 1.9322794701262504e-21], [8.263251973225863e-14, 1.5989728521563934e-13, 1.5470387386329718e-13, 9.978609520494886e-14, 4.827253778911399e-14, 1.868186464108375e-14, 6.025027936043884e-15, 1.6655248588108847e-15, 4.0285728948771323e-16, 8.66161370946032e-17, 1.6760574677097647e-17, 2.9483994021255455e-18, 4.754393928472184e-19, 7.076881190560768e-20, 8.164643876407494e-21, 9.644434340236648e-22, 1.1663982847196632e-22], [4.655482572958658e-15, 9.00854805343913e-15, 8.715953368884257e-15, 5.621908042444431e-15, 2.719655157048008e-15, 1.0525286600087161e-15, 3.3944762484219943e-16, 9.383499353701198e-17, 2.2696815934892058e-17, 4.879917955878378e-18, 9.442839644104303e-19, 1.6611162384001067e-19, 2.6786062134738327e-20, 3.987086096406763e-21, 5.510838354838386e-22, 5.934030729318386e-23, 6.571440523943513e-24], [2.4589499604711225e-16, 4.758168145354815e-16, 4.603624405421314e-16, 2.9694001302974657e-16, 1.4364774942478707e-16, 5.559284706501121e-17, 1.7929069878512786e-17, 4.956211306403975e-18, 1.1988087973972273e-18, 2.5774930690125076e-19, 4.987553879908298e-20, 8.77374503016565e-21, 1.4147961117923995e-21, 2.1059138436262453e-22, 2.9107349329375165e-23, 3.7549269566595146e-24, 3.7905732041887017e-25]] |
| Legacy trial inputs | {"lambda_home": 0.8450939027473283, "lambda_away": 1.9350406563146056, "rho": -0.031918512138755184, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1885 |
| Legacy p draw | 0.2248 |
| Legacy p away | 0.5867 |
| Legacy p over 1 5 | 0.7636 |
| Legacy p under 3 5 | 0.7017 |
| Legacy p btts yes | 0.4951 |
| Legacy p over 2 5 | 0.5206 |
| Legacy goal margin distribution | {"-1": 0.2300742908871991, "-10": 1.366064357253417e-05, "-11": 2.3739741631638086e-06, "-12": 3.788748249031359e-07, "-13": 5.5896602704639105e-08, "-14": 7.66535193731533e-09, "-15": 9.778634312981005e-10, "-16": 1.0729652770820541e-10, "-2": 0.181597461615656, "-3": 0.10398395117603336, "-4": 0.04667720078619406, "-5": 0.017163027609037047, "-6": 0.0053333046001254915, "-7": 0.0014333656937363388, "-8": 0.00033913554063807496, "-9": 7.163294806042412e-05, "0": 0.2247968158715901, "1": 0.12922983364737442, "10": 4.511759470996931e-09, "11": 3.424251390344652e-10, "12": 2.3867134222963575e-11, "13": 1.5378175538499193e-12, "14": 9.210143022623988e-14, "15": 5.13129938749414e-15, "16": 2.4589499604711225e-16, "2": 0.045317459926179, "3": 0.011332793505395839, "4": 0.0022217251825657654, "5": 0.0003567749132239627, "6": 4.8418537843618346e-05, "7": 5.683124393888712e-06, "8": 5.872436585006321e-07, "9": 5.417173302411268e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1538 |
| Legacy raw p draw | 0.2198 |
| Legacy raw p away | 0.6264 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.8451 |
| Legacy lambda away | 1.9350 |
| Legacy model home team | Monza |
| Legacy model away team | Napoli |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.66080077526733, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,361.2920 |
| Elo away rating | 1,577.2069 |
| Elo rating diff | -155.9150 |
| Elo home expectancy | 0.2896 |

</details>


---

## 2026-10-28 — Parma vs Udinese

The model's most likely 1X2 outcome is **Udinese win** at **38.7%**. Expected goals are 1.03 for Parma and 1.15 for Udinese (2.18 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 37.5%; Under 3.5 goals: 82.3%; Double Chance 1X: 61.3%; Double Chance X2: 67.6%; Double Chance 12 (either team wins): 71.1%; Under 4.5 goals: 92.9%; BTTS Yes (both teams score): 44.1%; BTTS No (at least one team does not score): 55.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 32.4% | 3.09 |
| Draw | 28.9% | 3.45 |
| Udinese win | 38.7% | 2.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.03 |
| Udinese expected goals | 1.15 |
| Expected total goals | 2.18 |
| Over 0.5 | 88.7% |
| Under 0.5 | 11.3% |
| Over 1.5 | 64.5% |
| Under 1.5 | 35.5% |
| Over 2.5 | 37.5% |
| Under 2.5 | 62.5% |
| Over 3.5 | 17.7% |
| Under 3.5 | 82.3% |
| Over 4.5 | 7.1% |
| Under 4.5 | 92.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.29% |
| 2 | 0-1 | 12.83% |
| 3 | 1-0 | 11.46% |
| 4 | 0-0 | 11.26% |
| 5 | 1-2 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 32.4% | 32.6% | 3.04 | -1.5% |
| Draw | 28.9% | 28.6% | 3.19 | -7.7% |
| Udinese win | 38.7% | 38.8% | 2.56 | -1.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 482c18a8081afdfa310324fa8f37e95a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T10:50:11Z |
| Market best draw last update utc | 2026-10-26T10:50:11Z |
| Market best away last update utc | 2026-10-26T10:50:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Parma |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0276 |
| Dc lambda away | 1.1540 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:49:44.033835+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 44.1% |
| P btts no | 55.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.88 |
| Fair Over 1.5 odds | 1.55 |
| Fair Under 1.5 odds | 2.81 |
| Fair Over 2.5 odds | 2.67 |
| Fair Under 2.5 odds | 1.60 |
| Fair Over 3.5 odds | 5.64 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 14.05 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.22334587735307887, "-10": 1.4651325383994434e-07, "-11": 1.523330662469387e-08, "-12": 1.4488893304142757e-09, "-13": 1.1786788248242412e-10, "-2": 0.11072845510657135, "-3": 0.038953047668142775, "-4": 0.010631197680393115, "-5": 0.002362847445370817, "-6": 0.0004422326211250601, "-7": 7.141858705302098e-05, "-8": 1.0137529657573615e-05, "-9": 1.2831554314220207e-06, "0": 0.2894750487854077, "1": 0.19969473419905778, "10": 4.616895034734401e-08, "11": 4.274222584270392e-09, "12": 3.6198287786035366e-10, "13": 2.6220330342512907e-11, "2": 0.08831071913236593, "3": 0.027662121616743425, "4": 0.0067222723081297175, "5": 0.0013303302102862095, "6": 0.00022169934452107777, "7": 3.187973856813239e-05, "8": 4.029261912130362e-06, "9": 4.5411149010411214e-07} |
| Raw goal margin distribution | {"-1": 0.2211296111661548, "-10": 1.4505939951198482e-07, "-11": 1.5082146178898026e-08, "-12": 1.4345119688544925e-09, "-13": 1.1669827682161682e-10, "-2": 0.10962969414491237, "-3": 0.03856651569608372, "-4": 0.010525704065624876, "-5": 0.00233940085678769, "-6": 0.0004378443368344804, "-7": 7.070989880016696e-05, "-8": 1.003693472174902e-05, "-9": 1.2704226510862862e-06, "0": 0.2984214326750444, "1": 0.19654460209295424, "10": 4.544064725323591e-08, "11": 4.206797842975403e-09, "12": 3.5627269281225417e-10, "13": 2.5806711501856563e-11, "2": 0.08691764067805546, "3": 0.027225758896527757, "4": 0.00661623022390179, "5": 0.0013093445998045392, "6": 0.0002182020954529987, "7": 3.1376844045648104e-05, "8": 3.965701361251491e-06, "9": 4.4694800033827014e-07} |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 38.3% |
| Raw p over 1 5 | 64.4% |
| Raw p under 3 5 | 82.3% |
| Raw p btts yes | 44.3% |
| P home draw | 61.3% |
| P draw away | 67.6% |
| P home away | 71.1% |
| Raw p home draw | 61.7% |
| Raw p draw away | 68.1% |
| Raw p home away | 70.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.3751 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.75 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-26T10:50:12Z |
| Market reference home last update utc | 2026-10-26T10:50:12Z |
| Market reference draw last update utc | 2026-10-26T10:50:12Z |
| Market reference away last update utc | 2026-10-26T10:50:12Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.68 |
| Market reference over 2 5 last update utc | 2026-10-26T10:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-26T10:50:12Z |
| Home probability edge | -0.2% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0073 |
| Raw ev home | -0.0306 |
| Raw edge prob draw | 0.0128 |
| Raw ev draw | -0.0480 |
| Raw edge prob away | -0.0055 |
| Raw ev away | -0.0203 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.11102118274967314, 0.12417470227080411, 0.07472028750416357, 0.02896780084033912, 0.008422747491557699, 0.0019592146658989795, 0.0003797773144413469, 6.30999805649614e-05, 9.173551108525314e-06, 1.1854772440288338e-06, 1.3787688666428556e-07, 1.457796923865551e-08, 1.4129084739483614e-09, 1.264063595230195e-10], [0.11106949002418338, 0.1349378608616631, 0.07862574876687452, 0.030481882595465744, 0.008862985546745071, 0.0020616184070861004, 0.00039962741994213787, 6.639807453656901e-05, 9.653031979016458e-06, 1.2474394715446469e-06, 1.4508340122514763e-07, 1.5339926881650237e-08, 1.4867580199963993e-09, 1.330133354457227e-10], [0.0606904203106597, 0.07058597071288165, 0.04000856112980932, 0.01603755099817374, 0.004663116927139684, 0.001084687280677844, 0.00021025752289144994, 3.4934276228698804e-05, 5.0787871177453764e-06, 6.56320162620405e-07, 7.633329204157889e-08, 8.070855167892985e-09, 7.822337578054616e-10, 6.99828215651381e-11], [0.021287523996906695, 0.024758446847195477, 0.014397651187016311, 0.005440451332597844, 0.0016356158513773326, 0.0003804604812155746, 7.374907013612751e-05, 1.2253404074751072e-05, 1.78141463003175e-06, 2.3020818013648894e-07, 2.677435380708e-08, 2.830900201096544e-09, 2.743731186114315e-10, 2.4546888715111665e-11], [0.005600043741655614, 0.006513128785663251, 0.0037875460028187055, 0.001468367988776289, 0.0004161399910399631, 0.00010008657357653057, 1.9400942013207118e-05, 3.2234654820710157e-06, 4.686312908750061e-07, 6.056016090169078e-08, 7.043447255584965e-09, 7.447162458492568e-10, 7.217849600459644e-11, 6.45747483578423e-12], [0.0011785490849199093, 0.0013707110737745016, 0.0007971025016305231, 0.00030902325576949154, 8.985234559956355e-05, 2.037154423334066e-05, 4.082997117713513e-06, 6.783897536204883e-07, 9.862511874992769e-08, 1.2745100843121124e-08, 1.4823184783369494e-09, 1.5672817759297547e-10, 1.519022070923384e-11, 1.3589985024575666e-12], [0.0002066915321919303, 0.00024039250944745416, 0.00013979420923926106, 5.4195867643710024e-05, 1.575812091379691e-05, 3.6654953306228827e-06, 6.925417450765135e-07, 1.1897460987690095e-07, 1.729667195695878e-08, 2.235209763354394e-09, 2.599659881834243e-10, 2.7486667784008746e-11, 2.6640298931108976e-12, 2.3833838260421866e-13], [3.1070690485800114e-05, 3.6136754984286874e-05, 2.1014419705142808e-05, 8.14693766749699e-06, 2.3688232041153413e-06, 5.510117888582552e-07, 1.068090092629495e-07, 1.7297143299777277e-08, 2.6001042960485e-09, 3.3600559244746046e-10, 3.907911790107532e-11, 4.1319048639588745e-12, 4.0046753428150113e-13, 3.582797049424072e-14], [4.086835693742668e-06, 4.75319272976285e-06, 2.7640995160219177e-06, 1.0715949704896276e-06, 3.1157953271649504e-07, 7.247649186966325e-08, 1.4048959474158028e-08, 2.334233868290234e-09, 3.307645183156693e-10, 4.419598106900814e-11, 5.140211930310434e-12, 5.434837789940161e-13, 5.267488387600306e-14, 4.712577234713858e-15], [4.778272664045769e-07, 5.557368240260115e-07, 3.231747529838742e-07, 1.2528942531894042e-07, 3.642945485023767e-08, 8.473852776048338e-09, 1.64258521859438e-09, 2.729154465744308e-10, 3.9676776047166813e-11, 4.997564447957909e-12, 6.009865821522998e-13, 6.354338366221867e-14, 6.15867572292812e-15, 5.509881156297718e-16], [5.028022222237187e-08, 5.847839370791373e-08, 3.40066369986744e-08, 1.31838021604563e-08, 3.833354046729779e-09, 8.916761989438702e-10, 1.7284394511756482e-10, 2.871801227446404e-11, 4.175059183478441e-12, 5.395334474004951e-13, 6.116217342877768e-14, 6.686465331579884e-15, 6.480575842278609e-16, 5.797870243824472e-17], [4.809841479772818e-09, 5.594084339620501e-09, 3.253098852674187e-09, 1.261171802543594e-09, 3.6670134867486886e-10, 8.52983733691237e-11, 1.6534373557007363e-11, 2.7471852857659486e-12, 3.9938910278455284e-13, 5.161214967496834e-14, 6.002749143502471e-15, 6.186172784741646e-16, 6.199364505818788e-17, 5.546283520735795e-18], [4.2177008907613957e-10, 4.90539544836022e-10, 2.852609173578597e-10, 1.1059086785626278e-10, 3.2155666906146176e-11, 7.479727281083779e-12, 1.4498823375539913e-12, 2.4089787315420876e-13, 3.502202269365366e-14, 4.525816715034573e-15, 5.263749442895031e-16, 5.56545620625698e-17, 5.257557854497593e-18, 4.863479398270629e-19], [3.413962018448827e-11, 3.970607252604473e-11, 2.3090066423173876e-11, 8.951631047985885e-12, 2.6027977881489213e-12, 6.054365994020444e-13, 1.1735880186457608e-13, 1.949915867848813e-14, 2.8348111538038043e-15, 3.663362283805668e-16, 4.2606721382347116e-17, 4.504884674283205e-18, 4.366170367253342e-19, 3.807341759214883e-20]] |
| Legacy trial inputs | {"lambda_home": 1.052267749404649, "lambda_away": 1.1630496271333925, "rho": -0.031918512138755184, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3247 |
| Legacy p draw | 0.2918 |
| Legacy p away | 0.3835 |
| Legacy p over 1 5 | 0.6537 |
| Legacy p under 3 5 | 0.8161 |
| Legacy p btts yes | 0.4502 |
| Legacy p over 2 5 | 0.3834 |
| Legacy goal margin distribution | {"-1": 0.22057790907744182, "-10": 1.5402359419245635e-07, "-11": 1.613471008021705e-08, "-12": 1.5459218093940842e-09, "-13": 1.264063595230195e-10, "-2": 0.11026584447763337, "-3": 0.03899254710333756, "-4": 0.010707358466152837, "-5": 0.002395619847071076, "-6": 0.0004514915871510888, "-7": 7.343686720521028e-05, "-8": 1.0500228309807145e-05, "-9": 1.3389123310153215e-06, "0": 0.291845277783729, "1": 0.19761510693725334, "10": 5.616851911039822e-08, "11": 5.323471091032014e-09, "12": 4.614761616021843e-10, "13": 3.413962018448827e-11, "2": 0.08956175987524817, "3": 0.02865439412324735, "4": 0.007119016191348885, "5": 0.0014410649469521512, "6": 0.00024572159623935966, "7": 3.616061606914205e-05, "8": 4.677873087673403e-06, "9": 5.396719526308094e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3232 |
| Legacy raw p draw | 0.2980 |
| Legacy raw p away | 0.3788 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0523 |
| Legacy lambda away | 1.1630 |
| Legacy model home team | Parma |
| Legacy model away team | Udinese |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 9.168902944182147, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,368.9562 |
| Elo away rating | 1,450.1567 |
| Elo rating diff | -21.2005 |
| Elo home expectancy | 0.4695 |

</details>


---

## 2026-10-28 — Venezia vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **76.4%**. Expected goals are 0.67 for Venezia and 2.72 for Inter Milan (3.39 combined). The most likely exact score is 0-2 at 11.9%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 65.0%; Under 3.5 goals: 57.1%; Double Chance 1X: 23.6%; Double Chance X2: 90.0%; Double Chance 12 (either team wins): 86.4%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 46.3%; BTTS No (at least one team does not score): 53.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 10.0% | 9.96 |
| Draw | 13.6% | 7.37 |
| Inter Milan win | 76.4% | 1.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Inter Milan expected goals | 2.72 |
| Expected total goals | 3.39 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 84.5% |
| Under 1.5 | 15.5% |
| Over 2.5 | 65.0% |
| Under 2.5 | 35.0% |
| Over 3.5 | 42.9% |
| Under 3.5 | 57.1% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 11.89% |
| 2 | 0-3 | 10.77% |
| 3 | 0-1 | 8.60% |
| 4 | 1-2 | 7.96% |
| 5 | 0-4 | 7.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 10.0% | 11.5% | 7.72 | -22.5% |
| Draw | 13.6% | 13.7% | 5.85 | -20.6% |
| Inter Milan win | 76.4% | 74.8% | 1.35 | +3.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 33320ad169692216a91dec030e7ef6a6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T10:50:11Z |
| Market best draw last update utc | 2026-10-26T10:50:11Z |
| Market best away last update utc | 2026-10-26T10:50:11Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Venezia |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6694 |
| Dc lambda away | 2.7187 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:49:44.033835+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 46.3% |
| P btts no | 53.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.71 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.47 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.04 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.19376611861279974, "-10": 0.0002304857858913795, "-11": 5.620033959973746e-05, "-12": 1.2587413360184877e-05, "-13": 2.6066065215753056e-06, "-14": 5.018739820061337e-07, "-15": 9.028404281048649e-08, "-16": 1.5239726492363727e-08, "-17": 2.4225678179311233e-09, "-18": 3.625439633643615e-10, "-19": 4.7342224993805716e-11, "-2": 0.2095370837326786, "-3": 0.16662291095594312, "-4": 0.10428359688636349, "-5": 0.0535842883247902, "-6": 0.023301593584881465, "-7": 0.008771941782629626, "-8": 0.002908978351501475, "-9": 0.0008616060093391265, "0": 0.1356854569608515, "1": 0.07518779070858533, "10": 3.041506395408105e-10, "11": 1.8259954122217496e-11, "12": 1.0069627196740574e-12, "13": 5.134149741469369e-14, "14": 2.4339065023786223e-15, "15": 1.0780436926082451e-16, "16": 4.4804196514369556e-18, "17": 1.7536124492252063e-19, "18": 6.4615172815337075e-21, "19": 2.0774886165759351e-22, "2": 0.020472752501143384, "3": 0.0040083553345421335, "4": 0.0006176801636456892, "5": 7.814501431436118e-05, "6": 8.366919430383759e-06, "7": 7.755179602474929e-07, "8": 6.332172894014207e-08, "9": 4.617821592287958e-09} |
| Raw goal margin distribution | {"-1": 0.20345008394483832, "-10": 0.00024200491202178409, "-11": 5.9009097623219394e-05, "-12": 1.321650205470351e-05, "-13": 2.73687845647246e-06, "-14": 5.269564385139791e-07, "-15": 9.479622247776958e-08, "-16": 1.6001371428425583e-08, "-17": 2.5436419403386495e-09, "-18": 3.806630401033452e-10, "-19": 4.9708275719617685e-11, "-2": 0.22000924403175828, "-3": 0.17495032394626614, "-4": 0.10949544065026659, "-5": 0.05626230238728044, "-6": 0.02446615127986301, "-7": 0.009210342369511355, "-8": 0.0030543621043952586, "-9": 0.0009046670087752013, "0": 0.13248847824805027, "1": 0.0489828812933086, "10": 1.9814619543290109e-10, "11": 1.189588305176402e-11, "12": 6.560099039982759e-13, "13": 3.3447644219681695e-14, "14": 1.5856264981517915e-15, "15": 7.023173008061283e-17, "16": 2.9188763476392975e-18, "17": 1.1424326958586678e-19, "18": 4.209509695566672e-21, "19": 1.353429557311348e-22, "2": 0.013337463384148705, "3": 0.0026113387783165496, "4": 0.0004024024891269144, "5": 5.090943521216111e-05, "6": 5.4508294150790596e-06, "7": 5.052296899487724e-07, "8": 4.125245206344222e-08, "9": 3.0083901223458924e-09} |
| Unadjusted home-win probability | 6.5% |
| Unadjusted draw probability | 13.2% |
| Unadjusted away-win probability | 80.2% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 56.1% |
| Raw p btts yes | 45.7% |
| P home draw | 23.6% |
| P draw away | 90.0% |
| P home away | 86.4% |
| Raw p home draw | 19.8% |
| Raw p draw away | 93.5% |
| Raw p home away | 86.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.6505 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:49:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.92, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:50:11Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 6.25 |
| Reference draw odds | 5.40 |
| Reference away odds | 1.28 |
| Market reference 1x2 last update utc | 2026-10-26T10:50:13Z |
| Market reference home last update utc | 2026-10-26T10:50:13Z |
| Market reference draw last update utc | 2026-10-26T10:50:13Z |
| Market reference away last update utc | 2026-10-26T10:50:13Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-26T10:49:52Z |
| Market reference under 2 5 last update utc | 2026-10-26T10:49:52Z |
| Home probability edge | -1.5% |
| Draw probability edge | -0.1% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -7.9% |
| Under 2.5 probability edge | +7.9% |
| Raw edge prob home | -0.0500 |
| Raw ev home | -0.4952 |
| Raw edge prob draw | -0.0046 |
| Raw ev draw | -0.2249 |
| Raw edge prob away | 0.0545 |
| Raw ev away | 0.0829 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.03836325421143271, 0.0920953610702745, 0.12426430873752244, 0.10940785458093058, 0.07224567596448313, 0.038164994391361194, 0.016801083910875363, 0.006339610983802538, 0.0020931288828896647, 0.0006142947581246735, 0.00016225577299599462, 3.8961065103633424e-05, 8.575766019389137e-06, 1.7424202884129075e-06, 3.28736730838912e-07, 5.7886903823694436e-08, 9.556166036370549e-09, 1.4847663415474943e-09, 2.1787578111133793e-10, 3.028856545508e-11], [0.030029915122524987, 0.06582937463162097, 0.08261654126141722, 0.07273929758383815, 0.04803219790073488, 0.025373817034911497, 0.01117012162431349, 0.004214860548019162, 0.0013916068940115676, 0.00040841098097184217, 0.00010787498760357247, 2.5903080904124047e-05, 5.701557707013469e-06, 1.158439934321447e-06, 2.1855906948199603e-07, 3.8485835770813404e-08, 6.353372047579476e-09, 9.871399194689451e-10, 1.448536884236744e-10, 2.013721029868937e-11], [0.010901720224352178, 0.02879508604938045, 0.028006464265867375, 0.02418018995645478, 0.015966990441819363, 0.008434831462557465, 0.0037132014149751096, 0.00140111510663962, 0.00046260164944716536, 0.0001357650599913876, 3.586008909143154e-05, 8.610770759742694e-06, 1.895326913823628e-06, 3.8509167115272464e-07, 7.265398474173451e-08, 1.2793563458577553e-08, 2.112004763277171e-09, 3.281476665188755e-10, 4.815264675797196e-11, 6.6940647818899886e-12], [0.0024159858071503715, 0.006381425846498539, 0.008427739044210578, 0.005464616936815101, 0.003538526168023502, 0.0018692860099017274, 0.0008229014993093567, 0.00031050826311463666, 0.00010251951035508413, 3.008758721521884e-05, 7.947137195331464e-06, 1.9082768146712367e-06, 4.2003306170702134e-07, 8.534212883931239e-08, 1.610122002368493e-08, 2.8352468328582273e-09, 4.680521447719358e-10, 7.272247761304365e-11, 1.0671353579971254e-11, 1.4835058295721774e-12], [0.00040156420043554764, 0.0010606652407078607, 0.0014007856671805474, 0.0012333143452932934, 0.0005997685521898522, 0.0003106965031540943, 0.00013677554794791393, 5.160998961054701e-05, 1.703990358012103e-05, 5.000897715274603e-06, 1.3209041974294404e-06, 3.17177216449374e-07, 6.981425142551633e-08, 1.41848282508114e-08, 2.6762051025763515e-09, 4.712501307352551e-10, 7.779556681219667e-11, 1.2087299308607364e-11, 1.773699810331486e-12, 2.4657546850255456e-13], [5.339561402858999e-05, 0.0001410356594162295, 0.00018626115261377338, 0.00016399264846262996, 0.00010828984616113273, 4.2129628668823436e-05, 1.818691596226568e-05, 6.862531775181522e-06, 2.2657799516532494e-06, 6.649646654548298e-07, 1.7563938871589523e-07, 4.21747561406724e-08, 9.28313534615028e-09, 1.886143270542193e-09, 3.5585247530412125e-10, 6.266168663533774e-11, 1.0344403346050161e-11, 1.607236819991456e-12, 2.358471954729047e-13, 3.278690812278806e-14], [5.916637145438132e-06, 1.5627815814359313e-05, 2.0639141891255334e-05, 1.8171623514868608e-05, 1.1999332490636369e-05, 6.338849364913567e-06, 2.0550816427581353e-06, 7.604203294871386e-07, 2.5106552418636244e-07, 7.368310509412416e-08, 1.9462170262188382e-08, 4.673281379404837e-09, 1.0286414795371317e-09, 2.0899891384586061e-10, 3.9431140777838674e-11, 6.943387944634029e-12, 1.146237985986339e-12, 1.7809397351598217e-13, 2.613364979069695e-14, 3.633036945309526e-15], [5.61949768683803e-07, 1.4842971211583358e-06, 1.960262346080422e-06, 1.7259026335023619e-06, 1.1396713963897854e-06, 6.020505984689505e-07, 2.6503613546342253e-07, 7.365071193338596e-08, 2.3845676145576197e-08, 6.998266556784302e-09, 1.8484760528798107e-09, 4.4385844958832656e-10, 9.769820715305185e-11, 1.9850277852749812e-11, 3.74508692934288e-12, 6.594684029892568e-13, 1.0886727633420102e-13, 1.6914991533399927e-14, 2.4821191656258266e-15, 3.4505821818235187e-16], [4.670120761442188e-08, 1.2335349506248872e-07, 1.629089002340115e-07, 1.434322811418829e-07, 9.471314601601959e-08, 5.003381362597543e-08, 2.202600352802333e-08, 8.31114793761273e-09, 2.020881855708992e-09, 5.815955760155281e-10, 1.5361882631969007e-10, 3.6887150348314244e-11, 8.11927419509049e-12, 1.649670484563987e-12, 3.1123792902513337e-13, 5.480555828911083e-14, 9.047487084848236e-15, 1.4057315714315853e-15, 2.06278156763246e-16, 2.867629169799313e-17], [3.449897583477656e-09, 9.112332341448613e-09, 1.2034357352908381e-08, 1.0595586396598046e-08, 6.9966210780238565e-09, 3.696082853907178e-09, 1.627098317721707e-09, 6.13958624424115e-10, 2.0270873606672236e-10, 4.381268358926169e-11, 1.134808380272616e-11, 2.7249164924961786e-12, 5.997845849404792e-13, 1.2186396260284726e-13, 2.29916748212484e-14, 4.048579742600899e-15, 6.683532487696168e-16, 1.0384378047223027e-16, 1.523811804648035e-17, 2.1183664081837586e-18], [2.2936481838488003e-10, 6.058291302816487e-10, 8.000985889691567e-10, 7.044425785785812e-10, 4.6516706193088614e-10, 2.457323303108948e-10, 1.0817686644551958e-10, 4.081875040618288e-11, 1.3476994985487076e-11, 3.955249694623618e-12, 7.693851586002988e-13, 1.8116479150239624e-13, 3.98763960570236e-14, 8.102068242236821e-15, 1.5285906877339662e-15, 2.691679201799046e-16, 4.443515142454099e-17, 6.904004907995759e-18, 1.0130991119843962e-18, 1.4083859440137643e-19], [1.386292007483507e-11, 3.661660437394692e-11, 4.835834400834559e-11, 4.257684867676008e-11, 2.8114921226379447e-11, 1.4852180377491886e-11, 6.538261901020492e-12, 2.4671049310012982e-12, 8.145560668299793e-13, 2.3905719621121103e-13, 6.31429938941998e-14, 1.1166122385699951e-14, 2.410148580343165e-15, 4.896929061479493e-16, 9.238875726631518e-17, 1.6268638714687836e-17, 2.6856819500449285e-18, 4.1728138129366897e-19, 6.123219819074005e-20, 8.512352467073486e-21], [7.680581013179463e-13, 2.0286981011465343e-12, 2.679234799120912e-12, 2.358918134003807e-12, 1.5576727629725967e-12, 8.228668563036342e-13, 3.6224438967466317e-13, 1.3668692590219264e-13, 4.5129480854623706e-14, 1.3244671053227499e-14, 3.498360211276537e-15, 8.400307578015764e-16, 1.3617075358074618e-16, 2.7130835472939557e-17, 5.1186858977786384e-18, 9.013439949721005e-19, 1.4879691783261818e-19, 2.311896366001074e-20, 3.392494916512999e-21, 4.716164587486726e-22], [3.927998588924095e-14, 1.0375156859855623e-13, 1.3702128123230004e-13, 1.2063966366417794e-13, 7.966241622167355e-14, 4.208301227324816e-14, 1.8525882990442193e-14, 6.990435373923966e-15, 2.3080094697478697e-15, 6.773582508741103e-16, 1.7891294877122802e-16, 4.2960807595615835e-17, 9.456154059546971e-18, 1.414949974488321e-18, 2.617795574204479e-19, 4.609648585582716e-20, 7.609763926451043e-21, 1.182348789474161e-21, 1.7349879159049318e-22, 2.411938343335431e-23], [1.86536527775587e-15, 4.927053032100592e-15, 6.5069967449851765e-15, 5.729050930767852e-15, 3.783084484323815e-15, 1.998478056973869e-15, 8.797747272003091e-16, 3.3196843450205525e-16, 1.096049458301526e-16, 3.2167031967496245e-17, 8.496388041477798e-18, 2.040163634966138e-18, 4.490628253667633e-19, 9.124038318233014e-20, 1.2677364101132042e-20, 2.189073702431673e-21, 3.6137969703825807e-22, 5.61485023009107e-23, 8.239275402951581e-24, 1.1454041888997411e-24], [8.267862215253454e-17, 2.1838186913000852e-16, 2.8840974560951977e-16, 2.5392883787749655e-16, 1.676777285287605e-16, 8.857858250232671e-17, 3.8994272659053526e-17, 1.4713843497603652e-17, 4.858022184932184e-18, 1.4257399950151675e-18, 3.765855754470582e-19, 9.042621320132799e-20, 1.9903820503142942e-20, 4.044049310953033e-21, 7.6297754260252015e-22, 9.894421219839365e-23, 1.6017439469533152e-23, 2.4886711795947075e-24, 3.65189566877131e-25, 5.0767772551176384e-26], [3.435530819296814e-18, 9.074384916425324e-18, 1.198424143787796e-17, 1.0551462103793906e-17, 6.967484327538252e-18, 3.680690875023733e-18, 1.620322424448322e-18, 6.114018532271556e-19, 2.0186457517846452e-19, 5.924353316074875e-20, 1.5648196799459282e-20, 3.757465161336671e-21, 8.270600909887466e-22, 1.6804169785150785e-22, 3.170387693697133e-23, 5.582702214034032e-24, 6.7872583275231615e-25, 1.0341133311123131e-25, 1.5174660380495687e-26, 2.109544676553014e-27], [1.343586181322729e-19, 3.548860079854553e-19, 4.686862681925758e-19, 4.126523504251275e-19, 2.724881875162214e-19, 1.4394647166677904e-19, 6.336845551051424e-20, 2.3911038044457204e-20, 7.894630203430456e-21, 2.3169284944388645e-21, 6.1197823824719415e-22, 1.4694900244285548e-22, 3.234511834777966e-23, 6.571866619595853e-24, 1.2398925577267794e-24, 2.1833137130032224e-25, 3.6042881848524964e-26, 4.124207290902205e-27, 5.9345891700289355e-28, 8.250122689569387e-29], [4.962649743887847e-21, 1.31080163008566e-20, 1.7311325623487867e-20, 1.5241665250947417e-20, 1.0064582776957177e-20, 5.31678526231517e-21, 2.3405677572556476e-21, 8.831745107008923e-22, 2.915948757270882e-22, 8.557772295792647e-23, 2.2603936312536994e-23, 5.4276862881968285e-24, 1.1946944343131391e-24, 2.427374786222858e-25, 4.5796485328493146e-26, 8.064254745457e-27, 1.3312744717162156e-27, 2.0684357298132374e-28, 2.2353185638038298e-29, 3.0472529281395213e-30], [1.7365233386179403e-22, 4.586738416801777e-22, 6.0575544354356535e-22, 5.333341822132512e-22, 3.521784487644727e-22, 1.8604419354401356e-22, 8.190081399754204e-23, 3.090391683985906e-23, 1.0203446409755934e-23, 2.9945235076331854e-24, 7.909537238588788e-25, 1.899248264651131e-25, 4.1804577690716205e-26, 8.493835320617355e-27, 1.6025040997009697e-27, 2.821832548487636e-28, 4.6583766929929885e-29, 7.237840880621883e-30, 1.0620864652558694e-30, 1.0873670592500958e-31]] |
| Legacy trial inputs | {"lambda_home": 0.6648452970991389, "lambda_away": 2.6413341616544344, "rho": -0.031918512138755184, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0918 |
| Legacy p draw | 0.1383 |
| Legacy p away | 0.7699 |
| Legacy p over 1 5 | 0.8395 |
| Legacy p under 3 5 | 0.5847 |
| Legacy p btts yes | 0.4556 |
| Legacy p over 2 5 | 0.6385 |
| Legacy goal margin distribution | {"-1": 0.2027602867344193, "-10": 0.0001901422629729322, "-11": 4.506429747696216e-05, "-12": 9.809774614567516e-06, "-13": 1.974253300277794e-06, "-14": 3.694091003373341e-07, "-15": 6.457934146684126e-08, "-16": 1.0592942108427037e-08, "-17": 1.6363140947530587e-09, "-18": 2.380129914100273e-10, "-19": 3.028856545508e-11, "-2": 0.2149837790729796, "-3": 0.16675173678217076, "-4": 0.10166092746000134, "-5": 0.050843931942425896, "-6": 0.02150999782331757, "-7": 0.007875256748152102, "-8": 0.002539379970262067, "-9": 0.0007312150972840983, "0": 0.13830773902442475, "1": 0.06860095681094672, "10": 2.6878517052920694e-10, "11": 1.603453993082591e-11, "12": 8.78577709301636e-13, "13": 4.450627801592845e-14, "14": 2.0961542913011523e-15, "15": 9.223728718085215e-17, "16": 3.8082614870879705e-18, "17": 1.4807238987667306e-19, "18": 5.4213235855680244e-21, "19": 1.7365233386179403e-22, "2": 0.018860548423264747, "3": 0.003682275197941939, "4": 0.0005650634242951915, "5": 7.113437350086933e-05, "6": 7.574919141815257e-06, "7": 6.980710203286307e-07, "8": 5.6657816043984433e-08, "9": 4.106525676409588e-09} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0682 |
| Legacy raw p draw | 0.1396 |
| Legacy raw p away | 0.7922 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.6648 |
| Legacy lambda away | 2.6413 |
| Legacy model home team | Venezia |
| Legacy model away team | Inter |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.02142125436294478, "mu": 8.662593689998463, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,360.3350 |
| Elo away rating | 1,685.7694 |
| Elo rating diff | -265.4343 |
| Elo home expectancy | 0.1783 |

</details>


---
