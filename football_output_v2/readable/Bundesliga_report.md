# Bundesliga — football model report

Fixtures in this report: **8**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,596 |
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
| Training sha256 | a6e137f395277b07dd8371ce84c711b7685e06eff8e056fddaa069df2df72c97 |
| Training as of utc | 2026-10-31T11:37:21.613878+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 64, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 64, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 64, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-31T11:37:21.613878+00:00', 'observations': 344, 'observations_sha256': '57e685e69923ba72d50eca36e40633d2241d396e49c1437718711289d57a0011', 'eligible_training_matches': 69, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 105, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 15, 'retrospective_eligible_training_matches': 69, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'a922e60a3d306786e67e6880adc79d7adde0d3e5a2fc5ed54fc2297e4686ce31', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-31', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1592, 'tune_start_date': '2025-11-01', 'audit_start_date': '2026-05-02', 'training_shot_matches': 1296, 'tuning_matches': 206, 'audit_matches': 84, 'audit_matchdays': 27, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.7195544279347862, 'audit_candidate_poisson_score': 0.7082647731827235, 'audit_gain': 0.011289654752062672, 'audit_gain_lower95': 0.002656610885075427, 'audit_baseline_briers': [0.6263962287424126, 0.153684165257626, 0.29449877252531215, 0.2450227059534969], 'audit_candidate_briers': [0.6204096743402818, 0.15115592184763776, 0.2912163681860282, 0.24278228320516007], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1576.584 |
| Base scoring parameter | 0.227 |
| Home-advantage parameter | 0.230 |
| Dixon-Coles low-score adjustment | -0.073 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1596, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-30'} |
| Training data health | {'training_end': '2026-10-30', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 8.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 17.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261031T113721613878Z_e8de525dec6b049d5c69ec181a8d7bfe09419f7767688ab40a2d16248134f147.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 6, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 8 |
| Goal rate features used | {'shot_features': 8} |
| Legacy comparison status | {'AVAILABLE': 8} |
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

## 2026-10-31 — Augsburg vs SC Freiburg

The model's most likely 1X2 outcome is **SC Freiburg win** at **39.0%**. Expected goals are 1.52 for Augsburg and 1.45 for SC Freiburg (2.97 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 61.2%; Under 3.5 goals: 60.9%; Double Chance 1X: 61.0%; Double Chance X2: 64.8%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 64.2%; BTTS No (at least one team does not score): 35.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 35.2% | 2.84 |
| Draw | 25.8% | 3.88 |
| SC Freiburg win | 39.0% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.52 |
| SC Freiburg expected goals | 1.45 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 61.2% |
| Under 2.5 | 38.8% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.3% |
| Under 4.5 | 78.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.63% |
| 2 | 1-2 | 8.86% |
| 3 | 2-1 | 7.72% |
| 4 | 2-2 | 6.81% |
| 5 | 0-1 | 6.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 35.2% | 33.9% | 2.88 | +1.5% |
| Draw | 25.8% | 25.6% | 3.78 | -2.5% |
| SC Freiburg win | 39.0% | 40.5% | 2.42 | -5.7% |

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
| Market best home last update utc | 2026-10-31T11:37:47Z |
| Market best draw last update utc | 2026-10-31T11:37:47Z |
| Market best away last update utc | 2026-10-31T11:37:47Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Augsburg |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5046 |
| Dc lambda away | 1.4542 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:37:21.613878+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.5704 |
| Shot lambda away | 1.4329 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 64.2% |
| P btts no | 35.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.59 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.97 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.57 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.69 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.19672634400476416, "-10": 1.256639197104609e-06, "-11": 1.737877721781234e-07, "-12": 2.209238586957995e-08, "-13": 2.596544571448586e-09, "-14": 2.80931503216336e-10, "-15": 2.485890947533124e-11, "-2": 0.11748912257851137, "-3": 0.05110421398495186, "-4": 0.01773443643299367, "-5": 0.005093211555579393, "-6": 0.001244179180540576, "-7": 0.0002639945890667955, "-8": 4.9460410180436035e-05, "-9": 8.290439624018438e-06, "0": 0.2578087718342721, "1": 0.17174234425290086, "10": 1.6517816915236379e-06, "11": 2.3911152414061705e-07, "12": 3.181728790178046e-08, "13": 3.914313137664548e-09, "14": 4.433017771873184e-10, "15": 4.1060132646975016e-11, "2": 0.10715828134680212, "3": 0.04878923829878928, "4": 0.017722458285324014, "5": 0.005327672649311747, "6": 0.0013622850554218255, "7": 0.0003025654496674456, "8": 5.9336410142684324e-05, "9": 1.0410710287017212e-05} |
| Raw goal margin distribution | {"-1": 0.18456262950409563, "-10": 7.098608386191005e-07, "-11": 9.20577792474776e-08, "-12": 1.0970387331878314e-08, "-13": 1.2085948885640988e-09, "-14": 1.228170736615524e-10, "-15": 1.0353215468329164e-11, "-2": 0.10637022710373571, "-3": 0.04408140905904818, "-4": 0.014489080951860887, "-5": 0.003927517709807751, "-6": 0.000903536269290602, "-7": 0.00018027964030970946, "-8": 3.172824570889131e-05, "-9": 4.992006303192924e-06, "0": 0.260947798334174, "1": 0.19357714924749295, "10": 1.1208969213455717e-06, "11": 1.5215709159993114e-07, "12": 1.8979855939100388e-08, "13": 2.1887237437282866e-09, "14": 2.3281351468743418e-10, "15": 2.054300350769518e-11, "2": 0.11654632352618124, "3": 0.05055605827916608, "4": 0.01739393417778034, "5": 0.004935309366137708, "6": 0.0011884504121287055, "7": 0.00024821121694774815, "8": 4.572566465159244e-05, "9": 7.530578459576744e-06} |
| Unadjusted home-win probability | 38.4% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 80.4% |
| Raw p under 3 5 | 65.4% |
| Raw p btts yes | 60.6% |
| P home draw | 61.0% |
| P draw away | 64.8% |
| P home away | 74.2% |
| Raw p home draw | 64.5% |
| Raw p draw away | 61.6% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0688 |
| Totals anchor target over 2 5 | 0.6116 |
| Totals anchor reference over odds | 1.59 |
| Totals anchor reference under odds | 2.44 |
| Totals anchor reference last update utc | 2026-10-31T11:37:47Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5705 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.45, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.8, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.19, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.24, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.11, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.17, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.14, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.71, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.14, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.88 |
| Reference draw odds | 3.78 |
| Reference away odds | 2.42 |
| Market reference 1x2 last update utc | 2026-10-31T11:37:47Z |
| Market reference home last update utc | 2026-10-31T11:37:47Z |
| Market reference draw last update utc | 2026-10-31T11:37:47Z |
| Market reference away last update utc | 2026-10-31T11:37:47Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-31T11:37:27Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:37:27Z |
| Home probability edge | +1.4% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -1.2% |
| Under 2.5 probability edge | +1.2% |
| Raw edge prob home | 0.0457 |
| Raw ev home | 0.1074 |
| Raw edge prob draw | 0.0045 |
| Raw ev draw | -0.0136 |
| Raw edge prob away | -0.0502 |
| Raw ev away | -0.1420 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0711080536411314, 0.07692517619878289, 0.06488785317620863, 0.030964290160898137, 0.011082050240180814, 0.0031729928091419096, 0.0007570713562822636, 0.00015483094073160414, 2.7706823812303485e-05, 4.407204584353087e-06, 6.309314680719853e-07, 8.211234990021831e-08, 9.795942166552494e-09, 1.0787525558341363e-09, 1.1030946531686549e-10], [0.06934346939715652, 0.1270068370420058, 0.08868034655895389, 0.042317997098218936, 0.01514551657633366, 0.004336437224693742, 0.00103466746022019, 0.00021160295509918068, 3.786611233770693e-05, 6.02319865376502e-06, 8.622757342831603e-07, 1.122205665542241e-07, 1.3387829981711579e-08, 1.4742998237735514e-09, 1.507567462043766e-10], [0.05631736045262048, 0.0806234297233713, 0.05592641147081595, 0.028917389500927662, 0.010349469069012957, 0.002963241478129135, 0.0007070250012466226, 0.0001445958100982017, 2.5875258623746143e-05, 4.1158654344658686e-06, 5.892236158434351e-07, 7.668429641250329e-08, 9.148379429555868e-09, 1.0074414000799468e-09, 1.0301743581498418e-10], [0.025655767593674824, 0.036728567513883585, 0.026290144442111422, 0.012157867266306506, 0.004714773047218827, 0.001349925388473726, 0.000322090186207528, 6.587163299351659e-05, 1.1787655109219028e-05, 1.87501129642489e-06, 2.68424940858188e-07, 3.493406777291729e-08, 4.167608258219064e-09, 4.5894697863977794e-10, 4.6930313674574345e-11], [0.008765748326056725, 0.012548966934150937, 0.008982494434976236, 0.004286419575293281, 0.0014866898228401738, 0.0004612259668750808, 0.00011004782843776653, 2.2506212474028525e-05, 4.027461570366154e-06, 6.40630886328501e-07, 9.171214493615978e-08, 1.1935844249629791e-08, 1.423937326363628e-09, 1.5680738044852965e-10, 1.603457456621328e-11], [0.0023959787891034696, 0.003430061813434714, 0.002455222912967732, 0.0011716250571639037, 0.0004193219892552669, 0.00011634917636381852, 3.0079834934343737e-05, 6.1517175379693075e-06, 1.1008429785557832e-06, 1.751063295674308e-07, 2.506806558853969e-08, 3.262474416148385e-09, 3.8921076719010966e-10, 4.286081958487702e-11, 4.382797580298265e-12], [0.0005457524507414374, 0.0007812943292277926, 0.0005592469883133034, 0.0002668709961896345, 9.5512533051875e-05, 2.7346977679067413e-05, 6.323299696752173e-06, 1.401228983279971e-06, 2.5074836061179234e-07, 3.988545680636919e-08, 5.7099663371443224e-09, 7.431215235258624e-10, 8.865384410537217e-11, 9.762773124542499e-12, 9.98307051560516e-13], [0.00010655200604499978, 0.0001525388992348193, 0.00010918666219171702, 5.210354980651306e-05, 1.8647744018905445e-05, 5.339188723777221e-06, 1.2739224737323397e-06, 2.5248212653506333e-07, 4.8955787187732875e-08, 7.787185250320207e-09, 1.1148064783686965e-09, 1.450860897817772e-10, 1.7308662416806e-11, 1.9060712591743402e-12, 1.9490818382607308e-13], [1.8202691952534194e-05, 2.6058811059619365e-05, 1.8652780468176883e-05, 8.901051251545039e-06, 3.18566634815391e-06, 9.121142925672931e-07, 2.176291110931018e-07, 4.4507984249459255e-08, 7.71851262533888e-09, 1.3303150222158441e-09, 1.904467092235203e-10, 2.478561875015344e-11, 2.956905850749215e-12, 3.2562153692044604e-13, 3.32969200759633e-14], [2.7641212263274833e-06, 3.957091235218274e-06, 2.8324682171494088e-06, 1.3516453920761496e-06, 4.837508647562133e-07, 1.3850668261025693e-07, 3.3047488086259454e-08, 6.75864121228794e-09, 1.2094512918063773e-09, 1.8643676281077613e-10, 2.891977696604717e-11, 3.763754013615636e-12, 4.490130496972974e-13, 4.944638981411079e-14, 5.0562149704723455e-15], [3.7776442937020596e-07, 5.408041797154416e-07, 3.871052143332879e-07, 1.8472545465269708e-07, 6.611282733962253e-08, 1.8929306508651985e-08, 4.516504326986926e-09, 9.23683887869909e-10, 1.6529219946960609e-10, 2.6292314997750323e-11, 3.647661311680053e-12, 5.143813425044339e-13, 6.136531092887001e-14, 6.757694653415065e-15, 6.910182320879445e-16], [4.693451698077848e-08, 6.719103489560114e-08, 4.809504242038765e-08, 2.295081091312202e-08, 8.214043928360183e-09, 2.351830370175021e-09, 5.611432219336584e-10, 1.1476108852381252e-10, 2.0536368539859964e-11, 3.2666312886663094e-12, 4.676480147813795e-13, 5.898099436515199e-14, 7.624199114309083e-15, 8.395950221951739e-16, 8.585405196044932e-17], [5.345336900125485e-09, 7.65233651668697e-09, 5.477508271110677e-09, 2.6138506232408013e-09, 9.35491295830251e-10, 2.678481950859485e-10, 6.390818023514977e-11, 1.3070054208422528e-11, 2.3388715941328695e-12, 3.720341848529847e-13, 5.3260081289535274e-14, 6.93151420062222e-15, 8.013690243433628e-16, 9.562084670306752e-17, 9.777853517858204e-18], [5.619474519074443e-10, 8.044789481070093e-10, 5.75842434866984e-10, 2.74790293828322e-10, 9.834683197630848e-11, 2.8158489079149223e-11, 6.718573536186472e-12, 1.3740356867951185e-12, 2.4588215059574895e-13, 3.911140983381047e-14, 5.59915446458297e-15, 7.286999520663482e-16, 8.693336137482219e-17, 9.277453799665392e-18, 1.0279314423297939e-18], [5.485694861403575e-11, 7.8532717191942e-11, 5.6213367908432545e-11, 2.68248516422828e-11, 9.600554446443415e-12, 2.7488135825165982e-12, 6.558628248658838e-13, 1.3413247948455128e-13, 2.400285730374875e-14, 3.818030657836694e-15, 5.465858554978669e-16, 7.113522036601023e-17, 8.48637879146302e-18, 9.34540308162025e-19, 9.260953048664748e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3666709903028336, "lambda_away": 1.431591059584538, "rho": -0.1107929355926174, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3422 |
| Legacy p draw | 0.2678 |
| Legacy p away | 0.3900 |
| Legacy p over 1 5 | 0.7826 |
| Legacy p under 3 5 | 0.6915 |
| Legacy p btts yes | 0.5778 |
| Legacy p over 2 5 | 0.5344 |
| Legacy goal margin distribution | {"-1": 0.19973044265222006, "-10": 7.527753956089713e-07, "-11": 9.655455159568442e-08, "-12": 1.137325942614103e-08, "-13": 1.229509302038513e-09, "-14": 1.1030946531686549e-10, "-2": 0.11902170300770852, "-3": 0.04941878648252581, "-4": 0.016195592525074097, "-5": 0.004364710194282301, "-6": 0.0009965196465141798, "-7": 0.00019709367845733327, "-8": 3.435564794613785e-05, "-9": 5.350493413484999e-06, "0": 0.26780879210994374, "1": 0.1809914517715431, "10": 4.507173633851925e-07, "11": 5.518952078397472e-08, "12": 6.206029216140927e-09, "13": 6.404801690993863e-10, "14": 5.485694861403575e-11, "2": 0.10330112373678502, "3": 0.04094642228738065, "4": 0.012810489484285965, "5": 0.003295864086408766, "6": 0.0007183643058004382, "7": 0.0001356364995212507, "8": 2.257080351864661e-05, "9": 3.3557353947321124e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3457 |
| Legacy raw p draw | 0.2792 |
| Legacy raw p away | 0.3751 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3667 |
| Legacy lambda away | 1.4316 |
| Legacy model home team | Augsburg |
| Legacy model away team | Freiburg |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 59.9% |
| Market home draw odds | 1.62 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:37:38Z |
| Market reference home draw last update utc | 2026-10-31T11:37:38Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 66.0% |
| Market draw away odds | 1.47 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:37:38Z |
| Market reference draw away last update utc | 2026-10-31T11:37:38Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:37:38Z |
| Market reference home away last update utc | 2026-10-31T11:37:38Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.62 |
| Market reference dc draw away odds | 1.47 |
| Market reference dc home away odds | 1.31 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.56, "price": 1.48, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.48, "price": 2.56, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.98, "price": 1.84, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.84, "price": 1.98, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.6, "price": 2.29, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.29, "price": 1.6, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-31T11:37:24Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.2% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market reference under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.4% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:37:38Z |
| Market reference btts yes odds | 1.54 |
| Market reference btts yes opposite odds | 2.76 |
| Market reference btts yes last update utc | 2026-10-31T11:37:48Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 9.859727763945733, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,473.6758 |
| Elo away rating | 1,485.2934 |
| Elo rating diff | 48.3824 |
| Elo home expectancy | 0.5692 |

</details>


---

## 2026-10-31 — Bayer Leverkusen vs VfB Stuttgart

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **57.0%**. Expected goals are 2.13 for Bayer Leverkusen and 1.41 for VfB Stuttgart (3.54 combined). The most likely exact score is 2-1 at 9.9%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 69.0%; Under 3.5 goals: 52.5%; Double Chance 1X: 78.3%; Double Chance X2: 43.0%; Double Chance 12 (either team wins): 78.7%; Under 4.5 goals: 71.5%; BTTS Yes (both teams score): 66.9%; BTTS No (at least one team does not score): 33.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 57.0% | 1.75 |
| Draw | 21.3% | 4.69 |
| VfB Stuttgart win | 21.7% | 4.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.13 |
| VfB Stuttgart expected goals | 1.41 |
| Expected total goals | 3.54 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 87.6% |
| Under 1.5 | 12.4% |
| Over 2.5 | 69.0% |
| Under 2.5 | 31.0% |
| Over 3.5 | 47.5% |
| Under 3.5 | 52.5% |
| Over 4.5 | 28.5% |
| Under 4.5 | 71.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.91% |
| 2 | 1-1 | 9.03% |
| 3 | 3-1 | 7.04% |
| 4 | 2-0 | 7.03% |
| 5 | 2-2 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 57.0% | 58.6% | 1.68 | -4.2% |
| Draw | 21.3% | 21.0% | 4.54 | -3.1% |
| VfB Stuttgart win | 21.7% | 20.4% | 4.67 | +1.1% |

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
| Market best home last update utc | 2026-10-31T11:37:47Z |
| Market best draw last update utc | 2026-10-31T11:37:47Z |
| Market best away last update utc | 2026-10-31T11:37:47Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Leverkusen |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1770 |
| Dc lambda away | 1.3747 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:37:21.613878+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9414 |
| Shot lambda away | 1.5542 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 66.9% |
| P btts no | 33.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.25 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.08 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.23 |
| Fair Over 3.5 odds | 2.11 |
| Fair Under 3.5 odds | 1.90 |
| Fair Over 4.5 odds | 3.51 |
| Fair Under 4.5 odds | 1.40 |
| Goal margin distribution | {"-1": 0.1197261904674191, "-10": 2.881055717069655e-07, "-11": 3.613887196189593e-08, "-12": 4.169174719544024e-09, "-13": 4.4514711987971145e-10, "-14": 4.4225711309423004e-11, "-15": 4.10505851769432e-12, "-16": 3.5361166318307205e-13, "-17": 2.49350035838831e-14, "-2": 0.06269085113111354, "-3": 0.02415927732936644, "-4": 0.007491034473764411, "-5": 0.0019322162298775535, "-6": 0.0004253360862782915, "-7": 8.15093041610326e-05, "-8": 1.3814041284661598e-05, "-9": 2.096969861055402e-06, "0": 0.213355355406089, "1": 0.22238649973377228, "10": 2.148624978486497e-05, "11": 4.0694188483536466e-06, "12": 7.088538989561744e-07, "13": 1.1427705545273254e-07, "14": 1.7142696536531576e-08, "15": 2.4025503607373307e-09, "16": 3.124845612603387e-10, "17": 3.327057113717329e-11, "2": 0.1730702551833843, "3": 0.10070500235986957, "4": 0.0471473988409767, "5": 0.018362022036294768, "6": 0.006103034795837639, "7": 0.0017659143591799704, "8": 0.00045188927998595854, "9": 0.00010357437341932374} |
| Raw goal margin distribution | {"-1": 0.135723391912418, "-10": 3.2660076519829364e-07, "-11": 4.096756326588255e-08, "-12": 4.726238529789387e-09, "-13": 5.046254021300323e-10, "-14": 5.013492474136406e-11, "-15": 4.653555448856053e-12, "-16": 4.00859445703807e-13, "-17": 2.8266691277326394e-14, "-2": 0.07106728213912905, "-3": 0.027387316446744376, "-4": 0.008491948200664052, "-5": 0.002190389083653094, "-6": 0.0004821673195068546, "-7": 9.24001606496182e-05, "-8": 1.5659802853934945e-05, "-9": 2.377156252691436e-06, "0": 0.22082760270003746, "1": 0.2081868844120309, "10": 2.0114329807630856e-05, "11": 3.8095821123159766e-06, "12": 6.635928210735515e-07, "13": 1.0698034351440582e-07, "14": 1.604811706930895e-08, "15": 2.2491449563875978e-09, "16": 2.9253208856441587e-10, "17": 3.11462096662744e-11, "2": 0.1620195347026821, "3": 0.09427488049457158, "4": 0.0441369871129085, "5": 0.017189587334742025, "6": 0.005713349511434846, "7": 0.00165315884289857, "8": 0.00042303566723742877, "9": 9.696103914990791e-05} |
| Unadjusted home-win probability | 53.4% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 52.8% |
| Raw p btts yes | 67.3% |
| P home draw | 78.3% |
| P draw away | 43.0% |
| P home away | 78.7% |
| Raw p home draw | 75.5% |
| Raw p draw away | 46.6% |
| Raw p home away | 77.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6901 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.33, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 7.29, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.74, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.39, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.68, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.56, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:36:34Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.13, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.13, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.68 |
| Reference draw odds | 4.54 |
| Reference away odds | 4.67 |
| Market reference 1x2 last update utc | 2026-10-31T11:37:47Z |
| Market reference home last update utc | 2026-10-31T11:37:47Z |
| Market reference draw last update utc | 2026-10-31T11:37:47Z |
| Market reference away last update utc | 2026-10-31T11:37:47Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.31 |
| Reference Under 2.5 odds | 3.51 |
| Market reference over 2 5 last update utc | 2026-10-31T11:37:27Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:37:27Z |
| Home probability edge | -1.6% |
| Draw probability edge | +0.3% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | -0.0520 |
| Raw ev home | -0.1034 |
| Raw edge prob draw | 0.0107 |
| Raw ev draw | 0.0026 |
| Raw edge prob away | 0.0413 |
| Raw ev away | 0.1463 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.03849857404436158, 0.02842499878784369, 0.023477276768468176, 0.00964303086077411, 0.0029705759242932735, 0.0007320786544725383, 0.00015034659102954555, 2.6465654393174443e-05, 4.0764276759101515e-06, 5.581158080098751e-07, 6.877196210107448e-08, 7.703814583663586e-09, 7.910640840990187e-10, 7.498172137037688e-11, 6.5995521082473874e-12, 5.42138556142844e-13, 4.17520115242006e-14, 3.026325058640179e-15, 2.071715714944442e-16], [0.05748545081703091, 0.0920221183476888, 0.05383373576664699, 0.02211160947106759, 0.006811573631825502, 0.0016786669609913417, 0.00034474691143783736, 6.0686128955428836e-05, 9.347307719757843e-06, 1.279767633695306e-06, 1.5769510545939977e-07, 1.7664958452472457e-08, 1.8139214057001466e-09, 1.7193417343031095e-10, 1.5132868597893554e-11, 1.2431315636873007e-12, 9.573796732415781e-14, 6.939407204571104e-15, 4.75047414918754e-16], [0.07632783032015289, 0.09405242744785193, 0.05851847723477497, 0.02535112043402487, 0.007809518511602905, 0.0019246038309600868, 0.00039525483129368736, 6.957708645482694e-05, 1.0716756012154294e-05, 1.4672628626074542e-06, 1.8079858074503508e-07, 2.0253002829877354e-08, 2.0796740315954876e-09, 1.9712377532081497e-10, 1.734994346926433e-11, 1.42525934295333e-12, 1.097642730584224e-13, 7.95608062877605e-15, 5.446453024251995e-16], [0.058340273584815215, 0.07188785958684477, 0.044290710674032535, 0.018371490700244016, 0.0059691130302219194, 0.0014710481559561512, 0.0003021083515235902, 5.318042242237305e-05, 8.191225599736691e-06, 1.1214850005078272e-06, 1.3819125501366036e-07, 1.5480142970828185e-08, 1.5895742281892408e-09, 1.5066922424036946e-10, 1.3261223913117141e-11, 1.089380107471194e-12, 8.389702279243165e-14, 6.0811360495739236e-15, 4.1629318974341453e-16], [0.033443773139576936, 0.041209975884274254, 0.025389810313788477, 0.0104285827875018, 0.003244279818188403, 0.0008432836835032529, 0.0001731847067401529, 3.0485869771848925e-05, 4.695649743473115e-06, 6.428953385330765e-07, 7.92186374620156e-08, 8.874048026736454e-09, 9.112291837094827e-10, 8.637167851613394e-11, 7.602044640031612e-12, 6.244910923166688e-13, 4.809427218878008e-14, 3.486033266148207e-15, 2.38641578824432e-16], [0.01533741126784989, 0.018899014349769202, 0.011643840578934058, 0.004782578284011135, 0.0014732932116107349, 0.0003666673050478949, 7.9423008327741e-05, 1.398090821264538e-05, 2.1534385783820097e-06, 2.9483366509255403e-07, 3.632989668249506e-08, 4.06966413833384e-09, 4.1789234400949154e-10, 3.961030203642923e-11, 3.486319699458219e-12, 2.8639342444991617e-13, 2.2056172582821396e-14, 1.5987049569191471e-15, 1.0944171953217697e-16], [0.005861484374022209, 0.007222618951856736, 0.0044499158570581576, 0.0018277535491293565, 0.0005630471131925205, 0.00013875921152518337, 2.8778196661480643e-05, 5.343070847610377e-06, 8.229776431738239e-07, 1.1267631092988024e-07, 1.3884163239507274e-08, 1.5552998050176449e-09, 1.5970553319970617e-10, 1.5137832739969165e-11, 1.332363596720901e-12, 1.0945071191738506e-13, 8.429187213356139e-15, 6.109756046834555e-16, 4.182524141141489e-17], [0.0019200669414657426, 0.002365938556746125, 0.0014576745043130594, 0.0005987236240675616, 0.00018443931256048463, 4.5453840336783496e-05, 9.334830215423253e-06, 1.6594393582227265e-06, 2.695856655741828e-07, 3.6909773343696444e-08, 4.54808392294638e-09, 5.094749979915549e-10, 5.2315300203639783e-11, 4.958752826889724e-12, 4.3644700434827155e-13, 3.585315259115035e-14, 2.761178343069579e-15, 2.0013941618507506e-16, 1.3700840645212545e-17], [0.0005503426643159871, 0.000678141423513913, 0.00041780859462990134, 0.00017161024302971898, 5.286525198004782e-05, 1.30282893028942e-05, 2.6756126157620594e-06, 4.709906509610214e-07, 7.326141502657162e-08, 1.057933062779703e-08, 1.303602790940336e-09, 1.4602919395248442e-10, 1.4994967663254e-11, 1.4213115092495928e-12, 1.250974130216514e-13, 1.0276474791070906e-14, 7.914277430434198e-16, 5.736532261414678e-17, 3.927028261993318e-18], [0.00014021596695429526, 0.00017277645655175015, 0.00010644901785083169, 4.3722752615555576e-05, 1.3468976521887196e-05, 3.3193395693500927e-06, 6.816909435514576e-07, 1.1999870959125662e-07, 1.8483051791738832e-08, 2.555548774122075e-09, 3.3213112067769485e-10, 3.7205228598899894e-11, 3.820408677500512e-12, 3.6212087583723085e-13, 3.187224227311673e-14, 2.618233953390388e-15, 2.0163947565870187e-16, 1.4615501761952042e-17, 1.0005258554624529e-18], [3.215172436617715e-05, 3.961789180420073e-05, 2.4408914015518756e-05, 1.002569051985439e-05, 3.088455830193616e-06, 7.61129372279525e-07, 1.563127209836946e-07, 2.7515877962262515e-08, 4.238190553915084e-09, 5.802632435935489e-10, 7.22067942993454e-11, 8.531212820308529e-12, 8.760252447225669e-13, 8.303484146675244e-14, 7.308351329426663e-15, 6.003648387848268e-16, 4.6236223901891885e-17, 3.351355728815331e-18, 2.2942202820986897e-19], [6.702215434796744e-06, 8.25858180793408e-06, 5.088181224691423e-06, 2.0899139648432145e-06, 6.438067239898031e-07, 1.586618798006176e-07, 3.2584303078129416e-08, 5.7358460740806195e-09, 8.834756675116652e-10, 1.2095927494169156e-10, 1.490480390033366e-11, 1.6861126412501296e-12, 1.826125979926495e-13, 1.73090994985579e-14, 1.5234686800975668e-15, 1.2514957030565488e-16, 9.638211933913246e-18, 6.986097491178288e-19, 4.782436677542913e-20], [1.2806897577539801e-06, 1.5780873112616201e-06, 9.722727721085302e-07, 3.9935024998832894e-07, 1.230215121265927e-07, 3.031783242175151e-08, 6.226356586369173e-09, 1.0960315123548696e-09, 1.6881854210963066e-10, 2.3113447490646055e-11, 2.848077606903692e-12, 3.1904079995890565e-13, 3.308399775169948e-14, 3.3075013268981752e-15, 2.9111131294440383e-16, 2.391414815549339e-17, 1.8417133001632937e-18, 1.3349352300989027e-19, 9.13849715757746e-21], [2.2589539761854577e-07, 2.783520821462723e-07, 1.7149504251078218e-07, 7.043968530550923e-08, 2.1699239202325104e-08, 5.347632998841877e-09, 1.098240450723511e-09, 1.9332431823306652e-10, 2.977718176033388e-11, 4.076882304728998e-12, 5.023602473313262e-13, 5.627424434911464e-14, 5.778505321090776e-15, 5.531273947767325e-16, 5.134788139803771e-17, 4.218114475880528e-18, 3.2485194460317637e-19, 2.3546352484855682e-20, 1.6119004907693422e-21], [3.699867282073759e-08, 4.55903826499894e-08, 2.8088615505790148e-08, 1.1537087066355928e-08, 3.554047847674419e-09, 8.758714244529909e-10, 1.79877233193717e-10, 3.1663961612337654e-11, 4.877107798958443e-12, 6.6773929930186e-13, 8.227995180558123e-14, 9.216975542029363e-15, 9.464426014068397e-16, 8.970941401361792e-17, 7.973756832305954e-18, 6.908712574881959e-19, 5.320644395707929e-20, 3.856580527506124e-21, 2.640079413139182e-22], [5.6558995207465845e-09, 6.969293861703114e-09, 4.293840153330842e-09, 1.7636471860915047e-09, 5.432988803616074e-10, 1.3389239105416488e-10, 2.7497406783827534e-11, 4.840394848103324e-12, 7.455519228056617e-13, 1.0207572582950179e-13, 1.2577941436953454e-14, 1.4089772301691333e-15, 1.446804397997425e-16, 1.3713665735644709e-17, 1.2070148559330026e-18, 1.0013233864784393e-19, 8.133543122898304e-21, 5.8954633488952405e-22, 4.035826895698132e-23], [8.105662214503369e-10, 9.987932372094255e-10, 6.153648550209205e-10, 2.527542843287654e-10, 7.786201274572435e-11, 1.9188574531712936e-11, 3.940747008445412e-12, 6.936934696175242e-13, 1.0684758502991362e-13, 1.4628819886902477e-14, 1.8025876214344765e-15, 2.019253251191071e-16, 2.0734646536077438e-17, 1.965352138382258e-18, 1.7298140948566418e-19, 1.421003880868163e-20, 1.1051679567124466e-21, 8.448989294955114e-23, 5.7838809640696406e-24], [1.093317699524607e-10, 1.3472043313779403e-10, 8.300238399472805e-11, 3.4092307990932675e-11, 1.0502277840198248e-11, 2.588216435497521e-12, 5.315405872666254e-13, 9.356759858811155e-14, 1.4411944733601567e-14, 1.9731821142127352e-15, 2.431387959804128e-16, 2.7236335057234675e-17, 2.7967555828711533e-18, 2.6509299571441755e-19, 2.333228694640071e-20, 1.916695580117396e-21, 1.476115193112376e-22, 1.0804989073085405e-23, 7.801484027604811e-25], [1.3927740693847846e-11, 1.7161994722320244e-11, 1.057364827947469e-11, 4.3430086749621885e-12, 1.3378819579764197e-12, 3.297120991349443e-13, 6.771279263954274e-14, 1.1919547731166415e-14, 1.8359332262794946e-15, 2.513630652869067e-16, 3.0973376764155715e-17, 3.469628382425948e-18, 3.562778372584466e-19, 3.3770115545290576e-20, 2.9722928891137574e-21, 2.4416726300623232e-22, 1.8804186242349945e-23, 1.3629901399978146e-24, 9.422653306010715e-26]] |
| Legacy trial inputs | {"lambda_home": 2.293014487904744, "lambda_away": 1.2322167033093192, "rho": -0.1107929355926174, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5941 |
| Legacy p draw | 0.2111 |
| Legacy p away | 0.1948 |
| Legacy p over 1 5 | 0.8756 |
| Legacy p under 3 5 | 0.5321 |
| Legacy p btts yes | 0.6466 |
| Legacy p over 2 5 | 0.6838 |
| Legacy goal margin distribution | {"-1": 0.11450729828726058, "-10": 8.867516088070093e-08, "-11": 9.72876816053901e-09, "-12": 9.81487315908452e-10, "-13": 9.162734180900188e-11, "-14": 7.95876772262151e-12, "-15": 6.462488972855213e-13, "-16": 4.92360640311969e-14, "-17": 3.5013724735589332e-15, "-18": 2.071715714944442e-16, "-2": 0.05505747975116578, "-3": 0.01871407335776256, "-4": 0.005102683031412003, "-5": 0.0011552747122690538, "-6": 0.0002229544140912855, "-7": 3.742772375568541e-05, "-8": 5.553426241830089e-06, "-9": 7.377434607958131e-07, "0": 0.21105212097721573, "1": 0.20787904904896423, "10": 4.1456710607914536e-05, "11": 8.463897906550531e-06, "12": 1.5889746205341078e-06, "13": 2.760432066961341e-07, "14": 4.461876172741053e-08, "15": 6.7420381506257e-09, "16": 9.558603028676056e-10, "17": 1.2649376467478096e-10, "18": 1.3927740693847846e-11, "2": 0.17899937943170705, "3": 0.11322002131293861, "4": 0.05744777378356745, "5": 0.024203578783735864, "6": 0.008692207820385704, "7": 0.0027153583285715933, "8": 0.0007497465028197044, "9": 0.0001853439935495661} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6026 |
| Legacy raw p draw | 0.2120 |
| Legacy raw p away | 0.1855 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2930 |
| Legacy lambda away | 1.2322 |
| Legacy model home team | Leverkusen |
| Legacy model away team | Stuttgart |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 79.2% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:37:38Z |
| Market reference home draw last update utc | 2026-10-31T11:37:38Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.2% |
| Market draw away odds | 2.31 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:37:38Z |
| Market reference draw away last update utc | 2026-10-31T11:37:38Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.6% |
| Market home away odds | 1.24 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:37:38Z |
| Market reference home away last update utc | 2026-10-31T11:37:38Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.23 |
| Market reference dc draw away odds | 2.31 |
| Market reference dc home away odds | 1.24 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.36, "price": 1.56, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.56, "price": 2.36, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.9, "price": 1.93, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.93, "price": 1.9, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 1.54, "price": 2.42, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 11.5, "market_key": "alternate_totals_corners", "opposite_price": 2.42, "price": 1.54, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 90.1% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 8.30 |
| Market reference over 1 5 last update utc | 2026-10-31T11:37:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 45.8% |
| Market under 3 5 odds | 2.10 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market reference under 3 5 odds | 2.10 |
| Market reference under 3 5 opposite odds | 1.79 |
| Market reference under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.9% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:37:38Z |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 3.35 |
| Market reference btts yes last update utc | 2026-10-31T11:37:48Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 10.795913207014925, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,573.7409 |
| Elo away rating | 1,532.4073 |
| Elo rating diff | 101.3336 |
| Elo home expectancy | 0.6418 |

</details>


---

## 2026-10-31 — Bayern Munich vs Borussia Dortmund

The model's most likely 1X2 outcome is **Bayern Munich win** at **71.5%**. Expected goals are 2.52 for Bayern Munich and 1.23 for Borussia Dortmund (3.76 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 73.5%; Under 3.5 goals: 47.4%; Double Chance 1X: 87.7%; Double Chance X2: 28.5%; Double Chance 12 (either team wins): 83.8%; Under 4.5 goals: 66.7%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 71.5% | 1.40 |
| Draw | 16.2% | 6.18 |
| Borussia Dortmund win | 12.3% | 8.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 2.52 |
| Borussia Dortmund expected goals | 1.23 |
| Expected total goals | 3.76 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 89.8% |
| Under 1.5 | 10.2% |
| Over 2.5 | 73.5% |
| Under 2.5 | 26.5% |
| Over 3.5 | 52.6% |
| Under 3.5 | 47.4% |
| Over 4.5 | 33.3% |
| Under 4.5 | 66.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.10% |
| 2 | 3-1 | 8.50% |
| 3 | 2-0 | 8.20% |
| 4 | 3-0 | 6.90% |
| 5 | 1-1 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 71.5% | 74.3% | 1.33 | -4.9% |
| Draw | 16.2% | 15.1% | 6.13 | -0.7% |
| Borussia Dortmund win | 12.3% | 10.6% | 8.62 | +6.2% |

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
| Market best home last update utc | 2026-10-31T11:37:47Z |
| Market best draw last update utc | 2026-10-31T11:37:47Z |
| Market best away last update utc | 2026-10-31T11:37:47Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Bayern Munich |
| Matched away-team name | Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5441 |
| Dc lambda away | 1.2728 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:37:21.613878+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 2.4429 |
| Shot lambda away | 1.0663 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.22 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.84 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.78 |
| Fair Over 3.5 odds | 1.90 |
| Fair Under 3.5 odds | 2.11 |
| Fair Over 4.5 odds | 3.00 |
| Fair Under 4.5 odds | 1.50 |
| Goal margin distribution | {"-1": 0.07417817749745807, "-10": 5.1505262228123596e-08, "-11": 5.636030925012732e-09, "-12": 5.672764392212789e-10, "-13": 5.2848448053805274e-11, "-14": 4.581765802735561e-12, "-15": 3.713903372438662e-13, "-16": 2.8245295381451388e-14, "-17": 2.001816653165787e-15, "-18": 1.1678986130039707e-16, "-2": 0.033853664025013656, "-3": 0.011327079722204382, "-4": 0.003054499318523923, "-5": 0.0006859171825644829, "-6": 0.00013154106912739597, "-7": 2.1971046264568853e-05, "-8": 3.246542397922851e-06, "-9": 4.2978701570475747e-07, "0": 0.16192086926701785, "1": 0.2283552632089242, "10": 9.840544166663065e-05, "11": 2.206862149311591e-05, "12": 4.5523003828103085e-06, "13": 8.691660004893812e-07, "14": 1.5443214508057026e-07, "15": 2.5654865605768636e-08, "16": 3.998707073110045e-09, "17": 5.808073373664118e-10, "18": 6.94460046898467e-11, "2": 0.20782537924827715, "3": 0.14250994922767457, "4": 0.07875925276046526, "5": 0.03624662402803015, "6": 0.014245955205602373, "7": 0.004876579087910091, "8": 0.0014767940657552366, "9": 0.0004006696778572054} |
| Raw goal margin distribution | {"-1": 0.09847896323243936, "-10": 6.837839640121039e-08, "-11": 7.482395779543652e-09, "-12": 7.531163137920964e-10, "-13": 7.016161017113852e-11, "-14": 6.082753193049334e-12, "-15": 4.930578857585883e-13, "-16": 3.749845977888388e-14, "-17": 2.6576121877887048e-15, "-18": 1.5505024314351245e-16, "-2": 0.04494413110805965, "-3": 0.015037833297159398, "-4": 0.004055153904161861, "-5": 0.0009106237883045974, "-6": 0.00017463394959516896, "-7": 2.9168765400590302e-05, "-8": 4.310110334654098e-06, "-9": 5.705853277241686e-07, "0": 0.18707066543352766, "1": 0.207421650387204, "10": 8.938449165018665e-05, "11": 2.0045563336478125e-05, "12": 4.134985308382915e-06, "13": 7.894884652472827e-07, "14": 1.4027515703082852e-07, "15": 2.330305196224829e-08, "16": 3.632140590342467e-09, "17": 5.275640017253197e-10, "18": 6.307980251099627e-11, "2": 0.1887737665874809, "3": 0.12944588379535854, "4": 0.07153929347313695, "5": 0.03292385063172338, "6": 0.012940010659551748, "7": 0.004429536978670817, "8": 0.0013414145051726981, "9": 0.0003639397869503673} |
| Unadjusted home-win probability | 64.9% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 16.4% |
| Raw p over 1 5 | 89.4% |
| Raw p under 3 5 | 48.3% |
| Raw p btts yes | 65.7% |
| P home draw | 87.7% |
| P draw away | 28.5% |
| P home away | 83.8% |
| Raw p home draw | 83.6% |
| Raw p draw away | 35.1% |
| Raw p home away | 81.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7354 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 5.7, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 4.15, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.05, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.9, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 5.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:38Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 7.23, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:38Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.12, "price": 7.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.57, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.57, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.33 |
| Reference draw odds | 6.13 |
| Reference away odds | 8.62 |
| Market reference 1x2 last update utc | 2026-10-31T11:37:47Z |
| Market reference home last update utc | 2026-10-31T11:37:47Z |
| Market reference draw last update utc | 2026-10-31T11:37:47Z |
| Market reference away last update utc | 2026-10-31T11:37:47Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.66 |
| Market reference over 2 5 last update utc | 2026-10-31T11:37:27Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:37:27Z |
| Home probability edge | -2.8% |
| Draw probability edge | +1.1% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -2.2% |
| Under 2.5 probability edge | +2.2% |
| Raw edge prob home | -0.0936 |
| Raw ev home | -0.1364 |
| Raw edge prob draw | 0.0359 |
| Raw ev draw | 0.1467 |
| Raw edge prob away | 0.0577 |
| Raw ev away | 0.4105 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.021601094772045484, 0.013148467404307886, 0.012973536135954335, 0.005970535893685699, 0.0020607700062011893, 0.0005690307327956596, 0.00013093648405353774, 2.582491123167846e-05, 4.45681957421398e-06, 6.836892414597955e-07, 9.439194788882094e-08, 1.1847274896708422e-08, 1.3630551314596593e-09, 1.4475923263212772e-10, 1.427560224987413e-11, 1.313951643463536e-12, 1.1337977799078604e-13, 9.207948536678499e-15, 7.06263204692648e-16, 5.1320299502706285e-17], [0.041147252227000004, 0.0634855009094182, 0.03517349642302223, 0.016187153656440776, 0.00558710329105327, 0.001542740563161468, 0.00035499141523464336, 7.001579317414759e-05, 1.2083207362195353e-05, 1.8535995766258323e-06, 2.559128680598011e-07, 3.212000774770119e-08, 3.695477800991355e-09, 3.9246727321124767e-10, 3.8703622467345094e-11, 3.562349767023574e-12, 3.073921538284296e-13, 2.4964338290210457e-14, 1.9148014884795866e-15, 1.3913819270786533e-16], [0.06585154620797248, 0.09091638921784538, 0.05348288527129737, 0.021943084185653616, 0.007573800834388395, 0.002091318015048622, 0.0004812215090439115, 9.491245196985716e-05, 1.637983069839233e-05, 2.5127142436316293e-06, 3.469119850971391e-07, 4.3541443357536364e-08, 5.009539182393693e-09, 5.320232697464811e-10, 5.246610146020241e-11, 4.8290726396755295e-12, 4.166966010594933e-13, 3.384131567338647e-14, 2.595678718587084e-15, 1.8861383173523934e-16], [0.059511637144106434, 0.08216334280894563, 0.056718443866645187, 0.022243631774815253, 0.006844627241315774, 0.0018899747391115738, 0.00043489153226129463, 8.577468149720884e-05, 1.4802849699626406e-05, 2.270800716532446e-06, 3.135127626744037e-07, 3.93494568774553e-08, 4.5272418834366545e-09, 4.808023137585866e-10, 4.741488654806142e-11, 4.364149898125084e-12, 3.7657881020920934e-13, 3.058321656523099e-14, 2.3457777218377915e-15, 1.7045488771269223e-16], [0.04033658083425929, 0.05568975208665054, 0.0384433735250871, 0.01769197997374021, 0.005203781976483902, 0.0012810119582877557, 0.0002947665076447963, 5.8137492762415896e-05, 1.0033270334010684e-05, 1.5391332024542682e-06, 2.1249680736501796e-07, 2.667079287834483e-08, 3.0685336003325095e-09, 3.2588452149720005e-10, 3.213748597374148e-11, 2.9579909675864125e-12, 2.5524254326411594e-13, 2.0729095120806395e-14, 1.589952104106838e-15, 1.1553315766071986e-16], [0.021871886998623604, 0.03019690661500142, 0.02084532462088203, 0.009593202466950331, 0.0033111573666635414, 0.0007791345480390794, 0.00015983257908439664, 3.152415613280893e-05, 5.440385635902496e-06, 8.345711704775336e-07, 1.1522310672174023e-07, 1.4461824872955058e-08, 1.663864878228585e-09, 1.7670584073733554e-10, 1.74260546407176e-11, 1.6039248455845812e-12, 1.384013207875197e-13, 1.1240031174901218e-14, 8.621269337908962e-16, 6.264606758149465e-17], [0.009883076994184552, 0.013644837918239084, 0.009419212352821345, 0.004334804701927992, 0.0014961865520179624, 0.00041313495806512355, 8.101087806737722e-05, 1.424457168496033e-05, 2.458304128997359e-06, 3.771110894764242e-07, 5.2064956046625705e-08, 6.53475069182748e-09, 7.518374935133595e-10, 7.984667392617295e-11, 7.874173807221894e-12, 7.247528639296431e-13, 6.253831274484776e-14, 5.078944195604797e-15, 3.895624948113469e-16, 2.830738423848673e-17], [0.003827818300495319, 0.005284787351293674, 0.0036481587102475056, 0.0016789148538331497, 0.0005794885811513291, 0.0001600114573615671, 3.6819342836320654e-05, 6.188432205585776e-06, 9.521267049418251e-07, 1.4605903915015364e-07, 2.016529788111826e-08, 2.5309767698936715e-09, 2.9119446487793176e-10, 3.09254455740993e-11, 3.0497492449265055e-12, 2.80704306717301e-13, 2.422173763775068e-14, 1.967127803473579e-15, 1.5088159767478595e-16, 1.0963743729912387e-17], [0.0012972345385399737, 0.0017909963699296347, 0.0012363485174821706, 0.0005689785054265319, 0.0001963866994579535, 5.422733598004936e-05, 1.2477949438571561e-05, 2.4610553653840543e-06, 3.6193788294253577e-07, 4.949890913762124e-08, 6.833950526844121e-09, 8.577393764284884e-10, 9.86848088433137e-11, 1.0480527801768588e-11, 1.0335495950507717e-12, 9.512973009807748e-14, 8.208664095439934e-15, 6.666528889466867e-16, 5.1133257738095265e-17, 3.7155752759484515e-18], [0.000390780756585317, 0.0005395222650102854, 0.0003724393659827998, 0.0001713998850829329, 5.915980550737356e-05, 1.6335518946126853e-05, 3.7588750356017977e-06, 7.413717790504996e-07, 1.2794468979970854e-07, 1.6725626759313117e-08, 2.058668866735912e-09, 2.583866159245142e-10, 2.972795058838866e-11, 3.157168932919507e-12, 3.1134793340991726e-13, 2.86570136679553e-14, 2.4727895152877143e-15, 2.0082345372609413e-16, 1.5403454465569757e-17, 1.119285121038343e-18], [0.00010594741017328998, 0.0001462738012182223, 0.00010097474250589124, 4.6469468167303744e-05, 1.6039244702402194e-05, 4.4288412287798945e-06, 1.0190959213727238e-06, 2.0099868952686365e-07, 3.468801444613764e-08, 5.321243521196136e-09, 6.260597438880821e-10, 7.005307277628482e-11, 8.059760675323008e-12, 8.559630081205473e-13, 8.441180035533537e-14, 7.769411185828376e-15, 6.704159317814323e-16, 5.444670564193964e-17, 4.17614245545128e-18, 3.0345752143918526e-19], [2.6112883766593842e-05, 3.605213910431427e-05, 2.4887269165950976e-05, 1.1453341039327773e-05, 3.953196514504084e-06, 1.091577567008656e-06, 2.511768178031853e-07, 4.9540195539162807e-08, 8.54956329601985e-09, 1.3115281754925444e-09, 1.810730543769901e-10, 1.9367063970998077e-11, 1.9864911596898366e-12, 2.1096940928520087e-13, 2.080499681495281e-14, 1.914928650908715e-15, 1.6523757657924088e-16, 1.3419492685818889e-17, 1.0292948393318023e-18, 7.479324857945261e-20], [5.89971136970669e-06, 8.145297810733304e-06, 5.622806970371771e-06, 2.587665420442543e-06, 8.931498578162135e-07, 2.466212709618998e-07, 5.6748643353437345e-08, 1.1192668626427062e-08, 1.931611852386945e-09, 2.963149439106675e-10, 4.091002614663696e-11, 5.134678716044784e-12, 5.034248775857569e-13, 4.7664541141660226e-14, 4.700494872684803e-15, 4.3264184970624105e-16, 3.733229994668211e-17, 3.031880135563768e-18, 2.3254966861051346e-19, 1.689811753330731e-20], [1.230395087973608e-06, 1.6987160537832696e-06, 1.1726461929125084e-06, 5.396621331307525e-07, 1.8626795939951717e-07, 5.143329586247463e-08, 1.1835028471012604e-08, 2.334250548252978e-09, 4.0284101816436077e-10, 6.179699796042499e-11, 8.531857249517694e-12, 1.0708461947788851e-12, 1.2320321875901963e-13, 1.1150166349595722e-14, 9.802963975649611e-16, 9.022821175010122e-17, 7.785716215374562e-18, 6.3230388613195465e-19, 4.84986386685712e-20, 3.5241318610499555e-21], [2.3827239418230913e-07, 3.2896517966231184e-07, 2.2708902095359038e-07, 1.0450837277184793e-07, 3.6071757014790776e-08, 9.960324667763756e-09, 2.291914683801513e-09, 4.5203973275739784e-10, 7.801225379641652e-11, 1.1967309363661551e-11, 1.6522384342515175e-12, 2.0737492300233675e-13, 2.385894270191371e-14, 2.5338683353507116e-15, 2.1294068828042797e-16, 1.7473161463845284e-17, 1.5077443507325807e-18, 1.2244892902455305e-19, 9.392013072138543e-21, 6.824664241219249e-22], [4.306650665195272e-08, 5.945875999108776e-08, 4.1045169605339685e-08, 1.8889349505255077e-08, 6.519784084750048e-09, 1.8002773255874937e-09, 4.142517613690661e-10, 8.170385085755274e-11, 1.4100312621556068e-11, 2.1630294608185547e-12, 2.986335776055588e-13, 3.748194805183775e-14, 4.3123808702502865e-15, 4.579836363085317e-16, 4.516459579131933e-17, 3.54249718275954e-18, 2.7251701705983817e-19, 2.2132012541601994e-20, 1.6975579350455565e-21, 1.233522871797436e-22], [7.2975459514294825e-09, 1.0075185265352973e-08, 6.955033843349861e-09, 3.2007679917303086e-09, 1.1047662708371726e-09, 3.0505391614333847e-10, 7.019425300691973e-11, 1.3844577895771766e-11, 2.3892738762608912e-12, 3.6652164551413474e-13, 5.060294935989508e-14, 6.351252040661546e-15, 7.307255685965889e-16, 7.760454447755257e-17, 7.653063570456722e-18, 7.044014872312088e-19, 5.179679957956816e-20, 3.750231701521838e-21, 2.87648290963646e-22, 2.0901834253308066e-23], [1.163818061128896e-09, 1.6067980467790855e-09, 1.1091939751427966e-09, 5.104608621928997e-10, 1.761889473370784e-10, 4.865022564964765e-11, 1.1194631726971441e-11, 2.2079435896733e-12, 3.8104317652582605e-13, 5.845314489050597e-14, 8.07019603623059e-15, 1.0129024037533794e-15, 1.1653665768213558e-16, 1.2376430527438405e-17, 1.2205162756831178e-18, 1.123384735885288e-19, 9.693592042487247e-21, 6.708701394703694e-22, 4.5874363588046247e-23, 3.333440087480017e-24], [1.7529509465862628e-10, 2.4201705156063964e-10, 1.670675764206929e-10, 7.688597397331338e-11, 2.653770312801176e-11, 7.327731193779779e-12, 1.6861433017669788e-12, 3.3256201590243433e-13, 5.73929911633504e-14, 8.8042537823623e-15, 1.2155386012075592e-15, 1.5256407223451213e-16, 1.7552833318100048e-17, 1.8641466680271313e-18, 1.8383501959982951e-19, 1.692049987813839e-20, 1.4600556490948915e-21, 1.18575971092879e-22, 7.750448409493586e-24, 5.020850897492234e-25], [2.5013435124417142e-11, 3.453421118259955e-11, 2.383942341530297e-11, 1.0971113171788113e-11, 3.786752372256975e-12, 1.045618128571851e-12, 2.4060134809450214e-13, 4.745437073308068e-14, 8.189595172964903e-15, 1.2563080058394914e-15, 1.734492114667615e-16, 2.1769870575023917e-17, 2.504671669832133e-18, 2.6600123542476107e-19, 2.6232025176239036e-20, 2.4144419260490423e-21, 2.0834015536941116e-22, 1.691999634115566e-23, 1.2977886216122447e-24, 8.036241992081465e-26]] |
| Legacy trial inputs | {"lambda_home": 2.711172655968777, "lambda_away": 1.3806264917563678, "rho": -0.1107929355926174, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6960 |
| Legacy p draw | 0.1669 |
| Legacy p away | 0.1372 |
| Legacy p over 1 5 | 0.9241 |
| Legacy p under 3 5 | 0.4098 |
| Legacy p btts yes | 0.6993 |
| Legacy p over 2 5 | 0.7818 |
| Legacy goal margin distribution | {"-1": 0.07856576811972779, "-10": 1.3203610310118683e-07, "-11": 1.6125292479824062e-08, "-12": 1.8126195391299122e-09, "-13": 1.8869012607879635e-10, "-14": 1.8286884432694117e-11, "-15": 1.6576464238448506e-12, "-16": 1.4111024988729625e-13, "-17": 1.1311363856893324e-14, "-18": 8.454013974005133e-16, "-19": 5.1320299502706285e-17, "-2": 0.038953367493453496, "-3": 0.0141478247751791, "-4": 0.004181429299269425, "-5": 0.0010353986427539329, "-6": 0.00021983065110067786, "-7": 4.07627632520176e-05, "-8": 6.699933995547329e-06, "-9": 9.880148549936687e-07, "0": 0.16688360787182352, "1": 0.210237771460428, "10": 0.00014819996287629306, "11": 3.5542172516395734e-05, "12": 7.845560944042965e-06, "13": 1.603789962512869e-06, "14": 3.052242322001962e-07, "15": 5.433155861879407e-08, "16": 9.082382687801049e-09, "17": 1.4296745361048386e-09, "18": 2.0982930584122582e-10, "19": 2.5013435124417142e-11, "2": 0.19772091838110054, "3": 0.14101920319904537, "4": 0.08184540750553551, "5": 0.03979771356387274, "6": 0.016592802733433557, "7": 0.006041935623903787, "8": 0.0019501318463166558, "9": 0.0005647261491603603} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6490 |
| Legacy raw p draw | 0.1826 |
| Legacy raw p away | 0.1684 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.7112 |
| Legacy lambda away | 1.3806 |
| Legacy model home team | Bayern Munich |
| Legacy model away team | Dortmund |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 87.7% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:37:38Z |
| Market reference home draw last update utc | 2026-10-31T11:37:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 28.4% |
| Market draw away odds | 3.64 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:37:38Z |
| Market reference draw away last update utc | 2026-10-31T11:37:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.9% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:37:38Z |
| Market reference home away last update utc | 2026-10-31T11:37:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.10 |
| Market reference dc draw away odds | 3.40 |
| Market reference dc home away odds | 1.15 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.75, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.07, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.21, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.21, "price": 1.65, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 91.4% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 6.40 |
| Market reference over 1 5 last update utc | 2026-10-31T11:37:24Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 44.9% |
| Market under 3 5 odds | 2.14 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market reference under 3 5 odds | 2.14 |
| Market reference under 3 5 opposite odds | 1.76 |
| Market reference under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.4% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:37:38Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.66 |
| Market reference btts yes last update utc | 2026-10-31T11:37:48Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 10.050716353752582, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,725.3250 |
| Elo away rating | 1,617.6097 |
| Elo rating diff | 167.7154 |
| Elo home expectancy | 0.7242 |

</details>


---

## 2026-10-31 — Borussia Monchengladbach vs SC Paderborn

The model's most likely 1X2 outcome is **Borussia Monchengladbach win** at **45.3%**. Expected goals are 1.45 for Borussia Monchengladbach and 0.99 for SC Paderborn (2.44 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 63.4%; Under 3.5 goals: 57.9%; Double Chance 1X: 71.4%; Double Chance X2: 54.7%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 76.5%; BTTS Yes (both teams score): 65.3%; BTTS No (at least one team does not score): 34.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 45.3% | 2.21 |
| Draw | 26.1% | 3.83 |
| SC Paderborn win | 28.6% | 3.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.45 |
| SC Paderborn expected goals | 0.99 |
| Expected total goals | 2.44 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 84.9% |
| Under 1.5 | 15.1% |
| Over 2.5 | 63.4% |
| Under 2.5 | 36.6% |
| Over 3.5 | 42.1% |
| Under 3.5 | 57.9% |
| Over 4.5 | 23.5% |
| Under 4.5 | 76.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.56% |
| 2 | 2-1 | 8.33% |
| 3 | 1-2 | 7.29% |
| 4 | 2-2 | 7.18% |
| 5 | 2-0 | 6.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 45.3% | 44.6% | 2.20 | -0.3% |
| Draw | 26.1% | 25.1% | 3.85 | +0.4% |
| SC Paderborn win | 28.6% | 30.3% | 3.21 | -8.1% |

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
| Market best home last update utc | 2026-10-31T11:37:47Z |
| Market best draw last update utc | 2026-10-31T11:37:47Z |
| Market best away last update utc | 2026-10-31T11:37:47Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | M'gladbach |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3298 |
| Dc lambda away | 0.8711 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:37:21.613878+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9452 |
| Shot lambda away | 1.4508 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 65.3% |
| P btts no | 34.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.72 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.61 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.73 |
| Fair Over 3.5 odds | 2.38 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.25 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.16038779304724138, "-10": 2.779663464407838e-07, "-11": 3.33508369040605e-08, "-12": 3.6789083257821948e-09, "-13": 3.754691366547743e-10, "-14": 3.5628484114731716e-11, "-15": 3.1275997804191873e-12, "-16": 2.2552279869925925e-13, "-2": 0.0826313634203918, "-3": 0.03094972082564449, "-4": 0.009273752061738208, "-5": 0.00230347931899094, "-6": 0.00048717970750819663, "-7": 8.956207568086162e-05, "-8": 1.4545434161313269e-05, "-9": 2.1141897572148635e-06, "0": 0.26087514057962063, "1": 0.18611318017865144, "10": 1.0301277413462707e-05, "11": 1.819324031578294e-06, "12": 2.9541105321536234e-07, "13": 4.4379915885589854e-08, "14": 6.1988914452842755e-09, "15": 8.009996305416902e-10, "16": 8.501901121808145e-11, "2": 0.13893387169077018, "3": 0.07659923127412638, "4": 0.033785286917336003, "5": 0.012352671830519813, "6": 0.0038456542196048647, "7": 0.0010406618829394872, "8": 0.0002487806750255473, "9": 5.322778242458422e-05} |
| Raw goal margin distribution | {"-1": 0.15519996502443392, "-10": 2.3998251306601914e-08, "-11": 2.1304093355802237e-09, "-12": 1.7364553508244055e-10, "-13": 1.307989642342565e-11, "-14": 9.123886204531587e-13, "-15": 5.47977194029883e-14, "-2": 0.06676479258639204, "-3": 0.019756563339313884, "-4": 0.00456237393298184, "-5": 0.000860811070163684, "-6": 0.00013704205772622601, "-7": 1.884993368218572e-05, "-8": 2.280935514386959e-06, "-9": 2.46273993735512e-07, "0": 0.28313877885464694, "1": 0.23277922996761044, "10": 1.1461043274206675e-06, "11": 1.4976559888889447e-07, "12": 1.796871776915515e-08, "13": 1.992334369529273e-09, "14": 2.0457013775247686e-10, "15": 1.8085449918395197e-11, "2": 0.1446626495950379, "3": 0.06301221813638139, "4": 0.02141946895985543, "5": 0.005948810315354029, "6": 0.0013940572337712179, "7": 0.0002822545914929591, "8": 5.027460320737838e-05, "9": 7.990218453264812e-06} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 70.9% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.0% |
| P home draw | 71.4% |
| P draw away | 54.7% |
| P home away | 73.9% |
| Raw p home draw | 75.3% |
| Raw p draw away | 53.0% |
| Raw p home away | 71.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.3637 |
| Totals anchor target over 2 5 | 0.6343 |
| Totals anchor reference over odds | 1.53 |
| Totals anchor reference under odds | 2.56 |
| Totals anchor reference last update utc | 2026-10-31T11:37:47Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4475 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.96, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.20 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.21 |
| Market reference 1x2 last update utc | 2026-10-31T11:37:47Z |
| Market reference home last update utc | 2026-10-31T11:37:47Z |
| Market reference draw last update utc | 2026-10-31T11:37:47Z |
| Market reference away last update utc | 2026-10-31T11:37:47Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.56 |
| Market reference over 2 5 last update utc | 2026-10-31T11:37:27Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:37:27Z |
| Home probability edge | +0.7% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.0237 |
| Raw ev home | 0.0330 |
| Raw edge prob draw | 0.0318 |
| Raw ev draw | 0.0901 |
| Raw edge prob away | -0.0555 |
| Raw ev away | -0.2062 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10978957819395281, 0.09151898756420328, 0.045717808248443126, 0.012859744447604862, 0.002712942181507611, 0.0004578663478230538, 6.439552167686355e-05, 7.762932626989421e-06, 8.188493737868874e-07, 7.677674624263617e-08, 6.4788495382378404e-09, 4.970194681137904e-10, 3.4951059501225746e-11, 2.268742383121066e-12, 1.3674937176952775e-13], [0.12883682210493613, 0.12759238311269205, 0.0641141810369969, 0.01803437249490916, 0.00380460203216342, 0.0006421070265562336, 9.03076130055488e-05, 1.088665635762972e-05, 1.1483458854305835e-06, 1.0767091417160353e-07, 9.085871526227209e-09, 6.970149571561018e-10, 4.9015004046541285e-11, 3.1816608330668443e-12, 1.9177590340030498e-13], [0.09965696660707349, 0.08409609988471607, 0.03398353380072187, 0.01264560865148887, 0.0026677672531705255, 0.0004502421236166333, 6.332323082716881e-05, 7.633667091033552e-06, 8.052141912784518e-07, 7.54982877361824e-08, 6.370966087719922e-09, 4.887432803619012e-10, 3.436906714656537e-11, 2.2309641085705015e-12, 1.344722708744409e-13], [0.04658596612157476, 0.03931183331751017, 0.016586757423369094, 0.0044685118756134104, 0.001247083060098153, 0.0002104716311505872, 2.9601281139273208e-05, 3.5684585693683723e-06, 3.764080155420531e-07, 3.529267239873077e-08, 2.9781922973276184e-09, 2.2846950570810135e-10, 1.6066274664298058e-11, 1.0428936573003991e-12, 6.286084022552701e-14], [0.016332919162872165, 0.01378262702642205, 0.005815274227930932, 0.0016357507791612278, 0.00033050636099288093, 7.379080920398405e-05, 1.0378132562572232e-05, 1.2510923396426048e-06, 1.3196767614653614e-07, 1.2373519609444003e-08, 1.0441465122092496e-09, 8.010081744733045e-11, 5.6327943195527095e-12, 3.656358173555409e-13, 2.203884790613525e-14], [0.004581023352564952, 0.0038657226940336637, 0.0016310560760184434, 0.0004587919920247846, 9.678856005056647e-05, 1.564504088304063e-05, 2.910837135178579e-06, 3.5090378927155853e-07, 3.701402059132584e-08, 3.470499163011561e-09, 2.928600520354669e-10, 2.2466511443949088e-11, 1.5798744891068518e-12, 1.0255277707168653e-13, 6.1814104334230185e-15], [0.0010707299548167553, 0.0009035415816422828, 0.0003812293595056631, 0.0001072341900671465, 2.2622545783726706e-05, 3.818032867437913e-06, 5.142935648649283e-07, 8.20173069454871e-08, 8.651346554072132e-09, 8.111653501880438e-10, 6.845065090270615e-11, 5.251133847593424e-12, 3.692666048930688e-13, 2.3969825497357102e-14, 1.4447910007655885e-15], [0.0002145115149871439, 0.0001810167658615068, 7.637601535032598e-05, 2.1483445444149988e-05, 4.532232004066562e-06, 7.649099672428439e-07, 1.0757894003485758e-07, 1.2420866637546333e-08, 1.7332226932143915e-09, 1.6250998432531342e-10, 1.3713497750708333e-11, 1.0520193929199566e-12, 7.397938060239254e-14, 4.8021478789164086e-15, 2.8945142051905957e-16], [3.7603591011153116e-05, 3.173200482979067e-05, 1.3388616664552182e-05, 3.766020187963584e-06, 7.944944058541188e-07, 1.3408772750627526e-07, 1.885844898688351e-08, 2.273401396906332e-09, 2.2967240252605275e-10, 2.8487789973252628e-11, 2.4039584111879018e-12, 1.844176383236794e-13, 1.2968489694352896e-14, 8.418103094590116e-16, 5.074045948278503e-17], [5.859431864247262e-06, 4.944515010839703e-06, 2.0862286019226462e-06, 5.868253030463861e-07, 1.2379897005706387e-07, 2.0893693448632168e-08, 2.9385437383161843e-09, 3.5424384286347217e-10, 3.736633600143829e-11, 3.3555265787983613e-12, 3.7458737679233345e-13, 2.873615410832696e-14, 2.0207639670295263e-15, 1.3117178488174195e-16, 7.906432792862693e-18], [8.217206592161814e-07, 6.93413666775945e-07, 2.9257053956164714e-07, 8.229577304351144e-08, 1.7361439409560134e-08, 2.9301099410047396e-09, 4.120983320103781e-10, 4.96787898255458e-11, 5.2402162808560485e-12, 4.913318230814504e-13, 3.9709788301593643e-14, 4.029928505750393e-15, 2.8338984693034346e-16, 1.8395395328559733e-17, 1.1087899504799844e-18], [1.0476114058130383e-07, 8.840328621578562e-08, 3.729980873816889e-08, 1.0491885475146883e-08, 2.213409355453749e-09, 3.735596227324701e-10, 5.253840317735301e-11, 6.33354732712623e-12, 6.680750061691856e-13, 6.263987842170407e-14, 5.285901881087549e-15, 3.883730539217317e-16, 3.612936252801863e-17, 2.345228362521808e-18, 1.413595953498003e-19], [1.2242994925835303e-08, 1.0331321123093858e-08, 4.359072138601048e-09, 1.2261426319139615e-09, 2.586718639874451e-10, 4.365634566627454e-11, 6.139942730125408e-12, 7.40175100789067e-13, 7.807512275278179e-14, 7.320459756513265e-15, 6.177411733923746e-16, 4.738949216514366e-17, 3.1917104578391602e-18, 2.740769982357726e-19, 1.652010276885626e-20], [1.3207268730691564e-09, 1.1145029075184499e-09, 4.702398187676002e-10, 1.3227151803904102e-10, 2.7904518799904648e-11, 4.7094774808551305e-12, 6.623532405187992e-13, 7.984722302922097e-14, 8.422441842246924e-15, 7.897028449506377e-16, 6.663952515237348e-17, 5.1121948659416955e-18, 3.594962338587545e-19, 2.2349801516120613e-20, 1.7821247010934313e-21], [1.3229812108636776e-10, 1.1164052433289451e-10, 4.7104246723152756e-11, 1.3249729120102805e-11, 2.795214879263915e-12, 4.717516049081479e-13, 6.634838057960509e-14, 7.998351359491837e-15, 8.436818038684126e-16, 7.910507822161801e-17, 6.675327160761961e-18, 5.120920829147448e-19, 3.6010985501200063e-20, 2.3375442756367815e-21, 1.3494428229928895e-22]] |
| Legacy trial inputs | {"lambda_home": 1.4023896484403373, "lambda_away": 0.8438557057058473, "rho": -0.1107929355926174, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4664 |
| Legacy p draw | 0.2762 |
| Legacy p away | 0.2575 |
| Legacy p over 1 5 | 0.6699 |
| Legacy p under 3 5 | 0.8108 |
| Legacy p btts yes | 0.4395 |
| Legacy p over 2 5 | 0.3969 |
| Legacy goal margin distribution | {"-1": 0.16960264573852246, "-10": 7.211298495045714e-09, "-11": 5.483282971091276e-10, "-12": 3.826719260516703e-11, "-13": 2.460518286521371e-12, "-14": 1.3674937176952775e-13, "-2": 0.06664115748031475, "-3": 0.017145478815949727, "-4": 0.0034220764051514623, "-5": 0.0005561967076408025, "-6": 7.61237518853136e-05, "-7": 8.98983669740473e-06, "-8": 9.331254603438065e-07, "-9": 8.636779914111736e-08, "0": 0.2761806853323555, "1": 0.23125614667530495, "10": 9.146180843034865e-07, "11": 1.155759512522854e-07, "12": 1.3404602080076907e-08, "13": 1.432367397402051e-09, "14": 1.3229812108636776e-10, "2": 0.14526627281828666, "3": 0.06211155272271196, "4": 0.0206021704684657, "5": 0.005564833752112601, "6": 0.0012657399038655266, "7": 0.0002484143019279534, "8": 4.2851431894719465e-05, "9": 6.591399858663695e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4868 |
| Legacy raw p draw | 0.3010 |
| Legacy raw p away | 0.2121 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4024 |
| Legacy lambda away | 0.8439 |
| Legacy model home team | M'gladbach |
| Legacy model away team | Paderborn |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 69.7% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:37:38Z |
| Market reference home draw last update utc | 2026-10-31T11:37:38Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.7% |
| Market draw away odds | 1.74 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:37:38Z |
| Market reference draw away last update utc | 2026-10-31T11:37:38Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.6% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:37:38Z |
| Market reference home away last update utc | 2026-10-31T11:37:38Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.39 |
| Market reference dc draw away odds | 1.74 |
| Market reference dc home away odds | 1.30 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.27, "price": 1.61, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.27, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.8, "price": 2.03, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.03, "price": 1.8, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.49, "price": 2.54, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.54, "price": 1.49, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 83.6% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-31T11:37:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 58.7% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.32 |
| Market reference under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.4% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:37:38Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.84 |
| Market reference btts yes last update utc | 2026-10-31T11:37:48Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 10.202008312298068, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,420.8760 |
| Elo away rating | 1,403.5364 |
| Elo rating diff | 77.3396 |
| Elo home expectancy | 0.6095 |

</details>


---

## 2026-10-31 — FC Schalke 04 vs RB Leipzig

The model's most likely 1X2 outcome is **RB Leipzig win** at **53.0%**. Expected goals are 0.87 for FC Schalke 04 and 1.61 for RB Leipzig (2.48 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 60.9%; Under 3.5 goals: 60.7%; Double Chance 1X: 47.0%; Double Chance X2: 78.3%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 21.7% | 4.61 |
| Draw | 25.3% | 3.95 |
| RB Leipzig win | 53.0% | 1.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| RB Leipzig expected goals | 1.61 |
| Expected total goals | 2.48 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 60.9% |
| Under 2.5 | 39.1% |
| Over 3.5 | 39.3% |
| Under 3.5 | 60.7% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.63% |
| 2 | 1-2 | 8.93% |
| 3 | 0-2 | 7.90% |
| 4 | 0-1 | 6.96% |
| 5 | 2-2 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 21.7% | 22.6% | 4.25 | -7.8% |
| Draw | 25.3% | 24.8% | 3.89 | -1.4% |
| RB Leipzig win | 53.0% | 52.6% | 1.87 | -1.0% |

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
| Market best home last update utc | 2026-10-31T11:37:47Z |
| Market best draw last update utc | 2026-10-31T11:37:47Z |
| Market best away last update utc | 2026-10-31T11:37:47Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Schalke 04 |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7533 |
| Dc lambda away | 1.5293 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:37:21.613878+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.3535 |
| Shot lambda away | 1.9242 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.50 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.98 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.68 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.2015968694204266, "-10": 1.8911287263134943e-05, "-11": 3.515613853370241e-06, "-12": 6.006664412760899e-07, "-13": 9.493028353485308e-08, "-14": 1.3954361111276483e-08, "-15": 1.9163934313251e-09, "-16": 2.451756495002756e-10, "-17": 2.6363372801655455e-11, "-2": 0.162251338657758, "-3": 0.09564603425477856, "-4": 0.04484778586144435, "-5": 0.017371854903751604, "-6": 0.005717019973287604, "-7": 0.0016329755649275332, "-8": 0.00041162925289441526, "-9": 9.279409331335568e-05, "0": 0.253455360029564, "1": 0.132419287606132, "10": 5.236186647046773e-08, "11": 5.285702474145411e-09, "12": 4.903909361688595e-10, "13": 4.208442161290539e-11, "14": 3.3591860762020377e-12, "15": 2.5050494124452543e-13, "16": 1.7402693721275826e-14, "17": 1.0161261606254217e-15, "2": 0.059432248640548274, "3": 0.01902428574882217, "4": 0.004843841444653959, "5": 0.0010188321113850304, "6": 0.00018206801607937619, "7": 2.8239119799128247e-05, "8": 3.865317915121214e-06, "9": 4.731587117285766e-07} |
| Raw goal margin distribution | {"-1": 0.24517333003553157, "-10": 3.0285376214015282e-06, "-11": 4.3816799713316046e-07, "-12": 5.820380281863853e-08, "-13": 7.144867196641451e-09, "-14": 8.123158278123417e-10, "-15": 7.963765700605563e-11, "-2": 0.16852615321673642, "-3": 0.08141553213670165, "-4": 0.030673717066699732, "-5": 0.009438360989472408, "-6": 0.002449931761908156, "-7": 0.0005493572230015691, "-8": 0.00010835707276566734, "-9": 1.9069065966556815e-05, "0": 0.2665357979236627, "1": 0.12919598581642175, "10": 6.7500682649309636e-09, "11": 5.303021228323515e-10, "12": 3.825089410684895e-11, "13": 2.549716594197297e-12, "14": 1.574092262948278e-13, "15": 8.379753861863374e-15, "2": 0.049691527393430156, "3": 0.013035563915662523, "4": 0.0026668370748782625, "5": 0.00044558871137268793, "6": 6.280570620502727e-05, "7": 7.64728847948087e-06, "8": 8.19063207529727e-07, "9": 7.827031721297209e-08} |
| Unadjusted home-win probability | 19.5% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 53.8% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.2% |
| Raw p btts yes | 47.4% |
| P home draw | 47.0% |
| P draw away | 78.3% |
| P home away | 74.7% |
| Raw p home draw | 46.2% |
| Raw p draw away | 80.5% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2938 |
| Totals anchor target over 2 5 | 0.6086 |
| Totals anchor reference over odds | 1.60 |
| Totals anchor reference under odds | 2.43 |
| Totals anchor reference last update utc | 2026-10-31T11:37:47Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4552 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.95, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 8.25, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.46, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.99, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.25, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.1, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.37, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 5.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 7.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:15Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.19, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.25 |
| Reference draw odds | 3.89 |
| Reference away odds | 1.87 |
| Market reference 1x2 last update utc | 2026-10-31T11:37:47Z |
| Market reference home last update utc | 2026-10-31T11:37:47Z |
| Market reference draw last update utc | 2026-10-31T11:37:47Z |
| Market reference away last update utc | 2026-10-31T11:37:47Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-31T11:37:27Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:37:27Z |
| Home probability edge | -0.9% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.0312 |
| Raw ev home | -0.1708 |
| Raw edge prob draw | 0.0187 |
| Raw ev draw | 0.0368 |
| Raw edge prob away | 0.0125 |
| Raw ev away | 0.0067 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0671729028036173, 0.08996303692660272, 0.10200636164381627, 0.06951948007962545, 0.03553424045808826, 0.014530399174297626, 0.004951386264877263, 0.001446203073979131, 0.00036960667515882324, 8.3964906622593e-05, 1.7167154751737415e-05, 3.190848243245833e-06, 5.436575408355536e-07, 8.55032409544744e-08, 1.2486912077602152e-08, 1.7020186220660485e-09, 2.1749277652597276e-10, 2.615751173837473e-11], [0.04711194638514852, 0.11281080912642215, 0.09060875558358912, 0.06175177192210768, 0.03156384814270636, 0.01290685567154263, 0.004398146749324836, 0.0012846126333960278, 0.0003283089441859238, 7.458314931700749e-05, 1.5248995296952854e-05, 2.834321153283807e-06, 4.829123639440188e-07, 7.594959898972488e-08, 1.1091696107973168e-08, 1.5118448186986052e-09, 1.9319138053614404e-10, 2.3234821334507792e-11], [0.02705182922131536, 0.055309171085880064, 0.04611062776902287, 0.02742599147140049, 0.014018542351438618, 0.005732358806105707, 0.001953361522793266, 0.0005705386911328367, 0.00014581279245857662, 3.312482789414699e-05, 6.772579991537522e-06, 1.258815178214217e-06, 2.1447725243687965e-07, 3.373171310413445e-08, 4.926186786094983e-09, 6.714599729382749e-10, 8.580264160866086e-11, 1.03193478004732e-11], [0.008009737636305378, 0.016376413796459932, 0.016741305459075487, 0.00930469081631217, 0.004150730265219347, 0.0016972859653384621, 0.0005783680348721072, 0.00016892998953779763, 4.3173502318652346e-05, 9.807883175265238e-06, 2.0052835765488094e-06, 3.7272079561075304e-07, 6.350426460704655e-08, 9.987574953872334e-09, 1.4585876386120648e-09, 1.988116283197053e-10, 2.5405182110413154e-11, 3.0554410122642466e-12], [0.0017786938679149168, 0.003636651800699501, 0.003717681990727916, 0.0025336784385982386, 0.0010561494692010302, 0.0003769102404755062, 0.0001284361265919742, 3.7513680240394305e-05, 9.587385669478575e-06, 2.1780016341605233e-06, 4.453061714369832e-07, 8.276877766785562e-08, 1.4102165535487143e-08, 2.217905146514593e-09, 3.2390335444401375e-10, 4.414938918343332e-11, 5.641638176540491e-12, 6.785108875047998e-13], [0.0003159905624292041, 0.0006460626353928502, 0.0006604579036189893, 0.0004501159470268678, 0.0002300726109768543, 7.672356910305792e-05, 2.281708202300259e-05, 6.66442333432419e-06, 1.7032292316134203e-06, 3.869288435546743e-07, 7.911004254516204e-08, 1.4704133790882628e-08, 2.5052940809044717e-09, 3.940178280837796e-10, 5.754245010326064e-11, 7.843277907812659e-12, 1.0022547739015282e-12, 1.2053959415079968e-13], [4.678059808636175e-05, 9.564588338520373e-05, 9.77770206320108e-05, 6.66370952608549e-05, 3.406093606735313e-05, 1.3927946423749133e-05, 3.870523583000889e-06, 9.866298128768959e-07, 2.5215336027923807e-07, 5.7282605465178524e-08, 1.1711789986542245e-08, 2.1768630296782486e-09, 3.708944804742102e-10, 5.833208913819426e-11, 8.518831102078434e-12, 1.1611524998226144e-12, 1.4837809521140149e-13, 1.7845198489828596e-14], [5.936228891939096e-06, 1.2136994385965561e-05, 1.2407425270021999e-05, 8.455921179804424e-06, 4.322166048331452e-06, 1.7673882196504768e-06, 6.022561149567495e-07, 1.4345545228847005e-07, 3.199702705223694e-08, 7.268882217798664e-09, 1.4861688165270336e-09, 2.762332620612097e-10, 4.706469393117116e-11, 7.40205655836338e-12, 1.0809979645910146e-12, 1.4734456803372573e-13, 1.882845392653495e-14, 2.2644683306986576e-15], [6.591185884024667e-07, 1.3476095266456511e-06, 1.3776363375729982e-06, 9.388881279903983e-07, 4.799039990667737e-07, 1.9623879902559575e-07, 6.687043366641112e-08, 1.9531545622421485e-08, 4.0708069397331924e-09, 8.070873737980522e-10, 1.6501410412378566e-10, 3.067106762120136e-11, 5.225744355921299e-12, 8.218741492008069e-13, 1.2002668115690297e-13, 1.6360141338727364e-14, 2.090583803247647e-15, 2.514312026679012e-16], [6.505249510885653e-08, 1.3300392931299802e-07, 1.359674612257e-07, 9.266468345536085e-08, 4.736469749347939e-08, 1.9368022292803956e-08, 6.599857196494515e-09, 1.9276891873896768e-09, 4.926602661204089e-10, 9.127228190056239e-11, 1.6286263792715603e-11, 3.027117595404995e-12, 5.157610711262908e-13, 8.111584927465994e-14, 1.1846176433616255e-14, 1.6146836595782777e-15, 2.0633266157012131e-16, 2.481530238953029e-17], [5.778390224330007e-09, 1.181428327466372e-08, 1.2077523659297572e-08, 8.231086296122605e-09, 4.20724377315095e-09, 1.7203950516281932e-09, 5.862426989523092e-10, 1.7123002487944018e-10, 4.376132323444759e-11, 9.941420612824622e-12, 1.6576098913558772e-12, 2.688884829385147e-13, 4.581328858330578e-14, 7.205242930383894e-15, 1.0522552591588042e-15, 1.4342681642386778e-16, 1.8327823284590047e-17, 2.2042582763583006e-18], [4.666132752236119e-10, 9.54020271943396e-10, 9.752773095051621e-10, 6.646719910175816e-10, 3.3974095214065176e-10, 1.3892436103375212e-10, 4.733993642075017e-11, 1.3827069412723878e-11, 3.5337894413166494e-12, 8.027839333165635e-13, 1.6413423857420944e-13, 2.4879427376423582e-14, 3.699488578083949e-15, 5.818336720099285e-16, 8.497111717723947e-17, 1.1581920564078287e-17, 1.4799979438103324e-18, 1.7799700848164105e-19], [3.453971524052596e-11, 7.061862633638718e-11, 7.219211784043561e-11, 4.920044610196505e-11, 2.514835382010896e-11, 1.0283479114001443e-11, 3.504203609924585e-12, 1.0235093287853854e-12, 2.615786723268049e-13, 5.94237882390629e-14, 1.2149568309767782e-14, 2.258232610939461e-15, 3.137771467026544e-16, 4.306857609000059e-17, 6.2897443060632045e-18, 8.573185964971726e-19, 1.0955262151784164e-19, 1.3175720265727801e-20], [2.3600342670357306e-12, 4.825238913646811e-12, 4.932752650878981e-12, 3.3617746395848372e-12, 1.718340072050122e-12, 7.026509316705091e-13, 2.3943569136287987e-13, 6.993448184917541e-14, 1.787318239070607e-14, 4.0603165238813285e-15, 8.30157322985119e-16, 1.5430081885856162e-16, 2.628981303235703e-17, 3.371925929635243e-18, 4.2976648735613597e-19, 5.857897934046477e-20, 7.48552612623581e-21, 9.002723706161402e-22], [1.4973839770154703e-13, 3.061495985666924e-13, 3.1297108203789256e-13, 2.132963724282687e-13, 1.0902447167359314e-13, 4.458148176975106e-14, 1.5191608561799313e-14, 4.437171698077258e-15, 1.1340096753651557e-15, 2.576171451996551e-16, 5.267145020742845e-17, 9.790009281915172e-18, 1.6680242885976672e-18, 2.6233698965471066e-19, 3.1243909831961304e-20, 3.716692858214512e-21, 4.749383107489635e-22, 5.712007836240167e-23], [8.867165838272466e-15, 1.812947983604179e-14, 1.8533432503698402e-14, 1.2630923904990099e-14, 6.456180148839679e-15, 2.640013505127944e-15, 8.996123541810987e-16, 2.627591713527037e-16, 6.715346235846939e-17, 1.5255498818818053e-17, 3.1190829546772517e-18, 5.797419846444081e-19, 9.877658781111128e-20, 1.5534997225080194e-20, 2.268734404800576e-21, 2.521890808647262e-22, 2.8124761777897216e-23, 3.382520551235346e-24], [4.9227497261679855e-16, 1.0064872308267345e-15, 1.0289133128506932e-15, 7.01226054960675e-16, 3.5842522446815586e-16, 1.4656459568348757e-16, 4.994342669320292e-17, 1.4587497994473655e-17, 3.728132466064175e-18, 8.469335524181837e-19, 1.7316090666489769e-19, 3.218530867933284e-20, 5.483741135191057e-21, 8.62450355960446e-22, 1.2595243929886617e-22, 1.7167847090541842e-23, 1.7890798922802248e-24, 1.8778606852576305e-25], [2.5721822901654102e-17, 5.258988927770261e-17, 5.3761672817970576e-17, 3.663971033068227e-17, 1.8728049687856335e-17, 7.658135764618309e-18, 2.6095902655289127e-18, 7.622102704054503e-19, 1.9479837160167125e-19, 4.4253061919780223e-20, 9.047817627307024e-21, 1.6817121648174961e-21, 2.865305493149636e-22, 4.506382926509582e-23, 6.581131517727336e-24, 8.970358986934325e-25, 1.1462790460745902e-25, 1.1242821435612765e-26]] |
| Legacy trial inputs | {"lambda_home": 0.8882657328762978, "lambda_away": 2.044563073106327, "rho": -0.1107929355926174, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1850 |
| Legacy p draw | 0.2365 |
| Legacy p away | 0.5785 |
| Legacy p over 1 5 | 0.7958 |
| Legacy p under 3 5 | 0.6696 |
| Legacy p btts yes | 0.5301 |
| Legacy p over 2 5 | 0.5539 |
| Legacy goal margin distribution | {"-1": 0.21254926101979638, "-10": 2.0226272629686888e-05, "-11": 3.7089960774217547e-06, "-12": 6.24737900417464e-07, "-13": 9.729248072838376e-08, "-14": 1.4087614978921683e-08, "-15": 1.9055293504026657e-09, "-16": 2.4072759786048056e-10, "-17": 2.615751173837473e-11, "-2": 0.17960932202295743, "-3": 0.10743333077275004, "-4": 0.05057337394980617, "-5": 0.019544517453512242, "-6": 0.006392079962630557, "-7": 0.001809727463137155, "-8": 0.0004513496301146336, "-9": 0.0001005384979901961, "0": 0.2365359216964759, "1": 0.1219407242165316, "10": 6.808076103944239e-09, "11": 5.42384555937641e-10, "12": 3.969092224347588e-11, "13": 2.68543725221077e-12, "14": 1.6893343056077019e-13, "15": 9.92741474191717e-15, "16": 5.448648618945012e-16, "17": 2.5721822901654102e-17, "2": 0.04763193812251635, "3": 0.012378009615413355, "4": 0.0025314893174764016, "5": 0.0004250318926865451, "6": 6.039224323677738e-05, "7": 7.428387234478697e-06, "8": 8.048905798286717e-07, "9": 7.789301997507586e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1436 |
| Legacy raw p draw | 0.2252 |
| Legacy raw p away | 0.6311 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.8883 |
| Legacy lambda away | 2.0446 |
| Legacy model home team | Schalke 04 |
| Legacy model away team | RB Leipzig |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 48.3% |
| Market home draw odds | 2.01 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:37:38Z |
| Market reference home draw last update utc | 2026-10-31T11:37:38Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 77.0% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:37:38Z |
| Market reference draw away last update utc | 2026-10-31T11:37:38Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.7% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:37:38Z |
| Market reference home away last update utc | 2026-10-31T11:37:38Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.01 |
| Market reference dc draw away odds | 1.26 |
| Market reference dc home away odds | 1.30 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.53, "price": 1.5, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.5, "price": 2.53, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.99, "price": 1.84, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.84, "price": 1.99, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.6, "price": 2.28, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.28, "price": 1.6, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 83.6% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-31T11:37:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.2% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market reference under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.1% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:37:38Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.60 |
| Market reference btts yes last update utc | 2026-10-31T11:37:48Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 10.281865210655456, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,439.0939 |
| Elo away rating | 1,517.4050 |
| Elo rating diff | -18.3111 |
| Elo home expectancy | 0.4737 |

</details>


---

## 2026-10-31 — Werder Bremen vs TSG Hoffenheim

The model's most likely 1X2 outcome is **Werder Bremen win** at **39.5%**. Expected goals are 1.77 for Werder Bremen and 1.64 for TSG Hoffenheim (3.41 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 69.2%; Under 3.5 goals: 51.8%; Double Chance 1X: 63.9%; Double Chance X2: 60.5%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 71.0%; BTTS Yes (both teams score): 70.4%; BTTS No (at least one team does not score): 29.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 39.5% | 2.53 |
| Draw | 24.4% | 4.10 |
| TSG Hoffenheim win | 36.1% | 2.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.77 |
| TSG Hoffenheim expected goals | 1.64 |
| Expected total goals | 3.41 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 88.0% |
| Under 1.5 | 12.0% |
| Over 2.5 | 69.2% |
| Under 2.5 | 30.8% |
| Over 3.5 | 48.2% |
| Under 3.5 | 51.8% |
| Over 4.5 | 29.0% |
| Under 4.5 | 71.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.00% |
| 2 | 2-1 | 7.94% |
| 3 | 1-2 | 7.76% |
| 4 | 2-2 | 7.51% |
| 5 | 3-1 | 4.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 39.5% | 39.0% | 2.51 | -0.9% |
| Draw | 24.4% | 24.6% | 3.94 | -3.9% |
| TSG Hoffenheim win | 36.1% | 36.5% | 2.68 | -3.1% |

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
| Market best home last update utc | 2026-10-31T11:37:47Z |
| Market best draw last update utc | 2026-10-31T11:37:47Z |
| Market best away last update utc | 2026-10-31T11:37:47Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7792 |
| Dc lambda away | 1.6692 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:37:21.613878+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.7215 |
| Shot lambda away | 1.5412 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 70.4% |
| P btts no | 29.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.96 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.30 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.25 |
| Fair Over 3.5 odds | 2.07 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.45 |
| Fair Under 4.5 odds | 1.41 |
| Goal margin distribution | {"-1": 0.1741662234969847, "-10": 2.4719169859383453e-06, "-11": 3.798380201841956e-07, "-12": 5.369236988572123e-08, "-13": 7.025192597306524e-09, "-14": 8.545826855203713e-10, "-15": 9.580738749564401e-11, "-16": 8.626551908588713e-12, "-2": 0.10899377107728525, "-3": 0.050948386287357636, "-4": 0.019228804572530064, "-5": 0.006050229909707819, "-6": 0.001626929468745743, "-7": 0.00038122663256457366, "-8": 7.90557006912551e-05, "-9": 1.4691225623674365e-05, "0": 0.24387482485741138, "1": 0.17858798196234865, "10": 4.86566280300821e-06, "11": 8.040872743656169e-07, "12": 1.2224017342611872e-07, "13": 1.7201101071434866e-08, "14": 2.250343062038672e-09, "15": 2.713252850336646e-10, "16": 2.627393606055748e-11, "2": 0.11987725125462449, "3": 0.06026458341233633, "4": 0.024461362303919855, "5": 0.008277455629512244, "6": 0.0023938136415190448, "7": 0.0006032557546881789, "8": 0.00013453895855527622, "9": 2.6888682714437586e-05} |
| Raw goal margin distribution | {"-1": 0.17486865821033165, "-10": 1.698989274958561e-06, "-11": 2.4848900147807974e-07, "-12": 3.342184013730999e-08, "-13": 4.159860957991358e-09, "-14": 4.813873341420604e-10, "-15": 5.145426698376879e-11, "-16": 4.473362339504684e-12, "-2": 0.10685345803620401, "-3": 0.048235610760005605, "-4": 0.017490830199317617, "-5": 0.00527070303804115, "-6": 0.0013545754466375184, "-7": 0.0003029297629713722, "-8": 5.989382429169806e-05, "-9": 1.0604248045908468e-05, "0": 0.23965043654984167, "1": 0.18859586168256615, "10": 3.5168749328143123e-06, "11": 5.531846064910602e-07, "12": 8.001840710369812e-08, "13": 1.0711122534145751e-08, "14": 1.3330531359706703e-09, "15": 1.532395351580232e-10, "16": 1.432782063642191e-11, "2": 0.12358957503690073, "3": 0.060000886632131475, "4": 0.02339898065789033, "5": 0.0075831857003611745, "6": 0.0020959599090549664, "7": 0.0005041019133503631, "8": 0.00010719019812927427, "9": 2.0410306945346655e-05} |
| Unadjusted home-win probability | 40.6% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 55.6% |
| Raw p btts yes | 67.6% |
| P home draw | 63.9% |
| P draw away | 60.5% |
| P home away | 75.6% |
| Raw p home draw | 64.6% |
| Raw p draw away | 59.4% |
| Raw p home away | 76.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0530 |
| Totals anchor target over 2 5 | 0.6919 |
| Totals anchor reference over odds | 1.41 |
| Totals anchor reference under odds | 3.00 |
| Totals anchor reference last update utc | 2026-10-31T11:37:47Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6609 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.25, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.2, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.55, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.32, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.01, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:16Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.16, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.16, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.51 |
| Reference draw odds | 3.94 |
| Reference away odds | 2.68 |
| Market reference 1x2 last update utc | 2026-10-31T11:37:47Z |
| Market reference home last update utc | 2026-10-31T11:37:47Z |
| Market reference draw last update utc | 2026-10-31T11:37:47Z |
| Market reference away last update utc | 2026-10-31T11:37:47Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-31T11:37:27Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:37:27Z |
| Home probability edge | +0.5% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.0161 |
| Raw ev home | 0.0188 |
| Raw edge prob draw | -0.0060 |
| Raw ev draw | -0.0558 |
| Raw edge prob away | -0.0101 |
| Raw ev away | -0.0501 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.04278163754682302, 0.04328238376871386, 0.043537839380431785, 0.023270237447849014, 0.009328160720396047, 0.002991446309752476, 0.0007994386828910824, 0.00018312275588254376, 3.6703503826775856e-05, 6.5391336315829115e-06, 1.0485168382876269e-06, 1.528403138442494e-07, 2.0422639509518225e-08, 2.5189741796733286e-09, 2.885033609523208e-10, 3.084003161112495e-11, 3.0906514397993464e-12], [0.04652322983866414, 0.10532143658940661, 0.07976400485699159, 0.04263250908238266, 0.01708976530752889, 0.005480513993713934, 0.0014646209341672397, 0.00033549217410650575, 6.724308094221562e-05, 1.1980095801091254e-05, 1.9209474648253035e-06, 2.8001287407239085e-07, 3.7415534170075394e-08, 4.614915934308063e-09, 5.285559368984719e-10, 5.650083849418502e-11, 5.66226390568714e-12], [0.051823135687204556, 0.08309576381564954, 0.06963361612828994, 0.03905269197902931, 0.015654751618281407, 0.005020319692413193, 0.0013416379058887589, 0.0003073211691912925, 6.159673414207875e-05, 1.0974136903253815e-05, 1.7596470690185132e-06, 2.565004208450554e-07, 3.4273782205763086e-08, 4.227405197835813e-09, 4.841735248914336e-10, 5.175650905290257e-11, 5.1868082121432775e-12], [0.03164772609667431, 0.05074552008787319, 0.04068393098958451, 0.022728549190574827, 0.009560156574029258, 0.0030658450214632958, 0.0008193211082934668, 0.00018767710709325413, 3.7616337659388155e-05, 6.70176503710358e-06, 1.074593957479566e-06, 1.5664152612421522e-07, 2.0930560398584217e-08, 2.5816222817601157e-09, 2.956785786084486e-10, 3.16070380633245e-11, 3.167517430914958e-12], [0.014495146141900908, 0.023242230025423107, 0.01863386720169476, 0.00995948628883987, 0.004172986763865765, 0.001404204254636789, 0.00037526169070030034, 8.595900654902908e-05, 1.722886219472242e-05, 3.069511639627929e-06, 4.921805885607306e-07, 7.174423230677187e-08, 9.586519135137602e-09, 1.1824227795384304e-09, 1.354253444581404e-10, 1.4476510395755024e-11, 1.4507717846103214e-12], [0.005311200205240505, 0.008516239551696277, 0.006827678613048237, 0.0036492785311400358, 0.0014628581564006195, 0.0004903455898855558, 0.00013750050873270864, 3.149643948092001e-05, 6.31286746120863e-06, 1.1247068977975827e-06, 1.8034103398396874e-07, 2.6287970995412e-08, 3.5126187690445517e-09, 4.332542802870963e-10, 4.962151538449514e-11, 5.304371838159147e-12, 5.315806632611836e-13], [0.0016217410150033966, 0.002600379281683393, 0.0020847879982224156, 0.0011142838606011758, 0.0004466743823790222, 0.000143243933384111, 4.001244111594928e-05, 9.617236360696987e-06, 1.9275937054718515e-06, 3.4342205820369357e-07, 5.506598135979698e-08, 8.026863819295402e-09, 1.0725556762498918e-09, 1.3229142361722456e-10, 1.5151612369320166e-11, 1.6196560167857794e-12, 1.6231475581409256e-13], [0.00042444706896126183, 0.0006805792997076021, 0.0005456371560346009, 0.000291633814676641, 0.00011690499939687396, 3.749024481029162e-05, 1.001895030998691e-05, 2.3988011210838283e-06, 5.044957800700325e-07, 8.988148210637459e-08, 1.4412038772782933e-08, 2.1008155985029437e-09, 2.8071258534524833e-10, 3.462372011533914e-11, 3.9655268015662e-12, 4.239013767859576e-13, 4.248151937768572e-14], [9.720164847390896e-05, 0.00015585790240157165, 0.00012495511198834367, 6.678639013028776e-05, 2.6772145426817846e-05, 8.585554863575569e-06, 2.2944168008798067e-06, 5.255686730104896e-07, 1.1010563458643712e-07, 2.058355179457049e-08, 3.3004679005387304e-09, 4.811029554613909e-10, 6.428534448289781e-11, 7.929098626470584e-12, 9.081361855625912e-13, 9.707668076208406e-14, 9.728595189248976e-15], [1.9786601140302633e-05, 3.17268091416361e-05, 2.5436162865271367e-05, 1.3595198063573591e-05, 5.4498022569320205e-06, 1.7476961792407706e-06, 4.6705699750353415e-07, 1.0698602202706546e-07, 2.1443331004698156e-08, 3.993188397280108e-09, 6.718511769053091e-10, 9.793447371101462e-11, 1.3086079201542377e-11, 1.6140663701419381e-12, 1.848623841973843e-13, 1.9761162412584355e-14, 1.9803762146771267e-15], [3.625027268045377e-06, 5.812546957963449e-06, 4.660061792686524e-06, 2.490724068549056e-06, 9.984373590365731e-07, 3.2018871058668407e-07, 8.556772028082723e-08, 1.960049855949559e-08, 3.92855038915313e-09, 6.999145393399351e-10, 1.1730460884415653e-10, 1.794219912590158e-11, 2.397450355471563e-12, 2.957069060376307e-13, 3.386792803875912e-14, 3.620366736355813e-15, 3.6281712701887854e-16], [6.037521231892664e-07, 9.68085839779072e-07, 7.76138217311873e-07, 4.1483272634137784e-07, 1.662907975075318e-07, 5.3327768191432045e-08, 1.4251394258854995e-08, 3.264483753040692e-09, 6.543042198372591e-10, 1.1657150634493752e-10, 1.8691648489470108e-11, 2.8479016059946903e-12, 3.9929789083691355e-13, 4.9250297766232855e-14, 5.6407392136522126e-15, 6.029759067101327e-16, 6.042757600694982e-17], [9.217592476605603e-08, 1.477994099021768e-07, 1.1849442044044463e-07, 6.333325996727618e-08, 2.5387915754851313e-08, 8.141646480329107e-09, 2.175786046227812e-09, 4.9839461802764e-10, 9.989380446936441e-11, 1.7797181965931366e-11, 2.8536876621117146e-12, 4.1597664621478476e-13, 5.809754266397931e-14, 7.519131721849066e-15, 8.611818218311351e-16, 9.205741839724223e-17, 9.22558693522912e-18], [1.2990151900693382e-08, 2.082904826108284e-08, 1.6699160055216917e-08, 8.92541810054055e-09, 3.577863557480382e-09, 1.1473844690969405e-09, 3.066287787797335e-10, 7.023766575815517e-11, 1.407781584278788e-11, 2.5081180116010595e-12, 4.021639739666251e-13, 5.862268087014552e-14, 7.833207406996945e-15, 1.009872007142565e-15, 1.2136447459675393e-16, 1.2973451056779985e-17, 1.3001418316750163e-18], [1.6999113448454335e-09, 2.7257214320532934e-09, 2.1852778816033475e-09, 1.167994000577299e-09, 4.682047521973395e-10, 1.5014850409972757e-10, 4.012591566969646e-11, 9.191409443901611e-12, 1.842244728525655e-12, 3.2821619752608385e-13, 5.2627798894137515e-14, 7.67145457868699e-15, 1.0250656219786488e-15, 1.264338937692932e-16, 1.5135805485253927e-17, 1.6977258466115476e-18, 1.7013856854549266e-19], [2.0762282296082908e-10, 3.329126427938484e-10, 2.6690425009993793e-10, 1.426557992782975e-10, 5.718533067601004e-11, 1.8338754182128013e-11, 4.900876690124128e-12, 1.1226152360935005e-12, 2.2500705832749242e-13, 4.0087486725980273e-14, 6.4278247249471435e-15, 9.369718371916593e-16, 1.2519889275440813e-16, 1.544231234288109e-17, 1.768640205900985e-18, 1.976142665788127e-19, 2.0780289515122703e-20], [2.3773612928919847e-11, 3.811977987804307e-11, 3.056156467035739e-11, 1.6334638484073457e-11, 6.547940622887292e-12, 2.0998579891516785e-12, 5.611692577041898e-13, 1.2854376850482393e-13, 2.5764174837184942e-14, 4.590171634919292e-15, 7.360106890303882e-16, 1.0728688428870819e-16, 1.4335755448398808e-17, 1.7682042423457395e-18, 2.025161158392874e-19, 2.164828650047526e-20, 2.267637366198443e-21]] |
| Legacy trial inputs | {"lambda_home": 1.8320616271289232, "lambda_away": 1.6034491682865568, "rho": -0.1107929355926174, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4073 |
| Legacy p draw | 0.2452 |
| Legacy p away | 0.3475 |
| Legacy p over 1 5 | 0.8674 |
| Legacy p under 3 5 | 0.5510 |
| Legacy p btts yes | 0.6818 |
| Legacy p over 2 5 | 0.6667 |
| Legacy goal margin distribution | {"-1": 0.17321108494802637, "-10": 1.365526008878593e-06, "-11": 1.947939398818281e-07, "-12": 2.5554786778565657e-08, "-13": 3.102454143055618e-09, "-14": 3.501910076586491e-10, "-15": 3.650229551681209e-11, "-16": 3.0906514397993464e-12, "-2": 0.1052997241087779, "-3": 0.04629227375868226, "-4": 0.016356400528915366, "-5": 0.004804262919138054, "-6": 0.001203748932843983, "-7": 0.00026248996089257604, "-8": 5.06099235816676e-05, "-9": 8.738745784084313e-06, "0": 0.24517109727011738, "1": 0.1818790797038669, "10": 4.721020051041071e-06, "11": 7.694779723359025e-07, "12": 1.153394546486434e-07, "13": 1.5999112221330688e-08, "14": 2.0633855523096393e-09, "15": 2.4574260283887215e-10, "16": 2.3773612928919847e-11, "2": 0.12533837158596003, "3": 0.06295789648001471, "4": 0.02541641628276184, "5": 0.008529787788257748, "6": 0.0024419246377969236, "7": 0.0006084066067904273, "8": 0.000134029928709092, "9": 2.644235261702727e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4249 |
| Legacy raw p draw | 0.2447 |
| Legacy raw p away | 0.3305 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8321 |
| Legacy lambda away | 1.6034 |
| Legacy model home team | Werder Bremen |
| Legacy model away team | Hoffenheim |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 63.8% |
| Market home draw odds | 1.52 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:37:38Z |
| Market reference home draw last update utc | 2026-10-31T11:37:38Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.0% |
| Market draw away odds | 1.59 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:37:38Z |
| Market reference draw away last update utc | 2026-10-31T11:37:38Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:37:38Z |
| Market reference home away last update utc | 2026-10-31T11:37:38Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.52 |
| Market reference dc draw away odds | 1.59 |
| Market reference dc home away odds | 1.29 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.14, "price": 1.7, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.7, "price": 2.14, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.72, "price": 2.11, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.11, "price": 1.72, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 87.6% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.80 |
| Market reference over 1 5 last update utc | 2026-10-31T11:37:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.88 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market reference under 3 5 odds | 1.88 |
| Market reference under 3 5 opposite odds | 1.99 |
| Market reference under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.6% |
| Market btts yes odds | 1.37 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:37:38Z |
| Market reference btts yes odds | 1.41 |
| Market reference btts yes opposite odds | 3.35 |
| Market reference btts yes last update utc | 2026-10-31T11:37:48Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 9.899993199435306, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,429.0507 |
| Elo away rating | 1,502.5249 |
| Elo rating diff | -13.4741 |
| Elo home expectancy | 0.4806 |

</details>


---

## 2026-11-01 — Eintracht Frankfurt vs Hamburger SV

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **60.5%**. Expected goals are 2.01 for Eintracht Frankfurt and 1.15 for Hamburger SV (3.16 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 68.5%; Under 3.5 goals: 53.0%; Double Chance 1X: 81.4%; Double Chance X2: 39.5%; Double Chance 12 (either team wins): 79.0%; Under 4.5 goals: 72.0%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 60.5% | 1.65 |
| Draw | 21.0% | 4.77 |
| Hamburger SV win | 18.6% | 5.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 2.01 |
| Hamburger SV expected goals | 1.15 |
| Expected total goals | 3.16 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.5% |
| Under 2.5 | 31.5% |
| Over 3.5 | 47.0% |
| Under 3.5 | 53.0% |
| Over 4.5 | 28.0% |
| Under 4.5 | 72.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.83% |
| 2 | 1-1 | 9.04% |
| 3 | 2-0 | 7.67% |
| 4 | 3-1 | 7.34% |
| 5 | 1-0 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 60.5% | 62.1% | 1.58 | -4.5% |
| Draw | 21.0% | 20.2% | 4.66 | -2.3% |
| Hamburger SV win | 18.6% | 17.7% | 5.27 | -2.0% |

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
| Market best home last update utc | 2026-10-31T11:37:47Z |
| Market best draw last update utc | 2026-10-31T11:37:47Z |
| Market best away last update utc | 2026-10-31T11:37:47Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0337 |
| Dc lambda away | 1.1005 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:37:21.613878+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9213 |
| Shot lambda away | 1.3486 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.17 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.92 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.17 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.89 |
| Fair Over 4.5 odds | 3.57 |
| Fair Under 4.5 odds | 1.39 |
| Goal margin distribution | {"-1": 0.10833043243274872, "-10": 1.1441800199258353e-07, "-11": 1.3051113884182337e-08, "-12": 1.3689669436302479e-09, "-13": 1.3288265079101674e-10, "-14": 1.2001204665507945e-11, "-15": 1.0126499693953842e-12, "-16": 7.936262881733414e-14, "-17": 5.11806050286424e-15, "-2": 0.0523520578263937, "-3": 0.018459962368366886, "-4": 0.005225737910123902, "-5": 0.0012289386652231916, "-6": 0.00024642930089508814, "-7": 4.299250904690681e-05, "-8": 6.630529107144228e-06, "-9": 9.156457554660225e-07, "0": 0.20955046611384032, "1": 0.2203375591839422, "10": 3.480512173678804e-05, "11": 6.942376856269697e-06, "12": 1.2734015531427437e-06, "13": 2.1614863887903837e-07, "14": 3.413664788215669e-08, "15": 5.03694481129853e-09, "16": 6.902965322971452e-10, "17": 7.784610191739934e-11, "2": 0.18213276848387772, "3": 0.11230444638238316, "4": 0.05559369916200255, "5": 0.02286230239056325, "6": 0.008016668208926199, "7": 0.002445716784845728, "8": 0.0006595889432108932, "9": 0.0001592811841629088} |
| Raw goal margin distribution | {"-1": 0.12434220411050233, "-10": 5.825132935301043e-08, "-11": 5.9872163476159096e-09, "-12": 5.65559830824585e-10, "-13": 4.9414836924957426e-11, "-14": 4.015679088036602e-12, "-15": 3.0487931558435796e-13, "-16": 2.1567578310509218e-14, "-17": 1.2843878485525277e-15, "-2": 0.05693985610810231, "-3": 0.018593926726096454, "-4": 0.004826264561310273, "-5": 0.0010344216464142047, "-6": 0.00018831511401576025, "-7": 2.9749576150857847e-05, "-8": 4.147039457829018e-06, "-9": 5.169439486841571e-07, "0": 0.22830383789307507, "1": 0.2228162751899984, "10": 1.557485180323003e-05, "11": 2.799334792641209e-06, "12": 4.6240258625734515e-07, "13": 7.064978967048184e-08, "14": 1.0039782720839478e-08, "15": 1.3329230679148717e-09, "16": 1.6488848018504368e-10, "17": 1.717105296165027e-11, "2": 0.17411652130133337, "3": 0.09942750461346994, "4": 0.0451292751191155, "5": 0.0169144017270542, "6": 0.00538463198763434, "7": 0.0014875221458435705, "8": 0.0003626040356100242, "9": 7.904050926607744e-05} |
| Unadjusted home-win probability | 56.6% |
| Unadjusted draw probability | 22.8% |
| Unadjusted away-win probability | 20.6% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 59.9% |
| P home draw | 81.4% |
| P draw away | 39.5% |
| P home away | 79.0% |
| Raw p home draw | 79.4% |
| Raw p draw away | 43.4% |
| Raw p home away | 77.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1142 |
| Totals anchor target over 2 5 | 0.6846 |
| Totals anchor reference over odds | 1.42 |
| Totals anchor reference under odds | 2.91 |
| Totals anchor reference last update utc | 2026-10-31T11:37:47Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6202 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 9.1, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 7.39, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.31, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.19, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.58 |
| Reference draw odds | 4.66 |
| Reference away odds | 5.27 |
| Market reference 1x2 last update utc | 2026-10-31T11:37:47Z |
| Market reference home last update utc | 2026-10-31T11:37:47Z |
| Market reference draw last update utc | 2026-10-31T11:37:47Z |
| Market reference away last update utc | 2026-10-31T11:37:47Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.91 |
| Market reference over 2 5 last update utc | 2026-10-31T11:37:27Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:37:27Z |
| Home probability edge | -1.7% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0555 |
| Raw ev home | -0.1061 |
| Raw edge prob draw | 0.0268 |
| Raw ev draw | 0.0639 |
| Raw edge prob away | 0.0287 |
| Raw ev away | 0.0854 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05687593212299579, 0.03998770098776905, 0.02620106221573308, 0.008956788160322615, 0.0022963969978111107, 0.0004710116240030337, 8.050725773078484e-05, 1.1794829105878345e-05, 1.5120157842082127e-06, 1.7229333379322487e-07, 1.7669454156271014e-08, 1.6473470684977137e-09, 1.4078569217513043e-10, 1.1106310914781626e-11, 8.135728562178376e-13, 5.562369697940038e-14, 3.5652872565551664e-15], [0.09073946660854085, 0.10396240888316625, 0.05141547818884244, 0.017576292995580167, 0.004506319201172771, 0.0009242864919452523, 0.000157982875649031, 2.314550355406056e-05, 2.9670940030614987e-06, 3.3809866458044464e-07, 3.467353450406991e-08, 3.23266043843589e-09, 2.762698559978583e-10, 2.179439451330963e-11, 1.5965092216293606e-12, 1.0915278759613917e-13, 6.996317464804782e-15], [0.10044372032159894, 0.10300954032486143, 0.047088285012770785, 0.01724536016353396, 0.004421472585579634, 0.0009068836899733907, 0.00015500831665263254, 2.270971160167293e-05, 2.9112284788791596e-06, 3.317328200528879e-07, 3.402068859547193e-08, 3.1717947328969375e-09, 2.7106814674794077e-10, 2.138404173295739e-11, 1.5664495658057718e-12, 1.0709761924328956e-13, 6.864588256996034e-15], [0.06570168630161223, 0.06738002617613104, 0.03455061949745344, 0.010529312224434298, 0.002892148995266399, 0.0005932057028543542, 0.00010139317582268261, 1.4854749932359405e-05, 1.9042765407257416e-06, 2.1699122263970186e-07, 2.2253423137930938e-08, 2.074716685987674e-09, 1.7730958478011388e-10, 1.3987610149255227e-11, 1.024637256070815e-12, 7.00540975647138e-14, 4.490226196389704e-15], [0.03223231553740459, 0.033055685278116566, 0.016950043938634723, 0.00579434343602103, 0.0013243709966900238, 0.0002910183051499582, 4.974205413013962e-05, 7.287529651081401e-06, 9.342110649851496e-07, 1.0645281652076037e-07, 1.0917213799907738e-08, 1.0178265831181887e-09, 8.698556774026943e-11, 6.862123171014168e-12, 5.026725067214069e-13, 3.436754677845421e-14, 2.202841292869549e-15], [0.012650173514676689, 0.012973320329079573, 0.0066523609405689235, 0.002274098172817657, 0.0005830474187075225, 0.00010661033120418215, 1.952219706314573e-05, 2.8601269577591814e-06, 3.666485598181336e-07, 4.177939368181348e-08, 4.284664212392361e-09, 3.9946502972626195e-10, 3.413910874352517e-11, 2.693168248854966e-12, 1.9728320243402878e-13, 1.3488184847182125e-14, 8.645461585828833e-16], [0.004137330483484325, 0.004243017979732402, 0.0021757026237327224, 0.000743760208657894, 0.00019068986333956495, 3.911220154794546e-05, 5.959727898853946e-06, 9.354251493264819e-07, 1.1991505582917375e-07, 1.366425202474206e-08, 1.4013303324937312e-09, 1.3064791899138435e-10, 1.1165441732455388e-11, 8.808200994407096e-13, 6.452289420083717e-14, 4.411408133680784e-15, 2.8275605643940886e-16], [0.0011598375204470383, 0.001189465398635631, 0.0006099250582987268, 0.00020850183461545847, 5.34569957979001e-05, 1.096450937233082e-05, 1.8740993575227725e-06, 2.4477101666221414e-07, 3.361635759395433e-08, 3.830564720513533e-09, 3.9284159306460936e-10, 3.662515214083619e-11, 3.130061353658359e-12, 2.4692448528667237e-13, 1.808800962860019e-14, 1.2366710109024828e-15, 7.926634932868043e-17], [0.0002844999195268187, 0.0002917674279595137, 0.00014961029191097076, 5.114402157504669e-05, 1.3112622013457728e-05, 2.6895164012945967e-06, 4.5970328343489553e-07, 6.734947656094866e-08, 7.696790359808684e-09, 9.396103639657464e-10, 9.636125719625918e-11, 8.983890116530496e-12, 7.677818552434656e-13, 6.056882533527869e-14, 4.43686050245523e-15, 3.033466299204548e-16, 1.9443473424193326e-17], [6.20318336999627e-05, 6.361642773169325e-05, 3.262074999198505e-05, 1.1151347411159941e-05, 2.8590517335193972e-06, 5.864171575721717e-07, 1.0023284954452211e-07, 1.468475469784616e-08, 1.882484323516244e-09, 1.9122923108384476e-10, 2.1010429428097658e-11, 1.958830704114927e-12, 1.674057287661971e-13, 1.3206314106693168e-14, 9.674048178853396e-16, 6.614113540688004e-17, 4.239418808993755e-18], [1.2172775158326143e-05, 1.2483726902212653e-05, 6.401310931239519e-06, 2.1882771579024576e-06, 5.61044093690481e-07, 1.1507517644307605e-07, 1.9669125805393273e-08, 2.8816529599408303e-09, 3.694080449092174e-10, 4.209383542961871e-11, 3.848432899980943e-12, 3.8438982554905556e-13, 3.2850750573376535e-14, 2.591532165058395e-15, 1.8983803368054827e-16, 1.2979161214523941e-17, 8.319194981961467e-19], [2.171560313427368e-06, 2.227032500963265e-06, 1.1419608586691424e-06, 3.9037736005747816e-07, 1.0008737301844706e-07, 2.0528818036494335e-08, 3.5088706102968463e-09, 5.140720274125636e-10, 6.590049018008473e-11, 7.509323163369133e-12, 7.701147714688456e-13, 6.400710553270727e-14, 5.860404491464815e-15, 4.623159737541037e-16, 3.386612621673148e-17, 2.315415427332318e-18, 1.4841014828187955e-19], [3.5511223111066824e-07, 3.6418352061557323e-07, 1.8674326743566968e-07, 6.383786554208476e-08, 1.6367148597632177e-08, 3.3570489983299556e-09, 5.738007198771003e-10, 8.406548207631257e-11, 1.0776615300268195e-11, 1.2279891496387973e-12, 1.2593579511312576e-13, 1.1741164218415171e-14, 8.94530877681961e-16, 7.56018867644553e-17, 5.538080414132256e-18, 3.7863665736749145e-19, 2.4269304679207147e-20], [5.3604007533763086e-08, 5.497331399060075e-08, 2.818879958933762e-08, 9.636292770751774e-09, 2.470612611651432e-09, 5.067448091969836e-10, 8.661492175296333e-11, 1.2689641019837878e-11, 1.626724503228998e-12, 1.853643267164838e-13, 1.9009943107002248e-14, 1.7723226633186186e-15, 1.514663653364365e-16, 1.0652174483909939e-17, 8.359703728402863e-19, 5.715500750454477e-20, 3.663438983204116e-21], [7.5135331141863e-09, 7.705465208077577e-09, 3.951150089482514e-09, 1.3506938783529183e-09, 3.4629928850519615e-10, 7.102909053852726e-11, 1.2140586361264908e-11, 1.7786736924405362e-12, 2.280137061575273e-13, 2.5982031401214098e-14, 2.6645738556635858e-15, 2.4842181830304035e-16, 2.1230643080630562e-17, 1.674844363310186e-18, 1.0937343207360628e-19, 8.011267464591682e-21, 5.134946318102793e-22], [9.82942077622134e-10, 1.0080511878456124e-09, 5.169008532909654e-10, 1.7670166975280544e-10, 4.5303871953351744e-11, 9.292230534490927e-12, 1.5882665318877806e-12, 2.3269122370117805e-13, 2.9829410831188546e-14, 3.3990443028903466e-15, 3.4858723876766074e-16, 3.24992589369726e-17, 2.7774539756173022e-18, 2.191079713294273e-19, 1.6050360864409782e-20, 9.7827051042409e-22, 6.717684910264357e-23], [1.2055436087083804e-10, 1.236339042172269e-10, 6.33960570218242e-11, 2.1671833312286388e-11, 5.55635927350153e-12, 1.1396591301290066e-12, 1.9479525905277244e-13, 2.8538753597170294e-14, 3.658471480442616e-15, 4.168807326855877e-16, 4.275298894419744e-17, 3.9859188848651035e-18, 3.4064488284876353e-19, 2.6872815852206643e-20, 1.968519854634883e-21, 1.3458702690890402e-22, 7.690394819403872e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9623432731658004, "lambda_away": 1.025544852331707, "rho": -0.1107929355926174, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6008 |
| Legacy p draw | 0.2199 |
| Legacy p away | 0.1793 |
| Legacy p over 1 5 | 0.8124 |
| Legacy p under 3 5 | 0.6473 |
| Legacy p btts yes | 0.5577 |
| Legacy p over 2 5 | 0.5818 |
| Legacy goal margin distribution | {"-1": 0.11185219884014298, "-10": 2.1187686795051723e-08, "-11": 1.9460608355775374e-09, "-12": 1.6421879319310342e-10, "-13": 1.2814407981850664e-11, "-14": 9.29590232070973e-13, "-15": 6.262001444420516e-14, "-16": 3.5652872565551664e-15, "-2": 0.048844759524809093, "-3": 0.014479052471749899, "-4": 0.0033915239855366866, "-5": 0.0006537193591147262, "-6": 0.00010679230908206394, "-7": 1.5116962217038219e-05, "-8": 1.8862995985851148e-06, "-9": 2.1032303651201976e-07, "0": 0.2198931319621098, "1": 0.23471807286132645, "10": 1.4596543005810129e-05, "11": 2.5653297710417154e-06, "12": 4.142189532197778e-07, "13": 6.184804542844392e-08, "14": 8.584980359053737e-09, "15": 1.1065759818393608e-09, "16": 1.2055436087083804e-10, "2": 0.18725001774697747, "3": 0.10620974242280506, "4": 0.047603559558165885, "5": 0.017557238295781978, "6": 0.00548813968107563, "7": 0.0014865175084022983, "8": 0.00035492492182015185, "9": 7.572390258489407e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5803 |
| Legacy raw p draw | 0.2383 |
| Legacy raw p away | 0.1814 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9623 |
| Legacy lambda away | 1.0255 |
| Legacy model home team | Ein Frankfurt |
| Legacy model away team | Hamburg |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 81.0% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:37:38Z |
| Market reference home draw last update utc | 2026-10-31T11:37:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.0% |
| Market draw away odds | 2.50 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:37:38Z |
| Market reference draw away last update utc | 2026-10-31T11:37:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.0% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:37:38Z |
| Market reference home away last update utc | 2026-10-31T11:37:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.41 |
| Market reference dc home away odds | 1.22 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.66, "price": 1.44, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.44, "price": 2.66, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.01, "price": 1.81, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.81, "price": 2.01, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.24, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.24, "price": 1.61, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 86.8% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 5.70 |
| Market reference over 1 5 last update utc | 2026-10-31T11:37:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 53.4% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market reference under 3 5 odds | 1.81 |
| Market reference under 3 5 opposite odds | 2.06 |
| Market reference under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.4% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:37:38Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.66 |
| Market reference btts yes last update utc | 2026-10-31T11:37:48Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 10.303752938389106, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.6780 |
| Elo away rating | 1,410.4104 |
| Elo rating diff | 124.2676 |
| Elo home expectancy | 0.6716 |

</details>


---

## 2026-11-01 — Union Berlin vs 1. FC Köln

The model's most likely 1X2 outcome is **Union Berlin win** at **37.2%**. Expected goals are 1.44 for Union Berlin and 1.19 for 1. FC Köln (2.63 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.3%; Under 3.5 goals: 63.7%; Double Chance 1X: 64.1%; Double Chance X2: 62.8%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 62.1%; BTTS No (at least one team does not score): 37.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 37.2% | 2.69 |
| Draw | 26.9% | 3.72 |
| 1. FC Köln win | 35.9% | 2.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 1.44 |
| 1. FC Köln expected goals | 1.19 |
| Expected total goals | 2.63 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 81.5% |
| Under 1.5 | 18.5% |
| Over 2.5 | 58.3% |
| Under 2.5 | 41.7% |
| Over 3.5 | 36.3% |
| Under 3.5 | 63.7% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.37% |
| 2 | 1-2 | 8.75% |
| 3 | 2-1 | 7.75% |
| 4 | 2-2 | 6.67% |
| 5 | 0-1 | 6.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 37.2% | 35.1% | 2.76 | +2.7% |
| Draw | 26.9% | 26.5% | 3.63 | -2.5% |
| 1. FC Köln win | 35.9% | 38.4% | 2.53 | -9.1% |

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
| Market best home last update utc | 2026-10-31T11:37:47Z |
| Market best draw last update utc | 2026-10-31T11:37:47Z |
| Market best away last update utc | 2026-10-31T11:37:47Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Union Berlin |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4333 |
| Dc lambda away | 1.1508 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-31T11:37:21.613878+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.4864 |
| Shot lambda away | 1.3222 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 62.1% |
| P btts no | 37.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.17 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.42 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.40 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.19477122940374295, "-10": 4.612122616700871e-07, "-11": 5.681883910894701e-08, "-12": 6.432947124031018e-09, "-13": 6.733472997519682e-10, "-14": 6.496503081724158e-11, "-15": 5.172160570033848e-12, "-2": 0.10586937157640088, "-3": 0.04143288554679597, "-4": 0.012889166219003096, "-5": 0.003311025750299924, "-6": 0.0007224516184645006, "-7": 0.00013679427977862725, "-8": 2.2855584354634397e-05, "-9": 3.4148144969599983e-06, "0": 0.26863933806580975, "1": 0.17406160997817047, "10": 2.4185442569525134e-06, "11": 3.6303053001924756e-07, "12": 5.0079314395549685e-08, "13": 6.386826449007057e-09, "14": 7.50798230559872e-10, "15": 7.283048299711096e-11, "2": 0.11429907989220513, "3": 0.054502343787553656, "4": 0.02065819736552457, "5": 0.0064658817167299095, "6": 0.0017189829337153316, "7": 0.00039657773974322865, "8": 8.073285758946742e-05, "9": 1.4696797532093348e-05} |
| Raw goal margin distribution | {"-1": 0.17371358740173568, "-10": 1.267916540333067e-07, "-11": 1.3486806877492142e-08, "-12": 1.3172471975978172e-09, "-13": 1.182424670942214e-10, "-14": 8.918953443569503e-12, "-2": 0.08650204362227955, "-3": 0.03018882688405186, "-4": 0.008273059133066477, "-5": 0.0018588612531112768, "-6": 0.0003531790732345908, "-7": 5.805878159676784e-05, "-8": 8.404496091276133e-06, "-9": 1.0863286831524933e-06, "0": 0.27772652200132747, "1": 0.21363392673682627, "10": 9.142535620982347e-07, "11": 1.1849028166094656e-07, "12": 1.4100628665717884e-08, "13": 1.5422055951507583e-09, "14": 1.4173603785607245e-10, "2": 0.1284167180949166, "3": 0.05460583281674396, "4": 0.018232932577524306, "5": 0.004991544781872692, "6": 0.001155528227121356, "7": 0.0002314467641136265, "8": 4.082183044581696e-05, "9": 6.428943973925635e-06} |
| Unadjusted home-win probability | 42.1% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 30.1% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 73.0% |
| Raw p btts yes | 53.9% |
| P home draw | 64.1% |
| P draw away | 62.8% |
| P home away | 73.1% |
| Raw p home draw | 69.9% |
| Raw p draw away | 57.9% |
| Raw p home away | 72.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1633 |
| Totals anchor target over 2 5 | 0.5833 |
| Totals anchor reference over odds | 1.67 |
| Totals anchor reference under odds | 2.30 |
| Totals anchor reference last update utc | 2026-10-31T11:37:47Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4911 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-31T11:37:23Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.15, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-31T11:37:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.42, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.76 |
| Reference draw odds | 3.63 |
| Reference away odds | 2.53 |
| Market reference 1x2 last update utc | 2026-10-31T11:37:47Z |
| Market reference home last update utc | 2026-10-31T11:37:47Z |
| Market reference draw last update utc | 2026-10-31T11:37:47Z |
| Market reference away last update utc | 2026-10-31T11:37:47Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-10-31T11:37:23Z |
| Market reference under 2 5 last update utc | 2026-10-31T11:37:23Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.4% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0702 |
| Raw ev home | 0.1628 |
| Raw edge prob draw | 0.0130 |
| Raw ev draw | 0.0081 |
| Raw edge prob away | -0.0831 |
| Raw ev away | -0.2386 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09218772112240174, 0.09042495172971243, 0.05691801345572231, 0.020098932092845752, 0.005323012611645502, 0.0011277997510652945, 0.00019912475185578348, 3.0135035761325167e-05, 3.990490008845299e-06, 4.697082864481557e-07, 4.975912393769226e-08, 4.792085344113611e-09, 4.230462030679754e-10, 3.447378373272863e-11, 2.6085875711884532e-12], [0.0939643756689088, 0.1328812593247159, 0.08142777400673169, 0.028753837333167716, 0.007615182640083447, 0.0016134474427157018, 0.00028487089251406656, 4.3111639579038495e-05, 5.708855578193198e-06, 6.719718042820131e-07, 7.118615799764898e-08, 6.855630032221797e-09, 6.052163195158349e-10, 4.931871828466552e-11, 3.731884975021867e-12], [0.07615129796502848, 0.08067181233082688, 0.04532501611130335, 0.02056783807127157, 0.005447197937776588, 0.0011541112010119267, 0.00020377031143906953, 3.0838082986087476e-05, 4.083587722363229e-06, 4.806665315237778e-07, 5.091999908209461e-08, 4.903884192758982e-09, 4.3291582663068835e-10, 3.527805349276176e-11, 2.6694456457233163e-12], [0.03631440092241554, 0.0384701064119074, 0.020376889742795685, 0.007632429297633291, 0.002597614684217421, 0.0005503630007967119, 9.717230018957933e-05, 1.4705809870106044e-05, 1.947347526759869e-06, 2.2921627867403383e-07, 2.4282307866707727e-08, 2.3385237206951807e-09, 2.0644531759846644e-10, 1.682310627045257e-11, 1.2729831534048324e-12], [0.012987983293727443, 0.01375897954239293, 0.00728787194157442, 0.0025734988690181318, 0.0007229531253266197, 0.0001968394157211922, 3.475404190672725e-05, 5.259588704815256e-06, 6.964762326294288e-07, 8.198007188468027e-08, 8.684659553650382e-09, 8.363818828035905e-10, 7.383595124605417e-11, 6.016847796995282e-12, 4.552872554593881e-13], [0.0037161612088502005, 0.003936760996104579, 0.002085228044405198, 0.0007363373090173099, 0.0001950119918918188, 4.3826568011867817e-05, 9.943931976483828e-06, 1.5048894872524686e-06, 1.9927789403868368e-07, 2.3456387042300186e-08, 2.4848811563325934e-09, 2.3930812339132514e-10, 2.1126166521299438e-11, 1.7215587575900432e-12, 1.3026817169060912e-13], [0.0008860661054818045, 0.0009386650061691833, 0.0004971931486576239, 0.0001755692218540189, 4.649785261369119e-05, 9.851614194575585e-06, 1.8450251671564106e-06, 3.588196238566504e-07, 4.751499667424409e-08, 5.592843891095737e-09, 5.924847833654618e-10, 5.7059638962519005e-11, 5.0372357498128246e-12, 4.104813483502979e-13, 3.106060395960232e-14], [0.00018108851715364894, 0.0001918383436851696, 0.00010161315219297905, 3.588171339211347e-05, 9.502933391254934e-06, 2.013409829163324e-06, 3.5548840318278356e-07, 5.706548947646004e-08, 9.710810781573355e-09, 1.1430296234609426e-09, 1.2108824634185901e-10, 1.166148365806926e-11, 1.0294779891066324e-12, 8.389154966216266e-14, 6.34796735609547e-15], [3.238349767220968e-05, 3.430585579812436e-05, 1.8171164738818008e-05, 6.416615478288419e-06, 1.699380094287038e-06, 3.60051832886748e-07, 6.357088819275939e-08, 9.620657257393426e-09, 1.3513284026781914e-09, 2.0440444116734152e-10, 2.1653835401481896e-11, 2.08538694132207e-12, 1.8409835470428653e-13, 1.5002065541779528e-14, 1.1351873069067122e-15], [5.1475914797880055e-06, 5.453164225827469e-06, 2.888438232774171e-06, 1.0199675000967708e-06, 2.7012877308124316e-07, 5.7232846371638165e-08, 1.0105053065482389e-08, 1.5292731449023814e-09, 2.0250678492176534e-10, 2.528385076943789e-11, 3.442033956481956e-12, 3.314873569207689e-13, 2.9263766740429185e-14, 2.384686964445991e-15, 1.8044624358199404e-16], [7.364222506135519e-07, 7.801379514899959e-07, 4.1322435793319533e-07, 1.4591809876973294e-07, 3.864503230473119e-08, 8.1878178755081e-09, 1.4456442299804217e-09, 2.1878013738927398e-10, 2.8970928035404736e-11, 3.4100786956387884e-12, 3.831868092582269e-13, 4.7423084444840944e-14, 4.186518889277589e-15, 3.411569368434884e-16, 2.581491350570147e-17], [9.577607726009312e-08, 1.014615631903907e-07, 5.374227625277266e-08, 1.8977513362438675e-08, 5.026015437003713e-09, 1.0648742304878483e-09, 1.8801459807312446e-10, 2.8453653218803613e-11, 3.767840854216119e-12, 4.4350094031567794e-13, 4.6982816553070687e-14, 4.79946150321995e-15, 5.4448158818697e-16, 4.43694811145585e-17, 3.3573824641022963e-18], [1.1418225825896392e-08, 1.2096037698539705e-08, 6.407043013313642e-09, 2.262459889621924e-09, 5.991911644940754e-10, 1.2695210315273747e-10, 2.2414711489322826e-11, 3.3921856826706246e-12, 4.491941931662715e-13, 5.2873264758691626e-14, 5.601194209309619e-15, 5.394267132511639e-16, 5.051232428147985e-17, 5.289637763802705e-18, 4.0026019289680847e-19], [1.25654516795893e-09, 1.3311365489967355e-09, 7.050779220906023e-10, 2.48977650762319e-10, 6.593938269473729e-11, 1.397073890560162e-11, 2.466678960686171e-12, 3.7330094827097303e-13, 4.943261777308364e-14, 5.818561163509957e-15, 6.163964197086642e-16, 5.936246491696141e-17, 5.2405296618358896e-18, 4.529789077911426e-19, 4.40475621151336e-20], [1.284023278819219e-10, 1.3602458230572364e-10, 7.204965555009859e-11, 2.5442229028967806e-11, 6.738134412513152e-12, 1.4276250814156284e-12, 2.5206202591502563e-13, 3.814642878009819e-14, 5.051360951609394e-15, 5.945801371641913e-16, 6.298757673569084e-17, 6.066060240817302e-18, 5.355129485770961e-19, 4.363863200151755e-20, 3.50258949793261e-21]] |
| Legacy trial inputs | {"lambda_home": 1.4306151789727524, "lambda_away": 1.05936227597689, "rho": -0.1107929355926174, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3964 |
| Legacy p draw | 0.2788 |
| Legacy p away | 0.3248 |
| Legacy p over 1 5 | 0.7234 |
| Legacy p under 3 5 | 0.7610 |
| Legacy p btts yes | 0.5094 |
| Legacy p over 2 5 | 0.4575 |
| Legacy goal margin distribution | {"-1": 0.19522533057795985, "-10": 5.706494819007065e-08, "-11": 5.433852700275613e-09, "-12": 4.750343669983642e-10, "-13": 3.8205668707750495e-11, "-14": 2.6085875711884532e-12, "-2": 0.09170571933887316, "-3": 0.02897086281677669, "-4": 0.007155656712622827, "-5": 0.001445540597149549, "-6": 0.00024655812452579876, "-7": 3.634969810378749e-05, "-8": 4.715795924500711e-06, "-9": 5.460109210721308e-07, "0": 0.2787951090170497, "1": 0.1977918055326607, "10": 8.44546572602431e-07, "11": 1.086026351097524e-07, "12": 1.2821412030443226e-08, "13": 1.3925697502646535e-09, "14": 1.284023278819219e-10, "2": 0.1226941900195519, "3": 0.05234405104394637, "4": 0.017459577239375374, "5": 0.00476313449073842, "6": 0.0010971353141054879, "7": 0.00021843388475568275, "8": 3.82694771832982e-05, "9": 5.983801534428173e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4417 |
| Legacy raw p draw | 0.2928 |
| Legacy raw p away | 0.2655 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4306 |
| Legacy lambda away | 1.0594 |
| Legacy model home team | Union Berlin |
| Legacy model away team | FC Koln |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 62.4% |
| Market home draw odds | 1.56 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-31T11:37:38Z |
| Market reference home draw last update utc | 2026-10-31T11:37:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.2% |
| Market draw away odds | 1.49 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-31T11:37:38Z |
| Market reference draw away last update utc | 2026-10-31T11:37:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.5% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-31T11:37:38Z |
| Market reference home away last update utc | 2026-10-31T11:37:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.54 |
| Market reference dc draw away odds | 1.52 |
| Market reference dc home away odds | 1.29 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.57, "price": 1.47, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.47, "price": 2.57, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.96, "price": 1.85, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.85, "price": 1.96, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.59, "price": 2.28, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-31T11:37:38Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.28, "price": 1.59, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 80.7% |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-31T11:37:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.6% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.59 |
| Market reference under 3 5 last update utc | 2026-10-31T11:37:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.6% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-31T11:37:38Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.62 |
| Market reference btts yes last update utc | 2026-10-31T11:37:48Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 10.176507153371874, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,423.5440 |
| Elo away rating | 1,399.5687 |
| Elo rating diff | 83.9753 |
| Elo home expectancy | 0.6186 |

</details>


---
