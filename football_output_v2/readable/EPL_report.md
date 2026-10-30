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
| Training sha256 | 1df0a1867f19626bd88cf76148d059a2e141190dcb5889a973c5a54fd68855a3 |
| Training as of utc | 2026-10-30T11:41:52.235573+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 80, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 80, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 186, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-30T11:41:52.235573+00:00', 'observations': 461, 'observations_sha256': '985e047814125cf51dc6b0b4f1c2810401369e3f227cd2521b5e3daaa35dfd72', 'eligible_training_matches': 243, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 222, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 18, 'retrospective_eligible_training_matches': 243, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '8bd4d61a2607de62687827179bc80eba3a30b1da2cacdd4d50ac83632b36afad', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 182, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-21T00:00:00+00:00', 'audit_origin_utc': '2025-10-19T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 31, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1979, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1609, 'tuning_matches': 249, 'audit_matches': 114, 'audit_matchdays': 38, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.929183161468839, 'audit_candidate_poisson_score': 0.9172218058913034, 'audit_gain': 0.011961355577535526, 'audit_gain_lower95': 0.0018326111823448584, 'audit_baseline_briers': [0.6363694338550931, 0.15621482628659347, 0.217284511347824, 0.25224717235003363], 'audit_candidate_briers': [0.6347830434102995, 0.15464916228694495, 0.21528056259496078, 0.24898494343162267], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1867.018 |
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
| Bbs statistics model artifact | bbs/feature_models/EPL/20261030T114152235573Z_64fe8d44c3181b2aaf6a3b7f6d5d91148302e5bda0f962811f0fb53987b7fb58.json |
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

