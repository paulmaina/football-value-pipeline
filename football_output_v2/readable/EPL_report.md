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
| Training as of utc | 2026-11-01T06:59:16.579426+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 88, 'bbs_added_results': 8, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 88, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 201, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-01T06:59:16.579426+00:00', 'observations': 565, 'observations_sha256': '97785850b77db94b1ef8432706e62e47d106e18a0256c32589f66ea6c50cc421', 'eligible_training_matches': 265, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 243, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 26, 'retrospective_eligible_training_matches': 265, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '0e007d7c5c41d11472fcb2df663471f0a76eb9206044dda97d19304c56b83de5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 205, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-03T00:00:00+00:00', 'audit_origin_utc': '2025-11-01T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 13, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1979, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1616, 'tuning_matches': 247, 'audit_matches': 107, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9197582143957189, 'audit_candidate_poisson_score': 0.910195307480813, 'audit_gain': 0.009562906914905911, 'audit_gain_lower95': 0.0010631190827245455, 'audit_baseline_briers': [0.6326505118014825, 0.15710994303526649, 0.2200875586724739, 0.2505864830196242], 'audit_candidate_briers': [0.6323739432377693, 0.15631048962236782, 0.21733652908626439, 0.24791736058525773], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum']} |
| Optimizer objective | 1884.520 |
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
| Bbs statistics model artifact | bbs/feature_models/EPL/20261101T065916579426Z_8345508eebab0a60557c10af9099ddca33b7724b07fb115fec5ef497df9c3da1.json |
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

