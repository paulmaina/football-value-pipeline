# Ligue 1 — football model report

Fixtures in this report: **3**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,761 |
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
| Training sha256 | e02d7cce6f58dc8767248bdc40a2388c8eb56e123963a100f9048a5cd845b5c3 |
| Training as of utc | 2026-11-05T12:30:12.307455+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 81, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 81, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 144, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_CHRONOLOGICAL_PARTITIONS', 'cutoff_utc': '2026-11-05T12:30:12.307455+00:00', 'observations': 514, 'observations_sha256': 'cd8a9ee495a2993a68a29a1ab182f0496a0ed8ce5889bf97708c3da8db9d5940', 'eligible_training_matches': 186, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 183, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 23, 'retrospective_eligible_training_matches': 186, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '608386dfd0aa877d2c75d41b6593ca8164fbfef0decec13dec5d64515dfb66b9', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 126, 'tuning_matches': 17, 'audit_matches': 43, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-05T00:00:00+00:00', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1759, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1471, 'tuning_matches': 187, 'audit_matches': 96, 'audit_matchdays': 34, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8547734904983413, 'audit_candidate_poisson_score': 0.8530374480014693, 'audit_gain': 0.0017360424968719812, 'audit_gain_lower95': -0.004922765199428151, 'audit_baseline_briers': [0.5824614078047651, 0.17370432402916056, 0.21287468772376236, 0.2466063615696182], 'audit_candidate_briers': [0.5816260245758471, 0.17326240897441395, 0.21186772195909942, 0.24573349270218828], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1597.385 |
| Base scoring parameter | 0.200 |
| Home-advantage parameter | 0.202 |
| Dixon-Coles low-score adjustment | -0.054 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1761, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 3.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 4.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261105T123012307455Z_1282190333efd1da1656bb7754fc033e8e07ecb4ae0b82004aaabb0949960d69.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 3} |
| Legacy comparison status | {'None': 3} |
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

## 2026-11-06 — Toulouse vs Strasbourg

