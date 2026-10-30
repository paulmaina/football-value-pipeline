# Bundesliga — football model report

Fixtures in this report: **9**.

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
| Training sha256 | 69df04e69ba5d7ae4236cbf04e74187a5243585339c354bc88d80c442420a325 |
| Training as of utc | 2026-10-30T11:50:54.576591+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 64, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-30T11:50:54.576591+00:00', 'observations': 292, 'observations_sha256': 'df3ff0afa9102c7ffb274e2c208da88e976185bb9af2524035f0d343658fb9e7', 'eligible_training_matches': 68, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 104, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 14, 'retrospective_eligible_training_matches': 68, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '1c67f28e7f02f59f28b2ec48a8efb884fcdd954e1bb0d6574d720b78af23c23a', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1592, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1295, 'tuning_matches': 207, 'audit_matches': 84, 'audit_matchdays': 27, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.7186083396552695, 'audit_candidate_poisson_score': 0.7073752479581806, 'audit_gain': 0.01123309169708886, 'audit_gain_lower95': 0.002610647947329236, 'audit_baseline_briers': [0.625855444724906, 0.15383375866533233, 0.29443943969390557, 0.24506868373662988], 'audit_candidate_briers': [0.6198948864567517, 0.1513017524624931, 0.2911766969145373, 0.2428205789901822], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1575.313 |
| Base scoring parameter | 0.225 |
| Home-advantage parameter | 0.227 |
| Dixon-Coles low-score adjustment | -0.074 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1595, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 13.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261030T115054576591Z_4039d1b4c9421952453410e5fcd24d59c79b3b8a06f1d28dc83145cb90f40f68.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 6, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3} |
| Shot features applied fixtures | 9 |
| Goal rate features used | {'shot_features': 9} |
| Legacy comparison status | {'AVAILABLE': 9} |
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

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **43.4%**. Expected goals are 1.83 for Elversberg and 1.67 for FSV Mainz 05 (3.51 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.9%; Double Chance 1X: 56.6%; Double Chance X2: 67.6%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 76.1%; BTTS Yes (both teams score): 66.1%; BTTS No (at least one team does not score): 33.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 32.4% | 3.09 |
| Draw | 24.2% | 4.13 |
| FSV Mainz 05 win | 43.4% | 2.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 1.83 |
| FSV Mainz 05 expected goals | 1.67 |
| Expected total goals | 3.51 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 84.9% |
| Under 1.5 | 15.1% |
| Over 2.5 | 64.3% |
| Under 2.5 | 35.7% |
| Over 3.5 | 42.1% |
| Under 3.5 | 57.9% |
| Over 4.5 | 23.9% |
| Under 4.5 | 76.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.65% |
| 2 | 1-2 | 9.88% |
| 3 | 2-1 | 6.82% |
| 4 | 2-2 | 6.78% |
| 5 | 0-1 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 32.4% | 28.4% | 3.42 | +10.7% |
| Draw | 24.2% | 24.5% | 3.95 | -4.3% |
| FSV Mainz 05 win | 43.4% | 47.0% | 2.09 | -9.3% |

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
| Market best home last update utc | 2026-10-30T11:50:53Z |
| Market best draw last update utc | 2026-10-30T11:50:53Z |
| Market best away last update utc | 2026-10-30T11:50:53Z |
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
| Dc lambda away | 1.7409 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:50:54.576591+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.6420 |
| Shot lambda away | 1.4043 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 66.1% |
| P btts no | 33.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.96 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.64 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.38 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.19 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.21871733753100345, "-10": 1.5587636331964226e-06, "-11": 2.1935812159630787e-07, "-12": 2.8382849583783308e-08, "-13": 3.398011942373696e-09, "-14": 3.7823575056155536e-10, "-15": 3.893154573797865e-11, "-16": 3.282280017804513e-12, "-2": 0.13053508602550806, "-3": 0.05715792734466583, "-4": 0.020045969397784268, "-5": 0.005832041698400265, "-6": 0.0014454115786473264, "-7": 0.0003114787831651683, "-8": 5.931008862002821e-05, "-9": 1.0109110098200609e-05, "0": 0.2423274943661528, "1": 0.15142122882970088, "10": 2.456732482092375e-06, "11": 3.789715553380897e-07, "12": 5.375070734318269e-08, "13": 7.05388510617415e-09, "14": 8.606792820470698e-10, "15": 9.710815729561259e-11, "16": 8.97439100151092e-12, "2": 0.09869667508926533, "3": 0.0473725788393716, "4": 0.018211801612942464, "5": 0.005807935180246658, "6": 0.0015778581674287355, "7": 0.00037271785217906733, "8": 7.77956996398013e-05, "9": 1.453500672237929e-05} |
| Raw goal margin distribution | {"-1": 0.17147717044455799, "-10": 1.8749821029389834e-06, "-11": 2.78902493406037e-07, "-12": 3.81583084237936e-08, "-13": 4.831777759393868e-09, "-14": 5.688340843224571e-10, "-15": 6.178478593530688e-11, "-16": 5.4221593256928276e-12, "-2": 0.10519820657135437, "-3": 0.04792988000111971, "-4": 0.017589290228634313, "-5": 0.005373222522976669, "-6": 0.0014014310304508535, "-7": 0.00031829875922463776, "-8": 6.394803383880759e-05, "-9": 1.1509152989638557e-05, "0": 0.23538256072800054, "1": 0.1886188195652639, "10": 4.696237501107353e-06, "11": 7.657387323801883e-07, "12": 1.1483985213472651e-07, "13": 1.5939905914763517e-08, "14": 2.057025649467544e-09, "15": 2.4491249050379426e-10, "16": 2.3560090573354455e-11, "2": 0.12640344812239215, "3": 0.06312948106152758, "4": 0.025395074145941273, "5": 0.008503765768748235, "6": 0.002431215661479837, "7": 0.0006052879018474023, "8": 0.00013329981188839557, "9": 2.6297895550419184e-05} |
| Unadjusted home-win probability | 41.5% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 34.9% |
| Raw p over 1 5 | 87.2% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 68.9% |
| P home draw | 56.6% |
| P draw away | 67.6% |
| P home away | 75.8% |
| Raw p home draw | 65.1% |
| Raw p draw away | 58.5% |
| Raw p home away | 76.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9438 |
| Totals anchor target over 2 5 | 0.6427 |
| Totals anchor reference over odds | 1.52 |
| Totals anchor reference under odds | 2.65 |
| Totals anchor reference last update utc | 2026-10-30T11:50:53Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6777 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.11, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.26, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.72, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.48, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.55, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.61, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.26, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.56, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.55, "price": 2.56, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.42 |
| Reference draw odds | 3.95 |
| Reference away odds | 2.09 |
| Market reference 1x2 last update utc | 2026-10-30T11:50:53Z |
| Market reference home last update utc | 2026-10-30T11:50:53Z |
| Market reference draw last update utc | 2026-10-30T11:50:53Z |
| Market reference away last update utc | 2026-10-30T11:50:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Market reference over 2 5 last update utc | 2026-10-30T11:50:11Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:50:11Z |
| Home probability edge | +3.9% |
| Draw probability edge | -0.3% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.1310 |
| Raw ev home | 0.4202 |
| Raw edge prob draw | -0.0099 |
| Raw ev draw | -0.0702 |
| Raw edge prob away | -0.1211 |
| Raw ev away | -0.2698 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.042175837698018796, 0.049473346239278466, 0.05158773891989809, 0.02880248049916818, 0.012060756590724236, 0.004040258950471967, 0.0011278792409689545, 0.00026987907694666854, 5.650461001227148e-05, 1.051588977062025e-05, 1.7613703356139827e-06, 2.682023911046772e-07, 3.7435708083743704e-08, 4.823334178430376e-09, 5.770639837123896e-10, 6.443730423407836e-11, 6.74562249727161e-12], [0.03930140886362381, 0.10481843760819931, 0.09162743334431271, 0.051157453638086534, 0.02142168262723208, 0.007176095821004134, 0.0020032798904558195, 0.00047934504693745083, 0.00010036052162675434, 1.8677771291929888e-05, 3.12845351240757e-06, 4.7636700557640254e-07, 6.649133920109307e-08, 8.566952926890318e-09, 1.0249507501212842e-09, 1.1445015661110652e-10, 1.1981220512385108e-11], [0.04285837787278527, 0.07178610375753895, 0.07018026428708118, 0.04543159160907259, 0.019024033987004654, 0.006372902314369896, 0.0017790602813369553, 0.000425693752592893, 8.91275446287194e-05, 1.6587238362287613e-05, 2.778297437342615e-06, 4.2304903223860733e-07, 5.904921283797831e-08, 7.608085997831301e-09, 9.102318545474911e-10, 1.0164017958233693e-10, 1.0640207410395329e-11], [0.025374266857489662, 0.04250090282954656, 0.035593673532943654, 0.023198300550638595, 0.011263163447880585, 0.0037730714975150364, 0.001053291155073547, 0.00025203163101320317, 5.276788842720082e-05, 9.820460631589534e-06, 1.6448886794984459e-06, 2.5046582653426856e-07, 3.496003718859817e-08, 4.504360966640479e-09, 5.389020099648201e-10, 6.017598351063733e-11, 6.299525918871745e-12], [0.011267110140044634, 0.018871968042319654, 0.015804903536201852, 0.008824198063798127, 0.0043134013396977635, 0.001675382873819545, 0.00046770011210178357, 0.000111911337629945, 2.3430888234367603e-05, 4.360646641872603e-06, 7.303912276208755e-07, 1.1121606270353963e-07, 1.5523545634490948e-08, 2.000102363811788e-09, 2.392923639948573e-10, 2.6720355618855412e-11, 2.7972217978405783e-12], [0.004002409894114465, 0.006703879759330456, 0.0056143679703630186, 0.0031346154603252518, 0.0013125895206697808, 0.000513290871850023, 0.0001661408766655766, 3.975420843732889e-05, 8.323342696706043e-06, 1.5490303234134161e-06, 2.594565101138367e-07, 3.950722627331469e-08, 5.5144213438014585e-09, 7.104953613358677e-10, 8.500370665900518e-11, 9.491858548809772e-12, 9.936556988041862e-13], [0.00118481171905022, 0.0019845132088140735, 0.0016619909360428096, 0.0009279232338423614, 0.0003885587652276553, 0.00013016414162630077, 4.2417466064131316e-05, 1.1768222966711802e-05, 2.4639140491906716e-06, 4.585510552138065e-07, 7.680550515797672e-08, 1.1695110174653519e-08, 1.6324042776138955e-09, 2.103240929119794e-10, 2.516318679913203e-11, 2.8098234667903817e-12, 2.941465136730361e-13], [0.00030062862412603525, 0.0005035411668648682, 0.0004217058629475906, 0.00023544693270609538, 9.859109688427203e-05, 3.302724490185648e-05, 9.219890202050086e-06, 2.575326648826484e-06, 6.251821100881625e-07, 1.1635061554841453e-07, 1.948827224586976e-08, 2.967462951520196e-09, 4.1419868161830596e-10, 5.3366658732386065e-11, 6.384790177559707e-12, 7.129515595400983e-13, 7.463537056156235e-14], [6.674509727319121e-05, 0.00011179542287816771, 9.362647660361091e-05, 5.22735600172076e-05, 2.188904124130431e-05, 7.332657294522116e-06, 2.04698561280706e-06, 4.89802957303198e-07, 1.197115430175522e-07, 2.5831981818600423e-08, 4.3267557456261604e-09, 6.588314866210831e-10, 9.195974393792663e-11, 1.1848382164517355e-11, 1.417541136373888e-12, 1.5828839097047302e-13, 1.657042832376365e-14], [1.3172126382276426e-05, 2.2062795610049088e-05, 1.8477159116305014e-05, 1.0316172529944523e-05, 4.319796200718547e-06, 1.4470978775569389e-06, 4.039720413356287e-07, 9.666247738921e-08, 2.0238232802228888e-08, 4.396779544969426e-09, 8.538840429485753e-10, 1.3002021063622978e-10, 1.8148229888319905e-11, 2.338274924639578e-12, 2.7975134898623323e-13, 3.1238169931437205e-14, 3.2701694207693813e-15], [2.339563930043397e-06, 3.9186779193558024e-06, 3.28181599110264e-06, 1.8323044014850729e-06, 7.672595208271156e-07, 2.570259272739737e-07, 7.175139299654216e-08, 1.7168681724214368e-08, 3.5946086529829467e-09, 6.689809619972075e-10, 1.3080320078260045e-10, 2.309350716452793e-11, 3.2233933086140747e-12, 4.1531211540549107e-13, 4.968796582075177e-14, 5.548359732601219e-15, 5.808303230568257e-16], [3.7776460161601506e-07, 6.327409069943475e-07, 5.299081143010099e-07, 2.958584432670066e-07, 1.2388782520509005e-07, 4.150145066556847e-08, 1.1585550641580501e-08, 2.7721919151402254e-09, 5.804141055185422e-10, 1.0801898736440422e-10, 1.8092757168136535e-11, 3.2160047527011986e-12, 5.204747232779134e-13, 6.705959764884458e-14, 8.023014191810646e-15, 8.958822954539057e-16, 9.378548402906564e-17], [5.591380429265368e-08, 9.365343150282682e-08, 7.843291422586195e-08, 4.3790686116153235e-08, 1.8336920884400373e-08, 6.1427248091776755e-09, 1.714803897519279e-09, 4.103184775432809e-10, 8.590842171508423e-11, 1.5988137833843767e-11, 2.6779504460875506e-12, 4.077692796217977e-13, 6.64412616418238e-14, 9.925644707951997e-15, 1.1875047144148973e-15, 1.3260159136927297e-16, 1.388140439061896e-17], [7.639320271292633e-09, 1.2795562147962472e-08, 1.0716032635627816e-08, 5.982978271161834e-09, 2.505313548191065e-09, 8.392604071458015e-10, 2.3428804999648006e-10, 5.6060472057598046e-11, 1.1737386782838272e-11, 2.1844069992989316e-12, 3.6587961393643966e-13, 5.5712183480144155e-14, 7.776310378443429e-15, 1.1695932327404345e-15, 1.6224488660445516e-16, 1.8116921890182348e-17, 1.8965708968795527e-18], [9.69182826895841e-10, 1.6233432627357695e-09, 1.3595181814714646e-09, 7.590465628062807e-10, 3.178433133665976e-10, 1.0647501937521063e-10, 2.9723580965284097e-11, 7.11226193645428e-12, 1.4890950108884782e-12, 2.7713064454533877e-13, 4.641829717115338e-14, 7.068075373241216e-15, 9.86562443745274e-16, 1.271118030792302e-16, 1.7752619970329775e-17, 2.298451818830082e-18, 2.4061354648966437e-19], [1.1476077679070154e-10, 1.922198048289709e-10, 1.6098032098490206e-10, 8.987857682843826e-11, 3.7635773692470955e-11, 1.2607689275139597e-11, 3.5195642616807402e-12, 8.421617489660196e-13, 1.7632349173174698e-13, 3.281499337167771e-14, 5.496382821520717e-15, 8.369296253900337e-16, 1.1681869432144633e-16, 1.5051287389563777e-17, 1.800736905160531e-18, 2.3472730849136363e-19, 2.8491009885059655e-20], [1.2739504151193377e-11, 2.1338170323004194e-11, 1.787029963371395e-11, 9.977350577693338e-12, 4.177917826950928e-12, 1.3995697340958655e-12, 3.9070407830932877e-13, 9.348771764150497e-14, 1.9573533028329112e-14, 3.642766770760857e-15, 6.101491618431132e-16, 9.290690369200205e-17, 1.2967951968112135e-17, 1.67083165121699e-18, 1.9989839664764665e-19, 2.2321465494732313e-20, 2.7277673980369087e-21]] |
| Legacy trial inputs | {"lambda_home": 1.7761474967256365, "lambda_away": 1.6749608202769282, "rho": -0.11082685883326926, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3413 |
| Legacy p draw | 0.2452 |
| Legacy p away | 0.4135 |
| Legacy p over 1 5 | 0.8690 |
| Legacy p under 3 5 | 0.5478 |
| Legacy p btts yes | 0.6860 |
| Legacy p over 2 5 | 0.6698 |
| Legacy goal margin distribution | {"-1": 0.1996494785055962, "-10": 2.3015399933640616e-06, "-11": 3.4286843232488407e-07, "-12": 4.697586607048999e-08, "-13": 5.956224634052869e-09, "-14": 7.021543477338915e-10, "-15": 7.641852474646346e-11, "-16": 6.74562249727161e-12, "-2": 0.1260523370877758, "-3": 0.057771069992901006, "-4": 0.021293004109953037, "-5": 0.006526632706542499, "-6": 0.001706943878840905, "-7": 0.0003885886729696979, "-8": 7.822740450178287e-05, "-9": 1.4104440342984334e-05, "0": 0.24524464939060805, "1": 0.15695786849908216, "10": 3.0570515712414884e-06, "11": 4.829321476607025e-07, "12": 7.0162941116743e-08, "13": 9.433621205590997e-09, "14": 1.1792729313585259e-09, "15": 1.3609894711370574e-10, "16": 1.2739504151193377e-11, "2": 0.10472253306244093, "3": 0.050894871595691865, "4": 0.019891838518967864, "5": 0.006465491355910556, "6": 0.001793106068407026, "7": 0.00043286378265228545, "8": 9.240477408421774e-05, "9": 1.7667118503668936e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3983 |
| Legacy raw p draw | 0.2452 |
| Legacy raw p away | 0.3565 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7761 |
| Legacy lambda away | 1.6750 |
| Legacy model home team | Elversberg |
| Legacy model away team | Mainz |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 53.0% |
| Market home draw odds | 1.83 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:50:54Z |
| Market reference home draw last update utc | 2026-10-30T11:50:59Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.0% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:50:54Z |
| Market reference draw away last update utc | 2026-10-30T11:50:59Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.0% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:50:54Z |
| Market reference home away last update utc | 2026-10-30T11:50:59Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.82 |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home away odds | 1.27 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.11, "price": 1.72, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.72, "price": 2.11, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.7, "price": 2.14, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.14, "price": 1.7, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 85.4% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-10-30T11:50:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.5% |
| Market under 3 5 odds | 1.70 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market reference under 3 5 odds | 1.70 |
| Market reference under 3 5 opposite odds | 2.27 |
| Market reference under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.6% |
| Market btts yes odds | 1.47 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:50:54Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.82 |
| Market reference btts yes last update utc | 2026-10-30T11:50:54Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.09333149511901, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,430.0448 |
| Elo away rating | 1,516.7168 |
| Elo rating diff | -26.6720 |
| Elo home expectancy | 0.4617 |

</details>


---

## 2026-10-31 — Augsburg vs SC Freiburg

The model's most likely 1X2 outcome is **SC Freiburg win** at **41.4%**. Expected goals are 1.51 for Augsburg and 1.46 for SC Freiburg (2.97 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 66.1%; Under 3.5 goals: 55.3%; Double Chance 1X: 58.6%; Double Chance X2: 66.7%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 74.2%; BTTS Yes (both teams score): 68.2%; BTTS No (at least one team does not score): 31.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 33.3% | 3.00 |
| Draw | 25.2% | 3.96 |
| SC Freiburg win | 41.4% | 2.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.51 |
| SC Freiburg expected goals | 1.46 |
| Expected total goals | 2.97 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 86.3% |
| Under 1.5 | 13.7% |
| Over 2.5 | 66.1% |
| Under 2.5 | 33.9% |
| Over 3.5 | 44.7% |
| Under 3.5 | 55.3% |
| Over 4.5 | 25.8% |
| Under 4.5 | 74.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.79% |
| 2 | 1-2 | 9.05% |
| 3 | 2-2 | 7.38% |
| 4 | 2-1 | 7.04% |
| 5 | 0-1 | 5.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 33.3% | 31.2% | 3.09 | +3.0% |
| Draw | 25.2% | 24.9% | 3.85 | -2.8% |
| SC Freiburg win | 41.4% | 43.9% | 2.22 | -8.0% |

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
| Market best home last update utc | 2026-10-30T11:50:53Z |
| Market best draw last update utc | 2026-10-30T11:50:53Z |
| Market best away last update utc | 2026-10-30T11:50:53Z |
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
| Bbs statistics cutoff utc | 2026-10-30T11:50:54.576591+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.5704 |
| Shot lambda away | 1.4329 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 68.2% |
| P btts no | 31.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.03 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.29 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.95 |
| Fair Over 3.5 odds | 2.24 |
| Fair Under 3.5 odds | 1.81 |
| Fair Over 4.5 odds | 3.87 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.20119288686283385, "-10": 2.360199666023207e-06, "-11": 3.52792522258853e-07, "-12": 4.8496646270667393e-08, "-13": 6.1693668539659935e-09, "-14": 7.29685928378753e-10, "-15": 7.969748397414451e-11, "-16": 7.070566178681259e-12, "-2": 0.125244303566906, "-3": 0.05769240560691106, "-4": 0.0213590968489787, "-5": 0.006573707758517426, "-6": 0.0017258786986656975, "-7": 0.00039434769429382206, "-8": 7.96701476074611e-05, "-9": 1.4414618903307374e-05, "0": 0.2524206186936619, "1": 0.1565824357870296, "10": 2.630565270579937e-06, "11": 4.0928373793210383e-07, "12": 5.8562769207920664e-08, "13": 7.754526317500053e-09, "14": 9.546747362508754e-10, "15": 1.0853475995340574e-10, "16": 1.002266491120014e-11, "2": 0.10130247998663289, "3": 0.04857194826235394, "4": 0.018717788721844007, "5": 0.005996347999352954, "6": 0.0016386699324248378, "7": 0.0003897313147873182, "8": 8.195706528341024e-05, "9": 1.5434718820341932e-05} |
| Raw goal margin distribution | {"-1": 0.1850539750992949, "-10": 7.347302176897305e-07, "-11": 9.562799794687114e-08, "-12": 1.1437157306276928e-08, "-13": 1.2645876808462098e-09, "-14": 1.2897017348708738e-10, "-15": 1.0909228265615806e-11, "-2": 0.10701327539753647, "-3": 0.04449996911090908, "-4": 0.014677863428138612, "-5": 0.003992788374162031, "-6": 0.0009218313489326426, "-7": 0.00018458994787437136, "-8": 3.260380592286186e-05, "-9": 5.14827972854421e-06, "0": 0.2609478695443053, "1": 0.19296163165547656, "10": 1.096921893188198e-06, "11": 1.4860644557167678e-07, "12": 1.850015886626093e-08, "13": 2.129173687336241e-09, "14": 2.2602485953399785e-10, "15": 1.9900579966683743e-11, "2": 0.11594371654514087, "3": 0.050185014084799785, "4": 0.017229868527493104, "5": 0.004878655968380195, "6": 0.0011724117299634098, "7": 0.00024436641029656824, "8": 4.4926909174445016e-05, "9": 7.384229033418027e-06} |
| Unadjusted home-win probability | 38.3% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 35.6% |
| Raw p over 1 5 | 80.5% |
| Raw p under 3 5 | 65.4% |
| Raw p btts yes | 60.6% |
| P home draw | 58.6% |
| P draw away | 66.7% |
| P home away | 74.8% |
| Raw p home draw | 64.4% |
| Raw p draw away | 61.7% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1545 |
| Totals anchor target over 2 5 | 0.6612 |
| Totals anchor reference over odds | 1.47 |
| Totals anchor reference under odds | 2.74 |
| Totals anchor reference last update utc | 2026-10-30T11:50:53Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5729 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.88, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.27, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.5, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.83, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:56Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.3, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:56Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.65, "price": 2.3, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.09 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.22 |
| Market reference 1x2 last update utc | 2026-10-30T11:50:53Z |
| Market reference home last update utc | 2026-10-30T11:50:53Z |
| Market reference draw last update utc | 2026-10-30T11:50:53Z |
| Market reference away last update utc | 2026-10-30T11:50:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Market reference over 2 5 last update utc | 2026-10-30T11:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:50:12Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.4% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0705 |
| Raw ev home | 0.1824 |
| Raw edge prob draw | 0.0122 |
| Raw ev draw | 0.0046 |
| Raw edge prob away | -0.0827 |
| Raw ev away | -0.2088 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0700370369637164, 0.08026531783023459, 0.06779247056921384, 0.032394301165753245, 0.011609594021353696, 0.0033285527019336785, 0.0007952663309595304, 0.00016286320051966136, 2.918376953676168e-05, 4.648440608954181e-06, 6.6637039677071e-07, 8.684232041894416e-08, 1.0374294733483537e-08, 1.1439937156975147e-09, 1.171396742573511e-10], [0.06657132916566051, 0.12515806947189026, 0.0925848224268998, 0.044241205489224264, 0.015855333075935344, 0.004545836112175208, 0.0010861027989650695, 0.0002224238233742288, 3.9856551879902704e-05, 6.3484195918573935e-06, 9.100683945803338e-07, 1.1860138371737055e-07, 1.4168273078693226e-08, 1.5623631081154737e-09, 1.5997876827912611e-10], [0.05404488853982907, 0.07747525858530271, 0.05514666300961959, 0.03021031775195352, 0.010826889660674664, 0.00310414582691621, 0.0007416504660121134, 0.0001518831665058605, 2.7216236164323234e-05, 4.335048536131147e-06, 6.214445350721426e-07, 8.098751940192568e-08, 9.674872711323948e-09, 1.0668670850660804e-09, 1.0924226340206097e-10], [0.024603206258395217, 0.03526956606621464, 0.02528008499043932, 0.011996193823927562, 0.004928795426456583, 0.0014131205022186886, 0.0003376263672647528, 6.914276213129718e-05, 1.2389824274215396e-05, 1.9734723515247386e-06, 2.829042391911797e-07, 3.6868475410638045e-08, 4.404355254891518e-09, 4.85676844810765e-10, 4.973106636410403e-11], [0.008400208251151833, 0.012041995533930287, 0.008631313183176937, 0.004124430875052744, 0.0014678789314563946, 0.0004824780306249208, 0.00011527488597694611, 2.360723211693448e-05, 4.230225239975451e-06, 6.737974943831333e-07, 9.659125316354548e-08, 1.2587906962172948e-08, 1.5037674750427784e-09, 1.65823372625698e-10, 1.697954769077218e-11], [0.002294448875374244, 0.0032891735876071217, 0.0023575733165219657, 0.0011265549019604333, 0.00040373907088180375, 0.00011495211706184338, 3.1486401834434416e-05, 6.448124327628651e-06, 1.155451776223587e-06, 1.8404233049881565e-07, 2.6383118794905696e-08, 3.4382848745104627e-09, 4.1074191124525553e-10, 4.529331171993584e-11, 4.63782598462527e-12], [0.0005222584452974989, 0.0007486759468097124, 0.0005366267203320453, 0.0002564244590301307, 9.1898382102846e-05, 2.6347915998538474e-05, 6.2514565772734905e-06, 1.4677107965123162e-06, 2.630019150757226e-07, 4.1891393801294575e-08, 6.005279416687474e-09, 7.826163974818793e-10, 9.349235639450956e-11, 1.0309584499837844e-11, 1.0556538497270563e-12], [0.00010189333293384528, 0.00014606769540009812, 0.00010469660293352163, 5.002876068658837e-05, 1.7929499327393375e-05, 5.140514243714665e-06, 1.2281848202280985e-06, 2.497766775812542e-07, 5.131203130623236e-08, 8.173067901710335e-09, 1.1716381812011559e-09, 1.526895234842641e-10, 1.824048587945563e-11, 2.0114139566535776e-12, 2.0595950174029585e-13], [1.73945868489434e-05, 2.4935755267831262e-05, 1.787314341458314e-05, 8.540594341661855e-06, 3.0608109895757693e-06, 8.775561549113306e-07, 2.0966796263188405e-07, 4.2938062522356533e-08, 7.640796905502566e-09, 1.3952545799136304e-09, 2.0001467722793504e-10, 2.606619197445643e-11, 3.1139006514107835e-12, 3.4337589860666803e-13, 3.516010652740835e-14], [2.639550316947684e-06, 3.783888705843677e-06, 2.7121691233316083e-06, 1.2959967774586434e-06, 4.6446430075126666e-07, 1.3316519943538046e-07, 3.181617028474474e-08, 6.515657860933334e-09, 1.1675532396952517e-09, 1.8468021987051366e-10, 3.0351327643246315e-11, 3.955427391595388e-12, 4.725204181480286e-13, 5.210574817731191e-14, 5.3353880223934376e-15], [3.604858995837336e-07, 5.16769282742119e-07, 3.70403519103212e-07, 1.769955136600863e-07, 6.343233171416322e-08, 1.8186498057449938e-08, 4.34516466413426e-09, 8.898495968413591e-10, 1.5945385743210568e-10, 2.539808249267163e-11, 3.6156562027392367e-12, 5.401964843565683e-13, 6.453256333629883e-14, 7.116131632187432e-15, 7.286590213990971e-16], [4.475627498308289e-08, 6.415970263448394e-08, 4.598760110958029e-08, 2.1974950724259284e-08, 7.875467207720222e-09, 2.2579521389836383e-09, 5.394757042628673e-10, 1.10479642326666e-10, 1.979705918757285e-11, 3.1533093677107803e-12, 4.5203804700754897e-13, 5.850170235233562e-14, 8.012066916841288e-15, 8.835062467457649e-16, 9.046696020094108e-17], [5.093672567918892e-09, 7.301959722935664e-09, 5.23380871899653e-09, 2.5009499500983436e-09, 8.963000448690624e-10, 2.569755609545706e-10, 6.139725875089373e-11, 1.25735916057701e-11, 2.253086016370267e-12, 3.588753851955106e-13, 5.144605534236933e-14, 6.704521755443543e-15, 7.953765039304411e-16, 1.0055107433169796e-16, 1.0295965731123102e-17], [5.351136243640887e-10, 7.671043005218389e-10, 5.498355686405789e-10, 2.627362427218391e-10, 9.416042337474735e-11, 2.699645922697729e-11, 6.450063135808077e-12, 1.3209133656948989e-12, 2.3669700165209726e-13, 3.770150230631903e-14, 5.40464365669629e-15, 7.043407066993877e-16, 8.414144220051889e-17, 9.21409739336131e-18, 1.081638339576418e-18], [5.220069792620306e-11, 7.483154613567918e-11, 5.363683360108279e-11, 2.5630099134341352e-11, 9.185413327925792e-12, 2.6335229547914913e-12, 6.292080448472528e-13, 1.288559970254254e-13, 2.3089953461682604e-14, 3.677807186454964e-15, 5.272266637898483e-16, 6.870891487996759e-17, 8.208054901618242e-18, 9.05118224108757e-19, 9.203721586224407e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3657095197965063, "lambda_away": 1.4335353569691673, "rho": -0.11082685883326926, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3286 |
| Legacy p draw | 0.2639 |
| Legacy p away | 0.4075 |
| Legacy p over 1 5 | 0.7831 |
| Legacy p under 3 5 | 0.6909 |
| Legacy p btts yes | 0.5770 |
| Legacy p over 2 5 | 0.5361 |
| Legacy goal margin distribution | {"-1": 0.20850473831698596, "-10": 7.95149309591906e-07, "-11": 1.0212719164906756e-07, "-12": 1.2045900105001072e-08, "-13": 1.3039724839766409e-09, "-14": 1.171396742573511e-10, "-2": 0.12439568061065454, "-3": 0.05171621220934061, "-4": 0.01697064379037846, "-5": 0.004579629473497596, "-6": 0.0010469799879265756, "-7": 0.0002073507143393038, "-8": 3.6192052255542465e-05, "-9": 5.644071339389943e-06, "0": 0.26392730338007897, "1": 0.17388246291962853, "10": 4.301513325932638e-07, "11": 5.263370037379347e-08, "12": 5.914413702041813e-09, "13": 6.099451704997679e-10, "14": 5.220069792620306e-11, "2": 0.09916957793380746, "3": 0.039278039349541195, "4": 0.01227923575390222, "5": 0.0031568452225476194, "6": 0.000687561033914754, "7": 0.00012972639186035608, "8": 2.1571777950326687e-05, "9": 3.204904944695811e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3451 |
| Legacy raw p draw | 0.2791 |
| Legacy raw p away | 0.3758 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3657 |
| Legacy lambda away | 1.4335 |
| Legacy model home team | Augsburg |
| Legacy model away team | Freiburg |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 56.3% |
| Market home draw odds | 1.71 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:50:56Z |
| Market reference home draw last update utc | 2026-10-30T11:50:59Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.8% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:50:56Z |
| Market reference draw away last update utc | 2026-10-30T11:50:59Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:50:56Z |
| Market reference home away last update utc | 2026-10-30T11:50:59Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.71 |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home away odds | 1.27 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:56Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.02, "price": 1.77, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:56Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.77, "price": 2.02, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:56Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.21, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:56Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.21, "price": 1.65, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 86.3% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-30T11:50:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 55.4% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.15 |
| Market reference under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 69.3% |
| Market btts yes odds | 1.41 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:50:56Z |
| Market reference btts yes odds | 1.41 |
| Market reference btts yes opposite odds | 3.03 |
| Market reference btts yes last update utc | 2026-10-30T11:50:56Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 9.85969265539543, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,473.6758 |
| Elo away rating | 1,485.3747 |
| Elo rating diff | 48.3011 |
| Elo home expectancy | 0.5691 |

</details>


---

## 2026-10-31 — Bayer Leverkusen vs VfB Stuttgart

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **53.6%**. Expected goals are 2.13 for Bayer Leverkusen and 1.42 for VfB Stuttgart (3.54 combined). The most likely exact score is 2-1 at 8.4%. Goal-market probabilities: at least one goal: 97.3%; Over 2.5 goals: 74.6%; Under 3.5 goals: 45.1%; Double Chance 1X: 75.3%; Double Chance X2: 46.4%; Double Chance 12 (either team wins): 78.3%; Under 4.5 goals: 64.8%; BTTS Yes (both teams score): 72.3%; BTTS No (at least one team does not score): 27.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 53.6% | 1.87 |
| Draw | 21.7% | 4.61 |
| VfB Stuttgart win | 24.7% | 4.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.13 |
| VfB Stuttgart expected goals | 1.42 |
| Expected total goals | 3.54 |
| Over 0.5 | 97.3% |
| Under 0.5 | 2.7% |
| Over 1.5 | 90.7% |
| Under 1.5 | 9.3% |
| Over 2.5 | 74.6% |
| Under 2.5 | 25.4% |
| Over 3.5 | 54.9% |
| Under 3.5 | 45.1% |
| Over 4.5 | 35.2% |
| Under 4.5 | 64.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.44% |
| 2 | 1-1 | 8.27% |
| 3 | 2-2 | 7.08% |
| 4 | 3-1 | 6.62% |
| 5 | 1-2 | 5.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 53.6% | 53.8% | 1.82 | -2.5% |
| Draw | 21.7% | 21.5% | 4.41 | -4.4% |
| VfB Stuttgart win | 24.7% | 24.7% | 3.85 | -4.8% |

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
| Market best home last update utc | 2026-10-30T11:50:53Z |
| Market best draw last update utc | 2026-10-30T11:50:53Z |
| Market best away last update utc | 2026-10-30T11:50:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Leverkusen |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1730 |
| Dc lambda away | 1.3808 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:50:54.576591+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9414 |
| Shot lambda away | 1.5542 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 72.3% |
| P btts no | 27.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 37.58 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 10.75 |
| Fair Over 2.5 odds | 1.34 |
| Fair Under 2.5 odds | 3.93 |
| Fair Over 3.5 odds | 1.82 |
| Fair Under 3.5 odds | 2.22 |
| Fair Over 4.5 odds | 2.84 |
| Fair Under 4.5 odds | 1.54 |
| Goal margin distribution | {"-1": 0.13160406013713918, "-10": 6.733409518016251e-07, "-11": 9.323967769951616e-08, "-12": 1.1882885715691885e-08, "-13": 1.4023728658248755e-09, "-14": 1.540753638734217e-10, "-15": 1.5831556713376676e-11, "-16": 1.52606319568253e-12, "-17": 1.3658926206212985e-13, "-18": 9.858684393009842e-15, "-2": 0.07216788487976039, "-3": 0.029800545473934868, "-4": 0.010004398572272848, "-5": 0.0028122056991922995, "-6": 0.0006775307125633825, "-7": 0.00014252356498113312, "-8": 2.656995745207998e-05, "-9": 4.443431166796772e-06, "0": 0.21678544001866704, "1": 0.19601359146831365, "10": 3.8591366263440716e-05, "11": 8.028842136498479e-06, "12": 1.5373441692328588e-06, "13": 2.725898711217195e-07, "14": 4.499626291757719e-08, "15": 6.946465677348106e-09, "16": 1.0060274275722808e-09, "17": 1.3528538777478902e-10, "18": 1.467068273755078e-11, "2": 0.15930260108435726, "3": 0.0988325800720569, "4": 0.04984985902615025, "5": 0.021053148918269426, "6": 0.007620719813790077, "7": 0.0024085225361075817, "8": 0.0006746086814539174, "9": 0.00016950267375098255} |
| Raw goal margin distribution | {"-1": 0.13623825044320545, "-10": 3.376406050741335e-07, "-11": 4.249634637625766e-08, "-12": 4.919304468518568e-09, "-13": 5.27030638987047e-10, "-14": 5.2539675892446126e-11, "-15": 4.89341346992229e-12, "-16": 4.2294438605684395e-13, "-17": 2.99180251971475e-14, "-2": 0.07155389809106699, "-3": 0.027661225248122187, "-4": 0.008604560330240398, "-5": 0.0022267292800591068, "-6": 0.0004917962873716762, "-7": 9.456115264945111e-05, "-8": 1.608002869876482e-05, "-9": 2.4492017134333505e-06, "0": 0.2211395341251234, "1": 0.20791714180252494, "10": 1.9789050858220507e-05, "11": 3.7421304032254586e-06, "12": 6.508307391057089e-07, "13": 1.0476042385866175e-07, "14": 1.5690825842238537e-08, "15": 2.195671452083698e-09, "16": 2.8512528760950545e-10, "17": 3.030277664227359e-11, "2": 0.16152039092558484, "3": 0.0938128870982631, "4": 0.043844669615025735, "5": 0.017047180799687117, "6": 0.005656755694729291, "7": 0.0016341501709840856, "8": 0.0004175063212806922, "9": 9.554276814702703e-05} |
| Unadjusted home-win probability | 53.2% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 52.8% |
| Raw p btts yes | 67.3% |
| P home draw | 75.3% |
| P draw away | 46.4% |
| P home away | 78.3% |
| Raw p home draw | 75.3% |
| Raw p draw away | 46.8% |
| Raw p home away | 77.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1054 |
| Totals anchor target over 2 5 | 0.7458 |
| Totals anchor reference over odds | 1.31 |
| Totals anchor reference under odds | 3.53 |
| Totals anchor reference last update utc | 2026-10-30T11:50:53Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6884 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 8.1, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.62, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.02, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.86, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.36, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.49, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:40Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.82 |
| Reference draw odds | 4.41 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-30T11:50:53Z |
| Market reference home last update utc | 2026-10-30T11:50:53Z |
| Market reference draw last update utc | 2026-10-30T11:50:53Z |
| Market reference away last update utc | 2026-10-30T11:50:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.31 |
| Reference Under 2.5 odds | 3.51 |
| Market reference over 2 5 last update utc | 2026-10-30T11:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:50:12Z |
| Home probability edge | -0.2% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.0057 |
| Raw ev home | -0.0318 |
| Raw edge prob draw | 0.0062 |
| Raw ev draw | -0.0248 |
| Raw edge prob away | -0.0005 |
| Raw ev away | -0.0495 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.03891529704545585, 0.03157161472815633, 0.02611198591034282, 0.010741270735588018, 0.00331384878417559, 0.0008178990389282559, 0.00016822303446529176, 2.965681020462179e-05, 4.574793190599713e-06, 6.272865443003622e-07, 7.741105510997682e-08, 8.684549940734308e-09, 8.931061625344786e-10, 8.4780651368981e-11, 7.473184913903174e-12, 6.148249519815408e-13, 4.7420760768425644e-14, 3.4423625699085337e-15, 2.3600495484078606e-16], [0.05512285280063982, 0.09307267602717312, 0.059834947688865485, 0.02461334709595104, 0.007593599710522887, 0.0018741947233381854, 0.00038547877981605426, 6.795782187172833e-05, 1.0483021559018533e-05, 1.4374110683505888e-06, 1.773854523723024e-07, 1.9900424011769657e-08, 2.0465299230529628e-09, 1.942726936629356e-10, 1.712461204321876e-11, 1.4088556483577602e-12, 1.0866346013234739e-13, 7.888085762753138e-15, 5.407993162870889e-16], [0.07316254133962091, 0.09028711951639545, 0.0592335641831774, 0.02820042759273197, 0.008700269734546512, 0.002147334630440136, 0.0004416573811095185, 7.786180512477766e-05, 1.2010787857324026e-05, 1.6468953448708523e-06, 2.03237113023609e-07, 2.2800656254544667e-08, 2.344785481081862e-09, 2.2258545371863925e-10, 1.9620305198469264e-11, 1.6141783376816806e-12, 1.2449976947434646e-13, 9.037673361961119e-15, 6.196138989833609e-16], [0.05588336391918141, 0.06896354151679743, 0.042552646485429294, 0.018611328912027304, 0.006645481839043262, 0.0016401874567492823, 0.00033734886328736305, 5.9472778166550215e-05, 9.17413770075584e-06, 1.2579395167125354e-06, 1.5523754835497343e-07, 1.7415706832190823e-08, 1.7910053143650067e-09, 1.700162909258953e-10, 1.498647580490328e-11, 1.232949455055002e-12, 9.509601222150695e-14, 6.903199099176916e-15, 4.73276465965493e-16], [0.03201382468824021, 0.03950704777170951, 0.024377075198538784, 0.010027608215948808, 0.0032893450253183667, 0.0009396118990288451, 0.00019325657245110507, 3.407008741814532e-05, 5.2555754596756334e-06, 7.20634055148959e-07, 8.893071765070526e-08, 9.97691166469263e-09, 1.0260107146146141e-09, 9.739699527963179e-11, 8.585281476730312e-12, 7.063180334075051e-13, 5.447751978948275e-14, 3.954626032689707e-15, 2.711252284740972e-16], [0.014671772052256105, 0.018105877851484452, 0.011171888835420715, 0.004595601537974771, 0.0014178144228983972, 0.0003720672541927152, 8.856849833517323e-05, 1.561414674027018e-05, 2.4086033424215215e-06, 3.302629002689049e-07, 4.0756492875216634e-08, 4.57236756792872e-09, 4.702154608077069e-10, 4.463654459388408e-11, 3.934590573219256e-12, 3.2370194075434525e-13, 2.49667685791122e-14, 1.8123848764891426e-15, 1.2425530496670167e-16], [0.005603331718136233, 0.006914859315465065, 0.0042666829091976555, 0.0017551172257811872, 0.0005414809130050496, 0.00013364421468464868, 2.9226107447127555e-05, 5.963236299594477e-06, 9.198754899497038e-07, 1.2613149780471487e-07, 1.5565410124578475e-08, 1.746243884453801e-09, 1.7958111648120342e-10, 1.704724999952904e-11, 1.50266893993961e-12, 1.2362578599169047e-13, 9.535118578753699e-15, 6.921722630185233e-16, 4.745464208323406e-17], [0.001834270183099772, 0.0022636033168684324, 0.0013967135330845272, 0.000574543745942287, 0.00017725566562979916, 4.374889984585342e-05, 8.998143213655447e-06, 1.686657588844965e-06, 3.011244502833506e-07, 4.128958576984927e-08, 5.095391298505923e-09, 5.716390267073699e-10, 5.878650488299179e-11, 5.580476750425982e-12, 4.91903918998778e-13, 4.0469332267598946e-14, 3.1213543265195194e-15, 2.265850046882236e-16, 1.5534442614063276e-17], [0.0005253978997895169, 0.0006483736363360867, 0.00040006666610591205, 0.00016456903690445043, 5.0772102880889335e-05, 1.2531185595717142e-05, 2.5773768717488425e-06, 4.543775883855424e-07, 7.452448419329876e-08, 1.1826753684671301e-08, 1.4594948505986674e-09, 1.637370256775522e-10, 1.6838471500035317e-11, 1.598439963486317e-12, 1.4089815574684773e-13, 1.1591804945195513e-14, 8.940629481753263e-16, 6.490171768796349e-17, 4.4495972289299736e-18], [0.00013377064956422304, 0.0001650812889197739, 0.00010186028116104165, 4.1900637542872365e-05, 1.2926997205049812e-05, 3.190543467380575e-06, 6.562214627119205e-07, 1.1568829104590939e-07, 1.7845816945831364e-08, 2.601752545100624e-09, 3.715994568658111e-10, 4.1688800604979226e-11, 4.287214073620712e-12, 4.0697603148135756e-13, 3.587383547632703e-14, 2.9513693864436645e-15, 2.2763581920793967e-16, 1.652451396633072e-17, 1.1329042461943347e-18], [3.065320212129262e-05, 3.782795502739865e-05, 2.334102283821291e-05, 9.60142389826743e-06, 2.9621883383136e-06, 7.311048731615286e-07, 1.5037146936467164e-07, 2.6509675927040006e-08, 4.089323298064192e-09, 5.607198781008451e-10, 7.35729239478916e-11, 9.552882005893074e-12, 9.824041369616962e-13, 9.325751644444488e-14, 8.220397623126675e-15, 6.762987443954894e-16, 5.2162165609257866e-17, 3.7865501006098855e-18, 2.59602109698908e-19], [6.385548041638031e-06, 7.880162835470542e-06, 4.8623051544376084e-06, 2.0001288390008096e-06, 6.170707995802619e-07, 1.5230073754042606e-07, 3.132476137143355e-08, 5.522385835272429e-09, 8.518708836438333e-10, 1.168068414303523e-10, 1.4414689620470639e-11, 1.7194306893348305e-12, 2.046503588124424e-13, 1.9427019374468525e-14, 1.7124391682192359e-15, 1.4088375190783384e-16, 1.0866206184130602e-17, 7.887984258166018e-19, 5.4079235723352833e-20], [1.219359997959182e-06, 1.5047659615622482e-06, 9.284873223929379e-07, 3.819370054283553e-07, 1.1783349588954687e-07, 2.9082770312826178e-08, 5.981657441597595e-09, 1.0545338218299968e-09, 1.6267002803332957e-10, 2.2304990738366852e-11, 2.7525743744448467e-12, 3.0880433791388635e-13, 3.376557968224226e-14, 3.709709824488033e-15, 3.270008787107008e-16, 2.6902626104861444e-17, 2.0749694566712046e-18, 1.5062595107298063e-19, 1.0326765428946028e-20], [2.149332492580726e-07, 2.652409772608832e-07, 1.6366191890077247e-07, 6.732299052454441e-08, 2.0770187791436673e-08, 5.12634031887537e-09, 1.054370384482908e-09, 1.8587979034723254e-10, 2.8673400587703774e-11, 3.9316396651457855e-12, 4.851887507496715e-13, 5.443209539750807e-14, 5.5977155029254905e-15, 5.649884029760669e-16, 5.763954983693713e-17, 4.742052266738765e-18, 3.657491866061107e-19, 2.655042410845672e-20, 1.820270676161384e-21], [3.5179574430225336e-08, 4.3413779551115614e-08, 2.6787650013377263e-08, 1.1019207889886826e-08, 3.3995967113550738e-09, 8.390626923710722e-10, 1.7257591157245594e-10, 3.0424198871825066e-11, 4.693168849513896e-12, 6.43517979234325e-13, 7.941411498046778e-14, 8.909268147388972e-15, 9.1621584773021e-16, 8.697440419033224e-17, 8.151461661571951e-18, 7.761636752136409e-19, 5.986463600871088e-20, 4.345686971660674e-21, 2.979359775940804e-22], [5.3742063203634565e-09, 6.632104345583377e-09, 4.092214313027272e-09, 1.6833488649694652e-09, 5.19339259463982e-10, 1.281793795847493e-10, 2.636355242314502e-11, 4.647751558031274e-12, 7.169517568671995e-13, 9.83069990834587e-14, 1.2131694188074531e-14, 1.361024002222529e-15, 1.3996567836415746e-16, 1.3286641475342472e-17, 1.171181478635094e-18, 1.0244835757520239e-19, 9.14521879286449e-21, 6.638687013039666e-22, 4.551417803605067e-23], [7.696785184020284e-10, 9.498310898959023e-10, 5.860752754318133e-10, 2.4108442867817003e-10, 7.437828917316502e-11, 1.835748556854976e-11, 3.7757128698192886e-12, 6.656377369680702e-13, 1.0267978806477193e-13, 1.407924833782505e-14, 1.7374666791267168e-15, 1.949219801202924e-16, 2.0045485701258656e-17, 1.902874939231757e-18, 1.6773327474237953e-19, 1.3799551834631112e-20, 1.1316628602090794e-21, 9.507738407753561e-23, 6.5184109110839766e-24], [1.037469784812439e-10, 1.2803021428847363e-10, 7.899861764993905e-11, 3.249640003746682e-11, 1.0025643930326626e-11, 2.4744534435028584e-12, 5.089382027573878e-13, 8.972304971808898e-14, 1.3840476910972214e-14, 1.897778669163095e-15, 2.3419767326425975e-16, 2.6274042984916092e-17, 2.701983391731208e-18, 2.5649348481603027e-19, 2.2609206349444555e-20, 1.8600776467175344e-21, 1.4346570810342878e-22, 1.1073151668545164e-23, 8.786336377532874e-25], [1.3207419279103825e-11, 1.6298775590915953e-11, 1.0056850628772616e-11, 4.136926073793101e-12, 1.2763059210901708e-12, 3.15008153426587e-13, 6.478993730102301e-14, 1.1422115168789363e-14, 1.7619499310913723e-15, 2.4159507052157705e-16, 2.981433204390471e-17, 3.344794296074065e-18, 3.439736565072178e-19, 3.2652681031440347e-20, 2.878245440939519e-21, 2.3679557449789828e-22, 1.8263777768121357e-23, 1.3258021161054406e-24, 9.664474986904095e-26]] |
| Legacy trial inputs | {"lambda_home": 2.2914744169329992, "lambda_away": 1.2340621014964772, "rho": -0.11082685883326926, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5698 |
| Legacy p draw | 0.2135 |
| Legacy p away | 0.2167 |
| Legacy p over 1 5 | 0.8744 |
| Legacy p under 3 5 | 0.5347 |
| Legacy p btts yes | 0.6493 |
| Legacy p over 2 5 | 0.6820 |
| Legacy goal margin distribution | {"-1": 0.1272869288150254, "-10": 9.98351996433249e-08, "-11": 1.0969383785819504e-08, "-12": 1.1082884482102463e-09, "-13": 1.036186166434406e-10, "-14": 9.013714656062932e-12, "-15": 7.329993619418148e-13, "-16": 5.592846043016214e-14, "-17": 3.983161886195622e-15, "-18": 2.3600495484078606e-16, "-2": 0.061275623584042566, "-3": 0.02085616402560731, "-4": 0.005694775659452749, "-5": 0.001291176958783258, "-6": 0.000249543272101771, "-7": 4.195242933496884e-05, "-8": 6.2339292701144285e-06, "-9": 8.293651166406021e-07, "0": 0.21352526841394417, "1": 0.19955115659806447, "10": 3.953270691296945e-05, "11": 8.06553334709629e-06, "12": 1.5131488916309656e-06, "13": 2.626906682029774e-07, "14": 4.243152675719908e-08, "15": 6.40717295398309e-09, "16": 9.077655833192747e-10, "17": 1.2004575407215986e-10, "18": 1.3207419279103825e-11, "2": 0.17168668667988365, "3": 0.1085078882091271, "4": 0.05501504790175054, "5": 0.0231616044484128, "6": 0.008312023000059777, "7": 0.002594752763590913, "8": 0.0007159434775509836, "9": 0.00017686448304524366} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6019 |
| Legacy raw p draw | 0.2121 |
| Legacy raw p away | 0.1860 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2915 |
| Legacy lambda away | 1.2341 |
| Legacy model home team | Leverkusen |
| Legacy model away team | Stuttgart |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 74.8% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:50:17Z |
| Market reference home draw last update utc | 2026-10-30T11:50:59Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.8% |
| Market draw away odds | 2.06 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:50:17Z |
| Market reference draw away last update utc | 2026-10-30T11:50:59Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.4% |
| Market home away odds | 1.24 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:50:17Z |
| Market reference home away last update utc | 2026-10-30T11:50:59Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 2.06 |
| Market reference dc home away odds | 1.23 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:17Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.3, "price": 1.58, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:17Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.58, "price": 2.3, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:17Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.84, "price": 1.97, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:17Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.97, "price": 1.84, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:17Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.47, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:17Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.47, "price": 1.51, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 91.3% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 8.00 |
| Market reference over 1 5 last update utc | 2026-10-30T11:50:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 45.2% |
| Market under 3 5 odds | 2.14 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market reference under 3 5 odds | 2.14 |
| Market reference under 3 5 opposite odds | 1.78 |
| Market reference under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 72.3% |
| Market btts yes odds | 1.34 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:50:17Z |
| Market reference btts yes odds | 1.33 |
| Market reference btts yes opposite odds | 3.10 |
| Market reference btts yes last update utc | 2026-10-30T11:50:54Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.79589043379434, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,573.7454 |
| Elo away rating | 1,532.5206 |
| Elo rating diff | 101.2247 |
| Elo home expectancy | 0.6417 |

</details>


---

## 2026-10-31 — Bayern Munich vs Borussia Dortmund

The model's most likely 1X2 outcome is **Bayern Munich win** at **70.9%**. Expected goals are 2.52 for Bayern Munich and 1.24 for Borussia Dortmund (3.76 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 97.4%; Over 2.5 goals: 73.3%; Under 3.5 goals: 47.4%; Double Chance 1X: 87.7%; Double Chance X2: 29.1%; Double Chance 12 (either team wins): 83.2%; Under 4.5 goals: 66.8%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 70.9% | 1.41 |
| Draw | 16.8% | 5.95 |
| Borussia Dortmund win | 12.3% | 8.15 |

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
| Over 2.5 | 73.3% |
| Under 2.5 | 26.7% |
| Over 3.5 | 52.6% |
| Under 3.5 | 47.4% |
| Over 4.5 | 33.2% |
| Under 4.5 | 66.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.05% |
| 2 | 3-1 | 8.44% |
| 3 | 2-0 | 8.13% |
| 4 | 1-1 | 7.01% |
| 5 | 3-0 | 6.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 70.9% | 73.6% | 1.34 | -5.0% |
| Draw | 16.8% | 16.0% | 5.75 | -3.3% |
| Borussia Dortmund win | 12.3% | 10.4% | 8.62 | +5.7% |

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
| Market best home last update utc | 2026-10-30T11:50:53Z |
| Market best draw last update utc | 2026-10-30T11:50:53Z |
| Market best away last update utc | 2026-10-30T11:50:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Bayern Munich |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5385 |
| Dc lambda away | 1.2791 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:50:54.576591+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 2.4430 |
| Shot lambda away | 1.0663 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 38.83 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.81 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.75 |
| Fair Over 3.5 odds | 1.90 |
| Fair Under 3.5 odds | 2.11 |
| Fair Over 4.5 odds | 3.01 |
| Fair Under 4.5 odds | 1.50 |
| Goal margin distribution | {"-1": 0.0736527137292316, "-10": 5.295881971169751e-08, "-11": 5.818534669621386e-09, "-12": 5.880196745222647e-10, "-13": 5.5003309860580364e-11, "-14": 4.787966081406043e-12, "-15": 3.8968347584254207e-13, "-16": 2.975707716302193e-14, "-17": 2.117446159200522e-15, "-18": 1.2399949520547215e-16, "-2": 0.03373342447099601, "-3": 0.011328765723552264, "-4": 0.0030666574492401954, "-5": 0.0006913357748977263, "-6": 0.00013310409093068965, "-7": 2.2320683690469994e-05, "-8": 3.3114216709592057e-06, "-9": 4.4013977252850366e-07, "0": 0.16812604434114087, "1": 0.22723650800999545, "10": 9.622019863032812e-05, "11": 2.1539568058933563e-05, "12": 4.435173695791028e-06, "13": 8.452847069446955e-07, "14": 1.499203766220675e-07, "15": 2.4860908874299835e-08, "16": 3.8680376656993395e-09, "17": 5.608002666779297e-10, "18": 6.691310211114557e-11, "2": 0.20635979473222354, "3": 0.14120259032264318, "4": 0.07787906830246964, "5": 0.03577172826497317, "6": 0.014032585838150277, "7": 0.004794564979319557, "8": 0.001449277715296796, "9": 0.000392485082089406} |
| Raw goal margin distribution | {"-1": 0.09906992719027721, "-10": 7.123466532691499e-08, "-11": 7.826484278538047e-09, "-12": 7.90942565341632e-10, "-13": 7.398469964249617e-11, "-14": 6.440271200572942e-12, "-15": 5.241614548094067e-13, "-16": 4.002610791469069e-14, "-17": 2.848167110210243e-15, "-18": 1.6679115187525917e-16, "-2": 0.045374674428240606, "-3": 0.015238270778644673, "-4": 0.004124946859808216, "-5": 0.0009299125777624782, "-6": 0.00017903770179750886, "-7": 3.0023449185884337e-05, "-8": 4.454178091037966e-06, "-9": 5.920299879003379e-07, "0": 0.18764673805933016, "1": 0.20742321688210819, "10": 8.783053085844889e-05, "11": 1.96614819342259e-05, "12": 4.04846036171009e-06, "13": 7.7158232465008e-07, "14": 1.368484627204295e-07, "15": 2.2693227151217238e-08, "16": 3.5307742697983445e-09, "17": 5.119027587660501e-10, "18": 6.107878972882424e-11, "2": 0.18836679384549648, "3": 0.1288908009250026, "4": 0.07108860726890379, "5": 0.03265270627124312, "6": 0.012809051332523613, "7": 0.004376515465186676, "8": 0.0013229117473024645, "9": 0.0003582633750983442} |
| Unadjusted home-win probability | 64.7% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 16.5% |
| Raw p over 1 5 | 89.4% |
| Raw p under 3 5 | 48.3% |
| Raw p btts yes | 65.8% |
| P home draw | 87.7% |
| P draw away | 29.1% |
| P home away | 83.2% |
| Raw p home draw | 83.5% |
| Raw p draw away | 35.3% |
| Raw p home away | 81.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7335 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 5.75, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.98, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.08, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 3.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 5.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 7.09, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.12, "price": 7.09, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.34 |
| Reference draw odds | 5.75 |
| Reference away odds | 8.62 |
| Market reference 1x2 last update utc | 2026-10-30T11:50:53Z |
| Market reference home last update utc | 2026-10-30T11:50:53Z |
| Market reference draw last update utc | 2026-10-30T11:50:53Z |
| Market reference away last update utc | 2026-10-30T11:50:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.02 |
| Market reference over 2 5 last update utc | 2026-10-30T11:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:50:12Z |
| Home probability edge | -2.7% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0883 |
| Raw ev home | -0.1325 |
| Raw edge prob draw | 0.0279 |
| Raw ev draw | 0.0790 |
| Raw edge prob away | 0.0605 |
| Raw ev away | 0.4219 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.022147921647216674, 0.013080090996370806, 0.012923408130764086, 0.00595628531999328, 0.002058899698952896, 0.0005693572745575744, 0.00013120588400384125, 2.5916417034488378e-05, 4.479243384390631e-06, 6.881479803977367e-07, 9.51484083490842e-08, 1.1959927052227541e-08, 1.3780563379367943e-09, 1.4656939954450028e-10, 1.4475546245237747e-11, 1.3343304293570415e-12, 1.1530897076426476e-13, 9.378510359022417e-15, 7.204121777788283e-16, 5.242604943269911e-17], [0.04090645876193128, 0.06512794378504928, 0.03501551479818909, 0.01613834328020484, 0.00557851552370727, 0.0015426532901386156, 0.00035549767727364605, 7.021961041584112e-05, 1.2136350676526033e-05, 1.8645124836381868e-06, 2.5780122912318136e-07, 3.2404997075471556e-08, 3.733794646545079e-09, 3.9712457633330987e-10, 3.922097782823986e-11, 3.615320852059408e-12, 3.124255561153857e-13, 2.5410740335560627e-14, 1.9519311791880053e-15, 1.42046516766064e-16], [0.06544608405064609, 0.0904905762638471, 0.05491160622175714, 0.021863133634272128, 0.007557394724976104, 0.0020898821178887477, 0.0004816041578716757, 9.51287687721422e-05, 1.6441505306107833e-05, 2.525915137928142e-06, 3.4925163169091924e-07, 4.390009365758389e-08, 5.058291914045143e-09, 5.379974592855886e-10, 5.313392240066096e-11, 4.897791647318468e-12, 4.232529675143807e-13, 3.442474869050495e-14, 2.6443440615019603e-15, 1.9243499313517608e-16], [0.059107945865139594, 0.0817269995706635, 0.05650088461932591, 0.0228572922949171, 0.006825497426854361, 0.0018874870953791145, 0.0004349631136047189, 8.591600546260118e-05, 1.4849224665952085e-05, 2.2812924164729964e-06, 3.1542829244486674e-07, 3.964858092012016e-08, 4.568420692582326e-09, 4.858949952517638e-10, 4.798815780070788e-11, 4.4234641040463436e-12, 3.822629551332602e-13, 3.109087749917582e-14, 2.3882520689107327e-15, 1.7379859042429916e-16], [0.040037719388519105, 0.055359099819533526, 0.03827178445268619, 0.01763912936888762, 0.0053518994241722045, 0.001278519792358572, 0.0002946292724601886, 5.819659044728971e-05, 1.0058361555465667e-05, 1.5452701709901784e-06, 2.1366043558545666e-07, 2.685660504350221e-08, 3.0944933555234662e-09, 3.2912880303034703e-10, 3.2505551798068375e-11, 2.9963046749599023e-12, 2.589319710952435e-13, 2.1059906762704488e-14, 1.6177210147391117e-15, 1.1772527520081197e-16], [0.02169615540342059, 0.029998702499085993, 0.020739207820358523, 0.00955851876213924, 0.0033040780191883577, 0.0008019939251425483, 0.0001596575074534842, 3.153631849109979e-05, 5.450554595618441e-06, 8.373709162786876e-07, 1.157810705710144e-07, 1.4553403278988945e-08, 1.676883942484039e-09, 1.7835255772175324e-10, 1.7614527352101367e-11, 1.6236761947676499e-12, 1.4031339370961608e-13, 1.141221370456498e-14, 8.766315132630539e-16, 6.379448941339277e-17], [0.009797493598506445, 0.013546736287294315, 0.009365357690331736, 0.004316411117174165, 0.0014920469843638798, 0.00041260281157032785, 8.345872041923525e-05, 1.4241088929898506e-05, 2.461347310890956e-06, 3.781377870533903e-07, 5.228411562579856e-08, 6.571988115456475e-09, 7.572429025529291e-10, 8.053998554419622e-11, 7.954322586835886e-12, 7.332154858079292e-13, 6.336235849591774e-14, 5.153497872606266e-15, 3.958669856360676e-16, 2.880815010889727e-17], [0.003792280074955095, 0.005243485753418489, 0.0036250148067753433, 0.0016707374912160783, 0.0005775211785351447, 0.0001597046637955582, 3.6803238544928e-05, 6.380853679083616e-06, 9.527047168531953e-07, 1.4636441259311342e-07, 2.0237421737595208e-08, 2.5437954444682227e-09, 2.931032454760064e-10, 3.1174318140201406e-11, 3.0788506011804307e-12, 2.838030410044672e-13, 2.4525436756892653e-14, 1.994745605303327e-15, 1.5322678875636587e-16, 1.1150665479479432e-17], [0.001284381002091906, 0.0017758797750480016, 0.0012277310900301172, 0.000565850478020412, 0.00019559663720909403, 5.4089263469528655e-05, 1.2464633272931933e-05, 2.4620742929014248e-06, 3.735097610228396e-07, 4.9571146434684723e-08, 6.854071824164211e-09, 8.615404130249026e-10, 9.926910267705389e-11, 1.0558213312585543e-11, 1.0427545282193364e-12, 9.611928101232454e-14, 8.306349851792648e-15, 6.755865360203518e-16, 5.189531695982564e-17, 3.776541452491481e-18], [0.0003866649616658151, 0.0005346314559493118, 0.0003696104147361525, 0.00017035019440180842, 5.8884681496561746e-05, 1.6283659562009704e-05, 3.7524978482294556e-06, 7.412114166532933e-07, 1.2810668735808966e-07, 1.727508054434869e-08, 2.0634293210727172e-09, 2.59368123814702e-10, 2.9885122653407396e-11, 3.1785670600243407e-12, 3.1392292397979066e-13, 2.89368637868693e-14, 2.5006399516927992e-15, 2.0338641075100369e-16, 1.562316844474039e-17, 1.1369338643117747e-18], [0.00010476549645538473, 0.00014485649194044033, 0.00010014462760755781, 4.615577943987933e-05, 1.5954595068627613e-05, 4.411999656692046e-06, 1.0167259488003371e-06, 2.0082859773365033e-07, 3.471005141635926e-08, 5.3325192966531994e-09, 6.471772241431245e-10, 7.027487088326807e-11, 8.09726771705856e-12, 8.612214425262301e-13, 8.505630000137771e-14, 7.840340349000461e-15, 6.775395031052461e-16, 5.5106824789114377e-17, 4.233041937050263e-18, 3.0804818781202924e-19], [2.5805307943783223e-05, 3.568031946253509e-05, 2.466711886798584e-05, 1.1368858470867358e-05, 3.929855274819724e-06, 1.0867414715806687e-06, 2.5043480049179256e-07, 4.9467085861059223e-08, 8.549604553490973e-09, 1.3134792199920836e-09, 1.8161131143567393e-10, 2.0037382958370075e-11, 1.994478086885551e-12, 2.1213171591892264e-13, 2.0950638219225916e-14, 1.931193035258382e-15, 1.6688810833015527e-16, 1.3573634751903216e-17, 1.0426615099471161e-18, 7.587687375107369e-20], [5.826547023783851e-06, 8.056213071550442e-06, 5.569556788033218e-06, 2.5669598142970518e-06, 8.873169274044017e-07, 2.453739478968807e-07, 5.654534891178798e-08, 1.1169109181991012e-08, 1.93040412748388e-09, 2.9656877014290816e-10, 4.1005782548157177e-11, 5.154328658827063e-12, 5.212927086569027e-13, 4.789694510641655e-14, 4.730417440804496e-15, 4.360415716196714e-16, 3.768144960774398e-17, 3.064773392277373e-18, 2.3542119050975735e-19, 1.7132140949120045e-20], [1.2143709215288838e-06, 1.6790786810432993e-06, 1.1608089287845517e-06, 5.350066415822278e-07, 1.8493489719070267e-07, 5.1140922060765544e-08, 1.1785200940777235e-08, 2.327869552004891e-09, 4.023354878363931e-10, 6.181096440568116e-11, 8.54643920966422e-12, 1.0742669402190276e-12, 1.2378004975616237e-13, 1.1555748728339678e-14, 9.859152193155225e-16, 9.087993334494827e-17, 7.85358060235537e-18, 6.387611175993049e-19, 4.906656496545365e-20, 3.57068667037629e-21], [2.350210593666967e-07, 3.249574272430782e-07, 2.2465503688263074e-07, 1.0354153368113492e-07, 3.57910377143334e-08, 9.897464989180334e-09, 2.280827349244938e-09, 4.5051998403492274e-10, 7.786526414275375e-11, 1.1962472155386542e-11, 1.6540195102329645e-12, 2.0790629111493467e-13, 2.395554595916251e-14, 2.5479001767460196e-15, 2.2087428796355377e-16, 1.7588281991316204e-17, 1.5199283845363364e-18, 1.236214667849926e-19, 9.496008075644196e-21, 6.910463261767243e-22], [4.245208022977907e-08, 5.86973729492965e-08, 4.0579655608159746e-08, 1.8702806917773506e-08, 6.464969601661299e-09, 1.787788630194781e-09, 4.119880400562137e-10, 8.137785847322019e-11, 1.4064877630151337e-11, 2.1607928627987844e-12, 2.9876713660996983e-13, 3.755431353458402e-14, 4.3271133308091705e-15, 4.602296620232895e-16, 4.5453387792760775e-17, 3.677610988122426e-18, 2.7454612747353806e-19, 2.2329864567120288e-20, 1.7152730813832833e-21, 1.2482436323110814e-22], [7.188900116647527e-09, 9.939902802362554e-09, 6.871820870874063e-09, 3.1671618941891793e-09, 1.0947878283454261e-09, 3.027468576942164e-10, 6.976668406322087e-11, 1.3780650868088286e-11, 2.381767863641728e-12, 3.6591196425113714e-13, 5.059368331541093e-14, 6.359504822569534e-15, 7.327599816128729e-16, 7.793599402186695e-17, 7.697146124212526e-18, 7.095094111645873e-19, 5.3818175059055885e-20, 3.7813733772859674e-21, 2.904669638824627e-22, 2.113794835342599e-23], [1.1457687789572292e-09, 1.584224305807653e-09, 1.0952326059171784e-09, 5.047830902340138e-10, 1.7448757013549114e-10, 4.825187328311406e-11, 1.1119432335121793e-11, 2.1963637360604544e-12, 3.796067844321326e-13, 5.831914447037554e-14, 8.06363446628053e-15, 1.0135795402768936e-15, 1.1678747733009675e-16, 1.2421459090865074e-17, 1.2267731604409992e-18, 1.1308179533697787e-19, 9.772201207136732e-21, 6.976446502028261e-22, 4.629470059882048e-23, 3.3689717316395624e-24], [1.7246776473328897e-10, 2.3846663469697464e-10, 1.6486076673992017e-10, 7.598287965836806e-11, 2.6264881490661133e-11, 7.2631519397014735e-12, 1.6737614736603844e-12, 3.306094135715164e-13, 5.714061579526189e-14, 8.778536012403323e-15, 1.2137850477051838e-15, 1.5256987352199093e-16, 1.7579528726810715e-17, 1.869750095719323e-18, 1.8466101424810225e-19, 1.7021727971629315e-20, 1.4709684272010826e-21, 1.1963937012761548e-22, 8.066634919114506e-24, 5.071171729206308e-25], [2.4594488206058725e-11, 3.4006150909783484e-11, 2.350970449171799e-11, 1.0835416348730664e-11, 3.745461182584184e-12, 1.0357501008727424e-12, 2.386840630036313e-13, 4.714602369591219e-14, 8.148445614963365e-15, 1.2518490093345688e-15, 1.7308986457057957e-16, 2.1756981432091406e-17, 2.5069004205408165e-18, 2.6663270523949764e-19, 2.633328694244499e-20, 2.427356140971501e-21, 2.0976508676985776e-22, 1.7060979958395615e-23, 1.3105426401800013e-24, 8.371212069008319e-26]] |
| Legacy trial inputs | {"lambda_home": 2.709464441878524, "lambda_away": 1.3826736553682886, "rho": -0.11082685883326926, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6920 |
| Legacy p draw | 0.1713 |
| Legacy p away | 0.1367 |
| Legacy p over 1 5 | 0.9239 |
| Legacy p under 3 5 | 0.4102 |
| Legacy p btts yes | 0.7005 |
| Legacy p over 2 5 | 0.7804 |
| Legacy goal margin distribution | {"-1": 0.0782376596560392, "-10": 1.3313178697198184e-07, "-11": 1.628284924442879e-08, "-12": 1.8330090519772625e-09, "-13": 1.9109239732161792e-10, "-14": 1.8546892457814867e-11, "-15": 1.6836867115070436e-12, "-16": 1.4353785375175167e-13, "-17": 1.1522876531345599e-14, "-18": 8.624586945448923e-16, "-19": 5.242604943269911e-17, "-2": 0.03883541365575309, "-3": 0.014123692487753869, "-4": 0.004180023815343299, "-5": 0.0010365008724823835, "-6": 0.0002203772954707311, "-7": 4.092272834788564e-05, "-8": 6.735937173192776e-06, "-9": 9.94765225633907e-07, "0": 0.17128888832494252, "1": 0.20929312878368708, "10": 0.00014658803019532008, "11": 3.51326506524489e-05, "12": 7.750128309236681e-06, "13": 1.5832571556804492e-06, "14": 3.011223369086928e-07, "15": 5.356694397889975e-08, "16": 8.94882060554383e-09, "17": 1.407745118145922e-09, "18": 2.0647391564307247e-10, "19": 2.4594488206058725e-11, "2": 0.19666838039461915, "3": 0.1401582372455885, "4": 0.08128546555286609, "5": 0.039497315675176795, "6": 0.01645616092619321, "7": 0.005988113523561779, "8": 0.0019314667666156385, "9": 0.0005589507908079676} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6483 |
| Legacy raw p draw | 0.1828 |
| Legacy raw p away | 0.1689 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.7095 |
| Legacy lambda away | 1.3827 |
| Legacy model home team | Bayern Munich |
| Legacy model away team | Dortmund |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 87.6% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:50:54Z |
| Market reference home draw last update utc | 2026-10-30T11:50:59Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 27.9% |
| Market draw away odds | 3.50 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:50:54Z |
| Market reference draw away last update utc | 2026-10-30T11:50:59Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.5% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:50:54Z |
| Market reference home away last update utc | 2026-10-30T11:50:59Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.10 |
| Market reference dc draw away odds | 3.45 |
| Market reference dc home away odds | 1.14 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.11, "price": 1.7, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.7, "price": 2.11, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.15, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.15, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 92.5% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 9.50 |
| Market reference over 1 5 last update utc | 2026-10-30T11:50:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 40.9% |
| Market under 3 5 odds | 2.30 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market reference under 3 5 odds | 2.30 |
| Market reference under 3 5 opposite odds | 1.63 |
| Market reference under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.9% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:50:54Z |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.75 |
| Market reference btts yes last update utc | 2026-10-30T11:50:54Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.05076922801949, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,725.3258 |
| Elo away rating | 1,617.6463 |
| Elo rating diff | 167.6795 |
| Elo home expectancy | 0.7242 |

</details>


---

## 2026-10-31 — Borussia Monchengladbach vs SC Paderborn

The model's most likely 1X2 outcome is **Borussia Monchengladbach win** at **48.2%**. Expected goals are 1.45 for Borussia Monchengladbach and 0.99 for SC Paderborn (2.44 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 64.1%; Under 3.5 goals: 57.3%; Double Chance 1X: 73.5%; Double Chance X2: 51.8%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 75.9%; BTTS Yes (both teams score): 65.4%; BTTS No (at least one team does not score): 34.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 48.2% | 2.07 |
| Draw | 25.3% | 3.95 |
| SC Paderborn win | 26.5% | 3.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.45 |
| SC Paderborn expected goals | 0.99 |
| Expected total goals | 2.44 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 64.1% |
| Under 2.5 | 35.9% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.1% |
| Under 4.5 | 75.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.18% |
| 2 | 2-1 | 8.86% |
| 3 | 2-2 | 7.02% |
| 4 | 1-2 | 6.72% |
| 5 | 2-0 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 48.2% | 48.8% | 2.00 | -3.6% |
| Draw | 25.3% | 24.0% | 3.97 | +0.5% |
| SC Paderborn win | 26.5% | 27.1% | 3.53 | -6.6% |

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
| Market best home last update utc | 2026-10-30T11:50:53Z |
| Market best draw last update utc | 2026-10-30T11:50:53Z |
| Market best away last update utc | 2026-10-30T11:50:53Z |
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
| Dc lambda away | 0.8762 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:50:54.576591+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9453 |
| Shot lambda away | 1.4507 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 65.4% |
| P btts no | 34.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.63 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.79 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.15 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.14767627902957742, "-10": 2.7566523733601724e-07, "-11": 3.3375100085626526e-08, "-12": 3.7151508356464388e-09, "-13": 3.8264635111394505e-10, "-14": 3.666501372312752e-11, "-15": 3.2823579673503736e-12, "-16": 2.732069166905809e-13, "-17": 1.884132335596564e-14, "-2": 0.07655966258657322, "-3": 0.02889006038772881, "-4": 0.008726369221272512, "-5": 0.002185750405888394, "-6": 0.00046627397015978477, "-7": 8.64724434264431e-05, "-8": 1.4168640078705325e-05, "-9": 2.077911303112393e-06, "0": 0.2532667766911285, "1": 0.19793660513726846, "10": 1.1151061393735128e-05, "11": 1.9747747369712567e-06, "12": 3.215379354796767e-07, "13": 4.8441114489050586e-08, "14": 6.789365420696615e-09, "15": 8.890456409275678e-10, "16": 1.082406985676997e-10, "17": 1.091870372012351e-11, "2": 0.14779098985558947, "3": 0.08157501811064524, "4": 0.036041519780512524, "5": 0.013204770609446755, "6": 0.004120332340605136, "7": 0.0011177111631898698, "8": 0.00026788031928353, "9": 5.7464605196975295e-05} |
| Raw goal margin distribution | {"-1": 0.1558636527673419, "-10": 2.499194659902522e-08, "-11": 2.2277403265187893e-09, "-12": 1.8232552371887097e-10, "-13": 1.3790221340237563e-11, "-14": 9.658837397405938e-13, "-15": 5.824039590637929e-14, "-2": 0.06731331198777729, "-3": 0.019997500642713602, "-4": 0.004636536525677836, "-5": 0.0008783440716121051, "-6": 0.00014040230380286153, "-7": 1.9390987771281512e-05, "-8": 2.35600996085085e-06, "-9": 2.5542283899334705e-07, "0": 0.2834756915943044, "1": 0.2322522815395958, "10": 1.1204897940643177e-06, "11": 1.4609426556473825e-07, "12": 1.7489478294539073e-08, "13": 1.9349128287610798e-09, "14": 1.9823293186265362e-10, "15": 1.7483808858290906e-11, "2": 0.14401990617936508, "3": 0.06258324323040067, "4": 0.021224468024152746, "5": 0.005881235700279791, "6": 0.001375114705831229, "7": 0.0002777956284249188, "8": 4.937002861919257e-05, "9": 7.82900853518389e-06} |
| Unadjusted home-win probability | 46.8% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 24.9% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.1% |
| P home draw | 73.5% |
| P draw away | 51.8% |
| P home away | 74.7% |
| Raw p home draw | 75.1% |
| Raw p draw away | 53.2% |
| Raw p home away | 71.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.3708 |
| Totals anchor target over 2 5 | 0.6414 |
| Totals anchor reference over odds | 1.51 |
| Totals anchor reference under odds | 2.59 |
| Totals anchor reference last update utc | 2026-10-30T11:50:53Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4515 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.67, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.66, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.56, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.51, "price": 2.67, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.00 |
| Reference draw odds | 3.97 |
| Reference away odds | 3.53 |
| Market reference 1x2 last update utc | 2026-10-30T11:50:53Z |
| Market reference home last update utc | 2026-10-30T11:50:53Z |
| Market reference draw last update utc | 2026-10-30T11:50:53Z |
| Market reference away last update utc | 2026-10-30T11:50:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Market reference over 2 5 last update utc | 2026-10-30T11:50:11Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:50:11Z |
| Home probability edge | -0.6% |
| Draw probability edge | +1.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0206 |
| Raw ev home | -0.0647 |
| Raw edge prob draw | 0.0432 |
| Raw ev draw | 0.1254 |
| Raw edge prob away | -0.0225 |
| Raw ev away | -0.1216 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10782421791559614, 0.08613531702104124, 0.04305894883172664, 0.01212605519351949, 0.0025611612431177986, 0.00043275718664083406, 6.09355043838461e-05, 7.35444225169179e-06, 7.766710673495642e-07, 7.290746356965727e-08, 6.159555339263878e-09, 4.730794117744948e-10, 3.330659023118359e-11, 2.1645329113258885e-12, 1.3062115805225514e-13], [0.13488608682100275, 0.12512438023752845, 0.0602148701784703, 0.016957423696250095, 0.0035816014079478797, 0.0006051800733504561, 8.521395866100077e-05, 1.0284663175390386e-05, 1.086119117180331e-06, 1.0195589007629807e-07, 8.613699014352024e-09, 6.615678305439489e-10, 4.657689194169316e-11, 3.0269449624018677e-12, 1.8266437727998286e-13], [0.10405734242424326, 0.08791239301672936, 0.03327003660738086, 0.011856874054466674, 0.0025043071145724473, 0.00042315059401246407, 5.95828230528583e-05, 7.19118411779623e-06, 7.594300768343428e-07, 7.12890218113169e-08, 6.022821991458566e-09, 4.625777232293239e-10, 3.256723140811087e-11, 2.1164833663345878e-12, 1.277215545498981e-13], [0.04850559163809776, 0.040979738058387595, 0.017310776702443697, 0.00436745533312086, 0.0011673649874757257, 0.00019724864614460044, 2.7774110085033725e-05, 3.352119438050649e-06, 3.5400294036371287e-07, 3.323087155312124e-08, 2.8074957251510688e-09, 2.1562732260030387e-10, 1.5180983779355303e-11, 9.865836997614304e-13, 5.95364961669156e-14], [0.016957902960150078, 0.014326810535812253, 0.006051971774204693, 0.0017043273408837978, 0.00032249738106533883, 6.895954234096817e-05, 9.710028219851608e-06, 1.1719250136235424e-06, 1.2376196862179046e-07, 1.1617751192141553e-08, 9.815206548424873e-10, 7.538485953320348e-11, 5.30738088282012e-12, 3.4491674212421356e-13, 2.0814386351962774e-14], [0.004742883665065949, 0.0040070046291972245, 0.0016926502136949137, 0.00047667605623163175, 0.00010067942304890295, 1.52406639178145e-05, 2.71575644344034e-06, 3.277707165124678e-07, 3.461445797349342e-08, 3.249319357676109e-09, 2.7451733222655907e-10, 2.108407034251348e-11, 1.4843987580636606e-12, 9.646829480466724e-14, 5.82148708239938e-15], [0.0011054307792464579, 0.0009339183843624933, 0.0003945084418785621, 0.00011109958023415574, 2.3465499247805192e-05, 3.96494498926623e-06, 5.001716686824656e-07, 7.639399659690134e-08, 8.06764195644688e-09, 7.573235784872569e-10, 6.398215303382195e-11, 4.914094874407537e-12, 3.4597097287562716e-13, 2.2484005476237532e-14, 1.3568224431202559e-15], [0.00022083801947132912, 0.00018657403993316336, 7.881313294765562e-05, 2.219497749079488e-05, 4.687832541919759e-06, 7.920989854644762e-07, 1.1153356360380839e-07, 1.2059816813781892e-08, 1.6117174452841134e-09, 1.5129471904706006e-10, 1.2782068513717847e-11, 9.817159065338623e-13, 6.91165343672669e-14, 4.491754103806971e-15, 2.7105992228403708e-16], [3.860327827818034e-05, 3.2613811699028135e-05, 1.3776818459235307e-05, 3.879761711802255e-06, 8.194499505585917e-07, 1.3846174509692756e-07, 1.9496467154804937e-08, 2.353072207276747e-09, 2.2262731052324509e-10, 2.644685980871616e-11, 2.2343514444978883e-12, 1.7160746333791002e-13, 1.208181823125531e-14, 7.85174735951346e-16, 4.738224711053936e-17], [5.998214729269689e-06, 5.067565617123021e-06, 2.1406553818867795e-06, 6.02841128623593e-07, 1.2732692617243583e-07, 2.1514319921119527e-08, 3.0293799302214636e-09, 3.656226362697358e-10, 3.8611836688697113e-11, 3.2472155922739306e-12, 3.4717568928148514e-13, 2.6664533691374886e-14, 1.8772846064743774e-15, 1.2200121016395198e-16, 7.362299400488385e-18], [8.388075673585343e-07, 7.086629238173764e-07, 2.9935539397603825e-07, 8.430303405726803e-08, 1.7805762884874966e-08, 3.0086242608731605e-09, 4.2363718615709154e-10, 5.112971908192621e-11, 5.3995900890387765e-12, 5.068689104785382e-13, 3.8364436749105695e-14, 3.72884493969009e-15, 2.625248686600655e-16, 1.706099946923402e-17, 1.0295650837829808e-18], [1.0663750750923399e-07, 9.009223426305839e-08, 3.805701607291859e-08, 1.0717434817192774e-08, 2.2636445440315156e-09, 3.824860488820446e-10, 5.385694571435364e-11, 6.500115181022702e-12, 6.864492537661412e-13, 6.443818505067095e-14, 5.444032028382358e-15, 3.7459429503056634e-16, 3.337475571573189e-17, 2.1689628584834078e-18, 1.3088848816527753e-19], [1.2427079320023088e-08, 1.0498963896058625e-08, 4.435001984462176e-09, 1.24896404362132e-09, 2.6379545957205775e-10, 4.4573289260796036e-11, 6.276258250583128e-12, 7.574956394855782e-13, 7.999586191550672e-14, 7.509350655009194e-15, 6.344242229367137e-16, 4.8726413137195713e-17, 3.0733807699375938e-18, 2.527616606401206e-19, 1.525318494871009e-20], [1.3367988058865039e-09, 1.129388655038424e-09, 4.770795457449689e-10, 1.3435285951848723e-10, 2.8376857206183277e-11, 4.794812869847778e-12, 6.751461319874521e-13, 8.148489602838338e-14, 8.605269985861196e-15, 8.077916564373128e-16, 6.824592664189226e-17, 5.241570381866259e-18, 3.690264943509005e-19, 2.148559414110138e-20, 1.6408070553269601e-21], [1.3352984477456514e-10, 1.1281210839908502e-10, 4.765440948026576e-11, 1.3420206838549271e-11, 2.8345008398020353e-12, 4.789431404445907e-13, 6.74388380715584e-14, 8.13934413333505e-15, 8.595611848211263e-16, 8.0688503026252e-17, 6.816933072396782e-18, 5.23568749750202e-19, 3.686123169125668e-20, 2.395542401486428e-21, 1.2951169853317103e-22]] |
| Legacy trial inputs | {"lambda_home": 1.3984287079043336, "lambda_away": 0.8448456492220346, "rho": -0.11082685883326926, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4869 |
| Legacy p draw | 0.2709 |
| Legacy p away | 0.2422 |
| Legacy p over 1 5 | 0.6712 |
| Legacy p under 3 5 | 0.8098 |
| Legacy p btts yes | 0.4373 |
| Legacy p over 2 5 | 0.3989 |
| Legacy goal margin distribution | {"-1": 0.15944617957275017, "-10": 6.854697799302051e-09, "-11": 5.218323235786894e-10, "-12": 3.646125674813536e-11, "-13": 2.3471972886058714e-12, "-14": 1.3062115805225514e-13, "-2": 0.0627279743088281, "-3": 0.016159788615315612, "-4": 0.003229403335223217, "-5": 0.000525528229612523, "-6": 7.201383146285925e-05, "-7": 8.514734778421943e-06, "-8": 8.848708119459213e-07, "-9": 8.199927202924719e-08, "0": 0.27092434059600823, "1": 0.24191834217485778, "10": 9.334719909664131e-07, "11": 1.1762697115787613e-07, "12": 1.3604122384541778e-08, "13": 1.4496109142855889e-09, "14": 1.3352984477456514e-10, "2": 0.15159000577885495, "3": 0.06464098134332978, "4": 0.02138245240320525, "5": 0.0057596253342614605, "6": 0.0013064026733750167, "7": 0.00025567909848742007, "8": 4.398118538180787e-05, "9": 6.746212489003953e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4855 |
| Legacy raw p draw | 0.3015 |
| Legacy raw p away | 0.2130 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3984 |
| Legacy lambda away | 0.8448 |
| Legacy model home team | M'gladbach |
| Legacy model away team | Paderborn |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 72.3% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:50:54Z |
| Market reference home draw last update utc | 2026-10-30T11:50:59Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.4% |
| Market draw away odds | 1.87 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:50:54Z |
| Market reference draw away last update utc | 2026-10-30T11:50:59Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:50:54Z |
| Market reference home away last update utc | 2026-10-30T11:50:59Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.87 |
| Market reference dc home away odds | 1.26 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.32, "price": 1.57, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.57, "price": 2.32, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.85, "price": 1.96, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.96, "price": 1.85, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.52, "price": 2.45, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.45, "price": 1.52, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 85.4% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-10-30T11:50:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.9% |
| Market under 3 5 odds | 1.68 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.27 |
| Market reference under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.5% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:50:54Z |
| Market reference btts yes odds | 1.49 |
| Market reference btts yes opposite odds | 2.72 |
| Market reference btts yes last update utc | 2026-10-30T11:50:54Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.201980448238338, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,420.8820 |
| Elo away rating | 1,406.2048 |
| Elo rating diff | 74.6772 |
| Elo home expectancy | 0.6058 |

</details>


---

## 2026-10-31 — FC Schalke 04 vs RB Leipzig

The model's most likely 1X2 outcome is **RB Leipzig win** at **53.7%**. Expected goals are 0.87 for FC Schalke 04 and 1.62 for RB Leipzig (2.49 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 66.5%; Under 3.5 goals: 54.1%; Double Chance 1X: 46.3%; Double Chance X2: 78.9%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 73.4%; BTTS Yes (both teams score): 65.5%; BTTS No (at least one team does not score): 34.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 21.1% | 4.73 |
| Draw | 25.1% | 3.98 |
| RB Leipzig win | 53.7% | 1.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| RB Leipzig expected goals | 1.62 |
| Expected total goals | 2.49 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 86.8% |
| Under 1.5 | 13.2% |
| Over 2.5 | 66.5% |
| Under 2.5 | 33.5% |
| Over 3.5 | 45.9% |
| Under 3.5 | 54.1% |
| Over 4.5 | 26.6% |
| Under 4.5 | 73.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.92% |
| 2 | 1-2 | 8.47% |
| 3 | 2-2 | 7.16% |
| 4 | 0-2 | 6.89% |
| 5 | 1-3 | 6.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 21.1% | 22.0% | 4.33 | -8.4% |
| Draw | 25.1% | 24.5% | 3.89 | -2.3% |
| RB Leipzig win | 53.7% | 53.5% | 1.83 | -1.7% |

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
| Market best home last update utc | 2026-10-30T11:50:53Z |
| Market best draw last update utc | 2026-10-30T11:50:53Z |
| Market best away last update utc | 2026-10-30T11:50:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Schalke 04 |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7503 |
| Dc lambda away | 1.5472 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:50:54.576591+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.3534 |
| Shot lambda away | 1.9243 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 65.5% |
| P btts no | 34.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.94 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.56 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 2.98 |
| Fair Over 3.5 odds | 2.18 |
| Fair Under 3.5 odds | 1.85 |
| Fair Over 4.5 odds | 3.75 |
| Fair Under 4.5 odds | 1.36 |
| Goal margin distribution | {"-1": 0.18990392546563478, "-10": 3.705462643064533e-05, "-11": 7.557362031360532e-06, "-12": 1.417309323649976e-06, "-13": 2.459626494070273e-07, "-14": 3.971469539997015e-08, "-15": 5.994657619648734e-09, "-16": 8.489991549382228e-10, "-17": 1.1223919635866459e-10, "-18": 1.2350275433443988e-11, "-2": 0.16111936620353462, "-3": 0.1018514096960286, "-4": 0.05164097390885839, "-5": 0.02173878424240569, "-6": 0.007799961334836684, "-7": 0.002434318376410414, "-8": 0.0006714896291533969, "-9": 0.0001658320082781182, "0": 0.25117509885730566, "1": 0.12582620776064726, "10": 9.309870725912161e-08, "11": 1.0191685510026826e-08, "12": 1.0259235662371135e-09, "13": 9.556395159425532e-11, "14": 8.282296016211591e-12, "15": 6.710246458891181e-13, "16": 5.1010070184691903e-14, "17": 3.619660069493221e-15, "18": 2.137836348984771e-16, "2": 0.058756017794752056, "3": 0.01993637658021921, "4": 0.005425605136654522, "5": 0.0012259241118434282, "6": 0.00023609965905847005, "7": 3.955076270345855e-05, "8": 5.855869237098054e-06, "9": 7.76238173013424e-07} |
| Raw goal margin distribution | {"-1": 0.2453026033150293, "-10": 3.2730448046219087e-06, "-11": 4.777389168518878e-07, "-12": 6.402306626808465e-08, "-13": 7.928970350781306e-09, "-14": 9.094305233813943e-10, "-15": 8.990656820330662e-11, "-2": 0.16994607308315604, "-3": 0.08278658782207483, "-4": 0.03145687940601581, "-5": 0.009763184565773813, "-6": 0.002556375568760655, "-7": 0.000578256986435907, "-8": 0.0001150620655303287, "-9": 2.0427856806219784e-05, "0": 0.2649104131458789, "1": 0.1276805632384595, "10": 6.496773162054238e-09, "11": 5.089919911794845e-10, "12": 3.661266768006999e-11, "13": 2.433807767498456e-12, "14": 1.498351064294812e-13, "15": 7.95078574155928e-15, "2": 0.04896212794852985, "3": 0.012802173503659914, "4": 0.002611042486389904, "5": 0.0004349750792618577, "6": 6.113249347474009e-05, "7": 7.422375398344941e-06, "8": 7.9273634212427e-07, "9": 7.554295736518684e-08} |
| Unadjusted home-win probability | 19.3% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 54.3% |
| Raw p over 1 5 | 72.0% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 47.5% |
| P home draw | 46.3% |
| P draw away | 78.9% |
| P home away | 74.9% |
| Raw p home draw | 45.7% |
| Raw p draw away | 80.7% |
| Raw p home away | 73.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.4116 |
| Totals anchor target over 2 5 | 0.6646 |
| Totals anchor reference over odds | 1.46 |
| Totals anchor reference under odds | 2.75 |
| Totals anchor reference last update utc | 2026-10-30T11:50:53Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4587 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.7, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.0, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.68, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.95, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 4.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 7.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:39Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.28, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.28, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.33 |
| Reference draw odds | 3.89 |
| Reference away odds | 1.83 |
| Market reference 1x2 last update utc | 2026-10-30T11:50:53Z |
| Market reference home last update utc | 2026-10-30T11:50:53Z |
| Market reference draw last update utc | 2026-10-30T11:50:53Z |
| Market reference away last update utc | 2026-10-30T11:50:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-10-30T11:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:50:12Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0270 |
| Raw ev home | -0.1662 |
| Raw edge prob draw | 0.0196 |
| Raw ev draw | 0.0305 |
| Raw edge prob away | 0.0074 |
| Raw ev away | -0.0072 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.06657192137020919, 0.09036309144966664, 0.10277133790245718, 0.07025702690551326, 0.036022080161252794, 0.014775350638037282, 0.0050503974576074796, 0.0014796756593170458, 0.0003793285708222201, 8.643946243579223e-05, 1.772764594291908e-05, 3.3051973529602498e-06, 5.648786521961983e-07, 8.91150021659647e-08, 1.3054546765060901e-08, 1.7848821705185503e-09, 2.2878554450958682e-10, 2.760060941961421e-11], [0.046058505681657695, 0.11201702157599396, 0.09122042820937416, 0.06236053952242274, 0.031973404690135085, 0.013114685861389237, 0.004482761712684427, 0.001313368590978145, 0.0003366942123035796, 7.672416199412498e-05, 1.5735160085121253e-05, 2.9337121030737833e-06, 5.013895273853328e-07, 7.909898638445424e-08, 1.1587290486754322e-08, 1.5842716385818948e-09, 2.0307135981909176e-10, 2.4498459020612767e-11], [0.026453582930650976, 0.05425296952356408, 0.04589197685949689, 0.0276757860445592, 0.014189888575324274, 0.005820335146569832, 0.001989462487000883, 0.000582876742246363, 0.0001494258557337325, 3.4050402835818963e-05, 6.98330911226512e-06, 1.3019898336801537e-06, 2.2251810826475717e-07, 3.5104356701893536e-08, 5.142472704750423e-09, 7.031042906562766e-10, 9.012365109686169e-11, 1.0872486278475663e-11], [0.007826783912898988, 0.016051748838983495, 0.016460058413339602, 0.009282252215188044, 0.00419834212697494, 0.0017220542719024534, 0.0005886194331178014, 0.0001724549117363944, 4.4210415159787304e-05, 1.0074444200688082e-05, 2.0661417231065625e-06, 3.852178781120252e-07, 6.583611583583922e-08, 1.0386276030257461e-08, 1.5214960764890349e-09, 2.0802646528544858e-10, 2.6664756317728798e-11, 3.2168270332480906e-12], [0.0017367745584730215, 0.0035619060539796446, 0.0036525105332414175, 0.00249694648375768, 0.0010560694765494722, 0.00038212630897103495, 0.000130615495130382, 3.8267991875163686e-05, 9.810354434661846e-06, 2.2355335950536486e-06, 4.5847980713727927e-07, 8.548039879717596e-08, 1.4609128383361315e-08, 2.3047295245880814e-09, 3.376221582031534e-10, 4.616137054728231e-11, 5.916947611673744e-12, 7.138185252752404e-13], [0.00030831420931276587, 0.0006323136433116671, 0.0006483978542689881, 0.0004432608003613835, 0.00022726802977917983, 7.689738832820597e-05, 2.318701233194319e-05, 6.7933777584534515e-06, 1.7415453582300603e-06, 3.968544848774609e-07, 8.138986060901319e-08, 1.5174578322970403e-08, 2.5934292071993735e-09, 4.0913822556101136e-10, 5.993507231266352e-11, 8.194619383181171e-12, 1.0503833186283898e-12, 1.2671788237532442e-13], [4.561024304143179e-05, 9.354086862925591e-05, 9.592027492560626e-05, 6.557347090906581e-05, 3.362073417531118e-05, 1.3790378954372673e-05, 3.8883754960969505e-06, 1.0049735019542928e-06, 2.5763427262598604e-07, 5.870838566827529e-08, 1.2040351081320215e-08, 2.2448404402270447e-09, 3.8365710329982344e-10, 6.052557210053053e-11, 8.866452250059124e-12, 1.2122651840537324e-12, 1.5538770839039266e-13, 1.8745919708718417e-14], [5.783416140683602e-06, 1.1861058687027347e-05, 1.2162769352481516e-05, 8.314769770282566e-06, 4.263136605400197e-06, 1.7486313361324002e-06, 5.977038021392748e-07, 1.4445455005894774e-07, 3.266823659205025e-08, 7.444271344025763e-09, 1.526726369775087e-09, 2.8464760478199854e-10, 4.8648034646439824e-11, 7.674692070646084e-12, 1.1242734007580645e-12, 1.5371621733908316e-13, 1.9703288578236497e-14, 2.3769979589207114e-15], [6.416741618257536e-07, 1.3159929540302334e-06, 1.3494679683919546e-06, 9.22529659518766e-07, 4.729980588420042e-07, 1.9401189879142582e-07, 6.631566481267448e-08, 1.942929757081482e-08, 4.1087560844426995e-09, 8.259472358350108e-10, 1.6939138388663629e-10, 3.1581855562724186e-11, 5.397534276780354e-12, 8.515125804383997e-13, 1.2473893881154275e-13, 1.7054924377000262e-14, 2.1860939756198195e-15, 2.6372962551017263e-16], [6.328374018076314e-08, 1.2978698713004934e-07, 1.3308838874077797e-07, 9.098251223942357e-08, 4.664842071339477e-08, 1.9134008076870547e-08, 6.540240439133472e-09, 1.9161728685906846e-09, 4.912286764427178e-10, 9.233884748102367e-11, 1.6705862514770756e-11, 3.114692878035115e-12, 5.323202602028508e-13, 8.397860488536833e-14, 1.2302110734384505e-14, 1.6820053966419981e-15, 2.1559883722016464e-16, 2.6009769586589398e-17], [5.617101028167087e-09, 1.1519967321282263e-08, 1.1813001619334914e-08, 8.075659902298902e-09, 4.140540543323191e-09, 1.698345517103582e-09, 5.805154877094935e-10, 1.7008060142403576e-10, 4.360173870302167e-11, 9.935742110291619e-12, 1.6809065052536349e-12, 2.764619239896634e-13, 4.724905121534722e-14, 7.45398907362671e-15, 1.0919423955877707e-15, 1.4929576247979634e-16, 1.913667628938823e-17, 2.3086420472289245e-18], [4.532519134602264e-10, 9.29562634744754e-10, 9.532079912437411e-10, 6.516365443342213e-10, 3.3410613670825664e-10, 1.3704192811981202e-10, 4.684262474151777e-11, 1.3724046915187014e-11, 3.5182866390042647e-12, 8.017292372977889e-13, 1.6442457715952469e-13, 2.5288163801413687e-14, 3.812593500659274e-15, 6.014730362852979e-16, 8.81103931915569e-17, 1.2046888541997981e-17, 1.544165771977308e-18, 1.8628762775568116e-19], [3.352574955594014e-11, 6.875709327093045e-11, 7.050607276027027e-11, 4.819969411726369e-11, 2.4712876728686175e-11, 1.0136600032712575e-11, 3.46481517008492e-12, 1.015128554582281e-12, 2.602376144973913e-13, 5.93016219526213e-14, 1.2162016377621555e-14, 2.267524095833498e-15, 3.1967885582479565e-16, 4.4489242693337886e-17, 6.517274142020287e-18, 8.910739396642183e-19, 1.1421753203190623e-19, 1.3779163789575963e-20], [2.289049795812601e-12, 4.694553064350651e-12, 4.81396877305162e-12, 3.290948045568859e-12, 1.687330072526837e-12, 6.921003271350736e-13, 2.365684455280445e-13, 6.931030152548513e-14, 1.7768338253975456e-14, 4.048958410176766e-15, 8.303904155643698e-16, 1.548205673942393e-16, 2.645979168644226e-17, 3.4433908083243432e-18, 4.449822969402639e-19, 6.084017946381482e-20, 7.798471975685629e-21, 9.408049775701056e-22], [1.451266936234623e-13, 2.9763658506487113e-13, 3.052075898556698e-13, 2.086474525865248e-13, 1.0697741697241094e-13, 4.3879443914488277e-14, 1.4998536238893582e-14, 4.394301475153387e-15, 1.1265199152503932e-15, 2.5670561984400407e-16, 5.264709210255025e-17, 9.815687317915308e-18, 1.6775616189929818e-18, 2.6465136667649225e-19, 3.198080216229731e-20, 3.857292270877435e-21, 4.944263140176528e-22, 5.964742051003547e-23], [8.587685637609634e-15, 1.7612262520225624e-14, 1.8060267001557682e-14, 1.234644493831051e-14, 6.3302512056543424e-15, 2.5965097176983324e-15, 8.87519111942965e-16, 2.6002714403052276e-16, 6.666036864160335e-17, 1.519022524104163e-17, 3.1153240346260442e-18, 5.8083068592489925e-19, 9.926755348681181e-20, 1.5660404601225234e-20, 2.294108503142139e-21, 2.587414114875234e-22, 2.9257041897213254e-23, 3.529559474175759e-24], [4.764049352053786e-16, 9.770465686379855e-16, 1.0018997776290087e-15, 6.849234530771447e-16, 3.5117295191338164e-16, 1.4404230616021054e-16, 4.923544047385671e-17, 1.442509890685543e-17, 3.698007815329076e-18, 8.426831834668629e-19, 1.728237161313803e-19, 3.222179024363648e-20, 5.506903068245584e-21, 8.687665518009563e-22, 1.272664905206931e-22, 1.7400503741946145e-23, 1.8398613063985035e-24, 1.958035754399452e-25], [2.4874102905629383e-17, 5.1013654762867275e-17, 5.23112930371461e-17, 3.5761292957587257e-17, 1.833547786359808e-17, 7.520751531779681e-18, 2.5706858230230935e-18, 7.531647305003675e-19, 1.930807599729472e-19, 4.399826003767533e-20, 9.023489434953068e-21, 1.682367387689417e-21, 2.87526982800493e-22, 4.536012751662573e-23, 6.644850940272727e-24, 9.085168702132942e-25, 1.1645336049690447e-25, 1.1589010371373993e-26]] |
| Legacy trial inputs | {"lambda_home": 0.8876057281258103, "lambda_away": 2.0508741543930062, "rho": -0.11082685883326926, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1812 |
| Legacy p draw | 0.2349 |
| Legacy p away | 0.5839 |
| Legacy p over 1 5 | 0.7970 |
| Legacy p under 3 5 | 0.6678 |
| Legacy p btts yes | 0.5298 |
| Legacy p over 2 5 | 0.5558 |
| Legacy goal margin distribution | {"-1": 0.2138639996365499, "-10": 2.089460840483017e-05, "-11": 3.8432599636237515e-06, "-12": 6.493341814161825e-07, "-13": 1.0143277551821833e-07, "-14": 1.4732158881772905e-08, "-15": 1.9988260166161177e-09, "-16": 2.532840035301996e-10, "-17": 2.760060941961421e-11, "-2": 0.18118149439609338, "-3": 0.10867945597980314, "-4": 0.05130890296078016, "-5": 0.01988751872593596, "-6": 0.006523740394363741, "-7": 0.0018525745516746739, "-8": 0.00046343628709571175, "-9": 0.00010354481436725857, "0": 0.23490017591861334, "1": 0.11951015614548344, "10": 6.620570307632976e-09, "11": 5.270380998209925e-10, "12": 3.853821534878822e-11, "13": 2.605449906809971e-12, "14": 1.6377661721427452e-13, "15": 9.617043499284767e-15, "16": 5.274185899682458e-16, "17": 2.4874102905629383e-17, "2": 0.04663654074500219, "3": 0.012107125154460349, "4": 0.00247381597305137, "5": 0.000414988771596034, "6": 5.8916033326829316e-05, "7": 7.240917627123913e-06, "8": 7.839512073588334e-07, "9": 7.580684729906015e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1429 |
| Legacy raw p draw | 0.2245 |
| Legacy raw p away | 0.6326 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.8876 |
| Legacy lambda away | 2.0509 |
| Legacy model home team | Schalke 04 |
| Legacy model away team | RB Leipzig |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 47.5% |
| Market home draw odds | 2.07 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:49:37Z |
| Market reference home draw last update utc | 2026-10-30T11:50:59Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.0% |
| Market draw away odds | 1.24 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:49:37Z |
| Market reference draw away last update utc | 2026-10-30T11:50:59Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.4% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:49:37Z |
| Market reference home away last update utc | 2026-10-30T11:50:59Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.02 |
| Market reference dc draw away odds | 1.28 |
| Market reference dc home away odds | 1.24 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:49:37Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.47, "price": 1.51, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:49:37Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.47, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:49:37Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.95, "price": 1.85, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:49:37Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.85, "price": 1.95, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:49:37Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.58, "price": 2.3, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:49:37Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.3, "price": 1.58, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 87.6% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-30T11:50:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 55.0% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market reference under 3 5 odds | 1.76 |
| Market reference under 3 5 opposite odds | 2.13 |
| Market reference under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.8% |
| Market btts yes odds | 1.44 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:49:37Z |
| Market reference btts yes odds | 1.41 |
| Market reference btts yes opposite odds | 2.73 |
| Market reference btts yes last update utc | 2026-10-30T11:50:54Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.281793634485094, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,439.0953 |
| Elo away rating | 1,517.4051 |
| Elo rating diff | -18.3098 |
| Elo home expectancy | 0.4737 |

</details>


---

## 2026-10-31 — Werder Bremen vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **39.9%**. Expected goals are 1.77 for Werder Bremen and 1.65 for TSG Hoffenheim (3.41 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 69.0%; Under 3.5 goals: 52.1%; Double Chance 1X: 60.1%; Double Chance X2: 64.1%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 71.3%; BTTS Yes (both teams score): 70.2%; BTTS No (at least one team does not score): 29.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 35.9% | 2.78 |
| Draw | 24.2% | 4.14 |
| TSG Hoffenheim win | 39.9% | 2.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.77 |
| TSG Hoffenheim expected goals | 1.65 |
| Expected total goals | 3.41 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 87.8% |
| Under 1.5 | 12.2% |
| Over 2.5 | 69.0% |
| Under 2.5 | 31.0% |
| Over 3.5 | 47.9% |
| Under 3.5 | 52.1% |
| Over 4.5 | 28.7% |
| Under 4.5 | 71.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.95% |
| 2 | 1-2 | 8.59% |
| 3 | 2-2 | 7.40% |
| 4 | 2-1 | 7.26% |
| 5 | 1-3 | 4.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 35.9% | 34.0% | 2.85 | +2.4% |
| Draw | 24.2% | 24.2% | 3.95 | -4.5% |
| TSG Hoffenheim win | 39.9% | 41.8% | 2.33 | -7.0% |

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
| Market best home last update utc | 2026-10-30T11:50:53Z |
| Market best draw last update utc | 2026-10-30T11:50:53Z |
| Market best away last update utc | 2026-10-30T11:50:53Z |
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
| Dc lambda away | 1.6720 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:50:54.576591+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.7215 |
| Shot lambda away | 1.5412 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 70.2% |
| P btts no | 29.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.91 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.20 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.23 |
| Fair Over 3.5 odds | 2.09 |
| Fair Under 3.5 odds | 1.92 |
| Fair Over 4.5 odds | 3.48 |
| Fair Under 4.5 odds | 1.40 |
| Goal margin distribution | {"-1": 0.19245422383797667, "-10": 2.68219525171254e-06, "-11": 4.1106992161615084e-07, "-12": 5.795340710896029e-08, "-13": 7.562496795698022e-09, "-14": 9.174951171904926e-10, "-15": 1.0260593606876813e-10, "-16": 9.22520895053791e-12, "-2": 0.12038522533099609, "-3": 0.05619113835926964, "-4": 0.021167926173299895, "-5": 0.006646236931376509, "-6": 0.0017831097563401031, "-7": 0.0004168198887978018, "-8": 8.622219858002341e-05, "-9": 1.5982286171444523e-05, "0": 0.24166775336653576, "1": 0.16304388364390848, "10": 4.267365532836169e-06, "11": 7.016494332998071e-07, "12": 1.0612518854122745e-07, "13": 1.4857294357650793e-08, "14": 1.9338078045391086e-09, "15": 2.320155305937904e-10, "16": 2.237977955177343e-11, "2": 0.10913460059714244, "3": 0.054650246681798666, "4": 0.02208704577100929, "5": 0.00743995247141049, "6": 0.002141447545445547, "7": 0.0005370476502912725, "8": 0.00011918414983788586, "9": 2.3701363756323784e-05} |
| Raw goal margin distribution | {"-1": 0.1750734094173767, "-10": 1.722086607181755e-06, "-11": 2.5221367579119987e-07, "-12": 3.3969515159112955e-08, "-13": 4.2338517932500895e-09, "-14": 4.906245994604308e-10, "-15": 5.251352365498404e-11, "-16": 4.5715403848911155e-12, "-2": 0.10713409375221326, "-3": 0.04842673210449478, "-4": 0.01758380271434011, "-5": 0.0053059122762528785, "-6": 0.0013654837611465542, "-7": 0.00030578693797568286, "-8": 6.054160903906311e-05, "-9": 1.0733655688797215e-05, "0": 0.23973422260249236, "1": 0.18834047404320772, "10": 3.478605803638224e-06, "11": 5.465801838984988e-07, "12": 7.897863470945378e-08, "13": 1.056065725266595e-08, "14": 1.3129241556827742e-09, "15": 1.5076360111280397e-10, "16": 1.4080657197565457e-11, "2": 0.12330984330045883, "3": 0.05979849194881843, "4": 0.023294473211856962, "5": 0.007541108327059772, "6": 0.002082076471785673, "7": 0.0005002234989670907, "8": 0.00010625127288607357, "9": 2.0209839531734475e-05} |
| Unadjusted home-win probability | 40.5% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.6% |
| Raw p btts yes | 67.6% |
| P home draw | 60.1% |
| P draw away | 64.1% |
| P home away | 75.8% |
| Raw p home draw | 64.5% |
| Raw p draw away | 59.5% |
| Raw p home away | 76.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0486 |
| Totals anchor target over 2 5 | 0.6901 |
| Totals anchor reference over odds | 1.41 |
| Totals anchor reference under odds | 2.96 |
| Totals anchor reference last update utc | 2026-10-30T11:50:53Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6616 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.33, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.67, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.24, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.55, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 3.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:49:46Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.15, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.75, "price": 2.15, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.85 |
| Reference draw odds | 3.95 |
| Reference away odds | 2.33 |
| Market reference 1x2 last update utc | 2026-10-30T11:50:53Z |
| Market reference home last update utc | 2026-10-30T11:50:53Z |
| Market reference draw last update utc | 2026-10-30T11:50:53Z |
| Market reference away last update utc | 2026-10-30T11:50:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.95 |
| Market reference over 2 5 last update utc | 2026-10-30T11:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:50:12Z |
| Home probability edge | +2.0% |
| Draw probability edge | -0.1% |
| Away probability edge | -1.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0655 |
| Raw ev home | 0.1542 |
| Raw edge prob draw | -0.0028 |
| Raw ev draw | -0.0530 |
| Raw edge prob away | -0.0627 |
| Raw ev away | -0.1722 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.042515438295106206, 0.04662361403481065, 0.046916750323211645, 0.025087527166933486, 0.010061183079855871, 0.0032279755367775097, 0.0008630385034685291, 0.00019778043101619815, 3.96592520423766e-05, 7.068922123968614e-06, 1.1339773616306588e-06, 1.6537234572036848e-07, 2.2107153561031588e-08, 2.7279767397744534e-09, 3.125818913213915e-10, 3.3429027528094374e-11, 3.351621344579985e-12], [0.04365297582449653, 0.10465167729458864, 0.08590499022037891, 0.04593548702930248, 0.018422116368380547, 0.00591045213080973, 0.0015802312327585636, 0.0003621377413222718, 7.261644584028996e-05, 1.29432597472061e-05, 2.076322709691553e-06, 3.0279824676605816e-07, 4.047839625246302e-08, 4.994949853460004e-09, 5.723402437731654e-10, 6.120884893123058e-11, 6.136848712774348e-12], [0.04860592026591624, 0.07797230222113367, 0.06918014800306091, 0.04205414416850905, 0.01686553006721631, 0.005411045404865018, 0.001446708773102095, 0.0003315387245749707, 6.648068149194182e-05, 1.184961228499095e-05, 1.9008827427478312e-06, 2.772131514649786e-07, 3.7058153114284404e-08, 4.572898968457281e-09, 5.239800572860455e-10, 5.603697541511729e-11, 5.6183124899211604e-12], [0.02966595850686519, 0.047589328002064966, 0.03817075620806295, 0.02257774866749904, 0.010293645556612835, 0.003302557539931053, 0.000882978908733055, 0.00020235012510517043, 4.057557449500725e-05, 7.2322487558266405e-06, 1.1601777780209314e-06, 1.6919325472959174e-07, 2.2617936798952506e-08, 2.79100632828607e-09, 3.198040599340899e-10, 3.4201401360582954e-11, 3.4290601698879653e-12], [0.013579658958975236, 0.021784121494179944, 0.017472749157649087, 0.009343103820143887, 0.004144787871290587, 0.0015117531117114405, 0.00040418557336646297, 9.262622303601922e-05, 1.8573560115348406e-05, 3.3105780683901037e-06, 5.310739767150957e-07, 7.744859134941417e-08, 1.035341123444074e-08, 1.2775893986939814e-09, 1.4639102480358469e-10, 1.565576808476518e-11, 1.5696599739431386e-12], [0.004972895445785823, 0.00797738432873188, 0.006398552053032431, 0.003421461361957787, 0.001372153936665494, 0.00048697196167062925, 0.00014801348127509194, 3.391988886375699e-05, 6.801670998416255e-06, 1.2123396212637975e-06, 1.9448024196781175e-07, 2.836181294151538e-08, 3.791437747563543e-09, 4.678555272664219e-10, 5.3608655618594576e-11, 5.73317032807744e-12, 5.748122953187312e-13], [0.001517569353142255, 0.0024344436973393387, 0.0019526343567903117, 0.0010441210683943913, 0.00041873769211087813, 0.00013434553528469836, 3.9732245723989935e-05, 1.0351270072498898e-05, 2.0756534236206714e-06, 3.699674515355307e-07, 5.9349177600777664e-08, 8.655122270079365e-09, 1.1570260812390589e-09, 1.4277461040919532e-10, 1.6359654796056278e-11, 1.7495810400775452e-12, 1.7541441051697338e-13], [0.0003969547261671833, 0.0006367840318110173, 0.0005107558575819992, 0.00027311357595070695, 0.0001095303523121231, 3.5141125550735947e-05, 9.395407139851949e-06, 2.3817089547685317e-06, 5.429342881004299e-07, 9.67733883864817e-08, 1.5524125137334558e-08, 2.263943775320024e-09, 3.0264644597332406e-10, 3.734594156191803e-11, 4.279239216521938e-12, 4.576426515422493e-13, 4.588362248378634e-14], [9.085345754556186e-05, 0.00014574465848648922, 0.00011689981895675809, 6.25091755861943e-05, 2.5068882060743647e-05, 8.042964468906203e-06, 2.1503843321021434e-06, 4.927983379007494e-07, 1.0930760340687981e-07, 2.2149117654310078e-08, 3.5531015280135395e-09, 5.18162667220515e-10, 6.926854428978893e-11, 8.547594202885844e-12, 9.79415668480635e-13, 1.0474347443698342e-13, 1.0501665486183342e-14], [1.8483721646845453e-05, 2.9651086174985253e-05, 2.3782735104822605e-05, 1.2717206731836084e-05, 5.100149741423003e-06, 1.636304445366621e-06, 4.3748588663652153e-07, 1.002575746907334e-07, 2.0103811096920645e-08, 3.96375689398642e-09, 7.228623037692163e-10, 1.0541783182976805e-10, 1.4092369471933089e-11, 1.7389690636385647e-12, 1.9925765162736465e-13, 2.1309582245076026e-14, 2.1365159556811934e-15], [3.384385995129099e-06, 5.429140446297112e-06, 4.354640107251546e-06, 2.328531947338267e-06, 9.33841987437587e-07, 2.9960881009108954e-07, 8.010405783469326e-08, 1.835725175762082e-08, 3.6810258250535376e-09, 6.561113372944349e-10, 1.1642564892283684e-10, 1.93020994634179e-11, 2.58032547720902e-12, 3.1840679368516403e-13, 3.64842545497355e-14, 3.90180360266329e-15, 3.9119798582399376e-16], [5.633491892276532e-07, 9.037095275262388e-07, 7.248531867609272e-07, 3.8759662358597584e-07, 1.5544300421017356e-07, 4.987149234549379e-08, 1.333374978503246e-08, 3.0556629500853132e-09, 6.127264789106483e-10, 1.0921324885514188e-10, 1.7519693896746093e-11, 2.8262134168615084e-12, 4.2950900624847613e-13, 5.30005174720833e-14, 6.072999725725668e-15, 6.494761233646026e-16, 6.511700156501544e-17], [8.595811776154589e-08, 1.3789168685204222e-07, 1.1060105664277242e-07, 5.9141074224067495e-08, 2.3718127791086717e-08, 7.60959577816245e-09, 2.03451794400585e-09, 4.662455200532538e-10, 9.349230608111348e-11, 1.6664203101244975e-11, 2.6732263752565175e-12, 3.8984703864107213e-13, 5.764798324422302e-14, 8.087035198424981e-15, 9.26643076038598e-16, 9.909971677074067e-17, 9.93581777667642e-18], [1.210692952418171e-08, 1.9421608780678177e-08, 1.5577809669921668e-08, 8.329833601073812e-09, 3.3406234232444202e-09, 1.0717875425017516e-09, 2.8655542961157206e-10, 6.566920960169563e-11, 1.3168096164195365e-11, 2.347100399325854e-12, 3.7651549580455046e-13, 5.490872467835574e-14, 7.34025754437433e-15, 1.0019338994747758e-15, 1.305147519259558e-16, 1.3957882257706478e-17, 1.3994285673056814e-18], [1.5834211741446573e-09, 2.5400814069212276e-09, 2.037364934592408e-09, 1.0894285685480921e-09, 4.36907958590462e-10, 1.4017518525998393e-10, 3.747753994163518e-11, 8.588636513079602e-12, 1.7222072902889263e-12, 3.069687043864351e-13, 4.924308903093199e-14, 7.181311919535943e-15, 9.600055237971617e-16, 1.184626836622671e-16, 1.501497648183761e-17, 1.825500534130206e-18, 1.830261604107674e-19], [1.9328389049762026e-10, 3.100607876963702e-10, 2.4869556334824824e-10, 1.3298356469306098e-10, 5.333215912775383e-11, 1.7110801346274765e-11, 4.574780762365521e-12, 1.048391360696989e-12, 2.102251319774239e-13, 3.7470829880037745e-14, 6.01096914922883e-15, 8.766030979942129e-16, 1.1718524772093862e-16, 1.446041568150715e-17, 1.6569291142096503e-18, 1.9601251228334383e-19, 2.2341502642936608e-20], [2.2119033458957652e-11, 3.5482755027901394e-11, 2.8460237801670045e-11, 1.521838115615482e-11, 6.103228826510841e-12, 1.958126911215547e-12, 5.235290353978291e-13, 1.1997587344520236e-13, 2.4057756267999372e-14, 4.2880890782859614e-15, 6.878836481935969e-16, 1.0031675792969752e-16, 1.3410452410505444e-17, 1.654821917471858e-18, 1.8961575339759397e-19, 2.0278430760313002e-20, 2.2489794473582283e-21]] |
| Legacy trial inputs | {"lambda_home": 1.8310089600958186, "lambda_away": 1.604172944253664, "rho": -0.11082685883326926, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3820 |
| Legacy p draw | 0.2436 |
| Legacy p away | 0.3744 |
| Legacy p over 1 5 | 0.8672 |
| Legacy p under 3 5 | 0.5516 |
| Legacy p btts yes | 0.6820 |
| Legacy p over 2 5 | 0.6670 |
| Legacy goal margin distribution | {"-1": 0.18654707766937834, "-10": 1.4767770674488295e-06, "-11": 2.1075967558160297e-07, "-12": 2.7661854533112164e-08, "-13": 3.3597830191326237e-09, "-14": 3.7940905274254327e-10, "-15": 3.956587624086872e-11, "-16": 3.351621344579985e-12, "-2": 0.11346060650985734, "-3": 0.04990348176710282, "-4": 0.017640541692775513, "-5": 0.005183835093435943, "-6": 0.0012994498062013655, "-7": 0.00028348805410932665, "-8": 5.468342588162094e-05, "-9": 9.446408915443072e-06, "0": 0.2435989994385656, "1": 0.17065554652910442, "10": 4.407480955188156e-06, "11": 7.17963404604204e-07, "12": 1.0755617827033606e-07, "13": 1.491092487560734e-08, "14": 1.9219421996426972e-09, "15": 2.2876664552552167e-10, "16": 2.2119033458957652e-11, "2": 0.11754559204012469, "3": 0.05901078291216588, "4": 0.023809579662564574, "5": 0.00798601774832135, "6": 0.0022849562260691693, "7": 0.0005689739996644011, "8": 0.0001252716089167073, "9": 2.47003418474927e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4245 |
| Legacy raw p draw | 0.2447 |
| Legacy raw p away | 0.3308 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8310 |
| Legacy lambda away | 1.6042 |
| Legacy model home team | Werder Bremen |
| Legacy model away team | Hoffenheim |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 57.3% |
| Market home draw odds | 1.65 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-30T11:50:54Z |
| Market reference home draw last update utc | 2026-10-30T11:50:59Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 66.4% |
| Market draw away odds | 1.46 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-30T11:50:54Z |
| Market reference draw away last update utc | 2026-10-30T11:50:59Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.4% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-30T11:50:54Z |
| Market reference home away last update utc | 2026-10-30T11:50:59Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.68 |
| Market reference dc draw away odds | 1.45 |
| Market reference dc home away odds | 1.26 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.15, "price": 1.68, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.15, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.73, "price": 2.08, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-30T11:50:54Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.08, "price": 1.73, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 87.6% |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-30T11:50:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 51.9% |
| Market under 3 5 odds | 1.86 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market reference under 3 5 odds | 1.86 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market reference under 3 5 last update utc | 2026-10-30T11:50:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.9% |
| Market btts yes odds | 1.38 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-30T11:50:54Z |
| Market reference btts yes odds | 1.38 |
| Market reference btts yes opposite odds | 3.17 |
| Market reference btts yes last update utc | 2026-10-30T11:50:54Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 9.899922336466238, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,429.1271 |
| Elo away rating | 1,502.6430 |
| Elo rating diff | -13.5159 |
| Elo home expectancy | 0.4806 |

</details>


---

## 2026-11-01 — Eintracht Frankfurt vs Hamburger SV

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **59.9%**. Expected goals are 2.01 for Eintracht Frankfurt and 1.15 for Hamburger SV (3.16 combined). The most likely exact score is 2-1 at 10.5%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 62.0%; Under 3.5 goals: 60.7%; Double Chance 1X: 81.0%; Double Chance X2: 40.1%; Double Chance 12 (either team wins): 78.9%; Under 4.5 goals: 78.3%; BTTS Yes (both teams score): 59.4%; BTTS No (at least one team does not score): 40.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 59.9% | 1.67 |
| Draw | 21.1% | 4.73 |
| Hamburger SV win | 19.0% | 5.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 2.01 |
| Hamburger SV expected goals | 1.15 |
| Expected total goals | 3.16 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 62.0% |
| Under 2.5 | 38.0% |
| Over 3.5 | 39.3% |
| Under 3.5 | 60.7% |
| Over 4.5 | 21.7% |
| Under 4.5 | 78.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.45% |
| 2 | 1-1 | 9.74% |
| 3 | 2-0 | 9.07% |
| 4 | 1-0 | 8.26% |
| 5 | 3-1 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 59.9% | 61.4% | 1.60 | -4.2% |
| Draw | 21.1% | 20.4% | 4.62 | -2.3% |
| Hamburger SV win | 19.0% | 18.2% | 5.15 | -2.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:30:00+00:00 |
| Fixture id | 1eb5e1a69ae9dd9edd92fde344308a4e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T11:50:53Z |
| Market best draw last update utc | 2026-10-30T11:50:53Z |
| Market best away last update utc | 2026-10-30T11:50:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0310 |
| Dc lambda away | 1.1033 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:50:54.576591+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9213 |
| Shot lambda away | 1.3486 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 59.4% |
| P btts no | 40.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.81 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.00 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.61 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.1143304761043796, "-10": 5.448961940197728e-08, "-11": 5.611454605765257e-09, "-12": 5.310954638682456e-10, "-13": 4.649387061462342e-11, "-14": 3.785665478879192e-12, "-15": 2.879759517770036e-13, "-16": 2.0411267168771386e-14, "-17": 1.2177755646226303e-15, "-2": 0.05245739789669819, "-3": 0.01716161519531015, "-4": 0.004462845591321097, "-5": 0.0009583456075938561, "-6": 0.00017479941694737114, "-7": 2.7667513283099886e-05, "-8": 3.8642485703900426e-06, "-9": 4.826252696093095e-07, "0": 0.21138706167227966, "1": 0.23621297539979844, "10": 1.6348142847426958e-05, "11": 2.9351658156878323e-06, "12": 4.843199025572041e-07, "13": 7.391932019866324e-08, "14": 1.0493177846997367e-08, "15": 1.3916292826835542e-09, "16": 1.7196491168912269e-10, "17": 1.788708894148615e-11, "2": 0.18439158367908767, "3": 0.10517076853909935, "4": 0.047681651169156215, "5": 0.017851064498996448, "6": 0.005676550157049899, "7": 0.0015664522626488197, "8": 0.00038142980821850213, "9": 8.305430898791453e-05} |
| Raw goal margin distribution | {"-1": 0.12464442236455131, "-10": 5.9405220433290346e-08, "-11": 6.117673447996062e-09, "-12": 5.790064868955363e-10, "-13": 5.068816157960465e-11, "-14": 4.127176785737569e-12, "-15": 3.1395475106179063e-13, "-16": 2.225260221655442e-14, "-17": 1.327633164786922e-15, "-2": 0.05718966877748274, "-3": 0.018709793624135874, "-4": 0.004865446465249992, "-5": 0.0010447995911001488, "-6": 0.0001905683689725387, "-7": 3.0163446606196993e-05, "-8": 4.212848991283605e-06, "-9": 5.261637141619829e-07, "0": 0.22859920276731518, "1": 0.2226821018239395, "10": 1.5411680090907258e-05, "11": 2.7670321324765886e-06, "12": 4.565768399219607e-07, "13": 6.968503554631216e-08, "14": 9.892102217614961e-09, "15": 1.311913255837086e-09, "16": 1.6211432885974587e-10, "17": 1.6862471480494634e-11, "2": 0.17382916981087695, "3": 0.09914632229278325, "4": 0.0449503262164686, "5": 0.016828510608713296, "6": 0.0053513830810581475, "7": 0.0014767219356308168, "8": 0.0003595805490728799, "9": 7.82967491928028e-05} |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 20.7% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 60.0% |
| P home draw | 81.0% |
| P draw away | 40.1% |
| P home away | 78.9% |
| Raw p home draw | 79.3% |
| Raw p draw away | 43.5% |
| Raw p home away | 77.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6195 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.60 |
| Reference draw odds | 4.62 |
| Reference away odds | 5.15 |
| Market reference 1x2 last update utc | 2026-10-30T11:50:53Z |
| Market reference home last update utc | 2026-10-30T11:50:53Z |
| Market reference draw last update utc | 2026-10-30T11:50:53Z |
| Market reference away last update utc | 2026-10-30T11:50:53Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.91 |
| Market reference over 2 5 last update utc | 2026-10-30T11:50:12Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:50:12Z |
| Home probability edge | -1.5% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.0490 |
| Raw ev home | -0.0964 |
| Raw edge prob draw | 0.0246 |
| Raw ev draw | 0.0561 |
| Raw edge prob away | 0.0244 |
| Raw ev away | 0.0644 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05717525911347834, 0.040530202613566, 0.026581901522878416, 0.00909558440849838, 0.0023341912445837085, 0.0004792170373308199, 8.198734408224158e-05, 1.2023048429938098e-05, 1.5427317870936345e-06, 1.7595991238759012e-07, 1.8062570515384227e-08, 1.6855928830414374e-09, 1.4419070370936581e-10, 1.1385699766557391e-11, 8.348289680218104e-13, 5.713103209540257e-14, 3.665370715116459e-15], [0.09012697074698366, 0.10456423412679815, 0.05214842570745431, 0.01784373504597559, 0.004579220888332557, 0.0009401289086668219, 0.0001608429298462504, 2.3586839612889336e-05, 3.02653419720701e-06, 3.451984957034326e-07, 3.5435185695668466e-08, 3.3067993709421352e-09, 2.82873600807742e-10, 2.2336487775062843e-11, 1.637769080584644e-12, 1.1207976902077834e-13, 7.190731342639909e-15], [0.09975422920280273, 0.10239933486750843, 0.047391207387455545, 0.017502936924728242, 0.0044917621880380615, 0.0009221733536791213, 0.0001577709850899375, 2.3136353736164316e-05, 2.9687303144637706e-06, 3.3860553753127717e-07, 3.47584078417035e-08, 3.2436426938195854e-09, 2.7747098798832037e-10, 2.190988241192601e-11, 1.6064892714941064e-12, 1.099391535827155e-13, 7.053395312618614e-15], [0.06523267978790588, 0.06696240425382431, 0.03436899724211478, 0.01060415921716283, 0.002937315909684537, 0.0006030404883104369, 0.00010317180767615215, 1.5129647803328646e-05, 1.9413536200691044e-06, 2.2142566566560118e-07, 2.2729703861132893e-08, 2.1211281655251212e-09, 1.8144770657370214e-10, 1.4327616533051048e-11, 1.0505379177160427e-12, 7.189294788930301e-14, 4.612454845499813e-15], [0.03199339927478412, 0.03284174347363383, 0.01685629127940248, 0.0057677521682970405, 0.0013346802472930092, 0.0002957614984407488, 5.0600662852062427e-05, 7.420343064742473e-06, 9.521378196076146e-07, 1.0859832455691691e-07, 1.1147794225090992e-08, 1.0403083321623282e-09, 8.899111523213237e-11, 7.026986441278864e-12, 5.152368285967764e-13, 3.525993097849335e-14, 2.2621807043460953e-15], [0.012552942488136497, 0.012885799145437617, 0.006613740952509145, 0.002263037466966564, 0.0005807611698510233, 0.00010751231178836198, 1.9853695607273372e-05, 2.9114486689562093e-06, 3.735811624035289e-07, 4.260968053949178e-08, 4.373952844937001e-09, 4.081757787411924e-10, 3.4916588320908365e-11, 2.7571111123478375e-12, 2.021585209372479e-13, 1.3834600128206479e-14, 8.875900943045464e-16], [0.004104397799815784, 0.004213230938593556, 0.0021624749607261095, 0.0007399385450141679, 0.0001898897306354855, 3.898497792151298e-05, 6.014183510287712e-06, 9.519476029173154e-07, 1.2214870756165565e-07, 1.3931958918988543e-08, 1.4301381887333482e-09, 1.3346000507743483e-10, 1.1416571725462007e-11, 9.014843168494458e-13, 6.609916275271881e-14, 4.5234575384381706e-15, 2.902126599914565e-16], [0.0011502879320960703, 0.0011807892266230838, 0.000606049650181279, 0.00020737326651445036, 5.3218005717860976e-05, 1.0925829274677234e-05, 1.8692568384383274e-06, 2.471733088765236e-07, 3.4233081460966284e-08, 3.904534842039437e-09, 4.008068369502433e-10, 3.7403156503237525e-11, 3.199578920517297e-12, 2.5264766750735743e-13, 1.852478072167349e-14, 1.2677325326623944e-15, 8.133425092096469e-17], [0.0002820796356379211, 0.00028955932294628657, 0.00014861867166606672, 5.0853159306687554e-05, 1.3050398290205894e-05, 2.679289119574703e-06, 4.58388959136136e-07, 6.722052918209369e-08, 7.77754573133934e-09, 9.574904985494242e-10, 9.828795327974435e-11, 9.172198076455354e-12, 7.846175126341443e-13, 6.195558521194147e-14, 4.542743821297101e-15, 3.108800161435414e-16, 1.9945211302758267e-17], [6.148715261935879e-05, 6.311755984118633e-05, 3.2395599654515934e-05, 1.1084869563148688e-05, 2.844699616824925e-06, 5.840260628319185e-07, 9.991870496320073e-08, 1.4652595986329375e-08, 1.8801409412327656e-09, 1.9336529519214504e-10, 2.1424610714236196e-11, 1.9993373208476393e-12, 1.7102935005589493e-13, 1.350495407062349e-14, 9.902181772855133e-16, 6.776500173682488e-17, 4.347617113956562e-18], [1.206256146714641e-05, 1.238241507057351e-05, 6.3553749921838655e-06, 2.1746318501449545e-06, 5.580737198215104e-07, 1.145743457163685e-07, 1.9602070822788494e-08, 2.874549108372813e-09, 3.688464126956225e-10, 4.206964749502466e-11, 3.8940319128703164e-12, 3.922303814519354e-13, 3.355257090057209e-14, 2.6494044958685516e-15, 1.9426119312006526e-16, 1.3294151118560246e-17, 8.52916364453788e-19], [2.1513051241399993e-06, 2.208349616547477e-06, 1.1334533567977553e-06, 3.878360873083794e-07, 9.953000914190606e-08, 2.043383386737022e-08, 3.4959436699804064e-09, 5.126632716672431e-10, 6.5782145841406e-11, 7.502937785917899e-12, 7.701887378311788e-13, 6.48089689063749e-14, 5.983954395015167e-15, 4.725097139115276e-16, 3.46456348694247e-17, 2.370953756409408e-18, 1.5211390634649046e-19], [3.517028786914906e-07, 3.61028711632657e-07, 1.8530091523286956e-07, 6.340479871321345e-08, 1.62715136679611e-08, 3.3405945596539668e-09, 5.715290865431834e-10, 8.381198297793553e-11, 1.075429505527472e-11, 1.22660648568174e-12, 1.2591314602073323e-13, 1.1750171584555916e-14, 9.063451097645926e-16, 7.724753905321073e-17, 5.663989445728666e-18, 3.8761180458162048e-19, 2.4868112919340107e-20], [5.3074722012400305e-08, 5.4482063324839975e-08, 2.7963361008639524e-08, 9.56828126763189e-09, 2.4554989935284314e-09, 5.041219118519e-10, 8.624822038175275e-11, 1.2647885381012039e-11, 1.6229074456871852e-12, 1.851045362164127e-13, 1.9001280989284307e-14, 1.7731930223845484e-15, 1.5168428407743807e-16, 1.0800102248910083e-17, 8.547404173422011e-19, 5.849366048248976e-20, 3.752793224432857e-21], [7.437292290839531e-09, 7.634501212464068e-09, 3.918469685190762e-09, 1.3407909040336896e-09, 3.44085904594403e-10, 7.06419528261201e-11, 1.2085851799543488e-11, 1.7723318535261549e-12, 2.274159256403708e-13, 2.5938459741345576e-14, 2.6626249796402614e-15, 2.484752495259397e-16, 2.1255322945395197e-17, 1.6783795298293471e-18, 1.1096672576175481e-19, 8.196641144305291e-21, 5.258740707236924e-22], [9.726996246165497e-10, 9.984919474853837e-10, 5.124840927054835e-10, 1.75357745539894e-10, 4.500189277851298e-11, 9.23903462565011e-12, 1.5806698256389466e-12, 2.317976033756559e-13, 2.974300012044352e-14, 3.392408025245206e-15, 3.482361882402736e-16, 3.249728160315488e-17, 2.779915571632807e-18, 2.1950988004598404e-19, 1.609503239911877e-20, 9.931874646404328e-22, 6.877738445462817e-23], [1.192652500478737e-10, 1.2242771434663357e-10, 6.283701763139064e-11, 2.1501072726219527e-11, 5.517800006320301e-12, 1.1328222474265934e-12, 1.9381006965256557e-13, 2.842131160274027e-14, 3.646867189793587e-15, 4.1595203817908313e-16, 4.269815163398183e-17, 3.984576860307024e-18, 3.408527333332369e-19, 2.6914681643866665e-20, 1.97345410137919e-21, 1.350521770607184e-22, 7.812899541160363e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9618019298796734, "lambda_away": 1.0265162257865592, "rho": -0.11082685883326926, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5969 |
| Legacy p draw | 0.2212 |
| Legacy p away | 0.1820 |
| Legacy p over 1 5 | 0.8122 |
| Legacy p under 3 5 | 0.6476 |
| Legacy p btts yes | 0.5584 |
| Legacy p over 2 5 | 0.5813 |
| Legacy goal margin distribution | {"-1": 0.1134354835094789, "-10": 2.1661697852489118e-08, "-11": 1.991463051699894e-09, "-12": 1.6820783588451643e-10, "-13": 1.3138020455570251e-11, "-14": 9.539621323552075e-13, "-15": 6.432176343804248e-14, "-16": 3.665370715116459e-15, "-2": 0.04957407751028725, "-3": 0.014707958724525023, "-4": 0.003448217001983608, "-5": 0.0006652507835332489, "-6": 0.00010877590731909486, "-7": 1.5411994013782328e-05, "-8": 1.9249016344174803e-06, "-9": 2.1482742223340588e-07, "0": 0.22118332173566618, "1": 0.23328473957303678, "10": 1.4466133798943679e-05, "11": 2.5416841224003556e-06, "12": 4.102842872470676e-07, "13": 6.124320839029608e-08, "14": 8.498621255956306e-09, "15": 1.0951273389631833e-09, "16": 1.192652500478737e-10, "2": 0.18603725118093845, "3": 0.10548410291418253, "4": 0.04726270119749152, "5": 0.01742603909158541, "6": 0.005445469659629595, "7": 0.0014745204452014304, "8": 0.0003519571945154758, "9": 7.506895359548077e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5800 |
| Legacy raw p draw | 0.2384 |
| Legacy raw p away | 0.1817 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9618 |
| Legacy lambda away | 1.0265 |
| Legacy model home team | Ein Frankfurt |
| Legacy model away team | Hamburg |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.303801471653667, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.6826 |
| Elo away rating | 1,410.4900 |
| Elo rating diff | 124.1926 |
| Elo home expectancy | 0.6715 |

</details>


---

## 2026-11-01 — Union Berlin vs 1. FC Köln

The model's most likely 1X2 outcome is **Union Berlin win** at **38.1%**. Expected goals are 1.44 for Union Berlin and 1.19 for 1. FC Köln (2.63 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 49.3%; Under 3.5 goals: 73.0%; Double Chance 1X: 64.5%; Double Chance X2: 61.9%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 53.8%; BTTS No (at least one team does not score): 46.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 38.1% | 2.62 |
| Draw | 26.4% | 3.79 |
| 1. FC Köln win | 35.5% | 2.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 1.44 |
| 1. FC Köln expected goals | 1.19 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.8% |
| Under 4.5 | 87.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.59% |
| 2 | 0-1 | 8.99% |
| 3 | 1-2 | 8.62% |
| 4 | 1-0 | 8.60% |
| 5 | 2-1 | 8.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 38.1% | 36.4% | 2.66 | +1.4% |
| Draw | 26.4% | 25.8% | 3.72 | -1.8% |
| 1. FC Köln win | 35.5% | 37.8% | 2.57 | -8.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:30:00+00:00 |
| Fixture id | 60eaeb599578cd5c951f917c4fef06ff |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T11:50:53Z |
| Market best draw last update utc | 2026-10-30T11:50:53Z |
| Market best away last update utc | 2026-10-30T11:50:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Union Berlin |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4298 |
| Dc lambda away | 1.1555 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-30T11:50:54.576591+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.4864 |
| Shot lambda away | 1.3222 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.8% |
| P btts no | 46.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.97 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.95 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.70 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.82 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.20457174950567306, "-10": 1.5357258214202695e-07, "-11": 1.638734366328606e-08, "-12": 1.605623583270681e-09, "-13": 1.4458454896495927e-10, "-14": 1.0939210209841303e-11, "-2": 0.10218211477717205, "-3": 0.03576998905173618, "-4": 0.009832930629983633, "-5": 0.002216254783398782, "-6": 0.0004224066194623863, "-7": 6.96580697840569e-05, "-8": 1.011547371456423e-05, "-9": 1.3116234192166793e-06, "0": 0.2638771233768783, "1": 0.19349454305532857, "10": 8.135518888552048e-07, "11": 1.0523450972233525e-07, "12": 1.249888891554101e-08, "13": 1.3643556813734894e-09, "14": 1.2513238907307387e-10, "2": 0.11609728496478487, "3": 0.04926562915183484, "4": 0.016416714696852356, "5": 0.004485398264749163, "6": 0.0010363109554979383, "7": 0.00020716141052700245, "8": 3.646713951335382e-05, "9": 5.731953841091889e-06} |
| Raw goal margin distribution | {"-1": 0.17422238171380447, "-10": 1.3078922720940425e-07, "-11": 1.3956189209307928e-08, "-12": 1.367420308469883e-09, "-13": 1.2313461922557805e-10, "-14": 9.316316947143606e-12, "-2": 0.08702282425628159, "-3": 0.03046331031302721, "-4": 0.008374160155162874, "-5": 0.0018874609411190472, "-6": 0.0003597402254819783, "-7": 5.93239039734968e-05, "-8": 8.614786386552814e-06, "-9": 1.1170367196825321e-06, "0": 0.2778952713220413, "1": 0.21312575287034746, "10": 8.96091724725174e-07, "11": 1.1591119707237118e-07, "12": 1.3766977962814236e-08, "13": 1.5027779449703358e-09, "14": 1.378278384938137e-10, "2": 0.1278760675811299, "3": 0.05426392981332706, "4": 0.018082291232491696, "5": 0.0049404694675273956, "6": 0.0011414510668403314, "7": 0.0002281792079874092, "8": 4.0166954794116086e-05, "9": 6.313495763296394e-06} |
| Unadjusted home-win probability | 42.0% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 30.2% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 54.0% |
| P home draw | 64.5% |
| P draw away | 61.9% |
| P home away | 73.6% |
| Raw p home draw | 69.8% |
| Raw p draw away | 58.0% |
| Raw p home away | 72.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4933 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T11:50:54Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T11:50:53Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.66 |
| Reference draw odds | 3.72 |
| Reference away odds | 2.57 |
| Market reference 1x2 last update utc | 2026-10-30T11:50:53Z |
| Market reference home last update utc | 2026-10-30T11:50:53Z |
| Market reference draw last update utc | 2026-10-30T11:50:53Z |
| Market reference away last update utc | 2026-10-30T11:50:53Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-10-30T11:50:54Z |
| Market reference under 2 5 last update utc | 2026-10-30T11:50:54Z |
| Home probability edge | +1.7% |
| Draw probability edge | +0.6% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -9.1% |
| Under 2.5 probability edge | +9.1% |
| Raw edge prob home | 0.0552 |
| Raw ev home | 0.1164 |
| Raw edge prob draw | 0.0200 |
| Raw ev draw | 0.0338 |
| Raw edge prob away | -0.0753 |
| Raw ev away | -0.2228 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0910149480883111, 0.08951013361608896, 0.05642069448353078, 0.01995296635699147, 0.00529221861881874, 0.0011229439235558244, 0.00019856244710030727, 3.0094655336419557e-05, 3.991073117870648e-06, 4.7047599808383144e-07, 4.991462005636342e-08, 4.8142138938561545e-09, 4.2563215828330634e-10, 3.473612575514285e-11, 2.6323500429954344e-12], [0.09547047398340833, 0.1312653461969073, 0.08065113037910522, 0.028521968859801145, 0.00756501524357642, 0.0016052035093889392, 0.00028383709126720587, 4.301910838691112e-05, 5.7050796933363845e-06, 6.725266572671262e-07, 7.135095671614538e-08, 6.8817265717923625e-09, 6.084241784947749e-10, 4.965390505713789e-11, 3.762839299736713e-12], [0.077327865063896, 0.08204012574827162, 0.044802892521950306, 0.02038550792610386, 0.005406943642883524, 0.0011472871674640098, 0.00020286689541635768, 3.0747049031081924e-05, 4.077591833832956e-06, 4.806750042265743e-07, 5.099667210288848e-08, 4.918576703597552e-09, 4.348590370498334e-10, 3.5489137516411627e-11, 2.6894142808475344e-12], [0.03684569869439538, 0.039091028204042165, 0.020736592603706833, 0.007549633558144722, 0.002576336695169914, 0.0005466670682475898, 9.666337609866939e-05, 1.4650559709684652e-05, 1.9429182479561743e-06, 2.2903524313034052e-07, 2.4299235639924673e-08, 2.3436363473410123e-09, 2.072045444476392e-10, 1.6910101769564937e-11, 1.2814701165567093e-12], [0.013167363839248441, 0.013969766063663788, 0.007410532824033792, 0.0026207070557858567, 0.0007155965174417367, 0.00019535968760571202, 3.454410930236745e-05, 5.235597559054984e-06, 6.943310179281667e-07, 8.184918416994639e-08, 8.683696822804176e-09, 8.375336494031637e-10, 7.404765610545472e-11, 6.0430788517643054e-12, 4.579525934296627e-13], [0.003764444190095281, 0.0039938445794743815, 0.0021186121668326776, 0.0007492392228646635, 0.00019872422447122915, 4.3410075200573314e-05, 9.87588504068676e-06, 1.496815539805613e-06, 1.985036943121195e-07, 2.340002824970771e-08, 2.482599588819431e-09, 2.394441832849812e-10, 2.1169633665432505e-11, 1.7276679942574023e-12, 1.3092499005281211e-13], [0.0008968537813988992, 0.0009515068978431144, 0.0005047452524707266, 0.0001785012597521172, 4.734472426009708e-05, 1.00459701780364e-05, 1.8287332694829302e-06, 3.566063432321256e-07, 4.7292184416996103e-08, 5.5749010373986315e-09, 5.914628339531059e-10, 5.7045983515476456e-11, 5.043524367721341e-12, 4.1160540451853127e-13, 3.1192007765031e-14], [0.00018314523956835925, 0.0001943058750163367, 0.00010307331262020663, 3.645148926011492e-05, 9.668199038407971e-06, 2.051473331676502e-06, 3.6274791318950154e-07, 5.6600023878414374e-08, 9.657469951514227e-09, 1.138442639414086e-09, 1.207817870279375e-10, 1.1649279441135253e-11, 1.0299309628314363e-12, 8.405335627909787e-14, 6.369675696560244e-15], [3.272485107182575e-05, 3.471906142511031e-05, 1.841739819678469e-05, 6.5132435885032975e-06, 1.7275380698419765e-06, 3.66562403779421e-07, 6.481670756891933e-08, 9.823793485697354e-09, 1.3412167512030127e-09, 2.0341978812251118e-10, 2.1581592849444104e-11, 2.081522488401569e-12, 1.8403064940347875e-13, 1.501886466065589e-14, 1.138149640345737e-15], [5.197652021105753e-06, 5.514390253176222e-06, 2.92521505295537e-06, 1.0344912992097394e-06, 2.743829672606765e-07, 5.822070250782027e-08, 1.029476621169596e-08, 1.5603022899566596e-09, 2.0692313819796395e-10, 2.5111709494270436e-11, 3.427780601549315e-12, 3.306059222415244e-13, 2.922938517635949e-14, 2.3854297178262644e-15, 1.807710527231977e-16], [7.429836067363236e-07, 7.882600725519284e-07, 4.1814781399348063e-07, 1.4787640140262464e-07, 3.9221949798590464e-08, 8.322416999124213e-09, 1.4715957319601173e-09, 2.2303898342627375e-10, 2.9578836542199905e-11, 3.4868147571735446e-12, 3.808365367184667e-13, 4.725879676399341e-14, 4.1782239235778474e-15, 3.40987655227739e-16, 2.584050032599727e-17], [9.655140045357346e-08, 1.024351186708401e-07, 5.4338691556082654e-08, 1.921667385391609e-08, 5.096928313409749e-09, 1.0815057144447018e-09, 1.912352137167342e-10, 2.8984120255550293e-11, 3.843796910246303e-12, 4.531147724861822e-13, 4.807270041976369e-14, 4.773265211831067e-15, 5.429640271635662e-16, 4.431165822653528e-17, 3.3579966937029367e-18], [1.1501364374584497e-08, 1.2202242733430298e-08, 6.472915859207857e-09, 2.289122343364827e-09, 6.07154629019079e-10, 1.2883077031083573e-10, 2.2780258638146916e-11, 3.4526369018971714e-12, 4.578795194990728e-13, 5.397578986310452e-14, 5.7265005106146e-15, 5.523150990680647e-16, 5.0270754292690753e-17, 5.27847887147425e-18, 4.0001018484966013e-19], [1.2646724018872137e-09, 1.341739912196773e-09, 7.11751908753345e-10, 2.517083850151011e-10, 6.676179260047473e-11, 1.416603408253211e-11, 2.504882331280631e-12, 3.796466628964155e-13, 5.0347730307498877e-14, 5.935095140605695e-15, 6.296772208322421e-16, 6.073172192340163e-17, 5.36938624839825e-18, 4.511189031008879e-19, 4.398450694867614e-20], [1.291284793703214e-10, 1.369974028957179e-10, 7.26729242522363e-11, 2.570050627597871e-11, 6.816665521973574e-12, 1.4464128710769899e-12, 2.55759235322271e-13, 3.876355347414561e-14, 5.140719323559794e-15, 6.059986833593812e-16, 6.429274640520607e-17, 6.200969428768676e-18, 5.482373778165317e-19, 4.474201990825399e-20, 3.490577482457789e-21]] |
| Legacy trial inputs | {"lambda_home": 1.4294600787419822, "lambda_away": 1.0609387144011009, "rho": -0.11082685883326926, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4027 |
| Legacy p draw | 0.2754 |
| Legacy p away | 0.3219 |
| Legacy p over 1 5 | 0.7240 |
| Legacy p under 3 5 | 0.7605 |
| Legacy p btts yes | 0.5088 |
| Legacy p over 2 5 | 0.4590 |
| Legacy goal margin distribution | {"-1": 0.19332871065982293, "-10": 5.724857371956861e-08, "-11": 5.4594086799838975e-09, "-12": 4.779754776212918e-10, "-13": 3.849896505487956e-11, "-14": 2.6323500429954344e-12, "-2": 0.09093236343184868, "-3": 0.028767371943177855, "-4": 0.007115657917678455, "-5": 0.0014395553719769414, "-6": 0.00024589711083390365, "-7": 3.630556839088059e-05, "-8": 4.717015890104112e-06, "-9": 5.46958910051864e-07, "0": 0.2753937136579632, "1": 0.20107704236798715, "10": 8.521501663169086e-07, "11": 1.0949109560203309e-07, "12": 1.2915777211033506e-08, "13": 1.4016698047829315e-09, "14": 1.291284793703214e-10, "2": 0.12462812791947599, "3": 0.05312262346778975, "4": 0.01770419242026975, "5": 0.00482582054427017, "6": 0.0011106518725317893, "7": 0.00022094262075055717, "8": 3.86772273892717e-05, "9": 6.0426081157626e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4410 |
| Legacy raw p draw | 0.2929 |
| Legacy raw p away | 0.2661 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4295 |
| Legacy lambda away | 1.0609 |
| Legacy model home team | Union Berlin |
| Legacy model away team | FC Koln |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01168409266038481, "mu": 10.176468642637284, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,423.5449 |
| Elo away rating | 1,399.5689 |
| Elo rating diff | 83.9760 |
| Elo home expectancy | 0.6186 |

</details>


---
