# La Liga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,999 |
| Training data through | 2026-10-26 |
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
| Training sha256 | 52a0b16db419da627916b95040bdf4d32e045e308c16dd1928af6d14745798ef |
| Training as of utc | 2026-10-28T11:48:18.595123+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 99, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 99, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 82, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-10-28T11:48:18.595123+00:00', 'observations': 381, 'observations_sha256': '35b48cd4f62948e5d4f6d9900ab67ded35a7d4f16596a5d5dc77a0ed3f5fc376', 'eligible_training_matches': 140, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 153, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 20, 'retrospective_eligible_training_matches': 140, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '302f78cd279408d7ed03f49af6843a0b81c8eabad3c0edc756de43e85a76beb6', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 80, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-20T00:00:00+00:00', 'audit_origin_utc': '2026-09-18T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 16, 'selected_ridge': 1.0, 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8175310729051967, 'audit_candidate_poisson_score': 0.8069329890033836, 'audit_gain': 0.010598083901813049, 'audit_gain_lower95': -0.016991554638011257, 'audit_baseline_briers': [0.552093299134768, 0.18075667919524327, 0.22581865901912312, 0.2521852580679206], 'audit_candidate_briers': [0.5384668935368899, 0.18516883120715347, 0.22823371406662382, 0.25285535105064827], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1620, 'tuning_matches': 230, 'audit_matches': 135, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8136086319179086, 'audit_candidate_poisson_score': 0.81493464214411, 'audit_gain': -0.0013260102262014906, 'audit_gain_lower95': -0.01113868773614534, 'audit_baseline_briers': [0.5676553268100237, 0.1855855771539734, 0.20276536589243288, 0.2468256123726131], 'audit_candidate_briers': [0.571305015059924, 0.1822429267896673, 0.20478339722054126, 0.2441757973228736], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1839.273 |
| Base scoring parameter | 0.091 |
| Home-advantage parameter | 0.288 |
| Dixon-Coles low-score adjustment | -0.033 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1999, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261028T114818595123Z_b5fa04b839fa0cce06dff270ed4737c3a411182301043aae4a7af3e8efa4f3f4.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'AVAILABLE': 1} |
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

## 2026-10-30 — Villarreal vs Espanyol

