# Ligue 1 — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,756 |
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
| Training sha256 | 47b25ac334e6029623ac9a98dd81bd03d80ab2d781f8f78ce52f1d10b87f3ef8 |
| Training as of utc | 2026-11-01T07:26:21.225636+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 76, 'bbs_added_results': 4, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 76, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 134, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-01T07:26:21.225636+00:00', 'observations': 462, 'observations_sha256': 'fad4edfd2cff03c9620cae8d9fa11469dc7b5cfbfd352bf74a0a68c8c62cd190', 'eligible_training_matches': 176, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 173, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 19, 'retrospective_eligible_training_matches': 176, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'c4783747d26d9f9fbf43cad53b735a1f684b3a12eed1526f37dd9a5b35168d9c', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 116, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-08-31T00:00:00+00:00', 'audit_origin_utc': '2025-10-04T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 27, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1750, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1465, 'tuning_matches': 188, 'audit_matches': 92, 'audit_matchdays': 31, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8740131822149474, 'audit_candidate_poisson_score': 0.8703668995751509, 'audit_gain': 0.0036462826397964943, 'audit_gain_lower95': -0.0020867462877964963, 'audit_baseline_briers': [0.5996494886937357, 0.1768950345442525, 0.21631319722812875, 0.2479498473881944], 'audit_candidate_briers': [0.597548154604849, 0.17562674277341245, 0.21497744296277202, 0.24618847014556947], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1592.126 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.196 |
| Dixon-Coles low-score adjustment | -0.053 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1756, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-31'} |
| Training data health | {'training_end': '2026-10-31', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 16.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261101T072621225636Z_2f02dfe0b4e7d28e09c54b35f86142b13bd5e2429df03e627c0d41f877834ca8.json |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 3, 'ANCHORED_MAIN': 2} |
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

## 2026-11-01 — Lyon vs Angers

