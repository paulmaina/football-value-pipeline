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
| Training as of utc | 2026-11-05T13:35:50.710885+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 81, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 81, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 144, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_CHRONOLOGICAL_PARTITIONS', 'cutoff_utc': '2026-11-05T13:35:50.710885+00:00', 'observations': 514, 'observations_sha256': 'cd8a9ee495a2993a68a29a1ab182f0496a0ed8ce5889bf97708c3da8db9d5940', 'eligible_training_matches': 186, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 183, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 23, 'retrospective_eligible_training_matches': 186, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '608386dfd0aa877d2c75d41b6593ca8164fbfef0decec13dec5d64515dfb66b9', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 126, 'tuning_matches': 17, 'audit_matches': 43, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-05T00:00:00+00:00', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1759, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1471, 'tuning_matches': 187, 'audit_matches': 96, 'audit_matchdays': 34, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8547734904983413, 'audit_candidate_poisson_score': 0.8530374480014693, 'audit_gain': 0.0017360424968719812, 'audit_gain_lower95': -0.004922765199428151, 'audit_baseline_briers': [0.5824614078047651, 0.17370432402916056, 0.21287468772376236, 0.2466063615696182], 'audit_candidate_briers': [0.5816260245758471, 0.17326240897441395, 0.21186772195909942, 0.24573349270218828], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1597.280 |
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
| Additional event odds calls used before this league | 6.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261105T133550710885Z_61c697e43bb5f73e854f069f0b2d66b236c01b604c97f2b6400d3eb9f794d0d8.json |
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
| Market best home last update utc | 2026-11-05T13:36:18Z |
| Market best draw last update utc | 2026-11-05T13:34:29Z |
| Market best away last update utc | 2026-11-05T13:34:29Z |
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
| Bbs statistics cutoff utc | 2026-11-05T13:35:50.710885+00:00 |
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
| Score matrix json | [[0.050308908642355314,0.05092518656085761,0.04210293274751705,0.02115742965253173,0.00797397236291504,0.0024042328879746266,0.0006040836691907896,0.0001300980739457712,2.4516173825205684e-05,4.106596137982167e-06,6.190900245957801e-07,8.484630483960216e-08,1.0659172703515604e-08,1.2360953094566198e-09,1.3310541831823453e-10,1.3377540901137918e-11],[0.07187834556485037,0.11522418305453487,0.0687604418208325,0.034553274932779085,0.013022700010689411,0.003926475065494354,0.0009865597781370207,0.000212469784425602,4.003861094633334e-05,6.7066911115361805e-06,1.0110674207270352e-06,1.385668177231701e-07,1.7408037319716495e-08,2.018730146913774e-09,2.1738123154492808e-10,2.1847542743747402e-11],[0.0639013812948922,0.09633454663744437,0.06728508632903629,0.02821535574472185,0.010634017014978266,0.0032062631114194292,0.0008056004867186423,0.00017349760809171898,3.269454642354645e-05,5.4765192575839495e-06,8.256128257946639e-07,1.1315026040453001e-07,1.4214975765647072e-08,1.648445461640807e-09,1.7750817519318093e-10,1.7840166868757937e-11],[0.034786865776053666,0.05244294998896413,0.03953019253373207,0.018406636110482315,0.0057889847615843135,0.001745437144542214,0.00043855571558427286,9.44492573220075e-05,1.7798375794042126e-05,2.9813274216151238e-06,4.494501053329039e-07,6.159714925493373e-08,7.738400077573077e-09,8.97386720775428e-10,9.663254439056991e-11,9.711894762054047e-12],[0.014203050145387494,0.02141181252891258,0.016139692216822397,0.008110465955867925,0.002832386828284347,0.0007126405537408361,0.00017905691360897133,3.8562472013863035e-05,7.266858288890339e-06,1.2172393782646219e-06,1.835049591701703e-07,2.514935968399247e-08,3.1594937311799765e-09,3.6639197900237365e-10,3.945388131518371e-11,3.9652473781392764e-12],[0.004639144779090845,0.006993744110425143,0.005271710521146094,0.0026491229285265762,0.0009984215174033552,0.00027893992481878944,5.848539133679987e-05,1.2595667049027997e-05,2.3735752071710308e-06,3.9758711324510673e-07,5.993825724455674e-08,8.214539798225039e-09,1.0319859957921707e-09,1.19674676853945e-10,1.2886828226657002e-11,1.2951694518992084e-12],[0.001262737232558171,0.0019036398956595946,0.0014349164493254664,0.0007210695752697785,0.000271762163900286,8.193902642488754e-05,1.90768340093853e-05,3.4284374618786386e-06,6.460677411665539e-07,1.0821995755396682e-07,1.6314702963890663e-08,2.235930488373861e-09,2.8089814015693934e-10,3.2574467375743146e-11,3.5076891509668327e-12,3.5253452247411807e-13],[0.0002946057753098841,0.0004441330253923483,0.00033477643816839047,0.0001682307734320614,6.340408830231216e-05,1.9116970487309216e-05,4.803299103654748e-06,9.585358112789453e-07,1.5073230034049057e-07,2.524850275824936e-08,3.806338794564731e-09,5.216588361237251e-10,6.553557797324816e-11,7.599860025585523e-12,8.183693766383399e-13,8.224886669935333e-14],[6.014196028443873e-05,9.06670303596661e-05,6.834255447745697e-05,3.4343279535946006e-05,1.2943555354737028e-05,3.902612155505712e-06,9.805640219456759e-07,2.1117851241788944e-07,3.6874529789275494e-08,5.154326823806937e-09,7.770406957264769e-10,1.0649344864736266e-10,1.3378685884684327e-11,1.5514647645494521e-12,1.6706508382604894e-13,1.6790601166149795e-14],[1.0913432842547715e-05,1.64525489721936e-05,1.2401522581745118e-05,6.231973035727059e-06,2.348753207239089e-06,7.081727211449414e-07,1.7793433321280517e-07,3.832070824033455e-08,7.221299407680979e-09,1.120829606623693e-09,1.4100274431745851e-10,1.932442997347742e-11,2.4277125194042227e-12,2.815306723527354e-13,3.031583214193871e-14,3.046842792388858e-15],[1.782328249045357e-06,2.6869494892220576e-06,2.0253557562973206e-06,1.017775227017596e-06,3.8358683758765343e-07,1.1565529053141568e-07,2.9059361351803327e-08,6.258349852476756e-09,1.1793471508750014e-09,1.975472392084379e-10,2.759546498770989e-11,3.155970988720274e-12,3.964820846311358e-13,4.59782066327238e-14,4.951032805116962e-15,4.975953998730218e-16],[2.6461917771649525e-07,3.989267211494461e-07,3.007010493728242e-07,1.5110731921455498e-07,5.695047116022709e-08,1.7171139993644762e-08,4.314392879089137e-09,9.291663265235069e-10,1.75095621961885e-10,2.9329495297793677e-11,4.4215689479060604e-12,5.615009148357095e-13,5.886500607876697e-14,6.826304435530976e-15,7.350712364230179e-16,7.387712427294803e-17],[3.601358699318612e-08,5.429229392970982e-08,4.092418204145717e-08,2.056508765842671e-08,7.750726024963859e-09,2.3369218711571675e-09,5.871712119078732e-10,1.2645573393491645e-10,2.3829797477514035e-11,3.9916242635482e-12,6.017574361990742e-13,8.247087312476157e-14,9.600328597096308e-15,9.290320934121867e-16,1.0004018660911685e-16,1.005437423231924e-17],[4.5242785708693326e-09,6.820577523588525e-09,5.141181851048374e-09,2.583530083206463e-09,9.73700388968694e-10,2.9358046299227723e-10,7.376455258313451e-11,1.5886253355255712e-11,2.9936657544296076e-12,5.014557456315047e-13,7.559697605161767e-14,1.0360567639925397e-14,1.3015897391075788e-15,1.3986128551727775e-16,1.2567747627778141e-17,1.2631007816963455e-18],[5.277735389921835e-10,7.9564515783191e-10,5.99737548788649e-10,3.0137817416593056e-10,1.1358568933241648e-10,3.424722803985646e-11,8.604903159509777e-12,1.8531891932151113e-12,3.4922199087122713e-13,5.849663529207715e-14,8.818662017136416e-15,1.2085978711608484e-15,1.5183517375516608e-16,1.7607627844081202e-17,1.7568697551420723e-18,1.4734529698324512e-19],[5.7462254771451985e-11,8.66272395056291e-11,6.529746051745473e-11,3.281306876344594e-11,1.2366837926876396e-11,3.728726049055278e-12,9.368736799113115e-13,2.0176917123123413e-13,3.802214686540649e-14,6.368922107850939e-15,9.60147044392698e-16,1.3158817875086335e-16,1.6531316545819195e-17,1.9170608648352314e-18,2.0643326319843547e-19,1.922450518575437e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.15446467930138144, "-10": 7.728099538561398e-07, "-11": 1.0400338541272817e-07, "-12": 1.2865122920384615e-08, "-13": 1.471316707870306e-09, "-14": 1.5495296106198192e-10, "-15": 1.3377540901137918e-11, "-2": 0.08922798653348707, "-3": 0.0378659966727101, "-4": 0.01280817846787922, "-5": 0.0035833681306812622, "-6": 0.0008524213356286336, "-7": 0.00017608886901032857, "-8": 3.2113357670137515e-05, "-9": 5.2389318505330565e-06, "0": 0.2543562142828587, "1": 0.21693893313669108, "10": 2.224879996734849e-06, "11": 3.2436639850934626e-07, "12": 4.346671513432674e-08, "13": 5.3852211892186976e-09, "14": 6.144007784978125e-10, "15": 5.7462254771451985e-11, "2": 0.13542504565761196, "3": 0.06225894947368707, "4": 0.022813623219513926, "5": 0.006914373244854282, "6": 0.0017818461468543407, "7": 0.0003987514665271082, "8": 7.877902544530449e-05, "9": 1.3922657353291712e-05} |
| Raw goal margin distribution | {"-1": 0.18445628838833214, "-10": 4.916414807003589e-07, "-11": 6.111181343741461e-08, "-12": 6.979512913691527e-09, "-13": 7.368958443108687e-10, "-14": 7.181145864226864e-11, "-15": 5.835466890450607e-12, "-2": 0.10181954410649696, "-3": 0.04068103599763229, "-4": 0.01286327842160094, "-5": 0.003349986998603878, "-6": 0.0007398295653500213, "-7": 0.00014163117138683124, "-8": 2.3906756781654163e-05, "-9": 3.60656719329548e-06, "0": 0.2601507029608643, "1": 0.2003454252322167, "10": 1.0944438905336263e-06, "11": 1.4737528324908013e-07, "12": 1.8233880115134662e-08, "13": 2.085521087856369e-09, "14": 2.201692813398958e-10, "15": 1.9381754318324086e-11, "2": 0.11949236170504172, "3": 0.05171964071481304, "4": 0.01771616282853517, "5": 0.004998222821866035, "6": 0.001195800340445612, "7": 0.0002479935213608704, "8": 4.5347844613147195e-05, "9": 7.4111313896013285e-06} |
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
| Totals anchor reference last update utc | 2026-11-05T13:36:18Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5548 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.88, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.76, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.23, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.04, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:29Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.6, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:29Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 6.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:27Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.56, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:27Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.54, "price": 2.56, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.66, "under": 2.42}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:36Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.17, "under": 4.75}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.5, "draw": 4.0, "home": 2.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:29Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.66, "under": 2.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.45, "draw": 3.82, "home": 2.09}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.61, "under": 2.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:27Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.81, "home_away": 1.29, "home_draw": 1.34}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.83, "home_away": 1.29, "home_draw": 1.35}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.09 |
| Reference draw odds | 3.82 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:18Z |
| Market reference home last update utc | 2026-11-05T13:36:18Z |
| Market reference draw last update utc | 2026-11-05T13:36:18Z |
| Market reference away last update utc | 2026-11-05T13:36:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-05T13:34:29Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:34:29Z |
| Market best over 2 5 last update utc | 2026-11-05T13:34:29Z |
| Market best under 2 5 last update utc | 2026-11-05T13:34:29Z |
| Home probability edge | -2.2% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | -0.0727 |
| Raw ev home | -0.1728 |
| Raw edge prob draw | 0.0083 |
| Raw ev draw | 0.0406 |
| Raw edge prob away | 0.0644 |
| Raw ev away | 0.2043 |
| Market p home draw | 71.8% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T13:36:39Z |
| Market reference home draw last update utc | 2026-11-05T13:36:39Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.0% |
| Market draw away odds | 1.83 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T13:36:39Z |
| Market reference draw away last update utc | 2026-11-05T13:36:39Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-05T13:36:27Z |
| Market reference home away last update utc | 2026-11-05T13:36:39Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home draw odds | 1.35 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-05T13:33:36Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-11-05T13:36:20Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.7% |
| Market under 3 5 odds | 1.57 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T13:36:18Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.30 |
| Market reference under 3 5 last update utc | 2026-11-05T13:36:20Z |
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
| Market best home last update utc | 2026-11-05T13:36:18Z |
| Market best draw last update utc | 2026-11-05T13:36:18Z |
| Market best away last update utc | 2026-11-05T13:34:29Z |
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
| Bbs statistics cutoff utc | 2026-11-05T13:35:50.710885+00:00 |
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
| Score matrix json | [[0.06531210024917977,0.109179165967253,0.08815997771885496,0.04432788485242059,0.016716440608876268,0.005043135039001591,0.001267874125473257,0.00027321522124847965,5.1515947970973405e-05,8.634277022328109e-06,1.3024251396145839e-06,1.7860223006443177e-07,2.2450831129771422e-08,2.6050487976843185e-09,2.8068203669537685e-10,2.8226052965788125e-11],[0.05941138497372194,0.11525119321718887,0.10757907579398343,0.05409203822094003,0.020398589902130934,0.0061539921020648414,0.0015471501941220038,0.0003333966472688203,6.286342413835443e-05,1.0536158994657122e-05,1.5893117992544636e-06,2.1794314542988664e-07,2.7396101113476695e-08,3.178865844848885e-09,3.425081866054465e-10,3.4443437599940346e-11],[0.039467035479373615,0.05953348388228679,0.05031594269567614,0.033003476351701706,0.01244590519390748,0.003754769453860791,0.0009439713592539291,0.0002034171520572058,3.835521086232641e-05,6.4284853308286476e-06,9.696956540615197e-07,1.3297486437525756e-07,1.671533565687375e-08,1.939539111230762e-09,2.0897642626676094e-10,2.1015166292271203e-11],[0.016053494684929285,0.024215663919807104,0.01826388554597857,0.010290731183019377,0.005062459605914606,0.0015272789237537564,0.0003839669996604705,8.274135945884409e-05,1.5601252190312e-05,2.6148316902225434e-06,3.944305377740193e-07,5.4088462752492254e-08,6.7990805203667304e-09,7.88921195503222e-10,8.500263340281184e-11,8.54806691909243e-12],[0.004897404032291844,0.007387418904920504,0.005571723071747238,0.00280152859772291,0.0011838846241725208,0.000465923595231124,0.00011713596131623051,2.5241723089207652e-05,4.7594394170986385e-06,7.977009065497933e-07,1.2032804969044854e-07,1.650064741561844e-08,2.0741804205149383e-09,2.406744400423365e-10,2.5931564917959157e-11,2.6077398236014168e-12],[0.0011952321523125893,0.0018029308056968312,0.0013598025638120995,0.0006837248945651385,0.0002578387538873108,8.716708056911479e-05,2.8587526418906522e-05,6.160349200732268e-06,1.1615613048854506e-06,1.9468227762107504e-07,2.9366569077574635e-08,4.027052739590165e-09,5.062124978764599e-10,5.873761427108795e-11,6.328708014564514e-12,6.36429925218111e-13],[0.0002430845485523566,0.000366677402482837,0.0002765546356036725,0.00013905495849304023,5.2438864673050806e-05,1.5820130733913625e-05,4.456902455205495e-06,1.2528827152846172e-06,2.3623662136903508e-07,3.959419387697902e-08,5.9725294144253215e-09,8.190160340865651e-10,1.0295274962255039e-10,1.1945969174694433e-11,1.2871232820030051e-12,1.2943617753046708e-13],[4.2375579599259876e-05,6.392083556398745e-05,4.8210234029102054e-05,2.4240678798325374e-05,9.141376106713215e-06,2.7578355480758313e-06,6.933362495103716e-07,1.6742495014919338e-07,4.1181818477152704e-08,6.902235968079538e-09,1.041157889784137e-09,1.427745175585695e-10,1.7947181186851138e-11,2.0824744751044407e-12,2.24377054878218e-13,2.256389012230809e-14],[6.463712059996032e-06,9.750093795228826e-06,7.353694605620937e-06,3.697525069225542e-06,1.39436967103935e-06,4.206633882099128e-07,1.0575727624197215e-07,2.278972103504487e-08,4.815299823193028e-09,1.052824912124466e-09,1.5881186457388977e-10,2.1777952767389625e-11,2.737553387527229e-12,3.176479355954716e-13,3.4225105339398355e-14,3.441757967283012e-15],[8.763868034821939e-07,1.32197311011676e-06,9.970556932897073e-07,5.013314556923255e-07,1.8905656185363003e-07,5.703593209495489e-08,1.4339172353346177e-08,3.0899598535282143e-09,5.826257055494923e-10,1.0942623172988117e-10,2.1532614859246032e-11,2.952778563624709e-12,3.711730411856113e-13,4.306851176619462e-14,4.640434225539296e-15,4.666530989173402e-16],[1.0694295166149258e-07,1.6131656233443281e-07,1.216678279358226e-07,6.117603028647084e-08,2.3070026471492306e-08,6.959930141306451e-09,1.7497678077267706e-09,3.770588807805279e-10,7.109613291500036e-11,1.1915993609401373e-11,2.0142091895652435e-12,3.6031904399074467e-13,4.529317470760902e-14,5.255526159960206e-15,5.662587924628277e-16,5.694433051925431e-17],[1.1863581515117141e-08,1.789544946403538e-08,1.3497067100342762e-08,6.786485792650437e-09,2.5592443012680485e-09,7.72091075550901e-10,1.9410828574473477e-10,4.18285515654917e-11,7.886959871058207e-12,1.3218857280675798e-12,1.9939795763800073e-13,3.064095746364471e-14,5.024541233189506e-15,5.830151686936174e-16,6.281720523572835e-17,6.317047514055097e-18],[1.2063988369274232e-09,1.819775031022122e-09,1.372506778921401e-09,6.901127249511827e-10,2.6024766168030365e-10,7.85133708871771e-11,1.973872812877215e-11,4.25351449683782e-12,8.020191207194595e-13,1.3442158279602316e-13,2.0276630954460345e-14,2.780544844006752e-15,3.916723998840499e-16,5.92863816484748e-17,6.387835177669419e-18,6.423758933219666e-19],[1.1324105186061417e-10,1.7081684129228335e-10,1.28833107736354e-10,6.477881815180172e-11,2.4428669898258353e-11,7.369815381313513e-12,1.852815393444649e-12,3.99264688411883e-13,7.528313693828627e-14,1.2617752075556796e-14,1.9033067234386884e-15,2.6100143107140163e-16,3.280865558900801e-17,4.265985683471726e-18,5.996069894048113e-19,6.029790449313687e-20],[9.870341894622315e-12,1.488877573293437e-11,1.122938015685108e-11,5.6462658389543955e-12,2.12925719043538e-12,6.423694969148458e-13,1.614955098035298e-13,3.4800798088010266e-14,6.5618456228681436e-15,1.0997913290369399e-15,1.6589644640352534e-16,2.274946512181277e-17,2.8596753778392877e-18,3.3181817910201947e-19,4.0063275311210077e-20,5.255699440244637e-21],[8.029662183599554e-13,1.2112228810227293e-12,9.135258955908803e-13,4.593316803980572e-13,1.7321807211674729e-13,5.225766353732144e-14,1.3137887235669603e-14,2.8310939514529584e-15,5.33815385678479e-16,8.946957399145416e-17,1.34959096280718e-17,1.8507010368633927e-18,2.3263862066741046e-19,2.6993876331862374e-20,2.9084661269552175e-21,3.277532920589696e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2553199839797595, "-10": 1.5378991098916906e-06, "-11": 2.0802548066236564e-07, "-12": 2.584722146780616e-08, "-13": 2.9685721505820362e-09, "-14": 3.151254742953172e-10, "-15": 2.8226052965788125e-11, "-2": 0.15634873966864105, "-3": 0.06889165514997311, "-4": 0.023902105669433727, "-5": 0.0068101315421323005, "-6": 0.001642365275466972, "-7": 0.00034291858028913825, "-8": 6.307802531016649e-05, "-9": 1.036360989906243e-05, "0": 0.24244564830398246, "1": 0.14028465860504588, "10": 1.262778682374551e-07, "11": 1.3818009137786689e-08, "12": 1.3889043900569559e-09, "13": 1.2904335348913944e-10, "14": 1.1081564775645044e-11, "15": 8.029662183599554e-13, "2": 0.06999345298538888, "3": 0.02494934787590439, "4": 0.007002583350404971, "5": 0.0016140135288239452, "6": 0.00031488427243984843, "7": 5.318654476388704e-05, "8": 7.91440726564493e-06, "9": 1.051915629819203e-06} |
| Raw goal margin distribution | {"-1": 0.2151664828042469, "-10": 1.2960377688626581e-06, "-11": 1.753098614142654e-07, "-12": 2.1782297048597498e-08, "-13": 2.5017126299131055e-09, "-14": 2.6556652123054624e-10, "-15": 2.3787015984524245e-11, "-2": 0.13176018532119765, "-3": 0.05805724605700234, "-4": 0.020143084486936254, "-5": 0.005739120097512743, "-6": 0.0013840748158204135, "-7": 0.00028898867867267644, "-8": 5.3157910464625966e-05, "-9": 8.73375227578471e-06, "0": 0.266534076859324, "1": 0.17282081463795607, "10": 1.5556543585412777e-07, "11": 1.702281361064752e-08, "12": 1.7110323433131478e-09, "13": 1.5897231882207148e-10, "14": 1.3651706972335823e-11, "15": 9.891978022658497e-13, "2": 0.08622700218641936, "3": 0.03073583859756755, "4": 0.008626689270380744, "5": 0.001988350940592469, "6": 0.0003879152362122749, "7": 6.552207550899267e-05, "8": 9.749992084851666e-06, "9": 1.2958859356643466e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:29Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.36, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:29Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.09, "price": 1.36, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.79, "draw": 4.11, "home": 4.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.87, "draw": 4.04, "home": 4.3}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:29Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.77, "under": 2.22}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.33 |
| Reference draw odds | 4.11 |
| Reference away odds | 1.79 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:18Z |
| Market reference home last update utc | 2026-11-05T13:36:18Z |
| Market reference draw last update utc | 2026-11-05T13:36:18Z |
| Market reference away last update utc | 2026-11-05T13:36:18Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-05T13:34:29Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:34:29Z |
| Market best over 2 5 last update utc | 2026-11-05T13:34:29Z |
| Market best under 2 5 last update utc | 2026-11-05T13:34:29Z |
| Home probability edge | +2.4% |
| Draw probability edge | +1.0% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0809 |
| Raw ev home | 0.3027 |
| Raw edge prob draw | 0.0344 |
| Raw ev draw | 0.0955 |
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
| 1 | 3-0 | 12.40% |
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
| Market best home last update utc | 2026-11-05T13:34:29Z |
| Market best draw last update utc | 2026-11-05T13:36:18Z |
| Market best away last update utc | 2026-11-05T13:34:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris SG |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.3342 |
| Dc lambda away | 0.5756 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_CHRONOLOGICAL_PARTITIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:35:50.710885+00:00 |
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
| Fair Under 0.5 odds | 51.62 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.37 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 4.04 |
| Fair Over 3.5 odds | 1.82 |
| Fair Under 3.5 odds | 2.22 |
| Fair Over 4.5 odds | 2.82 |
| Fair Under 4.5 odds | 1.55 |
| Score matrix json | [[0.01937057838370203,0.012182239465052126,0.004276521860743266,0.0008204595628102609,0.00011805514787368733,1.3589474554227386e-05,1.3035843980983094e-06,1.0718372682061465e-07,7.711282367237673e-09,4.931418230164805e-10,2.8383083568189926e-11,1.4850963487193727e-12,7.122970141848184e-14,3.1535920430344983e-15,1.2964781894343426e-16,4.974640435072926e-18,1.7894907281273684e-19,6.0585440620494106e-21,1.9372403455736653e-22,5.868372102663722e-24,1.6887889854920306e-25,4.628537989630794e-27],[0.06486561404501584,0.03549915167320906,0.014258646251927739,0.0027355507702442926,0.0003936158042829146,4.530960362836181e-05,4.346370578071925e-06,3.573686501471043e-07,2.5710717962765193e-08,1.6442181369325824e-09,9.463399494171762e-11,4.9515620815132984e-12,2.3749185628623175e-13,1.0514608560122697e-14,4.322677278041823e-16,1.6586291501363382e-17,5.966464359201959e-19,2.020020928116237e-20,6.459086540877946e-22,1.9566143845695323e-23,5.630707739232197e-25,1.5432327486403625e-26],[0.11160874409413135,0.06423710508241726,0.016157358706660935,0.004560394171622758,0.0006561907895242993,7.553493598178256e-05,7.245766836994863e-06,5.957637222379194e-07,4.286193830544774e-08,2.7410505007275594e-09,1.5776286211315546e-10,8.25467218615904e-12,3.959189823842607e-13,1.75287405066864e-14,7.206268104769124e-16,2.765074876855558e-17,9.946599999118148e-19,3.3675454929738395e-20,1.0767842781582255e-21,3.2618414297268927e-23,9.386865356482685e-25,2.5726993294766698e-26],[0.1240408017294349,0.07139245298272263,0.020545184615977746,0.0034451108084548074,0.0007292836442225039,8.394874517949632e-05,8.052870184144055e-06,6.621256277678127e-07,4.763631410995222e-08,3.0463751245543636e-09,1.7533601026046384e-10,9.174157135226418e-12,4.4002025462651933e-13,1.9481260571508666e-14,8.008971702422547e-16,3.073075567249545e-17,1.1054548175293793e-18,3.7426551673811403e-20,1.1967268894249689e-21,3.6251767667627116e-23,1.0432464893273488e-24,2.859271377231148e-26],[0.10339324632600633,0.059508624373143165,0.01712527897430529,0.0032855201862151263,0.0004131983229828293,6.997482415532549e-05,6.712407360899695e-06,5.519096714634798e-07,3.970687943130678e-08,2.5392823108440457e-09,1.4614996876771557e-10,7.647047385141688e-12,3.667754637241735e-13,1.6238453355087703e-14,6.67581612260804e-16,2.5615382573560488e-17,9.214432723548166e-19,3.1196611295564683e-20,9.97522398582733e-22,3.021737921678297e-23,8.69590003820232e-25,2.3833234362980307e-26],[0.06894610958189863,0.039682361110532034,0.01141971456298159,0.002190895854822879,0.0003152459253824043,3.171712978461082e-05,4.476059993354977e-06,3.6803201408387923e-07,2.6477888621411065e-08,1.693279229388065e-09,9.7457736555424e-11,5.099309536442477e-12,2.445782699785293e-13,1.0828349280477335e-14,4.451659719501121e-16,1.7081202463944093e-17,6.144495031035591e-19,2.0802954326301016e-20,6.651816346517458e-22,2.014996929479405e-23,5.798719918868919e-25,1.5892805830856274e-26],[0.03831299589506747,0.022051282480680494,0.006345876218797196,0.0012174694758177792,0.00017518052749250133,2.016524788315546e-05,1.69070063705833e-06,2.0451348350699473e-07,1.471362552889442e-08,9.409464951417702e-10,5.415675928973428e-11,2.833659890632788e-12,1.359108775032358e-13,6.017257595085619e-15,2.4737642427363615e-16,9.491935714030824e-18,3.414464055026762e-19,1.1560093942096775e-20,3.696379881683354e-22,1.1197233543107198e-23,3.222318616605443e-25,8.831549861931063e-27],[0.018248857135650356,0.010503242940070249,0.0030226033180626353,0.000579892697299459,8.344020989416015e-05,9.604906093288729e-06,9.21360548448551e-07,6.621341295034636e-08,7.00824469481961e-09,4.48182079239169e-10,2.57953976221265e-11,1.3497001032445435e-12,6.473568899519904e-14,2.8660790323437353e-15,1.178278262984598e-16,4.521102428547654e-18,1.626342844753071e-19,5.506186553560031e-21,1.760622128446395e-22,5.333352573166491e-24,1.5348220807642392e-25,4.206554145704421e-27],[0.007605596524238914,0.00437744826453694,0.0012597337531400925,0.00024168252566327705,3.477546926010133e-05,4.003047415832297e-06,3.8399646250512574e-07,3.157307804333499e-08,1.985369463509639e-09,1.8678934460111954e-10,1.0750776612357658e-11,5.625160160823281e-13,2.697996524145349e-14,1.1944989521564737e-15,4.9107234469138454e-17,1.884264897285838e-18,6.778127197407073e-20,2.2948195058065345e-21,7.337764464411652e-23,2.222787295198479e-24,6.396695089459157e-26,1.7531702589249383e-27],[0.0028175937233661163,0.001621683547794224,0.0004666850134171631,8.953448492644871e-05,1.2883032067517934e-05,1.4829818065210486e-06,1.422565631901574e-07,1.1696663928823308e-08,8.415109362710894e-10,4.703613808895251e-11,3.982767243536025e-12,2.0839149054979423e-13,9.995084603644875e-15,4.425179194606669e-16,1.8192423851455716e-17,6.980508275493821e-19,2.5110467780832566e-20,8.50146206837558e-22,2.7183717980009627e-23,8.23460922673111e-25,2.3697402139210325e-26,6.494850866458986e-28],[0.0009394333407229877,0.0005406966874840233,0.00015560066647794338,2.985230964522428e-05,4.295420504901914e-06,4.944511840646422e-07,4.743074109273746e-08,3.899865327937041e-09,2.8057396052530746e-10,1.7942898184127617e-11,9.026242444334514e-13,6.948124299182286e-14,3.3325300387144965e-15,1.475429491346515e-16,6.065661409198443e-18,2.327419370226754e-19,8.372254111313997e-21,2.8345310559474376e-22,9.063510748002076e-24,2.745557811001395e-25,7.901114157614732e-27,2.165492986577871e-28],[0.000284748131113423,0.00016388855343563255,4.7163536846051035e-05,9.048422077882531e-06,1.3019688658013654e-06,1.4987125162161148e-07,1.4376554778317269e-08,1.1820736135141683e-09,8.504372522821794e-11,5.438604851682957e-12,3.130222763412256e-13,1.4315184900552734e-14,1.0101107330010222e-15,4.472119223778239e-17,1.8385399744348296e-18,7.054553923743142e-20,2.537682673225776e-21,8.591641213657857e-23,2.7472068905217028e-24,8.321957734061692e-26,2.3948772015725308e-27,6.563744910231979e-29],[7.911653061089456e-05,4.5536010030916126e-05,1.3104266539021897e-05,2.514080635071606e-06,3.617486767088729e-07,4.164133903267383e-08,3.994488503753774e-09,3.2843609144065716e-10,2.3629178755181077e-11,1.5111022697365508e-12,8.697242862035783e-14,4.550683715285511e-15,1.9076988046626175e-16,1.24256674163275e-17,5.108335692949157e-19,1.9600895334119383e-20,7.050885570765366e-22,2.3871652552038195e-23,7.6330431809522375e-25,2.31223439899313e-26,6.654104267046928e-28,1.8237195204123047e-29],[2.0291375155123288e-05,1.1678826857930255e-05,3.3609106266776413e-06,6.44797654075137e-07,9.277932252957464e-08,1.0679942936695332e-08,1.0244845692378433e-09,8.423549281604928e-11,6.060282560757591e-12,3.875592473055229e-13,2.2306212919867928e-14,1.1671344757684957e-15,5.597929070116892e-17,2.1661994475066627e-18,1.3101580057109386e-19,5.02713045592211e-21,1.8083725763442944e-22,6.1224709143080354e-24,1.9576811769173992e-25,5.930292351582191e-27,1.706608277200709e-28,4.6773761034096464e-30],[4.832490877323972e-06,2.7813701051475744e-06,8.004174097988683e-07,1.5356173532927146e-07,2.2095852365888783e-08,2.543480982307392e-09,2.439860431810628e-10,2.0061097262679523e-11,1.4432861235366912e-12,9.229914250309493e-14,5.312334409020633e-15,2.7795882061435777e-16,1.3331743638092614e-17,5.902436739115106e-19,2.120887864573812e-20,1.1972358640871768e-21,4.3067283075588843e-23,1.4580965860564007e-24,4.6623140895276134e-26,1.4123283153458082e-27,4.064371619808976e-29,1.1139401433733397e-30],[1.0741560576434498e-06,6.182371830253897e-07,1.7791512311241857e-07,3.4133384296737474e-08,4.911420273752879e-09,5.653596817878144e-10,5.4232712056049084e-11,4.4591391261175895e-12,3.208106485589824e-13,2.0516062120306986e-14,1.1808146834696445e-15,6.178411062074835e-17,2.963352347958641e-18,1.311981406509895e-19,5.393707414503595e-21,1.8088832063254573e-22,9.572906431953026e-24,3.241026874755374e-25,1.0363295139163801e-26,3.1392941110944264e-28,9.03420100887911e-30,2.476043066053923e-31],[2.2383860857081712e-07,1.2883169985443564e-07,3.7074942060614876e-08,7.1129043051310525e-09,1.0234690502934947e-09,1.1781279229673206e-10,1.1301313919208273e-11,9.292201913412885e-13,6.685230574939439e-14,4.2752510360894934e-15,2.460647257417129e-16,1.2874916316605e-17,6.175198301514423e-19,2.733979764059931e-20,1.1239707248398126e-21,4.312722158531553e-23,1.3559569431903076e-24,6.753831911328053e-26,2.1595610318003985e-27,6.541835524938088e-29,1.8825970109157196e-30,5.159716139225086e-32],[4.390092533226621e-08,2.5267449935693932e-08,7.271418784691958e-09,1.39503673110227e-09,2.007305113434217e-10,2.3106338226581227e-11,2.216499386283029e-12,1.8224571041506418e-13,1.311158115989392e-14,8.384946534041684e-16,4.826007997755161e-17,2.525126221447315e-18,1.2111267188339108e-19,5.362088437212077e-21,2.2044166188262696e-22,8.458437740895956e-24,3.042691448624071e-25,9.003749304747598e-27,4.235494860018599e-28,1.2830343913856701e-29,3.6922920194444843e-31,1.0119626565322628e-32],[8.131838920980357e-09,4.680330340781723e-09,1.3468965821694535e-09,2.5840489466487165e-10,3.718163506615235e-11,4.280024147330427e-12,4.105657418673589e-13,3.3757665696529227e-14,2.428679240463614e-15,1.5531571159331578e-16,8.939292138396954e-18,4.677331863176323e-19,2.2433894766255106e-20,9.932282547906156e-22,4.083276314417954e-23,1.5667700102337745e-24,5.636026247553831e-26,1.9081469838854344e-27,5.332780666271725e-29,2.3765852136055086e-30,6.839291819955332e-32,1.8744746846872292e-33],[1.4269960290108593e-09,8.213164175599997e-10,2.363568797809382e-10,4.534555617086502e-11,6.524729044329588e-12,7.510696561577724e-13,7.20471333711547e-14,5.9238820844493285e-15,4.2619088567298717e-16,2.725520092568898e-17,1.5686899983654088e-18,8.207902369903204e-20,3.936757608921513e-21,1.7429425118478905e-22,7.165438399173367e-24,2.7494083499471965e-25,9.890243956886805e-27,3.348465451951296e-28,1.0706833692788787e-29,2.834796302738554e-31,1.200176536102133e-32,3.289376434435795e-34],[2.378922900798066e-10,1.3692038343577208e-10,3.940268806927216e-11,7.559487190659517e-12,1.0877274378834182e-12,1.2520965502383026e-13,1.201086562464346e-14,9.875611750715426e-16,7.104962014096566e-17,4.543672184772474e-18,2.6151387148225576e-19,1.3683266469081993e-20,6.562907422556783e-22,2.905632371719724e-23,1.1945390986033107e-24,4.583495927363254e-26,1.6487871980853746e-27,5.582174711235629e-29,1.7849196037684098e-30,5.406955534549503e-32,1.3599946630626474e-33,5.483668328529911e-35],[3.7770146603596714e-11,2.1738842203145313e-11,6.2559627487420185e-12,1.2002193906470696e-12,1.7269842910768094e-13,1.9879530458298256e-14,1.9069645145990036e-15,1.5679503673683213e-16,1.1280544518504022e-17,7.213985979956249e-19,4.152054386228885e-20,2.1724915102541866e-21,1.0419924723606844e-22,4.613271015180587e-24,1.8965691096100448e-25,7.277214115489897e-27,2.617778582438567e-28,8.86281590460661e-30,2.8339159325991646e-31,8.584620508321327e-33,2.47046579621313e-34,5.917986258467062e-36]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.031805226129544624, "-10": 3.375073090250052e-11, "-11": 1.7409440842530124e-12, "-12": 8.249661016601657e-14, "-13": 3.614647847570165e-15, "-14": 1.4726721499518958e-16, "-15": 5.606189858895043e-18, "-16": 2.002632036225347e-19, "-17": 6.738138210158164e-21, "-18": 2.1425745765248246e-22, "-19": 6.457169869881708e-24, "-2": 0.007759307777836491, "-20": 1.843112260356067e-25, "-21": 4.628537989630794e-27, "-3": 0.00129824252813374, "-4": 0.0001713140996593605, "-5": 1.858188480830309e-05, "-6": 1.7070127497804901e-06, "-7": 1.358187290570181e-07, "-8": 9.522815379197808e-09, "-9": 5.96487203675203e-10, "0": 0.07491887397216701, "1": 0.1532697888962895, "10": 0.0011170936310497808, "11": 0.00033380364499009993, "12": 9.163095525487035e-05, "13": 2.325797837126988e-05, "14": 5.489235984013463e-06, "15": 1.2105242330229061e-06, "16": 2.5049940825181977e-07, "17": 4.8825344738448636e-08, "18": 8.993758246000277e-09, "19": 1.5701723751953733e-09, "2": 0.2025025533187951, "20": 2.5963113228295193e-10, "21": 3.7770146603596714e-11, "3": 0.19627419964169335, "4": 0.15003768344053844, "5": 0.09427507010070126, "6": 0.05016995644514882, "7": 0.023124187378325316, "8": 0.00939230183772149, "9": 0.0034080634063099746} |
| Raw goal margin distribution | {"-1": 0.02469341924443515, "-10": 2.6203899465672217e-11, "-11": 1.3516603208063525e-12, "-12": 6.404995747481407e-14, "-13": 2.806394595576584e-15, "-14": 1.1433753264399914e-16, "-15": 4.352617899515564e-18, "-16": 1.5548335440669094e-19, "-17": 5.2314569647351765e-21, "-18": 1.6634842357384964e-22, "-19": 5.013314543970725e-24, "-2": 0.006024287933822851, "-20": 1.4309831841520224e-25, "-21": 3.5935738548507745e-27, "-3": 0.0010079490363497955, "-4": 0.0001330074141947974, "-5": 1.442688286680634e-05, "-6": 1.325316201627938e-06, "-7": 1.0544898515077191e-07, "-8": 7.393466456993653e-09, "-9": 4.6310969569275177e-10, "0": 0.08557354308137319, "1": 0.15301411469102794, "10": 0.0011152301716663097, "11": 0.0003332468165227234, "12": 9.147810274668297e-05, "13": 2.3219180998487637e-05, "14": 5.480079215038883e-06, "15": 1.2085049190833704e-06, "16": 2.500815422288775e-07, "17": 4.8743897629383523e-08, "18": 8.978755472078426e-09, "19": 1.567553120761459e-09, "2": 0.202164752374747, "20": 2.5919803334097764e-10, "21": 3.770714102183773e-11, "3": 0.19594678841233037, "4": 0.14978740081309316, "5": 0.0941178068605184, "6": 0.05008626634656848, "7": 0.023085613186549836, "8": 0.0093766342405699, "9": 0.003402378307445} |
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
| Unanchored p over 2 5 | 0.7522 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:29Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:29Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:18Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 17.6, "draw": 11.64, "home": 1.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:29Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 22.0, "draw": 11.1, "home": 1.14}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.12 |
| Reference draw odds | 11.64 |
| Reference away odds | 17.60 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:18Z |
| Market reference home last update utc | 2026-11-05T13:36:18Z |
| Market reference draw last update utc | 2026-11-05T13:36:18Z |
| Market reference away last update utc | 2026-11-05T13:36:18Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.02 |
| Market reference over 2 5 last update utc | 2026-11-05T13:35:35Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:35:35Z |
| Home probability edge | -0.1% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | -0.0021 |
| Raw ev home | 0.0061 |
| Raw edge prob draw | 0.0152 |
| Raw ev draw | -0.0039 |
| Raw edge prob away | -0.0131 |
| Raw ev away | -0.2988 |
| Count model | {"corners": {"alpha": 0.015413236227799179, "mu": 9.410650896644807, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,662.7279 |
| Elo away rating | 1,413.0859 |
| Elo rating diff | 309.6419 |
| Elo home expectancy | 0.8560 |

</details>


---
