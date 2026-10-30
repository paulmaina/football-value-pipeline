# Premier League — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
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
| Training sha256 | caec3d999508121198de612578e3af7a9d9a0431629bf22227bd2f33a911fe1d |
| Training as of utc | 2026-10-30T06:51:51.118483+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 80, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 80, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 166, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-30T06:51:51.118483+00:00', 'observations': 441, 'observations_sha256': '81e21d5556bad4ceb97313573c6a1780e32425548ccd50a954ec78000a67b1c7', 'eligible_training_matches': 222, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 205, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 18, 'retrospective_eligible_training_matches': 222, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'c1bea8bcc71272d16515e30303b9d6597c8fbc0948816402b03c46fe3d949b4a', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 161, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-21T00:00:00+00:00', 'audit_origin_utc': '2025-10-19T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 31, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1979, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1609, 'tuning_matches': 249, 'audit_matches': 114, 'audit_matchdays': 38, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9291857747736281, 'audit_candidate_poisson_score': 0.9172214195203522, 'audit_gain': 0.011964355253275882, 'audit_gain_lower95': 0.0018385349221286726, 'audit_baseline_briers': [0.6363657019212162, 0.15621635836881023, 0.2172863699964663, 0.25224676296374665], 'audit_candidate_briers': [0.6347789666987903, 0.15464943556253888, 0.21528153413704115, 0.2489835188738788], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1867.561 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.175 |
| Dixon-Coles low-score adjustment | -0.076 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1980, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261030T065151118483Z_60701e3d60548b90cd33aac756bad765f4a8497c0ace47267d86457d7daabc0d.json |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 5, 'ANCHORED_MAIN': 4} |
| Shot features applied fixtures | 9 |
| Goal rate features used | {'shot_features': 9} |
| Legacy comparison status | {'AVAILABLE': 9} |
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

## 2026-10-31 — Aston Villa vs Fulham

