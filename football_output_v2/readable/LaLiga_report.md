# La Liga — football model report

Fixtures in this report: **9**.

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
| Training sha256 | 0bc30dcf0bcd145287e49f4b5ad93c0c5d833f1685e3b08d1a34845052679fae |
| Training as of utc | 2026-10-30T07:00:18.879025+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 99, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 99, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 89, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-10-30T07:00:18.879025+00:00', 'observations': 410, 'observations_sha256': '8165964735e76ea42f02a3748dfeaa705e175692adb5582ba6a727ccb63ed467', 'eligible_training_matches': 146, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 158, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 20, 'retrospective_eligible_training_matches': 146, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '26c05c669722a7f57680f57ff47ece9746f1a55f42adc6192265e13cc0c4195e', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 86, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-20T00:00:00+00:00', 'audit_origin_utc': '2026-09-18T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 16, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8175310728786089, 'audit_candidate_poisson_score': 0.8092170230971366, 'audit_gain': 0.008314049781472321, 'audit_gain_lower95': -0.030066464950571126, 'audit_baseline_briers': [0.5520932991942327, 0.18075667919310287, 0.22581865901120918, 0.25218525802844377], 'audit_candidate_briers': [0.5294982728718252, 0.18982470750712058, 0.23342014665888827, 0.2547217781537697], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1620, 'tuning_matches': 230, 'audit_matches': 132, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8318743559297036, 'audit_candidate_poisson_score': 0.8321637367930856, 'audit_gain': -0.0002893808633820383, 'audit_gain_lower95': -0.00911269101088794, 'audit_baseline_briers': [0.5680229999189184, 0.18323019113367303, 0.19905730595023735, 0.24590362970652666], 'audit_candidate_briers': [0.5724719440820307, 0.18024247132351665, 0.20128393456909932, 0.24347527965161764], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1834.500 |
| Base scoring parameter | 0.091 |
| Home-advantage parameter | 0.288 |
| Dixon-Coles low-score adjustment | -0.033 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1999, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 8.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261030T070018879025Z_9462347a3d68b1d5ac19be044fb8ad3a4305d977ccddb208e36eebab9b97b2fa.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 4, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 4, 'ANCHORED_MAIN': 1} |
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

## 2026-10-30 — Villarreal vs Espanyol

