# La Liga — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 2,000 |
| Training data through | 2026-10-30 |
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
| Training sha256 | b5bed448bb93fbfd7dd50ef4e0ecc1bc52ae9a3813a734cfef8f20d1e2aaa45e |
| Training as of utc | 2026-10-31T11:27:45.223690+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 100, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 100, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 96, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-10-31T11:27:45.223690+00:00', 'observations': 498, 'observations_sha256': 'ee01558e5040308fd9ebc0de0a5eedf5029218af8cfb055e80581b70ed7ee0b3', 'eligible_training_matches': 155, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 166, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 21, 'retrospective_eligible_training_matches': 155, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '7c2cd1d9b8dd7685cfea56c9705a94116cb3b349e8c14c33bbea1d3646041ab8', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 95, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-25T00:00:00+00:00', 'audit_origin_utc': '2026-09-19T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 16, 'selected_ridge': 1.0, 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8340710293949452, 'audit_candidate_poisson_score': 0.8240448588495166, 'audit_gain': 0.010026170545428537, 'audit_gain_lower95': -0.016891353314772217, 'audit_baseline_briers': [0.5584268185611213, 0.19721035590808725, 0.21822280588534607, 0.2559015784230917], 'audit_candidate_briers': [0.5417645466159129, 0.20111639605140724, 0.22090666042076829, 0.2525690485613323], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-31', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-11-01', 'audit_start_date': '2026-05-02', 'training_shot_matches': 1621, 'tuning_matches': 230, 'audit_matches': 131, 'audit_matchdays': 55, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.827538963879531, 'audit_candidate_poisson_score': 0.8281823721244723, 'audit_gain': -0.000643408244941357, 'audit_gain_lower95': -0.009288406825720073, 'audit_baseline_briers': [0.5652643106500623, 0.18055279433233673, 0.19961611458530326, 0.24610102573130246], 'audit_candidate_briers': [0.5699644576467575, 0.17751887012287215, 0.20201067879695647, 0.24356755741374655], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1834.536 |
| Base scoring parameter | 0.092 |
| Home-advantage parameter | 0.285 |
| Dixon-Coles low-score adjustment | -0.026 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 2000, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-30'} |
| Training data health | {'training_end': '2026-10-30', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 9.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261031T112745223690Z_804f73105ea85b9a53093313ddaaee4ae2b57e3ddf698c619cf688da956aa71e.json |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 5, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3, 'ANCHORED_MAIN': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 9} |
| Legacy comparison status | {'AVAILABLE': 9} |
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

## 2026-10-31 — Barcelona vs Alavés

