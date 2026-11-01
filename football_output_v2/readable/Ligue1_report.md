# Ligue 1 — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,755 |
| Training data through | 2026-10-30 |
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
| Training sha256 | 7ba61d96a0c5dfcd99dd07eb2a990d220e48573254fa6cfa0ab2458bf6c9545e |
| Training as of utc | 2026-10-31T11:54:26.099671+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 75, 'bbs_added_results': 3, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 75, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 134, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-31T11:54:26.099671+00:00', 'observations': 440, 'observations_sha256': '93801213d449225ef6b528d9c3903b04b5a746db867efd416649a80b626575a5', 'eligible_training_matches': 175, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 172, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 18, 'retrospective_eligible_training_matches': 175, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '6ce50504f23c879f4e2c11e1082a2c3c3c1c71ea0766b33c5c17e13a3c465a11', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 114, 'tuning_matches': 20, 'audit_matches': 41, 'tuning_origin_utc': '2025-08-30T00:00:00+00:00', 'audit_origin_utc': '2025-09-28T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 29, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-31', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1750, 'tune_start_date': '2025-11-01', 'audit_start_date': '2026-05-02', 'training_shot_matches': 1462, 'tuning_matches': 187, 'audit_matches': 97, 'audit_matchdays': 32, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.880068019546734, 'audit_candidate_poisson_score': 0.875150551379139, 'audit_gain': 0.004917468167594974, 'audit_gain_lower95': -0.0024171858326772436, 'audit_baseline_briers': [0.6053846766357742, 0.16831364768840842, 0.21508819074507035, 0.24602400309300249], 'audit_candidate_briers': [0.6035036701425932, 0.16740691599848975, 0.21309904694618081, 0.24398787094786833], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1590.931 |
| Base scoring parameter | 0.208 |
| Home-advantage parameter | 0.194 |
| Dixon-Coles low-score adjustment | -0.053 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1755, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-30'} |
| Training data health | {'training_end': '2026-10-30', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 33.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261031T115426099671Z_9c8084ebbd368c6132f24a3def94889d29e1252c3574a3a480017ee510c061e2.json |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 3, 'ANCHORED_ALTERNATE': 3} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 6} |
| Legacy comparison status | {'AVAILABLE': 6} |
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

## 2026-10-31 — Troyes vs Le Mans FC

