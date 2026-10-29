# Bundesliga — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,595 |
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
| Training sha256 | 06debe711522955ad060af84bffa2407baee549b899203439be3c3f334178961 |
| Training as of utc | 2026-10-29T11:57:09.762880+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 55, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-29T11:57:09.762880+00:00', 'observations': 273, 'observations_sha256': '31451cc8cf8ed55bf701b893734092212cfd2325b5758f9f8ca06f243a899933', 'eligible_training_matches': 63, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 98, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 14, 'retrospective_eligible_training_matches': 63, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'bb286f060ce438b97ba59a81e19c2b17cb82ff915ae624a17c41d3275d0fdd77', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-29', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1592, 'tune_start_date': '2025-10-30', 'audit_start_date': '2026-04-30', 'training_shot_matches': 1295, 'tuning_matches': 207, 'audit_matches': 84, 'audit_matchdays': 27, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.7185807275797149, 'audit_candidate_poisson_score': 0.7073568627976201, 'audit_gain': 0.011223864782094806, 'audit_gain_lower95': 0.0026007605798779062, 'audit_baseline_briers': [0.6258397368528292, 0.15380899896647546, 0.29442742944181494, 0.24506499984455776], 'audit_candidate_briers': [0.6198846178831948, 0.1512842324079272, 0.2911675744948323, 0.24281744538200445], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1577.580 |
| Base scoring parameter | 0.225 |
| Home-advantage parameter | 0.227 |
| Dixon-Coles low-score adjustment | -0.074 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1595, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261029T115709762880Z_ad0f28be0b3cde4437ee6a3b100181cd41cdb248f1277efdb99c1060586b4d2d.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 6} |
| Shot features applied fixtures | 7 |
| Goal rate features used | {'shot_features': 7} |
| Legacy comparison status | {'AVAILABLE': 7} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Elversberg vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **41.7%**. Expected goals are 1.83 for Elversberg and 1.67 for FSV Mainz 05 (3.51 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 65.8%; Under 3.5 goals: 56.1%; Double Chance 1X: 58.3%; Double Chance X2: 65.8%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 74.6%; BTTS Yes (both teams score): 67.4%; BTTS No (at least one team does not score): 32.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 34.2% | 2.92 |
| Draw | 24.1% | 4.15 |
| FSV Mainz 05 win | 41.7% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 1.83 |
| FSV Mainz 05 expected goals | 1.67 |
| Expected total goals | 3.51 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 85.9% |
| Under 1.5 | 14.1% |
| Over 2.5 | 65.8% |
| Under 2.5 | 34.2% |
| Over 3.5 | 43.9% |
| Under 3.5 | 56.1% |
| Over 4.5 | 25.4% |
| Under 4.5 | 74.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.40% |
| 2 | 1-2 | 9.36% |
| 3 | 2-1 | 7.11% |
| 4 | 2-2 | 6.96% |
| 5 | 0-1 | 5.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 34.2% | 31.1% | 3.10 | +6.1% |
| Draw | 24.1% | 24.4% | 3.93 | -5.2% |
| FSV Mainz 05 win | 41.7% | 44.5% | 2.19 | -8.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T19:30:00+00:00 |
| Fixture id | b275fe870ec88a9f0054c9220beb2673 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:57:03Z |
| Market best draw last update utc | 2026-10-29T11:57:03Z |
| Market best away last update utc | 2026-10-29T11:57:03Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Elversberg |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8827 |
| Dc lambda away | 1.7412 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:57:09.762880+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.6419 |
| Shot lambda away | 1.4043 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 67.4% |
| P btts no | 32.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.50 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.09 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
| Fair Over 3.5 odds | 2.28 |
| Fair Under 3.5 odds | 1.78 |
| Fair Over 4.5 odds | 3.94 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.20749842262731516, "-10": 1.7827749827284822e-06, "-11": 2.570073084141017e-07, "-12": 3.407119791216122e-08, "-13": 4.179692619035118e-09, "-14": 4.767265184726055e-10, "-15": 5.023345145675606e-11, "-16": 4.310573011068761e-12, "-2": 0.12535972691447245, "-3": 0.05585757855837637, "-4": 0.0199825332202833, "-5": 0.005938815890338521, "-6": 0.001505006980910117, "-7": 0.0003318349379351883, "-8": 6.46793029781277e-05, "-9": 1.1288490396540334e-05, "0": 0.24110159544252474, "1": 0.158174257143073, "10": 3.089772158543335e-06, "11": 4.881832123958766e-07, "12": 7.093036812442224e-08, "13": 9.536666553887038e-09, "14": 1.1921447965256051e-09, "15": 1.376766083669881e-10, "16": 1.294820564756795e-11, "2": 0.1043586415093264, "3": 0.05096357997255841, "4": 0.019981855290717568, "5": 0.006508674767898574, "6": 0.0018077512329429271, "7": 0.0004368473492639207, "8": 9.332121172937509e-05, "9": 1.7850827331942016e-05} |
| Raw goal margin distribution | {"-1": 0.1714921443991827, "-10": 1.8775815507929603e-06, "-11": 2.7933343415554846e-07, "-12": 3.822334693704507e-08, "-13": 4.8407850299876285e-09, "-14": 5.69985328532595e-10, "-15": 6.191947386479236e-11, "-16": 5.434713665167113e-12, "-2": 0.10521741137180572, "-3": 0.047945094941923776, "-4": 0.01759739395435034, "-5": 0.005376495962182588, "-6": 0.0014024976833205381, "-7": 0.00031859011455081116, "-8": 6.401653778162767e-05, "-9": 1.1523290305371664e-05, "0": 0.23536701203740767, "1": 0.18860432758590578, "10": 4.695406968442407e-06, "11": 7.656050593056247e-07, "12": 1.1482012874260832e-07, "13": 1.593721960936463e-08, "14": 2.0566854722550095e-09, "15": 2.448718734204803e-10, "16": 2.3555686037136372e-11, "2": 0.12638702726695564, "3": 0.06311993053457408, "4": 0.025390901991347564, "5": 0.00850230224463659, "6": 0.0024307864742617188, "7": 0.0006051797640967718, "8": 0.00013327593167323512, "9": 2.6293202792004442e-05} |
| Unadjusted home-win probability | 41.5% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 34.9% |
| Raw p over 1 5 | 87.2% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 69.0% |
| P home draw | 58.3% |
| P draw away | 65.8% |
| P home away | 75.9% |
| Raw p home draw | 65.1% |
| Raw p draw away | 58.5% |
| Raw p home away | 76.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9677 |
| Totals anchor target over 2 5 | 0.6585 |
| Totals anchor reference over odds | 1.48 |
| Totals anchor reference under odds | 2.74 |
| Totals anchor reference last update utc | 2026-10-29T11:57:03Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6783 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.57, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.98, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.78, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.16, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 5.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:10Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.81, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:10Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.33, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:10Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.64, "price": 2.33, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.10 |
| Reference draw odds | 3.93 |
| Reference away odds | 2.19 |
| Market reference 1x2 last update utc | 2026-10-29T11:57:03Z |
| Market reference home last update utc | 2026-10-29T11:57:03Z |
| Market reference draw last update utc | 2026-10-29T11:57:03Z |
| Market reference away last update utc | 2026-10-29T11:57:03Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.72 |
| Market reference over 2 5 last update utc | 2026-10-29T11:56:21Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:56:21Z |
| Home probability edge | +3.1% |
| Draw probability edge | -0.2% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | 0.1041 |
| Raw ev home | 0.2871 |
| Raw edge prob draw | -0.0082 |
| Raw ev draw | -0.0750 |
| Raw edge prob away | -0.0959 |
| Raw ev away | -0.2348 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.042045133197463634, 0.04799582654131466, 0.05006076593689674, 0.0279612728844848, 0.011713256379848705, 0.003925440035205162, 0.0010962706818590188, 0.0002624221336698756, 5.4965625923414e-05, 1.0233621992176583e-05, 1.7147865704688347e-06, 2.6121498727058915e-07, 3.647518872262653e-08, 4.701483301031754e-09, 5.62713798556505e-10, 6.286038091041948e-11, 6.583210292147066e-12], [0.040856301067005926, 0.10446735885348475, 0.08885253398705954, 0.049628284801351986, 0.020789783997742905, 0.0069672384673835465, 0.0019457638371270518, 0.00046577137034321456, 9.755813867563233e-05, 1.8163590365692197e-05, 3.043563740618635e-06, 4.6362881390280447e-07, 6.473957968894971e-08, 8.34463270739985e-09, 9.987571299698865e-10, 1.1157048891986626e-10, 1.1684497935255073e-11], [0.04452836610834052, 0.0746135085562817, 0.06992299012907247, 0.0440424629897797, 0.018449827471393128, 0.006183053546358908, 0.0017267619085877687, 0.00041334731639730495, 8.657765887279426e-05, 1.6119220312460298e-05, 2.7010009300095734e-06, 4.1144591152087236e-07, 5.745293341966929e-08, 7.405417669581663e-09, 8.863438280921404e-10, 9.901287438551517e-11, 1.0369370408981161e-11], [0.02634437094588074, 0.04414368005773629, 0.0369844566234458, 0.023106305595763245, 0.010915493679047001, 0.003658087426949451, 0.0010216062306075155, 0.00024454917133407393, 5.122204473933296e-05, 9.536633754686303e-06, 1.5979964378709365e-06, 2.4342424087376533e-07, 3.399094829246956e-08, 4.381276187452495e-09, 5.243886680243053e-10, 5.857910629110924e-11, 6.13484312145626e-12], [0.01168961396728919, 0.01958758400534691, 0.01641086900902577, 0.009166235834492097, 0.00429500388185392, 0.0016231790072907233, 0.000453310594772299, 0.00010851219088845911, 2.2728420080633676e-05, 4.231627597740524e-06, 7.090684198984568e-07, 1.0801303291470956e-07, 1.5082579300804516e-08, 1.9440747862459156e-09, 2.32683525092239e-10, 2.5992920479998787e-11, 2.72217347633865e-12], [0.004149564246114109, 0.0069531755696798985, 0.005825509334873892, 0.003253818697237853, 0.001363057138769973, 0.0005109478575863088, 0.0001609156163510218, 3.8519519022464196e-05, 8.068105550891049e-06, 1.5021377636241844e-06, 2.517042026787805e-07, 3.834232856204095e-08, 5.353994749607014e-09, 6.901051863091356e-10, 8.25977007525131e-11, 9.226933736025041e-12, 9.663136661949585e-13], [0.00122750584983757, 0.0020568578242215387, 0.0017232765569390905, 0.0009625303401220056, 0.0004032135694898197, 0.00013512815199164636, 4.2211142998520814e-05, 1.13946747486276e-05, 2.3866715089662917e-06, 4.4435578840292204e-07, 7.44580305043452e-08, 1.1342259045723705e-08, 1.5837951855539296e-09, 2.0414388185241165e-10, 2.4433688658222258e-11, 2.7294709673770664e-12, 2.8585065989593614e-13], [0.0003112417570378076, 0.000521529117985373, 0.00043694750906055497, 0.0002440555654389862, 0.00010223731304099608, 3.4262584945495116e-05, 9.568625943482885e-06, 2.562029125981187e-06, 6.051554328812686e-07, 1.1266917901103811e-07, 1.8879297595863702e-08, 2.8759004567156603e-09, 4.01581138212135e-10, 5.1761953301217155e-11, 6.195314010036e-12, 6.920743716068937e-13, 7.247921600389986e-14], [6.9052626038157e-05, 0.0001157073379067167, 9.694191816876805e-05, 5.414658320008815e-05, 2.26825443081801e-05, 7.601555420645137e-06, 2.12291164033645e-06, 5.081765037308097e-07, 1.1905759875704317e-07, 2.499697585028833e-08, 4.188593102537628e-09, 6.380521709252151e-10, 8.909547492874331e-11, 1.1483995072933975e-11, 1.3745029124482296e-12, 1.5354479819158127e-13, 1.6080362242808383e-14], [1.3617896142205046e-05, 2.2818690626392694e-05, 1.911795465561208e-05, 1.0678269441434628e-05, 4.47323368207714e-06, 1.499105800557967e-06, 4.186602580646986e-07, 1.0021769260290022e-07, 2.0991096008114847e-08, 4.3714461284080075e-09, 8.260341296910973e-10, 1.2583052514420995e-10, 1.7570554429742042e-11, 2.2647632852426605e-12, 2.7106627195517916e-13, 3.0280631380961086e-14, 3.171214702690611e-15], [2.417031695705068e-06, 4.050074837004056e-06, 3.3932335712603274e-06, 1.8952792285759914e-06, 7.939513915344954e-07, 2.6607533185204756e-07, 7.430774202619141e-08, 1.7787574303853863e-08, 3.725696234527633e-09, 6.93658377964366e-10, 1.300104199731198e-10, 2.2333579606190355e-11, 3.118586492679843e-12, 4.019713901867284e-13, 4.811137962212348e-14, 5.3744899395225864e-15, 5.6285687379666e-16], [3.899976483509984e-07, 6.534956347009659e-07, 5.475116919023914e-07, 3.058108188761313e-07, 1.281072052773109e-07, 4.293230986209301e-08, 1.198984882820647e-08, 2.8700956469451853e-09, 6.011558609338347e-10, 1.1192452984616585e-10, 1.8754521207932823e-11, 3.1955515018706804e-12, 5.031962967161418e-13, 6.485967774265171e-14, 7.762961877947938e-15, 8.671952631918123e-16, 9.081918848186989e-17], [5.76836947665111e-08, 9.665710263312011e-08, 8.098125065710477e-08, 4.523180590174039e-08, 1.894805509174877e-08, 6.350023565981603e-09, 1.773392180766215e-09, 4.2450953729873793e-10, 8.891564176304277e-11, 1.6554511145977177e-11, 2.773940000470996e-12, 4.225567860111595e-13, 6.599884870924268e-14, 9.593252342368425e-15, 1.1482026246696577e-15, 1.282649448693597e-16, 1.343286650440391e-17], [7.87557090148165e-09, 1.3196621124915644e-08, 1.1056392691595626e-08, 6.175511049060327e-09, 2.5869832354581254e-09, 8.669704848553037e-10, 2.421217280254018e-10, 5.795840528045273e-11, 1.2139677317655644e-11, 2.2601920143506977e-12, 3.787268003305592e-13, 5.769179560365351e-14, 8.055889726612896e-15, 1.1614557960268503e-15, 1.5676442392353619e-16, 1.7512048622789274e-17, 1.8339930025943724e-18], [9.984500380903754e-10, 1.6730427583805271e-09, 1.4017086306706931e-09, 7.829196536090869e-10, 3.2797285965597577e-10, 1.0991288434266481e-10, 3.0695736422611546e-11, 7.347857404094791e-12, 1.5390454142109007e-12, 2.8654288445240965e-13, 4.8014270069583455e-14, 7.314057131671957e-15, 1.0213105189460342e-15, 1.316422071591434e-16, 1.7623803613092715e-17, 2.2201445245290063e-18, 2.3251017687534684e-19], [1.1814284005114101e-10, 1.9796486099605842e-10, 1.658589135500058e-10, 9.263993978721317e-11, 3.8807795704589874e-11, 1.3005578465689463e-11, 3.632111112304174e-12, 8.694443476319311e-13, 1.8210945892728012e-13, 3.390554246499952e-14, 5.681348102156747e-15, 8.654448884439945e-16, 1.2084783482322574e-16, 1.557672755877455e-17, 1.864356198341546e-18, 2.329539919801124e-19, 2.7512055274577685e-20], [1.3105685803184588e-11, 2.1960410526464198e-11, 1.839887044955915e-11, 1.0276627370322213e-11, 4.3049818084478945e-12, 1.4427198887906153e-12, 4.0291317712955287e-13, 9.644820150325172e-14, 2.0201557279778906e-14, 3.761170684067409e-15, 6.302367806051931e-16, 9.600453809142697e-17, 1.3405753175586111e-17, 1.7279396460990546e-18, 2.068146199135494e-19, 2.3103122438011267e-20, 2.7063453948243097e-21]] |
| Legacy trial inputs | {"lambda_home": 1.7748936182690676, "lambda_away": 1.6756399364562804, "rho": -0.11084550577255979, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3545 |
| Legacy p draw | 0.2444 |
| Legacy p away | 0.4011 |
| Legacy p over 1 5 | 0.8691 |
| Legacy p under 3 5 | 0.5477 |
| Legacy p btts yes | 0.6857 |
| Legacy p over 2 5 | 0.6700 |
| Legacy goal margin distribution | {"-1": 0.19360243749688066, "-10": 2.240491790288249e-06, "-11": 3.3391133253129106e-07, "-12": 4.576746653788597e-08, "-13": 5.8053881485086126e-09, "-14": 6.846536578853524e-10, "-15": 7.454487884567456e-11, "-16": 6.583210292147066e-12, "-2": 0.1222912994086823, "-3": 0.05607276084675207, "-4": 0.020676113910338544, "-5": 0.006340268320869981, "-6": 0.00165890539254066, "-7": 0.0003778110666194154, "-8": 7.608943928632004e-05, "-9": 1.3724652067045742e-05, "0": 0.24439263624966687, "1": 0.163128785878374, "10": 3.1580254734634978e-06, "11": 4.985343138449167e-07, "12": 7.237896944369309e-08, "13": 9.724749200782503e-09, "14": 1.214813769535993e-09, "15": 1.4010325057760522e-10, "16": 1.3105685803184588e-11, "2": 0.10877643699656213, "3": 0.05283027056061408, "4": 0.0206343805785183, "5": 0.006702267898400583, "6": 0.0018574938720587093, "7": 0.0004480970357130117, "8": 9.559020766564508e-05, "9": 1.826341510169235e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3979 |
| Legacy raw p draw | 0.2452 |
| Legacy raw p away | 0.3569 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7749 |
| Legacy lambda away | 1.6756 |
| Legacy model home team | Elversberg |
| Legacy model away team | Mainz |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 55.8% |
| Market home draw odds | 1.73 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-29T11:57:10Z |
| Market reference home draw last update utc | 2026-10-29T11:57:10Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.9% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-29T11:57:10Z |
| Market reference draw away last update utc | 2026-10-29T11:57:10Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-29T11:57:10Z |
| Market reference home away last update utc | 2026-10-29T11:57:10Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.73 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.28 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:57:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.02, "price": 1.78, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:57:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.02, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:57:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.64, "price": 2.21, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T11:57:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.21, "price": 1.64, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 86.7% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-29T11:56:41Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 56.3% |
| Market under 3 5 odds | 1.73 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-29T11:57:03Z |
| Market reference under 3 5 odds | 1.73 |
| Market reference under 3 5 opposite odds | 2.20 |
| Market reference under 3 5 last update utc | 2026-10-29T11:57:03Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.4% |
| Market btts yes odds | 1.43 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-29T11:57:10Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 2.96 |
| Market reference btts yes last update utc | 2026-10-29T11:57:10Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.09333149511901, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,430.0448 |
| Elo away rating | 1,516.7168 |
| Elo rating diff | -26.6720 |
| Elo home expectancy | 0.4617 |

</details>


---

## 2026-10-31 — Augsburg vs SC Freiburg

The model's most likely 1X2 outcome is **SC Freiburg win** at **41.6%**. Expected goals are 1.51 for Augsburg and 1.46 for SC Freiburg (2.97 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.3%; Under 3.5 goals: 65.4%; Double Chance 1X: 58.4%; Double Chance X2: 66.9%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 33.1% | 3.02 |
| Draw | 25.3% | 3.95 |
| SC Freiburg win | 41.6% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.51 |
| SC Freiburg expected goals | 1.46 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.3% |
| Under 2.5 | 42.7% |
| Over 3.5 | 34.6% |
| Under 3.5 | 65.4% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.77% |
| 2 | 1-2 | 9.60% |
| 3 | 0-1 | 7.74% |
| 4 | 2-1 | 7.41% |
| 5 | 0-2 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 33.1% | 30.9% | 3.12 | +3.3% |
| Draw | 25.3% | 25.0% | 3.84 | -2.9% |
| SC Freiburg win | 41.6% | 44.1% | 2.21 | -8.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 24400b6372faf9f4996cd5704d707374 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:57:03Z |
| Market best draw last update utc | 2026-10-29T11:57:03Z |
| Market best away last update utc | 2026-10-29T11:57:03Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Augsburg |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5009 |
| Dc lambda away | 1.4609 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:57:09.762880+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.5703 |
| Shot lambda away | 1.4329 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.30 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.12 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.53 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.21591055013001048, "-10": 8.572644063568062e-07, "-11": 1.1157710954650646e-07, "-12": 1.334477715649558e-08, "-13": 1.4755209402419862e-09, "-14": 1.5048343843740692e-10, "-15": 1.2729016817197027e-11, "-2": 0.1248544614338071, "-3": 0.0519191405109677, "-4": 0.01712508229039835, "-5": 0.004658526271136246, "-6": 0.00107553961107251, "-7": 0.00021537030777486204, "-8": 3.804074739340126e-05, "-9": 6.006838022309786e-06, "0": 0.2529709957071405, "1": 0.1670198933177292, "10": 9.496489105752629e-07, "11": 1.2865803437321228e-07, "12": 1.6017202066182402e-08, "13": 1.8434621667059469e-09, "14": 1.9570011501648271e-10, "15": 1.7231010948571325e-11, "2": 0.10035618936511674, "3": 0.043439129563197454, "4": 0.014914194760106718, "5": 0.004223079092238985, "6": 0.0010148937992551343, "7": 0.00021154050719610697, "8": 3.8892895507887794e-05, "9": 6.392646361439595e-06} |
| Raw goal margin distribution | {"-1": 0.18505494901108233, "-10": 7.347534472578983e-07, "-11": 9.56317155669307e-08, "-12": 1.1437685906374312e-08, "-13": 1.264655442713876e-09, "-14": 1.289779726385681e-10, "-15": 1.0909923376366743e-11, "-2": 0.1070116118944937, "-3": 0.044499418366406605, "-4": 0.014677750708114973, "-5": 0.003992780070509766, "-6": 0.0009218351199910076, "-7": 0.0001845919122515287, "-8": 3.260437512196796e-05, "-9": 5.148405685905672e-06, "0": 0.2609371189735839, "1": 0.1929665320184428, "10": 1.0971774276025642e-06, "11": 1.486451357149384e-07, "12": 1.850548383161832e-08, "13": 2.1298450989891197e-09, "14": 2.2610224303341976e-10, "15": 1.9907858638086417e-11, "2": 0.11594658243214831, "3": 0.05018742390024175, "4": 0.01723112369153891, "5": 0.004879136914060328, "6": 0.0011725581481286723, "7": 0.00024440344945856897, "8": 4.493492970945467e-05, "9": 7.385747735095532e-06} |
| Unadjusted home-win probability | 38.3% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 35.6% |
| Raw p over 1 5 | 80.5% |
| Raw p under 3 5 | 65.4% |
| Raw p btts yes | 60.6% |
| P home draw | 58.4% |
| P draw away | 66.9% |
| P home away | 74.7% |
| Raw p home draw | 64.4% |
| Raw p draw away | 61.7% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5727 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.12 |
| Reference draw odds | 3.84 |
| Reference away odds | 2.21 |
| Market reference 1x2 last update utc | 2026-10-29T11:57:03Z |
| Market reference home last update utc | 2026-10-29T11:57:03Z |
| Market reference draw last update utc | 2026-10-29T11:57:03Z |
| Market reference away last update utc | 2026-10-29T11:57:03Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Market reference over 2 5 last update utc | 2026-10-29T11:56:21Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:56:21Z |
| Home probability edge | +2.2% |
| Draw probability edge | +0.3% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | 0.0735 |
| Raw ev home | 0.1940 |
| Raw edge prob draw | 0.0114 |
| Raw ev draw | 0.0020 |
| Raw edge prob away | -0.0849 |
| Raw ev away | -0.2124 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.07013685640406088, 0.08046951491571554, 0.06796845510756835, 0.032478623126783755, 0.011639895579598731, 0.0033372638630664495, 0.0007973532362301729, 0.00016329172881400514, 2.9260764303147855e-05, 4.66073727240842e-06, 6.681378697983013e-07, 8.707327285697692e-08, 1.0401957823896703e-08, 1.1470522524299032e-09, 1.1745368102149885e-10], [0.06626349447751498, 0.125344018517429, 0.09283282762251348, 0.04436002579981495, 0.015898028257002764, 0.004558109205815886, 0.0010890427833921245, 0.00022302747486583374, 3.996500265245328e-05, 6.365738622697284e-06, 9.125575621352099e-07, 1.1892661260090547e-07, 1.4207225338198582e-08, 1.566669477117244e-09, 1.6042084974040207e-10], [0.05380119916115095, 0.07712646411744689, 0.05523261512456608, 0.030293954908105002, 0.010856940284904661, 0.003112783463434794, 0.0007437194270796798, 0.00015230794268118473, 2.7292544727527346e-05, 4.347233693303634e-06, 6.231957069441021e-07, 8.121630622497369e-08, 9.702272169699015e-09, 1.0698960074971874e-09, 1.0955318218899463e-10], [0.02449429145578003, 0.035113680001590694, 0.025168528052342595, 0.012015967446660296, 0.00494288350079157, 0.0014171696278316406, 0.00033859617800804644, 6.934185849443007e-05, 1.2425588194113892e-05, 1.9791828206508758e-06, 2.8372485219441283e-07, 3.697567910480437e-08, 4.417193036833178e-09, 4.870959206042148e-10, 4.987672424192113e-11], [0.008363712007472247, 0.011989761270948744, 0.008593933842169034, 0.004106598244650121, 0.0014704301753843136, 0.00048390044898087895, 0.00011561554759820766, 2.3677163128286822e-05, 4.242786175980294e-06, 6.758029784998886e-07, 9.687942831090679e-08, 1.2625551217580405e-08, 1.5082751223149407e-09, 1.6632161037615463e-10, 1.703068481032138e-11], [0.0022846687741989347, 0.0032751765198710103, 0.0023475571946037286, 0.0011217766428770024, 0.00040202944982459135, 0.0001151622241470274, 3.158205724605855e-05, 6.467759197409307e-06, 1.158978343970346e-06, 1.8460534761478071e-07, 2.6464015562279925e-08, 3.448851729720562e-09, 4.1200714129986846e-10, 4.5433150897758584e-11, 4.652177616183239e-12], [0.0005200752372407826, 0.000745551488606742, 0.0005343909711148053, 0.0002553579145755971, 9.151679396879605e-05, 2.6238696669329517e-05, 6.263443860637532e-06, 1.4723015594189619e-06, 2.6382639969710675e-07, 4.2023014907418e-08, 6.024190170289461e-09, 7.850863993060047e-10, 9.378808612270551e-11, 1.03422679902617e-11, 1.0590079423093143e-12], [0.00010147576080509344, 0.00014547011491476268, 0.00010426901047807707, 4.9824788422225594e-05, 1.78565246515035e-05, 5.11962792379897e-06, 1.223203217016403e-06, 2.502780457587822e-07, 5.1477137753701165e-08, 8.199424051946826e-09, 1.1754247020256933e-09, 1.531840663861951e-10, 1.8299693414068324e-11, 2.0179570908431494e-12, 2.06630942889367e-13], [1.7324731369452754e-05, 2.483578978059937e-05, 1.7801616685200235e-05, 8.50647551795986e-06, 3.048604812862671e-06, 8.740627100271445e-07, 2.0883476977090976e-07, 4.2767733349391734e-08, 7.656819818162364e-09, 1.3998694659412536e-09, 2.0067764997325392e-10, 2.6152775590602318e-11, 3.124266031875507e-12, 3.4452133432228606e-13, 3.5277642165707545e-14], [2.629167045672429e-06, 3.7690304485490287e-06, 2.7015382201507304e-06, 1.2909259387463636e-06, 4.6265025057702117e-07, 1.3264603208257964e-07, 3.1692352566018924e-08, 6.490346819379184e-09, 1.163025891800414e-09, 1.850840757212538e-10, 3.0454444162000986e-11, 3.9688936162621646e-12, 4.741324478718492e-13, 5.228387785154213e-14, 5.353665361567575e-15], [3.59097482435677e-07, 5.147825610872177e-07, 3.6898209840134856e-07, 1.7631753576774774e-07, 6.318980017032459e-08, 1.8117090070157163e-08, 4.328611998105501e-09, 8.864660032954975e-10, 1.5884866290274924e-10, 2.530186416844338e-11, 3.6238874465231866e-12, 5.420803170345014e-13, 6.475806421356569e-14, 7.14104831770451e-15, 7.312155217776642e-16], [4.45875752667795e-08, 6.39183155304166e-08, 4.581490511427163e-08, 2.189258288188009e-08, 7.846003130060321e-09, 2.249520413340274e-09, 5.374649578635938e-10, 1.1006863477651682e-10, 1.9723548784478858e-11, 3.141622618316125e-12, 4.50365880166257e-13, 5.864013700591614e-14, 8.040727667230314e-15, 8.866729646493481e-16, 9.079185655204098e-17], [5.07489182824593e-09, 7.275088075987799e-09, 5.214584695066631e-09, 2.4917813830802376e-09, 8.930204643534789e-10, 2.560370842062507e-10, 6.117346606786014e-11, 1.2527849111133712e-11, 2.2449051322362127e-12, 3.5757483688519617e-13, 5.125997794904549e-14, 6.680318910747075e-15, 7.973300464563217e-16, 1.0091980458013773e-16, 1.033379474282656e-17], [5.331846250744697e-10, 7.643443918527843e-10, 5.478612115598838e-10, 2.617946485303482e-10, 9.382363163289562e-11, 2.690008799554154e-11, 6.4270831130545195e-12, 1.3162165337459206e-12, 2.3585702745369206e-13, 3.756797421366808e-14, 5.385539839877536e-15, 7.018560107981006e-16, 8.384520741240578e-17, 9.237555735028454e-18, 1.0857020527775274e-18], [5.201681564965631e-11, 7.45684692582834e-11, 5.344864480915504e-11, 2.5540353810404246e-11, 9.153314481916936e-12, 2.6243384606751992e-12, 6.270180754182144e-13, 1.2840841534267544e-13, 2.300991240139583e-14, 3.665083907343497e-15, 5.254064349392344e-16, 6.847218207237107e-17, 8.179832073119436e-18, 9.020123867850044e-19, 9.22798003938449e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3658222402671092, "lambda_away": 1.4335454473129803, "rho": -0.11084550577255979, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3271 |
| Legacy p draw | 0.2643 |
| Legacy p away | 0.4085 |
| Legacy p over 1 5 | 0.7831 |
| Legacy p under 3 5 | 0.6909 |
| Legacy p btts yes | 0.5771 |
| Legacy p over 2 5 | 0.5360 |
| Legacy goal margin distribution | {"-1": 0.20905618866292386, "-10": 7.972708811743203e-07, "-11": 1.024002709269146e-07, "-12": 1.2078180483202942e-08, "-13": 1.3074731021703052e-09, "-14": 1.1745368102149885e-10, "-2": 0.12472494635745117, "-3": 0.05185291039177537, "-4": 0.01701549964306384, "-5": 0.0045917432480639024, "-6": 0.0010497528627655462, "-7": 0.00020790073811921425, "-8": 3.62882290791752e-05, "-9": 5.659099307593429e-06, "0": 0.26432157145974117, "1": 0.17309462019818378, "10": 4.285013306241725e-07, "11": 5.243606490813759e-08, "12": 5.89268486490787e-09, "13": 6.07753094332753e-10, "14": 5.201681564965631e-11, "2": 0.09872744155683913, "3": 0.03910573102217478, "4": 0.012226289978688866, "5": 0.00314347706637469, "6": 0.0006847033966127681, "7": 0.00012919751493731707, "8": 2.1485557046855432e-05, "9": 3.1923527412270918e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3451 |
| Legacy raw p draw | 0.2791 |
| Legacy raw p away | 0.3758 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3658 |
| Legacy lambda away | 1.4335 |
| Legacy model home team | Augsburg |
| Legacy model away team | Freiburg |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 9.85969265539543, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,473.6758 |
| Elo away rating | 1,485.3747 |
| Elo rating diff | 48.3011 |
| Elo home expectancy | 0.5691 |

</details>


---

## 2026-10-31 — Bayer Leverkusen vs VfB Stuttgart

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **53.4%**. Expected goals are 2.13 for Bayer Leverkusen and 1.42 for VfB Stuttgart (3.54 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.9%; Under 3.5 goals: 52.7%; Double Chance 1X: 74.8%; Double Chance X2: 46.6%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 71.6%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 53.4% | 1.87 |
| Draw | 21.5% | 4.66 |
| VfB Stuttgart win | 25.2% | 3.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.13 |
| VfB Stuttgart expected goals | 1.42 |
| Expected total goals | 3.54 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 87.5% |
| Under 1.5 | 12.5% |
| Over 2.5 | 68.9% |
| Under 2.5 | 31.1% |
| Over 3.5 | 47.3% |
| Under 3.5 | 52.7% |
| Over 4.5 | 28.4% |
| Under 4.5 | 71.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.30% |
| 2 | 1-1 | 9.08% |
| 3 | 3-1 | 6.59% |
| 4 | 2-0 | 6.57% |
| 5 | 2-2 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 53.4% | 53.5% | 1.83 | -2.3% |
| Draw | 21.5% | 21.2% | 4.47 | -4.0% |
| VfB Stuttgart win | 25.2% | 25.3% | 3.76 | -5.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | a7ba9b844f121a4a8777d87b1f863137 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:57:03Z |
| Market best draw last update utc | 2026-10-29T11:57:03Z |
| Market best away last update utc | 2026-10-29T11:57:03Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Leverkusen |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1729 |
| Dc lambda away | 1.3808 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:57:09.762880+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9414 |
| Shot lambda away | 1.5542 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 67.2% |
| P btts no | 32.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.12 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.01 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.22 |
| Fair Over 3.5 odds | 2.12 |
| Fair Under 3.5 odds | 1.90 |
| Fair Over 4.5 odds | 3.52 |
| Fair Under 4.5 odds | 1.40 |
| Goal margin distribution | {"-1": 0.13879103251361014, "-10": 3.440138980801125e-07, "-11": 4.329925838950356e-08, "-12": 5.0123352269829416e-09, "-13": 5.370068269944376e-10, "-14": 5.3535130622917857e-11, "-15": 4.986214128893094e-12, "-16": 4.309727811840069e-13, "-17": 3.048647825127132e-14, "-2": 0.07289430853751375, "-3": 0.02817990400170233, "-4": 0.008766060687611975, "-5": 0.0022685630384074, "-6": 0.0005010444875892298, "-7": 9.634105292357201e-05, "-8": 1.6382984617900847e-05, "-9": 2.4953893662695653e-06, "0": 0.2146687139298568, "1": 0.20864441080835183, "10": 1.9854293250440004e-05, "11": 3.7543890597666095e-06, "12": 6.529490593427697e-07, "13": 1.0509919079728941e-07, "14": 1.574123511736225e-08, "15": 2.2026791347772763e-09, "16": 2.8602930387189666e-10, "17": 3.039823154967896e-11, "2": 0.16207986789998918, "3": 0.09413591243954646, "4": 0.043994731744368916, "5": 0.01710517125589022, "6": 0.005675880419338017, "7": 0.0016396407786515022, "8": 0.0004189003466299432, "9": 9.585977165088225e-05} |
| Raw goal margin distribution | {"-1": 0.13624594287392747, "-10": 3.3770552071556854e-07, "-11": 4.250525540575704e-08, "-12": 4.920421201805848e-09, "-13": 5.271594291685848e-10, "-14": 5.2553426662367766e-11, "-15": 4.8947791010613016e-12, "-16": 4.230697896109089e-13, "-17": 2.992743046163756e-14, "-2": 0.07155760438530229, "-3": 0.027663153168286984, "-4": 0.008605312476197937, "-5": 0.002226963115260698, "-6": 0.0004918565515152013, "-7": 9.457439256208316e-05, "-8": 1.60825605655471e-05, "-9": 2.4496300004946607e-06, "0": 0.22113681765190749, "1": 0.20791902100675685, "10": 1.978526623080431e-05, "11": 3.741336251284353e-06, "12": 6.506789645591458e-07, "13": 1.0473379456709627e-07, "14": 1.5686507883719107e-08, "15": 2.1950211247957816e-09, "16": 2.850348715783014e-10, "17": 3.029254663309178e-11, "2": 0.16151636810259218, "3": 0.09380863201740175, "4": 0.04384177615065024, "5": 0.01704570205307052, "6": 0.005656147200723106, "7": 0.001633940272730902, "8": 0.00041744396427034546, "9": 9.5526497922296e-05} |
| Unadjusted home-win probability | 53.2% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 52.8% |
| Raw p btts yes | 67.3% |
| P home draw | 74.8% |
| P draw away | 46.6% |
| P home away | 78.5% |
| Raw p home draw | 75.3% |
| Raw p draw away | 46.8% |
| Raw p home away | 77.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6890 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.49, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.83 |
| Reference draw odds | 4.47 |
| Reference away odds | 3.76 |
| Market reference 1x2 last update utc | 2026-10-29T11:57:03Z |
| Market reference home last update utc | 2026-10-29T11:57:03Z |
| Market reference draw last update utc | 2026-10-29T11:57:03Z |
| Market reference away last update utc | 2026-10-29T11:57:03Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.57 |
| Market reference over 2 5 last update utc | 2026-10-29T11:56:21Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:56:21Z |
| Home probability edge | -0.1% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | -0.0027 |
| Raw ev home | -0.0265 |
| Raw edge prob draw | 0.0092 |
| Raw ev draw | -0.0115 |
| Raw edge prob away | -0.0066 |
| Raw ev away | -0.0716 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.038635523344487714, 0.0320096893374896, 0.026478227043494913, 0.010892769455740218, 0.003360848884094485, 0.0008295635204703107, 0.00017063537076201853, 3.0084422921501495e-05, 4.641115357080869e-06, 6.364298173380097e-07, 7.854547734975645e-08, 8.812500671759791e-09, 9.063346460881965e-10, 8.604306939002039e-11, 7.585051321521334e-12, 6.240766439502825e-13, 4.813806307321689e-14, 3.4947036622231058e-15, 2.396119727993641e-16], [0.054963917408415844, 0.09240960531287223, 0.06067656384729758, 0.024961483269609282, 0.007701601831644445, 0.0019009982742621708, 0.0003910219499078035, 6.894039412861866e-05, 1.0635414970345416e-05, 1.4584199456632737e-06, 1.799920237673099e-07, 2.0194413273442804e-08, 2.0769242566752177e-09, 1.971732391630677e-10, 1.7381633975692767e-11, 1.430111852657428e-12, 1.1031147413115292e-13, 8.008338682946671e-15, 5.490862791626904e-16], [0.07295729923219148, 0.09004081421436666, 0.05881745152091005, 0.028600423866064602, 0.008824358490782044, 0.002178130034393843, 0.0004480260001982369, 7.899067824918193e-05, 1.2185869439646044e-05, 1.6710316518520509e-06, 2.0623166166264502e-07, 2.313839979413955e-08, 2.379702898142405e-09, 2.259175928849734e-10, 1.9915567268987216e-11, 1.6385967420326937e-12, 1.263929263884156e-13, 9.17581212307747e-15, 6.2913329923038e-16], [0.055728784480379615, 0.06877810969702497, 0.042441517589186226, 0.01848274344663807, 0.0067405287433311796, 0.0016637751196170506, 0.000342226818555768, 6.033741010749092e-05, 9.308235075242929e-06, 1.2764255772349874e-06, 1.5753104825400332e-07, 1.7674378148848727e-08, 1.8177475226412563e-09, 1.7256824165247608e-10, 1.521260199895359e-11, 1.251650015118703e-12, 9.65458457025304e-14, 7.008988293440133e-15, 4.805665013812611e-16], [0.03192652536838545, 0.03940236781594895, 0.02431436825005557, 0.010002588442751974, 0.003267000448343945, 0.0009531619800974433, 0.00019605870298874573, 3.456676603340772e-05, 5.332605152535964e-06, 7.312528696332202e-07, 9.024813756992118e-08, 1.0125494169683935e-08, 1.0413714014408114e-09, 9.886281203271487e-11, 8.71516449115695e-12, 7.170591702766509e-13, 5.531025700227273e-14, 4.015387104594332e-15, 2.75312277857896e-16], [0.014632338122601979, 0.018058613083057576, 0.011143588391381003, 0.004584315220863613, 0.0014144420073315361, 0.00036958294933804456, 8.985623085846002e-05, 1.5842394453188607e-05, 2.4440016809189558e-06, 3.3514261630837053e-07, 4.1361884784550436e-08, 4.640644499822777e-09, 4.772739369934267e-10, 4.5310101137607224e-11, 3.994272228414184e-12, 3.28637460930531e-13, 2.5349403756497673e-14, 1.8403036700555083e-15, 1.2617916583273347e-16], [0.005588490982124542, 0.006897079299203447, 0.004256041837739213, 0.0017508756328859928, 0.0005402141705911316, 0.00013334189801999122, 2.9034353997973137e-05, 6.0506446608247695e-06, 9.334312288078838e-07, 1.2800015098556926e-07, 1.579723747396772e-08, 1.7723893284317934e-09, 1.8228399798736627e-10, 1.730516951460668e-11, 1.5255220417687961e-12, 1.2551565384903708e-13, 9.68163208835348e-15, 7.028624118923157e-16, 4.8191281836155075e-17], [0.001829483896496295, 0.0022578716779021644, 0.001393284883140009, 0.000573177765765123, 0.0001768479414061534, 4.365165049672951e-05, 8.9788369221692e-06, 1.6757870464213812e-06, 3.0557397462983244e-07, 4.1902942265850935e-08, 5.171483976657455e-09, 5.802206257573928e-10, 5.967364713901184e-11, 5.665130185300168e-12, 4.99404583114341e-13, 4.108960150593639e-14, 3.169440561700768e-15, 2.30093502543453e-16, 1.5776204050926625e-17], [0.0005240475328607395, 0.000646757309308278, 0.0003991002637301237, 0.00016418422409461854, 5.0657306994001746e-05, 1.2503821319181918e-05, 2.5719479389969115e-06, 4.53455629880989e-07, 7.405281915796245e-08, 1.2002911616811634e-08, 1.4813486056840367e-09, 1.6620162004453696e-10, 1.7093251063806133e-11, 1.6227513686384994e-12, 1.4305222373458946e-13, 1.176993377020441e-14, 9.078721655265511e-16, 6.590926138574352e-17, 4.5190235490069234e-18], [0.0001334320775011397, 0.00016467622879351218, 0.00010161821968717207, 4.1804303503284145e-05, 1.2898275994019205e-05, 3.183701383372123e-06, 6.548649410707735e-07, 1.1545808911514711e-07, 1.781168652926172e-08, 2.58558797432638e-09, 3.7717842288242135e-10, 4.231796937490945e-11, 4.352254056500472e-12, 4.131821501062056e-13, 3.642371007810184e-14, 2.9968402034754703e-15, 2.3116084239606155e-16, 1.6781702272802097e-17, 1.150625969230169e-18], [3.057682055704142e-05, 3.773661920078034e-05, 2.3286469992001247e-05, 9.579725585259655e-06, 2.955723076116773e-06, 7.295656916212105e-07, 1.5006652198791943e-07, 2.6457965272275674e-08, 4.0816627682264465e-09, 5.597128470539864e-10, 7.312435706956459e-11, 9.697435430426603e-12, 9.973470682350269e-13, 9.468335274223766e-14, 8.346727922828814e-15, 6.867452478884941e-16, 5.297199691504867e-17, 3.845635237394704e-18, 2.6367335687419116e-19], [6.369886822410561e-06, 7.861445009331432e-06, 4.851131531670935e-06, 1.995687146543505e-06, 6.157481755870557e-07, 1.5198607312592534e-07, 3.126246429423808e-08, 5.511830244785013e-09, 8.503084822814277e-10, 1.166016421534725e-10, 1.4390481704671388e-11, 1.7091470581974826e-12, 2.0777137163324517e-13, 1.972481866809202e-14, 1.7388240908399394e-15, 1.4306554524586136e-16, 1.1035340462441797e-17, 8.011382732478729e-19, 5.492949923424545e-20], [1.2164171838405168e-06, 1.50125066045509e-06, 9.263900475333678e-07, 3.8110381020969115e-07, 1.1758555255132388e-07, 2.902382353237059e-08, 5.969995988456316e-09, 1.0525595212429715e-09, 1.6237805760904494e-10, 2.2266681517872166e-11, 2.7480596935756054e-12, 3.0832173554479165e-13, 3.356755283974904e-14, 3.7667244403135925e-15, 3.320522895841867e-16, 2.7320326483716294e-17, 2.107349493372139e-18, 1.5298833234877547e-19, 1.0489540651368276e-20], [2.1442295210791954e-07, 2.6463174209067125e-07, 1.6329865397687772e-07, 6.717876492564589e-08, 2.0727297869709663e-08, 5.116150943890437e-09, 1.0523561989445503e-09, 1.8553907558396242e-10, 2.8623060355127422e-11, 3.92504121787791e-12, 4.844119927711591e-13, 5.434916376783055e-14, 5.589620011781464e-15, 5.617404762185793e-16, 5.853224792668664e-17, 4.815868383818124e-18, 3.7147132208815137e-19, 2.6967894153485487e-20, 1.8490352673423797e-21], [3.509742962594007e-08, 4.331576379072814e-08, 2.6729242180564685e-08, 1.0996033545647393e-08, 3.3927099275822523e-09, 8.374278310397791e-10, 1.7225300403143723e-10, 3.0369625005874466e-11, 4.685113401421246e-12, 6.42463209134672e-13, 7.929009305724973e-14, 8.896043692235276e-15, 9.149267514072271e-16, 8.685876270745291e-17, 8.105548116925398e-18, 7.882766281651413e-19, 6.080360547634803e-20, 4.41419054213646e-21, 3.0265596352189004e-22], [5.361868139373983e-09, 6.617390967870162e-09, 4.083452080822919e-09, 1.6798746391478827e-09, 5.183075644205055e-10, 1.2793465658689193e-10, 2.6315257386968356e-11, 4.639596872455361e-12, 7.157492883144942e-13, 9.814972345533677e-14, 1.2113223910204743e-14, 1.3590571659589904e-15, 1.3977424131952946e-16, 1.3269496864873692e-17, 1.169760858653273e-18, 1.0188320810618807e-19, 9.28902539124227e-21, 6.74360142074749e-22, 4.623704314803054e-23], [7.679416515621746e-10, 9.47761119222925e-10, 5.848433518897153e-10, 2.4059631294014905e-10, 7.423344936728015e-11, 1.8323156951570996e-11, 3.768944273476971e-12, 6.644959540597834e-13, 1.0251160160698353e-13, 1.4057276078307688e-14, 1.734889582053602e-15, 1.9464794311704364e-16, 2.0018855170373805e-17, 1.9004942070432833e-18, 1.67536400071163e-19, 1.378442278950231e-20, 1.1255515432632464e-21, 9.658373309289336e-23, 6.622197777992301e-24], [1.0351692882357662e-10, 1.2775621705213586e-10, 7.883566089605189e-11, 3.243187988459294e-11, 1.0006513748602382e-11, 2.469923242372056e-12, 5.080458070009435e-13, 8.957266511073219e-14, 1.3818349539387898e-14, 1.8948914208408828e-15, 2.3385948791405954e-16, 2.623813571293346e-17, 2.698499816471142e-18, 2.561826450745538e-19, 2.2583556402033125e-20, 1.8581113680607162e-21, 1.4332515581194197e-22, 1.1014639471784203e-23, 8.92658413104157e-25], [1.3178650793436724e-11, 1.6264533640580166e-11, 1.0036499892587963e-11, 4.128874614336418e-12, 1.2739206219815857e-12, 3.14443794534221e-13, 6.467887285321273e-14, 1.1403418624828238e-14, 1.7592021439469546e-15, 2.412369900318526e-16, 2.977244940490732e-17, 3.340354393829318e-18, 3.4354368074458053e-19, 3.2614391260877035e-20, 2.8750930584842842e-21, 2.365545532820135e-22, 1.8246601786067458e-23, 1.3246579113062625e-24, 9.614529090052894e-26]] |
| Legacy trial inputs | {"lambda_home": 2.2915644520921354, "lambda_away": 1.2341577218724304, "rho": -0.11084550577255979, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5682 |
| Legacy p draw | 0.2120 |
| Legacy p away | 0.2198 |
| Legacy p over 1 5 | 0.8744 |
| Legacy p under 3 5 | 0.5348 |
| Legacy p btts yes | 0.6493 |
| Legacy p over 2 5 | 0.6825 |
| Legacy goal margin distribution | {"-1": 0.12907659261377338, "-10": 1.0130121548119084e-07, "-11": 1.1131298250531585e-08, "-12": 1.1247323012873244e-09, "-13": 1.0516398751971879e-10, "-14": 9.148840401138477e-12, "-15": 7.440444967058941e-13, "-16": 5.677553505539394e-14, "-17": 4.043789941385796e-15, "-18": 2.396119727993641e-16, "-2": 0.06214072187980028, "-3": 0.021151872250333888, "-4": 0.005775894711404253, "-5": 0.0013096588321798055, "-6": 0.000253133136784819, "-7": 4.255902117663874e-05, "-8": 6.324529591594775e-06, "-9": 8.414809742585158e-07, "0": 0.21201269387690921, "1": 0.19900607223872815, "10": 3.943535888369218e-05, "11": 8.045969320558773e-06, "12": 1.509534810802383e-06, "13": 2.6207308524995385e-07, "14": 4.233336974620653e-08, "15": 6.392593794107296e-09, "16": 9.057343685068984e-10, "17": 1.197814624641568e-10, "18": 1.3178650793436724e-11, "2": 0.17122064982831936, "3": 0.10821565027929583, "4": 0.05486835480806074, "5": 0.02310054671502734, "6": 0.008290381096729445, "7": 0.0025880850065319915, "8": 0.0007141287974933288, "9": 0.00017642252376331435} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6018 |
| Legacy raw p draw | 0.2121 |
| Legacy raw p away | 0.1860 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2916 |
| Legacy lambda away | 1.2342 |
| Legacy model home team | Leverkusen |
| Legacy model away team | Stuttgart |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.79589043379434, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,573.7454 |
| Elo away rating | 1,532.5206 |
| Elo rating diff | 101.2247 |
| Elo home expectancy | 0.6417 |

</details>


---

## 2026-10-31 — Bayern Munich vs Borussia Dortmund

The model's most likely 1X2 outcome is **Bayern Munich win** at **70.1%**. Expected goals are 2.52 for Bayern Munich and 1.24 for Borussia Dortmund (3.76 combined). The most likely exact score is 2-1 at 9.9%. Goal-market probabilities: at least one goal: 97.4%; Over 2.5 goals: 73.2%; Under 3.5 goals: 47.5%; Double Chance 1X: 87.2%; Double Chance X2: 29.9%; Double Chance 12 (either team wins): 82.8%; Under 4.5 goals: 66.9%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 70.1% | 1.43 |
| Draw | 17.2% | 5.83 |
| Borussia Dortmund win | 12.8% | 7.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.52 |
| Borussia Dortmund expected goals | 1.24 |
| Expected total goals | 3.76 |
| Over 0.5 | 97.4% |
| Under 0.5 | 2.6% |
| Over 1.5 | 89.8% |
| Under 1.5 | 10.2% |
| Over 2.5 | 73.2% |
| Under 2.5 | 26.8% |
| Over 3.5 | 52.5% |
| Under 3.5 | 47.5% |
| Over 4.5 | 33.1% |
| Under 4.5 | 66.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.93% |
| 2 | 3-1 | 8.34% |
| 3 | 2-0 | 8.03% |
| 4 | 1-1 | 7.15% |
| 5 | 3-0 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 70.1% | 72.4% | 1.36 | -4.7% |
| Draw | 17.2% | 16.5% | 5.56 | -4.6% |
| Borussia Dortmund win | 12.8% | 11.2% | 8.04 | +2.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:30:00+00:00 |
| Fixture id | bad7337b335a16859b1db6b8e6cf6ca5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:57:03Z |
| Market best draw last update utc | 2026-10-29T11:57:03Z |
| Market best away last update utc | 2026-10-29T11:57:03Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Bayern Munich |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5383 |
| Dc lambda away | 1.2791 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:57:09.762880+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 2.4430 |
| Shot lambda away | 1.0662 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 38.06 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.76 |
| Fair Over 2.5 odds | 1.37 |
| Fair Under 2.5 odds | 3.73 |
| Fair Over 3.5 odds | 1.91 |
| Fair Under 3.5 odds | 2.10 |
| Fair Over 4.5 odds | 3.02 |
| Fair Under 4.5 odds | 1.49 |
| Goal margin distribution | {"-1": 0.07667836167218504, "-10": 5.5130694755774525e-08, "-11": 6.057100144961681e-09, "-12": 6.12123213860177e-10, "-13": 5.725739766835998e-11, "-14": 4.984132442126402e-12, "-15": 4.0564504964070984e-13, "-16": 3.097563051451408e-14, "-17": 2.2041365642306943e-15, "-18": 1.2907604958493402e-16, "-2": 0.03511854107655778, "-3": 0.011793935274819747, "-4": 0.003192567268689052, "-5": 0.0007197166595301415, "-6": 0.0001385674001767623, "-7": 2.3236670169294522e-05, "-8": 3.4472861563379727e-06, "-9": 4.5819432071272434e-07, "0": 0.17151994971617343, "1": 0.22455051737846277, "10": 9.503871837104339e-05, "11": 2.127391435541763e-05, "12": 4.380231348230222e-06, "13": 8.347671526219404e-07, "14": 1.4804674627804424e-07, "15": 2.45488425256161e-08, "16": 3.819271584918502e-09, "17": 5.536998838221348e-10, "18": 6.606282562676934e-11, "2": 0.20391031561894438, "3": 0.1395201767982197, "4": 0.07694738787912678, "5": 0.03534198409361092, "6": 0.013863279750772181, "7": 0.004736465285520496, "8": 0.001431638428289786, "9": 0.0003876870198254077} |
| Raw goal margin distribution | {"-1": 0.09907941182742115, "-10": 7.123674385991321e-08, "-11": 7.826639832346448e-09, "-12": 7.909507541966346e-10, "-13": 7.39847482397077e-11, "-14": 6.4402120763488655e-12, "-15": 5.241514301118125e-13, "-16": 4.0024945570464185e-14, "-17": 2.8480597343084435e-15, "-18": 1.6678471989994826e-16, "-2": 0.045378178644167176, "-3": 0.015239451452491063, "-4": 0.004125253595708103, "-5": 0.0009299768768339506, "-6": 0.00017904890256606438, "-7": 3.002510177570252e-05, "-8": 4.454386835115131e-06, "-9": 5.92052605309503e-07, "0": 0.18765250437088293, "1": 0.20743069254476293, "10": 8.779292695659148e-05, "11": 1.9651982277309603e-05, "12": 4.046280688537933e-06, "13": 7.711241577330553e-07, "14": 1.3675960077034734e-07, "15": 2.267722856179568e-08, "16": 3.528088730879782e-09, "17": 5.11485574400178e-10, "18": 6.102616832598316e-11, "2": 0.1883641083514852, "3": 0.12888310049379675, "4": 0.07108088702541845, "5": 0.03264749652786525, "6": 0.01280633753694604, "7": 0.004375355202294348, "8": 0.00132248971910999, "9": 0.000358129600197985} |
| Unadjusted home-win probability | 64.7% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 16.5% |
| Raw p over 1 5 | 89.4% |
| Raw p under 3 5 | 48.3% |
| Raw p btts yes | 65.8% |
| P home draw | 87.2% |
| P draw away | 29.9% |
| P home away | 82.8% |
| Raw p home draw | 83.5% |
| Raw p draw away | 35.3% |
| Raw p home away | 81.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7319 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.36 |
| Reference draw odds | 5.56 |
| Reference away odds | 8.04 |
| Market reference 1x2 last update utc | 2026-10-29T11:57:03Z |
| Market reference home last update utc | 2026-10-29T11:57:03Z |
| Market reference draw last update utc | 2026-10-29T11:57:03Z |
| Market reference away last update utc | 2026-10-29T11:57:03Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.02 |
| Market reference over 2 5 last update utc | 2026-10-29T11:56:21Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:56:21Z |
| Home probability edge | -2.3% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.0763 |
| Raw ev home | -0.1196 |
| Raw edge prob draw | 0.0230 |
| Raw ev draw | 0.0433 |
| Raw edge prob away | 0.0533 |
| Raw ev away | 0.3263 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.022464113103592163, 0.013425625917228295, 0.013266579805867281, 0.006115130055604646, 0.0021140423611906204, 0.0005846711437722991, 0.00013474988038535376, 2.661940397573347e-05, 4.601255175494568e-06, 7.069713075741724e-07, 9.776193008279978e-08, 1.228980694397045e-08, 1.4162234901608754e-09, 1.5064558908751457e-10, 1.4879774963862392e-11, 1.3717440430563257e-12, 1.185553287241256e-13, 9.643621054805274e-15, 7.408590837534558e-16, 5.3920012975106685e-17], [0.040553316587177306, 0.06605538449430018, 0.03594117807235976, 0.016566815372182332, 0.005727261590245024, 0.0015839628600279403, 0.00036505787603352595, 7.211600521551102e-05, 1.2465498571506623e-05, 1.915292564428308e-06, 2.6485190525515334e-07, 3.329495215133101e-08, 3.8367643654183935e-09, 4.081217632908922e-10, 4.031156857898668e-11, 3.7162627928700785e-12, 3.2118437784669013e-13, 2.6126032984011856e-14, 2.007099693014474e-15, 1.4607749822189897e-16], [0.06487688700645601, 0.08971353750236083, 0.05569239366784319, 0.022441008537866583, 0.007758010417686773, 0.0021455978875237606, 0.0004944985942584713, 9.768660134134935e-05, 1.688546371692281e-05, 2.594409113957922e-06, 3.5876200305105404e-07, 4.5100539162793495e-08, 5.1971884727290495e-09, 5.528318973046908e-10, 5.460507854604453e-11, 5.03395994886177e-12, 4.350686117737229e-13, 3.538969416169463e-14, 2.718768836098519e-15, 1.9787305593398428e-16], [0.0585871109409364, 0.08101586276837903, 0.05601547776200959, 0.023182202120700456, 0.007005875867267266, 0.0019375834333494497, 0.0004465572461742064, 8.821594275414506e-05, 1.5248427933573152e-05, 2.3428826751583134e-06, 3.239802377085856e-07, 4.072806839766663e-08, 4.693324104814593e-09, 4.992351697740246e-10, 4.9311148273765104e-11, 4.545920490402792e-12, 3.9288896556287907e-13, 3.195868411211972e-14, 2.455185795326674e-15, 1.7868937945608932e-16], [0.03968034372623358, 0.05487106686601311, 0.03793860758600172, 0.01748751546456196, 0.0054279522502345395, 0.0013123018936890614, 0.0003024478377077934, 5.974759421312187e-05, 1.0327576355469518e-05, 1.5868061825789976e-06, 2.1942790805547214e-07, 2.758462957755693e-08, 3.178731818426887e-09, 3.381259601079973e-10, 3.3397846072506736e-11, 3.0788971279563836e-12, 2.660989584466138e-13, 2.1645231352771022e-14, 1.662867731582524e-15, 1.2102416185350268e-16], [0.021500014633858706, 0.029730809509464405, 0.02055628912679995, 0.009475266670871665, 0.003275664612797791, 0.000813387179766296, 0.00016387541855887307, 3.2373060041582014e-05, 5.595794338547781e-06, 8.597797534699989e-07, 1.1889270079963227e-07, 1.4946189571310433e-08, 1.7223333821099795e-09, 1.8320690820032627e-10, 1.8095966714712033e-11, 1.668239916567151e-12, 1.441804924909052e-13, 1.1728043336735659e-14, 9.009922093885354e-16, 6.557456429442513e-17], [0.009707800425599091, 0.013424212500528143, 0.009281684488698936, 0.004278322567989995, 0.0014790454268882082, 0.00040905291081437474, 8.464399158433149e-05, 1.4617255448500649e-05, 2.5266426831063768e-06, 3.882123058424886e-07, 5.3683061666649116e-08, 6.748582638309177e-09, 7.776770864862408e-10, 8.272255306277523e-11, 8.170786688584678e-12, 7.532525185609794e-13, 6.510113924118246e-14, 5.295508214050606e-15, 4.068207721118973e-16, 2.960857441293957e-17], [0.003757129234222478, 0.005195461280719166, 0.0035922131282553663, 0.0016558035897855836, 0.0005724226465813258, 0.0001583123449377714, 3.648644160245671e-05, 6.4714465487578525e-06, 9.778654971213481e-07, 1.5024657897988465e-07, 2.0776508738114943e-08, 2.611847793357673e-09, 3.0097789286207996e-10, 3.201542149775837e-11, 3.162271594843059e-12, 2.915250555392949e-13, 2.5195552308559152e-14, 2.0494764878571317e-15, 1.5744845886613332e-16, 1.1459160225128117e-17], [0.0012723291611710069, 0.001759411636145607, 0.001216481316263924, 0.0005607279018422724, 0.00019384747778334718, 5.3611521052555424e-05, 1.23559134499071e-05, 2.4408708243129938e-06, 3.788111098517735e-07, 5.088009804428526e-08, 7.035839410059153e-09, 8.844865068147759e-10, 1.0192434864047893e-10, 1.0841829449928115e-11, 1.0708842083506898e-12, 9.872320227797585e-14, 8.532321870110855e-15, 6.940428550828382e-16, 5.33189712432854e-17, 3.8805755160505295e-18], [0.0003829925322582992, 0.0005296125706903891, 0.0003661813892027973, 0.00016878855377078865, 5.835135958040816e-05, 1.6137971865110475e-05, 3.7193383009385135e-06, 7.347432774854002e-07, 1.2700289274964448e-07, 1.7520197674321507e-08, 2.1179063047971093e-09, 2.6624535327125045e-10, 3.068094764775111e-11, 3.263573485589928e-12, 3.2235420457877087e-13, 2.971734861306726e-14, 2.5683727598202973e-15, 2.089186027295883e-16, 1.6049909439377112e-17, 1.1681186668266516e-18], [0.00010375848940502136, 0.00014348008296852138, 9.92040956200423e-05, 4.572738080517952e-05, 1.5808268869088833e-05, 4.372021493242349e-06, 1.0076251915829788e-06, 1.990531045680136e-07, 3.4407011082095325e-08, 5.286550883762585e-09, 6.563572926902861e-10, 7.212990682518088e-11, 8.311934341576752e-12, 8.841515862735295e-13, 8.733064617012703e-14, 8.05088073919606e-15, 6.958111590756352e-16, 5.659922009448038e-17, 4.3481640456478534e-18, 3.1646107458303954e-19], [2.5554317683266357e-05, 3.5337210886780394e-05, 2.4432631869378475e-05, 1.1262037666700101e-05, 3.8933635890388735e-06, 1.076769976095823e-06, 2.4816450585418265e-07, 4.902409720052546e-08, 8.473983158056457e-09, 1.3020062407142543e-09, 1.800449915129286e-10, 2.0321523219994682e-11, 2.047117416079348e-12, 2.1775462080603723e-13, 2.1508361277360244e-14, 1.9828234317909212e-15, 1.7136891167692793e-16, 1.39396251739327e-17, 1.0708942082580532e-18, 7.794009801661084e-20], [5.76921040069508e-06, 7.977822264965694e-06, 5.515975642326571e-06, 2.5425474334731334e-06, 8.789760693269875e-07, 2.43094439939442e-07, 5.6026275716014486e-08, 1.1067809947403244e-08, 1.9131088678132665e-09, 2.9394437522459605e-10, 4.064743385066488e-11, 5.109853236013099e-12, 5.28682675115514e-13, 4.9160859574671537e-14, 4.8557845731294555e-15, 4.476474663583316e-16, 3.8688699101902924e-17, 3.1470466764958874e-18, 2.4176791103963385e-19, 1.7595962830307526e-20], [1.2022820407051843e-06, 1.6625485581095475e-06, 1.1495088566950997e-06, 5.298574509498759e-07, 1.8317535138502674e-07, 5.0659979275372504e-08, 1.1675667972318306e-08, 2.3064905256528545e-09, 3.986847894139207e-10, 6.12569171088403e-11, 8.470774391157322e-12, 1.0648744541467314e-12, 1.22711465111723e-13, 1.1719516299104176e-14, 1.0119274875299165e-15, 9.328807098194192e-17, 8.06258133744967e-18, 6.558328501862382e-19, 5.038353557477118e-20, 3.66693336357535e-21], [2.3265460788638577e-07, 3.2172116839754184e-07, 2.2244242470715367e-07, 1.0253316053371179e-07, 3.544641615534577e-08, 9.803255155446817e-09, 2.259368319531811e-09, 4.463309195941105e-10, 7.714982858511067e-11, 1.1853877499431752e-11, 1.6391866698040473e-12, 2.0606475035793035e-13, 2.3745998719224412e-14, 2.525893681598639e-15, 2.2400356448037514e-16, 1.8052252998847804e-17, 1.5601968890063584e-18, 1.269107658878399e-19, 9.749760302668066e-21, 7.095913562409501e-22], [4.201977607773731e-08, 5.8106098040982725e-08, 4.017535247334551e-08, 1.8518526176250202e-08, 6.40198138836466e-09, 1.7705670659485099e-09, 4.0806477776800493e-10, 8.061187985184354e-11, 1.3934039609330552e-11, 2.1409302085359558e-12, 2.9605369711144476e-13, 3.721737878401917e-14, 4.288767619901651e-15, 4.562019547396086e-16, 4.5060611901859604e-17, 3.7296984852276646e-18, 2.817873435167233e-19, 2.292136834472399e-20, 1.760905354300089e-21, 1.281593782595674e-22], [7.11487190307482e-09, 9.838639872432195e-09, 6.802570436832407e-09, 3.1355936151112636e-09, 1.0839961978811283e-09, 2.9979593053331235e-10, 6.909433826122348e-11, 1.3649363527089241e-11, 2.3593392484850202e-12, 3.625065530805376e-13, 5.0128399720236344e-14, 6.3017204595910286e-15, 7.261826474563749e-16, 7.724502062790223e-17, 7.629752261477626e-18, 7.033753695936778e-19, 5.458019362273629e-20, 3.881091591592484e-21, 2.981599903365872e-22, 2.1700200348702923e-23], [1.133839280057379e-09, 1.5679040328022382e-09, 1.0840703348860498e-09, 4.996940571163061e-10, 1.7274765945670882e-10, 4.7776039635108567e-11, 1.1011002842692053e-11, 2.1751880744483968e-12, 3.7598871087999147e-13, 5.776972161414281e-14, 7.98855544042303e-15, 1.0042539467137348e-15, 1.157258235143013e-16, 1.230991081356044e-17, 1.2158915759862528e-18, 1.120912131004816e-19, 9.687675104901436e-21, 7.075197091554932e-22, 4.751533314873175e-23, 3.458184472701598e-24], [1.7065237137354968e-10, 2.359827763863616e-10, 1.6316172550898087e-10, 7.520816866024629e-11, 2.5999979233411203e-11, 7.190696778608147e-12, 1.6572487647554456e-12, 3.273841448404391e-13, 5.658947105634535e-14, 8.694830176058442e-15, 1.2023449475910484e-15, 1.5114868613413395e-16, 1.741771215658801e-17, 1.8527453658376365e-18, 1.8300193371733964e-19, 1.687067264486291e-20, 1.4580767828613844e-21, 1.1860403167068601e-22, 8.180782480042068e-24, 5.204859200890016e-25], [2.4332798568239504e-11, 3.3648060775047896e-11, 2.326473033395993e-11, 1.0723702249001397e-11, 3.707257346457614e-12, 1.0252994134852102e-12, 2.3630202173978265e-13, 4.668070174893843e-14, 8.068919225758246e-15, 1.2397691843142639e-15, 1.7143868077421905e-16, 2.1551827870620434e-17, 2.48353818944659e-18, 2.641772828722262e-19, 2.609368481024536e-20, 2.4055375021983715e-21, 2.0790269932276984e-22, 1.6911385343170292e-23, 1.2991959533809939e-24, 8.489633783466672e-26]] |
| Legacy trial inputs | {"lambda_home": 2.7091517631744395, "lambda_away": 1.3828274080634184, "rho": -0.11084550577255979, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6860 |
| Legacy p draw | 0.1737 |
| Legacy p away | 0.1403 |
| Legacy p over 1 5 | 0.9236 |
| Legacy p under 3 5 | 0.4110 |
| Legacy p btts yes | 0.7014 |
| Legacy p over 2 5 | 0.7794 |
| Legacy goal margin distribution | {"-1": 0.08030551390014702, "-10": 1.3678843916772576e-07, "-11": 1.6731942889424996e-08, "-12": 1.8837744977699304e-09, "-13": 1.964065824130625e-10, "-14": 1.906479349491419e-11, "-15": 1.7308943250218906e-12, "-16": 1.4757881992369206e-13, "-17": 1.1848593803753732e-14, "-18": 8.869365819753548e-16, "-19": 5.3920012975106685e-17, "-2": 0.039866494126716695, "-3": 0.014500300072987457, "-4": 0.004291963514526852, "-5": 0.0010643768086970663, "-6": 0.00022632941688439224, "-7": 4.203268484804019e-05, "-8": 6.919408221155635e-06, "-9": 1.0219740771822366e-06, "0": 0.1737269452630969, "1": 0.20749362462687237, "10": 0.00014517882169565508, "11": 3.479089508923566e-05, "12": 7.673853385855013e-06, "13": 1.56749432984944e-06, "14": 2.980899956999642e-07, "15": 5.302140171106226e-08, "16": 8.856661363635042e-09, "17": 1.3930867867777005e-09, "18": 2.0430043214859757e-10, "19": 2.4332798568239504e-11, "2": 0.19495710821101564, "3": 0.1389227508373876, "4": 0.08055968538916268, "5": 0.03914015118871508, "6": 0.016305475027306306, "7": 0.0059325982347086205, "8": 0.0019133398435952729, "9": 0.000553641195235209} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6482 |
| Legacy raw p draw | 0.1828 |
| Legacy raw p away | 0.1689 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.7092 |
| Legacy lambda away | 1.3828 |
| Legacy model home team | Bayern Munich |
| Legacy model away team | Dortmund |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.05076922801949, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,725.3258 |
| Elo away rating | 1,617.6463 |
| Elo rating diff | 167.6795 |
| Elo home expectancy | 0.7242 |

</details>


---

## 2026-10-31 — Borussia Monchengladbach vs SC Paderborn

The model's most likely 1X2 outcome is **Borussia Monchengladbach win** at **48.0%**. Expected goals are 1.45 for Borussia Monchengladbach and 0.99 for SC Paderborn (2.44 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.9%; Double Chance 1X: 73.2%; Double Chance X2: 52.0%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 48.0% | 2.08 |
| Draw | 25.2% | 3.98 |
| SC Paderborn win | 26.8% | 3.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.45 |
| SC Paderborn expected goals | 0.99 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.02% |
| 2 | 1-1 | 11.92% |
| 3 | 2-0 | 9.40% |
| 4 | 2-1 | 9.32% |
| 5 | 0-0 | 8.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 48.0% | 48.6% | 2.01 | -3.4% |
| Draw | 25.2% | 23.8% | 4.01 | +0.9% |
| SC Paderborn win | 26.8% | 27.6% | 3.47 | -7.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | aecb9d8c01176616c87d893bee4bc0de |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:57:03Z |
| Market best draw last update utc | 2026-10-29T11:57:03Z |
| Market best away last update utc | 2026-10-29T11:57:03Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | M'gladbach |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3258 |
| Dc lambda away | 0.8763 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:57:09.762880+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9454 |
| Shot lambda away | 1.4506 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.70 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.46 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.32 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.60 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.16788134013681752, "-10": 2.693111984887828e-08, "-11": 2.4007299716910573e-09, "-12": 1.9649462770864367e-10, "-13": 1.4862741906464598e-11, "-14": 1.0410626726305615e-12, "-15": 6.277671996487505e-14, "-2": 0.07250466745367701, "-3": 0.02154084857881801, "-4": 0.00499463523731872, "-5": 0.0009462334269191929, "-6": 0.00015126264232620263, "-7": 2.0892067718312172e-05, "-8": 2.538532924589028e-06, "-9": 2.752261490348359e-07, "0": 0.25155977582081934, "1": 0.23857406415969434, "10": 1.1510084684855162e-06, "11": 1.500743935578296e-07, "12": 1.7966072172129688e-08, "13": 1.987653014039878e-09, "14": 2.036374672026648e-10, "15": 1.7960507675878044e-11, "2": 0.14793695001422136, "3": 0.06428544875587373, "4": 0.021801823789103877, "5": 0.006041245862392854, "6": 0.0014125345640945174, "7": 0.0002853566528549428, "8": 5.0714080331226e-05, "9": 8.04219544910638e-06} |
| Raw goal margin distribution | {"-1": 0.1558726187390108, "-10": 2.5004709713406675e-08, "-11": 2.2290033381181596e-09, "-12": 1.8243916902338527e-10, "-13": 1.3799595003915557e-11, "-14": 9.665944108029642e-13, "-15": 5.828623793922563e-14, "-2": 0.06731833554339892, "-3": 0.020000009977907674, "-4": 0.004637363946776558, "-5": 0.0008785483965763091, "-6": 0.0001404426731258669, "-7": 1.9397637065990375e-05, "-8": 2.356949106961022e-06, "-9": 2.5553894530834065e-07, "0": 0.28346463881769324, "1": 0.2322513731182193, "10": 1.1205044362974914e-06, "11": 1.4609712122923425e-07, "12": 1.748993523757513e-08, "13": 1.9349762239214916e-09, "14": 1.9824066602846374e-10, "15": 1.7484518211630978e-11, "2": 0.14401632422510807, "3": 0.06258175547145244, "4": 0.02122403174601359, "5": 0.005881140734335301, "6": 0.0013750995660127639, "7": 0.00027779412941390536, "8": 4.9370055520665475e-05, "9": 7.829061145094939e-06} |
| Unadjusted home-win probability | 46.8% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 24.9% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.1% |
| P home draw | 73.2% |
| P draw away | 52.0% |
| P home away | 74.8% |
| Raw p home draw | 75.1% |
| Raw p draw away | 53.2% |
| Raw p home away | 71.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4520 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.56, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.66, "price": 1.56, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.01 |
| Reference draw odds | 4.01 |
| Reference away odds | 3.47 |
| Market reference 1x2 last update utc | 2026-10-29T11:57:03Z |
| Market reference home last update utc | 2026-10-29T11:57:03Z |
| Market reference draw last update utc | 2026-10-29T11:57:03Z |
| Market reference away last update utc | 2026-10-29T11:57:03Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.65 |
| Market reference over 2 5 last update utc | 2026-10-29T11:56:21Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:56:21Z |
| Home probability edge | -0.5% |
| Draw probability edge | +1.4% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -19.8% |
| Under 2.5 probability edge | +19.8% |
| Raw edge prob home | -0.0182 |
| Raw ev home | -0.0600 |
| Raw edge prob draw | 0.0456 |
| Raw ev draw | 0.1367 |
| Raw edge prob away | -0.0274 |
| Raw ev away | -0.1364 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10725388771695087, 0.08691485473495972, 0.043425219516696534, 0.012219162922061834, 0.0025787079059868094, 0.00043536432122647005, 6.125228186208362e-05, 7.386605753366236e-06, 7.794273133154626e-07, 7.310613074847534e-08, 6.1712691299606125e-09, 4.735899622854326e-10, 3.33151620868252e-11, 2.163312530817195e-12, 1.3044033871622332e-13], [0.13447530196542914, 0.12452245735250259, 0.060810245573379544, 0.017111031475753834, 0.0036110781423863785, 0.0006096598147878132, 8.577426535589609e-05, 1.0343789042752764e-05, 1.091466361179568e-06, 1.0237373151389811e-07, 8.641899694900365e-09, 6.631888618684301e-10, 4.665268731774277e-11, 3.0293817213838765e-12, 1.8266134560260626e-13], [0.1038755217176396, 0.08768673625200597, 0.0331275601581066, 0.011980665125415737, 0.002528375804050325, 0.0004268667316605461, 6.005673889757522e-05, 7.242431458604154e-06, 7.642141847192396e-07, 7.167922031148029e-08, 6.0508161906395175e-09, 4.6434627159735347e-10, 3.2664905370935964e-11, 2.1210882577350144e-12, 1.2789435961961753e-13], [0.048487154507715506, 0.0409305316461897, 0.017275796423289316, 0.004351133058078875, 0.0011801986284872667, 0.0001992534220765669, 2.8033364646502284e-05, 3.3806318114043805e-06, 3.5672091594585175e-07, 3.345852201525097e-08, 2.8244080480368204e-09, 2.1674817169365087e-10, 1.524736807585652e-11, 9.900844046478956e-13, 5.969869968401483e-14], [0.01697467396586736, 0.014329206095876987, 0.006048014464106574, 0.0017018146347766952, 0.0003214680412410804, 6.975583349183502e-05, 9.814088491518473e-06, 1.1835118678308408e-06, 1.248829985274321e-07, 1.1713360133317496e-08, 9.887857154902312e-10, 7.588050040371225e-11, 5.3378900979651054e-12, 3.466146887401613e-13, 2.089967896881078e-14], [0.004754076566017427, 0.004013163554541472, 0.0016938601526344144, 0.00047662518238440787, 0.00010058603308971069, 1.5200337039199418e-05, 2.7486199857603707e-06, 3.3146474847009614e-07, 3.497583152330767e-08, 3.2805467151299155e-09, 2.76928028678322e-10, 2.12517606825523e-11, 1.4949764736418423e-12, 9.70759598971081e-14, 5.853348006724652e-15], [0.0011095570986617341, 0.000936634917043893, 0.0003953311500976094, 0.00011123986902015431, 2.3475841310315042e-05, 3.963435988061035e-06, 4.991213408831182e-07, 7.736077858948248e-08, 8.163032633021467e-09, 7.656489845541308e-10, 6.463241720480657e-11, 4.959962591460672e-12, 3.4891355568788555e-13, 2.265662298818839e-14, 1.366116792948396e-15], [0.00022196594644522554, 0.00018737301224610066, 7.908565768857955e-05, 2.2253440439687595e-05, 4.696321930008766e-06, 7.928819718481565e-07, 1.1155215908872035e-07, 1.204108110606627e-08, 1.6330076806657988e-09, 1.5316742302524337e-10, 1.2929659657182936e-11, 9.922362646089667e-13, 6.979985771731908e-14, 4.53243800692321e-15, 2.732904933574327e-16], [3.885358514731288e-05, 3.279833416883559e-05, 1.3843390772974852e-05, 3.895308973250189e-06, 8.220582792496784e-07, 1.387884389399964e-07, 1.9526424575175716e-08, 2.3547530920468207e-09, 2.224031479803309e-10, 2.6810885217360747e-11, 2.263246414422861e-12, 1.736840123930885e-13, 1.2217976489287351e-14, 7.933715457130471e-16, 4.783758780869765e-17], [6.045376090744996e-06, 5.103216716006353e-06, 2.1539454667176307e-06, 6.06085838505427e-07, 1.2790715316830114e-07, 2.1594617517495758e-08, 3.03819016486994e-09, 3.663849291717735e-10, 3.8660574358322945e-11, 3.245722107646581e-12, 3.52147059514341e-13, 2.702415161650666e-14, 1.901041117970823e-15, 1.2344367592710458e-16, 7.443231003809076e-18], [8.465606132866958e-07, 7.146258905961406e-07, 3.016264609379936e-07, 8.487286670800089e-08, 1.7911401442117462e-08, 3.023989306023469e-09, 4.254511366449899e-10, 5.130649370408914e-11, 5.41381033165209e-12, 5.077865750812054e-13, 3.836778749556145e-14, 3.784310855539053e-15, 2.662111522187e-16, 1.7286361084995048e-17, 1.0423083872425618e-18], [1.0777055226864056e-07, 9.097473433828783e-08, 3.839825496714255e-08, 1.080465541886287e-08, 2.2801930482307975e-09, 3.849659344525213e-10, 5.416163147673338e-11, 6.531521871765439e-12, 6.891997101715234e-13, 6.464326212702041e-14, 5.456874326955853e-15, 3.7483212765689756e-16, 3.388974450783289e-17, 2.200622910641064e-18, 1.326900268738646e-19], [1.2576320515230791e-08, 1.06163269440645e-08, 4.48089716092933e-09, 1.2608528651270935e-09, 2.66087887716021e-10, 4.492372802407006e-11, 6.320409636403211e-12, 7.621981216798905e-13, 8.042638987796458e-14, 7.543567018502236e-15, 6.367917682750942e-16, 4.886809879299506e-17, 3.077015885893103e-18, 2.5680242399050313e-19, 1.548430690955907e-20], [1.3547057667840485e-09, 1.1435776716863616e-09, 4.826767270224772e-10, 1.3581751875560548e-10, 2.8662659759961197e-11, 4.839128689980675e-12, 6.808267467820473e-13, 8.210304354292047e-14, 8.663431727694114e-15, 8.125837545020132e-16, 6.859442550610366e-17, 5.264011454420865e-18, 3.7030217867083774e-19, 2.152278444649553e-20, 1.66795048198951e-21], [1.3550386367754556e-10, 1.1438586645772764e-10, 4.827953273871586e-11, 1.358508910032253e-11, 2.8669702572904008e-12, 4.840317730999728e-13, 6.809940353541548e-14, 8.212321739916935e-15, 8.665560452997766e-16, 8.127834175978756e-17, 6.861128010758883e-18, 5.265304895026613e-19, 3.703931670507905e-20, 2.4051396704052477e-21, 1.2980690862170585e-22]] |
| Legacy trial inputs | {"lambda_home": 1.4003439994125684, "lambda_away": 0.8441520658770899, "rho": -0.11084550577255979, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4860 |
| Legacy p draw | 0.2696 |
| Legacy p away | 0.2444 |
| Legacy p over 1 5 | 0.6714 |
| Legacy p under 3 5 | 0.8097 |
| Legacy p btts yes | 0.4372 |
| Legacy p over 2 5 | 0.3995 |
| Legacy goal margin distribution | {"-1": 0.16095854753667294, "-10": 6.8681338812835956e-09, "-11": 5.224234365605943e-10, "-12": 3.6472438167828694e-11, "-13": 2.3459738764198016e-12, "-14": 1.3044033871622332e-13, "-2": 0.06327403409030784, "-3": 0.016286360427208862, "-4": 0.0032519333206658405, "-5": 0.0005287497342756415, "-6": 7.239475400254086e-05, "-7": 8.552653141312111e-06, "-8": 8.880740455238686e-07, "-9": 8.222797655108565e-08, "0": 0.2695922180520288, "1": 0.24124431269066499, "10": 9.421549292749259e-07, "11": 1.1888314102882787e-07, "12": 1.376817771965587e-08, "13": 1.4690916332417762e-09, "14": 1.3550386367754556e-10, "2": 0.151354981631891, "3": 0.06462629882580949, "4": 0.0214062661959068, "5": 0.005773823435798198, "6": 0.0013113978902900708, "7": 0.00025700542475330207, "8": 4.42695039747919e-05, "9": 6.799690235864939e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4862 |
| Legacy raw p draw | 0.3013 |
| Legacy raw p away | 0.2125 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4003 |
| Legacy lambda away | 0.8442 |
| Legacy model home team | M'gladbach |
| Legacy model away team | Paderborn |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.201980448238338, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,420.8820 |
| Elo away rating | 1,406.2048 |
| Elo rating diff | 74.6772 |
| Elo home expectancy | 0.6058 |

</details>


---

## 2026-10-31 — FC Schalke 04 vs RB Leipzig

The model's most likely 1X2 outcome is **RB Leipzig win** at **53.7%**. Expected goals are 0.87 for FC Schalke 04 and 1.62 for RB Leipzig (2.49 combined). The most likely exact score is 0-1 at 12.4%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 45.8%; Under 3.5 goals: 75.9%; Double Chance 1X: 46.3%; Double Chance X2: 78.8%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 89.1%; BTTS Yes (both teams score): 47.3%; BTTS No (at least one team does not score): 52.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 21.2% | 4.73 |
| Draw | 25.2% | 3.97 |
| RB Leipzig win | 53.7% | 1.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| RB Leipzig expected goals | 1.62 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 72.0% |
| Under 1.5 | 28.0% |
| Over 2.5 | 45.8% |
| Under 2.5 | 54.2% |
| Over 3.5 | 24.1% |
| Under 3.5 | 75.9% |
| Over 4.5 | 10.9% |
| Under 4.5 | 89.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.41% |
| 2 | 1-1 | 11.92% |
| 3 | 0-2 | 10.76% |
| 4 | 1-2 | 9.37% |
| 5 | 0-0 | 8.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 21.2% | 22.0% | 4.31 | -8.8% |
| Draw | 25.2% | 24.6% | 3.86 | -2.8% |
| RB Leipzig win | 53.7% | 53.4% | 1.83 | -1.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 3966f2fe1c2f73bfa12e61db83bd0bf9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:57:03Z |
| Market best draw last update utc | 2026-10-29T11:57:03Z |
| Market best away last update utc | 2026-10-29T11:57:03Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Schalke 04 |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7504 |
| Dc lambda away | 1.5470 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:57:09.762880+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.3532 |
| Shot lambda away | 1.9244 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.3% |
| P btts no | 52.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.53 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.57 |
| Fair Over 2.5 odds | 2.18 |
| Fair Under 2.5 odds | 1.85 |
| Fair Over 3.5 odds | 4.15 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.19 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.2426678271685275, "-10": 3.2356077115215704e-06, "-11": 4.722367498023319e-07, "-12": 6.328063432571958e-08, "-13": 7.836394821656392e-09, "-14": 8.987407068559781e-10, "-15": 8.88432187713128e-11, "-2": 0.16810682364268825, "-3": 0.08188463724295594, "-4": 0.031111800354810763, "-5": 0.009655336249374992, "-6": 0.0025279387931573206, "-7": 0.0005717794115509055, "-8": 0.00011376412687040977, "-9": 2.019581549929715e-05, "0": 0.2518360726697057, "1": 0.1402398918557846, "10": 7.135722825166911e-09, "11": 5.590500266650754e-10, "12": 4.02133724389153e-11, "13": 2.673158819470649e-12, "14": 1.645703704610865e-13, "15": 8.73273536317619e-15, "2": 0.05377707857486753, "3": 0.014061222279086133, "4": 0.0028678376918889826, "5": 0.0004777554046808087, "6": 6.714497885830997e-05, "7": 8.152377489780222e-06, "8": 8.707026909512885e-07, "9": 8.297260475171884e-08} |
| Raw goal margin distribution | {"-1": 0.24530717080335573, "-10": 3.2707993589593445e-06, "-11": 4.773729686174334e-07, "-12": 6.3968897542827e-08, "-13": 7.921626304683501e-09, "-14": 9.085157379825972e-10, "-15": 8.98095099632592e-11, "-2": 0.16993521465821576, "-3": 0.0827752443688331, "-4": 0.03145018362214636, "-5": 0.009760351201580485, "-6": 0.002555433575802411, "-7": 0.0005779982925950525, "-8": 0.00011500146693163955, "-9": 2.041547254123051e-05, "0": 0.26491782563972965, "1": 0.1276954164542435, "10": 6.4974315496390255e-09, "11": 5.090429337122178e-10, "12": 3.6616281378036995e-11, "13": 2.43404443759601e-12, "14": 1.4984953078592065e-13, "15": 7.951591121677596e-15, "2": 0.04896671234866639, "3": 0.012803444234184409, "4": 0.0026113092611732124, "5": 0.00043502012556254744, "6": 6.11388523241335e-05, "7": 7.423146330718922e-06, "8": 7.928182292324631e-07, "9": 7.555069515426933e-08} |
| Unadjusted home-win probability | 19.3% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 54.3% |
| Raw p over 1 5 | 72.0% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 47.5% |
| P home draw | 46.3% |
| P draw away | 78.8% |
| P home away | 74.8% |
| Raw p home draw | 45.7% |
| Raw p draw away | 80.7% |
| Raw p home away | 73.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4584 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.31 |
| Reference draw odds | 3.86 |
| Reference away odds | 1.83 |
| Market reference 1x2 last update utc | 2026-10-29T11:57:03Z |
| Market reference home last update utc | 2026-10-29T11:57:03Z |
| Market reference draw last update utc | 2026-10-29T11:57:03Z |
| Market reference away last update utc | 2026-10-29T11:57:03Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-10-29T11:56:21Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:56:21Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -20.7% |
| Under 2.5 probability edge | +20.7% |
| Raw edge prob home | -0.0270 |
| Raw ev home | -0.1700 |
| Raw edge prob draw | 0.0187 |
| Raw ev draw | 0.0226 |
| Raw edge prob away | 0.0083 |
| Raw ev away | -0.0072 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.06671321373909285, 0.09029431440481483, 0.10270674248232056, 0.0702238621036559, 0.036010713777643276, 0.014773001289632427, 0.005050385107865987, 0.0014799037342913667, 0.0003794464459628275, 8.647986248031285e-05, 1.7738708649841504e-05, 3.3077777829554396e-06, 5.654081837416469e-07, 8.921250790443472e-08, 1.3070876851315738e-08, 1.7873947345543842e-09, 2.2914347867501247e-10, 2.764811905439125e-11], [0.046064928939069445, 0.11223193152366424, 0.09112779317668224, 0.06230696668187448, 0.03195093912981081, 0.013107523163362106, 0.004481014960156385, 0.0013130623964937604, 0.0003366684252037279, 7.673029863069037e-05, 1.5738882706190738e-05, 2.9348656416736667e-06, 5.016652147962097e-07, 7.915487116620286e-08, 1.1597292773155741e-08, 1.585887486633123e-09, 2.0331030882491912e-10, 2.4531126331326783e-11], [0.026449554924697374, 0.05425320245322972, 0.04596864390659867, 0.027641302975944602, 0.014174427610355542, 0.005814903827248937, 0.0019879172225768936, 0.0005825152059338226, 0.00014935655576052228, 3.4039940392453934e-05, 6.982256536510711e-06, 1.3019974284639875e-06, 2.2255424927800685e-07, 3.511555597142177e-08, 5.14491878380568e-09, 7.035488780508658e-10, 9.019475900753938e-11, 1.0882768514915235e-11], [0.007822561961492823, 0.016045602242006716, 0.0164563318626343, 0.009295614208880263, 0.004192143821186417, 0.0017197811312243477, 0.0005879344923647858, 0.00017228120869717118, 4.417280045422961e-05, 1.0067448909578954e-05, 2.0650303773880327e-06, 3.8507096194475534e-07, 6.582131191724193e-08, 1.0385566531488963e-08, 1.5216303672311685e-09, 2.0807740270716956e-10, 2.6675461759077688e-11, 3.2186224404485585e-12], [0.0017351655580484563, 0.003559163418011704, 0.003650269617603544, 0.0024958052808644036, 0.0010573457328640551, 0.0003814741258645943, 0.00013041298829742932, 3.821464388544669e-05, 9.798212187775297e-06, 2.233116297615141e-06, 4.580557629081053e-07, 8.54147111726576e-08, 1.4600187762855008e-08, 2.3036797196325983e-09, 3.3752121342050557e-10, 4.615479485658919e-11, 5.9170311104262846e-12, 7.139403727985838e-13], [0.0003079093042569443, 0.0006315821142792343, 0.0006477491286599071, 0.00044288665368397384, 0.00022711175438073068, 7.697255750482775e-05, 2.314209863518343e-05, 6.781280527737505e-06, 1.738716333842509e-06, 3.9627186139912956e-07, 8.128309751983899e-08, 1.5157046063120617e-08, 2.59083845643961e-09, 4.087935104594193e-10, 5.98939516256611e-11, 8.190279426937252e-12, 1.049991410921708e-12, 1.266904373762451e-13], [4.553270589859747e-05, 9.339647182695416e-05, 9.578720150246697e-05, 6.549275215073848e-05, 3.358460616605124e-05, 1.3777717189013252e-05, 3.8912785892136146e-06, 1.00279545832657e-06, 2.5711616497263774e-07, 5.859949625270026e-08, 1.201990106414388e-08, 2.2413785849993554e-09, 3.831254328365444e-10, 6.045116022045046e-11, 8.856938217756195e-12, 1.2111539963822212e-12, 1.552695857142917e-13, 1.8734602512704524e-14], [5.7713487458393345e-06, 1.1838163357669328e-05, 1.214119245383461e-05, 8.301318920700772e-06, 4.25690656530734e-06, 1.7463493383508747e-06, 5.970172559132245e-07, 1.445290516224946e-07, 3.258991590692089e-08, 7.427586885743501e-09, 1.5235431227423818e-09, 2.8409858870007606e-10, 4.856180722543994e-11, 7.662288476766676e-12, 1.1226321446579837e-12, 1.5351585108088513e-13, 1.968068690612945e-14, 2.3746430742835823e-15], [6.400873279471917e-07, 1.3129441115260346e-06, 1.3465523880306419e-06, 9.20680638164427e-07, 4.7212394688031683e-07, 1.9368368311708956e-07, 6.621384305555168e-08, 1.9402503275853867e-08, 4.109926804566193e-09, 8.237769804187665e-10, 1.6897274612828256e-10, 3.150873643629616e-11, 5.3858809779303905e-12, 8.498072067798544e-13, 1.245086099258501e-13, 1.702609827325765e-14, 2.1827407853305247e-15, 2.6336633033002247e-16], [6.310279823723199e-08, 1.2943616245629604e-07, 1.3274942331739266e-07, 9.076499723457885e-08, 4.6544183679593445e-08, 1.9094242057218184e-08, 6.527669891929084e-09, 1.9127893899103253e-09, 4.904380731388714e-10, 9.234384996000708e-11, 1.665812247950599e-11, 3.1062783955219207e-12, 5.30965300891141e-13, 8.377796336314753e-14, 1.2274640268456215e-14, 1.678512286050601e-15, 2.1518478083704993e-16, 2.5963882863599995e-17], [5.598871707592342e-09, 1.1484379269385485e-08, 1.1778352326258922e-08, 8.053233600606678e-09, 4.129688705356025e-09, 1.6941596033534017e-09, 5.791753661545275e-10, 1.6971454035191938e-10, 4.3514708202007927e-11, 9.917462717648548e-12, 1.680609776049873e-12, 2.756082885454606e-13, 4.711053525228054e-14, 7.433300612600692e-15, 1.0890822283596366e-15, 1.4892802239742777e-16, 1.9092528619787337e-17, 2.3036767503993374e-18], [4.516060269010162e-10, 9.263321547872839e-10, 9.500440758964123e-10, 6.495753108870042e-10, 3.3310145435817276e-10, 1.366512267764822e-10, 4.67163920961612e-11, 1.3689206196978825e-11, 3.509904407385772e-12, 7.99944376075409e-13, 1.640842135533145e-13, 2.527786695266015e-14, 3.7999444819591415e-15, 5.995714014781474e-16, 8.784557385929152e-17, 1.2012561816325319e-17, 1.5400068877777361e-18, 1.8581499252810482e-19], [3.3391073476231815e-11, 6.849161260347374e-11, 7.024483654835935e-11, 4.802862593091154e-11, 2.4629022809634248e-11, 1.0103787111129154e-11, 3.454140086950783e-12, 1.0121594104739332e-12, 2.595170767888272e-13, 5.91466894756189e-14, 1.2132141080237004e-14, 2.2623082388383185e-15, 3.1947497147833405e-16, 4.433141173599128e-17, 6.495170207151085e-18, 8.881908352711422e-19, 1.1386580355571817e-19, 1.3738882341912016e-20], [2.2789716730197455e-12, 4.6746159590785825e-12, 4.794275116179306e-12, 3.2779981772230553e-12, 1.680953604479558e-12, 6.895928228505656e-13, 2.3574825824051763e-13, 6.90808166647408e-14, 1.771228071141876e-14, 4.036816305524839e-15, 8.280298587770793e-16, 1.5440463139412492e-16, 2.639283770744969e-17, 3.440400831082625e-18, 4.433013788573041e-19, 6.061984665630782e-20, 7.771446491944197e-21, 9.376914371577749e-22], [1.4443178861560908e-13, 2.9625780436584694e-13, 3.0384130629739723e-13, 2.0774595200987833e-13, 1.0653187950912022e-13, 4.370353787189487e-14, 1.494074849801674e-14, 4.378056132964072e-15, 1.1225310142719791e-15, 2.5583670311577233e-16, 5.2477104014125923e-17, 9.785526229572434e-18, 1.6726687750696855e-18, 2.6392079316911735e-19, 3.1945661170079434e-20, 3.841834886246359e-21, 4.925221011960669e-22, 5.94270008011043e-23], [8.543256163451383e-15, 1.75238867937523e-14, 1.797245701668078e-14, 1.2288339720447516e-14, 6.3014461355357854e-15, 2.5850993252073165e-15, 8.837572595044625e-16, 2.5896553245231514e-16, 6.639861001699176e-17, 1.5132946227979427e-17, 3.104062800897205e-18, 5.788217266761384e-19, 9.893969990261831e-20, 1.5611126639896533e-20, 2.287247815507702e-21, 2.58397478496891e-22, 2.91330773994485e-23, 3.515154771230163e-24], [4.73756677204292e-16, 9.717674643339179e-16, 9.966424223407407e-16, 6.814360804516527e-16, 3.4943961946556117e-16, 1.433537802357675e-16, 4.900776644263243e-17, 1.4360642806183278e-17, 3.68206035857942e-18, 8.391805400790446e-19, 1.721323170289223e-19, 3.2097908885943554e-20, 5.486589957349229e-21, 8.656974978665432e-22, 1.2683675922693423e-22, 1.7344464198462993e-23, 1.8369917867457334e-24, 1.9492896062290617e-25], [2.4726253690797218e-17, 5.071837508101617e-17, 5.2016646011685095e-17, 3.556543307999506e-17, 1.8237912194734614e-17, 7.481903914392506e-18, 2.557807676781996e-18, 7.495090080503311e-19, 1.9217366828120285e-19, 4.37984136684305e-20, 8.98390997749785e-21, 1.6752503473754617e-21, 2.8635546834582603e-22, 4.518238366170009e-23, 6.61984946464693e-24, 9.052402689771745e-25, 1.1605153593665932e-25, 1.1568266375091366e-26]] |
| Legacy trial inputs | {"lambda_home": 0.8872620333798292, "lambda_away": 2.0511952888315172, "rho": -0.11084550577255979, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1812 |
| Legacy p draw | 0.2353 |
| Legacy p away | 0.5835 |
| Legacy p over 1 5 | 0.7969 |
| Legacy p under 3 5 | 0.6679 |
| Legacy p btts yes | 0.5298 |
| Legacy p over 2 5 | 0.5555 |
| Legacy goal margin distribution | {"-1": 0.21366120682921666, "-10": 2.0906859976461742e-05, "-11": 3.846127407611173e-06, "-12": 6.499220948159104e-07, "-13": 1.015407389577732e-07, "-14": 1.475017771939685e-08, "-15": 2.0015878118942182e-09, "-16": 2.5367460500633926e-10, "-17": 2.764811905439125e-11, "-2": 0.18104537689047873, "-3": 0.10861765306838632, "-4": 0.05128864216579904, "-5": 0.019883020946374626, "-6": 0.006523345112752748, "-7": 0.0018527651974056018, "-8": 0.00046355909008590943, "-9": 0.00010358892873165412, "0": 0.23534776168022264, "1": 0.11951177492764871, "10": 6.598835863841318e-09, "11": 5.251061079304025e-10, "12": 3.838217600285162e-11, "13": 2.5939016083949197e-12, "14": 1.6298788326478211e-13, "15": 9.567040273796986e-15, "16": 5.2447505228530815e-16, "17": 2.4726253690797218e-17, "2": 0.0466237125644554, "3": 0.012099424551517919, "4": 0.002471328004067975, "5": 0.0004144159352657032, "6": 5.881245650582289e-05, "7": 7.2254389597184e-06, "8": 7.819767518597062e-07, "9": 7.558697576389722e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1428 |
| Legacy raw p draw | 0.2245 |
| Legacy raw p away | 0.6328 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.8873 |
| Legacy lambda away | 2.0512 |
| Legacy model home team | Schalke 04 |
| Legacy model away team | RB Leipzig |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.281793634485094, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,439.0953 |
| Elo away rating | 1,517.4051 |
| Elo rating diff | -18.3098 |
| Elo home expectancy | 0.4737 |

</details>


---

## 2026-10-31 — Werder Bremen vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **40.7%**. Expected goals are 1.77 for Werder Bremen and 1.65 for TSG Hoffenheim (3.41 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 66.3%; Under 3.5 goals: 55.6%; Double Chance 1X: 59.3%; Double Chance X2: 64.5%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 74.2%; BTTS Yes (both teams score): 67.6%; BTTS No (at least one team does not score): 32.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 35.5% | 2.82 |
| Draw | 23.8% | 4.19 |
| TSG Hoffenheim win | 40.7% | 2.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.77 |
| TSG Hoffenheim expected goals | 1.65 |
| Expected total goals | 3.41 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 66.3% |
| Under 2.5 | 33.7% |
| Over 3.5 | 44.4% |
| Under 3.5 | 55.6% |
| Over 4.5 | 25.8% |
| Under 4.5 | 74.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.24% |
| 2 | 1-2 | 9.04% |
| 3 | 2-1 | 7.41% |
| 4 | 2-2 | 6.93% |
| 5 | 0-1 | 5.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 35.5% | 33.3% | 2.90 | +2.9% |
| Draw | 23.8% | 23.8% | 4.02 | -4.2% |
| TSG Hoffenheim win | 40.7% | 42.9% | 2.27 | -7.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 2fad25b09c01b71e47a5b0fd1d0b4e61 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T11:57:03Z |
| Market best draw last update utc | 2026-10-29T11:57:03Z |
| Market best away last update utc | 2026-10-29T11:57:03Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7768 |
| Dc lambda away | 1.6721 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:57:09.762880+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.7215 |
| Shot lambda away | 1.5412 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 67.6% |
| P btts no | 32.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.11 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.21 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.96 |
| Fair Over 3.5 odds | 2.25 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.88 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.20051350963334605, "-10": 1.972544477113001e-06, "-11": 2.88899378412831e-07, "-12": 3.8911097244622716e-08, "-13": 4.849823446531485e-09, "-14": 5.62012202923765e-10, "-15": 6.015528384453331e-11, "-16": 5.2368682593473504e-12, "-2": 0.12270135757905552, "-3": 0.055464270674243615, "-4": 0.020139436220950165, "-5": 0.006077162728754991, "-6": 0.0015639886205642821, "-7": 0.0003502452044837352, "-8": 6.93447239623399e-05, "-9": 1.2294568918656396e-05, "0": 0.23839323375282626, "1": 0.1649602950483535, "10": 3.0462085841098644e-06, "11": 4.786300088624583e-07, "12": 6.915877277669256e-08, "13": 9.247412125623469e-09, "14": 1.1496364196870866e-09, "15": 1.3201066904493704e-10, "16": 1.232898670439897e-11, "2": 0.10799865108201957, "3": 0.05237243345855719, "4": 0.020401271693315032, "5": 0.006604368238253318, "6": 0.0018234106499892039, "7": 0.00043807006745003464, "8": 9.304762434585162e-05, "9": 1.7698059676266308e-05} |
| Raw goal margin distribution | {"-1": 0.1750802538825816, "-10": 1.7223457336073434e-06, "-11": 2.5225520520551876e-07, "-12": 3.397558995848036e-08, "-13": 4.23466888518927e-09, "-14": 4.907262326260632e-10, "-15": 5.252515098428134e-11, "-16": 4.5726206980903025e-12, "-2": 0.10713784261200647, "-3": 0.04842914878311959, "-4": 0.017584937858120393, "-5": 0.0053063317049398505, "-6": 0.0013656113508689264, "-7": 0.00030581988931468573, "-8": 6.054899691768669e-05, "-9": 1.0735118304952778e-05, "0": 0.23972847622064727, "1": 0.1883410372929282, "10": 3.477964708863442e-06, "11": 5.464689083046023e-07, "12": 7.896103119147649e-08, "13": 1.0558099399037846e-08, "14": 1.312580798489274e-09, "15": 1.507212771071305e-10, "16": 1.407644272215067e-11, "2": 0.12330590197515298, "3": 0.059795470420613644, "4": 0.023292857664248944, "5": 0.00754044216696201, "6": 0.0020818528066361315, "7": 0.0005001601802805825, "8": 0.00010623578287007516, "9": 2.020650433804745e-05} |
| Unadjusted home-win probability | 40.5% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.6% |
| Raw p btts yes | 67.6% |
| P home draw | 59.3% |
| P draw away | 64.5% |
| P home away | 76.2% |
| Raw p home draw | 64.5% |
| Raw p draw away | 59.5% |
| Raw p home away | 76.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6627 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:56:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:57:03Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.90 |
| Reference draw odds | 4.02 |
| Reference away odds | 2.27 |
| Market reference 1x2 last update utc | 2026-10-29T11:57:03Z |
| Market reference home last update utc | 2026-10-29T11:57:03Z |
| Market reference draw last update utc | 2026-10-29T11:57:03Z |
| Market reference away last update utc | 2026-10-29T11:57:03Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.99 |
| Market reference over 2 5 last update utc | 2026-10-29T11:56:21Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:56:21Z |
| Home probability edge | +2.2% |
| Draw probability edge | +0.1% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | 0.0718 |
| Raw ev home | 0.1745 |
| Raw edge prob draw | 0.0019 |
| Raw ev draw | -0.0363 |
| Raw edge prob away | -0.0737 |
| Raw ev away | -0.1935 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.042105207673148334, 0.04730695279168805, 0.04761290444058193, 0.025463760367495432, 0.010213666331714753, 0.0032774100425094176, 0.000876392492004241, 0.00020087214950113993, 4.028550930281868e-05, 7.181670370124477e-06, 1.1522443473580052e-06, 1.680625774422939e-07, 2.2470301113823042e-08, 2.7732221386547455e-09, 3.1781598833746527e-10, 3.3994104174355806e-11, 3.4088095421840023e-12], [0.04328115358902378, 0.10364534440437093, 0.08717269941176968, 0.04662065367549931, 0.018699822568853993, 0.0060004883936733205, 0.001604554483072063, 0.0003677693624112153, 7.375724363732478e-05, 1.3148653706487101e-05, 2.109601405780624e-06, 3.0769953477690623e-07, 4.1140040241227277e-08, 5.077389475298738e-09, 5.818774961349061e-10, 6.223854351631915e-11, 6.241062860250632e-12], [0.048191449214267455, 0.07731951215573239, 0.06851901070565151, 0.042678012158512704, 0.017118405514227993, 0.005493035734863311, 0.0014688596220505945, 0.0003366676372614418, 6.751969980177282e-05, 1.2036691005223652e-05, 1.9311954541048526e-06, 2.816778284101753e-07, 3.766088630669537e-08, 4.648001962147159e-09, 5.326689545724067e-10, 5.6975119555509794e-11, 5.713265165387363e-12], [0.029410645187696063, 0.047187141602389446, 0.03785408851784492, 0.022363692545315672, 0.010447151081088573, 0.003352331744229242, 0.0008964268532906796, 0.0002054640934671203, 4.120643737482338e-05, 7.345843591766463e-06, 1.1785846911603978e-06, 1.7190449350835793e-07, 2.29839729387606e-08, 2.836618088255248e-09, 3.250812723181598e-10, 3.477121051751989e-11, 3.4867350408023127e-12], [0.013461714647405709, 0.02159829650877014, 0.017326411393315786, 0.009266302758291541, 0.004105806414158254, 0.0015344149390892404, 0.0004103086628755551, 9.404414554289961e-05, 1.8860834165179357e-05, 3.362308091024252e-06, 5.394567408823626e-07, 7.868338907384585e-08, 1.0520125729670457e-08, 1.2983646915619735e-09, 1.4879480872433962e-10, 1.5915329668712815e-11, 1.5959334407946784e-12], [0.004929310733352827, 0.007908703875500366, 0.006344456697276493, 0.003393065953433057, 0.001360979014478351, 0.00048242899140586747, 0.0001502437801480138, 3.443638705586057e-05, 6.906320236725814e-06, 1.2311850158790098e-06, 1.9753426459113263e-07, 2.881169928624441e-08, 3.852181541040132e-09, 4.75425544037673e-10, 5.4484578445095556e-11, 5.82775726686152e-12, 5.843870595594587e-13], [0.0015041486753590008, 0.002413292060825128, 0.0019359717115236509, 0.0010353730846646445, 0.00041529432664241876, 0.0001332616273657472, 3.936459942881834e-05, 1.05080504711844e-05, 2.1074208946471447e-06, 3.756884909336289e-07, 6.027635880456459e-08, 8.791711795123392e-09, 1.1754693659283192e-09, 1.450731635677779e-10, 1.662563204651965e-11, 1.778304076866584e-12, 1.783220959445212e-13], [0.00039341285395586836, 0.0006312009794189069, 0.0005063569637001236, 0.0002708037355747363, 0.00010862099535278956, 3.485482386390371e-05, 9.320318650475268e-06, 2.359851610125931e-06, 5.511998130447322e-07, 9.82620161409883e-08, 1.5765392565141145e-08, 2.2994883984134392e-09, 3.0744617574268833e-10, 3.794415289298714e-11, 4.3484646560489364e-12, 4.651187037175435e-13, 4.664047234039701e-14], [9.003562391740693e-05, 0.00014445530548331975, 0.00011588377119162089, 6.197556344808946e-05, 2.48587685653383e-05, 7.97680040589097e-06, 2.1330281823956848e-06, 4.888973374982512e-07, 1.0831276920932966e-07, 2.2488034749440667e-08, 3.6080340071058277e-09, 5.262559943331627e-10, 7.036147389611945e-11, 8.68381763682996e-12, 9.95180316182748e-13, 1.0644607125511518e-13, 1.067403869686797e-14], [1.8315875758471956e-05, 2.9386428535350766e-05, 2.357414391348008e-05, 1.260763985173031e-05, 5.056999626825684e-06, 1.6227141971987958e-06, 4.339202359936711e-07, 9.945599866648427e-08, 1.994619746664799e-08, 3.927982815576955e-09, 7.339795042361642e-10, 1.0705584067701248e-10, 1.4313578981209637e-11, 1.7665421532626826e-12, 2.0244874456804918e-13, 2.1654240080289024e-14, 2.1714112493105964e-15], [3.3533857064928944e-06, 5.380252121973415e-06, 4.316102504992409e-06, 2.308285982549697e-06, 9.258672907569402e-07, 2.9709671906310797e-07, 7.944484535314379e-08, 1.820902962823924e-08, 3.6518752565027436e-09, 6.51017320592282e-10, 1.1538371496545942e-10, 1.9600456492331245e-11, 2.6206200455440267e-12, 3.234296456683583e-13, 3.7065589179808057e-14, 3.9645944386043836e-15, 3.9755562564285034e-16], [5.581444924312527e-07, 8.955003547479295e-07, 7.18381078939376e-07, 3.8419592044596384e-07, 1.5410327778807407e-07, 4.944939591750487e-08, 1.3222965315339212e-08, 3.0307487682794443e-09, 6.078257140287879e-10, 1.083566770331206e-10, 1.7385004069428793e-11, 2.801135295581217e-12, 4.361814515828757e-13, 5.383230299731354e-14, 6.169273763937404e-15, 6.59875345191014e-16, 6.616998529515501e-17], [8.515716946681077e-08, 1.366281966425592e-07, 1.0960477100564748e-07, 5.861750415803678e-08, 2.3511830932572384e-08, 7.544588624059662e-09, 2.0174530313954437e-09, 4.624071185356897e-10, 9.273712817691231e-11, 1.6532184826864475e-11, 2.6524632201828847e-12, 3.8687957669478374e-13, 5.71408284020982e-14, 8.213297114448507e-15, 9.412578615876532e-16, 1.0067843965032551e-16, 1.0095680827827825e-17], [1.1993161588805699e-08, 1.924211490566233e-08, 1.5436254373004886e-08, 8.255431735243579e-09, 3.3113029635504774e-09, 1.0625467128129226e-09, 2.841292207672717e-10, 6.512338687553431e-11, 1.3060689669129615e-11, 2.3283202728087687e-12, 3.7356126568316083e-13, 5.4486419731431425e-14, 7.284942767224896e-15, 9.931955526850704e-16, 1.3256262157884525e-16, 1.4179109084946396e-17, 1.4218313299426455e-18], [1.5684167416096002e-09, 2.5164052813384776e-09, 2.018690368431548e-09, 1.079611680947976e-09, 4.330386917676169e-10, 1.3895552401074506e-10, 3.715726027137236e-11, 8.516570838272036e-12, 1.7080237085399206e-12, 3.044882259495976e-13, 4.885281823111718e-14, 7.125511672994536e-15, 9.526950932144575e-16, 1.175789817193318e-16, 1.4885164323924814e-17, 1.8542860366941224e-18, 1.8594130039143066e-19], [1.9143706630953847e-10, 3.0714620159619337e-10, 2.463963509617076e-10, 1.3177473019198033e-10, 5.2855631128648005e-11, 1.6960567404312412e-11, 4.535323240143072e-12, 1.039511561591065e-12, 2.0847714722456724e-13, 3.71650793791999e-14, 5.962854103125932e-15, 8.697223221632665e-16, 1.1628360555836576e-16, 1.4351399550167845e-17, 1.6446948726130473e-18, 1.943327756769845e-19, 2.2695534999317457e-20], [2.1905938675850698e-11, 3.514641122742406e-11, 2.8194870816674316e-11, 1.50788413877217e-11, 6.0482133188637234e-12, 1.940779581660293e-12, 5.189721859459169e-13, 1.1895019580080694e-13, 2.385581690346933e-14, 4.252760269777032e-15, 6.823230152561791e-16, 9.952139479363562e-17, 1.3306208570129196e-17, 1.6422152957060012e-18, 1.882006745845767e-19, 2.0130243827503347e-20, 2.22987761088359e-21]] |
| Legacy trial inputs | {"lambda_home": 1.8308628813131118, "lambda_away": 1.6044238846596324, "rho": -0.11084550577255979, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3788 |
| Legacy p draw | 0.2413 |
| Legacy p away | 0.3800 |
| Legacy p over 1 5 | 0.8673 |
| Legacy p under 3 5 | 0.5515 |
| Legacy p btts yes | 0.6816 |
| Legacy p over 2 5 | 0.6679 |
| Legacy goal margin distribution | {"-1": 0.18930055665463974, "-10": 1.5005961874179493e-06, "-11": 2.141922006347148e-07, "-12": 2.8116726687652503e-08, "-13": 3.4155614893859635e-09, "-14": 3.8576779701917176e-10, "-15": 4.0235167034606435e-11, "-16": 3.4088095421840023e-12, "-2": 0.11515124982514593, "-3": 0.05065438798506581, "-4": 0.0179086331080998, "-5": 0.005263407550621629, "-6": 0.001319596880679915, "-7": 0.00028792735393570924, "-8": 5.554827560961748e-05, "-9": 9.597288251468594e-06, "0": 0.24126332754408453, "1": 0.1692251274937188, "10": 4.367196782213072e-06, "11": 7.113433515384751e-07, "12": 1.065557976844155e-07, "13": 1.4771042062493605e-08, "14": 1.9037578140224677e-09, "15": 2.2658347753696253e-10, "16": 2.1905938675850698e-11, "2": 0.11655045356103297, "3": 0.05850582202817035, "4": 0.023603758023476307, "5": 0.00791630311641573, "6": 0.002264818466830223, "7": 0.0005639125300601516, "8": 0.0001241469634764691, "9": 2.4476581376303782e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4244 |
| Legacy raw p draw | 0.2447 |
| Legacy raw p away | 0.3309 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8309 |
| Legacy lambda away | 1.6044 |
| Legacy model home team | Werder Bremen |
| Legacy model away team | Hoffenheim |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 9.899922336466238, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,429.1271 |
| Elo away rating | 1,502.6430 |
| Elo rating diff | -13.5159 |
| Elo home expectancy | 0.4806 |

</details>


---
