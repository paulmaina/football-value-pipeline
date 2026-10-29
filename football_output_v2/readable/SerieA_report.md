# Serie A — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,988 |
| Training data through | 2026-10-28 |
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
| Training sha256 | cafbcc085d84f313d3f23539eee0f6162cadaefb42132b7e90d9c6a39369a861 |
| Training as of utc | 2026-10-29T12:00:04.904189+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 88, 'bbs_added_results': 8, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 88, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 144, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-29T12:00:04.904189+00:00', 'observations': 433, 'observations_sha256': 'e34000de2095b37e0a7276d609840c3377204d1e954083e0d836093d3be431d0', 'eligible_training_matches': 187, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 185, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 24, 'retrospective_eligible_training_matches': 187, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '5842adce891b2d16a7b2ad65ab97aae96922630ae093cd0107ed7284867425be', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 127, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-21T00:00:00+00:00', 'audit_origin_utc': '2025-10-25T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 16, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-29', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1980, 'tune_start_date': '2025-10-30', 'audit_start_date': '2026-04-30', 'training_shot_matches': 1608, 'tuning_matches': 252, 'audit_matches': 120, 'audit_matchdays': 40, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8683019038207488, 'audit_candidate_poisson_score': 0.8653426316110677, 'audit_gain': 0.002959272209681063, 'audit_gain_lower95': -0.004128583142222661, 'audit_baseline_briers': [0.5674437979193624, 0.1666900652812552, 0.19159818005234183, 0.24300980886873508], 'audit_candidate_briers': [0.5693589383013008, 0.1644142895891482, 0.19095197450924978, 0.2430299604046859], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1803.938 |
| Base scoring parameter | 0.149 |
| Home-advantage parameter | 0.106 |
| Dixon-Coles low-score adjustment | -0.025 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1988, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-28'} |
| Training data health | {'training_end': '2026-10-28', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 2.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261029T120004904189Z_f80bd4c266cc6010d1d95eabae5541854f94d7640778e690a86d281c257600ea.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 2, 'ANCHORED_MAIN': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 6} |
| Legacy comparison status | {'AVAILABLE': 6} |
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

## 2026-10-29 — Fiorentina vs Atalanta BC

