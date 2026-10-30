# Serie A — football model report

Fixtures in this report: **8**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,990 |
| Training data through | 2026-10-29 |
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
| Training sha256 | 46e47c50c3d2114f316aeaed676dbbfd15f50dd6b41b49297bd4758f25990547 |
| Training as of utc | 2026-10-30T11:54:12.994081+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 90, 'bbs_added_results': 2, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 90, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 162, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-30T11:54:12.994081+00:00', 'observations': 483, 'observations_sha256': '711d82b278033d23ba41dfcf34a64fd4aee6896bee7ad42dc000bc76f6a282de', 'eligible_training_matches': 211, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 202, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 26, 'retrospective_eligible_training_matches': 211, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '34335c19a9644417224e0777bfea27f54ced8ea7159b12237a12a5746f979303', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 151, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-27T00:00:00+00:00', 'audit_origin_utc': '2025-10-29T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 14, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1989, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1610, 'tuning_matches': 250, 'audit_matches': 129, 'audit_matchdays': 43, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8484185469679917, 'audit_candidate_poisson_score': 0.8461831964582414, 'audit_gain': 0.0022353505097503223, 'audit_gain_lower95': -0.0034427442353438848, 'audit_baseline_briers': [0.5603532207348766, 0.16261438493242025, 0.20598943106194342, 0.24319321493269438], 'audit_candidate_briers': [0.5631288064848636, 0.16062702433950166, 0.20517893615291022, 0.24312504824338985], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1808.546 |
| Base scoring parameter | 0.151 |
| Home-advantage parameter | 0.110 |
| Dixon-Coles low-score adjustment | -0.026 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1990, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-29'} |
| Training data health | {'training_end': '2026-10-29', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 8.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 20.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261030T115412994081Z_20647bc10abd2ca733be3d426b03a7093a37805ae97157a570167034f05731bd.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 3, 'ANCHORED_ALTERNATE': 3, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
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

## 2026-10-31 — AC Milan vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **48.9%**. Expected goals are 1.25 for AC Milan and 1.80 for Inter Milan (3.05 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 58.7%; Under 3.5 goals: 63.3%; Double Chance 1X: 51.1%; Double Chance X2: 73.9%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 80.6%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 26.1% | 3.84 |
| Draw | 25.0% | 4.00 |
| Inter Milan win | 48.9% | 2.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.25 |
| Inter Milan expected goals | 1.80 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 81.3% |
| Under 1.5 | 18.7% |
| Over 2.5 | 58.7% |
| Under 2.5 | 41.3% |
| Over 3.5 | 36.7% |
| Under 3.5 | 63.3% |
| Over 4.5 | 19.4% |
| Under 4.5 | 80.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.52% |
| 2 | 1-2 | 9.37% |
| 3 | 0-1 | 7.96% |
| 4 | 0-2 | 7.44% |
| 5 | 2-1 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 26.1% | 25.9% | 3.71 | -3.3% |
| Draw | 25.0% | 25.6% | 3.76 | -6.0% |
| Inter Milan win | 48.9% | 48.5% | 2.02 | -1.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T19:45:00+00:00 |
| Fixture id | e82f25e981f2ebc731cfaf5716231af5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T11:54:14Z |
| Market best draw last update utc | 2026-10-30T11:54:14Z |
| Market best away last update utc | 2026-10-30T11:54:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Milan |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2514 |
| Dc lambda away | 1.8001 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:54:12.994081+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.17 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.35 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.72 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.15 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.2163883125500791, "-10": 5.806885061477475e-06, "-11": 9.396032879525471e-07, "-12": 1.3972164705239622e-07, "-13": 1.9217119878730612e-08, "-14": 2.457307236628001e-09, "-15": 2.913652069396502e-10, "-16": 2.885552130247587e-11, "-2": 0.1497286212088854, "-3": 0.0771121587477148, "-4": 0.03154540416494303, "-5": 0.010651810224448773, "-6": 0.003054235935331863, "-7": 0.0007598305233655185, "-8": 0.00016677912218532334, "-9": 3.273238504201031e-05, "0": 0.2500213650076396, "1": 0.1514376281442365, "10": 1.549966689590246e-07, "11": 1.7435694482081605e-08, "12": 1.8024947433316118e-09, "13": 1.7235115470029078e-10, "14": 1.532148800110249e-11, "15": 1.262975026867254e-12, "16": 8.695640685565936e-14, "2": 0.07324184207640438, "3": 0.0262236344435762, "4": 0.007457988419000573, "5": 0.0017507519415859223, "6": 0.0003489951299831787, "7": 6.0359982820434306e-05, "8": 9.210636500869087e-06, "9": 1.2567277313930056e-06} |
| Raw goal margin distribution | {"-1": 0.22184269941096546, "-10": 5.702580534305902e-06, "-11": 9.177425569644274e-07, "-12": 1.3573016093036615e-07, "-13": 1.8566420245151737e-08, "-14": 2.361153665313918e-09, "-15": 2.784770563812447e-10, "-16": 2.7463265297340077e-11, "-2": 0.15301508624495386, "-3": 0.07848134143525208, "-4": 0.031958264527011546, "-5": 0.01073863595619643, "-6": 0.0030635699026184387, "-7": 0.000758208465758603, "-8": 0.0001655477947561532, "-9": 3.231785561339724e-05, "0": 0.23659229943623195, "1": 0.15339541797036857, "10": 1.5039288982571703e-07, "11": 1.682644366707344e-08, "12": 1.7300689692095817e-09, "13": 1.6452458980019154e-10, "14": 1.4545963055188891e-11, "15": 1.192678074151632e-12, "16": 8.177142680950156e-14, "2": 0.07395463991686202, "3": 0.02637018525073714, "4": 0.007465270316053349, "5": 0.001743922008134648, "6": 0.0003458767109994847, "7": 5.951106785661211e-05, "8": 9.033334696152048e-06, "9": 1.2259784202531873e-06} |
| Unadjusted home-win probability | 26.3% |
| Unadjusted draw probability | 23.7% |
| Unadjusted away-win probability | 50.0% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 59.9% |
| P home draw | 51.1% |
| P draw away | 73.9% |
| P home away | 75.0% |
| Raw p home draw | 50.0% |
| Raw p draw away | 73.7% |
| Raw p home away | 76.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0056 |
| Totals anchor target over 2 5 | 0.5871 |
| Totals anchor reference over odds | 1.66 |
| Totals anchor reference under odds | 2.32 |
| Totals anchor reference last update utc | 2026-10-30T11:54:14Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5836 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.66, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.56, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:22Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.74, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:22Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.49, "price": 2.74, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.71 |
| Reference draw odds | 3.76 |
| Reference away odds | 2.02 |
| Market reference 1x2 last update utc | 2026-10-30T11:54:14Z |
| Market reference home last update utc | 2026-10-30T11:54:14Z |
| Market reference draw last update utc | 2026-10-30T11:54:14Z |
| Market reference away last update utc | 2026-10-30T11:54:14Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-30T11:54:15Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:54:15Z |
| Home probability edge | +0.1% |
| Draw probability edge | -0.6% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0040 |
| Raw ev home | -0.0230 |
| Raw edge prob draw | -0.0192 |
| Raw ev draw | -0.1104 |
| Raw edge prob away | 0.0152 |
| Raw ev away | 0.0101 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.054533001532217844, 0.08277343097045803, 0.07582314088178946, 0.04437853331525333, 0.01948073697860413, 0.006841129435868349, 0.002002022648052551, 0.0005021845823503183, 0.00011022137318037755, 2.1503825986160342e-05, 3.7757929050447288e-06, 6.027093238266942e-07, 8.818994932087e-08, 1.1911547030543198e-08, 1.4939379623148167e-09, 1.7487741831974878e-10, 1.9191378890238256e-11], [0.05711681827739879, 0.11546946382938034, 0.09495969741742893, 0.0555789703042738, 0.024397365598990323, 0.008567721854681798, 0.0025073013683025802, 0.0006289279952413216, 0.0001380394972355457, 2.693105014135942e-05, 4.7287430671450245e-06, 7.548235849326549e-07, 1.1044769189691427e-07, 1.491783232189367e-08, 1.8709841772842855e-09, 2.1901370130095523e-10, 2.4034978124705298e-11], [0.03798072463707353, 0.06668922577099332, 0.06143973166919766, 0.034803109852006096, 0.015277436598639576, 0.005365039389133752, 0.0015700522063542045, 0.0003938297163037317, 8.643923699743253e-05, 1.6864009739085484e-05, 2.9611013577037316e-06, 4.7266453483173234e-07, 6.916146760087148e-08, 9.34142813748295e-09, 1.1715954343325262e-09, 1.3714464056714392e-10, 1.505051243996075e-11], [0.015855485441900675, 0.027840175732494536, 0.024441868640865325, 0.015011938669526562, 0.006377739653309431, 0.002239696707803211, 0.0006554361492243303, 0.00016440869396542476, 3.608504252928323e-05, 7.040072654357434e-06, 1.236145437394724e-06, 1.9731918552212054e-07, 2.8872241200361587e-08, 3.899685412948838e-09, 4.890958382274822e-10, 5.725258990515666e-11, 6.283007582535941e-12], [0.0049642895376645685, 0.00871664848244458, 0.007652652025031549, 0.004479021429254308, 0.0020632258927323274, 0.0007012401464988781, 0.00020521445591333785, 5.14757092959631e-05, 1.129808354028092e-05, 2.204218795475463e-06, 3.870322283336409e-07, 6.177985353127943e-08, 9.039784082618494e-09, 1.220976019095911e-09, 1.5313396499432027e-10, 1.7925558577933938e-11, 1.967184727414524e-12], [0.001243439474827544, 0.002183318424325062, 0.001916811971350034, 0.0011218910604383066, 0.0004924737938451439, 0.00018148333496543904, 5.1401465074082996e-05, 1.2893472157036896e-05, 2.829908077942948e-06, 5.52105722411271e-07, 9.69426031840438e-08, 1.5474421475020602e-08, 2.264256403048873e-09, 3.058261949555587e-10, 3.8356509137131454e-11, 4.489936973866051e-12, 4.927341819582562e-13], [0.0002595439749952574, 0.0004557255531945383, 0.00040009747835268166, 0.0002341730910370102, 0.00010279439299069307, 3.609872401147929e-05, 1.1085728322801982e-05, 2.6912632925636816e-06, 5.90688655370515e-07, 1.152414063677072e-07, 2.0234896097587902e-08, 3.229986615099099e-09, 4.726197930440275e-10, 6.383531157191951e-11, 8.006180477561019e-12, 9.37187626150437e-13, 1.0284874398025615e-13], [4.6435536029618795e-05, 8.153477785554307e-05, 7.158224679168555e-05, 4.189638001119073e-05, 1.839115217160924e-05, 6.458495518876683e-06, 1.8900467272763726e-06, 4.975057811538645e-07, 1.0568129866719441e-07, 2.0618072438743346e-08, 3.620266071721778e-09, 5.778834197301685e-10, 8.455736038028987e-11, 1.1420904340060195e-11, 1.4324018965657308e-12, 1.6767412836848455e-13, 1.8400876216770172e-14], [7.269390979304179e-06, 1.2764107606394325e-05, 1.1206058626606453e-05, 6.55879511597726e-06, 2.8790983614366213e-06, 1.0110646517540382e-06, 2.958830629404719e-07, 7.42188968400689e-08, 1.7094174710831148e-08, 3.2277183082637374e-09, 5.667454663960151e-10, 9.046650211588876e-11, 1.323728690006247e-11, 1.7879199010898354e-12, 2.2423967323197068e-13, 2.6249051921078012e-14, 2.8806206414019077e-15], [1.011563312225792e-06, 1.7761739607471995e-06, 1.5593655388186963e-06, 9.126812040536807e-07, 4.006374513367351e-07, 1.4069347912562395e-07, 4.117324986806879e-08, 1.0327840850908636e-08, 2.266793606541767e-09, 4.6408026459135805e-10, 7.886478011826239e-11, 1.2588756717910029e-11, 1.842018653231387e-12, 2.4879583204286e-13, 3.120380059797991e-14, 3.6526550820649426e-15, 4.008492823646993e-16], [1.2668658265857153e-07, 2.2244520592496157e-07, 1.9529246349771453e-07, 1.1430274447563453e-07, 5.017519811311777e-08, 1.762022787634657e-08, 5.156472422132314e-09, 1.2934423854936724e-09, 2.8388963116228073e-10, 5.538592971254811e-11, 1.0205236664385128e-11, 1.5765958978909407e-12, 2.306914906371579e-13, 3.115879486757272e-14, 3.9079144290230944e-15, 4.574527213319719e-16, 5.020172749463003e-17], [1.4423660371420155e-08, 2.532607663874957e-08, 2.2234652695467732e-08, 1.3013721984126995e-08, 5.712601930409451e-09, 2.0061175952657783e-09, 5.870803787633671e-10, 1.4726242737670035e-10, 3.232171503029668e-11, 6.305859884800449e-12, 1.1072271989440087e-12, 1.854674457625568e-13, 2.6264941730211618e-14, 3.5475254389317974e-15, 4.449281786747108e-16, 5.2082411175749284e-17, 5.7156223827791225e-18], [1.5053302643858813e-09, 2.6431646794739578e-09, 2.3205271587590204e-09, 1.3581815607518649e-09, 5.961976608429987e-10, 2.093691512630414e-10, 6.12708451961843e-11, 1.5369093768757987e-11, 3.373266880879215e-12, 6.581132308395002e-13, 1.1555614658150162e-13, 1.8445600360417582e-14, 2.8322734382736512e-15, 3.7023870982737555e-16, 4.643508205200384e-17, 5.435598715315942e-18, 5.965128913910787e-19], [1.4501936272812115e-10, 2.546351896798993e-10, 2.2355318146335074e-10, 1.308434627730505e-10, 5.743603704846837e-11, 2.0170046141655605e-11, 5.902664109253755e-12, 1.4806160726219732e-12, 3.2497122056903e-13, 6.340081216544516e-14, 1.1132360208942789e-14, 1.776998226031579e-15, 2.6001486504639328e-16, 3.685347590608287e-17, 4.473427636929113e-18, 5.236505771459363e-19, 5.746640548938564e-20], [1.2972853334540026e-11, 2.277864767426365e-11, 1.9998175285261337e-11, 1.1704733908673985e-11, 5.137998614322285e-12, 1.8043318176563964e-12, 5.280287703095357e-13, 1.324500038722269e-13, 2.9070628246327166e-14, 5.671583587462212e-15, 9.958565086831648e-16, 1.5896316828577027e-16, 2.3259891959192726e-17, 3.1416425469212925e-18, 4.134779597921916e-19, 4.684369044289126e-20, 5.1407152538289505e-21], [1.083133032090356e-12, 1.901841105121684e-12, 1.6696931410862627e-12, 9.772548568446735e-13, 4.289831908597821e-13, 1.5064776746931213e-13, 4.408632305227461e-14, 1.1058552085264223e-14, 2.427172874403912e-15, 4.735334139241357e-16, 8.314632501895601e-17, 1.3272196487231832e-17, 1.9420212850766645e-18, 2.623028820137032e-19, 3.2897845431836027e-20, 4.041102136982945e-21, 4.292100092712812e-22], [8.478116294212473e-14, 1.4886472468868558e-13, 1.306935732396476e-13, 7.649365387207524e-14, 3.357823344518016e-14, 1.1791804461944996e-14, 3.4508131757376248e-15, 8.655971874806118e-16, 1.8998454747189092e-16, 3.7065357933884587e-17, 6.508196057751582e-18, 1.0388680057262159e-18, 1.5200978839081714e-19, 2.053149772126749e-20, 2.5750461959585525e-21, 3.0142980643290358e-22, 3.471281569516849e-23]] |
| Legacy trial inputs | {"lambda_home": 1.252384118002628, "lambda_away": 1.755870284420456, "rho": -0.03320816174939849, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2645 |
| Legacy p draw | 0.2487 |
| Legacy p away | 0.4868 |
| Legacy p over 1 5 | 0.8056 |
| Legacy p under 3 5 | 0.6456 |
| Legacy p btts yes | 0.5961 |
| Legacy p over 2 5 | 0.5763 |
| Legacy goal margin distribution | {"-1": 0.219669419757553, "-10": 4.603835369741917e-06, "-11": 7.230059579920788e-07, "-12": 1.0433859685172876e-07, "-13": 1.3925958855977163e-08, "-14": 1.7280021760557326e-09, "-15": 1.9891239644445407e-10, "-16": 1.9191378890238256e-11, "-2": 0.14913796430687276, "-3": 0.07485079902398818, "-4": 0.02979479074913781, "-5": 0.009780650040766168, "-6": 0.002724832943864111, "-7": 0.0006583883441666419, "-8": 0.0001403201976519756, "-9": 2.6735366117454198e-05, "0": 0.24871044573077267, "1": 0.15325747322529795, "10": 1.5446932201604813e-07, "11": 1.730252374126146e-08, "12": 1.7809744624413317e-09, "13": 1.6954419719734314e-10, "14": 1.5005388012901357e-11, "15": 1.2319977567790415e-12, "16": 8.478116294212473e-14, "2": 0.07470500284476415, "3": 0.02674256370323904, "4": 0.0075926269193665906, "5": 0.0017777249303891577, "6": 0.00035324973677818087, "7": 6.087923992796747e-05, "8": 9.25448803251751e-06, "9": 1.2576606377277596e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2697 |
| Legacy raw p draw | 0.2416 |
| Legacy raw p away | 0.4887 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2524 |
| Legacy lambda away | 1.7559 |
| Legacy model home team | Milan |
| Legacy model away team | Inter |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 54.0% |
| Market home draw odds | 1.87 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:54:22Z |
| Market reference home draw last update utc | 2026-10-30T11:54:36Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.7% |
| Market draw away odds | 1.30 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:54:22Z |
| Market reference draw away last update utc | 2026-10-30T11:54:36Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.3% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:54:22Z |
| Market reference home away last update utc | 2026-10-30T11:54:36Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.75 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.29 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.75, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.07, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.23, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.23, "price": 1.65, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 81.5% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-30T11:54:36Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:54:14Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market reference under 3 5 last update utc | 2026-10-30T11:54:16Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.6% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:54:22Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-30T11:54:36Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021569260499678382, "mu": 8.170388356030594, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,536.0077 |
| Elo away rating | 1,691.0397 |
| Elo rating diff | -95.0319 |
| Elo home expectancy | 0.3665 |

</details>


---

## 2026-10-31 — Bologna vs Monza

The model's most likely 1X2 outcome is **Bologna win** at **58.7%**. Expected goals are 2.01 for Bologna and 0.98 for Monza (2.98 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.3%; Under 3.5 goals: 68.9%; Double Chance 1X: 81.5%; Double Chance X2: 41.3%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 58.7% | 1.70 |
| Draw | 22.8% | 4.38 |
| Monza win | 18.5% | 5.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 2.01 |
| Monza expected goals | 0.98 |
| Expected total goals | 2.98 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 53.3% |
| Under 2.5 | 46.7% |
| Over 3.5 | 31.1% |
| Under 3.5 | 68.9% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.87% |
| 2 | 1-0 | 10.82% |
| 3 | 2-0 | 10.50% |
| 4 | 2-1 | 9.71% |
| 5 | 3-0 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 58.7% | 57.7% | 1.70 | -0.2% |
| Draw | 22.8% | 23.4% | 4.07 | -7.1% |
| Monza win | 18.5% | 18.9% | 5.00 | -7.6% |
| Over 2.5 | 53.3% | 53.3% | 1.83 | -2.4% |
| Under 2.5 | 46.7% | 46.7% | 2.08 | -2.9% |

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
| Market best home last update utc | 2026-10-30T11:54:14Z |
| Market best draw last update utc | 2026-10-30T11:54:14Z |
| Market best away last update utc | 2026-10-30T11:54:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Bologna |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0052 |
| Dc lambda away | 0.9796 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:54:12.994081+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.83 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.42 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.22 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.48 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.12278369810392181, "-10": 9.272825706638125e-09, "-11": 7.698649181928015e-10, "-12": 5.87066928759275e-11, "-13": 4.138797529191156e-12, "-14": 2.712306177452433e-13, "-15": 1.6526397361385466e-14, "-16": 8.613539695720752e-16, "-2": 0.04620805591991625, "-3": 0.012557987439934862, "-4": 0.00268229832079147, "-5": 0.0004699760643214945, "-6": 6.965436490772053e-05, "-7": 8.933795027545946e-06, "-8": 1.0091521952958192e-06, "-9": 1.0179532714269968e-07, "0": 0.22837713094924772, "1": 0.23819988353458174, "10": 1.1218787407591026e-05, "11": 1.9065879228466085e-06, "12": 2.976037574337973e-07, "13": 4.2947062244308066e-08, "14": 5.761114144062079e-09, "15": 7.185457812419587e-10, "16": 7.665957354709752e-11, "2": 0.1813775904681929, "3": 0.10090076564263036, "4": 0.04411537562100988, "5": 0.01582220947794845, "6": 0.004800077098966363, "7": 0.0012602141353725757, "8": 0.0002913892450320345, "9": 6.016628238014602e-05} |
| Raw goal margin distribution | {"-1": 0.11441118513861495, "-10": 1.3534163727805843e-08, "-11": 1.1878210252599968e-09, "-12": 9.57726713687539e-11, "-13": 7.140484371659661e-12, "-14": 4.950333980734997e-13, "-15": 3.2061132888200906e-14, "-16": 1.9380751235753344e-15, "-17": 1.0011126582697488e-16, "-2": 0.04458908182809011, "-3": 0.012662460920318216, "-4": 0.002838674321994365, "-5": 0.0005233678109573247, "-6": 8.175145073689832e-05, "-7": 1.1062593728579244e-05, "-8": 1.3193761665315275e-06, "-9": 1.4059143962906611e-07, "0": 0.21574919324259892, "1": 0.2368576288960958, "10": 1.747898819923131e-05, "11": 3.140106354811182e-06, "12": 5.182549240001822e-07, "13": 7.909299023806557e-08, "14": 1.1224146035295079e-08, "15": 1.4880110589952569e-09, "16": 1.8412229866886926e-10, "17": 1.946826369537081e-11, "2": 0.18682952177422937, "3": 0.10860343881904322, "4": 0.04983672722732103, "5": 0.01880829552423794, "6": 0.006013764072116791, "7": 0.001665775105962949, "8": 0.000406664746337448, "9": 8.870237636682657e-05} |
| Unadjusted home-win probability | 60.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 17.5% |
| Raw p over 1 5 | 80.1% |
| Raw p under 3 5 | 65.1% |
| Raw p btts yes | 54.3% |
| P home draw | 81.5% |
| P draw away | 41.3% |
| P home away | 77.2% |
| Raw p home draw | 82.5% |
| Raw p draw away | 39.1% |
| Raw p home away | 78.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9445 |
| Totals anchor target over 2 5 | 0.5333 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.08 |
| Totals anchor reference last update utc | 2026-10-30T11:54:14Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5677 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.36, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:22Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.79, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:22Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.29, "price": 3.79, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.70 |
| Reference draw odds | 4.07 |
| Reference away odds | 5.00 |
| Market reference 1x2 last update utc | 2026-10-30T11:54:14Z |
| Market reference home last update utc | 2026-10-30T11:54:14Z |
| Market reference draw last update utc | 2026-10-30T11:54:14Z |
| Market reference away last update utc | 2026-10-30T11:54:14Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-30T11:54:14Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:54:14Z |
| Market best over 2 5 last update utc | 2026-10-30T11:54:14Z |
| Market best under 2 5 last update utc | 2026-10-30T11:54:14Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0318 |
| Raw ev home | 0.0355 |
| Raw edge prob draw | -0.0180 |
| Raw ev draw | -0.1219 |
| Raw edge prob away | -0.0138 |
| Raw ev away | -0.1244 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06237496490825386, 0.05267488565580221, 0.026513717685110728, 0.008333746983152587, 0.0019645869622295503, 0.00037050339444812656, 5.8228000735329e-05, 7.84376866818577e-06, 9.2454004731693e-07, 9.686662229765985e-08, 9.134085958016766e-09, 7.830028577576581e-10, 6.152803410234483e-11, 4.462935648309341e-12, 3.0059622831166973e-13, 1.8896579805148956e-14, 1.113663949450815e-15], [0.10521224272555056, 0.1093356315737142, 0.05055070482161268, 0.01588901220140574, 0.003745655618858189, 0.0007063968904922946, 0.00011101673905116751, 1.4954826001528234e-05, 1.7627158734485395e-06, 1.8468462586012477e-07, 1.7414927946458387e-08, 1.4928629325797718e-09, 1.173085391909559e-10, 8.508974308126942e-12, 5.731128085597192e-13, 3.6027970095063745e-14, 2.1232970135596597e-15], [0.10354038068211997, 0.09763391298708592, 0.04756214406669541, 0.015146890663155029, 0.0035707088270507956, 0.0006734035023355857, 0.00010583152601766368, 1.425633711273853e-05, 1.6803854303145829e-06, 1.7605863722739866e-07, 1.660153609098435e-08, 1.4231363994334535e-09, 1.1182945764385797e-10, 8.111549155295587e-12, 5.463446650346048e-13, 3.434522655832999e-14, 2.024125055863848e-15], [0.0658029085565083, 0.06204917739319018, 0.029254789033111708, 0.009500937041672422, 0.002269288801918762, 0.00042796741516590785, 6.725899772685158e-05, 9.06031483755485e-06, 1.0679335741497232e-06, 1.1189035939152756e-07, 1.0550756662238768e-08, 9.044443698045e-10, 7.107085686554223e-11, 5.155124250086048e-12, 3.472178467643641e-13, 2.1827385486526638e-14, 1.2863900545900424e-15], [0.031364739626005125, 0.02957553603081162, 0.013944198835060552, 0.004382917037674581, 0.0010675641547103895, 0.00020398925882685032, 3.205877973307491e-05, 4.31856922502907e-06, 5.090270206264646e-07, 5.333217126658906e-08, 5.028983411641729e-09, 4.3110042986570546e-10, 3.387568983627151e-11, 2.457172994181605e-12, 1.6550024301607107e-13, 1.0403951398492388e-14, 6.131535824902167e-16], [0.011959919868433217, 0.011277665468046457, 0.005317165156969786, 0.00167128237586633, 0.00039398599123163493, 7.677176055699995e-05, 1.2224569413272772e-05, 1.6467454375041453e-06, 1.9410084222450236e-07, 2.0336483017672137e-08, 1.9176387032094645e-09, 1.6438607997134688e-10, 1.2917388786284913e-11, 9.369627315166446e-13, 6.310811657550952e-14, 3.967207332971925e-15, 2.338061084220062e-16], [0.0038004376083078345, 0.0035836413997891708, 0.0016896061724851043, 0.0005310741597950646, 0.0001251947500229614, 2.361060148640651e-05, 3.833950707770755e-06, 5.232771925603172e-07, 6.167835141949498e-08, 6.462211764902038e-09, 6.093574477918844e-10, 5.223605571591914e-11, 4.104687212336836e-12, 2.97733466579252e-13, 2.0053517269464856e-14, 1.2606375388831323e-15, 7.429527432239359e-17], [0.0010351234676337848, 0.0009760747826504739, 0.00046019726685552864, 0.0001446484280273542, 3.409923727994425e-05, 6.43080881793781e-06, 1.0106604856816483e-06, 1.4066886085506832e-07, 1.6799304601058823e-08, 1.760109687380879e-09, 1.6597041167258043e-10, 1.4227510802959638e-11, 1.1179917942865494e-12, 8.109352925106076e-14, 5.4619674031341345e-15, 3.43359274686014e-16, 2.02357701695415e-17], [0.00024669409571174706, 0.00023262141510850976, 0.00010967575573903144, 3.4473098392701545e-05, 8.12664456778816e-06, 1.532611920839537e-06, 2.408639958253149e-07, 3.2446270520882545e-08, 3.9515321718830194e-09, 4.194752425761156e-10, 3.9554625030450104e-11, 3.3907480812781494e-12, 2.66443553188043e-13, 1.932648180839254e-14, 1.301714386210711e-15, 8.183053367202297e-17, 4.822656600006597e-18], [5.226041252249278e-05, 4.927921391901343e-05, 2.3234038991088056e-05, 7.3028839126986794e-06, 1.7215726072039143e-06, 3.2467307735468557e-07, 5.102534678557991e-08, 6.873514655247484e-09, 8.101768210441077e-10, 8.77057423618188e-11, 8.379369661441838e-12, 7.183061798710451e-13, 5.644419645874332e-14, 4.094179510056885e-15, 2.757590554146201e-16, 1.733522415401699e-17, 1.0216459483698373e-18], [9.963901398723095e-06, 9.395510000697017e-06, 4.429771263318124e-06, 1.3923582252844398e-06, 3.282327651267502e-07, 6.190174117339279e-08, 9.728425392515825e-09, 1.3104952483505064e-09, 1.544672452966194e-10, 1.6183961258282223e-11, 1.5767961631078932e-12, 1.3695130988964416e-13, 1.076157613189555e-14, 7.805908713277295e-16, 5.25758581942635e-17, 3.3051109981393108e-18, 1.9478567050309325e-19], [1.7270039211758913e-06, 1.6284868710895183e-06, 7.67794866240154e-07, 2.4133198618925417e-07, 5.689129686740453e-08, 1.0729185833549558e-08, 1.68618978926217e-09, 2.2714299770908393e-10, 2.6773201344072598e-11, 2.8051024829284204e-12, 2.645085230842557e-13, 2.342813456159766e-14, 1.8652617518072045e-15, 1.3529675191184202e-16, 9.112767140822651e-18, 5.7286191676280985e-19, 3.376143573548683e-20], [2.7439024357743474e-07, 2.5873763443261916e-07, 1.2198896469308187e-07, 3.834336544436329e-08, 9.039016422298787e-09, 1.7046770294827765e-09, 2.6790560306221095e-10, 3.608898723626957e-11, 4.253786078925514e-12, 4.4568095307295186e-13, 4.20257054355608e-14, 3.602576941641833e-15, 2.924978938626037e-16, 2.149625038896776e-17, 1.4478568142058697e-18, 9.101758192289266e-20, 5.364092380680036e-21], [4.024221717906786e-08, 3.7946597304205315e-08, 1.7890965606593298e-08, 5.6234581064941625e-09, 1.3256668940149689e-09, 2.500088281063637e-10, 3.9291176396642314e-11, 5.292829814937349e-12, 6.238624995903231e-13, 6.536380256200417e-14, 6.1635120228467595e-15, 5.283558256288352e-16, 4.151797778945665e-17, 3.111598577497726e-18, 2.1234344050218808e-19, 1.3348686349414586e-20, 7.867006047209952e-22], [5.480377220324337e-09, 5.167748748271249e-09, 2.4364770937864915e-09, 7.658293669343171e-10, 1.8053564532415354e-10, 3.404739555818468e-11, 5.350859947048562e-12, 7.208028280291691e-13, 8.496057302597669e-14, 8.901554628578314e-15, 8.39376487058335e-16, 7.195401829171771e-17, 5.654116389730701e-18, 4.1012130427319455e-19, 2.854138333388715e-20, 1.817887823254391e-21, 1.0713664344446017e-22], [6.965876669728096e-10, 6.568507785759475e-10, 3.0969034177048493e-10, 9.734134541572091e-11, 2.294712552183409e-11, 4.327621053240687e-12, 6.801252718498492e-13, 9.161821169210083e-14, 1.0798980612019916e-14, 1.1314391184892589e-15, 1.066896100989915e-16, 9.14577221897514e-18, 7.186709210652005e-19, 5.2128791693394267e-20, 3.51107867204293e-21, 2.280552245561037e-22, 1.361768752477545e-23], [8.300655427155756e-11, 7.827144002867832e-11, 3.6903220341614776e-11, 1.1599357918910528e-11, 2.7344179495482144e-12, 5.15686580245728e-13, 8.104486766841651e-14, 1.0917379709193539e-14, 1.2868246349301476e-15, 1.3482418229134084e-16, 1.2713312811550155e-17, 1.0898255511022363e-18, 8.563803185323599e-20, 6.2117542155355865e-21, 4.1838602111515093e-22, 2.6301277570135958e-23, 1.6015761258775185e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9065868250532205, "lambda_away": 0.9429549354935488, "rho": -0.03320816174939849, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T11:54:14Z", "over": 1.83, "under": 2.08, "bookmaker": "pinnacle", "event_id": "04aa939b89001eedf55668e66c74836e", "kickoff_utc": "2026-10-31T14:00:00Z", "home_team": "Bologna", "away_team": "Monza"}} |
| Legacy p home | 0.5866 |
| Legacy p draw | 0.2299 |
| Legacy p away | 0.1835 |
| Legacy p over 1 5 | 0.7797 |
| Legacy p under 3 5 | 0.6820 |
| Legacy p btts yes | 0.5247 |
| Legacy p over 2 5 | 0.5403 |
| Legacy goal margin distribution | {"-1": 0.12085852427521943, "-10": 1.0744103014236104e-08, "-11": 9.087808017081809e-10, "-12": 7.06057936145754e-11, "-13": 5.07168007348198e-12, "-14": 3.386483234625973e-13, "-15": 2.1019876818708614e-14, "-16": 1.113663949450815e-15, "-2": 0.046435175132648686, "-3": 0.012824584403770625, "-4": 0.002786405680936257, "-5": 0.0004968997073698051, "-6": 7.498030008315493e-05, "-7": 9.793538256620882e-06, "-8": 1.1267654866921105e-06, "-9": 1.1577827906240131e-07, "0": 0.22992199216601034, "1": 0.23690250230952592, "10": 1.1720185636923434e-05, "11": 2.00442181339414e-06, "12": 3.148733937387918e-07, "13": 4.57312556270285e-08, "14": 6.1741312192418994e-09, "15": 7.74859107001488e-10, "16": 8.300655427155756e-11, "2": 0.1813369127399033, "3": 0.10126236811635271, "4": 0.04448512097209757, "5": 0.016040016830730645, "6": 0.004893830265845537, "7": 0.0012924299159554772, "8": 0.00030065370734928327, "9": 6.246342116020654e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5959 |
| Legacy raw p draw | 0.2261 |
| Legacy raw p away | 0.1781 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9066 |
| Legacy lambda away | 0.9430 |
| Legacy model home team | Bologna |
| Legacy model away team | Monza |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 79.8% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:54:22Z |
| Market reference home draw last update utc | 2026-10-30T11:54:36Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.8% |
| Market draw away odds | 2.24 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:54:22Z |
| Market reference draw away last update utc | 2026-10-30T11:54:36Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.3% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:54:22Z |
| Market reference home away last update utc | 2026-10-30T11:54:36Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.18 |
| Market reference dc draw away odds | 2.10 |
| Market reference dc home away odds | 1.25 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.09, "price": 1.74, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.74, "price": 2.09, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.67, "price": 2.19, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.19, "price": 1.67, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 77.7% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T11:54:14Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market reference over 1 5 last update utc | 2026-10-30T11:54:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.8% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:54:14Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 3.15 |
| Market reference under 3 5 last update utc | 2026-10-30T11:54:16Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.7% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:54:22Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.05 |
| Market reference btts yes last update utc | 2026-10-30T11:54:36Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021569260499678382, "mu": 8.81404549207439, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,462.4109 |
| Elo away rating | 1,358.1569 |
| Elo rating diff | 164.2540 |
| Elo home expectancy | 0.7202 |

</details>


---

## 2026-10-31 — Udinese vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **61.4%**. Expected goals are 0.86 for Udinese and 1.73 for AS Roma (2.60 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 60.6%; Under 3.5 goals: 61.5%; Double Chance 1X: 38.6%; Double Chance X2: 83.0%; Double Chance 12 (either team wins): 78.3%; Under 4.5 goals: 79.2%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 17.0% | 5.90 |
| Draw | 21.7% | 4.61 |
| AS Roma win | 61.4% | 1.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 0.86 |
| AS Roma expected goals | 1.73 |
| Expected total goals | 2.60 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 82.4% |
| Under 1.5 | 17.6% |
| Over 2.5 | 60.6% |
| Under 2.5 | 39.4% |
| Over 3.5 | 38.5% |
| Under 3.5 | 61.5% |
| Over 4.5 | 20.8% |
| Under 4.5 | 79.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.07% |
| 2 | 1-2 | 9.94% |
| 3 | 0-2 | 9.50% |
| 4 | 0-1 | 8.82% |
| 5 | 1-3 | 6.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 17.0% | 16.4% | 5.68 | -3.7% |
| Draw | 21.7% | 20.7% | 4.55 | -1.3% |
| AS Roma win | 61.4% | 62.9% | 1.56 | -4.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:00:00+00:00 |
| Fixture id | 34cd26b96f78bd7aa3dbff3d1daca7a7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T11:54:14Z |
| Market best draw last update utc | 2026-10-30T11:54:14Z |
| Market best away last update utc | 2026-10-30T11:54:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Udinese |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8644 |
| Dc lambda away | 1.7317 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:54:12.994081+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.14 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.68 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.60 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.80 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.2314475734730451, "-10": 2.3801975197417995e-05, "-11": 4.462822203762177e-06, "-12": 7.689264245287854e-07, "-13": 1.225295487083062e-07, "-14": 1.815870710311433e-08, "-15": 2.5141316530159667e-09, "-16": 3.245350641726513e-10, "-17": 3.5445254113675565e-11, "-2": 0.18661645737037014, "-3": 0.11185579406465451, "-4": 0.05316865432114351, "-5": 0.020840519950518745, "-6": 0.006932480691592615, "-7": 0.0019999870373208196, "-8": 0.0005089244828125823, "-9": 0.00011577146055451996, "0": 0.21698343440717227, "1": 0.10837308514499883, "10": 2.1663546331138156e-08, "11": 2.027466492176217e-09, "12": 1.7436384301511787e-10, "13": 1.3868836449460904e-11, "14": 1.0259156682083987e-12, "15": 7.089935775395578e-14, "16": 4.568182631280581e-15, "17": 2.4903906204798415e-16, "2": 0.04408046068664374, "3": 0.013188099509694063, "4": 0.0031290099565329404, "5": 0.0006121916090641025, "6": 0.0001016471105137366, "7": 1.4637304112567662e-05, "8": 1.8591516031436363e-06, "9": 2.1110111152984297e-07} |
| Raw goal margin distribution | {"-1": 0.2502575969481562, "-10": 5.706104448554315e-06, "-11": 8.883362426979327e-07, "-12": 1.2698832970010558e-07, "-13": 1.6779085817455723e-08, "-14": 2.060642338458355e-09, "-15": 2.355502680513464e-10, "-16": 2.331333050985418e-11, "-2": 0.17913520697381793, "-3": 0.09262125213417927, "-4": 0.03742657135652726, "-5": 0.012366265453598044, "-6": 0.0034493852165086852, "-7": 0.0008315639664005545, "-8": 0.00017639801479183966, "-9": 3.339360930111321e-05, "0": 0.2412962694322181, "1": 0.12348309371666298, "10": 5.477913618630939e-09, "11": 4.2567720053516813e-10, "12": 3.037346688437546e-11, "13": 2.0032096174036423e-12, "14": 1.2279714402990162e-13, "15": 7.006430148480359e-15, "16": 3.461346372228304e-16, "2": 0.04463094087057628, "3": 0.011518429980863653, "4": 0.0023232194143837236, "5": 0.0003831565869897347, "6": 5.334662825108096e-05, "7": 6.419312022166428e-06, "8": 6.796949813574654e-07, "9": 6.422605960144769e-08} |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 57.6% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 47.9% |
| P home draw | 38.6% |
| P draw away | 83.0% |
| P home away | 78.3% |
| Raw p home draw | 42.4% |
| Raw p draw away | 81.8% |
| Raw p home away | 75.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2105 |
| Totals anchor target over 2 5 | 0.6057 |
| Totals anchor reference over odds | 1.61 |
| Totals anchor reference under odds | 2.42 |
| Totals anchor reference last update utc | 2026-10-30T11:54:14Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4909 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 7.8, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.38, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.36, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.65, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.52, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.61, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.01, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:24Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.48, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:24Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.23, "price": 4.48, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.68 |
| Reference draw odds | 4.55 |
| Reference away odds | 1.56 |
| Market reference 1x2 last update utc | 2026-10-30T11:54:14Z |
| Market reference home last update utc | 2026-10-30T11:54:14Z |
| Market reference draw last update utc | 2026-10-30T11:54:14Z |
| Market reference away last update utc | 2026-10-30T11:54:14Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.46 |
| Market reference over 2 5 last update utc | 2026-10-30T11:54:14Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:54:14Z |
| Home probability edge | +0.6% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0184 |
| Raw ev home | 0.0360 |
| Raw edge prob draw | 0.0347 |
| Raw ev draw | 0.0979 |
| Raw edge prob away | -0.0532 |
| Raw ev away | -0.1010 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07349313766548465, 0.13299777204992416, 0.1140277015459041, 0.06322119843989617, 0.026289137713836723, 0.00874540538669622, 0.0024243889944895497, 0.0005760734665029288, 0.0001197737077744622, 2.213566599587223e-05, 3.681850936794318e-06, 5.56733205764401e-07, 7.716839856133863e-08, 9.873468476236996e-09, 1.173046739702507e-09, 1.300761476458423e-10], [0.059678747401985775, 0.10863156440871197, 0.10296670535955751, 0.05708857079451265, 0.023739020084060355, 0.007897077354833191, 0.0021892166893503974, 0.0005201927784801223, 0.00010815533340615502, 1.9988446383065967e-05, 3.324701414191831e-06, 5.027285754659159e-07, 6.968285469242338e-08, 8.915715266437306e-09, 1.059258025746606e-09, 1.1745840867943764e-10], [0.028520201718480184, 0.0474379815065562, 0.03947919325048199, 0.025775412328338614, 0.01071813538895217, 0.0035655197209662213, 0.0009884283676884543, 0.0002348663343458242, 4.883198642486491e-05, 9.024756446975829e-06, 1.5010981817684952e-06, 2.2698127035819585e-07, 3.1461714436290626e-08, 4.025433357259206e-09, 4.782535627664554e-10, 5.3032312300135894e-11], [0.008584554943898719, 0.014278789564339174, 0.011875037946351965, 0.006588488844479227, 0.0032261490662243574, 0.0010732182138934764, 0.00029751604544337807, 7.069455439220704e-05, 1.4698383785004589e-05, 2.716443534975694e-06, 4.518291961879156e-07, 6.832115725756857e-08, 9.469947613749942e-09, 1.2116518027992344e-09, 1.439538902007014e-10, 1.5962678077677104e-11], [0.0019379574602657224, 0.0032234270664715688, 0.002680781767892061, 0.001486325110690153, 0.0006184803233024451, 0.00024227828439564295, 6.716404561258437e-05, 1.595924773967583e-05, 3.3181501774000925e-06, 6.132352869077108e-07, 1.0200013480495776e-07, 1.5423454945139057e-08, 2.1378342553955932e-09, 2.735295732655389e-10, 3.249749314575688e-11, 3.6035637570752346e-12], [0.0003499940665386581, 0.0005821491804213657, 0.00048414773372713063, 0.0002684295090861489, 0.00011162047707039552, 3.71574526994924e-05, 1.2129790220427834e-05, 2.882231488477129e-06, 5.992561228949743e-07, 1.1074996031151357e-07, 1.8421169039997175e-08, 2.785467600297497e-09, 3.8609170736335696e-10, 4.939929262052185e-11, 5.869029641567098e-12, 6.5080166062941e-13], [5.267394887135045e-05, 8.761318861280361e-05, 7.286401516668652e-05, 4.0398519829203386e-05, 1.6798831364052136e-05, 5.5883381151774574e-06, 1.5502562390689237e-06, 4.3377453669681487e-07, 9.018777572541247e-08, 1.6667818985178177e-08, 2.7723776170249453e-09, 4.192116152479621e-10, 5.810662750496536e-11, 7.434571218614764e-12, 8.832863091700428e-13, 9.79453558639033e-14], [6.7949190040548825e-06, 1.1302067398914593e-05, 9.399429736644462e-06, 5.211393411828407e-06, 2.167042739861789e-06, 7.208934525232989e-07, 1.998450700931206e-07, 4.7519018617554804e-08, 1.1634188139316797e-08, 2.1501421937274676e-09, 3.5763563886863414e-10, 5.4078136008485883e-11, 7.49573244374273e-12, 9.590568078301316e-13, 1.1394359179069357e-13, 1.2634912972711248e-14], [7.669741799001794e-07, 1.2757170275740139e-06, 1.060957446216826e-06, 5.882342653075142e-07, 2.4460421488796136e-07, 8.137060415503375e-08, 2.2557444562664727e-08, 5.3600083626010385e-09, 1.115186603914e-09, 2.4269657147035766e-10, 4.0368001540660003e-11, 6.10405127579705e-12, 8.460782594111863e-13, 1.0825321217578089e-13, 1.2861344309828678e-14, 1.426161520037609e-15], [7.695284501486587e-08, 1.279965574832065e-07, 1.0644907751225354e-07, 5.901932742577328e-08, 2.4541882545128214e-08, 8.1641594390091e-09, 2.2632568094901023e-09, 5.377858911225732e-10, 1.1181318688319828e-10, 2.067866892366247e-11, 4.050243994553472e-12, 6.124379726190243e-13, 8.488959716400133e-14, 1.0861373012594044e-14, 1.2904176715386736e-15, 1.4309110957542677e-16], [6.948821042433794e-09, 1.1558054440047945e-08, 9.612322840330566e-09, 5.329429266030083e-09, 2.2161253403637115e-09, 7.37221383986667e-10, 2.0437147631355585e-10, 4.8561920171172764e-11, 1.0096700462282509e-11, 1.865995411232546e-12, 3.1058654312423026e-13, 5.5302982891645406e-14, 7.66550760979644e-15, 9.807790384495323e-16, 1.1652436589945595e-16, 1.2921088401745797e-17], [5.704333238744826e-10, 9.488083477034787e-10, 7.890819513814835e-10, 4.374963798910424e-10, 1.8192319766280492e-10, 6.051899191687488e-11, 1.6776989913363064e-11, 3.986480205463327e-12, 8.288448313309273e-13, 1.5318079977364086e-13, 2.5478739661623585e-14, 3.855292377867141e-15, 6.29266599087695e-16, 8.051280116047342e-17, 9.565562409290724e-18, 1.0607007088071959e-18], [4.292497874811872e-11, 7.139761380800939e-11, 5.937823857048581e-11, 3.29215037467448e-11, 1.3689679523673818e-11, 4.554040469173279e-12, 1.2624647006894934e-12, 2.999817348275434e-13, 6.237038630337218e-14, 1.1526820576054175e-14, 1.9172694033294105e-15, 2.8991058018197345e-16, 4.0211926733510206e-17, 6.058570097712743e-18, 7.198064102281579e-19, 7.981748870211833e-20], [2.9816261105529015e-12, 4.959373208087218e-12, 4.12449141930348e-12, 2.2867714331544438e-12, 9.509033458677294e-13, 3.163297074898783e-13, 8.769247708461874e-14, 2.0837130252276732e-14, 4.332329980141362e-15, 8.006682869406859e-16, 1.3317608256664996e-16, 2.0137574456784025e-17, 2.7912550493662467e-18, 3.5737834473768197e-19, 4.9998710538061494e-20, 5.544228915976518e-21], [1.9231430674643688e-13, 3.1987861155176314e-13, 2.6602889784792247e-13, 1.474963146110569e-13, 6.133308166848208e-14, 2.0403204876663138e-14, 5.6561477905353335e-15, 1.3439908662151848e-15, 2.7943444477456335e-16, 5.1642949460320414e-17, 8.589831536343167e-18, 1.2988696528730853e-18, 1.8003541016476385e-19, 2.3034998522811873e-20, 2.7386227820150775e-21, 3.576016914548198e-22], [1.1577286507709573e-14, 1.9256634601324127e-14, 1.6014891569020848e-14, 8.87925148145596e-15, 3.692240431248742e-15, 1.2282692459488731e-15, 3.4049907471165954e-16, 8.090800723647277e-17, 1.6821903071118268e-17, 3.1088962236886323e-18, 5.171063059823365e-19, 7.819171834837812e-20, 1.0838099152751134e-20, 1.386702747782964e-21, 1.6475133749991713e-22, 1.8281412727016856e-23]] |
| Legacy trial inputs | {"lambda_home": 0.9029972889360245, "lambda_away": 1.663311570332194, "rho": -0.03320816174939849, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1818 |
| Legacy p draw | 0.2288 |
| Legacy p away | 0.5893 |
| Legacy p over 1 5 | 0.7338 |
| Legacy p under 3 5 | 0.7396 |
| Legacy p btts yes | 0.4789 |
| Legacy p over 2 5 | 0.4827 |
| Legacy goal margin distribution | {"-1": 0.2652208925341883, "-10": 4.21728602679413e-06, "-11": 6.305890512680415e-07, "-12": 8.657833006862007e-08, "-13": 1.0985758814283737e-08, "-14": 1.2905051483819446e-09, "-15": 1.300761476458423e-10, "-2": 0.18297776459926954, "-3": 0.09083982982587326, "-4": 0.0352487697182011, "-5": 0.011184818877450297, "-6": 0.0029962350476106067, "-7": 0.000693721202648841, "-8": 0.00014133376162602345, "-9": 2.5697098124584275e-05, "0": 0.22884962085659724, "1": 0.12059550609955307, "10": 7.959356961491827e-09, "11": 6.461066176568377e-10, "12": 4.815926010553531e-11, "13": 3.3175196136736856e-12, "14": 2.1157094134776101e-13, "15": 1.1577286507709573e-14, "2": 0.045765745390096424, "3": 0.012334778989929877, "4": 0.002598435026061066, "5": 0.000447620215338699, "6": 6.50982709718243e-05, "7": 8.182601104698603e-06, "8": 9.050345683498944e-07, "9": 8.933387455709189e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1997 |
| Legacy raw p draw | 0.2511 |
| Legacy raw p away | 0.5492 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9030 |
| Legacy lambda away | 1.6633 |
| Legacy model home team | Udinese |
| Legacy model away team | Roma |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 40.9% |
| Market home draw odds | 2.54 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:54:24Z |
| Market reference home draw last update utc | 2026-10-30T11:54:36Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.9% |
| Market draw away odds | 1.17 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:54:24Z |
| Market reference draw away last update utc | 2026-10-30T11:54:36Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.2% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:54:24Z |
| Market reference home away last update utc | 2026-10-30T11:54:36Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.30 |
| Market reference dc draw away odds | 1.15 |
| Market reference dc home away odds | 1.22 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:24Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.22, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:24Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.22, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:24Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.77, "price": 2.05, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:24Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.05, "price": 1.77, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 82.9% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market reference over 1 5 last update utc | 2026-10-30T11:54:36Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:54:14Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.63 |
| Market reference under 3 5 last update utc | 2026-10-30T11:54:16Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.8% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:54:24Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-30T11:54:36Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021569260499678382, "mu": 8.940821201689916, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,376.7934 |
| Elo away rating | 1,594.6836 |
| Elo rating diff | -157.8902 |
| Elo home expectancy | 0.2872 |

</details>


---

## 2026-11-01 — Como vs Venezia

The model's most likely 1X2 outcome is **Como win** at **75.2%**. Expected goals are 2.14 for Como and 0.58 for Venezia (2.72 combined). The most likely exact score is 2-0 at 9.6%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 70.6%; Under 3.5 goals: 49.7%; Double Chance 1X: 90.7%; Double Chance X2: 24.8%; Double Chance 12 (either team wins): 84.5%; Under 4.5 goals: 69.0%; BTTS Yes (both teams score): 53.6%; BTTS No (at least one team does not score): 46.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 75.2% | 1.33 |
| Draw | 15.5% | 6.45 |
| Venezia win | 9.3% | 10.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.14 |
| Venezia expected goals | 0.58 |
| Expected total goals | 2.72 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 88.2% |
| Under 1.5 | 11.8% |
| Over 2.5 | 70.6% |
| Under 2.5 | 29.4% |
| Over 3.5 | 50.3% |
| Under 3.5 | 49.7% |
| Over 4.5 | 31.0% |
| Under 4.5 | 69.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.56% |
| 2 | 3-0 | 9.40% |
| 3 | 2-1 | 7.64% |
| 4 | 3-1 | 7.51% |
| 5 | 1-1 | 7.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 75.2% | 76.0% | 1.30 | -2.2% |
| Draw | 15.5% | 14.4% | 6.36 | -1.4% |
| Venezia win | 9.3% | 9.6% | 9.32 | -13.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T11:30:00+00:00 |
| Fixture id | 9507f4bcbcfd4e4953720628a2b86a17 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T11:54:14Z |
| Market best draw last update utc | 2026-10-30T11:54:14Z |
| Market best away last update utc | 2026-10-30T11:54:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Como |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1417 |
| Dc lambda away | 0.5799 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:54:12.994081+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 53.6% |
| P btts no | 46.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.18 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.50 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.40 |
| Fair Over 3.5 odds | 1.99 |
| Fair Under 3.5 odds | 2.01 |
| Fair Over 4.5 odds | 3.23 |
| Fair Under 4.5 odds | 1.45 |
| Goal margin distribution | {"-1": 0.06678181112479663, "-10": 1.130246041366598e-09, "-11": 8.066431364351043e-11, "-12": 5.291085119531622e-12, "-13": 3.2103296704388944e-13, "-14": 1.8117414060701974e-14, "-15": 9.555909565711078e-16, "-16": 4.7305160526996125e-17, "-17": 2.2060826213916204e-18, "-18": 9.722001797640711e-20, "-19": 4.038865358912731e-21, "-2": 0.020566456525722115, "-20": 1.4431869701668408e-22, "-3": 0.004653047629442226, "-4": 0.0008374494798242614, "-5": 0.00012452006764349902, "-6": 1.573100579290513e-05, "-7": 1.7249328769538953e-06, "-8": 1.6692175257055628e-07, "-9": 1.4445991449101974e-08, "0": 0.15498322748443438, "1": 0.17653184103994388, "10": 0.00037412227711423554, "11": 9.860908773158018e-05, "12": 2.3887745869713096e-05, "13": 5.352725573333511e-06, "14": 1.115620482885476e-06, "15": 2.1731375906066806e-07, "16": 3.9730006625781735e-08, "17": 6.842689194266932e-09, "18": 1.113667796322913e-09, "19": 1.7086545356839225e-10, "2": 0.19671643999163438, "20": 2.2548227661286022e-11, "3": 0.16436661309473194, "4": 0.10925206365606274, "5": 0.059993652555571604, "6": 0.027990932723542677, "7": 0.011335169090655814, "8": 0.004051013241909296, "9": 0.0012947711208209822} |
| Raw goal margin distribution | {"-1": 0.06517672232927028, "-10": 8.722288717928898e-11, "-11": 4.555719153632328e-12, "-12": 2.18428572206819e-13, "-13": 9.677969389023134e-15, "-14": 3.9853121359986648e-16, "-15": 1.5327381793379022e-17, "-16": 5.517180672091578e-19, "-17": 1.75388219776245e-20, "-2": 0.01641022026843061, "-3": 0.0028898651310151377, "-4": 0.00039535831862482754, "-5": 4.4080275565393175e-05, "-6": 4.140547891965257e-06, "-7": 3.356955104918942e-07, "-8": 2.3926642543073713e-08, "-9": 1.5209224199780555e-09, "0": 0.18079111476752452, "1": 0.24634162320155195, "10": 4.1169888964900415e-05, "11": 7.941473746432434e-06, "12": 1.4062046571385067e-06, "13": 2.301008658279389e-07, "14": 3.499381360128533e-08, "15": 4.9704056204551304e-09, "16": 6.607481959949551e-10, "17": 7.757363165237872e-11, "2": 0.22382276575274765, "3": 0.14556680372213351, "4": 0.07354795066672071, "5": 0.03028439622018785, "6": 0.01050575708512866, "7": 0.003145647103277561, "8": 0.0008280206187414476, "9": 0.00019438438532994102} |
| Unadjusted home-win probability | 73.4% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 8.5% |
| Raw p over 1 5 | 75.7% |
| Raw p under 3 5 | 70.9% |
| Raw p btts yes | 39.0% |
| P home draw | 90.7% |
| P draw away | 24.8% |
| P home away | 84.5% |
| Raw p home draw | 91.5% |
| Raw p draw away | 26.6% |
| Raw p home away | 81.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.3776 |
| Totals anchor target over 2 5 | 0.7059 |
| Totals anchor reference over odds | 1.38 |
| Totals anchor reference under odds | 3.10 |
| Totals anchor reference last update utc | 2026-10-30T11:54:14Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5218 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.86, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.88, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:22Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 7.63, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:22Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.11, "price": 7.63, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.30 |
| Reference draw odds | 6.36 |
| Reference away odds | 9.32 |
| Market reference 1x2 last update utc | 2026-10-30T11:54:14Z |
| Market reference home last update utc | 2026-10-30T11:54:14Z |
| Market reference draw last update utc | 2026-10-30T11:54:14Z |
| Market reference away last update utc | 2026-10-30T11:54:14Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-30T11:53:51Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:53:51Z |
| Home probability edge | -0.8% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | -0.0254 |
| Raw ev home | -0.0454 |
| Raw edge prob draw | 0.0369 |
| Raw ev draw | 0.1498 |
| Raw edge prob away | -0.0115 |
| Raw ev away | -0.2085 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.0601474452187582, 0.03794842459352688, 0.012390625939918973, 0.0025066498310984757, 0.00038032542138386296, 4.616438223042112e-05, 4.669576076372429e-06, 4.048564780191855e-07, 3.071374563218448e-08, 2.0711518980727217e-09, 1.2569952270346426e-10, 6.935257982672066e-12, 3.507543391105507e-13, 1.63750025931844e-14, 7.098637830290763e-16, 2.8721388902559306e-17, 1.0894495714533817e-18, 3.889375627969733e-20], [0.13873321310291298, 0.07691269060898191, 0.026350634062192298, 0.005330788996585915, 0.0008088224155930572, 9.817589109375976e-05, 9.930595194358856e-06, 8.609916037915127e-07, 6.531765834569636e-08, 4.404633471945986e-09, 2.673199998621603e-10, 1.4748927625966626e-11, 7.459348123690244e-13, 3.482404385320938e-14, 1.5096380821520453e-15, 6.108059531447694e-17, 2.3168875507808295e-18, 8.271375021729533e-20], [0.15055339620734082, 0.09137181132034898, 0.024019816535722372, 0.005668384744762752, 0.000860044665940841, 0.00010439331283526037, 1.0559493977752459e-05, 9.15517698304375e-07, 6.945418743219684e-08, 4.683576332629212e-09, 2.8424921904789357e-10, 1.5682968583108825e-11, 7.931744275993682e-13, 3.7029430175327286e-14, 1.6052425786246624e-15, 6.494879367826207e-17, 2.4636146837902943e-18, 8.795196362379172e-20], [0.10672523646818098, 0.06477222311385346, 0.019655336572440577, 0.0034446625029146446, 0.0006096738609557746, 7.400298683861048e-05, 7.485480368758459e-06, 6.489979323201411e-07, 4.923512032367652e-08, 3.320122987649056e-09, 2.0150037051972546e-10, 1.1117441205047563e-11, 5.622704666819673e-13, 2.624965488192093e-14, 1.1379344346146094e-15, 4.604130852079467e-17, 1.7464226401900446e-18, 6.234794001367294e-20], [0.05674204162506513, 0.03443710505312428, 0.0104500487687427, 0.002114066965474952, 0.0002778729015062808, 3.93447763484459e-05, 3.979765730426212e-06, 3.4504929582676336e-07, 2.6176575843465632e-08, 1.7651922169475356e-09, 1.0713063554471581e-10, 5.9107511259447754e-12, 2.9893936317981304e-13, 1.3956015083626622e-14, 6.0499957828388245e-16, 2.4478538825615812e-17, 9.285112820917853e-19, 3.314819928787543e-20], [0.02413419276885301, 0.014647194706970318, 0.004444737697230539, 0.0008991798357938985, 0.00013642948676174788, 1.434583027183634e-05, 1.6927207862494856e-06, 1.4676042633900443e-07, 1.113372923042008e-08, 7.507923229021093e-10, 4.5566062405195314e-11, 2.514030214578174e-12, 1.271484072577462e-13, 5.9359365413541995e-15, 2.5732553903961213e-16, 1.0411500146943942e-17, 3.949253433305992e-19, 1.4098982141674455e-20], [0.008554199025431577, 0.005191597659291704, 0.0015754067783455203, 0.00031870812289867383, 4.8356495445069684e-05, 5.869572775143798e-06, 5.143309851792568e-07, 5.2018226090463895e-08, 3.946273929459661e-09, 2.6611318714414836e-10, 1.615057815906393e-11, 8.910807590467513e-13, 4.5066880498820224e-14, 2.1039519764923547e-15, 9.120727162302845e-17, 3.69028478653779e-18, 1.399785780859741e-19, 4.997287477190423e-21], [0.0025988375556454104, 0.0015772510004333669, 0.00047862181939075483, 9.682620624279184e-05, 1.4691109716809865e-05, 1.7832255385089031e-06, 1.8037514878538328e-07, 1.3547716799936223e-08, 1.1989111852850226e-09, 8.084742273901165e-11, 4.906681378394076e-12, 2.707178234734702e-13, 1.3691697049357437e-14, 6.391982926194376e-16, 2.7709535648770985e-17, 1.1211395322658458e-18, 4.2526668438991545e-20, 1.5182179340775571e-21], [0.0006908551043743958, 0.0004192843458653203, 0.00012723316479430568, 2.573953830809104e-05, 3.905372274898426e-06, 4.7403904213001357e-07, 4.794955035568816e-08, 4.1572694741678306e-09, 2.7321569041947967e-10, 2.1491860679568222e-11, 1.3043546598127019e-12, 7.196555621012108e-14, 3.6396960531637924e-15, 1.6991958662605567e-16, 7.366091082227555e-18, 2.9803516071993477e-19, 1.1304964367354804e-20, 4.035914468881638e-22], [0.00016324590087197306, 9.90749729268945e-05, 3.006461481738228e-05, 6.082135157614551e-06, 9.228216035742276e-07, 1.1201325718086315e-07, 1.1330259405564654e-08, 9.823437594669573e-10, 7.452383249305983e-11, 4.353515738863454e-12, 3.0821303939050987e-13, 1.7005131728616687e-14, 8.600435277046044e-16, 4.015122102873148e-17, 1.7405736268130413e-18, 7.04243451270535e-20, 2.6713113658551796e-21, 9.536681268519142e-23], [3.4716833652218225e-05, 2.1069866598969188e-05, 6.393717856668535e-06, 1.293462643713244e-06, 1.962526711594759e-07, 2.3821398244118518e-08, 2.4095596209056268e-09, 2.0891100299942761e-10, 1.584867664037942e-11, 1.0687402669398226e-12, 5.6190076053611874e-14, 3.616411354300662e-15, 1.8290191622271764e-16, 8.538794872902278e-18, 3.7016062724231615e-19, 1.497685553991192e-20, 5.680967903408846e-22, 2.028126742692666e-23], [6.711896439097219e-06, 4.073492531449186e-06, 1.236114230481496e-06, 2.5006852293655205e-07, 3.794204327255632e-08, 4.605453355876533e-09, 4.658464767081537e-10, 4.038931174331027e-11, 3.0640661925736744e-12, 2.0662235686159334e-13, 1.2540041926203141e-14, 5.993682735609234e-16, 3.536090682972979e-17, 1.6508275920477696e-18, 7.15641242162345e-20, 2.8955147342702826e-21, 1.0983164139762818e-22, 3.921030586683982e-24], [1.1894928189233148e-06, 7.219107383528537e-07, 2.1906610357719222e-07, 4.43175360303679e-08, 6.724148445599952e-09, 8.161856703853221e-10, 8.255804358620407e-11, 7.157857204123469e-12, 5.430186186338589e-13, 3.6617938304920234e-14, 2.222365907395055e-15, 1.2261526987687626e-16, 5.3721825224536275e-18, 2.925622562623164e-19, 1.2682706388598084e-20, 5.131476647104543e-22, 1.946453583104027e-23, 6.948911932655809e-25], [1.9458810818285942e-07, 1.1809675738952846e-07, 3.5836835652913955e-08, 7.24986763962209e-09, 1.0999976665301439e-09, 1.335191125155314e-10, 1.3505599412747005e-11, 1.1709477096752708e-12, 8.88319492367144e-14, 5.9902970635507955e-15, 3.635549292357407e-16, 2.0058526642698706e-17, 1.0144705897992312e-18, 4.1028303176031325e-20, 2.074753040568855e-21, 8.394538555082854e-23, 3.1841866918103585e-24, 1.1367665322508888e-25], [2.9558751317578192e-08, 1.7939393705441903e-08, 5.4437659267336085e-09, 1.101285359347687e-09, 1.6709426787954624e-10, 2.028211425582882e-11, 2.0515573030859223e-12, 1.7787187757462306e-13, 1.3493946372489915e-14, 9.099512959626683e-16, 5.522552145612357e-17, 3.0469744855702066e-18, 1.5410234552819275e-19, 7.194283936839972e-21, 2.701761357120374e-22, 1.2751656814626115e-23, 4.836913388536409e-25, 1.7267961309009517e-26], [4.19075863254271e-09, 2.5433980016928077e-09, 7.718021917060432e-10, 1.5613721557427936e-10, 2.3690166679949776e-11, 2.875542491312391e-12, 2.9086416356669657e-13, 2.5218186601446235e-14, 1.9131346801497344e-15, 1.290103972180046e-16, 7.829722855758463e-18, 4.3199167959937103e-19, 2.1848207587622326e-20, 1.0199858305701146e-21, 4.4216847979365836e-23, 1.5498296624964528e-24, 6.857643044554412e-26, 2.4482041593925576e-27], [5.570196155977487e-10, 3.380587386287681e-10, 1.0258499661689085e-10, 2.0753161760337086e-11, 3.1488063843719193e-12, 3.8220611435547675e-13, 3.8660552608055934e-14, 3.3519049505093913e-15, 2.5428654751160174e-16, 1.7147568773934492e-17, 1.0406968278927806e-18, 5.741868248944426e-20, 2.9039802238797095e-21, 1.3557261705492061e-22, 5.877134386397863e-24, 2.3779134304337827e-25, 7.813821832944431e-27, 3.2540593704921605e-28], [6.968180493511179e-11, 4.229032950026503e-11, 1.2833134638995256e-11, 2.5961702767303306e-12, 3.93908052984419e-13, 4.781305928866646e-14, 4.8363415041089064e-15, 4.193151917491915e-16, 3.181063126890371e-17, 2.145119326066237e-18, 1.3018865283585075e-19, 7.182938124301029e-21, 3.6328089322071267e-22, 1.6959806067199057e-23, 7.35215278641381e-25, 2.974712113760236e-26, 1.1283572840185634e-27, 3.4896764506955803e-29]] |
| Legacy trial inputs | {"lambda_home": 2.1266588298253972, "lambda_away": 0.6069063443411965, "rho": -0.03320816174939849, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7419 |
| Legacy p draw | 0.1648 |
| Legacy p away | 0.0933 |
| Legacy p over 1 5 | 0.7632 |
| Legacy p under 3 5 | 0.7036 |
| Legacy p btts yes | 0.3976 |
| Legacy p over 2 5 | 0.5233 |
| Legacy goal margin distribution | {"-1": 0.07061820799751341, "-10": 1.4126848996448742e-10, "-11": 7.71938503811249e-12, "-12": 3.8723060946116977e-13, "-13": 1.7951369039854182e-14, "-14": 7.734703409673572e-16, "-15": 3.112622841696393e-17, "-16": 1.172163321670677e-18, "-17": 3.889375627969733e-20, "-2": 0.018659593143884, "-3": 0.0034277074940133115, "-4": 0.0004897367481808378, "-5": 5.7061541906631515e-05, "-6": 5.603451680963062e-06, "-7": 4.7506525309952623e-07, "-8": 3.5414050732022924e-08, "-9": 2.3547313540585106e-09, "0": 0.16481736175448322, "1": 0.2520169116287379, "10": 3.9016812163774466e-05, "11": 7.47076937567147e-06, "12": 1.3131926760745951e-06, "13": 2.133204511498207e-07, "14": 3.220733048616462e-08, "15": 4.541650505810473e-09, "16": 5.993099450980137e-10, "17": 6.968180493511179e-11, "2": 0.22672503659466614, "3": 0.14594096403246487, "4": 0.07306548915265385, "5": 0.02983109890193946, "6": 0.010264966267683995, "7": 0.0030495187508861707, "8": 0.0007965807234254855, "9": 0.00018559731981148276} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7242 |
| Legacy raw p draw | 0.1857 |
| Legacy raw p away | 0.0901 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1267 |
| Legacy lambda away | 0.6069 |
| Legacy model home team | Como |
| Legacy model away team | Venezia |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 89.1% |
| Market home draw odds | 1.09 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:54:22Z |
| Market reference home draw last update utc | 2026-10-30T11:54:36Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 27.2% |
| Market draw away odds | 3.82 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:54:22Z |
| Market reference draw away last update utc | 2026-10-30T11:54:36Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.6% |
| Market home away odds | 1.15 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:54:22Z |
| Market reference home away last update utc | 2026-10-30T11:54:36Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.07 |
| Market reference dc draw away odds | 3.50 |
| Market reference dc home away odds | 1.14 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.33, "price": 1.58, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.58, "price": 2.33, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.83, "price": 2.0, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.0, "price": 1.83, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.48, "price": 2.57, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:54:22Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.57, "price": 1.48, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 88.6% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-10-30T11:54:36Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.6% |
| Market under 3 5 odds | 1.85 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:54:14Z |
| Market reference under 3 5 odds | 1.85 |
| Market reference under 3 5 opposite odds | 2.04 |
| Market reference under 3 5 last update utc | 2026-10-30T11:54:16Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:54:22Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.15 |
| Market reference btts yes last update utc | 2026-10-30T11:54:36Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021569260499678382, "mu": 9.837532916242429, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,565.5304 |
| Elo away rating | 1,354.7810 |
| Elo rating diff | 270.7494 |
| Elo home expectancy | 0.8261 |

</details>


---

## 2026-11-01 — Frosinone vs Torino

The model's most likely 1X2 outcome is **Frosinone win** at **46.9%**. Expected goals are 1.99 for Frosinone and 1.43 for Torino (3.41 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.8%; Under 3.5 goals: 55.8%; Double Chance 1X: 70.4%; Double Chance X2: 53.1%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 74.5%; BTTS Yes (both teams score): 66.2%; BTTS No (at least one team does not score): 33.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 46.9% | 2.13 |
| Draw | 23.5% | 4.26 |
| Torino win | 29.6% | 3.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.99 |
| Torino expected goals | 1.43 |
| Expected total goals | 3.41 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.6% |
| Under 1.5 | 14.4% |
| Over 2.5 | 65.8% |
| Under 2.5 | 34.2% |
| Over 3.5 | 44.2% |
| Under 3.5 | 55.8% |
| Over 4.5 | 25.5% |
| Under 4.5 | 74.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.10% |
| 2 | 2-1 | 8.64% |
| 3 | 1-2 | 7.20% |
| 4 | 2-2 | 6.98% |
| 5 | 2-0 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 46.9% | 45.5% | 2.15 | +0.9% |
| Draw | 23.5% | 24.0% | 4.00 | -6.2% |
| Torino win | 29.6% | 30.6% | 3.16 | -6.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:00:00+00:00 |
| Fixture id | b7b781db85506536dce5e7ce59a59863 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T11:54:14Z |
| Market best draw last update utc | 2026-10-30T11:54:14Z |
| Market best away last update utc | 2026-10-30T11:54:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Frosinone |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9865 |
| Dc lambda away | 1.4268 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:54:12.994081+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 66.2% |
| P btts no | 33.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.82 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.94 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.92 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.92 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.16343454285202716, "-10": 4.4259574749693246e-07, "-11": 5.622399820405087e-08, "-12": 6.567668846313191e-09, "-13": 7.099325489626912e-10, "-14": 7.139926739315353e-11, "-15": 6.708867022429374e-12, "-16": 5.85634097603533e-13, "-17": 4.212893318867722e-14, "-2": 0.08516363739110912, "-3": 0.03350281154884138, "-4": 0.01057432062349571, "-5": 0.002771535646618947, "-6": 0.0006192395494265433, "-7": 0.00012035416107558922, "-8": 2.0675986564867555e-05, "-9": 3.1802203560544894e-06, "0": 0.2345008877609008, "1": 0.19703103230870903, "10": 1.044033120537966e-05, "11": 1.846481818196819e-06, "12": 3.0029688461812953e-07, "13": 4.5193183850205015e-08, "14": 6.32799133943742e-09, "15": 8.278231637994621e-10, "16": 1.0060765255999192e-10, "17": 1.0076307051047185e-11, "2": 0.14230857813512374, "3": 0.077942512634023, "4": 0.0342501038240926, "5": 0.012498162206419606, "6": 0.0038877707172731207, "7": 0.0010520087174858994, "8": 0.0002516174404278075, "9": 5.388253035560314e-05} |
| Raw goal margin distribution | {"-1": 0.15123398462920415, "-10": 4.0955551565684187e-07, "-11": 5.2026818393479926e-08, "-12": 6.077385551549651e-09, "-13": 6.569353474730489e-10, "-14": 6.606923798997052e-11, "-15": 6.208043137294912e-12, "-16": 5.419159044945559e-13, "-17": 3.898396460820249e-14, "-2": 0.07880608348404826, "-3": 0.031001791900259566, "-4": 0.009784936615791997, "-5": 0.002564637634527224, "-6": 0.0005730126744660059, "-7": 0.00011136959805765231, "-8": 1.9132502711962813e-05, "-9": 2.9428136063040438e-06, "0": 0.22216801695785943, "1": 0.21149292236622477, "10": 1.120664156921963e-05, "11": 1.9820118244860054e-06, "12": 3.2233838985248e-07, "13": 4.8510320488695194e-08, "14": 6.7924598749951605e-09, "15": 8.88584595344799e-10, "16": 1.0799215840771893e-10, "17": 1.0815898388769542e-11, "2": 0.15275389219106894, "3": 0.08366341880454789, "4": 0.03676402881427615, "5": 0.01341551540521442, "6": 0.00417312938399289, "7": 0.0011292251550874227, "8": 0.0002700859208361073, "9": 5.783745674913981e-05} |
| Unadjusted home-win probability | 50.4% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 85.7% |
| Raw p under 3 5 | 55.5% |
| Raw p btts yes | 65.8% |
| P home draw | 70.4% |
| P draw away | 53.1% |
| P home away | 76.5% |
| Raw p home draw | 72.6% |
| Raw p draw away | 49.6% |
| Raw p home away | 77.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6580 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.15 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.16 |
| Market reference 1x2 last update utc | 2026-10-30T11:54:14Z |
| Market reference home last update utc | 2026-10-30T11:54:14Z |
| Market reference draw last update utc | 2026-10-30T11:54:14Z |
| Market reference away last update utc | 2026-10-30T11:54:14Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.95 |
| Market reference over 2 5 last update utc | 2026-10-30T11:53:51Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:53:51Z |
| Home probability edge | +1.5% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | 0.0492 |
| Raw ev home | 0.0830 |
| Raw edge prob draw | -0.0176 |
| Raw ev draw | -0.1113 |
| Raw edge prob away | -0.0316 |
| Raw ev away | -0.1338 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.04604666565843063, 0.05627698370256361, 0.04208644650410256, 0.019764392284027363, 0.006961229234193756, 0.0019614551969869896, 0.0004605635920939065, 9.269451259086201e-05, 1.6323996751934634e-05, 2.5553268114235244e-06, 3.6000531555885186e-07, 4.610825534801839e-08, 5.413272691848113e-09, 5.866499179803266e-10, 5.903552640952968e-11, 5.544784126824601e-12, 4.882329899935537e-13], [0.07102271892501297, 0.10833481154102961, 0.07358858794921005, 0.03455824477160501, 0.012171781470909976, 0.0034296247429167486, 0.0008053002146356727, 0.00016207731606746314, 2.8542677523160885e-05, 4.468015416390268e-06, 6.294730258018635e-07, 8.062076239987463e-08, 9.465163411652981e-09, 1.025763462365108e-09, 1.0322422984539938e-10, 9.695112518859043e-12, 8.536804436635948e-13], [0.06513953804748072, 0.0917713532582445, 0.06457298833509514, 0.03021272459410044, 0.010641243032757723, 0.0029983672059639686, 0.0007040378862166258, 0.00014169693355840562, 2.495358375070129e-05, 3.9061856338407055e-06, 5.503200551317674e-07, 7.048311935550581e-08, 8.27496816705793e-09, 8.96779023123071e-10, 9.024431791511765e-11, 8.476002365773498e-12, 7.463345521810131e-13], [0.037965719154666414, 0.05348772080186622, 0.037677888635842594, 0.017674170838670396, 0.006202107913994568, 0.001747558712823762, 0.00041033918052753467, 8.258618568394826e-05, 1.4543866612793899e-05, 2.2766686897946833e-06, 3.207467735353593e-07, 4.108015492288955e-08, 4.822955870754391e-09, 5.226758057582414e-10, 5.2597708426676445e-11, 4.940125997496083e-12, 4.349912334790335e-13], [0.0165958633665819, 0.023380958558993796, 0.01647004470518179, 0.007734566624838456, 0.00272113280838997, 0.0007639061308163889, 0.00017937057760574867, 3.610070042383239e-05, 6.357525380842232e-06, 9.951947005898768e-07, 1.402072645372383e-07, 1.7957269172247342e-08, 2.1082470827964266e-09, 2.2847601600918741e-10, 2.299190959318746e-11, 2.1594653780729752e-12, 1.901466701333817e-13], [0.005803607823367734, 0.00817636967800373, 0.005759608776647593, 0.002704793982858434, 0.0009526572168455664, 0.0002681269096146253, 6.272626283311687e-05, 1.26244897768136e-05, 2.2232398051559862e-06, 3.480216498858228e-07, 4.903077106550665e-08, 6.2796942558728425e-09, 7.372583753580014e-10, 7.989853644088617e-11, 8.04031844814284e-12, 7.551695193943576e-13, 6.649468472942143e-14], [0.0016912780725064226, 0.002382744522025553, 0.0016784559409644985, 0.000788226719151613, 0.00027762183636504686, 7.822509149109515e-05, 1.8347148432954102e-05, 3.679008538470889e-06, 6.478929739607803e-07, 1.014199103598017e-07, 1.4288468570754325e-08, 1.8300184161719016e-09, 2.1485065186419465e-10, 2.3283903189277203e-11, 2.3430966910892907e-12, 2.2007028869772128e-13, 1.9377774247302424e-14], [0.0004224596057582073, 0.0005951790706454754, 0.0004192568014859604, 0.00019688894122974629, 6.934637978652198e-05, 1.9539626185038392e-05, 4.5880428152410825e-06, 9.223657481990486e-07, 1.618353686495538e-07, 2.5333394929633518e-08, 3.5690764856566695e-09, 4.571151670408147e-10, 5.366694168093216e-11, 5.816020867152206e-12, 5.852755501666228e-13, 5.497074012468824e-14, 4.840319875285225e-15], [9.233437494626682e-05, 0.00013008459677587124, 9.163435788777813e-05, 4.3032794318058184e-05, 1.5156607981212992e-05, 4.270654864720584e-06, 1.002780052335845e-06, 2.0182274453026625e-07, 3.550208552454512e-08, 5.5369629526980936e-09, 7.800709036952105e-10, 9.990882596081671e-11, 1.172965047508653e-11, 1.2711715963450092e-12, 1.279200457496466e-13, 1.2014613611725529e-14, 1.0579186841362779e-15], [1.7938623518107757e-05, 2.5272696202526857e-05, 1.7802624953371822e-05, 8.360365212338759e-06, 2.9446095730300913e-06, 8.296982552660402e-07, 1.948190350645614e-07, 3.9209906750617643e-08, 6.9050731542855175e-09, 1.0796910955909418e-09, 1.515513400828436e-10, 1.9410179752559238e-11, 2.278823937390809e-12, 2.469618569142338e-13, 2.4852169546362514e-14, 2.3341862705162665e-15, 2.0553130942334852e-16], [3.136586915983413e-06, 4.4189571268080864e-06, 3.1128074259733427e-06, 1.4618185231098905e-06, 5.148680360074775e-07, 1.450735999367382e-07, 3.406431021595324e-08, 6.855892837417105e-09, 1.2073591983118272e-09, 1.8899766872958867e-10, 2.6596849288891773e-11, 3.3938900488829445e-12, 3.984547275121023e-13, 4.3181536663737474e-14, 4.345427605091112e-15, 4.081348888435633e-16, 3.593736249113364e-17], [4.98577703102085e-07, 7.024174854404756e-07, 4.947978226690754e-07, 2.3236407634369718e-07, 8.184109979072785e-08, 2.306024483766998e-08, 5.414709045262327e-09, 1.089781789937025e-09, 1.9191637025774956e-10, 3.004221661662552e-11, 4.232475323628222e-12, 5.414713653164182e-13, 6.333656555819214e-14, 6.863942222201936e-15, 6.907295644518904e-16, 6.487528032413839e-17, 5.712440983245874e-18], [7.264735681328851e-08, 1.0234868783580328e-07, 7.209659347024308e-08, 3.3857583000005175e-08, 1.1925000940669006e-08, 3.3600897603336883e-09, 7.889729075404938e-10, 1.587912296309991e-10, 2.7963980221496627e-11, 4.377427262452669e-12, 6.167105811711386e-13, 7.898619193531102e-14, 9.262829611109654e-15, 1.0001395101697944e-15, 1.0064565025273389e-16, 9.45292500796971e-18, 8.323551891764897e-19], [9.771127415113602e-09, 1.3765980119326131e-08, 9.6970493063353e-09, 4.553871909078467e-09, 1.6039221346496763e-09, 4.519347518564288e-10, 1.0611748513389357e-10, 2.1357546993963643e-11, 3.7611776362382355e-12, 5.887674570424716e-13, 8.294806488774685e-14, 1.0623705793152394e-14, 1.2472607350295686e-15, 1.3501674799449915e-16, 1.3536920206524813e-17, 1.271425950647807e-18, 1.1195243660381578e-19], [1.2203512546829914e-09, 1.7192827804677078e-09, 1.2110993731803192e-09, 5.687494453622296e-10, 2.0031960553559082e-10, 5.6443757002878794e-11, 1.325339447796415e-11, 2.6674208782417625e-12, 4.697470058950793e-13, 7.353328581172135e-14, 1.0359682231010103e-14, 1.326832835482553e-15, 1.5577488024113215e-16, 1.6881713876057485e-17, 1.6969234243462234e-18, 1.5879296095449874e-19, 1.3982142558387283e-20], [1.4225312120441451e-10, 2.0041225083024806e-10, 1.4117465382404506e-10, 6.629762002995908e-11, 2.3350727109529862e-11, 6.579499611567814e-12, 1.5449131746363493e-12, 3.109342036070427e-13, 5.4757167257030444e-14, 8.571580828874483e-15, 1.207600784111882e-15, 1.5466539772020547e-16, 1.815826618320743e-17, 1.967856779704692e-18, 1.9802859819427142e-19, 1.8578489411948978e-20, 1.6298614127883604e-21], [1.5545691057244906e-11, 2.1901431118809265e-11, 1.542783409517201e-11, 7.2451297383861674e-12, 2.5518117742046396e-12, 7.190202043139562e-13, 1.6883104370450067e-13, 3.397947986996835e-14, 5.983967157560445e-15, 9.367186203697214e-16, 1.3196890550692145e-16, 1.6902128191262563e-17, 1.984369789775835e-18, 2.1505112354079332e-19, 2.164094103498585e-20, 2.0325785783281654e-21, 1.7877266185016911e-22]] |
| Legacy trial inputs | {"lambda_home": 1.7485103652558713, "lambda_away": 1.408842555674123, "rho": -0.03320816174939849, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4537 |
| Legacy p draw | 0.2396 |
| Legacy p away | 0.3066 |
| Legacy p over 1 5 | 0.8267 |
| Legacy p under 3 5 | 0.6120 |
| Legacy p btts yes | 0.6276 |
| Legacy p over 2 5 | 0.6111 |
| Legacy goal margin distribution | {"-1": 0.1671108830893978, "-10": 4.4944748838842944e-07, "-11": 5.652502145128392e-08, "-12": 6.534410744795968e-09, "-13": 6.987851414249786e-10, "-14": 6.947697348056974e-11, "-15": 6.398464570488196e-12, "-16": 4.882329899935537e-13, "-2": 0.08922616211492701, "-3": 0.03538330917287621, "-4": 0.011184198353606565, "-5": 0.002924042322247312, "-6": 0.0006500178683576215, "-7": 0.00012548284093034546, "-8": 2.1385602923124142e-05, "-9": 3.2603426536967142e-06, "0": 0.23963720221433588, "1": 0.2092422067162185, "10": 3.915861934739402e-06, "11": 6.112162594368997e-07, "12": 8.769328573759914e-08, "13": 1.163882997914374e-08, "14": 1.4361913396084114e-09, "15": 1.6415455232322378e-10, "16": 1.5545691057244906e-11, "2": 0.13810030222792524, "3": 0.06796833211541665, "4": 0.026663599415671632, "5": 0.008651737201706483, "6": 0.0023869906053417653, "7": 0.0005718939560407113, "8": 0.0001209646331571159, "9": 2.2887897995369233e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4529 |
| Legacy raw p draw | 0.2395 |
| Legacy raw p away | 0.3076 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7485 |
| Legacy lambda away | 1.4088 |
| Legacy model home team | Frosinone |
| Legacy model away team | Torino |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021569260499678382, "mu": 9.798265474221179, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.7336 |
| Elo away rating | 1,449.1597 |
| Elo rating diff | 85.5739 |
| Elo home expectancy | 0.6207 |

</details>


---

## 2026-11-01 — Juventus vs Napoli

The model's most likely 1X2 outcome is **Juventus win** at **40.7%**. Expected goals are 1.13 for Juventus and 1.10 for Napoli (2.23 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 47.3%; Under 3.5 goals: 73.7%; Double Chance 1X: 70.0%; Double Chance X2: 59.3%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 53.7%; BTTS No (at least one team does not score): 46.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 40.7% | 2.46 |
| Draw | 29.4% | 3.41 |
| Napoli win | 30.0% | 3.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.13 |
| Napoli expected goals | 1.10 |
| Expected total goals | 2.23 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 73.5% |
| Under 1.5 | 26.5% |
| Over 2.5 | 47.3% |
| Under 2.5 | 52.7% |
| Over 3.5 | 26.3% |
| Under 3.5 | 73.7% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.98% |
| 2 | 1-0 | 10.32% |
| 3 | 2-1 | 8.99% |
| 4 | 0-0 | 8.44% |
| 5 | 0-1 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 40.7% | 42.6% | 2.29 | -6.9% |
| Draw | 29.4% | 29.3% | 3.30 | -3.1% |
| Napoli win | 30.0% | 28.1% | 3.43 | +2.8% |
| Over 2.5 | 47.3% | 47.3% | 2.05 | -3.0% |
| Under 2.5 | 52.7% | 52.7% | 1.85 | -2.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T19:45:00+00:00 |
| Fixture id | aeadf1388a1075328536501576b3d550 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T11:54:14Z |
| Market best draw last update utc | 2026-10-30T11:54:14Z |
| Market best away last update utc | 2026-10-30T11:54:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Juventus |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1306 |
| Dc lambda away | 1.0954 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:54:12.994081+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 53.7% |
| P btts no | 46.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.86 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.77 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.81 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.35 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.1673120471293072, "-10": 2.347418111771989e-07, "-11": 2.6935373268126297e-08, "-12": 2.8378396384057854e-09, "-13": 2.748269920571234e-10, "-14": 2.239374131081006e-11, "-2": 0.08702093004862337, "-3": 0.032807016807080196, "-4": 0.009706759331294171, "-5": 0.0023540079153128598, "-6": 0.0004826421632933632, "-7": 8.560766582741001e-05, "-8": 1.3370047502608952e-05, "-9": 1.8643688815993522e-06, "0": 0.2936423183753679, "1": 0.22227542501808795, "10": 4.14273210903386e-07, "11": 4.906223520009425e-08, "12": 5.335069910576685e-09, "13": 5.33260703485105e-10, "14": 4.484714348645584e-11, "2": 0.11926050947024994, "3": 0.046405303060420164, "4": 0.01417108380930644, "5": 0.0035470283194089032, "6": 0.0007506023649392141, "7": 0.00013741218889929863, "8": 2.2149987460326778e-05, "9": 3.187867868304496e-06} |
| Raw goal margin distribution | {"-1": 0.20483980699566434, "-10": 8.280380702690773e-08, "-11": 8.168988521515472e-09, "-12": 7.370730263354048e-10, "-13": 5.6706966149634734e-11, "-2": 0.0960116757495573, "-3": 0.03194658669624384, "-4": 0.008257324172747832, "-5": 0.0017393001528492084, "-6": 0.0003086439849325063, "-7": 4.7272384443235856e-05, "-8": 6.365028745141027e-06, "-9": 7.643256925322198e-07, "0": 0.296063439796115, "1": 0.2115281516783109, "10": 1.1358726147596444e-07, "11": 1.1565796397382224e-08, "12": 1.0770744097892219e-09, "13": 8.552627058127628e-11, "2": 0.10227745543592694, "3": 0.035124347125385064, "4": 0.00937024755157476, "5": 0.002037108671062279, "6": 0.0003731001402191165, "7": 5.897976476054708e-05, "8": 8.196412914194487e-06, "9": 1.0158506212690876e-06} |
| Unadjusted home-win probability | 36.1% |
| Unadjusted draw probability | 29.6% |
| Unadjusted away-win probability | 34.3% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.4% |
| Raw p btts yes | 45.4% |
| P home draw | 70.0% |
| P draw away | 59.3% |
| P home away | 70.6% |
| Raw p home draw | 65.7% |
| Raw p draw away | 63.9% |
| Raw p home away | 70.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1668 |
| Totals anchor target over 2 5 | 0.4733 |
| Totals anchor reference over odds | 2.05 |
| Totals anchor reference under odds | 1.85 |
| Totals anchor reference last update utc | 2026-10-30T11:54:14Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3852 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.4, "price": 1.67, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.29 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.43 |
| Market reference 1x2 last update utc | 2026-10-30T11:54:14Z |
| Market reference home last update utc | 2026-10-30T11:54:14Z |
| Market reference draw last update utc | 2026-10-30T11:54:14Z |
| Market reference away last update utc | 2026-10-30T11:54:14Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-30T11:54:14Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:54:14Z |
| Market best over 2 5 last update utc | 2026-10-30T11:54:14Z |
| Market best under 2 5 last update utc | 2026-10-30T11:54:14Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.1% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0654 |
| Raw ev home | -0.1738 |
| Raw edge prob draw | 0.0035 |
| Raw ev draw | -0.0230 |
| Raw edge prob away | 0.0620 |
| Raw ev away | 0.1770 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.1125194952781948, 0.10439922952010049, 0.058939483908822456, 0.021353137882600636, 0.005802008270110213, 0.0012612029258278702, 0.00022846009319323784, 3.5472266615802835e-05, 4.819207026994959e-06, 5.819822033698864e-07, 6.325375831081914e-08, 6.249859871184557e-09, 5.660641675399887e-10, 4.732590662984562e-11], [0.12953244953502202, 0.1368103568890946, 0.06641185022251303, 0.024060295421549683, 0.0065375887040412944, 0.0014210986295680498, 0.0002574243356871261, 3.9969451737752975e-05, 5.430187610111801e-06, 6.55766090218234e-07, 7.127308969056574e-08, 7.042219072004355e-09, 6.37829960797638e-10, 5.332589996220646e-11], [0.07570989481944337, 0.08228662940064066, 0.040540307430315184, 0.013555333622510659, 0.0036832131284084218, 0.0008006329804676552, 0.00014503033697860638, 2.25183957021914e-05, 3.059314251892436e-06, 3.694521607276695e-07, 4.015455721285224e-08, 3.967516910799346e-09, 3.5934712195183863e-10, 3.0043287168490614e-11], [0.028436139701581046, 0.030906318055112666, 0.016795537399731417, 0.005516459191503164, 0.0013833906825508027, 0.0003007124938763564, 5.44724429102218e-05, 8.457761664708449e-06, 1.1490583584262177e-06, 1.3876380730098368e-07, 1.5081788203284547e-08, 1.4901733176744745e-09, 1.3496842104394685e-10, 1.1284061522675844e-11], [0.008010320609904314, 0.00870615769549627, 0.004731220228883846, 0.0017140699442938928, 0.00042223702079475747, 8.470922961528332e-05, 1.534461909016875e-05, 2.3825098373920933e-06, 3.2368408465698294e-07, 3.908908161222949e-08, 4.248465514194424e-09, 4.197744899330922e-10, 3.801993998202434e-11, 3.178664598187108e-12], [0.0018051743154121655, 0.0019619854214581274, 0.0010662091636106945, 0.0003862760542235347, 0.00010495772909220464, 2.0683888187319938e-05, 3.458002945238754e-06, 5.369130368339149e-07, 7.294417094966469e-08, 8.808961535472114e-09, 9.574174617499765e-10, 9.459872636752206e-11, 8.568023986980246e-12, 7.163313392053907e-13], [0.00033900581384497847, 0.00036845442507945893, 0.00020023058280456922, 7.254137565156822e-05, 1.9710717168108793e-05, 4.2845878539418595e-06, 7.036319674135093e-07, 1.0083050676150428e-07, 1.3698675982098819e-08, 1.6542940750738477e-09, 1.797998581294001e-10, 1.776533044322536e-11, 1.6090467939581456e-12, 1.3452467529405346e-13], [5.4569296797620625e-05, 5.9309599002192734e-05, 3.2230839869960364e-05, 1.1676884868553567e-05, 3.1728068703044076e-06, 6.896841785850601e-07, 1.2493256119749057e-07, 1.758593094786551e-08, 2.205056919004401e-09, 2.662894283415762e-10, 2.894213438746502e-11, 2.859660660886125e-12, 2.590060361056625e-13, 2.165425085034565e-14], [7.68595117679883e-06, 8.353611077983441e-06, 4.539634486155556e-06, 1.6446605007509832e-06, 4.4688204044503797e-07, 9.714031946709108e-08, 1.7596443826599085e-08, 2.732143448699231e-09, 3.3651255422890727e-10, 3.750621073094471e-11, 4.0764284113719055e-12, 4.027761673986129e-13, 3.648036285655632e-14, 3.049947948260316e-15], [9.622642761302327e-07, 1.0458538354100221e-06, 5.683523082871975e-07, 2.0590789738717504e-07, 5.594865401468071e-08, 1.2161755525747664e-08, 2.2030362790205704e-09, 3.4205838385789875e-10, 4.647152055392317e-11, 5.087824632649496e-12, 5.103599208782966e-13, 5.0426695180460415e-14, 4.567261637453306e-15, 3.818468120805781e-16], [1.0842604438087042e-07, 1.1784475137132012e-07, 6.404081927486791e-08, 2.3201296540132584e-08, 6.304184197340736e-09, 1.3703626717672583e-09, 2.482337911601156e-10, 3.8542465338291174e-11, 5.2363194550768785e-12, 6.32353977935348e-13, 6.230860312789076e-14, 5.681980746084817e-15, 5.146300504816179e-16, 4.302574710540256e-17], [1.1106575672802548e-08, 1.207137691153371e-08, 6.559994044660383e-09, 2.3766149286506496e-09, 6.457664230293004e-10, 1.4037251658562025e-10, 2.542772266395535e-11, 3.948081020021286e-12, 5.363801530053813e-13, 6.477491038283945e-14, 7.0401749439012154e-15, 6.306356621258086e-16, 5.2715910017839917e-17, 4.407324078211314e-18], [1.0428892359155912e-09, 1.1334824895261225e-09, 6.159726794640749e-10, 2.2316024308693567e-10, 6.063640777617239e-11, 1.3180749033566569e-11, 2.3876214452869736e-12, 3.707183311581301e-13, 5.0365216463421344e-14, 6.0822578250722454e-15, 6.610608781909623e-16, 6.531687547661566e-17, 5.363297843762449e-18, 4.1384050095778777e-19], [9.039285087401047e-11, 9.82450581667809e-11, 5.3389683812756625e-11, 1.9342505301299307e-11, 5.255685433204401e-12, 1.142446811000908e-12, 2.06948064870892e-13, 3.213216290915014e-14, 4.365425727132334e-15, 5.271821835195715e-16, 5.729772187023943e-17, 5.661366884595882e-18, 5.127630056863709e-19, 3.8865216604317175e-20]] |
| Legacy trial inputs | {"lambda_home": 1.1267803146232176, "lambda_away": 1.086867569911196, "rho": -0.03320816174939849, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T11:54:14Z", "over": 2.05, "under": 1.85, "bookmaker": "pinnacle", "event_id": "aeadf1388a1075328536501576b3d550", "kickoff_utc": "2026-11-01T19:45:00Z", "home_team": "Juventus", "away_team": "Napoli"}} |
| Legacy p home | 0.3933 |
| Legacy p draw | 0.2958 |
| Legacy p away | 0.3108 |
| Legacy p over 1 5 | 0.6535 |
| Legacy p under 3 5 | 0.8164 |
| Legacy p btts yes | 0.4516 |
| Legacy p over 2 5 | 0.3821 |
| Legacy goal margin distribution | {"-1": 0.1858380743538215, "-10": 7.066660856629801e-08, "-11": 6.917733119150685e-09, "-12": 6.193900675021951e-10, "-13": 4.732590662984562e-11, "-2": 0.08699960045387671, "-3": 0.02874828914767174, "-4": 0.007376927674064151, "-5": 0.0015423347801020743, "-6": 0.00027163196768512587, "-7": 4.128741665188419e-05, "-8": 5.516656584015041e-06, "-9": 6.573609570568937e-07, "0": 0.29583026125765144, "1": 0.23043805630844977, "10": 1.211327364771695e-07, "11": 1.2293447846141427e-08, "12": 1.1411342940823721e-09, "13": 9.039285087401047e-11, "2": 0.1117541275028141, "3": 0.03828432012565062, "4": 0.0101846727950643, "5": 0.002207561585681829, "6": 0.00040306740220718147, "7": 6.351512063455152e-05, "8": 8.798284225266957e-06, "9": 1.0868974374747334e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3605 |
| Legacy raw p draw | 0.2991 |
| Legacy raw p away | 0.3405 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1268 |
| Legacy lambda away | 1.0869 |
| Legacy model home team | Juventus |
| Legacy model away team | Napoli |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021569260499678382, "mu": 9.111241661534153, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,551.0647 |
| Elo away rating | 1,587.2609 |
| Elo rating diff | 23.8038 |
| Elo home expectancy | 0.5342 |

</details>


---

## 2026-11-01 — Lazio vs Cagliari

The model's most likely 1X2 outcome is **Lazio win** at **64.2%**. Expected goals are 1.76 for Lazio and 0.84 for Cagliari (2.60 combined). The most likely exact score is 1-0 at 12.3%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 52.9%; Under 3.5 goals: 69.5%; Double Chance 1X: 85.6%; Double Chance X2: 35.8%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 49.8%; BTTS No (at least one team does not score): 50.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 64.2% | 1.56 |
| Draw | 21.5% | 4.66 |
| Cagliari win | 14.4% | 6.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.76 |
| Cagliari expected goals | 0.84 |
| Expected total goals | 2.60 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 77.0% |
| Under 1.5 | 23.0% |
| Over 2.5 | 52.9% |
| Under 2.5 | 47.1% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.30% |
| 2 | 2-0 | 11.77% |
| 3 | 2-1 | 10.54% |
| 4 | 1-1 | 10.22% |
| 5 | 3-0 | 7.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 64.2% | 66.5% | 1.48 | -5.0% |
| Draw | 21.5% | 20.5% | 4.59 | -1.5% |
| Cagliari win | 14.4% | 13.1% | 7.07 | +1.5% |
| Over 2.5 | 52.9% | 52.9% | 1.84 | -2.6% |
| Under 2.5 | 47.1% | 47.1% | 2.06 | -3.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:00:00+00:00 |
| Fixture id | 3f9f4bc9a19bf36dcb74be2f29610d55 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T11:54:14Z |
| Market best draw last update utc | 2026-10-30T11:54:14Z |
| Market best away last update utc | 2026-10-30T11:54:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lazio |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7562 |
| Dc lambda away | 0.8405 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:54:12.994081+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 49.8% |
| P btts no | 50.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.10 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.35 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.28 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.65 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.09641748904579854, "-10": 5.537408409237294e-09, "-11": 4.4499197667041757e-10, "-12": 3.284211692863371e-11, "-13": 2.2407551963540786e-12, "-14": 1.4210907895329088e-13, "-15": 8.382549753100359e-15, "-16": 4.245191284903178e-16, "-2": 0.035406786350988505, "-3": 0.009354861215810126, "-4": 0.0019392648311722317, "-5": 0.00032945564966311213, "-6": 4.731508357090814e-05, "-7": 5.878214703227644e-06, "-8": 6.42992086287466e-07, "-9": 6.279587374528332e-08, "0": 0.21465309823425194, "1": 0.2621981879275801, "10": 1.1291880835826381e-05, "11": 1.895993900367218e-06, "12": 2.92375463293562e-07, "13": 4.168014460292659e-08, "14": 5.523084074030733e-09, "15": 6.807082185694974e-10, "16": 7.202895981522683e-11, "2": 0.1987678053778655, "3": 0.10972912243600923, "4": 0.047527689633498106, "5": 0.01687064030420579, "6": 0.0050624324681063215, "7": 0.0013141051002415393, "8": 0.0003003414746063438, "9": 6.128664016887163e-05} |
| Raw goal margin distribution | {"-1": 0.1189229548647902, "-10": 4.1304524075296455e-09, "-11": 3.121590566447053e-10, "-12": 2.1661727485040356e-11, "-13": 1.3893782538955054e-12, "-14": 8.282729113991929e-14, "-15": 4.596299964345429e-15, "-16": 2.2106407547132824e-16, "-2": 0.041914418677495714, "-3": 0.01053308342123846, "-4": 0.0020676765557728744, "-5": 0.0003318052951933603, "-6": 4.4942556206984344e-05, "-7": 5.260617307661979e-06, "-8": 5.417860849241835e-07, "-9": 4.979294553469532e-08, "0": 0.23804899898326704, "1": 0.2515492126250759, "10": 6.550099092147204e-06, "11": 1.0343111635206141e-06, "12": 1.4996619937971668e-07, "13": 2.0097675012940048e-08, "14": 2.5033628608871564e-09, "15": 2.902576906233906e-10, "16": 2.91688004041028e-11, "2": 0.1829841600115103, "3": 0.09607946986481827, "4": 0.039407846482724045, "5": 0.013213213013451464, "6": 0.003739451620723143, "7": 0.0009145593263995878, "8": 0.0001968013370918781, "9": 3.7791405233210924e-05} |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 17.4% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 47.3% |
| P home draw | 85.6% |
| P draw away | 35.8% |
| P home away | 78.5% |
| Raw p home draw | 82.6% |
| Raw p draw away | 41.2% |
| Raw p home away | 76.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0649 |
| Totals anchor target over 2 5 | 0.5294 |
| Totals anchor reference over odds | 1.84 |
| Totals anchor reference under odds | 2.06 |
| Totals anchor reference last update utc | 2026-10-30T11:54:14Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4923 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.48 |
| Reference draw odds | 4.59 |
| Reference away odds | 7.07 |
| Market reference 1x2 last update utc | 2026-10-30T11:54:14Z |
| Market reference home last update utc | 2026-10-30T11:54:14Z |
| Market reference draw last update utc | 2026-10-30T11:54:14Z |
| Market reference away last update utc | 2026-10-30T11:54:14Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-10-30T11:54:14Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:54:14Z |
| Market best over 2 5 last update utc | 2026-10-30T11:54:14Z |
| Market best under 2 5 last update utc | 2026-10-30T11:54:14Z |
| Home probability edge | -2.3% |
| Draw probability edge | +1.0% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0767 |
| Raw ev home | -0.1296 |
| Raw edge prob draw | 0.0334 |
| Raw ev draw | 0.0926 |
| Raw edge prob away | 0.0433 |
| Raw ev away | 0.2289 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06938598277597272, 0.049674091251056686, 0.022275382167457346, 0.006258946720244801, 0.0013189812104804426, 0.00022236475386164153, 3.124007337826134e-05, 3.7619355498337015e-06, 3.9638636715180384e-07, 3.7125605507516e-08, 3.1294707100627044e-09, 2.39814562465096e-10, 1.6845800421335577e-11, 1.0923093330052862e-12, 6.576804832518622e-14, 3.695907053511296e-15, 1.94714549314491e-16], [0.13070009391272233, 0.10412761014778854, 0.040327737111520504, 0.01133130538598779, 0.0023879063942166246, 0.00040257299601804524, 5.6557569116980926e-05, 6.810673179193047e-06, 7.176247342881507e-07, 6.721283826952279e-08, 5.665647895279989e-09, 4.3416443129472157e-10, 3.0497928417912665e-11, 1.9775357071202908e-12, 1.1906761209559231e-13, 6.6911340475390415e-15, 3.525145875169202e-16], [0.12171805162758817, 0.10260117572421072, 0.038449802787723815, 0.010257195618490096, 0.0021615535165446513, 0.0003644125570902847, 5.119640062446136e-05, 6.165080254475654e-06, 6.496001148608062e-07, 6.084164239867356e-08, 5.128593466312937e-09, 3.9300939747748696e-10, 2.7606988522970478e-11, 1.790082422062773e-12, 1.0778103206019308e-13, 6.0568723988339016e-15, 3.190992528542814e-16], [0.07345348856213968, 0.061916980979772926, 0.026096190995791472, 0.006519700449931497, 0.0013044379562511686, 0.00021991293186346327, 3.0895616364263585e-05, 3.72045597100373e-06, 3.9201576075900527e-07, 3.671625386928085e-08, 3.0949647688272483e-09, 2.371703366625604e-10, 1.6660056487853878e-11, 1.080265391665805e-12, 6.50428814772006e-14, 3.6551555132619825e-15, 1.9256760198095948e-16], [0.03324536650358368, 0.02802389329305408, 0.011811248873069667, 0.0033187299252757495, 0.0006218472168173174, 9.953354376754318e-05, 1.3983489545430248e-05, 1.6838944580804852e-06, 1.7742802822209033e-07, 1.661793524606025e-08, 1.4007944356284195e-09, 1.073443197929913e-10, 7.540413597109828e-12, 4.889327868571543e-13, 2.943868937319944e-14, 1.654339188576306e-15, 8.715692923362411e-17], [0.012037597294212523, 0.010146988213873493, 0.00427665784524914, 0.0012016572103187712, 0.0002532316302872783, 3.795943340973657e-05, 5.063190261342897e-06, 6.097103297129873e-07, 6.424375415483745e-08, 6.017079472768348e-09, 5.072044943842313e-10, 3.8867602598091574e-11, 2.7302590363691193e-12, 1.7703447460833476e-13, 1.0659262472133948e-14, 5.990088555037955e-16, 3.1558082399285674e-17], [0.003632179053734017, 0.0030617138244553874, 0.0012904225540897162, 0.00036258349921597204, 7.640915381964018e-05, 1.2881686673680274e-05, 1.6091378702703017e-06, 1.8397168756372216e-07, 1.938466726135012e-08, 1.8155707897081498e-09, 1.5304196472396403e-10, 1.1727763321466173e-11, 8.238180295278497e-13, 5.341771241760629e-14, 3.2162855205458808e-15, 1.8074266523337816e-16, 9.522216358060689e-18], [0.0009393942535165207, 0.0007918542368247741, 0.0003337433298267022, 9.377534822608407e-05, 1.9761779073209254e-05, 3.331604047552482e-06, 4.680577884101711e-07, 5.011563194113864e-08, 5.013476693259857e-09, 4.695629652263236e-10, 3.958140281128824e-11, 3.0331636485434994e-12, 2.1306491542210108e-13, 1.3815478625567815e-14, 8.318312756534177e-16, 4.674566384907335e-17, 2.4627407391459154e-18], [0.00021258695033318233, 0.00017919832560698944, 7.552683701897081e-05, 2.1221564025103778e-05, 4.472133324858341e-06, 7.539491981514584e-07, 1.0592248935453202e-07, 1.2755206218784905e-08, 1.1950037613294632e-09, 1.0626311412188635e-10, 8.957357022424062e-12, 6.864114906936581e-13, 4.821705095919593e-14, 3.1264726789720302e-15, 1.882452159154185e-16, 1.0578644782821024e-17, 5.573235531689464e-19], [4.276345460117246e-05, 3.604708308619302e-05, 1.5192787990838299e-05, 4.26887628018129e-06, 8.996030570467203e-07, 1.5166251858925964e-07, 2.1307100730578962e-08, 2.565805103326992e-09, 2.7035289420955233e-10, 2.2514395380569252e-11, 1.801839340442034e-12, 1.3807680374546324e-13, 9.699220325915514e-15, 6.28913356438312e-16, 3.786693271656757e-17, 2.1279734960358268e-18, 1.1210979990423384e-19], [7.741969777093052e-06, 6.526026262574611e-06, 2.750528612616519e-06, 7.728447444563291e-07, 1.628656932418475e-07, 2.7457244654029155e-08, 3.857474365251512e-09, 4.645177932683684e-10, 4.894515552217812e-11, 4.584210472416431e-12, 3.4358668379321007e-13, 2.4997663343262175e-14, 1.755963621857289e-15, 1.1385956170673983e-16, 6.8554949869472066e-18, 3.8525200188837693e-19, 2.0296552059915453e-20], [1.2741996341678105e-06, 1.0740755280323986e-06, 4.526913244138256e-07, 1.2719740828341563e-07, 2.6804987971054777e-08, 4.5190064157750475e-09, 6.348762093541441e-10, 7.645191331000459e-11, 8.055559638733574e-12, 7.544849017861329e-13, 6.359865028588509e-14, 4.333382135947358e-15, 2.8900244627700627e-16, 1.8739392693381136e-17, 1.1283006077152757e-18, 6.34060806231802e-20, 3.340475351135093e-21], [1.922360878331178e-07, 1.6204374260481534e-07, 6.829668355551082e-08, 1.9190032311448104e-08, 4.0440178161993765e-09, 6.817739473208373e-10, 9.578257242576386e-11, 1.1534155502776106e-11, 1.2153270403878969e-12, 1.138277095356777e-13, 9.59500803059798e-15, 7.352753439449289e-16, 4.592408707763508e-17, 2.827176717953501e-18, 1.7022457777471664e-19, 9.565955409955918e-21, 5.039711955533329e-22], [2.677134907599706e-08, 2.25666764641013e-08, 9.51119208056677e-09, 2.6724589518042304e-09, 5.631815225089776e-10, 9.49457957680211e-11, 1.333895581579422e-11, 1.606279584350005e-12, 1.6924993015862646e-13, 1.585197337737251e-14, 1.3362283443737489e-15, 1.0239655374599415e-16, 7.192857224792758e-18, 4.1469601526554616e-19, 2.3705963038933944e-20, 1.3321823930773604e-21, 7.018447447868577e-23], [3.4619509540729347e-09, 2.9182215245624892e-09, 1.2299447593850008e-09, 3.455904217473521e-10, 7.282811201002536e-11, 1.2277965048052877e-11, 1.7249340211333989e-12, 2.0771688134813466e-13, 2.1886642900442327e-14, 2.049906196432114e-15, 1.7279506454949583e-16, 1.3241463697941131e-17, 9.301480796202375e-19, 6.031232728836862e-20, 3.2288645448717426e-21, 1.7227186024959658e-22, 9.07594188446943e-24], [4.178383919350338e-10, 3.522132477639094e-10, 1.4844755088911169e-10, 4.171085841674855e-11, 8.789951565932097e-12, 1.4818826840621044e-12, 2.0819002555090116e-13, 2.507028228639553e-14, 2.641597121304706e-15, 2.474123753044974e-16, 2.0855411547852506e-17, 1.5981716586436903e-18, 1.1226374463587847e-19, 7.279365358536643e-21, 4.382912772151581e-22, 2.1899961091804976e-23, 1.095416143270594e-24], [4.7278865684496004e-11, 3.9853309688017136e-11, 1.6797000838472345e-11, 4.719628714675651e-12, 9.94592520649811e-13, 1.6767662745276403e-13, 2.3556926421455433e-14, 2.8367295389055233e-15, 2.9889956954969055e-16, 2.7994977691093016e-17, 2.3598123590306988e-18, 1.808348506221788e-19, 1.2702764050229993e-20, 8.2366805850654725e-22, 4.9593131761246927e-23, 2.78694001342161e-24, 1.305507626263864e-25]] |
| Legacy trial inputs | {"lambda_home": 1.810417294228796, "lambda_away": 0.8429413250725705, "rho": -0.03320816174939849, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T11:54:14Z", "over": 1.84, "under": 2.06, "bookmaker": "pinnacle", "event_id": "3f9f4bc9a19bf36dcb74be2f29610d55", "kickoff_utc": "2026-11-01T14:00:00Z", "home_team": "Lazio", "away_team": "Cagliari"}} |
| Legacy p home | 0.6320 |
| Legacy p draw | 0.2191 |
| Legacy p away | 0.1488 |
| Legacy p over 1 5 | 0.7502 |
| Legacy p under 3 5 | 0.7205 |
| Legacy p btts yes | 0.4748 |
| Legacy p over 2 5 | 0.5021 |
| Legacy goal margin distribution | {"-1": 0.10166824776460184, "-10": 3.592352442492507e-09, "-11": 2.721693020838197e-10, "-12": 1.8934859472958558e-11, "-13": 1.2176263851016935e-12, "-14": 7.277828162557953e-14, "-15": 4.0484216410282164e-15, "-16": 1.94714549314491e-16, "-2": 0.03600276706505583, "-3": 0.009043911281976628, "-4": 0.0017766546643256291, "-5": 0.0002854965560775905, "-6": 3.87385034260466e-05, "-7": 4.543607020128417e-06, "-8": 4.689726899359624e-07, "-9": 4.320142263201606e-08, "0": 0.21914456328301196, "1": 0.26298278496295735, "10": 8.887088781184386e-06, "11": 1.4461091169031333e-06, "12": 2.160754145075415e-07, "13": 2.984273778016334e-08, "14": 3.830961202675317e-09, "15": 4.576917016230509e-10, "16": 4.7278865684496004e-11, "2": 0.1967277879866205, "3": 0.10613716070771947, "4": 0.04478118035077405, "5": 0.015455203719403102, "6": 0.00450399648596859, "7": 0.0011345857121700653, "8": 0.0002515159001541905, "9": 4.9761937890986656e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5992 |
| Legacy raw p draw | 0.2337 |
| Legacy raw p away | 0.1671 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8104 |
| Legacy lambda away | 0.8429 |
| Legacy model home team | Lazio |
| Legacy model away team | Cagliari |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021569260499678382, "mu": 9.342652294376947, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,538.3289 |
| Elo away rating | 1,414.0618 |
| Elo rating diff | 184.2671 |
| Elo home expectancy | 0.7428 |

</details>


---

## 2026-11-01 — Lecce vs Genoa

The model's most likely 1X2 outcome is **Genoa win** at **40.0%**. Expected goals are 0.86 for Lecce and 1.09 for Genoa (1.95 combined). The most likely exact score is 0-1 at 15.1%. Goal-market probabilities: at least one goal: 85.4%; Over 2.5 goals: 31.0%; Under 3.5 goals: 86.6%; Double Chance 1X: 60.0%; Double Chance X2: 71.7%; Double Chance 12 (either team wins): 68.3%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 38.6%; BTTS No (at least one team does not score): 61.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 28.3% | 3.53 |
| Draw | 31.7% | 3.16 |
| Genoa win | 40.0% | 2.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.86 |
| Genoa expected goals | 1.09 |
| Expected total goals | 1.95 |
| Over 0.5 | 85.4% |
| Under 0.5 | 14.6% |
| Over 1.5 | 58.4% |
| Under 1.5 | 41.6% |
| Over 2.5 | 31.0% |
| Under 2.5 | 69.0% |
| Over 3.5 | 13.4% |
| Under 3.5 | 86.6% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.06% |
| 2 | 0-0 | 14.56% |
| 3 | 1-1 | 13.66% |
| 4 | 1-0 | 12.03% |
| 5 | 0-2 | 8.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 28.3% | 28.5% | 3.39 | -4.0% |
| Draw | 31.7% | 31.7% | 3.06 | -3.1% |
| Genoa win | 40.0% | 39.8% | 2.45 | -2.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T17:00:00+00:00 |
| Fixture id | 940b9e69539033539039f9af694e2925 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T11:54:14Z |
| Market best draw last update utc | 2026-10-30T11:54:14Z |
| Market best away last update utc | 2026-10-30T11:54:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lecce |
| Matched away-team name | Genoa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8554 |
| Dc lambda away | 1.0949 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:54:12.994081+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 38.6% |
| P btts no | 61.4% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.87 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.40 |
| Fair Over 2.5 odds | 3.23 |
| Fair Under 2.5 odds | 1.45 |
| Fair Over 3.5 odds | 7.47 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.73 |
| Fair Under 4.5 odds | 1.05 |
| Goal margin distribution | {"-1": 0.23482729410416886, "-10": 1.0446379780011489e-07, "-11": 1.0324971769811535e-08, "-12": 9.344245791955938e-10, "-13": 7.341419499763256e-11, "-2": 0.11386810606162522, "-3": 0.03867260478061291, "-4": 0.010125966314818336, "-5": 0.0021517435962651993, "-6": 0.0003842447477628202, "-7": 5.912761899856562e-05, "-8": 7.989830361987382e-06, "-9": 9.621207311121177e-07, "0": 0.31681033778205836, "1": 0.18799107025913303, "10": 9.101403321461415e-09, "11": 7.027641260738764e-10, "12": 4.968704010843216e-11, "13": 3.0496996871909887e-12, "2": 0.071502191758683, "3": 0.018971376526564207, "4": 0.003880699892970626, "5": 0.0006442319524063039, "6": 8.987478060971347e-05, "7": 1.0804345306049652e-05, "8": 1.1405748343261654e-06, "9": 1.0729857657684578e-07} |
| Raw goal margin distribution | {"-1": 0.23756065565744303, "-10": 1.0567974388383193e-07, "-11": 1.0445153203498388e-08, "-12": 9.453011692825818e-10, "-13": 7.426872742682321e-11, "-2": 0.11519351716615774, "-3": 0.039122749264351685, "-4": 0.010243831348865, "-5": 0.0021767896337838454, "-6": 0.0003887173105651515, "-7": 5.981585739574117e-05, "-8": 8.082831029613994e-06, "-9": 9.733197010873173e-07, "0": 0.3168943515824845, "1": 0.18484266766697713, "10": 8.948976497304038e-09, "11": 6.909945010956511e-10, "12": 4.885490055170584e-11, "13": 2.998624482463371e-12, "2": 0.07030470038014276, "3": 0.018653651163595276, "4": 0.0038157074144153087, "5": 0.0006334426019009325, "6": 8.836959213532997e-05, "7": 1.0623398260420171e-05, "8": 1.1214729229428733e-06, "9": 1.0550158102719803e-07} |
| Unadjusted home-win probability | 27.8% |
| Unadjusted draw probability | 31.7% |
| Unadjusted away-win probability | 40.5% |
| Raw p over 1 5 | 58.4% |
| Raw p under 3 5 | 86.6% |
| Raw p btts yes | 38.6% |
| P home draw | 60.0% |
| P draw away | 71.7% |
| P home away | 68.3% |
| Raw p home draw | 59.5% |
| Raw p draw away | 72.2% |
| Raw p home away | 68.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3098 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:54:15Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:54:14Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.39 |
| Reference draw odds | 3.06 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-30T11:54:14Z |
| Market reference home last update utc | 2026-10-30T11:54:14Z |
| Market reference draw last update utc | 2026-10-30T11:54:14Z |
| Market reference away last update utc | 2026-10-30T11:54:14Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.48 |
| Reference Under 2.5 odds | 1.63 |
| Market reference over 2 5 last update utc | 2026-10-30T11:54:15Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:54:15Z |
| Home probability edge | -0.2% |
| Draw probability edge | +0.0% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -8.4% |
| Under 2.5 probability edge | +8.4% |
| Raw edge prob home | -0.0068 |
| Raw ev home | -0.0564 |
| Raw edge prob draw | 0.0001 |
| Raw ev draw | -0.0303 |
| Raw edge prob away | 0.0067 |
| Raw ev away | -0.0083 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.14930194468070115, 0.15206229220592457, 0.08331766514957857, 0.029566739212627483, 0.007869208163401819, 0.0016755161716988504, 0.00029729319470380295, 4.521416578198845e-05, 6.016890802775263e-06, 7.1173318374174e-07, 7.577131234373602e-08, 7.333304499037083e-09, 6.505880274626086e-10, 5.3278293869367114e-11], [0.12127236246416942, 0.1367996989231411, 0.0715094059294037, 0.025376370696044294, 0.00675393867422273, 0.001438052372785432, 0.00025515909143585767, 3.880615387936037e-05, 5.164142394966385e-06, 6.108622590208577e-07, 6.503256569257405e-08, 6.2939863627253546e-09, 5.583829463429105e-10, 4.5727387303650394e-11], [0.05394978634101442, 0.05743509232254863, 0.030244819401475925, 0.010889942666184014, 0.002898365799198916, 0.0006171216553454741, 0.00010949823793854169, 1.6653161159378233e-05, 2.216125200675779e-06, 2.62143671266189e-07, 2.7907888023458457e-08, 2.700983188368519e-09, 2.3962285010271694e-10, 1.9623319346007488e-11], [0.01543457066532912, 0.01643168678219848, 0.008746609684284309, 0.003070592322323968, 0.0008291975701060326, 0.00017655320705678814, 3.132650573458537e-05, 4.764326425517861e-06, 6.340143925100824e-07, 7.499705361299718e-08, 7.984207149504393e-09, 7.727280998524895e-10, 6.855404003938097e-11, 5.6140631812663005e-12], [0.0033117736108891323, 0.0035257233808207336, 0.0018767474499455038, 0.0006659968485780716, 0.00017535407006987513, 3.7882767504634575e-05, 6.7216832435911916e-06, 1.0222746632748885e-06, 1.3603955559032203e-07, 1.60920098417694e-08, 1.713159835472311e-09, 1.658031561080295e-10, 1.4709541693456472e-11, 1.2046014558310077e-12], [0.0005684819973344058, 0.0006052075126715787, 0.0003221527991313501, 0.00011432158812221314, 3.0426770028132376e-05, 6.408988841198882e-06, 1.15380951862227e-06, 1.7547840241617308e-07, 2.3351849300383884e-08, 2.76227151091948e-09, 2.9407219195786525e-10, 2.8460915637085282e-11, 2.5249641504102773e-12, 2.067756803638801e-13], [8.131890925724421e-05, 8.657233656564201e-05, 4.6082574931777835e-05, 1.635321240469413e-05, 4.352418832101135e-06, 9.267194345052809e-07, 1.6266746106512475e-07, 2.5101432146659337e-08, 3.3403817942359856e-09, 3.9513108135981644e-10, 4.206576462408801e-11, 4.071211800764878e-12, 3.6118528218621073e-13, 2.957837339961379e-14], [9.970560747185303e-06, 1.0614686653296573e-05, 5.650212440633275e-06, 2.0050772837696645e-06, 5.33652710778235e-07, 1.1362563150106427e-07, 2.016102712690496e-08, 3.033320370843872e-09, 4.095662362226625e-10, 4.844726135389115e-11, 5.1577088944279535e-12, 4.991737462411644e-13, 4.4285146344434875e-14, 3.626622288437877e-15], [1.069684433868612e-06, 1.1387890181231382e-06, 6.061789751897758e-07, 2.1511327331890003e-07, 5.7252547001673394e-08, 1.2190244098306237e-08, 2.1629612852558105e-09, 3.289563699196511e-10, 4.3306389860537116e-11, 5.197629566466609e-12, 5.533410866939212e-13, 5.3553496106103254e-14, 4.7511000531849086e-15, 3.890795621056822e-16], [1.0200917744627603e-07, 1.0859925352327067e-07, 5.780753340562382e-08, 2.051402018600585e-08, 5.459820711069928e-09, 1.1625080574840634e-09, 2.06268217589288e-10, 3.1370531017130064e-11, 4.17464430208149e-12, 4.885180736728631e-13, 5.276871132613731e-14, 5.107065143874895e-15, 4.530829776007382e-16, 3.7104107374935343e-17], [8.75518494839535e-09, 9.32079420358683e-09, 4.961471693498646e-09, 1.7606655132395978e-09, 4.686023484080323e-10, 9.977507222458588e-11, 1.7703469816930662e-11, 2.6924518740384488e-12, 3.582989675388523e-13, 4.2382897289773306e-14, 4.463692918056805e-15, 4.3832624669164343e-16, 3.888694493153121e-17, 3.1845499644751623e-18], [6.831227025536135e-10, 7.272543257315517e-10, 3.8711848714597837e-10, 1.373758053983336e-10, 3.656266595786025e-11, 7.784943137955434e-12, 1.381312013075694e-12, 2.1007837201951845e-13, 2.7956252263085564e-14, 3.306922641759683e-15, 3.520559025617492e-16, 3.370719493677733e-17, 3.0341511998041677e-18, 2.4847429163081253e-19], [4.8858884996355774e-11, 5.20153046168619e-11, 2.7687818854101323e-11, 9.825509607788438e-12, 2.615066201895205e-12, 5.568013477793641e-13, 9.879537678760319e-14, 1.5025404631341075e-14, 1.9995109358029388e-15, 2.3652054373482147e-16, 2.518004275257233e-17, 2.4369766748358284e-18, 2.1388178212864315e-19, 1.7771590365770396e-20], [3.225717115507432e-12, 3.4341073969137616e-12, 1.8279801345324513e-12, 6.486909087833227e-13, 1.7264953562218107e-13, 3.676063499204831e-14, 6.522579012201096e-15, 9.919936750573943e-16, 1.3200990257442214e-16, 1.56153454208266e-17, 1.6624140088796466e-18, 1.6089186993720072e-19, 1.4273827619043845e-20, 1.1563805092467273e-21]] |
| Legacy trial inputs | {"lambda_home": 0.8582742423353351, "lambda_away": 1.0646027763576993, "rho": -0.03320816174939849, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2846 |
| Legacy p draw | 0.3196 |
| Legacy p away | 0.3958 |
| Legacy p over 1 5 | 0.5774 |
| Legacy p under 3 5 | 0.8706 |
| Legacy p btts yes | 0.3812 |
| Legacy p over 2 5 | 0.3033 |
| Legacy goal margin distribution | {"-1": 0.23532990046489083, "-10": 8.231053561974536e-08, "-11": 7.911310764726001e-09, "-12": 6.96315414766259e-10, "-13": 5.3278293869367114e-11, "-2": 0.11177585540291211, "-3": 0.036970172074785645, "-4": 0.009421661944948137, "-5": 0.0019479788288845159, "-6": 0.00033839221282301515, "-7": 5.0648604413069155e-05, "-8": 6.656448594236807e-06, "-9": 7.795364912641778e-07, "0": 0.3195989841311341, "1": 0.18815143530324394, "10": 9.510775783889787e-09, "11": 7.369659873050078e-10, "12": 5.229299239326954e-11, "13": 3.225717115507432e-12, "2": 0.07237701040043766, "3": 0.019299346109629637, "4": 0.003965127208746881, "5": 0.0006609252206062528, "6": 9.256076539299549e-05, "7": 1.1168955090217189e-05, "8": 1.1833851867176167e-06, "9": 1.1172708829615225e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2840 |
| Legacy raw p draw | 0.3224 |
| Legacy raw p away | 0.3936 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.8583 |
| Legacy lambda away | 1.0646 |
| Legacy model home team | Lecce |
| Legacy model away team | Genoa |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021569260499678382, "mu": 8.985313160598633, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,357.9326 |
| Elo away rating | 1,431.0354 |
| Elo rating diff | -13.1028 |
| Elo home expectancy | 0.4812 |

</details>


---