The model's most likely 1X2 outcome is **Toulouse win** at **44.7%**. Expected goals are 1.50 for Toulouse and 1.39 for Strasbourg (2.89 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.6%; Under 3.5 goals: 61.5%; Double Chance 1X: 70.1%; Double Chance X2: 55.3%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 79.2%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 44.7% | 2.24 |
| Draw | 25.4% | 3.93 |
| Strasbourg win | 29.9% | 3.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.50 |
| Strasbourg expected goals | 1.39 |
| Expected total goals | 2.89 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 60.6% |
| Under 2.5 | 39.4% |
| Over 3.5 | 38.5% |
| Under 3.5 | 61.5% |
| Over 4.5 | 20.8% |
| Under 4.5 | 79.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.52% |
| 2 | 2-1 | 9.63% |
| 3 | 1-0 | 7.19% |
| 4 | 1-2 | 6.88% |
| 5 | 2-2 | 6.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 44.7% | 46.8% | 2.09 | -6.7% |
| Draw | 25.4% | 25.2% | 4.00 | +1.7% |
| Strasbourg win | 29.9% | 28.0% | 3.50 | +4.7% |
| Over 2.5 | 60.6% | 59.5% | 1.66 | +0.5% |
| Under 2.5 | 39.4% | 40.5% | 2.42 | -4.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:45:00+00:00 |
| Fixture id | 5e7d141f719835de18877ed95bedcb32 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:30:22Z |
| Market best draw last update utc | 2026-11-05T12:29:38Z |
| Market best away last update utc | 2026-11-05T12:29:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5044 |
| Dc lambda away | 1.3887 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_CHRONOLOGICAL_PARTITIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:30:12.307455+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.88 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.78 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.60 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.80 |
| Fair Under 4.5 odds | 1.26 |
| Score matrix json | [[0.05030729226423917,0.050926645322035766,0.04210233126701849,0.021156870254039478,0.007973664619200765,0.0024041108801470257,0.0006040456720200664,0.00013008830959358104,2.4514035845635656e-05,4.106188107096354e-06,6.190209881933903e-07,8.48358122888396e-08,1.065772499691168e-08,1.2359124040653256e-09,1.330841051413536e-10,1.3375236290329824e-11],[0.07187990238470254,0.11522310628659779,0.06876036384975638,0.03455281578978612,0.01302236868915786,0.003926327447420084,0.0009865106976274965,0.0002124566319979892,4.0035645852521094e-05,6.70611293443186e-06,1.0109679701313003e-06,1.385515040360694e-07,1.7405901919078852e-08,2.0184579816018574e-09,2.1734928249227883e-10,2.1844066260055168e-11],[0.06390166034041349,0.09633379645408661,0.06728566686014342,0.028215351908558922,0.010633886322983887,0.003206184737914736,0.0008055710036617561,0.00017348914987421848,3.2692555173730255e-05,5.476119154360384e-06,8.255424744274564e-07,1.1313924363274067e-07,1.4213418985026543e-08,1.6482448958724498e-09,1.7748442065914751e-10,1.7837562657441252e-11],[0.03478747520926005,0.0524432313355875,0.039529924151923634,0.018406813291537816,0.005788989751881894,0.0017454174350455553,0.00043854543324688735,9.44458949606993e-05,1.7797525863568947e-05,2.981148820084528e-06,4.4941771794893095e-07,6.15919619631425e-08,7.737654357436646e-09,8.972893372175753e-10,9.66208835704569e-11,9.710604786068771e-12],[0.014203485773939248,0.02141220901297672,0.016139794910649038,0.008110418985727338,0.0028324169193826142,0.0007126418792719968,0.00017905507039183262,3.856160636585005e-05,7.266606843236161e-06,1.2171824658546996e-06,1.8349414911676945e-07,2.514757251769838e-08,3.159230813055838e-09,3.6635703682469973e-10,3.944963918775915e-11,3.964772841535801e-12],[0.004639348085296956,0.006993965598825026,0.005271813399017344,0.00264914242822201,0.0009984167316573847,0.00027894316664208314,5.848555848939827e-05,1.2595549959125582e-05,2.37352429405951e-06,3.975737528305268e-07,5.993551462768688e-08,8.214064087276029e-09,1.0319136905430777e-09,1.1966483751800508e-10,1.2885612091589157e-11,1.2950314861979852e-12],[0.0012628091793283713,0.0019037252208114427,0.0014349633244989167,0.0007210843666396019,0.00027176443550932107,8.193871543978505e-05,1.9077074757999196e-05,3.4284506820002447e-06,6.460623800564405e-07,1.0821774423987471e-07,1.6314171010250526e-08,2.2358304094226516e-09,2.8088215342630517e-10,3.257221757933742e-11,3.507404258389872e-12,3.525016054460163e-13],[0.0002946264359456424,0.00044415877395333496,0.0003347917776735531,0.00016823643701429158,6.340545219466616e-05,1.9117149361257954e-05,4.803285667224648e-06,9.585488645736813e-07,1.5073303199761723e-07,2.524831844224386e-08,3.806264745964413e-09,5.216423476248663e-10,6.553271003996269e-11,7.599435079613678e-12,8.183136716028464e-13,8.224226856896392e-14],[6.0146969080216934e-05,9.067347930926025e-05,6.834658483856221e-05,3.43448874259585e-05,1.294400402472154e-05,3.9026999998927876e-06,9.805741755071557e-07,2.111781324353363e-07,3.6875068745898364e-08,5.154356987006051e-09,7.770357987457687e-10,1.0649148319912889e-10,1.337827636500232e-11,1.5513984184534276e-12,1.6705590910686631e-13,1.6789475013766263e-14],[1.0914485292160213e-05,1.645393560879236e-05,1.2402417052719375e-05,6.232346773310928e-06,2.3488655157513767e-06,7.081979757239973e-07,1.7793851594036756e-07,3.832114328848949e-08,7.221293620884477e-09,1.1208471072205469e-09,1.4100371018831838e-10,1.93243274747075e-11,2.4276701362213637e-12,2.815223356958801e-13,3.031456598392521e-14,3.046678509376724e-15],[1.7825235737234643e-06,2.6872112901437033e-06,2.025528476684273e-06,1.0178496507779275e-06,3.8361022450965914e-07,1.1566093615958417e-07,2.9060426657489857e-08,6.258503214332293e-09,1.1793617167867182e-09,1.9754727805444257e-10,2.7595923402924235e-11,3.155995756827899e-12,3.964803773337215e-13,4.597744982697905e-14,4.950891136603213e-15,4.975751140937044e-16],[2.6465165793456386e-07,3.9897083754772215e-07,3.0073064808248475e-07,1.5112035631809572e-07,5.695469244485937e-08,1.7172204039331504e-08,4.314607788959109e-09,9.292013167612644e-10,1.7510008745644783e-10,2.9329886812301575e-11,4.421574230068552e-12,5.615108028592722e-13,5.886552679957392e-14,6.826281853258083e-15,7.350598706633699e-16,7.387508408475484e-17],[3.601848113352427e-08,5.4299012132363535e-08,4.092874860020611e-08,2.0567132454090393e-08,7.751402471085472e-09,2.3370974209601278e-09,5.872081832323347e-10,1.2646215919526462e-10,2.3830718635013826e-11,3.991730046363398e-12,6.017660695160977e-13,8.247105395287724e-14,9.600507239988528e-15,9.290412388215163e-16,1.0003995550273715e-16,1.005422880442401e-17],[4.5249529192421036e-09,6.821511227790629e-09,5.141823159418371e-09,2.5838209471846554e-09,9.737981762677045e-10,2.93606378301271e-10,7.377016740572423e-11,1.5887269490985363e-11,2.9938208514510997e-12,5.014756302232542e-13,7.559905490915633e-14,1.0360726621248585e-14,1.3015938919933657e-15,1.3986402763900972e-16,1.2567883887575464e-17,1.2630991243259833e-18],[5.278591465921935e-10,7.957645437278352e-10,5.998202485857377e-10,3.014160687347809e-10,1.1359859062661828e-10,3.425070162057999e-11,8.605671330890012e-12,1.8533321041926693e-12,3.492446767736941e-13,5.849972429122337e-14,8.81902051131342e-15,1.2086323128602446e-15,1.5183765517549453e-16,1.7607701595787618e-17,1.7569059537267112e-18,1.4734704155545874e-19],[5.747233132358468e-11,8.664137735974527e-11,6.530732352346105e-11,3.28176262179292e-11,1.2368405246995144e-11,3.7291532870301566e-12,9.369696389345452e-13,2.0178738482121562e-13,3.8025116939089196e-14,6.369342197646909e-15,9.60198704612519e-16,1.3159365937208848e-16,1.6531804141274075e-17,1.91709410832985e-18,2.064343338893731e-19,1.922492047422642e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.15446606275228483, "-10": 7.727239452223777e-07, "-11": 1.0399054476020288e-07, "-12": 1.2863378003958755e-08, "-13": 1.4710992492150457e-09, "-14": 1.5492817140140877e-10, "-15": 1.3375236290329824e-11, "-2": 0.08922677354264703, "-3": 0.037865016377993735, "-4": 0.012807689995317555, "-5": 0.003583187674438122, "-6": 0.0008523680048767656, "-7": 0.00017607570521194042, "-8": 3.2110565701755224e-05, "-9": 5.238412570368353e-06, "0": 0.2543543124362485, "1": 0.21693941931068325, "10": 2.225124308562491e-06, "11": 3.2440627770032755e-07, "12": 4.347263023611857e-08, "13": 5.3860247864934e-09, "14": 6.145005239519388e-10, "15": 5.747233132358468e-11, "2": 0.13542573070436528, "3": 0.06226007451627607, "4": 0.02281433335024705, "5": 0.0069146789417830505, "6": 0.0017819482707731953, "7": 0.0003987795494097904, "8": 7.878560733831977e-05, "9": 1.3924003348688017e-05} |
| Raw goal margin distribution | {"-1": 0.18445509638326138, "-10": 4.916219957094338e-07, "-11": 6.110931808086378e-08, "-12": 6.979219908564358e-09, "-13": 7.368640759520307e-10, "-14": 7.180826103119963e-11, "-15": 5.835185287903069e-12, "-2": 0.10181719008231004, "-3": 0.0406799407497681, "-4": 0.012862895788821369, "-5": 0.003349879818007555, "-6": 0.0007398044992801521, "-7": 0.00014162613966291448, "-8": 2.390587209277375e-05, "-9": 3.606428830869955e-06, "0": 0.26014436347216346, "1": 0.20034918340218924, "10": 1.0946775013001234e-06, "11": 1.4741029417081817e-07, "12": 1.8238652416416237e-08, "13": 2.086117358367154e-09, "14": 2.2023749111720667e-10, "15": 1.938817723415839e-11, "2": 0.11949564690366209, "3": 0.051722174804243216, "4": 0.017717429194367643, "5": 0.004998695357219242, "6": 0.0011959414003674287, "7": 0.0002480286436696977, "8": 4.5355347725615576e-05, "9": 7.41253512506943e-06} |
| Research history json | {"away": [{"away": "Auxerre", "away_goals": 1.0, "away_xg": 0.47, "date": "2026-11-01T00:00:00+00:00", "home": "Strasbourg", "home_goals": 5.0, "home_xg": 2.82, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 0.0, "away_xg": 0.89, "date": "2026-10-25T00:00:00+00:00", "home": "Rennes", "home_goals": 3.0, "home_xg": 1.92, "source": "pipeline training history"}, {"away": "Paris SG", "away_goals": 3.0, "away_xg": 2.69, "date": "2026-10-17T00:00:00+00:00", "home": "Strasbourg", "home_goals": 1.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 1.0, "away_xg": 0.63, "date": "2026-10-11T00:00:00+00:00", "home": "Nice", "home_goals": 2.0, "home_xg": 1.25, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 1.0, "away_xg": 0.24, "date": "2026-09-19T00:00:00+00:00", "home": "Paris FC", "home_goals": 2.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Monaco", "away_goals": 1.0, "away_xg": 1.05, "date": "2026-09-12T00:00:00+00:00", "home": "Strasbourg", "home_goals": 1.0, "home_xg": 1.01, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 6.0, "away_xg": 2.95, "date": "2026-09-06T00:00:00+00:00", "home": "Troyes", "home_goals": 2.0, "home_xg": 2.94, "source": "pipeline training history"}, {"away": "Lens", "away_goals": 1.0, "away_xg": 2.88, "date": "2026-08-29T00:00:00+00:00", "home": "Strasbourg", "home_goals": 2.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 0.0, "away_xg": 0.19, "date": "2026-08-21T00:00:00+00:00", "home": "Marseille", "home_goals": 4.0, "home_xg": 1.86, "source": "pipeline training history"}, {"away": "Monaco", "away_goals": 4.0, "away_xg": null, "date": "2026-05-17T00:00:00+00:00", "home": "Strasbourg", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [{"away": "Toulouse", "away_goals": 2.0, "away_xg": null, "date": "2026-05-03T00:00:00+00:00", "home": "Strasbourg", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 0.0, "away_xg": null, "date": "2025-12-06T00:00:00+00:00", "home": "Toulouse", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 1.0, "away_xg": null, "date": "2025-03-16T00:00:00+00:00", "home": "Strasbourg", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 2.0, "away_xg": null, "date": "2025-01-12T00:00:00+00:00", "home": "Toulouse", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 0.0, "away_xg": null, "date": "2024-04-07T00:00:00+00:00", "home": "Toulouse", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 0.0, "away_xg": null, "date": "2023-08-27T00:00:00+00:00", "home": "Strasbourg", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": null, "date": "2023-01-29T00:00:00+00:00", "home": "Strasbourg", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Toulouse", "away_goals": 0.0, "away_xg": 1.9, "date": "2026-11-01T00:00:00+00:00", "home": "Marseille", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Troyes", "away_goals": 0.0, "away_xg": 0.39, "date": "2026-10-25T00:00:00+00:00", "home": "Toulouse", "home_goals": 0.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 3.0, "away_xg": 1.81, "date": "2026-10-16T00:00:00+00:00", "home": "Le Mans", "home_goals": 0.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": 1.43, "date": "2026-10-10T00:00:00+00:00", "home": "Monaco", "home_goals": 2.0, "home_xg": 1.17, "source": "pipeline training history"}, {"away": "Le Havre", "away_goals": 2.0, "away_xg": 2.34, "date": "2026-09-19T00:00:00+00:00", "home": "Toulouse", "home_goals": 3.0, "home_xg": 1.95, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": 1.63, "date": "2026-09-12T00:00:00+00:00", "home": "Lorient", "home_goals": 2.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Lille", "away_goals": 1.0, "away_xg": 1.07, "date": "2026-09-03T00:00:00+00:00", "home": "Toulouse", "home_goals": 0.0, "home_xg": 3.41, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": 1.12, "date": "2026-08-29T00:00:00+00:00", "home": "Brest", "home_goals": 2.0, "home_xg": 2.73, "source": "pipeline training history"}, {"away": "Lyon", "away_goals": 2.0, "away_xg": 0.7, "date": "2026-08-22T00:00:00+00:00", "home": "Toulouse", "home_goals": 0.0, "home_xg": 2.76, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 0.0, "away_xg": null, "date": "2026-05-17T00:00:00+00:00", "home": "Nantes", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 34.4% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.1% |
| Raw p btts yes | 59.0% |
| P home draw | 70.1% |
| P draw away | 55.3% |
| P home away | 74.6% |
| Raw p home draw | 65.6% |
| Raw p draw away | 60.4% |
| Raw p home away | 74.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0856 |
| Totals anchor target over 2 5 | 0.6057 |
| Totals anchor reference over odds | 1.61 |
| Totals anchor reference under odds | 2.42 |
| Totals anchor reference last update utc | 2026-11-05T12:30:22Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5548 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.88, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.76, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.23, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.04, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 6.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.5, "draw": 4.0, "home": 2.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:38Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.66, "under": 2.42}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:38Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.83, "home_away": 1.29, "home_draw": 1.35}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:04Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.81, "home_away": 1.29, "home_draw": 1.34}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.66, "under": 2.42}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:10Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.17, "under": 4.75}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.45, "draw": 3.82, "home": 2.09}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.61, "under": 2.42}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.09 |
| Reference draw odds | 3.82 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-11-05T12:30:22Z |
| Market reference home last update utc | 2026-11-05T12:30:22Z |
| Market reference draw last update utc | 2026-11-05T12:30:22Z |
| Market reference away last update utc | 2026-11-05T12:30:22Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-05T12:29:38Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:29:38Z |
| Market best over 2 5 last update utc | 2026-11-05T12:29:38Z |
| Market best under 2 5 last update utc | 2026-11-05T12:29:38Z |
| Home probability edge | -2.2% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | -0.0726 |
| Raw ev home | -0.1728 |
| Raw edge prob draw | 0.0083 |
| Raw ev draw | 0.0406 |
| Raw edge prob away | 0.0644 |
| Raw ev away | 0.2043 |
| Market p home draw | 71.6% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T12:29:38Z |
| Market reference home draw last update utc | 2026-11-05T12:30:47Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.8% |
| Market draw away odds | 1.83 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T12:29:38Z |
| Market reference draw away last update utc | 2026-11-05T12:30:47Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.5% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-05T12:30:04Z |
| Market reference home away last update utc | 2026-11-05T12:30:47Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home draw odds | 1.35 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 82.4% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-05T12:30:10Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 5.10 |
| Market reference over 1 5 last update utc | 2026-11-05T12:30:50Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.9% |
| Market under 3 5 odds | 1.57 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T12:30:22Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.51 |
| Market reference under 3 5 last update utc | 2026-11-05T12:30:50Z |
| Market under 3 5 bookmakers | 2 |
| Count model | {"corners": {"alpha": 0.015413236227799179, "mu": 9.118241731788824, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,453.8748 |
| Elo away rating | 1,507.0944 |
| Elo rating diff | 6.7804 |
| Elo home expectancy | 0.5098 |

</details>


---

## 2026-11-07 — Auxerre vs Paris FC

The model's most likely 1X2 outcome is **Paris FC win** at **51.3%**. Expected goals are 1.22 for Auxerre and 1.51 for Paris FC (2.73 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 52.3%; Under 3.5 goals: 70.4%; Double Chance 1X: 48.7%; Double Chance X2: 75.6%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 85.5%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 24.4% | 4.09 |
| Draw | 24.2% | 4.12 |
| Paris FC win | 51.3% | 1.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.22 |
| Paris FC expected goals | 1.51 |
| Expected total goals | 2.73 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 76.6% |
| Under 1.5 | 23.4% |
| Over 2.5 | 52.3% |
| Under 2.5 | 47.7% |
| Over 3.5 | 29.6% |
| Under 3.5 | 70.4% |
| Over 4.5 | 14.5% |
| Under 4.5 | 85.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.53% |
| 2 | 0-1 | 10.92% |
| 3 | 1-2 | 10.76% |
| 4 | 0-2 | 8.82% |
| 5 | 0-0 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 24.4% | 22.0% | 4.33 | +5.7% |
| Draw | 24.2% | 23.2% | 4.11 | -0.4% |
| Paris FC win | 51.3% | 54.8% | 1.87 | -4.0% |
| Over 2.5 | 52.3% | 55.8% | 1.77 | -7.4% |
| Under 2.5 | 47.7% | 44.2% | 2.22 | +5.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T18:00:00+00:00 |
| Fixture id | 8553a80cf1ae5cbe3e7a69b76ce8167f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:30:22Z |
| Market best draw last update utc | 2026-11-05T12:30:22Z |
| Market best away last update utc | 2026-11-05T12:29:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2203 |
| Dc lambda away | 1.5084 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_CHRONOLOGICAL_PARTITIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:30:12.307455+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.31 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.28 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.38 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.87 |
| Fair Under 4.5 odds | 1.17 |
| Score matrix json | [[0.06530920516572888,0.10917905459714766,0.08815809186126915,0.04432699754649696,0.0167161289735536,0.005043047954102826,0.0012678539744267808,0.0002732112544011385,5.151527080990744e-05,8.634175394779718e-06,1.3024115998655218e-06,1.786006188310964e-07,2.2450659450488333e-08,2.605032457647259e-09,2.806806619158438e-10,2.8225953510136813e-11],[0.05941158336636215,0.11525014347742572,0.10757925718171867,0.054092203772425865,0.020398680370244723,0.006154027853596488,0.0015471613087810684,0.0003333995006200094,6.286404855456832e-05,1.0536278130982936e-05,1.5893319546761066e-06,2.1794620891160505e-07,2.7396523857662553e-08,3.1789192666394512e-09,3.4251441333028073e-10,3.44441111162513e-11],[0.03946692315136248,0.05953339626898692,0.05031756886764086,0.03300433901358242,0.012446247618265094,0.0037548779198133715,0.0009439999257293753,0.00020342358746772116,3.8356477007115864e-05,6.4287063777131845e-06,9.69730330417584e-07,1.3297980233725423e-07,1.671597934881925e-08,1.9396164669937243e-09,2.0898504823634967e-10,2.1016062223772076e-11],[0.016053819474499787,0.024216187128161804,0.018264305262608596,0.010291315412485224,0.005062715723550213,0.0015273582904419586,0.0003839874806931187,8.274588666406272e-05,1.5602127259539926e-05,2.614981949481158e-06,3.9445374557741497e-07,5.40917195974332e-08,6.79949926109572e-09,7.889708678698801e-10,8.500810221229942e-11,8.548628625326322e-12],[0.004897616139179539,0.007387749008680848,0.005571979700353572,0.002801661484408948,0.0011839807865875265,0.00046595856054443936,0.00011714491281484322,2.5243686751327564e-05,4.7598162165229345e-06,7.977651561228328e-07,1.2033790672483953e-07,1.650202179719089e-08,2.074356035482913e-09,2.4069514808982315e-10,2.5933831759931012e-11,2.6079713671724176e-12],[0.0011953115025294897,0.0018030529786183663,0.0013598965779317252,0.0006837731058009925,0.0002578572891887641,8.717629243361566e-05,2.8590370860271948e-05,6.160970619712135e-06,1.1616800728873318e-06,1.9470245121958494e-07,2.9369652502537315e-08,4.0274811068551855e-09,5.06267040758643e-10,5.874402381461478e-11,6.329407312942898e-12,6.365011231711136e-13],[0.00024310629693385471,0.0003667107125463754,0.0002765801387959509,0.00013906797294468358,5.244384462077574e-05,1.582165486629802e-05,4.457482456502129e-06,1.253038015368334e-06,2.3626622863065964e-07,3.959921059888738e-08,5.973294364704581e-09,8.191220579628538e-10,1.0296621866186567e-10,1.194754845606687e-11,1.2872952116493546e-12,1.2945364511335927e-13],[4.2380348900438425e-05,6.392811761462647e-05,4.8215792552232134e-05,2.4243507011568747e-05,9.142455217083853e-06,2.758164892777207e-06,6.934200018040708e-07,1.674508325537325e-07,4.118793025539152e-08,6.903269814600505e-09,1.0413152701267992e-09,1.427962954738116e-10,1.794994340700276e-11,2.0827978479338837e-12,2.2441220526018372e-13,2.2567455946360913e-14],[6.464588725709295e-06,9.751429592007365e-06,7.3547121961299745e-06,3.6980418086416525e-06,1.3945664548564156e-06,4.207233336229157e-07,1.0577249225519099e-07,2.2793031274158245e-08,4.816161989389152e-09,1.0530069093776162e-09,1.5883953600724128e-10,2.1781777303478168e-11,2.7380379064040577e-12,3.177045926949808e-13,3.4231256931005024e-14,3.4423813173769486e-15],[8.765258947043183e-07,1.322184737566983e-06,9.972166771209823e-07,5.014130894487724e-07,1.890876065644114e-07,5.7045376291335155e-08,1.434156639236388e-08,3.090479994674835e-09,5.827245814131881e-10,1.094485004074926e-10,2.1536863723359283e-11,2.953365271831211e-12,3.7124730241548837e-13,4.3077187765426586e-14,4.641375403972117e-15,4.667483875853521e-16],[1.069623929715058e-07,1.6134611006360974e-07,1.2169028061850394e-07,6.118740386188862e-08,2.307434726295989e-08,6.961243236447137e-09,1.750100333093341e-09,3.7713105529243685e-10,7.110983947861522e-11,1.1918307265016161e-11,2.0146683514696723e-12,3.6039895535610095e-13,4.530328207128698e-14,5.256706178004259e-15,5.663867124603517e-16,5.695727274385016e-17],[1.1866012048571351e-08,1.789914036903544e-08,1.3499869401742577e-08,6.787904152811795e-09,2.5597826958503104e-09,7.72254563701864e-10,1.941496544886244e-10,4.183752365359487e-11,7.888662440919809e-12,1.3221729027970746e-12,1.9944155022284113e-13,3.0648691833905737e-14,5.0257784625379806e-15,5.831595302903764e-16,6.283284589561884e-17,6.318629060704867e-18],[1.206673842925528e-09,1.8201923616593548e-09,1.3728234240209408e-09,6.902728866240883e-10,2.6030841785870686e-10,7.853180818328089e-11,1.9743390511107582e-11,4.2545250450549814e-12,8.02210766697566e-13,1.344538882228957e-13,2.0281531896421394e-14,2.781220735378505e-15,3.9178084531527933e-16,5.930243021612781e-17,6.389573119297678e-18,6.425515480257446e-19],[1.1326947981205243e-10,1.7085995786829254e-10,1.2886580414774898e-10,6.479534735476966e-11,2.4434936792919133e-11,7.371716154925466e-12,1.85329580651015e-12,3.9936876192854425e-13,7.530286396459912e-14,1.2621075750504323e-14,1.9038106951332843e-15,2.6107089980093293e-16,3.2817433121025684e-17,4.267271183039852e-18,5.997839662200985e-19,6.031578460410613e-20],[9.873047581963826e-12,1.4892877557882907e-11,1.123248926498008e-11,5.6478368982095786e-12,2.129852578285605e-12,6.425500009276661e-13,1.6154111161709218e-13,3.481067270559626e-14,6.5637165476019724e-15,1.100106415488632e-15,1.6594420325132022e-16,2.275604532021922e-17,2.8605064599875218e-18,3.3191506868699434e-19,4.0076327798567347e-20,5.257379236913003e-21],[8.032048656852136e-13,1.2115845304339485e-12,9.137999140073407e-13,4.594700916387257e-13,1.7327050638308807e-13,5.227355412871249e-14,1.3141900287817536e-14,2.8319626197272816e-15,5.339799108882461e-16,8.949727207900597e-17,1.3500106261738948e-17,1.851279067908404e-18,2.327116007405039e-19,2.700238157979259e-20,2.909386527170339e-21,3.278680899978413e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2553212107482586, "-10": 1.5378893293266988e-06, "-11": 2.0802437522933218e-07, "-12": 2.584711239398946e-08, "-13": 2.9685629332013118e-09, "-14": 3.151247730320951e-10, "-15": 2.8225953510136813e-11, "-2": 0.15634745075717382, "-3": 0.0688909893467566, "-4": 0.02390186327708362, "-5": 0.006810062949814185, "-6": 0.0016423494044749331, "-7": 0.00034291548354323844, "-8": 6.307750540082737e-05, "-9": 1.0363533805063222e-05, "0": 0.2424440198632471, "1": 0.14028534213429988, "10": 1.2630133423804935e-07, "11": 1.3820891321783047e-08, "12": 1.3892257601504392e-09, "13": 1.2907615728394268e-10, "14": 1.1084632112397776e-11, "15": 8.032048656852136e-13, "2": 0.06999417403061721, "3": 0.024950110939330243, "4": 0.007002946168189429, "5": 0.0016141322967671355, "6": 0.000314914406585299, "7": 5.319282277657316e-05, "8": 7.915519492554681e-06, "9": 1.0520872376849888e-06} |
| Raw goal margin distribution | {"-1": 0.2151662053912753, "-10": 1.2960216283371046e-06, "-11": 1.7530786148087966e-07, "-12": 2.1782072385752402e-08, "-13": 2.5016896165038904e-09, "-14": 2.655643118697111e-10, "-15": 2.3786787210228314e-11, "-2": 0.13175829616125936, "-3": 0.058056331160075726, "-4": 0.020142757462410437, "-5": 0.005739027318149387, "-6": 0.001384053006218569, "-7": 0.00028898430783591355, "-8": 5.315714837348767e-05, "-9": 8.733634924981913e-06, "0": 0.2665286487235395, "1": 0.17282490003873646, "10": 1.5559726434963698e-07, "11": 1.7026683791715842e-08, "12": 1.7114603669668385e-09, "13": 1.590157149748819e-10, "14": 1.3655741987337132e-11, "15": 9.89510368729633e-13, "2": 0.08622950870059344, "3": 0.03073735547450931, "4": 0.008627298141635821, "5": 0.001988534572421803, "6": 0.00038795964005105675, "7": 6.553103937500947e-05, "8": 9.75154527367372e-06, "9": 1.296121668298528e-06} |
| Research history json | {"away": [{"away": "Monaco", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-11-01T00:00:00+00:00", "home": "Paris FC", "home_goals": 3.0, "home_xg": 2.15, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 1.0, "away_xg": 0.42, "date": "2026-10-24T00:00:00+00:00", "home": "Lens", "home_goals": 2.0, "home_xg": 1.06, "source": "pipeline training history"}, {"away": "Rennes", "away_goals": 3.0, "away_xg": 3.35, "date": "2026-10-18T00:00:00+00:00", "home": "Paris FC", "home_goals": 4.0, "home_xg": 3.62, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 0.0, "away_xg": 0.97, "date": "2026-10-10T00:00:00+00:00", "home": "Lorient", "home_goals": 1.0, "home_xg": 0.55, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 1.0, "away_xg": 0.24, "date": "2026-09-19T00:00:00+00:00", "home": "Paris FC", "home_goals": 2.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Lyon", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-09-12T00:00:00+00:00", "home": "Paris FC", "home_goals": 0.0, "home_xg": 0.3, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 3.0, "away_xg": 3.29, "date": "2026-09-06T00:00:00+00:00", "home": "Marseille", "home_goals": 2.0, "home_xg": 1.42, "source": "pipeline training history"}, {"away": "Nice", "away_goals": 0.0, "away_xg": 0.65, "date": "2026-08-30T00:00:00+00:00", "home": "Paris FC", "home_goals": 3.0, "home_xg": 2.88, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 0.0, "away_xg": 1.8, "date": "2026-08-22T00:00:00+00:00", "home": "Troyes", "home_goals": 0.0, "home_xg": 0.41, "source": "pipeline training history"}, {"away": "Paris SG", "away_goals": 1.0, "away_xg": null, "date": "2026-05-17T00:00:00+00:00", "home": "Paris FC", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [{"away": "Paris FC", "away_goals": 0.0, "away_xg": null, "date": "2026-02-08T00:00:00+00:00", "home": "Auxerre", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Auxerre", "away_goals": 1.0, "away_xg": null, "date": "2025-11-29T00:00:00+00:00", "home": "Paris FC", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Auxerre", "away_goals": 1.0, "away_xg": 0.47, "date": "2026-11-01T00:00:00+00:00", "home": "Strasbourg", "home_goals": 5.0, "home_xg": 2.82, "source": "pipeline training history"}, {"away": "Le Mans", "away_goals": 1.0, "away_xg": 1.33, "date": "2026-10-25T00:00:00+00:00", "home": "Auxerre", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Auxerre", "away_goals": 3.0, "away_xg": 2.7, "date": "2026-10-18T00:00:00+00:00", "home": "Le Havre", "home_goals": 1.0, "home_xg": 1.4, "source": "pipeline training history"}, {"away": "Auxerre", "away_goals": 1.0, "away_xg": 1.76, "date": "2026-10-11T00:00:00+00:00", "home": "Rennes", "home_goals": 4.0, "home_xg": 2.56, "source": "pipeline training history"}, {"away": "Brest", "away_goals": 1.0, "away_xg": 0.34, "date": "2026-09-20T00:00:00+00:00", "home": "Auxerre", "home_goals": 2.0, "home_xg": 0.96, "source": "pipeline training history"}, {"away": "Nice", "away_goals": 0.0, "away_xg": 1.08, "date": "2026-09-12T00:00:00+00:00", "home": "Auxerre", "home_goals": 1.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Auxerre", "away_goals": 1.0, "away_xg": 0.71, "date": "2026-09-04T00:00:00+00:00", "home": "Lyon", "home_goals": 3.0, "home_xg": 2.85, "source": "pipeline training history"}, {"away": "Angers", "away_goals": 3.0, "away_xg": 1.74, "date": "2026-08-29T00:00:00+00:00", "home": "Auxerre", "home_goals": 1.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Auxerre", "away_goals": 2.0, "away_xg": 1.85, "date": "2026-08-22T00:00:00+00:00", "home": "Lens", "home_goals": 5.0, "home_xg": 4.42, "source": "pipeline training history"}, {"away": "Auxerre", "away_goals": 2.0, "away_xg": null, "date": "2026-05-17T00:00:00+00:00", "home": "Lille", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 43.3% |
| Raw p over 1 5 | 76.3% |
| Raw p under 3 5 | 70.8% |
| Raw p btts yes | 55.5% |
| P home draw | 48.7% |
| P draw away | 75.6% |
| P home away | 75.8% |
| Raw p home draw | 56.7% |
| Raw p draw away | 69.9% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5232 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:38Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.36, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:38Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.09, "price": 1.36, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.79, "draw": 4.11, "home": 4.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.87, "draw": 4.04, "home": 4.3}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:38Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.77, "under": 2.22}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.33 |
| Reference draw odds | 4.11 |
| Reference away odds | 1.79 |
| Market reference 1x2 last update utc | 2026-11-05T12:30:22Z |
| Market reference home last update utc | 2026-11-05T12:30:22Z |
| Market reference draw last update utc | 2026-11-05T12:30:22Z |
| Market reference away last update utc | 2026-11-05T12:30:22Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-05T12:29:38Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:29:38Z |
| Market best over 2 5 last update utc | 2026-11-05T12:29:38Z |
| Market best under 2 5 last update utc | 2026-11-05T12:29:38Z |
| Home probability edge | +2.4% |
| Draw probability edge | +1.0% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0809 |
| Raw ev home | 0.3028 |
| Raw edge prob draw | 0.0344 |
| Raw ev draw | 0.0954 |
| Raw edge prob away | -0.1153 |
| Raw ev away | -0.1910 |
| Count model | {"corners": {"alpha": 0.015413236227799179, "mu": 9.292628239207868, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,456.4699 |
| Elo away rating | 1,497.8028 |
| Elo rating diff | 18.6671 |
| Elo home expectancy | 0.5268 |

</details>


---

## 2026-11-07 — Paris Saint Germain vs Troyes

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **88.4%**. Expected goals are 3.33 for Paris Saint Germain and 0.58 for Troyes (3.91 combined). The most likely exact score is 3-0 at 12.4%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 75.2%; Under 3.5 goals: 45.1%; Double Chance 1X: 95.9%; Double Chance X2: 11.6%; Double Chance 12 (either team wins): 92.5%; Under 4.5 goals: 64.5%; BTTS Yes (both teams score): 42.2%; BTTS No (at least one team does not score): 57.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 88.4% | 1.13 |
| Draw | 7.5% | 13.35 |
| Troyes win | 4.1% | 24.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 3.33 |
| Troyes expected goals | 0.58 |
| Expected total goals | 3.91 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 90.4% |
| Under 1.5 | 9.6% |
| Over 2.5 | 75.2% |
| Under 2.5 | 24.8% |
| Over 3.5 | 54.9% |
| Under 3.5 | 45.1% |
| Over 4.5 | 35.5% |
| Under 4.5 | 64.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 12.41% |
| 2 | 2-0 | 11.16% |
| 3 | 4-0 | 10.34% |
| 4 | 3-1 | 7.14% |
| 5 | 5-0 | 6.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 88.4% | 88.5% | 1.14 | +0.8% |
| Draw | 7.5% | 7.0% | 11.64 | -12.8% |
| Troyes win | 4.1% | 4.5% | 22.00 | -9.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T20:05:00+00:00 |
| Fixture id | f7b240389fa5ec055c58a48ab153dcdd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:29:38Z |
| Market best draw last update utc | 2026-11-05T12:30:22Z |
| Market best away last update utc | 2026-11-05T12:29:38Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris SG |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.3337 |
| Dc lambda away | 0.5755 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_CHRONOLOGICAL_PARTITIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:30:12.307455+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 42.2% |
| P btts no | 57.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 51.61 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.37 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 4.03 |
| Fair Over 3.5 odds | 1.82 |
| Fair Under 3.5 odds | 2.22 |
| Fair Over 4.5 odds | 2.82 |
| Fair Under 4.5 odds | 1.55 |
| Score matrix json | [[0.019376553390001754,0.012186348821580817,0.004277104702890206,0.000820491610102283,0.00011804828190083658,1.3587363174136262e-05,1.3032551529844672e-06,1.0714623824754434e-07,7.707835876398281e-09,4.928734979963305e-10,2.8364882183582242e-11,1.4839997107118435e-12,7.117018384016285e-14,3.1506506667482798e-15,1.295143035502811e-16,4.969034280570115e-18,1.7873002974842706e-19,6.05053982302923e-21,1.934492881765949e-22,5.859479679593027e-24,1.6860660133321687e-25,4.620625780809232e-27],[0.06489301785177172,0.035502937578309204,0.014258577980323997,0.0027352717357934896,0.0003935373926640009,4.529617365562482e-05,4.344659885116008e-06,3.5719326494827717e-07,2.5695601706663437e-08,1.6430916925804659e-09,9.455996815883705e-11,4.947207765024929e-12,2.3725994256657456e-13,1.0503319731741278e-14,4.317616530385977e-16,1.656526264800931e-17,5.958320507963009e-19,2.017067616591677e-20,6.44901622080995e-22,1.9533739232323326e-23,5.620835916133954e-25,1.540377371847918e-26],[0.11163861061845853,0.06424804843848511,0.016155506036222355,0.004559285784590809,0.0006559675284172112,7.550189545776043e-05,7.2418932985263294e-06,5.953873444891298e-07,4.283069577864527e-08,2.7387862415023168e-09,1.5761721695737764e-10,8.246249811795065e-12,3.9547656974666493e-13,1.7507451167387645e-14,7.196816101560921e-16,2.7611796488355947e-17,9.931622381975511e-19,3.362147749542356e-20,1.0749538188608783e-21,3.2559799612011726e-23,9.369086425525733e-25,2.567576947646197e-26],[0.12405649348437903,0.07139454314540852,0.02054378875211165,0.003443895041775918,0.0007289326780783041,8.390018784742248e-05,8.047429861641936e-06,6.616139865331238e-07,4.7594876919010985e-08,3.043429290653156e-09,1.7514943208426018e-10,9.163503830621585e-12,4.3946656292307706e-13,1.945485517638645e-14,7.997338598765644e-16,3.068313580913881e-17,1.1036345225843785e-18,3.7361290871856976e-20,1.1945240153631375e-21,3.618151951232151e-23,1.0411236781467443e-24,2.853175895971307e-26],[0.10339173980924986,0.05950197221735773,0.01712169997471337,0.003284514211318667,0.00041295409321127045,6.992448479095679e-05,6.7069264253615185e-06,5.514054059444036e-07,3.9666743694341886e-08,2.5364689949638396e-09,1.4597385433978887e-10,7.637089983653216e-12,3.662622669109175e-13,1.6214155889202742e-14,6.66517913207151e-16,2.5572081758943304e-17,9.19796217018804e-19,3.1137820812637596e-20,9.955457608341743e-22,3.015457027884063e-23,8.676981382981914e-25,2.3779071258646685e-26],[0.0689353797486122,0.0396723283519789,0.01141571746327337,0.0021899160887000513,0.00031507431470970723,3.169083025471161e-05,4.471774253255531e-06,3.6764388648786894e-07,2.644739362162945e-08,1.6911646298921254e-09,9.732656690802383e-11,5.091951244545718e-12,2.4420160163348776e-13,1.0810621772953194e-14,4.443939674577072e-16,1.704992265598384e-17,6.132646730629402e-19,2.0760821959506077e-20,6.637699027682392e-22,2.0105249772981604e-23,5.785288145949001e-25,1.5854451335361585e-26],[0.03830162988078659,0.022042597612253276,0.006342760229890967,0.001216753368230452,0.0001750604672225169,2.0149468567313876e-05,1.6888962335698476e-06,2.0426898523723242e-07,1.469460653587711e-08,9.396388611743257e-10,5.4076240050796105e-11,2.8291717932188097e-12,1.35682423106539e-13,6.006559120132535e-15,2.469125915442873e-16,9.473217228177786e-18,3.40739930820374e-19,1.1535053866587526e-20,3.688014664537571e-22,1.1170807186001075e-23,3.2144011700218656e-25,8.80899371591824e-27],[0.01824087001322792,0.01049762527209567,0.003020692989792337,0.0005794698579963698,8.337126218909873e-05,9.596036464139265e-06,9.204202323760545e-07,6.61269874290414e-08,6.998198472251516e-09,4.474961086357402e-10,2.5753412286652898e-11,1.3473722942292555e-12,6.461775779958903e-14,2.8605796797192615e-15,1.1759030884604455e-16,4.5115501508447425e-18,1.622748902789792e-19,5.493484711509723e-21,1.7563899059150593e-22,5.32001490424546e-24,1.5308349565079252e-25,4.195218579980343e-27],[0.007601195364027786,0.004374489840325003,0.0012587600006748563,0.0002414722321359491,3.4741832554333205e-05,3.9987866714340554e-06,3.835504555550622e-07,3.153334049494961e-08,1.982305630637867e-09,1.8647714412282732e-10,1.073176432589253e-11,5.614666421660732e-13,2.6927016127186806e-14,1.1920388108761229e-15,4.900133106627939e-17,1.880018555382017e-18,6.762194691328847e-20,2.2892027897355682e-21,7.319093223396204e-23,2.216915782930536e-24,6.37917794823459e-26,1.748199290829043e-27],[0.002815566042151767,0.0016203589641235752,0.0004662584953271181,8.944396037260985e-05,1.2868755412473808e-05,1.4811943941318315e-06,1.420712909476439e-07,1.168029480117764e-08,8.4025157381098e-10,4.6952362160146015e-11,3.975163084395144e-12,2.0797339573260245e-13,9.974061788093129e-15,4.415442356228743e-16,1.8150629889526462e-17,6.96379470550006e-19,2.5047910008243353e-20,8.479457940103798e-22,2.711072318527786e-23,8.211698947074583e-25,2.3629174028195713e-26,6.4755217073697915e-28],[0.0009386248586256228,0.0005401788417866101,0.0001554365295317131,2.9817920589600345e-05,4.290055196321996e-06,4.937855685056295e-07,4.7362286440484055e-08,3.893858248156126e-09,2.801145499238749e-10,1.7911777089519606e-11,9.008019073646027e-13,6.933206191754543e-14,3.325051586649128e-15,1.471975402224074e-16,6.0508729537747616e-18,2.3215192693375737e-19,8.350218264596987e-21,2.826795710382001e-22,9.037898005607561e-24,2.7375329322353677e-25,7.877254448879991e-27,2.158743768077984e-28],[0.00028446294377894364,0.00016370849556095985,4.71071401476803e-05,9.036723660509434e-06,1.3001591838371065e-06,1.4964838734224868e-07,1.4353780747602562e-08,1.1800863462643596e-09,8.489249856788755e-11,5.4284060265116605e-12,3.124049031092304e-13,1.42828796730873e-14,1.0077018031889975e-15,4.461020313269425e-17,1.833798793038032e-18,7.035677771865919e-20,2.5306464525369848e-21,8.566986286879095e-23,2.7390570882742947e-24,8.296463378731765e-26,2.3873083786692423e-27,6.542364625107843e-29],[7.902614323118661e-05,4.5479565269548904e-05,1.3086750615275476e-05,2.5104760882001844e-06,3.6119490475743044e-07,4.157355167362232e-08,3.98759823757773e-09,3.2783768383387593e-10,2.3583833669008713e-11,1.5080557997090555e-12,8.678864913392793e-14,4.540626305945584e-15,1.9029401794247888e-16,1.2393080995028282e-17,5.094443731427336e-19,1.95456909761864e-20,7.030343789913537e-22,2.3799791859449656e-23,7.609325661221108e-25,2.3048256991583666e-26,6.632138842531806e-28,1.8175226518649675e-29],[2.026533410979023e-05,1.1662704867921485e-05,3.3559447897414267e-06,6.437823563422815e-07,9.262422692512917e-08,1.066105316985915e-08,1.0225731292961897e-09,8.40701560904646e-11,6.047799492049249e-12,3.867233473346364e-13,2.2255938348036694e-14,1.1643907369805247e-15,5.584226345498118e-17,2.1602811800389045e-18,1.3064107661040315e-19,5.012264825835684e-21,1.8028497910177903e-22,6.103179454984152e-24,1.9513229492134838e-25,5.910457090336966e-27,1.700734769672834e-28,4.660825175841301e-30],[4.825608289018907e-06,2.7771387818291267e-06,7.991220330802468e-07,1.5329831022073362e-07,2.205580400462977e-08,2.538624148382034e-09,2.4349647245518686e-10,2.0018897289893177e-11,1.440110052025157e-12,9.208707738766598e-14,5.299613615563101e-15,2.7726626965975127e-16,1.3297233983216287e-17,5.886585765918181e-19,2.1145894519179085e-20,1.1935271611744948e-21,4.2929698806142735e-23,1.4532972023941768e-24,4.6465161379838105e-26,1.4074058968138014e-27,4.049812234771413e-29,1.1098418846863318e-30],[1.0724749080061714e-06,6.172095788089968e-07,1.776021337794259e-07,3.4070024192723826e-08,4.9018268691006005e-09,5.642005187602577e-10,5.4116256698758464e-11,4.44913133090796e-12,3.2005952473992685e-13,2.0466037426749643e-14,1.1778209677219453e-15,6.162147842029103e-17,2.9552646917775025e-18,1.3082735169656873e-19,5.3779409818849736e-21,1.8030816521683072e-22,9.540978467444396e-24,3.229903237256342e-25,1.0326722910712101e-26,3.1279113830012134e-28,9.000568930993313e-30,2.466585561635722e-31],[2.2345675652698822e-07,1.2859941948147964e-07,3.700449909863476e-08,7.098699507157401e-09,1.0213258371353514e-09,1.175546551363101e-10,1.1275455590628027e-11,9.270039318827348e-13,6.668637444107163e-14,4.264225025873618e-15,2.4540625729502836e-16,1.2839214789458549e-17,6.157476112247937e-19,2.725868498823899e-20,1.1205271467280494e-21,4.2990910283816374e-23,1.3512860068774786e-24,6.729702447165957e-26,2.15163635993187e-27,6.517196133275644e-29,1.8753240054412297e-30,5.139283028300428e-32],[4.381985161484034e-08,2.5218335605584825e-08,7.2565792361164335e-09,1.392054390731338e-09,2.002819128374327e-10,2.3052458223990607e-11,2.2111159158947517e-12,1.8178539495881806e-13,1.3077192554643163e-14,8.362141775896705e-16,4.8124146913958665e-17,2.517768966440659e-18,1.2074805602400336e-19,5.345425888950665e-21,2.1973528150666276e-22,8.43051397819883e-24,3.0323518193662545e-25,8.970595777272158e-27,4.219357135881564e-28,1.2780216268397253e-29,3.6775088355074097e-31,1.0078129800456177e-32],[8.115676566001175e-09,4.67057390122437e-09,1.3439582263655143e-09,2.578160988941205e-10,3.7093307409972284e-11,4.269441545388567e-12,4.0951078020679523e-13,3.366765097417419e-14,2.421967698513606e-15,1.5487144650494639e-16,8.912855634502933e-18,4.663046050258038e-19,2.236320143841664e-20,9.900021570945018e-22,4.0696177853859934e-23,1.5613773714615277e-24,5.61608168293461e-26,1.9012096579299046e-27,5.31187844115683e-29,2.366966063452666e-30,6.810947818792265e-32,1.8665248474502006e-33],[1.423958928660319e-09,8.194887209376918e-10,2.3580798231867135e-10,4.52358510084816e-11,6.508310903030183e-12,7.491069117290992e-13,7.185186929466839e-14,5.907252688276697e-15,4.249531756444363e-16,2.7173406585610037e-17,1.5638302312070046e-18,8.181679006080547e-20,3.923798601716979e-21,1.7370362156784446e-22,7.14046270154722e-24,2.7395587182650926e-25,9.85385456340431e-27,3.335821044182463e-28,1.0665365824474891e-29,2.823012341166526e-31,1.1950340652852685e-32,3.2749638313921304e-34],[2.3735249468363264e-10,1.3659642027923935e-10,3.930563708203831e-11,7.54013466954528e-12,1.084837348830163e-12,1.2486483332137433e-13,1.1976623820756332e-14,9.846500022357992e-16,7.083329043614543e-17,4.529397381015155e-18,2.606669329907394e-19,1.3637625943473867e-20,6.5403809618994905e-22,2.895377604289357e-23,1.1902075272649624e-24,4.5664315383328565e-26,1.6424890604633673e-27,5.560310980315789e-29,1.7777557584011916e-30,5.384730975139135e-32,1.3540186182555631e-33,5.45887117763224e-35],[3.7679127636039716e-11,2.168434741411841e-11,6.239673690407198e-12,1.196977925112645e-12,1.7221527410275566e-13,1.9821986696368696e-14,1.901259720032047e-15,1.563107780287757e-16,1.1244611499793259e-17,7.190307490177924e-19,4.138023765768478e-20,2.1649397418874175e-21,1.0382694708147459e-22,4.596341085521885e-24,1.8894253204697505e-25,7.249098308548164e-27,2.60741118531272e-28,8.826857598553774e-30,2.8221437577804477e-31,8.548128637469723e-33,2.4597250884621485e-34,5.8905778137066714e-36]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.03180775298132451, "-10": 3.372770528767352e-11, "-11": 1.739593035365048e-12, "-12": 8.242480924909426e-14, "-13": 3.611159563714172e-15, "-14": 1.4711110570400579e-16, "-15": 5.5997130747852905e-18, "-16": 2.0001272480530668e-19, "-17": 6.729066147471642e-21, "-18": 2.1394846781043055e-22, "-19": 6.4472390406828834e-24, "-2": 0.007759333878305932, "-20": 1.8401037505169604e-25, "-21": 4.620625780809232e-27, "-3": 0.0012981571468491156, "-4": 0.0001712893762008321, "-5": 1.8577641971222257e-05, "-6": 1.7064737474003362e-06, "-7": 1.3576366304543442e-07, "-8": 9.518085614148051e-09, "-9": 5.961358507175512e-10, "0": 0.07492529402316948, "1": 0.1533055458490174, "10": 0.001116086518622414, "11": 0.0003334567737751921, "12": 9.152308495016601e-05, "13": 2.322737834910809e-05, "14": 5.481252275864526e-06, "15": 1.2085953578996578e-06, "16": 2.5006539086928257e-07, "17": 4.8733945848327026e-08, "18": 8.975667901946019e-09, "19": 1.5667950226299655e-09, "2": 0.2025298218473484, "20": 2.5903684209775103e-10, "21": 3.7679127636039716e-11, "3": 0.19627845263367338, "4": 0.15002256984241327, "5": 0.09425351981153425, "6": 0.05015190289064261, "7": 0.023112779045121552, "8": 0.009386399685314647, "9": 0.0034054577180818255} |
| Raw goal margin distribution | {"-1": 0.02470021056761838, "-10": 2.6191143494394097e-11, "-11": 1.3508755019792613e-12, "-12": 6.400672646205988e-14, "-13": 2.804234604983867e-15, "-14": 1.142386665872805e-16, "-15": 4.3484395815904265e-18, "-16": 1.5531925256697153e-19, "-17": 5.225435159269808e-21, "-18": 1.6614100998079686e-22, "-19": 5.006583205614604e-24, "-2": 0.006025486326278389, "-20": 1.4289267818043968e-25, "-21": 3.5881324219024286e-27, "-3": 0.001008079850716215, "-4": 0.00013301422652020275, "-5": 1.442640946087688e-05, "-6": 1.3251568230440256e-06, "-7": 1.0542684566942904e-07, "-8": 7.391239456874278e-09, "-9": 4.6292742050264365e-10, "0": 0.08559494325138134, "1": 0.15304622506986434, "10": 0.0011141986258915374, "11": 0.0003328927219666919, "12": 9.136827099631763e-05, "13": 2.3188088564659545e-05, "14": 5.471980578594607e-06, "15": 1.2065509837828856e-06, "16": 2.4964239800467146e-07, "17": 4.865151096484905e-08, "18": 8.960485299249805e-09, "19": 1.5641447433866974e-09, "2": 0.2021872367770411, "20": 2.5859867376306933e-10, "21": 3.7615392298337e-11, "3": 0.19594644193578217, "4": 0.14976880231243497, "5": 0.09409408724789096, "6": 0.0500670694916838, "7": 0.023073683108720943, "8": 0.009370522317888975, "9": 0.003399697287538136} |
| Research history json | {"away": [{"away": "Le Mans", "away_goals": 0.0, "away_xg": 0.2, "date": "2026-10-31T00:00:00+00:00", "home": "Troyes", "home_goals": 2.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Troyes", "away_goals": 0.0, "away_xg": 0.39, "date": "2026-10-25T00:00:00+00:00", "home": "Toulouse", "home_goals": 0.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Lens", "away_goals": 3.0, "away_xg": 1.43, "date": "2026-10-17T00:00:00+00:00", "home": "Troyes", "home_goals": 1.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Marseille", "away_goals": 2.0, "away_xg": 1.3, "date": "2026-10-11T00:00:00+00:00", "home": "Troyes", "home_goals": 0.0, "home_xg": 1.06, "source": "pipeline training history"}, {"away": "Troyes", "away_goals": 0.0, "away_xg": 1.02, "date": "2026-09-19T00:00:00+00:00", "home": "Angers", "home_goals": 2.0, "home_xg": 2.25, "source": "pipeline training history"}, {"away": "Troyes", "away_goals": 0.0, "away_xg": 0.44, "date": "2026-09-13T00:00:00+00:00", "home": "Lille", "home_goals": 2.0, "home_xg": 1.56, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 6.0, "away_xg": 2.95, "date": "2026-09-06T00:00:00+00:00", "home": "Troyes", "home_goals": 2.0, "home_xg": 2.94, "source": "pipeline training history"}, {"away": "Troyes", "away_goals": 2.0, "away_xg": 1.57, "date": "2026-08-29T00:00:00+00:00", "home": "Lorient", "home_goals": 1.0, "home_xg": 1.07, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 0.0, "away_xg": 1.8, "date": "2026-08-22T00:00:00+00:00", "home": "Troyes", "home_goals": 0.0, "home_xg": 0.41, "source": "pipeline training history"}, {"away": "Lille", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Troyes", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [{"away": "Paris SG", "away_goals": 3.0, "away_xg": null, "date": "2023-05-07T00:00:00+00:00", "home": "Troyes", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Paris SG", "away_goals": 5.0, "away_xg": 3.97, "date": "2026-10-30T00:00:00+00:00", "home": "Le Havre", "home_goals": 1.0, "home_xg": 2.01, "source": "pipeline training history"}, {"away": "Lyon", "away_goals": 0.0, "away_xg": 0.62, "date": "2026-10-26T00:00:00+00:00", "home": "Paris SG", "home_goals": 2.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Paris SG", "away_goals": 3.0, "away_xg": 2.69, "date": "2026-10-17T00:00:00+00:00", "home": "Strasbourg", "home_goals": 1.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Le Mans", "away_goals": 1.0, "away_xg": 1.43, "date": "2026-10-10T00:00:00+00:00", "home": "Paris SG", "home_goals": 3.0, "home_xg": 4.25, "source": "pipeline training history"}, {"away": "Paris SG", "away_goals": 2.0, "away_xg": 5.09, "date": "2026-09-20T00:00:00+00:00", "home": "Marseille", "home_goals": 1.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Paris SG", "away_goals": 1.0, "away_xg": 1.16, "date": "2026-09-13T00:00:00+00:00", "home": "Brest", "home_goals": 0.0, "home_xg": 1.25, "source": "pipeline training history"}, {"away": "Monaco", "away_goals": 2.0, "away_xg": 0.5, "date": "2026-09-04T00:00:00+00:00", "home": "Paris SG", "home_goals": 1.0, "home_xg": 2.32, "source": "pipeline training history"}, {"away": "Paris SG", "away_goals": 2.0, "away_xg": 1.44, "date": "2026-08-28T00:00:00+00:00", "home": "Lille", "home_goals": 2.0, "home_xg": 1.27, "source": "pipeline training history"}, {"away": "Paris SG", "away_goals": 2.0, "away_xg": 2.17, "date": "2026-08-23T00:00:00+00:00", "home": "Rennes", "home_goals": 2.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Paris SG", "away_goals": 1.0, "away_xg": null, "date": "2026-05-17T00:00:00+00:00", "home": "Paris FC", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 88.3% |
| Unadjusted draw probability | 8.6% |
| Unadjusted away-win probability | 3.2% |
| Raw p over 1 5 | 90.4% |
| Raw p under 3 5 | 45.1% |
| Raw p btts yes | 42.4% |
| P home draw | 95.9% |
| P draw away | 11.6% |
| P home away | 92.5% |
| Raw p home draw | 96.8% |
| Raw p draw away | 11.7% |
| Raw p home away | 91.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7521 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:38Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:38Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:30:22Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 17.6, "draw": 11.64, "home": 1.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:29:38Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 22.0, "draw": 11.1, "home": 1.14}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.12 |
| Reference draw odds | 11.64 |
| Reference away odds | 17.60 |
| Market reference 1x2 last update utc | 2026-11-05T12:30:22Z |
| Market reference home last update utc | 2026-11-05T12:30:22Z |
| Market reference draw last update utc | 2026-11-05T12:30:22Z |
| Market reference away last update utc | 2026-11-05T12:30:22Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.02 |
| Market reference over 2 5 last update utc | 2026-11-05T12:29:58Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:29:58Z |
| Home probability edge | -0.1% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | -0.0021 |
| Raw ev home | 0.0061 |
| Raw edge prob draw | 0.0152 |
| Raw ev draw | -0.0037 |
| Raw edge prob away | -0.0131 |
| Raw ev away | -0.2986 |
| Count model | {"corners": {"alpha": 0.015413236227799179, "mu": 9.410650896644807, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,662.7279 |
| Elo away rating | 1,413.0859 |
| Elo rating diff | 309.6419 |
| Elo home expectancy | 0.8560 |

</details>


---