The model's most likely 1X2 outcome is **Aston Villa win** at **48.5%**. Expected goals are 1.56 for Aston Villa and 1.15 for Fulham (2.72 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 55.6%; Under 3.5 goals: 66.7%; Double Chance 1X: 74.4%; Double Chance X2: 51.5%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 48.5% | 2.06 |
| Draw | 25.9% | 3.86 |
| Fulham win | 25.6% | 3.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.56 |
| Fulham expected goals | 1.15 |
| Expected total goals | 2.72 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 55.6% |
| Under 2.5 | 44.4% |
| Over 3.5 | 33.3% |
| Under 3.5 | 66.7% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.19% |
| 2 | 2-1 | 9.77% |
| 3 | 1-0 | 8.57% |
| 4 | 2-0 | 7.92% |
| 5 | 1-2 | 6.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 48.5% | 49.6% | 1.97 | -4.4% |
| Draw | 25.9% | 25.5% | 3.75 | -2.8% |
| Fulham win | 25.6% | 24.9% | 3.84 | -1.8% |

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
| Market best home last update utc | 2026-10-30T11:42:07Z |
| Market best draw last update utc | 2026-10-30T11:42:07Z |
| Market best away last update utc | 2026-10-30T11:42:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Aston Villa |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5969 |
| Dc lambda away | 1.1022 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:41:52.235573+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.4880 |
| Shot lambda away | 1.2702 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.77 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.90 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 3.00 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.88 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.1465764406693792, "-10": 1.3882453974521863e-07, "-11": 1.5340111243566815e-08, "-12": 1.5574144585166415e-09, "-13": 1.4616975826474887e-10, "-14": 1.2664019530907027e-11, "-15": 9.158380152117593e-13, "-2": 0.07349411073458469, "-3": 0.026133231752720722, "-4": 0.007350999166959206, "-5": 0.0017026376835701106, "-6": 0.0003343694533306689, "-7": 5.691463299743041e-05, "-8": 8.541304823571505e-06, "-9": 1.145547691217403e-06, "0": 0.259230938621776, "1": 0.22351530335093303, "10": 3.259178653874576e-06, "11": 4.88753363240979e-07, "12": 6.734180874788452e-08, "13": 8.577434857814837e-09, "14": 1.0085345861939726e-09, "15": 9.898222594107982e-11, "2": 0.14994771942245705, "3": 0.07236020195513991, "4": 0.027623095755218176, "5": 0.008682954824014225, "6": 0.002314148478615431, "7": 0.0005345740709875729, "8": 0.00010887483163008556, "9": 1.9816902579172366e-05} |
| Raw goal margin distribution | {"-1": 0.15983787270594813, "-10": 8.867997569316536e-08, "-11": 9.168236646359287e-09, "-12": 8.706369682086223e-10, "-13": 7.642176048666152e-11, "-14": 6.201320275697901e-12, "-15": 4.2538081928410424e-13, "-2": 0.07699305096441499, "-3": 0.02598346860794062, "-4": 0.006899130876026215, "-5": 0.0015036334331171852, "-6": 0.00027730670951367893, "-7": 4.426942342577963e-05, "-8": 6.225245328433981e-06, "-9": 7.818334009317409e-07, "0": 0.26904185917870876, "1": 0.2201423373309501, "10": 1.879398235106631e-06, "11": 2.636928710560068e-07, "12": 3.398357024080022e-08, "13": 4.048258739691881e-09, "14": 4.4581503478519497e-10, "15": 4.1501880665182775e-11, "2": 0.14180455436476724, "3": 0.06494640263470179, "4": 0.0234030081182348, "5": 0.006922111623267132, "6": 0.0017325123022928271, "7": 0.00037535235080845864, "8": 7.163265867680057e-05, "9": 1.2209226326365338e-05} |
| Unadjusted home-win probability | 45.9% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 27.2% |
| Raw p over 1 5 | 76.3% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 55.0% |
| P home draw | 74.4% |
| P draw away | 51.5% |
| P home away | 74.1% |
| Raw p home draw | 72.8% |
| Raw p draw away | 54.1% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0709 |
| Totals anchor target over 2 5 | 0.5561 |
| Totals anchor reference over odds | 1.75 |
| Totals anchor reference under odds | 2.17 |
| Totals anchor reference last update utc | 2026-10-30T11:42:07Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5146 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.85, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.22, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.32, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.99, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.53, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.8, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.55, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.8, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.97 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.84 |
| Market reference 1x2 last update utc | 2026-10-30T11:42:07Z |
| Market reference home last update utc | 2026-10-30T11:42:07Z |
| Market reference draw last update utc | 2026-10-30T11:42:07Z |
| Market reference away last update utc | 2026-10-30T11:42:07Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-30T11:41:26Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:41:26Z |
| Home probability edge | -1.1% |
| Draw probability edge | +0.4% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.0367 |
| Raw ev home | -0.0950 |
| Raw edge prob draw | 0.0140 |
| Raw ev draw | 0.0089 |
| Raw edge prob away | 0.0227 |
| Raw ev away | 0.0427 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.0842939755519181, 0.06684853706888329, 0.04100060872787535, 0.014091998802152313, 0.003632588083470015, 0.0007491170766862648, 0.00012873658800286944, 1.8963019960128512e-05, 2.444111772250712e-06, 2.800155187571389e-07, 2.8872583681131118e-08, 2.7064282077326175e-09, 2.3255132207067453e-10, 1.84450148072155e-11, 1.3584839763902097e-12, 9.33827821683953e-14], [0.10654209266624427, 0.12759861124043828, 0.06354972246457931, 0.02184217846109941, 0.005630403345102242, 0.0011611091589604319, 0.00019953787742319675, 2.9392116189170846e-05, 3.7883004574354915e-06, 4.3401571476408437e-07, 4.475164483408648e-08, 4.194883120229939e-09, 3.6044762345966733e-10, 2.8589223629176653e-11, 2.1056097055817935e-12, 1.4474053127257829e-13], [0.09236453590791754, 0.0952376783975015, 0.04622672006949334, 0.016927363059868025, 0.004363478751251068, 0.0008998423083515062, 0.0001546388837245991, 2.277845237452e-05, 2.935876443692739e-06, 3.363557161014966e-07, 3.4681858358679463e-08, 3.2509719530178227e-09, 2.793415408282164e-10, 2.2156222596236042e-11, 1.6318161676154897e-12, 1.1217175643412406e-13], [0.04772075996461268, 0.04920518839530663, 0.025367896140097334, 0.008208758363650776, 0.0022544207043570567, 0.0004649095930677899, 7.989522146004385e-05, 1.1768640933935033e-05, 1.5168403508777034e-06, 1.7378044758225235e-07, 1.7918615858268683e-08, 1.6796365693464498e-09, 1.4432368968213134e-10, 1.1447161725487263e-11, 8.430888205705559e-13, 5.795429393959609e-14], [0.018491439186170675, 0.019066644150902062, 0.009829870880169478, 0.003378548098835468, 0.0008199443740865243, 0.00018014900587617178, 3.095880346393452e-05, 4.560260739667891e-06, 5.877643424828996e-07, 6.733862957328579e-08, 6.943330233827681e-09, 6.508466650566743e-10, 5.5924355204315956e-11, 4.435689939935481e-12, 3.266906408381069e-13, 2.2456857408729217e-14], [0.005732236006793001, 0.005910546119755178, 0.003047201423000879, 0.001047329786927054, 0.0002699771520611633, 5.241689400029659e-05, 9.597044673294764e-06, 1.4136536669270528e-06, 1.8220344525748108e-07, 2.0874574077325796e-08, 2.152391015793277e-09, 2.017585895168829e-10, 1.7336217010010216e-11, 1.3750374609934893e-12, 1.0127215278597685e-13, 6.961492036488241e-15], [0.0014807991825639111, 0.0015268617433524707, 0.0007871785758541665, 0.00027055499643045697, 6.974275755731985e-05, 1.438244289219576e-05, 2.32699625008376e-06, 3.651868471453968e-07, 4.706831897323683e-08, 5.392494690281878e-09, 5.560236621394376e-10, 5.2119967509676314e-11, 4.478436677546367e-12, 3.552111856212768e-13, 2.6161470128628194e-14, 1.79835088870046e-15], [0.00032788494748696976, 0.0003380843185449156, 0.00017430047844834708, 5.9907455272456495e-05, 1.5442742451872818e-05, 3.184622592968249e-06, 5.472808716484308e-07, 7.589733114867106e-08, 1.0422070376969306e-08, 1.194029453261482e-09, 1.2311715957760094e-10, 1.1540628203443251e-11, 9.91634782171169e-13, 7.865239413663024e-14, 5.792785652714229e-15, 3.981986171033331e-16], [6.352648795840776e-05, 6.550257813168926e-05, 3.377006883103002e-05, 1.1606846441573223e-05, 2.991973861357807e-06, 6.17008771994056e-07, 1.0603363151955177e-07, 1.561885321137573e-08, 1.8952802277352495e-09, 2.3133876155633565e-10, 2.3853491339948287e-11, 2.235953752124085e-12, 1.92125547487167e-13, 1.5238608564728774e-14, 1.1223306554120233e-15, 7.714949968990202e-17], [1.0940462712803942e-05, 1.1280782814744402e-05, 5.815844551277579e-06, 1.9989184793343606e-06, 5.152744865936953e-07, 1.0626058012043003e-07, 1.8260996778263033e-08, 2.6898619248035833e-09, 3.4669178274159464e-10, 3.739515298486173e-11, 4.108022353537912e-12, 3.8507352505751143e-13, 3.308765297770883e-14, 2.6243766050247206e-15, 1.932865656765297e-16, 1.3286602987111016e-17], [1.6957391380388799e-06, 1.7484877403120205e-06, 9.014385849338522e-07, 3.0982641119826105e-07, 7.986601085228502e-08, 1.6470073457683607e-08, 2.830400116465114e-09, 4.1692058750602966e-10, 5.3736193821433096e-11, 6.156415741611698e-12, 5.976435207315423e-13, 5.968524957343997e-14, 5.1284876712284476e-15, 4.067705579660498e-16, 2.99588420415914e-17, 2.0593838933759366e-18], [2.3894046928543136e-07, 2.4637308406595175e-07, 1.270184509423945e-07, 4.365651911198393e-08, 1.1253630753059137e-08, 2.3207384867555123e-09, 3.9882144424398354e-10, 5.874677218847349e-11, 7.571772733956755e-12, 8.674782774183917e-13, 8.944625379155863e-14, 7.893756880605133e-15, 7.226366505316679e-16, 5.731656823366674e-17, 4.2213920856627845e-18, 2.901803366354942e-19], [3.086255094696087e-08, 3.1822578576516264e-08, 1.6406234679027294e-08, 5.638858705224472e-09, 1.4535660430116589e-09, 2.997562949309563e-10, 5.151344675320321e-11, 7.587978943284068e-12, 9.780018531787393e-13, 1.1204712459246578e-13, 1.1553252460382129e-14, 1.0829667581938234e-15, 8.760888550615569e-17, 7.403247815268077e-18, 5.452526677481029e-19, 3.748090664591844e-20], [3.679694987055277e-09, 3.7941576204902305e-09, 1.9560903960472522e-09, 6.723125429905768e-10, 1.7330646747301613e-10, 3.573948691705019e-11, 6.141869870363608e-12, 9.047031830734944e-13, 1.1660567276688316e-13, 1.3359208167381081e-14, 1.3774767107136521e-15, 1.2912047867079277e-16, 1.109474765874068e-17, 8.284920630510034e-19, 6.500964588569706e-20, 4.468791466145936e-21], [4.073869744814638e-10, 4.200593796917563e-10, 2.1656298988402194e-10, 7.443317279241539e-11, 1.9187133088550647e-11, 3.9567957387437176e-12, 6.799796703119251e-13, 1.00161642161273e-13, 1.2909665720389376e-14, 1.4790267714913959e-15, 1.525034198677955e-16, 1.4295206894685604e-17, 1.22832346083846e-18, 9.742556705968789e-20, 6.75552619188401e-21, 4.947495489126608e-22], [4.209584518742381e-11, 4.3405301898855926e-11, 2.2377745648562008e-11, 7.691280072629941e-12, 1.9826323242518783e-12, 4.088610370236383e-13, 7.026321587350775e-14, 1.0349837491750579e-14, 1.333973159742323e-15, 1.528298298687749e-16, 1.5758383933307403e-17, 1.4771429968442925e-18, 1.2692431885764466e-19, 1.006711516356595e-20, 7.414477451560156e-22, 4.7984786327149496e-23]] |
| Legacy trial inputs | {"lambda_home": 1.549970218402473, "lambda_away": 1.0311065547110887, "rho": -0.10285845637220993, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4885 |
| Legacy p draw | 0.2672 |
| Legacy p away | 0.2443 |
| Legacy p over 1 5 | 0.7423 |
| Legacy p under 3 5 | 0.7392 |
| Legacy p btts yes | 0.5165 |
| Legacy p over 2 5 | 0.4814 |
| Legacy goal margin distribution | {"-1": 0.14977016519266184, "-10": 3.335858915604764e-08, "-11": 3.0898975994665003e-09, "-12": 2.6283031616140627e-10, "-13": 2.0662796269231416e-11, "-14": 1.5032245076627878e-12, "-15": 9.33827821683953e-14, "-2": 0.06770359627701665, "-3": 0.020706887659132332, "-4": 0.004960713973764612, "-5": 0.0009730197909824845, "-6": 0.00016124551073036332, "-7": 2.3106263293486957e-05, "-8": 2.914546307895156e-06, "-9": 3.28166997994369e-07, "0": 0.2672028313204496, "1": 0.23081113815029553, "10": 1.959210365320975e-06, "11": 2.7279555406311155e-07, "12": 3.488096283740775e-08, "13": 4.1221321123955955e-09, "14": 4.507922763803197e-10, "15": 4.209584518742381e-11, "2": 0.15251996112857977, "3": 0.07012123897177254, "4": 0.025252172461632357, "5": 0.007445537226122967, "6": 0.0018547347275997424, "7": 0.00039952475621154836, "8": 7.575385587305743e-05, "9": 1.2821785096290008e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4809 |
| Legacy raw p draw | 0.2794 |
| Legacy raw p away | 0.2398 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5500 |
| Legacy lambda away | 1.0311 |
| Legacy model home team | Aston Villa |
| Legacy model away team | Fulham |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 74.0% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:41:51Z |
| Market reference home draw last update utc | 2026-10-30T11:42:12Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.4% |
| Market draw away odds | 1.89 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:41:51Z |
| Market reference draw away last update utc | 2026-10-30T11:42:12Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.6% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:41:51Z |
| Market reference home away last update utc | 2026-10-30T11:42:12Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.30 |
| Market reference dc draw away odds | 1.87 |
| Market reference dc home away odds | 1.29 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.15, "price": 1.69, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.69, "price": 2.15, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:51Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.72, "price": 2.1, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:51Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.1, "price": 1.72, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 79.3% |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-30T11:42:11Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.0% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market reference under 3 5 last update utc | 2026-10-30T11:42:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.8% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:41:51Z |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-30T11:42:07Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.733840632585078, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,530.3526 |
| Elo away rating | 1,453.3052 |
| Elo rating diff | 137.0473 |
| Elo home expectancy | 0.6876 |

</details>


---

## 2026-10-31 — Bournemouth vs Leeds United

The model's most likely 1X2 outcome is **Bournemouth win** at **45.4%**. Expected goals are 1.64 for Bournemouth and 1.19 for Leeds United (2.83 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 51.2%; Under 3.5 goals: 70.7%; Double Chance 1X: 72.9%; Double Chance X2: 54.6%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 45.4% | 2.20 |
| Draw | 27.4% | 3.65 |
| Leeds United win | 27.1% | 3.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.64 |
| Leeds United expected goals | 1.19 |
| Expected total goals | 2.83 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 76.6% |
| Under 1.5 | 23.4% |
| Over 2.5 | 51.2% |
| Under 2.5 | 48.8% |
| Over 3.5 | 29.3% |
| Under 3.5 | 70.7% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.06% |
| 2 | 1-0 | 9.18% |
| 3 | 2-1 | 9.16% |
| 4 | 2-0 | 7.96% |
| 5 | 0-0 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 45.4% | 44.8% | 2.18 | -1.0% |
| Draw | 27.4% | 28.0% | 3.44 | -5.6% |
| Leeds United win | 27.1% | 27.2% | 3.53 | -4.2% |
| Over 2.5 | 51.2% | 51.2% | 1.90 | -2.7% |
| Under 2.5 | 48.8% | 48.8% | 1.99 | -2.9% |

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
| Market best home last update utc | 2026-10-30T11:42:07Z |
| Market best draw last update utc | 2026-10-30T11:42:07Z |
| Market best away last update utc | 2026-10-30T11:42:07Z |
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
| Dc lambda home | 1.6063 |
| Dc lambda away | 1.1733 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:41:52.235573+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7240 |
| Shot lambda away | 1.2382 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.4% |
| P btts no | 44.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.19 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.27 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.42 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.08 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.1600284853577698, "-10": 8.697116797352729e-08, "-11": 8.97534269803794e-09, "-12": 8.507988103799812e-10, "-13": 7.454789421455353e-11, "-14": 6.037922538946652e-12, "-15": 4.130061718255943e-13, "-2": 0.07682391302873529, "-3": 0.02585193718574036, "-4": 0.006847302854268266, "-5": 0.0014890148835395227, "-6": 0.00027403954842262796, "-7": 4.366110244130979e-05, "-8": 6.127939125099256e-06, "-9": 7.681752304703289e-07, "0": 0.27427762734989136, "1": 0.21581889844560842, "10": 2.0467415843098653e-06, "11": 2.9070927625021883e-07, "12": 3.792755642620205e-08, "13": 4.5738667536487895e-09, "14": 5.098657090366673e-10, "15": 4.800041013495702e-11, "2": 0.14041807731539882, "3": 0.06503390452194459, "4": 0.023707535698810102, "5": 0.007095549826227261, "6": 0.0017972992687655667, "7": 0.00039411411662741117, "8": 7.613105971293769e-05, "9": 1.3134933282586421e-05} |
| Raw goal margin distribution | {"-1": 0.1564053989637433, "-10": 1.1258311193253832e-07, "-11": 1.2031115116182835e-08, "-12": 1.1811403828374127e-09, "-13": 1.0719044084196636e-10, "-14": 8.985440575074433e-12, "-15": 6.319866460644865e-13, "-2": 0.07669622298772978, "-3": 0.02652923156317742, "-4": 0.007243143318551148, "-5": 0.0016262630057290485, "-6": 0.00030933641868490446, "-7": 5.097189799389824e-05, "-8": 7.402379223115322e-06, "-9": 9.60469668847374e-07, "0": 0.2614235596566518, "1": 0.2185433293850943, "10": 2.745836287544468e-06, "11": 4.0385681190299746e-07, "12": 5.4568647227386366e-08, "13": 6.81581612476324e-09, "14": 7.863598371287081e-10, "15": 7.612196464335801e-11, "2": 0.14528281805586923, "3": 0.06916479402009448, "4": 0.02599008112295458, "5": 0.00803140410748318, "6": 0.0021025768962746397, "7": 0.0004768390116869481, "8": 9.530867746389503e-05, "9": 1.702020970554469e-05} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 26.9% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.0% |
| P home draw | 72.9% |
| P draw away | 54.6% |
| P home away | 72.6% |
| Raw p home draw | 73.1% |
| Raw p draw away | 53.0% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9647 |
| Totals anchor target over 2 5 | 0.5121 |
| Totals anchor reference over odds | 1.90 |
| Totals anchor reference under odds | 1.99 |
| Totals anchor reference last update utc | 2026-10-30T11:42:07Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5338 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.23, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.14, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.57, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.52, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:01Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.52, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.52, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.18 |
| Reference draw odds | 3.44 |
| Reference away odds | 3.53 |
| Market reference 1x2 last update utc | 2026-10-30T11:42:07Z |
| Market reference home last update utc | 2026-10-30T11:42:07Z |
| Market reference draw last update utc | 2026-10-30T11:42:07Z |
| Market reference away last update utc | 2026-10-30T11:42:07Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.99 |
| Market reference over 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market best over 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market best under 2 5 last update utc | 2026-10-30T11:42:07Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0219 |
| Raw ev home | 0.0240 |
| Raw edge prob draw | -0.0184 |
| Raw ev draw | -0.1007 |
| Raw edge prob away | -0.0036 |
| Raw ev away | -0.0509 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08648922032886683, 0.07110994264206294, 0.047892882918399736, 0.018302123894502424, 0.005245576983021211, 0.0012027490598757091, 0.0002298135021997654, 3.763823647620306e-05, 5.3937528802431765e-06, 6.870689161250052e-07, 7.876840770938599e-08, 8.209394888737937e-09, 7.842990085216458e-10, 6.916558891234731e-11, 5.663876940606969e-12, 4.328867722029706e-13], [0.09769816212917387, 0.13521913090581203, 0.06933023325904991, 0.026494344074125365, 0.007593551560276704, 0.0017411119939336516, 0.0003326804055779169, 5.448550087912791e-05, 7.808052523504816e-06, 9.946080778045766e-07, 1.1402596267257966e-07, 1.18840050518903e-08, 1.1353593664071735e-09, 1.0012482274167558e-10, 8.199086910509914e-12, 6.266513741242946e-13], [0.0801679316379271, 0.09190781559568527, 0.050870009403438374, 0.01917674341962555, 0.00549625193617596, 0.0012602258760995768, 0.00024079580006417973, 3.943688764385125e-05, 5.651508843974074e-06, 7.199024764599681e-07, 8.2532582170372e-08, 8.601704387926328e-09, 8.217789879132063e-10, 7.247086511297175e-11, 5.934541557932474e-12, 4.5357350918052815e-13], [0.03868397600135368, 0.044348901863875745, 0.025421702987082503, 0.009380430174319259, 0.0026521437394280544, 0.0006081053427634809, 0.00011619283123056942, 1.9029748978344355e-05, 2.727060908582824e-06, 3.4737942658255386e-07, 3.9825006867184466e-08, 4.150638781802612e-09, 3.965385908972564e-10, 3.4969858265636406e-11, 2.8636346044568098e-12, 2.1886590293029814e-13], [0.013999831061177182, 0.016049982396361216, 0.00920018012352516, 0.0035158216881491147, 0.0009729851655040005, 0.00022007489782823936, 4.2050486425979606e-05, 6.886915420072316e-06, 9.869304027167192e-07, 1.257175137869534e-07, 1.4412773085457746e-08, 1.5021269204378947e-09, 1.4350834261722676e-10, 1.2655682237396908e-11, 1.0363567768197713e-12, 7.920813687737152e-14], [0.004053260083392526, 0.004646824143951739, 0.002663655203534308, 0.0010179079766482742, 0.00029174289737726885, 6.459065025875667e-05, 1.2174543919341459e-05, 1.9939140156690135e-06, 2.857381341915866e-07, 3.639799496074495e-08, 4.172815913492019e-09, 4.3489889700771165e-10, 4.1548832569649095e-11, 3.664099332112039e-12, 3.000481603871371e-13, 2.2932503833938816e-14], [0.0009779235449241756, 0.0011211317916932347, 0.0006426558092753255, 0.0002455890212940168, 7.038833988931558e-05, 1.613921784049887e-05, 2.9776291167010776e-06, 4.810684294517323e-07, 6.893958032783744e-08, 8.78168573637443e-09, 1.0067685878727621e-09, 1.0492735780464069e-10, 1.00244200465824e-11, 8.840313560175517e-13, 7.239213734544626e-14, 5.532888337257211e-15], [0.00020223603576407208, 0.0002318517130484789, 0.00013290217205954547, 5.078817291134066e-05, 1.4556412816845533e-05, 3.337614124679197e-06, 6.377296948901335e-07, 1.0085047987843658e-07, 1.4256807196335239e-08, 1.8160656013123838e-09, 2.0820123331723953e-10, 2.1699132816414834e-11, 2.073064895080227e-12, 1.8281899220044744e-13, 1.4970801095055384e-14, 1.1442094931244605e-15], [3.659487244899693e-05, 4.195386758860628e-05, 2.4048820064825133e-05, 9.190185629312543e-06, 2.634001741256642e-06, 6.039455961206311e-07, 1.1539801377766217e-07, 1.889957591644161e-08, 2.6151791291063924e-09, 3.286194213011973e-10, 3.767428266768761e-11, 3.926486170827202e-12, 3.751237761723944e-13, 3.3081333282434143e-14, 2.7089858365893834e-15, 2.070461888635369e-16], [5.886124034330071e-06, 6.748094796356246e-06, 3.868146773243541e-06, 1.4782008760392364e-06, 4.2366757739861845e-07, 9.714198877747114e-08, 1.856126219205522e-08, 3.0399135342105e-09, 4.3563524532306084e-10, 5.358211711599151e-11, 6.059742413243447e-12, 6.315580045478239e-13, 6.033700699064757e-14, 5.320986736401541e-15, 4.3572843883065883e-16, 3.330246744771786e-17], [8.520814104824384e-07, 9.768611905920976e-07, 5.599569324864866e-07, 2.139858895405088e-07, 6.133055722577542e-08, 1.4062374889114549e-08, 2.6869475357124085e-09, 4.4006103114161555e-10, 6.306300922742695e-11, 8.033114300838336e-12, 8.892488573990774e-13, 9.142499073719098e-14, 8.734447612898663e-15, 7.702715500162578e-16, 6.307650001609175e-17, 4.820899673519467e-18], [1.1213471576312957e-07, 1.285558522923965e-07, 7.36908594548669e-08, 2.816074450839102e-08, 8.07115906708121e-09, 1.850621773631489e-09, 3.5360482517387614e-10, 5.791244596869634e-11, 8.299151381417075e-12, 1.0571654043094559e-12, 1.2119779199522796e-13, 1.2196673330699764e-14, 1.1494615284070016e-15, 1.0136846111053436e-16, 8.300926781905498e-18, 6.344349353973041e-19], [1.3527281310845674e-08, 1.5508231918010235e-08, 8.889637603306263e-09, 3.3971487803343774e-09, 9.736577870819326e-10, 2.2324827027492738e-10, 4.265683388455336e-11, 6.986221373874394e-12, 1.0011614566791946e-12, 1.2753029888082176e-13, 1.462059822790291e-14, 1.523786856340563e-15, 1.4056666673463208e-16, 1.222850283391531e-17, 1.0013756306901855e-18, 7.653454852176471e-20], [1.506325577305876e-09, 1.7269136244073407e-09, 9.899024192026058e-10, 3.782882886917079e-10, 1.0842131500944329e-10, 2.4859731373723828e-11, 4.750036496666434e-12, 7.779481850318752e-13, 1.1148397631086158e-13, 1.4201090867506715e-14, 1.6280714919815839e-15, 1.696807409651489e-16, 1.6210748624938356e-17, 1.3803813672388317e-18, 1.1150782558133482e-19, 8.522477306172364e-21], [1.5575517887136424e-10, 1.78564146103152e-10, 1.0235664234279255e-10, 3.911528885773863e-11, 1.1210844167545619e-11, 2.5705146119431273e-12, 4.911572871961899e-13, 8.044041775418123e-14, 1.1527525611458954e-14, 1.4684032997654239e-15, 1.6834379650015602e-16, 1.7545114122885106e-17, 1.6762033983595339e-18, 1.478206575868894e-19, 1.1688168492884776e-20, 8.812304572456129e-22], [1.50315206553137e-11, 1.7232753799247548e-11, 9.878169026115847e-12, 3.774913146799754e-12, 1.0819289405916958e-12, 2.480735713842295e-13, 4.7400291669240395e-14, 7.763092115175508e-15, 1.1124910297615795e-15, 1.4171172150226842e-16, 1.6246414871224876e-17, 1.6932325926433171e-18, 1.6176595980642958e-19, 1.426578097691681e-20, 1.168205594508926e-21, 8.621193485037822e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4476103553251385, "lambda_away": 1.1464411481985157, "rho": -0.10285845637220993, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T11:42:07Z", "over": 1.9, "under": 1.99, "bookmaker": "pinnacle", "event_id": "a6c06eabdf4e6710354b6098d39449e7", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Bournemouth", "away_team": "Leeds United"}} |
| Legacy p home | 0.4375 |
| Legacy p draw | 0.2830 |
| Legacy p away | 0.2795 |
| Legacy p over 1 5 | 0.7447 |
| Legacy p under 3 5 | 0.7368 |
| Legacy p btts yes | 0.5337 |
| Legacy p over 2 5 | 0.4814 |
| Legacy goal margin distribution | {"-1": 0.1625018081619224, "-10": 9.151022089673579e-08, "-11": 9.420167962999415e-09, "-12": 8.905772387241842e-10, "-13": 7.781824933203776e-11, "-14": 6.290528314731264e-12, "-15": 4.328867722029706e-13, "-2": 0.0805356994658668, "-3": 0.02727927580953811, "-4": 0.007247538883243294, "-5": 0.001577723411369705, "-6": 0.0002903127492314137, "-7": 4.620756105799724e-05, "-8": 6.475191424978224e-06, "-9": 8.101060830396945e-07, "0": 0.28299944777745867, "1": 0.21885204158837046, "10": 9.899166475845717e-07, "11": 1.2867304731814075e-07, "12": 1.5360326490742605e-08, "13": 1.6947678924351439e-09, "14": 1.729879326706118e-10, "15": 1.50315206553137e-11, "2": 0.13480876605805253, "3": 0.057658381990707754, "4": 0.019342833076921136, "5": 0.005316922323430921, "6": 0.0012353655035389696, "7": 0.0002482803352543892, "8": 4.3932083938786896e-05, "9": 6.940184272387282e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4273 |
| Legacy raw p draw | 0.2862 |
| Legacy raw p away | 0.2865 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4476 |
| Legacy lambda away | 1.1464 |
| Legacy model home team | Bournemouth |
| Legacy model away team | Leeds |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 73.4% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:41:52Z |
| Market reference home draw last update utc | 2026-10-30T11:42:12Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.3% |
| Market draw away odds | 1.74 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:41:52Z |
| Market reference draw away last update utc | 2026-10-30T11:42:12Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.3% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:41:52Z |
| Market reference home away last update utc | 2026-10-30T11:42:12Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.31 |
| Market reference dc draw away odds | 1.77 |
| Market reference dc home away odds | 1.33 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:52Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.52, "price": 1.5, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:52Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.5, "price": 2.52, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:52Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.93, "price": 1.89, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:52Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.89, "price": 1.93, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:52Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.57, "price": 2.35, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:52Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.35, "price": 1.57, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 75.6% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market reference over 1 5 last update utc | 2026-10-30T11:42:11Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.30 |
| Market reference under 3 5 last update utc | 2026-10-30T11:42:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.3% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:41:52Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.26 |
| Market reference btts yes last update utc | 2026-10-30T11:42:07Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.998287458206503, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,502.9673 |
| Elo away rating | 1,455.9965 |
| Elo rating diff | 106.9708 |
| Elo home expectancy | 0.6493 |

</details>


---

## 2026-10-31 — Brentford vs Nottingham Forest

The model's most likely 1X2 outcome is **Brentford win** at **46.1%**. Expected goals are 1.58 for Brentford and 1.20 for Nottingham Forest (2.78 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 55.2%; Under 3.5 goals: 67.2%; Double Chance 1X: 71.9%; Double Chance X2: 53.9%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 58.3%; BTTS No (at least one team does not score): 41.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 46.1% | 2.17 |
| Draw | 25.8% | 3.87 |
| Nottingham Forest win | 28.1% | 3.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.58 |
| Nottingham Forest expected goals | 1.20 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 79.3% |
| Under 1.5 | 20.7% |
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 32.8% |
| Under 3.5 | 67.2% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.16% |
| 2 | 2-1 | 9.42% |
| 3 | 1-0 | 8.33% |
| 4 | 2-0 | 7.55% |
| 5 | 1-2 | 7.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 46.1% | 46.5% | 2.10 | -3.2% |
| Draw | 25.8% | 25.5% | 3.76 | -2.9% |
| Nottingham Forest win | 28.1% | 28.1% | 3.42 | -3.9% |

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
| Market best home last update utc | 2026-10-30T11:42:07Z |
| Market best draw last update utc | 2026-10-30T11:42:07Z |
| Market best away last update utc | 2026-10-30T11:42:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Brentford |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6216 |
| Dc lambda away | 1.1275 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:41:52.235573+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.4728 |
| Shot lambda away | 1.3686 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.3% |
| P btts no | 41.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.69 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.05 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.99 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.15982171806198842, "-10": 1.685213973668326e-07, "-11": 1.8837303306892907e-08, "-12": 1.9345816278056385e-09, "-13": 1.8366648427519375e-10, "-14": 1.6098341770815246e-11, "-15": 1.1788440553311271e-12, "-2": 0.08114508072247396, "-3": 0.029217602195135875, "-4": 0.008319045488405582, "-5": 0.0019499691021769602, "-6": 0.00038748003355596584, "-7": 6.673033661267866e-05, "-8": 1.0131459642695792e-05, "-9": 1.3746402067785453e-06, "0": 0.25822612409548595, "1": 0.21582643503609458, "10": 2.6295564156176032e-06, "11": 3.863187439637472e-07, "12": 5.214512555467771e-08, "13": 6.506631028122871e-09, "14": 7.495610638772608e-10, "15": 7.214094749546386e-11, "2": 0.14219776450762608, "3": 0.06729375344770772, "4": 0.02518275779611627, "5": 0.0077581313465861544, "6": 0.0020261814518592503, "7": 0.0004586188816299641, "8": 9.151667708580108e-05, "9": 1.6319876765220468e-05} |
| Raw goal margin distribution | {"-1": 0.16254733136761285, "-10": 1.2578881817496693e-07, "-11": 1.3528745936215815e-08, "-12": 1.3366125706898317e-09, "-13": 1.2206751675124226e-10, "-14": 1.0300987785893137e-11, "-15": 7.316660797778909e-13, "-2": 0.08064849942971541, "-3": 0.028175924672057394, "-4": 0.007759298830976736, "-5": 0.001755843265520807, "-6": 0.0003364431605383688, "-7": 5.582844877747787e-05, "-8": 8.162853952199585e-06, "-9": 1.0661777812380777e-06, "0": 0.2667454193868952, "1": 0.21644183493022942, "10": 1.934809107120141e-06, "11": 2.7349742120311524e-07, "12": 3.5514102568972554e-08, "13": 4.262800633762614e-09, "14": 4.727955636416895e-10, "15": 4.4137430903745954e-11, "2": 0.13931423946245586, "3": 0.06397009613533487, "4": 0.02315372722065404, "5": 0.006886265918056733, "6": 0.0017342406261689441, "7": 0.0003782272553283991, "8": 7.268401263066486e-05, "9": 1.247745767198977e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 28.1% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.3% |
| P home draw | 71.9% |
| P draw away | 53.9% |
| P home away | 74.2% |
| Raw p home draw | 71.9% |
| Raw p draw away | 54.8% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0405 |
| Totals anchor target over 2 5 | 0.5523 |
| Totals anchor reference over odds | 1.76 |
| Totals anchor reference under odds | 2.15 |
| Totals anchor reference last update utc | 2026-10-30T11:42:07Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5282 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.34, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.08, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.32, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.53, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:00Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.10 |
| Reference draw odds | 3.76 |
| Reference away odds | 3.42 |
| Market reference 1x2 last update utc | 2026-10-30T11:42:07Z |
| Market reference home last update utc | 2026-10-30T11:42:07Z |
| Market reference draw last update utc | 2026-10-30T11:42:07Z |
| Market reference away last update utc | 2026-10-30T11:42:07Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-30T11:41:26Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:41:26Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.4% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | -0.0127 |
| Raw ev home | -0.0509 |
| Raw edge prob draw | 0.0122 |
| Raw ev draw | 0.0030 |
| Raw edge prob away | 0.0005 |
| Raw ev away | -0.0380 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.0784032023648123, 0.06677425649200731, 0.042908127710290705, 0.01535797202934678, 0.004122773191947553, 0.0008853907929907517, 0.00015845257949267206, 2.4306187066106238e-05, 3.2624390851578875e-06, 3.892382080119367e-07, 4.179564453449704e-08, 4.079941200989717e-09, 3.6508015025293104e-10, 3.015507623410113e-11, 2.312852609548874e-12, 1.6556642100668664e-13], [0.09632882197076809, 0.12618723065021487, 0.06861542165672044, 0.024559303395869574, 0.006592826022857664, 0.0014158497663245375, 0.0002533853406024331, 3.8868609827690496e-05, 5.2170450076242e-06, 6.224402040557912e-07, 6.683642298522206e-08, 6.5243323533176646e-09, 5.83808471374898e-10, 4.822170952933851e-11, 3.698538377287007e-12, 2.647612561021468e-13], [0.08658383156395354, 0.0929720405652159, 0.049117174388377045, 0.019636687126979517, 0.005271373532330632, 0.0011320597507174367, 0.00020259730399396964, 3.1077865603279464e-05, 4.1713512346329965e-06, 4.976795695415567e-07, 5.343986780455661e-08, 5.2166085930627735e-09, 4.667911019168849e-10, 3.855624923445348e-11, 2.9572109506219152e-12, 2.1169305438436565e-13], [0.04615276427757296, 0.049557943961419125, 0.026607179961229313, 0.009371057436146933, 0.0028098601743790043, 0.0006034346815016854, 0.00010799274466848877, 1.656578808687635e-05, 2.2235027807562296e-06, 2.65283800034301e-07, 2.8485660397075442e-08, 2.780668196072545e-09, 2.4881896890559387e-10, 2.0552075950008137e-11, 1.5763157792607014e-12, 1.1284115592625942e-13], [0.018450999557185283, 0.019812325792400894, 0.010637045762417063, 0.003807284540520823, 0.001005695140098375, 0.0002412417374226093, 4.317345050176685e-05, 6.622687794323688e-06, 8.889142278974858e-07, 1.0605543034265937e-07, 1.138802660251423e-08, 1.1116583905104235e-09, 9.947310322487655e-11, 8.216330054949847e-12, 6.30181143001579e-13, 4.511175333953747e-14], [0.005901087659439398, 0.0063364735810640905, 0.003401991273532236, 0.0012176641026091493, 0.0003268760295591838, 6.907550635495265e-05, 1.380794114604919e-05, 2.118099948692715e-06, 2.842968352087571e-07, 3.3919159190911315e-08, 3.6421735874625963e-09, 3.5553594749281194e-10, 3.1813967588431705e-11, 2.627786301922282e-12, 2.015475722414104e-13, 1.4427858507207562e-14], [0.0015727619279947997, 0.0016888012822689061, 0.0009067010461746543, 0.0003245326712959822, 8.711922346085371e-05, 1.8709386801922577e-05, 3.2947260583681432e-06, 5.64517450213256e-07, 7.577098739594423e-08, 9.04015755802688e-09, 9.707146011204305e-10, 9.475768443395301e-11, 8.479080449094585e-12, 7.003594064491894e-13, 5.3716597107995756e-14, 3.84532273916223e-15], [0.0003592916461076713, 0.0003858004074582021, 0.00020713250086297635, 7.413828858021467e-05, 1.990206441783583e-05, 4.27409022438527e-06, 7.649058770428545e-07, 1.1545718514636865e-07, 1.730960185652614e-08, 2.0651905620816393e-09, 2.217561607572587e-10, 2.1647042578804592e-11, 1.937014571505217e-12, 1.599945163543868e-13, 1.227135795615354e-14, 8.784497591001105e-16], [7.181899185239481e-05, 7.711784178691379e-05, 4.1403822084375024e-05, 1.4819540618813308e-05, 3.978233888137902e-06, 8.543500922633111e-07, 1.5289742900041435e-07, 2.3454042358348842e-08, 3.0976955050785535e-09, 4.128120031695251e-10, 4.432695297867063e-11, 4.327038469827691e-12, 3.871908385178927e-13, 3.198138612730248e-14, 2.4529280505639738e-15, 1.755937739577797e-16], [1.2760831292034073e-05, 1.3702333369857346e-05, 7.356650028588316e-06, 2.6331427493550514e-06, 7.068544152097803e-07, 1.5180131481255712e-07, 2.716688505555771e-08, 4.167324964213217e-09, 5.593490993394781e-10, 6.566764490393517e-11, 7.876033261693321e-12, 7.688301726804487e-13, 6.87962451255612e-14, 5.682467301889555e-15, 4.358373769584062e-16, 3.119958199931313e-17], [2.0406153018491987e-06, 2.191173169339252e-06, 1.1764196450162252e-06, 4.210722062943828e-07, 1.1303479396026273e-07, 2.4274914287183136e-08, 4.3443220962066895e-09, 6.664069836155742e-10, 8.944686322279284e-11, 1.0671812053601531e-11, 1.1275847028635394e-12, 1.2294548677831517e-13, 1.100137344505328e-14, 9.086970482661402e-16, 6.969580587546305e-17, 4.989200388444975e-18], [2.966542849218287e-07, 3.185416227650483e-07, 1.7102191101087315e-07, 6.121333802874123e-08, 1.6432424055225477e-08, 3.52896370662184e-09, 6.315554743475772e-10, 9.687886149449268e-11, 1.300333052673499e-11, 1.551413816564269e-12, 1.6658780938853536e-13, 1.600153108586713e-14, 1.5993237772660075e-15, 1.3210176010132131e-16, 1.0132022157875591e-17, 7.25304604069479e-19], [3.953225168204832e-08, 4.244896582455999e-08, 2.2790438476249448e-08, 8.15731040557249e-09, 2.1897904615417833e-09, 4.702709130385575e-10, 8.416129896678499e-11, 1.2910110286388705e-11, 1.7328282826698668e-12, 2.0674193691686316e-13, 2.2199548574341484e-14, 2.1670404627226616e-15, 1.9080808894647539e-16, 1.760392582680249e-17, 1.350196745342057e-18, 9.665434012449428e-20], [4.862844376779025e-09, 5.2216280625822154e-09, 2.8034415160542047e-09, 1.003427058858689e-09, 2.693651330027417e-10, 5.784781204534202e-11, 1.0352643272502892e-11, 1.5880668198384161e-12, 2.131544223202266e-13, 2.5431232034706107e-14, 2.7307564168117178e-15, 2.665666659505972e-16, 2.3852843377757346e-17, 1.9386875066813355e-18, 1.660870901925757e-19, 1.188940660769695e-20], [5.554494071222629e-10, 5.964308102113995e-10, 3.2021792336806387e-10, 1.1461460037564794e-10, 3.076773423806017e-11, 6.6075593653252174e-12, 1.182511534878452e-12, 1.8139399602461704e-13, 2.434716974876336e-14, 2.904835454640358e-15, 3.119156023080582e-16, 3.0448084513633984e-17, 2.7245469288760602e-18, 2.2504351520268417e-19, 1.6984371267479573e-20, 1.3580454852341e-21], [5.921550269139167e-11, 6.358445934847855e-11, 3.41378801739537e-11, 1.2218864742658815e-11, 3.2800950477580426e-12, 7.0442050052422e-13, 1.2606551393938845e-13, 1.933810086403363e-14, 2.5956097482489884e-15, 3.096794946158683e-16, 3.325278405400169e-17, 3.2460177422926777e-18, 2.9045924602845216e-19, 2.3991500772691465e-20, 1.840114902656531e-21, 1.2961781344006504e-22]] |
| Legacy trial inputs | {"lambda_home": 1.599124112802161, "lambda_away": 1.0737806226159425, "rho": -0.10285845637220993, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4740 |
| Legacy p draw | 0.2642 |
| Legacy p away | 0.2618 |
| Legacy p over 1 5 | 0.7585 |
| Legacy p under 3 5 | 0.7203 |
| Legacy p btts yes | 0.5359 |
| Legacy p over 2 5 | 0.5028 |
| Legacy goal margin distribution | {"-1": 0.15809185737651965, "-10": 4.880796467468311e-08, "-11": 4.703927349131668e-09, "-12": 4.163719118888177e-10, "-13": 3.40653076657725e-11, "-14": 2.577613865651021e-12, "-15": 1.6556642100668664e-13, "-2": 0.07338760875172795, "-3": 0.023197766798530372, "-4": 0.005758709876494612, "-5": 0.0011721872963082719, "-6": 0.00020176957655913895, "-7": 3.005054148883353e-05, "-8": 3.941201980698881e-06, "-9": 4.6154848028207705e-07, "0": 0.2641568488337549, "1": 0.22006170138420433, "10": 2.382982262304094e-06, "11": 3.4202458695786636e-07, "12": 4.508631653274126e-08, "13": 5.4934130671643775e-09, "14": 6.190338664707414e-10, "15": 5.921550269139167e-11, "2": 0.14808803585985883, "3": 0.06971239827581703, "4": 0.02577244695116673, "5": 0.007812572757201269, "6": 0.002002715949818422, "7": 0.00044420412336106894, "8": 8.676120704542034e-05, "9": 1.5131459781547653e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4833 |
| Legacy raw p draw | 0.2737 |
| Legacy raw p away | 0.2429 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5991 |
| Legacy lambda away | 1.0738 |
| Legacy model home team | Brentford |
| Legacy model away team | Nott'm Forest |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 73.0% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:41:51Z |
| Market reference home draw last update utc | 2026-10-30T11:42:12Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.4% |
| Market draw away odds | 1.79 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:41:51Z |
| Market reference draw away last update utc | 2026-10-30T11:42:12Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.7% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:41:51Z |
| Market reference home away last update utc | 2026-10-30T11:42:12Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.32 |
| Market reference dc draw away odds | 1.84 |
| Market reference dc home away odds | 1.29 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.17, "price": 1.68, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.17, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:51Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.73, "price": 2.09, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:51Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.09, "price": 1.73, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 78.8% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 4.25 |
| Market reference over 1 5 last update utc | 2026-10-30T11:42:11Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.5% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.90 |
| Market reference under 3 5 last update utc | 2026-10-30T11:42:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.6% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:41:51Z |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-30T11:42:07Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.859049559640097, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,503.9116 |
| Elo away rating | 1,478.7386 |
| Elo rating diff | 85.1730 |
| Elo home expectancy | 0.6202 |

</details>


---

## 2026-10-31 — Chelsea vs Manchester United

The model's most likely 1X2 outcome is **Chelsea win** at **50.6%**. Expected goals are 1.74 for Chelsea and 1.38 for Manchester United (3.11 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 58.5%; Under 3.5 goals: 64.1%; Double Chance 1X: 75.0%; Double Chance X2: 49.4%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 81.0%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 50.6% | 1.98 |
| Draw | 24.4% | 4.10 |
| Manchester United win | 25.0% | 4.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.74 |
| Manchester United expected goals | 1.38 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 81.3% |
| Under 1.5 | 18.7% |
| Over 2.5 | 58.5% |
| Under 2.5 | 41.5% |
| Over 3.5 | 35.9% |
| Under 3.5 | 64.1% |
| Over 4.5 | 19.0% |
| Under 4.5 | 81.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.32% |
| 2 | 2-1 | 10.43% |
| 3 | 1-0 | 8.36% |
| 4 | 2-0 | 7.82% |
| 5 | 1-2 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 50.6% | 52.9% | 1.85 | -6.4% |
| Draw | 24.4% | 24.1% | 3.95 | -3.6% |
| Manchester United win | 25.0% | 22.9% | 4.15 | +3.7% |

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
| Market best home last update utc | 2026-10-30T11:42:07Z |
| Market best draw last update utc | 2026-10-30T11:42:07Z |
| Market best away last update utc | 2026-10-30T11:42:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7690 |
| Dc lambda away | 1.3441 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:41:52.235573+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6583 |
| Shot lambda away | 1.4547 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.23 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.36 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.26 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.13782268217432864, "-10": 2.4906973125533906e-07, "-11": 2.971337915991219e-08, "-12": 3.2574424949795743e-09, "-13": 3.301447509384032e-10, "-14": 3.085586901347936e-11, "-15": 2.3875495539098473e-12, "-2": 0.07321263758430586, "-3": 0.02784857650643127, "-4": 0.00840870277359538, "-5": 0.0020948811750051153, "-6": 0.0004430718928101447, "-7": 8.129283233883066e-05, "-8": 1.3158035525368178e-05, "-9": 1.9041654586080968e-06, "0": 0.2440154436583743, "1": 0.23516806320996173, "10": 3.3724944115112433e-06, "11": 5.070367812115081e-07, "12": 7.005212455052669e-08, "13": 8.947590169191296e-09, "14": 1.053893200883787e-09, "15": 1.0277047128960573e-10, "2": 0.15579706497372897, "3": 0.07468499444730133, "4": 0.028419503552412635, "5": 0.008922858649972661, "6": 0.0023783510240324313, "7": 0.000549934722026786, "8": 0.00011217784021225805, "9": 2.0458690665255317e-05} |
| Raw goal margin distribution | {"-1": 0.16212590914121863, "-10": 3.733673164918822e-07, "-11": 4.593014175557144e-08, "-12": 5.193133964827213e-09, "-13": 5.431340055850394e-10, "-14": 5.281288546392825e-11, "-15": 4.758804169080045e-12, "-16": 3.563968108027873e-13, "-2": 0.0875972629683144, "-3": 0.03410200073087079, "-4": 0.010567842584253606, "-5": 0.0027065499172911687, "-6": 0.0005890961431414493, "-7": 0.00011130753213909518, "-8": 1.8562508231061747e-05, "-9": 2.7687115709740384e-06, "0": 0.25005302580801386, "1": 0.20641463841248958, "10": 3.773180950967891e-06, "11": 5.849601136876285e-07, "12": 8.335182780858269e-08, "13": 1.0986256390194142e-08, "14": 1.3462935491824308e-09, "15": 1.5288146497254063e-10, "16": 1.4429389106725872e-11, "2": 0.13912488025464662, "3": 0.06825763863303115, "4": 0.026657220814069016, "5": 0.008604025892858523, "6": 0.0023600922582773286, "7": 0.0005619846950514956, "8": 0.00011811191938933045, "9": 2.2201990734204497e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 29.8% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 62.4% |
| P home draw | 75.0% |
| P draw away | 49.4% |
| P home away | 75.6% |
| Raw p home draw | 70.2% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9687 |
| Totals anchor target over 2 5 | 0.5853 |
| Totals anchor reference over odds | 1.66 |
| Totals anchor reference under odds | 2.30 |
| Totals anchor reference last update utc | 2026-10-30T11:42:07Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6048 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.1, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.95, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.19, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 5.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 8.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.1, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.1, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.85 |
| Reference draw odds | 3.95 |
| Reference away odds | 4.15 |
| Market reference 1x2 last update utc | 2026-10-30T11:42:07Z |
| Market reference home last update utc | 2026-10-30T11:42:07Z |
| Market reference draw last update utc | 2026-10-30T11:42:07Z |
| Market reference away last update utc | 2026-10-30T11:42:07Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-30T11:41:26Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:41:26Z |
| Home probability edge | -2.3% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | -0.0770 |
| Raw ev home | -0.1636 |
| Raw edge prob draw | 0.0086 |
| Raw ev draw | -0.0123 |
| Raw edge prob away | 0.0684 |
| Raw ev away | 0.2360 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.045709997141196765, 0.03810891062528467, 0.034903670867414735, 0.017282581519832602, 0.006418113408277079, 0.0019067604998355592, 0.0004720670198613648, 0.00010017616097789582, 1.860086588407378e-05, 3.0700780461566154e-06, 4.5604550569909754e-07, 6.158490262271102e-08, 7.623453876892981e-09, 8.710983454823695e-10, 9.242680002327594e-11, 9.153041306671302e-12, 8.497754960601207e-13], [0.060980745582878554, 0.10746567651344517, 0.06415790341192219, 0.03176783897802724, 0.01179740382320145, 0.0035048965606745467, 0.0008677262165136474, 0.00018413800899656074, 3.4191032837255184e-05, 5.643239403115774e-06, 8.382763984117034e-07, 1.1320179614085341e-07, 1.4012990764119333e-08, 1.6012024558688669e-09, 1.6989358314464318e-10, 1.682458966305992e-11, 1.5620080307639488e-12], [0.06615328445645251, 0.09826756066142092, 0.06651626132026972, 0.029196899553916925, 0.010842651735336833, 0.0032212487887408195, 0.0007975020019892649, 0.00016923590416236415, 3.1423986758573235e-05, 5.186537684399618e-06, 7.704355282011577e-07, 1.040404880399178e-07, 1.2878933441866897e-08, 1.4716187431516484e-09, 1.5614426544279895e-10, 1.54629924549792e-11, 1.4355962836556368e-12], [0.040533043555416155, 0.06020991019721574, 0.044719480305006214, 0.020180092108071375, 0.006643444519129234, 0.0019737042314628087, 0.0004886406419237057, 0.00010369320784168956, 1.925391663370138e-05, 3.1778642525597503e-06, 4.720566344937033e-07, 6.374706362500818e-08, 7.891102829370995e-09, 9.016814071022962e-10, 9.56717775107251e-11, 9.474391964428152e-12, 8.796099418421515e-13], [0.018626372447313314, 0.027668591203109164, 0.020550188753344554, 0.010175442970647363, 0.0034438242850918796, 0.0009069871613712605, 0.00022454772183395585, 4.765071013913278e-05, 8.847858212239317e-06, 1.4603414390595747e-06, 2.16926781683288e-07, 2.9294038773047418e-08, 3.626241886300979e-09, 4.143546164882232e-10, 4.3964578139189354e-11, 4.353819451036269e-12, 4.0421199465842333e-13], [0.006847583504489603, 0.010171759920016243, 0.0075548330153704935, 0.0037407818207098008, 0.0013891884110823081, 0.000376130713951539, 8.255011974823375e-05, 1.751775433723842e-05, 3.2527239598353392e-06, 5.368629869993464e-07, 7.97484457125606e-08, 1.0769320609775101e-08, 1.3331095034291283e-09, 1.5232852477848584e-10, 1.616262752714263e-11, 1.600587679580208e-12, 1.4859980894127886e-13], [0.0020978051408735, 0.003116189855581994, 0.002314475979401199, 0.0011460146968965037, 0.000425587594295073, 0.0001264380297449012, 2.8528183565781945e-05, 5.3666866685340205e-06, 9.96494754727871e-07, 1.644717342013455e-07, 2.4431494597005376e-08, 3.2992567559181702e-09, 4.0840742837343377e-10, 4.666690989200323e-11, 4.951534084138285e-12, 4.90351240030978e-13, 4.5524591693616785e-14], [0.0005508662484914674, 0.0008182856366806538, 0.0006077622154484153, 0.0003009339640251798, 0.00011175577602799507, 3.3201579000433145e-05, 8.219894661536063e-06, 1.5897025213660215e-06, 2.6167126606897217e-07, 4.3188914659945706e-08, 6.415508052424717e-09, 8.663574878961391e-10, 1.0724440680436274e-10, 1.225434387590117e-11, 1.300231824234704e-12, 1.2876217279481458e-13, 1.1954380581757152e-14], [0.00012657129853853842, 0.00018801564970395763, 0.00013964415685771754, 6.91449198518228e-05, 2.5677873222004994e-05, 7.628652107699031e-06, 1.8886667026882377e-06, 4.007892347524131e-07, 6.782248713030424e-08, 9.923419751980176e-09, 1.4740768511476953e-09, 1.9906101080233256e-10, 2.464130606548445e-11, 2.8156530216873906e-12, 2.987513409020707e-13, 2.9585394744938316e-14, 2.746731130470281e-15], [2.5850668885560582e-05, 3.839994028599368e-05, 2.852064332446585e-05, 1.4122020148697895e-05, 5.244397474087247e-06, 1.5580606500550067e-06, 3.8573751024219296e-07, 8.185639177374186e-08, 1.5199222552295042e-08, 2.2862647253830258e-09, 3.010625080952801e-10, 4.065582274728173e-11, 5.032691071053855e-12, 5.750633421692109e-13, 6.101637639772799e-14, 6.0424618553402724e-15, 5.609868729428355e-16], [4.7517200233564425e-06, 7.0584543077168844e-06, 5.242499239142329e-06, 2.5958278374875304e-06, 9.63994726727549e-07, 2.863936721036062e-07, 7.090403189533336e-08, 1.504636717730192e-08, 2.7938329356550034e-09, 4.6112289685006857e-10, 6.242583188427624e-11, 7.473117537867518e-12, 9.2508008359704e-13, 1.0570480825005009e-13, 1.121567642080184e-14, 1.1106902925991837e-15, 1.0311735331891327e-16], [7.940305592837445e-07, 1.1794946659496757e-06, 8.760416401723107e-07, 4.3377274323258704e-07, 1.6108719963458117e-07, 4.785747613873951e-08, 1.1848334460908694e-08, 2.514305406517301e-09, 4.668601511745842e-10, 7.705539675836547e-11, 1.1446213045139221e-11, 1.4086944088963762e-12, 1.545844141806059e-13, 1.766367706876827e-14, 1.8741823544696567e-15, 1.8560058881596264e-16, 1.7231303470156957e-17], [1.2162841009415776e-07, 1.8067322379053895e-07, 1.3419074445516463e-07, 6.644465818689932e-08, 2.4675095623206203e-08, 7.330736412871388e-09, 1.8149101012486011e-09, 3.851375309304232e-10, 7.151293770721413e-11, 1.1803230099038806e-11, 1.7533137459282576e-12, 2.367694779592827e-13, 2.671112142297986e-14, 2.7056955594113238e-15, 2.870844419467878e-16, 2.8430019810053927e-17, 2.639465220098916e-18], [1.7197714547228174e-08, 2.5546387777919426e-08, 1.8973972579543022e-08, 9.394978227552526e-09, 3.488948434209968e-09, 1.0365334230048383e-09, 2.5662019117072765e-10, 5.4456728598508817e-11, 1.0111610339807057e-11, 1.6689240763846125e-12, 2.4791074133800477e-13, 3.3478147846278265e-14, 4.144183154002226e-15, 4.315620423312154e-16, 4.05924592759953e-17, 4.0198779617923714e-18, 3.732086062578427e-19], [2.257988673655841e-09, 3.3541348821061314e-09, 2.4912039946476392e-09, 1.23352171992388e-09, 4.580844754563693e-10, 1.360925443077475e-10, 3.3693167979014475e-11, 7.1499428625881825e-12, 1.3276125474117453e-12, 2.191228172394198e-13, 3.254965329733653e-14, 4.395542119522835e-15, 5.441140796699962e-16, 6.217350851834237e-17, 6.012083324879897e-18, 5.277933229022489e-19, 4.900074387947745e-20], [2.767002545948462e-10, 4.1102508026383435e-10, 3.052791130482721e-10, 1.5115920550593204e-10, 5.613495429075979e-11, 1.6677161448044405e-11, 4.128855147358107e-12, 8.761740187179948e-13, 1.6268935896714477e-13, 2.685192358362057e-14, 3.988725656344787e-15, 5.386420391494473e-16, 6.667726287996251e-17, 7.61891582397826e-18, 8.083955306642971e-19, 7.29592390488157e-20, 6.004688360476173e-21], [3.1788397479353207e-11, 4.722015396964938e-11, 3.507164748341951e-11, 1.7365755280281923e-11, 6.449001075524246e-12, 1.915936932237487e-12, 4.743388789109471e-13, 1.006582665016769e-13, 1.869038399000121e-14, 3.0848530342380383e-15, 4.58240259972438e-16, 6.188128473045098e-17, 7.660142338383848e-18, 8.752905736533638e-19, 9.28716111480151e-20, 9.197091025988419e-21, 7.781765746922657e-22]] |
| Legacy trial inputs | {"lambda_home": 1.8381420010414589, "lambda_away": 1.4854524831054856, "rho": -0.10285845637220993, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4899 |
| Legacy p draw | 0.2437 |
| Legacy p away | 0.2663 |
| Legacy p over 1 5 | 0.8552 |
| Legacy p under 3 5 | 0.5736 |
| Legacy p btts yes | 0.6591 |
| Legacy p over 2 5 | 0.6467 |
| Legacy goal margin distribution | {"-1": 0.13910233398141983, "-10": 5.830735273793306e-07, "-11": 7.716968632675272e-08, "-12": 9.390679202163732e-09, "-13": 1.0573345310238341e-09, "-14": 1.106869859699915e-10, "-15": 1.071504933743525e-11, "-16": 8.497754960601207e-13, "-2": 0.07973097248775791, "-3": 0.032840949299241105, "-4": 0.010833615223061678, "-5": 0.0029645200364090043, "-6": 0.0006910349969380208, "-7": 0.0001400564632796089, "-8": 2.508207153246979e-05, "-9": 4.020717054987244e-06, "0": 0.2437221701407271, "1": 0.2156674923167092, "10": 6.075275647964619e-06, "11": 9.949693282649734e-07, "12": 1.4982361007330627e-07, "13": 2.0874494297662857e-08, "14": 2.704085401403095e-09, "15": 3.239204085644956e-10, "16": 3.1788397479353207e-11, "2": 0.15111492779678826, "3": 0.07702226816172118, "4": 0.031440851736180254, "5": 0.010646223530324801, "6": 0.0030708706774851876, "7": 0.0007701670512293341, "8": 0.00017067325702398557, "9": 3.3855238762128606e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4507 |
| Legacy raw p draw | 0.2460 |
| Legacy raw p away | 0.3033 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8381 |
| Legacy lambda away | 1.4855 |
| Legacy model home team | Chelsea |
| Legacy model away team | Man United |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 76.7% |
| Market home draw odds | 1.26 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:41:11Z |
| Market reference home draw last update utc | 2026-10-30T11:42:12Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.8% |
| Market draw away odds | 2.03 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:41:11Z |
| Market reference draw away last update utc | 2026-10-30T11:42:12Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.5% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:41:11Z |
| Market reference home away last update utc | 2026-10-30T11:42:12Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.26 |
| Market reference dc draw away odds | 2.02 |
| Market reference dc home away odds | 1.28 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:11Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.23, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:11Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.23, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:11Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.04, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:11Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.04, "price": 1.78, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 81.4% |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market reference over 1 5 last update utc | 2026-10-30T11:42:11Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.8% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market reference under 3 5 last update utc | 2026-10-30T11:42:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:41:11Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-30T11:42:07Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.967201976495664, "version": "count-markets-nb2-v1"}} |
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
| Market best home last update utc | 2026-10-30T11:42:07Z |
| Market best draw last update utc | 2026-10-30T11:42:07Z |
| Market best away last update utc | 2026-10-30T11:42:07Z |
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
| Dc lambda home | 0.8793 |
| Dc lambda away | 1.1502 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:41:52.235573+00:00 |
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
| Fair Under 0.5 odds | 11.50 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.81 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.27 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.21052386537093515, "-10": 5.948890426283736e-07, "-11": 7.35328065587444e-08, "-12": 8.345576485115462e-09, "-13": 8.706748364498706e-10, "-14": 7.645808620904324e-11, "-2": 0.12147343717979028, "-3": 0.04935414540197896, "-4": 0.015734689898519557, "-5": 0.004111284732723154, "-6": 0.0009081446817586459, "-7": 0.00017353447992225353, "-8": 2.9196971677646662e-05, "-9": 4.38591403485314e-06, "0": 0.2919923084149661, "1": 0.17310192467859298, "10": 1.646633876551863e-07, "11": 1.8022623123238222e-08, "12": 1.81121073349839e-09, "13": 1.6731867514197874e-10, "14": 1.3010309554177039e-11, "2": 0.08896847287244225, "3": 0.03200768280234086, "4": 0.009035757545242584, "5": 0.002090545955745795, "6": 0.00040889612042086887, "7": 6.918620465375343e-05, "8": 1.0307357034955504e-05, "9": 1.3710251101267057e-06} |
| Raw goal margin distribution | {"-1": 0.21440621178574798, "-10": 1.600608751116413e-07, "-11": 1.6833737910179114e-08, "-12": 1.6194229023266344e-09, "-13": 1.330827433050724e-10, "-2": 0.110726077316745, "-3": 0.03935080683503916, "-4": 0.010855252987975227, "-5": 0.0024392864959950967, "-6": 0.0004616600440310577, "-7": 7.540077538011751e-05, "-8": 1.0824877910856703e-05, "-9": 1.3858625202076422e-06, "0": 0.310583473324795, "1": 0.18869260356953876, "10": 4.742889568363653e-08, "11": 4.416865449714987e-09, "12": 3.762440735933363e-10, "13": 2.7378327749597495e-11, "2": 0.08681634134300335, "3": 0.027320018503392864, "4": 0.00667333734835524, "5": 0.0013278277004208062, "6": 0.00022252406461325297, "7": 3.218150052101129e-05, "8": 4.090998002817358e-06, "9": 4.637695098797212e-07} |
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
| Totals anchor scale | 1.1793 |
| Totals anchor target over 2 5 | 0.4772 |
| Totals anchor reference over odds | 2.03 |
| Totals anchor reference under odds | 1.86 |
| Totals anchor reference last update utc | 2026-10-30T11:42:07Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3840 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:30:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.3, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:30:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.89, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:30:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.15, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:30:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.51, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:30:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.22, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:30:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:30:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:30:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 5.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:30:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 5.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:30:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.26, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.01, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.26, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.18 |
| Reference draw odds | 3.39 |
| Reference away odds | 2.36 |
| Market reference 1x2 last update utc | 2026-10-30T11:42:07Z |
| Market reference home last update utc | 2026-10-30T11:42:07Z |
| Market reference draw last update utc | 2026-10-30T11:42:07Z |
| Market reference away last update utc | 2026-10-30T11:42:07Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market best over 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market best under 2 5 last update utc | 2026-10-30T11:42:07Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.8% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0077 |
| Raw ev home | -0.0107 |
| Raw edge prob draw | 0.0266 |
| Raw ev draw | 0.0529 |
| Raw edge prob away | -0.0343 |
| Raw ev away | -0.1071 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.12759297493494734, 0.13167852341066083, 0.0854811800942225, 0.033465466556998245, 0.009826175632839058, 0.0023081400022426164, 0.0004518127965054894, 7.58067916978685e-05, 1.1129246444489364e-05, 1.452348631133851e-06, 1.7057622914449134e-07, 1.8212663096437336e-08, 1.7825422715733375e-09, 1.6104383906047967e-10], [0.10481344169535009, 0.13782659143836098, 0.07927327972410815, 0.031035103733318893, 0.00911256920765082, 0.002140515933899108, 0.00041900079246486667, 7.030147450735178e-05, 1.0321007098171438e-05, 1.3468747058228891e-06, 1.5818847040190503e-07, 1.689000473055473e-08, 1.6530886910864148e-09, 1.4934835115301034e-10], [0.05527878233683415, 0.06492412386793696, 0.03402962739815161, 0.014390620583421176, 0.004225393513561369, 0.000992532614751322, 0.00019428584741739742, 3.259798500380802e-05, 4.785732261920127e-06, 6.245303070824138e-07, 7.335017397675458e-08, 7.831700896448377e-09, 7.665182094632213e-10, 6.925111237489287e-11], [0.01708809030699581, 0.0200697129144004, 0.011785792596775655, 0.004118306178208716, 0.0013061775764590072, 0.00030681730379230726, 6.0058741630918366e-05, 1.0076873766446798e-05, 1.4793926642320824e-06, 1.9305834600066748e-07, 2.267442125101666e-08, 2.420979741565602e-09, 2.3695045063495163e-10, 2.1407296110673648e-11], [0.0039617754497660975, 0.0046530475014854794, 0.002732468223603955, 0.0010697480293824237, 0.00028035131381856534, 7.113382712111197e-05, 1.3924273799033343e-05, 2.336265222214847e-06, 3.429886799766758e-07, 4.4759467080108085e-08, 5.2569341474720525e-09, 5.612902280010184e-10, 5.4935599079333386e-11, 4.96315847198085e-12], [0.0007348118804331741, 0.0008630258397187279, 0.0005068056327444959, 0.00019841194207677527, 5.825798326099773e-05, 1.2214242381596915e-05, 2.582610232121598e-06, 4.333197231629253e-07, 6.361596211007701e-08, 8.3017799946897e-09, 9.750319560502518e-10, 1.0410552872968708e-10, 1.0189202132743591e-11, 9.205437955599946e-13], [0.00011357460530682342, 0.00013339171796985987, 7.833331392559831e-05, 3.0667111691560924e-05, 9.004518885757289e-06, 2.1151352283696682e-06, 3.6954555271593637e-07, 6.697512362059163e-08, 9.83266327104915e-09, 1.283146627522053e-09, 1.5070370052354952e-10, 1.6090845358627353e-11, 1.5748719385641982e-12, 1.4228185612178553e-13], [1.504663941586551e-05, 1.7672058607935355e-05, 1.037778758468168e-05, 4.062853401976718e-06, 1.1929405206500072e-06, 2.8021824959105277e-07, 5.48520414084911e-08, 8.214400001347512e-09, 1.3026550991519285e-09, 1.6999438008038825e-10, 1.9965592081861262e-11, 2.1317542539870317e-12, 2.0864285745677103e-13, 1.8849845691305632e-14], [1.7442384013752e-06, 2.0485825707242113e-06, 1.2030151800826782e-06, 4.70974596188795e-07, 1.3828819905661156e-07, 3.2483494698988223e-08, 6.3585651502774045e-09, 1.066863151226724e-09, 1.3979763359961417e-10, 1.9706109620832484e-11, 2.3144538426736705e-12, 2.4711748114190053e-13, 2.4186323210817673e-14, 2.185114151144221e-15], [1.7972961812612702e-07, 2.1108981595968265e-07, 1.2396095553550625e-07, 4.853011162544087e-08, 1.4249477128928447e-08, 3.3471606249743202e-09, 6.551985585160996e-10, 1.0993159341729756e-10, 1.6139131702772094e-11, 1.8798307441405956e-12, 2.384856938055718e-13, 2.546345183256304e-14, 2.4922044091725434e-15, 2.2515828778767243e-16], [1.666771127482664e-08, 1.9575983870411514e-08, 1.1495853815076289e-08, 4.500570897225813e-09, 1.3214637246686456e-09, 3.104079754311248e-10, 6.076160687864633e-11, 1.0194803050075527e-11, 1.4967059422528314e-12, 1.9531770073409824e-13, 2.04749427000816e-14, 2.361421938301661e-15, 2.311213030052021e-16, 2.0880661579916306e-17], [1.4052047233124994e-09, 1.6503924590856986e-09, 9.691809399082136e-10, 3.794296276259599e-10, 1.1140864135287958e-10, 2.6169564977314112e-11, 5.122628750528265e-12, 8.594932539324181e-13, 1.2618278687368482e-13, 1.6466649265314122e-14, 1.9339839471803283e-15, 1.843067630214108e-16, 1.9485143538066678e-17, 1.7603859218693722e-18], [1.0859621086380608e-10, 1.2754466628351085e-10, 7.489967544896163e-11, 2.932285891589676e-11, 8.609817564438185e-12, 2.022421038972321e-12, 3.9588400376138605e-13, 6.642285575303081e-14, 9.751584451278573e-15, 1.2725659728932709e-15, 1.4946101806441514e-16, 1.5958162410495727e-17, 1.3940640459340516e-18, 1.360451168441511e-19], [7.746894418789137e-12, 9.098614542060122e-12, 5.343095059111922e-12, 2.0917957474905986e-12, 6.141959015530349e-13, 1.4427282623060839e-13, 2.8241055142091833e-14, 4.738386785506999e-15, 6.9564577400130135e-16, 9.078064653021477e-17, 1.0662054573173525e-17, 1.138402512653443e-18, 1.1141976272909888e-19, 8.984625281551008e-21]] |
| Legacy trial inputs | {"lambda_home": 0.9273769926518137, "lambda_away": 1.1744854196015055, "rho": -0.10285845637220993, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T11:42:07Z", "over": 2.03, "under": 1.86, "bookmaker": "pinnacle", "event_id": "d20fbb0cd5ad9369b8ed6f2c4a198619", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Coventry City", "away_team": "Sunderland"}} |
| Legacy p home | 0.2892 |
| Legacy p draw | 0.3039 |
| Legacy p away | 0.4070 |
| Legacy p over 1 5 | 0.6359 |
| Legacy p under 3 5 | 0.8374 |
| Legacy p btts yes | 0.4271 |
| Legacy p over 2 5 | 0.3573 |
| Legacy goal margin distribution | {"-1": 0.22672238602972805, "-10": 1.8825415938061995e-07, "-11": 1.9935002899898646e-08, "-12": 1.931890622726348e-09, "-13": 1.6104383906047967e-10, "-2": 0.12106286224341507, "-3": 0.04363302830557748, "-4": 0.012171405731241848, "-5": 0.002761263923176233, "-6": 0.00052709842425416, "-7": 8.677557514608536e-05, "-8": 1.2551948160173448e-05, "-9": 1.6186107160413112e-06, "0": 0.3038604434075196, "1": 0.18265353524317549, "10": 1.8395095205108787e-08, "11": 1.5380924846551222e-09, "12": 1.176948254058662e-10, "13": 7.746894418789137e-12, "2": 0.0782886666240607, "3": 0.022279836642453525, "4": 0.004907339153803024, "5": 0.000879066925658756, "6": 0.00013249955724037893, "7": 1.72237969723259e-05, "8": 1.9672122548679756e-06, "9": 2.003047199912642e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2749 |
| Legacy raw p draw | 0.3237 |
| Legacy raw p away | 0.4014 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9274 |
| Legacy lambda away | 1.1745 |
| Legacy model home team | Coventry |
| Legacy model away team | Sunderland |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 59.8% |
| Market home draw odds | 1.64 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:41:55Z |
| Market reference home draw last update utc | 2026-10-30T11:42:12Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.3% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:41:55Z |
| Market reference draw away last update utc | 2026-10-30T11:42:12Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:41:55Z |
| Market reference home away last update utc | 2026-10-30T11:42:12Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.61 |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home away odds | 1.34 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:55Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.1, "price": 1.72, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:55Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.72, "price": 2.1, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:55Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.16, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:55Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.16, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 74.4% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.60 |
| Market reference over 1 5 last update utc | 2026-10-30T11:42:11Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.2% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.45 |
| Market reference under 3 5 last update utc | 2026-10-30T11:42:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.0% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:41:55Z |
| Market reference btts yes odds | 1.84 |
| Market reference btts yes opposite odds | 2.16 |
| Market reference btts yes last update utc | 2026-10-30T11:42:07Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.384542581390274, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,364.9791 |
| Elo away rating | 1,407.0794 |
| Elo rating diff | 17.8997 |
| Elo home expectancy | 0.5257 |

</details>


---

## 2026-10-31 — Hull City vs Ipswich Town

The model's most likely 1X2 outcome is **Hull City win** at **42.5%**. Expected goals are 1.75 for Hull City and 0.91 for Ipswich Town (2.66 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 51.5%; Under 3.5 goals: 70.4%; Double Chance 1X: 69.7%; Double Chance X2: 57.5%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 85.6%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 42.5% | 2.35 |
| Draw | 27.2% | 3.67 |
| Ipswich Town win | 30.3% | 3.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.75 |
| Ipswich Town expected goals | 0.91 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 76.6% |
| Under 1.5 | 23.4% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 29.6% |
| Under 3.5 | 70.4% |
| Over 4.5 | 14.4% |
| Under 4.5 | 85.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.98% |
| 2 | 1-2 | 8.45% |
| 3 | 0-1 | 8.14% |
| 4 | 0-0 | 7.67% |
| 5 | 2-0 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 42.5% | 36.5% | 2.66 | +13.0% |
| Draw | 27.2% | 28.1% | 3.42 | -6.9% |
| Ipswich Town win | 30.3% | 35.4% | 2.74 | -17.0% |
| Over 2.5 | 51.5% | 51.5% | 1.89 | -2.7% |
| Under 2.5 | 48.5% | 48.5% | 2.00 | -2.9% |

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
| Market best home last update utc | 2026-10-30T11:42:07Z |
| Market best draw last update utc | 2026-10-30T11:42:07Z |
| Market best away last update utc | 2026-10-30T11:42:07Z |
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
| Dc lambda home | 1.8158 |
| Dc lambda away | 0.7782 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:41:52.235573+00:00 |
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
| Fair Under 0.5 odds | 13.04 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.27 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.38 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.93 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.19509990549276984, "-10": 2.172084297323754e-08, "-11": 1.875408551114497e-09, "-12": 1.4873093272776106e-10, "-13": 1.0905167156885377e-11, "-14": 7.432703817828579e-13, "-15": 4.709459386066569e-14, "-16": 2.5485604480987995e-15, "-2": 0.07949009862638466, "-3": 0.022425597152249604, "-4": 0.004975799443037212, "-5": 0.0009060198269226749, "-6": 0.00013958048887448233, "-7": 1.8612218137483385e-05, "-8": 2.186018930137385e-06, "-9": 2.2929554876894235e-07, "0": 0.2722867285149325, "1": 0.17426853644569543, "10": 6.886414975416549e-06, "11": 1.1458292959922396e-06, "12": 1.7511883030037883e-07, "13": 2.474408445700144e-08, "14": 3.250075170129348e-09, "15": 3.9684887250425587e-10, "16": 4.1386295080396125e-11, "2": 0.1324858266724994, "3": 0.07202908811499595, "4": 0.030798834613632874, "5": 0.010807285746239972, "6": 0.0032085673809375747, "7": 0.0008245027320306736, "8": 0.00018661880315542833, "9": 3.772286084809891e-05} |
| Raw goal margin distribution | {"-1": 0.12099409407898666, "-10": 8.647637509921849e-09, "-11": 7.070253223047906e-10, "-12": 5.308462667720531e-11, "-13": 3.684324599244576e-12, "-14": 2.3768217932682143e-13, "-15": 1.4266140964453258e-14, "-16": 7.378779170859319e-16, "-2": 0.047617850984653425, "-3": 0.012856460698600714, "-4": 0.002718822341311717, "-5": 0.00047073646449055195, "-6": 6.885838614535923e-05, "-7": 8.70979054651009e-06, "-8": 9.697388790101298e-07, "-9": 9.637901992308336e-08, "0": 0.25080786684779505, "1": 0.24097823081179878, "10": 6.109035357577785e-06, "11": 9.625374741144793e-07, "12": 1.3927044458789415e-07, "13": 1.86275439377014e-08, "14": 2.315804256308946e-09, "15": 2.6786702486561904e-10, "16": 2.6699601072211347e-11, "2": 0.17684175816375186, "3": 0.09201189500255932, "4": 0.03749824090240222, "5": 0.012511674063821709, "6": 0.0035269713921261166, "7": 0.0008597265220120688, "8": 0.00018446540829628426, "9": 3.533052992716588e-05} |
| Unadjusted home-win probability | 56.4% |
| Unadjusted draw probability | 25.1% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 50.3% |
| P home draw | 69.7% |
| P draw away | 57.5% |
| P home away | 72.8% |
| Raw p home draw | 81.5% |
| Raw p draw away | 43.6% |
| Raw p home away | 74.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0575 |
| Totals anchor target over 2 5 | 0.5147 |
| Totals anchor reference over odds | 1.89 |
| Totals anchor reference under odds | 2.00 |
| Totals anchor reference last update utc | 2026-10-30T11:42:07Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4816 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.39, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.39, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.48, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:22Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.7, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.49, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.7, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.66 |
| Reference draw odds | 3.42 |
| Reference away odds | 2.74 |
| Market reference 1x2 last update utc | 2026-10-30T11:42:07Z |
| Market reference home last update utc | 2026-10-30T11:42:07Z |
| Market reference draw last update utc | 2026-10-30T11:42:07Z |
| Market reference away last update utc | 2026-10-30T11:42:07Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market best over 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market best under 2 5 last update utc | 2026-10-30T11:42:07Z |
| Home probability edge | +6.0% |
| Draw probability edge | -0.9% |
| Away probability edge | -5.1% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1997 |
| Raw ev home | 0.5015 |
| Raw edge prob draw | -0.0307 |
| Raw ev draw | -0.1422 |
| Raw edge prob away | -0.1690 |
| Raw ev away | -0.4938 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08600737390601546, 0.07713288033409069, 0.0411629506865523, 0.011952398151131687, 0.0026029442589835, 0.00045348682195521723, 6.583900038622465e-05, 8.193227162118434e-06, 8.921437076694339e-07, 8.634995486831924e-08, 7.521975638560672e-09, 5.956745494475248e-10, 4.324118694568457e-11, 2.8975041181941906e-12, 1.8028759021458036e-13, 1.0469944569142465e-14, 5.700253991610956e-16], [0.09289206750808225, 0.12729837272113242, 0.07357281215597114, 0.0213631804649484, 0.004652385842719006, 0.000810542009511953, 0.00011767767682250027, 1.4644206814519519e-05, 1.5945776560167323e-06, 1.5433803707563e-07, 1.3444441942749557e-08, 1.0646819774004445e-09, 7.728735844963174e-11, 5.1788689259027755e-12, 3.2223795397746796e-13, 1.8713509411282376e-14, 1.018837836382628e-15], [0.09118584335250081, 0.0794323162444141, 0.04492868920928772, 0.019091795378935773, 0.00415773291241836, 0.0007243632200282027, 0.00010516590122196182, 1.3087199279543171e-05, 1.4250382977592852e-06, 1.379284431861231e-07, 1.2014996314621838e-08, 9.514824110352383e-10, 6.906997931884932e-11, 4.628239039121158e-12, 2.879768342901372e-13, 1.67238437688709e-14, 9.10512530119272e-16], [0.05432716243095662, 0.04732458667071207, 0.020612308864833735, 0.007772520997829903, 0.0024771151197703085, 0.000431564778771152, 6.265627193682986e-05, 7.79715770437672e-06, 8.490165164500766e-07, 8.217570470730286e-08, 7.158355205078049e-09, 5.668789978142147e-10, 4.1150861225818033e-11, 2.757435636973071e-12, 1.715722932161036e-13, 9.963816130856389e-15, 5.42469755178882e-16], [0.024275483473816546, 0.02114646100079482, 0.009210379132931695, 0.002674398134331006, 0.0007563496085744981, 0.00019283988314785835, 2.799725267938471e-05, 3.4840725067481772e-06, 3.7937351210408523e-07, 3.671929238171758e-08, 3.1986307715118583e-09, 2.5330352492791403e-10, 1.838780099899787e-11, 1.2321292009411123e-12, 7.6665155737253e-14, 4.452219534347064e-15, 2.4239652850682435e-16], [0.008677782111465433, 0.0075592472212314896, 0.0032924437268479823, 0.0009560198590510478, 0.0002081980847797915, 4.710459161864357e-05, 1.0008206787452523e-05, 1.2454549919353068e-06, 1.3561504060059263e-07, 1.3126083314444547e-08, 1.1434178404787327e-09, 9.054867227511523e-11, 6.573106185522382e-12, 4.4045049609304355e-13, 2.7405572282299465e-14, 1.5915395082922206e-15, 8.664973701663368e-17], [0.0025850464336200207, 0.002251843249702958, 0.000980794378639417, 0.00028479117075831754, 6.202065339200269e-05, 1.0805282865837831e-05, 2.0372363065425495e-06, 3.7101173361829474e-07, 4.039870701369738e-08, 3.910162115567807e-09, 3.4061562882084213e-10, 2.6973772713715493e-11, 1.958079205542636e-12, 1.3120691087727903e-13, 8.163915154780288e-15, 4.741077244196205e-16, 2.5812309040695127e-17], [0.0006600565817528538, 0.0005749776633453896, 0.0002504325556971047, 7.27175667869491e-05, 1.5836133519147933e-05, 2.7589825778525865e-06, 4.0055994179862123e-07, 6.473303844670121e-08, 1.0315262469523488e-08, 9.984069170033978e-10, 8.697158578163138e-11, 6.8873873919011044e-12, 4.99968994909665e-13, 3.350190695597314e-14, 2.0845451210091038e-15, 1.2105698369402592e-16, 6.590823379791516e-18], [0.00014746944185138342, 0.00012846116141344068, 5.595148996468263e-05, 1.6246514743303235e-05, 3.538099362559129e-06, 6.164102170652325e-07, 8.949285966999586e-08, 1.1136793152425759e-08, 1.5748046323924455e-09, 2.2306346889239994e-10, 1.9431139036727655e-11, 1.5387759209985634e-12, 1.1170277012695915e-13, 7.484975767735351e-15, 4.657278088082756e-16, 2.7046478000660945e-17, 1.472517768973373e-18], [2.9286696364668044e-05, 2.5511746581095198e-05, 1.1111687120900697e-05, 3.226476877499358e-06, 7.026489043317874e-07, 1.224159977594655e-07, 1.777283601983354e-08, 2.2117116294500147e-09, 2.4082874480962906e-10, 3.027069065363794e-11, 3.858927394339714e-12, 3.0559323074514367e-13, 2.2183613572616747e-14, 1.4864788925388266e-15, 9.249122227570284e-17, 5.3712957680906854e-18, 2.924346918934042e-19], [5.23457277568445e-06, 4.559855179660016e-06, 1.9860531270150855e-06, 5.766860083511827e-07, 1.25588314218908e-07, 2.1880086480256374e-08, 3.1766370101190863e-09, 3.953114185030055e-10, 4.304464988081051e-11, 4.166261043571485e-12, 4.713060286833799e-13, 5.46203636686666e-14, 3.964999610321868e-15, 2.656865713232353e-16, 1.6531466304211155e-17, 9.600413186827292e-19, 5.226846544213265e-20], [8.505491492156767e-07, 7.40916424282477e-07, 3.227074815592641e-07, 9.370388277838921e-08, 2.0406447362145252e-08, 3.5552259445116056e-09, 5.161616854148204e-10, 6.423290019862403e-11, 6.994188810303221e-12, 6.769625598636933e-13, 5.897045217079321e-14, 6.064545934726241e-15, 6.442602270934692e-16, 4.3170569381846046e-17, 2.6861455944694345e-18, 1.5599407283256686e-19, 8.492937383376418e-21], [1.2668611729104777e-07, 1.1035673260747949e-07, 4.806607342704994e-08, 1.395684317036386e-08, 3.039464076118644e-09, 5.295376186289789e-10, 7.688035415696541e-11, 9.56725044756187e-12, 1.0417582861553424e-12, 1.0083104349657391e-13, 8.783428479476208e-15, 6.955705593215271e-16, 6.557170297188927e-17, 6.430094981898622e-18, 4.0009134822554007e-19, 2.323473420177818e-20, 1.2649912853220905e-21], [1.7417929612702372e-08, 1.5172821157892767e-08, 6.608549552339157e-09, 1.9189104311913585e-09, 4.1789244528305585e-10, 7.280552254488707e-11, 1.0570192108968206e-11, 1.3153903398893067e-12, 1.4323015725563986e-13, 1.3863145038724471e-14, 1.2076235524863853e-15, 9.563320197979189e-17, 6.942202195574727e-18, 6.041022085409182e-19, 5.500810263237971e-20, 3.1945170753529652e-21, 1.7392220741758465e-22], [2.223716164601401e-09, 1.9370871522414865e-09, 8.437017941207502e-10, 2.449838895404992e-10, 5.33515869166819e-11, 9.294951865992682e-12, 1.3494776691779263e-12, 1.679335504628075e-13, 1.8285940007214877e-14, 1.7698831261979382e-15, 1.5417515595303322e-16, 1.2209321190502837e-17, 8.862986349980864e-19, 5.938907153687959e-20, 4.7988261555163914e-21, 4.078383261680578e-22, 2.2204339586697662e-23], [2.6497137018874956e-10, 2.3081751397730794e-10, 1.0053298347046634e-10, 2.9191547877852055e-11, 6.3572155979678924e-12, 1.1075586763169602e-12, 1.6079972468306886e-13, 2.0010459821776654e-14, 2.178897943915205e-15, 2.1089398210435612e-16, 1.8371050663861158e-17, 1.4548262122751462e-18, 1.0560869568259708e-19, 7.076624215746252e-21, 4.40319486933523e-22, 3.320726931065325e-23, 2.645802723423646e-24], [2.959987154780177e-11, 2.578455460997327e-11, 1.1230509148680209e-11, 3.260978976145302e-12, 7.101626299003118e-13, 1.2372504443511137e-13, 1.7962888564716414e-14, 2.235362408833504e-15, 2.4340402968712074e-16, 2.3558902895986892e-17, 2.052224508108526e-18, 1.6251819574712576e-19, 1.1797515423303981e-20, 7.905275488025018e-22, 4.918795658543057e-23, 2.8565203978038135e-24, 2.0196395377986844e-25]] |
| Legacy trial inputs | {"lambda_home": 1.7873551562475076, "lambda_away": 0.8711035981468018, "rho": -0.10285845637220993, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T11:42:07Z", "over": 1.89, "under": 2.0, "bookmaker": "pinnacle", "event_id": "1ec76c009147b63859f68c6b5a1dd77b", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Hull City", "away_team": "Ipswich Town"}} |
| Legacy p home | 0.4720 |
| Legacy p draw | 0.2668 |
| Legacy p away | 0.2612 |
| Legacy p over 1 5 | 0.7440 |
| Legacy p under 3 5 | 0.7350 |
| Legacy p btts yes | 0.5058 |
| Legacy p over 2 5 | 0.4843 |
| Legacy goal margin distribution | {"-1": 0.17247783263267696, "-10": 8.658563313424493e-09, "-11": 6.777662580987652e-10, "-12": 4.871823891853685e-11, "-13": 3.2370083856957087e-12, "-14": 1.9991161215598203e-13, "-15": 1.1488782405525092e-14, "-16": 5.700253991610956e-16, "-2": 0.0671447129672162, "-3": 0.017395427172058005, "-4": 0.003526842174633432, "-5": 0.0005851386047652531, "-6": 8.199371237470682e-05, "-7": 9.933151626476274e-06, "-8": 1.0590824565954396e-06, "-9": 1.0078829009880162e-07, "0": 0.2668125146093564, "1": 0.19583050606109637, "10": 6.025528660933651e-06, "11": 9.677658962056783e-07, "12": 1.4273254195356909e-07, "13": 1.945881072739047e-08, "14": 2.4657641877273893e-09, "15": 2.9075592479872285e-10, "16": 2.959987154780177e-11, "2": 0.14874170039946724, "3": 0.07906732904833763, "4": 0.03289190639776041, "5": 0.011197029486473565, "6": 0.0032193312855619996, "7": 0.0008002270630208553, "8": 0.00017506405908160227, "9": 3.4183643219489927e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5792 |
| Legacy raw p draw | 0.2521 |
| Legacy raw p away | 0.1687 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7874 |
| Legacy lambda away | 0.8711 |
| Legacy model home team | Hull |
| Legacy model away team | Ipswich |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 63.9% |
| Market home draw odds | 1.49 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:40:26Z |
| Market reference home draw last update utc | 2026-10-30T11:42:12Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.9% |
| Market draw away odds | 1.52 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:40:26Z |
| Market reference draw away last update utc | 2026-10-30T11:42:12Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.1% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:40:26Z |
| Market reference home away last update utc | 2026-10-30T11:42:12Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.50 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.33 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:40:26Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.38, "price": 1.56, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:40:26Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.56, "price": 2.38, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:40:26Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.88, "price": 1.94, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:40:26Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.94, "price": 1.88, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:40:26Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.54, "price": 2.41, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:40:26Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.41, "price": 1.54, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 76.4% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-10-30T11:42:11Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.5% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.15 |
| Market reference under 3 5 last update utc | 2026-10-30T11:42:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.6% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:40:26Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-30T11:42:08Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.830643156000104, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,403.0690 |
| Elo away rating | 1,376.0928 |
| Elo rating diff | 86.9763 |
| Elo home expectancy | 0.6226 |

</details>


---

## 2026-10-31 — Manchester City vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Manchester City win** at **59.7%**. Expected goals are 2.03 for Manchester City and 1.07 for Brighton and Hove Albion (3.09 combined). The most likely exact score is 2-1 at 9.1%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 69.6%; Under 3.5 goals: 51.5%; Double Chance 1X: 80.6%; Double Chance X2: 40.3%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 70.7%; BTTS Yes (both teams score): 65.4%; BTTS No (at least one team does not score): 34.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 59.7% | 1.67 |
| Draw | 20.9% | 4.79 |
| Brighton and Hove Albion win | 19.4% | 5.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 2.03 |
| Brighton and Hove Albion expected goals | 1.07 |
| Expected total goals | 3.09 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
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
| 1 | 2-1 | 9.12% |
| 2 | 1-1 | 8.92% |
| 3 | 2-0 | 7.32% |
| 4 | 3-1 | 7.19% |
| 5 | 2-2 | 6.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 59.7% | 60.1% | 1.63 | -2.6% |
| Draw | 20.9% | 20.2% | 4.66 | -2.7% |
| Brighton and Hove Albion win | 19.4% | 19.7% | 4.76 | -7.7% |

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
| Market best home last update utc | 2026-10-30T11:42:07Z |
| Market best draw last update utc | 2026-10-30T11:42:07Z |
| Market best away last update utc | 2026-10-30T11:42:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man City |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1447 |
| Dc lambda away | 1.0539 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:41:52.235573+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7466 |
| Shot lambda away | 1.0955 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 65.4% |
| P btts no | 34.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.05 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.35 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.28 |
| Fair Over 3.5 odds | 2.06 |
| Fair Under 3.5 odds | 1.94 |
| Fair Over 4.5 odds | 3.41 |
| Fair Under 4.5 odds | 1.41 |
| Goal margin distribution | {"-1": 0.11506883440036936, "-10": 9.246833172845682e-08, "-11": 1.0245457378332307e-08, "-12": 1.043988490190204e-09, "-13": 9.845040528423421e-11, "-14": 8.638833060157615e-12, "-15": 7.086851416117356e-13, "-16": 5.4547830275579026e-14, "-17": 3.916304610038239e-15, "-18": 2.3287209908403304e-16, "-2": 0.05388769977346066, "-3": 0.018393387162073963, "-4": 0.005046532426299541, "-5": 0.001151123776416098, "-6": 0.0002239987660425705, "-7": 3.79361733965158e-05, "-8": 5.68092924627118e-06, "-9": 7.618759424507732e-07, "0": 0.20884776525844526, "1": 0.20488415487580233, "10": 5.155933771649522e-05, "11": 1.0849405940731475e-05, "12": 2.09957125851103e-06, "13": 3.7602153405843485e-07, "14": 6.266291450996435e-08, "15": 9.762681847097416e-09, "16": 1.4270973177009504e-09, "17": 1.9458657477672202e-10, "18": 2.197425539159545e-11, "2": 0.1775503577415359, "3": 0.11509432717752067, "4": 0.05997159154616743, "5": 0.02597974182294263, "6": 0.009601050029155662, "7": 0.0030880685241087627, "8": 0.00087823974564272, "9": 0.00022368572409260253} |
| Raw goal margin distribution | {"-1": 0.11593707667016569, "-10": 2.89279215960088e-08, "-11": 2.7598701601259207e-09, "-12": 2.4194848116315183e-10, "-13": 1.9616678307201885e-11, "-14": 1.4791296270667921e-12, "-15": 1.041941400350053e-13, "-16": 6.8442169100875505e-15, "-17": 3.8093656986042024e-16, "-2": 0.0502369649208961, "-3": 0.015348620340451851, "-4": 0.003716366472786941, "-5": 0.0007417456719510747, "-6": 0.00012560660786315085, "-7": 1.8444102942730876e-05, "-8": 2.3885861806007977e-06, "-9": 2.7650989222923704e-07, "0": 0.22595588063176542, "1": 0.2268637445230338, "10": 1.7657134868175842e-05, "11": 3.199277809098205e-06, "12": 5.326556072517573e-07, "13": 8.201803750507614e-08, "14": 1.174493018703552e-08, "15": 1.5712590725773029e-09, "16": 1.9601466694598145e-10, "17": 2.071942845168856e-11, "2": 0.1811940757341749, "3": 0.10513570817653946, "4": 0.04834590946650285, "5": 0.018325529083150563, "6": 0.005893513581732301, "7": 0.001643537581716711, "8": 0.0004042251374093652, "9": 8.886963065137187e-05} |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 57.7% |
| P home draw | 80.6% |
| P draw away | 40.3% |
| P home away | 79.1% |
| Raw p home draw | 81.4% |
| Raw p draw away | 41.2% |
| Raw p home away | 77.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1680 |
| Totals anchor target over 2 5 | 0.6955 |
| Totals anchor reference over odds | 1.40 |
| Totals anchor reference under odds | 3.01 |
| Totals anchor reference last update utc | 2026-10-30T11:42:07Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6034 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 8.4, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.9, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.68, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:42:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.25, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.25, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.63 |
| Reference draw odds | 4.66 |
| Reference away odds | 4.76 |
| Market reference 1x2 last update utc | 2026-10-30T11:42:07Z |
| Market reference home last update utc | 2026-10-30T11:42:07Z |
| Market reference draw last update utc | 2026-10-30T11:42:07Z |
| Market reference away last update utc | 2026-10-30T11:42:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.98 |
| Market reference over 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:42:07Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.0135 |
| Raw ev home | -0.0417 |
| Raw edge prob draw | 0.0244 |
| Raw ev draw | 0.0530 |
| Raw edge prob away | -0.0110 |
| Raw ev away | -0.1140 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.04934306703345167, 0.03868138141203966, 0.028171176483052233, 0.010884864949798147, 0.0031542954475105565, 0.0007312597678390372, 0.00014127318787941277, 2.3393813359247386e-05, 3.3896148146676837e-06, 4.365632311177965e-07, 5.060418916785547e-08, 5.332527463285842e-09, 5.150995496573911e-10, 4.592901518244737e-11, 3.802755586818558e-12, 2.938640565793342e-13, 2.1289516685100616e-14, 1.4516308734079485e-15], [0.07849540495279261, 0.1012580905981178, 0.05592570397925901, 0.02160874379537692, 0.006261939169161984, 0.001451704274143851, 0.00028045695891697664, 4.6441634472113226e-05, 6.729097552701037e-06, 8.666697340954446e-07, 1.0045994725191839e-07, 1.0586187358998131e-08, 1.022580826587748e-09, 9.117874465405167e-11, 7.549268784774796e-12, 5.833818920657107e-13, 4.2264163468952605e-14, 2.881792266013671e-15], [0.08846212292299702, 0.10254079325744997, 0.052819678751896415, 0.02144894817564547, 0.006215632430568925, 0.0014409689909478309, 0.0002783829932120511, 4.609820082173136e-05, 6.679336200359153e-06, 8.602607531489492e-07, 9.971705077994745e-08, 1.0507903013288674e-08, 1.0150188906206492e-09, 9.050448222832718e-11, 7.49344230566959e-12, 5.790678110684299e-13, 4.195162201546017e-14, 2.860481550988049e-15], [0.058538633189430915, 0.06785500601965175, 0.039327035763095645, 0.013505138324515121, 0.0041131120853851455, 0.0009535420631027027, 0.00018421624292242335, 3.0504871231103298e-05, 4.419961887214282e-06, 5.692661108719389e-07, 6.598643199440684e-08, 6.953465051030474e-09, 6.716752498705721e-10, 5.989013729384646e-11, 4.958685773792578e-12, 3.8319042166157725e-13, 2.7760927860643275e-14, 1.8928856184491715e-15], [0.029052871408051295, 0.03367661075895124, 0.01951810711377082, 0.007541465658592602, 0.001942338169772152, 0.0004732453327334013, 9.142698633875526e-05, 1.5139644588702484e-05, 2.1936382409575803e-06, 2.8252820769839877e-07, 3.2749232753793664e-08, 3.4510222559217755e-09, 3.3335412187218103e-10, 2.9723626306375906e-11, 2.461008265648056e-12, 1.9017837347355024e-13, 1.3777818568013242e-14, 9.39443910229228e-16], [0.01153521072924757, 0.013371029537675723, 0.0077495086606475284, 0.002994278753291891, 0.0008677039066305867, 0.00017878481390298115, 3.630035527109088e-05, 6.011075058426028e-06, 8.709665567228317e-07, 1.1217557008339272e-07, 1.3002821501887658e-08, 1.3702008450135199e-09, 1.3235559367785073e-10, 1.1801528608509074e-11, 9.77123691216397e-13, 7.550880542413459e-14, 5.4703729052863644e-15, 3.7299870710195467e-16], [0.003816636133806079, 0.004424050472722516, 0.002564067139101133, 0.000990712068703325, 0.0002870957593426655, 6.655736021499841e-05, 1.1428096966586351e-05, 1.988874482616908e-06, 2.881752669933108e-07, 3.711534571492823e-08, 4.30222208769065e-09, 4.533560919169564e-10, 4.3792276812197535e-11, 3.904752290929318e-12, 3.2329930285874674e-13, 2.4983473814793743e-14, 1.8099732536981195e-15, 1.2341346654194417e-16], [0.001082403512399545, 0.0012546670950087026, 0.000727173138882286, 0.00028096737161886954, 8.142077143665821e-05, 1.8875763354709255e-05, 3.646637460525721e-06, 5.366901533129405e-07, 8.172692136338843e-08, 1.0525965577362768e-08, 1.2201163892968237e-09, 1.2857244155713833e-10, 1.2419552866892226e-11, 1.10739338165235e-12, 9.168814859530749e-14, 7.0853492083111955e-15, 5.133110253290965e-16, 3.500023711434876e-17], [0.0002685997976379531, 0.0003113472230658643, 0.00018044893213487628, 6.972240785914847e-05, 2.0204667188237795e-05, 4.6840444984303705e-06, 9.049176880300372e-07, 1.4984779360487054e-07, 1.929698432315055e-08, 2.6120316422070854e-09, 3.0277342183910557e-10, 3.190541363590593e-11, 3.0819277178858084e-12, 2.748010652312392e-13, 2.2752529787992328e-14, 1.7582383480331162e-15, 1.2737877875421378e-16, 8.68535301160799e-18], [5.9247447793259664e-05, 6.867662785448304e-05, 3.980322688262473e-05, 1.5379292002383715e-05, 4.45672325497746e-06, 1.0332013810975608e-06, 1.9960574784581e-07, 3.3053261419454036e-08, 4.789207422490508e-09, 5.482141182735115e-10, 6.678542821457536e-11, 7.037661030793682e-12, 6.798082246292745e-13, 6.061531657505406e-14, 5.018727983539569e-15, 3.8783028002728397e-16, 2.8097070848809466e-17, 1.9158056098571093e-18], [1.176186315401422e-05, 1.3633753499766564e-05, 7.90177678733484e-06, 3.0531125757326132e-06, 8.847532002268161e-07, 2.0511218132826517e-07, 3.962593459062346e-08, 6.561766828607672e-09, 9.50758292848033e-10, 1.224522947391208e-10, 1.2615254212660324e-11, 1.3971235732782234e-12, 1.3495621510927828e-13, 1.203341384561961e-14, 9.963229463587069e-16, 7.699245875672778e-17, 5.5778588725966305e-18, 3.8032766392674235e-19], [2.1227063168034316e-06, 2.4605331907656364e-06, 1.426062459732144e-06, 5.510063555031036e-07, 1.5967463507620766e-07, 3.701734302275432e-08, 7.15143685684258e-09, 1.1842259779840223e-09, 1.7158681473801874e-10, 2.209941198483468e-11, 2.561651428397993e-12, 2.3991446139986527e-13, 2.4356040072322827e-14, 2.171714059952218e-15, 1.7981003384570387e-16, 1.389510967855086e-17, 1.006656522700487e-18, 6.863911984869984e-20], [3.511681676360185e-07, 4.0705627771907596e-07, 2.359194660864736e-07, 9.115528167326017e-08, 2.641564147324025e-08, 6.123933592297479e-09, 1.1830920542809386e-09, 1.9591144731781144e-10, 2.838632308438684e-11, 3.655997982911979e-12, 4.2378468990819677e-13, 4.4657241517289626e-14, 3.833890682197233e-15, 3.5927572317740504e-16, 2.9746724550786536e-17, 2.2987260019399422e-18, 1.6653539103229212e-19, 1.1355256143824379e-20], [5.362635322275861e-08, 6.21609409459058e-08, 3.6026900460952316e-08, 1.3920183500792119e-08, 4.033892165641834e-09, 9.3517652281527e-10, 1.8066817623307077e-10, 2.991733716917127e-11, 4.334831937262816e-12, 5.583018544452535e-13, 6.471551115922738e-14, 6.8195389795193515e-15, 6.587385590428694e-16, 5.22034026501239e-17, 4.542576762350504e-18, 3.510349282858157e-19, 2.5431364590097104e-20, 1.734043780228924e-21], [7.604255560459659e-09, 8.814466254451619e-09, 5.108640466718473e-09, 1.973892059167548e-09, 5.720088181916208e-10, 1.3260870535219155e-10, 2.56188776814938e-11, 4.2422999859380364e-12, 6.146822948348382e-13, 7.91676055883381e-14, 9.176706152968365e-15, 9.670155453116562e-16, 9.340960273176006e-17, 8.328896938284919e-18, 6.128984609963628e-19, 4.977700598518632e-20, 3.606185839096941e-21, 2.4588865856890297e-22], [1.006402994239509e-09, 1.1665711601316818e-09, 6.761149755319128e-10, 2.6123936299317756e-10, 7.570384540372444e-11, 1.7550409381638824e-11, 3.3905903086393075e-12, 5.614571175790661e-13, 8.135156651552618e-14, 1.0477621994342839e-14, 1.2145126470532805e-15, 1.2798193492315694e-16, 1.2362512429064625e-17, 1.1023073528706516e-18, 9.126704389085229e-20, 6.268329297130473e-21, 4.772691024645018e-22, 3.2542709837374496e-23], [1.2487008657044142e-10, 1.447430528227902e-10, 8.388939223103066e-11, 3.241343881057826e-11, 9.393002389089357e-12, 2.177578118681927e-12, 4.206896320738999e-13, 6.966314615415739e-14, 1.0093746949859767e-14, 1.3000175605345884e-15, 1.5069142306461305e-16, 1.5879439334720366e-17, 1.533886530625801e-18, 1.3676948038514573e-19, 1.1324016062065495e-20, 8.750815614610997e-22, 5.634529133448677e-23, 4.037757258165143e-24], [1.4581962152206507e-11, 1.6902668813848426e-11, 9.79635696652157e-12, 3.785146234299137e-12, 1.0968872457377532e-12, 2.5429118039555675e-13, 4.9126900294625163e-14, 8.135057710963531e-15, 1.1787181385012847e-15, 1.5181223450362013e-16, 1.759730202918332e-17, 1.8543543112427356e-18, 1.7912276630598086e-19, 1.5971538431088435e-20, 1.322385353956385e-21, 1.0218945593603922e-22, 7.403301215248576e-24, 4.486478353359183e-25]] |
| Legacy trial inputs | {"lambda_home": 1.9852100963161365, "lambda_away": 1.1591491348981973, "rho": -0.10285845637220993, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5782 |
| Legacy p draw | 0.2191 |
| Legacy p away | 0.2027 |
| Legacy p over 1 5 | 0.8335 |
| Legacy p under 3 5 | 0.6123 |
| Legacy p btts yes | 0.5975 |
| Legacy p over 2 5 | 0.6156 |
| Legacy goal margin distribution | {"-1": 0.12068076462197667, "-10": 6.226782391681266e-08, "-11": 6.450767230035555e-09, "-12": 6.141690778560491e-10, "-13": 5.408605215006147e-11, "-14": 4.429981986518178e-12, "-15": 3.3898870159927486e-13, "-16": 2.4171308951114287e-14, "-17": 1.4516308734079485e-15, "-2": 0.05704683184467878, "-3": 0.01878803833203535, "-4": 0.004917197833846686, "-5": 0.0010625308865497023, "-6": 0.0001949975890191721, "-7": 3.1052745473168533e-05, "-8": 4.363300550758534e-06, "-9": 5.482334828883419e-07, "0": 0.21905908233683355, "1": 0.22884276229829723, "10": 1.4472825982419387e-05, "11": 2.56784131759305e-06, "12": 4.1870863570520543e-07, "13": 6.315044477879845e-08, "14": 8.85850125905667e-09, "15": 1.1609424040288207e-09, "16": 1.4177275538428985e-10, "17": 1.4581962152206507e-11, "2": 0.1791364252766467, "3": 0.10104177583649127, "4": 0.04529021416413086, "5": 0.016760825935911362, "6": 0.005268054437129995, "7": 0.0014367730584855804, "8": 0.0003457565856438505, "9": 7.44025889967348e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5551 |
| Legacy raw p draw | 0.2366 |
| Legacy raw p away | 0.2083 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9852 |
| Legacy lambda away | 1.1591 |
| Legacy model home team | Man City |
| Legacy model away team | Brighton |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 79.8% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:41:52Z |
| Market reference home draw last update utc | 2026-10-30T11:42:12Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 41.8% |
| Market draw away odds | 2.37 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:41:52Z |
| Market reference draw away last update utc | 2026-10-30T11:42:12Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.5% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:41:52Z |
| Market reference home away last update utc | 2026-10-30T11:42:12Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.21 |
| Market reference dc draw away odds | 2.31 |
| Market reference dc home away odds | 1.23 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:52Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.24, "price": 1.64, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:52Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.64, "price": 2.24, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:52Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.04, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:52Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.04, "price": 1.78, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 87.5% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.70 |
| Market reference over 1 5 last update utc | 2026-10-30T11:42:11Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.0% |
| Market under 3 5 odds | 1.82 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 3 5 odds | 1.86 |
| Market reference under 3 5 opposite odds | 2.01 |
| Market reference under 3 5 last update utc | 2026-10-30T11:42:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.7% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:41:52Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.51 |
| Market reference btts yes last update utc | 2026-10-30T11:42:08Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 10.24924717794746, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,654.7730 |
| Elo away rating | 1,529.0307 |
| Elo rating diff | 185.7423 |
| Elo home expectancy | 0.7444 |

</details>


---

## 2026-10-31 — Tottenham Hotspur vs Crystal Palace

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **56.5%**. Expected goals are 1.62 for Tottenham Hotspur and 1.21 for Crystal Palace (2.83 combined). The most likely exact score is 2-1 at 11.4%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 58.3%; Under 3.5 goals: 64.7%; Double Chance 1X: 79.3%; Double Chance X2: 43.5%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 81.3%; BTTS Yes (both teams score): 58.9%; BTTS No (at least one team does not score): 41.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 56.5% | 1.77 |
| Draw | 22.8% | 4.39 |
| Crystal Palace win | 20.7% | 4.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.62 |
| Crystal Palace expected goals | 1.21 |
| Expected total goals | 2.83 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 58.3% |
| Under 2.5 | 41.7% |
| Over 3.5 | 35.3% |
| Under 3.5 | 64.7% |
| Over 4.5 | 18.7% |
| Under 4.5 | 81.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.40% |
| 2 | 1-1 | 10.64% |
| 3 | 1-0 | 9.49% |
| 4 | 2-0 | 8.94% |
| 5 | 3-1 | 6.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 56.5% | 61.0% | 1.61 | -9.1% |
| Draw | 22.8% | 21.3% | 4.43 | +1.0% |
| Crystal Palace win | 20.7% | 17.7% | 5.29 | +9.6% |

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
| Market best home last update utc | 2026-10-30T11:42:07Z |
| Market best draw last update utc | 2026-10-30T11:42:07Z |
| Market best away last update utc | 2026-10-30T11:42:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Tottenham |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6563 |
| Dc lambda away | 1.2166 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:41:52.235573+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.5392 |
| Shot lambda away | 1.2062 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.9% |
| P btts no | 41.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.84 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.26 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.40 |
| Fair Over 3.5 odds | 2.83 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.35 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.11716032489107181, "-10": 1.4321576368873693e-07, "-11": 1.632461688716442e-08, "-12": 1.7098379140428148e-09, "-13": 1.6556168332089323e-10, "-14": 1.4789953227216268e-11, "-15": 1.0976146805836619e-12, "-2": 0.059980388857731555, "-3": 0.021883955024962976, "-4": 0.0063288443242455516, "-5": 0.0015088872394278404, "-6": 0.00030523859705793764, "-7": 5.3546269876077525e-05, "-8": 8.284588132561258e-06, "-9": 1.1458000113163052e-06, "0": 0.22795449394178055, "1": 0.25841417217547774, "10": 4.226668635075433e-06, "11": 6.436568054267597e-07, "12": 9.006795458589395e-08, "13": 1.1651428657170759e-08, "14": 1.3905612953851877e-09, "15": 1.3787236754228127e-10, "2": 0.1744153635374346, "3": 0.08501689973624237, "4": 0.03284791838513329, "5": 0.010462710658799853, "6": 0.002827683957826376, "7": 0.0006627116899243027, "8": 0.00013698415053865821, "9": 2.5311169399425214e-05} |
| Raw goal margin distribution | {"-1": 0.15978956502616137, "-10": 1.338194385440863e-07, "-11": 1.4548051717426774e-08, "-12": 1.452973673919975e-09, "-13": 1.3414399196096317e-10, "-14": 1.1439085534346572e-11, "-15": 8.180975963828692e-13, "-2": 0.0795732317014566, "-3": 0.027986881065056046, "-4": 0.007770980079955715, "-5": 0.0017746232870717586, "-6": 0.0003433547233081533, "-7": 5.755183468433627e-05, "-8": 8.502171107363578e-06, "-9": 1.1222308680121466e-06, "0": 0.2627068100650511, "1": 0.2164182376751997, "10": 2.4241478277020715e-06, "11": 3.5208597253962296e-07, "12": 4.697920049647349e-08, "13": 5.794595062535765e-09, "14": 6.601568937733716e-10, "15": 6.307611870056648e-11, "2": 0.14202832842555313, "3": 0.06673696790045827, "4": 0.024756643020949327, "5": 0.007553115476761027, "6": 0.0019523917512609449, "7": 0.00043720699395300425, "8": 8.629025618230617e-05, "9": 1.5216617267832368e-05} |
| Unadjusted home-win probability | 46.0% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.3% |
| P home draw | 79.3% |
| P draw away | 43.5% |
| P home away | 77.2% |
| Raw p home draw | 72.3% |
| Raw p draw away | 54.0% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0500 |
| Totals anchor target over 2 5 | 0.5833 |
| Totals anchor reference over odds | 1.67 |
| Totals anchor reference under odds | 2.30 |
| Totals anchor reference last update utc | 2026-10-30T11:42:07Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5536 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.61, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.58, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.24, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 4.15, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.24, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.61 |
| Reference draw odds | 4.43 |
| Reference away odds | 5.29 |
| Market reference 1x2 last update utc | 2026-10-30T11:42:07Z |
| Market reference home last update utc | 2026-10-30T11:42:07Z |
| Market reference draw last update utc | 2026-10-30T11:42:07Z |
| Market reference away last update utc | 2026-10-30T11:42:07Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:42:07Z |
| Home probability edge | -4.5% |
| Draw probability edge | +1.5% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | -0.6% |
| Under 2.5 probability edge | +0.6% |
| Raw edge prob home | -0.1498 |
| Raw ev home | -0.2594 |
| Raw edge prob draw | 0.0496 |
| Raw ev draw | 0.1638 |
| Raw edge prob away | 0.1001 |
| Raw ev away | 0.4669 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.06539299814587164, 0.05007639226197826, 0.035441288402174705, 0.013946726821912654, 0.004116198884429996, 0.0009718749623495777, 0.00019122434900129776, 3.2249961364136867e-05, 4.759082782829104e-06, 6.242589786033543e-07, 7.369683637268345e-08, 7.909339316327995e-09, 7.781136053442088e-10, 7.066163861463049e-11, 5.95853803961168e-12, 4.689564405979091e-13], [0.1005323740432956, 0.11487724367801942, 0.05718994011829306, 0.022505177090075382, 0.0066421165349364545, 0.0015682689147336463, 0.0003085697377715181, 5.20402457806551e-05, 7.679508043824258e-06, 1.0073373518340256e-06, 1.189211185336815e-07, 1.2762928840033467e-08, 1.255605326473793e-09, 1.1402336267163515e-10, 9.615012575475487e-12, 7.567329508889021e-13], [0.09232290144948843, 0.10899171649555811, 0.049607623901528515, 0.018157772871118544, 0.005359035520678636, 0.0012653208921927098, 0.00024896223615261795, 4.198744845509479e-05, 6.1960304628387915e-06, 8.127464523379585e-07, 9.594870776938737e-08, 1.0297468983248949e-08, 1.0130556290504361e-09, 9.199706863474376e-11, 7.757646776102204e-12, 6.105521850077546e-13], [0.049659041224540956, 0.0586249354993207, 0.03460480687453388, 0.010500261241944116, 0.0028825411860648833, 0.0006805962698437149, 0.0001339128835245814, 2.2584390232640316e-05, 3.332747642804158e-06, 4.3716357423874844e-07, 5.160930559757492e-08, 5.538847119393959e-09, 5.449067398872097e-10, 4.948378086199086e-11, 4.1727165742365346e-12, 3.28406447902008e-13], [0.020033114779407113, 0.023650075249798314, 0.013960037305234173, 0.0054935030721926, 0.001250185074011235, 0.00027456154722289465, 5.402223039222831e-05, 9.110842066153616e-06, 1.344474528962502e-06, 1.7635757445459346e-07, 2.081987725149185e-08, 2.2344442694067206e-09, 2.198225941349498e-10, 1.9962412428482308e-11, 1.6833291181688066e-12, 1.3248350960644476e-13], [0.00646529901292688, 0.007632602810489798, 0.004505331118190901, 0.001772921504281859, 0.0005232552133050335, 9.526392889576361e-05, 1.743462645110043e-05, 2.9403474629809396e-06, 4.339030620411516e-07, 5.6915984588453826e-08, 6.7192113321138166e-09, 7.211235241503937e-10, 7.094347616580562e-11, 6.442481201284549e-12, 5.432618045654682e-13, 4.2756481621525756e-14], [0.0017387914871131835, 0.0020527286928045314, 0.0012116734862955758, 0.00047681334038866363, 0.00014072538774513677, 3.322664544557687e-05, 5.0410403768032765e-06, 7.907834003599434e-07, 1.166948271071451e-07, 1.530710788243444e-08, 1.8070792149031378e-09, 1.9394051882870646e-10, 1.9079691778629104e-11, 1.7326548155441018e-12, 1.4610600363006988e-13, 1.1499020557869607e-14], [0.0004008294341325313, 0.00047319882025100615, 0.00027931721627622226, 0.00010991589436185769, 3.24402770291988e-05, 7.659467849238384e-06, 1.5070629555329e-06, 1.9598294700824225e-07, 2.6900707682442104e-08, 3.528622860299537e-09, 4.1657124762259356e-10, 4.470752760961717e-11, 4.398285887486174e-12, 3.994147972363179e-13, 3.3680626568764884e-14, 2.6507755170469127e-15], [8.084995061255361e-05, 9.54473349244176e-05, 5.6340131782092874e-05, 2.2170763606528296e-05, 6.543418652236686e-06, 1.544965375782781e-06, 3.039845758546678e-07, 5.126695882510255e-08, 5.833544267729932e-09, 7.117465926696806e-10, 8.402517861440427e-11, 9.017804311376455e-12, 8.871633829804324e-13, 8.05646089847835e-14, 6.7936053662769114e-15, 5.3467897162299585e-16], [1.4495973615197932e-05, 1.711320833497806e-05, 1.0101491189571393e-05, 3.975102048103451e-06, 1.1732007678096104e-06, 2.770042177399196e-07, 5.4502845798055334e-08, 9.191897791273772e-09, 1.3564358116912945e-09, 1.3719606866879797e-10, 1.506527540188224e-11, 1.6168451851154745e-12, 1.5906375816706135e-13, 1.444481335256159e-14, 1.2180579381371463e-15, 9.586514532817362e-17], [2.339147080664977e-06, 2.7614779372671267e-06, 1.6300301210313889e-06, 6.414435206627266e-07, 1.8931388976719577e-07, 4.469886773102899e-08, 8.79486787302032e-09, 1.4832533126085793e-09, 2.1888166695478606e-10, 2.871117231689915e-11, 2.6135803414505395e-12, 2.6090270271221413e-13, 2.5667370501143188e-14, 2.330891589714967e-15, 1.9655228035784493e-16, 1.5469307601168613e-17], [3.4314287478150794e-07, 4.050970056017899e-07, 2.39118448914359e-07, 9.409702173478007e-08, 2.77715381421495e-08, 6.557132768386386e-09, 1.2901695110227044e-09, 2.175869187212513e-10, 3.2109004626798474e-11, 4.2118062128728e-12, 4.972243955513217e-13, 4.114761545401074e-14, 3.7652935014845316e-15, 3.4193182955877075e-16, 2.883337909118494e-17, 2.269281279925079e-18], [4.614279311294555e-08, 5.4473832021309583e-08, 3.2154516175716055e-08, 1.2653328177707168e-08, 3.734468739114668e-09, 8.817447278729685e-10, 1.73490488082135e-10, 2.925914804738664e-11, 4.31773254362447e-12, 5.663661319972177e-13, 6.686230168480962e-14, 7.175838984750063e-15, 5.443476699869445e-16, 4.597994255339723e-17, 3.877255638773866e-18, 3.051527055059401e-19], [5.727573455862321e-09, 6.76168158179445e-09, 3.991248489950167e-09, 1.570621579442658e-09, 4.6354896569752544e-10, 1.0944846112479677e-10, 2.153488003969691e-11, 3.631854692609435e-12, 5.359478401284355e-13, 7.030141448061994e-14, 8.299427028407032e-15, 8.90716450388992e-16, 8.762787393895053e-17, 6.135978816943711e-18, 4.812726967757695e-19, 3.7877736004456274e-20], [6.601654207191191e-10, 7.793576809818489e-10, 4.600349971706828e-10, 1.8103129776921954e-10, 5.342908307014394e-11, 1.2615130987374357e-11, 2.4821302164167315e-12, 4.1861093526145575e-13, 6.177384438426602e-14, 8.103006137834026e-15, 9.565996452351147e-16, 1.0266480294733458e-16, 1.0100069900704519e-17, 9.172021725418626e-19, 5.963784861049607e-20, 4.365822929721791e-21], [7.101852590809952e-11, 8.384085552102111e-11, 4.948912248328616e-11, 1.9474779361808297e-11, 5.747733221363993e-12, 1.3570962348876146e-12, 2.6701978557109103e-13, 4.503285179477513e-14, 6.645436477221185e-15, 8.71695992053631e-16, 1.029079902652364e-16, 1.1044357579382153e-17, 1.0865338495546355e-18, 9.866973368988961e-20, 8.320318819040676e-21, 5.049328639974838e-22]] |
| Legacy trial inputs | {"lambda_home": 1.6136529651327194, "lambda_away": 1.1805490813694746, "rho": -0.10285845637220993, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5361 |
| Legacy p draw | 0.2417 |
| Legacy p away | 0.2222 |
| Legacy p over 1 5 | 0.7840 |
| Legacy p under 3 5 | 0.6884 |
| Legacy p btts yes | 0.5586 |
| Legacy p over 2 5 | 0.5414 |
| Legacy goal margin distribution | {"-1": 0.12859946102231343, "-10": 8.752403070822912e-08, "-11": 9.261246911520373e-09, "-12": 9.002230212398481e-10, "-13": 8.088720337511373e-11, "-14": 6.715270990500582e-12, "-15": 4.689564405979091e-13, "-2": 0.06404318016974565, "-3": 0.021997637610552952, "-4": 0.005957417668751001, "-5": 0.0013259481714253843, "-6": 0.0002499193493058021, "-7": 4.0796132320512356e-05, "-8": 5.868134103384027e-06, "-9": 7.540429900334256e-07, "0": 0.24172881896699014, "1": 0.2501804420598966, "10": 2.778024010201231e-06, "11": 4.0179473432375825e-07, "12": 5.33839844712725e-08, "13": 6.556420259327456e-09, "14": 7.440062762401401e-10, "15": 7.101852590809952e-11, "2": 0.1668294940135544, "3": 0.0783253021941067, "4": 0.02899413641026812, "5": 0.008820734905222515, "6": 0.0022725015894019098, "7": 0.0005070483790101894, "8": 9.969113253466115e-05, "9": 1.750969976067359e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4624 |
| Legacy raw p draw | 0.2704 |
| Legacy raw p away | 0.2672 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6137 |
| Legacy lambda away | 1.1805 |
| Legacy model home team | Tottenham |
| Legacy model away team | Crystal Palace |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 82.5% |
| Market home draw odds | 1.18 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:41:13Z |
| Market reference home draw last update utc | 2026-10-30T11:42:12Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.7% |
| Market draw away odds | 2.44 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:41:13Z |
| Market reference draw away last update utc | 2026-10-30T11:42:12Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.8% |
| Market home away odds | 1.24 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:41:13Z |
| Market reference home away last update utc | 2026-10-30T11:42:12Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.17 |
| Market reference dc draw away odds | 2.43 |
| Market reference dc home away odds | 1.24 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:13Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.3, "price": 1.59, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:13Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.59, "price": 2.3, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:13Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.83, "price": 1.99, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:13Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.99, "price": 1.83, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:13Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.5, "price": 2.52, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:41:13Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.52, "price": 1.5, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 81.5% |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-30T11:42:11Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.5% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market reference under 3 5 last update utc | 2026-10-30T11:42:11Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.6% |
| Market btts yes odds | 1.74 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:41:13Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.05 |
| Market reference btts yes last update utc | 2026-10-30T11:42:08Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 10.0289616681416, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,397.3033 |
| Elo away rating | 1,450.5828 |
| Elo rating diff | 6.7205 |
| Elo home expectancy | 0.5097 |

</details>


---

## 2026-11-01 — Liverpool vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **40.2%**. Expected goals are 1.24 for Liverpool and 1.39 for Arsenal (2.63 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 52.3%; Under 3.5 goals: 69.8%; Double Chance 1X: 59.8%; Double Chance X2: 67.7%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 32.3% | 3.10 |
| Draw | 27.6% | 3.63 |
| Arsenal win | 40.2% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.24 |
| Arsenal expected goals | 1.39 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 52.3% |
| Under 2.5 | 47.7% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.09% |
| 2 | 1-2 | 8.78% |
| 3 | 0-1 | 8.26% |
| 4 | 2-1 | 7.70% |
| 5 | 0-0 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 32.3% | 32.2% | 3.00 | -3.2% |
| Draw | 27.6% | 27.4% | 3.51 | -3.2% |
| Arsenal win | 40.2% | 40.4% | 2.41 | -3.2% |
| Over 2.5 | 52.3% | 52.3% | 1.86 | -2.8% |
| Under 2.5 | 47.7% | 47.7% | 2.03 | -3.1% |

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
| Market best home last update utc | 2026-10-30T11:42:07Z |
| Market best draw last update utc | 2026-10-30T11:42:07Z |
| Market best away last update utc | 2026-10-30T11:42:07Z |
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
| Dc lambda home | 1.1857 |
| Dc lambda away | 1.4390 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:41:52.235573+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.3547 |
| Shot lambda away | 1.2844 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.77 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.77 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.2034144938951526, "-10": 9.6032352895864e-07, "-11": 1.264927901306222e-07, "-12": 1.5305882099826903e-08, "-13": 1.7119947153322925e-09, "-14": 1.7691745769544827e-10, "-15": 1.5369489182913735e-11, "-2": 0.12209663716086229, "-3": 0.05216913003610729, "-4": 0.017579898486197305, "-5": 0.004869359119185241, "-6": 0.0011422821906915803, "-7": 0.00023208556538494745, "-8": 4.155312958295628e-05, "-9": 6.64642375868039e-06, "0": 0.27584863850433766, "1": 0.17737210061349798, "10": 2.885851345207029e-07, "11": 3.374774744401068e-08, "12": 3.625434085110775e-09, "13": 3.6002006112093336e-10, "14": 3.3030686739750106e-11, "15": 2.547586733119421e-12, "2": 0.09505589065261137, "3": 0.036058824025981734, "4": 0.010787901171497223, "5": 0.002652864286875274, "6": 0.0005525088837817789, "7": 9.966361173090822e-05, "8": 1.5842177006144366e-05, "9": 2.2496853597196906e-06} |
| Raw goal margin distribution | {"-1": 0.20628141080404205, "-10": 6.372359926404364e-07, "-11": 7.964580279982099e-08, "-12": 9.140464010111724e-09, "-13": 9.640434496299762e-10, "-14": 8.539297419423747e-11, "-2": 0.11982692450435067, "-3": 0.04910903205991197, "-4": 0.015807661521108258, "-5": 0.004172455643899739, "-6": 0.000931361356726872, "-7": 0.0001798841373851973, "-8": 3.0595274244423206e-05, "-9": 4.646577005345137e-06, "0": 0.2800850788643836, "1": 0.1820842525329164, "10": 1.938771445853685e-07, "11": 2.151353824092319e-08, "12": 2.1919963335218305e-09, "13": 2.052536175367524e-10, "14": 1.614131763727644e-11, "2": 0.09444950282971566, "3": 0.03436602244160148, "4": 0.009821055264412465, "5": 0.0023014677151786925, "6": 0.0004560936279430149, "7": 7.820801979277465e-05, "8": 1.1809605873978024e-05, "9": 1.5923437374444504e-06} |
| Unadjusted home-win probability | 32.4% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 39.6% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 73.0% |
| Raw p btts yes | 54.3% |
| P home draw | 59.8% |
| P draw away | 67.7% |
| P home away | 72.4% |
| Raw p home draw | 60.4% |
| Raw p draw away | 67.6% |
| Raw p home away | 72.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0554 |
| Totals anchor target over 2 5 | 0.5228 |
| Totals anchor reference over odds | 1.86 |
| Totals anchor reference under odds | 2.03 |
| Totals anchor reference last update utc | 2026-10-30T11:42:07Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4904 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:41:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:42:07Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.00 |
| Reference draw odds | 3.51 |
| Reference away odds | 2.41 |
| Market reference 1x2 last update utc | 2026-10-30T11:42:07Z |
| Market reference home last update utc | 2026-10-30T11:42:07Z |
| Market reference draw last update utc | 2026-10-30T11:42:07Z |
| Market reference away last update utc | 2026-10-30T11:42:07Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 2.03 |
| Market reference over 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market best over 2 5 last update utc | 2026-10-30T11:42:07Z |
| Market best under 2 5 last update utc | 2026-10-30T11:42:07Z |
| Home probability edge | +0.0% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0014 |
| Raw ev home | -0.0293 |
| Raw edge prob draw | 0.0061 |
| Raw ev draw | -0.0169 |
| Raw edge prob away | -0.0074 |
| Raw ev away | -0.0448 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.09617940454480167, 0.10453291081672601, 0.083340169327013, 0.03963613183840871, 0.014138046752826499, 0.004034386943711059, 0.0009593662580683979, 0.0001955440205049284, 3.4874877742930346e-05, 5.528767472834684e-06, 7.888355335491916e-07, 1.023179713360064e-07, 1.2165467847201717e-08, 1.335191636955819e-09, 1.3607354784427013e-10], [0.08482535736404732, 0.1345844397294774, 0.08523599103460236, 0.040537774344668556, 0.01445965896160124, 0.0041261611554323134, 0.000981189916362614, 0.00019999225479406106, 3.566821126754968e-05, 5.654535844507726e-06, 8.06779959872017e-07, 1.0464549997797705e-07, 1.2442207842019915e-08, 1.3655645688753628e-09, 1.391689481526092e-10], [0.050838354768247614, 0.07253533614032111, 0.04451863697059026, 0.020729963704819027, 0.007394293601554797, 0.0021100115232052796, 0.0005017550095570672, 0.00010227083874601162, 1.8239795769383832e-05, 2.891582597199485e-06, 4.125662929524358e-07, 5.351298761426467e-08, 6.362621558349304e-09, 6.983142120405072e-10, 7.116738130495945e-11], [0.017331608459770477, 0.024728456520923293, 0.017641079399138816, 0.007218153719545562, 0.002520832983737237, 0.0007193366845269837, 0.00017105630990645133, 3.486576507202921e-05, 6.218238180645894e-06, 9.857867673374979e-07, 1.406504495620808e-07, 1.8243433586136717e-08, 2.1691194793714985e-09, 2.380664866153062e-10, 2.4262098832811284e-11], [0.0044314669481161145, 0.0063227448280267235, 0.004510594643759397, 0.0021452143115783056, 0.0006583137422601766, 0.00018392503785485194, 4.373687447282575e-05, 8.914722825415411e-06, 1.5899226570348503e-06, 2.520528598073467e-07, 3.596249130130003e-08, 4.6646087779314476e-09, 5.546156493011917e-10, 6.087050543165963e-11, 6.2035032304759104e-12], [0.0009064547867131146, 0.0012933149184305368, 0.0009226403251177107, 0.000438802726957557, 0.00015651914506404998, 3.842551434282356e-05, 8.946360129937887e-06, 1.8235029781173774e-06, 3.2521804175602554e-07, 5.155731137162764e-08, 7.35611317061729e-09, 9.541438544853573e-10, 1.1344640860038171e-10, 1.2451037470025775e-11, 1.2689240974810082e-12], [0.00015451246919194892, 0.00022045587316505815, 0.00015727142368229214, 7.47974348243262e-05, 2.6679940284008105e-05, 7.613300806157969e-06, 1.5575570601045825e-06, 3.108306689509062e-07, 5.543601665970091e-08, 8.788356133916678e-09, 1.2539083320073211e-09, 1.626414522619931e-10, 1.9337847811874895e-11, 2.1223789335055265e-12, 2.16298262630289e-13], [2.2575331140055358e-05, 3.221011459138961e-05, 2.2978433307443968e-05, 1.0928418065005318e-05, 3.8981222024233215e-06, 1.1123554472121673e-06, 2.6451510425827053e-07, 4.638469045893178e-08, 8.099582122551336e-09, 1.2840390871848392e-09, 1.83204604536957e-10, 2.3763031301717866e-11, 2.8253921523106313e-12, 3.100941139516873e-13, 3.160265918623913e-14], [2.886109330883669e-06, 4.117853762335281e-06, 2.937643322539521e-06, 1.397127207283665e-06, 4.983495830711062e-07, 1.4220741284109647e-07, 3.381653654705103e-08, 6.892697611938277e-09, 1.0576000576474905e-09, 1.6415605014839337e-10, 2.3421517732548648e-11, 3.037949075674133e-12, 3.612080196565042e-13, 3.964351664105309e-14, 4.0401945376699185e-15], [3.279736144294465e-07, 4.679474085312931e-07, 3.3382986849733096e-07, 1.5876767213466724e-07, 5.663178184562907e-08, 1.6160260697357078e-08, 3.842866103560249e-09, 7.832769620908484e-10, 1.3969585068996643e-10, 1.905299370574206e-11, 2.661590031939431e-12, 3.452284804804584e-13, 4.1047197519497337e-14, 4.5050363485291564e-15, 4.591223178340225e-16], [3.354343563834508e-08, 4.7859227357377654e-08, 3.414238284862481e-08, 1.623793182559424e-08, 5.792004130357577e-09, 1.6527874217676878e-09, 3.9302836002766513e-10, 8.010949420611039e-11, 1.4287365112326061e-11, 2.264997746739174e-12, 2.780289381473863e-13, 3.530817360312696e-14, 4.198093894000996e-15, 4.607516890289372e-16, 4.6956642976248625e-17], [3.1187710477623853e-09, 4.449811708608601e-09, 3.1744594166789882e-09, 1.5097556553005864e-09, 5.385236916408656e-10, 1.536713655300819e-10, 3.654263336110338e-11, 7.448347684913294e-12, 1.3283976376646222e-12, 2.1059290026040074e-13, 3.004705183475748e-14, 3.3529834343720443e-15, 3.9032655550140655e-16, 4.2839351444024083e-17, 4.365892039008333e-18], [2.658097361819343e-10, 3.7925300004729636e-10, 2.705560001504757e-10, 1.2867496404475e-10, 4.5897835464864106e-11, 1.3097256741425533e-11, 3.1144920817695403e-12, 6.34815221379779e-13, 1.1321800164384502e-13, 1.7948622198531574e-14, 2.5608801668760058e-15, 3.321656446312033e-16, 3.3977834193879115e-17, 3.651155064335706e-18, 3.7210061056589256e-19], [2.0912028813835362e-11, 2.983694193689806e-11, 2.1285431271901348e-11, 1.0123235493079448e-11, 3.610916859256665e-12, 1.0303994665245263e-12, 2.4502619463813787e-13, 4.994276880764409e-14, 8.90719108573368e-15, 1.412070565870594e-15, 2.0147192728048113e-16, 2.6132442066529622e-17, 3.1071118746600067e-18, 2.9338355395056076e-19, 2.927424255247629e-20], [1.5276953949141545e-12, 2.179690894704744e-12, 1.5549737245642946e-12, 7.39537056977333e-13, 2.637898554182682e-13, 7.527421341778539e-14, 1.7900003510628747e-14, 3.648490473876067e-15, 6.507008442094854e-16, 1.0315659565977271e-16, 1.4718214968565775e-17, 1.9090644795059592e-18, 2.269851741625736e-19, 2.491221135605893e-20, 2.1842707539112985e-21]] |
| Legacy trial inputs | {"lambda_home": 1.0227479944293185, "lambda_away": 1.4267837043700893, "rho": -0.10285845637220993, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T11:42:07Z", "over": 1.86, "under": 2.03, "bookmaker": "pinnacle", "event_id": "6a3819cdbe2ba2fe5a3d8f9b4b459965", "kickoff_utc": "2026-11-01T16:30:00Z", "home_team": "Liverpool", "away_team": "Arsenal"}} |
| Legacy p home | 0.2898 |
| Legacy p draw | 0.2832 |
| Legacy p away | 0.4270 |
| Legacy p over 1 5 | 0.7145 |
| Legacy p under 3 5 | 0.7690 |
| Legacy p btts yes | 0.4984 |
| Legacy p over 2 5 | 0.4457 |
| Legacy goal margin distribution | {"-1": 0.21321288903497385, "-10": 9.000879250753637e-07, "-11": 1.1548275548889962e-07, "-12": 1.3602199797382039e-08, "-13": 1.4743605851084284e-09, "-14": 1.3607354784427013e-10, "-2": 0.13203719107904102, "-3": 0.05638610754862906, "-4": 0.018802471440893437, "-5": 0.005124325511480255, "-6": 0.0011786210316863182, "-7": 0.00023424924502840776, "-8": 4.096079059696167e-05, "-9": 6.391291679229866e-06, "0": 0.28319897923970294, "1": 0.17731139121074885, "10": 3.827419037245265e-08, "11": 3.52004901613856e-09, "12": 2.9720165184339663e-10, "13": 2.3091719708540105e-11, "14": 1.5276953949141545e-12, "2": 0.08054403556993314, "3": 0.02465583530167665, "4": 0.0058934966187290695, "5": 0.0011513445421486267, "6": 0.00018982494361859418, "7": 2.704380457233663e-05, "8": 3.3897558240538226e-06, "9": 3.791396623586206e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2574 |
| Legacy raw p draw | 0.2924 |
| Legacy raw p away | 0.4503 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0227 |
| Legacy lambda away | 1.4268 |
| Legacy model home team | Liverpool |
| Legacy model away team | Arsenal |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.786775718535143, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,570.2236 |
| Elo away rating | 1,650.6613 |
| Elo rating diff | -20.4377 |
| Elo home expectancy | 0.4706 |

</details>


---
