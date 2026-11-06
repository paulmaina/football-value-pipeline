# La Liga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 2,009 |
| Training data through | 2026-11-02 |
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
| Training sha256 | 494f7cfecd2da025b582016e9ec2d381e9a1d07ba38552b72e03a86637a9546f |
| Training as of utc | 2026-11-06T13:17:34.983687+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 109, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 109, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 109, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-06T13:17:34.983687+00:00', 'observations': 597, 'observations_sha256': 'cf89ea84106d8c64affc2ad9a61e7f05a9547cb8b3c6a0da3fcbd25f525dadfb', 'eligible_training_matches': 177, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 184, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 30, 'retrospective_eligible_training_matches': 177, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '5d6ed38ad6bb38e9ede666515c6caae4c3ea8c2e406a8c42dd3bc406fe6876b8', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 115, 'tuning_matches': 22, 'audit_matches': 40, 'tuning_origin_utc': '2026-09-13T00:00:00+00:00', 'audit_origin_utc': '2026-10-09T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 17, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8357146014438204, 'audit_candidate_poisson_score': 0.8396597021665778, 'audit_gain': -0.003945100722757444, 'audit_gain_lower95': -0.032190166944846305, 'audit_baseline_briers': [0.5199253099278909, 0.20340070445316755, 0.22970209423243637, 0.28429820925953975], 'audit_candidate_briers': [0.5203622273931179, 0.21120580894026078, 0.23224016069563502, 0.2860639451268953], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-06', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2009, 'tune_start_date': '2025-11-07', 'audit_start_date': '2026-05-08', 'training_shot_matches': 1630, 'tuning_matches': 230, 'audit_matches': 129, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8434334657804535, 'audit_candidate_poisson_score': 0.8401860849808457, 'audit_gain': 0.0032473807996078463, 'audit_gain_lower95': -0.005248924741175115, 'audit_baseline_briers': [0.572479350599252, 0.18487847203851904, 0.2035768017324472, 0.25230542723445465], 'audit_candidate_briers': [0.5747575557978511, 0.1816774214546962, 0.20418486053167212, 0.24854937767119567], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1844.371 |
| Base scoring parameter | 0.089 |
| Home-advantage parameter | 0.289 |
| Dixon-Coles low-score adjustment | -0.021 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 2009, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261106T131734983687Z_ff29b5fb03379c437db8618b48d9262a07b2ec8da49fa13d3fe01899dfd88088.json |
| Over 1 5 in window quote fixtures | 0 |
| Odds provider health | — |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'None': 1} |
| Bbs statistics applied fixtures | 0 |
| Goal market validation | SKIPPED: not required by 48h-ah-price-edge-cagey-v28 |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-06 — Sevilla FC vs Deportivo Alavés

