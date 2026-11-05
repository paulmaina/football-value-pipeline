# La Liga — football model report

Fixtures in this report: **6**.

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
| Training sha256 | 2b6bb97105e3a6f1a8812b2b964ef5aceb0f8831f76069b5c6bb61fc3ea716cb |
| Training as of utc | 2026-11-05T13:32:13.282064+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 109, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 109, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 108, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-05T13:32:13.282064+00:00', 'observations': 583, 'observations_sha256': 'bd1b3a519db09934def0ee8a93db1e19ca3c6d977ffd04005cb961e04e46a3dd', 'eligible_training_matches': 176, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 183, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 30, 'retrospective_eligible_training_matches': 176, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '835e29ace60a9700f5989f01a4aa8ff703a7a15ee1bb5e477446b1fa6f2cfecf', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 114, 'tuning_matches': 22, 'audit_matches': 40, 'tuning_origin_utc': '2026-09-13T00:00:00+00:00', 'audit_origin_utc': '2026-10-09T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 17, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8357146014438204, 'audit_candidate_poisson_score': 0.8437651841527154, 'audit_gain': -0.008050582708895027, 'audit_gain_lower95': -0.03725049821585039, 'audit_baseline_briers': [0.5199253099278909, 0.20340070445316755, 0.22970209423243637, 0.28429820925953975], 'audit_candidate_briers': [0.5207453946703196, 0.21314479122702693, 0.23282815042185553, 0.28812038229266573], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2009, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1630, 'tuning_matches': 230, 'audit_matches': 129, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8432834464502666, 'audit_candidate_poisson_score': 0.8400225074412011, 'audit_gain': 0.0032609390090655443, 'audit_gain_lower95': -0.005259240284233485, 'audit_baseline_briers': [0.5723880944925321, 0.1848831628824439, 0.20353795326472862, 0.2524151023574783], 'audit_candidate_briers': [0.574670571206337, 0.1816626862987799, 0.20413573167809032, 0.24863999990406543], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1847.009 |
| Base scoring parameter | 0.089 |
| Home-advantage parameter | 0.289 |
| Dixon-Coles low-score adjustment | -0.021 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 2009, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 2.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261105T133213282064Z_dbf96f819426472aa72326fa3b02d2159fafd4f7915d3cd939461fb77a1fa37f.json |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 2, 'ANCHORED_MAIN': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 6} |
| Legacy comparison status | {'None': 6} |
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

## 2026-11-06 — Sevilla vs Alavés

The model's most likely 1X2 outcome is **Sevilla win** at **49.5%**. Expected goals are 1.52 for Sevilla and 1.05 for Alavés (2.57 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 43.2%; Under 3.5 goals: 77.8%; Double Chance 1X: 76.5%; Double Chance X2: 50.5%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 90.4%; BTTS Yes (both teams score): 47.5%; BTTS No (at least one team does not score): 52.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 49.5% | 2.02 |
| Draw | 27.1% | 3.70 |
| Alavés win | 23.5% | 4.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.52 |
| Alavés expected goals | 1.05 |
| Expected total goals | 2.57 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 69.5% |
| Under 1.5 | 30.5% |
| Over 2.5 | 43.2% |
| Under 2.5 | 56.8% |
| Over 3.5 | 22.2% |
| Under 3.5 | 77.8% |
| Over 4.5 | 9.6% |
| Under 4.5 | 90.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.35% |
| 2 | 1-1 | 12.74% |
| 3 | 2-0 | 9.65% |
| 4 | 2-1 | 9.46% |
| 5 | 0-0 | 9.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 49.5% | 50.2% | 2.05 | +1.4% |
| Draw | 27.1% | 27.4% | 3.50 | -5.3% |
| Alavés win | 23.5% | 22.4% | 4.26 | +0.0% |
| Over 2.5 | 43.2% | 43.0% | 2.28 | -1.6% |
| Under 2.5 | 56.8% | 57.0% | 1.73 | -1.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:00:00+00:00 |
| Fixture id | 9dd0014685fd62d9b2890d7c33a8c9ab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:31:12Z |
| Market best draw last update utc | 2026-11-05T13:32:59Z |
| Market best away last update utc | 2026-11-05T13:32:59Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sevilla |
| Matched away-team name | Alaves |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5209 |
| Dc lambda away | 1.0533 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:32:13.282064+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.5% |
| P btts no | 52.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.82 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.28 |
| Fair Over 2.5 odds | 2.32 |
| Fair Under 2.5 odds | 1.76 |
| Fair Over 3.5 odds | 4.50 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.38 |
| Fair Under 4.5 odds | 1.11 |
| Score matrix json | [[0.09243540749442164,0.07872866624008308,0.03977339127449259,0.013005243321119967,0.003189375140422194,0.0006257238583040733,0.00010230069360835872,1.4335988778248697e-05,1.7578620058751964e-06,1.9159729975905123e-07,1.8794747617868133e-08,1.6760652703427727e-09,1.3701142877440344e-10,1.0338572009814407e-11,7.244019912671681e-13],[0.13345920484070337,0.12743852122364327,0.05633835180059756,0.01842171235590662,0.004517697207288949,0.000886327510165573,0.00014490724278895132,2.030669131591917e-05,2.489982496599779e-06,2.7139441048348684e-07,2.6622449566626908e-08,2.3741187717601644e-09,1.9407442583215657e-10,1.4644416489027834e-11,1.0261034556345805e-12],[0.09646800513652071,0.09463034249544325,0.04337666976857939,0.013047025639753202,0.0031996217375113564,0.0006277341393098597,0.000102629357984042,1.4382046421021324e-05,1.7635095396144122e-06,1.9221284990526028e-07,1.8855130043187746e-08,1.681450013361139e-09,1.3745160932559312e-10,1.037178703695851e-11,7.267292983440392e-13],[0.045548445302497374,0.04468077237640023,0.02191481407206484,0.006696877047933802,0.0015107371142740096,0.00029639168000210857,4.845759681617852e-05,6.790643735389827e-06,8.326607116202305e-07,9.075544236616989e-08,8.902660091583885e-09,7.939153904351753e-10,6.489931143747522e-11,4.897155008787556e-12,3.431333492228948e-13],[0.01612965511107972,0.015822394018978274,0.007760493041163393,0.0025375533002868337,0.0005815820202278726,0.00010495847980052557,1.7159846378200303e-05,2.404708672417553e-06,2.9486253622457106e-07,3.2138396274516344e-08,3.152617743476486e-09,2.8114200934966836e-10,2.2982200676246383e-11,1.734184795829001e-12,1.2151068040452985e-13],[0.004569478010053893,0.004482431957671888,0.002198522042446734,0.0007188804673842886,0.00017629654709244545,3.2324334469942523e-05,4.8613277928817625e-06,6.812460231496137e-07,8.353358245963784e-08,9.104701498169221e-09,8.9312619232794e-10,7.964660252054699e-11,6.510781531876395e-12,4.912888239294764e-13,3.4423574358622333e-14],[0.0010787650211453873,0.0010582151385697652,0.0005190283599987561,0.0001697137180423091,4.1620191175796396e-05,8.165469867688581e-06,1.2476297440329234e-06,1.6082895660100494e-07,1.972065663739968e-08,2.1494432148671444e-09,2.1084974993473842e-10,1.8803016157029885e-11,1.5370690834826446e-12,1.1598375074104432e-13,8.126737417090898e-15],[0.00021829326205994172,0.000214134895024998,0.00010502787130180827,3.4342382633468696e-05,8.422044765296982e-06,1.6523218854253843e-06,2.7014100980810793e-07,3.5379221216828506e-08,3.990569199927589e-09,4.3495011590918174e-10,4.2666455451908726e-11,3.804880259396788e-12,3.1103328126885114e-13,2.3469866744777893e-14,1.64448418877893e-15],[3.865110001796648e-05,3.791481774034451e-05,1.859628061834364e-05,6.080677220614291e-06,1.4912109128219398e-06,2.9256083239946674e-07,4.783128480704345e-08,6.7028750055998154e-09,7.681161981210417e-10,7.701245688570836e-11,7.554541177872008e-12,6.736937552472377e-13,5.5071688195018935e-14,4.155584823830535e-15,2.911730864189728e-16],[6.083182752520768e-06,5.9673014541842475e-06,2.926813815543664e-06,9.570198720060362e-07,2.3469729195372167e-07,4.6045287427480285e-08,7.528024988522016e-09,1.0549457481782843e-09,1.2935620121270286e-10,1.3176514176826794e-11,1.188986977733545e-12,1.0603067520706906e-13,8.667570745060684e-15,6.540352516542156e-16,4.582687417638274e-17],[8.616727892615797e-07,8.452583947541145e-07,4.1457834273411887e-07,1.3556028415363407e-07,3.324448375418296e-08,6.522238910798305e-09,1.0663323055357262e-09,1.4943132276861888e-10,1.8323092243290493e-11,1.997116375072118e-12,1.8308769725756206e-13,1.501907001151728e-14,1.227747079754203e-15,9.264301312249014e-17,6.491301034534941e-18],[1.1095866124389653e-07,1.0884495954369744e-07,5.3385761351373604e-08,1.745626394958984e-08,4.280932921497655e-09,8.398766989905899e-10,1.3731291801004474e-10,1.9242454594068777e-11,2.3594870471727803e-12,2.571711235260964e-13,2.522721545321901e-14,2.102482651851864e-15,1.5809849633568326e-16,1.192975435429662e-17,8.358927907429429e-19],[1.3097592578372478e-08,1.2848090616190649e-08,6.301670764840607e-09,2.0605424631944663e-09,5.053225645708873e-10,9.913928931845526e-11,1.6208456696227112e-11,2.2713849253007993e-12,2.7851453587645104e-13,3.035655406352871e-14,2.9778278341589115e-15,2.655547132300315e-16,2.0287501164198554e-17,1.408191666526952e-18,9.866902763259548e-20],[1.4271171964204645e-09,1.3999313957750623e-09,6.866317348681523e-10,2.2451725884611475e-10,5.5060082020662097e-11,1.0802243525340447e-11,1.7660777841584434e-12,2.4749071000571466e-13,3.034701844815959e-14,3.3076582638297818e-15,3.244649186236761e-16,2.893491270043577e-17,2.3653098722930835e-18,1.6680170362865202e-19,1.0751003686057589e-20],[1.4439199549578052e-10,1.416414070968838e-10,6.947160794994153e-11,2.271607062779859e-11,5.570835482233519e-12,1.092942823734105e-12,1.7868714363124552e-13,2.504046449305348e-14,3.0704321705797876e-15,3.3466023556468893e-16,3.282851414443009e-17,2.927558994307843e-18,2.39315883294594e-19,1.8058234372603885e-20,1.1825051463076893e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.14973476550004367, "-10": 2.1311336664643082e-08, "-11": 1.880854616561111e-09, "-12": 1.5238257456177531e-10, "-13": 1.1364675465448987e-11, "-14": 7.244019912671681e-13, "-2": 0.06170897830358259, "-3": 0.018201622699581956, "-4": 0.004185426834255284, "-5": 0.0007858788588663841, "-6": 0.0001244648837314346, "-7": 1.7027374555264437e-05, "-8": 2.048928943408544e-06, "-9": 2.199678672588469e-07, "0": 0.27056266567971904, "1": 0.25272665370072206, "10": 9.770495076644461e-07, "11": 1.2451609966558313e-07, "12": 1.4566995582097483e-08, "13": 1.5687586035173482e-09, "14": 1.4439199549578052e-10, "2": 0.14967147243934367, "3": 0.06374779736740886, "4": 0.021166996153440695, "5": 0.0057390430562919295, "6": 0.0013124873174802062, "7": 0.0002592748357633126, "8": 4.505095238232967e-05, "9": 6.983943604114296e-06} |
| Raw goal margin distribution | {"-1": 0.16171512488955345, "-10": 4.079177045293639e-08, "-11": 3.8595453587593085e-09, "-12": 3.3534858705140915e-10, "-13": 2.6930225825934386e-11, "-14": 2.001230251245286e-12, "-15": 1.269640033172459e-13, "-2": 0.06988782202434891, "-3": 0.021829239338045908, "-4": 0.005341192546435791, "-5": 0.0010700562674666573, "-6": 0.00018112407523601255, "-7": 2.6511250689477238e-05, "-8": 3.41577422227746e-06, "-9": 3.928573823944515e-07, "0": 0.2618601413228539, "1": 0.2346302415565804, "10": 1.607742756210101e-06, "11": 2.196567514179158e-07, "12": 2.755937019587917e-08, "13": 3.1957824219366345e-09, "14": 3.4292462171194385e-10, "15": 3.141569105805871e-11, "2": 0.14572373959489993, "3": 0.0657251830729118, "4": 0.023221797675231616, "5": 0.0067178239491117115, "6": 0.0016419600452666327, "7": 0.0003470411876498333, "8": 6.456607137765078e-05, "9": 1.0722956012179026e-05} |
| Research history json | {"away": [{"away": "Alaves", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-10-31T00:00:00+00:00", "home": "Barcelona", "home_goals": 6.0, "home_xg": 3.26, "source": "pipeline training history"}, {"away": "Malaga", "away_goals": 1.0, "away_xg": 0.71, "date": "2026-10-23T00:00:00+00:00", "home": "Alaves", "home_goals": 1.0, "home_xg": 1.84, "source": "pipeline training history"}, {"away": "Alaves", "away_goals": 1.0, "away_xg": 1.06, "date": "2026-10-18T00:00:00+00:00", "home": "Celta", "home_goals": 2.0, "home_xg": 0.97, "source": "pipeline training history"}, {"away": "Ath Madrid", "away_goals": 2.0, "away_xg": 2.05, "date": "2026-10-10T00:00:00+00:00", "home": "Alaves", "home_goals": 1.0, "home_xg": 1.3, "source": "pipeline training history"}, {"away": "Alaves", "away_goals": 0.0, "away_xg": 0.05, "date": "2026-09-19T00:00:00+00:00", "home": "Ath Bilbao", "home_goals": 0.0, "home_xg": 1.62, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 1.0, "away_xg": 0.65, "date": "2026-09-15T00:00:00+00:00", "home": "Alaves", "home_goals": 0.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Alaves", "away_goals": 1.0, "away_xg": 1.98, "date": "2026-09-12T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Osasuna", "away_goals": 2.0, "away_xg": 1.63, "date": "2026-09-06T00:00:00+00:00", "home": "Alaves", "home_goals": 5.0, "home_xg": 1.19, "source": "pipeline training history"}, {"away": "Villarreal", "away_goals": 0.0, "away_xg": 1.4, "date": "2026-08-28T00:00:00+00:00", "home": "Alaves", "home_goals": 1.0, "home_xg": 0.81, "source": "pipeline training history"}, {"away": "Alaves", "away_goals": 1.0, "away_xg": 2.0, "date": "2026-08-20T00:00:00+00:00", "home": "Vallecano", "home_goals": 1.0, "home_xg": 0.42, "source": "pipeline training history"}], "h2h": [{"away": "Alaves", "away_goals": 1.0, "away_xg": null, "date": "2026-02-14T00:00:00+00:00", "home": "Sevilla", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 2.0, "away_xg": null, "date": "2025-09-20T00:00:00+00:00", "home": "Alaves", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alaves", "away_goals": 1.0, "away_xg": null, "date": "2025-04-20T00:00:00+00:00", "home": "Sevilla", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 1.0, "away_xg": null, "date": "2024-09-20T00:00:00+00:00", "home": "Alaves", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alaves", "away_goals": 3.0, "away_xg": null, "date": "2024-01-12T00:00:00+00:00", "home": "Sevilla", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 3.0, "away_xg": null, "date": "2023-08-21T00:00:00+00:00", "home": "Alaves", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Sevilla", "away_goals": 1.0, "away_xg": 0.77, "date": "2026-11-01T00:00:00+00:00", "home": "Getafe", "home_goals": 3.0, "home_xg": 1.58, "source": "pipeline training history"}, {"away": "Osasuna", "away_goals": 0.0, "away_xg": 0.77, "date": "2026-10-26T00:00:00+00:00", "home": "Sevilla", "home_goals": 2.0, "home_xg": 1.14, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 1.0, "away_xg": 0.75, "date": "2026-10-18T00:00:00+00:00", "home": "Real Madrid", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 3.0, "away_xg": 2.53, "date": "2026-10-12T00:00:00+00:00", "home": "Levante", "home_goals": 3.0, "home_xg": 1.95, "source": "pipeline training history"}, {"away": "Barcelona", "away_goals": 3.0, "away_xg": 3.26, "date": "2026-09-19T00:00:00+00:00", "home": "Sevilla", "home_goals": 1.0, "home_xg": 0.45, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 1.0, "away_xg": 0.73, "date": "2026-09-16T00:00:00+00:00", "home": "La Coruna", "home_goals": 0.0, "home_xg": 0.14, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 0.0, "away_xg": 0.1, "date": "2026-09-11T00:00:00+00:00", "home": "Sevilla", "home_goals": 1.0, "home_xg": 0.93, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 1.0, "away_xg": 0.53, "date": "2026-09-06T00:00:00+00:00", "home": "Espanol", "home_goals": 1.0, "home_xg": 1.22, "source": "pipeline training history"}, {"away": "Ath Madrid", "away_goals": 3.0, "away_xg": 0.93, "date": "2026-08-29T00:00:00+00:00", "home": "Sevilla", "home_goals": 1.0, "home_xg": 0.89, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 3.0, "away_xg": 0.41, "date": "2026-08-22T00:00:00+00:00", "home": "Ath Bilbao", "home_goals": 1.0, "home_xg": 1.25, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 47.8% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 26.0% |
| Raw p over 1 5 | 73.0% |
| Raw p under 3 5 | 74.2% |
| Raw p btts yes | 51.1% |
| P home draw | 76.5% |
| P draw away | 50.5% |
| P home away | 72.9% |
| Raw p home draw | 74.0% |
| Raw p draw away | 52.2% |
| Raw p home away | 73.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9313 |
| Totals anchor target over 2 5 | 0.4317 |
| Totals anchor reference over odds | 2.22 |
| Totals anchor reference under odds | 1.71 |
| Totals anchor reference last update utc | 2026-11-05T13:33:25Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4730 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.65, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.7, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.75, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.99, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.47, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 8.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.2, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.2, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.28, "under": 1.73}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:22:34Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.38, "under": 2.98}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.17, "draw": 3.47, "home": 2.05}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.28, "under": 1.73}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.86, "home_away": 1.35, "home_draw": 1.27}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.26, "draw": 3.5, "home": 1.95}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:24Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.93, "home_away": 1.33, "home_draw": 1.26}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.22, "under": 1.71}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.39, "under": 3.12}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.95 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.26 |
| Market reference 1x2 last update utc | 2026-11-05T13:32:59Z |
| Market reference home last update utc | 2026-11-05T13:32:59Z |
| Market reference draw last update utc | 2026-11-05T13:32:59Z |
| Market reference away last update utc | 2026-11-05T13:32:59Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.28 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-11-05T13:31:12Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:31:12Z |
| Market best over 2 5 last update utc | 2026-11-05T13:31:12Z |
| Market best under 2 5 last update utc | 2026-11-05T13:31:12Z |
| Home probability edge | -0.7% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | -0.0237 |
| Raw ev home | -0.0199 |
| Raw edge prob draw | -0.0124 |
| Raw ev draw | -0.0835 |
| Raw edge prob away | 0.0361 |
| Raw ev away | 0.1078 |
| Market p home draw | 76.9% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T13:31:12Z |
| Market reference home draw last update utc | 2026-11-05T13:33:24Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.2% |
| Market draw away odds | 1.93 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-05T13:33:24Z |
| Market reference draw away last update utc | 2026-11-05T13:33:24Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.9% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T13:31:12Z |
| Market reference home away last update utc | 2026-11-05T13:33:24Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.93 |
| Market reference dc home draw odds | 1.26 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 70.3% |
| Market over 1 5 odds | 1.39 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T13:33:25Z |
| Market reference over 1 5 odds | 1.39 |
| Market reference over 1 5 opposite odds | 3.12 |
| Market reference over 1 5 last update utc | 2026-11-05T13:33:25Z |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 78.4% |
| Market under 3 5 odds | 1.23 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-05T13:22:34Z |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 4.30 |
| Market reference under 3 5 last update utc | 2026-11-05T13:32:42Z |
| Market under 3 5 bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.014493407444055235, "mu": 8.663289582047497, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,445.5951 |
| Elo away rating | 1,433.5816 |
| Elo rating diff | 72.0135 |
| Elo home expectancy | 0.6022 |

