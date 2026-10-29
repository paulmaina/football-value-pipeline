# Premier League — football model report

Fixtures in this report: **8**.

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
| Training sha256 | c913096327d9efa08f5a726520cc60ba30678e0bfd1415f333a3f08aba3fec06 |
| Training as of utc | 2026-10-29T11:48:36.104635+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 80, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 80, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 166, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-29T11:48:36.104635+00:00', 'observations': 431, 'observations_sha256': '1b32174bba2caf259c3e394bbae13fb0c88637f7ab6777517d9205e2ee261e6b', 'eligible_training_matches': 222, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 205, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 18, 'retrospective_eligible_training_matches': 222, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '3ed3f2793af1dc0a4980cf0477553a4f9137b241daadad05ecd1d5f71a333ebe', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 161, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-21T00:00:00+00:00', 'audit_origin_utc': '2025-10-19T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 31, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-29', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1979, 'tune_start_date': '2025-10-30', 'audit_start_date': '2026-04-30', 'training_shot_matches': 1609, 'tuning_matches': 249, 'audit_matches': 114, 'audit_matchdays': 38, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.929200845416159, 'audit_candidate_poisson_score': 0.9172355016612314, 'audit_gain': 0.011965343754927638, 'audit_gain_lower95': 0.0018383116577410925, 'audit_baseline_briers': [0.6363739648435346, 0.15621970125887985, 0.21728847237239374, 0.2522562096024789], 'audit_candidate_briers': [0.6347872769493693, 0.15465302512048604, 0.21528351959541353, 0.24899227063248608], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1869.703 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.175 |
| Dixon-Coles low-score adjustment | -0.076 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1980, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 8.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261029T114836104635Z_fadf22c0fdc19c5d939ce8c3c5ca4b913de1efaa7f3f7640f80581e4a58053a5.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 5, 'ANCHORED_MAIN': 3} |
| Shot features applied fixtures | 8 |
| Goal rate features used | {'shot_features': 8} |
| Legacy comparison status | {'AVAILABLE': 8} |
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

