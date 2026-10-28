# Serie A — football model report

Fixtures in this report: **8**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,983 |
| Training data through | 2026-10-27 |
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
| Training sha256 | a99fb4ad4b4b8fe9fd38120f107e400608da5c9ec2f09b413ebef880b14c3179 |
| Training as of utc | 2026-10-28T16:07:21.315970+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 83, 'bbs_added_results': 3, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 83, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 131, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-28T16:07:21.315970+00:00', 'observations': 399, 'observations_sha256': '210ae88113333ba6d5521020580e6c5b01ac916d906742efb429d80863a1e1ba', 'eligible_training_matches': 171, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 169, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 19, 'retrospective_eligible_training_matches': 171, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '2f1a134e7b9dd41208774447c6f4987ffc4403888724d1aadccfd09314f619bd', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 110, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-14T00:00:00+00:00', 'audit_origin_utc': '2025-10-19T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 28, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1980, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1602, 'tuning_matches': 258, 'audit_matches': 120, 'audit_matchdays': 40, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8683005027248231, 'audit_candidate_poisson_score': 0.8659310430398178, 'audit_gain': 0.0023694596850052374, 'audit_gain_lower95': -0.0023660903071611367, 'audit_baseline_briers': [0.5674415697640655, 0.1666904345752652, 0.19159848167132806, 0.24301006972672107], 'audit_candidate_briers': [0.5684821403059223, 0.16511556160319063, 0.19111534068285901, 0.2429513410619891], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1789.870 |
| Base scoring parameter | 0.148 |
| Home-advantage parameter | 0.108 |
| Dixon-Coles low-score adjustment | -0.023 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1983, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-27'} |
| Training data health | {'training_end': '2026-10-27', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 8.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261028T160721315970Z_765bb1e5f0a7b3ddca17aa2cbc2f93ee7a4b799512e4c5ba4b28e661dc6b5643.json |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 7, 'ANCHORED_MAIN': 1} |
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

## 2026-10-28 — AC Milan vs Bologna