The model's most likely 1X2 outcome is **Aston Villa win** at **48.5%**. Expected goals are 1.56 for Aston Villa and 1.15 for Fulham (2.72 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 56.9%; Under 3.5 goals: 65.4%; Double Chance 1X: 74.2%; Double Chance X2: 51.5%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 59.5%; BTTS No (at least one team does not score): 40.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 48.5% | 2.06 |
| Draw | 25.7% | 3.89 |
| Fulham win | 25.8% | 3.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.56 |
| Fulham expected goals | 1.15 |
| Expected total goals | 2.72 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 56.9% |
| Under 2.5 | 43.1% |
| Over 3.5 | 34.6% |
| Under 3.5 | 65.4% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.02% |
| 2 | 2-1 | 9.72% |
| 3 | 1-0 | 8.17% |
| 4 | 2-0 | 7.72% |
| 5 | 1-2 | 6.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 48.5% | 49.6% | 1.97 | -4.5% |
| Draw | 25.7% | 25.2% | 3.79 | -2.5% |
| Fulham win | 25.8% | 25.2% | 3.79 | -2.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:00:00+00:00 |
| Fixture id | 640c52a86289f35698261b41987dd71e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T06:52:26Z |
| Market best draw last update utc | 2026-10-30T06:52:26Z |
| Market best away last update utc | 2026-10-30T06:52:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Aston Villa |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5968 |
| Dc lambda away | 1.1022 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T06:51:51.118483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.4880 |
| Shot lambda away | 1.2702 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.5% |
| P btts no | 40.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.57 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.13 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.57 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.14670220675917467, "-10": 1.6250223947874355e-07, "-11": 1.8312782512758436e-08, "-12": 1.8963078107058944e-09, "-13": 1.8160328227629274e-10, "-14": 1.616861324127711e-11, "-15": 1.335762426507999e-12, "-16": 9.268319843710624e-14, "-2": 0.07439982707242747, "-3": 0.0268592296791044, "-4": 0.007683541083793407, "-5": 0.0018116862470047652, "-6": 0.00036241349088341824, "-7": 6.286359329117866e-05, "-8": 9.61662215010698e-06, "-9": 1.314998295865031e-06, "0": 0.25714508252753754, "1": 0.22083646880003527, "10": 3.7656228696790945e-06, "11": 5.758858279097612e-07, "12": 8.092737771147423e-08, "13": 1.0517557836498244e-08, "14": 1.2707747265229179e-09, "15": 1.424720260210473e-10, "16": 1.3415472417131962e-11, "2": 0.1498693249119428, "3": 0.07342415528252881, "4": 0.02850436723357907, "5": 0.009120897080908538, "6": 0.0024760733430026455, "7": 0.0005828582276047324, "8": 0.00012100153032134069, "9": 2.245422558835105e-05} |
| Raw goal margin distribution | {"-1": 0.15983658486223687, "-10": 8.868953970178121e-08, "-11": 9.169300218307126e-09, "-12": 8.707450392820222e-10, "-13": 7.643186616974995e-11, "-14": 6.202191625835349e-12, "-15": 4.254447852348663e-13, "-2": 0.07699596644374984, "-3": 0.0259847112417409, "-4": 0.006899524750517191, "-5": 0.0015037326109172394, "-6": 0.00027732739093286877, "-7": 4.4273099431717106e-05, "-8": 6.2258142022605366e-06, "-9": 7.81911306905063e-07, "0": 0.2690565605072868, "1": 0.22013487297921064, "10": 1.878962922722182e-06, "11": 2.636249939844377e-07, "12": 3.397394506470313e-08, "13": 4.047007560473339e-09, "14": 4.456658055930488e-10, "15": 4.14869892577236e-11, "2": 0.14180029568280214, "3": 0.06494289400088256, "4": 0.023401166179160642, "5": 0.006921393215655206, "6": 0.0017322886166252882, "7": 0.00037529432157175656, "8": 7.161975043758377e-05, "9": 1.2206712665084348e-05} |
| Unadjusted home-win probability | 45.9% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 27.2% |
| Raw p over 1 5 | 76.3% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 55.0% |
| P home draw | 74.2% |
| P draw away | 51.5% |
| P home away | 74.3% |
| Raw p home draw | 72.8% |
| Raw p draw away | 54.1% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0928 |
| Totals anchor target over 2 5 | 0.5693 |
| Totals anchor reference over odds | 1.71 |
| Totals anchor reference under odds | 2.23 |
| Totals anchor reference last update utc | 2026-10-30T06:52:47Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5153 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.85, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.22, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.32, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.99, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.97 |
| Reference draw odds | 3.79 |
| Reference away odds | 3.79 |
| Market reference 1x2 last update utc | 2026-10-30T06:52:26Z |
| Market reference home last update utc | 2026-10-30T06:52:26Z |
| Market reference draw last update utc | 2026-10-30T06:52:26Z |
| Market reference away last update utc | 2026-10-30T06:52:26Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-30T06:51:37Z |
| Market reference under 2 5 last update utc | 2026-10-30T06:51:37Z |
| Home probability edge | -1.1% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | -0.0365 |
| Raw ev home | -0.0950 |
| Raw edge prob draw | 0.0170 |
| Raw ev draw | 0.0197 |
| Raw edge prob away | 0.0195 |
| Raw ev away | 0.0292 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08381822275279682, 0.06727875062469266, 0.041269095371418534, 0.014185268371462398, 0.003656886048011797, 0.0007541804761365794, 0.00012961578583479068, 1.909385936408279e-05, 2.461147229744494e-06, 2.819869092630651e-07, 2.907788466746538e-08, 2.7258627615795773e-09, 2.342375963707303e-10, 1.858006002927964e-11, 1.3685256424995438e-12, 9.407961738617951e-14], [0.10650931826302396, 0.12688641582828442, 0.06396682150467904, 0.021987070996999057, 0.005668148889401774, 0.0011689746883270294, 0.00020090360018952302, 2.9595354169638692e-05, 3.81476172726657e-06, 4.370778212884922e-07, 4.507052654092301e-08, 4.225069029183785e-09, 3.630667060152848e-10, 2.879896864088446e-11, 2.1212055827851197e-12, 1.4582277702985643e-13], [0.0923405362258435, 0.09521957843802226, 0.04597170813581713, 0.017039906414447307, 0.0043927964134805484, 0.0009059514699647352, 0.0001556996175626238, 2.2936300402263525e-05, 2.9564275675877785e-06, 3.3873384825122695e-07, 3.492950718228967e-08, 3.2744143529485016e-09, 2.8137548168860225e-10, 2.2319104283615232e-11, 1.6439272252950347e-12, 1.1301216401323818e-13], [0.047709070958504435, 0.04919656967583291, 0.02536522320854006, 0.008164165796371055, 0.0022696016761742915, 0.0004680729041880126, 8.044445490699084e-05, 1.1850370683800615e-05, 1.527480978242885e-06, 1.7501173225526652e-07, 1.8046834086274828e-08, 1.6917734409760132e-09, 1.453767042139815e-10, 1.1531487399996769e-11, 8.493587307138436e-13, 5.838936584573067e-14], [0.018487185136303493, 0.019063588399347197, 0.009828981534513665, 0.0033784782445652173, 0.0008155592492118258, 0.00018137746686657126, 3.117209162064928e-05, 4.5919988036613195e-06, 5.918963222218109e-07, 6.781675329713263e-08, 6.993117999872575e-09, 6.555593765220785e-10, 5.633322953714791e-11, 4.468432064965411e-12, 3.291250864117602e-13, 2.262578152737974e-14], [0.005731002635724766, 0.005909686875396112, 0.0030469711135294557, 0.0010473237316329204, 0.000269994436599104, 5.2140980421194966e-05, 9.663306659280599e-06, 1.4235134799050336e-06, 1.8348706726952026e-07, 2.1023102707450644e-08, 2.1678572153476864e-09, 2.0322252885023732e-10, 1.746322571965306e-11, 1.385207956379792e-12, 1.020283360501948e-13, 7.013961974887929e-15], [0.0014805026188197824, 0.0015266625146687564, 0.0007871308041159367, 0.00027055746192979296, 6.974826149267579e-05, 1.4384581956236877e-05, 2.314943397830338e-06, 3.6773939376458494e-07, 4.7400620952206553e-08, 5.4309447390721315e-09, 5.600273614502923e-10, 5.2498926503792426e-11, 4.511313823138329e-12, 3.5784384293358956e-13, 2.635720628961731e-14, 1.811932349741578e-15], [0.0003278241637613371, 0.0003380452394039208, 0.0001742924965818695, 5.99088934926908e-05, 1.544419118682209e-05, 3.1851436741253016e-06, 5.47408628811678e-07, 7.551061040047471e-08, 1.0495806442958245e-08, 1.2025611403103345e-09, 1.2400552293332893e-10, 1.1624712081356086e-11, 9.98929459992605e-13, 7.923650865296244e-14, 5.83621332454437e-15, 4.0121185859141847e-16], [6.351565735665808e-05, 6.54959822078898e-05, 3.376902533880918e-05, 1.1607297973521267e-05, 2.992299116446649e-06, 6.171189210590133e-07, 1.0605996367916659e-07, 1.5623822496674412e-08, 1.885782891410394e-09, 2.329952144528021e-10, 2.4025966282035984e-11, 2.252278236471769e-12, 1.9354174682057006e-13, 1.535200723459602e-14, 1.1307614470176563e-15, 7.77344618082297e-17], [1.0938760403100083e-05, 1.1279814876429215e-05, 5.815751463504732e-06, 1.999026015691997e-06, 5.15338177253184e-07, 1.0628113285167084e-07, 1.8265803729830805e-08, 2.690757806567376e-09, 3.4683146006636503e-10, 3.721091564487534e-11, 4.137787429899019e-12, 3.878906873550427e-13, 3.333204574392626e-14, 2.6439453803165485e-15, 1.9474140797335675e-16, 1.3387543924947246e-17], [1.6955005383329851e-06, 1.7483637533428446e-06, 9.014375828534088e-07, 3.098476939660247e-07, 7.987707242483229e-08, 1.647350443050002e-08, 2.8311873480870704e-09, 4.170656583963326e-10, 5.3758644086095985e-11, 6.159417733649817e-12, 5.947494391024457e-13, 6.012279682425814e-14, 5.166444772531104e-15, 4.098097636711443e-16, 3.0184787844971406e-17, 2.0750603446137903e-18], [2.3891040745786335e-07, 2.46359282850115e-07, 1.270202016149661e-07, 4.366016827578506e-08, 1.1255357039473893e-08, 2.3212565061284174e-09, 3.989383120963592e-10, 5.876808891026194e-11, 7.575048944318921e-12, 8.679142042008978e-13, 8.949744935664744e-14, 7.856196818907693e-15, 7.27995891365233e-16, 5.774567179739539e-17, 4.2532926413350355e-18, 2.92393603672199e-19], [3.085912765942547e-08, 3.182126990803886e-08, 1.6406705168980652e-08, 5.6394140413999145e-09, 1.4538106708256181e-09, 2.998276701927376e-10, 5.152930938510305e-11, 7.590845360313961e-12, 9.784395953548487e-13, 1.1210510044267499e-13, 1.1560037272034084e-14, 1.0836783859166597e-15, 8.719941019076719e-17, 7.458783720376007e-18, 5.49381259646472e-19, 3.7767343995306e-20], [3.6793416347680745e-09, 3.794058099632607e-09, 1.9561756276398568e-09, 6.723887696119244e-10, 1.7333821581975295e-10, 3.5748529328848454e-11, 6.1438526559757186e-12, 9.050584217910846e-13, 1.1665960165906216e-13, 1.3366319621242018e-14, 1.378306182335474e-15, 1.2920724940789413e-16, 1.110297846302452e-17, 8.246896177532803e-19, 6.550286723225628e-20, 4.503010024461738e-21], [4.073539213228961e-10, 4.2005461792613864e-10, 2.165756517920094e-10, 7.44427207755498e-11, 1.919093385133335e-11, 3.957855793010888e-12, 6.802093200023151e-13, 1.002024638481687e-13, 1.2915828676176058e-14, 1.4798361369645726e-15, 1.5259752528887882e-16, 1.4305026533087574e-17, 1.229253019762541e-18, 9.750610171995111e-20, 6.725090609758392e-21, 4.98545384828453e-22], [4.209305670499224e-11, 4.3405456351415226e-11, 2.2379387345029353e-11, 7.692381250935061e-12, 1.983054598327063e-12, 4.089766652653194e-13, 7.028799277330619e-14, 1.0354209869990588e-14, 1.334629864597024e-15, 1.5291574026108494e-16, 1.5768342831134125e-17, 1.4781796897110887e-18, 1.270222633370272e-19, 1.007558698699079e-20, 7.421234986971251e-22, 4.777264709980067e-23]] |
| Legacy trial inputs | {"lambda_home": 1.5499933044081247, "lambda_away": 1.0311785303600283, "rho": -0.10287979955549995, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4884 |
| Legacy p draw | 0.2657 |
| Legacy p away | 0.2459 |
| Legacy p over 1 5 | 0.7424 |
| Legacy p under 3 5 | 0.7392 |
| Legacy p btts yes | 0.5162 |
| Legacy p over 2 5 | 0.4819 |
| Legacy goal margin distribution | {"-1": 0.1507464994659132, "-10": 3.3596196804786155e-08, "-11": 3.112120556390719e-09, "-12": 2.6473888160275553e-10, "-13": 2.0814277776077996e-11, "-14": 1.5143484195294002e-12, "-15": 9.407961738617951e-14, "-2": 0.06814967991878787, "-3": 0.020844594228843112, "-4": 0.004994024215858469, "-5": 0.0009796178958305264, "-6": 0.00016234978023649564, "-7": 2.3266075160046895e-05, "-8": 2.9349040768521634e-06, "-9": 3.304817991334839e-07, "0": 0.2657106051205072, "1": 0.23075754055823958, "10": 1.958958515032209e-06, "11": 2.7276427876891594e-07, "12": 3.487745379210102e-08, "13": 4.1217756400392425e-09, "14": 4.5075937767431133e-10, "15": 4.209305670499224e-11, "2": 0.1524864533783495, "3": 0.0701062679339767, "4": 0.02524701318050493, "5": 0.007444097163277909, "6": 0.001854398160354572, "7": 0.00039945730655679707, "8": 7.574206023398018e-05, "9": 1.28199611384589e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4809 |
| Legacy raw p draw | 0.2794 |
| Legacy raw p away | 0.2398 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5500 |
| Legacy lambda away | 1.0312 |
| Legacy model home team | Aston Villa |
| Legacy model away team | Fulham |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 73.5% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T06:52:39Z |
| Market reference home draw last update utc | 2026-10-30T06:52:47Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.9% |
| Market draw away odds | 1.90 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T06:52:39Z |
| Market reference draw away last update utc | 2026-10-30T06:52:47Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.6% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T06:52:39Z |
| Market reference home away last update utc | 2026-10-30T06:52:47Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.32 |
| Market reference dc draw away odds | 1.87 |
| Market reference dc home away odds | 1.30 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.15, "price": 1.69, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.69, "price": 2.15, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.72, "price": 2.1, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.1, "price": 1.72, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 81.0% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-30T06:52:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.8% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T06:52:47Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.73 |
| Market reference under 3 5 last update utc | 2026-10-30T06:52:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.9% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T06:52:39Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.26 |
| Market reference btts yes last update utc | 2026-10-30T06:52:47Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.734510102202092, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,530.3526 |
| Elo away rating | 1,453.3052 |
| Elo rating diff | 137.0473 |
| Elo home expectancy | 0.6876 |

</details>


---

## 2026-10-31 — Bournemouth vs Leeds United

The model's most likely 1X2 outcome is **Bournemouth win** at **45.1%**. Expected goals are 1.64 for Bournemouth and 1.19 for Leeds United (2.83 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.5%; Double Chance 1X: 72.7%; Double Chance X2: 54.9%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 45.1% | 2.22 |
| Draw | 27.6% | 3.62 |
| Leeds United win | 27.3% | 3.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.64 |
| Leeds United expected goals | 1.19 |
| Expected total goals | 2.83 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.5% |
| Under 3.5 | 71.5% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.15% |
| 2 | 1-0 | 9.35% |
| 3 | 2-1 | 9.10% |
| 4 | 2-0 | 8.01% |
| 5 | 0-0 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 45.1% | 44.3% | 2.20 | -0.7% |
| Draw | 27.6% | 28.2% | 3.41 | -5.9% |
| Leeds United win | 27.3% | 27.5% | 3.50 | -4.5% |
| Over 2.5 | 50.4% | 50.4% | 1.93 | -2.7% |
| Under 2.5 | 49.6% | 49.6% | 1.96 | -2.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | a6c06eabdf4e6710354b6098d39449e7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T06:52:26Z |
| Market best draw last update utc | 2026-10-30T06:52:26Z |
| Market best away last update utc | 2026-10-30T06:52:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Bournemouth |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6062 |
| Dc lambda away | 1.1733 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T06:51:51.118483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7240 |
| Shot lambda away | 1.2382 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.82 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.16 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.50 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.34 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.16167110538531546, "-10": 7.975610280293611e-08, "-11": 8.132751547732685e-09, "-12": 7.617114527257023e-10, "-13": 6.594271820086264e-11, "-14": 5.278198121970347e-12, "-15": 3.575679682121977e-13, "-2": 0.07703970446956916, "-3": 0.025678620459873593, "-4": 0.006730551843181423, "-5": 0.0014475970058945573, "-6": 0.0002634106160694193, "-7": 4.1484869263811456e-05, "-8": 5.754635093875553e-06, "-9": 7.128925055008424e-07, "0": 0.2758832706520896, "1": 0.2158535874731563, "10": 1.8573073986968417e-06, "11": 2.6065105398366566e-07, "12": 3.3598089452668885e-08, "13": 4.003068831814648e-09, "14": 4.409750484824818e-10, "15": 4.1113935638983456e-11, "2": 0.139385482685141, "3": 0.06394060477104481, "4": 0.02306523274531524, "5": 0.006827425341672154, "6": 0.00170979748461859, "7": 0.00037059814544064014, "8": 7.075113673128401e-05, "9": 1.206262417929818e-05} |
| Raw goal margin distribution | {"-1": 0.1564045425140927, "-10": 1.1261288285666085e-07, "-11": 1.2034620297205259e-08, "-12": 1.1815163138279915e-09, "-13": 1.0722744556183377e-10, "-14": 8.988783467111892e-12, "-15": 6.322379638928575e-13, "-2": 0.07670026654163561, "-3": 0.026531308525800393, "-4": 0.007243899248290321, "-5": 0.0016264756165644775, "-6": 0.00030938507483438486, "-7": 5.098127535481868e-05, "-8": 7.403939170276066e-06, "-9": 9.606978403746376e-07, "0": 0.26143587992643635, "1": 0.21853478819802757, "10": 2.7454228106997063e-06, "11": 4.03790102858995e-07, "12": 5.4558838507799124e-08, "13": 6.814491745557185e-09, "14": 7.861954835268485e-10, "15": 7.610484614022983e-11, "2": 0.14527841915605674, "3": 0.06916159785895144, "4": 0.025988479184255, "5": 0.008030787559803245, "6": 0.0021023840627477242, "7": 0.0004767882110124669, "8": 9.529711893551186e-05, "9": 1.7017895778648974e-05} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 26.9% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.0% |
| P home draw | 72.7% |
| P draw away | 54.9% |
| P home away | 72.4% |
| Raw p home draw | 73.1% |
| Raw p draw away | 53.0% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9529 |
| Totals anchor target over 2 5 | 0.5040 |
| Totals anchor reference over odds | 1.93 |
| Totals anchor reference under odds | 1.96 |
| Totals anchor reference last update utc | 2026-10-30T06:52:26Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5331 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.23, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.14, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.57, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.52, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:45Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.49, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.8, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:39Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.5, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:39Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.56, "price": 2.5, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.20 |
| Reference draw odds | 3.41 |
| Reference away odds | 3.50 |
| Market reference 1x2 last update utc | 2026-10-30T06:52:26Z |
| Market reference home last update utc | 2026-10-30T06:52:26Z |
| Market reference draw last update utc | 2026-10-30T06:52:26Z |
| Market reference away last update utc | 2026-10-30T06:52:26Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference under 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market best over 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market best under 2 5 last update utc | 2026-10-30T06:52:26Z |
| Home probability edge | +0.8% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0264 |
| Raw ev home | 0.0333 |
| Raw edge prob draw | -0.0206 |
| Raw ev draw | -0.1085 |
| Raw edge prob away | -0.0057 |
| Raw ev away | -0.0589 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08683912355460272, 0.07138239914787237, 0.048080574837902755, 0.01837488413313658, 0.005266727280889786, 0.0012076665539891532, 0.00023076609499603643, 3.7796377123527924e-05, 5.4167201565178844e-06, 6.90033383843677e-07, 7.911271975555761e-08, 8.245743906499695e-09, 7.878160222931001e-10, 6.947965757321858e-11, 5.689915886681809e-12, 4.3490139415991913e-13], [0.09719652366845803, 0.1357676324693586, 0.06959978193641653, 0.026598848559627786, 0.0076239327733564665, 0.0017481764536493843, 0.00033404904047405727, 5.4712732005656936e-05, 7.841057287173677e-06, 9.98868528637217e-07, 1.1452084468513853e-07, 1.19362545005077e-08, 1.1404153037369665e-09, 1.00576356094245e-10, 8.236526004206984e-12, 6.295482593421968e-13], [0.0797566455771459, 0.09144144758679554, 0.051076662502575275, 0.01925178791800206, 0.0055180710745705245, 0.0012652999716681673, 0.00024177893516713302, 3.960013196158181e-05, 5.675222053585188e-06, 7.229638165795687e-07, 8.288821259034202e-08, 8.639255179183122e-09, 8.254129315699677e-10, 7.279543220644413e-11, 5.961455491527514e-12, 4.556561742074496e-13], [0.03848432316560289, 0.044122495300493905, 0.025293345853645458, 0.009418775430046275, 0.0026625897935881695, 0.0006105348671416436, 0.00011666361603193527, 1.9107928433824814e-05, 2.738418572725342e-06, 3.4884582912120783e-07, 3.9995372634628134e-08, 4.16862928248655e-09, 3.982797643223429e-10, 3.512538569971268e-11, 2.876532457115316e-12, 2.1986405438328184e-13], [0.013927144742584456, 0.015967550625996682, 0.009153443785723659, 0.00349815844650138, 0.0009769872583375691, 0.00022094730439942332, 4.2219556770646016e-05, 6.914994552033052e-06, 9.91010070880375e-07, 1.2624429781736124e-07, 1.4473980517187074e-08, 1.5085909954954682e-09, 1.4413401274827377e-10, 1.271157423436892e-11, 1.0409922948260201e-12, 7.95669056179296e-14], [0.004032090882227352, 0.004622815119722625, 0.002650041908198626, 0.0010127627045906158, 0.0002902845496432865, 6.48579669860049e-05, 1.2223114863313454e-05, 2.0019815259513305e-06, 2.8691040014643626e-07, 3.654937832347942e-08, 4.190407003844811e-09, 4.367568593832811e-10, 4.172868519447222e-11, 3.680167293188038e-12, 3.0138090886660936e-13, 2.3035661695116668e-14], [0.0009727859504486386, 0.0011153046226734687, 0.0006393515453132999, 0.0002443400605146789, 7.00343171256369e-05, 1.605894854874893e-05, 2.9900281065728122e-06, 4.8299990213201e-07, 6.922026671826215e-08, 8.817936591516546e-09, 1.010981443391969e-09, 1.0537236113473368e-10, 1.0067500925339465e-11, 8.878805420517448e-13, 7.271143494586241e-14, 5.557604902972479e-15], [0.00020116734178673924, 0.0002306395010353615, 0.00013221474958453487, 5.052832068871883e-05, 1.4482751733324645e-05, 3.3209114399236e-06, 6.34573974320495e-07, 1.012729896707808e-07, 1.4314410119780094e-08, 1.823505842514798e-09, 2.0906598154412916e-10, 2.1790485129324324e-11, 2.0819095903390185e-12, 1.8360932164608713e-13, 1.5036366508801513e-14, 1.1492853124742487e-15], [3.640036326595723e-05, 4.17332234278183e-05, 2.39236889608882e-05, 9.142881801549904e-06, 2.6205914911504776e-06, 6.009046086389188e-07, 1.1482342501137964e-07, 1.8806529938550003e-08, 2.6262018151126837e-09, 3.299555210880134e-10, 3.782958807910172e-11, 3.942894345592681e-12, 3.7671256528089174e-13, 3.32233152139515e-14, 2.7207656981453815e-15, 2.0795822273498619e-16], [5.8546567212277e-06, 6.712397215790489e-06, 3.84790078461712e-06, 1.4705467085515614e-06, 4.21497540427164e-07, 9.664986527963514e-08, 1.8468270002842795e-08, 3.0248537934421153e-09, 4.335015088855726e-10, 5.3809321819331905e-11, 6.084534115507647e-12, 6.341775413847049e-13, 6.059067971872073e-14, 5.3436583667487895e-15, 4.3760962123227153e-16, 3.3448127909443725e-17], [8.474999154727184e-07, 9.716634712972274e-07, 5.570088469724278e-07, 2.1287126992046602e-07, 6.10145302949671e-08, 1.3990701172615296e-08, 2.673403072393025e-09, 4.3786740304766395e-10, 6.275218336981811e-11, 7.993970554700102e-12, 8.930421528823262e-13, 9.180135374453335e-14, 8.770897831441488e-15, 7.735295560052957e-16, 6.3346859545102e-17, 4.841835640541177e-18], [1.1152833173914156e-07, 1.278678663999601e-07, 7.330061789106741e-08, 2.8013191713629532e-08, 8.029320890078657e-09, 1.8411324097564048e-09, 3.5181146249906327e-10, 5.762197741060222e-11, 8.257990586725678e-12, 1.0519814617801248e-12, 1.206102726657454e-13, 1.224901111112061e-14, 1.1542226555261676e-15, 1.0179406434992925e-16, 8.336248106925464e-18, 6.371703898559956e-19], [1.345371388713341e-08, 1.542475945867227e-08, 8.842287206116368e-09, 3.3792441839988475e-09, 9.685806671596597e-10, 2.2209664829495458e-10, 4.2439178322392385e-11, 6.950965603128762e-12, 9.961651977033632e-13, 1.2690100695186017e-13, 1.4549272592809748e-14, 1.5164385221092876e-15, 1.4117343328028005e-16, 1.2279464740632876e-17, 1.0056054383118848e-18, 7.686215680627197e-20], [1.4980870948023428e-09, 1.7175653711178225e-09, 9.845992313458685e-10, 3.762828721276751e-10, 1.0785261303457815e-10, 2.4730726801595384e-11, 4.725653146198866e-12, 7.739983140581651e-13, 1.1092418342550369e-13, 1.4130578547074385e-14, 1.620078863940655e-15, 1.688572389075167e-16, 1.6132982032907427e-17, 1.3863749808485972e-18, 1.1197536548170757e-19, 8.558692875152584e-21], [1.5489851518076415e-10, 1.7759202828401054e-10, 1.0180513503703819e-10, 3.8906722034222187e-11, 1.115169450119714e-11, 2.5570962290504756e-12, 4.886208940355969e-13, 8.002951898857586e-14, 1.1469287313042529e-14, 1.4610670121791366e-15, 1.6751216359236887e-16, 1.7459422536277085e-17, 1.668110599848015e-18, 1.4711525279004393e-19, 1.1739215662109436e-20, 8.849477596122253e-22], [1.494838322989033e-11, 1.7138406357639408e-11, 9.824640162163204e-12, 3.7546686003262325e-12, 1.0761872240803566e-12, 2.467709541498612e-13, 4.71540503125674e-14, 7.723198109090586e-15, 1.106836317501188e-15, 1.4099934784472886e-16, 1.6165655391367964e-17, 1.6849105282919096e-18, 1.6097995831187255e-19, 1.4197264416004333e-20, 1.1626603119469472e-21, 8.659065070331543e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4475655120818105, "lambda_away": 1.1465056852014588, "rho": -0.10287979955549995, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T06:52:26Z", "over": 1.93, "under": 1.96, "bookmaker": "pinnacle", "event_id": "a6c06eabdf4e6710354b6098d39449e7", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Bournemouth", "away_team": "Leeds United"}} |
| Legacy p home | 0.4353 |
| Legacy p draw | 0.2841 |
| Legacy p away | 0.2806 |
| Legacy p over 1 5 | 0.7446 |
| Legacy p under 3 5 | 0.7369 |
| Legacy p btts yes | 0.5340 |
| Legacy p over 2 5 | 0.4810 |
| Legacy goal margin distribution | {"-1": 0.1631302268655871, "-10": 9.19105766012915e-08, "-11": 9.461910741805837e-09, "-12": 8.945736979332559e-10, "-13": 7.817183975163301e-11, "-14": 6.319464146024006e-12, "-15": 4.3490139415991913e-13, "-2": 0.08085232195978449, "-3": 0.027387991430152168, "-4": 0.0072768191907433815, "-5": 0.0015841846871902752, "-6": 0.0002915178158756408, "-7": 4.6401944822721354e-05, "-8": 6.502793415068692e-06, "-9": 8.136047819850692e-07, "0": 0.28414713316391926, "1": 0.21773647287571432, "10": 9.84597750416378e-07, "11": 1.27977673338418e-07, "12": 1.5276839061888598e-08, "13": 1.6855037632485165e-09, "14": 1.7203692153840354e-10, "15": 1.494838322989033e-11, "2": 0.13411882050861734, "3": 0.05736135833117878, "4": 0.01924255970170104, "5": 0.005289188983403335, "6": 0.0012288825860409314, "7": 0.00024696959349342307, "8": 4.369877632817183e-05, "9": 6.903110511463308e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4272 |
| Legacy raw p draw | 0.2862 |
| Legacy raw p away | 0.2866 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4476 |
| Legacy lambda away | 1.1465 |
| Legacy model home team | Bournemouth |
| Legacy model away team | Leeds |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 72.2% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T06:52:39Z |
| Market reference home draw last update utc | 2026-10-30T06:52:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.2% |
| Market draw away odds | 1.72 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T06:52:39Z |
| Market reference draw away last update utc | 2026-10-30T06:52:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.6% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T06:52:39Z |
| Market reference home away last update utc | 2026-10-30T06:52:39Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.72 |
| Market reference dc home away odds | 1.35 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.52, "price": 1.5, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.5, "price": 2.52, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.93, "price": 1.89, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.89, "price": 1.93, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.57, "price": 2.35, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.35, "price": 1.57, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 76.6% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market reference over 1 5 last update utc | 2026-10-30T06:52:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.4% |
| Market under 3 5 odds | 1.37 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.21 |
| Market reference under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.6% |
| Market btts yes odds | 1.71 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T06:52:39Z |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-30T06:52:39Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.998094794574687, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,502.9673 |
| Elo away rating | 1,455.9965 |
| Elo rating diff | 106.9708 |
| Elo home expectancy | 0.6493 |

</details>


---

## 2026-10-31 — Brentford vs Nottingham Forest

The model's most likely 1X2 outcome is **Brentford win** at **46.1%**. Expected goals are 1.58 for Brentford and 1.20 for Nottingham Forest (2.78 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 54.9%; Under 3.5 goals: 67.6%; Double Chance 1X: 71.9%; Double Chance X2: 53.9%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 83.6%; BTTS Yes (both teams score): 58.0%; BTTS No (at least one team does not score): 42.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 46.1% | 2.17 |
| Draw | 25.9% | 3.87 |
| Nottingham Forest win | 28.1% | 3.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.58 |
| Nottingham Forest expected goals | 1.20 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 79.0% |
| Under 1.5 | 21.0% |
| Over 2.5 | 54.9% |
| Under 2.5 | 45.1% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.4% |
| Under 4.5 | 83.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.19% |
| 2 | 2-1 | 9.43% |
| 3 | 1-0 | 8.44% |
| 4 | 2-0 | 7.60% |
| 5 | 1-2 | 7.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 46.1% | 46.4% | 2.10 | -3.3% |
| Draw | 25.9% | 25.5% | 3.75 | -3.0% |
| Nottingham Forest win | 28.1% | 28.1% | 3.42 | -4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | b9254b648ca25ce7831988b53ed17c3c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T06:52:26Z |
| Market best draw last update utc | 2026-10-30T06:52:26Z |
| Market best away last update utc | 2026-10-30T06:52:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Brentford |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6215 |
| Dc lambda away | 1.1275 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T06:51:51.118483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.4728 |
| Shot lambda away | 1.3686 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.0% |
| P btts no | 42.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.48 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.76 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.08 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.09 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.16010614674964546, "-10": 1.6108392146849362e-07, "-11": 1.7900520069270287e-08, "-12": 1.8275632295680638e-09, "-13": 1.7248430654336683e-10, "-14": 1.503128483961385e-11, "-15": 1.095651563599363e-12, "-2": 0.08101222133624039, "-3": 0.02903707232121903, "-4": 0.00822595412347151, "-5": 0.0019178694859447812, "-6": 0.00037900079222875547, "-7": 6.490244821015865e-05, "-8": 9.797613094233179e-06, "-9": 1.3216653918457994e-06, "0": 0.25856001726645195, "1": 0.21648664791026553, "10": 2.5160754043618047e-06, "11": 3.6747437991212144e-07, "12": 4.9308726547582415e-08, "13": 6.116330153976868e-09, "14": 7.005310605233201e-10, "15": 6.711100034384702e-11, "2": 0.14213542551576686, "3": 0.06695678275699893, "4": 0.02492975398936055, "5": 0.007639074004243128, "6": 0.0019840460311354923, "7": 0.0004465423602145034, "8": 8.859553348993035e-05, "9": 1.57073535280239e-05} |
| Raw goal margin distribution | {"-1": 0.16254476202764992, "-10": 1.2579377365574082e-07, "-11": 1.3529297183879438e-08, "-12": 1.336668784598603e-09, "-13": 1.220728084642114e-10, "-14": 1.0301449761048585e-11, "-15": 7.317013242453063e-13, "-2": 0.08065036629375802, "-3": 0.028176673136998495, "-4": 0.007759525342293495, "-5": 0.001755898335681998, "-6": 0.00033645434753366203, "-7": 5.583039993702706e-05, "-8": 8.163152035741225e-06, "-9": 1.0662182864143142e-06, "0": 0.26675936682331797, "1": 0.2164352410992915, "10": 1.934455426611801e-06, "11": 2.734417194860304e-07, "12": 3.550612715032966e-08, "13": 4.2617541465663424e-09, "14": 4.726696999429268e-10, "15": 4.412484709686606e-11, "2": 0.13931127292569528, "3": 0.06396753102979348, "4": 0.023152345166869773, "5": 0.00688571681898959, "6": 0.001734067079544944, "7": 0.0003781816445167184, "8": 7.267374663291256e-05, "9": 1.2475436505584877e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 28.1% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.3% |
| P home draw | 71.9% |
| P draw away | 53.9% |
| P home away | 74.1% |
| Raw p home draw | 71.9% |
| Raw p draw away | 54.8% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0342 |
| Totals anchor target over 2 5 | 0.5485 |
| Totals anchor reference over odds | 1.77 |
| Totals anchor reference under odds | 2.13 |
| Totals anchor reference last update utc | 2026-10-30T06:52:26Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5281 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.34, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.08, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.32, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.53, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:41Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.77, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.10 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.42 |
| Market reference 1x2 last update utc | 2026-10-30T06:52:26Z |
| Market reference home last update utc | 2026-10-30T06:52:26Z |
| Market reference draw last update utc | 2026-10-30T06:52:26Z |
| Market reference away last update utc | 2026-10-30T06:52:26Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-30T06:51:37Z |
| Market reference under 2 5 last update utc | 2026-10-30T06:51:37Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.4% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -0.6% |
| Under 2.5 probability edge | +0.6% |
| Raw edge prob home | -0.0125 |
| Raw ev home | -0.0509 |
| Raw edge prob draw | 0.0117 |
| Raw ev draw | 0.0003 |
| Raw edge prob away | 0.0008 |
| Raw ev away | -0.0380 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.07847267378904624, 0.0667413384933638, 0.042891642599057804, 0.015353216519316084, 0.004121803978676111, 0.0008852486652425336, 0.00015843895928577414, 2.4305910358627056e-05, 3.2626452540251386e-06, 3.892918369437581e-07, 4.1804520645225364e-08, 4.081112000930685e-09, 3.652121508587592e-10, 3.016822905984687e-11, 2.314033980381617e-12, 1.6566334409694182e-13], [0.096299174607732, 0.12630195966238753, 0.06858676074022657, 0.02455087574627786, 0.0065910551840181195, 0.0014155750332566729, 0.0002533550671874385, 3.8866864436130705e-05, 5.217199805329291e-06, 6.22505095647033e-07, 6.684837608473681e-08, 6.525985842473868e-09, 5.839999797751622e-10, 4.824112538253594e-11, 3.700303493638514e-12, 2.6490736788085534e-13], [0.08655731363962975, 0.09295049784375335, 0.04916289853036256, 0.019629290681560187, 0.005269780982249103, 0.0011318021441075149, 0.00020256630805613613, 3.107542833836673e-05, 4.171335172763203e-06, 4.977147699124583e-07, 5.3447633368292144e-08, 5.2177557497144364e-09, 4.669285723043874e-10, 3.8570480447442054e-11, 2.9585230945431808e-12, 2.1180277972807838e-13], [0.046137082511333215, 0.049544799950021784, 0.026602106900503558, 0.009380166236023418, 0.0028089171182799372, 0.0006032771433572372, 0.00010797260307444622, 1.6563933664709108e-05, 2.2234196852441216e-06, 2.6529367006656725e-07, 2.8488844755683075e-08, 2.781186446599014e-09, 2.4888390317884504e-10, 2.055897259374569e-11, 1.5769623430425983e-12, 1.1289585955877044e-13], [0.0184441119977439, 0.019806407112100077, 0.010634661151977233, 0.0038067149071938913, 0.0010067140201388872, 0.00024117067209498229, 4.3163951324920634e-05, 6.6217244568953835e-06, 8.888512116594612e-07, 1.0605582097217202e-07, 1.1388917867337724e-08, 1.1118283063320921e-09, 9.949572740189329e-11, 8.218811689803911e-12, 6.304184939339772e-13, 4.513210988735659e-14], [0.005898687110122436, 0.006334368298363892, 0.003401114603151465, 0.0012174411084535923, 0.0003268405417402009, 6.914832631103373e-05, 1.3804440318590876e-05, 2.1177208588545268e-06, 2.842671517974792e-07, 3.391814711375243e-08, 3.6423365370219835e-09, 3.555783710287919e-10, 3.1820136681537876e-11, 2.6284918775758935e-12, 2.0161672432947806e-13, 1.4433885181229865e-14], [0.0015720694327536007, 0.0016881835892893493, 0.0009064370096408337, 0.000324462362055652, 8.710684521182074e-05, 1.8708123641051893e-05, 3.2983347968168776e-06, 5.643974950962946e-07, 7.576053649461483e-08, 9.039584791956053e-09, 9.707254897157975e-10, 9.476581442731914e-11, 8.480440357184666e-12, 7.005239738665189e-13, 5.373322631511858e-14, 3.8468000193378034e-15], [0.00035912140959887945, 0.00038564637007499784, 0.0002070652414153453, 7.411974203907239e-05, 1.989856960922378e-05, 4.2736583976171635e-06, 7.648856365977822e-07, 1.1558839170685563e-07, 1.730663423068908e-08, 2.064990492811562e-09, 2.2175121463285844e-10, 2.164817415177029e-11, 1.937260296294255e-12, 1.6002674672714878e-13, 1.2274745360821144e-14, 8.78757780418032e-16], [7.178255688146667e-05, 7.708446713594669e-05, 4.138899010970586e-05, 1.481533669881193e-05, 3.977401977869678e-06, 8.542351383660556e-07, 1.528882579800067e-07, 2.3454384641886186e-08, 3.1013430777408072e-09, 4.127581746671679e-10, 4.432447844225423e-11, 4.327119606054798e-12, 3.872269758805915e-13, 3.198675640733355e-14, 2.453522913192007e-15, 1.7564945634498756e-16], [1.2753929970235701e-05, 1.3695944228738262e-05, 7.353768162224052e-06, 2.6323075542450583e-06, 7.066829114626318e-07, 1.5177580189607577e-07, 2.7164344936447662e-08, 4.167246086142428e-09, 5.593802274713656e-10, 6.57476685643859e-11, 7.875329586729847e-12, 7.688188165209473e-13, 6.880035969075815e-14, 5.683230981417569e-15, 4.3592845915048136e-16, 3.1208429496781276e-17], [2.039443328256623e-06, 2.190078050190113e-06, 1.175919379437885e-06, 4.209245379230651e-07, 1.1300358025635256e-07, 2.4270020871224074e-08, 4.343770286993033e-09, 6.663720317910476e-10, 8.944884247737997e-11, 1.067284411553859e-11, 1.12900514672792e-12, 1.2293954958597139e-13, 1.1001662615400066e-14, 9.087887055239332e-16, 6.97080342832719e-17, 4.9904479224141076e-18], [2.96473970902034e-07, 3.1837174739260294e-07, 1.7094345454581686e-07, 6.118981953513356e-08, 1.6427335685462057e-08, 3.528134055932759e-09, 6.314540874111736e-10, 9.687053306454471e-11, 1.3003182365713897e-11, 1.5515118424285923e-12, 1.6661076008508298e-13, 1.6022346365478448e-14, 1.5993122029531065e-15, 1.3211065613081707e-16, 1.0133460166016568e-17, 7.25461645165041e-19], [3.950689861667322e-08, 4.2424905998944704e-08, 2.2779219731762092e-08, 8.153902986464389e-09, 2.1890390022875194e-09, 4.701445932325228e-10, 8.414496738629539e-11, 1.2908567713651528e-11, 1.7327504531118605e-12, 2.067480692315095e-13, 2.220186273722918e-14, 2.167427997294128e-15, 1.9106414198009867e-16, 1.7604521172845263e-17, 1.3503431083573972e-18, 9.667202681779711e-20], [4.859562804558095e-09, 5.2184935390584214e-09, 2.8019675753188347e-09, 1.0029742918942949e-09, 2.6926367003543783e-10, 5.7830334904412e-11, 1.0350287368004697e-11, 1.5878238413507449e-12, 2.1313770370144646e-13, 2.5431133860951227e-14, 2.730949533563477e-15, 2.6660539920901854e-16, 2.385808849487086e-17, 1.941368811292368e-18, 1.660995262228849e-19, 1.1891183621453524e-20], [5.550559689181081e-10, 5.96052794069889e-10, 3.200388368140752e-10, 1.1455904363766432e-10, 3.075511383982546e-11, 6.605341645779187e-12, 1.1822028060302274e-12, 1.8136016266845097e-13, 2.4344444016655717e-14, 2.9047268681529066e-15, 3.119272042325983e-16, 3.045148794824918e-17, 2.7250546929105338e-18, 2.251022425815435e-19, 1.700855980597347e-20, 1.358202931423832e-21], [5.917157536335087e-11, 6.354202963277362e-11, 3.411764436774692e-11, 1.2212532544010105e-11, 3.2786397017381893e-12, 7.041604682780527e-13, 1.260283761439978e-13, 1.9333845835696448e-14, 2.5952321648178664e-15, 3.096575380026556e-16, 3.3252906205304995e-17, 3.2462717544829075e-18, 2.9050363956107373e-19, 2.399695716692355e-20, 1.8406706671400864e-21, 1.2980773972620427e-22]] |
| Legacy trial inputs | {"lambda_home": 1.5990705084755414, "lambda_away": 1.0738607049514128, "rho": -0.10287979955549995, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4739 |
| Legacy p draw | 0.2644 |
| Legacy p away | 0.2617 |
| Legacy p over 1 5 | 0.7585 |
| Legacy p under 3 5 | 0.7203 |
| Legacy p btts yes | 0.5360 |
| Legacy p over 2 5 | 0.5027 |
| Legacy goal margin distribution | {"-1": 0.15802186427073148, "-10": 4.8818638884976475e-08, "-11": 4.70530455560622e-09, "-12": 4.165246951953971e-10, "-13": 3.4080335333213457e-11, "-14": 2.5789413482624727e-12, "-15": 1.6566334409694182e-13, "-2": 0.07336093601375719, "-3": 0.023190961707857703, "-4": 0.005757433015779047, "-5": 0.0011720123753465946, "-6": 0.0002017542057039248, "-7": 3.0050458140041873e-05, "-8": 3.941481348318326e-06, "-9": 4.6161527695660226e-07, "0": 0.26439697765569414, "1": 0.22000483183480718, "10": 2.3816287289471906e-06, "11": 3.418186821596369e-07, "12": 4.505764352508973e-08, "13": 5.489733242995731e-09, "14": 6.185979985508817e-10, "15": 5.917157536335087e-11, "2": 0.14804575350021867, "3": 0.06968984723731766, "4": 0.02576317066796678, "5": 0.007809482875037007, "6": 0.0020018537179643065, "7": 0.0004439974774494947, "8": 8.671785838005177e-05, "9": 1.5123381372998153e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4833 |
| Legacy raw p draw | 0.2737 |
| Legacy raw p away | 0.2430 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5991 |
| Legacy lambda away | 1.0739 |
| Legacy model home team | Brentford |
| Legacy model away team | Nott'm Forest |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 73.0% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T06:51:55Z |
| Market reference home draw last update utc | 2026-10-30T06:52:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.4% |
| Market draw away odds | 1.79 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T06:51:55Z |
| Market reference draw away last update utc | 2026-10-30T06:52:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.7% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T06:51:55Z |
| Market reference home away last update utc | 2026-10-30T06:52:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.32 |
| Market reference dc draw away odds | 1.84 |
| Market reference dc home away odds | 1.29 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:51:55Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.17, "price": 1.68, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:51:55Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.17, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:51:55Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.73, "price": 2.09, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:51:55Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.09, "price": 1.73, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 79.8% |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market reference over 1 5 last update utc | 2026-10-30T06:52:22Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.8% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.90 |
| Market reference under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.6% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T06:51:55Z |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-30T06:52:22Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.85815621132972, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,503.9116 |
| Elo away rating | 1,478.7386 |
| Elo rating diff | 85.1730 |
| Elo home expectancy | 0.6202 |

</details>


---

## 2026-10-31 — Chelsea vs Manchester United

The model's most likely 1X2 outcome is **Chelsea win** at **50.8%**. Expected goals are 1.74 for Chelsea and 1.38 for Manchester United (3.11 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.0%; Under 3.5 goals: 62.5%; Double Chance 1X: 75.0%; Double Chance X2: 49.2%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 79.8%; BTTS Yes (both teams score): 61.6%; BTTS No (at least one team does not score): 38.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 50.8% | 1.97 |
| Draw | 24.1% | 4.14 |
| Manchester United win | 25.0% | 3.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.74 |
| Manchester United expected goals | 1.38 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 82.3% |
| Under 1.5 | 17.7% |
| Over 2.5 | 60.0% |
| Under 2.5 | 40.0% |
| Over 3.5 | 37.5% |
| Under 3.5 | 62.5% |
| Over 4.5 | 20.2% |
| Under 4.5 | 79.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.09% |
| 2 | 2-1 | 10.40% |
| 3 | 1-0 | 7.94% |
| 4 | 2-0 | 7.62% |
| 5 | 1-2 | 6.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 50.8% | 53.2% | 1.84 | -6.5% |
| Draw | 24.1% | 23.8% | 4.01 | -3.2% |
| Manchester United win | 25.0% | 23.0% | 4.14 | +3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T12:30:00+00:00 |
| Fixture id | 6601f69175a02f03fb7065aacb538e01 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T06:52:26Z |
| Market best draw last update utc | 2026-10-30T06:52:26Z |
| Market best away last update utc | 2026-10-30T06:52:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7691 |
| Dc lambda away | 1.3441 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T06:51:51.118483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6583 |
| Shot lambda away | 1.4547 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.6% |
| P btts no | 38.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.35 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.66 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.67 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.95 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.13678153438167934, "-10": 2.9453063583396895e-07, "-11": 3.592435417740285e-08, "-12": 4.027155179463892e-09, "-13": 4.1757897187927906e-10, "-14": 4.025606106814297e-11, "-15": 3.5971167121410012e-12, "-16": 2.6763458706217676e-13, "-2": 0.0735612579982499, "-3": 0.028454528050894334, "-4": 0.008754518907611244, "-5": 0.002225022330825209, "-6": 0.0004804502992916588, "-7": 9.004192883502399e-05, "-8": 1.4892058064577495e-05, "-9": 2.202673200334107e-06, "0": 0.2414461079309191, "1": 0.2331452491760665, "10": 3.986831443540273e-06, "11": 6.128742502913873e-07, "12": 8.658960848185121e-08, "13": 1.131595046332236e-08, "14": 1.3748923669822822e-09, "15": 1.5483778768379981e-10, "16": 1.4519433490002591e-11, "2": 0.1564107152376368, "3": 0.07625244027275922, "4": 0.029567843491117157, "5": 0.009471237899810222, "6": 0.002577542561962732, "7": 0.0006088175631572818, "8": 0.00012690598647890444, "9": 2.365715209329295e-05} |
| Raw goal margin distribution | {"-1": 0.1621132837062547, "-10": 3.7325808464252773e-07, "-11": 4.591547227636108e-08, "-12": 5.191336172752504e-09, "-13": 5.429314362129782e-10, "-14": 5.2791774221742406e-11, "-15": 4.756773772071716e-12, "-16": 3.562347529988592e-13, "-2": 0.08759074728450629, "-3": 0.03409850431708467, "-4": 0.010566466767581786, "-5": 0.0027061234739635853, "-6": 0.0005889873101562735, "-7": 0.00011128395635751751, "-8": 1.8558075828449515e-05, "-9": 2.767975940202286e-06, "0": 0.2500593964231838, "1": 0.20641376757234323, "10": 3.774498699758703e-06, "11": 5.851862571586244e-07, "12": 8.338716741372432e-08, "13": 1.0991325324471563e-08, "14": 1.346965082726906e-09, "15": 1.529634191299096e-10, "16": 1.4437645583612543e-11, "2": 0.13913238919721846, "3": 0.06826378216721428, "4": 0.026660593567673845, "5": 0.00860543120422111, "6": 0.0023605650463131324, "7": 0.0005621181355513804, "8": 0.00011814435903270691, "9": 2.2208916029563534e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 29.8% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 62.4% |
| P home draw | 75.0% |
| P draw away | 49.2% |
| P home away | 75.9% |
| Raw p home draw | 70.2% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9912 |
| Totals anchor target over 2 5 | 0.6003 |
| Totals anchor reference over odds | 1.62 |
| Totals anchor reference under odds | 2.38 |
| Totals anchor reference last update utc | 2026-10-30T06:52:26Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6057 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.75, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.94, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.16, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 5.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.09, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:39Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.13, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:39Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.39, "price": 3.13, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.84 |
| Reference draw odds | 4.01 |
| Reference away odds | 4.14 |
| Market reference 1x2 last update utc | 2026-10-30T06:52:26Z |
| Market reference home last update utc | 2026-10-30T06:52:26Z |
| Market reference draw last update utc | 2026-10-30T06:52:26Z |
| Market reference away last update utc | 2026-10-30T06:52:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-10-30T06:52:22Z |
| Market reference under 2 5 last update utc | 2026-10-30T06:52:22Z |
| Home probability edge | -2.4% |
| Draw probability edge | +0.4% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0801 |
| Raw ev home | -0.1681 |
| Raw edge prob draw | 0.0123 |
| Raw ev draw | 0.0027 |
| Raw edge prob away | 0.0678 |
| Raw ev away | 0.2329 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.04537173879667717, 0.03815576551204333, 0.03494541659891319, 0.017301842579865286, 0.006424742908940227, 0.0019085745928130683, 0.00047247765759657855, 0.00010025513480145156, 1.8614013606563726e-05, 3.0719978425845302e-06, 4.562935135797144e-07, 6.161337498613117e-08, 7.626357177677818e-09, 8.7135911364814e-10, 9.244693796067015e-11, 9.154289879811198e-12, 8.498221897496619e-13], [0.061174245592050466, 0.10666072086173163, 0.06423453961636005, 0.03180319483348056, 0.011809571699943166, 0.0035082257481698492, 0.0008684796968674943, 0.00018428289186135036, 3.4215147816193676e-05, 5.646759613305213e-06, 8.387309875606358e-07, 1.1325395893455669e-07, 1.4018305973587761e-08, 1.601679331745284e-09, 1.6993033927746993e-10, 1.6826858946722755e-11, 1.5620914679847942e-12], [0.06636460441586836, 0.09857343682496811, 0.0660112753171297, 0.029229349329341774, 0.010853818254892915, 0.0032243036102617096, 0.0007981932814641904, 0.0001693688024061709, 3.1446101975319685e-05, 5.189765059149363e-06, 7.708521473114728e-07, 1.0408826993520006e-07, 1.288379876465236e-08, 1.4720547714245482e-09, 1.5617780774546006e-10, 1.5465054402381635e-11, 1.435670769593399e-12], [0.040662459976775485, 0.06039723230400313, 0.04485495555442524, 0.02002522461636637, 0.0066502762168088704, 0.001975572937701266, 0.0004890634495141826, 0.0001037744775211617, 1.926743742770348e-05, 3.1798368401947403e-06, 4.723111794902736e-07, 6.377624258511893e-08, 7.894071790643268e-09, 9.019471863582697e-10, 9.569218279242582e-11, 9.47564083611317e-12, 8.796542331902966e-13], [0.018685815269105076, 0.027754629853737715, 0.020612412871051623, 0.010205421980781755, 0.0034171118599480243, 0.000907844507824006, 0.00022474167272990437, 4.768798340572249e-05, 8.854057936699831e-06, 1.4612456751438659e-06, 2.1704342173417717e-07, 2.9307402655516043e-08, 3.627600673576141e-09, 4.144761167033603e-10, 4.397388774260034e-11, 4.3543866829780484e-12, 4.042317290067606e-13], [0.00686942585314404, 0.010203374544590608, 0.0075776967626450505, 0.003751797210204584, 0.001393165636016977, 0.00037318224188440455, 8.262129506772021e-05, 1.7531430198456813e-05, 3.254998169449096e-06, 5.371945871275297e-07, 7.979120370416725e-08, 1.0774217051325173e-08, 1.3336069897441598e-09, 1.5237295834238293e-10, 1.6166025242779785e-11, 1.6007937584661843e-12, 1.4860683625034838e-13], [0.002104493474160652, 0.003125870429721573, 0.0023214768929860404, 0.0011493875782407586, 0.00042680539132403745, 0.00012678949765027487, 2.8302203603371116e-05, 5.3708681386333205e-06, 9.971899475230941e-07, 1.6457307017105186e-07, 2.444455636914525e-08, 3.3007517598179696e-09, 4.0855921106231733e-10, 4.6680450932203084e-11, 4.9525674130357415e-12, 4.904136226504733e-13, 4.552667483285827e-14], [0.0005526217030318552, 0.000820826418109285, 0.0006095996637208447, 0.00030181919247071996, 0.00011207538778932885, 3.3293820569338384e-05, 8.242060024416601e-06, 1.5769791566468603e-06, 2.618534168970254e-07, 4.321545845960891e-08, 6.418928134696615e-09, 8.667487360698534e-10, 1.0728409937058973e-10, 1.2257880867384325e-11, 1.3005011760672979e-12, 1.2877835672415952e-13, 1.1954909287397991e-14], [0.00012697445091184017, 0.00018859915048857778, 0.00014006612869588083, 6.934821059030243e-05, 2.5751270258130407e-05, 7.649834529400277e-06, 1.8937566878773128e-06, 4.018366349640176e-07, 6.727407909652965e-08, 9.929503453641909e-09, 1.4748604169436376e-09, 1.991506020071331e-10, 2.4650388383980434e-11, 2.8164613947294736e-12, 2.988127716218717e-13, 2.9589067973026505e-14, 2.746848403057954e-15], [2.5932968202555935e-05, 3.851905432570197e-05, 2.8606782196265248e-05, 1.4163518150522415e-05, 5.2593798829906835e-06, 1.5623845126409824e-06, 3.8677648627280256e-07, 8.207018500421976e-08, 1.5237678782110923e-08, 2.2675899572461547e-09, 3.0122208067167333e-10, 4.067405838168714e-11, 5.034538315005299e-12, 5.752275616766222e-13, 6.10288294167769e-14, 6.043202812670798e-15, 5.610099652504268e-16], [4.766840505855313e-06, 7.080338315800681e-06, 5.258324733606772e-06, 2.6034517721991016e-06, 9.667472256203063e-07, 2.8718801960525357e-07, 7.109490155839058e-08, 1.5085642304631993e-08, 2.8008974470812594e-09, 4.6225124234893964e-10, 6.19107845018387e-11, 7.476458055898157e-12, 9.254182159480883e-13, 1.0573483218994796e-13, 1.1217948281761055e-14, 1.1108247898016828e-15, 1.0312144007798708e-16], [7.965560296832532e-07, 1.1831497552143166e-06, 8.786847949794178e-07, 4.350460655411932e-07, 1.6154690529324478e-07, 4.799014114031289e-08, 1.1880211315337898e-08, 2.520864569443624e-09, 4.680399411846249e-10, 7.724382929727474e-11, 1.1473269213871638e-11, 1.3969559737924924e-12, 1.5464068054861476e-13, 1.7668667123432052e-14, 1.8745591201416384e-15, 1.8562277952268032e-16, 1.7231959991705698e-17], [1.2201507099057548e-07, 1.812328273158157e-07, 1.3459541280528074e-07, 6.663960172680774e-08, 2.474547474770994e-08, 7.351046580378578e-09, 1.8197901629097005e-09, 3.8614166227653745e-10, 7.169354636958242e-11, 1.1832075791377342e-11, 1.7574554776532172e-12, 2.373094513585737e-13, 2.6486343639756893e-14, 2.706455783445227e-15, 2.8714171457727074e-16, 2.843337540227265e-17, 2.639561742481316e-18], [1.7252360250169394e-08, 2.5625473973216803e-08, 1.903116173178579e-08, 9.422527943351364e-09, 3.4988943697122213e-09, 1.0394035981855298e-09, 2.573098160362307e-10, 5.45986246707887e-11, 1.0137132073428841e-11, 1.6730001663148422e-12, 2.4849598314333474e-13, 3.3554446285773977e-14, 4.153289644206611e-15, 4.2789487716940234e-16, 4.060049518900031e-17, 4.020346270225936e-18, 3.7322168248682946e-19], [2.2651599588756555e-09, 3.364513419012974e-09, 2.498708866533468e-09, 1.237136988746622e-09, 4.5938963200874376e-10, 1.3646917740997354e-10, 3.378366112574121e-11, 7.1685622500687545e-12, 1.3309614068799485e-12, 2.1965765454564297e-13, 3.262644315302857e-14, 4.405553041244481e-15, 5.453088889433177e-16, 6.230495885045668e-17, 5.960501450598501e-18, 5.278540014280921e-19, 4.90023856848844e-20], [2.775786188420413e-10, 4.122962637873479e-10, 3.061983121072805e-10, 1.516019984854148e-10, 5.629480561127147e-11, 1.672328951054419e-11, 4.139938090449703e-12, 8.784543452043741e-13, 1.6309948778945234e-13, 2.6917422819502015e-14, 3.998129576968737e-15, 5.398679786971845e-16, 6.682357581064914e-17, 7.635012422391735e-18, 8.100374560686748e-19, 7.2327268213489e-20, 6.004880355172261e-21], [3.188925852800206e-11, 4.736611991547506e-11, 3.5177194757869576e-11, 1.7416598379337972e-11, 6.467355509622419e-12, 1.9212333603541863e-12, 4.756114019408704e-13, 1.0092008468134306e-13, 1.873747248112906e-14, 3.0923731041658845e-15, 4.593199153460777e-16, 6.202203042685123e-17, 7.676939577266124e-18, 8.771384698787228e-19, 9.306009937544484e-20, 9.215006410372228e-21, 7.713720156226179e-22]] |
| Legacy trial inputs | {"lambda_home": 1.8381391858512786, "lambda_away": 1.485331490974703, "rho": -0.10287979955549995, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4915 |
| Legacy p draw | 0.2419 |
| Legacy p away | 0.2666 |
| Legacy p over 1 5 | 0.8553 |
| Legacy p under 3 5 | 0.5734 |
| Legacy p btts yes | 0.6587 |
| Legacy p over 2 5 | 0.6473 |
| Legacy goal margin distribution | {"-1": 0.13926603943736068, "-10": 5.833788386734576e-07, "-11": 7.720393090745512e-08, "-12": 9.394094189733681e-09, "-13": 1.0576341615611817e-09, "-14": 1.1070946767698631e-10, "-15": 1.0716381347795993e-11, "-16": 8.498221897496619e-13, "-2": 0.07982131764980012, "-3": 0.03287589551745059, "-4": 0.010844353005161383, "-5": 0.0029672349773077625, "-6": 0.0006916147270342799, "-7": 0.00014016304787703234, "-8": 2.5099186667490067e-05, "-9": 4.023142316381488e-06, "0": 0.24188920248150103, "1": 0.216336674694197, "10": 6.094484790351183e-06, "11": 9.981153717585728e-07, "12": 1.5029732318432082e-07, "13": 2.0940488579668987e-08, "14": 2.712633417420873e-09, "15": 3.2494473875751634e-10, "16": 3.188925852800206e-11, "2": 0.15158812471982677, "3": 0.0772643017359713, "4": 0.031539873243089066, "5": 0.010679803001793185, "6": 0.003080566152230226, "7": 0.000772600250085341, "8": 0.00017121269559588893, "9": 3.396227051946814e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4507 |
| Legacy raw p draw | 0.2460 |
| Legacy raw p away | 0.3032 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8381 |
| Legacy lambda away | 1.4853 |
| Legacy model home team | Chelsea |
| Legacy model away team | Man United |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 76.6% |
| Market home draw odds | 1.26 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T06:52:39Z |
| Market reference home draw last update utc | 2026-10-30T06:52:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.3% |
| Market draw away odds | 2.04 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T06:52:39Z |
| Market reference draw away last update utc | 2026-10-30T06:52:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.0% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T06:52:39Z |
| Market reference home away last update utc | 2026-10-30T06:52:39Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.26 |
| Market reference dc draw away odds | 2.04 |
| Market reference dc home away odds | 1.27 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.23, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.23, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.04, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.04, "price": 1.78, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-30T06:52:22Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.5% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.53 |
| Market reference under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.6% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T06:52:39Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.47 |
| Market reference btts yes last update utc | 2026-10-30T06:52:39Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.966170897129066, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,487.8075 |
| Elo away rating | 1,504.9896 |
| Elo rating diff | 42.8180 |
| Elo home expectancy | 0.5613 |

</details>


---

## 2026-10-31 — Coventry City vs Sunderland

The model's most likely 1X2 outcome is **Sunderland win** at **40.2%**. Expected goals are 1.03 for Coventry City and 1.17 for Sunderland (2.20 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 47.7%; Under 3.5 goals: 73.7%; Double Chance 1X: 59.8%; Double Chance X2: 69.4%; Double Chance 12 (either team wins): 70.8%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 53.8%; BTTS No (at least one team does not score): 46.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 30.6% | 3.27 |
| Draw | 29.2% | 3.42 |
| Sunderland win | 40.2% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.03 |
| Sunderland expected goals | 1.17 |
| Expected total goals | 2.20 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 47.7% |
| Under 2.5 | 52.3% |
| Over 3.5 | 26.3% |
| Under 3.5 | 73.7% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.94% |
| 2 | 0-1 | 9.47% |
| 3 | 1-2 | 8.76% |
| 4 | 0-0 | 8.70% |
| 5 | 1-0 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 30.6% | 30.3% | 3.18 | -2.8% |
| Draw | 29.2% | 28.4% | 3.39 | -1.0% |
| Sunderland win | 40.2% | 41.3% | 2.36 | -5.1% |
| Over 2.5 | 47.7% | 47.7% | 2.03 | -3.1% |
| Under 2.5 | 52.3% | 52.3% | 1.86 | -2.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | d20fbb0cd5ad9369b8ed6f2c4a198619 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T06:52:26Z |
| Market best draw last update utc | 2026-10-30T06:52:26Z |
| Market best away last update utc | 2026-10-30T06:52:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Coventry |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8797 |
| Dc lambda away | 1.1502 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T06:51:51.118483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.3944 |
| Shot lambda away | 1.2078 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 53.8% |
| P btts no | 46.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.49 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.81 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.27 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.21053154496667115, "-10": 5.940391685237813e-07, "-11": 7.341549128457558e-08, "-12": 8.330870105234735e-09, "-13": 8.689953995009341e-10, "-14": 7.629787736188889e-11, "-2": 0.12146203359351486, "-3": 0.049341280037280985, "-4": 0.015727962901063212, "-5": 0.004108840993220343, "-6": 0.0009074533376727132, "-7": 0.0001733734164884134, "-8": 2.916500144230536e-05, "-9": 4.380379818976768e-06, "0": 0.2919920154347939, "1": 0.17309751724514152, "10": 1.64907754408153e-07, "11": 1.8052344744696437e-08, "12": 1.8144967106676544e-09, "13": 1.676498667128944e-10, "14": 1.3038213972571409e-11, "2": 0.08898304036271024, "3": 0.03201820769603294, "4": 0.009040219897540622, "5": 0.002091923344464942, "6": 0.0004092329994062507, "7": 6.925462226288629e-05, "8": 1.0319250915834335e-05, "9": 1.3728334507871695e-06} |
| Raw goal margin distribution | {"-1": 0.21436292201688265, "-10": 1.5994609268382564e-07, "-11": 1.682076930468887e-08, "-12": 1.6180870968305984e-09, "-13": 1.3296356884418638e-10, "-2": 0.11069856508745594, "-3": 0.03933827322364364, "-4": 0.010851108327400692, "-5": 0.002438209828635191, "-6": 0.0004614298138326515, "-7": 7.535896204729749e-05, "-8": 1.0818281332549535e-05, "-9": 1.384942977021443e-06, "0": 0.3105824967242211, "1": 0.1887195256104545, "10": 4.7552435471749684e-08, "11": 4.4296039445491206e-09, "12": 3.7743385282940825e-10, "13": 2.7472079337370758e-11, "2": 0.08685239870800879, "3": 0.02733852197893133, "4": 0.006679650677589745, "5": 0.0013294458187957784, "6": 0.00022285640964861704, "7": 3.223846082367039e-05, "8": 4.099374308459114e-06, "9": 4.6484815234192433e-07} |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 31.1% |
| Unadjusted away-win probability | 37.8% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.9% |
| Raw p btts yes | 45.4% |
| P home draw | 59.8% |
| P draw away | 69.4% |
| P home away | 70.8% |
| Raw p home draw | 62.2% |
| Raw p draw away | 68.9% |
| Raw p home away | 68.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1791 |
| Totals anchor target over 2 5 | 0.4772 |
| Totals anchor reference over odds | 2.03 |
| Totals anchor reference under odds | 1.86 |
| Totals anchor reference last update utc | 2026-10-30T06:52:26Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3840 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:37Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.22, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:37Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.26, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.01, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:39Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:39Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.18 |
| Reference draw odds | 3.39 |
| Reference away odds | 2.36 |
| Market reference 1x2 last update utc | 2026-10-30T06:52:26Z |
| Market reference home last update utc | 2026-10-30T06:52:26Z |
| Market reference draw last update utc | 2026-10-30T06:52:26Z |
| Market reference away last update utc | 2026-10-30T06:52:26Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference under 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market best over 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market best under 2 5 last update utc | 2026-10-30T06:52:26Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.8% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0078 |
| Raw ev home | -0.0104 |
| Raw edge prob draw | 0.0266 |
| Raw ev draw | 0.0529 |
| Raw edge prob away | -0.0344 |
| Raw ev away | -0.1074 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.1276232584754107, 0.13170674675218907, 0.08550063130190667, 0.03347395653121074, 0.009828925372756864, 0.0023088462552826126, 0.00045196285693890144, 7.583395148179905e-05, 1.113352479174214e-05, 1.4529449246675638e-06, 1.7065072331043944e-07, 1.8221093194280028e-08, 1.7834139708944764e-09, 1.6112680419348947e-10], [0.10482412369469751, 0.13782141636756087, 0.0792651507764946, 0.031032732403615315, 0.00911211110116227, 0.002140464272111638, 0.00041900163139308165, 7.030345281261251e-05, 1.0321567313054462e-05, 1.3469830195411525e-06, 1.5820532676018025e-07, 1.6892246026316274e-08, 1.6533512694274716e-09, 1.4937597809581147e-10], [0.05526794551206234, 0.06491309283229267, 0.03401735051812721, 0.014384772226379586, 0.0042237867096876665, 0.000992181114204505, 0.00019422211849346414, 3.2588144101666025e-05, 4.784412564335974e-06, 6.243744081859569e-07, 7.333378063028779e-08, 7.830155215472319e-09, 7.663869591495913e-10, 6.924106433987702e-11], [0.017079102097121074, 0.02005968070010234, 0.01178020915566419, 0.004115569361437316, 0.0013052499741549892, 0.00030660742662554156, 6.0019227429849885e-05, 1.0070507146797668e-05, 1.4784966204906027e-06, 1.9294645685554065e-07, 2.2661872355635316e-08, 2.4197031230728396e-09, 2.36831693306951e-10, 2.1397126240489422e-11], [0.003958384816116724, 0.004649186769181471, 0.002730272398823624, 0.0010689163133061961, 0.0002800798676949816, 7.10617089330327e-05, 1.3910520423285106e-05, 2.334018635979599e-06, 3.4266781356242415e-07, 4.471876336339921e-08, 5.252290836322311e-09, 5.608091132317942e-10, 5.4889945234268e-11, 4.95916349332926e-12], [0.0007339407078129542, 0.0008620251912433191, 0.0005062312407717395, 0.0001981922506337821, 5.8194998225616355e-05, 1.2198707944217748e-05, 2.579207853653855e-06, 4.32760170957815e-07, 6.353547452151173e-08, 8.291493212540003e-09, 9.738492423360735e-10, 1.0398196654288119e-10, 1.0177374643573563e-11, 9.194992739551051e-13], [0.00011340251718995903, 0.00013319308430165649, 7.821871218286744e-05, 3.0623046071920647e-05, 8.99181530115097e-06, 2.1122064008948977e-06, 3.689633958822821e-07, 6.68665632029234e-08, 9.81698203260605e-09, 1.2811337367665496e-09, 1.504712223600904e-10, 1.6066443273684707e-11, 1.5725247157984844e-12, 1.4207350963209267e-13], [1.5018882628824458e-05, 1.7639919727238845e-05, 1.0359185023066702e-05, 4.0556765942051145e-06, 1.1908643826824306e-06, 2.797378824471195e-07, 5.4759441974781046e-08, 8.198967267758052e-09, 1.3001483967945254e-09, 1.6967169425431208e-10, 1.992821397303201e-11, 2.1278189564869922e-12, 2.0826313844463885e-13, 1.88160317663433e-14], [1.7404462077370894e-06, 2.0441821241173477e-06, 1.2004624268146696e-06, 4.699874899245321e-07, 1.3800197058541323e-07, 3.2417107763468855e-08, 6.345735929775126e-09, 1.064738447478063e-09, 1.3949258692527388e-10, 1.9662212171396273e-11, 2.309358511782416e-12, 2.4657989046810613e-13, 2.413433798475373e-14, 2.1804745360711324e-15], [1.7927967830829649e-07, 2.1056687186662452e-07, 1.2365709249948948e-07, 4.8412416096528964e-08, 1.4215290758472685e-08, 3.3392176245862993e-09, 6.536608204620466e-10, 1.0967645279570587e-10, 1.61020952015721e-11, 1.875158830397995e-12, 2.3788213002525597e-13, 2.539967236212042e-14, 2.48602704918758e-15, 2.246060646105967e-16], [1.6620498019587937e-08, 1.952104281909627e-08, 1.1463889719065036e-08, 4.488174418029346e-09, 1.3178582989912046e-09, 3.095691627746601e-10, 6.059899523742571e-11, 1.0167785237497844e-11, 1.4927784561768742e-12, 1.9481026199034353e-13, 2.0417850013016068e-14, 2.3547298175471403e-15, 2.304723437567219e-16, 2.0822575582874125e-17], [1.4007618864039543e-09, 1.6452174135590425e-09, 9.66167185211852e-10, 3.782596440190559e-10, 1.1106801220591784e-10, 2.6090234113903914e-11, 5.107233416406687e-12, 8.56932566824545e-13, 1.258101390098624e-13, 1.6418448457732053e-14, 1.92837323519899e-15, 1.8373698631468364e-16, 1.9424019341907196e-17, 1.7549095231009698e-18], [1.0821713675980457e-10, 1.271027714066366e-10, 7.464212685235382e-11, 2.922279369880034e-11, 8.58066055565225e-12, 2.0156248257496044e-12, 3.9456397439995767e-13, 6.620310680786121e-14, 9.719577003877757e-15, 1.2684222060720795e-15, 1.4897823259112826e-16, 1.5907030496576943e-17, 1.3893320245439697e-18, 1.3557713534742342e-19], [7.717304837180475e-12, 9.064098921528813e-12, 5.322965140850664e-12, 2.083969451790606e-12, 6.119139278219654e-13, 1.4374055425458446e-13, 2.813759963888593e-14, 4.721152043956607e-15, 6.931336466040628e-16, 9.04551822345301e-17, 1.0624106952320997e-17, 1.1343804416936621e-18, 1.1102900942633934e-19, 8.951406746707742e-21]] |
| Legacy trial inputs | {"lambda_home": 0.9270709416940522, "lambda_away": 1.174516118355173, "rho": -0.10287979955549995, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T06:52:26Z", "over": 2.03, "under": 1.86, "bookmaker": "pinnacle", "event_id": "d20fbb0cd5ad9369b8ed6f2c4a198619", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Coventry City", "away_team": "Sunderland"}} |
| Legacy p home | 0.2891 |
| Legacy p draw | 0.3039 |
| Legacy p away | 0.4070 |
| Legacy p over 1 5 | 0.6358 |
| Legacy p under 3 5 | 0.8375 |
| Legacy p btts yes | 0.4270 |
| Legacy p over 2 5 | 0.3573 |
| Legacy goal margin distribution | {"-1": 0.22673562883261905, "-10": 1.883307534221458e-07, "-11": 1.9943685528047376e-08, "-12": 1.932789948990288e-09, "-13": 1.6112680419348947e-10, "-2": 0.12107811111141815, "-3": 0.04364066682942891, "-4": 0.012174033382438939, "-5": 0.0027619602362873434, "-6": 0.000527249026636849, "-7": 8.680312620395651e-05, "-8": 1.2556317104481162e-05, "-9": 1.6192221975000165e-06, "0": 0.3038702506019268, "1": 0.18264670504106637, "10": 1.834244152945112e-08, "11": 1.5331876229514415e-09, "12": 1.1728123568133337e-10, "13": 7.717304837180475e-12, "2": 0.07826536887172743, "3": 0.022266367098592345, "4": 0.004902825798791064, "5": 0.0008779774946616528, "6": 0.0001322926561079273, "7": 1.719132313163396e-05, "8": 1.962863953367908e-06, "9": 1.9979672302023122e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2748 |
| Legacy raw p draw | 0.3237 |
| Legacy raw p away | 0.4014 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9271 |
| Legacy lambda away | 1.1745 |
| Legacy model home team | Coventry |
| Legacy model away team | Sunderland |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 58.9% |
| Market home draw odds | 1.64 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T06:52:39Z |
| Market reference home draw last update utc | 2026-10-30T06:52:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.5% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T06:52:39Z |
| Market reference draw away last update utc | 2026-10-30T06:52:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.6% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T06:52:39Z |
| Market reference home away last update utc | 2026-10-30T06:52:39Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.64 |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home away odds | 1.35 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.1, "price": 1.72, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.72, "price": 2.1, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.16, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.16, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 74.7% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.57 |
| Market reference over 1 5 last update utc | 2026-10-30T06:52:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.7% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.48 |
| Market reference under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.4% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T06:52:39Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-30T06:52:39Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.38433409336513, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,364.9791 |
| Elo away rating | 1,407.0794 |
| Elo rating diff | 17.8997 |
| Elo home expectancy | 0.5257 |

</details>


---

## 2026-10-31 — Hull City vs Ipswich Town

The model's most likely 1X2 outcome is **Hull City win** at **42.0%**. Expected goals are 1.75 for Hull City and 0.91 for Ipswich Town (2.66 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 51.3%; Under 3.5 goals: 70.6%; Double Chance 1X: 69.3%; Double Chance X2: 58.0%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 42.0% | 2.38 |
| Draw | 27.3% | 3.66 |
| Ipswich Town win | 30.7% | 3.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.75 |
| Ipswich Town expected goals | 0.91 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 51.3% |
| Under 2.5 | 48.7% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.01% |
| 2 | 1-2 | 8.56% |
| 3 | 0-1 | 8.26% |
| 4 | 0-0 | 7.71% |
| 5 | 1-0 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 42.0% | 35.8% | 2.71 | +13.8% |
| Draw | 27.3% | 28.3% | 3.41 | -6.9% |
| Ipswich Town win | 30.7% | 35.9% | 2.70 | -17.1% |
| Over 2.5 | 51.3% | 51.3% | 1.89 | -2.9% |
| Under 2.5 | 48.7% | 48.7% | 1.99 | -3.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | 1ec76c009147b63859f68c6b5a1dd77b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T06:52:26Z |
| Market best draw last update utc | 2026-10-30T06:52:26Z |
| Market best away last update utc | 2026-10-30T06:52:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Hull |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8165 |
| Dc lambda away | 0.7786 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T06:51:51.118483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6094 |
| Shot lambda away | 1.2179 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.97 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.26 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.97 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.19770751944027087, "-10": 2.180620656365379e-08, "-11": 1.880590581828293e-09, "-12": 1.489678483773154e-10, "-13": 1.0909751438369367e-11, "-14": 7.427111211807731e-13, "-15": 4.700492392309529e-14, "-16": 2.5412860824587542e-15, "-2": 0.08049822173660177, "-3": 0.022689007280635377, "-4": 0.005029130105602694, "-5": 0.0009147520231787098, "-6": 0.0001407705700135158, "-7": 1.8749832978078694e-05, "-8": 2.199676575630604e-06, "-9": 2.3046316756595627e-07, "0": 0.27302772252530344, "1": 0.17249524027078672, "10": 6.751174529637964e-06, "11": 1.1219942363279988e-06, "12": 1.7127188190675088e-07, "13": 2.417160764284665e-08, "14": 3.1710841184258512e-09, "15": 3.8674823927579195e-10, "16": 4.029356601938044e-11, "2": 0.13104131919421383, "3": 0.07117617081802277, "4": 0.030402489837451946, "5": 0.010656554614079218, "6": 0.003160257429321553, "7": 0.0008111574302260017, "8": 0.00018338496755275212, "9": 3.7025726169142984e-05} |
| Raw goal margin distribution | {"-1": 0.12098029583010309, "-10": 8.666178660632548e-09, "-11": 7.0873239249088e-10, "-12": 5.322720196176309e-11, "-13": 3.695222773210054e-12, "-14": 2.3845003672469405e-13, "-15": 1.4316069017815824e-14, "-16": 7.406291768660662e-16, "-2": 0.04762302355139477, "-3": 0.012860708615311328, "-4": 0.0027203746496789003, "-5": 0.00047112349496452823, "-6": 6.893275554073169e-05, "-7": 8.721481327707958e-06, "-8": 9.712977497084485e-07, "-9": 9.655972778847656e-08, "0": 0.25077329775863333, "1": 0.24094929373361887, "10": 6.120673213896679e-06, "11": 9.646082962251607e-07, "12": 1.396045273360737e-07, "13": 1.867685069237425e-08, "14": 2.322509880807596e-09, "15": 2.687083211866028e-10, "16": 2.6788926122773028e-11, "2": 0.17685252953381086, "3": 0.09203570957328769, "4": 0.037516070303840174, "5": 0.012520467362111725, "6": 0.0035302752854570693, "7": 0.0008607367453688992, "8": 0.00018472668060683735, "9": 3.538917448361953e-05} |
| Unadjusted home-win probability | 56.4% |
| Unadjusted draw probability | 25.1% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 50.3% |
| P home draw | 69.3% |
| P draw away | 58.0% |
| P home away | 72.7% |
| Raw p home draw | 81.5% |
| Raw p draw away | 43.6% |
| Raw p home away | 74.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0560 |
| Totals anchor target over 2 5 | 0.5135 |
| Totals anchor reference over odds | 1.89 |
| Totals anchor reference under odds | 1.99 |
| Totals anchor reference last update utc | 2026-10-30T06:52:26Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4812 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.39, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.39, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.48, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.61, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.6, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:41Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:41Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.61, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.71 |
| Reference draw odds | 3.41 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-10-30T06:52:26Z |
| Market reference home last update utc | 2026-10-30T06:52:26Z |
| Market reference draw last update utc | 2026-10-30T06:52:26Z |
| Market reference away last update utc | 2026-10-30T06:52:26Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.99 |
| Market reference over 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference under 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market best over 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market best under 2 5 last update utc | 2026-10-30T06:52:26Z |
| Home probability edge | +6.2% |
| Draw probability edge | -1.0% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.2065 |
| Raw ev home | 0.5298 |
| Raw edge prob draw | -0.0318 |
| Raw ev draw | -0.1449 |
| Raw edge prob away | -0.1747 |
| Raw ev away | -0.5012 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08616089343926112, 0.07794529638197023, 0.041612363503198316, 0.012086975055746544, 0.002633141097362995, 0.00045890271182949874, 6.664780805434514e-05, 8.296679767277788e-06, 9.037136407629426e-07, 8.749934966323215e-08, 7.624674743785546e-09, 6.040113978225804e-10, 4.386118742274174e-11, 2.940041965689922e-12, 1.8299616599391567e-13, 1.0630831356145922e-14, 5.789802414147963e-16], [0.09220612813715012, 0.12755989185021227, 0.0743749568430529, 0.021603393137357162, 0.004706287722950164, 0.0008202098250164431, 0.0001191215165498832, 1.4828890927680381e-05, 1.615233007013794e-06, 1.5639006793012134e-07, 1.3627797300381158e-08, 1.0795666927766234e-09, 7.839434358014155e-11, 5.254820344394659e-12, 3.270742347330388e-13, 1.9000786226871157e-14, 1.0348277973899783e-15], [0.09051600412763311, 0.07887545373041334, 0.045034651770352915, 0.019306178464616044, 0.0042058407263805735, 0.0007329921350556938, 0.00010645463158798492, 1.325204854912649e-05, 1.4434758696041393e-06, 1.3976020074047092e-07, 1.2178674205850129e-08, 9.647700758247896e-10, 7.005821623259097e-11, 4.696044677951425e-12, 2.9229452553055063e-13, 1.6980321912008185e-14, 9.247885278729189e-16], [0.05392727332171268, 0.04699211142480785, 0.02047441303946335, 0.007793367203829017, 0.002505739450001576, 0.0004366992068505019, 6.342312687502865e-05, 7.895254005840277e-06, 8.599884462826742e-07, 8.326578948625852e-08, 7.2557632092209516e-09, 5.747869680399398e-10, 4.173901191969656e-11, 2.7977912560277175e-12, 1.7414209697657482e-13, 1.0116470227169283e-14, 5.509669167130443e-16], [0.024096436060749266, 0.020997583199734552, 0.009148624699483153, 0.002657364043466085, 0.0007586229851278029, 0.00019513121779543438, 2.8339488117631012e-05, 3.5278528213386527e-06, 3.842704318686556e-07, 3.72058264550824e-08, 3.242107814350307e-09, 2.5683326025589724e-10, 1.8650329786966456e-11, 1.2501429046858802e-12, 7.781227654970864e-14, 4.52036350021259e-15, 2.4618969701957096e-16], [0.008613648642917702, 0.007505915131057812, 0.003270319250888261, 0.0009499164162299027, 0.00020693878684274666, 4.7261426780985674e-05, 1.013039408607981e-05, 1.2610862697839213e-06, 1.373634870996737e-07, 1.3299805653645152e-08, 1.15894223962691e-09, 9.180907326220376e-11, 6.666852618970903e-12, 4.468831700776372e-13, 2.7815217512456225e-14, 1.6158747638421582e-15, 8.800436480676008e-17], [0.0025659030639975772, 0.002235922479694187, 0.0009741890497244684, 0.0002829687562134281, 6.164459327654727e-05, 1.0743393528195059e-05, 2.0446791470672323e-06, 3.756625395051833e-07, 4.091894237179556e-08, 3.961853274026846e-09, 3.4523505275548484e-10, 2.7348826513832705e-11, 1.9859757776750027e-12, 1.331211595557666e-13, 8.285821119445492e-15, 4.813497948965005e-16, 2.6215449301904358e-17], [0.0006551587542815902, 0.0005709039468484111, 0.0002487422433090214, 7.22511541541133e-05, 1.57398755650327e-05, 2.743138826812601e-06, 3.9839422449034137e-07, 6.49905074345411e-08, 1.0447940799859877e-08, 1.0115903800410752e-09, 8.814977084334473e-11, 6.983047552057827e-12, 5.070844003389038e-13, 3.3990174565362773e-14, 2.1156404226582764e-15, 1.2290430469605145e-16, 6.69365937807854e-18], [0.00014637297660134225, 0.0001275491008973679, 5.5573007796501114e-05, 1.6142066983469707e-05, 3.516540720447043e-06, 6.128612228521008e-07, 8.900766130092943e-08, 1.1080155285016767e-08, 1.581578650969334e-09, 2.2600552012810973e-10, 1.9694073017790927e-11, 1.5601248541114736e-12, 1.13290790332339e-13, 7.593950311763676e-15, 4.726680122319103e-16, 2.745879345717672e-17, 1.49547089330922e-18], [2.9068507800244684e-05, 2.533023595227847e-05, 1.1036356902240093e-05, 3.205685987373426e-06, 6.983569900378425e-07, 1.2170935954567737e-07, 1.767621289723692e-08, 2.2004306246203553e-09, 2.396813215407976e-10, 3.041071388413965e-11, 3.911086106388535e-12, 3.0982837504637515e-13, 2.2498648992024947e-14, 1.5080980724562836e-15, 9.38681040688998e-17, 5.45309776659915e-18, 2.969886131754685e-19], [5.195496797409684e-06, 4.5273448734298865e-06, 1.9725593530527225e-06, 5.729613434357144e-07, 1.24819324408518e-07, 2.175345883179555e-08, 3.159319636529576e-09, 3.932892029304998e-10, 4.283892200526553e-11, 4.147749515621081e-12, 4.736389997960053e-13, 5.5376503718795603e-14, 4.021247309541164e-15, 2.695466433801733e-16, 1.677731232095728e-17, 9.746476213027113e-19, 5.3081616683719205e-20], [8.441871544343133e-07, 7.356228932234253e-07, 3.20510113303619e-07, 9.30972773108066e-08, 2.0281192424827383e-08, 3.534597599881726e-09, 5.133401401074994e-10, 6.390335824230854e-11, 6.960656329282869e-12, 6.739445711224749e-13, 5.872738677403217e-14, 6.096532946256945e-15, 6.533899366872248e-16, 4.3797123304142446e-17, 2.7260514440786495e-18, 1.5836502919488343e-19, 8.624934378430026e-21], [1.2573663588724463e-07, 1.0956663743306502e-07, 4.773806756351494e-08, 1.3866283557899793e-08, 3.020762509693091e-09, 5.264572068998933e-10, 7.64589486394822e-11, 9.518023633834517e-12, 1.036748197143274e-12, 1.0038001964646752e-13, 8.747093590122185e-15, 6.929271613272157e-16, 6.593883550313764e-17, 6.523319997082722e-18, 4.0602908494112292e-19, 2.3587525477680446e-20, 1.284632474914564e-21], [1.728712719087357e-08, 1.506396591428028e-08, 6.563353950053602e-09, 1.906430896919279e-09, 4.153149585242276e-10, 7.238091453625205e-11, 1.0512095863583416e-11, 1.3086025723750863e-12, 1.4253918774315468e-13, 1.3800927269972453e-14, 1.2026098708296747e-15, 9.526833517811436e-17, 6.918052076108756e-18, 6.076806514221017e-19, 5.582363791620458e-20, 3.2429733002901024e-21, 1.7662000283902629e-22], [2.206983746656999e-09, 1.923160948949529e-09, 8.379191829497572e-10, 2.4338699872855846e-10, 5.302172842752006e-11, 9.240604305497985e-12, 1.342040493950719e-12, 1.6706446225432165e-13, 1.819745219303475e-14, 1.7619134652809481e-15, 1.5353276511389191e-16, 1.2162556854453548e-17, 8.832021840250716e-19, 5.920157747203069e-20, 4.828810665810549e-21, 4.140184361205704e-22, 2.2548424113292268e-23], [2.629736406718277e-10, 2.2915467189516415e-10, 9.984244716927995e-11, 2.900083212882213e-11, 6.3178158789879434e-12, 1.101066267436467e-12, 1.5991113444211888e-13, 1.9906603269030823e-14, 2.1683214755897436e-15, 2.0994119200718197e-16, 1.8294230877581392e-17, 1.4492321752430334e-18, 1.0523815326424306e-19, 7.054177170501273e-21, 4.390710716064955e-22, 3.342554517204187e-23, 2.6867625053726592e-24], [2.9376265142816864e-11, 2.5598415046883867e-11, 1.115320224893804e-11, 3.2396255830133036e-12, 7.057507129250882e-13, 1.2299793442944294e-13, 1.786335646667559e-14, 2.2237272687481247e-15, 2.4221890231682085e-16, 2.3452115219784847e-17, 2.0436123387529742e-18, 1.6189085919287508e-19, 1.175594590215518e-20, 7.880081760120341e-22, 4.904776076834733e-23, 2.8493409700300876e-24, 2.033571160155915e-25]] |
| Legacy trial inputs | {"lambda_home": 1.7873283462338412, "lambda_away": 0.8713978758849552, "rho": -0.10287979955549995, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T06:52:26Z", "over": 1.89, "under": 1.99, "bookmaker": "pinnacle", "event_id": "1ec76c009147b63859f68c6b5a1dd77b", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Hull City", "away_team": "Ipswich Town"}} |
| Legacy p home | 0.4686 |
| Legacy p draw | 0.2674 |
| Legacy p away | 0.2641 |
| Legacy p over 1 5 | 0.7437 |
| Legacy p under 3 5 | 0.7353 |
| Legacy p btts yes | 0.5063 |
| Legacy p over 2 5 | 0.4840 |
| Legacy goal margin distribution | {"-1": 0.17433781909197518, "-10": 8.777176898417552e-09, "-11": 6.872805365455151e-10, "-12": 4.941866495259113e-11, "-13": 3.2846474892516817e-12, "-14": 2.0292174074865974e-13, "-15": 1.16656591535359e-14, "-16": 5.789802414147963e-16, "-2": 0.0678879390987147, "-3": 0.01759334730852181, "-4": 0.0035680987305437024, "-5": 0.0005921746580070856, "-6": 8.300677657844766e-05, "-7": 1.0059192373618705e-05, "-8": 1.0728762754901322e-06, "-9": 1.0213493449752344e-07, "0": 0.26735679995768774, "1": 0.1944314508491321, "10": 5.980818329751595e-06, "11": 9.605669736299739e-07, "12": 1.4166822756731643e-07, "13": 1.931337021257539e-08, "14": 2.4472916208011008e-09, "15": 2.885720557187116e-10, "16": 2.9376265142816864e-11, "2": 0.147671135651871, "3": 0.07849451534190116, "4": 0.03265243287003935, "5": 0.011115176066355733, "6": 0.003195714136337832, "7": 0.0007943379917556177, "8": 0.0001737719636895978, "9": 3.3930653788233785e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5791 |
| Legacy raw p draw | 0.2521 |
| Legacy raw p away | 0.1687 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7873 |
| Legacy lambda away | 0.8714 |
| Legacy model home team | Hull |
| Legacy model away team | Ipswich |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 64.4% |
| Market home draw odds | 1.50 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T06:52:41Z |
| Market reference home draw last update utc | 2026-10-30T06:52:41Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.0% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T06:52:41Z |
| Market reference draw away last update utc | 2026-10-30T06:52:41Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.6% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T06:52:41Z |
| Market reference home away last update utc | 2026-10-30T06:52:41Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.50 |
| Market reference dc draw away odds | 1.51 |
| Market reference dc home away odds | 1.35 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.38, "price": 1.56, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.56, "price": 2.38, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.88, "price": 1.94, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.94, "price": 1.88, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.54, "price": 2.41, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.41, "price": 1.54, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 76.7% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 3.89 |
| Market reference over 1 5 last update utc | 2026-10-30T06:52:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.7% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.14 |
| Market reference under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T06:52:41Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.26 |
| Market reference btts yes last update utc | 2026-10-30T06:52:41Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.82919620852559, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,403.0690 |
| Elo away rating | 1,376.0928 |
| Elo rating diff | 86.9763 |
| Elo home expectancy | 0.6226 |

</details>


---

## 2026-10-31 — Manchester City vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Manchester City win** at **59.5%**. Expected goals are 2.03 for Manchester City and 1.07 for Brighton and Hove Albion (3.09 combined). The most likely exact score is 2-1 at 9.1%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 69.6%; Under 3.5 goals: 51.5%; Double Chance 1X: 80.5%; Double Chance X2: 40.5%; Double Chance 12 (either team wins): 79.0%; Under 4.5 goals: 70.7%; BTTS Yes (both teams score): 65.5%; BTTS No (at least one team does not score): 34.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 59.5% | 1.68 |
| Draw | 21.0% | 4.76 |
| Brighton and Hove Albion win | 19.5% | 5.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 2.03 |
| Brighton and Hove Albion expected goals | 1.07 |
| Expected total goals | 3.09 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 88.0% |
| Under 1.5 | 12.0% |
| Over 2.5 | 69.6% |
| Under 2.5 | 30.4% |
| Over 3.5 | 48.5% |
| Under 3.5 | 51.5% |
| Over 4.5 | 29.3% |
| Under 4.5 | 70.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.08% |
| 2 | 1-1 | 8.97% |
| 3 | 2-0 | 7.29% |
| 4 | 3-1 | 7.17% |
| 5 | 2-2 | 6.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 59.5% | 59.8% | 1.64 | -2.4% |
| Draw | 21.0% | 20.3% | 4.64 | -2.5% |
| Brighton and Hove Albion win | 19.5% | 19.8% | 4.75 | -7.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | 7df53f9af95d5a4e13b504882078dab8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T06:52:26Z |
| Market best draw last update utc | 2026-10-30T06:52:26Z |
| Market best away last update utc | 2026-10-30T06:52:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man City |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1446 |
| Dc lambda away | 1.0541 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T06:51:51.118483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7466 |
| Shot lambda away | 1.0955 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 65.5% |
| P btts no | 34.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.94 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.36 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.28 |
| Fair Over 3.5 odds | 2.06 |
| Fair Under 3.5 odds | 1.94 |
| Fair Over 4.5 odds | 3.41 |
| Fair Under 4.5 odds | 1.41 |
| Goal margin distribution | {"-1": 0.11556317556225544, "-10": 9.352828544186894e-08, "-11": 1.037232830039039e-08, "-12": 1.057883704808532e-09, "-13": 9.985249480690143e-11, "-14": 8.76995182771585e-12, "-15": 7.201075101186106e-13, "-16": 5.547830436165778e-14, "-17": 3.986675647174994e-15, "-18": 2.3722229319256393e-16, "-2": 0.0541461743688765, "-3": 0.018493960270047877, "-4": 0.005077953647467115, "-5": 0.0011592261857299745, "-6": 0.00022576532133462807, "-7": 3.826843803194191e-05, "-8": 5.7357389409878e-06, "-9": 7.699140962781293e-07, "0": 0.2100753621308697, "1": 0.20403125539539, "10": 5.164889074230872e-05, "11": 1.0876665344936634e-05, "12": 2.106487690092106e-06, "13": 3.775560243700876e-07, "14": 6.296818541602383e-08, "15": 9.817994778709244e-09, "16": 1.4363164072910292e-09, "17": 1.9599244560480517e-10, "18": 2.2145496158167137e-11, "2": 0.17687803868661175, "3": 0.11471957856326, "4": 0.05981331062491527, "5": 0.025928582675735553, "6": 0.009588911580414732, "7": 0.0030864148765725003, "8": 0.0008784244791899483, "9": 0.00022390243192380648} |
| Raw goal margin distribution | {"-1": 0.11594572937904557, "-10": 2.896108578804635e-08, "-11": 2.763369435214476e-09, "-12": 2.422847064362851e-10, "-13": 1.9646331264169237e-11, "-14": 1.481546168205993e-12, "-15": 1.0437710062474883e-13, "-16": 6.857063427239222e-15, "-17": 3.816937891828799e-16, "-2": 0.05024743638981702, "-3": 0.015353490716311842, "-4": 0.0037179677844736904, "-5": 0.0007421515664606826, "-6": 0.00012569017416064142, "-7": 1.845857345958486e-05, "-8": 2.390746992204999e-06, "-9": 2.767934025917867e-07, "0": 0.2259705038678452, "1": 0.2268526650328888, "10": 1.7653454465656827e-05, "11": 3.198565859968987e-06, "12": 5.325297015188462e-07, "13": 8.199753232234576e-08, "14": 1.1741835611735136e-08, "15": 1.5708239756986014e-09, "16": 1.9595752487294084e-10, "17": 2.0712873749920738e-11, "2": 0.18118276430396774, "3": 0.10512635079766398, "4": 0.04834054773879281, "5": 0.018323145880409692, "6": 0.00589264455217025, "7": 0.001643268526877441, "8": 0.0004041527212679011, "9": 8.88523891236115e-05} |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 57.7% |
| P home draw | 80.5% |
| P draw away | 40.5% |
| P home away | 79.0% |
| Raw p home draw | 81.4% |
| Raw p draw away | 41.2% |
| Raw p home away | 77.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1689 |
| Totals anchor target over 2 5 | 0.6955 |
| Totals anchor reference over odds | 1.40 |
| Totals anchor reference under odds | 3.01 |
| Totals anchor reference last update utc | 2026-10-30T06:52:26Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6029 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 8.7, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 8.5, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.85, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.66, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.99, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.54, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:52:11Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.23, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:39Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.75, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:39Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.3, "price": 3.75, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.64 |
| Reference draw odds | 4.64 |
| Reference away odds | 4.75 |
| Market reference 1x2 last update utc | 2026-10-30T06:52:26Z |
| Market reference home last update utc | 2026-10-30T06:52:26Z |
| Market reference draw last update utc | 2026-10-30T06:52:26Z |
| Market reference away last update utc | 2026-10-30T06:52:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.98 |
| Market reference over 2 5 last update utc | 2026-10-30T06:52:22Z |
| Market reference under 2 5 last update utc | 2026-10-30T06:52:22Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.0105 |
| Raw ev home | -0.0359 |
| Raw edge prob draw | 0.0227 |
| Raw ev draw | 0.0485 |
| Raw edge prob away | -0.0122 |
| Raw ev away | -0.1158 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.049535424475842874, 0.038794866217574275, 0.028255647349451993, 0.01091736445488196, 0.0031636732252136412, 0.0007334245049560836, 0.00014168959786550853, 2.3462469950556463e-05, 3.3995195583473646e-06, 4.3783334744818e-07, 5.075077026701473e-08, 5.347905871880013e-09, 5.165784803267819e-10, 4.606029973021084e-11, 3.813577053692675e-12, 2.9469656141320264e-13, 2.134955796242026e-14, 1.455706321041344e-15], [0.07827957600162132, 0.10165737565475698, 0.05609862212094984, 0.021675281246847485, 0.0062811411319114155, 0.0014561373749086663, 0.00028130982492887964, 4.6582271483719344e-05, 6.749389272095576e-06, 8.692721567011756e-07, 1.0076032760267349e-07, 1.0617705796459983e-08, 1.025612353002017e-09, 9.144789066009136e-11, 7.57145696994197e-12, 5.850890915575917e-13, 4.238730650092002e-14, 2.890152110592514e-15], [0.08822943492058731, 0.10226977475655208, 0.05303120003886839, 0.021516997947240272, 0.00623527322679244, 0.0014455039614014965, 0.00027925556566485524, 4.624210539546088e-05, 6.700101994474846e-06, 8.629243144908536e-07, 1.0002452736364434e-07, 1.054017021624846e-08, 1.0181228396941012e-09, 9.078009430206698e-11, 7.516166559709773e-12, 5.808164903894112e-13, 4.207777405896364e-14, 2.8690468337003e-15], [0.05839009418001007, 0.06768196787362743, 0.039226249242932346, 0.01356031193203335, 0.004126493514077267, 0.0009566321321198504, 0.0001848108717248299, 3.060294890875336e-05, 4.43411642412971e-06, 5.710818848459443e-07, 6.619606686057771e-08, 6.975467225354274e-09, 6.737920122696639e-10, 6.007811634222583e-11, 4.97418660438106e-12, 3.8438339320279626e-13, 2.784700131423801e-14, 1.898730451775006e-15], [0.02898185085356561, 0.03359386084122516, 0.019469900178593274, 0.007522743808380545, 0.001950430284475758, 0.0004748231727346256, 9.173064705006342e-05, 1.5189735748986345e-05, 2.200868189650362e-06, 2.8345578550966865e-07, 3.2856335715634385e-08, 3.462264509043439e-09, 3.3443582991528375e-10, 2.981969856095293e-11, 2.468931354033158e-12, 1.9078822065344005e-13, 1.3821824577302857e-14, 9.42432505671581e-16], [0.011508084591319318, 0.013339416942802515, 0.007731088651718336, 0.0029871236500071917, 0.0008656194588891164, 0.00017954410788978398, 3.6424314347705325e-05, 6.031525205286047e-06, 8.739185578178533e-07, 1.1255434216489339e-07, 1.3046561197446355e-08, 1.3747925572080073e-09, 1.3279744763297825e-10, 1.1840776327950412e-11, 9.803608132528411e-13, 7.575799742399682e-14, 5.488356393995047e-15, 3.742201646015044e-16], [0.0038080156793674734, 0.0044140020408025725, 0.002558210844794309, 0.00098843674680816, 0.0002864327634767105, 6.640281495631491e-05, 1.1477555225790026e-05, 1.9958267051281953e-06, 2.891789284526867e-07, 3.7244138791620466e-08, 4.3170963167214064e-09, 4.5491772085815154e-10, 4.394256565925954e-11, 3.918103100035447e-12, 3.244005827972697e-13, 2.506825873053367e-14, 1.816092594423123e-15, 1.238291431584477e-16], [0.0010800593492767039, 0.001251933965956556, 0.0007255798749232297, 0.0002803482021734037, 8.124031258809593e-05, 1.8833688500928566e-05, 3.638462761999762e-06, 5.39056200063286e-07, 8.201920149158174e-08, 1.0563475493444009e-08, 1.2244488025263263e-09, 1.2902734099196505e-10, 1.246333599114069e-11, 1.1112832091401048e-12, 9.20090440434323e-14, 7.110056651998227e-15, 5.150944615030289e-16, 3.512139524683365e-17], [0.0002680430594720028, 0.00031069793592050296, 0.00018007033566810917, 6.957524128498884e-05, 2.016176421523319e-05, 4.674038968610647e-06, 9.029732404561722e-07, 1.4952390887910648e-07, 1.9383616374527635e-08, 2.62158398222879e-09, 3.0387682252441e-10, 3.2021280365921133e-11, 3.0930806835106707e-12, 2.7579202153775955e-13, 2.2834287468565316e-14, 1.7645339020463557e-15, 1.2783324867361867e-16, 8.716230493436463e-18], [5.91301512205284e-05, 6.853979346107376e-05, 3.97234168247462e-05, 1.5348259889623625e-05, 4.4476740762015474e-06, 1.0310904209532711e-06, 1.9919539928188634e-07, 3.298489190700182e-08, 4.779240438203179e-09, 5.507195852353879e-10, 6.703505960451413e-11, 7.0638768041282635e-12, 6.823318944111091e-13, 6.083956798234606e-14, 5.037231233253819e-15, 3.892552064853897e-16, 2.8199944217813263e-17, 1.9227956439726867e-18], [1.1739670899238395e-05, 1.3607856603205001e-05, 7.88666747657309e-06, 3.047235906909156e-06, 8.830390053789165e-07, 2.047121808331546e-07, 3.9548155787565005e-08, 6.54880408120311e-09, 9.488680264588683e-10, 1.2220728758301326e-10, 1.2673928596106706e-11, 1.4024585975426947e-12, 1.3546983593133998e-13, 1.2079057655388179e-14, 1.00008939096429e-15, 7.728253565445095e-17, 5.598802939963968e-18, 3.817508935930434e-19], [2.118898580314031e-06, 2.4560882741200653e-06, 1.4234682269162825e-06, 5.49997005235524e-07, 1.59380114733939e-07, 3.694859532804286e-08, 7.138064761061232e-09, 1.1819966496093356e-09, 1.7126162491484376e-10, 2.2057249337413215e-11, 2.556731688825531e-12, 2.410497137836527e-13, 2.4451012766372605e-14, 2.1801546514556685e-15, 1.8050659246664503e-16, 1.3948760275035312e-17, 1.01053050828855e-18, 6.890239372216038e-20], [3.505708944350187e-07, 4.063587899247276e-07, 2.3551222986610014e-07, 9.099677721876785e-08, 2.6369374115655926e-08, 6.1131298272661195e-09, 1.1809898647671267e-09, 1.9556085719370677e-10, 2.833516506481086e-11, 3.649362787268073e-12, 4.2301020129480857e-13, 4.457506216097716e-14, 3.852342238670298e-15, 3.607056860900852e-16, 2.98647411255855e-17, 2.3078166228956842e-18, 1.6719185497405338e-19, 1.139987256601572e-20], [5.3540131941896164e-08, 6.206020971416363e-08, 3.5968062554886256e-08, 1.389727309345478e-08, 4.027201892081582e-09, 9.3361366481163e-10, 1.8036395543781902e-10, 2.9866581233720024e-11, 4.3274227845135106e-12, 5.573405215200923e-13, 6.460325814152866e-14, 6.807623642753117e-15, 6.575792394741268e-16, 5.24588652873034e-17, 4.561023763399735e-18, 3.5245597523624193e-19, 2.5533990747712852e-20, 1.741019265985921e-21], [7.592736602775538e-09, 8.801002328197998e-09, 5.10077235871924e-09, 1.970826934269686e-09, 5.711133331901122e-10, 1.3239942429278265e-10, 2.5578121618383222e-11, 4.235497304697225e-12, 6.136888382590883e-13, 7.903865053130724e-14, 9.161642023633187e-15, 9.65415872832478e-16, 9.325389721114083e-17, 8.314907840989153e-18, 6.159472994271518e-19, 4.998316752277294e-20, 3.621075614372592e-21, 2.469007868963525e-22], [1.0049721064610912e-09, 1.164897758405697e-09, 6.75136543001731e-10, 2.6085800143247954e-10, 7.559237196168147e-11, 1.7524344025988478e-11, 3.385511720865958e-12, 5.606090229253905e-13, 8.12276517364563e-14, 1.046152965285975e-14, 1.2126319092601463e-15, 1.2778212574590882e-16, 1.2343055003610643e-17, 1.1005584527894818e-18, 9.112108445643999e-20, 6.300017731300748e-21, 4.7928437113183165e-22, 3.26797065241832e-23], [1.2470416476661687e-10, 1.4454888953289661e-10, 8.377579651929535e-11, 3.2369136399096415e-11, 9.380045025731154e-12, 2.174546607606123e-12, 4.2009863631426736e-13, 6.956439836994291e-14, 1.0079311058113031e-14, 1.2981418182192898e-15, 1.5047208618171652e-16, 1.5856124922073462e-17, 1.531615011996624e-18, 1.3656520588938961e-19, 1.1306959324257272e-20, 8.737523815524017e-22, 5.663469172691032e-23, 4.055132954154492e-24], [1.456394295819118e-11, 1.688156755443459e-11, 9.784002996752114e-12, 3.780324875312819e-12, 1.095476169185521e-12, 2.5396082650787077e-13, 4.906245583333357e-14, 8.12428303157963e-15, 1.1771420111184646e-15, 1.5160731341708527e-16, 1.757332551043395e-17, 1.851804222699469e-18, 1.7887416759796552e-19, 1.594916955956501e-20, 1.3205165275534869e-21, 1.0204374383428302e-22, 7.392650980537664e-24, 4.509884635424124e-25]] |
| Legacy trial inputs | {"lambda_home": 1.985395040755909, "lambda_away": 1.159134418673338, "rho": -0.10287979955549995, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5767 |
| Legacy p draw | 0.2199 |
| Legacy p away | 0.2033 |
| Legacy p over 1 5 | 0.8334 |
| Legacy p under 3 5 | 0.6124 |
| Legacy p btts yes | 0.5978 |
| Legacy p over 2 5 | 0.6152 |
| Legacy goal margin distribution | {"-1": 0.12105030782287692, "-10": 6.24492235600765e-08, "-11": 6.469468906194668e-09, "-12": 6.159411169845277e-10, "-13": 5.424136262436213e-11, "-14": 4.442642649761006e-12, "-15": 3.3995291474782297e-13, "-16": 2.4239710073012773e-14, "-17": 1.455706321041344e-15, "-2": 0.05722089618094944, "-3": 0.01884492257552998, "-4": 0.004931986986506323, "-5": 0.0010657075217132253, "-6": 0.0001955773294338996, "-7": 3.1144578677865404e-05, "-8": 4.376138317884177e-06, "-9": 5.498384629308152e-07, "0": 0.21992632305254783, "1": 0.22823415897405228, "10": 1.444575774221815e-05, "11": 2.5632740757089396e-06, "12": 4.1800236851518627e-07, "13": 6.304973542566417e-08, "14": 8.845190482575844e-09, "15": 1.1593049989907398e-09, "16": 1.4158573232105146e-10, "17": 1.456394295819118e-11, "2": 0.17867463000428038, "3": 0.10078960069049839, "4": 0.04518106045702625, "5": 0.016721901472620457, "6": 0.005256289439963217, "7": 0.0014336936158554194, "8": 0.0003450468465516272, "9": 7.425663588543808e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5551 |
| Legacy raw p draw | 0.2366 |
| Legacy raw p away | 0.2083 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9854 |
| Legacy lambda away | 1.1591 |
| Legacy model home team | Man City |
| Legacy model away team | Brighton |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 79.5% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T06:52:39Z |
| Market reference home draw last update utc | 2026-10-30T06:52:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.9% |
| Market draw away odds | 2.37 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T06:52:39Z |
| Market reference draw away last update utc | 2026-10-30T06:52:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.5% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T06:52:39Z |
| Market reference home away last update utc | 2026-10-30T06:52:39Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.37 |
| Market reference dc home away odds | 1.22 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.24, "price": 1.64, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.64, "price": 2.24, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.04, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.04, "price": 1.78, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 87.8% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-30T06:52:22Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 53.1% |
| Market under 3 5 odds | 1.82 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference under 3 5 odds | 1.82 |
| Market reference under 3 5 opposite odds | 2.05 |
| Market reference under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.9% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T06:52:39Z |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.75 |
| Market reference btts yes last update utc | 2026-10-30T06:52:39Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 10.249093243279138, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,654.7730 |
| Elo away rating | 1,529.0307 |
| Elo rating diff | 185.7423 |
| Elo home expectancy | 0.7444 |

</details>


---

## 2026-10-31 — Tottenham Hotspur vs Crystal Palace

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **57.3%**. Expected goals are 1.62 for Tottenham Hotspur and 1.21 for Crystal Palace (2.83 combined). The most likely exact score is 2-1 at 11.5%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.0%; Under 3.5 goals: 63.0%; Double Chance 1X: 79.7%; Double Chance X2: 42.7%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 80.1%; BTTS Yes (both teams score): 60.0%; BTTS No (at least one team does not score): 40.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 57.3% | 1.75 |
| Draw | 22.4% | 4.47 |
| Crystal Palace win | 20.3% | 4.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.62 |
| Crystal Palace expected goals | 1.21 |
| Expected total goals | 2.83 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 82.0% |
| Under 1.5 | 18.0% |
| Over 2.5 | 60.0% |
| Under 2.5 | 40.0% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.9% |
| Under 4.5 | 80.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.48% |
| 2 | 1-1 | 10.35% |
| 3 | 1-0 | 9.10% |
| 4 | 2-0 | 8.80% |
| 5 | 3-1 | 6.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 57.3% | 62.2% | 1.58 | -9.5% |
| Draw | 22.4% | 20.7% | 4.55 | +1.8% |
| Crystal Palace win | 20.3% | 17.2% | 5.45 | +10.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:30:00+00:00 |
| Fixture id | 01b17432a283eb27af86ae45602eb6dd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T06:52:26Z |
| Market best draw last update utc | 2026-10-30T06:52:26Z |
| Market best away last update utc | 2026-10-30T06:52:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Tottenham |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6562 |
| Dc lambda away | 1.2166 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T06:51:51.118483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.5392 |
| Shot lambda away | 1.2062 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 60.0% |
| P btts no | 40.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.17 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.57 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.71 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.01 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.11385544109801744, "-10": 1.6704205375020308e-07, "-11": 1.9483675822489122e-08, "-12": 2.0884891803188113e-09, "-13": 2.070607379786764e-10, "-14": 1.908576343944612e-11, "-15": 1.6313113900482781e-12, "-16": 1.1647779649416576e-13, "-2": 0.059051537795424616, "-3": 0.02192653560740935, "-4": 0.006466591035352761, "-5": 0.0015741201171784451, "-6": 0.0003253729289336514, "-7": 5.835159929435449e-05, "-8": 9.232724720312674e-06, "-9": 1.3062141994166003e-06, "0": 0.22367800489678097, "1": 0.2586068987940252, "10": 5.076390674083751e-06, "11": 7.910253859643775e-07, "12": 1.1327708526853321e-07, "13": 1.500368380913386e-08, "14": 1.8475661292827815e-09, "15": 2.1096850894337957e-10, "16": 2.012399592580127e-11, "2": 0.17686339253499436, "3": 0.0877338257307036, "4": 0.03456708476476244, "5": 0.011241274102995767, "6": 0.0031041978573256228, "7": 0.0007437227240871371, "8": 0.00015720939064311934, "9": 2.9713465550593314e-05} |
| Raw goal margin distribution | {"-1": 0.15978803793481836, "-10": 1.338349937922513e-07, "-11": 1.454988230535939e-08, "-12": 1.4531703976926696e-09, "-13": 1.3416343574747577e-10, "-14": 1.1440854456445539e-11, "-15": 8.182330061544143e-13, "-2": 0.07957609488445931, "-3": 0.027988193983340272, "-4": 0.007771425615496187, "-5": 0.0017747430000150063, "-6": 0.0003433812981998671, "-7": 5.755685403653752e-05, "-8": 8.502995358170687e-06, "-9": 1.1223505158033847e-06, "0": 0.2627205042172876, "1": 0.21641098243688497, "10": 2.423666051258741e-06, "11": 3.52008285954678e-07, "12": 4.696780434000413e-08, "13": 5.7930622720679654e-09, "14": 6.599678748212808e-10, "15": 6.305675812483117e-11, "2": 0.14202449119395885, "3": 0.06673379213631422, "4": 0.024754943138757094, "5": 0.007552435416552109, "6": 0.001952173873212104, "7": 0.00043714872460710375, "8": 8.627687756467989e-05, "9": 1.5213925924309527e-05} |
| Unadjusted home-win probability | 46.0% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.3% |
| P home draw | 79.7% |
| P draw away | 42.7% |
| P home away | 77.6% |
| Raw p home draw | 72.3% |
| Raw p draw away | 54.0% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0753 |
| Totals anchor target over 2 5 | 0.5995 |
| Totals anchor reference over odds | 1.62 |
| Totals anchor reference under odds | 2.37 |
| Totals anchor reference last update utc | 2026-10-30T06:52:26Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5553 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:37Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.49, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:37Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.63, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.02, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:39Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 4.29, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:39Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.24, "price": 4.29, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.58 |
| Reference draw odds | 4.55 |
| Reference away odds | 5.45 |
| Market reference 1x2 last update utc | 2026-10-30T06:52:26Z |
| Market reference home last update utc | 2026-10-30T06:52:26Z |
| Market reference draw last update utc | 2026-10-30T06:52:26Z |
| Market reference away last update utc | 2026-10-30T06:52:26Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-10-30T06:52:22Z |
| Market reference under 2 5 last update utc | 2026-10-30T06:52:22Z |
| Home probability edge | -4.8% |
| Draw probability edge | +1.7% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | -0.1615 |
| Raw ev home | -0.2732 |
| Raw edge prob draw | 0.0558 |
| Raw ev draw | 0.1954 |
| Raw edge prob away | 0.1058 |
| Raw ev away | 0.5113 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.06455947195289603, 0.049430347711144296, 0.03498728019860854, 0.013768567035105978, 0.004063764826618615, 0.0009595296024026951, 0.0001888021529232147, 3.1842614362449644e-05, 4.699141744517332e-06, 6.164187646631742e-07, 7.27739026993558e-08, 7.810571197988042e-09, 7.684247854613439e-10, 6.978431618578434e-11, 5.884771530531505e-12, 4.63167590304024e-13], [0.10162211587512944, 0.11342171503959521, 0.05646147351815026, 0.022219320239314576, 0.00655798761263079, 0.0015484614673790973, 0.0003046835220380405, 5.1386701606077495e-05, 7.583340735832665e-06, 9.947589969712727e-07, 1.1744044569190415e-07, 1.2604476722782455e-08, 1.2400619719146233e-09, 1.1261593636142619e-10, 9.496676221911166e-12, 7.474466287738523e-13], [0.09333365195300132, 0.1101889574940944, 0.04898350710046549, 0.017928452199797648, 0.0052915465537906655, 0.0012494314453425001, 0.000245844782922734, 4.146319570207723e-05, 6.118889346425313e-06, 8.026568290762561e-07, 9.476101852948437e-08, 1.0170372270346214e-08, 1.0005882965276515e-09, 9.086819084675864e-11, 7.662732426900812e-12, 6.031040109031389e-13], [0.05020639394452669, 0.059273264171329915, 0.03498876905405862, 0.010369294445788019, 0.002846448899151574, 0.0006720989272243702, 0.00013224576304847482, 2.2304040333338244e-05, 3.2914962888658073e-06, 4.3176822206806684e-07, 5.0974208415969904e-08, 5.4708854318120616e-09, 5.382402717622873e-10, 4.888016370532787e-11, 4.121966245467479e-12, 3.244240092113251e-13], [0.020255411152632623, 0.023913375206262567, 0.01411596904763815, 0.005555066441135274, 0.0012347273386150827, 0.0002711535132599787, 5.3353608839148845e-05, 8.998405816913256e-06, 1.3279306757622558e-06, 1.7419380627680583e-07, 2.056518041877844e-08, 2.207189664183839e-09, 2.1714919449295305e-10, 1.972035303219267e-11, 1.6629778500218133e-12, 1.3088655006016912e-13], [0.006537520801283069, 0.0077181443843221805, 0.00455598953700864, 0.0017929215130600433, 0.0005291771731280349, 9.409637555999421e-05, 1.7220106024069608e-05, 2.9042740610481806e-06, 4.2859531954399746e-07, 5.622179788936452e-08, 6.637500160169756e-09, 7.123799281706216e-10, 7.008583362155222e-11, 6.364828498672515e-12, 5.367332316617816e-13, 4.2244195251268456e-14], [0.0017583440586629736, 0.0020758868284460976, 0.0012253876319839097, 0.0004822275884031488, 0.00014232850137427182, 3.360637639256861e-05, 4.979803826938308e-06, 7.811390885319706e-07, 1.1527581427244405e-07, 1.512152194861279e-08, 1.78523469764233e-09, 1.916030636512435e-10, 1.885041943127915e-11, 1.7118964077105662e-12, 1.443607932833263e-13, 1.1362079294415118e-14], [0.0004053664888677568, 0.00047857241066568155, 0.0002824993660552427, 0.00011117215847664671, 3.281223864217399e-05, 7.747572913677954e-06, 1.5244536931108567e-06, 1.9362346800580166e-07, 2.6575545242564468e-08, 3.4860971767419006e-09, 4.1156582389139307e-10, 4.417193596779288e-11, 4.345752642035571e-12, 3.9465850422165217e-13, 3.328076073343877e-14, 2.6193998649594793e-15], [8.177110776555389e-05, 9.653831098734681e-05, 5.6986176064839784e-05, 2.242580677232245e-05, 6.618931696925716e-06, 1.5628514863559003e-06, 3.075149787816607e-07, 5.186424375151969e-08, 5.763945430282783e-09, 7.032205072421546e-10, 8.302164649091438e-11, 8.91042608461372e-12, 8.7663143691747e-13, 7.961107779145761e-14, 6.71344264311262e-15, 5.283890862240336e-16], [1.4662208695548391e-05, 1.7310085450603328e-05, 1.02180737066634e-05, 4.021125163237013e-06, 1.1868269922446457e-06, 2.802316769242925e-07, 5.51398766521688e-08, 9.299670586606761e-09, 1.372389520733497e-09, 1.355740848614661e-10, 1.4886440215386312e-11, 1.5977101251146238e-12, 1.5718697506232012e-13, 1.4274898175558338e-14, 1.2037735550939492e-15, 9.474435734537606e-17], [2.366145362777358e-06, 2.7934521509477785e-06, 1.6489635510971407e-06, 6.489176941690464e-07, 1.9152675033000108e-07, 4.5222987656631336e-08, 8.898315809967738e-09, 1.50075427861952e-09, 2.2147230119522935e-10, 2.905204603992982e-11, 2.582965000928012e-12, 2.5783389679552e-13, 2.53663850962393e-14, 2.3036422972530215e-15, 1.9426153824180241e-16, 1.5289573790485313e-17], [3.4712889157580957e-07, 4.0981757253085803e-07, 2.419136620876836e-07, 9.520044011008077e-08, 2.8098218137845627e-08, 6.634505988493688e-09, 1.3054407191534196e-09, 2.2017039927477472e-10, 3.2491424930209483e-11, 4.262123831653682e-12, 5.031829055153044e-13, 4.067007667502397e-14, 3.7214134348056215e-15, 3.379592859392032e-16, 2.8499429285500654e-17, 2.2430797727185615e-18], [4.6682224244150616e-08, 5.511265781776885e-08, 3.253277988483027e-08, 1.280264593703535e-08, 3.778675160161684e-09, 8.922146897599393e-10, 1.7555691233973904e-10, 2.960872517470817e-11, 4.369477797479087e-12, 5.731744758045979e-13, 6.766851679920966e-14, 7.26262779262978e-15, 5.38089278845367e-16, 4.5449086937096476e-17, 3.832630417757968e-18, 3.016515060795458e-19], [5.794956938564296e-09, 6.841479470931976e-09, 4.038497770337172e-09, 1.589272642982543e-09, 4.690706193311532e-10, 1.1075619876362698e-10, 2.1792979313824586e-11, 3.675516541282155e-12, 5.424106518141505e-13, 7.11517383619098e-14, 8.400116903107293e-15, 9.015554849956276e-16, 8.869742846947206e-17, 6.066098728576199e-18, 4.7576842346200035e-19, 3.7445891160660995e-20], [6.679811427553788e-10, 7.886131551242934e-10, 4.6551516848945126e-10, 1.8319448573372023e-10, 5.4069483458737255e-11, 1.276679930527642e-11, 2.5120633993355357e-12, 4.2367454417533976e-13, 6.252334415642286e-14, 8.201617372465813e-15, 9.682763388413618e-16, 1.0392174946410556e-16, 1.0224098342166489e-17, 9.28499086603437e-19, 5.896512763910596e-20, 4.3163649763355944e-21], [7.186459267141781e-11, 8.484275908531644e-11, 5.008233889337809e-11, 1.9708935259157293e-11, 5.817052542363596e-12, 1.3735130725500437e-12, 2.702597444792491e-13, 4.5580925259082454e-14, 6.726559138663677e-15, 8.82369058036307e-16, 1.0417178005530737e-16, 1.1180396746130961e-17, 1.099957193045172e-18, 9.989235381600476e-20, 8.423722004944627e-21, 4.992919508758897e-22]] |
| Legacy trial inputs | {"lambda_home": 1.6137714391527853, "lambda_away": 1.1805919428673022, "rho": -0.10287979955549995, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5419 |
| Legacy p draw | 0.2387 |
| Legacy p away | 0.2194 |
| Legacy p over 1 5 | 0.7844 |
| Legacy p under 3 5 | 0.6880 |
| Legacy p btts yes | 0.5578 |
| Legacy p over 2 5 | 0.5426 |
| Legacy goal margin distribution | {"-1": 0.12695590438053014, "-10": 8.642955310441651e-08, "-11": 9.145754213544953e-09, "-12": 8.890278782588823e-10, "-13": 7.988409641859865e-11, "-14": 6.632218159305358e-12, "-15": 4.63167590304024e-13, "-2": 0.06322662264839485, "-3": 0.021717674399421915, "-4": 0.005881761100025172, "-5": 0.001309148843767762, "-6": 0.0002467608089100186, "-7": 4.028186515697789e-05, "-8": 5.794356306453086e-06, "-9": 7.445880913455301e-07, "0": 0.23866799158235846, "1": 0.25291927013382737, "10": 2.81014043083256e-06, "11": 4.0646905870219167e-07, "12": 5.40089278188312e-08, "13": 6.633652432581968e-09, "14": 7.528239018406952e-10, "15": 7.186459267141781e-11, "2": 0.16866619979976974, "3": 0.0791924180400336, "4": 0.029317023613717026, "5": 0.008919566188136793, "6": 0.002298122111108885, "7": 0.0005128008039121441, "8": 0.00010082924919636769, "9": 1.771085926219927e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4624 |
| Legacy raw p draw | 0.2704 |
| Legacy raw p away | 0.2672 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6138 |
| Legacy lambda away | 1.1806 |
| Legacy model home team | Tottenham |
| Legacy model away team | Crystal Palace |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 82.3% |
| Market home draw odds | 1.18 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T06:52:39Z |
| Market reference home draw last update utc | 2026-10-30T06:52:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 38.7% |
| Market draw away odds | 2.51 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T06:52:39Z |
| Market reference draw away last update utc | 2026-10-30T06:52:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.0% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T06:52:39Z |
| Market reference home away last update utc | 2026-10-30T06:52:39Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.18 |
| Market reference dc draw away odds | 2.51 |
| Market reference dc home away odds | 1.23 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.3, "price": 1.59, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.59, "price": 2.3, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.83, "price": 1.99, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.99, "price": 1.83, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.5, "price": 2.52, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:52:39Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.52, "price": 1.5, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 82.8% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-30T06:52:22Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.9% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.56 |
| Market reference under 3 5 last update utc | 2026-10-30T06:52:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.4% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T06:52:39Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.19 |
| Market reference btts yes last update utc | 2026-10-30T06:52:39Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 10.029673704149188, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,397.3033 |
| Elo away rating | 1,450.5828 |
| Elo rating diff | 6.7205 |
| Elo home expectancy | 0.5097 |

</details>


---

## 2026-11-01 — Liverpool vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **40.1%**. Expected goals are 1.24 for Liverpool and 1.39 for Arsenal (2.63 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.1%; Double Chance 1X: 59.9%; Double Chance X2: 67.8%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 32.2% | 3.10 |
| Draw | 27.6% | 3.62 |
| Arsenal win | 40.1% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.24 |
| Arsenal expected goals | 1.39 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 76.3% |
| Under 1.5 | 23.7% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.15% |
| 2 | 1-2 | 8.78% |
| 3 | 0-1 | 8.64% |
| 4 | 2-1 | 7.69% |
| 5 | 0-0 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 32.2% | 32.2% | 3.00 | -3.3% |
| Draw | 27.6% | 27.5% | 3.50 | -3.3% |
| Arsenal win | 40.1% | 40.4% | 2.41 | -3.3% |
| Over 2.5 | 50.9% | 50.9% | 1.91 | -2.7% |
| Under 2.5 | 49.1% | 49.1% | 1.98 | -2.9% |

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
| Market best home last update utc | 2026-10-30T06:52:26Z |
| Market best draw last update utc | 2026-10-30T06:52:26Z |
| Market best away last update utc | 2026-10-30T06:52:26Z |
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
| Dc lambda home | 1.1858 |
| Dc lambda away | 1.4391 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T06:51:51.118483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.3547 |
| Shot lambda away | 1.2844 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.18 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.22 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.19 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.20558287959219704, "-10": 8.167041156206678e-07, "-11": 1.0529564430656178e-07, "-12": 1.2466091505144671e-08, "-13": 1.3554917073567934e-09, "-14": 1.2306789107934314e-10, "-2": 0.12178396249822102, "-3": 0.05116292883894795, "-4": 0.01692263132942567, "-5": 0.0045962245299834325, "-6": 0.001056602105495872, "-7": 0.000210289125028568, "-8": 3.6870559344532766e-05, "-9": 5.774077455825593e-06, "0": 0.27622925353932226, "1": 0.17895682969087617, "10": 2.451166344903635e-07, "11": 2.8058182743331998e-08, "12": 2.9493107627977938e-09, "13": 2.8472669198390476e-10, "14": 2.2951822050636324e-11, "2": 0.0946606329586423, "3": 0.03530821752423201, "4": 0.010368821090493844, "5": 0.0025003673328462817, "6": 0.0005103347528048554, "7": 9.017820332680907e-05, "8": 1.4038011137937122e-05, "9": 1.951864000201079e-06} |
| Raw goal margin distribution | {"-1": 0.20626805409067767, "-10": 6.374572791451597e-07, "-11": 7.967739374788659e-08, "-12": 9.144542438355564e-09, "-13": 9.645200603975237e-10, "-14": 8.543820956677999e-11, "-2": 0.11982556608089902, "-3": 0.04911021577849055, "-4": 0.015808687782500462, "-5": 0.004172909705859035, "-6": 0.0009315053801467385, "-7": 0.00017992042199887811, "-8": 3.06029125181755e-05, "-9": 4.647962733223439e-06, "0": 0.28008582435399104, "1": 0.18207991686392214, "10": 1.9402692750027613e-07, "11": 2.1532136971574886e-08, "12": 2.1940932729092514e-09, "13": 2.0546860056744805e-10, "14": 1.61594817808816e-11, "2": 0.09445646184559056, "3": 0.03437123355277887, "4": 0.009823362962564955, "5": 0.0023022074149855547, "6": 0.00045628051250861925, "7": 7.824707399119064e-05, "8": 1.1816571801542718e-05, "9": 1.5934280825077396e-06} |
| Unadjusted home-win probability | 32.4% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 39.6% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 73.0% |
| Raw p btts yes | 54.3% |
| P home draw | 59.9% |
| P draw away | 67.8% |
| P home away | 72.4% |
| Raw p home draw | 60.4% |
| Raw p draw away | 67.6% |
| Raw p home away | 72.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0323 |
| Totals anchor target over 2 5 | 0.5094 |
| Totals anchor reference over odds | 1.91 |
| Totals anchor reference under odds | 1.98 |
| Totals anchor reference last update utc | 2026-10-30T06:52:26Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4903 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:37Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:51:37Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T06:52:26Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.00 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.41 |
| Market reference 1x2 last update utc | 2026-10-30T06:52:26Z |
| Market reference home last update utc | 2026-10-30T06:52:26Z |
| Market reference draw last update utc | 2026-10-30T06:52:26Z |
| Market reference away last update utc | 2026-10-30T06:52:26Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market reference under 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market best over 2 5 last update utc | 2026-10-30T06:52:26Z |
| Market best under 2 5 last update utc | 2026-10-30T06:52:26Z |
| Home probability edge | +0.1% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0017 |
| Raw ev home | -0.0293 |
| Raw edge prob draw | 0.0055 |
| Raw ev draw | -0.0197 |
| Raw edge prob away | -0.0072 |
| Raw ev away | -0.0448 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.0962722498742817, 0.10449554283352284, 0.08331142566169596, 0.03962183361532083, 0.014132722671933167, 0.004032803773009466, 0.000958974587388943, 0.0001954610902460878, 3.4859534876920824e-05, 5.526247569809082e-06, 7.884635030152322e-07, 1.0226809548989688e-07, 1.2159344986216761e-08, 1.3344984891291732e-09, 1.360007517650471e-10], [0.08478280442427027, 0.13471548183544443, 0.08520951807363301, 0.04052454175090913, 0.014454709883777755, 0.004124683538354782, 0.0009808229998138464, 0.00019991429950614272, 3.565374309155662e-05, 5.652152612189876e-06, 8.064271446199226e-07, 1.045980795766039e-07, 1.2436372539990504e-08, 1.3649024995735908e-09, 1.390992702802771e-10], [0.050816270677549236, 0.0725026779608698, 0.044561944782564075, 0.020723908187406073, 0.007392016480982935, 0.002109328304719253, 0.0005015845933848802, 0.00010223448333556929, 1.823302291506373e-05, 2.890463080772594e-06, 4.1240002681980703e-07, 5.349057396005975e-08, 6.359855819896085e-09, 6.979996037904509e-10, 7.113419132392717e-11], [0.017324674258231518, 0.02471817120331249, 0.01763346249774268, 0.007225309043747006, 0.002520143173377091, 0.0007191284463752226, 0.00017100408151713754, 3.4854567211085164e-05, 6.216142556992225e-06, 9.854389285586317e-07, 1.4059859240901842e-07, 1.823641832404867e-08, 2.168251013699368e-09, 2.3796739915797817e-10, 2.425161620241101e-11], [0.004429846004319747, 0.006320331932766896, 0.00450880185241193, 0.002144327688331136, 0.0006589785007300507, 0.00018387810513980382, 4.37250210849498e-05, 8.912165561725298e-06, 1.5894413861946312e-06, 2.5197257016838115e-07, 3.5950465995061583e-08, 4.662975109474689e-09, 5.544126224961909e-10, 6.08472584595619e-11, 6.201035790413349e-12], [0.000906154324381083, 0.0012928657354715533, 0.0009223052657714021, 0.00043863642342793676, 0.000156457345874034, 3.846502669282422e-05, 8.944242508914403e-06, 1.8230424614044054e-06, 3.25130757151839e-07, 5.154265720768694e-08, 7.353905800150416e-09, 9.53842426082416e-10, 1.1340877197006016e-10, 1.2446709507756888e-11, 1.2684629198499189e-12], [0.00015446655459238487, 0.0002203868704651844, 0.0001572197062387008, 7.477165337363176e-05, 2.667032149776234e-05, 7.610435417172111e-06, 1.5591874781707016e-06, 3.107628362101517e-07, 5.542304053292491e-08, 8.786159773442185e-09, 1.2535750933176293e-09, 1.6259565199517804e-10, 1.933209586428182e-11, 2.121714019285456e-12, 2.1622707256982962e-13], [2.2569397330169085e-05, 3.220113803280538e-05, 2.2971665468924975e-05, 1.0925026187554834e-05, 3.89685057969192e-06, 1.1119749594920813e-06, 2.644204350091626e-07, 4.643410287201211e-08, 8.097964160167238e-09, 1.2837622452086537e-09, 1.831622025813229e-10, 2.3757154962903457e-11, 2.8246487010554778e-12, 3.1000760552086694e-13, 3.1593342178478144e-14], [2.885449766406177e-06, 4.116847466306503e-06, 2.9368788980761776e-06, 1.396741516829209e-06, 4.982041137563504e-07, 1.421636493069754e-07, 3.3805593976154786e-08, 6.89035803648031e-09, 1.058746252515831e-09, 1.6412629085167637e-10, 2.341690063412781e-11, 3.037302070381494e-12, 3.611253688083739e-13, 3.9633817414282823e-14, 4.0391420504181105e-15], [3.2790991694164053e-07, 4.678491119321532e-07, 3.3375445545713685e-07, 1.587292907000949e-07, 5.6617194124748404e-08, 1.6155841969285796e-08, 3.841754461277738e-09, 7.830379713227596e-10, 1.3965101410675984e-10, 1.9073995163517135e-11, 2.661156687378837e-12, 3.4516680249330316e-13, 4.1039213737191776e-14, 4.504088730882507e-15, 4.590184690401738e-16], [3.3538072085841894e-08, 4.7850816430386325e-08, 3.413584160702438e-08, 1.623456357552546e-08, 5.790710923182781e-09, 1.652392210723562e-09, 3.929281531347177e-10, 8.008780025048159e-11, 1.4283269690824872e-11, 2.2643126104963367e-12, 2.7834054232826764e-13, 3.530307717323542e-14, 4.197421418362197e-15, 4.60670582781582e-16, 4.694763320055969e-17], [3.1183793894204745e-09, 4.449182390136591e-09, 3.1739601678775085e-09, 1.509494294143596e-09, 5.38421932743362e-10, 1.5363989319274371e-10, 3.653457035700081e-11, 7.44658622612226e-12, 1.3280624391109612e-12, 2.105364243270693e-13, 3.0038517916590056e-14, 3.356803348250952e-15, 3.902774257933066e-16, 4.283328054700084e-17, 4.365204159022031e-18], [2.6578547783496124e-10, 3.7921237920864787e-10, 2.7052273456862226e-10, 1.286571042700046e-10, 4.5890737719893886e-11, 1.3095023833624908e-11, 3.113911755822329e-12, 6.346868777621579e-13, 1.1319331803285471e-13, 1.794442470062423e-14, 2.560240702270245e-15, 3.3207743873445434e-16, 3.4017172203410924e-17, 3.650762949513747e-18, 3.7205475292358377e-19], [2.091083804154697e-11, 2.983477016718582e-11, 2.128354466617424e-11, 1.0122177826265732e-11, 3.610482378061608e-12, 1.0302591577451072e-12, 2.449889472219492e-13, 4.993438549046955e-14, 8.905554810786555e-15, 1.411788791923719e-15, 2.0142853217056907e-16, 2.6126399362345075e-17, 3.106344178725917e-18, 2.937286470199976e-19, 2.927163946031615e-20], [1.5276608373634117e-12, 2.1796070480576597e-12, 1.5548892685309109e-12, 7.39485171435554e-13, 2.6376716810663976e-13, 7.52665466824006e-14, 1.7897896751639518e-14, 3.64800325075612e-15, 6.506036387638477e-16, 1.0313955106750535e-16, 1.4715549874815532e-17, 1.9086885493479866e-18, 2.269368802810702e-19, 2.4906516280775702e-20, 2.186880410972973e-21]] |
| Legacy trial inputs | {"lambda_home": 1.0227830984389183, "lambda_away": 1.4267610943142601, "rho": -0.10287979955549995, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T06:52:26Z", "over": 1.91, "under": 1.98, "bookmaker": "pinnacle", "event_id": "6a3819cdbe2ba2fe5a3d8f9b4b459965", "kickoff_utc": "2026-11-01T16:30:00Z", "home_team": "Liverpool", "away_team": "Arsenal"}} |
| Legacy p home | 0.2896 |
| Legacy p draw | 0.2835 |
| Legacy p away | 0.4269 |
| Legacy p over 1 5 | 0.7144 |
| Legacy p under 3 5 | 0.7691 |
| Legacy p btts yes | 0.4985 |
| Legacy p over 2 5 | 0.4456 |
| Legacy goal margin distribution | {"-1": 0.21314225364321127, "-10": 8.996656068466805e-07, "-11": 1.1542671924988026e-07, "-12": 1.359538167711428e-08, "-13": 1.4735977594094502e-09, "-14": 1.360007517650471e-10, "-2": 0.13199271713407867, "-3": 0.056366122154054635, "-4": 0.018795487632625243, "-5": 0.005122336890652236, "-6": 0.0011781442726932715, "-7": 0.00023415067354801483, "-8": 4.0942891009813635e-05, "-9": 6.388395655124143e-06, "0": 0.2834740357631431, "1": 0.1772276118052438, "10": 3.826816315554148e-08, "11": 3.519614798466732e-09, "12": 2.97175137270678e-10, "13": 2.309044508960463e-11, "14": 1.5276608373634117e-12, "2": 0.08050969705628717, "3": 0.02464612604756092, "4": 0.005891371232662641, "5": 0.0011509679085966232, "6": 0.00018976924832927964, "7": 2.703678558110178e-05, "8": 3.388991153134273e-06, "9": 3.790670363930991e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2574 |
| Legacy raw p draw | 0.2924 |
| Legacy raw p away | 0.4502 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0228 |
| Legacy lambda away | 1.4268 |
| Legacy model home team | Liverpool |
| Legacy model away team | Arsenal |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.788153494379117, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,570.2236 |
| Elo away rating | 1,650.6613 |
| Elo rating diff | -20.4377 |
| Elo home expectancy | 0.4706 |

</details>


---
