# Ligue 1 — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,751 |
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
| Training sha256 | dcb4f67f73dec029a09c4b807eb50a43374b03d4f76d82f7042fe6eda94a0d6f |
| Training as of utc | 2026-10-26T11:44:12.100474+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 71, 'bbs_added_results': 8, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 71, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 80, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-26T11:44:12.100474+00:00', 'observations': 278, 'observations_sha256': 'f15706afdba55ec4b08959f76ce1965327f38aa94fa471773b034c391c8f8aef', 'eligible_training_matches': 115, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 122, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 14, 'retrospective_eligible_training_matches': 115, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '481fe77c86554edabad44b4faa13b6ff0b095bdefe697545466dd95806316859', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-26', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1741, 'tune_start_date': '2025-10-27', 'audit_start_date': '2026-04-27', 'training_shot_matches': 1453, 'tuning_matches': 196, 'audit_matches': 88, 'audit_matchdays': 28, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.873365030729784, 'audit_candidate_poisson_score': 0.8692351434347145, 'audit_gain': 0.004129887295069468, 'audit_gain_lower95': -0.0034463444146306393, 'audit_baseline_briers': [0.6036683508631172, 0.16968918140114747, 0.22109314542147204, 0.24521839802974899], 'audit_candidate_briers': [0.602908213184978, 0.16856938601387472, 0.21938689348044688, 0.24310665446246993], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1588.318 |
| Base scoring parameter | 0.209 |
| Home-advantage parameter | 0.191 |
| Dixon-Coles low-score adjustment | -0.056 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1751, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261026T114412100474Z_53cd7f0d414f918a7bbe999be4b5de61addfad777c8ea4e4ff5dce3b917c4470.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'AVAILABLE': 1} |
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