</details>


---

## 2026-11-07 — CA Osasuna vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **43.5%**. Expected goals are 1.12 for CA Osasuna and 1.19 for Athletic Bilbao (2.32 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.5%; Double Chance 1X: 56.5%; Double Chance X2: 71.0%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 46.9%; BTTS No (at least one team does not score): 53.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CA Osasuna win | 29.0% | 3.45 |
| Draw | 27.5% | 3.64 |
| Athletic Bilbao win | 43.5% | 2.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CA Osasuna expected goals | 1.12 |
| Athletic Bilbao expected goals | 1.19 |
| Expected total goals | 2.32 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 67.6% |
| Under 1.5 | 32.4% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.5% |
| Under 3.5 | 79.5% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.41% |
| 2 | 1-1 | 12.88% |
| 3 | 0-0 | 9.69% |
| 4 | 1-0 | 9.26% |
| 5 | 1-2 | 9.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CA Osasuna win | 29.0% | 26.9% | 3.65 | +5.8% |
| Draw | 27.5% | 26.9% | 3.58 | -1.6% |
| Athletic Bilbao win | 43.5% | 46.2% | 2.18 | -5.1% |
| Over 2.5 | 41.2% | 45.3% | 2.17 | -10.5% |
| Under 2.5 | 58.8% | 54.7% | 1.81 | +6.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T17:30:00+00:00 |
| Fixture id | 71ca5141a1c532e390c6fa14e080d8bd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:31:12Z |
| Market best draw last update utc | 2026-11-05T13:32:59Z |
| Market best away last update utc | 2026-11-05T13:31:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Osasuna |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1205 |
| Dc lambda away | 1.1946 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:32:13.282064+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.9% |
| P btts no | 53.1% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.32 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.89 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.52 |
| Fair Under 4.5 odds | 1.10 |
| Score matrix json | [[0.09689973797089312,0.13405537274074344,0.08195786042597424,0.03263462285884944,0.009746032323232266,0.0023284508960024664,0.0004635804085260637,7.911089074155889e-05,1.1812872813357104e-05,1.5679140765746063e-06,1.8729729265068884e-07,2.0339864489905995e-08,2.0247716423360264e-09,1.8605525377823687e-10],[0.0925910077947495,0.12881783461608856,0.09183061872818477,0.03656583509516967,0.010920052984980888,0.002608939342080939,0.000519423951820507,8.864069910044651e-05,1.3235867966413432e-05,1.7567871954700922e-06,2.0985938604097223e-07,2.2790032966301636e-08,2.2686784614996237e-09,2.0846772943172315e-10],[0.05317910425268037,0.06352581688580716,0.042235631032992174,0.02048530332325527,0.006117748907446759,0.0014616079090058061,0.00029099724315643025,4.9659240740215394e-05,7.415139551246148e-06,9.842061169927944e-07,1.1756967035191108e-07,1.2767676079230257e-08,1.2709833183297151e-09,1.1679002159814733e-10],[0.019861711134447835,0.02372607516235356,0.014171151689778616,0.0062811999217888105,0.00228490049428892,0.0005458917461746161,0.00010868372579258669,1.854708740582912e-05,2.7694592050419303e-06,3.675883200210575e-07,4.391075900050003e-08,4.768562722285594e-09,4.746959144971758e-10,4.361957022341927e-11],[0.005563570147503456,0.006646037826104108,0.003969557102270651,0.0015806293414196335,0.0005254468256907706,0.0001529126570327628,3.04439797883455e-05,5.195323862869021e-06,7.757680319484863e-07,1.0296713057582977e-07,1.2300077585243377e-08,1.335747611503237e-09,1.3296961179028652e-10,1.2218511139306866e-11],[0.0012467531151435073,0.001489325764459903,0.0008895470986766945,0.00035420683177445907,0.00010578063814356205,2.813163039585637e-05,6.822260820332751e-06,1.1642319658929633e-06,1.7384362645171854e-07,2.307413897898091e-08,2.7563524210781033e-09,2.993307267698336e-10,2.979746337760355e-11,2.738074010297543e-12],[0.00023282312269960054,0.00027812200425792556,0.00016611719737186196,6.614584688306091e-05,1.9753853585443636e-05,4.71944649422969e-06,1.045920176403993e-06,2.1741282901442296e-07,3.246417873778735e-08,4.308946996352637e-09,5.147310803888711e-10,5.589808734383776e-11,5.564484570228725e-12,5.113177047780742e-13],[3.726704587770348e-05,4.451785274631889e-05,2.658970098738961e-05,1.0587695422293251e-05,3.1619186242940483e-06,7.554225155065599e-07,1.5040002730980795e-07,2.8569892063288044e-08,5.1964084338997766e-09,6.897155382837832e-10,8.239090071943637e-11,8.947378427728011e-12,8.906843072972958e-13,8.184453563331245e-14],[5.219535782373491e-06,6.23506693088506e-06,3.7240916868413783e-06,1.4828879995179564e-06,4.428509695835586e-07,1.0580272081227974e-07,2.1064678074823255e-08,3.5947279372349953e-09,5.974956728772388e-10,9.659995438181598e-11,1.153947795750481e-11,1.2531490157609697e-12,1.2474717282375764e-13,1.1462955334095864e-14],[6.498098167332404e-07,7.762390888017848e-07,4.636334412528447e-07,1.8461319538353795e-07,5.513304619101054e-08,1.3171984921165178e-08,2.622462067521495e-09,4.4752820930721317e-10,6.682510798931493e-11,9.873153390884156e-12,1.436615509388016e-12,1.5601167732598318e-13,1.5530487938092908e-14,1.4270887710023463e-15],[7.280868145668474e-08,8.697459332781623e-08,5.194833729436047e-08,2.0685195866929624e-08,6.177444991579536e-09,1.4758700616415474e-09,2.938367509840116e-10,5.014380822705509e-11,7.487495380359805e-12,9.938098539314714e-13,1.3214843465312196e-13,1.7480506181108815e-14,1.740131219986921e-15,1.5989978769584575e-16],[7.416301535048273e-09,8.859243116372368e-09,5.291464230794678e-09,2.1069966766524873e-09,6.292353309678198e-10,1.5033231181635502e-10,2.9930248752997396e-11,5.107654670943523e-12,7.626772298584315e-13,1.0122959786935376e-13,1.2092518270178131e-14,1.461782611904785e-15,1.7724998694904335e-16,1.628741267135963e-17],[6.924732977599305e-10,8.272033260054609e-10,4.940734500290586e-10,1.9673403652151595e-10,5.875282479321566e-11,1.4036796000186897e-11,2.7946406923742e-12,4.769108236891763e-13,7.121253282253968e-14,9.451988047711813e-15,1.1290999921186397e-15,1.2261651255193724e-16,1.3587089566029436e-17,1.520784761948041e-18],[5.968381523751926e-11,7.129610720424827e-11,4.258386366765167e-11,1.6956376404209358e-11,5.063867084816178e-12,1.2098221573481459e-12,2.40868231711571e-13,4.1104628262079046e-14,6.137761073712511e-15,8.146605942666215e-16,9.731638105366489e-17,1.0568236066130442e-17,1.0520357550480748e-18,1.0760832527372485e-19]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.24881615291161718, "-10": 2.1140192850554363e-07, "-11": 2.2725332973003767e-08, "-12": 2.2332393717677494e-09, "-13": 1.8605525377823687e-10, "-2": 0.12521897755211106, "-3": 0.04513034103872478, "-4": 0.012665315361851026, "-5": 0.0029004093280514624, "-6": 0.0005600164405524185, "-7": 9.337624164035819e-05, "-8": 1.3692133949587195e-05, "-9": 1.7910280531204452e-06, "0": 0.2747890570954202, "1": 0.17197925985897908, "10": 8.217895439949039e-08, "11": 8.286088724721387e-09, "12": 7.637694049641788e-10, "13": 5.968381523751926e-11, "2": 0.08124947414497613, "3": 0.02746671230083491, "4": 0.007230057126728451, "5": 0.0015530043477178903, "6": 0.000281256010941193, "7": 4.398707495870351e-05, "8": 6.0498901677932395e-06, "9": 7.422776721954576e-07} |
| Raw goal margin distribution | {"-1": 0.2139310912117764, "-10": 1.817624970093062e-07, "-11": 1.9539146571374658e-08, "-12": 1.9201299037409488e-09, "-13": 1.5996953172329113e-10, "-2": 0.10766275498866663, "-3": 0.03880287912257655, "-4": 0.010889585359293439, "-5": 0.0024937598514002826, "-6": 0.0004814998014476581, "-7": 8.028450337174096e-05, "-8": 1.1772439701266018e-05, "-9": 1.539918455097498e-06, "0": 0.287786352667363, "1": 0.2004916641842951, "10": 9.580338548956082e-08, "11": 9.659837583673481e-09, "12": 8.903945695538014e-10, "13": 6.957878206738587e-11, "2": 0.0947198069045221, "3": 0.03202041259731661, "4": 0.00842872673526992, "5": 0.0018104766029038654, "6": 0.0003278853842124615, "7": 5.12796826099921e-05, "8": 7.052900151260551e-06, "9": 8.653397270539656e-07} |
| Research history json | {"away": [{"away": "Sociedad", "away_goals": 1.0, "away_xg": 1.15, "date": "2026-11-01T00:00:00+00:00", "home": "Ath Bilbao", "home_goals": 2.0, "home_xg": 3.08, "source": "pipeline training history"}, {"away": "Getafe", "away_goals": 0.0, "away_xg": 0.41, "date": "2026-10-25T00:00:00+00:00", "home": "Ath Bilbao", "home_goals": 4.0, "home_xg": 0.74, "source": "pipeline training history"}, {"away": "Ath Bilbao", "away_goals": 1.0, "away_xg": 1.9, "date": "2026-10-21T00:00:00+00:00", "home": "Levante", "home_goals": 3.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Ath Bilbao", "away_goals": 0.0, "away_xg": 0.59, "date": "2026-10-17T00:00:00+00:00", "home": "Valencia", "home_goals": 0.0, "home_xg": 1.41, "source": "pipeline training history"}, {"away": "Alaves", "away_goals": 0.0, "away_xg": 0.05, "date": "2026-09-19T00:00:00+00:00", "home": "Ath Bilbao", "home_goals": 0.0, "home_xg": 1.62, "source": "pipeline training history"}, {"away": "Elche", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-09-12T00:00:00+00:00", "home": "Ath Bilbao", "home_goals": 1.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "Ath Madrid", "away_goals": 0.0, "away_xg": 1.03, "date": "2026-09-05T00:00:00+00:00", "home": "Ath Bilbao", "home_goals": 3.0, "home_xg": 1.41, "source": "pipeline training history"}, {"away": "Ath Bilbao", "away_goals": 2.0, "away_xg": 2.64, "date": "2026-08-30T00:00:00+00:00", "home": "Celta", "home_goals": 0.0, "home_xg": 0.57, "source": "pipeline training history"}, {"away": "Ath Bilbao", "away_goals": 0.0, "away_xg": 0.25, "date": "2026-08-27T00:00:00+00:00", "home": "Barcelona", "home_goals": 2.0, "home_xg": 3.91, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 3.0, "away_xg": 0.41, "date": "2026-08-22T00:00:00+00:00", "home": "Ath Bilbao", "home_goals": 1.0, "home_xg": 1.25, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 28.8% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 47.3% |
| P home draw | 56.5% |
| P draw away | 71.0% |
| P home away | 72.5% |
| Raw p home draw | 62.6% |
| Raw p draw away | 66.2% |
| Raw p home away | 71.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4125 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.12, "draw": 3.58, "home": 3.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.18, "draw": 3.54, "home": 3.65}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.17, "under": 1.81}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.58 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.12 |
| Market reference 1x2 last update utc | 2026-11-05T13:32:59Z |
| Market reference home last update utc | 2026-11-05T13:32:59Z |
| Market reference draw last update utc | 2026-11-05T13:32:59Z |
| Market reference away last update utc | 2026-11-05T13:32:59Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.18 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-11-05T13:32:59Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:32:59Z |
| Market best over 2 5 last update utc | 2026-11-05T13:31:12Z |
| Market best under 2 5 last update utc | 2026-11-05T13:31:12Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.6% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | 0.0686 |
| Raw ev home | 0.2332 |
| Raw edge prob draw | 0.0186 |
| Raw ev draw | 0.0303 |
| Raw edge prob away | -0.0872 |
| Raw ev away | -0.1839 |
| Count model | {"corners": {"alpha": 0.014493407444055235, "mu": 9.237924731367405, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,457.7140 |
| Elo away rating | 1,478.3170 |
| Elo rating diff | 39.3971 |
| Elo home expectancy | 0.5565 |

</details>


---

## 2026-11-07 — Espanyol vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Espanyol win** at **41.0%**. Expected goals are 1.29 for Espanyol and 1.14 for Deportivo La Coruña (2.43 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 46.1%; Under 3.5 goals: 75.0%; Double Chance 1X: 69.5%; Double Chance X2: 59.0%; Double Chance 12 (either team wins): 71.5%; Under 4.5 goals: 88.8%; BTTS Yes (both teams score): 52.0%; BTTS No (at least one team does not score): 48.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Espanyol win | 41.0% | 2.44 |
| Draw | 28.5% | 3.51 |
| Deportivo La Coruña win | 30.5% | 3.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Espanyol expected goals | 1.29 |
| Deportivo La Coruña expected goals | 1.14 |
| Expected total goals | 2.43 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 72.3% |
| Under 1.5 | 27.7% |
| Over 2.5 | 46.1% |
| Under 2.5 | 53.9% |
| Over 3.5 | 25.0% |
| Under 3.5 | 75.0% |
| Over 4.5 | 11.2% |
| Under 4.5 | 88.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.56% |
| 2 | 1-0 | 10.62% |
| 3 | 2-1 | 8.72% |
| 4 | 0-0 | 8.57% |
| 5 | 0-1 | 8.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Espanyol win | 41.0% | 41.5% | 2.35 | -3.7% |
| Draw | 28.5% | 28.7% | 3.43 | -2.3% |
| Deportivo La Coruña win | 30.5% | 29.7% | 3.41 | +4.1% |
| Over 2.5 | 46.1% | 46.1% | 2.10 | -3.1% |
| Under 2.5 | 53.9% | 53.9% | 1.86 | +0.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:15:00+00:00 |
| Fixture id | 262c2c99c38456b8a70cb9daa32f2f6d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:32:59Z |
| Market best draw last update utc | 2026-11-05T13:31:12Z |
| Market best away last update utc | 2026-11-05T13:31:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Espanol |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.2896 |
| Dc lambda away | 1.1381 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:32:13.282064+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 52.0% |
| P btts no | 48.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.67 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.60 |
| Fair Over 2.5 odds | 2.17 |
| Fair Under 2.5 odds | 1.86 |
| Fair Over 3.5 odds | 4.00 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.89 |
| Fair Under 4.5 odds | 1.13 |
| Score matrix json | [[0.0856663130033177,0.08557915983279164,0.05232485894047299,0.020737254925982385,0.0061639020712087175,0.0014657171888588824,0.00029044465298357975,4.9332122432019494e-05,7.331692953604416e-06,9.685592972860184e-07,1.1515708670099058e-07,1.244693550571668e-08,1.233234450392647e-09,1.127890012472483e-10,9.578624983034206e-12],[0.10619338404334662,0.13557276678073488,0.07049234834161663,0.027937348088301242,0.00830404401933643,0.0019746225549289826,0.0003912886927296011,6.646051665166252e-05,9.877298555304745e-06,1.3048486084113701e-06,1.551402838747642e-07,1.6768582490643688e-08,1.661420483958876e-09,1.519499856477241e-10,1.2904378198246415e-11],[0.0733255438697263,0.08718057878814457,0.05319461630639468,0.018818677327176046,0.00559362772789436,0.0013301113830390058,0.00026357317906399206,4.476799350861713e-05,6.653376468981977e-06,8.789497430069565e-07,1.0450293755362681e-07,1.1295364976237642e-08,1.119137575032588e-09,1.0235394357172236e-10,8.692425947269321e-12],[0.03292819694416878,0.039150057627160194,0.023273776799998664,0.009467243309507647,0.00251192239069793,0.000597311213350194,0.00011836242994445844,2.0103898713196368e-05,2.987822239730965e-06,3.947087019658492e-07,4.6928984463089804e-08,5.072393368873185e-09,5.025695076161196e-10,4.59639388141451e-11,3.903495267935685e-12],[0.011090263673192038,0.01318579522110028,0.007838641205306373,0.003106590332764663,0.0009477677429404932,0.000201175268182457,3.98646351426243e-05,6.771021746697162e-06,1.006302789777002e-06,1.3293845351832524e-07,1.5805748869069653e-08,1.7083893178340714e-09,1.6926612662756466e-10,1.5480720118737218e-11,1.314702771058665e-12],[0.0029881732923175775,0.0035527957024956785,0.002112052426163356,0.0008370432422611165,0.0002488011355929328,6.072398751388476e-05,1.0741172757607527e-05,1.8243918216381279e-06,2.7113937134470495e-07,3.5819088529490784e-08,4.258719001406636e-09,4.6031036617933633e-10,4.560725820299219e-11,4.1711428842286045e-12,3.542350140249354e-13],[0.0006709473498590887,0.0007977244383077416,0.00047422817871406025,0.00018794490485422226,5.586438477218971e-05,1.3284018477205985e-05,2.7018183626241405e-06,4.0963851091893265e-07,6.08800845365614e-08,8.04261338691992e-09,9.562284205987912e-10,1.0335545836471821e-10,1.0240393053611655e-11,9.365645798561488e-13,7.953790514705801e-14],[0.0001291291565338491,0.00015352841603257118,9.126898665713622e-05,3.617149250795494e-05,1.075154538941137e-05,2.5566150633159695e-06,5.066155875919741e-07,8.83198731100172e-08,1.1716856721420306e-08,1.5478649452880682e-09,1.8403376871754404e-10,1.9891580411798888e-11,1.970845130941608e-12,1.802493060919049e-13,1.5307702767237884e-14],[2.1745442003481453e-05,2.585429469484301e-05,1.536976240953781e-05,6.091305121356637e-06,1.8105679072716407e-06,4.305357990160124e-07,8.531442606575947e-08,1.4490684089582682e-08,2.210430324268939e-09,2.6066156010366654e-10,3.0991417831188585e-11,3.3497563200528932e-12,3.318917248677321e-13,3.0354111627468385e-14,2.5778280573237293e-15],[3.255064829798769e-06,3.8701170271435615e-06,2.3006923958427684e-06,9.118045549465818e-07,2.710230454721832e-07,6.444669816883766e-08,1.27706756991493e-08,2.1691035818988433e-09,3.223701041640917e-10,4.371094326545458e-11,4.6390905363868735e-12,5.014234240009764e-13,4.968071381327834e-14,4.543692475073147e-15,3.8587385095780315e-16],[4.385241900370145e-07,5.213843727903594e-07,3.0995059151360745e-07,1.2283882958937235e-07,3.6512379234057075e-08,8.682295927358418e-09,1.7204727125330537e-09,2.922228714619431e-10,4.342988426115179e-11,5.737340399738717e-12,7.001458935594504e-13,6.755204961285158e-14,6.693014094830007e-15,6.121288412347563e-16,5.19851452415451e-17],[5.3707480859635706e-08,6.385563637843515e-08,3.796065494071089e-08,1.5044470154393086e-08,4.471789592011695e-09,1.0633489621107012e-09,2.107118771944943e-10,3.5789483527614206e-11,5.3189988846342174e-12,7.026707002826293e-13,8.354419908149137e-14,9.268331165538159e-15,8.197151595240692e-16,7.496940595562516e-17,6.3667894644762965e-18],[6.029585372947407e-09,7.168889788257191e-09,4.261734233564397e-09,1.688999665125751e-09,5.020350365223789e-10,1.1937914878260742e-10,2.3656020209897276e-11,4.017983024514334e-12,5.971488023676333e-13,7.888683119388429e-14,9.379268450383682e-15,1.0137730367897948e-15,1.0309495620740821e-16,8.416600934048349e-18,7.147812560408801e-19],[6.248532151932247e-10,7.429207078908464e-10,4.4164866627305554e-10,1.7503307540004384e-10,5.202649723115424e-11,1.2371405383614129e-11,2.4515019479033663e-12,4.1638843405783183e-13,6.188325167138383e-14,8.17513760217451e-15,9.71984918511533e-16,1.0505852431518888e-16,1.040913174438791e-17,9.771226519312546e-19,7.407364493102287e-20],[6.012898676200925e-11,7.149050100698853e-11,4.249940011844168e-11,1.6843254091904566e-11,5.006456696103282e-12,1.190487705674608e-12,2.359055288319812e-13,4.00686337695724e-14,5.95496210960214e-15,7.866851425366327e-16,9.353311606147325e-17,1.0109674503044336e-17,1.0016601173585473e-18,9.160970502413537e-20,7.985302585965961e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.177614445953959, "-10": 1.3309208540825207e-07, "-11": 1.4214613428515213e-08, "-12": 1.3938768619876404e-09, "-13": 1.2569337944549471e-10, "-14": 9.578624983034206e-12, "-2": 0.08649489745643212, "-3": 0.03049682314946753, "-4": 0.008423244802249685, "-5": 0.001904898999866395, "-6": 0.0003639695312886456, "-7": 6.013705466324261e-05, "-8": 8.746290409745702e-06, "-9": 1.135513350599769e-06, "0": 0.2849122235234958, "1": 0.22001693655278834, "10": 5.068216001811102e-07, "11": 6.133486256825785e-08, "12": 6.815005480956695e-09, "13": 6.963437162002132e-10, "14": 6.012898676200925e-11, "2": 0.12120979447196117, "3": 0.0484251846457725, "4": 0.015155335818382788, "5": 0.0038835379425377417, "6": 0.0008407949326627041, "7": 0.00015741157611443563, "8": 2.594106873464045e-05, "9": 3.816152074179902e-06} |
| Raw goal margin distribution | {"-1": 0.19186191252103355, "-10": 1.0124056792445168e-07, "-11": 1.0360578240352137e-08, "-12": 9.733658496234862e-10, "-13": 8.414987538250958e-11, "-14": 6.191707464437794e-12, "-2": 0.09076948271818432, "-3": 0.030902912354356535, "-4": 0.008216935324117894, "-5": 0.0017858564834996272, "-6": 0.00032758795496639666, "-7": 5.1927184231351386e-05, "-8": 7.242037305792193e-06, "-9": 9.01293482189562e-07, "0": 0.2791003468599086, "1": 0.21775394356586364, "10": 3.53223139697003e-07, "11": 4.095887560135242e-08, "12": 4.360231956615657e-09, "13": 4.2712640766666787e-10, "14": 3.561089039300044e-11, "2": 0.1165410093715326, "3": 0.0449580827454064, "4": 0.01354527099297293, "5": 0.003335752665387227, "6": 0.0006933374664272335, "7": 0.00012453200348373574, "8": 1.9679606788713523e-05, "9": 2.7751812131165586e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 39.7% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 70.0% |
| Raw p under 3 5 | 77.3% |
| Raw p btts yes | 49.5% |
| P home draw | 69.5% |
| P draw away | 59.0% |
| P home away | 71.5% |
| Raw p home draw | 67.6% |
| Raw p draw away | 60.3% |
| Raw p home away | 72.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0447 |
| Totals anchor target over 2 5 | 0.4613 |
| Totals anchor reference over odds | 2.10 |
| Totals anchor reference under odds | 1.81 |
| Totals anchor reference last update utc | 2026-11-05T13:32:59Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4358 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.25, "draw": 3.36, "home": 2.35}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.1, "under": 1.81}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.41, "draw": 3.43, "home": 2.32}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.1, "under": 1.86}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.35 |
| Reference draw odds | 3.36 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-11-05T13:32:59Z |
| Market reference home last update utc | 2026-11-05T13:32:59Z |
| Market reference draw last update utc | 2026-11-05T13:32:59Z |
| Market reference away last update utc | 2026-11-05T13:32:59Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-11-05T13:32:59Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:32:59Z |
| Market best over 2 5 last update utc | 2026-11-05T13:32:59Z |
| Market best under 2 5 last update utc | 2026-11-05T13:31:12Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0182 |
| Raw ev home | -0.0671 |
| Raw edge prob draw | -0.0083 |
| Raw ev draw | -0.0427 |
| Raw edge prob away | 0.0265 |
| Raw ev away | 0.1046 |
| Count model | {"corners": {"alpha": 0.014493407444055235, "mu": 9.554886460393718, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,436.9009 |
| Elo away rating | 1,445.5717 |
| Elo rating diff | 51.3291 |
| Elo home expectancy | 0.5733 |

</details>


---

## 2026-11-07 — Málaga vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **Málaga win** at **39.9%**. Expected goals are 1.69 for Málaga and 1.59 for Real Racing Club de Santander (3.28 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 57.6%; Under 3.5 goals: 64.5%; Double Chance 1X: 65.8%; Double Chance X2: 60.1%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 81.5%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Málaga win | 39.9% | 2.51 |
| Draw | 25.9% | 3.86 |
| Real Racing Club de Santander win | 34.2% | 2.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Málaga expected goals | 1.69 |
| Real Racing Club de Santander expected goals | 1.59 |
| Expected total goals | 3.28 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.6% |
| Under 2.5 | 42.4% |
| Over 3.5 | 35.5% |
| Under 3.5 | 64.5% |
| Over 4.5 | 18.5% |
| Under 4.5 | 81.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.94% |
| 2 | 2-1 | 8.68% |
| 3 | 1-2 | 7.82% |
| 4 | 1-0 | 7.43% |
| 5 | 0-1 | 6.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 39.9% | 39.6% | 2.48 | -1.1% |
| Draw | 25.9% | 26.9% | 3.72 | -3.7% |
| Real Racing Club de Santander win | 34.2% | 33.4% | 2.92 | -0.0% |
| Over 2.5 | 57.6% | 57.0% | 1.73 | -0.4% |
| Under 2.5 | 42.4% | 43.0% | 2.28 | -3.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T13:00:00+00:00 |
| Fixture id | de935794b7d93f3607ac9ad54d18f4c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:31:12Z |
| Market best draw last update utc | 2026-11-05T13:31:12Z |
| Market best away last update utc | 2026-11-05T13:31:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Malaga |
| Matched away-team name | Santander |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6933 |
| Dc lambda away | 1.5891 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:32:13.282064+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.53 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.13 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.40 |
| Fair Under 4.5 odds | 1.23 |
| Score matrix json | [[0.05396910285020025,0.06675899707683622,0.050308842323273935,0.02446648768402405,0.008924013035511224,0.002603986634664385,0.0006331929337291229,0.0001319734526570864,2.406828530239527e-05,3.901675985987392e-06,5.692457014502842e-07,7.550150937079752e-08,9.17958287171352e-09,1.0302156756769688e-09,1.0736152636749545e-10,1.044253590941075e-11],[0.07425670791559251,0.11936220601983823,0.07821309507528366,0.038037045557368324,0.013873797284272078,0.004048311287368928,0.0009843991004309565,0.0002051737174502015,3.741797663637413e-05,6.065775731512084e-06,8.849829595090997e-07,1.1737910192407137e-07,1.4271121233187864e-08,1.6016340839648785e-09,1.6691056445407078e-10,1.6234582554326923e-11],[0.0595079043762508,0.08682068652075114,0.0663204399261705,0.029567317823024603,0.010784511985758694,0.003146871812103392,0.0007652024661916292,0.00015948758437697326,2.908609728464747e-05,4.715106451322818e-06,6.879233665059884e-07,9.124223928316942e-08,1.109336361458917e-08,1.2449974308692041e-09,1.2974450657033073e-10,1.261962003289525e-11],[0.030838166597719673,0.04499218756094941,0.032821292003613105,0.0167143155381881,0.005588746247711243,0.0016307708735588055,0.00039654296989192903,8.26496034239081e-05,1.5072987750840908e-05,2.443460911554232e-06,3.564954203166717e-07,4.728352317656688e-08,5.748799237035674e-09,6.451821583923908e-10,6.723615544343714e-11,6.5397353352214126e-12],[0.011985708399709423,0.017486877459519556,0.012756479345503962,0.0062038049453166004,0.0023694760412382265,0.0006338231585615914,0.00015412227539593303,3.212298768967151e-05,5.858339059214046e-06,9.49687131340123e-07,1.3855720443716097e-07,1.8377438850308934e-08,2.2343556347696966e-09,2.507595641486075e-10,2.6132323739445754e-11,2.5417646179081166e-12],[0.003726737914529269,0.005437226325037137,0.0039663951138634145,0.0019289602527470188,0.0007035773447668884,0.0002149789912839462,4.792151686298909e-05,9.988058457517462e-06,1.8215439221489833e-06,2.9528793136595736e-07,4.3081841296895676e-08,5.714130183331499e-09,6.947322244916466e-10,7.79691232239645e-11,8.125370518517441e-12,7.903154536611976e-13],[0.0009656344470446353,0.001408838817284245,0.001027731984480005,0.0004998125732884345,0.00018230380988648704,5.319542704652877e-05,1.3544944433425534e-05,2.5880041813706716e-06,4.719799455642764e-07,7.65120072468356e-08,1.1162928800601565e-08,1.4805873303863199e-09,1.8001195222922395e-10,2.0202566672960675e-11,2.105363416378699e-12,2.0477850699177922e-13],[0.00021446175641411596,0.00031289485186022865,0.00022825325586625297,0.00011100544587380687,4.0488608695453744e-05,1.1814392861101187e-05,2.8728219939244152e-06,6.269961230334446e-07,1.0482398223028049e-07,1.699286879330585e-08,2.4792211220609776e-09,3.2882977649663305e-10,3.997960052975286e-11,4.486871761893719e-12,4.675888868178794e-13,4.548010732190386e-14],[4.167686277852813e-05,6.0805600136492725e-05,4.435699764167349e-05,2.1571952093960712e-05,7.868247546362438e-06,2.2959190408426935e-06,5.582823251560611e-07,1.163601835768288e-07,2.222125530780264e-08,3.302264575063073e-09,4.817929323596779e-10,6.390227190940887e-11,7.76933077989661e-12,8.719444522510164e-13,9.086765957023933e-14,8.838257336415992e-15],[7.1992566987872994e-06,1.0503552688998416e-05,7.662222900674584e-06,3.7263366353567476e-06,1.3591602169501642e-06,3.965968029430408e-07,9.643762752855326e-08,2.010004533064783e-08,3.6656889387150045e-09,6.222533996100636e-10,8.322485821811381e-11,1.1038471430929197e-11,1.3420733455753742e-12,1.5061958891187554e-13,1.5696469533719367e-14,1.5267196015430496e-15],[1.1192389302767407e-06,1.6329442840564691e-06,1.1912143880544706e-06,5.793182829986121e-07,2.1130306793342303e-07,6.165727936217583e-08,1.4992762668355252e-08,3.124871660455974e-09,5.698896341876192e-10,9.238400959754654e-11,1.4114028359332127e-11,1.7161059083119897e-12,2.086466420773319e-13,2.3416210120809665e-14,2.4402657809105235e-15,2.3735283865505337e-16],[1.5818498990547115e-07,2.3078832240565553e-07,1.6835747118182988e-07,8.187658083473898e-08,2.986401988338543e-08,8.714185907644429e-09,2.118966689947513e-09,4.4164635333306337e-10,8.054400503108967e-11,1.3056875730726667e-11,1.9049686367551466e-12,2.6457531577289245e-13,2.948858021106585e-14,3.3094747344687184e-15,3.4488919879203373e-16,3.354570268334134e-17],[2.049364333652446e-08,2.9899762097798987e-08,2.1811538310312732e-08,1.0607513685362756e-08,3.869030635907432e-09,1.1289656374233259e-09,2.7452255496371966e-10,5.721745692491532e-11,1.0434871936893504e-11,1.6915824597184464e-12,2.467980548107297e-13,3.273388907551426e-14,4.167451350939844e-15,4.2875872660213195e-16,4.4682091738839235e-17,4.346010747772669e-18],[2.450817483946049e-09,3.5756872758936475e-09,2.6084234298838537e-09,1.2685435954158117e-09,4.6269410337132104e-10,1.3501204629828512e-10,3.282992030233732e-11,6.842587309431243e-12,1.2478975146453238e-12,2.0229491651324483e-13,2.9514370763738987e-14,3.914618125555137e-15,4.759449419503127e-16,5.593292636672756e-17,5.3434935826008205e-18,5.197357517721426e-19],[2.721561062087902e-10,3.970696032658764e-10,2.8965778507421244e-10,1.4086805229110493e-10,5.138082552624643e-11,1.499269245976664e-11,3.645666531741504e-12,7.598492873202808e-13,1.3857536546812652e-13,2.2464258209645188e-14,3.277484462583743e-15,4.347068818156399e-16,5.285229235528712e-17,5.931561470800793e-18,6.472844564668292e-19,5.771513357741267e-20],[2.8207329536554328e-11,4.115385579361922e-11,3.002127238750466e-11,1.460011912831896e-11,5.3253108947963976e-12,1.5539016292671808e-12,3.7785122176288083e-13,7.875376946022332e-14,1.4362496046328454e-14,2.3282840974642142e-15,3.3969138365064677e-16,4.5054731411297993e-17,5.4778195058544094e-18,6.147703661840637e-19,6.406686137410397e-20,6.525238168139445e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18081259711367934, "-10": 6.983902717865302e-07, "-11": 9.108740595491593e-08, "-12": 1.091750119758395e-08, "-13": 1.2097458601639348e-09, "-14": 1.2359610892182237e-10, "-15": 1.044253590941075e-11, "-2": 0.10092577053967099, "-3": 0.04191772333839976, "-4": 0.013826341519167269, "-5": 0.0037639405976506017, "-6": 0.0008700406653013649, "-7": 0.00017448212401516863, "-8": 3.0871582399191424e-05, "-9": 4.883909073729871e-06, "0": 0.2589647141653672, "1": 0.2008622570992754, "10": 1.3731602693152803e-06, "11": 1.908393687963399e-07, "12": 2.437358851662064e-08, "13": 2.87790835959943e-09, "14": 3.133099620024094e-10, "15": 2.8207329536554328e-11, "2": 0.11938022870376655, "3": 0.0528341359168921, "4": 0.01856995244449919, "5": 0.005386824934724889, "6": 0.0013268329319417811, "7": 0.0002835399243239348, "8": 5.345751420351826e-05, "9": 9.011644032358014e-06} |
| Raw goal margin distribution | {"-1": 0.18308179236289635, "-10": 1.3533302872305102e-06, "-11": 1.9166531272687773e-07, "-12": 2.4956046690285953e-08, "-13": 3.0043265351789747e-09, "-14": 3.325395336250951e-10, "-15": 2.9870784571246934e-11, "-2": 0.10708206360826816, "-3": 0.0472880180995618, "-4": 0.016713016582429296, "-5": 0.004897782317452141, "-6": 0.0012223382270478134, "-7": 0.0002651926479145907, "-8": 5.083150166369014e-05, "-9": 8.72054658298107e-06, "0": 0.23477849593763023, "1": 0.19522479901622525, "10": 2.5542870132596224e-06, "11": 3.854748121321403e-07, "12": 5.3482889444562414e-08, "13": 6.860768980661851e-09, "14": 8.09199368020875e-10, "15": 7.745428882561371e-11, "2": 0.12158777490265683, "3": 0.057215128907634305, "4": 0.021547713954761665, "5": 0.00672871952592239, "6": 0.0017894144099730165, "7": 0.0004136829344990695, "8": 8.449395809493322e-05, "9": 1.5446248264653055e-05} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Malaga", "away_goals": 1.0, "away_xg": 1.16, "date": "2026-10-31T00:00:00+00:00", "home": "Betis", "home_goals": 2.0, "home_xg": 1.8, "source": "pipeline training history"}, {"away": "Malaga", "away_goals": 1.0, "away_xg": 0.71, "date": "2026-10-23T00:00:00+00:00", "home": "Alaves", "home_goals": 1.0, "home_xg": 1.84, "source": "pipeline training history"}, {"away": "Sociedad", "away_goals": 5.0, "away_xg": 2.44, "date": "2026-10-18T00:00:00+00:00", "home": "Malaga", "home_goals": 2.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Espanol", "away_goals": 1.0, "away_xg": 0.99, "date": "2026-10-09T00:00:00+00:00", "home": "Malaga", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Malaga", "away_goals": 0.0, "away_xg": 0.52, "date": "2026-09-20T00:00:00+00:00", "home": "Getafe", "home_goals": 1.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Villarreal", "away_goals": 3.0, "away_xg": 3.33, "date": "2026-09-17T00:00:00+00:00", "home": "Malaga", "home_goals": 1.0, "home_xg": 0.63, "source": "pipeline training history"}, {"away": "Malaga", "away_goals": 1.0, "away_xg": 0.42, "date": "2026-09-13T00:00:00+00:00", "home": "Celta", "home_goals": 1.0, "home_xg": 1.9, "source": "pipeline training history"}, {"away": "Levante", "away_goals": 0.0, "away_xg": 0.98, "date": "2026-09-06T00:00:00+00:00", "home": "Malaga", "home_goals": 0.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Malaga", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-08-30T00:00:00+00:00", "home": "Real Madrid", "home_goals": 4.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "La Coruna", "away_goals": 1.0, "away_xg": 1.11, "date": "2026-08-24T00:00:00+00:00", "home": "Malaga", "home_goals": 1.0, "home_xg": 1.97, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 40.5% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 58.4% |
| Raw p btts yes | 65.2% |
| P home draw | 65.8% |
| P draw away | 60.1% |
| P home away | 74.1% |
| Raw p home draw | 63.9% |
| Raw p draw away | 59.5% |
| Raw p home away | 76.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9181 |
| Totals anchor target over 2 5 | 0.5758 |
| Totals anchor reference over odds | 1.69 |
| Totals anchor reference under odds | 2.26 |
| Totals anchor reference last update utc | 2026-11-05T13:33:25Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6293 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.3, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.5, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.47, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.73, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.33, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.33, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.73, "under": 2.28}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:27:26Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.2, "under": 4.35}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.92, "draw": 3.72, "home": 2.48}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.73, "under": 2.28}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.61, "home_away": 1.32, "home_draw": 1.46}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.9, "draw": 3.58, "home": 2.46}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:23Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.6, "home_away": 1.32, "home_draw": 1.45}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:25Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.69, "under": 2.26}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.46 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-11-05T13:32:59Z |
| Market reference home last update utc | 2026-11-05T13:32:59Z |
| Market reference draw last update utc | 2026-11-05T13:32:59Z |
| Market reference away last update utc | 2026-11-05T13:32:59Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-11-05T13:31:12Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:31:12Z |
| Market best over 2 5 last update utc | 2026-11-05T13:31:12Z |
| Market best under 2 5 last update utc | 2026-11-05T13:31:12Z |
| Home probability edge | +0.3% |
| Draw probability edge | -1.0% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | 0.0084 |
| Raw ev home | 0.0034 |
| Raw edge prob draw | -0.0346 |
| Raw ev draw | -0.1266 |
| Raw edge prob away | 0.0261 |
| Raw ev away | 0.0530 |
| Market p home draw | 66.6% |
| Market home draw odds | 1.46 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T13:31:12Z |
| Market reference home draw last update utc | 2026-11-05T13:33:23Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.3% |
| Market draw away odds | 1.61 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T13:31:12Z |
| Market reference draw away last update utc | 2026-11-05T13:33:23Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.1% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-05T13:33:23Z |
| Market reference home away last update utc | 2026-11-05T13:33:23Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.60 |
| Market reference dc home draw odds | 1.45 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-05T13:27:26Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-11-05T13:32:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.9% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T13:33:25Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.67 |
| Market reference under 3 5 last update utc | 2026-11-05T13:33:25Z |
| Market under 3 5 bookmakers | 2 |
| Count model | {"corners": {"alpha": 0.014493407444055235, "mu": 10.72822899303499, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,392.6833 |
| Elo away rating | 1,397.9822 |
| Elo rating diff | 54.7011 |
| Elo home expectancy | 0.5781 |

</details>


---

## 2026-11-07 — Valencia vs Real Madrid

The model's most likely 1X2 outcome is **Real Madrid win** at **71.1%**. Expected goals are 0.86 for Valencia and 1.82 for Real Madrid (2.68 combined). The most likely exact score is 0-1 at 14.6%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 53.1%; Under 3.5 goals: 70.6%; Double Chance 1X: 28.9%; Double Chance X2: 87.8%; Double Chance 12 (either team wins): 83.4%; Under 4.5 goals: 85.4%; BTTS Yes (both teams score): 46.5%; BTTS No (at least one team does not score): 53.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 12.2% | 8.18 |
| Draw | 16.6% | 6.01 |
| Real Madrid win | 71.1% | 1.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 0.86 |
| Real Madrid expected goals | 1.82 |
| Expected total goals | 2.68 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 76.3% |
| Under 1.5 | 23.7% |
| Over 2.5 | 53.1% |
| Under 2.5 | 46.9% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.6% |
| Under 4.5 | 85.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.58% |
| 2 | 0-2 | 13.50% |
| 3 | 1-2 | 11.62% |
| 4 | 0-3 | 8.19% |
| 5 | 1-1 | 7.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 12.2% | 10.1% | 10.60 | +29.6% |
| Draw | 16.6% | 13.9% | 6.61 | +9.9% |
| Real Madrid win | 71.1% | 76.0% | 1.32 | -6.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T20:00:00+00:00 |
| Fixture id | 5b386dfdf6f76705116fbb4120ee8493 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:31:12Z |
| Market best draw last update utc | 2026-11-05T13:32:59Z |
| Market best away last update utc | 2026-11-05T13:31:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8607 |
| Dc lambda away | 1.8193 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:32:13.282064+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 46.5% |
| P btts no | 53.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.58 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.21 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.86 |
| Fair Under 4.5 odds | 1.17 |
| Score matrix json | [[0.05106058208225907,0.1457518442610292,0.13497205701853457,0.08185098583642263,0.03722761601763018,0.013545546265021626,0.004107206854425588,0.0010674556459892653,0.00024275107073332583,4.907043944570296e-05,8.927323031401346e-06,1.4764878149423022e-06,2.238463017791484e-07,3.1326211367549324e-08,4.070812887803791e-09,4.937318958939772e-10,5.614001239010891e-11],[0.040506765844441586,0.07905498230546426,0.11617479409817885,0.07045177821490532,0.0320430074279771,0.011659087688573544,0.0035352051466919407,0.0009187934348863925,0.0002089436605065884,4.22365067617578e-05,7.684034295176822e-06,1.270860589061313e-06,1.9267171734116997e-07,2.696347848504165e-08,3.50387968813334e-09,4.249709355567547e-10,4.832151575784677e-11],[0.01811051121390639,0.0329482241644194,0.03032462555700838,0.030320056642699204,0.013790223963618124,0.005017676034257382,0.001521432432326938,0.00039541754224738297,8.992226714800437e-05,1.817716046144181e-05,3.3069478298123828e-06,5.46935308400219e-07,8.291937451756845e-08,1.1604166930419654e-08,1.507951017067864e-09,1.8289308182224978e-10,2.079594201823888e-11],[0.0051960999873216,0.009453199036786384,0.008599042767377768,0.005276212576600272,0.003956563219899428,0.0014396250923037828,0.0004365152893229387,0.00011344953557582027,2.5799663282221148e-05,5.2152223715648376e-06,9.487988148764653e-07,1.569216084227319e-07,2.3790458247728146e-08,3.3293600013748877e-09,4.3264732663379273e-10,5.2473987559670695e-11,5.9665788989069616e-12],[0.0011181126291528285,0.0020341681751152225,0.0018503682262254535,0.001122117176121485,0.0005163826588523403,0.00030978291427757697,9.393069013320943e-05,2.441241677572759e-05,5.5516501634164136e-06,1.122227442065214e-06,2.0416542022422647e-07,3.376686988174617e-08,5.1193033015189246e-09,7.164218305299404e-10,9.309837013506108e-11,1.1291512545107779e-11,1.2839066291993098e-12],[0.00019247910617908957,0.00035017480525265684,0.00031853429878161375,0.00019316847467478685,8.785724116109902e-05,3.234454066339887e-05,1.616983370747167e-05,4.202510586275826e-06,9.556967995997209e-07,1.9318745656421157e-07,3.514634981559266e-08,5.812846366138089e-09,8.812698274257145e-10,1.23329466095085e-10,1.6026552784672365e-11,1.9437936621278025e-12,2.2101995269737072e-13],[2.7612160401327294e-05,5.02344544458942e-05,4.569545404631427e-05,2.7711054010387928e-05,1.2603592584751456e-05,4.585911340156294e-06,1.406914917314975e-06,6.028726894053421e-07,1.3709983306463143e-07,2.7713777064260738e-08,5.041932435650169e-09,8.338839962231407e-10,1.2642288461734562e-10,1.7692273554403572e-11,2.2990949768800782e-12,2.7884762897754514e-13,3.170649795149853e-14],[3.3952393238058796e-06,6.176915991565677e-06,5.618792598704189e-06,3.4073994541787143e-06,1.5497596907672368e-06,5.638916438004438e-07,1.7098015681738158e-07,4.496153208909783e-08,1.6858034204592066e-08,3.407734285624549e-09,6.199647917686634e-10,1.0253582821187385e-10,1.554517803181935e-11,2.1754727636796696e-12,2.8270072175491867e-13,3.42875900144736e-14,3.898686198415814e-15],[3.6529897194111686e-07,6.645838028749797e-07,6.04534456662752e-07,3.666072988954851e-07,1.6674100639199083e-07,6.066996111943767e-08,1.8396015582697545e-08,4.781091236322286e-09,1.1000957196650358e-09,3.666433239209021e-10,6.670295654414072e-11,1.1031985984110855e-11,1.6725293895629713e-12,2.3406242926265067e-13,3.0416201385274694e-14,3.689054051301932e-15,4.1946558824780646e-16],[3.49360648640761e-08,6.355874127288043e-08,5.7815807359959616e-08,3.506118921112353e-08,1.5946594604024522e-08,5.8022876048808225e-09,1.7593380846997604e-09,4.572487917654074e-10,1.039833684983745e-10,2.1267419776449103e-11,6.3792646447069135e-12,1.0550650495194953e-12,1.5995554252549126e-13,2.238500745707351e-14,2.9089115112156515e-15,3.5280972990020225e-16,4.011639266708745e-17],[3.0070595587257877e-09,5.470705450908508e-09,4.976392643064581e-09,3.0178294140395495e-09,1.372574728141899e-09,4.994215711648224e-10,1.5143189209231056e-10,3.9356875347682273e-11,8.950183239242508e-12,1.8092172501750429e-12,3.3303060819942837e-13,9.081284496633295e-14,1.3767888426868706e-14,1.9267496470433135e-15,2.5037937728021295e-16,3.036746911352298e-17,3.452947047714172e-18],[2.352975415078668e-10,4.280738434917846e-10,3.893946666580501e-10,2.3614026524786396e-10,1.0740175003533022e-10,3.9078929291601294e-11,1.184930036114874e-11,3.0796117701989547e-12,7.003373465376444e-13,1.415683203827858e-13,2.575534560819426e-14,4.3099092672427844e-15,1.0773149767507587e-15,1.5076504013194484e-16,1.9591780863585167e-17,2.376205287818053e-18,2.7018751555032974e-19],[1.687734733168409e-11,3.070474469865328e-11,2.7930376986423096e-11,1.6937793952475118e-11,7.70367861797816e-12,2.8030410295750046e-12,8.49922853213793e-13,2.2089341503235602e-13,5.023357477991605e-14,1.0154367525270238e-14,1.8473712504239067e-15,3.05536288015049e-16,4.686784474280392e-17,1.0814026918751516e-17,1.4052730358422105e-18,1.7043969825136836e-19,1.9379924309473733e-20],[1.1174520087816868e-12,2.0329663168231584e-12,1.8492749634248326e-12,1.1214541897227755e-12,5.100618585070758e-13,1.8558981856798262e-13,5.6273535228503587e-14,1.462539020519895e-14,3.3259734449336016e-15,6.723223837266671e-16,1.2231476156660584e-16,2.0229609078267876e-17,3.066956010595393e-18,4.342677966357064e-19,9.304336433490487e-20,1.1284841121305015e-20,1.2831480518862751e-21],[6.870192240551846e-14,1.2498853915318697e-13,1.1369503481603383e-13,6.894797997426121e-14,3.1359047144559524e-14,1.141022362867558e-14,3.459745940201868e-15,8.991817233596393e-16,2.0448374314147818e-16,4.133496550660966e-17,7.520018034027417e-18,1.2437339789691631e-18,1.8855912576575632e-19,2.6387941109905924e-20,3.4695320295133885e-21,6.938018572446517e-22,7.888905939825965e-23],[3.942263737604175e-15,7.172110594101068e-15,6.524065080089978e-15,3.956383048922597e-15,1.7994494196844562e-15,6.547431174308578e-16,1.9852764644451227e-16,5.1596976873421494e-17,1.1733715990623626e-17,2.371889022988059e-18,4.3151477227505387e-19,7.13681246876207e-20,1.0819927272384107e-20,1.5141966877372348e-21,1.9676849264625146e-22,2.4146696874620218e-23,4.526823519198638e-24],[2.1207708104259244e-16,3.8582915323569583e-16,3.5096705111826067e-16,2.1283664015127913e-16,9.680275238063827e-17,3.522240479574063e-17,1.0679945981948749e-17,2.7756986782897153e-18,6.312241906439656e-19,1.275975769337988e-19,2.321366590923932e-20,3.8393026369242046e-21,5.820662304077326e-22,8.145736435554467e-23,1.0585310963220433e-23,1.2838481636324301e-24,1.4770225035469818e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.29652983107362985, "-10": 1.0284527428851897e-05, "-11": 1.6812078590730235e-06, "-12": 2.5237148917544676e-07, "-13": 3.501895071640382e-08, "-14": 4.516579765378785e-09, "-15": 5.420534116518239e-10, "-16": 5.614001239010891e-11, "-2": 0.22075195806542053, "-3": 0.11937358104649111, "-4": 0.05052733565788989, "-5": 0.017503126840701228, "-6": 0.00512134788572727, "-7": 0.0012955599318905846, "-8": 0.00028845669189988843, "-9": 5.732593223865736e-05, "0": 0.16626658271899766, "1": 0.0832687689719282, "10": 3.464217257863926e-09, "11": 2.679223438217437e-10, "12": 1.9028061869124586e-11, "13": 1.249177449655115e-12, "14": 7.622500005073779e-14, "15": 4.32809289083987e-15, "16": 2.1207708104259244e-16, "2": 0.029620433298179556, "3": 0.007578125744286285, "4": 0.0015175629857623926, "5": 0.0002487154186123201, "6": 3.44300845571794e-05, "7": 4.1207670254305025e-06, "8": 4.3407813890272044e-07, "9": 4.081362444898061e-08} |
| Raw goal margin distribution | {"-1": 0.24927540504401755, "-10": 8.645604832509381e-06, "-11": 1.4132937941395612e-06, "-12": 2.121540519481513e-07, "-13": 2.9438397791015187e-08, "-14": 3.79682626315209e-09, "-15": 4.5567281799532974e-10, "-16": 4.7193647522922244e-11, "-2": 0.18557334876488013, "-3": 0.10035043576958079, "-4": 0.04247539620655595, "-5": 0.014713862065598502, "-6": 0.004305219693963929, "-7": 0.0010891019821227866, "-8": 0.0002424887858690603, "-9": 4.819058145542514e-05, "0": 0.2304467166262749, "1": 0.11677229779655778, "10": 4.8580592010869735e-09, "11": 3.7572199163472183e-10, "12": 2.6684080172024792e-11, "13": 1.7517890915506096e-12, "14": 1.0689443972046837e-13, "15": 6.069518718484962e-15, "16": 2.9740715960000655e-16, "2": 0.041538335448722145, "3": 0.010627215546441962, "4": 0.0021281606427761743, "5": 0.00034878708172789803, "6": 4.8283169508930945e-05, "7": 5.778774445507015e-06, "8": 6.087312485670615e-07, "9": 5.723515271277675e-08} |
| Research history json | {"away": [{"away": "Real Madrid", "away_goals": 3.0, "away_xg": 3.36, "date": "2026-11-01T00:00:00+00:00", "home": "Santander", "home_goals": 0.0, "home_xg": 0.97, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 2.0, "away_xg": 1.94, "date": "2026-10-25T00:00:00+00:00", "home": "Barcelona", "home_goals": 1.0, "home_xg": 1.19, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 1.0, "away_xg": 0.75, "date": "2026-10-18T00:00:00+00:00", "home": "Real Madrid", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Villarreal", "away_goals": 0.0, "away_xg": 0.59, "date": "2026-10-10T00:00:00+00:00", "home": "Real Madrid", "home_goals": 1.0, "home_xg": 1.43, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 1.0, "away_xg": 0.3, "date": "2026-09-20T00:00:00+00:00", "home": "Ath Madrid", "home_goals": 2.0, "home_xg": 2.35, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 3.0, "away_xg": 3.62, "date": "2026-09-15T00:00:00+00:00", "home": "Elche", "home_goals": 2.0, "home_xg": 0.78, "source": "pipeline training history"}, {"away": "Vallecano", "away_goals": 1.0, "away_xg": 1.22, "date": "2026-09-12T00:00:00+00:00", "home": "Real Madrid", "home_goals": 4.0, "home_xg": 2.61, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 0.0, "away_xg": 3.46, "date": "2026-09-04T00:00:00+00:00", "home": "Betis", "home_goals": 1.0, "home_xg": 0.93, "source": "pipeline training history"}, {"away": "Malaga", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-08-30T00:00:00+00:00", "home": "Real Madrid", "home_goals": 4.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "Sociedad", "away_goals": 1.0, "away_xg": 0.56, "date": "2026-08-26T00:00:00+00:00", "home": "Real Madrid", "home_goals": 4.0, "home_xg": 3.14, "source": "pipeline training history"}], "h2h": [{"away": "Real Madrid", "away_goals": 2.0, "away_xg": null, "date": "2026-02-08T00:00:00+00:00", "home": "Valencia", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 0.0, "away_xg": null, "date": "2025-11-01T00:00:00+00:00", "home": "Real Madrid", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 2.0, "away_xg": null, "date": "2025-04-05T00:00:00+00:00", "home": "Real Madrid", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 2.0, "away_xg": null, "date": "2025-01-03T00:00:00+00:00", "home": "Valencia", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 2.0, "away_xg": null, "date": "2024-03-02T00:00:00+00:00", "home": "Valencia", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 1.0, "away_xg": null, "date": "2023-11-11T00:00:00+00:00", "home": "Real Madrid", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 0.0, "away_xg": null, "date": "2023-05-21T00:00:00+00:00", "home": "Valencia", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 0.0, "away_xg": null, "date": "2023-02-02T00:00:00+00:00", "home": "Real Madrid", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Valencia", "away_goals": 1.0, "away_xg": 0.9, "date": "2026-11-01T00:00:00+00:00", "home": "Elche", "home_goals": 0.0, "home_xg": 1.25, "source": "pipeline training history"}, {"away": "Villarreal", "away_goals": 2.0, "away_xg": 1.5, "date": "2026-10-24T00:00:00+00:00", "home": "Valencia", "home_goals": 1.0, "home_xg": 1.13, "source": "pipeline training history"}, {"away": "Ath Bilbao", "away_goals": 0.0, "away_xg": 0.59, "date": "2026-10-17T00:00:00+00:00", "home": "Valencia", "home_goals": 0.0, "home_xg": 1.41, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 2.0, "away_xg": 1.8, "date": "2026-10-11T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Sociedad", "away_goals": 3.0, "away_xg": 2.65, "date": "2026-09-20T00:00:00+00:00", "home": "Valencia", "home_goals": 2.0, "home_xg": 1.55, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 1.0, "away_xg": 0.65, "date": "2026-09-15T00:00:00+00:00", "home": "Alaves", "home_goals": 0.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 0.0, "away_xg": 0.1, "date": "2026-09-11T00:00:00+00:00", "home": "Sevilla", "home_goals": 1.0, "home_xg": 0.93, "source": "pipeline training history"}, {"away": "Barcelona", "away_goals": 5.0, "away_xg": 4.08, "date": "2026-09-06T00:00:00+00:00", "home": "Valencia", "home_goals": 0.0, "home_xg": 0.66, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 1.0, "away_xg": 1.33, "date": "2026-08-30T00:00:00+00:00", "home": "La Coruna", "home_goals": 3.0, "home_xg": 1.42, "source": "pipeline training history"}, {"away": "Betis", "away_goals": 1.0, "away_xg": 0.71, "date": "2026-08-25T00:00:00+00:00", "home": "Valencia", "home_goals": 0.0, "home_xg": 1.12, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 17.1% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 59.8% |
| Raw p over 1 5 | 75.0% |
| Raw p under 3 5 | 71.8% |
| Raw p btts yes | 48.6% |
| P home draw | 28.9% |
| P draw away | 87.8% |
| P home away | 83.4% |
| Raw p home draw | 40.2% |
| Raw p draw away | 82.9% |
| Raw p home away | 77.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5305 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.08, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.13, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.13, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.3, "draw": 6.61, "home": 8.94}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.32, "draw": 6.12, "home": 10.6}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 8.94 |
| Reference draw odds | 6.61 |
| Reference away odds | 1.30 |
| Market reference 1x2 last update utc | 2026-11-05T13:32:59Z |
| Market reference home last update utc | 2026-11-05T13:32:59Z |
| Market reference draw last update utc | 2026-11-05T13:32:59Z |
| Market reference away last update utc | 2026-11-05T13:32:59Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.91 |
| Market reference over 2 5 last update utc | 2026-11-05T13:32:39Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:32:39Z |
| Home probability edge | +2.1% |
| Draw probability edge | +2.8% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -15.4% |
| Under 2.5 probability edge | +15.4% |
| Raw edge prob home | 0.0703 |
| Raw ev home | 0.8176 |
| Raw edge prob draw | 0.0917 |
| Raw ev draw | 0.5233 |
| Raw edge prob away | -0.1620 |
| Raw ev away | -0.2105 |
| Count model | {"corners": {"alpha": 0.014493407444055235, "mu": 9.801212284987749, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,462.7950 |
| Elo away rating | 1,679.9082 |
| Elo rating diff | -157.1133 |
| Elo home expectancy | 0.2881 |

</details>


---

## 2026-11-08 — Elche CF vs Real Betis

The model's most likely 1X2 outcome is **Real Betis win** at **43.9%**. Expected goals are 1.33 for Elche CF and 1.45 for Real Betis (2.78 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 52.8%; Under 3.5 goals: 69.6%; Double Chance 1X: 56.1%; Double Chance X2: 69.1%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elche CF win | 30.9% | 3.23 |
| Draw | 25.1% | 3.98 |
| Real Betis win | 43.9% | 2.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elche CF expected goals | 1.33 |
| Real Betis expected goals | 1.45 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 52.8% |
| Under 2.5 | 47.2% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.88% |
| 2 | 0-1 | 9.69% |
| 3 | 1-2 | 9.58% |
| 4 | 1-0 | 7.23% |
| 5 | 0-2 | 7.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elche CF win | 30.9% | 29.5% | 3.39 | +4.9% |
| Draw | 25.1% | 24.8% | 3.88 | -2.6% |
| Real Betis win | 43.9% | 45.7% | 2.19 | -3.8% |
| Over 2.5 | 52.8% | 57.0% | 1.73 | -8.7% |
| Under 2.5 | 47.2% | 43.0% | 2.28 | +7.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T13:00:00+00:00 |
| Fixture id | c35673eb1e889309d6985c091a43a3f5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:31:12Z |
| Market best draw last update utc | 2026-11-05T13:32:59Z |
| Market best away last update utc | 2026-11-05T13:31:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Elche |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3282 |
| Dc lambda away | 1.4478 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:32:13.282064+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.90 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.68 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.06290894478878634,0.09686409382344274,0.07209053960859359,0.034791363839271706,0.012592904051993243,0.0036464504972054004,0.0008799003770741868,0.00018199099351202442,3.29362644449845e-05,5.2984185628860195e-06,7.671153898762492e-07,1.0096769517178303e-07,1.2181916787578855e-08,1.35670900738954e-09,1.4030498599315634e-10,1.3542419969817908e-11],[0.07228224093165617,0.11876429929889099,0.09575088483059616,0.04621000050991938,0.016725935360059604,0.004843227190336687,0.0011686864895873994,0.000241721018521803,4.374605157270642e-05,7.037376448472523e-06,1.0188851095666197e-06,1.3410561502929421e-07,1.6180060763539135e-08,1.8019852344079666e-09,1.863535302680364e-10,1.7987085433093727e-11],[0.04947629729025869,0.07163274972518734,0.05594505645740625,0.030688135092830124,0.011107720368305811,0.0032163949072109553,0.0007761265630353071,0.0001605273142029343,2.9051822671002837e-05,4.673532931545138e-06,6.766432274706764e-07,8.905975298231457e-08,1.0745204177504895e-08,1.1967012702569933e-09,1.23757676883464e-10,1.1945252144686032e-11],[0.021904858665251613,0.031714282282043545,0.022958278709660593,0.011953584577857886,0.004917769883494918,0.0014240086609707304,0.00034361792617377586,7.107096371619626e-05,1.2862241202952043e-05,2.069133786069544e-06,2.995732315535079e-07,3.942981606717607e-08,4.7572714962212435e-09,5.298208157276083e-10,5.4791780495787e-11,5.2885740097947654e-12],[0.007273525800592602,0.010530752740790204,0.007623314767002357,0.003679061346469037,0.0014366703465112107,0.00047284321228095705,0.00011409860660437975,2.3599170218923496e-05,4.270917455930651e-06,6.870575249010314e-07,9.947353060660858e-08,1.3092701891392528e-08,1.5796557967789798e-09,1.7592742467674403e-10,1.8193654439264354e-11,1.7560752204079034e-12],[0.001932144037279176,0.0027973958811724287,0.0020250622016307193,0.0009773082048853518,0.0003537414776323014,0.00011050859844631582,3.03092267019323e-05,6.268898643284442e-06,1.1345292396592078e-06,1.8251039955026498e-07,2.6424212176852026e-08,3.4779536891540036e-09,4.196207743500853e-10,4.673347340781524e-11,4.83297398055265e-12,4.664849426736625e-13],[0.0004277133129952507,0.0006192516898379911,0.00044828234674503296,0.00021634397957079278,7.83067599634062e-05,2.267481135599616e-05,5.902996447569467e-06,1.3877285315262445e-06,2.511475596135943e-07,4.0401815879967716e-08,5.849453827141252e-09,7.699048653364833e-10,9.289027532939292e-11,1.0345258093273278e-11,1.0698619114095265e-12,1.0326446499005127e-13],[8.115574109104451e-05,0.0001174988673107817,8.505857770326101e-05,4.104982346632834e-05,1.4858184078407047e-05,4.302393832001048e-06,1.0381816393779868e-06,2.3166231587354416e-07,4.765357005353454e-08,7.665974402810135e-09,1.1098947493475988e-09,1.46084299968182e-10,1.7625308601492516e-11,1.9629435461295582e-12,2.029991436962488e-13,1.9593741719072675e-14],[1.3473914297112529e-05,1.950779632924788e-05,1.4121884302951599e-05,6.81531332055005e-06,2.4668359402766907e-06,7.143066526836835e-07,1.7236452092923331e-07,3.565038864336173e-08,6.9607233180107094e-09,1.2727464590760812e-09,1.8427071862664527e-10,2.4253704192249272e-11,2.9262488933500282e-12,3.258984854928323e-13,3.370301383215776e-14,3.253058787133375e-15],[1.988455108880819e-06,2.8789241506614178e-06,2.0840813122320117e-06,1.0057912119698904e-06,3.64051041148836e-07,1.0541604180611515e-07,2.543723410093072e-08,5.2612177774257455e-09,9.52161734358018e-10,1.6525260114062362e-10,2.7194328521802716e-11,3.5793163699057646e-12,4.3185034679088473e-13,4.8095489860256714e-14,4.973827839590517e-15,4.800803405845633e-16],[2.6410724230251337e-07,3.8237962468121526e-07,2.768083451567577e-07,1.3358950983559354e-07,4.835337549525776e-08,1.4001392322872016e-08,3.3785815531845273e-09,6.98796624647439e-10,1.2646642549995169e-10,2.034450681467077e-11,3.177805086950718e-12,4.754059428156363e-13,5.735850091306269e-14,6.388058315950763e-15,6.606254013655249e-16,6.376442408438598e-17],[3.1889825662833804e-08,4.6170712555229823e-08,3.3423429785978735e-08,1.6130364854443675e-08,5.838464334829171e-09,1.6906085434109243e-09,4.0794934580139496e-10,8.437671886429551e-11,1.527028273149645e-11,2.456512626689189e-12,3.5565869683428117e-13,5.050342564944309e-14,6.925794909871943e-15,7.713308587969263e-16,7.97677060815144e-17,7.699282873935482e-18],[3.529680686823671e-09,5.110340649902449e-09,3.6994255111425635e-09,1.7853668408261146e-09,6.462222472220336e-10,1.871226386668923e-10,4.515330194343808e-11,9.339118944759674e-12,1.6901698557266566e-12,2.71895659356603e-13,3.936558470371026e-14,5.181296593807631e-15,6.744306470043075e-16,8.53736757369496e-17,8.828976820537719e-18,8.521843408568636e-19],[3.6062562734177905e-10,5.221208280060294e-10,3.77968367150095e-10,1.8240999516234487e-10,6.602418858357827e-11,1.911822199979875e-11,4.613289213579955e-12,9.541728918556136e-13,1.726837690477011e-13,2.7779437129543368e-14,4.0219611741215404e-15,5.29370359636456e-16,6.38693956510577e-17,7.674136930399584e-18,9.020519381762135e-19,8.706722783156374e-20],[3.421315067140515e-11,4.9534467888271445e-11,3.585848512666989e-11,1.7305538417947537e-11,6.263824145327274e-12,1.8137773920004202e-12,4.376703899786707e-13,9.052396291483547e-14,1.6382795234171836e-14,2.6354812193619888e-15,3.8157011929257363e-16,5.0222242963484935e-17,6.059395370230447e-18,6.748393066112881e-19,7.529262254422686e-20,8.260212138278466e-21],[3.029467728975119e-12,4.386122557981576e-12,3.175156960682193e-12,1.532351424551161e-12,5.546420816514872e-13,1.6060432812469336e-13,3.875434727139914e-14,8.015614433856855e-15,1.4506453950706136e-15,2.333636378905653e-16,3.378684336441916e-17,4.447022894672699e-18,5.365405515416818e-19,5.975491474778222e-20,6.179595205048001e-21,6.435004546693956e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.22872547275187163, "-10": 9.125146900381578e-07, "-11": 1.1840100506129535e-07, "-12": 1.411294827288008e-08, "-13": 1.5550077898022625e-09, "-14": 1.5829207142625006e-10, "-15": 1.3542419969817908e-11, "-2": 0.13095289565447935, "-3": 0.05510208726857727, "-4": 0.018287788195450055, "-5": 0.0049892408117968735, "-6": 0.00115284539842476, "-7": 0.00023072367412200554, "-8": 4.069134141572072e-05, "-9": 6.411301560594298e-06, "0": 0.25112520585586734, "1": 0.1709298218068566, "10": 3.1416621479252155e-07, "11": 3.739599486038594e-08, "12": 4.0891923513809205e-09, "13": 4.1333525219073267e-10, "14": 3.859927322938673e-11, "15": 3.029467728975119e-12, "2": 0.08987398945268689, "3": 0.034692616229551394, "4": 0.010562829568635083, "5": 0.0026436480880382683, "6": 0.0005603899459290835, "7": 0.00010288723853459731, "8": 1.6646442943940373e-05, "9": 2.4061114069091618e-06} |
| Raw goal margin distribution | {"-1": 0.2071208282703037, "-10": 8.263215991450002e-07, "-11": 1.0721724144356915e-07, "-12": 1.2779886299703607e-08, "-13": 1.4081269458781061e-09, "-14": 1.4334033086902304e-10, "-15": 1.2263248195253908e-11, "-2": 0.11858352235990068, "-3": 0.049897328081473576, "-4": 0.01656038478225204, "-5": 0.004517973782921891, "-6": 0.0010439514712398412, "-7": 0.0002089302862106616, "-8": 3.684777316690374e-05, "-9": 5.8057114214014275e-06, "0": 0.2584729797462715, "1": 0.189805302610689, "10": 3.4885903956612725e-07, "11": 4.152556906613823e-08, "12": 4.540754699692997e-09, "13": 4.589791400495126e-10, "14": 4.286172335764132e-11, "15": 3.3640065435578285e-12, "2": 0.09979861667540113, "3": 0.03852366106861736, "4": 0.011729264334958155, "5": 0.0029355815155137823, "6": 0.0006222728260212266, "7": 0.00011424889605807818, "8": 1.8484680478614e-05, "9": 2.671814074781329e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Valencia", "away_goals": 1.0, "away_xg": 0.9, "date": "2026-11-01T00:00:00+00:00", "home": "Elche", "home_goals": 0.0, "home_xg": 1.25, "source": "pipeline training history"}, {"away": "Elche", "away_goals": 3.0, "away_xg": 2.52, "date": "2026-10-24T00:00:00+00:00", "home": "Vallecano", "home_goals": 0.0, "home_xg": 1.52, "source": "pipeline training history"}, {"away": "Elche", "away_goals": 0.0, "away_xg": 0.3, "date": "2026-10-17T00:00:00+00:00", "home": "Villarreal", "home_goals": 0.0, "home_xg": 2.38, "source": "pipeline training history"}, {"away": "Celta", "away_goals": 0.0, "away_xg": 0.47, "date": "2026-10-11T00:00:00+00:00", "home": "Elche", "home_goals": 0.0, "home_xg": 0.78, "source": "pipeline training history"}, {"away": "Elche", "away_goals": 3.0, "away_xg": 1.44, "date": "2026-09-18T00:00:00+00:00", "home": "Espanol", "home_goals": 1.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 3.0, "away_xg": 3.62, "date": "2026-09-15T00:00:00+00:00", "home": "Elche", "home_goals": 2.0, "home_xg": 0.78, "source": "pipeline training history"}, {"away": "Elche", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-09-12T00:00:00+00:00", "home": "Ath Bilbao", "home_goals": 1.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "Sociedad", "away_goals": 3.0, "away_xg": 0.58, "date": "2026-09-07T00:00:00+00:00", "home": "Elche", "home_goals": 2.0, "home_xg": 2.47, "source": "pipeline training history"}, {"away": "Elche", "away_goals": 2.0, "away_xg": 1.04, "date": "2026-08-28T00:00:00+00:00", "home": "Santander", "home_goals": 3.0, "home_xg": 1.72, "source": "pipeline training history"}, {"away": "Barcelona", "away_goals": 5.0, "away_xg": 4.38, "date": "2026-08-23T00:00:00+00:00", "home": "Elche", "home_goals": 0.0, "home_xg": 0.7, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 34.4% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 39.8% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.5% |
| P home draw | 56.1% |
| P draw away | 69.1% |
| P home away | 74.9% |
| Raw p home draw | 60.2% |
| Raw p draw away | 65.6% |
| Raw p home away | 74.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5276 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.04, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.49, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.63, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.88, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.14, "draw": 3.88, "home": 3.28}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.19, "draw": 3.8, "home": 3.39}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.73, "under": 2.28}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.28 |
| Reference draw odds | 3.88 |
| Reference away odds | 2.14 |
| Market reference 1x2 last update utc | 2026-11-05T13:32:59Z |
| Market reference home last update utc | 2026-11-05T13:32:59Z |
| Market reference draw last update utc | 2026-11-05T13:32:59Z |
| Market reference away last update utc | 2026-11-05T13:32:59Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-11-05T13:31:12Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:31:12Z |
| Market best over 2 5 last update utc | 2026-11-05T13:31:12Z |
| Market best under 2 5 last update utc | 2026-11-05T13:31:12Z |
| Home probability edge | +1.5% |
| Draw probability edge | +0.3% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | 0.0488 |
| Raw ev home | 0.1646 |
| Raw edge prob draw | 0.0105 |
| Raw ev draw | 0.0029 |
| Raw edge prob away | -0.0593 |
| Raw ev away | -0.1284 |
| Count model | {"corners": {"alpha": 0.014493407444055235, "mu": 9.58617789582258, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,459.5603 |
| Elo away rating | 1,551.0281 |
| Elo rating diff | -31.4678 |
| Elo home expectancy | 0.4548 |

</details>


---
