# Premier League — football model report

Fixtures in this report: **10**.

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
| Training sha256 | 45f275a290adb8601b7d5cc5d4a3bf5e7d3874a643c35e7e6bb2e893725be8da |
| Training as of utc | 2026-10-31T11:17:21.264748+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 80, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 80, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 201, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-31T11:17:21.264748+00:00', 'observations': 542, 'observations_sha256': 'eb8e90d9bc19b03240fd86db5f66bf855193910af006457f91259f0af2bba60b', 'eligible_training_matches': 257, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 235, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 18, 'retrospective_eligible_training_matches': 257, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '9fc40be2ef9beec965beb6f74be0c435c286fba2326560358c898ca8f1d1ccd2', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 196, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-21T00:00:00+00:00', 'audit_origin_utc': '2025-10-19T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 31, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-31', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1979, 'tune_start_date': '2025-11-01', 'audit_start_date': '2026-05-02', 'training_shot_matches': 1609, 'tuning_matches': 250, 'audit_matches': 113, 'audit_matchdays': 37, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9335406702974351, 'audit_candidate_poisson_score': 0.9213418851050769, 'audit_gain': 0.012198785192358286, 'audit_gain_lower95': 0.002012891294258251, 'audit_baseline_briers': [0.6395128061328191, 0.15743362581394504, 0.215449165502342, 0.25260755005198404], 'audit_candidate_briers': [0.6378845304392079, 0.15580446095319062, 0.21336731892090813, 0.24930173791012294], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1864.370 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.175 |
| Dixon-Coles low-score adjustment | -0.076 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1980, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 6, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 10.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261031T111721264748Z_f3cdfb344418aece0ddb24ee1bbe4e8dd760fc59628cdb2530737b70a430ca3e.json |
| Over 1 5 in window quote fixtures | 4 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 5, 'ANCHORED_MAIN': 4, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
| Shot features applied fixtures | 10 |
| Goal rate features used | {'shot_features': 10} |
| Legacy comparison status | {'AVAILABLE': 10} |
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