The model's most likely 1X2 outcome is **Arsenal win** at **39.8%**. Expected goals are 1.19 for Liverpool and 1.44 for Arsenal (2.63 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 49.7%; Under 3.5 goals: 72.0%; Double Chance 1X: 60.2%; Double Chance X2: 68.1%; Double Chance 12 (either team wins): 71.7%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 31.9% | 3.13 |
| Draw | 28.3% | 3.53 |
| Arsenal win | 39.8% | 2.51 |

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
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.49% |
| 2 | 0-1 | 8.72% |
| 3 | 1-2 | 8.45% |
| 4 | 0-0 | 7.97% |
| 5 | 1-0 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 31.9% | 32.5% | 2.97 | -5.2% |
| Draw | 28.3% | 28.6% | 3.37 | -4.6% |
| Arsenal win | 39.8% | 38.9% | 2.50 | -0.5% |
| Over 2.5 | 49.7% | 49.7% | 1.95 | -3.0% |
| Under 2.5 | 50.3% | 50.3% | 1.93 | -3.0% |

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
| Market best home last update utc | 2026-11-01T06:59:32Z |
| Market best draw last update utc | 2026-11-01T06:59:32Z |
| Market best away last update utc | 2026-11-01T06:59:32Z |
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
| Dc lambda home | 1.1922 |
| Dc lambda away | 1.4402 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T06:59:16.579426+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.54 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.55 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.20069328678015042, "-10": 9.56196324482984e-07, "-11": 1.2567243883491338e-07, "-12": 1.517091411305258e-08, "-13": 1.6928034310227304e-09, "-14": 1.7464129344420237e-10, "-15": 1.5250063918528067e-11, "-2": 0.12124189021200497, "-3": 0.05209109378046646, "-4": 0.01759879656913566, "-5": 0.004878798635022262, "-6": 0.0011442652223703875, "-7": 0.00023227809196723915, "-8": 4.152974504182557e-05, "-9": 6.631120676395375e-06, "0": 0.28301371320415214, "1": 0.18253545852455164, "10": 1.600543566361044e-07, "11": 1.7413421328218422e-08, "12": 1.7401210056245443e-09, "13": 1.6073034074439427e-10, "14": 1.3726566201251163e-11, "15": 9.922252361071841e-13, "2": 0.09204157661202302, "3": 0.03273546106768816, "4": 0.009155068363615336, "5": 0.00210094725323033, "6": 0.0004078989515152871, "7": 6.854215822233964e-05, "8": 1.0144541546166661e-05, "9": 1.340860899476368e-06} |
| Raw goal margin distribution | {"-1": 0.2133679657006581, "-10": 8.883526219742334e-07, "-11": 1.148308848816574e-07, "-12": 1.362929525694888e-08, "-13": 1.4866968568032961e-09, "-14": 1.362308823758825e-10, "-2": 0.12754126740187283, "-3": 0.05407348780930541, "-4": 0.018004147030637675, "-5": 0.0049153324580725015, "-6": 0.0011348010437960427, "-7": 0.00022668576747096917, "-8": 3.987570544833608e-05, "-9": 6.2633202846426305e-06, "0": 0.27665879548573347, "1": 0.17515982481353107, "10": 1.3422139174890583e-07, "11": 1.4362124780760447e-08, "12": 1.4110974888428436e-09, "13": 1.2741767529728361e-10, "14": 9.665102374069331e-12, "2": 0.08739729641332632, "3": 0.030672931716281143, "4": 0.008454094355170977, "5": 0.0019106057134730082, "6": 0.00036514178654867215, "7": 6.0379525833039274e-05, "8": 8.792197977159299e-06, "9": 1.1431871520369775e-06} |
| Unadjusted home-win probability | 30.4% |
| Unadjusted draw probability | 27.7% |
| Unadjusted away-win probability | 41.9% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 54.0% |
| P home draw | 60.2% |
| P draw away | 68.1% |
| P home away | 71.7% |
| Raw p home draw | 58.1% |
| Raw p draw away | 69.6% |
| Raw p home away | 72.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0172 |
| Totals anchor target over 2 5 | 0.4973 |
| Totals anchor reference over odds | 1.95 |
| Totals anchor reference under odds | 1.93 |
| Totals anchor reference last update utc | 2026-11-01T06:59:32Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4871 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.4, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.9, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.08, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.82, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:15Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.39, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.13, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.71, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 5.39, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.97 |
| Reference draw odds | 3.37 |
| Reference away odds | 2.50 |
| Market reference 1x2 last update utc | 2026-11-01T06:59:32Z |
| Market reference home last update utc | 2026-11-01T06:59:32Z |
| Market reference draw last update utc | 2026-11-01T06:59:32Z |
| Market reference away last update utc | 2026-11-01T06:59:32Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-11-01T06:59:32Z |
| Market reference under 2 5 last update utc | 2026-11-01T06:59:32Z |
| Market best over 2 5 last update utc | 2026-11-01T06:59:32Z |
| Market best under 2 5 last update utc | 2026-11-01T06:59:32Z |
| Home probability edge | -0.6% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0215 |
| Raw ev home | -0.0970 |
| Raw edge prob draw | -0.0091 |
| Raw ev draw | -0.0677 |
| Raw edge prob away | 0.0305 |
| Raw ev away | 0.0483 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.09597897824825959, 0.1028274429913508, 0.08092156540731478, 0.03849986305823784, 0.01373774204727399, 0.00392158395518361, 0.0009328813925311443, 0.0001902149093273934, 3.393678769626439e-05, 5.382008583934152e-06, 7.681756738766515e-07, 9.967449153350394e-08, 1.1855474665880959e-08, 1.3016426143286524e-09, 1.327027389781114e-10], [0.08612875959891143, 0.13654270967040183, 0.08384276357231955, 0.03988967464619427, 0.014233662592777651, 0.004063149726880348, 0.0009665575998352449, 0.00019708150219774717, 3.516187623039602e-05, 5.576294415162119e-06, 7.959061479182096e-07, 1.032726540294946e-07, 1.2283446995196547e-08, 1.3486307811705804e-09, 1.374931924949551e-10], [0.051188147115028955, 0.07306099347734835, 0.04631630521092973, 0.020664828612147055, 0.0073737427194318144, 0.002104912949935159, 0.0005007247444739232, 0.00010209798655074982, 1.8215594697811982e-05, 2.8887968980010717e-06, 4.123188339830979e-07, 5.350035353182987e-08, 6.363434376779177e-09, 6.986575899940299e-10, 7.122828860967575e-11], [0.017678664909113496, 0.02523281060966056, 0.01800743253340294, 0.00761042430975519, 0.0025466428071700404, 0.0007269661591996114, 0.00017293349082090446, 3.526121170336214e-05, 6.291053943780952e-06, 9.97693318249708e-07, 1.4240106181853666e-07, 1.847722326191865e-08, 2.1977162753207597e-09, 2.412928405468085e-10, 2.459985596959365e-11], [0.004579212336008151, 0.006535923284362378, 0.004664371298439201, 0.0022191569742724187, 0.0007034064747780312, 0.0001883022513963277, 4.4794059876535565e-05, 9.133527698202627e-06, 1.6295388805635243e-06, 2.5842729493259375e-07, 3.6885404089759485e-08, 4.786058739794142e-09, 5.692629805889207e-10, 6.250082558286357e-11, 6.371972346278031e-12], [0.0009489035841135008, 0.0013543728866324631, 0.0009665502095024981, 0.0004598533223801618, 0.00016408750111356207, 4.1608669256493335e-05, 9.282217299600606e-06, 1.8926480216419865e-06, 3.3767276351438405e-07, 5.3551259125071185e-08, 7.643387022484922e-09, 9.91766259943165e-10, 1.1796257586405133e-10, 1.2951410210720239e-11, 1.3203990017475737e-12], [0.00016385969643423643, 0.0002338774284109045, 0.00016690697197175187, 7.94089379269068e-05, 2.8335152876716985e-05, 8.08856946844897e-06, 1.709223277656088e-06, 3.268284949865031e-07, 5.83104094556338e-08, 9.247402171110053e-09, 1.3198844415830065e-09, 1.7126135996190603e-10, 2.0370153717716394e-11, 2.2364908100821813e-12, 2.2801070964502425e-13], [2.4253555575726656e-05, 3.4617171466251636e-05, 2.4704595509352706e-05, 1.1753647364973755e-05, 4.19400389477701e-06, 1.1972228278226215e-06, 2.847999460302131e-07, 5.158461482100598e-08, 8.6307663638519e-09, 1.368746478656676e-09, 1.953615889329934e-10, 2.5349106596677128e-11, 3.0150712226969816e-12, 3.3103231201639613e-13, 3.3748814007207135e-14], [3.1411359810087603e-06, 4.483352657876634e-06, 3.1995512414006227e-06, 1.5222429771558026e-06, 5.431754736843463e-07, 1.550551913931498e-07, 3.68851220626876e-08, 7.52089194280904e-09, 1.1919490486724766e-09, 1.7726962958331971e-10, 2.5301746557878974e-11, 3.2830234135624636e-12, 3.9048908409932435e-13, 4.2872786338671354e-14, 4.3708896068214794e-15], [3.616142510324059e-07, 5.161330879319496e-07, 3.683391399780549e-07, 1.7524384725832732e-07, 6.25315151216274e-08, 1.7850283223432295e-08, 4.246293656046739e-09, 8.658210671036091e-10, 1.5447362060707148e-10, 2.176156605155968e-11, 2.9127908459412992e-12, 3.7794863386843355e-13, 4.4953933397547336e-14, 4.935606295067864e-15, 5.031861024394373e-16], [3.7466821113856964e-08, 5.347650437248948e-08, 3.816358627291206e-08, 1.815699978025321e-08, 6.47888484580355e-09, 1.849466293030819e-09, 4.3995811656701434e-10, 8.970764549562129e-11, 1.600499840250018e-11, 2.5382201627053275e-12, 3.218159900462997e-13, 3.915922509952804e-14, 4.657673131414311e-15, 5.113777391731232e-16, 5.2135068331109043e-17], [3.5290309805144e-09, 5.036996335681431e-09, 3.5946598692043748e-09, 1.7102228807452317e-09, 6.10251541505072e-10, 1.7420276531304024e-10, 4.144002019214613e-11, 8.449637592177902e-12, 1.507524084679202e-12, 2.390770640063862e-13, 3.412353991775128e-14, 3.933142867685356e-15, 4.387100984073461e-16, 4.8167093728160325e-17, 4.9106453614681596e-18], [3.047021609230954e-10, 4.349022937226047e-10, 3.1036866379972974e-10, 1.4766337000170945e-10, 5.26900909711316e-11, 1.5040944475337287e-11, 3.577997408059906e-12, 7.295551803227142e-13, 1.3016203280210618e-13, 2.064229484867732e-14, 2.9462808370610428e-15, 3.8229412143051173e-16, 4.0391939131445276e-17, 4.158823661620683e-18, 4.2399294917728977e-19], [2.428474185005802e-11, 3.466168372766219e-11, 2.473636175040526e-11, 1.1768760714848319e-11, 4.199396726999113e-12, 1.198762268892516e-12, 2.8516615416075805e-13, 5.814549908617583e-14, 1.0373905310358906e-14, 1.6451895190839614e-15, 2.348183856951999e-16, 3.046881591390454e-17, 3.624019241124164e-18, 3.534479539171271e-19, 3.37922096969113e-20], [1.7972428514138653e-12, 2.5652100270260995e-12, 1.8306659218531905e-12, 8.709716247080856e-13, 3.107850927322872e-13, 8.871689604996124e-14, 2.110431460194345e-14, 4.303178646894748e-15, 7.6774244813487e-16, 1.2175567360983088e-16, 1.7378223234859448e-17, 2.2549081201033693e-18, 2.682030846657382e-19, 2.9446696495418555e-20, 2.6667780623562413e-21]] |
| Legacy trial inputs | {"lambda_home": 1.0360991306866232, "lambda_away": 1.4273029518565534, "rho": -0.0899136506170151, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-11-01T06:59:32Z", "over": 1.95, "under": 1.93, "bookmaker": "pinnacle", "event_id": "6a3819cdbe2ba2fe5a3d8f9b4b459965", "kickoff_utc": "2026-11-01T16:30:00Z", "home_team": "Liverpool", "away_team": "Arsenal"}} |
| Legacy p home | 0.2940 |
| Legacy p draw | 0.2872 |
| Legacy p away | 0.4188 |
| Legacy p over 1 5 | 0.7151 |
| Legacy p under 3 5 | 0.7667 |
| Legacy p btts yes | 0.5022 |
| Legacy p over 2 5 | 0.4464 |
| Legacy goal margin distribution | {"-1": 0.21007959809116675, "-10": 8.780594270958184e-07, "-11": 1.1268119597466412e-07, "-12": 1.3275333735661216e-08, "-13": 1.4391358068236074e-09, "-14": 1.327027389781114e-10, "-2": 0.128958695344879, "-3": 0.05502085273832554, "-4": 0.018338562166100338, "-5": 0.004996796840515148, "-6": 0.0011492140806208596, "-7": 0.00022841288980916433, "-8": 3.994446061107303e-05, "-9": 6.233676622884097e-06, "0": 0.2871951946053098, "1": 0.17958881113240147, "10": 4.2826265659145705e-08, "11": 3.9895406076121185e-09, "12": 3.411945105726108e-10, "13": 2.684995187708412e-11, "14": 1.7972428514138653e-12, "2": 0.0815747524884036, "3": 0.02526490073752116, "4": 0.006112807316273827, "5": 0.0012090722741723995, "6": 0.0002018583197136688, "7": 2.912402995531691e-05, "8": 3.697196788051922e-06, "9": 4.188373667577244e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2625 |
| Legacy raw p draw | 0.2887 |
| Legacy raw p away | 0.4489 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0361 |
| Legacy lambda away | 1.4273 |
| Legacy model home team | Liverpool |
| Legacy model away team | Arsenal |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 60.1% |
| Market home draw odds | 1.57 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T06:59:17Z |
| Market reference home draw last update utc | 2026-11-01T06:59:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.4% |
| Market draw away odds | 1.43 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T06:59:17Z |
| Market reference draw away last update utc | 2026-11-01T06:59:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T06:59:17Z |
| Market reference home away last update utc | 2026-11-01T06:59:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home draw odds | 1.57 |
| Market reference dc home away odds | 1.30 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T06:59:17Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.04, "price": 1.78, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T06:59:17Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.04, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T06:59:17Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.64, "price": 2.24, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T06:59:17Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.24, "price": 1.64, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 77.3% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T06:59:32Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.60 |
| Market reference over 1 5 last update utc | 2026-11-01T06:59:33Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.4% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T06:59:32Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.31 |
| Market reference under 3 5 last update utc | 2026-11-01T06:59:32Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.2% |
| Market btts yes odds | 1.71 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T06:59:17Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.05 |
| Market reference btts yes last update utc | 2026-11-01T06:59:33Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.788153494379117, "version": "count-markets-nb2-v1"}} |
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
| Market best home last update utc | 2026-11-01T06:59:32Z |
| Market best draw last update utc | 2026-11-01T06:59:32Z |
| Market best away last update utc | 2026-11-01T06:59:32Z |
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
| Bbs statistics cutoff utc | 2026-11-01T06:59:16.579426+00:00 |
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
| Goal margin distribution | {"-1": 0.17945578154951197, "-10": 1.0067336650801794e-07, "-11": 1.0509039772302254e-08, "-12": 1.0079775865538091e-09, "-13": 8.940946699985125e-11, "-14": 7.373021924317052e-12, "-15": 5.643063758759501e-13, "-16": 3.6344064374376435e-14, "-2": 0.08452771187280148, "-3": 0.028330340836771425, "-4": 0.007517678652435826, "-5": 0.0016434386050888483, "-6": 0.0003047102019822141, "-7": 4.897827104068662e-05, "-8": 6.942012645777732e-06, "-9": 8.79429751798192e-07, "0": 0.26874345718606013, "1": 0.18547993952491743, "10": 5.306195303443112e-06, "11": 8.59111024428133e-07, "12": 1.2780703178689356e-07, "13": 1.758348667693764e-08, "14": 2.2489750285510577e-09, "15": 2.669756683253133e-10, "16": 2.666906779366704e-11, "2": 0.13302302352083156, "3": 0.0691507856206611, "4": 0.028460773155415918, "5": 0.009650149420392027, "6": 0.0027751417147156496, "7": 0.0006918616176588986, "8": 0.00015209635467953252, "9": 2.988492540477531e-05} |
| Raw goal margin distribution | {"-1": 0.14667959186125634, "-10": 3.146983844944013e-08, "-11": 2.9158055995349387e-09, "-12": 2.481090468323614e-10, "-13": 1.9512890347822762e-11, "-14": 1.4197558033683449e-12, "-15": 8.797647273347114e-14, "-2": 0.06422159566505042, "-3": 0.019588655006629745, "-4": 0.004685568819932189, "-5": 0.0009182426344209691, "-6": 0.0001520966317870524, "-7": 2.1790896418559363e-05, "-8": 2.7485938563547492e-06, "-9": 3.095185536786865e-07, "0": 0.26607216555681446, "1": 0.23201377518267727, "10": 2.5355412784866566e-06, "11": 3.6437817353778696e-07, "12": 4.8089914664392965e-08, "13": 5.866115738322567e-09, "14": 6.620035114263544e-10, "15": 6.362544067960028e-11, "2": 0.15449567505194456, "3": 0.07308991706389088, "4": 0.02711644733229621, "5": 0.008242245370575, "6": 0.0021175091696566273, "7": 0.00047054202434264526, "8": 9.205587467604307e-05, "9": 1.6078489335997355e-05} |
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
| Totals anchor reference last update utc | 2026-11-01T06:59:32Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4859 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.23, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T06:59:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.6, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.12, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.24, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 5.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T06:59:47Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.6, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.43 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.93 |
| Market reference 1x2 last update utc | 2026-11-01T06:59:32Z |
| Market reference home last update utc | 2026-11-01T06:59:32Z |
| Market reference draw last update utc | 2026-11-01T06:59:32Z |
| Market reference away last update utc | 2026-11-01T06:59:32Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-01T06:59:10Z |
| Market reference under 2 5 last update utc | 2026-11-01T06:59:10Z |
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
| Legacy trial matrix | [[0.0803577916863329, 0.07609294040476589, 0.04956473047267138, 0.018562916670442943, 0.00521411907259036, 0.00117167094744069, 0.00021940631932329999, 3.5216469312467926e-05, 4.945959397744006e-06, 6.174513696880922e-07, 6.937411873887168e-08, 7.0859733576725505e-09, 6.634573199181438e-10, 5.734088065594464e-11, 4.601835011402754e-12, 3.446946206835392e-13], [0.09095651198897894, 0.13038443036965613, 0.0758215330061077, 0.028396579293287108, 0.007976286718197056, 0.0017923609503466284, 0.00033563631484877476, 5.387231333389622e-05, 7.56607006931443e-06, 9.44544819673441e-07, 1.0612489937031419e-07, 1.0839751526852438e-08, 1.01492231674807e-09, 8.771708095237553e-11, 7.03964657687627e-12, 5.272958071182291e-13], [0.07738825315610429, 0.0869500356952399, 0.05140296657692423, 0.021719801092569924, 0.006100853176266264, 0.0013709300308865468, 0.0002567194422492252, 4.120552401483922e-05, 5.787089186365637e-06, 7.224576380991864e-07, 8.117216096648384e-08, 8.29104254510588e-09, 7.762875456407337e-10, 6.709250191824462e-11, 5.384441619976688e-12, 4.033147770816699e-13], [0.03946150105127586, 0.044337206036618455, 0.024907666798827947, 0.009816579937600566, 0.0031109220613015076, 0.0006990590257403668, 0.00013090532641647654, 2.1011352019407767e-05, 2.950928812812742e-06, 3.6839263948555165e-07, 4.139097582228568e-08, 4.227734452797394e-09, 3.9584136544084594e-10, 3.4211533753565555e-11, 2.7456124150863286e-12, 2.056566190698158e-13], [0.015091535230276244, 0.016956184865958363, 0.009525611570377414, 0.0035675193253278856, 0.001054519846806686, 0.00026734598618777673, 5.006303087350991e-05, 8.035516916211578e-06, 1.1285441494669367e-06, 1.408869492862564e-07, 1.5829437634059294e-08, 1.616841775880232e-09, 1.5138435571391003e-10, 1.3083753865643341e-11, 1.0500235770838595e-12, 7.865068558843578e-14], [0.004617248295967806, 0.00518773699851266, 0.0029143564998702423, 0.0010914809046502075, 0.0003065849781767635, 7.249854360701534e-05, 1.5316761380774783e-05, 2.458462722478053e-06, 3.4527756596936154e-07, 4.310429764700372e-08, 4.8430091986506976e-09, 4.946720012656998e-10, 4.6315974338645246e-11, 4.002968506465072e-12, 3.212542327893916e-13, 2.4063141255593615e-14], [0.001177204168944104, 0.001322654800125841, 0.0007430383643073023, 0.00027828173598530386, 7.816627811861554e-05, 1.7564838061063207e-05, 3.4613165157153457e-06, 6.268046205403842e-07, 8.80312610558467e-08, 1.098978344607832e-08, 1.2347637063107595e-09, 1.2612056030394714e-10, 1.1808625957537523e-11, 1.0205886519202029e-12, 8.190632123052029e-14, 6.135089210756445e-15], [0.000257260769039725, 0.00028904687906402925, 0.0001623801767531731, 6.0814406963494395e-05, 1.708209786566163e-05, 3.838538689257658e-06, 7.188021920572022e-07, 1.2141148405617026e-07, 1.923794573296252e-08, 2.4016565821832305e-09, 2.698395648333199e-10, 2.7561805497696165e-11, 2.580602647596304e-12, 2.2303473636328437e-13, 1.789942963579405e-14, 1.3407340970446936e-15], [4.919300908353872e-05, 5.52711002164876e-05, 3.105008797035822e-05, 1.162883748397427e-05, 3.2664125144616665e-06, 7.339994718705388e-07, 1.374482510299787e-07, 2.2061543757621386e-08, 3.260575994422642e-09, 4.592410825166929e-10, 5.159830709319656e-11, 5.2703261102260445e-12, 4.93458874270124e-13, 4.2648359688956334e-14, 3.4227014400622123e-15, 2.5637311456666475e-16], [8.36143256242314e-06, 9.394537673560167e-06, 5.277644556781809e-06, 1.9765763919118783e-06, 5.551985631605833e-07, 1.2475933469484403e-07, 2.3362349716369516e-08, 3.749844008099631e-09, 5.266449639620249e-10, 6.918689506626477e-11, 8.770265798587474e-12, 8.958077005982357e-13, 8.387417595317537e-14, 7.249025625401357e-15, 5.817632994108775e-16, 4.357624280773809e-17], [1.279088232628778e-06, 1.4371272505672388e-06, 8.07346468225371e-07, 3.0236632119097726e-07, 8.493137313605349e-08, 1.9085030672366573e-08, 3.5738501011250856e-09, 5.736315289450569e-10, 8.056339283346637e-11, 1.0057498101264905e-11, 1.1891547475813196e-12, 1.3703597798334566e-13, 1.2830632870888314e-14, 1.108918036024712e-15, 8.899510758430352e-17, 6.666065770600368e-18], [1.778802087751421e-07, 1.9985837477525934e-07, 1.1227603746041337e-07, 4.204947162205065e-08, 1.1811233970897833e-08, 2.6541165448011927e-09, 4.970080920943733e-10, 7.977377441667428e-11, 1.120378780078253e-11, 1.3986758820631073e-12, 1.5714906708921561e-13, 1.6891473526024734e-14, 1.7843301154449735e-15, 1.5421498433864831e-16, 1.2376369286524838e-17, 9.27036259684955e-19], [2.2675986856242217e-08, 2.5477740951173396e-08, 1.43128342790605e-08, 5.360423581573844e-09, 1.5056840113036168e-09, 3.3834405918044644e-10, 6.33580826185368e-11, 1.016947907022093e-11, 1.4282473955932005e-12, 1.783017691299124e-13, 2.003320214386752e-14, 2.046220395168405e-15, 2.0161348553193813e-16, 1.9659168279475695e-17, 1.5777268826123395e-18, 1.1817763305219166e-19], [2.668349153599205e-09, 2.998039685490862e-09, 1.6842327293739556e-09, 6.307765927677075e-10, 1.771782054126512e-10, 3.9813926937911256e-11, 7.455529375662085e-12, 1.1966721025902763e-12, 1.6806601420798938e-13, 2.098128640483282e-14, 2.3573650101034295e-15, 2.4078468973102326e-16, 2.2544590116655177e-17, 2.05044160926323e-18, 1.8565569906698215e-19, 1.3906304899906346e-20], [2.915643579215118e-10, 3.2758888196632544e-10, 1.8403222594312406e-10, 6.892350351308628e-11, 1.9359853874124864e-11, 4.3503759724727875e-12, 8.14648499971527e-13, 1.307576007299105e-13, 1.836418575690653e-14, 2.292576775697053e-15, 2.5758383779362146e-16, 2.6309987718084497e-17, 2.4633953667944704e-18, 2.129048176802033e-19, 1.7980669899796736e-20, 1.5195098638920399e-21], [2.973466061684007e-11, 3.3408556164265265e-11, 1.876819176386953e-11, 7.029038117330176e-12, 1.97437947711594e-12, 4.4366517917103023e-13, 8.308044522778067e-14, 1.3335076030873482e-14, 1.872838075541523e-15, 2.3380427172018136e-16, 2.6269219090346912e-17, 2.6831762332248815e-18, 2.5122489497309554e-19, 2.1712710505977714e-20, 1.742531859571326e-21, 1.3735291572234043e-22]] |
| Legacy trial inputs | {"lambda_home": 1.5297477113875078, "lambda_away": 1.1235559939548967, "rho": -0.0899136506170151, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4278 |
| Legacy p draw | 0.2731 |
| Legacy p away | 0.2991 |
| Legacy p over 1 5 | 0.7526 |
| Legacy p under 3 5 | 0.7255 |
| Legacy p btts yes | 0.5398 |
| Legacy p over 2 5 | 0.4953 |
| Legacy goal margin distribution | {"-1": 0.17702850582303004, "-10": 8.102544343183675e-08, "-11": 8.170812439439539e-09, "-12": 7.567644991095659e-10, "-13": 6.478384200990258e-11, "-14": 5.1291308185209835e-12, "-15": 3.446946206835392e-13, "-2": 0.08481383394698586, "-3": 0.02804943080540354, "-4": 0.007285383728479045, "-5": 0.0015516095738200015, "-6": 0.00027945045062780974, "-7": 4.35480521921985e-05, "-8": 5.976059583408005e-06, "-9": 7.322765641121407e-07, "0": 0.2730923730198965, "1": 0.20670662502521006, "10": 1.4939100217949189e-06, "11": 2.0511308033867966e-07, "12": 2.5865087805793532e-08, "13": 3.0147062273294e-09, "14": 3.2497291408577706e-10, "15": 2.973466061684007e-11, "2": 0.13242469776463564, "3": 0.05962816419779303, "4": 0.02108651982698222, "5": 0.006114486901272582, "6": 0.001499365362433437, "7": 0.0003181240373003753, "8": 5.943848902286812e-05, "9": 9.916377885694197e-06} |
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
| Market p home draw | 68.0% |
| Market home draw odds | 1.44 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T06:59:25Z |
| Market reference home draw last update utc | 2026-11-01T06:59:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.8% |
| Market draw away odds | 1.61 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T06:59:25Z |
| Market reference draw away last update utc | 2026-11-01T06:59:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.2% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T06:59:25Z |
| Market reference home away last update utc | 2026-11-01T06:59:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.62 |
| Market reference dc home draw odds | 1.40 |
| Market reference dc home away odds | 1.30 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T06:59:25Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.27, "price": 1.61, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T06:59:25Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.27, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T06:59:25Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.81, "price": 2.02, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T06:59:25Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.02, "price": 1.81, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T06:59:25Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.5, "price": 2.52, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T06:59:25Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.52, "price": 1.5, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 80.6% |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.25 |
| Market reference over 1 5 last update utc | 2026-11-01T06:59:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.9% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T06:59:32Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.77 |
| Market reference under 3 5 last update utc | 2026-11-01T06:59:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T06:59:25Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-11-01T06:59:33Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 10.130671706390222, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,496.2139 |
| Elo away rating | 1,476.4968 |
| Elo rating diff | 79.7171 |
| Elo home expectancy | 0.6128 |

</details>


---
