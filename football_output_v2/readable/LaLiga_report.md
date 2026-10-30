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
| Training sha256 | b0c6831fb5090bc7a8040a418fd6e7b8533f159a47786af87217f753bfe49191 |
| Training as of utc | 2026-10-30T11:46:35.127291+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 99, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 99, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 95, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-10-30T11:46:35.127291+00:00', 'observations': 416, 'observations_sha256': '23105b594b35eaf1394dc72fb672aa50390e5f858e1e00f9092a12402b94dee5', 'eligible_training_matches': 152, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 164, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 20, 'retrospective_eligible_training_matches': 152, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'f65f773067d2b2d23a6553106aac64520c4d7bf5f0344e70bdd29b486064ec08', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 92, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-20T00:00:00+00:00', 'audit_origin_utc': '2026-09-18T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 16, 'selected_ridge': 1.0, 'proposed_weight': 0.1, 'audit_baseline_poisson_score': 0.817502522631521, 'audit_candidate_poisson_score': 0.809374548264147, 'audit_gain': 0.008127974367374002, 'audit_gain_lower95': -0.007072001060020365, 'audit_baseline_briers': [0.5521078342824518, 0.18074894030573588, 0.22581628123747038, 0.25215851249634236], 'audit_candidate_briers': [0.5419827780121326, 0.18287728247711024, 0.22694550278521158, 0.2502796026252731], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1620, 'tuning_matches': 230, 'audit_matches': 132, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8318519327596118, 'audit_candidate_poisson_score': 0.8321484414148786, 'audit_gain': -0.0002965086552668694, 'audit_gain_lower95': -0.00911683030416819, 'audit_baseline_briers': [0.568024980216413, 0.1832233366275823, 0.19904895402390196, 0.24589676700044888], 'audit_candidate_briers': [0.5724746293057228, 0.1802373351182294, 0.20127854712845308, 0.24346965372402718], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1833.973 |
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
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261030T114635127291Z_1621a7c7e263830fc2d26f6251f9597ef12d66985f9f3682af6ab610e77b96de.json |
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