The model's most likely 1X2 outcome is **Villarreal win** at **67.9%**. Expected goals are 2.16 for Villarreal and 0.95 for Espanyol (3.12 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 61.0%; Under 3.5 goals: 61.7%; Double Chance 1X: 86.4%; Double Chance X2: 32.1%; Double Chance 12 (either team wins): 81.4%; Under 4.5 goals: 79.1%; BTTS Yes (both teams score): 54.1%; BTTS No (at least one team does not score): 45.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 67.9% | 1.47 |
| Draw | 18.6% | 5.39 |
| Espanyol win | 13.6% | 7.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.16 |
| Espanyol expected goals | 0.95 |
| Expected total goals | 3.12 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 82.4% |
| Under 1.5 | 17.6% |
| Over 2.5 | 61.0% |
| Under 2.5 | 39.0% |
| Over 3.5 | 38.3% |
| Under 3.5 | 61.7% |
| Over 4.5 | 20.9% |
| Under 4.5 | 79.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.89% |
| 2 | 2-1 | 10.36% |
| 3 | 1-0 | 9.75% |
| 4 | 1-1 | 8.71% |
| 5 | 3-0 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 67.9% | 69.2% | 1.42 | -3.6% |
| Draw | 18.6% | 17.9% | 5.16 | -4.3% |
| Espanyol win | 13.6% | 12.9% | 7.06 | -4.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:00:00+00:00 |
| Fixture id | 00b03cb40c27ed23e2ecb18f062a5122 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T11:48:49Z |
| Market best draw last update utc | 2026-10-28T11:48:49Z |
| Market best away last update utc | 2026-10-28T11:48:49Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Villarreal |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1639 |
| Dc lambda away | 0.9515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T11:48:18.595123+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.1% |
| P btts no | 45.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.88 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.67 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.61 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.79 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.08989194124219296, "-10": 8.015850187020033e-09, "-11": 6.828836583627821e-10, "-12": 5.345144362362472e-11, "-13": 3.869038016639369e-12, "-14": 2.6043253139019604e-13, "-15": 1.6377014612125174e-14, "-16": 9.607929198867589e-16, "-17": 4.7968427236982656e-17, "-2": 0.03395764268630229, "-3": 0.009313421179034762, "-4": 0.002020317081134852, "-5": 0.00036083530813275596, "-6": 5.4638621201816624e-05, "-7": 7.170761950700239e-06, "-8": 8.297002483848359e-07, "-9": 8.579396160931529e-08, "0": 0.18551766989139643, "1": 0.24344589555006707, "10": 3.473256163901157e-05, "11": 6.728831334132645e-06, "12": 1.1977276086256816e-06, "13": 1.9715478292589285e-07, "14": 3.017902825375523e-08, "15": 4.315692122038791e-09, "16": 5.757728886833742e-10, "17": 6.537061875048276e-11, "2": 0.20572125516262044, "3": 0.12830883850445793, "4": 0.06329546064690374, "5": 0.025707968279484666, "6": 0.008852463783730058, "7": 0.002642015928636534, "8": 0.0006951796417715124, "9": 0.00016347006921088765} |
| Raw goal margin distribution | {"-1": 0.10044589653756433, "-10": 8.956968193363575e-09, "-11": 7.630590723399096e-10, "-12": 5.972702448973256e-11, "-13": 4.3232906860047735e-12, "-14": 2.9100916880363306e-13, "-15": 1.829979298023638e-14, "-16": 1.073596864094325e-15, "-17": 5.3600262857090104e-17, "-2": 0.0379445122309463, "-3": 0.010406883278219703, "-4": 0.0022575167217491793, "-5": 0.00040319994792581854, "-6": 6.105358518630822e-05, "-7": 8.012660568258606e-06, "-8": 9.27112977590665e-07, "-9": 9.586678485603943e-08, "0": 0.20092488035767989, "1": 0.23221146792990072, "10": 3.312973958725842e-05, "11": 6.418312364729547e-06, "12": 1.1424554336835792e-06, "13": 1.880565759762709e-07, "14": 2.8786340536438423e-08, "15": 4.116533575264295e-09, "16": 5.492023900148633e-10, "17": 6.23539259318242e-11, "2": 0.1962277266484832, "3": 0.12238770208131583, "4": 0.06037453125634646, "5": 0.024521608952107928, "6": 0.00844394441471894, "7": 0.0025200934100640675, "8": 0.0006630988159648231, "9": 0.00015592632871584358} |
| Unadjusted home-win probability | 64.8% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 15.2% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 54.6% |
| P home draw | 86.4% |
| P draw away | 32.1% |
| P home away | 81.4% |
| Raw p home draw | 84.8% |
| Raw p draw away | 35.2% |
| Raw p home away | 79.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6097 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T11:48:49Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T11:47:41Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.28, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T11:47:41Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.74, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T11:48:49Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.42 |
| Reference draw odds | 5.16 |
| Reference away odds | 7.06 |
| Market reference 1x2 last update utc | 2026-10-28T11:48:49Z |
| Market reference home last update utc | 2026-10-28T11:48:49Z |
| Market reference draw last update utc | 2026-10-28T11:48:49Z |
| Market reference away last update utc | 2026-10-28T11:48:49Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.61 |
| Market reference over 2 5 last update utc | 2026-10-28T11:48:02Z |
| Market reference under 2 5 last update utc | 2026-10-28T11:48:02Z |
| Home probability edge | -1.3% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | -0.0448 |
| Raw ev home | -0.0805 |
| Raw edge prob draw | 0.0220 |
| Raw ev draw | 0.0368 |
| Raw edge prob away | 0.0227 |
| Raw ev away | 0.0698 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.040705418920783984, 0.03486595874874144, 0.01794647419706022, 0.005857954676577472, 0.0014340825090224563, 0.00028086153017294665, 4.583836624624646e-05, 6.412379444971732e-06, 7.849054585568933e-07, 8.540100135430736e-08, 8.362787973413956e-09, 7.444688382317598e-10, 6.07509957749851e-11, 4.5761280833789384e-12, 3.20079794094099e-13, 2.0895613323296904e-14, 1.2788607644086627e-15, 7.366521573081634e-17], [0.09072461207956836, 0.08664903902565348, 0.04000048890208589, 0.013056662186478003, 0.0031963939466296367, 0.0006260058882510825, 0.00010216809386565089, 1.4292406965741046e-05, 1.7494579570027562e-06, 1.9034835307425328e-07, 1.8639628254993883e-08, 1.6593296919857577e-09, 1.3540651526337266e-10, 1.0199627993988229e-11, 7.134185863393847e-13, 4.657375814675245e-14, 2.8504237240327362e-15, 1.6419072693359272e-16], [0.10332133743969149, 0.10117614833963735, 0.046267461097545634, 0.014550848962133477, 0.0035621849502282003, 0.0006976451561089837, 0.00011386007245617319, 1.5928010703931736e-05, 1.949663561358971e-06, 2.121315613605104e-07, 2.0772722122627958e-08, 1.849221139494088e-09, 1.5090225387975933e-10, 1.1366859637693147e-11, 7.950612452357069e-13, 5.1903596088605924e-14, 3.1766223629065512e-15, 1.8298049183411287e-16], [0.07676352777754447, 0.07516974001646164, 0.03680452148132882, 0.011220376829888634, 0.0026465577212955, 0.0005183218166441227, 8.459337685058883e-05, 1.183386048236137e-05, 1.4485202830112774e-06, 1.5760507370993282e-07, 1.5433282913186466e-08, 1.373895671755454e-09, 1.1211420258815766e-10, 8.445111795526447e-12, 5.906979864553572e-13, 3.856224898780255e-14, 2.36010048878897e-15, 1.3594702135805623e-16], [0.042774121078523825, 0.041886031739227336, 0.02050819059074057, 0.006694131095613761, 0.0015306001223157957, 0.00028881893243657976, 4.713706428831908e-05, 6.594055741754961e-06, 8.0714349332375e-07, 8.782059267774292e-08, 8.599723476503148e-09, 7.65561217864178e-10, 6.24722002097831e-11, 4.705779488279181e-12, 3.2914833287368634e-13, 2.1487630324188475e-14, 1.3150935996257559e-15, 7.57523073807353e-17], [0.01906765347566983, 0.018671765042426396, 0.009142048082749972, 0.002984079364659485, 0.0007305307498372918, 0.00013362755393769493, 2.1012546489501304e-05, 2.939468227815045e-06, 3.59804761565659e-07, 3.914826504869798e-08, 3.8335456837446186e-09, 3.4126840361835193e-10, 2.7848573750376682e-11, 2.0977210133833322e-12, 1.467262493087437e-13, 9.578658279915747e-15, 5.862364535720481e-16, 3.376851962584231e-17], [0.007083243323706158, 0.006936178866861368, 0.0033960839035472663, 0.001108524458140809, 0.00027137723386622825, 5.3148563404295e-05, 8.101544122315907e-06, 1.0919523331218852e-06, 1.3366011074459757e-07, 1.4542779865110168e-08, 1.4240838236941336e-09, 1.2677423284443408e-10, 1.0345175631799374e-11, 7.792604570879758e-13, 5.45058009972092e-14, 3.558275662909931e-15, 2.1777485369009272e-16, 1.2544314458850073e-17], [0.0022553828906491484, 0.002208555943637422, 0.0010813506159861555, 0.0003529664283012021, 8.640950793334266e-05, 1.6923089478438067e-05, 2.7619545227606406e-06, 3.6086603281817446e-07, 4.255885519656353e-08, 4.630581697013443e-09, 4.534440148428265e-10, 4.0366315636168774e-11, 3.294018157280054e-12, 2.4812513448374163e-13, 1.735524891525421e-14, 1.132994263162099e-15, 6.934191818350022e-17, 3.994248243700016e-18], [0.0006283714651743673, 0.0006153250252880863, 0.00030127472978162616, 9.833985733799394e-05, 2.407452381153903e-05, 4.714936242059705e-06, 7.69507216449864e-07, 1.0764721043967353e-07, 1.2306663188436681e-08, 1.2901248021458841e-09, 1.2633388377763432e-10, 1.1246445561485008e-11, 9.17745285903665e-13, 6.913005988852738e-14, 4.8353400367443965e-15, 3.1566314887331997e-16, 1.93193283976833e-17, 1.1128361537058243e-18], [0.00015561809921299882, 0.0001523871088050618, 7.461160060238682e-05, 2.4354163936405864e-05, 5.962128840414774e-06, 1.1676682608370953e-06, 1.905707960837849e-07, 2.6659158161415225e-08, 3.2632065742514103e-09, 3.3161149738486696e-10, 3.128696949059572e-11, 2.7852163539843643e-12, 2.2728240359289374e-13, 1.7120269004176043e-14, 1.1974866257777513e-15, 7.817493623079266e-17, 4.784490273575562e-18, 2.755972487183991e-19], [3.4685364836469796e-05, 3.3965216719707105e-05, 1.663001026882216e-05, 5.428244308942645e-06, 1.3288853615206672e-06, 2.602589277206502e-07, 4.247589208948795e-08, 5.9419992387659204e-09, 7.273287049326877e-10, 7.913640940806471e-11, 7.237754754996241e-12, 6.207905499104074e-13, 5.065845894145706e-14, 3.815897890486181e-15, 2.6690507538614784e-16, 1.7424234057257462e-17, 1.066404174930621e-18, 6.142724508311242e-20], [7.028129293462535e-06, 6.8822091309123034e-06, 3.3696593036265545e-06, 1.0998991366998105e-06, 2.6926567389416324e-07, 5.273501958022983e-08, 8.606686505029918e-09, 1.203998836644591e-09, 1.4737513072772554e-10, 1.6035031482657762e-11, 1.5702107271570183e-12, 1.3055477982241278e-13, 1.0264680822205813e-14, 7.731971069478121e-16, 5.408169663889085e-17, 3.5305890646189435e-18, 2.1608036864643947e-19, 1.2446708363044112e-20], [1.3054031519815356e-06, 1.278299973855898e-06, 6.258797600877489e-07, 2.04295017913981e-07, 5.001334562083734e-08, 9.794990659018529e-09, 1.598604012910494e-09, 2.236304727347472e-10, 2.7373423587214968e-11, 2.9783431359260023e-12, 2.91650586794504e-13, 2.5963204401543398e-14, 1.978812149782517e-15, 1.4361345649283182e-16, 1.0045122152574368e-17, 6.557708176473348e-19, 4.013471900335892e-20, 2.3118488079077255e-21], [2.2381411146973988e-07, 2.1916721466932406e-07, 1.0730839907832157e-07, 3.5026809796426006e-08, 8.574893123833244e-09, 1.6793717158372865e-09, 2.7408401473400425e-10, 3.834191412569325e-11, 4.693230952259868e-12, 5.106431845268791e-13, 5.000410550867388e-14, 4.4514459117231145e-15, 3.632519695760301e-16, 2.5555956915469175e-17, 1.7222572856291321e-18, 1.124332836616278e-19, 6.8811818473007e-21, 3.963713324951153e-22], [3.563244227437974e-08, 3.4892630647183916e-08, 1.7084089607242497e-08, 5.576461510540512e-09, 1.3651703292411662e-09, 2.673652493528706e-10, 4.3635688425571296e-11, 6.10424442320164e-12, 7.471882799907459e-13, 8.129721435334752e-14, 7.960929680971947e-15, 7.086947665873284e-16, 5.783171915289457e-17, 4.356230720988695e-18, 2.845839215253579e-19, 1.7899999528553283e-20, 1.0955221426536486e-21, 6.310450458911626e-23], [5.294689441873848e-09, 5.184759485871206e-09, 2.5385559645607577e-09, 8.286165639593028e-10, 2.0285314357443854e-10, 3.972828895566504e-11, 6.483906351877783e-12, 9.070407874169675e-13, 1.1102606626555598e-13, 1.2080101026359328e-14, 1.182929028686009e-15, 1.053062450580086e-16, 8.593320391748943e-18, 6.473002503499274e-19, 4.5275771804026845e-20, 2.7605913646395027e-21, 1.627856288205622e-22, 9.376813175192035e-24], [7.375758182851006e-10, 7.222620443342722e-10, 3.536331098129089e-10, 1.1543029046677615e-10, 2.8258422898297412e-11, 5.534342581794758e-12, 9.032394790425486e-13, 1.2635516366759019e-13, 1.5466467405841172e-14, 1.6828164328237393e-15, 1.647877285126463e-16, 1.4669668678755082e-17, 1.1970910455301608e-18, 9.017205202861333e-20, 6.307133742867074e-21, 4.117455406464173e-22, 2.3536205292174915e-23, 1.3062353753747437e-24], [9.670388213633569e-11, 9.46960866602766e-11, 4.636498882293171e-11, 1.5134114931012243e-11, 3.704973955991861e-12, 7.256100314898235e-13, 1.1842411580859756e-13, 1.6566479745821786e-14, 2.027815180488755e-15, 2.2063478484861698e-16, 2.16053898196561e-17, 1.9233465573583646e-18, 1.569511208252013e-19, 1.1822496447403799e-20, 8.269310123350123e-22, 5.39841345740026e-23, 3.3039562198577398e-24, 1.7775134040846954e-25]] |
| Legacy trial inputs | {"lambda_home": 2.228877297170622, "lambda_away": 0.9792376952020558, "rho": -0.021885823849288083, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6735 |
| Legacy p draw | 0.1865 |
| Legacy p away | 0.1400 |
| Legacy p over 1 5 | 0.8337 |
| Legacy p under 3 5 | 0.5980 |
| Legacy p btts yes | 0.5560 |
| Legacy p over 2 5 | 0.6258 |
| Legacy goal margin distribution | {"-1": 0.09237482164641367, "-10": 1.0181803979835254e-08, "-11": 8.918549975303732e-10, "-12": 7.178559612531609e-11, "-13": 5.3438861186030984e-12, "-14": 3.699661216251161e-13, "-15": 2.3929017539163753e-14, "-16": 1.4430514913422553e-15, "-17": 7.366521573081634e-17, "-2": 0.03513385810278966, "-3": 0.009843556024371479, "-4": 0.002186630087355721, "-5": 0.00040049793930249823, "-6": 6.224699343715189e-05, "-7": 8.390196452976014e-06, "-8": 9.974650550051433e-07, "-9": 1.060068210858515e-07, "0": 0.18651499860592538, "1": 0.23618596525506258, "10": 4.222988635569043e-05, "11": 8.419522633817566e-06, "12": 1.5425120568549912e-06, "13": 2.6136443334590734e-07, "14": 4.118596898499486e-08, "15": 6.063316475031052e-09, "16": 8.322719049453772e-10, "17": 9.670388213633569e-11, "2": 0.20227244464493235, "3": 0.12899145316503755, "4": 0.06522022235265414, "5": 0.02718975403871619, "6": 0.009618811419148075, "7": 0.002951027101814107, "8": 0.000798540220660704, "9": 0.00019316611912490895} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6546 |
| Legacy raw p draw | 0.1941 |
| Legacy raw p away | 0.1512 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2289 |
| Legacy lambda away | 0.9792 |
| Legacy model home team | Villarreal |
| Legacy model away team | Espanol |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01468479762968863, "mu": 10.164044473652304, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,563.5990 |
| Elo away rating | 1,432.0064 |
| Elo rating diff | 191.5927 |
| Elo home expectancy | 0.7508 |

</details>


---
