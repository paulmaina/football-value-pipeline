# Serie A — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,993 |
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
| Training sha256 | daf58db2ffdb9e54f36003dba9978da024f5c4c6081ee615daad6b589b4b3639 |
| Training as of utc | 2026-11-01T07:18:28.962483+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 93, 'bbs_added_results': 3, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 93, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 171, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-01T07:18:28.962483+00:00', 'observations': 595, 'observations_sha256': 'b1183526566875dd78846a0d423dc633088cd0d3fac8d6a5a4fe43f980230a65', 'eligible_training_matches': 224, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 214, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 29, 'retrospective_eligible_training_matches': 224, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'c5d067288381305e1e34d5e5bf24ed1226cf2a7f052510f09df288ccc146ee29', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 163, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-28T00:00:00+00:00', 'audit_origin_utc': '2026-09-13T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 14, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1989, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1613, 'tuning_matches': 251, 'audit_matches': 125, 'audit_matchdays': 41, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8353035256086855, 'audit_candidate_poisson_score': 0.834738995404647, 'audit_gain': 0.0005645302040384603, 'audit_gain_lower95': -0.005927145293252567, 'audit_baseline_briers': [0.555247448352224, 0.15608820250165614, 0.20937071254302808, 0.24137570462219218], 'audit_candidate_briers': [0.5585874150483705, 0.15467744986372542, 0.20901614766110158, 0.2416407845704014], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1815.160 |
| Base scoring parameter | 0.152 |
| Home-advantage parameter | 0.110 |
| Dixon-Coles low-score adjustment | -0.024 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1993, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-31'} |
| Training data health | {'training_end': '2026-10-31', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 9.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261101T071828962483Z_0d5cbdc5efe6b7f2ada28b38f9a7e2c37350dc209d7f2af5193426a7672f8411.json |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 6, 'ANCHORED_MAIN': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 7} |
| Legacy comparison status | {'AVAILABLE': 7} |
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

## 2026-11-01 — Como vs Venezia

