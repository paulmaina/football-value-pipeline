# Premier League — football model report

Fixtures in this report: **2**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,988 |
| Training data through | 2026-10-31 |
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
| Training sha256 | 5dbc67abb74d17aad6716092b30491fc174e495c246f00de69431ffa0984f52a |
| Training as of utc | 2026-11-01T12:03:57.378405+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 88, 'bbs_added_results': 8, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 88, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 212, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-01T12:03:57.378405+00:00', 'observations': 576, 'observations_sha256': '3071ee95d1c21a154dc521fe86ed1bc36a93e26de4ccf16506c129332b8b188f', 'eligible_training_matches': 276, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 252, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 26, 'retrospective_eligible_training_matches': 276, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'b28c6bf0b892a6277f11253f9ba9cefc5056309437eb31c158cf7ea87791e429', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 216, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-03T00:00:00+00:00', 'audit_origin_utc': '2025-11-01T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 13, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1979, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1616, 'tuning_matches': 247, 'audit_matches': 107, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9197690623642132, 'audit_candidate_poisson_score': 0.91020295395996, 'audit_gain': 0.009566108404253204, 'audit_gain_lower95': 0.00106704065356859, 'audit_baseline_briers': [0.632655692234939, 0.1571100102185937, 0.22009131526644332, 0.25058796247925585], 'audit_candidate_briers': [0.6323775316870927, 0.1563108435222485, 0.217339355217242, 0.24791856581492158], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum']} |
| Optimizer objective | 1883.944 |
| Base scoring parameter | 0.213 |
| Home-advantage parameter | 0.180 |
| Dixon-Coles low-score adjustment | -0.069 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1988, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-31'} |
| Training data health | {'training_end': '2026-10-31', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261101T120357378405Z_fa0b586e0e3b2960bbf564058a52017b3657be7638a4d8279d3ad99310b28696.json |
| Over 1 5 in window quote fixtures | 0 |
| Odds provider health | — |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 2} |
| Legacy comparison status | {'AVAILABLE': 2} |
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

