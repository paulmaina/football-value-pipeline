# Premier League — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,990 |
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
| Training sha256 | 360bea142f79da4d57d8363e05c1e1dd30c82d5fbca24beefafe296e82c9d2a4 |
| Training as of utc | 2026-11-05T13:30:52.436797+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 90, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 90, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 233, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-05T13:30:52.436797+00:00', 'observations': 642, 'observations_sha256': 'a74496bfcfd3037993920b5bf282167ffb16f3b640390b628049004d45ef0edb', 'eligible_training_matches': 297, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 267, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 28, 'retrospective_eligible_training_matches': 297, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'bb420e73fb62ceaa6d23f7532df48dcd3a7b8d7256ad31a4600ea2866a27ccd5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 236, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-04T00:00:00+00:00', 'audit_origin_utc': '2025-11-02T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 12, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1989, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1619, 'tuning_matches': 249, 'audit_matches': 112, 'audit_matchdays': 37, 'selected_shrinkage': 15.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9372365915629014, 'audit_candidate_poisson_score': 0.9280458784415208, 'audit_gain': 0.009190713121380645, 'audit_gain_lower95': 0.0003476760981782903, 'audit_baseline_briers': [0.6265817822406763, 0.16783379803353324, 0.2144793454599894, 0.2603736901518194], 'audit_candidate_briers': [0.6267009894464598, 0.1671447860232481, 0.21207329001908468, 0.2571284796929984], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'market_brier_worse']} |
| Optimizer objective | 1877.909 |
| Base scoring parameter | 0.214 |
| Home-advantage parameter | 0.178 |
| Dixon-Coles low-score adjustment | -0.061 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1990, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261105T133052436797Z_694117c5a1070177ef3ed63c463bbdaf309e3ff7e28c990a254cab03a9670b54.json |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'ANCHORED_MAIN': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3} |
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

## 2026-11-06 — Everton vs Coventry City