The model's most likely 1X2 outcome is **Barcelona win** at **87.0%**. Expected goals are 2.93 for Barcelona and 0.73 for Alavés (3.65 combined). The most likely exact score is 2-0 at 11.8%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 72.6%; Under 3.5 goals: 49.0%; Double Chance 1X: 95.7%; Double Chance X2: 13.0%; Double Chance 12 (either team wins): 91.3%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 47.6%; BTTS No (at least one team does not score): 52.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 87.0% | 1.15 |
| Draw | 8.7% | 11.49 |
| Alavés win | 4.3% | 23.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.93 |
| Alavés expected goals | 0.73 |
| Expected total goals | 3.65 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 88.9% |
| Under 1.5 | 11.1% |
| Over 2.5 | 72.6% |
| Under 2.5 | 27.4% |
| Over 3.5 | 51.0% |
| Under 3.5 | 49.0% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.82% |
| 2 | 3-0 | 11.54% |
| 3 | 2-1 | 8.57% |
| 4 | 4-0 | 8.45% |
| 5 | 3-1 | 8.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 87.0% | 89.3% | 1.11 | -3.4% |
| Draw | 8.7% | 7.3% | 11.12 | -3.2% |
| Alavés win | 4.3% | 3.5% | 21.79 | -6.2% |

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
| Market best home last update utc | 2026-10-31T11:28:22Z |
| Market best draw last update utc | 2026-10-31T11:28:22Z |
| Market best away last update utc | 2026-10-31T11:28:22Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.9293 |
| Dc lambda away | 0.7253 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:27:45.223690+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 47.6% |
| P btts no | 52.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 50.80 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.02 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.64 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.16 |
| Fair Under 4.5 odds | 1.46 |
| Goal margin distribution | {"-1": 0.03168693247469067, "-10": 2.4113615561387626e-10, "-11": 1.5650120065000754e-11, "-12": 9.33295868295053e-13, "-13": 5.147263038506832e-14, "-14": 2.6400093661670603e-15, "-15": 1.2653388554739701e-16, "-16": 5.6914341998736e-18, "-17": 2.4114313499427554e-19, "-18": 9.654752438182224e-21, "-19": 3.647332513938741e-22, "-2": 0.009085873457362236, "-20": 1.1956193630378553e-23, "-3": 0.0018918954616817226, "-4": 0.00031198270594342176, "-5": 4.2391069953329595e-05, "-6": 4.885711174442055e-06, "-7": 4.881964292787455e-07, "-8": 4.301778973820222e-08, "-9": 3.388056800288179e-09, "0": 0.08704330196704835, "1": 0.20118230355939867, "10": 0.00042769067269170013, "11": 0.00011211338714803015, "12": 2.7004211244230114e-05, "13": 6.0153495543307e-06, "14": 1.2461270638236638e-06, "15": 2.41232633832717e-07, "16": 4.3825137467561496e-08, "17": 7.499785183710377e-09, "18": 1.2127950544030947e-09, "19": 1.8505208671753658e-10, "2": 0.22753871518870947, "20": 2.4501006299976905e-11, "3": 0.19136305982018723, "4": 0.1274570449518903, "5": 0.0699487658967107, "6": 0.03256160633175742, "7": 0.013141501353569562, "8": 0.004677037279663035, "9": 0.0014878041826030183} |
| Raw goal margin distribution | {"-1": 0.04569062999273078, "-10": 3.4770367478213043e-10, "-11": 2.2566521571720615e-11, "-12": 1.3457558956227098e-12, "-13": 7.422040336517955e-14, "-14": 3.80673298758814e-15, "-15": 1.8245416941846473e-16, "-16": 8.206702064395301e-18, "-17": 3.477137386243045e-19, "-18": 1.392156598549718e-20, "-19": 5.2592317191933695e-22, "-2": 0.013101277084258504, "-20": 1.724010425191541e-23, "-3": 0.0027279982243049237, "-4": 0.00044986009272994396, "-5": 6.112534540162863e-05, "-6": 7.044898451469979e-06, "-7": 7.039495675942763e-07, "-8": 6.202903722546201e-08, "-9": 4.885371904647699e-09, "0": 0.12083639293573917, "1": 0.18896997867531964, "10": 0.00040172866036560504, "11": 0.00010530779300042153, "12": 2.5364980580706724e-05, "13": 5.650201120551598e-06, "14": 1.1704836882334001e-06, "15": 2.265891426066739e-07, "16": 4.116482983923541e-08, "17": 7.044527382184952e-09, "18": 1.1391750244097415e-09, "19": 1.7381891081941848e-10, "2": 0.21372648287787901, "20": 2.301372713263284e-11, "3": 0.17974679031740975, "4": 0.11972004813766714, "5": 0.06570268142875549, "6": 0.030585026343182532, "7": 0.012343775702978375, "8": 0.004393128119942483, "9": 0.001397490334315288} |
| Unadjusted home-win probability | 81.7% |
| Unadjusted draw probability | 12.1% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 88.1% |
| Raw p under 3 5 | 50.4% |
| Raw p btts yes | 49.0% |
| P home draw | 95.7% |
| P draw away | 13.0% |
| P home away | 91.3% |
| Raw p home draw | 93.8% |
| Raw p draw away | 18.3% |
| Raw p home away | 87.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7256 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": -2.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.92, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:10Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 19.1, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:10Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.03, "price": 19.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.08, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.11 |
| Reference draw odds | 11.12 |
| Reference away odds | 21.79 |
| Market reference 1x2 last update utc | 2026-10-31T11:28:22Z |
| Market reference home last update utc | 2026-10-31T11:28:22Z |
| Market reference draw last update utc | 2026-10-31T11:28:22Z |
| Market reference away last update utc | 2026-10-31T11:28:22Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.63 |
| Market reference over 2 5 last update utc | 2026-10-31T11:26:29Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:26:29Z |
| Home probability edge | -2.3% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -9.1% |
| Under 2.5 probability edge | +9.1% |
| Raw edge prob home | -0.0754 |
| Raw ev home | -0.0930 |
| Raw edge prob draw | 0.0483 |
| Raw ev draw | 0.3437 |
| Raw edge prob away | 0.0272 |
| Raw ev away | 0.3518 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.02820008688981613, 0.016662148717136928, 0.005698077899615925, 0.001229441030782798, 0.00019895198979389414, 2.5756026195252383e-05, 2.778613766976952e-06, 2.569394076390227e-07, 2.078936895968904e-08, 1.495200291127812e-09, 9.678319353662169e-11, 5.695185032903916e-12, 3.0720421345170326e-13, 1.5296229501922412e-14, 7.072239031642031e-16, 3.0518715251648014e-17, 1.2346584694270914e-18, 4.7010892240144374e-20, 1.6905443330179206e-21, 5.759350888009197e-23], [0.09883223155418105, 0.0485941242074363, 0.015390033996776584, 0.00332061786344737, 0.0005373527601054318, 6.956488236033427e-05, 7.504804443015627e-06, 6.93971947793612e-07, 5.6150354680604165e-08, 4.038411499077316e-09, 2.614033477755041e-10, 1.53822206046415e-11, 8.297330033507271e-13, 4.1313842352515135e-14, 1.9101528804588228e-15, 8.242850897009774e-17, 3.3347097308325423e-18, 1.2697250591175482e-19, 4.566019492284844e-21, 1.555552723696555e-22], [0.13520571999804468, 0.08751764859515042, 0.020825756972638432, 0.004484356190725586, 0.0007256725330871443, 9.394447771409648e-05, 1.0134925983107003e-05, 9.371802261665153e-07, 7.582871651542435e-08, 5.45370661464304e-09, 3.530143392219496e-10, 2.077304858075973e-11, 1.1205198801051801e-12, 5.579262424488205e-14, 2.57958194738646e-15, 1.1131626995121594e-16, 4.503386670999512e-18, 1.7147108350076587e-19, 6.1662192456990515e-21, 2.1007091973138915e-22], [0.12172646425612041, 0.07879262743951475, 0.02550093842272273, 0.004045480004629752, 0.0006533270312954073, 8.45787375614748e-05, 9.124530422521636e-06, 8.437485877346828e-07, 6.826901665577297e-08, 4.910002500636171e-09, 3.178207796668665e-10, 1.8702091565305596e-11, 1.0088103013383461e-12, 5.023041096928448e-14, 2.3224120230920143e-15, 1.0021865905922689e-16, 4.054424151928179e-18, 1.543763734035518e-19, 5.551481598691551e-21, 1.8912802137589358e-22], [0.0821932613160385, 0.05320308165106076, 0.017218977881201945, 0.003715238416926179, 0.0004420402833503569, 5.711003207604795e-05, 6.16114924546291e-06, 5.697236716807725e-07, 4.609723251281243e-08, 3.315376989411733e-09, 2.1460186619617854e-10, 1.2628198055184643e-11, 6.811781581181117e-13, 3.39170394871863e-14, 1.568160378797118e-15, 6.767056353059097e-17, 2.737665517864042e-18, 1.0423943287700056e-19, 3.748522398320556e-21, 1.2770475983288518e-22], [0.04439943111500942, 0.028739418792371924, 0.009301405128185562, 0.002006909928222579, 0.00032476443648767636, 3.091246319441449e-05, 3.3281502295108968e-06, 3.077552406409352e-07, 2.490095741152704e-08, 1.7909114434050323e-09, 1.1592435465838418e-10, 6.8215423099224205e-12, 3.679610983207517e-13, 1.8321419958579187e-14, 8.470941242734652e-16, 3.6554511597218525e-17, 1.4788413262855005e-18, 5.630840588858506e-20, 2.024889380740842e-21, 6.898398477531401e-23], [0.019986527806262318, 0.012937129562351093, 0.004187053472605112, 0.0009034161041654592, 0.0001461936172905552, 1.892600642202675e-05, 1.5012149607714069e-06, 1.3853688031857786e-07, 1.1209235461122717e-08, 8.061837835140124e-10, 5.218367171870279e-11, 3.0707363052849868e-12, 1.656387151484107e-13, 8.247438317482475e-15, 3.8132178372865725e-16, 1.645511539527732e-17, 6.657045495085896e-19, 2.5347386030765172e-20, 9.115096048854754e-22, 3.105333323589584e-23], [0.00771170679543988, 0.004991729975639355, 0.0016155546891662629, 0.00034857881154422857, 5.640811264657318e-05, 7.302509658008326e-06, 7.878099562177145e-07, 5.356222088484545e-08, 4.3250302461311485e-09, 3.110621825843343e-10, 2.0134821801215197e-11, 1.1848290139245903e-12, 6.391091126882475e-14, 3.1822348901429834e-15, 1.4713119854205793e-16, 6.349128094863343e-18, 2.568589375785474e-19, 9.78016847122606e-21, 3.517016503437668e-22, 1.1981781090624624e-23], [0.002603584749231677, 0.001685280882896419, 0.0005454348384653645, 0.00011768529350448274, 1.9044201979567514e-05, 2.4654338243189147e-06, 2.65976137541199e-07, 2.4594908453326534e-08, 1.4631551305231565e-09, 1.0501913209643709e-10, 6.797809662724755e-12, 4.000155650271077e-13, 2.157725628098386e-14, 1.0743689365042334e-15, 4.9673639678157594e-17, 2.1435582961322463e-18, 8.671932560750468e-20, 3.3019275955431605e-21, 1.1873960945404589e-22, 4.04522414345803e-24], [0.0007813406265151942, 0.0005057559279700619, 0.00016368600965860832, 3.531757550260361e-05, 5.715200440695583e-06, 7.398812769561505e-07, 7.981993365334444e-08, 7.380977779070557e-09, 5.972064454509132e-10, 3.158036374529269e-11, 2.0400353252844205e-12, 1.200454151862517e-13, 6.475374748618424e-15, 3.2242011642002556e-16, 1.490715167189206e-17, 6.432858321842846e-19, 2.6024630932846772e-20, 9.909146137727395e-22, 3.5633977680339414e-23, 1.2139792905057594e-24], [0.00021103359794259844, 0.00013660046532630192, 4.421022839320041e-05, 9.538983096482924e-06, 1.543628055464564e-06, 1.9983577280860135e-07, 2.155869951564231e-08, 1.993540645644821e-09, 1.6130048869993777e-10, 1.1600955186800087e-11, 5.521141786804254e-13, 3.242326716870788e-14, 1.7489448069817232e-15, 8.708298904238063e-17, 4.0262975527412005e-18, 1.7374614740925446e-19, 7.029036139310614e-21, 2.676377870315373e-22, 9.624440690390799e-24, 3.278856990271341e-25], [5.181674343868882e-05, 3.354058943421784e-05, 1.0855286003508367e-05, 2.3421817407050508e-06, 3.7901916895965404e-07, 4.9067253131475015e-08, 5.2934774963068965e-09, 4.894897550771665e-10, 3.960538094873978e-11, 2.848474008018634e-12, 1.8437958635906796e-13, 7.977288566399708e-15, 4.294322100144886e-16, 2.1382173005032858e-17, 9.886085880740141e-19, 4.2661261673673253e-20, 1.725894671762166e-21, 6.571521634618466e-23, 2.363164817625421e-24, 8.050836127205418e-26], [1.1662725822822699e-05, 7.549194961856234e-06, 2.443268642249634e-06, 5.271698230396518e-07, 8.530826825118618e-08, 1.1043880455909875e-08, 1.1914368328020788e-09, 1.1017258954724625e-10, 8.914236373425129e-12, 6.411242614709334e-13, 4.1499492641324576e-14, 2.442028215100659e-15, 9.685110554724275e-17, 4.812622420954083e-18, 2.2251245724150147e-19, 9.602042991074074e-21, 3.884581511697961e-22, 1.4790944003261773e-23, 5.31892618352542e-25, 1.812053173645921e-26], [2.4230808794775156e-06, 1.5684420816723438e-06, 5.076203985586981e-07, 1.0952629238228681e-07, 1.7723886919838335e-08, 2.2945078169962445e-09, 2.4753628375782613e-10, 2.2889768586692703e-11, 1.852046943375854e-12, 1.3320178858182002e-13, 8.622051881767891e-15, 5.073626839083901e-16, 2.7367671698868177e-17, 1.0019121661244989e-18, 4.6229817006617026e-20, 1.9949475902162247e-21, 8.07071633918345e-23, 3.0730083299730735e-24, 1.1050751368459645e-25, 3.7647728878833404e-27], [4.6746712248618445e-07, 3.025879626699498e-07, 9.793145950649916e-08, 2.113009977098588e-08, 3.4193387797579006e-09, 4.4266246984069943e-10, 4.77553495053562e-11, 4.415954228446208e-12, 3.573017568922125e-13, 2.5697638632592034e-14, 1.6633888770422398e-15, 9.788174051980648e-17, 5.279843048811118e-18, 2.628925238404696e-19, 8.936868162038216e-21, 3.848705247140637e-22, 1.5570237772227566e-23, 5.928528319278984e-25, 2.1319399559778627e-26, 7.263098659308115e-28], [8.417265183314572e-08, 5.448432628857512e-08, 1.763364790386084e-08, 3.804709348891998e-09, 6.156899571405499e-10, 7.970629839235968e-11, 8.598881533542145e-12, 7.951416471927301e-13, 6.433615314443493e-14, 4.6271454943210285e-15, 2.9951165777341195e-16, 1.7624695447623657e-17, 9.506944324076338e-19, 4.7336721267311786e-20, 2.1886217628636365e-21, 6.944078239468216e-23, 2.8035943918168036e-24, 1.0674974262310024e-25, 3.838794880146896e-27, 1.3078016512226434e-28], [1.4208957785114115e-08, 9.197351815876781e-09, 2.9766884279729933e-09, 6.422626986993315e-10, 1.0393295707340256e-10, 1.3455004736096145e-11, 1.4515539435717869e-12, 1.3422571170198765e-13, 1.0860412071821362e-14, 7.81095920854646e-16, 5.055975318311305e-17, 2.9751771880396314e-18, 1.6048415681854197e-19, 7.990783936643022e-21, 3.6945532258810905e-22, 1.594304397493528e-23, 4.742271481178809e-25, 1.8020135441499037e-26, 6.480165850761572e-28, 2.2076646094459398e-29], [2.257483057023079e-09, 1.4612518530792111e-09, 4.729286830048617e-10, 1.020410632784504e-10, 1.6512603753761444e-11, 2.137696915091397e-12, 2.3061919695484734e-13, 2.13254395267153e-14, 1.7254746347484303e-15, 1.240985323417964e-16, 8.032804932232383e-18, 4.726885810497251e-19, 2.549731447003407e-20, 1.269555418638956e-21, 5.869812154297663e-23, 2.5329902583352085e-24, 1.0247409989714434e-25, 2.868800461063011e-27, 1.0295522610475761e-28, 3.5074813556240404e-30], [3.3873743242703533e-10, 2.1926219968801258e-10, 7.096338876333297e-11, 1.531135645493952e-11, 2.477731551886014e-12, 3.2076341041519985e-13, 3.460462500564012e-14, 3.199902036112469e-15, 2.5890907383527016e-16, 1.8621100203895683e-17, 1.2053298515204782e-18, 7.092736124164208e-20, 3.825895751684366e-21, 1.9049797140036445e-22, 8.80770773357555e-24, 3.800775442375289e-25, 1.5376334002348762e-26, 5.854697462759122e-28, 1.5479862692454155e-29, 5.263008397753117e-31], [4.815271591647516e-11, 3.116889189703753e-11, 1.0087694988734983e-11, 2.1765631049039826e-12, 3.52218243730574e-13, 4.559764554940313e-14, 4.919169001647514e-15, 4.548773148614573e-16, 3.680483432628282e-17, 2.6470548050916934e-18, 1.7134187240559747e-19, 1.0082573549971258e-20, 5.43864520483987e-22, 2.70799558046554e-23, 1.2520465935265657e-24, 5.402935802745534e-26, 2.1857998915175206e-27, 8.322658103688438e-29, 2.9928856531723954e-30, 7.496726631459112e-32]] |
| Legacy trial inputs | {"lambda_home": 2.7009167420848943, "lambda_away": 0.6472925006162171, "rho": -0.01984634636300814, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8486 |
| Legacy p draw | 0.1021 |
| Legacy p away | 0.0493 |
| Legacy p over 1 5 | 0.8563 |
| Legacy p under 3 5 | 0.5591 |
| Legacy p btts yes | 0.4343 |
| Legacy p over 2 5 | 0.6668 |
| Legacy goal margin distribution | {"-1": 0.03725044708724265, "-10": 1.1333776982283272e-10, "-11": 6.583102247630608e-12, "-12": 3.5120065130807924e-13, "-13": 1.732185937185997e-14, "-14": 7.943139926850871e-16, "-15": 3.403057525233984e-17, "-16": 1.367986322605921e-18, "-17": 5.1786982652160605e-20, "-18": 1.8460996053875762e-21, "-19": 5.759350888009197e-23, "-2": 0.009835427465415287, "-3": 0.0018704582503791245, "-4": 0.0002795434882594308, "-5": 3.426971431817103e-05, "-6": 3.5535460260664047e-06, "-7": 3.1887429426982966e-07, "-8": 2.5200196776890318e-08, "-9": 1.7784202786343378e-09, "0": 0.10213995709354273, "1": 0.21591056044574902, "10": 0.0002471304828296673, "11": 5.989531827769252e-05, "12": 1.3333010179063924e-05, "13": 2.7439615910363585e-06, "14": 5.250327015952083e-07, "15": 9.385859590672604e-08, "16": 1.5743349590061564e-08, "17": 2.4868329516998267e-09, "18": 3.6990632432407286e-10, "19": 4.815271591647516e-11, "2": 0.2333780048952388, "3": 0.18519332253973259, "4": 0.11548811853305467, "5": 0.05907572110177289, "6": 0.02556060410586682, "7": 0.00957060298615817, "8": 0.0031559807386731895, "9": 0.0009293417229522854} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.8046 |
| Legacy raw p draw | 0.1317 |
| Legacy raw p away | 0.0637 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.7009 |
| Legacy lambda away | 0.6473 |
| Legacy model home team | Barcelona |
| Legacy model away team | Alaves |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 94.4% |
| Market home draw odds | 1.03 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:28:10Z |
| Market reference home draw last update utc | 2026-10-31T11:28:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 14.8% |
| Market draw away odds | 7.68 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:28:10Z |
| Market reference draw away last update utc | 2026-10-31T11:28:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 90.8% |
| Market home away odds | 1.07 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:28:10Z |
| Market reference home away last update utc | 2026-10-31T11:28:22Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 6.50 |
| Market reference dc home draw odds | 1.02 |
| Market reference dc home away odds | 1.06 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.99, "price": 1.66, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.66, "price": 1.99, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.07, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.61, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 94.5% |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 7.60 |
| Market reference over 1 5 last update utc | 2026-10-31T11:28:22Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 37.4% |
| Market under 3 5 odds | 2.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market reference under 3 5 odds | 2.47 |
| Market reference under 3 5 opposite odds | 1.54 |
| Market reference under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 50.8% |
| Market btts yes odds | 1.89 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:28:10Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 1.85 |
| Market reference btts yes last update utc | 2026-10-31T11:28:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 10.265900662256545, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,725.4846 |
| Elo away rating | 1,438.3571 |
| Elo rating diff | 347.1275 |
| Elo home expectancy | 0.8806 |

</details>


---

## 2026-10-31 — Levante vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **60.7%**. Expected goals are 1.22 for Levante and 1.88 for Atlético Madrid (3.10 combined). The most likely exact score is 1-2 at 11.0%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.8%; Double Chance 1X: 39.3%; Double Chance X2: 81.6%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 76.9%; BTTS Yes (both teams score): 61.5%; BTTS No (at least one team does not score): 38.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 18.4% | 5.44 |
| Draw | 20.9% | 4.79 |
| Atlético Madrid win | 60.7% | 1.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.22 |
| Atlético Madrid expected goals | 1.88 |
| Expected total goals | 3.10 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 63.6% |
| Under 2.5 | 36.4% |
| Over 3.5 | 41.2% |
| Under 3.5 | 58.8% |
| Over 4.5 | 23.1% |
| Under 4.5 | 76.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.04% |
| 2 | 1-1 | 9.38% |
| 3 | 0-2 | 8.64% |
| 4 | 0-1 | 8.52% |
| 5 | 1-3 | 7.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 18.4% | 15.8% | 5.94 | +9.2% |
| Draw | 20.9% | 19.9% | 4.74 | -1.1% |
| Atlético Madrid win | 60.7% | 64.3% | 1.53 | -7.1% |

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
| Market best home last update utc | 2026-10-31T11:28:22Z |
| Market best draw last update utc | 2026-10-31T11:28:22Z |
| Market best away last update utc | 2026-10-31T11:28:22Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Levante |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2226 |
| Dc lambda away | 1.8755 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:27:45.223690+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.5% |
| P btts no | 38.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.67 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.25 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.43 |
| Fair Under 3.5 odds | 1.70 |
| Fair Over 4.5 odds | 4.32 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.2525526273477259, "-10": 1.2954700368652447e-05, "-11": 2.2650976132372813e-06, "-12": 3.64056157212874e-07, "-13": 5.412964017727059e-08, "-14": 7.482797009695433e-09, "-15": 9.579180097321064e-10, "-16": 1.0143429566183966e-10, "-2": 0.18523676376286663, "-3": 0.10192718203560108, "-4": 0.04473646444485706, "-5": 0.016247670370723638, "-6": 0.005018821497292412, "-7": 0.0013465091257704276, "-8": 0.0003189705898865578, "-9": 6.759848327275214e-05, "0": 0.20865537411924243, "1": 0.10704888761879429, "10": 1.1748417541376517e-07, "11": 1.339101607955765e-08, "12": 1.4030385317966514e-09, "13": 1.3599125022171889e-10, "14": 1.2255030569008606e-11, "15": 1.0227120710491194e-12, "16": 7.059671126300699e-14, "2": 0.05150890488556943, "3": 0.018476502188015574, "4": 0.005286472865362817, "5": 0.0012516129762141146, "6": 0.0002520317851880058, "7": 4.407958284099059e-05, "8": 6.806963546638626e-06, "9": 9.404037310799664e-07} |
| Raw goal margin distribution | {"-1": 0.2240135138387655, "-10": 8.234670034743093e-06, "-11": 1.3803641858799687e-06, "-12": 2.1265030407873444e-07, "-13": 3.0300454341877816e-08, "-14": 4.014025564525738e-09, "-15": 4.930390630108603e-10, "-16": 5.054872007868771e-11, "-2": 0.1603724977645938, "-3": 0.08549899223387071, "-4": 0.03621688402639864, "-5": 0.01266510448935956, "-6": 0.003761359927881528, "-7": 0.0009692752666226708, "-8": 0.00022038492812873281, "-9": 4.480674394087356e-05, "0": 0.23093504547962396, "1": 0.14507765324300095, "10": 1.1412802125872544e-07, "11": 1.2471376127418014e-08, "12": 1.2524526364021164e-09, "13": 1.1633731931457262e-10, "14": 1.0046728230216449e-11, "15": 8.0445259762357e-13, "16": 5.37655262651338e-14, "2": 0.0681520792879509, "3": 0.02368562350045283, "4": 0.006540478416220949, "5": 0.0014910143393167168, "6": 0.00028866394663939885, "7": 4.849192122938035e-05, "8": 7.187514918079914e-06, "9": 9.526094001852452e-07} |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 52.4% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 62.5% |
| Raw p btts yes | 60.0% |
| P home draw | 39.3% |
| P draw away | 81.6% |
| P home away | 79.1% |
| Raw p home draw | 47.6% |
| Raw p draw away | 75.5% |
| Raw p home away | 76.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0446 |
| Totals anchor target over 2 5 | 0.6358 |
| Totals anchor reference over odds | 1.54 |
| Totals anchor reference under odds | 2.62 |
| Totals anchor reference last update utc | 2026-10-31T11:28:22Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6091 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.51, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.62, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.72, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.72, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.94 |
| Reference draw odds | 4.74 |
| Reference away odds | 1.53 |
| Market reference 1x2 last update utc | 2026-10-31T11:28:22Z |
| Market reference home last update utc | 2026-10-31T11:28:22Z |
| Market reference draw last update utc | 2026-10-31T11:28:22Z |
| Market reference away last update utc | 2026-10-31T11:28:22Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.56 |
| Market reference over 2 5 last update utc | 2026-10-31T11:26:29Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:26:29Z |
| Home probability edge | +2.6% |
| Draw probability edge | +1.0% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0877 |
| Raw ev home | 0.4570 |
| Raw edge prob draw | 0.0318 |
| Raw ev draw | 0.0946 |
| Raw edge prob away | -0.1196 |
| Raw ev away | -0.1986 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.036905415320898804, 0.07863013838515996, 0.08464457373954987, 0.05927747927468406, 0.03113447850749922, 0.013082280337084699, 0.004580828795554572, 0.0013748581121179224, 0.00036106031216544607, 8.428476953980206e-05, 1.7707651390413975e-05, 3.382050889410496e-06, 5.921213925650758e-07, 9.569279933690875e-08, 1.4360285803225838e-08, 2.0113316340832815e-09, 2.641043542128298e-10, 3.263912441697208e-11], [0.03667884576523255, 0.09166694644712908, 0.10310777901606191, 0.07220745481558874, 0.037925726220907195, 0.015935869370348542, 0.005580027901325051, 0.0016747507860206596, 0.00043981705186177145, 0.00010266949206773606, 2.1570155366062984e-05, 4.119765040100579e-06, 7.212786242286458e-07, 1.1656591287018528e-07, 1.749264140383602e-08, 2.4500559042708523e-09, 3.2171245229666177e-10, 3.9758574932612146e-11], [0.023311734495826072, 0.04897635361784325, 0.05750719682878528, 0.043978898856213845, 0.02309916173859722, 0.009705950569983132, 0.003398589291285279, 0.0010200289653730637, 0.0002678763527736356, 6.253220278705927e-05, 1.3137586466378315e-05, 2.5091970139741575e-06, 4.393042206391754e-07, 7.099600041702865e-08, 1.0654123026383677e-08, 1.4922387318758566e-09, 1.9594319501322317e-10, 2.4215482322346857e-11], [0.009465545408233135, 0.019886461008827256, 0.020890044598572504, 0.016352488738627248, 0.009379231921501236, 0.0039410244598784, 0.001379970300637886, 0.00041417469348668725, 0.00010876907427993918, 2.5390706344211798e-05, 5.33441307313956e-06, 1.0188396010699224e-06, 1.783760041207192e-07, 2.882736442758674e-08, 4.3260223862447225e-09, 6.059117342394315e-10, 7.95611845255027e-11, 9.832505065012695e-12], [0.002882557384072992, 0.006056055150737993, 0.006361678034828583, 0.004455149588467519, 0.0026155802276013294, 0.0012001663578470212, 0.00042024451929048215, 0.00012612926878653808, 3.312361672806632e-05, 7.732271612756286e-06, 1.624497176919064e-06, 3.1026882113899117e-07, 5.432112420826594e-08, 8.778842487177322e-09, 1.3174103799965264e-09, 1.845192504289476e-10, 2.4228892266482803e-11, 2.994308183703275e-12], [0.0007022637757563507, 0.0014754079762105666, 0.0015498654290699227, 0.0010853869514770179, 0.000570080865896628, 0.0002677516813052235, 0.0001023821778842941, 3.0728275183984664e-05, 8.069749549023738e-06, 1.8837766380474512e-06, 3.9576853785188215e-07, 7.558932045427837e-08, 1.3233997699613729e-08, 2.1387477334811337e-09, 3.209544388565561e-10, 4.4953549310740495e-11, 5.902770040058014e-12, 7.294890927355621e-13], [0.00014257432580079308, 0.0002995388695120686, 0.00031465529941881364, 0.00022035639339811766, 0.00011573841327584529, 4.863169196424066e-05, 1.9034167003166112e-05, 6.2384865468240485e-06, 1.638328988412028e-06, 3.8244630208875065e-07, 8.03493422348682e-08, 1.534622284895972e-08, 2.6867800459158327e-09, 4.342108003942412e-10, 6.51605056568113e-11, 9.12651656911776e-12, 1.19838654344942e-12, 1.4810163811138945e-13], [2.4810504558011323e-05, 5.212516661460095e-05, 5.4755698100516407e-05, 3.834598741452035e-05, 2.0140571691213887e-05, 8.462791658776227e-06, 2.9632907048634656e-06, 9.941272193468637e-07, 2.8509879746029704e-07, 6.655255543291333e-08, 1.3982234953975988e-08, 2.6705196030480186e-09, 4.675481942569905e-10, 7.556051190711044e-11, 1.1339103401123333e-11, 1.5881785143647686e-12, 2.0854087600634391e-13, 2.577235660609473e-14], [3.777790926556965e-06, 7.936879357752703e-06, 8.337419296643428e-06, 5.8387818347558014e-06, 3.066719937630989e-06, 1.288593606273253e-06, 4.512077822282345e-07, 1.354223672906605e-07, 3.975265692282362e-08, 1.0133677026429325e-08, 2.129015966548003e-09, 4.0662876089433153e-10, 7.119159232986306e-11, 1.1505280580700996e-11, 1.7265574685873504e-12, 2.4182524653182044e-13, 3.175363996934993e-14, 3.924248082695952e-15], [5.113140417835292e-07, 1.0742356955310458e-06, 1.1284477202384582e-06, 7.902637274165261e-07, 4.1507245816732966e-07, 1.74407747238803e-07, 6.106978371764114e-08, 1.832906037243009e-08, 4.813512173684794e-09, 1.2559874831287607e-09, 2.8815669793284726e-10, 5.5036130712453234e-11, 9.635594325587326e-12, 1.5572093929859964e-12, 2.3368500131359106e-13, 3.273040954708826e-14, 4.2977714515463434e-15, 5.311366317334173e-16], [6.228450673075119e-08, 1.3085547225601722e-07, 1.3745918140900382e-07, 9.626410078169048e-08, 5.0561066588931056e-08, 2.1245065887295385e-08, 7.43907079441656e-09, 2.232710997243224e-09, 5.863465637177835e-10, 1.3687487471833468e-10, 3.214322741444305e-11, 6.7040956705146325e-12, 1.173737058996928e-12, 1.8968776718963482e-13, 2.8465783936663285e-14, 3.986977174780829e-15, 5.23522831423425e-16, 6.469914848955787e-17], [6.897308541735262e-09, 1.449077168461576e-08, 1.5222058194516654e-08, 1.0660166379004251e-08, 5.599069411765951e-09, 2.3526520816423835e-09, 8.237934155071348e-10, 2.472476293194882e-10, 6.493128668146089e-11, 1.5157352800830754e-11, 3.184455754747932e-12, 6.798424521714834e-13, 1.2997817704115735e-13, 2.100578660043887e-14, 3.1522653866760445e-15, 4.4151287642360474e-16, 5.797426497378746e-17, 7.164702956533208e-18], [7.001493948045659e-10, 1.470965807001923e-09, 1.5451990828134529e-09, 1.0821190604441262e-09, 5.683644622240471e-10, 2.3881894237157096e-10, 8.36237001464049e-11, 2.509823607098652e-11, 6.59120884600432e-12, 1.538630804483486e-12, 3.232557679531832e-13, 6.173983400785583e-14, 1.208230953713678e-14, 2.1323083760424355e-15, 3.199881068665881e-16, 4.481820283316464e-17, 5.8849979365175435e-18, 7.272927415987639e-19], [6.560541321687175e-11, 1.37832468773593e-10, 1.4478827673428806e-10, 1.01396742805307e-10, 5.325689871145559e-11, 2.237781752661027e-11, 7.835709697871033e-12, 2.3517554405817622e-12, 6.17609588967103e-13, 1.4417281578101368e-13, 3.028971872099587e-14, 5.78514721584108e-15, 1.0128497582231444e-15, 1.8296474837511553e-16, 2.9983532273604015e-17, 4.1995561780469366e-18, 5.514361995748642e-19, 6.814879966515864e-20], [5.7082626710844615e-12, 1.1992667948951784e-11, 1.259788597872035e-11, 8.822431161461477e-12, 4.633830532968083e-12, 1.9470719592181234e-12, 6.817774170852865e-13, 2.0462393474476737e-13, 5.373760470573615e-14, 1.2544335324699276e-14, 2.6354787237014732e-15, 5.033599863131611e-16, 8.812706425870419e-17, 1.4242223946219303e-17, 2.3889965411987145e-18, 3.653992649512424e-19, 4.797992298459258e-20, 5.929560231895563e-21], [4.635589816360212e-13, 9.739055929707029e-13, 1.0230543917757122e-12, 7.16455678446208e-13, 3.7630604734040666e-13, 1.5811863374110152e-13, 5.5366065539946484e-14, 1.6617186046664412e-14, 4.363945870805131e-15, 1.0187056278742718e-15, 2.1402305809630096e-16, 4.087706822491421e-17, 7.156659480523869e-18, 1.1565884769432483e-18, 1.7356521285522313e-19, 2.717297395168242e-20, 3.89637364628965e-21, 4.815302064795761e-22], [3.5292085871407194e-14, 7.414624930027448e-14, 7.788808949023513e-14, 5.4545842769657313e-14, 2.864926765046519e-14, 1.2038028861324327e-14, 4.215178686650894e-15, 1.2651144301643682e-15, 3.322398195523602e-16, 7.755700551791635e-17, 1.6294194361498888e-17, 3.112089419287268e-18, 5.448571831089775e-19, 8.805442557083516e-20, 1.3214021600352088e-20, 1.850783474816192e-21, 2.7164478802414838e-22, 3.666028719102071e-23], [2.528836292803626e-15, 5.3129114240796576e-15, 5.581031061686853e-15, 3.908454357729628e-15, 2.0528485638599773e-15, 8.6257877727193265e-16, 3.020364645573747e-16, 9.065112493510061e-17, 2.3806473685343434e-17, 5.557307409641575e-18, 1.1675521309081419e-18, 2.229951694728211e-19, 3.904146170507418e-20, 6.3094946537549305e-21, 9.46843933187138e-22, 1.326169396246506e-22, 1.7413692801194193e-23, 2.4055129740848868e-24]] |
| Legacy trial inputs | {"lambda_home": 1.2181262715472234, "lambda_away": 2.100931341106874, "rho": -0.01984634636300814, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1857 |
| Legacy p draw | 0.2053 |
| Legacy p away | 0.6089 |
| Legacy p over 1 5 | 0.8478 |
| Legacy p under 3 5 | 0.5727 |
| Legacy p btts yes | 0.6167 |
| Legacy p over 2 5 | 0.6482 |
| Legacy goal margin distribution | {"-1": 0.2364051307286825, "-10": 2.2296911603669526e-05, "-11": 4.178842106564522e-06, "-12": 7.199722985772434e-07, "-13": 1.1476023496532983e-07, "-14": 1.7016117407574922e-08, "-15": 2.35725956870229e-09, "-16": 3.03862929145442e-10, "-17": 3.263912441697208e-11, "-2": 0.18434489461487968, "-3": 0.10842372222954211, "-4": 0.05091820234862541, "-5": 0.019799250143727413, "-6": 0.006550549491290829, "-7": 0.0018828657284548228, "-8": 0.00047794275695354105, "-9": 0.00010855160705986764, "0": 0.2053354485800492, "1": 0.11162220979468312, "10": 7.842667049598225e-08, "11": 8.522273702745599e-09, "12": 8.513257170817531e-10, "13": 7.867773424893276e-11, "14": 6.76396480790313e-12, "15": 5.432862619979825e-13, "16": 4.060499729548685e-14, "17": 2.528836292803626e-15, "2": 0.050769931834569196, "3": 0.017313314915732084, "4": 0.004714215467858245, "5": 0.001062834292249769, "6": 0.00020388017518835298, "7": 3.3977941669914615e-05, "8": 5.00073741088817e-06, "9": 6.585289519201643e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2139 |
| Legacy raw p draw | 0.2116 |
| Legacy raw p away | 0.5745 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2181 |
| Legacy lambda away | 2.1009 |
| Legacy model home team | Levante |
| Legacy model away team | Ath Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 37.1% |
| Market home draw odds | 2.66 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:28:10Z |
| Market reference home draw last update utc | 2026-10-31T11:28:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.2% |
| Market draw away odds | 1.16 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:28:10Z |
| Market reference draw away last update utc | 2026-10-31T11:28:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.7% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:28:10Z |
| Market reference home away last update utc | 2026-10-31T11:28:22Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.14 |
| Market reference dc home draw odds | 2.56 |
| Market reference dc home away odds | 1.19 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.29, "price": 1.62, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.62, "price": 2.29, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.06, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.06, "price": 1.78, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 85.0% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-31T11:28:22Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 58.8% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.33 |
| Market reference under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.9% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:28:10Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.25 |
| Market reference btts yes last update utc | 2026-10-31T11:28:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 9.763842394005463, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,476.0819 |
| Elo away rating | 1,586.5836 |
| Elo rating diff | -50.5017 |
| Elo home expectancy | 0.4278 |

</details>


---

## 2026-10-31 — Rayo Vallecano vs Celta Vigo

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **37.7%**. Expected goals are 1.17 for Rayo Vallecano and 1.10 for Celta Vigo (2.28 combined). The most likely exact score is 1-1 at 14.2%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 43.5%; Under 3.5 goals: 77.0%; Double Chance 1X: 67.6%; Double Chance X2: 62.3%; Double Chance 12 (either team wins): 70.1%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 50.5%; BTTS No (at least one team does not score): 49.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 37.7% | 2.65 |
| Draw | 29.9% | 3.34 |
| Celta Vigo win | 32.4% | 3.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.17 |
| Celta Vigo expected goals | 1.10 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 70.4% |
| Under 1.5 | 29.6% |
| Over 2.5 | 43.5% |
| Under 2.5 | 56.5% |
| Over 3.5 | 23.0% |
| Under 3.5 | 77.0% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.19% |
| 2 | 1-0 | 10.56% |
| 3 | 0-0 | 9.64% |
| 4 | 0-1 | 9.42% |
| 5 | 2-1 | 8.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 37.7% | 37.9% | 2.58 | -2.7% |
| Draw | 29.9% | 30.2% | 3.22 | -3.6% |
| Celta Vigo win | 32.4% | 31.8% | 3.06 | -1.0% |

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
| Market best home last update utc | 2026-10-31T11:28:22Z |
| Market best draw last update utc | 2026-10-31T11:28:22Z |
| Market best away last update utc | 2026-10-31T11:28:22Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Vallecano |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1747 |
| Dc lambda away | 1.1016 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:27:45.223690+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 50.5% |
| P btts no | 49.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.37 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.37 |
| Fair Over 2.5 odds | 2.30 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.35 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 10.04 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.1874195144763123, "-10": 1.3896371099655325e-07, "-11": 1.4772770692222448e-08, "-12": 1.4417602270638058e-09, "-13": 1.294676870521954e-10, "-14": 9.882622534447842e-12, "-2": 0.09220429248503811, "-3": 0.03256540664794974, "-4": 0.008987576430296481, "-5": 0.0020280773844488036, "-6": 0.00038632305494048233, "-7": 6.359957235884298e-05, "-8": 9.212821119513666e-06, "-9": 1.1909571606565794e-06, "0": 0.2992821538407435, "1": 0.20984263645891088, "10": 2.7695061021736934e-07, "11": 3.139349470582479e-08, "12": 3.2669879458281417e-09, "13": 3.128186697242468e-10, "14": 2.5461282026064534e-11, "2": 0.1099607743839938, "3": 0.041411402547397606, "4": 0.012186607248588135, "5": 0.002932253575459549, "6": 0.0005955859076045441, "7": 0.00010455017548602458, "8": 1.6148790244411255e-05, "9": 2.22597498168355e-06} |
| Raw goal margin distribution | {"-1": 0.2003539429156431, "-10": 8.372480879495748e-08, "-11": 8.302918194580144e-09, "-12": 7.528736947383568e-10, "-13": 5.802334259689488e-11, "-2": 0.09390987746950714, "-3": 0.031306084379198976, "-4": 0.008117799497777455, "-5": 0.0017166789909073934, "-6": 0.0003059728872395034, "-7": 4.7083631825811766e-05, "-8": 6.370696386225747e-06, "-9": 7.688665680264993e-07, "0": 0.29224174372075196, "1": 0.21386948243224777, "10": 1.5908235290286468e-07, "11": 1.6821913076631867e-08, "12": 1.6264605463192758e-09, "13": 1.3365984025305486e-10, "2": 0.10677383514628296, "3": 0.03795413551217653, "4": 0.010494106249762917, "5": 0.0023663174854519336, "6": 0.00044972149888961575, "7": 7.379168782605249e-05, "8": 1.0646360824941861e-05, "9": 1.370067721295065e-06} |
| Unadjusted home-win probability | 37.2% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 33.6% |
| Raw p over 1 5 | 66.7% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 46.5% |
| P home draw | 67.6% |
| P draw away | 62.3% |
| P home away | 70.1% |
| Raw p home draw | 66.4% |
| Raw p draw away | 62.8% |
| Raw p home away | 70.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0734 |
| Totals anchor target over 2 5 | 0.4354 |
| Totals anchor reference over odds | 2.22 |
| Totals anchor reference under odds | 1.73 |
| Totals anchor reference last update utc | 2026-10-31T11:28:22Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3955 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:25:15Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:25:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.34, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:25:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.51, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:25:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.03, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:25:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:25:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:25:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 5.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:25:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:25:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:25:15Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.82, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.44, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.86, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.82, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.58 |
| Reference draw odds | 3.22 |
| Reference away odds | 3.06 |
| Market reference 1x2 last update utc | 2026-10-31T11:28:22Z |
| Market reference home last update utc | 2026-10-31T11:28:22Z |
| Market reference draw last update utc | 2026-10-31T11:28:22Z |
| Market reference away last update utc | 2026-10-31T11:28:22Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.32 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-31T11:28:22Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:28:22Z |
| Home probability edge | -0.2% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | -0.0072 |
| Raw ev home | -0.0403 |
| Raw edge prob draw | -0.0101 |
| Raw ev draw | -0.0590 |
| Raw edge prob away | 0.0173 |
| Raw ev away | 0.0274 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10682283669405979, 0.10628591783534755, 0.0586054562583396, 0.021026704661567766, 0.0056580351534488895, 0.0012180077596724652, 0.00021850089627521927, 3.359770409197618e-05, 4.520370497594677e-06, 5.406123222543361e-07, 5.818892827830498e-08, 5.693798469211911e-09, 5.10711060275933e-10, 4.228499942636474e-11, 3.250968125244952e-12], [0.11904904258307256, 0.13807669452159513, 0.07078952891170695, 0.02539815594979118, 0.006834340497460571, 0.0014712315375199883, 0.00026392722626244325, 4.058266579653972e-05, 5.460155392708336e-06, 6.530056083438912e-07, 7.028640477672506e-08, 6.877539005531645e-09, 6.168878748689387e-10, 5.107604957854422e-11, 3.926844304028721e-12], [0.07346908919232235, 0.07907861855344811, 0.04400591290667769, 0.01533921591691335, 0.004127599844157766, 0.0008885502657123836, 0.00015939884446709003, 2.450990041826936e-05, 3.2976607701056593e-06, 3.9438272767297737e-07, 4.244947314384138e-08, 4.1536895824797396e-09, 3.725694230654679e-10, 3.084737940097194e-11, 2.3716175603722578e-12], [0.02958110356693734, 0.031839687017711595, 0.017135359184484816, 0.006357024926086032, 0.0016619092439445252, 0.00035775994671258926, 6.417928653352454e-05, 9.868502667703053e-06, 1.3277481161331155e-06, 1.5879162843255628e-07, 1.7091572459035197e-08, 1.6724138419982224e-09, 1.5000886509867628e-10, 1.2420182894061494e-11, 9.548922607559748e-13], [0.008932753534761213, 0.00961478925590337, 0.005174449965270764, 0.0018565102663171463, 0.0005165582719094114, 0.00010803455730991644, 1.9380539584789743e-05, 2.9800410213989787e-06, 4.0094672772509396e-07, 4.7951100842525616e-08, 5.1612274691711634e-09, 5.050271577897028e-10, 4.5298925948571495e-11, 3.750584639219238e-12, 2.8835358350584984e-13], [0.0021579745470206046, 0.0023227407325709104, 0.0012500435925420898, 0.0004484957393489689, 0.00012068484816104851, 2.6863630217521822e-05, 4.681950640275841e-06, 7.199182926329544e-07, 9.68607081539816e-08, 1.158402666290005e-08, 1.2468493020111824e-09, 1.2200445784419267e-10, 1.0943314267430037e-11, 9.060662153484491e-13, 6.966045702775997e-14], [0.0004344362321079526, 0.00046760641056446016, 0.0002516546031854049, 9.028966508814713e-05, 2.4295870764552477e-05, 5.2301829728268795e-06, 9.701694364351557e-07, 1.4493154745910204e-07, 1.9499674427495465e-08, 2.3320575782585006e-09, 2.510115392788257e-10, 2.456153018087405e-11, 2.2030714976130394e-12, 1.8240622586570963e-13, 1.4023810669982396e-14], [7.496507316299247e-05, 8.068882424783228e-05, 4.342479826799966e-05, 1.558012626238118e-05, 4.19242594151471e-06, 9.025054087025982e-07, 1.6190228603123134e-07, 2.5741680616836915e-08, 3.3648080249174324e-09, 4.024131830031571e-10, 4.3313833000274914e-11, 4.238267370265606e-12, 3.801557139940071e-13, 3.1475496417643157e-14, 2.419908642974211e-15], [1.1318788711939955e-05, 1.2183003558074747e-05, 6.5566015707798705e-06, 2.3524042574575386e-06, 6.330038966184435e-07, 1.3626703211877381e-07, 2.4445220824145517e-08, 3.758809733568133e-09, 5.229285007564132e-10, 6.075935900720919e-11, 6.5398472028222835e-12, 6.399253791754831e-13, 5.73987594860246e-14, 4.752406401046517e-15, 3.653759474424698e-16], [1.5191071729214026e-06, 1.635094404869963e-06, 8.799687607608267e-07, 3.157187815817186e-07, 8.495615425932484e-08, 1.8288549348569074e-08, 3.280820169249581e-09, 5.04474018663034e-10, 6.787396735576387e-11, 8.393492031448467e-12, 8.77720138475362e-13, 8.588509410149698e-14, 7.703551101720832e-15, 6.378257281940195e-16, 4.9037510700001273e-17], [1.8349295100351404e-07, 1.9750304841358767e-07, 1.0629142405561109e-07, 3.813567070995641e-08, 1.0261853626149539e-08, 2.2090738226775267e-09, 3.9629025871145785e-10, 6.093541524859306e-11, 8.198496319699538e-12, 9.804966510476978e-13, 1.0912595849693859e-13, 1.0374060266986542e-14, 9.305119151947176e-16, 7.704296785539652e-17, 5.923240774978013e-18], [2.0149193653262033e-08, 2.168762967640513e-08, 1.1671764366231637e-08, 4.187643231140956e-09, 1.12684479062499e-09, 2.4257638238445953e-10, 4.351627199851158e-11, 6.691262391667158e-12, 9.002694060330335e-13, 1.0766744330116857e-13, 1.1588809352393402e-14, 1.1725411412368504e-15, 1.0217866502984652e-16, 8.460018057645701e-18, 6.504256690909302e-19], [2.0281842023628514e-09, 2.183040604667547e-09, 1.1748603199046743e-09, 4.2152117810217185e-10, 1.1342631582135196e-10, 2.441733376952487e-11, 4.3802753068888935e-12, 6.735313040403936e-13, 9.061961578254931e-14, 1.0837625136273155e-14, 1.166510206670924e-15, 1.141432610220339e-16, 1.0586465501680573e-17, 8.515712971691854e-19, 6.547076223310527e-20], [1.8844951070050653e-10, 2.028380525347062e-10, 1.0916259586754566e-10, 3.916580144481569e-11, 1.0539049506545158e-11, 2.268745903906167e-12, 4.069949550711688e-13, 6.258141866010773e-14, 8.419956251603876e-15, 1.0069820836326588e-15, 1.0838674190351183e-16, 1.0605664744012343e-17, 9.512859149535941e-19, 8.144223264735153e-20, 6.0832409076276675e-21], [1.6259154178562093e-11, 1.750057698309641e-11, 9.418392598340239e-12, 3.3791693162326517e-12, 9.092941137679268e-13, 1.9574415081509913e-13, 3.5114942457535925e-14, 5.399435270091681e-15, 7.264617794054438e-16, 8.688097354019344e-17, 9.35145302829634e-18, 9.150415811537233e-19, 8.207558778810574e-20, 6.795557121209557e-21, 5.4023036152158935e-22]] |
| Legacy trial inputs | {"lambda_home": 1.2078999709456837, "lambda_away": 1.0763522376933452, "rho": -0.01984634636300814, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3836 |
| Legacy p draw | 0.2958 |
| Legacy p away | 0.3206 |
| Legacy p over 1 5 | 0.6678 |
| Legacy p under 3 5 | 0.8028 |
| Legacy p btts yes | 0.4664 |
| Legacy p over 2 5 | 0.3977 |
| Legacy goal margin distribution | {"-1": 0.19418943677386563, "-10": 6.545174524337964e-08, "-11": 6.342488615742576e-09, "-12": 5.641587274148495e-10, "-13": 4.621184373039346e-11, "-14": 3.250968125244952e-12, "-2": 0.08850909236559285, "-3": 0.028816853989022912, "-4": 0.007298946824165908, "-5": 0.001507821857365943, "-6": 0.0002625452999371366, "-7": 3.946984994011472e-05, "-8": 5.217544211940383e-06, "-9": 6.152062457237359e-07, "0": 0.2958068873930949, "1": 0.21724561134841844, "10": 2.0639551609538243e-07, "11": 2.2444776023113357e-08, "12": 2.240440647495898e-09, "13": 2.0595008768360295e-10, "14": 1.6259154178562093e-11, "2": 0.11095694524882913, "3": 0.040540558116111375, "4": 0.011523380692299034, "5": 0.002671445369536914, "6": 0.0005220078855817382, "7": 8.806733282705679e-05, "8": 1.3064477914273337e-05, "9": 1.7287142416729814e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3879 |
| Legacy raw p draw | 0.2893 |
| Legacy raw p away | 0.3228 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2079 |
| Legacy lambda away | 1.0764 |
| Legacy model home team | Vallecano |
| Legacy model away team | Celta |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 68.2% |
| Market home draw odds | 1.42 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:28:10Z |
| Market reference home draw last update utc | 2026-10-31T11:28:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.6% |
| Market draw away odds | 1.56 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:28:10Z |
| Market reference draw away last update utc | 2026-10-31T11:28:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.2% |
| Market home away odds | 1.39 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:28:10Z |
| Market reference home away last update utc | 2026-10-31T11:28:22Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.55 |
| Market reference dc home draw odds | 1.40 |
| Market reference dc home away odds | 1.36 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.35, "price": 1.58, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.58, "price": 2.35, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.85, "price": 1.99, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.99, "price": 1.85, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.52, "price": 2.5, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.5, "price": 1.52, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 71.1% |
| Market over 1 5 odds | 1.38 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:28:22Z |
| Market reference over 1 5 odds | 1.38 |
| Market reference over 1 5 opposite odds | 3.23 |
| Market reference over 1 5 last update utc | 2026-10-31T11:28:22Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 77.6% |
| Market reference under 3 5 odds | 1.24 |
| Market reference under 3 5 opposite odds | 3.55 |
| Market reference under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 52.2% |
| Market btts yes odds | 1.87 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:28:10Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-10-31T11:28:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 9.257971319589126, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.5850 |
| Elo away rating | 1,513.4884 |
| Elo rating diff | 21.0966 |
| Elo home expectancy | 0.5303 |

</details>


---

## 2026-10-31 — Real Betis vs Málaga

The model's most likely 1X2 outcome is **Real Betis win** at **75.4%**. Expected goals are 2.36 for Real Betis and 0.60 for Málaga (2.96 combined). The most likely exact score is 2-0 at 11.3%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 65.5%; Under 3.5 goals: 55.8%; Double Chance 1X: 91.2%; Double Chance X2: 24.6%; Double Chance 12 (either team wins): 84.2%; Under 4.5 goals: 74.4%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 75.4% | 1.33 |
| Draw | 15.8% | 6.34 |
| Málaga win | 8.8% | 11.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 2.36 |
| Málaga expected goals | 0.60 |
| Expected total goals | 2.96 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.5% |
| Under 2.5 | 34.5% |
| Over 3.5 | 44.2% |
| Under 3.5 | 55.8% |
| Over 4.5 | 25.6% |
| Under 4.5 | 74.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.30% |
| 2 | 3-0 | 10.39% |
| 3 | 1-0 | 8.05% |
| 4 | 2-1 | 7.90% |
| 5 | 1-1 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 75.4% | 74.9% | 1.32 | -0.4% |
| Draw | 15.8% | 15.7% | 5.92 | -6.6% |
| Málaga win | 8.8% | 9.4% | 9.72 | -14.5% |

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
| Market best home last update utc | 2026-10-31T11:28:22Z |
| Market best draw last update utc | 2026-10-31T11:28:22Z |
| Market best away last update utc | 2026-10-31T11:28:22Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Betis |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3624 |
| Dc lambda away | 0.5987 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:27:45.223690+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.19 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.80 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.90 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.06517221226843221, "-10": 3.7507037436299146e-10, "-11": 2.347624867542857e-11, "-12": 1.3498859419165765e-12, "-13": 7.177054972414795e-14, "-14": 3.5481947408823426e-15, "-15": 1.6390480538257243e-16, "-16": 7.104719116987552e-18, "-17": 2.900300431843776e-19, "-18": 1.1141847801152403e-20, "-19": 3.7188977210279044e-22, "-2": 0.018361358757958447, "-3": 0.003726601333653659, "-4": 0.0005965933440790305, "-5": 7.85116294906118e-05, "-6": 8.751029087998269e-06, "-7": 8.448368926988689e-07, "-8": 7.18750618439632e-08, "-9": 5.4628591069984025e-09, "0": 0.15774941479839338, "1": 0.18928103978289038, "10": 0.0002467786316624804, "11": 6.0952861789049975e-05, "12": 1.3830347239249376e-05, "13": 2.901702555206255e-06, "14": 5.660889494480911e-07, "15": 1.0319045457833805e-07, "16": 1.765083933819912e-08, "17": 2.8433612871987997e-09, "18": 4.3103932147356024e-10, "19": 5.677334891914362e-11, "2": 0.2054635214729069, "3": 0.1645558991662015, "4": 0.10395599380568672, "5": 0.053985326429093226, "6": 0.023744961943875938, "7": 0.009045984325299322, "8": 0.003036909160354128, "9": 0.0009108443731476616} |
| Raw goal margin distribution | {"-1": 0.05678173602701365, "-10": 9.586786524483465e-11, "-11": 5.1627497815831305e-12, "-12": 2.552691015474702e-13, "-13": 1.1665503427196036e-14, "-14": 4.95524840359011e-16, "-15": 1.9661784973070702e-17, "-16": 7.318410902001073e-19, "-17": 2.558529744631275e-20, "-18": 7.889627552755925e-22, "-2": 0.01449942706241078, "-3": 0.0026057974587833156, "-4": 0.00036529897794152074, "-5": 4.182950661674698e-05, "-6": 4.040900557164426e-06, "-7": 3.3724006245939815e-07, "-8": 2.4758078000778646e-08, "-9": 1.6217178017363495e-09, "0": 0.15918256161808864, "1": 0.22978254986007238, "10": 8.777668099620445e-05, "11": 1.8653390643535622e-05, "12": 3.6395322171279476e-06, "13": 6.563287275068513e-07, "14": 1.1001552315198085e-07, "15": 1.7225906677858665e-08, "16": 2.5301516224790088e-09, "17": 3.4905256831077293e-10, "18": 4.2474422163372904e-11, "2": 0.22578342740041654, "3": 0.16012254558546055, "4": 0.08857902518336382, "5": 0.040025410188151915, "6": 0.015258147965130676, "7": 0.005024969499931527, "8": 0.0014557332633891383, "9": 0.00037627968582244493} |
| Unadjusted home-win probability | 76.7% |
| Unadjusted draw probability | 15.9% |
| Unadjusted away-win probability | 7.4% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 41.0% |
| P home draw | 91.2% |
| P draw away | 24.6% |
| P home away | 84.2% |
| Raw p home draw | 92.6% |
| Raw p draw away | 23.3% |
| Raw p home away | 84.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1666 |
| Totals anchor target over 2 5 | 0.6552 |
| Totals anchor reference over odds | 1.49 |
| Totals anchor reference under odds | 2.73 |
| Totals anchor reference last update utc | 2026-10-31T11:28:22Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5664 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.01, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.93, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:12Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 8.03, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:12Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.11, "price": 8.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.75, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.32 |
| Reference draw odds | 5.92 |
| Reference away odds | 9.72 |
| Market reference 1x2 last update utc | 2026-10-31T11:28:22Z |
| Market reference home last update utc | 2026-10-31T11:28:22Z |
| Market reference draw last update utc | 2026-10-31T11:28:22Z |
| Market reference away last update utc | 2026-10-31T11:28:22Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Market reference over 2 5 last update utc | 2026-10-31T11:26:29Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:26:29Z |
| Home probability edge | +0.5% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.0174 |
| Raw ev home | 0.0118 |
| Raw edge prob draw | 0.0020 |
| Raw ev draw | -0.0576 |
| Raw edge prob away | -0.0195 |
| Raw ev away | -0.2778 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.059399487775020014, 0.03587220735202122, 0.01050052114079871, 0.0019570181545696935, 0.0002735521413147722, 3.0589710716036094e-05, 2.850554673030454e-06, 2.2768613797811726e-07, 1.5912992540761503e-08, 9.885863402469089e-10, 5.527386848560674e-11, 2.8095219617071804e-12, 1.3090506202021235e-13, 5.63012897821992e-15, 2.2485138339879113e-16, 8.381264767551758e-18, 2.928834511238822e-19, 9.632769482192162e-21], [0.13190625565691555, 0.07484563559550562, 0.023786825943529544, 0.004433232368839917, 0.0006196775459698127, 6.929485829404505e-05, 6.457360252953369e-06, 5.157773086896494e-07, 3.604769503649475e-08, 2.239444203796482e-09, 1.2521187008368447e-10, 6.364408869955292e-12, 2.96539179689217e-13, 1.2753928709709009e-14, 5.093557403820478e-16, 1.8986075408941644e-17, 6.634687536178902e-19, 2.182110849115622e-20], [0.15108005062540106, 0.0844719222701537, 0.023238208378713016, 0.005021299672217752, 0.0007018776368072846, 7.848680607944657e-05, 7.313927677116429e-06, 5.841950557936592e-07, 4.082941389294287e-08, 2.5365059872590838e-09, 1.4182119724382978e-10, 7.208646313508915e-12, 3.358750369683034e-13, 1.444573456146371e-14, 5.769216678556111e-16, 2.150457415625324e-17, 7.514777385648317e-19, 2.47156737562897e-20], [0.11408052418157394, 0.06378473618001358, 0.017831670211641042, 0.003270325862782889, 0.000529987701134892, 5.9265375817761374e-05, 5.522745721739122e-06, 4.4112560138379657e-07, 3.083028447271541e-08, 1.9153153008512823e-09, 1.0708916534420537e-10, 5.443247779441791e-12, 2.5361919140373513e-13, 1.0907972059433405e-14, 4.3563346721311245e-16, 1.623810080743005e-17, 5.674407307343474e-19, 1.866280164685254e-20], [0.06460664037212022, 0.03612288373652394, 0.010098518681103832, 0.0018820955767989763, 0.0002588820523252255, 3.3563457473971726e-05, 3.1276683664528225e-06, 2.498204079267495e-07, 1.7459957479934207e-08, 1.0846907281418736e-09, 6.064725984368406e-11, 3.082646702981566e-12, 1.436308608155536e-13, 6.177456082786617e-15, 2.4671007564359775e-16, 9.196040662664794e-18, 3.213558097322314e-19, 1.0569209100190686e-20], [0.029270678830535437, 0.01636583054302944, 0.00457523398951277, 0.0008527020572428234, 0.00011919075616014116, 1.3115740965891919e-05, 1.4170211562706823e-06, 1.1318361214295186e-07, 7.910406807200261e-09, 4.914298863248329e-10, 2.7476842234974855e-11, 1.3966236453601437e-12, 6.507338522588829e-14, 2.7987577120170654e-15, 1.1177444527106378e-16, 4.166357377492772e-18, 1.4559343502185745e-19, 4.788484949574252e-21], [0.011051142656873588, 0.0061789181274662245, 0.0017273792589304843, 0.0003219375994987013, 4.500046129207792e-05, 5.032134226391843e-06, 4.6144636229366683e-07, 4.273246450667063e-08, 2.986573512913465e-09, 1.8553931772710978e-10, 1.0373879781098397e-11, 5.272951554077586e-13, 2.4568451844265845e-14, 1.0566707699740746e-15, 4.2200433657002404e-17, 1.5730079238940594e-18, 5.496879076997374e-20, 1.8078921433428603e-21], [0.003576306946121878, 0.001999585789893999, 0.0005590044970107762, 0.00010418358617322647, 1.4562789323640515e-05, 1.6284702085959735e-06, 1.5175179020475746e-07, 1.1927681759636131e-08, 9.664976673423662e-10, 6.004316217504121e-11, 3.3571350466912977e-12, 1.706402121022546e-13, 7.950700458242565e-15, 3.419536903789571e-16, 1.3656660555641537e-17, 5.090477373421739e-19, 1.7788682524001728e-20, 5.850596115556233e-22], [0.0010126758199351395, 0.0005662076018132005, 0.00015828908029599708, 2.9500879018833496e-05, 4.123635034977161e-06, 4.6112160633140317e-07, 4.2970407989972035e-08, 3.4322324476518607e-09, 2.3605160945560505e-10, 1.7001968623818525e-11, 9.506145689557498e-13, 4.8318899721944554e-14, 2.2513397834434907e-15, 9.682844314016998e-17, 3.867053397292164e-18, 1.4414320206997848e-19, 5.037086841803044e-21, 1.6566691024256227e-22], [0.00025489045462097695, 0.00014251442583596333, 3.9841353811298815e-05, 7.425369814113388e-06, 1.0379187377295498e-06, 1.1606428588459288e-07, 1.0815649600989131e-08, 8.638927401296931e-10, 6.037749531780037e-11, 3.6910747773354425e-12, 2.3926964076813273e-13, 1.2161864709775208e-14, 5.666621139872355e-16, 2.437171442863137e-17, 9.733371520044038e-19, 3.628083694986748e-20, 1.267834513077197e-21, 4.169835324999056e-23], [5.774032352717221e-05, 3.228378664589072e-05, 9.025260134773232e-06, 1.682068698937151e-06, 2.3511968622180924e-07, 2.6292037600591544e-08, 2.4500686306447835e-09, 1.9569758460369842e-10, 1.3677311371248228e-11, 8.496958166909735e-13, 4.675022875325783e-14, 2.7550266803060066e-15, 1.2836594387525405e-16, 5.520923402618523e-18, 2.2049002243462383e-19, 8.218696406018843e-21, 2.8720249674648884e-22, 9.445926136327826e-24], [1.1890829964511292e-05, 6.64840434148581e-06, 1.8586288938538373e-06, 3.463990443052501e-07, 4.841968384290594e-08, 5.414485569725774e-09, 5.045581269504005e-10, 4.0301241157629933e-11, 2.8166552238082754e-12, 1.749832328714653e-13, 9.783667654671414e-15, 4.89360900386659e-16, 2.6435210587906426e-17, 1.1369586697368312e-18, 4.5406904663559536e-20, 1.6925281246115705e-21, 5.914542637760758e-23, 1.9452593037784123e-24], [2.2446909927718607e-06, 1.2550522870294768e-06, 3.5086260163427576e-07, 6.539146695204911e-08, 9.140424051089286e-09, 1.0221193159039656e-09, 9.524794200872698e-11, 7.60786532933797e-12, 5.31713987122521e-13, 3.303245340190367e-14, 1.846911504601346e-15, 9.387688207237255e-17, 4.304251813134647e-18, 2.1462933140319551e-19, 8.571686771414674e-21, 3.1950693497994084e-22, 1.1165175706801343e-23, 3.6721625410750073e-25], [3.9114596332978876e-07, 2.1869764587650432e-07, 6.113914599138901e-08, 1.1394712420047958e-08, 1.5927537385852817e-09, 1.7810818760561353e-10, 1.659731702588512e-11, 1.3256995384707928e-12, 9.265318940498785e-14, 5.756030940846364e-15, 3.218313709897732e-16, 1.635840460483691e-17, 7.621929988568953e-19, 3.225832871440293e-20, 1.4936490993025338e-21, 5.567530153402226e-23, 1.945574433918098e-24, 6.398883228281981e-26], [6.329019853588579e-08, 3.538683439047694e-08, 9.892748617852917e-09, 1.8437455040693136e-09, 2.577188819122339e-10, 2.8819171386723047e-11, 2.6855639280767366e-12, 2.1450761315413712e-13, 1.4991944957081238e-14, 9.313667407522583e-16, 5.207460455841504e-17, 2.6469061993043148e-18, 1.2332824761799418e-19, 5.304255847951391e-21, 2.084570983995858e-22, 9.00865972803769e-24, 3.1480777953267526e-25, 1.0353848125602615e-26], [9.558083935822817e-09, 5.344118696917377e-09, 1.4940026075573123e-09, 2.784423922165187e-10, 3.8920698025095324e-11, 4.3522704217617125e-12, 4.055737860424177e-13, 3.239493347832896e-14, 2.264083089892184e-15, 1.4065497800731817e-16, 7.864305260662054e-18, 3.9973569697139715e-19, 1.8625028356047186e-20, 8.010485633577556e-22, 3.1991607712254064e-23, 1.1734512903349643e-24, 4.754226167764703e-26, 1.5636378417609035e-27], [1.3532452097287642e-09, 7.566268590424134e-10, 2.1152271580519147e-10, 3.942221432479861e-11, 5.510440012392079e-12, 6.161997675725796e-13, 5.742163249858644e-14, 4.58651428920066e-15, 3.2055165202530123e-16, 1.9914103756667037e-17, 1.1134379540180812e-18, 5.65950687100306e-20, 2.636954286352323e-21, 1.1341343499414172e-22, 4.529410934117595e-24, 1.6883237143600155e-25, 5.805718816180428e-27, 2.2138175740255304e-28], [1.8032386948236392e-10, 1.0082273485687184e-10, 2.8186018559825948e-11, 5.2531249913203815e-12, 7.342821969302582e-13, 8.211041551375017e-14, 7.651599938945844e-15, 6.111664006781056e-16, 4.271444217692981e-17, 2.6536123836678748e-18, 1.4836885351865365e-19, 7.54145790433538e-21, 3.513818465010223e-22, 1.5112670861424494e-23, 6.035572121326921e-25, 2.2497405712099754e-26, 7.861722555053772e-28, 2.544421472911796e-29]] |
| Legacy trial inputs | {"lambda_home": 2.265299562238701, "lambda_away": 0.5591202936488258, "rho": -0.01984634636300814, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7550 |
| Legacy p draw | 0.1610 |
| Legacy p away | 0.0840 |
| Legacy p over 1 5 | 0.7728 |
| Legacy p under 3 5 | 0.6879 |
| Legacy p btts yes | 0.3851 |
| Legacy p over 2 5 | 0.5364 |
| Legacy goal margin distribution | {"-1": 0.06524534486373985, "-10": 6.198531129657664e-11, "-11": 3.1209518528670635e-12, "-12": 1.4425247664287908e-13, "-13": 6.161567302698055e-15, "-14": 2.4460759934794447e-16, "-15": 9.069449194925938e-18, "-16": 3.147045596150384e-19, "-17": 9.632769482192162e-21, "-2": 0.015698140421821848, "-3": 0.00266096317210077, "-4": 0.0003506200148214797, "-5": 3.766320901216988e-05, "-6": 3.4091387797116964e-06, "-7": 2.663805769577764e-07, "-8": 1.8299847661914343e-08, "-9": 1.1212667666569964e-09, "0": 0.16102612901914665, "1": 0.23621632185115554, "10": 6.475124731189747e-05, "11": 1.3208904687585618e-05, "12": 2.4735654222088623e-06, "13": 4.2806695682434476e-07, "14": 6.885109307359968e-08, "15": 1.0342896813425056e-08, "16": 1.454067944585636e-09, "17": 1.8032386948236392e-10, "2": 0.22586268032341683, "3": 0.15511561443223656, "4": 0.08280827595048162, "5": 0.03603916705706618, "6": 0.013216683527638265, "7": 0.004184087429062581, "8": 0.001164571226200702, "9": 0.0002890998836107865} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7609 |
| Legacy raw p draw | 0.1649 |
| Legacy raw p away | 0.0742 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2653 |
| Legacy lambda away | 0.5591 |
| Legacy model home team | Betis |
| Legacy model away team | Malaga |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 89.1% |
| Market home draw odds | 1.09 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:28:12Z |
| Market reference home draw last update utc | 2026-10-31T11:28:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 27.2% |
| Market draw away odds | 3.74 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:28:12Z |
| Market reference draw away last update utc | 2026-10-31T11:28:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.6% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:28:12Z |
| Market reference home away last update utc | 2026-10-31T11:28:22Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.50 |
| Market reference dc home draw odds | 1.07 |
| Market reference dc home away odds | 1.14 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:12Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.77, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:12Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.77, "price": 2.07, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:12Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.67, "price": 2.21, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:12Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.21, "price": 1.67, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 85.9% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-31T11:28:22Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.0% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market reference under 3 5 odds | 1.71 |
| Market reference under 3 5 opposite odds | 2.24 |
| Market reference under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.7% |
| Market btts yes odds | 1.87 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:28:12Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-31T11:28:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 10.079740328079192, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,565.5196 |
| Elo away rating | 1,404.7246 |
| Elo rating diff | 220.7950 |
| Elo home expectancy | 0.7809 |

</details>


---

## 2026-11-01 — Athletic Bilbao vs Real Sociedad

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **46.2%**. Expected goals are 1.55 for Athletic Bilbao and 1.04 for Real Sociedad (2.59 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.2%; Under 3.5 goals: 64.6%; Double Chance 1X: 72.1%; Double Chance X2: 53.8%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 81.7%; BTTS Yes (both teams score): 59.7%; BTTS No (at least one team does not score): 40.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 46.2% | 2.16 |
| Draw | 25.9% | 3.86 |
| Real Sociedad win | 27.9% | 3.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.55 |
| Real Sociedad expected goals | 1.04 |
| Expected total goals | 2.59 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 57.2% |
| Under 2.5 | 42.8% |
| Over 3.5 | 35.4% |
| Under 3.5 | 64.6% |
| Over 4.5 | 18.3% |
| Under 4.5 | 81.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.04% |
| 2 | 2-1 | 8.77% |
| 3 | 1-0 | 7.74% |
| 4 | 2-0 | 7.21% |
| 5 | 1-2 | 7.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 46.2% | 45.2% | 2.16 | -0.2% |
| Draw | 25.9% | 25.8% | 3.71 | -3.8% |
| Real Sociedad win | 27.9% | 29.0% | 3.32 | -7.5% |

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
| Market best home last update utc | 2026-10-31T11:28:22Z |
| Market best draw last update utc | 2026-10-31T11:28:22Z |
| Market best away last update utc | 2026-10-31T11:28:22Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5457 |
| Dc lambda away | 1.0423 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:27:45.223690+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.7% |
| P btts no | 40.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.67 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.10 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.83 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.45 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.16454385652244177, "-10": 1.2690505661263482e-07, "-11": 1.38026987745396e-08, "-12": 1.3795176132026398e-09, "-13": 1.2751617372672855e-10, "-14": 1.0958263303233778e-11, "-15": 8.736374108409367e-13, "-16": 5.83936656581248e-14, "-2": 0.07760225189141848, "-3": 0.026982609232970387, "-4": 0.007440078233927229, "-5": 0.0016917024656670616, "-6": 0.00032643442088703075, "-7": 5.4629237144707214e-05, "-8": 8.063826256724358e-06, "-9": 1.064090595198943e-06, "0": 0.25926496288563033, "1": 0.2037228844801237, "10": 5.41836199209323e-06, "11": 8.739704628274216e-07, "12": 1.295399278569169e-07, "13": 1.7757643374943344e-08, "14": 2.263108858177488e-09, "15": 2.6757072307894273e-10, "16": 2.6522640831877927e-11, "2": 0.1416166004086072, "3": 0.07302430639723008, "4": 0.029861021146352404, "5": 0.010069195918955469, "6": 0.002881445512294923, "7": 0.0007151271341945671, "8": 0.0001565463473562721, "9": 3.0635434038445275e-05} |
| Raw goal margin distribution | {"-1": 0.1576678985945468, "-10": 3.6255250730974236e-08, "-11": 3.394291142384575e-09, "-12": 2.9182890903274335e-10, "-13": 2.3189582296395416e-11, "-14": 1.7051111788306351e-12, "-15": 1.0698953229305029e-13, "-2": 0.06768141576443631, "-3": 0.020907195648724643, "-4": 0.005060254155053479, "-5": 0.0010029227828670735, "-6": 0.0001679556442415049, "-7": 2.432351646817667e-05, "-8": 3.1008226959908776e-06, "-9": 3.5287776780100514e-07, "0": 0.2611400760122736, "1": 0.235372771597264, "10": 1.8655524910645212e-06, "11": 2.5901761922404174e-07, "12": 3.302571159693286e-08, "13": 3.891889081615117e-09, "14": 4.2438877285798576e-10, "15": 3.949081798901886e-11, "2": 0.14885271034845782, "3": 0.06819095166952441, "4": 0.024476366881102586, "5": 0.007194254170808744, "6": 0.0017867201668352426, "7": 0.000383735478182757, "8": 7.254812329780447e-05, "9": 1.2243827488192217e-05} |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 25.3% |
| Raw p over 1 5 | 73.3% |
| Raw p under 3 5 | 73.9% |
| Raw p btts yes | 51.3% |
| P home draw | 72.1% |
| P draw away | 53.8% |
| P home away | 74.1% |
| Raw p home draw | 74.7% |
| Raw p draw away | 51.4% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1667 |
| Totals anchor target over 2 5 | 0.5721 |
| Totals anchor reference over odds | 1.70 |
| Totals anchor reference under odds | 2.24 |
| Totals anchor reference last update utc | 2026-10-31T11:28:22Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4781 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.05, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.08, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.23, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.29, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 6.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.2, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.57, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.2, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.16 |
| Reference draw odds | 3.71 |
| Reference away odds | 3.32 |
| Market reference 1x2 last update utc | 2026-10-31T11:28:22Z |
| Market reference home last update utc | 2026-10-31T11:28:22Z |
| Market reference draw last update utc | 2026-10-31T11:28:22Z |
| Market reference away last update utc | 2026-10-31T11:28:22Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-31T11:27:35Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:27:35Z |
| Home probability edge | +1.0% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +1.4% |
| Under 2.5 probability edge | -1.4% |
| Raw edge prob home | 0.0347 |
| Raw ev home | 0.0505 |
| Raw edge prob draw | 0.0027 |
| Raw ev draw | -0.0312 |
| Raw edge prob away | -0.0373 |
| Raw ev away | -0.1616 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10526524387041813, 0.10171308136732866, 0.04666990375098548, 0.013898254081512781, 0.0031041653880131688, 0.0005546505452915194, 8.258720915776871e-05, 1.0540454718025607e-05, 1.1771016171426109e-06, 1.1684659020009313e-07, 1.0439041879050404e-08, 8.478373626164405e-10, 6.312129519441209e-11, 4.337876124359672e-12, 2.7681760485374347e-13], [0.1390488662376115, 0.12491116632233286, 0.062218591232509314, 0.018528638802366038, 0.004138358596696629, 0.0007394396127001385, 0.00011010221565996818, 1.4052144761317649e-05, 1.569268382186781e-06, 1.5577555658487102e-07, 1.3916944911590225e-08, 1.130305444333966e-09, 8.415097842760715e-11, 5.783096164904711e-12, 3.6904300240802755e-13], [0.09436047990539001, 0.08430139037629142, 0.036469884889142386, 0.01235084830997622, 0.0027585533845885793, 0.0004928967847158186, 7.339210282597266e-05, 9.366900085218284e-06, 1.0460453114103415e-06, 1.0383710807380931e-07, 9.276778363200488e-09, 7.534407268561151e-10, 5.609348753469887e-11, 3.854905061111259e-12, 2.459972473540635e-13], [0.04193263506650435, 0.03746249957389235, 0.01673444647704654, 0.004826360387630023, 0.0012258671480200461, 0.000219037260298643, 3.261454655222755e-05, 4.162535029195319e-06, 4.648496526339966e-07, 4.6143931904393615e-08, 4.122486045926834e-09, 3.3481977916153627e-10, 2.492725497749064e-11, 1.7130723297049024e-12, 1.0931814686620011e-13], [0.013975759915991518, 0.012485905049069466, 0.00557743642676614, 0.0016609553985001244, 0.00035927552273405335, 7.300309550628886e-05, 1.0870127089794152e-05, 1.3873344739169083e-06, 1.5493009518579657e-07, 1.5379346250310124e-08, 1.37398651774501e-09, 1.1159233950515046e-10, 8.308023819099229e-12, 5.709511830275689e-13, 3.643472852683943e-14], [0.003726393343412041, 0.003329149451693793, 0.0014871264316886105, 0.0004428648730286985, 9.891356154232129e-05, 1.7116520557118017e-05, 2.8983303571996204e-06, 3.6990861175102277e-07, 4.1309415650017424e-08, 4.1006352311196465e-09, 3.6634961135847857e-10, 2.975415674048286e-11, 2.2151900749937606e-12, 1.5223420412457906e-13, 9.714686762476983e-15], [0.0008279816525955509, 0.0007397165062094748, 0.0003304303349255713, 9.840184748480402e-05, 2.197798423365933e-05, 3.927014000826122e-06, 5.662925523486071e-07, 8.21914155166715e-08, 9.178697760966868e-09, 9.111358953440893e-10, 8.140062754689998e-11, 6.6111903922129694e-12, 4.922015928214342e-13, 3.3825502650029806e-14, 2.1585435725040168e-15], [0.00015769064934294678, 0.00014088038766101374, 6.293107330782018e-05, 1.8740815304036777e-05, 4.185748070854546e-06, 7.479071375892008e-07, 1.1136302619192945e-07, 1.3764886499999214e-08, 1.7481001004215904e-09, 1.7352752989885352e-10, 1.5502901271490072e-11, 1.2591135354386426e-12, 9.374071096422954e-14, 6.442130040579873e-15, 4.1109864755598754e-16], [2.6278418381274776e-05, 2.3477065914167908e-05, 1.0487172704635332e-05, 3.123070311509903e-06, 6.975355831360169e-07, 1.246352700924415e-07, 1.8558133958291535e-08, 2.3685407538683573e-09, 2.5616543292836e-10, 2.891756137952135e-11, 2.583486893061201e-12, 2.0982545516585284e-13, 1.5621456518444843e-14, 1.0735512167545563e-15, 6.850769085843494e-17], [3.89260182232983e-06, 3.4776396446129768e-06, 1.553456794425648e-06, 4.6261799357415903e-07, 1.0332540728516414e-07, 1.846212631404468e-08, 2.7490020524432473e-09, 3.5085011285687515e-10, 3.918106441008021e-11, 3.7667202890630265e-12, 3.8268991847169973e-13, 3.108128264415596e-14, 2.313994291013901e-15, 1.5902431272960312e-16, 1.0147991344455338e-17], [5.189472918279733e-07, 4.636260675758841e-07, 2.071011198254139e-07, 6.167452153441921e-08, 1.3774961512905254e-08, 2.4613024628152256e-09, 3.6648679609647607e-10, 4.677404065839916e-11, 5.223474733508371e-12, 5.185153114379313e-13, 4.486330210448677e-14, 4.143641757088462e-15, 3.084931686920699e-16, 2.1200533779855908e-17, 1.3528927093156423e-18], [6.289466858310937e-08, 5.618992203227774e-08, 2.509996005322269e-08, 7.4747448402043e-09, 1.6694790641405984e-09, 2.983015907767187e-10, 4.441696862773946e-11, 5.668856609965878e-12, 6.330675916219237e-13, 6.284231401089379e-14, 5.614314860303329e-15, 4.416047443210333e-16, 3.7388335791667987e-17, 2.56943347978982e-18, 1.6396605189167993e-19], [6.9874040169374575e-09, 6.24252732011661e-09, 2.788528275160639e-09, 8.304211358234646e-10, 1.8547398343556546e-10, 3.314038821744965e-11, 4.934588447660572e-12, 6.297925140598583e-13, 7.033186011381418e-14, 6.981587585172326e-15, 6.237330936150349e-16, 5.0658310139404235e-17, 3.6525746712993285e-18, 2.85456147912011e-19, 1.821612348772249e-20], [7.165652962690113e-10, 6.401774432627306e-10, 2.859663738924291e-10, 8.516052110010916e-11, 1.902054319008032e-11, 3.3985800798041094e-12, 5.060469989129566e-13, 6.458585453644697e-14, 7.212602857576684e-15, 7.1596881535265e-16, 6.396445488705806e-17, 5.195060558333043e-18, 3.867710548204952e-19, 2.574188011115411e-20, 1.868081749990727e-21], [6.823559828352681e-11, 6.096149377606982e-11, 2.7231414517449726e-11, 8.109490004133988e-12, 1.8112489552739182e-12, 3.23632956085622e-13, 4.818879718317462e-14, 6.1502482019347e-15, 6.868268303401843e-16, 6.817879783225663e-17, 6.091074841083985e-18, 4.947044842427408e-19, 3.683063422390382e-20, 2.5311066313328773e-21, 1.5642712258755588e-22]] |
| Legacy trial inputs | {"lambda_home": 1.3331630500994018, "lambda_away": 0.8933972194801862, "rho": -0.01984634636300814, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4591 |
| Legacy p draw | 0.2718 |
| Legacy p away | 0.2690 |
| Legacy p over 1 5 | 0.6540 |
| Legacy p under 3 5 | 0.8143 |
| Legacy p btts yes | 0.4346 |
| Legacy p over 2 5 | 0.3880 |
| Legacy goal margin distribution | {"-1": 0.1775843734525178, "-10": 1.16271903179773e-08, "-11": 9.35952564252025e-10, "-12": 6.915038860667086e-11, "-13": 4.706919126767699e-12, "-14": 2.7681760485374347e-13, "-2": 0.06818738258878045, "-3": 0.01856355358021798, "-4": 0.003921318751974415, "-5": 0.0006746002630912164, "-6": 9.773294740178782e-05, "-7": 1.2217796536098307e-05, "-8": 1.3424972342864106e-06, "-9": 1.3154248375938675e-07, "0": 0.2718496278302308, "1": 0.24184861283626494, "10": 5.780127139054671e-07, "11": 6.943127176712255e-08, "12": 7.654812874717638e-09, "13": 7.775267900450812e-10, "14": 6.823559828352681e-11, "2": 0.13786602558471944, "3": 0.056008381574504384, "4": 0.017654796887851074, "5": 0.004532269825004637, "6": 0.0009798259092177388, "7": 0.00018278454970472436, "8": 2.997082281130568e-05, "9": 4.3821776152709065e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4665 |
| Legacy raw p draw | 0.2852 |
| Legacy raw p away | 0.2482 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3332 |
| Legacy lambda away | 0.8934 |
| Legacy model home team | Ath Bilbao |
| Legacy model away team | Sociedad |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 69.8% |
| Market home draw odds | 1.36 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:28:10Z |
| Market reference home draw last update utc | 2026-10-31T11:28:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.1% |
| Market draw away odds | 1.75 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:28:10Z |
| Market reference draw away last update utc | 2026-10-31T11:28:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:28:10Z |
| Market reference home away last update utc | 2026-10-31T11:28:22Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.69 |
| Market reference dc home draw odds | 1.36 |
| Market reference dc home away odds | 1.28 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.11, "price": 1.72, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.72, "price": 2.11, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.69, "price": 2.16, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.16, "price": 1.69, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 81.1% |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-31T11:28:22Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.8% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.74 |
| Market reference under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:28:10Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-31T11:28:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 10.303234661826316, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,505.1233 |
| Elo away rating | 1,510.6645 |
| Elo rating diff | 54.4588 |
| Elo home expectancy | 0.5777 |

</details>


---

## 2026-11-01 — Elche CF vs Valencia

The model's most likely 1X2 outcome is **Elche CF win** at **42.6%**. Expected goals are 1.49 for Elche CF and 1.07 for Valencia (2.56 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 47.4%; Under 3.5 goals: 73.9%; Double Chance 1X: 70.4%; Double Chance X2: 57.4%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 52.3%; BTTS No (at least one team does not score): 47.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 42.6% | 2.35 |
| Draw | 27.7% | 3.61 |
| Valencia win | 29.6% | 3.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elche CF expected goals | 1.49 |
| Valencia expected goals | 1.07 |
| Expected total goals | 2.56 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 73.3% |
| Under 1.5 | 26.7% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 26.1% |
| Under 3.5 | 73.9% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.21% |
| 2 | 1-0 | 9.98% |
| 3 | 0-1 | 8.57% |
| 4 | 2-1 | 8.42% |
| 5 | 0-0 | 8.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 42.6% | 40.9% | 2.38 | +1.5% |
| Draw | 27.7% | 28.2% | 3.41 | -5.4% |
| Valencia win | 29.6% | 30.8% | 3.13 | -7.2% |
| Over 2.5 | 47.4% | 47.4% | 2.04 | -3.2% |
| Under 2.5 | 52.6% | 52.6% | 1.85 | -2.8% |

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
| Market best home last update utc | 2026-10-31T11:28:22Z |
| Market best draw last update utc | 2026-10-31T11:28:22Z |
| Market best away last update utc | 2026-10-31T11:28:22Z |
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
| Dc lambda home | 1.4934 |
| Dc lambda away | 1.0692 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:27:45.223690+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.3% |
| P btts no | 47.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.20 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.74 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.84 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.36 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.18164049415708952, "-10": 5.837195269578007e-08, "-11": 5.67654430940715e-09, "-12": 5.069644157944287e-10, "-13": 4.184684387251141e-11, "-14": 3.195867250300306e-12, "-15": 2.080013879584687e-13, "-2": 0.08072393509107184, "-3": 0.025862621240768643, "-4": 0.006496037584457423, "-5": 0.0013365607743069743, "-6": 0.00023240778419583645, "-7": 3.495234096174819e-05, "-8": 4.627658972598956e-06, "-9": 5.469811618382141e-07, "0": 0.2773422862231797, "1": 0.21034915826622377, "10": 1.359924058264901e-06, "11": 1.847166539080189e-07, "12": 2.3041517775842154e-08, "13": 2.6564882579203256e-09, "14": 2.8336454444435784e-10, "15": 2.5759331974353558e-11, "2": 0.12984345843021866, "3": 0.05810344399000677, "4": 0.02038400185896711, "5": 0.00585789007994301, "6": 0.0014227046882317011, "7": 0.0002988490960032537, "8": 5.526480101769241e-05, "9": 9.123704667632273e-06} |
| Raw goal margin distribution | {"-1": 0.16503742346940442, "-10": 4.794255845296431e-08, "-11": 4.60506681766305e-09, "-12": 4.0620475089820985e-10, "-13": 3.311585740646328e-11, "-14": 2.4983356347285717e-12, "-15": 1.6095426661660818e-13, "-2": 0.07274674273939652, "-3": 0.02307425628284164, "-4": 0.005732649532406084, "-5": 0.0011660681937373657, "-6": 0.00020039021449615375, "-7": 2.9778462174107848e-05, "-8": 3.895158714635968e-06, "-9": 4.548092668587828e-07, "0": 0.2655317976572104, "1": 0.2318064273191371, "10": 1.3546810717502067e-06, "11": 1.8174537919023623e-07, "12": 2.2391543217158948e-08, "13": 2.5496855169035296e-09, "14": 2.6866616817136057e-10, "15": 2.4175545255070614e-11, "2": 0.1419177521339752, "3": 0.06287275179768409, "4": 0.0218173367163527, "5": 0.0061984325205402604, "6": 0.0014878050342610346, "7": 0.0003088043187177777, "8": 5.6418020385020055e-05, "9": 9.200969172067055e-06} |
| Unadjusted home-win probability | 46.6% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 26.8% |
| Raw p over 1 5 | 72.9% |
| Raw p under 3 5 | 74.4% |
| Raw p btts yes | 51.2% |
| P home draw | 70.4% |
| P draw away | 57.4% |
| P home away | 72.3% |
| Raw p home draw | 73.2% |
| Raw p draw away | 53.4% |
| Raw p home away | 73.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0127 |
| Totals anchor target over 2 5 | 0.4745 |
| Totals anchor reference over odds | 2.04 |
| Totals anchor reference under odds | 1.85 |
| Totals anchor reference last update utc | 2026-10-31T11:28:22Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4670 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.25, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.25, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.38 |
| Reference draw odds | 3.41 |
| Reference away odds | 3.13 |
| Market reference 1x2 last update utc | 2026-10-31T11:28:22Z |
| Market reference home last update utc | 2026-10-31T11:28:22Z |
| Market reference draw last update utc | 2026-10-31T11:28:22Z |
| Market reference away last update utc | 2026-10-31T11:28:22Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-31T11:28:22Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:28:22Z |
| Market best over 2 5 last update utc | 2026-10-31T11:28:22Z |
| Market best under 2 5 last update utc | 2026-10-31T11:28:22Z |
| Home probability edge | +1.7% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0574 |
| Raw ev home | 0.1102 |
| Raw edge prob draw | -0.0169 |
| Raw ev draw | -0.0945 |
| Raw edge prob away | -0.0405 |
| Raw ev away | -0.1612 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09335960635909536, 0.0974291038222713, 0.05710472995725588, 0.021755857854706268, 0.006216437999292778, 0.001421009519629368, 0.00027068932067782914, 4.419757763770399e-05, 6.314425818981918e-06, 8.018935889355503e-07, 9.165203801090035e-08, 9.523022854284893e-09, 9.070243906241277e-10, 7.974454761092494e-11, 6.510260222663625e-12], [0.11451150782336894, 0.13318721434422084, 0.0718857560426677, 0.027387158496555545, 0.007825504924128427, 0.0017888245638994682, 0.000340754723543341, 5.563770787672123e-05, 7.948855975899425e-06, 1.009456256067554e-06, 1.153753121711022e-07, 1.1987968390784582e-08, 1.1417991840248708e-09, 1.003856790774205e-10, 8.195380286203702e-12], [0.07374873471402081, 0.08429075790763688, 0.04697469269658471, 0.017238034361242178, 0.00492553189821286, 0.0011259225487964106, 0.00021447795082262555, 3.501950449807702e-05, 5.003171558026099e-06, 6.353722906467968e-07, 7.26195671557032e-08, 7.545471030440043e-09, 7.186716201439607e-10, 6.318478733494174e-11, 5.158338970974074e-12], [0.030945968667719773, 0.0353695444851093, 0.020212724483061155, 0.007509613507038332, 0.002066819944572839, 0.00047245236209739, 8.999785517421047e-05, 1.4694658737657397e-05, 2.099398598149334e-06, 2.6661082491704123e-07, 3.047215465564481e-08, 3.1661819148036503e-09, 3.0156435260341137e-10, 2.651319316495213e-11, 2.164508947743254e-12], [0.0097390109182588, 0.011131155195462856, 0.006361149865495368, 0.0024234817740980603, 0.0006752953373534444, 0.00014868556102505344, 2.8323239888618853e-05, 4.624558482003966e-06, 6.607020800897143e-07, 8.390513681032471e-08, 9.589896832144072e-09, 9.96429634132968e-10, 9.490536729024211e-11, 8.343971406547652e-12, 6.81192968980463e-13], [0.002451972589629146, 0.002802470154234374, 0.0016015348211054648, 0.0006101554799998787, 0.00017434356009673343, 3.886421412011338e-05, 7.130889208285292e-06, 1.1643164518638826e-06, 1.6634372873057403e-07, 2.112463958760834e-08, 2.4144304146639825e-09, 2.508692279836821e-10, 2.3894147070734027e-11, 2.1007460972394124e-12, 1.7150268155637442e-13], [0.0005144404661789102, 0.0005879772305345662, 0.00033601285897566437, 0.00012801475469194747, 3.657846042439636e-05, 8.361434712670937e-06, 1.55325777851258e-06, 2.442814821054844e-07, 3.490004158938722e-08, 4.432092545926198e-09, 5.065638634500966e-10, 5.2634064157050085e-11, 5.013153984676069e-12, 4.407507678341639e-13, 3.598242485416146e-14], [9.251408240336755e-05, 0.00010573852084579402, 6.0426664245061116e-05, 2.3021454071031303e-05, 6.578064760391615e-06, 1.5036734294331241e-06, 2.8643603966897873e-07, 4.5608270619049576e-08, 6.276227349422086e-09, 7.970426161432026e-10, 9.109759843326977e-11, 9.465414306960849e-12, 9.015374398595582e-13, 7.926214117179605e-14, 6.470877073020085e-15], [1.455756108806078e-05, 1.6638493692910516e-05, 9.508442749935282e-06, 3.6225428093617947e-06, 1.0350919244174991e-06, 2.366106568514131e-07, 4.507216671211966e-08, 7.359287697682742e-09, 1.0253208259297245e-09, 1.2541870678349933e-10, 1.433467013579418e-11, 1.4894310511193196e-12, 1.418614984117457e-13, 1.2472300779550482e-14, 1.0182253970060767e-15], [2.0361833146763553e-06, 2.327245823246977e-06, 1.3299571513975806e-06, 5.066893541097877e-07, 1.4477953366678339e-07, 3.309501286933212e-08, 6.3042973517588385e-09, 1.0293522882905316e-09, 1.470616493801923e-10, 1.8212556311220828e-11, 2.005007293140042e-12, 2.0832848554125617e-13, 1.9842335835903508e-14, 1.7445154850680136e-15, 1.4242039249719304e-16], [2.563230351085411e-07, 2.9296316719556085e-07, 1.6742041404298715e-07, 6.378411617779635e-08, 1.8225436395429694e-08, 4.1661347897705285e-09, 7.936105849518815e-10, 1.2957905156613496e-10, 1.851271840089237e-11, 2.3510023911941843e-12, 2.620396769389509e-13, 2.622523685790454e-14, 2.497833917232628e-15, 2.196067027479579e-16, 1.7928458112344695e-17], [2.9333623555623906e-08, 3.352672247556238e-08, 1.9159602253399e-08, 7.2994580919946115e-09, 2.0857200373509755e-09, 4.767727159338902e-10, 9.082084307748301e-11, 1.482903445539423e-11, 2.1185966073361052e-12, 2.690488550607986e-13, 3.0750808125993646e-14, 3.115859259603296e-15, 2.8585226373253826e-16, 2.5131804271795398e-17, 2.051733824771517e-18], [3.077196507109856e-09, 3.5170667920043716e-09, 2.0099071981330448e-09, 7.657378878503454e-10, 2.187990993194209e-10, 5.001507343185927e-11, 9.527414182596673e-12, 1.5556159621201043e-12, 2.2224796291215624e-13, 2.8224136560048867e-14, 3.2258639706300817e-15, 3.351805042619009e-16, 3.1132320190314716e-17, 2.6364114264945774e-18, 2.152338304585491e-19], [2.979769297718106e-10, 3.4057128365459966e-10, 1.9462714670388321e-10, 7.414938379931394e-11, 2.1187169458109284e-11, 4.8431544716442225e-12, 9.225766441093946e-13, 1.5063635592513094e-13, 2.1521136360187392e-14, 2.7330531339783012e-15, 3.1237297962899905e-16, 3.2456834442832976e-17, 3.091365098305168e-18, 2.6504580301392466e-19, 2.084193058028038e-20], [2.6793248245001452e-11, 3.0623212861023796e-11, 1.7500326152252284e-11, 6.667304240198446e-12, 1.9050907442222334e-12, 4.354828413965641e-13, 8.295549950659914e-14, 1.3544797854368148e-14, 1.9351201096494335e-15, 2.457484582498955e-16, 2.808770059695517e-17, 2.918427353217216e-18, 2.7796686326774614e-19, 2.4438528876672748e-20, 1.9456333773969822e-21]] |
| Legacy trial inputs | {"lambda_home": 1.2588406616487937, "lambda_away": 1.1429451397979287, "rho": -0.01984634636300814, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T11:28:22Z", "over": 2.04, "under": 1.85, "bookmaker": "pinnacle", "event_id": "5262991e389930615bec34b642428c93", "kickoff_utc": "2026-11-01T17:30:00Z", "home_team": "Elche CF", "away_team": "Valencia"}} |
| Legacy p home | 0.3983 |
| Legacy p draw | 0.2817 |
| Legacy p away | 0.3199 |
| Legacy p over 1 5 | 0.6947 |
| Legacy p under 3 5 | 0.7782 |
| Legacy p btts yes | 0.4904 |
| Legacy p over 2 5 | 0.4307 |
| Legacy goal margin distribution | {"-1": 0.18877578130614703, "-10": 1.0438587240796281e-07, "-11": 1.073017133459245e-08, "-12": 1.0125684086725223e-09, "-13": 8.793992789712865e-11, "-14": 6.510260222663625e-12, "-2": 0.0899193959820919, "-3": 0.030802078609715688, "-4": 0.008235117515645107, "-5": 0.0017989695193843765, "-6": 0.00033160665679698797, "-7": 5.2813298829908705e-05, "-8": 7.399764866215792e-06, "-9": 9.251244519637841e-07, "0": 0.2817468863682605, "1": 0.22162147092774553, "10": 2.9193571925678004e-07, "11": 3.305198479857236e-08, "12": 3.435268116916708e-09, "13": 3.286001426328344e-10, "14": 2.6793248245001452e-11, "2": 0.1161277127987832, "3": 0.04381349455042083, "4": 0.012901584381141784, "5": 0.003104148065284817, "6": 0.0006302128310178462, "7": 0.00011054845403508566, "8": 1.7059750508652032e-05, "9": 2.349093444665465e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3875 |
| Legacy raw p draw | 0.2811 |
| Legacy raw p away | 0.3314 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2588 |
| Legacy lambda away | 1.1429 |
| Legacy model home team | Elche |
| Legacy model away team | Valencia |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 68.6% |
| Market home draw odds | 1.40 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:28:10Z |
| Market reference home draw last update utc | 2026-10-31T11:28:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.6% |
| Market draw away odds | 1.62 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:28:10Z |
| Market reference draw away last update utc | 2026-10-31T11:28:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.7% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:28:10Z |
| Market reference home away last update utc | 2026-10-31T11:28:22Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.60 |
| Market reference dc home draw odds | 1.39 |
| Market reference dc home away odds | 1.33 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.24, "price": 1.64, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.64, "price": 2.24, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.06, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.06, "price": 1.76, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 74.4% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:28:22Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.46 |
| Market reference over 1 5 last update utc | 2026-10-31T11:28:22Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 74.4% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.47 |
| Market reference under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.7% |
| Market btts yes odds | 1.79 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:28:10Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.05 |
| Market reference btts yes last update utc | 2026-10-31T11:28:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 9.23453524708649, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,471.9746 |
| Elo away rating | 1,446.4037 |
| Elo rating diff | 85.5709 |
| Elo home expectancy | 0.6207 |

</details>


---

## 2026-11-01 — Getafe vs Sevilla

The model's most likely 1X2 outcome is **Sevilla win** at **36.3%**. Expected goals are 1.02 for Getafe and 0.92 for Sevilla (1.94 combined). The most likely exact score is 1-1 at 14.2%. Goal-market probabilities: at least one goal: 86.2%; Over 2.5 goals: 32.9%; Under 3.5 goals: 85.2%; Double Chance 1X: 63.7%; Double Chance X2: 68.3%; Double Chance 12 (either team wins): 68.0%; Under 4.5 goals: 94.5%; BTTS Yes (both teams score): 41.2%; BTTS No (at least one team does not score): 58.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 31.7% | 3.16 |
| Draw | 32.0% | 3.13 |
| Sevilla win | 36.3% | 2.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 1.02 |
| Sevilla expected goals | 0.92 |
| Expected total goals | 1.94 |
| Over 0.5 | 86.2% |
| Under 0.5 | 13.8% |
| Over 1.5 | 60.5% |
| Under 1.5 | 39.5% |
| Over 2.5 | 32.9% |
| Under 2.5 | 67.1% |
| Over 3.5 | 14.8% |
| Under 3.5 | 85.2% |
| Over 4.5 | 5.5% |
| Under 4.5 | 94.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.20% |
| 2 | 0-1 | 14.09% |
| 3 | 0-0 | 13.80% |
| 4 | 1-0 | 11.62% |
| 5 | 1-2 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 31.7% | 29.5% | 3.27 | +3.5% |
| Draw | 32.0% | 32.0% | 3.02 | -3.4% |
| Sevilla win | 36.3% | 38.5% | 2.52 | -8.4% |

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
| Market best home last update utc | 2026-10-31T11:28:22Z |
| Market best draw last update utc | 2026-10-31T11:28:22Z |
| Market best away last update utc | 2026-10-31T11:28:22Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Getafe |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0249 |
| Dc lambda away | 0.9195 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:27:45.223690+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.25 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.53 |
| Fair Over 2.5 odds | 3.04 |
| Fair Under 2.5 odds | 1.49 |
| Fair Over 3.5 odds | 6.76 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.19 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.2296675875779055, "-10": 3.0816394625529255e-08, "-11": 2.6726597508826092e-09, "-12": 2.1217602699732541e-10, "-13": 1.4540122947209176e-11, "-2": 0.09699325542186094, "-3": 0.02873553664154857, "-4": 0.006579228706697921, "-5": 0.0012241105631908267, "-6": 0.00019154512356503266, "-7": 2.5840842868632907e-05, "-8": 3.06236386519833e-06, "-9": 3.234880090312436e-07, "0": 0.3199951367401852, "1": 0.189059994008932, "10": 6.724746377549465e-08, "11": 6.500854976580392e-09, "12": 5.752489556804418e-10, "13": 4.394002769916755e-11, "2": 0.08883290117082926, "3": 0.02933488186263235, "4": 0.007486394980651256, "5": 0.001552569750390689, "6": 0.0002707910438090412, "7": 4.0719514677806065e-05, "8": 5.378800432502988e-06, "9": 6.333146700595505e-07} |
| Raw goal margin distribution | {"-1": 0.200508049086988, "-10": 1.8557801839746534e-08, "-11": 1.5403022210877672e-09, "-12": 1.1706020561094732e-10, "-13": 7.72037486163386e-12, "-2": 0.08186836515100403, "-3": 0.02334063223414092, "-4": 0.005131057055901969, "-5": 0.0009154989230178307, "-6": 0.00013727569013041952, "-7": 1.773814730204608e-05, "-8": 2.012783095524731e-06, "-9": 2.0353410972017965e-07, "0": 0.32033720351468514, "1": 0.22390286116773964, "10": 5.493558442623572e-08, "11": 5.082365325126512e-09, "12": 4.30528535514404e-10, "13": 3.164927520980516e-11, "2": 0.10171419379660483, "3": 0.03232293437979051, "4": 0.00792022884820761, "5": 0.0015751482889382036, "6": 0.0002632630844988501, "7": 3.7917291584300375e-05, "8": 4.7957744452427455e-06, "9": 5.405448031146346e-07} |
| Unadjusted home-win probability | 36.8% |
| Unadjusted draw probability | 32.0% |
| Unadjusted away-win probability | 31.2% |
| Raw p over 1 5 | 58.2% |
| Raw p under 3 5 | 86.7% |
| Raw p btts yes | 38.9% |
| P home draw | 63.7% |
| P draw away | 68.3% |
| P home away | 68.0% |
| Raw p home draw | 68.8% |
| Raw p draw away | 63.2% |
| Raw p home away | 68.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0456 |
| Totals anchor target over 2 5 | 0.3293 |
| Totals anchor reference over odds | 2.81 |
| Totals anchor reference under odds | 1.45 |
| Totals anchor reference last update utc | 2026-10-31T11:28:22Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3078 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 5.24, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.61, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.17, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.24, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.27 |
| Reference draw odds | 3.02 |
| Reference away odds | 2.52 |
| Market reference 1x2 last update utc | 2026-10-31T11:28:22Z |
| Market reference home last update utc | 2026-10-31T11:28:22Z |
| Market reference draw last update utc | 2026-10-31T11:28:22Z |
| Market reference away last update utc | 2026-10-31T11:28:22Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.72 |
| Reference Under 2.5 odds | 1.47 |
| Market reference over 2 5 last update utc | 2026-10-31T11:26:29Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:26:29Z |
| Home probability edge | +2.2% |
| Draw probability edge | +0.0% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | 0.0731 |
| Raw ev home | 0.2025 |
| Raw edge prob draw | 0.0005 |
| Raw ev draw | -0.0326 |
| Raw edge prob away | -0.0736 |
| Raw ev away | -0.2140 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.14005935529007132, 0.14015411400283218, 0.06845714149948444, 0.02183250049304107, 0.005222151414789518, 0.0009992759338832695, 0.0001593456273612802, 2.177950891229381e-05, 2.604738136064823e-06, 2.769029176223417e-07, 2.6493144264107838e-08, 2.304341237340703e-09, 1.8372638010584616e-10, 1.3521788500021124e-11], [0.1253132271484469, 0.13906720448859577, 0.07103368381994477, 0.022654216975056533, 0.005418699120833574, 0.00103688598707965, 0.00016534296735362756, 2.2599230934017292e-05, 2.7027734599811527e-06, 2.8732479721423617e-07, 2.749027481766811e-08, 2.3910704315305444e-09, 1.9064134592765537e-10, 1.4030712179209227e-11], [0.0662732574671547, 0.06340803433947022, 0.033843988485486094, 0.011753430325503076, 0.0028113221764277407, 0.000537955790661387, 8.578301553050885e-05, 1.1724902541782211e-05, 1.4022492846468417e-06, 1.490694641339904e-07, 1.4262467339045501e-08, 1.240531939431321e-09, 9.890828621390635e-11, 7.279395187090177e-12], [0.02292253475933365, 0.021931513957766064, 0.010491669213934478, 0.003733280130494939, 0.0009723775889662347, 0.00018606766562714842, 2.9670552352630094e-05, 4.05539875864715e-06, 4.850087229301837e-07, 5.1560012345253114e-08, 4.933089391224811e-09, 4.2907407283806897e-10, 3.4210309186145515e-11, 2.5177906682148264e-12], [0.005946319298398045, 0.005689239259940443, 0.002721636842270441, 0.0008679903425590101, 0.0002316445815194917, 4.82676877816086e-05, 7.696817995956336e-06, 1.0520082597507658e-06, 1.2581578605205614e-07, 1.3375148065131895e-08, 1.2796893954242382e-09, 1.1130581615632053e-10, 8.874473257583776e-12, 6.531383809391397e-13], [0.0012340245464033106, 0.0011806733787436028, 0.0005648143836914587, 0.00018013183198006192, 4.308602679400562e-05, 9.198853173052684e-06, 1.5973010966242018e-06, 2.1832060311682459e-07, 2.6110230635460817e-08, 2.7757105187066e-09, 2.6557069112500473e-10, 2.3099013423540383e-11, 1.84169690302511e-12, 1.355441498901934e-13], [0.00021341165079157264, 0.00020418512381923558, 9.767874582862958e-05, 3.1151918116231154e-05, 7.4512781216213265e-06, 1.4258266971194737e-06, 2.536779595955817e-07, 3.775626704409639e-08, 4.515491558659191e-09, 4.800301303918363e-10, 4.592767604180458e-11, 3.994733006521032e-12, 3.1850223520907214e-13, 2.3440944402213338e-14], [3.163484145756717e-05, 3.0267157374288538e-05, 1.4479301512364848e-05, 4.61777033751806e-06, 1.1045320213747102e-06, 2.1135585307567638e-07, 3.370303422993912e-08, 5.139705150645122e-09, 6.693489274429397e-10, 7.115673869479622e-11, 6.808038571033666e-12, 5.921548559222044e-13, 4.721282871552409e-14, 3.474742625480634e-15], [4.103186454637147e-06, 3.925791451338045e-06, 1.8780329251162165e-06, 5.989463460704964e-07, 1.4326295375612208e-07, 2.7413839725153712e-08, 4.371440701479441e-09, 5.97492590754142e-10, 7.972780016088189e-11, 9.229360822315825e-12, 8.830343494776869e-13, 7.680524611215974e-14, 6.1237240442784945e-15, 4.506903217247517e-16], [4.730688150096411e-07, 4.526164068807108e-07, 2.1652411369943092e-07, 6.905434138136937e-08, 1.651722058391885e-08, 3.1606247527422035e-09, 5.039966609844617e-10, 6.88867335203996e-11, 8.238565093092456e-12, 9.771839205205356e-13, 1.0180770918857984e-13, 8.855109843653535e-15, 7.060227238269767e-16, 5.1961454540699525e-17], [4.9087385033048455e-08, 4.696516686769044e-08, 2.2467349782688414e-08, 7.1653360695986e-09, 1.713888425433611e-09, 3.2795821508479323e-10, 5.2296573708015114e-11, 7.1479444526816825e-12, 8.548642481035667e-13, 9.087838857710649e-14, 9.701253693236058e-15, 9.188392314477545e-16, 7.325955164867535e-17, 5.39171436583614e-18], [4.630445629071859e-09, 4.4302553801697636e-09, 2.119360025555172e-09, 6.759109099408321e-10, 1.6167223336347817e-10, 3.09365162258121e-11, 4.933170528001832e-12, 6.742703471672965e-13, 8.063991223846894e-14, 8.572618746764467e-15, 8.20199466041674e-16, 7.959651277543061e-17, 6.910622158646003e-18, 5.0860399676375775e-19], [4.0039359366109603e-10, 3.830831877963617e-10, 1.8326058545337014e-10, 5.844586458953783e-11, 1.3979761711313636e-11, 2.6750736104616693e-12, 4.265701476869684e-13, 5.830400549494044e-14, 6.972915101509966e-15, 7.412724178323873e-16, 7.092246363189973e-17, 6.168749015653553e-18, 5.487608230052397e-19, 4.397887338015369e-20], [3.195871765409926e-11, 3.05770312778253e-11, 1.4627540001517903e-11, 4.665046878966202e-12, 1.1158401744599907e-12, 2.1351970554513687e-13, 3.4048084498410526e-14, 4.653723933687659e-15, 5.565659103521628e-16, 5.916707030614659e-17, 5.660907233354764e-18, 4.923787772617156e-19, 3.9257627699114303e-20, 3.223650450019433e-21]] |
| Legacy trial inputs | {"lambda_home": 1.037637305093724, "lambda_away": 0.9567665263910632, "rho": -0.01984634636300814, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3294 |
| Legacy p draw | 0.3169 |
| Legacy p away | 0.3536 |
| Legacy p over 1 5 | 0.5945 |
| Legacy p under 3 5 | 0.8585 |
| Legacy p btts yes | 0.4012 |
| Legacy p over 2 5 | 0.3207 |
| Legacy goal margin distribution | {"-1": 0.22396350916107255, "-10": 2.89856407725205e-08, "-11": 2.5022619784554488e-09, "-12": 1.9775709228505538e-10, "-13": 1.3521788500021124e-11, "-2": 0.09411666804273518, "-3": 0.027819904562294738, "-4": 0.006349004454180901, "-5": 0.0011768424572627622, "-6": 0.0001833999707026754, "-7": 2.4636398096754183e-05, "-8": 2.90676348470835e-06, "-9": 3.056685878270082e-07, "0": 0.3169449307277201, "1": 0.20012546720675883, "10": 5.370556604555055e-08, "11": 5.028156356869739e-09, "12": 4.3097062493892135e-10, "13": 3.195871765409926e-11, "2": 0.09111420717433691, "3": 0.029208872778168877, "4": 0.007229435669864181, "5": 0.0014533047682518119, "6": 0.0002456276406885243, "7": 3.57844867400293e-05, "8": 4.578960315491904e-06, "9": 5.222129036076507e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3642 |
| Legacy raw p draw | 0.3140 |
| Legacy raw p away | 0.3218 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0376 |
| Legacy lambda away | 0.9568 |
| Legacy model home team | Getafe |
| Legacy model away team | Sevilla |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 61.7% |
| Market home draw odds | 1.54 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:28:10Z |
| Market reference home draw last update utc | 2026-10-31T11:28:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.9% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:28:10Z |
| Market reference draw away last update utc | 2026-10-31T11:28:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 68.4% |
| Market home away odds | 1.43 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:28:10Z |
| Market reference home away last update utc | 2026-10-31T11:28:22Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home draw odds | 1.54 |
| Market reference dc home away odds | 1.39 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 2.6, "price": 1.47, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 1.47, "price": 2.6, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.99, "price": 1.83, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.83, "price": 1.99, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.6, "price": 2.29, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.29, "price": 1.6, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 61.6% |
| Market over 1 5 odds | 1.57 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:28:22Z |
| Market reference over 1 5 odds | 1.55 |
| Market reference over 1 5 opposite odds | 2.38 |
| Market reference over 1 5 last update utc | 2026-10-31T11:28:27Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 85.9% |
| Market reference under 3 5 odds | 1.13 |
| Market reference under 3 5 opposite odds | 4.80 |
| Market reference under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 43.1% |
| Market btts yes odds | 2.26 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:28:10Z |
| Market reference btts yes odds | 2.15 |
| Market reference btts yes opposite odds | 1.67 |
| Market reference btts yes last update utc | 2026-10-31T11:28:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 8.569662180849814, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,449.4205 |
| Elo away rating | 1,481.9065 |
| Elo rating diff | 27.5140 |
| Elo home expectancy | 0.5395 |

</details>


---

## 2026-11-01 — Real Racing Club de Santander vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **80.6%**. Expected goals are 1.19 for Real Racing Club de Santander and 3.51 for Real Madrid (4.70 combined). The most likely exact score is 1-3 at 7.9%. Goal-market probabilities: at least one goal: 99.0%; Over 2.5 goals: 84.9%; Under 3.5 goals: 30.9%; Double Chance 1X: 19.4%; Double Chance X2: 91.6%; Double Chance 12 (either team wins): 89.0%; Under 4.5 goals: 49.3%; BTTS Yes (both teams score): 67.6%; BTTS No (at least one team does not score): 32.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 8.4% | 11.92 |
| Draw | 11.0% | 9.09 |
| Real Madrid win | 80.6% | 1.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.19 |
| Real Madrid expected goals | 3.51 |
| Expected total goals | 4.70 |
| Over 0.5 | 99.0% |
| Under 0.5 | 1.0% |
| Over 1.5 | 94.9% |
| Under 1.5 | 5.1% |
| Over 2.5 | 84.9% |
| Under 2.5 | 15.1% |
| Over 3.5 | 69.1% |
| Under 3.5 | 30.9% |
| Over 4.5 | 50.7% |
| Under 4.5 | 49.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-3 | 7.85% |
| 2 | 1-4 | 6.88% |
| 3 | 1-2 | 6.71% |
| 4 | 0-3 | 6.58% |
| 5 | 0-4 | 5.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 8.4% | 8.3% | 10.23 | -14.2% |
| Draw | 11.0% | 10.9% | 7.96 | -12.4% |
| Real Madrid win | 80.6% | 80.8% | 1.22 | -1.6% |

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
| Market best home last update utc | 2026-10-31T11:28:22Z |
| Market best draw last update utc | 2026-10-31T11:28:22Z |
| Market best away last update utc | 2026-10-31T11:28:22Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santander |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1924 |
| Dc lambda away | 3.5072 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:27:45.223690+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 67.6% |
| P btts no | 32.4% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 101.81 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 19.78 |
| Fair Over 2.5 odds | 1.18 |
| Fair Under 2.5 odds | 6.62 |
| Fair Over 3.5 odds | 1.45 |
| Fair Under 3.5 odds | 3.24 |
| Fair Over 4.5 odds | 1.97 |
| Fair Under 4.5 odds | 2.03 |
| Goal margin distribution | {"-1": 0.1653002656707747, "-10": 0.0010332183028905787, "-11": 0.0003195648204942384, "-12": 9.101293272877935e-05, "-13": 2.401294253821571e-05, "-14": 5.900127383680013e-06, "-15": 1.3562617301163875e-06, "-16": 2.9285273169588324e-07, "-17": 5.961268552084255e-08, "-18": 1.147582609697615e-08, "-19": 2.0932763768539637e-09, "-2": 0.1895499891008599, "-20": 3.5789439488199196e-10, "-21": 4.984570017987728e-11, "-3": 0.17125256741931602, "-4": 0.12666536805799133, "-5": 0.07879881950401195, "-6": 0.042142004041828066, "-7": 0.019719456636830838, "-8": 0.008189796525866627, "-9": 0.0030546116119330455, "0": 0.10999113652717041, "1": 0.053961555391409836, "10": 2.0720251452929428e-08, "11": 2.1788484100918852e-09, "12": 2.1097756850597472e-10, "13": 1.8925339416130184e-11, "14": 1.5809742819073322e-12, "15": 1.2355833461470752e-13, "16": 9.070744615831606e-15, "17": 6.277655351049406e-16, "18": 4.108732447881746e-17, "19": 2.548094892794453e-18, "2": 0.021291473666573253, "20": 1.4811841069078738e-19, "21": 7.013696502585289e-21, "3": 0.006540096714213968, "4": 0.0016446371287693578, "5": 0.000347854025876415, "6": 6.324957748495398e-05, "7": 1.0062421604129735e-05, "8": 1.4208420427481531e-06, "9": 1.801746999350638e-07} |
| Raw goal margin distribution | {"-1": 0.16425852869142246, "-10": 0.001026706869230766, "-11": 0.00031755089456702944, "-12": 9.043936113022123e-05, "-13": 2.386161083815092e-05, "-14": 5.862944256033323e-06, "-15": 1.3477144480402867e-06, "-16": 2.9100714772858617e-07, "-17": 5.923700107355169e-08, "-18": 1.1403504420024671e-08, "-19": 2.0800843629093742e-09, "-2": 0.18835542820719833, "-20": 3.5563891256719626e-10, "-21": 4.9531568143075223e-11, "-3": 0.17017331850482834, "-4": 0.1258671116403515, "-5": 0.07830222233356261, "-6": 0.04187642138340804, "-7": 0.01959518286686466, "-8": 0.00813818369959714, "-9": 0.003035361177816703, "0": 0.11317692370634068, "1": 0.055180689323181424, "10": 2.1188376610513884e-08, "11": 2.2280743452907895e-09, "12": 2.1574410851288568e-10, "13": 1.9352912774332002e-11, "14": 1.6166926628611598e-12, "15": 1.2634984344334215e-13, "16": 9.275676672874484e-15, "17": 6.419484151107496e-16, "18": 4.2015595561340966e-17, "19": 2.6056630804170453e-18, "2": 0.02177250424132338, "20": 1.5146479644789554e-19, "21": 7.172154414545526e-21, "3": 0.006687854757204613, "4": 0.0016817938214293573, "5": 0.0003557129662493012, "6": 6.467855234534873e-05, "7": 1.0289758261207245e-05, "8": 1.4529426138572966e-06, "9": 1.8424532185736232e-07} |
| Unadjusted home-win probability | 8.6% |
| Unadjusted draw probability | 11.3% |
| Unadjusted away-win probability | 80.1% |
| Raw p over 1 5 | 94.9% |
| Raw p under 3 5 | 31.0% |
| Raw p btts yes | 67.7% |
| P home draw | 19.4% |
| P draw away | 91.6% |
| P home away | 89.0% |
| Raw p home draw | 19.9% |
| Raw p draw away | 91.4% |
| Raw p home away | 88.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8489 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.68, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:10Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 8.89, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:10Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.08, "price": 8.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.77, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.23 |
| Reference draw odds | 7.96 |
| Reference away odds | 1.22 |
| Market reference 1x2 last update utc | 2026-10-31T11:28:22Z |
| Market reference home last update utc | 2026-10-31T11:28:22Z |
| Market reference draw last update utc | 2026-10-31T11:28:22Z |
| Market reference away last update utc | 2026-10-31T11:28:22Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.19 |
| Reference Under 2.5 odds | 4.78 |
| Market reference over 2 5 last update utc | 2026-10-31T11:26:29Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:26:29Z |
| Home probability edge | +0.1% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +2.5% |
| Under 2.5 probability edge | -2.5% |
| Raw edge prob home | 0.0027 |
| Raw ev home | -0.1227 |
| Raw edge prob draw | 0.0046 |
| Raw ev draw | -0.0991 |
| Raw edge prob away | -0.0073 |
| Raw ev away | -0.0227 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.008899269685274854, 0.028287593700925127, 0.05309554144397953, 0.0649031792557818, 0.0595024915880077, 0.04364096237847118, 0.026673023074199304, 0.013973441224720396, 0.006405345458137765, 0.002609932166045449, 0.00095710237024517, 0.0003190765432863228, 9.750857379935276e-05, 2.7506075066957472e-05, 7.2049299061766226e-06, 1.7614392640455802e-06, 4.037168371159641e-07, 8.708775850204253e-08, 1.7742457738521404e-08, 3.4244383368790325e-09, 6.278971713566535e-10, 1.0964741660157436e-10, 1.8276999283025272e-11], [0.009084157701786258, 0.03575537358930448, 0.06187826253307045, 0.0756390434299937, 0.06934500893524735, 0.05085976814268065, 0.03108510205282212, 0.016284837503841305, 0.007464876279524241, 0.0030416502661425944, 0.0011154200546111953, 0.00037185612156243395, 0.00011363781147514371, 3.205595211875422e-05, 8.396722815929019e-06, 2.0528051556206454e-06, 4.704970654163106e-07, 1.0149325230427729e-07, 2.067730035457849e-08, 3.990886780225856e-09, 7.317598607403383e-10, 1.277845831500507e-10, 2.1300262304416443e-11], [0.005708891037063027, 0.020935383739583723, 0.03745896841633654, 0.04407538241275603, 0.04040780592453966, 0.02963633103567057, 0.01811349930126684, 0.009489285003659607, 0.00434983391862244, 0.0017723901911871015, 0.0006499628132308037, 0.00021668307817189348, 6.621752166857157e-05, 1.867922020387199e-05, 4.892827200657474e-06, 1.196183454337276e-06, 2.7416182360233626e-07, 5.9140804864429347e-08, 1.204880282806531e-08, 2.32551673088341e-09, 4.2640142225339355e-10, 7.44609412466439e-11, 1.2411806971462713e-11], [0.0022177396240623784, 0.008132793175206902, 0.014912103322015488, 0.017787812070030315, 0.01569726795247726, 0.011512860417712443, 0.007036572404351213, 0.003686313720127233, 0.0016897851048112433, 0.0006885225047695606, 0.00025249181946386746, 8.417513054739158e-05, 2.572359862155468e-05, 7.256338669589519e-06, 1.9007223445222134e-06, 4.6468279515391635e-07, 1.0650396647277763e-07, 2.29744981109784e-08, 4.680612623509123e-09, 9.033962230173157e-10, 1.6564466264088982e-10, 2.8925929532650098e-11, 4.82162927057503e-12], [0.000646145942557693, 0.0023695168065739664, 0.004344691753701737, 0.005310884869667239, 0.0047512926218667055, 0.0033543108331678183, 0.002050129176236012, 0.0010740199739462163, 0.0004923246071909028, 0.00020060336118339476, 7.356434583458505e-05, 2.4524709067438917e-05, 7.494657486821689e-06, 2.1141588211294356e-06, 5.537818856264569e-07, 1.3538690448930061e-07, 3.1030290957524154e-08, 6.693697752270729e-09, 1.363712323372219e-09, 2.6320754595858946e-10, 4.82611328717182e-11, 8.427667431939207e-12, 1.4047980005843262e-12], [0.00015060544513120045, 0.0005522933905416722, 0.0010126725131693942, 0.0012378754197088766, 0.0011348700108811292, 0.00081223368863052, 0.0004778496572172118, 0.0002503354824386715, 0.00011475235195554742, 4.67571743718604e-05, 1.7146576834248273e-05, 5.716285567304381e-06, 1.746875051850816e-06, 4.927738601497495e-07, 1.290769807517924e-07, 3.15563461326322e-08, 7.232624202064563e-09, 1.5601851890673094e-09, 3.1785775931578874e-10, 6.134912720193216e-11, 1.1248835471921501e-11, 1.9643435351164436e-12, 3.2743412016168803e-13], [2.925293731292214e-05, 0.00010727503190726094, 0.00019669704186629422, 0.00024043946101952156, 0.00022043214478533724, 0.00016167173307951745, 9.642457348082108e-05, 4.8624059831296805e-05, 2.228899064932003e-05, 9.081907295170183e-06, 3.3304754474614637e-06, 1.1103060929665858e-06, 3.393053042722495e-07, 9.571422087594199e-08, 2.5071343358031103e-08, 6.129365471737009e-09, 1.404833020523285e-09, 3.030434888497965e-10, 6.173928903825781e-11, 1.1916183844994447e-11, 2.1849241813058724e-12, 3.8154542316678036e-13, 6.359935912580991e-14], [4.870252717176387e-06, 1.785996770316573e-05, 3.274762778050009e-05, 4.0030200243497424e-05, 3.669922922986523e-05, 2.691634651585291e-05, 1.6451065525646167e-05, 8.410094488910685e-06, 3.7108416194847527e-06, 1.5120253808463884e-06, 5.544830224732109e-07, 1.8485224947921127e-07, 5.649014190975995e-08, 1.5935235470783303e-08, 4.174068976614366e-09, 1.0204636383679568e-09, 2.338873447884604e-10, 5.045299756415821e-11, 1.0278828993432018e-11, 1.9838974161347336e-12, 3.637628870222452e-13, 6.352259993677211e-14, 1.0588507686587985e-14], [7.094823031275709e-07, 2.6017810072025337e-06, 4.7705660730361155e-06, 5.83146713583278e-06, 5.3462222987284966e-06, 3.921084310573254e-06, 2.3965367991837837e-06, 1.255495712395151e-06, 5.616039192600808e-07, 2.2026685510730264e-07, 8.077525226606893e-08, 2.692866414021719e-08, 8.229296981815795e-09, 2.3213923833599777e-09, 6.080645590520081e-10, 1.48657766742542e-10, 3.407193459749561e-11, 7.349825766795476e-12, 1.4973858013558354e-12, 2.890076120699037e-13, 5.299177391076024e-14, 9.25376220105502e-15, 1.5424987688359321e-15], [9.18711419317682e-08, 3.369056439242903e-07, 6.17742473432735e-07, 7.551189684997739e-07, 6.922844240654083e-07, 5.07742746556332e-07, 3.10328490861498e-07, 1.6257463262961976e-07, 7.452328084225278e-08, 2.9631547963392187e-08, 1.0459619123404771e-08, 3.487003290079204e-09, 1.0656148964988759e-09, 3.005980109593271e-10, 7.873851844096011e-11, 1.924975256952683e-11, 4.411988185607502e-12, 9.517318236387655e-13, 1.9389707520053648e-13, 3.742370913381521e-14, 6.861925605065085e-15, 1.1982732998811572e-15, 1.9973877106815279e-16], [1.0706787208611338e-08, 3.926343967245528e-08, 7.199254383577507e-08, 8.800258648050484e-08, 8.067976363904679e-08, 5.9173026804565076e-08, 3.6166102288041925e-08, 1.8946667696546815e-08, 8.685044000630562e-09, 3.5388217308353987e-09, 1.2663786161776288e-09, 4.0638008233677674e-10, 1.2418820211915337e-10, 3.5032098992125703e-11, 9.176293494803781e-12, 2.243392214863441e-12, 5.141790738302796e-13, 1.1091611469172636e-13, 2.2597027541968402e-14, 4.361409707417274e-15, 7.996980961586207e-16, 1.396483919740165e-16, 2.3277826683862647e-17], [1.1343486096648276e-09, 4.159831267337298e-09, 7.627371350078176e-09, 9.323582291873783e-09, 8.54775348840706e-09, 6.269186019820389e-09, 3.83167863973615e-09, 2.007336630550902e-09, 9.201516192522621e-10, 3.749264304978617e-10, 1.3749130340072433e-10, 4.4728818537104385e-11, 1.3157328306416143e-11, 3.7115347499758946e-12, 9.72197874572042e-13, 2.3767996788210193e-13, 5.447556826841753e-14, 1.1751194643038282e-14, 2.3940801545185696e-15, 4.620768995771548e-16, 8.472536213286673e-17, 1.4795284167994606e-17, 2.4662085666203455e-18], [1.1016543505654175e-10, 4.0399363777897735e-10, 7.407534826242213e-10, 9.05485748136314e-10, 8.30138965908087e-10, 6.088495189569388e-10, 3.721241783582886e-10, 1.9494810618661044e-10, 8.936309577957597e-11, 3.6412027993931694e-11, 1.3352852136088292e-11, 4.451542525701884e-12, 1.3274988805910308e-12, 3.604560687735866e-13, 9.441771330325027e-14, 2.3082954254859447e-14, 5.2905470391644445e-15, 1.1412501053507096e-15, 2.325077842346024e-16, 4.487588933223656e-17, 8.228340300472732e-18, 1.4368853659845315e-18, 2.3951273653183096e-19], [9.876022220595287e-12, 3.6216896358068545e-11, 6.640647178151128e-11, 8.117425728348325e-11, 7.441962961687976e-11, 5.4581651451122906e-11, 3.335988872009624e-11, 1.7476550858023476e-11, 8.011150858409561e-12, 3.264236167909121e-12, 1.1970457370467254e-12, 3.990683001178423e-13, 1.2195374938014402e-13, 3.3570413267130584e-14, 8.464283140370745e-15, 2.0693220974525566e-15, 4.742827012036569e-16, 1.0230987054982842e-16, 2.0843670633931322e-17, 4.0229975943604806e-18, 7.376476260850828e-19, 1.2881274235996187e-19, 2.1471644957330783e-20], [8.221178533326512e-13, 3.0148329381210867e-12, 5.527928634522719e-12, 6.757255568401007e-12, 6.19497453325418e-12, 4.543585374764722e-12, 2.777004697780898e-12, 1.4548149198262062e-12, 6.668788302951701e-13, 2.7172750032254295e-13, 9.964666438574871e-14, 3.32199712493372e-14, 1.0151896422143618e-14, 2.863736122672249e-15, 7.319979166527032e-16, 1.7225828401477335e-16, 3.948110559869306e-17, 8.516664834528545e-18, 1.7351068450823674e-18, 3.3488970279359126e-19, 6.140460899413016e-20, 1.072286522503192e-20, 1.787381828994875e-21], [6.387381812503118e-14, 2.342351403588617e-13, 4.2948818928858156e-13, 5.249998056248977e-13, 4.813138104497139e-13, 3.530103922288184e-13, 2.1575725703969393e-13, 1.1303073302430897e-13, 5.1812640906694536e-14, 2.1111660408314517e-14, 7.74197141193327e-15, 2.581000270335153e-15, 7.887438316338077e-16, 2.22495788792505e-16, 5.828045472744348e-17, 1.3903897440372062e-17, 3.0674543171192726e-18, 6.61695763529917e-19, 1.3480779988054069e-19, 2.601899944329312e-20, 4.770784153428079e-21, 8.331048162820725e-22, 1.388692647926345e-22], [4.652463252376379e-15, 1.7061300152773597e-14, 3.128320924989046e-14, 3.824011738883953e-14, 3.5058101765502543e-14, 2.571269302136693e-14, 1.5715401697856636e-14, 8.232971618439728e-15, 3.77394705535073e-15, 1.5377384213053829e-15, 5.639123909026603e-16, 1.8799579020941673e-16, 5.745079595886521e-17, 1.6206225203875275e-17, 4.245051915018641e-18, 1.0378173304108774e-18, 2.321163961296512e-19, 4.8196824840656356e-20, 9.819177144698334e-21, 1.8951808789098227e-21, 3.4749602592091574e-22, 6.068197669885614e-23, 1.011500753043392e-23], [3.189437432605544e-16, 1.1696158874200734e-15, 2.1445809065266506e-15, 2.621502958994853e-15, 2.4033638961011735e-15, 1.762701200779062e-15, 1.0773495184077976e-15, 5.644009729258669e-16, 2.5871817474020796e-16, 1.0541771565765766e-16, 3.8658301864853357e-17, 1.2887814001752925e-17, 3.9384667696320885e-18, 1.1109973040641152e-18, 2.910141734961303e-19, 7.114625655836192e-20, 1.630651834364897e-20, 3.432552631317993e-21, 6.731412897606295e-22, 1.299217319699587e-22, 2.382215124832486e-23, 4.1599762850135866e-24, 6.934215682880371e-25], [2.0650075256402334e-17, 7.572701019119009e-17, 1.3885131170935234e-16, 1.6972972360176167e-16, 1.5560626716061854e-16, 1.141264352093035e-16, 6.97532060203963e-17, 3.654225176690363e-17, 1.6750759002097312e-17, 6.825290690560103e-18, 2.5029393416938383e-18, 8.344240470310804e-19, 2.549968040015819e-19, 7.193173850675589e-20, 1.8841769780275986e-20, 4.6063783447266746e-21, 1.0557687306352684e-21, 2.27745101998711e-22, 4.527739410444914e-23, 8.411808036096344e-24, 1.5423698581396408e-24, 2.693384810505665e-25, 4.4895715536462877e-26], [1.2666251135938254e-18, 4.644909604181644e-18, 8.516799880038337e-18, 1.0410806148063624e-17, 9.544507870842865e-18, 7.000236423652964e-18, 4.278491066114911e-18, 2.241412354217847e-18, 1.0274505908755088e-18, 4.186466387603722e-19, 1.5352417793288667e-19, 5.118153034471293e-20, 1.56408803272728e-20, 4.4121169209237234e-21, 1.155708078151025e-21, 2.825439821260032e-22, 6.475827190775497e-23, 1.3969327574247864e-23, 2.8459821263609796e-24, 5.360230311811884e-25, 9.460519501807242e-26, 1.652056372288968e-26, 2.753793392284014e-27], [7.380710242180444e-20, 2.706620255800437e-19, 4.962796918406731e-19, 6.066447186441046e-19, 5.561649318560078e-19, 4.079085130654391e-19, 2.493105694324502e-19, 1.306086145156793e-19, 5.987024114730282e-20, 2.4394822914777226e-20, 8.945957729170304e-21, 2.982382404797547e-21, 9.114046799583662e-22, 2.5709703840912476e-22, 6.734389171534526e-23, 1.6464029019817517e-23, 3.773508322279671e-24, 8.140021699955619e-25, 1.6583730421620905e-25, 3.2007945607764705e-26, 5.7270725891978245e-27, 9.626644266523481e-28, 1.6046540430270634e-28], [4.09599028491318e-21, 1.5020627973375977e-20, 2.7541479473912765e-20, 3.366628403537039e-20, 3.0864863718300064e-20, 2.263724291872251e-20, 1.383571007144441e-20, 7.24824032685707e-21, 3.3225518689691213e-21, 1.353812226499029e-21, 4.964638191391784e-22, 1.6550994355711094e-22, 5.057920704432128e-23, 1.4267827038995421e-23, 3.737308702865559e-24, 9.136858202386063e-25, 2.094141745297727e-25, 4.517376879457443e-26, 9.203287551701953e-27, 1.7763091890557987e-27, 3.256999850899538e-28, 5.550132189255728e-29, 8.905169225209666e-30], [2.1697829583999384e-22, 7.956928687341213e-22, 1.4589642224428344e-21, 1.783415591625285e-21, 1.6350149939558157e-21, 1.1991704201819146e-21, 7.32923806996256e-22, 3.8396351665016274e-22, 1.760066778049468e-22, 7.17159586230155e-23, 2.6299347881709424e-23, 8.767614911068253e-24, 2.6793496532054554e-24, 7.558144870762629e-25, 1.9797773358071703e-25, 4.8400991803803045e-26, 1.1093368771301235e-26, 2.3930055219660786e-27, 4.8752890270491605e-28, 9.409703488454882e-29, 1.725341683065723e-29, 3.0129019038965e-30, 4.900802421543272e-31]] |
| Legacy trial inputs | {"lambda_home": 1.165413532854872, "lambda_away": 3.6671541992425305, "rho": -0.01984634636300814, "max_goals": 22, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0789 |
| Legacy p draw | 0.1056 |
| Legacy p away | 0.8155 |
| Legacy p over 1 5 | 0.9537 |
| Legacy p under 3 5 | 0.2908 |
| Legacy p btts yes | 0.6728 |
| Legacy p over 2 5 | 0.8592 |
| Legacy goal margin distribution | {"-1": 0.15382323313744542, "-10": 0.0014030191471991662, "-11": 0.0004534372304568815, "-12": 0.00013495469016746472, "-13": 3.721250914860837e-05, "-14": 9.556298694950436e-06, "-15": 2.296032595465191e-06, "-16": 5.182125775470899e-07, "-17": 1.1026497535169741e-07, "-18": 2.219007666853389e-08, "-19": 4.23548076813659e-09, "-2": 0.18297960128118199, "-20": 7.680935614781669e-10, "-21": 1.309476789059908e-10, "-22": 1.8276999283025272e-11, "-3": 0.17211952837757724, "-4": 0.1327046784006565, "-5": 0.08612405367644661, "-6": 0.04807585350121472, "-7": 0.02348957114048786, "-8": 0.010189147226259255, "-9": 0.0039700085040529605, "0": 0.10557037728734962, "1": 0.051556856142421684, "10": 1.5695110497763016e-08, "11": 1.612014116241309e-09, "12": 1.5247215271359291e-10, "13": 1.3361105368219052e-11, "14": 1.090420569138799e-12, "15": 8.325939554399067e-14, "16": 5.971920792752449e-15, "17": 4.038262620845654e-16, "18": 2.5826565851453978e-17, "19": 1.5666120342394072e-18, "2": 0.01967416806214628, "20": 9.028669461762324e-20, "21": 4.891683153647301e-21, "22": 2.1697829583999384e-22, "3": 0.005881318951318975, "4": 0.0014410588064229786, "5": 0.0002972150643232225, "6": 5.272592929657939e-05, "7": 8.186970255393054e-06, "8": 1.12859168771422e-06, "9": 1.397466261733583e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0748 |
| Legacy raw p draw | 0.1025 |
| Legacy raw p away | 0.8227 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1654 |
| Legacy lambda away | 3.6672 |
| Legacy model home team | Santander |
| Legacy model away team | Real Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 23.2% |
| Market home draw odds | 4.61 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:28:10Z |
| Market reference home draw last update utc | 2026-10-31T11:28:22Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.6% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:28:10Z |
| Market reference draw away last update utc | 2026-10-31T11:28:22Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.2% |
| Market home away odds | 1.10 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:28:10Z |
| Market reference home away last update utc | 2026-10-31T11:28:22Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home draw odds | 4.10 |
| Market reference dc home away odds | 1.09 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.05, "price": 1.76, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.05, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.17, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:28:10Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.17, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 94.5% |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 7.60 |
| Market reference over 1 5 last update utc | 2026-10-31T11:28:22Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 37.1% |
| Market under 3 5 odds | 2.48 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market reference under 3 5 odds | 2.48 |
| Market reference under 3 5 opposite odds | 1.53 |
| Market reference under 3 5 last update utc | 2026-10-31T11:28:22Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.8% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:28:10Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-31T11:28:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 10.724069412838478, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,438.0702 |
| Elo away rating | 1,670.4419 |
| Elo rating diff | -172.3717 |
| Elo home expectancy | 0.2705 |

</details>


---

## 2026-11-02 — Deportivo La Coruña vs CA Osasuna

The model's most likely 1X2 outcome is **Deportivo La Coruña win** at **46.0%**. Expected goals are 1.50 for Deportivo La Coruña and 0.98 for CA Osasuna (2.47 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 44.3%; Under 3.5 goals: 76.5%; Double Chance 1X: 74.4%; Double Chance X2: 54.0%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Deportivo La Coruña win | 46.0% | 2.17 |
| Draw | 28.4% | 3.52 |
| CA Osasuna win | 25.6% | 3.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Deportivo La Coruña expected goals | 1.50 |
| CA Osasuna expected goals | 0.98 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 70.9% |
| Under 1.5 | 29.1% |
| Over 2.5 | 44.3% |
| Under 2.5 | 55.7% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.46% |
| 2 | 1-0 | 11.54% |
| 3 | 0-0 | 9.31% |
| 4 | 2-0 | 8.86% |
| 5 | 2-1 | 8.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Deportivo La Coruña win | 46.0% | 44.7% | 2.18 | +0.2% |
| Draw | 28.4% | 29.2% | 3.30 | -6.2% |
| CA Osasuna win | 25.6% | 26.1% | 3.67 | -6.1% |

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
| Market best home last update utc | 2026-10-31T11:28:22Z |
| Market best draw last update utc | 2026-10-31T11:28:22Z |
| Market best away last update utc | 2026-10-31T11:28:22Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | La Coruna |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.4968 |
| Dc lambda away | 0.9779 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:27:45.223690+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.75 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.43 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.69 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.16379097162138012, "-10": 2.2243719758522577e-08, "-11": 1.955969291772948e-09, "-12": 1.5792391553852893e-10, "-13": 1.1783704370457362e-11, "-14": 8.141345130535351e-13, "-15": 4.835708677365184e-14, "-2": 0.0670736008341976, "-3": 0.019626082077063838, "-4": 0.0044846383950845545, "-5": 0.0008375783851810092, "-6": 0.0001320245448666771, "-7": 1.798293409123513e-05, "-8": 2.155060654417343e-06, "-9": 2.3045895895589793e-07, "0": 0.28418509871115627, "1": 0.22599129046090308, "10": 1.4054274025492793e-06, "11": 1.8916697088810974e-07, "12": 2.337832845399124e-08, "13": 2.6701131545127543e-09, "14": 2.8237501639217385e-10, "15": 2.5672756867492285e-11, "2": 0.14063532521129685, "3": 0.06298812575087745, "4": 0.022031028951249195, "5": 0.006298180267845901, "6": 0.0015195905354998347, "7": 0.00031682156054504696, "8": 5.811603136342388e-05, "9": 9.512886662565228e-06} |
| Raw goal margin distribution | {"-1": 0.15594036433934333, "-10": 2.1177563873450283e-08, "-11": 1.8622184176348483e-09, "-12": 1.5035452005194214e-10, "-13": 1.1218903793085329e-11, "-14": 7.751125189016836e-13, "-15": 4.603930030590393e-14, "-2": 0.06385871973343339, "-3": 0.018685391260306158, "-4": 0.004269686774166537, "-5": 0.0007974327110642539, "-6": 0.00012569652297952547, "-7": 1.7121000420950893e-05, "-8": 2.051767202407615e-06, "-9": 2.194129118906662e-07, "0": 0.2670810878632111, "1": 0.2404263361157293, "10": 1.4951981573379573e-06, "11": 2.012498872500014e-07, "12": 2.4871603871281137e-08, "13": 2.840664883344144e-09, "14": 3.0041153560975186e-10, "15": 2.7312587396853406e-11, "2": 0.14961831449361, "3": 0.06701145102625194, "4": 0.023438246495277065, "5": 0.006700472407172437, "6": 0.001616653385629348, "7": 0.0003370583302080453, "8": 6.182815480100154e-05, "9": 1.012051606723502e-05} |
| Unadjusted home-win probability | 48.9% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 76.3% |
| Raw p btts yes | 48.8% |
| P home draw | 74.4% |
| P draw away | 54.0% |
| P home away | 71.6% |
| Raw p home draw | 75.6% |
| Raw p draw away | 51.1% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4430 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.63, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:28:22Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:27:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.49, "price": 1.63, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.18 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.67 |
| Market reference 1x2 last update utc | 2026-10-31T11:28:22Z |
| Market reference home last update utc | 2026-10-31T11:28:22Z |
| Market reference draw last update utc | 2026-10-31T11:28:22Z |
| Market reference away last update utc | 2026-10-31T11:28:22Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.28 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-10-31T11:27:35Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:27:35Z |
| Home probability edge | +1.3% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | 0.0420 |
| Raw ev home | 0.0665 |
| Raw edge prob draw | -0.0244 |
| Raw ev draw | -0.1186 |
| Raw edge prob away | -0.0175 |
| Raw ev away | -0.1056 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09460765232980406, 0.08557076642184433, 0.04305161510817015, 0.014025416393445622, 0.0034269150736031605, 0.0006698551596472625, 0.00010911318325392985, 1.5234449147068594e-05, 1.861162690489804e-06, 2.0211074268625418e-07, 1.975317755192865e-08, 1.7550595292103388e-09, 1.4294144732207904e-10, 1.0746384919608175e-11, 7.502084060346504e-13, 4.88807922771858e-14], [0.12177168944920559, 0.13264490273302335, 0.06225660499476659, 0.020282045310029747, 0.004955635173079377, 0.000968672324443218, 0.00015778772370080826, 2.2030418149908546e-05, 2.6914128578379758e-06, 2.922707694241452e-07, 2.8564916069978822e-08, 2.537977903449514e-09, 2.067065126581532e-10, 1.5540263457730223e-11, 1.0848705276422755e-12, 7.068613265694828e-14], [0.08978814018479574, 0.08775392399012508, 0.04595569985431533, 0.01466485380606374, 0.0035831526958209846, 0.0007003947484978231, 0.00011408779859690283, 1.59290079731307e-05, 1.946015576271101e-06, 2.1132524061916549e-07, 2.0653751224072472e-08, 1.8350750305592672e-09, 1.4945833827686263e-10, 1.1236326920275185e-11, 7.844114064035621e-13, 5.110933269720883e-14], [0.04328064318961119, 0.04230008846255183, 0.020670874461140205, 0.007216729533897448, 0.0017271897268675367, 0.00033761179526853465, 5.499382538939052e-05, 7.678271417924792e-06, 9.380393181623927e-07, 1.018652610174636e-07, 9.955742878918052e-09, 8.845625653937935e-10, 7.204351262159751e-11, 5.416254921834357e-12, 3.7811040661428635e-13, 2.4636269195178188e-14], [0.015646950179481808, 0.01529245704278471, 0.007472997604097972, 0.0024345637867789266, 0.0006374762379514089, 0.00012205444631285367, 1.9881535546437094e-05, 2.775872110182651e-06, 3.3912283635389984e-07, 3.6826639964138717e-08, 3.5992305415542733e-09, 3.197897575300717e-10, 2.6045390494926512e-11, 1.9581010048773405e-12, 1.3669562785188582e-13, 8.906579207163546e-15], [0.004525386535437672, 0.004422860583139457, 0.0021613287157576243, 0.0007041207426352512, 0.0001720420926469622, 3.603856972997264e-05, 5.750106713041988e-06, 8.028334037894628e-07, 9.808057799709795e-08, 1.0650943393279433e-08, 1.0409638455962135e-09, 9.24890950822591e-11, 7.532807231054928e-12, 5.663189197162993e-13, 3.953489636244305e-14, 2.5759469518705834e-15], [0.001090687698465742, 0.0010659773684045478, 0.0005209134345005983, 0.00016970391948022988, 4.146478816758073e-05, 8.105074593672618e-06, 1.4148441398683967e-06, 1.9349518777534864e-07, 2.3638926540779652e-08, 2.567041035088359e-09, 2.508882836965385e-10, 2.2291293231748673e-11, 1.8155223023464439e-12, 1.3649156250102234e-13, 9.528517571917044e-15, 6.208428010081233e-16], [0.00022531928259808645, 0.00022021450893099345, 0.00010761269382838527, 3.5058216430933595e-05, 8.565986703749705e-06, 1.674383597998976e-06, 2.727415348447011e-07, 4.080901145649325e-08, 4.883438198716086e-09, 5.303111470309902e-10, 5.182965588984759e-11, 4.605037909776105e-12, 3.7505894976258015e-13, 2.8197054928449072e-14, 1.968444997177204e-15, 1.282565620994126e-16], [4.07290572582698e-05, 3.980631058261842e-05, 1.9452234704967873e-05, 6.337176685118896e-06, 1.5484008244111213e-06, 3.026641335302532e-07, 4.9301175919386494e-08, 6.883460229426725e-09, 9.011968293812354e-10, 9.585985195351126e-11, 9.368807667382263e-12, 8.32413677786878e-13, 6.779622793027834e-14, 5.096942664884617e-15, 3.558191206510878e-16, 2.3183851826892755e-17], [6.544219132639669e-06, 6.3959550466068085e-06, 3.1255249961132026e-06, 1.0182379780286348e-06, 2.4879226238532285e-07, 4.863113822774086e-08, 7.921560684976903e-09, 1.1060131307859358e-09, 1.3511944897638085e-10, 1.572454872619535e-11, 1.5053510813696842e-12, 1.3374965892041994e-13, 1.0893288521968968e-14, 8.189610059960985e-16, 5.717191739445606e-17, 3.725109710537895e-18], [9.463544271597452e-07, 9.249140732592798e-07, 4.519797331537549e-07, 1.4724660022515224e-07, 3.597765511505268e-08, 7.032510988224899e-09, 1.145530715322892e-09, 1.5993969663939e-10, 1.953951818276071e-11, 2.121870673546564e-12, 2.2223975263864638e-13, 1.9341433910601697e-14, 1.5752699611902482e-15, 1.1842931264787773e-16, 8.267586405474024e-18, 5.386852112944669e-19], [1.2441052361049164e-07, 1.2159191191639654e-07, 5.941857896914251e-08, 1.9357469155458035e-08, 4.7297278722254415e-09, 9.245144834028542e-10, 1.5059482157541096e-10, 2.1026140771306267e-11, 2.5687222656207235e-12, 2.789473308873887e-13, 2.7262757443867063e-14, 2.5958520067429884e-15, 2.0708960097301482e-16, 1.556906416296186e-17, 1.0868811136510718e-18, 7.081713497078645e-20], [1.4992424028207566e-08, 1.465275966170236e-08, 7.160395320318356e-09, 2.3327237702189185e-09, 5.699685504133337e-10, 1.1141109894200275e-10, 1.8147833125271256e-11, 2.533811521500766e-12, 3.0955077029863253e-13, 3.361529671954353e-14, 3.285371750836022e-15, 2.9190356757261245e-16, 2.5477745282517522e-17, 1.8761918596555954e-18, 1.309775254633938e-19, 8.53400890160148e-21], [1.6677251932503527e-09, 1.6299416553645264e-09, 7.965070656259005e-10, 2.594872045486797e-10, 6.340208288508127e-11, 1.2393132435669215e-11, 2.018726154554781e-12, 2.818557760509154e-13, 3.443376583038139e-14, 3.7392937334411235e-15, 3.654577290339161e-16, 3.247072873102991e-17, 2.6445900456176314e-18, 2.1306780956430324e-19, 1.4569659886481114e-20, 9.493049034529692e-22], [1.722631715029497e-10, 1.6836042296070995e-10, 8.227304702509729e-11, 2.680303025996201e-11, 6.548946985918345e-12, 1.2801151573801131e-12, 2.0851886820861686e-13, 2.911353146517297e-14, 3.556742881104247e-15, 3.862402512780035e-16, 3.77489694995556e-17, 3.3539762635099106e-18, 2.73165789200161e-19, 2.0536693678489472e-20, 1.5364036285877196e-21, 9.80558871773075e-23], [1.6607228627712332e-11, 1.6230979678201166e-11, 7.931627462350086e-12, 2.583976874215735e-12, 6.313587455578178e-13, 1.2341096998813507e-13, 2.0102500652456762e-14, 2.806723392956604e-15, 3.4289187689473754e-16, 3.723593442658189e-17, 3.639232701163433e-18, 3.2334392856035197e-19, 2.6334861218080305e-20, 1.9798635088413502e-21, 1.3821487488540429e-22, 9.650867663916119e-24]] |
| Legacy trial inputs | {"lambda_home": 1.4460922044002902, "lambda_away": 0.9773442662863495, "rho": -0.01984634636300814, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4620 |
| Legacy p draw | 0.2811 |
| Legacy p away | 0.2569 |
| Legacy p over 1 5 | 0.6980 |
| Legacy p under 3 5 | 0.7748 |
| Legacy p btts yes | 0.4821 |
| Legacy p over 2 5 | 0.4326 |
| Legacy goal margin distribution | {"-1": 0.16434741797857882, "-10": 2.2446169320151666e-08, "-11": 1.9733893857745885e-09, "-12": 1.5929075845540802e-10, "-13": 1.1882364779947659e-11, "-14": 8.208945386915986e-13, "-15": 4.88807922771858e-14, "-2": 0.0672751334569815, "-3": 0.019739316712814512, "-4": 0.004517703497402899, "-5": 0.0008445478209146805, "-6": 0.00013319517580484246, "-7": 1.8147470449452605e-05, "-8": 2.1749983950696042e-06, "-9": 2.325847755561579e-07, "0": 0.28109995582901914, "1": 0.23281147861675439, "10": 1.0753728939589645e-06, "11": 1.3988722472682545e-07, "12": 1.6707222707471405e-08, "13": 1.8440172436734129e-09, "14": 1.8849415118115086e-10, "15": 1.6607228627712332e-11, "2": 0.14030853659285716, "3": 0.06091300960257411, "4": 0.020627380612385622, "5": 0.005705569752292554, "6": 0.0013314096006826134, "7": 0.00026840320796419693, "8": 4.7596932080194266e-05, "9": 7.530949210938853e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4768 |
| Legacy raw p draw | 0.2707 |
| Legacy raw p away | 0.2525 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4461 |
| Legacy lambda away | 0.9773 |
| Legacy model home team | La Coruna |
| Legacy model away team | Osasuna |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 95/100 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 9.68675382627685, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,438.5249 |
| Elo away rating | 1,412.0509 |
| Elo rating diff | 86.4740 |
| Elo home expectancy | 0.6219 |

</details>


---