The model's most likely 1X2 outcome is **Sevilla FC win** at **47.8%**. Expected goals are 1.52 for Sevilla FC and 1.05 for Deportivo Alavés (2.57 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 47.5%; Under 3.5 goals: 74.2%; Double Chance 1X: 74.0%; Double Chance X2: 52.2%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 88.1%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla FC win | 47.8% | 2.09 |
| Draw | 26.2% | 3.82 |
| Deportivo Alavés win | 26.0% | 3.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla FC expected goals | 1.52 |
| Deportivo Alavés expected goals | 1.05 |
| Expected total goals | 2.57 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 73.0% |
| Under 1.5 | 27.0% |
| Over 2.5 | 47.5% |
| Under 2.5 | 52.5% |
| Over 3.5 | 25.8% |
| Under 3.5 | 74.2% |
| Over 4.5 | 11.9% |
| Under 4.5 | 88.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.46% |
| 2 | 1-0 | 11.34% |
| 3 | 2-1 | 9.28% |
| 4 | 2-0 | 8.82% |
| 5 | 0-0 | 7.87% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:00:00+00:00 |
| Fixture id | fdorg:564740 |
| Matched home-team name | Sevilla |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.5210 |
| Dc lambda away | 1.0532 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-06T13:17:34.983687+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.70 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.71 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.41 |
| Fair Under 4.5 odds | 1.14 |
| Score matrix json | [[0.07871672085875624,0.0777687544190823,0.04227319673978525,0.014841413653305945,0.003907929424838696,0.0008232052685152812,0.0001445068134641164,2.174311275646691e-05,2.8626164634140263e-06,3.350056169619057e-07,3.528446382787937e-08,3.378487145465329e-09,2.9653260881165776e-10,2.4024841971969794e-11,1.8074402010205267e-12,1.2691241612070375e-13],[0.11341506201195513,0.12459402995352961,0.06429609618816472,0.022573285992426875,0.005943827899807523,0.0012520672484948052,0.0002197899542711802,3.307053587230104e-05,4.3539423955669154e-06,5.095321630002561e-07,5.3666470841795024e-08,5.138564178442596e-09,4.5101602456144464e-10,3.654096849698227e-11,2.7490551456166476e-12,1.9302947360707708e-13],[0.08815384345569742,0.092848028307979,0.04889608905714768,0.017166600581286,0.004520180159598016,0.000952175875635963,0.000167146527006227,2.514958081509902e-05,3.311099238440523e-06,3.874905553617059e-07,4.081243952951308e-08,3.907790777214369e-09,3.429900259981334e-10,2.7788785879534646e-11,2.090609744481262e-12,1.4679563599824504e-13],[0.04469300041405486,0.047072898979136794,0.024789763472706842,0.008703272107164641,0.0022916801562491607,0.00048274238689817174,8.47413964934087e-05,1.2750552689712381e-05,1.6786898203589879e-06,1.964533237841917e-07,2.0691444698129375e-08,1.981205673826963e-09,1.7389205930261148e-10,1.4088599772105062e-11,1.0599154672443205e-12,7.442372519750857e-14],[0.016994133843533606,0.017899070061159244,0.009426097028657715,0.003309345304535345,0.0008713919168787993,0.00018355869283536672,3.2222196333993684e-05,4.848289373739553e-06,6.383075475950079e-07,7.469970795126352e-08,7.867746120385874e-09,7.533366317020764e-10,6.612097873802498e-11,5.357070413196909e-12,4.030238548834818e-13,2.82989894485376e-14],[0.005169500054440093,0.005444775503565767,0.002867354673762622,0.0010066803574379356,0.00026507150074363256,5.5837307234487066e-05,9.801773202236005e-06,1.4748166874668157e-06,1.9416881921860856e-07,2.272314363745302e-08,2.3933149151424223e-09,2.2915988507866422e-10,2.0113552495993458e-11,1.629584422932997e-12,1.2259711844940987e-13,8.608360322552111e-15],[0.0013104389951508993,0.0013802197629510908,0.0007268581754244122,0.00025518777099268217,6.719412465800799e-05,1.415444124455444e-05,2.484694011136124e-06,3.7385768016306124e-07,4.9220696327863574e-08,5.760188258312855e-09,6.066917805301362e-10,5.809073341114525e-11,5.098671678922985e-12,4.130904248405443e-13,3.10776754071707e-14,2.1821706029953554e-15],[0.0002847333135718085,0.00029989533890290417,0.00015793237041264932,5.544741867925203e-05,1.45999972812383e-05,3.0754891850996616e-06,5.398764548527111e-07,8.123211875638663e-08,1.0694715292817213e-08,1.2515786661232419e-09,1.3182251262847543e-10,1.2622004590200174e-11,1.1078437739769068e-12,8.975664331180108e-14,6.75258408024851e-15,4.741439081628604e-16],[5.413371216659745e-05,5.701632784946237e-05,3.0026221289173702e-05,1.0541705027453573e-05,2.7757624864515052e-06,5.847143217250586e-07,1.0264171847650399e-07,1.5443911638853918e-08,2.033287331582532e-09,2.379510792602869e-10,2.5062195449454734e-11,2.399705025309758e-12,2.1062409323908739e-13,1.7064600671869082e-14,1.2838063744470587e-15,9.014459716025026e-17],[9.148393026833685e-06,9.635544196718447e-06,5.074318062996926e-06,1.7815083596576401e-06,4.6909338301149065e-07,9.881451334977857e-08,1.7346062998282213e-08,2.6099627734583144e-09,3.4361788433339007e-10,4.021283424149822e-11,4.235416432948937e-12,4.0554109151870896e-13,3.55946767504444e-14,2.8838531026984805e-15,2.1695843151586182e-16,1.523409666659481e-17],[1.3914395015857533e-06,1.465533539635185e-06,7.717865395325878e-07,2.7096136958283144e-07,7.134751000969971e-08,1.5029351799989546e-08,2.63827725612686e-09,3.9696647159846917e-10,5.226311291069276e-11,6.11623548203708e-12,6.441924514157317e-13,6.168142236567612e-14,5.413829415884446e-15,4.3862426024935705e-16,3.299864040906227e-17,2.317054351589483e-18],[1.923938376036808e-07,2.026387934983764e-07,1.0671464622235918e-07,3.7465730760826314e-08,9.865194454081108e-09,2.0781030481026427e-09,3.6479364384170705e-10,5.488841073132002e-11,7.2264017562699396e-12,8.456896722680772e-13,8.90722577172408e-14,8.5286680047976e-15,7.485682390550633e-16,6.064841813048717e-17,4.562710097541469e-18,3.203782687860794e-19],[2.4385374269030727e-08,2.5683893426263265e-08,1.3525779310457756e-08,4.748675312290815e-09,1.2503854697003647e-09,2.6339367845026555e-10,4.623656166351836e-11,6.956950676729545e-12,9.15925965404477e-13,1.0718877189919134e-13,1.128965651122769e-14,1.0809845258230776e-15,9.487890518026527e-17,7.687015308583378e-18,5.783105882987271e-19,4.06070386105922e-20],[2.8530250671732478e-09,3.004948415362087e-09,1.5824808346205104e-09,5.55582602602841e-10,1.462918325274543e-10,3.081637209513484e-11,5.409556892200318e-12,8.1394504971796e-13,1.0716094451306107e-13,1.2540806213349284e-14,1.3208603104039438e-15,1.2647236476154414e-16,1.1100583974592816e-17,8.993607038865677e-19,6.766082762663943e-20,4.750917405718227e-21],[3.09953871979414e-10,3.264588899538487e-10,1.7192139938322417e-10,6.035873321357454e-11,1.5893207687717444e-11,3.347903935771972e-12,5.876965904445019e-13,8.842734073434571e-14,1.1642011161753828e-14,1.3624385878328014e-15,1.434988329630306e-16,1.374001217419131e-17,1.205972223569231e-18,9.770693418826712e-20,7.350701452121206e-21,5.1614171298388265e-22],[3.142862066059708e-11,3.3102192103993333e-11,1.7432440543969798e-11,6.120238852346414e-12,1.6115352659008948e-12,3.3946987702894585e-13,5.959110330402093e-14,8.966332087471702e-15,1.1804735659295116e-15,1.3814818726704153e-16,1.4550456678060174e-17,1.3932061172099989e-18,1.2228285228290827e-19,9.90726184803693e-21,7.4534447997914085e-22,5.233560078113367e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.16171687660546416, "-10": 4.0780518264307405e-08, "-11": 3.858380170363001e-09, "-12": 3.352386107783188e-10, "-13": 2.6920692753584684e-11, "-14": 2.000469674627604e-12, "-15": 1.2691241612070375e-13, "-2": 0.06988315278947799, "-3": 0.021827207177882307, "-4": 0.0053405554032479995, "-5": 0.0010699006456606473, "-6": 0.000181093003994375, "-7": 2.650601102221101e-05, "-8": 3.4150100537326025e-06, "-9": 3.9275925248991996e-07, "0": 0.2618399092009943, "1": 0.23464198070935527, "10": 1.608175889674755e-06, "11": 2.1972218213304403e-07, "12": 2.7568364322628387e-08, "13": 3.1969163976710662e-09, "14": 3.4305606408340737e-10, "15": 3.142862066059708e-11, "2": 0.14572989473957446, "3": 0.06572981538193677, "4": 0.023224092212297116, "5": 0.00671867838742523, "6": 0.0016422155363779794, "7": 0.0003471050549411479, "8": 6.457979043211401e-05, "9": 1.0725539587331088e-05} |
| Raw goal margin distribution | {"-1": 0.16171687660546416, "-10": 4.0780518264307405e-08, "-11": 3.858380170363001e-09, "-12": 3.352386107783188e-10, "-13": 2.6920692753584684e-11, "-14": 2.000469674627604e-12, "-15": 1.2691241612070375e-13, "-2": 0.06988315278947799, "-3": 0.021827207177882307, "-4": 0.0053405554032479995, "-5": 0.0010699006456606473, "-6": 0.000181093003994375, "-7": 2.650601102221101e-05, "-8": 3.4150100537326025e-06, "-9": 3.9275925248991996e-07, "0": 0.2618399092009943, "1": 0.23464198070935527, "10": 1.608175889674755e-06, "11": 2.1972218213304403e-07, "12": 2.7568364322628387e-08, "13": 3.1969163976710662e-09, "14": 3.4305606408340737e-10, "15": 3.142862066059708e-11, "2": 0.14572989473957446, "3": 0.06572981538193677, "4": 0.023224092212297116, "5": 0.00671867838742523, "6": 0.0016422155363779794, "7": 0.0003471050549411479, "8": 6.457979043211401e-05, "9": 1.0725539587331088e-05} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Sevilla", "away_goals": 1.0, "away_xg": 0.77, "date": "2026-11-01T00:00:00+00:00", "home": "Getafe", "home_goals": 3.0, "home_xg": 1.58, "source": "pipeline training history"}, {"away": "Osasuna", "away_goals": 0.0, "away_xg": 0.77, "date": "2026-10-26T00:00:00+00:00", "home": "Sevilla", "home_goals": 2.0, "home_xg": 1.14, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 1.0, "away_xg": 0.75, "date": "2026-10-18T00:00:00+00:00", "home": "Real Madrid", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 3.0, "away_xg": 2.53, "date": "2026-10-12T00:00:00+00:00", "home": "Levante", "home_goals": 3.0, "home_xg": 1.95, "source": "pipeline training history"}, {"away": "Barcelona", "away_goals": 3.0, "away_xg": 3.26, "date": "2026-09-19T00:00:00+00:00", "home": "Sevilla", "home_goals": 1.0, "home_xg": 0.45, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 1.0, "away_xg": 0.73, "date": "2026-09-16T00:00:00+00:00", "home": "La Coruna", "home_goals": 0.0, "home_xg": 0.14, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 0.0, "away_xg": 0.1, "date": "2026-09-11T00:00:00+00:00", "home": "Sevilla", "home_goals": 1.0, "home_xg": 0.93, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 1.0, "away_xg": 0.53, "date": "2026-09-06T00:00:00+00:00", "home": "Espanol", "home_goals": 1.0, "home_xg": 1.22, "source": "pipeline training history"}, {"away": "Ath Madrid", "away_goals": 3.0, "away_xg": 0.93, "date": "2026-08-29T00:00:00+00:00", "home": "Sevilla", "home_goals": 1.0, "home_xg": 0.89, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 3.0, "away_xg": 0.41, "date": "2026-08-22T00:00:00+00:00", "home": "Ath Bilbao", "home_goals": 1.0, "home_xg": 1.25, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 47.8% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 26.0% |
| Raw p over 1 5 | 73.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 51.1% |
| P home draw | 74.0% |
| P draw away | 52.2% |
| P home away | 73.8% |
| Raw p home draw | 74.0% |
| Raw p draw away | 52.2% |
| Raw p home away | 73.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4751 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.014493407444055235, "mu": 8.663289582047497, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,445.5951 |
| Elo away rating | 1,433.5816 |
| Elo rating diff | 72.0135 |
| Elo home expectancy | 0.6022 |
| Research p home | 0.4806 |
| Research p draw | 0.2568 |
| Research p away | 0.2626 |
| Research p over 1 5 | 0.7276 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.5209660292298808, 1.0532499170571128], "coverage": {"team_news": "dated news leads; absences and tactics require confirmation", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [{"headline": "Getafe vs. Sevilla - Game Highlights", "published_at_utc": "2026-11-01T15:07:45+00:00", "source": "ESPN league news; unconfirmed context lead", "url": "https://www.espn.com/video/clip/_/id/50348131/getafe-vs-sevilla-game-highlights"}], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:21:37.188231+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-06T13:21:37.269465+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:21:37.423948+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/La_liga/2026"}, {"observed_at_utc": "2026-11-06T13:21:37.582168+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/La_liga/2025"}, {"observed_at_utc": "2026-11-06T13:21:37.608096+00:00", "reason": "HTTPError", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Sevilla+FC_vs_Deportivo+Alav%C3%A9s&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 1.9658152096820078, "goals_for": 1.4771346844204023, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 1.2630268310800783, "results": "LWLDLWWDLW", "xg_against": 1.4461597878889831, "xg_for": 0.9735333845193156, "xg_matches": 10}, "venue": {"goals_against": 1.3961941158577094, "goals_for": 1.3041211947932392, "last_match": "2026-10-26T00:00:00+00:00", "matches": 4, "points_per_game": 1.6038058841422904, "results": "WLWL", "xg_against": 1.3069157769949158, "xg_for": 0.8587582632892911, "xg_matches": 4}}}, "goal_rates": [1.5209660292298808, 1.0532499170571128], "h2h": [], "margin_distribution": {"-1": 0.16422004256383768, "-10": 4.0780518264307405e-08, "-11": 3.858380170363001e-09, "-12": 3.352386107783188e-10, "-13": 2.6920692753584684e-11, "-14": 2.000469674627604e-12, "-15": 1.2691241612070375e-13, "-2": 0.06988315278947799, "-3": 0.021827207177882307, "-4": 0.0053405554032479995, "-5": 0.0010699006456606473, "-6": 0.000181093003994375, "-7": 2.650601102221101e-05, "-8": 3.4150100537326025e-06, "-9": 3.9275925248991996e-07, "0": 0.2568335772842473, "1": 0.2371451466677288, "10": 1.608175889674755e-06, "11": 2.1972218213304403e-07, "12": 2.7568364322628387e-08, "13": 3.1969163976710662e-09, "14": 3.4305606408340737e-10, "15": 3.142862066059708e-11, "2": 0.14572989473957446, "3": 0.06572981538193677, "4": 0.023224092212297116, "5": 0.00671867838742523, "6": 0.0016422155363779794, "7": 0.0003471050549411479, "8": 6.457979043211401e-05, "9": 1.0725539587331088e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:21:37.608589+00:00", "p_over_1_5": 0.7275962967518329, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
