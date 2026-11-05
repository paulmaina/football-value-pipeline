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
| Training sha256 | be8b4bf67072a54ecf97ecc40eba94c2529e2a13e599d124eb34cf9b1abd5efd |
| Training as of utc | 2026-11-05T16:23:31.994387+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 109, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 109, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 108, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-05T16:23:31.994387+00:00', 'observations': 590, 'observations_sha256': '209e30dc9bdbb139d2b3e3cee2eb73bb0d03c884ff52a341ec8bfd00f495a18e', 'eligible_training_matches': 176, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 183, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 30, 'retrospective_eligible_training_matches': 176, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '7c6f1b4c5cbd9ff2f2094c518add55ffe33c55f8eccd0e8f6bdec59fd3143743', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 114, 'tuning_matches': 22, 'audit_matches': 40, 'tuning_origin_utc': '2026-09-13T00:00:00+00:00', 'audit_origin_utc': '2026-10-09T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 17, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8357146014438204, 'audit_candidate_poisson_score': 0.8437651841527154, 'audit_gain': -0.008050582708895027, 'audit_gain_lower95': -0.03725049821585039, 'audit_baseline_briers': [0.5199253099278909, 0.20340070445316755, 0.22970209423243637, 0.28429820925953975], 'audit_candidate_briers': [0.5207453946703196, 0.21314479122702693, 0.23282815042185553, 0.28812038229266573], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2009, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1630, 'tuning_matches': 230, 'audit_matches': 129, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8432834464502666, 'audit_candidate_poisson_score': 0.8400225074412011, 'audit_gain': 0.0032609390090655443, 'audit_gain_lower95': -0.005259240284233485, 'audit_baseline_briers': [0.5723880944925321, 0.1848831628824439, 0.20353795326472862, 0.2524151023574783], 'audit_candidate_briers': [0.574670571206337, 0.1816626862987799, 0.20413573167809032, 0.24863999990406543], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1846.692 |
| Base scoring parameter | 0.089 |
| Home-advantage parameter | 0.289 |
| Dixon-Coles low-score adjustment | -0.020 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 2009, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261105T162331994387Z_9d2ef1bd9b894bdc0635f9b4c9a6526608b5553b80eb5988bbc24613567cf925.json |
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
| Dc lambda home | 1.5208 |
| Dc lambda away | 1.0532 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T16:23:31.994387+00:00 |
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
| Fair Under 1.5 odds | 3.70 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.41 |
| Fair Under 4.5 odds | 1.13 |
| Score matrix json | [[0.07872757551685815,0.07778007500391995,0.04227723929332215,0.014842373053659848,0.003908060960454042,0.0008232074704177548,0.0001445027227502754,2.1741823606469897e-05,2.8623580521233278e-06,3.3496499718602405e-07,3.527909247095788e-08,3.377868178982498e-09,2.9646909588100873e-10,2.4018952005853105e-11,1.8069411004317113e-12,1.268734399260283e-13],[0.1134249629869793,0.12459829979210248,0.06429696186994112,0.02257289052554922,0.005943539615166147,0.0012519677306569428,0.00021976567557581019,3.306585829101168e-05,4.353191684504397e-06,5.094285249424176e-07,5.3653892764223086e-08,5.137200657755119e-09,4.5088237718700953e-10,3.6529008683881076e-11,2.7480702377375525e-12,1.929543382110247e-13],[0.08815325015691755,0.09284452674242395,0.04889273016411999,0.017164889496992797,0.004519589575816796,0.000952021971940361,0.00016711433266471167,2.5143957662224515e-05,3.3102563510495676e-06,3.8737991164026523e-07,4.079952185737997e-08,3.90643287417883e-09,3.428602186236022e-10,2.7777408337838598e-11,2.08968904125725e-12,1.4672644115333247e-13],[0.044689027782584226,0.047067256484218,0.024786024029532547,0.00870168963992424,0.0022911924830908287,0.00048262470502155206,8.47181135355482e-05,1.2746654496925514e-05,1.6781246043248867e-06,1.963810931859143e-07,2.0683196167527e-08,1.98035451823076e-09,1.7381196732212274e-10,1.4081674478572195e-11,1.0593616395932607e-12,7.43825326175616e-14],[0.016991227214518102,0.017895454185714272,0.00942390083040512,0.003308471747058023,0.0008711349072481652,0.0001834988682738079,3.2210696622691245e-05,4.846408917998979e-06,6.380402049710599e-07,7.466610800286171e-08,7.86396355084409e-09,7.529511214309655e-10,6.608509461741982e-11,5.353997222547429e-12,4.027801725346161e-13,2.8281002635479757e-14],[0.005168191237633333,0.005443228340625797,0.002866451085676131,0.0010063319427859037,0.0002649715489996867,5.5814523056816424e-05,9.79747006744856e-06,1.4741235455075834e-06,1.940715496860437e-07,2.2711056726900374e-08,2.3919677492049252e-09,2.290237979291288e-10,2.0100985210067154e-11,1.62851577361286e-12,1.225129257648435e-13,8.602182065300398e-15],[0.0013099995825064917,0.0013797142028692852,0.000726569423005825,0.0002550784915451709,6.716326904432452e-05,1.4147503167028876e-05,2.4833991444664188e-06,3.7365127186397066e-07,4.919199723374133e-08,5.756651304595457e-09,6.063004654336971e-10,5.805146634020422e-11,5.095067311250553e-12,4.127856121119482e-13,3.105378153094191e-14,2.180425296984307e-15],[0.0002846144525111373,0.0002997608607783933,0.00015785665988111953,5.541912088215174e-05,1.4592094000010041e-05,3.0737291233171454e-06,5.395507733800624e-07,8.118060004887607e-08,1.0687601391309061e-08,1.2507073904711272e-09,1.3172666413869204e-10,1.2612436317172693e-11,1.1069696606500884e-12,8.968304460901204e-14,6.74683805006915e-15,4.737257632977508e-16],[5.4106668584061615e-05,5.6986078554724445e-05,3.0009361452368426e-05,1.053545939194109e-05,2.774031982705172e-06,5.843316863397552e-07,1.025713719805104e-07,1.543284883654288e-08,2.0317678927969646e-09,2.377658958453972e-10,2.5041915114824694e-11,2.397688893975409e-12,2.1044061548161105e-13,1.704920719751414e-14,1.2826085504253976e-15,9.005769962957176e-17],[9.14307153081737e-06,9.62964096887873e-06,5.071052155555968e-06,1.7803065934633105e-06,4.6876241894737237e-07,9.874173638369791e-08,1.7332750575372498e-08,2.607878927485263e-09,3.433328952603986e-10,4.017823773285712e-11,4.231641443748847e-12,4.0516708272668007e-13,3.5560747883568346e-14,2.881014947509018e-15,2.1673819566913504e-16,1.5218160924743986e-17],[1.3905158695732646e-06,1.464515348084747e-06,7.712264389452838e-07,2.70756338564415e-07,7.12913139100861e-08,1.5017048807719134e-08,2.6360358941932044e-09,3.9661693801380337e-10,5.221547680087333e-11,6.1104714089479135e-12,6.43565410381369e-13,6.161947398762029e-14,5.408224588348502e-15,4.381565857257315e-16,3.296243495468587e-17,2.3144404153736846e-18],[1.9225033125485202e-07,2.0248137181168125e-07,1.0662844028183068e-07,3.7434305438264565e-08,9.856614379391339e-09,2.0762313260331833e-09,3.6445378650288173e-10,5.4835575330642644e-11,7.2192219673685815e-12,8.448232617827329e-13,8.897824615835068e-14,8.5194024355186e-15,7.477318248296717e-16,6.057877553969804e-17,4.5573295333548724e-18,3.1999054901959473e-19],[2.4365183301142708e-08,2.5661832190647695e-08,1.351374260644445e-08,4.744302430070637e-09,1.2491953304579171e-09,2.6313482272918763e-10,4.618969057154293e-11,6.949682924517754e-12,9.149407721612559e-13,1.0707015949490621e-13,1.1276814262486196e-14,1.0797214267602124e-15,9.476510575121872e-17,7.677557487414063e-18,5.775811605583395e-19,4.055456409674688e-20],[2.8504285736687103e-09,3.0021206417717844e-09,1.5809426749031263e-09,5.550253836245514e-10,1.4614058183029463e-10,3.0783557347559574e-11,5.4036291123599895e-12,8.130279399561868e-13,1.0703688488404049e-13,1.2525899692174015e-14,1.3192494058617645e-15,1.2631420697316556e-16,1.108635883758537e-17,8.981803653035863e-19,6.756993466127601e-20,4.744388206126283e-21],[3.096463459799615e-10,3.261248836413369e-10,1.7174018216407167e-10,6.029324276112987e-11,1.5875471352328532e-11,3.3440641652942793e-12,5.870043631788551e-13,8.832044876080744e-14,1.1627577900246313e-14,1.3607073355994208e-15,1.43312048488049e-16,1.3721702412018817e-17,1.204327845992167e-18,9.757068488449929e-20,7.340223698024368e-21,5.153900313476759e-22],[3.1394858689026626e-11,3.306560781297773e-11,1.7412634834120225e-11,6.113095991487484e-12,1.6096045898771844e-12,3.390526750257397e-13,5.951602294391302e-14,8.954757723433319e-15,1.1789132015060353e-15,1.3796130673872143e-16,1.4530323283738655e-17,1.3912352391398306e-18,1.2210608337884512e-19,9.892633657426187e-21,7.442209111688742e-22,5.225508847096294e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.16172679977321913, "-10": 4.077364640416977e-08, "-11": 3.8576156071495756e-09, "-12": 3.351621761387646e-10, "-13": 2.6913748684743988e-11, "-14": 1.999895438642736e-12, "-15": 1.268734399260283e-13, "-2": 0.06988607938803508, "-3": 0.02182769912558125, "-4": 0.005340551048660578, "-5": 0.001069872345511571, "-6": 0.0001810833166589195, "-7": 2.650385187051123e-05, "-8": 3.4146341985792546e-06, "-9": 3.927046134823217e-07, "0": 0.26184981119565265, "1": 0.23464365989131616, "10": 1.607082223899042e-06, "11": 2.1955500896775382e-07, "12": 2.7545157221070054e-08, "13": 3.1939660921441676e-09, "14": 3.4271195379293925e-10, "15": 3.1394858689026626e-11, "2": 0.14572108164481684, "3": 0.06572120570790128, "4": 0.023219319564550044, "5": 0.006716781710755316, "6": 0.001641623525890437, "7": 0.0003469524648023128, "8": 6.454625087217082e-05, "9": 1.0719109165776037e-05} |
| Raw goal margin distribution | {"-1": 0.16172679977321913, "-10": 4.077364640416977e-08, "-11": 3.8576156071495756e-09, "-12": 3.351621761387646e-10, "-13": 2.6913748684743988e-11, "-14": 1.999895438642736e-12, "-15": 1.268734399260283e-13, "-2": 0.06988607938803508, "-3": 0.02182769912558125, "-4": 0.005340551048660578, "-5": 0.001069872345511571, "-6": 0.0001810833166589195, "-7": 2.650385187051123e-05, "-8": 3.4146341985792546e-06, "-9": 3.927046134823217e-07, "0": 0.26184981119565265, "1": 0.23464365989131616, "10": 1.607082223899042e-06, "11": 2.1955500896775382e-07, "12": 2.7545157221070054e-08, "13": 3.1939660921441676e-09, "14": 3.4271195379293925e-10, "15": 3.1394858689026626e-11, "2": 0.14572108164481684, "3": 0.06572120570790128, "4": 0.023219319564550044, "5": 0.006716781710755316, "6": 0.001641623525890437, "7": 0.0003469524648023128, "8": 6.454625087217082e-05, "9": 1.0719109165776037e-05} |
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
| Unanchored p over 2 5 | 0.4750 |
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
| Team research json | {"base_rates": [1.520841070625372, 1.0532172844127208], "coverage": {"team_news": "dated news leads; absences and tactics require confirmation", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [{"headline": "Getafe vs. Sevilla - Game Highlights", "published_at_utc": "2026-11-01T15:07:45+00:00", "source": "ESPN league news; unconfirmed context lead", "url": "https://www.espn.com/video/clip/_/id/50348131/getafe-vs-sevilla-game-highlights"}], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:27:19.059268+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-05T16:27:19.103167+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:27:19.213147+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/La_liga/2026"}, {"observed_at_utc": "2026-11-05T16:27:19.319321+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/La_liga/2025"}, {"observed_at_utc": "2026-11-05T16:27:19.340801+00:00", "reason": "HTTPError", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Sevilla+FC_vs_Deportivo+Alav%C3%A9s&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 1.9658152096820078, "goals_for": 1.4771346844204023, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 1.2630268310800783, "results": "LWLDLWWDLW", "xg_against": 1.4461597878889831, "xg_for": 0.9735333845193156, "xg_matches": 10}, "venue": {"goals_against": 1.3961941158577094, "goals_for": 1.3041211947932392, "last_match": "2026-10-26T00:00:00+00:00", "matches": 4, "points_per_game": 1.6038058841422904, "results": "WLWL", "xg_against": 1.3069157769949158, "xg_for": 0.8587582632892911, "xg_matches": 4}}}, "goal_rates": [1.520841070625372, 1.0532172844127208], "h2h": [], "margin_distribution": {"-1": 0.1642288088539639, "-10": 4.077364640416977e-08, "-11": 3.8576156071495756e-09, "-12": 3.351621761387646e-10, "-13": 2.6913748684743988e-11, "-14": 1.999895438642736e-12, "-15": 1.268734399260283e-13, "-2": 0.06988607938803508, "-3": 0.02182769912558125, "-4": 0.005340551048660578, "-5": 0.001069872345511571, "-6": 0.0001810833166589195, "-7": 2.650385187051123e-05, "-8": 3.4146341985792546e-06, "-9": 3.927046134823217e-07, "0": 0.2568457930341631, "1": 0.23714566897206096, "10": 1.607082223899042e-06, "11": 2.1955500896775382e-07, "12": 2.7545157221070054e-08, "13": 3.1939660921441676e-09, "14": 3.4271195379293925e-10, "15": 3.1394858689026626e-11, "2": 0.14572108164481684, "3": 0.06572120570790128, "4": 0.023219319564550044, "5": 0.006716781710755316, "6": 0.001641623525890437, "7": 0.0003469524648023128, "8": 6.454625087217082e-05, "9": 1.0719109165776037e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:27:19.341155+00:00", "p_over_1_5": 0.7275653774114975, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
