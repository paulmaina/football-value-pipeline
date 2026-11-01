# Premier League — football model report

Fixtures in this report: **2**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,988 |
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
| Training sha256 | 710cd14c77659538d82d7513f6e2c48597e59395dab66f3650b09eb1c23b07c2 |
| Training as of utc | 2026-11-01T08:47:34.311683+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 88, 'bbs_added_results': 8, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 88, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 201, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-01T08:47:34.311683+00:00', 'observations': 565, 'observations_sha256': '97785850b77db94b1ef8432706e62e47d106e18a0256c32589f66ea6c50cc421', 'eligible_training_matches': 265, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 243, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 26, 'retrospective_eligible_training_matches': 265, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '0e007d7c5c41d11472fcb2df663471f0a76eb9206044dda97d19304c56b83de5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 205, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-03T00:00:00+00:00', 'audit_origin_utc': '2025-11-01T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 13, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1979, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1616, 'tuning_matches': 247, 'audit_matches': 107, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9197629882632063, 'audit_candidate_poisson_score': 0.9101983643886844, 'audit_gain': 0.00956462387452195, 'audit_gain_lower95': 0.0010634214007443634, 'audit_baseline_briers': [0.6326531963674555, 0.1571095989813288, 0.22008773968314155, 0.2505880399093558], 'audit_candidate_briers': [0.6323760785267843, 0.15631033250496124, 0.21733676331513951, 0.24791853345253542], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum']} |
| Optimizer objective | 1884.315 |
| Base scoring parameter | 0.213 |
| Home-advantage parameter | 0.181 |
| Dixon-Coles low-score adjustment | -0.069 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1988, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-31'} |
| Training data health | {'training_end': '2026-10-31', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 2.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261101T084734311683Z_fa6eab174b585c528e349ae7047e2c3935e021231618a54561d4b774f581f1c7.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 1, 'ANCHORED_ALTERNATE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 2} |
| Legacy comparison status | {'AVAILABLE': 2} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-01 — Liverpool vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **39.1%**. Expected goals are 1.19 for Liverpool and 1.44 for Arsenal (2.63 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 49.7%; Under 3.5 goals: 72.0%; Double Chance 1X: 60.9%; Double Chance X2: 67.5%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 86.7%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 32.5% | 3.08 |
| Draw | 28.4% | 3.52 |
| Arsenal win | 39.1% | 2.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.19 |
| Arsenal expected goals | 1.44 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 49.7% |
| Under 2.5 | 50.3% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.3% |
| Under 4.5 | 86.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.53% |
| 2 | 0-1 | 8.56% |
| 3 | 1-2 | 8.31% |
| 4 | 0-0 | 7.99% |
| 5 | 1-0 | 7.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 32.5% | 33.3% | 2.93 | -4.9% |
| Draw | 28.4% | 28.7% | 3.39 | -3.7% |
| Arsenal win | 39.1% | 38.0% | 2.58 | +1.0% |
| Over 2.5 | 49.7% | 49.7% | 1.96 | -2.5% |
| Under 2.5 | 50.3% | 50.3% | 1.94 | -2.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:30:00+00:00 |
| Fixture id | 6a3819cdbe2ba2fe5a3d8f9b4b459965 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T08:48:12Z |
| Market best draw last update utc | 2026-11-01T08:48:12Z |
| Market best away last update utc | 2026-11-01T08:48:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Liverpool |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1921 |
| Dc lambda away | 1.4401 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T08:47:34.311683+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.52 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.55 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.19736183991065034, "-10": 9.464737602507033e-07, "-11": 1.2449475246795397e-07, "-12": 1.5040892257443913e-08, "-13": 1.679654071214434e-09, "-14": 1.7342245775137504e-10, "-15": 1.515352858897031e-11, "-2": 0.11928908992972266, "-3": 0.05128512037884333, "-4": 0.017338739180989434, "-5": 0.004810270254788298, "-6": 0.0011290544520379236, "-7": 0.0002293688046227858, "-8": 4.104191714281015e-05, "-9": 6.558442444247495e-06, "0": 0.28399743309951586, "1": 0.18559583769942845, "10": 1.63768101119108e-07, "11": 1.783140611401234e-08, "12": 1.783289923266639e-09, "13": 1.648473660065078e-10, "14": 1.4089037077988341e-11, "15": 1.0190689234458482e-12, "2": 0.09362912837215819, "3": 0.033320801879944115, "4": 0.009325140605417058, "5": 0.002141515204115598, "6": 0.0004160833934309179, "7": 6.997028717900529e-05, "8": 1.036384130891205e-05, "9": 1.3709058725009279e-06} |
| Raw goal margin distribution | {"-1": 0.2133764678402891, "-10": 8.879208850163546e-07, "-11": 1.1476768256612181e-07, "-12": 1.3620913697745174e-08, "-13": 1.485688753045825e-09, "-14": 1.3613177957482893e-10, "-2": 0.12754004354915846, "-3": 0.054070290827052926, "-4": 0.018002087316313697, "-5": 0.004914482222012966, "-6": 0.0011345359657570925, "-7": 0.00022661877174431932, "-8": 3.9861413044198206e-05, "-9": 6.260677377658504e-06, "0": 0.27666586309862967, "1": 0.17516306961448053, "10": 1.341258142299563e-07, "11": 1.4350648346835288e-08, "12": 1.4098469250775894e-09, "13": 1.2729383358006275e-10, "14": 9.655012982379992e-12, "2": 0.08739250357675034, "3": 0.030669036724985135, "4": 0.008452362293045575, "5": 0.0019100591584355526, "6": 0.00036500694514585185, "7": 6.035212295304516e-05, "8": 8.787456133187303e-06, "9": 1.1424721304244895e-06} |
| Unadjusted home-win probability | 30.4% |
| Unadjusted draw probability | 27.7% |
| Unadjusted away-win probability | 41.9% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 54.0% |
| P home draw | 60.9% |
| P draw away | 67.5% |
| P home away | 71.6% |
| Raw p home draw | 58.1% |
| Raw p draw away | 69.6% |
| Raw p home away | 72.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0181 |
| Totals anchor target over 2 5 | 0.4973 |
| Totals anchor reference over odds | 1.96 |
| Totals anchor reference under odds | 1.94 |
| Totals anchor reference last update utc | 2026-11-01T08:48:12Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4866 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.4, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.9, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.08, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.82, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:48:09Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.26, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.3, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 5.26, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.93 |
| Reference draw odds | 3.39 |
| Reference away odds | 2.58 |
| Market reference 1x2 last update utc | 2026-11-01T08:48:12Z |
| Market reference home last update utc | 2026-11-01T08:48:12Z |
| Market reference draw last update utc | 2026-11-01T08:48:12Z |
| Market reference away last update utc | 2026-11-01T08:48:12Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.94 |
| Market reference over 2 5 last update utc | 2026-11-01T08:48:12Z |
| Market reference under 2 5 last update utc | 2026-11-01T08:48:12Z |
| Market best over 2 5 last update utc | 2026-11-01T08:48:12Z |
| Market best under 2 5 last update utc | 2026-11-01T08:48:12Z |
| Home probability edge | -0.9% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0293 |
| Raw ev home | -0.1092 |
| Raw edge prob draw | -0.0105 |
| Raw ev draw | -0.0621 |
| Raw edge prob away | 0.0397 |
| Raw ev away | 0.0818 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.09621915402734399, 0.10170005697259991, 0.08003068520628805, 0.03807350395559811, 0.013584711598936643, 0.0038776444519842933, 0.0009223681579164286, 0.00018805887276734029, 3.354991378183629e-05, 5.320304213274265e-06, 7.593185900643786e-07, 9.851875485869211e-08, 1.1717237560644773e-08, 1.2863805045930285e-09, 1.3113812828823003e-10], [0.08727342281566182, 0.13687872987354507, 0.08292185219673358, 0.0394489371105597, 0.014075469233315641, 0.004017727191640513, 0.000955689381698685, 0.00019485263698170206, 3.4761928935877704e-05, 5.512504091119847e-06, 7.86749529049433e-07, 1.0207781687663003e-07, 1.214053133061843e-08, 1.3328519404234918e-09, 1.3587558900993271e-10], [0.051870566001609754, 0.07403013711868983, 0.04642777223195713, 0.020437029396713522, 0.007291977922944023, 0.0020814352613204657, 0.0004951071795208093, 0.00010094591544663532, 1.8008864511556917e-05, 2.8558236650072697e-06, 4.0758571537608806e-07, 5.288272630548523e-08, 6.2895584486902326e-09, 6.905010954176021e-10, 7.039209698119953e-11], [0.017914809368679712, 0.025568176641399865, 0.018245565534979635, 0.007628433445000515, 0.002518468651491274, 0.000718876210424366, 0.00017099776273705436, 3.486422013820342e-05, 6.219815967709144e-06, 9.863307939917549e-07, 1.407700157374986e-07, 1.826438448019693e-08, 2.1722577813775474e-09, 2.38481984038635e-10, 2.4311687642673275e-11], [0.0046404987373692965, 0.006622961427023849, 0.004726174981001299, 0.002248413110173692, 0.000705042674682121, 0.00018621153472228922, 4.4293795470777916e-05, 9.030928892469794e-06, 1.6111278412643708e-06, 2.5549067868672025e-07, 3.6463858858100765e-08, 4.731049679342894e-09, 5.626830453103526e-10, 6.177432999936913e-11, 6.297491281508208e-12], [0.0009616280291175914, 0.0013724441497426781, 0.000979382301226875, 0.0004659277353891058, 0.00016624406092457947, 4.170378008700669e-05, 9.178788240517556e-06, 1.871435559723917e-06, 3.3386620239225397e-07, 5.29440932339757e-08, 7.556228481513532e-09, 9.803924613032096e-10, 1.1660207630751869e-10, 1.2801194563201022e-11, 1.3049985512667152e-12], [0.00016606125740642764, 0.000237004116275083, 0.00016912720043380476, 8.045995255591996e-05, 2.8708291519766613e-05, 8.194546238750073e-06, 1.7130614689481576e-06, 3.231737561643525e-07, 5.7654560491171875e-08, 9.142789549036772e-09, 1.3048671262648452e-09, 1.6930164257502626e-10, 2.013573525471665e-11, 2.210607845343429e-12, 2.253570962732588e-13], [2.4580048812822855e-05, 3.508086616870334e-05, 2.503386344994692e-05, 1.1909518163297813e-05, 4.249342790182308e-06, 1.2129400300422775e-06, 2.885198153225949e-07, 5.169837501922657e-08, 8.533910517649733e-09, 1.353297071879163e-09, 1.9314377211620654e-10, 2.5059684020097988e-11, 2.980450486603723e-12, 3.27209667042106e-13, 3.335689800996481e-14], [3.183502629946942e-06, 4.543523512069791e-06, 3.2422787577648493e-06, 1.542469776320403e-06, 5.503566754934315e-07, 1.5709479688230355e-07, 3.7367850563100766e-08, 7.618818791955595e-09, 1.1945296784414807e-09, 1.7527323970078157e-10, 2.5015154004456276e-11, 3.2456229274045685e-12, 3.860151798225794e-13, 4.237879442408554e-14, 4.320242541023638e-15], [3.6650099877722655e-07, 5.230735132670972e-07, 3.732676052649617e-07, 1.7757695824945333e-07, 6.335985695586449e-08, 1.8085551247378543e-08, 4.301976830395404e-09, 8.771171320819565e-10, 1.564786799202367e-10, 2.1807804806864426e-11, 2.879871636026311e-12, 3.7365260306628534e-13, 4.444002892201285e-14, 4.878862149286483e-15, 4.973682733447017e-16], [3.79741115201305e-08, 5.4196992620216175e-08, 3.8675217029352544e-08, 1.8399205564154963e-08, 6.564877809252559e-09, 1.8738905003324184e-09, 4.4573888873288283e-10, 9.088036294859589e-11, 1.621315865888195e-11, 2.5710628314649736e-12, 3.2248682544495835e-13, 3.871510764217828e-14, 4.604545744411767e-15, 5.05511460995944e-16, 5.153360657018772e-17], [3.576904913702146e-09, 5.104990780583878e-09, 3.642944318985678e-09, 1.733080937410582e-09, 6.183671652547188e-10, 1.7650783310165422e-10, 4.198559380359937e-11, 8.560316588777692e-12, 1.5271700785637775e-12, 2.421767595649704e-13, 3.456368437737561e-14, 3.94118328814034e-15, 4.3371712040772325e-16, 4.761576654165072e-17, 4.854117797172999e-18], [3.0884360147949426e-10, 4.407843586099949e-10, 3.1454569540130897e-10, 1.4964081273587734e-10, 5.339217758413023e-11, 1.5240358963871466e-11, 3.6251961719434595e-12, 7.391303567939671e-13, 1.3186168447714988e-13, 2.0910464332490585e-14, 2.9843602279213734e-15, 3.872096081299527e-16, 4.0472885304941307e-17, 4.111326742177634e-18, 4.191230291702006e-19], [2.461544632996053e-11, 3.513138582270677e-11, 2.506991450164497e-11, 1.1926668958094724e-11, 4.255462232229994e-12, 1.2146867745596436e-12, 2.8893531023007907e-13, 5.891015239217922e-14, 1.0509637245766218e-14, 1.6666053952396705e-15, 2.37859417089283e-16, 3.08613721693073e-17, 3.670468934305057e-18, 3.5414204226911443e-19, 3.3404934992232775e-20], [1.8217640941349062e-12, 2.600038057855923e-12, 1.855398820314709e-12, 8.826806135968682e-13, 3.1494242252223304e-13, 8.989773014271599e-14, 2.1383807819247943e-14, 4.359880335684318e-15, 7.778075408454502e-16, 1.2334376665125512e-16, 1.7603733025864228e-17, 2.284018699484149e-18, 2.7164766478419926e-19, 2.982292185235742e-20, 2.6719076406734232e-21]] |
| Legacy trial inputs | {"lambda_home": 1.0361257308117908, "lambda_away": 1.4272089708138596, "rho": -0.08992886901281963, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-11-01T08:48:12Z", "over": 1.96, "under": 1.94, "bookmaker": "pinnacle", "event_id": "6a3819cdbe2ba2fe5a3d8f9b4b459965", "kickoff_utc": "2026-11-01T16:30:00Z", "home_team": "Liverpool", "away_team": "Arsenal"}} |
| Legacy p home | 0.2979 |
| Legacy p draw | 0.2879 |
| Legacy p away | 0.4142 |
| Legacy p over 1 5 | 0.7148 |
| Legacy p under 3 5 | 0.7669 |
| Legacy p btts yes | 0.5025 |
| Legacy p over 2 5 | 0.4460 |
| Legacy goal margin distribution | {"-1": 0.20777312942636003, "-10": 8.679307448650191e-07, "-11": 1.1137409897237082e-07, "-12": 1.3120481598049464e-08, "-13": 1.4222560936029613e-09, "-14": 1.3113812828823003e-10, "-2": 0.12753670071449766, "-3": 0.05441078034729002, "-4": 0.018134075592488422, "-5": 0.0049407627843294595, "-6": 0.001136253454922264, "-7": 0.00022582224527968315, "-8": 3.9488843682409395e-05, "-9": 6.162171805739112e-06, "0": 0.28790260200912376, "1": 0.18197227348438708, "10": 4.3405889607496304e-08, "11": 4.043641867427383e-09, "12": 3.458303861225158e-10, "13": 2.7215484387816452e-11, "14": 1.8217640941349062e-12, "2": 0.08266080485237588, "3": 0.025602023881478937, "4": 0.006194548502368568, "5": 0.001225273755101755, "6": 0.00020456872436167177, "7": 2.9515873036541173e-05, "8": 3.747039069428969e-06, "9": 4.2449492188912664e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2625 |
| Legacy raw p draw | 0.2887 |
| Legacy raw p away | 0.4488 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0361 |
| Legacy lambda away | 1.4272 |
| Legacy model home team | Liverpool |
| Legacy model away team | Arsenal |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 62.1% |
| Market home draw odds | 1.56 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T08:47:56Z |
| Market reference home draw last update utc | 2026-11-01T08:47:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 66.8% |
| Market draw away odds | 1.45 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T08:47:56Z |
| Market reference draw away last update utc | 2026-11-01T08:47:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.2% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T08:47:56Z |
| Market reference home away last update utc | 2026-11-01T08:47:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.45 |
| Market reference dc home draw odds | 1.56 |
| Market reference dc home away odds | 1.36 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:47:56Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.05, "price": 1.79, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:47:56Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.79, "price": 2.05, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:47:56Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.25, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:47:56Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.25, "price": 1.65, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 75.5% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T08:48:12Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market reference over 1 5 last update utc | 2026-11-01T08:48:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T08:48:12Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.30 |
| Market reference under 3 5 last update utc | 2026-11-01T08:48:15Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.5% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T08:47:56Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.28 |
| Market reference btts yes last update utc | 2026-11-01T08:48:12Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 9.78696978427008, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,570.2236 |
| Elo away rating | 1,650.6613 |
| Elo rating diff | -20.4377 |
| Elo home expectancy | 0.4706 |

</details>


---

## 2026-11-02 — Newcastle United vs Everton

The model's most likely 1X2 outcome is **Newcastle United win** at **42.9%**. Expected goals are 1.60 for Newcastle United and 1.03 for Everton (2.63 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 56.0%; Under 3.5 goals: 66.0%; Double Chance 1X: 69.8%; Double Chance X2: 57.1%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 82.6%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 42.9% | 2.33 |
| Draw | 26.9% | 3.72 |
| Everton win | 30.2% | 3.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.60 |
| Everton expected goals | 1.03 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 79.9% |
| Under 1.5 | 20.1% |
| Over 2.5 | 56.0% |
| Under 2.5 | 44.0% |
| Over 3.5 | 34.0% |
| Under 3.5 | 66.0% |
| Over 4.5 | 17.4% |
| Under 4.5 | 82.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.60% |
| 2 | 2-1 | 8.09% |
| 3 | 1-2 | 7.98% |
| 4 | 1-0 | 7.05% |
| 5 | 2-0 | 6.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 42.9% | 40.0% | 2.43 | +4.3% |
| Draw | 26.9% | 27.0% | 3.56 | -4.3% |
| Everton win | 30.2% | 33.0% | 2.93 | -11.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T20:00:00+00:00 |
| Fixture id | 0f552d9c6990c69474f50ff2fb54e9a3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T08:48:12Z |
| Market best draw last update utc | 2026-11-01T08:48:12Z |
| Market best away last update utc | 2026-11-01T08:48:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Newcastle |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6004 |
| Dc lambda away | 1.0318 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T08:47:34.311683+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.63 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.98 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.94 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.73 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.1794574232405143, "-10": 1.0066430560234587e-07, "-11": 1.0507995917189808e-08, "-12": 1.0078680657580621e-09, "-13": 8.939891868971496e-11, "-14": 7.37208333369724e-12, "-15": 5.642292742989873e-13, "-16": 3.633875742594986e-14, "-2": 0.08452642656088502, "-3": 0.028329643853402538, "-4": 0.007517423261142659, "-5": 0.001643367400167285, "-6": 0.00030469415235607355, "-7": 4.897523388541055e-05, "-8": 6.941517373417044e-06, "-9": 8.793588039398074e-07, "0": 0.26874112361668023, "1": 0.18548054346683704, "10": 5.306631851853271e-06, "11": 8.591902383811211e-07, "12": 1.2782008589264674e-07, "13": 1.7585457346318802e-08, "14": 2.2492494288742345e-09, "15": 2.670108932672956e-10, "16": 2.667284976267538e-11, "2": 0.13302342182495758, "3": 0.06915167471338418, "4": 0.028461420538196593, "5": 0.009650464508191025, "6": 0.0027752598397168494, "7": 0.0006918979308551274, "8": 0.00015210584725440128, "9": 2.988708728851906e-05} |
| Raw goal margin distribution | {"-1": 0.14667932667322098, "-10": 3.1468768303799524e-08, "-11": 2.915703524640655e-09, "-12": 2.481001204149177e-10, "-13": 1.951216969069796e-11, "-14": 1.4197018160184894e-12, "-15": 8.797290376182783e-14, "-2": 0.06422020257921131, "-3": 0.019588178170429602, "-4": 0.004685445337823723, "-5": 0.0009182169235237487, "-6": 0.00015209215693453426, "-7": 2.1790227568594807e-05, "-8": 2.7485062731185726e-06, "-9": 3.0950835126256817e-07, "0": 0.2660643869922143, "1": 0.23201661709574134, "10": 2.5359434159995863e-06, "11": 3.64442617701023e-07, "12": 4.809929955731037e-08, "13": 5.867367928481411e-09, "14": 6.621568522822731e-10, "15": 6.364124226296651e-11, "2": 0.15449827471780817, "3": 0.07309236089149047, "4": 0.02711782172160126, "5": 0.008242808305047398, "6": 0.0021176915684739356, "7": 0.00047059102025240167, "8": 9.20671254854538e-05, "9": 1.6080746457329354e-05} |
| Unadjusted home-win probability | 49.8% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 52.2% |
| P home draw | 69.8% |
| P draw away | 57.1% |
| P home away | 73.1% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.2% |
| Raw p home away | 73.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1304 |
| Totals anchor target over 2 5 | 0.5599 |
| Totals anchor reference over odds | 1.74 |
| Totals anchor reference under odds | 2.19 |
| Totals anchor reference last update utc | 2026-11-01T08:48:12Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4859 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.6, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.12, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.24, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 5.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T08:47:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.23, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T08:48:12Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.23, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.43 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.93 |
| Market reference 1x2 last update utc | 2026-11-01T08:48:12Z |
| Market reference home last update utc | 2026-11-01T08:48:12Z |
| Market reference draw last update utc | 2026-11-01T08:48:12Z |
| Market reference away last update utc | 2026-11-01T08:48:12Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-01T08:47:26Z |
| Market reference under 2 5 last update utc | 2026-11-01T08:47:26Z |
| Home probability edge | +2.9% |
| Draw probability edge | -0.1% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0975 |
| Raw ev home | 0.2093 |
| Raw edge prob draw | -0.0038 |
| Raw ev draw | -0.0528 |
| Raw edge prob away | -0.0937 |
| Raw ev away | -0.3077 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08035796446613272, 0.07609057963621184, 0.049565760637030026, 0.018563791020303047, 0.005214501895306734, 0.00117178780935075, 0.0002194339775416938, 3.5221835593338324e-05, 4.94684324599359e-06, 6.1757796140303e-07, 6.939016813351726e-08, 7.087799192272994e-09, 6.63645737037926e-10, 5.735867453452292e-11, 4.60338418630473e-12, 3.448197341165599e-13], [0.09095343051802081, 0.13038548663950064, 0.0758223954082769, 0.028397649605854572, 0.007976797278639473, 0.0017925228519304508, 0.0003356754662360047, 5.3880015378362645e-05, 7.567350925313365e-06, 9.447295831460468e-07, 1.0614845203718472e-07, 1.0842442565674914e-08, 1.0152009943556492e-09, 8.774347543053978e-11, 7.041950158824813e-12, 5.27482235493629e-13], [0.07738660397599195, 0.08695047098145459, 0.0514035343365937, 0.02172041535737261, 0.006101186278384426, 0.001371040963667805, 0.0002567469721304887, 4.121102731116126e-05, 5.788014414366107e-06, 7.225921592503611e-07, 8.118941179253328e-08, 8.293022812928991e-09, 7.7649339204736e-10, 6.711205883946925e-11, 5.386152885838036e-12, 4.034535747703221e-13], [0.03946028878644739, 0.044337010784324594, 0.024908212607461427, 0.009816854335413593, 0.0031110626402426214, 0.0006991090135078799, 0.00013091813239999694, 2.1013960496174482e-05, 2.951372828840809e-06, 3.6845776676913985e-07, 4.13993827242901e-08, 4.2287044307086686e-09, 3.959426039739738e-10, 3.422118411708685e-11, 2.7464591725599306e-12, 2.0572545834031585e-13], [0.015090929609660521, 0.016955950638627846, 0.009525730670545867, 0.0035676578188450973, 0.0010545671525536398, 0.000267362587471739, 5.0067457219297254e-05, 8.036438871092871e-06, 1.1287033364844043e-06, 1.4091053039519336e-07, 1.583250375983638e-08, 1.6171975134100217e-09, 1.5142164818847168e-10, 1.3087321369213029e-11, 1.050337524725445e-12, 7.867627192315741e-14], [0.004617019560423378, 0.0051876165212514785, 0.002914365514307408, 0.0010915130055315235, 0.000306602063655593, 7.250302168070952e-05, 1.531797147699745e-05, 2.458721657559785e-06, 3.453230196718712e-07, 4.311110660060099e-08, 4.843901697271626e-09, 4.947761831519195e-10, 4.632694801718368e-11, 4.004022304664551e-12, 3.213472610461102e-13, 2.407074287709026e-14], [0.0011771347741496982, 0.0013226116377030549, 0.0007430336706564301, 0.00027828730167432685, 7.81698986178786e-05, 1.7566113906499217e-05, 3.4615888377259382e-06, 6.268647392958431e-07, 8.80420213625573e-08, 1.0991416013621672e-08, 1.2349796347621088e-09, 1.2614593526993355e-10, 1.1811312639587705e-11, 1.0208477199649239e-12, 8.192926856919142e-14, 6.136969555667388e-15], [0.00025724318316085746, 0.00028903472672795285, 0.0001623776230495155, 6.081505099334169e-05, 1.708272832424824e-05, 3.838781383667971e-06, 7.188665569050374e-07, 1.2142308907653352e-07, 1.9240116191096608e-08, 2.4019907532097835e-09, 2.6988421322827804e-10, 2.756709141914657e-11, 2.5811654939090392e-12, 2.230892526269762e-13, 1.7904275961946355e-14, 1.3411323988805949e-15], [4.918918346815028e-05, 5.526825639067623e-05, 3.104930748081381e-05, 1.1628851206781297e-05, 3.2665023319687843e-06, 7.34038972209763e-07, 1.3745926528442945e-07, 2.2063892278074048e-08, 3.260942785913108e-09, 4.593006601638675e-10, 5.160635907440894e-11, 5.271287273147083e-12, 4.935618564561043e-13, 4.2658382789404916e-14, 3.4235959310372127e-15, 2.564468640646804e-16], [8.360703640752997e-06, 9.393965905589627e-06, 5.277462234472439e-06, 1.9765601249564175e-06, 5.55208605101217e-07, 1.247648746066801e-07, 2.3364001975411888e-08, 3.750207901253711e-09, 5.267099319178438e-10, 6.919584797377483e-11, 8.771551869300468e-12, 8.959626403351846e-13, 8.389089062397752e-14, 7.25066104272587e-15, 5.819098620253298e-16, 4.3588367988127685e-17], [1.2789646909342329e-06, 1.4370262620631632e-06, 8.073109807084644e-07, 3.023609875376633e-07, 8.493211008772834e-08, 1.9085698542522372e-08, 3.574069223051448e-09, 5.736817970663162e-10, 8.057257310302473e-11, 1.0058908877345718e-11, 1.1893287339998192e-12, 1.3705839013350131e-13, 1.2833069034537585e-14, 1.109157776431313e-15, 8.901669031887594e-17, 6.667857872694848e-18], [1.778613544051137e-07, 1.998424499894307e-07, 1.1227004582123508e-07, 4.2048334206500704e-08, 1.1811225313541024e-08, 2.6541844482517403e-09, 4.970338878434695e-10, 7.978001437181309e-11, 1.1204959043506489e-11, 1.3988589125595571e-12, 1.5717376785443777e-13, 1.6894230560795314e-14, 1.7846521141955058e-15, 1.5424687308680517e-16, 1.2379254264799713e-17, 9.272767580096473e-19], [2.2673369963850063e-08, 2.547547115137842e-08, 1.4311935795593353e-08, 5.3602281452107934e-09, 1.5056687393166903e-09, 3.383495315707477e-10, 6.336077480877282e-11, 1.017017883184064e-11, 1.4283832633172947e-12, 1.783234236451982e-13, 2.0036162431660272e-14, 2.046576622009604e-15, 2.0164980222740617e-16, 1.9663048394978436e-17, 1.5780798069437326e-18, 1.1820717920175538e-19], [2.668016110225319e-09, 2.9977443827638426e-09, 1.6841111547173619e-09, 6.30747659862961e-10, 1.7717474109779142e-10, 3.9814196238019555e-11, 7.45577601457967e-12, 1.1967431842062088e-12, 1.6808042051899884e-13, 2.0983637098255817e-14, 2.3576911698609996e-15, 2.4082434181764423e-16, 2.2548896136402873e-17, 2.050845629023217e-18, 1.8569548130075146e-19, 1.3909650791100203e-20], [2.9152522378526154e-10, 3.2755353263681613e-10, 1.8401721015723985e-10, 6.891969354639725e-11, 1.935929316531279e-11, 4.350364461307078e-12, 8.146677836062855e-13, 1.3076413716247684e-13, 1.8365587080950534e-14, 2.2928120551645133e-15, 2.576170523393943e-16, 2.6314072794484737e-17, 2.4638426908600334e-18, 2.1294908280444138e-19, 1.798451687713261e-20, 1.5198611597993214e-21], [2.973038982992182e-11, 3.3404636789281126e-11, 1.8766483813487354e-11, 7.0285834257774e-12, 1.9743037160326447e-12, 4.436598303828695e-13, 8.308163003532782e-14, 1.3335617148783916e-14, 1.8729633624232542e-15, 2.3382606596332338e-16, 2.6272359192243513e-17, 2.6835675899154324e-18, 2.512681500686516e-19, 2.1717020446792695e-20, 1.7429236172159307e-21, 1.3738462520458421e-22]] |
| Legacy trial inputs | {"lambda_home": 1.5297333165836828, "lambda_away": 1.1235855627988234, "rho": -0.08992886901281963, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4278 |
| Legacy p draw | 0.2731 |
| Legacy p away | 0.2991 |
| Legacy p over 1 5 | 0.7526 |
| Legacy p under 3 5 | 0.7255 |
| Legacy p btts yes | 0.5398 |
| Legacy p over 2 5 | 0.4953 |
| Legacy goal margin distribution | {"-1": 0.17702778017411927, "-10": 8.104439968362421e-08, "-11": 8.172937380912595e-09, "-12": 7.569810908126442e-10, "-13": 6.480407826811805e-11, "-14": 5.130866421798359e-12, "-15": 3.448197341165599e-13, "-2": 0.08481632221018118, "-3": 0.02805094042355762, "-4": 0.007285958757354562, "-5": 0.0015517715589291967, "-6": 0.00027948680441900375, "-7": 4.355484262409621e-05, "-8": 5.977146454303772e-06, "-9": 7.324287936627176e-07, "0": 0.2730944962951468, "1": 0.20670468157072128, "10": 1.4937696273321155e-06, "11": 2.050918307084719e-07, "12": 2.586216014019692e-08, "13": 3.0143361266756224e-09, "14": 3.249298605745427e-10, "15": 2.973038982992182e-11, "2": 0.13242300840786037, "3": 0.05962673295742287, "4": 0.021085789775067205, "5": 0.006114212474060839, "6": 0.0014992830193540747, "7": 0.00031810341993680205, "8": 5.943405499959382e-05, "9": 9.915541784969795e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4555 |
| Legacy raw p draw | 0.2763 |
| Legacy raw p away | 0.2682 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5297 |
| Legacy lambda away | 1.1236 |
| Legacy model home team | Newcastle |
| Legacy model away team | Everton |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 67.2% |
| Market home draw odds | 1.44 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T08:47:56Z |
| Market reference home draw last update utc | 2026-11-01T08:48:20Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.2% |
| Market draw away odds | 1.61 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T08:47:56Z |
| Market reference draw away last update utc | 2026-11-01T08:48:20Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.6% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T08:47:56Z |
| Market reference home away last update utc | 2026-11-01T08:48:20Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.45 |
| Market reference dc home draw odds | 1.32 |
| Market reference dc home away odds | 1.24 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:47:56Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.27, "price": 1.61, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:47:56Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.27, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:47:56Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.81, "price": 2.02, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:47:56Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.02, "price": 1.81, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:47:56Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.5, "price": 2.52, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T08:47:56Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.52, "price": 1.5, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 79.5% |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-11-01T08:48:15Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.2% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T08:48:12Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.80 |
| Market reference under 3 5 last update utc | 2026-11-01T08:48:15Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T08:47:56Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.27 |
| Market reference btts yes last update utc | 2026-11-01T08:48:20Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 10.130337476180937, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,496.2139 |
| Elo away rating | 1,476.4968 |
| Elo rating diff | 79.7171 |
| Elo home expectancy | 0.6128 |

</details>


---