The model's most likely 1X2 outcome is **Como win** at **74.7%**. Expected goals are 2.14 for Como and 0.58 for Venezia (2.71 combined). The most likely exact score is 2-0 at 9.2%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 71.1%; Under 3.5 goals: 48.8%; Double Chance 1X: 90.8%; Double Chance X2: 25.3%; Double Chance 12 (either team wins): 83.9%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 74.7% | 1.34 |
| Draw | 16.1% | 6.21 |
| Venezia win | 9.2% | 10.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.14 |
| Venezia expected goals | 0.58 |
| Expected total goals | 2.71 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 71.1% |
| Under 2.5 | 28.9% |
| Over 3.5 | 51.2% |
| Under 3.5 | 48.8% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.24% |
| 2 | 3-0 | 9.21% |
| 3 | 2-1 | 7.48% |
| 4 | 3-1 | 7.46% |
| 5 | 1-1 | 7.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 74.7% | 75.3% | 1.31 | -2.1% |
| Draw | 16.1% | 15.2% | 5.99 | -3.5% |
| Venezia win | 9.2% | 9.5% | 9.43 | -13.5% |

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
| Market best home last update utc | 2026-11-01T07:19:01Z |
| Market best draw last update utc | 2026-11-01T07:19:01Z |
| Market best away last update utc | 2026-11-01T07:19:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Como |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1352 |
| Dc lambda away | 0.5778 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:18:28.962483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.06 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.77 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.46 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.46 |
| Goal margin distribution | {"-1": 0.06575130662749061, "-10": 1.2294197711042934e-09, "-11": 8.887692772623786e-11, "-12": 5.9055848703963065e-12, "-13": 3.629964474948589e-13, "-14": 2.0754052503716727e-14, "-15": 1.1090434570821792e-15, "-16": 5.56247445680347e-17, "-17": 2.6282999115169194e-18, "-18": 1.1735557188538969e-19, "-19": 4.938384460061791e-21, "-2": 0.020364298728122423, "-20": 1.783084327355007e-22, "-3": 0.004651619778670231, "-4": 0.0008462672548216173, "-5": 0.00012728712676425352, "-6": 1.627412279431742e-05, "-7": 1.806521350529429e-06, "-8": 1.770138399286455e-07, "-9": 1.5514322533833372e-08, "0": 0.16104326937666938, "1": 0.17242332421737241, "10": 0.00040626373694930016, "11": 0.0001085263874382056, "12": 2.6646960334328815e-05, "13": 6.052371563859315e-06, "14": 1.278687929487256e-06, "15": 2.52492606499928e-07, "16": 4.6795767916240025e-08, "17": 8.170561744720595e-09, "18": 1.3480908380368006e-09, "19": 2.0962293020302015e-10, "2": 0.1935841287028769, "20": 2.796818089811417e-11, "3": 0.16339657335293187, "4": 0.10984611965767181, "5": 0.06105203066120228, "6": 0.02884374623697431, "7": 0.011831385994106764, "8": 0.004283888858770348, "9": 0.001387401739827113} |
| Raw goal margin distribution | {"-1": 0.0653819237371728, "-10": 8.480974601084117e-11, "-11": 4.414086997777261e-12, "-12": 2.1089101276066287e-13, "-13": 9.310959095649968e-15, "-14": 3.8205999090193227e-16, "-15": 1.4641806745992477e-17, "-16": 5.2518464556607055e-19, "-17": 1.664303473398388e-20, "-2": 0.01639196867935194, "-3": 0.002877913042469328, "-4": 0.0003924538432298179, "-5": 4.3610600763532384e-05, "-6": 4.082505551865984e-06, "-7": 3.2985036138745277e-07, "-8": 2.3428410610579784e-08, "-9": 1.4840502876385368e-09, "0": 0.18114457511664522, "1": 0.2469610778135866, "10": 4.0255964259843325e-05, "11": 7.742189675507563e-06, "12": 1.3668455335235886e-06, "13": 2.2299454095993375e-07, "14": 3.3811919068480274e-08, "15": 4.7881900220971455e-09, "16": 6.346396101421727e-10, "17": 7.431664934071211e-11, "2": 0.22382469936236885, "3": 0.1452088241802244, "4": 0.07317157023215458, "5": 0.030045836874230108, "6": 0.010393395810215547, "7": 0.003103030855784302, "8": 0.0008144237012634319, "9": 0.00019063148964573577} |
| Unadjusted home-win probability | 73.4% |
| Unadjusted draw probability | 18.1% |
| Unadjusted away-win probability | 8.5% |
| Raw p over 1 5 | 75.6% |
| Raw p under 3 5 | 71.1% |
| Raw p btts yes | 38.9% |
| P home draw | 90.8% |
| P draw away | 25.3% |
| P home away | 83.9% |
| Raw p home draw | 91.5% |
| Raw p draw away | 26.6% |
| Raw p home away | 81.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.4011 |
| Totals anchor target over 2 5 | 0.7108 |
| Totals anchor reference over odds | 1.37 |
| Totals anchor reference under odds | 3.14 |
| Totals anchor reference last update utc | 2026-11-01T07:19:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5174 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:26Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 6.17, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:26Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 4.25, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:26Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.88, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:26Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:26Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:26Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:06Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 7.63, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:06Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.11, "price": 7.63, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.31 |
| Reference draw odds | 5.99 |
| Reference away odds | 9.43 |
| Market reference 1x2 last update utc | 2026-11-01T07:19:01Z |
| Market reference home last update utc | 2026-11-01T07:19:01Z |
| Market reference draw last update utc | 2026-11-01T07:19:01Z |
| Market reference away last update utc | 2026-11-01T07:19:01Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.07 |
| Market reference over 2 5 last update utc | 2026-11-01T07:18:38Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:18:38Z |
| Home probability edge | -0.6% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | -0.0192 |
| Raw ev home | -0.0388 |
| Raw edge prob draw | 0.0287 |
| Raw ev draw | 0.0851 |
| Raw edge prob away | -0.0095 |
| Raw ev away | -0.1976 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06199884274762197, 0.037790950093199945, 0.0122792158553796, 0.002477566950955801, 0.0003749224341010656, 4.53886686010369e-05, 4.579016551148406e-06, 3.9595897683487437e-07, 2.9959614883833446e-08, 2.01497534733404e-09, 1.2196795918425912e-10, 6.711646773542833e-12, 3.3855081685313503e-13, 1.5763640928515818e-14, 6.815606652133656e-16, 2.7503583275870125e-17, 1.0405077433238009e-18, 3.70486523603298e-20], [0.13885651069634972, 0.07890676392877331, 0.026047686226710387, 0.00525561952035326, 0.0007953164141617866, 9.628219031999437e-05, 9.713387870689895e-06, 8.399408650126098e-07, 6.355280802603428e-08, 4.2743320273924225e-09, 2.5872850253316016e-10, 1.4237299130560188e-11, 7.181619374598364e-13, 3.343913630418187e-14, 1.4457827406110805e-15, 5.834287105281265e-17, 2.2072109110034873e-18, 7.859065946638257e-20], [0.15021492297948477, 0.09092621216963792, 0.024536801301661405, 0.0055743269686541344, 0.0008435454124687775, 0.00010212086472838116, 1.0302420058167607e-05, 8.908759467427662e-07, 6.740673108874702e-08, 4.533532954774125e-09, 2.744181278048746e-10, 1.5100667047325238e-11, 7.617121902260893e-13, 3.5466928035226865e-14, 1.533456843782581e-15, 6.188085691495112e-17, 2.3410589863033692e-18, 8.335649695553365e-20], [0.10621609790131366, 0.0642933955032209, 0.019458635682390577, 0.0035006603409327786, 0.0005964660523590212, 7.22090691830793e-05, 7.284781270821124e-06, 6.299331977161708e-07, 4.7662907296551974e-08, 3.2056347705805813e-09, 1.9403946126443463e-10, 1.0677593794678388e-11, 5.386022571188079e-13, 2.507845842295571e-14, 1.0842984106771785e-15, 4.375559382467805e-17, 1.6553491860186802e-18, 5.894089392535722e-20], [0.05632858854637017, 0.03409611436596736, 0.010319316042333541, 0.0020821196307704475, 0.0002809341467518129, 3.82939594628033e-05, 3.863269833501497e-06, 3.3406657377699236e-07, 2.5276623290433043e-08, 1.700014268926914e-09, 1.029031304226484e-10, 5.662548327509926e-12, 2.8563189131255384e-13, 1.3299624009878565e-14, 5.750258222935764e-16, 2.3204494326673082e-17, 8.778658324131656e-19, 3.1257572327326437e-20], [0.023897770302759542, 0.01446549843271397, 0.004378036993741788, 0.0008833528047317826, 0.00013367500869846383, 1.442909387366874e-05, 1.6390173707725224e-06, 1.4172991818142925e-07, 1.0723771942676813e-08, 7.212421180549369e-10, 4.3657322821979843e-11, 2.4023729823748197e-12, 1.2118118891104464e-13, 5.642452046166615e-15, 2.4395844763649493e-16, 9.844657743448014e-18, 3.7244029294965398e-19, 1.3261228498303565e-20], [0.008448987157047233, 0.005114234881744356, 0.0015478422407018747, 0.00031230681388960625, 4.726041038151082e-05, 5.721415710688469e-06, 5.146489558495147e-07, 5.0108200192466286e-08, 3.791358368203809e-09, 2.5499305229593084e-10, 1.5434919457376302e-11, 8.493519779198099e-13, 4.284325674796962e-14, 1.9948725035160157e-15, 8.62507993348615e-17, 3.48055010095704e-18, 1.3167518191164357e-19, 4.6884687504046185e-21], [0.0025603841365798067, 0.001549819595954695, 0.0004690586747685676, 9.464157030488188e-05, 1.4321811926077172e-05, 1.7338198948742157e-06, 1.749156835844719e-07, 1.3486198691839947e-08, 1.1489346168482837e-09, 7.727318717628823e-11, 4.6774035980266014e-12, 2.573879318569789e-13, 1.2983236084744343e-14, 6.045268879644832e-16, 2.6137473555053356e-17, 1.0547471666622903e-18, 3.990289494837585e-20, 1.4207952728835022e-21], [0.0006789122713021142, 0.0004109506565697043, 0.00012437574726051733, 2.5095188857526856e-05, 3.797576201547321e-06, 4.597402343033757e-07, 4.638069824449338e-08, 4.010654605991933e-09, 2.7057278866191945e-10, 2.0489782867771663e-11, 1.2402618244521922e-12, 6.824906580471178e-14, 3.4426390060828308e-15, 1.6029654172104474e-16, 6.930620793903325e-18, 2.7967709389291677e-19, 1.058066430497395e-20, 3.7673852606240734e-22], [0.00016001830542690065, 9.686027261259125e-05, 2.9315122371644315e-05, 5.914887335366067e-06, 8.950813443622551e-07, 1.0835988144491114e-07, 1.093184060934081e-08, 9.453035109713511e-10, 7.152490736142067e-11, 4.289173723445347e-12, 2.9232730622746346e-13, 1.6086172424152793e-14, 8.1142333588014e-16, 3.7781583948686217e-17, 1.6335338774622581e-18, 6.591934852735863e-20, 2.4938420528554597e-21, 8.879653981494756e-23], [3.394440377447831e-05, 2.054680053320399e-05, 6.2185657311307424e-06, 1.2547147243971577e-06, 1.8987204297020113e-07, 2.298619247909071e-08, 2.318952263940936e-09, 2.0052558349645702e-10, 1.5172453732284496e-11, 1.0204443664466689e-12, 5.50741971131234e-14, 3.412331673520691e-15, 1.7212581567883112e-16, 8.014541444943692e-18, 3.4651868964578146e-19, 1.3983356322851435e-20, 5.29014360988657e-22, 1.8836254972291515e-23], [6.545970103124331e-06, 3.962324479133659e-06, 1.1992122657609105e-06, 2.419640400350473e-07, 3.661565909242951e-08, 4.4327462562745124e-09, 4.471957230765396e-10, 3.86701290498523e-11, 2.925914656873301e-12, 1.9678643817228764e-13, 1.1911629733221918e-14, 5.844365146978019e-16, 3.3193407988408087e-17, 1.5455551683101728e-18, 6.682400426489641e-20, 2.6966045136294894e-21, 1.0201717532475329e-22, 3.63245625766901e-24], [1.1571543418284162e-06, 7.004341453643582e-07, 2.1198900365230906e-07, 4.2772841165171704e-08, 6.472679867188993e-09, 7.835922706435073e-10, 7.905237336145639e-11, 6.835855805046263e-12, 5.172243068150221e-13, 3.478663632076884e-14, 2.1056610169165634e-15, 1.158702093966566e-16, 5.21133975360781e-18, 2.732132663868807e-19, 1.18127161376094e-20, 4.766883398460886e-22, 1.8033937752292057e-23, 6.421221704109664e-25], [1.8881933107890993e-07, 1.1429374804362706e-07, 3.459142866150947e-08, 6.979483172824452e-09, 1.0561832926102244e-09, 1.2786312338224842e-10, 1.2899416887400634e-11, 1.115444736975382e-12, 8.43983763447234e-14, 5.676329563949259e-15, 3.4359245808548993e-16, 1.8907188643201838e-17, 9.537218473393262e-19, 3.959471499231368e-20, 1.9275468091871778e-21, 7.778389641664675e-23, 2.942698255555098e-24, 1.0477865769950578e-25], [2.8609939332835118e-08, 1.731780945820619e-08, 5.24129955225977e-09, 1.0575325577527935e-09, 1.600330842889405e-10, 1.9373843673581017e-11, 1.9545219891879064e-12, 1.6901238910045258e-13, 1.2788057309678835e-14, 8.600784862959714e-16, 5.206119164217044e-17, 2.8648206565799707e-18, 1.4450810749548963e-19, 6.7286026334015896e-21, 2.5939146842903967e-22, 1.1785830109851281e-23, 4.458781740471629e-25, 1.587608124141684e-26], [4.045984322798719e-09, 2.4490644582633676e-09, 7.412184825990518e-10, 1.4955502350913331e-10, 2.2631692525788236e-11, 2.7398264240881986e-12, 2.7640622494238596e-13, 2.3901535361676862e-14, 1.808472181366381e-15, 1.2163129853044382e-16, 7.362433130667111e-18, 4.05139603034729e-19, 2.043616837638796e-20, 9.515511533378445e-22, 4.1141500240614014e-23, 1.480293075111423e-24, 6.30555724388588e-26, 2.2451769317990383e-27], [5.364172443892212e-10, 3.246973550121122e-10, 9.827086419630778e-11, 1.982802877986472e-11, 3.0005133910528502e-12, 3.6324662264077675e-13, 3.664598122146456e-14, 3.1688693560022133e-15, 2.3976752915643425e-16, 1.6125896885347176e-17, 9.761125542919784e-19, 5.3713472943588494e-20, 2.7094304504752106e-21, 1.26156803102933e-22, 5.454546638935789e-24, 2.2011184825216354e-25, 7.424757608164503e-27, 2.9766591435747414e-28], [6.693485505248926e-11, 4.051616651215004e-11, 1.2262368743108382e-11, 2.4741677234258184e-12, 3.744080396629605e-13, 4.5326395243782765e-14, 4.572734129954942e-15, 3.954157202119678e-16, 2.991851022360962e-17, 2.0122107965434946e-18, 1.2180061886496928e-19, 6.702438378800827e-21, 3.3808632435717987e-22, 1.574201317706543e-23, 6.80625562420017e-25, 2.7465848296636386e-26, 1.0390801643173478e-27, 3.298822705988554e-29]] |
| Legacy trial inputs | {"lambda_home": 2.1212825422641903, "lambda_away": 0.6053074512580615, "rho": -0.03231166128486351, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7383 |
| Legacy p draw | 0.1692 |
| Legacy p away | 0.0924 |
| Legacy p over 1 5 | 0.7614 |
| Legacy p under 3 5 | 0.7057 |
| Legacy p btts yes | 0.3976 |
| Legacy p over 2 5 | 0.5200 |
| Legacy goal margin distribution | {"-1": 0.07004941359567743, "-10": 1.369926339670444e-10, "-11": 7.46638351907166e-12, "-12": 3.7356805672198503e-13, "-13": 1.72729911328002e-14, "-14": 7.42303536146407e-16, "-15": 2.9794150683829146e-17, "-16": 1.1190984027901835e-18, "-17": 3.70486523603298e-20, "-2": 0.018454598727024478, "-3": 0.003382634061202034, "-4": 0.0004821629912381403, "-5": 5.6042339859855024e-05, "-6": 5.489675130978529e-06, "-7": 4.6424514302775574e-07, "-8": 3.4519333994484995e-08, "-9": 2.289356666274932e-09, "0": 0.16923895996968713, "1": 0.25146305360245336, "10": 3.812585955038921e-05, "11": 7.282076209219834e-06, "12": 1.2768419902875985e-06, "13": 2.068985614565347e-07, "14": 3.1159748823018215e-08, "15": 4.38294404655394e-09, "16": 5.769334109013713e-10, "17": 6.693485505248926e-11, "2": 0.22576002890142047, "3": 0.1450173487624, "4": 0.07244047908431925, "5": 0.029507077569783678, "6": 0.010129291772567765, "7": 0.0030019420425671695, "8": 0.0007822396762075272, "9": 0.00018180816690377202} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7237 |
| Legacy raw p draw | 0.1860 |
| Legacy raw p away | 0.0902 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1213 |
| Legacy lambda away | 0.6053 |
| Legacy model home team | Como |
| Legacy model away team | Venezia |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 89.6% |
| Market home draw odds | 1.09 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:19:06Z |
| Market reference home draw last update utc | 2026-11-01T07:19:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 26.2% |
| Market draw away odds | 3.72 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:19:06Z |
| Market reference draw away last update utc | 2026-11-01T07:19:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.2% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:19:06Z |
| Market reference home away last update utc | 2026-11-01T07:19:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.09 |
| Market reference dc draw away odds | 3.72 |
| Market reference dc home away odds | 1.16 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:19:06Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.46, "price": 1.53, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:19:06Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.53, "price": 2.46, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:19:06Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.94, "price": 1.9, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:19:06Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.9, "price": 1.94, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:19:06Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.56, "price": 2.39, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:19:06Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.39, "price": 1.56, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 88.4% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 7.20 |
| Market reference over 1 5 last update utc | 2026-11-01T07:19:05Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 51.3% |
| Market under 3 5 odds | 1.90 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:19:01Z |
| Market reference under 3 5 odds | 1.89 |
| Market reference under 3 5 opposite odds | 1.99 |
| Market reference under 3 5 last update utc | 2026-11-01T07:19:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.3% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:19:06Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.34 |
| Market reference btts yes last update utc | 2026-11-01T07:19:06Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 9.837650724177182, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,565.5304 |
| Elo away rating | 1,354.7810 |
| Elo rating diff | 270.7494 |
| Elo home expectancy | 0.8261 |

</details>


---

## 2026-11-01 — Frosinone vs Torino

The model's most likely 1X2 outcome is **Frosinone win** at **48.2%**. Expected goals are 1.98 for Frosinone and 1.42 for Torino (3.41 combined). The most likely exact score is 1-1 at 9.8%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 69.4%; Under 3.5 goals: 51.1%; Double Chance 1X: 72.1%; Double Chance X2: 51.8%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 70.6%; BTTS Yes (both teams score): 69.5%; BTTS No (at least one team does not score): 30.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 48.2% | 2.08 |
| Draw | 23.9% | 4.18 |
| Torino win | 27.9% | 3.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.98 |
| Torino expected goals | 1.42 |
| Expected total goals | 3.41 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 87.8% |
| Under 1.5 | 12.2% |
| Over 2.5 | 69.4% |
| Under 2.5 | 30.6% |
| Over 3.5 | 48.9% |
| Under 3.5 | 51.1% |
| Over 4.5 | 29.4% |
| Under 4.5 | 70.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.76% |
| 2 | 2-1 | 8.45% |
| 3 | 2-2 | 7.63% |
| 4 | 1-2 | 6.55% |
| 5 | 3-1 | 5.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 48.2% | 47.3% | 2.07 | -0.3% |
| Draw | 23.9% | 24.7% | 3.89 | -6.9% |
| Torino win | 27.9% | 28.1% | 3.43 | -4.4% |

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
| Market best home last update utc | 2026-11-01T07:19:01Z |
| Market best draw last update utc | 2026-11-01T07:19:01Z |
| Market best away last update utc | 2026-11-01T07:19:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Frosinone |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9818 |
| Dc lambda away | 1.4233 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:18:28.962483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 69.5% |
| P btts no | 30.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.22 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.23 |
| Fair Over 2.5 odds | 1.44 |
| Fair Under 2.5 odds | 3.27 |
| Fair Over 3.5 odds | 2.04 |
| Fair Under 3.5 odds | 1.96 |
| Fair Over 4.5 odds | 3.41 |
| Fair Under 4.5 odds | 1.42 |
| Goal margin distribution | {"-1": 0.15024614202184142, "-10": 6.400190762484705e-07, "-11": 8.622912504182875e-08, "-12": 1.0687072499546586e-08, "-13": 1.226066386387498e-09, "-14": 1.309005966911371e-10, "-15": 1.3056593202859356e-11, "-16": 1.2070190518495012e-12, "-17": 9.063820142494197e-14, "-2": 0.08063813967932636, "-3": 0.033072883469427765, "-4": 0.010949372945664556, "-5": 0.0030216004237218026, "-6": 0.0007125545097336658, "-7": 0.00014641539679347048, "-8": 2.6623768710290415e-05, "-9": 4.33822010805599e-06, "0": 0.23933993819924404, "1": 0.19468825287035116, "10": 1.6257110785830444e-05, "11": 3.0498916552359005e-06, "12": 5.26343390330453e-07, "13": 8.408226258542653e-08, "14": 1.2500057637082331e-08, "15": 1.7361220309696068e-09, "16": 2.234829964750112e-10, "17": 2.3368004377961176e-11, "2": 0.14492758699174982, "3": 0.08276802793573387, "4": 0.038155731247114286, "5": 0.014661808777254473, "6": 0.004814471243525142, "7": 0.0013775178603048705, "8": 0.00034878677316005976, "9": 7.91374485152389e-05} |
| Raw goal margin distribution | {"-1": 0.1514711044193352, "-10": 4.022414349040348e-07, "-11": 5.097490882598124e-08, "-12": 5.940106145452802e-09, "-13": 6.405134228521898e-10, "-14": 6.421419119180037e-11, "-15": 5.949639893115917e-12, "-16": 4.499264957764949e-13, "-2": 0.07876246436855941, "-3": 0.0309303223695495, "-4": 0.009742988307850668, "-5": 0.002548205704965025, "-6": 0.0005680764707436054, "-7": 0.00011015801226138274, "-8": 1.8880300195991297e-05, "-9": 2.8971672056899985e-06, "0": 0.22225015376525187, "1": 0.2118094958662851, "10": 1.1022666353609065e-05, "11": 1.9450747674131694e-06, "12": 3.1561238242932385e-07, "13": 4.7387963913495366e-08, "14": 6.61531937723083e-09, "15": 8.534743341581037e-10, "16": 8.987136537384296e-11, "2": 0.15271414586353746, "3": 0.0835072925676289, "4": 0.03662790878871517, "5": 0.013339342143567945, "6": 0.004140823463322042, "7": 0.0011180880102712766, "8": 0.00026683867814743635, "9": 5.701556489691845e-05} |
| Unadjusted home-win probability | 50.4% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 85.6% |
| Raw p under 3 5 | 55.7% |
| Raw p btts yes | 65.7% |
| P home draw | 72.1% |
| P draw away | 51.8% |
| P home away | 76.1% |
| Raw p home draw | 72.6% |
| Raw p draw away | 49.6% |
| Raw p home away | 77.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0661 |
| Totals anchor target over 2 5 | 0.6942 |
| Totals anchor reference over odds | 1.40 |
| Totals anchor reference under odds | 2.98 |
| Totals anchor reference last update utc | 2026-11-01T07:19:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6554 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:16Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.55, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:16Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.61, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.24, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.24, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.07 |
| Reference draw odds | 3.89 |
| Reference away odds | 3.43 |
| Market reference 1x2 last update utc | 2026-11-01T07:19:01Z |
| Market reference home last update utc | 2026-11-01T07:19:01Z |
| Market reference draw last update utc | 2026-11-01T07:19:01Z |
| Market reference away last update utc | 2026-11-01T07:19:01Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.94 |
| Market reference over 2 5 last update utc | 2026-11-01T07:18:38Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:18:38Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | 0.0311 |
| Raw ev home | 0.0424 |
| Raw edge prob draw | -0.0244 |
| Raw ev draw | -0.1354 |
| Raw edge prob away | -0.0067 |
| Raw ev away | -0.0596 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.04689641721270767, 0.05433527765399846, 0.04047780290892993, 0.018969647636068628, 0.006667497472248247, 0.0018748064653730159, 0.0004393076634367356, 8.823366650008374e-05, 1.550629088222815e-05, 2.4223059968616293e-06, 3.405591800319551e-07, 4.3527476880709465e-08, 5.099714161684552e-09, 5.515261000026137e-10, 5.5386206551721225e-11, 5.19127396587466e-12, 4.561603714162449e-13], [0.07287484979108336, 0.11003461448825175, 0.07062509688515614, 0.033097972367444314, 0.01163335510127653, 0.003271135752001879, 0.0007664977855249709, 0.00015394885090777038, 2.7055156584231883e-05, 4.226405175664951e-06, 5.942028310923953e-07, 7.59461248127256e-08, 8.897908998813683e-09, 9.622949233438677e-10, 9.663706828696522e-11, 9.057661247626715e-12, 7.959021515798169e-13], [0.066601049909035, 0.09363639018222693, 0.06536785195941319, 0.028874436569743773, 0.010148856559428317, 0.002853715651630189, 0.0006686872368882454, 0.00013430388669046425, 2.3602726898288552e-05, 3.6870859280434363e-06, 5.18378339478454e-07, 6.62548611521551e-08, 7.762472762298594e-09, 8.394992725539109e-10, 8.430549362844348e-11, 7.901839492200243e-12, 6.943393974828112e-13], [0.03873485601529537, 0.05445848220792904, 0.03828239716729859, 0.01781670613183192, 0.005902527033526726, 0.0016597075425307183, 0.00038890533821176495, 7.81105060709253e-05, 1.3727234468859636e-05, 2.1443917585961305e-06, 3.014863935113716e-07, 3.8533514269629616e-08, 4.514617489978917e-09, 4.882488112685086e-10, 4.903167684978429e-11, 4.595672521745474e-12, 4.038245136372104e-13], [0.016896006961319574, 0.023754596999785722, 0.016698646014826176, 0.007825707131718138, 0.0027315751080767966, 0.000723958549924141, 0.00016963913068698724, 3.4071526012783216e-05, 5.987771041511895e-06, 9.353760877987934e-07, 1.3150729672261628e-07, 1.680818240518777e-08, 1.9692601544267608e-09, 2.1297240167334652e-10, 2.1387443729027895e-11, 2.004616072115907e-12, 1.761468221508702e-13], [0.005895982700939602, 0.008289336841489438, 0.0058271121844305765, 0.0027308365803150837, 0.0009598410231802998, 0.00026802718808667064, 5.9196790237046305e-05, 1.1889503148635919e-05, 2.0894756115313546e-06, 3.2640618846569947e-07, 4.589041353373832e-08, 5.865335692752621e-09, 6.871874420228714e-10, 7.431824566113595e-11, 7.463301745338487e-12, 6.995251428505452e-13, 6.146769580555999e-14], [0.0017145378436337969, 0.0024105195748109244, 0.0016945104600991558, 0.0007941208275566275, 0.0002791195024796372, 7.848447637792217e-05, 1.826341811126999e-05, 3.4574394336487543e-06, 6.076145726732647e-07, 9.49181486627364e-08, 1.3344823866437075e-08, 1.7056257660385967e-09, 1.9983248506315258e-10, 2.1611570305012015e-11, 2.170310519873435e-12, 2.034202593232615e-13, 1.7874660758894008e-14], [0.00042735733314782, 0.0006008343419288451, 0.0004223654052944498, 0.0001979386808648511, 6.957196462717538e-05, 1.9562657449009798e-05, 4.583953327058672e-06, 9.143062615137171e-07, 1.514510422289988e-07, 2.3658834379452334e-08, 3.326265652323518e-09, 4.2513595219199393e-10, 4.9809269716609866e-11, 5.386794514323485e-12, 5.409610055092325e-13, 5.0703540814462655e-14, 4.4553506831048366e-15], [9.32058773238411e-05, 0.00013104090563575348, 9.21171467018963e-05, 4.317007566113496e-05, 1.5173522242980135e-05, 4.266580935654723e-06, 9.997521004565525e-07, 2.007973016549596e-07, 3.504430345639922e-08, 5.159949868073434e-09, 7.254526465086669e-10, 9.272139807240719e-11, 1.0863313491313455e-11, 1.1748503412181031e-12, 1.1798263702435413e-13, 1.105835243361211e-14, 9.717040916214342e-16], [1.8069365987719978e-05, 2.5404257234420572e-05, 1.7858299125470444e-05, 8.369170692190675e-06, 2.9416162864773174e-06, 8.271411058630095e-07, 1.9381703299004758e-07, 3.892758737030845e-08, 6.841181116584119e-09, 1.0612999060303992e-09, 1.4063994409902023e-10, 1.7975442373040625e-11, 2.1060172700468663e-12, 2.2776246955445475e-13, 2.2872714787955396e-14, 2.143828512550462e-15, 1.8837950317518768e-16], [3.152717370572827e-06, 4.4324988006712205e-06, 3.1158907235604944e-06, 1.46024104202053e-06, 5.132490409591394e-07, 1.4431840796967427e-07, 3.381692124869695e-08, 6.7920302782216665e-09, 1.1936395862559583e-09, 1.8646369720776014e-10, 2.603417609577009e-11, 3.136329711387229e-12, 3.674549087397684e-13, 3.9739672914749643e-14, 3.990798862182107e-15, 3.740521607476718e-16, 3.28681887523843e-17], [5.000742354096916e-07, 7.030691902132979e-07, 4.94232907062505e-07, 2.316188978492513e-07, 8.14099684697602e-08, 2.2891337547287344e-08, 5.363934996266181e-09, 1.0773307433022614e-09, 1.8933140313279485e-10, 2.957629240197094e-11, 4.158218615588038e-12, 5.277936734360636e-13, 5.828455612632054e-14, 6.30338346651857e-15, 6.330081181101813e-16, 5.933099174546327e-17, 5.213449994936781e-18], [7.271020326259761e-08, 1.0222542996280922e-07, 7.186088101927195e-08, 3.367711421541376e-08, 1.1836913273863113e-08, 3.328373445699295e-09, 7.799098138826373e-10, 1.5664261779529122e-10, 2.7528562423337212e-11, 4.300357986928697e-12, 6.046000760307594e-13, 7.727501525295762e-14, 8.990987633807657e-15, 9.165045120094583e-16, 9.203863281810194e-17, 8.626656132463746e-18, 7.580294724055988e-19], [9.758748633957087e-09, 1.3720113962580615e-08, 9.64475744826462e-09, 4.519950125271384e-09, 1.5886829641280991e-09, 4.4671529385237263e-10, 1.0467504544512818e-10, 2.1023678436277947e-11, 3.694726584291314e-12, 5.771695133199328e-13, 8.114597266007889e-14, 1.0371411654775676e-14, 1.2151229219527792e-15, 1.3050477674679736e-16, 1.2352900170572871e-17, 1.157820566726477e-18, 1.0173839085033348e-19], [1.2162090229017372e-09, 1.7099043148285723e-09, 1.2020025796608455e-09, 5.633103517281423e-10, 1.9799368013021494e-10, 5.5673036721220845e-11, 1.3045395420887335e-11, 2.6201297284996112e-12, 4.604647560378768e-13, 7.193122767820168e-14, 1.0113024509916856e-14, 1.2925637197862356e-15, 1.5143780386670756e-16, 1.6377761323779128e-17, 1.6333379355671491e-18, 1.442963511995852e-19, 1.2679407326583187e-20], [1.4146828451186605e-10, 1.9889445444262235e-10, 1.3981580445583992e-10, 6.552372791695258e-11, 2.303043781519099e-11, 6.4758350334600095e-12, 1.5174280705208933e-12, 3.047710146114653e-13, 5.356082539120939e-14, 8.366972445401607e-15, 1.1763374565590465e-15, 1.5034979071620394e-16, 1.761510227259551e-17, 1.9050457240416455e-18, 1.9131144647867772e-19, 1.7807347887179438e-20, 1.474856681164281e-21], [1.542699112509013e-11, 2.1689264092678046e-11, 1.5246789638610908e-11, 7.145304493834173e-12, 2.5114488452858172e-12, 7.061840746386918e-13, 1.6547418707777526e-13, 3.3235009202373e-14, 5.840760569153453e-15, 9.124109343975085e-16, 1.2827855773514625e-16, 1.6395511510168107e-17, 1.9209113008229934e-18, 2.077435488744918e-19, 2.0862343790612393e-20, 1.9553991675923378e-21, 1.7063377157639144e-22]] |
| Legacy trial inputs | {"lambda_home": 1.74478582852073, "lambda_away": 1.4059296409008164, "rho": -0.03231166128486351, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4626 |
| Legacy p draw | 0.2431 |
| Legacy p away | 0.2942 |
| Legacy p over 1 5 | 0.8259 |
| Legacy p under 3 5 | 0.6132 |
| Legacy p btts yes | 0.6270 |
| Legacy p over 2 5 | 0.6088 |
| Legacy goal margin distribution | {"-1": 0.16052410767684755, "-10": 4.2477813126178037e-07, "-11": 5.3315982912694756e-08, "-12": 6.15108639800076e-09, "-13": 6.564688322954163e-10, "-14": 6.513820719683075e-11, "-15": 5.987176117454476e-12, "-16": 4.561603714162449e-13, "-2": 0.08556650002937788, "-3": 0.03388188306809354, "-4": 0.010691758925494219, "-5": 0.0027903183951917816, "-6": 0.000619141210973245, "-7": 0.00011929491293949568, "-8": 2.0291653712027035e-05, "-9": 3.087498950175187e-06, "0": 0.24313440594491523, "1": 0.21366246155439547, "10": 3.932372026920019e-06, "11": 6.125314697943835e-07, "12": 8.770035498160132e-08, "13": 1.1615614057735333e-08, "14": 1.4303502669829705e-09, "15": 1.631575486045441e-10, "16": 1.542699112509013e-11, "2": 0.14078873677555273, "3": 0.0691847253754086, "4": 0.027093828529489855, "5": 0.008775129215746023, "6": 0.0024163954447376877, "7": 0.0005778016246426284, "8": 0.00012196994116424633, "9": 2.3031420716333045e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4528 |
| Legacy raw p draw | 0.2396 |
| Legacy raw p away | 0.3076 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7448 |
| Legacy lambda away | 1.4059 |
| Legacy model home team | Frosinone |
| Legacy model away team | Torino |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 70.8% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:18:54Z |
| Market reference home draw last update utc | 2026-11-01T07:19:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.8% |
| Market draw away odds | 1.82 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:18:54Z |
| Market reference draw away last update utc | 2026-11-01T07:19:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:18:54Z |
| Market reference home away last update utc | 2026-11-01T07:19:02Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home away odds | 1.25 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.06, "price": 1.78, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.06, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.67, "price": 2.21, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.21, "price": 1.67, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 87.5% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.70 |
| Market reference over 1 5 last update utc | 2026-11-01T07:19:05Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.8% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:19:01Z |
| Market reference under 3 5 odds | 1.84 |
| Market reference under 3 5 opposite odds | 2.05 |
| Market reference under 3 5 last update utc | 2026-11-01T07:19:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.0% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:18:54Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.90 |
| Market reference btts yes last update utc | 2026-11-01T07:19:02Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 9.79873558198315, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.7336 |
| Elo away rating | 1,449.1597 |
| Elo rating diff | 85.5739 |
| Elo home expectancy | 0.6207 |

</details>


---

## 2026-11-01 — Juventus vs Napoli

The model's most likely 1X2 outcome is **Juventus win** at **41.4%**. Expected goals are 1.13 for Juventus and 1.09 for Napoli (2.22 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 48.8%; Under 3.5 goals: 72.4%; Double Chance 1X: 70.4%; Double Chance X2: 58.6%; Double Chance 12 (either team wins): 70.9%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 41.4% | 2.42 |
| Draw | 29.1% | 3.44 |
| Napoli win | 29.6% | 3.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.13 |
| Napoli expected goals | 1.09 |
| Expected total goals | 2.22 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 48.8% |
| Under 2.5 | 51.2% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 12.8% |
| Under 4.5 | 87.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.83% |
| 2 | 1-0 | 10.07% |
| 3 | 2-1 | 9.17% |
| 4 | 0-0 | 7.98% |
| 5 | 0-1 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 41.4% | 43.6% | 2.24 | -7.4% |
| Draw | 29.1% | 28.8% | 3.35 | -2.6% |
| Napoli win | 29.6% | 27.6% | 3.50 | +3.5% |
| Over 2.5 | 48.8% | 48.8% | 1.99 | -2.9% |
| Under 2.5 | 51.2% | 51.2% | 1.90 | -2.7% |

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
| Market best home last update utc | 2026-11-01T07:19:01Z |
| Market best draw last update utc | 2026-11-01T07:19:01Z |
| Market best away last update utc | 2026-11-01T07:19:01Z |
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
| Dc lambda home | 1.1275 |
| Dc lambda away | 1.0917 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:18:28.962483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.54 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.81 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.16347767584038947, "-10": 2.7379472357705326e-07, "-11": 3.211232880280599e-08, "-12": 3.458386842568575e-09, "-13": 3.422118911892949e-10, "-14": 2.837611169215388e-11, "-2": 0.08616471174284288, "-3": 0.033058196485569624, "-4": 0.009970791253719082, "-5": 0.002467336720622648, "-6": 0.000516502642888904, "-7": 9.357482065576781e-05, "-8": 1.493129070602229e-05, "-9": 2.1276477286272123e-06, "0": 0.2906662963134217, "1": 0.22372313340017644, "10": 5.00779298644527e-07, "11": 6.06614818422963e-08, "12": 6.747372756352656e-09, "13": 6.895664912832714e-10, "14": 5.905461707030348e-11, "2": 0.12172824855400817, "3": 0.04823485867891089, "4": 0.015025585281590582, "5": 0.003840167041200537, "6": 0.0008302600889419099, "7": 0.0001553533193005673, "8": 2.5602289521242734e-05, "9": 3.7679150031176087e-06} |
| Raw goal margin distribution | {"-1": 0.20505878786652723, "-10": 8.049735578601878e-08, "-11": 7.914596290410969e-09, "-12": 7.117294537962924e-10, "-13": 5.459823882746147e-11, "-2": 0.09578870693563529, "-3": 0.03177930972651416, "-4": 0.008188578884185487, "-5": 0.0017192867309726468, "-6": 0.00030409486202253195, "-7": 4.642144689581237e-05, "-8": 6.229589041668008e-06, "-9": 7.455499959479305e-07, "0": 0.29625215571426244, "1": 0.21189320826846492, "10": 1.1116826144564003e-07, "11": 1.1288802789970631e-08, "12": 1.0484650974159288e-09, "13": 8.306873420255041e-11, "2": 0.1021772360310718, "3": 0.03501097613816388, "4": 0.00931726004382517, "5": 0.002020449085948539, "6": 0.0003690868751740833, "7": 5.8191307049215296e-05, "8": 8.065267144323398e-06, "9": 9.969102271476434e-07} |
| Unadjusted home-win probability | 36.1% |
| Unadjusted draw probability | 29.6% |
| Unadjusted away-win probability | 34.3% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 45.2% |
| P home draw | 70.4% |
| P draw away | 58.6% |
| P home away | 70.9% |
| Raw p home draw | 65.7% |
| Raw p draw away | 63.9% |
| Raw p home away | 70.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1974 |
| Totals anchor target over 2 5 | 0.4879 |
| Totals anchor reference over odds | 1.99 |
| Totals anchor reference under odds | 1.90 |
| Totals anchor reference last update utc | 2026-11-01T07:19:01Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3844 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.35, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.75, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.56, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.89, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.25, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:38Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.49, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.93, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.49, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.24 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.50 |
| Market reference 1x2 last update utc | 2026-11-01T07:19:01Z |
| Market reference home last update utc | 2026-11-01T07:19:01Z |
| Market reference draw last update utc | 2026-11-01T07:19:01Z |
| Market reference away last update utc | 2026-11-01T07:19:01Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.90 |
| Market reference over 2 5 last update utc | 2026-11-01T07:19:01Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:19:01Z |
| Market best over 2 5 last update utc | 2026-11-01T07:19:01Z |
| Market best under 2 5 last update utc | 2026-11-01T07:19:01Z |
| Home probability edge | -2.3% |
| Draw probability edge | +0.2% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0753 |
| Raw ev home | -0.1917 |
| Raw edge prob draw | 0.0080 |
| Raw ev draw | -0.0076 |
| Raw edge prob away | 0.0673 |
| Raw ev away | 0.2001 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.11212641449692957, 0.1038864001592231, 0.05843409112345094, 0.021116116930448063, 0.005722991309281388, 0.001240858047300663, 0.00022420220043751766, 3.4722489092152565e-05, 4.705327782696413e-06, 5.667824480837968e-07, 6.14448392253332e-08, 6.055663669690235e-09, 5.470783393828112e-10, 4.562209107634567e-11], [0.1317294716659854, 0.13571832335138842, 0.06568866977443774, 0.02373767787424259, 0.006433499332489671, 0.0013949102816348067, 0.0002520368508192969, 3.903327793534483e-05, 5.289493118752189e-06, 6.371483555287509e-07, 6.907320154409828e-08, 6.8074728880946016e-09, 6.14997986373112e-10, 5.128606293887727e-11], [0.07672959165424437, 0.0831824880773915, 0.04005537984403178, 0.013342352495898734, 0.0036161083797226837, 0.0007840440322901133, 0.0001416635832452756, 2.1939625099086244e-05, 2.9730912218503713e-06, 3.581250869054541e-07, 3.8824311624079695e-08, 3.826309521951505e-09, 3.456749207706486e-10, 2.882660778710151e-11], [0.028751850795766837, 0.0311698581272134, 0.0168956089570007, 0.005423898307692223, 0.0013550157944748767, 0.00029379430474878285, 5.308369458051916e-05, 8.221141462690105e-06, 1.1140665989471288e-06, 1.341954107005478e-07, 1.4548113589526028e-08, 1.4337816493186837e-09, 1.2953012692445938e-10, 1.080180811827618e-11], [0.008080346575156475, 0.008759897168199833, 0.004748298707469085, 0.0017158755924822405, 0.0004131281127226802, 8.256719962273963e-05, 1.4918505690197265e-05, 2.310448559774294e-06, 3.1309442620730466e-07, 3.7713934833563385e-08, 4.088564616348857e-09, 4.029463258518358e-10, 3.640281541902471e-11, 3.0357125130484123e-12], [0.0018167039398870558, 0.0019694872677123907, 0.001067559774743035, 0.00038578022863557153, 0.00010455600823986886, 2.0139001474094872e-05, 3.354126931626567e-06, 5.194580408659081e-07, 7.039300509662516e-08, 8.479222192205473e-09, 9.192317901116685e-10, 9.059440346144653e-11, 8.184443275991881e-12, 6.825191013187065e-13], [0.00034037455102776514, 0.0003689997746931628, 0.00020001617822552488, 7.227912552740142e-05, 1.9589435339757778e-05, 4.247378192588354e-06, 6.817554623079534e-07, 9.732477238337923e-08, 1.318871335015025e-08, 1.5886526050667504e-09, 1.7222570006049524e-10, 1.6973612885837168e-11, 1.533423330193878e-12, 1.278756145008808e-13], [5.466171019646023e-05, 5.92587156881522e-05, 3.2121162806544064e-05, 1.1607508848421817e-05, 3.14592273194593e-06, 6.820984564121867e-07, 1.232437305583204e-07, 1.695609103381789e-08, 2.1180127152082307e-09, 2.551262074053436e-10, 2.7658211451658563e-11, 2.7258404183009876e-12, 2.4625678221375423e-13, 2.0535905989256035e-14], [7.680993580475749e-06, 8.326958910579605e-06, 4.5136247005030305e-06, 1.6310722922792314e-06, 4.420610372764043e-07, 9.584760239158599e-08, 1.731805133520399e-08, 2.6820693437018276e-09, 3.228783750434871e-10, 3.5850008246146477e-11, 3.8864964861891114e-12, 3.830316080327662e-13, 3.460368796611397e-14, 2.8856792351686002e-15], [9.593985693908647e-07, 1.0400832109134205e-06, 5.63776682672564e-07, 2.0372994813632546e-07, 5.521586788257087e-08, 1.1971895517238071e-08, 2.1631203699825466e-09, 3.3500529122890514e-10, 4.539737056252466e-11, 4.8578839230637105e-12, 4.85444901069883e-13, 4.784276577345572e-14, 4.3221919641653116e-15, 3.6043729251108186e-16], [1.078507675829879e-07, 1.169209296595176e-07, 6.337694250496097e-08, 2.2902297321639345e-08, 6.207090487613586e-09, 1.3458203526165825e-09, 2.4316712544728537e-10, 3.765961192368635e-11, 5.103344342618993e-12, 6.147257180596744e-13, 5.920253819257373e-14, 5.378243387663566e-15, 4.858791078583921e-16, 4.051854974886549e-17], [1.1021855907105041e-08, 1.1948785049122272e-08, 6.476834090077862e-09, 2.3405101945755967e-09, 6.343363008909238e-10, 1.3753669385779182e-10, 2.4850569709321882e-11, 3.848640352243901e-12, 5.215384855319165e-13, 6.282216101644274e-14, 6.810545380319568e-15, 5.962771261529537e-16, 4.965462587892305e-17, 4.1408107415946325e-18], [1.0325180601817937e-09, 1.1193519915730256e-09, 6.067442930818542e-10, 2.1925699866762708e-10, 5.942408360433933e-11, 1.2884320167379505e-11, 2.3279801738417824e-12, 3.605373454641713e-13, 4.8857280473466525e-14, 5.885126459266419e-15, 6.38006082109509e-16, 6.287835237558973e-17, 5.046367223406961e-18, 3.879076183290624e-19], [8.928499493707007e-11, 9.679379059268022e-11, 5.246703493629093e-11, 1.8959823339564145e-11, 5.1385822760517175e-12, 1.1141465755180345e-12, 2.0130756647342963e-13, 3.1176767076331324e-14, 4.2248384875170356e-15, 5.089048863969544e-16, 5.517033745728168e-17, 5.437283462642169e-18, 4.912128826414925e-19, 3.6390275170900444e-20]] |
| Legacy trial inputs | {"lambda_home": 1.124149764486974, "lambda_away": 1.0840991889051739, "rho": -0.03231166128486351, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-11-01T07:19:01Z", "over": 1.99, "under": 1.9, "bookmaker": "pinnacle", "event_id": "aeadf1388a1075328536501576b3d550", "kickoff_utc": "2026-11-01T19:45:00Z", "home_team": "Juventus", "away_team": "Napoli"}} |
| Legacy p home | 0.3983 |
| Legacy p draw | 0.2938 |
| Legacy p away | 0.3079 |
| Legacy p over 1 5 | 0.6523 |
| Legacy p under 3 5 | 0.8174 |
| Legacy p btts yes | 0.4497 |
| Legacy p over 2 5 | 0.3814 |
| Legacy goal margin distribution | {"-1": 0.18435845902971482, "-10": 6.860878884231672e-08, "-11": 6.699488263850448e-09, "-12": 5.983644023216884e-10, "-13": 4.562209107634567e-11, "-2": 0.08609712309367044, "-3": 0.02838912644807145, "-4": 0.007268108064259065, "-5": 0.0015159872402073723, "-6": 0.0002663469457183925, "-7": 4.038506667004447e-05, "-8": 5.382771316833082e-06, "-9": 6.398145249892841e-07, "0": 0.29375798215358817, "1": 0.23363237365111117, "10": 1.204252567485316e-07, "11": 1.2193674933614357e-08, "12": 1.129311850774474e-09, "13": 8.928499493707007e-11, "2": 0.11305381790958202, "3": 0.03865483083587891, "4": 0.010261911809940738, "5": 0.002219512536582609, "6": 0.0004043569683508951, "7": 6.357599550896267e-05, "8": 8.786854782318886e-06, "9": 1.0830207287214038e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3604 |
| Legacy raw p draw | 0.2992 |
| Legacy raw p away | 0.3403 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1241 |
| Legacy lambda away | 1.0841 |
| Legacy model home team | Juventus |
| Legacy model away team | Napoli |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 71.3% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:18:54Z |
| Market reference home draw last update utc | 2026-11-01T07:19:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.5% |
| Market draw away odds | 1.70 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:18:54Z |
| Market reference draw away last update utc | 2026-11-01T07:19:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.2% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:18:54Z |
| Market reference home away last update utc | 2026-11-01T07:19:02Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.62 |
| Market reference dc home away odds | 1.35 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.4, "price": 1.55, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.55, "price": 2.4, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.88, "price": 1.94, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.94, "price": 1.88, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.53, "price": 2.45, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.45, "price": 1.53, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 74.6% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:19:01Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.65 |
| Market reference over 1 5 last update utc | 2026-11-01T07:19:05Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.9% |
| Market under 3 5 odds | 1.34 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:19:01Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.45 |
| Market reference under 3 5 last update utc | 2026-11-01T07:19:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.7% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:18:54Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-11-01T07:19:02Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 9.111253982530137, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,551.0647 |
| Elo away rating | 1,587.2609 |
| Elo rating diff | 23.8038 |
| Elo home expectancy | 0.5342 |

</details>


---

## 2026-11-01 — Lazio vs Cagliari

The model's most likely 1X2 outcome is **Lazio win** at **64.5%**. Expected goals are 1.75 for Lazio and 0.84 for Cagliari (2.59 combined). The most likely exact score is 1-0 at 11.8%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 54.1%; Under 3.5 goals: 68.2%; Double Chance 1X: 86.2%; Double Chance X2: 35.5%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 84.1%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 64.5% | 1.55 |
| Draw | 21.8% | 4.59 |
| Cagliari win | 13.8% | 7.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.75 |
| Cagliari expected goals | 0.84 |
| Expected total goals | 2.59 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 31.8% |
| Under 3.5 | 68.2% |
| Over 4.5 | 15.9% |
| Under 4.5 | 84.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.84% |
| 2 | 2-0 | 11.55% |
| 3 | 2-1 | 10.55% |
| 4 | 1-1 | 10.36% |
| 5 | 3-0 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 64.5% | 66.9% | 1.47 | -5.2% |
| Draw | 21.8% | 20.9% | 4.49 | -2.3% |
| Cagliari win | 13.8% | 12.2% | 7.51 | +3.4% |

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
| Market best home last update utc | 2026-11-01T07:19:01Z |
| Market best draw last update utc | 2026-11-01T07:19:01Z |
| Market best away last update utc | 2026-11-01T07:19:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lazio |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7497 |
| Dc lambda away | 0.8368 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:18:28.962483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.54 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.30 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.09198462829883351, "-10": 6.180125825744387e-09, "-11": 5.064009129964272e-10, "-12": 3.811167038227519e-11, "-13": 2.6517440160751207e-12, "-14": 1.7150691040134575e-13, "-15": 1.031393738682531e-14, "-16": 5.307817923986398e-16, "-2": 0.03416419183096292, "-3": 0.009168271681613977, "-4": 0.0019333212398514475, "-5": 0.00033439031808060027, "-6": 4.891895977927879e-05, "-7": 6.192927001814002e-06, "-8": 6.904528846575918e-07, "-9": 6.874051589409217e-08, "0": 0.21768244150543647, "1": 0.25938340576062857, "10": 1.315759203830142e-05, "11": 2.2542097189430118e-06, "12": 3.547141882280639e-07, "13": 5.1602757839598785e-08, "14": 6.978204251141237e-09, "15": 8.774195014473566e-10, "16": 9.441033690666109e-11, "2": 0.19915184881216355, "3": 0.1117432770275192, "4": 0.04926729181628294, "5": 0.017816775219621512, "6": 0.005449709575571654, "7": 0.001442490110793698, "8": 0.00033625726060761846, "9": 6.999566564087416e-05} |
| Raw goal margin distribution | {"-1": 0.11917410245181234, "-10": 3.988322182825488e-09, "-11": 3.001147460697706e-10, "-12": 2.0735643245330567e-11, "-13": 1.3241995479375573e-12, "-14": 7.859816424214323e-14, "-15": 4.3428370248237116e-15, "-16": 2.080951654499345e-16, "-2": 0.04182371997146538, "-3": 0.010472161969563543, "-4": 0.0020476988900978853, "-5": 0.00032726715951248315, "-6": 4.414397161128681e-05, "-7": 5.145386338183943e-06, "-8": 5.276650150567339e-07, "-9": 4.828744575387107e-08, "0": 0.23841814611411563, "1": 0.2520964789026197, "10": 6.367920308052272e-06, "11": 1.0018794280867853e-06, "12": 1.4473260373146776e-07, "13": 1.932515725971083e-08, "14": 2.3982957766119953e-09, "15": 2.7706687750201615e-10, "16": 2.775836024931543e-11, "2": 0.1828370204221045, "3": 0.0957190911616388, "4": 0.03913353220014486, "5": 0.013076939663434125, "6": 0.0036880418050623783, "7": 0.0008988001972431928, "8": 0.00019271885616664418, "9": 3.68740534102703e-05} |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 17.4% |
| Raw p over 1 5 | 73.3% |
| Raw p under 3 5 | 73.9% |
| Raw p btts yes | 47.1% |
| P home draw | 86.2% |
| P draw away | 35.5% |
| P home away | 78.2% |
| Raw p home draw | 82.6% |
| Raw p draw away | 41.2% |
| Raw p home away | 76.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0912 |
| Totals anchor target over 2 5 | 0.5408 |
| Totals anchor reference over odds | 1.79 |
| Totals anchor reference under odds | 2.09 |
| Totals anchor reference last update utc | 2026-11-01T07:19:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4892 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:18:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.82, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:18:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.16, "price": 5.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 4.43, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.69, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.43, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.47 |
| Reference draw odds | 4.49 |
| Reference away odds | 7.51 |
| Market reference 1x2 last update utc | 2026-11-01T07:19:01Z |
| Market reference home last update utc | 2026-11-01T07:19:01Z |
| Market reference draw last update utc | 2026-11-01T07:19:01Z |
| Market reference away last update utc | 2026-11-01T07:19:01Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 2.14 |
| Market reference over 2 5 last update utc | 2026-11-01T07:19:02Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:19:02Z |
| Home probability edge | -2.4% |
| Draw probability edge | +0.9% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | -0.0814 |
| Raw ev home | -0.1361 |
| Raw edge prob draw | 0.0296 |
| Raw ev draw | 0.0705 |
| Raw edge prob away | 0.0518 |
| Raw ev away | 0.3060 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07043817802649623, 0.04857668202654354, 0.021673439279767785, 0.006070641315662706, 0.001275271272399061, 0.00021431894702924432, 3.0014928359330464e-05, 3.6030249184487378e-06, 3.7844717990343395e-07, 3.533383352255911e-08, 2.969058489342258e-09, 2.2680575101448597e-10, 1.5881839805920348e-11, 1.0265626368047898e-12, 6.161485239071537e-14, 3.4516134126502428e-15, 1.812717635459418e-16], [0.1319497017135891, 0.10515004458865924, 0.0391266056599293, 0.010959201527490749, 0.0023022204985792614, 0.0003869055029808986, 5.418532105898121e-05, 6.504465366447052e-06, 6.832027616870519e-07, 6.378742906675278e-08, 5.3599790598165085e-09, 4.0944766849403247e-10, 2.8671152520795094e-11, 1.8532320116343156e-12, 1.1123200158346543e-13, 6.231125348590075e-15, 3.2724611530219506e-16], [0.12242704319609171, 0.10287393574047192, 0.03862877812299347, 0.009892208407230225, 0.002078075205955077, 0.00034923619752684715, 4.890981219603961e-05, 5.87118749674436e-06, 6.166858129262802e-07, 5.7577054359927345e-08, 4.838128926189655e-09, 3.695836469871781e-10, 2.5879715351500442e-11, 1.6728004535778106e-12, 1.0040240052679619e-13, 5.624459994207379e-15, 2.953852764642975e-16], [0.07367165834352579, 0.06190538665698837, 0.026009166776737907, 0.0065108965670837024, 0.0012505018710617832, 0.00021015626248671278, 2.9431952938545442e-05, 3.53304390957258e-06, 3.7109665747979724e-07, 3.464754981002917e-08, 2.91139091467948e-09, 2.2240053716385788e-10, 1.557336922978391e-11, 1.006623865737645e-12, 6.041811641756692e-14, 3.384573246585629e-15, 1.7775094945754878e-16], [0.033249475165335385, 0.027939124251204032, 0.011738450908512913, 0.0032878918821904854, 0.0006172955525388794, 9.484767395636785e-05, 1.3283221937727495e-05, 1.5945325294784308e-06, 1.6748325440535994e-07, 1.5637123866229942e-08, 1.3139682489952436e-09, 1.0037375706551857e-10, 7.02856926379753e-12, 4.5430924153506596e-13, 2.726788980363398e-14, 1.5275247854862079e-15, 8.022251585603042e-17], [0.012004916122455214, 0.010087583082220825, 0.004238235877815372, 0.001187112460245657, 0.00024937899291666417, 3.745635166604619e-05, 4.795984429992641e-06, 5.757152308639099e-07, 6.047080175113171e-08, 5.645874392815832e-09, 4.744158678691773e-10, 3.624052796248376e-11, 2.5377057548482664e-12, 1.6403099029878173e-13, 9.845229986374604e-15, 5.515216957124063e-16, 2.8964805284747236e-17], [0.003612037242456402, 0.0030351503840330726, 0.0012751997329118483, 0.00035717820713223025, 7.503311149474655e-05, 1.2609879792579425e-05, 1.578320900427184e-06, 1.7322110656317802e-07, 1.8194445157157362e-08, 1.6987297841203885e-09, 1.4274217043053207e-10, 1.0904044255829606e-11, 7.635445015531864e-13, 4.9353618120493023e-14, 2.9622312233249247e-15, 1.6594175957711703e-16, 8.714925980474743e-18], [0.0009315335894401732, 0.00078275619600375, 0.00032887019283463616, 9.21151901339257e-05, 1.9350814785628455e-05, 3.2520502412102137e-06, 4.554429571621066e-07, 4.8862036303425025e-08, 4.692292927077632e-09, 4.3809732488097294e-10, 3.6812778346440166e-11, 2.8121203640026032e-12, 1.9691584069754582e-13, 1.2728150335564364e-14, 7.639505627962608e-16, 4.2795882921673914e-17, 2.247553315584355e-18], [0.0002102097580275839, 0.00017663666927504595, 7.421280825718805e-05, 2.0786702753632702e-05, 4.366702542812382e-06, 7.338572672502103e-07, 1.0277520306911316e-07, 1.2337248092798853e-08, 1.1581476294134849e-09, 9.886098976968309e-11, 8.307167144857162e-12, 6.345827439423678e-13, 4.4436004985827544e-14, 2.8722328775988088e-15, 1.7239299234174553e-16, 9.657313805450974e-18, 5.071826115331123e-19], [4.216525224490544e-05, 3.543094186286502e-05, 1.488609191756226e-05, 4.169533199461565e-06, 8.759018416832642e-07, 1.472019047817071e-07, 2.0615324438753617e-08, 2.474686155019409e-09, 2.5993103509158876e-10, 2.1689584786058014e-11, 1.666306081078928e-12, 1.2728876965399037e-13, 8.91326538103636e-15, 5.761313124872748e-16, 3.457971730498784e-17, 1.9371273552468214e-18, 1.0173401534821873e-19], [7.6120046100756186e-06, 6.396273671813171e-06, 2.6873549728659396e-06, 7.527170892236167e-07, 1.581247236027696e-07, 2.6574051337393575e-08, 3.7216413115364986e-09, 4.4674990466288634e-10, 4.6924804953774775e-11, 4.381148372510809e-12, 3.290209656848061e-13, 2.2979174790400955e-14, 1.609093117176213e-15, 1.0400777828127254e-16, 6.24260388653272e-18, 3.497055412546238e-19, 1.8365828557938028e-20], [1.2492538523786552e-06, 1.0497326177133501e-06, 4.410386914529681e-07, 1.2353312584955322e-07, 2.595084084100516e-08, 4.361234353773898e-09, 6.107819140643338e-10, 7.331893082555073e-11, 7.701124258782835e-12, 7.190177571565122e-13, 6.041817609488628e-14, 4.124872574585174e-15, 2.640783707366138e-16, 1.7069369285883014e-17, 1.0245129047612983e-18, 5.73923712595021e-20, 3.014131395527633e-21], [1.879376496281172e-07, 1.5792169104411937e-07, 6.63498254649428e-08, 1.858431357179629e-08, 3.904042420397977e-09, 6.561037473408806e-10, 9.188598229739177e-11, 1.10300940888545e-11, 1.1585565175035609e-12, 1.0816897387474815e-13, 9.089305579062493e-15, 6.9433013376443e-16, 4.345306140672734e-17, 2.5679145500452483e-18, 1.5412763944485496e-19, 8.634103741651527e-21, 4.5344568605267e-22], [2.6098453825418124e-08, 2.1930209140650445e-08, 9.213842248468208e-09, 2.580759366685477e-09, 5.421450733413165e-10, 9.111156486495708e-11, 1.2759987532763587e-11, 1.5317228976610486e-12, 1.6088598445300685e-13, 1.5021167794739844e-14, 1.2622102193449378e-15, 9.641997211045416e-17, 6.7517095324965365e-18, 3.900371812495683e-19, 2.1403338230693927e-20, 1.1989974242587835e-21, 6.296892252934796e-23], [3.365356547970823e-09, 2.827867636280372e-09, 1.1881111636066782e-09, 3.3278505659799796e-10, 6.990879554490585e-11, 1.1748699883344116e-11, 1.645381288970824e-12, 1.9751337446282098e-13, 2.0746006827742953e-14, 1.9369570984685066e-15, 1.627601180898739e-16, 1.243321105026736e-17, 8.706228360185324e-19, 5.627489542316639e-20, 3.018716109116915e-21, 1.5460892280137986e-22, 8.119748287403137e-24], [4.050271759142987e-10, 3.4033934480811283e-10, 1.4299147873589182e-10, 4.005132583697213e-11, 8.413658887999883e-12, 1.413978776568186e-12, 1.9802482360328474e-13, 2.3771117004590656e-14, 2.496822086208364e-15, 2.3311653677019397e-16, 1.9588495317433133e-17, 1.496361020728286e-18, 1.0478114384988517e-19, 6.77279261297314e-21, 4.0650672658430456e-22, 2.035223406680877e-23, 9.772274263078673e-25], [4.569919196081124e-11, 3.840046785772627e-11, 1.6133719967705223e-11, 4.518988691504669e-12, 9.493126275972395e-13, 1.5953914053553593e-13, 2.2343128967640254e-14, 2.6820937055975514e-15, 2.817162862024168e-16, 2.6302524859109117e-17, 2.2101687515512363e-18, 1.6883432420200537e-19, 1.1822450174756859e-20, 7.64173784221616e-22, 4.586612957414968e-23, 2.569382898470512e-24, 1.2059920861347019e-25]] |
| Legacy trial inputs | {"lambda_home": 1.8052790401592655, "lambda_away": 0.8402876770918862, "rho": -0.03231166128486351, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6340 |
| Legacy p draw | 0.2214 |
| Legacy p away | 0.1447 |
| Legacy p over 1 5 | 0.7490 |
| Legacy p under 3 5 | 0.7220 |
| Legacy p btts yes | 0.4736 |
| Legacy p over 2 5 | 0.4998 |
| Legacy goal margin distribution | {"-1": 0.09894581963710124, "-10": 3.4054203251799537e-09, "-11": 2.5721167859486723e-10, "-12": 1.7838939013843903e-11, "-13": 1.1435968493319203e-12, "-14": 6.814136301576973e-14, "-15": 3.7788595279524375e-15, "-16": 1.812717635459418e-16, "-2": 0.03493474985384747, "-3": 0.008753186704224753, "-4": 0.001714792906213679, "-5": 0.000274762674886051, "-6": 3.717207807373779e-05, "-7": 4.3468190870005446e-06, "-8": 4.473023340393286e-07, "-9": 4.107943392125341e-08, "0": 0.2213842775725447, "1": 0.26438315303027726, "10": 8.730739157738046e-06, "11": 1.4167307439258694e-06, "12": 2.110969705708389e-07, "13": 2.9073831929125893e-08, "14": 3.721829612746641e-09, "15": 4.4342764377202494e-10, "16": 4.569919196081124e-11, "2": 0.1973363836811168, "3": 0.10622630242161521, "4": 0.044708890871183564, "5": 0.015390626499944425, "6": 0.004473338359313446, "7": 0.0011238356876266176, "8": 0.0002484555848125838, "9": 4.9021703016223514e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5988 |
| Legacy raw p draw | 0.2340 |
| Legacy raw p away | 0.1672 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8053 |
| Legacy lambda away | 0.8403 |
| Legacy model home team | Lazio |
| Legacy model away team | Cagliari |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 86.6% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:18:54Z |
| Market reference home draw last update utc | 2026-11-01T07:19:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 35.3% |
| Market draw away odds | 2.84 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:18:54Z |
| Market reference draw away last update utc | 2026-11-01T07:19:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.1% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:18:54Z |
| Market reference home away last update utc | 2026-11-01T07:19:02Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.10 |
| Market reference dc draw away odds | 2.70 |
| Market reference dc home away odds | 1.22 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.24, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.24, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.08, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.08, "price": 1.76, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 77.1% |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 4.05 |
| Market reference over 1 5 last update utc | 2026-11-01T07:19:05Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 69.3% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:19:01Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 3.10 |
| Market reference under 3 5 last update utc | 2026-11-01T07:19:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 50.0% |
| Market btts yes odds | 1.93 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:18:54Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 1.85 |
| Market reference btts yes last update utc | 2026-11-01T07:19:02Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 9.342734941214754, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,538.3289 |
| Elo away rating | 1,414.0618 |
| Elo rating diff | 184.2671 |
| Elo home expectancy | 0.7428 |

</details>


---

## 2026-11-01 — Lecce vs Genoa

The model's most likely 1X2 outcome is **Genoa win** at **39.7%**. Expected goals are 0.85 for Lecce and 1.09 for Genoa (1.94 combined). The most likely exact score is 1-1 at 14.7%. Goal-market probabilities: at least one goal: 88.5%; Over 2.5 goals: 39.1%; Under 3.5 goals: 80.3%; Double Chance 1X: 60.3%; Double Chance X2: 71.3%; Double Chance 12 (either team wins): 68.4%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 46.9%; BTTS No (at least one team does not score): 53.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 28.7% | 3.49 |
| Draw | 31.6% | 3.16 |
| Genoa win | 39.7% | 2.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.85 |
| Genoa expected goals | 1.09 |
| Expected total goals | 1.94 |
| Over 0.5 | 88.5% |
| Under 0.5 | 11.5% |
| Over 1.5 | 66.8% |
| Under 1.5 | 33.2% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.74% |
| 2 | 0-1 | 11.87% |
| 3 | 0-0 | 11.50% |
| 4 | 1-0 | 9.84% |
| 5 | 1-2 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 28.7% | 29.0% | 3.33 | -4.6% |
| Draw | 31.6% | 31.5% | 3.07 | -3.0% |
| Genoa win | 39.7% | 39.4% | 2.47 | -1.8% |

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
| Market best home last update utc | 2026-11-01T07:19:01Z |
| Market best draw last update utc | 2026-11-01T07:19:01Z |
| Market best away last update utc | 2026-11-01T07:19:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lecce |
| Matched away-team name | Genoa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8520 |
| Dc lambda away | 1.0906 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:18:28.962483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.9% |
| P btts no | 53.1% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.69 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.01 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.51 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.21591633813048908, "-10": 3.596950815053339e-07, "-11": 4.161366273095507e-08, "-12": 4.419129766233427e-09, "-13": 4.3218179850472164e-10, "-14": 3.631996350514438e-11, "-2": 0.11765721781593179, "-3": 0.045761988827945924, "-4": 0.013843339590306111, "-5": 0.003415029393880939, "-6": 0.0007100300593682195, "-7": 0.00012745087983285307, "-8": 2.0115576509815655e-05, "-9": 2.8318140024605673e-06, "0": 0.3159803412063222, "1": 0.1796689114162178, "10": 3.258339691876581e-08, "11": 2.9450847078906994e-09, "12": 2.443422622347859e-10, "13": 1.866931125714407e-11, "14": 1.225764997097396e-12, "2": 0.07678573209039277, "3": 0.023332798660488197, "4": 0.005514457622061234, "5": 0.0010628117939437628, "6": 0.00017263889287203802, "7": 2.4210554322197725e-05, "8": 2.985343899119534e-06, "9": 3.2834211877430886e-07} |
| Raw goal margin distribution | {"-1": 0.23785697717606696, "-10": 1.0226482042138143e-07, "-11": 1.0067943607892919e-08, "-12": 9.076075918404758e-10, "-13": 7.106103264184707e-11, "-2": 0.11489992971658469, "-3": 0.03888807869080457, "-4": 0.010145217905483282, "-5": 0.0021477414062735884, "-6": 0.0003820664304658802, "-7": 5.8565702741775964e-05, "-8": 7.883166356067958e-06, "-9": 9.455716651751143e-07, "0": 0.31731001532060715, "1": 0.18512196500458092, "10": 8.664153565175882e-09, "11": 6.664086776278093e-10, "12": 4.6935124837410825e-11, "13": 2.8709878842579056e-12, "2": 0.07013256764244351, "3": 0.018544556488925695, "4": 0.0037797348240525596, "5": 0.0006251466820993949, "6": 8.688380047737033e-05, "7": 1.0405028536772966e-05, "8": 1.0942097905732037e-06, "9": 1.025402431129043e-07} |
| Unadjusted home-win probability | 27.8% |
| Unadjusted draw probability | 31.7% |
| Unadjusted away-win probability | 40.4% |
| Raw p over 1 5 | 58.1% |
| Raw p under 3 5 | 86.7% |
| Raw p btts yes | 38.4% |
| P home draw | 60.3% |
| P draw away | 71.3% |
| P home away | 68.4% |
| Raw p home draw | 59.6% |
| Raw p draw away | 72.2% |
| Raw p home away | 68.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1782 |
| Totals anchor target over 2 5 | 0.3914 |
| Totals anchor reference over odds | 2.43 |
| Totals anchor reference under odds | 1.60 |
| Totals anchor reference last update utc | 2026-11-01T07:19:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3080 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:16Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.24, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:16Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.81, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.3, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.25, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.81, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.33 |
| Reference draw odds | 3.07 |
| Reference away odds | 2.47 |
| Market reference 1x2 last update utc | 2026-11-01T07:19:01Z |
| Market reference home last update utc | 2026-11-01T07:19:01Z |
| Market reference draw last update utc | 2026-11-01T07:19:01Z |
| Market reference away last update utc | 2026-11-01T07:19:01Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.48 |
| Reference Under 2.5 odds | 1.65 |
| Market reference over 2 5 last update utc | 2026-11-01T07:19:02Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:19:02Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -0.7% |
| Under 2.5 probability edge | +0.7% |
| Raw edge prob home | -0.0118 |
| Raw ev home | -0.0733 |
| Raw edge prob draw | 0.0019 |
| Raw ev draw | -0.0259 |
| Raw edge prob away | 0.0099 |
| Raw ev away | -0.0012 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.1495976067267633, 0.15195567155664264, 0.08295099723456188, 0.029353353175807693, 0.007790316313744402, 0.0016540264522340326, 0.00029265002370775997, 4.438210400900844e-05, 5.889457106124403e-06, 6.946885117446616e-07, 7.374753015237196e-08, 7.117248969242208e-09, 6.296341502790108e-10, 5.1416473490398144e-11], [0.12280652055521775, 0.13628955903474527, 0.07098321053871681, 0.02511838697494923, 0.006666365462708589, 0.001415391156341838, 0.00025042783015938395, 3.797885906198668e-05, 5.039753440704711e-06, 5.94462062325315e-07, 6.310757717250285e-08, 6.0904051654931636e-09, 5.387934436187751e-10, 4.399834220927987e-11], [0.0544106641353976, 0.057761889337399966, 0.02998355694993096, 0.010747211067240163, 0.0028522865242318826, 0.0006055925292926417, 0.00010714862982714717, 1.624972235833478e-05, 2.156320547498566e-06, 2.543479110202676e-07, 2.700135372910051e-08, 2.6058548211652063e-09, 2.3052940724223556e-10, 1.8825232320983794e-11], [0.015520181619810253, 0.01647609025666377, 0.008745437289188418, 0.003026439751427911, 0.000813590600137832, 0.00017274014555002416, 3.056324015992441e-05, 4.635095826900152e-06, 6.150721932823154e-07, 7.255058978568458e-08, 7.701907714516423e-09, 7.432980416982487e-10, 6.575656309218017e-11, 5.369738254430069e-12], [0.0033202503774695355, 0.0035247490160865013, 0.0018709214989791462, 0.0006620513478391877, 0.00017183176069399987, 3.695449882716142e-05, 6.538429263492196e-06, 9.91591403107617e-07, 1.315831046274567e-07, 1.5520831458188933e-08, 1.647678011945283e-09, 1.590146084612088e-10, 1.406737748153876e-11, 1.1487543060338241e-12], [0.0005682439981251396, 0.0006032429020654552, 0.00032019871753420013, 0.00011330672753269769, 3.0071359911359722e-05, 6.243883936672569e-06, 1.1190189786159603e-06, 1.697058352080736e-07, 2.2519780425779228e-08, 2.6563115185154863e-09, 2.819917279383728e-10, 2.721454306140803e-11, 2.40756024831398e-12, 1.9660346826663968e-13], [8.10433965051696e-05, 8.603496713088645e-05, 4.566698761657003e-05, 1.615989271586358e-05, 4.2888005025779245e-06, 9.105906864273248e-07, 1.575591796930846e-07, 2.4203576874348364e-08, 3.2117884223633478e-09, 3.788451938719663e-10, 4.021787734475045e-11, 3.88135908396694e-12, 3.433680962015644e-13, 2.8039738009720132e-14], [9.907261375794294e-06, 1.0517462786362757e-05, 5.582623656865869e-06, 1.975488292012074e-06, 5.242903111170454e-07, 1.1131640979810101e-07, 1.9695422598880915e-08, 2.9210502036684464e-09, 3.926294893387637e-10, 4.631245133480574e-11, 4.916489683507553e-12, 4.744820749920211e-13, 4.197550477737914e-14, 3.4277563052699953e-15], [1.0597359337819565e-06, 1.125006480010176e-06, 5.971485630142347e-07, 2.1130924585533055e-07, 5.6081015868011206e-08, 1.1907024051153372e-08, 2.1067322509578935e-09, 3.1949838478234983e-10, 4.146201814649544e-11, 4.95383809908689e-12, 5.25895157910227e-13, 5.0753249130278113e-14, 4.4899341063017554e-15, 3.666519324722123e-16], [1.0076023651299378e-07, 1.069661935496841e-07, 5.677719186890247e-08, 2.009139155429098e-08, 5.332211773345814e-09, 1.1321259582832757e-09, 2.0030918374024417e-10, 3.037807041354211e-11, 4.031137023856931e-12, 4.650041284017407e-13, 5.000238153948961e-14, 4.825644977347649e-15, 4.269052393686276e-16, 3.4861453930321916e-17], [8.622301504233983e-09, 9.153360526567322e-09, 4.858564090352131e-09, 1.7192698391331903e-09, 4.5629048903914415e-10, 9.687880547828412e-11, 1.714095000216343e-11, 2.5995262743218377e-12, 3.449543195553402e-13, 4.0688946120788654e-14, 4.2242362472565675e-15, 4.1294232116771696e-16, 3.6531332348538176e-17, 2.9831804396810393e-18], [6.707559702909065e-10, 7.120687229975962e-10, 3.779629915567681e-10, 1.3374741170595687e-10, 3.549627318873884e-11, 7.536507177033998e-12, 1.3334484470026067e-12, 2.0222533015961348e-13, 2.6835082165215665e-14, 3.1653211757860815e-15, 3.3602775187252014e-16, 3.171423344606672e-17, 2.8418873155190404e-18, 2.320709951268259e-19], [4.783186644984556e-11, 5.077789474875861e-11, 2.695268642526839e-11, 9.537579414995437e-12, 2.5312529054264436e-12, 5.37431227982735e-13, 9.508872206850539e-14, 1.442076614059129e-14, 1.9136200394020258e-15, 2.2572027153989327e-16, 2.3962268340358488e-17, 2.3125578482933967e-18, 2.0007052729667522e-19, 1.654907199853155e-20], [3.1485312087497945e-12, 3.34245343527871e-12, 1.7741597948845766e-12, 6.278108857727775e-13, 1.6661964839549935e-13, 3.537639484828906e-14, 6.259212346370632e-15, 9.492465090264234e-16, 1.259639830710755e-16, 1.485803026599491e-17, 1.5773156119919598e-18, 1.5222405266216702e-19, 1.3466644551030204e-20, 1.0754440033628309e-21]] |
| Legacy trial inputs | {"lambda_home": 0.8557246194159237, "lambda_away": 1.0615913305829727, "rho": -0.03231166128486351, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2870 |
| Legacy p draw | 0.3191 |
| Legacy p away | 0.3939 |
| Legacy p over 1 5 | 0.5756 |
| Legacy p under 3 5 | 0.8716 |
| Legacy p btts yes | 0.3796 |
| Legacy p over 2 5 | 0.3020 |
| Legacy goal margin distribution | {"-1": 0.23453778188175387, "-10": 8.007383446336179e-08, "-11": 7.674867645181968e-09, "-12": 6.736324924882907e-10, "-13": 5.1416473490398144e-11, "-2": 0.11110112227302336, "-3": 0.03665688890296524, "-4": 0.009317625475853316, "-5": 0.001921334883691921, "-6": 0.0003328594291463818, "-7": 4.968406871865638e-05, "-8": 6.511678084201466e-06, "-9": 7.604688490557279e-07, "0": 0.3190753986296593, "1": 0.19000690049923627, "10": 9.361950724542621e-09, "11": 7.233080248345497e-10, "12": 5.117431988512427e-11, "13": 3.1485312087497945e-12, "2": 0.07287538487294405, "3": 0.019381825646417758, "4": 0.003971192985930502, "5": 0.0006600783285973213, "6": 9.217856316913508e-05, "7": 1.1090800357476134e-05, "8": 1.1716970054629988e-06, "9": 1.1030126423018126e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2839 |
| Legacy raw p draw | 0.3227 |
| Legacy raw p away | 0.3934 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.8557 |
| Legacy lambda away | 1.0616 |
| Legacy model home team | Lecce |
| Legacy model away team | Genoa |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 62.4% |
| Market home draw odds | 1.55 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:18:54Z |
| Market reference home draw last update utc | 2026-11-01T07:19:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.8% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:18:54Z |
| Market reference draw away last update utc | 2026-11-01T07:19:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 68.8% |
| Market home away odds | 1.42 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:18:54Z |
| Market reference home away last update utc | 2026-11-01T07:19:02Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.50 |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home away odds | 1.36 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 2.58, "price": 1.48, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 1.48, "price": 2.58, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.0, "price": 1.83, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.83, "price": 2.0, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.59, "price": 2.3, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.3, "price": 1.59, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 66.2% |
| Market over 1 5 odds | 1.44 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:19:01Z |
| Market reference over 1 5 odds | 1.48 |
| Market reference over 1 5 opposite odds | 2.80 |
| Market reference over 1 5 last update utc | 2026-11-01T07:19:05Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 80.9% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 4.75 |
| Market reference under 3 5 last update utc | 2026-11-01T07:19:05Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 47.8% |
| Market btts yes odds | 2.01 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:18:54Z |
| Market reference btts yes odds | 1.95 |
| Market reference btts yes opposite odds | 1.80 |
| Market reference btts yes last update utc | 2026-11-01T07:19:02Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 8.985447111288464, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,357.9326 |
| Elo away rating | 1,431.0354 |
| Elo rating diff | -13.1028 |
| Elo home expectancy | 0.4812 |

</details>


---

## 2026-11-02 — Atalanta BC vs Parma

The model's most likely 1X2 outcome is **Atalanta BC win** at **64.4%**. Expected goals are 1.81 for Atalanta BC and 0.71 for Parma (2.52 combined). The most likely exact score is 2-0 at 10.6%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 58.9%; Under 3.5 goals: 63.0%; Double Chance 1X: 85.4%; Double Chance X2: 35.6%; Double Chance 12 (either team wins): 79.0%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 64.4% | 1.55 |
| Draw | 21.0% | 4.77 |
| Parma win | 14.6% | 6.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 1.81 |
| Parma expected goals | 0.71 |
| Expected total goals | 2.52 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 81.3% |
| Under 1.5 | 18.7% |
| Over 2.5 | 58.9% |
| Under 2.5 | 41.1% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.59% |
| 2 | 1-1 | 9.92% |
| 3 | 1-0 | 9.30% |
| 4 | 2-1 | 9.24% |
| 5 | 3-0 | 7.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 64.4% | 64.7% | 1.52 | -2.2% |
| Draw | 21.0% | 20.3% | 4.65 | -2.4% |
| Parma win | 14.6% | 15.0% | 6.21 | -9.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T19:45:00+00:00 |
| Fixture id | 2e488800d615a94e5377c195810303c0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:19:01Z |
| Market best draw last update utc | 2026-11-01T07:19:01Z |
| Market best away last update utc | 2026-11-01T07:19:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Atalanta |
| Matched away-team name | Parma |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8146 |
| Dc lambda away | 0.7100 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:18:28.962483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.17 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.36 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.08 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.10046995745398486, "-10": 4.206238591349092e-09, "-11": 3.2869273866651086e-10, "-12": 2.3596501657257692e-11, "-13": 1.5663647925156738e-12, "-14": 9.668361353560097e-14, "-15": 5.575041448156873e-15, "-16": 3.000760825912906e-16, "-17": 1.381423262514428e-17, "-2": 0.034978984278149626, "-3": 0.008854308662230154, "-4": 0.0017685900570275726, "-5": 0.0002904606469879867, "-6": 4.040898081072545e-05, "-7": 4.869646573714626e-06, "-8": 5.171738782570083e-07, "-9": 4.907183158676786e-08, "0": 0.20985353501471535, "1": 0.22067518752961207, "10": 4.236455746236743e-05, "11": 8.46078050987225e-06, "12": 1.5523136900305906e-06, "13": 2.6335182241334263e-07, "14": 4.154395480843148e-08, "15": 6.122300076984789e-09, "16": 8.421887610052724e-10, "17": 9.908693005367659e-11, "2": 0.19356355018060664, "3": 0.12522256355377157, "4": 0.06392439998113861, "5": 0.026831090850181472, "6": 0.009539826460318535, "7": 0.0029381337929247505, "8": 0.0007974845080885301, "9": 0.00019338798595588995} |
| Raw goal margin distribution | {"-1": 0.09975717145136409, "-10": 8.073249792557392e-10, "-11": 5.160966166674165e-11, "-12": 3.0287404806154737e-12, "-13": 1.6426020921845556e-13, "-14": 8.279172150150096e-15, "-15": 3.887066734460783e-16, "-16": 1.596349943041938e-17, "-2": 0.03037995766738086, "-3": 0.006529725396886714, "-4": 0.0010915302440361375, "-5": 0.00014879385812308576, "-6": 1.7094537110287493e-05, "-7": 1.695547079210252e-06, "-8": 1.4787113502943892e-07, "-9": 1.1502646501702341e-08, "0": 0.22669364693798036, "1": 0.2588521895208339, "10": 9.597627105068452e-06, "11": 1.5680432688042505e-06, "12": 2.3518013799791695e-07, "13": 3.259736523959108e-08, "14": 4.199026236355828e-09, "15": 5.038429895656833e-10, "16": 5.288260893756624e-11, "2": 0.1984313380117623, "3": 0.10900076912143537, "4": 0.04656739741480755, "5": 0.01622343249346615, "6": 0.004763505102164233, "7": 0.0012075098737706303, "8": 0.0002691384780889804, "9": 5.3505904163363073e-05} |
| Unadjusted home-win probability | 63.5% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 13.8% |
| Raw p over 1 5 | 72.0% |
| Raw p under 3 5 | 75.2% |
| Raw p btts yes | 42.8% |
| P home draw | 85.4% |
| P draw away | 35.6% |
| P home away | 79.0% |
| Raw p home draw | 86.2% |
| Raw p draw away | 36.5% |
| Raw p home away | 77.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2283 |
| Totals anchor target over 2 5 | 0.5891 |
| Totals anchor reference over odds | 1.65 |
| Totals anchor reference under odds | 2.32 |
| Totals anchor reference last update utc | 2026-11-01T07:19:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4683 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:16Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:18:16Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:18:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.87, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:18:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.2, "price": 4.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 4.12, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.7, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.12, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.52 |
| Reference draw odds | 4.65 |
| Reference away odds | 6.21 |
| Market reference 1x2 last update utc | 2026-11-01T07:19:01Z |
| Market reference home last update utc | 2026-11-01T07:19:01Z |
| Market reference draw last update utc | 2026-11-01T07:19:01Z |
| Market reference away last update utc | 2026-11-01T07:19:01Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-11-01T07:19:02Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:19:02Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.7% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -0.6% |
| Under 2.5 probability edge | +0.6% |
| Raw edge prob home | -0.0119 |
| Raw ev home | -0.0342 |
| Raw edge prob draw | 0.0241 |
| Raw ev draw | 0.0541 |
| Raw edge prob away | -0.0121 |
| Raw ev away | -0.1435 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07449240485077996, 0.05387228863980609, 0.02093540991048049, 0.005097564625352619, 0.0009309048122567908, 0.0001359996520962841, 1.655728305656974e-05, 1.7278003582451494e-06, 1.577633425292916e-07, 1.280460294294839e-08, 9.35338136909136e-10, 6.211242474534218e-11, 3.780939811193164e-12, 2.1245107743519312e-13, 1.1084942090074442e-14, 5.398146863526002e-16, 2.4644910176973258e-17], [0.13689224845667503, 0.10017466085614597, 0.038975344736172625, 0.009490109791859198, 0.0017330606914033795, 0.00025318985141048803, 3.082460853566275e-05, 3.2166370224341926e-06, 2.937072017267658e-07, 2.3838263308204306e-08, 1.7413141890607632e-09, 1.1563438104153792e-10, 7.038956160786767e-12, 3.955190759586094e-13, 2.0636779560971372e-14, 1.0049702195565278e-15, 4.588130226476641e-17], [0.13050609381257564, 0.09533081750822057, 0.03299119745360657, 0.008833844245310755, 0.001613215078782427, 0.0002356811207571337, 2.8693007425510003e-05, 2.9941982835919328e-06, 2.733965918925387e-07, 2.2189785973185035e-08, 1.6208978258089061e-09, 1.0763796562186459e-10, 6.552194204043981e-12, 3.681679126689104e-13, 1.9209693076766705e-14, 9.354739392323603e-16, 4.2708491984639773e-17], [0.08098750742189596, 0.059158963883864726, 0.02160693123681814, 0.00498501641219988, 0.0010011047327310074, 0.00014625544263037216, 1.7805874683271586e-05, 1.858094504485607e-06, 1.6966034204361767e-07, 1.3770203395823627e-08, 1.0058723762459616e-09, 6.679634862259998e-11, 4.0660620606099405e-12, 2.284721018667417e-13, 1.1920862200206889e-14, 5.805223371820098e-16, 2.6503393140793712e-17], [0.037693506296138345, 0.027533984544221103, 0.01005637813215423, 0.0024486283117855848, 0.0004236991889723565, 6.8070750948213e-05, 8.287276283066465e-06, 8.648012407492938e-07, 7.89639461023478e-08, 6.408979173734301e-09, 4.681568547310055e-10, 3.1088604496109096e-11, 1.8924416957750847e-12, 1.0633633364394236e-13, 5.5482519304873865e-15, 2.7018886082797235e-16, 1.2335307605126319e-17], [0.01403476128233467, 0.010251975424987864, 0.003744381468277859, 0.0009117197417263774, 0.00016649603435756218, 2.304775596520667e-05, 3.085675909261522e-06, 3.219992026007573e-07, 2.9401354300943097e-08, 2.386312699597027e-09, 1.743130407454673e-10, 1.1575498954007049e-11, 7.046297904013497e-13, 3.959316086453647e-14, 2.0658304050270984e-15, 1.0060184194790673e-16, 4.592915719274742e-18], [0.004354740458135179, 0.003181008302235664, 0.0011618159470318217, 0.0002828906574117345, 5.166080151634256e-05, 7.5473356037391356e-06, 8.706370988238633e-07, 9.991070933409747e-08, 9.122724962870556e-09, 7.404310090957449e-10, 5.4086281600692734e-11, 3.59167445773118e-12, 2.1863427489360406e-13, 1.2285063921911596e-14, 6.40990969738873e-16, 3.121498844764059e-17, 1.4251012540345548e-18], [0.0011581711240028893, 0.0008460095374869846, 0.00030899239442493473, 7.523658271123869e-05, 1.373952113433056e-05, 2.0072622567161597e-06, 2.4437422332293214e-07, 2.4163069988279448e-08, 2.4262471496961554e-09, 1.9692237052819392e-10, 1.4384593101889659e-11, 9.55228832522506e-13, 5.814718611439733e-14, 3.2672914557531658e-15, 1.7047565498681387e-16, 8.301826160180057e-18, 3.7901480859089416e-19], [0.0002695201515907236, 0.0001968764494858198, 7.190619353205468e-05, 1.7508444786135487e-05, 3.197349460855221e-06, 4.671137248204502e-07, 5.686877901706146e-08, 5.934421512450705e-09, 5.134322693532663e-10, 4.582617029245762e-11, 3.3474653555449077e-12, 2.2229307432176437e-13, 1.3531539589729303e-14, 7.603374580797029e-16, 3.967170603923583e-17, 1.9319333721930906e-18, 8.820123947960908e-20], [5.575158635542819e-05, 4.0724874596859506e-05, 1.487415443532445e-05, 3.6217090472914216e-06, 6.613876681326669e-07, 9.662480157208914e-08, 1.1763590312579019e-08, 1.2275646606318313e-09, 1.1208743134467799e-10, 8.620037689609952e-12, 6.924398889655767e-13, 4.5982430093327446e-14, 2.7990663907917373e-15, 1.5727959190883857e-16, 8.206290075379073e-18, 3.9963004471857016e-19, 1.824486588657913e-20], [1.0379244099268927e-05, 7.581728915445756e-06, 2.7691136655777817e-06, 6.742517068253503e-07, 1.2313020131895931e-07, 1.7988589511453275e-08, 2.190021545927994e-09, 2.2853508022365829e-10, 2.0867259327288872e-11, 1.6936568781424009e-12, 1.1722498546839048e-13, 8.56052531265322e-15, 5.211007474275837e-16, 2.9280660568975847e-17, 1.5277607940832062e-18, 7.439891946916673e-20, 3.396637279304821e-21], [1.7566350225838588e-06, 1.283169604378689e-06, 4.6865860364649507e-07, 1.1411372070243344e-07, 2.0839169202111756e-08, 3.0444785805672715e-09, 3.7065016594622066e-10, 3.867841645984284e-11, 3.5316790133336627e-12, 2.8664293468100837e-13, 2.0938413293818766e-14, 1.3174854878039034e-15, 8.819368871866067e-17, 4.955604988948674e-18, 2.5856585425196014e-19, 1.2591644086214315e-20, 5.748638288852911e-22], [2.725265307024391e-07, 1.9907251995338805e-07, 7.27082755914549e-08, 1.7703743810616574e-08, 3.2330144921162855e-09, 4.723241736006526e-10, 5.750312531115707e-11, 6.000617382295123e-12, 5.479090515016128e-13, 4.4470139519407116e-14, 3.2484113432879324e-15, 2.1571525541408389e-16, 1.2442119577452063e-17, 7.688186890315795e-19, 4.011422652484164e-20, 1.9534832418451648e-21, 8.918508563149751e-23], [3.902778751517316e-08, 2.8508637264875882e-08, 1.0412355534941522e-08, 2.535305277922513e-09, 4.629912629297657e-10, 6.764026767615198e-11, 8.234867079978309e-12, 8.593321888787859e-13, 7.846457364913585e-14, 6.368448427608418e-15, 4.651962043509952e-16, 3.089199840610903e-17, 1.8804737876495845e-18, 1.0011950394066764e-19, 5.7446499066046e-21, 2.797530525951922e-22, 1.2771954945366558e-23], [5.1898450629076455e-09, 3.7910273622817894e-09, 1.3846163312549127e-09, 3.371403406989023e-10, 6.156774629233703e-11, 8.994681266939642e-12, 1.0950578287870054e-12, 1.142724505230104e-13, 1.0434078027297937e-14, 8.468648297717592e-16, 6.186095544093456e-17, 4.107962444680345e-18, 2.5006202565201024e-19, 1.4050989814257674e-20, 6.946621572232078e-22, 3.7201058304420754e-23, 1.6983916213830864e-24], [6.441271871248366e-10, 4.705157401773695e-10, 1.7184887253621839e-10, 4.184349565129927e-11, 7.641357064844687e-12, 1.1163567839368838e-12, 1.3591090108582626e-13, 1.4182695481088311e-14, 1.2950046193092072e-15, 1.0510692594168182e-16, 7.677748128900763e-18, 5.098515008122325e-19, 3.103594562796574e-20, 1.7439103548703735e-21, 9.099104380826736e-23, 4.19857722298381e-24, 2.1079246190539802e-25], [7.49480165407573e-11, 5.4747295537869735e-11, 1.9995635021781497e-11, 4.868738762906598e-12, 8.891171916623629e-13, 1.2989472945763514e-13, 1.581403900698196e-14, 1.650240692764176e-15, 1.5068146410894002e-16, 1.2229813896208967e-17, 8.933515076877195e-19, 5.932424446602234e-20, 3.611216251662435e-21, 2.0291430750786107e-22, 1.0587347332509201e-23, 5.155828089279726e-25, 2.230350937088248e-26]] |
| Legacy trial inputs | {"lambda_home": 1.861694846331198, "lambda_away": 0.7304702387700646, "rho": -0.03231166128486351, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6435 |
| Legacy p draw | 0.2131 |
| Legacy p away | 0.1434 |
| Legacy p over 1 5 | 0.7347 |
| Legacy p under 3 5 | 0.7373 |
| Legacy p btts yes | 0.4386 |
| Legacy p over 2 5 | 0.4831 |
| Legacy goal margin distribution | {"-1": 0.1027538411643617, "-10": 1.0577588345354582e-09, "-11": 6.95317444627746e-11, "-12": 4.196261437873327e-12, "-13": 2.340498343285377e-13, "-14": 1.213262080161561e-14, "-15": 5.856959886173666e-16, "-16": 2.4644910176973258e-17, "-2": 0.03219360882227947, "-3": 0.007085007269832177, "-4": 0.001214727170911277, "-5": 0.00016999470620038715, "-6": 2.006156682858762e-05, "-7": 2.0447350240131227e-06, "-8": 1.8329123269616504e-07, "-9": 1.465772959344968e-08, "0": 0.21309092184000963, "1": 0.25645291930590774, "10": 1.1737719984434109e-05, "11": 1.9664648096646814e-06, "12": 3.024625169114129e-07, "13": 4.299553248875408e-08, "14": 5.680356438106796e-09, "15": 6.988744826627064e-10, "16": 7.49480165407573e-11, "2": 0.20068688175159488, "3": 0.11256298272236782, "4": 0.049185830454386, "5": 0.017542950176769146, "6": 0.005276404131254407, "7": 0.0013706172994746814, "8": 0.0003131315553380144, "9": 6.38201497418364e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6396 |
| Legacy raw p draw | 0.2235 |
| Legacy raw p away | 0.1368 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8617 |
| Legacy lambda away | 0.7305 |
| Legacy model home team | Atalanta |
| Legacy model away team | Parma |
| Legacy home name match score | 95/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 85.2% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:18:54Z |
| Market reference home draw last update utc | 2026-11-01T07:19:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.1% |
| Market draw away odds | 2.68 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:18:54Z |
| Market reference draw away last update utc | 2026-11-01T07:19:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.8% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:18:54Z |
| Market reference home away last update utc | 2026-11-01T07:19:02Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.11 |
| Market reference dc draw away odds | 2.62 |
| Market reference dc home away odds | 1.20 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.44, "price": 1.53, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.53, "price": 2.44, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.89, "price": 1.94, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.94, "price": 1.89, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.53, "price": 2.45, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.45, "price": 1.53, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 81.5% |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.85 |
| Market reference over 1 5 last update utc | 2026-11-01T07:19:05Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:19:01Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.63 |
| Market reference under 3 5 last update utc | 2026-11-01T07:19:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.7% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:18:54Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-11-01T07:19:02Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 9.571725715823522, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,508.6715 |
| Elo away rating | 1,398.3138 |
| Elo rating diff | 170.3577 |
| Elo home expectancy | 0.7272 |

</details>


---

## 2026-11-02 — Sassuolo vs Fiorentina

The model's most likely 1X2 outcome is **Fiorentina win** at **41.6%**. Expected goals are 1.40 for Sassuolo and 1.61 for Fiorentina (3.01 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 62.1%; Under 3.5 goals: 59.7%; Double Chance 1X: 58.4%; Double Chance X2: 66.6%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 77.8%; BTTS Yes (both teams score): 64.5%; BTTS No (at least one team does not score): 35.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 33.4% | 3.00 |
| Draw | 25.0% | 4.00 |
| Fiorentina win | 41.6% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.40 |
| Fiorentina expected goals | 1.61 |
| Expected total goals | 3.01 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 83.5% |
| Under 1.5 | 16.5% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 40.3% |
| Under 3.5 | 59.7% |
| Over 4.5 | 22.2% |
| Under 4.5 | 77.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.13% |
| 2 | 1-2 | 8.60% |
| 3 | 2-1 | 7.70% |
| 4 | 2-2 | 7.04% |
| 5 | 0-1 | 6.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 33.4% | 33.5% | 2.90 | -3.2% |
| Draw | 25.0% | 25.2% | 3.82 | -4.4% |
| Fiorentina win | 41.6% | 41.3% | 2.36 | -1.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T17:30:00+00:00 |
| Fixture id | 66608b64d462d1d3deabe573c8456d86 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:19:01Z |
| Market best draw last update utc | 2026-11-01T07:19:01Z |
| Market best away last update utc | 2026-11-01T07:19:01Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sassuolo |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4043 |
| Dc lambda away | 1.6107 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:18:28.962483+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 64.5% |
| P btts no | 35.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.43 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.04 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.48 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.51 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.19630556877928, "-10": 3.111146258540234e-06, "-11": 4.784157578195905e-07, "-12": 6.763223665261475e-08, "-13": 8.84542802821435e-09, "-14": 1.0755974337856579e-09, "-15": 1.210533100506577e-10, "-16": 1.1226409819857753e-11, "-2": 0.12577767698185194, "-3": 0.060600097764046755, "-4": 0.0233266813189869, "-5": 0.0074372626284640725, "-6": 0.002018017711683682, "-7": 0.00047579041604540697, "-8": 9.907584556206374e-05, "-9": 1.8461095211458816e-05, "0": 0.2502800030972097, "1": 0.17542308434425774, "10": 8.106605200348854e-07, "11": 1.0868403249234447e-07, "12": 1.3395400138980797e-08, "13": 1.5274340482112538e-09, "14": 1.6193288175796419e-10, "15": 1.588925846379656e-11, "16": 1.2847230780870469e-12, "2": 0.0981722577488419, "3": 0.041238248135545635, "4": 0.013839535437678454, "5": 0.0038470102795091785, "6": 0.0009100743533278114, "7": 0.00018707220487558507, "8": 3.396276467346997e-05, "9": 5.517398896612897e-06} |
| Raw goal margin distribution | {"-1": 0.2064512647159, "-10": 1.9476310811915474e-06, "-11": 2.80445206325182e-07, "-12": 3.711002309125413e-08, "-13": 4.539830423505937e-09, "-14": 5.120883902654471e-10, "-15": 4.7782363412366275e-11, "-2": 0.12740332029263898, "-3": 0.05843860112623365, "-4": 0.021285306740759628, "-5": 0.006398151165747946, "-6": 0.001632941048684828, "-7": 0.00036156620567587543, "-8": 7.063052835622586e-05, "-9": 1.233647563529398e-05, "0": 0.24631990333377643, "1": 0.17964894383233596, "10": 4.942235410178236e-07, "11": 6.204494808814337e-08, "12": 7.15799354286109e-09, "13": 7.634513752921447e-10, "14": 7.508070706387515e-11, "15": 6.107911336734006e-12, "2": 0.0968420764175641, "3": 0.03872797871015374, "4": 0.012298343124114739, "5": 0.0032230189754919683, "6": 0.000717167409057924, "7": 0.00013844572302214726, "8": 2.357902485043521e-05, "9": 3.5905928655562625e-06} |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 42.2% |
| Raw p over 1 5 | 80.6% |
| Raw p under 3 5 | 64.4% |
| Raw p btts yes | 60.6% |
| P home draw | 58.4% |
| P draw away | 66.6% |
| P home away | 75.0% |
| Raw p home draw | 57.8% |
| Raw p draw away | 66.8% |
| Raw p home away | 75.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0705 |
| Totals anchor target over 2 5 | 0.6213 |
| Totals anchor reference over odds | 1.57 |
| Totals anchor reference under odds | 2.51 |
| Totals anchor reference last update utc | 2026-11-01T07:19:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5788 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.7, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.42, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.72, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.24, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.01, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:19:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.90 |
| Reference draw odds | 3.82 |
| Reference away odds | 2.36 |
| Market reference 1x2 last update utc | 2026-11-01T07:19:01Z |
| Market reference home last update utc | 2026-11-01T07:19:01Z |
| Market reference draw last update utc | 2026-11-01T07:19:01Z |
| Market reference away last update utc | 2026-11-01T07:19:01Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-11-01T07:18:38Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:18:38Z |
| Home probability edge | -0.1% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | -0.0029 |
| Raw ev home | -0.0383 |
| Raw edge prob draw | -0.0057 |
| Raw ev draw | -0.0591 |
| Raw edge prob away | 0.0086 |
| Raw ev away | -0.0039 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.0522142072393232, 0.07392320273913416, 0.06392910559381819, 0.03521026364946601, 0.014544580141734258, 0.0048064351600511515, 0.0013236212803814762, 0.0003124335073183819, 6.452968133659853e-05, 1.1847014344888997e-05, 1.957495704036018e-06, 2.940356815779472e-07, 4.048654276695808e-08, 5.145875137196769e-09, 6.073277308118983e-10, 6.689963616693143e-11], [0.06453023084152826, 0.1147116604138487, 0.08842100981950342, 0.048699681295053046, 0.020116759832429092, 0.006647830382360068, 0.001830714338059367, 0.00043213002844219193, 8.925167236603015e-05, 1.638572856590256e-05, 2.707432635893805e-06, 4.0668380460811737e-07, 5.599735773405083e-08, 7.117313339669373e-09, 8.400012912892737e-10, 9.252958150269275e-11], [0.04714313772469478, 0.07789514461986005, 0.06348709959776262, 0.03367851746085559, 0.013911849713503623, 0.004597341618165018, 0.001266040006024313, 0.00029884176489936785, 6.172245744234976e-05, 1.133163566866395e-05, 1.8723390970384471e-06, 2.8124429668357943e-07, 3.872526349365616e-08, 4.922014994968445e-09, 5.809072544936914e-10, 6.398931252555549e-11], [0.021734721115200036, 0.03591252780898333, 0.029669339827163722, 0.016120990525570037, 0.006413874602181763, 0.002119543644414178, 0.0005836910265141407, 0.00013777704945293793, 2.8456323948746256e-05, 5.22430098895287e-06, 8.632172161484947e-07, 1.2966396910946713e-07, 1.7853771360372532e-08, 2.2692300174248632e-09, 2.678196187099182e-10, 2.950142755066966e-11], [0.00751537961973734, 0.012417747536688367, 0.010258993004156404, 0.005650350417061109, 0.0023026105249617716, 0.0007328907062549868, 0.00020182728002983948, 4.764021696151511e-05, 9.839559289651505e-06, 1.8064462374118978e-06, 2.984811739365671e-07, 4.483489554315236e-08, 6.1734341428175745e-09, 7.846489004878162e-10, 9.260602395356849e-11, 1.0200932700829823e-11], [0.0020789199191247536, 0.0034350231140534227, 0.0028378639517410873, 0.0015630116675960728, 0.0006456455051895517, 0.00021048891143526298, 5.5829881377498136e-05, 1.3178335759994533e-05, 2.721839326511684e-06, 4.99702910006136e-07, 8.256648225072047e-08, 1.2402321922867104e-08, 1.7077081742088831e-09, 2.170512084924418e-10, 2.5616870679746988e-11, 2.821803190049283e-12], [0.0004792292881190828, 0.0007918360233488302, 0.0006541798502485162, 0.00036030294476145105, 0.00014883316715707845, 4.918374821648546e-05, 1.3362123047376582e-05, 3.0378488400434868e-06, 6.274340395794936e-07, 1.151907140002271e-07, 1.9033093168960692e-08, 2.8589633739339003e-09, 3.936581515779644e-10, 5.0034296739535714e-11, 5.905159975985137e-12, 6.504775492019927e-13], [9.468957213725224e-05, 0.00015645666096086492, 0.00012925756345979296, 7.119124921007787e-05, 2.9407528436438065e-05, 9.718078986792004e-06, 2.6762154742578617e-06, 6.232009863605561e-07, 1.239729336771399e-07, 2.276021039047126e-08, 3.76069554448749e-09, 5.648945616333174e-10, 7.778181105658248e-11, 9.886136486043988e-12, 1.1667840121430882e-12, 1.2852603617064383e-13], [1.637076631602789e-05, 2.7049604062670233e-05, 2.234718478727747e-05, 1.2308169508623043e-05, 5.0842322454161095e-06, 1.680146995519941e-06, 4.626876767053958e-07, 1.0921487571157627e-07, 2.2253427109275454e-08, 3.934985418098092e-09, 6.501821325720325e-10, 9.76639417938172e-11, 1.3447603824833352e-11, 1.7092022545712999e-12, 2.0172388546000494e-13, 2.2220711913505286e-14], [2.515841877127845e-06, 4.1569542528968874e-06, 3.4342914826597054e-06, 1.8915063401928255e-06, 7.81339379546232e-07, 2.582031952237413e-07, 7.11053478264335e-08, 1.678402541556554e-08, 3.4665545987938057e-09, 6.27856839968753e-10, 9.991929548731706e-11, 1.500889023195577e-11, 2.0666133885508386e-12, 2.626683763924835e-13, 3.100071119825009e-14, 3.4148552665404104e-15], [3.4796870260507694e-07, 5.749526595131409e-07, 4.750004213114691e-07, 2.616162061494807e-07, 1.0806786096801352e-07, 3.571235206286575e-08, 9.834654497322162e-09, 2.3214159846215945e-09, 4.794627664076546e-10, 8.802464468780937e-11, 1.4348594926230591e-11, 2.075895193984908e-12, 2.858354438480373e-13, 3.632993590718813e-14, 4.287740558561979e-15, 4.723121780764435e-16], [4.3752647823541214e-08, 7.229299945241635e-08, 5.972527412403895e-08, 3.2894917407500716e-08, 1.3588161885188824e-08, 4.490374999415488e-09, 1.23658297848671e-09, 2.918885959188156e-10, 6.028635738238619e-11, 1.1067981832806015e-11, 1.82877527276848e-12, 2.7100215867877963e-13, 3.59401791498541e-14, 4.568028329269159e-15, 5.391289538771843e-16, 5.938726165726955e-17], [5.0428951295604015e-09, 8.332433189191983e-09, 6.8838872382420894e-09, 3.791441822003785e-09, 1.5661606508218613e-09, 5.175570243378103e-10, 1.4252756323818768e-10, 3.364284567804433e-11, 6.948557245008509e-12, 1.2756867173805477e-12, 2.107831725590461e-13, 3.1661767471966214e-14, 4.300896619302745e-15, 5.26507284913869e-16, 6.213957122497637e-17, 6.844928192168427e-18], [5.365292785930917e-10, 8.865134517108268e-10, 7.323981480797084e-10, 4.0338327356109323e-10, 1.666286969206893e-10, 5.5064499610754105e-11, 1.5163950214939756e-11, 3.5793668632235307e-12, 7.392785909970335e-13, 1.357242727842803e-13, 2.2425876526709877e-14, 3.3685937986572955e-15, 4.638304989447142e-16, 5.815955089704243e-17, 6.611222019270288e-18, 7.282531741416127e-19], [5.300565834413699e-11, 8.758185436232914e-11, 7.235624887199124e-11, 3.9851685328686104e-11, 1.6461848647788836e-11, 5.440020087835851e-12, 1.4981012151811928e-12, 3.536185341792729e-13, 7.303599258977754e-14, 1.340868936561078e-14, 2.2155330504229645e-15, 3.3279550458088685e-16, 4.582348426748221e-17, 5.824205088319047e-18, 6.781311876266479e-19, 7.194675197932554e-20], [4.887511766251886e-12, 8.075691484235487e-12, 6.671778613288815e-12, 3.674618654566063e-12, 1.5179035875369924e-12, 5.016098850300439e-13, 1.3813595651801242e-13, 3.2606231118665307e-14, 6.7344559862807095e-15, 1.2363798336199354e-15, 2.0428845128493574e-16, 3.068619455369395e-17, 4.225262462997976e-18, 5.370345692795662e-19, 6.338202494858408e-20, 6.887790760696864e-21]] |
| Legacy trial inputs | {"lambda_home": 1.3831103845140227, "lambda_away": 1.6523114153909313, "rho": -0.03231166128486351, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3264 |
| Legacy p draw | 0.2491 |
| Legacy p away | 0.4246 |
| Legacy p over 1 5 | 0.8093 |
| Legacy p under 3 5 | 0.6397 |
| Legacy p btts yes | 0.6101 |
| Legacy p over 2 5 | 0.5835 |
| Legacy goal margin distribution | {"-1": 0.2032284910680982, "-10": 2.40526942998236e-06, "-11": 3.552330748583773e-07, "-12": 4.821426478867182e-08, "-13": 6.049865741011598e-09, "-14": 6.998573123145911e-10, "-15": 6.689963616693143e-11, "-2": 0.12887583672231032, "-3": 0.060558537234039256, "-4": 0.022606586453473583, "-5": 0.006966339538164155, "-6": 0.0018230093545002568, "-7": 0.0004139266263962433, "-8": 8.292380948768632e-05, "-9": 1.4854355965075472e-05, "0": 0.24906106543284323, "1": 0.1784426839458093, "10": 4.275659360278293e-07, "11": 5.2858848749729126e-08, "12": 6.005439448797785e-09, "13": 6.307829115687097e-10, "14": 6.108134982837248e-11, "15": 4.887511766251886e-12, "2": 0.09503670141402153, "3": 0.037381796712171525, "4": 0.011681126402319619, "5": 0.0030131399981523244, "6": 0.0006600373446245879, "7": 0.0001254492051319444, "8": 2.1037238663501626e-05, "9": 3.1544834594399937e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3182 |
| Legacy raw p draw | 0.2461 |
| Legacy raw p away | 0.4357 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3831 |
| Legacy lambda away | 1.6523 |
| Legacy model home team | Sassuolo |
| Legacy model away team | Fiorentina |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 61.2% |
| Market home draw odds | 1.64 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:18:56Z |
| Market reference home draw last update utc | 2026-11-01T07:19:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 65.9% |
| Market draw away odds | 1.45 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:18:56Z |
| Market reference draw away last update utc | 2026-11-01T07:19:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.0% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:18:56Z |
| Market reference home away last update utc | 2026-11-01T07:19:02Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.55 |
| Market reference dc draw away odds | 1.44 |
| Market reference dc home away odds | 1.30 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:56Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.14, "price": 1.7, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:56Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.7, "price": 2.14, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:56Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.72, "price": 2.1, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:18:56Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.1, "price": 1.72, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 83.0% |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market reference over 1 5 last update utc | 2026-11-01T07:19:05Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.2% |
| Market under 3 5 odds | 1.61 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:19:01Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.48 |
| Market reference under 3 5 last update utc | 2026-11-01T07:19:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.8% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:18:56Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-11-01T07:19:02Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 9.144169919538685, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,428.6172 |
| Elo away rating | 1,446.0432 |
| Elo rating diff | 42.5740 |
| Elo home expectancy | 0.5610 |

</details>


---