The model's most likely 1X2 outcome is **Aston Villa win** at **45.2%**. Expected goals are 1.56 for Aston Villa and 1.15 for Fulham (2.72 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 54.3%; Under 3.5 goals: 67.8%; Double Chance 1X: 71.9%; Double Chance X2: 54.8%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 57.9%; BTTS No (at least one team does not score): 42.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 45.2% | 2.21 |
| Draw | 26.7% | 3.74 |
| Fulham win | 28.1% | 3.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.56 |
| Fulham expected goals | 1.15 |
| Expected total goals | 2.72 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 78.8% |
| Under 1.5 | 21.2% |
| Over 2.5 | 54.3% |
| Under 2.5 | 45.7% |
| Over 3.5 | 32.2% |
| Under 3.5 | 67.8% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.62% |
| 2 | 2-1 | 9.12% |
| 3 | 1-0 | 8.26% |
| 4 | 2-0 | 7.51% |
| 5 | 1-2 | 7.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 45.2% | 44.8% | 2.19 | -1.1% |
| Draw | 26.7% | 26.7% | 3.64 | -2.7% |
| Fulham win | 28.1% | 28.5% | 3.41 | -4.2% |

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
| Market best home last update utc | 2026-10-31T11:18:04Z |
| Market best draw last update utc | 2026-10-31T11:18:04Z |
| Market best away last update utc | 2026-10-31T11:18:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Aston Villa |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5968 |
| Dc lambda away | 1.1022 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:17:21.264748+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.4880 |
| Shot lambda away | 1.2702 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.9% |
| P btts no | 42.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.83 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.71 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.20 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.16205179512132062, "-10": 1.361827970528629e-07, "-11": 1.4824847166449579e-08, "-12": 1.482664173606743e-09, "-13": 1.3707635358300203e-10, "-14": 1.1703021237293365e-11, "-15": 8.364739582935527e-13, "-2": 0.08054207831701336, "-3": 0.028308603818124393, "-4": 0.007861025889604672, "-5": 0.0017961488688824918, "-6": 0.00034780268130896836, "-7": 5.8355670848770055e-05, "-8": 8.630648478726946e-06, "-9": 1.1405796573090503e-06, "0": 0.2673345546881774, "1": 0.20997793157030661, "10": 2.716223083960724e-06, "11": 4.012828880965742e-07, "12": 5.4465367602533836e-08, "13": 6.833723747073287e-09, "14": 7.917901566021071e-10, "15": 7.680363231163485e-11, "2": 0.13961374576985963, "3": 0.06659490864143311, "4": 0.02509683950930854, "5": 0.00778214584798393, "6": 0.0020450653587873132, "7": 0.0004656660350965728, "8": 9.346567669031808e-05, "9": 1.676299353590463e-05} |
| Raw goal margin distribution | {"-1": 0.15984011488182712, "-10": 8.867176799784893e-08, "-11": 9.167272122429127e-09, "-12": 8.705343103694207e-10, "-13": 7.641177626801608e-11, "-14": 6.2004328992873045e-12, "-15": 4.253158078173796e-13, "-2": 0.07699309510112463, "-3": 0.025983234708733333, "-4": 0.00689899457072561, "-5": 0.00150358653191691, "-6": 0.0002772947715622756, "-7": 4.4266980365084536e-05, "-8": 6.224825027404453e-06, "-9": 7.81770867160835e-07, "0": 0.26904266774323277, "1": 0.22014395021284158, "10": 1.8791336352547925e-06, "11": 2.6365113873239536e-07, "12": 3.3977596196885786e-08, "13": 4.047476010184274e-09, "14": 4.457211370062307e-10, "15": 4.1492535299496515e-11, "2": 0.14180326749660754, "3": 0.06494487808475216, "4": 0.023402094165453458, "5": 0.006921728751127901, "6": 0.0017323875740836974, "7": 0.0003753189622444427, "8": 7.16250580804294e-05, "9": 1.2207719754721244e-05} |
| Unadjusted home-win probability | 45.9% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 27.2% |
| Raw p over 1 5 | 76.3% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 55.0% |
| P home draw | 71.9% |
| P draw away | 54.8% |
| P home away | 73.3% |
| Raw p home draw | 72.8% |
| Raw p draw away | 54.1% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0545 |
| Totals anchor target over 2 5 | 0.5430 |
| Totals anchor reference over odds | 1.79 |
| Totals anchor reference under odds | 2.11 |
| Totals anchor reference last update utc | 2026-10-31T11:18:04Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5109 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.31, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.6, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.99, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.12, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 6.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:19Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.19 |
| Reference draw odds | 3.64 |
| Reference away odds | 3.41 |
| Market reference 1x2 last update utc | 2026-10-31T11:18:04Z |
| Market reference home last update utc | 2026-10-31T11:18:04Z |
| Market reference draw last update utc | 2026-10-31T11:18:04Z |
| Market reference away last update utc | 2026-10-31T11:18:04Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.14 |
| Market reference over 2 5 last update utc | 2026-10-31T11:17:43Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:17:43Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | 0.0110 |
| Raw ev home | 0.0061 |
| Raw edge prob draw | 0.0024 |
| Raw ev draw | -0.0207 |
| Raw edge prob away | -0.0135 |
| Raw ev away | -0.0740 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08611121484425885, 0.07178633201581339, 0.04403598487607415, 0.015136807091367164, 0.0039023130100199867, 0.0008048221391078505, 0.0001383236629863139, 2.0377282112287617e-05, 2.6266613763274573e-06, 3.009604278539025e-07, 3.1035390383888095e-08, 2.909459689521665e-09, 2.5002239750249396e-10, 1.9832770212292396e-11, 1.4608417134096655e-12, 1.0042913435061428e-13], [0.10132043029666991, 0.13036304123789266, 0.06825675669623266, 0.02346238790164121, 0.0060486720219171735, 0.0012474922290808888, 0.00021440475639091075, 3.158524082481946e-05, 4.071383596663603e-06, 4.664953618507394e-07, 4.81055458704323e-08, 4.509727276545503e-09, 3.8754028104430394e-10, 3.074123526026195e-11, 2.2643371707143837e-12, 1.5566739356175074e-13], [0.08784432788092494, 0.09058609559520604, 0.047233527103890754, 0.018183611732788492, 0.00468778813165172, 0.0009668203606714286, 0.00016616607227786515, 2.4478913146132156e-05, 3.1553675971658567e-06, 3.6153909698369425e-07, 3.7282333408212024e-08, 3.4950888273283093e-09, 3.003480306807313e-10, 2.382479944080239e-11, 1.754886506735788e-12, 1.2064396240691476e-13], [0.04538688780843065, 0.04680348813592743, 0.024132151458983734, 0.008388679833798736, 0.0024220586477635316, 0.0004995310260690055, 8.585370349996962e-05, 1.2647620073339676e-05, 1.6302966689101634e-06, 1.8679788244726773e-07, 1.9262815533505425e-08, 1.8058218249615132e-09, 1.5518204420059708e-10, 1.2309656472570802e-11, 9.067043817070564e-13, 6.233360899464726e-14], [0.017587671577333434, 0.018136612086793274, 0.00935134297170814, 0.0032144046512484294, 0.0008380296568696032, 0.00019357105220063414, 3.3268787832038804e-05, 4.901023155050284e-06, 6.317490308530608e-07, 7.238521886961431e-08, 7.464448205570073e-09, 6.997660055181074e-10, 6.013390562532412e-11, 4.7700603791819644e-12, 3.513529931926892e-13, 2.4154620335614515e-14], [0.005452256481083247, 0.005622430482642886, 0.0028989579490463872, 0.000996479750917123, 0.00025689538571467297, 5.358029876126213e-05, 1.0313472325056832e-05, 1.5193389951345333e-06, 1.958450118164473e-07, 2.2439740074809898e-08, 2.3140121719682526e-09, 2.1693057674245562e-10, 1.864177843194814e-11, 1.4787399516301656e-12, 1.0892099194936653e-13, 7.48803982914302e-15], [0.001408519816698655, 0.0014524820650476244, 0.000748908224177428, 0.0002574276322061155, 6.636559429164475e-05, 1.3687394994665412e-05, 2.3789668021133576e-06, 3.925015432334972e-07, 5.0594021228114066e-08, 5.797016095372149e-09, 5.97795061844123e-10, 5.604120371991573e-11, 4.815861915338174e-12, 3.8201330638819914e-13, 2.8138326974793504e-14, 1.934438066912304e-15], [0.00031189100946413267, 0.0003216256470981351, 0.00016583205948934233, 5.7002651379738655e-05, 1.4695449756484728e-05, 3.030823841602958e-06, 5.209034832236307e-07, 7.76029182330922e-08, 1.1203122715498336e-08, 1.2836434251263814e-09, 1.3237080734031762e-10, 1.2409301873194094e-11, 1.0663847369469024e-12, 8.458987537527643e-14, 6.230719014923009e-15, 4.283460085419613e-16], [6.042975082948118e-05, 6.231586395486033e-05, 3.213042290541911e-05, 1.1044422298083334e-05, 2.8472842761235677e-06, 5.872305516943092e-07, 1.0092649913665688e-07, 1.4868083313530353e-08, 1.9381341351511616e-09, 2.4870948498183475e-10, 2.564721220536672e-11, 2.404336763196023e-12, 2.0661500968810024e-13, 1.6389523700626798e-14, 1.2072191443004948e-15, 8.299323090289423e-17], [1.0407495423445387e-05, 1.0732330681758374e-05, 5.533652294630606e-06, 1.9021222650122813e-06, 4.903726668776414e-07, 1.0113560283429529e-07, 1.738203556114414e-08, 2.560651118314406e-09, 3.300716628283988e-10, 3.82458716453182e-11, 4.417083307271656e-12, 4.140861664313924e-13, 3.5584207087197906e-14, 2.8226807253937447e-15, 2.079129492831458e-16, 1.4293483903915577e-17], [1.613184955291493e-06, 1.663535143337529e-06, 8.577284222871302e-07, 2.948331847574309e-07, 7.600885482122056e-08, 1.5676243543579677e-08, 2.6942542003344642e-09, 3.9690662275089807e-10, 5.11618424009402e-11, 5.86207651947493e-12, 6.113224073703286e-13, 6.418427745609439e-14, 5.515631300661297e-15, 4.3752179506498723e-16, 3.2226969904620867e-17, 2.215521819068395e-18], [2.2731568967604244e-07, 2.3441059078050694e-07, 1.20863467779931e-07, 4.154527260664248e-08, 1.0710492432065798e-08, 2.2089569462879886e-09, 3.7965036166664323e-10, 5.5928554498145826e-11, 7.209272224067611e-12, 8.260317346670245e-13, 8.518135602636822e-14, 8.075523696658319e-15, 7.772137528285077e-16, 6.165168368776825e-17, 4.541138240849914e-18, 3.121916483549468e-19], [2.9362031542912294e-08, 3.0278469428568213e-08, 1.5611755433149573e-08, 5.3663414367639715e-09, 1.3834584716902788e-09, 2.8532770274800306e-10, 4.9038875892907146e-11, 7.224208692608874e-12, 9.312110340741879e-13, 1.0669729785614501e-13, 1.1002749814932221e-14, 1.0314694503426057e-15, 8.963837095062807e-17, 7.963456828227407e-18, 5.865721123719391e-19, 4.032533363401104e-20], [3.500907878604221e-09, 3.61017704172242e-09, 1.8614283386651033e-09, 6.398422053252746e-10, 1.6495318643683535e-10, 3.4020329999122735e-11, 5.847026855769972e-12, 8.613603282753972e-13, 1.1103060226159523e-13, 1.2721783577694154e-14, 1.3118851622072316e-15, 1.2298466201040756e-16, 1.0568601504470861e-17, 8.477991994273864e-19, 6.993844845412767e-20, 4.808089590814821e-21], [3.8760608099147707e-10, 3.9970391205647204e-10, 2.0608966828459146e-10, 7.084068997495351e-11, 1.8262936460735793e-11, 3.766590622274263e-12, 6.473586976874373e-13, 9.536626290705745e-14, 1.2292850341979994e-14, 1.4085034073326494e-15, 1.4524651435179874e-16, 1.3616354533419169e-17, 1.1701119688821395e-18, 9.281793164654786e-20, 6.913893448701957e-21, 5.323318487588039e-22], [4.0053203516275636e-11, 4.1303330677625355e-11, 2.1296238194431178e-11, 7.320309747314285e-12, 1.8871972003007507e-12, 3.8921995333650015e-13, 6.68946926740198e-14, 9.854655342435176e-15, 1.270279442683124e-15, 1.4554744209109246e-16, 1.5009022006262507e-17, 1.407043506339604e-18, 1.2091330638204526e-19, 9.591323997521826e-21, 7.064775133492306e-22, 4.9116330794938066e-23]] |
| Legacy trial inputs | {"lambda_home": 1.5500222576676885, "lambda_away": 1.031211664775871, "rho": -0.10288407687222552, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4646 |
| Legacy p draw | 0.2730 |
| Legacy p away | 0.2624 |
| Legacy p over 1 5 | 0.7408 |
| Legacy p under 3 5 | 0.7408 |
| Legacy p btts yes | 0.5187 |
| Legacy p over 2 5 | 0.4785 |
| Legacy goal margin distribution | {"-1": 0.16085304757498123, "-10": 3.585813418861993e-08, "-11": 3.321755629008814e-09, "-12": 2.825808528784863e-10, "-13": 2.2217751345413695e-11, "-14": 1.6165091069714162e-12, "-15": 1.0042913435061428e-13, "-2": 0.07272053196599478, "-3": 0.022243255977449864, "-4": 0.005329273730636842, "-5": 0.0010454108616690333, "-6": 0.0001732587555712021, "-7": 2.483018641757939e-05, "-8": 3.13230653462362e-06, "-9": 3.5272112551167297e-07, "0": 0.2729905315221917, "1": 0.21952420089040398, "10": 1.8638657958668888e-06, "11": 2.59528315330451e-07, "12": 3.318561856266662e-08, "13": 3.921908028855124e-09, "14": 4.2890941166910244e-10, "15": 4.0053203516275636e-11, "2": 0.14506513869676016, "3": 0.06669518594304409, "4": 0.024018964106539278, "5": 0.007082121463815742, "6": 0.0017642562766916638, "7": 0.00038004636066217925, "8": 7.206277334214836e-05, "9": 1.2197429162671363e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4809 |
| Legacy raw p draw | 0.2794 |
| Legacy raw p away | 0.2398 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5500 |
| Legacy lambda away | 1.0312 |
| Legacy model home team | Aston Villa |
| Legacy model away team | Fulham |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 71.3% |
| Market home draw odds | 1.36 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:18:01Z |
| Market reference home draw last update utc | 2026-10-31T11:18:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.7% |
| Market draw away odds | 1.74 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:18:01Z |
| Market reference draw away last update utc | 2026-10-31T11:18:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.9% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:18:01Z |
| Market reference home away last update utc | 2026-10-31T11:18:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.74 |
| Market reference dc home away odds | 1.33 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.75, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.07, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.66, "price": 2.2, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.2, "price": 1.66, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 79.2% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.04 |
| Market reference over 1 5 last update utc | 2026-10-31T11:18:19Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.9% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 2.86 |
| Market reference under 3 5 last update utc | 2026-10-31T11:18:19Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:18:01Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-31T11:18:05Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 9.73459078630861, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,530.3526 |
| Elo away rating | 1,453.3052 |
| Elo rating diff | 137.0473 |
| Elo home expectancy | 0.6876 |

</details>


---

## 2026-10-31 — Bournemouth vs Leeds United

The model's most likely 1X2 outcome is **Bournemouth win** at **46.4%**. Expected goals are 1.64 for Bournemouth and 1.19 for Leeds United (2.83 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 48.0%; Under 3.5 goals: 73.7%; Double Chance 1X: 74.2%; Double Chance X2: 53.6%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 87.8%; BTTS Yes (both teams score): 52.7%; BTTS No (at least one team does not score): 47.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 46.4% | 2.16 |
| Draw | 27.8% | 3.59 |
| Leeds United win | 25.8% | 3.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.64 |
| Leeds United expected goals | 1.19 |
| Expected total goals | 2.83 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 48.0% |
| Under 2.5 | 52.0% |
| Over 3.5 | 26.3% |
| Under 3.5 | 73.7% |
| Over 4.5 | 12.2% |
| Under 4.5 | 87.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.28% |
| 2 | 1-0 | 10.41% |
| 3 | 2-1 | 9.33% |
| 4 | 2-0 | 8.54% |
| 5 | 0-0 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 46.4% | 46.1% | 2.13 | -1.3% |
| Draw | 27.8% | 28.6% | 3.40 | -5.4% |
| Leeds United win | 25.8% | 25.3% | 3.82 | -1.4% |
| Over 2.5 | 48.0% | 48.0% | 2.03 | -2.5% |
| Under 2.5 | 52.0% | 52.0% | 1.88 | -2.3% |

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
| Market best home last update utc | 2026-10-31T11:18:04Z |
| Market best draw last update utc | 2026-10-31T11:18:04Z |
| Market best away last update utc | 2026-10-31T11:18:04Z |
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
| Dc lambda home | 1.6062 |
| Dc lambda away | 1.1733 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:17:21.264748+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7240 |
| Shot lambda away | 1.2382 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.7% |
| P btts no | 47.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.84 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.87 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.80 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.20 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.1551964796571106, "-10": 5.6051931059866183e-08, "-11": 5.500420068537087e-09, "-12": 4.956982634897531e-10, "-13": 4.1288779369553705e-11, "-14": 3.181823090241953e-12, "-15": 2.0890614527386274e-13, "-2": 0.07216752622832948, "-3": 0.023323865697815915, "-4": 0.005910417771682666, "-5": 0.0012269597957737472, "-6": 0.00021526973729584184, "-7": 3.2667173954100484e-05, "-8": 4.364234817809916e-06, "-9": 5.205191103656461e-07, "0": 0.27831877865434546, "1": 0.2267758219665516, "10": 1.4282182540033236e-06, "11": 1.9288622657174332e-07, "12": 2.3923466859426973e-08, "13": 2.742458855875506e-09, "14": 2.9086098118098736e-10, "15": 2.628221780671553e-11, "2": 0.1428679944608108, "3": 0.06354699527618093, "4": 0.022162259045010374, "5": 0.006331805100387111, "6": 0.0015289086781724347, "7": 0.0003193092420806568, "8": 5.870963662497897e-05, "9": 9.636943666718515e-06} |
| Raw goal margin distribution | {"-1": 0.1564123283917034, "-10": 1.1259195695453996e-07, "-11": 1.2032091332870276e-08, "-12": 1.1812391686761708e-09, "-13": 1.0719966982740281e-10, "-14": 8.986240141677895e-12, "-15": 6.320470193355887e-13, "-2": 0.07669983082633564, "-3": 0.02653065747118538, "-4": 0.007243569849826312, "-5": 0.001626365644601199, "-6": 0.00030935707236955996, "-7": 5.097546824577381e-05, "-8": 7.40292001671999e-06, "-9": 9.605425500397715e-07, "0": 0.26142734615225427, "1": 0.21854275469443246, "10": 2.7448647886715484e-06, "11": 4.0369750671857897e-07, "12": 5.4544899439071414e-08, "13": 6.812572117161143e-09, "14": 7.859538469230731e-10, "15": 7.607987147065314e-11, "2": 0.14527708721820554, "3": 0.06915953890885919, "4": 0.025987116164223226, "5": 0.008030174556574534, "6": 0.002102171782067732, "7": 0.00047672808263012214, "8": 9.528267208775958e-05, "9": 1.7014877925172383e-05} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 26.9% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.0% |
| P home draw | 74.2% |
| P draw away | 53.6% |
| P home away | 72.2% |
| Raw p home draw | 73.1% |
| Raw p draw away | 53.0% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9162 |
| Totals anchor target over 2 5 | 0.4801 |
| Totals anchor reference over odds | 2.03 |
| Totals anchor reference under odds | 1.88 |
| Totals anchor reference last update utc | 2026-10-31T11:18:04Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5326 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.5, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.24, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.93, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.53, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 3.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:41Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.96, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.67, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.96, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.13 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.82 |
| Market reference 1x2 last update utc | 2026-10-31T11:18:04Z |
| Market reference home last update utc | 2026-10-31T11:18:04Z |
| Market reference draw last update utc | 2026-10-31T11:18:04Z |
| Market reference away last update utc | 2026-10-31T11:18:04Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market best over 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market best under 2 5 last update utc | 2026-10-31T11:18:04Z |
| Home probability edge | +0.3% |
| Draw probability edge | -0.7% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0087 |
| Raw ev home | 0.0004 |
| Raw edge prob draw | -0.0241 |
| Raw ev draw | -0.1111 |
| Raw edge prob away | 0.0154 |
| Raw ev away | 0.0271 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08738379159966696, 0.06869879808164077, 0.04626684317250476, 0.017679280322040747, 0.005066645970526932, 0.0011616265333449314, 0.000221937782052201, 3.634537633592249e-05, 5.208050079111755e-06, 6.633589770867919e-07, 7.604393452779859e-08, 7.92479182492403e-09, 7.570465508327023e-10, 6.675675247491886e-11, 5.466169998703202e-12, 4.1774171336778196e-13], [0.09918232726272135, 0.13660163206463702, 0.06697367218799838, 0.02559168172320295, 0.007334234692812804, 0.0016815150832542227, 0.0003212665321875438, 5.26118307055382e-05, 7.538924526071712e-06, 9.6024676913291e-07, 1.1007756729720007e-07, 1.1471550109042335e-08, 1.0958644257937033e-09, 9.663388617029176e-11, 7.912566592280012e-12, 6.047029503619357e-13], [0.08138433465558069, 0.09329465990369358, 0.05138261970741732, 0.01852264802332519, 0.0053083439066164565, 0.0012170404575167638, 0.0002325250431662285, 3.8079186532626624e-05, 5.456493519307614e-06, 6.950036778574797e-07, 7.967151421945492e-08, 8.302833993089192e-09, 7.931604987825584e-10, 6.994129889617772e-11, 5.726926723109514e-12, 4.3766955330900324e-13], [0.039269358477291995, 0.045016297783592694, 0.025802141220525956, 0.009473794186719389, 0.002561368360039496, 0.0005872432109920312, 0.00011219738188787027, 1.8373870509622033e-05, 2.6328531276383437e-06, 3.353513754744475e-07, 3.844289279445383e-08, 4.006261964687665e-09, 3.827137506073375e-10, 3.374789448540504e-11, 2.7633418570627743e-12, 2.1118317986161676e-13], [0.014211111896510914, 0.01629086060418392, 0.009337486790534325, 0.003567998920041121, 0.0009825489037325397, 0.00021251630547262305, 4.060289269625075e-05, 6.649284325213328e-06, 9.527981065843839e-07, 1.2135965817399478e-07, 1.391202383516071e-08, 1.4498183641027538e-09, 1.3849953615512447e-10, 1.221296001260287e-11, 1.0000204195273479e-12, 7.642467094057261e-14], [0.004114265354285076, 0.004716374331816878, 0.0027032999724547918, 0.0010329729614229467, 0.0002960362750814005, 6.52175348848912e-05, 1.1754961604725178e-05, 1.925037275706247e-06, 2.758450055207149e-07, 3.5134888858044595e-08, 4.027676236019421e-09, 4.1973756232956873e-10, 4.009706258997819e-11, 3.5357795096566408e-12, 2.8951635843843725e-13, 2.212574062840459e-14], [0.0009926023340478616, 0.0011378663666233907, 0.0006521946523199927, 0.0002492137196374194, 7.142132854960052e-05, 1.637472023357761e-05, 3.0061599933151146e-06, 4.644320014519801e-07, 6.655000899009467e-08, 8.476597808812795e-09, 9.717119554522958e-10, 1.0126534099750275e-10, 9.673765420556244e-12, 8.530375879398383e-13, 6.984834189941706e-14, 5.338027545408111e-15], [0.0002052633894264846, 0.00023530300011993942, 0.00013486940369674197, 5.153569665280656e-05, 1.4769443383886567e-05, 3.386180407563408e-06, 6.469560979458838e-07, 1.0180432370318004e-07, 1.376208773957122e-08, 1.7529025848110993e-09, 2.0094340168331498e-10, 2.0940981510500753e-11, 2.000468677765925e-12, 1.7640235228409326e-13, 1.4444160478271617e-14, 1.1038676711086333e-15], [3.7141184736741654e-05, 4.257667293219016e-05, 2.4403813325069043e-05, 9.325076601661125e-06, 2.672442595401278e-06, 6.127091266525697e-07, 1.1706284309884456e-07, 1.917065696538242e-08, 2.6395899224308014e-09, 3.1717725654773135e-10, 3.6359508748257654e-11, 3.7891455705926574e-12, 3.6197286290831764e-13, 3.1918952388369404e-14, 2.6135845958188634e-15, 1.9973826414985889e-16], [5.973756103763157e-06, 6.847995334812027e-06, 3.925088277044476e-06, 1.4998372739608825e-06, 4.298333609816772e-07, 9.854760722135443e-08, 1.882828666996745e-08, 3.0833919238664985e-09, 4.4182950272972824e-10, 5.407563838348115e-11, 5.848032012287096e-12, 6.094429039034686e-13, 5.8219402922172e-14, 5.1338167591386065e-15, 4.2036669111767274e-16, 3.212573005082212e-17], [8.647323992535716e-07, 9.912830944368344e-07, 5.681770303532475e-07, 2.1710927963482038e-07, 6.222062418764742e-08, 1.4265280897480553e-08, 2.725492842886327e-09, 4.4633708672580835e-10, 6.395712836615637e-11, 8.146337805111519e-12, 8.973293388502506e-13, 8.822004369554431e-14, 8.427562675397133e-15, 7.431467917917746e-16, 6.085027427676216e-17, 4.650367229944308e-18], [1.1379502874821962e-07, 1.3044855070358666e-07, 7.476962995596791e-08, 2.857063842973338e-08, 8.18796395772523e-09, 1.8772490208895377e-09, 3.586630230080805e-10, 5.873602244949097e-11, 8.41648036706227e-12, 1.0720226806877618e-12, 1.22890961543239e-13, 1.2305994301911798e-14, 1.109030652433113e-15, 9.779489077671784e-17, 8.007631860027823e-18, 6.119681338158273e-19], [1.37270206722184e-08, 1.573592424789541e-08, 9.019412072302408e-09, 3.446457623480002e-09, 9.877087931473623e-10, 2.264513344749746e-10, 4.326528834652009e-11, 7.0852883753997995e-12, 1.015274579714816e-12, 1.293174021814914e-13, 1.482425715859078e-14, 1.5448852386514287e-15, 1.4180920749942894e-16, 1.1796934383659087e-17, 9.65955448909154e-19, 7.382131992967404e-20], [1.5285061106391413e-09, 1.752197868991458e-09, 1.0043130841048487e-09, 3.837636485978057e-10, 1.0998154384026088e-10, 2.5215395006136383e-11, 4.817597291891674e-12, 7.889480781038896e-13, 1.1305099891132385e-13, 1.4399514954212215e-14, 1.650683581940739e-15, 1.7202323678975714e-16, 1.64331885242943e-17, 1.3924125781784756e-18, 1.0755930522134253e-19, 8.220016659282741e-21], [1.5804231678028373e-10, 1.8117128138734884e-10, 1.0384254631361083e-10, 3.9679851914423064e-11, 1.1371716390665285e-11, 2.6071858120563415e-12, 4.981231229796064e-13, 8.157453948990317e-14, 1.1689087572440238e-14, 1.4888607170333434e-15, 1.7067505045956684e-16, 1.7786615763628444e-17, 1.6991356255557623e-18, 1.498306494518443e-19, 1.1788595845903214e-20, 8.49921676964937e-22], [1.5251633913311416e-11, 1.748365953889944e-11, 1.0021167325730183e-11, 3.8292438851965005e-12, 1.0974102309418104e-12, 2.5160250975530835e-13, 4.8070615960421877e-14, 7.872227124312689e-15, 1.1280376551512135e-15, 1.4368024378984382e-16, 1.647073670379152e-17, 1.716470358763036e-18, 1.6397250469359606e-19, 1.4459179420978368e-20, 1.1839451415272691e-21, 8.694202937136756e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4475522338597584, "lambda_away": 1.1463466562516915, "rho": -0.10288407687222552, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T11:18:04Z", "over": 2.03, "under": 1.88, "bookmaker": "pinnacle", "event_id": "a6c06eabdf4e6710354b6098d39449e7", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Bournemouth", "away_team": "Leeds United"}} |
| Legacy p home | 0.4441 |
| Legacy p draw | 0.2859 |
| Legacy p away | 0.2700 |
| Legacy p over 1 5 | 0.7447 |
| Legacy p under 3 5 | 0.7367 |
| Legacy p btts yes | 0.5341 |
| Legacy p over 2 5 | 0.4805 |
| Legacy goal margin distribution | {"-1": 0.15698123643728498, "-10": 8.834341517626905e-08, "-11": 9.093437316141916e-09, "-12": 8.596185469059652e-10, "-13": 7.510698862050787e-11, "-14": 6.070872949065138e-12, "-15": 4.1774171336778196e-13, "-2": 0.07779670828317721, "-3": 0.026349686664978243, "-4": 0.007000048893472553, "-5": 0.0015237305958253036, "-6": 0.00028035579926673226, "-7": 4.461923821575431e-05, "-8": 6.252116730696682e-06, "-9": 7.821345999420871e-07, "0": 0.28589271465595045, "1": 0.2221602048791522, "10": 1.004595748996959e-06, "11": 1.3057604334236523e-07, "12": 1.5586890331408666e-08, "13": 1.7196985593522203e-09, "14": 1.7552597631918317e-10, "15": 1.5251633913311416e-11, "2": 0.13684601991136697, "3": 0.058528134209249905, "4": 0.019633990352761924, "5": 0.005396770665711617, "6": 0.001253873126706109, "7": 0.0002519906792309461, "8": 4.4586941170520164e-05, "9": 7.0433679225797065e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4273 |
| Legacy raw p draw | 0.2862 |
| Legacy raw p away | 0.2865 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4476 |
| Legacy lambda away | 1.1463 |
| Legacy model home team | Bournemouth |
| Legacy model away team | Leeds |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 74.6% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:18:01Z |
| Market reference home draw last update utc | 2026-10-31T11:18:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.5% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:18:01Z |
| Market reference draw away last update utc | 2026-10-31T11:18:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.8% |
| Market home away odds | 1.37 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:18:01Z |
| Market reference home away last update utc | 2026-10-31T11:18:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.30 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.37 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.55, "price": 1.5, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.5, "price": 2.55, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.58, "price": 2.34, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.34, "price": 1.58, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 74.9% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.63 |
| Market reference over 1 5 last update utc | 2026-10-31T11:18:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.2% |
| Market under 3 5 odds | 1.34 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.45 |
| Market reference under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.0% |
| Market btts yes odds | 1.79 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:18:01Z |
| Market reference btts yes odds | 1.84 |
| Market reference btts yes opposite odds | 2.16 |
| Market reference btts yes last update utc | 2026-10-31T11:18:04Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 9.997892027272577, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,502.9673 |
| Elo away rating | 1,455.9965 |
| Elo rating diff | 106.9708 |
| Elo home expectancy | 0.6493 |

</details>


---

## 2026-10-31 — Brentford vs Nottingham Forest

The model's most likely 1X2 outcome is **Brentford win** at **44.8%**. Expected goals are 1.58 for Brentford and 1.20 for Nottingham Forest (2.78 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 56.7%; Under 3.5 goals: 65.4%; Double Chance 1X: 71.3%; Double Chance X2: 55.2%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 82.1%; BTTS Yes (both teams score): 60.1%; BTTS No (at least one team does not score): 39.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 44.8% | 2.23 |
| Draw | 26.5% | 3.77 |
| Nottingham Forest win | 28.7% | 3.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.58 |
| Nottingham Forest expected goals | 1.20 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 56.7% |
| Under 2.5 | 43.3% |
| Over 3.5 | 34.6% |
| Under 3.5 | 65.4% |
| Over 4.5 | 17.9% |
| Under 4.5 | 82.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.37% |
| 2 | 2-1 | 9.11% |
| 3 | 1-0 | 7.57% |
| 4 | 1-2 | 7.21% |
| 5 | 2-0 | 7.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 44.8% | 44.6% | 2.20 | -1.4% |
| Draw | 26.5% | 26.4% | 3.67 | -2.7% |
| Nottingham Forest win | 28.7% | 28.9% | 3.36 | -3.6% |

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
| Market best home last update utc | 2026-10-31T11:18:04Z |
| Market best draw last update utc | 2026-10-31T11:18:04Z |
| Market best away last update utc | 2026-10-31T11:18:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Brentford |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6215 |
| Dc lambda away | 1.1274 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:17:21.264748+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.4728 |
| Shot lambda away | 1.3686 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 60.1% |
| P btts no | 39.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.21 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.12 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.31 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.59 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.1613861311172635, "-10": 2.1290894571729395e-07, "-11": 2.4477483391190986e-08, "-12": 2.5858312880408758e-09, "-13": 2.52538036467353e-10, "-14": 2.2753643266535596e-11, "-15": 1.703005329481883e-12, "-2": 0.0832822321362965, "-3": 0.030644320414130646, "-4": 0.008938085717641915, "-5": 0.0021492233481784054, "-6": 0.00043850483754787355, "-7": 7.75850442704993e-05, "-8": 1.2106988239616722e-05, "-9": 1.6888546608285286e-06, "0": 0.2650789367311779, "1": 0.20637595267280873, "10": 3.1467860675763204e-06, "11": 4.7549035810906683e-07, "12": 6.602019113714789e-08, "13": 8.474323362682102e-09, "14": 1.0035310588886069e-09, "15": 9.87182667190863e-11, "2": 0.13823325598512093, "3": 0.06685160164633218, "4": 0.025627602449917998, "5": 0.008099284490235703, "6": 0.002171906544440974, "7": 0.0005050639819678527, "8": 0.00010358721279460652, "9": 1.899170452880923e-05} |
| Raw goal margin distribution | {"-1": 0.16254859310816216, "-10": 1.2576820642131466e-07, "-11": 1.3526254680989168e-08, "-12": 1.3363392269754909e-09, "-13": 1.2204006438162889e-10, "-14": 1.0298464960500197e-11, "-15": 7.314746976705463e-13, "-2": 0.08064756687635012, "-3": 0.028175134208923463, "-4": 0.007758941949434266, "-5": 0.0017557295346260252, "-6": 0.000336414874057855, "-7": 5.582265805988003e-05, "-8": 8.161844929958504e-06, "-9": 1.0660246015331024e-06, "0": 0.2667462037537442, "1": 0.216444269478317, "10": 1.9345826021749507e-06, "11": 2.7346113480541494e-07, "12": 3.550883380671509e-08, "13": 4.262101239688645e-09, "14": 4.72710740593793e-10, "15": 4.412898348923271e-11, "2": 0.13931393246822968, "3": 0.06396919956900853, "4": 0.02315309569219193, "5": 0.00688598099912536, "6": 0.001734143511957339, "7": 0.0003782004134672706, "8": 7.26777489528862e-05, "9": 1.2476190478641991e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 28.1% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.3% |
| P home draw | 71.3% |
| P draw away | 55.2% |
| P home away | 73.5% |
| Raw p home draw | 71.9% |
| Raw p draw away | 54.8% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0711 |
| Totals anchor target over 2 5 | 0.5674 |
| Totals anchor reference over odds | 1.72 |
| Totals anchor reference under odds | 2.23 |
| Totals anchor reference last update utc | 2026-10-31T11:18:04Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5255 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.6, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.8, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.83, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.07, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 6.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:40Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.22, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.22, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.20 |
| Reference draw odds | 3.67 |
| Reference away odds | 3.36 |
| Market reference 1x2 last update utc | 2026-10-31T11:18:04Z |
| Market reference home last update utc | 2026-10-31T11:18:04Z |
| Market reference draw last update utc | 2026-10-31T11:18:04Z |
| Market reference away last update utc | 2026-10-31T11:18:04Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.19 |
| Market reference over 2 5 last update utc | 2026-10-31T11:17:43Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:17:43Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | 0.0057 |
| Raw ev home | -0.0057 |
| Raw edge prob draw | 0.0024 |
| Raw ev draw | -0.0210 |
| Raw edge prob away | -0.0081 |
| Raw ev away | -0.0549 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.0798509831714436, 0.06786176502883921, 0.04361338672775827, 0.015611942035085459, 0.004191363347249669, 0.0009002096814957475, 0.0001611205001650273, 2.4717875122758636e-05, 3.318023970963897e-06, 3.959090070904254e-07, 4.2516132776705685e-08, 4.150681811668299e-09, 3.714467547220215e-10, 3.068397275521308e-11, 2.3536502371102666e-12, 1.685035436573597e-13], [0.09445000859236251, 0.12852639603324018, 0.06974326011058651, 0.024965447902062763, 0.006702514206702549, 0.001439547870073268, 0.0002576518311293015, 3.952697378968624e-05, 5.305935315333184e-06, 6.331080187372285e-07, 6.798861380913514e-08, 6.637459343262105e-09, 5.939898177025322e-10, 4.906751008471778e-11, 3.7637811005318894e-12, 2.6945824107191183e-13], [0.08489880193586209, 0.09117167508300546, 0.0500314714986929, 0.01996143681387932, 0.005359079250493516, 0.0011510085443589358, 0.0002060087512646994, 3.160428736716132e-05, 4.242427091676698e-06, 5.06209452438437e-07, 5.4361148413530386e-08, 5.307063818962057e-09, 4.749320044515255e-10, 3.923254275320063e-11, 3.0093783582121462e-12, 2.1544871432855855e-13], [0.045254600867164686, 0.048598303770991134, 0.02609453054674023, 0.009546442723813029, 0.0028566126607982674, 0.0006135355397477898, 0.00010981125293935294, 1.684640275103709e-05, 2.2613905068638785e-06, 2.6983074204738283e-07, 2.8976758423440754e-08, 2.828886267266027e-09, 2.5315855831196914e-10, 2.0912580894149228e-11, 1.6041241260631591e-12, 1.1484314680492784e-13], [0.018091941696599747, 0.019428691481761854, 0.01043210449778393, 0.00373429863954361, 0.0010246189717466293, 0.0002452800157599604, 4.39004818900265e-05, 6.734876245264655e-06, 9.040615632323605e-07, 1.0787327607641212e-07, 1.1584365211664524e-08, 1.1309357376483519e-09, 1.0120804933004262e-10, 8.360458097353187e-12, 6.412987764057586e-13, 4.5912138797722537e-14], [0.005786255506951682, 0.006213781525746248, 0.00333644796737005, 0.0011943221147856329, 0.00032064159125574226, 7.038225685598917e-05, 1.4040472236417804e-05, 2.153981889634585e-06, 2.8914150214510945e-07, 3.450057203464067e-08, 3.704969766353556e-09, 3.6170153816083296e-10, 3.236886579696743e-11, 2.6738836282863183e-12, 2.0510339016163198e-13, 1.4683850435145985e-14], [0.0015421577072451112, 0.0016561023030445452, 0.000889232931646441, 0.0003183117392650812, 8.545766785174024e-05, 1.8354366726202598e-05, 3.3573876788030844e-06, 5.740810733946221e-07, 7.706223748360183e-08, 9.195121612528982e-09, 9.874516729217723e-10, 9.640099959757933e-11, 8.626977464718589e-12, 7.126457241102094e-13, 5.466432886343384e-14, 3.913552226200362e-15], [0.0003523004359690807, 0.00037833067307639433, 0.00020314209631435093, 7.271718319749038e-05, 1.9522499871204027e-05, 4.192989711233092e-06, 7.504658229604703e-07, 1.176647067132451e-07, 1.7604593703146263e-08, 2.1005927848128954e-09, 2.2557981796179966e-10, 2.2022465034884025e-11, 1.9708022776380863e-12, 1.628013776515942e-13, 1.248787124693469e-14, 8.940370683236587e-16], [7.042155742294824e-05, 7.562475801548603e-05, 4.06062023774352e-05, 1.4535483835241527e-05, 3.902364872009845e-06, 8.381393707652039e-07, 1.500110889735291e-07, 2.3013554206192655e-08, 3.157236006419974e-09, 4.198888230468006e-10, 4.509129277787574e-11, 4.402084492978217e-12, 3.939449163104305e-13, 3.254247055724057e-14, 2.4962084979752235e-15, 1.7870963620017884e-16], [1.2512541994908365e-05, 1.3437049607414609e-05, 7.214932913935185e-06, 2.582672956413536e-06, 6.93374388856766e-07, 1.489210755635491e-07, 2.665405479759462e-08, 4.089061276046826e-09, 5.488984496151698e-10, 6.693647417869329e-11, 8.011846302962064e-12, 7.821648526275779e-13, 6.999635465898727e-14, 5.782164501418015e-15, 4.4352773215981073e-16, 3.175322883615825e-17], [2.0009119595385876e-06, 2.148752289609085e-06, 1.1537580102137532e-06, 4.1300170726040954e-07, 1.1087923682220757e-07, 2.381434254076502e-08, 4.262316724803488e-09, 6.538920399913616e-10, 8.777572717471033e-11, 1.0473462909396732e-11, 1.1494858695247851e-12, 1.250779424828391e-13, 1.1193292555442717e-14, 9.246404213959652e-16, 7.092563158043507e-17, 5.077738429016947e-18], [2.9088258887862075e-07, 3.1237487780546226e-07, 1.6772757809284835e-07, 6.004012582687617e-08, 1.6119069760154253e-08, 3.4620101987382863e-09, 6.196343210509818e-10, 9.505955948390232e-11, 1.276039689780806e-11, 1.5225797372474448e-12, 1.6350777858698414e-13, 1.6313947898524175e-14, 1.6272249766320512e-15, 1.3441960715727841e-16, 1.0310814143329799e-17, 7.381762565013176e-19], [3.876313669553994e-08, 4.162720819869489e-08, 2.235144792367732e-08, 8.000972535402493e-09, 2.148034046749117e-09, 4.61348941826985e-10, 8.2572731426596e-11, 1.2667677060691689e-11, 1.700455882031075e-12, 2.0289961909480182e-13, 2.1789115658607168e-14, 2.127185144789768e-15, 1.9455275418068687e-16, 1.7912813643764037e-17, 1.3740234491895887e-18, 9.836967983017562e-20], [4.768238745197028e-09, 5.1205470946895364e-09, 2.7494431329958534e-09, 9.84196597458354e-10, 2.64228853515097e-10, 5.675035838181251e-11, 1.015724037962968e-11, 1.5582461514107446e-12, 2.09172433203314e-13, 2.4958605201443095e-14, 2.6802708543167024e-15, 2.61664237991379e-16, 2.3416473832197405e-17, 1.9769308700297807e-18, 1.6901810342889224e-19, 1.2100417012249647e-20], [5.44643579850998e-10, 5.848853737150902e-10, 3.1405024592360854e-10, 1.1241810378241454e-10, 3.018107027953376e-11, 6.482208630604189e-12, 1.1601926953303238e-12, 1.7798789187061137e-13, 2.3892348708577354e-14, 2.850852235260718e-15, 3.06149165566797e-16, 2.9888131638156766e-17, 2.674705025687262e-18, 2.2094842690936503e-19, 1.7321129794082986e-20, 1.3821485859700266e-21], [5.8063546855799035e-11, 6.23536576181959e-11, 3.348037476958655e-11, 1.1984707206492822e-11, 3.2175537418678366e-12, 6.910574887435929e-13, 1.2368621502065168e-13, 1.8974993338251497e-14, 2.5471235869797585e-15, 3.0392461871359143e-16, 3.263805372426244e-17, 3.1863240401716908e-18, 2.8514585745584433e-19, 2.355494457875872e-20, 1.8068097418544216e-21, 1.3220092756637363e-22]] |
| Legacy trial inputs | {"lambda_home": 1.599125070151857, "lambda_away": 1.0738864742977445, "rho": -0.10288407687222552, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4648 |
| Legacy p draw | 0.2691 |
| Legacy p away | 0.2661 |
| Legacy p over 1 5 | 0.7578 |
| Legacy p under 3 5 | 0.7210 |
| Legacy p btts yes | 0.5373 |
| Legacy p over 2 5 | 0.5008 |
| Legacy goal margin distribution | {"-1": 0.1606829872157942, "-10": 4.965009268794031e-08, "-11": 4.785554208388893e-09, "-12": 4.236384863117563e-10, "-13": 3.4663202570073523e-11, "-14": 2.6231084781821784e-12, "-15": 1.685035436573597e-13, "-2": 0.07459758309255707, "-3": 0.023582309482008155, "-4": 0.005854705943347878, "-5": 0.0011918388671497099, "-6": 0.0002051716866474942, "-7": 3.0560160678869446e-05, "-8": 4.008425961873246e-06, "-9": 4.6946641275187434e-07, "0": 0.26905377293351634, "1": 0.2157902828585485, "10": 2.336653353992954e-06, "11": 3.353748758678358e-07, "12": 4.4209718743359575e-08, "13": 5.386604493681704e-09, "14": 6.06997237469194e-10, "15": 5.8063546855799035e-11, "2": 0.14521333716645637, "3": 0.06835844001571648, "4": 0.02527172898223951, "5": 0.007660753211391271, "6": 0.0019637916810575492, "7": 0.0004355697193622397, "8": 8.50746111299763e-05, "9": 1.4837293669894064e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4833 |
| Legacy raw p draw | 0.2737 |
| Legacy raw p away | 0.2430 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5991 |
| Legacy lambda away | 1.0739 |
| Legacy model home team | Brentford |
| Legacy model away team | Nott'm Forest |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 70.9% |
| Market home draw odds | 1.37 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:18:01Z |
| Market reference home draw last update utc | 2026-10-31T11:18:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.5% |
| Market draw away odds | 1.75 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:18:01Z |
| Market reference draw away last update utc | 2026-10-31T11:18:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.6% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:18:01Z |
| Market reference home away last update utc | 2026-10-31T11:18:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.37 |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home away odds | 1.32 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.13, "price": 1.72, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.72, "price": 2.13, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.7, "price": 2.15, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.15, "price": 1.7, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 79.6% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-31T11:17:43Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 65.5% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.73 |
| Market reference under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:18:01Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-31T11:18:04Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 9.858934231912516, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,503.9116 |
| Elo away rating | 1,478.7386 |
| Elo rating diff | 85.1730 |
| Elo home expectancy | 0.6202 |

</details>


---

## 2026-10-31 — Chelsea vs Manchester United

The model's most likely 1X2 outcome is **Chelsea win** at **44.9%**. Expected goals are 1.74 for Chelsea and 1.38 for Manchester United (3.11 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.6%; Under 3.5 goals: 61.4%; Double Chance 1X: 70.6%; Double Chance X2: 55.1%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 79.1%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 44.9% | 2.23 |
| Draw | 25.7% | 3.90 |
| Manchester United win | 29.4% | 3.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.74 |
| Manchester United expected goals | 1.38 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 60.6% |
| Under 2.5 | 39.4% |
| Over 3.5 | 38.6% |
| Under 3.5 | 61.4% |
| Over 4.5 | 20.9% |
| Under 4.5 | 79.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.67% |
| 2 | 2-1 | 9.12% |
| 3 | 1-2 | 7.21% |
| 4 | 1-0 | 6.67% |
| 5 | 2-2 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 44.9% | 44.8% | 2.19 | -1.6% |
| Draw | 25.7% | 26.0% | 3.73 | -4.2% |
| Manchester United win | 29.4% | 29.2% | 3.32 | -2.4% |

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
| Market best home last update utc | 2026-10-31T11:18:04Z |
| Market best draw last update utc | 2026-10-31T11:18:04Z |
| Market best away last update utc | 2026-10-31T11:18:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7689 |
| Dc lambda away | 1.3441 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:17:21.264748+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6583 |
| Shot lambda away | 1.4547 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.03 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.59 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.78 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.15933438228993008, "-10": 4.0071758814618644e-07, "-11": 4.9849895427664105e-08, "-12": 5.7001513457984445e-09, "-13": 6.029401677857856e-10, "-14": 5.929541203088361e-11, "-15": 5.401924265686083e-12, "-16": 4.0803759063650875e-13, "-2": 0.08661146744668707, "-3": 0.03400191635990534, "-4": 0.010636533211406344, "-5": 0.0027516318338365498, "-6": 0.0006051919027282407, "-7": 0.00011557916348765717, "-8": 1.948589980721898e-05, "-9": 2.938656638125626e-06, "0": 0.25672719329197885, "1": 0.20374332523461677, "10": 4.068263687872473e-06, "11": 6.37822591236569e-07, "12": 9.191512650080793e-08, "13": 1.2252925029441063e-08, "14": 1.5186287112910114e-09, "15": 1.7435883667459715e-10, "16": 1.6598185063426182e-11, "2": 0.1381740334184796, "3": 0.06836272873187764, "4": 0.026951382743868376, "5": 0.008786911104531791, "6": 0.0024355888243333046, "7": 0.0005862128947732264, "8": 0.00012455502175754877, "9": 2.3673069759578754e-05} |
| Raw goal margin distribution | {"-1": 0.1621256775766645, "-10": 3.732787115331995e-07, "-11": 4.591795524298103e-08, "-12": 5.191610086877121e-09, "-13": 5.429593168039888e-10, "-14": 5.279440964404683e-11, "-15": 4.757007784665745e-12, "-16": 3.5625387490643285e-13, "-2": 0.08759499101102161, "-3": 0.03410032266651413, "-4": 0.010567058130816893, "-5": 0.002706278450200771, "-6": 0.0005890213070277173, "-7": 0.000111290366663577, "-8": 1.855913525117783e-05, "-9": 2.768131727326218e-06, "0": 0.2500534643757948, "1": 0.20641801262343967, "10": 3.7729650863064505e-06, "11": 5.849207939789302e-07, "12": 8.334538256766318e-08, "13": 1.098529497406524e-08, "14": 1.3461620018134132e-09, "15": 1.5286505193091853e-10, "16": 1.4427759662774895e-11, "2": 0.13912628391253437, "3": 0.06825796834489704, "4": 0.02665716266834728, "5": 0.008603937784714178, "6": 0.0023600474973616632, "7": 0.0005619688821562431, "8": 0.00011810747583278397, "9": 2.2200939877941738e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 29.8% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 62.4% |
| P home draw | 70.6% |
| P draw away | 55.1% |
| P home away | 74.3% |
| Raw p home draw | 70.2% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0117 |
| Totals anchor target over 2 5 | 0.6064 |
| Totals anchor reference over odds | 1.61 |
| Totals anchor reference under odds | 2.43 |
| Totals anchor reference last update utc | 2026-10-31T11:18:04Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5993 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.23, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.1, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.44, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.29, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.6, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 6.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:42Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.14, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.14, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.19 |
| Reference draw odds | 3.73 |
| Reference away odds | 3.32 |
| Market reference 1x2 last update utc | 2026-10-31T11:18:04Z |
| Market reference home last update utc | 2026-10-31T11:18:04Z |
| Market reference draw last update utc | 2026-10-31T11:18:04Z |
| Market reference away last update utc | 2026-10-31T11:18:04Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-10-31T11:17:43Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:17:43Z |
| Home probability edge | +0.1% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | 0.0042 |
| Raw ev home | -0.0098 |
| Raw edge prob draw | -0.0095 |
| Raw ev draw | -0.0673 |
| Raw edge prob away | 0.0053 |
| Raw ev away | -0.0112 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.04741696117878192, 0.042620796639927544, 0.03903671799474766, 0.019328226577806782, 0.00717747985422278, 0.0021322687562831577, 0.0005278744700279909, 0.0001120140716460129, 2.0798047337459215e-05, 3.4325748676621976e-06, 5.098706156320838e-07, 6.88505262634717e-08, 8.52247985986341e-09, 9.737839153919654e-10, 1.0331765169536083e-10, 1.0231121282908771e-11, 9.498241677602534e-13], [0.055925532477215066, 0.11147217456734122, 0.071755555511361, 0.03552828481448118, 0.013193323633934948, 0.003919441412241751, 0.0009703153283075744, 0.00020589927506535, 3.8230043838515464e-05, 6.309606163524752e-06, 9.372214454228043e-07, 1.265579693443923e-07, 1.5665642710054833e-08, 1.7899662007031474e-09, 1.8991390343131353e-10, 1.880639123550307e-11, 1.7459244602715658e-12], [0.06067197085969978, 0.09012142874225369, 0.06899201266794508, 0.03265325498895631, 0.012125689799556751, 0.0036022712753090687, 0.0008917951992437818, 0.0001892374361964624, 3.51363815117021e-05, 5.799018444411013e-06, 8.613793488289993e-07, 1.1631660986354611e-07, 1.4397943178185898e-08, 1.6451180539216447e-09, 1.7454563728793003e-10, 1.7284535170824068e-11, 1.6046402715581207e-12], [0.037174837747994335, 0.055219064810964544, 0.0410108732587812, 0.020930447041516552, 0.007429634219785138, 0.0022071781794190076, 0.0005464193987202202, 0.00011594927421622134, 2.1528710263420264e-05, 3.5531657652446442e-06, 5.277830450940706e-07, 7.126933636412088e-08, 8.821885855523223e-09, 1.0079942329919553e-09, 1.0694733752433728e-10, 1.0590554112882592e-11, 9.83192747718924e-13], [0.017083282552153557, 0.025375306082735524, 0.018846089936952495, 0.009331253115493803, 0.0035717472644223145, 0.0010142841439569456, 0.00025110094746328776, 5.3283197268553256e-05, 9.893278967526878e-06, 1.6328177444591014e-06, 2.4253681876700204e-07, 3.27510295718355e-08, 4.053999367378034e-09, 4.6321252051925695e-10, 4.9146457545127e-11, 4.866771161738463e-12, 4.518152742554148e-13], [0.006280345748596245, 0.00932875137957292, 0.00692840854512948, 0.003430458733797579, 0.0012738907190195322, 0.00039008828799433625, 9.23125144746112e-05, 1.9588559775649698e-05, 3.6370769091770014e-06, 6.002745636466394e-07, 8.916407452555888e-08, 1.2040296629507982e-08, 1.490376197548456e-09, 1.7029132282149921e-10, 1.8067765650998626e-11, 1.7891763764781768e-12, 1.6610134077909585e-13], [0.001924041949661222, 0.002857949181582902, 0.0021225819753952217, 0.001050952730091897, 0.00039026819235637116, 0.00011593995246716109, 2.958575180534913e-05, 6.001136283017629e-06, 1.1142521172444795e-06, 1.838996590321273e-07, 2.731623809536921e-08, 3.6886561232263295e-09, 4.5659051900140245e-10, 5.217032021606459e-11, 5.535226950990646e-12, 5.481307146913549e-13, 5.0886680502484615e-14], [0.0005052411678654478, 0.0007504792618774719, 0.0005573765147520082, 0.00027597349674028914, 0.00010248194293351494, 3.0445093464353574e-05, 7.537130359431152e-06, 1.6485750725280642e-06, 2.925955128536951e-07, 4.829087978867067e-08, 7.173070233434907e-09, 9.686176166174817e-10, 1.1989776371413222e-10, 1.3699593981576114e-11, 1.453515361040457e-12, 1.439356363733883e-13, 1.3362518364216624e-14], [0.00011608897510374684, 0.00017243719215527975, 0.00012806808403564398, 6.341027301423186e-05, 2.354721760314027e-05, 6.995351768634633e-06, 1.7318021457877626e-06, 3.674854925730791e-07, 7.033167392241097e-08, 1.1095767918535853e-08, 1.6481522581873514e-09, 2.2255871756377385e-10, 2.754884081518784e-11, 3.147747899043267e-12, 3.3397339586087746e-13, 3.3072009112175405e-14, 3.070298226608524e-15], [2.3709953446720257e-05, 3.521848474268148e-05, 2.6156560584518176e-05, 1.2950882027062827e-05, 4.809271790635597e-06, 1.4287271003084788e-06, 3.5370239265927363e-07, 7.50550507786467e-08, 1.3935735716694321e-08, 2.3707629645948962e-09, 3.3661778200562064e-10, 4.545527969286487e-11, 5.6265612876285e-12, 6.42894435769022e-13, 6.821055712851156e-14, 6.754610381721586e-15, 6.270761539188256e-16], [4.358257989175292e-06, 6.473704929086301e-06, 4.807982410973178e-06, 2.380573424074813e-06, 8.840189100646378e-07, 2.626222490593716e-07, 6.501599769319373e-08, 1.3796284982973777e-08, 2.561604840718061e-09, 4.227752853169928e-10, 6.473070444478765e-11, 8.355386960872724e-12, 1.0342494234961645e-12, 1.1817399039534012e-13, 1.2538160659803196e-14, 1.2416023812976571e-15, 1.1526634431313404e-16], [7.282868753026023e-07, 1.081788720664395e-06, 8.034380927642446e-07, 3.9780581708425575e-07, 1.4772401526446042e-07, 4.3885501415345156e-08, 1.0864500890553594e-08, 2.305428752953539e-09, 4.280570791908533e-10, 7.064788093394692e-11, 1.049395277121121e-11, 1.4606533603554135e-12, 1.7282829121000986e-13, 1.974746938359835e-14, 2.0951898376943048e-15, 2.0747801550285227e-16, 1.9261587068931517e-17], [1.1155870676253009e-07, 1.6570798508138458e-07, 1.2307034169095995e-07, 6.093574386891413e-08, 2.262830851348801e-08, 6.722364427461205e-09, 1.664220117198897e-09, 3.5314470016473496e-10, 6.556962070095798e-11, 1.0821815550677909e-11, 1.607459697110387e-12, 2.170637857923396e-13, 2.769535072131672e-14, 3.0249098548584232e-15, 3.2094038302977056e-16, 3.1781403559603135e-17, 2.9504825865646e-18], [1.57740187406113e-08, 2.3430541084585586e-08, 1.740172446045851e-08, 8.616105310430024e-09, 3.1995652595713086e-09, 9.505192874430818e-10, 2.353150200376378e-10, 4.9933450110745535e-11, 9.271319610699192e-12, 1.5301676243630259e-12, 2.2728929119778138e-13, 3.069207527015211e-14, 3.799137167758429e-15, 4.474477862612593e-16, 4.5379870056282756e-17, 4.493781524549655e-18, 4.171881242168478e-19], [2.07107845331573e-09, 3.0763554670363994e-09, 2.2847910334862604e-09, 1.1312672029473776e-09, 4.200927346444172e-10, 1.248001570212473e-10, 3.0896113143746914e-11, 6.556103065722192e-12, 1.2172947550827206e-12, 2.00906138688711e-13, 2.984236049226901e-14, 4.0297717927710046e-15, 4.988146178042708e-16, 5.699487233378744e-17, 6.233163107881591e-18, 5.900192108585276e-19, 5.477547283624157e-20], [2.537976082676411e-10, 3.769879689805714e-10, 2.799867377123278e-10, 1.3862966415396292e-10, 5.147971634424233e-11, 1.5293472496278254e-11, 3.786123895063286e-12, 8.034091006898141e-13, 1.491717983459898e-13, 2.4619780773562348e-14, 3.656993150536146e-15, 4.938231293132816e-16, 6.112658685863984e-17, 6.984362305868491e-18, 7.410349468972981e-19, 7.563941696182178e-20, 6.712388888654019e-21], [2.915746588114434e-11, 4.33101553563946e-11, 3.216619655221932e-11, 1.5926429450119588e-11, 5.914232537980984e-12, 1.7569862283501538e-12, 4.349677644545722e-13, 9.229942552201279e-14, 1.7137559531748727e-14, 2.8284364963336917e-15, 4.201326156781253e-16, 5.673272944750501e-17, 7.022510507199443e-18, 8.023964726261601e-19, 8.513358864323232e-20, 8.43042845404978e-21, 8.067340848000059e-22]] |
| Legacy trial inputs | {"lambda_home": 1.83815543922047, "lambda_away": 1.4853881860975635, "rho": -0.10288407687222552, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4493 |
| Legacy p draw | 0.2528 |
| Legacy p away | 0.2979 |
| Legacy p over 1 5 | 0.8540 |
| Legacy p under 3 5 | 0.5755 |
| Legacy p btts yes | 0.6619 |
| Legacy p over 2 5 | 0.6429 |
| Legacy goal margin distribution | {"-1": 0.15557214319117438, "-10": 6.518855089082561e-07, "-11": 8.627326723747503e-08, "-12": 1.0498034067241625e-08, "-13": 1.1819655467418218e-09, "-14": 1.2372868320242202e-10, "-15": 1.1977045743180336e-11, "-16": 9.498241677602534e-13, "-2": 0.08916972453310243, "-3": 0.036727352460983596, "-4": 0.012115187606515905, "-5": 0.0033150760246407054, "-6": 0.0007727183401166404, "-7": 0.00015660521203733749, "-8": 2.8044532159100174e-05, "-9": 4.495416650583475e-06, "0": 0.2528047381035357, "1": 0.19778683725030835, "10": 5.5721689780159815e-06, "11": 9.125810887499654e-07, "12": 1.3741858277729388e-07, "13": 1.9146287374810147e-08, "14": 2.4802326188485207e-09, "15": 2.971077636240357e-10, "16": 2.915746588114434e-11, "2": 0.1385901071183231, "3": 0.07063935033844129, "4": 0.02883563273712201, "5": 0.009764164839106613, "6": 0.0028164697974087834, "7": 0.0007063701824321358, "8": 0.00015653685861894648, "9": 3.105136045627962e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4507 |
| Legacy raw p draw | 0.2460 |
| Legacy raw p away | 0.3032 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8382 |
| Legacy lambda away | 1.4854 |
| Legacy model home team | Chelsea |
| Legacy model away team | Man United |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 71.4% |
| Market home draw odds | 1.36 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:18:01Z |
| Market reference home draw last update utc | 2026-10-31T11:18:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.1% |
| Market draw away odds | 1.76 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:18:01Z |
| Market reference draw away last update utc | 2026-10-31T11:18:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.5% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:18:01Z |
| Market reference home away last update utc | 2026-10-31T11:18:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.76 |
| Market reference dc home away odds | 1.32 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.2, "price": 1.68, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.2, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.08, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.08, "price": 1.76, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 82.9% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market reference over 1 5 last update utc | 2026-10-31T11:17:43Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.5% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.48 |
| Market reference under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.2% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:18:01Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.76 |
| Market reference btts yes last update utc | 2026-10-31T11:18:04Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 9.967292560077574, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,487.8075 |
| Elo away rating | 1,504.9896 |
| Elo rating diff | 42.8180 |
| Elo home expectancy | 0.5613 |

</details>


---

## 2026-10-31 — Coventry City vs Sunderland

The model's most likely 1X2 outcome is **Sunderland win** at **39.6%**. Expected goals are 1.03 for Coventry City and 1.17 for Sunderland (2.20 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.1%; Double Chance 1X: 60.4%; Double Chance X2: 69.1%; Double Chance 12 (either team wins): 70.5%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 55.5%; BTTS No (at least one team does not score): 44.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 30.9% | 3.24 |
| Draw | 29.5% | 3.39 |
| Sunderland win | 39.6% | 2.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.03 |
| Sunderland expected goals | 1.17 |
| Expected total goals | 2.20 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.08% |
| 2 | 0-1 | 8.79% |
| 3 | 1-2 | 8.65% |
| 4 | 0-0 | 8.34% |
| 5 | 1-0 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 30.9% | 30.8% | 3.17 | -2.2% |
| Draw | 29.5% | 28.9% | 3.37 | -0.5% |
| Sunderland win | 39.6% | 40.4% | 2.43 | -3.8% |
| Over 2.5 | 49.3% | 49.3% | 1.98 | -2.3% |
| Under 2.5 | 50.7% | 50.7% | 1.93 | -2.2% |

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
| Market best home last update utc | 2026-10-31T11:18:04Z |
| Market best draw last update utc | 2026-10-31T11:18:04Z |
| Market best away last update utc | 2026-10-31T11:18:04Z |
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
| Dc lambda home | 0.8796 |
| Dc lambda away | 1.1504 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:17:21.264748+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.3945 |
| Shot lambda away | 1.2078 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 55.5% |
| P btts no | 44.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.98 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.64 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.20420524416610694, "-10": 7.274562855171661e-07, "-11": 9.252180860214927e-08, "-12": 1.0805393261231186e-08, "-13": 1.1593648430022112e-09, "-14": 1.0415997546296157e-10, "-2": 0.11998794783643585, "-3": 0.04987867396802917, "-4": 0.01630544129208116, "-5": 0.004374000877452071, "-6": 0.0009927053782194132, "-7": 0.00019500111407473058, "-8": 3.373870693203646e-05, "-9": 5.2131488966123e-06, "0": 0.29539819499673614, "1": 0.1725717224227648, "10": 2.072173270572423e-07, "11": 2.3340197766865622e-08, "12": 2.4140276868458404e-09, "13": 2.2938396052777724e-10, "14": 1.8250931732239778e-11, "2": 0.09032891259607871, "3": 0.03325410830726878, "4": 0.009627293590640304, "5": 0.002287134874486117, "6": 0.0004597000344949622, "7": 7.997099607670005e-05, "8": 1.2253639460628921e-05, "9": 1.6767875652744483e-06} |
| Raw goal margin distribution | {"-1": 0.21438637456056334, "-10": 1.6014765293288685e-07, "-11": 1.6844246246320487e-08, "-12": 1.6205640443798678e-09, "-13": 1.3318421363511423e-10, "-2": 0.1107199742423643, "-3": 0.039350945237764307, "-4": 0.010856029900756086, "-5": 0.00243963979051132, "-6": 0.0004617621918675551, "-7": 7.542337624182587e-05, "-8": 1.0828987371552876e-05, "-9": 1.3865007430136635e-06, "0": 0.310555610550751, "1": 0.18870516386489355, "10": 4.7526199954368505e-08, "11": 4.4269574291294856e-09, "12": 3.771909066273728e-10, "13": 2.7452949887576147e-11, "2": 0.08683773328942954, "3": 0.027332472680424495, "4": 0.006677840410346832, "5": 0.0013290213705710418, "6": 0.00022277470565007133, "7": 3.22251337141838e-05, "8": 4.097489575962892e-06, "9": 4.6461301149689694e-07} |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 31.1% |
| Unadjusted away-win probability | 37.8% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.9% |
| Raw p btts yes | 45.4% |
| P home draw | 60.4% |
| P draw away | 69.1% |
| P home away | 70.5% |
| Raw p home draw | 62.2% |
| Raw p draw away | 68.9% |
| Raw p home away | 68.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.2142 |
| Totals anchor target over 2 5 | 0.4934 |
| Totals anchor reference over odds | 1.98 |
| Totals anchor reference under odds | 1.93 |
| Totals anchor reference last update utc | 2026-10-31T11:18:04Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3829 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:16:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.2, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:16:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.24, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:16:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.56, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:16:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:16:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.3, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.72, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:16:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:16:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:16:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:16:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:16:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.43, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.99, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.93, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.43, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.17 |
| Reference draw odds | 3.37 |
| Reference away odds | 2.43 |
| Market reference 1x2 last update utc | 2026-10-31T11:18:04Z |
| Market reference home last update utc | 2026-10-31T11:18:04Z |
| Market reference draw last update utc | 2026-10-31T11:18:04Z |
| Market reference away last update utc | 2026-10-31T11:18:04Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.98 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market best over 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market best under 2 5 last update utc | 2026-10-31T11:18:04Z |
| Home probability edge | +0.1% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0036 |
| Raw ev home | -0.0137 |
| Raw edge prob draw | 0.0217 |
| Raw ev draw | 0.0466 |
| Raw edge prob away | -0.0253 |
| Raw ev away | -0.0807 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.12859699495271598, 0.1301957368018483, 0.08453273625228984, 0.0330985701308719, 0.009719743438553688, 0.002283443958763395, 0.0004470382325226025, 7.50157037024115e-05, 1.1014575417714477e-05, 1.437575993584875e-06, 1.6886372765735875e-07, 1.8032222072297462e-08, 1.7651172591116399e-09, 1.5949084883487193e-10], [0.10554871912784815, 0.13893644591826526, 0.07839930133457183, 0.030697039850799735, 0.00901450879881173, 0.0021177642998495712, 0.0004146025155865522, 6.957279534685599e-05, 1.0215391758626214e-05, 1.3332699083114582e-06, 1.5661149580651044e-07, 1.6723859591610836e-08, 1.6370457886863732e-09, 1.4791868419582905e-10], [0.05567346204966078, 0.06539639208813199, 0.034309876362784555, 0.014234878604660202, 0.004180221905936744, 0.000982052923283952, 0.00019226011717242346, 3.2262403826653077e-05, 4.737097201875704e-06, 6.182659756219327e-07, 7.262412407631046e-08, 7.755213930888528e-09, 7.59133394799096e-10, 6.859308008598881e-11], [0.017211322386566235, 0.020217143782851693, 0.011873954062226, 0.00415307208653886, 0.0012923059608954573, 0.00030359939621202135, 5.943677179231109e-05, 9.973847732530183e-06, 1.464462674249667e-06, 1.9113550038583993e-07, 2.245158045685039e-08, 2.3975064999954555e-09, 2.34684338125786e-10, 2.120539250450122e-11], [0.0039906304645211275, 0.004687562528514572, 0.00275310413405701, 0.0010779706690993446, 0.00028277584740197485, 7.039278983464704e-05, 1.3781055685315504e-05, 2.3125440170126663e-06, 3.3955144356463024e-07, 4.4316824329928554e-08, 5.205640736686548e-09, 5.558877036221779e-10, 5.441409138915002e-11, 4.916698638254566e-12], [0.0007402165224349743, 0.0008694894865365406, 0.0005106694759464723, 0.0001999512876628557, 5.871779985077581e-05, 1.2322395097636914e-05, 2.55622894817225e-06, 4.289505895044919e-07, 6.29829273789566e-08, 8.220266417175723e-09, 9.655870964284708e-10, 1.031108408803643e-10, 1.0093194510900138e-11, 9.11991626442489e-13], [0.00011441811533228422, 0.0001344003346797571, 7.893614533665518e-05, 3.0907239705200066e-05, 9.07623619813787e-06, 2.1322658201800733e-06, 3.7289405081337416e-07, 6.630454270370295e-08, 9.735513367230189e-09, 1.270638201763645e-09, 1.4925451190833636e-10, 1.5938239320907245e-11, 1.5601439019767344e-12, 1.4097005394194078e-13], [1.5159469911155376e-05, 1.7806951492864755e-05, 1.0458397402006241e-05, 4.094957944265707e-06, 1.20252749446737e-06, 2.8250788303698194e-07, 5.530760858915415e-08, 8.290528190685188e-09, 1.2898763585781102e-09, 1.6834922976716368e-10, 1.977500919157498e-11, 2.111687111087318e-12, 2.0670638098174906e-13, 1.867738587461086e-14], [1.7574431846290366e-06, 2.064366743927255e-06, 1.2124460382861148e-06, 4.747300514245888e-07, 1.3940947552035087e-07, 3.2751247672715025e-08, 6.411832362397642e-09, 1.075944028261242e-09, 1.411221070619998e-10, 1.9516791037273172e-11, 2.2925244308269665e-12, 2.4480869998748793e-13, 2.3963550348708804e-14, 2.165276537002592e-15], [1.8110316904514194e-07, 2.1273140586649606e-07, 1.2494163211096446e-07, 4.892056682452809e-08, 1.4366039273688361e-08, 3.374990893354553e-09, 6.60734395497127e-10, 1.1087520492131151e-10, 1.6279835371604653e-11, 1.898029067120051e-12, 2.3624288009277044e-13, 2.52273483235897e-14, 2.4694254401402165e-15, 2.2313008246296917e-16], [1.6796288103393046e-08, 1.9729627043041257e-08, 1.1587625219969588e-08, 4.537104120807802e-09, 1.332368372225355e-09, 3.1301119516567377e-10, 6.127935433214158e-11, 1.0283044163169192e-11, 1.5098620671244154e-12, 1.9706083793585592e-13, 2.0677388368502737e-14, 2.3396929648538835e-15, 2.290251537901283e-16, 2.0694045108883256e-17], [1.4161455621708123e-09, 1.6634641897243898e-09, 9.769875302414916e-10, 3.825368930466791e-10, 1.1233598434897792e-10, 2.639091519596555e-11, 5.166646651686355e-12, 8.669943780219377e-13, 1.2730101155006695e-13, 1.6614791875601924e-14, 1.9516433933825942e-15, 1.861671886089878e-16, 1.930979947288824e-17, 1.744777177189972e-18], [1.0944953358157225e-10, 1.2856402940379526e-10, 7.550836040896035e-11, 2.9565099549175254e-11, 8.682102617032687e-12, 2.0396726411100778e-12, 3.993142239848757e-13, 6.700732807924496e-14, 9.838703527947503e-15, 1.2841061469358934e-15, 1.508365134413472e-16, 1.610717437497552e-17, 1.4084241849674227e-18, 1.3484846003717582e-19], [7.808324047093746e-12, 9.171986115744774e-12, 5.386900492348694e-12, 2.1092266929807537e-12, 6.193966152755352e-13, 1.455138675388611e-13, 2.848778569863773e-14, 4.78042175285031e-15, 7.019105777389369e-16, 9.161041237939644e-17, 1.0760944670504747e-17, 1.1491144172772345e-18, 1.1248318052527377e-19, 9.079033011047032e-21]] |
| Legacy trial inputs | {"lambda_home": 0.9274430807561628, "lambda_away": 1.1746420948242513, "rho": -0.10288407687222552, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T11:18:04Z", "over": 1.98, "under": 1.93, "bookmaker": "pinnacle", "event_id": "d20fbb0cd5ad9369b8ed6f2c4a198619", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Coventry City", "away_team": "Sunderland"}} |
| Legacy p home | 0.2912 |
| Legacy p draw | 0.3063 |
| Legacy p away | 0.4025 |
| Legacy p over 1 5 | 0.6357 |
| Legacy p under 3 5 | 0.8376 |
| Legacy p btts yes | 0.4277 |
| Legacy p over 2 5 | 0.3565 |
| Legacy goal margin distribution | {"-1": 0.22419523933493307, "-10": 1.8636792603627317e-07, "-11": 1.9737860941069823e-08, "-12": 1.913035943307469e-09, "-13": 1.5949084883487193e-10, "-2": 0.11972781731769375, "-3": 0.04315694544236479, "-4": 0.012040089626408582, "-5": 0.0027318186394093874, "-6": 0.0005215445709021189, "-7": 8.587237913898469e-05, "-8": 1.2422922282685255e-05, "-9": 1.6021823043590383e-06, "0": 0.30629186889042426, "1": 0.18395794241300792, "10": 1.8537369880219378e-08, "11": 1.5500964920669562e-09, "12": 1.1862151969731703e-10, "13": 7.808324047093746e-12, "2": 0.0788530265225477, "3": 0.022441697580620652, "4": 0.004943293900961282, "5": 0.000885564668852987, "6": 0.0001334877925936417, "7": 1.735342979545918e-05, "8": 1.9821535802250334e-06, "9": 2.0183996811458916e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2749 |
| Legacy raw p draw | 0.3237 |
| Legacy raw p away | 0.4014 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9274 |
| Legacy lambda away | 1.1746 |
| Legacy model home team | Coventry |
| Legacy model away team | Sunderland |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 59.9% |
| Market home draw odds | 1.62 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:18:01Z |
| Market reference home draw last update utc | 2026-10-31T11:18:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.3% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:18:01Z |
| Market reference draw away last update utc | 2026-10-31T11:18:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.8% |
| Market home away odds | 1.37 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:18:01Z |
| Market reference home away last update utc | 2026-10-31T11:18:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.62 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.37 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.09, "price": 1.75, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.09, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.19, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.19, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 75.5% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.72 |
| Market reference over 1 5 last update utc | 2026-10-31T11:18:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.7% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.38 |
| Market reference under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.6% |
| Market btts yes odds | 1.74 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:18:01Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.24 |
| Market reference btts yes last update utc | 2026-10-31T11:18:04Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 9.383813207623444, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,364.9791 |
| Elo away rating | 1,407.0794 |
| Elo rating diff | 17.8997 |
| Elo home expectancy | 0.5257 |

</details>


---

## 2026-10-31 — Hull City vs Ipswich Town

The model's most likely 1X2 outcome is **Hull City win** at **40.3%**. Expected goals are 1.75 for Hull City and 0.91 for Ipswich Town (2.66 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 50.7%; Under 3.5 goals: 71.1%; Double Chance 1X: 68.3%; Double Chance X2: 59.7%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 40.3% | 2.48 |
| Draw | 28.0% | 3.57 |
| Ipswich Town win | 31.7% | 3.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.75 |
| Ipswich Town expected goals | 0.91 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 76.1% |
| Under 1.5 | 23.9% |
| Over 2.5 | 50.7% |
| Under 2.5 | 49.3% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.34% |
| 2 | 1-2 | 8.82% |
| 3 | 0-1 | 8.62% |
| 4 | 0-0 | 7.99% |
| 5 | 1-0 | 7.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 40.3% | 33.4% | 2.92 | +17.8% |
| Draw | 28.0% | 29.2% | 3.33 | -6.8% |
| Ipswich Town win | 31.7% | 37.3% | 2.62 | -17.0% |
| Over 2.5 | 50.7% | 50.7% | 1.93 | -2.2% |
| Under 2.5 | 49.3% | 49.3% | 1.98 | -2.3% |

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
| Market best home last update utc | 2026-10-31T11:18:04Z |
| Market best draw last update utc | 2026-10-31T11:18:04Z |
| Market best away last update utc | 2026-10-31T11:18:04Z |
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
| Dc lambda home | 1.8157 |
| Dc lambda away | 0.7783 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:17:21.264748+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6095 |
| Shot lambda away | 1.2179 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.52 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.18 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.16 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.20442793027184725, "-10": 2.1523742944471483e-08, "-11": 1.8456094560266694e-09, "-12": 1.453570177720448e-10, "-13": 1.0583966136979375e-11, "-14": 7.163744890352868e-13, "-15": 4.5080839436047866e-14, "-16": 2.4258090542817844e-15, "-2": 0.08293481818662661, "-3": 0.023269084497086125, "-4": 0.005131868292345682, "-5": 0.0009285238255949379, "-6": 0.00014211475830719678, "-7": 1.8824203099344303e-05, "-8": 2.1960300621876616e-06, "-9": 2.2878023984430495e-07, "0": 0.2798223821016221, "1": 0.16636918040075468, "10": 6.21105707981241e-06, "11": 1.026243765113397e-06, "12": 1.5574342828426909e-07, "13": 2.1851696958112337e-08, "14": 2.8499670587841164e-09, "15": 3.455848728916419e-10, "16": 3.583293185756979e-11, "2": 0.1259159107514455, "3": 0.06807474324984138, "4": 0.028929785820539924, "5": 0.010086158063087521, "6": 0.0029746433299384476, "7": 0.0007592334259940979, "8": 0.00017067110581629798, "9": 3.426125233861155e-05} |
| Raw goal margin distribution | {"-1": 0.12100706787466871, "-10": 8.65219932496161e-09, "-11": 7.07431978425884e-10, "-12": 5.311768764389046e-11, "-13": 3.686794651294718e-12, "-14": 2.3785284547060047e-13, "-15": 1.4277064792164884e-14, "-16": 7.384785201824984e-16, "-2": 0.04762474115768939, "-3": 0.01285894198167749, "-4": 0.0027194776848945583, "-5": 0.00047087247561623823, "-6": 6.888157322505899e-05, "-7": 8.713139291709109e-06, "-8": 9.701579865129698e-07, "-9": 9.642526871293236e-08, "0": 0.25081748372573137, "1": 0.24097714446067445, "10": 6.105996175400714e-06, "11": 9.620058228768132e-07, "12": 1.3918587857488332e-07, "13": 1.8615211048055285e-08, "14": 2.314143937317819e-09, "15": 2.6766029262930295e-10, "16": 2.6677546580720347e-11, "2": 0.17683109273711636, "3": 0.09200135854355172, "4": 0.037491904688103005, "5": 0.012508876677812641, "6": 0.003525989907312273, "7": 0.0008594402029761118, "8": 0.0001843938672693496, "9": 3.5314890875954835e-05} |
| Unadjusted home-win probability | 56.4% |
| Unadjusted draw probability | 25.1% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 50.3% |
| P home draw | 68.3% |
| P draw away | 59.7% |
| P home away | 72.0% |
| Raw p home draw | 81.5% |
| Raw p draw away | 43.6% |
| Raw p home away | 74.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0500 |
| Totals anchor target over 2 5 | 0.5066 |
| Totals anchor reference over odds | 1.93 |
| Totals anchor reference under odds | 1.98 |
| Totals anchor reference last update utc | 2026-10-31T11:18:04Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4778 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:06Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:06Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.07, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:06Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.93, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:06Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.14, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:06Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:06Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:06Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 4.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:06Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:06Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:06Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.16, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.38, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 5.16, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.92 |
| Reference draw odds | 3.33 |
| Reference away odds | 2.62 |
| Market reference 1x2 last update utc | 2026-10-31T11:18:04Z |
| Market reference home last update utc | 2026-10-31T11:18:04Z |
| Market reference draw last update utc | 2026-10-31T11:18:04Z |
| Market reference away last update utc | 2026-10-31T11:18:04Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market best over 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market best under 2 5 last update utc | 2026-10-31T11:18:04Z |
| Home probability edge | +6.9% |
| Draw probability edge | -1.2% |
| Away probability edge | -5.7% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.2301 |
| Raw ev home | 0.6481 |
| Raw edge prob draw | -0.0414 |
| Raw ev draw | -0.1648 |
| Raw edge prob away | -0.1887 |
| Raw ev away | -0.5159 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08771664316965856, 0.08001553574090553, 0.04271569787402143, 0.012406501301590395, 0.002702541727171012, 0.000470961577937478, 6.839388937192025e-05, 8.513386209739572e-06, 9.272469696349498e-07, 8.977098434709273e-08, 7.822022508670771e-09, 6.195972053588862e-10, 4.498951156912889e-11, 3.015442142171993e-12, 1.8767483312605874e-13, 1.090179103860677e-14, 5.936916554177343e-16], [0.08986447921180611, 0.12986582010377323, 0.07635483613238603, 0.022176773902956394, 0.0048308266278982185, 0.0008418496219848986, 0.00012225491974521892, 1.5217782719914685e-05, 1.65746538028088e-06, 1.6046674034170353e-07, 1.3981961587864471e-08, 1.1075376369312308e-09, 8.041930612179228e-11, 5.390139974097479e-12, 3.3547107603802407e-13, 1.9487085772478525e-14, 1.061231147300425e-15], [0.08822605015959517, 0.0768740763197192, 0.04584976583246548, 0.019820628265270996, 0.0043175810523449825, 0.0007524082847053407, 0.00010926608750551807, 1.3600987034136815e-05, 1.481369892161088e-06, 1.4341813751497328e-07, 1.2496464285791155e-08, 9.898685844690944e-10, 7.187525015884233e-11, 4.81747080039091e-12, 2.998293404169901e-13, 1.741670293253328e-14, 9.48481874154143e-16], [0.05256838381688958, 0.04580445279181932, 0.019955415624590005, 0.007934630912261362, 0.0025725764387007047, 0.0004483130257542901, 6.51048257943034e-05, 8.103977287951655e-06, 8.826556433733666e-07, 8.545389582274778e-08, 7.445861281800543e-09, 5.898007627285045e-10, 4.282596501203624e-11, 2.8704294661667487e-12, 1.7864954645587754e-13, 1.0377523678391508e-14, 5.651410112285881e-16], [0.023491658405773677, 0.020469005898999942, 0.008917637811179806, 0.002590070878340965, 0.0007723939522051813, 0.00020034126399174016, 2.909391952118174e-05, 3.621489807254507e-06, 3.944394588253179e-07, 3.818747285636714e-08, 3.327392190296636e-09, 2.6356903217236113e-10, 1.913798499997137e-11, 1.2827320073589886e-12, 7.983456623483825e-14, 4.637487852009557e-15, 2.525491297796005e-16], [0.008398325755280336, 0.007317720037351905, 0.0031880774874321434, 0.0009259567200341339, 0.0002017036562214252, 4.8120593302958324e-05, 1.0401147906047413e-05, 1.2946915281756192e-06, 1.4101307829068978e-07, 1.3652115626705778e-08, 1.1895509055596862e-09, 9.422657834337563e-11, 6.841876786780004e-12, 4.585798528331123e-13, 2.8541054113356646e-14, 1.6579133322387868e-15, 9.02869360887849e-17], [0.0025020184567042573, 0.0021800857847098214, 0.0009497879633858399, 0.0002758598405376342, 6.009129502191959e-05, 1.0471879430869914e-05, 2.081903474344735e-06, 3.857128424909388e-07, 4.2010435746453284e-08, 4.067220808814444e-09, 3.5438948281189287e-10, 2.8071861582528713e-11, 2.038323172717724e-12, 1.3661952263994669e-13, 8.502914300569377e-15, 4.939234173274859e-16, 2.689816840593331e-17], [0.0006389126874062083, 0.0005567043135724021, 0.00024253681203945042, 7.044326615300465e-05, 1.534484715302485e-05, 2.6740876396987083e-06, 3.883358277363601e-07, 6.617540795646611e-08, 1.0727738770251987e-08, 1.0386010423988041e-09, 9.049650942627175e-11, 7.168399767847322e-12, 5.205039685434123e-13, 3.4887011376015295e-14, 2.1712948647539114e-15, 1.261277418205966e-16, 6.868686766274714e-18], [0.00014275803737796535, 0.00012438947726657913, 5.419219239364879e-05, 1.573977574826742e-05, 3.42863791345866e-06, 5.974955745046203e-07, 8.67693844619867e-08, 1.0800691229727744e-08, 1.6104556549473417e-09, 2.3206401962917337e-10, 2.0220453169741774e-11, 1.6017003608944175e-12, 1.1630090693355942e-13, 7.79512032268699e-15, 4.851520396621117e-16, 2.818186152214472e-17, 1.5347327756131415e-18], [2.835352781578497e-05, 2.4705302541608595e-05, 1.076324571739213e-05, 3.1261158929437684e-06, 6.809702783467236e-07, 1.1867007772509504e-07, 1.7233482619180457e-08, 2.1451520687483054e-09, 2.336421379400638e-10, 3.0966767200472726e-11, 4.016034346830706e-12, 3.181176805823915e-13, 2.3098811529687427e-14, 1.548208177670075e-15, 9.635724967992375e-17, 5.597269402444615e-18, 3.048170824030999e-19], [5.068228023651133e-06, 4.4161032619176296e-06, 1.923943430417165e-06, 5.587970666908755e-07, 1.217242760905739e-07, 2.1212422574109006e-08, 3.080506246810296e-09, 3.834485747403411e-10, 4.176381996297314e-11, 4.0433448163727994e-12, 4.823119102975194e-13, 5.686392726936014e-14, 4.1289410146212034e-15, 2.767441188798005e-16, 1.7223977075539034e-17, 1.0005188005424026e-18, 5.448642896080469e-20], [8.235927294516034e-07, 7.17621725394024e-07, 3.126429619530522e-07, 9.08051491009961e-08, 1.978033117652345e-08, 3.4470424228280157e-09, 5.005857147831131e-10, 6.231082279664671e-11, 6.786667512810798e-12, 6.570480605628902e-13, 5.725062230720485e-14, 6.208329144384119e-15, 6.70957538632367e-16, 4.497122922731049e-17, 2.7989155628865777e-18, 1.62585425509869e-19, 8.854105722254483e-21], [1.2268184575954035e-07, 1.06896472832035e-07, 4.657109547539307e-08, 1.3526276881533706e-08, 2.946465469755553e-09, 5.134692326941299e-10, 7.456692762616225e-11, 9.281780275766105e-12, 1.010937648250407e-12, 9.787345849477702e-14, 8.528016050125819e-15, 6.755202898043827e-16, 6.71497436357172e-17, 6.698885517548808e-18, 4.1692467053305375e-19, 2.4218620905544413e-20, 1.3189019204668908e-21], [1.6868870040047425e-08, 1.4698366304965957e-08, 6.403569756660218e-09, 1.8598758881368248e-09, 4.051417940370246e-10, 7.060250603709696e-11, 1.0253023205053431e-11, 1.2762535829389253e-12, 1.390048845560439e-13, 1.345769328376752e-14, 1.172610287678394e-15, 9.288467994246129e-17, 6.7444403343389984e-18, 6.188562362775572e-19, 5.73275372584191e-20, 3.3300833230497284e-21, 1.813502637996853e-22], [2.1538080708224507e-09, 1.8766793448751615e-09, 8.176042729137392e-10, 2.374679328898253e-10, 5.172828196274238e-11, 9.014489231465012e-12, 1.3091003770227556e-12, 1.6295135719370327e-13, 1.774806738861501e-14, 1.7182708942815525e-15, 1.4971823812355724e-16, 1.1859464969549962e-17, 8.611264412372559e-19, 5.771738500995898e-20, 4.917742874097455e-21, 4.251832114817567e-22, 2.3154702175679612e-23], [2.566638971825154e-10, 2.236391630910996e-10, 9.743184728571673e-11, 2.82984570153015e-11, 6.1643294140148794e-12, 1.0742340362640218e-12, 1.5600220331677767e-13, 1.941850388393485e-14, 2.114992605483347e-15, 2.047620259743861e-16, 1.7841546327486022e-17, 1.4132626480603148e-18, 1.0261827475206084e-19, 6.878035778825417e-21, 4.280746093494423e-22, 3.404202740746547e-23, 2.7592876909598625e-24], [2.867436736646013e-11, 2.4984859929255118e-11, 1.0885039200806637e-11, 3.161490031391972e-12, 6.886759225807464e-13, 1.2001291078147086e-13, 1.7428491256413527e-14, 2.1694259309053794e-15, 2.3628595845659727e-16, 2.2875915233668388e-17, 1.9932489898111903e-18, 1.578890245205018e-19, 1.14644643872936e-20, 7.684108550001872e-22, 4.782428983384115e-23, 2.77805183387644e-24, 2.0711310000646727e-25]] |
| Legacy trial inputs | {"lambda_home": 1.7875123182483, "lambda_away": 0.8713308164726744, "rho": -0.10288407687222552, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T11:18:04Z", "over": 1.93, "under": 1.98, "bookmaker": "pinnacle", "event_id": "1ec76c009147b63859f68c6b5a1dd77b", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Hull City", "away_team": "Ipswich Town"}} |
| Legacy p home | 0.4567 |
| Legacy p draw | 0.2722 |
| Legacy p away | 0.2711 |
| Legacy p over 1 5 | 0.7424 |
| Legacy p under 3 5 | 0.7366 |
| Legacy p btts yes | 0.5080 |
| Legacy p over 2 5 | 0.4816 |
| Legacy goal margin distribution | {"-1": 0.17897471566587989, "-10": 9.004387344604747e-09, "-11": 7.050173596023135e-10, "-12": 5.069011095645153e-11, "-13": 3.368895062153779e-12, "-14": 2.0811040077269141e-13, "-15": 1.1963022185907194e-14, "-16": 5.936916554177343e-16, "-2": 0.06968879753570599, "-3": 0.018058607702216203, "-4": 0.003662169867199581, "-5": 0.000607739545984227, "-6": 8.518191957228839e-05, "-7": 1.0321986138545488e-05, "-8": 1.1008195802206027e-06, "-9": 1.047869522582919e-07, "0": 0.2721895242844601, "1": 0.18949661694437095, "10": 5.8343335403531775e-06, "11": 9.371365243155131e-07, "12": 1.3822680347035794e-07, "13": 1.8846142722239697e-08, "14": 2.388332273114357e-09, "15": 2.816487571117705e-10, "16": 2.867436736646013e-11, "2": 0.14393695182225608, "3": 0.07651728701040375, "4": 0.031833160124497224, "5": 0.010837390820487033, "6": 0.003116166325742901, "7": 0.0007746445116753921, "8": 0.00016948110689582306, "9": 3.309621463099208e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5792 |
| Legacy raw p draw | 0.2521 |
| Legacy raw p away | 0.1687 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7875 |
| Legacy lambda away | 0.8713 |
| Legacy model home team | Hull |
| Legacy model away team | Ipswich |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 62.9% |
| Market home draw odds | 1.54 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:18:01Z |
| Market reference home draw last update utc | 2026-10-31T11:18:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 66.4% |
| Market draw away odds | 1.46 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:18:01Z |
| Market reference draw away last update utc | 2026-10-31T11:18:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.7% |
| Market home away odds | 1.37 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:18:01Z |
| Market reference home away last update utc | 2026-10-31T11:18:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.54 |
| Market reference dc draw away odds | 1.46 |
| Market reference dc home away odds | 1.37 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.39, "price": 1.56, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.56, "price": 2.39, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.89, "price": 1.95, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.95, "price": 1.89, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.55, "price": 2.42, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.42, "price": 1.55, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 76.8% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 3.94 |
| Market reference over 1 5 last update utc | 2026-10-31T11:18:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.0% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.20 |
| Market reference under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.2% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:18:01Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.32 |
| Market reference btts yes last update utc | 2026-10-31T11:18:05Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 9.82900394938274, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,403.0690 |
| Elo away rating | 1,376.0928 |
| Elo rating diff | 86.9763 |
| Elo home expectancy | 0.6226 |

</details>


---

## 2026-10-31 — Manchester City vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Manchester City win** at **57.2%**. Expected goals are 2.03 for Manchester City and 1.07 for Brighton and Hove Albion (3.09 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 64.5%; Under 3.5 goals: 57.3%; Double Chance 1X: 79.6%; Double Chance X2: 42.8%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 62.0%; BTTS No (at least one team does not score): 38.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 57.2% | 1.75 |
| Draw | 22.4% | 4.46 |
| Brighton and Hove Albion win | 20.4% | 4.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 2.03 |
| Brighton and Hove Albion expected goals | 1.07 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 64.5% |
| Under 2.5 | 35.5% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.10% |
| 2 | 2-1 | 9.26% |
| 3 | 2-0 | 8.02% |
| 4 | 3-1 | 6.77% |
| 5 | 1-0 | 6.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 57.2% | 56.5% | 1.74 | -0.5% |
| Draw | 22.4% | 22.4% | 4.27 | -4.2% |
| Brighton and Hove Albion win | 20.4% | 21.2% | 4.50 | -8.2% |

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
| Market best home last update utc | 2026-10-31T11:18:04Z |
| Market best draw last update utc | 2026-10-31T11:18:04Z |
| Market best away last update utc | 2026-10-31T11:18:04Z |
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
| Dc lambda away | 1.0540 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:17:21.264748+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7466 |
| Shot lambda away | 1.0955 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.0% |
| P btts no | 38.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.64 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.74 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.12 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.12402234806481066, "-10": 5.678531896936204e-08, "-11": 5.851410781705676e-09, "-12": 5.542702372475824e-10, "-13": 4.857230531989395e-11, "-14": 3.959513310598486e-12, "-15": 3.015588593444886e-13, "-16": 2.137420015966513e-14, "-17": 1.2637608891791098e-15, "-2": 0.05602693530600798, "-3": 0.018141171857168577, "-4": 0.0046879609594672675, "-5": 0.0010027801646290537, "-6": 0.00018247423959328932, "-7": 2.8844081951661583e-05, "-8": 4.026145090498568e-06, "-9": 5.028041300022137e-07, "0": 0.22429038493756576, "1": 0.20780732174596026, "10": 2.972269488798264e-05, "11": 5.816403239395436e-06, "12": 1.0463025534381122e-06, "13": 1.741270526202564e-07, "14": 2.695635370238595e-08, "15": 3.8988204666598656e-09, "16": 5.247987883185767e-10, "17": 5.892636731929173e-11, "2": 0.17334628165619156, "3": 0.10659204813436897, "4": 0.05231006530096817, "5": 0.021249504965357012, "6": 0.007343218500911309, "7": 0.0022043645368844096, "8": 0.0005843296484681783, "9": 0.00013858273998666019} |
| Raw goal margin distribution | {"-1": 0.1159421938839054, "-10": 2.893791949360084e-08, "-11": 2.7609239352732176e-09, "-12": 2.420496398198222e-10, "-13": 1.9625592863751087e-11, "-14": 1.479855615392962e-12, "-15": 1.0424907316154789e-13, "-16": 6.848072183381285e-15, "-17": 3.8116380452529947e-16, "-2": 0.05024024265941065, "-3": 0.015350124098729106, "-4": 0.0037168570409040385, "-5": 0.0007418693935332408, "-6": 0.00012563199018111575, "-7": 1.8448486754635276e-05, "-8": 2.389239481274152e-06, "-9": 2.7659547228089467e-07, "0": 0.22595621550908973, "1": 0.22686275632383487, "10": 1.7655717333232086e-05, "11": 3.1990005238641956e-06, "12": 5.326060758339373e-07, "13": 8.200989712773428e-08, "14": 1.1743691475011241e-08, "15": 1.5710836071510498e-09, "16": 1.9599149714354323e-10, "17": 2.071678507045043e-11, "2": 0.18119046560012908, "3": 0.10513257697576056, "4": 0.04834405581691531, "5": 0.01832468364634963, "6": 0.005893198606720717, "7": 0.0016434382584784239, "8": 0.0004041979747802326, "9": 8.88630721461717e-05} |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 57.7% |
| P home draw | 79.6% |
| P draw away | 42.8% |
| P home away | 77.6% |
| Raw p home draw | 81.4% |
| Raw p draw away | 41.2% |
| Raw p home away | 77.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0830 |
| Totals anchor target over 2 5 | 0.6446 |
| Totals anchor reference over odds | 1.51 |
| Totals anchor reference under odds | 2.64 |
| Totals anchor reference last update utc | 2026-10-31T11:18:04Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5967 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.55, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.7, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.09, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.44, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.85, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:00Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.96, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.74 |
| Reference draw odds | 4.27 |
| Reference away odds | 4.50 |
| Market reference 1x2 last update utc | 2026-10-31T11:18:04Z |
| Market reference home last update utc | 2026-10-31T11:18:04Z |
| Market reference draw last update utc | 2026-10-31T11:18:04Z |
| Market reference away last update utc | 2026-10-31T11:18:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.64 |
| Market reference over 2 5 last update utc | 2026-10-31T11:17:45Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:17:45Z |
| Home probability edge | +0.7% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.0233 |
| Raw ev home | 0.0230 |
| Raw edge prob draw | 0.0024 |
| Raw ev draw | -0.0352 |
| Raw edge prob away | -0.0257 |
| Raw ev away | -0.1624 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.05182674159122435, 0.04007469920368296, 0.029183793566575723, 0.011274109521597688, 0.0032665101920785057, 0.0007571392713198099, 0.00014624676960672074, 2.421307801681133e-05, 3.5076945976083493e-06, 4.516905701051538e-07, 5.2348324205569514e-08, 5.515334508137574e-09, 5.326628043672642e-10, 4.748656750839573e-11, 3.931013200918331e-12, 3.0372112698026876e-13, 2.1999701061313215e-14, 1.4997871132614736e-15], [0.0759960364494748, 0.10635102978992866, 0.05794545325994515, 0.0223851427964954, 0.006485771400021199, 0.0015033267747541423, 0.00029037812830371313, 4.8075921908570835e-05, 6.964651558824935e-06, 8.968475862563202e-07, 1.0393944730216239e-07, 1.0950891535919921e-08, 1.0576208183272245e-09, 9.428625760238466e-11, 7.80516560255972e-12, 6.030490288160997e-13, 4.3681183759506253e-14, 2.9778803044609754e-15], [0.085660253100482, 0.09927527820187296, 0.055474222083584754, 0.022223245971646294, 0.006438864136310334, 0.0014924542137097051, 0.0002882780167518066, 4.7728220793619276e-05, 6.9142808739557416e-06, 8.903612851454237e-07, 1.0318772252435906e-07, 1.0871691032932289e-08, 1.049971751536e-09, 9.360434791471802e-11, 7.748716039563244e-12, 5.986875769423619e-13, 4.336526685780922e-14, 2.9563432800847722e-15], [0.056693819704484914, 0.06570485750126621, 0.03807406452559221, 0.014183652764135258, 0.004261530747725494, 0.0009877735244373299, 0.0001907953959384395, 3.158868957946231e-05, 4.576182991128817e-06, 5.89281263419523e-07, 6.829428964738272e-08, 7.1953755562795605e-09, 6.949186702327088e-10, 6.19515800170224e-11, 5.128449825766123e-12, 3.9623844569628307e-13, 2.8701089848398755e-14, 1.9566413457719343e-15], [0.02814189553801255, 0.032614829019791014, 0.01889935009092364, 0.007301084498354038, 0.0020398934671787636, 0.0004903148082952472, 9.470774997382214e-05, 1.5680114816070682e-05, 2.2715432541051614e-06, 2.9250969231040175e-07, 3.39001812740336e-08, 3.571668099222634e-09, 3.4494639322311223e-10, 3.075176275547282e-11, 2.5456795823766265e-12, 1.9668635849644714e-13, 1.4246756993105803e-14, 9.712451312169063e-16], [0.01117534558229472, 0.012951579075805202, 0.007505065472990549, 0.0028993122472660377, 0.0008400337949147791, 0.00018776163468233834, 3.760911676505258e-05, 6.226684396683845e-06, 9.020458780207759e-07, 1.161576658304337e-07, 1.346200153888129e-08, 1.4183346413235072e-09, 1.3698065030578417e-10, 1.2211742296923426e-11, 1.0109073511563333e-12, 7.810554283921333e-14, 5.6574878763896975e-15, 3.856883048908028e-16], [0.003698173917573701, 0.004285969644233677, 0.00248359544476811, 0.0009594478177684765, 0.000277986130035756, 6.443396884010941e-05, 1.200172678738989e-05, 2.0605503122213915e-06, 2.9850732704288425e-07, 3.8439191605933736e-08, 4.454879950048499e-09, 4.693589239194514e-10, 4.532998683957614e-11, 4.041140966787041e-12, 3.3453204391753695e-13, 2.5846885827275037e-14, 1.87219034520073e-15, 1.276329594424496e-16], [0.0010489792826725627, 0.001215706308889412, 0.0007044666438540408, 0.00027214536311067765, 7.885018330050394e-05, 1.8276560248412715e-05, 3.530246015628949e-06, 5.63620830102223e-07, 8.467097783205013e-08, 1.090319615464704e-08, 1.2636173632039917e-09, 1.331326752885683e-10, 1.2857755783895646e-11, 1.14626116753864e-12, 9.488931328839017e-14, 7.331415006085708e-15, 5.310428684824072e-16, 3.620282150742005e-17], [0.00026034817858793246, 0.0003017284787654038, 0.00017484292648380488, 6.754427925068273e-05, 1.9569978113684778e-05, 4.5360945159983175e-06, 8.761785245125723e-07, 1.4506288944178242e-07, 2.0264992178153644e-08, 2.7060851501443614e-09, 3.136196151596789e-10, 3.304245383532206e-11, 3.191191050539175e-12, 2.8449275603845776e-13, 2.3550760525175663e-14, 1.819597941385134e-15, 1.3180054729895184e-16, 8.985247654450523e-18], [5.743672303474375e-05, 6.656583948671553e-05, 3.857297868378422e-05, 1.490128366153538e-05, 4.3174314443381725e-06, 1.0007306591807735e-06, 1.9329815754567255e-07, 3.200305471187771e-08, 4.636211143493487e-09, 5.757060597538378e-10, 6.918920298151971e-11, 7.289662173252737e-12, 7.040247314765252e-13, 6.276337988073492e-14, 5.195651903073425e-15, 4.0143066704278497e-16, 2.9077182610212556e-17, 1.9822807431431636e-18], [1.1404264296283761e-05, 1.3216882623183454e-05, 7.658801205261997e-06, 2.9587025208114334e-06, 8.572412677954286e-07, 1.9869860820207782e-07, 3.838003214950269e-08, 6.354319587520858e-09, 9.205361033879457e-10, 1.185386771200609e-10, 1.3247690702373754e-11, 1.447388180626335e-12, 1.397865979231055e-13, 1.246189083341309e-14, 1.0316150428410905e-15, 7.970547729229155e-17, 5.773377343926484e-18, 3.9358884542496733e-19], [2.0585063363923046e-06, 2.385689766593912e-06, 1.3824382178987478e-06, 5.340553084669302e-07, 1.5473480232730966e-07, 3.586573700765554e-08, 6.927719081049071e-09, 1.1469750958539133e-09, 1.6615972345708064e-10, 2.1396611970727633e-11, 2.4797435556019362e-12, 2.519382966881105e-13, 2.5231929924774192e-14, 2.2494113234791816e-15, 1.8620982881798034e-16, 1.438709466816031e-17, 1.0421131548774423e-18, 7.104405082094103e-20], [3.4060308857326014e-07, 3.947392769767255e-07, 2.2873999387500126e-07, 8.836547370146903e-08, 2.5602618097751885e-08, 5.9343906709431006e-09, 1.1462692506978683e-09, 1.8977996485020404e-10, 2.749300014550687e-11, 3.5403107551302387e-12, 4.103015370785306e-13, 4.322870427149882e-14, 4.025975020465022e-15, 3.721904716559794e-16, 3.081051619654332e-17, 2.3805070661863642e-18, 1.724293741141228e-19, 1.1755039421825034e-20], [5.20214974374812e-08, 6.028990627106737e-08, 3.493625690554596e-08, 1.3496366938358041e-08, 3.9103771411589375e-09, 9.063801810331419e-10, 1.7507369982353147e-10, 2.898575581476755e-11, 4.1991017832785415e-12, 5.407240070762932e-13, 6.266678452369465e-14, 6.6024707465379025e-15, 6.376568054783846e-16, 5.481807118847272e-17, 4.70579757828944e-18, 3.63583145303404e-19, 2.633573958826555e-20, 1.7953881619850053e-21], [7.3778943718962965e-09, 8.550552792026673e-09, 4.954798033415296e-09, 1.9141081010831495e-09, 5.54585141198991e-10, 1.285464195735491e-10, 2.482964405527569e-11, 4.110874450470036e-12, 5.9553321107495e-13, 7.668761579483203e-14, 8.887651059984384e-15, 9.363884963141213e-16, 9.043500837311026e-17, 8.062226412323446e-18, 6.435866966308625e-19, 5.156479866182451e-20, 3.735038675530267e-21, 2.5462904507117484e-22], [9.766046636083757e-10, 1.131828312008834e-09, 6.558617706839407e-10, 2.533686176490913e-10, 7.340989284502822e-11, 1.7015563861131886e-11, 3.2866757041800395e-12, 5.441524312316333e-13, 7.883014881385213e-14, 1.0151064714550914e-14, 1.176449680110258e-15, 1.2394882961906122e-16, 1.197079362738854e-17, 1.0671890266325392e-18, 8.834359634071228e-20, 6.582091563086678e-21, 4.944034172100749e-22, 3.3704997709629976e-23], [1.2119269158640168e-10, 1.4045531898161195e-10, 8.138979492901986e-11, 3.144202140399844e-11, 9.10987099947533e-12, 2.1115627029381236e-12, 4.078631710496728e-13, 6.752711740140865e-14, 9.7825028580228e-15, 1.2597061032646319e-15, 1.4599265041570361e-16, 1.538154878865306e-17, 1.4855271065041016e-18, 1.3243384492062375e-19, 1.0963083245368279e-20, 8.47038620395346e-22, 5.916479081231385e-23, 4.18265398943619e-24], [1.4154845363154608e-11, 1.64046469683354e-11, 9.506018442851446e-12, 3.67230849528003e-12, 1.0639982790045455e-12, 2.466224913685106e-13, 4.763686687672987e-14, 7.886910440924434e-15, 1.1425591214071826e-15, 1.4712888096903724e-16, 1.7051386215959285e-17, 1.7965063874662855e-18, 1.7350391512964325e-19, 1.5467769311509897e-20, 1.2804464197492177e-21, 9.893088874726532e-23, 7.165948578582964e-24, 4.710910677604572e-25]] |
| Legacy trial inputs | {"lambda_home": 1.9855353324014131, "lambda_away": 1.1589421535495599, "rho": -0.10288407687222552, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5599 |
| Legacy p draw | 0.2301 |
| Legacy p away | 0.2100 |
| Legacy p over 1 5 | 0.8321 |
| Legacy p under 3 5 | 0.6143 |
| Legacy p btts yes | 0.6007 |
| Legacy p over 2 5 | 0.6109 |
| Legacy goal margin distribution | {"-1": 0.12503500110609758, "-10": 6.441376476656085e-08, "-11": 6.6718905956846144e-09, "-12": 6.351086489002065e-10, "-13": 5.5920093022877426e-11, "-14": 4.579384137938011e-12, "-15": 3.5035865401985974e-13, "-16": 2.497758136577419e-14, "-17": 1.4997871132614736e-15, "-2": 0.05909681818976383, "-3": 0.019459752428529226, "-4": 0.005092095965351478, "-5": 0.0011001282576085694, "-6": 0.00020186161866878825, "-7": 3.2140097937057946e-05, "-8": 4.5152827820780695e-06, "-9": 5.672284161675017e-07, "0": 0.23007588753255356, "1": 0.2215546115052274, "10": 1.4032762440146175e-05, "11": 2.490171547468074e-06, "12": 4.0611051798888275e-07, "13": 6.126041801987482e-08, "14": 8.59478478732943e-09, "15": 1.1265660010328392e-09, "16": 1.3759733855473707e-10, "17": 1.4154845363154608e-11, "2": 0.173460944754151, "3": 0.09785674811509223, "4": 0.043869825685519385, "5": 0.01623784940146169, "6": 0.005104518719474094, "7": 0.0013924002911002416, "8": 0.0003351334089703818, "9": 7.212845162843354e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5552 |
| Legacy raw p draw | 0.2366 |
| Legacy raw p away | 0.2083 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9855 |
| Legacy lambda away | 1.1589 |
| Legacy model home team | Man City |
| Legacy model away team | Brighton |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 78.3% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:18:01Z |
| Market reference home draw last update utc | 2026-10-31T11:18:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.7% |
| Market draw away odds | 2.17 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:18:01Z |
| Market reference draw away last update utc | 2026-10-31T11:18:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.0% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:18:01Z |
| Market reference home away last update utc | 2026-10-31T11:18:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.24 |
| Market reference dc draw away odds | 2.17 |
| Market reference dc home away odds | 1.26 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.17, "price": 1.69, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.69, "price": 2.17, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.74, "price": 2.11, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.11, "price": 1.74, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 85.5% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-31T11:17:43Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.7% |
| Market under 3 5 odds | 1.69 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.27 |
| Market reference under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.2% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:18:01Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.76 |
| Market reference btts yes last update utc | 2026-10-31T11:18:05Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 10.249390249828863, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,654.7730 |
| Elo away rating | 1,529.0307 |
| Elo rating diff | 185.7423 |
| Elo home expectancy | 0.7444 |

</details>


---

## 2026-10-31 — Tottenham Hotspur vs Crystal Palace

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **54.5%**. Expected goals are 1.62 for Tottenham Hotspur and 1.21 for Crystal Palace (2.83 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 55.7%; Under 3.5 goals: 67.1%; Double Chance 1X: 78.5%; Double Chance X2: 45.5%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 83.1%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 54.5% | 1.83 |
| Draw | 24.0% | 4.17 |
| Crystal Palace win | 21.5% | 4.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.62 |
| Crystal Palace expected goals | 1.21 |
| Expected total goals | 2.83 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 79.4% |
| Under 1.5 | 20.6% |
| Over 2.5 | 55.7% |
| Under 2.5 | 44.3% |
| Over 3.5 | 32.9% |
| Under 3.5 | 67.1% |
| Over 4.5 | 16.9% |
| Under 4.5 | 83.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.32% |
| 2 | 2-1 | 11.08% |
| 3 | 1-0 | 9.94% |
| 4 | 2-0 | 9.00% |
| 5 | 3-1 | 6.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 54.5% | 58.1% | 1.69 | -7.9% |
| Draw | 24.0% | 23.0% | 4.14 | -0.6% |
| Crystal Palace win | 21.5% | 18.8% | 5.03 | +8.2% |

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
| Market best home last update utc | 2026-10-31T11:18:04Z |
| Market best draw last update utc | 2026-10-31T11:18:04Z |
| Market best away last update utc | 2026-10-31T11:18:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Tottenham |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6563 |
| Dc lambda away | 1.2165 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:17:21.264748+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.5392 |
| Shot lambda away | 1.2062 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.66 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.84 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 3.04 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.93 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.123238460401285, "-10": 1.1477677231992151e-07, "-11": 1.2644401768605261e-08, "-12": 1.2797788853649626e-09, "-13": 1.1974066457596998e-10, "-14": 1.0344814633021495e-11, "-15": 7.47610242320886e-13, "-2": 0.061855944921982986, "-3": 0.02198171138537808, "-4": 0.006173834418020102, "-5": 0.0014270440788664894, "-6": 0.0002795770981925799, "-7": 4.7463676144952896e-05, "-8": 7.103238479948318e-06, "-9": 9.499293006194088e-07, "0": 0.24002135856828236, "1": 0.25441324551887134, "10": 3.169588367490041e-06, "11": 4.665011120629483e-07, "12": 6.308046367670085e-08, "13": 7.885098818281842e-09, "14": 9.101096704995818e-10, "15": 8.787226045470268e-11, "2": 0.16830072377894975, "3": 0.0799045627358666, "4": 0.029982690052023215, "5": 0.009258881918505463, "6": 0.0024234177822123402, "7": 0.0005496593364524229, "8": 0.00010989910932071734, "9": 1.9635167054959426e-05} |
| Raw goal margin distribution | {"-1": 0.15979098317460255, "-10": 1.3379751773800497e-07, "-11": 1.454536968958023e-08, "-12": 1.4526758368332053e-09, "-13": 1.3411372324398811e-10, "-14": 1.143627286973987e-11, "-15": 8.178828435534654e-13, "-2": 0.07957241972317221, "-3": 0.027986134644274775, "-4": 0.0077706328220581815, "-5": 0.0017745104118106932, "-6": 0.0003433261944512398, "-7": 5.754590995004741e-05, "-8": 8.501124805001852e-06, "-9": 1.1220699775806894e-06, "0": 0.262707797975501, "1": 0.2164206496835504, "10": 2.4238372451769802e-06, "11": 3.52034884922429e-07, "12": 4.697158235573478e-08, "13": 5.7935563756071225e-09, "14": 6.600275546918448e-10, "15": 6.30629373878903e-11, "2": 0.14202789304330102, "3": 0.06673590261270192, "4": 0.02475589018295371, "5": 0.007552769851519608, "6": 0.0019522713396857249, "7": 0.00043717290812069187, "8": 8.628210079813335e-05, "9": 1.5214924475168373e-05} |
| Unadjusted home-win probability | 46.0% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.3% |
| P home draw | 78.5% |
| P draw away | 45.5% |
| P home away | 76.0% |
| Raw p home draw | 72.3% |
| Raw p draw away | 54.0% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0138 |
| Totals anchor target over 2 5 | 0.5572 |
| Totals anchor reference over odds | 1.75 |
| Totals anchor reference under odds | 2.18 |
| Totals anchor reference last update utc | 2026-10-31T11:18:04Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5488 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.85, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.86, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.54, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.42, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.69 |
| Reference draw odds | 4.14 |
| Reference away odds | 5.03 |
| Market reference 1x2 last update utc | 2026-10-31T11:18:04Z |
| Market reference home last update utc | 2026-10-31T11:18:04Z |
| Market reference draw last update utc | 2026-10-31T11:18:04Z |
| Market reference away last update utc | 2026-10-31T11:18:04Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.26 |
| Market reference over 2 5 last update utc | 2026-10-31T11:18:05Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:18:05Z |
| Home probability edge | -3.6% |
| Draw probability edge | +1.0% |
| Away probability edge | +2.7% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.1214 |
| Raw ev home | -0.2226 |
| Raw edge prob draw | 0.0324 |
| Raw ev draw | 0.0876 |
| Raw edge prob away | 0.0890 |
| Raw ev away | 0.3948 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.0677169606662519, 0.05132016827508951, 0.036326794764905676, 0.014296391814310543, 0.004219753357631859, 0.000996409087301114, 0.00019606814765223973, 3.306965182449619e-05, 4.8804543179367264e-06, 6.402334476301677e-07, 7.558906542002625e-08, 8.113101460699945e-09, 7.982267501306954e-10, 7.249424680587905e-11, 6.1135873670863575e-12, 4.811998468707319e-13], [0.09785674849959565, 0.11897119225516149, 0.05862185206484877, 0.023070600404560732, 0.006809567391842146, 0.001607941093891016, 0.00031640220450724824, 5.3365683640344294e-05, 7.875764236478517e-06, 1.0331676850885316e-06, 1.2198078689435565e-07, 1.3092402913447502e-08, 1.2881271459042287e-09, 1.1698656705910207e-10, 9.865715280916976e-12, 7.765294576480416e-13], [0.08987452532041419, 0.10611022275054423, 0.051381292813251836, 0.01861492780626432, 0.005494421608809738, 0.001297396116903393, 0.00025529479473282256, 4.305905918688484e-05, 6.354701659702967e-06, 8.336298809928795e-07, 9.84223861525886e-08, 1.0563840158931061e-08, 1.0393484957398998e-09, 9.439271028583135e-11, 7.96032935818711e-12, 6.265567232787892e-13], [0.04834458202573275, 0.05707795784449344, 0.033694502415634354, 0.010877161816190485, 0.0029555150940054693, 0.0006978848875127966, 0.00013732612328913347, 2.3161982902160627e-05, 3.4182700219145296e-06, 4.4841948279651147e-07, 5.2942578595643314e-08, 5.682415959911285e-09, 5.590779859641319e-10, 5.077496775393897e-11, 4.281956363460344e-12, 3.370323547672248e-13], [0.019503846637106484, 0.023027187112005153, 0.013593506864499273, 0.0053497177915940546, 0.0012952353184874788, 0.00028155047051929886, 5.540202305346212e-05, 9.344330706894272e-06, 1.3790462442337996e-06, 1.809076520073856e-07, 2.135883464568505e-08, 2.292479627838423e-09, 2.2555105121444115e-10, 2.048434679918701e-11, 1.727486653525306e-12, 1.3597030078001145e-13], [0.006294811417606904, 0.0074319596049451445, 0.004387265948511502, 0.001726606308082466, 0.0005096287832952554, 9.871013390336322e-05, 1.7880846469124653e-05, 3.0158563445502604e-06, 4.4508328049992795e-07, 5.8387433749709405e-08, 6.893503558351535e-09, 7.398913252575399e-10, 7.27959647578802e-11, 6.611265075701581e-12, 5.575414385019946e-13, 4.388403055718654e-14], [0.001693027172216354, 0.001998869977072313, 0.001179981411642247, 0.0004643810912472235, 0.00013706770872421839, 3.236575670977131e-05, 5.22410998525807e-06, 8.111325979588752e-07, 1.1970780978090739e-07, 1.570364944972737e-08, 1.8540490035039351e-09, 1.9899819629932702e-10, 1.9578910023908146e-11, 1.7781392758773138e-12, 1.4995410384816972e-13, 1.1802872434252369e-14], [0.0003902998130236419, 0.0004608068855082721, 0.00027202547714130147, 0.0001070554897522603, 3.159872562270072e-05, 7.461397548425244e-06, 1.4682146267646398e-06, 2.0312777114481657e-07, 2.7596683940868958e-08, 3.6202203630280308e-09, 4.274207710777256e-10, 4.587578987642136e-11, 4.5135985097831164e-12, 4.099210209345781e-13, 3.4569473930799485e-14, 2.7209598167287453e-15], [7.873010145844843e-05, 9.295257552844462e-05, 5.487215904282338e-05, 2.1594910601119845e-05, 6.373999656725964e-06, 1.5050906160023055e-06, 2.9616382757774e-07, 4.9952196612666414e-08, 6.047033863208471e-09, 7.302599360094315e-10, 8.621802919070125e-11, 9.253926010049959e-12, 9.104694820758243e-13, 8.268803235674414e-14, 6.97325004809103e-15, 5.488638100434835e-16], [1.4116621049486239e-05, 1.6666767348208378e-05, 9.83879686454481e-06, 3.872053559011757e-06, 1.142883548435974e-06, 2.698687475013077e-07, 5.3103354943431215e-08, 8.956627987360132e-09, 1.321828665359123e-09, 1.42236302221605e-10, 1.5459236342544635e-11, 1.6592658244293583e-12, 1.6325080772783892e-13, 1.4826293837864156e-14, 1.2503315325227417e-15, 9.841346918942166e-17], [2.278049787144937e-06, 2.6895760449248642e-06, 1.5877219502080697e-06, 6.248471751844292e-07, 1.8443121871156092e-07, 4.354968803421969e-08, 8.569478914358773e-09, 1.4453631934027663e-09, 2.1330823425858104e-10, 2.7982449446429863e-11, 2.709964019242724e-12, 2.677616792933415e-13, 2.634436856326729e-14, 2.39257223120854e-15, 2.0177048541142903e-16, 1.5881334616353968e-17], [3.341973340580778e-07, 3.945695783439744e-07, 2.329239887465505e-07, 9.166711865506345e-08, 2.705666134177621e-08, 6.3888812800434236e-09, 1.2571705076889094e-09, 2.1203949479359732e-10, 3.129301371029175e-11, 4.105116603764908e-12, 4.84669972597352e-13, 4.2670843297385424e-14, 3.864804795298887e-15, 3.5099815013850196e-16, 2.960038832189652e-17, 2.3298435881516055e-18], [4.494218570710538e-08, 5.3060923763166534e-08, 3.132314980127285e-08, 1.232720985474764e-08, 3.638525430083317e-09, 8.591639121168523e-10, 1.6906176280937116e-10, 2.8514645034836175e-11, 4.208221581021117e-12, 5.520478290938805e-13, 6.517744366968082e-14, 6.9956045957551965e-15, 5.64575210604743e-16, 4.720152568193034e-17, 3.98060072117129e-18, 3.13312682467484e-19], [5.578832118154674e-09, 6.586639725048116e-09, 3.888253127962213e-09, 1.530220063463138e-09, 4.5166300242629537e-10, 1.0665104850294627e-10, 2.0986233256644925e-11, 3.539623519756258e-12, 5.223813961678443e-13, 6.852764526803126e-14, 8.0907061016871e-15, 8.683890867937759e-16, 8.543852211858768e-17, 6.364849984380461e-18, 4.941260155335324e-19, 3.889260899250055e-20], [6.430543963909248e-10, 7.592212030994605e-10, 4.4818668410547494e-10, 1.7638364417767356e-10, 5.20617708592072e-11, 1.2293330246726722e-11, 2.419016968704702e-12, 4.080012478849922e-13, 6.021325723450427e-14, 7.898965702968925e-15, 9.325901942210987e-16, 1.0009647327859518e-16, 9.84822918236053e-18, 8.944074560643447e-19, 6.187072030674549e-20, 4.4830284672580085e-21], [6.918133008768803e-11, 8.167883301316414e-11, 4.821699549528932e-11, 1.8975774333260052e-11, 5.600929835756614e-12, 1.322545872400419e-12, 2.6024363154799554e-13, 4.389375014701107e-14, 6.477886237578481e-15, 8.497896238877684e-16, 1.0033028375989723e-16, 1.0768618016399063e-17, 1.0594960514505252e-18, 9.622249345957508e-20, 8.114638697043497e-21, 5.239088388894455e-22]] |
| Legacy trial inputs | {"lambda_home": 1.6137358785499494, "lambda_away": 1.1806484915747562, "rho": -0.10288407687222552, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5219 |
| Legacy p draw | 0.2503 |
| Legacy p away | 0.2278 |
| Legacy p over 1 5 | 0.7831 |
| Legacy p under 3 5 | 0.6894 |
| Legacy p btts yes | 0.5608 |
| Legacy p over 2 5 | 0.5379 |
| Legacy goal margin distribution | {"-1": 0.13181273403246924, "-10": 8.977336316765167e-08, "-11": 9.500039243554244e-09, "-12": 9.235106789027518e-10, "-13": 8.298651881007481e-11, "-14": 6.8901168247343994e-12, "-15": 4.811998468707319e-13, "-2": 0.06564824296112108, "-3": 0.022550487000822433, "-4": 0.0061075905636861355, "-5": 0.0013594766257684764, "-6": 0.0002562590711569571, "-7": 4.183435560941344e-05, "-8": 6.017959120129112e-06, "-9": 7.733582063605287e-07, "0": 0.2503459864330263, "1": 0.24355470551449954, "10": 2.705526119670379e-06, "11": 3.9132849552321997e-07, "12": 5.1995987890592236e-08, "13": 6.386270316749424e-09, "14": 7.247332294040889e-10, "15": 6.918133008768803e-11, "2": 0.16241743078169696, "3": 0.0762565745743067, "4": 0.028229495797646463, "5": 0.008588489501873641, "6": 0.002212769263088902, "7": 0.000493743969817782, "8": 9.708000551490923e-05, "9": 1.7051912509588707e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4624 |
| Legacy raw p draw | 0.2704 |
| Legacy raw p away | 0.2673 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6137 |
| Legacy lambda away | 1.1806 |
| Legacy model home team | Tottenham |
| Legacy model away team | Crystal Palace |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 81.0% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:18:01Z |
| Market reference home draw last update utc | 2026-10-31T11:18:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.4% |
| Market draw away odds | 2.29 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:18:01Z |
| Market reference draw away last update utc | 2026-10-31T11:18:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.5% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:18:01Z |
| Market reference home away last update utc | 2026-10-31T11:18:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.29 |
| Market reference dc home away odds | 1.27 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.31, "price": 1.6, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.6, "price": 2.31, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.84, "price": 2.01, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.01, "price": 1.84, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.53, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.53, "price": 1.51, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 79.6% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-31T11:17:43Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.9% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.84 |
| Market reference under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.5% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:18:01Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.24 |
| Market reference btts yes last update utc | 2026-10-31T11:18:05Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 10.028655619350316, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,397.3033 |
| Elo away rating | 1,450.5828 |
| Elo rating diff | 6.7205 |
| Elo home expectancy | 0.5097 |

</details>


---

## 2026-11-01 — Liverpool vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **39.2%**. Expected goals are 1.24 for Liverpool and 1.39 for Arsenal (2.63 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 51.6%; Under 3.5 goals: 70.3%; Double Chance 1X: 60.8%; Double Chance X2: 67.2%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 85.6%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 32.8% | 3.05 |
| Draw | 28.0% | 3.57 |
| Arsenal win | 39.2% | 2.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.24 |
| Arsenal expected goals | 1.39 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 76.9% |
| Under 1.5 | 23.1% |
| Over 2.5 | 51.6% |
| Under 2.5 | 48.4% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.4% |
| Under 4.5 | 85.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.29% |
| 2 | 1-2 | 8.58% |
| 3 | 0-1 | 8.21% |
| 4 | 2-1 | 7.83% |
| 5 | 0-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 32.8% | 33.0% | 2.93 | -3.9% |
| Draw | 28.0% | 28.0% | 3.44 | -3.7% |
| Arsenal win | 39.2% | 39.0% | 2.49 | -2.4% |
| Over 2.5 | 51.6% | 51.6% | 1.88 | -3.0% |
| Under 2.5 | 48.4% | 48.4% | 2.00 | -3.2% |

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
| Market best home last update utc | 2026-10-31T11:18:04Z |
| Market best draw last update utc | 2026-10-31T11:18:04Z |
| Market best away last update utc | 2026-10-31T11:18:04Z |
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
| Dc lambda away | 1.4389 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:17:21.264748+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.3547 |
| Shot lambda away | 1.2844 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.35 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.33 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.07 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.95 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.19948868880808188, "-10": 8.811982609118621e-07, "-11": 1.151163954501735e-07, "-12": 1.3814342120156685e-08, "-13": 1.5323872803742678e-09, "-14": 1.5707467937790783e-10, "-15": 1.3556112396485015e-11, "-2": 0.11913469699780414, "-3": 0.05057339228235386, "-4": 0.016920360292338805, "-5": 0.004651382623447545, "-6": 0.0010826697084958584, "-7": 0.00021822965446565657, "-8": 3.875827365376299e-05, "-9": 6.149066948147544e-06, "0": 0.27979945408840584, "1": 0.18104772964653593, "10": 2.7575832047484473e-07, "11": 3.198446064467608e-08, "12": 3.4078377681003416e-09, "13": 3.3563256976136065e-10, "14": 3.0545595534252484e-11, "15": 2.340585073747697e-12, "2": 0.09654247238038798, "3": 0.036387238114606174, "4": 0.010808949029410321, "5": 0.0026381700387910594, "6": 0.0005452096812768136, "7": 9.757267088585205e-05, "8": 1.5385999294472887e-05, "9": 2.167291661871326e-06} |
| Raw goal margin distribution | {"-1": 0.20627644519314148, "-10": 6.371517057298391e-07, "-11": 7.96344849041358e-08, "-12": 9.139075632544386e-09, "-13": 9.638872436453248e-10, "-14": 8.537799172028138e-11, "-2": 0.11982161624496934, "-3": 0.049106198809472035, "-4": 0.01580655953191812, "-5": 0.004172117910085134, "-6": 0.000931275963298697, "-7": 0.00017986576973941647, "-8": 3.0591838161199184e-05, "-9": 4.646008507590904e-06, "0": 0.2800811141185164, "1": 0.18209065159247562, "10": 1.9395965480757179e-07, "11": 2.1523682791696635e-08, "12": 2.193130801257195e-09, "13": 2.0536921869506657e-10, "14": 1.615109264850903e-11, "2": 0.09445585507163223, "3": 0.03436979038693078, "4": 0.009822561854187123, "5": 0.0023019233056765643, "6": 0.0004562044583527833, "7": 7.823057229021976e-05, "8": 1.181354976209292e-05, "9": 1.5929483628747222e-06} |
| Unadjusted home-win probability | 32.4% |
| Unadjusted draw probability | 28.0% |
| Unadjusted away-win probability | 39.6% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 73.0% |
| Raw p btts yes | 54.3% |
| P home draw | 60.8% |
| P draw away | 67.2% |
| P home away | 72.0% |
| Raw p home draw | 60.4% |
| Raw p draw away | 67.6% |
| Raw p home away | 72.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0465 |
| Totals anchor target over 2 5 | 0.5162 |
| Totals anchor reference over odds | 1.88 |
| Totals anchor reference under odds | 2.00 |
| Totals anchor reference last update utc | 2026-10-31T11:18:04Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4889 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.48, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.0, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.8, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.12, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.33, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.56, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.71, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:18:18Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.8, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.93 |
| Reference draw odds | 3.44 |
| Reference away odds | 2.49 |
| Market reference 1x2 last update utc | 2026-10-31T11:18:04Z |
| Market reference home last update utc | 2026-10-31T11:18:04Z |
| Market reference draw last update utc | 2026-10-31T11:18:04Z |
| Market reference away last update utc | 2026-10-31T11:18:04Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market best over 2 5 last update utc | 2026-10-31T11:18:04Z |
| Market best under 2 5 last update utc | 2026-10-31T11:18:04Z |
| Home probability edge | -0.2% |
| Draw probability edge | +0.0% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0064 |
| Raw ev home | -0.0519 |
| Raw edge prob draw | 0.0004 |
| Raw ev draw | -0.0365 |
| Raw edge prob away | 0.0060 |
| Raw ev away | -0.0131 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.09713832023860268, 0.10287956950754103, 0.08202682202156854, 0.03901272303113195, 0.01391611171316268, 0.003971179659695846, 0.0009443650768881526, 0.00019249236640053944, 3.4331688057551446e-05, 5.442823881145827e-06, 7.76597369064984e-07, 1.007337178454922e-07, 1.197747437164226e-08, 1.3145997072588665e-09, 1.3397912243512875e-10], [0.08596634382874051, 0.13592682123304034, 0.08389145727306614, 0.03989956098032903, 0.014232453024756085, 0.004061452589952147, 0.0009658324014687133, 0.00019686810647175982, 3.511211663222787e-05, 5.566550255353144e-06, 7.942509949752761e-07, 1.0302359860254176e-07, 1.2249746542949847e-08, 1.3444832123777016e-09, 1.3702473835075652e-10], [0.051523859832167944, 0.07351568756127201, 0.044962327919497835, 0.02040327927318232, 0.007277992706478953, 0.00207688880307324, 0.0004938938608364608, 0.00010067165797403679, 1.7955142961926084e-05, 2.8465445899058607e-06, 4.0615296171987733e-07, 5.2682766485882306e-08, 6.264104005172549e-09, 6.875230149467507e-10, 7.006979363215456e-11], [0.01756503372566439, 0.025062282515040668, 0.017879783627912017, 0.00729020540854241, 0.0024811453909093376, 0.0007080335593891245, 0.00016837368843773605, 3.4320042661642777e-05, 6.121099869122266e-06, 9.70417431577741e-07, 1.3846187947926386e-07, 1.796011737280762e-08, 2.135499911503729e-09, 2.34383933658062e-10, 2.388754049693159e-11], [0.004491080600163555, 0.0064079996974136175, 0.004571556800890816, 0.0021742751321920674, 0.0006648953082248623, 0.00018103214787405545, 4.3050290567665675e-05, 8.775051628240435e-06, 1.56506120644177e-06, 2.481192446930237e-07, 3.5402349377953463e-08, 4.5920967741623734e-09, 5.460110338525764e-10, 5.992798840481182e-11, 6.107638128507658e-12], [0.0009186343856633846, 0.001310733293263616, 0.0009350955031086869, 0.0004447401590280287, 0.00015864193154179338, 3.881027728575447e-05, 8.805782115515257e-06, 1.7949052531766115e-06, 3.2012764140836667e-07, 5.075189920028113e-08, 7.241423249155762e-09, 9.392968807742696e-10, 1.1168459337610741e-10, 1.2258054511489256e-11, 1.2492954145226356e-12], [0.00015658613328167447, 0.00022342148449787272, 0.00015939201859413647, 7.580833343940847e-05, 2.70413638158414e-05, 7.716675186958473e-06, 1.5731775158651394e-06, 3.059511788239097e-07, 5.456746482281892e-08, 8.650932053598707e-09, 1.2343392363028942e-09, 1.6010816583767177e-10, 1.9037234940070057e-11, 2.0894508059634393e-12, 2.1294907020637929e-13], [2.2877950312921767e-05, 3.26429008371187e-05, 2.328790299146955e-05, 1.107594427031659e-05, 3.950866943368489e-06, 1.1274415416505666e-06, 2.681108661422994e-07, 4.685059779043151e-08, 7.972556207597846e-09, 1.2639407432500655e-09, 1.8034260841366778e-10, 2.3392535379478417e-11, 2.7814271029407427e-12, 3.052783201060134e-13, 3.111283320727222e-14], [2.9247515383857326e-06, 4.173117483641522e-06, 2.9771605046981893e-06, 1.4159653553135973e-06, 5.050847655721911e-07, 1.4413382048128734e-07, 3.4275695920395405e-08, 6.986503397058224e-09, 1.0682395389671248e-09, 1.6158408348151208e-10, 2.305526999490229e-11, 2.990536866374308e-12, 3.555818194796483e-13, 3.902723907314259e-14, 3.977511339165365e-15], [3.323596716697603e-07, 4.7422009647628064e-07, 3.383152636602421e-07, 1.6090590069320134e-07, 5.739626243384221e-08, 1.6378919242524367e-08, 3.894983520084822e-09, 7.939245247640905e-10, 1.4159922097234993e-10, 1.9244964556254847e-11, 2.6199292025990916e-12, 3.398353118135511e-13, 4.0407212449649616e-14, 4.434934111253113e-15, 4.51992022364192e-16], [3.3991487793885855e-08, 4.850000765738358e-08, 3.4600585255779416e-08, 1.6456361663552572e-08, 5.870099534437972e-09, 1.6751245140911736e-09, 3.983524358271168e-10, 8.119720319016249e-11, 1.4481805711036585e-11, 2.2958940391748854e-12, 2.808345921318224e-13, 3.47560454474138e-14, 4.132574995837516e-15, 4.535749116371034e-16, 4.622667134655283e-17], [3.1603802663463113e-09, 4.509319158004337e-09, 3.217011491508403e-09, 1.5300407258638556e-09, 5.457762497075338e-10, 1.5574577053255527e-10, 3.703707189496588e-11, 7.54936177553426e-12, 1.3464551262876396e-12, 2.1346221321726237e-13, 3.0457386973986694e-14, 3.3868714806410164e-15, 3.8422879708108286e-16, 4.2171416818816495e-17, 4.297954263973122e-18], [2.693518408030802e-10, 3.8431875711629e-10, 2.741783880723358e-10, 1.3040180335373316e-10, 4.6515237134826816e-11, 1.3273848858300964e-11, 3.1565832754671185e-12, 6.434145007111436e-13, 1.1475523078227526e-13, 1.819288668652534e-14, 2.595812072000867e-15, 3.367070392675735e-16, 3.432177270493942e-17, 3.594171521186653e-18, 3.663046200535138e-19], [2.1190365529471603e-11, 3.023500756053964e-11, 2.1570078178087106e-11, 1.0258930737317917e-11, 3.6594324903747225e-12, 1.0442761722055406e-12, 2.4833375273000945e-13, 5.0618508551420614e-14, 9.027988371807987e-15, 1.4312652097505945e-15, 2.0421693234956502e-16, 2.6489313075243844e-17, 3.1496412052197403e-18, 2.9635788872078837e-19, 2.8817804886445775e-20], [1.548004665342339e-12, 2.208736451255702e-12, 1.5757435427453166e-12, 7.49438353043269e-13, 2.673299127250431e-13, 7.628676269089005e-14, 1.8141348588506927e-14, 3.697797816714873e-15, 6.595151980166734e-16, 1.0455719694663284e-16, 1.4918513962364407e-17, 1.9351049025162237e-18, 2.3008849342657867e-19, 2.5253593263229917e-20, 2.2064490666909047e-21]] |
| Legacy trial inputs | {"lambda_home": 1.0227320186927065, "lambda_away": 1.4268280326966862, "rho": -0.10288407687222552, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-31T11:18:04Z", "over": 1.88, "under": 2.0, "bookmaker": "pinnacle", "event_id": "6a3819cdbe2ba2fe5a3d8f9b4b459965", "kickoff_utc": "2026-11-01T16:30:00Z", "home_team": "Liverpool", "away_team": "Arsenal"}} |
| Legacy p home | 0.2937 |
| Legacy p draw | 0.2860 |
| Legacy p away | 0.4203 |
| Legacy p over 1 5 | 0.7140 |
| Legacy p under 3 5 | 0.7694 |
| Legacy p btts yes | 0.4992 |
| Legacy p over 2 5 | 0.4445 |
| Legacy goal margin distribution | {"-1": 0.20984560346266257, "-10": 8.86125563244485e-07, "-11": 1.1369487494388572e-07, "-12": 1.3392027377652115e-08, "-13": 1.451624445609623e-09, "-14": 1.3397912243512875e-10, "-2": 0.12995731031839136, "-3": 0.055499542560974724, "-4": 0.018507395277810403, "-5": 0.005044060342604732, "-6": 0.0011601951047461659, "-7": 0.0002305941954040836, "-8": 4.032290987403471e-05, "-9": 6.291954319802309e-06, "0": 0.28602300150107635, "1": 0.17970272399814077, "10": 3.8785511600612574e-08, "11": 3.5670185399937317e-09, "12": 3.0116259190636514e-10, "13": 2.3399101980727306e-11, "14": 1.548004665342339e-12, "2": 0.0816306431968033, "3": 0.02498803623793553, "4": 0.005972803725994438, "5": 0.0011668188475846071, "6": 0.00019237312957735083, "7": 2.7406398724017197e-05, "8": 3.435149838498312e-06, "9": 3.8421082834125905e-07} |
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
| Market p home draw | 61.0% |
| Market home draw odds | 1.58 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:18:01Z |
| Market reference home draw last update utc | 2026-10-31T11:18:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.0% |
| Market draw away odds | 1.44 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:18:01Z |
| Market reference draw away last update utc | 2026-10-31T11:18:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.0% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:18:01Z |
| Market reference home away last update utc | 2026-10-31T11:18:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.58 |
| Market reference dc draw away odds | 1.44 |
| Market reference dc home away odds | 1.34 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.59, "price": 1.47, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.47, "price": 2.59, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.02, "price": 1.81, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.81, "price": 2.02, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.62, "price": 2.25, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:18:01Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.25, "price": 1.62, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 75.9% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 3.58 |
| Market reference over 1 5 last update utc | 2026-10-31T11:18:18Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.5% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:18:04Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.15 |
| Market reference under 3 5 last update utc | 2026-10-31T11:18:18Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.2% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:18:01Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-31T11:18:05Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 9.78696978427008, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,570.2236 |
| Elo away rating | 1,650.6613 |
| Elo rating diff | -20.4377 |
| Elo home expectancy | 0.4706 |

</details>


---

## 2026-11-02 — Newcastle United vs Everton

The model's most likely 1X2 outcome is **Newcastle United win** at **42.9%**. Expected goals are 1.62 for Newcastle United and 1.09 for Everton (2.71 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 50.6%; Under 3.5 goals: 71.5%; Double Chance 1X: 69.7%; Double Chance X2: 57.1%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 86.3%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 42.9% | 2.33 |
| Draw | 26.8% | 3.73 |
| Everton win | 30.3% | 3.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.62 |
| Everton expected goals | 1.09 |
| Expected total goals | 2.71 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 28.5% |
| Under 3.5 | 71.5% |
| Over 4.5 | 13.7% |
| Under 4.5 | 86.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.78% |
| 2 | 1-0 | 8.69% |
| 3 | 2-1 | 8.37% |
| 4 | 1-2 | 7.85% |
| 5 | 0-1 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Newcastle United win | 42.9% | 40.4% | 2.41 | +3.4% |
| Draw | 26.8% | 26.9% | 3.57 | -4.3% |
| Everton win | 30.3% | 32.7% | 2.96 | -10.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T20:00:00+00:00 |
| Fixture id | 0f552d9c6990c69474f50ff2fb54e9a3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-31T11:18:04Z |
| Market best draw last update utc | 2026-10-31T11:18:04Z |
| Market best away last update utc | 2026-10-31T11:18:04Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Newcastle |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5938 |
| Dc lambda away | 1.0349 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:17:21.264748+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6804 |
| Shot lambda away | 1.2236 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.12 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.15 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.51 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.31 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.18333141945693543, "-10": 6.31606708899556e-08, "-11": 6.185464650051302e-09, "-12": 5.563814664587112e-10, "-13": 4.625878471319993e-11, "-14": 3.5561513502506684e-12, "-15": 2.314899630343996e-13, "-2": 0.08416886854432382, "-3": 0.026958822820064295, "-4": 0.006788594018995913, "-5": 0.001402566942099542, "-6": 0.00024514494447293967, "-7": 3.708270212806088e-05, "-8": 4.9405621688499905e-06, "-9": 5.878259439184118e-07, "0": 0.2680815074596212, "1": 0.19923482422555577, "10": 2.3494314985813903e-06, "11": 3.414304671739209e-07, "12": 4.5573930780047126e-08, "13": 5.622791026026385e-09, "14": 6.414338143166769e-10, "15": 6.196089331497288e-11, "2": 0.13315467468894712, "3": 0.0632877627858907, "4": 0.023648987236587777, "5": 0.007250537427886691, "6": 0.0018805437089900537, "7": 0.0004221295490193902, "8": 8.345735953582824e-05, "9": 1.4735026187003016e-05} |
| Raw goal margin distribution | {"-1": 0.14969593929841674, "-10": 5.157269814196267e-08, "-11": 5.0506287658133e-09, "-12": 4.543031765994246e-10, "-13": 3.7771770103336427e-11, "-14": 2.903710767308785e-12, "-15": 1.890189229824309e-13, "-2": 0.06872656020310364, "-3": 0.02201273691320044, "-4": 0.00554310309274575, "-5": 0.001145240550956506, "-6": 0.00020016864995558, "-7": 3.0279206604230932e-05, "-8": 4.034126265530553e-06, "-9": 4.799785933011616e-07, "0": 0.26507539800191116, "1": 0.2264442106498766, "10": 2.6702920196818594e-06, "11": 3.880594315353629e-07, "12": 5.179793653953067e-08, "13": 6.390692392692839e-09, "14": 7.290340648612795e-10, "15": 7.042285721087578e-11, "2": 0.15133953274224904, "3": 0.07193093648941219, "4": 0.026878715948751387, "5": 0.008240739193196678, "6": 0.00213736849182926, "7": 0.0004797795410076863, "8": 9.48550835752412e-05, "9": 1.6747380317628062e-05} |
| Unadjusted home-win probability | 48.8% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 54.2% |
| P home draw | 69.7% |
| P draw away | 57.1% |
| P home away | 73.2% |
| Raw p home draw | 75.3% |
| Raw p draw away | 51.2% |
| Raw p home away | 73.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5060 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:18:04Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:17:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.41 |
| Reference draw odds | 3.57 |
| Reference away odds | 2.96 |
| Market reference 1x2 last update utc | 2026-10-31T11:18:04Z |
| Market reference home last update utc | 2026-10-31T11:18:04Z |
| Market reference draw last update utc | 2026-10-31T11:18:04Z |
| Market reference away last update utc | 2026-10-31T11:18:04Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.24 |
| Market reference over 2 5 last update utc | 2026-10-31T11:18:05Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:18:05Z |
| Home probability edge | +2.5% |
| Draw probability edge | -0.1% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | 0.0837 |
| Raw ev home | 0.1750 |
| Raw edge prob draw | -0.0043 |
| Raw ev draw | -0.0537 |
| Raw edge prob away | -0.0794 |
| Raw ev away | -0.2678 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.081625355487024, 0.07455728310966248, 0.04997010301008912, 0.018842376341927553, 0.0053287134430033386, 0.001205588358596163, 0.0002272974058261311, 3.6731877126509775e-05, 5.193974578334843e-06, 6.528358479711371e-07, 7.385003029405377e-08, 7.594596003911077e-09, 7.159292629519877e-10, 6.22979055050787e-11, 5.033755229045345e-12, 3.796186308427985e-13], [0.09010777929233513, 0.131313170822735, 0.075811498930438, 0.02858646886528408, 0.00808438904765303, 0.0018290428686890655, 0.00034484133513192734, 5.57272948372177e-05, 7.879971712498814e-06, 9.90441508199868e-07, 1.1204062340075785e-07, 1.1522043624992448e-08, 1.08616287105903e-09, 9.451446589200012e-11, 7.636896987901113e-12, 5.759335220962522e-13], [0.07735595735017073, 0.08750652727618313, 0.05108459481872668, 0.02168479674104256, 0.006132563420127911, 0.0013874544290548086, 0.0002615857976543152, 4.2272974223156375e-05, 5.977498854999059e-06, 7.513177962070183e-07, 8.499049521067829e-08, 8.740260128903594e-09, 8.239290133237037e-10, 7.169570301301553e-11, 5.7931100093313346e-12, 4.3688506691278814e-13], [0.03911986517706011, 0.04425313403673443, 0.02502999260362422, 0.009741345933629807, 0.0031013132330479135, 0.0007016528792765205, 0.00013228717589451372, 2.1377966337579877e-05, 3.0228951630068383e-06, 3.79950709674458e-07, 4.2980745476689113e-08, 4.420057737859383e-09, 4.1667110098302357e-10, 3.6257404493715047e-11, 2.929647441308786e-12, 2.209381862877486e-13], [0.014837550046828896, 0.016784518249927646, 0.009493482818693631, 0.0035797359879232633, 0.00104488983961112, 0.0002661259098068637, 5.017444676776394e-05, 8.10832665188399e-06, 1.1465366269649717e-06, 1.4410933280590087e-07, 1.630192126618969e-08, 1.6764584335484804e-09, 1.5803680012497222e-10, 1.3751863696582528e-11, 1.1111692316228492e-12, 8.379838175471018e-14], [0.004502119634527781, 0.005092883186954383, 0.002880583065479019, 0.0010861900803562545, 0.00030717970906737256, 7.17301964216425e-05, 1.5224303286713889e-05, 2.4602886937128578e-06, 3.478906587457443e-07, 4.3726724068088766e-08, 4.946450025873663e-09, 5.086834690583833e-10, 4.7952699642124736e-11, 4.172692618682425e-12, 3.371592209754024e-13, 2.5426727367309943e-14], [0.0011383888141701926, 0.0012877670347630423, 0.0007283732566501091, 0.0002746498844804416, 7.767229063850263e-05, 1.7572873899276373e-05, 3.419566406026798e-06, 6.220992234574147e-07, 8.796630623344026e-08, 1.105657281464932e-08, 1.2507405036776774e-09, 1.286237635020313e-10, 1.2125136894009595e-11, 1.0550911543195442e-12, 8.525279577404929e-14, 6.429305386269858e-15], [0.00024672742062377737, 0.00027910274143287076, 0.000157863159429951, 5.9525934135142425e-05, 1.6834216644290627e-05, 3.808637080886811e-06, 7.180670931716942e-07, 1.1976956837765844e-07, 1.9065278548611297e-08, 2.396333886578023e-09, 2.710778378185488e-10, 2.7877126869795872e-11, 2.6279279217530448e-12, 2.286739959035704e-13, 1.847716890790897e-14, 1.3934482793677261e-15], [4.678991651506265e-05, 5.2929641698327756e-05, 2.993750768300132e-05, 1.1288625648591641e-05, 3.1924769018029753e-06, 7.222780937778421e-07, 1.36175781584284e-07, 2.2006375561481672e-08, 3.211722639383585e-09, 4.544458909825598e-10, 5.1407781788285125e-11, 5.2866780498894215e-12, 4.983658798667682e-13, 4.336622638230872e-14, 3.5040498881317082e-15, 2.6425651634032552e-16], [7.887413322412599e-06, 8.922391664185187e-06, 5.046589404850063e-06, 1.9029325753074826e-06, 5.381583623614546e-07, 1.217549908967283e-07, 2.295525946305254e-08, 3.709632175252304e-09, 5.245507913160183e-10, 6.804943704789222e-11, 8.665850532605017e-12, 8.911795101959749e-13, 8.400993147811267e-14, 7.310279162401806e-15, 5.906804676847672e-16, 4.4545930464441985e-17], [1.1966287652744575e-06, 1.3536491729259626e-06, 7.656368192615162e-07, 2.8870096759354526e-07, 8.164600362007304e-08, 1.8471901809526252e-08, 3.482627658141438e-09, 5.628020731309602e-10, 7.958154848467206e-11, 1.0002684245809897e-11, 1.167874186537247e-12, 1.352041529120109e-13, 1.2745458677788177e-14, 1.1090695986552822e-15, 8.961432726098834e-17, 6.7582285333263294e-18], [1.6504090335851722e-07, 1.866974025807996e-07, 1.055978227854821e-07, 3.981808717525551e-08, 1.1260744003574931e-08, 2.547673472227465e-09, 4.803294316840112e-10, 7.762253863275286e-11, 1.0976011135389567e-11, 1.3795857928919467e-12, 1.560613635341006e-13, 1.6564648003780427e-14, 1.7578735151150669e-15, 1.5296460670285961e-16, 1.2359747612808793e-17, 9.321054069660952e-19], [2.086580694379823e-08, 2.36037968763245e-08, 1.3350531529392393e-08, 5.034124892454019e-09, 1.423674408226646e-09, 3.22097502773945e-10, 6.072713483136465e-11, 9.813669657879727e-12, 1.3876761742300483e-12, 1.7441840314190582e-13, 1.9730540833351583e-14, 2.0290511184806037e-15, 1.9742004297752098e-16, 1.9339023767717268e-17, 1.562619340508052e-18, 1.1784431057539603e-19], [2.435099274772824e-09, 2.754630521131435e-09, 1.5580451660757737e-09, 5.874967552296904e-10, 1.661468702515596e-10, 3.758969866459413e-11, 7.087030105530603e-12, 1.145283282411744e-12, 1.619457735130377e-13, 2.0355125883311532e-14, 2.3026104767278267e-15, 2.367960616331524e-16, 2.2322349969327122e-17, 2.0048231109678412e-18, 1.8236214075334932e-19, 1.3752767673504323e-20], [2.6388425270388564e-10, 2.985108755419831e-10, 1.6884058427850477e-10, 6.366522458687343e-11, 1.8004827626385993e-11, 4.0734805534349584e-12, 7.679997537112132e-13, 1.241108427259793e-13, 1.7549567635605947e-14, 2.205822669349813e-15, 2.4952684730939637e-16, 2.5660864185143828e-17, 2.419004720372245e-18, 2.104941581305299e-19, 1.7554623171740308e-20, 1.4903453250263953e-21], [2.6689906612867872e-11, 3.0192128971338336e-11, 1.7076954690100704e-11, 6.4392584297846236e-12, 1.8210528404219164e-12, 4.1200190783082475e-13, 7.76773964161446e-14, 1.2552877892709296e-14, 1.7750067178739012e-15, 2.2310236570106077e-16, 2.523776308685003e-17, 2.595403331912764e-18, 2.44664126113165e-19, 2.1289900270639984e-20, 1.7202528069655776e-21, 1.3389998112522802e-22]] |
| Legacy trial inputs | {"lambda_home": 1.5171371352812986, "lambda_away": 1.131218981365111, "rho": -0.10288407687222552, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4264 |
| Legacy p draw | 0.2749 |
| Legacy p away | 0.2987 |
| Legacy p over 1 5 | 0.7537 |
| Legacy p under 3 5 | 0.7262 |
| Legacy p btts yes | 0.5408 |
| Legacy p over 2 5 | 0.4951 |
| Legacy goal margin distribution | {"-1": 0.17543688385503522, "-10": 8.62333969328226e-08, "-11": 8.755468023806185e-09, "-12": 8.16457777039607e-10, "-13": 7.03716875598926e-11, "-14": 5.6096887511415975e-12, "-15": 3.796186308427985e-13, "-2": 0.08544351332519108, "-3": 0.028454974544862996, "-4": 0.007441911618158729, "-5": 0.0015958747501927403, "-6": 0.0002893989731901171, "-7": 4.540787286565806e-05, "-8": 6.273988935622236e-06, "-9": 7.740474980540045e-07, "0": 0.2748846297150794, "1": 0.20654952835121274, "10": 1.3972826129694133e-06, "11": 1.9026823167834476e-07, "12": 2.3795717307637952e-08, "13": 2.750687105004908e-09, "14": 2.94076381675224e-10, "15": 2.6689906612867872e-11, "2": 0.13227038518006928, "3": 0.05907719640089958, "4": 0.020721650218119708, "5": 0.005959595574940815, "6": 0.0014494162514286553, "7": 0.00030500394274897105, "8": 5.651922513034413e-05, "9": 9.3518647410447e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4489 |
| Legacy raw p draw | 0.2804 |
| Legacy raw p away | 0.2707 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5171 |
| Legacy lambda away | 1.1312 |
| Legacy model home team | Newcastle |
| Legacy model away team | Everton |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009189157242000747, "mu": 10.130337476180937, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,496.2139 |
| Elo away rating | 1,476.4968 |
| Elo rating diff | 79.7171 |
| Elo home expectancy | 0.6128 |

</details>


---
