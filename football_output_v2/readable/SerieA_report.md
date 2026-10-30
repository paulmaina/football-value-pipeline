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
| Training sha256 | 9be5dde42f14befdd5aba3b010ce00267f6d705863ee881bc89739237cdefbb1 |
| Training as of utc | 2026-10-30T07:11:26.876100+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 90, 'bbs_added_results': 2, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 90, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 144, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-30T07:11:26.876100+00:00', 'observations': 465, 'observations_sha256': '004c4e846de1cbb38557dd2d7b3f88b0315429f222ddae6caf125ce1ae875007', 'eligible_training_matches': 189, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 185, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 26, 'retrospective_eligible_training_matches': 189, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '5959a5ed16adb8d0b80ab0d596a82207858e504fec7e148ec36cc2a43be9cbd0', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 129, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-27T00:00:00+00:00', 'audit_origin_utc': '2025-10-29T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 14, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1989, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1610, 'tuning_matches': 250, 'audit_matches': 129, 'audit_matchdays': 43, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.848418301807522, 'audit_candidate_poisson_score': 0.846182937757146, 'audit_gain': 0.002235364050375943, 'audit_gain_lower95': -0.0034427898431542672, 'audit_baseline_briers': [0.5603539578857293, 0.16261418970112082, 0.20598918955371587, 0.24319206410252], 'audit_candidate_briers': [0.563129452608437, 0.16062683204349562, 0.20517871625338577, 0.24312418666535762], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1809.059 |
| Base scoring parameter | 0.150 |
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
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261030T071126876100Z_f6ed8ce30d197e3c2cf97a164900d89ec2c8538db7022dc2d4cc8dba133e820e.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 3.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 3.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 3, 'ANCHORED_ALTERNATE': 2, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3} |
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
| Market best home last update utc | 2026-10-30T07:12:04Z |
| Market best draw last update utc | 2026-10-30T07:12:04Z |
| Market best away last update utc | 2026-10-30T07:12:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Milan |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2513 |
| Dc lambda away | 1.8000 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:11:26.876100+00:00 |
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
| Goal margin distribution | {"-1": 0.21638492814929847, "-10": 5.807832810870126e-06, "-11": 9.397749478827448e-07, "-12": 1.3974989457260674e-07, "-13": 1.922137917483215e-08, "-14": 2.4578997191380174e-09, "-15": 2.91441142115524e-10, "-16": 2.8863613013879634e-11, "-2": 0.14972958592166524, "-3": 0.0771141842245032, "-4": 0.0315468540779181, "-5": 0.010652508805513178, "-6": 0.003054496022486261, "-7": 0.0007599100756136687, "-8": 0.0001667998388990068, "-9": 3.273708933209176e-05, "0": 0.25002313238652585, "1": 0.15143713082167795, "10": 1.5496582014957754e-07, "11": 1.7431835086810286e-08, "12": 1.802055514420829e-09, "13": 1.723053073181838e-10, "14": 1.5317070119734132e-11, "15": 1.2625826949953798e-12, "16": 8.6927481528457e-14, "2": 0.07324027764231587, "3": 0.026222497876142642, "4": 0.007457500292230416, "5": 0.0017505985154119238, "6": 0.0003489567871876912, "7": 6.0352007472088975e-05, "8": 9.209214239474667e-06, "9": 1.2565056472571554e-06} |
| Raw goal margin distribution | {"-1": 0.2218481588652229, "-10": 5.7015706764892535e-06, "-11": 9.175539777324164e-07, "-12": 1.3569838364842073e-07, "-13": 1.856153821144416e-08, "-14": 2.360464618365668e-09, "-15": 2.78388106396425e-10, "-16": 2.7454013106574108e-11, "-2": 0.1530179172209788, "-3": 0.07848149211934538, "-4": 0.03195765533983167, "-5": 0.010738177930851573, "-6": 0.003063361909335784, "-7": 0.0007581370164585434, "-8": 0.00016552770645962819, "-9": 3.2313039945710484e-05, "0": 0.23659819069918586, "1": 0.15339249731079077, "10": 1.503034089276162e-07, "11": 1.681525170430415e-08, "12": 1.728796428933076e-09, "13": 1.6439196161059017e-10, "14": 1.4533209727846708e-11, "15": 1.1915496806118983e-12, "16": 8.168921941898887e-14, "2": 0.07394982490398953, "3": 0.026366928830658984, "4": 0.007463879785794329, "5": 0.0017434831526835278, "6": 0.00034576648817458556, "7": 5.948804885124971e-05, "8": 9.029218282846143e-06, "9": 1.2253346201617983e-06} |
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
| Totals anchor scale | 1.0057 |
| Totals anchor target over 2 5 | 0.5871 |
| Totals anchor reference over odds | 1.66 |
| Totals anchor reference under odds | 2.32 |
| Totals anchor reference last update utc | 2026-10-30T07:12:04Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5835 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.66, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.56, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.66, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.71 |
| Reference draw odds | 3.76 |
| Reference away odds | 2.02 |
| Market reference 1x2 last update utc | 2026-10-30T07:12:04Z |
| Market reference home last update utc | 2026-10-30T07:12:04Z |
| Market reference draw last update utc | 2026-10-30T07:12:04Z |
| Market reference away last update utc | 2026-10-30T07:12:04Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-30T07:11:45Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:11:45Z |
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
| Legacy trial matrix | [[0.0545458763489633, 0.08279480514777975, 0.07582792888599124, 0.04437407400696315, 0.01947559236652725, 0.00683820373072106, 0.0020008390238241518, 0.0005018055647657778, 0.00011012016414246428, 2.1480565209087027e-05, 3.771091486881634e-06, 6.018603693832003e-07, 8.805131883867902e-08, 1.1890876729701631e-08, 1.4911014933884467e-09, 1.7451682774824154e-10, 1.9148673377335506e-11], [0.05713295525630553, 0.11547789356610064, 0.0949621069738805, 0.0555712865249391, 0.024390001320892266, 0.008563734282684456, 0.0025057243710767613, 0.0006284295828918497, 0.0001379075356653963, 2.690090262535954e-05, 4.7226767029859185e-06, 7.537318982645398e-07, 1.102699082197225e-07, 1.4891382695113575e-08, 1.8673612955585563e-09, 2.1855384828310219e-10, 2.3980588635098147e-11], [0.037988021608020985, 0.0666911245095549, 0.06143319798993881, 0.03479698399511711, 0.015272248290006696, 0.005362339859439367, 0.0015690054394800334, 0.0003935027512478447, 8.635334201235854e-05, 1.6844495361624444e-05, 2.9571909510168307e-06, 4.7196310254127536e-07, 6.904753284311192e-08, 9.324513390102745e-09, 1.1692826489718097e-09, 1.3685151516809685e-10, 1.5015887000465875e-11], [0.01585793266704675, 0.02783991682627792, 0.024437642193571432, 0.015007319412943927, 0.006375332928793783, 0.0022384852074227397, 0.0006549744251027518, 0.00016426599410663674, 3.6047823109516746e-05, 7.031660558985804e-06, 1.2344663659695083e-06, 1.9701892292937247e-07, 2.8823589128963058e-08, 3.892477134476612e-09, 4.881119029432655e-10, 5.7128063559403224e-11, 6.268316035154941e-12], [0.004964868223477529, 0.008716238194293324, 0.007651039749695948, 0.004477345076820988, 0.0020621756537799385, 0.0007008343589547735, 0.00020506214641335816, 5.142908798148347e-05, 1.1286003998105578e-05, 2.2015018477241683e-06, 3.864919193464581e-07, 6.16835126251029e-08, 9.024210454010701e-09, 1.2186731045803367e-09, 1.528201265137219e-10, 1.788589429593708e-11, 1.9625107352313674e-12], [0.0012435374519010386, 0.0021831331963735622, 0.0019163357508140157, 0.0011214288149246849, 0.0004921903376310161, 0.0001813544256917665, 5.136137507666103e-05, 1.2881308051574664e-05, 2.8267756609497586e-06, 5.514043625828231e-07, 9.680361188474785e-08, 1.544970675181369e-08, 2.2602701961622308e-09, 3.0523783894282013e-10, 3.827645411119504e-11, 4.479832780367767e-12, 4.915448888407126e-13], [0.00025955462204214615, 0.0004556696790966422, 0.0003999829685450978, 0.00023406776511634338, 0.00010273134666054363, 3.607068092077717e-05, 1.1075623125435687e-05, 2.688622717091263e-06, 5.900125381460091e-07, 1.1509066389901115e-07, 2.02051211699733e-08, 3.224706091882239e-09, 4.717699298731716e-10, 6.371009718979499e-11, 7.989168773933637e-12, 9.350432528934447e-13, 1.0259662678012613e-13], [4.643568696735909e-05, 8.152170210867145e-05, 7.155905671608213e-05, 4.1875954219481955e-05, 1.8379178215865644e-05, 6.453234524425929e-06, 1.888198125533061e-06, 4.969521812819963e-07, 1.0555634614634716e-07, 2.059032507158441e-08, 3.6148024427555385e-09, 5.769168796387864e-10, 8.440212164916222e-11, 1.1398071459829208e-11, 1.4293043113504743e-12, 1.6728415564586166e-13, 1.835507612072233e-14], [7.269140041774631e-06, 1.2761578599845343e-05, 1.1202005149447623e-05, 6.555349893247627e-06, 2.8771151893967383e-06, 1.0102028966092592e-06, 2.955825034044238e-07, 7.413137353361374e-08, 1.7071714493673467e-08, 3.2232527658354713e-09, 5.658687723993296e-10, 9.03117809693617e-11, 1.321248552911312e-11, 1.7842780641081848e-12, 2.2374630117612195e-13, 2.6187013342013455e-14, 2.873342196762429e-15], [1.0114901877864242e-06, 1.7757549669186823e-06, 1.5587426060143803e-06, 9.121673342955706e-07, 4.003463637351543e-07, 1.4056825315257412e-07, 4.112987233107861e-08, 1.0315272027428809e-08, 2.263664511900802e-09, 4.633771690513544e-10, 7.873981070213873e-11, 1.2566752018403092e-11, 1.838498005563996e-12, 2.482796787180043e-13, 3.113397002844123e-14, 3.643884543516407e-15, 3.998213573373875e-16], [1.2667264005063706e-07, 2.22384332007101e-07, 1.9520707511296494e-07, 1.1423407344765023e-07, 5.013684901875945e-08, 1.760387984890923e-08, 5.150845332988511e-09, 1.291819492005587e-09, 2.8348704058012794e-10, 5.5298336217829285e-11, 1.0187723366090169e-11, 1.5737806201723756e-12, 2.302418737271985e-13, 3.109297821559715e-14, 3.8990216873886224e-15, 4.563370764644492e-16, 5.007110053473893e-17], [1.4421528239091347e-08, 2.531818964766057e-08, 2.222409152510508e-08, 1.3005412340290431e-08, 5.7080201664231635e-09, 2.0041806206701762e-09, 5.864175673230718e-10, 1.4707210078135198e-10, 3.227465978058447e-11, 6.2956492974441825e-12, 1.1052534809438173e-12, 1.8511187732515243e-13, 2.6212761354391604e-14, 3.5398983015940647e-15, 4.4389894571571947e-16, 5.1953429186805254e-17, 5.700534780323999e-18], [1.505050895590309e-09, 2.642241749431801e-09, 2.3193373336727513e-09, 1.3572630560205217e-09, 5.956969830864479e-10, 2.0915909798575157e-10, 6.119935905940359e-11, 1.5348650526323734e-11, 3.3682287204467413e-12, 6.570227826311057e-13, 1.153458020378018e-13, 1.840901162508761e-14, 2.8262742713264275e-15, 3.694287471331432e-16, 4.632591600036502e-17, 5.42193267109087e-18, 5.949157977040383e-19], [1.4498697272982638e-10, 2.5453666290814834e-10, 2.234301177014924e-10, 1.3075003793361102e-10, 5.738563559215676e-11, 2.0149049128309432e-11, 5.895554648036271e-12, 1.4785907784380333e-12, 3.244736022350194e-13, 6.32933707074724e-14, 1.1111676491176331e-14, 1.7734063839899417e-15, 2.5944683998262576e-16, 3.676800890380052e-17, 4.462742316228948e-18, 5.223142995560159e-19, 5.73103811910809e-20], [1.29694659780206e-11, 2.2768973843585957e-11, 1.998641157502092e-11, 1.1695934722113303e-11, 5.133296008783122e-12, 1.8023854298001777e-12, 5.273728666074701e-13, 1.3226383333143502e-13, 2.9025016977178126e-14, 5.661758450219294e-15, 9.939686821355107e-16, 1.5863586451467823e-16, 2.320820209502452e-17, 3.1341480612634943e-18, 4.1243598710435126e-19, 4.672238760753054e-20, 5.1265643047129325e-21], [1.0828093146265805e-12, 1.9009616127684707e-12, 1.6686479347776565e-12, 9.764833094771401e-13, 4.285743717178195e-13, 1.5047957527644669e-13, 4.4029897083784364e-14, 1.1042591187810272e-14, 2.423273155066307e-15, 4.726952364463396e-16, 8.298557159465246e-17, 1.3244368890857733e-17, 1.9376323934090008e-18, 2.616672667869471e-19, 3.2812757305127683e-20, 4.030106716490015e-21, 4.280123476620207e-22], [8.47526230428271e-14, 1.487902632620149e-13, 1.3060682753377846e-13, 7.64303748756252e-14, 3.354496648797591e-14, 1.177819450458608e-14, 3.446266318316029e-15, 8.643152175683679e-16, 1.896721366051088e-16, 3.6998352939448573e-17, 6.495367903055596e-18, 1.0366506723615662e-18, 1.5166052380219586e-19, 2.0480971972695847e-20, 2.568288999098892e-21, 3.005896317928788e-22, 3.4611394131255517e-23]] |
| Legacy trial inputs | {"lambda_home": 1.2523368153264198, "lambda_away": 1.7555829887038235, "rho": -0.03318537521090455, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2645 |
| Legacy p draw | 0.2487 |
| Legacy p away | 0.4868 |
| Legacy p over 1 5 | 0.8055 |
| Legacy p under 3 5 | 0.6457 |
| Legacy p btts yes | 0.5960 |
| Legacy p over 2 5 | 0.5762 |
| Legacy goal margin distribution | {"-1": 0.21968422226225873, "-10": 4.5979207976796825e-06, "-11": 7.219612803351537e-07, "-12": 1.0417107475705903e-07, "-13": 1.3901357856463441e-08, "-14": 1.7246712286720146e-09, "-15": 1.9849741638333969e-10, "-16": 1.9148673377335506e-11, "-2": 0.14912850354435728, "-3": 0.07483576427368813, "-4": 0.029784456286661834, "-5": 0.009775780292538878, "-6": 0.0027230560343088853, "-7": 0.0006578560711075778, "-8": 0.0001401846142493893, "-9": 2.6705286506700206e-05, "0": 0.2487194075181925, "1": 0.1532692927043905, "10": 1.5444620429175436e-07, "11": 1.7299336393512975e-08, "12": 1.7805839983494435e-09, "13": 1.6950102488306564e-10, "14": 1.5001034418322848e-11, "15": 1.2315995778885954e-12, "16": 8.47526230428271e-14, "2": 0.07470989776777978, "3": 0.02674400621301769, "4": 0.007592883327408182, "5": 0.001777740089947032, "6": 0.00035324270037165426, "7": 6.0876165456209624e-05, "8": 9.253723880783914e-06, "9": 1.257515107289885e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2697 |
| Legacy raw p draw | 0.2417 |
| Legacy raw p away | 0.4886 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2523 |
| Legacy lambda away | 1.7556 |
| Legacy model home team | Milan |
| Legacy model away team | Inter |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 51.6% |
| Market home draw odds | 1.87 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T07:11:46Z |
| Market reference home draw last update utc | 2026-10-30T07:11:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.2% |
| Market draw away odds | 1.30 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T07:11:46Z |
| Market reference draw away last update utc | 2026-10-30T07:11:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.2% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T07:11:46Z |
| Market reference home away last update utc | 2026-10-30T07:11:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.87 |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home away odds | 1.30 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:46Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.75, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:46Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.07, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:46Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.23, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:46Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.23, "price": 1.65, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 80.9% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-30T07:12:06Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:12:04Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market reference under 3 5 last update utc | 2026-10-30T07:12:06Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.3% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T07:11:46Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.52 |
| Market reference btts yes last update utc | 2026-10-30T07:12:06Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 8.169964141798744, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,536.0077 |
| Elo away rating | 1,691.0397 |
| Elo rating diff | -95.0319 |
| Elo home expectancy | 0.3665 |

</details>


---

## 2026-10-31 — Bologna vs Monza

The model's most likely 1X2 outcome is **Bologna win** at **58.7%**. Expected goals are 2.00 for Bologna and 0.98 for Monza (2.98 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.3%; Under 3.5 goals: 68.9%; Double Chance 1X: 81.5%; Double Chance X2: 41.3%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

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
| Bologna expected goals | 2.00 |
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
| Draw | 22.8% | 23.4% | 4.07 | -7.0% |
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
| Market best home last update utc | 2026-10-30T07:12:04Z |
| Market best draw last update utc | 2026-10-30T07:12:04Z |
| Market best away last update utc | 2026-10-30T07:12:04Z |
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
| Dc lambda home | 2.0050 |
| Dc lambda away | 0.9796 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:11:26.876100+00:00 |
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
| Goal margin distribution | {"-1": 0.12278444898461144, "-10": 9.275898626475264e-09, "-11": 7.701482113162163e-10, "-12": 5.873044564532084e-11, "-13": 4.140623779508636e-12, "-14": 2.7136024309394067e-13, "-15": 1.6534899212534604e-14, "-16": 8.618273021591441e-16, "-2": 0.046210053267570265, "-3": 0.012558968060210006, "-4": 0.0026826030604354375, "-5": 0.00047004633332279033, "-6": 6.966729676875532e-05, "-7": 8.935777932275758e-06, "-8": 1.0094129217748753e-06, "-9": 1.0182534115382028e-07, "0": 0.22838299749169183, "1": 0.2382009075278873, "10": 1.1216817784950381e-05, "11": 1.906216186606335e-06, "12": 2.9753996593685024e-07, "13": 4.2937025535698246e-08, "14": 5.759656373973863e-09, "15": 7.18349968369126e-10, "16": 7.663707908067337e-11, "2": 0.18137472807243152, "3": 0.10089704146026113, "4": 0.04411284443783301, "5": 0.015820983830575053, "6": 0.004799609978237912, "7": 0.0012600666760701853, "8": 0.00029134944131996933, "9": 6.015688976515804e-05} |
| Raw goal margin distribution | {"-1": 0.11442110153184563, "-10": 1.3530826596716348e-08, "-11": 1.187474448410815e-09, "-12": 9.574036734441706e-11, "-13": 7.137749027918819e-12, "-14": 4.94821003442241e-13, "-15": 3.204590067511878e-14, "-16": 1.937067727284446e-15, "-17": 1.0005605080760046e-16, "-2": 0.044592340562117444, "-3": 0.012663015318286966, "-4": 0.0028386982820500853, "-5": 0.000523351890664429, "-6": 8.17456072590093e-05, "-7": 1.1061332643204382e-05, "-8": 1.3191683348072786e-06, "-9": 1.405630714980075e-07, "0": 0.21576874838407964, "1": 0.23686529061317269, "10": 1.7464897289484668e-05, "11": 3.137257395015646e-06, "12": 5.177321547155408e-07, "13": 7.900516661533958e-08, "14": 1.1210539575020769e-08, "15": 1.4860555483113277e-09, "16": 1.8386181272090632e-10, "17": 1.943901523413785e-11, "2": 0.18682225493616167, "3": 0.10858995283205258, "4": 0.04982598786756611, "5": 0.018802459036699932, "6": 0.006011314484930789, "7": 0.0016649325658992906, "8": 0.00040641860796252404, "9": 8.86398015918247e-05} |
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
| Totals anchor scale | 0.9446 |
| Totals anchor target over 2 5 | 0.5333 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.08 |
| Totals anchor reference last update utc | 2026-10-30T07:12:04Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5677 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.36, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.8, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.36, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.70 |
| Reference draw odds | 4.07 |
| Reference away odds | 5.00 |
| Market reference 1x2 last update utc | 2026-10-30T07:12:04Z |
| Market reference home last update utc | 2026-10-30T07:12:04Z |
| Market reference draw last update utc | 2026-10-30T07:12:04Z |
| Market reference away last update utc | 2026-10-30T07:12:04Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-30T07:12:04Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:12:04Z |
| Market best over 2 5 last update utc | 2026-10-30T07:12:04Z |
| Market best under 2 5 last update utc | 2026-10-30T07:12:04Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0318 |
| Raw ev home | 0.0355 |
| Raw edge prob draw | -0.0180 |
| Raw ev draw | -0.1218 |
| Raw edge prob away | -0.0138 |
| Raw ev away | -0.1243 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06238475538281032, 0.05268492219688335, 0.026515700398886143, 0.008333842012987215, 0.0019644848614016343, 0.0003704606604888482, 5.821759504928347e-05, 7.84186994688479e-06, 9.242576696155589e-07, 9.68308999573121e-08, 9.130138862032525e-09, 7.826149004158623e-10, 6.149365129866148e-11, 4.460159020580449e-12, 3.003901737284785e-13, 1.8882429748769333e-14, 1.1127594970642218e-15], [0.10523130152020255, 0.10933892282583454, 0.05055000433887864, 0.015887785107638698, 0.0037451289905087912, 0.0007062528129893105, 0.0001109870619319557, 1.4949880782956812e-05, 1.7620213121457283e-06, 1.8460015535494845e-07, 1.74058596283467e-08, 1.4919910097247433e-09, 1.1723259401782228e-10, 8.502926735885938e-12, 5.726691868176702e-13, 3.5997800977150785e-14, 2.1213845592812536e-15], [0.10354744927295448, 0.097634390580706, 0.047557395047317735, 0.015144378501124663, 0.0035698903644240964, 0.0006732064818935466, 0.00010579385756024444, 1.4250359731699394e-05, 1.6795744339060496e-06, 1.7596251492082612e-07, 1.659142067715849e-08, 1.4221791406709726e-09, 1.1174715446151022e-10, 8.105065620108176e-12, 5.458733777138202e-13, 3.431342503141088e-14, 2.022122686991181e-15], [0.06580156826943616, 0.06204398140514245, 0.02925048543553996, 0.009498544402301932, 0.0022685675618125444, 0.0004278042828556215, 6.722909921602167e-05, 9.055713350095606e-06, 1.067323556034082e-06, 1.1181935933450973e-07, 1.0543393468796244e-08, 9.037558961934911e-10, 7.101225636018496e-11, 5.150547236793279e-12, 3.4688758228528754e-13, 2.1805241902296632e-14, 1.285003589866114e-15], [0.031361320948406324, 0.029570438287979416, 0.013940911831834584, 0.004381606179574049, 0.001067133080794537, 0.00020389342945143323, 3.204168856512231e-05, 4.315993376118811e-06, 5.086911676560564e-07, 5.3293605434683727e-08, 5.025028356563264e-09, 4.307340913742865e-10, 3.384475813499259e-11, 2.4547737873297573e-12, 1.6532816902661388e-13, 1.0392475554008898e-14, 6.124384427531034e-16], [0.011957556362203435, 0.011274722230778375, 0.005315440610550616, 0.00167063443964716, 0.0003938082892030562, 7.672909625858458e-05, 1.2216969354955989e-05, 1.6456173558103887e-06, 1.939555836378593e-07, 2.0319976055174593e-08, 1.915960743303102e-09, 1.6423183140798945e-10, 1.290445015470187e-11, 9.359649093462941e-13, 6.303691425013435e-14, 3.962480164158955e-15, 2.335127149027974e-16], [0.003799349799670396, 0.0035823886044350295, 0.0016889084698517758, 0.0005308212172563218, 0.00012512719149052485, 2.35963650906533e-05, 3.831237639464498e-06, 5.228723814252807e-07, 6.162673087360342e-08, 6.456394150778528e-09, 6.08770290998118e-10, 5.218241560890844e-11, 4.10021233645171e-12, 2.9739003380855347e-13, 2.0029116340619533e-14, 1.2590238140530131e-15, 7.419546767856077e-17], [0.0010347354638360587, 0.000975647079027224, 0.0004599664629669877, 0.00014456671994228883, 3.4077815771710124e-05, 6.426361631413953e-06, 1.0098975653831194e-06, 1.4054795121323764e-07, 1.6783757041989126e-08, 1.758369286474702e-09, 1.6579579208005458e-10, 1.4211641166563307e-11, 1.1166739935745717e-12, 8.099280950646088e-14, 5.4548378221808546e-15, 3.4288935183799237e-16, 2.0206794770402324e-17], [0.00024657976877683004, 0.0002324988748935339, 0.00010961103397676334, 3.445057178579723e-05, 8.120819501301092e-06, 1.5314163093200095e-06, 2.406608421801493e-07, 3.241684964978167e-08, 3.947535586115559e-09, 4.1902332261408504e-10, 3.9509507022896916e-11, 3.3866657858608727e-12, 2.6610590315897693e-13, 1.93007671416326e-14, 1.2999000188144415e-15, 8.171129728056285e-17, 4.815324260497265e-18], [5.223156341353507e-05, 4.924888926539649e-05, 2.321827009726042e-05, 7.29746496960578e-06, 1.720186132285549e-06, 3.2439104176938483e-07, 5.097779149458095e-08, 6.866673395585989e-09, 8.093191539266298e-10, 8.760371898951164e-11, 8.36906990277728e-12, 7.173777866372279e-13, 5.6367671299682736e-14, 4.088369649662777e-15, 2.7535028766050896e-16, 1.7308430560556884e-17, 1.0200022317991976e-18], [9.957518441758843e-06, 9.388896120410697e-06, 4.426372437844685e-06, 1.3912017420889354e-06, 3.2793935344949846e-07, 6.184248698791525e-08, 9.718497126124436e-09, 1.30907486779084e-09, 1.542900475080314e-10, 1.6164371306622068e-11, 1.574722569267439e-12, 1.3676218120434917e-13, 1.074603342890064e-14, 7.794140845627994e-16, 5.2493270125102567e-17, 3.2997100841133486e-18, 1.944550453786288e-19], [1.7257446201281162e-06, 1.6271962802288835e-06, 7.671377628846817e-07, 2.411101657471565e-07, 5.683540314325546e-08, 1.0717965509073817e-08, 1.684319665510692e-09, 2.2687669861206166e-10, 2.6740118131206284e-11, 2.801458715172511e-12, 2.641481913010432e-13, 2.3393768620818663e-14, 1.8624027147035334e-15, 1.3508081066116969e-16, 9.097646069267672e-18, 5.718751071311364e-19, 3.370114254688362e-20], [2.7416586124114334e-07, 2.585096684492156e-07, 1.2187375988242616e-07, 3.8304726826357736e-08, 9.029335551746595e-09, 1.7027433898823014e-09, 2.6758475519155984e-10, 3.6043482184464494e-11, 4.248153192323339e-12, 4.4506257323274094e-13, 4.196473540677441e-14, 3.59712242252135e-15, 2.920244445697376e-16, 2.1460038965279827e-17, 1.445326232373075e-18, 9.085274231209218e-20, 5.354038287826707e-21], [4.0205745353259476e-08, 3.7909803408685516e-08, 1.7872485410454827e-08, 5.617293435567945e-09, 1.3241297230049774e-09, 2.497031060892712e-10, 3.924064243061799e-11, 5.285687502422907e-12, 6.229811570958528e-13, 6.526732542358072e-14, 6.154024640207417e-15, 5.275091051441592e-16, 4.1448815951966776e-17, 3.1060898218138604e-18, 2.1195351670741613e-19, 1.3323329919739527e-20, 7.851564707490211e-22], [5.47492502145872e-09, 5.162280400902133e-09, 2.4337446479256057e-09, 7.649220307458748e-10, 1.8031032352318862e-10, 3.400274690724719e-11, 5.343504347795609e-12, 7.197663544939295e-13, 8.483302808873007e-14, 8.887628121444138e-15, 8.38010169673763e-16, 7.183234071214451e-17, 5.644197304922319e-18, 4.0937587851500857e-19, 2.8486523274059123e-20, 1.8142738483224747e-21, 1.0691687891107692e-22], [6.958329830412472e-10, 6.560975641814422e-10, 3.0931561467768544e-10, 9.721740048707692e-11, 2.291645452650309e-11, 4.321562892520199e-12, 6.791301352342231e-13, 9.147836136152115e-14, 1.0781813223749922e-14, 1.1295688550375848e-15, 1.065065026274338e-16, 9.129497065377045e-18, 7.17346563133582e-19, 5.2029431931167024e-20, 3.5041643189581444e-21, 2.275822768817682e-22, 1.358854970589763e-23], [8.290927587883828e-11, 7.81747564112357e-11, 3.685530041829662e-11, 1.1583561678807023e-11, 2.7305211118313297e-12, 5.149190377807495e-13, 8.091911293665894e-14, 1.0899748767179141e-14, 1.2846650688143655e-15, 1.3458938870235068e-16, 1.2690368557456957e-17, 1.0877897559844784e-18, 8.547264293744053e-20, 6.1993648345707375e-21, 4.1752508622900453e-22, 2.624549269109666e-23, 1.5980117977617553e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9064178422004692, "lambda_away": 0.9428951776816685, "rho": -0.03318537521090455, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T07:12:04Z", "over": 1.83, "under": 2.08, "bookmaker": "pinnacle", "event_id": "04aa939b89001eedf55668e66c74836e", "kickoff_utc": "2026-10-31T14:00:00Z", "home_team": "Bologna", "away_team": "Monza"}} |
| Legacy p home | 0.5866 |
| Legacy p draw | 0.2299 |
| Legacy p away | 0.1835 |
| Legacy p over 1 5 | 0.7797 |
| Legacy p under 3 5 | 0.6820 |
| Legacy p btts yes | 0.5246 |
| Legacy p over 2 5 | 0.5403 |
| Legacy goal margin distribution | {"-1": 0.12086452308117511, "-10": 1.073919693830023e-08, "-11": 9.08310073624347e-10, "-12": 7.056486909260628e-11, "-13": 5.068426636019396e-12, "-14": 3.384100973926205e-13, "-15": 2.1003814308050587e-14, "-16": 1.1127594970642218e-15, "-2": 0.04643493088506342, "-3": 0.012823923159199096, "-4": 0.0027861168796971753, "-5": 0.0004968206685933845, "-6": 7.496406306819136e-05, "-7": 9.790841108889274e-06, "-8": 1.1263878026437249e-06, "-9": 1.1573247007262216e-07, "0": 0.22992745565764602, "1": 0.2369162315104826, "10": 1.1712390488111248e-05, "11": 2.0029151273920965e-06, "12": 3.146093572193534e-07, "13": 4.56889249305181e-08, "14": 6.167877886058459e-09, "15": 7.740077394524829e-10, "16": 8.290927587883828e-11, "2": 0.18133477818735017, "3": 0.1012539299313613, "4": 0.04447797352920992, "5": 0.016036145751005645, "6": 0.004892244307919366, "7": 0.0012919023886868003, "8": 0.0003005054251207436, "9": 6.242726084615661e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5959 |
| Legacy raw p draw | 0.2261 |
| Legacy raw p away | 0.1781 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9064 |
| Legacy lambda away | 0.9429 |
| Legacy model home team | Bologna |
| Legacy model away team | Monza |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 80.6% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T07:11:45Z |
| Market reference home draw last update utc | 2026-10-30T07:11:45Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.2% |
| Market draw away odds | 2.24 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T07:11:45Z |
| Market reference draw away last update utc | 2026-10-30T07:11:45Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.2% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T07:11:45Z |
| Market reference home away last update utc | 2026-10-30T07:11:45Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.24 |
| Market reference dc home away odds | 1.27 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:45Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.09, "price": 1.74, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:45Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.74, "price": 2.09, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:45Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.67, "price": 2.19, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:45Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.19, "price": 1.67, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 77.0% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:12:04Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-30T07:12:06Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.8% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:12:04Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 3.15 |
| Market reference under 3 5 last update utc | 2026-10-30T07:12:06Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.2% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T07:11:45Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-30T07:12:06Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 8.813892049007379, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,462.4109 |
| Elo away rating | 1,358.1569 |
| Elo rating diff | 164.2540 |
| Elo home expectancy | 0.7202 |

</details>


---

## 2026-10-31 — Udinese vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **61.1%**. Expected goals are 0.86 for Udinese and 1.73 for AS Roma (2.60 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 60.6%; Under 3.5 goals: 61.5%; Double Chance 1X: 38.9%; Double Chance X2: 83.0%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 79.2%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 17.0% | 5.87 |
| Draw | 21.8% | 4.58 |
| AS Roma win | 61.1% | 1.64 |

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
| 1 | 1-1 | 10.13% |
| 2 | 1-2 | 9.90% |
| 3 | 0-2 | 9.46% |
| 4 | 0-1 | 8.77% |
| 5 | 1-3 | 6.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 17.0% | 16.5% | 5.67 | -3.3% |
| Draw | 21.8% | 20.8% | 4.54 | -1.0% |
| AS Roma win | 61.1% | 62.6% | 1.57 | -4.0% |

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
| Market best home last update utc | 2026-10-30T07:12:04Z |
| Market best draw last update utc | 2026-10-30T07:12:04Z |
| Market best away last update utc | 2026-10-30T07:12:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Udinese |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8643 |
| Dc lambda away | 1.7317 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:11:26.876100+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.07 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.68 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.60 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.80 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.23047107337330602, "-10": 2.386699341958616e-05, "-11": 4.478897513983983e-06, "-12": 7.723691301649761e-07, "-13": 1.2318588053244922e-07, "-14": 1.827200030189891e-08, "-15": 2.5320399289470046e-09, "-16": 3.2712772127791734e-10, "-17": 3.575340977548821e-11, "-2": 0.18592849752723856, "-3": 0.11151842337911215, "-4": 0.053047825273663536, "-5": 0.020809562533385558, "-6": 0.006927832270596241, "-7": 0.002000313410028396, "-8": 0.0005094386212031191, "-9": 0.0001159876249219086, "0": 0.21816366400499526, "1": 0.10897127838257276, "10": 2.1919643765296348e-08, "11": 2.053054199263601e-09, "12": 1.7670454024510515e-10, "13": 1.4066214767049291e-11, "14": 1.0413480707272017e-12, "15": 7.202344394165301e-14, "16": 4.644235071359476e-15, "17": 2.533423664416235e-16, "2": 0.04434387577990327, "3": 0.013274794942083504, "4": 0.003151681307528362, "5": 0.0006170653682425163, "6": 0.00010253192195012263, "7": 1.477587782310303e-05, "8": 1.878194750662158e-06, "9": 2.1342924237522824e-07} |
| Raw goal margin distribution | {"-1": 0.2502654519783257, "-10": 5.704850436170078e-06, "-11": 8.881104277083829e-07, "-12": 1.2695164525341523e-07, "-13": 1.6773653507464083e-08, "-14": 2.059903114703582e-09, "-15": 2.354577381990781e-10, "-16": 2.330363140333592e-11, "-2": 0.17913914189113617, "-3": 0.09262130483730925, "-4": 0.03742560044856197, "-5": 0.012365581115001124, "-6": 0.0034490868168216273, "-7": 0.0008314651470186234, "-8": 0.00017637120945107956, "-9": 3.338740968419134e-05, "0": 0.24130248530979423, "1": 0.12347683221366963, "10": 5.472419409156792e-09, "11": 4.252022872531145e-10, "12": 3.0336150302049475e-11, "13": 2.00052191167232e-12, "14": 1.2261848626364546e-13, "15": 6.995449651341362e-15, "16": 3.455570683164973e-16, "2": 0.04462492629743265, "3": 0.011515728798054332, "4": 0.0023224310082959614, "5": 0.000382985283696146, "6": 5.331693716158796e-05, "7": 6.415029050862929e-06, "8": 6.791657589941816e-07, "9": 6.416886040705703e-08} |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 57.6% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 47.9% |
| P home draw | 38.9% |
| P draw away | 83.0% |
| P home away | 78.2% |
| Raw p home draw | 42.4% |
| Raw p draw away | 81.8% |
| Raw p home away | 75.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2116 |
| Totals anchor target over 2 5 | 0.6057 |
| Totals anchor reference over odds | 1.61 |
| Totals anchor reference under odds | 2.42 |
| Totals anchor reference last update utc | 2026-10-30T07:12:04Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4903 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.52, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.61, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.45, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.02, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.67 |
| Reference draw odds | 4.54 |
| Reference away odds | 1.57 |
| Market reference 1x2 last update utc | 2026-10-30T07:12:04Z |
| Market reference home last update utc | 2026-10-30T07:12:04Z |
| Market reference draw last update utc | 2026-10-30T07:12:04Z |
| Market reference away last update utc | 2026-10-30T07:12:04Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.46 |
| Market reference over 2 5 last update utc | 2026-10-30T07:12:06Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:12:06Z |
| Home probability edge | +0.5% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0170 |
| Raw ev home | 0.0341 |
| Raw edge prob draw | 0.0331 |
| Raw ev draw | 0.0955 |
| Raw edge prob away | -0.0501 |
| Raw ev away | -0.0952 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07376970208947435, 0.13266383733493703, 0.11373491816481536, 0.06305675962880722, 0.026219882594388802, 0.00872207512483036, 0.002417840551895556, 0.000574498239145091, 0.00011944220151605906, 2.207366131721443e-05, 3.6714148432153554e-06, 5.551365970542056e-07, 7.694452048331054e-08, 9.844494707162311e-09, 1.1695653111004243e-09, 1.296857638484947e-10], [0.05991518283938144, 0.1090302626728965, 0.10269463644754201, 0.056935821558832984, 0.023674710934649255, 0.007875420745585037, 0.0021831400635047137, 0.0005187315273156766, 0.00010784791213733275, 1.9930964567562078e-05, 3.3150295323177936e-06, 5.012493254762242e-07, 6.947549341191241e-08, 8.888886731309376e-09, 1.0560352648345305e-09, 1.1709712888300094e-10], [0.028629845728222282, 0.04761876113573785, 0.039620672607896305, 0.0257045223673238, 0.010688299915560057, 0.003555475677079626, 0.0009856110100276887, 0.00023418905324381424, 4.868954190708727e-05, 8.998130008536906e-06, 1.4966193238074398e-06, 2.2629645354279952e-07, 3.136574348965913e-08, 4.013019950356766e-09, 4.767628066554291e-10, 5.286523819476769e-11], [0.008616912747787805, 0.014332131362479416, 0.011919001352549408, 0.006611383680706727, 0.0032169278405779094, 0.0010701148716311742, 0.0002966458204940861, 7.048541782045723e-05, 1.4654411285546953e-05, 2.708226300373715e-06, 4.504473496757002e-07, 6.81099302393342e-08, 9.440353870068457e-09, 1.2078249773196796e-09, 1.434944339322974e-10, 1.5911198028785824e-11], [0.0019451166277974505, 0.0032352267965221073, 0.002690505102716293, 0.0014916662031286734, 0.0006205623252771876, 0.00024155962714111367, 6.696258101926341e-05, 1.5910844432655997e-05, 3.3079758257292185e-06, 6.113344956460977e-07, 1.0168057347759895e-07, 1.5374619855662927e-08, 2.1309939908207084e-09, 2.7264526352047977e-10, 3.23913468323966e-11, 3.591673347500797e-12], [0.0003512607177511872, 0.0005842364773371143, 0.0004858673973516454, 0.0002693739458437901, 0.00011200945426927303, 3.727849957239957e-05, 1.2092500745280665e-05, 2.8732748235105867e-06, 5.973739292769129e-07, 1.1039841552836151e-07, 1.836208210380533e-08, 2.7764402033656255e-09, 3.8482755637473036e-10, 4.9235901635425214e-11, 5.849421867396668e-12, 6.486057133754111e-13], [5.286062288494288e-05, 8.792074531379989e-05, 7.311735120260888e-05, 4.0537623043758324e-05, 1.6856110639363647e-05, 5.607205248906995e-06, 1.5551380598286202e-06, 4.3239419956426535e-07, 8.98977779211029e-08, 1.6613668182713314e-08, 2.7632782386989e-09, 4.178217236823614e-10, 5.791203885106212e-11, 7.409426381101673e-12, 8.802694631126271e-13, 9.760756123046745e-14], [6.81848954085785e-06, 1.134089327042971e-05, 9.431404081547979e-06, 5.228946305395073e-06, 2.174269008222035e-06, 7.232731711530019e-07, 2.0049806706358034e-07, 4.7663496392573176e-08, 1.1595910623974182e-08, 2.1429963658521503e-09, 3.5643514474013965e-10, 5.389480670843325e-11, 7.470071475608706e-12, 9.557415998154784e-13, 1.1354592132662286e-13, 1.2590395251436957e-14], [7.695770962628422e-07, 1.2800036811358153e-06, 1.0644868666684267e-06, 5.901713700823507e-07, 2.454015100874211e-07, 8.163310415384398e-08, 2.2629457643443126e-08, 5.3769399966322035e-09, 1.1184561198032859e-09, 2.4187188535700695e-10, 4.022948514498001e-11, 6.082902760470464e-12, 8.431186820228754e-13, 1.0787093545516562e-13, 1.2815498198452579e-14, 1.4210302384922775e-15], [7.720822475658493e-08, 1.2841703889357525e-07, 1.067952017429823e-07, 5.920925142847172e-08, 2.4620034871676807e-08, 8.189883877384843e-09, 2.270312175789912e-09, 5.394443178969837e-10, 1.1215424614847598e-10, 2.0737049208947894e-11, 4.036044141644348e-12, 6.102704014757343e-13, 8.458632281835084e-14, 1.0822208027980294e-14, 1.285721560684018e-15, 1.4256560203286376e-16], [6.971359983437737e-09, 1.1595155942992778e-08, 9.642856032519896e-09, 5.3461792102990575e-09, 2.2230160897542324e-09, 7.394889457930854e-10, 2.0499323099464725e-10, 4.870803004389967e-11, 1.0126740072539068e-11, 1.8714845152836253e-12, 3.1142966974481346e-13, 5.510312754032809e-14, 7.637550376285587e-15, 9.771693134579662e-16, 1.1609161933529913e-16, 1.2872671741385305e-17], [5.722407303802421e-10, 9.517827972525689e-10, 7.915291983357943e-10, 4.388385484773929e-10, 1.8247520625390083e-10, 6.070059435376881e-11, 1.682677074574717e-11, 3.998175213146754e-12, 8.312485869683934e-13, 1.5361990608224337e-13, 2.555092221895479e-14, 3.865339473625186e-15, 6.269246482787932e-16, 8.021047298759686e-17, 9.529324722476502e-18, 1.0566470669619553e-18], [4.3057762965486075e-11, 7.161608026659857e-11, 5.9557935660325e-11, 3.3020030202851787e-11, 1.3730190391616915e-11, 4.567364161254294e-12, 1.2661159329982098e-12, 3.0083926481039364e-13, 6.25465869919771e-14, 1.155899807843851e-14, 1.9225572281831282e-15, 2.9070043099810606e-16, 4.0312355637584615e-17, 6.0353682460781294e-18, 7.170258657556518e-19, 7.950650230226053e-20], [2.990625641646244e-12, 4.974175880227767e-12, 4.1366638042031515e-12, 2.2934435560838985e-12, 9.53645907772043e-13, 3.1723144526416954e-13, 8.793951459012029e-14, 2.089513150223667e-14, 4.3442439637563385e-15, 8.028432892072713e-16, 1.3353338743458536e-16, 2.0190927328886515e-17, 2.798556660970499e-18, 3.58232100103741e-19, 4.9801842737889257e-20, 5.522214069814536e-21], [1.92880338381281e-13, 3.2080936964688347e-13, 2.667940457720053e-13, 1.479155943143474e-13, 6.150537293117793e-14, 2.0459835445687533e-14, 5.67165715929964e-15, 1.3476310704185108e-15, 2.801819238328045e-16, 5.1779361192194434e-17, 8.612233037433492e-18, 1.3022134369461647e-18, 1.804928534786596e-19, 2.3092754748360438e-20, 2.744867940033586e-21, 3.56155081253627e-22], [1.1610492507522775e-14, 1.9311220697182952e-14, 1.6059751322938258e-14, 8.903825625490399e-15, 3.702335228063554e-15, 1.2315862163084949e-15, 3.414071828467778e-16, 8.112107525998368e-17, 1.686563884481344e-17, 3.1168748987669436e-18, 5.184160707790727e-19, 7.838714655804574e-20, 1.0864823965793922e-20, 1.3900756201178497e-21, 1.651465385941461e-22, 1.832111764888761e-23]] |
| Legacy trial inputs | {"lambda_home": 0.9029297079963192, "lambda_away": 1.6632559458326728, "rho": -0.03318537521090455, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1825 |
| Legacy p draw | 0.2297 |
| Legacy p away | 0.5878 |
| Legacy p over 1 5 | 0.7337 |
| Legacy p under 3 5 | 0.7397 |
| Legacy p btts yes | 0.4792 |
| Legacy p over 2 5 | 0.4823 |
| Legacy goal margin distribution | {"-1": 0.26453402035434104, "-10": 4.205270777111104e-06, "-11": 6.287721965237545e-07, "-12": 8.632608121930413e-08, "-13": 1.0953395210191609e-08, "-14": 1.2866624399834253e-09, "-15": 1.296857638484947e-10, "-2": 0.1824990824483041, "-3": 0.09060011725566393, "-4": 0.03515482096009035, "-5": 0.011154688774843149, "-6": 0.0029880743633131134, "-7": 0.0006918104956124418, "-8": 0.00014094007646042026, "-9": 2.5624706249238044e-05, "0": 0.2296914658168882, "1": 0.12106243417937418, "10": 7.985056896865862e-09, "11": 6.481450923805863e-10, "12": 4.830763671711134e-11, "13": 3.3274947626160657e-12, "14": 2.1219155907846395e-13, "15": 1.1610492507522775e-14, "2": 0.04593945870225656, "3": 0.01238080278668084, "4": 0.0026079532030912978, "5": 0.00044922841517244143, "6": 6.532749727744797e-05, "7": 8.210821734821375e-06, "8": 9.080898829120299e-07, "9": 8.962890437526675e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1997 |
| Legacy raw p draw | 0.2511 |
| Legacy raw p away | 0.5492 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9029 |
| Legacy lambda away | 1.6633 |
| Legacy model home team | Udinese |
| Legacy model away team | Roma |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 38.2% |
| Market home draw odds | 2.54 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T07:11:46Z |
| Market reference home draw last update utc | 2026-10-30T07:11:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 82.9% |
| Market draw away odds | 1.17 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T07:11:46Z |
| Market reference draw away last update utc | 2026-10-30T07:11:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.9% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T07:11:46Z |
| Market reference home away last update utc | 2026-10-30T07:11:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.54 |
| Market reference dc draw away odds | 1.17 |
| Market reference dc home away odds | 1.23 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:46Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.22, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:46Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.22, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:46Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.77, "price": 2.05, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T07:11:46Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.05, "price": 1.77, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 81.5% |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.85 |
| Market reference over 1 5 last update utc | 2026-10-30T07:12:06Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:12:04Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.63 |
| Market reference under 3 5 last update utc | 2026-10-30T07:12:06Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.5% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T07:11:46Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.18 |
| Market reference btts yes last update utc | 2026-10-30T07:12:06Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 8.940795928529967, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,376.7934 |
| Elo away rating | 1,594.6836 |
| Elo rating diff | -157.8902 |
| Elo home expectancy | 0.2872 |

</details>


---

## 2026-11-01 — Como vs Venezia

The model's most likely 1X2 outcome is **Como win** at **75.2%**. Expected goals are 2.14 for Como and 0.58 for Venezia (2.72 combined). The most likely exact score is 2-0 at 15.5%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 52.2%; Under 3.5 goals: 70.6%; Double Chance 1X: 90.7%; Double Chance X2: 24.8%; Double Chance 12 (either team wins): 84.5%; Under 4.5 goals: 85.6%; BTTS Yes (both teams score): 38.3%; BTTS No (at least one team does not score): 61.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 75.2% | 1.33 |
| Draw | 15.5% | 6.46 |
| Venezia win | 9.3% | 10.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.14 |
| Venezia expected goals | 0.58 |
| Expected total goals | 2.72 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 52.2% |
| Under 2.5 | 47.8% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.4% |
| Under 4.5 | 85.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 15.45% |
| 2 | 1-0 | 14.22% |
| 3 | 3-0 | 11.03% |
| 4 | 2-1 | 8.96% |
| 5 | 1-1 | 7.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 75.2% | 76.0% | 1.30 | -2.2% |
| Draw | 15.5% | 14.4% | 6.37 | -1.3% |
| Venezia win | 9.3% | 9.7% | 9.32 | -13.3% |

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
| Market best home last update utc | 2026-10-30T07:12:04Z |
| Market best draw last update utc | 2026-10-30T07:12:04Z |
| Market best away last update utc | 2026-10-30T07:12:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Como |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1414 |
| Dc lambda away | 0.5798 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:11:26.876100+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 38.3% |
| P btts no | 61.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.20 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.17 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.09 |
| Fair Over 3.5 odds | 3.41 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.97 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.07140583067395337, "-10": 9.547780662768512e-11, "-11": 4.9863651676476576e-12, "-12": 2.390515759630627e-13, "-13": 1.059061863918033e-14, "-14": 4.360680459950948e-16, "-15": 1.6769290224437772e-17, "-16": 6.035580640265056e-19, "-17": 1.9185059135646615e-20, "-2": 0.01797738395731722, "-3": 0.0031655712128823886, "-4": 0.0004330369162495962, "-5": 4.827655363171147e-05, "-6": 4.534263050579795e-06, "-7": 3.675790398626496e-07, "-8": 2.6196473978536116e-08, "-9": 1.665036287188325e-09, "0": 0.15488961108317462, "1": 0.25233878722055886, "10": 4.21313598109582e-05, "11": 8.125995117614661e-06, "12": 1.4387108610331959e-06, "13": 2.3539252894045566e-07, "14": 3.5794396371671384e-08, "15": 5.083524188268572e-09, "16": 6.757074451952756e-10, "17": 7.932173841317298e-11, "2": 0.22925249151484692, "3": 0.1490833325190219, "4": 0.07531671328084846, "5": 0.031009312059293245, "6": 0.010756030329952777, "7": 0.0032202195302534512, "8": 0.0008475532904867225, "9": 0.00019894696194542818} |
| Raw goal margin distribution | {"-1": 0.06518231449375653, "-10": 8.715624984739475e-11, "-11": 4.551768664696466e-12, "-12": 2.182165637957669e-13, "-13": 9.667572357985326e-15, "-14": 3.9806167432624406e-16, "-15": 1.5307729619971983e-17, "-16": 5.509537690872213e-19, "-17": 1.751294742121371e-20, "-2": 0.016410529557893704, "-3": 0.0028896696026498065, "-4": 0.00039529472867940157, "-5": 4.406891526639389e-05, "-6": 4.1390704004248905e-06, "-7": 3.3554196277111627e-07, "-8": 2.3913268557763744e-08, "-9": 1.5199167615679714e-09, "0": 0.1808154996134595, "1": 0.2463606895749103, "10": 4.113323587738427e-05, "11": 7.933484117557013e-06, "12": 1.4046267073212507e-06, "13": 2.298159010325462e-07, "14": 3.494639991803913e-08, "15": 4.963091636791961e-09, "16": 6.596994222838461e-10, "17": 7.744254614598473e-11, "2": 0.2238213257599522, "3": 0.14555143506895446, "4": 0.07353240310284687, "5": 0.030274677889664734, "6": 0.010501211796899388, "7": 0.003143930082228748, "8": 0.000827474108898235, "9": 0.0001942337572181052} |
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
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5218 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.88, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.30 |
| Reference draw odds | 6.37 |
| Reference away odds | 9.32 |
| Market reference 1x2 last update utc | 2026-10-30T07:12:04Z |
| Market reference home last update utc | 2026-10-30T07:12:04Z |
| Market reference draw last update utc | 2026-10-30T07:12:04Z |
| Market reference away last update utc | 2026-10-30T07:12:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-30T07:11:19Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:11:19Z |
| Home probability edge | -0.8% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -17.3% |
| Under 2.5 probability edge | +17.3% |
| Raw edge prob home | -0.0255 |
| Raw ev home | -0.0455 |
| Raw edge prob draw | 0.0370 |
| Raw ev draw | 0.1518 |
| Raw edge prob away | -0.0116 |
| Raw ev away | -0.2085 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06013600984176558, 0.037972389145442945, 0.012396070293307035, 0.0025074228497015184, 0.00038039289055580137, 4.616652550729451e-05, 4.669181369954781e-06, 4.0476924585458e-07, 3.0703106868680735e-08, 2.0701633635439125e-09, 1.2562307564117905e-10, 6.930132538180544e-12, 3.5044922032823823e-13, 1.63586156788653e-14, 7.090605404800682e-16, 2.868513260983002e-17, 1.087931829161627e-18, 3.883448633997811e-20], [0.1387737015091622, 0.0768802321245843, 0.026359118813464748, 0.0053318071975248715, 0.0008088709696468408, 9.816892791489478e-05, 9.928590559760367e-06, 8.607050775823743e-07, 6.528737113817651e-08, 4.4020145716984455e-09, 2.6712607287541547e-10, 1.4736298088402134e-11, 7.451984716241649e-13, 3.478511206376696e-14, 1.507752907995769e-15, 6.099633196261784e-17, 2.3133883293082635e-18, 8.257801184364439e-20], [0.15057713158762198, 0.09137424960937107, 0.024004248027474424, 0.005668802131830714, 0.0008599953650309388, 0.00010437365929169934, 1.0556123514250784e-05, 9.151056289022393e-07, 6.941383568061617e-08, 4.680242301330442e-09, 2.8400967913593774e-10, 1.566770044828449e-11, 7.922984699336272e-13, 3.6983692417571253e-14, 1.6030498820527734e-15, 6.48515829349677e-17, 2.459605197093927e-18, 8.779732504185503e-20], [0.106729536274945, 0.06476635054376963, 0.01965098092412099, 0.0034415751491062817, 0.0006095673728181138, 7.398037230533822e-05, 7.482212973896522e-06, 6.486296981855687e-07, 4.920074127555239e-08, 3.31737020893312e-09, 2.0130693839213986e-10, 1.1105314503664071e-11, 5.615836043347486e-13, 2.621415549522301e-14, 1.1362467111251725e-15, 4.596700242837021e-17, 1.7433757658779776e-18, 6.223101535471207e-20], [0.05673766889447704, 0.03442994208453874, 0.01044650701238171, 0.0021130737211578878, 0.00027755492340486647, 3.9328137412096906e-05, 3.977561761509865e-06, 3.448130511498968e-07, 2.6155228114772953e-08, 1.7635216930951337e-09, 1.0701523510072053e-10, 5.9036109334791585e-12, 2.985391458764528e-13, 1.3935505828534677e-14, 6.040313855780571e-16, 2.443616504745125e-17, 9.267825984760749e-19, 3.308215202085201e-20], [0.024129501046731453, 0.014642429619604103, 0.00444270987514062, 0.0008986519108024755, 0.00013633153179342698, 1.432585621058524e-05, 1.6915848422728173e-06, 1.4664273384446364e-07, 1.1123343917189865e-08, 7.499937760681394e-10, 4.551163764203234e-11, 2.51069860596171e-12, 1.2696328159540223e-13, 5.926517761978262e-15, 2.568835878271893e-16, 1.039225758793861e-17, 3.941438221864943e-19, 1.406923896185981e-20], [0.008551532460839988, 0.0051892996856879, 0.001574503245540824, 0.0003184836259705515, 4.831610555517281e-05, 5.863902230840474e-06, 5.134873488599699e-07, 5.1970411497054865e-08, 3.942130274335747e-09, 2.65798953283513e-10, 1.6129394714299174e-11, 8.897954660017973e-13, 4.499598320724173e-14, 2.1003670537218595e-15, 9.103994051542221e-17, 3.6830321494238226e-18, 1.396851796951648e-19, 4.986160030770978e-21], [0.002597722559753322, 0.0015763678527284865, 0.000478291185828518, 9.674664791186146e-05, 1.467711640864971e-05, 1.7812937251887441e-06, 1.8015614960572422e-07, 1.3522136917435942e-08, 1.1975117669286876e-09, 8.0742479838003e-11, 4.899670639896662e-12, 2.702956184969032e-13, 1.3668553702040449e-14, 6.38034282650662e-16, 2.7655453382010838e-17, 1.1188048161738776e-18, 4.243255161796853e-20, 1.514659560469211e-21], [0.0006904776672846712, 0.00041900040235161583, 0.00012713035155881102, 2.5715371149618428e-05, 3.901194552998131e-06, 4.7346993677182394e-07, 4.788571337601234e-08, 4.151191087829772e-09, 2.726321171109452e-10, 2.1461444725882494e-11, 1.302338135070243e-12, 7.184488868385224e-14, 3.633117416602161e-15, 1.6959025184510532e-16, 7.350851563118468e-18, 2.973796168948662e-19, 1.1278621401699454e-20, 4.025982667458215e-22], [0.0001631375682360627, 9.899626007946334e-05, 3.0036795373643214e-05, 6.075711517410996e-06, 9.217262523416267e-07, 1.1186565153017875e-07, 1.131384721555524e-08, 9.807923578686313e-10, 7.439639470644137e-11, 4.343138292408067e-12, 3.0770043180680447e-13, 1.697462638605817e-14, 8.583882847237761e-16, 4.006869822647794e-17, 1.7367687693467414e-18, 7.026119719987858e-20, 2.664773903208484e-21, 9.512096527502725e-23], [3.4689723777993234e-05, 2.1050656536952215e-05, 6.387052019679755e-06, 1.291944930727296e-06, 1.9599672496275296e-07, 2.3787215868094047e-08, 2.405786962608837e-09, 2.0855659641068737e-10, 1.581971835396347e-11, 1.066647798805176e-12, 5.604221852422879e-14, 3.609500294346211e-15, 1.8252848079876385e-16, 8.520245144324911e-18, 3.6930812152173206e-19, 1.494040612183226e-20, 5.666399936729755e-22, 2.0226610256394366e-23], [6.705868209071935e-06, 4.069301022823144e-06, 1.2346806034711206e-06, 2.497457891069146e-07, 3.7888113938910506e-08, 4.5983051261243305e-09, 4.650625186180599e-10, 4.031606185777417e-11, 3.0581087086549392e-12, 2.061936154366799e-13, 1.2512382648095674e-14, 5.976426873466522e-16, 3.5284568550388024e-17, 1.6470480253023563e-18, 7.139092854454327e-20, 2.888128919221232e-21, 1.095371396981514e-22, 3.910004690832675e-24], [1.1882850282924034e-06, 7.210832856055959e-07, 2.187863569765577e-07, 4.425514680907966e-08, 6.7138030662363575e-09, 8.148232214736534e-10, 8.240943765434944e-11, 7.1440373135417746e-12, 5.418992261835991e-13, 3.653766798181639e-14, 2.21720387359886e-15, 1.2231444445840814e-16, 5.3553859989260236e-18, 2.918581827626196e-19, 1.2650527702081702e-20, 5.117786761520435e-22, 1.9410065794194986e-23, 6.928558524881225e-25], [1.9436771557374082e-07, 1.1794755267006424e-07, 3.57868721659685e-08, 7.238811886759451e-09, 1.0981763917968235e-09, 1.332805887337147e-10, 1.347970710496153e-11, 1.1685497835499038e-12, 8.863842609869683e-14, 5.976464306903586e-15, 3.626679135156236e-16, 2.000696683456142e-17, 1.011730423577984e-18, 4.088987051070083e-20, 2.069246108224879e-21, 8.371160941577434e-23, 3.1749033756447656e-24, 1.1333039301482719e-25], [2.9521808047023795e-08, 1.791462640420253e-08, 5.43553834323005e-09, 1.0994769083878561e-09, 1.6679803302055679e-10, 2.024350569422767e-11, 2.0473838698371764e-12, 1.774867925031688e-13, 1.3462969367890017e-14, 9.077435084704642e-16, 5.5084315293919804e-17, 3.03878569931029e-18, 1.5366806813589222e-19, 7.173070227961334e-21, 2.691976875425921e-22, 1.2714653033735589e-23, 4.822245697901049e-25, 1.7213342753972787e-26], [4.185029758019098e-09, 2.5395885132089873e-09, 7.705452755819569e-10, 1.5586252618839492e-10, 2.3645392269273827e-11, 2.8697318809886636e-12, 2.902384030039343e-13, 2.5160637420918583e-14, 1.9085188598941328e-15, 1.2868228089371845e-16, 7.808786587121023e-18, 4.3078013919742046e-19, 2.1784080330772592e-20, 1.0168588696384198e-21, 4.4075520438400654e-23, 1.5438335257710416e-24, 6.836045310656375e-26, 2.4401741094452025e-27], [5.561928801797005e-10, 3.3751278516632803e-10, 1.0240591367685894e-10, 2.07142200570254e-11, 3.14248633573664e-12, 3.813890300713389e-13, 3.857285196029857e-14, 3.3438632945161475e-15, 2.536432625186967e-16, 1.7101949705668946e-17, 1.0377922628333282e-18, 5.725093014818466e-20, 2.895116900428759e-21, 1.3514113307241296e-22, 5.857662209230448e-24, 2.3697245533026317e-25, 7.781658423660354e-27, 3.2430055329276094e-28], [6.957021751043355e-11, 4.221707740844731e-11, 1.2809228493813034e-11, 2.590994682385434e-12, 3.930712989891713e-13, 4.770524529113656e-14, 4.824804121923865e-15, 4.1826011265998547e-16, 3.172643443004965e-17, 2.139161437110585e-18, 1.2981006415010695e-19, 7.161112277807278e-21, 3.6212961305057717e-22, 1.6903844614869195e-23, 7.32693366853498e-25, 2.9641201548609134e-26, 1.1241923493244008e-27, 3.4744493242494846e-29]] |
| Legacy trial inputs | {"lambda_home": 2.1264092724366632, "lambda_away": 0.6068268710258948, "rho": -0.03318537521090455, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7419 |
| Legacy p draw | 0.1648 |
| Legacy p away | 0.0933 |
| Legacy p over 1 5 | 0.7631 |
| Legacy p under 3 5 | 0.7037 |
| Legacy p btts yes | 0.3976 |
| Legacy p over 2 5 | 0.5233 |
| Legacy goal margin distribution | {"-1": 0.07065095037550695, "-10": 1.4117850091985303e-10, "-11": 7.713475784228435e-12, "-12": 3.8688429012832375e-13, "-13": 1.793299662771394e-14, "-14": 7.725787086551348e-16, "-15": 3.108631826418014e-17, "-16": 1.1705098410052715e-18, "-17": 3.883448633997811e-20, "-2": 0.01866598145685579, "-3": 0.003428505898780358, "-4": 0.0004897934933083873, "-5": 5.706123237419876e-05, "-6": 5.6027272250018505e-06, "-7": 4.749441989350167e-07, "-8": 3.540054099185253e-08, "-9": 2.353532916587231e-09, "0": 0.1647544732090637, "1": 0.2520543855806528, "10": 3.898521967643571e-05, "11": 7.4638618753579905e-06, "12": 1.311827172023467e-06, "13": 2.1307399454488134e-07, "14": 3.216639346859203e-08, "15": 4.5353517716792386e-09, "16": 5.984099575881477e-10, "17": 6.957021751043355e-11, "2": 0.22673878733639, "3": 0.14593583397243914, "4": 0.07305536391438931, "5": 0.029823753275161808, "6": 0.010261307055266367, "7": 0.003048090419005588, "8": 0.0007961175743293764, "9": 0.00018546827923680658} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7242 |
| Legacy raw p draw | 0.1857 |
| Legacy raw p away | 0.0901 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1264 |
| Legacy lambda away | 0.6068 |
| Legacy model home team | Como |
| Legacy model away team | Venezia |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 9.837650724177182, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,565.5304 |
| Elo away rating | 1,354.7810 |
| Elo rating diff | 270.7494 |
| Elo home expectancy | 0.8261 |

</details>


---

## 2026-11-01 — Frosinone vs Torino

The model's most likely 1X2 outcome is **Frosinone win** at **46.7%**. Expected goals are 1.99 for Frosinone and 1.43 for Torino (3.41 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.8%; Under 3.5 goals: 55.8%; Double Chance 1X: 70.0%; Double Chance X2: 53.3%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 74.5%; BTTS Yes (both teams score): 66.2%; BTTS No (at least one team does not score): 33.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 46.7% | 2.14 |
| Draw | 23.3% | 4.29 |
| Torino win | 30.0% | 3.33 |

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
| 1 | 1-1 | 10.05% |
| 2 | 2-1 | 8.59% |
| 3 | 1-2 | 7.29% |
| 4 | 2-2 | 6.94% |
| 5 | 2-0 | 6.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 46.7% | 45.1% | 2.17 | +1.3% |
| Draw | 23.3% | 23.8% | 4.04 | -5.8% |
| Torino win | 30.0% | 31.1% | 3.11 | -6.6% |

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
| Market best home last update utc | 2026-10-30T07:12:04Z |
| Market best draw last update utc | 2026-10-30T07:12:04Z |
| Market best away last update utc | 2026-10-30T07:12:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Frosinone |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9862 |
| Dc lambda away | 1.4267 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:11:26.876100+00:00 |
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
| Fair Under 0.5 odds | 26.97 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.93 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
| Fair Over 3.5 odds | 2.26 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.92 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.1656206352867159, "-10": 4.4826467220138137e-07, "-11": 5.693971075133757e-08, "-12": 6.650751675151129e-09, "-13": 7.188566442419043e-10, "-14": 7.229104354818341e-11, "-15": 6.792121865891095e-12, "-16": 5.928569521771378e-13, "-17": 4.2646418586100127e-14, "-2": 0.08630077440600364, "-3": 0.03394856705727871, "-4": 0.01071439229410935, "-5": 0.0028080669397100026, "-6": 0.0006273583471582207, "-7": 0.00012192333028877238, "-8": 2.0944005693813874e-05, "-9": 3.221201208846534e-06, "0": 0.23317660731093554, "1": 0.1959466501400424, "10": 1.0370887920781201e-05, "11": 1.8339364628248642e-06, "12": 2.9821354301105014e-07, "13": 4.4873146420118364e-08, "14": 6.28226607993766e-09, "15": 8.217219790601199e-10, "16": 9.985204234765675e-11, "17": 9.999475066818375e-12, "2": 0.14151266500779813, "3": 0.07749785212368085, "4": 0.034050489774106615, "5": 0.01242369775689684, "6": 0.00386408528251267, "7": 0.0010454552316594371, "8": 0.0002500149461885288, "9": 5.3531779389322544e-05} |
| Raw goal margin distribution | {"-1": 0.15124766803725984, "-10": 4.093631582596861e-07, "-11": 5.1998342205046794e-08, "-12": 6.073583040060891e-09, "-13": 6.564724915253284e-10, "-14": 6.601744847623902e-11, "-15": 6.202684776945228e-12, "-16": 5.414073635283386e-13, "-17": 3.894545718969269e-14, "-2": 0.0788113803338649, "-3": 0.031002426670632296, "-4": 0.009784570902744295, "-5": 0.0025643759643139592, "-6": 0.000572914642351944, "-7": 0.00011134252295065624, "-8": 1.912643321929413e-05, "-9": 2.941657422539291e-06, "0": 0.22218898028956685, "1": 0.211498197313975, "10": 1.1193986211159362e-05, "11": 1.9794890884769614e-06, "12": 3.218816280675049e-07, "13": 4.843455894182519e-08, "14": 6.7808658632537924e-09, "15": 8.869389557835166e-10, "16": 1.0777692264478497e-10, "17": 1.0793095718689935e-11, "2": 0.15274399192257232, "3": 0.08364856458709127, "4": 0.036752948824256594, "5": 0.01340971982771549, "6": 0.004170763169132047, "7": 0.001128429073476924, "8": 0.0002698576902571837, "9": 5.7780394978732297e-05} |
| Unadjusted home-win probability | 50.4% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 85.7% |
| Raw p under 3 5 | 55.6% |
| Raw p btts yes | 65.8% |
| P home draw | 70.0% |
| P draw away | 53.3% |
| P home away | 76.7% |
| Raw p home draw | 72.6% |
| Raw p draw away | 49.6% |
| Raw p home away | 77.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6583 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.91, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.99, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.17 |
| Reference draw odds | 4.04 |
| Reference away odds | 3.11 |
| Market reference 1x2 last update utc | 2026-10-30T07:12:04Z |
| Market reference home last update utc | 2026-10-30T07:12:04Z |
| Market reference draw last update utc | 2026-10-30T07:12:04Z |
| Market reference away last update utc | 2026-10-30T07:12:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.95 |
| Market reference over 2 5 last update utc | 2026-10-30T07:11:19Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:11:19Z |
| Home probability edge | +1.6% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | 0.0529 |
| Raw ev home | 0.0930 |
| Raw edge prob draw | -0.0157 |
| Raw ev draw | -0.1024 |
| Raw edge prob away | -0.0372 |
| Raw ev away | -0.1475 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.04586743681710595, 0.056802337073754934, 0.04247504239922644, 0.019945750658061284, 0.007024706983944017, 0.001979228921738393, 0.00046471061991142836, 9.352385000032645e-05, 1.6469112983649516e-05, 2.577896748901938e-06, 3.6316445755986776e-07, 4.651022839767318e-08, 5.4601559308058974e-09, 5.916971976500614e-10, 5.95400638457377e-11, 5.591854418743387e-12, 4.923497172650772e-13], [0.0707391800598971, 0.10790764633539873, 0.07426578159040678, 0.03487428565945985, 0.012282397500695437, 0.0034605964942348542, 0.0008125264967766863, 0.00016352242223411425, 2.8795534477293957e-05, 4.507341396322132e-06, 6.349774070391719e-07, 8.132113045199547e-08, 9.546847393239569e-09, 1.0345570567137447e-09, 1.04103236340194e-10, 9.777116525145851e-12, 8.608522676641915e-13], [0.06487513744469174, 0.09139366853718617, 0.06431417939552043, 0.030488092955430115, 0.010737621420359294, 0.0030253519348818103, 0.0007103337858838107, 0.0001429559549420742, 2.517387568645122e-05, 3.940446115937899e-06, 5.551153190476017e-07, 7.109324643008321e-08, 8.346125669743734e-09, 9.044392197960038e-10, 9.101001171732974e-11, 8.547433497719864e-12, 7.525815500200609e-13], [0.0378104608884616, 0.05326596390835163, 0.03751954941061892, 0.017601795764454024, 0.006258089473732932, 0.0017632325034409619, 0.00041399600658742464, 8.33174426446205e-05, 1.4671812338972396e-05, 2.296566752968801e-06, 3.235317393713302e-07, 4.143449277267572e-08, 4.86428037975358e-09, 5.271243359637096e-10, 5.3042361435152395e-11, 4.981606401031326e-12, 4.386188050340635e-13], [0.01652749044828644, 0.02328331073009227, 0.01640032890202745, 0.007701390099047744, 0.002709753270400295, 0.0007707340157713268, 0.0001809635451069157, 3.6419239679377695e-05, 6.413257934272264e-06, 1.0038620048962967e-06, 1.4142032671727954e-07, 1.8111606350161436e-08, 2.126246166406766e-09, 2.304135475470533e-10, 2.318557090748298e-11, 2.177531039704757e-12, 1.9172652065850688e-13], [0.00577952099180167, 0.008141973129209163, 0.005735053694830399, 0.002693109754488757, 0.0009484880877741692, 0.0002669823151121325, 6.328139235468163e-05, 1.2735494290014409e-05, 2.2426610363467544e-06, 3.5104189279817654e-07, 4.9453469629123815e-08, 6.333472672305141e-09, 7.435299624547545e-10, 8.057363209559465e-11, 8.10779435547017e-12, 7.614638407235124e-13, 6.704511216013575e-14], [0.001684207240415181, 0.002372648203014, 0.0016712490482696833, 0.0007847977287696933, 0.0002763984259496265, 7.787595408788485e-05, 1.826723215429914e-05, 3.711243842514712e-06, 6.535326994347966e-07, 1.022969374760301e-07, 1.4411210155853826e-08, 1.8456340147910392e-09, 2.1667168403891453e-10, 2.3479920698349515e-11, 2.362688184133304e-12, 2.218977862836874e-13, 1.9537581660266327e-14], [0.00042068054221457504, 0.0005926390224295165, 0.0004174438506916572, 0.0001960264308008883, 6.903867701404752e-05, 1.9451821489077982e-05, 4.567166497676451e-06, 9.182679411953855e-07, 1.6323910962727562e-07, 2.555168395648165e-08, 3.5996257211424178e-09, 4.610016507710525e-10, 5.41201577435126e-11, 5.864804243509809e-12, 5.901512133032681e-13, 5.542553125886329e-14, 4.880088536121157e-15], [9.19427253709185e-05, 0.0001295254745952422, 9.123532341161841e-05, 4.2842971052781425e-05, 1.5088894026946496e-05, 4.2513339735646675e-06, 9.981867305023574e-07, 2.0088687896483117e-07, 3.534127412418489e-08, 5.5845023123912435e-09, 7.867238103641135e-10, 1.0075519050454065e-10, 1.1828345504757147e-11, 1.2817946917073684e-12, 1.28981746211548e-13, 1.2113644173425166e-14, 1.066578068242325e-15], [1.7861988215847346e-05, 2.5163301300224858e-05, 1.7724559121703023e-05, 8.323232109875252e-06, 2.931364566497136e-06, 8.259193648121132e-07, 1.9392072124814135e-07, 3.902689473596056e-08, 6.872453805155447e-09, 1.0747066545239003e-09, 1.52839187365389e-10, 1.95740121713512e-11, 2.2979280543033617e-12, 2.49018088011284e-13, 2.5057669561085232e-14, 2.353353879861465e-15, 2.0720731095764902e-16], [3.1230916808518506e-06, 4.399694815819961e-06, 3.0990627958563744e-06, 1.4552812736203714e-06, 5.125364646164502e-07, 1.4440844244934973e-07, 3.3906202599413735e-08, 6.823684396523227e-09, 1.201618937743848e-09, 1.8808842686938898e-10, 2.647175241242709e-11, 3.4224316931865026e-12, 4.0178281963167547e-13, 4.3539739789979566e-14, 4.381225561347595e-15, 4.114737864273697e-16, 3.6229305564616686e-17], [4.964173859106751e-07, 6.993342567126833e-07, 4.925979795355958e-07, 2.3131787326151575e-07, 8.146799324168378e-08, 2.295381270542309e-08, 5.3894122173088835e-09, 1.0846289243348695e-09, 1.9099808551661264e-10, 2.989677368711945e-11, 4.211745720032278e-12, 5.388775316555843e-13, 6.386363174934854e-14, 6.920669009587731e-15, 6.963985571041499e-16, 6.540401701346399e-17, 5.758670893977907e-18], [7.233036758623384e-08, 1.0189631807693356e-07, 7.177386196231439e-08, 3.3704111252223364e-08, 1.1870273010027322e-08, 3.3444793788659984e-09, 7.852629215162799e-10, 1.580355785643637e-10, 2.782932694498612e-11, 4.356101723683188e-12, 6.136713273062074e-13, 7.859247511689607e-14, 9.217652646163024e-15, 1.0083742987523217e-15, 1.0146857272023447e-16, 9.52967548370955e-18, 8.390656620646993e-19], [9.72819471984422e-09, 1.3704717072062182e-08, 9.65334655782261e-09, 4.5330912597674216e-09, 1.5965123788647105e-09, 4.4982139203595576e-10, 1.0561526039082421e-10, 2.1255261548400762e-11, 3.74295224091407e-12, 5.858812446503373e-13, 8.253675966602243e-14, 1.0570427428564467e-14, 1.2409352523866997e-15, 1.3434650968653502e-16, 1.3647186739238741e-17, 1.2817097688868424e-18, 1.1285155067916364e-19], [1.2149520947624519e-09, 1.7115790950261031e-09, 1.2056043243018368e-09, 5.661367684766062e-10, 1.9938807917353508e-10, 5.617809452438652e-11, 1.3190266595811773e-11, 2.6545649307651637e-12, 4.674564805346724e-13, 7.317057953393414e-14, 1.030799772609247e-14, 1.320138352151994e-15, 1.5498013020610422e-16, 1.67946318560281e-17, 1.688352288603363e-18, 1.6007245058634101e-19, 1.4094005295263703e-20], [1.416194260845577e-10, 1.995081535978718e-10, 1.405298144912205e-10, 6.59910498386351e-11, 2.3241431050974357e-11, 6.548331855523239e-12, 1.5375075225220364e-12, 3.0942616060319623e-13, 5.448850105136957e-14, 8.52904038319e-15, 1.2015393268123587e-15, 1.5388033535637722e-16, 1.8065072021288073e-17, 1.957646013374021e-18, 1.9698989463961844e-19, 1.8483035897688775e-20, 1.6428507344054737e-21], [1.547596655069212e-11, 2.1801963170133782e-11, 1.535689536788939e-11, 7.211406712932122e-12, 2.539790051968842e-12, 7.155922570848472e-13, 1.680166037093065e-13, 3.381364438339801e-14, 5.954424777606821e-15, 9.32041227175568e-16, 1.3130248402494273e-16, 1.68158210255892e-17, 1.9741250057768976e-18, 2.1392873180394627e-19, 2.1526771464578923e-20, 2.021740729861545e-21, 1.7783862666952755e-22]] |
| Legacy trial inputs | {"lambda_home": 1.7484569148248652, "lambda_away": 1.4087626190403433, "rho": -0.03318537521090455, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4519 |
| Legacy p draw | 0.2387 |
| Legacy p away | 0.3094 |
| Legacy p over 1 5 | 0.8266 |
| Legacy p under 3 5 | 0.6121 |
| Legacy p btts yes | 0.6274 |
| Legacy p over 2 5 | 0.6113 |
| Legacy goal margin distribution | {"-1": 0.16865219672523174, "-10": 4.5338280458990054e-07, "-11": 5.701680194829576e-08, "-12": 6.5908963321586614e-09, "-13": 7.047864862930094e-10, "-14": 7.006976192090361e-11, "-15": 6.452706686407579e-12, "-16": 4.923497172650772e-13, "-2": 0.09004456091297351, "-3": 0.035706264000602235, "-4": 0.01128573389082799, "-5": 0.002950438402332093, "-6": 0.0006558514610522119, "-7": 0.00012660224155163505, "-8": 2.157521343077072e-05, "-9": 3.289070430870724e-06, "0": 0.23868701584108784, "1": 0.20838492726682245, "10": 3.898938995214248e-06, "11": 6.085571443372159e-07, "12": 8.730921982248847e-08, "13": 1.1587515036074477e-08, "14": 1.429817143728213e-09, "15": 1.6342138925469148e-10, "16": 1.547596655069212e-11, "2": 0.13753142870276366, "3": 0.06768711399298527, "4": 0.02655268888921513, "5": 0.008615537340834194, "6": 0.0023769411156378136, "7": 0.000569470778003007, "8": 0.0001204487409403105, "9": 2.278963938424968e-05} |
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
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 9.79873558198315, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.7336 |
| Elo away rating | 1,449.1597 |
| Elo rating diff | 85.5739 |
| Elo home expectancy | 0.6207 |

</details>


---

## 2026-11-01 — Juventus vs Napoli

The model's most likely 1X2 outcome is **Juventus win** at **40.3%**. Expected goals are 1.13 for Juventus and 1.10 for Napoli (2.23 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 47.4%; Under 3.5 goals: 73.7%; Double Chance 1X: 69.3%; Double Chance X2: 59.7%; Double Chance 12 (either team wins): 71.0%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 53.7%; BTTS No (at least one team does not score): 46.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 40.3% | 2.48 |
| Draw | 29.0% | 3.45 |
| Napoli win | 30.7% | 3.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.13 |
| Napoli expected goals | 1.10 |
| Expected total goals | 2.23 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 73.5% |
| Under 1.5 | 26.5% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 26.3% |
| Under 3.5 | 73.7% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.82% |
| 2 | 1-0 | 10.23% |
| 3 | 2-1 | 8.91% |
| 4 | 0-0 | 8.34% |
| 5 | 0-1 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 40.3% | 42.1% | 2.32 | -6.5% |
| Draw | 29.0% | 28.8% | 3.36 | -2.5% |
| Napoli win | 30.7% | 29.1% | 3.32 | +1.9% |
| Over 2.5 | 47.4% | 47.4% | 2.04 | -3.2% |
| Under 2.5 | 52.6% | 52.6% | 1.85 | -2.8% |

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
| Market best home last update utc | 2026-10-30T07:12:04Z |
| Market best draw last update utc | 2026-10-30T07:12:04Z |
| Market best away last update utc | 2026-10-30T07:12:04Z |
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
| Dc lambda home | 1.1305 |
| Dc lambda away | 1.0954 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:11:26.876100+00:00 |
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
| Fair Under 0.5 odds | 12.00 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.77 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.80 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.33 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.1712403910542527, "-10": 2.4046459568926455e-07, "-11": 2.7594945045558358e-08, "-12": 2.907637879845166e-09, "-13": 2.816158450948577e-10, "-14": 2.2948951918752926e-11, "-2": 0.08907108377745843, "-3": 0.03358290728906935, "-4": 0.009937271916619425, "-5": 0.0024101485496655457, "-6": 0.0004942027218139029, "-7": 8.766720688815384e-05, "-8": 1.369312457280005e-05, "-9": 1.909619650871962e-06, "0": 0.2902204673973495, "1": 0.22028246807078647, "10": 4.107806521837999e-07, "11": 4.865191497967929e-08, "12": 5.290811540601636e-09, "13": 5.288720663179815e-10, "14": 4.4480326568933015e-11, "2": 0.11819606709259002, "3": 0.045993467020589554, "4": 0.01404612729396507, "5": 0.003515967126464142, "6": 0.0007440766843370216, "7": 0.00013622640683770513, "8": 2.1960299523976795e-05, "9": 3.1607790909187915e-06} |
| Raw goal margin distribution | {"-1": 0.20484635185082065, "-10": 8.276431533534475e-08, "-11": 8.16457918260739e-09, "-12": 7.366295438578305e-10, "-13": 5.66700151311054e-11, "-2": 0.09601114761086746, "-3": 0.03194479875887534, "-4": 0.008256404253722701, "-5": 0.0017390051636943544, "-6": 0.00030857316069056456, "-7": 4.725865560910034e-05, "-8": 6.362787550043813e-06, "-9": 7.640090107193249e-07, "0": 0.29607943438608375, "1": 0.2115268298192984, "10": 1.1349031765490624e-07, "11": 1.155476344131741e-08, "12": 1.0759397556833502e-09, "13": 8.542868452590384e-11, "2": 0.10226918565316236, "3": 0.03511841139161081, "4": 0.009367791647530287, "5": 0.002036379488800658, "6": 0.00037293020499232704, "7": 5.894708617757802e-05, "8": 8.191057422570173e-06, "9": 1.0150854367038987e-06} |
| Unadjusted home-win probability | 36.1% |
| Unadjusted draw probability | 29.6% |
| Unadjusted away-win probability | 34.3% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.4% |
| Raw p btts yes | 45.4% |
| P home draw | 69.3% |
| P draw away | 59.7% |
| P home away | 71.0% |
| Raw p home draw | 65.7% |
| Raw p draw away | 63.9% |
| Raw p home away | 70.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1670 |
| Totals anchor target over 2 5 | 0.4745 |
| Totals anchor reference over odds | 2.04 |
| Totals anchor reference under odds | 1.85 |
| Totals anchor reference last update utc | 2026-10-30T07:12:04Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3862 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.4, "price": 1.67, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.32 |
| Reference draw odds | 3.36 |
| Reference away odds | 3.32 |
| Market reference 1x2 last update utc | 2026-10-30T07:12:04Z |
| Market reference home last update utc | 2026-10-30T07:12:04Z |
| Market reference draw last update utc | 2026-10-30T07:12:04Z |
| Market reference away last update utc | 2026-10-30T07:12:04Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-30T07:12:04Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:12:04Z |
| Market best over 2 5 last update utc | 2026-10-30T07:12:04Z |
| Market best under 2 5 last update utc | 2026-10-30T07:12:04Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.3% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0603 |
| Raw ev home | -0.1630 |
| Raw edge prob draw | 0.0084 |
| Raw ev draw | -0.0052 |
| Raw edge prob away | 0.0519 |
| Raw ev away | 0.1393 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.1115858550246562, 0.10609329545171181, 0.05989428900744547, 0.021699047811034624, 0.005895996309185277, 0.001281633103190768, 0.0002321608490826565, 3.604686175959632e-05, 4.8972693581561875e-06, 5.914090959653709e-07, 6.427831999627578e-08, 6.351091209314318e-09, 5.752327729694809e-10, 4.809243720505574e-11], [0.12868128918815266, 0.13567682344021717, 0.06748824944503592, 0.02445025687188343, 0.006643546091545438, 0.0014441305840428593, 0.00026159638179049023, 4.061722141555014e-05, 5.518191158454027e-06, 6.663934951730128e-07, 7.242812905379408e-08, 7.156342196984713e-09, 6.481661860331651e-10, 5.419004803798669e-11], [0.07521107627496071, 0.08174445846448913, 0.0402056134240915, 0.013775145027264183, 0.0037429386278387583, 0.0008136155107791195, 0.0001473820138845024, 2.2883527094846605e-05, 3.1089196278867454e-06, 3.754425603515799e-07, 4.080562371991823e-08, 4.0318452335589354e-09, 3.651733910674358e-10, 3.0530385617996904e-11], [0.02824901428160757, 0.030702929528139314, 0.01668500486800427, 0.005470958874384394, 0.0014058345125450467, 0.00030559110867807866, 5.535616323125896e-05, 8.594971854313e-06, 1.1676992182304552e-06, 1.410148979988205e-07, 1.5326447969175487e-08, 1.5143468119994969e-09, 1.3715783433033246e-10, 1.1467104874191368e-11], [0.007957672400854938, 0.00864893381750822, 0.00470012161920618, 0.0017028028118032128, 0.00041875763125005534, 8.608420482329915e-05, 1.5593684366162686e-05, 2.4211807757031352e-06, 3.2893777279380497e-07, 3.9723522765366026e-08, 4.317419743982177e-09, 4.2658748057687236e-10, 3.863699815968973e-11, 3.230253029907454e-12], [0.0017933241679319895, 0.0019491053740934858, 0.0010592094355425488, 0.0003837400287175901, 0.0001042686210339146, 2.0513605195017888e-05, 3.5141596225974793e-06, 5.456321624316014e-07, 7.41287185475839e-08, 8.95200880635323e-09, 9.7296455294618e-10, 9.613484950367319e-11, 8.7071519265698e-12, 7.279629689764823e-13], [0.00033678310789130657, 0.0003660385429656165, 0.0001989176591654257, 7.206569888746988e-05, 1.958146266875848e-05, 4.256490243400945e-06, 6.978446591742103e-07, 1.0246875535117299e-07, 1.3921242273361274e-08, 1.6811714254376366e-09, 1.8272102270676428e-10, 1.8053954757017443e-11, 1.6351877363552957e-12, 1.3671015843409982e-13], [5.4211947585132586e-05, 5.892119242451627e-05, 3.201975829474696e-05, 1.1600409281911945e-05, 3.152026342667904e-06, 6.851668642666999e-07, 1.2411424188048715e-07, 1.7441424246124693e-08, 2.2409011579255474e-09, 2.7061801813071395e-10, 2.94125871327189e-11, 2.9061435269718556e-12, 2.632160276986183e-13, 2.2006222312600432e-14], [7.635680926673644e-06, 8.298971817351399e-06, 4.5099404942786225e-06, 1.6339022640056346e-06, 4.4395873044935057e-07, 9.650484422929693e-08, 1.7481326380447122e-08, 2.71426882654969e-09, 3.337499728398298e-10, 3.8116188986016134e-11, 4.142723893487641e-12, 4.093264619248008e-13, 3.707362844946618e-14, 3.0995472301855714e-15], [9.559782513896096e-07, 1.039021489042156e-06, 5.646392337493678e-07, 2.0456263747601085e-07, 5.5583109731774825e-08, 1.2082292741525014e-08, 2.1886414565558725e-09, 3.398232576143899e-10, 4.616784778111027e-11, 5.0460957513943854e-12, 5.186641481903215e-13, 5.124719053560992e-14, 4.641574580988718e-15, 3.880596595990995e-16], [1.0771861518514885e-07, 1.170758391046477e-07, 6.362294984250362e-08, 2.3049900973695954e-08, 6.263045837379423e-09, 1.3614199282115548e-09, 2.4661379743138377e-10, 3.8290924155145506e-11, 5.202144109273402e-12, 6.282266952752002e-13, 6.179804754325148e-14, 5.7744790622601465e-15, 5.230076996165088e-16, 4.3726150757585714e-17], [1.1034199347431596e-08, 1.1992710315000554e-08, 6.5172422652033415e-09, 2.3611258076903333e-09, 6.415576005406543e-10, 1.3945759382101127e-10, 2.526198278735551e-11, 3.922346101451837e-12, 5.328837085133975e-13, 6.435265231668547e-14, 6.994279266991849e-15, 6.254731205718312e-16, 5.3574502493287e-17, 4.479105708198593e-18], [1.0361015637249733e-09, 1.126104896189408e-09, 6.119632870076287e-10, 2.2170762594286282e-10, 6.024169150927466e-11, 1.3094944769590834e-11, 2.372077850384755e-12, 3.683048312998584e-13, 5.0037309123186177e-14, 6.0426571603210474e-15, 6.567566397417165e-16, 6.489157341953083e-17, 5.319434010971525e-18, 4.205840661592041e-19], [8.980525001354486e-11, 9.760638848973994e-11, 5.3042595352571956e-11, 1.92167539117752e-11, 5.221515299889373e-12, 1.13501883417563e-12, 2.0560247360261794e-13, 3.1923228971074096e-14, 4.33703916019334e-15, 5.23753998669589e-16, 5.69251087876134e-17, 5.624548961939575e-18, 5.09428189495081e-19, 3.854765719133718e-20]] |
| Legacy trial inputs | {"lambda_home": 1.1267893911662672, "lambda_away": 1.086867287547426, "rho": -0.03318537521090455, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T07:12:04Z", "over": 2.04, "under": 1.85, "bookmaker": "pinnacle", "event_id": "aeadf1388a1075328536501576b3d550", "kickoff_utc": "2026-11-01T19:45:00Z", "home_team": "Juventus", "away_team": "Napoli"}} |
| Legacy p home | 0.3908 |
| Legacy p draw | 0.2934 |
| Legacy p away | 0.3159 |
| Legacy p over 1 5 | 0.6536 |
| Legacy p under 3 5 | 0.8163 |
| Legacy p btts yes | 0.4510 |
| Legacy p over 2 5 | 0.3829 |
| Legacy goal margin distribution | {"-1": 0.18885222754930006, "-10": 7.181130268920211e-08, "-11": 7.02978778096548e-09, "-12": 6.294228210074676e-10, "-13": 4.809243720505574e-11, "-2": 0.08840922912842915, "-3": 0.029214062597082716, "-4": 0.00749644195441318, "-5": 0.0015673214261019237, "-6": 0.0002760324202358797, "-7": 4.195625735771376e-05, "-8": 5.606022188822247e-06, "-9": 6.680094583400842e-07, "0": 0.29337923762473617, "1": 0.22892220731904042, "10": 1.203425055410688e-07, "11": 1.2213346838973577e-08, "12": 1.1337079522147132e-09, "13": 8.980525001354486e-11, "2": 0.1110181519069736, "3": 0.03803247399220407, "4": 0.010117752135005658, "5": 0.0021930733416206435, "6": 0.0004004252083550098, "7": 6.309926339535483e-05, "8": 8.740747868076337e-06, "9": 1.0797982619007035e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3605 |
| Legacy raw p draw | 0.2990 |
| Legacy raw p away | 0.3405 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1268 |
| Legacy lambda away | 1.0869 |
| Legacy model home team | Juventus |
| Legacy model away team | Napoli |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 9.111253982530137, "version": "count-markets-nb2-v1"}} |
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
| Cagliari win | 14.4% | 6.96 |

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
| 1 | 1-0 | 12.29% |
| 2 | 2-0 | 11.76% |
| 3 | 2-1 | 10.53% |
| 4 | 1-1 | 10.22% |
| 5 | 3-0 | 7.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 64.2% | 66.4% | 1.48 | -5.0% |
| Draw | 21.5% | 20.5% | 4.58 | -1.7% |
| Cagliari win | 14.4% | 13.1% | 7.03 | +1.1% |
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
| Market best home last update utc | 2026-10-30T07:12:04Z |
| Market best draw last update utc | 2026-10-30T07:12:04Z |
| Market best away last update utc | 2026-10-30T07:12:04Z |
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
| Dc lambda home | 1.7561 |
| Dc lambda away | 0.8405 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:11:26.876100+00:00 |
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
| Fair Under 0.5 odds | 16.11 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.35 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.28 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.65 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.09660057408027041, "-10": 5.550296094953612e-09, "-11": 4.4605037961669496e-10, "-12": 3.292191427817783e-11, "-13": 2.246314735747824e-12, "-14": 1.4246897554960072e-13, "-15": 8.404204847406206e-15, "-16": 4.256345236201491e-16, "-2": 0.03547546415219446, "-3": 0.009373409384126547, "-4": 0.0019431993844017744, "-5": 0.00033013987124418646, "-6": 4.7415668808829105e-05, "-7": 5.891003460533854e-06, "-8": 6.444233089966898e-07, "-9": 6.293882848402424e-08, "0": 0.21465815084289813, "1": 0.2620777388956629, "10": 1.1289566377245569e-05, "11": 1.8956658193098407e-06, "12": 2.923342516380395e-07, "13": 4.1675612013225524e-08, "14": 5.522661674987279e-09, "15": 6.806777016321202e-10, "16": 7.20275260198958e-11, "2": 0.19868045190506287, "3": 0.10968352392813097, "4": 0.04750922336580102, "5": 0.016864571129853876, "6": 0.005060762560487206, "7": 0.0013137118452463505, "8": 0.00030026093703502385, "9": 6.12721340842839e-05} |
| Raw goal margin distribution | {"-1": 0.11892874959604649, "-10": 4.128011837114309e-09, "-11": 3.1194992354809906e-10, "-12": 2.164549569738288e-11, "-13": 1.3882265580125259e-12, "-14": 8.275203016126295e-14, "-15": 4.5917619331379056e-15, "-16": 2.2083128402839944e-16, "-2": 0.04191449573822206, "-3": 0.010532432928047867, "-4": 0.002067404763351851, "-5": 0.0003317374167036234, "-6": 4.492998120358511e-05, "-7": 5.25874240650535e-06, "-8": 5.41550978638164e-07, "-9": 4.9767443474255994e-08, "0": 0.23806836534762238, "1": 0.25155723950616765, "10": 6.54498272068548e-06, "11": 1.0334017934359968e-06, "12": 1.4981959555461419e-07, "13": 2.0076046366840757e-08, "14": 2.500421679020897e-09, "15": 2.898883209724582e-10, "16": 2.91292102513182e-11, "2": 0.1829775295486938, "3": 0.0960680495207294, "4": 0.03939966604320599, "5": 0.013209252549202613, "6": 0.0037379783281064048, "7": 0.0009141115516338434, "8": 0.0001966859787528063, "9": 3.77655788026572e-05} |
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
| Totals anchor scale | 1.0650 |
| Totals anchor target over 2 5 | 0.5294 |
| Totals anchor reference over odds | 1.84 |
| Totals anchor reference under odds | 2.06 |
| Totals anchor reference last update utc | 2026-10-30T07:12:04Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4922 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.1, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.82, "price": 2.1, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.48 |
| Reference draw odds | 4.58 |
| Reference away odds | 7.03 |
| Market reference 1x2 last update utc | 2026-10-30T07:12:04Z |
| Market reference home last update utc | 2026-10-30T07:12:04Z |
| Market reference draw last update utc | 2026-10-30T07:12:04Z |
| Market reference away last update utc | 2026-10-30T07:12:04Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-10-30T07:12:04Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:12:04Z |
| Market best over 2 5 last update utc | 2026-10-30T07:12:04Z |
| Market best under 2 5 last update utc | 2026-10-30T07:12:04Z |
| Home probability edge | -2.3% |
| Draw probability edge | +1.0% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0764 |
| Raw ev home | -0.1296 |
| Raw edge prob draw | 0.0334 |
| Raw ev draw | 0.0904 |
| Raw edge prob away | 0.0429 |
| Raw ev away | 0.2220 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06938328388458966, 0.049740218355728456, 0.022303773829392963, 0.00626683745573894, 0.001320625782784448, 0.00022263892695131556, 3.127815896082382e-05, 3.766469675009423e-06, 3.968586227123308e-07, 3.716932241259035e-08, 3.133112409784476e-09, 2.400903055428502e-10, 1.6864936524249847e-11, 1.0935350089935038e-12, 6.584093480524168e-14, 3.6999517616574025e-15, 1.949249412488294e-16], [0.1306605372347758, 0.10412514611465563, 0.04037987472307959, 0.011345797949186276, 0.0023909273862268306, 0.0004030767191033551, 5.662755325926877e-05, 6.819006271697751e-06, 7.184928250473554e-07, 6.729321208342803e-08, 5.672344400914617e-09, 4.3467157325949515e-10, 3.0533129921019865e-11, 1.979790819536893e-12, 1.1920174224428408e-13, 6.698578893419035e-15, 3.529019245011598e-16], [0.1216809808701092, 0.10256850715948208, 0.03844991020103197, 0.010270501829106478, 0.0021643276394909356, 0.0003648751898598859, 5.126068628508023e-05, 6.1727360825408666e-06, 6.503977866429385e-07, 6.091550906200176e-08, 5.13474890050318e-09, 3.9347564695019225e-10, 2.7639357593590053e-11, 1.7921564727635737e-12, 1.0790441688064813e-13, 6.063722189077802e-15, 3.194557030996931e-16], [0.07343245738442797, 0.06189839592937777, 0.026087996746262356, 0.006519747370141773, 0.0013061358974621742, 0.00022019613614573488, 3.0934975492545166e-05, 3.725144028961806e-06, 3.925042961444117e-07, 3.6761501191555646e-08, 3.098735949691557e-09, 2.374560384857808e-10, 1.667989470590175e-11, 1.0815367600703312e-12, 6.511852910388715e-14, 3.65935594910911e-15, 1.927862278585824e-16], [0.0332364542035865, 0.028015992857383192, 0.01180775558934697, 0.0033177024463014104, 0.0006218544301112032, 9.966354191990284e-05, 1.4001559158839766e-05, 1.6860470605278687e-06, 1.7765238326725403e-07, 1.6638718004653467e-08, 1.4025268818359163e-09, 1.0747559089819241e-10, 7.549530224912644e-12, 4.895171464491349e-13, 2.94734656506977e-14, 1.656270547783387e-15, 8.725747253370201e-17], [0.012034589906139868, 0.010144312711178678, 0.00427547100419598, 0.0012013070987435843, 0.00025315434441177705, 3.796004087102129e-05, 5.0698254841219e-06, 6.105008919307621e-07, 6.43261632355199e-08, 6.0247145054451275e-09, 5.078410516309219e-10, 3.891584383391394e-11, 2.7336098996693657e-12, 1.7724929601255258e-13, 1.067204913153977e-14, 5.997191124569423e-16, 3.1595064014862674e-17], [0.003631337880835448, 0.0030609623851287, 0.001290087982809407, 0.0003624844725251919, 7.638722779340756e-05, 1.287781190584692e-05, 1.6091707064160632e-06, 1.8421359036263937e-07, 1.940988725895627e-08, 1.8179077289272636e-09, 1.5323683337891087e-10, 1.1742533728271925e-11, 8.248441581737423e-13, 5.3483507787283716e-14, 3.2202024813264133e-15, 1.8096027765888693e-16, 9.53354901990113e-18], [0.0009391938385913673, 0.0007916743378369981, 0.0003336628880198289, 9.375144763515574e-05, 1.9756468840111935e-05, 3.330662690558386e-06, 4.679190584805088e-07, 5.011687527036339e-08, 5.020090974616437e-09, 4.70175950067005e-10, 3.963252511264916e-11, 3.0370391544250956e-12, 2.1333419708568466e-13, 1.3832747771880086e-14, 8.328595214011288e-16, 4.680279923935592e-17, 2.46571671191884e-18], [0.00021254547455232045, 0.00017916088342192569, 7.551001077800742e-05, 2.1216542431184938e-05, 4.471013195101171e-06, 7.537499215286563e-07, 1.0589302681753014e-07, 1.2751481786467713e-08, 1.1950386702456072e-09, 1.0640377558264601e-10, 8.969089778537013e-12, 6.873010679876423e-13, 4.827887097920309e-14, 3.130437848640961e-15, 1.884813495764861e-16, 1.0591767924740432e-17, 5.580072048091843e-19], [4.275589165129294e-05, 3.604020897585443e-05, 1.5189680449384097e-05, 4.2679440308643295e-06, 8.993941468002888e-07, 1.5162519947756728e-07, 2.1301562833902018e-08, 2.565102714155608e-09, 2.7027514306295565e-10, 2.251515221525342e-11, 1.8042323958652394e-12, 1.382582718196798e-13, 9.71183310762719e-15, 6.297224712006377e-16, 3.791512464688103e-17, 2.1306521944995126e-18, 1.1224936988055878e-19], [7.740741821357324e-06, 6.5249008287590635e-06, 2.7500162004935198e-06, 7.726900685492973e-07, 1.6283084312218884e-07, 2.745098926576027e-08, 3.8565421494062074e-09, 4.6439910591692817e-10, 4.893197223539809e-11, 4.582912272060656e-12, 3.4359974654978516e-13, 2.5030973404827134e-14, 1.7582791469156302e-15, 1.1400812567368957e-16, 6.86434499857314e-18, 3.857439971838452e-19, 2.0322190891069234e-20], [1.2740207815014853e-06, 1.073909897128912e-06, 4.5261524925529087e-07, 1.2717427188638562e-07, 2.6799741264423263e-08, 4.5180593287401896e-09, 6.34734364802568e-10, 7.643377411405909e-11, 8.053536850402227e-12, 7.542850038343811e-13, 6.358091976482536e-14, 4.33356596689142e-15, 2.8938882403630165e-16, 1.8764186265399104e-17, 1.129777788925725e-18, 6.348821341589393e-20, 3.3447561123182474e-21], [1.9221261218371954e-07, 1.620217107713302e-07, 6.828645233793883e-08, 1.9186891891226382e-08, 4.0433000380195196e-09, 6.816435007870881e-10, 9.576292009749553e-11, 1.1531629306869774e-11, 1.2150440383784686e-12, 1.1379962793632367e-13, 9.592508105431025e-15, 7.350735947943941e-16, 4.5926237487054855e-17, 2.8309689370400816e-18, 1.7045054770663275e-19, 9.578521418751451e-21, 5.046262343605289e-22], [2.6768568265084732e-08, 2.2564019998139948e-08, 9.509940790156938e-09, 2.6720703680681607e-09, 5.630918380137004e-10, 9.49293616894927e-11, 1.3336462341209405e-11, 1.6059570847179867e-12, 1.6921360631283875e-13, 1.5848351855512328e-14, 1.335904575336488e-15, 1.0237032564391531e-16, 7.190915268518767e-18, 4.147172595548434e-19, 2.3737865430729235e-20, 1.333956713679904e-21, 7.02769794831216e-23], [3.461654520660558e-09, 2.9179312489684678e-09, 1.2298053897189557e-09, 3.455464774039154e-10, 7.281784319969191e-11, 1.2276063881402117e-11, 1.7246430476180231e-12, 2.0767896688565285e-13, 2.188234497450288e-14, 2.0494752764648745e-15, 1.7275634866196826e-16, 1.3238313571255587e-17, 9.299139236902414e-19, 6.029630941353479e-20, 3.2290441726763143e-21, 1.7250445532040582e-22, 9.088070057277944e-24], [4.1781023829741586e-10, 3.5218463979887673e-10, 1.4843343836630885e-10, 4.1706315637590864e-11, 8.788872557323133e-12, 1.4816802615716206e-12, 2.0815870515171077e-13, 2.5066163629551948e-14, 2.6411265808693967e-15, 2.4736487957817714e-16, 2.0851119246895572e-17, 1.5978206129035543e-18, 1.1223753142730296e-19, 7.277564891055747e-21, 4.381768042103567e-22, 2.1901275860262388e-23, 1.0968999631916884e-24], [4.727654277679928e-11, 3.985079986702237e-11, 1.67957104809789e-11, 4.719200810727123e-12, 9.94488577181174e-13, 1.6765678254601817e-13, 2.3553812296631e-14, 2.83631526578149e-15, 2.988517808664382e-16, 2.7990114264578625e-17, 2.359369734540319e-18, 1.8079842864409227e-19, 1.270002974869192e-20, 8.234793605943513e-22, 4.958108377733417e-23, 2.7862243877531698e-24, 1.3055917512582565e-25]] |
| Legacy trial inputs | {"lambda_home": 1.8104503314979412, "lambda_away": 0.8429296544623592, "rho": -0.03318537521090455, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T07:12:04Z", "over": 1.84, "under": 2.06, "bookmaker": "pinnacle", "event_id": "3f9f4bc9a19bf36dcb74be2f29610d55", "kickoff_utc": "2026-11-01T14:00:00Z", "home_team": "Lazio", "away_team": "Cagliari"}} |
| Legacy p home | 0.6318 |
| Legacy p draw | 0.2191 |
| Legacy p away | 0.1490 |
| Legacy p over 1 5 | 0.7502 |
| Legacy p under 3 5 | 0.7205 |
| Legacy p btts yes | 0.4748 |
| Legacy p over 2 5 | 0.5021 |
| Legacy goal margin distribution | {"-1": 0.10180165351469539, "-10": 3.5965349601159434e-09, "-11": 2.7248239833134935e-10, "-12": 1.895637837408903e-11, "-13": 1.2189932596547242e-12, "-14": 7.28589694017604e-14, "-15": 4.052853686158563e-15, "-16": 1.949249412488294e-16, "-2": 0.036048727503439015, "-3": 0.009055327238779347, "-4": 0.001778872165622406, "-5": 0.0002858488791073625, "-6": 3.878576680194927e-05, "-7": 4.549087008596341e-06, "-8": 4.6953176978183196e-07, "-9": 4.3252322727782625e-08, "0": 0.21913956254688474, "1": 0.2629012566886019, "10": 8.885684564269517e-06, "11": 1.4459069360697165e-06, "12": 2.1604913837579324e-07, "13": 2.9839652153230235e-08, "14": 3.830634870940414e-09, "15": 4.576610381644382e-10, "16": 4.727654277679928e-11, "2": 0.19666826588588698, "3": 0.1061069377114246, "4": 0.044769232917811305, "5": 0.015451359213292926, "6": 0.004502957619774778, "7": 0.001134344587462802, "8": 0.0002514670139799626, "9": 4.9753170200095435e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5992 |
| Legacy raw p draw | 0.2337 |
| Legacy raw p away | 0.1671 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8105 |
| Legacy lambda away | 0.8429 |
| Legacy model home team | Lazio |
| Legacy model away team | Cagliari |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 9.342734941214754, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,538.3289 |
| Elo away rating | 1,414.0618 |
| Elo rating diff | 184.2671 |
| Elo home expectancy | 0.7428 |

</details>


---

## 2026-11-01 — Lecce vs Genoa

The model's most likely 1X2 outcome is **Genoa win** at **40.1%**. Expected goals are 0.86 for Lecce and 1.09 for Genoa (1.95 combined). The most likely exact score is 0-1 at 15.1%. Goal-market probabilities: at least one goal: 85.6%; Over 2.5 goals: 31.1%; Under 3.5 goals: 86.6%; Double Chance 1X: 59.9%; Double Chance X2: 71.5%; Double Chance 12 (either team wins): 68.6%; Under 4.5 goals: 95.2%; BTTS Yes (both teams score): 38.5%; BTTS No (at least one team does not score): 61.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 28.5% | 3.51 |
| Draw | 31.4% | 3.19 |
| Genoa win | 40.1% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.86 |
| Genoa expected goals | 1.09 |
| Expected total goals | 1.95 |
| Over 0.5 | 85.6% |
| Under 0.5 | 14.4% |
| Over 1.5 | 58.4% |
| Under 1.5 | 41.6% |
| Over 2.5 | 31.1% |
| Under 2.5 | 68.9% |
| Over 3.5 | 13.4% |
| Under 3.5 | 86.6% |
| Over 4.5 | 4.8% |
| Under 4.5 | 95.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.10% |
| 2 | 0-0 | 14.43% |
| 3 | 1-1 | 13.53% |
| 4 | 1-0 | 12.10% |
| 5 | 0-2 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 28.5% | 28.8% | 3.36 | -4.3% |
| Draw | 31.4% | 31.3% | 3.10 | -2.7% |
| Genoa win | 40.1% | 40.0% | 2.44 | -2.1% |

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
| Market best home last update utc | 2026-10-30T07:12:04Z |
| Market best draw last update utc | 2026-10-30T07:12:04Z |
| Market best away last update utc | 2026-10-30T07:12:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lecce |
| Matched away-team name | Genoa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8553 |
| Dc lambda away | 1.0949 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T07:11:26.876100+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 38.5% |
| P btts no | 61.5% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.93 |
| Fair Over 1.5 odds | 1.71 |
| Fair Under 1.5 odds | 2.40 |
| Fair Over 2.5 odds | 3.22 |
| Fair Under 2.5 odds | 1.45 |
| Fair Over 3.5 odds | 7.46 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 20.66 |
| Fair Under 4.5 odds | 1.05 |
| Goal margin distribution | {"-1": 0.2355093930179146, "-10": 1.0470062789869246e-07, "-11": 1.0347601917730812e-08, "-12": 9.364026888894943e-10, "-13": 7.356472235584856e-11, "-2": 0.11419241235141801, "-3": 0.03878016869786634, "-4": 0.010153419462487398, "-5": 0.0021574220670534995, "-6": 0.00038523060763028726, "-7": 5.927494557661696e-05, "-8": 8.009142862747227e-06, "-9": 9.643742555753418e-07, "0": 0.3138527650375343, "1": 0.18919686168683875, "10": 9.15452655713093e-09, "11": 7.068177525567777e-10, "12": 4.9970249941066676e-11, "13": 3.0668999134346322e-12, "2": 0.07195728733344213, "3": 0.019090986150313287, "4": 0.0039049199050566696, "5": 0.0006482104856955757, "6": 9.04238209517836e-05, "7": 1.0869620119792842e-05, "8": 1.1473881922735463e-06, "9": 1.0793221192433966e-07} |
| Raw goal margin distribution | {"-1": 0.23756172887288501, "-10": 1.0561303674116294e-07, "-11": 1.0437775622297676e-08, "-12": 9.44562927377105e-10, "-13": 7.420579877075132e-11, "-2": 0.11518753691622274, "-3": 0.039118116707754745, "-4": 0.010241900972912044, "-5": 0.0021762228231752795, "-6": 0.000388587682175554, "-7": 5.9791494384073885e-05, "-8": 8.078938172624936e-06, "-9": 9.727782510039957e-07, "0": 0.31690985818412076, "1": 0.1848446580212312, "10": 8.943939744624527e-09, "11": 6.905584193618866e-10, "12": 4.882075568928142e-11, "13": 2.9963502598817375e-12, "2": 0.07030201267979516, "3": 0.018651825272259278, "4": 0.0038150927981312837, "5": 0.0006332993289946835, "6": 8.834375005897996e-05, "7": 1.0619580028708108e-05, "8": 1.1209941651646126e-06, "9": 1.0544938549589836e-07} |
| Unadjusted home-win probability | 27.8% |
| Unadjusted draw probability | 31.7% |
| Unadjusted away-win probability | 40.5% |
| Raw p over 1 5 | 58.4% |
| Raw p under 3 5 | 86.6% |
| Raw p btts yes | 38.6% |
| P home draw | 59.9% |
| P draw away | 71.5% |
| P home away | 68.6% |
| Raw p home draw | 59.5% |
| Raw p draw away | 72.2% |
| Raw p home away | 68.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3106 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.24, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:11:45Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:12:04Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.36 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-10-30T07:12:04Z |
| Market reference home last update utc | 2026-10-30T07:12:04Z |
| Market reference draw last update utc | 2026-10-30T07:12:04Z |
| Market reference away last update utc | 2026-10-30T07:12:04Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.52 |
| Reference Under 2.5 odds | 1.63 |
| Market reference over 2 5 last update utc | 2026-10-30T07:12:06Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:12:06Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | -0.0094 |
| Raw ev home | -0.0648 |
| Raw edge prob draw | 0.0044 |
| Raw ev draw | -0.0176 |
| Raw edge prob away | 0.0050 |
| Raw ev away | -0.0124 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.14830667638868072, 0.1523775481455312, 0.08349187550880013, 0.029629676789901152, 0.007886256069743039, 0.0016792092668052744, 0.00029795969688573454, 4.5317238326692216e-05, 6.030834361643744e-06, 7.134094258472691e-07, 7.595262620910541e-08, 7.3511293019035856e-09, 6.521939527913049e-10, 5.34118188361865e-11], [0.12182225743718976, 0.13589313765807232, 0.07165927859144262, 0.025430513456822946, 0.00676860373900221, 0.001441229148704993, 0.0002557323907031669, 3.889480966210849e-05, 5.176135247007637e-06, 6.123039455636881e-07, 6.518850328971616e-08, 6.309315959147466e-09, 5.597640234324391e-10, 4.5842213781082604e-11], [0.054193393604513716, 0.05769661036589331, 0.030046331299968945, 0.010913231002541261, 0.0029046734071575416, 0.0006184879693490249, 0.00010974480162637113, 1.6691288729311124e-05, 2.2212827022505366e-06, 2.6276364466841523e-07, 2.797494420702394e-08, 2.7075750022547363e-09, 2.4021670285981355e-10, 1.9672692394128955e-11], [0.01550434085734179, 0.016506586023273942, 0.008786809599026616, 0.003050570800235065, 0.0008310062092158025, 0.0001769449679223219, 3.139719989033677e-05, 4.775257879144753e-06, 6.354930345853288e-07, 7.517479236652257e-08, 8.003430706260348e-09, 7.746177705372373e-10, 6.872427417896813e-11, 5.628216064232717e-12], [0.00332676046053079, 0.003541811820692441, 0.0018853823595094705, 0.0006690862984837223, 0.00017421810800514394, 3.796701377957152e-05, 6.736885116731244e-06, 1.0246252483319406e-06, 1.3635749625564313e-07, 1.6130226313692943e-08, 1.71729305148609e-09, 1.662094373929814e-10, 1.4746141104670394e-11, 1.2076441583743532e-12], [0.0005710573710205969, 0.0006079721611972007, 0.00032363661476796107, 0.000114852471986232, 3.056921649024292e-05, 6.367741885851024e-06, 1.1564246807882622e-06, 1.7588275667446383e-07, 2.340654046317314e-08, 2.7688451699329957e-09, 2.947831281778302e-10, 2.8530796095040934e-11, 2.5312590647383937e-12, 2.0729899443965596e-13], [8.168770712177168e-05, 8.696823535139382e-05, 4.629505605329682e-05, 1.642923385623266e-05, 4.372816691139305e-06, 9.310976266639483e-07, 1.6162744851008613e-07, 2.515939701350117e-08, 3.3482215957958843e-09, 3.960733628265536e-10, 4.216766836577922e-11, 4.081227970488153e-12, 3.6208752329058316e-13, 2.9653377057650526e-14], [1.0015828531583514e-05, 1.0663280482037213e-05, 5.676292793953155e-06, 2.014408226246515e-06, 5.36156341286566e-07, 1.1416300571307071e-07, 2.0257138434298262e-08, 3.0140552141198105e-09, 4.105294978991838e-10, 4.856303387344221e-11, 5.170228799527151e-12, 5.004042957133912e-13, 4.4395988998663646e-14, 3.6358364123145015e-15], [1.0745462398212837e-06, 1.1440079979405577e-06, 6.089799818989794e-07, 2.1611539955507132e-07, 5.752143007132036e-08, 1.2247956135515138e-08, 2.173283205226056e-09, 3.3053863993020464e-10, 4.30331756917861e-11, 5.210075759431029e-12, 5.546870034794071e-13, 5.3685778730502085e-14, 4.76301515059172e-15, 3.900700109969008e-16], [1.024733216914747e-07, 1.0909749180275407e-07, 5.807493365681639e-08, 2.0609688108695725e-08, 5.485489399537078e-09, 1.1680174408748176e-09, 2.0725357435790618e-10, 3.1521577318686457e-11, 4.1949028371124964e-12, 4.854567504659198e-13, 5.2897323204145265e-14, 5.1197052953468485e-15, 4.542214803423722e-16, 3.719874328137849e-17], [8.7950645048163e-09, 9.363602759045889e-09, 4.984446480250295e-09, 1.7688851434509962e-09, 4.708077411081756e-10, 1.0024842140058319e-10, 1.7788127926794583e-11, 2.705429093497087e-12, 3.6003947598110063e-13, 4.2590384752669764e-14, 4.435909847585542e-15, 4.394132792317909e-16, 3.8984851404662426e-17, 3.1926880212085906e-18], [6.862376768992673e-10, 7.305980531758967e-10, 3.889130058526086e-10, 1.380178202079932e-10, 3.673492222226907e-11, 7.8219146405444e-12, 1.3879242816452153e-12, 2.1109195675829886e-13, 2.8092193463049603e-14, 3.323128178868148e-15, 3.537944737900799e-16, 3.3498819882395284e-17, 3.0418053042758736e-18, 2.4911048799454637e-19], [4.908191821978129e-11, 5.225471451748129e-11, 2.7816304744615576e-11, 9.871476883825457e-12, 2.6273993821940814e-12, 5.594484063364318e-13, 9.926879327693743e-14, 1.5097973351272714e-14, 2.0092437191700154e-15, 2.376807788316749e-16, 2.530451476759159e-17, 2.449115577206919e-18, 2.1256863432706962e-19, 1.781718056444299e-20], [3.240457948826222e-12, 3.4499304665230703e-12, 1.836471944984708e-12, 6.517289237068668e-13, 1.7346463874226827e-13, 3.693557833565721e-14, 6.553866717356516e-15, 9.967896433513951e-16, 1.3265312394187535e-16, 1.5692022581503345e-17, 1.6706400033645238e-18, 1.616940887317596e-19, 1.4345538289694658e-20, 1.1493297397038005e-21]] |
| Legacy trial inputs | {"lambda_home": 0.8582784630809934, "lambda_away": 1.0646428748667223, "rho": -0.03318537521090455, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2859 |
| Legacy p draw | 0.3175 |
| Legacy p away | 0.3967 |
| Legacy p over 1 5 | 0.5775 |
| Legacy p under 3 5 | 0.8706 |
| Legacy p btts yes | 0.3808 |
| Legacy p over 2 5 | 0.3039 |
| Legacy goal margin distribution | {"-1": 0.2358202129623812, "-10": 8.250778708717692e-08, "-11": 7.930566017730152e-09, "-12": 6.980361665723875e-10, "-13": 5.34118188361865e-11, "-2": 0.11201092350592082, "-3": 0.03704921413122925, "-4": 0.009442144446967848, "-5": 0.0019522848684077937, "-6": 0.000339152710232031, "-7": 5.076430941942436e-05, "-8": 6.671902822625092e-06, "-9": 7.813754360575773e-07, "0": 0.3174774666818749, "1": 0.18900628460662522, "10": 9.554130591660518e-09, "11": 7.403288633617332e-10, "12": 5.253184868630436e-11, "13": 3.240457948826222e-12, "2": 0.07270470364414838, "3": 0.01938676714094318, "4": 0.003983100793456292, "5": 0.0006639236017064749, "6": 9.29810560037379e-05, "7": 1.1219717649248835e-05, "8": 1.1887688602594568e-06, "9": 1.1223588239789577e-07} |
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
| Count model | {"corners": {"alpha": 0.021573187775897174, "mu": 8.985447111288464, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,357.9326 |
| Elo away rating | 1,431.0354 |
| Elo rating diff | -13.1028 |
| Elo home expectancy | 0.4812 |

</details>


---