The model's most likely 1X2 outcome is **Villarreal win** at **68.6%**. Expected goals are 2.16 for Villarreal and 0.95 for Espanyol (3.12 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 65.6%; Under 3.5 goals: 56.5%; Double Chance 1X: 86.8%; Double Chance X2: 31.4%; Double Chance 12 (either team wins): 81.8%; Under 4.5 goals: 75.0%; BTTS Yes (both teams score): 57.8%; BTTS No (at least one team does not score): 42.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 68.6% | 1.46 |
| Draw | 18.2% | 5.50 |
| Espanyol win | 13.2% | 7.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.16 |
| Espanyol expected goals | 0.95 |
| Expected total goals | 3.12 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.5% |
| Under 3.5 | 56.5% |
| Over 4.5 | 25.0% |
| Under 4.5 | 75.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.06% |
| 2 | 2-0 | 9.82% |
| 3 | 1-1 | 8.28% |
| 4 | 1-0 | 8.15% |
| 5 | 3-1 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 68.6% | 70.2% | 1.40 | -4.0% |
| Draw | 18.2% | 17.3% | 5.30 | -3.7% |
| Espanyol win | 13.2% | 12.4% | 7.28 | -3.6% |

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
| Market best home last update utc | 2026-10-30T07:00:40Z |
| Market best draw last update utc | 2026-10-30T07:00:40Z |
| Market best away last update utc | 2026-10-30T07:00:40Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Villarreal |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1641 |
| Dc lambda away | 0.9516 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:00:18.879025+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 57.8% |
| P btts no | 42.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.61 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.80 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.90 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.99 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.0859989188503303, "-10": 1.3536808802983565e-08, "-11": 1.2386920632947425e-09, "-12": 1.0417876786393791e-10, "-13": 8.104901461019539e-12, "-14": 5.864982801637835e-13, "-15": 3.966588006122119e-14, "-16": 2.5170597728401213e-15, "-17": 1.4943109002471856e-16, "-18": 7.509261698154655e-18, "-2": 0.033865979851656895, "-3": 0.009808922100814785, "-4": 0.0022613382688509926, "-5": 0.0004308387491177793, "-6": 6.975780425250775e-05, "-7": 9.80463215019438e-06, "-8": 1.216292693980989e-06, "-9": 1.349490720680338e-07, "0": 0.18169585382036713, "1": 0.23103079246031374, "10": 5.82510451808377e-05, "11": 1.2121986836270152e-05, "12": 2.3185298713567258e-06, "13": 4.1020811144530914e-07, "14": 6.750660597060638e-08, "15": 1.0382923417649458e-08, "16": 1.4983701449124303e-09, "17": 2.0229706059705514e-10, "18": 2.311899087866362e-11, "2": 0.20368866717464523, "3": 0.13416756321821288, "4": 0.07034201499019938, "5": 0.030478041390422, "6": 0.011222461546951836, "7": 0.0035871509649635083, "8": 0.0010119975793549537, "9": 0.00025534908390094537} |
| Raw goal margin distribution | {"-1": 0.1004335134725657, "-10": 8.959409151364592e-09, "-11": 7.63302444203592e-10, "-12": 5.974886494483585e-11, "-13": 4.325074666868268e-12, "-14": 2.911429777802274e-13, "-15": 1.8309071724515048e-14, "-16": 1.0741904918713979e-15, "-17": 5.363170628864363e-17, "-2": 0.03794226631566478, "-3": 0.010406594900919292, "-4": 0.0022575379432769175, "-5": 0.0004032200317022527, "-6": 6.105922013345576e-05, "-7": 8.013751552892913e-06, "-8": 9.27280765427889e-07, "-9": 9.588849793037131e-08, "0": 0.2009174035418722, "1": 0.23219789699449217, "10": 3.315199194911568e-05, "11": 6.423177699174675e-06, "12": 1.143420486646541e-06, "13": 1.8823177823331327e-07, "14": 2.881566729034656e-08, "15": 4.121086338649359e-09, "16": 5.498569478233548e-10, "17": 6.243283456706492e-11, "2": 0.19623176930833627, "3": 0.12239895965965476, "4": 0.060384734575197524, "5": 0.02452772275315052, "6": 0.008446745477945527, "7": 0.002521140533358246, "8": 0.000663430537170449, "9": 0.00015601765569095462} |
| Unadjusted home-win probability | 64.8% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 15.2% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 54.6% |
| P home draw | 86.8% |
| P draw away | 31.4% |
| P home away | 81.8% |
| Raw p home draw | 84.8% |
| Raw p draw away | 35.2% |
| Raw p home away | 79.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0766 |
| Totals anchor target over 2 5 | 0.6556 |
| Totals anchor reference over odds | 1.48 |
| Totals anchor reference under odds | 2.69 |
| Totals anchor reference last update utc | 2026-10-30T07:01:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6116 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:26Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 6.17, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:26Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.15, "price": 6.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.99, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.99, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.40 |
| Reference draw odds | 5.30 |
| Reference away odds | 7.28 |
| Market reference 1x2 last update utc | 2026-10-30T07:00:40Z |
| Market reference home last update utc | 2026-10-30T07:00:40Z |
| Market reference draw last update utc | 2026-10-30T07:00:40Z |
| Market reference away last update utc | 2026-10-30T07:00:40Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-30T07:00:42Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:00:42Z |
| Home probability edge | -1.6% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | -0.0547 |
| Raw ev home | -0.0934 |
| Raw edge prob draw | 0.0275 |
| Raw ev draw | 0.0649 |
| Raw edge prob away | 0.0272 |
| Raw ev away | 0.1030 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.04010941000959987, 0.03430245068714693, 0.017656291493871636, 0.0057630473051790854, 0.0014108022451908902, 0.0002762931303023632, 4.509130302309518e-05, 6.307666083571203e-06, 7.720628515941146e-07, 8.400093035491462e-08, 8.225419287211955e-09, 7.322161591714911e-10, 5.974918861622939e-11, 4.50051909555972e-12, 3.147810082466087e-13, 2.0549024600401874e-14, 1.2576076729700266e-15, 7.243862632926457e-17], [0.09139189568694668, 0.0853798443484388, 0.03935521389848192, 0.012845617069763225, 0.0031446254807934856, 0.0006158470619668222, 0.00010050682931073706, 1.4059551973601392e-05, 1.7208992430887642e-06, 1.8723493452385464e-07, 1.833415219528311e-08, 1.6320824548077331e-09, 1.3317870851127576e-10, 1.003148887304176e-11, 7.01635103556427e-13, 4.5803007887283703e-14, 2.803160504417719e-15, 1.6146299095084123e-16], [0.10408621818369361, 0.101921821932656, 0.04558957002448026, 0.014316200194530995, 0.0035046263387246246, 0.0006863500430106836, 0.00011201298322343573, 1.566910796159993e-05, 1.9179100501654396e-06, 2.0866983590557977e-07, 2.0433070034642643e-08, 1.8189253992326715e-09, 1.4842518209455362e-10, 1.1179906903321935e-11, 7.81959212350197e-13, 5.104659642778238e-14, 3.124070003075863e-15, 1.7994748636101115e-16], [0.07733476349257008, 0.07572664404026375, 0.037075982123820385, 0.011056043094004117, 0.002603893712006925, 0.000509949531989644, 8.322425117217591e-05, 1.1641952022998135e-05, 1.4249832755745546e-06, 1.5503908864583522e-07, 1.5181516497865854e-08, 1.3514389129984199e-09, 1.1027806134109491e-10, 8.306531559360687e-12, 5.809859537908799e-13, 3.79269852505956e-14, 2.3211450952682805e-15, 1.3369874073291503e-16], [0.04309407442801607, 0.04219796488766055, 0.02066024464262069, 0.006743543356957077, 0.0015081914562332316, 0.0002841646123118357, 4.63759364127909e-05, 6.487368995635121e-06, 7.940586168882223e-07, 8.639408363868993e-08, 8.45975822958378e-09, 7.530767079576875e-10, 6.145141936933763e-11, 4.628737104654688e-12, 3.23748994676909e-13, 2.113445818420925e-14, 1.2934364181940746e-15, 7.450237414419469e-17], [0.019211016282330108, 0.01881153734702365, 0.009210182640986863, 0.003006221225321849, 0.0007359272672311998, 0.0001316719306863627, 2.0674045825549185e-05, 2.892020609766404e-06, 3.539853963831019e-07, 3.851383675155244e-08, 3.77129698804839e-09, 3.3571596769260816e-10, 2.7394583449021765e-11, 2.063456404724098e-12, 1.4432488203256749e-13, 9.421583493416742e-15, 5.766042877099344e-16, 3.32126015410111e-17], [0.007136772891603918, 0.006988368955322618, 0.0034215254848008227, 0.0011167924607286335, 0.00027339239599721713, 5.3541480493400996e-05, 7.983024073036012e-06, 1.074367643357039e-06, 1.3150336993125346e-07, 1.4307650466828909e-08, 1.40101334124874e-09, 1.247163909652665e-10, 1.0176917122056936e-11, 7.665612019592363e-13, 5.3615794736551567e-14, 3.5000595847521722e-15, 2.1420490146040963e-16, 1.2338274605261073e-17], [0.0022725142948251385, 0.0022252590336966347, 0.0010894932054606723, 0.0003556126655430658, 8.705449051504606e-05, 1.704885129951363e-05, 2.7823888321101837e-06, 3.555888175340414e-07, 4.1873728157726165e-08, 4.555888313257366e-09, 4.4611519710457816e-10, 3.971259637545692e-11, 3.2405668484047135e-12, 2.4409089595104136e-13, 1.7072514681049487e-14, 1.1145002874403483e-15, 6.820781717225017e-17, 3.928793285116339e-18], [0.0006331686794990569, 0.0006200024031168789, 0.0003035549548777683, 9.908091771645737e-05, 2.4255150750598982e-05, 4.75015655077296e-06, 7.752300906057385e-07, 1.084442502575964e-07, 1.2126762078825498e-08, 1.2693630987576756e-09, 1.2429676279633787e-10, 1.1064736650407686e-11, 9.028878000482337e-13, 6.80086856302722e-14, 4.756749649911503e-15, 3.10522436275466e-16, 1.9004084431420406e-17, 1.094641675973829e-18], [0.00015681214712962396, 0.00015355135401707635, 7.517918334791838e-05, 2.453862919906862e-05, 6.007091619192768e-06, 1.1764357145995973e-06, 1.9199543338681494e-07, 2.685757567826963e-08, 3.287386521470659e-09, 3.26765783543707e-10, 3.0783648791308124e-11, 2.7403204987129454e-12, 2.2361146267487954e-13, 1.6843202076236734e-14, 1.1780685781091622e-15, 7.690476730908826e-17, 4.7065993319212044e-18, 2.71101709710014e-19], [3.495284156533442e-05, 3.422602296660688e-05, 1.6757159012680883e-05, 5.469568744037076e-06, 1.338958272540787e-06, 2.622231242724475e-07, 4.279506458699143e-08, 5.98645324800986e-09, 7.327461701930418e-10, 7.972325035860504e-11, 7.132032445817728e-12, 6.108071981858428e-13, 4.984215936158961e-14, 3.754286797291084e-15, 2.625870834464805e-16, 1.7141785228866774e-17, 1.049083401837259e-18, 6.042755794774332e-20], [7.08259796458871e-06, 6.935320556016632e-06, 3.395552836345409e-06, 1.1083149386090375e-06, 2.71317086424583e-07, 5.313504948570723e-08, 8.671690877312738e-09, 1.2130527788479234e-09, 1.4847852996068013e-10, 1.615455869774718e-11, 1.5818636546931174e-12, 1.2864848493648286e-13, 1.0099664594801114e-14, 7.607422698172752e-16, 5.320879961272856e-17, 3.473490787421394e-18, 2.1257888153807616e-19, 1.2244615309051721e-20], [1.3155705146712596e-06, 1.2882141946932878e-06, 6.307133646211118e-07, 2.0586604823452054e-07, 5.039630384377219e-08, 9.869669964113796e-09, 1.6107395743164794e-09, 2.2532077587507617e-10, 2.7579424535266142e-11, 3.0006589681554032e-12, 2.938262474799713e-13, 2.615603155063975e-14, 1.9499295462102726e-15, 1.4130550744790327e-16, 9.883368820528857e-18, 6.451900963122364e-19, 3.94858652138005e-20, 2.2743991603956855e-21], [2.2556596249337355e-07, 2.2087548442527106e-07, 1.0814127069710556e-07, 3.529751753848833e-08, 8.6408829141854e-09, 1.6922404235424632e-09, 2.761752550357618e-10, 3.8633199143046746e-11, 4.728731277369192e-12, 5.144889770013433e-13, 5.037905576288897e-14, 4.484678218256813e-15, 3.659518864605723e-16, 2.5183086162780816e-17, 1.6945892111580732e-18, 1.1062343176810133e-19, 6.770193685938731e-21, 3.899654408391564e-22], [3.591272147634362e-08, 3.516594288178678e-08, 1.721734649906287e-08, 5.6197748195423084e-09, 1.3757289352375264e-09, 2.694243330417176e-10, 4.39703087430527e-11, 6.150854079347691e-12, 7.528689498337908e-13, 8.191262160948149e-14, 8.020930896907667e-15, 7.140128678235896e-16, 5.826379134035854e-17, 4.3886337468315995e-18, 2.804333216508603e-19, 1.7612535375153664e-20, 1.0778934795676917e-21, 6.208702814666729e-23], [5.336540937333571e-09, 5.2255714987294215e-09, 2.558454793937843e-09, 8.350845369053689e-10, 2.0442989224321124e-10, 4.0035784637987444e-11, 6.533878330247538e-12, 9.140015917653613e-13, 1.1187445022460643e-13, 1.2172011491561788e-14, 1.1918903476882765e-15, 1.0610053324511995e-16, 8.65785423298811e-18, 6.521400408030261e-19, 4.5612804923879715e-20, 2.720344050186705e-21, 1.601722855670242e-22, 9.225977697076643e-24], [7.434343946875239e-10, 7.279752239650911e-10, 3.5641875765632906e-10, 1.163357640272043e-10, 2.8479161872935076e-11, 5.577391735151566e-12, 9.102356635975862e-13, 1.2732971190454881e-13, 1.558524803995727e-14, 1.695684920554595e-15, 1.660424401448097e-16, 1.47808827169836e-17, 1.2061270955433506e-18, 9.084973622035759e-20, 6.3543273473936814e-21, 4.1481291933058007e-22, 2.3193196356634908e-23, 1.285272468659044e-24], [9.747573426653869e-11, 9.54487981601533e-11, 4.6732005348664064e-11, 1.52534159046769e-11, 3.734058088645152e-12, 7.312822201406641e-13, 1.1934595748970908e-13, 1.6694892314014457e-14, 2.043466790448272e-15, 2.2233048927636647e-16, 2.177072904909916e-17, 1.9380020701774866e-18, 1.5814189536693596e-19, 1.1911803932239194e-20, 8.331504815801345e-22, 5.438838206024871e-23, 3.3285884819105454e-24, 1.7516183979083174e-25]] |
| Legacy trial inputs | {"lambda_home": 2.228962628541889, "lambda_away": 0.9792057364672636, "rho": -0.021895783674930586, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6785 |
| Legacy p draw | 0.1838 |
| Legacy p away | 0.1377 |
| Legacy p over 1 5 | 0.8342 |
| Legacy p under 3 5 | 0.5973 |
| Legacy p btts yes | 0.5551 |
| Legacy p over 2 5 | 0.6271 |
| Legacy goal margin distribution | {"-1": 0.09088371469244347, "-10": 1.0014566844385468e-08, "-11": 8.771774839406263e-10, "-12": 7.060189033589169e-11, "-13": 5.255596443013342e-12, "-14": 3.6384178487770116e-13, "-15": 2.3532132591180604e-14, "-16": 1.4190706639208677e-15, "-17": 7.243862632926457e-17, "-2": 0.03456588857771763, "-3": 0.009684103199605266, "-4": 0.0021511382565037214, "-5": 0.0003939843442570634, "-6": 6.123261003554786e-05, "-7": 8.253197934303825e-06, "-8": 9.811458646909546e-07, "-9": 1.0426906264212024e-07, "0": 0.18378308193712373, "1": 0.23792560604990529, "10": 4.2555589695161085e-05, "11": 8.484783331428582e-06, "12": 1.554527640576592e-06, "13": 2.63410429991214e-07, "14": 4.150996514863405e-08, "15": 6.1112481666473264e-09, "16": 8.388831928476771e-10, "17": 9.747573426653869e-11, "2": 0.203770572176062, "3": 0.12995170626242886, "4": 0.06570822554806821, "5": 0.027394237577396827, "6": 0.0096915192528374, "7": 0.0029734469192300625, "8": 0.0008046376409118084, "9": 0.0001946485059513095} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6547 |
| Legacy raw p draw | 0.1941 |
| Legacy raw p away | 0.1512 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2290 |
| Legacy lambda away | 0.9792 |
| Legacy model home team | Villarreal |
| Legacy model away team | Espanol |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 85.6% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T07:00:26Z |
| Market reference home draw last update utc | 2026-10-30T07:01:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.9% |
| Market draw away odds | 3.13 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T07:00:26Z |
| Market reference draw away last update utc | 2026-10-30T07:01:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.5% |
| Market home away odds | 1.18 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T07:00:26Z |
| Market reference home away last update utc | 2026-10-30T07:01:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.80 |
| Market reference dc home draw odds | 1.11 |
| Market reference dc home away odds | 1.18 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:26Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.08, "price": 1.74, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:26Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.74, "price": 2.08, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:26Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.67, "price": 2.19, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:26Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.19, "price": 1.67, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 84.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-30T07:01:04Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.4% |
| Market under 3 5 odds | 1.69 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:01:05Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.24 |
| Market reference under 3 5 last update utc | 2026-10-30T07:01:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T07:00:26Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.15 |
| Market reference btts yes last update utc | 2026-10-30T07:01:04Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 10.163900130311859, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,563.5990 |
| Elo away rating | 1,432.0064 |
| Elo rating diff | 191.5927 |
| Elo home expectancy | 0.7508 |

</details>


---

## 2026-10-31 — Barcelona vs Alavés

The model's most likely 1X2 outcome is **Barcelona win** at **87.5%**. Expected goals are 2.93 for Barcelona and 0.72 for Alavés (3.65 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 72.7%; Under 3.5 goals: 49.0%; Double Chance 1X: 95.8%; Double Chance X2: 12.5%; Double Chance 12 (either team wins): 91.7%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 47.3%; BTTS No (at least one team does not score): 52.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 87.5% | 1.14 |
| Draw | 8.3% | 12.08 |
| Alavés win | 4.2% | 23.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.93 |
| Alavés expected goals | 0.72 |
| Expected total goals | 3.65 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 89.0% |
| Under 1.5 | 11.0% |
| Over 2.5 | 72.7% |
| Under 2.5 | 27.3% |
| Over 3.5 | 51.0% |
| Under 3.5 | 49.0% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.92% |
| 2 | 3-0 | 11.63% |
| 3 | 2-1 | 8.62% |
| 4 | 4-0 | 8.51% |
| 5 | 3-1 | 8.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 87.5% | 90.0% | 1.10 | -3.8% |
| Draw | 8.3% | 6.6% | 11.51 | -4.7% |
| Alavés win | 4.2% | 3.4% | 20.85 | -11.6% |

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
| Market best home last update utc | 2026-10-30T07:00:40Z |
| Market best draw last update utc | 2026-10-30T07:00:40Z |
| Market best away last update utc | 2026-10-30T07:00:40Z |
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
| Dc lambda away | 0.7229 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:00:18.879025+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 47.3% |
| P btts no | 52.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 52.82 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.08 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.67 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.46 |
| Goal margin distribution | {"-1": 0.031202567323786574, "-10": 2.328994510114249e-10, "-11": 1.5067438338141754e-11, "-12": 8.956800532101285e-13, "-13": 4.924007538639119e-14, "-14": 2.5174112159520622e-15, "-15": 1.2027071486683535e-16, "-16": 5.3923424881810366e-18, "-17": 2.2773616379667374e-19, "-18": 9.088646993420967e-21, "-19": 3.422533688813479e-22, "-2": 0.008991988023621018, "-20": 1.1187027836853129e-23, "-3": 0.0018671830461516954, "-4": 0.0003070092561318765, "-5": 4.158968458352859e-05, "-6": 4.778632064270118e-06, "-7": 4.7601191786360616e-07, "-8": 4.1812566319527376e-08, "-9": 3.2827386951181415e-09, "0": 0.08280757002021988, "1": 0.20203834344321245, "10": 0.0004290490198830997, "11": 0.00011241063320483296, "12": 2.7061408422225653e-05, "13": 6.024842864109193e-06, "14": 1.247414247264428e-06, "15": 2.413492488533901e-07, "16": 4.382208624267597e-08, "17": 7.495094342532893e-09, "18": 1.2113617621932572e-09, "19": 1.8473614584326314e-10, "2": 0.22895914441881252, "20": 2.44539144026543e-11, "3": 0.19253899077774705, "4": 0.12820730969266309, "5": 0.07033580563657062, "6": 0.03272833820768037, "7": 0.013202850624891281, "8": 0.00469662871927112, "9": 0.0014932937308525282} |
| Raw goal margin distribution | {"-1": 0.04524567183404049, "-10": 3.3771875312189276e-10, "-11": 2.1848726848431343e-11, "-12": 1.2987920300054154e-12, "-13": 7.140118532226292e-14, "-14": 3.65040352501601e-15, "-15": 1.7440004983057624e-16, "-16": 7.819233465798814e-18, "-17": 3.3023166411157823e-19, "-18": 1.3179105905374592e-20, "-19": 4.962887653380774e-22, "-2": 0.013038944360909275, "-20": 1.6221889213541395e-23, "-3": 0.0027075320592565726, "-4": 0.0004451826001627245, "-5": 6.0307640740609046e-05, "-6": 6.929315012831158e-06, "-7": 6.902470172167644e-07, "-8": 6.063083318115909e-08, "-9": 4.760176179573323e-09, "0": 0.12145953645623929, "1": 0.18870233818783294, "10": 0.0004007286531325939, "11": 0.00010499071097803271, "12": 2.5275157957158815e-05, "13": 5.627159262426034e-06, "14": 1.165075802622461e-06, "15": 2.254184369281014e-07, "16": 4.0929508712716754e-08, "17": 7.000363412561284e-09, "18": 1.1314030446970623e-09, "19": 1.7254221191053526e-10, "2": 0.21384616981607477, "20": 2.2839777573819824e-11, "3": 0.17983001212984395, "4": 0.11974469152474093, "5": 0.06569312911475333, "6": 0.030568029016370145, "7": 0.012331366121906185, "8": 0.004386616945192352, "9": 0.0013947254457286104} |
| Unadjusted home-win probability | 81.7% |
| Unadjusted draw probability | 12.1% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 88.1% |
| Raw p under 3 5 | 50.5% |
| Raw p btts yes | 48.9% |
| P home draw | 95.8% |
| P draw away | 12.5% |
| P home away | 91.7% |
| Raw p home draw | 93.8% |
| Raw p draw away | 18.3% |
| Raw p home away | 87.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7273 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": -2.5, "market_key": "spreads", "opposite_price": 2.09, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.86, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:27Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 18.1, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:27Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.03, "price": 18.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.18, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.10 |
| Reference draw odds | 11.51 |
| Reference away odds | 20.85 |
| Market reference 1x2 last update utc | 2026-10-30T07:00:40Z |
| Market reference home last update utc | 2026-10-30T07:00:40Z |
| Market reference draw last update utc | 2026-10-30T07:00:40Z |
| Market reference away last update utc | 2026-10-30T07:00:40Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.21 |
| Reference Under 2.5 odds | 4.48 |
| Market reference over 2 5 last update utc | 2026-10-30T07:00:42Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:00:42Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -8.3% |
| Under 2.5 probability edge | +8.3% |
| Raw edge prob home | -0.0825 |
| Raw ev home | -0.1013 |
| Raw edge prob draw | 0.0552 |
| Raw ev draw | 0.3980 |
| Raw edge prob away | 0.0273 |
| Raw ev away | 0.2824 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.027439361015821825, 0.016474834826815634, 0.005659523083477721, 0.0012194846845250407, 0.00019707617680710617, 2.5478971541185127e-05, 2.7450383286387845e-06, 2.534942672856697e-07, 2.0483111298210265e-08, 1.4711981999868469e-09, 9.510184761092833e-11, 5.588741710416774e-12, 3.0105827033006743e-13, 1.4970109579439165e-14, 6.912174812706339e-16, 2.97879916612176e-17, 1.2034803687676348e-18, 4.5762301549335493e-20, 1.6434372368156858e-21, 5.591357891860838e-23], [0.09921247582771281, 0.04714813126349989, 0.0152839985103818, 0.003293316738317976, 0.0005322201090662639, 6.880801744910256e-05, 7.413197385542794e-06, 6.845817123522918e-07, 5.5316293961903176e-08, 3.973089386757666e-09, 2.5683020915020307e-10, 1.5092847704126667e-11, 8.130321384669347e-13, 4.042798821341732e-14, 1.8666885527743806e-15, 8.04448737927137e-17, 3.250095792915353e-18, 1.2358478592544108e-19, 4.438234796272265e-21, 1.50999129131035e-22], [0.1358890150890716, 0.08784198080935385, 0.0201359816118033, 0.004446933723939952, 0.0007186516632392177, 9.291080014008646e-05, 1.000996869582327e-05, 9.243840618278347e-07, 7.469305646811207e-08, 5.364824153301554e-09, 3.4679534619555234e-10, 2.0379726208797565e-11, 1.0978294292586643e-12, 5.4589521282764095e-14, 2.520571489781672e-15, 1.0862393465671328e-16, 4.3885728995906824e-18, 1.668753405657641e-19, 5.992905498785129e-21, 2.0389266292112422e-22], [0.12232641476228238, 0.07907478445540393, 0.025557936725357857, 0.0039057569755427397, 0.0006469255912214974, 8.36377029179437e-05, 9.01090924560844e-06, 8.321245692499598e-07, 6.723820758721255e-08, 4.829380094287354e-09, 3.1218293346625406e-10, 1.8345698063416288e-11, 9.88258970114025e-13, 4.914113490139554e-14, 2.2690021948787627e-15, 9.778256524428054e-17, 3.950565013499868e-18, 1.5022010506341838e-19, 5.3947748697349175e-21, 1.8354285984873186e-22], [0.08258808708039568, 0.05338695814111317, 0.017255317324316177, 0.003718086293358259, 0.00042614770605325176, 5.646759046453491e-05, 6.083671780097932e-06, 5.61804876898447e-07, 4.539555053692822e-08, 3.2605326048868475e-09, 2.1076879710917562e-10, 1.238600928635441e-11, 6.672182622238115e-13, 3.317739947134704e-14, 1.5319058538617124e-15, 6.601742582771364e-17, 2.66720485502443e-18, 1.014203771304276e-19, 3.642256152006302e-21, 1.2391807379975483e-22], [0.04460715792809857, 0.02883515719141431, 0.009319875204712627, 0.002008198377529679, 0.00032453712911361803, 2.975740575960867e-05, 3.285889254383307e-06, 3.034398755862906e-07, 2.4518869047814676e-08, 1.7610662503215518e-09, 1.1383962689209822e-10, 6.6898833944109746e-12, 3.603753452547754e-13, 1.791964858589507e-14, 8.274070603871494e-16, 3.565707651076458e-17, 1.4406003626025136e-18, 5.477878153758815e-20, 1.967241295091095e-21, 6.693015038295465e-23], [0.02007753790290753, 0.012978611243964436, 0.004194845768354067, 0.0009038836122758609, 0.00014607311501849832, 1.88850463855476e-05, 1.4430038395982433e-06, 1.3657730925510653e-07, 1.1035863872731362e-08, 7.926502389449444e-10, 5.123884887405515e-11, 3.011094937584234e-12, 1.6220378050735318e-13, 8.065576028627919e-15, 3.724132490761536e-16, 1.604913512548155e-17, 6.484095765463443e-19, 2.465575288093452e-20, 8.854489615774535e-22, 3.012504480395516e-23], [0.00774585861423118, 0.005007112335734216, 0.0016183598998695517, 0.0003487157986336298, 5.6354603923310947e-05, 7.285798683735299e-06, 7.849530586142776e-07, 5.140984887621152e-08, 4.257605771059199e-09, 3.058022707313615e-10, 1.9767806234693454e-11, 1.1616721020946067e-12, 6.257777007218592e-14, 3.1116769328094148e-15, 1.4367600187633584e-16, 6.191711960093915e-18, 2.5015462196259434e-19, 9.512121295285168e-21, 3.416037613607766e-22, 1.1622158998142123e-23], [0.00261478948348041, 0.001690263833892915, 0.0005463139281797142, 0.00011771689213581011, 1.9023769090446165e-05, 2.4594858653868385e-06, 2.649786298602761e-07, 2.4469809008495713e-08, 1.4023010970938316e-09, 1.0323046176749234e-10, 6.673069368835273e-12, 3.921486496317943e-13, 2.1124539348520988e-14, 1.050416813050262e-15, 4.8501078762853603e-17, 2.090152186388751e-18, 8.444534135312672e-20, 3.211031335222792e-21, 1.153160633583508e-22, 3.923322208314742e-24], [0.0007846055416684984, 0.0005071881997892239, 0.00016392942462425242, 3.532266230274575e-05, 5.708358070921461e-06, 7.380044366207633e-07, 7.951068440713198e-08, 7.3425214048514925e-09, 5.93298163131938e-10, 3.0222554923354835e-11, 2.0023513326042074e-12, 1.1766989488170372e-13, 6.338724682333686e-15, 3.1519281295410387e-16, 1.4553452740517864e-17, 6.271805048673737e-19, 2.5339050509550384e-20, 9.635165645280047e-22, 3.460225877684337e-23, 1.17724978084948e-24], [0.00021188905413439376, 0.0001369702636727876, 4.427046316109754e-05, 9.539169821463808e-06, 1.5415881332367896e-06, 1.9930404989240984e-07, 2.147250155381091e-08, 1.982907120598518e-09, 1.602249537243447e-10, 1.1508147374702217e-11, 5.276015904647047e-13, 3.1777704084980964e-14, 1.71182372036507e-15, 8.512036107313334e-17, 3.930277281779414e-18, 1.693751533608559e-19, 6.843014941896406e-21, 2.602054187209883e-22, 9.344619039456927e-24, 3.179257974824648e-25], [5.2020316263858106e-05, 3.362720393514598e-05, 1.0868723276885671e-05, 2.3419361280099752e-06, 3.784711889304309e-07, 4.893060545494222e-08, 5.271656558044525e-09, 4.86818235877186e-10, 3.933640083558008e-11, 2.8253345529750224e-12, 1.8263653130443134e-13, 7.611945082015754e-15, 4.2026527366007364e-16, 2.089767270710301e-17, 9.64911887676574e-19, 4.158284193143228e-20, 1.6800103380987994e-21, 6.388233800340649e-23, 2.294172484669721e-24, 7.805311416882946e-26], [1.1707088279333606e-05, 7.567748013278059e-06, 2.4459886449123966e-06, 5.270489486474356e-07, 8.517433068878252e-08, 1.1011753844723099e-08, 1.186377806515435e-09, 1.0955765886727775e-10, 8.852593568204387e-12, 6.35836984584242e-13, 4.1102056822706407e-14, 2.415397651250083e-15, 9.228010389155854e-17, 4.70298753997869e-18, 2.1715186415843395e-19, 9.35815151387448e-21, 3.780836171497943e-22, 1.4376617141324574e-23, 5.162998177446031e-25, 1.756572746341125e-26], [2.4319950799742825e-06, 1.5721010635297805e-06, 5.0812227670658e-07, 1.0948755313299333e-07, 1.769385762136003e-08, 2.287548409413624e-09, 2.4645453417563666e-10, 2.2759176405039194e-11, 1.839010989683128e-12, 1.3208685040022455e-13, 8.538416862039354e-15, 5.0176739628686e-16, 2.702955911392054e-17, 9.532269024941903e-19, 4.5110470907853814e-20, 1.9440340669142123e-21, 7.854194610886797e-23, 2.9865549246858088e-24, 1.0725456121852765e-25, 3.649051049063842e-27], [4.691284890379551e-07, 3.0325612194761804e-07, 9.801608476954829e-08, 2.11199976483041e-08, 3.4131206759057732e-09, 4.412649259638876e-10, 4.7540738953958776e-11, 4.39021366719098e-12, 3.5474267773739226e-13, 2.5479370850822205e-14, 1.647048809534219e-15, 9.679023712130728e-17, 5.213964588534332e-18, 2.592641655321402e-19, 8.49014563530355e-21, 3.7500148415572417e-22, 1.5150632831273392e-23, 5.761023164822904e-25, 2.068925659479903e-26, 7.038969030676605e-28], [8.44612878962207e-08, 5.459784093401524e-08, 1.764668944143234e-08, 3.802417127552864e-09, 6.144938428774418e-10, 7.94447679499701e-11, 8.559173304148926e-12, 7.904084043818115e-13, 6.386741401038647e-14, 4.587273054465379e-15, 2.9653254264407366e-16, 1.7425989412433226e-17, 9.387154574559832e-19, 4.667758585945067e-20, 2.155252315178576e-21, 6.587301513827908e-23, 2.727700387576729e-24, 1.0372071777153074e-25, 3.724867064022466e-27, 1.2672869025962272e-28], [1.4255907469476133e-08, 9.215367037084043e-09, 2.9785192493009293e-09, 6.417958816511298e-10, 1.0371813623523494e-10, 1.3409187676848745e-11, 1.4446711112087749e-12, 1.3341010250528725e-13, 1.0779943890573017e-14, 7.742688020816432e-16, 5.005062786653951e-17, 2.941268110106983e-18, 1.5844229983921733e-19, 7.878536563738945e-21, 3.637770432332564e-22, 1.5676958155709492e-23, 4.492028444768995e-25, 1.750663519404792e-26, 6.287064941047339e-28, 2.13900655207736e-29], [2.264660459836374e-09, 1.463931875010312e-09, 4.73160673018959e-10, 1.019542080764185e-10, 1.647642302692992e-11, 2.1301525136372417e-12, 2.2949710848134553e-13, 2.11932200551484e-14, 1.712476932142469e-15, 1.2299854955663563e-16, 7.950926881507165e-18, 4.672430432786552e-19, 2.5169776976996614e-20, 1.2515660806214798e-21, 5.778877898656959e-23, 2.4904052822846556e-24, 1.0061617787435264e-25, 2.7134359553917136e-27, 9.987485827120496e-29, 3.397976293120916e-30], [3.397721227676151e-10, 2.1963700500840953e-10, 7.098936424819324e-11, 1.5296420067191325e-11, 2.471994953222116e-12, 3.195915918581412e-13, 3.443196942793375e-14, 3.1796666626745635e-15, 2.569267811858471e-16, 1.845375014107647e-17, 1.1928955145421546e-18, 7.01015288952675e-20, 3.776278477383529e-21, 1.8777528531911984e-22, 8.670181007988265e-24, 3.7364112824872504e-25, 1.5095672374481603e-26, 5.740124469154351e-28, 1.4620071139284107e-29, 5.098060564501326e-31], [4.82937904805184e-11, 3.121828658350338e-11, 1.0090131748955293e-11, 2.1741692632393486e-12, 3.5135903842664073e-13, 4.542541410052232e-14, 4.894016330237732e-15, 4.519445396352298e-16, 3.6518499629558036e-17, 2.6229389734322482e-18, 1.6955318633910004e-19, 9.963938539912305e-21, 5.367444512438195e-22, 2.668959481653354e-23, 1.2323433176839325e-24, 5.310778946655928e-26, 2.1456358246152458e-27, 8.158773185610486e-29, 2.93001689294631e-30, 7.069964034465197e-32]] |
| Legacy trial inputs | {"lambda_home": 2.7005806469809355, "lambda_away": 0.6464244424155682, "rho": -0.021895783674930586, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8521 |
| Legacy p draw | 0.0991 |
| Legacy p away | 0.0488 |
| Legacy p over 1 5 | 0.8569 |
| Legacy p under 3 5 | 0.5585 |
| Legacy p btts yes | 0.4329 |
| Legacy p over 2 5 | 0.6682 |
| Legacy goal margin distribution | {"-1": 0.03691258707225784, "-10": 1.1134323410018361e-10, "-11": 6.458699855388823e-12, "-12": 3.4410733547921843e-13, "-13": 1.694947604962723e-14, "-14": 7.762048572543041e-16, "-15": 3.321048148764226e-17, "-16": 1.3332416030517097e-18, "-17": 5.040442900852888e-20, "-18": 1.7944363659467208e-21, "-19": 5.591357891860838e-23, "-2": 0.009761527648067158, "-3": 0.001854213639539564, "-4": 0.0002767734965600339, "-5": 3.38871686431126e-05, "-6": 3.5093601015985717e-06, "-7": 3.145003229303401e-07, "-8": 2.482202724582809e-08, "-9": 1.7494304154250293e-09, "0": 0.09908663182522805, "1": 0.21667471185914097, "10": 0.00024807522829915286, "11": 6.011793468723489e-05, "12": 1.338111372793315e-05, "13": 2.7535564881536195e-06, "14": 5.268093208497151e-07, "15": 9.416546338542931e-08, "16": 1.579300287799788e-08, "17": 2.494387596593739e-09, "18": 3.7099040935111847e-10, "19": 4.82937904805184e-11, "2": 0.23438094664426679, "3": 0.18599602734374515, "4": 0.11598658958063089, "5": 0.05932775900926819, "6": 0.02566787855735926, "7": 0.009609980776421985, "8": 0.0031686775927798915, "9": 0.000932989721383681} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.8046 |
| Legacy raw p draw | 0.1319 |
| Legacy raw p away | 0.0635 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.7006 |
| Legacy lambda away | 0.6464 |
| Legacy model home team | Barcelona |
| Legacy model away team | Alaves |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 94.9% |
| Market home draw odds | 1.03 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T07:00:27Z |
| Market reference home draw last update utc | 2026-10-30T07:01:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 12.9% |
| Market draw away odds | 7.22 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T07:00:27Z |
| Market reference draw away last update utc | 2026-10-30T07:01:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 92.2% |
| Market home away odds | 1.06 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T07:00:27Z |
| Market reference home away last update utc | 2026-10-30T07:01:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 7.50 |
| Market reference dc home draw odds | 1.02 |
| Market reference dc home away odds | 1.05 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:27Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.39, "price": 1.44, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:27Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.44, "price": 2.39, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:27Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.88, "price": 1.83, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:27Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.83, "price": 1.88, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:27Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.23, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:27Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.23, "price": 1.51, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 94.3% |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 11.00 |
| Market reference over 1 5 last update utc | 2026-10-30T07:01:04Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 38.0% |
| Market under 3 5 odds | 2.43 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:01:05Z |
| Market reference under 3 5 odds | 2.43 |
| Market reference under 3 5 opposite odds | 1.55 |
| Market reference under 3 5 last update utc | 2026-10-30T07:01:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 48.3% |
| Market btts yes odds | 1.93 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T07:00:27Z |
| Market reference btts yes odds | 1.91 |
| Market reference btts yes opposite odds | 1.80 |
| Market reference btts yes last update utc | 2026-10-30T07:01:04Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 10.265510305338314, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,725.4846 |
| Elo away rating | 1,438.3571 |
| Elo rating diff | 347.1275 |
| Elo home expectancy | 0.8806 |

</details>


---

## 2026-10-31 — Levante vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **59.7%**. Expected goals are 1.22 for Levante and 1.87 for Atlético Madrid (3.09 combined). The most likely exact score is 1-2 at 11.0%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 62.2%; Under 3.5 goals: 60.6%; Double Chance 1X: 40.3%; Double Chance X2: 80.2%; Double Chance 12 (either team wins): 79.6%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 60.2%; BTTS No (at least one team does not score): 39.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 19.8% | 5.04 |
| Draw | 20.4% | 4.90 |
| Atlético Madrid win | 59.7% | 1.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.22 |
| Atlético Madrid expected goals | 1.87 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 62.2% |
| Under 2.5 | 37.8% |
| Over 3.5 | 39.4% |
| Under 3.5 | 60.6% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.01% |
| 2 | 1-1 | 9.31% |
| 3 | 0-1 | 8.86% |
| 4 | 0-2 | 8.82% |
| 5 | 1-3 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 19.8% | 17.8% | 5.25 | +4.2% |
| Draw | 20.4% | 19.2% | 4.89 | -0.2% |
| Atlético Madrid win | 59.7% | 63.0% | 1.56 | -6.8% |

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
| Market best home last update utc | 2026-10-30T07:00:40Z |
| Market best draw last update utc | 2026-10-30T07:00:40Z |
| Market best away last update utc | 2026-10-30T07:00:40Z |
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
| Dc lambda away | 1.8698 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:00:18.879025+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.2% |
| P btts no | 39.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.54 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.90 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.65 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.58 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.2522051191190466, "-10": 1.068368620608781e-05, "-11": 1.8228887999886974e-06, "-12": 2.8586864142321895e-07, "-13": 4.1468307583802033e-08, "-14": 5.592694438364201e-09, "-15": 6.989839154241136e-10, "-16": 7.26292580359352e-11, "-2": 0.18284308072354105, "-3": 0.09876099508004373, "-4": 0.04245783471175335, "-5": 0.015084209965410766, "-6": 0.004554157870442694, "-7": 0.0011935721220564432, "-8": 0.0002760919716186466, "-9": 5.7119076095295924e-05, "0": 0.204166331718794, "1": 0.11622624785321342, "10": 1.07729620363773e-07, "11": 1.201029993590781e-08, "12": 1.2306650450945674e-09, "13": 1.1664586012389906e-10, "14": 1.0279069006534772e-11, "15": 8.394204452536377e-13, "16": 5.699065379778927e-14, "2": 0.0554951676499074, "3": 0.01958582030762007, "4": 0.005501660936783094, "5": 0.0012771391542311834, "6": 0.0002519436419982463, "7": 4.314432305572552e-05, "8": 6.5209135369402105e-06, "9": 8.814861819431472e-07} |
| Raw goal margin distribution | {"-1": 0.22343525106537301, "-10": 8.035632948897577e-06, "-11": 1.343016877146553e-06, "-12": 2.062831319635625e-07, "-13": 2.9305808407586172e-08, "-14": 3.8707116307005225e-09, "-15": 4.740445781577527e-10, "-16": 4.847724180764641e-11, "-2": 0.16006051744904426, "-3": 0.0851175550845592, "-4": 0.035958576284035114, "-5": 0.01253982654248896, "-6": 0.003713576968712276, "-7": 0.0009542050250636722, "-8": 0.00021632718574516886, "-9": 4.385289552991275e-05, "0": 0.23265827575796438, "1": 0.14481969128067226, "10": 1.139768895740651e-07, "11": 1.2446804017509896e-08, "12": 1.2491648887626128e-09, "13": 1.1595498634175503e-10, "14": 1.0007053267223647e-11, "15": 8.007819010402425e-13, "16": 5.3507250866848326e-14, "2": 0.06833505661651848, "3": 0.023744233446557735, "4": 0.006554222375697493, "5": 0.0014934472385334263, "6": 0.00028898177593708667, "7": 4.851760968639874e-05, "8": 7.187013630548474e-06, "9": 9.519525759926816e-07} |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 52.2% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 60.0% |
| P home draw | 40.3% |
| P draw away | 80.2% |
| P home away | 79.6% |
| Raw p home draw | 47.8% |
| Raw p draw away | 75.5% |
| Raw p home away | 76.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0216 |
| Totals anchor target over 2 5 | 0.6224 |
| Totals anchor reference over odds | 1.55 |
| Totals anchor reference under odds | 2.46 |
| Totals anchor reference last update utc | 2026-10-30T07:01:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6093 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.51, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.62, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.15, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.15, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.25 |
| Reference draw odds | 4.89 |
| Reference away odds | 1.56 |
| Market reference 1x2 last update utc | 2026-10-30T07:00:40Z |
| Market reference home last update utc | 2026-10-30T07:00:40Z |
| Market reference draw last update utc | 2026-10-30T07:00:40Z |
| Market reference away last update utc | 2026-10-30T07:00:40Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-10-30T07:00:42Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:00:42Z |
| Home probability edge | +2.0% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | 0.0670 |
| Raw ev home | 0.2878 |
| Raw edge prob draw | 0.0407 |
| Raw ev draw | 0.1377 |
| Raw edge prob away | -0.1077 |
| Raw ev away | -0.1856 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.03648946710374628, 0.07771269139679211, 0.0837813307920479, 0.058610271774008106, 0.0307511583274093, 0.012907413118623416, 0.004514770675221357, 0.001353584557240361, 0.0003550938408009029, 8.280343730464544e-05, 1.737785226744551e-05, 3.315516176395373e-06, 5.798526423863442e-07, 9.360995225359491e-08, 1.4032715600583696e-08, 1.9633521389603836e-09, 2.5752888806942524e-10, 3.1792506355280884e-11], [0.03864006036067424, 0.09025091075029511, 0.10202929443690098, 0.07137586165466649, 0.0374489036829766, 0.015718707748477823, 0.005498108733562484, 0.0016484015714516114, 0.0004324349314256074, 0.00010083841119822625, 2.116282934293584e-05, 4.037651025279006e-06, 7.061472457019833e-07, 1.139986353811034e-07, 1.7089106346555456e-08, 2.3909793694554404e-09, 3.136198780616294e-10, 3.8717062156261216e-11], [0.024661267132812744, 0.051756288254713144, 0.056430040113270234, 0.04346092820205411, 0.02280272456935134, 0.009571157714227084, 0.0033478111980287844, 0.0010037155515071508, 0.00026331063571153094, 6.140074315738638e-05, 1.2886096017665737e-05, 2.4585351020155184e-06, 4.2997470060700386e-07, 6.941403427675974e-08, 1.040559660853294e-08, 1.4558729001585603e-09, 1.9096387332064254e-10, 2.3574909213831157e-11], [0.010010868617521184, 0.021009682878748052, 0.02204637736894289, 0.016024821990829288, 0.009256421357261483, 0.00388526679828286, 0.001358993350959653, 0.0004074431561601136, 0.00010688697241338677, 2.4924703562734206e-05, 5.230915894584099e-06, 9.980051619121429e-07, 1.7454173029525838e-07, 2.8177577965252644e-08, 4.2239946542060036e-09, 5.909895971202912e-10, 7.751889780076643e-11, 9.569878041491198e-12], [0.0030478205946662604, 0.006396422389679808, 0.006712045233042547, 0.004695494706863719, 0.0025597561532616146, 0.0011828739958542852, 0.0004137471064019365, 0.0001240465428072019, 3.25418630759845e-05, 7.588354990644456e-06, 1.592558428404204e-06, 3.0384383236589105e-07, 5.313943280521199e-08, 8.578696386046094e-09, 1.2860000855786883e-09, 1.7992747024810586e-10, 2.360071860093064e-11, 2.913560500859262e-12], [0.0007423300200754752, 0.0015579185891885375, 0.0016347919826093192, 0.0011436390600254832, 0.0006000351941696547, 0.000261688086361441, 0.00010077263023257151, 3.021289139311912e-05, 7.925926451433449e-06, 1.848226802589001e-06, 3.8788501271942894e-07, 7.400448654185939e-08, 1.2942689701003174e-08, 2.089435274379176e-09, 3.1321937748413447e-10, 4.382330207858952e-11, 5.748212983232659e-12, 7.096295066969973e-13], [0.0001506688253648111, 0.00031620675103934885, 0.00033180954706710296, 0.00023212149469293566, 0.00012178760852739901, 5.111882158244399e-05, 1.8578336080593592e-05, 6.132233284345737e-06, 1.608705018078005e-06, 3.751298665323172e-07, 7.872802885852461e-08, 1.5020501336931312e-08, 2.6269446224377632e-09, 4.240873330631357e-10, 6.357333586244252e-11, 8.894703527033756e-12, 1.1667000858221582e-12, 1.4403168580919858e-13], [2.6212170932319164e-05, 5.5011150369879274e-05, 5.772560145497493e-05, 4.0382662314016206e-05, 2.118764518425803e-05, 8.893248393842537e-06, 3.11069125059986e-06, 9.690274938875313e-07, 2.798697793750012e-07, 6.526212811147114e-08, 1.3696479975917879e-08, 2.6131480588599986e-09, 4.5701505474905717e-10, 7.37793610427821e-11, 1.1059986313222219e-11, 1.5474301912050568e-12, 2.0297325609511422e-13, 2.5057493870809375e-14], [3.990162964410994e-06, 8.374104357945123e-06, 8.78731325301987e-06, 6.147274256136802e-06, 3.2253016102938764e-06, 1.3537799088081262e-06, 4.7352678471041443e-07, 1.4196923594403214e-07, 3.869737354302313e-08, 9.93456540633042e-09, 2.0849546298097853e-09, 3.9778798299111764e-10, 6.956938249588196e-11, 1.1231106142674983e-11, 1.683612848697657e-12, 2.3555846079672817e-13, 3.0897721952440207e-14, 3.814391577195963e-15], [5.399154469516155e-07, 1.1331136942440204e-06, 1.1890256625667467e-06, 8.317976877483737e-07, 4.364208118834659e-07, 1.831821634999692e-07, 6.407368017066054e-08, 1.921008845046416e-08, 5.039496094656675e-09, 1.2210173503624602e-09, 2.8211860539730105e-10, 5.382533960247269e-11, 9.413546408863688e-12, 1.5196992571150557e-12, 2.278123955852668e-13, 3.187379883444784e-14, 4.180821060826277e-15, 5.161315343806365e-16], [6.575115432910486e-08, 1.3799111287389667e-07, 1.4480009838966214e-07, 1.0129670941353361e-07, 5.314752951892212e-08, 2.230800909777483e-08, 7.80292258189892e-09, 2.3394135091219486e-09, 6.137121790671541e-10, 1.431099954532222e-10, 3.1206653554024276e-11, 6.554874899394787e-12, 1.146386061387969e-12, 1.8506968258189617e-13, 2.7743099525641656e-14, 3.8816060515609454e-15, 5.091423339428834e-16, 6.285473839058383e-17], [7.279278332155056e-09, 1.527692902462528e-08, 1.6030748501022363e-08, 1.1214509455785258e-08, 5.883937156422056e-09, 2.46970884261829e-09, 8.638577658059111e-10, 2.5899533233539295e-10, 6.794377700051576e-11, 1.5843638026539134e-11, 3.325084198994146e-12, 6.59154457999266e-13, 1.269158435634057e-13, 2.0488974590684592e-14, 3.071425061725967e-15, 4.2973071900248406e-16, 5.636690028136484e-17, 6.958617531636579e-18], [7.387282516863691e-10, 1.5503596035950821e-09, 1.6268600090578154e-09, 1.1380901492936665e-09, 5.971238370424142e-10, 2.5063524325242316e-10, 8.766750052962534e-11, 2.6283810059288103e-11, 6.895187312023009e-12, 1.607871341860324e-12, 3.3744191730963947e-13, 6.438046072758097e-14, 1.1699035691691649e-14, 2.0792973819070702e-15, 3.1169964418200674e-16, 4.361067241272089e-17, 5.720322784457253e-18, 7.061864004557352e-19], [6.920205399131857e-11, 1.452334721855146e-10, 1.5239982216211928e-10, 1.066131906809018e-10, 5.5936937454581066e-11, 2.3478828102333265e-11, 8.212453078768617e-12, 2.4621958598012814e-12, 6.459223991469221e-13, 1.5062101544987528e-13, 3.1610641297782384e-14, 6.030986508348033e-15, 1.0547629017645228e-15, 1.7692480503309426e-16, 2.919917514528167e-17, 4.085329212756442e-18, 5.358642847002475e-19, 6.615362185040747e-20], [6.0196130941353284e-12, 1.2633285581152516e-11, 1.3256658034255392e-11, 9.273859974023512e-12, 4.865733048757002e-12, 2.0423304357048166e-12, 7.143688263086717e-13, 2.1417668382856022e-13, 5.618623591993233e-14, 1.3101926670670388e-14, 2.7496847173642714e-15, 5.246116735315358e-16, 9.174965493750252e-17, 1.481183354211733e-17, 2.30705537465818e-18, 3.5536663732621793e-19, 4.661271564664448e-20, 5.754442033832502e-21], [4.887141888465159e-13, 1.0256582638632515e-12, 1.076267988774682e-12, 7.529166549087148e-13, 3.950341563287029e-13, 1.6581063377884793e-13, 5.79974453552199e-14, 1.7388357469201546e-14, 4.561590634238756e-15, 1.0637058171432138e-15, 2.2323858946010366e-16, 4.2591635787882046e-17, 7.448877110293764e-18, 1.202527986710295e-18, 1.8026644425085704e-19, 2.6206007741744907e-20, 3.784345465554439e-21, 4.671857521156363e-22], [3.71974008095825e-14, 7.806571285484765e-14, 8.191776025874329e-14, 5.730658783398906e-14, 3.006715209377492e-14, 1.2620310078821391e-14, 4.414347424415595e-15, 1.3234764141569055e-15, 3.4719539359293217e-16, 8.096161831754577e-17, 1.6991312054828046e-17, 3.2417682639354818e-18, 5.669548250827241e-19, 9.152776106619485e-20, 1.372058215691233e-20, 1.91968077258225e-21, 2.616292306076093e-22, 3.555881140874609e-23], [2.664656927608771e-15, 5.592281665922174e-15, 5.868225268885522e-15, 4.105189958060766e-15, 2.1538775123100642e-15, 9.040630782847344e-16, 3.1622428420618934e-16, 9.480798439555261e-17, 2.4871539156922205e-17, 5.799731498032239e-18, 1.217182286682685e-18, 2.32225910256951e-19, 4.0614130810685976e-20, 6.556643133267727e-21, 9.828816933311987e-22, 1.3751742213506731e-22, 1.8037879252455504e-23, 2.313735902718901e-24]] |
| Legacy trial inputs | {"lambda_home": 1.2178046525680766, "lambda_away": 2.0986873049134385, "rho": -0.021895783674930586, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1961 |
| Legacy p draw | 0.2020 |
| Legacy p away | 0.6019 |
| Legacy p over 1 5 | 0.8472 |
| Legacy p under 3 5 | 0.5739 |
| Legacy p btts yes | 0.6161 |
| Legacy p over 2 5 | 0.6485 |
| Legacy goal margin distribution | {"-1": 0.23374940434552718, "-10": 2.1874986586442012e-05, "-11": 4.095487270743239e-06, "-12": 7.048721743212084e-07, "-13": 1.1223536395861055e-07, "-14": 1.662422872140127e-08, "-15": 2.3005469262358444e-09, "-16": 2.9624595022568645e-10, "-17": 3.1792506355280884e-11, "-2": 0.18229081991923698, "-3": 0.10712168822516631, "-4": 0.050259591932248784, "-5": 0.019524116105089046, "-6": 0.006453076851302165, "-7": 0.0018529683696271275, "-8": 0.0004698716471989665, "-9": 0.00010660824449714675, "0": 0.20203627151160702, "1": 0.11779263255342924, "10": 8.276659260630681e-08, "11": 8.991719588576974e-09, "12": 8.980022697762198e-10, "13": 8.297106802659207e-11, "14": 7.131294308215384e-12, "15": 5.726481269702491e-13, "16": 4.2789682475504673e-14, "17": 2.664656927608771e-15, "2": 0.053657808528322616, "3": 0.018296812392273782, "4": 0.004981347945976227, "5": 0.0011228692664477437, "6": 0.00021535479410078373, "7": 3.5882740665917785e-05, "8": 5.279912601275785e-06, "9": 6.951334370895118e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2139 |
| Legacy raw p draw | 0.2121 |
| Legacy raw p away | 0.5740 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2178 |
| Legacy lambda away | 2.0987 |
| Legacy model home team | Levante |
| Legacy model away team | Ath Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 39.6% |
| Market home draw odds | 2.58 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T07:00:26Z |
| Market reference home draw last update utc | 2026-10-30T07:01:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.2% |
| Market draw away odds | 1.18 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T07:00:26Z |
| Market reference draw away last update utc | 2026-10-30T07:01:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.2% |
| Market home away odds | 1.21 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T07:00:26Z |
| Market reference home away last update utc | 2026-10-30T07:01:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.17 |
| Market reference dc home draw odds | 2.40 |
| Market reference dc home away odds | 1.20 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:26Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.3, "price": 1.61, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:26Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.3, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:26Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.77, "price": 2.04, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:26Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.04, "price": 1.77, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 84.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-30T07:01:04Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.2% |
| Market under 3 5 odds | 1.60 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:01:05Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.35 |
| Market reference under 3 5 last update utc | 2026-10-30T07:01:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.9% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T07:00:26Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.25 |
| Market reference btts yes last update utc | 2026-10-30T07:01:04Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 9.763974031546171, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,476.0819 |
| Elo away rating | 1,586.5836 |
| Elo rating diff | -50.5017 |
| Elo home expectancy | 0.4278 |

</details>


---

## 2026-10-31 — Rayo Vallecano vs Celta Vigo

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **38.9%**. Expected goals are 1.17 for Rayo Vallecano and 1.10 for Celta Vigo (2.27 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 43.5%; Under 3.5 goals: 77.3%; Double Chance 1X: 68.1%; Double Chance X2: 61.1%; Double Chance 12 (either team wins): 70.9%; Under 4.5 goals: 90.2%; BTTS Yes (both teams score): 50.0%; BTTS No (at least one team does not score): 50.0%.

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
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 43.5% |
| Under 2.5 | 56.5% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.8% |
| Under 4.5 | 90.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.81% |
| 2 | 1-0 | 10.98% |
| 3 | 0-0 | 9.53% |
| 4 | 0-1 | 9.35% |
| 5 | 2-1 | 8.39% |

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
| Market best home last update utc | 2026-10-30T07:00:40Z |
| Market best draw last update utc | 2026-10-30T07:00:40Z |
| Market best away last update utc | 2026-10-30T07:00:40Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Vallecano |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1745 |
| Dc lambda away | 1.0992 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:00:18.879025+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.49 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.35 |
| Fair Over 2.5 odds | 2.30 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.41 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.16 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.18513555825647163, "-10": 1.2914266728918125e-07, "-11": 1.3621871902485059e-08, "-12": 1.3190686778950847e-09, "-13": 1.1753789779263366e-10, "-14": 8.912662769213593e-12, "-2": 0.09093365349565115, "-3": 0.031904785102764024, "-4": 0.00874306772664229, "-5": 0.00195845095569086, "-6": 0.0003702671639580414, "-7": 6.049354477738485e-05, "-8": 8.695729647159668e-06, "-9": 1.1154378879281046e-06, "0": 0.29143011671119046, "1": 0.21694605497159275, "10": 2.742110017433414e-07, "11": 3.0903105061521485e-08, "12": 3.1972966850193347e-09, "13": 3.0439930151956107e-10, "14": 2.466172269245979e-11, "2": 0.11369415516592986, "3": 0.04262059667181987, "4": 0.012478941457681388, "5": 0.0029865982623036753, "6": 0.0006032947007732696, "7": 0.00010531095421629649, "8": 1.617412317081688e-05, "9": 2.2167173080885962e-06} |
| Raw goal margin distribution | {"-1": 0.1993667521807398, "-10": 8.211127402887275e-08, "-11": 8.125379308670898e-09, "-12": 7.35199781048394e-10, "-13": 5.654994603032723e-11, "-2": 0.09365848986574067, "-3": 0.03116070301949937, "-4": 0.008063583519514831, "-5": 0.0017016595939834077, "-6": 0.0003026563226686957, "-7": 4.647432265087464e-05, "-8": 6.2748247336546975e-06, "-9": 7.556729433728814e-07, "0": 0.29404697586598677, "1": 0.21330803501741505, "10": 1.59185982273923e-07, "11": 1.6830455811566035e-08, "12": 1.627075876800915e-09, "13": 1.3371644906385404e-10, "2": 0.10691719519701634, "3": 0.03800649816996285, "4": 0.010508213814684265, "5": 0.0023693199001326632, "6": 0.00045024714702174024, "7": 7.386938621774428e-05, "8": 1.0656221141484052e-05, "9": 1.371152313009918e-06} |
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
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0672 |
| Totals anchor target over 2 5 | 0.4345 |
| Totals anchor reference over odds | 2.21 |
| Totals anchor reference under odds | 1.72 |
| Totals anchor reference last update utc | 2026-10-30T07:01:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3979 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.27, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.74, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.64, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.11, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.9, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.64, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.45 |
| Reference draw odds | 3.32 |
| Reference away odds | 3.09 |
| Market reference 1x2 last update utc | 2026-10-30T07:00:40Z |
| Market reference home last update utc | 2026-10-30T07:00:40Z |
| Market reference draw last update utc | 2026-10-30T07:00:40Z |
| Market reference away last update utc | 2026-10-30T07:00:40Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.26 |
| Reference Under 2.5 odds | 1.77 |
| Market reference over 2 5 last update utc | 2026-10-30T07:00:41Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:00:41Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.0254 |
| Raw ev home | -0.0895 |
| Raw edge prob draw | 0.0037 |
| Raw ev draw | -0.0238 |
| Raw edge prob away | 0.0217 |
| Raw ev away | 0.0330 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10494008065035451, 0.10515597527636879, 0.05807270589843905, 0.02081515097726593, 0.005595621516639468, 0.001203391902049659, 0.00021566744427054655, 3.312953264302409e-05, 4.453014198551464e-06, 5.320351526748776e-07, 5.720962295527185e-08, 5.5924892492009635e-09, 5.011326158300466e-10, 4.145129228063196e-11, 3.183748816033685e-12], [0.12169380961154427, 0.13541806638302128, 0.0701373127364402, 0.02513949937690024, 0.006758112097508535, 0.0014533966150322816, 0.0002604723639419512, 4.0012194297602756e-05, 5.378128066045698e-06, 6.425654756848623e-07, 6.909492427931766e-08, 6.754329101391689e-09, 6.052429356464182e-10, 5.0062799813404585e-11, 3.845172752496588e-12], [0.07525980515281337, 0.08092670295999767, 0.04302449949962814, 0.015181115659728451, 0.004081055070172102, 0.0008776699082773645, 0.00015729275368144637, 2.4162364585095095e-05, 3.247717187180463e-06, 3.880292387319259e-07, 4.17246987005768e-08, 4.0787706133207885e-09, 3.6549108916323985e-10, 3.0231674180253214e-11, 2.3220037683377595e-12], [0.030298344169449754, 0.03257974284948277, 0.017516462916291786, 0.0062083920585913836, 0.0016429648049112707, 0.00035333528826127886, 6.332344306132973e-05, 9.727365579281847e-06, 1.3074768517195998e-06, 1.5621410923185187e-07, 1.679766880913073e-08, 1.6420451206285277e-09, 1.4714062556832079e-10, 1.2170768543342942e-11, 9.348000462266248e-13], [0.009148206577998102, 0.009837046413435658, 0.005288877186749261, 0.0018957060023160116, 0.0005039239148813683, 0.00010668517692692741, 1.911972268567921e-05, 2.937056536201945e-06, 3.9477630422925887e-07, 4.716689907733972e-08, 5.071846284249071e-09, 4.957950140737475e-10, 4.4427274018232714e-11, 3.674811541673907e-12, 2.822511977610375e-13], [0.0022097493678380807, 0.0023761386352777456, 0.0012775283243057142, 0.0004579077991416922, 0.00012309681233216941, 2.6177657296673304e-05, 4.618369158773909e-06, 7.094460284473801e-07, 9.535821926082435e-08, 1.139316482748709e-08, 1.2251045081716813e-09, 1.1975928938483607e-10, 1.0731408373819441e-11, 8.876507555773826e-13, 6.81777789456607e-14], [0.0004448041470412935, 0.00047829692104431744, 0.00025715581363412553, 9.217302694379634e-05, 2.4778363288539648e-05, 5.328823909695173e-06, 9.443524129467105e-07, 1.4280557793036245e-07, 1.9194815484067893e-08, 2.2933492082630607e-09, 2.466033359823448e-10, 2.4106547710978576e-11, 2.160143144622146e-12, 1.7867670558106867e-13, 1.372361918164675e-14], [7.674460362070096e-05, 8.25233034869618e-05, 4.436856337195452e-05, 1.5903139537647214e-05, 4.275152742162198e-06, 9.194124682387558e-07, 1.647737008349463e-07, 2.502901920529697e-08, 3.311791303421747e-09, 3.956846560957485e-10, 4.254788404603305e-11, 4.1592405580040996e-12, 3.7270185204143553e-13, 3.082811398518459e-14, 2.367814511943282e-15], [1.1586037239234105e-05, 1.2458440361879143e-05, 6.698266760480381e-06, 2.400877171958139e-06, 6.45414485673939e-07, 1.3880255539370616e-07, 2.4875680423804516e-08, 3.821252064284864e-09, 5.078900150208892e-10, 5.973601978813647e-11, 6.4234010699220425e-12, 6.279153675760191e-13, 5.6266334480341564e-14, 4.654081978362821e-15, 3.5746600824939183e-16], [1.5547818791257068e-06, 1.6718535351521512e-06, 8.988702146993433e-07, 3.221843883192842e-07, 8.661104104283145e-08, 1.8626532389493895e-08, 3.3381782187686148e-09, 5.127908138429694e-10, 6.89253542914171e-11, 8.143113219896225e-12, 8.61984764907562e-13, 8.426275653816977e-14, 7.550629732020783e-15, 6.245519649652338e-16, 4.796995388099537e-17], [1.8777878730827454e-07, 2.0191811700587756e-07, 1.0856105356635959e-07, 3.891182071293096e-08, 1.0460448808211981e-08, 2.2496195195073203e-09, 4.031684869467053e-10, 6.193231247356893e-11, 8.324459924187885e-12, 9.94585938697859e-13, 1.0575387518998557e-13, 1.0176834738315472e-14, 9.119273343280513e-16, 7.543026592136496e-17, 5.793571360680154e-18], [2.0617257949563722e-08, 2.2169692129100904e-08, 1.1919510594024435e-08, 4.2723411756228895e-09, 1.1485097674694026e-09, 2.4699800540256355e-10, 4.426606866338653e-11, 6.799886611176807e-12, 9.139878897291423e-13, 1.0920101862985638e-13, 1.174236151640793e-14, 1.1350545588189892e-15, 1.0012547930791211e-16, 8.281900591635349e-18, 6.361078208277688e-19], [2.075041172103188e-09, 2.2312872086712103e-09, 1.199649114078442e-09, 4.2999335131647947e-10, 1.155927262437971e-10, 2.4859320860780638e-11, 4.455195507975758e-12, 6.843802759000585e-13, 9.198907568752666e-14, 1.0990627863651198e-14, 1.1818197969813963e-15, 1.155280207715873e-16, 1.0236702040398925e-17, 8.335388126272511e-19, 6.40216037139114e-20], [1.927793118288067e-10, 2.0729517002502378e-10, 1.1145202020915814e-10, 3.994803740387232e-11, 1.0739009190409795e-11, 2.309526592773782e-12, 4.1390481096808214e-13, 6.358156184607084e-14, 8.546139202064734e-15, 1.0210716320263087e-15, 1.0979560802488216e-16, 1.0732997802986809e-17, 9.617640776828329e-19, 7.866457037050948e-20, 5.9478534074747835e-21], [1.6630658651660192e-11, 1.7882910671895467e-11, 9.614727257572218e-12, 3.4462316913835957e-12, 9.264313395897265e-13, 1.9923791638731845e-13, 3.570668221703611e-14, 5.4850452653365016e-15, 7.372571388019253e-16, 8.808566443168339e-17, 9.471832123432475e-18, 9.259127500621149e-19, 8.296932864650839e-20, 6.862825893616534e-21, 5.2122942017913075e-22]] |
| Legacy trial inputs | {"lambda_home": 1.2077500376700276, "lambda_away": 1.0752978006743148, "rho": -0.021895783674930586, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3925 |
| Legacy p draw | 0.2901 |
| Legacy p away | 0.3174 |
| Legacy p over 1 5 | 0.6682 |
| Legacy p under 3 5 | 0.8027 |
| Legacy p btts yes | 0.4648 |
| Legacy p over 2 5 | 0.3995 |
| Legacy goal margin distribution | {"-1": 0.19222881820151194, "-10": 6.434189616556789e-08, "-11": 6.228898659073861e-09, "-12": 5.535174194117889e-10, "-13": 4.5296465033128554e-11, "-14": 3.183748816033685e-12, "-2": 0.08766644439949553, "-3": 0.028517291177401257, "-4": 0.007216444671221007, "-5": 0.001489382523915962, "-6": 0.00025908876366146396, "-7": 3.891299432407781e-05, "-8": 5.138991746705925e-06, "-9": 6.053597311824051e-07, "0": 0.2901221100613455, "1": 0.22216127579127634, "10": 2.1118900302019735e-07, "11": 2.2963443410135475e-08, "12": 2.2919510693857842e-09, "13": 2.1066222250070217e-10, "14": 1.6630658651660192e-11, "2": 0.11361205616084998, "3": 0.0415095092904681, "4": 0.011798068617527075, "5": 0.0027349046350459566, "6": 0.0005343586136433829, "7": 9.014199980647057e-05, "8": 1.3370842107087759e-05, "9": 1.7690604383240322e-06} |
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
| Market p home draw | 69.6% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T06:59:57Z |
| Market reference home draw last update utc | 2026-10-30T07:01:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.2% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T06:59:57Z |
| Market reference draw away last update utc | 2026-10-30T07:01:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.2% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T06:59:57Z |
| Market reference home away last update utc | 2026-10-30T07:01:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.60 |
| Market reference dc home draw odds | 1.36 |
| Market reference dc home away odds | 1.33 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:59:57Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.39, "price": 1.55, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:59:57Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.55, "price": 2.39, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:59:57Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.88, "price": 1.94, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:59:57Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.94, "price": 1.88, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:59:57Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.53, "price": 2.44, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T06:59:57Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.44, "price": 1.53, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 70.8% |
| Market over 1 5 odds | 1.38 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:01:05Z |
| Market reference over 1 5 odds | 1.38 |
| Market reference over 1 5 opposite odds | 3.16 |
| Market reference over 1 5 last update utc | 2026-10-30T07:01:05Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 77.0% |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 4.00 |
| Market reference under 3 5 last update utc | 2026-10-30T07:00:18Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 52.2% |
| Market btts yes odds | 1.93 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T06:59:57Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-10-30T07:01:04Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 9.257935485706028, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.5850 |
| Elo away rating | 1,513.4884 |
| Elo rating diff | 21.0966 |
| Elo home expectancy | 0.5303 |

</details>


---

## 2026-10-31 — Real Betis vs Málaga

The model's most likely 1X2 outcome is **Real Betis win** at **74.4%**. Expected goals are 2.36 for Real Betis and 0.60 for Málaga (2.96 combined). The most likely exact score is 2-0 at 11.4%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.8%; Under 3.5 goals: 56.7%; Double Chance 1X: 90.3%; Double Chance X2: 25.6%; Double Chance 12 (either team wins): 84.1%; Under 4.5 goals: 75.1%; BTTS Yes (both teams score): 47.9%; BTTS No (at least one team does not score): 52.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 74.4% | 1.34 |
| Draw | 15.9% | 6.30 |
| Málaga win | 9.7% | 10.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 2.36 |
| Málaga expected goals | 0.60 |
| Expected total goals | 2.96 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 64.8% |
| Under 2.5 | 35.2% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 24.9% |
| Under 4.5 | 75.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.36% |
| 2 | 3-0 | 10.34% |
| 3 | 1-0 | 8.13% |
| 4 | 2-1 | 7.83% |
| 5 | 1-1 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 74.4% | 73.5% | 1.34 | -0.3% |
| Draw | 15.9% | 15.8% | 5.75 | -8.7% |
| Málaga win | 9.7% | 10.7% | 8.32 | -19.2% |

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
| Market best home last update utc | 2026-10-30T07:00:40Z |
| Market best draw last update utc | 2026-10-30T07:00:40Z |
| Market best away last update utc | 2026-10-30T07:00:40Z |
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
| Dc lambda away | 0.5960 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:00:18.879025+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 47.9% |
| P btts no | 52.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.33 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.57 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.84 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.02 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.07200448881517532, "-10": 3.743267082001399e-10, "-11": 2.3120240952462202e-11, "-12": 1.311795137843888e-12, "-13": 6.881837111287741e-14, "-14": 3.356925843590257e-15, "-15": 1.5300004301451546e-16, "-16": 6.543403593409837e-18, "-17": 2.6354419656921704e-19, "-18": 9.99058818848726e-21, "-19": 3.296330141421532e-22, "-2": 0.02025667100173287, "-3": 0.004066446268457762, "-4": 0.0006433290291772748, "-5": 8.362138133661816e-05, "-6": 9.203038146837671e-06, "-7": 8.770839970090482e-07, "-8": 7.36509992403336e-08, "-9": 5.52467022467301e-09, "0": 0.15871650345931404, "1": 0.18833542960715188, "10": 0.000229878122437154, "11": 5.62887233788663e-05, "12": 1.2661270199210487e-05, "13": 2.633285004653176e-06, "14": 5.092340576304524e-07, "15": 9.201305789341705e-08, "16": 1.560069104419735e-08, "17": 2.49101189958126e-09, "18": 3.7436532811787785e-10, "19": 4.8968576630161014e-11, "2": 0.20387180358895318, "3": 0.16225061273362354, "4": 0.1017622434929022, "5": 0.05243884031490123, "6": 0.02287963967034666, "7": 0.008644529533245498, "8": 0.0028778028320658464, "9": 0.0008557974117994219} |
| Raw goal margin distribution | {"-1": 0.05606649661478445, "-10": 9.18004921222604e-11, "-11": 4.921621558359733e-12, "-12": 2.422576938912629e-13, "-13": 1.1021295147617268e-14, "-14": 4.660607052609951e-16, "-15": 1.8409685302769802e-17, "-16": 6.821591200275651e-19, "-17": 2.374177851570886e-20, "-18": 7.290443807638843e-22, "-2": 0.014377109157569658, "-3": 0.002573211205729464, "-4": 0.0003591985876587877, "-5": 4.095294318540198e-05, "-6": 3.938902613940793e-06, "-7": 3.2727807015014177e-07, "-8": 2.392024902293476e-08, "-9": 1.5598692229642796e-09, "0": 0.15983700323628772, "1": 0.22933590010095234, "10": 8.803739411613132e-05, "11": 1.8711672291758346e-05, "12": 3.651440114620755e-06, "13": 6.585692571974484e-07, "14": 1.1040621606080519e-07, "15": 1.728938794463052e-08, "16": 2.5398096050169803e-09, "17": 3.504377939093189e-10, "18": 4.266127907553027e-11, "2": 0.2259623090627926, "3": 0.16033269215544796, "4": 0.0887285712316781, "5": 0.04010478604140352, "6": 0.015292149854051971, "7": 0.005037237460224452, "8": 0.001459564972446541, "9": 0.0003773359137164635} |
| Unadjusted home-win probability | 76.7% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 7.3% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 40.9% |
| P home draw | 90.3% |
| P draw away | 25.6% |
| P home away | 84.1% |
| Raw p home draw | 92.7% |
| Raw p draw away | 23.3% |
| Raw p home away | 84.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1561 |
| Totals anchor target over 2 5 | 0.6476 |
| Totals anchor reference over odds | 1.51 |
| Totals anchor reference under odds | 2.69 |
| Totals anchor reference last update utc | 2026-10-30T07:01:05Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5640 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.01, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.93, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:27Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 6.88, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:27Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.13, "price": 6.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:01:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.48, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.34 |
| Reference draw odds | 5.75 |
| Reference away odds | 8.32 |
| Market reference 1x2 last update utc | 2026-10-30T07:00:40Z |
| Market reference home last update utc | 2026-10-30T07:00:40Z |
| Market reference draw last update utc | 2026-10-30T07:00:40Z |
| Market reference away last update utc | 2026-10-30T07:00:40Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Market reference over 2 5 last update utc | 2026-10-30T07:00:42Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:00:42Z |
| Home probability edge | +1.0% |
| Draw probability edge | +0.0% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0322 |
| Raw ev home | 0.0274 |
| Raw edge prob draw | 0.0016 |
| Raw ev draw | -0.0809 |
| Raw edge prob away | -0.0338 |
| Raw ev away | -0.3891 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05969583092716829, 0.03859385463900976, 0.011354480679650626, 0.0021165688272995658, 0.0002959094119155767, 3.309597266324265e-05, 3.084681106275541e-06, 2.464328547308523e-07, 1.722641857414123e-08, 1.070382156869182e-09, 5.985841811120222e-11, 3.0431189253138163e-12, 1.418156152801424e-13, 6.1005230986959555e-15, 2.4368310220214573e-16, 9.084907930401022e-18, 3.175315785055308e-19, 1.0445383162352259e-20], [0.13049811809834394, 0.07519005851532926, 0.025720091400888167, 0.0047944371240138985, 0.0006702919609957788, 7.496876923886662e-05, 6.9873983878618895e-06, 5.582180045643749e-07, 3.902116466065476e-08, 2.4246222865916473e-09, 1.3559087626895088e-10, 6.8932520219191794e-12, 3.2123975459445577e-13, 1.3818862889334493e-14, 5.519892840826968e-16, 2.0579070847100855e-17, 7.192703437742645e-19, 2.3660809968568715e-20], [0.14963393623422655, 0.0836789987692964, 0.023301583258750605, 0.005430162969339924, 0.0007591703658005814, 8.490936976498837e-05, 7.913903341801991e-06, 6.322357888524279e-07, 4.4195236662819754e-08, 2.746118848726003e-09, 1.5356975933800444e-10, 7.807273492078981e-12, 3.638350393504089e-13, 1.56511965010874e-14, 6.251811614934481e-16, 2.330778474445708e-17, 8.146431134000384e-19, 2.6798151856530284e-20], [0.11298325378328085, 0.06318303048235742, 0.01766675683014032, 0.003279703081570678, 0.0005732224939249699, 6.411203978300335e-05, 5.975506440487849e-06, 4.773787175589091e-07, 3.337024852484883e-08, 2.07349649827425e-09, 1.1595505357530238e-10, 5.8949940401907e-12, 2.7471887474664026e-13, 1.1817660824790077e-14, 4.720520197969894e-16, 1.7598877802605907e-17, 6.151079891396025e-19, 2.0234329646918086e-20], [0.06398222199813418, 0.03578044132621087, 0.010004653961031177, 0.001864949996329491, 0.00025966065710637603, 3.6306537692901394e-05, 3.3839190041378536e-06, 2.703387454447568e-07, 1.8897514257690268e-08, 1.1742174952706911e-09, 6.566514710128137e-11, 3.3383249705362377e-12, 1.5557282555194212e-13, 6.6923209685634145e-15, 2.673222456776865e-16, 9.966214184663475e-18, 3.4833459469530537e-19, 1.1458666024399097e-20], [0.028986417683958127, 0.0162099218315386, 0.004532494643689815, 0.0008448943763609713, 0.00011812145904025817, 1.3157026508216755e-05, 1.5330460024580553e-06, 1.2247389269862284e-07, 8.561303817768907e-09, 5.319658759384745e-10, 2.974884775354941e-11, 1.5123901443055922e-12, 7.048049850243792e-14, 3.0318798693103726e-15, 1.211073018010074e-16, 4.515079940375749e-18, 1.5780902476167249e-19, 5.1912182651908835e-21], [0.010943305602575327, 0.006119767207196389, 0.00171116260618102, 0.0003189748199734373, 4.459465252289561e-05, 4.9876865736384045e-06, 4.629636096412106e-07, 4.623783631185962e-08, 3.2321677364840447e-09, 2.0083423947065234e-10, 1.1231147492632257e-11, 5.709759557014393e-13, 2.6608656597151135e-14, 1.144632231616589e-15, 4.572190426432756e-17, 1.7045879951883185e-18, 5.957798592570139e-20, 1.9598519742953424e-21], [0.003541242921339457, 0.0019803506444734126, 0.0005537305350380856, 0.0001032199377718774, 1.443078566124781e-05, 1.6140104657773832e-06, 1.504324299446856e-07, 1.1968573247517116e-08, 1.0459262980568045e-09, 6.498976220865761e-11, 3.6343882736349464e-12, 1.8476725724509766e-13, 8.610535083552722e-15, 3.7040186347307395e-16, 1.4795563215205005e-17, 5.516029973923321e-19, 1.927937760208407e-20, 6.342061697713397e-22], [0.0010026998831927383, 0.0005607345793558478, 0.00015678832408168411, 2.9226636479339673e-05, 4.086064531105229e-06, 4.570056732777596e-07, 4.259481297512402e-08, 3.4028675887538996e-09, 2.3689397460545007e-10, 1.8401795195314188e-11, 1.0290739094714285e-12, 5.231668975350215e-14, 2.4380655928680555e-15, 1.0487896862448028e-16, 4.189350981334365e-18, 1.5618591362968436e-19, 5.458939163181262e-21, 1.7957493074474068e-22], [0.00025236765184491694, 0.00014113023395364392, 3.946175904519248e-05, 7.355997286177166e-06, 1.0284139135614259e-06, 1.150229002497492e-07, 1.0720608540491055e-08, 8.564613572892214e-10, 5.986929725484428e-11, 3.704764464054432e-12, 2.5900568102315496e-13, 1.3167489461901618e-14, 6.136321535780274e-16, 2.639679078788637e-17, 1.0544098863830498e-18, 3.931013948906573e-20, 1.3739501532498918e-21, 4.51968773128426e-23], [5.716614660952072e-05, 3.1968723353608636e-05, 8.938850468971031e-06, 1.666275436834716e-06, 2.329556111020556e-07, 2.6054908111480608e-08, 2.428424859877046e-09, 1.9400503653404692e-10, 1.3561551963016918e-11, 8.426617046480999e-13, 4.69301787989916e-14, 2.9826906402447802e-15, 1.3899953262359444e-16, 5.979382861352053e-18, 2.388442009538615e-19, 8.904505711586124e-21, 3.1122624203486543e-22, 1.0237965507347256e-23], [1.1772032855784931e-05, 6.5832119881507445e-06, 1.840747499257721e-06, 3.431305125949983e-07, 4.7971767741576786e-08, 5.3653998482333354e-09, 5.000773872961452e-10, 3.995080654756247e-11, 2.7926849149822076e-12, 1.7352649884183505e-13, 9.70403108309388e-15, 4.913132143588789e-16, 2.862370759674721e-17, 1.231314259853063e-18, 4.918438530146242e-20, 1.833674998549903e-21, 6.408977627690457e-23, 2.1082699023273422e-24], [2.222160642770763e-06, 1.2426872029919954e-06, 3.474707126831639e-07, 6.477140607432678e-08, 9.055443146090685e-09, 1.0128055639611411e-09, 9.439765433911794e-11, 7.541357643536951e-12, 5.271642189380629e-13, 3.2755919128669556e-14, 1.8317920288914727e-15, 9.312576520152672e-17, 4.322027835125985e-18, 2.324303814513476e-19, 9.28434422454685e-21, 3.4613566436046412e-22, 1.2097976635915916e-23, 3.979698713623408e-25], [3.8720176745156944e-07, 2.165328069117392e-07, 6.054525109436778e-08, 1.1286134057811162e-08, 1.5778713400537986e-09, 1.7647693731158953e-10, 1.6448378168472204e-11, 1.314048567128339e-12, 9.185605819007427e-14, 5.707575562722229e-15, 3.191817448022559e-16, 1.6226757052249162e-17, 7.562003299390598e-19, 3.23960799052138e-20, 1.6177563512649076e-21, 6.031262476653487e-23, 2.1080194860141225e-24, 6.934450850134531e-26], [6.264905540951478e-08, 3.5034901590133036e-08, 9.796191829285663e-09, 1.8260909360013753e-09, 2.5529880625991724e-10, 2.8553881602614627e-11, 2.661339492470572e-12, 2.126124114428629e-13, 1.4862265007530897e-14, 9.234829170238799e-16, 5.164344922140174e-17, 2.6254813049381184e-18, 1.2235284121468045e-19, 5.263287350597935e-21, 2.0937652938772715e-22, 9.758553003931026e-24, 3.4107651536005483e-25, 1.1219907347116477e-26], [9.460813909935746e-09, 5.2907211789632275e-09, 1.4793510822643465e-09, 2.7576324040642397e-10, 3.8553406458654906e-11, 4.312003724283561e-12, 4.018965254119852e-13, 3.2107211297205396e-14, 2.2443933527375212e-15, 1.3945780937729273e-16, 7.798825689504235e-18, 3.9648147745675937e-19, 1.8476854192253397e-20, 7.948241494310419e-22, 3.1748951902163966e-23, 1.1787917430608492e-24, 5.150694483385207e-26, 1.6943504543512797e-27], [1.3394106551171893e-09, 7.490315725283783e-10, 2.0943849240741161e-10, 3.9041062006526236e-11, 5.458181916838588e-12, 6.104700703546162e-13, 5.689832751345656e-14, 4.5455646128302274e-15, 3.1774902239370283e-16, 1.9743679306817317e-17, 1.1041153885241759e-18, 5.613169443111857e-20, 2.6158526754405844e-21, 1.1252688667455518e-22, 4.494844193257194e-24, 1.6757520438723181e-25, 5.832956348905272e-27, 2.3987693592381086e-28], [1.7847198748015058e-10, 9.980595041841445e-11, 2.7906978231053993e-11, 5.202090862141829e-12, 7.272844747088939e-13, 8.134309394739221e-14, 7.581511731915146e-15, 6.05681273007547e-16, 4.233899389244245e-17, 2.6307791957576357e-18, 1.4711968061810543e-19, 7.479360439217744e-21, 3.4855361509745755e-22, 1.4993831080136075e-23, 5.98922946834433e-25, 2.2328835197122573e-26, 7.804273131493604e-28, 2.5567160053805754e-29]] |
| Legacy trial inputs | {"lambda_home": 2.265193109798798, "lambda_away": 0.5592247378850688, "rho": -0.021895783674930586, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7476 |
| Legacy p draw | 0.1617 |
| Legacy p away | 0.0906 |
| Legacy p over 1 5 | 0.7712 |
| Legacy p under 3 5 | 0.6895 |
| Legacy p btts yes | 0.3860 |
| Legacy p over 2 5 | 0.5350 |
| Legacy goal margin distribution | {"-1": 0.0703552183892846, "-10": 6.712759473083441e-11, "-11": 3.380492054412218e-12, "-12": 1.562776117345859e-13, "-13": 6.676446734178273e-15, "-14": 2.6509705049229353e-16, "-15": 9.830976426031816e-18, "-16": 3.4119238847409953e-19, "-17": 1.0445383162352259e-20, "-2": 0.016975709900344825, "-3": 0.002878024769071647, "-4": 0.00037928890411231727, "-5": 4.075018163451727e-05, "-6": 3.689235048521543e-06, "-7": 2.883195032588627e-07, "-8": 1.9810664265095508e-08, "-9": 1.2140618406572758e-09, "0": 0.16174046863926247, "1": 0.23383208673574332, "10": 6.410837511272643e-05, "11": 1.3077130572265338e-05, "12": 2.448770944277205e-06, "13": 4.237557884704481e-07, "14": 6.815441717174756e-08, "15": 1.0237752460695177e-08, "16": 1.4392166055356038e-09, "17": 1.7847198748015058e-10, "2": 0.22371276718197602, "3": 0.1536300632819288, "4": 0.08201072992996562, "5": 0.035690197039205146, "6": 0.013088038985154257, "7": 0.004143154536413892, "8": 0.0011531213327417985, "9": 0.0002862435009355637} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7607 |
| Legacy raw p draw | 0.1652 |
| Legacy raw p away | 0.0741 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2652 |
| Legacy lambda away | 0.5592 |
| Legacy model home team | Betis |
| Legacy model away team | Malaga |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 87.8% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T07:00:27Z |
| Market reference home draw last update utc | 2026-10-30T07:01:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 29.6% |
| Market draw away odds | 3.47 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T07:00:27Z |
| Market reference draw away last update utc | 2026-10-30T07:01:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.5% |
| Market home away odds | 1.17 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T07:00:27Z |
| Market reference home away last update utc | 2026-10-30T07:01:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.20 |
| Market reference dc home draw odds | 1.08 |
| Market reference dc home away odds | 1.15 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:27Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.13, "price": 1.7, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:27Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.7, "price": 2.13, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:27Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.7, "price": 2.13, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:00:27Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.13, "price": 1.7, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 84.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-30T07:01:04Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 58.2% |
| Market under 3 5 odds | 1.67 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:01:05Z |
| Market reference under 3 5 odds | 1.67 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market reference under 3 5 last update utc | 2026-10-30T07:01:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.7% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T07:00:27Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-30T07:01:04Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 10.079781316510822, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,565.5196 |
| Elo away rating | 1,404.7246 |
| Elo rating diff | 220.7950 |
| Elo home expectancy | 0.7809 |

</details>


---

## 2026-11-01 — Athletic Bilbao vs Real Sociedad

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **46.2%**. Expected goals are 1.55 for Athletic Bilbao and 1.04 for Real Sociedad (2.59 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 47.7%; Under 3.5 goals: 74.1%; Double Chance 1X: 72.3%; Double Chance X2: 53.8%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 46.2% | 2.17 |
| Draw | 26.1% | 3.82 |
| Real Sociedad win | 27.7% | 3.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.55 |
| Real Sociedad expected goals | 1.04 |
| Expected total goals | 2.59 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 73.2% |
| Under 1.5 | 26.8% |
| Over 2.5 | 47.7% |
| Under 2.5 | 52.3% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.45% |
| 2 | 1-0 | 10.69% |
| 3 | 2-1 | 8.89% |
| 4 | 2-0 | 8.55% |
| 5 | 0-1 | 8.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 46.2% | 45.1% | 2.16 | -0.2% |
| Draw | 26.1% | 26.1% | 3.67 | -4.0% |
| Real Sociedad win | 27.7% | 28.8% | 3.34 | -7.6% |

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
| Market best home last update utc | 2026-10-30T07:00:40Z |
| Market best draw last update utc | 2026-10-30T07:00:40Z |
| Market best away last update utc | 2026-10-30T07:00:40Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5459 |
| Dc lambda away | 1.0394 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:00:18.879025+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.66 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.73 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.33 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.17265852073485657, "-10": 3.896383640004132e-08, "-11": 3.63792824275747e-09, "-12": 3.119217094779172e-10, "-13": 2.4718462357822297e-11, "-14": 1.8125957523431498e-12, "-15": 1.1344894283599483e-13, "-2": 0.07429779128727472, "-3": 0.02289393358044159, "-4": 0.005526812194067918, "-5": 0.0010925079714728051, "-6": 0.000182470337487199, "-7": 2.6354530151433044e-05, "-8": 3.3506624489756516e-06, "-9": 3.802754339857483e-07, "0": 0.26149565038929484, "1": 0.22304879361622448, "10": 1.7780801020683193e-06, "11": 2.469160984882553e-07, "12": 3.148810658478569e-08, "13": 3.7113171011515552e-09, "14": 4.0477458494732374e-10, "15": 3.7680651085263064e-11, "2": 0.14158595652929587, "3": 0.06488889240906855, "4": 0.023298626362692195, "5": 0.006849926175125158, "6": 0.001701606824168113, "7": 0.0003655340919818281, "8": 6.912083176127466e-05, "9": 1.1667618342148845e-05} |
| Raw goal margin distribution | {"-1": 0.1566362501411939, "-10": 3.534809170634412e-08, "-11": 3.300337775413562e-09, "-12": 2.8297616997009446e-10, "-13": 2.2424652061807522e-11, "-14": 1.6443914870838418e-12, "-15": 1.0292117013791496e-13, "-2": 0.06740314565119711, "-3": 0.020769434903990667, "-4": 0.0050139381110697444, "-5": 0.0009911260166745731, "-6": 0.0001655375553106016, "-7": 2.390889693473507e-05, "-8": 3.0397295150143203e-06, "-9": 3.4498684308672914e-07, "0": 0.26264638036762966, "1": 0.2348936077932292, "10": 1.8725035152568532e-06, "11": 2.6002836534470157e-07, "12": 3.316025537893803e-08, "13": 3.9084034009802675e-09, "14": 4.262697908372268e-10, "15": 3.968164962436041e-11, "2": 0.149104756868779, "3": 0.06833476118188743, "4": 0.02453587985943327, "5": 0.00721368560800584, "6": 0.001791969189764554, "7": 0.000384945465272349, "8": 7.279143403039515e-05, "9": 1.228721717032611e-05} |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 25.1% |
| Raw p over 1 5 | 73.4% |
| Raw p under 3 5 | 73.9% |
| Raw p btts yes | 51.3% |
| P home draw | 72.3% |
| P draw away | 53.8% |
| P home away | 73.9% |
| Raw p home draw | 74.9% |
| Raw p draw away | 51.4% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4772 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.57, "price": 2.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:40Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:40Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.63, "price": 1.57, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.16 |
| Reference draw odds | 3.67 |
| Reference away odds | 3.34 |
| Market reference 1x2 last update utc | 2026-10-30T07:00:40Z |
| Market reference home last update utc | 2026-10-30T07:00:40Z |
| Market reference draw last update utc | 2026-10-30T07:00:40Z |
| Market reference away last update utc | 2026-10-30T07:00:40Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-30T06:59:54Z |
| Market reference under 2 5 last update utc | 2026-10-30T06:59:54Z |
| Home probability edge | +1.1% |
| Draw probability edge | +0.0% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | 0.0350 |
| Raw ev home | 0.0505 |
| Raw edge prob draw | 0.0016 |
| Raw ev draw | -0.0361 |
| Raw edge prob away | -0.0367 |
| Raw ev away | -0.1616 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10599226257756042, 0.10111615625762944, 0.04648707839799832, 0.013832061780493203, 0.0030867599076889775, 0.0005510725373510493, 8.198481862974072e-05, 1.0454693913376028e-05, 1.1665336133937668e-06, 1.1569928365426775e-07, 1.0327770821150664e-08, 8.380883989264094e-10, 6.234254179309704e-11, 4.280722494964381e-12, 2.7293860107852346e-13], [0.1388535946309178, 0.12562025223937384, 0.06197354741236733, 0.018440004536854276, 0.004115067414044985, 0.0007346540414690667, 0.00010929682439805357, 1.393751750487068e-05, 1.5551466921373935e-06, 1.5424275493797095e-07, 1.3768311898822278e-08, 1.117284908333953e-09, 8.311101929323122e-11, 5.706780629007772e-12, 3.638639793576149e-13], [0.09440034559546007, 0.08426544261593372, 0.03657152649309323, 0.012291506960977507, 0.0027429700282088037, 0.0004896964773831743, 7.285370647368557e-05, 9.290295622621822e-06, 1.0366101783513338e-06, 1.0281320116875847e-07, 9.177508671814752e-09, 7.447457618969039e-10, 5.539910091318001e-11, 3.803954260750242e-12, 2.425398880018965e-13], [0.04194946563728708, 0.03744573462237302, 0.01671276403772407, 0.004835602621145889, 0.0012189163738399215, 0.00021761049094796894, 3.237460664989187e-05, 4.128405828634545e-06, 4.6064707477196583e-07, 4.568795614341202e-08, 4.078285754524953e-09, 3.309488598812062e-10, 2.4618158603497838e-11, 1.69039474951698e-12, 1.0777946450543847e-13], [0.013981074350048991, 0.01248005408160089, 0.005570092325527806, 0.0016573607941141157, 0.00035965048250454016, 7.252603595956016e-05, 1.0789929639137137e-05, 1.3759304906618585e-06, 1.5352617497456005e-07, 1.522705240791074e-08, 1.3592262854494485e-09, 1.1029987023125102e-10, 8.204831708055591e-12, 5.633810661207208e-13, 3.592114187313049e-14], [0.003727731679287046, 0.003327519173019506, 0.0014851369142708907, 0.00044189710901622347, 9.861366303023465e-05, 1.7119483755772765e-05, 2.8768863912771346e-06, 3.6686019615647103e-07, 4.0934220913461366e-08, 4.059943050294563e-09, 3.624064043098242e-10, 2.940892167423771e-11, 2.1876295280005078e-12, 1.502125941903286e-13, 9.577545699566624e-15], [0.000828261543953494, 0.000739338666217281, 0.00032998131288022246, 9.818474430873305e-05, 2.1910886250255328e-05, 3.911702899685015e-06, 5.658980391323925e-07, 8.151235620632303e-08, 9.095139868221774e-09, 9.020753070519736e-10, 8.052277196885001e-11, 6.53434339366673e-12, 4.860675516233769e-13, 3.337560905379768e-14, 2.1280267655759456e-15], [0.00015774062640614385, 0.00014080545594175874, 6.284423003341882e-05, 1.8699072996749245e-05, 4.172881075380584e-06, 7.44975388771266e-07, 1.1083236414868777e-07, 1.3743335060952635e-08, 1.732149790773517e-09, 1.7179829854310185e-10, 1.5335388420543004e-11, 1.2444516198952155e-12, 9.257051788592662e-14, 6.35631283048947e-15, 4.052781122841043e-16], [2.628619211596501e-05, 2.3464083731551343e-05, 1.047247967549598e-05, 3.1160483914742446e-06, 6.953766833796246e-07, 1.2414408790597085e-07, 1.8469311825717e-08, 2.355204355584461e-09, 2.55541939296177e-10, 2.8628788813558293e-11, 2.555517721588292e-12, 2.0737773841067625e-13, 1.542612371247099e-14, 1.0592278223951054e-15, 6.753630033436127e-17], [3.893671172311302e-06, 3.47564325814812e-06, 1.5512475917091477e-06, 4.615681016057601e-07, 1.0300343747119753e-07, 1.838897981723182e-08, 2.7357871657852502e-09, 3.4886724040457586e-10, 3.892656886139717e-11, 3.754284609326296e-12, 3.7853887847207863e-13, 3.071805601460054e-14, 2.2850115731778375e-15, 1.5689928837068028e-16, 1.0003888906250074e-17], [5.190788996019e-07, 4.633501387271351e-07, 2.0680223297759873e-07, 6.15332552930077e-08, 1.3731747908754224e-08, 2.4514991086584454e-09, 3.647173396817268e-10, 4.650870996609173e-11, 5.189436815707596e-12, 5.146993753567749e-13, 4.467630206995312e-14, 4.095131306248259e-15, 3.0462287144774034e-16, 2.0916791981544988e-17, 1.3336533609009074e-18], [6.29092914414978e-08, 5.615529534912555e-08, 2.5063207067592135e-08, 7.457466472901763e-09, 1.6642066010687742e-09, 2.971071873918293e-10, 4.4201583677167676e-11, 5.636580473737001e-12, 6.28929038161567e-13, 6.237851901494959e-14, 5.568150711064707e-15, 4.3938160806996365e-16, 3.691848968306951e-17, 2.5349914315480328e-18, 1.6163089662707057e-19], [6.988881086570156e-09, 6.238548751438942e-09, 2.7843863732971604e-09, 8.284840790912789e-10, 1.848843274474153e-10, 3.300699713933025e-11, 4.9105562164069775e-12, 6.261935202761722e-13, 6.987060510274097e-14, 6.929915148658974e-15, 6.185913447764906e-16, 5.01980764979545e-17, 3.631026408050801e-18, 2.8162379935623753e-19, 1.7956315999724675e-20], [7.167016468363952e-10, 6.397559364140919e-10, 2.8553559210008463e-10, 8.496008109273091e-11, 1.8959673274514194e-11, 3.384829261487923e-12, 5.035718427008967e-13, 6.421541898639759e-14, 7.165149488494909e-15, 7.10654758316657e-16, 6.343582470904882e-17, 5.147754504399406e-18, 3.8292392633310166e-19, 2.5567762796280042e-20, 1.8413993726187575e-21], [6.824714218811729e-11, 6.092006980990161e-11, 2.7189819138606107e-11, 8.090232191099155e-12, 1.8054144615372866e-12, 3.2231671981074555e-13, 4.795208620273412e-14, 6.114844091093068e-15, 6.822936407345166e-16, 6.767133374338454e-17, 6.040608065921203e-18, 4.901893767958159e-19, 3.646351834552565e-20, 2.5037510299992512e-21, 1.552339408204001e-22]] |
| Legacy trial inputs | {"lambda_home": 1.3331349172297269, "lambda_away": 0.8926391326684533, "rho": -0.021895783674930586, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4589 |
| Legacy p draw | 0.2734 |
| Legacy p away | 0.2677 |
| Legacy p over 1 5 | 0.6540 |
| Legacy p under 3 5 | 0.8145 |
| Legacy p btts yes | 0.4349 |
| Legacy p over 2 5 | 0.3875 |
| Legacy goal margin distribution | {"-1": 0.1766756132006825, "-10": 1.1502181146289187e-08, "-11": 9.251111519448962e-10, "-12": 6.829186231010671e-11, "-13": 4.644586474321996e-12, "-14": 2.7293860107852346e-13, "-2": 0.06789882951336935, "-3": 0.01847061806090321, "-4": 0.0038985537293611972, "-5": 0.000670135900533292, "-6": 9.700602339680465e-05, "-7": 1.2116844613717352e-05, "-8": 1.330293183035763e-06, "-9": 1.3023753243220224e-07, "0": 0.27339699379814925, "1": 0.24159180067163502, "10": 5.781053468198769e-07, "11": 6.944146601722792e-08, "12": 7.655826842122853e-09, "13": 7.776217166462969e-10, "14": 6.824714218811729e-11, "2": 0.13788074433744762, "3": 0.05601714118556268, "4": 0.017657988045033175, "5": 0.004533136123700809, "6": 0.0009800150815029046, "7": 0.00018281918870798226, "8": 2.997628339067243e-05, "9": 4.382932284175115e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4664 |
| Legacy raw p draw | 0.2858 |
| Legacy raw p away | 0.2478 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3331 |
| Legacy lambda away | 0.8926 |
| Legacy model home team | Ath Bilbao |
| Legacy model away team | Sociedad |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 10.303210650139496, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,505.1233 |
| Elo away rating | 1,510.6645 |
| Elo rating diff | 54.4588 |
| Elo home expectancy | 0.5777 |

</details>


---

## 2026-11-01 — Elche CF vs Valencia

The model's most likely 1X2 outcome is **Elche CF win** at **43.4%**. Expected goals are 1.49 for Elche CF and 1.07 for Valencia (2.56 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 47.4%; Under 3.5 goals: 74.0%; Double Chance 1X: 71.0%; Double Chance X2: 56.6%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 88.1%; BTTS Yes (both teams score): 52.2%; BTTS No (at least one team does not score): 47.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 43.4% | 2.31 |
| Draw | 27.6% | 3.62 |
| Valencia win | 29.0% | 3.45 |

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
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 11.9% |
| Under 4.5 | 88.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.14% |
| 2 | 1-0 | 10.14% |
| 3 | 2-1 | 8.57% |
| 4 | 0-1 | 8.37% |
| 5 | 0-0 | 8.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 43.4% | 42.0% | 2.32 | +0.6% |
| Draw | 27.6% | 28.0% | 3.44 | -5.1% |
| Valencia win | 29.0% | 30.0% | 3.21 | -6.8% |
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
| Market best home last update utc | 2026-10-30T07:00:40Z |
| Market best draw last update utc | 2026-10-30T07:00:40Z |
| Market best away last update utc | 2026-10-30T07:00:40Z |
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
| Dc lambda home | 1.4930 |
| Dc lambda away | 1.0662 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:00:18.879025+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.2% |
| P btts no | 47.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.17 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.74 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.38 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.17785238586132923, "-10": 5.582196026253363e-08, "-11": 5.410555468254882e-09, "-12": 4.816027880475307e-10, "-13": 3.96210764027075e-11, "-14": 3.0159110402532012e-12, "-15": 1.9570950252684461e-13, "-2": 0.07919604778782309, "-3": 0.025298870609659702, "-4": 0.0063348793832551315, "-5": 0.00129927785881721, "-6": 0.0002251978358365596, "-7": 3.3757846274753815e-05, "-8": 4.454861260866406e-06, "-9": 5.24821982091299e-07, "0": 0.275948842164428, "1": 0.21373348845435336, "10": 1.378468808770891e-06, "11": 1.8708255395520207e-07, "12": 2.3317393655890466e-08, "13": 2.6860671052906686e-09, "14": 2.862916564834342e-10, "15": 2.6013671596707054e-11, "2": 0.1323423254048841, "3": 0.05919649079673697, "4": 0.020755478717050864, "5": 0.005960682892051388, "6": 0.001446631005214101, "7": 0.00030364620911819, "8": 5.61082717256473e-05, "9": 9.255594118682386e-06} |
| Raw goal margin distribution | {"-1": 0.1640548245479437, "-10": 4.674855466695466e-08, "-11": 4.477867727266562e-09, "-12": 3.93882146308361e-10, "-13": 3.202152769042543e-11, "-14": 2.409082204163062e-12, "-15": 1.5481286426027277e-13, "-2": 0.07248210831829062, "-3": 0.0229328233988099, "-4": 0.005682630183057963, "-5": 0.001152801805402991, "-6": 0.0001975727119771052, "-7": 2.9279344772487773e-05, "-8": 3.81931275654036e-06, "-9": 4.4471815463965334e-07, "0": 0.2671558449669275, "1": 0.23132204302802697, "10": 1.3544530271984455e-06, "11": 1.816630479911398e-07, "12": 2.2374905392830634e-08, "13": 2.5470445158668446e-09, "14": 2.6831545166076976e-10, "15": 2.414352541494663e-11, "2": 0.14211174406231836, "3": 0.06295877287377954, "4": 0.021844781128880855, "5": 0.006205153479801972, "6": 0.0014891018979872822, "7": 0.0003089999332324815, "8": 5.6439327636130194e-05, "9": 9.201974869031746e-06} |
| Unadjusted home-win probability | 46.6% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 72.9% |
| Raw p under 3 5 | 74.5% |
| Raw p btts yes | 51.2% |
| P home draw | 71.0% |
| P draw away | 56.6% |
| P home away | 72.4% |
| Raw p home draw | 73.3% |
| Raw p draw away | 53.4% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0122 |
| Totals anchor target over 2 5 | 0.4745 |
| Totals anchor reference over odds | 2.04 |
| Totals anchor reference under odds | 1.85 |
| Totals anchor reference last update utc | 2026-10-30T07:00:40Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4673 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:40Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:40Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.32 |
| Reference draw odds | 3.44 |
| Reference away odds | 3.21 |
| Market reference 1x2 last update utc | 2026-10-30T07:00:40Z |
| Market reference home last update utc | 2026-10-30T07:00:40Z |
| Market reference draw last update utc | 2026-10-30T07:00:40Z |
| Market reference away last update utc | 2026-10-30T07:00:40Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-30T07:00:40Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:00:40Z |
| Market best over 2 5 last update utc | 2026-10-30T07:00:40Z |
| Market best under 2 5 last update utc | 2026-10-30T07:00:40Z |
| Home probability edge | +1.4% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0464 |
| Raw ev home | 0.0818 |
| Raw edge prob draw | -0.0126 |
| Raw ev draw | -0.0810 |
| Raw edge prob away | -0.0339 |
| Raw ev away | -0.1444 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09323908726936528, 0.0960847357235366, 0.05640121876216602, 0.021463364023500665, 0.006125878198854512, 0.0013987139636121404, 0.00026613881423692763, 4.3405097388086204e-05, 6.194144112677332e-06, 7.857227959619807e-07, 8.970154242096235e-08, 9.309744947352864e-09, 8.857009172690933e-10, 7.778113918802412e-11, 6.342738715306144e-12], [0.11596644362276505, 0.13270117934641446, 0.07097053895650461, 0.02700768788332109, 0.007708288701843473, 0.0017600237374680824, 0.00033488664780963764, 5.4617315417985935e-05, 7.794188772847148e-06, 9.88687328459637e-07, 1.1287285896587556e-07, 1.1714598211917332e-08, 1.1144913679600076e-09, 9.787322845101186e-11, 7.981167693977636e-12], [0.074831781894238, 0.08543122705004227, 0.04663675839113019, 0.016992098815550017, 0.004849730339241674, 0.0011073327488814923, 0.00021069656299989482, 3.436291268737656e-05, 4.903775043144617e-06, 6.220403929224635e-07, 7.101484515919071e-08, 7.37033141308975e-09, 7.011909918119672e-10, 6.157770988843308e-11, 5.0214142989742974e-12], [0.03138733528971304, 0.03583315136636816, 0.020454344483105562, 0.007443994072946098, 0.002034163939028065, 0.00046445806028707183, 8.837426424796999e-05, 1.4413130821529596e-05, 2.0568323721335653e-06, 2.609077304078677e-07, 2.978636481901284e-08, 3.0914012389268668e-09, 2.9410654410493577e-10, 2.582806633380125e-11, 2.1061748129052822e-12], [0.009873794178600754, 0.011272354218554003, 0.006434505689005518, 0.002448637475313797, 0.0006683534713646607, 0.00014610871708404323, 2.780068100128638e-05, 4.534067192625678e-06, 6.470361155184145e-07, 8.207607322745401e-08, 9.37016260975929e-09, 9.724896769634097e-10, 9.251972033520945e-11, 8.124965329400936e-12, 6.625582074689667e-13], [0.002484870042811756, 0.002836836053394116, 0.0016193279035088685, 0.0006162317947947875, 0.00017587927563643315, 3.84048763764503e-05, 6.996406663973237e-06, 1.1410575848814956e-06, 1.6283514026994246e-07, 2.0655522274966707e-08, 2.3581245409923343e-09, 2.4473980533919837e-10, 2.3283803295043305e-11, 2.0447542839882913e-12, 1.6674147866347406e-13], [0.0005211251637394297, 0.0005949392231209412, 0.00033960428687409416, 0.00012923569016933252, 3.68852755819359e-05, 8.42196797477673e-06, 1.5325125608049115e-06, 2.393017785689223e-07, 3.414966886545351e-08, 4.331861321602688e-09, 4.945441879737339e-10, 5.132665649855388e-11, 4.883062532669165e-12, 4.288244023597099e-13, 3.496890335252039e-14], [9.367713916745892e-05, 0.00010694590911819265, 6.104705789889129e-05, 2.3231328240845727e-05, 6.630474470134758e-06, 1.5139277872820714e-06, 2.8806100219881227e-07, 4.492914300890929e-08, 6.138723487993562e-09, 7.786927289521789e-10, 8.889895929960862e-11, 9.226448228509515e-12, 8.777763199034012e-13, 7.708521102684475e-14, 6.2859885759142035e-15], [1.4734426845129043e-05, 1.6821464535450044e-05, 9.60205890909649e-06, 3.654043126445393e-06, 1.0429037638954025e-06, 2.381248875527638e-07, 4.530896013215738e-08, 7.389526524824835e-09, 1.008482422244844e-09, 1.224801605978742e-10, 1.3982869503162675e-11, 1.4512230803752839e-12, 1.3806496533677273e-13, 1.2124691390137251e-14, 9.887197628394138e-16], [2.060062288968091e-06, 2.3518569876473054e-06, 1.3424912731925493e-06, 5.108822030319897e-07, 1.4581135307166978e-07, 3.329292045549667e-08, 6.334775088416318e-09, 1.033150803022481e-09, 1.474362540148587e-10, 1.7885598858643226e-11, 1.9549849110384682e-12, 2.0289964259787591e-13, 1.9303257025704907e-14, 1.6951877233321116e-15, 1.38235733170462e-16], [2.5922087171298765e-07, 2.9593785670801085e-07, 1.6892778435275828e-07, 6.428510959197273e-08, 1.8347671452119828e-08, 4.189300444244324e-09, 7.971146937248905e-10, 1.3000298738763476e-10, 1.85521352885758e-11, 2.3533252286091987e-12, 2.5693523057584117e-13, 2.553118054057525e-14, 2.4289591338568424e-15, 2.1330813233779427e-16, 1.7394419307719366e-17], [2.965288110306258e-08, 3.3853022794298965e-08, 1.932404389860388e-08, 7.353723868110146e-09, 2.0988330009558635e-09, 4.792238647963788e-10, 9.118381202227884e-11, 1.4871345438251356e-11, 2.1222220968733326e-12, 2.6920237070281344e-13, 3.073331714381176e-14, 3.0504117132599964e-15, 2.778543098188577e-16, 2.440081558529858e-17, 1.989788261184896e-18], [3.1093904819854703e-09, 3.5498158339885147e-09, 2.0263123155875248e-09, 7.711088485189211e-10, 2.200828760539947e-10, 5.025124266202427e-11, 9.561501839493879e-12, 1.5594039513159144e-12, 2.225354482669697e-13, 2.822846408353893e-14, 3.2226846178848853e-15, 3.344688511315314e-16, 3.0430994103290305e-17, 2.558660774644728e-18, 2.0864848373387002e-19], [3.009688349838439e-10, 3.4359915300201197e-10, 1.9613389198592205e-10, 7.463833607552592e-11, 2.1302595215885793e-11, 4.8639944220909054e-12, 9.254913739527553e-13, 1.5094019011631704e-13, 2.1539988301742768e-14, 2.732332268278196e-15, 3.1193497265284946e-16, 3.237441583701102e-17, 3.080003798712542e-18, 2.5867211100542804e-19, 2.0195820188666093e-20], [2.705098640558724e-11, 3.088258628946636e-11, 1.76284539429835e-11, 6.708470711338223e-12, 1.9146707120675404e-12, 4.371743240322417e-13, 8.318288030263382e-14, 1.3566457906222839e-14, 1.936007529677384e-15, 2.455811846721887e-16, 2.803661948956417e-17, 2.9098025473063496e-18, 2.768297949938988e-19, 2.431084398354612e-20, 1.895892497885167e-21]] |
| Legacy trial inputs | {"lambda_home": 1.2583156980308323, "lambda_away": 1.1416436290503518, "rho": -0.021895783674930586, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T07:00:40Z", "over": 2.04, "under": 1.85, "bookmaker": "pinnacle", "event_id": "5262991e389930615bec34b642428c93", "kickoff_utc": "2026-11-01T17:30:00Z", "home_team": "Elche CF", "away_team": "Valencia"}} |
| Legacy p home | 0.4036 |
| Legacy p draw | 0.2807 |
| Legacy p away | 0.3156 |
| Legacy p over 1 5 | 0.6947 |
| Legacy p under 3 5 | 0.7785 |
| Legacy p btts yes | 0.4898 |
| Legacy p over 2 5 | 0.4308 |
| Legacy goal margin distribution | {"-1": 0.18623488812333033, "-10": 1.021438222492329e-07, "-11": 1.0487920200014211e-08, "-12": 9.885955600190793e-10, "-13": 8.576230688200176e-11, "-14": 6.342738715306144e-12, "-2": 0.08875207172615183, "-3": 0.030372061063037522, "-4": 0.008111679825692227, "-5": 0.0017701048428957523, "-6": 0.0003259304322920176, "-7": 5.1852109127265476e-05, "-8": 7.257032286978609e-06, "-9": 9.062683845918591e-07, "0": 0.28072935589592896, "1": 0.22448524947518725, "10": 2.9517675982966175e-07, "11": 3.3405539299748354e-08, "12": 3.4706180889304655e-09, "13": 3.3185142127331025e-10, "14": 2.705098640558724e-11, "2": 0.11775411630871122, "3": 0.04441512816823176, "4": 0.013074542856005495, "5": 0.003144660460376551, "6": 0.0006382028505794458, "7": 0.00011190753010899493, "8": 1.726279037105057e-05, "9": 2.376117038192764e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3874 |
| Legacy raw p draw | 0.2817 |
| Legacy raw p away | 0.3308 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2583 |
| Legacy lambda away | 1.1416 |
| Legacy model home team | Elche |
| Legacy model away team | Valencia |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 9.234617494310402, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,471.9746 |
| Elo away rating | 1,446.4037 |
| Elo rating diff | 85.5709 |
| Elo home expectancy | 0.6207 |

</details>


---

## 2026-11-01 — Getafe vs Sevilla

The model's most likely 1X2 outcome is **Sevilla win** at **35.9%**. Expected goals are 1.02 for Getafe and 0.92 for Sevilla (1.94 combined). The most likely exact score is 0-1 at 14.7%. Goal-market probabilities: at least one goal: 85.3%; Over 2.5 goals: 30.7%; Under 3.5 goals: 86.8%; Double Chance 1X: 64.1%; Double Chance X2: 67.9%; Double Chance 12 (either team wins): 68.0%; Under 4.5 goals: 95.3%; BTTS Yes (both teams score): 38.9%; BTTS No (at least one team does not score): 61.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Getafe win | 32.1% | 3.11 |
| Draw | 32.0% | 3.13 |
| Sevilla win | 35.9% | 2.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Getafe expected goals | 1.02 |
| Sevilla expected goals | 0.92 |
| Expected total goals | 1.94 |
| Over 0.5 | 85.3% |
| Under 0.5 | 14.7% |
| Over 1.5 | 58.1% |
| Under 1.5 | 41.9% |
| Over 2.5 | 30.7% |
| Under 2.5 | 69.3% |
| Over 3.5 | 13.2% |
| Under 3.5 | 86.8% |
| Over 4.5 | 4.7% |
| Under 4.5 | 95.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.71% |
| 2 | 0-0 | 14.70% |
| 3 | 1-1 | 13.82% |
| 4 | 1-0 | 12.48% |
| 5 | 1-2 | 7.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Getafe win | 32.1% | 30.2% | 3.20 | +2.8% |
| Draw | 32.0% | 31.9% | 3.03 | -3.0% |
| Sevilla win | 35.9% | 37.9% | 2.56 | -8.2% |

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
| Market best home last update utc | 2026-10-30T07:00:40Z |
| Market best draw last update utc | 2026-10-30T07:00:40Z |
| Market best away last update utc | 2026-10-30T07:00:40Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Getafe |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0239 |
| Dc lambda away | 0.9165 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:00:18.879025+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 38.9% |
| P btts no | 61.1% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.80 |
| Fair Over 1.5 odds | 1.72 |
| Fair Under 1.5 odds | 2.39 |
| Fair Over 2.5 odds | 3.25 |
| Fair Under 2.5 odds | 1.44 |
| Fair Over 3.5 odds | 7.59 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 21.11 |
| Fair Under 4.5 odds | 1.05 |
| Goal margin distribution | {"-1": 0.2305889560107072, "-10": 2.082147091811354e-08, "-11": 1.722443932713548e-09, "-12": 1.3046937271141766e-10, "-13": 8.578389408250524e-12, "-2": 0.09427243510402453, "-3": 0.026794644388476445, "-4": 0.005871687505034126, "-5": 0.001044262455309304, "-6": 0.0001560724485251613, "-7": 2.0100738754280664e-05, "-8": 2.2733449759487435e-06, "-9": 2.2912133251896178e-07, "0": 0.3199910255611152, "1": 0.19537764809558436, "10": 4.7755142348029075e-08, "11": 4.41385254939696e-09, "12": 3.7354703249371165e-10, "13": 2.744141252874663e-11, "2": 0.08903926087401534, "3": 0.02827540329666795, "4": 0.006922894831403825, "5": 0.0013756199118191486, "6": 0.00022970953512329675, "7": 3.305436266781213e-05, "8": 4.176823294423281e-06, "9": 4.7033822311064794e-07} |
| Raw goal margin distribution | {"-1": 0.19947068319599223, "-10": 1.801158694256258e-08, "-11": 1.4899979338525187e-09, "-12": 1.1286236496812359e-10, "-13": 7.420724849916665e-12, "-2": 0.0815502501163865, "-3": 0.023178673058023107, "-4": 0.005079295810195451, "-5": 0.0009033379091529384, "-6": 0.0001350102731456908, "-7": 1.7388118500672437e-05, "-8": 1.966554180815217e-06, "-9": 1.9820111736058702e-07, "0": 0.32235882484215117, "1": 0.22338119382013288, "10": 5.4599903380627355e-08, "11": 5.046491558481472e-09, "12": 4.2708765756864056e-10, "13": 3.1374599656268014e-11, "2": 0.1018012888617084, "3": 0.03232812660875795, "4": 0.007915155736615529, "5": 0.0015727879884938193, "6": 0.0002626338820631421, "7": 3.7792055875742645e-05, "8": 4.775488818595825e-06, "9": 5.377519629384415e-07} |
| Unadjusted home-win probability | 36.7% |
| Unadjusted draw probability | 32.2% |
| Unadjusted away-win probability | 31.0% |
| Raw p over 1 5 | 58.2% |
| Raw p under 3 5 | 86.8% |
| Raw p btts yes | 38.9% |
| P home draw | 64.1% |
| P draw away | 67.9% |
| P home away | 68.0% |
| Raw p home draw | 69.0% |
| Raw p draw away | 63.3% |
| Raw p home away | 67.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3074 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:40Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.78, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:40Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.17, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.20 |
| Reference draw odds | 3.03 |
| Reference away odds | 2.56 |
| Market reference 1x2 last update utc | 2026-10-30T07:00:40Z |
| Market reference home last update utc | 2026-10-30T07:00:40Z |
| Market reference draw last update utc | 2026-10-30T07:00:40Z |
| Market reference away last update utc | 2026-10-30T07:00:40Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.72 |
| Reference Under 2.5 odds | 1.47 |
| Market reference over 2 5 last update utc | 2026-10-30T07:00:42Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:00:42Z |
| Home probability edge | +2.0% |
| Draw probability edge | +0.1% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | 0.0658 |
| Raw ev home | 0.1754 |
| Raw edge prob draw | 0.0034 |
| Raw ev draw | -0.0233 |
| Raw edge prob away | -0.0692 |
| Raw ev away | -0.2055 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.14016682588055906, 0.13882142678511175, 0.06789043688974176, 0.02163176770733113, 0.005169358847666794, 0.000988260275627669, 0.00015744350527217586, 2.149964911389003e-05, 2.568893186915859e-06, 2.728400995786697e-07, 2.6080316723765292e-08, 2.266338820504207e-09, 1.805295309517355e-10, 1.3274236878288617e-11], [0.12651159519853455, 0.1390028589242681, 0.07042120897631106, 0.022438141570939846, 0.005362058580891105, 0.0010250999489955935, 0.00016331257382746537, 2.2301097953243263e-05, 2.6646545852610077e-06, 2.830108414348739e-07, 2.705252047730108e-08, 2.3508218093963736e-09, 1.8725918417927473e-10, 1.3769064569803406e-11], [0.06701644386951226, 0.06405986819812608, 0.033717601158604546, 0.011637287436914135, 0.002780970819803416, 0.0005316564529335959, 8.470021270183428e-05, 1.1566211320138262e-05, 1.3819928549222855e-06, 1.4678036053600873e-07, 1.4030482680218324e-08, 1.2192270479451428e-09, 9.711985034975366e-11, 7.141169050459874e-12], [0.023171545285770298, 0.02214928234395076, 0.010586059373720792, 0.0037146140305344966, 0.0009615459664638513, 0.00018382505642361056, 2.928586927346334e-05, 3.999122810980679e-06, 4.778366050695638e-07, 5.075064528706052e-08, 4.851167057430152e-09, 4.2155884621549266e-10, 3.358007200304956e-11, 2.469124180451333e-12], [0.006008829474478776, 0.005743736938796885, 0.002745169767441397, 0.0008746868844417947, 0.00023019360121891098, 4.766938948453457e-05, 7.594391841625892e-06, 1.0370498265145065e-06, 1.2391226571712953e-07, 1.3160623061120501e-08, 1.2580013650711398e-09, 1.0931835529857757e-10, 8.707961593349386e-12, 6.40291614938404e-13], [0.0012465644809813406, 0.001191569587124249, 0.000569500456102241, 0.00018145856971918015, 4.336328290659778e-05, 9.129621518735304e-06, 1.5754980507657848e-06, 2.1514164850767084e-07, 2.57062760487631e-08, 2.7302431072900114e-09, 2.6097925151383196e-10, 2.2678689653832422e-11, 1.8065141755350983e-12, 1.32831991329165e-13], [0.00021550550622272273, 0.00020599801373343942, 9.845498244083375e-05, 3.1370475833707403e-05, 7.496624825142419e-06, 1.4331789945897013e-06, 2.514489392901944e-07, 3.7193591329296586e-08, 4.444089429396046e-09, 4.720031991320958e-10, 4.5117975499221306e-11, 3.920681656571554e-12, 3.1230935730716004e-13, 2.2963934855121636e-14], [3.1934138474787954e-05, 3.0525294742567975e-05, 1.4589302602547116e-05, 4.648554632558959e-06, 1.1108683924401238e-06, 2.1237200512679631e-07, 3.3833792304974415e-08, 5.088072172442146e-09, 6.585361539950807e-10, 6.99426004737413e-11, 6.685693106166706e-12, 5.809762967593061e-13, 4.627877235262632e-14, 3.402852615893589e-15], [4.1405696111953036e-06, 3.957899408610739e-06, 1.8916440489644441e-06, 6.02730023944464e-07, 1.4403482064832803e-07, 2.7536082471455017e-08, 4.386878085346587e-09, 5.99048778654405e-10, 7.882660533560563e-11, 9.068733959370433e-12, 8.668647105362566e-13, 7.532919045508524e-14, 6.0004899959331765e-15, 4.4121272110939563e-16], [4.77213206764138e-07, 4.5615991184550244e-07, 2.180177143313437e-07, 6.946646344547986e-08, 1.6600449962594285e-08, 3.1736170266031066e-09, 5.056010055068776e-10, 6.904218875993792e-11, 8.249530370269021e-12, 9.649111841935925e-13, 9.990878724201715e-14, 8.681917686595828e-15, 6.915746725699316e-16, 5.085110438342889e-17], [4.950024259583272e-08, 4.7316432107894663e-08, 2.2614482576389312e-08, 7.205598554453514e-09, 1.7219269892388713e-09, 3.2919208960778604e-10, 5.244484451507885e-11, 7.161589504486091e-12, 8.557050577014616e-13, 9.088375271590655e-14, 9.567244554405191e-15, 9.005556124433728e-16, 7.173547081287055e-17, 5.274669618458059e-18], [4.667770719889978e-09, 4.4618418977503464e-09, 2.132499035962681e-09, 6.794730730186608e-10, 1.6237416143156778e-10, 3.104213467470931e-11, 4.9454406039067905e-12, 6.753231104310955e-13, 8.069122096660007e-14, 8.570150318349028e-15, 8.192059562284902e-16, 7.839728813858485e-17, 6.7645068524579106e-18, 4.973904593389718e-19], [4.034810502259744e-10, 3.856806091986022e-10, 1.8433273660373382e-10, 5.873349946980715e-11, 1.4035585960724972e-11, 2.6832751331245913e-12, 4.274827724917733e-13, 5.837477763797118e-14, 6.9749309752702146e-15, 7.408018642191232e-16, 7.081197843801456e-17, 6.153450412070367e-18, 5.398064669280444e-19, 4.299431933349084e-20], [3.219397952354218e-11, 3.0773672340282175e-11, 1.4708012543378353e-11, 4.6863788973929414e-12, 1.1199072837929451e-12, 2.141000293408126e-13, 3.4109090418396134e-14, 4.657756281033864e-15, 5.565336584461824e-16, 5.910899665378389e-17, 5.650127515476048e-18, 4.909872631053554e-19, 3.9110524653134776e-20, 3.16702078480139e-21]] |
| Legacy trial inputs | {"lambda_home": 1.0372772985785823, "lambda_away": 0.9558828326202609, "rho": -0.021895783674930586, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3328 |
| Legacy p draw | 0.3168 |
| Legacy p away | 0.3504 |
| Legacy p over 1 5 | 0.5945 |
| Legacy p under 3 5 | 0.8587 |
| Legacy p btts yes | 0.4009 |
| Legacy p over 2 5 | 0.3206 |
| Legacy goal margin distribution | {"-1": 0.22189075191363314, "-10": 2.8530727507691873e-08, "-11": 2.460739173733942e-09, "-12": 1.9429859552153891e-10, "-13": 1.3274236878288617e-11, "-2": 0.09330118838530642, "-3": 0.027555831845296776, "-4": 0.00628328482038903, "-5": 0.0011636303229500566, "-6": 0.0001811786277213954, "-7": 2.431604637457789e-05, "-8": 2.8663649106707516e-06, "-9": 3.011460674675339e-07, "0": 0.3168414798335164, "1": 0.20207704055790676, "10": 5.415110360908419e-08, "11": 5.068159341631959e-09, "12": 4.3425472256625657e-10, "13": 3.219397952354218e-11, "2": 0.09210006800423849, "3": 0.02951729207382208, "4": 0.007303649860241295, "5": 0.001467771461987696, "6": 0.0002479936648789651, "7": 3.6117426287830136e-05, "8": 4.620037728376204e-06, "9": 5.26721991314749e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3640 |
| Legacy raw p draw | 0.3147 |
| Legacy raw p away | 0.3213 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0373 |
| Legacy lambda away | 0.9559 |
| Legacy model home team | Getafe |
| Legacy model away team | Sevilla |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p over 1 5 | 61.6% |
| Market reference over 1 5 odds | 1.57 |
| Market reference over 1 5 opposite odds | 2.44 |
| Market reference over 1 5 last update utc | 2026-10-30T07:00:45Z |
| Market over 1 5 bookmakers | 0 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 8.569664528102011, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,449.4205 |
| Elo away rating | 1,481.9065 |
| Elo rating diff | 27.5140 |
| Elo home expectancy | 0.5395 |

</details>


---

## 2026-11-01 — Real Racing Club de Santander vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **81.5%**. Expected goals are 1.19 for Real Racing Club de Santander and 3.49 for Real Madrid (4.68 combined). The most likely exact score is 1-3 at 8.0%. Goal-market probabilities: at least one goal: 99.0%; Over 2.5 goals: 84.9%; Under 3.5 goals: 31.0%; Double Chance 1X: 18.5%; Double Chance X2: 92.2%; Double Chance 12 (either team wins): 89.3%; Under 4.5 goals: 49.4%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 7.8% | 12.86 |
| Draw | 10.7% | 9.35 |
| Real Madrid win | 81.5% | 1.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.19 |
| Real Madrid expected goals | 3.49 |
| Expected total goals | 4.68 |
| Over 0.5 | 99.0% |
| Under 0.5 | 1.0% |
| Over 1.5 | 95.0% |
| Under 1.5 | 5.0% |
| Over 2.5 | 84.9% |
| Under 2.5 | 15.1% |
| Over 3.5 | 69.0% |
| Under 3.5 | 31.0% |
| Over 4.5 | 50.6% |
| Under 4.5 | 49.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-3 | 7.97% |
| 2 | 1-4 | 6.96% |
| 3 | 1-2 | 6.85% |
| 4 | 0-3 | 6.71% |
| 5 | 0-4 | 5.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 7.8% | 7.4% | 11.19 | -13.0% |
| Draw | 10.7% | 10.4% | 8.20 | -12.3% |
| Real Madrid win | 81.5% | 82.2% | 1.20 | -2.2% |

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
| Market best home last update utc | 2026-10-30T07:00:40Z |
| Market best draw last update utc | 2026-10-30T07:00:40Z |
| Market best away last update utc | 2026-10-30T07:00:40Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santander |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1885 |
| Dc lambda away | 3.4930 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:00:18.879025+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 67.2% |
| P btts no | 32.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 101.52 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 19.84 |
| Fair Over 2.5 odds | 1.18 |
| Fair Under 2.5 odds | 6.62 |
| Fair Over 3.5 odds | 1.45 |
| Fair Under 3.5 odds | 3.23 |
| Fair Over 4.5 odds | 1.98 |
| Fair Under 4.5 odds | 2.02 |
| Goal margin distribution | {"-1": 0.16785365340383557, "-10": 0.0010203667923870052, "-11": 0.0003143766622879493, "-12": 8.918834990470116e-05, "-13": 2.3439768877688738e-05, "-14": 5.736718042882314e-06, "-15": 1.3135076090426705e-06, "-16": 2.825005751012846e-07, "-17": 5.727758608941503e-08, "-18": 1.0982527684252258e-08, "-19": 1.9953646621002816e-09, "-2": 0.1923771514080151, "-20": 3.398637832067007e-10, "-21": 4.719998692170401e-11, "-3": 0.17335051262819232, "-4": 0.12782848036140454, "-5": 0.07926032314440225, "-6": 0.04224155274786639, "-7": 0.01969490337488034, "-8": 0.00814942756261092, "-9": 0.0030281410086215746, "0": 0.1069734095128672, "1": 0.05001124415736954, "10": 1.885839481017053e-08, "11": 1.9769384106439603e-09, "12": 1.9082945196228987e-10, "13": 1.706416463052414e-11, "14": 1.420985497617377e-12, "15": 1.1070141364210911e-13, "16": 8.100920000305015e-15, "17": 5.588485740206347e-16, "18": 3.645911985428362e-17, "19": 2.2538270322212646e-18, "2": 0.01979458637092063, "20": 1.3061637530261976e-19, "21": 6.172044543617673e-21, "3": 0.006068935263732522, "4": 0.0015226827716983344, "5": 0.00032124182154854875, "6": 5.825196077909485e-05, "7": 9.24099982880474e-06, "8": 1.301028004526874e-06, "9": 1.6448642777866386e-07} |
| Raw goal margin distribution | {"-1": 0.16469291678201362, "-10": 0.001001152967587914, "-11": 0.0003084568517304213, "-12": 8.750890547160655e-05, "-13": 2.2998390722394674e-05, "-14": 5.628693853718072e-06, "-15": 1.2887738512795638e-06, "-16": 2.771810012028234e-07, "-17": 5.619903128711463e-08, "-18": 1.0775723264164514e-08, "-19": 1.9577913234597675e-09, "-2": 0.18875462967359566, "-20": 3.334640422166852e-10, "-21": 4.631119645341422e-11, "-3": 0.17008626843353472, "-4": 0.12542143022578378, "-5": 0.07776782655025762, "-6": 0.04144613114085742, "-7": 0.019324042204462665, "-8": 0.007995971301030132, "-9": 0.0029711201694089533, "0": 0.11424043417667422, "1": 0.0552087236332979, "10": 2.0818276465311716e-08, "11": 2.182394143402057e-09, "12": 2.1066163523802843e-10, "13": 1.8837578728400427e-11, "14": 1.5686631465920396e-12, "15": 1.222061929183578e-13, "16": 8.942817980391931e-15, "17": 6.169275929005533e-16, "18": 4.02481783019553e-17, "19": 2.488058752300086e-18, "2": 0.02185176287454079, "20": 1.4419084123110811e-19, "21": 6.813481791989777e-21, "3": 0.00669965675457829, "4": 0.0016809294337759388, "5": 0.00035462726921017015, "6": 6.430586676930037e-05, "7": 1.0201381993986138e-05, "8": 1.43623892489227e-06, "9": 1.8158088017337402e-07} |
| Unadjusted home-win probability | 8.6% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 80.0% |
| Raw p over 1 5 | 94.9% |
| Raw p under 3 5 | 31.3% |
| Raw p btts yes | 67.5% |
| P home draw | 18.5% |
| P draw away | 92.2% |
| P home away | 89.3% |
| Raw p home draw | 20.0% |
| Raw p draw away | 91.4% |
| Raw p home away | 88.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8489 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.67, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:40Z", "line": -2.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:00:40Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T06:59:54Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.67, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 11.19 |
| Reference draw odds | 8.20 |
| Reference away odds | 1.20 |
| Market reference 1x2 last update utc | 2026-10-30T07:00:40Z |
| Market reference home last update utc | 2026-10-30T07:00:40Z |
| Market reference draw last update utc | 2026-10-30T07:00:40Z |
| Market reference away last update utc | 2026-10-30T07:00:40Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.63 |
| Market reference over 2 5 last update utc | 2026-10-30T07:00:42Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:00:42Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +3.2% |
| Under 2.5 probability edge | -3.2% |
| Raw edge prob home | 0.0115 |
| Raw ev home | -0.0391 |
| Raw edge prob draw | 0.0104 |
| Raw ev draw | -0.0632 |
| Raw edge prob away | -0.0219 |
| Raw ev away | -0.0401 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.00880439132304533, 0.028589223330354407, 0.05372343992396453, 0.06558726664764286, 0.060053249834670516, 0.04398893870763208, 0.026851540562626133, 0.014049088282562057, 0.006431838462751079, 0.0026173969555192667, 0.0009586201793146584, 0.0003191764614046265, 9.741516790168499e-05, 2.744480851333064e-05, 7.1797470391412285e-06, 1.7530522400845904e-06, 4.012840049906706e-07, 8.645296685703546e-08, 1.759075057292604e-08, 3.3908434812524503e-09, 6.209472696091862e-10, 1.0829599626644476e-10, 1.802879472938075e-11], [0.008552296801568045, 0.03508790665061037, 0.0625464801314436, 0.076358711878064, 0.06991583939764323, 0.051213274592509815, 0.03126138889609306, 0.016356380424891445, 0.007488144042683784, 0.0030472539901798203, 0.0011160550791975523, 0.000371595047337314, 0.00011341373285641144, 3.1952089680403953e-05, 8.358882196821525e-06, 2.0409573039071717e-06, 4.6718717343375414e-07, 1.0065120143983673e-07, 2.047969252832435e-08, 3.94772420993813e-09, 7.229258981973813e-10, 1.260815276977935e-10, 2.0989677000040358e-11], [0.00541246632878998, 0.019823127828197003, 0.0366021752185057, 0.044449579756093864, 0.040699084663482474, 0.029812034247063527, 0.018197734938773125, 0.009521300429716701, 0.004358963733986327, 0.0017738533815220686, 0.0006496728144681613, 0.0002163111881715021, 6.601987697340394e-05, 1.8599802480834996e-05, 4.865833796053707e-06, 1.1880726144735512e-06, 2.719568339461913e-07, 5.859061128599179e-08, 1.1921543777109525e-08, 2.2980309359450724e-09, 4.2082627612922756e-10, 7.33939950443716e-11, 1.2218413576145804e-11], [0.002100453223489889, 0.007692898249530002, 0.014087598527734283, 0.017341250892695018, 0.01579437512983313, 0.011569362214773298, 0.007062120794921581, 0.003694996876569047, 0.0016916131888757614, 0.0006883915440540831, 0.0002521230201663853, 8.394537810886207e-05, 2.5620790039019765e-05, 7.218153925380485e-06, 1.8883177577516595e-06, 4.610635524025379e-07, 1.0554016853165118e-07, 2.2737663546706543e-08, 4.626475904784732e-09, 8.918127511315944e-10, 1.633129620637278e-10, 2.8482515014595142e-11, 4.741684219897143e-12], [0.0006113530518334967, 0.00223907715234934, 0.004100303809015954, 0.005005779965670328, 0.004621431012217198, 0.003367351778497174, 0.002055484526914956, 0.0010754572354877293, 0.0004923570179881078, 0.0002003616489086088, 7.338234248325783e-05, 2.443294738499407e-05, 7.4571278263057154e-06, 2.100899168586763e-06, 5.496093943547988e-07, 1.341960900143996e-07, 3.071827708481085e-08, 6.61797170505245e-09, 1.34657136469095e-09, 2.5956895443853794e-10, 4.753349260296379e-11, 8.290054871650398e-12, 1.3801036301339021e-12], [0.00014235120299042634, 0.0005213604892776668, 0.0009547399462375066, 0.001165576581128474, 0.0010672294365306498, 0.0007882291669163873, 0.00047861165370323807, 0.00025041607427541155, 0.00011464343492060396, 4.665343809071857e-05, 1.7086795754791175e-05, 5.689117675007457e-06, 1.736363487095361e-06, 4.891862780646807e-07, 1.2797443020298097e-07, 3.124704259326091e-08, 7.15263248249394e-09, 1.5409692169613894e-09, 3.135439548413719e-10, 6.04396310977383e-11, 1.1067990638265894e-11, 1.9303073409004278e-12, 3.2135181367266895e-13], [2.7621607694670835e-05, 0.00010116398456638166, 0.00018525626542950337, 0.00022616668061591053, 0.00020708355248699072, 0.00015168847186101538, 9.336111626452049e-05, 4.859034850966564e-05, 2.224523514816674e-05, 9.052561112786015e-06, 3.3154954730487974e-06, 1.1039076119254313e-06, 3.369212907819563e-07, 9.492095028678837e-08, 2.4831960895009146e-08, 6.063127911801136e-09, 1.3878857660858291e-09, 2.9900728821613265e-10, 6.083958501036639e-11, 1.172761272347401e-11, 2.1476158188774184e-12, 3.745538568021846e-13, 6.235460988576531e-14], [4.593989245977445e-06, 1.682546006429058e-05, 3.081157695601048e-05, 3.7615743081760185e-05, 3.4441862460004006e-05, 2.522862594282318e-05, 1.539995036810254e-05, 8.124300731878265e-06, 3.699798077453483e-06, 1.505609986949319e-06, 5.514288203872989e-07, 1.8360045344922163e-07, 5.603630330655133e-08, 1.5787126862988416e-08, 4.130018881204153e-09, 1.0084114122428178e-09, 2.308313243212706e-10, 4.9730496563341386e-11, 1.011875928283777e-11, 1.950521031511953e-12, 3.571886215123322e-13, 6.2295301895863e-14, 1.0370736215603846e-14], [6.685579364991024e-07, 2.448589724296754e-06, 4.483973123800995e-06, 5.474175542888384e-06, 5.0122843704103935e-06, 3.67149272624231e-06, 2.2411369485251454e-06, 1.172593087152915e-06, 5.412800897006979e-07, 2.1910967835387465e-07, 8.024879784102063e-08, 2.671916143595469e-08, 8.154898346893021e-09, 2.297482295591099e-09, 6.010368664528075e-10, 1.4675294538434665e-10, 3.3592615394716443e-11, 7.2372215917952644e-12, 1.4725713239291226e-12, 2.83857067594915e-13, 5.198124657090592e-14, 9.065763165543828e-15, 1.50924123524051e-15], [8.648396667397707e-08, 3.167470469698141e-07, 5.800421489818551e-07, 7.081337149294238e-07, 6.483839481750742e-07, 4.749405208512029e-07, 2.899111693790019e-07, 1.5168543507613382e-07, 6.94433827974986e-08, 2.8493976967474996e-08, 1.0380901907248343e-08, 3.4563632275223475e-09, 1.0549092582095366e-09, 2.971999454922627e-10, 7.774951053655766e-11, 1.8983809996166058e-11, 4.3455061583765765e-12, 9.361995375218305e-13, 1.904903110875141e-13, 3.671945815586685e-14, 6.724240564177413e-15, 1.172737793808411e-15, 1.952338930789246e-16], [1.006872923796046e-08, 3.687666483760211e-08, 6.753028994055563e-08, 8.244310378100244e-08, 7.548685227430713e-08, 5.52940353281181e-08, 3.375234947931683e-08, 1.7659684608145737e-08, 8.084812083052213e-09, 3.290064365682936e-09, 1.2149799308824966e-09, 4.024004312516957e-10, 1.2281577846180785e-10, 3.460093119894579e-11, 9.051837006131547e-12, 2.2101535129262046e-12, 5.059171843438227e-13, 1.0899522788479464e-13, 2.2177467553325806e-14, 4.274992188202789e-15, 7.828567557133696e-16, 1.3653373876215838e-16, 2.2729729949772398e-17], [1.0656658250312602e-09, 3.90299515756219e-09, 7.147349029188886e-09, 8.725708689999118e-09, 7.989464887448618e-09, 5.852274143502798e-09, 3.5723202506044837e-09, 1.8690861500952976e-09, 8.556897037439605e-10, 3.482176423458637e-10, 1.2753451785073043e-10, 4.2815376694765456e-11, 1.299871858584911e-11, 3.6621334253341695e-12, 9.58038807401839e-13, 2.339207869368958e-13, 5.3545848826545756e-14, 1.1535963149193589e-14, 2.3472444931994465e-15, 4.524615738069178e-16, 8.28568998869587e-17, 1.4450615954000033e-17, 2.4056954802539176e-18], [1.0339007586262154e-10, 3.786655778512576e-10, 6.934302864810331e-10, 8.465615225933336e-10, 7.75131717103561e-10, 5.677831206118143e-10, 3.465837535934329e-10, 1.8133729571975284e-10, 8.301835463510058e-11, 3.378380690568356e-11, 1.2373300490614014e-11, 4.119740384887098e-12, 1.2678074883815063e-12, 3.5529735848781214e-13, 9.294818567885107e-14, 2.269481420832871e-14, 5.1949769264137125e-15, 1.1192102412672795e-15, 2.277278491246471e-16, 4.3897472680468203e-17, 8.038712477997506e-18, 1.4019876068577561e-18, 2.333987187761437e-19], [9.25922341258275e-12, 3.391185425415781e-11, 6.21009888039011e-11, 7.581484204154393e-11, 6.941785933475163e-11, 5.0848504750336936e-11, 3.1038727643039725e-11, 1.62398810533207e-11, 7.434809255124291e-12, 3.025549727644319e-12, 1.1081059051145761e-12, 3.689483377127496e-13, 1.1260593624970275e-13, 3.198767268195139e-14, 8.324087295750292e-15, 2.0324615617962146e-15, 4.652424479191922e-16, 1.0023222812326915e-16, 2.039444322599978e-17, 3.9312913101667295e-18, 7.199166279962561e-19, 1.2555669744180268e-19, 2.090230482305104e-20], [7.699908936096126e-13, 2.820087365602763e-12, 5.164277146415492e-12, 6.3047121093448756e-12, 5.7727432593315345e-12, 4.2285280165308536e-12, 2.5811600573209466e-12, 1.350497765003407e-12, 6.182738192050303e-13, 2.5160271381758816e-13, 9.214935400886523e-14, 3.068149968874966e-14, 9.364235164779357e-15, 2.6381891701971937e-15, 6.958932234827436e-16, 1.690181589168637e-16, 3.8689254190757e-17, 8.335245782733597e-18, 1.6959884068590334e-18, 3.2692358463252834e-19, 5.986779052787027e-20, 1.0441211898020113e-20, 1.7382218412971844e-21], [5.976313777463242e-14, 2.1888215973170577e-13, 4.0082734636092013e-13, 4.89342642292604e-13, 4.480536764892256e-13, 3.2819881966545854e-13, 2.003377252955659e-13, 1.0481940067612274e-13, 4.7987559003953806e-14, 1.952824088589223e-14, 7.152207363983866e-15, 2.38135633583316e-15, 7.268086946889313e-16, 2.047640617084692e-16, 5.3567659802028586e-17, 1.3187914555241247e-17, 3.0028812649468453e-18, 6.469432901520657e-19, 1.3163478901438063e-19, 2.5374299088888056e-20, 4.646661464796418e-21, 8.10398655846801e-22, 1.3491275318508782e-22], [4.3486301262356116e-15, 1.5926833652781134e-14, 2.916596983875306e-14, 3.5606734110078976e-14, 3.260236641354387e-14, 2.3881197134833e-14, 1.4577458615494695e-14, 7.627123015412192e-15, 3.491786953289468e-15, 1.42096114412559e-15, 5.204262287798814e-16, 1.732780153270629e-16, 5.28858139553016e-17, 1.4899538422391572e-17, 3.897819757815998e-18, 9.517162123726601e-19, 2.1966061477194385e-19, 4.707445402432373e-20, 9.578329225738597e-21, 1.846346185271563e-21, 3.381116317625623e-22, 5.896818909284452e-23, 9.816848391168175e-24], [2.978122860497321e-16, 1.0907358413980605e-15, 1.9974069765403574e-15, 2.4384973143869207e-15, 2.232745713108837e-15, 1.6354837514050715e-15, 9.983250239849487e-16, 5.223371211772179e-16, 2.391321001719573e-16, 9.731333188509412e-17, 3.564095368288859e-17, 1.1866799513571038e-17, 3.621840601850222e-18, 1.0203823893616281e-18, 2.6693891616159525e-19, 6.517748639216819e-20, 1.4919511339497868e-20, 3.2409354957122595e-21, 6.559638415887705e-22, 1.264454695646687e-22, 2.3155291453214347e-23, 4.0383869605288696e-24, 6.722986265351158e-25], [1.9262345427157128e-17, 7.054823300097767e-17, 1.2919125550887766e-16, 1.577207516048282e-16, 1.444128439003512e-16, 1.0578224752892327e-16, 6.457114887920288e-17, 3.378449623754686e-17, 1.5466941197531987e-17, 6.294176235312347e-18, 2.305238545727639e-18, 7.675384866662426e-19, 2.3425878656762823e-19, 6.599780792250262e-20, 1.726547174819019e-20, 4.2156462838142416e-21, 9.649863168432374e-22, 2.0789747169085568e-22, 4.265219759836429e-23, 8.17842791095261e-24, 1.497672337009735e-24, 2.6120079071970915e-25, 4.3483929243806145e-26], [1.1803060336711597e-18, 4.322864284143518e-18, 7.91623319970675e-18, 9.66438668947718e-18, 8.848940625625166e-18, 6.481839165736076e-18, 3.9566166493801715e-18, 2.070155210564217e-18, 9.477414932112109e-19, 3.8567754978866147e-19, 1.4125418811862877e-19, 4.703115258278808e-20, 1.4354277897874006e-20, 4.0440356131385596e-21, 1.0579469958957864e-21, 2.5831499925207744e-22, 5.912982801016465e-23, 1.2738980367143762e-23, 2.5920247082138353e-24, 5.037908158431486e-25, 9.17703247779348e-26, 1.6005157339328806e-26, 2.6644908974498125e-27], [6.870742825526448e-20, 2.516405738740684e-19, 4.608161011674784e-19, 5.62578802578065e-19, 5.151104339263467e-19, 3.773178199019968e-19, 2.3032073616139103e-19, 1.205069164686914e-19, 5.516948892213191e-20, 2.245088292851463e-20, 8.222623386690445e-21, 2.7377556749359068e-21, 8.355845778037265e-22, 2.3540952839767e-22, 6.158472061037848e-23, 1.5036913115802605e-23, 3.442038166252734e-24, 7.415556259577728e-25, 1.50885741998242e-25, 2.9085167943665164e-26, 5.3703957446080056e-27, 9.316848073594864e-28, 1.5510411024836183e-28], [3.809109520495095e-21, 1.3950842434756962e-20, 2.5547441415404438e-20, 3.118912070129249e-20, 2.855749527817418e-20, 2.0918333527219824e-20, 1.2768880034635439e-20, 6.680850301964668e-21, 3.058572134491725e-21, 1.2446670480636616e-21, 4.558586141417443e-22, 1.517799671884647e-22, 4.632444047630578e-23, 1.3051000431909171e-23, 3.414229749984115e-24, 8.336398314235053e-25, 1.9082507789798075e-25, 4.1111516855472186e-26, 8.3650389913762e-27, 1.6124688833907107e-27, 2.9528291589012177e-28, 5.192586452845941e-29, 8.598903466739597e-30], [2.015764722567442e-22, 7.38272708588983e-22, 1.3519598446814209e-21, 1.6505151374432444e-21, 1.511250627919664e-21, 1.1069894040113827e-21, 6.757237559598543e-22, 3.535477854599472e-22, 1.6185834975243424e-22, 6.586725620067703e-23, 2.4123845951952992e-23, 8.032131966927125e-24, 2.4514698882345444e-24, 6.906534486158741e-25, 1.806796010387147e-25, 4.411586893128123e-26, 1.0098382788372466e-26, 2.1756041647688382e-27, 4.426743418899024e-28, 8.533117448810554e-29, 1.5626247600011034e-29, 2.7252878538533826e-30, 4.574613525452417e-31]] |
| Legacy trial inputs | {"lambda_home": 1.1642307383884285, "lambda_away": 3.662494438580405, "rho": -0.021895783674930586, "max_goals": 22, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0746 |
| Legacy p draw | 0.1033 |
| Legacy p away | 0.8221 |
| Legacy p over 1 5 | 0.9541 |
| Legacy p under 3 5 | 0.2902 |
| Legacy p btts yes | 0.6710 |
| Legacy p over 2 5 | 0.8598 |
| Legacy goal margin distribution | {"-1": 0.15527814183285574, "-10": 0.001404035553114056, "-11": 0.00045321997263888923, "-12": 0.00013472647702012972, "-13": 3.710424710287961e-05, "-14": 9.51680806295745e-06, "-15": 2.283727522578791e-06, "-16": 5.147980891133022e-07, "-17": 1.0940261469005395e-07, "-18": 2.1989163677638125e-08, "-19": 4.1919050587141e-09, "-2": 0.1846803339583438, "-20": 7.592472108831254e-10, "-21": 1.292856732664851e-10, "-22": 1.802879472938075e-11, "-3": 0.17357699355726555, "-4": 0.13370177425591717, "-5": 0.08668185198839289, "-6": 0.048334701054672254, "-7": 0.02358947723998539, "-8": 0.010220682834536053, "-9": 0.0039776191879174385, "0": 0.10334744071414889, "1": 0.0487043664402333, "10": 1.4747085581780955e-08, "11": 1.5132100717495642e-09, "12": 1.4298985445339475e-10, "13": 1.2518087466865156e-11, "14": 1.020628652340969e-12, "15": 7.785433853643209e-14, "16": 5.5787583143232365e-15, "17": 3.7686899553767673e-16, "18": 2.4078726183797338e-17, "19": 1.459144564098076e-18, "2": 0.01860595841505937, "20": 8.401023053470286e-20, "21": 4.547382229084078e-21, "22": 2.015764722567442e-22, "3": 0.005558858819345919, "4": 0.0013611084820878072, "5": 0.00028050837939049754, "6": 4.9720877186078885e-05, "7": 7.713653909715467e-06, "8": 1.0623896518922364e-06, "9": 1.3142839666113128e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0748 |
| Legacy raw p draw | 0.1028 |
| Legacy raw p away | 0.8223 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1642 |
| Legacy lambda away | 3.6625 |
| Legacy model home team | Santander |
| Legacy model away team | Real Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01468911490264166, "mu": 10.724162471624577, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,438.0702 |
| Elo away rating | 1,670.4419 |
| Elo rating diff | -172.3717 |
| Elo home expectancy | 0.2705 |

</details>


---