The model's most likely 1X2 outcome is **Fiorentina win** at **37.9%**. Expected goals are 1.24 for Fiorentina and 1.61 for Atalanta BC (2.85 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 64.0%; Under 3.5 goals: 57.3%; Double Chance 1X: 63.7%; Double Chance X2: 62.1%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 76.0%; BTTS Yes (both teams score): 66.5%; BTTS No (at least one team does not score): 33.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 37.9% | 2.64 |
| Draw | 25.8% | 3.87 |
| Atalanta BC win | 36.3% | 2.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.24 |
| Atalanta BC expected goals | 1.61 |
| Expected total goals | 2.85 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 64.0% |
| Under 2.5 | 36.0% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.0% |
| Under 4.5 | 76.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.22% |
| 2 | 2-1 | 9.05% |
| 3 | 2-2 | 7.59% |
| 4 | 1-2 | 6.94% |
| 5 | 1-0 | 6.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 37.9% | 41.7% | 2.35 | -11.0% |
| Draw | 25.8% | 26.1% | 3.71 | -4.2% |
| Atalanta BC win | 36.3% | 32.2% | 3.03 | +9.9% |

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
| Market best home last update utc | 2026-10-29T11:59:52Z |
| Market best draw last update utc | 2026-10-29T11:59:52Z |
| Market best away last update utc | 2026-10-29T11:59:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Fiorentina |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2358 |
| Dc lambda away | 1.6142 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T12:00:04.904189+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 66.5% |
| P btts no | 33.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.68 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.56 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.78 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.16 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.15824137124354898, "-10": 5.811164785309652e-06, "-11": 9.85332892430213e-07, "-12": 1.536206913467644e-07, "-13": 2.2161378774405623e-08, "-14": 2.972437756238584e-09, "-15": 3.6856839780741733e-10, "-16": 3.737185945101228e-11, "-2": 0.11012429706866685, "-3": 0.05799029207452142, "-4": 0.024475175455479923, "-5": 0.00857275578831771, "-6": 0.0025586402541300894, "-7": 0.0006641145614369126, "-8": 0.00015233353353154056, "-9": 3.1280430676360404e-05, "0": 0.25829228516029507, "1": 0.20548812160043564, "10": 6.840817337343888e-07, "11": 8.879894151437498e-08, "12": 1.0598747079178425e-08, "13": 1.1705274288763482e-09, "14": 1.201925619570797e-10, "15": 1.1409403068571496e-11, "16": 8.856651178020027e-13, "2": 0.1098722232937973, "3": 0.0442935066919911, "4": 0.014311679013443861, "5": 0.0038376488221354504, "6": 0.0008768675762443975, "7": 0.00017423997138048963, "8": 3.059710306821449e-05, "9": 4.8099163354512246e-06} |
| Raw goal margin distribution | {"-1": 0.2202357281646359, "-10": 2.2926288676308444e-06, "-11": 3.3149350294847643e-07, "-12": 4.403482885073278e-08, "-13": 5.407332385633771e-09, "-14": 6.132105944346775e-10, "-15": 5.824509190737974e-11, "-2": 0.13977801381410282, "-3": 0.06528870093316878, "-4": 0.024088799254593393, "-5": 0.007312126760079985, "-6": 0.0018809093863971422, "-7": 0.0004192088340904488, "-8": 8.235472354886448e-05, "-9": 1.445632319248092e-05, "0": 0.2511122161805771, "1": 0.16791748432658513, "10": 1.585381574577177e-07, "11": 1.754910917990352e-08, "12": 1.784663627968199e-09, "13": 1.6777340980982469e-10, "14": 1.4565644951455033e-11, "15": 1.0591547294998598e-12, "2": 0.08192168472789109, "3": 0.02929395718025513, "4": 0.008274374483590998, "5": 0.0019228426057459691, "6": 0.00037865866874816614, "7": 6.46086194285759e-05, "8": 9.71691835484775e-06, "9": 1.3058036972185265e-06} |
| Unadjusted home-win probability | 29.0% |
| Unadjusted draw probability | 25.1% |
| Unadjusted away-win probability | 45.9% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.1% |
| Raw p btts yes | 57.1% |
| P home draw | 63.7% |
| P draw away | 62.1% |
| P home away | 74.2% |
| Raw p home draw | 54.1% |
| Raw p draw away | 71.0% |
| Raw p home away | 74.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1793 |
| Totals anchor target over 2 5 | 0.6402 |
| Totals anchor reference over odds | 1.53 |
| Totals anchor reference under odds | 2.65 |
| Totals anchor reference last update utc | 2026-10-29T11:59:52Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5374 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.91, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.69, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:00:08Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.18, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:00:08Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.74, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.24, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.24, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.35 |
| Reference draw odds | 3.71 |
| Reference away odds | 3.03 |
| Market reference 1x2 last update utc | 2026-10-29T11:59:52Z |
| Market reference home last update utc | 2026-10-29T11:59:52Z |
| Market reference draw last update utc | 2026-10-29T11:59:52Z |
| Market reference away last update utc | 2026-10-29T11:59:52Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Market reference over 2 5 last update utc | 2026-10-29T11:59:53Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:59:53Z |
| Home probability edge | -3.8% |
| Draw probability edge | -0.3% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | -0.1273 |
| Raw ev home | -0.3190 |
| Raw edge prob draw | -0.0103 |
| Raw ev draw | -0.0684 |
| Raw edge prob away | 0.1376 |
| Raw ev away | 0.3911 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06148459257016101, 0.07469129652243664, 0.06225256034524412, 0.033142591486930946, 0.013233568599964059, 0.004227245487644197, 0.0011252699450028894, 0.00025674924780779595, 5.1258948552551334e-05, 9.096570392742133e-06, 1.4528747803469048e-06, 2.1095314310107688e-07, 2.8077294355079585e-08, 3.449549674526773e-09, 3.9353636349369543e-10, 4.190290281456773e-11], [0.08158517377727137, 0.12098587610473054, 0.07921768035078014, 0.04217463834174268, 0.0168399918242425, 0.005379257976657001, 0.0014319294550651993, 0.0003267187683581765, 6.522808024334237e-05, 1.1575575392629918e-05, 1.8488134351573505e-06, 2.6844227075152206e-07, 3.572894218326524e-08, 4.3896238476828545e-09, 5.007832236418795e-10, 5.332231706655946e-11], [0.05478724979058996, 0.08750442207188763, 0.059516435739161495, 0.026834053093859347, 0.01071462026657437, 0.0034226089381378644, 0.0009110800361232669, 0.00020787822069374447, 4.150204571471002e-05, 7.365080458090492e-06, 1.1763268122811568e-06, 1.707991918653371e-07, 2.273291175052562e-08, 2.792943911844003e-09, 3.1862854407502585e-10, 3.3926879838480075e-11], [0.023239305698912086, 0.03711706687793079, 0.029641088926449306, 0.01344032619578549, 0.004544859192137219, 0.0014517803997322757, 0.00038645611080264584, 8.817645596946144e-05, 1.7604072684444654e-05, 3.1240727891409155e-06, 4.989667942252483e-07, 7.244851033875861e-08, 9.64270131492517e-09, 1.1846931104471347e-09, 1.3515382079701716e-10, 1.4390887204418766e-11], [0.0073931251992719205, 0.011808060275705112, 0.009429725841002684, 0.0050202843007401575, 0.0017072818773196277, 0.0004618552032547257, 0.00012294336363592024, 2.8051594443324262e-05, 5.60038733770239e-06, 9.938619320644614e-07, 1.5873641096598258e-07, 2.3048059798975098e-08, 3.0676345930490982e-09, 3.768866678603296e-10, 4.299651337514293e-11, 4.578175966584444e-12], [0.0018815811770028315, 0.003005200554952002, 0.0023999045286660593, 0.0012776832785688192, 0.0005101685944695929, 0.00013879717458824365, 3.1289598460681176e-05, 7.1392477019967286e-06, 1.4253219192857122e-06, 2.5294200402507986e-07, 4.039907818793498e-08, 5.865827280790267e-09, 7.807257895175852e-10, 9.591922779545938e-11, 1.0942791859035018e-11, 1.1651648648639639e-12], [0.00039905854315393945, 0.0006373633888360009, 0.0005089880875846889, 0.0002709797663739355, 0.00010820002801910593, 3.4562716530443904e-05, 7.835983784777904e-06, 1.5141402465090862e-06, 3.0229197421157936e-07, 5.3645661883943444e-08, 8.568111481705774e-09, 1.2440645759400446e-09, 1.6558163951441774e-10, 2.0343202712879427e-11, 2.3208217804661484e-12, 2.4711609532968367e-13], [7.25443303341334e-05, 0.00011586545637431773, 9.252827835749089e-05, 4.9261057112900484e-05, 1.9669541498207172e-05, 6.283111007755865e-06, 1.6725302561230346e-06, 3.250220704064929e-07, 5.4953262399152994e-08, 9.752174670774503e-09, 1.5575857736461763e-09, 2.2615687122170876e-10, 3.010086955980192e-11, 3.698164199151277e-12, 4.2189915433997117e-13, 4.492291158283101e-14], [1.15392715171068e-05, 1.843015097663203e-05, 1.4718020306476634e-05, 7.835715218919104e-06, 3.1287376824542522e-06, 9.994237117728789e-07, 2.6604120069875377e-07, 6.070177068944332e-08, 1.0321629892954377e-08, 1.551230687360413e-09, 2.477575445317644e-10, 3.5973666452866143e-11, 4.78799797519309e-12, 5.882488764083536e-13, 6.710943325747404e-14, 7.145667644951199e-15], [1.6315514975581853e-06, 2.605861243629591e-06, 2.0809986173325164e-06, 1.10790121204049e-06, 4.4237598913478415e-07, 1.41309722301e-07, 3.761588578349526e-08, 8.582696466234663e-09, 1.7135006250699072e-09, 2.589874188357028e-10, 3.503073761743756e-11, 5.086360026005201e-12, 6.769808003174959e-13, 8.317321711497487e-14, 9.48868359403727e-15, 1.010334554472491e-15], [2.0761832813399283e-07, 3.3160127373316254e-07, 2.6481141075004257e-07, 1.4098273804150503e-07, 5.6293266506293535e-08, 1.7981956645022257e-08, 4.786699855528158e-09, 1.0921660112279852e-09, 2.1804652538764174e-10, 3.869520587313711e-11, 5.263735658685229e-12, 6.472499130228107e-13, 8.614721763369803e-14, 1.0583965206602894e-14, 1.2074547612716148e-15, 1.2856717754206246e-16], [2.401805901909755e-08, 3.836086647509722e-08, 3.0634367155775476e-08, 1.6309406560530112e-08, 6.512214068371437e-09, 2.080219505959336e-09, 5.537432107756084e-10, 1.2634581904251088e-10, 2.522443159396621e-11, 4.47640507834805e-12, 7.149569303765027e-13, 8.841462407478764e-14, 9.965829972977387e-15, 1.2243923899830438e-15, 1.3968284967787374e-16, 1.4873128426942905e-17], [2.5469567188203184e-09, 4.067916834196749e-09, 3.248572550853134e-09, 1.7295049773291444e-09, 6.905773427672278e-10, 2.2059355600348134e-10, 5.872081461972627e-11, 1.3398140642809963e-11, 2.6748845722958713e-12, 4.746932290154872e-13, 7.581646610334648e-14, 1.1008327792363736e-14, 1.2478920457901654e-15, 1.2983873599695042e-16, 1.4812444761175234e-17, 1.5771971559716425e-18], [2.493119616901318e-10, 3.981929957552019e-10, 3.1799048227291337e-10, 1.692947019729843e-10, 6.759800461148009e-11, 2.1593069005468935e-11, 5.747958485791342e-12, 1.311493321412379e-12, 2.618343354977127e-13, 4.646592509891141e-14, 7.42138716098543e-15, 1.0775635787456106e-15, 1.434208058813182e-16, 1.500740890009264e-17, 1.4499342032579862e-18, 1.5438586530418665e-19], [2.2661047627444053e-11, 3.619349180260539e-11, 2.8903536817927254e-11, 1.5387931162532724e-11, 6.144276398277467e-12, 1.9626878784251517e-12, 5.224569255484884e-13, 1.1920732731042915e-13, 2.379926060101547e-14, 4.223489858173771e-15, 6.745621300185267e-16, 9.79444364161845e-17, 1.3036140307148378e-17, 1.6016077968521758e-18, 1.5561987001620557e-19, 1.4032802208706917e-20], [1.922443690036177e-12, 3.070464838175833e-12, 2.4520235290472238e-12, 1.3054308720615274e-12, 5.212479840253091e-13, 1.665040817803753e-13, 4.432248836633677e-14, 1.0112920548142365e-14, 2.019003671945826e-15, 3.5829859065936523e-16, 5.722629119851275e-17, 8.30908909676393e-18, 1.105917347155337e-18, 1.3587195321201003e-19, 1.5500734708270383e-20, 1.4057171197080156e-21]] |
| Legacy trial inputs | {"lambda_home": 1.2725208394875616, "lambda_away": 1.5971676330962146, "rho": -0.032887856522608186, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3590 |
| Legacy p draw | 0.2573 |
| Legacy p away | 0.3837 |
| Legacy p over 1 5 | 0.7822 |
| Legacy p under 3 5 | 0.6789 |
| Legacy p btts yes | 0.5802 |
| Legacy p over 2 5 | 0.5442 |
| Legacy goal margin distribution | {"-1": 0.18578260464135646, "-10": 1.7452788176376396e-06, "-11": 2.496147611929497e-07, "-12": 3.2799937634041886e-08, "-13": 3.984259778007133e-09, "-14": 4.4685868056025487e-10, "-15": 4.190290281456773e-11, "-2": 0.11672399426171154, "-3": 0.05382118051638559, "-4": 0.019617945197196257, "-5": 0.005885692771861149, "-6": 0.001496779603451087, "-7": 0.00032986522486129006, "-8": 6.408646518736672e-05, "-9": 1.1126213797655562e-05, "0": 0.2572814812535723, "1": 0.20429743537229725, "10": 2.4940337264239625e-07, "11": 2.8419875514713774e-08, "12": 2.975358682265509e-09, "13": 2.879574770217844e-10, "14": 2.5731512465619884e-11, "15": 1.922443690036177e-12, "2": 0.10272648377361612, "3": 0.03773895796862562, "4": 0.010959849862093977, "5": 0.002619769484768489, "6": 0.0005308083545892521, "7": 9.320320134294863e-05, "8": 1.4426966281028582e-05, "9": 1.995586248439431e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3009 |
| Legacy raw p draw | 0.2532 |
| Legacy raw p away | 0.4459 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2725 |
| Legacy lambda away | 1.5972 |
| Legacy model home team | Fiorentina |
| Legacy model away team | Atalanta |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 95/100 |
| Market p home draw | 69.5% |
| Market home draw odds | 1.44 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-29T12:00:08Z |
| Market reference home draw last update utc | 2026-10-29T12:00:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.3% |
| Market draw away odds | 1.64 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-29T12:00:08Z |
| Market reference draw away last update utc | 2026-10-29T12:00:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.3% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-29T12:00:08Z |
| Market reference home away last update utc | 2026-10-29T12:00:19Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.65 |
| Market reference dc home away odds | 1.29 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:00:08Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.24, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:00:08Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.24, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:00:08Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.79, "price": 2.05, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:00:08Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.05, "price": 1.79, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 84.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-29T12:00:19Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.9% |
| Market under 3 5 odds | 1.69 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-29T11:59:52Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market reference under 3 5 last update utc | 2026-10-29T12:00:18Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.3% |
| Market btts yes odds | 1.44 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-29T12:00:08Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.62 |
| Market reference btts yes last update utc | 2026-10-29T12:00:19Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021256305988342366, "mu": 9.546548382688224, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,434.0364 |
| Elo away rating | 1,539.1317 |
| Elo rating diff | -45.0953 |
| Elo home expectancy | 0.4355 |

</details>


---

## 2026-10-29 — Frosinone vs Lecce

The model's most likely 1X2 outcome is **Frosinone win** at **56.1%**. Expected goals are 1.83 for Frosinone and 1.00 for Lecce (2.84 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 69.5%; Under 3.5 goals: 50.8%; Double Chance 1X: 79.0%; Double Chance X2: 43.9%; Double Chance 12 (either team wins): 77.1%; Under 4.5 goals: 70.4%; BTTS Yes (both teams score): 67.0%; BTTS No (at least one team does not score): 33.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 56.1% | 1.78 |
| Draw | 22.9% | 4.36 |
| Lecce win | 21.0% | 4.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.83 |
| Lecce expected goals | 1.00 |
| Expected total goals | 2.84 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 88.0% |
| Under 1.5 | 12.0% |
| Over 2.5 | 69.5% |
| Under 2.5 | 30.5% |
| Over 3.5 | 49.2% |
| Under 3.5 | 50.8% |
| Over 4.5 | 29.6% |
| Under 4.5 | 70.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.56% |
| 2 | 2-1 | 8.57% |
| 3 | 2-2 | 7.14% |
| 4 | 3-1 | 6.75% |
| 5 | 2-0 | 6.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 56.1% | 55.8% | 1.76 | -1.3% |
| Draw | 22.9% | 22.8% | 4.20 | -3.7% |
| Lecce win | 21.0% | 21.4% | 4.47 | -6.1% |

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
| Market best home last update utc | 2026-10-29T11:59:52Z |
| Market best draw last update utc | 2026-10-29T11:59:52Z |
| Market best away last update utc | 2026-10-29T11:59:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Frosinone |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8333 |
| Dc lambda away | 1.0040 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T12:00:04.904189+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 67.0% |
| P btts no | 33.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.46 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.30 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.27 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.97 |
| Fair Over 4.5 odds | 3.38 |
| Fair Under 4.5 odds | 1.42 |
| Goal margin distribution | {"-1": 0.12438995218997767, "-10": 1.3257096318814733e-07, "-11": 1.5258836926262796e-08, "-12": 1.6153738227248196e-09, "-13": 1.5827925353756855e-10, "-14": 1.443193486596083e-11, "-15": 1.2303022729915471e-12, "-16": 9.840555224579266e-14, "-17": 7.336849749567863e-15, "-18": 4.510798059542569e-16, "-2": 0.05781653574977305, "-3": 0.02039092119429941, "-4": 0.005791696025394761, "-5": 0.0013692479818048664, "-6": 0.0002763660359692673, "-7": 4.857323954394709e-05, "-8": 7.551389083866586e-06, "-9": 1.0516519399016277e-06, "0": 0.22938091460873558, "1": 0.19655983200598734, "10": 4.6902778836795837e-05, "11": 9.85738139214866e-06, "12": 1.9054744748267975e-06, "13": 3.409133860137742e-07, "14": 5.675898062723344e-08, "15": 8.835107120189512e-09, "16": 1.2903560491366605e-09, "17": 1.7566674357612348e-10, "18": 1.9720743135454748e-11, "2": 0.16553220467719315, "3": 0.10660001004600864, "4": 0.05528612172079108, "5": 0.023866154138036073, "6": 0.008795792331828915, "7": 0.0028227819598736032, "8": 0.0008013035704584586, "9": 0.0002037662361576043} |
| Raw goal margin distribution | {"-1": 0.12961778718374536, "-10": 1.984198305431973e-08, "-11": 1.7864345137025947e-09, "-12": 1.477412009160259e-10, "-13": 1.1296978176878138e-11, "-14": 8.02999749614855e-13, "-15": 5.3047546821357524e-14, "-16": 2.985345653735836e-15, "-2": 0.052365143941048936, "-3": 0.01535780378182566, "-4": 0.0035466041229996192, "-5": 0.0006725828804406153, "-6": 0.00010796267342710837, "-7": 1.5004044276937933e-05, "-8": 1.8369983544206494e-06, "-9": 2.0088847962488835e-07, "0": 0.2329142935005732, "1": 0.2389363583730918, "10": 8.174943048073939e-06, "11": 1.3439302461560393e-06, "12": 2.029463376614373e-07, "13": 2.8335563229157825e-08, "14": 3.6776884495059046e-09, "15": 4.436237583841287e-10, "16": 4.5586272337738504e-11, "2": 0.174591153348302, "3": 0.09349728781305383, "4": 0.03942507962783725, "5": 0.013651979878614436, "6": 0.004001413445014953, "7": 0.001015402200043861, "8": 0.0002270013794633594, "9": 4.532780899870179e-05} |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 20.2% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 53.5% |
| P home draw | 79.0% |
| P draw away | 43.9% |
| P home away | 77.1% |
| Raw p home draw | 79.8% |
| Raw p draw away | 43.5% |
| Raw p home away | 76.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2897 |
| Totals anchor target over 2 5 | 0.6946 |
| Totals anchor reference over odds | 1.41 |
| Totals anchor reference under odds | 3.06 |
| Totals anchor reference last update utc | 2026-10-29T11:59:52Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5402 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 8.8, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.1, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.88, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.28, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.83, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:58:26Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.93, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.93, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.76 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.47 |
| Market reference 1x2 last update utc | 2026-10-29T11:59:52Z |
| Market reference home last update utc | 2026-10-29T11:59:52Z |
| Market reference draw last update utc | 2026-10-29T11:59:52Z |
| Market reference away last update utc | 2026-10-29T11:59:52Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-29T11:59:53Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:59:53Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0070 |
| Raw ev home | -0.0049 |
| Raw edge prob draw | 0.0050 |
| Raw ev draw | -0.0218 |
| Raw edge prob away | -0.0120 |
| Raw ev away | -0.0985 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06792476078891324, 0.06275821613036123, 0.03340834617275413, 0.01119448619902666, 0.0028132907405574972, 0.0005656073642107647, 9.476200647563025e-05, 1.3608386977802408e-05, 1.7099645485249445e-06, 1.9099193996118444e-07, 1.9199303895184827e-08, 1.754539866182902e-09, 1.4697803518963772e-10, 1.1365263992479403e-11, 8.160597071903336e-13, 5.46891431409687e-14], [0.11272917226943538, 0.1133379976509725, 0.056700627177909184, 0.018999275963469037, 0.004774715533614352, 0.0009599485147022662, 0.00016083002648563556, 2.3096147068494024e-05, 2.902150913187865e-06, 3.2415141790396447e-07, 3.25850482573143e-08, 2.9778041183717226e-09, 2.4945104236934e-10, 1.9289119942777634e-11, 1.385016096667749e-12, 9.281838436062106e-14], [0.09893268365012031, 0.09945124694533558, 0.04680213891469662, 0.01612278047952921, 0.00405182231937045, 0.0008146120517409885, 0.00013648031727790723, 1.9599384198862923e-05, 2.4627644854340944e-06, 2.7507480616853516e-07, 2.7651663199044325e-08, 2.526963775033202e-09, 2.1168408755384323e-10, 1.636874200252045e-11, 1.175324287626763e-12, 7.876565603806407e-14], [0.055969499181917196, 0.05626286763060869, 0.028278886896330475, 0.00887210188259403, 0.0022922502212847076, 0.0004608530455389268, 7.7211440389592e-05, 1.1088021444599771e-05, 1.393267520572213e-06, 1.556189377543195e-07, 1.564346264244576e-08, 1.4295871871790994e-09, 1.1975670656089908e-10, 9.260340044540656e-12, 6.649199165308755e-13, 4.456034303867018e-14], [0.023747850986382442, 0.023872327179763904, 0.011998727912358913, 0.0040205400568532465, 0.000946040799047886, 0.00019553988533123885, 3.2760803788081576e-05, 4.704646009861771e-06, 5.911632218679088e-07, 6.602909439008694e-08, 6.637519098328243e-09, 6.065736515316084e-10, 5.0812754510888974e-11, 3.9291610372678114e-12, 2.821254312876664e-13, 1.8906947567011896e-14], [0.008060967987416, 0.008103220173124034, 0.004072846913461864, 0.0013647316849428619, 0.00034297125784379576, 6.456143666927217e-05, 1.1120323718098702e-05, 1.5969445361336748e-06, 2.0066438051794548e-07, 2.2412908705792752e-08, 2.25303876962034e-09, 2.058952951073389e-10, 1.7247875931998135e-11, 1.333714000352284e-12, 9.57646260855305e-14, 6.417772250837774e-15], [0.0022801784230008183, 0.002292130154148552, 0.0011520722656086588, 0.00038603698042842424, 9.701510576220019e-05, 1.9504723584990294e-05, 3.0596659527699354e-06, 4.517222348116912e-07, 5.676124647016693e-08, 6.339862769262535e-09, 6.373093649165352e-10, 5.824089737535786e-11, 4.878847627745538e-12, 3.772631141576128e-13, 2.7088611991494204e-14, 1.8153732694309603e-15], [0.0005528453706625029, 0.0005557431523315933, 0.00027932806147345064, 9.359739368707681e-05, 2.3521997912067003e-05, 4.729058055826427e-06, 7.923076297550908e-07, 1.0653228991215924e-07, 1.3762165288261683e-08, 1.5371445266154464e-09, 1.545201588261147e-10, 1.4120917105610617e-11, 1.1829110818517237e-12, 9.147010781255897e-14, 6.567825388620896e-15, 4.4015007681221205e-16], [0.00011728610826346475, 0.00011790087244998138, 5.92594294852091e-05, 1.9856680785814513e-05, 4.9901902775846114e-06, 1.0032693489957234e-06, 1.680880104504917e-07, 2.4138436675329725e-08, 2.8399102604599706e-09, 3.261051081049407e-10, 3.2781441319205864e-11, 2.995751615760776e-12, 2.5095450658446393e-13, 1.9405377230379023e-14, 1.3933637151781074e-15, 9.337780924041448e-17], [2.2117546660035647e-05, 2.2233477487492696e-05, 1.1175007987663667e-05, 3.7445275514397215e-06, 9.4103869538414e-07, 1.8919424446372182e-07, 3.169765344912029e-08, 4.5519713065049185e-09, 5.719788519185072e-10, 5.981676562581465e-11, 6.18184939969239e-12, 5.649320036659967e-13, 4.732442819621728e-14, 3.659421756789583e-15, 2.627573498783429e-16, 1.7608974186844287e-17], [3.753788831018047e-06, 3.773464604826418e-06, 1.8966217553607158e-06, 6.355210148796464e-07, 1.5971303682933368e-07, 3.2110037007136686e-08, 5.379724040631759e-09, 7.725603256145793e-10, 9.707622002171724e-11, 1.0842783613286168e-11, 1.020531125507051e-12, 9.588022931484784e-14, 8.03189941126091e-15, 6.210768639833871e-16, 4.45951633064006e-17, 2.9885941530621213e-18], [5.791753079565252e-07, 5.82211100023618e-07, 2.926314022145394e-07, 9.805508409644285e-08, 2.4642261846469982e-08, 4.954285232677863e-09, 8.300422501680784e-10, 1.1919899723860254e-10, 1.497797349753561e-11, 1.672942411261809e-12, 1.6817112679983465e-13, 1.4389450618778036e-14, 1.2392486696517915e-15, 9.582648362899391e-17, 6.88062610979406e-18, 4.611127628315177e-19], [8.191466846158895e-08, 8.23440305170461e-08, 4.138782155342371e-08, 1.386825300455706e-08, 3.485236130696324e-09, 7.007008529607691e-10, 1.1739560509152988e-10, 1.6858706173445703e-11, 2.1183840478385722e-12, 2.366097468093873e-13, 2.3784995505461613e-14, 2.1736060358823647e-15, 1.7048455861846622e-16, 1.3553054711541909e-17, 9.731495781139907e-19, 6.521669444786889e-20], [1.0694271639200938e-08, 1.0750326489191296e-08, 5.403337577501595e-09, 1.8105531961158215e-09, 4.5501083759988053e-10, 9.147916240295924e-11, 1.5326442915237897e-11, 2.2009682354857315e-12, 2.7656309754044606e-13, 3.0890302706268946e-14, 3.1052216611467416e-15, 2.837725381899427e-16, 2.3771662820448182e-17, 1.7210824394690257e-18, 1.2704838009330244e-19, 8.514287598726231e-21], [1.2964508629457814e-09, 1.3032463101809072e-09, 6.550386881385339e-10, 2.1949070798887859e-10, 5.516029636779681e-11, 1.1089884663499652e-11, 1.858002191613873e-12, 2.6682015049553536e-13, 3.3527338612848243e-14, 3.744786082803401e-15, 3.764414668012328e-16, 3.440132852695658e-17, 2.8818038120760633e-18, 2.228391545479517e-19, 1.4981280328841996e-20, 1.0321745956288385e-21], [1.4668904721043933e-10, 1.4745792917024187e-10, 7.411542064208267e-11, 2.4834634112762256e-11, 6.241201690939798e-12, 1.2547830862375386e-12, 2.1022668810097843e-13, 3.018980107260183e-14, 3.793505405554396e-15, 4.2370992853920226e-16, 4.2593083682402865e-17, 3.8923944197363755e-18, 3.2606639211942775e-19, 2.521349955951698e-20, 1.8104041473562213e-21, 1.1359775300137013e-22]] |
| Legacy trial inputs | {"lambda_home": 1.6971994628142018, "lambda_away": 1.005241577162196, "rho": -0.032887856522608186, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5453 |
| Legacy p draw | 0.2380 |
| Legacy p away | 0.2167 |
| Legacy p over 1 5 | 0.7566 |
| Legacy p under 3 5 | 0.7124 |
| Legacy p btts yes | 0.5188 |
| Legacy p over 2 5 | 0.5109 |
| Legacy goal margin distribution | {"-1": 0.13808100003491788, "-10": 2.239834098435847e-08, "-11": 2.0210434774188603e-09, "-12": 1.674870397630808e-10, "-13": 1.2829045745185217e-11, "-14": 9.088780915509547e-13, "-15": 5.46891431409687e-14, "-2": 0.05695471358120226, "-3": 0.016865937032588603, "-4": 0.003921421821797786, "-5": 0.0007474983839924747, "-6": 0.00012048338535343484, "-7": 1.6801880365253032e-05, "-8": 2.0632493908124056e-06, "-9": 2.2622773544112946e-07, "0": 0.23795077057189834, "1": 0.2448431391784419, "10": 4.379254720870658e-06, "11": 6.671484079607526e-07, "12": 9.334486827303155e-08, "13": 1.2071633370023927e-08, "14": 1.4439087921160232e-09, "15": 1.4668904721043933e-10, "2": 0.1686609277806038, "3": 0.08432526800826397, "4": 0.03310192570439695, "5": 0.010653256879737517, "6": 0.0028990903193216472, "7": 0.0006825821306747836, "8": 0.00014151784119389971, "9": 2.6197977231030116e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5322 |
| Legacy raw p draw | 0.2480 |
| Legacy raw p away | 0.2197 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6972 |
| Legacy lambda away | 1.0052 |
| Legacy model home team | Frosinone |
| Legacy model away team | Lecce |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 78.3% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-29T11:58:59Z |
| Market reference home draw last update utc | 2026-10-29T12:00:19Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.7% |
| Market draw away odds | 2.25 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-29T11:58:59Z |
| Market reference draw away last update utc | 2026-10-29T12:00:19Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.0% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-29T11:58:59Z |
| Market reference home away last update utc | 2026-10-29T12:00:19Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.10 |
| Market reference dc home away odds | 1.22 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:58:59Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.29, "price": 1.61, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:58:59Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.29, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:58:59Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.85, "price": 1.99, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:58:59Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.99, "price": 1.85, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:58:59Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.5, "price": 2.54, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:58:59Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.54, "price": 1.5, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 88.6% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-10-29T12:00:19Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 51.7% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-29T11:59:52Z |
| Market reference under 3 5 odds | 1.88 |
| Market reference under 3 5 opposite odds | 2.01 |
| Market reference under 3 5 last update utc | 2026-10-29T12:00:18Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.5% |
| Market btts yes odds | 1.44 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-29T11:58:59Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.80 |
| Market reference btts yes last update utc | 2026-10-29T12:00:19Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021256305988342366, "mu": 9.589939076787333, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,461.3882 |
| Elo away rating | 1,418.2291 |
| Elo rating diff | 103.1592 |
| Elo home expectancy | 0.6442 |

</details>


---

## 2026-10-31 — AC Milan vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **49.5%**. Expected goals are 1.25 for AC Milan and 1.81 for Inter Milan (3.06 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 58.6%; Under 3.5 goals: 63.5%; Double Chance 1X: 50.5%; Double Chance X2: 74.1%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 60.2%; BTTS No (at least one team does not score): 39.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 25.9% | 3.86 |
| Draw | 24.6% | 4.06 |
| Inter Milan win | 49.5% | 2.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.25 |
| Inter Milan expected goals | 1.81 |
| Expected total goals | 3.06 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 58.6% |
| Under 2.5 | 41.4% |
| Over 3.5 | 36.5% |
| Under 3.5 | 63.5% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.35% |
| 2 | 1-2 | 9.46% |
| 3 | 0-1 | 8.10% |
| 4 | 0-2 | 7.56% |
| 5 | 2-1 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 25.9% | 25.8% | 3.72 | -3.5% |
| Draw | 24.6% | 25.0% | 3.83 | -5.8% |
| Inter Milan win | 49.5% | 49.2% | 1.99 | -1.6% |

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
| Market best home last update utc | 2026-10-29T11:59:52Z |
| Market best draw last update utc | 2026-10-29T11:59:52Z |
| Market best away last update utc | 2026-10-29T11:59:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Milan |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2520 |
| Dc lambda away | 1.8063 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T12:00:04.904189+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.2% |
| P btts no | 39.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.32 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.31 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.74 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.18 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.21888680913058398, "-10": 5.788407210248198e-06, "-11": 9.347133540239851e-07, "-12": 1.3871005701635483e-07, "-13": 1.9038683782432806e-08, "-14": 2.429466743965204e-09, "-15": 2.8749661791448115e-10, "-16": 2.8437058042391852e-11, "-2": 0.15135105015465417, "-3": 0.07785596938748358, "-4": 0.031802101795260725, "-5": 0.01072042672222682, "-6": 0.003068374702645465, "-7": 0.0007619125469369576, "-8": 0.00016691237022034433, "-9": 3.269380697545816e-05, "0": 0.24602855030463197, "1": 0.1510854428052694, "10": 1.4830463185925925e-07, "11": 1.6598913929735842e-08, "12": 1.7073193486716247e-09, "13": 1.6242366982466615e-10, "14": 1.4365771124303984e-11, "15": 1.1783011749493707e-12, "16": 8.078185494280358e-14, "2": 0.07280083957246725, "3": 0.025956638691767692, "4": 0.007348825669581729, "5": 0.0017170375013993275, "6": 0.00034062905349596944, "7": 5.862515527092186e-05, "8": 8.9017007638829e-06, "9": 1.2085247452644505e-06} |
| Raw goal margin distribution | {"-1": 0.22187675177225236, "-10": 5.86747549953436e-06, "-11": 9.474813199239581e-07, "-12": 1.4060480396775302e-07, "-13": 1.9298747752063688e-08, "-14": 2.4626526917303946e-09, "-15": 2.914237545046314e-10, "-16": 2.882550160727484e-11, "-2": 0.1534184701171277, "-3": 0.0789194637282558, "-4": 0.03223651107113263, "-5": 0.010866865245045914, "-6": 0.0031102879837632087, "-7": 0.0007723200942092554, "-8": 0.0001691923541770113, "-9": 3.3140396735629955e-05, "0": 0.23605597814622997, "1": 0.1529590065116462, "10": 1.501437115917601e-07, "11": 1.6804751912049655e-08, "12": 1.7284912862684779e-09, "13": 1.6443783536695635e-10, "14": 1.4543916595455051e-11, "15": 1.1929129222863505e-12, "16": 8.178360566573527e-14, "2": 0.07370362019966858, "3": 0.026278518915894323, "4": 0.00743995617695142, "5": 0.0017383299507933837, "6": 0.0003448530887181456, "7": 5.9352147634692296e-05, "8": 9.012087993562823e-06, "9": 1.2235112857209267e-06} |
| Unadjusted home-win probability | 26.3% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 50.1% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 59.9% |
| P home draw | 50.5% |
| P draw away | 74.1% |
| P home away | 75.4% |
| Raw p home draw | 49.9% |
| Raw p draw away | 73.7% |
| Raw p home away | 76.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5863 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.66, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.56, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.72 |
| Reference draw odds | 3.83 |
| Reference away odds | 1.99 |
| Market reference 1x2 last update utc | 2026-10-29T11:59:52Z |
| Market reference home last update utc | 2026-10-29T11:59:52Z |
| Market reference draw last update utc | 2026-10-29T11:59:52Z |
| Market reference away last update utc | 2026-10-29T11:59:52Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-29T12:00:16Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:00:16Z |
| Home probability edge | +0.1% |
| Draw probability edge | -0.4% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.0046 |
| Raw ev home | -0.0234 |
| Raw edge prob draw | -0.0142 |
| Raw ev draw | -0.0959 |
| Raw edge prob away | 0.0097 |
| Raw ev away | -0.0022 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.05368522491428544, 0.08310018398014866, 0.0762898275771926, 0.04476784052098807, 0.01970275338692513, 0.006937095674185929, 0.002035387958548982, 0.0005118820822818955, 0.00011264209210245036, 2.2033270469297025e-05, 3.878820951039228e-06, 6.207658463671678e-07, 9.106832225738872e-08, 1.2332319010302862e-08, 1.5507346174089295e-09, 1.8199815689003656e-10, 2.002478096077788e-11], [0.05678592300091598, 0.11403079718459265, 0.09558121371821222, 0.05608827111595976, 0.02468498280989589, 0.008691277006061506, 0.002550075909775768, 0.0006413215530681868, 0.00014112586462483457, 2.7604817057767834e-05, 4.859657257985413e-06, 7.777387223814536e-07, 1.1409674197828105e-07, 1.5450788871848517e-08, 1.942868421570594e-09, 2.2801997700710293e-10, 2.5088441401127243e-11], [0.037758804149321264, 0.06647203864930695, 0.060874537179487154, 0.03513564782405069, 0.015463533556919583, 0.0054445188263140005, 0.001597456425519631, 0.00040174617227888265, 8.840616014124028e-05, 1.7292619492296877e-05, 3.044258675920957e-06, 4.872026415687869e-07, 7.147417569231785e-08, 9.678912642585586e-09, 1.217080492419552e-09, 1.4283966058440368e-10, 1.5716274079867506e-11], [0.015768953929839274, 0.027760267802396998, 0.024435116999186192, 0.014918317220064052, 0.006457930904995883, 0.0022737575640046155, 0.0006671349198276344, 0.00016777853602307078, 3.6920466571668974e-05, 7.221799689998176e-06, 1.2713531557109444e-06, 2.0346714315983704e-07, 2.98492764550558e-08, 4.042138806840751e-09, 5.082810922181973e-10, 5.965316110652909e-11, 6.5634812197465405e-12], [0.004939111161824155, 0.008694999628262865, 0.007653504452364761, 0.0044911736942052, 0.0020564896577779292, 0.000712180491719641, 0.00020895828243420566, 5.25511612040401e-05, 1.1564133509123932e-05, 2.261993510541747e-06, 3.982099630660974e-07, 6.372945487167566e-08, 9.349313541500322e-09, 1.2660683129228481e-09, 1.592024954279678e-10, 1.868440957911756e-11, 2.0557966937508697e-12], [0.0012376125481700678, 0.0021787403226409337, 0.001917768772028165, 0.0011253710916493771, 0.0004952865456431226, 0.00018143171083600523, 5.235950030513711e-05, 1.3167951559731182e-05, 2.8976705060268244e-06, 5.6679662813902e-07, 9.978103973568502e-08, 1.5968940656134984e-08, 2.3426943384411895e-09, 3.172437265686329e-10, 3.989199667433109e-11, 4.681826140905185e-12, 5.151290791626846e-13], [0.00025842787787858996, 0.0004549462906312089, 0.0004004523990564483, 0.00023499055780492643, 0.00010342158466446064, 3.6413460266390246e-05, 1.1115714145184968e-05, 2.7496212628265747e-06, 6.050672650104622e-07, 1.1835372064971905e-07, 2.0835440291503e-08, 3.334500326322653e-09, 4.891817938471238e-10, 6.624417564984274e-11, 8.329912346259195e-12, 9.776196887948598e-13, 1.0756493618168405e-13], [4.6253779848891646e-05, 8.142691780262135e-05, 7.167352554208316e-05, 4.205893581025996e-05, 1.851053859963528e-05, 6.517331599531406e-06, 1.9122265112933858e-06, 5.003431570526939e-07, 1.0829577791415017e-07, 2.1183112999136918e-08, 3.729155988157995e-09, 5.96813491121281e-10, 8.755443562989265e-11, 1.1856474394061424e-11, 1.4908992597363952e-12, 1.7497572720348388e-13, 1.9252121398238215e-14], [7.2437449352909175e-06, 1.275216480374246e-05, 1.1224698594062038e-05, 6.5867958090045025e-06, 2.8989116277343143e-06, 1.020670914246338e-06, 2.994713329713399e-07, 7.531439343602431e-08, 1.7243072939134166e-08, 3.3174600649393234e-09, 5.840183200244243e-10, 9.346619276838764e-11, 1.3711787484790543e-11, 1.8568271960252977e-12, 2.334878143370434e-13, 2.7402723450275028e-14, 3.0150499554348465e-15], [1.0083853972386484e-06, 1.7752001052143781e-06, 1.5625649787188115e-06, 9.169329908392364e-07, 4.03550950427716e-07, 1.4208529628064455e-07, 4.168872893200018e-08, 1.0484346870466273e-08, 2.307130502697943e-09, 4.695224051035529e-10, 8.129987332427048e-11, 1.3011217921817881e-11, 1.9087870146199652e-12, 2.584847266702245e-13, 3.25033121008405e-14, 3.814671336259117e-15, 4.1971830512602586e-16], [1.263375514465127e-07, 2.2240944309043631e-07, 1.9576903228467403e-07, 1.1487975651014001e-07, 5.05596759934879e-08, 1.7801436313739715e-08, 5.2230545489938505e-09, 1.3135520563445246e-09, 2.8905339107111034e-10, 5.65400679858175e-11, 1.0355784298694014e-11, 1.630136075037216e-12, 2.391461422590528e-13, 3.238476830710062e-14, 4.072241502075382e-15, 4.779286149084493e-16, 5.258523488351648e-17], [1.4389499156688023e-08, 2.5331823018148466e-08, 2.2297553599165513e-08, 1.3084487869966668e-08, 5.758607846525554e-09, 2.027534568238332e-09, 5.948915280339409e-10, 1.4960996149302124e-10, 3.292238514545286e-11, 6.439758023531504e-12, 1.1336795586521897e-12, 1.8876622916152153e-13, 2.7238086958007293e-14, 3.6885359175403314e-15, 4.638170915062573e-16, 5.4434752949076837e-17, 5.989313425398736e-18], [1.5023472961295663e-09, 2.6447894678571665e-09, 2.327994115378277e-09, 1.3660965373869908e-09, 6.012321091576781e-10, 2.1168638624828875e-10, 6.211013106851486e-11, 1.5620149018085948e-11, 3.4372882451866744e-12, 6.723481442288113e-13, 1.1836273111888432e-13, 1.8942751389867037e-14, 2.8912688883816053e-15, 3.851045753609789e-16, 4.842519852396923e-17, 5.683304402607818e-18, 6.253191116897321e-19], [1.4478810866670346e-10, 2.548905075804996e-10, 2.243594845354364e-10, 1.3165699729614093e-10, 5.794349960152336e-11, 2.0401189241888636e-11, 5.985838580479438e-12, 1.505385498577609e-12, 3.3126725441249076e-13, 6.479727851160054e-14, 1.1407159995215143e-14, 1.8255999486591947e-15, 2.678213136410738e-16, 3.7733618400910025e-17, 4.666958781207447e-18, 5.477261466444361e-19, 6.026487465844322e-20], [1.295718820659385e-11, 2.2810328204489308e-11, 2.00780857891582e-11, 1.1782075948018915e-11, 5.185403943730704e-12, 1.82571656664149e-12, 5.356768437393011e-13, 1.3471799174784604e-13, 2.964533622015146e-14, 5.798753369191335e-15, 1.0208346550128054e-15, 1.6337420484701072e-16, 2.396751500202882e-17, 3.245640564826129e-18, 4.2461864148222493e-19, 4.90163925276583e-20, 5.393145406669782e-21], [1.0822445704690441e-12, 1.9052246101791344e-12, 1.6770150270465426e-12, 9.840937339405488e-13, 4.331090337126898e-13, 1.5249233166634296e-13, 4.4742219254624205e-14, 1.1252272699057043e-14, 2.476116241613367e-15, 4.843388279335742e-16, 8.526485415809771e-17, 1.3645772781196197e-17, 2.0018782289031627e-18, 2.7109098231587206e-19, 3.408849303958206e-20, 4.162394251972436e-21, 4.504605660623318e-22], [8.47444646869125e-14, 1.491873871245082e-13, 1.3131758256580917e-13, 7.70588265907333e-14, 3.3914324187499074e-14, 1.1940813905236393e-14, 3.503510687971663e-15, 8.811019730775585e-16, 1.9389068896612827e-16, 3.792584025857343e-17, 6.6766095385482354e-18, 1.0685234568379756e-18, 1.5675578654393958e-19, 2.1227604928386158e-20, 2.6692775121716863e-21, 3.13273194516662e-22, 3.5861621507414144e-23]] |
| Legacy trial inputs | {"lambda_home": 1.2528697043062518, "lambda_away": 1.7604381321621339, "rho": -0.032887856522608186, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2635 |
| Legacy p draw | 0.2458 |
| Legacy p away | 0.4907 |
| Legacy p over 1 5 | 0.8064 |
| Legacy p under 3 5 | 0.6442 |
| Legacy p btts yes | 0.5960 |
| Legacy p over 2 5 | 0.5783 |
| Legacy goal margin distribution | {"-1": 0.22104237773689067, "-10": 4.732239979806346e-06, "-11": 7.450689816189109e-07, "-12": 1.0779790057945707e-07, "-13": 1.4424590573677608e-08, "-14": 1.7944708684959e-09, "-15": 2.070865982911638e-10, "-16": 2.002478096077788e-11, "-2": 0.15033814289572098, "-3": 0.07562004808702012, "-4": 0.030171417730894785, "-5": 0.009928203421307104, "-6": 0.0027727521516277527, "-7": 0.0006716380594668453, "-8": 0.0001435043100444702, "-9": 2.741128660248769e-05, "0": 0.24575843164748828, "1": 0.152717942255252, "10": 1.5413436697712167e-07, "11": 1.7270875234876263e-08, "12": 1.7783338975573522e-09, "13": 1.6935251072483004e-10, "14": 1.4993730399338795e-11, "15": 1.2314319575935524e-12, "16": 8.47444646869125e-14, "2": 0.0744081966632896, "3": 0.026636287133336406, "4": 0.007563409192423444, "5": 0.0017712411233879353, "6": 0.0003520490781223272, "7": 6.0689365805166446e-05, "8": 9.228420741081344e-06, "9": 1.2545183053051265e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2691 |
| Legacy raw p draw | 0.2412 |
| Legacy raw p away | 0.4897 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2529 |
| Legacy lambda away | 1.7604 |
| Legacy model home team | Milan |
| Legacy model away team | Inter |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021256305988342366, "mu": 8.249678047262647, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,536.0001 |
| Elo away rating | 1,691.0319 |
| Elo rating diff | -95.0318 |
| Elo home expectancy | 0.3665 |

</details>


---

## 2026-10-31 — Bologna vs Monza

The model's most likely 1X2 outcome is **Bologna win** at **58.2%**. Expected goals are 2.01 for Bologna and 0.98 for Monza (2.99 combined). The most likely exact score is 1-0 at 11.1%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 52.4%; Under 3.5 goals: 69.8%; Double Chance 1X: 81.3%; Double Chance X2: 41.8%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 58.2% | 1.72 |
| Draw | 23.1% | 4.33 |
| Monza win | 18.7% | 5.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 2.01 |
| Monza expected goals | 0.98 |
| Expected total goals | 2.99 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 76.7% |
| Under 1.5 | 23.3% |
| Over 2.5 | 52.4% |
| Under 2.5 | 47.6% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.06% |
| 2 | 1-1 | 10.99% |
| 3 | 2-0 | 10.57% |
| 4 | 2-1 | 9.66% |
| 5 | 3-0 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 58.2% | 57.1% | 1.72 | +0.1% |
| Draw | 23.1% | 23.7% | 4.02 | -7.2% |
| Monza win | 18.7% | 19.2% | 4.93 | -7.7% |
| Over 2.5 | 52.4% | 52.4% | 1.86 | -2.5% |
| Under 2.5 | 47.6% | 47.6% | 2.04 | -2.9% |

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
| Market best home last update utc | 2026-10-29T11:59:52Z |
| Market best draw last update utc | 2026-10-29T11:59:52Z |
| Market best away last update utc | 2026-10-29T11:59:52Z |
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
| Dc lambda home | 2.0074 |
| Dc lambda away | 0.9835 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T12:00:04.904189+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.27 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.29 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.74 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.1247871980821016, "-10": 8.59216368704451e-09, "-11": 7.052015238977595e-10, "-12": 5.315850771156792e-11, "-13": 3.704492751408991e-12, "-14": 2.3996875848316124e-13, "-15": 1.445590343086033e-14, "-16": 7.4650970084046e-16, "-2": 0.04662666702642371, "-3": 0.012559044788123211, "-4": 0.0026560408671446817, "-5": 0.00046052009088703956, "-6": 6.751711894863498e-05, "-7": 8.564339803552807e-06, "-8": 9.566158526918002e-07, "-9": 9.540737808472558e-08, "0": 0.2307238954904054, "1": 0.2389748236142266, "10": 9.999854196177045e-06, "11": 1.675177847561298e-06, "12": 2.5773714496288815e-07, "13": 3.6659753078766874e-08, "14": 4.8469891126622965e-09, "15": 5.959627718647135e-10, "16": 6.28153671097015e-11, "2": 0.18016609693697938, "3": 0.09904940263258395, "4": 0.04275496526199285, "5": 0.015130627518578042, "6": 0.004527712203849938, "7": 0.0011722368122096755, "8": 0.00026724869447852686, "9": 5.440220884003379e-05} |
| Raw goal margin distribution | {"-1": 0.1146434320787302, "-10": 1.4011060438693014e-08, "-11": 1.234496530946217e-09, "-12": 9.992737429652584e-11, "-13": 7.479598800379093e-12, "-14": 5.205900314009526e-13, "-15": 3.3849481042699685e-14, "-16": 2.054166404917954e-15, "-17": 1.0647545819932386e-16, "-2": 0.044801403540340554, "-3": 0.01276576041510397, "-4": 0.0028720919597693038, "-5": 0.0005314906926977875, "-6": 8.33340241185293e-05, "-7": 1.1319924182341633e-05, "-8": 1.355282201365391e-06, "-9": 1.4497904642820461e-07, "0": 0.21560148847523566, "1": 0.2366150780636913, "10": 1.7580715303384522e-05, "11": 3.1616366842202404e-06, "12": 5.223518264786353e-07, "13": 7.980194902683873e-08, "14": 1.1336724592168028e-08, "15": 1.5045281462544354e-09, "16": 1.863547546176093e-10, "17": 1.9715642139752632e-11, "2": 0.18664000041279122, "3": 0.10854663129706131, "4": 0.049845339124373333, "5": 0.018826883318898813, "6": 0.006025064143280274, "7": 0.0016704727379548876, "8": 0.0004082086118203646, "9": 8.912801209547335e-05} |
| Unadjusted home-win probability | 60.9% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 17.6% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 64.9% |
| Raw p btts yes | 54.4% |
| P home draw | 81.3% |
| P draw away | 41.8% |
| P home away | 76.9% |
| Raw p home draw | 82.4% |
| Raw p draw away | 39.1% |
| Raw p home away | 78.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9297 |
| Totals anchor target over 2 5 | 0.5240 |
| Totals anchor reference over odds | 1.86 |
| Totals anchor reference under odds | 2.04 |
| Totals anchor reference last update utc | 2026-10-29T11:59:52Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5680 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.72 |
| Reference draw odds | 4.02 |
| Reference away odds | 4.93 |
| Market reference 1x2 last update utc | 2026-10-29T11:59:52Z |
| Market reference home last update utc | 2026-10-29T11:59:52Z |
| Market reference draw last update utc | 2026-10-29T11:59:52Z |
| Market reference away last update utc | 2026-10-29T11:59:52Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-10-29T11:59:52Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:59:52Z |
| Market best over 2 5 last update utc | 2026-10-29T11:59:52Z |
| Market best under 2 5 last update utc | 2026-10-29T11:59:52Z |
| Home probability edge | +1.1% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0380 |
| Raw ev home | 0.0469 |
| Raw edge prob draw | -0.0216 |
| Raw ev draw | -0.1333 |
| Raw edge prob away | -0.0164 |
| Raw ev away | -0.1337 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06253781977841097, 0.052996263269173484, 0.026745632588533515, 0.008433696800135825, 0.001994547375571755, 0.0003773642166824028, 5.949710436246302e-05, 8.040520319688327e-06, 9.507810798704232e-07, 9.993655754685277e-08, 9.453894457080322e-09, 8.130259891378177e-10, 6.409284450761652e-11, 4.663935741625158e-12, 3.151453377613175e-13, 1.9874947566540856e-14, 1.1750933620186605e-15], [0.10426154529090913, 0.11008066759649325, 0.05104241185690957, 0.016095197005487484, 0.00380647226327705, 0.0007201766383428584, 0.0001135466022390642, 1.5344843624201025e-05, 1.8145078193181115e-06, 1.9072283719530054e-07, 1.8042182136941814e-08, 1.5516106134552712e-09, 1.2231729257513153e-10, 8.900837481041806e-12, 6.014356950261254e-13, 3.793012769347569e-14, 2.242594156482643e-15], [0.10268303706256679, 0.0971370856422448, 0.048101937435904296, 0.015358351905731371, 0.003632210312112551, 0.0006872066394828976, 0.00010834838954087319, 1.4642350027685159e-05, 1.731438864357333e-06, 1.8199146298776354e-07, 1.7216203213416968e-08, 1.4805772066032581e-09, 1.167175538693119e-10, 8.493353280668542e-12, 5.739017080517925e-13, 3.6193669996528435e-14, 2.1399272233359067e-15], [0.06532144205995047, 0.061793405154018995, 0.02922795945797004, 0.009649054000545313, 0.0023106174324357648, 0.00043716401431371187, 6.892543551639056e-05, 9.314677928469923e-06, 1.101448561455675e-06, 1.157732099189592e-07, 1.0952025308837685e-08, 9.418638266171326e-10, 7.424944908678395e-11, 5.40301592248222e-12, 3.6508549262883154e-13, 2.3024472057391832e-14, 1.361306951278374e-15], [0.031165499055541872, 0.02948223813244695, 0.013944945398584062, 0.004397257795148516, 0.0010887531675121001, 0.00020857522806533725, 3.2884999591977956e-05, 4.444123966460796e-06, 5.255118842947483e-07, 5.523653107772665e-08, 5.225318420031071e-09, 4.493724460636558e-10, 3.54251385519768e-11, 2.577831755071407e-12, 1.7418586021529297e-13, 1.0985200870189418e-14, 6.494928643098749e-16], [0.011895491596643652, 0.011253011393456476, 0.005322615900001577, 0.001678379770439248, 0.00039693245390187763, 7.862381267722317e-05, 1.2551804019080618e-05, 1.6962680175043292e-06, 2.0058148892221743e-07, 2.1083111491070557e-08, 1.994440430570098e-09, 1.7151999223201526e-10, 1.3521344137758757e-11, 9.839269997045108e-13, 6.648462239454222e-14, 4.1929174439304915e-15, 2.4790351971290773e-16], [0.0037836369440033472, 0.0035792812170609097, 0.001692981411854204, 0.0005338476055326352, 0.00012625357133460555, 2.3886913208256998e-05, 3.942904666065569e-06, 5.395373773179388e-07, 6.379959378756854e-08, 6.705972500931666e-09, 6.34378027541809e-10, 5.455591086519944e-11, 4.3007770462081646e-12, 3.1296079830233864e-13, 2.1146975848486905e-14, 1.3336546215952687e-15, 7.885146301972698e-17], [0.0010315486867598241, 0.0009758343344371413, 0.0004615645681530939, 0.00014554509445993482, 3.4421036594264445e-05, 6.512388560370711e-06, 1.0267753133344581e-06, 1.452729895110672e-07, 1.7393948775048838e-08, 1.8282771918027429e-09, 1.7295312179916744e-10, 1.48738050296225e-11, 1.1725387450543144e-12, 8.532380491942832e-14, 5.765388034922697e-15, 3.635998098808479e-16, 2.1497602526585917e-17], [0.00024608098511858797, 0.00023279005384138884, 0.00011010848550805669, 3.472049422735365e-05, 8.211306652452478e-06, 1.5535621468772963e-06, 2.449422735386794e-07, 3.3101834932003025e-08, 4.097977570526294e-09, 4.361444672493835e-10, 4.125881321739653e-11, 3.548218946066586e-12, 2.797148531873992e-13, 2.0354411030846273e-14, 1.3753615175267306e-15, 8.673851322079466e-17, 5.128358239732622e-18], [5.218117575312522e-05, 4.9362849824512654e-05, 2.3348371396666473e-05, 7.362438876127764e-06, 1.741197660550424e-06, 3.2943097732862285e-07, 5.193971333759281e-08, 7.01920412706978e-09, 8.30011767201781e-10, 9.133752419875879e-11, 8.748881522986515e-12, 7.523955430609325e-13, 5.931319686442844e-14, 4.316128281265206e-15, 2.9164374905099595e-16, 1.839279699224992e-17, 1.087462172274367e-18], [9.958459779002126e-06, 9.42059942995612e-06, 4.455894565483819e-06, 1.4050766462250284e-06, 3.322969752908546e-07, 6.28698968609953e-08, 9.912378146717782e-09, 1.3395723835495152e-09, 1.5840269370094382e-10, 1.6649700177856168e-11, 1.6489743973407756e-12, 1.435901097537843e-13, 1.1319562597304436e-14, 8.237068113096102e-16, 5.565843434541214e-17, 3.5101533537159144e-18, 2.0753553647422298e-19], [1.7277376674752608e-06, 1.6344218731144085e-06, 7.730730508464367e-07, 2.437730232632468e-07, 5.765168647953655e-08, 1.0907579220841182e-08, 1.7197427592622175e-09, 2.324083961505972e-10, 2.748199085100793e-11, 2.8886308513397576e-12, 2.7326147572402717e-13, 2.4603291920359352e-14, 1.963881474918874e-15, 1.4290857385961705e-16, 9.656430378323346e-18, 6.089921837729503e-19, 3.6006267200300997e-20], [2.747735146166662e-07, 2.599328884796867e-07, 1.2294690521328564e-07, 3.87688314214124e-08, 9.168727877947492e-09, 1.7347042522085686e-09, 2.7350203164208616e-10, 3.6961439829022244e-11, 4.370642231716374e-12, 4.593980130169982e-13, 4.3458574474300445e-14, 3.7373963353298995e-15, 3.0845754997792613e-16, 2.272769289428291e-17, 1.5357258012325199e-18, 9.685204291106209e-20, 5.726314111858744e-21], [4.033757906802014e-08, 3.815893047790953e-08, 1.8048975779663735e-08, 5.6913811544670344e-09, 1.3459968521559786e-09, 2.5465980602502245e-10, 4.015092153993809e-11, 5.426050628100171e-12, 6.416234361082551e-13, 6.744101118922226e-14, 6.37984955167949e-15, 5.4866103232409e-16, 4.3252302757784686e-17, 3.2951362538636977e-18, 2.2544917045748616e-19, 1.4218171443032094e-20, 8.406401489520102e-22], [5.4987010289972655e-09, 5.20171401289341e-09, 2.460383691461206e-09, 7.758324652481323e-10, 1.8348236178221462e-10, 3.471448137908205e-11, 5.4732564196417025e-12, 7.396633824209842e-13, 8.746423384526605e-14, 9.193361778044705e-15, 8.696824674458483e-16, 7.479187032825699e-17, 5.896027654006783e-18, 4.290446822946786e-19, 3.035162747941476e-20, 1.9381796268046947e-21, 1.1459361118980787e-22], [6.995957481307781e-10, 6.618103052378786e-10, 3.1303283452573115e-10, 9.870860246577029e-11, 2.3344327957259155e-11, 4.416698315347334e-12, 6.963584489169953e-13, 9.410683626203887e-14, 1.1128011104619499e-14, 1.1696647584640459e-15, 1.1064907025140646e-16, 9.515715475430903e-18, 7.5014732676907e-19, 5.45870440870676e-20, 3.6884840184818846e-21, 2.435365460641156e-22, 1.4579662129032083e-23], [8.344599391888974e-11, 7.893904280278026e-11, 3.733775694898022e-11, 1.1773709979096425e-11, 2.784451812302709e-12, 5.268124938563071e-13, 8.305985713742883e-14, 1.1224823060216892e-14, 1.327320741223018e-15, 1.395146248139932e-16, 1.3197938478041843e-17, 1.1350102367235331e-18, 8.947565709925061e-20, 6.5110031916433435e-21, 4.399529525422802e-22, 2.774606131138503e-23, 1.717468792259839e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9084391325555206, "lambda_away": 0.945989604719787, "rho": -0.032887856522608186, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-29T11:59:52Z", "over": 1.86, "under": 2.04, "bookmaker": "pinnacle", "event_id": "04aa939b89001eedf55668e66c74836e", "kickoff_utc": "2026-10-31T14:00:00Z", "home_team": "Bologna", "away_team": "Monza"}} |
| Legacy p home | 0.5832 |
| Legacy p draw | 0.2315 |
| Legacy p away | 0.1853 |
| Legacy p over 1 5 | 0.7802 |
| Legacy p under 3 5 | 0.6812 |
| Legacy p btts yes | 0.5264 |
| Legacy p over 2 5 | 0.5407 |
| Legacy goal margin distribution | {"-1": 0.12192932887269962, "-10": 1.112780409795651e-08, "-11": 9.442129535906367e-10, "-12": 7.359125766163181e-11, "-13": 5.302926413599091e-12, "-14": 3.552153926781291e-13, "-15": 2.21175417230235e-14, "-16": 1.1750933620186605e-15, "-2": 0.046944850857950395, "-3": 0.013000952726401534, "-4": 0.0028329343259156617, "-5": 0.0005067119042312152, "-6": 7.669456128684741e-05, "-7": 1.0048434839907252e-05, "-8": 1.1596984146870134e-06, "-9": 1.195362120110143e-07, "0": 0.23154094816018772, "1": 0.23544572827746937, "10": 1.1721707920604241e-05, "11": 2.0065192353403105e-06, "12": 3.15494321840315e-07, "13": 4.586409962541838e-08, "14": 6.197849091184124e-09, "15": 7.785347909335584e-10, "16": 8.344599391888974e-11, "2": 0.18023278546831706, "3": 0.10069617160390634, "4": 0.04426558784216776, "5": 0.01597286370099755, "6": 0.004877285686395914, "7": 0.0012891516159366887, "8": 0.00030015293148822226, "9": 6.241499848426601e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5956 |
| Legacy raw p draw | 0.2259 |
| Legacy raw p away | 0.1785 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9084 |
| Legacy lambda away | 0.9460 |
| Legacy model home team | Bologna |
| Legacy model away team | Monza |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021256305988342366, "mu": 9.017072147987378, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,462.4031 |
| Elo away rating | 1,358.1496 |
| Elo rating diff | 164.2535 |
| Elo home expectancy | 0.7202 |

</details>


---

## 2026-10-31 — Udinese vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **61.8%**. Expected goals are 0.86 for Udinese and 1.74 for AS Roma (2.60 combined). The most likely exact score is 0-1 at 13.5%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 49.3%; Under 3.5 goals: 73.1%; Double Chance 1X: 38.2%; Double Chance X2: 83.4%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 47.2%; BTTS No (at least one team does not score): 52.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 16.6% | 6.01 |
| Draw | 21.6% | 4.64 |
| AS Roma win | 61.8% | 1.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 0.86 |
| AS Roma expected goals | 1.74 |
| Expected total goals | 2.60 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 74.0% |
| Under 1.5 | 26.0% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 26.9% |
| Under 3.5 | 73.1% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.46% |
| 2 | 0-2 | 11.96% |
| 3 | 1-2 | 10.34% |
| 4 | 1-1 | 10.24% |
| 5 | 0-3 | 6.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 16.6% | 16.0% | 5.86 | -2.4% |
| Draw | 21.6% | 20.5% | 4.61 | -0.5% |
| AS Roma win | 61.8% | 63.5% | 1.55 | -4.2% |

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
| Market best home last update utc | 2026-10-29T11:59:52Z |
| Market best draw last update utc | 2026-10-29T11:59:52Z |
| Market best away last update utc | 2026-10-29T11:59:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Udinese |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8648 |
| Dc lambda away | 1.7388 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T12:00:04.904189+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 47.2% |
| P btts no | 52.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.51 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.85 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.72 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.87 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.2674105047327473, "-10": 6.309688338023546e-06, "-11": 9.862521161461932e-07, "-12": 1.41553306266218e-07, "-13": 1.8779010363962158e-08, "-14": 2.315563107986986e-09, "-15": 2.657513658910321e-10, "-16": 2.6399234446153574e-11, "-2": 0.1920229754704723, "-3": 0.09964469231004099, "-4": 0.040416798273562, "-5": 0.013405920671475618, "-6": 0.0037540430385174075, "-7": 0.0009085898809005194, "-8": 0.00019350450259433052, "-9": 3.677844643948849e-05, "0": 0.2157307553313202, "1": 0.11271366068077136, "10": 5.009868042361746e-09, "11": 3.894727236650101e-10, "12": 2.7802243210036977e-11, "13": 1.8344388654101847e-12, "14": 1.1250138885756399e-13, "15": 6.421662672539869e-15, "16": 3.1727367343144367e-16, "2": 0.04071981598047155, "3": 0.010509389859344478, "4": 0.0021200981164674697, "5": 0.0003497529767916259, "6": 4.871186332936693e-05, "7": 5.863731986783629e-06, "8": 6.211092711792211e-07, "9": 5.871391477399494e-08} |
| Raw goal margin distribution | {"-1": 0.2501364136825606, "-10": 5.9020972788830304e-06, "-11": 9.22542543966988e-07, "-12": 1.3240929487690712e-07, "-13": 1.756593036479129e-08, "-14": 2.1659831653448813e-09, "-15": 2.485844513163744e-10, "-16": 2.4693905854317455e-11, "-2": 0.17961874189214017, "-3": 0.09320787903170047, "-4": 0.037805967954714616, "-5": 0.012539929656941283, "-6": 0.003511540668169322, "-7": 0.0008498971068614455, "-8": 0.00018100456584062595, "-9": 3.440264511068476e-05, "0": 0.24046452815917574, "1": 0.1229883117699186, "10": 5.46655311342623e-09, "11": 4.2497592993325e-10, "12": 3.0336615235161664e-11, "13": 2.0016610031051257e-12, "14": 1.2275668986166975e-13, "15": 7.007042856042365e-15, "16": 3.4619542324057085e-16, "2": 0.04443171655300793, "3": 0.011467395422400491, "4": 0.0023133601247271097, "5": 0.00038163544589270813, "6": 5.315229580745835e-05, "7": 6.39825282374862e-06, "8": 6.777277947109453e-07, "9": 6.406610531360751e-08} |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 57.8% |
| Raw p over 1 5 | 73.6% |
| Raw p under 3 5 | 73.5% |
| Raw p btts yes | 48.0% |
| P home draw | 38.2% |
| P draw away | 83.4% |
| P home away | 78.4% |
| Raw p home draw | 42.2% |
| Raw p draw away | 81.8% |
| Raw p home away | 76.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4931 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.61, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -1.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.52, "price": 1.61, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.86 |
| Reference draw odds | 4.61 |
| Reference away odds | 1.55 |
| Market reference 1x2 last update utc | 2026-10-29T11:59:52Z |
| Market reference home last update utc | 2026-10-29T11:59:52Z |
| Market reference draw last update utc | 2026-10-29T11:59:52Z |
| Market reference away last update utc | 2026-10-29T11:59:52Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-29T12:00:16Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:00:16Z |
| Home probability edge | +0.7% |
| Draw probability edge | +1.1% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | 0.0217 |
| Raw ev home | 0.0644 |
| Raw edge prob draw | 0.0353 |
| Raw ev draw | 0.1085 |
| Raw edge prob away | -0.0570 |
| Raw ev away | -0.1043 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.0729246377419152, 0.13317370021689223, 0.11449711256180242, 0.0636767961261571, 0.02656006518965843, 0.008862720561270536, 0.002464471101830203, 0.0005873995561940785, 0.00012250436151012962, 2.270999118932651e-05, 3.789002482160421e-06, 5.746985861113477e-07, 7.990368464979875e-08, 1.025489878840854e-08, 1.2221127268753337e-09, 1.359339483961523e-10], [0.05881860587255472, 0.10816380376264302, 0.10343122166090228, 0.057522575612774546, 0.023993094048347673, 0.008006158359640808, 0.0022262854591437666, 0.000530628697447992, 0.0001106645878335332, 2.0515121124582806e-05, 3.4228038317953725e-06, 5.191552478339126e-07, 7.218117150399928e-08, 9.263785662031238e-09, 1.1039982539282168e-09, 1.227962350597704e-10], [0.02810934963178415, 0.04689847505392353, 0.03945788770357513, 0.0259815734021216, 0.01083710747511648, 0.0036161904934559628, 0.0010055599641469145, 0.0002396723078748142, 4.998455095557205e-05, 9.266190181397097e-06, 1.545998732662887e-06, 2.3449002474252789e-07, 3.2602511026397825e-08, 4.1842307058680205e-09, 4.986496408530084e-10, 5.546412622735678e-11], [0.008464214533327326, 0.014121947300177108, 0.0117807384704002, 0.006607792045772142, 0.003263241725322301, 0.0010888979122939358, 0.0003027916111243087, 7.216950438640732e-05, 1.5051218480046335e-05, 2.7902111798869858e-06, 4.655271328908461e-07, 7.060902871625818e-08, 9.817183651256379e-09, 1.2599447093345865e-09, 1.501520879150483e-10, 1.670121398899463e-11], [0.0019115417629188202, 0.00318927313712776, 0.002660539084344533, 0.0014796408491789179, 0.0006224456381726203, 0.00024591458861413515, 6.838186908502924e-05, 1.6298620634032982e-05, 3.399137934670715e-06, 6.301358710505537e-07, 1.0513374310030603e-07, 1.5946205840933898e-08, 2.2170936794820874e-09, 2.8454346488721466e-10, 3.391005576582938e-11, 3.7717697142132046e-12], [0.0003453591018512511, 0.0005762073984273926, 0.00048068078157306737, 0.0002673273713646585, 0.0001115042345465734, 3.7525497877302236e-05, 1.2354582750028292e-05, 2.9446790505842308e-06, 6.141237648890694e-07, 1.1384692853269198e-07, 1.8994560200421754e-08, 2.881008112922921e-09, 4.00563302732579e-10, 5.140859455826851e-11, 6.126544881305856e-12, 6.814473144972779e-13], [5.1996818983689325e-05, 8.675303946671749e-05, 7.237067578186534e-05, 4.024846272683603e-05, 1.6787933106596402e-05, 5.601897392292497e-06, 1.5710463789272353e-06, 4.4334706320911676e-07, 9.246167848291517e-08, 1.714064607833343e-08, 2.859796377515225e-09, 4.337608493165325e-10, 6.030829195480551e-11, 7.740011400086055e-12, 9.224046607751366e-13, 1.0259782489849503e-13], [6.710206035059657e-06, 1.1195507347707994e-05, 9.339458737757619e-06, 5.194076921824923e-06, 2.1664881092706434e-06, 7.229266409804316e-07, 2.0102538527786348e-07, 4.832345412840745e-08, 1.1932209029218217e-08, 2.212005830505399e-09, 3.6905763249601843e-10, 5.5976975625555495e-11, 7.782804266665206e-12, 9.988509340269435e-13, 1.19036614979121e-13, 1.3240281949436815e-14], [7.577099459909446e-07, 1.2641858123954952e-06, 1.0546026066557383e-06, 5.865101195620418e-07, 2.4463773238684e-07, 8.163217391995146e-08, 2.269959119375156e-08, 5.410381879947621e-09, 1.1380020374168374e-09, 2.497775492446559e-10, 4.167362929320514e-11, 6.320865701644435e-12, 8.788266961910893e-13, 1.1278927700881412e-13, 1.3441498910096101e-14, 1.4950797737648685e-15], [7.605321860182021e-08, 1.2688945216060723e-07, 1.0585306819107904e-07, 5.886946920948133e-08, 2.455489338355905e-08, 8.193622904020943e-09, 2.27841402949061e-09, 5.430533913565666e-10, 1.1325580394559615e-10, 2.1174982715205435e-11, 4.182885093876313e-12, 6.344409011699274e-13, 8.821000594247856e-14, 1.1320938290013036e-14, 1.3491564421907214e-15, 1.500648493040348e-16], [6.870284442311962e-09, 1.1462586923989085e-08, 9.562260492506655e-09, 5.317986613486766e-09, 2.21817176310349e-09, 7.401727500631875e-10, 2.058210388426612e-10, 4.905684906664127e-11, 1.0230988275759052e-11, 1.896631685079872e-12, 3.19145046651845e-13, 5.731236012107201e-14, 7.968470534504794e-15, 1.0226794820277184e-15, 1.2187634771325815e-16, 1.3556141586974522e-17], [5.642078866976226e-10, 9.413412208440295e-10, 7.85280846787445e-10, 4.3672864113205694e-10, 1.821627639003264e-10, 6.078515476482741e-11, 1.6902626716318162e-11, 4.028692170221082e-12, 8.401987315610561e-13, 1.5575695065728039e-13, 2.598695295538225e-14, 3.975280530947972e-15, 6.543941460118484e-16, 8.398543527110607e-17, 1.0008842742846023e-17, 1.1132700633842772e-18], [4.2473204262648835e-11, 7.086355738091133e-11, 5.911543350514022e-11, 3.287664922715282e-11, 1.3713094876204323e-11, 4.575867079020248e-12, 1.272418791058547e-12, 3.032773371153499e-13, 6.324961629956169e-14, 1.1725282358804469e-14, 1.9562809862481264e-15, 2.9671976255668e-16, 4.1607376561573616e-17, 6.32236916827946e-18, 7.534591987677381e-19, 8.380624928583023e-20], [2.951404898037569e-12, 4.924211723067785e-12, 4.107850656092789e-12, 2.2845534083100155e-12, 9.529042154343747e-13, 3.179707475394269e-13, 8.841864223528285e-14, 2.1074327538155286e-14, 4.395129366533017e-15, 8.147738411881903e-16, 1.3593929125399134e-16, 2.0618650647096585e-17, 2.8667308377382542e-18, 3.7106387243702954e-19, 5.2356849649560206e-20, 5.8235816892645985e-21], [1.9043987060947573e-13, 3.1773554486482916e-13, 2.65059717136582e-13, 1.4741117213984446e-13, 6.148629610637596e-14, 2.0517113073597646e-14, 5.7052269574902804e-15, 1.3598243372898667e-15, 2.8359642163330186e-16, 5.257341173182853e-17, 8.771504395878526e-18, 1.3304217133968696e-18, 1.8497626339716057e-19, 2.373999231336647e-20, 2.85336707097467e-21, 3.7576753502194165e-22], [1.1468952086426394e-14, 1.9135140811359015e-14, 1.596281905754421e-14, 8.877614046182342e-15, 3.702918836055771e-15, 1.2356119862915704e-15, 3.4358863198255347e-16, 8.189335626212091e-17, 1.7079163943899882e-17, 3.166153905915892e-18, 5.282505355640781e-19, 8.012262787649041e-20, 1.1139914636775982e-20, 1.4297049956123179e-21, 1.703830244321909e-22, 1.911349778974228e-23]] |
| Legacy trial inputs | {"lambda_home": 0.9033522273766768, "lambda_away": 1.668429745556756, "rho": -0.032887856522608186, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1795 |
| Legacy p draw | 0.2278 |
| Legacy p away | 0.5927 |
| Legacy p over 1 5 | 0.7351 |
| Legacy p under 3 5 | 0.7382 |
| Legacy p btts yes | 0.4794 |
| Legacy p over 2 5 | 0.4843 |
| Legacy goal margin distribution | {"-1": 0.2661084617098932, "-10": 4.342054777233146e-06, "-11": 6.512179121788443e-07, "-12": 8.968282116667199e-08, "-13": 1.1414361168564114e-08, "-14": 1.344908961935104e-09, "-15": 1.359339483961523e-10, "-2": 0.18401711482612346, "-3": 0.09160580253959778, "-4": 0.03564746891935939, "-5": 0.011344379118858222, "-6": 0.003047982637485602, "-7": 0.0007078122159715864, "-8": 0.00014463835983401054, "-9": 2.637739300212326e-05, "0": 0.22781571291928868, "1": 0.11909477292894212, "10": 7.873088371977535e-09, "11": 6.393304088256026e-10, "12": 4.767135331689938e-11, "13": 3.2851032619599424e-12, "14": 2.0957501142083475e-13, "15": 1.1468952086426394e-14, "2": 0.04517669750045134, "3": 0.01217666736336112, "4": 0.0025655669553189984, "5": 0.0004420634224517742, "6": 6.43080786579603e-05, "7": 8.085749730686243e-06, "8": 8.946124241379346e-07, "9": 8.833493678674105e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1991 |
| Legacy raw p draw | 0.2505 |
| Legacy raw p away | 0.5504 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9034 |
| Legacy lambda away | 1.6684 |
| Legacy model home team | Udinese |
| Legacy model away team | Roma |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021256305988342366, "mu": 8.657134404654249, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,376.7850 |
| Elo away rating | 1,594.6749 |
| Elo rating diff | -157.8898 |
| Elo home expectancy | 0.2872 |

</details>


---

## 2026-11-01 — Como vs Venezia

The model's most likely 1X2 outcome is **Como win** at **75.2%**. Expected goals are 2.15 for Como and 0.58 for Venezia (2.73 combined). The most likely exact score is 2-0 at 15.4%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 52.4%; Under 3.5 goals: 70.4%; Double Chance 1X: 90.7%; Double Chance X2: 24.8%; Double Chance 12 (either team wins): 84.5%; Under 4.5 goals: 85.5%; BTTS Yes (both teams score): 38.6%; BTTS No (at least one team does not score): 61.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 75.2% | 1.33 |
| Draw | 15.5% | 6.45 |
| Venezia win | 9.3% | 10.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.15 |
| Venezia expected goals | 0.58 |
| Expected total goals | 2.73 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 76.2% |
| Under 1.5 | 23.8% |
| Over 2.5 | 52.4% |
| Under 2.5 | 47.6% |
| Over 3.5 | 29.6% |
| Under 3.5 | 70.4% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 15.36% |
| 2 | 1-0 | 14.08% |
| 3 | 3-0 | 11.01% |
| 4 | 2-1 | 8.97% |
| 5 | 1-1 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 75.2% | 75.9% | 1.30 | -2.3% |
| Draw | 15.5% | 14.4% | 6.31 | -2.2% |
| Venezia win | 9.3% | 9.7% | 9.23 | -13.9% |

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
| Market best home last update utc | 2026-10-29T11:59:52Z |
| Market best draw last update utc | 2026-10-29T11:59:52Z |
| Market best away last update utc | 2026-10-29T11:59:52Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Como |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1500 |
| Dc lambda away | 0.5838 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T12:00:04.904189+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 38.6% |
| P btts no | 61.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.33 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.21 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.38 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.88 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.07145729864959464, "-10": 1.0110611146134688e-10, "-11": 5.31590632672147e-12, "-12": 2.5657222709939753e-13, "-13": 1.1443775183095053e-14, "-14": 4.743908832940494e-16, "-15": 1.8366796245424885e-17, "-16": 6.655133038325487e-19, "-17": 2.1283408635605258e-20, "-2": 0.018078410263274395, "-3": 0.0032022159634869434, "-4": 0.00044078754754984915, "-5": 4.945666049024232e-05, "-6": 4.6754874978646955e-06, "-7": 3.8153419146943705e-07, "-8": 2.7372170177335913e-08, "-9": 1.751414055904187e-09, "0": 0.15502133122802653, "1": 0.25133570000269856, "10": 4.3302415108620695e-05, "11": 8.384431369911982e-06, "12": 1.4902787956341456e-06, "13": 2.447872419092061e-07, "14": 3.736950794884474e-08, "15": 5.328145019150166e-09, "16": 7.109858438002391e-10, "17": 8.373499121104961e-11, "2": 0.22887706789609807, "3": 0.1492980876841665, "4": 0.07568233579329227, "5": 0.031271706508858375, "6": 0.010887176842413044, "7": 0.0032717749609389867, "8": 0.0008644119769189557, "9": 0.00020368636533868927} |
| Raw goal margin distribution | {"-1": 0.06520309733130654, "-10": 9.225693877306297e-11, "-11": 4.850638971464877e-12, "-12": 2.3411609747672713e-13, "-13": 1.044217457421573e-14, "-14": 4.3287047678903337e-16, "-15": 1.6759267784908184e-17, "-16": 6.072651715797714e-19, "-17": 1.9420607706071072e-20, "-2": 0.016496122387328144, "-3": 0.0029219464363880927, "-4": 0.0004022082265697817, "-5": 4.512803462442316e-05, "-6": 4.266271915616391e-06, "-7": 3.481409385987777e-07, "-8": 2.4976458807851174e-08, "-9": 1.598123960920077e-09, "0": 0.18011941990748034, "1": 0.24567272129919615, "10": 4.232674529900868e-05, "11": 8.195517274985241e-06, "12": 1.4567005292682188e-06, "13": 2.3927181000754616e-07, "14": 3.6527515634691206e-08, "15": 5.20809374202441e-09, "16": 6.949662425581982e-10, "17": 8.184831346506668e-11, "2": 0.22372011661061914, "3": 0.14593417284429305, "4": 0.07397709672130956, "5": 0.03056710701113505, "6": 0.010641872054437491, "7": 0.003198056854333953, "8": 0.0008449354496437144, "9": 0.0001990969992076764} |
| Unadjusted home-win probability | 73.5% |
| Unadjusted draw probability | 18.0% |
| Unadjusted away-win probability | 8.5% |
| Raw p over 1 5 | 75.9% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 39.3% |
| P home draw | 90.7% |
| P draw away | 24.8% |
| P home away | 84.5% |
| Raw p home draw | 91.5% |
| Raw p draw away | 26.5% |
| Raw p home away | 82.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5245 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.88, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:00:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:59:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.30 |
| Reference draw odds | 6.31 |
| Reference away odds | 9.23 |
| Market reference 1x2 last update utc | 2026-10-29T11:59:52Z |
| Market reference home last update utc | 2026-10-29T11:59:52Z |
| Market reference draw last update utc | 2026-10-29T11:59:52Z |
| Market reference away last update utc | 2026-10-29T11:59:52Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-29T11:59:53Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:59:53Z |
| Home probability edge | -0.7% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -17.1% |
| Under 2.5 probability edge | +17.1% |
| Raw edge prob home | -0.0242 |
| Raw ev home | -0.0448 |
| Raw edge prob draw | 0.0359 |
| Raw ev draw | 0.1366 |
| Raw edge prob away | -0.0117 |
| Raw ev away | -0.2148 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.0598141093962455, 0.03788304356747798, 0.012420816769771902, 0.002524684647345589, 0.0003848800376832772, 4.6938977052147905e-05, 4.7704638480002664e-06, 4.1556676508726517e-07, 3.167590700384413e-08, 2.1461733042112667e-09, 1.3087088133056732e-10, 7.2548523909687376e-12, 3.6865962178133124e-13, 1.7292606519292735e-14, 7.532006090101458e-16, 3.0619468094354463e-17, 1.166959806879984e-18, 4.185864977995951e-20], [0.1379572069644469, 0.07699342621490866, 0.026469373944267044, 0.005380227666233222, 0.0008201983677849023, 0.00010002927820160483, 1.0166094051691339e-05, 8.855932993612787e-07, 6.750292215477026e-08, 4.573601301053122e-09, 2.7889231123551936e-10, 1.546044872945484e-11, 7.856318604449806e-13, 3.685139849612605e-14, 1.6051076949672563e-15, 6.525159866591492e-17, 2.4868489793206405e-18, 8.920284989021754e-20], [0.15000510150968352, 0.09147117709521675, 0.024216548027460857, 0.005732765430909484, 0.0008739416138160589, 0.00010658366592030572, 1.0832224240747272e-05, 9.436215281904278e-07, 7.19260303877011e-08, 4.87328512099871e-09, 2.9716664423548356e-10, 1.647348988200329e-11, 8.371101467037539e-13, 3.9266075059453335e-14, 1.7102818834871617e-15, 6.952718961899059e-17, 2.6497989945698907e-18, 9.504783922039326e-20], [0.10655609312989558, 0.06497653191234892, 0.01981092575442773, 0.0034965639832181834, 0.0006208042463533393, 7.571168525356199e-05, 7.69466827050857e-06, 6.703013592557233e-07, 5.109264095235336e-08, 3.4617370874426646e-09, 2.1109226486014291e-10, 1.1701940163200508e-11, 5.946410212347848e-13, 2.7892648375098638e-14, 1.2148983855956842e-15, 4.93886249036858e-17, 1.8822841729997153e-18, 6.751721312031354e-20], [0.05676907419565665, 0.03461704960045772, 0.0105545152886449, 0.0021453357861509962, 0.00028398359324859307, 4.033633508313928e-05, 4.099429522317117e-06, 3.571113249305272e-07, 2.7220235275897405e-08, 1.8442831732139871e-09, 1.1246201032695839e-10, 6.234353098400946e-12, 3.1680234571951983e-13, 1.4860152794726326e-14, 6.472521145082682e-16, 2.6312399687561086e-17, 1.0028101325380844e-18, 3.597062888218523e-20], [0.02419554013567937, 0.014754128455573098, 0.0044984386639616465, 0.0009143633017410926, 0.00013939173844952104, 1.476131317422658e-05, 1.7472173528628985e-06, 1.5220437390756823e-07, 1.1601533131414014e-08, 7.860517045823382e-10, 4.7932419599213704e-11, 2.6571428678309853e-12, 1.3502428883225424e-13, 6.333543896240563e-15, 2.758652441734962e-16, 1.12146046368875e-17, 4.2740758333782287e-19, 1.5331037314875368e-20], [0.008593648489545351, 0.0052402960630675635, 0.001597732491735545, 0.0003247588920453917, 4.95084464270916e-05, 6.037922477655477e-06, 5.32836842925301e-07, 5.405917291361361e-08, 4.120573341703041e-09, 2.791858336664029e-10, 1.702439222183832e-11, 9.437504459331962e-13, 4.7957237956599805e-14, 2.2495158046558988e-15, 9.798040984477736e-17, 3.983146053289399e-18, 1.5180444463626677e-19, 5.44519960808235e-21], [0.00261621276179959, 0.0015953328149835488, 0.0004864066920942372, 9.886817675992697e-05, 1.507213490486634e-05, 1.8381587122182344e-06, 1.8681424765141007e-07, 1.4130903132954265e-08, 1.2544493268033368e-09, 8.499411418098898e-11, 5.1828315117659015e-12, 2.8731125826338137e-13, 1.459989178232655e-14, 6.848327533026656e-16, 2.982872745541194e-17, 1.2126115641575083e-18, 4.6214681207691786e-20, 1.65771275408134e-21], [0.0006969098247867151, 0.0004249666268739996, 0.0001295695852845349, 2.633662091585685e-05, 4.0149329783434366e-06, 4.896508742587943e-07, 4.9763798456839494e-08, 4.335046109160299e-09, 2.869205788028148e-10, 2.26408318492533e-11, 1.3806087385183884e-12, 7.653431004512545e-14, 3.889136301333285e-15, 1.8242655225948496e-16, 7.945811414153723e-18, 3.230168910765712e-19, 1.2310720998422212e-20, 4.415834682340058e-22], [0.00016501658376002768, 0.0001006249854494899, 3.067990945514517e-05, 6.2360710909013916e-06, 9.506689395783311e-07, 1.1594113274271259e-07, 1.1783234680015274e-08, 1.0264663718792634e-09, 7.824074509758533e-11, 4.603079040315739e-12, 3.2690504486612694e-13, 1.8122043821010172e-14, 9.208823916631374e-16, 4.319555467623566e-17, 1.881435170133185e-18, 7.648499413615506e-20, 2.9149727131543744e-21, 1.0455957540156835e-22], [3.516584894142874e-05, 2.144368134051373e-05, 6.538040219068496e-06, 1.3289375466017239e-06, 2.02592245947452e-07, 2.4707627968213877e-08, 2.511065502370403e-09, 2.1874505309996811e-10, 1.6673489175898177e-11, 1.1296976390613056e-12, 5.981638807240799e-14, 3.86189703482375e-15, 1.9624458548445516e-16, 9.205186024785963e-18, 4.0094312631153557e-19, 1.6299329975158612e-20, 6.211950809031596e-22, 2.228216189045934e-23], [6.8127418887444025e-06, 4.1543221766301884e-06, 1.2666260537298974e-06, 2.574574129104174e-07, 3.9248552838859416e-08, 4.7866523089183405e-09, 4.864731450639283e-10, 4.237786463485914e-11, 3.230184441995525e-12, 2.1885831449903053e-13, 1.3345697874821345e-14, 6.424015317945397e-16, 3.801880939078249e-17, 1.7833369110239937e-18, 7.767541844862848e-20, 3.1576979206496823e-21, 1.2034521776510202e-22, 4.3167624912384385e-24], [1.2098574512816295e-06, 7.377554767962705e-07, 2.2493688945186094e-07, 4.572120513063604e-08, 6.970050367322283e-09, 8.500493717818789e-10, 8.639152473637536e-11, 7.525776865639913e-12, 5.736402141726435e-13, 3.8866489718193487e-14, 2.370028437901354e-15, 1.313829807254191e-16, 5.797167231189064e-18, 3.1669825236041464e-19, 1.379417939592772e-20, 5.607675177752293e-22, 2.1371800196888622e-23, 7.666028378480695e-25], [1.9832815215853177e-07, 1.209379504195666e-07, 3.687320154123755e-08, 7.494934315124892e-09, 1.1425785809217123e-09, 1.3934593779658172e-10, 1.416189274610254e-11, 1.2336770895932189e-12, 9.403504814568583e-14, 6.3712622330277765e-15, 3.8851135739521997e-16, 2.1537201564324502e-17, 1.0944256554159822e-18, 4.457597764842781e-20, 2.261236732674225e-21, 9.192486724206578e-23, 3.5034124366140736e-24, 1.2566680819201955e-25], [3.01890776270703e-08, 1.8408910351550477e-08, 5.612758106056612e-09, 1.1408625118850267e-09, 1.7392081305180221e-10, 2.1210933936374834e-11, 2.155692345263155e-12, 1.8778762883192468e-13, 1.431380939739815e-14, 9.698196047404783e-16, 5.913834924467727e-17, 3.2783457256009233e-18, 1.665910800298305e-19, 7.814237921311042e-21, 2.9554019704628714e-22, 1.3992602274691608e-23, 5.332817800069233e-25, 1.9128726740833645e-26], [4.2889610216730895e-09, 2.615353139457161e-09, 7.974043141805205e-10, 1.6208229032394535e-10, 2.47089227849742e-11, 3.013436515358124e-12, 3.0625912317580033e-13, 2.667898073475192e-14, 2.0335623146713667e-15, 1.377822315133109e-16, 8.401782854374861e-18, 4.657544429268297e-19, 2.3667587914831714e-20, 1.1101684613421318e-21, 4.835474399153505e-23, 1.706891019171575e-24, 7.576332063776608e-26, 2.7176174243927384e-27], [5.712492343465243e-10, 3.483404187893219e-10, 1.0620674835663213e-10, 2.158783532440835e-11, 3.2909959197852e-12, 4.013613771380634e-13, 4.079083226491229e-14, 3.553389093736172e-15, 2.708513575623043e-16, 1.8351296237201764e-17, 1.1190383867921339e-18, 6.20341074612179e-20, 3.1522999175923e-21, 1.4786398858200909e-22, 6.4403967167347285e-24, 2.6181805939085203e-25, 8.664381790855317e-27, 3.619610588872948e-28], [7.160943116498775e-11, 4.3666507964447354e-11, 1.3313636812838032e-11, 2.7061613648072925e-12, 4.1254557837911577e-13, 5.031299506480944e-14, 5.113369295940083e-15, 4.454380967379356e-16, 3.3952801122768504e-17, 2.3004422687576674e-18, 1.4027800391126743e-19, 7.776338034320844e-21, 3.951592236590906e-22, 1.8535615411820188e-23, 8.073413803167838e-25, 3.2820424386471596e-26, 1.2508419801981372e-27, 3.8959331041451854e-29]] |
| Legacy trial inputs | {"lambda_home": 2.1310493854707375, "lambda_away": 0.6097871084025224, "rho": -0.032887856522608186, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7417 |
| Legacy p draw | 0.1648 |
| Legacy p away | 0.0935 |
| Legacy p over 1 5 | 0.7643 |
| Legacy p under 3 5 | 0.7021 |
| Legacy p btts yes | 0.3993 |
| Legacy p over 2 5 | 0.5249 |
| Legacy goal margin distribution | {"-1": 0.07074812607803772, "-10": 1.4719699147528234e-10, "-11": 8.080991970111236e-12, "-12": 4.07271708927018e-13, "-13": 1.8969159658680864e-14, "-14": 8.211695238837509e-16, "-15": 3.32013649128955e-17, "-16": 1.2561626567702015e-18, "-17": 4.185864977995951e-20, "-2": 0.018754953575937355, "-3": 0.0034595303466254967, "-4": 0.0004964398650875017, "-5": 5.81016784471095e-05, "-6": 5.731560082639978e-06, "-7": 4.88160436284952e-07, "-8": 3.655870012439099e-08, "-9": 2.4421488863978655e-09, "0": 0.16481993978758622, "1": 0.2515302664898473, "10": 3.955277991731175e-05, "11": 7.588536544991327e-06, "12": 1.3365735834064918e-06, "13": 2.1755646720516556e-07, "14": 3.29133436762489e-08, "15": 4.6506150772752495e-09, "16": 6.149157423109716e-10, "17": 7.160943116498775e-11, "2": 0.22650190942471732, "3": 0.14601191407738864, "4": 0.07322393674785974, "5": 0.02994955538241851, "6": 0.010324994427442245, "7": 0.0030732283486292794, "8": 0.0008043374194471334, "9": 0.00018777377645876327} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7243 |
| Legacy raw p draw | 0.1854 |
| Legacy raw p away | 0.0903 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1310 |
| Legacy lambda away | 0.6098 |
| Legacy model home team | Como |
| Legacy model away team | Venezia |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021256305988342366, "mu": 9.807442899958398, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,565.5082 |
| Elo away rating | 1,354.7745 |
| Elo rating diff | 270.7337 |
| Elo home expectancy | 0.8261 |

</details>


---