The model's most likely 1X2 outcome is **Troyes win** at **38.2%**. Expected goals are 1.24 for Troyes and 1.78 for Le Mans FC (3.02 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 47.7%; Under 3.5 goals: 74.1%; Double Chance 1X: 65.7%; Double Chance X2: 61.8%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 38.2% | 2.62 |
| Draw | 27.5% | 3.64 |
| Le Mans FC win | 34.3% | 2.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 1.24 |
| Le Mans FC expected goals | 1.78 |
| Expected total goals | 3.02 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 73.4% |
| Under 1.5 | 26.6% |
| Over 2.5 | 47.7% |
| Under 2.5 | 52.3% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.09% |
| 2 | 1-0 | 10.71% |
| 3 | 2-1 | 9.62% |
| 4 | 0-0 | 8.19% |
| 5 | 0-1 | 7.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 38.2% | 43.4% | 2.26 | -13.6% |
| Draw | 27.5% | 28.8% | 3.38 | -7.2% |
| Le Mans FC win | 34.3% | 27.8% | 3.49 | +19.7% |
| Over 2.5 | 47.7% | 47.7% | 2.04 | -2.6% |
| Under 2.5 | 52.3% | 52.3% | 1.87 | -2.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T19:45:00+00:00 |
| Fixture id | 75cf0c0e471877a0bfa95d689d0f0325 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:54:57Z |
| Market best draw last update utc | 2026-10-31T11:54:57Z |
| Market best away last update utc | 2026-10-31T11:54:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Troyes |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2413 |
| Dc lambda away | 1.7772 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:54:26.099671+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.21 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.76 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.31 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.16600732127983986, "-10": 1.2552028072421025e-06, "-11": 1.73280426994855e-07, "-12": 2.1968723723671295e-08, "-13": 2.5742752320374947e-09, "-14": 2.7907399449042155e-10, "-15": 2.5766596917287405e-11, "-2": 0.10546079983622582, "-3": 0.04792921617174933, "-4": 0.01708198235972018, "-5": 0.0049878168867398855, "-6": 0.0012309709524910705, "-7": 0.0002627708529151263, "-8": 4.938393279867932e-05, "-9": 8.285794647270711e-06, "0": 0.27461286988629213, "1": 0.23373350034384666, "10": 7.075317667879643e-08, "11": 6.8219349181463125e-09, "12": 6.040722846108439e-10, "13": 4.9438476839525913e-11, "14": 3.743307402887233e-12, "15": 2.4138996332841045e-13, "2": 0.10498202291644528, "3": 0.03332347038647152, "4": 0.008294957909185345, "5": 0.0016916575038260413, "6": 0.0002915921068880963, "7": 4.347415709597634e-05, "8": 5.70644549317651e-06, "9": 6.687136476277787e-07} |
| Raw goal margin distribution | {"-1": 0.219412068639768, "-10": 5.165724577600373e-06, "-11": 8.210732774958148e-07, "-12": 1.1992697736175473e-07, "-13": 1.6200610747700717e-08, "-14": 2.03463099221101e-09, "-15": 2.3703995085434546e-10, "-16": 2.31392502664701e-11, "-2": 0.152122049979829, "-3": 0.07724513002221478, "-4": 0.031113201402646423, "-5": 0.010335622320832506, "-6": 0.0029140390047595857, "-7": 0.0007125885873168823, "-8": 0.00015370514247332962, "-9": 2.9639660157154086e-05, "0": 0.24438618379610025, "1": 0.1515174390843758, "10": 1.4268931528573404e-07, "11": 1.584047299598357e-08, "12": 1.6159545291475378e-09, "13": 1.5246482383517984e-10, "14": 1.3373649754578491e-11, "15": 1.0882078608032638e-12, "16": 7.41934582073987e-14, "2": 0.07420688656711248, "3": 0.026317775056695858, "4": 0.007403699494146185, "5": 0.0017177768066217389, "6": 0.0003382606543753304, "7": 5.7772479522149244e-05, "8": 8.70355270032204e-06, "9": 1.1722153550875352e-06} |
| Unadjusted home-win probability | 26.2% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 49.4% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 64.3% |
| Raw p btts yes | 59.6% |
| P home draw | 65.7% |
| P draw away | 61.8% |
| P home away | 72.5% |
| Raw p home draw | 50.6% |
| Raw p draw away | 73.8% |
| Raw p home away | 75.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.8650 |
| Totals anchor target over 2 5 | 0.4775 |
| Totals anchor reference over odds | 2.04 |
| Totals anchor reference under odds | 1.87 |
| Totals anchor reference last update utc | 2026-10-31T11:54:57Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5658 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.47, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.0, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 4.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.47, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.26 |
| Reference draw odds | 3.38 |
| Reference away odds | 3.49 |
| Market reference 1x2 last update utc | 2026-10-31T11:54:57Z |
| Market reference home last update utc | 2026-10-31T11:54:57Z |
| Market reference draw last update utc | 2026-10-31T11:54:57Z |
| Market reference away last update utc | 2026-10-31T11:54:57Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-31T11:54:57Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:54:57Z |
| Market best over 2 5 last update utc | 2026-10-31T11:54:57Z |
| Market best under 2 5 last update utc | 2026-10-31T11:54:57Z |
| Home probability edge | -5.2% |
| Draw probability edge | -1.3% |
| Away probability edge | +6.5% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.1726 |
| Raw ev home | -0.4089 |
| Raw edge prob draw | -0.0432 |
| Raw ev draw | -0.1740 |
| Raw edge prob away | 0.2157 |
| Raw ev away | 0.7242 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05289370861424158, 0.0543324568260803, 0.050635641800782456, 0.028683267246489935, 0.012186028319298138, 0.004141767670261723, 0.0011730811019082731, 0.00028478922483853405, 6.049606429229281e-05, 1.1422947142539283e-05, 1.9412064347148437e-06, 2.9989732510727965e-07, 4.247025818495045e-08, 5.5518165081264135e-09, 6.739080176226068e-10, 7.634892372875076e-11], [0.06497811139151764, 0.12092080534639955, 0.07386602753659993, 0.041842444035855804, 0.017776678074635434, 0.006041908701096473, 0.0017112618285186328, 0.00041544350927383804, 8.82501690894213e-05, 1.6663514042136497e-05, 2.8317841516655938e-06, 4.3748283396271015e-07, 6.195456696132134e-08, 8.098853228341598e-09, 9.830804235225026e-10, 1.1137593011510965e-10], [0.05282629937966435, 0.08977258758038989, 0.07066568786307945, 0.030519363569155026, 0.012966090143938914, 0.004406893826335569, 0.0012481733108568641, 0.00030301938125576244, 6.436858691073276e-05, 1.2154162002484524e-05, 2.0654684989240704e-06, 3.190945933638781e-07, 4.51888984362826e-08, 5.9072038420407424e-09, 7.170467584898213e-10, 8.123623230810905e-11], [0.02568723495851007, 0.043652680143985316, 0.03709150647843057, 0.019464715527844293, 0.006304871019392174, 0.002142889403263146, 0.0006069348313515238, 0.0001473457375342003, 3.129976991270695e-05, 5.9100640920874385e-06, 1.0043515304743804e-06, 1.5516244541035358e-07, 2.1973484141042907e-08, 2.872427840302715e-09, 3.486700521872349e-10, 3.950180517936865e-11], [0.009367976475194481, 0.015919863750557726, 0.013527044101114716, 0.007662583255759838, 0.0030158522282288888, 0.0007814985751147218, 0.000221345397091622, 5.373608351268928e-05, 1.1414833425817896e-05, 2.155363995813199e-06, 3.6628082101894313e-07, 5.6586788760472746e-08, 8.013594411536798e-09, 1.0475567525314651e-09, 1.2715782184305235e-10, 1.4406065201091034e-11], [0.0027331546857898943, 0.004644701053870892, 0.003946583775882155, 0.0022355975579347737, 0.0009497891198179567, 0.00029905566180412084, 6.457864308699944e-05, 1.5677775113718438e-05, 3.3303355903909453e-06, 6.288383857856964e-07, 1.0686428866828586e-07, 1.650948283911849e-08, 2.338006844264285e-09, 3.056299996475791e-10, 3.709893993921029e-11, 4.2030426434583126e-12], [0.000664509793571346, 0.0011292625896936242, 0.0009595298736139945, 0.0005435391123142755, 0.00023092149713587737, 7.848522637118718e-05, 2.0593563722492698e-05, 3.8117253877506624e-06, 8.097019269344482e-07, 1.5288899237967038e-07, 2.5981832192782922e-08, 4.013937846412715e-09, 5.684378032198527e-10, 7.43075864059001e-11, 9.019836692336966e-12, 1.021882520552937e-12], [0.00013848150366776093, 0.00023533435168210606, 0.0001999626506602209, 0.0001132716391898284, 4.812322777174156e-05, 1.63560451158643e-05, 4.6325552167360145e-06, 1.0418792951569333e-06, 1.687390335693029e-07, 3.1861528248059454e-08, 5.414522441818177e-09, 8.364905287742559e-10, 1.1846043879717829e-10, 1.548543964131402e-11, 1.879702240774209e-12, 2.1295672296630902e-13], [2.5251675992073942e-05, 4.291249474542485e-05, 3.6462573926857845e-05, 2.065473479241648e-05, 8.775122476285576e-06, 2.982474488206333e-06, 8.447321862496724e-07, 2.0507586741177882e-07, 4.035705003432659e-08, 5.809851616448131e-09, 9.87321503098583e-10, 1.525314734718871e-10, 2.1600896431352396e-11, 2.8237222593670717e-12, 3.4275791848334674e-13, 3.8832003020277685e-14], [4.092947022736627e-06, 6.955521196360102e-06, 5.91007834260548e-06, 3.347846507319786e-06, 1.4223258458066604e-06, 4.834178167312006e-07, 1.3691939053097427e-07, 3.3239958457475585e-08, 7.060964701374114e-09, 1.2351405331776875e-09, 1.6003114438263874e-10, 2.4723239772930278e-11, 3.501206207655159e-12, 4.576862786509397e-13, 5.5556312476691057e-14, 6.294129989575063e-15], [5.970690342521461e-07, 1.0146543066307095e-06, 8.62147677155763e-07, 4.883756056078498e-07, 2.0748539241532606e-07, 7.05198008605038e-08, 1.997346357541206e-08, 4.848963298214548e-09, 1.0300361455250678e-09, 1.9449279193418106e-10, 3.061951826693688e-11, 3.606565345900301e-12, 5.107473410991184e-13, 6.676614744010568e-14, 8.104418076462085e-15, 9.181721858252541e-16], [7.918087331527646e-08, 1.3455933820576812e-07, 1.1433452764710174e-07, 6.476639172276345e-08, 2.7515871078771e-08, 9.352049926936913e-09, 2.6487997171263557e-09, 6.430498428163479e-10, 1.3659921528359326e-10, 2.579284510737371e-11, 4.383215318013534e-12, 6.273284202142097e-13, 6.773324053279392e-14, 8.854255636998104e-15, 1.07477504977319e-15, 1.2176427072373933e-16], [9.625592370438221e-09, 1.6357654127499633e-08, 1.3899032820913233e-08, 7.873301466948696e-09, 3.3449562707801138e-09, 1.1368783477071573e-09, 3.2200031750687123e-10, 7.817210649065096e-11, 1.660563099886811e-11, 3.1354972821388653e-12, 5.32843882070685e-13, 8.231914549379236e-14, 1.0799768610528651e-14, 1.0763641765612544e-15, 1.306546150083727e-16, 1.4802226676682456e-17], [1.080121319542837e-09, 1.8355494686313896e-09, 1.5596589896119324e-09, 8.834906406131152e-10, 3.7534921924432356e-10, 1.2757308785030443e-10, 3.613277962059597e-11, 8.771964941445057e-12, 1.8633758189702242e-12, 3.5184509497908695e-13, 5.979227198318537e-14, 9.23731866388456e-15, 1.3081520765532028e-15, 1.584198966790871e-16, 1.466121042073383e-17, 1.6610095249091196e-18], [1.1254674191482642e-10, 1.9126102649783015e-10, 1.6251372378548027e-10, 9.205817097965858e-11, 3.911072852825686e-11, 1.3292891394498823e-11, 3.764972090677481e-12, 9.140233198698271e-13, 1.9416048326565122e-13, 3.6661640115917014e-14, 6.230249585519624e-15, 9.625123593424206e-16, 1.36307145763489e-16, 1.7818405028992515e-17, 2.003713545103475e-18, 1.730742713208719e-19], [1.0945361069504889e-11, 1.860045842221857e-11, 1.5804734595764776e-11, 8.952812881363754e-12, 3.803584520972822e-12, 1.292756178411745e-12, 3.661499057898986e-13, 8.889031429709378e-14, 1.8882435498491806e-14, 3.565406529250178e-15, 6.059023131762653e-16, 9.360595542460559e-17, 1.3256100544110733e-17, 1.7328700361010852e-18, 2.1034466991427934e-19, 2.2076747759278295e-20]] |
| Legacy trial inputs | {"lambda_home": 1.4587753785606903, "lambda_away": 1.6993919436830383, "rho": -0.06050917105558633, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T11:54:57Z", "over": 2.04, "under": 1.87, "bookmaker": "pinnacle", "event_id": "75cf0c0e471877a0bfa95d689d0f0325", "kickoff_utc": "2026-10-31T19:45:00Z", "home_team": "Troyes", "away_team": "Le Mans FC"}} |
| Legacy p home | 0.3795 |
| Legacy p draw | 0.2673 |
| Legacy p away | 0.3532 |
| Legacy p over 1 5 | 0.8278 |
| Legacy p under 3 5 | 0.6146 |
| Legacy p btts yes | 0.6392 |
| Legacy p over 2 5 | 0.6034 |
| Legacy goal margin distribution | {"-1": 0.16587278260740862, "-10": 2.426881955818626e-06, "-11": 3.681221720280301e-07, "-12": 5.1325659976961237e-08, "-13": 6.616133163957025e-09, "-14": 7.852839477377165e-10, "-15": 7.634892372875076e-11, "-2": 0.1078249311320653, "-3": 0.051530998857530895, "-4": 0.019635526580986808, "-5": 0.006189615013511789, "-6": 0.0016591866367610846, "-7": 0.00038625690848263967, "-8": 7.938853773596832e-05, "-9": 1.4596885049284788e-05, "0": 0.2672815023080639, "1": 0.20053790794329557, "10": 7.464512994041473e-07, "11": 9.719404818788867e-08, "12": 1.1632608375736457e-08, "13": 1.2871870806364317e-09, "14": 1.31147200337045e-10, "15": 1.0945361069504889e-11, "2": 0.1124897777534668, "3": 0.046148469207673494, "4": 0.01509475821563943, "5": 0.00408453023545529, "6": 0.0009398717340999802, "7": 0.00018782114217651095, "8": 3.313758764053361e-05, "9": 5.230198166741932e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3249 |
| Legacy raw p draw | 0.2470 |
| Legacy raw p away | 0.4281 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4588 |
| Legacy lambda away | 1.6994 |
| Legacy model home team | Troyes |
| Legacy model away team | Le Mans |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 71.8% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:54:51Z |
| Market reference home draw last update utc | 2026-10-31T11:54:51Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.0% |
| Market draw away odds | 1.70 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:54:51Z |
| Market reference draw away last update utc | 2026-10-31T11:54:51Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.2% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:54:51Z |
| Market reference home away last update utc | 2026-10-31T11:54:51Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.70 |
| Market reference dc home draw odds | 1.35 |
| Market reference dc home away odds | 1.36 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.06, "price": 1.74, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.74, "price": 2.06, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.66, "price": 2.18, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.18, "price": 1.66, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 74.4% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:54:57Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.59 |
| Market reference over 1 5 last update utc | 2026-10-31T11:54:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.8% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:54:57Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.50 |
| Market reference under 3 5 last update utc | 2026-10-31T11:54:57Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.3% |
| Market btts yes odds | 1.79 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:54:51Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.11 |
| Market reference btts yes last update utc | 2026-10-31T11:54:51Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 9.888307703472368, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,390.3655 |
| Elo away rating | 1,409.0026 |
| Elo rating diff | 41.3628 |
| Elo home expectancy | 0.5592 |

</details>


---

## 2026-11-01 — Lyon vs Angers

The model's most likely 1X2 outcome is **Lyon win** at **69.5%**. Expected goals are 2.05 for Lyon and 0.74 for Angers (2.79 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 62.4%; Under 3.5 goals: 59.7%; Double Chance 1X: 87.9%; Double Chance X2: 30.5%; Double Chance 12 (either team wins): 81.5%; Under 4.5 goals: 77.6%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 69.5% | 1.44 |
| Draw | 18.5% | 5.41 |
| Angers win | 12.1% | 8.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 2.05 |
| Angers expected goals | 0.74 |
| Expected total goals | 2.79 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 83.6% |
| Under 1.5 | 16.4% |
| Over 2.5 | 62.4% |
| Under 2.5 | 37.6% |
| Over 3.5 | 40.3% |
| Under 3.5 | 59.7% |
| Over 4.5 | 22.4% |
| Under 4.5 | 77.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.93% |
| 2 | 2-1 | 9.36% |
| 3 | 1-0 | 8.77% |
| 4 | 1-1 | 8.69% |
| 5 | 3-0 | 8.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 69.5% | 70.3% | 1.40 | -2.8% |
| Draw | 18.5% | 17.5% | 5.27 | -2.7% |
| Angers win | 12.1% | 12.2% | 7.48 | -9.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:15:00+00:00 |
| Fixture id | 961df571fad52d969150e9ced52b16f7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:54:57Z |
| Market best draw last update utc | 2026-10-31T11:54:57Z |
| Market best away last update utc | 2026-10-31T11:54:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lyon |
| Matched away-team name | Angers |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0495 |
| Dc lambda away | 0.7376 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:54:26.099671+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.27 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.10 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.66 |
| Fair Over 3.5 odds | 2.48 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.47 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.08295175634103279, "-10": 2.9512004920737085e-09, "-11": 2.2627862394465128e-10, "-12": 1.5940198164533113e-11, "-13": 1.0384049157072144e-12, "-14": 6.290505294898107e-14, "-15": 3.56083860089914e-15, "-16": 1.8911453868922995e-16, "-17": 9.411721713326627e-18, "-18": 4.021940237496059e-19, "-2": 0.028951864219986318, "-3": 0.007154793766266944, "-4": 0.0013978710475237538, "-5": 0.00022480478409818433, "-6": 3.0646132070502224e-05, "-7": 3.6205494031232353e-06, "-8": 3.770782961782837e-07, "-9": 3.5094983460339824e-08, "0": 0.18468647905268548, "1": 0.21900450305327593, "10": 7.433004740260418e-05, "11": 1.5836036804254423e-05, "12": 3.0998020973717067e-06, "13": 5.611051635147822e-07, "14": 9.444964728195148e-08, "15": 1.4856085002103813e-08, "16": 2.192372179419715e-09, "17": 3.0317662942433033e-10, "18": 3.59997540982089e-11, "2": 0.2051842411429122, "3": 0.14089703929590636, "4": 0.07649078809412467, "5": 0.03418100699067294, "6": 0.012947688753870387, "7": 0.004250385665677091, "8": 0.0012300497432664206, "9": 0.00031810717067418093} |
| Raw goal margin distribution | {"-1": 0.08465747399129514, "-10": 9.275750324615197e-10, "-11": 6.150043864041523e-11, "-12": 3.7442366616510274e-12, "-13": 2.1070431182333608e-13, "-14": 1.102221638454041e-14, "-15": 5.385672506202105e-16, "-16": 2.4607399956362012e-17, "-17": 9.804804757978427e-19, "-2": 0.02696646458422956, "-3": 0.0059329725885361164, "-4": 0.0010204846470225084, "-5": 0.000143553000921411, "-6": 1.7049567576887272e-05, "-7": 1.7502434416563448e-06, "-8": 1.5810675603112673e-07, "-9": 1.2746482705792773e-08, "0": 0.20630901942507138, "1": 0.24403594792420774, "10": 2.5451995207384097e-05, "11": 4.689086822334695e-06, "12": 7.932510039649391e-07, "13": 1.240389383290927e-07, "14": 1.8029796639983368e-08, "15": 2.447930677855886e-09, "16": 3.107865247960613e-10, "17": 3.44090498457853e-11, "2": 0.20820855441825992, "3": 0.12728703686356535, "4": 0.060835290783978375, "5": 0.023779278152656166, "6": 0.00784760324558986, "7": 0.0022385118965447624, "8": 0.0005618865729310338, "9": 0.00012587105299653145} |
| Unadjusted home-win probability | 67.5% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 11.9% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 45.9% |
| P home draw | 87.9% |
| P draw away | 30.5% |
| P home away | 81.5% |
| Raw p home draw | 88.1% |
| Raw p draw away | 32.5% |
| Raw p home away | 79.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1609 |
| Totals anchor target over 2 5 | 0.6243 |
| Totals anchor reference over odds | 1.56 |
| Totals anchor reference under odds | 2.52 |
| Totals anchor reference last update utc | 2026-10-31T11:54:57Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5365 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.17, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.8, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:52Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 6.03, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:52Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.15, "price": 6.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 4.02, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.02, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.40 |
| Reference draw odds | 5.27 |
| Reference away odds | 7.48 |
| Market reference 1x2 last update utc | 2026-10-31T11:54:57Z |
| Market reference home last update utc | 2026-10-31T11:54:57Z |
| Market reference draw last update utc | 2026-10-31T11:54:57Z |
| Market reference away last update utc | 2026-10-31T11:54:57Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Market reference over 2 5 last update utc | 2026-10-31T11:54:12Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:54:12Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | +2.2% |
| Under 2.5 probability edge | -2.2% |
| Raw edge prob home | -0.0281 |
| Raw ev home | -0.0551 |
| Raw edge prob draw | 0.0309 |
| Raw ev draw | 0.0872 |
| Raw edge prob away | -0.0028 |
| Raw ev away | -0.1118 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05385883875017966, 0.03666983805319663, 0.017346223131610626, 0.0047670181943610624, 0.0009825393527867375, 0.0001620104711857891, 2.226152799834172e-05, 2.6219238010290953e-06, 2.702048963822504e-07, 2.4752202011290414e-08, 2.040689718615985e-09, 1.5294927647485652e-10, 1.0508223868648879e-11, 6.664216534968207e-13, 3.9244987921642765e-14, 2.157029458695546e-15, 1.111473798650304e-16, 5.390306290330261e-18], [0.10855150950359885, 0.0904626648055066, 0.03685458594701033, 0.010128226785857617, 0.002087548439153305, 0.0003442149215613083, 4.729786943830708e-05, 5.570660272174566e-06, 5.740897889682583e-07, 5.2589670355414254e-08, 4.335743524990035e-09, 3.249630892331459e-10, 2.232625723647002e-11, 1.4159101909042958e-12, 8.338171193657813e-14, 4.582924304188099e-15, 2.3614885113266844e-16, 1.1452493430438268e-17], [0.12137159484299763, 0.10006453794096905, 0.03735465247456362, 0.010759448951454333, 0.0022176508622536993, 0.0003656674514870819, 5.024561776643961e-05, 5.917840910518443e-06, 6.098688258620122e-07, 5.5867219951372584e-08, 4.605960363058634e-09, 3.452157859056934e-10, 2.3717698081984286e-11, 1.5041540578604586e-12, 8.857831603052086e-14, 4.868546206740163e-15, 2.5086637201433747e-16, 1.2166247956031787e-17], [0.08595722999234118, 0.07086724462173834, 0.029213170088919667, 0.007270293344718986, 0.0015705744450012283, 0.0002589713125945776, 3.558471920916916e-05, 4.1911059409043215e-06, 4.319184814007947e-07, 3.9566024328878647e-08, 3.262011962314428e-09, 2.4448712851196824e-10, 1.6797238526520465e-11, 1.0652650355519664e-12, 6.273252562281084e-14, 3.4479792950108746e-15, 1.7766742263274072e-16, 8.616323902254547e-18], [0.04565717413646467, 0.03764195435979544, 0.015516912235850406, 0.004264294445388843, 0.0007959425003825167, 0.00013755559964569557, 1.8901234040173198e-05, 2.2261542605001345e-06, 2.2941848312039062e-07, 2.101595017466439e-08, 1.7326552776525112e-09, 1.2986215821042327e-10, 8.922046981800258e-12, 5.658278103426196e-13, 3.3321104538106996e-14, 1.8314339713513668e-15, 9.437010073780495e-17, 4.576659820895468e-18], [0.01940106771996442, 0.01599516657477368, 0.006593589524237443, 0.001812023343047467, 0.0003734796407570559, 5.576881670121699e-05, 8.03168677299772e-06, 9.459580094458007e-07, 9.748661872779801e-08, 8.930291465682754e-09, 7.362558680617684e-10, 5.5182226525249475e-11, 3.7912385286316855e-12, 2.404367741526276e-13, 1.4159111199383674e-14, 7.782298220347663e-16, 4.0100613973210444e-17, 1.9447565206519924e-18], [0.006870067260215209, 0.005664011475717011, 0.0023348407506019837, 0.0006416513989591367, 0.0001322520125880316, 2.180697476786613e-05, 2.713555273883238e-06, 3.349710048970369e-07, 3.452076129509827e-08, 3.162284875663478e-09, 2.607138641708612e-10, 1.954045072513107e-11, 1.3425067149483046e-12, 8.514051051726111e-14, 5.013850149315942e-15, 2.755771640229068e-16, 1.4199935753452795e-17, 6.886532377737509e-19], [0.002085208836712454, 0.0017191457278448656, 0.0007086729112051054, 0.0001947545950454912, 4.014124678495963e-05, 6.618872096238477e-06, 9.09485698111964e-07, 9.700460146630643e-08, 1.0477771727132298e-08, 9.598194773320262e-10, 7.913210057939089e-11, 5.930934732087499e-12, 4.0747881488256624e-13, 2.5841922381301555e-14, 1.5218081921629035e-15, 8.364342237876749e-17, 4.309976946706246e-18, 2.0902063436151643e-19], [0.0005537913621527717, 0.0004565720409392318, 0.00018820989529077305, 5.1723074723679e-05, 1.0660743108398222e-05, 1.7578451278145721e-06, 2.4154190925546304e-07, 2.8448383276749193e-08, 2.6549852041315995e-09, 2.5490959294537203e-10, 2.1015963964051663e-11, 1.575142195014037e-12, 1.0821853618172218e-13, 6.8631175660803385e-15, 4.0416298686027335e-16, 2.2214084267591684e-17, 1.1446469831417825e-18, 5.55118603868946e-20], [0.00013073451973644718, 0.00010778378027646746, 4.443104741618996e-05, 1.2210358982499165e-05, 2.5167007388706786e-06, 4.1497765090184776e-07, 5.7021231569925115e-08, 6.715860844247308e-09, 6.921095429337839e-10, 5.741519308462557e-11, 4.961276291775804e-12, 3.718466419939675e-13, 2.5547343857623892e-14, 1.62018846846652e-15, 9.541148091769922e-17, 5.24411869990022e-18, 2.702188655075704e-19, 1.3104784406794939e-20], [2.7776459217151945e-05, 2.2900239226450574e-05, 9.440025320160962e-06, 2.594269202869295e-06, 5.347098499764397e-07, 8.816806624250146e-08, 1.2114993931264234e-08, 1.426882779118797e-09, 1.470487865932964e-10, 1.3470448981514094e-11, 1.0057188105493308e-12, 7.900425310164545e-14, 5.427906540662613e-15, 3.4423271687679474e-16, 2.027156342411454e-17, 1.11418965313316e-18, 5.741194684163889e-20, 2.784302955016924e-21], [5.365013340132956e-06, 4.423173161908171e-06, 1.8233375743796265e-06, 5.010821851870639e-07, 1.0327901968342513e-07, 1.7029631021964645e-08, 2.340006821917991e-09, 2.756019075336724e-10, 2.840242147336917e-11, 2.6018124887126496e-12, 2.1450584449257132e-13, 1.4559315126494175e-14, 1.0483982415464882e-15, 6.648842833840423e-17, 3.915445354120885e-18, 2.1520534009627563e-19, 1.1089097364080057e-20, 5.377871376569593e-22], [9.498962384615851e-07, 7.83139813862361e-07, 3.228289276361716e-07, 8.87185273722931e-08, 1.82859475064892e-08, 3.0151616453859645e-09, 4.143072043245401e-10, 4.879637732132557e-11, 5.0287579191900616e-12, 4.606609041813255e-13, 3.797908446700519e-14, 2.8465246026453933e-15, 1.7710392959065667e-16, 1.177203186195762e-17, 6.93244653458615e-19, 3.810293285295584e-20, 1.9633673219930674e-21, 9.521728032473234e-23], [1.5524564403403404e-07, 1.279919214846671e-07, 5.276132566317228e-08, 1.4499652027224786e-08, 2.98855136221519e-09, 4.927808875870098e-10, 6.771201543809937e-11, 7.975002655075028e-12, 8.218716215997334e-13, 7.528780076732823e-14, 6.207085773339068e-15, 4.652198074940354e-16, 3.19624518529887e-17, 1.8356557382038526e-18, 1.1329996724024907e-19, 6.2273268498493024e-21, 3.208815995227431e-22, 1.5561771284748632e-23], [2.3560146978149168e-08, 1.9424110099561978e-08, 8.007081906361374e-09, 2.200473546417467e-09, 4.535438645228709e-10, 7.478464347139769e-11, 1.0276005139046558e-11, 1.2102898981404364e-12, 1.2472759749584041e-13, 1.1425709640851513e-14, 9.419900573428482e-16, 7.060196187728698e-17, 4.8506357014006995e-18, 3.076227443424081e-19, 1.640532763673703e-20, 9.450618519851024e-22, 4.869713217642401e-23, 2.3616612304345366e-24], [3.3371316823739853e-09, 2.7512906976041695e-09, 1.1341477087500389e-09, 3.116818411526073e-10, 6.424134794444763e-11, 1.0592726917828821e-11, 1.4555249739975983e-12, 1.714291836841045e-13, 1.7666800536337635e-14, 1.6183726558010975e-15, 1.3342636901864759e-16, 1.000027903208622e-17, 6.870589599382143e-19, 4.357263166974217e-20, 2.5659541442276653e-21, 1.2771800719229902e-22, 6.89761158015766e-24, 3.345129604847885e-25], [4.431389958472318e-10, 3.653449468175669e-10, 1.5060390917519903e-10, 4.138835121241828e-11, 8.530633229229825e-12, 1.4066122695857567e-12, 1.932797194712498e-13, 2.2764147042181737e-14, 2.3459812181989383e-15, 2.1490432558781624e-16, 1.7717738709191133e-17, 1.3279408876422588e-18, 9.123482276799866e-20, 5.7860264689390054e-21, 3.4073403482064363e-22, 1.872782715988556e-23, 8.739003466616635e-25, 4.442010430396358e-26], [5.538315030245196e-11, 4.5660513499051446e-11, 1.8822353744878572e-11, 5.172682380582577e-12, 1.0661515838980703e-12, 1.757972543012154e-13, 2.4155941711756372e-14, 2.8450445322101616e-15, 2.931988194039069e-16, 2.6858567348426804e-17, 2.2143485343117624e-18, 1.65964969145746e-19, 1.1402453743699797e-20, 7.231328693394568e-22, 4.258466178891237e-23, 2.3405885651098317e-24, 1.206058105999784e-25, 5.296802895268604e-27]] |
| Legacy trial inputs | {"lambda_home": 2.1246461357832374, "lambda_away": 0.8244477471883705, "rho": -0.06050917105558633, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6853 |
| Legacy p draw | 0.1898 |
| Legacy p away | 0.1249 |
| Legacy p over 1 5 | 0.8009 |
| Legacy p under 3 5 | 0.6559 |
| Legacy p btts yes | 0.4956 |
| Legacy p over 2 5 | 0.5717 |
| Legacy goal margin distribution | {"-1": 0.08600038039180877, "-10": 2.3904698847099836e-09, "-11": 1.7684429251804838e-10, "-12": 1.2016256669735964e-11, "-13": 7.548541557225926e-13, "-14": 4.408739492174746e-14, "-15": 2.405344557784246e-15, "-16": 1.2259987329546868e-16, "-17": 5.390306290330261e-18, "-2": 0.029970954786340216, "-3": 0.00725814568810786, "-4": 0.001381429613584634, "-5": 0.00021567987217694732, "-6": 2.8483412326969455e-05, "-7": 3.2552765619925862e-06, "-8": 3.276541818116426e-07, "-9": 2.9450538827576857e-08, "0": 0.18980097396534878, "1": 0.24248973723428008, "10": 3.253742529143972e-05, "11": 6.203180625321063e-06, "12": 1.0862156301242496e-06, "13": 1.758463563451424e-07, "14": 2.646721426730912e-08, "15": 3.7212989829364308e-09, "16": 4.887995093462832e-10, "17": 5.538315030245196e-11, "2": 0.20970689433577724, "3": 0.1308763828442297, "4": 0.06419302417334596, "5": 0.025828082440051952, "6": 0.008790185404222918, "7": 0.002588912557392263, "8": 0.0006715350391127884, "9": 0.0001555498798792377} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6677 |
| Legacy raw p draw | 0.2042 |
| Legacy raw p away | 0.1282 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1246 |
| Legacy lambda away | 0.8244 |
| Legacy model home team | Lyon |
| Legacy model away team | Angers |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 87.0% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:54:52Z |
| Market reference home draw last update utc | 2026-10-31T11:54:52Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 31.1% |
| Market draw away odds | 3.13 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:54:52Z |
| Market reference draw away last update utc | 2026-10-31T11:54:52Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.9% |
| Market home away odds | 1.19 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:54:52Z |
| Market reference home away last update utc | 2026-10-31T11:54:52Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.13 |
| Market reference dc home draw odds | 1.12 |
| Market reference dc home away odds | 1.19 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:52Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.23, "price": 1.63, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:52Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.63, "price": 2.23, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:52Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.02, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:52Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.02, "price": 1.78, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 83.1% |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-10-31T11:54:35Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.6% |
| Market under 3 5 odds | 1.61 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:54:57Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.42 |
| Market reference under 3 5 last update utc | 2026-10-31T11:54:57Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.3% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:54:52Z |
| Market reference btts yes odds | 1.81 |
| Market reference btts yes opposite odds | 2.05 |
| Market reference btts yes last update utc | 2026-10-31T11:54:52Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 9.904560292539232, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,581.6014 |
| Elo away rating | 1,418.6457 |
| Elo rating diff | 222.9557 |
| Elo home expectancy | 0.7830 |

</details>


---

## 2026-11-01 — Marseille vs Toulouse

The model's most likely 1X2 outcome is **Marseille win** at **51.5%**. Expected goals are 1.95 for Marseille and 1.16 for Toulouse (3.11 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 62.9%; Under 3.5 goals: 59.0%; Double Chance 1X: 74.8%; Double Chance X2: 48.5%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 77.1%; BTTS Yes (both teams score): 62.4%; BTTS No (at least one team does not score): 37.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 51.5% | 1.94 |
| Draw | 23.3% | 4.29 |
| Toulouse win | 25.2% | 3.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 1.95 |
| Toulouse expected goals | 1.16 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 62.9% |
| Under 2.5 | 37.1% |
| Over 3.5 | 41.0% |
| Under 3.5 | 59.0% |
| Over 4.5 | 22.9% |
| Under 4.5 | 77.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.51% |
| 2 | 2-1 | 8.93% |
| 3 | 2-0 | 7.33% |
| 4 | 1-2 | 6.71% |
| 5 | 1-0 | 6.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 51.5% | 49.9% | 1.96 | +0.9% |
| Draw | 23.3% | 23.5% | 4.06 | -5.3% |
| Toulouse win | 25.2% | 26.7% | 3.59 | -9.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T19:45:00+00:00 |
| Fixture id | df1e1589c51bbcac432125567d1f7c58 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:54:57Z |
| Market best draw last update utc | 2026-10-31T11:54:57Z |
| Market best away last update utc | 2026-10-31T11:54:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Marseille |
| Matched away-team name | Toulouse |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9534 |
| Dc lambda away | 1.1582 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:54:26.099671+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 62.4% |
| P btts no | 37.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.16 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.27 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.70 |
| Fair Over 3.5 odds | 2.44 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.37 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.14947199660158908, "-10": 1.0988064482117773e-07, "-11": 1.195299843364238e-08, "-12": 1.195243843776082e-09, "-13": 1.1056876353473583e-10, "-14": 9.514514582654858e-12, "-15": 7.649220666244807e-13, "-16": 5.724012602161244e-14, "-17": 3.5770266720310726e-15, "-2": 0.07002733199078194, "-3": 0.023968823972399328, "-4": 0.006544310768222835, "-5": 0.0014786196994901368, "-6": 0.00028414597234234, "-7": 4.74275807157052e-05, "-8": 6.989715797787752e-06, "-9": 9.215881254502228e-07, "0": 0.23319450821677237, "1": 0.20216694925086753, "10": 1.615178352204298e-05, "11": 2.963313569216539e-06, "12": 4.997568134589912e-07, "13": 7.797154189569643e-08, "14": 1.1315969463291837e-08, "15": 1.534347682376228e-09, "16": 1.9364604632151867e-10, "17": 2.0409468396870718e-11, "2": 0.15723715470759653, "3": 0.090768630583371, "4": 0.041797897151126716, "5": 0.0159275313208396, "6": 0.005162201414754994, "7": 0.0014532016224602586, "8": 0.0003612067696216536, "9": 8.032203350946317e-05} |
| Raw goal margin distribution | {"-1": 0.13121581595186246, "-10": 6.537802913210672e-08, "-11": 6.769587785789709e-09, "-12": 6.441741642947232e-10, "-13": 5.6694936123813764e-11, "-14": 4.639064515008361e-12, "-15": 3.52015212261032e-13, "-16": 2.2325447234633263e-14, "-2": 0.05981911819546904, "-3": 0.019730192230427882, "-4": 0.0051676108925344, "-5": 0.001116982626191377, "-6": 0.00020499664969624593, "-7": 3.263998604625684e-05, "-8": 4.5850232052603885e-06, "-9": 5.758745898349749e-07, "0": 0.22950427763273024, "1": 0.22497827187751743, "10": 1.2174368314633704e-05, "11": 2.126073614559023e-06, "12": 3.4120928230680916e-07, "13": 5.064811260755533e-08, "14": 6.989576607652241e-09, "15": 8.945061895464677e-10, "16": 9.568052443429442e-11, "2": 0.1701543001761292, "3": 0.09465328700688026, "4": 0.041811490523475894, "5": 0.015242412974089212, "6": 0.004717973863073921, "7": 0.001266952091844825, "8": 0.0003001602840768706, "9": 6.358300757270764e-05} |
| Unadjusted home-win probability | 55.3% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 21.7% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 59.4% |
| P home draw | 74.8% |
| P draw away | 48.5% |
| P home away | 76.7% |
| Raw p home draw | 78.3% |
| Raw p draw away | 44.7% |
| Raw p home away | 77.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0524 |
| Totals anchor target over 2 5 | 0.6295 |
| Totals anchor reference over odds | 1.55 |
| Totals anchor reference under odds | 2.56 |
| Totals anchor reference last update utc | 2026-10-31T11:54:57Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5983 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.23, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.02, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.54, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.35, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:17Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.56, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.96 |
| Reference draw odds | 4.06 |
| Reference away odds | 3.59 |
| Market reference 1x2 last update utc | 2026-10-31T11:54:57Z |
| Market reference home last update utc | 2026-10-31T11:54:57Z |
| Market reference draw last update utc | 2026-10-31T11:54:57Z |
| Market reference away last update utc | 2026-10-31T11:54:57Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-10-31T11:54:34Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:54:34Z |
| Home probability edge | +1.6% |
| Draw probability edge | -0.2% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.0546 |
| Raw ev home | 0.0843 |
| Raw edge prob draw | -0.0053 |
| Raw ev draw | -0.0682 |
| Raw edge prob away | -0.0493 |
| Raw ev away | -0.2199 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05896304684221397, 0.05701868628331317, 0.03370900760258006, 0.011760003212270408, 0.003077018994072045, 0.0006440845784804661, 0.00011235033675871798, 1.6798057617450664e-05, 2.19761599633242e-06, 2.5555949793301015e-07, 2.6746980083641342e-08, 2.544865283572778e-09, 2.2195568809418697e-10, 1.786922243735285e-11, 1.3358581591363283e-12, 9.320770535753431e-14, 6.096977071395559e-15], [0.08798211641459006, 0.11087699976100171, 0.06397363829259206, 0.022318372605069667, 0.005839629053070487, 0.0012223567759494707, 0.00021322074771797824, 3.187969443380047e-05, 4.170680208474128e-06, 4.850059982706663e-07, 5.076096126778495e-08, 4.829696948485624e-09, 4.2123200642768534e-10, 3.391257275368691e-11, 2.5352187074250836e-12, 1.7689147360627144e-13, 1.1570966741062792e-14], [0.0891317649151285, 0.0932857342531509, 0.05191643437584733, 0.021178130088391284, 0.005541283226259227, 0.0011599067402254992, 0.0002023273297126364, 3.0250965329964405e-05, 3.957600743348116e-06, 4.602271100489221e-07, 4.816759089758844e-08, 4.582948410821895e-09, 3.9971132247757116e-10, 3.217998418247007e-11, 2.405694740313438e-12, 1.6785411310454982e-13, 1.097980767804785e-14], [0.056385357056356895, 0.0590131861423015, 0.030881742357196817, 0.011457771568433075, 0.0035054532305126116, 0.00073376484536086, 0.00012799363660047868, 1.9136965177944134e-05, 2.5036049854131325e-06, 2.911427811603804e-07, 3.047114363651592e-08, 2.899204147490132e-09, 2.5286008482864763e-10, 2.0357275545079187e-11, 1.5218587563068612e-12, 1.0618564671966603e-13, 6.945900565599325e-15], [0.02675231854827683, 0.027999105382088173, 0.014651999242282025, 0.005111617647926009, 0.0014223877010648615, 0.00034813845131814654, 6.0727229856254916e-05, 9.079630159581021e-06, 1.1878480794558535e-06, 1.3813416871420956e-07, 1.4457188597380172e-08, 1.3755421077252397e-09, 1.1997074933336155e-10, 9.658612600655784e-12, 7.220536032699562e-13, 5.0380318483396565e-14, 3.2955177414207775e-15], [0.010154218542848302, 0.010627454010795498, 0.0055613722648859, 0.0019401863285552182, 0.00050765208794962, 0.00011300971802731193, 2.3049873690365178e-05, 3.446301252814621e-06, 4.508644352724442e-07, 5.2430765386841935e-08, 5.487429146302108e-09, 5.221063419802894e-10, 4.553658425088888e-11, 3.66606217665887e-12, 2.740655945025177e-13, 1.9122558039802493e-14, 1.2508600814480005e-15], [0.003211813648658054, 0.00336149962681266, 0.0017590808460794163, 0.0006136874939905954, 0.00016057207139733186, 3.361110058824169e-05, 6.235210245738486e-06, 1.090076735542909e-06, 1.426099449004321e-07, 1.6584028319702766e-08, 1.735692387726899e-09, 1.6514400080588016e-10, 1.4403375522509402e-11, 1.1595878585964681e-12, 8.668787394483797e-14, 6.048529746560427e-15, 3.9565127195197024e-16], [0.0008707778689089021, 0.0009113603096484114, 0.00047691704374800797, 0.0001663812246443532, 4.353384767390747e-05, 9.112546910727648e-06, 1.5895392443104683e-06, 2.5275097152011286e-07, 3.866400653646242e-08, 4.496215041675701e-09, 4.705760308035682e-10, 4.4773376296261084e-11, 3.905002598088368e-12, 3.143841937228072e-13, 2.3502572188604013e-14, 1.6398603464875975e-15, 1.0726785832216038e-16], [0.00020657248752151236, 0.00021619975990931327, 0.00011313785476872126, 3.947020782088256e-05, 1.0327427380130719e-05, 2.1617470427494456e-06, 3.770824769831511e-07, 5.637947653416776e-08, 7.84423635903331e-09, 1.0666260119292917e-09, 1.1163359189743312e-10, 1.0621477699983858e-11, 9.263741411754615e-13, 7.458058737314953e-14, 5.575457270448565e-15, 3.8902002801965e-16, 2.5446889632690004e-17], [4.35597173765202e-05, 4.5589809908933125e-05, 2.385725726325515e-05, 8.323040101316071e-06, 2.1777334595836835e-06, 4.558452645437009e-07, 7.951497472921553e-08, 1.1888679335425759e-08, 1.5553436282809602e-09, 1.9235499298296692e-10, 2.3540054975963727e-11, 2.239739533001105e-12, 1.9534351480526865e-13, 1.5726727923586362e-14, 1.1756906539662617e-15, 8.203223322552678e-17, 5.365958138041223e-18], [8.266851508733678e-06, 8.65212658683813e-06, 4.527678669175603e-06, 1.5795634306824843e-06, 4.13294672698755e-07, 8.651123882115596e-08, 1.5090513171269056e-08, 2.256257676132027e-09, 2.951762682230912e-10, 3.432587814919695e-11, 3.8206853697266615e-12, 4.25062311068644e-13, 3.707268842289905e-14, 2.984650321276487e-15, 2.2312495676989864e-16, 1.5568243594040817e-17, 1.018362418328701e-18], [1.4262725869310056e-06, 1.4927437557608248e-06, 7.811564005298815e-07, 2.7252068313081624e-07, 7.13053647294981e-08, 1.4925707600009486e-08, 2.603552904774416e-09, 3.8927014343005976e-10, 5.0926500764458254e-11, 5.922213429721206e-12, 6.198217085922911e-13, 6.271821890508188e-14, 6.39611817940043e-15, 5.14939082952459e-16, 3.8495551657709635e-17, 2.6859753125341857e-18, 1.7569716829781065e-19], [2.255674201850928e-07, 2.360799478793206e-07, 1.2354120498645053e-07, 4.309960662790963e-08, 1.1277063946099702e-08, 2.360525883075138e-09, 4.1175629218889175e-10, 6.156373109402489e-11, 8.054112167444117e-12, 9.366080631207868e-13, 9.802585078264756e-14, 9.326757030862652e-15, 8.651054261920349e-16, 8.14384862742107e-17, 6.088136556502143e-18, 4.2479153527928887e-19, 2.778680411438095e-20], [3.2929724987741136e-08, 3.446440870054361e-08, 1.8035308031274043e-08, 6.291946736688725e-09, 1.646295436235945e-09, 3.446041458129253e-10, 6.011072633018601e-11, 8.9874536512497e-12, 1.1757890322845578e-12, 1.367318290671602e-13, 1.4310419054813758e-14, 1.3615775886507455e-15, 1.1875280492581623e-16, 1.0167639578198905e-17, 8.88783771738496e-19, 6.201369161552245e-20, 4.056489261720385e-21], [4.463907138660121e-09, 4.671946701204745e-09, 2.444840954447976e-09, 8.529274375789647e-10, 2.2316949057099675e-10, 4.671405264024681e-11, 8.148525396894566e-12, 1.218326558364086e-12, 1.5938830514762063e-13, 1.8535174165049117e-14, 1.9399002512101735e-15, 1.8457354017017632e-16, 1.6097962975445638e-17, 1.2960158113832204e-18, 1.0303905883576763e-19, 8.406488690696688e-21, 5.498919708571146e-22], [5.647795667895483e-10, 5.911010135310022e-10, 3.0932458320289586e-10, 1.0791353263754453e-10, 2.823570569238233e-11, 5.910325101669086e-12, 1.0309624507585766e-12, 1.5414432345194447e-13, 2.0166023874684255e-14, 2.345095296594231e-15, 2.4543880270373986e-16, 2.335249386245408e-17, 2.036736041555594e-18, 1.639736727868234e-19, 1.2258259666517305e-20, 9.096140849886992e-22, 6.957307565653157e-23], [6.699063227182484e-11, 7.011271823811161e-11, 3.6690154220296334e-11, 1.2800030679525456e-11, 3.349143432589319e-12, 7.010459279600422e-13, 1.2228634052294335e-13, 1.8283638956446633e-14, 2.3919680689815167e-15, 2.7816058847445795e-16, 2.9112421100195303e-17, 2.7699272795268175e-18, 2.4158493546468e-19, 1.9449535113963864e-20, 1.4539983630785273e-21, 1.0145077910350958e-22, 7.057567212545191e-24]] |
| Legacy trial inputs | {"lambda_home": 1.89782028135695, "lambda_away": 1.0466048141420494, "rho": -0.06050917105558633, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5323 |
| Legacy p draw | 0.2348 |
| Legacy p away | 0.2329 |
| Legacy p over 1 5 | 0.7960 |
| Legacy p under 3 5 | 0.6631 |
| Legacy p btts yes | 0.5599 |
| Legacy p over 2 5 | 0.5623 |
| Legacy goal margin distribution | {"-1": 0.1460482260511573, "-10": 3.19974872019622e-08, "-11": 2.9998507641178054e-09, "-12": 2.5838343675264837e-10, "-13": 2.0579241158448084e-11, "-14": 1.5237294404206476e-12, "-15": 1.0477867209859711e-13, "-16": 6.096977071395559e-15, "-2": 0.06236674903044976, "-3": 0.018897080202185924, "-4": 0.0045220821251650304, "-5": 0.000890203687236458, "-6": 0.00014849376873538454, "-7": 2.1460858341787025e-05, "-8": 2.7338125148128563e-06, "-9": 3.1116620653043845e-07, "0": 0.23475614596828115, "1": 0.21780412137042124, "10": 9.889657618319654e-06, "11": 1.6812697070307994e-06, "12": 2.6258793251615455e-07, "13": 3.79237963028283e-08, "14": 5.09169830641142e-09, "15": 6.348922850276599e-10, "16": 6.699063227182484e-11, "2": 0.16490721051892954, "3": 0.09060529961514822, "4": 0.039316033390416893, "5": 0.014034372332239465, "6": 0.00424506349446231, "7": 0.0011124881767522628, "8": 0.00025697412675590556, "9": 5.303779402925109e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5661 |
| Legacy raw p draw | 0.2347 |
| Legacy raw p away | 0.1992 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8978 |
| Legacy lambda away | 1.0466 |
| Legacy model home team | Marseille |
| Legacy model away team | Toulouse |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 73.2% |
| Market home draw odds | 1.32 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:54:51Z |
| Market reference home draw last update utc | 2026-10-31T11:54:51Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.6% |
| Market draw away odds | 1.91 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:54:51Z |
| Market reference draw away last update utc | 2026-10-31T11:54:51Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.1% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:54:51Z |
| Market reference home away last update utc | 2026-10-31T11:54:51Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.91 |
| Market reference dc home draw odds | 1.32 |
| Market reference dc home away odds | 1.27 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.19, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.19, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.71, "price": 2.11, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.11, "price": 1.71, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 83.7% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-31T11:54:35Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.1% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:54:57Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.39 |
| Market reference under 3 5 last update utc | 2026-10-31T11:54:57Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.5% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:54:51Z |
| Market reference btts yes odds | 1.51 |
| Market reference btts yes opposite odds | 2.65 |
| Market reference btts yes last update utc | 2026-10-31T11:54:51Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 9.523036445585282, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,566.8488 |
| Elo away rating | 1,531.5216 |
| Elo rating diff | 95.3273 |
| Elo home expectancy | 0.6338 |

</details>


---

## 2026-11-01 — Paris FC vs AS Monaco

The model's most likely 1X2 outcome is **Paris FC win** at **39.0%**. Expected goals are 1.52 for Paris FC and 1.50 for AS Monaco (3.02 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 52.7%; Under 3.5 goals: 69.6%; Double Chance 1X: 65.5%; Double Chance X2: 61.0%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 39.0% | 2.57 |
| Draw | 26.5% | 3.77 |
| AS Monaco win | 34.5% | 2.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.52 |
| AS Monaco expected goals | 1.50 |
| Expected total goals | 3.02 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 77.2% |
| Under 1.5 | 22.8% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.55% |
| 2 | 2-1 | 8.82% |
| 3 | 1-0 | 8.44% |
| 4 | 1-2 | 7.87% |
| 5 | 0-1 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 39.0% | 39.5% | 2.46 | -4.1% |
| Draw | 26.5% | 27.0% | 3.56 | -5.6% |
| AS Monaco win | 34.5% | 33.5% | 2.89 | -0.3% |
| Over 2.5 | 52.7% | 52.7% | 1.85 | -2.6% |
| Under 2.5 | 47.3% | 47.3% | 2.05 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:15:00+00:00 |
| Fixture id | cf3a2e2b4a4e9815d1d0be8dcef916da |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:54:57Z |
| Market best draw last update utc | 2026-10-31T11:54:57Z |
| Market best away last update utc | 2026-10-31T11:54:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Paris FC |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5198 |
| Dc lambda away | 1.5015 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:54:26.099671+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.72 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.39 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.68 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.1839693316763614, "-10": 4.928606015546444e-07, "-11": 6.106034762024441e-08, "-12": 6.9469479600641205e-09, "-13": 7.25472051618083e-10, "-14": 6.294382005419174e-11, "-2": 0.10254610084717099, "-3": 0.04117392295554627, "-4": 0.013042789873122003, "-5": 0.003396721093601954, "-6": 0.0007492913362859119, "-7": 0.00014316974444501237, "-8": 2.4107825697666244e-05, "-9": 3.6267011793334943e-06, "0": 0.2651434259845537, "1": 0.2060939200431938, "10": 6.155968018487249e-07, "11": 7.719709227662487e-08, "12": 8.890069033222506e-09, "13": 9.39725889362976e-10, "14": 8.252832298605038e-11, "2": 0.11623477015172154, "3": 0.04723985706240333, "4": 0.01514698665395749, "5": 0.003992868901731379, "6": 0.0008915491533030023, "7": 0.0001724309609076057, "8": 2.9389450041544452e-05, "9": 4.475222245576085e-06} |
| Raw goal margin distribution | {"-1": 0.18930469338924477, "-10": 9.609790163318678e-07, "-11": 1.2897693393970645e-07, "-12": 1.59082062749978e-08, "-13": 1.8140031109566269e-09, "-14": 1.9070286745068696e-10, "-15": 1.6568817398081933e-11, "-2": 0.11064709215865458, "-3": 0.04725685243624734, "-4": 0.016033133013821393, "-5": 0.0044902037559482536, "-6": 0.0010678695051945723, "-7": 0.00022035035784524816, "-8": 4.0116776289078734e-05, "-9": 6.530607414254494e-06, "0": 0.2538280552433084, "1": 0.1916877097874761, "10": 1.08494589997069e-06, "11": 1.4739258808302457e-07, "12": 1.8401542440034004e-08, "13": 2.12393127183955e-09, "14": 2.260107377227364e-10, "15": 1.98761735040441e-11, "2": 0.1133649604053923, "3": 0.049008684513197266, "4": 0.016830463134446316, "5": 0.0047710408822370385, "6": 0.001148509763964428, "7": 0.0002398831178837895, "8": 4.420601526174363e-05, "9": 7.284140893172646e-06} |
| Unadjusted home-win probability | 37.7% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 36.9% |
| Raw p over 1 5 | 81.0% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 61.3% |
| P home draw | 65.5% |
| P draw away | 61.0% |
| P home away | 73.5% |
| Raw p home draw | 63.1% |
| Raw p draw away | 62.3% |
| Raw p home away | 74.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9208 |
| Totals anchor target over 2 5 | 0.5267 |
| Totals anchor reference over odds | 1.85 |
| Totals anchor reference under odds | 2.05 |
| Totals anchor reference last update utc | 2026-10-31T11:54:57Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5777 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:53Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.9, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:53Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.76, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:53Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.67, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:53Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.93, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:53Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:53Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:53Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:53Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:53Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:53Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.34, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.34, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.46 |
| Reference draw odds | 3.56 |
| Reference away odds | 2.89 |
| Market reference 1x2 last update utc | 2026-10-31T11:54:57Z |
| Market reference home last update utc | 2026-10-31T11:54:57Z |
| Market reference draw last update utc | 2026-10-31T11:54:57Z |
| Market reference away last update utc | 2026-10-31T11:54:57Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-31T11:54:57Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:54:57Z |
| Market best over 2 5 last update utc | 2026-10-31T11:54:57Z |
| Market best under 2 5 last update utc | 2026-10-31T11:54:57Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.5% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0181 |
| Raw ev home | -0.0723 |
| Raw edge prob draw | -0.0162 |
| Raw ev draw | -0.0964 |
| Raw edge prob away | 0.0343 |
| Raw ev away | 0.0666 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05299072116572285, 0.05990886798653487, 0.05286197462802957, 0.028258170254337474, 0.01132937510954774, 0.0036337735732380094, 0.0009712443871120997, 0.0002225114645346919, 4.460507926024343e-05, 7.948107203168002e-06, 1.2746343744852578e-06, 1.8582958262198226e-07, 2.4834505431244645e-08, 3.0636141978740172e-09, 3.5093602134739645e-10, 3.7519634517611156e-11], [0.06415891429924246, 0.11857058211349766, 0.07972648745573131, 0.042619003019795695, 0.01708697582541102, 0.005480461243498707, 0.0014648318378270271, 0.00033559203209512745, 6.727342890853822e-05, 1.1987343902476562e-05, 1.922404945769063e-06, 2.8026837801778684e-07, 3.7455428021100766e-08, 4.620546255313194e-09, 5.292820879392936e-10, 5.658715346448362e-11], [0.053581753543574306, 0.0859288169699259, 0.06760575870822931, 0.03213901328453052, 0.012885297734211739, 0.004132818795135765, 0.0011046304831124076, 0.0002530701333552592, 5.073092921444395e-05, 9.03966253619269e-06, 1.4496866118998968e-06, 2.1135053581998722e-07, 2.824515857841165e-08, 3.4843564363137073e-09, 3.9913190948281714e-10, 4.2672403108164597e-11], [0.026937352932219934, 0.04319931164411488, 0.03463927081515885, 0.01816863668586094, 0.006477873338373045, 0.0020777072627708873, 0.0005553349641513542, 0.00012722688318236468, 2.5504147484042647e-05, 4.544542946463361e-06, 7.288063066861826e-07, 1.062530357683588e-07, 1.419979293201832e-08, 1.7517033851888626e-09, 2.0065705956237533e-10, 2.1452854880081434e-11], [0.010156736225582098, 0.016288312166381564, 0.013060746451269018, 0.006981820097825032, 0.0027465247487523515, 0.0007834000866766309, 0.00020938919877988045, 4.797093079404267e-05, 9.616345722816976e-06, 1.7135211499511694e-06, 2.7479661550925146e-07, 4.0062735940759106e-08, 5.354035774461284e-09, 6.604802362574344e-10, 7.565779870442552e-11, 8.088804748222237e-12], [0.0030636801178088226, 0.004913210014366283, 0.003939646392087117, 0.0021059977284778515, 0.0008443447693545809, 0.0002657202589604816, 6.316020333087599e-05, 1.4469961968325963e-05, 2.9006766093585154e-06, 5.168668912881453e-07, 8.288971069824149e-08, 1.208453235770571e-08, 1.6149925121555587e-09, 1.9922740170517777e-10, 2.2821434809354443e-11, 2.4399088184990054e-12], [0.0007701076126383906, 0.0012350181118976592, 0.00099029649342751, 0.0005293780096271646, 0.00021224028278658046, 6.807375722924804e-05, 1.785267607882864e-05, 3.6372687218944107e-06, 7.291339346050165e-07, 1.299232009856254e-07, 2.083572525964766e-08, 3.0376508009916373e-09, 4.0595557634604325e-10, 5.0079163881200616e-11, 5.736552121043373e-12, 6.13312187635797e-13], [0.0001659253052085521, 0.00026609366508227307, 0.00021336660646162692, 0.0001140583554513279, 4.5728717806414805e-05, 1.466698778143306e-05, 3.920230380745728e-06, 8.812282356723343e-07, 1.5709722725992278e-07, 2.7992901801549187e-08, 4.489209061450891e-09, 6.544840331401941e-10, 8.746609149279953e-11, 1.0789921324254002e-11, 1.2359820184972399e-12, 1.321425866353283e-13], [3.1281090654915785e-05, 5.016534427750666e-05, 4.02249684041195e-05, 2.1502866921589384e-05, 8.621012722788686e-06, 2.7650958595428426e-06, 7.390619639007397e-07, 1.6931862068043918e-07, 3.330347786161847e-08, 5.277365606456532e-09, 8.46328746803335e-10, 1.2338669106029832e-10, 1.6489556754338883e-11, 2.0341713801831957e-12, 2.3301367756932843e-13, 2.4912199056794123e-14], [5.242019427322287e-06, 8.406602959659775e-06, 6.740815662854235e-06, 3.60340524534696e-06, 1.4446911929827197e-06, 4.6336895263765917e-07, 1.2385045059654334e-07, 2.837405859040258e-08, 5.687918755136202e-09, 9.944563586246141e-10, 1.418259926287839e-10, 2.0676882361499554e-11, 2.763285264179052e-12, 3.408821645976592e-13, 3.9047942353579025e-14, 4.1747339590447636e-15], [7.906019384556019e-07, 1.2678847699594758e-06, 1.0166505492229243e-06, 5.434659698443041e-07, 2.1788848238307984e-07, 6.988535568297357e-08, 1.8679138388894583e-08, 4.279378593391451e-09, 8.578525234283115e-10, 1.5285935892941172e-10, 2.4052869108376618e-11, 3.118489639892543e-12, 4.167589831847914e-13, 5.1411885028727796e-14, 5.88921489999357e-15, 6.2963382839716e-16], [1.0839879098915766e-07, 1.7383865317311205e-07, 1.39392132796316e-07, 7.451417863957193e-08, 2.987451321827818e-08, 9.581924474761469e-09, 2.5610815248324137e-09, 5.867421304514872e-10, 1.1761946418734858e-10, 2.0958422808441474e-11, 3.361092831760927e-12, 4.807980266641484e-13, 5.714148639624041e-14, 7.049041886330553e-15, 8.074654816577913e-16, 8.632858388565629e-17], [1.3623931176152477e-08, 2.184863710170355e-08, 1.7519280486293112e-08, 9.36519708540476e-09, 3.754731102559893e-09, 1.204289073595835e-09, 3.218854944085348e-10, 7.374375978252095e-11, 1.4782816952493945e-11, 2.6341263338580135e-12, 4.2243365445976677e-13, 6.158681365033677e-14, 8.075721684671835e-15, 8.859477180588595e-16, 1.0148502625204457e-16, 1.0850071985678577e-17], [1.5805867517848674e-09, 2.534779859131715e-09, 2.0325075251340315e-09, 1.0865077230392603e-09, 4.3560688618340216e-10, 1.3971616051442863e-10, 3.734369628528415e-11, 8.555416805325899e-12, 1.7150354275183087e-12, 3.055993994678576e-13, 4.900883813299888e-14, 7.145023010007335e-15, 9.548701032674272e-16, 1.1557816569855278e-16, 1.1773832818481781e-17, 1.2587761795578054e-18], [1.7027447521262388e-10, 2.7306840944085514e-10, 2.1895928952782427e-10, 1.1704800900428765e-10, 4.6927341292798313e-11, 1.5051433199381333e-11, 4.022985945121882e-12, 9.216634930712175e-13, 1.8475844939353608e-13, 3.292181040421944e-14, 5.2796559154082034e-15, 7.697236751081622e-16, 1.028668660840548e-16, 1.268977923874529e-17, 1.4262671684493824e-18, 1.356062570702416e-19], [1.7120543210370675e-11, 2.7456138081656228e-11, 2.2015642526527405e-11, 1.1768795606877867e-11, 4.718391134947989e-12, 1.513372524838128e-12, 4.044981176548459e-13, 9.267025864471489e-14, 1.8576859581409573e-14, 3.3101806767294177e-15, 5.308521851132616e-16, 7.739320543069634e-17, 1.0342927931554746e-17, 1.275915920549532e-18, 1.4615575846403188e-19, 1.5332025256821253e-20]] |
| Legacy trial inputs | {"lambda_home": 1.5082010843661724, "lambda_away": 1.6036954986933372, "rho": -0.06050917105558633, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T11:54:57Z", "over": 1.85, "under": 2.05, "bookmaker": "pinnacle", "event_id": "cf3a2e2b4a4e9815d1d0be8dcef916da", "kickoff_utc": "2026-11-01T16:15:00Z", "home_team": "Paris FC", "away_team": "AS Monaco"}} |
| Legacy p home | 0.3746 |
| Legacy p draw | 0.2604 |
| Legacy p away | 0.3650 |
| Legacy p over 1 5 | 0.8229 |
| Legacy p under 3 5 | 0.6229 |
| Legacy p btts yes | 0.6309 |
| Legacy p over 2 5 | 0.5979 |
| Legacy goal margin distribution | {"-1": 0.17910260214349452, "-10": 1.5849777121741679e-06, "-11": 2.2697811294370732e-07, "-12": 2.9875636450920734e-08, "-13": 3.6355686889214754e-09, "-14": 4.075231748118801e-10, "-15": 3.7519634517611156e-11, "-2": 0.11066859979982203, "-3": 0.050084305985051265, "-4": 0.018051848439001032, "-5": 0.00537897922995573, "-6": 0.0013623991894986876, "-7": 0.00029959509135462, "-8": 5.8153921942259125e-05, "-9": 1.0096746392672325e-05, "0": 0.2603667119078142, "1": 0.19262533610193922, "10": 9.83094820551864e-07, "11": 1.3240170201613447e-07, "12": 1.6389439120418892e-08, "13": 1.87567080375225e-09, "14": 1.977306132942801e-10, "15": 1.7120543210370675e-11, "2": 0.1121754849532672, "3": 0.04774331156411431, "4": 0.016183404751476938, "5": 0.004535084916212136, "6": 0.0010802574524059678, "7": 0.00022340604820498582, "8": 4.078275690535733e-05, "9": 6.659112589980984e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3540 |
| Legacy raw p draw | 0.2507 |
| Legacy raw p away | 0.3953 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5082 |
| Legacy lambda away | 1.6037 |
| Legacy model home team | Paris FC |
| Legacy model away team | Monaco |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 66.6% |
| Market home draw odds | 1.45 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:54:51Z |
| Market reference home draw last update utc | 2026-10-31T11:54:51Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.8% |
| Market draw away odds | 1.59 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:54:51Z |
| Market reference draw away last update utc | 2026-10-31T11:54:51Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:54:51Z |
| Market reference home away last update utc | 2026-10-31T11:54:51Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.59 |
| Market reference dc home draw odds | 1.45 |
| Market reference dc home away odds | 1.33 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.2, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.2, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.05, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.05, "price": 1.75, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 78.0% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:54:57Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 4.07 |
| Market reference over 1 5 last update utc | 2026-10-31T11:54:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.3% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:54:57Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 3.02 |
| Market reference under 3 5 last update utc | 2026-10-31T11:54:57Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.7% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:54:51Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-31T11:54:51Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 8.959867238398926, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,504.1286 |
| Elo away rating | 1,558.3951 |
| Elo rating diff | 5.7335 |
| Elo home expectancy | 0.5083 |

</details>


---

## 2026-11-01 — Strasbourg vs Auxerre

The model's most likely 1X2 outcome is **Strasbourg win** at **52.9%**. Expected goals are 1.81 for Strasbourg and 1.12 for Auxerre (2.93 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 61.3%; Under 3.5 goals: 60.8%; Double Chance 1X: 76.5%; Double Chance X2: 47.1%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Strasbourg win | 52.9% | 1.89 |
| Draw | 23.6% | 4.24 |
| Auxerre win | 23.5% | 4.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Strasbourg expected goals | 1.81 |
| Auxerre expected goals | 1.12 |
| Expected total goals | 2.93 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 61.3% |
| Under 2.5 | 38.7% |
| Over 3.5 | 39.2% |
| Under 3.5 | 60.8% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.78% |
| 2 | 2-1 | 9.51% |
| 3 | 2-0 | 7.82% |
| 4 | 1-0 | 7.45% |
| 5 | 3-1 | 6.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Strasbourg win | 52.9% | 52.9% | 1.85 | -2.1% |
| Draw | 23.6% | 23.4% | 4.07 | -3.9% |
| Auxerre win | 23.5% | 23.8% | 4.00 | -6.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:00:00+00:00 |
| Fixture id | 448a1083448ea9dff55bfebf15ff20b4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:54:57Z |
| Market best draw last update utc | 2026-10-31T11:54:57Z |
| Market best away last update utc | 2026-10-31T11:54:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Strasbourg |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8135 |
| Dc lambda away | 1.1212 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:54:26.099671+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.71 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.91 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.67 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.13894672122794638, "-10": 1.0268267073091548e-07, "-11": 1.1144849928741371e-08, "-12": 1.1117841213518048e-09, "-13": 1.0259155418895201e-10, "-14": 8.80152693443149e-12, "-15": 6.997379067085773e-13, "-16": 4.6241787617744114e-14, "-2": 0.06558276737597835, "-3": 0.0225291923576416, "-4": 0.006160271371934959, "-5": 0.0013920859503892679, "-6": 0.00026734098032437834, "-7": 4.4568545982853666e-05, "-8": 6.557854471888531e-06, "-9": 8.630214848546859e-07, "0": 0.23601035671456974, "1": 0.2158682158761669, "10": 1.1905964765797965e-05, "11": 2.0900625903232737e-06, "12": 3.372276408083143e-07, "13": 5.0330580143869255e-08, "14": 6.983867314882221e-09, "15": 8.980302972654753e-10, "16": 9.598598639390496e-11, "2": 0.16237386743272184, "3": 0.09021726344726796, "4": 0.039898953113237795, "5": 0.014582948328986529, "6": 0.0045296271271130775, "7": 0.0012213580875206657, "8": 0.00029066581096807287, "9": 6.186876038824481e-05} |
| Raw goal margin distribution | {"-1": 0.13881661495489403, "-10": 5.5256390340962936e-08, "-11": 5.5480024893366446e-09, "-12": 5.117928299908437e-10, "-13": 4.3658482258451106e-11, "-14": 3.462287282981839e-12, "-15": 2.549408748240657e-13, "-16": 1.5851268595743132e-14, "-2": 0.06265402758255798, "-3": 0.020280014105967265, "-4": 0.005189232883012639, "-5": 0.0010929159778528808, "-6": 0.00019511456015145848, "-7": 3.018651984014134e-05, "-8": 4.1170766092685206e-06, "-9": 5.017844256188208e-07, "0": 0.24174669496367407, "1": 0.2280671221129172, "10": 6.769534591660614e-06, "11": 1.0993363243366652e-06, "12": 1.640233804663731e-07, "13": 2.263069152819774e-08, "14": 2.9027519251245977e-09, "15": 3.4570361663585816e-10, "16": 3.476531000615598e-11, "2": 0.16390200040027672, "3": 0.08580668874373726, "4": 0.03551188141585506, "5": 0.012096923259666477, "6": 0.0034929748586163658, "7": 0.0008740503626151514, "8": 0.00019281019282638398, "9": 3.800807271811238e-05} |
| Unadjusted home-win probability | 53.0% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 22.8% |
| Raw p over 1 5 | 79.7% |
| Raw p under 3 5 | 66.2% |
| Raw p btts yes | 57.0% |
| P home draw | 76.5% |
| P draw away | 47.1% |
| P home away | 76.4% |
| Raw p home draw | 77.2% |
| Raw p draw away | 47.0% |
| Raw p home away | 75.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0838 |
| Totals anchor target over 2 5 | 0.6131 |
| Totals anchor reference over odds | 1.59 |
| Totals anchor reference under odds | 2.46 |
| Totals anchor reference last update utc | 2026-10-31T11:54:57Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5639 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.6, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.05, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.6, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.98, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.37, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 4.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 7.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:53:16Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.9, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.9, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.85 |
| Reference draw odds | 4.07 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-31T11:54:57Z |
| Market reference home last update utc | 2026-10-31T11:54:57Z |
| Market reference draw last update utc | 2026-10-31T11:54:57Z |
| Market reference away last update utc | 2026-10-31T11:54:57Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-31T11:54:12Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:54:12Z |
| Home probability edge | +0.0% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | 0.0013 |
| Raw ev home | -0.0195 |
| Raw edge prob draw | 0.0082 |
| Raw ev draw | -0.0161 |
| Raw edge prob away | -0.0095 |
| Raw ev away | -0.0869 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.06614204080851745, 0.059735470527898946, 0.03450037373201423, 0.011871105237020592, 0.0030635133254581885, 0.0006324677413181031, 0.0001088117359905708, 1.6045982313125735e-05, 2.070450882830541e-06, 2.37471247017789e-07, 2.4513179358681425e-08, 2.3003587317203715e-09, 1.9788046934845006e-10, 1.5712604878515862e-11, 1.158533947090255e-12, 7.972712709374054e-14, 5.143689474895785e-15], [0.10043148153652849, 0.11467333362363506, 0.06063775061629288, 0.020864618003666967, 0.005384421585742, 0.0011116233542510703, 0.00019124717205597984, 2.8202369094740782e-05, 3.6390180950376615e-06, 4.1737873238870787e-07, 4.30842885445288e-08, 4.043103422170606e-09, 3.477941034897237e-10, 2.7616425942414444e-11, 2.0362356973246295e-12, 1.4012815303440123e-13, 9.040532779416108e-15], [0.09413906326969593, 0.09717588009362023, 0.049045132365660056, 0.018335794171941963, 0.004731821398013385, 0.000976892891913435, 0.0001680677202989347, 2.4784198531284936e-05, 3.1979634981506042e-06, 3.667917872965793e-07, 3.7862406426908777e-08, 3.553073061379097e-09, 3.0564092257437353e-10, 2.4269272591321584e-11, 1.7894407951846183e-12, 1.2314440510157429e-13, 7.944806284923826e-15], [0.0551528425570089, 0.056932009189297764, 0.02938428483518283, 0.009886926247016403, 0.0027722115719896615, 0.0005723279793894727, 9.846510252610988e-05, 1.4520210335868414e-05, 1.873576931727753e-06, 2.14890705232715e-07, 2.2182282975456324e-08, 2.0816234232795114e-09, 1.790645147321086e-10, 1.4218532920469053e-11, 1.0483718768176442e-12, 7.214607571445816e-14, 4.6545890192577655e-15], [0.024234116554281142, 0.02501588100262863, 0.012911432131969443, 0.004442646644637084, 0.001121112525711954, 0.0002514804734763049, 4.326549023616455e-05, 6.3801692416557924e-06, 8.23248261229153e-07, 9.44228104228417e-08, 9.746878060031015e-09, 9.146637294303265e-10, 7.868080990146982e-11, 6.2476124176076865e-12, 4.60653795473332e-13, 3.1700930119620504e-14, 2.045222831232568e-15], [0.008518761723795863, 0.008793567081139519, 0.00453861867004097, 0.0015616764120084566, 0.0004030135697324827, 8.136115197987059e-05, 1.520865847779344e-05, 2.242753161866572e-06, 2.8938772169524355e-07, 3.3191448158700874e-08, 3.4262165719273875e-09, 3.215220307686009e-10, 2.7657829831947915e-11, 2.196156868727531e-12, 1.619287384382192e-13, 1.1143491428988931e-14, 7.189354698494072e-16], [0.002495424894908794, 0.002575924403194618, 0.0013295103660525252, 0.00045746627534280494, 0.00011805590149179272, 2.4372849546727288e-05, 4.100364654946355e-06, 6.569760083351017e-07, 8.477116139802875e-08, 9.72286450998305e-09, 1.0036512824456545e-09, 9.418435517457898e-11, 8.101886088561741e-12, 6.433264247829727e-13, 4.743424199448708e-14, 3.264294369265553e-15, 2.1059979460204385e-16], [0.0006265644442601484, 0.0006467766853799782, 0.0003338204749593368, 0.00011486304523238346, 2.964209841007435e-05, 6.1196636141756284e-06, 1.052846142238055e-06, 1.5182185525577015e-07, 2.1284790313268284e-08, 2.441268102575736e-09, 2.5200205756524307e-10, 2.3648304654794012e-11, 2.034264290981296e-12, 1.615297918380124e-13, 1.191003966291017e-14, 8.196162471382079e-16, 5.287850719745016e-17], [0.0001376559671903909, 0.00014209658878314813, 7.334022983500774e-05, 2.5235366817802426e-05, 6.512357609135819e-06, 1.3444877400981648e-06, 2.3130989212703626e-07, 3.411024007780813e-08, 4.3039004072533554e-09, 5.363456623012333e-10, 5.536475503182088e-11, 5.195523428579816e-12, 4.4692708158147226e-13, 3.5488033081385564e-14, 2.6166311288374106e-15, 1.800693739619922e-16, 1.1617387674214728e-17], [2.6882633775290503e-05, 2.7749836312523287e-05, 1.4322506898108326e-05, 4.928178110941027e-06, 1.2717888529887528e-06, 2.625630568011432e-07, 4.51721726676236e-08, 6.66133921191149e-09, 8.595282845883424e-10, 9.640178760648746e-11, 1.08121025478001e-11, 1.014626219641298e-12, 8.727974023673692e-14, 6.9304064052144996e-15, 5.109980903644496e-16, 3.5165486343725864e-17, 2.2687427551872154e-18], [4.724883432965714e-06, 4.877302683826588e-06, 2.517319401330791e-06, 8.661750669866385e-07, 2.235292171126596e-07, 4.6148001998556085e-08, 7.939447155825228e-09, 1.1707949283100095e-09, 1.510704265796223e-10, 1.732708700547738e-11, 1.749012769169123e-12, 1.7833039187708814e-13, 1.534026026338087e-14, 1.2180860953369737e-15, 8.981286698401312e-17, 6.180675049420706e-18, 3.9875352791875856e-19], [7.549491427244477e-07, 7.793029250779508e-07, 4.0222116607973704e-07, 1.3839878455168633e-07, 3.5715842142405266e-08, 7.3735987440833085e-09, 1.2685770789977084e-09, 1.870714145595276e-10, 2.4138265135086155e-11, 2.7685486142218632e-12, 2.8578587764170714e-13, 2.622500035955485e-14, 2.4510903812372077e-15, 1.9462766997026383e-16, 1.435043803665782e-17, 9.875577664970524e-19, 6.371345205264884e-20], [1.1057469067847053e-07, 1.1414170175006572e-07, 5.891189022759637e-08, 2.0270773123673392e-08, 5.231171179247244e-09, 1.0799845369342488e-09, 1.8580393058763694e-10, 2.7399678506892136e-11, 3.535445038317318e-12, 4.0549937647604835e-13, 4.1858031531060454e-14, 3.928029363967454e-15, 3.30415873956893e-16, 2.850641611005628e-17, 2.1018571413666315e-18, 1.4464404074088713e-19, 9.331880591790579e-21], [1.4949671983526294e-08, 1.5431931035346887e-08, 7.964873601980181e-09, 2.740603723980406e-09, 7.072531041196888e-10, 1.4601365353483325e-10, 2.512064739671837e-11, 3.704430042885638e-12, 4.779913315997216e-13, 5.482341963287698e-14, 5.659195946430932e-15, 5.310686394206344e-16, 4.5683358067463496e-17, 3.5471707290201556e-18, 2.8417058756268746e-19, 1.9555840040609785e-20, 1.2616680451982257e-21], [1.8768212454200057e-09, 1.937365318577623e-09, 9.999312366019764e-10, 3.440626189063946e-10, 8.879041982752442e-11, 1.833093912545703e-11, 3.1537123212348152e-12, 4.650639167415336e-13, 6.000829230644762e-14, 6.882676678588196e-15, 7.1047038329405695e-16, 6.667175750339365e-17, 5.735209245903526e-18, 4.554015718337938e-19, 3.283476509455983e-20, 2.455091730487206e-21, 1.5839313360887648e-22], [2.199130160446798e-10, 2.2700715447912715e-10, 1.171650707892626e-10, 4.0314893289160326e-11, 1.040385122866326e-11, 2.1478934767218888e-12, 3.6953033752812806e-13, 5.4492993849979116e-14, 7.031359316187004e-15, 8.064647555233689e-16, 8.324803717023734e-17, 7.812138376710281e-18, 6.720124071441493e-19, 5.3360826673211306e-20, 3.934441782485255e-21, 2.6476421627955095e-22, 1.8559418920527464e-23], [2.4157402481665025e-11, 2.493669222314524e-11, 1.2870560473209719e-11, 4.428583267639574e-12, 1.1428610548414322e-12, 2.359456849719685e-13, 4.0592836446928793e-14, 5.9860448851167e-15, 7.723934674236109e-16, 8.858999815862389e-17, 9.144780858816682e-18, 8.581618969306892e-19, 7.382043356976869e-20, 5.8616765386785185e-21, 4.321976724691246e-22, 2.9742657821213e-23, 1.8764077417443564e-24]] |
| Legacy trial inputs | {"lambda_home": 1.7575969201755275, "lambda_away": 1.0322588383445481, "rho": -0.06050917105558633, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5329 |
| Legacy p draw | 0.2410 |
| Legacy p away | 0.2262 |
| Legacy p over 1 5 | 0.7737 |
| Legacy p under 3 5 | 0.6945 |
| Legacy p btts yes | 0.5382 |
| Legacy p over 2 5 | 0.5304 |
| Legacy goal margin distribution | {"-1": 0.14174859482821475, "-10": 2.887661424423357e-08, "-11": 2.673502899543824e-09, "-12": 2.273605273845948e-10, "-13": 1.787663956996132e-11, "-14": 1.30660690640958e-12, "-15": 8.876765987315665e-14, "-16": 5.143689474895785e-15, "-2": 0.060714736625306506, "-3": 0.018337564354316094, "-4": 0.004358582077806985, "-5": 0.0008504706341187151, "-6": 0.00014043703595485377, "-7": 2.0074917455413498e-05, "-8": 2.527854570301683e-06, "-9": 2.84294085996758e-07, "0": 0.24095416331110875, "1": 0.23186276736277528, "10": 5.5659298309013815e-06, "11": 8.774104204923137e-07, "12": 1.270480107047634e-07, "13": 1.700863095616082e-08, "14": 2.1166989603723424e-09, "15": 2.4484970826782505e-10, "16": 2.4157402481665025e-11, "2": 0.16566859469319026, "3": 0.08519584145868855, "4": 0.03447884009748106, "5": 0.011455061202084324, "6": 0.0032207010806197633, "7": 0.000783886536427902, "8": 0.00016806690208260715, "9": 3.218315435788013e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5371 |
| Legacy raw p draw | 0.2484 |
| Legacy raw p away | 0.2146 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7576 |
| Legacy lambda away | 1.0323 |
| Legacy model home team | Strasbourg |
| Legacy model away team | Auxerre |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 76.3% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:54:51Z |
| Market reference home draw last update utc | 2026-10-31T11:54:51Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.5% |
| Market draw away odds | 2.04 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:54:51Z |
| Market reference draw away last update utc | 2026-10-31T11:54:51Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:54:51Z |
| Market reference home away last update utc | 2026-10-31T11:54:51Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.04 |
| Market reference dc home draw odds | 1.27 |
| Market reference dc home away odds | 1.27 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.46, "price": 1.51, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.46, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.93, "price": 1.88, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.88, "price": 1.93, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.56, "price": 2.35, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:54:51Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.35, "price": 1.56, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 82.4% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 5.10 |
| Market reference over 1 5 last update utc | 2026-10-31T11:54:35Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.7% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:54:57Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.48 |
| Market reference under 3 5 last update utc | 2026-10-31T11:54:57Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.9% |
| Market btts yes odds | 1.57 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:54:51Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.48 |
| Market reference btts yes last update utc | 2026-10-31T11:54:51Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 9.310538983395414, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,524.8199 |
| Elo away rating | 1,446.2294 |
| Elo rating diff | 138.5904 |
| Elo home expectancy | 0.6895 |

</details>


---

## 2026-11-02 — Lorient vs Brest

The model's most likely 1X2 outcome is **Lorient win** at **39.1%**. Expected goals are 1.48 for Lorient and 1.29 for Brest (2.77 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.1%; Double Chance 1X: 67.6%; Double Chance X2: 60.9%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 39.1% | 2.55 |
| Draw | 28.4% | 3.52 |
| Brest win | 32.4% | 3.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.48 |
| Brest expected goals | 1.29 |
| Expected total goals | 2.77 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 71.6% |
| Under 1.5 | 28.4% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.9% |
| Under 3.5 | 76.1% |
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.52% |
| 2 | 1-0 | 10.19% |
| 3 | 0-1 | 9.14% |
| 4 | 0-0 | 9.03% |
| 5 | 2-1 | 8.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 39.1% | 38.4% | 2.54 | -0.6% |
| Draw | 28.4% | 29.2% | 3.31 | -5.9% |
| Brest win | 32.4% | 32.4% | 2.99 | -3.0% |
| Over 2.5 | 45.2% | 45.2% | 2.14 | -3.3% |
| Under 2.5 | 54.8% | 54.8% | 1.78 | -2.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T19:45:00+00:00 |
| Fixture id | 5118966f484adf525196d196a61bc5d6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:54:57Z |
| Market best draw last update utc | 2026-10-31T11:54:57Z |
| Market best away last update utc | 2026-10-31T11:54:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lorient |
| Matched away-team name | Brest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4802 |
| Dc lambda away | 1.2925 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:54:26.099671+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.07 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.53 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.18 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.37 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.18912902644183133, "-10": 1.1720972214942686e-07, "-11": 1.2204729845344826e-08, "-12": 1.1667521360483388e-09, "-13": 1.026049385973481e-10, "-14": 7.651241548015497e-12, "-2": 0.09242608724368807, "-3": 0.031888966933047394, "-4": 0.008606424426588289, "-5": 0.0019002840345503434, "-6": 0.0003543208455434465, "-7": 5.711049666502362e-05, "-8": 8.101049861874184e-06, "-9": 1.0256111628187033e-06, "0": 0.28419720041971924, "1": 0.20966919388809804, "10": 4.3825622047637176e-07, "11": 5.226149770870686e-08, "12": 5.721652976052212e-09, "13": 5.762360202461938e-10, "14": 4.9209990205355644e-11, "2": 0.1168006324120299, "3": 0.046150913809735246, "4": 0.014264345267199116, "5": 0.003606922663922139, "6": 0.0007702012924824046, "7": 0.00014217155212856722, "8": 2.3095496407512388e-05, "9": 3.3485590617583482e-06} |
| Raw goal margin distribution | {"-1": 0.18065103221433954, "-10": 2.6626079579751045e-07, "-11": 3.0843370476551436e-08, "-12": 3.2821519235815644e-09, "-13": 3.228539609238446e-10, "-14": 2.934192785287554e-11, "-15": 2.2422705527604138e-12, "-2": 0.09454856906070985, "-3": 0.035536952895392195, "-4": 0.010533114431005164, "-5": 0.0025660316374927637, "-6": 0.0005294175415043364, "-7": 9.460145503173485e-05, "-8": 1.489605571668527e-05, "-9": 2.0954074024829996e-06, "0": 0.2656713993173813, "1": 0.20780788835486289, "10": 1.0332359506596933e-06, "11": 1.3707029320664833e-07, "12": 1.6704343781193115e-08, "13": 1.881768034123809e-09, "14": 1.9585643317980382e-10, "15": 1.7140616491303213e-11, "2": 0.12400334973555613, "3": 0.05337622699089771, "4": 0.018118144355790598, "5": 0.00505484855081877, "6": 0.0011943557280787852, "7": 0.0002444119377934152, "8": 4.407426864482736e-05, "9": 7.100215471625315e-06} |
| Unadjusted home-win probability | 41.0% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 69.8% |
| Raw p btts yes | 56.7% |
| P home draw | 67.6% |
| P draw away | 60.9% |
| P home away | 71.6% |
| Raw p home draw | 67.6% |
| Raw p draw away | 59.0% |
| Raw p home away | 73.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.8964 |
| Totals anchor target over 2 5 | 0.4521 |
| Totals anchor reference over odds | 2.14 |
| Totals anchor reference under odds | 1.78 |
| Totals anchor reference last update utc | 2026-10-31T11:54:57Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5174 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:54:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:54:57Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.13, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.54 |
| Reference draw odds | 3.31 |
| Reference away odds | 2.99 |
| Market reference 1x2 last update utc | 2026-10-31T11:54:57Z |
| Market reference home last update utc | 2026-10-31T11:54:57Z |
| Market reference draw last update utc | 2026-10-31T11:54:57Z |
| Market reference away last update utc | 2026-10-31T11:54:57Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.14 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-31T11:54:57Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:54:57Z |
| Market best over 2 5 last update utc | 2026-10-31T11:54:57Z |
| Market best under 2 5 last update utc | 2026-10-31T11:54:57Z |
| Home probability edge | +0.8% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0263 |
| Raw ev home | 0.0410 |
| Raw edge prob draw | -0.0265 |
| Raw ev draw | -0.1206 |
| Raw edge prob away | 0.0002 |
| Raw ev away | -0.0298 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.07335734835128092, 0.07547177458850676, 0.057084419971686375, 0.026387094484956086, 0.00914801388500598, 0.0025371844736592356, 0.0005864027913870032, 0.00011616979506776817, 2.0137171580298964e-05, 3.1027815144229924e-06, 4.302753134455778e-07, 5.424365920475468e-08, 6.268490427666414e-09, 6.686746344944413e-10, 6.623416224921076e-11], [0.08180309522783707, 0.13312278089878427, 0.07857540384905677, 0.036321234525760776, 0.012592032743569079, 0.0034923766372017585, 0.0008071700855382585, 0.00015990507685003258, 2.771835800529368e-05, 4.270908080910685e-06, 5.922641683498739e-07, 7.466516135888294e-08, 8.628434292967104e-09, 9.204154036264439e-10, 9.116981568555891e-11], [0.061456932082142125, 0.08522482357242245, 0.05990212443371124, 0.024997676008388165, 0.008666323128072747, 0.002403588446700936, 0.000555525618702128, 0.00011005284802085896, 1.907684421930674e-05, 2.9394038463227568e-06, 4.0761906870998635e-07, 5.138744696135256e-08, 5.938421634933117e-09, 6.334654191521244e-10, 6.274658733407496e-11], [0.02819802239136082, 0.03910334281221378, 0.027113096760253332, 0.012704687263922907, 0.003976332129458383, 0.001102828249693631, 0.00025488945354773025, 5.049507952296474e-05, 8.752947181507986e-06, 1.3486741473700355e-06, 1.8702612117485975e-07, 2.357788342109802e-08, 2.7247007059736214e-09, 2.906502402288767e-10, 2.8789749417736496e-11], [0.00970348388511648, 0.013456215175882425, 0.009330140030292582, 0.004312828030122986, 0.0015156825822120112, 0.00037950449150050925, 8.771238176420165e-05, 1.7376331702569357e-05, 3.0120581062117385e-06, 4.6410481109795255e-07, 6.435929895112452e-08, 8.11360487081089e-09, 9.376221149565731e-10, 1.0001835884527193e-10, 9.907108578548298e-12], [0.0026713249092975523, 0.0037044347380570694, 0.0025685450468345477, 0.0011873019095806874, 0.0004116199440120479, 0.0001157264190035148, 2.4146819125439873e-05, 4.783624959741258e-06, 8.292058751925718e-07, 1.277659402632082e-07, 1.7717821812098873e-08, 2.2336384593619496e-09, 2.58123096904765e-10, 2.7534598555911228e-11, 2.727381859785903e-12], [0.0006128363152450642, 0.0008498450065116491, 0.0005892572919768743, 0.0002723823391225709, 9.443091287463637e-05, 2.6190236371601093e-05, 6.136126120369839e-06, 1.0974251329887964e-06, 1.9023049999043408e-07, 2.93111510966725e-08, 4.0646963593621934e-09, 5.124254104248933e-10, 5.921676058056056e-11, 6.316791290354087e-12, 6.25696501163141e-13], [0.00012050788986265022, 0.0001671131848707034, 0.00011587132008310698, 5.356115508655503e-05, 1.856885723845467e-05, 5.150037688095541e-06, 1.1902944020826072e-06, 2.3903553112319887e-07, 3.7406850036615465e-08, 5.7637331212867565e-09, 7.992802792753225e-10, 1.0076312938082488e-10, 1.1644360303960615e-11, 1.2421313328974908e-12, 1.230367117187915e-13], [2.073454569051405e-05, 2.875343656866118e-05, 1.9936779104021092e-05, 9.215713748242217e-06, 3.1949511295085886e-06, 8.86113696567037e-07, 2.048016415628419e-07, 4.057239337763692e-08, 7.129297705777596e-09, 9.917059197323927e-10, 1.375238873492008e-10, 1.733726905721411e-11, 2.003524591082485e-12, 2.1372068588153547e-13, 2.1169653901097554e-14], [3.171181095699923e-06, 4.397605611617556e-06, 3.0491691473491605e-06, 1.409468895919805e-06, 4.886419396311145e-07, 1.3552392442722958e-07, 3.132275497068266e-08, 6.205219482832717e-09, 1.0756287324628834e-09, 1.6800646539773397e-10, 2.103316649799908e-11, 2.651595106347255e-12, 3.064228849208597e-13, 3.268685067633831e-14, 3.2377273780531204e-15], [4.3650585465650017e-07, 6.053203957806972e-07, 4.1971118787907367e-07, 1.9401018310164846e-07, 6.72604499846807e-08, 1.8654559507410927e-08, 4.311505876221885e-09, 8.541343278559223e-10, 1.4805784500716751e-10, 2.2813091834753277e-11, 3.2069357459961183e-12, 3.649860267105433e-13, 4.2178412153774725e-14, 4.499270543032583e-15, 4.456657988464374e-16], [5.4621851491853e-08, 7.574633973544702e-08, 5.252026273929517e-08, 2.4277327087914342e-08, 8.416588852466898e-09, 2.3343251142910198e-09, 5.395172393794523e-10, 1.068814952022892e-10, 1.8527113750969855e-11, 2.854700116791072e-12, 3.9587285854183893e-13, 5.0590520969410546e-14, 5.27796578270097e-15, 5.630130382021781e-16, 5.576807463154065e-17], [6.265477868982381e-09, 8.688592610956259e-09, 6.024412114907433e-09, 2.7847656465848884e-09, 9.654369038610963e-10, 2.677621124721781e-10, 6.188609926140298e-11, 1.2259995304142548e-11, 2.1251791730299478e-12, 3.2745247397927614e-13, 4.540916439814629e-14, 5.724612036561265e-15, 6.70611386398492e-16, 6.458121858667537e-17, 6.396957039286588e-18], [6.634067365043982e-10, 9.199730634092721e-10, 6.378820042273041e-10, 2.948589601882187e-10, 1.0222322368452077e-10, 2.8351419142997022e-11, 6.55267738622828e-12, 1.2981234064436096e-12, 2.2502005579598325e-13, 3.467160552881587e-14, 4.808052345041432e-15, 6.061383135243158e-16, 7.004638462583643e-17, 7.574404285774126e-18, 6.773281275161882e-19], [6.522601871663139e-11, 9.045156907648026e-11, 6.271643210312297e-11, 2.8990474467206012e-11, 1.0050567072100789e-11, 2.7875059053638747e-12, 6.442579405965069e-13, 1.276312357805351e-13, 2.2123927243040498e-14, 3.408905376925143e-15, 4.727267526716421e-16, 5.959539873098999e-17, 6.886946639570155e-18, 7.346468149129255e-19, 7.376607471371176e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3764772224720832, "lambda_away": 1.386740611433591, "rho": -0.06050917105558633, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T11:54:57Z", "over": 2.14, "under": 1.78, "bookmaker": "pinnacle", "event_id": "5118966f484adf525196d196a61bc5d6", "kickoff_utc": "2026-11-02T19:45:00Z", "home_team": "Lorient", "away_team": "Brest"}} |
| Legacy p home | 0.3733 |
| Legacy p draw | 0.2807 |
| Legacy p away | 0.3460 |
| Legacy p over 1 5 | 0.7694 |
| Legacy p under 3 5 | 0.7007 |
| Legacy p btts yes | 0.5707 |
| Legacy p over 2 5 | 0.5177 |
| Legacy goal margin distribution | {"-1": 0.18342597373112848, "-10": 5.111794537882013e-07, "-11": 6.353434866629164e-08, "-12": 7.251652418626932e-09, "-13": 7.598444501800002e-10, "-14": 6.623416224921076e-11, "-2": 0.1032674980163888, "-3": 0.041655840794431215, "-4": 0.013249555211975452, "-5": 0.0034636427013195006, "-6": 0.0007668000400211846, "-7": 0.00014702296120835517, "-8": 2.484024239575075e-05, "-9": 3.7492605761808974e-06, "0": 0.2807247324111287, "1": 0.19889288573665845, "10": 5.185815160341149e-07, "11": 6.397731658150377e-08, "12": 7.248167364494775e-09, "13": 7.538583055808784e-10, "14": 6.522601871663139e-11, "2": 0.11117750894261151, "3": 0.04451465211988412, "4": 0.014054071965838612, "5": 0.003646764798145352, "6": 0.000801365406097154, "7": 0.0001525131967930358, "8": 2.557713424967954e-05, "9": 3.831911530596091e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3630 |
| Legacy raw p draw | 0.2693 |
| Legacy raw p away | 0.3677 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3765 |
| Legacy lambda away | 1.3867 |
| Legacy model home team | Lorient |
| Legacy model away team | Brest |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.015438103465453231, "mu": 9.147035869889242, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,498.9880 |
| Elo away rating | 1,450.3969 |
| Elo rating diff | 108.5911 |
| Elo home expectancy | 0.6514 |

</details>


---