The model's most likely 1X2 outcome is **AC Milan win** at **54.3%**. Expected goals are 1.55 for AC Milan and 1.02 for Bologna (2.58 combined). The most likely exact score is 1-0 at 13.1%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 46.8%; Under 3.5 goals: 74.8%; Double Chance 1X: 80.2%; Double Chance X2: 45.7%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 88.5%; BTTS Yes (both teams score): 49.6%; BTTS No (at least one team does not score): 50.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 54.3% | 1.84 |
| Draw | 25.9% | 3.87 |
| Bologna win | 19.8% | 5.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.55 |
| Bologna expected goals | 1.02 |
| Expected total goals | 2.58 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 72.6% |
| Under 1.5 | 27.4% |
| Over 2.5 | 46.8% |
| Under 2.5 | 53.2% |
| Over 3.5 | 25.2% |
| Under 3.5 | 74.8% |
| Over 4.5 | 11.5% |
| Under 4.5 | 88.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.13% |
| 2 | 1-1 | 12.28% |
| 3 | 2-1 | 10.30% |
| 4 | 2-0 | 10.26% |
| 5 | 0-0 | 8.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 54.3% | 56.4% | 1.74 | -5.5% |
| Draw | 25.9% | 25.8% | 3.71 | -4.1% |
| Bologna win | 19.8% | 17.8% | 5.32 | +5.6% |

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
| Market best home last update utc | 2026-10-28T16:07:31Z |
| Market best draw last update utc | 2026-10-28T16:07:31Z |
| Market best away last update utc | 2026-10-28T16:07:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Milan |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5549 |
| Dc lambda away | 1.0231 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:07:21.315970+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.6% |
| P btts no | 50.4% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.34 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.64 |
| Fair Over 2.5 odds | 2.14 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 3.96 |
| Fair Under 3.5 odds | 1.34 |
| Fair Over 4.5 odds | 8.71 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.12587294674326616, "-10": 2.122766327460078e-08, "-11": 1.916497659948107e-09, "-12": 1.5888352626694807e-10, "-13": 1.2173505935904205e-11, "-14": 8.633770737274443e-13, "-15": 5.245626856070316e-14, "-2": 0.05238268468158289, "-3": 0.01567338264839447, "-4": 0.003668080777648119, "-5": 0.0007022771462468168, "-6": 0.00011353985417302459, "-7": 1.586796156092125e-05, "-8": 1.95161681038045e-06, "-9": 2.1422989121357886e-07, "0": 0.258503856124351, "1": 0.26426002761598605, "10": 1.9172811114277275e-06, "11": 2.630906048585438e-07, "12": 3.315044468436321e-08, "13": 3.860464851382643e-09, "14": 4.1613848841629977e-10, "15": 3.8428037837099285e-11, "2": 0.1661360259495087, "3": 0.07555309223025566, "4": 0.026874589585174035, "5": 0.007820327262446755, "6": 0.0019216671512271664, "7": 0.00040819193189852685, "8": 7.630469650369897e-05, "9": 1.2730639748350388e-05} |
| Raw goal margin distribution | {"-1": 0.15544157080512075, "-10": 3.0343075934130066e-08, "-11": 2.7887903664209293e-09, "-12": 2.353767717419234e-10, "-13": 1.8360808219712444e-11, "-14": 1.3254272771699934e-12, "-15": 8.173134606772026e-14, "-2": 0.06546800895819692, "-3": 0.019876275999642642, "-4": 0.004726024218121227, "-5": 0.0009199505919688019, "-6": 0.00015128524695754586, "-7": 2.1512377391001665e-05, "-8": 2.6925768852398477e-06, "-9": 3.0083089535932153e-07, "0": 0.25964074595967584, "1": 0.237686231930959, "10": 1.996153927032193e-06, "11": 2.788455611229424e-07, "12": 3.577049172946043e-08, "13": 4.240983130933149e-09, "14": 4.653118331757787e-10, "15": 4.3610421769045644e-11, "2": 0.15123629097517954, "3": 0.06978713119506884, "4": 0.025220268870586, "5": 0.0074615957257768905, "6": 0.0018649931141652074, "7": 0.00040307188333565784, "8": 7.667886080289865e-05, "9": 1.3020972374203977e-05} |
| Unadjusted home-win probability | 49.4% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 73.1% |
| Raw p under 3 5 | 74.1% |
| Raw p btts yes | 50.8% |
| P home draw | 80.2% |
| P draw away | 45.7% |
| P home away | 74.1% |
| Raw p home draw | 75.3% |
| Raw p draw away | 50.6% |
| Raw p home away | 74.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9819 |
| Totals anchor target over 2 5 | 0.4679 |
| Totals anchor reference over odds | 2.07 |
| Totals anchor reference under odds | 1.83 |
| Totals anchor reference last update utc | 2026-10-28T16:07:31Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4786 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.93, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:35Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.95, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:35Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.28, "price": 3.95, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.74 |
| Reference draw odds | 3.71 |
| Reference away odds | 5.32 |
| Market reference 1x2 last update utc | 2026-10-28T16:07:31Z |
| Market reference home last update utc | 2026-10-28T16:07:31Z |
| Market reference draw last update utc | 2026-10-28T16:07:31Z |
| Market reference away last update utc | 2026-10-28T16:07:31Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.84 |
| Market reference over 2 5 last update utc | 2026-10-28T16:07:32Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:07:32Z |
| Home probability edge | -2.1% |
| Draw probability edge | +0.0% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | -0.0704 |
| Raw ev home | -0.1409 |
| Raw edge prob draw | 0.0016 |
| Raw ev draw | -0.0367 |
| Raw edge prob away | 0.0688 |
| Raw ev away | 0.3120 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07663064364694909, 0.062005998624660434, 0.033656121751201216, 0.011579404585455453, 0.002987924712735535, 0.000616798145230337, 0.00010610484660083672, 1.5645181110008738e-05, 2.018524481497748e-06, 2.3149143375949495e-07, 2.389342113791838e-08, 2.2419662258708465e-09, 1.9283738474233566e-10, 1.531056768562889e-11, 1.1287731522756916e-12, 7.767098723983914e-14], [0.11942422143351922, 0.12301658642287845, 0.05334841002949558, 0.018354545668954, 0.004736167580169541, 0.0009776884158082166, 0.00016818708062749804, 2.4799219084494657e-05, 3.199568639832171e-06, 3.669377006005328e-07, 3.7873526762708256e-08, 3.5537467559158033e-09, 3.0566706248269816e-10, 2.426882243638553e-11, 1.7892213904812313e-12, 1.2311649290128824e-13], [0.0977833622153839, 0.10092723587003805, 0.0488006775110804, 0.014546920104029993, 0.0037536560496051596, 0.0007748682821092293, 0.00013329689922843472, 1.9654654774412534e-05, 2.5358224720171445e-06, 2.9081697308482726e-07, 3.001671508583607e-08, 2.8165268190595886e-09, 2.422568456102109e-10, 1.9234288190425683e-11, 1.4180498436295646e-12, 9.757614369898377e-14], [0.05166555770638073, 0.05332667859695029, 0.02752060343898342, 0.00887123666708126, 0.0019833101342292513, 0.00040941527308068046, 7.04297590422272e-05, 1.038488222781362e-05, 1.3398463633573721e-06, 1.5365825805635114e-07, 1.5859858878725134e-08, 1.4881614377419967e-09, 1.280006613913606e-10, 1.0162774156350827e-11, 7.492515532978986e-13, 5.1556070161932006e-14], [0.0204738039731523, 0.021132065782354235, 0.010905745820740866, 0.0037521270007882385, 0.0009071205515915769, 0.00016224131542923908, 2.7909600602817585e-05, 4.115276258602562e-06, 5.309485277100181e-07, 6.0891030581351e-08, 6.284876349738413e-09, 5.897221845525781e-10, 5.07235490353936e-11, 4.027260231720063e-12, 2.969101682010208e-13, 2.0430416722108113e-14], [0.006490616460788517, 0.006699298977233296, 0.0034573454661428822, 0.001189501340650744, 0.00030693637357024885, 5.9364364252717645e-05, 8.847916748847803e-06, 1.3046271156939963e-06, 1.6832159076569842e-07, 1.9303707602356354e-08, 1.992434915520579e-09, 1.8695404739482776e-10, 1.6080407077769285e-11, 1.276724227024852e-12, 9.412662286051563e-14, 6.4768618108863765e-15], [0.0017147156311019922, 0.0017698461684010774, 0.0009133746152972642, 0.0003142469678115624, 8.108761327899e-05, 1.673893898947873e-05, 2.6978894133032315e-06, 3.4466133094671117e-07, 4.4467835140397764e-08, 5.099726561252021e-09, 5.263689996529948e-10, 4.939022807808131e-11, 4.2481828247457924e-12, 3.3728984017338824e-13, 2.4866727605433095e-14, 1.7110818756135847e-15], [0.0003882857722342018, 0.00040076971001408, 0.00020682751204168645, 7.115910320975617e-05, 1.836174230267351e-05, 3.7904196672738826e-06, 6.52047838436186e-07, 9.00801057628031e-08, 1.006944089964123e-08, 1.1547986325560192e-09, 1.191927044947144e-10, 1.1184083530979645e-11, 9.61972305366113e-13, 7.637700600787531e-14, 5.630902498397312e-15, 3.874629328488632e-16], [7.693410406470189e-05, 7.940764452632639e-05, 4.09803564094046e-05, 1.4099310979100622e-05, 3.6381559514652004e-06, 7.51025564117374e-07, 1.2919535003501408e-07, 1.904988051556949e-08, 2.3027656203277168e-09, 2.2880930624790617e-10, 2.3616584966751163e-11, 2.215990148930097e-12, 1.9060311435711872e-13, 1.5133174966854113e-14, 1.1156948561292916e-15, 7.677106844653869e-17], [1.3549828597590091e-05, 1.3985474787165898e-05, 7.21756380952451e-06, 2.4832062377728526e-06, 6.407612092576953e-07, 1.3227251801932395e-07, 2.2754211150725242e-08, 3.3551130402903705e-09, 4.328730848430984e-10, 4.651205645456001e-11, 4.159412555071536e-12, 3.902857784201754e-13, 3.3569501602745795e-14, 2.665292972876695e-15, 1.9649899419184735e-16, 1.3521114353000258e-17], [2.147787012411261e-06, 2.216841408283382e-06, 1.1440580004165783e-06, 3.9361369542163336e-07, 1.015672333704192e-07, 2.0966552768893765e-08, 3.6067761916843122e-09, 5.318198795805398e-10, 6.861483028750342e-11, 7.868988256527276e-12, 7.609679487105955e-13, 6.186430477568988e-14, 5.321110819683714e-15, 4.2247631327481853e-16, 3.1147108956949266e-17, 2.1432355096998386e-18], [3.094966389801574e-07, 3.1944739448138967e-07, 1.6485904043612418e-07, 5.671983073069641e-08, 1.4635863415230884e-08, 3.021285432621936e-09, 5.197373400757853e-10, 7.663537600416962e-11, 9.88741399191863e-12, 1.1339231513628232e-12, 1.170380387452943e-13, 1.0289204956066453e-14, 7.667733834018154e-16, 6.087894109224982e-17, 4.488306093862665e-18, 3.0884076631524497e-19], [4.088199694427292e-08, 4.219641107599041e-08, 2.1776542742286448e-08, 7.492229816300761e-09, 1.933278905353884e-09, 3.990873123250467e-10, 6.86530891541121e-11, 1.0122911893161249e-11, 1.3060472318418103e-12, 1.4978205566887376e-13, 1.5459776100042173e-14, 1.4506208916568532e-15, 1.1690151773590378e-16, 8.041614577480093e-18, 5.928688486533746e-19, 4.07953614823463e-20], [4.984781879254119e-09, 5.145049680128722e-09, 2.6552351589507913e-09, 9.135349105967618e-10, 2.3572658811380066e-10, 4.866110638944235e-11, 8.370938318808725e-12, 1.2342965496303895e-12, 1.592476165880415e-13, 1.8263072568431066e-14, 1.885025623035565e-15, 1.7687562435502592e-16, 1.5213535525961068e-17, 1.1317076941707333e-18, 7.22890786761237e-20, 4.9742183326323315e-21], [5.64385092868531e-10, 5.825308733402701e-10, 3.006300331834109e-10, 1.0343190491475356e-10, 2.668934680530022e-11, 5.509489424801134e-12, 9.477712194629731e-13, 1.397490581663507e-13, 1.803027355142418e-14, 2.0677747105638663e-15, 2.1342565975538295e-16, 2.0026145194687605e-17, 1.7225011783189623e-18, 1.3676015630717144e-19, 9.446676009104739e-21, 5.63189070979194e-22], [5.964055627375958e-11, 6.15580846688764e-11, 3.1768632159520944e-11, 1.0930012899911e-11, 2.82035707562918e-12, 5.822071104136649e-13, 1.0015431566722545e-13, 1.4767774119286753e-14, 1.9053223729023683e-15, 2.1850902078231958e-16, 2.2553439542865926e-17, 2.1162331438624036e-18, 1.8202275317905965e-19, 1.445192635544326e-20, 1.0654697333007334e-21, 6.869060256385043e-23]] |
| Legacy trial inputs | {"lambda_home": 1.5851027169400922, "lambda_away": 1.0321514170041448, "rho": -0.03104744974939825, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5312 |
| Legacy p draw | 0.2583 |
| Legacy p away | 0.2105 |
| Legacy p over 1 5 | 0.7419 |
| Legacy p under 3 5 | 0.7300 |
| Legacy p btts yes | 0.5144 |
| Legacy p over 2 5 | 0.4875 |
| Legacy goal margin distribution | {"-1": 0.13205608308839656, "-10": 2.7699890900630755e-08, "-11": 2.5676372585139905e-09, "-12": 2.185758130925127e-10, "-13": 1.7197365219809105e-11, "-14": 1.2518896451769799e-12, "-15": 7.767098723983914e-14, "-2": 0.056202998617205596, "-3": 0.01716515902579507, "-4": 0.004109845699981695, "-5": 0.000806042660828634, "-6": 0.00013360002257149108, "-7": 1.915203272739361e-05, "-8": 2.417019084149312e-06, "-9": 2.723136111005906e-07, "0": 0.2582884194834016, "1": 0.25194853459446814, "10": 2.48995175609945e-06, "11": 3.5445453747708897e-07, "12": 4.6338606670484966e-08, "13": 5.59908138475391e-09, "14": 6.259431775374074e-10, "15": 5.964055627375958e-11, "2": 0.16329029862689953, "3": 0.07658835198662634, "4": 0.028161410782098197, "5": 0.008482051709993997, "6": 0.0021590535621876876, "7": 0.0004753196377287946, "8": 9.21223395855658e-05, "9": 1.5939262612357747e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4982 |
| Legacy raw p draw | 0.2586 |
| Legacy raw p away | 0.2432 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5851 |
| Legacy lambda away | 1.0322 |
| Legacy model home team | Milan |
| Legacy model away team | Bologna |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 81.7% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-28T16:07:35Z |
| Market reference home draw last update utc | 2026-10-28T16:07:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.2% |
| Market draw away odds | 2.20 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-28T16:07:35Z |
| Market reference draw away last update utc | 2026-10-28T16:07:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.2% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-28T16:07:35Z |
| Market reference home away last update utc | 2026-10-28T16:07:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.20 |
| Market reference dc home away odds | 1.31 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 2.28, "price": 1.63, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 1.63, "price": 2.28, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.08, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.08, "price": 1.76, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 71.6% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-28T16:07:31Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.10 |
| Market reference over 1 5 last update utc | 2026-10-28T16:07:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 74.7% |
| Market reference under 3 5 odds | 1.32 |
| Market reference under 3 5 opposite odds | 3.70 |
| Market reference under 3 5 last update utc | 2026-10-28T16:07:06Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 49.0% |
| Market btts yes odds | 1.97 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-28T16:07:35Z |
| Market reference btts yes odds | 1.97 |
| Market reference btts yes opposite odds | 1.90 |
| Market reference btts yes last update utc | 2026-10-28T16:07:35Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021258779398154137, "mu": 8.429096366582412, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,555.4913 |
| Elo away rating | 1,508.1760 |
| Elo rating diff | 107.3154 |
| Elo home expectancy | 0.6497 |

</details>


---

## 2026-10-28 — Genoa vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **53.0%**. Expected goals are 0.77 for Genoa and 1.43 for Juventus (2.20 combined). The most likely exact score is 0-1 at 15.1%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 39.1%; Under 3.5 goals: 80.7%; Double Chance 1X: 47.0%; Double Chance X2: 80.8%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.5%; BTTS No (at least one team does not score): 57.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 19.2% | 5.20 |
| Draw | 27.8% | 3.60 |
| Juventus win | 53.0% | 1.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 0.77 |
| Juventus expected goals | 1.43 |
| Expected total goals | 2.20 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 66.3% |
| Under 1.5 | 33.7% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.07% |
| 2 | 1-1 | 12.72% |
| 3 | 0-2 | 11.26% |
| 4 | 0-0 | 10.98% |
| 5 | 1-2 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 19.2% | 18.9% | 5.01 | -3.7% |
| Draw | 27.8% | 27.9% | 3.44 | -4.3% |
| Juventus win | 53.0% | 53.2% | 1.84 | -2.5% |

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
| Market best home last update utc | 2026-10-28T16:07:31Z |
| Market best draw last update utc | 2026-10-28T16:07:31Z |
| Market best away last update utc | 2026-10-28T16:07:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Genoa |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7704 |
| Dc lambda away | 1.4264 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:07:21.315970+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 42.5% |
| P btts no | 57.5% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.11 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.19 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.70 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.25892267894939863, "-10": 1.480104557339111e-06, "-11": 1.95709212110955e-07, "-12": 2.3752925190568884e-08, "-13": 2.663695466053376e-09, "-14": 2.769071970740845e-10, "-15": 2.513692338228571e-11, "-2": 0.16304056307438325, "-3": 0.07303689155731342, "-4": 0.025368900613411762, "-5": 0.007173615998630288, "-6": 0.0017078672932814242, "-7": 0.0003508021860383585, "-8": 6.332781475889525e-05, "-9": 1.0193588174443228e-05, "0": 0.2781595405443764, "1": 0.13302322879622414, "10": 3.002284175783119e-09, "11": 2.144185647230928e-10, "12": 1.4055941198820145e-11, "13": 8.51371517635409e-13, "14": 4.7803588987865344e-14, "15": 2.3438515198523313e-15, "2": 0.04565846958937672, "3": 0.011047389848029861, "4": 0.00207257741020004, "5": 0.00031654754761160946, "6": 4.070489738353439e-05, "7": 4.515923208808194e-06, "8": 4.4032209055634514e-07, "9": 3.8282013369345864e-08} |
| Raw goal margin distribution | {"-1": 0.2603868858996816, "-10": 1.1798105644158192e-06, "-11": 1.517355830227919e-07, "-12": 1.790967988055017e-08, "-13": 1.948217845962655e-09, "-14": 1.8404962828885433e-10, "-2": 0.16062846162373684, "-3": 0.07026348487092993, "-4": 0.023793800263467592, "-5": 0.006553870533973796, "-6": 0.0015190902548362806, "-7": 0.00030367843450200663, "-8": 5.3341797594547764e-05, "-9": 8.353144734621777e-06, "0": 0.2768272489980685, "1": 0.13936007336914855, "10": 2.4930410380781145e-09, "11": 1.7317942735755086e-10, "12": 1.1040491291023057e-11, "13": 6.486789545758181e-13, "14": 3.3099310749465504e-14, "2": 0.04686039330981522, "3": 0.011071458330174465, "4": 0.0020250263109313276, "5": 0.0003012703773627866, "6": 3.771671549332949e-05, "7": 4.072451817212444e-06, "8": 3.863681910626568e-07, "9": 3.267950266925161e-08} |
| Unadjusted home-win probability | 20.0% |
| Unadjusted draw probability | 27.7% |
| Unadjusted away-win probability | 52.4% |
| Raw p over 1 5 | 64.7% |
| Raw p under 3 5 | 82.0% |
| Raw p btts yes | 41.1% |
| P home draw | 47.0% |
| P draw away | 80.8% |
| P home away | 72.2% |
| Raw p home draw | 47.6% |
| Raw p draw away | 80.0% |
| Raw p home away | 72.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0286 |
| Totals anchor target over 2 5 | 0.3914 |
| Totals anchor reference over odds | 2.43 |
| Totals anchor reference under odds | 1.60 |
| Totals anchor reference last update utc | 2026-10-28T16:07:31Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3765 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 4.63, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.3, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.79, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.33, "price": 3.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:35Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.6, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:35Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.32, "price": 3.6, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.01 |
| Reference draw odds | 3.44 |
| Reference away odds | 1.84 |
| Market reference 1x2 last update utc | 2026-10-28T16:07:31Z |
| Market reference home last update utc | 2026-10-28T16:07:31Z |
| Market reference draw last update utc | 2026-10-28T16:07:31Z |
| Market reference away last update utc | 2026-10-28T16:07:31Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.54 |
| Reference Under 2.5 odds | 1.61 |
| Market reference over 2 5 last update utc | 2026-10-28T16:07:32Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:07:32Z |
| Home probability edge | +0.3% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | 0.0107 |
| Raw ev home | 0.0003 |
| Raw edge prob draw | -0.0019 |
| Raw ev draw | -0.0477 |
| Raw edge prob away | -0.0088 |
| Raw ev away | -0.0367 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.11666208728603278, 0.15807034798041966, 0.11463982078526061, 0.054115663360193675, 0.019158951493822865, 0.005426383409911791, 0.0012807606286483375, 0.0002591067168340262, 4.586669285106068e-05, 7.21711557924479e-06, 1.0220506132409288e-06, 1.315795693718339e-07, 1.552801555434943e-08, 1.691536400303558e-09, 1.711047456035761e-10], [0.08063736082196599, 0.1256866769907603, 0.08742397896442705, 0.041268440432313196, 0.014610558189147126, 0.004138143498755694, 0.0009767041634438302, 0.00019759399488656625, 3.4977800588942614e-05, 5.503750409428913e-06, 7.794126918597099e-07, 1.0034217976019864e-07, 1.1841617475358776e-08, 1.2899605186465375e-09, 1.304839590457902e-10], [0.032160949146043685, 0.045544674234750074, 0.03291201054874326, 0.015735593633766063, 0.005570983638308171, 0.001577867828599711, 0.00037241581352140456, 7.534229002685806e-05, 1.3336982219457558e-05, 2.09857166874267e-06, 2.9718887517011675e-07, 3.8260320683126145e-08, 4.515190751256215e-09, 4.918599857999591e-10, 4.975333532744405e-11], [0.00817528069612738, 0.011577410056897101, 0.008197664924767353, 0.0039492599154897475, 0.0014161383978403186, 0.00040109240376005797, 9.466772256591343e-05, 1.9151933808345777e-05, 3.390247370753931e-06, 5.334547924877488e-07, 7.55451110366544e-08, 9.72573476261606e-09, 1.1477569153962207e-09, 1.2503031017051164e-10, 1.2647247443579951e-11], [0.0015586110539750995, 0.0022072244320161445, 0.0015628785901600642, 0.0007377559654108445, 0.0002665628037083841, 7.646796206789591e-05, 1.8048329388344424e-05, 3.6513016308818916e-06, 6.463480856712547e-07, 1.0170275092343361e-07, 1.440261802769435e-08, 1.8542039438748457e-09, 2.188189839720507e-10, 2.3836933648774423e-11, 2.4111881170342746e-12], [0.0002377184106937502, 0.0003366445289125198, 0.00023836929271905122, 0.00011252209146727965, 3.9836992814004296e-05, 1.1514984351117415e-05, 2.7527202292914606e-06, 5.568943056338728e-07, 9.858061720327904e-08, 1.5511641760168876e-08, 2.196678548275813e-09, 2.8280205861227897e-10, 3.337413844640174e-11, 3.635594633020972e-12, 3.677529461908982e-13], [3.0213889603096012e-05, 4.2787349126074854e-05, 3.029661637886274e-05, 1.4301500836978463e-05, 5.063261610613229e-06, 1.4340658888735788e-06, 3.4543366818937953e-07, 7.078098419853269e-08, 1.2529546518894201e-08, 1.9715218116122038e-09, 2.79196730944826e-10, 3.594399842024657e-11, 4.241836093701155e-12, 4.620822365551509e-13, 4.6741213206828955e-14], [3.291574342519504e-06, 4.661357488821322e-06, 3.300586797920983e-06, 1.5580401541447284e-06, 5.516039882945328e-07, 1.5623061271843022e-07, 3.687428672914661e-08, 7.61329043060186e-09, 1.3649991572343162e-09, 2.1478236321335245e-10, 3.0416368371159366e-11, 3.915826281284941e-12, 4.621159021435347e-13, 5.034035848939847e-14, 5.092101022109605e-15], [3.137680739000148e-07, 4.4434213201071256e-07, 3.146271827877901e-07, 1.4851958587411938e-07, 5.2581440658047754e-08, 1.489262381336919e-08, 3.515027375801295e-09, 7.111143039170269e-10, 1.2846837673735215e-10, 2.0474047188483835e-11, 2.899428761358882e-12, 3.732746528414625e-13, 4.405102283764852e-14, 4.798675551275726e-15, 4.854025957039917e-16], [2.658650885340772e-08, 3.765043995651821e-08, 2.6659303723092775e-08, 1.258450942974201e-08, 4.455382984648695e-09, 1.261896629389967e-09, 2.978387994837587e-10, 6.025484524884932e-11, 1.0666224764784771e-11, 1.7128330363890823e-12, 2.4567728473948253e-13, 3.1628679550375926e-14, 3.7325751282394996e-15, 4.0660615480362064e-16, 4.112961604966738e-17], [2.0274790860774868e-09, 2.8712111099036817e-09, 2.0330304007188324e-09, 9.596908649431984e-10, 3.397661525117049e-10, 9.623185349331416e-11, 2.2713096341656265e-11, 4.5950161884913644e-12, 8.134030593201046e-13, 1.279888199196543e-13, 1.8497747374830773e-14, 2.411993491218178e-15, 2.8464504502811353e-16, 3.100766180622698e-17, 3.1365320215184673e-18], [1.4055903545075015e-10, 1.9905244249119482e-10, 1.4094389142131443e-10, 6.653248520964356e-11, 2.3554966857020636e-11, 6.6714653677770094e-12, 1.5746307499820752e-12, 3.1855867109558154e-13, 5.6390791025083665e-14, 8.873080467227476e-15, 1.2565598033300326e-15, 1.6509627963071164e-16, 1.9733586032885903e-17, 2.1496680606942436e-18, 2.1744634439508e-19], [8.932491108771902e-12, 1.2649732313757414e-11, 8.956948608243202e-12, 4.228122586881821e-12, 1.4969121788792896e-12, 4.2396993469002755e-13, 1.0006738541359743e-13, 2.0244322878698924e-14, 3.58362048966014e-15, 5.638820167394942e-16, 7.98540572997777e-17, 1.028047176526828e-17, 1.2381652405746041e-18, 1.3661086089118997e-19, 1.3818660121814592e-20], [5.239915827368634e-13, 7.420498017371888e-13, 5.254262915657552e-13, 2.480271874136002e-13, 8.781082144697324e-14, 2.48706295260579e-14, 5.870083387121297e-15, 1.1875583930028655e-15, 2.1021985350326767e-16, 3.3078054803550226e-17, 4.684343187465375e-18, 6.030658867686448e-19, 7.116922873928791e-20, 7.912171937585713e-21, 8.106206320677691e-22], [2.854245633531574e-14, 4.0420351705056853e-14, 2.8620606663396674e-14, 1.3510341387065605e-14, 4.783161828340029e-15, 1.3547333214239853e-15, 3.197505537903078e-16, 6.468774441161917e-17, 1.1450930104819351e-17, 1.8018017197074583e-18, 2.5516184857306504e-19, 3.284972947562876e-20, 3.8766741120139664e-21, 4.2230350360186993e-22, 4.359568018763067e-23]] |
| Legacy trial inputs | {"lambda_home": 0.7625969612093745, "lambda_away": 1.416148324103575, "rho": -0.03104744974939825, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1935 |
| Legacy p draw | 0.2795 |
| Legacy p away | 0.5270 |
| Legacy p over 1 5 | 0.6446 |
| Legacy p under 3 5 | 0.8231 |
| Legacy p btts yes | 0.4075 |
| Legacy p over 2 5 | 0.3721 |
| Legacy goal margin distribution | {"-1": 0.2627253518254558, "-10": 1.1270354252506712e-06, "-11": 1.4392569408043622e-07, "-12": 1.686772940832341e-08, "-13": 1.8220203593493482e-09, "-14": 1.711047456035761e-10, "-2": 0.16189895523059625, "-3": 0.07040250898506972, "-4": 0.023689324882792757, "-5": 0.006481924046593659, "-6": 0.0014922397502595973, "-7": 0.00029626052224800484, "-8": 5.167758037174215e-05, "-9": 8.035960553389618e-06, "0": 0.2794884657062441, "1": 0.1351587646017936, "10": 2.2357412875261664e-09, "11": 1.537477043974604e-10, "12": 9.703161517172486e-12, "13": 5.644119344419203e-13, "14": 2.854245633531574e-14, "2": 0.04541898295289605, "3": 0.010635742720802437, "4": 0.0019271641057931862, "5": 0.0002839594194135454, "6": 3.5202805323019147e-05, "7": 3.7635594539898152e-06, "8": 3.535195988450204e-07, "9": 2.9602981142874365e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1980 |
| Legacy raw p draw | 0.2802 |
| Legacy raw p away | 0.5218 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.7626 |
| Legacy lambda away | 1.4161 |
| Legacy model home team | Genoa |
| Legacy model away team | Juventus |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 47.3% |
| Market home draw odds | 2.05 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-28T16:07:35Z |
| Market reference home draw last update utc | 2026-10-28T16:07:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.8% |
| Market draw away odds | 1.20 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-28T16:07:35Z |
| Market reference draw away last update utc | 2026-10-28T16:07:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-28T16:07:35Z |
| Market reference home away last update utc | 2026-10-28T16:07:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.05 |
| Market reference dc draw away odds | 1.20 |
| Market reference dc home away odds | 1.35 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.16, "price": 1.7, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.7, "price": 2.16, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.71, "price": 2.14, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.14, "price": 1.71, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 67.0% |
| Market over 1 5 odds | 1.46 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-28T16:07:31Z |
| Market reference over 1 5 odds | 1.44 |
| Market reference over 1 5 opposite odds | 2.75 |
| Market reference over 1 5 last update utc | 2026-10-28T16:07:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 80.9% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 4.70 |
| Market reference under 3 5 last update utc | 2026-10-28T16:07:06Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 43.2% |
| Market btts yes odds | 2.22 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-28T16:07:35Z |
| Market reference btts yes odds | 2.22 |
| Market reference btts yes opposite odds | 1.71 |
| Market reference btts yes last update utc | 2026-10-28T16:07:35Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021258779398154137, "mu": 8.486296138396419, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,403.5028 |
| Elo away rating | 1,567.3505 |
| Elo rating diff | -103.8477 |
| Elo home expectancy | 0.3548 |

</details>


---

## 2026-10-28 — Monza vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **58.3%**. Expected goals are 0.87 for Monza and 2.00 for Napoli (2.87 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 56.6%; Under 3.5 goals: 65.2%; Double Chance 1X: 41.7%; Double Chance X2: 81.3%; Double Chance 12 (either team wins): 77.0%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 53.8%; BTTS No (at least one team does not score): 46.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 18.7% | 5.35 |
| Draw | 23.0% | 4.35 |
| Napoli win | 58.3% | 1.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 0.87 |
| Napoli expected goals | 2.00 |
| Expected total goals | 2.87 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 79.8% |
| Under 1.5 | 20.2% |
| Over 2.5 | 56.6% |
| Under 2.5 | 43.4% |
| Over 3.5 | 34.8% |
| Under 3.5 | 65.2% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.89% |
| 2 | 0-2 | 9.78% |
| 3 | 0-1 | 9.11% |
| 4 | 1-2 | 8.94% |
| 5 | 0-3 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 18.7% | 20.1% | 4.71 | -12.0% |
| Draw | 23.0% | 23.8% | 4.01 | -7.7% |
| Napoli win | 58.3% | 56.1% | 1.75 | +2.0% |

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
| Market best home last update utc | 2026-10-28T16:07:31Z |
| Market best draw last update utc | 2026-10-28T16:07:31Z |
| Market best away last update utc | 2026-10-28T16:07:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Monza |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8693 |
| Dc lambda away | 1.9998 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:07:21.315970+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 53.8% |
| P btts no | 46.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.29 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.96 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 2.88 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.56 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.21419309786417623, "-10": 2.4466382848324744e-05, "-11": 4.609689394474668e-06, "-12": 7.97855472156556e-07, "-13": 1.2768978072980046e-07, "-14": 1.9001857222372378e-08, "-15": 2.641609856445904e-09, "-16": 3.4282578146275917e-10, "-17": 3.8090798976472744e-11, "-2": 0.17759992038326428, "-3": 0.10852369831500056, "-4": 0.052303452215827474, "-5": 0.020720815474042555, "-6": 0.006952496216968259, "-7": 0.002020483293107057, "-8": 0.0005174350241104302, "-9": 0.00011838284801268005, "0": 0.2301336589900508, "1": 0.1257674680889019, "10": 8.055381195735933e-09, "11": 6.597311896461331e-10, "12": 4.963620903680643e-11, "13": 3.4531030704972198e-12, "14": 2.2337186722559403e-13, "15": 1.349833257130761e-14, "16": 7.6148954668521e-16, "17": 3.6778124384334057e-17, "2": 0.04586980643072009, "3": 0.012183939945407745, "4": 0.0025525399190187152, "5": 0.00043957001003748535, "6": 6.411224672008288e-05, "7": 8.099058249377105e-06, "8": 9.016004177150723e-07, "9": 8.966564767889919e-08} |
| Raw goal margin distribution | {"-1": 0.24299216180014133, "-10": 1.871488796872223e-05, "-11": 3.3585418622863214e-06, "-12": 5.535773894655035e-07, "-13": 8.435612221751172e-08, "-14": 1.1951114787783135e-08, "-15": 1.5816481522703643e-09, "-16": 1.9556228355792283e-10, "-17": 2.0870400022614623e-11, "-2": 0.1953059682667319, "-3": 0.11482023205837881, "-4": 0.05303654427650338, "-5": 0.02009271136537811, "-6": 0.006438122363701738, "-7": 0.001785107079097559, "-8": 0.00043589426183034764, "-9": 9.504587936617494e-05, "0": 0.21203105024470598, "1": 0.1043547387065995, "10": 4.50793315786331e-09, "11": 3.516576144856184e-10, "12": 2.5195711490636852e-11, "13": 1.6689522616043922e-12, "14": 1.0278145191871487e-13, "15": 5.912827819127214e-15, "16": 3.1779676916070376e-16, "17": 1.4742603137927285e-17, "2": 0.03690401024220993, "3": 0.009430951058710507, "4": 0.0018936133786517507, "5": 0.0003118413225552825, "6": 4.343435417536072e-05, "7": 5.23500905924893e-06, "8": 5.556653817878189e-07, "9": 5.2667718502606714e-08} |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 63.5% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 50.4% |
| P home draw | 41.7% |
| P draw away | 81.3% |
| P home away | 77.0% |
| Raw p home draw | 36.5% |
| Raw p draw away | 84.7% |
| Raw p home away | 78.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0513 |
| Totals anchor target over 2 5 | 0.5665 |
| Totals anchor reference over odds | 1.72 |
| Totals anchor reference under odds | 2.22 |
| Totals anchor reference last update utc | 2026-10-28T16:07:31Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5364 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:06:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.2, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:06:35Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.62, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:06:35Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.99, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:06:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:06:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:06:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:06:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:06:35Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:06:35Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:06:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.13, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.71, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:35Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.59, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:35Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.32, "price": 3.59, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.71 |
| Reference draw odds | 4.01 |
| Reference away odds | 1.75 |
| Market reference 1x2 last update utc | 2026-10-28T16:07:31Z |
| Market reference home last update utc | 2026-10-28T16:07:31Z |
| Market reference draw last update utc | 2026-10-28T16:07:31Z |
| Market reference away last update utc | 2026-10-28T16:07:31Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.26 |
| Market reference over 2 5 last update utc | 2026-10-28T16:07:31Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:07:31Z |
| Home probability edge | -1.5% |
| Draw probability edge | -0.8% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | -0.0485 |
| Raw ev home | -0.2796 |
| Raw edge prob draw | -0.0259 |
| Raw ev draw | -0.1498 |
| Raw edge prob away | 0.0743 |
| Raw ev away | 0.1113 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06852824348945699, 0.11161480032366734, 0.1106269386760329, 0.07119407823585631, 0.03436276577283158, 0.01326851559363302, 0.004269483312799304, 0.0011775558440023299, 0.00028418147024692885, 6.09617575010048e-05, 1.1769600202799718e-05, 2.0657285755441975e-06, 3.3235042834372443e-07, 4.935795096648413e-08, 6.806648410396993e-09, 8.760850932933865e-10, 1.0571352141879387e-10], [0.057238873114710966, 0.10898787685489883, 0.09283249678549992, 0.059742447165887384, 0.028835484207775302, 0.011134263009857186, 0.003582733108722049, 0.0009881449347813858, 0.00023847062694605783, 5.1156004360052984e-05, 9.876449498369188e-06, 1.7334542891989821e-06, 2.7889156511173115e-07, 4.1418680470344484e-08, 5.71179293434703e-09, 7.351660235772437e-10, 8.870940708241947e-11], [0.0255473288579106, 0.04932302794946491, 0.042813715321558206, 0.025066410590672335, 0.012098635409526038, 0.004671653430175817, 0.0015032236441647083, 0.00041460046973881674, 0.00010005620680798147, 2.1463757684829104e-05, 4.143906887790183e-06, 7.273133092886476e-07, 1.1701580388822092e-07, 1.737822436216394e-08, 2.396522969735251e-09, 3.084569560421582e-10, 3.722020986198739e-11], [0.0071460060646569646, 0.013796458283934564, 0.013318087016588875, 0.007706971906917874, 0.0033841863660738695, 0.0013067379345091425, 0.00042047625947440407, 0.00011597053796275123, 2.7987358859828912e-05, 6.003764363749636e-06, 1.1591185879440032e-06, 2.034414379675181e-07, 3.273123577406854e-08, 4.860973817485412e-09, 6.703467032137483e-10, 8.628045972330134e-11, 1.0411101954371595e-11], [0.0014991411517069995, 0.0028943214117252624, 0.002793965206289188, 0.0017980591333845442, 0.0007803818527415518, 0.0002741369926633697, 8.821056939925345e-05, 2.4329143338602096e-05, 5.87139179770275e-06, 1.259513375921145e-06, 2.4316833195673743e-07, 4.26794252425804e-08, 6.866596816621361e-09, 1.0197704593625292e-09, 1.4063020932337956e-10, 1.8100542679235535e-11, 2.1841167266298503e-12], [0.0002516005917047063, 0.0004857534455274583, 0.0004689106814953957, 0.0003017679431749873, 0.00014565229870268454, 5.057204564956117e-05, 1.480436410553482e-05, 4.083155780688801e-06, 9.853946366225111e-07, 2.1138390489842805e-07, 4.081089771600053e-08, 7.162880314787555e-09, 1.1524197171776703e-09, 1.7114789403682444e-10, 2.3601942910466108e-11, 3.0378108446202076e-12, 3.665599200892451e-13], [3.5188401969397786e-05, 6.79365949953783e-05, 6.558099659626354e-05, 4.220471666609841e-05, 2.03706660615973e-05, 7.865737643990647e-06, 2.2758906355662556e-06, 5.710627544277757e-07, 1.3781550487233204e-07, 2.9563769166953448e-08, 5.707738061475084e-09, 1.0017874364590229e-09, 1.611753294010597e-10, 2.3936433737214552e-11, 3.3009248856099743e-12, 4.248627095160052e-13, 5.1266404926063654e-14], [4.21833086924593e-06, 8.144133287714838e-06, 7.861747817321108e-06, 5.059435756565788e-06, 2.4420037474127704e-06, 9.429323884014773e-07, 3.0341254596029725e-07, 7.524864381830386e-08, 1.65211082608768e-08, 3.5440586417273736e-09, 6.842347566459362e-10, 1.200927189394092e-10, 1.9321447673715063e-11, 2.869462427454472e-12, 3.957097385138502e-13, 5.093188046167768e-14, 6.145736843717686e-15], [4.424760726750168e-07, 8.542677718246677e-07, 8.246473324155035e-07, 5.307026245470803e-07, 2.561506579511227e-07, 9.890760894546483e-08, 3.182604586937947e-08, 8.777864570315442e-09, 1.9048556549981345e-09, 3.717492054865311e-10, 7.177187311590867e-11, 1.2596962229914738e-11, 2.026696944848603e-12, 3.0098835414860215e-13, 4.150743420659313e-14, 5.342430250063605e-15, 6.446486979311951e-16], [4.1255933466173825e-08, 7.965089308361372e-08, 7.688911916414387e-08, 4.94820703778914e-08, 2.388317731591737e-08, 9.222025745445086e-09, 2.9674219962688876e-09, 8.184374682650846e-10, 1.9751484757294087e-10, 3.809960042929424e-11, 6.691922580381789e-12, 1.1745255116087786e-12, 1.8896677012902063e-13, 2.8063789840152908e-14, 3.870102926981347e-15, 4.981217303159795e-16, 6.010626434582033e-17], [3.461987972113275e-09, 6.683897579232858e-09, 6.452143567443497e-09, 4.152283516357192e-09, 2.0041546913814817e-09, 7.738654667801119e-10, 2.490109517868585e-10, 6.867910705217019e-11, 1.6574440793394192e-11, 3.555499376802094e-12, 6.172538243205474e-13, 9.85602034059827e-14, 1.585712963814404e-14, 2.354970417968696e-15, 3.247593414662443e-16, 4.179984051060443e-17, 5.043811804294862e-18], [2.6410219225323087e-10, 5.098896985462152e-10, 4.922100465456655e-10, 3.167622731102335e-10, 1.5288951084522369e-10, 5.903531957129807e-11, 1.899611979929233e-11, 5.239273758481733e-12, 1.2644024716916493e-12, 2.712358296829187e-13, 5.236622772875293e-14, 8.264599019788142e-15, 1.2096814703030676e-15, 1.7965193844893285e-16, 2.477468284893982e-17, 3.188754439244144e-18, 3.8477365188934045e-19], [1.8468426562591544e-11, 3.565612376134116e-11, 3.441980174584174e-11, 2.215089821415273e-11, 1.0691424706267332e-11, 4.128286307658636e-12, 1.3283814136273224e-12, 3.6637765792210745e-13, 8.841851707011259e-14, 1.896727535241158e-14, 3.661922769051105e-15, 6.427183910346734e-16, 9.298280934780222e-17, 1.2562896974705985e-17, 1.7324710821348508e-18, 2.22986703309343e-19, 2.6906872194096725e-20], [1.1921356657884807e-12, 2.301600339130255e-12, 2.221795837968163e-12, 1.429838957901801e-12, 6.901307302621082e-13, 2.664805975358358e-13, 8.574692898653917e-14, 2.36496526478164e-14, 5.707409202303903e-15, 1.2243363208992125e-15, 2.3637686315905377e-16, 4.1487427984937387e-17, 6.674819056535993e-18, 8.913726970017403e-19, 1.1183088932673565e-19, 1.4393776378877395e-20, 1.736836751559954e-21], [7.14556842293943e-14, 1.3795613349625153e-13, 1.3317271379095222e-13, 8.570343460628018e-14, 4.136589899438525e-14, 1.597263967284032e-14, 5.139604205407245e-15, 1.4175417783675845e-15, 3.4209766676012465e-16, 7.338576644201754e-17, 1.4168245257436125e-17, 2.486724152842696e-18, 4.0008346069968604e-19, 5.941710360996819e-20, 7.367949225881385e-21, 8.62751756627728e-22, 1.0410464348903658e-22], [3.99746490678108e-15, 7.717717747353323e-15, 7.450117589121638e-15, 4.7945307070235885e-15, 2.314143813061175e-15, 8.935617543855633e-16, 2.8752628524139557e-16, 7.930192781765343e-17, 1.9138063434885375e-17, 4.105440024441346e-18, 7.926180235773309e-19, 1.3911549012561806e-19, 2.238197858124518e-20, 3.3239872951313364e-21, 4.583904395453705e-22, 5.305269796744054e-23, 5.823954573640316e-24], [2.096543191412661e-16, 4.0476974717177654e-16, 3.9073497006066595e-16, 2.5145788504053343e-16, 1.21369482118354e-16, 4.6864471757735464e-17, 1.5079839091331274e-17, 4.159133868816844e-18, 1.003730552410073e-18, 2.1531727061305024e-19, 4.1570294160759195e-20, 7.296164955648293e-21, 1.173863583523972e-21, 1.743325606218121e-22, 2.4041120496323957e-23, 3.0943374805032855e-24, 3.3574602347718527e-25]] |
| Legacy trial inputs | {"lambda_home": 0.8391491068676917, "lambda_away": 1.9306530331914633, "rho": -0.03104744974939825, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1773 |
| Legacy p draw | 0.2289 |
| Legacy p away | 0.5938 |
| Legacy p over 1 5 | 0.7626 |
| Legacy p under 3 5 | 0.7030 |
| Legacy p btts yes | 0.4929 |
| Legacy p over 2 5 | 0.5175 |
| Legacy goal margin distribution | {"-1": 0.23318742338508597, "-10": 1.3625074988990978e-05, "-11": 2.3626871788239053e-06, "-12": 3.762540963602541e-07, "-13": 5.538861195882768e-08, "-14": 7.579034643836225e-09, "-15": 9.64794500375806e-10, "-16": 1.0571352141879387e-10, "-2": 0.18386719434366136, "-3": 0.10514703693204931, "-4": 0.047122311570404696, "-5": 0.017295137876641133, "-6": 0.0053639387140514945, "-7": 0.0014386932034036665, "-8": 0.00033969186402995163, "-9": 7.159929534784742e-05, "0": 0.22887011455408326, "1": 0.12183187764202986, "10": 4.007769585903821e-09, "11": 3.0206817629543133e-10, "12": 2.090811551570189e-11, "13": 1.3377933747588944e-12, "14": 7.956413694680829e-14, "15": 4.402234653952856e-15, "16": 2.096543191412661e-16, "2": 0.04246086655109206, "3": 0.01055398682328479, "4": 0.002055800656610866, "5": 0.0003279543135530146, "6": 4.4208729202294285e-05, "7": 5.153797148732075e-06, "8": 5.289068347243979e-07, "9": 4.8454898385221856e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1531 |
| Legacy raw p draw | 0.2198 |
| Legacy raw p away | 0.6270 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.8391 |
| Legacy lambda away | 1.9307 |
| Legacy model home team | Monza |
| Legacy model away team | Napoli |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 44.7% |
| Market home draw odds | 2.17 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-28T16:07:35Z |
| Market reference home draw last update utc | 2026-10-28T16:07:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 79.5% |
| Market draw away odds | 1.22 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-28T16:07:35Z |
| Market reference draw away last update utc | 2026-10-28T16:07:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-28T16:07:35Z |
| Market reference home away last update utc | 2026-10-28T16:07:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.17 |
| Market reference dc draw away odds | 1.22 |
| Market reference dc home away odds | 1.28 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.37, "price": 1.57, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.57, "price": 2.37, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.88, "price": 1.96, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.96, "price": 1.88, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.51, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:35Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.51, "price": 1.51, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 79.6% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-28T16:07:32Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.0% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-28T16:07:31Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.76 |
| Market reference under 3 5 last update utc | 2026-10-28T16:07:31Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.3% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-28T16:07:35Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.25 |
| Market reference btts yes last update utc | 2026-10-28T16:07:35Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021258779398154137, "mu": 8.879405450540954, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,361.2116 |
| Elo away rating | 1,577.1183 |
| Elo rating diff | -155.9067 |
| Elo home expectancy | 0.2896 |

</details>


---

## 2026-10-28 — Parma vs Udinese

The model's most likely 1X2 outcome is **Udinese win** at **35.6%**. Expected goals are 1.02 for Parma and 1.15 for Udinese (2.17 combined). The most likely exact score is 1-1 at 14.6%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 44.8%; Under 3.5 goals: 75.7%; Double Chance 1X: 64.4%; Double Chance X2: 66.2%; Double Chance 12 (either team wins): 69.4%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 52.1%; BTTS No (at least one team does not score): 47.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 33.8% | 2.96 |
| Draw | 30.6% | 3.26 |
| Udinese win | 35.6% | 2.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.02 |
| Udinese expected goals | 1.15 |
| Expected total goals | 2.17 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 71.7% |
| Under 1.5 | 28.3% |
| Over 2.5 | 44.8% |
| Under 2.5 | 55.2% |
| Over 3.5 | 24.3% |
| Under 3.5 | 75.7% |
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.57% |
| 2 | 1-0 | 9.59% |
| 3 | 0-0 | 9.38% |
| 4 | 0-1 | 9.37% |
| 5 | 2-1 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 33.8% | 34.7% | 2.81 | -5.1% |
| Draw | 30.6% | 30.9% | 3.14 | -3.8% |
| Udinese win | 35.6% | 34.4% | 2.83 | +0.7% |

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
| Market best home last update utc | 2026-10-28T16:07:31Z |
| Market best draw last update utc | 2026-10-28T16:07:31Z |
| Market best away last update utc | 2026-10-28T16:07:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Parma |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0178 |
| Dc lambda away | 1.1488 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:07:21.315970+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 52.1% |
| P btts no | 47.9% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.66 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.53 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.35 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.19214077157080428, "-10": 4.0431543461199974e-07, "-11": 4.839327904916539e-08, "-12": 5.317982939402684e-09, "-13": 5.374928219740915e-10, "-14": 4.598064240058828e-11, "-2": 0.10514778140428577, "-3": 0.041617763308506965, "-4": 0.01289533358407753, "-5": 0.003270332720319959, "-6": 0.0007005705921241017, "-7": 0.0001297568706683511, "-8": 2.1152820268323825e-05, "-9": 3.0779421256571278e-06, "0": 0.306290056244734, "1": 0.19689043028710598, "10": 1.395323375783074e-07, "11": 1.4795818270863462e-08, "12": 1.4404568958251076e-09, "13": 1.2898089465259165e-10, "14": 9.775233491659429e-12, "2": 0.09562238047899023, "3": 0.03353030951485063, "4": 0.009204300662271113, "5": 0.002067995283852606, "6": 0.0003924721969162514, "7": 6.440013022097259e-05, "8": 9.30088020336099e-06, "9": 1.1989901351175415e-06} |
| Raw goal margin distribution | {"-1": 0.22205407307719724, "-10": 1.4052652160607405e-07, "-11": 1.4546745072752645e-08, "-12": 1.3776139212397467e-09, "-13": 1.116943185994721e-10, "-2": 0.10972665744396017, "-3": 0.0384700237326022, "-4": 0.010459594618993137, "-5": 0.002315381733425604, "-6": 0.00043155187225405286, "-7": 6.939857845377483e-05, "-8": 9.808496233765703e-06, "-9": 1.236123674034696e-06, "0": 0.29926536211847854, "1": 0.19637602623276343, "10": 4.185546645665366e-08, "11": 3.8384784504993455e-09, "12": 3.2204769162317676e-10, "13": 2.3132530302338073e-11, "2": 0.086121369556526, "3": 0.02674980504331237, "4": 0.006443360180813168, "5": 0.0012636288932332588, "6": 0.00020865526078743722, "7": 2.9726672423369908e-05, "8": 3.722181459099284e-06, "9": 4.155817091410834e-07} |
| Unadjusted home-win probability | 31.7% |
| Unadjusted draw probability | 29.9% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 64.0% |
| Raw p under 3 5 | 82.6% |
| Raw p btts yes | 43.9% |
| P home draw | 64.4% |
| P draw away | 66.2% |
| P home away | 69.4% |
| Raw p home draw | 61.6% |
| Raw p draw away | 68.3% |
| Raw p home away | 70.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1596 |
| Totals anchor target over 2 5 | 0.4483 |
| Totals anchor reference over odds | 2.16 |
| Totals anchor reference under odds | 1.77 |
| Totals anchor reference last update utc | 2026-10-28T16:07:31Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3658 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.03, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.08, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 5.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 5.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.97, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.97, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.81 |
| Reference draw odds | 3.14 |
| Reference away odds | 2.83 |
| Market reference 1x2 last update utc | 2026-10-28T16:07:31Z |
| Market reference home last update utc | 2026-10-28T16:07:31Z |
| Market reference draw last update utc | 2026-10-28T16:07:31Z |
| Market reference away last update utc | 2026-10-28T16:07:31Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.18 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-10-28T16:07:31Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:07:31Z |
| Home probability edge | -0.9% |
| Draw probability edge | -0.3% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.0294 |
| Raw ev home | -0.1087 |
| Raw edge prob draw | -0.0100 |
| Raw ev draw | -0.0603 |
| Raw edge prob away | 0.0394 |
| Raw ev away | 0.0854 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.11653679016321386, 0.11800635113077002, 0.07068637215451865, 0.02731184160280677, 0.007914573937670132, 0.0018348226099380986, 0.000354469913821107, 5.869726780925259e-05, 8.504806683702583e-06, 1.0953640516921475e-06, 1.2696821989319818e-07, 1.3379469458282766e-08, 1.2923917985754559e-09, 1.1523579118334075e-10], [0.11541364092350168, 0.1402652238207765, 0.07386526922425936, 0.02854010570229394, 0.008270506985750568, 0.001917337980870929, 0.0003704110823379175, 6.13369926522921e-05, 8.887283591506445e-06, 1.1446246017542134e-06, 1.3267821589195143e-07, 1.3981168979127416e-08, 1.3505130513180303e-09, 1.2041815813409044e-10], [0.06255319204314999, 0.07250801621695277, 0.041195758585887324, 0.014911803556564325, 0.0043212235011026185, 0.0010017821104281667, 0.00019353457736330116, 3.204771540519885e-05, 4.64348059710829e-06, 5.980502449925268e-07, 6.932250049295329e-08, 7.304964020897858e-09, 7.056240622196462e-10, 6.29167928622818e-11], [0.021788774980103932, 0.025256278664645956, 0.014637803469188153, 0.0055443563291911885, 0.001505185641674578, 0.0003489447024247139, 6.741272858033571e-05, 1.1162986840201621e-05, 1.6174355064898824e-06, 2.0831522404083545e-07, 2.414668724270975e-08, 2.544493927333137e-09, 2.4578576104709534e-10, 2.1915425853894348e-11], [0.005692164136157679, 0.006598025072955081, 0.003824023150246872, 0.0014775282898477665, 0.00041973220278336825, 9.115934798802973e-05, 1.7611100958907065e-05, 2.916251758174461e-06, 4.2254364419278714e-07, 5.4420886368492814e-08, 6.308152122158131e-09, 6.647311329371303e-10, 6.420980048157915e-11, 5.725250785694476e-12], [0.0011896302598946801, 0.00137895009605776, 0.0007991993107110646, 0.00030879509469658944, 8.948432127384795e-05, 2.0336369349228048e-05, 3.6806209570966774e-06, 6.094802001505917e-07, 8.830924288792962e-08, 1.1373658883622812e-08, 1.3183682812076722e-09, 1.3892506461872306e-10, 1.3419486825664259e-11, 1.1965451833835297e-12], [0.00020718835598739215, 0.00024016067262458296, 0.0001391901306437363, 5.378036366763366e-05, 1.5584766155004804e-05, 3.6129906090963433e-06, 6.842456722764921e-07, 1.0614827558879289e-07, 1.5380112182134032e-08, 1.9808588980141046e-09, 2.2960962408061479e-10, 2.4195463678221937e-11, 2.337164333605633e-12, 2.083926727215346e-13], [3.0929428582451485e-05, 3.585159183707969e-05, 2.0778538372057482e-05, 8.028423746446278e-06, 2.326520278942512e-06, 5.393533554555223e-07, 1.0419783165517779e-07, 1.6914420312195655e-08, 2.2959691873627966e-09, 2.957059701838119e-10, 3.427651344594414e-11, 3.611939784397937e-12, 3.4889584888692805e-13, 3.1109211023611335e-14], [4.0400477835409e-06, 4.682988040069589e-06, 2.714123465665292e-06, 1.0486846039102146e-06, 3.0389352558674595e-07, 7.045113434425823e-08, 1.3610475140401154e-08, 2.253781416073825e-09, 3.201240358173962e-10, 3.8625551915263693e-11, 4.477248967133053e-12, 4.717969257446746e-13, 4.557329267253253e-14, 4.063531232353773e-15], [4.6908180163274895e-07, 5.437322983678073e-07, 3.1513140273112e-07, 1.2176065475037203e-07, 3.528446447279887e-08, 8.17993914822244e-09, 1.5802848238447037e-09, 2.616820156052036e-10, 3.791581854467645e-11, 4.787120985903426e-12, 5.198443494696543e-13, 5.4779389697994104e-14, 5.2914231163948565e-15, 4.718084175214448e-16], [4.90177279010189e-08, 5.681849468390899e-08, 3.293034455477372e-08, 1.272364569000358e-08, 3.687127218836182e-09, 8.547806161288236e-10, 1.651353159122881e-10, 2.7345034049239335e-11, 3.962096312622336e-12, 5.102923595553284e-13, 5.798498414179223e-14, 5.7242920306305225e-15, 5.529388213863642e-16, 4.930265158651998e-17], [4.656558718863198e-09, 5.39761160181272e-09, 3.1282984670636557e-09, 1.2087137819433847e-09, 3.5026765077931224e-10, 8.120197122941703e-11, 1.5687432445998988e-11, 2.597708261319669e-12, 3.7638901106907e-13, 4.847646836782995e-14, 5.619109816379256e-15, 5.804586821520855e-16, 5.252777311351255e-17, 4.6836257398930136e-18], [4.054977323817554e-10, 4.700293493446686e-10, 2.7241532023831457e-10, 1.0525598994191858e-10, 3.0501652978697975e-11, 7.071147855405041e-12, 1.366077111403316e-12, 2.2621100107412273e-13, 3.277632683201287e-14, 4.221378744222045e-15, 4.893176326362546e-16, 5.156259044005635e-17, 4.882586640433881e-18, 4.0785475530631525e-19], [3.259490126190562e-11, 3.778211074597008e-11, 2.1897410901027705e-11, 8.460734365219674e-12, 2.4517976002627392e-12, 5.683961900390475e-13, 1.0980862531783609e-13, 1.8183394518779328e-14, 2.6346414578999894e-15, 3.3932476650075486e-16, 3.933255021626783e-17, 4.144727356007614e-18, 4.0036054186883176e-19, 3.4994870680216435e-20]] |
| Legacy trial inputs | {"lambda_home": 1.044971852039481, "lambda_away": 1.1591417455872726, "rho": -0.03104744974939825, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3343 |
| Legacy p draw | 0.3040 |
| Legacy p away | 0.3617 |
| Legacy p over 1 5 | 0.6500 |
| Legacy p under 3 5 | 0.8189 |
| Legacy p btts yes | 0.4504 |
| Legacy p over 2 5 | 0.3765 |
| Legacy goal margin distribution | {"-1": 0.20838355800560934, "-10": 1.4167692836039913e-07, "-11": 1.4792899302463079e-08, "-12": 1.4128099567095463e-09, "-13": 1.1523579118334075e-10, "-2": 0.10391488232184971, "-3": 0.036654550004179456, "-4": 0.01003704363331525, "-5": 0.0022389546069907776, "-6": 0.0004206651517400085, "-7": 6.82074266920067e-05, "-8": 9.721363686222748e-06, "-9": 1.2355987426168295e-06, "0": 0.3039828989562638, "1": 0.20413019270141813, "10": 5.4696215557435157e-08, "11": 5.148485479108894e-09, "12": 4.4327984312772546e-10, "13": 3.259490126190562e-11, "2": 0.09195842694841809, "3": 0.029242178306861506, "4": 0.007218645027836497, "5": 0.0014516543106565976, "6": 0.00024587960165833807, "7": 3.5940629119549456e-05, "8": 4.617950210294593e-06, "9": 5.291363025712638e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3220 |
| Legacy raw p draw | 0.2987 |
| Legacy raw p away | 0.3794 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0450 |
| Legacy lambda away | 1.1591 |
| Legacy model home team | Parma |
| Legacy model away team | Udinese |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 65.1% |
| Market home draw odds | 1.48 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-28T16:07:14Z |
| Market reference home draw last update utc | 2026-10-28T16:07:32Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 65.1% |
| Market draw away odds | 1.48 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-28T16:07:14Z |
| Market reference draw away last update utc | 2026-10-28T16:07:32Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.8% |
| Market home away odds | 1.40 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-28T16:07:14Z |
| Market reference home away last update utc | 2026-10-28T16:07:32Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.49 |
| Market reference dc draw away odds | 1.49 |
| Market reference dc home away odds | 1.39 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:14Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.2, "price": 1.68, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:14Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.2, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:14Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.09, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:14Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.09, "price": 1.75, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 71.6% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-28T16:07:31Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.10 |
| Market reference over 1 5 last update utc | 2026-10-28T16:07:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.3% |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.80 |
| Market reference under 3 5 last update utc | 2026-10-28T16:07:06Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 53.9% |
| Market btts yes odds | 1.82 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-28T16:07:14Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-28T16:07:32Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021258779398154137, "mu": 9.245453887606375, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,368.8636 |
| Elo away rating | 1,450.0685 |
| Elo rating diff | -21.2049 |
| Elo home expectancy | 0.4695 |

</details>


---

## 2026-10-28 — Venezia vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **74.1%**. Expected goals are 0.67 for Venezia and 2.71 for Inter Milan (3.38 combined). The most likely exact score is 0-2 at 10.1%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 68.1%; Under 3.5 goals: 52.6%; Double Chance 1X: 25.9%; Double Chance X2: 89.8%; Double Chance 12 (either team wins): 84.3%; Under 4.5 goals: 71.5%; BTTS Yes (both teams score): 50.4%; BTTS No (at least one team does not score): 49.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 10.2% | 9.77 |
| Draw | 15.7% | 6.37 |
| Inter Milan win | 74.1% | 1.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.67 |
| Inter Milan expected goals | 2.71 |
| Expected total goals | 3.38 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 68.1% |
| Under 2.5 | 31.9% |
| Over 3.5 | 47.4% |
| Under 3.5 | 52.6% |
| Over 4.5 | 28.5% |
| Under 4.5 | 71.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 10.13% |
| 2 | 0-3 | 9.88% |
| 3 | 1-1 | 7.34% |
| 4 | 1-2 | 7.27% |
| 5 | 0-4 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 10.2% | 11.8% | 7.72 | -21.0% |
| Draw | 15.7% | 16.7% | 5.54 | -13.1% |
| Inter Milan win | 74.1% | 71.4% | 1.38 | +2.2% |

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
| Market best home last update utc | 2026-10-28T16:07:31Z |
| Market best draw last update utc | 2026-10-28T16:07:31Z |
| Market best away last update utc | 2026-10-28T16:07:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Venezia |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6651 |
| Dc lambda away | 2.7122 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:07:21.315970+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 50.4% |
| P btts no | 49.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.95 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.52 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.14 |
| Fair Over 3.5 odds | 2.11 |
| Fair Under 3.5 odds | 1.90 |
| Fair Over 4.5 odds | 3.51 |
| Fair Under 4.5 odds | 1.40 |
| Goal margin distribution | {"-1": 0.1711823218092755, "-10": 0.0003636298718051746, "-11": 9.526727566811296e-05, "-12": 2.2933128099858143e-05, "-13": 5.105396617866795e-06, "-14": 1.056965308736479e-06, "-15": 2.044836088905675e-07, "-16": 3.71248756188783e-08, "-17": 6.349008753388599e-09, "-18": 1.0260271790569366e-09, "-19": 1.5646526499603858e-10, "-2": 0.1936930002810981, "-20": 2.0722873701855203e-11, "-3": 0.1630073392073843, "-4": 0.10859320548052051, "-5": 0.059592372109374334, "-6": 0.02773409556530525, "-7": 0.01118925961363603, "-8": 0.003980531041152202, "-9": 0.0012656248022393356, "0": 0.1568839393339766, "1": 0.07569429496034545, "10": 5.262404076659494e-10, "11": 3.3808236097672964e-11, "12": 1.9957042876793626e-12, "13": 1.0894730875070528e-13, "14": 5.530977356229965e-15, "15": 2.6239392463744835e-16, "16": 1.168192485209003e-17, "17": 4.899022719989583e-19, "18": 1.9414066808732332e-20, "19": 7.259884667673791e-22, "2": 0.021439050696937734, "20": 2.3578484550908776e-23, "3": 0.004424384988721897, "4": 0.0007227740166653274, "5": 9.726233208769836e-05, "6": 1.1099978561819851e-05, "7": 1.0981549149106808e-06, "8": 9.57982114795821e-08, "9": 7.46922410151999e-09} |
| Raw goal margin distribution | {"-1": 0.203944443573508, "-10": 0.00023850593171294906, "-11": 5.80237280087764e-05, "-12": 1.2966036492134112e-05, "-13": 2.678824467461413e-06, "-14": 5.145844308920196e-07, "-15": 9.235537456199716e-08, "-16": 1.5553005703268618e-08, "-17": 2.4665943708496668e-09, "-18": 3.682917434913102e-10, "-19": 4.8014800488150825e-11, "-2": 0.22030141473448192, "-3": 0.17493865905826717, "-4": 0.10929866422786706, "-5": 0.0560530660747066, "-6": 0.024325282501441916, "-7": 0.009137841036697299, "-8": 0.003023708192246423, "-9": 0.0008935983196032656, "0": 0.13254148755287679, "1": 0.048951482005128034, "10": 1.8751691658172267e-10, "11": 1.11866750807579e-11, "12": 6.129947596462327e-13, "13": 3.10561707695815e-14, "14": 1.4628992531511237e-15, "15": 6.43834251131764e-17, "16": 2.6587674970671724e-18, "17": 1.0339936998709232e-19, "18": 3.78587496204113e-21, "19": 1.2103292775898814e-22, "2": 0.013247244128328584, "3": 0.0025795750861366566, "4": 0.0003952131274765602, "5": 4.970155854191019e-05, "6": 5.289110663201433e-06, "7": 4.872170599255316e-07, "8": 3.953419421373486e-08, "9": 2.865032053456345e-09} |
| Unadjusted home-win probability | 6.5% |
| Unadjusted draw probability | 13.3% |
| Unadjusted away-win probability | 80.2% |
| Raw p over 1 5 | 85.2% |
| Raw p under 3 5 | 56.3% |
| Raw p btts yes | 45.5% |
| P home draw | 25.9% |
| P draw away | 89.8% |
| P home away | 84.3% |
| Raw p home draw | 19.8% |
| Raw p draw away | 93.5% |
| Raw p home away | 86.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0792 |
| Totals anchor target over 2 5 | 0.6811 |
| Totals anchor reference over odds | 1.43 |
| Totals anchor reference under odds | 2.90 |
| Totals anchor reference last update utc | 2026-10-28T16:07:31Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6380 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:56:42Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 5.15, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:56:42Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.49, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:56:42Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:56:42Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:56:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:56:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:56:42Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:56:42Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:56:42Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:56:42Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:34Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.4, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:34Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.14, "price": 6.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 7.72 |
| Reference draw odds | 5.54 |
| Reference away odds | 1.38 |
| Market reference 1x2 last update utc | 2026-10-28T16:07:31Z |
| Market reference home last update utc | 2026-10-28T16:07:31Z |
| Market reference draw last update utc | 2026-10-28T16:07:31Z |
| Market reference away last update utc | 2026-10-28T16:07:31Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.91 |
| Market reference over 2 5 last update utc | 2026-10-28T16:07:10Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:07:10Z |
| Home probability edge | -1.6% |
| Draw probability edge | -1.0% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | -0.0531 |
| Raw ev home | -0.4964 |
| Raw edge prob draw | -0.0348 |
| Raw ev draw | -0.2657 |
| Raw edge prob away | 0.0879 |
| Raw ev away | 0.1071 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.04283794506188371, 0.09076795485352267, 0.12214525425910637, 0.1073290694642081, 0.07073256277081667, 0.03729163374733961, 0.01638408456054942, 0.006170014173136108, 0.0020330974496322973, 0.0005954944346731099, 0.0001569783384518547, 3.761915738081677e-05, 8.263991057617456e-06, 1.675747218382933e-06, 3.155313331607146e-07, 5.5451494338210366e-08, 9.135983204720289e-09, 1.4166690045788745e-09, 2.0747124250074466e-10, 2.878500623134049e-11], [0.030738586642789986, 0.07306100758480907, 0.08079610004634341, 0.07099555596254029, 0.04678786132813753, 0.024667504189316583, 0.010837671453970623, 0.004081313559367337, 0.001344844267105122, 0.0003939050126239533, 0.00010383733380062306, 2.488415306706855e-05, 5.4664280845243554e-06, 1.108465823990497e-06, 2.087162642252927e-07, 3.667980808133009e-08, 6.043229575374694e-09, 9.37091918313109e-10, 1.3723715561040392e-10, 1.9040578018434257e-11], [0.011072643607719559, 0.02918860520944271, 0.03089035041439443, 0.023480912448006652, 0.015474513306933533, 0.008158475531705034, 0.0035844273785984133, 0.0013498445791583302, 0.0004447908050577249, 0.0001302792687352745, 3.4342929085495845e-05, 8.230129500203242e-06, 1.8079542798955835e-06, 3.666115239447041e-07, 6.903035352431046e-08, 1.2131398233177269e-08, 1.998724323497788e-09, 3.0993169912289553e-10, 4.5389511946376453e-11, 6.297438471306501e-12], [0.0024414276977939883, 0.006435849625705049, 0.008482774329568312, 0.005984889643209686, 0.003412004100907754, 0.0017988773810973797, 0.0007903370317762426, 0.0002976297314379961, 9.807274844779951e-05, 2.872551726643646e-05, 7.572336043964172e-06, 1.814676497328884e-06, 3.986391878634063e-07, 8.08348539516846e-08, 1.522063050645519e-08, 2.674874466184316e-09, 4.4070242812114186e-10, 6.833741439446809e-11, 1.000801755941798e-11, 1.3885338726410604e-12], [0.00040373618632049844, 0.0010642893033294407, 0.0014027869677778698, 0.0012326293053411203, 0.0006522468425576028, 0.00029747835422638276, 0.00013069715699773636, 4.921869806545889e-05, 1.6218181466549953e-05, 4.750306880565795e-06, 1.252228799849276e-06, 3.0009103652711425e-07, 6.592251966801979e-08, 1.3367570002468899e-08, 2.5170187589918103e-09, 4.423410190845072e-10, 7.287847098342671e-11, 1.1300882305691857e-11, 1.6550147463793339e-12, 2.2962030406367537e-13], [5.341232371268849e-05, 0.0001408002718593511, 0.00018558185805870168, 0.0001630708311648892, 0.00010746778909982303, 4.549333741346193e-05, 1.7290594934063093e-05, 6.5113931395351146e-06, 2.145586122505338e-06, 6.284423775627999e-07, 1.6566374847263738e-07, 3.9700577083121494e-08, 8.721227077894884e-09, 1.7684641615381556e-09, 3.329892769122693e-10, 5.851955436064575e-11, 9.641465431494635e-12, 1.4950514826318917e-12, 2.1895036010647005e-13, 3.0377643687155164e-14], [5.888491092803844e-06, 1.5522656366122293e-05, 2.0459643808851e-05, 1.7977894801503598e-05, 1.1847885935119845e-05, 6.246444433299078e-06, 2.203540913815569e-06, 7.178545668625928e-07, 2.3654212910072026e-07, 6.928321191425566e-08, 1.826375337139437e-08, 4.3768268871926645e-09, 9.614797559220217e-10, 1.9496596926162988e-10, 3.671071121422279e-11, 6.451542465388987e-12, 1.0629322854464265e-12, 1.6482333526840583e-13, 2.4138385219642923e-14, 3.3490114609952503e-15], [5.564418461586469e-07, 1.4668368227994683e-06, 1.933364896596035e-06, 1.6988482814586877e-06, 1.1195838490563148e-06, 5.902671868927502e-07, 2.5933397203490383e-07, 7.84153093112157e-08, 2.2352405214971473e-08, 6.5470215947991425e-09, 1.7258609181194918e-09, 4.1359485733154673e-10, 9.085647952889532e-11, 1.8423603290600277e-11, 3.4690340190550296e-12, 6.09648234740319e-13, 1.0044338930532569e-13, 1.5575229633761207e-14, 2.2809931140629704e-15, 3.164698886001595e-16], [4.600908498748963e-08, 1.212845879742096e-07, 1.5985920263436645e-07, 1.4046832656830524e-07, 9.257216871350553e-08, 4.880591449862321e-08, 2.1442885436936214e-08, 8.07508692779804e-09, 2.1364695489601624e-09, 5.413368441814893e-10, 1.4270185142708943e-10, 3.419786105721891e-11, 7.51241754581706e-12, 1.5233454051393316e-12, 2.868351510746913e-13, 5.0408425675166115e-14, 8.30510585586451e-15, 1.2878292113837107e-15, 1.8860264871395131e-16, 2.616713696337421e-17], [3.3815427889416523e-09, 8.914087815166644e-09, 1.1749217226580168e-08, 1.0324040500064527e-08, 6.803802980540968e-09, 3.5871021620055716e-09, 1.5759938421529112e-09, 5.934969577899089e-10, 1.9556472925148548e-10, 4.599255216910804e-11, 1.0488198511079032e-11, 2.513449908571565e-12, 5.521422863872196e-13, 1.1196174997214115e-13, 2.1081604578646812e-14, 3.704882381166864e-15, 6.10402724286564e-16, 9.46519493775443e-17, 1.3861782448126795e-17, 1.9232134985906964e-18], [2.2368078984611985e-10, 5.896451199064074e-10, 7.771820004494511e-10, 6.829100436077934e-10, 4.5005493635084314e-10, 2.3727803991717434e-10, 1.0424814039266235e-10, 3.9258373049085414e-11, 1.2936128813175765e-11, 3.7889933489680255e-12, 8.019796179199943e-13, 1.6625856772432108e-13, 3.652286262070033e-14, 7.405996088004684e-15, 1.3944966122552473e-15, 2.4506891351972086e-16, 4.037664817938752e-17, 6.260995089720681e-18, 9.169230260257938e-19, 1.2721587194291428e-19], [1.3450852269347325e-11, 3.545780308026866e-11, 4.673517239291318e-11, 4.106620919991048e-11, 2.7063667229136066e-11, 1.4268511229247048e-11, 6.268872426373923e-12, 2.360768560328537e-12, 7.779030006241413e-13, 2.278478622217391e-13, 6.006299429315358e-14, 1.1557230684185332e-14, 2.196270989129956e-15, 4.453532167677261e-16, 8.385685661452892e-17, 1.4737008724937682e-17, 2.4280150752595984e-18, 3.7649956470950267e-19, 5.513837899946868e-20, 7.650017245546805e-21], [7.414508326273831e-13, 1.954539169009747e-12, 2.5761811809261044e-12, 2.263691132309297e-12, 1.4918295286553643e-12, 7.865226172610199e-13, 3.455588231209772e-13, 1.3013255811938793e-13, 4.288031835949203e-14, 1.2559649290154242e-14, 3.3108502150632407e-15, 7.934304601075588e-16, 1.399481336769949e-16, 2.454918891185893e-17, 4.62243840860907e-18, 8.123475874047535e-19, 1.3383938527713983e-19, 2.0753771593631035e-20, 3.039390828196495e-21, 4.2169161795423873e-22], [3.7727046323014947e-14, 9.945229882348175e-14, 1.3108314465690575e-13, 1.1518279628468642e-13, 7.590836675465333e-14, 4.002042200203144e-14, 1.758297806614421e-14, 6.621500485615972e-15, 2.1818678810590604e-15, 6.390693080637471e-16, 1.6846511452368657e-16, 4.037191193986047e-17, 8.868702610017965e-18, 1.443963541350521e-18, 2.352023091658166e-19, 4.1334467117404244e-20, 6.810113990029144e-21, 1.0560086627937964e-21, 1.546525184452009e-22, 2.1456822899788773e-23], [1.782537068939951e-15, 4.698947479914516e-15, 6.193449719428751e-15, 5.442186020175154e-15, 3.586537796369036e-15, 1.8908950656368298e-15, 8.307650144914772e-16, 3.128543370863897e-16, 1.0308944793127471e-16, 3.019490901810938e-17, 7.959682528300495e-18, 1.9075023515127295e-18, 4.1903071394480057e-19, 8.496978619825108e-20, 1.2846238413274559e-20, 1.952981403071165e-21, 3.2176599585873435e-22, 4.989456557067735e-23, 7.307061479798871e-24, 1.0137974193124311e-24], [7.860697998841903e-17, 2.0721592664545902e-16, 2.73121040026358e-16, 2.3999153511885447e-16, 1.5816047233988084e-16, 8.338539106685008e-17, 3.6635383357298424e-17, 1.3796366450468689e-17, 4.546076663286415e-18, 1.3315462832703733e-18, 3.5100902871454575e-19, 8.411774531140174e-20, 1.847857164910465e-20, 3.7470291079434325e-21, 7.055390436287271e-22, 9.955642225150465e-23, 1.4189356080242786e-23, 2.2002690354582575e-24, 3.22229503961046e-25, 4.4706814147542276e-26], [3.2497872400002157e-18, 8.566766900807601e-18, 1.1291430748058407e-17, 9.921783391910248e-18, 6.53870540451085e-18, 3.4473373729839386e-18, 1.5145881623311965e-18, 5.703724485498068e-19, 1.8794491194786433e-19, 5.50490824285489e-20, 1.4511493289901962e-20, 3.477614524955106e-21, 7.639452166657117e-22, 1.5491051029689697e-22, 2.916855197393913e-23, 5.126082973866953e-24, 6.781177885162577e-25, 9.096401155537688e-26, 1.3321683780225176e-26, 1.8482790482365417e-27], [1.2645028372887215e-19, 3.3333570023068943e-19, 4.393532611066568e-19, 3.860598347981016e-19, 2.544231645207185e-19, 1.3413702397420168e-19, 5.893312045226632e-20, 2.2193378404135096e-20, 7.31299795527653e-21, 2.1419777905533333e-21, 5.646469471144841e-22, 1.3531511785374322e-22, 2.9725358082422503e-23, 6.0276185894636256e-24, 1.1349578912940501e-24, 1.994575640167674e-25, 3.2861890859015935e-26, 4.0915052764018614e-27, 5.183510701936521e-28, 7.191714189253353e-29], [4.646876211722776e-21, 1.2249634324594814e-20, 1.6145635718436832e-20, 1.418717467231202e-20, 9.34970579787328e-21, 4.929353477398997e-21, 2.1657121473876193e-21, 8.155765184763278e-22, 2.6874274404647013e-22, 7.871477506766664e-23, 2.075000853453275e-23, 4.972646827659528e-24, 1.0923665434734929e-24, 2.215067978556156e-25, 4.170816126968613e-26, 7.329794620825058e-27, 1.2076298637052756e-27, 1.8726082990511078e-28, 2.201982822159602e-29, 2.642857303444711e-30], [1.6177868571432524e-22, 4.264649306806759e-22, 5.621022828113168e-22, 4.939194348874831e-22, 3.2550536034932874e-22, 1.716129913216039e-22, 7.539819200607108e-23, 2.8393891131790895e-23, 9.356145063089749e-24, 2.740415771055094e-24, 7.224012339319891e-25, 1.7312022779320386e-25, 3.8030198281508447e-26, 7.711649073730064e-27, 1.4520489047564685e-27, 2.551831566594251e-28, 4.204303348704408e-29, 6.519392720511309e-30, 9.547653712356521e-31, 1.0636103286619262e-31]] |
| Legacy trial inputs | {"lambda_home": 0.6614755565938801, "lambda_away": 2.6361008484995554, "rho": -0.03104744974939825, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0932 |
| Legacy p draw | 0.1535 |
| Legacy p away | 0.7533 |
| Legacy p over 1 5 | 0.8357 |
| Legacy p under 3 5 | 0.5904 |
| Legacy p btts yes | 0.4588 |
| Legacy p over 2 5 | 0.6294 |
| Legacy goal margin distribution | {"-1": 0.19877248115690652, "-10": 0.0001837538572697819, "-11": 4.3467869769407304e-05, "-12": 9.44423650757577e-06, "-13": 1.8970471064512013e-06, "-14": 3.542798883723271e-07, "-15": 6.181489325057144e-08, "-16": 1.0119853168852417e-08, "-17": 1.560203598660585e-09, "-18": 2.2651182051917892e-10, "-19": 2.878500623134049e-11, "-2": 0.2105516526942178, "-3": 0.1631171786838452, "-4": 0.0992989893789878, "-5": 0.04958214296877344, "-6": 0.02094020735181179, "-7": 0.007653019055770102, "-8": 0.0024632277961516647, "-9": 0.0007079742442743667, "0": 0.15347421702376687, "1": 0.06975657732914879, "10": 2.6183362836383975e-10, "11": 1.554207843660192e-11, "12": 8.473432477419469e-13, "13": 4.2709296054263914e-14, "14": 2.0014400074870556e-15, "15": 8.762761283036594e-17, "16": 3.59976249538423e-18, "17": 1.3926202033627828e-19, "18": 5.073341142403452e-21, "19": 1.6177868571432524e-22, "2": 0.019086811235039105, "3": 0.0037104467597900374, "4": 0.0005667912161934711, "5": 7.101586078421298e-05, "6": 7.525975834470084e-06, "7": 6.90186429493325e-07, "8": 5.574295370700778e-08, "9": 4.020264608848251e-09} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0681 |
| Legacy raw p draw | 0.1396 |
| Legacy raw p away | 0.7923 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.6615 |
| Legacy lambda away | 2.6361 |
| Legacy model home team | Venezia |
| Legacy model away team | Inter |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 29.8% |
| Market home draw odds | 3.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-28T16:07:34Z |
| Market reference home draw last update utc | 2026-10-28T16:07:34Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 87.3% |
| Market draw away odds | 1.12 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-28T16:07:34Z |
| Market reference draw away last update utc | 2026-10-28T16:07:34Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.9% |
| Market home away odds | 1.18 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-28T16:07:34Z |
| Market reference home away last update utc | 2026-10-28T16:07:34Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.28 |
| Market reference dc draw away odds | 1.12 |
| Market reference dc home away odds | 1.18 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:34Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.23, "price": 1.66, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:34Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.66, "price": 2.23, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:34Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.05, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:34Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.05, "price": 1.78, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 87.6% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-28T16:07:32Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 54.6% |
| Market under 3 5 odds | 1.78 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-28T16:07:31Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.12 |
| Market reference under 3 5 last update utc | 2026-10-28T16:07:31Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.2% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-28T16:07:34Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.29 |
| Market reference btts yes last update utc | 2026-10-28T16:07:34Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021258779398154137, "mu": 8.629755869754138, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,360.2604 |
| Elo away rating | 1,685.6828 |
| Elo rating diff | -265.4224 |
| Elo home expectancy | 0.1783 |

</details>


---

## 2026-10-29 — Fiorentina vs Atalanta BC

The model's most likely 1X2 outcome is **Fiorentina win** at **38.1%**. Expected goals are 1.24 for Fiorentina and 1.62 for Atalanta BC (2.85 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 59.5%; Under 3.5 goals: 62.4%; Double Chance 1X: 64.3%; Double Chance X2: 61.9%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 79.9%; BTTS Yes (both teams score): 62.8%; BTTS No (at least one team does not score): 37.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 38.1% | 2.62 |
| Draw | 26.2% | 3.82 |
| Atalanta BC win | 35.7% | 2.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.24 |
| Atalanta BC expected goals | 1.62 |
| Expected total goals | 2.85 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 59.5% |
| Under 2.5 | 40.5% |
| Over 3.5 | 37.6% |
| Under 3.5 | 62.4% |
| Over 4.5 | 20.1% |
| Under 4.5 | 79.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.90% |
| 2 | 2-1 | 9.29% |
| 3 | 1-0 | 7.41% |
| 4 | 1-2 | 7.08% |
| 5 | 2-2 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 38.1% | 42.0% | 2.32 | -11.6% |
| Draw | 26.2% | 26.7% | 3.60 | -5.7% |
| Atalanta BC win | 35.7% | 31.3% | 3.08 | +10.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T19:45:00+00:00 |
| Fixture id | da159a6b84dbb548b4d7b94c722caac5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:07:31Z |
| Market best draw last update utc | 2026-10-28T16:07:31Z |
| Market best away last update utc | 2026-10-28T16:07:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Fiorentina |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2377 |
| Dc lambda away | 1.6150 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:07:21.315970+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.8% |
| P btts no | 37.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.62 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.50 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.66 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.98 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.1625498178273983, "-10": 3.4751706491334737e-06, "-11": 5.501031964281771e-07, "-12": 8.003693500966664e-08, "-13": 1.0771807759066935e-08, "-14": 1.3478555080480812e-09, "-15": 1.5627123536256918e-10, "-16": 1.504765019862832e-11, "-2": 0.10871563679216803, "-3": 0.05441400674775289, "-4": 0.021686310949101638, "-5": 0.007144421523922139, "-6": 0.002000515073693525, "-7": 0.000486317951211926, "-8": 0.00010435116863043881, "-9": 2.0027247232414862e-05, "0": 0.2618964349938575, "1": 0.21270575753681678, "10": 4.162592936342338e-07, "11": 5.049968709874989e-08, "12": 5.631079765055949e-09, "13": 5.808266510486278e-10, "14": 5.5700358531772985e-11, "15": 4.949375562654423e-12, "16": 3.6525549866155707e-13, "2": 0.10940221883444765, "3": 0.04196638240647336, "4": 0.012818382287362177, "5": 0.00323646802370297, "6": 0.0006945488392453111, "7": 0.0001294011017121055, "8": 2.1280003822655174e-05, "9": 3.1300577835331308e-06} |
| Raw goal margin distribution | {"-1": 0.22039007178831452, "-10": 2.2981636621664123e-06, "-11": 3.3244206376542397e-07, "-12": 4.418073112685442e-08, "-13": 5.427702068513234e-09, "-14": 6.157848295399725e-10, "-15": 5.850335729360361e-11, "-2": 0.13969715437394326, "-3": 0.06526575911114793, "-4": 0.024087803700434958, "-5": 0.007314446413088378, "-6": 0.0018822378067022527, "-7": 0.0004196764947200566, "-8": 8.248147104844454e-05, "-9": 1.4484842142777795e-05, "0": 0.2504129256718825, "1": 0.16829338541135866, "10": 1.6067491077052188e-07, "11": 1.781311185714193e-08, "12": 1.814318108727863e-09, "13": 1.7082571571250899e-10, "14": 1.485329973181425e-11, "15": 1.0815122932517788e-12, "2": 0.08205423151785111, "3": 0.02938025277002874, "4": 0.008310440585199419, "5": 0.0019340380742241365, "6": 0.00038142992348703513, "7": 6.51795902055467e-05, "8": 9.817707503038666e-06, "9": 1.3213691683371203e-06} |
| Unadjusted home-win probability | 29.0% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 45.9% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.0% |
| Raw p btts yes | 57.1% |
| P home draw | 64.3% |
| P draw away | 61.9% |
| P home away | 73.8% |
| Raw p home draw | 54.1% |
| Raw p draw away | 71.0% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0975 |
| Totals anchor target over 2 5 | 0.5945 |
| Totals anchor reference over odds | 1.64 |
| Totals anchor reference under odds | 2.36 |
| Totals anchor reference last update utc | 2026-10-28T16:07:31Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5365 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.81, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.32 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.08 |
| Market reference 1x2 last update utc | 2026-10-28T16:07:31Z |
| Market reference home last update utc | 2026-10-28T16:07:31Z |
| Market reference draw last update utc | 2026-10-28T16:07:31Z |
| Market reference away last update utc | 2026-10-28T16:07:31Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.32 |
| Market reference over 2 5 last update utc | 2026-10-28T16:07:32Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:07:32Z |
| Home probability edge | -3.9% |
| Draw probability edge | -0.5% |
| Away probability edge | +4.4% |
| Over 2.5 probability edge | +1.7% |
| Under 2.5 probability edge | -1.7% |
| Raw edge prob home | -0.1294 |
| Raw ev home | -0.3262 |
| Raw edge prob draw | -0.0164 |
| Raw ev draw | -0.0985 |
| Raw edge prob away | 0.1458 |
| Raw ev away | 0.4142 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06183945552585709, 0.07392524832854341, 0.061491404845730895, 0.03275012478816199, 0.01308195848262499, 0.004180445451077713, 0.0011132459124684013, 0.00025410479941792075, 5.075077511494803e-05, 9.009899959624943e-06, 1.439593137025514e-06, 2.091061861707584e-07, 2.7842320842440545e-08, 3.4220147737704967e-09, 3.90547303140802e-10, 4.1600847941691976e-11], [0.08197509655191239, 0.12210206216361454, 0.07836005879360851, 0.04173431572000517, 0.016670671915950033, 0.0053272478023839685, 0.0014186375375813936, 0.00032381219899074644, 6.467300156510617e-05, 1.1481544328544597e-05, 1.8345100935521448e-06, 2.6646932337219904e-07, 3.54801765163383e-08, 4.36076032964255e-09, 4.976843464964869e-10, 5.301301700218463e-11], [0.054957781715853984, 0.0878110142607879, 0.06028156125943891, 0.026591549190778236, 0.010621930290420866, 0.0033943235810777786, 0.0009039029205023581, 0.00020632105425677359, 4.120722414551153e-05, 7.31561175812557e-06, 1.1688814001636398e-06, 1.6978431293384456e-07, 2.260664498398509e-08, 2.778513815653615e-09, 3.1710590081624114e-10, 3.377791692627233e-11], [0.023344698971749088, 0.03729993515605646, 0.029798738555800185, 0.01363773097507366, 0.00451193183907651, 0.001441824246521788, 0.00038395548219016215, 8.76400530148917e-05, 1.7503804067492992e-05, 3.1074899487503033e-06, 4.965117508122614e-07, 7.212015390392755e-08, 9.60274060261227e-09, 1.1802435722504425e-09, 1.3469870081355486e-10, 1.4348019114263162e-11], [0.007437185686904791, 0.011883063654014446, 0.0094933223231197, 0.005056112988740721, 0.0017354906296847257, 0.00045933831326079014, 0.00012232105541429267, 2.7920486302723754e-05, 5.576385509818856e-06, 9.8998833940906e-07, 1.5817938329338497e-07, 2.297613590994502e-08, 3.0592540538318433e-09, 3.7600358921846953e-10, 4.291249379345427e-11, 4.571011282740018e-12], [0.0018954789182225131, 0.0030285779578880794, 0.0024195163446098485, 0.0012886266367106972, 0.0005147388069540273, 0.00014134563498768678, 3.1175365461261445e-05, 7.115956949484032e-06, 1.421225933938209e-06, 2.523134564113525e-07, 4.0314401031827824e-08, 5.855814695631324e-09, 7.796970263543797e-10, 9.583018450037132e-11, 1.0936896124170725e-11, 1.1649911520491888e-12], [0.00040257615365538185, 0.0006432323006131828, 0.0005138751870861051, 0.00027368827472443793, 0.00010932412228305585, 3.4935405910228766e-05, 7.994292550614715e-06, 1.5113407755476142e-06, 3.018507167025934e-07, 5.358824085093467e-08, 8.562277505852263e-09, 1.2437022295645386e-09, 1.655979535666022e-10, 2.035313962574826e-11, 2.32286074630994e-12, 2.4742963507835664e-13], [7.328757374066593e-05, 0.00011709817940165671, 9.354917156695318e-05, 4.982398841485561e-05, 1.9902072193554835e-05, 6.359867849991216e-06, 1.6936225985239638e-06, 3.32188117801276e-07, 5.495086198759611e-08, 9.755550887292199e-09, 1.5587325240216795e-09, 2.2641161934958347e-10, 3.0146525379406283e-11, 3.705217528738626e-12, 4.2286863414224036e-13, 4.504369536491224e-14], [1.1674027048103366e-05, 1.8652647970798817e-05, 1.4901510630775463e-05, 7.936496717132666e-06, 3.170214502161167e-06, 1.013067639077307e-06, 2.6977828593985886e-07, 6.157844953057854e-08, 1.0568278674627646e-08, 1.5539682802216217e-09, 2.4829155499918686e-10, 3.606525954379213e-11, 4.802060359248096e-12, 5.902065990431354e-13, 6.73590299255851e-14, 7.1750406132593e-15], [1.6529454593289064e-06, 2.641060333400681e-06, 2.109930380732114e-06, 1.1237421463482507e-06, 4.48876094329189e-07, 1.4344197997022343e-07, 3.819836898889774e-08, 8.718998005116047e-09, 1.7413913786711338e-09, 2.6565584423603076e-10, 3.5156025999811045e-11, 5.106541792030107e-12, 6.799319406692704e-13, 8.356836196578845e-14, 9.537480271504503e-15, 1.0159262740541867e-15], [2.1063903760304718e-07, 3.365570253630532e-07, 2.688737866688492e-07, 1.4320131549705192e-07, 5.720142063907087e-08, 1.827917578422126e-08, 4.867715166533198e-09, 1.1110840580343005e-09, 2.2190992571675863e-10, 3.939617131417768e-11, 5.409031508074599e-12, 6.507395888244665e-13, 8.664545391370295e-14, 1.0649328590480817e-14, 1.2153853318084645e-15, 1.2946206508792166e-16], [2.440206135270335e-08, 3.8989378583610446e-08, 3.1148426773537525e-08, 1.6589552090207326e-08, 6.626656633927797e-09, 2.1176016280705034e-09, 5.639139140251626e-10, 1.2871660287044243e-10, 2.5707768530157072e-11, 4.5639583261002735e-12, 7.292248652445534e-13, 9.101946483634715e-14, 1.0037682028910026e-14, 1.2337008969806056e-15, 1.4079967213796666e-16, 1.4997890662017715e-17], [2.591347206817301e-09, 4.140429606656495e-09, 3.3077692720175716e-09, 1.7617072939022978e-09, 7.037097362663486e-10, 2.2487612766551576e-10, 5.988415178837457e-11, 1.3668902987262627e-11, 2.73000519141585e-12, 4.846639998739405e-13, 7.743914706139574e-14, 1.1248320296790889e-14, 1.286980368664263e-15, 1.3101136527896326e-16, 1.49520498224258e-17, 1.5926827456675212e-18], [2.540168887646696e-10, 4.058657381245936e-10, 3.2424418349606316e-10, 1.726914110674933e-10, 6.898116830099752e-11, 2.2043489254069798e-11, 5.870145800445261e-12, 1.3398946310691543e-12, 2.67608841922256e-13, 4.750920332880675e-14, 7.59097474602226e-15, 1.1026169392130991e-15, 1.4681256040321732e-16, 1.550548497309138e-17, 1.4656751386132217e-18, 1.5612277458585997e-19], [2.3121440872341586e-11, 3.694321551529169e-11, 2.9513756952792163e-11, 1.5718932192171775e-11, 6.278889612155558e-12, 2.006469868545848e-12, 5.343197048711239e-13, 1.2196155396633748e-13, 2.4358624521039512e-14, 4.324441736930067e-15, 6.90955135334307e-16, 1.003637690739397e-16, 1.3363355291800579e-17, 1.6424492589705118e-18, 1.6107547466508176e-19, 1.4210801175338812e-20], [1.964282618787725e-12, 3.138511847919596e-12, 2.5073419999029602e-12, 1.3354022987348057e-12, 5.334232325113269e-13, 1.7045970057257745e-13, 4.539314461191896e-14, 1.0361247032099694e-14, 2.069387588274845e-15, 3.673830617525728e-16, 5.87001117358067e-17, 8.526406647251455e-18, 1.1352842010710934e-18, 1.3953432009057244e-19, 1.5924756615505277e-20, 1.4576291285559288e-21]] |
| Legacy trial inputs | {"lambda_home": 1.2743253953979023, "lambda_away": 1.5977903677916558, "rho": -0.03104744974939825, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3606 |
| Legacy p draw | 0.2597 |
| Legacy p away | 0.3796 |
| Legacy p over 1 5 | 0.7823 |
| Legacy p under 3 5 | 0.6786 |
| Legacy p btts yes | 0.5812 |
| Legacy p over 2 5 | 0.5437 |
| Legacy goal margin distribution | {"-1": 0.18388086971215148, "-10": 1.7298934264388942e-06, "-11": 2.4750414621484664e-07, "-12": 3.2534535092013606e-08, "-13": 3.953477037193256e-09, "-14": 4.4356032014298664e-10, "-15": 4.1600847941691976e-11, "-2": 0.11541922397479606, "-3": 0.05322847266334599, "-4": 0.019406586751068423, "-5": 0.005823939424172443, "-6": 0.0014815370301229445, "-7": 0.00032661370110808436, "-8": 6.347647844970297e-05, "-9": 1.102418429462852e-05, "0": 0.2597459835087609, "1": 0.20519239355268168, "10": 2.5311532621905544e-07, "11": 2.888298749828059e-08, "12": 3.028062104193421e-09, "13": 2.9346744627986426e-10, "14": 2.6259952720261182e-11, "15": 1.964282618787725e-12, "2": 0.10315562854571027, "3": 0.03794192172058362, "4": 0.011032781475985944, "5": 0.0026406646202447037, "6": 0.0005357589661052019, "7": 9.420021093463224e-05, "8": 1.4601277018169576e-05, "9": 2.022483651790714e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3014 |
| Legacy raw p draw | 0.2527 |
| Legacy raw p away | 0.4459 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2743 |
| Legacy lambda away | 1.5978 |
| Legacy model home team | Fiorentina |
| Legacy model away team | Atalanta |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 95/100 |
| Market p home draw | 68.8% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-28T16:07:13Z |
| Market reference home draw last update utc | 2026-10-28T16:07:32Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.1% |
| Market draw away odds | 1.66 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-28T16:07:13Z |
| Market reference draw away last update utc | 2026-10-28T16:07:32Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-28T16:07:13Z |
| Market reference home away last update utc | 2026-10-28T16:07:32Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.41 |
| Market reference dc draw away odds | 1.70 |
| Market reference dc home away odds | 1.31 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:13Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.21, "price": 1.66, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:13Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.66, "price": 2.21, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:13Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.07, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:13Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.75, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 82.7% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-28T16:07:32Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-28T16:07:31Z |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.53 |
| Market reference under 3 5 last update utc | 2026-10-28T16:07:31Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.0% |
| Market btts yes odds | 1.52 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-28T16:07:13Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.37 |
| Market reference btts yes last update utc | 2026-10-28T16:07:32Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021258779398154137, "mu": 9.546586050831579, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,434.0364 |
| Elo away rating | 1,539.1317 |
| Elo rating diff | -45.0953 |
| Elo home expectancy | 0.4355 |

</details>


---

## 2026-10-29 — Frosinone vs Lecce

The model's most likely 1X2 outcome is **Frosinone win** at **58.0%**. Expected goals are 1.84 for Frosinone and 1.01 for Lecce (2.84 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 68.8%; Under 3.5 goals: 51.7%; Double Chance 1X: 80.5%; Double Chance X2: 42.0%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 71.2%; BTTS Yes (both teams score): 66.0%; BTTS No (at least one team does not score): 34.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 58.0% | 1.72 |
| Draw | 22.4% | 4.46 |
| Lecce win | 19.5% | 5.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.84 |
| Lecce expected goals | 1.01 |
| Expected total goals | 2.84 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 87.5% |
| Under 1.5 | 12.5% |
| Over 2.5 | 68.8% |
| Under 2.5 | 31.2% |
| Over 3.5 | 48.3% |
| Under 3.5 | 51.7% |
| Over 4.5 | 28.8% |
| Under 4.5 | 71.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.48% |
| 2 | 2-1 | 8.99% |
| 3 | 2-0 | 7.05% |
| 4 | 3-1 | 6.98% |
| 5 | 2-2 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 58.0% | 58.7% | 1.67 | -3.1% |
| Draw | 22.4% | 22.1% | 4.27 | -4.2% |
| Lecce win | 19.5% | 19.2% | 4.88 | -4.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T17:30:00+00:00 |
| Fixture id | 667cf69986b200753742c90cb9c5126c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:07:31Z |
| Market best draw last update utc | 2026-10-28T16:07:31Z |
| Market best away last update utc | 2026-10-28T16:07:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Frosinone |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8358 |
| Dc lambda away | 1.0055 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:07:21.315970+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 66.0% |
| P btts no | 34.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.00 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.02 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.07 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.48 |
| Fair Under 4.5 odds | 1.40 |
| Goal margin distribution | {"-1": 0.11625138817138407, "-10": 1.1041981585601497e-07, "-11": 1.2523685298126412e-08, "-12": 1.306332125070328e-09, "-13": 1.261074427575971e-10, "-14": 1.1327921696402514e-11, "-15": 9.513176281233533e-13, "-16": 7.495935677978944e-14, "-17": 5.508639544528729e-15, "-18": 3.3499128226091767e-16, "-2": 0.05353337986396013, "-3": 0.018684702893635406, "-4": 0.00524408755233687, "-5": 0.0012239163221462658, "-6": 0.00024372124605282966, "-7": 4.224386708109623e-05, "-8": 6.474753046602034e-06, "-9": 8.888011512699197e-07, "0": 0.22433784367554835, "1": 0.20610812703898773, "10": 4.3823522409163614e-05, "11": 9.074886436705947e-06, "12": 1.7282694366409065e-06, "13": 3.0461224079087196e-07, "14": 4.995807093694336e-08, "15": 7.660017398295767e-09, "16": 1.1019930424373664e-09, "17": 1.4785844904815362e-10, "18": 1.6416632860857243e-11, "2": 0.17206582057993763, "3": 0.10964906492404287, "4": 0.05618720894132166, "5": 0.023942419824073014, "6": 0.008704793934666076, "7": 0.0027547206332082744, "8": 0.0007708784281767448, "9": 0.00019320398606254133} |
| Raw goal margin distribution | {"-1": 0.12983747122159353, "-10": 2.0065193103683348e-08, "-11": 1.809122865058869e-09, "-12": 1.4983310012807834e-10, "-13": 1.1473490158012106e-11, "-14": 8.167264313349849e-13, "-15": 5.403107496091526e-14, "-16": 3.0442788762697983e-15, "-2": 0.0523898862217144, "-3": 0.015382680114568422, "-4": 0.0035568141333855133, "-5": 0.0006754099622368945, "-6": 0.00010856396318378365, "-7": 1.5108528506192164e-05, "-8": 1.8523891985006562e-06, "-9": 2.0285877761271006e-07, "0": 0.23213301983433235, "1": 0.23908236466679464, "10": 8.259071770775443e-06, "11": 1.3595799418046864e-06, "12": 2.0558586007698748e-07, "13": 2.8742848967119547e-08, "14": 3.735593970314791e-09, "15": 4.5120660941791655e-10, "16": 4.641571753321505e-11, "2": 0.17464052752897527, "3": 0.09362209988359381, "4": 0.03952358492080862, "5": 0.01370286598704274, "6": 0.004021410679811738, "7": 0.0010217948180153236, "8": 0.00022872969827010935, "9": 4.573333905629206e-05} |
| Unadjusted home-win probability | 56.6% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 20.2% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 53.5% |
| P home draw | 80.5% |
| P draw away | 42.0% |
| P home away | 77.6% |
| Raw p home draw | 79.8% |
| Raw p draw away | 43.4% |
| Raw p home away | 76.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2682 |
| Totals anchor target over 2 5 | 0.6880 |
| Totals anchor reference over odds | 1.42 |
| Totals anchor reference under odds | 2.98 |
| Totals anchor reference last update utc | 2026-10-28T16:07:31Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5437 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 8.7, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 9.0, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.83, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.16, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.76, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.53, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:20Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 9.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.31, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:36Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.75, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:36Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.3, "price": 3.75, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.67 |
| Reference draw odds | 4.27 |
| Reference away odds | 4.88 |
| Market reference 1x2 last update utc | 2026-10-28T16:07:31Z |
| Market reference home last update utc | 2026-10-28T16:07:31Z |
| Market reference draw last update utc | 2026-10-28T16:07:31Z |
| Market reference away last update utc | 2026-10-28T16:07:31Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.86 |
| Market reference over 2 5 last update utc | 2026-10-28T16:07:10Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:07:10Z |
| Home probability edge | -0.6% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | -0.0208 |
| Raw ev home | -0.0549 |
| Raw edge prob draw | 0.0111 |
| Raw ev draw | -0.0088 |
| Raw edge prob away | 0.0096 |
| Raw ev away | -0.0144 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.0665605724566749, 0.059668211684117144, 0.03170477451659844, 0.010638101581624147, 0.002677101642885993, 0.0005389588096223985, 9.042011262487673e-05, 1.3002525750116684e-05, 1.6360570906482344e-06, 1.829854944459612e-07, 1.841948073335835e-08, 1.6855646574302365e-09, 1.4139201682975913e-10, 1.0948188239778937e-11, 7.871816091151661e-13, 5.282559518957868e-14], [0.11549968057499355, 0.1115189737742111, 0.05390140955413883, 0.018085877568044452, 0.0045513508382061035, 0.0009162859529267155, 0.00015372358254663718, 2.210564422492128e-05, 2.7814669759223584e-06, 3.110943455357069e-07, 3.1315030304458954e-08, 2.865634981335818e-09, 2.403811136659113e-10, 1.8613057092684355e-11, 1.3382904926256156e-12, 8.980899831865818e-14], [0.10134812238352506, 0.10201791094193424, 0.0462749856795011, 0.015373935137605377, 0.0038688845654190882, 0.0007788906429779294, 0.000130673028074018, 1.87909455435768e-05, 2.3643913719053993e-06, 2.6444634892322176e-07, 2.6619401957223027e-08, 2.435938547375307e-09, 2.0433642967564636e-10, 1.582206511013199e-11, 1.1376164165378027e-12, 7.634231237769305e-14], [0.05743411137521699, 0.05781368141318914, 0.029097879975104803, 0.008799134496544169, 0.0021925018619216104, 0.00044139832969595095, 7.405257316696004e-05, 1.0648853020792291e-05, 1.3399036330908058e-06, 1.4986208623924918e-07, 1.508524934450434e-08, 1.3804495095005384e-09, 1.1579771764881785e-10, 8.96638465863652e-12, 6.446886872008655e-13, 4.326328666602699e-14], [0.024410988619339158, 0.024572315741067347, 0.012367354520012306, 0.004149695927058904, 0.0009411441472675879, 0.00018760575109119922, 3.1474266381554365e-05, 4.5260390328202215e-06, 5.694938348520286e-07, 6.369527784206818e-08, 6.4116226620594705e-09, 5.867268851056138e-10, 4.921703670495871e-11, 3.810946293373663e-12, 2.740094314938388e-13, 1.8388020170454008e-14], [0.008300243198408913, 0.00835509777090183, 0.004205157432899693, 0.001410982813156064, 0.00035507692591588337, 6.442468586219513e-05, 1.0701904356771571e-05, 1.538947286556734e-06, 1.936397334404364e-07, 2.1657717551863115e-08, 2.1800848880558065e-09, 1.9949932849353631e-10, 1.6734814821573356e-11, 1.2958009011571414e-12, 9.316889846299878e-14, 6.252308816001923e-15], [0.0023518792508794356, 0.002367422329290281, 0.0011915340643288688, 0.0003998028879738565, 0.0001006112754247613, 2.0255238863125173e-05, 3.0625696986988984e-06, 4.360617038478829e-07, 5.4867943063606474e-08, 6.136728203505929e-09, 6.177284557586371e-10, 5.652826309213085e-11, 4.741820547344042e-12, 3.671660190976752e-13, 2.63994673269843e-14, 1.7715957259257482e-15], [0.0005712055705731815, 0.0005749805488033822, 0.0002893902375378554, 9.710091904442734e-05, 2.4435659680915466e-05, 4.919429969706641e-06, 8.253235756972073e-07, 1.0696115247583649e-07, 1.3325885974845398e-08, 1.4904393300061614e-09, 1.500289332026556e-10, 1.372913118774173e-11, 1.1516553455235775e-12, 8.917433807681588e-14, 6.411690902795907e-15, 4.302709618591308e-16], [0.00012138859946374835, 0.00012219083134658936, 6.149918250613616e-05, 2.0635205916528655e-05, 5.192894919884343e-06, 1.0454427354121399e-06, 1.7539197465767958e-07, 2.5221586222873846e-08, 2.860106942255673e-09, 3.167377073609194e-10, 3.188309606686051e-11, 2.917618616817254e-12, 2.447417123711956e-13, 1.895070455351003e-14, 1.3625675570773108e-15, 9.143816541843088e-17], [2.2930358508598187e-05, 2.3081900455385916e-05, 1.1617221955613347e-05, 3.897999249147424e-06, 9.809400778693961e-07, 1.9748458116422263e-07, 3.313161924759364e-08, 4.764368456353548e-09, 5.99481896462159e-10, 6.042733284723799e-11, 6.022730523351348e-12, 5.511394082354471e-13, 4.6231814449393286e-14, 3.579796219102788e-15, 2.573895960081354e-16, 1.7272708670135775e-17], [3.8983991024699095e-06, 3.924162807347105e-06, 1.975048389582525e-06, 6.627003571970615e-07, 1.66770001337262e-07, 3.357442988401478e-08, 5.6327193789736294e-09, 8.099921205819857e-10, 1.0191814865165448e-10, 1.1399078266058975e-11, 1.0341168107659532e-12, 9.369942356528005e-14, 7.85988862265234e-15, 6.086025372146974e-16, 4.375890458437276e-17, 2.9365398692581547e-18], [6.025166694679845e-07, 6.064985762065555e-07, 3.0525339926725854e-07, 1.0242358506101654e-07, 2.5775120281870634e-08, 5.189092532928803e-09, 8.705643601540823e-10, 1.2518824829380978e-10, 1.575194890770212e-11, 1.761783360641371e-12, 1.7734266186475483e-13, 1.4625825927632823e-14, 1.2147842719103298e-15, 9.406250209734524e-17, 6.763152965287524e-18, 4.538566153127804e-19], [8.536174298497522e-08, 8.592588090319774e-08, 4.3246873545506634e-08, 1.4510894364629384e-08, 3.6516984581532385e-09, 7.351663540068402e-10, 1.2333748579764543e-10, 1.773608535184815e-11, 2.2316624291225147e-12, 2.496012244093866e-13, 2.5125078673321187e-14, 2.2991931879060555e-15, 1.7381773269420754e-16, 1.3326335245873105e-17, 9.581718721586724e-19, 6.43002819865035e-20], [1.1163371445665827e-08, 1.123714783433225e-08, 5.655705897865809e-09, 1.8976944253550363e-09, 4.77558972795401e-10, 9.61430120467285e-11, 1.6129733519804014e-11, 2.319475936773727e-12, 2.9185060855676894e-13, 3.2642154247780716e-14, 3.2857879422779527e-15, 3.0068209345792677e-16, 2.5222436547421502e-17, 1.7601251497560335e-18, 1.2530705376504557e-19, 8.409012126225416e-21], [1.3556350636958723e-09, 1.3645941724952024e-09, 6.868062450860373e-10, 2.304484013375976e-10, 5.799284666420193e-11, 1.1675221853383928e-11, 1.958730159069143e-12, 2.8166785675756515e-13, 3.544116759405535e-14, 3.963932318138627e-15, 3.990129118341298e-16, 3.651362770655644e-17, 3.0629115533734235e-18, 2.371656688970017e-19, 1.5368222852168155e-20, 1.0211567128119545e-21], [1.5364802702080417e-10, 1.546634547179374e-10, 7.784279658224499e-11, 2.6119081118400357e-11, 6.572924166613074e-12, 1.3232726497291757e-12, 2.2200298034975953e-13, 3.1924307378115615e-14, 4.016911056648443e-15, 4.492731091401152e-16, 4.522422612173896e-17, 4.1384639618197344e-18, 3.471511837647712e-19, 2.6880417952414878e-20, 1.9327189297484528e-21, 1.1688998525956909e-22]] |
| Legacy trial inputs | {"lambda_home": 1.7001038605690055, "lambda_away": 1.0066087909934291, "rho": -0.03104744974939825, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5597 |
| Legacy p draw | 0.2342 |
| Legacy p away | 0.2061 |
| Legacy p over 1 5 | 0.7583 |
| Legacy p under 3 5 | 0.7103 |
| Legacy p btts yes | 0.5180 |
| Legacy p over 2 5 | 0.5137 |
| Legacy goal margin distribution | {"-1": 0.13133481560367613, "-10": 2.1498698790768763e-08, "-11": 1.942430912913651e-09, "-12": 1.611859536256473e-10, "-13": 1.2362821044782246e-11, "-14": 8.769906074338243e-13, "-15": 5.282559518957868e-14, "-2": 0.05413400458425063, "-3": 0.016047121604462998, "-4": 0.0037353012601658753, "-5": 0.0007128791744075627, "-6": 0.00011504662626230795, "-7": 1.6064128159675845e-05, "-8": 1.9752018273180093e-06, "-9": 2.1685616690223187e-07, "0": 0.2341624076924954, "1": 0.2511413507400931, "10": 4.5501015627666404e-06, "11": 6.943352775945523e-07, "12": 9.731181614551191e-08, "13": 1.2605808414743276e-08, "14": 1.5102985184138097e-09, "15": 1.5364802702080417e-10, "2": 0.17304585209532547, "3": 0.08663690249719048, "4": 0.03406011751328767, "5": 0.010978706374257635, "6": 0.002992429066224824, "7": 0.0007057028509346354, "8": 0.00014655172172590246, "9": 2.717477506577481e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5328 |
| Legacy raw p draw | 0.2473 |
| Legacy raw p away | 0.2199 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7001 |
| Legacy lambda away | 1.0066 |
| Legacy model home team | Frosinone |
| Legacy model away team | Lecce |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 80.2% |
| Market home draw odds | 1.21 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-28T16:07:36Z |
| Market reference home draw last update utc | 2026-10-28T16:07:36Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.8% |
| Market draw away odds | 2.27 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-28T16:07:36Z |
| Market reference draw away last update utc | 2026-10-28T16:07:36Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.0% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-28T16:07:36Z |
| Market reference home away last update utc | 2026-10-28T16:07:36Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.21 |
| Market reference dc draw away odds | 2.27 |
| Market reference dc home away odds | 1.26 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:36Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.18, "price": 1.68, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:36Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.18, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:36Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.74, "price": 2.08, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-28T16:07:36Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.08, "price": 1.74, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 87.5% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-28T16:07:32Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 53.9% |
| Market under 3 5 odds | 1.80 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-28T16:07:31Z |
| Market reference under 3 5 odds | 1.80 |
| Market reference under 3 5 opposite odds | 2.09 |
| Market reference under 3 5 last update utc | 2026-10-28T16:07:31Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.8% |
| Market btts yes odds | 1.46 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-28T16:07:36Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 2.82 |
| Market reference btts yes last update utc | 2026-10-28T16:07:36Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021258779398154137, "mu": 9.590156216022761, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,461.3882 |
| Elo away rating | 1,418.2291 |
| Elo rating diff | 103.1592 |
| Elo home expectancy | 0.6442 |

</details>


---

## 2026-10-31 — Bologna vs Monza

The model's most likely 1X2 outcome is **Bologna win** at **56.1%**. Expected goals are 1.89 for Bologna and 0.97 for Monza (2.86 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 51.7%; Under 3.5 goals: 70.4%; Double Chance 1X: 80.0%; Double Chance X2: 43.9%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 85.6%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 56.1% | 1.78 |
| Draw | 23.9% | 4.19 |
| Monza win | 20.0% | 4.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.89 |
| Monza expected goals | 0.97 |
| Expected total goals | 2.86 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 76.2% |
| Under 1.5 | 23.8% |
| Over 2.5 | 51.7% |
| Under 2.5 | 48.3% |
| Over 3.5 | 29.6% |
| Under 3.5 | 70.4% |
| Over 4.5 | 14.4% |
| Under 4.5 | 85.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.36% |
| 2 | 1-0 | 10.98% |
| 3 | 2-0 | 10.19% |
| 4 | 2-1 | 9.55% |
| 5 | 0-0 | 6.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 56.1% | 55.1% | 1.76 | -1.3% |
| Draw | 23.9% | 24.4% | 3.81 | -9.1% |
| Monza win | 20.0% | 20.6% | 4.47 | -10.4% |
| Over 2.5 | 51.7% | 51.7% | 1.86 | -3.9% |
| Under 2.5 | 48.3% | 48.3% | 1.98 | -4.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:00:00+00:00 |
| Fixture id | 04aa939b89001eedf55668e66c74836e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:07:31Z |
| Market best draw last update utc | 2026-10-28T16:07:31Z |
| Market best away last update utc | 2026-10-28T16:07:31Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Bologna |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8854 |
| Dc lambda away | 0.9718 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:07:21.315970+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.77 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.20 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.38 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.95 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.1323377235661883, "-10": 1.1329019518051456e-08, "-11": 9.528141684082374e-10, "-12": 7.359890588708847e-11, "-13": 5.255689668049478e-12, "-14": 3.4886505623227553e-13, "-15": 2.1535559748394502e-14, "-16": 1.139782424385882e-15, "-2": 0.05054442421767493, "-3": 0.013953425314435152, "-4": 0.003024219750123286, "-5": 0.0005373581087074889, "-6": 8.073368529154985e-05, "-7": 1.049429308188855e-05, "-8": 1.201186120773976e-06, "-9": 1.2276216669811605e-07, "0": 0.2385368002842609, "1": 0.23657119636887275, "10": 7.81199312573914e-06, "11": 1.274691188892435e-06, "12": 1.9102727714672922e-07, "13": 2.6465554073422696e-08, "14": 3.408285742624378e-09, "15": 4.0818960541970086e-10, "16": 4.191360174663728e-11, "2": 0.17363000670120501, "3": 0.09299500250427549, "4": 0.03910383695865447, "5": 0.013480223251618295, "6": 0.003929301059353454, "7": 0.0009909254137930906, "8": 0.00022005200659819984, "9": 4.363217098362348e-05} |
| Raw goal margin distribution | {"-1": 0.1227691198469694, "-10": 1.4026525396385318e-08, "-11": 1.2223947238953477e-09, "-12": 9.785461895814575e-11, "-13": 7.242595250941935e-12, "-14": 4.983084123860379e-13, "-15": 3.18651799860444e-14, "-16": 1.7365364943352467e-15, "-2": 0.047973790729978094, "-3": 0.013625465579922455, "-4": 0.0030466209754502313, "-5": 0.0005593588421938847, "-6": 8.692198129842971e-05, "-7": 1.1693844649432465e-05, "-8": 1.3859197539681725e-06, "-9": 1.4670860279981383e-07, "0": 0.22667329128274769, "1": 0.24044112380649274, "10": 1.0597967934498542e-05, "11": 1.7918894619138987e-06, "12": 2.7829687437890466e-07, "13": 3.996211488019239e-08, "14": 5.334328011453084e-09, "15": 6.617975027542981e-10, "16": 6.997129516385221e-11, "2": 0.1805753794317062, "3": 0.09950229564922615, "4": 0.04316457083795977, "5": 0.015375411826561061, "6": 0.004635462972464182, "7": 0.001209896078681429, "8": 0.00027819933272369476, "9": 5.7134815586634e-05} |
| Unadjusted home-win probability | 58.5% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 18.8% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 53.0% |
| P home draw | 80.0% |
| P draw away | 43.9% |
| P home away | 76.1% |
| Raw p home draw | 81.2% |
| Raw p draw away | 41.5% |
| Raw p home away | 77.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9642 |
| Totals anchor target over 2 5 | 0.5166 |
| Totals anchor reference over odds | 1.86 |
| Totals anchor reference under odds | 1.98 |
| Totals anchor reference last update utc | 2026-10-28T16:07:31Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5386 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.0, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:07:32Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:07:31Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.86, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.76 |
| Reference draw odds | 3.81 |
| Reference away odds | 4.47 |
| Market reference 1x2 last update utc | 2026-10-28T16:07:31Z |
| Market reference home last update utc | 2026-10-28T16:07:31Z |
| Market reference draw last update utc | 2026-10-28T16:07:31Z |
| Market reference away last update utc | 2026-10-28T16:07:31Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-28T16:07:31Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:07:31Z |
| Market best over 2 5 last update utc | 2026-10-28T16:07:31Z |
| Market best under 2 5 last update utc | 2026-10-28T16:07:31Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0347 |
| Raw ev home | 0.0300 |
| Raw edge prob draw | -0.0169 |
| Raw ev draw | -0.1364 |
| Raw edge prob away | -0.0177 |
| Raw ev away | -0.1593 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06798883978613258, 0.05872995029115551, 0.02918387630014537, 0.009120866531216524, 0.0021379152676126332, 0.0004008988993182052, 6.264667029812524e-05, 8.391011811812589e-06, 9.834192947454164e-07, 1.0244967734176971e-07, 9.605610545941995e-09, 8.187412445208168e-10, 6.397050839027243e-11, 4.613715698255958e-12, 3.089848409833952e-13, 1.9313469299242165e-14, 1.1317609117538126e-15], [0.1092637611089046, 0.11375827871972356, 0.05319212047911973, 0.016624187493558675, 0.0038966806643308803, 0.0007307001418579285, 0.00011418322911740723, 1.5293914579586835e-05, 1.792433502307868e-06, 1.8673035494545362e-07, 1.7507708303735672e-08, 1.4922823298685235e-09, 1.165961284378443e-10, 8.409209206962493e-12, 5.631725792275423e-13, 3.52017797522652e-14, 2.0628090029036797e-15], [0.10256056229922586, 0.09616007042489036, 0.047137123401382756, 0.015150074221299444, 0.0035511510745526286, 0.0006659069134627465, 0.00010405828234472406, 1.3937760332932473e-05, 1.6334934027440298e-06, 1.7017245130863376e-07, 1.5955250766344456e-08, 1.359957475539885e-09, 1.0625722312347242e-10, 7.663541070941347e-12, 5.132344890842825e-13, 3.2080339335398706e-14, 1.8798939503337804e-15], [0.062310819966931684, 0.05842219174629119, 0.02738812047612094, 0.008950334644518486, 0.0021575070409251746, 0.00040457272141755364, 6.322076197606016e-05, 8.467906721433337e-06, 9.92431311351363e-07, 1.0338852224588247e-07, 9.69363599166268e-09, 8.262441578061466e-10, 6.455673166958404e-11, 4.655995611523841e-12, 3.118163661861308e-13, 1.949045718932446e-14, 1.1421323252344957e-15], [0.02839277250857572, 0.026620866176775445, 0.012479769557336132, 0.0039003150678868156, 0.0009559562084704194, 0.0001843490624658782, 2.8807399959713288e-05, 3.8585168561911175e-06, 4.5221482350161193e-07, 4.711038618466298e-08, 4.417037067371031e-09, 3.764893869408158e-10, 2.941615271897253e-11, 2.1215677192031814e-12, 1.420833677725957e-13, 8.881091877113899e-15, 5.204281263235395e-16], [0.01035004233488254, 0.009704127761304348, 0.0045492613730833825, 0.0014217852821458697, 0.00033326399981440877, 6.534565216135283e-05, 1.050118684432353e-05, 1.406548543273602e-06, 1.6484626734812335e-07, 1.717319051095327e-08, 1.6101464070910099e-09, 1.3724200735572647e-10, 1.0723096023073392e-11, 7.733769466662988e-13, 5.179377502091007e-14, 3.2374322331624004e-15, 1.8971212262153388e-16], [0.0031440916962672248, 0.0029478785232601194, 0.0013819552079564535, 0.00043190386617104724, 0.00010123751580704776, 1.898391824577614e-05, 3.1019365003892707e-06, 4.2727531465246725e-07, 5.007629568654933e-08, 5.2167985344299594e-09, 4.891234049591742e-10, 4.1690791375017315e-11, 3.257416353824389e-12, 2.3493314881456525e-13, 1.57336919688478e-14, 9.834533494813261e-16, 5.762993909747746e-17], [0.0008186560795480512, 0.0007675662505966922, 0.000359832391020852, 0.00011245878300592156, 2.6360143341931808e-05, 4.943017439344718e-06, 7.724231329323827e-07, 1.0818213058478431e-07, 1.3038825793061464e-08, 1.3583458272094448e-09, 1.273575607207858e-10, 1.0855414891635698e-11, 8.481634631851182e-13, 6.11717052631611e-14, 4.0967261226273254e-15, 2.5607079604600485e-16, 1.5005637418955215e-17], [0.00018651588794454816, 0.00017487600026783482, 8.198126123917068e-05, 2.5621686925103412e-05, 6.005678898128064e-06, 1.1261765591892275e-06, 1.7598255251134054e-07, 2.3571431167344552e-08, 2.8886456061567113e-09, 3.094743744376857e-10, 2.901610226531618e-11, 2.4732087113280428e-12, 1.9323860826322743e-13, 1.3936859701255048e-14, 9.33364485425057e-16, 5.834107031557754e-17, 3.418761378911979e-18], [3.7772667043879486e-05, 3.541539010363639e-05, 1.6602611813665666e-05, 5.188831149934969e-06, 1.2162530060650268e-06, 2.2807007312708629e-07, 3.563948591617664e-08, 4.773619186246136e-09, 5.594640215989978e-10, 6.09435785519368e-11, 5.876258488525089e-12, 5.008671926693475e-13, 3.9134133238663335e-14, 2.822453180445834e-15, 1.8902232044180723e-16, 1.1815067597185281e-17, 6.9235782909019e-19], [6.884651769873698e-06, 6.455001651710894e-06, 3.0260823434759408e-06, 9.457445914125358e-07, 2.2168088901672067e-07, 4.156929217588948e-08, 6.495846573533179e-09, 8.700658002548364e-10, 1.0197095592979344e-10, 1.0623028843402553e-11, 1.041469747838913e-12, 9.129077913605889e-14, 7.132800004592025e-15, 5.144356701518822e-16, 3.4452236360847254e-17, 2.153478491461709e-18, 1.2619290419430556e-19], [1.1407582567902795e-06, 1.069567013397278e-06, 5.014092991824317e-07, 1.5670595805434498e-07, 3.673160429479108e-08, 6.887859381077084e-09, 1.0763348476137616e-09, 1.4416629609862685e-10, 1.6896164659878448e-11, 1.7601918398052938e-12, 1.650343635823374e-13, 1.470889325433413e-14, 1.1818753905430093e-15, 8.523985786487591e-17, 5.7085927374722986e-18, 3.5682245842919195e-19, 2.0909641071161932e-20], [1.7326733778346947e-07, 1.624542517130628e-07, 7.615798868172205e-08, 2.3801733632225724e-08, 5.579085008406257e-09, 1.0461822659465774e-09, 1.6348220361283638e-10, 2.189711113149955e-11, 2.5663224017378197e-12, 2.6735178312833344e-13, 2.5066717378980822e-14, 2.13658000027792e-15, 1.7455657475606803e-16, 1.2946900149418432e-17, 8.670659714485983e-19, 5.4197001919877416e-20, 3.1759207709808206e-21], [2.4292805783173362e-08, 2.2776765869445383e-08, 1.0677668691338873e-08, 3.3371026520478403e-09, 7.822110634977256e-10, 1.4667913136751102e-10, 2.292088902719166e-11, 3.070066607676775e-12, 3.598091393331934e-13, 3.7483838710779306e-14, 3.5144586665853033e-15, 2.9955745641932435e-16, 2.3405249103404404e-17, 1.7650955254607656e-18, 1.215662773783836e-19, 7.598646453004287e-21, 4.45277381525879e-22], [3.162670663722365e-09, 2.965298034023873e-09, 1.3901214140704694e-09, 4.3445605887041026e-10, 1.0183574534139988e-10, 1.909609741652935e-11, 2.9840613702574707e-12, 3.9969074311286137e-13, 4.6843407865899986e-14, 4.880005961946008e-15, 4.575459674309469e-16, 3.899926537810278e-17, 3.047120014754495e-18, 2.197660422014175e-19, 1.5389724661195605e-20, 9.89264740986019e-22, 5.79704841153613e-23], [3.842970395714926e-10, 3.6031423347169517e-10, 1.6891406057545637e-10, 5.279088308590746e-11, 1.2374091272341176e-11, 2.320372395620789e-12, 3.625941719584201e-13, 4.856653937581353e-14, 5.6919562231996035e-15, 5.92970955142016e-16, 5.559654464453054e-17, 4.7388121697844804e-18, 3.702564463386034e-19, 2.67038362182634e-20, 1.7883808034954903e-21, 1.1688722252462116e-22, 7.044010520475505e-24], [4.377754307383178e-11, 4.1045520135960784e-11, 1.9241997208365726e-11, 6.013720950793314e-12, 1.4096057421583793e-12, 2.6432730944241876e-13, 4.1305241380286733e-14, 5.532501035767389e-15, 6.48404315092647e-16, 6.754881994200621e-17, 6.3333304119283004e-18, 5.398260525578284e-19, 4.217809626122992e-20, 3.0419915323445927e-21, 2.0372500851095654e-22, 1.273407680726853e-23, 7.802715659611431e-25]] |
| Legacy trial inputs | {"lambda_home": 1.8226543976563787, "lambda_away": 0.9375930500881839, "rho": -0.03104744974939825, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-28T16:07:31Z", "over": 1.86, "under": 1.98, "bookmaker": "pinnacle", "event_id": "04aa939b89001eedf55668e66c74836e", "kickoff_utc": "2026-10-31T14:00:00Z", "home_team": "Bologna", "away_team": "Monza"}} |
| Legacy p home | 0.5646 |
| Legacy p draw | 0.2389 |
| Legacy p away | 0.1966 |
| Legacy p over 1 5 | 0.7640 |
| Legacy p under 3 5 | 0.7023 |
| Legacy p btts yes | 0.5153 |
| Legacy p over 2 5 | 0.5185 |
| Legacy goal margin distribution | {"-1": 0.12942494291139364, "-10": 1.1208951472975461e-08, "-11": 9.433218011997882e-10, "-12": 7.291296297163486e-11, "-13": 5.210110749144134e-12, "-14": 3.460665146859942e-13, "-15": 2.1376278302145844e-14, "-16": 1.1317609117538126e-15, "-2": 0.049794053002342915, "-3": 0.013750703580778708, "-4": 0.002981611486725647, "-5": 0.0005300610831655709, "-6": 7.968202440131007e-05, "-7": 1.0363698852992625e-05, "-8": 1.1869613501378678e-06, "-9": 1.2138407421266806e-07, "0": 0.23885909148166568, "1": 0.23706531156068122, "10": 8.033818072027725e-06, "11": 1.3143372716721332e-06, "12": 1.974884255558134e-07, "13": 2.7433031598723487e-08, "14": 3.542226894402426e-09, "15": 4.2534255970745334e-10, "16": 4.377754307383178e-11, "2": 0.17499067027817367, "3": 0.09394037422958147, "4": 0.03959755465243084, "5": 0.013684633856983559, "6": 0.003999056774601134, "7": 0.0010111182373338645, "8": 0.00022511979514713094, "9": 4.475368140369262e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5786 |
| Legacy raw p draw | 0.2341 |
| Legacy raw p away | 0.1873 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8227 |
| Legacy lambda away | 0.9376 |
| Legacy model home team | Bologna |
| Legacy model away team | Monza |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021258779398154137, "mu": 9.016791672405699, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,452.6574 |
| Elo away rating | 1,363.2171 |
| Elo rating diff | 149.4404 |
| Elo home expectancy | 0.7027 |

</details>


---