## 2026-10-26 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **71.3%**. Expected goals are 2.23 for Paris Saint Germain and 1.08 for Lyon (3.31 combined). The most likely exact score is 2-1 at 11.1%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 66.1%; Under 3.5 goals: 56.7%; Double Chance 1X: 87.8%; Double Chance X2: 28.7%; Double Chance 12 (either team wins): 83.5%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 58.1%; BTTS No (at least one team does not score): 41.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 71.3% | 1.40 |
| Draw | 16.5% | 6.07 |
| Lyon win | 12.2% | 8.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.23 |
| Lyon expected goals | 1.08 |
| Expected total goals | 3.31 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 66.1% |
| Under 2.5 | 33.9% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.14% |
| 2 | 2-0 | 10.29% |
| 3 | 1-0 | 8.68% |
| 4 | 3-1 | 8.27% |
| 5 | 3-0 | 7.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 71.3% | 75.0% | 1.36 | -3.0% |
| Draw | 16.5% | 14.8% | 5.61 | -7.5% |
| Lyon win | 12.2% | 10.2% | 8.22 | +0.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T19:30:00+00:00 |
| Fixture id | 8664b2167f22c59026d86615421463b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T11:44:30Z |
| Market best draw last update utc | 2026-10-26T11:44:30Z |
| Market best away last update utc | 2026-10-26T11:44:30Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2285 |
| Dc lambda away | 1.0820 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T11:44:12.100474+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.86 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.88 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.95 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 3.98 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.07661817590836535, "-10": 1.9940105776241284e-08, "-11": 1.9267496491249865e-09, "-12": 1.7112095737148785e-10, "-13": 1.4058614492397248e-11, "-14": 1.074318225283646e-12, "-15": 7.670010827994394e-14, "-16": 5.0996139365345444e-15, "-17": 2.8426224204444757e-16, "-2": 0.032374148041269805, "-3": 0.009889514033338091, "-4": 0.002405660469750212, "-5": 0.00048374443173699905, "-6": 8.26801175572253e-05, "-7": 1.2268647018583374e-05, "-8": 1.6069247261535761e-06, "-9": 1.8825423258335597e-07, "0": 0.16487088941816802, "1": 0.25308166065647886, "10": 4.287837256462152e-05, "11": 8.533077626561962e-06, "12": 1.560821294086456e-06, "13": 2.640961526496506e-07, "14": 4.156445285748748e-08, "15": 6.1115965045011935e-09, "16": 8.368845847383545e-10, "17": 9.607646563620224e-11, "2": 0.21505651626709715, "3": 0.1353003067645423, "4": 0.06778408441729761, "5": 0.028072361873985242, "6": 0.009881744764115939, "7": 0.003019943310659088, "8": 0.000814642802257743, "9": 0.00019655586756334146} |
| Raw goal margin distribution | {"-1": 0.10563740707072727, "-10": 2.7492446093175354e-08, "-11": 2.656508518963246e-09, "-12": 2.359332367009636e-10, "-13": 1.9383332536655255e-11, "-14": 1.4812176137359446e-12, "-15": 1.0575037143180875e-13, "-16": 7.031099173667955e-15, "-17": 3.919269262374635e-16, "-2": 0.04463589761382209, "-3": 0.013635179998553619, "-4": 0.0033168074194417593, "-5": 0.0006669632479206494, "-6": 0.0001139953167965538, "-7": 1.6915412615137095e-05, "-8": 2.215549501357528e-06, "-9": 2.595557615986531e-07, "0": 0.204032590125538, "1": 0.2228083622412257, "10": 3.774931752032445e-05, "11": 7.512362001734179e-06, "12": 1.3741178850516248e-06, "13": 2.3250531505697634e-07, "14": 3.65925671761722e-08, "15": 5.3805352956626845e-09, "16": 7.367775413943552e-10, "17": 8.458392402989636e-11, "2": 0.18933173606686138, "3": 0.11911586040152439, "4": 0.05967584057992641, "5": 0.024714382532346306, "6": 0.008699703333964649, "7": 0.0026587016276245186, "8": 0.0007171962919471374, "9": 0.00017304411084980066} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 84.8% |
| Raw p under 3 5 | 57.8% |
| Raw p btts yes | 59.5% |
| P home draw | 87.8% |
| P draw away | 28.7% |
| P home away | 83.5% |
| Raw p home draw | 83.2% |
| Raw p draw away | 37.2% |
| Raw p home away | 79.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.6611 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:43:22Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.61, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:43:22Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:43:22Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:43:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:43:22Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:44:10Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:44:10Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:43:22Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:43:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:43:22Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:43:22Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T11:43:22Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 5.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 7.01, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.13, "price": 7.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T11:44:30Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.41, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.30 |
| Reference draw odds | 5.70 |
| Reference away odds | 8.00 |
| Market reference 1x2 last update utc | 2026-10-26T11:44:31Z |
| Market reference home last update utc | 2026-10-26T11:44:31Z |
| Market reference draw last update utc | 2026-10-26T11:44:31Z |
| Market reference away last update utc | 2026-10-26T11:44:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.90 |
| Market reference over 2 5 last update utc | 2026-10-26T11:43:47Z |
| Market reference under 2 5 last update utc | 2026-10-26T11:43:47Z |
| Home probability edge | -3.7% |
| Draw probability edge | +1.7% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.1219 |
| Raw ev home | -0.1460 |
| Raw edge prob draw | 0.0559 |
| Raw ev draw | 0.1446 |
| Raw edge prob away | 0.0659 |
| Raw ev away | 0.3812 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.030739287287655546, 0.023162554821260475, 0.014924334712157077, 0.005453237495617799, 0.0014944283827634216, 0.0003276316049691337, 5.985703843507823e-05, 9.373415565909273e-06, 1.284365322103428e-06, 1.5643241430074956e-07, 1.7147761497870507e-08, 1.7088165268875805e-09, 1.5609711483427109e-10, 1.3162312878050084e-11, 1.0305874767617973e-12, 7.531375272913967e-14, 5.1598252314014415e-15, 3.3271069145952995e-16, 2.0261656023010796e-17], [0.07133945813402616, 0.0745273641017821, 0.03618479538588154, 0.013221646845591756, 0.0036233163013356523, 0.0007943592003534325, 0.00014512638117221, 2.2726314496483284e-05, 3.1140079124047747e-06, 3.7927820652408427e-07, 4.157560474845851e-08, 4.143111071280901e-09, 3.784652562102833e-10, 3.191268538819563e-11, 2.4987108432713292e-12, 1.826019574612522e-13, 1.2510254147079795e-14, 8.066736993878501e-16, 4.9125397648348017e-17], [0.09274631135230511, 0.10166637355727035, 0.046644901950610565, 0.01602827177892257, 0.004392455727871099, 0.0009629817905473312, 0.00017593308208010793, 2.7550542646988903e-05, 3.775033906489517e-06, 4.5978948348761955e-07, 5.0401065772191386e-08, 5.022589926677261e-09, 4.588039641552297e-10, 3.868695031495205e-11, 3.029124659024363e-12, 2.213637858984287e-13, 1.516586820344873e-14, 9.779103497238108e-16, 5.955349087378568e-17], [0.07495602235778244, 0.08216506789629881, 0.045033728912260304, 0.013774425742315927, 0.003549909478267274, 0.0007782658261007934, 0.00014218618338121523, 2.2265889182075956e-05, 3.0509194572855895e-06, 3.715941939001403e-07, 4.0733300956044395e-08, 4.059173430713875e-09, 3.707977136085194e-10, 3.126614816784185e-11, 2.4480880409773534e-12, 1.7890252068330475e-13, 1.2256801802227484e-14, 7.903308387043792e-16, 4.8130138313134407e-17], [0.045433655574384786, 0.04980332837337105, 0.027296631601708973, 0.009973979934479134, 0.0022880491347469054, 0.0004717360977293939, 8.618437691828406e-05, 1.349619027710888e-05, 1.8492766751397736e-06, 2.252371735857891e-07, 2.4689980975925294e-08, 2.460417212208167e-09, 2.2475439701756942e-10, 1.8951584706761313e-11, 1.4838779509754398e-12, 1.0843952561032071e-13, 7.429307132491992e-15, 4.790491542375881e-16, 2.9173481437271175e-17], [0.022031233717273214, 0.024150131734291987, 0.013236409505437412, 0.004836482564519654, 0.001325410239874351, 0.0002432412154386448, 4.1791665818208686e-05, 6.544437565693332e-06, 8.967327441042688e-07, 1.0921975681578755e-07, 1.1972418562382104e-08, 1.1930808991456315e-09, 1.0898565363229493e-10, 9.189812853684575e-12, 7.195472504369591e-13, 5.2583409868919836e-14, 3.602545287718735e-15, 2.3229572319557473e-16, 1.4146512750636315e-17], [0.008902637867766895, 0.009758866890904062, 0.00534872272740619, 0.001954382281911364, 0.0005355872278083131, 0.00011741968037526601, 1.7957525471261187e-05, 2.6445526584331833e-06, 3.623622257100393e-07, 4.4134793149335616e-08, 4.8379545253814444e-09, 4.821140444674968e-10, 4.4040194004636224e-11, 3.713526757457923e-12, 2.9076304493856873e-13, 2.1248517533011465e-14, 1.4557585158585269e-15, 9.386876506238526e-17, 5.716487861136889e-18], [0.003083555777027478, 0.0033801229282436913, 0.0018526065095298085, 0.0006769282167173653, 0.00018550828585199046, 4.06699833392967e-05, 7.430250070421682e-06, 9.740073589343827e-07, 1.2550933229692314e-07, 1.528671596047784e-08, 1.6756946477345805e-09, 1.6698708507355383e-10, 1.525395019560316e-11, 1.2862330307250598e-12, 1.0070993342463334e-13, 7.359727528558027e-15, 5.042227537733702e-16, 3.251278745578783e-17, 1.979987216186479e-18], [0.0009345293861055916, 0.0010244096210700272, 0.0005614671338019669, 0.0002051557865498585, 5.622176377878973e-05, 1.2325800897182505e-05, 2.2518765798411984e-06, 3.5263647413635074e-07, 4.044772421983087e-08, 4.632925854153799e-09, 5.078506774920156e-10, 5.0608566663186996e-11, 4.622995574843874e-12, 3.898170331625927e-13, 3.0522033348391393e-14, 2.2305034014328673e-15, 1.528141582697564e-16, 9.853609760524279e-18, 6.0007224497926815e-19], [0.00025175702241802964, 0.0002759702581549768, 0.00015125612516115916, 5.5267828622122535e-05, 1.514583067635998e-05, 3.320502253785231e-06, 6.066430344756006e-07, 9.499830614692852e-08, 1.3016869807568807e-08, 1.3271527134034925e-09, 1.3681214983636982e-10, 1.363366657207365e-11, 1.2454093128355797e-12, 1.0501454209568961e-13, 8.22246613983586e-15, 6.008852190064541e-16, 4.11672848829651e-17, 2.6545077022313473e-18, 1.6165612754162596e-19], [6.1039748296013e-05, 6.691036831137521e-05, 3.667280348087799e-05, 1.3399961262490474e-05, 3.6721823420836478e-06, 8.050723663662111e-07, 1.4708363553980583e-07, 2.3032814100127472e-08, 3.1560051394978273e-09, 3.84393361468741e-10, 3.527221445756549e-11, 3.305550597628708e-12, 3.019557121023137e-13, 2.546130056423363e-14, 1.9935780091754336e-15, 1.4568762440336962e-16, 9.981213962381584e-18, 6.435986588885929e-19, 3.9194336034307836e-20], [1.3453992758050684e-05, 1.4747957451170323e-05, 8.083185894811036e-06, 2.9535341612062685e-06, 8.093990557929949e-07, 1.7744892613695825e-07, 3.241923865386531e-08, 5.076746263727365e-09, 6.956265626335809e-10, 8.472553779814655e-11, 9.287418604613765e-12, 7.747457153299936e-13, 6.655515589899509e-14, 5.612017791104262e-15, 4.394117742423148e-16, 3.211153876577456e-17, 2.199995644071284e-18, 1.4185791942958993e-19, 8.638966048892212e-21], [2.7183231528830687e-06, 2.9797633251483304e-06, 1.6331740147380798e-06, 5.967492652643086e-07, 1.6353570518812856e-07, 3.5852815818091725e-08, 6.550172028218941e-09, 1.0257354198250801e-09, 1.4054844721362114e-10, 1.7118441727966308e-11, 1.8764842138280164e-12, 1.8699625822479334e-13, 1.4299093897080677e-14, 1.1338848006159261e-15, 8.878131726788406e-17, 6.4880025484980514e-18, 4.44499949053588e-19, 2.86618012763927e-20, 1.7454670780629238e-21], [5.069777183313619e-07, 5.557373155391565e-07, 3.0459323232111625e-07, 1.1129603211404121e-07, 3.0500037714078974e-08, 6.686687982601524e-09, 1.221632264737288e-09, 1.9130359913354644e-10, 2.6212825729642963e-11, 3.1926551923850887e-12, 3.4997151983286277e-13, 3.487552104714238e-14, 3.1858120097401007e-15, 2.248710979888696e-16, 1.6558056981263095e-17, 1.2100374177650596e-18, 8.290094933363073e-20, 5.3455361254459156e-21, 3.255363203305341e-22], [8.779948681530555e-08, 9.624377826514646e-08, 5.275010817680506e-08, 1.9274485151644782e-08, 5.282061838846585e-09, 1.1580149425477563e-09, 2.115648913999191e-10, 3.3130366922492974e-11, 4.539593287485352e-12, 5.529108624186474e-13, 6.060881717333075e-14, 6.039817411372157e-15, 5.517257453953769e-16, 4.652223643902344e-17, 3.049224468640421e-18, 2.0955687097406235e-19, 1.4356963915398495e-20, 9.257513922141832e-22, 5.637707700219401e-23], [1.419161625033466e-08, 1.5556523359805757e-08, 8.526351571776585e-09, 3.115463502313232e-09, 8.537748607248155e-10, 1.871776735023722e-10, 3.4196643507806724e-11, 5.355082024406991e-12, 7.337647201071861e-13, 8.937066792421343e-14, 9.796607086325939e-15, 9.762559444634611e-16, 8.917910956076452e-17, 7.519699153126068e-18, 5.887800911610062e-19, 3.601792629720845e-20, 2.3206117689029526e-21, 1.4963536779154028e-22, 9.11260271730007e-24], [2.1505176784991227e-09, 2.3573480223197224e-09, 1.2920353443020933e-09, 4.72099810216148e-10, 1.29376238693288e-10, 2.8363851501247857e-11, 5.181966952293851e-12, 8.114790000066785e-13, 1.1119057721225044e-13, 1.3542728179798638e-14, 1.484522717978433e-15, 1.4793633299230611e-16, 1.3513700503190517e-17, 1.1394929006349886e-18, 8.922042228701118e-20, 6.52009167007032e-21, 3.739302214907148e-22, 2.267490172282788e-23, 1.3808725443961196e-24], [3.0670809343199055e-10, 3.362063584550302e-10, 1.8427083909126865e-10, 6.733115200524887e-11, 1.8451715092486124e-11, 4.0452691476627544e-12, 7.39055167997903e-13, 1.157336112325515e-13, 1.585806537901743e-14, 1.9314718411394945e-15, 2.1172350129454077e-16, 2.109876663420732e-17, 1.9273318968654954e-18, 1.6251514624932605e-19, 1.2724668989442788e-20, 9.298993005836324e-22, 6.370838923762112e-23, 3.438781257746385e-24, 1.969408527066374e-25], [4.131272782963309e-11, 4.5286062151224605e-11, 2.4820769928602306e-11, 9.069319058791975e-12, 2.4853947448075507e-12, 5.4488651220435e-13, 9.954867726159754e-14, 1.5588995804087464e-14, 2.136037336273114e-15, 2.6016388935393343e-16, 2.8518567235193826e-17, 2.8419452312015045e-18, 2.59606250365318e-19, 2.189033856284648e-20, 1.713977550447618e-21, 1.2525485155642395e-22, 8.58134298181401e-24, 5.5333357799703205e-25, 2.8207939785532225e-26]] |
| Legacy trial inputs | {"lambda_home": 2.4245499771863264, "lambda_away": 1.0961770023508708, "rho": -0.061606117514439646, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7056 |
| Legacy p draw | 0.1682 |
| Legacy p away | 0.1261 |
| Legacy p over 1 5 | 0.8748 |
| Legacy p under 3 5 | 0.5257 |
| Legacy p btts yes | 0.6041 |
| Legacy p over 2 5 | 0.6926 |
| Legacy goal margin distribution | {"-1": 0.07944183406298146, "-10": 2.1782480631706704e-08, "-11": 2.128528959373443e-09, "-12": 1.9122549472151792e-10, "-13": 1.589513750468906e-11, "-14": 1.2291748067466398e-12, "-15": 8.88500473642564e-14, "-16": 6.026052421663077e-15, "-17": 3.8183608910787796e-16, "-18": 2.0261656023010796e-17, "-2": 0.03340981009693838, "-3": 0.010196160556270891, "-4": 0.00248895006048264, "-5": 0.0005035971556039484, "-6": 8.675590945138633e-05, "-7": 1.2990519482132567e-05, "-8": 1.718338010318569e-06, "-9": 2.0342109958420659e-07, "0": 0.1682362427763183, "1": 0.22946416675557094, "10": 7.75376503333844e-05, "11": 1.6758506694028167e-05, "12": 3.3300595611578614e-06, "13": 6.122389445801056e-07, "14": 1.0471786206616344e-07, "15": 1.6742304430804444e-08, "16": 2.511544806882755e-09, "17": 3.5199415558321516e-10, "18": 4.131272782963309e-11, "2": 0.20762310074350873, "3": 0.14014860699420112, "4": 0.07566913282301739, "5": 0.03386384727904942, "6": 0.012903352135808992, "7": 0.00427346799190292, "8": 0.0012502964213289473, "9": 0.00032737901896637755} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6614 |
| Legacy raw p draw | 0.1884 |
| Legacy raw p away | 0.1502 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.4245 |
| Legacy lambda away | 1.0962 |
| Legacy model home team | Paris SG |
| Legacy model away team | Lyon |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 87.9% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-26T11:44:03Z |
| Market reference home draw last update utc | 2026-10-26T11:44:10Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 29.5% |
| Market draw away odds | 3.45 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-26T11:44:03Z |
| Market reference draw away last update utc | 2026-10-26T11:44:10Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.6% |
| Market home away odds | 1.17 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-26T11:44:03Z |
| Market reference home away last update utc | 2026-10-26T11:44:10Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.28 |
| Market reference dc home draw odds | 1.10 |
| Market reference dc home away odds | 1.17 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:44:03Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.55, "price": 1.49, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:44:03Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.49, "price": 2.55, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:44:03Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.02, "price": 1.81, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:44:03Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.81, "price": 2.02, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:44:03Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.59, "price": 2.31, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T11:44:03Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.31, "price": 1.59, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 88.7% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market reference over 1 5 last update utc | 2026-10-26T11:44:10Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.90 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-26T11:44:30Z |
| Market reference under 3 5 odds | 1.90 |
| Market reference under 3 5 opposite odds | 2.01 |
| Market reference under 3 5 last update utc | 2026-10-26T11:44:30Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.3% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-26T11:44:03Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.28 |
| Market reference btts yes last update utc | 2026-10-26T11:44:10Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015553586640413052, "mu": 9.539580188438363, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,650.2101 |
| Elo away rating | 1,562.7526 |
| Elo rating diff | 147.4576 |
| Elo home expectancy | 0.7003 |

</details>


---