The model's most likely 1X2 outcome is **Villarreal win** at **68.0%**. Expected goals are 2.16 for Villarreal and 0.95 for Espanyol (3.12 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 68.1%; Under 3.5 goals: 53.3%; Double Chance 1X: 86.5%; Double Chance X2: 32.0%; Double Chance 12 (either team wins): 81.5%; Under 4.5 goals: 72.3%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 68.0% | 1.47 |
| Draw | 18.5% | 5.42 |
| Espanyol win | 13.5% | 7.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.16 |
| Espanyol expected goals | 0.95 |
| Expected total goals | 3.12 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 86.9% |
| Under 1.5 | 13.1% |
| Over 2.5 | 68.1% |
| Under 2.5 | 31.9% |
| Over 3.5 | 46.7% |
| Under 3.5 | 53.3% |
| Over 4.5 | 27.7% |
| Under 4.5 | 72.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.65% |
| 2 | 2-0 | 9.00% |
| 3 | 1-1 | 8.20% |
| 4 | 3-1 | 7.85% |
| 5 | 3-0 | 7.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 68.0% | 69.5% | 1.42 | -3.4% |
| Draw | 18.5% | 17.8% | 5.27 | -2.7% |
| Espanyol win | 13.5% | 12.8% | 7.24 | -2.4% |

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
| Market best home last update utc | 2026-10-30T11:46:34Z |
| Market best draw last update utc | 2026-10-30T11:46:34Z |
| Market best away last update utc | 2026-10-30T11:46:34Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Villarreal |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1640 |
| Dc lambda away | 0.9515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:46:35.127291+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.37 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.62 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.14 |
| Fair Over 3.5 odds | 2.14 |
| Fair Under 3.5 odds | 1.88 |
| Fair Over 4.5 odds | 3.61 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.08645693199732625, "-10": 1.926606673265679e-08, "-11": 1.842716882125621e-09, "-12": 1.620313922534219e-10, "-13": 1.318186465933642e-11, "-14": 9.976384637575838e-13, "-15": 7.05756037362286e-14, "-16": 4.684541422310138e-15, "-17": 2.9056505083885527e-16, "-18": 1.5117309254838205e-17, "-2": 0.03488555638720859, "-3": 0.01044177385807734, "-4": 0.0024980590786536135, "-5": 0.0004951383239793063, "-6": 8.353639650268977e-05, "-7": 1.2247668340129765e-05, "-8": 1.5860881206507143e-06, "-9": 1.8380786256714433e-07, "0": 0.18467195181463647, "1": 0.22022838760823363, "10": 7.865861454364708e-05, "11": 1.7109405107961247e-05, "12": 3.421358008076074e-06, "13": 6.329935252784889e-07, "14": 1.0894785061767355e-07, "15": 1.752762794783973e-08, "16": 2.64581022115304e-09, "17": 3.732141016137897e-10, "18": 4.415828809596946e-11, "2": 0.19907392891717388, "3": 0.1355083569500902, "4": 0.07372547234090378, "5": 0.033232610929751195, "6": 0.012750779055342568, "7": 0.004251453788839417, "8": 0.0012520867513534035, "9": 0.0003299850426881496} |
| Raw goal margin distribution | {"-1": 0.10043708424616798, "-10": 8.956965980459262e-09, "-11": 7.630664788107699e-10, "-12": 5.972820692225259e-11, "-13": 4.323420373861838e-12, "-14": 2.9102089177525766e-13, "-15": 1.830071892340664e-14, "-16": 1.0736616115132315e-15, "-17": 5.360372098618496e-17, "-2": 0.037942159407786696, "-3": 0.0104062714601915, "-4": 0.002257397001125719, "-5": 0.00040318148705039943, "-6": 6.105128926983718e-05, "-7": 8.0124297807221e-06, "-8": 9.270948348905332e-07, "-9": 9.586582390576288e-08, "0": 0.20092032938685725, "1": 0.2322040849627517, "10": 3.314297948063552e-05, "11": 6.421197991180225e-06, "12": 1.1430263047391021e-06, "13": 1.8815998727092282e-07, "14": 2.8803617810223554e-08, "15": 4.119211446970659e-09, "16": 5.495869635033895e-10, "17": 6.24003459546057e-11, "2": 0.19623124938450062, "3": 0.12239518631900943, "4": 0.060380984948617614, "5": 0.02452538840370732, "6": 0.008445652605884677, "7": 0.0025207261846059755, "8": 0.0006632979576808706, "9": 0.00015598088137782707} |
| Unadjusted home-win probability | 64.8% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 15.2% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 54.6% |
| P home draw | 86.5% |
| P draw away | 32.0% |
| P home away | 81.5% |
| Raw p home draw | 84.8% |
| Raw p draw away | 35.2% |
| Raw p home away | 79.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1272 |
| Totals anchor target over 2 5 | 0.6811 |
| Totals anchor reference over odds | 1.43 |
| Totals anchor reference under odds | 2.90 |
| Totals anchor reference last update utc | 2026-10-30T11:46:34Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6102 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:36:16Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.73, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:36:16Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.3, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:36:16Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:36:16Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:36:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.15, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.82, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:36:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:36:16Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:36:16Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:36:16Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:36:16Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.94, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:55Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.84, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:55Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.16, "price": 5.84, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.42 |
| Reference draw odds | 5.27 |
| Reference away odds | 7.24 |
| Market reference 1x2 last update utc | 2026-10-30T11:46:34Z |
| Market reference home last update utc | 2026-10-30T11:46:34Z |
| Market reference draw last update utc | 2026-10-30T11:46:34Z |
| Market reference away last update utc | 2026-10-30T11:46:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.86 |
| Market reference over 2 5 last update utc | 2026-10-30T11:45:53Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:45:53Z |
| Home probability edge | -1.4% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | -0.0470 |
| Raw ev home | -0.0805 |
| Raw edge prob draw | 0.0232 |
| Raw ev draw | 0.0589 |
| Raw edge prob away | 0.0238 |
| Raw ev away | 0.0970 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.040578361878337806, 0.03473785632390534, 0.01788019927215723, 0.005836050261084233, 0.0014286536519312566, 0.00027978528845600805, 4.566059306407864e-05, 6.387213476046465e-06, 7.817886627079037e-07, 8.505792468457763e-08, 8.328805222026262e-09, 7.414091545015296e-10, 6.049850205580043e-11, 4.556896796331804e-12, 3.187198268059841e-13, 2.0805863515629255e-14, 1.2733086404084854e-15, 7.33419897835552e-17], [0.09088208279010349, 0.08637140369405033, 0.03985172797915061, 0.013007499745237438, 0.0031842104132386146, 0.0006235907686711028, 0.00010176919767275132, 1.4235942794470797e-05, 1.742465430569019e-06, 1.895787191968976e-07, 1.856339938092168e-08, 1.65246681520246e-09, 1.3484021125134596e-10, 1.0156498190669663e-11, 7.103688077577921e-13, 4.6372504051860895e-14, 2.837974498979893e-15, 1.6346602080969152e-16], [0.10349914190030617, 0.10134554737035673, 0.046115304218608974, 0.014495681330108923, 0.003548514344981743, 0.0006949354787697498, 0.00011341256102850972, 1.5864669938422675e-05, 1.9418200349769426e-06, 2.1126832629419111e-07, 2.068722868342981e-08, 1.8415247227296873e-09, 1.5026721284386227e-10, 1.1318498103809716e-11, 7.916417502046545e-13, 5.167795920665536e-14, 3.1626657517522113e-15, 1.8216808705499524e-16], [0.07689361821057006, 0.07529362740363356, 0.03686346448201018, 0.011182664479755406, 0.002636332072400979, 0.0005162951344753398, 8.425869053493481e-05, 1.1786492630603852e-05, 1.4426551337689024e-06, 1.5695962037733194e-07, 1.536936282767094e-08, 1.3681417676998498e-09, 1.1163947335053446e-10, 8.408961233221883e-12, 5.881420597517446e-13, 3.8393605900284437e-14, 2.3496698463174472e-15, 1.353398982732557e-16], [0.04284548943802947, 0.041953966957817744, 0.020540497571436007, 0.006704364665624687, 0.0015253448433108342, 0.0002876821021803389, 4.6949342733367254e-05, 6.56748969898949e-06, 8.03854295519647e-07, 8.745864629048823e-08, 8.563881997318959e-09, 7.62335093884982e-10, 6.220604502195183e-11, 4.6855131555414494e-12, 3.277155503353632e-13, 2.1393099640385716e-14, 1.3092472031627158e-15, 7.541203440487407e-17], [0.019098968241106386, 0.018701559791369247, 0.009156210278349007, 0.002988563078752189, 0.0007315943772720378, 0.0001331590707156889, 2.092831748607608e-05, 2.9275491733199924e-06, 3.5832914647439227e-07, 3.89858986283298e-08, 3.81746859313973e-09, 3.3982138932615154e-10, 2.7729203093769898e-11, 2.088632155326547e-12, 1.4608372946759517e-13, 9.536269417613233e-15, 5.836150101431097e-16, 3.361595512122952e-17], [0.0070946905702949205, 0.006947065319270246, 0.003401255916098482, 0.0011101610320456998, 0.00027176524219467646, 5.322207840715556e-05, 8.072554412688244e-06, 1.0874962066969145e-06, 1.331084687120475e-07, 1.4482085308544515e-08, 1.4180744262328025e-09, 1.2623339522853216e-10, 1.0300562482100113e-11, 7.758638409229379e-13, 5.4265698798147367e-14, 3.5424364216343205e-15, 2.1679537118833577e-16, 1.248731328306709e-17], [0.0022589687412641318, 0.0022119644605020825, 0.0010829691188613431, 0.0003534782869404995, 8.653079101860401e-05, 1.6946054274763866e-05, 2.765573889005412e-06, 3.595486207893187e-07, 4.238209785737713e-08, 4.6111352843627486e-09, 4.515187477038633e-10, 4.019305579285345e-11, 3.279727062646931e-12, 2.47037153594873e-13, 1.7278345840919987e-14, 1.1279213751608126e-15, 6.902823483460918e-17, 3.975994455195576e-18], [0.0006293540582238232, 0.0006162585539297118, 0.00030171776945662966, 9.847989054311431e-05, 2.4107683959540183e-05, 4.721210981757797e-06, 7.704954559881999e-07, 1.0778044325473328e-07, 1.2260844354969533e-08, 1.284673245460122e-09, 1.2579419583847117e-10, 1.1197880835435229e-11, 9.13739751701149e-13, 6.882513790783632e-14, 4.813788201554506e-15, 3.142415748602214e-16, 1.9231430223721155e-17, 1.1077215014725918e-18], [0.00015585736520388945, 0.0001526143086626213, 7.471936657629516e-05, 2.438820575644653e-05, 5.970184912616765e-06, 1.1691916411330204e-06, 1.9081054630966145e-07, 2.669145560703746e-08, 3.2670079782067076e-09, 3.303528718414294e-10, 3.1152499400192215e-11, 2.773116626599038e-12, 2.2628450285061885e-13, 1.704430838880011e-14, 1.1921180708062284e-15, 7.782084385609346e-17, 4.762597467363348e-18, 2.743234151638926e-19], [3.473778578812875e-05, 3.4014967182270847e-05, 1.66535944384567e-05, 5.435689652625452e-06, 1.330646160601359e-06, 2.6059165520870754e-07, 4.2528217227012574e-08, 5.949042357014494e-09, 7.281569476462577e-10, 7.922284085947156e-11, 7.209760077462601e-12, 6.180775044815888e-13, 5.043472008470629e-14, 3.798867849090064e-15, 2.6570154142956493e-16, 1.7344857589424513e-17, 1.0614967755930208e-18, 6.11417241666126e-20], [7.038567019177034e-06, 6.89210957853677e-06, 3.3743498011128025e-06, 1.101378946510923e-06, 2.696154048887003e-07, 5.2801057644024514e-08, 8.617063533759902e-09, 1.2053944251126954e-09, 1.475390949713047e-10, 1.6052124860230608e-11, 1.5718114667891413e-12, 1.3004036163413736e-13, 1.0219078428739474e-14, 7.697262605020418e-16, 5.3836422328614305e-17, 3.514413478333047e-18, 2.1508038080553402e-19, 1.2388530628852173e-20], [1.3073076626167406e-06, 1.2801054020039492e-06, 6.267345809630188e-07, 2.0456452745218484e-07, 5.0076994906802e-08, 9.807000070359819e-09, 1.600489582076432e-09, 2.2388383375932915e-10, 2.740316159042236e-11, 2.9814400820344505e-12, 2.9194027266114745e-13, 2.598778395564271e-14, 1.9708719231350753e-15, 1.4296504327230288e-16, 9.999303444339096e-18, 6.527492964563027e-19, 3.9947936723415187e-20, 2.3009827107612405e-21], [2.241347819909731e-07, 2.1947101926207902e-07, 1.0745214970221752e-07, 3.507210052743614e-08, 8.58558138773003e-09, 1.6813867811007878e-09, 2.7440012310452684e-10, 3.838434953445359e-11, 4.6982067225390046e-12, 5.111607939850711e-13, 5.005246373016526e-14, 4.455543601471352e-15, 3.6356944353425434e-16, 2.545156102555592e-17, 1.7143567360972271e-18, 1.1191231065160974e-19, 6.848978510972583e-21, 3.944979999651881e-22], [3.568256158116067e-08, 3.494008422313782e-08, 1.7106528110982307e-08, 5.58352601829242e-09, 1.3668362128198468e-09, 2.676790582230771e-10, 4.368487212729743e-11, 6.1108405569604916e-12, 7.4796088857272e-13, 8.137749236074333e-14, 7.968420177696307e-15, 7.093285902562458e-16, 5.788074899710046e-17, 4.3597211618710505e-18, 2.834008046229546e-19, 1.7816591789296125e-20, 1.090366677206164e-21, 6.280461716990214e-23], [5.30199809702734e-09, 5.191674920526428e-09, 2.5418236660189532e-09, 8.296445942187903e-10, 2.0309536866728377e-10, 3.977387817533084e-11, 6.491044886477559e-12, 9.079971719672745e-13, 1.1113796297509098e-13, 1.2091713445407958e-14, 1.1840110896288915e-15, 1.0539766959139284e-16, 8.600380898639551e-18, 6.4780195926332485e-19, 4.5308756701969965e-20, 2.7489148473294546e-21, 1.620153316196157e-22, 9.332008296600558e-24], [7.385746332177755e-10, 7.232064836770833e-10, 3.540790561367358e-10, 1.1557047751861795e-10, 2.829142611457534e-11, 5.540548477651026e-12, 9.042102634699531e-13, 1.2648508467487086e-13, 1.5481650264439028e-14, 1.6843900468247522e-15, 1.6493415128510337e-16, 1.4682020577132215e-17, 1.198043275667572e-18, 9.023958245645508e-20, 6.311563631354947e-21, 4.120155711684606e-22, 2.3434950893554244e-23, 1.2999598413117754e-24], [9.683230472298145e-11, 9.481743273520518e-11, 4.642224294988539e-11, 1.5152098640738904e-11, 3.709204014547438e-12, 7.264046914026115e-13, 1.1854829536252558e-13, 1.658308004539579e-14, 2.0297527272084853e-15, 2.2083532652061566e-16, 2.1624021836336572e-17, 1.924915677485435e-18, 1.5707186020638056e-19, 1.1831040972025313e-20, 8.274901754575188e-22, 5.401812564856098e-23, 3.3058827899796334e-24, 1.7697378166514224e-25]] |
| Legacy trial inputs | {"lambda_home": 2.2288190065760123, "lambda_away": 0.9791921508680347, "rho": -0.021898200937208512, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6746 |
| Legacy p draw | 0.1859 |
| Legacy p away | 0.1395 |
| Legacy p over 1 5 | 0.8338 |
| Legacy p under 3 5 | 0.5979 |
| Legacy p btts yes | 0.5558 |
| Legacy p over 2 5 | 0.6261 |
| Legacy goal margin distribution | {"-1": 0.09203133931999098, "-10": 1.0140285683896925e-08, "-11": 8.881779951184009e-10, "-12": 7.148637846573332e-11, "-13": 5.321368645176974e-12, "-14": 3.6839033650787047e-13, "-15": 2.382600610166414e-14, "-16": 1.436774661218177e-15, "-17": 7.33419897835552e-17, "-2": 0.035002523236980956, "-3": 0.009806395607505071, "-4": 0.0021782877736541556, "-5": 0.00039895321689899173, "-6": 6.200422976978268e-05, "-7": 8.357107453495574e-06, "-8": 9.93487102446234e-07, "-9": 1.0557932347103692e-07, "0": 0.18591468288635152, "1": 0.23658315246593553, "10": 4.229310957904031e-05, "11": 8.431916851366932e-06, "12": 1.5447438724148267e-06, "13": 2.617359695616631e-07, "14": 4.124346765646458e-08, "15": 6.071626823654309e-09, "16": 8.333920659529807e-10, "17": 9.683230472298145e-11, "2": 0.20261133918201452, "3": 0.12920540539094286, "4": 0.06532710406957243, "5": 0.02723372219207706, "6": 0.009634146092862473, "7": 0.002955662054451531, "8": 0.0007997751432616718, "9": 0.00019346010659473096} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6546 |
| Legacy raw p draw | 0.1941 |
| Legacy raw p away | 0.1512 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2288 |
| Legacy lambda away | 0.9792 |
| Legacy model home team | Villarreal |
| Legacy model away team | Espanol |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 86.9% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:46:55Z |
| Market reference home draw last update utc | 2026-10-30T11:46:55Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 31.4% |
| Market draw away odds | 3.10 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:46:55Z |
| Market reference draw away last update utc | 2026-10-30T11:46:55Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.8% |
| Market home away odds | 1.19 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:46:55Z |
| Market reference home away last update utc | 2026-10-30T11:46:55Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.10 |
| Market reference dc home draw odds | 1.12 |
| Market reference dc home away odds | 1.19 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:55Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.16, "price": 1.69, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:55Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.69, "price": 2.16, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:55Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.71, "price": 2.12, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:55Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.12, "price": 1.71, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 87.6% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-30T11:46:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 54.2% |
| Market under 3 5 odds | 1.79 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:46:34Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market reference under 3 5 last update utc | 2026-10-30T11:46:34Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.4% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:46:55Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.35 |
| Market reference btts yes last update utc | 2026-10-30T11:46:55Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 10.16398044941085, "version": "count-markets-nb2-v1"}} |
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
| Market best home last update utc | 2026-10-30T11:46:34Z |
| Market best draw last update utc | 2026-10-30T11:46:34Z |
| Market best away last update utc | 2026-10-30T11:46:34Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.9277 |
| Dc lambda away | 0.7229 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:46:35.127291+00:00 |
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
| Goal margin distribution | {"-1": 0.0312021446582029, "-10": 2.328673406066788e-10, "-11": 1.5065201260434648e-11, "-12": 8.955376092050333e-13, "-13": 4.9231725746146827e-14, "-14": 2.51695787298783e-15, "-15": 1.202477939729467e-16, "-16": 5.391258321494552e-18, "-17": 2.2768799227491172e-19, "-18": 9.086629435237855e-21, "-19": 3.421737703929333e-22, "-2": 0.008991551474509429, "-20": 1.1184293721275322e-23, "-3": 0.0018670694232489832, "-4": 0.0003069869930697175, "-5": 4.1586199257019784e-05, "-6": 4.778178800131542e-06, "-7": 4.7596158241951557e-07, "-8": 4.180769406608281e-08, "-9": 3.2823210364379717e-09, "0": 0.08280515346340193, "1": 0.2020314488430606, "10": 0.0004291271536915702, "11": 0.00011243396672176512, "12": 2.7067715740298647e-05, "13": 6.026400907104428e-06, "14": 1.2477687062813982e-06, "15": 2.414240009826404e-07, "16": 4.383678034808298e-08, "17": 7.497799417175053e-09, "18": 1.2118299735482804e-09, "19": 1.8481225693919616e-10, "2": 0.22895523982981547, "20": 2.4464582116997864e-11, "3": 0.19254028107190863, "4": 0.12821129663450442, "5": 0.07033973536088504, "6": 0.032730985335346546, "7": 0.013204250801658783, "8": 0.004697245531006132, "9": 0.001493527715392184} |
| Raw goal margin distribution | {"-1": 0.045243674776426324, "-10": 3.376618607429622e-10, "-11": 2.1844814634859478e-11, "-12": 1.2985457501325657e-12, "-13": 7.138689384145592e-14, "-14": 3.649634494002308e-15, "-15": 1.743614787602252e-16, "-16": 7.817422193422082e-18, "-17": 3.301517118720034e-19, "-18": 1.3175777225740295e-20, "-19": 4.9615816330149325e-22, "-2": 0.01303791246097093, "-20": 1.621742842591359e-23, "-3": 0.002707284473417736, "-4": 0.00044513669900533343, "-5": 6.030074198369644e-05, "-6": 6.928445785534588e-06, "-7": 6.90152913428037e-07, "-8": 6.062191346776233e-08, "-9": 4.75942494053469e-09, "0": 0.1214514812668462, "1": 0.18869779139790394, "10": 0.0004008056497846055, "11": 0.00010501355764162871, "12": 2.5281302528044863e-05, "13": 5.628670921091551e-06, "14": 1.1654185543836785e-06, "15": 2.254905166336652e-07, "16": 4.094364358147018e-08, "17": 7.002960175098601e-09, "18": 1.1318517036225038e-09, "19": 1.7261503051823561e-10, "2": 0.21384466790823364, "20": 2.2849970335738247e-11, "3": 0.17983302105418097, "4": 0.11974961643712177, "5": 0.06569745842105292, "6": 0.03057080805204164, "7": 0.01233279757980906, "8": 0.004387237048639205, "9": 0.0013949579775819271} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 18.1, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.03, "price": 18.1, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.10 |
| Reference draw odds | 11.51 |
| Reference away odds | 20.85 |
| Market reference 1x2 last update utc | 2026-10-30T11:46:34Z |
| Market reference home last update utc | 2026-10-30T11:46:34Z |
| Market reference draw last update utc | 2026-10-30T11:46:34Z |
| Market reference away last update utc | 2026-10-30T11:46:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.21 |
| Reference Under 2.5 odds | 4.51 |
| Market reference over 2 5 last update utc | 2026-10-30T11:45:53Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:45:53Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -8.3% |
| Under 2.5 probability edge | +8.3% |
| Raw edge prob home | -0.0825 |
| Raw ev home | -0.1012 |
| Raw edge prob draw | 0.0552 |
| Raw ev draw | 0.3979 |
| Raw edge prob away | 0.0273 |
| Raw ev away | 0.2823 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.027442053646264928, 0.016476749262918908, 0.005660479945483947, 0.0012197516677420095, 0.0001971291496421262, 2.5487090637434314e-05, 2.746049947204995e-06, 2.536003283213606e-07, 2.0492702897262062e-08, 1.4719604919378688e-09, 9.515586746265186e-11, 5.5921949994046415e-12, 3.012593120440409e-13, 1.4980853152473217e-14, 6.91748029176992e-16, 2.9812341722685844e-17, 1.2045241929270582e-18, 4.580427623187731e-20, 1.6450266544424506e-21, 5.597044470176211e-23], [0.09922146889081171, 0.047152102996072726, 0.015285627107057222, 0.0032938318545215643, 0.0005323298911720115, 6.882564151444621e-05, 7.41546581113115e-06, 6.848253311170738e-07, 5.533873769010907e-08, 3.974899551412354e-09, 2.5696003185085047e-10, 1.5101229629661944e-11, 8.135242153993886e-13, 4.045447333789828e-14, 1.8680045734420888e-15, 8.050560078827013e-17, 3.2527114011244713e-18, 1.236904102005896e-19, 4.442249467033022e-21, 1.5114325197987372e-22], [0.1358931508440846, 0.08784903345998013, 0.0201373753508155, 0.004447351281734718, 0.0007187549724372394, 9.292878887709555e-05, 1.0012405865382094e-05, 9.246552187923719e-07, 7.471869144074324e-08, 5.366932920535561e-09, 3.469489571660197e-10, 2.0389769701526713e-11, 1.0984252147273699e-12, 5.462186954207408e-14, 2.5221908406100746e-15, 1.086991390774992e-16, 4.391830201971635e-18, 1.6700752456102152e-19, 5.997951545059761e-21, 2.0407451415454278e-22], [0.12232249150904599, 0.07907619024755347, 0.025559665221521623, 0.0039059778814864317, 0.0006469781476618542, 8.364866748440147e-05, 9.01253980679657e-06, 8.323166358788451e-07, 6.725707986426598e-08, 4.830976414367301e-09, 3.123016914642405e-10, 1.8353591889616365e-11, 9.887334877971113e-13, 4.9167181213823616e-14, 2.270318009173964e-15, 9.784414765762118e-17, 3.953250103135952e-18, 1.5032969931281566e-19, 5.3989798042436e-21, 1.8369507859540789e-22], [0.08258027632026137, 0.05338457024899307, 0.017255405695284894, 0.0037182906886156744, 0.0004261664147631532, 5.647146317464191e-05, 6.084392317479706e-06, 5.618994260899474e-07, 4.5405453822645814e-08, 3.2614064860313492e-09, 2.1083579690244272e-10, 1.239056424551116e-11, 6.674969061053098e-13, 3.3192909663924354e-14, 1.5326984123650465e-15, 6.605487388465498e-17, 2.668850853613674e-18, 1.0148802526210861e-19, 3.644867256885261e-21, 1.2401309163948065e-22], [0.044600151308241846, 0.028832065194317837, 0.009319340394432439, 0.0020081832455626854, 0.0003245508622719656, 2.97583355290014e-05, 3.2860730197353286e-06, 3.0347197345811196e-07, 2.45226850883342e-08, 1.7614281428480835e-09, 1.1386869676452702e-10, 6.691925297042167e-12, 3.605033106770536e-13, 1.7926905301582355e-14, 8.277833902647177e-16, 3.56750728040325e-17, 1.4413992928368964e-18, 5.48118931584896e-20, 1.968528544577587e-21, 6.697728438051554e-23], [0.02007312949849841, 0.01297640840621411, 0.004194342868596065, 0.0009038203046958156, 0.0001460701655967387, 1.888560650085379e-05, 1.4430306624023886e-06, 1.3658321874939149e-07, 1.1036891557317743e-08, 7.927635708974668e-10, 5.124872963283455e-11, 3.011825725734295e-12, 1.6225123519974811e-13, 8.068337910761355e-15, 3.7255934569933067e-16, 1.6056231543128648e-17, 6.487286212146176e-19, 2.4669114277755867e-20, 8.859729673045851e-22, 3.014437537523327e-23], [0.007743673816173054, 0.005005949571076348, 0.0016180647392340687, 0.0003486695798242171, 5.634994367670183e-05, 7.285559363035495e-06, 7.849664047114819e-07, 5.1410153815282765e-08, 4.257736102919887e-09, 3.058268770115687e-10, 1.9770382381063197e-11, 1.1618814103196877e-12, 6.259216539962107e-14, 3.1125478976396225e-15, 1.4372338157227976e-16, 6.194062554931363e-18, 2.502620649300087e-19, 9.516681208833384e-21, 3.417845567761062e-22, 1.1628889771051766e-23], [0.002613888564501049, 0.001689765691186104, 0.0005461801489717842, 0.00011769393302548931, 1.9021006938487172e-05, 2.459251352408262e-06, 2.6496657239197315e-07, 2.446991534920313e-08, 1.4022916666865286e-09, 1.0323231524396422e-10, 6.673521851313375e-12, 3.9219479072039366e-13, 2.1128078125362433e-14, 1.0506451523190256e-15, 4.8514040294231225e-17, 2.0908149884005154e-18, 8.44763306381434e-20, 3.212369835596351e-21, 1.1536988329935074e-22, 3.9253489638097296e-24], [0.0007842861830557328, 0.0005070070324332488, 0.00016387903834747433, 3.531356567949093e-05, 5.70717249857601e-06, 7.378879431010075e-07, 7.950209680737814e-08, 7.342094368352216e-09, 5.932932324268992e-10, 3.0221969171747794e-11, 2.0023619412806434e-12, 1.1767638437453978e-13, 6.339390275961083e-15, 3.152416240879755e-16, 1.4556432130930406e-17, 6.273401739455439e-19, 2.5346764898292572e-20, 9.638579513829242e-22, 3.4616244411209216e-23, 1.1777843163623023e-24], [0.00021178957005177042, 0.00013691277971249335, 4.425408967027893e-05, 9.536117113672096e-06, 1.5411716230614864e-06, 1.9926013436429787e-07, 2.1468840411603085e-08, 1.982667861741919e-09, 1.6021360738595203e-10, 1.150790608370526e-11, 5.275846874628972e-13, 3.17774702530487e-14, 1.7118964606836167e-15, 8.512822164976192e-17, 3.930836178301577e-18, 1.6940768381060221e-19, 6.844670422596516e-21, 2.6028134311766092e-22, 9.347811652237181e-24, 3.1805027216495616e-25], [5.199264219407842e-05, 3.3610990218490414e-05, 1.086402436762603e-05, 2.341040330223932e-06, 3.783452827158385e-07, 4.891676614204603e-08, 5.270428272598118e-09, 4.867290712193615e-10, 3.933115668257022e-11, 2.825098720710795e-12, 1.8263039049570547e-13, 7.611604878029785e-15, 4.202568621857802e-16, 2.089829620869601e-17, 9.649887805712748e-19, 4.158822876470815e-20, 1.6803117364630453e-21, 6.389698387509226e-23, 2.2948128484967476e-24, 7.807879300363871e-26], [1.1700128913441265e-05, 7.563626349221003e-06, 2.4447783427799855e-06, 5.268144202585783e-07, 8.514067365616318e-08, 1.1007951235757391e-08, 1.186027245706445e-09, 1.0953074586839635e-10, 8.850860123304899e-12, 6.357441713027408e-13, 4.1098105849970403e-14, 2.4152858688342425e-15, 9.227481169422435e-17, 4.7028338894627736e-18, 2.171555946428571e-19, 9.3587788059017e-21, 3.78127810046651e-22, 1.4379014356069863e-23, 5.164116503140762e-25, 1.757040813849067e-26], [2.430397441122222e-06, 1.5711466310113167e-06, 5.078391077877359e-07, 1.0943199245196612e-07, 1.768576029548206e-08, 2.286615533325274e-09, 2.463663096698624e-10, 2.2752163369494245e-11, 1.838535964394263e-12, 1.3205931477964353e-13, 8.537062457319542e-15, 5.017128134759056e-16, 2.702796612913585e-17, 9.531601718838439e-19, 4.5108426193412275e-20, 1.9440428588579034e-21, 7.854621677704504e-23, 2.9868662093718152e-24, 1.0727108759008419e-25, 3.649795253982451e-27], [4.6879100314477417e-07, 3.0305306974781645e-07, 9.795533880501131e-08, 2.110796063626562e-08, 3.411345473795745e-09, 4.4105740548303656e-10, 4.752075010327613e-11, 4.388586537012656e-12, 3.546288785871002e-13, 2.547246701410895e-14, 1.6466846144425139e-15, 9.677365896639325e-17, 5.213331424834804e-18, 2.5924560466103276e-19, 8.489443835789586e-21, 3.7497974057264505e-22, 1.51505095969553e-23, 5.761263498961309e-25, 2.0691151129819507e-26, 7.039964531880962e-28], [8.439525192478077e-08, 5.455787333027499e-08, 1.7634650495357612e-08, 3.800012465183444e-09, 6.14135848879637e-10, 7.940244287822995e-11, 8.555039771917278e-12, 7.900660718748973e-13, 6.384293501238122e-14, 4.5857434472510466e-15, 2.9644844279065304e-16, 1.742191567961754e-17, 9.38542796288334e-19, 4.667132681512487e-20, 2.1550707436250357e-21, 6.586673639645443e-23, 2.7275077073716347e-24, 1.037185613926396e-25, 3.724975309894224e-27, 1.2673869085028712e-28], [1.4243871135405741e-08, 9.208045469558508e-09, 2.9763011952102228e-09, 6.413499175907468e-10, 1.036512326412762e-10, 1.3401206091569598e-11, 1.4438831722200252e-12, 1.3334398629762108e-13, 1.0775138630226959e-14, 7.739622458961559e-16, 5.0033305441936827e-17, 2.940396719160829e-18, 1.5840325540244088e-19, 7.876987741745779e-21, 3.6372366051157774e-22, 1.5675439036231652e-23, 4.49154343577982e-25, 1.7505176999094134e-26, 6.286854661443589e-28, 2.1390416393928028e-29], [2.2626069628028945e-09, 1.4626773575226716e-09, 4.727787652432591e-10, 1.0187699504854798e-10, 1.6464765683979475e-11, 2.1287515117552493e-12, 2.2935760144715033e-13, 2.1181392963809415e-14, 1.7116065891186882e-15, 1.2294216578233073e-16, 7.947678281332997e-18, 4.670754198020596e-19, 2.5162001621408145e-20, 1.2512418247091481e-21, 5.777668717909314e-23, 2.4900083110278522e-24, 1.0060515470813141e-25, 2.7131086442441428e-27, 9.986527535870536e-29, 3.3978196383602774e-30], [3.394428138046393e-10, 2.1943507029200368e-10, 7.092763216040501e-11, 1.5283880245113954e-11, 2.4700915732534705e-12, 3.193614334793459e-13, 3.440888801396564e-14, 3.1776935836131773e-15, 2.5678015063530127e-16, 1.8444137835010378e-17, 1.192333588369987e-18, 7.007199984931977e-20, 3.7748759602273566e-21, 1.8771490263743354e-22, 8.667825031390697e-24, 3.7355821907539234e-25, 1.509307509381784e-26, 5.739422959249471e-28, 1.4618122562137202e-29, 5.097506892743303e-31], [4.82439682068929e-11, 3.118763492438396e-11, 1.0080727273567061e-11, 2.1722511204718223e-12, 3.5106655519518257e-13, 4.538986308354344e-14, 4.890429939505788e-15, 4.516358631981927e-16, 3.6495376892970266e-17, 2.6214088592487083e-18, 1.6946272358689122e-19, 9.959118871992403e-21, 5.365115666139454e-22, 2.667934458029927e-23, 1.2319314424431863e-24, 5.309268634235686e-26, 2.1451325683078662e-27, 8.157266187738579e-29, 2.9296217318839053e-30, 7.068932274441091e-32]] |
| Legacy trial inputs | {"lambda_home": 2.700411847453399, "lambda_away": 0.6464566677151573, "rho": -0.021898200937208512, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8521 |
| Legacy p draw | 0.0991 |
| Legacy p away | 0.0488 |
| Legacy p over 1 5 | 0.8569 |
| Legacy p under 3 5 | 0.5585 |
| Legacy p btts yes | 0.4329 |
| Legacy p over 2 5 | 0.6682 |
| Legacy goal margin distribution | {"-1": 0.03691660428178881, "-10": 1.1140625852010202e-10, "-11": 6.462678923643279e-12, "-12": 3.443365449305555e-13, "-13": 1.6961613601794123e-14, "-14": 7.767995017110878e-16, "-15": 3.323758364126722e-17, "-16": 1.334396249751303e-18, "-17": 5.0450600213064874e-20, "-18": 1.7961699064223243e-21, "-19": 5.597044470176211e-23, "-2": 0.009763114653729454, "-3": 0.0018546101226416649, "-4": 0.00027684673297185717, "-5": 3.389784709788816e-05, "-6": 3.51064263931231e-06, "-7": 3.146310599052034e-07, "-8": 2.4833590800380316e-08, "-9": 1.7503330639808382e-09, "0": 0.09909493049879688, "1": 0.21669270477100822, "10": 0.00024795826281873346, "11": 6.008584338135019e-05, "12": 1.3373136710567455e-05, "13": 2.7517433003005347e-06, "14": 5.264295701467442e-07, "15": 9.409171110638284e-08, "16": 1.577964837620929e-08, "17": 2.4921227603684653e-09, "18": 3.706304487290232e-10, "19": 4.82439682068929e-11, "2": 0.2343865582291925, "3": 0.18598911317693664, "4": 0.11597513482243516, "5": 0.05931823020117177, "6": 0.02566216408175391, "7": 0.00960724426687378, "8": 0.003167578202545706, "9": 0.0009326079370639258} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.8046 |
| Legacy raw p draw | 0.1319 |
| Legacy raw p away | 0.0635 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.7004 |
| Legacy lambda away | 0.6465 |
| Legacy model home team | Barcelona |
| Legacy model away team | Alaves |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 94.6% |
| Market home draw odds | 1.03 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:46:54Z |
| Market reference home draw last update utc | 2026-10-30T11:46:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 13.5% |
| Market draw away odds | 7.22 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:46:54Z |
| Market reference draw away last update utc | 2026-10-30T11:46:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 91.9% |
| Market home away odds | 1.06 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:46:54Z |
| Market reference home away last update utc | 2026-10-30T11:46:54Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 7.22 |
| Market reference dc home draw odds | 1.03 |
| Market reference dc home away odds | 1.06 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.39, "price": 1.44, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.44, "price": 2.39, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.88, "price": 1.83, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.83, "price": 1.88, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.52, "price": 2.22, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.22, "price": 1.52, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 94.3% |
| Market reference over 1 5 odds | 1.05 |
| Market reference over 1 5 opposite odds | 11.00 |
| Market reference over 1 5 last update utc | 2026-10-30T11:46:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 38.0% |
| Market under 3 5 odds | 2.43 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:46:34Z |
| Market reference under 3 5 odds | 2.43 |
| Market reference under 3 5 opposite odds | 1.55 |
| Market reference under 3 5 last update utc | 2026-10-30T11:46:34Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 49.6% |
| Market btts yes odds | 1.93 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:46:54Z |
| Market reference btts yes odds | 2.00 |
| Market reference btts yes opposite odds | 1.97 |
| Market reference btts yes last update utc | 2026-10-30T11:46:59Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 10.265784456508303, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,725.4846 |
| Elo away rating | 1,438.3571 |
| Elo rating diff | 347.1275 |
| Elo home expectancy | 0.8806 |

</details>


---

## 2026-10-31 — Levante vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **60.6%**. Expected goals are 1.22 for Levante and 1.87 for Atlético Madrid (3.09 combined). The most likely exact score is 1-2 at 11.2%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 62.2%; Under 3.5 goals: 60.7%; Double Chance 1X: 39.4%; Double Chance X2: 80.8%; Double Chance 12 (either team wins): 79.8%; Under 4.5 goals: 78.2%; BTTS Yes (both teams score): 60.0%; BTTS No (at least one team does not score): 40.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 19.2% | 5.20 |
| Draw | 20.2% | 4.96 |
| Atlético Madrid win | 60.6% | 1.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.22 |
| Atlético Madrid expected goals | 1.87 |
| Expected total goals | 3.09 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 62.2% |
| Under 2.5 | 37.8% |
| Over 3.5 | 39.3% |
| Under 3.5 | 60.7% |
| Over 4.5 | 21.8% |
| Under 4.5 | 78.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.17% |
| 2 | 1-1 | 9.21% |
| 3 | 0-1 | 9.02% |
| 4 | 0-2 | 8.97% |
| 5 | 1-3 | 7.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 19.2% | 17.0% | 5.47 | +5.3% |
| Draw | 20.2% | 18.8% | 4.95 | -0.1% |
| Atlético Madrid win | 60.6% | 64.2% | 1.53 | -7.3% |

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
| Market best home last update utc | 2026-10-30T11:46:34Z |
| Market best draw last update utc | 2026-10-30T11:46:34Z |
| Market best away last update utc | 2026-10-30T11:46:34Z |
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
| Bbs statistics cutoff utc | 2026-10-30T11:46:35.127291+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.0% |
| P btts no | 40.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.73 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.89 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.65 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.58 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.25602686082293585, "-10": 1.0695427751421579e-05, "-11": 1.8216775643756252e-06, "-12": 2.8517280534261547e-07, "-13": 4.129381948827197e-08, "-14": 5.55925213070533e-09, "-15": 6.936032515032247e-10, "-16": 7.197278225117184e-11, "-2": 0.1854248494527508, "-3": 0.10002307776063359, "-4": 0.04293657405928593, "-5": 0.015230170464193627, "-6": 0.0045906705576450706, "-7": 0.0012011150588427646, "-8": 0.00027736079434529076, "-9": 5.728207321270194e-05, "0": 0.20174318525550616, "1": 0.11283777703130007, "10": 1.0313497448304135e-07, "11": 1.1477726652897198e-08, "12": 1.1740025408354061e-09, "13": 1.1107659156112023e-10, "14": 9.770806707187221e-12, "15": 7.965292562695715e-13, "16": 5.400518572602966e-14, "2": 0.05382242423279307, "3": 0.0189702080868968, "4": 0.005320786471143766, "5": 0.0012331893540656, "6": 0.00024287213522452165, "7": 4.1520515450028054e-05, "8": 6.26469248688785e-06, "9": 8.453761169389014e-07} |
| Raw goal margin distribution | {"-1": 0.22343680335849858, "-10": 8.036362950195864e-06, "-11": 1.3431538740602385e-06, "-12": 2.0630648459539304e-07, "-13": 2.930945511305206e-08, "-14": 3.871236782387944e-09, "-15": 4.741141239048959e-10, "-16": 4.848481246736597e-11, "-2": 0.16006155303169164, "-3": 0.08511889955945974, "-4": 0.03595950412391209, "-5": 0.012540280679658749, "-6": 0.0037137510791850513, "-7": 0.0009542601071943434, "-8": 0.00021634204445889851, "-9": 4.385639207923661e-05, "0": 0.23265278285966096, "1": 0.14482030951206049, "10": 1.1397908117997508e-07, "11": 1.2447093126044531e-08, "12": 1.2491989472094686e-09, "13": 1.1595861944614505e-10, "14": 1.0007407579796604e-11, "15": 8.008133538232335e-13, "16": 5.350947554382546e-14, "2": 0.06833452000453344, "3": 0.023744098376919095, "4": 0.006554203745073811, "5": 0.001493447848448505, "6": 0.000288982907563069, "7": 4.851797817222671e-05, "8": 7.1870955161235275e-06, "9": 9.519671206615948e-07} |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 52.2% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 60.0% |
| P home draw | 39.4% |
| P draw away | 80.8% |
| P home away | 79.8% |
| Raw p home draw | 47.8% |
| Raw p draw away | 75.5% |
| Raw p home away | 76.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0197 |
| Totals anchor target over 2 5 | 0.6224 |
| Totals anchor reference over odds | 1.55 |
| Totals anchor reference under odds | 2.46 |
| Totals anchor reference last update utc | 2026-10-30T11:46:34Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6104 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.51, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.62, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.4, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.23, "price": 4.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.47 |
| Reference draw odds | 4.95 |
| Reference away odds | 1.53 |
| Market reference 1x2 last update utc | 2026-10-30T11:46:34Z |
| Market reference home last update utc | 2026-10-30T11:46:34Z |
| Market reference draw last update utc | 2026-10-30T11:46:34Z |
| Market reference away last update utc | 2026-10-30T11:46:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-10-30T11:45:53Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:45:53Z |
| Home probability edge | +2.3% |
| Draw probability edge | +1.3% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | 0.0755 |
| Raw ev home | 0.3417 |
| Raw edge prob draw | 0.0442 |
| Raw ev draw | 0.1516 |
| Raw edge prob away | -0.1196 |
| Raw ev away | -0.2013 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.03617917483021656, 0.07848506068897992, 0.08460994305888224, 0.05918686491292007, 0.03105206833476735, 0.013033039668996924, 0.004558475815051798, 0.0013666169509509664, 0.00035849409333317534, 8.359199367157192e-05, 1.754243481926655e-05, 3.346743084220777e-06, 5.852835484305126e-07, 9.448179874066886e-08, 1.4162675525116034e-08, 1.9814322827926015e-09, 2.5988693072573414e-10, 3.2081946258462256e-11], [0.03781006689028611, 0.08948111648978532, 0.10304127112225822, 0.07208006026105505, 0.03781641349129542, 0.015872141329130448, 0.005551488694846719, 0.0016643191411346721, 0.0004365880147344454, 0.0001018015728667756, 2.1363857686308045e-05, 4.07579356574846e-06, 7.127810115089625e-07, 1.1506359995279387e-07, 1.7247855699234542e-08, 2.4130651041750592e-09, 3.1650038662011223e-10, 3.907063878115792e-11], [0.02413228446966851, 0.05064348973568373, 0.0559472522017893, 0.043890946875471196, 0.02302714772373866, 0.009664854737270972, 0.003380409152029331, 0.0010134362088878544, 0.0002658469109456387, 6.198895242807134e-05, 1.3008867353451741e-05, 2.4818297629297024e-06, 4.3402618417187437e-07, 7.006445797267462e-08, 1.0502553902829042e-08, 1.4693621496821234e-09, 1.927232247711512e-10, 2.379086983173709e-11], [0.009796410748510058, 0.020558535509237922, 0.021571848768635896, 0.015887342016603457, 0.00934778461408801, 0.00392341168321601, 0.0013722644697365778, 0.00041140064390325973, 0.00010791956058364104, 2.5164183714911195e-05, 5.28090111516271e-06, 1.0074895228462668e-06, 1.7619130841509432e-07, 2.8442405029442658e-08, 4.263472530741884e-09, 5.964820767255577e-10, 7.823527329161968e-11, 9.657814751395327e-12], [0.0029826122659713235, 0.006259245529245081, 0.006567758579007868, 0.004594318655029549, 0.00253773491745783, 0.0011945207394039733, 0.0004177992271521942, 0.00012525491613558421, 3.285715691167384e-05, 7.661479794797815e-06, 1.6078215630006635e-06, 3.067399566862686e-07, 5.364315269409483e-08, 8.659566068872969e-09, 1.2980555626208883e-09, 1.8160475342913496e-10, 2.3819487743170957e-11, 2.9404153704326393e-12], [0.0007264681857465469, 0.0015245504069205682, 0.0015996942390898888, 0.0011190278991808189, 0.0005870919307011422, 0.00025943062363199354, 0.00010176242149152422, 3.0508059233512396e-05, 8.002944077828321e-06, 1.8660894646485402e-06, 3.916134950571211e-07, 7.471196386208063e-08, 1.3065742490237161e-08, 2.1091911017665573e-09, 3.161644845138167e-10, 4.423306282610223e-11, 5.801659251393922e-12, 7.161903824611972e-13], [0.00014745352335463814, 0.00030944277181411804, 0.0003246949508208965, 0.00022713259810102404, 0.0001191638882658007, 5.001495121473793e-05, 1.8417629485878428e-05, 6.192316350468326e-06, 1.6243826290524248e-06, 3.7876602424734e-07, 7.948701783830476e-08, 1.5164521343611432e-08, 2.6519946822585693e-09, 4.2810912505979385e-10, 6.417289582097406e-11, 8.978123323835923e-12, 1.1775809522091412e-12, 1.453674054261382e-13], [2.5653517319967517e-05, 5.3835916061361006e-05, 5.648944396232947e-05, 3.95158413766758e-05, 2.0731772303528585e-05, 8.70144970465537e-06, 3.043445661330817e-06, 9.606222571920752e-07, 2.8260516914491205e-07, 6.589656552237777e-08, 1.3828910577628305e-08, 2.638277486267447e-09, 4.6138600127008756e-10, 7.448112872924516e-11, 1.1164606019324708e-11, 1.561986698919965e-12, 2.0487196688074813e-13, 2.52905808421354e-14], [3.905231078406958e-06, 8.195433394768553e-06, 8.599379547533199e-06, 6.015490582006059e-06, 3.1559945757293507e-06, 1.324620378171917e-06, 4.633032747061515e-07, 1.3889688885786578e-07, 3.8360800724498115e-08, 1.0031424245983121e-08, 2.1051729747105556e-09, 4.016245844312964e-10, 7.023672149235476e-11, 1.1338251010198932e-11, 1.6995862930226618e-12, 2.377809999540547e-13, 3.118762866619928e-14, 3.849981313041865e-15], [5.284379901953396e-07, 1.1089685257953798e-06, 1.1636286697992432e-06, 8.139886448130476e-07, 4.2705473688541066e-07, 1.7924156505957598e-07, 6.269207799004539e-08, 1.8794891088077972e-08, 4.9303189421349724e-09, 1.2103685707044161e-09, 2.84862368816185e-10, 5.434600000584044e-11, 9.50411158728928e-12, 1.534240216741262e-12, 2.299802359492671e-13, 3.2175436280102454e-14, 4.220167124668027e-15, 5.209618448963518e-16], [6.435522853516799e-08, 1.3505448934413007e-07, 1.41711213736397e-07, 9.913069505584034e-08, 5.2008382628068314e-08, 2.1828733165354328e-08, 7.634884473204794e-09, 2.288914751983926e-09, 6.004333680761208e-10, 1.4000627412785033e-10, 3.093375424697291e-11, 6.618466717457718e-12, 1.1574475805527238e-12, 1.868457257203087e-13, 2.8007885348318526e-14, 3.918449455648146e-15, 5.139483246922107e-16, 6.344475455675355e-17], [7.1249358171149206e-09, 1.4952236054360642e-08, 1.5689219437477786e-08, 1.0975018749143038e-08, 5.757984185767355e-09, 2.416716190932122e-09, 8.452780462576507e-10, 2.534117440018258e-10, 6.647554996496808e-11, 1.5500461110307617e-11, 3.2528932108556818e-12, 6.533746096418052e-13, 1.2814405155296027e-13, 2.0686179410146393e-14, 3.1008263045920664e-15, 4.338217967611644e-16, 5.690056441559618e-17, 7.024134859570169e-18], [7.230852709878968e-10, 1.5174510952465439e-09, 1.5922450081986784e-09, 1.113816967622144e-09, 5.843580436624245e-10, 2.4526422787182353e-10, 8.57843664598551e-11, 2.5717887751762786e-11, 6.7463753069922045e-12, 1.5730885737189177e-12, 3.301249624194801e-13, 6.298119082606529e-14, 1.1596174834137107e-14, 2.099369317623805e-15, 3.1469221425916863e-16, 4.40270845272715e-17, 5.774642901481736e-18, 7.128553279297432e-19], [6.773856117643626e-11, 1.4215467797756975e-10, 1.491613648116292e-10, 1.0434227030727083e-10, 5.474260737670635e-11, 2.297633013792229e-11, 8.036271500156148e-12, 2.4092493412587625e-12, 6.31999813559388e-13, 1.4736679180482903e-13, 3.0926075886138436e-14, 5.900072119997089e-15, 1.03181363477497e-15, 1.7536504980900556e-16, 2.948033746866306e-17, 4.124453198439759e-18, 5.409680118634879e-19, 6.678022105877703e-20], [5.892474838291887e-12, 1.2365820126390584e-11, 1.297532120158981e-11, 9.076576054729106e-12, 4.761976501236109e-12, 1.998676158198219e-12, 6.990630858693946e-13, 2.0957695108937413e-13, 5.4976706539484545e-14, 1.2819214013831496e-14, 2.6902124999603277e-15, 5.132383373280762e-16, 8.975590527944352e-17, 1.4489215357478546e-17, 2.2866619467680548e-18, 3.587799367367279e-19, 4.7057987988904196e-20, 5.809110282981593e-21], [4.784056305462623e-13, 1.0039716990123708e-12, 1.0534566360212552e-12, 7.369204298414159e-13, 3.866213150229994e-13, 1.6227102430831554e-13, 5.675640975395494e-14, 1.70153961086645e-14, 4.463517737311734e-15, 1.0407824100564705e-15, 2.1841634333054488e-16, 4.16694372276912e-17, 7.28721490356167e-18, 1.1763685716856593e-18, 1.7633582976608615e-19, 2.5973737043332147e-20, 3.8206028933330464e-21, 4.716373245724704e-22], [3.6413808547024363e-14, 7.641723027532803e-14, 8.018377252974412e-14, 5.609064303025867e-14, 2.942765228195803e-14, 1.2351246796877193e-14, 4.32000985489473e-15, 1.295125593620656e-15, 3.3974031649069326e-16, 7.921907477475236e-17, 1.6624743526739282e-17, 3.1716660770460304e-18, 5.546658136868585e-19, 8.953920525806981e-20, 1.3421788405272573e-20, 1.8777783048023774e-21, 2.5930414981800516e-22, 3.589863944745518e-23], [2.60859698423022e-15, 5.474345156234326e-15, 5.74417111396564e-15, 4.018197713741296e-15, 2.1081256825019558e-15, 8.848133834781173e-16, 3.09475035130433e-16, 9.277965839127519e-17, 2.43381728081136e-17, 5.6750625050401176e-18, 1.190956331070094e-18, 2.2721047025012886e-19, 3.973491448911837e-20, 6.414371638850681e-21, 9.615043895163024e-22, 1.3451948638206092e-22, 1.7643730114946998e-23, 2.2931191299465214e-24]] |
| Legacy trial inputs | {"lambda_home": 1.217838795264868, "lambda_away": 2.0985783504805244, "rho": -0.021898200937208512, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1919 |
| Legacy p draw | 0.2003 |
| Legacy p away | 0.6078 |
| Legacy p over 1 5 | 0.8475 |
| Legacy p under 3 5 | 0.5734 |
| Legacy p btts yes | 0.6154 |
| Legacy p over 2 5 | 0.6493 |
| Legacy goal margin distribution | {"-1": 0.23606783170624782, "-10": 2.2082040465713306e-05, "-11": 4.1340395780132424e-06, "-12": 7.114707200409867e-07, "-13": 1.1328019227824757e-07, "-14": 1.677812166881364e-08, "-15": 2.3217235392444505e-09, "-16": 2.9895756950689205e-10, "-17": 3.2081946258462256e-11, "-2": 0.18409056245316965, "-3": 0.10817404847768995, "-4": 0.05075082490330144, "-5": 0.019713952864084536, "-6": 0.006515491312581978, "-7": 0.0018707950644436182, "-8": 0.00047436784118663587, "-9": 0.00010762285734662342, "0": 0.20031146893399573, "1": 0.11526001834774349, "10": 8.100898052834963e-08, "11": 8.801024135264678e-09, "12": 8.789825030625631e-10, "13": 8.121603670756085e-11, "14": 6.980648507547742e-12, "15": 5.60567031935556e-13, "16": 4.188815370325869e-14, "17": 2.60859698423022e-15, "2": 0.052505954509501324, "3": 0.017904604556700583, "4": 0.004874716596422945, "5": 0.0010988656472160259, "6": 0.00021075732095681449, "7": 3.5117721578397175e-05, "8": 5.167493887485576e-06, "9": 6.803523153039781e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2140 |
| Legacy raw p draw | 0.2121 |
| Legacy raw p away | 0.5739 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2178 |
| Legacy lambda away | 2.0986 |
| Legacy model home team | Levante |
| Legacy model away team | Ath Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 36.7% |
| Market home draw odds | 2.65 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:46:54Z |
| Market reference home draw last update utc | 2026-10-30T11:46:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.0% |
| Market draw away odds | 1.17 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:46:54Z |
| Market reference draw away last update utc | 2026-10-30T11:46:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.3% |
| Market home away odds | 1.21 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:46:54Z |
| Market reference home away last update utc | 2026-10-30T11:46:54Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.17 |
| Market reference dc home draw odds | 2.65 |
| Market reference dc home away odds | 1.21 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.3, "price": 1.61, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.3, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.77, "price": 2.04, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.04, "price": 1.77, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 83.8% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-30T11:46:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.2% |
| Market under 3 5 odds | 1.60 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:46:34Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.35 |
| Market reference under 3 5 last update utc | 2026-10-30T11:46:34Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.1% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:46:54Z |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.36 |
| Market reference btts yes last update utc | 2026-10-30T11:46:59Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 9.763905865240275, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,476.0819 |
| Elo away rating | 1,586.5836 |
| Elo rating diff | -50.5017 |
| Elo home expectancy | 0.4278 |

</details>


---

## 2026-10-31 — Rayo Vallecano vs Celta Vigo

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **39.3%**. Expected goals are 1.17 for Rayo Vallecano and 1.10 for Celta Vigo (2.27 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 43.2%; Under 3.5 goals: 77.5%; Double Chance 1X: 68.9%; Double Chance X2: 60.7%; Double Chance 12 (either team wins): 70.4%; Under 4.5 goals: 90.3%; BTTS Yes (both teams score): 49.9%; BTTS No (at least one team does not score): 50.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 39.3% | 2.55 |
| Draw | 29.6% | 3.38 |
| Celta Vigo win | 31.1% | 3.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.17 |
| Celta Vigo expected goals | 1.10 |
| Expected total goals | 2.27 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 43.2% |
| Under 2.5 | 56.8% |
| Over 3.5 | 22.5% |
| Under 3.5 | 77.5% |
| Over 4.5 | 9.7% |
| Under 4.5 | 90.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.02% |
| 2 | 1-0 | 11.12% |
| 3 | 0-0 | 9.72% |
| 4 | 0-1 | 9.16% |
| 5 | 2-1 | 8.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 39.3% | 40.2% | 2.42 | -4.9% |
| Draw | 29.6% | 29.7% | 3.25 | -3.9% |
| Celta Vigo win | 31.1% | 30.1% | 3.20 | -0.4% |

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
| Market best home last update utc | 2026-10-30T11:46:34Z |
| Market best draw last update utc | 2026-10-30T11:46:34Z |
| Market best away last update utc | 2026-10-30T11:46:34Z |
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
| Bbs statistics cutoff utc | 2026-10-30T11:46:35.127291+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 49.9% |
| P btts no | 50.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.29 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.32 |
| Fair Under 2.5 odds | 1.76 |
| Fair Over 3.5 odds | 4.44 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.27 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.1807671490151015, "-10": 1.236649306673899e-07, "-11": 1.301331179829541e-08, "-12": 1.257159216089061e-09, "-13": 1.117601894374794e-10, "-14": 8.45798461964306e-12, "-2": 0.08864329740243934, "-3": 0.031040589013160935, "-4": 0.008488298451942301, "-5": 0.0018971978012816517, "-6": 0.000357877156304036, "-7": 5.833521814578362e-05, "-8": 8.366040077490698e-06, "-9": 1.0706404066475546e-06, "0": 0.29583725811869976, "1": 0.2191126571509749, "10": 2.716254327664569e-07, "11": 3.053967676954705e-08, "12": 3.1522424396039124e-09, "13": 2.994119882648226e-10, "14": 2.4210383827711945e-11, "2": 0.11464310876277042, "3": 0.042892833115863775, "4": 0.012532223974575565, "5": 0.0029927665915811925, "6": 0.0006031800097534717, "7": 0.0001050501111196871, "8": 1.609675590242862e-05, "9": 2.200973304988965e-06} |
| Raw goal margin distribution | {"-1": 0.199368898972097, "-10": 8.210252006603516e-08, "-11": 8.124412068532826e-09, "-12": 7.351032114724027e-10, "-13": 5.654190362914904e-11, "-2": 0.09365746281666024, "-3": 0.03116002055194032, "-4": 0.00806331391559384, "-5": 0.0017015825080795412, "-6": 0.0003026389597901375, "-7": 4.6471089541846474e-05, "-8": 6.274311095438022e-06, "-9": 7.556017510574192e-07, "0": 0.2940437690391492, "1": 0.21331142964607103, "10": 1.5917826418102436e-07, "11": 1.6829528434120288e-08, "12": 1.626975646761967e-09, "13": 1.3370753611266838e-10, "2": 0.1069172657828722, "3": 0.03800632856380542, "4": 0.010508106809876891, "5": 0.002369281431960414, "6": 0.00045023702039844696, "7": 7.386725300768136e-05, "8": 1.0655844389459096e-05, "9": 1.371094866677059e-06} |
| Unadjusted home-win probability | 37.2% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 66.7% |
| Raw p under 3 5 | 80.5% |
| Raw p btts yes | 46.5% |
| P home draw | 68.9% |
| P draw away | 60.7% |
| P home away | 70.4% |
| Raw p home draw | 66.6% |
| Raw p draw away | 62.8% |
| Raw p home away | 70.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0646 |
| Totals anchor target over 2 5 | 0.4317 |
| Totals anchor reference over odds | 2.22 |
| Totals anchor reference under odds | 1.71 |
| Totals anchor reference last update utc | 2026-10-30T11:46:34Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3965 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:33:57Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.45, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:33:57Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.59, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:33:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.71, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:33:57Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.72, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:33:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.27, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.74, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:33:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:33:57Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:33:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:33:57Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:33:57Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.53, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.01, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.07, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.23, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.69, "price": 2.23, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.42 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-30T11:46:34Z |
| Market reference home last update utc | 2026-10-30T11:46:34Z |
| Market reference draw last update utc | 2026-10-30T11:46:34Z |
| Market reference away last update utc | 2026-10-30T11:46:34Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.26 |
| Reference Under 2.5 odds | 1.76 |
| Market reference over 2 5 last update utc | 2026-10-30T11:46:37Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:46:37Z |
| Home probability edge | -0.9% |
| Draw probability edge | -0.1% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.0304 |
| Raw ev home | -0.1006 |
| Raw edge prob draw | -0.0026 |
| Raw ev draw | -0.0444 |
| Raw edge prob away | 0.0329 |
| Raw ev away | 0.0698 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.1060714574591801, 0.10329144093535506, 0.05704483570234732, 0.02044729525850385, 0.0054968851900545086, 0.0011821904622842134, 0.00021187367039009457, 3.254765766483569e-05, 4.374924290155001e-06, 5.227196443698342e-07, 5.620948561384128e-08, 5.494873706990317e-09, 4.923991090152171e-10, 4.073002676051478e-11, 3.128437255181474e-12], [0.12245027120977472, 0.13688790525073358, 0.068899153494461, 0.02469638692471949, 0.006639176566782729, 0.0014278579492386235, 0.0002559025082272484, 3.931128968511358e-05, 5.28406430630901e-06, 6.313444603456946e-07, 6.789021178639994e-08, 6.636747083400319e-09, 5.947231046399401e-10, 4.9194012587729115e-11, 3.7785485046750554e-12], [0.07573145365288594, 0.0814361216469876, 0.0434946453086268, 0.014914234851717098, 0.004009422060030311, 0.0008622884333141319, 0.00015454042400933106, 2.374022598831336e-05, 3.1910650038037216e-06, 3.812711382692768e-07, 4.099913747713854e-08, 4.007954886477998e-09, 3.5915537286404637e-10, 2.9708437079002103e-11, 2.2818787205233398e-12], [0.030489660663966356, 0.03278637336326262, 0.01762804594912501, 0.0062767036751005005, 0.0016142027146244624, 0.0003471593434177952, 6.221833676277815e-05, 9.557870601391344e-06, 1.2847302465443478e-06, 1.535006535075463e-07, 1.6506348800893826e-08, 1.6136120271150138e-09, 1.4459679454268323e-10, 1.1960686368801165e-11, 9.186897188580648e-13], [0.009206406610766197, 0.009899903045864964, 0.005322819448519326, 0.0019079248722790655, 0.0005095068006492836, 0.00010482537373753333, 1.8786936109153883e-05, 2.8860158221928266e-06, 3.879265553393179e-07, 4.6349792042092404e-08, 4.984121023680582e-09, 4.872329868597156e-10, 4.3661256182710965e-11, 3.6115502651418324e-12, 2.7739997483584847e-13], [0.002223912522133883, 0.0023914344958285696, 0.0012857877481510383, 0.0004608810140744999, 0.0001238995176924341, 2.6469657282072672e-05, 4.538198694897682e-06, 6.971500388159576e-07, 9.370808400733598e-08, 1.1196320918540457e-08, 1.203971280546289e-09, 1.1769668519820422e-10, 1.054687441713433e-11, 8.724111587220488e-13, 6.700912785620767e-14], [0.0004476761957917585, 0.0004813985653313682, 0.0002588305798717273, 9.277588800819697e-05, 2.494111804710787e-05, 5.363974479100083e-06, 9.549577537771262e-07, 1.4033711945366524e-07, 1.8863547080118997e-08, 2.2538325162477453e-09, 2.423608291032621e-10, 2.3692480600035134e-11, 2.123098174754497e-12, 1.7561738819124945e-13, 1.3489015931798712e-14], [7.724377938838808e-05, 8.306236723750164e-05, 4.465962764721188e-05, 1.600790994301711e-05, 4.303436810445688e-06, 9.255208679920128e-07, 1.658730209556966e-07, 2.5311997627548133e-08, 3.254789249095938e-09, 3.888849648472227e-10, 4.1817873256650476e-11, 4.087992084091216e-12, 3.663275567747862e-13, 3.0301702252044364e-14, 2.3274468926352803e-15], [1.1661947455556079e-05, 1.25404138679867e-05, 6.742526519679567e-06, 2.416808267369722e-06, 6.497151532343057e-07, 1.3973132615991674e-07, 2.5042825066253576e-08, 3.847034394203301e-09, 5.136706939191219e-10, 5.871224922204994e-11, 6.313490153945956e-12, 6.171881963943325e-13, 5.53066247205404e-14, 4.574826119012623e-15, 3.5138833939021637e-16], [1.5650424557219245e-06, 1.6829333342925214e-06, 9.04852324394763e-07, 3.2433755684358826e-07, 8.719228094730585e-08, 1.8752053091305038e-08, 3.3607666806311474e-09, 5.162750199738017e-10, 6.939559671367355e-11, 8.236412933223757e-12, 8.472753090651458e-13, 8.282713793804459e-14, 7.422192228201745e-15, 6.139452377989568e-16, 4.7156589556515923e-17], [1.8902692777445563e-07, 2.0326587094648088e-07, 1.0928869970560576e-07, 3.9173718072546407e-08, 1.0531144974922574e-08, 2.264886152035919e-09, 4.059157617634216e-10, 6.235605977048533e-11, 8.381648944986547e-12, 1.0014464857404284e-12, 1.0697356114689637e-13, 1.0003919934272682e-14, 8.964575939259379e-16, 7.415273732581379e-17, 5.6956060301107854e-18], [2.0755277447303414e-08, 2.231872250548262e-08, 1.1999969057061539e-08, 4.301299274187424e-09, 1.156326447061003e-09, 2.486859466295227e-10, 4.456980999916476e-11, 6.8467352048449956e-12, 9.203104095659035e-13, 1.099594640027706e-13, 1.1824244557368158e-14, 1.1482314161511757e-15, 9.8431616599491e-17, 8.142017937839327e-18, 6.253811812808749e-19], [2.0890308314141314e-09, 2.2463924922279095e-09, 1.207803913961847e-09, 4.329282912131913e-10, 1.1638493415581095e-10, 2.5030386183345322e-11, 4.485977480904349e-12, 6.891279084928848e-13, 9.262978174759708e-14, 1.1067484455015294e-14, 1.1901171401460631e-15, 1.163423452502968e-16, 1.0356315556895273e-17, 8.194988742144283e-19, 6.294498218098619e-20], [1.9408816313065768e-10, 2.0870835697138764e-10, 1.1221492739970103e-10, 4.022260253190361e-11, 1.0813118574747278e-11, 2.325528950421418e-12, 4.1678424081698814e-13, 6.402565625654998e-14, 8.606069340975083e-15, 1.0282604239483299e-15, 1.1057168049784025e-16, 1.0809161714792562e-17, 9.686158192852225e-19, 7.958970813913731e-20, 5.8481070676824806e-21], [1.6744360539705463e-11, 1.8005672888077598e-11, 9.680998428804596e-12, 3.4700815741456163e-12, 9.328686152399102e-13, 2.0062787221684138e-13, 3.595678109854152e-14, 5.5236169731237994e-15, 7.424622169152261e-16, 8.871001193262147e-17, 9.539232346130156e-18, 9.32527249292507e-19, 8.3564356738518e-20, 6.91223526580317e-21, 5.273988549825543e-22]] |
| Legacy trial inputs | {"lambda_home": 1.2078070283867242, "lambda_away": 1.0753275913631466, "rho": -0.021898200937208512, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3949 |
| Legacy p draw | 0.2933 |
| Legacy p away | 0.3118 |
| Legacy p over 1 5 | 0.6682 |
| Legacy p under 3 5 | 0.8027 |
| Legacy p btts yes | 0.4656 |
| Legacy p over 2 5 | 0.3985 |
| Legacy goal margin distribution | {"-1": 0.18882853922006837, "-10": 6.321762615644929e-08, "-11": 6.120223938428118e-09, "-12": 5.438750003234695e-10, "-13": 4.4508575265189834e-11, "-14": 3.128437255181474e-12, "-2": 0.08611730737549217, "-3": 0.028013960615544762, "-4": 0.007089240803284861, "-5": 0.0014631655045730723, "-6": 0.00025453462970397955, "-7": 3.822999741602098e-05, "-8": 5.048926047161307e-06, "-9": 5.94766086396648e-07, "0": 0.29326766894333905, "1": 0.22355179696080227, "10": 2.1259460966504725e-07, "11": 2.311735494850517e-08, "12": 2.3074201868143237e-09, "13": 2.1209383601873528e-10, "14": 1.6744360539705463e-11, "2": 0.11432741968525038, "3": 0.041772573938181394, "4": 0.011873348476471998, "5": 0.002752477025814565, "6": 0.0005378162114874505, "7": 9.072940107798318e-05, "8": 1.345858953524828e-05, "9": 1.780752237763127e-06} |
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
| Market p home draw | 69.8% |
| Market home draw odds | 1.38 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:46:54Z |
| Market reference home draw last update utc | 2026-10-30T11:46:54Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.8% |
| Market draw away odds | 1.61 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:46:54Z |
| Market reference draw away last update utc | 2026-10-30T11:46:54Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.3% |
| Market home away odds | 1.37 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:46:54Z |
| Market reference home away last update utc | 2026-10-30T11:46:54Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.61 |
| Market reference dc home draw odds | 1.38 |
| Market reference dc home away odds | 1.37 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.39, "price": 1.55, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.55, "price": 2.39, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.88, "price": 1.94, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.94, "price": 1.88, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.53, "price": 2.44, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.44, "price": 1.53, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 70.8% |
| Market over 1 5 odds | 1.38 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T11:46:34Z |
| Market reference over 1 5 odds | 1.38 |
| Market reference over 1 5 opposite odds | 3.16 |
| Market reference over 1 5 last update utc | 2026-10-30T11:46:34Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 77.0% |
| Market reference under 3 5 odds | 1.25 |
| Market reference under 3 5 opposite odds | 3.50 |
| Market reference under 3 5 last update utc | 2026-10-30T11:46:13Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 51.3% |
| Market btts yes odds | 1.91 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:46:54Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 2.02 |
| Market reference btts yes last update utc | 2026-10-30T11:46:59Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 9.258036261887293, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.5850 |
| Elo away rating | 1,513.4884 |
| Elo rating diff | 21.0966 |
| Elo home expectancy | 0.5303 |

</details>


---

## 2026-10-31 — Real Betis vs Málaga

The model's most likely 1X2 outcome is **Real Betis win** at **75.3%**. Expected goals are 2.36 for Real Betis and 0.60 for Málaga (2.96 combined). The most likely exact score is 2-0 at 11.2%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 65.8%; Under 3.5 goals: 55.6%; Double Chance 1X: 90.8%; Double Chance X2: 24.7%; Double Chance 12 (either team wins): 84.5%; Under 4.5 goals: 74.2%; BTTS Yes (both teams score): 48.4%; BTTS No (at least one team does not score): 51.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 75.3% | 1.33 |
| Draw | 15.5% | 6.45 |
| Málaga win | 9.2% | 10.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 2.36 |
| Málaga expected goals | 0.60 |
| Expected total goals | 2.96 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 65.8% |
| Under 2.5 | 34.2% |
| Over 3.5 | 44.4% |
| Under 3.5 | 55.6% |
| Over 4.5 | 25.8% |
| Under 4.5 | 74.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.23% |
| 2 | 3-0 | 10.36% |
| 3 | 1-0 | 7.93% |
| 4 | 2-1 | 7.84% |
| 5 | 1-1 | 7.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 75.3% | 74.7% | 1.32 | -0.6% |
| Draw | 15.5% | 15.3% | 5.97 | -7.4% |
| Málaga win | 9.2% | 10.0% | 8.95 | -17.6% |

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
| Market best home last update utc | 2026-10-30T11:46:34Z |
| Market best draw last update utc | 2026-10-30T11:46:34Z |
| Market best away last update utc | 2026-10-30T11:46:34Z |
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
| Dc lambda away | 0.5959 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:46:35.127291+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.61 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.85 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.92 |
| Fair Over 3.5 odds | 2.25 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.87 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.0680775997697068, "-10": 3.932852327128978e-10, "-11": 2.4611715802997293e-11, "-12": 1.4149225327868408e-12, "-13": 7.521552652468974e-14, "-14": 3.717893346181099e-15, "-15": 1.7171631242470518e-16, "-16": 7.442158312696623e-18, "-17": 3.03758008544682e-19, "-18": 1.1667035964066412e-20, "-19": 3.8920972787434355e-22, "-2": 0.019305856605950026, "-3": 0.003915726612708737, "-4": 0.0006265710047006245, "-5": 8.242581613789144e-05, "-6": 9.18446434812309e-06, "-7": 8.864445965098126e-07, "-8": 7.539696474978275e-08, "-9": 5.729303266159452e-09, "0": 0.1550556430468512, "1": 0.1874126555631181, "10": 0.00025449351023745955, "11": 6.31448915590823e-05, "12": 1.43931632354187e-05, "13": 3.0336002106166533e-06, "14": 5.945317204432657e-07, "15": 1.0887217895251969e-07, "16": 1.870817929664319e-08, "17": 3.0275241343977714e-09, "18": 4.6104962316595427e-10, "19": 6.098149666801996e-11, "2": 0.20456912434286054, "3": 0.16450936671756336, "4": 0.10437003260764713, "5": 0.05443723264351843, "6": 0.024049933169561135, "7": 0.009203200763308035, "8": 0.003103619126975412, "9": 0.0009350689279124637} |
| Raw goal margin distribution | {"-1": 0.056061410572414906, "-10": 9.171795285637564e-11, "-11": 4.916750487437958e-12, "-12": 2.4199594478490514e-13, "-13": 1.1008386176097266e-14, "-14": 4.654724603231201e-16, "-15": 1.8384775017205148e-17, "-16": 6.811740277958627e-19, "-17": 2.3705342048958276e-20, "-18": 7.278630890562426e-22, "-2": 0.014374365598333128, "-3": 0.0025725037076434255, "-4": 0.0003590686845848376, "-5": 4.0934522938025725e-05, "-6": 3.9367802779750676e-06, "-7": 3.270724057322796e-07, "-8": 2.390306487961708e-08, "-9": 1.5586078291063295e-09, "0": 0.15982713400756984, "1": 0.2293354595247523, "10": 8.804950741718318e-05, "11": 1.871449038363433e-05, "12": 3.652037110330525e-06, "13": 6.58685355115629e-07, "14": 1.1042708301528788e-07, "15": 1.72928743757441e-08, "16": 2.540353796922389e-09, "17": 3.5051742193658665e-10, "18": 4.267173847159234e-11, "2": 0.22596605423190283, "3": 0.16033848759320146, "4": 0.08873328541660083, "5": 0.04010753972829184, "6": 0.015293423785946602, "7": 0.005037727939981976, "8": 0.0014597270389557996, "9": 0.00037738286187096105} |
| Unadjusted home-win probability | 76.7% |
| Unadjusted draw probability | 16.0% |
| Unadjusted away-win probability | 7.3% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 65.7% |
| Raw p btts yes | 40.9% |
| P home draw | 90.8% |
| P draw away | 24.7% |
| P home away | 84.5% |
| Raw p home draw | 92.7% |
| Raw p draw away | 23.3% |
| Raw p home away | 84.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1719 |
| Totals anchor target over 2 5 | 0.6579 |
| Totals anchor reference over odds | 1.48 |
| Totals anchor reference under odds | 2.73 |
| Totals anchor reference last update utc | 2026-10-30T11:46:34Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5666 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 7.45, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.11, "price": 7.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.67, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.01, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.93, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.67, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.32 |
| Reference draw odds | 5.97 |
| Reference away odds | 8.95 |
| Market reference 1x2 last update utc | 2026-10-30T11:46:34Z |
| Market reference home last update utc | 2026-10-30T11:46:34Z |
| Market reference draw last update utc | 2026-10-30T11:46:34Z |
| Market reference away last update utc | 2026-10-30T11:46:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Market reference over 2 5 last update utc | 2026-10-30T11:45:53Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:45:53Z |
| Home probability edge | +0.6% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.0198 |
| Raw ev home | 0.0121 |
| Raw edge prob draw | 0.0068 |
| Raw ev draw | -0.0458 |
| Raw edge prob away | -0.0266 |
| Raw ev away | -0.3430 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05875518617052255, 0.03706392355554911, 0.010896479458223755, 0.0020297067212080243, 0.0002835578264001462, 3.169129414516424e-05, 2.951597026215384e-06, 2.3562825348612543e-07, 1.6459086108071425e-08, 1.021954470908836e-09, 5.710838623588937e-11, 2.9011857993733623e-12, 1.3510226718266374e-13, 5.807478690054639e-15, 2.318077381061162e-16, 8.635848410780422e-18, 3.0161529974939114e-19, 9.914544959777863e-21], [0.13161876238941922, 0.07395640177806606, 0.024683965783876844, 0.004597926463284573, 0.0006423479906006878, 7.179078557667732e-05, 6.686299027334622e-06, 5.337723774972629e-07, 3.728502585474017e-08, 2.3150494881679676e-09, 1.2936852285397757e-10, 6.5721016846734035e-12, 3.0604928438094615e-13, 1.3155772543370675e-14, 5.251177040976127e-16, 1.9562922823258348e-17, 6.832538681370907e-19, 2.2459574166880423e-20], [0.15092591127559307, 0.08433971844621449, 0.02290367743331941, 0.005207877458569503, 0.0007275604878676142, 8.131439615732599e-05, 7.573289017074919e-06, 6.045814684015749e-07, 4.223117686670681e-08, 2.6221589538624666e-09, 1.4653027172130415e-10, 7.443942501548212e-12, 3.4664912152602433e-13, 1.4900988918762385e-14, 5.947786847187056e-16, 2.2158097918382568e-17, 7.738928507807556e-19, 2.5439012773860288e-20], [0.11396494449148327, 0.06368536224107282, 0.017794179525440663, 0.003221512201286084, 0.0005493847273356693, 6.140092556742273e-05, 5.71863012225176e-06, 4.5652262692752915e-07, 3.188898239372476e-08, 1.980005932043742e-09, 1.1064577408810326e-10, 5.620959892285409e-12, 2.617565635936198e-13, 1.1251814619784139e-14, 4.491204937296036e-16, 1.6731695558188023e-17, 5.843705367498896e-19, 1.9209131514847825e-20], [0.06454164395882236, 0.03606686243293984, 0.010077358477160354, 0.0018771275907539108, 0.00025488065191508374, 3.477311987819995e-05, 3.2386256223741884e-06, 2.585419663719909e-07, 1.805965296652031e-08, 1.1213346215587683e-09, 6.266190176819091e-11, 3.1833121464979686e-12, 1.4824031202513134e-13, 6.372228024338228e-15, 2.543499242705534e-16, 9.475643079216192e-18, 3.3094593509634777e-19, 1.0878686709509635e-20], [0.02924143962685786, 0.016340565806409642, 0.004565679636175562, 0.0008504573132961944, 0.00011881215383710661, 1.2906067493589791e-05, 1.4673018814189148e-06, 1.1713583412128554e-07, 8.182163011519048e-09, 5.080353803621105e-10, 2.838979773474126e-11, 1.4422413845648513e-12, 6.716222067592561e-14, 2.8870216132260086e-15, 1.1523657437976674e-16, 4.293064570889023e-18, 1.4993940326416267e-19, 4.928731918241508e-21], [0.011040181953384787, 0.006169423326145774, 0.0017237842790046737, 0.0003210923812982485, 4.4857839195797184e-05, 5.013449971450879e-06, 4.5382509012217117e-07, 4.422494030604099e-08, 3.0891970290154903e-09, 1.9181008560204885e-10, 1.071864233125701e-11, 5.445220040285863e-13, 2.535727194411313e-14, 1.0900025552809815e-15, 4.3507869826930695e-17, 1.6208577486284848e-18, 5.661001356779536e-20, 1.8608556169328576e-21], [0.0035727853285081376, 0.0019965273433063006, 0.000557845079686634, 0.00010391080091269754, 1.4516738077689506e-05, 1.622435262284571e-06, 1.5110695932614142e-07, 1.172436941623269e-08, 9.99715210196662e-10, 6.207291352555892e-11, 3.4687297930719684e-12, 1.7621631919270384e-13, 8.206032251591898e-15, 3.5274284010784e-16, 1.407986568053278e-17, 5.245363535084798e-19, 1.8319935919140968e-20, 6.022036298605875e-22], [0.00101168582866773, 0.0005653455872799484, 0.0001579619008194499, 2.94238458409664e-05, 4.110624300456412e-06, 4.5941600512267497e-07, 4.278812055779527e-08, 3.4158084682429034e-09, 2.3190311982286368e-10, 1.757684304647199e-11, 9.822209991535642e-13, 4.9898198888341563e-14, 2.323656692240293e-15, 9.988423587994363e-17, 3.9869175639746795e-18, 1.4853005335396463e-19, 5.1875547639563775e-21, 1.7052266573111456e-22], [0.0002546430857641241, 0.00014229846933575907, 3.975928565768422e-05, 7.406033264159101e-06, 1.0346512984803295e-06, 1.1563580894270578e-07, 1.0769844495333778e-08, 8.597649429151719e-10, 6.005623272582286e-11, 3.624254140947313e-12, 2.4722673683801376e-13, 1.2559463599220206e-14, 5.848684380087923e-16, 2.5141036202073857e-17, 1.0035140973701775e-18, 3.738527321725048e-20, 1.3057165725092756e-21, 4.29208520709215e-23], [5.76846975227269e-05, 3.223509539616472e-05, 9.00673332637698e-06, 1.6777003286945738e-06, 2.3438118107640005e-07, 2.6195161127738725e-08, 2.4397097616685463e-09, 1.9476390071178433e-10, 1.3604632573266052e-11, 8.447197488384929e-13, 4.5879187185785083e-14, 2.8451149835649205e-15, 1.324911643914746e-16, 5.6952383543919455e-18, 2.2732762208282423e-19, 8.468944565568206e-21, 2.9578602265831034e-22, 9.722927923604486e-24], [1.1879459077196333e-05, 6.6384242798081375e-06, 1.8548267489443154e-06, 3.4550189659352616e-07, 4.826794225565727e-08, 5.394573569791787e-09, 5.024284345524959e-10, 4.010924712414784e-11, 2.8017079547089965e-12, 1.739597175502719e-13, 9.721136334490746e-15, 4.799847245323815e-16, 2.7284937480317244e-17, 1.1728647955417035e-18, 4.681534791068803e-20, 1.7440757204989132e-21, 6.091351957582319e-23, 2.0023182809181326e-24], [2.2425604107325786e-06, 1.2531772181547134e-06, 3.5014734331927456e-07, 6.522257201264126e-08, 9.111843873248958e-09, 1.0183676749745197e-09, 9.484658427896111e-11, 7.57167553845658e-12, 5.288960802706674e-13, 3.283947300170607e-14, 1.835120214598864e-15, 9.322667050590504e-17, 4.2195097572588716e-18, 2.2140908441468714e-19, 8.837628477605638e-21, 3.2924017320103763e-22, 1.1499029256420023e-23, 3.7799025000159143e-25], [3.9077748183945145e-07, 2.183724617920517e-07, 6.101494365111963e-08, 1.1365362702477308e-08, 1.587784831419228e-09, 1.7745571254566092e-10, 1.6527496511676148e-11, 1.319402717564638e-12, 9.216281417159739e-14, 5.722444088072174e-15, 3.197789691201026e-16, 1.6245218352299784e-17, 7.565064708186473e-19, 3.160620569919139e-20, 1.5400014132877625e-21, 5.737176362703069e-23, 2.003763945406528e-24, 6.586671081348221e-26], [6.323102552668042e-08, 3.533446871324629e-08, 9.872722044659586e-09, 1.839009596401398e-09, 2.5691670547074356e-10, 2.871380059314653e-11, 2.6742855010547128e-12, 2.1349026182777008e-13, 1.4912704867393544e-14, 9.25938737576878e-16, 5.174287951329806e-17, 2.6286105624243336e-18, 1.224089979347515e-19, 5.2618483893824134e-21, 2.041330677436747e-22, 9.283225413438387e-24, 3.2422556331814436e-25, 1.065777806131844e-26], [9.549215576547634e-09, 5.336248403613082e-09, 1.4909888040959941e-09, 2.777291517431878e-10, 3.879982944007967e-11, 4.336388182890706e-12, 4.0387339205864437e-13, 3.2241522523254935e-14, 2.2521322787669206e-15, 1.3983623612220373e-16, 7.814263755936165e-18, 3.9697551507825225e-19, 1.8486334834074338e-20, 7.946498444837181e-22, 3.1718753157304244e-23, 1.148491844310614e-24, 4.8964883516655143e-26, 1.6095487844268197e-27], [1.3519992366460482e-09, 7.555179491347189e-10, 2.1109751987758284e-10, 3.932151265631984e-11, 5.4933663780527714e-12, 6.13955509337111e-13, 5.718129550933734e-14, 4.56482665935441e-15, 3.1886191041669094e-16, 1.9798326153301386e-17, 1.1063608888381737e-18, 5.620467870377767e-20, 2.6173365114339324e-21, 1.1250829709839974e-22, 4.490811806716347e-24, 1.6730230975461159e-25, 5.6791719949132826e-27, 2.2788350628862567e-28], [1.801591218475496e-10, 1.0067568573029228e-10, 2.812956011697623e-11, 5.239743483475432e-12, 7.320122939654726e-13, 8.181194368869046e-14, 7.61962855143566e-15, 6.082807889564484e-16, 4.248958151323449e-17, 2.6382034524505794e-18, 1.4742686295742478e-19, 7.489490588852438e-21, 3.487702024516114e-22, 1.4992165273771837e-23, 5.984180238797249e-25, 2.229367916155743e-26, 7.786281559129684e-28, 2.487621205130523e-29]] |
| Legacy trial inputs | {"lambda_home": 2.2653156809511947, "lambda_away": 0.5588153666484006, "rho": -0.021898200937208512, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7539 |
| Legacy p draw | 0.1591 |
| Legacy p away | 0.0870 |
| Legacy p over 1 5 | 0.7726 |
| Legacy p under 3 5 | 0.6882 |
| Legacy p btts yes | 0.3847 |
| Legacy p over 2 5 | 0.5368 |
| Legacy goal margin distribution | {"-1": 0.0675414371895732, "-10": 6.403864755690964e-11, "-11": 3.2225948206101382e-12, "-12": 1.4886988598097834e-13, "-13": 6.355349741294095e-15, "-14": 2.5216376291167017e-16, "-15": 9.344541291691373e-18, "-16": 3.2407487391627157e-19, "-17": 9.914544959777863e-21, "-2": 0.016286726248664715, "-3": 0.0027593546575469773, "-4": 0.00036339700220638054, "-5": 3.9015213900542384e-05, "-6": 3.5296447163685894e-06, "-7": 2.7564933564741564e-07, "-8": 1.8926437999224258e-08, "-9": 1.1590351819319024e-09, "0": 0.15910503008763607, "1": 0.2357537681393154, "10": 6.468489581944001e-05, "11": 1.3195529670003145e-05, "12": 2.4710888988993547e-06, "13": 4.27642992881744e-07, "14": 6.878361119365456e-08, "15": 1.0332863085799329e-08, "16": 1.4526749223763405e-09, "17": 1.801591218475496e-10, "2": 0.2255856132432465, "3": 0.154933566063423, "4": 0.08271413358561244, "5": 0.03599919323508405, "6": 0.013202317102710387, "7": 0.004179617204827655, "8": 0.0011633458252328936, "9": 0.00028879984738835855} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7608 |
| Legacy raw p draw | 0.1652 |
| Legacy raw p away | 0.0740 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2653 |
| Legacy lambda away | 0.5588 |
| Legacy model home team | Betis |
| Legacy model away team | Malaga |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 88.6% |
| Market home draw odds | 1.09 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:46:11Z |
| Market reference home draw last update utc | 2026-10-30T11:46:40Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 28.8% |
| Market draw away odds | 3.66 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:46:11Z |
| Market reference draw away last update utc | 2026-10-30T11:46:40Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.5% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:46:11Z |
| Market reference home away last update utc | 2026-10-30T11:46:40Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.32 |
| Market reference dc home draw odds | 1.08 |
| Market reference dc home away odds | 1.16 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:11Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.13, "price": 1.7, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:11Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.7, "price": 2.13, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:11Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.7, "price": 2.13, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:46:11Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.13, "price": 1.7, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 84.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-30T11:46:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.4% |
| Market under 3 5 odds | 1.69 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:46:34Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.24 |
| Market reference under 3 5 last update utc | 2026-10-30T11:46:34Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.8% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:46:11Z |
| Market reference btts yes odds | 1.88 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-30T11:46:59Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 10.07970162881688, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,565.5196 |
| Elo away rating | 1,404.7246 |
| Elo rating diff | 220.7950 |
| Elo home expectancy | 0.7809 |

</details>


---

## 2026-11-01 — Athletic Bilbao vs Real Sociedad

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **46.1%**. Expected goals are 1.55 for Athletic Bilbao and 1.04 for Real Sociedad (2.59 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 47.7%; Under 3.5 goals: 74.1%; Double Chance 1X: 72.2%; Double Chance X2: 53.9%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 46.1% | 2.17 |
| Draw | 26.1% | 3.83 |
| Real Sociedad win | 27.8% | 3.59 |

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
| 1 | 1-1 | 12.44% |
| 2 | 1-0 | 10.66% |
| 3 | 2-1 | 8.87% |
| 4 | 2-0 | 8.53% |
| 5 | 0-1 | 8.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 46.1% | 45.0% | 2.17 | -0.1% |
| Draw | 26.1% | 26.1% | 3.68 | -3.9% |
| Real Sociedad win | 27.8% | 29.0% | 3.32 | -7.6% |

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
| Market best home last update utc | 2026-10-30T11:46:34Z |
| Market best draw last update utc | 2026-10-30T11:46:34Z |
| Market best away last update utc | 2026-10-30T11:46:34Z |
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
| Bbs statistics cutoff utc | 2026-10-30T11:46:35.127291+00:00 |
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
| Fair Under 0.5 odds | 12.68 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.73 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.34 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.17360216941450723, "-10": 3.917978080866701e-08, "-11": 3.6581266378147203e-09, "-12": 3.1365666763790065e-10, "-13": 2.4856197233219946e-11, "-14": 1.822713943024662e-12, "-15": 1.1408339549392854e-13, "-2": 0.07470356897575872, "-3": 0.023019204011014302, "-4": 0.005557109828035865, "-5": 0.0010985080669110726, "-6": 0.00018347430790967612, "-7": 2.6499800047477914e-05, "-8": 3.3691653555904083e-06, "-9": 3.823791838330427e-07, "0": 0.26123225922337157, "1": 0.22244900419306943, "10": 1.7730791738551754e-06, "11": 2.462184659616183e-07, "12": 3.1398736188044104e-08, "13": 3.700735862347204e-09, "14": 4.0361535185697727e-10, "15": 3.757226338644962e-11, "2": 0.14120218241347735, "3": 0.06471219317958626, "4": 0.023234886510486816, "5": 0.006831099080540672, "6": 0.0016969082093420572, "7": 0.00036452007260516007, "8": 6.892819976212005e-05, "9": 1.1634952378248478e-05} |
| Raw goal margin distribution | {"-1": 0.1566412500211876, "-10": 3.535191905794742e-08, "-11": 3.300727929931142e-09, "-12": 2.8301243389977594e-10, "-13": 2.2427748561645522e-11, "-14": 1.6446349226472952e-12, "-15": 1.0293745600702815e-13, "-2": 0.06740503569092492, "-3": 0.020770229444360258, "-4": 0.005014180599841184, "-5": 0.0009911839082405467, "-6": 0.0001655488812995345, "-7": 2.3910771499849635e-05, "-8": 3.0399981440765258e-06, "-9": 3.4502076523407774e-07, "0": 0.2626437546250012, "1": 0.23489453722211903, "10": 1.8722790578977319e-06, "11": 2.5999384815136116e-07, "12": 3.315542648978874e-08, "13": 3.907783902745065e-09, "14": 4.2619674398677847e-10, "15": 3.967434897073194e-11, "2": 0.14910213427604252, "3": 0.0683326982050876, "4": 0.024534827360037675, "5": 0.007213284065094666, "6": 0.001791846495279729, "7": 0.00038491416975931764, "8": 7.278458109268264e-05, "9": 1.228590239998574e-05} |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 25.1% |
| Raw p over 1 5 | 73.4% |
| Raw p under 3 5 | 73.9% |
| Raw p btts yes | 51.3% |
| P home draw | 72.2% |
| P draw away | 53.9% |
| P home away | 73.9% |
| Raw p home draw | 74.9% |
| Raw p draw away | 51.4% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4773 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.6, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.57, "price": 1.6, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.17 |
| Reference draw odds | 3.68 |
| Reference away odds | 3.32 |
| Market reference 1x2 last update utc | 2026-10-30T11:46:34Z |
| Market reference home last update utc | 2026-10-30T11:46:34Z |
| Market reference draw last update utc | 2026-10-30T11:46:34Z |
| Market reference away last update utc | 2026-10-30T11:46:34Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-30T11:46:35Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:46:35Z |
| Home probability edge | +1.1% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | 0.0368 |
| Raw ev home | 0.0554 |
| Raw edge prob draw | 0.0020 |
| Raw ev draw | -0.0335 |
| Raw edge prob away | -0.0388 |
| Raw ev away | -0.1666 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10593067429476331, 0.10153067550271586, 0.046675324583731005, 0.013887360292009729, 0.0030989411043213845, 0.0005532187984539061, 8.229989660446822e-05, 1.0494333474312646e-05, 1.1708964368381383e-06, 1.161260318167444e-07, 1.0365331516190205e-08, 8.410932013001077e-10, 6.256284466035519e-11, 4.295628805221457e-12, 2.73874956250003e-13], [0.13859447095211597, 0.12553380122689117, 0.06222088561772319, 0.018512648041925574, 0.0041310662905438035, 0.0007374723986852077, 0.00010971048404368121, 1.3989548622593758e-05, 1.560872129255621e-06, 1.5480266302054212e-07, 1.3817581611065007e-08, 1.121225494169993e-09, 8.339986140960178e-11, 5.726319654540605e-12, 3.650910299685424e-13], [0.09421880920076835, 0.08409907556023255, 0.03654226866226363, 0.012339210991789345, 0.0027534741904371297, 0.0004915465095749349, 7.312518487687477e-05, 9.324435474770985e-06, 1.0403660508464624e-06, 1.0318041572310117e-07, 9.20981452837395e-09, 7.473289564304699e-10, 5.558840011912346e-11, 3.8167563205321635e-12, 2.433436448307778e-13], [0.04186635945653721, 0.03736963093923784, 0.016677940650471193, 0.004831204813472751, 0.001223513024511868, 0.0002184198997422971, 3.249335564045753e-05, 4.143335822512876e-06, 4.6228921189507945e-07, 4.584847134220702e-08, 4.092403723245084e-09, 3.320774587113095e-10, 2.470084222824226e-11, 1.6959850525483697e-12, 1.0813034671495497e-13], [0.013952564798465595, 0.012453965521309411, 0.0055581629415912305, 0.0016537262894252805, 0.0003592840346904036, 7.279156449207108e-05, 1.082887683520045e-05, 1.3808260927351276e-06, 1.5406451070324756e-07, 1.5279660701734354e-08, 1.3638522401102417e-09, 1.1066957626419215e-10, 8.231909968766382e-12, 5.652113451009722e-13, 3.6035989008960393e-14], [0.0037199138780142312, 0.003320370114613223, 0.0014818700189776878, 0.0004409024049217535, 9.838663049537993e-05, 1.7100167441255948e-05, 2.8871028233460685e-06, 3.6814408101186174e-07, 4.1075366411307334e-08, 4.073732873971749e-09, 3.6361865713068216e-10, 2.9505778942119416e-11, 2.1947216571067536e-12, 1.506918302850971e-13, 9.607608175175224e-15], [0.0008264764375892527, 0.0007377073109198622, 0.0003292362926715886, 9.795803367866866e-05, 2.1859170546614644e-05, 3.902269729532439e-06, 5.651976073033184e-07, 8.179286364464824e-08, 9.125970013696283e-09, 9.050866078565484e-10, 8.078742203214103e-11, 6.55548269880821e-12, 4.876149814613078e-13, 3.34801425925256e-14, 2.1345821539855076e-15], [0.00015739150136028483, 0.00014048659580521525, 6.26986953881301e-05, 1.8654811304674386e-05, 4.162789783647832e-06, 7.43135634012042e-07, 1.1055297833915311e-07, 1.372482093792665e-08, 1.7379202315970237e-09, 1.723617680948657e-10, 1.5384895523161828e-11, 1.248404935918542e-12, 9.285982095487713e-14, 6.375850137681584e-15, 4.0650292580950714e-16], [2.622648768561924e-05, 2.3409586559860852e-05, 1.0447619778002288e-05, 3.108491721161303e-06, 6.936547021604946e-07, 1.2383030459533825e-07, 1.842168287335462e-08, 2.3490100377662133e-09, 2.551697367616391e-10, 2.872101574318049e-11, 2.5636185530698348e-12, 2.0802442568729218e-13, 1.5473433633414863e-14, 1.062421755152366e-15, 6.773646534768613e-17], [3.884601422450118e-06, 3.4673691094087308e-06, 1.5474751761403239e-06, 4.604219789720005e-07, 1.0274239063202443e-07, 1.834143340654975e-08, 2.7285733549825394e-09, 3.4792946136892465e-10, 3.881993721517122e-11, 3.748405782687698e-12, 3.7971673512863127e-13, 3.081205495817592e-14, 2.2918860894785363e-15, 1.5736323943864714e-16, 1.0032954957428255e-17], [5.178396571043032e-07, 4.6222019594941523e-07, 2.062873194554149e-07, 6.137689141960023e-08, 1.3696150144898706e-08, 2.4450183051363224e-09, 3.63734483121541e-10, 4.6380993409133325e-11, 5.174920356085254e-12, 5.132332348219002e-13, 4.460145757448241e-14, 4.107423706846376e-15, 3.0552156518264467e-16, 2.097742267219123e-17, 1.3374504588480165e-18], [6.275545212956354e-08, 5.6015094599791255e-08, 2.4999348395622702e-08, 7.438083426986987e-09, 1.6597958132132463e-09, 2.9630451646344954e-10, 4.407990317127784e-11, 5.620775025003935e-12, 6.271332491153726e-13, 6.21972134758297e-14, 5.551681453109537e-15, 4.385974817859313e-16, 3.702525230605683e-17, 2.5421916345065846e-18, 1.6208165422331466e-19], [6.97138485139226e-09, 6.222611242383619e-09, 2.777130476888393e-09, 8.262826633649741e-10, 1.8438358733755488e-10, 3.291591005045583e-11, 4.896753330445987e-12, 6.244012995316605e-13, 6.966705018172775e-14, 6.9093711719104045e-15, 6.167258249061454e-16, 5.004412040121775e-17, 3.624149414417403e-18, 2.8240727536383048e-19, 1.8005345361996243e-20], [7.148658448286543e-10, 6.380844462974194e-10, 2.8477494312535964e-10, 8.472939979718771e-11, 1.8907223133474745e-11, 3.3752920471495443e-12, 5.021271642732082e-13, 6.402790435714743e-14, 7.143859612761868e-15, 7.085067838502783e-16, 6.324083912267914e-17, 5.131667978734355e-18, 3.8170769435041823e-19, 2.5516543387367643e-20, 1.846319877328904e-21], [6.8068370416561e-11, 6.075736973841501e-11, 2.711580984633312e-11, 8.067796513554571e-12, 1.8003152299245826e-12, 3.2138985376272437e-13, 4.781173707097231e-14, 6.096633574405954e-15, 6.802267668025721e-16, 6.746287090737497e-17, 6.021690494792706e-18, 4.886291314071934e-19, 3.634558976044432e-20, 2.495525310035355e-21, 1.5490599412539256e-22]] |
| Legacy trial inputs | {"lambda_home": 1.3330573739472331, "lambda_away": 0.8925932759458685, "rho": -0.021898200937208512, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4580 |
| Legacy p draw | 0.2732 |
| Legacy p away | 0.2688 |
| Legacy p over 1 5 | 0.6539 |
| Legacy p under 3 5 | 0.8146 |
| Legacy p btts yes | 0.4349 |
| Legacy p over 2 5 | 0.3875 |
| Legacy goal margin distribution | {"-1": 0.17739004736394443, "-10": 1.1543877431520878e-08, "-11": 9.284179493769566e-10, "-12": 6.853250795972657e-11, "-13": 4.6607198351899995e-12, "-14": 2.73874956250003e-13, "-2": 0.06817107303767872, "-3": 0.01854388926990991, "-4": 0.0039138402440010165, "-5": 0.0006727316571130273, "-6": 9.737705360132826e-05, "-7": 1.216259132119918e-05, "-8": 1.335249376582147e-06, "-9": 1.3071621804542141e-07, "0": 0.27321491238091394, "1": 0.24112761529379706, "10": 5.7671841189601e-07, "11": 6.927090611158608e-08, "12": 7.636585107536012e-09, "13": 7.756232145670694e-10, "14": 6.8068370416561e-11, "2": 0.13761012656754987, "3": 0.055904442426179674, "4": 0.01762153838261629, "5": 0.004523533608163838, "6": 0.0009778850725675652, "7": 0.00018241163320765268, "8": 2.9907770004601493e-05, "9": 4.372666478071508e-06} |
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
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 10.303107674781515, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,505.1233 |
| Elo away rating | 1,510.6645 |
| Elo rating diff | 54.4588 |
| Elo home expectancy | 0.5777 |

</details>


---

## 2026-11-01 — Elche CF vs Valencia

The model's most likely 1X2 outcome is **Elche CF win** at **43.2%**. Expected goals are 1.49 for Elche CF and 1.07 for Valencia (2.56 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 47.4%; Under 3.5 goals: 74.0%; Double Chance 1X: 70.9%; Double Chance X2: 56.8%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 88.1%; BTTS Yes (both teams score): 52.3%; BTTS No (at least one team does not score): 47.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 43.2% | 2.31 |
| Draw | 27.7% | 3.61 |
| Valencia win | 29.1% | 3.44 |

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
| 1 | 1-1 | 13.19% |
| 2 | 1-0 | 10.09% |
| 3 | 2-1 | 8.54% |
| 4 | 0-1 | 8.37% |
| 5 | 0-0 | 8.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 43.2% | 41.8% | 2.33 | +0.7% |
| Draw | 27.7% | 28.1% | 3.42 | -5.3% |
| Valencia win | 29.1% | 30.1% | 3.20 | -7.0% |
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
| Market best home last update utc | 2026-10-30T11:46:34Z |
| Market best draw last update utc | 2026-10-30T11:46:34Z |
| Market best away last update utc | 2026-10-30T11:46:34Z |
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
| Bbs statistics cutoff utc | 2026-10-30T11:46:35.127291+00:00 |
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
| Fair Under 0.5 odds | 12.14 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.75 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.84 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.37 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.1781132397499574, "-10": 5.6184694709958676e-08, "-11": 5.4490663005399936e-09, "-12": 4.85330404318767e-10, "-13": 3.995246102813572e-11, "-14": 3.0429886783032397e-12, "-15": 1.9756668675828586e-13, "-2": 0.07934329784571782, "-3": 0.025358550448115656, "-4": 0.006353278593192581, "-5": 0.0013037942933553884, "-6": 0.00022611307294080217, "-7": 3.3915261118801104e-05, "-8": 4.4783365781114605e-06, "-9": 5.279088332577884e-07, "0": 0.2769450050993924, "1": 0.212924992789162, "10": 1.3801987311611574e-06, "11": 1.8743322884408915e-07, "12": 2.3375606612303988e-08, "13": 2.6944481037839333e-09, "14": 2.8736079693999647e-10, "15": 2.612412756023375e-11, "2": 0.1318944973605462, "3": 0.0590257821057144, "4": 0.020706949361431762, "5": 0.005950153829184112, "6": 0.0014449262673327462, "7": 0.0003034702169838433, "8": 5.610977625716951e-05, "9": 9.26150640115873e-06} |
| Raw goal margin distribution | {"-1": 0.16405714542390845, "-10": 4.67440789112865e-08, "-11": 4.477386989875115e-09, "-12": 3.93835269719201e-10, "-13": 3.201734301197202e-11, "-14": 2.4087396248710413e-12, "-15": 1.5478932064177855e-13, "-2": 0.07248155202777266, "-3": 0.022932423977876405, "-4": 0.005682471695813901, "-5": 0.0011527571023698755, "-6": 0.00019756284885012865, "-7": 2.9277551908811656e-05, "-8": 3.8190352447093305e-06, "-9": 4.446807227123586e-07, "0": 0.267152917780171, "1": 0.23132512223440055, "10": 1.354364518372657e-06, "11": 1.8164961856224256e-07, "12": 2.2373058589470428e-08, "13": 2.546812297663725e-09, "14": 2.6828871331450553e-10, "15": 2.4140954409870108e-11, "2": 0.14211151732240637, "3": 0.06295825044003758, "4": 0.021844437483092897, "5": 0.0062050071639942785, "6": 0.0014890547171680832, "7": 0.00030898758674984537, "8": 5.6436599130022076e-05, "9": 9.201452061848955e-06} |
| Unadjusted home-win probability | 46.6% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 72.9% |
| Raw p under 3 5 | 74.5% |
| Raw p btts yes | 51.2% |
| P home draw | 70.9% |
| P draw away | 56.8% |
| P home away | 72.3% |
| Raw p home draw | 73.3% |
| Raw p draw away | 53.4% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0128 |
| Totals anchor target over 2 5 | 0.4745 |
| Totals anchor reference over odds | 2.04 |
| Totals anchor reference under odds | 1.85 |
| Totals anchor reference last update utc | 2026-10-30T11:46:34Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4669 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.33 |
| Reference draw odds | 3.42 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-30T11:46:34Z |
| Market reference home last update utc | 2026-10-30T11:46:34Z |
| Market reference draw last update utc | 2026-10-30T11:46:34Z |
| Market reference away last update utc | 2026-10-30T11:46:34Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-30T11:46:34Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:46:34Z |
| Market best over 2 5 last update utc | 2026-10-30T11:46:34Z |
| Market best under 2 5 last update utc | 2026-10-30T11:46:34Z |
| Home probability edge | +1.5% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0486 |
| Raw ev home | 0.0865 |
| Raw edge prob draw | -0.0140 |
| Raw ev draw | -0.0863 |
| Raw edge prob away | -0.0346 |
| Raw ev away | -0.1471 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0934523948915111, 0.09617274156684985, 0.05645893640837319, 0.021487479348531256, 0.006133374955214569, 0.0014005658916460917, 0.00026651786756418095, 4.347126961097194e-05, 6.2042083200778046e-06, 7.87078223763628e-07, 8.9865279907884e-08, 9.327672314571522e-09, 8.874953150884117e-10, 7.794652375698476e-11, 6.356861512599932e-12], [0.1156389849728455, 0.13303611006704114, 0.07105339460572771, 0.027041925448088835, 0.007718833167624409, 0.0017626077872004327, 0.0003354119014311853, 5.47084566265808e-05, 7.807976735411005e-06, 9.905354789920973e-07, 1.1309517325059082e-07, 1.1738846387865714e-08, 1.1169100738560754e-09, 9.809545597157929e-11, 8.000090299996154e-12], [0.07463162318059667, 0.08521124717481965, 0.046765769549105725, 0.01701608923221558, 0.0048570636806546195, 0.0011091181893085325, 0.00021105741361710287, 3.442521064196215e-05, 4.913157131058018e-06, 6.232928986717603e-07, 7.116496062601719e-08, 7.386650702911085e-09, 7.02813914548332e-10, 6.1726412022382e-11, 5.0340442906641386e-12], [0.031307887993502655, 0.035746029211776754, 0.020406656058600557, 0.007466408532874093, 0.0020375331422615973, 0.00046527392226752303, 8.853836462504486e-05, 1.4441339917305947e-05, 2.0610642861327283e-06, 2.6147072014687836e-07, 2.985362667176495e-08, 3.0986922566892914e-09, 2.9482970327081143e-10, 2.5894165388325145e-11, 2.111776323356449e-12], [0.009850219741052178, 0.011246566446102784, 0.006420428180879049, 0.0024435249177826622, 0.0006705295778506681, 0.00014638644341219875, 2.7856313630963704e-05, 4.5435952616865495e-06, 6.484607368933828e-07, 8.226502055432214e-08, 9.3926739116113e-09, 9.749236245070507e-10, 9.276056449446224e-11, 8.146931506177735e-12, 6.644159718895515e-13], [0.0024792941374301622, 0.0028307537282475843, 0.0016160177505790835, 0.0006150336908804784, 0.00017555489757887081, 3.853932505668766e-05, 7.011416688282627e-06, 1.1436200806979799e-06, 1.6321716120027117e-07, 2.0706054132566606e-08, 2.364130138823039e-09, 2.453876654760094e-10, 2.334777596659652e-11, 2.0505775558621156e-12, 1.6723308385247954e-13], [0.000520030650879585, 0.0005937491165555058, 0.00033895887945658323, 0.00012900299555137316, 3.6822548109465964e-05, 8.408487219873728e-06, 1.5382530226104406e-06, 2.398737148391641e-07, 3.42347143456213e-08, 4.343084043617172e-09, 4.958750622991862e-10, 5.1469934716007685e-11, 4.897183819054601e-12, 4.3010757172981156e-13, 3.507705202519758e-14], [9.349384929646144e-05, 0.00010674734331381084, 6.093981256683521e-05, 2.3192837969208343e-05, 6.620151634975989e-06, 1.5117221179490252e-06, 2.876701179348656e-07, 4.5108446487135457e-08, 6.154897251389257e-09, 7.808225233820552e-10, 8.915103035957136e-11, 9.253535943502292e-12, 8.80441499325736e-13, 7.73270045228263e-14, 6.306337155821489e-15], [1.4707714557399765e-05, 1.679264964523937e-05, 9.586570401785544e-06, 3.6485142412469916e-06, 1.0414300117774204e-06, 2.3781219372410197e-07, 4.525399278259971e-08, 7.381300695540165e-09, 1.0127542394494223e-09, 1.2283283745732483e-10, 1.4024536553938663e-11, 1.455693249639489e-12, 1.3850410860195604e-13, 1.2164474119513386e-14, 9.920631944079899e-16], [2.056623632983849e-06, 2.3481663303998007e-06, 1.3405187577329e-06, 5.101826381347242e-07, 1.456262674911984e-07, 3.325398898081346e-08, 6.3280009059428865e-09, 1.0321493113945676e-09, 1.473080819268388e-10, 1.796574471749904e-11, 1.9610928132926338e-12, 2.0355393272691574e-13, 1.936744297725236e-14, 1.700994730308025e-15, 1.387231580454085e-16], [2.5882543994965297e-07, 2.9551599709029665e-07, 1.687038657275338e-07, 6.420632518858716e-08, 1.8327020144638816e-08, 4.185004096035079e-09, 7.96376931692748e-10, 1.2989566750618402e-10, 1.8538675964516152e-11, 2.351853354417643e-12, 2.581495650693588e-13, 2.5617198668036393e-14, 2.4373866316095785e-15, 2.1406965395280626e-16, 1.7458265983365783e-17], [2.9611909579611833e-08, 3.380963241816149e-08, 1.9301207866686e-08, 7.3457690105479376e-09, 2.0967724945906995e-09, 4.788013222587477e-10, 9.111253398105538e-11, 1.486120824028991e-11, 2.1209877842524325e-12, 2.690727344617633e-13, 3.07215926802821e-14, 3.065576800122695e-15, 2.7885849458931545e-16, 2.4491453536493038e-17, 1.997379368182675e-18], [3.1055412869314616e-09, 3.545776373802951e-09, 2.0242091364114393e-09, 7.703856073579612e-10, 2.198984680048132e-10, 5.0214163680132656e-11, 9.55540321620901e-12, 1.5585653346612492e-12, 2.2243804018665222e-13, 2.8218932784864512e-14, 3.2219190124299333e-15, 3.34422869464603e-16, 3.058974678394705e-17, 2.5685347961115756e-18, 2.0947463981948594e-19], [3.0063953701019784e-10, 3.4325757375942545e-10, 1.9595852746941057e-10, 7.457906719516397e-11, 2.1287810240494754e-11, 4.861105206901261e-12, 9.250342318602161e-13, 1.50880737791023e-13, 2.1533659750905375e-14, 2.7318029623577157e-15, 3.1190576800812187e-16, 3.2374625661732176e-17, 3.0803321164748946e-18, 2.600850269994423e-19, 2.0278706000696642e-20], [2.7025279681348833e-11, 3.085632723441505e-11, 1.7615228068377652e-11, 6.704108745534182e-12, 1.9136173215079752e-12, 4.369775482075448e-13, 8.315376307273928e-14, 1.3563066847033965e-14, 1.93571738141508e-15, 2.4556896217396133e-16, 2.8038030854070513e-17, 2.9102403555710872e-18, 2.76899165648833e-19, 2.4319370510013232e-20, 1.906713549406843e-21]] |
| Legacy trial inputs | {"lambda_home": 1.2584968673832488, "lambda_away": 1.1417579243670206, "rho": -0.021898200937208512, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T11:46:34Z", "over": 2.04, "under": 1.85, "bookmaker": "pinnacle", "event_id": "5262991e389930615bec34b642428c93", "kickoff_utc": "2026-11-01T17:30:00Z", "home_team": "Elche CF", "away_team": "Valencia"}} |
| Legacy p home | 0.4026 |
| Legacy p draw | 0.2814 |
| Legacy p away | 0.3160 |
| Legacy p over 1 5 | 0.6947 |
| Legacy p under 3 5 | 0.7785 |
| Legacy p btts yes | 0.4900 |
| Legacy p over 2 5 | 0.4306 |
| Legacy goal margin distribution | {"-1": 0.18643340256058716, "-10": 1.0233349879165825e-07, "-11": 1.0508420576773335e-08, "-12": 9.906248153506552e-10, "-13": 8.594661405698091e-11, "-14": 6.356861512599932e-12, "-2": 0.08885223442286325, "-3": 0.030408680316222483, "-4": 0.008122151168009259, "-5": 0.0017725487495187447, "-6": 0.00032641059507904655, "-7": 5.193339157954085e-05, "-8": 7.26910229817171e-06, "-9": 9.078631915849907e-07, "0": 0.2814313363358897, "1": 0.22388467170995674, "10": 2.9473577418874263e-07, "11": 3.3360348589629734e-08, "12": 3.4664140887592647e-09, "13": 3.314958642446129e-10, "14": 2.7025279681348833e-11, "2": 0.11745149483931347, "3": 0.044306339609610695, "4": 0.01304420068218965, "5": 0.003137781484758216, "6": 0.0006368935627630027, "7": 0.00011169337194987786, "8": 1.7232155365264623e-05, "9": 2.3722329483359786e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3874 |
| Legacy raw p draw | 0.2817 |
| Legacy raw p away | 0.3308 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2585 |
| Legacy lambda away | 1.1418 |
| Legacy model home team | Elche |
| Legacy model away team | Valencia |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 9.234622291059388, "version": "count-markets-nb2-v1"}} |
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
| Market best home last update utc | 2026-10-30T11:46:34Z |
| Market best draw last update utc | 2026-10-30T11:46:34Z |
| Market best away last update utc | 2026-10-30T11:46:34Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Getafe |
| Matched away-team name | Sevilla |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0240 |
| Dc lambda away | 0.9165 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:46:35.127291+00:00 |
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
| Fair Over 4.5 odds | 21.10 |
| Fair Under 4.5 odds | 1.05 |
| Goal margin distribution | {"-1": 0.230589635474221, "-10": 2.0822220434631554e-08, "-11": 1.7225157902599215e-09, "-12": 1.3047555225644888e-10, "-13": 8.578832179220789e-12, "-2": 0.09427185761957828, "-3": 0.02679459458695054, "-4": 0.0058717051426292865, "-5": 0.0010442710068251707, "-6": 0.000156074566041159, "-7": 2.0101122083823305e-05, "-8": 2.273401031997324e-06, "-9": 2.2912827617734277e-07, "0": 0.3199887948126359, "1": 0.19537811118607107, "10": 4.7762317338330006e-08, "11": 4.4145967705701495e-09, "12": 3.7361684846536756e-10, "13": 2.7447004953589277e-11, "2": 0.08903988258998632, "3": 0.028276078824089685, "4": 0.006923181405989108, "5": 0.001375701379379799, "6": 0.00022972727863148514, "7": 3.3057515682991276e-05, "8": 4.177297861986097e-06, "9": 4.704002654934367e-07} |
| Raw goal margin distribution | {"-1": 0.199471399363212, "-10": 1.801224690521514e-08, "-11": 1.4900610532722221e-09, "-12": 1.1286778322779978e-10, "-13": 7.421112645293344e-12, "-2": 0.08154980305716746, "-3": 0.02317864489718789, "-4": 0.0050793143370894125, "-5": 0.0009033458881075098, "-6": 0.00013501219180649818, "-7": 1.7388461292221676e-05, "-8": 1.9666039379162535e-06, "-9": 1.9820725154788953e-07, "0": 0.32235138901388666, "1": 0.22338458657257879, "10": 5.460880672661452e-08, "11": 5.047407145518352e-09, "12": 4.2717295568233546e-10, "13": 3.138139588407574e-11, "2": 0.10180330457741196, "3": 0.032329313348706576, "4": 0.007915584845996288, "5": 0.0015729012938783679, "6": 0.00026265753543223155, "7": 3.779614527509061e-05, "8": 4.77609262483651e-06, "9": 5.378297916433848e-07} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.78, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.17, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.20 |
| Reference draw odds | 3.03 |
| Reference away odds | 2.56 |
| Market reference 1x2 last update utc | 2026-10-30T11:46:34Z |
| Market reference home last update utc | 2026-10-30T11:46:34Z |
| Market reference draw last update utc | 2026-10-30T11:46:34Z |
| Market reference away last update utc | 2026-10-30T11:46:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.72 |
| Reference Under 2.5 odds | 1.47 |
| Market reference over 2 5 last update utc | 2026-10-30T11:45:53Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:45:53Z |
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
| Legacy trial matrix | [[0.14016768589869877, 0.13881909736542997, 0.0678836215956607, 0.02162769302383169, 0.005167930362340131, 0.0009879002517954318, 0.00015737230042955889, 2.1488034905329446e-05, 2.5672795496938024e-06, 2.726447249080757e-07, 2.6059348085470287e-08, 2.2643174285065484e-09, 1.8035264288028976e-10, 1.3260063568177014e-11], [0.12651495065466667, 0.13900236424934392, 0.0704196368480503, 0.022435666406706453, 0.005360995344939992, 0.001024806504695658, 0.00016325145868322676, 2.2290790901295317e-05, 2.6631886945233334e-06, 2.828302625178522e-07, 2.7032880473086833e-08, 2.3489084299876954e-09, 1.8709030717105912e-10, 1.375543671807834e-11], [0.06702348553910639, 0.06406096212402176, 0.0337170667668217, 0.011636912142186458, 0.002780636451480178, 0.0005315457558381139, 8.467512608462666e-05, 1.1561768239729415e-05, 1.3813404199559847e-06, 1.4669815714000602e-07, 1.4021391177464893e-08, 1.2183298028373815e-09, 9.703983950097862e-11, 7.1346580780785274e-12], [0.023175789196335013, 0.022151389799542266, 0.010586135080329026, 0.003714518290822478, 0.0009615054143006126, 0.00018380113010271428, 2.9279481013642304e-05, 3.997898666498131e-06, 4.776483067655094e-07, 5.072618259138265e-08, 4.848402072116561e-09, 4.2128150237272786e-10, 3.35550269555684e-11, 2.4670655409139922e-12], [0.00601039919685576, 0.005744731898125051, 0.0027454037161624696, 0.0008746844585475702, 0.00023018538366356185, 4.766690598502828e-05, 7.593328006132306e-06, 1.0368133197393334e-06, 1.2387310632843194e-07, 1.3155306364066298e-08, 1.2573825069521894e-09, 1.0925496353374019e-10, 8.702146250800163e-12, 6.398077157193364e-13], [0.0012469874729884802, 0.0011918690386466834, 0.0005695934546479972, 0.000181472232858863, 4.336273226550652e-05, 9.129204997935234e-06, 1.5754003339566888e-06, 2.1510937613243787e-07, 2.5700158470760497e-08, 2.72935319302885e-09, 2.608712306071903e-10, 2.26673081814031e-11, 1.8054486910849838e-12, 1.3274196613109488e-13], [0.0002155954630827815, 0.0002060658690541915, 9.847874760879073e-05, 3.137528718400715e-05, 7.497114883529321e-06, 1.433146571623721e-06, 2.5143497193880405e-07, 3.719091535825686e-08, 4.4433786921094964e-09, 4.718861883650689e-10, 4.510282178933473e-11, 3.919019966173206e-12, 3.1214952440044664e-13, 2.2950162915402984e-14], [3.1949962638804426e-05, 3.053773360196464e-05, 1.4593963443511818e-05, 4.649630557976466e-06, 1.1110277415049955e-06, 2.1238378008783554e-07, 3.383269108961551e-08, 5.087739047071856e-09, 6.584822387864812e-10, 6.993072058405428e-11, 6.683969367762577e-12, 5.807754008806997e-13, 4.625869904546867e-14, 3.40107735671624e-15], [4.142944780801897e-06, 3.959821345459713e-06, 1.8923960995834662e-06, 6.029165940065851e-07, 1.4406672818464626e-07, 2.753975906604697e-08, 4.387077773917876e-09, 5.990233356253072e-10, 7.882066211814322e-11, 9.067901491363523e-12, 8.667088697493369e-13, 7.530902126860396e-14, 5.998355551888734e-15, 4.410169690463941e-16], [4.775242296020661e-07, 4.564170505276364e-07, 2.181214178241204e-07, 6.949339112638853e-08, 1.6605423684731718e-08, 3.1742885621794708e-09, 5.056634942136474e-10, 6.904464625829941e-11, 8.249098120685367e-12, 9.648288577327443e-13, 9.98986245808039e-14, 8.680270741241941e-15, 6.913826433478376e-16, 5.083251154135709e-17], [4.953637128410369e-08, 4.734680058889033e-08, 2.2627005853409345e-08, 7.208954459749416e-09, 1.7225773730103521e-09, 3.292874518849872e-10, 5.24554211941418e-11, 7.162403539357326e-12, 8.557270227016442e-13, 9.08780887257576e-14, 9.56633332879188e-15, 9.00455071448467e-16, 7.172115088024706e-17, 5.273152667278301e-18], [4.671542258782691e-09, 4.465054141746072e-09, 2.133846531222309e-09, 6.798425990311958e-10, 1.624481725940039e-10, 3.105355129759427e-11, 4.946824130602293e-12, 6.754526006086294e-13, 8.06995919342976e-14, 8.570285244450585e-15, 8.191467722407138e-16, 7.838904323097139e-17, 6.763684511003356e-18, 4.972862340061689e-19], [4.0383858635697183e-10, 3.8598840655247403e-10, 1.8446361371374912e-10, 5.877002902453655e-11, 1.4043079724538484e-11, 2.6844715433767716e-12, 4.276357470818537e-13, 5.83905289239551e-14, 6.976199148163851e-15, 7.408713624045882e-16, 7.081239046883136e-17, 6.152944784608268e-18, 5.397443394454087e-19, 4.2988665976054765e-20], [3.222502313861163e-11, 3.080063607739145e-11, 1.4719604369115438e-11, 4.689659703539302e-12, 1.1205926930929786e-12, 2.1421221379720562e-13, 3.4123960191433795e-14, 4.659376813455261e-15, 5.566783030743485e-16, 5.911915701665689e-17, 5.650601498840893e-18, 4.909852469603619e-19, 3.9106922814676785e-20, 3.1666248568155408e-21]] |
| Legacy trial inputs | {"lambda_home": 1.037358278665434, "lambda_away": 0.9557987265022783, "rho": -0.021898200937208512, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3328 |
| Legacy p draw | 0.3168 |
| Legacy p away | 0.3504 |
| Legacy p over 1 5 | 0.5945 |
| Legacy p under 3 5 | 0.8587 |
| Legacy p btts yes | 0.4009 |
| Legacy p over 2 5 | 0.3206 |
| Legacy goal margin distribution | {"-1": 0.22188643193485263, "-10": 2.8507763420499875e-08, "-11": 2.458542393755686e-09, "-12": 1.941080795983681e-10, "-13": 1.3260063568177014e-11, "-2": 0.09329153853551718, "-3": 0.027550576597747813, "-4": 0.006281536539936083, "-5": 0.0011632045471684678, "-6": 0.0001810964382987673, "-7": 2.4302881242427286e-05, "-8": 2.864561319779709e-06, "-9": 3.0093013001867123e-07, "0": 0.3168412063968544, "1": 0.20208156263645738, "10": 5.419057869926705e-08, "11": 5.07225026970428e-09, "12": 4.346392224343633e-10, "13": 3.222502313861163e-11, "2": 0.0921094652433204, "3": 0.029522628916699985, "4": 0.007305543907823867, "5": 0.001468267161797098, "6": 0.0002480968402386754, "7": 3.6135279523316107e-05, "8": 4.622682937073913e-06, "9": 5.270647673438964e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3640 |
| Legacy raw p draw | 0.3147 |
| Legacy raw p away | 0.3213 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0374 |
| Legacy lambda away | 0.9558 |
| Legacy model home team | Getafe |
| Legacy model away team | Sevilla |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p over 1 5 | 61.6% |
| Market reference over 1 5 odds | 1.57 |
| Market reference over 1 5 opposite odds | 2.44 |
| Market reference over 1 5 last update utc | 2026-10-30T11:46:40Z |
| Market over 1 5 bookmakers | 0 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 8.56987826690374, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,449.4205 |
| Elo away rating | 1,481.9065 |
| Elo rating diff | 27.5140 |
| Elo home expectancy | 0.5395 |

</details>


---

## 2026-11-01 — Real Racing Club de Santander vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **80.6%**. Expected goals are 1.19 for Real Racing Club de Santander and 3.49 for Real Madrid (4.68 combined). The most likely exact score is 1-3 at 7.9%. Goal-market probabilities: at least one goal: 99.0%; Over 2.5 goals: 84.7%; Under 3.5 goals: 31.1%; Double Chance 1X: 19.4%; Double Chance X2: 91.7%; Double Chance 12 (either team wins): 88.9%; Under 4.5 goals: 49.6%; BTTS Yes (both teams score): 67.4%; BTTS No (at least one team does not score): 32.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 8.3% | 12.06 |
| Draw | 11.1% | 9.03 |
| Real Madrid win | 80.6% | 1.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.19 |
| Real Madrid expected goals | 3.49 |
| Expected total goals | 4.68 |
| Over 0.5 | 99.0% |
| Under 0.5 | 1.0% |
| Over 1.5 | 94.9% |
| Under 1.5 | 5.1% |
| Over 2.5 | 84.7% |
| Under 2.5 | 15.3% |
| Over 3.5 | 68.9% |
| Under 3.5 | 31.1% |
| Over 4.5 | 50.4% |
| Under 4.5 | 49.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-3 | 7.88% |
| 2 | 1-4 | 6.89% |
| 3 | 1-2 | 6.77% |
| 4 | 0-3 | 6.63% |
| 5 | 0-4 | 5.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 8.3% | 8.2% | 10.50 | -12.9% |
| Draw | 11.1% | 10.9% | 7.99 | -11.5% |
| Real Madrid win | 80.6% | 80.9% | 1.22 | -1.6% |

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
| Market best home last update utc | 2026-10-30T11:46:34Z |
| Market best draw last update utc | 2026-10-30T11:46:34Z |
| Market best away last update utc | 2026-10-30T11:46:34Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santander |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1886 |
| Dc lambda away | 3.4930 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:46:35.127291+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 67.4% |
| P btts no | 32.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 98.08 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 19.62 |
| Fair Over 2.5 odds | 1.18 |
| Fair Under 2.5 odds | 6.55 |
| Fair Over 3.5 odds | 1.45 |
| Fair Under 3.5 odds | 3.21 |
| Fair Over 4.5 odds | 1.99 |
| Fair Under 4.5 odds | 2.01 |
| Goal margin distribution | {"-1": 0.16602289067195658, "-10": 0.0010092088356381279, "-11": 0.000310941642475114, "-12": 8.821467540369679e-05, "-13": 2.318410671080556e-05, "-14": 5.674205328125753e-06, "-15": 1.299208266118477e-06, "-16": 2.7942822665172714e-07, "-17": 5.6655294103222924e-08, "-18": 1.0863331242998735e-08, "-19": 1.97373035106995e-09, "-2": 0.19027283125578084, "-20": 3.361814686890372e-10, "-21": 4.6688094089113196e-11, "-3": 0.17145176799364914, "-4": 0.1264274686859146, "-5": 0.07839148177220964, "-6": 0.041778576482085016, "-7": 0.019479123115632782, "-8": 0.008060188434220237, "-9": 0.002995003202867903, "0": 0.11075053840346769, "1": 0.05331601957763693, "10": 2.0124996529333658e-08, "11": 2.109983494553731e-09, "12": 2.036978334657652e-10, "13": 1.821718783175599e-11, "14": 1.51719504640014e-12, "15": 1.1821172195715512e-13, "16": 8.651620137628236e-15, "17": 5.969157886765783e-16, "18": 3.894762589821201e-17, "19": 2.407970637652572e-18, "2": 0.021104173708968794, "20": 1.3956693374663638e-19, "21": 6.595691166008997e-21, "3": 0.006471112349334566, "4": 0.001623767386937919, "5": 0.0003426073258959771, "6": 6.213364180503517e-05, "7": 9.857980923958633e-06, "8": 1.3880629608808437e-06, "9": 1.7551193790420743e-07} |
| Raw goal margin distribution | {"-1": 0.16469474911143508, "-10": 0.0010011354176146763, "-11": 0.00030845418718147014, "-12": 8.750898008555502e-05, "-13": 2.2998639661403156e-05, "-14": 5.628813106073031e-06, "-15": 1.2888149252543279e-06, "-16": 2.771928707950925e-07, "-17": 5.620206593439929e-08, "-18": 1.0776427312756692e-08, "-19": 1.9579410023969513e-09, "-2": 0.18875069624171087, "-20": 3.3349210110462805e-10, "-21": 4.6314601025052463e-11, "-3": 0.17008019677370698, "-4": 0.12541608058832343, "-5": 0.07776436954382268, "-6": 0.04144435832975251, "-7": 0.019323295007426276, "-8": 0.007995708944664337, "-9": 0.0029710439270624746, "0": 0.11424477848813248, "1": 0.055216481301308434, "10": 2.084235663790904e-08, "11": 2.185194339263151e-09, "12": 2.1095868937292438e-10, "13": 1.886654366254476e-11, "14": 1.5712758111659499e-12, "15": 1.224254058489493e-13, "16": 8.96000911808027e-15, "17": 6.181929886180167e-16, "18": 4.033592293977278e-17, "19": 2.4938033022970104e-18, "2": 0.02185643681227879, "20": 1.4454182905159148e-19, "21": 6.830796087596506e-21, "3": 0.006701776630481443, "4": 0.001681646947180184, "5": 0.00035481964246185713, "6": 6.434840969165201e-05, "7": 1.020937091081589e-05, "8": 1.437540782895649e-06, "9": 1.817681011113773e-07} |
| Unadjusted home-win probability | 8.6% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 80.0% |
| Raw p over 1 5 | 94.9% |
| Raw p under 3 5 | 31.3% |
| Raw p btts yes | 67.5% |
| P home draw | 19.4% |
| P draw away | 91.7% |
| P home away | 88.9% |
| Raw p home draw | 20.0% |
| Raw p draw away | 91.4% |
| Raw p home away | 88.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8472 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:35Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.67, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": -2.0, "market_key": "spreads", "opposite_price": 2.01, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:46:34Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.88, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:46:35Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.67, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.50 |
| Reference draw odds | 7.99 |
| Reference away odds | 1.22 |
| Market reference 1x2 last update utc | 2026-10-30T11:46:34Z |
| Market reference home last update utc | 2026-10-30T11:46:34Z |
| Market reference draw last update utc | 2026-10-30T11:46:34Z |
| Market reference away last update utc | 2026-10-30T11:46:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.63 |
| Market reference over 2 5 last update utc | 2026-10-30T11:45:53Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:45:53Z |
| Home probability edge | +0.1% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | 0.0042 |
| Raw ev home | -0.0982 |
| Raw edge prob draw | 0.0050 |
| Raw ev draw | -0.0872 |
| Raw edge prob away | -0.0092 |
| Raw ev away | -0.0242 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.009040091273037724, 0.02838985951308036, 0.053331996323870624, 0.06508844512002454, 0.05957735477988633, 0.043626314268508465, 0.026621626394883382, 0.013924315511835794, 0.0063726663295302485, 0.0025924833823893793, 0.0009491903022034482, 0.00031593512926895057, 9.639488365498314e-05, 2.7148631477291734e-05, 7.09998151121642e-06, 1.7330187834696082e-06, 3.965706766868635e-07, 8.541005236329197e-08, 1.7372958977530833e-08, 3.3477845776163367e-09, 6.128649997383897e-10, 1.0685204447361957e-10, 1.778269036517657e-11], [0.008979196172360565, 0.03602088003975925, 0.06209922014920946, 0.07578830648177007, 0.06937125038253598, 0.05079802521560821, 0.030997944051944813, 0.016213327720671144, 0.007420266193145053, 0.003018660605136731, 0.0011052272857381136, 0.000367871568620809, 0.000112241196916699, 3.161158327207617e-05, 8.267144403199536e-06, 2.0179089922652227e-06, 4.617627588276859e-07, 9.9450573956663e-08, 2.022889219517169e-08, 3.8981254374022815e-09, 7.136136121622181e-10, 1.2441740588267649e-10, 2.0705979148544656e-11], [0.005683307463648706, 0.020808389228570173, 0.03756836632787569, 0.04412355671412101, 0.040387580125168486, 0.029574345312827068, 0.018046841338592644, 0.009439314828597488, 0.004320040272780927, 0.0017574484586678491, 0.0006434575607780584, 0.0002141729083952718, 6.534623938332822e-05, 1.8404098891748128e-05, 4.8130883492712035e-06, 1.174816089676923e-06, 2.6883586958765517e-07, 5.7899605413194066e-08, 1.1777155520056311e-08, 2.2694682966342516e-09, 4.154621227191853e-10, 7.243516473096778e-11, 1.2054913055775662e-11], [0.0022058613070818074, 0.008076357113456705, 0.014785051085186759, 0.017795714002440656, 0.015675625655413625, 0.011478686385543373, 0.007004517928771101, 0.003663679904517968, 0.0016767366086938163, 0.0006821182170702271, 0.0002497450903629826, 8.312690007994058e-05, 2.5362826477532783e-05, 7.143180251407868e-06, 1.8681032875894135e-06, 4.559811996326053e-07, 1.0434322733234313e-07, 2.2472565507528145e-08, 4.571065675285261e-09, 8.808484030143243e-10, 1.6125325383609612e-10, 2.8114250051423048e-11, 4.6788716676079715e-12], [0.0006421204734923113, 0.0023510064921744814, 0.004303889810727816, 0.005252634723197237, 0.004741667009877278, 0.00334141566983001, 0.002038996900923961, 0.0010664876651404528, 0.00048809365377586547, 0.00019856283398991665, 7.270014445668458e-05, 2.4198023814060188e-05, 7.383052640060064e-06, 2.0793611414050888e-06, 5.437999949082794e-07, 1.327349379907419e-07, 3.037404134396707e-08, 6.54170520964027e-09, 1.3306252965022744e-09, 2.564126728197458e-10, 4.694040163494732e-11, 8.183984866565999e-12, 1.3620073397038685e-12], [0.00014953567612043856, 0.0005474974866613735, 0.0010022808793103473, 0.0012232226150259893, 0.0011196513847549752, 0.0008085868237073258, 0.00047483734404054045, 0.0002483614222943711, 0.00011366623171273675, 4.624089848994375e-05, 1.693025795651422e-05, 5.635185298070535e-06, 1.7193498945138216e-06, 4.842372841461812e-07, 1.26639008207662e-07, 3.091103541567382e-08, 7.073443374539366e-09, 1.5234186603393923e-09, 3.098732427783415e-10, 5.971284825636167e-11, 1.093138279437034e-11, 1.905869320324728e-12, 3.1718142752234877e-13], [2.9019630214641247e-05, 0.0001062500603104368, 0.0001945075666449359, 0.00023738460867124724, 0.0002172850653293659, 0.00015910989302788905, 9.575462860997862e-05, 4.819824152705926e-05, 2.2058629069484656e-05, 8.97373663452825e-06, 3.2855692907746054e-06, 1.0935918289444131e-06, 3.336655134269587e-07, 9.397347366621935e-08, 2.4576190005489715e-08, 5.998747861293336e-09, 1.3727072789506742e-09, 2.956421325806332e-10, 6.013552853833079e-11, 1.158816959550802e-11, 2.12139801455688e-12, 3.6986239236118856e-13, 6.155379088423787e-14], [4.827164954743425e-06, 1.7673780257584046e-05, 3.2354654494085985e-05, 3.9486880270279596e-05, 3.614349475817459e-05, 2.6466557082098798e-05, 1.6150408449862795e-05, 8.331041791770586e-06, 3.669262509767556e-06, 1.492703617340959e-06, 5.465260866351966e-07, 1.819095595784283e-07, 5.550237756677075e-08, 1.563167605520387e-08, 4.088037036935144e-09, 9.978399185034293e-10, 2.28338005035252e-10, 4.917751642537547e-11, 1.0003026011983666e-11, 1.927591969550228e-12, 3.5287624532736836e-13, 6.152341588359429e-14, 1.0238941709122385e-14], [7.025875644162582e-07, 2.572395669429559e-06, 4.709177770316669e-06, 5.747263931436695e-06, 5.260638530010091e-06, 3.852172870231659e-06, 2.3506708893315575e-06, 1.229507267588699e-06, 5.549514059470961e-07, 2.172610649802553e-07, 7.95461592257481e-08, 2.647669918191875e-08, 8.078298678322608e-09, 2.27517006572927e-09, 5.950084598209848e-10, 1.4523429892938166e-10, 3.323429887427828e-11, 7.1577233869733306e-12, 1.4559273918422856e-12, 2.8055849753877257e-13, 5.136067734774303e-14, 8.954652953748204e-15, 1.4902646139207184e-15], [9.089840338544045e-08, 3.328078535250507e-07, 6.092574965166695e-07, 7.435615739034224e-07, 6.806036249206096e-07, 4.983811003824031e-07, 3.0412185120640524e-07, 1.5906949287874707e-07, 7.280047629358811e-08, 2.920825113370001e-08, 1.0291413106737884e-08, 3.425465813008802e-09, 1.0451429673969999e-09, 2.943538099439105e-10, 7.698018259616375e-11, 1.87899225066032e-11, 4.299741211355448e-12, 9.26042048995092e-13, 1.8836296294761155e-13, 3.6297709743384005e-14, 6.644870766512198e-15, 1.1585227202857032e-15, 1.9280539663374446e-16], [1.0584115263125103e-08, 3.875179927248977e-08, 7.094130730450588e-08, 8.657953396665595e-08, 7.924877606611871e-08, 5.80309754071586e-08, 3.5411631088331664e-08, 1.852188580624934e-08, 8.47681151267792e-09, 3.448476955466835e-09, 1.2452059033799373e-09, 3.9885766575067136e-10, 1.2169535680916344e-10, 3.4274250553947423e-11, 8.963492154194632e-12, 2.1878789746369885e-12, 5.006573810721582e-13, 1.0782737011896202e-13, 2.1932786901520158e-14, 4.2264674560056224e-15, 7.73721819987441e-16, 1.3489717695544439e-16, 2.2450059245495687e-17], [1.1203666724295734e-09, 4.10201734601659e-09, 7.509392559193032e-09, 9.164755103213487e-09, 8.388768010175473e-09, 6.142787488461633e-09, 3.748448528897019e-09, 1.96060823715378e-09, 8.973009903208008e-10, 3.6503369015708126e-10, 1.3365039908386932e-10, 4.387240250682295e-11, 1.2881891265246371e-11, 3.6280527080924384e-12, 9.488178868507969e-13, 2.315948594241699e-13, 5.299638468728275e-14, 1.1413914989937839e-14, 2.3216643873460265e-15, 4.473867831271874e-16, 8.190123777899344e-17, 1.4279351415631705e-17, 2.376419525621854e-18], [1.0871193879020618e-10, 3.980288503847399e-10, 7.286548630336371e-10, 8.892787694650059e-10, 8.139828298085705e-10, 5.960498057289929e-10, 3.637211968720953e-10, 1.9024264815627482e-10, 8.70673260251573e-11, 3.5420118392725776e-11, 1.296842753541078e-11, 4.316501991543566e-12, 1.29886657966026e-12, 3.520388937261785e-13, 9.206613743221688e-14, 2.2472219855709255e-14, 5.1423697883946665e-15, 1.1075202951654543e-15, 2.2527681604562213e-16, 4.34110419202311e-17, 7.947078904948186e-18, 1.3855606519369916e-18, 2.3058984202825214e-19], [9.737157494008593e-12, 3.565081854380978e-11, 6.526447084920333e-11, 7.9651301694373e-11, 7.290716272258114e-11, 5.3387244282863394e-11, 3.257793594029767e-11, 1.7039734989454493e-11, 7.798483547655457e-12, 3.172524334350963e-12, 1.1615616717646893e-12, 3.8662229910159556e-13, 1.1796222732988453e-13, 3.2765247638283085e-14, 8.246219228713614e-15, 2.0128014127068547e-15, 4.605939796424778e-16, 9.91988521393977e-17, 2.0177690343819364e-17, 3.8882587953107175e-18, 7.118073670282582e-19, 1.2410248989715515e-19, 2.0653569730557787e-20], [8.098460432859205e-13, 2.965102942555238e-12, 5.428090643177797e-12, 6.624653196731398e-12, 6.0637385494088415e-12, 4.440253592593029e-12, 2.70952919637031e-12, 1.4172064042654581e-12, 6.486052062509184e-13, 2.638610170353437e-13, 9.660787806811483e-14, 3.2155640839350743e-14, 9.810999064057755e-15, 2.7631673789606655e-15, 7.126774218510249e-16, 1.6740606907138507e-16, 3.830791606321401e-17, 8.250436326312685e-18, 1.6781922956104353e-18, 3.2338914129627867e-19, 5.920150517482173e-20, 1.0321688898118722e-20, 1.7177715094280796e-21], [6.286508562149208e-14, 2.301689955833533e-13, 4.2136080786421337e-13, 5.142451381690301e-13, 4.707035939179679e-13, 3.446789974387117e-13, 2.1032983532601464e-13, 1.1001202350262057e-13, 5.034860905175012e-14, 2.0482467705586485e-14, 7.499280359289858e-15, 2.4961128492740465e-15, 7.615883306558499e-16, 2.1449355134226176e-16, 5.609491771542983e-17, 1.3503492235537624e-17, 2.9736891885321486e-18, 6.404481325411603e-19, 1.3027130678420952e-19, 2.5103396164243265e-20, 4.595574334889237e-21, 8.012311249998283e-22, 1.3334368169559633e-22], [4.574965617263776e-15, 1.6750398580447942e-14, 3.066425805967924e-14, 3.742385463584028e-14, 3.4255147142613285e-14, 2.5083789303485053e-14, 1.5306616628106492e-14, 8.006053281156062e-15, 3.664087195803702e-15, 1.4905982324429978e-15, 5.457552385205567e-16, 1.8165298510839827e-16, 5.5424094198141846e-17, 1.5609628346392745e-17, 4.082271062136209e-18, 9.964325144678296e-19, 2.2487529737006164e-19, 4.660819526530471e-20, 9.480409412661741e-21, 1.826883288117256e-21, 3.344399258482883e-22, 5.830907270891565e-23, 9.703999493610157e-24], [3.1335542575081613e-16, 1.1472934919697566e-15, 2.10030248169834e-15, 2.5632909367445964e-15, 2.3462550574205886e-15, 1.7180766226912914e-15, 1.0484038070593194e-15, 5.4836264234064765e-16, 2.5096617095799787e-16, 1.0209629597827404e-16, 3.7380688606055407e-17, 1.2442049459946113e-17, 3.796190416989254e-18, 1.0691581413941561e-18, 2.796090492743421e-19, 6.82491544034309e-20, 1.5617611074525018e-20, 3.317260098200929e-21, 6.493464599135987e-22, 1.251296377801887e-22, 2.2906962394821303e-23, 3.993792704122106e-24, 6.646609280147064e-25], [2.027043270868277e-17, 7.421647629160945e-17, 1.3586501660577914e-16, 1.6581495699830704e-16, 1.5177527290263237e-16, 1.111394720074799e-16, 6.781946976537205e-17, 3.547265222833828e-17, 1.6234577296278464e-17, 6.604436774868811e-18, 2.4180935472163188e-18, 8.048551440641e-19, 2.455691399392552e-19, 6.916203256459534e-20, 1.8087436668677358e-20, 4.414922411011239e-21, 1.0102768560589178e-21, 2.175849205450657e-22, 4.3648581202663134e-23, 8.094424714069462e-24, 1.4818126690226701e-24, 2.5835169781203157e-25, 4.299579170563526e-26], [1.2422463358255662e-18, 4.548257408024909e-18, 8.3263056823209e-18, 1.0161747690170847e-17, 9.301344443005352e-18, 6.811033777672706e-18, 4.156225425694966e-18, 2.1738940103529415e-18, 9.949143390185368e-19, 4.0474406746423823e-19, 1.4818962633324654e-19, 4.9324470175504115e-20, 1.5049376037774728e-20, 4.238502589775259e-21, 1.1084643455350064e-21, 2.70562610421417e-22, 6.191346483052545e-23, 1.333440061011748e-23, 2.712303626792956e-24, 5.154642456665256e-25, 9.081090595983301e-26, 1.5832737987079976e-26, 2.6349395432178465e-27], [7.232293370335815e-20, 2.647971738775832e-19, 4.84753173738438e-19, 5.916116500501202e-19, 5.415194217952872e-19, 3.9653483383115828e-19, 2.4197327635422935e-19, 1.2656297535737714e-19, 5.792339386015452e-20, 2.3563988489118774e-20, 8.62752274789542e-21, 2.8716449254692445e-21, 8.761668230106346e-22, 2.4676340993037296e-22, 6.453421601069749e-23, 1.5752014050507408e-23, 3.6045696277360944e-24, 7.763218481611699e-25, 1.5790890238654681e-25, 3.0429185308140285e-26, 5.493816787824368e-27, 9.217737470895739e-28, 1.5340480579470198e-28], [4.010098548406553e-21, 1.4682241278320115e-20, 2.6878168497936903e-20, 3.280316350021397e-20, 3.0025693595092737e-20, 2.198671541811539e-20, 1.3416721841528637e-20, 7.017552770250336e-21, 3.2116855020028228e-21, 1.3065553510655822e-21, 4.7837130874122e-22, 1.5922444731564537e-22, 4.858092896961376e-23, 1.368232096364327e-23, 3.578236566128632e-24, 8.734038491511906e-25, 1.998630129013101e-25, 4.304481244049492e-26, 8.755594219090159e-27, 1.6872107585384282e-27, 3.088706567333869e-28, 5.310937609794281e-29, 8.505855024619386e-30], [2.12241677981611e-22, 7.770840261967567e-22, 1.4225754091109317e-21, 1.7361664259241304e-21, 1.5891638358155663e-21, 1.1636864574062003e-21, 7.101041339221155e-22, 3.71416601687823e-22, 1.69984231525969e-22, 6.915179184217348e-23, 2.531866188321975e-23, 8.427240245104587e-24, 2.571233040273637e-24, 7.241614451496543e-25, 1.8938460585016615e-25, 4.6226469564720795e-26, 1.0578109418655077e-26, 2.2782241160643285e-27, 4.634055712980422e-28, 8.929866390518391e-29, 1.634753502265552e-29, 2.850166904653512e-30, 4.6780133284194665e-31]] |
| Legacy trial inputs | {"lambda_home": 1.1643895677952476, "lambda_away": 3.6613168232871054, "rho": -0.021898200937208512, "max_goals": 22, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0783 |
| Legacy p draw | 0.1061 |
| Legacy p away | 0.8156 |
| Legacy p over 1 5 | 0.9536 |
| Legacy p under 3 5 | 0.2916 |
| Legacy p btts yes | 0.6723 |
| Legacy p over 2 5 | 0.8586 |
| Legacy goal margin distribution | {"-1": 0.15415661051430993, "-10": 0.001390127424867126, "-11": 0.00044858864267885163, "-12": 0.0001333074960516296, "-13": 3.670179872614625e-05, "-14": 9.410591461133281e-06, "-15": 2.2575199375427213e-06, "-16": 5.087281623913433e-07, "-17": 1.080781672752281e-07, "-18": 2.1716022795043426e-08, "-19": 4.138512226177131e-09, "-2": 0.18329756206930028, "-20": 7.493373186768418e-10, "-21": 1.2755802362216423e-10, "-22": 1.778269036517657e-11, "-3": 0.1722282604608212, "-4": 0.13262371165157416, "-5": 0.08595695429828977, "-6": 0.0479157978466606, "-7": 0.023377790838875187, "-8": 0.010125804293661837, "-9": 0.003939458637586173, "0": 0.10607997659716742, "1": 0.051121488789855986, "10": 1.550086306304393e-08, "11": 1.590781519138894e-09, "12": 1.5034113639174713e-10, "13": 1.3163506779662551e-11, "14": 1.0734014233331911e-12, "15": 8.189131330805194e-14, "16": 5.86885008977083e-15, "17": 3.965210087548491e-16, "18": 2.5337835617782145e-17, "19": 1.5356578446270107e-18, "2": 0.019533047220863173, "20": 8.842775039078919e-20, "21": 4.78718257460331e-21, "22": 2.12241677981611e-22, "3": 0.005836852532518906, "4": 0.0014294088892776292, "5": 0.0002946302362179322, "6": 5.223192281057794e-05, "7": 8.104416519491968e-06, "8": 1.1163716737329913e-06, "9": 1.3812643999651378e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0749 |
| Legacy raw p draw | 0.1029 |
| Legacy raw p away | 0.8222 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1644 |
| Legacy lambda away | 3.6613 |
| Legacy model home team | Santander |
| Legacy model away team | Real Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.014687134269420648, "mu": 10.724054049657926, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,438.0702 |
| Elo away rating | 1,670.4419 |
| Elo rating diff | -172.3717 |
| Elo home expectancy | 0.2705 |

</details>


---
