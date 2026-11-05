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
| Training as of utc | 2026-11-05T16:13:52.263713+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 109, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 109, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 108, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-05T16:13:52.263713+00:00', 'observations': 590, 'observations_sha256': '209e30dc9bdbb139d2b3e3cee2eb73bb0d03c884ff52a341ec8bfd00f495a18e', 'eligible_training_matches': 176, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 183, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 30, 'retrospective_eligible_training_matches': 176, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '7c6f1b4c5cbd9ff2f2094c518add55ffe33c55f8eccd0e8f6bdec59fd3143743', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 114, 'tuning_matches': 22, 'audit_matches': 40, 'tuning_origin_utc': '2026-09-13T00:00:00+00:00', 'audit_origin_utc': '2026-10-09T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 17, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8357146014438204, 'audit_candidate_poisson_score': 0.8437651841527154, 'audit_gain': -0.008050582708895027, 'audit_gain_lower95': -0.03725049821585039, 'audit_baseline_briers': [0.5199253099278909, 0.20340070445316755, 0.22970209423243637, 0.28429820925953975], 'audit_candidate_briers': [0.5207453946703196, 0.21314479122702693, 0.23282815042185553, 0.28812038229266573], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2009, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1630, 'tuning_matches': 230, 'audit_matches': 129, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8432834464502666, 'audit_candidate_poisson_score': 0.8400225074412011, 'audit_gain': 0.0032609390090655443, 'audit_gain_lower95': -0.005259240284233485, 'audit_baseline_briers': [0.5723880944925321, 0.1848831628824439, 0.20353795326472862, 0.2524151023574783], 'audit_candidate_briers': [0.574670571206337, 0.1816626862987799, 0.20413573167809032, 0.24863999990406543], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1846.710 |
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
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261105T161352263713Z_7a8d2bfee8190b63dc02b681b1b2d5504d65e86bb3984c5008dffcc8f70b386b.json |
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
| 4 | 2-0 | 8.81% |
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
| Dc lambda away | 1.0533 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T16:13:52.263713+00:00 |
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
| Fair Under 0.5 odds | 12.71 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.71 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.41 |
| Fair Under 4.5 odds | 1.14 |
| Score matrix json | [[0.07870915523323903,0.07777293496741688,0.0422759331440908,0.014843236379569634,0.003908636365320097,0.0008234020045564037,0.00014454974355486842,2.1750835380345387e-05,2.863799510082785e-06,3.351635308831037e-07,3.530314633921547e-08,3.3804723165875297e-09,2.967240811614927e-10,2.404175113703834e-11,1.8088173606425565e-12,1.270164921492196e-13],[0.1134120048951162,0.12459041324652503,0.06429984610114695,0.02257591361960696,0.005944865034648159,0.00125235845160175,0.00021985384054940623,3.3082069714718494e-05,4.355713855806442e-06,5.097690778592054e-07,5.369454220586767e-08,5.141550606698986e-09,4.513043553210146e-10,3.656645242683941e-11,2.7511321280120855e-12,1.93186531676686e-13],[0.08814818055462224,0.09284745597040425,0.048898627435845096,0.017168488823012758,0.004520939910623789,0.0009523912272616384,0.00016719403997412282,2.515819088030164e-05,3.3124251762155975e-06,3.876682407192722e-07,4.083352564379076e-08,3.910036847740331e-09,3.4320709720365737e-10,2.7807987768087046e-11,2.092175846623792e-12,1.4691413449452802e-13],[0.04468984299286104,0.047072307147993236,0.02479089152974848,0.008704173643716766,0.0022920506528292936,0.00048284847340356144,8.476494181471652e-05,1.2754836156015844e-05,1.6793512936883043e-06,1.9654214870977806e-07,2.0702002450693625e-08,1.9823317023944387e-09,1.7400099686190025e-10,1.4098244563688217e-11,1.0607026657928057e-12,7.448332526754855e-14],[0.016992824362571404,0.017898730318534395,0.00942646555334442,0.0033096668961810805,0.0008715272098822793,0.0001835978547428137,3.2230942690739775e-05,4.849887044964016e-06,6.385549750367448e-07,7.473300394904419e-08,7.871710170348002e-09,7.537599640376212e-10,6.616197732131074e-11,5.360703409264626e-12,4.0332059576955145e-13,2.8321470371106814e-14],[0.0051690685932967405,0.005444637264256636,0.00286744840045018,0.0010067717315436731,0.00026511095699480994,5.5848862113709575e-05,9.80437095330744e-06,1.4752932337945178e-06,1.942428401617602e-07,2.2733126368715642e-08,2.3945054070413018e-09,2.2928719051397044e-10,2.0125895009853836e-11,1.630679105460689e-12,1.2268659877483968e-13,8.615143656385052e-15],[0.001310321225011644,0.0013801758752237257,0.000726877276422295,0.00025520929830455993,6.720369591998304e-05,1.4157279614211783e-05,2.4853365990666565e-06,3.739760853365113e-07,4.923914466922751e-08,5.762681894070576e-09,6.069896735980971e-10,5.812263213983174e-11,5.101767741671272e-12,4.1336527161567103e-13,3.11001588579483e-14,2.18387614436474e-15],[0.0002847058998392114,0.00029988388113643674,0.00015793550856557764,5.545174079011639e-05,1.4601983356599817e-05,3.076086195431713e-06,5.400126162455392e-07,8.125732519759115e-08,1.0698655202079133e-08,1.2521124612965915e-09,1.3188639389804572e-10,1.2628854641538156e-11,1.1085093852847218e-12,8.981578667213745e-14,6.757425998892682e-15,4.745114487580903e-16],[5.4128153367291944e-05,5.701378411792296e-05,3.0026625491803216e-05,1.0542459189169758e-05,2.7761222898403167e-06,5.848240779392713e-07,1.0266694764287916e-07,1.5448604904201455e-08,2.0340233550796204e-09,2.3805103925291043e-10,2.5074179916904204e-11,2.4009919754963497e-12,2.107492891775689e-13,1.7075735622405492e-14,1.2847186905601787e-15,9.021389612023907e-17],[9.147394989731067e-06,9.635052569538442e-06,5.074353852762768e-06,1.7816243926165263e-06,4.691511818748111e-07,9.883242836893818e-08,1.7350215443465442e-08,2.610739186687632e-09,3.4374006667100464e-10,4.022946929274285e-11,4.2374146072772265e-12,4.0575598095890884e-13,3.561560614918733e-14,2.885716374221451e-15,2.1711121814004692e-16,1.5245710227259503e-17],[1.3912787875347543e-06,1.465449373491542e-06,7.717870370438274e-07,2.709772812461374e-07,7.135584373715494e-08,1.503198028122915e-08,2.6388919176169796e-09,3.970820167164365e-10,5.2281361384528016e-11,6.118726405015491e-12,6.44492236720177e-13,6.171371082775144e-14,5.416977991677768e-15,4.3890484480041485e-16,3.302166711650424e-17,2.3188058746669917e-18],[1.9237038292592494e-07,2.0262585735001917e-07,1.0671403113711123e-07,3.746769074939508e-08,9.866283527575214e-09,2.078453167505632e-09,3.648762945574815e-10,5.49040352610359e-11,7.2288786399534514e-12,8.460286695217044e-13,8.911313784229551e-14,8.533077834637644e-15,7.489987915411449e-16,6.068682554407907e-17,4.565864731762585e-18,3.2061839656951624e-19],[2.438224520161511e-08,2.568208922263286e-08,1.3525614671358982e-08,4.748893302051655e-09,1.2505154927649491e-09,2.634363668637599e-10,4.6246741035926445e-11,6.9588864456758895e-12,9.162340317216767e-13,1.0723105165215346e-13,1.1294765568943304e-14,1.0815365282540235e-15,9.493286811256052e-17,7.691834046476626e-18,5.787067206187851e-19,4.0637213704132524e-20],[2.8526406933390268e-09,3.004718072542113e-09,1.5824514311498336e-09,5.556045462482811e-10,1.4630610728481635e-10,3.082116901076733e-11,5.410713177663258e-12,8.141663120484678e-13,1.0719630050058729e-13,1.2545672435129534e-14,1.3214495883077209e-15,1.2653613669776693e-16,1.1106826318658228e-17,8.999187165067286e-19,6.770674017487822e-20,4.7544173441682835e-21],[3.099101273841546e-10,3.2643177347548574e-10,1.7191710324823522e-10,6.036073035944606e-11,1.589465664273496e-11,3.3484036165364566e-12,5.878184427657458e-13,8.845081193295619e-14,1.1645777619599738e-14,1.362958521754773e-15,1.4356193235287101e-16,1.3746852288222336e-17,1.2066426617577415e-18,9.77669303811055e-20,7.355642272564542e-21,5.165186376991479e-22],[3.142398367737867e-11,3.30992304383658e-11,1.743189321347419e-11,6.120402135870528e-12,1.6116718582729972e-12,3.395183677262981e-13,5.960307688762988e-14,8.968654538309925e-15,1.1808479087714864e-15,1.3820002173557872e-16,1.4556761526407013e-17,1.3938907565449278e-18,1.223500491176356e-19,9.913281796935414e-21,7.458406882689138e-22,5.237348445861007e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.16172710768719348, "-10": 4.080241422342123e-08, "-11": 3.860673683812795e-09, "-12": 3.354571927602235e-10, "-13": 2.6939797399544953e-11, "-14": 2.0020038923192427e-12, "-15": 1.270164921492196e-13, "-2": 0.06988939190039217, "-3": 0.02183030761018461, "-4": 0.005341605600985588, "-5": 0.0010701705740375927, "-6": 0.00018114888678475664, "-7": 2.651569378539375e-05, "-8": 3.416452269519273e-06, "-9": 3.929475965074578e-07, "0": 0.2618323143001521, "1": 0.23463984333922916, "10": 1.608002098277391e-06, "11": 2.1969689598192535e-07, "12": 2.756500077954133e-08, "13": 3.1965043600279867e-09, "14": 3.4300935782252043e-10, "15": 3.142398367737867e-11, "2": 0.14572411010044464, "3": 0.06572643557221962, "4": 0.02322266829348353, "5": 0.006718206991381125, "6": 0.0016420868374020965, "7": 0.00034707515031138256, "8": 6.457374259807248e-05, "9": 1.072445700177575e-05} |
| Raw goal margin distribution | {"-1": 0.16172710768719348, "-10": 4.080241422342123e-08, "-11": 3.860673683812795e-09, "-12": 3.354571927602235e-10, "-13": 2.6939797399544953e-11, "-14": 2.0020038923192427e-12, "-15": 1.270164921492196e-13, "-2": 0.06988939190039217, "-3": 0.02183030761018461, "-4": 0.005341605600985588, "-5": 0.0010701705740375927, "-6": 0.00018114888678475664, "-7": 2.651569378539375e-05, "-8": 3.416452269519273e-06, "-9": 3.929475965074578e-07, "0": 0.2618323143001521, "1": 0.23463984333922916, "10": 1.608002098277391e-06, "11": 2.1969689598192535e-07, "12": 2.756500077954133e-08, "13": 3.1965043600279867e-09, "14": 3.4300935782252043e-10, "15": 3.142398367737867e-11, "2": 0.14572411010044464, "3": 0.06572643557221962, "4": 0.02322266829348353, "5": 0.006718206991381125, "6": 0.0016420868374020965, "7": 0.00034707515031138256, "8": 6.457374259807248e-05, "9": 1.072445700177575e-05} |
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
| Team research json | {"base_rates": [1.520956282194674, 1.053311088058931], "coverage": {"team_news": "dated news leads; absences and tactics require confirmation", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [{"headline": "Getafe vs. Sevilla - Game Highlights", "published_at_utc": "2026-11-01T15:07:45+00:00", "source": "ESPN league news; unconfirmed context lead", "url": "https://www.espn.com/video/clip/_/id/50348131/getafe-vs-sevilla-game-highlights"}], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:17:36.715513+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-05T16:17:36.771329+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:17:36.943022+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/La_liga/2026"}, {"observed_at_utc": "2026-11-05T16:17:37.125651+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/La_liga/2025"}, {"observed_at_utc": "2026-11-05T16:17:37.137833+00:00", "reason": "HTTPError", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Sevilla+FC_vs_Deportivo+Alav%C3%A9s&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 1.9658152096820078, "goals_for": 1.4771346844204023, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 1.2630268310800783, "results": "LWLDLWWDLW", "xg_against": 1.4461597878889831, "xg_for": 0.9735333845193156, "xg_matches": 10}, "venue": {"goals_against": 1.3961941158577094, "goals_for": 1.3041211947932392, "last_match": "2026-10-26T00:00:00+00:00", "matches": 4, "points_per_game": 1.6038058841422904, "results": "WLWL", "xg_against": 1.3069157769949158, "xg_for": 0.8587582632892911, "xg_matches": 4}}}, "goal_rates": [1.520956282194674, 1.053311088058931], "h2h": [], "margin_distribution": {"-1": 0.16422662712258362, "-10": 4.080241422342123e-08, "-11": 3.860673683812795e-09, "-12": 3.354571927602235e-10, "-13": 2.6939797399544953e-11, "-14": 2.0020038923192427e-12, "-15": 1.270164921492196e-13, "-2": 0.06988939190039217, "-3": 0.02183030761018461, "-4": 0.005341605600985588, "-5": 0.0010701705740375927, "-6": 0.00018114888678475664, "-7": 2.651569378539375e-05, "-8": 3.416452269519273e-06, "-9": 3.929475965074578e-07, "0": 0.2568332754293718, "1": 0.23713936277461933, "10": 1.608002098277391e-06, "11": 2.1969689598192535e-07, "12": 2.756500077954133e-08, "13": 3.1965043600279867e-09, "14": 3.4300935782252043e-10, "15": 3.142398367737867e-11, "2": 0.14572411010044464, "3": 0.06572643557221962, "4": 0.02322266829348353, "5": 0.006718206991381125, "6": 0.0016420868374020965, "7": 0.00034707515031138256, "8": 6.457374259807248e-05, "9": 1.072445700177575e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:17:37.138097+00:00", "p_over_1_5": 0.7276063854688376, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