The model's most likely 1X2 outcome is **Aston Villa win** at **48.2%**. Expected goals are 1.56 for Aston Villa and 1.15 for Fulham (2.72 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 51.5%; Under 3.5 goals: 70.9%; Double Chance 1X: 74.0%; Double Chance X2: 51.8%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 54.7%; BTTS No (at least one team does not score): 45.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 48.2% | 2.08 |
| Draw | 25.9% | 3.87 |
| Fulham win | 26.0% | 3.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.56 |
| Fulham expected goals | 1.15 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.32% |
| 2 | 1-0 | 9.89% |
| 3 | 2-1 | 9.77% |
| 4 | 2-0 | 8.48% |
| 5 | 0-0 | 7.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 48.2% | 49.1% | 1.99 | -4.1% |
| Draw | 25.9% | 25.4% | 3.77 | -2.5% |
| Fulham win | 26.0% | 25.5% | 3.76 | -2.3% |

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
| Market best home last update utc | 2026-10-29T11:48:48Z |
| Market best draw last update utc | 2026-10-29T11:48:48Z |
| Market best away last update utc | 2026-10-29T11:48:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Aston Villa |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5969 |
| Dc lambda away | 1.1022 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:48:36.104635+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.4880 |
| Shot lambda away | 1.2702 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.7% |
| P btts no | 45.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.86 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.25 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.08 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.15288454385202935, "-10": 8.48320176013341e-08, "-11": 8.77046697350317e-09, "-12": 8.328689663742507e-10, "-13": 7.31070547963533e-11, "-14": 5.932381610769117e-12, "-15": 4.06935367211886e-13, "-2": 0.07364860784415336, "-3": 0.024854941758811963, "-4": 0.0065995244532306195, "-5": 0.0014383443797534078, "-6": 0.00026526743696126006, "-7": 4.2347725701467357e-05, "-8": 5.955049319018315e-06, "-9": 7.479038696308581e-07, "0": 0.2585089296690112, "1": 0.23084206743356314, "10": 1.9707462001072834e-06, "11": 2.7650831333288474e-07, "12": 3.563499724509258e-08, "13": 4.244963023042382e-09, "14": 4.67474878331094e-10, "15": 4.351802803794273e-11, "2": 0.14870269945418915, "3": 0.06810541353091643, "4": 0.02454121729030127, "5": 0.00725873452137365, "6": 0.001816755766494634, "7": 0.0003936019772066603, "8": 7.511507695586651e-05, "9": 1.2802715891553788e-05} |
| Raw goal margin distribution | {"-1": 0.15982930152355446, "-10": 8.868549938689658e-08, "-11": 9.168864131662238e-09, "-12": 8.707019153295154e-10, "-13": 7.642793188992644e-11, "-14": 6.201859163331121e-12, "-15": 4.254203457588009e-13, "-2": 0.07699408490439734, "-3": 0.025983973792435205, "-4": 0.006899306870211567, "-5": 0.0015036809593311016, "-6": 0.00027731717084165497, "-7": 4.42713648446207e-05, "-8": 6.225556548856997e-06, "-9": 7.818772917003204e-07, "0": 0.26906199773954625, "1": 0.22013171248572777, "10": 1.879309697437243e-06, "11": 2.6367918641183605e-07, "12": 3.3981644053001987e-08, "13": 4.048009923363941e-09, "14": 4.4578549592438375e-10, "15": 4.149892670126649e-11, "2": 0.1418033560608364, "3": 0.06494553387425396, "4": 0.023402581031523498, "5": 0.006921951784759183, "6": 0.0017324639416595262, "7": 0.0003753400679674946, "8": 7.162997068786432e-05, "9": 1.2208709638623759e-05} |
| Unadjusted home-win probability | 45.9% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 27.2% |
| Raw p over 1 5 | 76.3% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 55.0% |
| P home draw | 74.0% |
| P draw away | 51.8% |
| P home away | 74.1% |
| Raw p home draw | 72.8% |
| Raw p draw away | 54.1% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5148 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.53, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.53, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.99 |
| Reference draw odds | 3.77 |
| Reference away odds | 3.76 |
| Market reference 1x2 last update utc | 2026-10-29T11:48:48Z |
| Market reference home last update utc | 2026-10-29T11:48:48Z |
| Market reference draw last update utc | 2026-10-29T11:48:48Z |
| Market reference away last update utc | 2026-10-29T11:48:48Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-29T11:48:49Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:48:49Z |
| Home probability edge | -1.0% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | -0.0319 |
| Raw ev home | -0.0858 |
| Raw edge prob draw | 0.0151 |
| Raw ev draw | 0.0144 |
| Raw edge prob away | 0.0169 |
| Raw ev away | 0.0210 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08413419790326943, 0.06764460552482143, 0.04149258204741848, 0.014261502376061025, 0.003676388163611194, 0.0007581714505606545, 0.00013029634949297082, 1.9193327779778675e-05, 2.4738671007176625e-06, 2.834326827754766e-07, 2.9225772507261665e-08, 2.7396140586255423e-09, 2.35409623110026e-10, 1.867226195995054e-11, 1.3752604949479264e-12, 9.453873366563832e-14], [0.1060162760405543, 0.1273538216861269, 0.06430996669649792, 0.02210411349668158, 0.0056980883979464185, 0.0011751011465150495, 0.0002019482394947638, 2.974802264419045e-05, 3.834283214211612e-06, 4.3929650772659037e-07, 4.529745713278305e-08, 4.2461683553488984e-09, 3.6486485716747055e-10, 2.894041502214525e-11, 2.1315365847330535e-12, 1.465269817775669e-13], [0.09190959871282252, 0.0947713226615613, 0.04613618629839608, 0.0171297462423846, 0.0044157757486248585, 0.0009106533248646201, 0.0001565012818614487, 2.3053450172710813e-05, 2.971406136271426e-06, 3.4043607782107833e-07, 3.510359943755973e-08, 3.290599572812082e-09, 2.827547197032341e-10, 2.2427588672717756e-11, 1.651850041772445e-12, 1.135521682825709e-13], [0.04748401554086017, 0.04896249163431096, 0.025243500994319473, 0.00819262502615003, 0.002281358717796289, 0.00047047835303163916, 8.085455060350305e-05, 1.1910294480686551e-05, 1.5351421084295876e-06, 1.7588230431116343e-07, 1.813586268003876e-08, 1.7000496514229453e-09, 1.4608190757737243e-10, 1.158695048171041e-11, 8.534089382739349e-13, 5.866539511586104e-14], [0.01839904452414463, 0.018971922516063337, 0.009781318901728245, 0.0033619576289224194, 0.000818327206686699, 0.00018230033973488496, 3.13294160063913e-05, 4.614985399818531e-06, 5.948348656313658e-07, 6.815064630002922e-08, 7.027260460873851e-09, 6.587330257035947e-10, 5.66036273696192e-11, 4.48969648804447e-12, 3.306777843818532e-13, 2.2731590925254573e-14], [0.005703390255361276, 0.005880972670161806, 0.0030320421712926667, 0.0010421495722004103, 0.00026864956095938765, 5.23131506253917e-05, 9.711585062068254e-06, 1.4305668277186386e-06, 1.8438867147362297e-07, 2.1125538964487603e-08, 2.178330987885731e-09, 2.0419601217619175e-10, 1.754615987446204e-11, 1.3917294001783505e-12, 1.0250447791639321e-13, 7.046405806661477e-15], [0.0014732948207475016, 0.0015191677560135951, 0.0007832345021549872, 0.0002692071730009699, 6.939732142395444e-05, 1.4311619314251486e-05, 2.3223745902965966e-06, 3.695427813360366e-07, 4.763112158268282e-08, 5.457130890284412e-09, 5.627045701999825e-10, 5.2747736642023035e-11, 4.5325087903203754e-12, 3.5951033076113923e-13, 2.647886777091718e-14, 1.8202214323455714e-15], [0.0003262116337811057, 0.00033636865391635247, 0.00017342096298965937, 5.9606882813640046e-05, 1.536570500550244e-05, 3.1688272115057737e-06, 5.445821225896464e-07, 7.574606674846987e-08, 1.0546311418124757e-08, 1.2082982702496795e-09, 1.24592019598561e-10, 1.1679213899306043e-11, 1.003571774498916e-12, 7.960148281745448e-14, 5.862855549741403e-15, 4.0302687481625007e-16], [6.320002958751242e-05, 6.516784405699665e-05, 3.359846448454956e-05, 1.1548198676351533e-05, 2.976941685753541e-06, 6.139265212695154e-07, 1.055069859451758e-07, 1.5541726012911108e-08, 1.891489816204499e-09, 2.340949203594678e-10, 2.413837677622722e-11, 2.2627232984901003e-12, 1.9443134233552113e-13, 1.5421939465987158e-14, 1.1358658178929405e-15, 7.808216438424573e-17], [1.0883851194161107e-05, 1.1222733944744749e-05, 5.78608412351754e-06, 1.9887471062015618e-06, 5.126673283684451e-07, 1.0572597742844495e-07, 1.81696486926746e-08, 2.6764834499123425e-09, 3.449774019557647e-10, 3.732010729355665e-11, 4.156936359298186e-12, 3.8966981242036755e-13, 3.348355706907672e-14, 2.6558546786872056e-15, 1.9561058150079679e-16, 1.3446744623741038e-17], [1.6869041965771971e-06, 1.7394281353842481e-06, 8.967937373993788e-07, 3.082388558548048e-07, 7.945906758966924e-08, 1.6386625637343293e-08, 2.8161407284261023e-09, 4.1483212910414513e-10, 5.346855783876163e-11, 6.125930042070407e-12, 5.964400237004043e-13, 6.039550064815386e-14, 5.189666040864239e-15, 4.1163484533674274e-16, 3.031797338479079e-17, 2.0841308404013862e-18], [2.3768706980855638e-07, 2.4508776341948165e-07, 1.2635944358762389e-07, 4.343126930262383e-08, 1.1195889478151655e-08, 2.3088975886673326e-09, 3.967980157179615e-10, 5.845040484769274e-11, 7.533791702795722e-12, 8.631517809406842e-13, 8.900271253824804e-14, 7.877806399287842e-15, 7.312309241039604e-16, 5.799990326523044e-17, 4.271843220845856e-18, 2.936568381048426e-19], [3.06995587912312e-08, 3.165542916645811e-08, 1.6320530899598297e-08, 5.6095638959561855e-09, 1.446056226497646e-09, 2.9821621059705235e-10, 5.125025951806708e-11, 7.549428925344144e-12, 9.73061267014455e-13, 1.1148430945817712e-13, 1.1495551728361775e-14, 1.0775891422152139e-15, 8.743125385427469e-17, 7.491242336450252e-18, 5.517494166212269e-19, 3.792858977607771e-20], [3.660130791951427e-09, 3.77409368689966e-09, 1.9458024818153673e-09, 6.687958509316681e-10, 1.7240491817781124e-10, 3.5554593552566425e-11, 6.110271949939513e-12, 9.000747359012027e-13, 1.1601246552351643e-13, 1.3291629258980342e-14, 1.3705481286416871e-15, 1.2847471937026655e-16, 1.1039578794282522e-17, 8.268065285264745e-19, 6.578189096950204e-20, 4.522006334969499e-21], [4.052064897944932e-10, 4.1782311670037804e-10, 2.1541628928223324e-10, 7.404118446834423e-11, 1.9086638070901156e-11, 3.936185035022802e-12, 6.764572058379059e-13, 9.964565339829856e-14, 1.2843531173957189e-14, 1.4714923432585031e-15, 1.5173091560622012e-16, 1.422320485864462e-17, 1.2221718912006326e-18, 9.694044538663746e-20, 6.7417356742865445e-21, 5.00623179327568e-22], [4.186903550472088e-11, 4.317268194962411e-11, 2.2258459554355387e-11, 7.65050180437367e-12, 1.972177512412532e-12, 4.0671676080040997e-13, 6.98967353237995e-14, 1.0296151481039709e-14, 1.3270919303418098e-15, 1.5204584999628617e-16, 1.567799937237573e-17, 1.4696503738613197e-18, 1.2628415288092596e-19, 1.0016628686759345e-20, 7.377506675414457e-22, 4.788650023876673e-23]] |
| Legacy trial inputs | {"lambda_home": 1.549914792552638, "lambda_away": 1.0311362903202352, "rho": -0.10289506567663635, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4861 |
| Legacy p draw | 0.2667 |
| Legacy p away | 0.2472 |
| Legacy p over 1 5 | 0.7422 |
| Legacy p under 3 5 | 0.7394 |
| Legacy p btts yes | 0.5165 |
| Legacy p over 2 5 | 0.4814 |
| Legacy goal margin distribution | {"-1": 0.1515580694337029, "-10": 3.376662025698569e-08, "-11": 3.12778264499493e-09, "-12": 2.6606055356905954e-10, "-13": 2.0917350712966162e-11, "-14": 1.5217874767254934e-12, "-15": 9.453873366563832e-14, "-2": 0.06851575849254381, "-3": 0.020955903607566394, "-4": 0.005020517421453876, "-5": 0.0009847786650807747, "-6": 0.00016319889664747651, "-7": 2.338685957912825e-05, "-8": 2.9500252797719e-06, "-9": 3.321714154098365e-07, "0": 0.26668987132132593, "1": 0.22967657898067317, "10": 1.9490007801020405e-06, "11": 2.7136431481881065e-07, "12": 3.469671926921746e-08, "13": 4.10021236820616e-09, "14": 4.4837917174411733e-10, "15": 4.186903550472088e-11, "2": 0.15176823320751034, "3": 0.06977318562487139, "4": 0.025125944122515884, "5": 0.007408056631459833, "6": 0.0018453325063831135, "7": 0.00039748530113440815, "8": 7.536447083653258e-05, "9": 1.2755424748028884e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4808 |
| Legacy raw p draw | 0.2794 |
| Legacy raw p away | 0.2398 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5499 |
| Legacy lambda away | 1.0311 |
| Legacy model home team | Aston Villa |
| Legacy model away team | Fulham |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.733840632585078, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,530.3526 |
| Elo away rating | 1,453.3052 |
| Elo rating diff | 137.0473 |
| Elo home expectancy | 0.6876 |

</details>


---

## 2026-10-31 — Bournemouth vs Leeds United

The model's most likely 1X2 outcome is **Bournemouth win** at **47.0%**. Expected goals are 1.64 for Bournemouth and 1.19 for Leeds United (2.83 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.1%; Double Chance 1X: 74.1%; Double Chance X2: 53.0%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.0% | 2.13 |
| Draw | 27.1% | 3.69 |
| Leeds United win | 25.9% | 3.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.64 |
| Leeds United expected goals | 1.19 |
| Expected total goals | 2.83 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 76.3% |
| Under 1.5 | 23.7% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.90% |
| 2 | 1-0 | 9.64% |
| 3 | 2-1 | 9.47% |
| 4 | 2-0 | 8.29% |
| 5 | 0-0 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.0% | 47.0% | 2.08 | -2.3% |
| Draw | 27.1% | 27.5% | 3.50 | -5.2% |
| Leeds United win | 25.9% | 25.5% | 3.76 | -2.5% |
| Over 2.5 | 50.9% | 50.9% | 1.91 | -2.7% |
| Under 2.5 | 49.1% | 49.1% | 1.98 | -2.9% |

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
| Market best home last update utc | 2026-10-29T11:48:48Z |
| Market best draw last update utc | 2026-10-29T11:48:48Z |
| Market best away last update utc | 2026-10-29T11:48:48Z |
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
| Dc lambda away | 1.1734 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:48:36.104635+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7240 |
| Shot lambda away | 1.2381 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.18 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.22 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.19 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.15334415462969325, "-10": 7.878756482093627e-08, "-11": 8.074395569431564e-09, "-12": 7.60064214054762e-10, "-13": 6.613293409280746e-11, "-14": 5.319703012458641e-12, "-15": 3.61846979414485e-13, "-2": 0.07330379357072506, "-3": 0.02453151660358885, "-4": 0.006458214868037273, "-5": 0.001395453809521048, "-6": 0.00025513334301339937, "-7": 4.03765790368201e-05, "-8": 5.62847681696707e-06, "-9": 7.007291116539481e-07, "0": 0.27079937295933804, "1": 0.22411609322942389, "10": 2.0068619049568928e-06, "11": 2.8303019255794523e-07, "12": 3.6663672370594316e-08, "13": 4.390019028525296e-09, "14": 4.859582191779002e-10, "15": 4.5488270981267487e-11, "2": 0.1451719786610635, "3": 0.06685650616492962, "4": 0.02422114682278821, "5": 0.007202124275425552, "6": 0.0018120713681446807, "7": 0.0003946394814950078, "8": 7.570504584219615e-05, "9": 1.2970210930790195e-05} |
| Raw goal margin distribution | {"-1": 0.15640993969688746, "-10": 1.1268904581928489e-07, "-11": 1.2043621584672861e-08, "-12": 1.1824847933445626e-09, "-13": 1.0732303714659814e-10, "-14": 8.997436912920821e-12, "-15": 6.328884226106599e-13, "-2": 0.0767093693399217, "-3": 0.02653620415856843, "-4": 0.007245728697528048, "-5": 0.0016269991007364102, "-6": 0.00030950633903222707, "-7": 5.100485847432278e-05, "-8": 7.407889806089452e-06, "-9": 9.612789236359942e-07, "0": 0.2614447551261805, "1": 0.21852321896389962, "10": 2.7448020794349853e-06, "11": 4.036912787307299e-07, "12": 5.454447468592764e-08, "13": 6.812571707143525e-09, "14": 7.859589715653452e-10, "15": 7.608011317354711e-11, "2": 0.14526944547654547, "3": 0.06915563915679264, "4": 0.025985662985286883, "5": 0.008029749169374264, "6": 0.002102069872295317, "7": 0.0004767076041584317, "8": 9.527917312640702e-05, "9": 1.7014367913024367e-05} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 26.9% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.0% |
| P home draw | 74.1% |
| P draw away | 53.0% |
| P home away | 72.9% |
| Raw p home draw | 73.1% |
| Raw p draw away | 53.0% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9578 |
| Totals anchor target over 2 5 | 0.5094 |
| Totals anchor reference over odds | 1.91 |
| Totals anchor reference under odds | 1.98 |
| Totals anchor reference last update utc | 2026-10-29T11:48:48Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5355 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.57, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.14, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.65, "price": 1.57, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.76 |
| Market reference 1x2 last update utc | 2026-10-29T11:48:48Z |
| Market reference home last update utc | 2026-10-29T11:48:48Z |
| Market reference draw last update utc | 2026-10-29T11:48:48Z |
| Market reference away last update utc | 2026-10-29T11:48:48Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-29T11:48:48Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:48:48Z |
| Market best over 2 5 last update utc | 2026-10-29T11:48:48Z |
| Market best under 2 5 last update utc | 2026-10-29T11:48:48Z |
| Home probability edge | -0.0% |
| Draw probability edge | -0.4% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0003 |
| Raw ev home | -0.0231 |
| Raw edge prob draw | -0.0134 |
| Raw ev draw | -0.0849 |
| Raw edge prob away | 0.0137 |
| Raw ev away | 0.0111 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08573867301222843, 0.06892565650612673, 0.046425605216388555, 0.017742115824309672, 0.005085275772755558, 0.0011660403952291672, 0.00022280833660168084, 3.649240508720695e-05, 5.229757975801499e-06, 6.662054363269292e-07, 7.637957949501076e-08, 7.960744192169786e-09, 7.605740670846334e-10, 6.707601479971983e-11, 5.492983658153642e-12, 4.198422479567309e-13], [0.10017620869412647, 0.13403517962161238, 0.06719879700144671, 0.025680846466015896, 0.007360688412289018, 0.0016877865447154391, 0.00032250418948207883, 5.28209747642476e-05, 7.5698193474174355e-06, 9.64299844198694e-07, 1.1055571238367489e-07, 1.1522788565849897e-08, 1.1008938300397845e-09, 9.708925669753587e-11, 7.950825671653888e-12, 6.077011567555412e-13], [0.08219664683540621, 0.09423737752430093, 0.05041939507307703, 0.018585885746147807, 0.0053271185599289, 0.0012214943119370353, 0.00023340453463245318, 3.822789109648714e-05, 5.478471969226581e-06, 6.97888473147572e-07, 8.001199811174822e-08, 8.339336946907471e-09, 7.967450360655036e-10, 7.026597953251828e-11, 5.7542159958181264e-12, 4.3980887788129805e-13], [0.039658544454416945, 0.04546800106455573, 0.026064233436285278, 0.009296685437170576, 0.002570248013230232, 0.0005893511272762244, 0.00011261388960451381, 1.844433534477955e-05, 2.643273570136211e-06, 3.367198310652519e-07, 3.860448699757242e-08, 4.023594365005549e-09, 3.844165139109918e-10, 3.390219163688779e-11, 2.776315575590748e-12, 2.122006262594823e-13], [0.014350951730966604, 0.01645317793574001, 0.009431676353596395, 0.003604431078560038, 0.0009642311752400595, 0.00021326424598999306, 4.075077681704441e-05, 6.674318734691043e-06, 9.56502361309927e-07, 1.2184637910831015e-07, 1.3969527553833027e-08, 1.4559891017571833e-09, 1.391060340619402e-10, 1.226794181299736e-11, 1.0046453132194091e-12, 7.67875116604676e-14], [0.004154460400254975, 0.004763034359936266, 0.0027303782113967338, 0.0010434476027826071, 0.0002990747477423097, 6.400504028844356e-05, 1.1796951988956101e-05, 1.932150104171955e-06, 2.7689809409907466e-07, 3.527333701691953e-08, 4.044041825284648e-09, 4.214946283597882e-10, 4.0269838598915363e-11, 3.551449367971424e-12, 2.908350085984624e-13, 2.2229234855495048e-14], [0.001002229767338005, 0.0011490432832357413, 0.0006586815268199355, 0.00025172324379407453, 7.21493493662983e-05, 1.6543656550806632e-05, 2.950425749320552e-06, 4.66115491014793e-07, 6.679941212298486e-08, 8.509405541459155e-09, 9.755921845858595e-10, 1.016821494529887e-10, 9.714770892328868e-12, 8.567582624102647e-13, 7.016157934337135e-14, 5.362622032925706e-15], [0.00020723980832265662, 0.00023759772213181713, 0.0001362013360732694, 5.2051015140770474e-05, 1.4918951542409501e-05, 3.4208764539606355e-06, 6.536649978382844e-07, 9.99221165506885e-08, 1.3812698261001424e-08, 1.7595641546705384e-09, 2.017317225287213e-10, 2.1025706728351745e-11, 2.0088080829730246e-12, 1.7715939385072646e-13, 1.4507922961972245e-14, 1.1088762262192647e-15], [3.74961881088651e-05, 4.298888787535369e-05, 2.4643098058317086e-05, 9.41766290353369e-06, 2.6993067497451103e-06, 6.18943957018089e-07, 1.1826852146555306e-07, 1.937047266818217e-08, 2.590923951479521e-09, 3.18360401252744e-10, 3.649960244937823e-11, 3.8042104988856874e-12, 3.634564534845236e-13, 3.205369668522865e-14, 2.6249387743308505e-15, 2.006305251114266e-16], [6.030433520255904e-06, 6.9138129371813095e-06, 3.963297926241561e-06, 1.5146230302411145e-06, 4.341238596802157e-07, 9.954346225074681e-08, 1.902087898018503e-08, 3.1153126110381612e-09, 4.4645813110310394e-10, 5.308143585447383e-11, 5.870154732734166e-12, 6.118232190425194e-13, 5.845394134152537e-14, 5.1551290061140286e-15, 4.2216341371515795e-16, 3.226698778835177e-17], [8.728758108151573e-07, 1.000740668659318e-06, 5.73668025565653e-07, 2.1923428907063384e-07, 6.283730924812409e-08, 1.4408430178628588e-08, 2.753179370351708e-09, 4.5092629114784196e-10, 6.462263481931303e-11, 8.232111471620867e-12, 8.808778246534512e-13, 8.855842396793659e-14, 8.460922630593964e-15, 7.461797557263459e-16, 6.110609308689899e-17, 4.670488951368976e-18], [1.1485864739951515e-07, 1.316839327836941e-07, 7.54869509000228e-08, 2.8848266379075663e-08, 8.268539759080295e-09, 1.8959544771003944e-09, 3.622811568481087e-10, 5.933579924703502e-11, 8.503464450237707e-12, 1.0832344958550272e-12, 1.2419141420409415e-13, 1.2081012172644361e-14, 1.1133429487459623e-15, 9.818716064498422e-17, 8.040735134217568e-18, 6.145731580620235e-19], [1.3854357048740843e-08, 1.5883838645790886e-08, 9.105306339295264e-09, 3.479704764959539e-09, 9.973589685028065e-10, 2.2869179525109478e-10, 4.3698690630983086e-11, 7.157139380907435e-12, 1.0256958036001152e-12, 1.3066075400389644e-13, 1.4980084074878706e-14, 1.5613154469526182e-15, 1.392239159267462e-16, 1.1843426785673859e-17, 9.698809624348367e-19, 7.413038684625374e-20], [1.5425773417733416e-09, 1.7685446902501806e-09, 1.013806645771309e-09, 3.8743867417327485e-10, 1.1104833959557066e-10, 2.5463092972320153e-11, 4.865517020773183e-12, 7.968930641862521e-13, 1.1420343077770884e-13, 1.454808172449615e-14, 1.6679184887809525e-15, 1.7384060648622592e-16, 1.6608831273555912e-17, 1.3670995974093385e-18, 1.0798887249735458e-19, 8.253855064051241e-21], [1.5948609942063544e-10, 1.8284872120241567e-10, 1.0481683032820114e-10, 4.005704040587246e-11, 1.148121786157934e-11, 2.632613138652622e-12, 5.030427391185192e-13, 8.239027180077552e-14, 1.1807420750944477e-14, 1.5041170030574993e-15, 1.7244504163495034e-16, 1.7973270771326794e-17, 1.7171766005001445e-18, 1.5144003464433585e-19, 1.1574896041714683e-20, 8.533608744930034e-22], [1.538988950826723e-11, 1.7644306470944e-11, 1.0114482975116838e-11, 3.865374023905743e-12, 1.1079001552607298e-12, 2.540385994080826e-13, 4.854198705149611e-14, 7.950393069842553e-15, 1.1393776723787978e-15, 1.4514239528492644e-16, 1.6640385253958043e-17, 1.7343621311055708e-18, 1.6570195298449833e-19, 1.4613470445205048e-20, 1.1967251570341928e-21, 8.537045500986747e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4474511788965345, "lambda_away": 1.1464868842278388, "rho": -0.10289506567663635, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-29T11:48:48Z", "over": 1.91, "under": 1.98, "bookmaker": "pinnacle", "event_id": "a6c06eabdf4e6710354b6098d39449e7", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Bournemouth", "away_team": "Leeds United"}} |
| Legacy p home | 0.4486 |
| Legacy p draw | 0.2805 |
| Legacy p away | 0.2709 |
| Legacy p over 1 5 | 0.7452 |
| Legacy p under 3 5 | 0.7363 |
| Legacy p btts yes | 0.5329 |
| Legacy p over 2 5 | 0.4825 |
| Legacy goal margin distribution | {"-1": 0.15750612871743996, "-10": 8.873404216311112e-08, "-11": 9.13475710482934e-09, "-12": 8.636297404042468e-10, "-13": 7.546664934925501e-11, "-14": 6.100684814909183e-12, "-15": 4.198422479567309e-13, "-2": 0.07806567289262707, "-3": 0.02644387236996971, "-4": 0.007025903960133121, "-5": 0.0015295417435222413, "-6": 0.00028145890408298995, "-7": 4.480021452517671e-05, "-8": 6.278236141230833e-06, "-9": 7.854974663108662e-07, "0": 0.28052122235238125, "1": 0.22439854262785233, "10": 1.0140642238687806e-06, "11": 1.3179745763163847e-07, "12": 1.573158394334313e-08, "13": 1.7355405459508741e-09, "14": 1.7713040589157945e-10, "15": 1.538988950826723e-11, "2": 0.13821546353171635, "3": 0.05910938122128827, "4": 0.01982752029663116, "5": 0.005449571584311398, "6": 0.0012660499883296419, "7": 0.00025441973059392355, "8": 4.501354067104575e-05, "9": 7.110254574074926e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4272 |
| Legacy raw p draw | 0.2862 |
| Legacy raw p away | 0.2866 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4475 |
| Legacy lambda away | 1.1465 |
| Legacy model home team | Bournemouth |
| Legacy model away team | Leeds |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.998287458206503, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,502.9673 |
| Elo away rating | 1,455.9965 |
| Elo rating diff | 106.9708 |
| Elo home expectancy | 0.6493 |

</details>


---

## 2026-10-31 — Brentford vs Nottingham Forest

The model's most likely 1X2 outcome is **Brentford win** at **46.6%**. Expected goals are 1.58 for Brentford and 1.20 for Nottingham Forest (2.78 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 52.9%; Under 3.5 goals: 69.6%; Double Chance 1X: 72.3%; Double Chance X2: 53.4%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 46.6% | 2.15 |
| Draw | 25.8% | 3.88 |
| Nottingham Forest win | 27.7% | 3.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.58 |
| Nottingham Forest expected goals | 1.20 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 77.5% |
| Under 1.5 | 22.5% |
| Over 2.5 | 52.9% |
| Under 2.5 | 47.1% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.24% |
| 2 | 2-1 | 9.57% |
| 3 | 1-0 | 9.19% |
| 4 | 2-0 | 7.97% |
| 5 | 1-2 | 6.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 46.6% | 47.1% | 2.07 | -3.6% |
| Draw | 25.8% | 25.4% | 3.77 | -2.9% |
| Nottingham Forest win | 27.7% | 27.5% | 3.49 | -3.4% |

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
| Market best home last update utc | 2026-10-29T11:48:48Z |
| Market best draw last update utc | 2026-10-29T11:48:48Z |
| Market best away last update utc | 2026-10-29T11:48:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Brentford |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6216 |
| Dc lambda away | 1.1275 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:48:36.104635+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.4728 |
| Shot lambda away | 1.3686 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.55 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.44 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.66 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.15991561359288878, "-10": 1.2376107423762365e-07, "-11": 1.3310672960132087e-08, "-12": 1.3150687161755598e-09, "-13": 1.2010012128604305e-10, "-14": 1.0134974634236698e-11, "-15": 7.198755306119505e-13, "-2": 0.0793476566710688, "-3": 0.02772149835860505, "-4": 0.007634166126359347, "-5": 0.0017275292934734426, "-6": 0.0003310182107052737, "-7": 5.4928308792135925e-05, "-8": 8.031250273291408e-06, "-9": 1.0489896805291702e-06, "0": 0.2576413285794282, "1": 0.22297503355657622, "10": 1.9931821679348644e-06, "11": 2.8174687968182134e-07, "12": 3.658505629769499e-08, "13": 4.39131818523905e-09, "14": 4.870463640379627e-10, "15": 4.5467516209007286e-11, "2": 0.14352501297055614, "3": 0.0659031796803544, "4": 0.023853244181565373, "5": 0.007094265654675963, "6": 0.0017866113670928791, "7": 0.00038964635036631734, "8": 7.487791178151336e-05, "9": 1.285399004950824e-05} |
| Raw goal margin distribution | {"-1": 0.16253867079526724, "-10": 1.2579109725951282e-07, "-11": 1.3529004715188002e-08, "-12": 1.3366394708385074e-09, "-13": 1.2207009458050748e-10, "-14": 1.0301216176341127e-11, "-15": 7.316834751457148e-13, "-2": 0.0806491771270561, "-3": 0.028176207403560343, "-4": 0.007759387510262983, "-5": 0.001755865539408135, "-6": 0.0003364478224999004, "-7": 5.5829284580269286e-05, "-8": 8.162984932591731e-06, "-9": 1.0661960050081396e-06, "0": 0.2667657341838117, "1": 0.21643173559419446, "10": 1.9346913826210252e-06, "11": 2.7347889669590687e-07, "12": 3.5511452134448664e-08, "13": 4.26245307027382e-09, "14": 4.72753779659513e-10, "15": 4.4133252451224423e-11, "2": 0.13931320992722226, "3": 0.06396922261601999, "4": 0.023153260503752274, "5": 0.006886081387305698, "6": 0.0017341824904989409, "7": 0.0003782120111502431, "8": 7.268058735566878e-05, "9": 1.2476784200235067e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 28.1% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.3% |
| P home draw | 72.3% |
| P draw away | 53.4% |
| P home away | 74.2% |
| Raw p home draw | 71.9% |
| Raw p draw away | 54.8% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5285 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.07 |
| Reference draw odds | 3.77 |
| Reference away odds | 3.49 |
| Market reference 1x2 last update utc | 2026-10-29T11:48:48Z |
| Market reference home last update utc | 2026-10-29T11:48:48Z |
| Market reference draw last update utc | 2026-10-29T11:48:48Z |
| Market reference away last update utc | 2026-10-29T11:48:48Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-29T11:48:49Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:48:49Z |
| Home probability edge | -0.6% |
| Draw probability edge | +0.4% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -2.6% |
| Under 2.5 probability edge | +2.6% |
| Raw edge prob home | -0.0195 |
| Raw ev home | -0.0645 |
| Raw edge prob draw | 0.0130 |
| Raw ev draw | 0.0057 |
| Raw edge prob away | 0.0065 |
| Raw ev away | -0.0183 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.0782819421586541, 0.06601154715723766, 0.0424225751003169, 0.01518488544585782, 0.004076498399588587, 0.0008754936880412945, 0.0001566886419558643, 2.4036721080096957e-05, 3.2264206194950726e-06, 3.8495877404371545e-07, 4.1338048466473265e-08, 4.035459866063108e-09, 3.6111666749732136e-10, 2.982908482590762e-11, 2.28795585654783e-12, 1.637917901244937e-13], [0.09701721794689121, 0.12598948139268487, 0.06783578681114946, 0.024281379652722746, 0.006518521700216581, 0.001399957523465675, 0.0002505528550851016, 3.843590076681459e-05, 5.159205465241302e-06, 6.15568038134391e-07, 6.610157531289742e-08, 6.452899064044839e-09, 5.774433355913383e-10, 4.769817565852684e-11, 3.658554091803354e-12, 2.619111388223741e-13], [0.08720286130261755, 0.09364109483924636, 0.049038557903353715, 0.01941356093669074, 0.005211718611306559, 0.0011193005125444738, 0.0002003231772503929, 3.073044910812891e-05, 4.124911809660651e-06, 4.921618042268506e-07, 5.28498371468892e-08, 5.159251697796413e-09, 4.6168016576155987e-10, 3.813586595817489e-11, 2.9251040845794495e-12, 2.0940440478455558e-13], [0.046480556595619525, 0.0499122407606219, 0.02679864399451993, 0.009356055034830299, 0.0027779315753485114, 0.0005966055476125499, 0.00010677554197779196, 1.6379833845386863e-05, 2.19864570906134e-06, 2.6233032097631055e-07, 2.8169830781705358e-08, 2.749965849151261e-09, 2.4608310728802947e-10, 2.0327042593712472e-11, 1.559128495561095e-12, 1.1161598533084369e-13], [0.018581174767373202, 0.01995303276320335, 0.010713087881519034, 0.003834680282080731, 0.0010040847524075047, 0.000238500413061274, 4.2684837525317545e-05, 6.548040248088413e-06, 8.789356919072284e-07, 1.048697756192815e-07, 1.1261236681738143e-08, 1.099332705757724e-09, 9.837475191181454e-11, 8.125985543236937e-12, 6.232808120792303e-13, 4.461986435120328e-14], [0.005942442707636686, 0.006381176406947691, 0.0034261510240777716, 0.0012263685242539838, 0.00032922799083682933, 6.896487453408161e-05, 1.3651031468923562e-05, 2.0941277668777537e-06, 2.810922914318021e-07, 3.3538387167777196e-08, 3.601454409431073e-09, 3.5157742728233415e-10, 3.1461214612781605e-11, 2.598770214387038e-12, 1.9933134276599335e-13, 1.4269872107070775e-14], [0.0015837097571260673, 0.0017006358891165237, 0.000913097369747696, 0.0003268372777405791, 8.774196185976523e-05, 1.8843999495335782e-05, 3.2894480853346285e-06, 5.581022384634639e-07, 7.491340287073848e-08, 8.93825546313165e-09, 9.598171608336865e-10, 9.369827011655808e-11, 8.384671927803077e-12, 6.925935928274468e-13, 5.312343895783079e-14, 3.803038043575327e-15], [0.0003617756994480807, 0.00038848579136629237, 0.0002085839517741759, 7.466127188284555e-05, 2.00433883039066e-05, 4.304640460254302e-06, 7.704090583845526e-07, 1.1527218985490919e-07, 1.7112888646199007e-08, 2.0418158109274527e-09, 2.192564156029486e-10, 2.14040211951505e-11, 1.9153576200908518e-12, 1.5821303768002437e-13, 1.2135285016449379e-14, 8.687493033691044e-16], [7.231214501707365e-05, 7.76509890664548e-05, 4.1692001402911045e-05, 1.4923381332101612e-05, 4.0062956242687495e-06, 8.604165113443279e-07, 1.5399025317997074e-07, 2.3622776472739345e-08, 3.0927310650443663e-09, 4.081205046198221e-10, 4.382522581033546e-11, 4.278260499457249e-12, 3.828438952501941e-13, 3.162380486517876e-14, 2.4256147974331952e-15, 1.7364661502844801e-16], [1.2847853456523551e-05, 1.3796417296767623e-05, 7.407507054413917e-06, 2.651469077364397e-06, 7.118071116817692e-07, 1.528720417118739e-07, 2.735977761580841e-08, 4.197109217079751e-09, 5.633730022965473e-10, 6.556238213274188e-11, 7.786521597130043e-12, 7.601276926978423e-13, 6.802069364334007e-14, 5.618669043071284e-15, 4.3096416863361757e-16, 3.085216546376962e-17], [2.054435040769392e-06, 2.2061150703088568e-06, 1.1844968584699488e-06, 4.2398296341775534e-07, 1.1382146266350497e-07, 2.4444992333514335e-08, 4.374963182120867e-09, 6.711384337222981e-10, 9.008611756493847e-11, 1.0748580382425152e-11, 1.1257768448078706e-12, 1.2154816153703173e-13, 1.0876843901683983e-14, 8.984528507920342e-16, 6.891329297559773e-17, 4.933413198311365e-18], [2.986493460861179e-07, 3.20698785828598e-07, 1.7218807370547525e-07, 6.163360352778382e-08, 1.6546011297729264e-08, 3.553522418869068e-09, 6.359801442064191e-10, 9.756212797527158e-11, 1.309564895862092e-11, 1.562500852479215e-12, 1.677861119782056e-13, 1.5975870387688655e-14, 1.5811462782985727e-15, 1.3060639594511682e-16, 1.0017795391620516e-17, 7.171609695172131e-19], [3.979625102216663e-08, 4.2734429358699274e-08, 2.2944767480691108e-08, 8.212930614236466e-09, 2.2048239102126277e-09, 4.735214459616847e-10, 8.474696427647343e-11, 1.3000553947441332e-11, 1.745048968247776e-12, 2.0820965109256128e-13, 2.235818801489218e-14, 2.1826277185089422e-15, 1.9050203677368558e-16, 1.7403838268018752e-17, 1.3349123489414043e-18, 9.556464241504676e-20], [4.8950896360812e-09, 5.2564967021917254e-09, 2.822293321912741e-09, 1.0102215786409055e-09, 2.712016935025923e-10, 5.824493169716246e-11, 1.0424197653393017e-11, 1.5991173856046783e-12, 2.1464763387299638e-13, 2.5610575846141365e-14, 2.7501418254772855e-15, 2.6847147783708493e-16, 2.4024405795711844e-17, 1.935577235662257e-18, 1.641992759755218e-19, 1.1754813045106603e-20], [5.591063858089719e-10, 6.003855070429285e-10, 3.2235614385412547e-10, 1.1538528968640555e-10, 3.097606171741033e-11, 6.652608159175849e-12, 1.1906289584541239e-12, 1.8264767520487804e-13, 2.4516581251667136e-14, 2.9251837176337924e-15, 3.141151584173335e-16, 3.0664222481215483e-17, 2.744014858612847e-18, 2.266620717021339e-19, 1.6957117181969528e-20, 1.3426089257011285e-21], [5.960257638423663e-11, 6.40030662353071e-11, 3.436422329391534e-11, 1.230045071332988e-11, 3.3021498796216236e-12, 7.09189871598336e-13, 1.2692495604189406e-13, 1.9470841845332575e-14, 2.6135480542196773e-15, 3.1183418825726403e-16, 3.348570718956593e-17, 3.2689067932132782e-18, 2.9252099307238506e-19, 2.416292101992116e-20, 1.8533487360234206e-21, 1.2940977742391895e-22]] |
| Legacy trial inputs | {"lambda_home": 1.5990492479708691, "lambda_away": 1.0738305307928646, "rho": -0.10289506567663635, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4774 |
| Legacy p draw | 0.2637 |
| Legacy p away | 0.2589 |
| Legacy p over 1 5 | 0.7587 |
| Legacy p under 3 5 | 0.7201 |
| Legacy p btts yes | 0.5357 |
| Legacy p over 2 5 | 0.5031 |
| Legacy goal margin distribution | {"-1": 0.15629155355611385, "-10": 4.827359228955756e-08, "-11": 4.652642815972534e-09, "-12": 4.118515632257585e-10, "-13": 3.369704332249553e-11, "-14": 2.549866995370204e-12, "-15": 1.637917901244937e-13, "-2": 0.07255713487706597, "-3": 0.022936321494995256, "-4": 0.00569407238983883, "-5": 0.0011590842048193025, "-6": 0.00019952340621276628, "-7": 2.971738967916971e-05, "-8": 3.897689488139819e-06, "-9": 4.564740132816214e-07, "0": 0.26374249399617516, "1": 0.22164050365919682, "10": 2.3991205009089115e-06, "11": 3.4432475620629593e-07, "12": 4.538740431892581e-08, "13": 5.529839366418044e-09, "14": 6.231094520442789e-10, "15": 5.960257638423663e-11, "2": 0.14914676335036614, "3": 0.07020750950967916, "4": 0.025954273457913703, "5": 0.007867322831161807, "6": 0.0020166564803286275, "7": 0.0004472752086745697, "8": 8.73569570547807e-05, "9": 1.5234647512378737e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4833 |
| Legacy raw p draw | 0.2738 |
| Legacy raw p away | 0.2429 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5990 |
| Legacy lambda away | 1.0738 |
| Legacy model home team | Brentford |
| Legacy model away team | Nott'm Forest |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.859049559640097, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,503.9116 |
| Elo away rating | 1,478.7386 |
| Elo rating diff | 85.1730 |
| Elo home expectancy | 0.6202 |

</details>


---

## 2026-10-31 — Chelsea vs Manchester United

The model's most likely 1X2 outcome is **Chelsea win** at **50.8%**. Expected goals are 1.74 for Chelsea and 1.38 for Manchester United (3.11 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 60.6%; Under 3.5 goals: 61.9%; Double Chance 1X: 74.9%; Double Chance X2: 49.2%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 79.3%; BTTS Yes (both teams score): 62.1%; BTTS No (at least one team does not score): 37.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 50.8% | 1.97 |
| Draw | 24.1% | 4.15 |
| Manchester United win | 25.1% | 3.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.74 |
| Manchester United expected goals | 1.38 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 60.6% |
| Under 2.5 | 39.4% |
| Over 3.5 | 38.1% |
| Under 3.5 | 61.9% |
| Over 4.5 | 20.7% |
| Under 4.5 | 79.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.03% |
| 2 | 2-1 | 10.36% |
| 3 | 1-0 | 7.77% |
| 4 | 2-0 | 7.53% |
| 5 | 1-2 | 6.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 50.8% | 53.2% | 1.84 | -6.5% |
| Draw | 24.1% | 23.7% | 4.01 | -3.3% |
| Manchester United win | 25.1% | 23.1% | 4.12 | +3.4% |

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
| Market best home last update utc | 2026-10-29T11:48:48Z |
| Market best draw last update utc | 2026-10-29T11:48:48Z |
| Market best away last update utc | 2026-10-29T11:48:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
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
| Bbs statistics cutoff utc | 2026-10-29T11:48:36.104635+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6583 |
| Shot lambda away | 1.4548 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 62.1% |
| P btts no | 37.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.74 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.78 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.84 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.1365856094899596, "-10": 3.144874294618662e-07, "-11": 3.868577265050312e-08, "-12": 4.373906090891004e-09, "-13": 4.5743913565106197e-10, "-14": 4.447875313908291e-11, "-15": 4.007718845928214e-12, "-16": 3.001389004012634e-13, "-2": 0.07380030752671791, "-3": 0.02873007354588629, "-4": 0.008902898942488904, "-5": 0.0022800731138211184, "-6": 0.000496256433881072, "-7": 9.376300237277379e-05, "-8": 1.5636170978995506e-05, "-9": 2.332158894390558e-06, "0": 0.24117868767713713, "1": 0.23188148611531176, "10": 4.238258759575741e-06, "11": 6.570487623430841e-07, "12": 9.36220032349916e-08, "13": 1.2339681246774479e-08, "14": 1.512116933950651e-09, "15": 1.7170864785897637e-10, "16": 1.620613145828672e-11, "2": 0.15629502661159714, "3": 0.07668066556372628, "4": 0.029946269487946865, "5": 0.009665452861324718, "6": 0.002651195370770411, "7": 0.0006312904748408612, "8": 0.00013267536488553163, "9": 2.493906488642719e-05} |
| Raw goal margin distribution | {"-1": 0.1621170456251827, "-10": 3.7327338612757445e-07, "-11": 4.591715915934823e-08, "-12": 5.191503965499134e-09, "-13": 5.429465190513995e-10, "-14": 5.2792999781796235e-11, "-15": 4.75686671110114e-12, "-16": 3.562427402999626e-13, "-2": 0.08759552245026907, "-3": 0.034100478529516566, "-4": 0.010567084478705368, "-5": 0.002706278636544524, "-6": 0.0005890197893739472, "-7": 0.0001112897690348446, "-8": 1.8558981824445507e-05, "-9": 2.7681006168873343e-06, "0": 0.2500741164442431, "1": 0.20640828297798317, "10": 3.7726673570885805e-06, "11": 5.848690602258892e-07, "12": 8.333721359317165e-08, "13": 1.0984112881593927e-08, "14": 1.3460042249491026e-09, "15": 1.5284569618213314e-10, "16": 1.4425816498161369e-11, "2": 0.1391253291556669, "3": 0.0682569565245363, "4": 0.026656539813313375, "5": 0.008603660269447156, "6": 0.00235994987563504, "7": 0.0005619404341209869, "8": 0.00011810039136061785, "9": 2.2199398703715814e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 29.8% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 62.4% |
| P home draw | 74.9% |
| P draw away | 49.2% |
| P home away | 75.9% |
| Raw p home draw | 70.2% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6058 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.84 |
| Reference draw odds | 4.01 |
| Reference away odds | 4.12 |
| Market reference 1x2 last update utc | 2026-10-29T11:48:48Z |
| Market reference home last update utc | 2026-10-29T11:48:48Z |
| Market reference draw last update utc | 2026-10-29T11:48:48Z |
| Market reference away last update utc | 2026-10-29T11:48:48Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-29T11:48:49Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:48:49Z |
| Home probability edge | -2.4% |
| Draw probability edge | +0.4% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | -0.0797 |
| Raw ev home | -0.1681 |
| Raw edge prob draw | 0.0127 |
| Raw ev draw | 0.0028 |
| Raw edge prob away | 0.0670 |
| Raw ev away | 0.2270 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.04534318557129248, 0.038216173380041754, 0.03500081445829871, 0.017329105528042937, 0.006434805226314825, 0.0019115455547824738, 0.00047320862604431223, 0.00010040928244201144, 1.864245602240685e-05, 3.0766625740389628e-06, 4.5698202666018303e-07, 6.170575706185621e-08, 7.63771923855301e-09, 8.726489856365684e-10, 9.258290492712997e-11, 9.16766626380377e-12, 8.510558535749324e-13], [0.06115783435555263, 0.10658260440801626, 0.06433002345034307, 0.031850166410289246, 0.011826901102556337, 0.003513340254183697, 0.0008697375327252573, 0.00018454803392711351, 3.4264049327260005e-05, 5.6547762844927745e-06, 8.399137261922965e-07, 1.1341258368544063e-07, 1.4037806414723465e-08, 1.6038920973339896e-09, 1.7016348154295641e-10, 1.6849784636813903e-11, 1.5642048296692208e-12], [0.06634191896684967, 0.098538802525222, 0.06595488286350625, 0.029269632489729632, 0.010868673158717678, 0.0032286857382983506, 0.0007992704847271561, 0.0001695957584700014, 3.14879400785448e-05, 5.196620373238395e-06, 7.718630343101135e-07, 1.0422377708868638e-07, 1.290044860136709e-08, 1.4739430757567964e-09, 1.5637665762167657e-10, 1.5484597395739524e-11, 1.4374713121840306e-12], [0.040644551361921286, 0.060370056862236565, 0.04483434609840648, 0.02000595345456537, 0.0066587212325916415, 0.001978062820090319, 0.0004896751672919428, 0.00010390328804541212, 1.929116941044504e-05, 3.183723156606851e-06, 4.72883920618306e-07, 6.385297149953253e-08, 7.903493808071693e-09, 9.030151068901188e-10, 9.580457109909297e-11, 9.486679372122086e-12, 8.80670584891383e-13], [0.018675743569883774, 0.027739405737781452, 0.020600910154016727, 0.010199629681704257, 0.0034134542112776215, 0.000908899046865545, 0.00022500058557546276, 4.774246728238853e-05, 8.864089305957762e-06, 1.462887282008366e-06, 2.172851844555651e-07, 2.9339768356198102e-08, 3.6315722211168684e-09, 4.1492593744830683e-10, 4.402119208395615e-11, 4.359029324886197e-12, 4.046588647643412e-13], [0.006865046087625327, 0.01019677198504141, 0.007572721114163034, 0.003749297990711635, 0.001392224328405228, 0.00037274247361058485, 8.270832076582485e-05, 1.754972898423563e-05, 3.258364593758745e-06, 5.377450474412828e-07, 7.987220427737473e-08, 1.0785051808612118e-08, 1.3349353708577575e-09, 1.5252328095397472e-10, 1.618181955421049e-11, 1.6023424770572756e-12, 1.4874919148349795e-13], [0.0021029442821051863, 0.003123539604566671, 0.002319723766416105, 0.0011485086437639388, 0.0004264749505622397, 0.00012669012771971653, 2.8265794183219664e-05, 5.3759438390981135e-06, 9.981228245226765e-07, 1.6472545971475e-07, 2.4466958144245128e-08, 3.3037451961191957e-09, 4.0892583520824593e-10, 4.672189486801148e-11, 4.956917181797961e-12, 4.908396691139247e-13, 4.5565791941565156e-14], [0.0005521604367389475, 0.0008201334704419264, 0.000609079231854782, 0.00030155864790878603, 0.00011197757209474595, 3.326444587595248e-05, 8.234709703727738e-06, 1.5747801156382733e-06, 2.620725329706983e-07, 4.3251208580318824e-08, 6.4241770024814206e-09, 8.674492262520778e-10, 1.0736978135074058e-10, 1.2267553684193154e-11, 1.3015150136267154e-12, 1.2887752108935286e-13, 1.1964001040305345e-14], [0.000126855954616744, 0.00018842134891175054, 0.00013993274826153707, 6.928151241572883e-05, 2.5726257910905297e-05, 7.642331387074758e-06, 1.8918812195739182e-06, 4.01434854032323e-07, 6.717300214870587e-08, 9.936737563430796e-09, 1.4759208593244545e-09, 1.9929189481170475e-10, 2.46676422357997e-11, 2.818405901392441e-12, 2.990162252057557e-13, 2.960893225705502e-14, 2.748666278893863e-15], [2.5906211554126694e-05, 3.847894520181584e-05, 2.8576722241899756e-05, 1.4148500343198108e-05, 5.2537532191489976e-06, 1.5606981499484835e-06, 3.8635533710367906e-07, 8.198004015799393e-08, 1.5220796884423326e-08, 2.2639381077980452e-09, 3.0140893373373414e-10, 4.069890139262982e-11, 5.037565325433993e-12, 5.755679325220608e-13, 6.106435927032341e-14, 6.046663440123827e-15, 5.61325878062643e-16], [4.761452619258623e-06, 7.0722681328644505e-06, 5.2522812408997415e-06, 2.600434798308862e-06, 9.656177235328188e-07, 2.8684974946715253e-07, 7.101048441503298e-08, 1.5067586247477702e-08, 2.7975183882491086e-09, 4.61689174160681e-10, 6.180439506218364e-11, 7.48028673478569e-12, 9.258832988126844e-13, 1.057869628734614e-13, 1.1223372154726175e-14, 1.1113512840192473e-15, 1.0316933322245141e-16], [7.955772234945804e-07, 1.181684644344854e-06, 8.775883455705391e-07, 4.34499061977305e-07, 1.613422476027941e-07, 4.792888756640124e-08, 1.1864934621299143e-08, 2.5175990165370843e-09, 4.674291838999336e-10, 7.714229682988044e-11, 1.1458079102987695e-11, 1.3944045773420248e-12, 1.5470313852752185e-13, 1.767563492375925e-14, 1.8752805017922714e-15, 1.8569244295133562e-16, 1.7238262824021368e-17], [1.2185312026796436e-07, 1.80990552310779e-07, 1.3441420274558582e-07, 6.654924863594831e-08, 2.471168821939116e-08, 7.34093979624621e-09, 1.81727086030706e-09, 3.8560341685132715e-10, 7.159293011472574e-11, 1.1815357825439885e-11, 1.7549555841271766e-12, 2.3696963252567e-13, 2.6435109748497735e-14, 2.7072560709025114e-15, 2.872238844613163e-16, 2.844124104560335e-17, 2.6402667787290713e-18], [1.7227761928610783e-08, 2.5588693499854735e-08, 1.9003665065224996e-08, 9.408824406849931e-09, 3.493772507109544e-09, 1.0378721764685346e-09, 2.569282565134493e-10, 5.451714202939469e-11, 1.0121907039194844e-11, 1.6704715584664542e-12, 2.481180369623878e-13, 3.350309294078798e-14, 4.14689373713339e-15, 4.270209902025966e-16, 4.060810827682411e-17, 4.021061821071028e-18, 3.732845526806172e-19], [2.261707224362049e-09, 3.3593529554465187e-09, 2.4948525957975055e-09, 1.2352159393604088e-09, 4.586719129479146e-10, 1.3625466901680913e-10, 3.3730237061969454e-11, 7.157157992454142e-12, 1.3288313577661616e-12, 2.1930402843566406e-13, 3.2573607588598373e-14, 4.398376739628165e-15, 5.444154361316177e-16, 6.2202283596268e-17, 5.947685035597093e-18, 5.278958815433387e-19, 4.900580661835204e-20], [2.771281774111651e-10, 4.116232869558527e-10, 3.056956025676117e-10, 1.513516596210747e-10, 5.620131106969509e-11, 1.6695356358089494e-11, 4.13298371245499e-12, 8.769703383920678e-13, 1.628224061442847e-13, 2.6871438108636976e-14, 3.991261293901998e-15, 5.389354184711644e-16, 6.670751012532842e-17, 7.62167857013784e-18, 8.086150950252657e-19, 7.216394287641632e-20, 6.0047072956309026e-21], [3.1834370191677384e-11, 4.7284142012835003e-11, 3.5115977989011095e-11, 1.738612365769459e-11, 6.45597773046303e-12, 1.9178351322855514e-12, 4.747656291307332e-13, 1.0073966011068242e-13, 1.870379548235709e-14, 3.0867857477513664e-15, 4.584856392039708e-16, 6.190878813294716e-17, 7.662849702735483e-18, 8.755202713427402e-19, 9.28875313874005e-20, 9.19783072802189e-21, 7.695469103526077e-22]] |
| Legacy trial inputs | {"lambda_home": 1.8379579002936712, "lambda_away": 1.48531733871703, "rho": -0.10289506567663635, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4913 |
| Legacy p draw | 0.2417 |
| Legacy p away | 0.2670 |
| Legacy p over 1 5 | 0.8553 |
| Legacy p under 3 5 | 0.5735 |
| Legacy p btts yes | 0.6587 |
| Legacy p over 2 5 | 0.6474 |
| Legacy goal margin distribution | {"-1": 0.13947180618249377, "-10": 5.842437431542337e-07, "-11": 7.731781890195192e-08, "-12": 9.407879331745564e-09, "-13": 1.0591777351601558e-09, "-14": 1.108701608761279e-10, "-15": 1.073187109347299e-11, "-16": 8.510558535749324e-13, "-2": 0.07994131005355237, "-3": 0.03292553972213959, "-4": 0.010860746447286483, "-5": 0.0029717161888700404, "-6": 0.0006926568149413965, "-7": 0.00014037355882043533, "-8": 2.513673749675471e-05, "-9": 4.02913518168869e-06, "0": 0.24170273305673332, "1": 0.21625817895575336, "10": 6.087436132790848e-06, "11": 9.968647759561468e-07, "12": 1.5009447400096815e-07, "13": 2.0910196610282606e-08, "14": 2.7084464893069128e-09, "15": 3.244123194240001e-10, "16": 3.1834370191677384e-11, "2": 0.15152390010796218, "3": 0.07722520866353201, "4": 0.03152115852669088, "5": 0.010672499300314428, "6": 0.0030781744209071103, "7": 0.0007719278901296295, "8": 0.00017104746430774394, "9": 3.392625154209713e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4507 |
| Legacy raw p draw | 0.2460 |
| Legacy raw p away | 0.3033 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8380 |
| Legacy lambda away | 1.4853 |
| Legacy model home team | Chelsea |
| Legacy model away team | Man United |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.967201976495664, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,487.8075 |
| Elo away rating | 1,504.9896 |
| Elo rating diff | 42.8180 |
| Elo home expectancy | 0.5613 |

</details>


---

## 2026-10-31 — Coventry City vs Sunderland

The model's most likely 1X2 outcome is **Sunderland win** at **40.0%**. Expected goals are 1.03 for Coventry City and 1.17 for Sunderland (2.20 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 47.7%; Under 3.5 goals: 73.7%; Double Chance 1X: 60.0%; Double Chance X2: 69.3%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 30.7% | 3.25 |
| Draw | 29.3% | 3.42 |
| Sunderland win | 40.0% | 2.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.03 |
| Sunderland expected goals | 1.17 |
| Expected total goals | 2.20 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 47.7% |
| Under 2.5 | 52.3% |
| Over 3.5 | 26.3% |
| Under 3.5 | 73.7% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.97% |
| 2 | 0-1 | 9.41% |
| 3 | 0-0 | 8.72% |
| 4 | 1-2 | 8.71% |
| 5 | 1-0 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 30.7% | 30.6% | 3.16 | -2.9% |
| Draw | 29.3% | 28.5% | 3.38 | -1.0% |
| Sunderland win | 40.0% | 40.9% | 2.38 | -4.8% |
| Over 2.5 | 47.7% | 47.7% | 2.03 | -3.1% |
| Under 2.5 | 52.3% | 52.3% | 1.86 | -2.8% |

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
| Market best home last update utc | 2026-10-29T11:48:48Z |
| Market best draw last update utc | 2026-10-29T11:48:48Z |
| Market best away last update utc | 2026-10-29T11:48:48Z |
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
| Dc lambda home | 0.8795 |
| Dc lambda away | 1.1502 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:48:36.104635+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.3943 |
| Shot lambda away | 1.2078 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.47 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.80 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.26 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.20925230672405035, "-10": 5.931416658816612e-07, "-11": 7.334515897558321e-08, "-12": 8.32750687880412e-09, "-13": 8.691187772075825e-10, "-14": 7.634376119914637e-11, "-2": 0.12077223277748547, "-3": 0.04908361914241486, "-4": 0.015653593380600093, "-5": 0.004091526232099382, "-6": 0.0009041080226782018, "-7": 0.00017282724824108526, "-8": 2.9088942331541364e-05, "-9": 4.371351569120397e-06, "0": 0.2927722151550794, "1": 0.1739391094299137, "10": 1.6626758913965605e-07, "11": 1.8208795512084312e-08, "12": 1.830987426839848e-09, "13": 1.6924275733985644e-10, "14": 1.3166341315512229e-11, "2": 0.08943993659156438, "3": 0.032193008356789, "4": 0.009092841703235018, "5": 0.0021049002494789295, "6": 0.00041193348887590874, "7": 6.973962210636007e-05, "8": 1.0395751815171978e-05, "9": 1.38358009665973e-06} |
| Raw goal margin distribution | {"-1": 0.21437440036428068, "-10": 1.5996206798545903e-07, "-11": 1.6822416079598555e-08, "-12": 1.618243519679984e-09, "-13": 1.3297760093762037e-10, "-2": 0.11070844822298552, "-3": 0.0393421185069792, "-4": 0.010852215317765203, "-5": 0.0024384633028865722, "-6": 0.00046147803007856, "-7": 7.536680788764975e-05, "-8": 1.0819396778965513e-05, "-9": 1.3850837657543878e-06, "0": 0.31060182781144463, "1": 0.18870199515974345, "10": 4.749227618874214e-08, "11": 4.4233870548824065e-09, "12": 3.768521923992232e-10, "13": 2.7426239277991522e-11, "2": 0.08683642956134777, "3": 0.02732999389337263, "4": 0.006676683535820811, "5": 0.0013286763706125187, "6": 0.00022269712732674932, "7": 3.221100711027181e-05, "8": 4.095319862234189e-06, "9": 4.6432430384500654e-07} |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 31.1% |
| Unadjusted away-win probability | 37.8% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.9% |
| Raw p btts yes | 45.4% |
| P home draw | 60.0% |
| P draw away | 69.3% |
| P home away | 70.7% |
| Raw p home draw | 62.2% |
| Raw p draw away | 68.9% |
| Raw p home away | 68.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1798 |
| Totals anchor target over 2 5 | 0.4772 |
| Totals anchor reference over odds | 2.03 |
| Totals anchor reference under odds | 1.86 |
| Totals anchor reference last update utc | 2026-10-29T11:48:48Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3837 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.22, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.16 |
| Reference draw odds | 3.38 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-29T11:48:48Z |
| Market reference home last update utc | 2026-10-29T11:48:48Z |
| Market reference draw last update utc | 2026-10-29T11:48:48Z |
| Market reference away last update utc | 2026-10-29T11:48:48Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-10-29T11:48:48Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:48:48Z |
| Market best over 2 5 last update utc | 2026-10-29T11:48:48Z |
| Market best under 2 5 last update utc | 2026-10-29T11:48:48Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0055 |
| Raw ev home | -0.0168 |
| Raw edge prob draw | 0.0255 |
| Raw ev draw | 0.0498 |
| Raw edge prob away | -0.0310 |
| Raw ev away | -0.0997 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.12782153568997626, 0.13113654197866445, 0.08514862564351694, 0.03334219178433458, 0.009792011420456713, 0.002300592313272085, 0.000450428821058277, 7.559026864622221e-05, 1.1099761807005194e-05, 1.4488015675830137e-06, 1.7019494804074524e-07, 1.8175724736106937e-08, 1.7792961876675188e-09, 1.6078393500953245e-10], [0.10520095764931654, 0.13807700086769764, 0.07895096080475342, 0.03091533253549344, 0.009079285825384748, 0.0021331404022102455, 0.00041764371330649805, 7.00883225302305e-05, 1.0291849724455167e-05, 1.3433484675958575e-06, 1.5780706465172398e-07, 1.6852778543321367e-08, 1.6497875627576982e-09, 1.4908104570138905e-10], [0.05547767720833145, 0.06517124636774797, 0.03409138887929131, 0.014332557858856634, 0.00420921849247535, 0.0009889383593284088, 0.00019362245832163665, 3.2493421726628054e-05, 4.77137134077594e-06, 6.227854613667579e-07, 7.316042556102051e-08, 7.813062443282428e-09, 7.648527044274722e-10, 6.911498398798979e-11], [0.017146551635298282, 0.02014255457713214, 0.011831023331172823, 0.004125909709189221, 0.0013009481625276514, 0.000305652354165347, 5.9843123332257163e-05, 1.0042780474584829e-05, 1.4746934115242788e-06, 1.9248504278464088e-07, 2.261177968629958e-08, 2.414792495916414e-09, 2.363939344579063e-10, 2.1361450250929195e-11], [0.003974628820677228, 0.004669112463378454, 0.0027424713324502924, 0.0010738870350347142, 0.0002808777073037176, 7.085125229917975e-05, 1.3871838943177306e-05, 2.3279505735629514e-06, 3.418389341353568e-07, 4.461868572023311e-08, 5.241487217928689e-09, 5.597570901933432e-10, 5.479691572475955e-11, 4.95165661438426e-12], [0.0007370659522996619, 0.0008658528832455559, 0.0005085713246457511, 0.00019914452540130672, 5.848522135750006e-05, 1.2237558961135251e-05, 2.5724314501041623e-06, 4.3170147045765155e-07, 6.339153940886676e-08, 8.274210137473773e-09, 9.719956106721062e-10, 1.0380287351449993e-10, 1.0161688724652392e-11, 9.182486371948037e-13], [0.00011390292497527722, 0.0001338050898867863, 7.85923718969333e-05, 3.077491758403752e-05, 9.038048440117678e-06, 2.1234518502374946e-06, 3.702625867876718e-07, 6.671324329639271e-08, 9.79624921599949e-09, 1.2786599809391107e-09, 1.5020791935003405e-10, 1.6041238748379094e-11, 1.5703426061330667e-12, 1.4190209886201287e-13], [1.5087476745692875e-05, 1.7723699216331908e-05, 1.0410273341454563e-05, 4.076417295697729e-06, 1.1971715888447873e-06, 2.812704802621223e-07, 5.506944020115031e-08, 8.230596010606732e-09, 1.2976021667001504e-09, 1.693701257650252e-10, 1.9896402929990116e-11, 2.1248077399312466e-12, 2.0800613819132287e-13, 1.879622158263561e-14], [1.7486641390120316e-06, 2.054206793663028e-06, 1.2065683332179045e-06, 4.7246367704725606e-07, 1.387542172188976e-07, 3.259972561929389e-08, 6.382641501847543e-09, 1.071125032948904e-09, 1.400776495455975e-10, 1.963028478103917e-11, 2.306026838380379e-12, 2.462688201440764e-13, 2.410826413723451e-14, 2.1785139546188197e-15], [1.801539012996105e-07, 2.116320451128164e-07, 1.2430516962312935e-07, 4.867497007773703e-08, 1.429497694616245e-08, 3.3585453150144613e-09, 6.575635317850644e-10, 1.1035129568931548e-10, 1.6204110915102778e-11, 1.8836549942174792e-12, 2.375754852904736e-13, 2.537153231864968e-14, 2.483723283956705e-15, 2.2443863244199733e-16], [1.670411412143784e-08, 1.9622810318376433e-08, 1.1525743957196943e-08, 4.513209257033443e-09, 1.3254496547088473e-09, 3.1140887773904256e-10, 6.097018270376573e-11, 1.0231921836526125e-11, 1.5024671461993952e-12, 1.961102224087251e-13, 2.0517237978277398e-14, 2.3524828950645038e-15, 2.3029419225446904e-16, 2.0810254468681155e-17], [1.4080255652586029e-09, 1.6540487205505313e-09, 9.715296502632638e-10, 3.804280771231871e-10, 1.1172499096483675e-10, 2.6249321449638196e-11, 5.139307319219904e-12, 8.62470611899558e-13, 1.2664617455497765e-13, 1.653055078243606e-14, 1.941892039912085e-15, 1.846932654950874e-16, 1.9411990834564585e-17, 1.7541409318938472e-18], [1.0879503375684323e-10, 1.2780470101386813e-10, 7.506795594066724e-11, 2.9394839492894086e-11, 8.632743938331807e-12, 2.028227245066471e-12, 3.9710295542725386e-13, 6.664120428712815e-14, 9.785670925196057e-15, 1.2772792446165807e-15, 1.5004572022495789e-16, 1.6023916926058517e-17, 1.3970311902409352e-18, 1.3553860569612666e-19], [7.759710091504283e-12, 9.115557888566032e-12, 5.354155931081321e-12, 2.0965610724562293e-12, 6.157228684294812e-13, 1.446615243172005e-13, 2.8323019022007672e-14, 4.7531252811831605e-15, 6.979543717050194e-16, 9.110081868508842e-17, 1.070187902160009e-17, 1.142891780836839e-18, 1.1188236057073424e-19, 9.00402997553929e-21]] |
| Legacy trial inputs | {"lambda_home": 0.927213565786597, "lambda_away": 1.174729182027844, "rho": -0.10289506567663635, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-29T11:48:48Z", "over": 2.03, "under": 1.86, "bookmaker": "pinnacle", "event_id": "d20fbb0cd5ad9369b8ed6f2c4a198619", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Coventry City", "away_team": "Sunderland"}} |
| Legacy p home | 0.2902 |
| Legacy p draw | 0.3044 |
| Legacy p away | 0.4054 |
| Legacy p over 1 5 | 0.6358 |
| Legacy p under 3 5 | 0.8375 |
| Legacy p btts yes | 0.4273 |
| Legacy p over 2 5 | 0.3571 |
| Legacy goal margin distribution | {"-1": 0.22579450051926717, "-10": 1.87833940738745e-07, "-11": 1.9894627282852624e-08, "-12": 1.928377233368908e-09, "-13": 1.6078393500953245e-10, "-2": 0.1205931425340157, "-3": 0.04347265173329812, "-4": 0.012129167326964509, "-5": 0.0027522497486494896, "-6": 0.0005254863468512984, "-7": 8.652808567241145e-05, "-8": 1.2518741207822349e-05, "-9": 1.6146630402690926e-06, "0": 0.30440932904758417, "1": 0.18333777921344724, "10": 1.84353273590015e-08, "11": 1.5411844222035524e-09, "12": 1.1791059164540927e-10, "13": 7.759710091504283e-12, "2": 0.07857117345674752, "3": 0.022356240780144372, "4": 0.004923292667720478, "5": 0.0008817683907974204, "6": 0.000132883219595737, "7": 1.7270615699777294e-05, "8": 1.972211133564631e-06, "9": 2.0077825183061153e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2748 |
| Legacy raw p draw | 0.3237 |
| Legacy raw p away | 0.4015 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9272 |
| Legacy lambda away | 1.1747 |
| Legacy model home team | Coventry |
| Legacy model away team | Sunderland |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.384542581390274, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,364.9791 |
| Elo away rating | 1,407.0794 |
| Elo rating diff | 17.8997 |
| Elo home expectancy | 0.5257 |

</details>


---

## 2026-10-31 — Hull City vs Ipswich Town

The model's most likely 1X2 outcome is **Hull City win** at **42.2%**. Expected goals are 1.75 for Hull City and 0.91 for Ipswich Town (2.66 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 51.3%; Under 3.5 goals: 70.6%; Double Chance 1X: 69.5%; Double Chance X2: 57.8%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 42.2% | 2.37 |
| Draw | 27.3% | 3.66 |
| Ipswich Town win | 30.5% | 3.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.75 |
| Ipswich Town expected goals | 0.91 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 51.3% |
| Under 2.5 | 48.7% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.01% |
| 2 | 1-2 | 8.50% |
| 3 | 0-1 | 8.21% |
| 4 | 0-0 | 7.71% |
| 5 | 1-0 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 42.2% | 36.1% | 2.69 | +13.5% |
| Draw | 27.3% | 28.3% | 3.41 | -6.9% |
| Ipswich Town win | 30.5% | 35.7% | 2.72 | -17.0% |
| Over 2.5 | 51.3% | 51.3% | 1.89 | -2.9% |
| Under 2.5 | 48.7% | 48.7% | 1.99 | -3.2% |

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
| Market best home last update utc | 2026-10-29T11:48:48Z |
| Market best draw last update utc | 2026-10-29T11:48:48Z |
| Market best away last update utc | 2026-10-29T11:48:48Z |
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
| Dc lambda home | 1.8159 |
| Dc lambda away | 0.7784 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:48:36.104635+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6093 |
| Shot lambda away | 1.2179 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.97 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.26 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.97 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.19648540150228472, "-10": 2.1653772572030314e-08, "-11": 1.8672360419529937e-09, "-12": 1.478933728720858e-10, "-13": 1.0829838612647711e-11, "-14": 7.371874049602967e-13, "-15": 4.665019904475003e-14, "-16": 2.5219077011809007e-15, "-2": 0.07999930585079205, "-3": 0.022546686828880707, "-4": 0.0049971380332780695, "-5": 0.0009088445286538696, "-6": 0.00013984716331967554, "-7": 1.862487381439155e-05, "-8": 2.1847810471863826e-06, "-9": 2.288774781652258e-07, "0": 0.2730397448601114, "1": 0.1733047415712573, "10": 6.768953172539688e-06, "11": 1.1246700680333632e-06, "12": 1.7163766817647236e-07, "13": 2.4217195826033734e-08, "14": 3.176272482731977e-09, "15": 3.872855768449971e-10, "16": 4.0340844630665733e-11, "2": 0.13163468642039336, "3": 0.07148333958918071, "4": 0.0305268100215678, "5": 0.010697631946550145, "6": 0.0031716824058506707, "7": 0.0008138930638188625, "8": 0.00018395851908642173, "9": 3.713240011267683e-05} |
| Raw goal margin distribution | {"-1": 0.12100011269974695, "-10": 8.660316720513677e-09, "-11": 7.081728162991342e-10, "-12": 5.3179121130865143e-11, "-13": 3.691462594012167e-12, "-14": 2.3818008908681247e-13, "-15": 1.4298258190252318e-14, "-16": 7.396457187544185e-16, "-2": 0.047629749119771275, "-3": 0.012861503161105256, "-4": 0.002720290846319114, "-5": 0.00047106184443595394, "-6": 6.891652131012768e-05, "-7": 8.718488383467992e-06, "-8": 9.7085784804171e-07, "-9": 9.650525722884477e-08, "0": 0.25082901375927164, "1": 0.24095851700500412, "10": 6.108204134482763e-06, "11": 9.624030625348475e-07, "12": 1.392505363733849e-07, "13": 1.8624823672191417e-08, "14": 2.315459173779132e-09, "15": 2.6782603158279474e-10, "16": 2.6695089168105684e-11, "2": 0.17682930803723576, "3": 0.09200377751079672, "4": 0.037494472426343746, "5": 0.012510302525775981, "6": 0.0035265594381236154, "7": 0.0008596210277406313, "8": 0.00018444184575428993, "9": 3.532586162536331e-05} |
| Unadjusted home-win probability | 56.4% |
| Unadjusted draw probability | 25.1% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 50.3% |
| P home draw | 69.5% |
| P draw away | 57.8% |
| P home away | 72.7% |
| Raw p home draw | 81.5% |
| Raw p draw away | 43.6% |
| Raw p home away | 74.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0560 |
| Totals anchor target over 2 5 | 0.5135 |
| Totals anchor reference over odds | 1.89 |
| Totals anchor reference under odds | 1.99 |
| Totals anchor reference last update utc | 2026-10-29T11:48:48Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4812 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.69 |
| Reference draw odds | 3.41 |
| Reference away odds | 2.72 |
| Market reference 1x2 last update utc | 2026-10-29T11:48:48Z |
| Market reference home last update utc | 2026-10-29T11:48:48Z |
| Market reference draw last update utc | 2026-10-29T11:48:48Z |
| Market reference away last update utc | 2026-10-29T11:48:48Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.99 |
| Market reference over 2 5 last update utc | 2026-10-29T11:48:48Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:48:48Z |
| Market best over 2 5 last update utc | 2026-10-29T11:48:48Z |
| Market best under 2 5 last update utc | 2026-10-29T11:48:48Z |
| Home probability edge | +6.1% |
| Draw probability edge | -1.0% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.2036 |
| Raw ev home | 0.5183 |
| Raw edge prob draw | -0.0317 |
| Raw ev draw | -0.1447 |
| Raw edge prob away | -0.1719 |
| Raw ev away | -0.4974 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08616741393388443, 0.0775454618874696, 0.041396551173242487, 0.012023214520201669, 0.0026190168619450024, 0.0004564003619249869, 6.627846164717096e-05, 8.249964307254133e-06, 8.985448772804787e-07, 8.699112614768171e-08, 7.579710927973746e-09, 6.003958031107913e-10, 4.359473997978719e-11, 2.921920727921306e-12, 1.818520007472569e-13, 1.0563419192879018e-14, 5.752574101430845e-16], [0.09248129069967947, 0.12755841162824202, 0.07398891912349993, 0.021489342023127102, 0.004681023449769505, 0.000815733883846608, 0.000118460876557568, 1.4745333236739191e-05, 1.605987995852967e-06, 1.55481053725154e-07, 1.3547375395654993e-08, 1.0730999385080806e-09, 7.791778781463732e-11, 5.2224098456585014e-12, 3.2502787296040194e-13, 1.8880219394574596e-14, 1.0281695645646432e-15], [0.09078627003493615, 0.07910389410588405, 0.045029293168600826, 0.019204174549619136, 0.004183245410840758, 0.0007289890902462065, 0.00010586379742404856, 1.3177320783758137e-05, 1.4352079167319872e-06, 1.3894726472700376e-07, 1.210675326901028e-08, 9.58986948326112e-10, 6.963204346145611e-11, 4.66706100809135e-12, 2.9046454745358836e-13, 1.687250490956414e-14, 9.188344512016856e-16], [0.05408806451072107, 0.04712801314341731, 0.020531790543234067, 0.007791710939961783, 0.0024922672509693645, 0.00043431246735520115, 6.307085754507143e-05, 7.850700071234366e-06, 8.550590123002614e-07, 8.278111453692681e-08, 7.212884190281425e-09, 5.713391232621617e-10, 4.148493442133097e-11, 2.780511819507239e-12, 1.7305111416848988e-13, 1.0052193284896251e-14, 5.474173248019232e-16], [0.02416818138957133, 0.0210582201541792, 0.009174224343028742, 0.002664561761946678, 0.0007583908105961103, 0.00019406393232488848, 2.818196471502431e-05, 3.507929985535052e-06, 3.8206620064883736e-07, 3.69891030462509e-08, 3.2229345795529344e-09, 2.5529158217931016e-10, 1.8536722086449682e-11, 1.24241668873875e-12, 7.732446621495357e-14, 4.4916236672556195e-15, 2.4460259987643603e-16], [0.008639258911746713, 0.00752755919860066, 0.003279456494317569, 0.0009524853598513009, 0.00020747988934364189, 4.724254283278714e-05, 1.0074042638552195e-05, 1.2539592822815517e-06, 1.3657497747252806e-07, 1.3222279036176521e-08, 1.1520836358996395e-09, 9.125759364700147e-11, 6.626213983524436e-12, 4.4411945099521083e-13, 2.7640726171140513e-14, 1.6055945281962669e-15, 8.743666545513284e-17], [0.002573521266836714, 0.002242360587044192, 0.0009769068293944282, 0.00028373282418877563, 6.180552210801075e-05, 1.0770477681503082e-05, 2.0436709746008136e-06, 3.735379288507064e-07, 4.0683884188885024e-08, 3.9387425059552566e-09, 3.431905176647648e-10, 2.7184433342028162e-11, 1.973861737379414e-12, 1.3229732594284933e-13, 8.233807709538612e-15, 4.782854300860772e-16, 2.6046229236643643e-17], [0.0006571011748495105, 0.0005725454050722113, 0.0002494351352699812, 7.244594187751994e-05, 1.578089977833397e-05, 2.7500427641327708e-06, 3.9936121676566777e-07, 6.495238594824397e-08, 1.0387879223091716e-08, 1.0056852303669414e-09, 8.762736693134816e-11, 6.941043509860487e-12, 5.03989177527478e-13, 3.3779681336517456e-14, 2.1023508875343846e-15, 1.2212136036057301e-16, 6.650424091049149e-18], [0.0001468063289814665, 0.0001279152926687552, 5.5727577319227706e-05, 1.618551782239492e-05, 3.52569140515116e-06, 6.144010971169515e-07, 8.92233287885485e-08, 1.110601030238825e-08, 1.5805030823461755e-09, 2.2468527288033523e-10, 1.9577277518107236e-11, 1.5507339752004256e-12, 1.1259879578839985e-13, 7.546891104423324e-15, 4.696969475066535e-16, 2.7283756734820056e-17, 1.4858052067863517e-18], [2.915444589244634e-05, 2.540285221217176e-05, 1.106700677649704e-05, 3.214301500951031e-06, 7.001713074503704e-07, 1.22014654725255e-07, 1.771896845018229e-08, 2.205555977650027e-09, 2.402181332506124e-10, 3.038718993495658e-11, 3.887875148728224e-12, 3.0796213002006644e-13, 2.2361130627971418e-14, 1.498746204517323e-15, 9.327768316895043e-17, 5.418314148897491e-18, 2.9506784760918837e-19], [5.210834907959559e-06, 4.5403047465641684e-06, 1.978029198371324e-06, 5.744988098093816e-07, 1.2514307779587617e-07, 2.1807933667150272e-08, 3.1669481791511608e-09, 3.942036189676071e-10, 4.293468786492992e-11, 4.156650316090564e-12, 4.732283481065105e-13, 5.5042713669063985e-14, 3.99665150514373e-15, 2.678740343576275e-16, 1.6671714817817588e-17, 9.684265862408795e-19, 5.273809168627746e-20], [8.466758080608912e-07, 7.377255771945388e-07, 3.2139753023856026e-07, 9.334670021542611e-08, 2.033371204184632e-08, 3.543434053450551e-09, 5.145775016924768e-10, 6.405166801966866e-11, 6.9761875369250915e-12, 6.753879804993911e-13, 5.884790648327272e-14, 6.090677360785352e-15, 6.4939077948650435e-16, 4.3525167944168425e-17, 2.70888213970758e-18, 1.5735354831539222e-19, 8.569080998106893e-21], [1.2610677723746594e-07, 1.098793589469867e-07, 4.787004230496565e-08, 1.3903375315375328e-08, 3.0285722946833962e-09, 5.277711310277605e-10, 7.66429249064809e-11, 9.540073489454857e-12, 1.039057121167361e-12, 1.00594585075913e-13, 8.765007530773323e-15, 6.942842261027465e-16, 6.586934038432373e-17, 6.4827866887201715e-18, 4.034701278840438e-19, 2.343677317340678e-20, 1.2763080960503271e-21], [1.733794404365941e-08, 1.5106897652206662e-08, 6.581471139241217e-09, 1.911522509072224e-09, 4.1638695498910565e-10, 7.256125751582188e-11, 1.0537345989491865e-11, 1.311628636905848e-12, 1.4285603533458077e-13, 1.3830369194647436e-14, 1.2050677484576317e-15, 9.545451343901686e-17, 6.9309523346270845e-18, 6.069834111419771e-19, 5.547158252541055e-20, 3.222233338651531e-21, 1.754747749212619e-22], [2.2134620660367157e-09, 1.928633799051119e-09, 8.402286146928375e-10, 2.440360028589448e-10, 5.315836337573014e-11, 9.26358918743482e-12, 1.3452584438911084e-12, 1.6745008665432118e-13, 1.823782648745679e-14, 1.7656648040013846e-15, 1.538459082287047e-16, 1.2186274450835126e-17, 8.84845402406066e-19, 5.930642374504132e-20, 4.822818995163344e-21, 4.113689169294743e-22, 2.240212316157444e-23], [2.6374446042062695e-10, 2.2980582702756996e-10, 1.0011720824695509e-10, 2.907804244076498e-11, 6.3340700888898815e-12, 1.1038004080969075e-12, 1.6029389789617806e-13, 1.9952468772644686e-14, 2.173123172059602e-15, 2.1038730148597573e-16, 1.833146665411521e-17, 1.4520521624877349e-18, 1.0543350924966306e-19, 7.066640522157257e-21, 4.398075229200905e-22, 3.3380947273916385e-23, 2.669318790768865e-24], [2.9462248361081895e-11, 2.567104666354759e-11, 1.1183848373102203e-11, 3.2482369748263217e-12, 7.075634718460191e-13, 1.2330284288265295e-13, 1.7906039137471694e-14, 2.2288414682108503e-15, 2.427542724966929e-16, 2.3501850687260384e-17, 2.0477632877107216e-18, 1.6220519428628686e-19, 1.1777719350540945e-20, 7.89397122541421e-22, 4.912982229343736e-23, 2.853853164247137e-24, 2.0306678995633874e-25]] |
| Legacy trial inputs | {"lambda_home": 1.7873208522579576, "lambda_away": 0.8713200143088098, "rho": -0.10289506567663635, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-29T11:48:48Z", "over": 1.89, "under": 1.99, "bookmaker": "pinnacle", "event_id": "1ec76c009147b63859f68c6b5a1dd77b", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Hull City", "away_team": "Ipswich Town"}} |
| Legacy p home | 0.4699 |
| Legacy p draw | 0.2674 |
| Legacy p away | 0.2627 |
| Legacy p over 1 5 | 0.7438 |
| Legacy p under 3 5 | 0.7351 |
| Legacy p btts yes | 0.5061 |
| Legacy p over 2 5 | 0.4841 |
| Legacy goal margin distribution | {"-1": 0.17343534494095839, "-10": 8.725302377869763e-09, "-11": 6.831582821080211e-10, "-12": 4.9117911168784055e-11, "-13": 3.264368523116074e-12, "-14": 2.016510545930332e-13, "-15": 1.1591588757443662e-14, "-16": 5.752574101430845e-16, "-2": 0.06753292870802155, "-3": 0.017499946450668696, "-4": 0.003548860882012253, "-5": 0.0005889317871613592, "-6": 8.254510011546887e-05, "-7": 1.0002374504247802e-05, "-8": 1.0667230125968575e-06, "-9": 1.0154024396843491e-07, "0": 0.26735457325884815, "1": 0.19500019818943082, "10": 5.998396330037958e-06, "11": 9.633871315229098e-07, "12": 1.4208368911027808e-07, "13": 1.9369943287932313e-08, "14": 2.454451741437388e-09, "15": 2.8941550708417456e-10, "16": 2.9462248361081895e-11, "2": 0.14810563991860934, "3": 0.07872588740453214, "4": 0.0327487442975567, "5": 0.011147962655386616, "6": 0.003205137315213957, "7": 0.0007966788452947378, "8": 0.00017428365959123088, "9": 3.403047735763136e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5791 |
| Legacy raw p draw | 0.2522 |
| Legacy raw p away | 0.1687 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7873 |
| Legacy lambda away | 0.8713 |
| Legacy model home team | Hull |
| Legacy model away team | Ipswich |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.830643156000104, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,403.0690 |
| Elo away rating | 1,376.0928 |
| Elo rating diff | 86.9763 |
| Elo home expectancy | 0.6226 |

</details>


---

## 2026-10-31 — Manchester City vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Manchester City win** at **59.0%**. Expected goals are 2.03 for Manchester City and 1.07 for Brighton and Hove Albion (3.09 combined). The most likely exact score is 2-1 at 10.0%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.2%; Under 3.5 goals: 62.6%; Double Chance 1X: 80.1%; Double Chance X2: 41.0%; Double Chance 12 (either team wins): 78.8%; Under 4.5 goals: 79.8%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 59.0% | 1.70 |
| Draw | 21.2% | 4.72 |
| Brighton and Hove Albion win | 19.9% | 5.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 2.03 |
| Brighton and Hove Albion expected goals | 1.07 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 82.2% |
| Under 1.5 | 17.8% |
| Over 2.5 | 60.2% |
| Under 2.5 | 39.8% |
| Over 3.5 | 37.4% |
| Under 3.5 | 62.6% |
| Over 4.5 | 20.2% |
| Under 4.5 | 79.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.96% |
| 2 | 1-1 | 9.89% |
| 3 | 2-0 | 9.34% |
| 4 | 1-0 | 8.48% |
| 5 | 3-1 | 6.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 59.0% | 59.0% | 1.66 | -2.1% |
| Draw | 21.2% | 20.6% | 4.58 | -3.1% |
| Brighton and Hove Albion win | 19.9% | 20.4% | 4.61 | -8.4% |

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
| Market best home last update utc | 2026-10-29T11:48:48Z |
| Market best draw last update utc | 2026-10-29T11:48:48Z |
| Market best away last update utc | 2026-10-29T11:48:48Z |
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
| Dc lambda away | 1.0539 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:48:36.104635+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7466 |
| Shot lambda away | 1.0955 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.20 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.61 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.51 |
| Fair Over 3.5 odds | 2.68 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.94 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.12377535001258286, "-10": 3.088575334719226e-08, "-11": 2.94665851587857e-09, "-12": 2.583237063136875e-10, "-13": 2.0944357825071795e-11, "-14": 1.579239650597723e-12, "-15": 1.1124623582317149e-13, "-16": 7.307451786116699e-15, "-17": 4.067190109479e-16, "-2": 0.053637017758723156, "-3": 0.01638740140681627, "-4": 0.003967884777341001, "-5": 0.0007919457980416749, "-6": 0.00013410746024457952, "-7": 1.969237344816957e-05, "-8": 2.5502429724466627e-06, "-9": 2.952238686084759e-07, "0": 0.21164551024904402, "1": 0.2275204012566797, "10": 1.7710799334794703e-05, "11": 3.2090424881348642e-06, "12": 5.342882409937942e-07, "13": 8.227049238345005e-08, "14": 1.178123398834323e-08, "15": 1.5761362649789014e-09, "16": 1.9662561321327367e-10, "17": 2.078424718883242e-11, "2": 0.1817268209934841, "3": 0.10544602018848676, "4": 0.04848918091860155, "5": 0.018380061036873372, "6": 0.005911124722475315, "7": 0.0016484696011747717, "8": 0.00040544330539413984, "9": 8.913858503303653e-05} |
| Raw goal margin distribution | {"-1": 0.1159272111043925, "-10": 2.8927401522469255e-08, "-11": 2.7598217560126822e-09, "-12": 2.4194435186046003e-10, "-13": 1.961635326247272e-11, "-14": 1.4791058828810253e-12, "-15": 1.0419252188364478e-13, "-16": 6.8441131918286e-15, "-17": 3.8093045697332897e-16, "-2": 0.05023609208209417, "-3": 0.015348336661114537, "-4": 0.0037162958228270323, "-5": 0.0007417314328214842, "-6": 0.00012560420029405562, "-7": 1.8443752602116755e-05, "-8": 2.388541461642104e-06, "-9": 2.7650481081855956e-07, "0": 0.22596955400654042, "1": 0.2268551028506698, "10": 1.765901071934959e-05, "11": 3.1996588423590056e-06, "12": 5.327259146568168e-07, "13": 8.202992306684352e-08, "14": 1.1746784171315914e-08, "15": 1.5715274433569587e-09, "16": 1.9605065507181045e-10, "17": 2.0723471423457228e-11, "2": 0.1811954288032962, "3": 0.10513768269978682, "4": 0.04834739242580843, "5": 0.018326315415633898, "6": 0.005893839846772448, "7": 0.0016436492677367168, "8": 0.0004042577379315465, "9": 8.887793254557209e-05} |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 57.7% |
| P home draw | 80.1% |
| P draw away | 41.0% |
| P home away | 78.8% |
| Raw p home draw | 81.4% |
| Raw p draw away | 41.2% |
| Raw p home away | 77.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6020 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.68, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.56, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.66 |
| Reference draw odds | 4.58 |
| Reference away odds | 4.61 |
| Market reference 1x2 last update utc | 2026-10-29T11:48:48Z |
| Market reference home last update utc | 2026-10-29T11:48:48Z |
| Market reference draw last update utc | 2026-10-29T11:48:48Z |
| Market reference away last update utc | 2026-10-29T11:48:48Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.92 |
| Market reference over 2 5 last update utc | 2026-10-29T11:48:08Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:48:08Z |
| Home probability edge | -0.1% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -8.3% |
| Under 2.5 probability edge | +8.3% |
| Raw edge prob home | -0.0025 |
| Raw ev home | -0.0241 |
| Raw edge prob draw | 0.0205 |
| Raw ev draw | 0.0349 |
| Raw edge prob away | -0.0180 |
| Raw ev away | -0.1420 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.04979776012953698, 0.039348868703168595, 0.02865990994441324, 0.01107382273010838, 0.003209087626994699, 0.0007439702548050216, 0.0001437302966785899, 2.3800949471403924e-05, 3.4486434504564616e-06, 4.441705772252861e-07, 5.148654943783111e-08, 5.425566640255549e-09, 5.240923933563489e-10, 4.6731369059398055e-11, 3.869229311477311e-12, 2.9900414607402644e-13, 2.1662133505565032e-14, 1.4770537754561832e-15], [0.07774931274341583, 0.10218495186527538, 0.05689349953484403, 0.021982920726768707, 0.006370439605979526, 0.0014768738432110193, 0.0002853225841632617, 4.72478563368315e-05, 6.845987824976907e-06, 8.817340521226673e-07, 1.0220722891918839e-07, 1.077042718286057e-08, 1.0403888356755684e-09, 9.276760216623633e-11, 7.680903270795187e-12, 5.935605617244844e-13, 4.3002039605600204e-14, 2.9321361598778195e-15], [0.08762188516808089, 0.10156792804072151, 0.05329967817458812, 0.02181942114557706, 0.006323058995344107, 0.0014658894859529837, 0.00028320047656914173, 4.689644694863914e-05, 6.795070289671244e-06, 8.751760906017071e-07, 1.0144705517654748e-07, 1.0690321342715838e-08, 1.0326508675946348e-09, 9.20776363381804e-11, 7.623775990778237e-12, 5.891459116213406e-13, 4.268220878997338e-14, 2.9103281826715363e-15], [0.05798012732444204, 0.06720833943009058, 0.038952664450653096, 0.013627428259506845, 0.00418402052097779, 0.0009699912171037852, 0.0001873961015370053, 3.103176746232053e-05, 4.496354304839717e-06, 5.791112695995625e-07, 6.712835685448819e-08, 7.07387419707852e-09, 6.833136341449457e-10, 6.092853478763266e-11, 5.0447157327239204e-12, 3.8984273053421174e-13, 2.824317115962454e-14, 1.925788269260807e-15], [0.02877444794279931, 0.03335423624428437, 0.019331475579498183, 0.007469434973591467, 0.0019598631571908277, 0.0004813884182306598, 9.300116466089503e-05, 1.540048321075653e-05, 2.231456170370476e-06, 2.87402043581859e-07, 3.3314542394611994e-08, 3.5106308701040083e-09, 3.3911571949963744e-10, 3.0237687176287065e-11, 2.5035976451933744e-12, 1.9347162335234426e-13, 1.4016555253917045e-14, 9.557325390580612e-16], [0.011424174352426163, 0.013242464668799029, 0.007675078526228399, 0.002965552201802456, 0.0008593885878393508, 0.00018039212197136313, 3.692378467787898e-05, 6.114376396066435e-06, 8.859438207393622e-07, 1.1410578794247142e-07, 1.3226705219294464e-08, 1.3938081184669308e-09, 1.3463740861036348e-10, 1.2005116866280988e-11, 9.93990781816897e-13, 7.681306559965518e-14, 5.564922439501905e-15, 3.7944968335069453e-16], [0.0037797354066263903, 0.004381324289665527, 0.0025393315227251003, 0.000981165230113205, 0.0002843322741146025, 6.591741298770136e-05, 1.1530466904005633e-05, 2.02296675809617e-06, 2.9311818291877504e-07, 3.775237259886254e-08, 4.376110210516894e-09, 4.611471895379425e-10, 4.454534434455138e-11, 3.971942643761676e-12, 3.288659675520174e-13, 2.5413920934852847e-14, 1.8411776405747914e-15, 1.255424995233205e-16], [0.0010718923851461258, 0.0012424965342057992, 0.0007201271596415738, 0.00027824792626613787, 8.063358057826314e-05, 1.8693470687439967e-05, 3.6114590207137062e-06, 5.414802747789182e-07, 8.31251699967369e-08, 1.0706167590190775e-08, 1.2410178773333707e-09, 1.3077639245082664e-10, 1.263258145343408e-11, 1.1264002942167174e-12, 9.326285795950804e-14, 7.207115153885457e-15, 5.221382134774668e-16, 3.5602505142381733e-17], [0.0002659800267777956, 0.00030831384383267556, 0.00017869279030167948, 6.90446092394287e-05, 2.0008465605875373e-05, 4.638609157893588e-06, 8.961496325075514e-07, 1.4839746814010876e-07, 1.946858975655271e-08, 2.6566349213669496e-09, 3.0794692901923545e-10, 3.2450933366069643e-11, 3.134656426166351e-12, 2.795056524050559e-13, 2.3142302157564084e-14, 1.788377926912675e-15, 1.2956369307868006e-16, 8.834427226420089e-18], [5.866706241541024e-05, 6.800460823615732e-05, 3.941416657789287e-05, 1.5229129979301617e-05, 4.413255817577326e-06, 1.023135369537284e-06, 1.9766321201173912e-07, 3.27319446919892e-08, 4.7427018328976495e-09, 5.530715283582339e-10, 6.792367804556368e-11, 7.157683816672426e-12, 6.914093754806722e-13, 6.165040192587983e-14, 5.104484353813281e-15, 3.9446149672049985e-16, 2.8577789696096585e-17, 1.948604561686789e-18], [1.1646144369314189e-05, 1.3499763797426921e-05, 7.824204166080177e-06, 3.023172442181281e-06, 8.76086380911422e-07, 2.0310514507460554e-07, 3.923861548224367e-08, 6.49769969172996e-09, 9.414855282071958e-10, 1.2125932312825589e-10, 1.272662152921578e-11, 1.420889603924921e-12, 1.3725339353330502e-13, 1.2238374510233627e-14, 1.013303875596806e-15, 7.830553209591057e-17, 5.673048058892023e-18, 3.8682233453958517e-19], [2.1017318760958377e-06, 2.4362469666420217e-06, 1.412002013667372e-06, 5.455795229027428e-07, 1.5810371351968782e-07, 3.665355194523536e-08, 7.08123189252166e-09, 1.1726131954356967e-09, 1.6990602922025378e-10, 2.1883172371103666e-11, 2.5366133956458456e-12, 2.4202464167100696e-13, 2.4769556614062543e-14, 2.208609218990086e-15, 1.828667916160025e-16, 1.4131477994919662e-17, 1.0237916998017697e-18, 6.9808239113863e-20], [3.476833485838604e-07, 4.030212002650075e-07, 2.335833575646067e-07, 9.025362254769403e-08, 2.6154634263900663e-08, 6.063489745173752e-09, 1.1714274520421703e-09, 1.9398196650090346e-10, 2.810705678291352e-11, 3.6200691126008306e-12, 4.196245246558789e-13, 4.4219331986018905e-14, 3.867487518640637e-15, 3.653637543900686e-16, 3.025111774578212e-17, 2.337729015577229e-18, 1.6936286235552642e-19, 1.1548172538038798e-20], [5.3091912037231394e-08, 6.154210778503315e-08, 3.56686252697836e-08, 1.37819007118424e-08, 3.993862655087853e-09, 9.259064763976539e-10, 1.7887921148694334e-10, 2.9621417143568124e-11, 4.292001306424323e-12, 5.527914744198462e-13, 6.407746716211056e-14, 6.7523765337315e-15, 6.522579876080749e-16, 5.265917408400897e-17, 4.6194035145160515e-18, 3.5697568999906728e-19, 2.5862032873238205e-20, 1.763428024602234e-21], [7.528148151030227e-09, 8.726340550845231e-09, 5.057619608542432e-09, 1.9541995452863133e-09, 5.663082870566773e-10, 1.312885684627793e-10, 2.5364112037796573e-11, 4.200157955205487e-12, 6.085827475288366e-13, 7.838286391231748e-14, 9.08584090173404e-15, 9.574507484647277e-16, 9.248668158651018e-17, 8.246693340881101e-18, 6.182296061821709e-19, 5.061723674115687e-20, 3.667097444522623e-21, 2.5004462852222546e-22], [9.962875997856266e-10, 1.1548583672763948e-09, 6.693337590246406e-10, 2.5862200575968e-10, 7.494617703202279e-11, 1.7374946683956156e-11, 3.3567286131811675e-12, 5.558558630836088e-13, 8.054084917596515e-14, 1.037331808365638e-14, 1.2024352393734302e-15, 1.2671061846336466e-16, 1.2239840683442436e-17, 1.0913810607765698e-18, 9.036336138537897e-20, 6.322649512857612e-21, 4.853097518655329e-22, 3.309132044055284e-23], [1.2360970473413826e-10, 1.4328362795993884e-10, 8.304444252786969e-11, 3.208731070885889e-11, 9.29859491965389e-12, 2.155714905853835e-12, 4.164703373174952e-13, 6.896520555438888e-14, 9.992727589724083e-15, 1.287020721436225e-15, 1.4918650491369583e-16, 1.5721024871037965e-17, 1.5186007466104773e-18, 1.3540797928635296e-19, 1.1211409659253369e-20, 8.663890665532097e-22, 5.683174220452951e-23, 4.1056501654739386e-24], [1.4434158648447439e-11, 1.6731522999323948e-11, 9.697269813056177e-12, 3.7469010574036505e-12, 1.0858159928996557e-12, 2.517272492385758e-13, 4.863209514287376e-14, 8.053208446180481e-15, 1.1668712879059265e-15, 1.5028804831308022e-16, 1.7420814043389203e-17, 1.8357763056938988e-18, 1.773301226418399e-19, 1.581186735692536e-20, 1.3091792917268092e-21, 1.011700275864792e-22, 7.329525938404314e-24, 4.525066376471994e-25]] |
| Legacy trial inputs | {"lambda_home": 1.9851248536785597, "lambda_away": 1.159161639194233, "rho": -0.10289506567663635, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5727 |
| Legacy p draw | 0.2211 |
| Legacy p away | 0.2062 |
| Legacy p over 1 5 | 0.8331 |
| Legacy p under 3 5 | 0.6129 |
| Legacy p btts yes | 0.5983 |
| Legacy p over 2 5 | 0.6146 |
| Legacy goal margin distribution | {"-1": 0.12276623092540874, "-10": 6.335313831056488e-08, "-11": 6.563276990090312e-09, "-12": 6.24888010248835e-10, "-13": 5.503061714551326e-11, "-14": 4.507397870261029e-12, "-15": 3.4491651386229817e-13, "-16": 2.459426966544285e-14, "-17": 1.4770537754561832e-15, "-2": 0.05803530056428141, "-3": 0.019113873377154634, "-4": 0.00500254378627943, "-5": 0.0010809867430350236, "-6": 0.00019838708862049244, "-7": 3.159289107913858e-05, "-8": 4.4392498889937165e-06, "-9": 5.57782698744187e-07, "0": 0.22106216568988213, "1": 0.22666841093224044, "10": 1.4330340701989946e-05, "11": 2.5424530516999485e-06, "12": 4.145512483053646e-07, "13": 6.252075947380303e-08, "14": 8.769797861891894e-09, "15": 1.1492684975586218e-09, "16": 1.403412277334622e-10, "17": 1.4434158648447439e-11, "2": 0.17743120796964654, "3": 0.10007608384930702, "4": 0.04485556410146273, "5": 0.016599294051520806, "6": 0.0052170678027140035, "7": 0.0014228079183633549, "8": 0.00034238152517378705, "9": 7.367321042713646e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5550 |
| Legacy raw p draw | 0.2366 |
| Legacy raw p away | 0.2084 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9851 |
| Legacy lambda away | 1.1592 |
| Legacy model home team | Man City |
| Legacy model away team | Brighton |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 10.24924717794746, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,654.7730 |
| Elo away rating | 1,529.0307 |
| Elo rating diff | 185.7423 |
| Elo home expectancy | 0.7444 |

</details>


---

## 2026-10-31 — Tottenham Hotspur vs Crystal Palace

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **57.3%**. Expected goals are 1.62 for Tottenham Hotspur and 1.21 for Crystal Palace (2.83 combined). The most likely exact score is 2-1 at 11.7%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 55.5%; Under 3.5 goals: 67.8%; Double Chance 1X: 79.7%; Double Chance X2: 42.7%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 83.5%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 57.3% | 1.75 |
| Draw | 22.4% | 4.47 |
| Crystal Palace win | 20.3% | 4.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.62 |
| Crystal Palace expected goals | 1.21 |
| Expected total goals | 2.83 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 78.9% |
| Under 1.5 | 21.1% |
| Over 2.5 | 55.5% |
| Under 2.5 | 44.5% |
| Over 3.5 | 32.2% |
| Under 3.5 | 67.8% |
| Over 4.5 | 16.5% |
| Under 4.5 | 83.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.67% |
| 2 | 1-0 | 10.77% |
| 3 | 1-1 | 10.58% |
| 4 | 2-0 | 9.62% |
| 5 | 3-1 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 57.3% | 62.2% | 1.58 | -9.5% |
| Draw | 22.4% | 20.7% | 4.55 | +1.8% |
| Crystal Palace win | 20.3% | 17.2% | 5.45 | +10.8% |

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
| Market best home last update utc | 2026-10-29T11:48:48Z |
| Market best draw last update utc | 2026-10-29T11:48:48Z |
| Market best away last update utc | 2026-10-29T11:48:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Tottenham |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6563 |
| Dc lambda away | 1.2166 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T11:48:36.104635+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.5392 |
| Shot lambda away | 1.2062 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.40 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.74 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 3.10 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.05 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.1171231089251226, "-10": 9.811079066811515e-08, "-11": 1.066623364151543e-08, "-12": 1.0653018634255738e-09, "-13": 9.835463990648806e-11, "-14": 8.387327757360891e-12, "-15": 5.998547001185245e-13, "-2": 0.058330434476305544, "-3": 0.02051593704093913, "-4": 0.005696673227616432, "-5": 0.0013009492506628633, "-6": 0.0002517131345540813, "-7": 4.2192057224263934e-05, "-8": 6.23318545935944e-06, "-9": 8.227560785590258e-07, "0": 0.22368021846628108, "1": 0.26961164412589844, "10": 3.0195943346362444e-06, "11": 4.385609309647748e-07, "12": 5.85165287558971e-08, "13": 7.217515793418956e-09, "14": 8.22249325849356e-10, "15": 7.856208464273444e-11, "2": 0.17694197352789834, "3": 0.08314076850320341, "4": 0.030841181447616568, "5": 0.009409294785977707, "6": 0.002432145871325986, "7": 0.0005446298791973259, "8": 0.00010748994296095156, "9": 1.8954655887844177e-05} |
| Raw goal margin distribution | {"-1": 0.1597845805837565, "-10": 1.338471261693338e-07, "-11": 1.4551352713045421e-08, "-12": 1.45333242094326e-09, "-13": 1.3417979620035217e-10, "-14": 1.1442367439078004e-11, "-15": 8.183485953306559e-13, "-2": 0.07957698607559412, "-3": 0.027988758371031115, "-4": 0.007771656257684618, "-5": 0.0017748131200206725, "-6": 0.0003433983097038461, "-7": 5.756029044494398e-05, "-8": 8.503590226257095e-06, "-9": 1.1224406194625146e-06, "0": 0.2627278827822879, "1": 0.21640600467645044, "10": 2.4237022396448656e-06, "11": 3.5201453996902834e-07, "12": 4.6968773313384865e-08, "13": 5.793198441435352e-09, "14": 6.599851873306809e-10, "15": 6.305850369225269e-11, "2": 0.14202393103191846, "3": 0.06673362196888745, "4": 0.02475492806780838, "5": 0.007552447885023658, "6": 0.0019521818967069696, "7": 0.0004371516540638521, "8": 8.627768720633168e-05, "9": 1.5214110518126897e-05} |
| Unadjusted home-win probability | 46.0% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.3% |
| P home draw | 79.7% |
| P draw away | 42.7% |
| P home away | 77.6% |
| Raw p home draw | 72.3% |
| Raw p draw away | 54.0% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5553 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.49, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T11:48:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.63, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T11:48:48Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.58 |
| Reference draw odds | 4.55 |
| Reference away odds | 5.45 |
| Market reference 1x2 last update utc | 2026-10-29T11:48:48Z |
| Market reference home last update utc | 2026-10-29T11:48:48Z |
| Market reference draw last update utc | 2026-10-29T11:48:48Z |
| Market reference away last update utc | 2026-10-29T11:48:48Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.46 |
| Market reference over 2 5 last update utc | 2026-10-29T11:48:49Z |
| Market reference under 2 5 last update utc | 2026-10-29T11:48:49Z |
| Home probability edge | -4.8% |
| Draw probability edge | +1.7% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.1616 |
| Raw ev home | -0.2733 |
| Raw edge prob draw | 0.0558 |
| Raw ev draw | 0.1954 |
| Raw edge prob away | 0.1058 |
| Raw ev away | 0.5113 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.06455625297271549, 0.04943234074355127, 0.03499825821813439, 0.013776698700371773, 0.004067290132651833, 0.0009606277604210402, 0.00018907054082588915, 3.189670417114341e-05, 4.7084266325685545e-06, 6.178076507446723e-07, 7.295805813573631e-08, 7.832502913578307e-09, 7.707957353020579e-10, 7.001900498064714e-11, 5.9061963817043776e-12, 4.64982500036565e-13], [0.10161117521359918, 0.11342547017102382, 0.056469874935963095, 0.02222877629485384, 0.006562594163618038, 0.0015499779775578245, 0.00030506631867127247, 5.1465501059723744e-05, 7.597071300780788e-06, 9.96835915507241e-07, 1.177182130841302e-07, 1.2637784920855147e-08, 1.2436829999479086e-09, 1.1297603525734805e-10, 9.529679132696639e-12, 7.502517256950498e-13], [0.09331369757000028, 0.1101958864375767, 0.04898992584041082, 0.017933124121866796, 0.005294390214581748, 0.00125044883663432, 0.00024611306018673803, 4.151992922398347e-05, 6.128957383547671e-06, 8.04200013748153e-07, 9.496948003974464e-08, 1.0195566440768038e-08, 1.0033445525962161e-09, 9.114371552407327e-11, 7.688093868117106e-12, 6.052675658375712e-13], [0.05018738169527769, 0.05926721540257703, 0.03499488021613587, 0.010371812366781464, 0.0028475088809296295, 0.0006725352728360689, 0.00013236824189202085, 2.233087521113185e-05, 3.2963683961987555e-06, 4.325269933607455e-07, 5.1077919622478286e-08, 5.483533477799875e-09, 5.396339159666179e-10, 4.9020289188530315e-11, 4.134926720472857e-12, 3.2553414070505915e-13], [0.020244401521582692, 0.023906991461736204, 0.014116106127963345, 0.005556657698086702, 0.001235165201488812, 0.00027128480587784146, 5.339421478168478e-05, 9.007746346429707e-06, 1.3296769650364588e-06, 1.7447114845885192e-07, 2.0603623436722825e-08, 2.2119275748562673e-09, 2.1767554513648108e-10, 1.9773624036857926e-11, 1.6679315390436097e-12, 1.313127648983671e-13], [0.00653288980812677, 0.007714811460187833, 0.00455528239525838, 0.0017931393232039486, 0.0005293879204559069, 9.414026531248265e-05, 1.7230369650015217e-05, 2.9068092844357502e-06, 4.290881646329106e-07, 5.6302024357887644e-08, 6.648811100528172e-09, 7.137913706506728e-10, 7.024412891556704e-11, 6.380969415292479e-12, 5.382432738480543e-13, 4.2374768281834745e-14], [0.001756808715717719, 0.002074648189613843, 0.0012249953771744555, 0.00048220663198422336, 0.00014236170209019517, 3.3623518015290324e-05, 4.982683435574205e-06, 7.816920284608627e-07, 1.153893375793166e-07, 1.5140602399483937e-08, 1.7879819855583807e-09, 1.9195102596147526e-10, 1.8889878986379583e-11, 1.7159546560189727e-12, 1.4474306202079315e-13, 1.1395318829875088e-14], [0.00040494573776729656, 0.0004782079769040448, 0.00028236236098634155, 0.00011114899339815765, 3.281448000966377e-05, 7.750246334286443e-06, 1.5254017490761954e-06, 1.937570862733173e-07, 2.6597329588865675e-08, 3.4899203049522335e-09, 4.1213120004404114e-10, 4.424485666978474e-11, 4.3541313940655116e-12, 3.9552884610602124e-13, 3.336338527485169e-14, 2.6266296093437536e-15], [8.167276148803399e-05, 9.64488878305056e-05, 5.694914555512099e-05, 2.241743616686592e-05, 6.618292154301493e-06, 1.5631329368317317e-06, 3.076554748115969e-07, 5.190229860153051e-08, 5.768567778789565e-09, 7.038756112119025e-10, 8.31219841664736e-11, 8.923663811817046e-12, 8.781767572015494e-13, 7.977348591879225e-14, 6.728999848251789e-15, 5.297600976963914e-16], [1.4642159231526474e-05, 1.729119901896308e-05, 1.0209749763874822e-05, 4.018961327344393e-06, 1.186516603558736e-06, 2.80235918856339e-07, 5.515597083493106e-08, 9.304959288258997e-09, 1.3735500035593262e-09, 1.3569797282080271e-10, 1.4901973505380322e-11, 1.5998198674888584e-12, 1.5743809414665811e-13, 1.4301660210767147e-14, 1.2063640980408815e-15, 9.497452472102403e-17], [2.3625201444120083e-06, 2.789944116669646e-06, 1.6473485300327098e-06, 6.484615380373852e-07, 1.9144508219465628e-07, 4.521621388055952e-08, 8.899445096974339e-09, 1.501360107743735e-09, 2.216230203110414e-10, 2.9079862173536743e-11, 2.58561428631539e-12, 2.581317826564126e-13, 2.540271984738808e-14, 2.3075804471326332e-15, 1.9464748593776097e-16, 1.532418984873883e-17], [3.465398874141492e-07, 4.092354185293493e-07, 2.4163687047480386e-07, 9.511782954122068e-08, 2.808160488563388e-08, 6.632418227004363e-09, 1.3053910711611932e-09, 2.202229529920465e-10, 3.250817424292757e-11, 4.265501052963287e-12, 5.037209775972066e-13, 4.071634140803918e-14, 3.7261293609489916e-15, 3.384812062829876e-16, 2.855134083062255e-17, 2.2477874050960445e-18], [4.65953285937623e-08, 5.502529287715787e-08, 3.2490197489693525e-08, 1.2789426797792884e-08, 3.77581818026783e-09, 8.917868270938574e-10, 1.7552128373443826e-10, 2.961090838668665e-11, 4.371009271501956e-12, 5.735340444153108e-13, 6.772970536191935e-14, 7.271206610187824e-15, 5.38761600091118e-16, 4.5511768204391973e-17, 3.838978299792227e-18, 3.0223473993399276e-19], [5.783216106817745e-09, 6.829507799460902e-09, 4.03254659011545e-09, 1.5873698348349848e-09, 4.686386634788839e-10, 1.1068482824236391e-10, 2.1784963124355322e-11, 3.675181343013762e-12, 5.425112770936406e-13, 7.118463209882756e-14, 8.406326015511955e-15, 9.024715664236614e-16, 8.881212586908941e-17, 6.074356941446188e-18, 4.764778317295595e-19, 3.751210408375849e-20], [6.665178434313126e-10, 7.871033566993527e-10, 4.647525195559403e-10, 1.8294497378281624e-10, 5.401078319764786e-11, 1.275646831417821e-11, 2.510725238809336e-12, 4.2356603967760473e-13, 6.252462985419889e-14, 8.204055770288227e-15, 9.68832252426866e-16, 1.040101893307536e-16, 1.0235631093749349e-17, 9.298036713351142e-19, 5.905200065269016e-20, 4.323284182135714e-21], [7.169533795380281e-11, 8.466636222762758e-11, 4.999204339812742e-11, 1.9678845587665486e-11, 5.809778976913459e-12, 1.3721752776694189e-12, 2.7007123106994214e-13, 4.556173650821283e-14, 6.725588087418067e-15, 8.824858281581414e-16, 1.0421439792323633e-16, 1.1188066078347791e-17, 1.1010163308740251e-18, 1.0001620977447612e-19, 8.436500582164331e-21, 5.000834438067566e-22]] |
| Legacy trial inputs | {"lambda_home": 1.6135052945778645, "lambda_away": 1.1809186572519224, "rho": -0.10289506567663635, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5419 |
| Legacy p draw | 0.2387 |
| Legacy p away | 0.2194 |
| Legacy p over 1 5 | 0.7844 |
| Legacy p under 3 5 | 0.6880 |
| Legacy p btts yes | 0.5578 |
| Legacy p over 2 5 | 0.5427 |
| Legacy goal margin distribution | {"-1": 0.1269721728662362, "-10": 8.664991820468352e-08, "-11": 9.171595868535659e-09, "-12": 8.917853985682281e-10, "-13": 8.015395167918136e-11, "-14": 6.656448107399427e-12, "-15": 4.64982500036565e-13, "-2": 0.06325037998847757, "-3": 0.02173156233884425, "-4": 0.00588709985771644, "-5": 0.0013106916930582069, "-6": 0.00024711886296956045, "-7": 4.03513373268464e-05, "-8": 5.805939765477583e-06, "-9": 7.462813874481667e-07, "0": 0.23867794916514734, "1": 0.25292318971105826, "10": 2.8058885132243615e-06, "11": 4.057864816341823e-07, "12": 5.390926775836681e-08, "13": 6.620311506915225e-09, "14": 7.511842056589401e-10, "15": 7.169533795380281e-11, "2": 0.16864058755856035, "3": 0.07916629648762415, "4": 0.02930226500452752, "5": 0.008913550863264058, "6": 0.002296183056264523, "7": 0.0005122818325066819, "8": 0.0001007103159258665, "9": 1.768701131067174e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4622 |
| Legacy raw p draw | 0.2704 |
| Legacy raw p away | 0.2674 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6135 |
| Legacy lambda away | 1.1809 |
| Legacy model home team | Tottenham |
| Legacy model away team | Crystal Palace |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 10.0289616681416, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,397.3033 |
| Elo away rating | 1,450.5828 |
| Elo rating diff | 6.7205 |
| Elo home expectancy | 0.5097 |

</details>


---