The model's most likely 1X2 outcome is **Everton win** at **54.8%**. Expected goals are 1.44 for Everton and 0.89 for Coventry City (2.33 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 56.0%; Under 3.5 goals: 66.2%; Double Chance 1X: 79.6%; Double Chance X2: 45.2%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 54.8% | 1.82 |
| Draw | 24.8% | 4.03 |
| Coventry City win | 20.4% | 4.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.44 |
| Coventry City expected goals | 0.89 |
| Expected total goals | 2.33 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 79.8% |
| Under 1.5 | 20.2% |
| Over 2.5 | 56.0% |
| Under 2.5 | 44.0% |
| Over 3.5 | 33.8% |
| Under 3.5 | 66.2% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.68% |
| 2 | 2-1 | 10.19% |
| 3 | 1-0 | 9.37% |
| 4 | 2-0 | 9.08% |
| 5 | 3-1 | 6.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 54.8% | 57.3% | 1.74 | -4.6% |
| Draw | 24.8% | 23.3% | 4.21 | +4.4% |
| Coventry City win | 20.4% | 19.4% | 4.93 | +0.5% |
| Over 2.5 | 56.0% | 55.6% | 1.81 | +1.3% |
| Under 2.5 | 44.0% | 44.4% | 2.15 | -5.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:00:00+00:00 |
| Fixture id | 586bec023ee8ac2f0645d963bd2c9d25 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:31:30Z |
| Market best draw last update utc | 2026-11-05T13:31:30Z |
| Market best away last update utc | 2026-11-05T13:31:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Everton |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4393 |
| Dc lambda away | 0.8948 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:30:52.436797+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.37 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.94 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.96 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.78 |
| Fair Under 4.5 odds | 1.21 |
| Score matrix json | [[0.06108557752989479,0.04763267231441693,0.030029469883910163,0.011230614380768923,0.0031500730746444002,0.0007068507591243806,0.0001321762976697282,2.118520385586482e-05,2.971117072699425e-06,3.703858271291545e-07,4.155578249636453e-08,4.23853607483791e-09,3.9628874884823945e-10,3.4201526845953384e-11,2.7409086620955377e-12,2.0501253172902201e-13,1.4375982343186293e-14],[0.0937337436476224,0.11679790329302903,0.0541935535149588,0.020267653868114723,0.0056848707088978856,0.0012756387172262803,0.0002385357879731185,3.8232492392523926e-05,5.361912571251091e-06,6.684275220742741e-07,7.499484777050208e-08,7.649197021619286e-09,7.151739807964497e-10,6.172277707814564e-11,4.946460288280892e-12,3.6998180961718847e-13,2.5944033359809806e-14],[0.09079897883182976,0.10187275912994911,0.05572066907004573,0.018288304601621504,0.005129683377350443,0.0011510591987638876,0.00021524026299379374,3.449868796376352e-05,4.83826549379615e-06,6.031485542109521e-07,6.767081323294554e-08,6.902172594789927e-09,6.453297302721454e-10,5.569489963704957e-11,4.463386489652943e-12,3.338492000785129e-13,2.34103260183102e-14],[0.05462100327277624,0.06128254283728891,0.034378259566645135,0.012535766125490257,0.0030858106131513427,0.0006924307858052867,0.00012947986046398037,2.0753019168478243e-05,2.9105053687956146e-06,3.628298421124741e-07,4.070803172703105e-08,4.152068632705016e-09,3.8820433624588526e-10,3.350380515827795e-11,2.6849932807122707e-12,2.0083021290223812e-13,1.4082707873082715e-14],[0.024643344315994457,0.027648829446743167,0.01551043072670397,0.0058006906896672815,0.0015863827045478754,0.0003124038235690756,5.8417396096990554e-05,9.363134441365016e-06,1.3131319755990118e-06,1.636978486580102e-07,1.8366232441132233e-08,1.873287761273839e-09,1.7514605279756135e-10,1.5115903351100593e-11,1.211387743507498e-12,9.060851667056493e-14,6.3536917709989186e-15],[0.008894665168178481,0.009979452344917247,0.00559826970557392,0.0020936769282273743,0.0005872550775055366,0.00012848280978293515,2.108492952972886e-05,3.379490409770746e-06,4.739563386695553e-07,5.9084413783040525e-08,6.629030778861488e-09,6.761366146786752e-10,6.321648049008126e-11,5.455870652073922e-12,4.372332029764793e-13,3.2703857351330054e-14,2.293274815308515e-15],[0.0026753358986621933,0.0030016180038863927,0.001683846623850159,0.0006297357956010116,0.00017663448379630838,3.9635340514460307e-05,7.22635999111938e-06,1.0164825590951195e-06,1.4255650811651935e-07,1.7771400075934567e-08,1.9938787667323316e-09,2.0336825765193205e-10,1.9014242407601202e-11,1.6410158604025354e-12,1.3151092951704422e-13,9.836660733420102e-15,6.897708146274396e-16],[0.0006897317856432169,0.0007738509944394842,0.00043411466171340714,0.00016235299462790244,4.553836322979749e-05,1.0218438066519399e-05,1.910778610852827e-06,2.986074100132776e-07,3.675267653210821e-08,4.5816674885137725e-09,5.140444468382749e-10,5.243063181844153e-11,4.902086267001388e-12,4.230724075546064e-13,3.390500172062449e-14,2.5360021430658643e-15,1.7783070002367304e-16],[0.0001555930581722136,0.00017456907931560995,9.792970139892123e-05,3.6624379887052595e-05,1.0272765945495257e-05,2.3051250668843962e-06,4.310427527642378e-07,6.908748957941889e-08,9.447081772921423e-09,1.0335548845284305e-09,1.1596065192997189e-10,1.1827557488778051e-11,1.1058365144002514e-12,9.543873588240466e-14,7.648455551641009e-15,5.720837246944208e-16,4.011591611337092e-17],[3.119950264119977e-05,3.5004572280794956e-05,1.963685278340512e-05,7.343916563126351e-06,2.059893879675304e-06,4.622234208736638e-07,8.643264462642657e-08,1.385341569172832e-08,1.9428710791235324e-09,2.361509644649753e-10,2.3252416969399904e-11,2.371660506226703e-12,2.2174221431896256e-13,1.913736465633407e-14,1.5336674526983352e-15,1.1471416456019297e-16,8.044039017139e-18],[5.630508705489657e-06,6.317201630601978e-06,3.543821573597033e-06,1.3253411958711434e-06,3.7174472155145407e-07,8.341648984088718e-08,1.559831781949439e-08,2.5000968300706146e-09,3.506258625483161e-10,4.370977209418411e-11,4.781528971607354e-12,4.2800858976327405e-13,4.001735163716251e-14,3.453680000505144e-15,2.767777436407253e-16,2.0702224315147018e-17,1.4516908245034099e-18],[9.237509808229115e-07,1.0364110078784057e-06,5.814054867333631e-07,2.1743776515562802e-07,6.098908093581077e-08,1.368545336448828e-08,2.5590869561922405e-09,4.101702030365904e-10,5.7524284460318434e-11,7.171100686547489e-12,8.045683138026345e-13,8.001261955783063e-14,6.56531581040322e-15,5.666167045980355e-16,4.540863455353413e-17,3.396442669147759e-18,2.381669034059376e-19],[1.3892283260203116e-07,1.5586576463077788e-07,8.743752243208239e-08,3.2700447281977985e-08,9.172142771474521e-09,2.0581541847393007e-09,3.8486087290800995e-10,6.168546246525411e-11,8.65107231985115e-12,1.0784612313613668e-12,1.2099896129553268e-13,1.23414464043337e-14,1.1250532147728631e-15,8.521343872594787e-17,6.829000745577303e-18,5.107907284147881e-19,3.5817900646484e-20],[1.9285470603922525e-08,2.1637513183709914e-08,1.2138204620217968e-08,4.539523870768556e-09,1.27329026108316e-09,2.8571597112359475e-10,5.342694870273522e-11,8.56326602892512e-12,1.200954499645423e-12,1.497135638924889e-13,1.6797252600333446e-14,1.7132576221108746e-15,1.6018377749609985e-16,1.34791786153014e-17,9.480118614502725e-19,7.090871524207278e-20,4.972293301784327e-21],[2.4860059784015943e-09,2.789197538249622e-09,1.5646830649175972e-09,5.851702410379362e-10,1.6413429914691535e-10,3.683040081965154e-11,6.887035147368428e-12,1.1038533090409125e-12,1.5480981134572736e-13,1.929892313899957e-14,2.1652606380607266e-15,2.208485744829815e-16,2.064859275029878e-17,1.782067750681839e-18,1.3924654391588108e-19,9.140533494511418e-21,6.4095666258140835e-22],[2.990961846254017e-10,3.3557374724955727e-10,1.8825004401869257e-10,7.040296281318915e-11,1.9747314796310723e-11,4.4311367145081435e-12,8.285925109815564e-13,1.3280672532112752e-13,1.862546764503613e-14,2.32189074700656e-15,2.6050669273929964e-16,2.6570718888733078e-17,2.4842721068068267e-18,2.1440401576009655e-19,1.718232717012302e-20,1.2530805085042784e-21,7.711473502231513e-23],[3.373578760772093e-11,3.7850180797580896e-11,2.1233181259442147e-11,7.940921758646572e-12,2.2273477631468424e-12,4.997987093972622e-13,9.345896872215716e-14,1.497959421957128e-14,2.1008118888389616e-15,2.6189171616297946e-16,2.9383184769306634e-17,2.9969761404259306e-18,2.802071054834271e-19,2.4183151473443357e-20,1.9380365575161994e-21,1.4495987653088206e-22,9.910968076250621e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.12353488408972498, "-10": 4.988505783478592e-08, "-11": 5.012182850343608e-09, "-12": 4.6268209632071123e-10, "-13": 3.949591904218587e-11, "-14": 3.1343007977310365e-12, "-15": 2.309565650888318e-13, "-16": 1.4375982343186293e-14, "-2": 0.056181182058235885, "-3": 0.01820587953717203, "-4": 0.004663079337856988, "-5": 0.000982966275676832, "-6": 0.00017562894721229603, "-7": 2.7192911192796647e-05, "-8": 3.711548212649847e-06, "-9": 4.526866149817379e-07, "0": 0.24786231618828716, "1": 0.2364143253054023, "10": 6.759065418565743e-06, "11": 1.0923603674284509e-06, "12": 1.62197659161235e-07, "13": 2.2270859107949488e-08, "14": 2.8428129069105937e-09, "15": 3.369463654229826e-10, "16": 3.373578760772093e-11, "2": 0.169872927500001, "3": 0.08854577070035223, "4": 0.03647974728604714, "5": 0.012369168146027785, "6": 0.0035548463348199413, "7": 0.000885326160722913, "8": 0.0001943683546724465, "9": 3.81321211700511e-05} |
| Raw goal margin distribution | {"-1": 0.14827450281302046, "-10": 9.874564361771061e-09, "-11": 7.955729321469263e-10, "-12": 5.883566704241396e-11, "-13": 4.0071339948760685e-12, "-14": 2.3454350286715505e-13, "-2": 0.058369343118998746, "-3": 0.015811874032841813, "-4": 0.003331279015748369, "-5": 0.0005723277896888028, "-6": 8.287058812295185e-05, "-7": 1.0359416624309608e-05, "-8": 1.1386509782245205e-06, "-9": 1.1163139000538705e-07, "0": 0.2833404778493635, "1": 0.2431364589866305, "10": 1.144844583479692e-06, "11": 1.4836499504790236e-07, "12": 1.7648792141128187e-08, "13": 1.9334414751961026e-09, "14": 1.8203019377390573e-10, "2": 0.15101862912040404, "3": 0.06580394375556851, "4": 0.022299875822919188, "5": 0.006162531160305621, "6": 0.0014352831102877885, "7": 0.00028859932542780613, "8": 5.102388166568697e-05, "9": 8.046222956808518e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Everton", "away_goals": 1.0, "away_xg": 2.15, "date": "2026-11-02T00:00:00+00:00", "home": "Newcastle", "home_goals": 0.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-10-24T00:00:00+00:00", "home": "Arsenal", "home_goals": 2.0, "home_xg": 1.96, "source": "pipeline training history"}, {"away": "Chelsea", "away_goals": 2.0, "away_xg": 1.47, "date": "2026-10-17T00:00:00+00:00", "home": "Everton", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 2.0, "away_xg": 1.68, "date": "2026-10-11T00:00:00+00:00", "home": "Hull", "home_goals": 2.0, "home_xg": 1.33, "source": "pipeline training history"}, {"away": "Ipswich", "away_goals": 0.0, "away_xg": 1.44, "date": "2026-09-19T00:00:00+00:00", "home": "Everton", "home_goals": 1.0, "home_xg": 2.24, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": 1.11, "date": "2026-09-12T00:00:00+00:00", "home": "Tottenham", "home_goals": 0.0, "home_xg": 0.69, "source": "pipeline training history"}, {"away": "Man United", "away_goals": 2.0, "away_xg": 0.69, "date": "2026-09-06T00:00:00+00:00", "home": "Everton", "home_goals": 2.0, "home_xg": 1.01, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 1.0, "away_xg": 1.84, "date": "2026-08-29T00:00:00+00:00", "home": "Bournemouth", "home_goals": 1.0, "home_xg": 2.15, "source": "pipeline training history"}, {"away": "Crystal Palace", "away_goals": 0.0, "away_xg": 1.96, "date": "2026-08-22T00:00:00+00:00", "home": "Everton", "home_goals": 2.0, "home_xg": 1.12, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Tottenham", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 49.0% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.2% |
| Raw p btts yes | 45.9% |
| P home draw | 79.6% |
| P draw away | 45.2% |
| P home away | 75.2% |
| Raw p home draw | 77.4% |
| Raw p draw away | 51.0% |
| Raw p home away | 71.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2538 |
| Totals anchor target over 2 5 | 0.5599 |
| Totals anchor reference over odds | 1.74 |
| Totals anchor reference under odds | 2.19 |
| Totals anchor reference last update utc | 2026-11-05T13:31:51Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4269 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.8, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.01, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 5.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.24, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:01Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.66, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:01Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.31, "price": 3.66, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.15}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:02Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.22, "under": 4.09}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.93, "draw": 4.21, "home": 1.74}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.15}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.22, "home_away": 1.27, "home_draw": 1.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.86, "draw": 4.08, "home": 1.71}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.74, "under": 2.19}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:01Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.23, "home_away": 1.27, "home_draw": 1.21}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.71 |
| Reference draw odds | 4.08 |
| Reference away odds | 4.86 |
| Market reference 1x2 last update utc | 2026-11-05T13:31:31Z |
| Market reference home last update utc | 2026-11-05T13:31:31Z |
| Market reference draw last update utc | 2026-11-05T13:31:31Z |
| Market reference away last update utc | 2026-11-05T13:31:31Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.24 |
| Market reference over 2 5 last update utc | 2026-11-05T13:31:09Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:31:09Z |
| Market best over 2 5 last update utc | 2026-11-05T13:31:30Z |
| Market best under 2 5 last update utc | 2026-11-05T13:31:30Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.5% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | -0.0831 |
| Raw ev home | -0.1470 |
| Raw edge prob draw | 0.0507 |
| Raw ev draw | 0.1929 |
| Raw edge prob away | 0.0324 |
| Raw ev away | 0.1164 |
| Market p home draw | 80.1% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T13:31:30Z |
| Market reference home draw last update utc | 2026-11-05T13:32:01Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.5% |
| Market draw away odds | 2.23 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-05T13:32:01Z |
| Market reference draw away last update utc | 2026-11-05T13:32:01Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.4% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T13:31:30Z |
| Market reference home away last update utc | 2026-11-05T13:32:01Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.23 |
| Market reference dc home draw odds | 1.21 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 79.5% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-05T13:31:02Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-11-05T13:31:52Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.5% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T13:31:51Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.80 |
| Market reference under 3 5 last update utc | 2026-11-05T13:31:52Z |
| Market under 3 5 bookmakers | 2 |
| Count model | {"corners": {"alpha": 0.009288361750668784, "mu": 9.755785148145803, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,448.4574 |
| Elo away rating | 1,377.6232 |
| Elo rating diff | 130.8342 |
| Elo home expectancy | 0.6799 |

</details>


---

## 2026-11-07 — Arsenal vs Hull City

The model's most likely 1X2 outcome is **Arsenal win** at **78.5%**. Expected goals are 1.67 for Arsenal and 0.60 for Hull City (2.27 combined). The most likely exact score is 1-0 at 20.8%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 44.1%; Under 3.5 goals: 78.6%; Double Chance 1X: 93.1%; Double Chance X2: 21.5%; Double Chance 12 (either team wins): 85.4%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 34.2%; BTTS No (at least one team does not score): 65.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 78.5% | 1.27 |
| Draw | 14.6% | 6.84 |
| Hull City win | 6.9% | 14.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.67 |
| Hull City expected goals | 0.60 |
| Expected total goals | 2.27 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 69.6% |
| Under 1.5 | 30.4% |
| Over 2.5 | 44.1% |
| Under 2.5 | 55.9% |
| Over 3.5 | 21.4% |
| Under 3.5 | 78.6% |
| Over 4.5 | 9.3% |
| Under 4.5 | 90.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.80% |
| 2 | 2-0 | 18.03% |
| 3 | 2-1 | 10.79% |
| 4 | 3-0 | 10.03% |
| 5 | 0-0 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 78.5% | 85.2% | 1.19 | -6.6% |
| Draw | 14.6% | 10.2% | 8.40 | +22.9% |
| Hull City win | 6.9% | 4.5% | 19.00 | +30.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:00:00+00:00 |
| Fixture id | 842fcc5b9feb8c63054a661ad1fc8926 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:31:30Z |
| Market best draw last update utc | 2026-11-05T13:31:30Z |
| Market best away last update utc | 2026-11-05T13:31:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Hull |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6696 |
| Dc lambda away | 0.5987 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:30:52.436797+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 34.2% |
| P btts no | 65.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.47 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.29 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.68 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.78 |
| Fair Under 4.5 odds | 1.10 |
| Score matrix json | [[0.06464569482655905,0.030938326501292718,0.010312081427228923,0.002057851127473873,0.0003079944111717118,3.6877519873638705e-05,3.679589149190823e-06,3.14695232524988e-07,2.3549899102530933e-08,1.5665180937534595e-09,9.378303637886532e-11,5.104115326335388e-12,2.546408684119187e-13,1.172664096500537e-14,5.014578877686562e-16,2.0013916433991836e-17],[0.20804086442713493,0.06461951656245284,0.01721752886997054,0.003435883574757994,0.0005142417370887196,6.157241557468079e-05,6.143612504701463e-06,5.254297388434293e-07,3.9320002517831e-08,2.615531180088756e-09,1.5658450214551096e-10,8.522067402880656e-12,4.2516019043254696e-13,1.9579343005344654e-14,8.372573200337293e-16,3.341616204596155e-17],[0.18026584125489745,0.10792009371412668,0.015218830253402229,0.002868355193843258,0.000429300913542538,5.140207872833722e-05,5.128830023893356e-06,4.38640916555914e-07,3.282524887412532e-08,2.1835060128878164e-09,1.3072036936992901e-10,7.114419265226932e-12,3.5493357499125405e-13,1.6345289058688393e-14,6.98961804219803e-16,2.789658609709815e-17],[0.10032673319408165,0.06006279599598475,0.01797895410327231,0.001690254590006867,0.00023892689770357476,2.8607763968477102e-05,2.8544440689534384e-06,2.4412506494275735e-07,1.8268852062588038e-08,1.21522759751755e-09,7.275226149065206e-11,3.959521329634409e-12,1.9753784650424828e-13,9.096950608919761e-15,3.890063361791178e-16,1.552581082975007e-17],[0.04187754037312515,0.02507090666830372,0.007504623666653634,0.0014976024367798523,0.00010559552205731033,1.1941212002359972e-05,1.1914780132348292e-06,1.0190062945092684e-07,7.625630432336374e-09,5.0725007340894e-10,3.036763652931006e-11,1.6527500603378228e-12,8.245458492303275e-14,3.797172540846129e-15,1.623757500129935e-16,6.4806532531123704e-18],[0.013984136286468305,0.00837190944241511,0.0025060134668388667,0.000500093281321661,7.484794874382855e-05,4.222006069657702e-06,3.9786937749808784e-07,3.402760231909786e-08,2.5464211671912516e-09,1.6938564430168602e-10,1.0140642553026674e-11,5.519016132586695e-13,2.7533998958253938e-14,1.2679870365190878e-15,5.4222014893129146e-17,2.1640797790270158e-18],[0.0038914269625223976,0.002329687973903303,0.0006973593630331998,0.00013916315164880962,2.0828267106712238e-05,2.4938596490733416e-06,1.172275565771626e-07,9.469010199983448e-09,7.08603791106813e-10,4.713568645191443e-11,2.821881097249802e-12,1.5358008349593916e-13,7.66200670082806e-15,3.52848316189101e-16,1.508859799382734e-17,6.022079754259929e-19],[0.0009281866759244231,0.0005556792809588714,0.00016633478549960915,3.319332069805782e-05,4.9679770935528545e-06,5.948376572883219e-07,5.935209842711785e-08,2.3913711923570597e-09,1.6901681664572459e-10,1.124284653073879e-11,6.730776295522423e-13,3.663206031133899e-14,1.8275487627146543e-15,8.41616992592358e-17,3.598946029600552e-18,1.436391905357807e-19],[0.00019371793418025278,0.00011597348374658825,3.4715032940123145e-05,6.927638244544202e-06,1.0368455878332787e-06,1.241460636436646e-07,1.238712663604372e-08,1.0594035200651397e-09,3.734912050863441e-11,2.3464471756947283e-12,1.4047519892476732e-13,7.64532311478346e-15,3.8142000969165645e-16,1.756503399637939e-17,7.51120877043498e-19,2.997833084621958e-20],[3.593782634601592e-05,2.1514966785415207e-05,6.440203023420141e-06,1.285189527102788e-06,1.9235171405716744e-07,2.303111322989866e-08,2.2980133866078924e-09,1.9653657724345082e-10,1.4707615768130618e-11,4.609021362300409e-13,2.606043331116087e-14,1.418331738984018e-15,7.075961310035362e-17,3.2585993867577425e-18,1.393451347614468e-19,5.561467773512295e-21],[6.0003459728574975e-06,3.592238525058728e-06,1.075286131773736e-06,2.145811972338375e-07,3.211593327049157e-08,3.845381359153007e-09,3.8368696084018787e-10,3.281465741493497e-11,2.4556516633739447e-12,1.633477385989158e-13,4.607041043902657e-15,2.368112377261848e-16,1.1814352805306233e-17,5.440708494506751e-19,2.3265709232184123e-20,9.285684236066977e-22],[9.107686917484228e-07,5.452516232756438e-07,1.632134126800036e-07,3.257042796573989e-08,4.874749999643051e-09,5.836751689972482e-10,5.823832041453612e-11,4.980806563348941e-12,3.727336161877748e-13,2.4793904694290384e-14,1.4843414035182572e-15,3.8058360135299366e-17,1.793253705205744e-18,8.25823540866037e-20,3.531409631352398e-21,1.4094371427793209e-22],[1.2672180001279703e-07,7.586478080262658e-08,2.2709056238347944e-08,4.531757949520939e-09,6.782590356518133e-10,8.121092513194953e-11,8.10311647679101e-12,6.930154483148154e-13,5.1861109408491723e-14,3.4497543236522383e-15,2.0652709759517349e-16,1.1240179086125719e-17,2.641806106141248e-19,1.1490277008818475e-20,4.913504264276098e-22,1.9610512894883817e-23],[1.627542983345768e-08,9.74364250396622e-09,2.916622486059638e-09,5.820333085719569e-10,8.71117466966614e-11,1.0430270983854025e-11,1.0407183581438144e-12,8.900697671127596e-14,6.660746984164849e-15,4.4306689481682974e-16,2.6525169980843617e-17,1.443624901266108e-18,7.202147189401439e-20,1.5625272332133432e-21,6.310626417991618e-23,2.5186631391486482e-24],[1.9410151162860605e-09,1.1620312078644415e-09,3.4783771561619493e-10,6.941355538258909e-11,1.0388986274065137e-11,1.243918830641382e-12,1.241165416596803e-13,1.0615012262002096e-14,7.943636951107242e-16,5.284035808366036e-17,3.1634037577941292e-18,1.721673580530676e-19,8.589313282287332e-21,3.9555234643011007e-22,7.968652426701857e-24,3.00376904078448e-25],[2.1605391719438703e-10,1.2934540913912025e-10,3.871773093175155e-11,7.726405848653722e-12,1.1563955176636007e-12,1.3846030037425217e-13,1.3815381853132473e-14,1.1815544150218809e-15,8.842042834476624e-17,5.8816473164686095e-18,3.5211769748945043e-19,1.916390645712613e-20,9.560743577302781e-22,4.402883480123376e-23,1.8827732993811907e-24,3.5401016020639495e-26]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.051275486184589714, "-10": 1.0266929884717593e-10, "-11": 5.5460162928160565e-12, "-12": 2.749346990323129e-13, "-13": 1.2591794871136197e-14, "-14": 5.348740498146177e-16, "-15": 2.0013916433991836e-17, "-2": 0.014207099905102029, "-3": 0.0026264538822269815, "-4": 0.00037494757971020317, "-5": 4.347855969309997e-05, "-6": 4.239090291790964e-06, "-7": 3.5627317395773403e-07, "-8": 2.630019391112345e-08, "-9": 1.7304184050074652e-09, "0": 0.14628423341729038, "1": 0.3355149169160811, "10": 6.568899213126635e-06, "11": 9.896206649880095e-07, "12": 1.368210066382281e-07, "13": 1.7476178772253872e-08, "14": 2.070360525425181e-09, "15": 2.1605391719438703e-10, "2": 0.24835478988976534, "3": 0.1280479109352345, "4": 0.05098106276469264, "5": 0.016487282940149228, "6": 0.004483139173749858, "7": 0.001050819900904012, "8": 0.0002163414463400122, "9": 3.969789841118508e-05} |
| Raw goal margin distribution | {"-1": 0.0922132050517809, "-10": 1.8463920698937325e-10, "-11": 9.973887634899991e-12, "-12": 4.944391884739611e-13, "-13": 2.2644929357510612e-14, "-14": 9.619109266925907e-16, "-15": 3.5992781684663103e-17, "-2": 0.025549874106001968, "-3": 0.004723382427403124, "-4": 0.0006743011256298357, "-5": 7.819130814094307e-05, "-6": 7.623527954522148e-06, "-7": 6.407173035150464e-07, "-8": 4.729794594823171e-08, "-9": 3.111963222189501e-09, "0": 0.2484648095389934, "1": 0.2684721753590511, "10": 5.256298818760329e-06, "11": 7.918742187431707e-07, "12": 1.0948137157242347e-07, "13": 1.3984080872100825e-08, "14": 1.6566601543305788e-09, "15": 1.7288192631545333e-10, "2": 0.19872842410527589, "3": 0.10246131979748273, "4": 0.040794003880241014, "5": 0.013192786649808354, "6": 0.0035873162882801035, "7": 0.0008408445958211907, "8": 0.00017311200125791684, "9": 3.176544650114378e-05} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Arsenal", "away_goals": 1.0, "away_xg": 0.96, "date": "2026-11-01T00:00:00+00:00", "home": "Liverpool", "home_goals": 0.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-10-24T00:00:00+00:00", "home": "Arsenal", "home_goals": 2.0, "home_xg": 1.96, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 1.0, "away_xg": 1.14, "date": "2026-10-18T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.9, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 1.0, "away_xg": 0.62, "date": "2026-10-10T00:00:00+00:00", "home": "Arsenal", "home_goals": 2.0, "home_xg": 2.33, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 0.0, "away_xg": 1.63, "date": "2026-09-19T00:00:00+00:00", "home": "Brighton", "home_goals": 3.0, "home_xg": 1.31, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 2.0, "away_xg": 1.88, "date": "2026-09-12T00:00:00+00:00", "home": "Sunderland", "home_goals": 0.0, "home_xg": 1.8, "source": "pipeline training history"}, {"away": "Chelsea", "away_goals": 1.0, "away_xg": 0.39, "date": "2026-09-06T00:00:00+00:00", "home": "Arsenal", "home_goals": 2.0, "home_xg": 2.05, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 1.0, "away_xg": 1.05, "date": "2026-08-31T00:00:00+00:00", "home": "Aston Villa", "home_goals": 0.0, "home_xg": 0.32, "source": "pipeline training history"}, {"away": "Coventry", "away_goals": 0.0, "away_xg": 0.2, "date": "2026-08-21T00:00:00+00:00", "home": "Arsenal", "home_goals": 3.0, "home_xg": 1.88, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 2.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Crystal Palace", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 12.3% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 37.2% |
| P home draw | 93.1% |
| P draw away | 21.5% |
| P home away | 85.4% |
| Raw p home draw | 87.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 75.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4412 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.87, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.44, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.65, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "line": -2.0, "market_key": "spreads", "opposite_price": 2.02, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 19.0, "draw": 8.4, "home": 1.19}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 17.83, "draw": 8.31, "home": 1.16}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 8.31 |
| Reference away odds | 17.83 |
| Market reference 1x2 last update utc | 2026-11-05T13:31:31Z |
| Market reference home last update utc | 2026-11-05T13:31:31Z |
| Market reference draw last update utc | 2026-11-05T13:31:31Z |
| Market reference away last update utc | 2026-11-05T13:31:31Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.64 |
| Market reference over 2 5 last update utc | 2026-11-05T13:31:30Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:31:30Z |
| Home probability edge | -6.7% |
| Draw probability edge | +4.4% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -20.6% |
| Under 2.5 probability edge | +20.6% |
| Raw edge prob home | -0.2241 |
| Raw ev home | -0.2523 |
| Raw edge prob draw | 0.1460 |
| Raw ev draw | 1.0871 |
| Raw edge prob away | 0.0782 |
| Raw ev away | 1.3417 |
| Count model | {"corners": {"alpha": 0.009288361750668784, "mu": 9.88825063485941, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,656.9795 |
| Elo away rating | 1,392.5184 |
| Elo rating diff | 324.4611 |
| Elo home expectancy | 0.8662 |

</details>


---

## 2026-11-07 — Fulham vs Newcastle United

The model's most likely 1X2 outcome is **Fulham win** at **44.1%**. Expected goals are 1.41 for Fulham and 1.41 for Newcastle United (2.82 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.7%; Double Chance 1X: 69.8%; Double Chance X2: 55.9%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 44.1% | 2.27 |
| Draw | 25.8% | 3.88 |
| Newcastle United win | 30.2% | 3.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 1.41 |
| Newcastle United expected goals | 1.41 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.8% |
| Under 2.5 | 46.2% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.17% |
| 2 | 2-1 | 10.04% |
| 3 | 1-0 | 9.23% |
| 4 | 2-0 | 7.11% |
| 5 | 1-2 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 44.1% | 47.3% | 2.16 | -4.8% |
| Draw | 25.8% | 25.4% | 3.88 | -0.0% |
| Newcastle United win | 30.2% | 27.3% | 3.52 | +6.2% |
| Over 2.5 | 53.8% | 58.1% | 1.71 | -7.9% |
| Under 2.5 | 46.2% | 41.9% | 2.32 | +7.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:00:00+00:00 |
| Fixture id | 3903e98a54db0f2cc23095407fe9dad8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:31:30Z |
| Market best draw last update utc | 2026-11-05T13:31:30Z |
| Market best away last update utc | 2026-11-05T13:31:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fulham |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4092 |
| Dc lambda away | 1.4114 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:30:52.436797+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.46 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.55 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.38 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.06466711172137901,0.0630823188588715,0.04870880847943128,0.02291640364519562,0.008086241058195357,0.002282637204811242,0.000536964844696261,0.00010826997218027883,1.910197402630815e-05,2.995683675241702e-06,4.2282062590887325e-07,5.4252991690406374e-08,6.3812044235377345e-09,6.928185659797052e-10,6.984763304852294e-11],[0.09226121983893606,0.12169958874689564,0.06864191818064613,0.032294485394206165,0.01139537415167968,0.003216761015924188,0.000756707012266346,0.00015257730180277048,2.6919076428575797e-05,4.221607552109826e-06,5.958515454341768e-07,7.645494794315754e-08,8.99258523475113e-09,9.763407647323911e-10,9.84313856671964e-11],[0.07113849075726576,0.10040720065603347,0.05703421075038317,0.022755180154440252,0.008029352026623207,0.002266578195553701,0.0005331871425744449,0.00010750826178587535,1.8967586145010488e-05,2.9746081789815114e-06,4.198459611958657e-07,5.387130628986653e-08,6.336310815085255e-09,6.879443881027243e-10,6.935623486076916e-11],[0.03341683372742812,0.04716561588026784,0.033285549126383186,0.012604773438642124,0.0037717348056790358,0.0010647100589956798,0.00025046112026481167,5.05012922003336e-05,8.90989766118629e-06,1.397302442927079e-06,1.9721985281198178e-07,2.5305688464918082e-08,2.9764399370727776e-09,3.23157308880608e-10,3.257963085288059e-11],[0.011773001835710055,0.016616801186792905,0.01172674928342729,0.005517172938822954,0.0015669573600458247,0.0003751053610075172,8.823933627893018e-05,1.7791985040529345e-05,3.1390239535182955e-06,4.922801591498579e-07,6.948203735077891e-08,8.91538435931634e-09,1.0486221743467218e-09,1.1385075024483272e-10,1.1478048966766649e-11],[0.0033181736690958484,0.004683379220699103,0.0033051375714841387,0.001554993214892874,0.0005486921147907986,0.00012466923291391,2.4869905424726464e-05,5.014600108475313e-06,8.84721396851575e-07,1.387472018355337e-07,1.958323544239757e-08,2.512765566826078e-09,2.955499826045403e-10,3.208838042676029e-11,3.235042377942587e-12],[0.0007793450254465855,0.00109999314741302,0.0007762832152949515,0.0003652238693582824,0.00012887223901107497,3.63789015584526e-05,6.8880914409716015e-06,1.1777875539013125e-06,2.0779600114490346e-07,3.258778844285773e-08,4.599547415593981e-09,5.901774710764261e-10,6.941632105001793e-11,7.536651831441809e-12,7.59819839401426e-13],[0.00015689663633218045,0.00022144906194615825,0.00015628023705048386,7.352635192314525e-05,2.5944376569091577e-05,7.323748919434048e-06,1.7228299323385076e-06,2.7960500500834014e-07,4.1833196541199675e-08,6.56052739832303e-09,9.259743689818803e-10,1.1881369230253768e-10,1.3974795403437144e-11,1.5172680686354516e-12,1.5296585354122067e-13],[2.7637932465746768e-05,3.9009084973070035e-05,2.7529351414439865e-05,1.2951943371190161e-05,4.570199490856673e-06,1.2901059115305445e-06,3.034829709104001e-07,6.119226080106579e-08,8.68974604415157e-09,1.1556615706575448e-09,1.6311386702230155e-10,2.092947867225903e-11,2.461712759508058e-12,2.6727247564822197e-13,2.6945510296261524e-14],[4.327578426935811e-06,6.1080862250888516e-06,4.310576684284036e-06,2.0280298025014497e-06,7.15606956053468e-07,2.0200622887118315e-07,4.751970356255625e-08,9.581552746983562e-09,1.6904647523121787e-09,2.13385145287328e-10,2.5540552026988097e-11,3.2771612167927067e-12,3.8545774162241933e-13,4.184982364952458e-14,4.21915818795049e-15],[6.098553702612059e-07,8.607698853482119e-07,6.074594335416197e-07,2.8579606054211123e-07,1.0084548495507958e-07,2.8467325453078973e-08,6.696619576081303e-09,1.3502612365887011e-09,2.3822537819720784e-10,3.7359901940542176e-11,4.244302215316246e-12,4.618274171146348e-13,5.431986449374069e-14,5.897603042452161e-15,5.945764640307255e-16],[7.812968487316287e-08,1.1027480148573572e-07,7.782273704584913e-08,3.661385508269408e-08,1.2919499187236815e-08,3.647001035472084e-09,8.579161596471523e-10,1.7298443213829194e-10,3.0519488119561904e-11,4.7862452441086664e-12,6.755463624523418e-13,6.976908819291821e-14,6.959017009936526e-15,7.555526927908157e-16,7.617227630187696e-17],[9.17522518678181e-09,1.2950213964152732e-08,9.13917851078703e-09,4.299778834194524e-09,1.5172122418742782e-09,4.2828863077082296e-10,1.0075010501988493e-10,2.0314572127777638e-11,3.5840817294590035e-12,5.620767315925143e-13,7.933335466121453e-14,1.0179427320876613e-14,9.63701805155675e-16,8.872896528495203e-17,8.945355266619695e-18],[9.946156419073946e-10,1.4038331607762618e-09,9.907080988168091e-10,4.661059754035566e-10,1.6446931787957957e-10,4.642747864427877e-11,1.0921544521975692e-11,2.2021466269898217e-12,3.8852275311237037e-13,6.093041836177369e-14,8.599919224293945e-15,1.103473476987713e-15,1.2978989016481674e-16,1.13422204790762e-17,9.696972106380868e-19],[1.0011730591930107e-10,1.4130885147509306e-10,9.97239753999431e-11,4.691789729025493e-11,1.6555365026143194e-11,4.673357110669544e-12,1.0993549346569731e-12,2.2166651945136466e-13,3.9108425095110185e-14,6.133212748613364e-15,8.65661776853576e-16,1.1107485848256934e-16,1.3064558399608694e-17,1.418442039278368e-18,1.1510233426178393e-19]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.15865234806849057, "-10": 5.059465200249634e-07, "-11": 6.396610094411311e-08, "-12": 7.426901423130895e-09, "-13": 7.912499516469016e-10, "-14": 6.984763304852294e-11, "-2": 0.09019082441861839, "-3": 0.03684752735421491, "-4": 0.011889973000914945, "-5": 0.0031562748443429997, "-6": 0.0007099791008504211, "-7": 0.00013837009526460772, "-8": 2.3769814698453376e-05, "-9": 3.648500052695441e-06, "0": 0.2577044878541519, "1": 0.23205799932722854, "10": 7.297520115981582e-07, "11": 9.211752483342267e-08, "12": 1.0678782322958015e-08, "13": 1.1359244933824876e-09, "14": 1.0011730591930107e-10, "2": 0.1317223584314, "3": 0.05373127973859915, "4": 0.01731096970259687, "5": 0.004588143949837436, "6": 0.001030456064087036, "7": 0.00020051545298110568, "8": 3.439165671853539e-05, "9": 5.270639970839056e-06} |
| Raw goal margin distribution | {"-1": 0.19325515729985598, "-10": 6.162957907848206e-07, "-11": 7.791740273819605e-08, "-12": 9.046742895718557e-09, "-13": 9.638252174056222e-10, "-14": 8.508172413551433e-11, "-2": 0.1098618594191829, "-3": 0.044884143106885536, "-4": 0.014483230979921536, "-5": 0.0038446729528500956, "-6": 0.000864828819017704, "-7": 0.00016854925156489824, "-8": 2.8954120972448195e-05, "-9": 4.444254750568207e-06, "0": 0.2662026993676765, "1": 0.19294226723838334, "10": 6.067449001875405e-07, "11": 7.659018066723118e-08, "12": 8.87876513074347e-09, "13": 9.44452885917443e-10, "14": 8.324151742181384e-11, "2": 0.10951921741729521, "3": 0.044674326954643816, "4": 0.014393029984733217, "5": 0.0038147656993690006, "6": 0.0008567622312994967, "7": 0.0001667165373599191, "8": 2.8594593767920178e-05, "9": 4.382220086009387e-06} |
| Research history json | {"away": [{"away": "Everton", "away_goals": 1.0, "away_xg": 2.15, "date": "2026-11-02T00:00:00+00:00", "home": "Newcastle", "home_goals": 0.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 2.0, "away_xg": 0.95, "date": "2026-10-25T00:00:00+00:00", "home": "Crystal Palace", "home_goals": 0.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Aston Villa", "away_goals": 1.0, "away_xg": 1.57, "date": "2026-10-17T00:00:00+00:00", "home": "Newcastle", "home_goals": 0.0, "home_xg": 0.99, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 1.0, "away_xg": 1.84, "date": "2026-10-12T00:00:00+00:00", "home": "Coventry", "home_goals": 4.0, "home_xg": 1.43, "source": "pipeline training history"}, {"away": "Hull", "away_goals": 1.0, "away_xg": 1.59, "date": "2026-09-19T00:00:00+00:00", "home": "Newcastle", "home_goals": 2.0, "home_xg": 1.44, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 1.0, "away_xg": 0.85, "date": "2026-09-14T00:00:00+00:00", "home": "Leeds", "home_goals": 4.0, "home_xg": 1.91, "source": "pipeline training history"}, {"away": "Bournemouth", "away_goals": 2.0, "away_xg": 1.37, "date": "2026-09-05T00:00:00+00:00", "home": "Newcastle", "home_goals": 2.0, "home_xg": 0.71, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 2.0, "away_xg": 0.75, "date": "2026-08-29T00:00:00+00:00", "home": "Tottenham", "home_goals": 0.0, "home_xg": 1.04, "source": "pipeline training history"}, {"away": "Liverpool", "away_goals": 2.0, "away_xg": 2.98, "date": "2026-08-23T00:00:00+00:00", "home": "Newcastle", "home_goals": 2.0, "home_xg": 1.57, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Fulham", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [{"away": "Newcastle", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Fulham", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 1.0, "away_xg": null, "date": "2025-10-25T00:00:00+00:00", "home": "Newcastle", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 2.0, "away_xg": null, "date": "2025-02-01T00:00:00+00:00", "home": "Newcastle", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 1.0, "away_xg": null, "date": "2024-09-21T00:00:00+00:00", "home": "Fulham", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 1.0, "away_xg": null, "date": "2024-04-06T00:00:00+00:00", "home": "Fulham", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 0.0, "away_xg": null, "date": "2023-12-16T00:00:00+00:00", "home": "Newcastle", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 0.0, "away_xg": null, "date": "2023-01-15T00:00:00+00:00", "home": "Newcastle", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Fulham", "away_goals": 1.0, "away_xg": 2.24, "date": "2026-10-31T00:00:00+00:00", "home": "Aston Villa", "home_goals": 1.0, "home_xg": 1.83, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 1.0, "away_xg": 0.55, "date": "2026-10-24T00:00:00+00:00", "home": "Coventry", "home_goals": 0.0, "home_xg": 0.51, "source": "pipeline training history"}, {"away": "Hull", "away_goals": 0.0, "away_xg": 0.16, "date": "2026-10-17T00:00:00+00:00", "home": "Fulham", "home_goals": 1.0, "home_xg": 1.38, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 1.0, "away_xg": 1.81, "date": "2026-10-10T00:00:00+00:00", "home": "Ipswich", "home_goals": 2.0, "home_xg": 1.15, "source": "pipeline training history"}, {"away": "Man United", "away_goals": 1.0, "away_xg": 1.6, "date": "2026-09-20T00:00:00+00:00", "home": "Fulham", "home_goals": 1.0, "home_xg": 1.62, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 0.0, "away_xg": 0.68, "date": "2026-09-12T00:00:00+00:00", "home": "Liverpool", "home_goals": 0.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Crystal Palace", "away_goals": 3.0, "away_xg": 1.97, "date": "2026-09-05T00:00:00+00:00", "home": "Fulham", "home_goals": 2.0, "home_xg": 3.14, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 0.0, "away_xg": 0.95, "date": "2026-08-30T00:00:00+00:00", "home": "Sunderland", "home_goals": 1.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Chelsea", "away_goals": 3.0, "away_xg": 1.7, "date": "2026-08-24T00:00:00+00:00", "home": "Fulham", "home_goals": 2.0, "home_xg": 1.35, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Fulham", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 36.6% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 36.7% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.9% |
| P home draw | 69.8% |
| P draw away | 55.9% |
| P home away | 74.2% |
| Raw p home draw | 63.3% |
| Raw p draw away | 63.4% |
| Raw p home away | 73.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5384 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.88, "home": 2.16}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.32}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.52, "draw": 3.78, "home": 2.07}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.07 |
| Reference draw odds | 3.78 |
| Reference away odds | 3.52 |
| Market reference 1x2 last update utc | 2026-11-05T13:31:31Z |
| Market reference home last update utc | 2026-11-05T13:31:31Z |
| Market reference draw last update utc | 2026-11-05T13:31:31Z |
| Market reference away last update utc | 2026-11-05T13:31:31Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-05T13:31:09Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:31:09Z |
| Market best over 2 5 last update utc | 2026-11-05T13:31:30Z |
| Market best under 2 5 last update utc | 2026-11-05T13:31:30Z |
| Home probability edge | -3.2% |
| Draw probability edge | +0.4% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | -0.1061 |
| Raw ev home | -0.2086 |
| Raw edge prob draw | 0.0121 |
| Raw ev draw | 0.0329 |
| Raw edge prob away | 0.0940 |
| Raw ev away | 0.2932 |
| Count model | {"corners": {"alpha": 0.009288361750668784, "mu": 10.272880036905677, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,459.2088 |
| Elo away rating | 1,451.5742 |
| Elo rating diff | 67.6346 |
| Elo home expectancy | 0.5961 |

</details>


---

## 2026-11-07 — Leeds United vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Leeds United win** at **36.7%**. Expected goals are 1.46 for Leeds United and 1.36 for Tottenham Hotspur (2.82 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 48.1%; Under 3.5 goals: 73.6%; Double Chance 1X: 64.7%; Double Chance X2: 63.3%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 87.7%; BTTS Yes (both teams score): 53.7%; BTTS No (at least one team does not score): 46.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 36.7% | 2.73 |
| Draw | 28.0% | 3.57 |
| Tottenham Hotspur win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.46 |
| Tottenham Hotspur expected goals | 1.36 |
| Expected total goals | 2.82 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 74.0% |
| Under 1.5 | 26.0% |
| Over 2.5 | 48.1% |
| Under 2.5 | 51.9% |
| Over 3.5 | 26.4% |
| Under 3.5 | 73.6% |
| Over 4.5 | 12.3% |
| Under 4.5 | 87.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.37% |
| 2 | 0-1 | 8.89% |
| 3 | 1-0 | 8.85% |
| 4 | 0-0 | 8.23% |
| 5 | 1-2 | 8.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 36.7% | 35.7% | 2.73 | +0.1% |
| Draw | 28.0% | 28.7% | 3.57 | +0.1% |
| Tottenham Hotspur win | 35.3% | 35.7% | 2.76 | -2.6% |
| Over 2.5 | 48.1% | 48.1% | 2.02 | -2.8% |
| Under 2.5 | 51.9% | 51.9% | 1.92 | -0.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T12:30:00+00:00 |
| Fixture id | 5c87852253fd11eea5d34ad723356607 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:31:31Z |
| Market best draw last update utc | 2026-11-05T13:31:30Z |
| Market best away last update utc | 2026-11-05T13:31:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4600 |
| Dc lambda away | 1.3602 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:30:52.436797+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.7% |
| P btts no | 46.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.16 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.85 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.79 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.16 |
| Fair Under 4.5 odds | 1.14 |
| Score matrix json | [[0.08225597993108542,0.08892878681548018,0.060790878094779566,0.025426117247907207,0.00797595945188167,0.002001593198294456,0.0004185886512701881,7.503299690958865e-05,1.1768610501339903e-05,1.640761902827422e-06,2.0587729191283969e-07,2.3484355459455418e-08,2.4556150285930876e-09,2.370171729815671e-10,2.1242941911922695e-11],[0.08846946836215462,0.1337012033607545,0.08187486856917113,0.03424461157891236,0.01074224706571444,0.0026958021528131,0.0005637669973093607,0.00010105655573432412,1.585029642994608e-05,2.2098243907227675e-06,2.772813412969627e-07,3.162939205577503e-08,3.3072915546486563e-09,3.1922141108484467e-10,2.861059309506121e-11],[0.0645189544717336,0.08095621674783281,0.05323712658727705,0.023060804187220157,0.0072339806086668705,0.0018153911727178643,0.0003796486434722517,6.80529092366527e-05,1.0673813059262931e-05,1.4881268968453399e-06,1.867251640943305e-07,2.129967849330797e-08,2.227176756145936e-09,2.1496819832317462e-10,1.9266776716828946e-11],[0.028965315647947295,0.0363447050710028,0.022802057515154135,0.009996481811609432,0.003247643013387097,0.0008150066716488322,0.00017044049897470848,3.055185895277247e-05,4.791930789333906e-06,6.680837537472788e-07,8.382890519059136e-08,9.5623358408381e-09,9.998748162263114e-10,9.650841012045899e-11,8.649679364627141e-12],[0.009752825942252248,0.012237518375019088,0.007677613486883683,0.0032112038322141307,0.0010558501359175067,0.0002744184909626107,5.738851736382705e-05,1.0287026255822872e-05,1.6134768729511499e-06,2.2494850891105262e-07,2.82257832502282e-08,3.219705878249713e-09,3.366648982949282e-10,3.249506193228847e-11,2.912408009801124e-12],[0.002627076190460483,0.003296366954941377,0.0020680852616849397,0.0008649879717198191,0.00027133946255087385,7.137355917181634e-05,1.5458494641966482e-05,2.7709713991956273e-06,4.3461522864107827e-07,6.059339880963188e-08,7.60305613704502e-09,8.672781307816672e-10,9.068595540526574e-11,8.753053116637475e-12,7.845026441318854e-13],[0.0005897033802774375,0.0007399399922325982,0.0004642259230798288,0.00019416503132826615,6.0907939727803e-05,1.5285047349700075e-05,3.3505024210933106e-06,6.220037343002752e-07,9.755867392820879e-08,1.3601482983360113e-08,1.7066683945959982e-09,1.9467910646055535e-10,2.03564002598647e-11,1.9648097871589773e-12,1.7609837992558183e-13],[0.00011346130554026872,0.00014236743479521656,8.931893738423767e-05,3.735813407480842e-05,1.1718932925283992e-05,2.9409046743565855e-06,6.150247323992041e-07,1.155550523775437e-07,1.877068180525649e-08,2.6169801093046795e-09,3.2836987314550293e-10,3.7457044200824465e-11,3.9166534003890025e-12,3.7803731680234457e-13,3.388203757706563e-14],[1.9101610656767732e-05,2.3968059390043164e-05,1.5037157893308368e-05,6.2893735319047024e-06,1.9729236587367122e-06,4.951116664904783e-07,1.0354158121689224e-07,1.8560071134002834e-08,3.0512939466635378e-09,4.4057782436411284e-10,5.528222541041945e-11,6.30602540020618e-12,6.59382403326777e-13,6.364391459187542e-14,5.7041604357829515e-15],[2.8585097541626094e-06,3.5867620163492787e-06,2.250274245731e-06,9.411895107469387e-07,2.952432454023948e-07,7.409226130160391e-08,1.5494746761841377e-08,2.7774696766579634e-09,4.3563445617474616e-10,6.366109600368355e-11,8.272851091303738e-12,9.436814224930269e-13,9.867497906334773e-14,9.5241576180651e-15,8.536137888046094e-16],[3.8499215303464347e-07,4.830752209560714e-07,3.0307327988676976e-07,1.2676205691739401e-07,3.976419270596533e-08,9.978954649418774e-09,2.0868761801078446e-09,3.7407744691017625e-10,5.867247679479175e-11,8.180028105990915e-12,1.0758437319831382e-12,1.2709767461710684e-13,1.3289824386614832e-14,1.2827404006163131e-15,1.1496711177332273e-16],[4.7138026023528626e-08,5.914721159186865e-08,3.710796711498995e-08,1.5520610201191413e-08,4.868685077874126e-09,1.2218124973305268e-09,2.5551487974601306e-10,4.580164111989136e-11,7.183795088334957e-12,1.0015538620567626e-12,1.2567161418714402e-13,1.502584506151939e-14,1.6271918345515048e-15,1.570573579463119e-16,1.4076449776713118e-17],[5.290568539013004e-09,6.638427681763604e-09,4.164838028374419e-09,1.7419662841995448e-09,5.464401943031289e-10,1.3713095995414176e-10,2.8677887006961148e-11,5.140578466801109e-12,8.062781472030768e-13,1.1241008162029576e-13,1.4104839433319015e-14,1.608934428236227e-15,1.763402681671002e-16,1.76274398159251e-17,1.5798799528114025e-18],[5.481143747517386e-10,6.877555051584879e-10,4.314862523812203e-10,1.8047148499483723e-10,5.661238924154536e-11,1.4207064858929591e-11,2.971091290115669e-12,5.325750779742456e-13,8.353216469484594e-14,1.1645928249252926e-14,1.4612919556675114e-15,1.6668909619943554e-16,1.7429656540355593e-17,1.7633554928014867e-18,1.636789895324896e-19],[5.27297066836058e-11,6.616346464817316e-11,4.15098464373888e-11,1.7361720303071367e-11,5.446225855172826e-12,1.3667482506468318e-12,2.858249655082928e-13,5.1234795039447887e-14,8.035962466776935e-15,1.120361750993245e-15,1.405792289909582e-16,1.6035826744979388e-17,1.6767680602889108e-18,1.618424796915996e-19,1.5204035896832277e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1974026207942587, "-10": 2.39833281542891e-07, "-11": 2.7015264891791874e-08, "-12": 2.7941032163947614e-09, "-13": 2.656277660766283e-10, "-14": 2.1242941911922695e-11, "-2": 0.10314473667466403, "-3": 0.038164931563057544, "-4": 0.011083637922186015, "-5": 0.0026384377858551084, "-6": 0.0005310162176190453, "-7": 9.245856153209615e-05, "-8": 1.4175067986047631e-05, "-9": 1.940376076998495e-06, "0": 0.2803214845593353, "1": 0.1957262049960016, "10": 4.484901203657365e-07, "11": 5.4225301677976524e-08, "12": 6.019833890608881e-09, "13": 6.142778393999118e-10, "14": 5.27297066836058e-11, "2": 0.10947021622448126, "3": 0.04347731423669326, "4": 0.013552826103764189, "5": 0.003462929976549386, "6": 0.0007480901777004108, "7": 0.00013981141007132417, "8": 2.30075274962891e-05, "9": 3.3804928876553627e-06} |
| Raw goal margin distribution | {"-1": 0.18584012475337214, "-10": 4.258691876162168e-07, "-11": 5.1889401374281963e-08, "-12": 5.808406173649983e-09, "-13": 6.010341942256756e-10, "-14": 5.743849415652711e-11, "-15": 4.599553270294787e-12, "-2": 0.10198539841179845, "-3": 0.040161302729411034, "-4": 0.012490395209699925, "-5": 0.0031955800813367663, "-6": 0.0006927712132981244, "-7": 0.00013012151753380308, "-8": 2.15422266650245e-05, "-9": 3.186645053005865e-06, "0": 0.26585796711301884, "1": 0.20000525691506016, "10": 8.645087179582268e-07, "11": 1.1306316385569142e-07, "12": 1.3584659831648099e-08, "13": 1.508829914922231e-09, "14": 1.5477238206488965e-10, "15": 1.3303177628671876e-11, "2": 0.11749966500356447, "3": 0.04966560602468101, "4": 0.016579576895236734, "5": 0.004552985680559404, "6": 0.001059462838094065, "7": 0.00021359659742094925, "8": 3.795640898217642e-05, "9": 6.026671699268644e-06} |
| Research history json | {"away": [{"away": "Crystal Palace", "away_goals": 0.0, "away_xg": 0.14, "date": "2026-10-31T00:00:00+00:00", "home": "Tottenham", "home_goals": 2.0, "home_xg": 3.47, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 2.0, "away_xg": 0.74, "date": "2026-10-24T00:00:00+00:00", "home": "Chelsea", "home_goals": 0.0, "home_xg": 0.47, "source": "pipeline training history"}, {"away": "Coventry", "away_goals": 1.0, "away_xg": 0.82, "date": "2026-10-19T00:00:00+00:00", "home": "Tottenham", "home_goals": 3.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 1.0, "away_xg": 1.62, "date": "2026-10-10T00:00:00+00:00", "home": "Man United", "home_goals": 1.0, "home_xg": 0.8, "source": "pipeline training history"}, {"away": "Aston Villa", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-19T00:00:00+00:00", "home": "Tottenham", "home_goals": 2.0, "home_xg": 1.56, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": 1.11, "date": "2026-09-12T00:00:00+00:00", "home": "Tottenham", "home_goals": 0.0, "home_xg": 0.69, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 0.0, "away_xg": 1.07, "date": "2026-09-05T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.92, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 2.0, "away_xg": 0.75, "date": "2026-08-29T00:00:00+00:00", "home": "Tottenham", "home_goals": 0.0, "home_xg": 1.04, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 0.0, "away_xg": 0.57, "date": "2026-08-22T00:00:00+00:00", "home": "Brentford", "home_goals": 3.0, "home_xg": 3.88, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Tottenham", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [{"away": "Leeds", "away_goals": 1.0, "away_xg": null, "date": "2026-05-11T00:00:00+00:00", "home": "Tottenham", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 2.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Leeds", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 4.0, "away_xg": null, "date": "2023-05-28T00:00:00+00:00", "home": "Leeds", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 3.0, "away_xg": null, "date": "2022-11-12T00:00:00+00:00", "home": "Tottenham", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Leeds", "away_goals": 0.0, "away_xg": 0.71, "date": "2026-10-31T00:00:00+00:00", "home": "Bournemouth", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 0.0, "away_xg": 0.76, "date": "2026-10-25T00:00:00+00:00", "home": "Sunderland", "home_goals": 0.0, "home_xg": 0.83, "source": "pipeline training history"}, {"away": "Man United", "away_goals": 1.0, "away_xg": 0.92, "date": "2026-10-18T00:00:00+00:00", "home": "Leeds", "home_goals": 1.0, "home_xg": 1.41, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 1.0, "away_xg": 0.62, "date": "2026-10-10T00:00:00+00:00", "home": "Arsenal", "home_goals": 2.0, "home_xg": 2.33, "source": "pipeline training history"}, {"away": "Crystal Palace", "away_goals": 0.0, "away_xg": 1.06, "date": "2026-09-20T00:00:00+00:00", "home": "Leeds", "home_goals": 0.0, "home_xg": 1.31, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 1.0, "away_xg": 0.85, "date": "2026-09-14T00:00:00+00:00", "home": "Leeds", "home_goals": 4.0, "home_xg": 1.91, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 1.0, "away_xg": 2.5, "date": "2026-09-05T00:00:00+00:00", "home": "Brighton", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Brentford", "away_goals": 1.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Leeds", "home_goals": 1.0, "home_xg": 1.43, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 1.0, "away_xg": 0.47, "date": "2026-08-22T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.66, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "West Ham", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 34.5% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.8% |
| P home draw | 64.7% |
| P draw away | 63.3% |
| P home away | 72.0% |
| Raw p home draw | 65.5% |
| Raw p draw away | 61.0% |
| Raw p home away | 73.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9225 |
| Totals anchor target over 2 5 | 0.4813 |
| Totals anchor reference over odds | 2.02 |
| Totals anchor reference under odds | 1.88 |
| Totals anchor reference last update utc | 2026-11-05T13:31:31Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5301 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:48Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.66, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:48Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.41, "price": 1.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:48Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.73, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:48Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.47, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.94, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:48Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:48Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:48Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:48Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:05Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:05Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.69, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.71, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.71, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:48Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.02, "under": 1.92}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:48Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.3, "under": 3.42}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.76, "draw": 3.57, "home": 2.68}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.02, "under": 1.92}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.53, "home_away": 1.34, "home_draw": 1.51}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.73, "draw": 3.38, "home": 2.73}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.02, "under": 1.88}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.02, "under": 1.88}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:51Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.31, "under": 3.59}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:32:05Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.5, "home_away": 1.36, "home_draw": 1.5}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.73 |
| Reference draw odds | 3.38 |
| Reference away odds | 2.73 |
| Market reference 1x2 last update utc | 2026-11-05T13:31:31Z |
| Market reference home last update utc | 2026-11-05T13:31:31Z |
| Market reference draw last update utc | 2026-11-05T13:31:31Z |
| Market reference away last update utc | 2026-11-05T13:31:31Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-11-05T13:31:31Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:31:31Z |
| Market best over 2 5 last update utc | 2026-11-05T13:31:30Z |
| Market best under 2 5 last update utc | 2026-11-05T13:31:30Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0329 |
| Raw ev home | 0.0637 |
| Raw edge prob draw | -0.0207 |
| Raw ev draw | -0.0509 |
| Raw edge prob away | -0.0122 |
| Raw ev away | -0.0491 |
| Market p home draw | 64.5% |
| Market home draw odds | 1.51 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T13:31:30Z |
| Market reference home draw last update utc | 2026-11-05T13:32:05Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.5% |
| Market draw away odds | 1.53 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T13:31:30Z |
| Market reference draw away last update utc | 2026-11-05T13:32:05Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.1% |
| Market home away odds | 1.36 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-05T13:32:05Z |
| Market reference home away last update utc | 2026-11-05T13:32:05Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home draw odds | 1.50 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 74.3% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T13:31:51Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.55 |
| Market reference over 1 5 last update utc | 2026-11-05T13:31:52Z |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 73.2% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T13:31:51Z |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.45 |
| Market reference under 3 5 last update utc | 2026-11-05T13:31:52Z |
| Market under 3 5 bookmakers | 2 |
| Count model | {"corners": {"alpha": 0.009288361750668784, "mu": 9.499534919178165, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,475.4318 |
| Elo away rating | 1,472.6402 |
| Elo rating diff | 62.7916 |
| Elo home expectancy | 0.5894 |

</details>


---

## 2026-11-07 — Nottingham Forest vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **56.1%**. Expected goals are 0.94 for Nottingham Forest and 1.84 for Manchester City (2.78 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.8%; Double Chance 1X: 43.9%; Double Chance X2: 79.6%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 52.0%; BTTS No (at least one team does not score): 48.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 20.4% | 4.91 |
| Draw | 23.5% | 4.26 |
| Manchester City win | 56.1% | 1.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.94 |
| Manchester City expected goals | 1.84 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.20% |
| 2 | 0-1 | 10.43% |
| 3 | 0-2 | 10.18% |
| 4 | 1-2 | 9.59% |
| 5 | 0-0 | 6.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 20.4% | 21.3% | 4.58 | -6.7% |
| Draw | 23.5% | 23.3% | 4.26 | +0.0% |
| Manchester City win | 56.1% | 55.4% | 1.78 | -0.1% |
| Over 2.5 | 52.6% | 57.9% | 1.70 | -10.5% |
| Under 2.5 | 47.4% | 42.1% | 2.34 | +10.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T17:30:00+00:00 |
| Fixture id | 59c5f635cfe11613c07e9a5520ced5c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:31:30Z |
| Market best draw last update utc | 2026-11-05T13:31:30Z |
| Market best away last update utc | 2026-11-05T13:31:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9418 |
| Dc lambda away | 1.8397 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:30:52.436797+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 52.0% |
| P btts no | 48.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.85 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.36 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.71 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.06735099878947028,0.10428696140320548,0.1017803155497069,0.06241510782037694,0.028706280260499466,0.010562193099348428,0.003238545771620824,0.0008511364434772923,0.00019572954481388523,4.0009310173621795e-05,7.360515817282787e-06,1.2310133194082338e-06,1.88724677861854e-07,2.6707456348874887e-08,3.50955197396045e-09,4.3043502797745035e-10,4.949197789826859e-11],[0.0576819674732894,0.11197209342150038,0.09585464686993268,0.05878128877041229,0.027034995347166805,0.00994726027564373,0.003049997041512627,0.0008015831232887272,0.00018433413473732996,3.7679960781111614e-05,6.931985233447503e-06,1.1593434976769407e-06,1.7773709242682643e-07,2.515254333108536e-08,3.3052252129377768e-09,4.0537502152936596e-10,4.661054584779886e-11],[0.03059847894137786,0.05629204484042685,0.04570993159289195,0.02767951566673854,0.01273050647434552,0.004684064476983658,0.0014362128265644498,0.0003774574032550242,8.680108376502393e-05,1.774311326919819e-05,3.264201889486143e-06,5.459231530703178e-07,8.369460311773958e-08,1.1844078817501812e-08,1.556397196749804e-09,1.9088700663151279e-10,2.194843565047501e-11],[0.009605676624345043,0.017671570547549656,0.016255200847879743,0.0087996343697892,0.0039964446824619655,0.0014704524607150565,0.000450865417269445,0.00011849392128540551,2.724916957104015e-05,5.570035317754546e-06,1.024719818493306e-06,1.7137980225039756e-07,2.6273962646710077e-08,3.7181714572199676e-09,4.885944886233788e-10,5.99245100060177e-11,6.890197897504231e-12],[0.002261608091408625,0.004160682115504978,0.0038272050166527254,0.002346970654147823,0.0009528865788739072,0.00034621061204125726,0.00010615398745035613,2.7898795851883296e-05,6.415679477470657e-06,1.3114367094285177e-06,2.4126511057613877e-07,4.035050966541746e-08,6.18607192798551e-09,8.754247078837764e-10,1.1503710692151658e-10,1.4108923504651866e-11,1.6222623273521637e-12],[0.0004259873705231021,0.0007836892875911752,0.0007208768874191967,0.00044206591825226915,0.00020331725100091393,6.603858617146764e-05,1.9994736557718316e-05,5.254904565849162e-06,1.2084314878023483e-06,2.4701692462948763e-07,4.544372229818193e-08,7.600259115155661e-09,1.165183536652461e-09,1.6489146409539699e-10,2.1667925082262956e-11,2.657499876963571e-12,3.055627832924018e-13],[6.686438458492395e-05,0.000123010458869319,0.00011315121708793961,6.938812653908073e-05,3.1913347212572723e-05,1.1742201798592807e-05,3.1782776322131777e-06,8.248271760182523e-07,1.8967939740966118e-07,3.8772592312136414e-08,7.132996738811377e-09,1.192961772075076e-09,1.8289105616225498e-10,2.5881908791114916e-11,3.4010690835238705e-12,4.171299576076134e-13,4.796214364715514e-14],[8.995932546270834e-06,1.6549823906159494e-05,1.52233617757855e-05,9.335476722512412e-06,4.29362089597031e-06,1.5797955216454356e-06,4.843918359119902e-07,1.1238085110532703e-07,2.5519461146724486e-08,5.2164635515494126e-09,9.596731939350725e-10,1.6050104548912313e-10,2.4606157893552797e-11,3.4821513291262835e-12,4.575797451889865e-13,5.6120653543156665e-14,6.452825546855372e-15],[1.0590234624830245e-06,1.948286264535281e-06,1.7921318568698299e-06,1.0989954439690756e-06,5.054556872733413e-07,1.8597744199868036e-07,5.702380677350411e-08,1.498667720433232e-08,3.042348131768401e-09,6.140950105910274e-10,1.1297510552305845e-10,1.8894580639835687e-11,2.8966978572595628e-12,4.0992747983530296e-13,5.386742103941421e-14,6.606662347276196e-15,7.596426071761205e-16],[1.1081854687064037e-07,2.0387296445501434e-07,1.8753262341633948e-07,1.1500130302359513e-07,5.289199602792595e-08,1.9461089015620297e-08,5.967096695719525e-09,1.5682389003067817e-09,3.6063628630732406e-10,6.507594071339956e-11,1.182196379036624e-11,1.9771705202143135e-12,3.0311684172903577e-13,4.289571406773263e-14,5.636805542778549e-15,6.913356945591353e-16,7.949067499496665e-17],[1.0436667070202333e-08,1.9200344299009156e-08,1.7661443961024352e-08,1.0830590602291118e-08,4.981261429698239e-09,1.8328060835943987e-09,5.61969122926916e-10,1.476935743269373e-10,3.396399754291383e-11,6.942621328439158e-12,1.1275012193921913e-12,1.8620592890992402e-13,2.8546932348697736e-14,4.039831770995078e-15,5.308629687963975e-16,6.51086003345921e-17,7.48627132853985e-18],[8.935493086352511e-10,1.6438633386056466e-09,1.5121083133839578e-09,9.272756024209421e-10,4.2647740669493384e-10,1.5691816150139083e-10,4.8113743390299535e-11,1.2644984298339357e-11,2.9078733966332846e-12,5.944018762325903e-13,1.0935215810636648e-13,1.61446344222963e-14,2.4440840636436654e-15,3.458756384288296e-16,4.5450548106722516e-17,5.574360514122999e-18,6.40947203247617e-19],[7.012722530343222e-11,1.2901310940581554e-10,1.1867275745289115e-10,7.277412053361404e-11,3.347065114044815e-11,1.2315196441274799e-11,3.77604603385169e-12,9.923992490155721e-13,2.2821470608154226e-13,4.66496408116646e-14,8.582137946762188e-15,1.4353241516928313e-15,1.942505640998005e-16,2.7144891265276624e-17,3.567034070131755e-18,4.374850183629116e-19,5.03025949383821e-20],[5.080338873540181e-12,9.346303266309015e-12,8.597200592344275e-12,5.272092143028551e-12,2.424767975287315e-12,8.921694954445876e-13,2.7355414920594413e-13,7.189396787097943e-14,1.6532923380370238e-14,3.3795146268333375e-15,6.217295613845758e-16,1.0398148582700712e-16,1.59412348403609e-17,1.991462575969029e-18,2.58412360838775e-19,3.169342770605471e-20,3.644151431910433e-21],[3.4175432932100437e-13,6.287256980128076e-13,5.783335709705038e-13,3.5465356924187257e-13,1.631141098617133e-13,6.001623024486467e-14,1.840198402546896e-14,4.836306274752695e-15,1.1121695387293527e-15,2.27339904575918e-16,4.1823739431374644e-17,6.994833186363289e-18,1.0723666584114684e-18,1.517564424747762e-19,1.7604052031474068e-20,2.1320164656690984e-21,2.4514201897891914e-22],[2.1457155296619878e-14,3.947474482046716e-14,3.631085894425317e-14,2.2267038216728994e-14,1.024117176021269e-14,3.768138285885963e-15,1.155374475533053e-15,3.0364904229761215e-16,6.982792158360853e-17,1.4273608902909688e-17,2.6259169089309163e-18,4.391728475011391e-19,6.732888496297388e-20,9.52807696661329e-21,1.2520578856111646e-21,1.3555848009871545e-22,1.539132037159045e-23],[1.2629947356976475e-15,2.3235323700673313e-15,2.1373021288835952e-15,1.310665447424769e-15,6.028080536175082e-16,2.2179728639072805e-16,6.800677257471998e-17,1.7873158702539188e-17,4.110157947111402e-18,8.401622980573691e-19,1.5456472148857646e-19,2.585025772464169e-20,3.96306155653467e-21,5.608344108899785e-22,7.369767783545542e-23,9.038778241879049e-24,9.174518715095884e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.23218462494368047, "-10": 8.607389832103627e-06, "-11": 1.4210974996274733e-06, "-12": 2.154951651620225e-07, "-13": 3.0210458766341675e-08, "-14": 3.93687543114029e-09, "-15": 4.770455738252492e-10, "-16": 4.949197789826859e-11, "-2": 0.17487416715803808, "-3": 0.09461418004060382, "-4": 0.04021491727683307, "-5": 0.014018254812102405, "-6": 0.004132749065789795, "-7": 0.0010542799533416905, "-8": 0.00023685144170807485, "-9": 4.751439003900207e-05, "0": 0.23485487710574843, "1": 0.13279174301474614, "10": 1.220464220865882e-08, "11": 1.0315247351716994e-09, "12": 8.00747319869821e-11, "13": 5.7466860959446665e-12, "14": 3.8336637627035514e-13, "15": 2.378068766668721e-14, "16": 1.2629947356976475e-15, "2": 0.052572872193179486, "3": 0.014561109469891689, "4": 0.0031683095644322846, "5": 0.0005653749605371928, "6": 8.532648367963466e-05, "7": 1.1143021095889004e-05, "8": 1.281519528031863e-06, "9": 1.3160625956102026e-07} |
| Raw goal margin distribution | {"-1": 0.23914008470838705, "-10": 8.865237885870598e-06, "-11": 1.4636687356978273e-06, "-12": 2.2195066561187715e-07, "-13": 3.1115461112959535e-08, "-14": 4.054810796871765e-09, "-15": 4.91336232801819e-10, "-16": 5.097458882063546e-11, "-2": 0.18011280099888502, "-3": 0.09744849830178391, "-4": 0.04141961909172656, "-5": 0.014438193933138667, "-6": 0.0042565521378136306, "-7": 0.001085862586334653, "-8": 0.00024394670339223187, "-9": 4.893775917139411e-05, "0": 0.23885838277251834, "1": 0.11922252922610553, "10": 1.095752099778076e-08, "11": 9.261192382481342e-10, "12": 7.189236211418962e-11, "13": 5.1594657579796595e-12, "14": 3.4419240203905655e-13, "15": 2.135067788095577e-14, "16": 1.1339366693334917e-15, "2": 0.04720075698423224, "3": 0.013073194612302852, "4": 0.00284455848735212, "5": 0.000507602590538092, "6": 7.66074679291347e-05, "7": 1.0004380755241771e-05, "8": 1.1505685211740713e-06, "9": 1.1815818341287824e-07} |
| Research history json | {"away": [{"away": "Brighton", "away_goals": 1.0, "away_xg": 1.0, "date": "2026-10-31T00:00:00+00:00", "home": "Man City", "home_goals": 0.0, "home_xg": 1.64, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 1.0, "away_xg": 1.56, "date": "2026-10-24T00:00:00+00:00", "home": "Aston Villa", "home_goals": 2.0, "home_xg": 0.61, "source": "pipeline training history"}, {"away": "Ipswich", "away_goals": 2.0, "away_xg": 1.66, "date": "2026-10-17T00:00:00+00:00", "home": "Man City", "home_goals": 3.0, "home_xg": 3.53, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 3.0, "away_xg": 1.29, "date": "2026-10-11T00:00:00+00:00", "home": "Liverpool", "home_goals": 0.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Sunderland", "away_goals": 3.0, "away_xg": 3.57, "date": "2026-09-20T00:00:00+00:00", "home": "Man City", "home_goals": 5.0, "home_xg": 2.82, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 1.0, "away_xg": 1.1, "date": "2026-09-13T00:00:00+00:00", "home": "Man United", "home_goals": 0.0, "home_xg": 1.0, "source": "pipeline training history"}, {"away": "Coventry", "away_goals": 0.0, "away_xg": 1.37, "date": "2026-09-05T00:00:00+00:00", "home": "Man City", "home_goals": 1.0, "home_xg": 2.12, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 4.0, "away_xg": 2.21, "date": "2026-08-28T00:00:00+00:00", "home": "Crystal Palace", "home_goals": 1.0, "home_xg": 0.66, "source": "pipeline training history"}, {"away": "Bournemouth", "away_goals": 1.0, "away_xg": 0.63, "date": "2026-08-23T00:00:00+00:00", "home": "Man City", "home_goals": 2.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Aston Villa", "away_goals": 2.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Man City", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [{"away": "Nott'm Forest", "away_goals": 2.0, "away_xg": null, "date": "2026-03-04T00:00:00+00:00", "home": "Man City", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 2.0, "away_xg": null, "date": "2025-12-27T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 0.0, "away_xg": null, "date": "2025-03-08T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 0.0, "away_xg": null, "date": "2024-12-04T00:00:00+00:00", "home": "Man City", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 2.0, "away_xg": null, "date": "2024-04-28T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 0.0, "away_xg": null, "date": "2023-09-23T00:00:00+00:00", "home": "Man City", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 1.0, "away_xg": null, "date": "2023-02-18T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Nott'm Forest", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-10-31T00:00:00+00:00", "home": "Brentford", "home_goals": 2.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 1.0, "away_xg": 2.31, "date": "2026-10-23T00:00:00+00:00", "home": "Ipswich", "home_goals": 1.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 1.0, "away_xg": 1.14, "date": "2026-10-18T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.9, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 1.0, "away_xg": 3.34, "date": "2026-10-11T00:00:00+00:00", "home": "Crystal Palace", "home_goals": 3.0, "home_xg": 2.41, "source": "pipeline training history"}, {"away": "Coventry", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-09-19T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 1.1, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 2.0, "away_xg": 2.28, "date": "2026-09-12T00:00:00+00:00", "home": "Aston Villa", "home_goals": 1.0, "home_xg": 0.82, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 0.0, "away_xg": 1.07, "date": "2026-09-05T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.92, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 2.0, "away_xg": 2.3, "date": "2026-08-29T00:00:00+00:00", "home": "Liverpool", "home_goals": 2.0, "home_xg": 1.75, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 1.0, "away_xg": 0.47, "date": "2026-08-22T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.66, "source": "pipeline training history"}, {"away": "Bournemouth", "away_goals": 1.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 18.3% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 57.8% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 52.0% |
| P home draw | 43.9% |
| P draw away | 79.6% |
| P home away | 76.5% |
| Raw p home draw | 42.2% |
| Raw p draw away | 81.7% |
| Raw p home away | 76.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5263 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.08, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.78, "draw": 4.26, "home": 4.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.7, "under": 2.34}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:31:31Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.77, "draw": 4.09, "home": 4.47}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.47 |
| Reference draw odds | 4.09 |
| Reference away odds | 1.77 |
| Market reference 1x2 last update utc | 2026-11-05T13:31:31Z |
| Market reference home last update utc | 2026-11-05T13:31:31Z |
| Market reference draw last update utc | 2026-11-05T13:31:31Z |
| Market reference away last update utc | 2026-11-05T13:31:31Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-05T13:31:09Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:31:09Z |
| Market best over 2 5 last update utc | 2026-11-05T13:31:30Z |
| Market best under 2 5 last update utc | 2026-11-05T13:31:30Z |
| Home probability edge | -0.9% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | -0.0297 |
| Raw ev home | -0.1622 |
| Raw edge prob draw | 0.0057 |
| Raw ev draw | 0.0175 |
| Raw edge prob away | 0.0240 |
| Raw ev away | 0.0292 |
| Count model | {"corners": {"alpha": 0.009288361750668784, "mu": 9.725962605950652, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,415.6922 |
| Elo away rating | 1,636.6871 |
| Elo rating diff | -160.9950 |
| Elo home expectancy | 0.2836 |

</details>


---
