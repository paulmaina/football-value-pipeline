# La Liga — football model report

Fixtures in this report: **5**.

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
| Training as of utc | 2026-11-05T12:26:42.954541+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 109, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 109, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 108, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-05T12:26:42.954541+00:00', 'observations': 583, 'observations_sha256': 'bd1b3a519db09934def0ee8a93db1e19ca3c6d977ffd04005cb961e04e46a3dd', 'eligible_training_matches': 176, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 183, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 30, 'retrospective_eligible_training_matches': 176, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '835e29ace60a9700f5989f01a4aa8ff703a7a15ee1bb5e477446b1fa6f2cfecf', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 114, 'tuning_matches': 22, 'audit_matches': 40, 'tuning_origin_utc': '2026-09-13T00:00:00+00:00', 'audit_origin_utc': '2026-10-09T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 17, 'selected_ridge': 1.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8357146014438204, 'audit_candidate_poisson_score': 0.8437651841527154, 'audit_gain': -0.008050582708895027, 'audit_gain_lower95': -0.03725049821585039, 'audit_baseline_briers': [0.5199253099278909, 0.20340070445316755, 0.22970209423243637, 0.28429820925953975], 'audit_candidate_briers': [0.5207453946703196, 0.21314479122702693, 0.23282815042185553, 0.28812038229266573], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2009, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1630, 'tuning_matches': 230, 'audit_matches': 129, 'audit_matchdays': 56, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8432834464502666, 'audit_candidate_poisson_score': 0.8400225074412011, 'audit_gain': 0.0032609390090655443, 'audit_gain_lower95': -0.005259240284233485, 'audit_baseline_briers': [0.5723880944925321, 0.1848831628824439, 0.20353795326472862, 0.2524151023574783], 'audit_candidate_briers': [0.574670571206337, 0.1816626862987799, 0.20413573167809032, 0.24863999990406543], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1847.130 |
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
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261105T122642954541Z_f35f2cbe427ac3bf7d89db7a2f0903533137131be497d8a163662758d57b1d84.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3, 'ANCHORED_MAIN': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 5} |
| Legacy comparison status | {'None': 5} |
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
| Market best home last update utc | 2026-11-05T12:27:26Z |
| Market best draw last update utc | 2026-11-05T12:27:25Z |
| Market best away last update utc | 2026-11-05T12:27:25Z |
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
| Dc lambda home | 1.5210 |
| Dc lambda away | 1.0533 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:26:42.954541+00:00 |
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
| Score matrix json | [[0.09243028277117285,0.07873362360671467,0.03977145466277652,0.0130043434305737,0.0031890890620085367,0.0006256549036692929,0.00010228732272084795,1.4333821127322168e-05,1.7575601727981033e-06,1.9156047371798946e-07,1.8790749866262536e-08,1.675674402321733e-09,1.369766682560406e-10,1.033573712844056e-11,7.241885078095472e-13],[0.13346453311117074,0.1274350863579493,0.05633705977934033,0.018420912170582303,0.004517408343531597,0.0008862526655894177,0.0001448920353468105,2.030414387814965e-05,2.4896190838447444e-06,2.713492365495418e-07,2.6617472443246052e-08,2.3736262546781942e-09,1.9403018605547525e-10,1.464077805063248e-11,1.0258274836037766e-12],[0.09646821570004771,0.09462860871459783,0.04337840663788102,0.013046794980765022,0.003199499566399105,0.0006276972997877404,0.00010262123080606593,1.4380612642039419e-05,1.7632975754042506e-06,1.9218580625462436e-07,1.8852090637931546e-08,1.6811444959388571e-09,1.3742381669829412e-10,1.0369477245026587e-11,7.265525583247756e-13],[0.04554971801409821,0.044681104669941935,0.02191452770254687,0.006697180390236752,0.001510718343634054,0.00029638192015951544,4.845500760592673e-05,6.790141664396387e-06,8.325820764047466e-07,9.074501085859644e-08,8.901454290437116e-09,7.937915838421625e-10,6.488786025121147e-11,4.896190533192742e-12,3.430587361231644e-13],[0.016130521302594448,0.01582291926546891,0.007760591532812959,0.0025375334740159227,0.0005816114195712417,0.0001049577271885019,1.7159371484206785e-05,2.4045928172657307e-06,2.9484228454385464e-07,3.213553002250641e-08,3.152271941870755e-09,2.8110540770028704e-10,2.297873746963656e-11,1.7338879172156912e-12,1.2148738767961366e-13],[0.004569841111427656,0.004482696225726466,0.002198606577577989,0.000718893368270539,0.00017629609597298286,3.2326138336670795e-05,4.861318477176253e-06,6.812307492391561e-07,8.35299968314752e-08,9.104124006875545e-09,8.93051231521196e-10,7.963828475566916e-11,6.509968103793301e-12,4.912173722138477e-13,3.441786215854987e-14],[0.0010788785326038732,0.0010583047874524012,0.0005190616873437693,0.00016972113545017138,4.162115677315151e-05,8.165491877203944e-06,1.247705924100117e-06,1.6082949345128733e-07,1.9720318105719502e-08,2.149362244700239e-09,2.1083748399792102e-10,1.8801536793353327e-11,1.5369166375511793e-12,1.1596986958656895e-13,8.125598180672437e-15],[0.00021832185528653354,0.00021415855230485218,0.0001050373208516314,3.434476825059171e-05,8.422457108266952e-06,1.6523689016739682e-06,2.7014315736707864e-07,3.538156737130746e-08,3.9906034883188144e-09,4.3494493473073654e-10,4.2665072368505194e-11,3.8046789058412535e-12,3.1101044426297235e-13,2.3467662318176136e-14,1.6442960134128811e-15],[3.865715849691299e-05,3.791998326989643e-05,1.859843282718326e-05,6.081256262962702e-06,1.4913223366502318e-06,2.9257669344897967e-07,4.783289715768464e-08,6.702963511235841e-09,7.68171171538139e-10,7.70135232556017e-11,7.554490880754714e-12,6.736754563574783e-13,5.5069063160396435e-14,4.155301541364854e-15,2.9114726751895934e-16],[6.08429300083556e-06,5.968268175201148e-06,2.9272279463059297e-06,9.571356601387572e-07,2.3472087467565224e-07,4.6048969902984256e-08,7.528472673681598e-09,1.0549868526815063e-09,1.2935858893650335e-10,1.3177526447194267e-11,1.1890096887054558e-12,1.06030526384339e-13,8.667380857186587e-15,6.540075129036275e-16,4.58239909723179e-17],[8.618522541090405e-07,8.454171058523912e-07,4.1464768436830384e-07,1.3558017769122019e-07,3.3248680643400184e-08,6.522928548121539e-09,1.0664231888437558e-09,1.4944099452707018e-10,1.832390245637077e-11,1.9971637325602027e-12,1.8310272483179812e-13,1.501943580891996e-14,1.2277518074757324e-15,9.264147027811307e-17,6.4910598333020515e-18],[1.1098462994808964e-07,1.0886820124617497e-07,5.339606596031033e-08,1.745927538927402e-08,4.281583647170126e-09,8.399871412293204e-10,1.3732815853018768e-10,1.9244195739566952e-11,2.359652160366576e-12,2.571838464738715e-13,2.522794621947079e-14,2.1026662686168407e-15,1.5810317762834638e-16,1.1929862975519333e-17,8.358832620501464e-19],[1.3100995393532615e-08,1.2851165100027173e-08,6.303049480869404e-09,2.060951021382699e-09,5.054123950752147e-10,9.915488003175864e-11,1.621067325401551e-11,2.2716489648542216e-12,2.7854120068482434e-13,3.0358837881615925e-14,2.97799080254774e-15,2.6556380100286746e-16,2.028937954508649e-17,1.4082407623547184e-18,9.867044446399474e-20],[1.4275247389450966e-09,1.4003024620261235e-09,6.867996510538367e-10,2.2456755997565904e-10,5.507128852938375e-11,1.0804220593982016e-11,1.7663647997683071e-12,2.4752585571698366e-13,3.0350705640988724e-14,3.3079923181275486e-15,3.2449103410008605e-16,2.8936648270789434e-17,2.3654032460827826e-18,1.668180239894214e-19,1.07514350050527e-20],[1.444369500622681e-10,1.4168260014127653e-10,6.949038723864906e-11,2.2721745242593067e-11,5.5721128567350764e-12,1.093171016810468e-12,1.7872078669853125e-13,2.504466555706337e-14,3.0708843324575746e-15,3.3470265574019692e-16,3.283200214281571e-17,2.927810010736477e-18,2.3933149542757305e-19,1.8059042133161837e-20,1.1826270598953372e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.14973818065443442, "-10": 2.1306817615559898e-08, "-11": 1.880417124358358e-09, "-12": 1.5234399886499784e-10, "-13": 1.1361564612044336e-11, "-14": 7.241885078095472e-13, "-2": 0.06170610908507569, "-3": 0.018200394397022812, "-4": 0.00418505726117486, "-5": 0.0007857931814325501, "-6": 0.00012444874265616252, "-7": 1.7024815204701945e-05, "-8": 2.0485787696498586e-06, "-9": 2.1992574682320494e-07, "0": 0.2705561775841732, "1": 0.25272994156768364, "10": 9.772536445089174e-07, "11": 1.2454531644441324e-07, "12": 1.4570788242797387e-08, "13": 1.5692073390863732e-09, "14": 1.444369500622681e-10, "2": 0.14967212770321606, "3": 0.063749687706701, "4": 0.02116816244117109, "5": 0.0057395058594283685, "6": 0.001312626758525102, "7": 0.0002593090292103638, "8": 4.5058050027208173e-05, "9": 6.9852232881291906e-06} |
| Raw goal margin distribution | {"-1": 0.16171634714104546, "-10": 4.078841464061219e-08, "-11": 3.859216678260589e-09, "-12": 3.3531908248886846e-10, "-13": 2.6927781478169466e-11, "-14": 2.0010424208424908e-12, "-15": 1.2695127351180636e-13, "-2": 0.06988437726429812, "-3": 0.021828017730348776, "-4": 0.0053408658596412716, "-5": 0.0010699861477570665, "-6": 0.00018111150907968528, "-7": 2.6509318281850267e-05, "-8": 3.4155140485114557e-06, "-9": 3.928262368842812e-07, "0": 0.26183851433770144, "1": 0.23463953647031854, "10": 1.6083543983656102e-06, "11": 2.19749846855778e-07, "12": 2.7572248232737592e-08, "13": 3.197414775111567e-09, "14": 3.431145944399145e-10, "15": 3.1434347518557785e-11, "2": 0.1457300401832499, "3": 0.06573062708021311, "4": 0.023224674750726232, "5": 0.006718937759199311, "6": 0.0016423019350248762, "7": 0.0003471282887499868, "8": 6.458505242107495e-05, "9": 1.0726571194467247e-05} |
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
| Totals anchor reference last update utc | 2026-11-05T12:27:47Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4730 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.99, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.47, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.2, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.2, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.26, "draw": 3.5, "home": 1.95}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.17, "draw": 3.47, "home": 2.05}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.28, "under": 1.73}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.86, "home_away": 1.35, "home_draw": 1.27}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:31Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.93, "home_away": 1.33, "home_draw": 1.26}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.22, "under": 1.71}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:47Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.39, "under": 3.12}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.95 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.26 |
| Market reference 1x2 last update utc | 2026-11-05T12:27:25Z |
| Market reference home last update utc | 2026-11-05T12:27:25Z |
| Market reference draw last update utc | 2026-11-05T12:27:25Z |
| Market reference away last update utc | 2026-11-05T12:27:25Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.28 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-11-05T12:27:26Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:27:26Z |
| Market best over 2 5 last update utc | 2026-11-05T12:27:26Z |
| Market best under 2 5 last update utc | 2026-11-05T12:27:26Z |
| Home probability edge | -0.7% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | -0.0237 |
| Raw ev home | -0.0199 |
| Raw edge prob draw | -0.0125 |
| Raw ev draw | -0.0836 |
| Raw edge prob away | 0.0361 |
| Raw ev away | 0.1078 |
| Market p home draw | 75.4% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T12:27:26Z |
| Market reference home draw last update utc | 2026-11-05T12:27:48Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.8% |
| Market draw away odds | 1.93 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-05T12:27:31Z |
| Market reference draw away last update utc | 2026-11-05T12:27:48Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.8% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T12:27:26Z |
| Market reference home away last update utc | 2026-11-05T12:27:48Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home draw odds | 1.25 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 70.4% |
| Market over 1 5 odds | 1.39 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T12:27:47Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 2.90 |
| Market reference over 1 5 last update utc | 2026-11-05T12:27:48Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 78.9% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 3.70 |
| Market reference under 3 5 last update utc | 2026-11-05T12:27:25Z |
| Market under 3 5 bookmakers | 0 |
| Count model | {"corners": {"alpha": 0.014493407444055235, "mu": 8.663289582047497, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,445.5951 |
| Elo away rating | 1,433.5816 |
| Elo rating diff | 72.0135 |
| Elo home expectancy | 0.6022 |

</details>


---

## 2026-11-07 — CA Osasuna vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **43.5%**. Expected goals are 1.12 for CA Osasuna and 1.19 for Athletic Bilbao (2.32 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.5%; Double Chance 1X: 56.5%; Double Chance X2: 71.0%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 46.9%; BTTS No (at least one team does not score): 53.1%.

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
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
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
| Over 2.5 | 41.3% | 45.3% | 2.17 | -10.5% |
| Under 2.5 | 58.7% | 54.7% | 1.81 | +6.3% |

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
| Market best home last update utc | 2026-11-05T12:27:26Z |
| Market best draw last update utc | 2026-11-05T12:27:25Z |
| Market best away last update utc | 2026-11-05T12:27:26Z |
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
| Dc lambda home | 1.1204 |
| Dc lambda away | 1.1947 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:26:42.954541+00:00 |
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
| Score matrix json | [[0.0968901899085237,0.13405561223250773,0.08195799663375568,0.03263704132586218,0.00974746068342153,0.0023289608595631747,0.0004637155307708726,7.913968250020715e-05,1.1818028110562082e-05,1.5687119731106967e-06,1.8740618218223472e-07,2.0353163917063884e-08,2.0262423410666687e-09,1.8620388417830827e-10],[0.0925924937941747,0.12881521059447243,0.0918295754702351,0.03656806867731638,0.010921511179334317,0.0026094767540034702,0.0005195685848683321,8.867180440389192e-05,1.324147183755399e-05,1.7576583181939218e-06,2.099786580581714e-07,2.280463748195496e-08,2.2702967571480644e-09,2.086315471010473e-10],[0.05317525876324298,0.06352582502198174,0.042239888167127725,0.02048628785675629,0.006118486153178061,0.0014618899458365457,0.00029107448043989224,4.9676019967741744e-05,7.41818240676008e-06,9.846813234268224e-07,1.1763495826684129e-07,1.2775691602605805e-08,1.2718733739429417e-09,1.1688027518291473e-10],[0.01986001626161979,0.02372576922637298,0.014171995580662131,0.006282206312420244,0.0022851460871988636,0.0005459899730113063,0.00010871115720596527,1.8553112618868106e-05,2.77055959211908e-06,3.677610142498786e-07,4.393457104771697e-08,4.7714942791510505e-09,4.750221527213035e-10,4.3652710297666216e-11],[0.005563022941758238,0.00664586558130087,0.00396974179210917,0.0015808173972459893,0.0005255622422000421,0.00015293818020187917,3.0451267189070606e-05,5.1969439390262415e-06,7.760661607439048e-07,1.0301416335242678e-07,1.2306587439562483e-08,1.3365513800047892e-09,1.3305926332693088e-10,1.2227634945352105e-11],[0.0012466142562163021,0.0014892677713689993,0.000889576901506873,0.00035424436039782967,0.00010579950985218275,2.813948162182382e-05,6.823805005871368e-06,1.1645798464205883e-06,1.7390817005055032e-07,2.3084378039027524e-08,2.757775315354398e-09,2.995069446815795e-10,2.981716529332977e-11,2.7400829013778723e-12],[0.00023279416006844538,0.0002781075526964746,0.00016612059951177908,6.615199363121e-05,1.9757120463588368e-05,4.7205689514225745e-06,1.0462742489599463e-06,2.174749613428772e-07,3.2475808915290976e-08,4.310802936434126e-09,5.149900901534576e-10,5.5930266539256386e-11,5.568091264374498e-12,5.116861887014164e-13],[3.726192469499097e-05,4.4514959836782105e-05,2.658989928044033e-05,1.0588541415235386e-05,3.1624003569833676e-06,7.555923427533734e-07,1.5044473711421916e-07,2.8581262002336918e-08,5.1982023340048395e-09,6.900036252847872e-10,8.243128587213147e-11,8.95241263502398e-12,8.912500095662095e-13,8.190245075414811e-14],[5.218750558953369e-06,6.234580565324971e-06,3.7240709616636013e-06,1.4829871747523786e-06,4.429126720032217e-07,1.058251282874589e-07,2.1070665628068524e-08,3.5960102201047802e-09,5.977689762097308e-10,9.663904467121907e-11,1.154498386065012e-11,1.2538377667134595e-12,1.2482477820626646e-13,1.1470917408362411e-14],[6.497035988586154e-07,7.761684305290839e-07,4.636248233874107e-07,1.8462313797404855e-07,5.514000980309162e-08,1.3174602986164886e-08,2.623173331290266e-09,4.476820179738567e-10,6.685291759913684e-11,9.87825646606141e-12,1.4372822533471153e-12,1.5609539107421108e-13,1.5539947102511903e-14,1.428061417811403e-15],[7.279583215202449e-08,8.696554381068014e-08,5.194669520703457e-08,2.068604050670125e-08,6.1781447810024165e-09,1.4761441822629085e-09,2.9391261779331447e-10,5.016038866824316e-11,7.490513792704004e-12,9.942825115523203e-13,1.3222459395047053e-13,1.7489658220002655e-14,1.741168408045051e-15,1.600066852891229e-16],[7.414896140913365e-09,8.858205973215336e-09,5.291228061236353e-09,2.107055272114929e-09,6.292984164119465e-10,1.5035827569955952e-10,2.993758668614634e-11,5.109277019955421e-12,7.629747496943014e-13,1.0127642393716236e-13,1.2098988393322964e-14,1.4627119729152316e-15,1.773533254284595e-16,1.6298089027857364e-17],[6.923330575240838e-10,8.270957150397574e-10,4.940449646327414e-10,1.9673694562846251e-10,5.875795000358286e-11,1.4039037467394982e-11,2.7952894459232282e-12,4.770560927273554e-13,7.123938504747023e-14,9.4562371349525e-15,1.1296894073914667e-15,1.2268940872852852e-16,1.3596535745346644e-17,1.5217618148682915e-18],[5.967095094459025e-11,7.128590394790055e-11,4.2580854010422035e-11,1.6956406319188547e-11,5.0642428729419915e-12,1.2099995904024112e-12,2.409210098967627e-13,4.1116613453000797e-14,6.1399954895877496e-15,8.150162065322649e-16,9.736591439407683e-17,1.0574381231833834e-17,1.052723747021901e-18,1.0768953675308246e-19]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2488166064031634, "-10": 2.1152634574843028e-07, "-11": 2.2740340949394864e-08, "-12": 2.234873888167716e-09, "-13": 1.8620388417830827e-10, "-2": 0.12522219046181232, "-3": 0.04513452885485184, "-4": 0.0126673647050913, "-5": 0.002901081852763023, "-6": 0.0005601858903401525, "-7": 9.341113711246718e-05, "-8": 1.3698228680648224e-05, "-9": 1.7919535725591407e-06, "0": 0.2747822721696579, "1": 0.17198180598147492, "10": 8.216503949619176e-08, "11": 8.284572709963545e-09, "12": 7.636189614719844e-10, "13": 5.967095094459025e-11, "2": 0.08124554838086986, "3": 0.027464881637650262, "4": 0.0072294562404231905, "5": 0.0015528513419427376, "6": 0.00028122414534432783, "7": 4.398145970258494e-05, "8": 6.049032707911197e-06, "9": 7.421621719190334e-07} |
| Raw goal margin distribution | {"-1": 0.21394672947302207, "-10": 1.8188243350979564e-07, "-11": 1.9553443974479886e-08, "-12": 1.921672215010406e-09, "-13": 1.601087347464762e-10, "-2": 0.10767319148844394, "-3": 0.03880924579107405, "-4": 0.010892123676443731, "-5": 0.0024945158737776797, "-6": 0.0004816798238177597, "-7": 8.032023091411434e-05, "-8": 1.1778519400950153e-05, "-9": 1.5408240300300617e-06, "0": 0.28776373624815527, "1": 0.20048948380123457, "10": 9.578470385916262e-08, "11": 9.6578222135503e-09, "12": 8.901963235741573e-10, "13": 6.956199863431095e-11, "2": 0.09471279803738887, "3": 0.032017456211546204, "4": 0.008427809799614418, "5": 0.0018102517425575173, "6": 0.00032783981660595497, "7": 5.127181972694176e-05, "8": 7.051719443140013e-06, "9": 8.651828598711057e-07} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.12, "draw": 3.58, "home": 3.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.18, "draw": 3.54, "home": 3.65}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.17, "under": 1.81}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.58 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.12 |
| Market reference 1x2 last update utc | 2026-11-05T12:27:25Z |
| Market reference home last update utc | 2026-11-05T12:27:25Z |
| Market reference draw last update utc | 2026-11-05T12:27:25Z |
| Market reference away last update utc | 2026-11-05T12:27:25Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.18 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-11-05T12:27:25Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:27:25Z |
| Market best over 2 5 last update utc | 2026-11-05T12:27:26Z |
| Market best under 2 5 last update utc | 2026-11-05T12:27:26Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.6% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | 0.0686 |
| Raw ev home | 0.2331 |
| Raw edge prob draw | 0.0185 |
| Raw ev draw | 0.0302 |
| Raw edge prob away | -0.0872 |
| Raw ev away | -0.1838 |
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
| Market best home last update utc | 2026-11-05T12:27:25Z |
| Market best draw last update utc | 2026-11-05T12:27:26Z |
| Market best away last update utc | 2026-11-05T12:27:26Z |
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
| Dc lambda away | 1.1382 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:26:42.954541+00:00 |
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
| Score matrix json | [[0.08566026866850229,0.08558446052844815,0.05232475556857073,0.020737706191280247,0.006164182518429822,0.0014658186694338567,0.0002904716569251519,4.933788015213814e-05,7.332722711108588e-06,9.687183278911568e-07,1.1517872858243228e-07,1.244957020755197e-08,1.2335247741080885e-09,1.128182315080117e-10,9.581334791904872e-12],[0.1061996065411211,0.135569581912446,0.07049134383654777,0.027937613116895285,0.008304319908545781,0.001974735031369309,0.000391320269356051,6.646745763414096e-05,9.878564596626502e-06,1.3050468366288524e-06,1.5516753534606948e-07,1.677192610996002e-08,1.6617912121653956e-09,1.5198749926008936e-10,1.2907870431313186e-11],[0.07332335325130193,0.08718004356612537,0.05319726066468601,0.018818624863088933,0.005593744907559627,0.0013301708203864264,0.000263591213734755,4.477211942145901e-05,6.654147602082794e-06,8.790724799760041e-07,1.0452001129766804e-07,1.129747857750632e-08,1.1193735589246267e-09,1.0237795621577006e-10,8.694671603185093e-12],[0.032926809048110635,0.03914933673954425,0.02327390068237078,0.009467822455988243,0.0025119441796913012,0.0005973305728956804,0.00011836907583396545,2.0105504747130622e-05,2.988131853719239e-06,3.947589738349153e-07,4.6936075630768765e-08,5.073280249087164e-09,5.026693105795835e-10,4.5974157830713184e-11,3.904455796407841e-12],[0.01108966010844052,0.013185390581822583,0.007838586714794451,0.003106642476967813,0.0009478365855248199,0.00020117931914125908,3.9866384150097875e-05,6.771479545088494e-06,1.0063947152769152e-06,1.3295375322247243e-07,1.580794315078492e-08,1.708667047421329e-09,1.6929766237374195e-10,1.5483971840984185e-11,1.3150101374028505e-12],[0.0029879739914316097,0.003552643069318872,0.002112011820412845,0.0008370470177703091,0.0002488081635669572,6.0729094372309766e-05,1.0741512166116785e-05,1.8244927767295502e-06,2.711608115088131e-07,3.582277119472774e-08,4.259257951163395e-09,4.60379547054407e-10,4.561519532937667e-11,4.17196782340575e-12,3.543134821632662e-13],[0.0006708943651239973,0.000797680375845871,0.00047421324062843164,0.00018794344568470796,5.586527707824664e-05,1.328454598311413e-05,2.702076555474158e-06,4.0965615049775683e-07,6.088415126951982e-08,8.043341543998567e-09,9.563376947856233e-10,1.0336972303736644e-10,1.0242049495165341e-11,9.367383090441498e-13,7.955454744668183e-14],[0.0001291173743563405,0.00015351805151286654,9.126499147691898e-05,3.6170767703210486e-05,1.0751585151113159e-05,2.5566852041434926e-06,5.066415123300431e-07,8.832932561986494e-08,1.171749557082912e-08,1.5479860842480357e-09,1.840525402622706e-10,1.989408157282714e-11,1.971139731661057e-12,1.8028052881383876e-13,1.5310717779726735e-14],[2.1743190990872052e-05,2.5852231980636427e-05,1.5368900973670652e-05,6.091108298770571e-06,1.8105523796518992e-06,4.3054232611491157e-07,8.531774458249297e-08,1.4491591715423167e-08,2.2106922364257575e-09,2.6067876030476584e-10,3.099419853623441e-11,3.3501363963007756e-12,3.3193726149449086e-13,3.035899691637602e-14,2.5783041403334674e-15],[3.2546879273206777e-06,3.869760761288161e-06,2.3005352101350737e-06,9.11763901275296e-07,2.710173945631344e-07,6.444688415766724e-08,1.2771015689253808e-08,2.1692128181023934e-09,3.223939911378206e-10,4.371662362098741e-11,4.63944983214336e-12,5.014741621179324e-13,4.968692029001381e-14,4.544367972059644e-15,3.8594037839372783e-16],[4.3846803157018503e-07,5.213299774170273e-07,3.0992561120175307e-07,1.2283184501133957e-07,3.6511169786162234e-08,8.682214414549584e-09,1.7204973980497213e-09,2.9223400081652665e-10,4.3432569217358336e-11,5.737831292122514e-12,7.00244905625709e-13,6.755805584351905e-14,6.693768072652609e-15,6.122123300097467e-16,5.1993469664865065e-17],[5.369994381313011e-08,6.384819069965327e-08,3.79571296182858e-08,1.5043430080754287e-08,4.471586580776135e-09,1.063325927240904e-09,2.1071231413393873e-10,3.579040726854393e-11,5.319262428961584e-12,7.027221959438979e-13,8.35523048806888e-14,9.269748108854792e-15,8.197974390797332e-16,7.497871077510126e-17,6.3677308232812866e-18],[6.0286652117816755e-09,7.167965900405389e-09,4.261286150785438e-09,1.6888621691916634e-09,5.020060831870638e-10,1.1937509746100188e-10,2.3655778902373555e-11,4.018037411104544e-12,5.97171059794984e-13,7.889164411374949e-14,9.380063330256665e-15,1.013883018319111e-15,1.031118992427637e-16,8.41754223890956e-18,7.148781649734119e-19],[6.24750189320736e-10,7.428158466274143e-10,4.415968105593726e-10,1.7501667829839526e-10,5.202285821053105e-11,1.2370833695192273e-11,2.45144685077307e-12,4.163889592640845e-13,6.188479863414443e-14,8.175536020737658e-15,9.720553614365418e-16,1.050686321751719e-16,1.0410380327114095e-17,9.772944379091027e-19,7.408277839605027e-20],[6.011833476855243e-11,7.147953294337706e-11,4.2493888507337576e-11,1.684146949593209e-11,5.006045070459393e-12,1.1904180809649147e-12,2.3589733138348557e-13,4.0068192494962284e-14,5.955037877486671e-15,7.867138254755104e-16,9.35387465763648e-17,1.0110523071067172e-17,1.0017679710571398e-18,9.162174384195408e-20,7.986798010743934e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1776187158781162, "-10": 1.3311731741928501e-07, "-11": 1.4217643831729542e-08, "-12": 1.3942069449713628e-09, "-13": 1.2572610193932488e-10, "-14": 9.581334791904872e-12, "-2": 0.08649519750648793, "-3": 0.03049761686719754, "-4": 0.0084236574623358, "-5": 0.0019050365084478673, "-6": 0.0003640042998828167, "-7": 6.01442085386632e-05, "-8": 8.747536388468941e-06, "-9": 1.1357018494106357e-06, "0": 0.28490629204251927, "1": 0.22002280743745556, "10": 5.067575311439926e-07, "11": 6.13263479935908e-08, "12": 6.813974946916428e-09, "13": 6.96229722264113e-10, "14": 6.011833476855243e-11, "2": 0.12120683321679551, "3": 0.04842335009215682, "4": 0.015154563942248091, "5": 0.003883290381455171, "6": 0.0008407306800856461, "7": 0.0001573975668453166, "8": 2.5938435406256932e-05, "9": 3.815717109801474e-06} |
| Raw goal margin distribution | {"-1": 0.1918730151825498, "-10": 1.0127931158630961e-07, "-11": 1.0364988340607438e-08, "-12": 9.738220608899592e-10, "-13": 8.419290756975815e-11, "-14": 6.195113294946028e-12, "-2": 0.09077404159958778, "-3": 0.030905657466713924, "-4": 0.008217996521871244, "-5": 0.0017861608481178645, "-6": 0.00032765750394297787, "-7": 5.194040333627013e-05, "-8": 7.2441889233327744e-06, "-9": 9.015997633725035e-07, "0": 0.27908057525665364, "1": 0.21775749759345642, "10": 3.532310900899713e-07, "11": 4.096008194851641e-08, "12": 4.3603909123202724e-09, "13": 4.27144819092688e-10, "14": 3.561252001182267e-11, "2": 0.11653846903374793, "3": 0.044957219282718126, "4": 0.013545069116961524, "5": 0.003335720515843165, "6": 0.0006933348448722272, "7": 0.0001245323100848137, "8": 1.9679783327430734e-05, "9": 2.7752246980183083e-06} |
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
| Totals anchor reference last update utc | 2026-11-05T12:27:25Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4358 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.25, "draw": 3.36, "home": 2.35}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.1, "under": 1.81}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.41, "draw": 3.43, "home": 2.32}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.1, "under": 1.86}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.35 |
| Reference draw odds | 3.36 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-11-05T12:27:25Z |
| Market reference home last update utc | 2026-11-05T12:27:25Z |
| Market reference draw last update utc | 2026-11-05T12:27:25Z |
| Market reference away last update utc | 2026-11-05T12:27:25Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-11-05T12:27:25Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:27:25Z |
| Market best over 2 5 last update utc | 2026-11-05T12:27:25Z |
| Market best under 2 5 last update utc | 2026-11-05T12:27:26Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0182 |
| Raw ev home | -0.0671 |
| Raw edge prob draw | -0.0083 |
| Raw ev draw | -0.0428 |
| Raw edge prob away | 0.0265 |
| Raw ev away | 0.1047 |
| Count model | {"corners": {"alpha": 0.014493407444055235, "mu": 9.554886460393718, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,436.9009 |
| Elo away rating | 1,445.5717 |
| Elo rating diff | 51.3291 |
| Elo home expectancy | 0.5733 |

</details>


---

## 2026-11-07 — Málaga vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **Málaga win** at **39.9%**. Expected goals are 1.69 for Málaga and 1.59 for Real Racing Club de Santander (3.28 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 62.9%; Under 3.5 goals: 58.5%; Double Chance 1X: 65.8%; Double Chance X2: 60.1%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 77.0%; BTTS Yes (both teams score): 65.7%; BTTS No (at least one team does not score): 34.3%.

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
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.9% |
| Under 2.5 | 37.1% |
| Over 3.5 | 41.5% |
| Under 3.5 | 58.5% |
| Over 4.5 | 23.0% |
| Under 4.5 | 77.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.37% |
| 2 | 2-1 | 8.43% |
| 3 | 1-2 | 7.62% |
| 4 | 2-2 | 7.49% |
| 5 | 1-0 | 6.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Málaga win | 39.9% | 39.6% | 2.48 | -1.1% |
| Draw | 25.9% | 26.9% | 3.72 | -3.7% |
| Real Racing Club de Santander win | 34.2% | 33.4% | 2.92 | -0.0% |
| Over 2.5 | 62.9% | 57.0% | 1.73 | +8.9% |
| Under 2.5 | 37.1% | 43.0% | 2.28 | -15.5% |

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
| Market best home last update utc | 2026-11-05T12:27:26Z |
| Market best draw last update utc | 2026-11-05T12:27:26Z |
| Market best away last update utc | 2026-11-05T12:27:26Z |
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
| Dc lambda home | 1.6927 |
| Dc lambda away | 1.5891 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:26:42.954541+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 65.7% |
| P btts no | 34.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.88 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.29 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.70 |
| Fair Over 3.5 odds | 2.41 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.35 |
| Fair Under 4.5 odds | 1.30 |
| Score matrix json | [[0.043711471631498,0.054680157475493305,0.04500877323748003,0.02384125787357031,0.009471579696168294,0.0030102714350594135,0.0007972740911424165,0.00018099344863167628,3.595225307091866e-05,6.347998956240999e-06,1.0087651976095307e-06,1.45730565278476e-07,1.9298459705474084e-08,2.3590249768893623e-09,2.6776742824018015e-10,2.8367413051377368e-11],[0.06062159666809901,0.11371940520701566,0.0761880888262625,0.04035701801996291,0.01603290877112333,0.0050956027233926915,0.0013495766470758633,0.00030637460098198823,6.085776735168754e-05,1.074550301105228e-05,1.7075758113824165e-06,2.4668375637690706e-07,3.2667248105005844e-08,3.9932126906527835e-09,4.532602677238603e-10,4.801861570245773e-11],[0.053036679030660235,0.08428097794552632,0.07493787854638825,0.034156941552759376,0.013569761956770215,0.004312761768297906,0.0011422402575020979,0.0002593060600715158,5.1508146648366514e-05,9.094663984389448e-06,1.4452397636872894e-06,2.0878556102468177e-07,2.7648556284813425e-08,3.3797326753650335e-09,3.83625580690171e-10,4.0641482707714934e-11],[0.029925745007664876,0.047555222180038714,0.037785177211354465,0.02239762826473418,0.007656686722376816,0.0024334594721188815,0.0006445047334833424,0.000146312461007531,2.906327640773544e-05,5.131629662745195e-06,8.154710557582449e-07,1.1780646101342254e-07,1.560059302979885e-08,1.9070013448349194e-09,2.1645927904940527e-10,2.293180248977135e-11],[0.012664116098022461,0.020124640325612956,0.01599010720924018,0.008469999113063476,0.003765522068532536,0.001029802708900068,0.00027274451374452067,6.191718843798774e-05,1.2299132620498087e-05,2.1716269320752334e-06,3.4509483797493603e-07,4.9853886644727354e-08,6.601931590233412e-09,8.07013707558115e-10,9.160224548039788e-11,9.704386941511466e-12],[0.0042874076886804625,0.0068131511900333215,0.005413414411324488,0.0028674989268406685,0.0011391909251716498,0.00040516165461125726,9.233703451725873e-05,2.0961923257475403e-05,4.163843362858806e-06,7.351993564697977e-07,1.1683107215739419e-07,1.6877919884561468e-08,2.2350689176427482e-09,2.7321265439089565e-10,3.101173177292492e-11,3.285398117399093e-12],[0.0012095767644235557,0.0019221473604497236,0.0015272492759252816,0.0008089876974082312,0.00032139207964006103,0.00010214530498922016,3.027394257461576e-05,5.913842851197459e-06,1.1747164133027278e-06,2.074167243653734e-07,3.2960744698335126e-08,4.7616511436660294e-09,6.305645802715878e-10,7.70796020565565e-11,8.749126022258566e-12,9.268867141276917e-13],[0.00029249961520627274,0.00046481329654942245,0.00036931911944017504,0.00019562924583069814,7.77189694693435e-05,2.470075755689048e-05,6.542026012119517e-06,1.661942715541637e-06,2.840696919565011e-07,5.015747147981158e-08,7.970560798404395e-09,1.1514615427757294e-09,1.5248300274686764e-10,1.8639374205026144e-11,2.1157119334393045e-12,2.2413956285888177e-13],[6.189067447861973e-05,9.835092743553636e-05,7.814509220425178e-05,4.1393647522124876e-05,1.644473766862504e-05,5.226490791280981e-06,1.3842425128020092e-06,3.142442842656721e-07,6.985206087492847e-08,1.0612936149808305e-08,1.6865095136559841e-09,2.436404282731296e-10,3.226423350975566e-11,3.943948577829496e-12,4.4766841307015503e-13,4.7426211870044474e-14],[1.16405261204789e-05,1.84980459403812e-05,1.4697690640050552e-05,7.785402877935114e-06,3.092960288260898e-06,9.830092027089751e-07,2.603511960903822e-07,5.9103715220770564e-08,1.1740268739631954e-08,2.319729537392406e-09,3.17202199063617e-10,4.58243958917877e-11,6.068323799852655e-12,7.417860093592847e-13,8.419840144829352e-14,8.920020063108727e-15],[1.9704368154450278e-06,3.131235681057087e-06,2.4879348613141498e-06,1.3178652145942607e-06,5.23557333888617e-07,1.6639776440442718e-07,4.407065251278618e-08,1.0004714150823427e-08,1.9873206338235057e-09,3.508962090454449e-10,6.23994123865797e-11,7.756872479488204e-12,1.0272086071981604e-12,1.2556498279335948e-13,1.425258861139104e-14,1.5099262477437416e-15],[3.03221318308452e-07,4.818512340524638e-07,3.828566755350895e-07,2.0280012258696607e-07,8.056779275914508e-08,2.560617477850674e-08,6.781826876606859e-09,1.5395787321537377e-09,3.058194902603125e-10,5.399777869668327e-11,8.580826851567527e-12,1.387197435196449e-12,1.5807233483001506e-13,1.9322608732004154e-14,2.1932642925563472e-15,2.3235549792850724e-16],[4.277286973106401e-08,6.797068286245221e-08,5.40063568079084e-08,2.8607300018503755e-08,1.1365017880110633e-08,3.612046752589416e-09,9.566550239605904e-10,2.1717536523649148e-10,4.313937189870772e-11,7.617010462340166e-12,1.2104247523043747e-12,1.7486317311340728e-13,2.5913073840295737e-14,2.7256771745764687e-15,3.0938526484432865e-16,3.277642713129622e-17],[5.569483738767867e-09,8.850507700222018e-09,7.032203542174132e-09,3.7249755105254877e-09,1.4798465165434587e-09,4.703270035118965e-10,1.245666852156415e-10,2.8278548359058696e-11,5.617206229116283e-12,9.918159846361323e-13,1.576102098678063e-13,2.2769049757191628e-14,3.015205413026668e-15,4.1245386296710547e-16,4.0285260549479955e-17,4.2678403172487626e-18],[6.734057309969718e-10,1.0701140154295271e-09,8.502630385424026e-10,4.50386422560266e-10,1.789280967461328e-10,5.686719172962554e-11,1.5061345656081642e-11,3.419156500397288e-12,6.791758526106461e-13,1.1992037313967166e-13,1.9056634971358505e-14,2.75300356640239e-15,3.6456818989015423e-16,4.456446156095391e-17,5.6605997993629776e-18,5.160241529408005e-19],[7.599332598055647e-11,1.2076155498484164e-10,9.595153899493885e-11,5.082576617838861e-11,2.0191900005036578e-11,6.417419454257171e-12,1.6996614336114064e-12,3.8584921771982684e-13,7.66444798281577e-14,1.3532923152021727e-14,2.1505268025071665e-15,3.1067436437987805e-16,4.114124371268305e-17,5.0290656860548424e-18,5.708375275371232e-19,6.767419228879225e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17381022317090852, "-10": 1.2850993992596838e-06, "-11": 1.820037097248378e-07, "-12": 2.3698229779306812e-08, "-13": 2.8529267273209375e-09, "-14": 3.157860439426379e-10, "-15": 2.8367413051377368e-11, "-2": 0.10166394573059954, "-3": 0.04489772981539745, "-4": 0.015868803615274325, "-5": 0.004650510794782564, "-6": 0.0011606510908539187, "-7": 0.00025181351922181407, "-8": 4.826768642418186e-05, "-9": 8.280799874003943e-06, "0": 0.25896907549367343, "1": 0.19240595553842424, "10": 2.5102047273321263e-06, "11": 3.7869478303564367e-07, "12": 5.2524466236006815e-08, "13": 6.7355492931923335e-09, "14": 7.941672859818134e-10, "15": 7.599332598055647e-11, "2": 0.11979704557275674, "3": 0.05635600357177832, "4": 0.021217619211064898, "5": 0.006623534178886671, "6": 0.0017608707051901134, "7": 0.00040695040639845184, "8": 8.309130619498055e-05, "9": 1.5184764190459287e-05} |
| Raw goal margin distribution | {"-1": 0.183133175066741, "-10": 1.3540304417615987e-06, "-11": 1.9176614946901348e-07, "-12": 2.4969371673138985e-08, "-13": 3.005953966777354e-09, "-14": 3.327243922362106e-10, "-15": 2.988900379824125e-11, "-2": 0.10711706614144509, "-3": 0.04730598502423773, "-4": 0.01671998538151681, "-5": 0.004899958080677678, "-6": 0.0012229068896813361, "-7": 0.0002653204653818038, "-8": 5.085670167567997e-05, "-9": 8.724971094061819e-06, "0": 0.23479303369865057, "1": 0.1952110471912562, "10": 2.546801070245911e-06, "11": 3.842157845654126e-07, "12": 5.329022185617863e-08, "13": 6.833747049320514e-09, "14": 8.057454724190566e-10, "15": 7.710123474451584e-11, "2": 0.12154356995465386, "3": 0.05717761927885862, "4": 0.021526951457955974, "5": 0.006720098863620308, "6": 0.0017865424870381478, "7": 0.00041288334742883956, "8": 8.430269660531478e-05, "9": 1.5406143280112118e-05} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Malaga", "away_goals": 1.0, "away_xg": 1.16, "date": "2026-10-31T00:00:00+00:00", "home": "Betis", "home_goals": 2.0, "home_xg": 1.8, "source": "pipeline training history"}, {"away": "Malaga", "away_goals": 1.0, "away_xg": 0.71, "date": "2026-10-23T00:00:00+00:00", "home": "Alaves", "home_goals": 1.0, "home_xg": 1.84, "source": "pipeline training history"}, {"away": "Sociedad", "away_goals": 5.0, "away_xg": 2.44, "date": "2026-10-18T00:00:00+00:00", "home": "Malaga", "home_goals": 2.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Espanol", "away_goals": 1.0, "away_xg": 0.99, "date": "2026-10-09T00:00:00+00:00", "home": "Malaga", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Malaga", "away_goals": 0.0, "away_xg": 0.52, "date": "2026-09-20T00:00:00+00:00", "home": "Getafe", "home_goals": 1.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Villarreal", "away_goals": 3.0, "away_xg": 3.33, "date": "2026-09-17T00:00:00+00:00", "home": "Malaga", "home_goals": 1.0, "home_xg": 0.63, "source": "pipeline training history"}, {"away": "Malaga", "away_goals": 1.0, "away_xg": 0.42, "date": "2026-09-13T00:00:00+00:00", "home": "Celta", "home_goals": 1.0, "home_xg": 1.9, "source": "pipeline training history"}, {"away": "Levante", "away_goals": 0.0, "away_xg": 0.98, "date": "2026-09-06T00:00:00+00:00", "home": "Malaga", "home_goals": 0.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Malaga", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-08-30T00:00:00+00:00", "home": "Real Madrid", "home_goals": 4.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "La Coruna", "away_goals": 1.0, "away_xg": 1.11, "date": "2026-08-24T00:00:00+00:00", "home": "Malaga", "home_goals": 1.0, "home_xg": 1.97, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 40.4% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 36.1% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 58.4% |
| Raw p btts yes | 65.2% |
| P home draw | 65.8% |
| P draw away | 60.1% |
| P home away | 74.1% |
| Raw p home draw | 63.9% |
| Raw p draw away | 59.6% |
| Raw p home away | 76.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6292 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.14, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.9, "draw": 3.58, "home": 2.46}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.92, "draw": 3.72, "home": 2.48}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.73, "under": 2.28}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.46 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-11-05T12:27:25Z |
| Market reference home last update utc | 2026-11-05T12:27:25Z |
| Market reference draw last update utc | 2026-11-05T12:27:25Z |
| Market reference away last update utc | 2026-11-05T12:27:25Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-11-05T12:27:26Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:27:26Z |
| Market best over 2 5 last update utc | 2026-11-05T12:27:26Z |
| Market best under 2 5 last update utc | 2026-11-05T12:27:26Z |
| Home probability edge | +0.2% |
| Draw probability edge | -1.0% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +5.9% |
| Under 2.5 probability edge | -5.9% |
| Raw edge prob home | 0.0083 |
| Raw ev home | 0.0031 |
| Raw edge prob draw | -0.0345 |
| Raw ev draw | -0.1266 |
| Raw edge prob away | 0.0262 |
| Raw ev away | 0.0533 |
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
| 1 | 0-1 | 14.57% |
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
| Market best home last update utc | 2026-11-05T12:27:26Z |
| Market best draw last update utc | 2026-11-05T12:27:25Z |
| Market best away last update utc | 2026-11-05T12:27:26Z |
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
| Dc lambda away | 1.8195 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:26:42.954541+00:00 |
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
| Fair Under 0.5 odds | 19.59 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.21 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.86 |
| Fair Under 4.5 odds | 1.17 |
| Score matrix json | [[0.05105090152877106,0.14573938880385195,0.13496621571339218,0.08185540970668298,0.037233251648383155,0.01354891541834058,0.004108628284446352,0.001067929004449109,0.00024288235504375355,4.910175626185185e-05,8.93388991064246e-06,1.4777177217235792e-06,2.2405456969945215e-07,3.135840927494834e-08,4.075393596066802e-09,4.943355798467986e-10,5.6214125337407484e-11],[0.04050612122094827,0.07905040204215706,0.11617018837990446,0.07045584196961421,0.03204797463666211,0.011662029998932818,0.0035364414662163177,0.0009192042094939369,0.0002090574207067136,4.2263615709849674e-05,7.68971455855734e-06,1.2719238306977115e-06,1.928516809320385e-07,2.6991290327801783e-08,3.5078351961998374e-09,4.2549209170716663e-10,4.8385482956163225e-11],[0.01810820067656717,0.03294722707300805,0.03032780250335567,0.030321915713543663,0.0137924117937835,0.005018960540262418,0.0015219700321051901,0.0003955957630288511,8.99715525746419e-05,1.8188893319255848e-05,3.3094044466368615e-06,5.473948804003592e-07,8.299712629874495e-08,1.1616178409625122e-08,1.509658818668941e-09,1.8311803508200614e-10,2.0823546989738968e-11],[0.005195455946015152,0.009452947305950742,0.008599650704152152,0.005277298098065375,0.003957205309560685,0.0014399988628061235,0.00043667111902455456,0.00011350108141369876,2.5813897589561774e-05,5.218607615125992e-06,9.495070944457836e-07,1.5705403518498222e-07,2.3812852587225164e-08,3.3328183327654988e-09,4.33138886960615e-10,5.253871995247716e-11,5.9745207686462855e-12],[0.0011179781043312348,0.0020341213974791814,0.0018505057673547929,0.0011223098087974042,0.0005165410453717884,0.00030986446918366927,9.396456344465878e-05,2.4423597304439928e-05,5.5547333270554745e-06,1.1229599691403265e-06,2.0431857233083347e-07,3.3795488665118476e-08,5.124140801271551e-09,7.171686105053717e-10,9.320448422390625e-11,1.1305482934853998e-11,1.2856202559742161e-12],[0.0001924566474628967,0.00035016802491455386,0.00031855913341782285,0.00019320233766570948,8.788119542911464e-05,3.235772810655121e-05,1.6175723648623192e-05,4.204450550494582e-06,9.562310295110949e-07,1.9331426085939944e-07,3.517284219865822e-08,5.817794125538592e-09,8.821057907305667e-10,1.2345847016928162e-10,1.6044878242916662e-11,1.9462056861055835e-12,2.2131575154881682e-13],[2.760903888990929e-05,5.023366428396545e-05,4.569918274693039e-05,2.771601253867999e-05,1.2607074758287627e-05,4.587624824869493e-06,1.4076306466279998e-06,6.031531791162705e-07,1.3717696961649266e-07,2.773206857960144e-08,5.0457512428538554e-09,8.345968111932693e-10,1.265432678078297e-10,1.771084422973508e-11,2.301732225060958e-12,2.791946611551087e-13,3.1749047237450084e-14],[3.394867831898058e-06,6.176841274193338e-06,5.619271502721059e-06,3.4080215458147397e-06,1.5501934972059895e-06,5.641043864246437e-07,1.7106131124762817e-07,4.4988946821682677e-08,1.6867580334297475e-08,3.409995831737883e-09,6.204366131841281e-10,1.0262385004500371e-10,1.556003709281868e-11,2.1777641587248496e-12,2.8302603070179745e-13,3.433038642788738e-14,3.903932316862527e-15],[3.652603296609121e-07,6.64578178530614e-07,6.045881793255319e-07,3.666755629245842e-07,1.6678828627949501e-07,6.069307093862117e-08,1.8404813981698704e-08,4.783843490284277e-09,1.1008776266574231e-09,3.668879801269143e-10,6.675396306625331e-11,1.1041496504313885e-11,1.6741341812065088e-12,2.3430981526453826e-13,3.04513125092589e-14,3.693672002843729e-15,4.2003155222506877e-16],[3.493249615602697e-08,6.355843430479293e-08,5.782115531099407e-08,3.5067845183908e-08,1.5951174261759105e-08,5.8045188461311946e-09,1.7601859316749218e-09,4.5751367111377116e-10,1.0405373151387375e-10,2.128468462676977e-11,6.384165946453189e-12,1.0559784429691544e-12,1.6010960156543954e-13,2.240874810753856e-14,2.9122800118019434e-15,3.5325265998841625e-16,4.0170665665044014e-17],[3.0067633130083146e-09,5.4706989058647236e-09,4.976871040887735e-09,3.018413281841526e-09,1.3729739024499934e-09,4.996154365339121e-10,1.5150541947516664e-10,3.937981744448851e-11,8.956272151297535e-12,1.8106242921952973e-12,3.3333461307561006e-13,9.089179391778146e-14,1.3781198855561409e-14,1.928800089156142e-15,2.5067022572856476e-16,3.040570400499466e-17,3.4576310619571342e-18],[2.3527521558547283e-10,4.280748866769794e-10,3.894335154416994e-10,2.36186810095403e-10,1.0743337511623315e-10,3.909424098391653e-11,1.1855096832920803e-11,3.0814181478417482e-12,7.008163403225839e-13,1.416789339046205e-13,2.5777978111639387e-14,4.314279081808062e-15,1.078360414250377e-15,1.5092603226672258e-16,1.9614610549488276e-17,2.379205750533717e-18,2.705550150879943e-19],[1.687580725987506e-11,3.0704931084120615e-11,2.7933265009557127e-11,1.6941194058949753e-11,7.705975009852903e-12,2.804149490093678e-12,8.503417102463377e-13,2.2102378535986085e-13,5.026811453311951e-14,1.0162338499655308e-14,1.849001345419084e-15,3.0583565310802386e-16,4.692010076898481e-17,1.0825613844164555e-17,1.4069156680484403e-18,1.7065553453082268e-19,1.9406354708700137e-20],[1.1173541000499734e-12,2.0329860438835115e-12,1.849472899611807e-12,1.1216833867566878e-12,5.102157567664424e-13,1.8566388449807468e-13,5.630147238327051e-14,1.463407521651407e-14,3.32827242041982e-15,6.728525879578944e-16,1.2242313523064178e-16,2.0249503663994904e-17,3.0702709748733354e-18,4.347958843461093e-19,9.315246174067234e-20,1.1299172730990663e-20,1.2849026815059005e-21],[6.869615248514557e-14,1.2499020611688665e-13,1.1370761723897078e-13,6.896232176822518e-14,3.136862291513842e-14,1.1414818739998139e-14,3.4614761173797826e-15,8.997189543652974e-16,2.0462582962289093e-16,4.136771322565786e-17,7.526708288032978e-18,1.2449616387393151e-18,1.887636184904875e-19,2.6419130003842934e-20,3.474101847312034e-21,6.946855010863766e-22,7.899722257550584e-23],[3.94194696946526e-15,7.172232306923434e-15,6.524810793110998e-15,3.957220389603708e-15,1.800005437908135e-15,6.55009174623873e-16,1.9862764939757162e-16,5.16279919213473e-17,1.1741911879718287e-17,2.37377678202358e-18,4.3190024262969155e-19,7.143882999837773e-20,1.0831700858570975e-20,1.5159918814532821e-21,1.9702095062263475e-22,2.4180942314269685e-23,4.5330466243364026e-24],[2.120608107396768e-16,3.8583710273144745e-16,3.5100844263711886e-16,2.1288245899684904e-16,9.683301562791098e-17,3.523684557113856e-17,1.0685364540121958e-17,2.7773772474639773e-18,6.3166738977837625e-19,1.276995943401104e-19,2.3234486998474228e-20,3.843120246187633e-21,5.827017165758086e-22,8.155423448006488e-23,1.0598930641475733e-23,1.2856251551915194e-24,1.4792665902351855e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.29651535879381663, "-10": 1.029223886841064e-05, "-11": 1.6826302467508899e-06, "-12": 2.5260934318613134e-07, "-13": 3.5055337026998835e-08, "-14": 4.521709234763708e-09, "-15": 5.427210628029618e-10, "-16": 5.6214125337407484e-11, "-2": 0.2207527780083805, "-3": 0.11938442419467477, "-4": 0.050536505958494654, "-5": 0.01750792552838075, "-6": 0.005123232919248353, "-7": 0.0012961595211615842, "-8": 0.0002886176791711791, "-9": 5.736341204998412e-05, "0": 0.16625675668792095, "1": 0.08326795357820505, "10": 3.4639251823990625e-09, "11": 2.6790041713325694e-10, "12": 1.9026554974402776e-11, "13": 1.249081999418968e-12, "14": 7.621939323470612e-14, "15": 4.327784072196707e-15, "16": 2.120608107396768e-16, "2": 0.0296180461381106, "3": 0.0075774651762958315, "4": 0.0015174260809814456, "5": 0.0002486927216816968, "6": 3.44269491219383e-05, "7": 4.120395873759175e-06, "8": 4.340397169693183e-07, "9": 4.0810091603372874e-08} |
| Raw goal margin distribution | {"-1": 0.2492776296186487, "-10": 8.652586898105157e-06, "-11": 1.4145711747982837e-06, "-12": 2.123662617178254e-07, "-13": 2.9470686965829254e-08, "-14": 3.801357759179105e-09, "-15": 4.562604130523621e-10, "-16": 4.725867817504358e-11, "-2": 0.185584751688783, "-3": 0.10036534497806383, "-4": 0.04248555779972964, "-5": 0.014718745743923983, "-6": 0.0043070529745560405, "-7": 0.001089668927630403, "-8": 0.0002426381258039828, "-9": 4.822487253552703e-05, "0": 0.2304139631893526, "1": 0.11676585959760108, "10": 4.8574293485515774e-09, "11": 3.756742077699919e-10, "12": 2.6680757137625376e-11, "13": 1.751575811612375e-12, "14": 1.0688173044506671e-13, "15": 6.068810456212827e-15, "16": 2.9737085864283495e-16, "2": 0.0415331044934327, "3": 0.010625807370780156, "4": 0.0021278721657931364, "5": 0.00034873943906351795, "6": 4.827658342498513e-05, "7": 5.777991957374459e-06, "8": 6.0864976829078e-07, "9": 5.7227603436287034e-08} |
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
| Unanchored p over 2 5 | 0.5306 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.08, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.13, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.13, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:27:25Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.3, "draw": 6.61, "home": 8.94}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:27:26Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.32, "draw": 6.12, "home": 10.6}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 8.94 |
| Reference draw odds | 6.61 |
| Reference away odds | 1.30 |
| Market reference 1x2 last update utc | 2026-11-05T12:27:25Z |
| Market reference home last update utc | 2026-11-05T12:27:25Z |
| Market reference draw last update utc | 2026-11-05T12:27:25Z |
| Market reference away last update utc | 2026-11-05T12:27:25Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.91 |
| Market reference over 2 5 last update utc | 2026-11-05T12:26:41Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:26:41Z |
| Home probability edge | +2.1% |
| Draw probability edge | +2.7% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -15.4% |
| Under 2.5 probability edge | +15.4% |
| Raw edge prob home | 0.0703 |
| Raw ev home | 0.8174 |
| Raw edge prob draw | 0.0917 |
| Raw ev draw | 0.5230 |
| Raw edge prob away | -0.1619 |
| Raw ev away | -0.2105 |
| Count model | {"corners": {"alpha": 0.014493407444055235, "mu": 9.801212284987749, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,462.7950 |
| Elo away rating | 1,679.9082 |
| Elo rating diff | -157.1133 |
| Elo home expectancy | 0.2881 |

</details>


---