The model's most likely 1X2 outcome is **Lyon win** at **68.5%**. Expected goals are 2.05 for Lyon and 0.74 for Angers (2.79 combined). The most likely exact score is 2-0 at 11.8%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 58.5%; Under 3.5 goals: 63.9%; Double Chance 1X: 87.7%; Double Chance X2: 31.5%; Double Chance 12 (either team wins): 80.8%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 50.0%; BTTS No (at least one team does not score): 50.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 68.5% | 1.46 |
| Draw | 19.2% | 5.20 |
| Angers win | 12.3% | 8.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 2.05 |
| Angers expected goals | 0.74 |
| Expected total goals | 2.79 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 81.1% |
| Under 1.5 | 18.9% |
| Over 2.5 | 58.5% |
| Under 2.5 | 41.5% |
| Over 3.5 | 36.1% |
| Under 3.5 | 63.9% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.76% |
| 2 | 1-0 | 10.05% |
| 3 | 2-1 | 9.48% |
| 4 | 1-1 | 9.15% |
| 5 | 3-0 | 8.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 68.5% | 68.9% | 1.43 | -2.0% |
| Draw | 19.2% | 18.6% | 5.03 | -3.3% |
| Angers win | 12.3% | 12.5% | 7.40 | -9.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:15:00+00:00 |
| Fixture id | 961df571fad52d969150e9ced52b16f7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:26:52Z |
| Market best draw last update utc | 2026-11-01T07:26:52Z |
| Market best away last update utc | 2026-11-01T07:26:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lyon |
| Matched away-team name | Angers |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0503 |
| Dc lambda away | 0.7372 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:26:21.225636+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.97 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.29 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.22 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.08566811158915848, "-10": 1.8923875461134335e-09, "-11": 1.3675441701502716e-10, "-12": 9.077546244940915e-12, "-13": 5.570978093379583e-13, "-14": 3.178834919997184e-14, "-15": 1.6944278414575454e-15, "-16": 8.435878435007318e-17, "-17": 3.6141600277061746e-18, "-2": 0.02884144619548163, "-3": 0.006802632582867451, "-4": 0.0012624388551544785, "-5": 0.00019231206356344431, "-6": 2.4790272000964265e-05, "-7": 2.7662171531204224e-06, "-8": 2.718966859883759e-07, "-9": 2.386872674360481e-08, "0": 0.1921861606108313, "1": 0.22849793612725924, "10": 4.8494526886889004e-05, "11": 9.74664363427826e-06, "12": 1.7993401644667925e-06, "13": 3.071194591518957e-07, "14": 4.873881189157618e-08, "15": 7.225387130118099e-09, "16": 1.0004593203669761e-09, "17": 1.1920859777712544e-10, "2": 0.20646718838201814, "3": 0.13543849043945336, "4": 0.06990472342864289, "5": 0.029616502934684402, "6": 0.010617924178820293, "7": 0.003295153704074941, "8": 0.0009007917518273875, "9": 0.0002199281487740112} |
| Raw goal margin distribution | {"-1": 0.08457870692289243, "-10": 9.223832974309357e-10, "-11": 6.112462882013064e-11, "-12": 3.719434035959067e-12, "-13": 2.0920037874305884e-13, "-14": 1.0937885954885366e-14, "-15": 5.341703548073165e-16, "-16": 2.439390114422898e-17, "-17": 9.71480494916293e-19, "-2": 0.026925796434609645, "-3": 0.005921032317010834, "-4": 0.0010179118936954141, "-5": 0.00014311775928969975, "-6": 1.6989143837338666e-05, "-7": 1.743143013814713e-06, "-8": 1.573841977645748e-07, "-9": 1.2681685501141099e-08, "0": 0.20617996592454468, "1": 0.24402151057109345, "10": 2.5540078280190682e-05, "11": 4.70715076139698e-06, "12": 7.96617446620123e-07, "13": 1.2461390296624926e-07, "14": 1.8120430124862517e-08, "15": 2.4611947096708185e-09, "16": 3.125924826878878e-10, "17": 3.462281977169019e-11, "2": 0.20827191817537372, "3": 0.12737689838262156, "4": 0.06090241389463091, "5": 0.02381490892996863, "6": 0.007862451321500631, "7": 0.002243626574865555, "8": 0.0005633908116557023, "9": 0.00012625735683340222} |
| Unadjusted home-win probability | 67.5% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 11.9% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 45.9% |
| P home draw | 87.7% |
| P draw away | 31.5% |
| P home away | 80.8% |
| Raw p home draw | 88.1% |
| Raw p draw away | 32.5% |
| Raw p home away | 79.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0929 |
| Totals anchor target over 2 5 | 0.5853 |
| Totals anchor reference over odds | 1.66 |
| Totals anchor reference under odds | 2.30 |
| Totals anchor reference last update utc | 2026-11-01T07:26:52Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5331 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:48Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.93, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:48Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.15, "price": 5.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.67, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.2, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.78, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.89, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.43 |
| Reference draw odds | 5.03 |
| Reference away odds | 7.40 |
| Market reference 1x2 last update utc | 2026-11-01T07:26:52Z |
| Market reference home last update utc | 2026-11-01T07:26:52Z |
| Market reference draw last update utc | 2026-11-01T07:26:52Z |
| Market reference away last update utc | 2026-11-01T07:26:52Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-01T07:26:52Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:26:52Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.0140 |
| Raw ev home | -0.0344 |
| Raw edge prob draw | 0.0200 |
| Raw ev draw | 0.0371 |
| Raw edge prob away | -0.0060 |
| Raw ev away | -0.1223 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0553769255965892, 0.037106576116174836, 0.017546137874721795, 0.004820312252206951, 0.0009931848125785138, 0.0001637099043092063, 2.2487366256427672e-05, 2.647618716348154e-06, 2.727597882659647e-07, 2.4977716058756928e-08, 2.0585793570611834e-09, 1.5423744324558117e-10, 1.059310947420584e-11, 6.715757369609535e-13, 3.9535009799444134e-14, 2.1722283671546e-15, 1.118923479865022e-16, 5.4245829559407235e-18], [0.10744487200729116, 0.09300930422261382, 0.03728977947054571, 0.010244327392578223, 0.0021107575296045182, 0.0003479230741500848, 4.779108283331409e-05, 5.626829035519441e-06, 5.796804074772401e-07, 5.30836774542171e-08, 4.374978174428966e-09, 3.277918072793968e-10, 2.2512915321927926e-11, 1.4272605919232947e-12, 8.402144148833156e-14, 4.616509761248127e-15, 2.3779825569872783e-16, 1.1528548538201765e-17], [0.12016232621485638, 0.09903374818596843, 0.03840507966510693, 0.010885834592798372, 0.002242934694709685, 0.0003697102690177252, 5.0783795050428486e-05, 5.979185144648539e-06, 6.159804143954698e-07, 5.640781577936622e-08, 4.648942476051686e-09, 3.483183676366197e-10, 2.392269038314144e-11, 1.5166366838053828e-12, 8.928292500228974e-14, 4.905598945753577e-15, 2.5268935468303444e-16, 1.2250474596588174e-17], [0.08512465206897307, 0.07015687547811952, 0.028910468690458085, 0.007474279381527279, 0.0015889259264105738, 0.0002619078625374455, 3.597594204925844e-05, 4.2357373656707026e-06, 4.3636903602348333e-07, 3.996007603584173e-08, 3.2933750804305108e-09, 2.4675354404577124e-10, 1.6947164386427383e-11, 1.0744063808579344e-12, 6.324925761615687e-14, 3.475194069566585e-15, 1.79008630046538e-16, 8.678405458377618e-18], [0.04522760971421565, 0.03727507491393021, 0.015360431588344499, 0.004219850380359425, 0.0008182245598147389, 0.00013915436128103198, 1.9114390797001104e-05, 2.250491153505698e-06, 2.3184739053790643e-07, 2.1231202468058834e-08, 1.749804306507418e-09, 1.3110271483587508e-10, 9.004204046683737e-12, 5.708432432538198e-13, 3.3604985966457567e-14, 1.846406619461562e-15, 9.510914004865788e-17, 4.610926746522168e-18], [0.019223918155262455, 0.015843706839794424, 0.0065289251753454895, 0.0017936401868698573, 0.0003695644803952315, 5.7326531898279375e-05, 8.124539116506871e-06, 9.565674157336135e-07, 9.854633681450082e-08, 9.024286296860903e-09, 7.437513277526025e-10, 5.572498471316313e-11, 3.827221529956838e-12, 2.4263594421941747e-13, 1.4283741809704155e-14, 7.848119756527238e-16, 4.042597731045054e-17, 1.959866527440914e-18], [0.006809244610674028, 0.005611950412015086, 0.002312590399348187, 0.0006353197447726645, 0.00013090229193151815, 2.1577053348538315e-05, 2.7891786654140605e-06, 3.3882278668292456e-07, 3.4905793264216395e-08, 3.1964645467062782e-09, 2.634418581726385e-10, 1.97381745372302e-11, 1.3556283046065862e-12, 8.594332758744085e-14, 5.0594000220169715e-15, 2.779858233084944e-16, 1.4319160428648722e-17, 6.941982629053318e-19], [0.002067326982691278, 0.0017038213745615165, 0.00070211613854948, 0.00019288683636745635, 3.9742710928895614e-05, 6.55092115863744e-06, 8.99841485051662e-07, 9.970189687107555e-08, 1.0597605519155367e-08, 9.704655632818882e-10, 7.998250803281303e-11, 5.992626663157387e-12, 4.115767802231754e-13, 2.609290314307049e-14, 1.536063804397413e-15, 8.439814196576699e-17, 4.3473818927325114e-18, 2.107627031039418e-19], [0.0005491961238741315, 0.0004526289757341284, 0.00018652078990371792, 5.124138743714651e-05, 1.0557857067189935e-05, 1.7402861464349108e-06, 2.39047552626712e-07, 2.8144993380485184e-08, 2.728642338472526e-09, 2.5780920491537455e-10, 2.124776765220219e-11, 1.5919723211595517e-12, 1.0933750406571173e-13, 6.931714908563851e-15, 4.080633080598597e-16, 2.2420803684106747e-17, 1.1549045238025728e-18, 5.599020405143359e-20], [0.00012968604063923352, 0.00010688287333033693, 4.4044634854450166e-05, 1.2100035606055201e-05, 2.493110605042465e-06, 4.1094758338494453e-07, 5.6448196330974345e-08, 6.646100721878174e-09, 6.846865881784279e-10, 5.900444926050075e-11, 5.017404055582916e-12, 3.759250624022061e-13, 2.5818732833788205e-14, 1.6368408702345816e-15, 9.63592284284942e-17, 5.294402366189574e-18, 2.727167736577499e-19, 1.3221411372665396e-20], [2.7561414884424602e-05, 2.2715191252477954e-05, 9.360548357193368e-06, 2.5715497196997973e-06, 5.298461993259936e-07, 8.733628373258874e-08, 1.1996604652951134e-08, 1.412456872431824e-09, 1.4551243163543584e-10, 1.3325161393897156e-11, 1.0334939235502651e-12, 7.989315241062208e-14, 5.487104116330575e-15, 3.4786820618432723e-16, 2.0478662619123256e-17, 1.1251883353086585e-18, 5.795889910489744e-20, 2.809869145541943e-21], [5.3249692080623534e-06, 4.388660541627258e-06, 1.8084932134888807e-06, 4.968330955368031e-07, 1.0236828218910525e-07, 1.6873699103359407e-08, 2.317789222583157e-09, 2.7289198994155845e-10, 2.811355008798383e-11, 2.5744713909829793e-12, 2.1217927405192485e-13, 1.496048674409593e-14, 1.060129190878529e-15, 6.720944821458502e-17, 3.956554782343696e-18, 2.173906261312982e-19, 1.1197877698259348e-20, 5.428773066055783e-22], [9.43070439365091e-07, 7.772469404987763e-07, 3.2029039470340037e-07, 8.79908572972775e-08, 1.8129776359074616e-08, 2.988390393511767e-09, 4.1048847703901595e-10, 4.833011399648004e-11, 4.979006825700493e-12, 4.559477756512024e-13, 3.7577682308725893e-14, 2.815478364976303e-15, 1.8197276666275564e-16, 1.190302542242829e-17, 7.007195180222775e-19, 3.8500630762162896e-20, 1.9831828181963714e-21, 9.61454461157637e-23], [1.5417326049932317e-07, 1.2706441642948126e-07, 5.236110941117284e-08, 1.4384755154434638e-08, 2.9638578591052657e-09, 4.885423944819482e-10, 6.710670196079235e-11, 7.90101242083012e-12, 8.139685906001105e-13, 7.453839316274707e-14, 6.143203690537029e-15, 4.602747167920272e-16, 3.161191187164419e-17, 1.886005087286849e-18, 1.1455370487674277e-19, 6.294087406534942e-21, 3.2421094807447837e-22, 1.57178682430219e-23], [2.340395738905548e-08, 1.928875460082675e-08, 7.948571428883681e-09, 2.1836484199402556e-09, 4.499223978078959e-10, 7.416218186066606e-11, 1.0186996033707964e-11, 1.199397077214424e-12, 1.23562841887995e-13, 1.1315148760424999e-14, 9.325565077885099e-16, 6.987106469806727e-17, 4.7987818123220255e-18, 3.0423035275641687e-19, 1.6854270312859373e-20, 9.554611025832278e-22, 4.9216181776435107e-23, 2.386018933601575e-24], [3.3159373533068377e-09, 2.732884051034918e-09, 1.1261755637441195e-09, 3.093853420514013e-10, 6.374624855872678e-11, 1.0507502852894314e-11, 1.4433217470288722e-12, 1.699338921050249e-13, 1.7506724870758487e-14, 1.6031615426911798e-15, 1.3212718288794045e-16, 9.899525515970456e-18, 6.799046672888457e-19, 4.310419703577452e-20, 2.537502113935956e-21, 1.3120506577628122e-22, 6.97308462952242e-24, 3.3805775562241843e-25], [4.4044796896977257e-10, 3.6300240368166896e-10, 1.4958718663964668e-10, 4.109490952827074e-11, 8.467260601028435e-12, 1.3956862863787467e-12, 1.9171295000938634e-13, 2.2571909436752483e-14, 2.325376082557331e-15, 2.1294408493713123e-16, 1.7550135345788608e-17, 1.314930121621678e-18, 9.031009874230591e-20, 5.725426633753114e-21, 3.3705029174481392e-22, 1.8519034359670574e-23, 8.97705331429593e-25, 4.490339713742952e-26], [5.50622517361347e-11, 4.538045612764259e-11, 1.870052289381237e-11, 5.137447355727542e-12, 1.0585278343315044e-12, 1.7448060851548993e-13, 2.3966841620782444e-14, 2.8218092649599568e-15, 2.9070503727931996e-16, 2.6621035029301853e-17, 2.1940161801026885e-18, 1.6438494095344098e-19, 1.1290045003261893e-20, 7.1575964657500745e-22, 4.213607354167242e-23, 2.3151423179619434e-24, 1.1925390248862287e-25, 5.4407544776021095e-27]] |
| Legacy trial inputs | {"lambda_home": 2.1252414483912156, "lambda_away": 0.8241663698228597, "rho": -0.06047613688333437, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6785 |
| Legacy p draw | 0.1951 |
| Legacy p away | 0.1263 |
| Legacy p over 1 5 | 0.8001 |
| Legacy p under 3 5 | 0.6569 |
| Legacy p btts yes | 0.4972 |
| Legacy p over 2 5 | 0.5694 |
| Legacy goal margin distribution | {"-1": 0.08701874468962681, "-10": 2.411402665432445e-09, "-11": 1.7833213203572568e-10, "-12": 1.2113225254207567e-11, "-13": 7.606863969518318e-13, "-14": 4.441288732083367e-14, "-15": 2.422277097449916e-15, "-16": 1.2342089652470398e-16, "-17": 5.4245829559407235e-18, "-2": 0.03031541468064796, "-3": 0.0073391083084339715, "-4": 0.0013963685603670126, "-5": 0.00021793853643376873, "-6": 2.877194269380427e-05, "-7": 3.2871353321236445e-06, "-8": 3.307484137252364e-07, "-9": 2.9718545174583202e-08, "0": 0.19514403162680793, "1": 0.24000100948252606, "10": 3.2285211200345116e-05, "11": 6.1568260722939295e-06, "12": 1.078401454306717e-06, "13": 1.7463034410125662e-07, "14": 2.629156607408577e-08, "15": 3.697640279882319e-09, "16": 4.858284250974152e-10, "17": 5.50622517361347e-11, "2": 0.2076109725230587, "3": 0.12960551278932567, "4": 0.06358777486892743, "5": 0.025591808907097693, "6": 0.00871223394915842, "7": 0.0025666775679959604, "8": 0.0006659550073352342, "9": 0.00015430075544872296} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6679 |
| Legacy raw p draw | 0.2041 |
| Legacy raw p away | 0.1280 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1252 |
| Legacy lambda away | 0.8242 |
| Legacy model home team | Lyon |
| Legacy model away team | Angers |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 87.4% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:26:48Z |
| Market reference home draw last update utc | 2026-11-01T07:26:58Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 31.8% |
| Market draw away odds | 3.04 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:26:48Z |
| Market reference draw away last update utc | 2026-11-01T07:26:58Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.8% |
| Market home away odds | 1.20 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:26:48Z |
| Market reference home away last update utc | 2026-11-01T07:26:58Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.02 |
| Market reference dc home draw odds | 1.10 |
| Market reference dc home away odds | 1.19 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.23, "price": 1.63, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.63, "price": 2.23, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.02, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.02, "price": 1.78, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 81.7% |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.95 |
| Market reference over 1 5 last update utc | 2026-11-01T07:26:33Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:26:52Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.66 |
| Market reference under 3 5 last update utc | 2026-11-01T07:26:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 50.9% |
| Market btts yes odds | 1.91 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:26:48Z |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 1.89 |
| Market reference btts yes last update utc | 2026-11-01T07:26:52Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015445853721645362, "mu": 9.904716561450385, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,581.6014 |
| Elo away rating | 1,418.6457 |
| Elo rating diff | 222.9557 |
| Elo home expectancy | 0.7830 |

</details>


---

## 2026-11-01 — Marseille vs Toulouse

The model's most likely 1X2 outcome is **Marseille win** at **51.9%**. Expected goals are 1.96 for Marseille and 1.16 for Toulouse (3.12 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 65.5%; Under 3.5 goals: 56.1%; Double Chance 1X: 75.0%; Double Chance X2: 48.1%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 74.8%; BTTS Yes (both teams score): 64.4%; BTTS No (at least one team does not score): 35.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 51.9% | 1.93 |
| Draw | 23.1% | 4.34 |
| Toulouse win | 25.0% | 3.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 1.96 |
| Toulouse expected goals | 1.16 |
| Expected total goals | 3.12 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 85.6% |
| Under 1.5 | 14.4% |
| Over 2.5 | 65.5% |
| Under 2.5 | 34.5% |
| Over 3.5 | 43.9% |
| Under 3.5 | 56.1% |
| Over 4.5 | 25.2% |
| Under 4.5 | 74.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.13% |
| 2 | 2-1 | 8.75% |
| 3 | 2-0 | 6.92% |
| 4 | 1-2 | 6.61% |
| 5 | 2-2 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 51.9% | 50.3% | 1.94 | +0.7% |
| Draw | 23.1% | 23.1% | 4.11 | -5.3% |
| Toulouse win | 25.0% | 26.5% | 3.60 | -9.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T19:45:00+00:00 |
| Fixture id | df1e1589c51bbcac432125567d1f7c58 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:26:52Z |
| Market best draw last update utc | 2026-11-01T07:26:52Z |
| Market best away last update utc | 2026-11-01T07:26:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Marseille |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9617 |
| Dc lambda away | 1.1562 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:26:21.225636+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 64.4% |
| P btts no | 35.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.64 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.94 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.28 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.96 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.14694488659389643, "-10": 1.4144717440428055e-07, "-11": 1.5934336187613043e-08, "-12": 1.6504124189372364e-09, "-13": 1.581694550766463e-10, "-14": 1.4102278100079556e-11, "-15": 1.174723802570113e-12, "-16": 9.097525291910886e-14, "-17": 5.834656112197836e-15, "-2": 0.07003287597146715, "-3": 0.024575283371944787, "-4": 0.0069043469644766925, "-5": 0.0016087322565509828, "-6": 0.000319267052202315, "-7": 5.508640103194568e-05, "-8": 8.39779864185113e-06, "-9": 1.1459012503054087e-06, "0": 0.23053160352792118, "1": 0.197523848674269, "10": 2.1821729592855762e-05, "11": 4.171008087187079e-06, "12": 7.330130415441687e-07, "13": 1.1919389162714224e-07, "14": 1.8031539951513612e-08, "15": 2.5485401199931858e-09, "16": 3.3488148767849957e-10, "17": 3.644142032603008e-11, "2": 0.15728943590850225, "3": 0.0936501096603961, "4": 0.04464209078910162, "5": 0.01764890847455313, "6": 0.0059429263200641135, "7": 0.0017398139370555532, "8": 0.000450024362834421, "9": 0.00010419093235774944} |
| Raw goal margin distribution | {"-1": 0.13044185077473586, "-10": 6.38593831142389e-08, "-11": 6.600335439196766e-09, "-12": 6.269321901089835e-10, "-13": 5.507785538161455e-11, "-14": 4.4986183575235085e-12, "-15": 3.407317031265851e-13, "-16": 2.1564891837067837e-14, "-2": 0.05933050433829957, "-3": 0.01952792061393547, "-4": 0.005104431349942344, "-5": 0.0011011951264446795, "-6": 0.0002017169015011355, "-7": 3.2057876296754366e-05, "-8": 4.4949376543810085e-06, "-9": 5.635250822701721e-07, "0": 0.22873747695832025, "1": 0.22503284470125437, "10": 1.262834226610491e-05, "11": 2.214622945510232e-06, "12": 3.569164129610325e-07, "13": 5.3202878988987785e-08, "14": 7.373088152736447e-09, "15": 9.475343910758318e-10, "16": 1.0175174933894327e-10, "2": 0.17080570218465402, "3": 0.09538772444323965, "4": 0.0423054206215102, "5": 0.015485495033452562, "6": 0.0048129933718548835, "7": 0.00129783620825322, "8": 0.00030875995750935173, "9": 6.56784225917624e-05} |
| Unadjusted home-win probability | 55.6% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 21.6% |
| Raw p over 1 5 | 82.3% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 59.4% |
| P home draw | 75.0% |
| P draw away | 48.1% |
| P home away | 76.9% |
| Raw p home draw | 78.4% |
| Raw p draw away | 44.4% |
| Raw p home away | 77.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0934 |
| Totals anchor target over 2 5 | 0.6546 |
| Totals anchor reference over odds | 1.49 |
| Totals anchor reference under odds | 2.72 |
| Totals anchor reference last update utc | 2026-11-01T07:26:52Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6003 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.88, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.14, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.22, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.46, "price": 1.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.79, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.52, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 6.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:05Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.57, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.57, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.94 |
| Reference draw odds | 4.11 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-11-01T07:26:52Z |
| Market reference home last update utc | 2026-11-01T07:26:52Z |
| Market reference draw last update utc | 2026-11-01T07:26:52Z |
| Market reference away last update utc | 2026-11-01T07:26:52Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.55 |
| Market reference over 2 5 last update utc | 2026-11-01T07:26:06Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:26:06Z |
| Home probability edge | +1.6% |
| Draw probability edge | -0.1% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | 0.0521 |
| Raw ev home | 0.0777 |
| Raw edge prob draw | -0.0026 |
| Raw ev draw | -0.0599 |
| Raw edge prob away | -0.0496 |
| Raw ev away | -0.2233 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.058447312349974606, 0.05678284507867531, 0.03354951591993072, 0.01169602524335595, 0.0030580994108759837, 0.0006396683873173095, 0.0001115005298928242, 1.6659124919201696e-05, 2.177887745670706e-06, 2.530849239012679e-07, 2.646912401710887e-08, 2.5166346803968783e-09, 2.1933716436084786e-10, 1.7645833037855818e-11, 1.3182185643582917e-12, 9.191141619921692e-14, 6.0079010151604775e-15], [0.08827927323754946, 0.10998055025810113, 0.0637620176238167, 0.02222870128663863, 0.005812023905114534, 0.0012157119370325902, 0.00021191062097762273, 3.166124421081352e-05, 4.13915113271884e-06, 4.809966682269876e-07, 5.0305487450066635e-08, 4.7829514210321705e-09, 4.1685788173253746e-10, 3.3536517183494826e-11, 2.5053200628365233e-12, 1.7468083156582612e-13, 1.141822407587214e-14], [0.08955310096543699, 0.09365995014762506, 0.051535213885726745, 0.02112320855203767, 0.005522976420172476, 0.0011552513326802782, 0.0002013717393374095, 3.0086645902431024e-05, 3.933300082509872e-06, 4.5707541816224256e-07, 4.780366108740657e-08, 4.545082461540658e-09, 3.9612642496976805e-10, 3.186865653738238e-11, 2.3807237991321487e-12, 1.6599348687213733e-13, 1.0850365270485714e-14], [0.056732923913152954, 0.059334660309369916, 0.03102785535448229, 0.011381792392502742, 0.0034988693595402625, 0.0007318650638665684, 0.00012757132296845617, 1.9060237717992298e-05, 2.491791036859289e-06, 2.8956255720479437e-07, 3.028417149160139e-08, 2.8793622408353175e-09, 2.5095066597942554e-10, 2.0189162039710015e-11, 1.508216027120324e-12, 1.0515879136815738e-13, 6.873831734290961e-15], [0.026955721976990754, 0.028191894522252132, 0.014742378583519516, 0.005139484947308011, 0.0014139685938574433, 0.00034773372894475604, 6.0613430032950476e-05, 9.056160573145391e-06, 1.1839338038906237e-06, 1.3758091860217564e-07, 1.4389029345301524e-08, 1.3680819298828278e-09, 1.1923510927159832e-10, 9.592550521879034e-12, 7.166042062371396e-13, 4.996448178654944e-14, 3.2659888538409344e-15], [0.010246056747057454, 0.010715934499124865, 0.005603680275463663, 0.0019535538490015316, 0.0005107856515733652, 0.00011242136158348647, 2.3039584852579e-05, 3.4423093999157938e-06, 4.500214444182788e-07, 5.2295460700828675e-08, 5.469369781038715e-09, 5.200174233941327e-10, 4.5322091423899526e-11, 3.646194937018728e-12, 2.7238622540153793e-13, 1.899184581883179e-14, 1.2414249991254399e-15], [0.0032454976520858063, 0.003394334143894238, 0.0017749980920493999, 0.0006187994646797664, 0.00016179430524592426, 3.3842818171872014e-05, 6.207195534605668e-06, 1.0903713839363693e-06, 1.4254689167783869e-07, 1.6564889216334664e-08, 1.73245446721228e-09, 1.6471852228947104e-10, 1.435603422225116e-11, 1.1549533053815986e-12, 8.627991009859371e-14, 6.0157768530313786e-15, 3.9322853848719237e-16], [0.0008811686795133867, 0.0009215785238606639, 0.0004819207691938267, 0.00016800711805322984, 4.39279548437546e-05, 9.18849267395239e-06, 1.6016451998804304e-06, 2.517957715720865e-07, 3.8702186774892175e-08, 4.49744942741288e-09, 4.703699644365517e-10, 4.472189424753653e-11, 3.897734361490024e-12, 3.135755400558268e-13, 2.342542272407766e-14, 1.633313196953349e-15, 1.0676349489362602e-16], [0.0002093364514065538, 0.0002189364900986027, 0.00011448839027944585, 3.991291874301213e-05, 1.043582505635259e-05, 2.1828810928714914e-06, 3.8049777568179707e-07, 5.684959508851071e-08, 7.820194324216335e-09, 1.068444811310099e-09, 1.1174430218939568e-10, 1.062443872509003e-11, 9.259724031615628e-13, 7.449514755725406e-14, 5.565103458358187e-15, 3.880210414134602e-16, 2.5363465225676883e-17], [4.420568668891809e-05, 4.623293182358419e-05, 2.4176572575899258e-05, 8.428431689458751e-06, 2.2037385733913354e-06, 4.6096012912359504e-07, 8.034991204161186e-08, 1.2004958391092142e-08, 1.5694372840142661e-09, 1.9190293297882548e-10, 2.3597102074987967e-11, 2.2435682193485107e-12, 1.9553807118497402e-13, 1.5731178830222566e-14, 1.1751857749504898e-15, 8.193860395635864e-17, 5.356016066853222e-18], [8.401443944701579e-06, 8.786728907718248e-06, 4.594841399044407e-06, 1.6018526502945538e-06, 4.1882815266311305e-07, 8.760706994164032e-08, 1.5270779226432282e-08, 2.281583943961667e-09, 2.9827699452242715e-10, 3.466175454188046e-11, 3.814439215811745e-12, 4.263979149021059e-13, 3.7162688042293444e-14, 2.9897650511856735e-15, 2.2334812899382804e-16, 1.5572715630250024e-17, 1.0179294141327973e-18], [1.4515668508006223e-06, 1.5181347984186803e-06, 7.93877755233434e-07, 2.767614974686697e-07, 7.236340164731435e-08, 1.5136388394670616e-08, 2.6384222827509727e-09, 3.942026682761304e-10, 5.153506950174304e-11, 5.988715060738139e-12, 6.263353786638232e-13, 6.266058059988924e-14, 6.42081604113517e-15, 5.165592805889397e-16, 3.8589169001150556e-17, 2.6905896099052756e-18, 1.7587364787953143e-19], [2.2989609185367686e-07, 2.4043898279367793e-07, 1.2573268205806158e-07, 4.3832901397910023e-08, 1.1460762708090053e-08, 2.397269223112127e-09, 4.1786774830904346e-10, 6.243298597304599e-11, 8.162015456142203e-12, 9.484800420521997e-13, 9.919767433727622e-14, 9.431528874568798e-15, 8.6493009561753e-16, 8.181156779148264e-17, 6.111671078980915e-18, 4.2612989939675368e-19, 2.785449687367347e-20], [3.360965302611914e-08, 3.5150970686321825e-08, 1.8381486105054976e-08, 6.408149852540812e-09, 1.6755058988943466e-09, 3.50468710230509e-10, 6.109016433568404e-11, 9.127388721658595e-12, 1.1932456322457206e-12, 1.3866301448857567e-13, 1.450220135797621e-14, 1.3788421126438186e-15, 1.2017291243913157e-16, 1.0172867560639667e-17, 8.934955906299389e-19, 6.22980492939201e-20, 4.0721874286455496e-21], [4.562593591293314e-09, 4.771831278844651e-09, 2.4953322379197135e-09, 8.699222043895629e-10, 2.27454073105979e-10, 4.757699491880753e-11, 8.293141023277976e-12, 1.2390656117252698e-12, 1.619860481836015e-13, 1.8823847445355195e-14, 1.9687097312229455e-15, 1.8718122979921892e-16, 1.631377032413077e-17, 1.3124545865102099e-18, 1.0316595563372326e-19, 8.457114396201066e-21, 5.528095232058623e-22], [5.780911487618629e-10, 6.046020471665882e-10, 3.161643593929254e-10, 1.1022115303643862e-10, 2.8818956538955766e-11, 6.028115171102606e-12, 1.0507601269022809e-12, 1.5699247556049386e-13, 2.0524006533597196e-14, 2.3850249591743405e-15, 2.494400711632803e-16, 2.3716294251536894e-17, 2.0669923890022987e-18, 1.6629102821283636e-19, 1.2422645052014262e-20, 9.1138730236057e-22, 7.00422437199777e-23], [6.866764132956686e-11, 7.181669639965266e-11, 3.75550825825374e-11, 1.3092445057925049e-11, 3.42321409927794e-12, 7.160401112335834e-13, 1.2481287712512365e-13, 1.864810251171929e-14, 2.4379116032362852e-15, 2.833014115670417e-16, 2.9629343705654284e-17, 2.817102442787721e-18, 2.455244165266105e-19, 1.975261635833792e-20, 1.4756042133203981e-21, 1.028849666229904e-22, 7.076395449955459e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9005346537932513, "lambda_away": 1.0458593743590532, "rho": -0.06047613688333437, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5351 |
| Legacy p draw | 0.2329 |
| Legacy p away | 0.2320 |
| Legacy p over 1 5 | 0.7965 |
| Legacy p under 3 5 | 0.6624 |
| Legacy p btts yes | 0.5595 |
| Legacy p over 2 5 | 0.5634 |
| Legacy goal margin distribution | {"-1": 0.14553884409391277, "-10": 3.1669127014431127e-08, "-11": 2.9669206406007042e-09, "-12": 2.553628301236968e-10, "-13": 2.0324020419298768e-11, "-14": 1.5037497611946036e-12, "-15": 1.0332964027508906e-13, "-16": 6.0079010151604775e-15, "-2": 0.062097261588407913, "-3": 0.018800395032218968, "-4": 0.004495481332346858, "-5": 0.0008843006642145486, "-6": 0.0001473995604653789, "-7": 2.1287050224367794e-05, "-8": 2.709690406468731e-06, "-9": 3.081963155381422e-07, "0": 0.23287772584902758, "1": 0.21865285225623995, "10": 1.0051953182032015e-05, "11": 1.711286776900395e-06, "12": 2.676560391450541e-07, "13": 3.8710741109414636e-08, "14": 5.204750721042439e-09, "15": 6.499078451615156e-10, "16": 6.866764132956686e-11, "2": 0.1657550693123482, "3": 0.09119349169547936, "4": 0.03962557414468828, "5": 0.014164518626599454, "6": 0.00429042738961597, "7": 0.001125958417859091, "8": 0.0002604528058106408, "9": 5.383185040556973e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5669 |
| Legacy raw p draw | 0.2345 |
| Legacy raw p away | 0.1987 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9005 |
| Legacy lambda away | 1.0459 |
| Legacy model home team | Marseille |
| Legacy model away team | Toulouse |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 73.0% |
| Market home draw odds | 1.32 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:26:48Z |
| Market reference home draw last update utc | 2026-11-01T07:26:58Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.5% |
| Market draw away odds | 1.93 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:26:48Z |
| Market reference draw away last update utc | 2026-11-01T07:26:58Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.5% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:26:48Z |
| Market reference home away last update utc | 2026-11-01T07:26:58Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.91 |
| Market reference dc home draw odds | 1.32 |
| Market reference dc home away odds | 1.26 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.26, "price": 1.62, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.62, "price": 2.26, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.04, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.04, "price": 1.76, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 84.6% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-11-01T07:26:33Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.5% |
| Market under 3 5 odds | 1.69 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:26:52Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.25 |
| Market reference under 3 5 last update utc | 2026-11-01T07:26:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.2% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:26:48Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.61 |
| Market reference btts yes last update utc | 2026-11-01T07:26:52Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015445853721645362, "mu": 9.522920976038039, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,566.8488 |
| Elo away rating | 1,531.5216 |
| Elo rating diff | 95.3273 |
| Elo home expectancy | 0.6338 |

</details>


---

## 2026-11-01 — Paris FC vs AS Monaco

The model's most likely 1X2 outcome is **Paris FC win** at **38.2%**. Expected goals are 1.52 for Paris FC and 1.50 for AS Monaco (3.02 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 52.7%; Under 3.5 goals: 69.5%; Double Chance 1X: 64.9%; Double Chance X2: 61.8%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 38.2% | 2.61 |
| Draw | 26.7% | 3.75 |
| AS Monaco win | 35.1% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.52 |
| AS Monaco expected goals | 1.50 |
| Expected total goals | 3.02 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.63% |
| 2 | 2-1 | 8.64% |
| 3 | 1-0 | 8.26% |
| 4 | 1-2 | 8.01% |
| 5 | 0-1 | 7.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 38.2% | 38.4% | 2.53 | -3.2% |
| Draw | 26.7% | 27.2% | 3.53 | -5.8% |
| AS Monaco win | 35.1% | 34.3% | 2.82 | -1.1% |
| Over 2.5 | 52.7% | 52.7% | 1.85 | -2.6% |
| Under 2.5 | 47.3% | 47.3% | 2.05 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:15:00+00:00 |
| Fixture id | cf3a2e2b4a4e9815d1d0be8dcef916da |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:26:52Z |
| Market best draw last update utc | 2026-11-01T07:26:52Z |
| Market best away last update utc | 2026-11-01T07:26:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Paris FC |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5228 |
| Dc lambda away | 1.4980 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:26:21.225636+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.65 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.40 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.28 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.67 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.18717769026194658, "-10": 4.957490679505183e-07, "-11": 6.134638167108213e-08, "-12": 6.9713444752248345e-09, "-13": 7.271531315641839e-10, "-14": 6.300239726389596e-11, "-2": 0.10417435283510351, "-3": 0.04177006588681859, "-4": 0.013214451652218248, "-5": 0.00343711702575264, "-6": 0.0007572747116683739, "-7": 0.00014452088176134756, "-8": 2.4306350685597817e-05, "-9": 3.652245786117565e-06, "0": 0.26687530948256594, "1": 0.2017971723468501, "10": 6.192195990892324e-07, "11": 7.78932795658814e-08, "12": 8.998203896805228e-09, "13": 9.540989443741498e-10, "14": 8.403357909023448e-11, "2": 0.11410839615263084, "3": 0.04651041343720302, "4": 0.014957617933665618, "5": 0.0039549031998688, "6": 0.0008857746418767699, "7": 0.00017184173191695098, "8": 2.9379611433235532e-05, "9": 4.487604082992216e-06} |
| Raw goal margin distribution | {"-1": 0.1889007677252972, "-10": 9.391127963008955e-07, "-11": 1.2574687966451967e-07, "-12": 1.547345367963664e-08, "-13": 1.7602924841776937e-09, "-14": 1.8462368424522714e-10, "-15": 1.6003845237461798e-11, "-2": 0.11016295286986273, "-3": 0.04694218061628097, "-4": 0.015889555326195744, "-5": 0.004439657948274051, "-6": 0.0010533889126751771, "-7": 0.00021685497842673988, "-8": 3.938812740845726e-05, "-9": 6.396988012743533e-06, "0": 0.2538261325133448, "1": 0.19212448557638281, "10": 1.1066244339572244e-06, "11": 1.5062878173829434e-07, "12": 1.884196771751588e-08, "13": 2.1789741624926243e-09, "14": 2.3231802597700403e-10, "15": 2.0471425639803182e-11, "2": 0.11383926100741854, "3": 0.04931147680123206, "4": 0.016967768969006633, "5": 0.004819375436071756, "6": 0.0011624070653316967, "7": 0.0002432580072124898, "8": 4.491499250204192e-05, "9": 7.415318066637641e-06} |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 36.8% |
| Raw p over 1 5 | 81.0% |
| Raw p under 3 5 | 64.3% |
| Raw p btts yes | 61.3% |
| P home draw | 64.9% |
| P draw away | 61.8% |
| P home away | 73.3% |
| Raw p home draw | 63.2% |
| Raw p draw away | 62.1% |
| Raw p home away | 74.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9219 |
| Totals anchor target over 2 5 | 0.5267 |
| Totals anchor reference over odds | 1.85 |
| Totals anchor reference under odds | 2.05 |
| Totals anchor reference last update utc | 2026-11-01T07:26:52Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5769 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:55Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.9, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:55Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.76, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:55Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.67, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.93, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:55Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:55Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:25:55Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.03, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 5.03, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.53 |
| Reference draw odds | 3.53 |
| Reference away odds | 2.82 |
| Market reference 1x2 last update utc | 2026-11-01T07:26:52Z |
| Market reference home last update utc | 2026-11-01T07:26:52Z |
| Market reference draw last update utc | 2026-11-01T07:26:52Z |
| Market reference away last update utc | 2026-11-01T07:26:52Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-11-01T07:26:52Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:26:52Z |
| Market best over 2 5 last update utc | 2026-11-01T07:26:52Z |
| Market best under 2 5 last update utc | 2026-11-01T07:26:52Z |
| Home probability edge | -0.2% |
| Draw probability edge | -0.6% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0056 |
| Raw ev home | -0.0423 |
| Raw edge prob draw | -0.0186 |
| Raw ev draw | -0.1040 |
| Raw edge prob away | 0.0242 |
| Raw ev away | 0.0368 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05325309636272039, 0.06063603804013348, 0.05348688171267642, 0.02858464222262203, 0.01145722668108436, 0.0036738061564504107, 0.0009816840243325742, 0.0002248435427743926, 4.506062061720642e-05, 8.027150318161626e-06, 1.2869691365320857e-06, 1.875781218328896e-07, 2.5061535322752832e-08, 3.0908010934146977e-09, 3.539563905640641e-10, 3.7832516918953314e-11], [0.06322321640380538, 0.11914227052631333, 0.08067485414450164, 0.043114531418575054, 0.017281061482743183, 0.005541242381990758, 0.001480684850996801, 0.0003391339976799981, 6.796543151425283e-05, 1.210743943893443e-05, 1.9411497558586298e-06, 2.829261518900892e-07, 3.780059038889875e-08, 4.661889409451229e-09, 5.338763313155062e-10, 5.706320291303488e-11], [0.05279956154540786, 0.08465196668564255, 0.06792077403112623, 0.032515061846255716, 0.013032607902547228, 0.004178958528072937, 0.001116666653234987, 0.0002557597762498777, 5.12565053215746e-05, 9.130892281648264e-06, 1.4639288028396607e-06, 2.1337031910002446e-07, 2.8507523887653646e-08, 3.5157896301154104e-09, 4.0262578206977785e-10, 4.3034529445527016e-11], [0.026546053849560956, 0.04256049861656003, 0.034117990808644555, 0.0182497854437761, 0.006552408790055984, 0.002101056426877744, 0.0005614268800942936, 0.00012858843130812724, 2.5770250937342634e-05, 4.590741875663485e-06, 7.360199913532207e-07, 1.0727626925189648e-07, 1.4332737660870157e-08, 1.767634770309734e-09, 2.0242830393305596e-10, 2.1636485277799328e-11], [0.010009926517729, 0.01604861747527566, 0.01286513554378003, 0.0068754297294795225, 0.0027582614279773672, 0.0007922616507084464, 0.00021170159025028405, 4.848783761680213e-05, 9.717388493525678e-06, 1.7310666624001028e-06, 2.775367695243006e-07, 4.0451495291657245e-08, 5.4045566092894115e-09, 6.665357593733599e-10, 7.63312113718143e-11, 8.15863739899249e-12], [0.0030196165338372168, 0.004841261380664538, 0.0038809251925326434, 0.00207405731216921, 0.0008313186007371843, 0.00026680444667386065, 6.386236912200838e-05, 1.4626948149758012e-05, 2.9313688675735445e-06, 5.221973913294687e-07, 8.372235465655352e-08, 1.2202687380849908e-08, 1.6303504792532721e-09, 2.0106864878905915e-10, 2.3026241750918116e-11, 2.4611525708951624e-12], [0.0007590868254022363, 0.0012170213307585505, 0.0009756070517601623, 0.0005213872566779678, 0.0002089811704433584, 6.701065903012745e-05, 1.7922071622048826e-05, 3.676997894237083e-06, 7.369026705327036e-07, 1.3127268167189895e-07, 2.1046558627324493e-08, 3.0675746809262365e-09, 4.0984593762861447e-10, 5.054567710398957e-11, 5.788455771050274e-12, 6.186972653435851e-13], [0.00016356271979069077, 0.00026223524403374263, 0.00021021698374005173, 0.00011234487928474619, 4.502980091196419e-05, 1.4438988109333043e-05, 3.858266699665916e-06, 8.844835791267621e-07, 1.5878263326396714e-07, 2.828571927472962e-08, 4.534965245240943e-09, 6.609795364416787e-10, 8.83107360191375e-11, 1.0891228966343516e-11, 1.2472559628464259e-12, 1.33312559328159e-13], [3.083793198460254e-05, 4.944153918342012e-05, 3.963407465270686e-05, 2.1181377704129908e-05, 8.489868226576037e-06, 2.7223106451879856e-06, 7.274332819545486e-07, 1.6661030656770073e-07, 3.342007701269618e-08, 5.3329578295464285e-09, 8.550172677749524e-10, 1.2462034144508473e-10, 1.665000725320141e-11, 2.053420110173236e-12, 2.3515624219790674e-13, 2.513460061385602e-14], [5.168132582365831e-06, 8.285913261101054e-06, 6.642279147864011e-06, 3.549789535393252e-06, 1.422817996474855e-06, 4.562323553908284e-07, 1.2191062772444429e-07, 2.7922240517309193e-08, 5.595862221381768e-09, 9.977461791924977e-10, 1.432924426410786e-10, 2.088513741354237e-11, 2.7903766382538993e-12, 3.441329133863551e-13, 3.9409861785042016e-14, 4.212310619339858e-15], [7.795151426503804e-07, 1.2497734442329484e-06, 1.0018622964778167e-06, 5.354186743394629e-07, 2.1460520909854545e-07, 6.881402981178904e-08, 1.8387914560372002e-08, 4.2115423614006255e-09, 8.440300762863655e-10, 1.5035647983980458e-10, 2.4127799721980985e-11, 3.150128331796319e-12, 4.2087558872591014e-13, 5.1905947224414065e-14, 5.944232958732601e-15, 6.35347460807458e-16], [1.0688648135948685e-07, 1.7136791659543204e-07, 1.3737454196611763e-07, 7.34161724680875e-08, 2.942649145206989e-08, 9.435723711204256e-09, 2.5213358655414182e-09, 5.774832578312552e-10, 1.1573271650515107e-10, 2.0616758033760684e-11, 3.3054234981457946e-12, 4.822030964167954e-13, 5.771011787668586e-14, 7.117301200314451e-15, 8.150683810705439e-16, 8.71183262656027e-17], [1.343483831546047e-08, 2.153967669843779e-08, 1.7266961513757606e-08, 9.227868616344647e-09, 3.69869182539752e-09, 1.186000519776062e-09, 3.169132266464492e-10, 7.258536439940237e-11, 1.454674449265819e-11, 2.5913736447266955e-12, 4.1546722931553415e-13, 6.055511382978638e-14, 8.097764615707068e-15, 8.945919975330024e-16, 1.0244805307883742e-16, 1.095012776924968e-17], [1.5587626878695212e-09, 2.499117857463149e-09, 2.0033806666323017e-09, 1.070653546397159e-09, 4.291367470141423e-10, 1.3760443666027262e-10, 3.676951678832993e-11, 8.42163895496968e-12, 1.6877704080021057e-12, 3.0066134425153865e-13, 4.8204139110801666e-14, 7.02584205192405e-15, 9.386936335424146e-16, 1.1587135613945152e-16, 1.1886425339439947e-17, 1.2704768150777183e-18], [1.679356406963627e-10, 2.692462180644178e-10, 2.1583722681317093e-10, 1.1534846880623454e-10, 4.623369234907259e-11, 1.482502077643989e-11, 3.961419148660513e-12, 9.073179289076395e-13, 1.818344812984904e-13, 3.239220175876978e-14, 5.193345368597054e-15, 7.569396519453239e-16, 1.0113156928461041e-16, 1.247240286351633e-17, 1.4296102866591623e-18, 1.3687672895324683e-19], [1.6886612050186245e-11, 2.7073802866267605e-11, 2.1703311459489465e-11, 1.1598757924386688e-11, 4.6489859038204896e-12, 1.490716166321885e-12, 3.983368155456593e-13, 9.123450988789195e-14, 1.8284197031088936e-14, 3.2571676999803957e-15, 5.222120100205113e-16, 7.611336220710018e-17, 1.0169190824855892e-17, 1.2541508617020688e-18, 1.4362448401376773e-19, 1.5365008053523418e-20]] |
| Legacy trial inputs | {"lambda_home": 1.5083110392913714, "lambda_away": 1.6032702584630647, "rho": -0.06047613688333437, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-11-01T07:26:52Z", "over": 1.85, "under": 2.05, "bookmaker": "pinnacle", "event_id": "cf3a2e2b4a4e9815d1d0be8dcef916da", "kickoff_utc": "2026-11-01T16:15:00Z", "home_team": "Paris FC", "away_team": "AS Monaco"}} |
| Legacy p home | 0.3691 |
| Legacy p draw | 0.2616 |
| Legacy p away | 0.3693 |
| Legacy p over 1 5 | 0.8229 |
| Legacy p under 3 5 | 0.6230 |
| Legacy p btts yes | 0.6311 |
| Legacy p over 2 5 | 0.5975 |
| Legacy goal margin distribution | {"-1": 0.18123832810076373, "-10": 1.600249239444081e-06, "-11": 2.2910508879323578e-07, "-12": 3.014768699955164e-08, "-13": 3.6677119541757307e-09, "-14": 4.1101959347709897e-10, "-15": 3.7832516918953314e-11, "-2": 0.1119621720637968, "-3": 0.050657644255127185, "-4": 0.01825398545804142, "-5": 0.005437838981630371, "-6": 0.001376955429643251, "-7": 0.0003027180202254855, "-8": 5.874487667525882e-05, "-9": 1.019669331147954e-05, "0": 0.2616098332362298, "1": 0.18977096351393116, "10": 9.692683987144826e-07, "11": 1.3054953617926698e-07, "12": 1.6161392157661175e-08, "13": 1.8497122173934283e-09, "14": 1.9500944356263032e-10, "15": 1.6886612050186245e-11, "2": 0.11052342939706172, "3": 0.04704486212614752, "4": 0.01594810491027091, "5": 0.00446953045370815, "6": 0.001064730300076846, "7": 0.00022021260698340512, "8": 4.020296406356522e-05, "9": 6.5649527972858495e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3541 |
| Legacy raw p draw | 0.2508 |
| Legacy raw p away | 0.3952 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5083 |
| Legacy lambda away | 1.6033 |
| Legacy model home team | Paris FC |
| Legacy model away team | Monaco |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 66.7% |
| Market home draw odds | 1.47 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:26:48Z |
| Market reference home draw last update utc | 2026-11-01T07:26:58Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.4% |
| Market draw away odds | 1.56 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:26:48Z |
| Market reference draw away last update utc | 2026-11-01T07:26:58Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.8% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:26:48Z |
| Market reference home away last update utc | 2026-11-01T07:26:58Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.59 |
| Market reference dc home draw odds | 1.44 |
| Market reference dc home away odds | 1.32 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.2, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.2, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.05, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:48Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.05, "price": 1.75, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 77.9% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:26:52Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 4.06 |
| Market reference over 1 5 last update utc | 2026-11-01T07:26:52Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.3% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:26:52Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 3.02 |
| Market reference under 3 5 last update utc | 2026-11-01T07:26:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.3% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:26:48Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.19 |
| Market reference btts yes last update utc | 2026-11-01T07:26:52Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015445853721645362, "mu": 8.959862649547432, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,504.1286 |
| Elo away rating | 1,558.3951 |
| Elo rating diff | 5.7335 |
| Elo home expectancy | 0.5083 |

</details>


---

## 2026-11-01 — Strasbourg vs Auxerre

The model's most likely 1X2 outcome is **Strasbourg win** at **53.2%**. Expected goals are 1.82 for Strasbourg and 1.12 for Auxerre (2.94 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.2%; Under 3.5 goals: 60.8%; Double Chance 1X: 76.9%; Double Chance X2: 46.8%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 53.2% | 1.88 |
| Draw | 23.7% | 4.22 |
| Auxerre win | 23.1% | 4.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.82 |
| Auxerre expected goals | 1.12 |
| Expected total goals | 2.94 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 61.2% |
| Under 2.5 | 38.8% |
| Over 3.5 | 39.2% |
| Under 3.5 | 60.8% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.84% |
| 2 | 2-1 | 9.53% |
| 3 | 2-0 | 7.88% |
| 4 | 1-0 | 7.48% |
| 5 | 3-1 | 6.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 53.2% | 53.2% | 1.84 | -2.1% |
| Draw | 23.7% | 23.6% | 4.04 | -4.2% |
| Auxerre win | 23.1% | 23.3% | 4.09 | -5.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:00:00+00:00 |
| Fixture id | 448a1083448ea9dff55bfebf15ff20b4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:26:52Z |
| Market best draw last update utc | 2026-11-01T07:26:52Z |
| Market best away last update utc | 2026-11-01T07:26:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Strasbourg |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8217 |
| Dc lambda away | 1.1174 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:26:21.225636+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.55 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.90 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.68 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.13679981255156842, "-10": 9.663524723159803e-08, "-11": 1.043436382774655e-08, "-12": 1.035530262517752e-09, "-13": 9.506100244020987e-11, "-14": 8.113286972759916e-12, "-15": 6.417079666175976e-13, "-16": 4.21999731190159e-14, "-2": 0.06427617927569074, "-3": 0.021973034525157146, "-4": 0.005978332753823807, "-5": 0.0013441671429165667, "-6": 0.0002568274280141839, "-7": 4.259716380907686e-05, "-8": 6.235650306490359e-06, "-9": 8.164002334493212e-07, "0": 0.23718697573165828, "1": 0.2164221677627121, "10": 1.2251214510362893e-05, "11": 2.1566115736054627e-06, "12": 3.4892422690060085e-07, "13": 5.2219546166958943e-08, "14": 7.265908337103269e-09, "15": 9.368992297854685e-10, "16": 1.0044538762212304e-10, "2": 0.16330318125464124, "3": 0.09101165328058958, "4": 0.04036913311897563, "5": 0.014797385506397373, "6": 0.004609305455520039, "7": 0.001246341754072085, "8": 0.00029744083153726173, "9": 6.348693026696553e-05} |
| Raw goal margin distribution | {"-1": 0.13784790082261486, "-10": 5.317031605981437e-08, "-11": 5.3201616394884726e-09, "-12": 4.890855618167454e-10, "-13": 4.1577898251660236e-11, "-14": 3.285946806424899e-12, "-15": 2.411213040126268e-13, "-16": 1.4938822745256033e-14, "-2": 0.06199495994666047, "-3": 0.01999526549767277, "-4": 0.005098383207901737, "-5": 0.0010700338362853317, "-6": 0.00019036572590414922, "-7": 2.934979460969131e-05, "-8": 3.989119995142067e-06, "-9": 4.84511136416196e-07, "0": 0.2409707260383599, "1": 0.2283312112943053, "10": 7.051686228813144e-06, "11": 1.1502995212501835e-06, "12": 1.7239843842972166e-07, "13": 2.3893148994114112e-08, "14": 3.078461748876382e-09, "15": 3.682741115339001e-10, "16": 3.719755158895082e-11, "2": 0.16477113425478387, "3": 0.08663917265722348, "4": 0.03601487984621409, "5": 0.012322799433736036, "6": 0.003574069570341768, "7": 0.0008983419549945254, "8": 0.00019905637486815355, "9": 3.941532643830159e-05} |
| Unadjusted home-win probability | 53.3% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.1% |
| Raw p btts yes | 57.0% |
| P home draw | 76.9% |
| P draw away | 46.8% |
| P home away | 76.3% |
| Raw p home draw | 77.4% |
| Raw p draw away | 46.7% |
| Raw p home away | 75.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0818 |
| Totals anchor target over 2 5 | 0.6124 |
| Totals anchor reference over odds | 1.59 |
| Totals anchor reference under odds | 2.45 |
| Totals anchor reference last update utc | 2026-11-01T07:26:52Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5642 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.6, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.05, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.6, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.98, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.37, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 4.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 7.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:23:33Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.87, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.84 |
| Reference draw odds | 4.04 |
| Reference away odds | 4.09 |
| Market reference 1x2 last update utc | 2026-11-01T07:26:52Z |
| Market reference home last update utc | 2026-11-01T07:26:52Z |
| Market reference draw last update utc | 2026-11-01T07:26:52Z |
| Market reference away last update utc | 2026-11-01T07:26:52Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-01T07:26:52Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:26:52Z |
| Home probability edge | +0.0% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +1.7% |
| Under 2.5 probability edge | -1.7% |
| Raw edge prob home | 0.0009 |
| Raw ev home | -0.0197 |
| Raw edge prob draw | 0.0054 |
| Raw ev draw | -0.0265 |
| Raw edge prob away | -0.0064 |
| Raw ev away | -0.0747 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.06634529127357688, 0.058974654481616054, 0.034034701080253756, 0.011700606177012338, 0.0030168661813729353, 0.0006222912843057991, 0.00010696708086080067, 1.576012943930761e-05, 2.031783687110117e-06, 2.328319823121763e-07, 2.401321513614039e-08, 2.2514655318405137e-09, 1.935047956427293e-10, 1.535168520532141e-11, 1.1309299272278816e-12, 7.775925906379074e-14, 5.012331741817234e-15], [0.10064668974464931, 0.11508617178413043, 0.05990518008139385, 0.020594478513050817, 0.005310048454677517, 0.0010953077378737127, 0.0001882749675584783, 2.773972922346465e-05, 3.5761844176556068e-06, 4.0981237931926735e-07, 4.226615575884522e-08, 3.962850968308007e-09, 3.4059178607907396e-10, 2.7020818094130648e-11, 1.9905731150766666e-12, 1.3686567736346963e-13, 8.822308587732989e-15], [0.09446730057517713, 0.0974292100902469, 0.04925069526332337, 0.018124383421167803, 0.004673162960478282, 0.000963936882053846, 0.00016569332884420243, 2.4412635072397773e-05, 3.1472580152647043e-06, 3.6065961509132443e-07, 3.719676670747754e-08, 3.487547904893297e-09, 2.997413174160069e-10, 2.377994991139517e-11, 1.75182441947511e-12, 1.2045005228762646e-13, 7.764163749162449e-15], [0.055424615398805735, 0.05716238809601713, 0.0294773232915396, 0.009933904252228017, 0.0027417768709748856, 0.0005655484027940659, 9.721341638241836e-05, 1.4323061011807743e-05, 1.846517937897876e-06, 2.1160147833810898e-07, 2.1823599026209167e-08, 2.046168358116645e-09, 1.758602938346149e-10, 1.3951860273524817e-11, 1.0278074434695688e-12, 7.066887464932963e-14, 4.555288306859417e-15], [0.024388502477062868, 0.025153174878044932, 0.012970911334973146, 0.0044591995954246415, 0.0011270679511265925, 0.0002488583551405073, 4.277683533185944e-05, 6.302578853314382e-06, 8.125235868273383e-07, 9.311103273276541e-08, 9.603041808759176e-09, 9.003757935231561e-10, 7.738383353572041e-11, 6.1392393324181166e-12, 4.522662755642929e-13, 3.109643634033333e-14, 2.004464250336869e-15], [0.008585341351222344, 0.00885452448743434, 0.00456607376988055, 0.0015697458552840049, 0.00040474084098828086, 8.183897950797612e-05, 1.5058478215070406e-05, 2.2186598336486285e-06, 2.860279082486884e-07, 3.277733023286059e-08, 3.380502432070038e-09, 3.1695400482436343e-10, 2.7240976628030226e-11, 2.1611603810127636e-12, 1.5920864190071668e-13, 1.094669592933813e-14, 7.056197825860325e-16], [0.002518539428785141, 0.0025975052280911206, 0.0013394734529161704, 0.0004604903483705912, 0.0001187321184758147, 2.449096448190437e-05, 4.1267467504042806e-06, 6.508514969309156e-07, 8.390727114824579e-08, 9.61534261535418e-09, 9.916820212466306e-10, 9.297954799990123e-11, 7.991234233981923e-12, 6.339838346362333e-13, 4.67044029615899e-14, 3.2112509200387963e-15, 2.069959913615667e-16], [0.000633276178365743, 0.0006531317974736038, 0.0003368049829159471, 0.00011578836712161548, 2.9854693310837624e-05, 6.158150320907556e-06, 1.0585386296456373e-06, 1.5288393468987872e-07, 2.109813148150336e-08, 2.417737580573028e-09, 2.4935428581795603e-10, 2.3379317453034357e-11, 2.0093623384576748e-12, 1.594125767321248e-13, 1.1743626278916819e-14, 8.07455578091382e-16, 5.204827403068e-17], [0.00013933030958903706, 0.00014369884523255286, 7.410217554987026e-05, 2.5475186954760825e-05, 6.568482762796082e-06, 1.3548859407945986e-06, 2.3289446219355836e-07, 3.4313798603561685e-08, 4.336426511068061e-09, 5.319387292849292e-10, 5.486170335670476e-11, 5.143802419850923e-12, 4.420900173702223e-13, 3.507317095961457e-14, 2.583774885330416e-15, 1.7765240430359598e-16, 1.1451405219416625e-17], [2.72486838491572e-05, 2.8103033825017035e-05, 1.4492085462587944e-05, 4.98215583799342e-06, 1.2845913477116968e-06, 2.6497363539400926e-07, 4.554692793872249e-08, 6.7107139327398255e-09, 8.651400453220118e-10, 9.718451807849795e-11, 1.0729246311175343e-11, 1.0059680936220066e-12, 8.64590852609248e-14, 6.859223595245468e-15, 5.05306169170391e-16, 3.474329608675635e-17, 2.239539418040769e-18], [4.796097104292705e-06, 4.94647300750906e-06, 2.5507818838901552e-06, 8.769195356374727e-07, 2.2610357538975572e-07, 4.6638556653312485e-08, 8.016808826643276e-09, 1.1811666148251662e-09, 1.5227508562050777e-10, 1.7449943252673467e-11, 1.7641974859565008e-12, 1.770625211676265e-13, 1.521784210772232e-14, 1.20730610714875e-15, 8.893998213474487e-17, 6.115239278260778e-18, 3.9418595691721546e-19], [7.674281397870599e-07, 7.914899336091316e-07, 4.081530781360272e-07, 1.4031674366535652e-07, 3.6179051943143e-08, 7.462680591427126e-09, 1.2827773397983844e-09, 1.8899961328608974e-10, 2.436568383677363e-11, 2.792182309612318e-12, 2.879727855005232e-13, 2.6467440289452333e-14, 2.435021644964132e-15, 1.93182218753129e-16, 1.4231372626144395e-17, 9.785053558377702e-19, 6.307407649782619e-20], [1.1256384281900292e-07, 1.1609314782791549e-07, 5.98665549925547e-08, 2.0581199802243474e-08, 5.30662469244154e-09, 1.0946015158304088e-09, 1.8815357342631385e-10, 2.772184346627012e-11, 3.573878599683781e-12, 4.095481444144213e-13, 4.223890379133828e-14, 3.960295839177283e-15, 3.336564796588541e-16, 2.833533431962395e-17, 2.0874110660477885e-18, 1.435239566568894e-19, 9.251498693838733e-21], [1.5240457218209626e-08, 1.5718303573231767e-08, 8.10556611533517e-09, 2.7865688237907528e-09, 7.184845912580804e-10, 1.4820236370061522e-10, 2.54748453361518e-11, 3.753368388790196e-12, 4.838813471314826e-13, 5.545031883623121e-14, 5.718889743406025e-15, 5.361998826344762e-16, 4.6084315858045105e-17, 3.5839585000163425e-18, 2.826227166042346e-19, 1.9432267648632788e-20, 1.2525964511933712e-21], [1.916074529821811e-09, 1.9761507609293748e-09, 1.0190553052977843e-09, 3.5033552290554e-10, 9.032996882364964e-11, 1.86324314474534e-11, 3.202771517998103e-12, 4.718843711726957e-13, 6.083496783723244e-14, 6.971375075654229e-15, 7.1899542246717065e-16, 6.741260601957566e-17, 5.793853988472187e-18, 4.596548745016227e-19, 3.31938031570542e-20, 2.443081107418355e-21, 1.5748006256722753e-22], [2.2483482272537078e-10, 2.318842503759402e-10, 1.1957735221045048e-10, 4.110885247986274e-11, 1.0599442877173598e-11, 2.186355152803161e-12, 3.7581761840231595e-13, 5.537156164241312e-14, 7.138458862797884e-15, 8.180307471821315e-16, 8.436791253928565e-17, 7.910287980956611e-18, 6.798588020038919e-19, 5.39365356696411e-20, 3.973403671581747e-21, 2.6780865574910005e-22, 1.847892730632751e-23], [2.473352585088867e-11, 2.5509016048162512e-11, 1.315441040772666e-11, 4.522283751182997e-12, 1.1660186408393406e-12, 2.4051555286492796e-13, 4.134277185045765e-14, 6.091289306014425e-15, 7.852843019525441e-16, 8.998955049309591e-17, 9.28110654960597e-18, 8.701913248729456e-19, 7.478959464769774e-20, 5.933425628297531e-21, 4.3710436504368695e-22, 3.005395006449153e-23, 1.8990428213396512e-24]] |
| Legacy trial inputs | {"lambda_home": 1.760120646869722, "lambda_away": 1.0313538070531896, "rho": -0.06047613688333437, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5349 |
| Legacy p draw | 0.2418 |
| Legacy p away | 0.2233 |
| Legacy p over 1 5 | 0.7740 |
| Legacy p under 3 5 | 0.6940 |
| Legacy p btts yes | 0.5383 |
| Legacy p over 2 5 | 0.5304 |
| Legacy goal margin distribution | {"-1": 0.14001058418098408, "-10": 2.8290222702105417e-08, "-11": 2.6168968773305753e-09, "-12": 2.2235011149523472e-10, "-13": 1.7467263660992562e-11, "-14": 1.2755597683405136e-12, "-15": 8.658156765152373e-14, "-16": 5.012331741817234e-15, "-2": 0.05991297283263424, "-3": 0.018078403406816063, "-4": 0.004293036625530096, "-5": 0.000836921991434233, "-6": 0.00013807559772694745, "-7": 1.9719725333758254e-05, "-8": 2.480918594012205e-06, "-9": 2.7876784798102294e-07, "0": 0.2418292535699804, "1": 0.23244274826264086, "10": 5.6503327193849304e-06, "11": 8.919880292116461e-07, "12": 1.2934347656865316e-07, "13": 1.7340707615100634e-08, "14": 2.1611131906054777e-09, "15": 2.503438387735333e-10, "16": 2.473352585088867e-11, "2": 0.16629547589053428, "3": 0.08563561072722901, "4": 0.03470513045037168, "5": 0.011546459290078661, "6": 0.0032509893158711935, "7": 0.0007923813282039384, "8": 0.0001701299001275941, "9": 3.262462863353615e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5379 |
| Legacy raw p draw | 0.2481 |
| Legacy raw p away | 0.2140 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7601 |
| Legacy lambda away | 1.0314 |
| Legacy model home team | Strasbourg |
| Legacy model away team | Auxerre |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 76.3% |
| Market home draw odds | 1.26 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:26:24Z |
| Market reference home draw last update utc | 2026-11-01T07:26:58Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.4% |
| Market draw away odds | 2.05 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:26:24Z |
| Market reference draw away last update utc | 2026-11-01T07:26:58Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:26:24Z |
| Market reference home away last update utc | 2026-11-01T07:26:58Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.03 |
| Market reference dc home draw odds | 1.26 |
| Market reference dc home away odds | 1.26 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:24Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.47, "price": 1.52, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:24Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.52, "price": 2.47, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:24Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.93, "price": 1.89, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:24Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.89, "price": 1.93, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:24Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.56, "price": 2.36, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:24Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.36, "price": 1.56, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 82.4% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 5.10 |
| Market reference over 1 5 last update utc | 2026-11-01T07:26:33Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.7% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:26:52Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.48 |
| Market reference under 3 5 last update utc | 2026-11-01T07:26:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.1% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:26:24Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.32 |
| Market reference btts yes last update utc | 2026-11-01T07:26:52Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015445853721645362, "mu": 9.31053319578099, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,524.8199 |
| Elo away rating | 1,446.2294 |
| Elo rating diff | 138.5904 |
| Elo home expectancy | 0.6895 |

</details>


---

## 2026-11-02 — Lorient vs Brest

The model's most likely 1X2 outcome is **Lorient win** at **39.4%**. Expected goals are 1.49 for Lorient and 1.29 for Brest (2.78 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 45.5%; Under 3.5 goals: 75.8%; Double Chance 1X: 67.8%; Double Chance X2: 60.6%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 89.2%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 39.4% | 2.54 |
| Draw | 28.4% | 3.52 |
| Brest win | 32.2% | 3.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.49 |
| Brest expected goals | 1.29 |
| Expected total goals | 2.78 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 71.9% |
| Under 1.5 | 28.1% |
| Over 2.5 | 45.5% |
| Under 2.5 | 54.5% |
| Over 3.5 | 24.2% |
| Under 3.5 | 75.8% |
| Over 4.5 | 10.8% |
| Under 4.5 | 89.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.51% |
| 2 | 1-0 | 10.16% |
| 3 | 0-1 | 9.03% |
| 4 | 0-0 | 8.95% |
| 5 | 2-1 | 8.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 39.4% | 38.6% | 2.52 | -0.8% |
| Draw | 28.4% | 29.2% | 3.31 | -6.0% |
| Brest win | 32.2% | 32.2% | 3.01 | -3.0% |
| Over 2.5 | 45.5% | 45.5% | 2.13 | -3.1% |
| Under 2.5 | 54.5% | 54.5% | 1.79 | -2.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T19:45:00+00:00 |
| Fixture id | 5118966f484adf525196d196a61bc5d6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:26:52Z |
| Market best draw last update utc | 2026-11-01T07:26:52Z |
| Market best away last update utc | 2026-11-01T07:26:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lorient |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4862 |
| Dc lambda away | 1.2928 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:26:21.225636+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.17 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.55 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.14 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.24 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.18779185448229013, "-10": 1.1848639217381251e-07, "-11": 1.2366970540438435e-08, "-12": 1.185082186537381e-09, "-13": 1.0445850280289094e-10, "-14": 7.80195660674135e-12, "-2": 0.09186084376064589, "-3": 0.03174459210803896, "-4": 0.008583752148714463, "-5": 0.0018992084186368987, "-6": 0.0003548921426834376, "-7": 5.733122821109843e-05, "-8": 8.151038232271431e-06, "-9": 1.0343451792837877e-06, "0": 0.28384903626906705, "1": 0.21024267792558302, "10": 4.629366494086233e-07, "11": 5.554666610485379e-08, "12": 6.11906018732311e-09, "13": 6.200427516703646e-10, "14": 5.323814955138434e-11, "2": 0.11766596269075406, "3": 0.04674463323186693, "4": 0.014530506659321818, "5": 0.003695879462554739, "6": 0.000793931693914747, "7": 0.00014744144696017344, "8": 2.4098102759355074e-05, "9": 3.5154182236296665e-06} |
| Raw goal margin distribution | {"-1": 0.18014200257586419, "-10": 2.6542551466718074e-07, "-11": 3.075227265271302e-08, "-12": 3.2730890443941863e-09, "-13": 3.2202572470089243e-10, "-14": 2.927110103722839e-11, "-15": 2.236315889226242e-12, "-2": 0.09422392219458965, "-3": 0.03540566767338589, "-4": 0.010493237360611982, "-5": 0.002556333964770611, "-6": 0.0005274527119167946, "-7": 9.426062799631652e-05, "-8": 1.4844424826310036e-05, "-9": 2.0884734655091606e-06, "0": 0.26521335914597577, "1": 0.2080353858654375, "10": 1.0699377254870967e-06, "11": 1.4250648642103515e-07, "12": 1.7436399849387043e-08, "13": 1.9721100610364424e-09, "14": 2.0607306213568284e-10, "15": 1.8099096621248108e-11, "2": 0.12452150036919678, "3": 0.053789503854821945, "4": 0.018326343813130593, "5": 0.005132459211619505, "6": 0.0012173992481697565, "7": 0.0002501044457976168, "8": 4.527891806422886e-05, "9": 7.3232390556758446e-06} |
| Unadjusted home-win probability | 41.1% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 32.3% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.8% |
| P home draw | 67.8% |
| P draw away | 60.6% |
| P home away | 71.6% |
| Raw p home draw | 67.7% |
| Raw p draw away | 58.9% |
| Raw p home away | 73.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.8984 |
| Totals anchor target over 2 5 | 0.4548 |
| Totals anchor reference over odds | 2.13 |
| Totals anchor reference under odds | 1.79 |
| Totals anchor reference last update utc | 2026-11-01T07:26:52Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5189 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:13:11Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.25, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:13:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.89, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:13:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.14, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:13:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.88, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:13:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:13:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:13:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:13:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 5.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:13:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 5.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:13:11Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.59, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.23, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:26:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.59, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.52 |
| Reference draw odds | 3.31 |
| Reference away odds | 3.01 |
| Market reference 1x2 last update utc | 2026-11-01T07:26:52Z |
| Market reference home last update utc | 2026-11-01T07:26:52Z |
| Market reference draw last update utc | 2026-11-01T07:26:52Z |
| Market reference away last update utc | 2026-11-01T07:26:52Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.13 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-11-01T07:26:52Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:26:52Z |
| Market best over 2 5 last update utc | 2026-11-01T07:26:52Z |
| Market best under 2 5 last update utc | 2026-11-01T07:26:52Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0250 |
| Raw ev home | 0.0365 |
| Raw edge prob draw | -0.0266 |
| Raw ev draw | -0.1221 |
| Raw edge prob away | 0.0017 |
| Raw ev away | -0.0264 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.07319012882254292, 0.07507964528863574, 0.05680964135501201, 0.02626862808172411, 0.009109908171006246, 0.002527438482922689, 0.0005843404387332544, 0.00011579891792062953, 2.0079417647485818e-05, 3.0948898913316694e-06, 4.293206728831423e-07, 5.414093044181603e-08, 6.25865580142889e-09, 6.678429019246397e-10, 6.617331289915169e-11], [0.08200103012627441, 0.13300333516580326, 0.07829033313229801, 0.03620124321142502, 0.012554519417852284, 0.003483105967222408, 0.0008052894987527244, 0.00015958445862580473, 2.7671787028198106e-05, 4.2651204059882895e-06, 5.916541224148773e-07, 7.46125372257502e-08, 8.625160025077819e-09, 9.203656637256308e-10, 9.119456817139914e-11], [0.0616777807414017, 0.08555892861973154, 0.05994104803627988, 0.02494477454200439, 0.008650798386468282, 0.002400063792031659, 0.0005548915784497364, 0.00010996302855069343, 1.9067480212251856e-05, 2.938917492433048e-06, 4.0768430532321545e-07, 5.141240338718148e-08, 5.943239875982311e-09, 6.341857886966848e-10, 6.283839284759897e-11], [0.028333066277309252, 0.039303404987319816, 0.027260685950436764, 0.012732231164476662, 0.0039739374713091465, 0.0011025229129840734, 0.00025490184114850553, 5.0513973403862806e-05, 8.759072944924786e-06, 1.3500573966137273e-06, 1.8727889207576143e-07, 2.3617435892387252e-08, 2.7301599909077275e-09, 2.9132740781656186e-10, 2.8866219372830117e-11], [0.009761570151658419, 0.013541172749453632, 0.009392103759014298, 0.004342883965922854, 0.0015212732359842645, 0.000379851395312054, 8.782114084668467e-05, 1.7403541508520515e-05, 3.0177568561949738e-06, 4.651342659782812e-07, 6.45230567362378e-08, 8.136897539059014e-09, 9.406199814610348e-10, 1.0037081411056659e-10, 9.945256989241145e-12], [0.0026905171757441865, 0.0037322641026079667, 0.0025886835916152677, 0.0011970004539274188, 0.0004151173857274342, 0.00011632951258272146, 2.420556162282063e-05, 4.796823320426191e-06, 8.317644116334032e-07, 1.2820188885587403e-07, 1.7784064416201632e-08, 2.2427193828432928e-09, 2.592568794415861e-10, 2.7664545263963187e-11, 2.741145566853018e-12], [0.0006179745813181342, 0.0008572494414721242, 0.0005945848155572867, 0.00027493444792777095, 9.534672179590673e-05, 2.6452843361743807e-05, 6.177462248231097e-06, 1.1017639693296214e-06, 1.910447807835695e-07, 2.9446200642814814e-08, 4.0847536157048005e-09, 5.151216220142888e-10, 5.95477192902311e-11, 6.354163404337139e-12, 6.296032224880747e-13], [0.0001216630403992426, 0.00016877000540635448, 0.00011705820695994315, 5.4127405651592766e-05, 1.8771277033834756e-05, 5.2078733460686955e-06, 1.204053438479709e-06, 2.4101091546232477e-07, 3.7611723176313436e-08, 5.797187144444535e-09, 8.041812061402697e-10, 1.0141398142294225e-10, 1.1723389273126966e-11, 1.250968668187474e-12, 1.2395241585774294e-13], [2.0958238195919764e-05, 2.9073101921716104e-05, 2.016498828405931e-05, 9.32423731028439e-06, 3.233627024490802e-06, 8.971323560788546e-07, 2.074158156944355e-07, 4.110365366653081e-08, 7.199120298252359e-09, 9.986502773635178e-10, 1.3853197499965444e-10, 1.7470041617271942e-11, 2.0195252727813236e-12, 2.1549765021053024e-13, 2.1352616603870862e-14], [3.2092116194988736e-06, 4.451792924092766e-06, 3.08774593089893e-06, 1.4277655611794317e-06, 4.951462676925661e-07, 1.373725956563073e-07, 3.1760362658918964e-08, 6.2939604807129736e-09, 1.091366512039678e-09, 1.6990928183442806e-10, 2.1212585699477875e-11, 2.6750846148028306e-12, 3.0923801469835467e-13, 3.299788639509673e-14, 3.269600463133761e-15], [4.4226691242866196e-07, 6.135091557526263e-07, 4.255275192591e-07, 1.9676280073839643e-07, 6.823694943718366e-08, 1.893155109001916e-08, 4.3769496051394904e-09, 8.673814004162218e-10, 1.5040307553267473e-10, 2.318199492949699e-11, 3.248177820976869e-12, 3.686579613154364e-13, 4.2616616846092205e-14, 4.5474948563566696e-15, 4.505892016966129e-16], [5.540868685084079e-08, 7.686249126019392e-08, 5.3311519352797465e-08, 2.4651105709307955e-08, 8.548954617154255e-09, 2.371808418104905e-09, 5.483589733206735e-10, 1.0866846025624486e-10, 1.8843003352500512e-11, 2.9043183234591755e-12, 4.028847360245905e-13, 5.13188739774179e-14, 5.339153147361604e-15, 5.697254562137723e-16, 5.645133125170221e-17], [6.363304491554697e-09, 8.827125558573924e-09, 6.122459307914703e-09, 2.8310090095457414e-09, 9.81788315248793e-10, 2.723857939579588e-10, 6.297523576599279e-11, 1.24798211352739e-11, 2.163988621317187e-12, 3.3354087387638466e-13, 4.626852567767003e-14, 5.8348483746133485e-15, 6.812983214207958e-16, 6.542902856076499e-17, 6.4830449903136036e-18], [6.74567551161893e-10, 9.35754760714107e-10, 6.490357938881698e-10, 3.001124364583005e-10, 1.0407839833151353e-10, 2.8875345859273165e-11, 6.675941820934228e-12, 1.3229733691563968e-12, 2.294022715652705e-13, 3.535833477744188e-14, 4.9048801772224224e-15, 6.185464462195217e-16, 7.150356066091982e-17, 7.706786122526771e-18, 6.872611217948716e-19], [6.640235837368302e-11, 9.211282526678445e-11, 6.388909058681794e-11, 2.9542146703882253e-11, 1.0245157943136037e-11, 2.842400380227207e-12, 6.571592133537759e-13, 1.3022943606796567e-13, 2.2581655198173375e-14, 3.4805659023241045e-15, 4.828213434620601e-16, 6.088781282451492e-17, 7.038590948857072e-18, 7.510675061683401e-19, 7.516919990868312e-20]] |
| Legacy trial inputs | {"lambda_home": 1.378117010861764, "lambda_away": 1.3871920745407014, "rho": -0.06047613688333437, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-11-01T07:26:52Z", "over": 2.13, "under": 1.79, "bookmaker": "pinnacle", "event_id": "5118966f484adf525196d196a61bc5d6", "kickoff_utc": "2026-11-02T19:45:00Z", "home_team": "Lorient", "away_team": "Brest"}} |
| Legacy p home | 0.3748 |
| Legacy p draw | 0.2805 |
| Legacy p away | 0.3446 |
| Legacy p over 1 5 | 0.7697 |
| Legacy p under 3 5 | 0.7002 |
| Legacy p btts yes | 0.5711 |
| Legacy p over 2 5 | 0.5182 |
| Legacy goal margin distribution | {"-1": 0.18269388778711157, "-10": 5.101777226496805e-07, "-11": 6.342914247496338e-08, "-12": 7.24185985800212e-09, "-13": 7.590374700960389e-10, "-14": 6.617331289915169e-11, "-2": 0.10285702081327468, "-3": 0.04149637870684244, "-4": 0.013201569837047875, "-5": 0.0034519335285652045, "-6": 0.0007644092615640844, "-7": 0.00014660530396587077, "-8": 2.4776808708819655e-05, "-9": 3.7407896890843132e-06, "0": 0.28051077178316314, "1": 0.19960634516350417, "10": 5.25562220591172e-07, "11": 6.491439035000677e-08, "12": 7.362948342855622e-09, "13": 7.666803764286774e-10, "14": 6.640235837368302e-11, "2": 0.11167105839993569, "3": 0.04475755812262141, "4": 0.014145921962913309, "5": 0.003674663700376998, "6": 0.0008084080136483735, "7": 0.00015402947919917838, "8": 2.5861221065801256e-05, "9": 3.878970224412555e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3633 |
| Legacy raw p draw | 0.2692 |
| Legacy raw p away | 0.3675 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3781 |
| Legacy lambda away | 1.3872 |
| Legacy model home team | Lorient |
| Legacy model away team | Brest |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 67.5% |
| Market home draw odds | 1.42 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:26:31Z |
| Market reference home draw last update utc | 2026-11-01T07:26:58Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.5% |
| Market draw away odds | 1.57 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:26:31Z |
| Market reference draw away last update utc | 2026-11-01T07:26:58Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.0% |
| Market home away odds | 1.37 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:26:31Z |
| Market reference home away last update utc | 2026-11-01T07:26:58Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.57 |
| Market reference dc home draw odds | 1.43 |
| Market reference dc home away odds | 1.36 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:31Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.22, "price": 1.63, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:31Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.63, "price": 2.22, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:31Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.04, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:26:31Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.04, "price": 1.76, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 72.5% |
| Market over 1 5 odds | 1.35 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:26:52Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.34 |
| Market reference over 1 5 last update utc | 2026-11-01T07:26:52Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.0% |
| Market under 3 5 odds | 1.29 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:26:52Z |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.75 |
| Market reference under 3 5 last update utc | 2026-11-01T07:26:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.5% |
| Market btts yes odds | 1.79 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:26:31Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-11-01T07:26:52Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015445853721645362, "mu": 9.14709113839762, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,498.9880 |
| Elo away rating | 1,450.3969 |
| Elo rating diff | 108.5911 |
| Elo home expectancy | 0.6514 |

</details>


---
