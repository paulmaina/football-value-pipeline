# Ligue 1 — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,751 |
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
| Training sha256 | dcb4f67f73dec029a09c4b807eb50a43374b03d4f76d82f7042fe6eda94a0d6f |
| Training as of utc | 2026-10-26T10:55:19.374605+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 71, 'bbs_added_results': 8, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 71, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 80, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-26T10:55:19.374605+00:00', 'observations': 278, 'observations_sha256': 'f15706afdba55ec4b08959f76ce1965327f38aa94fa471773b034c391c8f8aef', 'eligible_training_matches': 115, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 122, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 14, 'retrospective_eligible_training_matches': 115, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '481fe77c86554edabad44b4faa13b6ff0b095bdefe697545466dd95806316859', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-26', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1741, 'tune_start_date': '2025-10-27', 'audit_start_date': '2026-04-27', 'training_shot_matches': 1453, 'tuning_matches': 196, 'audit_matches': 88, 'audit_matchdays': 28, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.873365030729784, 'audit_candidate_poisson_score': 0.8692351434347145, 'audit_gain': 0.004129887295069468, 'audit_gain_lower95': -0.0034463444146306393, 'audit_baseline_briers': [0.6036683508631172, 0.16968918140114747, 0.22109314542147204, 0.24521839802974899], 'audit_candidate_briers': [0.602908213184978, 0.16856938601387472, 0.21938689348044688, 0.24310665446246993], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1588.396 |
| Base scoring parameter | 0.209 |
| Home-advantage parameter | 0.191 |
| Dixon-Coles low-score adjustment | -0.056 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1751, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Additional event odds calls used before this league | 4.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261026T105519374605Z_d2e9cde8f5d2af5842e30d0c722e04396a33f2dfb16255ac63870318130f81c6.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'AVAILABLE': 1} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-26 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **71.3%**. Expected goals are 2.23 for Paris Saint Germain and 1.08 for Lyon (3.31 combined). The most likely exact score is 2-1 at 11.1%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 66.2%; Under 3.5 goals: 56.7%; Double Chance 1X: 87.6%; Double Chance X2: 28.7%; Double Chance 12 (either team wins): 83.7%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 58.0%; BTTS No (at least one team does not score): 42.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 71.3% | 1.40 |
| Draw | 16.3% | 6.14 |
| Lyon win | 12.4% | 8.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.23 |
| Lyon expected goals | 1.08 |
| Expected total goals | 3.31 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 66.2% |
| Under 2.5 | 33.8% |
| Over 3.5 | 43.3% |
| Under 3.5 | 56.7% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.14% |
| 2 | 2-0 | 10.29% |
| 3 | 1-0 | 8.68% |
| 4 | 3-1 | 8.27% |
| 5 | 3-0 | 7.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 71.3% | 75.0% | 1.35 | -3.7% |
| Draw | 16.3% | 14.5% | 5.70 | -7.2% |
| Lyon win | 12.4% | 10.5% | 8.47 | +4.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T19:30:00+00:00 |
| Fixture id | 8664b2167f22c59026d86615421463b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T10:55:32Z |
| Market best draw last update utc | 2026-10-26T10:55:32Z |
| Market best away last update utc | 2026-10-26T10:55:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2285 |
| Dc lambda away | 1.0820 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:55:19.374605+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 58.0% |
| P btts no | 42.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.22 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.88 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.96 |
| Fair Over 3.5 odds | 2.31 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 3.98 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.07787309723883576, "-10": 2.0267532023731785e-08, "-11": 1.9583968377862754e-09, "-12": 1.739324503017172e-10, "-13": 1.4289661507126365e-11, "-14": 1.0919792092586143e-12, "-15": 7.796136073821449e-14, "-16": 5.183495509328064e-15, "-17": 2.889392178751638e-16, "-2": 0.03290456065238485, "-3": 0.01005158552939331, "-4": 0.0024450957648990317, "-5": 0.000491676519732801, "-6": 8.403622620194806e-05, "-7": 1.2469932584650572e-05, "-8": 1.6332962085250352e-06, "-9": 1.9134457887657788e-07, "0": 0.16289098560376697, "1": 0.2530765616344008, "10": 4.287659777464685e-05, "11": 8.532705023695922e-06, "12": 1.560749599444653e-06, "13": 2.640834239583418e-07, "14": 4.15623556569176e-08, "15": 6.1112743294698916e-09, "16": 8.368385514263618e-10, "17": 9.607093758765263e-11, "2": 0.21505169735478757, "3": 0.1352969276304179, "4": 0.06778222479463009, "5": 0.028071524494092597, "6": 0.009881426739572855, "7": 0.003019839094955926, "8": 0.0008146128103768603, "9": 0.00019654818049113577} |
| Raw goal margin distribution | {"-1": 0.10563804434250972, "-10": 2.749373689439533e-08, "-11": 2.6566454825316045e-09, "-12": 2.359464892120794e-10, "-13": 1.938451081892319e-11, "-14": 1.4813145003719236e-12, "-15": 1.0575777739271318e-13, "-16": 7.0316238582908135e-15, "-17": 3.9195787752698565e-16, "-2": 0.044636383558838894, "-3": 0.01363538725845155, "-4": 0.0033168725014480786, "-5": 0.0006669793270762815, "-6": 0.00011399858108470538, "-7": 1.6915974040242472e-05, "-8": 2.2156331700978614e-06, "-9": 2.59566754434705e-07, "0": 0.2040333969859668, "1": 0.22280822519598603, "10": 3.774849235707591e-05, "11": 7.5121807020478255e-06, "12": 1.37408160590538e-06, "13": 2.3249865027342443e-07, "14": 3.659143556826081e-08, "15": 5.380356751495741e-09, "16": 7.367514052456715e-10, "17": 8.458070932598598e-11, "2": 0.1893311917293387, "3": 0.11911521211257647, "4": 0.059675369021901584, "5": 0.024714128051533623, "6": 0.008699593277345655, "7": 0.0026586618088188948, "8": 0.0007171838961688772, "9": 0.00017304072324166408} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 84.8% |
| Raw p under 3 5 | 57.8% |
| Raw p btts yes | 59.5% |
| P home draw | 87.6% |
| P draw away | 28.7% |
| P home away | 83.7% |
| Raw p home draw | 83.2% |
| Raw p draw away | 37.2% |
| Raw p home away | 79.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.6618 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:54:13Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.61, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:54:13Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:54:13Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:54:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:54:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:55:32Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:55:32Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:54:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:54:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:54:13Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:54:13Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:54:13Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 5.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:37Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 7.01, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:55:37Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.13, "price": 7.01, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.30 |
| Reference draw odds | 5.80 |
| Reference away odds | 7.80 |
| Market reference 1x2 last update utc | 2026-10-26T10:55:34Z |
| Market reference home last update utc | 2026-10-26T10:55:34Z |
| Market reference draw last update utc | 2026-10-26T10:55:34Z |
| Market reference away last update utc | 2026-10-26T10:55:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.15 |
| Market reference over 2 5 last update utc | 2026-10-26T10:55:34Z |
| Market reference under 2 5 last update utc | 2026-10-26T10:55:34Z |
| Home probability edge | -3.7% |
| Draw probability edge | +1.8% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.1219 |
| Raw ev home | -0.1523 |
| Raw edge prob draw | 0.0588 |
| Raw ev draw | 0.1630 |
| Raw edge prob away | 0.0631 |
| Raw ev away | 0.4232 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.030480857040999634, 0.02342434000837018, 0.015093010827151448, 0.005514870455497006, 0.001511318541205234, 0.0003313345256498683, 6.053354785598593e-05, 9.47935471951339e-06, 1.2988813302025988e-06, 1.582004270092323e-07, 1.7341566986569636e-08, 1.728129719742571e-09, 1.5786133800305128e-10, 1.3311074484256632e-11, 1.0422352662553726e-12, 7.616495533427801e-14, 5.218142026891402e-15, 3.364710167887988e-16, 2.0490655033095128e-17], [0.07133831794400436, 0.07390080026236572, 0.03659375903885814, 0.013371079030562352, 0.0036642673328195563, 0.0008033371162150017, 0.00014676661200190827, 2.2983169257767266e-05, 3.149202697979917e-06, 3.835648415096854e-07, 4.2045495821228094e-08, 4.189936870540518e-09, 3.827427032678848e-10, 3.2273365321444776e-11, 2.5269514897941288e-12, 1.846657406283722e-13, 1.2651646126105752e-14, 8.15790795682661e-16, 4.9680617168878477e-17], [0.09274482898097569, 0.10166474862534196, 0.04625275054994677, 0.01620942467137534, 0.00444209963693723, 0.0009738654929226987, 0.00017792149280399918, 2.7861921236253422e-05, 3.817699662915728e-06, 4.6498606363990517e-07, 5.0970702942300984e-08, 5.079355669471969e-09, 4.6398940601268864e-10, 3.912419355790276e-11, 3.063360086976835e-12, 2.238656585050073e-13, 1.5337274155755543e-14, 9.889627770499609e-16, 6.022656958243282e-17], [0.07495482429356276, 0.08216375461347654, 0.04503300912122452, 0.013658621862945782, 0.003590030856053731, 0.000787061852500241, 0.00014379318370307974, 2.2517540154964764e-05, 3.0854012087093264e-06, 3.7579398314739146e-07, 4.11936721986218e-08, 4.105050555518078e-09, 3.7498850107200617e-10, 3.161952085071483e-11, 2.4757565417944903e-12, 1.8092449231910827e-13, 1.2395329228788276e-14, 7.992632257897541e-16, 4.8674109278710027e-17], [0.04543292936065988, 0.0498025323192074, 0.027296195296107946, 0.009973820512682492, 0.0022688131256936644, 0.0004770676988990627, 8.715844002435304e-05, 1.3648725360619605e-05, 1.870177356637793e-06, 2.2778282320598723e-07, 2.4969029235212215e-08, 2.4882250564732192e-09, 2.2729459031934964e-10, 1.9165777129996065e-11, 1.500648866002354e-12, 1.0966511837788722e-13, 7.513273796067388e-15, 4.844634087281511e-16, 2.950320262097648e-17], [0.022030881558271986, 0.024149745707934135, 0.013236197930057501, 0.004836405256946437, 0.0013253890543013466, 0.00024119624605041943, 4.226399873398754e-05, 6.6184033491259405e-06, 9.068676930333637e-07, 1.1045416770782103e-07, 1.2107731846635237e-08, 1.2065652001949169e-09, 1.1021741870110433e-10, 9.29367689614123e-12, 7.276796344124804e-13, 5.317771202640363e-14, 3.643261560399306e-15, 2.34921149201716e-16, 1.4306397841369388e-17], [0.008902495558923806, 0.009758710896128396, 0.005348637228959617, 0.0019543510416157196, 0.0005355786666345933, 0.00011741780347381034, 1.7806553558405066e-05, 2.6744416135557314e-06, 3.664576738977413e-07, 4.463360827766302e-08, 4.892633493045073e-09, 4.875629378641068e-10, 4.4537939977903875e-11, 3.755497349260846e-12, 2.9404927335937836e-13, 2.1488670069629305e-14, 1.4722116214761515e-15, 9.49296777767977e-17, 5.7810960905087785e-18], [0.0030835064848285455, 0.003380068895582408, 0.0018525768950213427, 0.0006769173958657933, 0.0001855053204770409, 4.0669333227905135e-05, 7.430131298251603e-06, 9.658187161745702e-07, 1.2692784920810098e-07, 1.5459487696965317e-08, 1.6946334883111776e-09, 1.6887438704297114e-10, 1.542635161498164e-11, 1.300770144006914e-12, 1.0184816552409188e-13, 7.442907785966145e-15, 5.099215216469521e-16, 3.28802497108828e-17, 2.002365198220408e-18], [0.000934514446726435, 0.0010243932449612034, 0.0005614581582971155, 0.00020515250698822368, 5.622086503899513e-05, 1.2325603862747212e-05, 2.2518405826140026e-06, 3.5263083712155163e-07, 4.01076734220548e-08, 4.685287565596603e-09, 5.13590447928397e-10, 5.118054888167463e-11, 4.675245054749287e-12, 3.9422277768048155e-13, 3.0866995909736645e-14, 2.2557127367367223e-15, 1.545412766343834e-16, 9.964976080957137e-18, 6.068543116630614e-19], [0.0002517529977099651, 0.00027596584638815767, 0.00015125370713652824, 5.5266945099585996e-05, 1.5145588553493706e-05, 3.3204491721897312e-06, 6.066333367278409e-07, 9.499678752030342e-08, 1.3016661723328715e-08, 1.315995117553547e-09, 1.3835841202252453e-10, 1.3787755395904365e-11, 1.2594850317026442e-12, 1.062014251296677e-13, 8.315397132487808e-15, 6.07676473526212e-16, 4.163256095068182e-17, 2.6845091686671876e-18, 1.6348317853144587e-19], [6.103877245576308e-05, 6.690929862394273e-05, 3.667221720089863e-05, 1.3399747041523512e-05, 3.672123636399977e-06, 8.050594960768301e-07, 1.4708128420091226e-07, 2.30324458903186e-08, 3.1559546869000518e-09, 3.8438721650691504e-10, 3.497567501042529e-11, 3.342910201434371e-12, 3.053684403397045e-13, 2.5749066275014817e-14, 2.0161095918070074e-15, 1.4733419793085857e-16, 1.0094022465412601e-17, 6.508726640485209e-19, 3.9637313658612406e-20], [1.3453777663016051e-05, 1.4747721670308246e-05, 8.083056666781634e-06, 2.953486942548977e-06, 8.093861158665345e-07, 1.774460892634609e-07, 3.2418720370958527e-08, 5.0766651027979025e-09, 6.956154418550703e-10, 8.472418332360116e-11, 9.28727013109069e-12, 7.682322973241512e-13, 6.730736769992935e-14, 5.675445274483174e-15, 4.44378042040466e-16, 3.2474466005310666e-17, 2.224860175121825e-18, 1.4346120927300797e-19, 8.736604352728113e-21], [2.7182796925068547e-06, 2.9797156851598517e-06, 1.6331479039597124e-06, 5.96739724641417e-07, 1.6353309065044983e-07, 3.585224262220282e-08, 6.550067308134741e-09, 1.0257190210991001e-09, 1.4054620023837422e-10, 1.711816805371107e-11, 1.8764542144596294e-12, 1.8699326873144007e-13, 1.4178878995425583e-14, 1.1467000586735652e-15, 8.97847309306404e-17, 6.56133048117066e-18, 4.495237236843941e-19, 2.89857392917456e-20, 1.7651944894831795e-21], [5.069696125577277e-07, 5.557284302280697e-07, 3.045883624125381e-07, 1.112942526971041e-07, 3.049955007792755e-08, 6.686581076114921e-09, 1.2216127334452855e-09, 1.913005406151344e-10, 2.6212406647381716e-11, 3.192604149532743e-12, 3.4996592466524297e-13, 3.4874963478189694e-14, 3.1857610771804093e-15, 2.2298056853447346e-16, 1.6745197478751282e-17, 1.2237133585155936e-18, 8.383790257492411e-20, 5.4059518080288616e-21, 3.2921555824045025e-22], [8.779808299740044e-08, 9.624223944117216e-08, 5.27492647699732e-08, 1.9274176979042014e-08, 5.281977386406641e-09, 1.1579964276906961e-09, 2.1156150882612796e-10, 3.312983722562391e-11, 4.5395207077157404e-12, 5.529020224394673e-13, 6.060784816076572e-14, 6.0397208474516765e-15, 5.517169245174907e-16, 4.652149265537938e-17, 3.023589120256585e-18, 2.119252995735435e-19, 1.4519227476899314e-20, 9.362143090326137e-22, 5.701425527380947e-23], [1.4191389334992884e-08, 1.555627462186984e-08, 8.526215242165115e-09, 3.1154136888073154e-09, 8.537612096991251e-10, 1.87174680731653e-10, 3.419609674323994e-11, 5.354996403368968e-12, 7.337529881986597e-13, 8.936923901602467e-14, 9.796450453605295e-15, 9.76240335718921e-16, 8.917768374013833e-17, 7.519578926763676e-18, 5.887706776889473e-19, 3.5715117454824906e-20, 2.346839508718035e-21, 1.5132655870022298e-22, 9.215594083748479e-24], [2.1504832919798003e-09, 2.3573103288267477e-09, 1.2920146850518901e-09, 4.72092261528293e-10, 1.2937417003078451e-10, 2.8363397979826842e-11, 5.1818840961492946e-12, 8.114660250819383e-13, 1.1118879937080243e-13, 1.3542511644509592e-14, 1.4844989820157506e-15, 1.4793396765908284e-16, 1.3513484435787436e-17, 1.1394746816546835e-18, 8.921899577905845e-20, 6.5199874236611165e-21, 3.707865262701977e-22, 2.2931175266624676e-23, 1.3964792759157246e-24], [3.0670318905736346e-10, 3.3620098242354387e-10, 1.8426789256732433e-10, 6.733007537423378e-11, 1.845142004965826e-11, 4.045204464205521e-12, 7.390433506467581e-13, 1.157317606849236e-13, 1.5857811814519693e-14, 1.9314409578107926e-15, 2.1172011595471494e-16, 2.109842927874083e-17, 1.927301080268976e-18, 1.6251254776867995e-19, 1.2724465533857172e-20, 9.298844324476392e-22, 6.370737061173493e-23, 3.409870835201034e-24, 1.991666938186533e-25], [4.131206720392233e-11, 4.5285337992714603e-11, 2.4820373027952637e-11, 9.069174035178559e-12, 2.485355002150673e-12, 5.448777992576041e-13, 9.954708544885863e-14, 1.55887465328885e-14, 2.136003180801822e-15, 2.601597293289438e-16, 2.851811122546728e-17, 2.8418997889765088e-18, 2.59602099329239e-19, 2.188998854408605e-20, 1.7139501447126547e-21, 1.2525284879895105e-22, 8.581205771567414e-24, 5.533247305944375e-25, 2.7970790797261925e-26]] |
| Legacy trial inputs | {"lambda_home": 2.4245499760079743, "lambda_away": 1.0961770024525677, "rho": -0.06160611751733561, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7056 |
| Legacy p draw | 0.1668 |
| Legacy p away | 0.1276 |
| Legacy p over 1 5 | 0.8748 |
| Legacy p under 3 5 | 0.5257 |
| Legacy p btts yes | 0.6038 |
| Legacy p over 2 5 | 0.6930 |
| Legacy goal margin distribution | {"-1": 0.08033969246881056, "-10": 2.202866811625031e-08, "-11": 2.152585778422134e-09, "-12": 1.933867418798334e-10, "-13": 1.6074785731591122e-11, "-14": 1.2430670474679113e-12, "-15": 8.985423834671243e-14, "-16": 6.094159392156495e-15, "-17": 3.8615163395767727e-16, "-18": 2.0490655033095128e-17, "-2": 0.033787410635375686, "-3": 0.010311398438703993, "-4": 0.002517080388194921, "-5": 0.0005092888540437692, "-6": 8.773643222444677e-05, "-7": 1.3137339455450528e-05, "-8": 1.7377588151267654e-06, "-9": 2.057201824664888e-07, "0": 0.16682185291970342, "1": 0.2294604992336903, "10": 7.753641073454713e-05, "11": 1.675823876680726e-05, "12": 3.330006320115285e-06, "13": 6.122291558004424e-07, "14": 1.0471618773469856e-07, "15": 1.6742036730422133e-08, "16": 2.511504647431297e-09, "17": 3.5198852705007806e-10, "18": 4.131206720392233e-11, "2": 0.20761978222733, "3": 0.1401463668876555, "4": 0.07566792330938031, "5": 0.03386330597567417, "6": 0.012903145873626825, "7": 0.0042733996778163705, "8": 0.0012502764339594212, "9": 0.00032737378529551725} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6614 |
| Legacy raw p draw | 0.1884 |
| Legacy raw p away | 0.1502 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.4245 |
| Legacy lambda away | 1.0962 |
| Legacy model home team | Paris SG |
| Legacy model away team | Lyon |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 88.5% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-26T10:55:37Z |
| Market reference home draw last update utc | 2026-10-26T10:55:37Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 28.2% |
| Market draw away odds | 3.45 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-26T10:55:37Z |
| Market reference draw away last update utc | 2026-10-26T10:55:37Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.2% |
| Market home away odds | 1.17 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-26T10:55:37Z |
| Market reference home away last update utc | 2026-10-26T10:55:37Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.45 |
| Market reference dc home draw odds | 1.10 |
| Market reference dc home away odds | 1.17 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:55:37Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.54, "price": 1.48, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:55:37Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.48, "price": 2.54, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:55:37Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.01, "price": 1.8, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:55:37Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.8, "price": 2.01, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:55:37Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.58, "price": 2.3, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:55:37Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.3, "price": 1.58, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 88.5% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 7.40 |
| Market reference over 1 5 last update utc | 2026-10-26T10:55:33Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 50.3% |
| Market under 3 5 odds | 1.91 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-26T10:55:32Z |
| Market reference under 3 5 odds | 1.93 |
| Market reference under 3 5 opposite odds | 1.95 |
| Market reference under 3 5 last update utc | 2026-10-26T10:55:33Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.1% |
| Market btts yes odds | 1.65 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-26T10:55:37Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.34 |
| Market reference btts yes last update utc | 2026-10-26T10:55:37Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015553586640413052, "mu": 9.539580188438363, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,650.2101 |
| Elo away rating | 1,562.7526 |
| Elo rating diff | 147.4576 |
| Elo home expectancy | 0.7003 |

</details>


---