## 2026-11-01 — Liverpool vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **41.9%**. Expected goals are 1.19 for Liverpool and 1.44 for Arsenal (2.63 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 49.0%; Under 3.5 goals: 72.9%; Double Chance 1X: 58.1%; Double Chance X2: 69.6%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 54.0%; BTTS No (at least one team does not score): 46.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 30.4% | 3.29 |
| Draw | 27.7% | 3.61 |
| Arsenal win | 41.9% | 2.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.19 |
| Arsenal expected goals | 1.44 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 49.0% |
| Under 2.5 | 51.0% |
| Over 3.5 | 27.1% |
| Under 3.5 | 72.9% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.20% |
| 2 | 0-1 | 9.50% |
| 3 | 1-2 | 8.89% |
| 4 | 0-0 | 8.04% |
| 5 | 1-0 | 7.72% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:30:00+00:00 |
| Fixture id | 6a3819cdbe2ba2fe5a3d8f9b4b459965 |
| Matched home-team name | Liverpool |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1922 |
| Dc lambda away | 1.4401 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T12:03:57.378405+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.0% |
| P btts no | 46.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.43 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.96 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.69 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.86 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.21335947172573963, "-10": 8.878105857294833e-07, "-11": 1.1475345635814968e-07, "-12": 1.3619231078841056e-08, "-13": 1.4855039302814683e-09, "-14": 1.3611305795528068e-10, "-2": 0.1275283561347054, "-3": 0.054064631897409, "-4": 0.01800006120431882, "-5": 0.0049139047814268245, "-6": 0.0011343991125234059, "-7": 0.0002265909990113239, "-8": 3.98564840925325e-05, "-9": 6.25990006929828e-06, "0": 0.27666298599808786, "1": 0.17517341285221108, "10": 1.3428971867734578e-07, "11": 1.4370122317491052e-08, "12": 1.4119506663496625e-09, "13": 1.2750082171863435e-10, "14": 9.671887005799033e-12, "2": 0.08740801356907663, "3": 0.030678207736028088, "4": 0.008455960776856824, "5": 0.001911120008002896, "6": 0.00036525767058915616, "7": 6.0401589254339536e-05, "8": 8.79583231157016e-06, "9": 1.1437144308945146e-06} |
| Raw goal margin distribution | {"-1": 0.21335947172573963, "-10": 8.878105857294833e-07, "-11": 1.1475345635814968e-07, "-12": 1.3619231078841056e-08, "-13": 1.4855039302814683e-09, "-14": 1.3611305795528068e-10, "-2": 0.1275283561347054, "-3": 0.054064631897409, "-4": 0.01800006120431882, "-5": 0.0049139047814268245, "-6": 0.0011343991125234059, "-7": 0.0002265909990113239, "-8": 3.98564840925325e-05, "-9": 6.25990006929828e-06, "0": 0.27666298599808786, "1": 0.17517341285221108, "10": 1.3428971867734578e-07, "11": 1.4370122317491052e-08, "12": 1.4119506663496625e-09, "13": 1.2750082171863435e-10, "14": 9.671887005799033e-12, "2": 0.08740801356907663, "3": 0.030678207736028088, "4": 0.008455960776856824, "5": 0.001911120008002896, "6": 0.00036525767058915616, "7": 6.0401589254339536e-05, "8": 8.79583231157016e-06, "9": 1.1437144308945146e-06} |
| Unadjusted home-win probability | 30.4% |
| Unadjusted draw probability | 27.7% |
| Unadjusted away-win probability | 41.9% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 54.0% |
| P home draw | 58.1% |
| P draw away | 69.6% |
| P home away | 72.3% |
| Raw p home draw | 58.1% |
| Raw p draw away | 69.6% |
| Raw p home away | 72.3% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4897 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.0964615377246417, 0.11019979804386856, 0.08672003925249154, 0.041257370562284616, 0.014721256820101976, 0.004202214526225948, 0.0009996093370410815, 0.00020381474450747062, 3.636209914405893e-05, 5.766466481259393e-06, 8.230251502526032e-07, 1.0678832051888082e-07, 1.2701231887544715e-08, 1.3944592500867683e-09, 1.421612150121567e-10], [0.07690217782197326, 0.13723543547359204, 0.08985726411459621, 0.04274991657343447, 0.015253819919652524, 0.004354235812207952, 0.0010357716738157061, 0.00021118804241236036, 3.7677551517655274e-05, 5.975076880510113e-06, 8.527992945653403e-07, 1.106515449477675e-07, 1.316071761656919e-08, 1.444905862729859e-09, 1.47304105882681e-10], [0.04570674010622259, 0.06523543796835689, 0.046553991348247205, 0.02214822881497766, 0.007902824635987033, 0.002255878345808993, 0.0005366211181333226, 0.00010941404010230996, 1.9520296157015303e-05, 3.0956170337618302e-06, 4.418252811520576e-07, 5.732726359884569e-08, 6.818412958546371e-09, 7.485887278603552e-10, 7.631652419417129e-11], [0.015786749533111523, 0.02253180860188009, 0.016079383466714663, 0.007649824513660604, 0.002729573643678988, 0.0007791626867217361, 0.00018534472523004745, 3.779075126527852e-05, 6.742157185719014e-06, 1.069201843072997e-06, 1.5260298666529772e-07, 1.9800387202202345e-08, 2.3550263558445976e-09, 2.5855667506756014e-10, 2.635912887007678e-11], [0.004089464599345831, 0.005836732472594273, 0.004165269698395976, 0.0019816420393702827, 0.000707079995392347, 0.00020183751048919715, 4.801246076109545e-05, 9.789471807220087e-06, 1.7465161575150862e-06, 2.7697044775629227e-07, 3.95309059926016e-08, 5.129173826880066e-09, 6.100557237924769e-10, 6.697758568954427e-11, 6.828177273458497e-12], [0.0008474813982055528, 0.0012095769694686234, 0.0008631908901875606, 0.00041066617046570727, 0.0001465319306674372, 4.182785580955396e-05, 9.949876417468274e-06, 2.028724067254146e-06, 3.6193978923212705e-07, 5.7398052146891956e-08, 8.192198922152637e-09, 1.0629458455610526e-09, 1.264250772254276e-10, 1.3880119656173854e-11, 1.415039324177464e-12], [0.0001463567138714052, 0.00020888919898513569, 0.00014906968152821057, 7.092043711493635e-05, 2.5305489766652174e-05, 7.223506660483029e-06, 1.7183046365037074e-06, 3.503526902936605e-07, 6.250558216792261e-08, 9.912418505734725e-09, 1.4147606262106055e-09, 1.8356657893492217e-10, 2.183311503099724e-11, 2.3970422304499773e-12, 2.4437174187414596e-13], [2.1664483296969913e-05, 3.0920867534011183e-05, 2.2066070903929448e-05, 1.0498012592987934e-05, 3.7458504353478174e-06, 1.0692610899223042e-06, 2.543524045596496e-07, 5.186103053382669e-08, 9.252401922840046e-09, 1.4672878303263286e-09, 2.0942023870992834e-10, 2.717248138484286e-11, 3.231851436111511e-12, 3.548226793978402e-13, 3.617317839436844e-14], [2.8060284772445975e-06, 4.004934419722745e-06, 2.858042930845463e-06, 1.35972420327775e-06, 4.851702599597728e-07, 1.3849289765203987e-07, 3.2944247073265726e-08, 6.717147440923404e-09, 1.1983901449444246e-09, 1.9004614048588793e-10, 2.7124540450665168e-11, 3.5194357288886723e-12, 4.1859605141014973e-13, 4.595736390822782e-14, 4.6852245352762914e-15], [3.23060075677314e-07, 4.6109097865920483e-07, 3.290485371105744e-07, 1.565460249507278e-07, 5.5858000790105156e-08, 1.594478686124127e-08, 3.792894847265523e-09, 7.733500134436559e-10, 1.3797151884105613e-10, 2.1880148767357138e-11, 3.1228678403538555e-12, 4.051951653864515e-13, 4.819326430342562e-14, 5.291104342854375e-15, 5.394132686842394e-16], [3.3474724867797826e-08, 4.777716224228692e-08, 3.409523515041178e-08, 1.622093074604271e-08, 5.787874605655915e-09, 1.6521612958106855e-09, 3.9301083923325934e-10, 8.013270866806778e-11, 1.4296284129549172e-11, 2.2671695303673178e-12, 3.2358421737867544e-13, 4.1985369596153357e-14, 4.993672646352077e-15, 5.48251781816499e-16, 5.589273363905301e-17], [3.153247475792654e-09, 4.500506481711323e-09, 3.2116982170633627e-09, 1.5279769776142597e-09, 5.452054068425134e-10, 1.5563005987926704e-10, 3.702078035489926e-11, 7.548329742333014e-12, 1.346679383407913e-12, 2.1356251999256724e-13, 3.048094108869592e-14, 3.954932003837009e-15, 4.703932811765153e-16, 5.164414506584203e-17, 5.264975947032764e-18], [2.7227673643190883e-10, 3.886099097956078e-10, 2.773238433264331e-10, 1.3193781585548446e-10, 4.7077417804891626e-11, 1.3438350500535138e-11, 3.196671790773618e-12, 6.517834719704978e-13, 1.1628312409645853e-13, 1.8440704833398267e-14, 2.6319694938999853e-15, 3.4150062343081984e-16, 4.061753745035288e-17, 4.459370659072294e-18, 4.546203491022291e-19], [2.1702057500394363e-11, 3.0974495721254675e-11, 2.2104341608361092e-11, 1.0516220018261563e-11, 3.752347121390406e-12, 1.071115582972328e-12, 2.5479354542875855e-13, 5.1950976685985886e-14, 9.268448999857672e-15, 1.4698326485277674e-15, 2.0978345063345407e-16, 2.7219608488180885e-17, 3.2374566583378374e-18, 3.55438072774758e-19, 3.6235916025581136e-20], [1.6062258088148836e-12, 2.2925031159649893e-12, 1.6359999035835706e-12, 7.783328379901539e-13, 2.7772098520612534e-13, 7.92760545198394e-14, 1.8857934026747582e-14, 3.845027115270269e-15, 6.859820545118988e-16, 1.0878614318762794e-16, 1.5526619660996376e-17, 2.0145941304762613e-18, 2.3961260076134847e-19, 2.6306897671608545e-20, 2.681914538530718e-21]] |
| Legacy trial inputs | {"lambda_home": 1.0361764695812743, "lambda_away": 1.4272607894754592, "rho": -0.08989939716087265, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2625 |
| Legacy p draw | 0.2887 |
| Legacy p away | 0.4488 |
| Legacy p over 1 5 | 0.7164 |
| Legacy p under 3 5 | 0.7654 |
| Legacy p btts yes | 0.5017 |
| Legacy p over 2 5 | 0.4468 |
| Legacy goal margin distribution | {"-1": 0.22514701180233176, "-10": 9.407604930112581e-07, "-11": 1.2072398599218045e-07, "-12": 1.4222454274468745e-08, "-13": 1.5417633559694493e-09, "-14": 1.421612150121567e-10, "-2": 0.13820204833386796, "-3": 0.058962575089979555, "-4": 0.01965170985827524, "-5": 0.005354427746821289, "-6": 0.0012314274934979912, "-7": 0.00024474577407767255, "-8": 4.279942587313849e-05, "-9": 6.679016458404437e-06, "0": 0.2886514682976084, "1": 0.1603526579435645, "10": 3.826334913383905e-08, "11": 3.5647400600346126e-09, "12": 3.048872320567471e-10, "13": 2.3994560616359353e-11, "14": 1.6062258088148836e-12, "2": 0.07284089305993054, "3": 0.02256148155073418, "4": 0.005459110778659412, "5": 0.0010798539401419226, "6": 0.00018029811711518687, "7": 2.6015246086945188e-05, "8": 3.3027908354231504e-06, "9": 3.7418470557569574e-07} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.2625 |
| Legacy raw p draw | 0.2887 |
| Legacy raw p away | 0.4488 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.0362 |
| Legacy lambda away | 1.4273 |
| Legacy model home team | Liverpool |
| Legacy model away team | Arsenal |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 9.786775718535143, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,570.2236 |
| Elo away rating | 1,650.6613 |
| Elo rating diff | -20.4377 |
| Elo home expectancy | 0.4706 |

</details>


---

## 2026-11-02 — Newcastle United vs Everton

The model's most likely 1X2 outcome is **Newcastle United win** at **49.8%**. Expected goals are 1.60 for Newcastle United and 1.03 for Everton (2.63 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 49.0%; Under 3.5 goals: 72.9%; Double Chance 1X: 76.4%; Double Chance X2: 50.2%; Double Chance 12 (either team wins): 73.4%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 52.2%; BTTS No (at least one team does not score): 47.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Newcastle United win | 49.8% | 2.01 |
| Draw | 26.6% | 3.76 |
| Everton win | 23.6% | 4.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Newcastle United expected goals | 1.60 |
| Everton expected goals | 1.03 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 49.0% |
| Under 2.5 | 51.0% |
| Over 3.5 | 27.1% |
| Under 3.5 | 72.9% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.69% |
| 2 | 1-0 | 10.69% |
| 3 | 2-1 | 9.50% |
| 4 | 2-0 | 9.21% |
| 5 | 0-0 | 8.01% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T20:00:00+00:00 |
| Fixture id | 0f552d9c6990c69474f50ff2fb54e9a3 |
| Matched home-team name | Newcastle |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6004 |
| Dc lambda away | 1.0318 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T12:03:57.378405+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.2% |
| P btts no | 47.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.48 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.95 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.69 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.86 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.1466786089297804, "-10": 3.1466738793596725e-08, "-11": 2.915488719821032e-09, "-12": 2.4807955430146843e-10, "-13": 1.951037185936484e-11, "-14": 1.4195581555363964e-12, "-15": 8.796338234711356e-14, "-2": 0.06422039348410416, "-3": 0.019588101438099567, "-4": 0.004685390541069619, "-5": 0.0009181985779834378, "-6": 0.00015208781061025996, "-7": 2.1789413051917977e-05, "-8": 2.7483789494063797e-06, "-9": 3.094912134309799e-07, "0": 0.26607072510558194, "1": 0.23201524770132906, "10": 2.53563775204121e-06, "11": 3.6439330324339054e-07, "12": 4.8092077901537035e-08, "13": 5.866399882638181e-09, "14": 6.620379007253385e-10, "15": 6.362900493863962e-11, "2": 0.15449700222259116, "3": 0.07309084564543888, "4": 0.027116896662683607, "5": 0.008242412641439096, "6": 0.002117559843020941, "7": 0.00047055496866865644, "8": 9.205873286707834e-05, "9": 1.607904499265417e-05} |
| Raw goal margin distribution | {"-1": 0.1466786089297804, "-10": 3.1466738793596725e-08, "-11": 2.915488719821032e-09, "-12": 2.4807955430146843e-10, "-13": 1.951037185936484e-11, "-14": 1.4195581555363964e-12, "-15": 8.796338234711356e-14, "-2": 0.06422039348410416, "-3": 0.019588101438099567, "-4": 0.004685390541069619, "-5": 0.0009181985779834378, "-6": 0.00015208781061025996, "-7": 2.1789413051917977e-05, "-8": 2.7483789494063797e-06, "-9": 3.094912134309799e-07, "0": 0.26607072510558194, "1": 0.23201524770132906, "10": 2.53563775204121e-06, "11": 3.6439330324339054e-07, "12": 4.8092077901537035e-08, "13": 5.866399882638181e-09, "14": 6.620379007253385e-10, "15": 6.362900493863962e-11, "2": 0.15449700222259116, "3": 0.07309084564543888, "4": 0.027116896662683607, "5": 0.008242412641439096, "6": 0.002117559843020941, "7": 0.00047055496866865644, "8": 9.205873286707834e-05, "9": 1.607904499265417e-05} |
| Unadjusted home-win probability | 49.8% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 52.2% |
| P home draw | 76.4% |
| P draw away | 50.2% |
| P home away | 73.4% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.2% |
| Raw p home away | 73.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4896 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.0813026374834888, 0.06824007623594981, 0.044447252317526435, 0.01664590687896754, 0.004675534505099171, 0.0010506185366683427, 0.00019673317713502728, 3.157645436050406e-05, 4.4346277732025575e-06, 5.536030321084291e-07, 6.219883596780093e-08, 6.3529197430599356e-09, 5.948067931008565e-10, 5.140630214301831e-11, 4.125457579397477e-12, 3.090044001334253e-13], [0.0968451766748826, 0.13191393355438336, 0.0679920381234285, 0.025463646819569873, 0.007152278346635937, 0.0016071566153970536, 0.00030094750479397916, 4.830326683288604e-05, 6.783757485497208e-06, 8.46859963254005e-07, 9.514706547311155e-08, 9.718215161635248e-09, 9.098903541589803e-10, 7.863746514909656e-11, 6.3108123537340524e-12, 4.726915131690697e-13], [0.0823955215376261, 0.09257365352718053, 0.05200453354407744, 0.019476178560480076, 0.0054705066866651475, 0.00122925319526791, 0.00023018334263864406, 3.6945338448881876e-05, 5.188639044309865e-06, 6.477310959002376e-07, 7.277438498070212e-08, 7.433094525632051e-09, 6.959406534981975e-10, 6.014681728974765e-11, 4.8269012342939855e-12, 3.615438267636101e-13], [0.042014141478414646, 0.047204053131560036, 0.026517531402991103, 0.00993106064781942, 0.0027894555141228946, 0.0006268061260489135, 0.00011737234431094805, 1.8838726275315917e-05, 2.6457289282222985e-06, 3.302833138897468e-07, 3.710824629209483e-08, 3.79019489402375e-09, 3.5486575642708203e-10, 3.0669347604455014e-11, 2.4612758991683012e-12, 1.8435411542795105e-13], [0.01606751238927014, 0.018052295770574583, 0.01014112747178993, 0.003797945986339187, 0.0010667744110757142, 0.00023971012715172504, 4.4886829291578805e-05, 7.204513936866219e-06, 1.011808901407695e-06, 1.2631059569833564e-07, 1.4191345724597195e-08, 1.4494882264525804e-09, 1.357116850965346e-10, 1.1728910915830234e-11, 9.412683351774854e-13, 7.050273858799108e-14], [0.004915772552667492, 0.005523006792320078, 0.00310262565051563, 0.0011619619878823018, 0.0003263741295358187, 7.333807717713614e-05, 1.3732893932925569e-05, 2.2041838841094015e-06, 3.095577153191497e-07, 3.864407534918749e-08, 4.341769037313868e-09, 4.434634476316681e-10, 4.1520290167587214e-11, 3.5883998067568594e-12, 2.879761928704317e-13, 2.1569949276664658e-14], [0.0012532960508610058, 0.0014081128708725826, 0.0007910269308496057, 0.00029624689813471055, 8.321040147158087e-05, 1.8697838746418006e-05, 3.5012567299699627e-06, 5.61965576667445e-07, 7.892298880112329e-08, 9.85246296597479e-09, 1.1069515381185155e-09, 1.1306279565688652e-10, 1.0585765541451394e-11, 9.148770124196126e-13, 7.342069255638165e-14, 5.4993456178208575e-15], [0.0002738853309321833, 0.0003077177649796767, 0.00017286472145442095, 6.47394362070454e-05, 1.818413800026507e-05, 4.086076669005028e-06, 7.651367428370736e-07, 1.2280747859400058e-07, 1.7247201003388397e-08, 2.1530787383230583e-09, 2.4190436739603377e-10, 2.4707842319722134e-11, 2.3133288391829914e-12, 1.999299312693533e-13, 1.60447730320861e-14, 1.2017831648097634e-15], [5.2371127829103826e-05, 5.88404145274474e-05, 3.30544187730651e-05, 1.2379185397201144e-05, 3.477089526601011e-06, 7.813213026913358e-07, 1.4630602533359667e-07, 2.348269671079556e-08, 3.297932625191804e-09, 4.117020851283297e-10, 4.625587103988821e-11, 4.724523084545593e-12, 4.423443925794008e-13, 3.822970712500063e-14, 3.068009727254802e-15, 2.2979960092386733e-16], [8.901486929283822e-06, 1.0001067430490693e-05, 5.618238309162411e-06, 2.104082183754888e-06, 5.909986715196965e-07, 1.3280067953039056e-07, 2.4867541070191315e-08, 3.991338863611787e-09, 5.605474881617778e-10, 6.997673873832696e-11, 7.862080664136211e-12, 8.030241514258779e-13, 7.518499203676416e-14, 6.497878743303072e-15, 5.214676410099677e-16, 3.905889043775148e-17], [1.3616820097840146e-06, 1.5298875015965099e-06, 8.594355182501317e-07, 3.218665465092816e-07, 9.040649783657774e-08, 2.0314841513582277e-08, 3.804047972193001e-09, 6.105647706623342e-10, 8.574830658330492e-11, 1.0704511167664239e-11, 1.20268151656842e-12, 1.2284054889992044e-13, 1.1501230286079075e-14, 9.939962454368992e-16, 7.977016773588764e-17, 5.974933048122801e-18], [1.8936344930598267e-07, 2.1275508692251814e-07, 1.1951812025315214e-07, 4.476064090240107e-08, 1.2572455350808146e-08, 2.825100451849614e-09, 5.290131177206011e-10, 8.490870127282867e-11, 1.1924660082229533e-11, 1.488631812184135e-12, 1.6725191252990877e-13, 1.708292383037273e-14, 1.5994282237596876e-15, 1.3823092049441358e-16, 1.109330519581476e-17, 8.309090692505418e-19], [2.4139487806837457e-08, 2.712138401276212e-08, 1.523581354860728e-08, 5.70595301917963e-09, 1.6026991151415043e-09, 3.601353807213321e-10, 6.743701464921543e-11, 1.082390802756198e-11, 1.520120106127401e-12, 1.8976634409011034e-13, 2.1320775038598866e-14, 2.177680186011415e-15, 2.0389034022596278e-16, 1.7621265518938724e-17, 1.4141414644343226e-18, 1.0592181025047696e-19], [2.8405199242901872e-09, 3.1914029112396942e-09, 1.7928148390675908e-09, 6.714257306425799e-10, 1.8859135726617242e-10, 4.237752402066383e-11, 7.935387249247592e-12, 1.273661092438991e-12, 1.7887419498378719e-13, 2.2330013199160976e-14, 2.508838910877591e-15, 2.562500085583956e-16, 2.3991999267611142e-17, 2.073513580664108e-18, 1.664035723389632e-19, 1.2463935226833718e-20], [3.1037229350128865e-10, 3.487118793210626e-10, 1.9589373363173987e-10, 7.336401415575027e-11, 2.0606626128084528e-11, 4.630423187926105e-12, 8.670681445705098e-13, 1.3916787241069245e-13, 1.9544870525485904e-14, 2.4399115638203176e-15, 2.7413083081574743e-16, 2.799941735521128e-17, 2.621510159000377e-18, 2.265645666251072e-19, 1.8182255280803073e-20, 1.3618845371664023e-21], [3.16522675184195e-11, 3.5562200371069075e-11, 1.9977559182704873e-11, 7.481780593515772e-12, 2.1014969973648e-12, 4.722180314948808e-13, 8.842500907231095e-14, 1.4192564284073958e-14, 1.9932174470431057e-15, 2.4882611997389935e-16, 2.7956304649952935e-17, 2.8554257807272524e-18, 2.673458378609747e-19, 2.3105420242618713e-20, 1.8542557447505702e-21, 1.388871835604453e-22]] |
| Legacy trial inputs | {"lambda_home": 1.529724214169655, "lambda_away": 1.1235277330565419, "rho": -0.08989939716087265, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4555 |
| Legacy p draw | 0.2763 |
| Legacy p away | 0.2682 |
| Legacy p over 1 5 | 0.7536 |
| Legacy p under 3 5 | 0.7244 |
| Legacy p btts yes | 0.5396 |
| Legacy p over 2 5 | 0.4949 |
| Legacy goal margin distribution | {"-1": 0.15875177108753225, "-10": 7.26446239688233e-08, "-11": 7.32548869314642e-09, "-12": 6.784555135996751e-10, "-13": 5.8078658323515975e-11, "-14": 4.598149092566546e-12, "-15": 3.090044001334253e-13, "-2": 0.07605538408612413, "-3": 0.025152334936002566, "-4": 0.006532764774495246, "-5": 0.0013912878766190434, "-6": 0.0002505700119240878, "-7": 3.9046543127861796e-05, "-8": 5.358191691038667e-06, "-9": 6.56550080250054e-07, "0": 0.27629590515135977, "1": 0.22008016875053668, "10": 1.5903654148299423e-06, "11": 2.183531136689655e-07, "12": 2.7534266232302405e-08, "13": 3.2092093627939543e-09, "14": 3.4593449387235774e-10, "15": 3.16522675184195e-11, "2": 0.14099011099162168, "3": 0.06348430074716534, "4": 0.0224498993293524, "5": 0.006509741183923098, "6": 0.0015962656171262606, "7": 0.00033867879098258225, "8": 6.327803737664693e-05, "9": 1.0556791814358125e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.4555 |
| Legacy raw p draw | 0.2763 |
| Legacy raw p away | 0.2682 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.5297 |
| Legacy lambda away | 1.1235 |
| Legacy model home team | Newcastle |
| Legacy model away team | Everton |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.009199607322035784, "mu": 10.130198353646474, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,496.2139 |
| Elo away rating | 1,476.4968 |
| Elo rating diff | 79.7171 |
| Elo home expectancy | 0.6128 |

</details>


---
