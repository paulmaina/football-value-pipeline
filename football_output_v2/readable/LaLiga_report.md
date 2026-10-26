# La Liga — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,998 |
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
| Training sha256 | 56dcfd7c8c10501f08c1085ba680ee0b381343806f4e9c1a234ff9a27fa939ba |
| Training as of utc | 2026-10-26T10:38:54.715248+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 98, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 98, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 62, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-26T10:38:54.715248+00:00', 'observations': 332, 'observations_sha256': '52efabc87e46235c26e5fe0236415abc5f8894bcd748bed7cedd6b88ca6e7660', 'eligible_training_matches': 113, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 134, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 19, 'retrospective_eligible_training_matches': 113, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '6b6b80a9a81fb5a41297f9c776dfcafacd47f2758bd8cf370f9a7645f43bb742', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-26', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1989, 'tune_start_date': '2025-10-27', 'audit_start_date': '2026-04-27', 'training_shot_matches': 1619, 'tuning_matches': 230, 'audit_matches': 126, 'audit_matchdays': 53, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8017114427406927, 'audit_candidate_poisson_score': 0.804890612238348, 'audit_gain': -0.0031791694976552876, 'audit_gain_lower95': -0.012999016820511715, 'audit_baseline_briers': [0.5696352072370781, 0.18734612086762337, 0.2015294815624924, 0.2482262774976402], 'audit_candidate_briers': [0.5729352189213638, 0.1847766252980737, 0.20545599220389799, 0.2453999021619766], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1842.283 |
| Base scoring parameter | 0.092 |
| Home-advantage parameter | 0.286 |
| Dixon-Coles low-score adjustment | -0.032 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1998, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261026T103854715248Z_84ed46fb02defcda6d9085ff4317007eee9e39b18b405c4e878125aa317ad44a.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE': 7} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 7} |
| Legacy comparison status | {'AVAILABLE': 7} |
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

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **64.8%**. Expected goals are 1.99 for Atlético Madrid and 0.81 for Deportivo La Coruña (2.80 combined). The most likely exact score is 2-0 at 12.1%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.0%; Under 3.5 goals: 69.3%; Double Chance 1X: 86.0%; Double Chance X2: 35.2%; Double Chance 12 (either team wins): 78.8%; Under 4.5 goals: 84.8%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 64.8% | 1.54 |
| Draw | 21.2% | 4.71 |
| Deportivo La Coruña win | 14.0% | 7.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 1.99 |
| Deportivo La Coruña expected goals | 0.81 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 53.0% |
| Under 2.5 | 47.0% |
| Over 3.5 | 30.7% |
| Under 3.5 | 69.3% |
| Over 4.5 | 15.2% |
| Under 4.5 | 84.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.09% |
| 2 | 1-0 | 11.83% |
| 3 | 1-1 | 10.11% |
| 4 | 2-1 | 9.74% |
| 5 | 3-0 | 8.02% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:00:00+00:00 |
| Fixture id | 70df1835c3b5ddff1c99e0189532136b |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.9906 |
| Dc lambda away | 0.8060 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:38:54.715248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.58 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.38 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.25 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.59 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.09754977027816303, "-10": 2.2484877181571567e-09, "-11": 1.627890049674588e-10, "-12": 1.082330325863073e-11, "-13": 6.652037806642935e-13, "-14": 3.8006940931135783e-14, "-15": 2.0284359197177758e-15, "-16": 1.0119628082145504e-16, "-17": 4.384009070899682e-18, "-2": 0.032787324620802326, "-3": 0.007835286932343635, "-4": 0.0014668623052674383, "-5": 0.00022485658613794962, "-6": 2.912266551985733e-05, "-7": 3.2617178482744166e-06, "-8": 3.2156606244564245e-07, "-9": 2.829980605383225e-08, "0": 0.21225812091349242, "1": 0.24557232567029091, "10": 1.8986270599332967e-05, "11": 3.3949167569390666e-06, "12": 5.574665369325964e-07, "13": 8.461913849361906e-08, "14": 1.1940753174025116e-08, "15": 1.5739285469442793e-09, "16": 1.9392919118334575e-10, "17": 2.0749373740987083e-11, "2": 0.1999934673172482, "3": 0.11803740391731163, "4": 0.054576917998633456, "5": 0.020662372468935025, "6": 0.006609378300339946, "7": 0.0018282298383873513, "8": 0.0004451532260416998, "9": 9.675595217104031e-05} |
| Raw goal margin distribution | {"-1": 0.09754977027816303, "-10": 2.2484877181571567e-09, "-11": 1.627890049674588e-10, "-12": 1.082330325863073e-11, "-13": 6.652037806642935e-13, "-14": 3.8006940931135783e-14, "-15": 2.0284359197177758e-15, "-16": 1.0119628082145504e-16, "-17": 4.384009070899682e-18, "-2": 0.032787324620802326, "-3": 0.007835286932343635, "-4": 0.0014668623052674383, "-5": 0.00022485658613794962, "-6": 2.912266551985733e-05, "-7": 3.2617178482744166e-06, "-8": 3.2156606244564245e-07, "-9": 2.829980605383225e-08, "0": 0.21225812091349242, "1": 0.24557232567029091, "10": 1.8986270599332967e-05, "11": 3.3949167569390666e-06, "12": 5.574665369325964e-07, "13": 8.461913849361906e-08, "14": 1.1940753174025116e-08, "15": 1.5739285469442793e-09, "16": 1.9392919118334575e-10, "17": 2.0749373740987083e-11, "2": 0.1999934673172482, "3": 0.11803740391731163, "4": 0.054576917998633456, "5": 0.020662372468935025, "6": 0.006609378300339946, "7": 0.0018282298383873513, "8": 0.0004451532260416998, "9": 9.675595217104031e-05} |
| Unadjusted home-win probability | 64.8% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 14.0% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 69.3% |
| Raw p btts yes | 48.1% |
| P home draw | 86.0% |
| P draw away | 35.2% |
| P home away | 78.8% |
| Raw p home draw | 86.0% |
| Raw p draw away | 35.2% |
| Raw p home away | 78.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.5297 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05775545862615334, 0.04416383629929985, 0.019204077311526246, 0.005316783882161261, 0.0011039917613996713, 0.00018338873066894864, 2.5386230006621087e-05, 3.0121527171813756e-06, 3.1272587503538934e-07, 2.8860119389420645e-08, 2.397038115153154e-09, 1.8099187160999272e-10, 1.2527218180910015e-11, 8.003650310471879e-13, 4.7482861818729255e-14, 2.629192856302298e-15, 1.364832254244607e-16, 6.668177816531445e-18], [0.11248189796557828, 0.0972303924864918, 0.039514902864707914, 0.010939978799718223, 0.0022716075605966604, 0.00037734631876930644, 5.223549127302703e-05, 6.197898503650034e-06, 6.434744234177475e-07, 5.9383473407095785e-08, 4.93221969203537e-09, 3.724144675088351e-10, 2.577639120868136e-11, 1.64685581843375e-12, 9.77022036554339e-14, 5.40990846079407e-15, 2.8083210184082417e-16, 1.3720648715920998e-17], [0.11786225850300434, 0.09789298587354434, 0.04065354255447971, 0.011255219206844384, 0.0023370649536449723, 0.000388219722578778, 5.374068043626089e-05, 6.376493735266715e-06, 6.620164281992107e-07, 6.109463488886215e-08, 5.074343819715851e-09, 3.8314575780714735e-10, 2.6519149509006145e-11, 1.6943107091776437e-12, 1.00517536575298e-13, 5.565797405088908e-15, 2.889244051020221e-16, 1.4116015376718675e-17], [0.08083900831076815, 0.06714254417919237, 0.027883328439188025, 0.007719695605344418, 0.0016029390206000092, 0.0002662709656047357, 3.685949486792238e-05, 4.373490179179347e-06, 4.5406181945594467e-07, 4.190340283864644e-08, 3.480375545351087e-09, 2.6279085003973537e-10, 1.8188873815772034e-11, 1.1620886892876203e-12, 6.894266305257785e-14, 3.817452239595129e-15, 1.9816659447969725e-16, 9.681849803721556e-18], [0.04158421033800565, 0.0345386433866539, 0.01434339954148643, 0.003971071052281316, 0.0008245642145358742, 0.0001369718415897027, 1.8960808891270763e-05, 2.249757132386423e-06, 2.3357290745238397e-07, 2.1555434114452693e-08, 1.7903320656378236e-09, 1.3518164325996562e-10, 9.356497195744984e-12, 5.977873986402754e-13, 3.546463844063212e-14, 1.963726920997729e-15, 1.0193842699221127e-16, 4.9804183291212636e-18], [0.017112991221146907, 0.014213555969005295, 0.005902684418910908, 0.0016341996999311046, 0.0003393297612225634, 5.636749871204417e-05, 7.802869249283487e-06, 9.258339582092431e-07, 9.612136631285868e-08, 8.870625455438925e-09, 7.367685155775705e-10, 5.5630785232290934e-11, 3.850443547442597e-12, 2.460051645057618e-13, 1.4594627176099295e-14, 8.08125038003924e-16, 4.1950331436758984e-17, 2.049572528878732e-18], [0.005868703252081044, 0.004874375324628188, 0.0020242576413212767, 0.0005604299663102835, 0.000116369233612058, 1.933058450905214e-05, 2.6759041448140337e-06, 3.1750409330634265e-07, 3.296371556467968e-08, 3.0420788385607745e-09, 2.526662771881692e-10, 1.907793710576609e-11, 1.3204652697365426e-12, 8.436463797045868e-14, 5.005059306373207e-15, 2.771371747541804e-16, 1.4386383031889693e-17, 7.028772942244545e-19], [0.001725089307010201, 0.001432809325959483, 0.0005950250100716462, 0.00016473685935085113, 3.4206418683368985e-05, 5.682172569042068e-06, 7.865747216245889e-07, 9.332946185352244e-08, 9.689594242099424e-09, 8.942107736700288e-10, 7.427056272862766e-11, 5.607907554245468e-12, 3.881471628835722e-13, 2.4798755125507116e-14, 1.471223525795862e-15, 8.146371629438319e-17, 4.2288380360798625e-18, 2.0660886269499272e-19], [0.00044369963272422337, 0.00036852409269980206, 0.00015304273080683786, 4.237095650241745e-05, 8.798023003763295e-06, 1.4614767315027559e-06, 2.0231005645722463e-07, 2.4004698063155086e-08, 2.49220106402343e-09, 2.2999446477531798e-10, 1.9102675595402447e-11, 1.4423754828568987e-12, 9.983294946791523e-14, 6.3783356006509596e-15, 3.784043732681955e-16, 2.0952782475252113e-17, 1.0876734762855763e-18, 5.3140597488380155e-20], [0.00010144111935646764, 8.42540622442432e-05, 3.498949464324996e-05, 9.687087702596542e-06, 2.0114537759385797e-06, 3.341310756712228e-07, 4.625326926255673e-08, 5.488089828674637e-09, 5.697811017865969e-10, 5.2582635260149023e-11, 4.367361728932323e-12, 3.2976404017956557e-13, 2.28243735080516e-14, 1.4582511574071828e-15, 8.651294786526588e-17, 4.790343626998713e-18, 2.486700614361937e-19, 1.2149303932021214e-20], [2.0872838162613502e-05, 1.733637618475991e-05, 7.199546532149186e-06, 1.9932450979056496e-06, 4.138829441462288e-07, 6.875184256472558e-08, 9.517215601856213e-09, 1.1292463208461962e-09, 1.1723992007535926e-10, 1.0819565506685706e-11, 8.986418440953862e-13, 6.785326784821994e-14, 4.696413618253606e-15, 3.000542640114638e-16, 1.780117146989252e-17, 9.856759064170965e-19, 5.116712020896975e-20, 2.4998783172961342e-21], [3.904417886826968e-06, 3.242896665091679e-06, 1.3467281276350719e-06, 3.728511548100147e-07, 7.741984858923497e-08, 1.286053778459494e-08, 1.7802651723345397e-09, 2.112338293142486e-10, 2.193058928671736e-11, 2.023879300116719e-12, 1.6809756596598238e-13, 1.2692452775338313e-14, 8.784987068932067e-16, 5.612735682124274e-17, 3.329840041495331e-18, 1.8437792741202493e-19, 9.571186141765821e-21, 4.676206245121292e-22], [6.694875739078773e-07, 5.560570317206903e-07, 2.3092245067461944e-07, 6.393250474153703e-08, 1.3275122721672728e-08, 2.205186660374661e-09, 3.052607189307654e-10, 3.622010451084028e-11, 3.760421512633328e-12, 3.470330486623864e-13, 2.8823562149450916e-14, 2.1763652513146402e-15, 1.5063550700949984e-16, 9.62411530663619e-18, 5.709651465339703e-19, 3.1615143379428355e-20, 1.641164028853213e-21, 8.01825538373234e-23], [1.0596602450996829e-07, 8.801231770190079e-08, 3.655024383089711e-08, 1.0119192093261442e-08, 2.1011771308711033e-09, 3.490354008190607e-10, 4.831645288848792e-11, 5.732892785366982e-12, 5.951968844612886e-13, 5.4928147994853716e-14, 4.562173238503736e-15, 3.4447356837004465e-16, 2.3842482594063197e-17, 1.5232982331799063e-18, 9.03719636778227e-20, 5.0040227612822736e-21, 2.5976229355717345e-22, 1.2691238487970525e-23], [1.5574211877530662e-08, 1.293549031456777e-08, 5.371922219694586e-09, 1.4872544517800734e-09, 3.088176420672473e-10, 5.129900182868074e-11, 7.101244742698185e-12, 8.425840954529079e-13, 8.747825003639953e-14, 8.072989610285314e-15, 6.7051918732474e-16, 5.062853272842599e-17, 3.504216349754124e-18, 2.2388467950857425e-19, 1.3282296062494205e-20, 7.354594180974008e-22, 3.817820868869311e-23, 1.8652774614690884e-24], [2.1363986392120095e-09, 1.774430971075525e-09, 7.368955431167483e-10, 2.0401471431944673e-10, 4.236218150011037e-11, 7.036960750344213e-12, 9.741160403050365e-13, 1.155818046590416e-13, 1.1999863351547237e-14, 1.1074155246769904e-15, 9.197873321813594e-17, 6.9449888878396e-18, 4.80692255890009e-19, 3.0711468959312233e-20, 1.822004185936553e-21, 1.0088693491359303e-22, 5.237110791317182e-24, 2.5587016933965215e-25], [2.747449908010164e-10, 2.2819524964919442e-10, 9.476618993241628e-11, 2.6236686253293364e-11, 5.447858350467621e-12, 9.049667422244471e-13, 1.2527320398942208e-13, 1.4864043289938613e-14, 1.543205601062511e-15, 1.4241577510670236e-16, 1.1828642720548988e-17, 8.931389830909259e-19, 6.181795241703219e-20, 3.949554217945089e-21, 2.343132569533878e-22, 1.2974254662042587e-23, 6.735025616357145e-25, 3.2905397911789707e-26], [3.325434014366745e-11, 2.7620093923748245e-11, 1.147022591729198e-11, 3.1756127249708306e-12, 6.593930397521888e-13, 1.0953456067351547e-13, 1.516270678568407e-14, 1.799100868163991e-15, 1.8678514872910893e-16, 1.7237594081023033e-17, 1.4317047503586253e-18, 1.0810296286997864e-19, 7.482266412456218e-21, 4.780426350867489e-22, 2.836059985727567e-23, 1.5703663108988382e-24, 8.151880479046224e-26, 3.982774322949845e-27]] |
| Legacy trial inputs | {"lambda_home": 2.057630899089911, "lambda_away": 0.8305711015290702, "rho": -0.021851862651747548, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6565 |
| Legacy p draw | 0.2042 |
| Legacy p away | 0.1393 |
| Legacy p over 1 5 | 0.7856 |
| Legacy p under 3 5 | 0.6723 |
| Legacy p btts yes | 0.4942 |
| Legacy p over 2 5 | 0.5513 |
| Legacy goal margin distribution | {"-1": 0.09668199953040926, "-10": 2.7971701082167533e-09, "-11": 2.0853352257103404e-10, "-12": 1.4278512976158179e-11, "-13": 9.038361791205196e-13, "-14": 5.3191376534429064e-14, "-15": 2.924140973519841e-15, "-16": 1.502038741403817e-16, "-17": 6.668177816531445e-18, "-2": 0.03276731255070719, "-3": 0.008015819656518226, "-4": 0.0015396949526928197, "-5": 0.00024247708917187846, "-6": 3.228989564980713e-05, "-7": 3.720341268977209e-06, "-8": 3.7745609070222377e-07, "-9": 3.41942863765239e-08, "0": 0.20424279276501905, "1": 0.24258875483651424, "10": 2.4357092452148182e-05, "11": 4.498555699141284e-06, "12": 7.630813859367032e-07, "13": 1.1966530644694586e-07, "14": 1.7446584651263573e-08, "15": 2.376064114778496e-09, "16": 3.0236508472476463e-10, "17": 3.325434014366745e-11, "2": 0.20110466124723464, "3": 0.12187648138285594, "4": 0.05799590269402797, "5": 0.022626844535056305, "6": 0.007464669451114102, "7": 0.0021306758136575886, "8": 0.0005355397240319352, "9": 0.00012019030963890372} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.6565 |
| Legacy raw p draw | 0.2042 |
| Legacy raw p away | 0.1393 |
| Legacy market weight | 0 |
| Legacy lambda home | 2.0576 |
| Legacy lambda away | 0.8306 |
| Legacy model home team | Ath Madrid |
| Legacy model away team | La Coruna |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 10.666991839562744, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,650.0417 |
| Elo away rating | 1,441.7911 |
| Elo rating diff | 268.2506 |
| Elo home expectancy | 0.8241 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **44.4%**. Expected goals are 1.24 for Valencia and 1.57 for Villarreal (2.81 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.3%; Under 3.5 goals: 69.0%; Double Chance 1X: 55.6%; Double Chance X2: 70.1%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 84.6%; BTTS Yes (both teams score): 56.7%; BTTS No (at least one team does not score): 43.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 29.9% | 3.34 |
| Draw | 25.6% | 3.90 |
| Villarreal win | 44.4% | 2.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.24 |
| Villarreal expected goals | 1.57 |
| Expected total goals | 2.81 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 53.3% |
| Under 2.5 | 46.7% |
| Over 3.5 | 31.0% |
| Under 3.5 | 69.0% |
| Over 4.5 | 15.4% |
| Under 4.5 | 84.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.11% |
| 2 | 1-2 | 9.18% |
| 3 | 0-1 | 9.05% |
| 4 | 0-2 | 7.38% |
| 5 | 2-1 | 7.30% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0dae715cc56fe201f9e667917c126691 |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2444 |
| Dc lambda away | 1.5658 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:38:54.715248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.63 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.43 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.22 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.50 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.2174471259076103, "-10": 1.751955992628547e-06, "-11": 2.45799749093563e-07, "-12": 3.168095887353433e-08, "-13": 3.77461259511139e-09, "-14": 4.154299173414124e-10, "-15": 3.8379907776673e-11, "-2": 0.13503174673253468, "-3": 0.06135260998454145, "-4": 0.02199875061016832, "-5": 0.0064859778572650875, "-6": 0.0016199400200582145, "-7": 0.0003504787231145771, "-8": 6.682686986670186e-05, "-9": 1.138419363292057e-05, "0": 0.2561847009952882, "1": 0.17203792760812991, "10": 1.7612198816005307e-07, "11": 1.9638162995087125e-08, "12": 2.011623875123108e-09, "13": 1.9048022135720483e-10, "14": 1.6661124521539282e-11, "15": 1.2233183956520923e-12, "2": 0.08528918469782674, "3": 0.03079783292077784, "4": 0.008776354776926742, "5": 0.002056461839116798, "6": 0.0004082001561420436, "7": 7.01883330901192e-05, "8": 1.0636124900720694e-05, "9": 1.4400037458437438e-06} |
| Raw goal margin distribution | {"-1": 0.2174471259076103, "-10": 1.751955992628547e-06, "-11": 2.45799749093563e-07, "-12": 3.168095887353433e-08, "-13": 3.77461259511139e-09, "-14": 4.154299173414124e-10, "-15": 3.8379907776673e-11, "-2": 0.13503174673253468, "-3": 0.06135260998454145, "-4": 0.02199875061016832, "-5": 0.0064859778572650875, "-6": 0.0016199400200582145, "-7": 0.0003504787231145771, "-8": 6.682686986670186e-05, "-9": 1.138419363292057e-05, "0": 0.2561847009952882, "1": 0.17203792760812991, "10": 1.7612198816005307e-07, "11": 1.9638162995087125e-08, "12": 2.011623875123108e-09, "13": 1.9048022135720483e-10, "14": 1.6661124521539282e-11, "15": 1.2233183956520923e-12, "2": 0.08528918469782674, "3": 0.03079783292077784, "4": 0.008776354776926742, "5": 0.002056461839116798, "6": 0.0004082001561420436, "7": 7.01883330901192e-05, "8": 1.0636124900720694e-05, "9": 1.4400037458437438e-06} |
| Unadjusted home-win probability | 29.9% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 44.4% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 69.0% |
| Raw p btts yes | 56.7% |
| P home draw | 55.6% |
| P draw away | 70.1% |
| P home away | 74.4% |
| Raw p home draw | 55.6% |
| Raw p draw away | 70.1% |
| Raw p home away | 74.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.5330 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0644472878028467, 0.09094596463283311, 0.0707383566009275, 0.0356620482164245, 0.013484003701471816, 0.004078696876138873, 0.001028117499800224, 0.00022213514872765033, 4.199522065436392e-05, 7.057159443139979e-06, 1.0673393011604944e-06, 1.467514454299914e-07, 1.8495825229157755e-08, 2.1518050987830886e-09, 2.3245959034058588e-10, 2.3438444197578586e-11], [0.07599074222266279, 0.12145539887822099, 0.08988173758994186, 0.045312995858692216, 0.017133076602200897, 0.005182483449512636, 0.0013063490837085577, 0.0002822498868623644, 5.336006636656516e-05, 8.966984584857756e-06, 1.3561851815070525e-06, 1.8646566789070997e-07, 2.350120909841417e-08, 2.7341316723632303e-09, 2.953683532278154e-10, 2.9781411275472457e-11], [0.04992784370679504, 0.07551189715893762, 0.05710287275801118, 0.028787852862923975, 0.01088483511113405, 0.0032924896750230973, 0.0008299381777072131, 0.00017931650864377855, 3.390024672186551e-05, 5.696825556579802e-06, 8.615996078002348e-07, 1.1846372347492653e-07, 1.493058088094119e-08, 1.7370244187188154e-09, 1.8765081698864115e-10, 1.892046353593867e-11], [0.021146478196181998, 0.031982368319393106, 0.02418539564432056, 0.01219282984572127, 0.004610171624842395, 0.0013945036667897311, 0.00035151266860491433, 7.594785511906807e-05, 1.4358137162081269e-05, 2.4128379772842427e-06, 3.6492257561099047e-07, 5.0174218622626636e-08, 6.3237099705186116e-09, 7.357006886254538e-10, 7.947777463111196e-11, 8.013588008607131e-12], [0.006717297006571026, 0.01015937807618953, 0.007682626121339804, 0.0038731205576860986, 0.001464446787216028, 0.00044297188494821075, 0.00011165996411723549, 2.4125260722559285e-05, 4.560942530666804e-06, 7.664514711049449e-07, 1.1591969603829714e-07, 1.5938121016371508e-08, 2.0087618212973863e-09, 2.3369943626491285e-10, 2.5246559387599895e-11, 2.545561026413803e-12], [0.001707029554742024, 0.002581746588976037, 0.0019523433062928778, 0.0009842547165298061, 0.00037215176650360173, 0.0001125699963522052, 2.8375529419511823e-05, 6.130819141833366e-06, 1.1590471122107577e-06, 1.9477407537165286e-07, 2.945803154461022e-08, 4.050266587198204e-09, 5.104755371152573e-10, 5.938874583638496e-11, 6.415768572987695e-12, 6.468893516599127e-13], [0.0003614983201715728, 0.0005467374905319496, 0.0004134485098178336, 0.00020843600842062983, 7.881072595738784e-05, 2.383899240056927e-05, 6.009097025085059e-06, 1.2983259808781825e-06, 2.4545186279872115e-07, 4.124738254485856e-08, 6.238338925858341e-09, 8.577265481150226e-10, 1.0810360526167634e-10, 1.2576778062986823e-11, 1.358669833982532e-12, 1.3699201241848265e-13], [6.561826408947552e-05, 9.924241148427823e-05, 7.504813159781903e-05, 3.7834778982678564e-05, 1.430552437007375e-05, 4.3271938254792595e-06, 1.0907561488644509e-06, 2.356688602233547e-07, 4.455380358817705e-08, 7.48712093473509e-09, 1.1323675609954262e-09, 1.5569236151374977e-10, 1.9622694002335535e-11, 2.2829050600846698e-12, 2.466223243702929e-13, 2.4866444869669928e-14], [1.0422004195105246e-05, 1.5762453383575575e-05, 1.191972925831681e-05, 6.009214519004622e-06, 2.2721148915916205e-06, 6.872786537096403e-07, 1.7324239397435445e-07, 3.743076541242143e-08, 7.076382381446628e-09, 1.1891629087393788e-09, 1.7985144280871447e-10, 2.4728274472935885e-11, 3.116629219766398e-12, 3.6258877681961547e-13, 3.917047997016502e-14, 3.949482607398321e-15], [1.4713812848702187e-06, 2.225347301541567e-06, 1.682830501991581e-06, 8.483824813836109e-07, 3.207777761337847e-07, 9.703018053227261e-08, 2.4458406604719668e-08, 5.284485275113459e-09, 9.990455200100567e-10, 1.6788633124929234e-10, 2.5391473852019166e-11, 3.4911442737376865e-12, 4.400065304135718e-13, 5.119037858063145e-14, 5.530098632521472e-15, 5.575889900500695e-16], [1.8695699602911364e-07, 2.827576039574285e-07, 2.138242063519666e-07, 1.0779737504762094e-07, 4.0758741487024974e-08, 1.2328871695602903e-08, 3.1077398316102333e-09, 6.714585150391112e-10, 1.2694095761446262e-10, 2.133201263837259e-11, 3.2262974423682465e-12, 4.4359259753654513e-13, 5.590821359846918e-14, 6.504363962922149e-15, 7.026666974169899e-16, 7.084850383146144e-17], [2.159561267895353e-08, 3.2661648543725337e-08, 2.469907433173897e-08, 1.2451795914466844e-08, 4.708088026287693e-09, 1.4241218224606686e-09, 3.589785198514833e-10, 7.756092753283144e-11, 1.4663092646773677e-11, 2.4640847488215823e-12, 3.726732426832167e-13, 5.1239879368613535e-14, 6.4580205720503046e-15, 7.513263897561561e-16, 8.116581974527295e-17, 8.183790283993097e-18], [2.2866556952194808e-09, 3.458385078861569e-09, 2.615266342610522e-09, 1.3184608590093498e-09, 4.985168264939953e-10, 1.507934192202708e-10, 3.801051116645748e-11, 8.212554063923352e-12, 1.5526044483541216e-12, 2.60910098183395e-13, 3.946057958651921e-14, 5.425544703104807e-15, 6.838087782207338e-16, 7.955434252527339e-17, 8.594258784728298e-18, 8.665422435369165e-19], [2.2349814272480926e-10, 3.3802318537446633e-10, 2.5561660705025965e-10, 1.2886660368677084e-10, 4.872512511236619e-11, 1.4738576166631522e-11, 3.7151542610827836e-12, 8.026965249518147e-13, 1.5175184061110546e-13, 2.5501400356882036e-14, 3.856884211676237e-15, 5.302937241270867e-16, 6.683559410835826e-17, 7.775655879135449e-18, 8.400044136503841e-19, 8.469599617816578e-20], [2.028440982224107e-11, 3.067855838962158e-11, 2.3199441174607405e-11, 1.169577057649803e-11, 4.422230960711664e-12, 1.3376546020267325e-12, 3.3718271957829167e-13, 7.285172519334752e-14, 1.3772805843962728e-14, 2.3144749641922615e-15, 3.500459513120043e-16, 4.812879022265912e-17, 6.065914307288822e-18, 7.0570873013162405e-19, 7.62377421630551e-20, 7.686901894734052e-21], [1.7182549783140807e-12, 2.5987241503407253e-12, 1.9651819126956357e-12, 9.907271739428306e-13, 3.7459903591407397e-13, 1.1331025646489515e-13, 2.85621268547645e-14, 6.17113539852592e-15, 1.1666690041331277e-15, 1.9605490937410396e-16, 2.9651747512074673e-17, 4.0769011336796916e-18, 5.138324234160091e-19, 5.977928613228943e-20, 6.457958656675475e-21, 6.511432949829579e-22]] |
| Legacy trial inputs | {"lambda_home": 1.270622359761795, "lambda_away": 1.5124205564010904, "rho": -0.021851862651747548, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3168 |
| Legacy p draw | 0.2568 |
| Legacy p away | 0.4265 |
| Legacy p over 1 5 | 0.7686 |
| Legacy p under 3 5 | 0.6957 |
| Legacy p btts yes | 0.5634 |
| Legacy p over 2 5 | 0.5265 |
| Legacy goal margin distribution | {"-1": 0.21469841821969807, "-10": 1.2694971440695102e-06, "-11": 1.720717022827819e-07, "-12": 2.1425621306518236e-08, "-13": 2.4660939155468428e-09, "-14": 2.6224100161605834e-10, "-15": 2.3438444197578586e-11, "-2": 0.12844873514318556, "-3": 0.05646445387501316, "-4": 0.01957713529761659, "-5": 0.005579517392873372, "-6": 0.001346800551750602, "-7": 0.0002815734246503096, "-8": 5.1876048599747954e-05, "-9": 8.538372310289327e-06, "0": 0.2567816580818006, "1": 0.1799582755501812, "10": 2.2236731306035342e-07, "11": 2.532168473447777e-08, "12": 2.6488690489424974e-09, "13": 2.561418830271265e-10, "14": 2.2883133972581796e-11, "15": 1.7182549783140807e-12, "2": 0.09066040944016489, "3": 0.033481653534901845, "4": 0.009752699216298918, "5": 0.0023351578653837968, "6": 0.0004735510650860375, "7": 8.317620802070845e-05, "8": 1.2874141097669763e-05, "9": 1.7802065153602367e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3168 |
| Legacy raw p draw | 0.2568 |
| Legacy raw p away | 0.4265 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.2706 |
| Legacy lambda away | 1.5124 |
| Legacy model home team | Valencia |
| Legacy model away team | Villarreal |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 9.873997057540466, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,456.5878 |
| Elo away rating | 1,556.2139 |
| Elo rating diff | -39.6261 |
| Elo home expectancy | 0.4432 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **51.2%**. Expected goals are 1.24 for Athletic Bilbao and 0.61 for Getafe (1.85 combined). The most likely exact score is 1-0 at 19.1%. Goal-market probabilities: at least one goal: 83.9%; Over 2.5 goals: 28.3%; Under 3.5 goals: 88.3%; Double Chance 1X: 82.1%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 69.2%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 32.9%; BTTS No (at least one team does not score): 67.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 51.2% | 1.95 |
| Draw | 30.8% | 3.24 |
| Getafe win | 17.9% | 5.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.24 |
| Getafe expected goals | 0.61 |
| Expected total goals | 1.85 |
| Over 0.5 | 83.9% |
| Under 0.5 | 16.1% |
| Over 1.5 | 55.6% |
| Under 1.5 | 44.4% |
| Over 2.5 | 28.3% |
| Under 2.5 | 71.7% |
| Over 3.5 | 11.7% |
| Under 3.5 | 88.3% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.10% |
| 2 | 0-0 | 16.11% |
| 3 | 1-1 | 12.29% |
| 4 | 2-0 | 12.07% |
| 5 | 0-1 | 9.22% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T13:00:00+00:00 |
| Fixture id | 9c4254cba9944a839b421db27260504d |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2394 |
| Dc lambda away | 0.6108 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:38:54.715248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 32.9% |
| P btts no | 67.1% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.21 |
| Fair Over 1.5 odds | 1.80 |
| Fair Under 1.5 odds | 2.25 |
| Fair Over 2.5 odds | 3.54 |
| Fair Under 2.5 odds | 1.39 |
| Fair Over 3.5 odds | 8.55 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.91 |
| Fair Under 4.5 odds | 1.04 |
| Goal margin distribution | {"-1": 0.13340689330575467, "-10": 3.3529402353562353e-10, "-11": 1.8511970184123253e-11, "-12": 9.376876063744705e-13, "-13": 4.381775621282618e-14, "-14": 1.8136062832787944e-15, "-2": 0.03746041819506334, "-3": 0.0071894205101252035, "-4": 0.0010587019666107556, "-5": 0.0001261998895263295, "-6": 1.2622416368098535e-05, "-7": 1.0868361004481238e-06, "-8": 8.212217815794172e-08, "-9": 5.527085754453303e-09, "0": 0.3084129250275592, "1": 0.2746626365628854, "10": 3.9685166600172294e-07, "11": 4.44605956856406e-08, "12": 4.569840585686303e-09, "13": 4.333245042542553e-10, "14": 3.6393712952683583e-11, "2": 0.15424571231723558, "3": 0.06006958131509196, "4": 0.01794959599310775, "5": 0.004341703607951823, "6": 0.0008811785952726002, "7": 0.00015395923070108506, "8": 2.360599855268888e-05, "9": 3.223876219468268e-06} |
| Raw goal margin distribution | {"-1": 0.13340689330575467, "-10": 3.3529402353562353e-10, "-11": 1.8511970184123253e-11, "-12": 9.376876063744705e-13, "-13": 4.381775621282618e-14, "-14": 1.8136062832787944e-15, "-2": 0.03746041819506334, "-3": 0.0071894205101252035, "-4": 0.0010587019666107556, "-5": 0.0001261998895263295, "-6": 1.2622416368098535e-05, "-7": 1.0868361004481238e-06, "-8": 8.212217815794172e-08, "-9": 5.527085754453303e-09, "0": 0.3084129250275592, "1": 0.2746626365628854, "10": 3.9685166600172294e-07, "11": 4.44605956856406e-08, "12": 4.569840585686303e-09, "13": 4.333245042542553e-10, "14": 3.6393712952683583e-11, "2": 0.15424571231723558, "3": 0.06006958131509196, "4": 0.01794959599310775, "5": 0.004341703607951823, "6": 0.0008811785952726002, "7": 0.00015395923070108506, "8": 2.360599855268888e-05, "9": 3.223876219468268e-06} |
| Unadjusted home-win probability | 51.2% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 17.9% |
| Raw p over 1 5 | 55.6% |
| Raw p under 3 5 | 88.3% |
| Raw p btts yes | 32.9% |
| P home draw | 82.1% |
| P draw away | 48.8% |
| P home away | 69.2% |
| Raw p home draw | 82.1% |
| Raw p draw away | 48.8% |
| Raw p home away | 69.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.2829 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.1493351738182912, 0.08936387064461813, 0.02881604820723804, 0.006019688045768935, 0.0009431370648336717, 0.00011821310556958617, 1.2347390824251123e-05, 1.1054471215875952e-06, 8.659818795059981e-08, 6.0301360899368545e-09, 3.7790960655564445e-10, 2.1530596656075463e-11, 1.124438319723309e-12, 5.420671679008314e-14, 2.4265312364057898e-15], [0.1870478282093517, 0.1214479021782475, 0.0372419917246778, 0.007779872200843887, 0.0012189146308739848, 0.00015277915513290852, 1.59578240427367e-05, 1.428684886218827e-06, 1.119198918545066e-07, 7.793375300631975e-09, 4.884120938028695e-10, 2.782624101425297e-11, 1.4532291970391539e-12, 7.005700724817478e-14, 3.1360600029534123e-15], [0.12254899096290321, 0.07680165135222838, 0.024065859718970586, 0.005027371103059547, 0.0007876654055689585, 9.872623737723125e-05, 1.0311982175164936e-05, 9.232194214675347e-07, 7.232288855668655e-08, 5.036096836840755e-09, 3.156130053785477e-10, 1.798138020398992e-11, 9.390800109190219e-13, 4.527099735238628e-14, 2.026529103472762e-15], [0.052794291043253644, 0.03308626780386494, 0.010367608841382076, 0.0021657990907302783, 0.00033932745051240754, 4.2531412692550614e-05, 4.442417550000887e-06, 3.977243260084905e-07, 3.115681000348934e-08, 2.169558150068028e-09, 1.3596656106319915e-10, 7.746405844632454e-12, 4.0455709198265383e-13, 1.9502814272569066e-14, 8.730318092031582e-16], [0.017057895447728493, 0.010690210736829159, 0.003349786201586656, 0.0006997721480944755, 0.00010963708497653105, 1.3741947786728148e-05, 1.435350160133511e-06, 1.2850518182946707e-07, 1.0066800728299139e-08, 7.009867044394525e-10, 4.3930950433694986e-11, 2.5028725337964104e-12, 1.307128562825738e-13, 6.30138146045739e-15, 2.8207756993512495e-16], [0.004409140327195568, 0.0027632153925676193, 0.0008658557835671212, 0.00018087774118831794, 2.8339093424949025e-05, 3.5520311603708073e-06, 3.710106146496538e-07, 3.321613625749788e-08, 2.60207580665504e-09, 1.8119168081684358e-10, 1.1355312017405282e-11, 6.469447685623752e-13, 3.378677795772056e-14, 1.6287868101598068e-15, 7.29116667885256e-17], [0.0009497321677457675, 0.0005951986895370397, 0.00018650599193005397, 3.8961202521989835e-05, 6.1042621992359325e-06, 7.651102036902463e-07, 7.991596754917169e-08, 7.154780921213577e-09, 5.604891006191133e-10, 3.9028825355879233e-11, 2.4459428136594063e-12, 1.3935239340620684e-13, 7.27769757587658e-15, 3.508419132109364e-16, 1.570522827906177e-17], [0.00017534831026634037, 0.00010989107037490376, 3.4434455997321794e-05, 7.1933764699063936e-06, 1.1270251744755497e-06, 1.4126170086778984e-07, 1.4754822832112498e-08, 1.3209816277345334e-09, 1.0348266601260474e-10, 7.205861621047554e-12, 4.515925162367298e-13, 2.5728523835669124e-14, 1.3436756339298867e-15, 6.47756691217137e-17, 2.8996440624066657e-18], [2.8327619183374805e-05, 1.7752964876053745e-05, 5.562905937315177e-06, 1.1620940570949602e-06, 1.820715574853668e-07, 2.2820908061791e-08, 2.3836500144847954e-09, 2.1340533274520863e-10, 1.6717683509084497e-11, 1.1641110403577953e-12, 7.295502766228666e-14, 4.156457648552097e-15, 2.170715623442886e-16, 1.0464546162099112e-17, 4.684391463050066e-19], [4.067860425937088e-06, 2.5493347250563624e-06, 7.988361029964592e-07, 1.6687729369249747e-07, 2.6145567638036033e-08, 3.277093926869456e-09, 3.4229334630768257e-10, 3.064511359527352e-11, 2.4006677977320966e-12, 1.6716693350802705e-13, 1.0476378829419356e-14, 5.968694181878748e-16, 3.1171586017892415e-17, 1.502714115599864e-18, 6.726809806636468e-20], [5.257321310346803e-07, 3.294771790051875e-07, 1.0324194116837749e-07, 2.1567297313070037e-08, 3.3790650494822652e-09, 4.2353310914717527e-10, 4.4238147711735884e-11, 3.960588414862238e-12, 3.1026339772148983e-13, 2.1604730494523353e-14, 1.3539719633444543e-15, 7.713967499291829e-17, 4.028629950139511e-18, 1.942114555585368e-19, 8.693759579750809e-21], [6.176896332393767e-08, 3.8710709474790255e-08, 1.2130032199042e-08, 2.533970282747668e-09, 3.9701082127107276e-10, 4.97614650904025e-11, 5.197598476903625e-12, 4.653347704987429e-13, 3.6453256902714933e-14, 2.5383683567397165e-15, 1.5907995651866775e-16, 9.063242427432546e-18, 4.733290604592496e-19, 2.281816074637536e-20, 1.0214413099916382e-21], [6.65254075439751e-09, 4.169158078016247e-09, 1.306409063935327e-09, 2.7290955957938543e-10, 4.275821587925381e-11, 5.359328644975685e-12, 5.597833253451395e-13, 5.01167310991833e-14, 3.926029580649502e-15, 2.7338323381476994e-16, 1.713297159284034e-17, 9.761146435189357e-19, 5.097771915698563e-20, 2.4575245582408565e-21, 1.1000961611267937e-22], [6.613672245345008e-10, 4.144799120366936e-10, 1.2987761648066332e-10, 2.713150428257656e-11, 4.250839432049477e-12, 5.32801592978264e-13, 5.5651270378085457e-14, 4.9823916265223404e-15, 3.9030911392434885e-16, 2.7178594954540154e-17, 1.7032869528676007e-18, 9.704115411617175e-20, 5.067987386573817e-21, 2.4431660869341476e-22, 1.0936686773764515e-23], [6.10538577222897e-11, 3.826255163467864e-11, 1.1989601576494323e-11, 2.5046342497937182e-12, 3.9241458641576353e-13, 4.918537152305966e-14, 5.137425348103351e-15, 4.5994754230001e-16, 3.6031233821758655e-17, 2.5089814068336455e-18, 1.5723827160289828e-19, 8.958316343519481e-21, 4.67849281548568e-22, 2.2553992567229102e-23, 1.009615979546978e-24]] |
| Legacy trial inputs | {"lambda_home": 1.2924045468289895, "lambda_away": 0.6267016215211189, "rho": -0.021851862651747548, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5249 |
| Legacy p draw | 0.2971 |
| Legacy p away | 0.1780 |
| Legacy p over 1 5 | 0.5743 |
| Legacy p under 3 5 | 0.8714 |
| Legacy p btts yes | 0.3404 |
| Legacy p over 2 5 | 0.3014 |
| Legacy goal margin distribution | {"-1": 0.13198668114070752, "-10": 4.0669471247265896e-10, "-11": 2.3029969882276207e-11, "-12": 1.1965218560749567e-12, "-13": 5.734277679303656e-14, "-14": 2.4265312364057898e-15, "-2": 0.037427586360408355, "-3": 0.007341902478312393, "-4": 0.0011066361769320526, "-5": 0.00013512601832651693, "-6": 1.385061274241485e-05, "-7": 1.2225416138530592e-06, "-8": 9.471505501980327e-08, "-9": 6.536940495328824e-09, "0": 0.2971280051762118, "1": 0.27494597972533596, "10": 5.65776773492275e-07, "11": 6.607050365268437e-08, "12": 7.079010268010697e-09, "13": 6.996297761691795e-10, "14": 6.10538577222897e-11, "2": 0.15917217064805117, "3": 0.06439046895854512, "4": 0.020014995602054924, "5": 0.005039962141135879, "6": 0.0010653564507429952, "7": 0.00019392208096896476, "8": 3.098277311603719e-05, "9": 4.4097448467256994e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.5249 |
| Legacy raw p draw | 0.2971 |
| Legacy raw p away | 0.1780 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.2924 |
| Legacy lambda away | 0.6267 |
| Legacy model home team | Ath Bilbao |
| Legacy model away team | Getafe |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 9.81489003483115, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,505.1233 |
| Elo away rating | 1,442.8223 |
| Elo rating diff | 122.3011 |
| Elo home expectancy | 0.6691 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **52.2%**. Expected goals are 2.02 for Barcelona and 1.37 for Real Madrid (3.39 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.9%; Under 3.5 goals: 56.0%; Double Chance 1X: 74.3%; Double Chance X2: 47.8%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 74.5%; BTTS Yes (both teams score): 65.1%; BTTS No (at least one team does not score): 34.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 52.2% | 1.92 |
| Draw | 22.1% | 4.52 |
| Real Madrid win | 25.7% | 3.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 2.02 |
| Real Madrid expected goals | 1.37 |
| Expected total goals | 3.39 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 65.9% |
| Under 2.5 | 34.1% |
| Over 3.5 | 44.0% |
| Under 3.5 | 56.0% |
| Over 4.5 | 25.5% |
| Under 4.5 | 74.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.62% |
| 2 | 2-1 | 9.41% |
| 3 | 2-0 | 6.86% |
| 4 | 1-0 | 6.49% |
| 5 | 2-2 | 6.46% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T20:00:00+00:00 |
| Fixture id | 72089d103a5fe6a922c35e17efba6ffc |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0202 |
| Dc lambda away | 1.3728 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:38:54.715248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 65.1% |
| P btts no | 34.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.31 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.91 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.93 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.93 |
| Fair Under 4.5 odds | 1.34 |
| Goal margin distribution | {"-1": 0.1445508692306922, "-10": 2.8257340531008774e-07, "-11": 3.455172083274906e-08, "-12": 3.884678935763073e-09, "-13": 4.041426245795382e-10, "-14": 3.911721828738414e-11, "-15": 3.537373069751624e-12, "-16": 2.9728694545408707e-13, "-17": 2.0639730161084055e-14, "-2": 0.07320517411881834, "-3": 0.0278006407079291, "-4": 0.008461710645597921, "-5": 0.0021373751280092616, "-6": 0.00046003863472219854, "-7": 8.610943079558253e-05, "-8": 1.4243750667742041e-05, "-9": 2.1092186599306343e-06, "0": 0.22123744233386983, "1": 0.2141365882031608, "10": 1.3456837524190553e-05, "11": 2.4213779202885564e-06, "12": 4.006168380319753e-07, "13": 6.133239133419593e-08, "14": 8.735834071205432e-09, "15": 1.1625146923641802e-09, "16": 1.4377209339285943e-10, "17": 1.4688719755094753e-11, "2": 0.15852732181091908, "3": 0.08859277840785361, "4": 0.03968102296610007, "5": 0.014749816354135272, "6": 0.004671768778963427, "7": 0.0012868233266133922, "8": 0.00031323749461335923, "9": 6.825777947514297e-05} |
| Raw goal margin distribution | {"-1": 0.1445508692306922, "-10": 2.8257340531008774e-07, "-11": 3.455172083274906e-08, "-12": 3.884678935763073e-09, "-13": 4.041426245795382e-10, "-14": 3.911721828738414e-11, "-15": 3.537373069751624e-12, "-16": 2.9728694545408707e-13, "-17": 2.0639730161084055e-14, "-2": 0.07320517411881834, "-3": 0.0278006407079291, "-4": 0.008461710645597921, "-5": 0.0021373751280092616, "-6": 0.00046003863472219854, "-7": 8.610943079558253e-05, "-8": 1.4243750667742041e-05, "-9": 2.1092186599306343e-06, "0": 0.22123744233386983, "1": 0.2141365882031608, "10": 1.3456837524190553e-05, "11": 2.4213779202885564e-06, "12": 4.006168380319753e-07, "13": 6.133239133419593e-08, "14": 8.735834071205432e-09, "15": 1.1625146923641802e-09, "16": 1.4377209339285943e-10, "17": 1.4688719755094753e-11, "2": 0.15852732181091908, "3": 0.08859277840785361, "4": 0.03968102296610007, "5": 0.014749816354135272, "6": 0.004671768778963427, "7": 0.0012868233266133922, "8": 0.00031323749461335923, "9": 6.825777947514297e-05} |
| Unadjusted home-win probability | 52.2% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 25.7% |
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 56.0% |
| Raw p btts yes | 65.1% |
| P home draw | 74.3% |
| P draw away | 47.8% |
| P home away | 77.9% |
| Raw p home draw | 74.3% |
| Raw p draw away | 47.8% |
| Raw p home away | 77.9% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.6589 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.04718293956967018, 0.05776016546375613, 0.04022309412785237, 0.017953505055723074, 0.006010135795893653, 0.0016095679221620374, 0.0003592138602790366, 6.871476622828752e-05, 1.1501516693628765e-05, 1.7112270333322645e-06, 2.291409240927619e-07, 2.7893627879745864e-08, 3.1125675437205376e-09, 3.206051246704714e-10, 3.0664610458250756e-11, 2.737418643847021e-12, 2.2909534556995986e-13], [0.07687256368795495, 0.10835568066035914, 0.07099516547738861, 0.03168856324873305, 0.010608099516530876, 0.0028409435787751444, 0.0006340250049193172, 0.00012128396148766939, 2.030057852609858e-05, 3.0203754592981526e-06, 4.0444173120791114e-07, 4.923322708075798e-08, 5.493790386278949e-09, 5.658792385918877e-10, 5.4124108077396494e-11, 4.8316394801223255e-12, 4.043612835238453e-13], [0.06988629558927101, 0.09358086356058704, 0.0626544728898869, 0.027965710251348808, 0.009361833007958694, 0.0025071823023605244, 0.0005595381349576502, 0.00010703521325585873, 1.7915614934619186e-05, 2.6655340692479583e-06, 3.569268880931844e-07, 4.3449182358697965e-08, 4.848365920486008e-09, 4.993983065593017e-10, 4.7765470217892385e-11, 4.264006186695158e-12, 3.568558916076284e-13], [0.04111725057078881, 0.055057830483179485, 0.036862444052474165, 0.016453484994435955, 0.005507987372122415, 0.0014750880996564236, 0.00032920144793734856, 6.297362946812999e-05, 1.0540561954031986e-05, 1.56825356539671e-06, 2.099961397214536e-07, 2.5563107946627918e-08, 2.8525117082053627e-09, 2.938184823260083e-10, 2.8102574203148125e-11, 2.5087065974155656e-12, 2.0995436929619879e-13], [0.01814334570439636, 0.024294748270451135, 0.01626587519030647, 0.007260243867284012, 0.002430447504164173, 0.000650895499212221, 0.00014526301232209476, 2.778766366524893e-05, 4.651114965028194e-06, 6.92005574160617e-07, 9.266262959376564e-08, 1.127994450786485e-08, 1.2586956892632332e-09, 1.2964996990749836e-10, 1.2400506159169137e-11, 1.106988683240094e-12, 9.264419802903071e-14], [0.006404727724340599, 0.008576215783946071, 0.0057419675229346484, 0.002562916781715746, 0.0008579649402096093, 0.00022977065627112378, 5.127885768693203e-05, 9.809239308511152e-06, 1.6418760602898753e-06, 2.442827997898306e-07, 3.2710555287809296e-08, 3.981899176458926e-09, 4.4432836748399723e-10, 4.576734469239978e-11, 4.377465263986124e-12, 3.9077473502371374e-13, 3.270404881675461e-14], [0.0018840946744916552, 0.0025228867145148876, 0.001689128858663391, 0.0007539396001557706, 0.00025238967905008054, 6.759220508151225e-05, 1.508482902634414e-05, 2.885608309583971e-06, 4.829947617618642e-07, 7.186127841231792e-08, 9.622545355551625e-09, 1.171365178291224e-09, 1.3070918030139372e-10, 1.3463493549126979e-11, 1.2877298374924434e-12, 1.149551751257105e-13, 9.620631330788748e-15], [0.00047507041163051203, 0.0006361404478175262, 0.0004259102013537103, 0.00019010424531197407, 6.363951363004907e-05, 1.7043228838673853e-05, 3.8036071286357994e-06, 7.275999162878344e-07, 1.2178608824288474e-07, 1.811966647846172e-08, 2.426304073190261e-09, 2.9535720521613553e-10, 3.295803811261447e-11, 3.3947908823075575e-12, 3.2469830324820917e-13, 2.898569966011056e-14, 2.4258214559713487e-15], [0.00010481448288113132, 0.00014035126256110308, 9.396829694249158e-05, 4.19425787800474e-05, 1.404074543191755e-05, 3.760236743053041e-06, 8.391874225604598e-07, 1.6052990694225276e-07, 2.686958722072925e-08, 3.997730495149524e-09, 5.353139250895126e-10, 6.516447240671961e-11, 7.271510994957603e-12, 7.489905540473634e-13, 7.163798021126008e-14, 6.39509648768693e-15, 5.352074455593388e-16], [2.055569130653595e-05, 2.7524986513175575e-05, 1.8428591655042037e-05, 8.22556843580941e-06, 2.753600655927186e-06, 7.374387928560489e-07, 1.6457723333943684e-07, 3.148232116275527e-08, 5.269528840491783e-09, 7.840148777742248e-10, 1.0498308529279615e-10, 1.2779729882032791e-11, 1.4260523091445633e-12, 1.4688827533471066e-13, 1.404928180313033e-14, 1.2541742864436672e-15, 1.0496220306075579e-16], [3.628151283367112e-06, 4.858256219808432e-06, 3.2527107683617363e-06, 1.451841547519093e-06, 4.860201296419612e-07, 1.3016052161936506e-07, 2.9048456286343775e-08, 5.556739602024844e-09, 9.300902382831196e-10, 1.3838136322231152e-10, 1.852988109019651e-11, 2.255666943093243e-12, 2.5170321145688543e-13, 2.5926293439606145e-14, 2.479747289657245e-15, 2.2136614035840208e-16, 1.8526195303333544e-17], [5.821648807046581e-07, 7.795447134752951e-07, 5.219225518823173e-07, 2.3295918370005769e-07, 7.798568160324571e-08, 2.0885260459886538e-08, 4.6610490488973015e-09, 8.916217640509887e-10, 1.4924015850633196e-10, 2.220435795535527e-11, 2.973262461187794e-12, 3.619391735001273e-13, 4.038772328555911e-14, 4.160073918796143e-15, 3.97894594880634e-16, 3.5519906042672033e-17, 2.972671048233428e-18], [8.562844500346392e-08, 1.1466030301375106e-07, 7.676762719837653e-08, 3.4265091060400386e-08, 1.1470620900625792e-08, 3.071934491320999e-09, 6.855761921929292e-10, 1.3114529528905792e-10, 2.1951174192265957e-11, 3.265955585840189e-12, 4.3732600432804785e-13, 5.3236273158802475e-14, 5.940478474047783e-15, 6.11889642561068e-16, 5.852482099860083e-17, 5.2244895250666245e-18, 4.372390156186363e-19], [1.162593808053336e-08, 1.5567649080619615e-08, 1.0422887865845164e-08, 4.652237080516141e-09, 1.5573881825198691e-09, 4.170824330876023e-10, 9.308199348476318e-11, 1.7805848074459046e-11, 2.9803529883552385e-12, 4.434250489217e-13, 5.937658971991459e-14, 7.227990831289305e-15, 8.065501470361512e-16, 8.307742942484699e-17, 7.946027106722624e-18, 7.093389552778008e-19, 5.93647790961285e-20], [1.4657276155721851e-09, 1.962674582381252e-09, 1.3140543561436747e-09, 5.865257767473503e-10, 1.9634603689377502e-10, 5.258321830994054e-11, 1.1735212024875032e-11, 2.244853108680941e-12, 3.757447914246033e-13, 5.5904335214829016e-14, 7.485839565643523e-15, 9.11261155283674e-16, 1.0168494066161916e-16, 1.0473897391784588e-17, 1.0017868049641452e-18, 8.94291444139618e-20, 7.484350553976637e-21], [1.724706943753319e-10, 2.3094594415754753e-10, 1.5462345448308694e-10, 6.90158982541627e-11, 2.3103840687134934e-11, 6.187414413192159e-12, 1.3808705963296109e-12, 2.641496075474309e-13, 4.421351170327598e-14, 6.578206899191791e-15, 8.808512128393389e-16, 1.0722718364536553e-16, 1.1965164698474752e-17, 1.232452972015455e-18, 1.17879245797496e-19, 1.0523037480225618e-20, 8.806760023340632e-22], [1.9026049823915206e-11, 2.5476728415149813e-11, 1.7057237228598217e-11, 7.613466876687958e-12, 2.5486928410030216e-12, 6.82562654095991e-13, 1.5233030087402705e-13, 2.913957998700958e-14, 4.877399488669901e-15, 7.256728029613981e-16, 9.717082153369249e-17, 1.1828732677768022e-17, 1.3199333401483202e-18, 1.3595765782776505e-19, 1.3003811527933901e-20, 1.160845534499892e-21, 9.715149324250005e-23]] |
| Legacy trial inputs | {"lambda_home": 1.7650349138165433, "lambda_away": 1.339044554751785, "rho": -0.021851862651747548, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4730 |
| Legacy p draw | 0.2373 |
| Legacy p away | 0.2897 |
| Legacy p over 1 5 | 0.8182 |
| Legacy p under 3 5 | 0.6239 |
| Legacy p btts yes | 0.6139 |
| Legacy p over 2 5 | 0.5997 |
| Legacy goal margin distribution | {"-1": 0.16293421442092323, "-10": 2.8352913647785744e-07, "-11": 3.3916058839519324e-08, "-12": 3.728813603325762e-09, "-13": 3.7920319330385924e-10, "-14": 3.585310582998071e-11, "-15": 3.1417799273708664e-12, "-16": 2.2909534556995986e-13, "-2": 0.08290415239860895, "-3": 0.03142749221647669, "-4": 0.00947849646218287, "-5": 0.0023618946235071736, "-6": 0.000500078468972374, "-7": 9.190261303092278e-05, "-8": 1.4905687929251432e-05, "-9": 2.1621046034232466e-06, "0": 0.23732263637623005, "1": 0.21550564186156437, "10": 4.489318546902907e-06, "11": 7.07858383764343e-07, "12": 1.0258171303132238e-07, "13": 1.3750849584274387e-08, "14": 1.7137307969583308e-09, "15": 1.9794742279048173e-10, "16": 1.9026049823915206e-11, "2": 0.1440432225748444, "3": 0.07197547600124285, "4": 0.028613602739022814, "5": 0.009398355775398288, "6": 0.0026229365968420447, "7": 0.0006353832603820566, "8": 0.00013583703905394146, "9": 2.5971746550698105e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.4730 |
| Legacy raw p draw | 0.2373 |
| Legacy raw p away | 0.2897 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.7650 |
| Legacy lambda away | 1.3390 |
| Legacy model home team | Barcelona |
| Legacy model away team | Real Madrid |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 10.654616418300819, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,725.4846 |
| Elo away rating | 1,670.4419 |
| Elo rating diff | 115.0427 |
| Elo home expectancy | 0.6598 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **40.1%**. Expected goals are 1.40 for Celta Vigo and 1.25 for Real Betis (2.65 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 49.3%; Under 3.5 goals: 72.6%; Double Chance 1X: 66.9%; Double Chance X2: 59.9%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 54.1%; BTTS No (at least one team does not score): 45.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 40.1% | 2.49 |
| Draw | 26.8% | 3.73 |
| Real Betis win | 33.1% | 3.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.40 |
| Real Betis expected goals | 1.25 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.3% |
| Under 2.5 | 50.7% |
| Over 3.5 | 27.4% |
| Under 3.5 | 72.6% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.77% |
| 2 | 1-0 | 9.51% |
| 3 | 2-1 | 8.66% |
| 4 | 0-1 | 8.44% |
| 5 | 1-2 | 7.72% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T15:15:00+00:00 |
| Fixture id | 2013e3955186ebe5258e85eb741a7553 |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3994 |
| Dc lambda away | 1.2481 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:38:54.715248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.1% |
| P btts no | 45.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.37 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.93 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.64 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.73 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.1876519948444608, "-10": 2.0966453572509842e-07, "-11": 2.348226251606447e-08, "-12": 2.414931340564352e-09, "-13": 2.2820931699606238e-10, "-14": 1.8088570357882617e-11, "-2": 0.09517709029989516, "-3": 0.03490521358853229, "-4": 0.0100595713748649, "-5": 0.002378042541986789, "-6": 0.0004754936004587667, "-7": 8.227582604106791e-05, "-8": 1.2537882742469943e-05, "-9": 1.7061626137447068e-06, "0": 0.26825332488454373, "1": 0.21088113700382516, "10": 6.582405348675262e-07, "11": 8.265812500342719e-08, "12": 9.530953772585739e-09, "13": 1.009836144681941e-09, "14": 8.974448053050371e-11, "2": 0.11964769954482851, "3": 0.049198084455103, "4": 0.015897298715774725, "5": 0.004213562524424654, "6": 0.0009446272375547354, "7": 0.00018326266744442073, "8": 3.131208020910308e-05, "9": 4.7774274742581635e-06} |
| Raw goal margin distribution | {"-1": 0.1876519948444608, "-10": 2.0966453572509842e-07, "-11": 2.348226251606447e-08, "-12": 2.414931340564352e-09, "-13": 2.2820931699606238e-10, "-14": 1.8088570357882617e-11, "-2": 0.09517709029989516, "-3": 0.03490521358853229, "-4": 0.0100595713748649, "-5": 0.002378042541986789, "-6": 0.0004754936004587667, "-7": 8.227582604106791e-05, "-8": 1.2537882742469943e-05, "-9": 1.7061626137447068e-06, "0": 0.26825332488454373, "1": 0.21088113700382516, "10": 6.582405348675262e-07, "11": 8.265812500342719e-08, "12": 9.530953772585739e-09, "13": 1.009836144681941e-09, "14": 8.974448053050371e-11, "2": 0.11964769954482851, "3": 0.049198084455103, "4": 0.015897298715774725, "5": 0.004213562524424654, "6": 0.0009446272375547354, "7": 0.00018326266744442073, "8": 3.131208020910308e-05, "9": 4.7774274742581635e-06} |
| Unadjusted home-win probability | 40.1% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 33.1% |
| Raw p over 1 5 | 74.6% |
| Raw p under 3 5 | 72.6% |
| Raw p btts yes | 54.1% |
| P home draw | 66.9% |
| P draw away | 59.9% |
| P home away | 73.2% |
| Raw p home draw | 66.9% |
| Raw p draw away | 59.9% |
| Raw p home away | 73.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.4934 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.07816237553097911, 0.09306542211949223, 0.06087272403950542, 0.02578168513892446, 0.008189570523054732, 0.0020811382961411786, 0.0004407167013492626, 7.999655540499824e-05, 1.270548120808402e-05, 1.793735597313709e-06, 2.2791255256989952e-07, 2.6326030383802318e-08, 2.787494058391685e-09, 2.724459875687139e-10, 2.4726474482002862e-11], [0.09635334161204406, 0.1286747419113656, 0.07999911589951812, 0.033882367678751565, 0.010762758062477135, 0.002735038169934287, 0.000579191206347391, 0.00010513171224690723, 1.6697581384151924e-05, 2.357332684002499e-06, 2.9952335788622847e-07, 3.4597747826780984e-08, 3.6633330241927897e-09, 3.580493312854428e-10, 3.2495606679084575e-11], [0.0651220407578973, 0.08274424926349765, 0.052567538628229694, 0.022264154443979084, 0.007072224409407071, 0.0017971976693878602, 0.00038058740737884614, 6.908220525252721e-05, 1.0972005684561602e-05, 1.5490068300446828e-06, 1.9681724614954433e-07, 2.2734231808491953e-08, 2.407181605596768e-09, 2.3527475074599787e-10, 2.135291171837596e-11], [0.02852786021110295, 0.036247579909808966, 0.023028138801777814, 0.009753206108167267, 0.0030981128199464216, 0.0007872941831571729, 0.00016672303615566824, 3.0262680216756334e-05, 4.8064808897537815e-06, 6.785698021633257e-07, 8.621927107847186e-08, 9.95913180071554e-09, 1.0545084206206356e-09, 1.0306626024569064e-10, 9.354020136845603e-12], [0.009372849791937038, 0.011909169468085347, 0.007565912212824725, 0.0032044231556517533, 0.0010178872822901289, 0.000258666092240805, 5.4776978125214584e-05, 9.942826201268574e-06, 1.579172888331267e-06, 2.2294461561284363e-07, 2.8327405946636686e-08, 3.2720801958318776e-09, 3.464595296552685e-10, 3.386249682770025e-11, 3.073270306452419e-12], [0.0024635654429636645, 0.0031302132230062855, 0.001988628889374285, 0.0008422524980275781, 0.0002675421018311148, 6.798795033065432e-05, 1.4397613679389448e-05, 2.6133783831583984e-06, 4.150707460931175e-07, 5.859889605732291e-08, 7.445592314833754e-09, 8.600355149179524e-10, 9.106362990884663e-11, 8.90043891122132e-12, 8.077802047329973e-13], [0.0005396041782462761, 0.0006856225958032513, 0.00043557700517048636, 0.0001844817917754612, 5.860077166498455e-05, 1.4891661260148006e-05, 3.15356448937203e-06, 5.724182805528858e-07, 9.091453588105426e-08, 1.2835140728030195e-08, 1.630836612876581e-09, 1.8837687410147662e-10, 1.9946015773777415e-11, 1.9494972372006916e-12, 1.76931193292837e-13], [0.00010130706058424644, 0.00012872103784798228, 8.177665746645024e-05, 3.463521746037548e-05, 1.1001901328196678e-05, 2.7958093919601723e-06, 5.920605541258986e-07, 1.0746768791889274e-07, 1.7068593546521842e-08, 2.409711473265186e-09, 3.061786216716257e-10, 3.5366493008435033e-11, 3.744730507787444e-12, 3.6600501382287886e-13, 3.321764330368054e-14], [1.6642255232119572e-05, 2.114569659069315e-05, 1.3433890962165704e-05, 5.689713290182719e-06, 1.8073414516866997e-06, 4.5928263255318995e-07, 9.726096875981769e-08, 1.7654294589513578e-08, 2.8039495827470257e-09, 3.9585625268928433e-10, 5.029760748255426e-11, 5.809843854090402e-12, 6.151670034318855e-13, 6.012561040807648e-14, 5.4568407658974535e-15], [2.4301446194150944e-06, 3.087748630034222e-06, 1.961651073377883e-06, 8.308264682461004e-07, 2.639126153879397e-07, 6.706562318163558e-08, 1.4202295098479134e-08, 2.5779251915013046e-09, 4.094398803878966e-10, 5.7803941179681495e-11, 7.344585123131432e-12, 8.483682400454008e-13, 8.98282572031739e-14, 8.779695214638652e-15, 7.968218274081667e-16], [3.1937033232652683e-07, 4.057928479796227e-07, 2.57800770459567e-07, 1.091874628158122e-07, 3.468347480566639e-08, 8.813784246453536e-09, 1.8664698673334072e-09, 3.387916992861347e-10, 5.3808711474417917e-11, 7.596611229162645e-12, 9.652275723983527e-13, 1.1149280770943712e-13, 1.1805256413997016e-14, 1.153830169621611e-15, 1.0471856275188557e-16], [3.815613140337078e-08, 4.848128853192319e-08, 3.080023119833299e-08, 1.3044953638778393e-08, 4.1437387517180666e-09, 1.0530092367026897e-09, 2.2299275264426374e-10, 4.0476460359243335e-11, 6.428688133639213e-12, 9.075899259919342e-13, 1.1531863281819646e-13, 1.3320380107011855e-14, 1.4104093880655743e-15, 1.3785155073278236e-16, 1.2511040745788133e-17], [4.178741829201033e-09, 5.3095211928118746e-09, 3.3731463259969435e-09, 1.4286430889462727e-09, 4.538094878653204e-10, 1.1532232388621703e-10, 2.4421478509766976e-11, 4.432857100031515e-12, 7.040500968752116e-13, 9.939644948305535e-14, 1.2629340997633264e-14, 1.4588069462699894e-15, 1.5446368616098186e-16, 1.509707667104892e-17, 1.3701705956134962e-18], [4.224396156497415e-10, 5.367529710263179e-10, 3.409999219207409e-10, 1.444251552411683e-10, 4.587675273269657e-11, 1.1658226368017346e-11, 2.4688292354344594e-12, 4.4812877323066903e-13, 7.11742109176899e-14, 1.004823931049099e-14, 1.2767321301516693e-15, 1.4747449612298606e-16, 1.5615126006998003e-17, 1.5262017915981107e-18, 1.385140225081124e-19], [3.965510040609969e-11, 5.038588278843866e-11, 3.201022262422231e-11, 1.3557426481998476e-11, 4.306526112904355e-12, 1.0943768530555656e-12, 2.317530543769865e-13, 4.206658381220249e-14, 6.681240053504051e-15, 9.43244724217384e-16, 1.198489415699973e-16, 1.3843673117875469e-17, 1.4658175197631546e-18, 1.432670683423139e-19, 1.3002538745717918e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3142029892994436, "lambda_away": 1.2706028297103589, "rho": -0.021851862651747548, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3751 |
| Legacy p draw | 0.2702 |
| Legacy p away | 0.3546 |
| Legacy p over 1 5 | 0.7324 |
| Legacy p under 3 5 | 0.7393 |
| Legacy p btts yes | 0.5288 |
| Legacy p over 2 5 | 0.4777 |
| Legacy goal margin distribution | {"-1": 0.19870045887904395, "-10": 2.650236215328294e-07, "-11": 3.023399217887795e-08, "-12": 3.166896301395504e-09, "-13": 3.0494159424779846e-10, "-14": 2.4726474482002862e-11, "-2": 0.10267209404273489, "-3": 0.03851873495111268, "-4": 0.011337098219196167, "-5": 0.0027344487710213045, "-6": 0.0005575281968418338, "-7": 9.833272801681394e-05, "-8": 1.526994580693654e-05, "-9": 2.1170823657060823e-06, "0": 0.270247001306272, "1": 0.20561319672806458, "10": 3.7137349886580103e-07, "11": 4.3820209944585396e-08, "12": 4.747505022851574e-09, "13": 4.728254984381801e-10, "14": 3.965510040609969e-11, "2": 0.10983928185323856, "3": 0.04262161609191497, "4": 0.012975151552309596, "5": 0.0032369273634209102, "6": 0.0006826256948850011, "7": 0.0001245278572831047, "8": 2.0001315285719428e-05, "9": 2.8682133128115824e-06} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3751 |
| Legacy raw p draw | 0.2702 |
| Legacy raw p away | 0.3546 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.3142 |
| Legacy lambda away | 1.2706 |
| Legacy model home team | Celta |
| Legacy model away team | Betis |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 8.736079430814915, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,477.5606 |
| Elo away rating | 1,548.8372 |
| Elo rating diff | -11.2766 |
| Elo home expectancy | 0.4838 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **54.6%**. Expected goals are 2.01 for Real Sociedad and 1.25 for Levante (3.26 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 63.2%; Under 3.5 goals: 59.0%; Double Chance 1X: 76.8%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 77.1%; BTTS Yes (both teams score): 62.0%; BTTS No (at least one team does not score): 38.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 54.6% | 1.83 |
| Draw | 22.2% | 4.51 |
| Levante win | 23.2% | 4.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 2.01 |
| Levante expected goals | 1.25 |
| Expected total goals | 3.26 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 83.9% |
| Under 1.5 | 16.1% |
| Over 2.5 | 63.2% |
| Under 2.5 | 36.8% |
| Over 3.5 | 41.0% |
| Under 3.5 | 59.0% |
| Over 4.5 | 22.9% |
| Under 4.5 | 77.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.98% |
| 2 | 2-1 | 9.69% |
| 3 | 2-0 | 7.76% |
| 4 | 1-0 | 7.42% |
| 5 | 3-1 | 6.48% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:30:00+00:00 |
| Fixture id | 3cb8660cd2375b60e81144a7572cfb89 |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0064 |
| Dc lambda away | 1.2493 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:38:54.715248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.0% |
| P btts no | 38.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.99 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.21 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.71 |
| Fair Over 3.5 odds | 2.44 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.36 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.13661477198806934, "-10": 1.233035921669504e-07, "-11": 1.3746782965168851e-08, "-12": 1.4088042748712628e-09, "-13": 1.3356624820614966e-10, "-14": 1.1779346359917052e-11, "-15": 9.705592316925778e-13, "-16": 7.443452846457344e-14, "-17": 4.7671132174324405e-15, "-2": 0.06456479941440528, "-3": 0.022648168647081923, "-4": 0.006337422288622856, "-5": 0.0014674730466500841, "-6": 0.00028901586830882404, "-7": 4.944003693315411e-05, "-8": 7.467508555864302e-06, "-9": 1.0090717163324027e-06, "0": 0.2217888289315859, "1": 0.2212981430880475, "10": 1.407641100484958e-05, "11": 2.520396727435226e-06, "12": 4.14829958221258e-07, "13": 6.316373459923696e-08, "14": 8.94630882656961e-09, "15": 1.1838491313184933e-09, "16": 1.4581438735090588e-10, "17": 1.4997988745711108e-11, "2": 0.1665325177760791, "3": 0.09381838513111784, "4": 0.042161798749993346, "5": 0.01567935662563476, "6": 0.004959425996285382, "7": 0.0013625113649733817, "8": 0.00033051311467233185, "9": 7.172765329661094e-05} |
| Raw goal margin distribution | {"-1": 0.13661477198806934, "-10": 1.233035921669504e-07, "-11": 1.3746782965168851e-08, "-12": 1.4088042748712628e-09, "-13": 1.3356624820614966e-10, "-14": 1.1779346359917052e-11, "-15": 9.705592316925778e-13, "-16": 7.443452846457344e-14, "-17": 4.7671132174324405e-15, "-2": 0.06456479941440528, "-3": 0.022648168647081923, "-4": 0.006337422288622856, "-5": 0.0014674730466500841, "-6": 0.00028901586830882404, "-7": 4.944003693315411e-05, "-8": 7.467508555864302e-06, "-9": 1.0090717163324027e-06, "0": 0.2217888289315859, "1": 0.2212981430880475, "10": 1.407641100484958e-05, "11": 2.520396727435226e-06, "12": 4.14829958221258e-07, "13": 6.316373459923696e-08, "14": 8.94630882656961e-09, "15": 1.1838491313184933e-09, "16": 1.4581438735090588e-10, "17": 1.4997988745711108e-11, "2": 0.1665325177760791, "3": 0.09381838513111784, "4": 0.042161798749993346, "5": 0.01567935662563476, "6": 0.004959425996285382, "7": 0.0013625113649733817, "8": 0.00033051311467233185, "9": 7.172765329661094e-05} |
| Unadjusted home-win probability | 54.6% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 23.2% |
| Raw p over 1 5 | 83.9% |
| Raw p under 3 5 | 59.0% |
| Raw p btts yes | 62.0% |
| P home draw | 76.8% |
| P draw away | 45.4% |
| P home away | 77.8% |
| Raw p home draw | 76.8% |
| Raw p draw away | 45.4% |
| Raw p home away | 77.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.6316 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.04896116429212747, 0.047491554357387895, 0.02635595519043591, 0.009324713640323636, 0.002474306580214279, 0.0005252444880595128, 9.291551770604478e-05, 1.4088612000443409e-05, 1.8692019253029343e-06, 2.204406627578986e-07, 2.3397513465721123e-08, 2.2576417020576343e-09, 1.9968790944996455e-10, 1.6303709026917307e-11, 1.2360509650016209e-12, 8.746274768040521e-14, 5.8020455227013316e-15, 3.622515132877145e-16], [0.09144098584282588, 0.10153091533127527, 0.05273007180688101, 0.018655852777109534, 0.004950318161653364, 0.0010508509128744079, 0.00018589506186408994, 2.8186932216072704e-05, 3.7396918848363618e-06, 4.410332273063856e-07, 4.681114974719817e-08, 4.516839105376366e-09, 3.995134203325542e-10, 3.261865265349258e-11, 2.472953671022767e-12, 1.749857644047165e-13, 1.160808913311002e-14, 7.247526477334464e-16], [0.09364443406059358, 0.09939395388812262, 0.05274823949025009, 0.018662280487420187, 0.0049520237503213735, 0.001051212974331922, 0.00018595911037584225, 2.81966437761389e-05, 3.7409803628477415e-06, 4.411851814334024e-07, 4.6827278117928714e-08, 4.518395342640675e-09, 3.996510691745448e-10, 3.262989112393323e-11, 2.473805705502183e-12, 1.750460542137925e-13, 1.1612088598323396e-14, 7.250023548962424e-16], [0.06245113228555013, 0.06628546613496049, 0.03517760895542335, 0.012445806941561345, 0.003302486617756658, 0.0007010501070230221, 0.00012401545396996475, 1.880423912149192e-05, 2.4948461898619403e-06, 2.942247919432533e-07, 3.122894136369856e-08, 3.013301410728583e-09, 2.665258436281572e-10, 2.1760755644326813e-11, 1.6497720223617338e-12, 1.1673757653012871e-13, 7.74405962767827e-15, 4.835014320622998e-16], [0.031236324637487156, 0.033154152105227076, 0.017594864545897475, 0.00622504751754601, 0.0016518122302655578, 0.00035064582384174034, 6.20290912030025e-05, 9.405358978507489e-06, 1.2478528836082737e-06, 1.471630822562854e-07, 1.5619850510656694e-08, 1.5071698086392334e-09, 1.33308836383989e-10, 1.088412656083255e-11, 8.251702184150541e-13, 5.838889871869167e-14, 3.8733638877222726e-15, 2.4183400911823667e-16], [0.012498834735577667, 0.013266230030921256, 0.007040370680810631, 0.002490876921209536, 0.0006609525390678626, 0.0001403066543129307, 2.482018511275058e-05, 3.76343980495279e-06, 4.993131281461973e-07, 5.888551440178346e-08, 6.250092877214762e-09, 6.030756363066609e-10, 5.334190670934459e-11, 4.355150636438678e-12, 3.3018180942813964e-13, 2.3363606440479705e-14, 1.5498793684995425e-15, 9.676693236129023e-17], [0.004167713699789763, 0.004423600264675195, 0.0023475987929091145, 0.0008305783769958241, 0.0002203934214877548, 4.6784998579680924e-05, 8.276245563218705e-06, 1.2549121550338616e-06, 1.6649505403381982e-07, 1.9635267629621764e-08, 2.0840820972838048e-09, 2.0109447357442264e-10, 1.778676173168619e-11, 1.4522170551201137e-12, 1.1009852355739865e-13, 7.79055205532992e-15, 5.168044552769669e-16, 3.2266757519467204e-17], [0.0011911856139886425, 0.001264321250661544, 0.000670973610704474, 0.00023738987013848125, 6.299124460185256e-05, 1.3371747982930359e-05, 2.365456305993562e-06, 3.5866986400030944e-07, 4.75864052694772e-08, 5.612009368206404e-09, 5.956571855645883e-10, 5.747535968858776e-11, 5.083682858373185e-12, 4.150621153596257e-13, 3.14675591534943e-14, 2.2266389204725778e-15, 1.4770929020441441e-16, 9.222249927865259e-18], [0.0002978990066338869, 0.00031618921536251746, 0.0001678011971930354, 5.936791518359896e-05, 1.5753236920558533e-05, 3.3440887753296986e-06, 5.91567825799871e-07, 8.969836013837408e-08, 1.1900700186923162e-08, 1.403485734192803e-09, 1.48965603504778e-10, 1.437379057981042e-11, 1.2713585991691887e-12, 1.0380128034199982e-13, 7.869600256193494e-15, 5.568515223417194e-16, 3.694004553593536e-17, 2.3063568432809245e-18], [6.622258780480525e-05, 7.028847901802613e-05, 3.7302002582788e-05, 1.3197415528363475e-05, 3.5019254577900905e-06, 7.433868781694138e-07, 1.315048100669746e-07, 1.993983664910557e-08, 2.6455112152681253e-09, 3.119931761961169e-10, 3.3114872954627726e-11, 3.1952762095954574e-12, 2.8262147435874883e-13, 2.307489870265768e-14, 1.749402590640293e-15, 1.2378741792124934e-16, 8.211727312079979e-18, 5.127003285079457e-19], [1.3249080843224433e-05, 1.4062539259293919e-05, 7.4629709320671294e-06, 2.6403925164069986e-06, 7.006264030932351e-07, 1.4872860111854638e-07, 2.6310023778983067e-08, 3.989341348957663e-09, 5.292845405869349e-10, 6.2420134141251e-11, 6.625256478683442e-12, 6.392754227929775e-13, 5.654376982136957e-14, 4.6165697912901915e-15, 3.50001066389279e-16, 2.476601355789413e-17, 1.6429113181283306e-18, 1.0257539498111544e-19], [2.4097537632230313e-06, 2.5577062515914115e-06, 1.357371315125594e-06, 4.802367709946892e-07, 1.2743050868549523e-07, 2.7050880773182044e-08, 4.785288848495096e-09, 7.255846984546267e-10, 9.626670925986547e-11, 1.1353025536461213e-11, 1.2050071186628616e-12, 1.1627194173240933e-13, 1.0284227541984068e-14, 8.396655254339786e-16, 6.365848294260817e-17, 4.504462994630174e-18, 2.988140670547792e-19, 1.865649753327908e-20], [4.017640037881664e-07, 4.2643124780474976e-07, 2.263064975828379e-07, 8.006703872642511e-08, 2.1245735624776705e-08, 4.510033486116012e-09, 7.978229296269865e-10, 1.2097244871553275e-10, 1.6049979518249747e-11, 1.8928228536252293e-12, 2.009037155479797e-13, 1.938533370154701e-14, 1.714628480384548e-15, 1.399924708033445e-16, 1.0613402652350515e-17, 7.51002494635696e-19, 4.9819503469758626e-20, 3.1104875776224766e-21], [6.183114277675863e-08, 6.562741091506273e-08, 3.482837992308154e-08, 1.2322250018735176e-08, 3.269700870228951e-09, 6.940903659329153e-10, 1.227842788483059e-10, 1.861755826320379e-11, 2.4700783688928918e-12, 2.913038475575357e-13, 3.091891310147859e-14, 2.9833865766318017e-15, 2.638798831655717e-16, 2.1544723689274817e-17, 1.6333937549336076e-18, 1.1557865322351044e-19, 7.667179744977933e-21, 4.787014259712387e-22], [8.836063736319938e-09, 9.378574609058077e-09, 4.977197105093634e-09, 1.7609279345446605e-09, 4.672610595659825e-10, 9.918992981081014e-11, 1.754665472768068e-11, 2.660567539925105e-12, 3.529899161017408e-13, 4.1629173391586286e-14, 4.418509420225282e-15, 4.2634492518402537e-16, 3.7710114380420046e-17, 3.0788781049570327e-18, 2.3342236091624305e-19, 1.6516924976273187e-20, 1.0956887720650632e-21, 6.840947976363518e-23], [1.1785477499354767e-09, 1.2509074552817573e-09, 6.638549272887544e-10, 2.348712862409113e-10, 6.232294003498302e-11, 1.3229880644056439e-11, 2.340360036472013e-12, 3.5486456201548665e-13, 4.7081538090498464e-14, 5.5524688477135485e-15, 5.893375705146298e-16, 5.686557581139757e-17, 5.0297476092406826e-18, 4.106585207175027e-19, 3.1133704605557656e-20, 2.2030154317047827e-21, 1.4614217093511573e-22, 9.124406619917292e-24], [1.4736922602715738e-10, 1.5641730555810411e-10, 8.301045658456745e-11, 2.936902613510654e-11, 7.793051607111566e-12, 1.6543048604123243e-12, 2.9264579837232123e-13, 4.437335343565975e-14, 5.887219952644897e-15, 6.942977377643344e-16, 7.36925777001578e-17, 7.11064604329617e-18, 6.289350705784518e-19, 5.13500011882497e-20, 3.893053931272932e-21, 2.754718076666746e-22, 1.827406536715686e-23, 1.1409437942653574e-24], [1.7343529505924403e-11, 1.84083762079625e-11, 9.76930083631839e-12, 3.4563699970889403e-12, 9.171454864275652e-13, 1.9469115725061888e-13, 3.444077963685468e-14, 5.2221931629494736e-15, 6.928527461883227e-16, 8.17102296417928e-17, 8.672702097755374e-18, 8.3683481811437e-19, 7.401785466307527e-20, 6.043258044753135e-21, 4.5816414692131555e-22, 3.2419614007044263e-23, 2.150630768937273e-24, 1.342749289922715e-25]] |
| Legacy trial inputs | {"lambda_home": 2.0006890824437193, "lambda_away": 1.0613973471590288, "rho": -0.021851862651747548, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5891 |
| Legacy p draw | 0.2175 |
| Legacy p away | 0.1934 |
| Legacy p over 1 5 | 0.8121 |
| Legacy p under 3 5 | 0.6333 |
| Legacy p btts yes | 0.5677 |
| Legacy p over 2 5 | 0.5906 |
| Legacy goal margin distribution | {"-1": 0.12256316321421086, "-10": 2.833661345576792e-08, "-11": 2.6914947565813286e-09, "-12": 2.349010755163095e-10, "-13": 1.895969464579066e-11, "-14": 1.423132319436723e-12, "-15": 9.979583916841147e-14, "-16": 6.526798170434778e-15, "-17": 3.622515132877145e-16, "-2": 0.05073084661517948, "-3": 0.015460185147971447, "-4": 0.0037312297238362756, "-5": 0.0007419846593484693, "-6": 0.00012515389621287437, "-7": 1.8302280004042002e-05, "-8": 2.360213508487613e-06, "-9": 2.7204795594030355e-07, "0": 0.2174868920746565, "1": 0.23294779160538756, "10": 1.604589663122562e-05, "11": 2.8728383305710825e-06, "12": 4.7261147083732805e-07, "13": 7.190385848472697e-08, "14": 1.017343801818335e-08, "15": 1.3447343563298992e-09, "16": 1.6577760223511988e-10, "17": 1.7343529505924403e-11, "2": 0.18025001888063572, "3": 0.10354270437430313, "4": 0.047104067007208976, "5": 0.017656432088973443, "6": 0.005613762057255677, "7": 0.0015474492904851574, "8": 0.0003761526510884538, "9": 8.172593669417748e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.5891 |
| Legacy raw p draw | 0.2175 |
| Legacy raw p away | 0.1934 |
| Legacy market weight | 0 |
| Legacy lambda home | 2.0007 |
| Legacy lambda away | 1.0614 |
| Legacy model home team | Sociedad |
| Legacy model away team | Levante |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 10.488199856444206, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,493.2106 |
| Elo away rating | 1,446.2845 |
| Elo rating diff | 106.9261 |
| Elo home expectancy | 0.6492 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **50.9%**. Expected goals are 1.54 for Sevilla and 1.09 for CA Osasuna (2.63 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 48.7%; Under 3.5 goals: 72.9%; Double Chance 1X: 77.6%; Double Chance X2: 49.1%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 87.4%; BTTS Yes (both teams score): 52.4%; BTTS No (at least one team does not score): 47.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 50.9% | 1.97 |
| Draw | 26.8% | 3.73 |
| CA Osasuna win | 22.4% | 4.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.54 |
| CA Osasuna expected goals | 1.09 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 74.3% |
| Under 1.5 | 25.7% |
| Over 2.5 | 48.7% |
| Under 2.5 | 51.3% |
| Over 3.5 | 27.1% |
| Under 3.5 | 72.9% |
| Over 4.5 | 12.6% |
| Under 4.5 | 87.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.76% |
| 2 | 1-0 | 11.55% |
| 3 | 2-1 | 10.00% |
| 4 | 2-0 | 9.22% |
| 5 | 0-0 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 50.9% | 52.4% | 1.88 | -4.4% |
| Draw | 26.8% | 27.0% | 3.45 | -7.6% |
| CA Osasuna win | 22.4% | 20.6% | 4.79 | +7.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T20:00:00+00:00 |
| Fixture id | 85e464708d03287f24590e1478aeca31 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-26T10:38:51Z |
| Market best draw last update utc | 2026-10-26T10:38:51Z |
| Market best away last update utc | 2026-10-26T10:38:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.5399 |
| Dc lambda away | 1.0852 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-26T10:38:54.715248+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.4% |
| P btts no | 47.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.83 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.89 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.69 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.91 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.13685854863066207, "-10": 4.4580449977910635e-08, "-11": 4.343702046410317e-09, "-12": 3.886914154489142e-10, "-13": 3.214766845121076e-11, "-14": 2.4596071060424786e-12, "-15": 1.6010867122977128e-13, "-2": 0.06100832565821089, "-3": 0.01954686274716965, "-4": 0.004913466229846076, "-5": 0.0010121482006596619, "-6": 0.0001762519268184835, "-7": 2.65497713476199e-05, "-8": 3.5212582864598687e-06, "-9": 4.169627782821076e-07, "0": 0.2677800132238897, "1": 0.247584615893122, "10": 1.8681323252903796e-06, "11": 2.5829309914320504e-07, "12": 3.27979963343555e-08, "13": 3.849297103179678e-09, "14": 4.1791434581797293e-10, "15": 3.8603437774094056e-11, "2": 0.1555018599812135, "3": 0.07069897763206581, "4": 0.025218173818207554, "5": 0.007371559136371452, "6": 0.0018215399817830909, "7": 0.0003893634739944603, "8": 7.32793980447795e-05, "9": 1.2313198681836444e-05} |
| Raw goal margin distribution | {"-1": 0.16143331533859048, "-10": 5.25854607638878e-08, "-11": 5.123671332270253e-09, "-12": 4.5848611188259765e-10, "-13": 3.7920208495635424e-11, "-14": 2.9012621683599738e-12, "-15": 1.888583056717262e-13, "-2": 0.07196317930303434, "-3": 0.023056761081543562, "-4": 0.005795744228070439, "-5": 0.0011938928278965462, "-6": 0.00020790029680869913, "-7": 3.131713475710169e-05, "-8": 4.153546892279001e-06, "-9": 4.918339726992373e-07, "0": 0.26229681751609063, "1": 0.23071593218447828, "10": 1.7408508574675966e-06, "11": 2.4069481429883107e-07, "12": 3.0563370307832386e-08, "13": 3.5870329269508665e-09, "14": 3.894405858814858e-10, "15": 3.59732695807738e-11, "2": 0.14490705108056176, "3": 0.06588204388237508, "4": 0.023499983872057668, "5": 0.00686931266575596, "6": 0.0016974329903026027, "7": 0.0003628349707317754, "8": 6.828665249991573e-05, "9": 1.147426346263344e-05} |
| Unadjusted home-win probability | 47.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 26.4% |
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 73.1% |
| Raw p btts yes | 52.4% |
| P home draw | 77.6% |
| P draw away | 49.1% |
| P home away | 73.2% |
| Raw p home draw | 73.6% |
| Raw p draw away | 52.6% |
| Raw p home away | 73.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE_OU25_QUOTE |
| Unanchored p over 2 5 | 0.4874 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:38:28Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.18, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-26T10:38:28Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.43, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.73, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.09, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:38:51Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:39:09Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.44, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-26T10:39:09Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.35, "price": 3.44, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.81 |
| Reference draw odds | 3.32 |
| Reference away odds | 4.25 |
| Market reference 1x2 last update utc | 2026-10-26T10:39:24Z |
| Market reference home last update utc | 2026-10-26T10:39:24Z |
| Market reference draw last update utc | 2026-10-26T10:39:24Z |
| Market reference away last update utc | 2026-10-26T10:39:24Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.18 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-26T10:39:16Z |
| Market reference under 2 5 last update utc | 2026-10-26T10:39:16Z |
| Home probability edge | -1.5% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | +5.4% |
| Under 2.5 probability edge | -5.4% |
| Raw edge prob home | -0.0495 |
| Raw ev home | -0.1088 |
| Raw edge prob draw | -0.0078 |
| Raw ev draw | -0.0951 |
| Raw edge prob away | 0.0573 |
| Raw ev away | 0.2631 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0883525535472642, 0.07411054458529996, 0.037511330444620544, 0.012247340861231002, 0.0029990410176058417, 0.000587506929198231, 9.590965629503178e-05, 1.3420382267808711e-05, 1.6431434933159453e-06, 1.7882719885808275e-07, 1.7515968911639875e-08, 1.5597035923388689e-09, 1.273096775790318e-10, 9.592209552293106e-12, 6.711061427887093e-13, 4.3822842791106574e-14], [0.12844620551289238, 0.12715088804961125, 0.05564801873953522, 0.018168917115894974, 0.004449074153601457, 0.0008715659033714305, 0.0001422818729047162, 1.9909122792466714e-05, 2.4376016212697165e-06, 2.6528995893346935e-07, 2.598492121400714e-08, 2.313818617090423e-09, 1.888637710171683e-10, 1.4230032648604853e-11, 9.955852476429293e-13, 6.501114057949734e-14], [0.09735874277477613, 0.09536204350394556, 0.04520217122356506, 0.013476784589593, 0.003300098382790114, 0.0006464835444207602, 0.00010553750341362906, 1.4767581222939248e-05, 1.80808970372566e-06, 1.9677868568185317e-07, 1.927430146468967e-08, 1.7162737263321802e-09, 1.400896015178513e-10, 1.0555119134774953e-11, 7.384748269517021e-13, 4.822197888431924e-14], [0.04814386371771834, 0.04715649663757319, 0.023094689576306813, 0.007298012739838934, 0.001631897478007211, 0.0003196858830679591, 5.218825794831834e-05, 7.302563668906811e-06, 8.940997162109059e-07, 9.730699016866651e-08, 9.531135227545796e-09, 8.486967480053012e-10, 6.927425818703431e-11, 5.21950266268786e-12, 3.6517553960176573e-13, 2.384575142856959e-14], [0.01785534262982552, 0.017489153127030924, 0.008565236843727946, 0.0027965250482698974, 0.000662784685699684, 0.00011856341671214893, 1.93553062625922e-05, 2.708336355157544e-06, 3.315989940437644e-07, 3.6088704054285784e-08, 3.5348572382319706e-09, 3.1476018030676493e-10, 2.5692072049075538e-11, 1.935781659444992e-12, 1.354343809597748e-13, 8.84378670808808e-15], [0.005297676352654381, 0.00518902800522336, 0.0025413039459744593, 0.0008297283857817436, 0.00020317793802149638, 3.852301652037729e-05, 5.742715242800127e-06, 8.035628193314867e-07, 9.838535085712871e-08, 1.0707510801107507e-08, 1.0487913891783814e-09, 9.338927841031701e-11, 7.622832301057337e-12, 5.743460057727272e-13, 4.018335196483401e-14, 2.6239496313611306e-15], [0.0013098495372561992, 0.001282986252651267, 0.0006283369492728926, 0.00020515019601376804, 5.0235709088717935e-05, 9.841088204378564e-06, 1.5549112892843328e-06, 1.986807643562937e-07, 2.432576052488163e-08, 2.6474301437778724e-09, 2.593134846950913e-10, 2.3090482499776178e-11, 1.8847439325202893e-12, 1.4200694791583719e-13, 9.935326636208847e-15, 6.487710803057771e-16], [0.00027759434180566405, 0.00027190124836512654, 0.00013316245637721018, 4.347715673743533e-05, 1.0646374413991858e-05, 2.0856062662498168e-06, 3.40472205895111e-07, 4.611023836033864e-08, 5.15531997359933e-09, 5.610656852831704e-10, 5.4955896885725554e-11, 4.893529454480279e-12, 3.9943080219438577e-13, 3.009530798560541e-14, 2.105578068134424e-15, 1.3749302946450267e-16], [5.1476363780259733e-05, 5.042065152375674e-05, 2.4693295265884895e-05, 8.062289460908334e-06, 1.974235637191623e-06, 3.8674933417419615e-07, 6.31362693263895e-08, 8.834489685970901e-09, 1.0469000578871653e-09, 1.0404254327516662e-10, 1.0190876808074517e-11, 9.07443216348378e-13, 7.406939617376465e-14, 5.580794665586263e-15, 3.904528525257303e-16, 2.5496345335884278e-17], [8.485014534522775e-06, 8.3109980892482e-06, 4.070275245755491e-06, 1.3289330914933528e-06, 3.254196070967938e-07, 6.374913612183861e-08, 1.040695425140723e-08, 1.4562173371558295e-09, 1.7829403027818275e-10, 1.878053827205829e-11, 1.6797949871743454e-12, 1.4957678271212248e-13, 1.2209096698837329e-14, 9.199003265620266e-16, 6.435959895825383e-17, 4.202644570538827e-18], [1.2587510019657679e-06, 1.2329356808538623e-06, 6.038248989468993e-07, 1.9714708250135096e-07, 4.827596403350584e-08, 9.457177550059398e-09, 1.543870554148383e-09, 2.160296867809571e-10, 2.644990039133741e-11, 2.878605317368162e-12, 2.7289518063936393e-13, 2.218969977525084e-14, 1.811218194173995e-15, 1.364671154135759e-16, 9.547739646785817e-18, 6.234618741721784e-19], [1.6975961545372396e-07, 1.6627806987566474e-07, 8.143396310035036e-08, 2.658795334501198e-08, 6.510667381545117e-09, 1.2754284379265466e-09, 2.0821184743707136e-10, 2.9134528192829227e-11, 3.5671271857663647e-12, 3.8821890187679365e-13, 3.802570447676359e-14, 3.277165138243501e-15, 2.442672964435324e-16, 1.840443820780182e-17, 1.2876419628341341e-18, 8.408227508398466e-20], [2.0986517384686795e-08, 2.0556111621783565e-08, 1.0067266456404755e-08, 3.2869333710904977e-09, 8.04880676853068e-10, 1.5767472737216438e-10, 2.5740171148814876e-11, 3.6017534604991677e-12, 4.4098578155581283e-13, 4.7993527268105166e-14, 4.7009243390051256e-15, 4.185922352252609e-16, 3.3069198174086663e-17, 2.275247039003315e-18, 1.5918462330422293e-19, 1.039466379019388e-20], [2.3948827827138124e-09, 2.3457668988220966e-09, 1.1488291584304643e-09, 3.7508939639961047e-10, 9.184920202820108e-11, 1.799309923275897e-11, 2.9373474206532123e-12, 4.1101518617964263e-13, 5.032322592219232e-14, 5.476795888962415e-15, 5.364474036334591e-16, 4.776777960549782e-17, 3.899010459495643e-18, 2.8433137855363103e-19, 1.816540146400078e-20, 1.1861902042593496e-21], [2.5377186114130204e-10, 2.485673353261902e-10, 1.2173477373198591e-10, 3.974605141669332e-11, 9.732728094786859e-12, 1.9066245383513744e-12, 3.112536977334167e-13, 4.3552899334785926e-14, 5.332460859081238e-15, 5.803443474832947e-16, 5.68442251149418e-17, 5.0616750099720035e-18, 4.131555615404216e-19, 3.1129406651201687e-20, 2.1079317721826224e-21, 1.256937074228607e-22], [2.5098019037575073e-11, 2.4583291804217653e-11, 1.2039560473409077e-11, 3.930881661340558e-12, 9.62566117109768e-13, 1.8856503138622594e-13, 3.078296859272051e-14, 4.3073786499812405e-15, 5.273800001168176e-16, 5.739601473535571e-17, 5.621889825352338e-18, 5.005992988779778e-19, 4.0861055683584134e-20, 3.0786961062056055e-21, 2.153968652780667e-22, 1.3613251321060458e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4834989343204072, "lambda_away": 0.9794913203075187, "rho": -0.021851862651747548, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5047 |
| Legacy p draw | 0.2687 |
| Legacy p away | 0.2266 |
| Legacy p over 1 5 | 0.7091 |
| Legacy p under 3 5 | 0.7643 |
| Legacy p btts yes | 0.4853 |
| Legacy p over 2 5 | 0.4471 |
| Legacy goal margin distribution | {"-1": 0.14499175546621945, "-10": 1.997523469124143e-08, "-11": 1.7594965018171217e-09, "-12": 1.4230203080601692e-10, "-13": 1.0636016778820353e-11, "-14": 7.361172833682067e-13, "-15": 4.3822842791106574e-14, "-2": 0.05932021559262401, "-3": 0.017397896242213384, "-4": 0.003983789558846667, "-5": 0.0007454876440330999, "-6": 0.00011772780594314335, "-7": 1.6064616237138457e-05, "-8": 1.9285827269529843e-06, "-9": 2.065996446703916e-07, "0": 0.26870653534998395, "1": 0.2499128321555472, "10": 1.4354813489873632e-06, "11": 1.915052648514718e-07, "12": 2.345794993890222e-08, "13": 2.655489678513412e-09, "14": 2.783551529455197e-10, "15": 2.5098019037575073e-11, "2": 0.1539625905765435, "3": 0.06839051473708525, "4": 0.023718224299284125, "5": 0.0067222224397929225, "6": 0.0016078225915277518, "7": 0.0003322890869812142, "8": 6.041859791113701e-05, "9": 9.802764898457612e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4859 |
| Legacy raw p draw | 0.2673 |
| Legacy raw p away | 0.2468 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4835 |
| Legacy lambda away | 0.9795 |
| Legacy model home team | Sevilla |
| Legacy model away team | Osasuna |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 95/100 |
| Count model | {"corners": {"alpha": 0.01460129601713404, "mu": 8.559671036495459, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,440.7731 |
| Elo away rating | 1,423.7802 |
| Elo rating diff | 76.9929 |
| Elo home expectancy | 0.6090 |
| Market p home draw | 77.2% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-26T10:39:09Z |
| Market reference home draw last update utc | 2026-10-26T10:39:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.3% |
| Market draw away odds | 2.00 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-26T10:39:09Z |
| Market reference draw away last update utc | 2026-10-26T10:39:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-26T10:39:09Z |
| Market reference home away last update utc | 2026-10-26T10:39:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.92 |
| Market reference dc home draw odds | 1.25 |
| Market reference dc home away odds | 1.33 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:39:09Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 2.66, "price": 1.45, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:39:09Z", "line": 7.5, "market_key": "alternate_totals_corners", "opposite_price": 1.45, "price": 2.66, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:39:09Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.02, "price": 1.81, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:39:09Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.81, "price": 2.02, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:39:09Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.6, "price": 2.29, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-26T10:39:09Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.29, "price": 1.6, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 70.4% |
| Market over 1 5 odds | 1.42 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-26T10:38:51Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 2.90 |
| Market reference over 1 5 last update utc | 2026-10-26T10:38:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 79.0% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 3.75 |
| Market reference under 3 5 last update utc | 2026-10-26T10:38:51Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 45.5% |
| Market btts yes odds | 2.11 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-26T10:39:09Z |
| Market reference btts yes odds | 2.11 |
| Market reference btts yes opposite odds | 1.78 |
| Market reference btts yes last update utc | 2026-10-26T10:39:09Z |
| Market btts yes bookmakers | 1 |

</details>


---
