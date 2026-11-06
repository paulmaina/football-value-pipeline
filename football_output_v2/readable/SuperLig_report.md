# Super Lig — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,840 |
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
| Training sha256 | 428b36b889bc8107b0a0c389334f72426054f163962dc5b037f54c55da735d9c |
| Training as of utc | 2026-11-06T11:25:21.293828+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-06', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1809, 'tune_start_date': '2025-11-07', 'audit_start_date': '2026-05-08', 'training_shot_matches': 1512, 'tuning_matches': 189, 'audit_matches': 91, 'audit_matchdays': 37, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8325620265193853, 'audit_candidate_poisson_score': 0.8249817971906659, 'audit_gain': 0.007580229328719379, 'audit_gain_lower95': -0.0033651228584291974, 'audit_baseline_briers': [0.5922471728635237, 0.16648912404164234, 0.22016596584554815, 0.2497288421028269], 'audit_candidate_briers': [0.5910954568612793, 0.16507580357810983, 0.21632000266714047, 0.2493762091936257], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1669.874 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1840, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 33.00 |
| Over 1 5 in window quote fixtures | 6 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 4, 'ANCHORED_MAIN': 2, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 9} |
| Legacy comparison status | {'None': 9} |
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

## 2026-11-06 — Gazişehir Gaziantep vs Kasimpasa SK

The model's most likely 1X2 outcome is **Kasimpasa SK win** at **36.5%**. Expected goals are 1.39 for Gazişehir Gaziantep and 1.41 for Kasimpasa SK (2.81 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 53.1%; Under 3.5 goals: 69.2%; Double Chance 1X: 63.5%; Double Chance X2: 63.8%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 84.8%; BTTS Yes (both teams score): 57.8%; BTTS No (at least one team does not score): 42.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gazişehir Gaziantep win | 36.2% | 2.76 |
| Draw | 27.3% | 3.66 |
| Kasimpasa SK win | 36.5% | 2.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gazişehir Gaziantep expected goals | 1.39 |
| Kasimpasa SK expected goals | 1.41 |
| Expected total goals | 2.81 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.1% |
| Under 2.5 | 46.9% |
| Over 3.5 | 30.8% |
| Under 3.5 | 69.2% |
| Over 4.5 | 15.2% |
| Under 4.5 | 84.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.95% |
| 2 | 2-1 | 8.39% |
| 3 | 1-2 | 8.36% |
| 4 | 1-0 | 7.41% |
| 5 | 0-1 | 7.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Gazişehir Gaziantep win | 36.2% | 36.4% | 2.67 | -3.4% |
| Draw | 27.3% | 27.2% | 3.54 | -3.3% |
| Kasimpasa SK win | 36.5% | 36.4% | 2.71 | -1.1% |
| Over 2.5 | 53.1% | 52.5% | 1.86 | -1.2% |
| Under 2.5 | 46.9% | 47.5% | 2.03 | -4.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T17:00:00+00:00 |
| Fixture id | 51baab3ec98943f452377895491bfd6a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T11:23:33Z |
| Market best draw last update utc | 2026-11-06T11:25:08Z |
| Market best away last update utc | 2026-11-06T11:23:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Gaziantep |
| Matched away-team name | Kasimpasa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3919 |
| Dc lambda away | 1.4143 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.8% |
| P btts no | 42.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.94 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.55 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.25 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.57 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.0717436346139766,0.074004811013672,0.06023487044944469,0.02830860905978996,0.009978157264893019,0.0028136634249362464,0.0006611693303897874,0.00013317001993319735,2.346974023089355e-05,3.676694778145274e-06,5.183813677861661e-07,6.644288829124889e-08,7.806548496766984e-09,8.466570220576306e-10,8.5265095733891e-11],[0.0740901255451178,0.1294630894908917,0.08358196829737317,0.03928105509854065,0.013845701301548672,0.0039042422674400853,0.000917439244070693,0.00018478685686821572,3.2566635725937936e-05,5.101785462359019e-06,7.193065200433531e-07,9.219622025096047e-08,1.0832374737425862e-08,1.1748221561423088e-09,1.1831393469143367e-10],[0.05949794160206807,0.08388682283738615,0.05774814345610692,0.027253216263569312,0.009606154695827093,0.0027087652964766186,0.0006365198201682992,0.00012820521649078124,2.2594748643827606e-05,3.539621382043015e-06,4.990552341672017e-07,6.396578510632833e-08,7.515507173280067e-09,8.150922171581037e-10,8.208626884004572e-11],[0.027519801689824788,0.03880048060005642,0.02735261888445934,0.012553127382925963,0.004443170051142609,0.001252895172103314,0.0002944118527634183,5.929923016537971e-05,1.0450832166065393e-05,1.6371940922322847e-06,2.3082985237380197e-07,2.958632977311129e-08,3.476175165695718e-09,3.770076001138658e-10,3.7967663739432325e-11],[0.009546626294811497,0.013459896714473028,0.009488630536566909,0.004459375945664276,0.0015349292840315008,0.0004346296579261442,0.00010213154755888489,2.0570918218796853e-05,3.625396370356508e-06,5.679430523074485e-07,8.007493524613492e-08,1.0263505419204452e-08,1.2058860603807187e-09,1.3078403358995005e-10,1.3170992331003729e-11],[0.002649381696568952,0.0037353933098244886,0.002633286701789973,0.0012375669313654722,0.00043621491401836364,0.00012011708433043198,2.8343568124357366e-05,5.7088454630425335e-06,1.00612074777142e-06,1.576156729099835e-07,2.2222412530210273e-08,2.848330138894731e-09,3.3465774796869243e-10,3.6295211951995066e-11,3.655216505790785e-12],[0.0006127141286489038,0.0008638726008993136,0.0006089918900924958,0.0002862081915106031,0.00010088204402278062,2.844694766421377e-05,6.52767764565302e-06,1.3202666410843148e-06,2.3268236437380603e-07,3.6451278354310854e-08,5.139307087218682e-09,6.587243059078318e-10,7.739523931481397e-11,8.393878916765272e-12,8.453303649183735e-13],[0.0001214575366014645,0.00017124435872581934,0.00012071968202203571,5.673468306123779e-05,1.9997718318241282e-05,5.6390019840819125e-06,1.3250821448079206e-06,2.606267798896784e-07,4.612432693492028e-08,7.2256902001778274e-09,1.0187582584858447e-09,1.3057807508290744e-10,1.534195911654034e-11,1.6639078619084222e-12,1.6756875504699752e-13],[2.1066825366174262e-05,2.9702356075743402e-05,2.0938844394343236e-05,9.840638083894169e-06,3.4686068178271728e-06,9.780856203922996e-07,2.298356686757263e-07,4.629255951854566e-08,7.967012212423174e-09,1.253296895825463e-09,1.7670375114137072e-10,2.264878394042476e-11,2.661064784671776e-12,2.886050329445465e-13,2.9064822144266706e-14],[3.2480387315401136e-06,4.579446654877272e-06,3.2283068950539774e-06,1.5172088382560792e-06,5.347824882469559e-07,1.5079917940068575e-07,3.5435578962306037e-08,7.137289253832536e-09,1.25786813596804e-09,1.924273870377828e-10,2.7243811905192873e-11,3.4919417701587267e-12,4.102773596647037e-13,4.449651567465999e-14,4.481153017078754e-15],[4.50698189043301e-07,6.354444896643619e-07,4.4796019737945675e-07,2.1052805471881437e-07,7.420647316932918e-08,2.0924909670913368e-08,4.917044587839449e-09,9.90370992237292e-10,1.7454191214870577e-10,2.7343180224888465e-11,3.764638689997721e-12,4.84542199812053e-13,5.693012869913351e-14,6.174341099620115e-15,6.218052543559628e-16],[5.685357013489292e-08,8.015849350682237e-08,5.650818467545819e-08,2.655717687645009e-08,9.360816238802711e-09,2.639584201717916e-09,6.202632851144379e-10,1.2493089174875014e-10,2.201768519391893e-11,3.449220459320193e-12,4.863095055174528e-13,6.086874529015418e-14,7.181482294515503e-15,7.788656428576828e-16,7.843796469165581e-17],[6.57417270808751e-09,9.269000681639497e-09,6.534234606473158e-09,3.0708971663656056e-09,1.0824231881401278e-09,3.052241464952914e-10,7.17231644583285e-11,1.4446186175872157e-11,2.545980221711487e-12,3.9884515526533316e-13,5.6233630909560335e-14,7.207675832740355e-15,8.269671840694693e-16,9.006289737642094e-17,9.070050051919869e-18],[7.017176017924555e-10,9.893596073816633e-10,6.97454667104036e-10,3.277830824679083e-10,1.1553627162423552e-10,3.2579180012161924e-11,7.655625915447765e-12,1.5419648324586421e-12,2.7175421375720693e-13,4.2572149875987664e-14,6.002295706864402e-15,7.693368009066726e-16,9.03913902763997e-17,9.57321891259511e-18,9.68123907475238e-19],[6.955029051764892e-11,9.805974361203711e-11,6.912777247722926e-11,3.2488010211202026e-11,1.145130353901003e-11,3.229064553724587e-12,7.587824577205278e-13,1.528308564464592e-13,2.6934744786121475e-14,4.219511359373837e-15,5.949136933702385e-16,7.62523241148559e-17,8.95908473431338e-18,9.71655015613766e-19,9.555608264564554e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18974750652380812, "-10": 6.184832738028515e-07, "-11": 7.812832290957227e-08, "-12": 9.06345692174934e-09, "-13": 9.649709567490644e-10, "-14": 8.5265095733891e-11, "-2": 0.11048305589724566, "-3": 0.04517910204264717, "-4": 0.014582006867301394, "-5": 0.003870349557487975, "-6": 0.0008702711323476601, "-7": 0.00016951771361816697, "-8": 2.9101410283795576e-05, "-9": 4.463577697710747e-06, "0": 0.2731698377799546, "1": 0.19025497773471942, "10": 5.377301515426035e-07, "11": 6.685251349384766e-08, "12": 7.632660087946402e-09, "13": 7.997773454044926e-10, "14": 6.955029051764892e-11, "2": 0.10913137786706979, "3": 0.04392020554990959, "4": 0.013951370628351575, "5": 0.003644370959957559, "6": 0.0008064914599567575, "7": 0.00015460840147582278, "8": 2.6121905156458053e-05, "9": 3.943181068382478e-06} |
| Raw goal margin distribution | {"-1": 0.19072635666368867, "-10": 6.369058768065023e-07, "-11": 8.06986404486041e-08, "-12": 9.389985220582014e-09, "-13": 1.002689178306871e-09, "-14": 8.880568876256016e-11, "-2": 0.1112527014035036, "-3": 0.045601412525271556, "-4": 0.014756790809735005, "-5": 0.003927549667568104, "-6": 0.0008856504223665956, "-7": 0.0001730155766342285, "-8": 2.9789596832857975e-05, "-9": 4.582760935170927e-06, "0": 0.27542284722629856, "1": 0.18752667458468233, "10": 5.430043926078965e-07, "11": 6.771222945767659e-08, "12": 7.754228822927454e-09, "13": 8.149159917018445e-10, "14": 7.103299201772632e-11, "2": 0.1077596525719733, "3": 0.04347070878130605, "4": 0.013844687439448305, "5": 0.003626483694526212, "6": 0.0008048207892027681, "7": 0.00015473724674912738, "8": 2.622086985142602e-05, "9": 3.9699266289878856e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 27.5% |
| Unadjusted away-win probability | 36.7% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 58.0% |
| P home draw | 63.5% |
| P draw away | 63.8% |
| P home away | 72.7% |
| Raw p home draw | 63.3% |
| Raw p draw away | 64.3% |
| Raw p home away | 72.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9969 |
| Totals anchor target over 2 5 | 0.5310 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.06 |
| Totals anchor reference last update utc | 2026-11-06T11:25:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5329 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.53, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.54, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.71, "draw": 3.48, "home": 2.67}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.86, "under": 2.03}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.51, "home_away": 1.33, "home_draw": 1.5}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.67, "draw": 3.54, "home": 2.67}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.26, "under": 4.05}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.67 |
| Reference draw odds | 3.54 |
| Reference away odds | 2.67 |
| Market reference 1x2 last update utc | 2026-11-06T11:25:08Z |
| Market reference home last update utc | 2026-11-06T11:25:08Z |
| Market reference draw last update utc | 2026-11-06T11:25:08Z |
| Market reference away last update utc | 2026-11-06T11:25:08Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-11-06T11:25:06Z |
| Market reference under 2 5 last update utc | 2026-11-06T11:25:06Z |
| Market best over 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market best under 2 5 last update utc | 2026-11-06T11:23:33Z |
| Home probability edge | -0.2% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | -0.0067 |
| Raw ev home | -0.0462 |
| Raw edge prob draw | 0.0032 |
| Raw ev draw | -0.0250 |
| Raw edge prob away | 0.0035 |
| Raw ev away | -0.0045 |
| Market p home draw | 64.9% |
| Market home draw odds | 1.50 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T11:23:33Z |
| Market reference home draw last update utc | 2026-11-06T11:25:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.2% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T11:23:33Z |
| Market reference draw away last update utc | 2026-11-06T11:25:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.8% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T11:23:33Z |
| Market reference home away last update utc | 2026-11-06T11:25:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home draw odds | 1.46 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 77.9% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 4.05 |
| Market reference over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.9% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 3.09 |
| Market reference under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,396.7846 |
| Elo away rating | 1,500.7901 |
| Elo rating diff | -44.0056 |
| Elo home expectancy | 0.4370 |
| Research p home | 0.3687 |
| Research p draw | 0.2525 |
| Research p away | 0.3788 |
| Research p over 1 5 | 0.7700 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.3919183862420723, 1.4142981162779908], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T11:26:28.848889+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-06T11:26:28.849834+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T11:26:28.850819+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Gazi%C5%9Fehir+Gaziantep%22+%22Kasimpasa+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T11:25:35.001023+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T11:25:35.083842+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T11:26:28.908664+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Gazi%C5%9Fehir+Gaziantep_vs_Kasimpasa+SK&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.3919183862420723, 1.4142981162779908], "h2h": [], "margin_distribution": {"-1": 0.20220549263839285, "-10": 6.369058768065023e-07, "-11": 8.069864044860409e-08, "-12": 9.389985220582014e-09, "-13": 1.0026891783068707e-09, "-14": 8.880568876256016e-11, "-2": 0.11125270140350359, "-3": 0.045601412525271556, "-4": 0.014756790809735004, "-5": 0.003927549667568104, "-6": 0.0008856504223665956, "-7": 0.0001730155766342285, "-8": 2.9789596832857975e-05, "-9": 4.582760935170926e-06, "0": 0.25246457527689015, "1": 0.19900581055938654, "10": 5.430043926078964e-07, "11": 6.771222945767659e-08, "12": 7.754228822927454e-09, "13": 8.149159917018444e-10, "14": 7.103299201772631e-11, "2": 0.10775965257197329, "3": 0.043470708781306044, "4": 0.013844687439448304, "5": 0.0036264836945262115, "6": 0.000804820789202768, "7": 0.00015473724674912738, "8": 2.6220869851426016e-05, "9": 3.9699266289878856e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T11:26:28.908987+00:00", "p_over_1_5": 0.769978121499485, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Eyüpspor vs Kocaelispor

The model's most likely 1X2 outcome is **Kocaelispor win** at **44.5%**. Expected goals are 0.80 for Eyüpspor and 0.87 for Kocaelispor (1.67 combined). The most likely exact score is 1-1 at 14.6%. Goal-market probabilities: at least one goal: 89.1%; Over 2.5 goals: 41.8%; Under 3.5 goals: 78.7%; Double Chance 1X: 55.5%; Double Chance X2: 75.3%; Double Chance 12 (either team wins): 69.2%; Under 4.5 goals: 90.9%; BTTS Yes (both teams score): 49.1%; BTTS No (at least one team does not score): 50.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eyüpspor win | 24.7% | 4.05 |
| Draw | 30.8% | 3.25 |
| Kocaelispor win | 44.5% | 2.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eyüpspor expected goals | 0.80 |
| Kocaelispor expected goals | 0.87 |
| Expected total goals | 1.67 |
| Over 0.5 | 89.1% |
| Under 0.5 | 10.9% |
| Over 1.5 | 69.6% |
| Under 1.5 | 30.4% |
| Over 2.5 | 41.8% |
| Under 2.5 | 58.2% |
| Over 3.5 | 21.3% |
| Under 3.5 | 78.7% |
| Over 4.5 | 9.1% |
| Under 4.5 | 90.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.55% |
| 2 | 0-1 | 12.41% |
| 3 | 0-0 | 10.85% |
| 4 | 1-2 | 9.65% |
| 5 | 0-2 | 8.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eyüpspor win | 24.7% | 22.6% | 4.20 | +3.7% |
| Draw | 30.8% | 28.1% | 3.50 | +7.7% |
| Kocaelispor win | 44.5% | 49.3% | 2.00 | -10.9% |
| Over 2.5 | 41.8% | 43.7% | 2.20 | -7.9% |
| Under 2.5 | 58.2% | 56.3% | 1.73 | +0.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T10:30:00+00:00 |
| Fixture id | a3dad1ddaa98a6ff741be7f63250f2ee |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T11:25:08Z |
| Market best draw last update utc | 2026-11-06T11:23:33Z |
| Market best away last update utc | 2026-11-06T11:23:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Eyupspor |
| Matched away-team name | Kocaelispor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7984 |
| Dc lambda away | 0.8690 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 49.1% |
| P btts no | 50.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.22 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.28 |
| Fair Over 2.5 odds | 2.39 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.69 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.04 |
| Fair Under 4.5 odds | 1.10 |
| Score matrix json | [[0.10851697624858578,0.12405864013595208,0.08551528225276434,0.035017981104890274,0.010754735601274469,0.002642398772376239,0.0005410230069121077,9.49481088606242e-05,1.4580249552057083e-05,1.9901741141791283e-06,2.4448921066449606e-07,2.730458867231651e-08,2.7952652000194794e-09,2.6414858628996864e-10,2.3178689636126943e-11],[0.07189840886668197,0.14552011552296662,0.09652279325461081,0.03952548902768698,0.012139083139332813,0.0029825278439522948,0.000610663386315107,0.00010716981152423266,1.6457016524299028e-05,2.2463489507734227e-06,2.7595981574614164e-07,3.081923017607769e-08,3.1550712093283994e-09,2.9814974249401115e-10,2.6162246194169e-11],[0.04603312628808632,0.056550844624141755,0.04600589090676371,0.02230660126005427,0.006850811815688517,0.001683219132733562,0.00034463393110971256,6.048234472473327e-05,9.287680293607874e-06,1.2677492820074626e-06,1.557406555889856e-07,1.7393137835639014e-08,1.78059569014482e-09,1.6826376055570239e-10,1.4764922794804744e-11],[0.01731950054040278,0.021276686225882958,0.013069007841728148,0.007088032642982055,0.00257754900680563,0.0006332942606711484,0.0001296650485726534,2.2755873576545494e-05,3.4943962497255144e-06,4.769779101556709e-07,5.859585446696484e-08,6.543993085727331e-09,6.699312105092334e-10,6.330754669228098e-11,5.555153624006815e-12],[0.004887215845798074,0.006003854315927666,0.003687812016516021,0.0015101362950663804,0.0006142716886628871,0.00017870294461349597,3.658887729193786e-05,6.421251332787249e-06,9.860485689709583e-07,1.3459360419606146e-07,1.6534575450428585e-08,1.8465836603516676e-09,1.8904115739120888e-10,1.7864120540390697e-11,1.5675529876716247e-12],[0.0011032594695303747,0.0013553338622076664,0.0008325012967387794,0.0003409041508256597,0.00010469861173678451,3.4070245575754526e-05,8.259718135126374e-06,1.4495587186358901e-06,2.2259451095646006e-07,3.0383693508277936e-08,3.732580576737536e-09,4.168551121626095e-10,4.267489990280459e-11,4.032717353370691e-12,3.5386562251517255e-13],[0.00020754513672560467,0.00025496536355175826,0.00015661011777169813,6.413087813654133e-05,1.9695899548581833e-05,4.8392096949227585e-06,1.31228310133572e-06,2.7269094058095026e-07,4.18744724035706e-08,5.7157794676248594e-09,7.021729407571604e-10,7.841877059562743e-11,8.028000828172565e-12,7.586346617421852e-13,6.656918978331116e-14],[3.3465758225451005e-05,4.1112065293865775e-05,2.525270608453852e-05,1.0340827524861875e-05,3.1758788604960444e-06,7.803016934415315e-07,1.5976436747459913e-07,3.713523952105688e-08,6.752078084725022e-09,9.216447889425886e-10,1.1322235846412895e-10,1.2644688565071111e-11,1.2944805115069635e-12,1.2232656747277397e-13,1.0733994762295065e-14],[4.721683038997953e-06,5.800500323001612e-06,3.562903706077888e-06,1.458987111674368e-06,4.4808467354886076e-07,1.1009274753028871e-07,2.2541150840184935e-08,3.9559124408277244e-09,8.045648009284344e-10,1.3003484154204974e-10,1.5974539886230814e-11,1.7840388115187552e-12,1.826382248482121e-13,1.7259052520608222e-14,1.5144590679340105e-15],[5.92161909909214e-07,7.274599589443421e-07,4.4683555545512623e-07,1.829764063886365e-07,5.619578313457714e-08,1.3807096136322616e-08,2.8269603916294104e-09,4.961240826727127e-10,7.618490795611193e-11,1.3773070892480217e-11,2.0034199608110244e-12,2.237422167594949e-13,2.2905264744644508e-14,2.164514945076818e-15,1.8993332816712195e-16],[6.683848792602782e-08,8.210984676475484e-08,5.043521438720401e-08,2.0652909490632112e-08,6.3429293740118496e-09,1.5584342946721928e-09,3.190846200024072e-10,5.599850810163663e-11,8.599141493837068e-12,1.1737651501845273e-12,1.9097897408413824e-13,2.52542272698947e-14,2.5853626102227816e-15,2.443130900540427e-16,2.1438151034393187e-17],[6.8583568622652725e-09,8.425364613901033e-09,5.175202333648269e-09,2.119213464068534e-09,6.508536406039468e-10,1.5991233301213576e-10,3.2741557463998604e-11,5.746056863831591e-12,8.82365578633646e-13,1.2044108899299412e-13,1.4795965121682358e-14,2.1885423696549635e-15,2.652863634331357e-16,2.506918408399363e-17,2.199787799265192e-18],[6.45096938663825e-10,7.92489663152184e-10,4.867794501582253e-10,1.9933318512012027e-10,6.121928320497644e-11,1.504135152959161e-11,3.0796703804262097e-12,5.404740182944777e-13,8.299529245710501e-14,1.132868693756703e-14,1.3917082467798875e-15,1.5542616840602301e-16,2.1074012820583068e-17,2.358007060898643e-18,2.0691200582223652e-19],[5.601028422551362e-11,6.880759870117253e-11,4.2264431474398444e-11,1.730702423930282e-11,5.315339830158191e-12,1.3059593431853523e-12,2.6739115160870104e-13,4.6926440922012566e-14,7.206033142136129e-15,9.836087217981014e-16,1.2083451306184903e-16,1.3494815037466045e-17,1.3815108994179223e-18,1.7290808800892555e-19,1.7965052321871275e-20],[4.515708389033474e-12,5.54746427340209e-12,3.4074786515676038e-12,1.3953415096405665e-12,4.285378121804914e-13,1.0529015596518623e-13,2.1557835014925952e-14,3.783343110451295e-15,5.809708835002605e-16,7.93013322101107e-17,9.742022056542471e-18,1.0879903631230263e-18,1.1138133727236023e-19,1.0525377978223716e-20,1.223246580102213e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2456528258952539, "-10": 2.7715391163039846e-07, "-11": 3.063347879582461e-08, "-12": 3.1081798653082952e-09, "-13": 2.9031083248413766e-10, "-14": 2.3178689636126943e-11, "-2": 0.1325629586051396, "-3": 0.04897659810218206, "-4": 0.014105670397177956, "-5": 0.003317177305581278, "-6": 0.0006579744362225082, "-7": 0.00011273336054932657, "-8": 1.6989076291949154e-05, "-9": 2.2842152169575816e-06, "0": 0.3077807074924087, "1": 0.1431380992467035, "10": 7.576836755213856e-08, "11": 7.694506298401495e-09, "12": 7.173120160165651e-10, "13": 6.155774849891572e-11, "14": 4.515708389033474e-12, "2": 0.0713590279285489, "3": 0.024223275886666507, "4": 0.006409962869986651, "5": 0.0013849943137850922, "6": 0.0002524095881008218, "7": 3.973441317956501e-05, "8": 5.50175997259395e-06, "9": 6.796517128227234e-07} |
| Raw goal margin distribution | {"-1": 0.21524372546979043, "-10": 1.3596089051065054e-08, "-11": 1.0669005206903448e-09, "-12": 7.303525502027716e-11, "-2": 0.08923672012449956, "-3": 0.024478880744428787, "-4": 0.005143340261513511, "-5": 0.0008739833906662309, "-6": 0.00012454363696172305, "-7": 1.5273051171982444e-05, "-8": 1.643243430430103e-06, "-9": 1.5745056074816003e-07, "0": 0.3695032051539474, "1": 0.19673830817998733, "10": 5.82893519058548e-09, "11": 4.2025866429495437e-10, "12": 2.643277878930746e-11, "2": 0.07533185204223385, "3": 0.018986465496834012, "4": 0.003665349118751421, "5": 0.0005722565765068613, "6": 7.492498758822079e-05, "7": 8.442060596648106e-06, "8": 8.345302539086019e-07, "9": 7.346862556518454e-08} |
| Research history json | {"away": [{"away": "Rizespor", "away_goals": 0.0, "away_xg": 1.17, "date": "2026-10-31T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 0.0, "home_xg": 0.62, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.83, "date": "2026-10-18T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.61, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 1.0, "away_xg": 1.65, "date": "2026-10-11T00:00:00+00:00", "home": "Besiktas", "home_goals": 2.0, "home_xg": 2.21, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.88, "date": "2026-09-19T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.16, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 0.77, "date": "2026-08-29T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 0.0, "away_xg": 0.59, "date": "2026-08-24T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.3, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.44, "date": "2026-08-16T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.96, "source": "pipeline training history"}], "h2h": [{"away": "Kocaelispor", "away_goals": 1.0, "away_xg": null, "date": "2026-03-09T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Eyupspor", "away_goals": 1.0, "away_xg": 0.98, "date": "2026-11-01T00:00:00+00:00", "home": "Amedspor", "home_goals": 5.0, "home_xg": 4.95, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.59, "date": "2026-10-24T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-10-17T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 4.0, "away_xg": 3.21, "date": "2026-10-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Rizespor", "away_goals": 2.0, "away_xg": 2.05, "date": "2026-09-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-06T00:00:00+00:00", "home": "Corum", "home_goals": 3.0, "home_xg": 2.58, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 1.0, "away_xg": 1.16, "date": "2026-08-23T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.09, "date": "2026-08-16T00:00:00+00:00", "home": "Besiktas", "home_goals": 1.0, "home_xg": 1.29, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 37.0% |
| Unadjusted away-win probability | 33.5% |
| Raw p over 1 5 | 50.9% |
| Raw p under 3 5 | 91.2% |
| Raw p btts yes | 33.2% |
| P home draw | 55.5% |
| P draw away | 75.3% |
| P home away | 69.2% |
| Raw p home draw | 66.5% |
| Raw p draw away | 70.5% |
| Raw p home away | 63.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.4137 |
| Totals anchor target over 2 5 | 0.4185 |
| Totals anchor reference over odds | 2.28 |
| Totals anchor reference under odds | 1.67 |
| Totals anchor reference last update utc | 2026-11-06T11:25:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.2511 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.14, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.01, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.14, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.0, "draw": 3.5, "home": 4.07}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.2, "under": 1.73}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.26, "home_away": 1.33, "home_draw": 1.86}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.98, "draw": 3.4, "home": 4.2}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.28, "under": 1.67}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.4, "under": 3.02}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.20 |
| Reference draw odds | 3.40 |
| Reference away odds | 1.98 |
| Market reference 1x2 last update utc | 2026-11-06T11:25:08Z |
| Market reference home last update utc | 2026-11-06T11:25:08Z |
| Market reference draw last update utc | 2026-11-06T11:25:08Z |
| Market reference away last update utc | 2026-11-06T11:25:08Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market reference under 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market best over 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market best under 2 5 last update utc | 2026-11-06T11:23:33Z |
| Home probability edge | +2.1% |
| Draw probability edge | +2.6% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.0694 |
| Raw ev home | 0.2406 |
| Raw edge prob draw | 0.0882 |
| Raw ev draw | 0.2933 |
| Raw edge prob away | -0.1576 |
| Raw ev away | -0.3298 |
| Market p home draw | 52.4% |
| Market home draw odds | 1.86 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T11:23:33Z |
| Market reference home draw last update utc | 2026-11-06T11:25:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 76.1% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T11:23:33Z |
| Market reference draw away last update utc | 2026-11-06T11:25:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.5% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T11:23:33Z |
| Market reference home away last update utc | 2026-11-06T11:25:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.24 |
| Market reference dc home draw odds | 1.80 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 69.6% |
| Market over 1 5 odds | 1.40 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference over 1 5 odds | 1.40 |
| Market reference over 1 5 opposite odds | 3.02 |
| Market reference over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 79.0% |
| Market under 3 5 odds | 1.24 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference under 3 5 odds | 1.24 |
| Market reference under 3 5 opposite odds | 4.16 |
| Market reference under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,370.1212 |
| Elo away rating | 1,438.4311 |
| Elo rating diff | -8.3099 |
| Elo home expectancy | 0.4880 |
| Research p home | 0.3260 |
| Research p draw | 0.3098 |
| Research p away | 0.3642 |
| Research p over 1 5 | 0.5895 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.7983931486433073, 0.8689589862898933], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T11:26:28.914251+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T11:26:28.849834+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T11:26:28.915253+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Ey%C3%BCpspor%22+%22Kocaelispor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T11:25:35.001023+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T11:25:35.083842+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T11:26:28.973034+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Ey%C3%BCpspor_vs_Kocaelispor&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 0.890448735118826, "goals_for": 1.0632630221502812, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.513167850691485, "results": "DWLLWLWWWL", "xg_against": 1.2372826932614873, "xg_for": 1.1882938425185394, "xg_matches": 10}, "venue": {"goals_against": 1.3740829150788851, "goals_for": 1.0848014184490722, "last_match": "2026-10-23T00:00:00+00:00", "matches": 5, "points_per_game": 1.2891252875508328, "results": "WLLWL", "xg_against": 1.5093258702129508, "xg_for": 1.1284305210338508, "xg_matches": 5}}, "home": {"all": {"goals_against": 3.0933035323073734, "goals_for": 0.3034050194301704, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.19620865573750387, "results": "LLLLLLLWLL", "xg_against": 2.5307266426055373, "xg_for": 0.8256655613941696, "xg_matches": 10}, "venue": {"goals_against": 1.8723623359830541, "goals_for": 0.3416191115517185, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.5124286673275777, "results": "LLLWL", "xg_against": 1.563686916043823, "xg_for": 1.0291416727227958, "xg_matches": 5}}}, "goal_rates": [0.9553400229181627, 1.0279922303728743], "h2h": [{"away": "Kocaelispor", "away_goals": 1.0, "away_xg": null, "date": "2026-03-09T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.22327310731523486, "-10": 5.4628005885769845e-08, "-11": 5.067391893517382e-09, "-12": 4.303474815338819e-10, "-13": 3.164005643446504e-11, "-2": 0.09963495623011459, "-3": 0.031667371182284104, "-4": 0.007768801843532388, "-5": 0.0015477255449592147, "-6": 0.0002592168272247035, "-7": 3.742005020339955e-05, "-8": 4.744418564789318e-06, "-9": 5.361152095725036e-07, "0": 0.3097867467033784, "1": 0.20749352880048216, "10": 2.6248032142994512e-08, "11": 2.2627367694012187e-09, "12": 1.7858169788950868e-10, "13": 1.2201776665237588e-11, "2": 0.08604943333353875, "3": 0.025416540242788003, "4": 0.00579464193268577, "5": 0.0010728392440304425, "6": 0.0001669829124681746, "7": 2.240171908866027e-05, "8": 2.6395392111820608e-06, "9": 2.77186062875496e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T11:26:28.973339+00:00", "p_over_1_5": 0.58946388327774, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Galatasaray vs Amed SK

The model's most likely 1X2 outcome is **Galatasaray win** at **64.3%**. Expected goals are 2.21 for Galatasaray and 1.53 for Amed SK (3.74 combined). The most likely exact score is 2-1 at 11.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 67.5%; Under 3.5 goals: 55.4%; Double Chance 1X: 83.1%; Double Chance X2: 35.7%; Double Chance 12 (either team wins): 81.2%; Under 4.5 goals: 73.7%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 64.3% | 1.56 |
| Draw | 18.8% | 5.32 |
| Amed SK win | 16.9% | 5.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 2.21 |
| Amed SK expected goals | 1.53 |
| Expected total goals | 3.74 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 86.5% |
| Under 1.5 | 13.5% |
| Over 2.5 | 67.5% |
| Under 2.5 | 32.5% |
| Over 3.5 | 44.6% |
| Under 3.5 | 55.4% |
| Over 4.5 | 26.3% |
| Under 4.5 | 73.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.86% |
| 2 | 2-0 | 8.62% |
| 3 | 1-1 | 8.26% |
| 4 | 3-1 | 7.89% |
| 5 | 1-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 64.3% | 69.3% | 1.45 | -6.8% |
| Draw | 18.8% | 17.5% | 5.15 | -3.3% |
| Amed SK win | 16.9% | 13.2% | 6.73 | +14.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | e300554369b00b495db88afb743c95ab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T11:23:33Z |
| Market best draw last update utc | 2026-11-06T11:23:33Z |
| Market best away last update utc | 2026-11-06T11:23:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Galatasaray |
| Matched away-team name | Amedspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2145 |
| Dc lambda away | 1.5275 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.0% |
| P btts no | 36.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.81 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.41 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.24 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.80 |
| Fair Under 4.5 odds | 1.36 |
| Score matrix json | [[0.03470954399315603,0.02533943050330943,0.02159249423748447,0.009904992384405873,0.003407742282668591,0.0009379276239218559,0.0002151248917770275,4.2292680661131585e-05,7.275248205301018e-06,1.1124433221347678e-06,1.5309128967647762e-07,1.9152716701460957e-08,2.196452051603692e-09,2.3251499345345326e-10,2.2855752037389497e-11,2.0968957766556328e-12,1.8035552484897804e-13,1.4600008800989355e-14],[0.07492283350624881,0.08261077389060308,0.043080376471384546,0.019761996746333905,0.006798974627023968,0.0018713111462278229,0.0004292075396288207,8.438046039640182e-05,1.4515249056453894e-05,2.2194970434423838e-06,3.054408777983208e-07,3.8212641711226276e-08,4.382262662372983e-09,4.6390349086337137e-10,4.560077179958361e-11,4.183632445887594e-12,3.5983725750866763e-13,2.9129283014477006e-14],[0.08618555019265833,0.11860610574884142,0.05171560357324721,0.019714124970805682,0.006782504682648163,0.00186677805231603,0.0004281678204518634,8.417605582580527e-05,1.4480087086057572e-05,2.2141204984700776e-06,3.0470097295334014e-07,3.812007479960184e-08,4.3716469995342685e-09,4.627797236617858e-10,4.5490307764014515e-11,4.1734979480474765e-12,3.589655820074892e-13,2.9058719775566146e-14],[0.05731784862920161,0.07887919495338185,0.05427565361659216,0.01577714271617915,0.0045107164235518755,0.0012415039596287301,0.0002847537466047951,5.598143093872976e-05,9.63000686171874e-06,1.472504651817271e-06,2.0264190697709012e-07,2.5351821415691855e-08,2.9073713681641444e-09,3.077724524611731e-10,3.025340754552251e-11,2.775592000117512e-12,2.3873067871128124e-13,1.9325551646779058e-14],[0.028589500480092615,0.039344058367887146,0.027072087704602947,0.012418612671367759,0.0027074324959380646,0.0006192482603361251,0.00014203197729787778,2.7922910314601234e-05,4.803339489893866e-06,7.344688165532578e-07,1.0107551199779037e-07,1.2645204379947437e-08,1.4501642527383551e-09,1.5351344978630527e-10,1.509006060472582e-11,1.3844341809345774e-12,1.1907618685729586e-13,9.639368561404086e-15],[0.011408097927594547,0.01569950027781662,0.010802603139344473,0.004955411850531605,0.0017048742528747,0.00029734928213766206,5.667516670997207e-05,1.1142107764849583e-05,1.916681521537859e-06,2.930758510397345e-07,4.033226602736414e-08,5.0458289742185995e-09,5.786605407063949e-10,6.125663054464693e-11,6.021402480673601e-12,5.524322022138263e-13,4.7515093922626574e-14,3.846407200617091e-15],[0.0037934875898528162,0.005220489852802816,0.003592144913840957,0.0016478025939916639,0.0005669147794476772,0.0001560344028237813,2.267846518601864e-05,3.7050389818727547e-06,6.373461739022071e-07,9.745529981080811e-08,1.3411521501350663e-08,1.677868625927377e-09,1.9241959473344787e-10,2.0369413835871124e-11,2.0022720464813398e-12,1.8369799388416436e-13,1.579999753422357e-14,1.279029867526575e-15],[0.0010812280528922978,0.001487955330020993,0.0010238409270899769,0.0004696602659300147,0.00016158327887448316,4.4473263600663384e-05,1.020047365601531e-05,1.2707696828523816e-06,1.8165778753829433e-07,2.777692072601811e-08,3.822580919472886e-09,4.782297515018155e-10,5.4843849841101765e-11,5.805734469575759e-12,5.70691917371395e-13,5.23580002683764e-14,4.503349533903307e-15,3.645518643466838e-16],[0.00026965221721097,0.0003710877208353456,0.00025534018963217564,0.00011713063835621503,4.029796424183516e-05,1.1091382714726304e-05,2.543940966559999e-06,5.001284697031125e-07,5.451752570316889e-08,6.9274083677610865e-09,9.533302596495693e-10,1.1926782003459652e-10,1.3677748806533897e-11,1.4479176414924208e-12,1.423273660463426e-13,1.3057791853747447e-14,1.1231101370748253e-15,9.091719202671116e-17],[5.977755719714445e-05,8.226417600726632e-05,5.6604810998179815e-05,2.596597760736617e-05,8.93341018038098e-06,2.4587810605919917e-06,5.639507741029349e-07,1.108704334524637e-07,1.9072092602947364e-08,1.847993264275795e-09,2.113379771670289e-10,2.6439756393023933e-11,3.0321368022391014e-12,3.2098004061042274e-13,3.155168665977517e-14,2.894702322418137e-15,2.489754438219833e-16,2.015487839407757e-17],[1.1926550218186899e-05,1.6412979591532983e-05,1.1293538120574437e-05,5.180615441966614e-06,1.7823539490681199e-06,4.905649740414293e-07,1.1251693015393619e-07,2.212037182988338e-08,3.805178412439852e-09,5.818420478583445e-10,5.0739904997820684e-11,5.275141661243585e-12,6.049583411555795e-13,6.40404986900125e-14,6.295051070341865e-15,5.775380298857602e-16,4.9674464348638566e-17,4.021210979158228e-18],[2.163210755103334e-06,2.9769491869957674e-06,2.0483964498252094e-06,9.39648333935433e-07,3.2327933572489465e-07,8.897756757064436e-08,2.0408066791103267e-08,4.012143107092285e-09,6.90174670486423e-10,1.055331971670398e-10,1.4523178787194755e-11,1.1513663836197476e-12,1.097259782616474e-13,1.1615521084811744e-14,1.141782152438582e-15,1.0475254410323478e-16,9.009842206433762e-18,7.293581697572468e-19],[3.596617598219966e-07,4.949562963153879e-07,3.4057239694246634e-07,1.562286858086933e-07,5.3749369785907684e-08,1.4793671149073905e-08,3.3931049942022064e-09,6.670706712927627e-10,1.1475046339618254e-10,1.7546258645023314e-11,2.414666267948746e-12,3.0209046547539945e-13,2.1953325613868678e-14,1.931230576936244e-15,1.89836046862568e-16,1.7416464978790763e-17,1.4980027702061204e-18,1.2126522681924774e-19],[5.519853991526287e-08,7.596266250823336e-08,5.226882906864913e-08,2.3976959223544363e-08,8.24910253182328e-09,2.270436111471995e-09,5.207516127148012e-10,1.0237765364290693e-10,1.7611152314897023e-11,2.692885278268638e-12,3.705872218369098e-13,4.6362873341933606e-14,5.316939098376805e-15,3.566669599974671e-16,2.913479769237982e-17,2.672965393347229e-18,2.299036899149926e-19,1.8610995692810016e-20],[7.866403727630615e-09,1.082552133503598e-08,7.448887460713748e-09,3.4169824365441896e-09,1.1755885392178449e-09,3.235623101271918e-10,7.421287653111755e-11,1.4589950340696506e-11,2.5097843970229725e-12,3.8376599858570993e-13,5.2812786493000454e-14,6.607223311350803e-15,7.577227514942156e-16,8.021204035597986e-17,4.9963870562030785e-18,3.8092719420355956e-19,3.2763823936641144e-20,2.6522731600796703e-21],[1.0463130701344093e-09,1.4399063226416346e-09,9.907790876190694e-10,4.5449401118556336e-10,1.5636543664335154e-10,4.303713435147264e-11,9.871080277005798e-12,1.940614321695995e-12,3.3382728737919846e-13,5.1044847696160195e-14,7.024646927763072e-15,8.788290491219655e-16,1.0078496424507863e-16,1.0669031124326678e-17,1.048744109938945e-18,6.097093039963235e-20,4.357927510391824e-21,3.527797668470193e-22],[1.3047230808700837e-10,1.7955228383030438e-10,1.2354737607300878e-10,5.6674129707168346e-11,1.9498331815037146e-11,5.366610064008841e-12,1.230896051874463e-12,2.419891683335802e-13,4.162732735546729e-14,6.365149480558718e-15,8.759537889016564e-16,1.0958751995530754e-16,1.2567602642900007e-17,1.3303982866850871e-18,1.3077545193888475e-19,1.1997964119153959e-20,6.539312965326325e-22,4.3990648440446725e-23],[1.5312499987151386e-11,2.107262747288139e-11,1.4499775640275579e-11,6.651393105072568e-12,2.2883645583101274e-12,6.29836459100431e-13,1.444605070214833e-13,2.8400349402324152e-14,4.885469253526677e-15,7.470271107204939e-16,1.0280374876450437e-16,1.2861418047334214e-17,1.4749598449626279e-18,1.5613829514065378e-19,1.534807757672592e-20,1.4081058893958614e-21,1.2111220765105038e-22,6.212745247827272e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.09332446563700021, "-10": 1.9599900949705565e-07, "-11": 2.4029445723345973e-08, "-12": 2.7087443648252533e-09, "-13": 2.82537633248357e-10, "-14": 2.741767561693136e-11, "-15": 2.4857917539398664e-12, "-16": 2.0948480786345504e-13, "-17": 1.4600008800989355e-14, "-2": 0.049532339814639406, "-3": 0.01888543980243269, "-4": 0.005768312999384325, "-5": 0.0014617177615133133, "-6": 0.00031556426362287776, "-7": 5.923793694136984e-05, "-8": 9.826311519769028e-06, "-9": 1.459071369245382e-06, "0": 0.18784185160356262, "1": 0.26209483446963966, "10": 1.526926864631865e-05, "11": 2.714014739431129e-06, "12": 4.4354793197040344e-07, "13": 6.707380283218339e-08, "14": 9.43650881945033e-09, "15": 1.2403651296049894e-09, "16": 1.5154493555988975e-10, "17": 1.5312499987151386e-11, "2": 0.1977062914687965, "3": 0.10928557417125827, "4": 0.04839367932955295, "5": 0.017779004414137496, "6": 0.005564623916674356, "7": 0.0015144398088565221, "8": 0.00036420567567450884, "9": 7.84037447071082e-05} |
| Raw goal margin distribution | {"-1": 0.13582781891135648, "-10": 6.120051732288555e-07, "-11": 8.290398167715176e-08, "-12": 1.033282395736358e-08, "-13": 1.1922750555167796e-09, "-14": 1.2804229078128123e-10, "-15": 1.2846186679519703e-11, "-16": 1.1930885763159199e-12, "-17": 8.941039505135056e-14, "-2": 0.0754609278514176, "-3": 0.030874158379999888, "-4": 0.010224618306816253, "-5": 0.0028273411278549863, "-6": 0.0006688584077511218, "-7": 0.00013797946444040626, "-8": 2.52027528901905e-05, "-9": 4.126824345537288e-06, "0": 0.2188656914875276, "1": 0.20040160331053936, "10": 2.5107067201929126e-05, "11": 4.930833865988542e-06, "12": 8.909802974519552e-07, "13": 1.4904918895890956e-07, "14": 2.3206555506471818e-08, "15": 3.375480213354061e-09, "16": 4.5450442340204406e-10, "17": 4.938073272633277e-11, "2": 0.15860991020344906, "3": 0.09408218503666939, "4": 0.045171390665695844, "5": 0.018109174624005825, "6": 0.006210959906099242, "7": 0.0018575609778721455, "8": 0.0004919043857541229, "9": 0.00011677578261477663} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Galatasaray", "away_goals": 4.0, "away_xg": 2.8, "date": "2026-10-30T00:00:00+00:00", "home": "Konyaspor", "home_goals": 0.0, "home_xg": 1.38, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 1.0, "away_xg": 1.92, "date": "2026-10-17T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 0.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.51, "date": "2026-10-09T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 3.0, "away_xg": 2.12, "date": "2026-09-04T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.63, "date": "2026-08-29T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.92, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 4.0, "away_xg": 3.08, "date": "2026-08-21T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 0.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 2.0, "away_xg": 0.61, "date": "2026-08-14T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 52.5% |
| Unadjusted draw probability | 21.9% |
| Unadjusted away-win probability | 25.6% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.5% |
| Raw p btts yes | 70.5% |
| P home draw | 83.1% |
| P draw away | 35.7% |
| P home away | 81.2% |
| Raw p home draw | 74.4% |
| Raw p draw away | 47.5% |
| Raw p home away | 78.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9009 |
| Totals anchor target over 2 5 | 0.6746 |
| Totals anchor reference over odds | 1.44 |
| Totals anchor reference under odds | 2.83 |
| Totals anchor reference last update utc | 2026-11-06T11:25:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7345 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.78, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.73, "draw": 5.15, "home": 1.45}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.87, "home_away": 1.19, "home_draw": 1.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.67, "draw": 5.14, "home": 1.41}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.44, "under": 2.83}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.14, "under": 5.96}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.41 |
| Reference draw odds | 5.14 |
| Reference away odds | 6.67 |
| Market reference 1x2 last update utc | 2026-11-06T11:25:08Z |
| Market reference home last update utc | 2026-11-06T11:25:08Z |
| Market reference draw last update utc | 2026-11-06T11:25:08Z |
| Market reference away last update utc | 2026-11-06T11:25:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-11-06T11:24:45Z |
| Market reference under 2 5 last update utc | 2026-11-06T11:24:45Z |
| Home probability edge | -5.0% |
| Draw probability edge | +1.3% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.1682 |
| Raw ev home | -0.2386 |
| Raw edge prob draw | 0.0443 |
| Raw ev draw | 0.1272 |
| Raw edge prob away | 0.1238 |
| Raw ev away | 0.7232 |
| Market p home draw | 85.4% |
| Market home draw odds | 1.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T11:23:33Z |
| Market reference home draw last update utc | 2026-11-06T11:25:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.3% |
| Market draw away odds | 2.87 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T11:23:33Z |
| Market reference draw away last update utc | 2026-11-06T11:25:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.3% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T11:23:33Z |
| Market reference home away last update utc | 2026-11-06T11:25:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.74 |
| Market reference dc home draw odds | 1.10 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 86.4% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.96 |
| Market reference over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.1% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.12 |
| Market reference under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,693.8730 |
| Elo away rating | 1,457.7667 |
| Elo rating diff | 296.1063 |
| Elo home expectancy | 0.8461 |
| Research p home | 0.5328 |
| Research p draw | 0.2034 |
| Research p away | 0.2638 |
| Research p over 1 5 | 0.8876 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.2145210217447233, 1.5274806525930467], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T11:26:28.914251+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T11:26:28.849834+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T11:26:29.055308+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Galatasaray%22+%22Amed+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T11:25:35.001023+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T11:25:35.083842+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T11:26:29.112833+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Galatasaray_vs_Amed+SK&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 1.0408527377748258, "goals_for": 2.2981057758943, "last_match": "2026-10-30T00:00:00+00:00", "matches": 10, "points_per_game": 2.6034710533412406, "results": "WWWWLWWWWD", "xg_against": 1.1147534090307207, "xg_for": 2.2984475091718832, "xg_matches": 10}, "venue": {"goals_against": 1.1232992550353904, "goals_for": 2.1999854601202053, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 2.70260329000593, "results": "WWWWD", "xg_against": 0.5544118907898825, "xg_for": 2.502044081155706, "xg_matches": 5}}}, "goal_rates": [2.2145210217447233, 1.5274806525930467], "h2h": [], "margin_distribution": {"-1": 0.14356537223024676, "-10": 6.120051732288555e-07, "-11": 8.290398167715176e-08, "-12": 1.033282395736358e-08, "-13": 1.1922750555167796e-09, "-14": 1.2804229078128123e-10, "-15": 1.2846186679519703e-11, "-16": 1.1930885763159199e-12, "-17": 8.941039505135056e-14, "-2": 0.0754609278514176, "-3": 0.030874158379999888, "-4": 0.010224618306816253, "-5": 0.0028273411278549863, "-6": 0.0006688584077511218, "-7": 0.00013797946444040626, "-8": 2.52027528901905e-05, "-9": 4.126824345537288e-06, "0": 0.203390584849747, "1": 0.20813915662942967, "10": 2.5107067201929126e-05, "11": 4.930833865988542e-06, "12": 8.909802974519552e-07, "13": 1.4904918895890956e-07, "14": 2.3206555506471818e-08, "15": 3.375480213354061e-09, "16": 4.5450442340204406e-10, "17": 4.938073272633277e-11, "2": 0.15860991020344906, "3": 0.09408218503666939, "4": 0.045171390665695844, "5": 0.018109174624005825, "6": 0.006210959906099242, "7": 0.0018575609778721455, "8": 0.0004919043857541229, "9": 0.00011677578261477663}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T11:26:29.113129+00:00", "p_over_1_5": 0.8875832502589232, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Goztepe vs Basaksehir

The model's most likely 1X2 outcome is **Goztepe win** at **44.9%**. Expected goals are 1.52 for Goztepe and 1.35 for Basaksehir (2.87 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 58.9%; Under 3.5 goals: 63.5%; Double Chance 1X: 70.7%; Double Chance X2: 55.1%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 80.6%; BTTS Yes (both teams score): 62.0%; BTTS No (at least one team does not score): 38.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Goztepe win | 44.9% | 2.23 |
| Draw | 25.8% | 3.88 |
| Basaksehir win | 29.3% | 3.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Goztepe expected goals | 1.52 |
| Basaksehir expected goals | 1.35 |
| Expected total goals | 2.87 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 81.9% |
| Under 1.5 | 18.1% |
| Over 2.5 | 58.9% |
| Under 2.5 | 41.1% |
| Over 3.5 | 36.5% |
| Under 3.5 | 63.5% |
| Over 4.5 | 19.4% |
| Under 4.5 | 80.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.89% |
| 2 | 2-1 | 9.74% |
| 3 | 1-0 | 7.24% |
| 4 | 1-2 | 6.99% |
| 5 | 2-0 | 6.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Goztepe win | 44.9% | 46.9% | 2.09 | -6.1% |
| Draw | 25.8% | 25.2% | 3.77 | -2.8% |
| Basaksehir win | 29.3% | 27.9% | 3.48 | +2.0% |
| Over 2.5 | 58.9% | 58.4% | 1.67 | -1.6% |
| Under 2.5 | 41.1% | 41.6% | 2.31 | -5.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | c7ad58db2278db2259846b11c28ae1c2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T11:23:33Z |
| Market best draw last update utc | 2026-11-06T11:23:33Z |
| Market best away last update utc | 2026-11-06T11:23:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Goztep |
| Matched away-team name | Buyuksehyr |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5169 |
| Dc lambda away | 1.3496 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.0% |
| P btts no | 38.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.47 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.54 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.74 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.15 |
| Fair Under 4.5 odds | 1.24 |
| Score matrix json | [[0.057256048110906156,0.05089543556636866,0.0432809643120441,0.020716137315795146,0.007436727995350865,0.002135723370965214,0.0005111246863919364,0.00010484842824184424,1.881936843940858e-05,3.002587295856837e-06,4.311503570611723e-07,5.628195470270834e-08,6.734743094080139e-09,7.438935423702006e-10,7.629847547313037e-11,7.30394860655795e-12],[0.07242948587125231,0.11890236434712678,0.06985066654068384,0.0334335434216272,0.012002052533114831,0.0034468201755597774,0.0008248984420141393,0.00016921371126654526,3.0372369245053773e-05,4.845842214837753e-06,6.958287621053786e-07,9.08328202175189e-08,1.086912691478217e-08,1.2005615077159744e-09,1.2313726028403428e-10,1.1787761355515794e-11],[0.06784687105989559,0.09742332129134558,0.06282505326265106,0.026979011788881044,0.00968498949388103,0.0027813923573062416,0.0006656472067909198,0.0001365460625435032,2.4508814324134633e-05,3.910325405610337e-06,5.614951469289955e-07,7.329703874225143e-08,8.770781471492637e-09,9.687864268970645e-10,9.936492686277726e-11,9.512068420760262e-12],[0.03649910333224517,0.05241013793612098,0.03762863067455887,0.01617696663040364,0.005210165580028098,0.0014962860552141975,0.00035809353922944975,7.345672347935986e-05,1.3184834209637858e-05,2.1036102153639205e-06,3.0206358919961553e-07,3.943109165106911e-08,4.718355529615246e-09,5.211712102534054e-10,5.345464980933008e-11,5.1171404483225266e-12],[0.014726374148652894,0.02114603455882619,0.015182107049886937,0.007266811620022918,0.0023430623234056537,0.0006037098523192884,0.0001444807942514408,2.963774709324202e-05,5.319714292475515e-06,8.48748277796988e-07,1.2187426608117988e-07,1.5909349976564153e-08,1.903725367250145e-09,2.1027810376145433e-10,2.1567466080241086e-11,2.0646240026019706e-12],[0.004753346263704439,0.006825469959389564,0.004900446715007734,0.0023455652772641023,0.0008420165736714388,0.00021719537124276762,4.66351891239269e-05,9.56640602691505e-06,1.7170855365254104e-06,2.7395707961561867e-07,3.933830428800356e-08,5.13518456788531e-09,6.144802359490237e-10,6.787309820895699e-11,6.961498687676901e-12,6.664147392737752e-13],[0.0012785621042105933,0.0018359249988033153,0.0013181294010399418,0.000630913615395844,0.00022648686262013282,6.504383191328265e-05,1.3981533203733737e-05,2.573186033784376e-06,4.6186420573925466e-07,7.368938022700595e-08,1.058127523563763e-08,1.3812695356867144e-09,1.6528380216477687e-10,1.8256606283445003e-11,1.8725142072100694e-12,1.7925322163649805e-13],[0.00029477959260690724,0.00042328270282828394,0.0003039020525965323,0.00014546063730816228,5.2217803792331554e-05,1.4996216616968895e-05,3.5889182183503945e-06,6.612496451700411e-07,1.0648535722994116e-07,1.6989495786897204e-08,2.4395717603007104e-09,3.184593612380335e-10,3.8107098361667446e-11,4.209161952239592e-12,4.317185479956265e-13,4.1327825588970525e-14],[5.946768791278362e-05,8.53914053142704e-05,6.130801749212224e-05,2.934466292777457e-05,1.0534216537690469e-05,3.0252783843134657e-06,7.240143955215025e-07,1.4851908627377164e-07,2.3943752332581484e-08,3.4273947674459244e-09,4.921497136196376e-10,6.424475228942307e-11,7.687577734240643e-12,8.491399527915686e-13,8.709321989124168e-14,8.337314711999721e-15],[1.0663804398300852e-05,1.5312470948978307e-05,1.0993814112000442e-05,5.26211387358461e-06,1.8890060903667463e-06,5.424959011024771e-07,1.29830974876957e-07,2.6632588907116546e-08,4.780314894012914e-09,6.850368379695243e-10,8.825277162980814e-11,1.1520432289825506e-11,1.3785440149431516e-12,1.5226861311023268e-13,1.561764201595529e-14,1.4950554900710846e-15],[1.7210195219091013e-06,2.471262642069531e-06,1.7742794222676567e-06,8.492467007732089e-07,3.04864590262399e-07,8.755280962409602e-08,2.095327651990089e-08,4.298203878854965e-09,7.714896997529263e-10,1.2308942134911197e-10,1.5875253173110217e-11,1.8592697438055823e-12,2.2248168410761032e-13,2.457446197892472e-14,2.5205138608815443e-15,2.4128534138901635e-16],[2.5250311360517135e-07,3.625766609355499e-07,2.603172554551827e-07,1.2459907248831337e-07,4.4728869887442425e-08,1.284550044524869e-08,3.074205431229585e-09,6.30620308778825e-10,1.1319078535834389e-10,1.805933154554373e-11,2.5931926292005864e-12,3.0404791059428377e-13,3.264188304789077e-14,3.605495513477463e-15,3.698026603740036e-16,3.540070242807579e-17],[3.395933036857646e-08,4.876320310211613e-08,3.5010260081254736e-08,1.6757421347544845e-08,6.015618769342652e-09,1.727600848724593e-09,4.1345216052757394e-10,8.481259140606186e-11,1.5223112379806725e-11,2.4288128468377576e-12,3.487603932761032e-13,4.5526847734187085e-14,4.8931244864655735e-15,4.849057563545773e-16,4.973503310718015e-17,4.761066633477233e-18],[4.215891175298716e-09,6.053722361608748e-09,4.34635915724807e-09,2.0803550603944993e-09,7.468107824381734e-10,2.1447352151902564e-10,5.132814151686863e-11,1.0529084401319438e-11,1.8898778169664518e-12,3.015256937136328e-13,4.329696281841226e-14,5.651944061280189e-15,6.763160845407224e-16,6.709749302237685e-17,6.174370486815338e-18,5.910640341618502e-19],[4.859985600374536e-10,6.978596525086827e-10,5.010386188819245e-10,2.3981870538836163e-10,8.609068635640949e-11,2.472403064745209e-11,5.9169940184305854e-12,1.2137694368241107e-12,2.1786091232000147e-13,3.4759211484802306e-14,4.991177596573654e-15,6.515435434596535e-16,7.79642143380683e-17,8.61162404740202e-18,7.93335623610247e-19,6.813654754080173e-20],[5.2289844424718394e-11,7.50845283515961e-11,5.3908043328549275e-11,2.580271594617153e-11,9.262720028732095e-12,2.6601225238354788e-12,6.366247189330783e-13,1.3059259890424298e-13,2.344022009152079e-14,3.739833633922963e-15,5.370137310712673e-16,7.01012581617721e-17,8.388371846449127e-18,9.265469462463284e-19,9.503257580060858e-20,8.171112155655238e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.15358830770633577, "-10": 5.312973638412569e-07, "-11": 6.817538731819951e-08, "-12": 8.039786669107214e-09, "-13": 8.765428710749952e-10, "-14": 8.808623682864616e-11, "-15": 7.30394860655795e-12, "-2": 0.0880503098406427, "-3": 0.03588910677267568, "-4": 0.011628256680130011, "-5": 0.003111242216556212, "-6": 0.0007070780012301816, "-7": 0.00013944972900858265, "-8": 2.426811040513389e-05, "-9": 3.7766488710897532e-06, "0": 0.2577353574735584, "1": 0.2156590522061127, "10": 2.1207755487951805e-06, "11": 3.0586175728995265e-07, "12": 4.053989406501331e-08, "13": 4.967658871135948e-09, "14": 5.610830883890496e-10, "15": 5.2289844424718394e-11, "2": 0.1380269158392927, "3": 0.0632318755484939, "4": 0.02302653245825588, "5": 0.006924497697875249, "6": 0.0017687330726981374, "7": 0.0003920605677700386, "8": 7.668527349639537e-05, "9": 1.3412913888610914e-05} |
| Raw goal margin distribution | {"-1": 0.17604973866772577, "-10": 3.782050071562631e-07, "-11": 4.570419457050809e-08, "-12": 5.074450079667729e-09, "-13": 5.208303113719945e-10, "-14": 4.935312475806248e-11, "-15": 3.907327374093747e-12, "-2": 0.09757658022851705, "-3": 0.037985576091309356, "-4": 0.01169307443198092, "-5": 0.002963182146095715, "-6": 0.0006365782452990807, "-7": 0.00011852098788162222, "-8": 1.945412970252911e-05, "-9": 2.8536157140489938e-06, "0": 0.27091606000268675, "1": 0.19926104126054645, "10": 1.2165570035214296e-06, "11": 1.6523489460361026e-07, "12": 2.0619361424867955e-08, "13": 2.378608667389541e-09, "14": 2.5332725629676016e-10, "15": 2.254174763670345e-11, "2": 0.12326126801310056, "3": 0.05393122363319, "4": 0.01865910419046601, "5": 0.005314482028187825, "6": 0.0012832016404343328, "7": 0.0002685213951452443, "8": 4.953771362546253e-05, "9": 8.166954911557272e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 58.9% |
| P home draw | 70.7% |
| P draw away | 55.1% |
| P home away | 74.2% |
| Raw p home draw | 67.3% |
| Raw p draw away | 59.8% |
| Raw p home away | 72.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0639 |
| Totals anchor target over 2 5 | 0.5894 |
| Totals anchor reference over odds | 1.64 |
| Totals anchor reference under odds | 2.30 |
| Totals anchor reference last update utc | 2026-11-06T11:25:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5515 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.76, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.48, "draw": 3.77, "home": 2.09}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.31}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.79, "home_away": 1.3, "home_draw": 1.33}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.73, "home": 2.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.64, "under": 2.3}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.19, "under": 4.75}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.06 |
| Reference draw odds | 3.73 |
| Reference away odds | 3.39 |
| Market reference 1x2 last update utc | 2026-11-06T11:25:08Z |
| Market reference home last update utc | 2026-11-06T11:25:08Z |
| Market reference draw last update utc | 2026-11-06T11:25:08Z |
| Market reference away last update utc | 2026-11-06T11:25:08Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market reference under 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market best over 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market best under 2 5 last update utc | 2026-11-06T11:23:33Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | -0.0673 |
| Raw ev home | -0.1597 |
| Raw edge prob draw | 0.0188 |
| Raw ev draw | 0.0214 |
| Raw edge prob away | 0.0484 |
| Raw ev away | 0.1381 |
| Market p home draw | 72.3% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T11:23:33Z |
| Market reference home draw last update utc | 2026-11-06T11:25:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.7% |
| Market draw away odds | 1.79 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T11:23:33Z |
| Market reference draw away last update utc | 2026-11-06T11:25:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.0% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T11:23:33Z |
| Market reference home away last update utc | 2026-11-06T11:25:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home draw odds | 1.30 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 82.4% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market reference over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.8% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.57 |
| Market reference under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,515.0066 |
| Elo away rating | 1,527.1311 |
| Elo rating diff | 47.8755 |
| Elo home expectancy | 0.5685 |
| Research p home | 0.4133 |
| Research p draw | 0.2484 |
| Research p away | 0.3383 |
| Research p over 1 5 | 0.7800 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.5169153698571327, 1.3496489863885945], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T11:26:28.914251+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T11:26:28.849834+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T11:26:29.122415+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Goztepe%22+%22Basaksehir%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T11:25:35.001023+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T11:25:35.083842+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T11:26:29.180155+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Goztepe_vs_Basaksehir&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.5169153698571327, 1.3496489863885945], "h2h": [], "margin_distribution": {"-1": 0.18728874486039104, "-10": 3.782050071562631e-07, "-11": 4.570419457050809e-08, "-12": 5.074450079667729e-09, "-13": 5.208303113719945e-10, "-14": 4.935312475806248e-11, "-15": 3.907327374093747e-12, "-2": 0.09757658022851705, "-3": 0.037985576091309356, "-4": 0.01169307443198092, "-5": 0.002963182146095715, "-6": 0.0006365782452990807, "-7": 0.00011852098788162222, "-8": 1.945412970252911e-05, "-9": 2.8536157140489938e-06, "0": 0.24843804761735622, "1": 0.2105000474532117, "10": 1.2165570035214296e-06, "11": 1.6523489460361026e-07, "12": 2.0619361424867955e-08, "13": 2.378608667389541e-09, "14": 2.5332725629676016e-10, "15": 2.254174763670345e-11, "2": 0.12326126801310056, "3": 0.05393122363319, "4": 0.01865910419046601, "5": 0.005314482028187825, "6": 0.0012832016404343328, "7": 0.0002685213951452443, "8": 4.953771362546253e-05, "9": 8.166954911557272e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T11:26:29.180451+00:00", "p_over_1_5": 0.7800154597593887, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Samsunspor vs Torku Konyaspor

The model's most likely 1X2 outcome is **Samsunspor win** at **41.4%**. Expected goals are 1.41 for Samsunspor and 1.08 for Torku Konyaspor (2.49 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 48.5%; Under 3.5 goals: 73.2%; Double Chance 1X: 70.1%; Double Chance X2: 58.6%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Samsunspor win | 41.4% | 2.41 |
| Draw | 28.7% | 3.48 |
| Torku Konyaspor win | 29.9% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Samsunspor expected goals | 1.41 |
| Torku Konyaspor expected goals | 1.08 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.71% |
| 2 | 1-0 | 9.04% |
| 3 | 0-0 | 8.61% |
| 4 | 2-1 | 8.58% |
| 5 | 0-1 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Samsunspor win | 41.4% | 40.6% | 2.37 | -1.8% |
| Draw | 28.7% | 28.6% | 3.48 | -0.1% |
| Torku Konyaspor win | 29.9% | 30.8% | 3.18 | -5.0% |
| Over 2.5 | 48.5% | 48.5% | 1.98 | -4.0% |
| Under 2.5 | 51.5% | 51.5% | 1.90 | -2.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T13:00:00+00:00 |
| Fixture id | 605767f0e7114a23442d92831c12c767 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T11:25:08Z |
| Market best draw last update utc | 2026-11-06T11:23:33Z |
| Market best away last update utc | 2026-11-06T11:23:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Samsunspor |
| Matched away-team name | Konyaspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4120 |
| Dc lambda away | 1.0826 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.62 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.96 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.01 |
| Fair Under 4.5 odds | 1.14 |
| Score matrix json | [[0.08605976860159095,0.07580492405748322,0.050364489101875944,0.019111883136055444,0.0054393097724181275,0.0012384374931430115,0.00023497580400728288,3.8214255883777224e-05,5.437956427281106e-06,6.878496442664343e-07,7.830578002968988e-08,8.104037425210484e-09,7.688126046883402e-10,6.73251679889364e-11,5.474566217183254e-12,4.1548826019762595e-13],[0.09038432860488145,0.13714106876453572,0.07478335955906268,0.028378146068817858,0.008076521090903257,0.0018388852541281592,0.00034890217993101724,5.674217070400291e-05,8.074511585837404e-06,1.0213487357272554e-06,1.1627179006358764e-07,1.2033223317796797e-08,1.1415660215206308e-09,9.996730503721906e-11,8.12887137644495e-12,6.169348385938679e-13],[0.07538377776456862,0.08581796281561879,0.052854748742676906,0.021068545903357144,0.005996182940579799,0.0013652279572334857,0.0002590324813971973,4.212660775070891e-05,5.994691040805223e-06,7.582712651426507e-07,8.63226773264067e-08,8.933723761289746e-09,8.475231633453243e-10,7.421787702072009e-11,6.035048918340091e-12,4.580256911348186e-13],[0.03731102514237047,0.042475400719245056,0.024177299596783747,0.009927098815042447,0.002967796773901917,0.0006757163961255764,0.00012820752306000785,2.0850466341158078e-05,2.967058361584973e-06,3.7530459572924277e-07,4.27252079902542e-08,4.4217257579407495e-09,4.194796147664211e-10,3.6733965286029776e-11,2.9870333990273644e-12,2.2669874851794805e-13],[0.013850253712963745,0.0157673254561231,0.008974873572410138,0.0034057078297729834,0.001048777119193379,0.00025083319176134953,4.759201108830599e-05,7.73991729674311e-06,1.1014039665840059e-06,1.3931710133014737e-07,1.5860056601129637e-08,1.6413921451619336e-09,1.557153433807289e-10,1.363604288955732e-11,1.1088189152606344e-12,8.415301298755638e-14],[0.004113090480499811,0.004682400595724886,0.0026652556566395436,0.0010113882925401971,0.00028784469767632735,7.091270253190003e-05,1.4133332992444162e-05,2.2985124181005136e-06,3.270823960359074e-07,4.137280479674607e-08,4.70993883420605e-09,4.874419304473563e-10,4.624256781141549e-11,4.049476591770226e-12,3.292844029772452e-13,2.499080260894576e-14],[0.0010178822744202059,0.001158771631871275,0.0006595810382858177,0.00025029213930827156,7.12340311840096e-05,1.621876647903745e-05,3.3296790828724484e-06,5.688216826280307e-07,8.094433486894338e-08,1.0238686662817514e-08,1.1655866253540656e-09,1.2062912380941328e-10,1.1443825591017498e-11,1.002139501424627e-12,8.148927397114997e-14,6.18456975838008e-15],[0.0002159136256352252,0.0002457991367057516,0.0001399106133935347,5.309207619007636e-05,1.5110193318095662e-05,3.440331717943233e-06,6.527537449014528e-07,1.1486484729055064e-07,1.716994711018068e-08,2.1718346165043217e-09,2.4724473605307094e-10,2.5587901600631177e-11,2.427469204040512e-12,2.1257426185962178e-13,1.7285539826808788e-14,1.3118735958796695e-15],[4.0074729704193706e-05,4.56216412281862e-05,2.596816202774704e-05,9.854174772398677e-06,2.804533114662344e-06,6.385440626255992e-07,1.2115460436258004e-07,1.970344594486813e-08,3.033807406435492e-09,4.031041809545828e-10,4.5889952238822715e-11,4.7492521017418665e-12,4.505513347338602e-13,3.945492583448623e-14,3.2082891216913766e-15,2.434907922382152e-16],[6.6116313611337364e-06,7.526775005524308e-06,4.2842937612050204e-06,1.625766947006158e-06,4.6269904329009624e-07,1.0534863194546651e-07,1.9988396370033633e-08,3.250724885559512e-09,4.6258391995159547e-10,6.331167886397675e-11,7.571041642019581e-12,7.835437536218962e-13,7.433311107810972e-14,6.509374534126837e-15,5.293117415671337e-16,4.017173340887223e-17],[9.817234606539914e-07,1.1176079249403608e-06,6.361503641042792e-07,2.414008685986502e-07,6.870354398315284e-08,1.564261796818212e-08,2.9679630616834947e-09,4.826816121427406e-10,6.868644997471499e-11,8.688181086558318e-12,1.0701993225999545e-12,1.1634394650333364e-13,1.1037300034263558e-14,9.665399271807193e-16,7.859448391977078e-17,5.964871752297003e-18],[1.3251865614562036e-07,1.5086111949706297e-07,8.587122009031661e-08,3.258567201579135e-08,9.27399790876325e-09,2.1115301760863567e-09,4.0063265490480116e-10,6.51551288636279e-11,9.271690461587835e-12,1.1727804499787708e-12,1.335109913985598e-13,1.4950652358110376e-14,1.4898779815674868e-15,1.3046909582434652e-16,1.0609133637866119e-17,8.051725566065159e-19],[1.639745001479064e-08,1.866708988815989e-08,1.0625440070813667e-08,4.032050607954794e-09,1.1475359135781885e-09,2.612742350711077e-10,4.9573049743845125e-11,8.062094801011083e-12,1.1472503971775465e-12,1.4511623771462557e-13,1.652023852005671e-14,1.7097158241598794e-15,1.755005543954002e-16,1.6143843738528255e-17,1.3127414930617903e-18,9.962957016201883e-20],[1.872895309579989e-09,2.132130609546431e-09,1.2136238776699982e-09,4.605355506384261e-10,1.310700522444994e-10,2.984240165009736e-11,5.662168950847596e-12,9.208419311894858e-13,1.3103744093438178e-13,1.6574987008008087e-14,1.8869200521695823e-15,1.9528150687426302e-16,1.8525936649850402e-17,1.755385997781917e-18,1.4993961761302858e-19,1.1379559290231378e-20],[1.9863967911071068e-10,2.2613423074747617e-10,1.2871720933271356e-10,4.8844499492289635e-11,1.3901317914406094e-11,3.165091533598669e-12,6.005308560034919e-13,9.766469315585333e-14,1.3897859151845256e-14,1.7579466848434163e-15,2.0012714632436496e-16,2.0711598594615926e-17,1.964864823211557e-18,1.7206384688749375e-19,1.513900736022615e-20,1.2069185043449047e-21],[1.9663249259592313e-11,2.2384922112341602e-11,1.2741656563478594e-11,4.835094240872311e-12,1.3760849816690233e-12,3.133109358271217e-13,5.944626955972709e-14,9.66778245908672e-15,1.3757426003750744e-15,1.7401832304554003e-16,1.981049294584119e-17,2.0502314922869577e-18,1.9450105312886797e-19,1.7032520013423073e-20,1.3850044707546332e-21,1.1373541685594898e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17489017922098163, "-10": 9.12243942858359e-08, "-11": 9.322892510163852e-09, "-12": 8.750416573924173e-10, "-13": 7.591206505651617e-11, "-14": 6.091501055777122e-12, "-15": 4.1548826019762595e-13, "-2": 0.08546450819375973, "-3": 0.028689917197700938, "-4": 0.007559221942687691, "-5": 0.0016325774893230704, "-6": 0.0002981043295060001, "-7": 4.709145259712904e-05, "-8": 6.550209413713829e-06, "-9": 8.134886092179404e-07, "0": 0.28710582238770593, "1": 0.20409003523981056, "10": 1.1436847704013568e-06, "11": 1.524495904959242e-07, "12": 1.866313292791066e-08, "13": 2.111771196890944e-09, "14": 2.210246012230523e-10, "15": 1.9663249259592313e-11, "2": 0.12792023918687112, "3": 0.05600966761231879, "4": 0.019248240339193354, "5": 0.0054221056510258435, "6": 0.0012913462056828337, "7": 0.0002660705025265683, "8": 4.8271418734351954e-05, "9": 7.819276851362416e-06} |
| Raw goal margin distribution | {"-1": 0.1652521797363055, "-10": 5.773030747405736e-08, "-11": 5.6170674898594745e-09, "-12": 5.01762781523617e-10, "-13": 4.123302417990868e-11, "-14": 2.874531429862869e-12, "-2": 0.07822354165681349, "-3": 0.02523152636806497, "-4": 0.006365028659636009, "-5": 0.0013134761141992575, "-6": 0.00022887408411593265, "-7": 3.4474072578530936e-05, "-8": 4.569632422881269e-06, "-9": 5.406004361840794e-07, "0": 0.29026665390569134, "1": 0.2192440754861437, "10": 8.226331875873252e-07, "11": 1.0439801311708681e-07, "12": 1.2163575945553516e-08, "13": 1.3037317772318943e-09, "14": 1.185469431062019e-10, "2": 0.1330754509004059, "3": 0.05598661757726273, "4": 0.01842134370886904, "5": 0.004958192194715218, "6": 0.0011268809387708664, "7": 0.0002213880834626988, "8": 3.82757008666867e-05, "9": 5.906068938355254e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.99, "date": "2026-11-01T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 5.0, "home_xg": 3.89, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 2.0, "away_xg": 1.63, "date": "2026-10-24T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.08, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 1.0, "away_xg": 1.07, "date": "2026-10-18T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 4.0, "home_xg": 2.41, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 0.36, "date": "2026-09-20T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 5.0, "away_xg": 1.73, "date": "2026-09-12T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.32, "date": "2026-08-22T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.85, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 3.0, "away_xg": 1.89, "date": "2026-08-17T00:00:00+00:00", "home": "Samsunspor", "home_goals": 3.0, "home_xg": 2.74, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 51.2% |
| P home draw | 70.1% |
| P draw away | 58.6% |
| P home away | 71.3% |
| Raw p home draw | 72.3% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0516 |
| Totals anchor target over 2 5 | 0.4849 |
| Totals anchor reference over odds | 1.98 |
| Totals anchor reference under odds | 1.87 |
| Totals anchor reference last update utc | 2026-11-06T11:25:08Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4555 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.25, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.25, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.18, "draw": 3.48, "home": 2.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.98, "under": 1.9}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.65, "home_away": 1.33, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.09, "draw": 3.32, "home": 2.37}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.98, "under": 1.87}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.98, "under": 1.87}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.3, "under": 3.56}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.37 |
| Reference draw odds | 3.32 |
| Reference away odds | 3.09 |
| Market reference 1x2 last update utc | 2026-11-06T11:25:08Z |
| Market reference home last update utc | 2026-11-06T11:25:08Z |
| Market reference draw last update utc | 2026-11-06T11:25:08Z |
| Market reference away last update utc | 2026-11-06T11:25:08Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.98 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference under 2 5 last update utc | 2026-11-06T11:25:08Z |
| Market best over 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market best under 2 5 last update utc | 2026-11-06T11:23:33Z |
| Home probability edge | +0.8% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0268 |
| Raw ev home | 0.0264 |
| Raw edge prob draw | 0.0045 |
| Raw ev draw | 0.0101 |
| Raw edge prob away | -0.0313 |
| Raw ev away | -0.1202 |
| Market p home draw | 69.0% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T11:23:33Z |
| Market reference home draw last update utc | 2026-11-06T11:25:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.8% |
| Market draw away odds | 1.65 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T11:23:33Z |
| Market reference draw away last update utc | 2026-11-06T11:25:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.1% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T11:23:33Z |
| Market reference home away last update utc | 2026-11-06T11:25:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.57 |
| Market reference dc home draw odds | 1.36 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 75.1% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.56 |
| Market reference over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.4% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.38 |
| Market reference under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,436.0175 |
| Elo away rating | 1,425.6973 |
| Elo rating diff | 70.3203 |
| Elo home expectancy | 0.5998 |
| Research p home | 0.4453 |
| Research p draw | 0.2659 |
| Research p away | 0.2888 |
| Research p over 1 5 | 0.7116 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4119969736997744, 1.0825638741932013], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T11:26:28.914251+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T11:26:28.849834+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T11:26:28.987803+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Samsunspor%22+%22Torku+Konyaspor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T11:25:35.001023+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T11:25:35.083842+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T11:26:29.045812+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Samsunspor_vs_Torku+Konyaspor&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.913613856180298, "goals_for": 0.9751316584067636, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.22037567410820427, "results": "LLLLLLLLWD", "xg_against": 2.102762810589968, "xg_for": 1.119679917641185, "xg_matches": 10}, "venue": {"goals_against": 2.9627088822913965, "goals_for": 0.9012025941363605, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.148698354997035, "results": "LLLLD", "xg_against": 1.764225747400591, "xg_for": 1.383053774479519, "xg_matches": 5}}}, "goal_rates": [1.4119969736997744, 1.0825638741932013], "h2h": [], "margin_distribution": {"-1": 0.177425024763834, "-10": 5.773030747405736e-08, "-11": 5.6170674898594745e-09, "-12": 5.01762781523617e-10, "-13": 4.123302417990868e-11, "-14": 2.874531429862869e-12, "-2": 0.07822354165681349, "-3": 0.02523152636806497, "-4": 0.006365028659636009, "-5": 0.0013134761141992575, "-6": 0.00022887408411593265, "-7": 3.4474072578530936e-05, "-8": 4.569632422881269e-06, "-9": 5.406004361840794e-07, "0": 0.2659209638506343, "1": 0.23141692051367224, "10": 8.226331875873252e-07, "11": 1.0439801311708681e-07, "12": 1.2163575945553516e-08, "13": 1.3037317772318943e-09, "14": 1.185469431062019e-10, "2": 0.1330754509004059, "3": 0.05598661757726273, "4": 0.01842134370886904, "5": 0.004958192194715218, "6": 0.0011268809387708664, "7": 0.0002213880834626988, "8": 3.82757008666867e-05, "9": 5.906068938355254e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T11:26:29.046120+00:00", "p_over_1_5": 0.7115845003983323, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Alanyaspor vs Trabzonspor

The model's most likely 1X2 outcome is **Trabzonspor win** at **55.6%**. Expected goals are 1.18 for Alanyaspor and 1.61 for Trabzonspor (2.79 combined). The most likely exact score is 1-2 at 11.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.1%; Under 3.5 goals: 68.9%; Double Chance 1X: 44.4%; Double Chance X2: 79.4%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 55.5%; BTTS No (at least one team does not score): 44.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alanyaspor win | 20.6% | 4.84 |
| Draw | 23.7% | 4.22 |
| Trabzonspor win | 55.6% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alanyaspor expected goals | 1.18 |
| Trabzonspor expected goals | 1.61 |
| Expected total goals | 2.79 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 78.3% |
| Under 1.5 | 21.7% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 31.1% |
| Under 3.5 | 68.9% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.30% |
| 2 | 1-1 | 11.27% |
| 3 | 0-1 | 10.58% |
| 4 | 0-2 | 9.60% |
| 5 | 0-0 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alanyaspor win | 20.6% | 18.0% | 5.16 | +6.5% |
| Draw | 23.7% | 22.3% | 4.13 | -2.1% |
| Trabzonspor win | 55.6% | 59.7% | 1.68 | -6.5% |
| Over 2.5 | 54.1% | 56.4% | 1.73 | -6.4% |
| Under 2.5 | 45.9% | 43.6% | 2.21 | +1.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T15:30:00+00:00 |
| Fixture id | a85eafd97e49ac329956fa1022be891d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T11:23:33Z |
| Market best draw last update utc | 2026-11-06T11:25:08Z |
| Market best away last update utc | 2026-11-06T11:23:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alanyaspor |
| Matched away-team name | Trabzonspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1769 |
| Dc lambda away | 1.6082 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.5% |
| P btts no | 44.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.57 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.60 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.22 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.41 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.06423605050608924,0.10584290598955229,0.09600835752973272,0.05146540007203663,0.02069106903340044,0.006654884052519924,0.0017836794577487003,0.00040977582988713734,8.23728171989919e-05,1.4718683877404405e-05,2.366990667608894e-06,3.460440835368557e-07,4.637434089076632e-08,5.736697709117932e-09,6.589637096377381e-10,7.064766406186427e-11],[0.04729027290138769,0.11272109288661855,0.11299214692488964,0.0605695816084229,0.024351299953558597,0.007832126868721465,0.0020992106993855553,0.0004822647941095853,9.694449215718691e-05,1.7322405403109216e-05,2.7857091212239524e-06,4.07258960943856e-07,5.457791878016075e-08,6.751514212828715e-09,7.755337786556643e-10,8.31451703056818e-11],[0.03293907988985936,0.05297110485443093,0.0486415740709105,0.03564214220703931,0.014329511164236097,0.004608811423583029,0.0012352795624996325,0.00028378849443318687,5.7046941449817826e-05,1.0193361425824132e-05,1.6392492404521316e-06,2.3965134669237057e-07,3.211635099451006e-08,3.97292540738014e-09,4.5636249237957166e-10,4.892673690602986e-11],[0.01292199085665728,0.020780548056739092,0.01670915814477487,0.010228969873231285,0.005621462799318584,0.001808035296515133,0.0004845997904437522,0.00011133013862415552,2.237949749293852e-05,3.998852535758093e-06,6.430769702048068e-07,9.40151492117966e-08,1.2599234565383816e-08,1.558577408962554e-09,1.7903086466193736e-10,1.91939437610227e-11],[0.0038019697633753595,0.0061141519332825545,0.004916248180531897,0.002635360982882556,0.0012099814304868768,0.000531968765859672,0.00014258126097156133,3.275608422082733e-05,6.584602460374857e-06,1.1765614600567877e-06,1.8920917243816916e-07,2.766158547607411e-08,3.7070068684179864e-09,4.5857207674022613e-10,5.267531464046483e-11,5.647333652286215e-12],[0.0008949069376054198,0.0014391479478286294,0.00115718558472756,0.0006203107792689191,0.00024938877649936667,9.160211158807258e-05,3.35607507574441e-05,7.710121027364872e-06,1.5498825056230236e-06,2.769388182059642e-07,4.453601990857831e-08,6.510978857897898e-09,8.725545890067817e-10,1.079386103540765e-10,1.2398705788351728e-11,1.3292683474464903e-12],[0.00017553585746723433,0.0002822886474880526,0.00022698177355446721,0.00012167386345947417,4.891756995722687e-05,1.5733394715897686e-05,4.815814751352393e-06,1.5123390476065175e-06,3.040092138809176e-07,5.432150637900253e-08,8.735733420224146e-09,1.277127496441502e-09,1.711514477450711e-10,2.1172141734673442e-11,2.432004223663648e-12,2.6073578085943317e-13],[2.951256969088314e-05,4.746074962770146e-05,3.816209125156595e-05,2.0456836721107048e-05,8.224434672789225e-06,2.6452310925349015e-06,7.089897169532286e-07,1.8601179388253705e-07,5.111259454784568e-08,9.132990067418643e-09,1.4687252227851274e-09,2.1472145228167094e-10,2.877542572869935e-11,3.559639138495903e-12,4.0888907357742056e-13,4.38370998071275e-14],[4.341664486878907e-06,6.98206402687114e-06,5.614116224624763e-06,3.009454020310118e-06,1.209916192236393e-06,3.8914625240493593e-07,1.0430116753300066e-07,2.3961759103273965e-08,5.500818245599231e-09,1.3435759423883206e-09,2.1606766904880384e-10,3.1588184753372375e-11,4.2332214812087075e-12,5.23667000047308e-13,6.015264642889792e-14,6.448980262778203e-15],[5.677445452809466e-07,9.130205196735578e-07,7.3413868638092e-07,3.9353596056731395e-07,1.5821658271045125e-07,5.088731816728863e-08,1.3639105258422267e-08,3.133396895898671e-09,6.298729961424008e-10,1.285313488103994e-10,2.8254426587949428e-11,4.130678370761478e-12,5.535638260823092e-13,6.847813407024066e-14,7.865954865335666e-15,8.433109877287784e-16],[6.68178028733828e-08,1.0745330027382765e-07,8.640071390567126e-08,4.631521069702575e-08,1.8620494943929105e-08,5.988923755092061e-09,1.605185032778441e-09,3.687691900423675e-10,7.412969449258812e-11,1.3245771800291466e-11,2.4326288527333194e-12,4.861391543168544e-13,6.514887534621743e-14,8.059185247087168e-15,9.257434985004394e-16,9.924919192510344e-17],[7.148891838665258e-09,1.149651722043107e-08,9.244083641384696e-09,4.955302591817571e-09,1.992222111655064e-09,6.407598920350219e-10,1.717400705635693e-10,3.945491979197146e-11,7.931197153624432e-12,1.417176049613079e-12,2.27903697893982e-13,3.805022871383005e-14,6.9703319060544075e-15,8.622588765507558e-16,9.90460604289571e-17,1.0618752901708106e-17],[7.011270145018839e-10,1.127520037767879e-09,9.066127886052686e-10,4.859909186712739e-10,1.9538702961131177e-10,6.284247688365402e-11,1.6843394145834467e-11,3.8695382089206545e-12,7.778515477980388e-13,1.3898943152485953e-13,2.2351637555084418e-14,3.2677154325710146e-15,5.001054275812575e-16,8.456597266922055e-17,9.713934720782328e-18,1.0414333700561159e-18],[6.347351792630863e-11,1.0207517589430915e-10,8.207628846057328e-11,4.39970970312989e-11,1.768852414767206e-11,5.6891732888685186e-12,1.5248442267126952e-12,3.503119945320569e-13,7.041944347022884e-14,1.25828102340748e-14,2.0235093466523273e-15,2.9582855858824474e-16,3.964481716022219e-17,5.600691505378336e-18,8.794092894461025e-19,9.428168978808511e-20],[5.335851740933794e-12,8.580869987923291e-12,6.8996791257132e-12,3.698581620496329e-12,1.4869719758952453e-12,4.782559119084351e-13,1.2818483971857204e-13,2.944870438824552e-14,5.919755550219295e-15,1.0577641209563283e-15,1.7010473379883996e-16,2.4868596872062797e-17,3.3327106102574246e-18,4.1227008202770074e-19,5.408195329801362e-20,7.925716661521595e-21],[4.186505976449694e-13,6.732545286442285e-13,5.413483975536478e-13,2.90190485237978e-13,1.1666772928007215e-13,3.752392927481649e-14,1.0057374597858162e-14,2.310543525306317e-15,4.64463654415128e-16,8.299210752213946e-17,1.334640689522981e-17,1.9511885728029802e-18,2.6148426839869967e-19,3.234668514268583e-20,3.715603072867086e-21,4.549216850296929e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2606657522613828, "-10": 2.8079785615392103e-06, "-11": 4.047796059227109e-07, "-12": 5.3601411539735634e-08, "-13": 6.561158224679625e-09, "-14": 7.421088799434198e-10, "-15": 7.064766406186427e-11, "-2": 0.17286609034337405, "-3": 0.08094447302872995, "-4": 0.029876676099281782, "-5": 0.009061485147746124, "-6": 0.0023271859407672413, "-7": 0.000517585316167898, "-8": 0.00010143230441308513, "-9": 1.7757114811404422e-05, "0": 0.23713427833729053, "1": 0.11987175264951734, "10": 7.926645447535561e-08, "11": 8.362303414243486e-09, "12": 8.103920600071443e-10, "13": 7.259573631178556e-11, "14": 6.0091062695780224e-12, "15": 4.186505976449694e-13, "2": 0.05930785721758299, "3": 0.020323629834998743, "4": 0.005489818770420526, "5": 0.0012185315115529132, "6": 0.0002290235377346727, "7": 3.727714423417816e-05, "8": 5.346242229748238e-06, "9": 6.849460969522644e-07} |
| Raw goal margin distribution | {"-1": 0.21670403712841482, "-10": 2.3344082802462367e-06, "-11": 3.365128483113563e-07, "-12": 4.4561443824790315e-08, "-13": 5.454607915276257e-09, "-14": 6.169509760197607e-10, "-15": 5.873281734589464e-11, "-2": 0.14371193505486152, "-3": 0.06729305225708604, "-4": 0.024837924700595804, "-5": 0.0075332505204853085, "-6": 0.0019347021391864759, "-7": 0.00043029368683423813, "-8": 8.432557660859349e-05, "-9": 1.476234769623854e-05, "0": 0.2694804284273124, "1": 0.15556817768188969, "10": 1.0287109015657819e-07, "11": 1.0852500898860773e-08, "12": 1.0517174663474947e-09, "13": 9.421390908098095e-11, "14": 7.798548792294102e-12, "15": 5.433199158394397e-13, "2": 0.07696905288882702, "3": 0.026375772335258073, "4": 0.007124623466674508, "5": 0.0015813961380417715, "6": 0.00029722410513020875, "7": 4.837784773742028e-05, "8": 6.938291488568173e-06, "9": 8.889151427086917e-07} |
| Research history json | {"away": [{"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.51, "date": "2026-11-01T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 1.37, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 4.0, "away_xg": 2.63, "date": "2026-10-26T00:00:00+00:00", "home": "Rizespor", "home_goals": 3.0, "home_xg": 1.81, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 1.19, "date": "2026-10-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.35, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": 0.92, "date": "2026-09-12T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Genclerbirligi", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-06T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": 3.2, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-08-31T00:00:00+00:00", "home": "Amedspor", "home_goals": 2.0, "home_xg": 2.39, "source": "pipeline training history"}, {"away": "Buyuksehyr", "away_goals": 1.0, "away_xg": 1.95, "date": "2026-08-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-08-15T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 1.0, "home_xg": 1.86, "source": "pipeline training history"}], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-11-02T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 5.0, "home_xg": 1.91, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Erzurumspor", "away_goals": 0.0, "away_xg": 1.69, "date": "2026-10-10T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 0.0, "home_xg": 0.98, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-19T00:00:00+00:00", "home": "Corum", "home_goals": 1.0, "home_xg": 1.14, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 1.79, "date": "2026-09-12T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": 1.73, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 2.06, "date": "2026-09-07T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 0.74, "date": "2026-08-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.54, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 1.25, "date": "2026-08-15T00:00:00+00:00", "home": "Gaziantep", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 46.3% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 56.5% |
| P home draw | 44.4% |
| P draw away | 79.4% |
| P home away | 76.3% |
| Raw p home draw | 53.7% |
| Raw p draw away | 73.2% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5410 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.68, "draw": 4.11, "home": 5.16}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.73, "under": 2.21}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.63, "draw": 4.13, "home": 5.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.06 |
| Reference draw odds | 4.13 |
| Reference away odds | 1.63 |
| Market reference 1x2 last update utc | 2026-11-06T11:25:08Z |
| Market reference home last update utc | 2026-11-06T11:25:08Z |
| Market reference draw last update utc | 2026-11-06T11:25:08Z |
| Market reference away last update utc | 2026-11-06T11:25:08Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market reference under 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market best over 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market best under 2 5 last update utc | 2026-11-06T11:23:33Z |
| Home probability edge | +2.6% |
| Draw probability edge | +1.4% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | 0.0878 |
| Raw ev home | 0.3827 |
| Raw edge prob draw | 0.0462 |
| Raw ev draw | 0.1130 |
| Raw edge prob away | -0.1340 |
| Raw ev away | -0.2229 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,452.1266 |
| Elo away rating | 1,593.6095 |
| Elo rating diff | -81.4829 |
| Elo home expectancy | 0.3848 |
| Research p home | 0.2847 |
| Research p draw | 0.2480 |
| Research p away | 0.4673 |
| Research p over 1 5 | 0.7654 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.1768990724572832, 1.6081537502429943], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T11:26:29.185741+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T11:26:28.849834+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T11:26:29.317989+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Alanyaspor%22+%22Trabzonspor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T11:25:35.001023+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T11:25:35.083842+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T11:26:29.375788+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Alanyaspor_vs_Trabzonspor&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.7743771520489182, "goals_for": 2.5504665648542564, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.445760234190055, "results": "WWWWWLWLWD", "xg_against": 1.304688418272264, "xg_for": 1.9416908629267322, "xg_matches": 10}, "venue": {"goals_against": 1.4632227425095123, "goals_for": 2.031257084649452, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.6015486554658407, "results": "WWLLD", "xg_against": 1.7335781977270697, "xg_for": 1.5880534238553998, "xg_matches": 5}}, "home": {"all": {"goals_against": 2.0080296773705193, "goals_for": 0.7681538045198641, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 0.9433296058372811, "results": "LLLDWDWLWD", "xg_against": 1.821921306986439, "xg_for": 0.9535220089451488, "xg_matches": 10}, "venue": {"goals_against": 1.069203922761527, "goals_for": 0.9657278891499795, "last_match": "2026-10-23T00:00:00+00:00", "matches": 4, "points_per_game": 1.0971691275701443, "results": "LDDW", "xg_against": 1.4768169943171596, "xg_for": 0.9185985305199439, "xg_matches": 4}}}, "goal_rates": [1.1876351419922726, 1.5916042512322786], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.22673324062836298, "-10": 2.1168191594815623e-06, "-11": 3.020116436432031e-07, "-12": 3.9581775893151146e-08, "-13": 4.795270202121306e-09, "-14": 5.368083668709388e-10, "-15": 5.0584610920746295e-11, "-2": 0.14149152762959513, "-3": 0.06558119717637168, "-4": 0.023959315747229027, "-5": 0.007192486089263, "-6": 0.001828270549445674, "-7": 0.00040245368550146727, "-8": 7.806048938032887e-05, "-9": 1.3525266430525002e-05, "0": 0.248034994144928, "1": 0.16918550212438194, "10": 1.1328261122134404e-07, "11": 1.2060106132196626e-08, "12": 1.1794259193948873e-09, "13": 1.0661944688436585e-10, "14": 8.906161520201934e-12, "15": 6.262354580060675e-13, "2": 0.07878187889288492, "3": 0.027247282117510145, "4": 0.007427902736302519, "5": 0.0016638676475463426, "6": 0.0003155935797562851, "7": 5.183839591307836e-05, "8": 7.502653065155519e-06, "9": 9.700125943251274e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T11:26:29.376090+00:00", "p_over_1_5": 0.7653632305558433, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Besiktas JK vs Genclerbirligi SK

The model's most likely 1X2 outcome is **Besiktas JK win** at **76.5%**. Expected goals are 1.92 for Besiktas JK and 0.81 for Genclerbirligi SK (2.73 combined). The most likely exact score is 2-0 at 14.7%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 55.4%; Under 3.5 goals: 68.8%; Double Chance 1X: 91.3%; Double Chance X2: 23.5%; Double Chance 12 (either team wins): 85.2%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 45.6%; BTTS No (at least one team does not score): 54.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Besiktas JK win | 76.5% | 1.31 |
| Draw | 14.8% | 6.76 |
| Genclerbirligi SK win | 8.7% | 11.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Besiktas JK expected goals | 1.92 |
| Genclerbirligi SK expected goals | 0.81 |
| Expected total goals | 2.73 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 55.4% |
| Under 2.5 | 44.6% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.72% |
| 2 | 1-0 | 14.12% |
| 3 | 2-1 | 11.90% |
| 4 | 3-0 | 9.43% |
| 5 | 3-1 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Besiktas JK win | 76.5% | 82.5% | 1.22 | -6.6% |
| Draw | 14.8% | 11.2% | 7.55 | +11.7% |
| Genclerbirligi SK win | 8.7% | 6.4% | 13.10 | +13.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T18:00:00+00:00 |
| Fixture id | 1fa78d1150755a8ec1d24cc1e19eeb0a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T11:23:33Z |
| Market best draw last update utc | 2026-11-06T11:23:33Z |
| Market best away last update utc | 2026-11-06T11:23:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Besiktas |
| Matched away-team name | Genclerbirligi |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9218 |
| Dc lambda away | 0.8084 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 45.6% |
| P btts no | 54.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.99 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.65 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.33 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.04763193870447873,0.026439990996475402,0.013119141468247851,0.0035349697197258143,0.0007143766390671822,0.00011549382832835273,1.5559981075898277e-05,1.796853053312533e-06,1.8156164647749405e-07,1.6307340540407683e-08,1.3182102310380256e-09,9.687094364916405e-11,6.525500417650345e-12,4.0576259280173064e-13,2.3428555286777728e-14,1.262570934479639e-15,6.378775861391498e-17],[0.141208491635345,0.07055887540935749,0.025212210158155147,0.006793462795728599,0.0013728805348909648,0.00022195466668545802,2.9902986707777217e-05,3.4531708430070626e-06,3.4892301441601997e-07,3.133925324461593e-08,2.533320755630186e-09,1.8616542823420886e-10,1.2540629149790146e-11,7.797897285272185e-13,4.5024719111523314e-14,2.4263938167541076e-15,1.2258655641332038e-16],[0.14716488468439773,0.11896130835056078,0.024991615603287224,0.006527798031679927,0.0013191927479205049,0.0002132749202987451,2.8733602235241782e-05,3.3181313432980136e-06,3.352780511501188e-07,3.011370221577578e-08,2.434252860354856e-09,1.788852537410244e-10,1.2050216029960353e-11,7.492953164039911e-13,4.326398504426068e-14,2.331507400179863e-15,1.1779269361251717e-16],[0.09427324213107077,0.07620614286086126,0.030800766359853397,0.00431378865293887,0.0008450696482993767,0.00013662306904889008,1.8406631762937194e-05,2.125581793647766e-06,2.1477779135350822e-07,1.9290718343163087e-08,1.5593727389833956e-09,1.1459318488762789e-10,7.719320651529049e-12,4.799956113343099e-13,2.7714737427881965e-14,1.493554404224273e-15,7.545753288917008e-17],[0.04529329908233402,0.03661301491794634,0.014798136684026726,0.003987377162827769,0.0004188378503078554,6.564014759749373e-05,8.843411541718176e-06,1.0212294573448414e-06,1.031893517196796e-07,9.268168312437656e-09,7.491959993209485e-10,5.505595520621113e-11,3.708724671800694e-12,2.3061246532866777e-13,1.3315463252702677e-14,7.17573775941791e-16,3.625334748127662e-17],[0.017408824776892897,0.014072491387780097,0.0056877766419362544,0.0015325788086416403,0.00030971651392474193,2.6026331315011353e-05,3.399032640123388e-06,3.9251732684784643e-07,3.966161395449633e-08,3.562291142905722e-09,2.879591935226164e-10,2.116117607964722e-11,1.4254765995241964e-12,8.863765902713712e-14,5.117899806063586e-15,2.758049509079901e-16,1.393425046672121e-17],[0.005576012093268757,0.004507391117224351,0.0018217835922700678,0.0004908819567312821,9.920158593483364e-05,1.603799775818333e-05,1.1230975868718527e-06,1.2572252230525062e-07,1.2703536389335728e-08,1.140994797015337e-09,9.223275930614562e-11,6.777882783019314e-12,4.565773312951442e-13,2.839046661612509e-14,1.6392531705314633e-15,8.833977947136471e-17,4.4631128240318035e-18],[0.0015308448246094649,0.0012374643829455188,0.0005001545794980852,0.00013476730150269972,2.7234918411442478e-05,4.403090498109111e-06,5.932092287326678e-07,3.5606431854348536e-08,3.4876436081135455e-09,3.132500343795556e-10,2.5321688669526015e-11,1.8608077971567286e-12,1.253492698645559e-13,7.794351619145261e-15,4.500424658981806e-16,2.425290547237735e-17,1.2253081689986053e-18],[0.0003677449238102919,0.00029726804304959086,0.0001201488908438609,3.2374274796841185e-05,6.542467815933267e-06,1.0577258737965386e-06,1.4250280571677754e-07,1.645609980557205e-08,8.642821064523179e-10,7.525002415308082e-11,6.082865043423555e-12,4.4700978870642314e-13,3.011184213774022e-14,1.872386538631982e-15,1.0811078279951948e-16,5.826118187643823e-18,2.94347834613135e-19],[7.852531378706772e-05,6.347624358066906e-05,2.565563450047622e-05,6.912944061090979e-06,1.397026321573316e-06,2.258583348479359e-07,3.0428910937789356e-08,3.5139041147185636e-09,3.5505976154043114e-10,1.6575916245650027e-11,1.2988864164597666e-12,9.54508999345713e-14,6.429842261514103e-15,3.9981446637889156e-16,2.3085113059173654e-17,1.2440627435588541e-18,6.285268559536664e-20],[1.5090901479538958e-05,1.2198789052465423e-05,4.930469347650153e-06,1.3285213739148242e-06,2.6847885817245423e-07,4.3405186367867134e-08,5.847791940533063e-09,6.752979166381574e-10,6.823496299912494e-11,6.128666488639602e-12,2.5750435863310235e-13,1.834364051001312e-14,1.2356794442184764e-15,7.683586898588053e-17,4.4364695920181275e-18,2.390824995404665e-19,1.2078954419922658e-20],[2.6365013740281136e-06,2.13122616577355e-06,8.613924905220613e-07,2.3210332613338092e-07,4.690540717059932e-08,7.58323375538492e-09,1.0216560957044283e-09,1.1797995550556188e-10,1.192119463160438e-11,1.0707271292020928e-12,8.655264498014137e-14,3.306025926005179e-15,2.1588309730585027e-16,1.3423841804983215e-17,7.750867760318243e-19,4.176962783828162e-20,2.110290095533907e-21],[4.2223308390735355e-07,3.4131375972080773e-07,1.3795115424957394e-07,3.717111780932707e-08,7.511854504105055e-09,1.2144473756274153e-09,1.6361721189735567e-10,1.8894373029002855e-11,1.909167513716013e-12,1.7147588931294308e-13,1.3861320373396374e-14,1.0186229428191686e-15,3.566570423133988e-17,2.149814970338066e-18,1.2412937954958024e-19,6.689364530417285e-21,3.3796086880663395e-22],[6.241865558377608e-08,5.045636361998436e-08,2.03932991342239e-08,5.495000957133533e-09,1.1104763623639974e-09,1.7953157948310208e-10,2.4187508715540723e-11,2.79315242579971e-12,2.8223195678461254e-13,2.5349255858630965e-14,2.0491169813525314e-15,1.5058288196931788e-16,1.0143688315255262e-17,3.2784694412168294e-19,1.8350028184037637e-20,9.888877887883873e-22,4.9960706242203647e-23],[8.56824503437267e-09,6.926174282289452e-09,2.799399993592743e-09,7.543019666875072e-10,1.5243573397448585e-10,2.464440398519254e-11,3.3202333422196407e-12,3.834176526036052e-13,3.8742144309971135e-14,3.4797070459846878e-15,2.812834758473405e-16,2.0670599496707068e-17,1.3924299750538144e-18,8.658278458529693e-20,2.598496339716775e-21,1.3574519999819073e-22,6.858135106722466e-24],[1.0977567651359656e-09,8.873759614007892e-10,3.5865690919902697e-10,9.664057033438941e-11,1.9529945461137236e-11,3.157421512685486e-12,4.2538566516596645e-13,4.912316586765023e-14,4.963612833378602e-15,4.458173097404481e-16,3.603781606310989e-17,2.6483008300879694e-18,1.7839702517393546e-19,1.109291776104984e-20,6.405002374958362e-22,1.7940999418219275e-23,8.786588361349616e-25],[1.3185349405356778e-10,1.0658428603293205e-10,4.307891160068384e-11,1.1607668720985353e-11,2.3457760676224277e-12,3.792434461525898e-13,5.109381973654859e-14,5.900269772257254e-15,5.961882595449432e-16,5.3547900469152736e-17,4.328565413479638e-18,3.180920663320287e-19,2.142758017531531e-20,1.3323898449053443e-21,7.69316090213354e-23,4.145864407947825e-24,1.0887137492790275e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.05909423730158085, "-10": 1.5169194666448453e-09, "-11": 1.1018931436081247e-10, "-12": 7.35008393897353e-12, "-13": 4.5319427684632297e-13, "-14": 2.5972741797144352e-14, "-15": 1.3851574908929593e-15, "-16": 6.378775861391498e-17, "-2": 0.021377669032780395, "-3": 0.005140593864519764, "-4": 0.0009672973355484756, "-5": 0.00014893928720341522, "-6": 1.9368491510055073e-05, "-7": 2.177505652961516e-06, "-8": 2.1545354479348371e-07, "-9": 1.9027501690360644e-08, "0": 0.1479422421368228, "1": 0.29528430804687444, "10": 1.7365729444768525e-05, "11": 2.99898264403874e-06, "12": 4.7558783386733263e-07, "13": 6.971509444398555e-08, "14": 9.498699907374141e-09, "15": 1.2043410511688977e-09, "16": 1.3185349405356778e-10, "2": 0.23980549380038985, "3": 0.1370932394082735, "4": 0.061329115657744356, "5": 0.022450186220756334, "6": 0.006940814539660713, "7": 0.0018551451679639365, "8": 0.0004363914348207808, "9": 9.162380199991681e-05} |
| Raw goal margin distribution | {"-1": 0.09596816354456597, "-10": 2.463454680292725e-09, "-11": 1.7894580968149929e-10, "-12": 1.1936427132850559e-11, "-13": 7.359807734871257e-13, "-14": 4.2179346858622615e-14, "-15": 2.2494751889697383e-15, "-16": 1.0359037243446626e-16, "-2": 0.03471701694819216, "-3": 0.008348248073475477, "-4": 0.0015708765039202167, "-5": 0.00024187518995470746, "-6": 3.1454142497220763e-05, "-7": 3.5362368339939193e-06, "-8": 3.4989335622484433e-07, "-9": 3.0900380095373303e-08, "0": 0.23289831293069307, "1": 0.24161927294878408, "10": 1.4209677955539012e-05, "11": 2.453946878625312e-06, "12": 3.891543963252889e-07, "13": 5.7045057844515235e-08, "14": 7.772404096780166e-09, "15": 9.854638436107157e-10, "16": 1.078904110404762e-10, "2": 0.19622319060712326, "3": 0.11217788392183159, "4": 0.050183148687548196, "5": 0.018370084438631494, "6": 0.00567938937845269, "7": 0.001517990677062126, "8": 0.0003570815594634842, "9": 7.497207206997596e-05} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 62.6% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 14.1% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 48.3% |
| P home draw | 91.3% |
| P draw away | 23.5% |
| P home away | 85.2% |
| Raw p home draw | 85.9% |
| Raw p draw away | 37.4% |
| Raw p home away | 76.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5539 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -2.0, "market_key": "spreads", "opposite_price": 1.87, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 13.1, "draw": 7.55, "home": 1.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 12.07, "draw": 7.26, "home": 1.19}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.19 |
| Reference draw odds | 7.26 |
| Reference away odds | 12.07 |
| Market reference 1x2 last update utc | 2026-11-06T11:25:08Z |
| Market reference home last update utc | 2026-11-06T11:25:08Z |
| Market reference draw last update utc | 2026-11-06T11:25:08Z |
| Market reference away last update utc | 2026-11-06T11:25:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.01 |
| Market reference over 2 5 last update utc | 2026-11-06T11:24:45Z |
| Market reference under 2 5 last update utc | 2026-11-06T11:24:45Z |
| Home probability edge | -6.0% |
| Draw probability edge | +3.6% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -15.8% |
| Under 2.5 probability edge | +15.8% |
| Raw edge prob home | -0.1987 |
| Raw ev home | -0.2360 |
| Raw edge prob draw | 0.1214 |
| Raw ev draw | 0.7584 |
| Raw edge prob away | 0.0773 |
| Raw ev away | 0.8455 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,572.0567 |
| Elo away rating | 1,407.1890 |
| Elo rating diff | 224.8678 |
| Elo home expectancy | 0.7849 |
| Research p home | 0.6360 |
| Research p draw | 0.2133 |
| Research p away | 0.1507 |
| Research p over 1 5 | 0.7568 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.9217881154171597, 0.8083538991361907], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T11:26:29.185741+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T11:26:28.849834+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T11:26:29.394787+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Besiktas+JK%22+%22Genclerbirligi+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T11:25:35.001023+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T11:25:35.083842+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T11:26:29.452806+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Besiktas+JK_vs_Genclerbirligi+SK&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.9217881154171597, 0.8083538991361907], "h2h": [], "margin_distribution": {"-1": 0.10574279151728629, "-10": 2.4634546802927243e-09, "-11": 1.7894580968149923e-10, "-12": 1.1936427132850557e-11, "-13": 7.359807734871255e-13, "-14": 4.21793468586226e-14, "-15": 2.249475188969738e-15, "-16": 1.0359037243446624e-16, "-2": 0.03471701694819215, "-3": 0.008348248073475475, "-4": 0.0015708765039202162, "-5": 0.00024187518995470744, "-6": 3.145414249722076e-05, "-7": 3.5362368339939184e-06, "-8": 3.498933562248443e-07, "-9": 3.09003800953733e-08, "0": 0.21334905698525236, "1": 0.2513939009215044, "10": 1.4209677955539009e-05, "11": 2.4539468786253114e-06, "12": 3.8915439632528884e-07, "13": 5.704505784451522e-08, "14": 7.772404096780163e-09, "15": 9.854638436107155e-10, "16": 1.0789041104047617e-10, "2": 0.1962231906071232, "3": 0.11217788392183156, "4": 0.05018314868754818, "5": 0.018370084438631494, "6": 0.005679389378452688, "7": 0.0015179906770621256, "8": 0.00035708155946348414, "9": 7.497207206997595e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T11:26:29.453108+00:00", "p_over_1_5": 0.7567573338937171, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Çaykur Rizespor vs Erzurum BB

The model's most likely 1X2 outcome is **Çaykur Rizespor win** at **49.0%**. Expected goals are 1.42 for Çaykur Rizespor and 0.93 for Erzurum BB (2.35 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.5%; Double Chance 1X: 75.8%; Double Chance X2: 51.0%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çaykur Rizespor win | 49.0% | 2.04 |
| Draw | 26.8% | 3.73 |
| Erzurum BB win | 24.2% | 4.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çaykur Rizespor expected goals | 1.42 |
| Erzurum BB expected goals | 0.93 |
| Expected total goals | 2.35 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.75% |
| 2 | 2-1 | 9.49% |
| 3 | 1-0 | 9.11% |
| 4 | 2-0 | 8.58% |
| 5 | 0-0 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çaykur Rizespor win | 49.0% | 49.9% | 2.01 | -1.5% |
| Draw | 26.8% | 25.7% | 3.71 | -0.6% |
| Erzurum BB win | 24.2% | 24.5% | 3.82 | -7.6% |
| Over 2.5 | 52.6% | 52.6% | 1.86 | -2.1% |
| Under 2.5 | 47.4% | 47.4% | 2.03 | -3.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T10:30:00+00:00 |
| Fixture id | cf2febfddf729564889172cf83e8fbab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T11:23:33Z |
| Market best draw last update utc | 2026-11-06T11:23:33Z |
| Market best away last update utc | 2026-11-06T11:25:08Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Rizespor |
| Matched away-team name | Erzurumspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4173 |
| Dc lambda away | 0.9324 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.57 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.28 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.67 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.07367510325933997,0.05766565160308147,0.03809523137163816,0.014054185331332441,0.003888678153714276,0.0008607723565143003,0.0001587791147469742,2.510450436654426e-05,3.4731055336364274e-06,4.2710217777495776e-07,4.727027199262946e-08,4.756108258126401e-09,4.386587540544122e-10,3.734562773375944e-11,2.9523513719280403e-12,2.178377285046848e-13],[0.0910727035185303,0.12750999698543938,0.06409008921445221,0.023644271455774298,0.006542176561851451,0.0014481334050488927,0.000267124447421035,4.223494297331627e-05,5.843031673189559e-06,7.185418145973787e-07,7.952585770235127e-08,8.001510729866614e-09,7.379841956539034e-10,6.282898218616175e-11,4.966933025642413e-12,3.6648260035330796e-13],[0.08576803486950238,0.09492525553664873,0.054132296589195446,0.0198891490148487,0.005503164889791397,0.001218144578498474,0.00022470042903219138,3.552729784891635e-05,4.915056395961267e-06,6.044248498270782e-07,6.68957653161033e-08,6.730731354861122e-09,6.20779441879533e-10,5.2850644668379914e-11,4.178097484566382e-12,3.082787754069746e-13],[0.04809771729616072,0.05323298023575244,0.02945826064188505,0.011199290733558145,0.0030861109212316014,0.0006831213242977546,0.0001260093894929538,1.9923295792349912e-05,2.7563065119461237e-06,3.389544321260241e-07,3.751436783388807e-08,3.774515930032447e-09,3.481258973021804e-10,2.9638027384529376e-11,2.3430285181913483e-12,1.7287915492632665e-13],[0.020229480708820573,0.022389327545865458,0.012389887688453565,0.004570907474197935,0.0013033081537479965,0.0002873148753936493,5.299845101134231e-05,8.379564572800218e-06,1.1592784968916066e-06,1.425612800632842e-07,1.577821616203426e-08,1.587528504140097e-09,1.4641871838432243e-10,1.2465496013689015e-11,9.854573745592656e-13,7.271146586864086e-14],[0.006806674624139964,0.007533404828901582,0.0041688630241590585,0.001537987077461106,0.00042554844751366695,9.706969823215397e-05,1.783254927845654e-05,2.819497463133193e-06,3.9006594586793386e-07,4.796802554445016e-08,5.308944164715296e-09,5.341605224457232e-10,4.926594949573319e-11,4.194303186275006e-12,3.315798265478669e-13,2.4465447073799463e-14],[0.0019085520164765233,0.002112322943444761,0.001168924970051511,0.0004312426405095151,0.00011932131216177877,2.641218506442108e-05,5.0206246567120035e-06,7.905707068219405e-07,1.0937222486070158e-07,1.3449955658902261e-08,1.488597097765474e-09,1.4977550691498646e-10,1.3813885993645915e-11,1.1760582436964248e-12,9.297305681933156e-14,6.8599692103836154e-15],[0.0004586973397315683,0.0005076712117078349,0.00028093694564233356,0.0001036439406800757,2.8677430842535907e-05,6.3478484845879685e-06,1.1709318442942522e-06,1.9078237480555224e-07,2.628628832278087e-08,3.2325337884349506e-09,3.5776626614439223e-10,3.599672735442916e-11,3.3200000324531352e-12,2.826513414860162e-13,2.234494709160258e-14,1.6487104361203758e-15],[9.646205170351991e-05,0.00010676104356918183,5.907981544396713e-05,2.1795869081099784e-05,6.030738740005898e-06,1.3349248746129013e-06,2.462418643450368e-07,3.893320584717381e-08,5.5505350872448496e-09,6.797877694600626e-10,7.52366867503342e-11,7.569954901531526e-12,6.981815394298912e-13,5.944034541915817e-14,4.699045001926452e-15,3.467166202146415e-16],[1.8031599222650494e-05,1.9956784209278522e-05,1.1043757990012763e-05,4.074290034672875e-06,1.1273227352713512e-06,2.495367857750889e-07,4.602985869878561e-08,7.277763139922657e-09,1.0068487736187086e-09,1.2759287089351203e-10,1.4063953216460777e-11,1.4150475809646731e-12,1.3051069805509395e-13,1.1111151663541266e-14,8.78389944103219e-16,6.481155054381044e-17],[3.0335733929136696e-06,3.3574598036395395e-06,1.8579633443824928e-06,6.854443519724691e-07,1.8965684700057055e-07,4.198119892380999e-08,7.743902961907486e-09,1.224385499510453e-09,1.6938872767872609e-10,2.0830433680016863e-11,2.3757622935508364e-12,2.3806267199689355e-13,2.1956664864932977e-14,1.869301421074546e-15,1.4777726202383775e-16,1.0903669322697085e-17],[4.639616474774666e-07,5.134975753264403e-07,2.8416115997921947e-07,1.0483342566827476e-07,2.9006551611810858e-08,6.420700504978498e-09,1.1843702164928889e-09,1.872603164398063e-10,2.590669912305967e-11,3.1858541317730265e-12,3.525999144333635e-13,3.6558990137748515e-14,3.3581025030221895e-15,2.85895231339932e-16,2.2601392176121386e-17,1.6676321048719126e-18],[6.504607512165126e-08,7.199086829928462e-08,3.983856911267988e-08,1.469734172717331e-08,4.066634269061084e-09,9.001635580249966e-10,1.6604526363913382e-10,2.6253352355033625e-11,3.6320439555176774e-12,4.4664749405174875e-13,4.9433483665768465e-14,4.97376025099617e-15,4.727246778677852e-16,4.008168087980215e-17,3.1686495238020574e-18,2.3379717646606576e-19],[8.417788400071065e-09,9.31653285686175e-09,5.155616911934483e-09,1.902022719610621e-09,5.262741328114254e-10,1.1649259917278698e-10,2.1488366385429946e-11,3.397517290687687e-12,4.70032625644589e-13,5.780185948680149e-14,6.3973207391616786e-15,6.436677580817459e-16,5.936586836573887e-17,5.20832583242879e-18,4.100634996879814e-19,3.025632455678064e-20],[1.011556696438444e-09,1.1195578637813856e-09,6.195450115489468e-10,2.2856405119234666e-10,6.324180389272296e-11,1.3998791984098507e-11,2.582234178340824e-12,4.0827604631063376e-13,5.648332167761717e-14,6.945988097060556e-15,7.68759242381158e-16,7.734887122651048e-17,7.133933383825539e-18,6.073541630420532e-19,4.9478742139360035e-20,3.635870404483916e-21],[1.1345384813435852e-10,1.2556700806024433e-10,6.948672862347161e-11,2.5635212780708682e-11,7.093053745628085e-12,1.5700719746310683e-12,2.896173841251988e-13,4.57912924882127e-14,6.33503808763176e-15,7.790458819377956e-16,8.622224996787804e-17,8.675269631839752e-18,8.001253885015686e-19,6.811943138743949e-20,5.385168463237925e-21,4.0946115591929157e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.14503696572937438, "-10": 5.592321011458177e-08, "-11": 5.549358838432745e-09, "-12": 5.058387128800667e-10, "-13": 4.2620839534808833e-11, "-14": 3.3188339722813483e-12, "-15": 2.178377285046848e-13, "-2": 0.06798171967140872, "-3": 0.021949299307118274, "-4": 0.005582644055413413, "-5": 0.0011663284316762621, "-6": 0.00020628439502636342, "-7": 3.159111325059833e-05, "-8": 4.26246833712328e-06, "-9": 5.137196966652817e-07, "0": 0.2679222825070854, "1": 0.22048029869692704, "10": 3.5888763719482678e-06, "11": 5.413437897936237e-07, "12": 7.500778820284266e-08, "13": 9.606832992475921e-09, "14": 1.1371237044986882e-09, "15": 1.1345384813435852e-10, "2": 0.15305481272406798, "3": 0.07511721014301591, "4": 0.029041742658833424, "5": 0.009222900897342987, "6": 0.0024795735807105466, "7": 0.0005772175142608826, "8": 0.00011838581843774291, "9": 2.1688458090538602e-05} |
| Raw goal margin distribution | {"-1": 0.15002527884375524, "-10": 1.4710652136030469e-08, "-11": 1.2346394466604012e-09, "-12": 9.511726995658301e-11, "-13": 6.747606040423701e-12, "-14": 4.106223415457794e-13, "-2": 0.06303160977488954, "-3": 0.017751471943399, "-4": 0.003891211480257444, "-5": 0.0006958791840048065, "-6": 0.00010491117023367747, "-7": 1.3657308373677784e-05, "-8": 1.5634397781005985e-06, "-9": 1.5965217782536758e-07, "0": 0.2940931276161528, "1": 0.23437535085432276, "10": 9.688830928629913e-07, "11": 1.2360713643084367e-07, "12": 1.4475271519063052e-08, "13": 1.560921294821895e-09, "14": 1.4439022978379747e-10, "2": 0.14564188428810737, "3": 0.062348528185093406, "4": 0.02077498004135238, "5": 0.005647465302977517, "6": 0.0012942119406917836, "7": 0.0002561018594965689, "8": 4.456487766845828e-05, "9": 6.917518888297832e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.9% |
| Raw p btts yes | 47.2% |
| P home draw | 75.8% |
| P draw away | 51.0% |
| P home away | 73.2% |
| Raw p home draw | 76.4% |
| Raw p draw away | 53.0% |
| Raw p home away | 70.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1870 |
| Totals anchor target over 2 5 | 0.5262 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.02 |
| Totals anchor reference last update utc | 2026-11-06T11:25:08Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4265 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.57, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.77, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.77, "draw": 3.71, "home": 2.01}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.86, "under": 2.03}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.85, "home_away": 1.3, "home_draw": 1.3}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.82, "draw": 3.65, "home": 1.94}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.02}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.02}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.25, "under": 3.89}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.94 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.82 |
| Market reference 1x2 last update utc | 2026-11-06T11:25:08Z |
| Market reference home last update utc | 2026-11-06T11:25:08Z |
| Market reference draw last update utc | 2026-11-06T11:25:08Z |
| Market reference away last update utc | 2026-11-06T11:25:08Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference under 2 5 last update utc | 2026-11-06T11:25:08Z |
| Market best over 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market best under 2 5 last update utc | 2026-11-06T11:23:33Z |
| Home probability edge | -0.8% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0282 |
| Raw ev home | -0.0545 |
| Raw edge prob draw | 0.0374 |
| Raw ev draw | 0.0911 |
| Raw edge prob away | -0.0092 |
| Raw ev away | -0.1003 |
| Market p home draw | 75.3% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T11:23:33Z |
| Market reference home draw last update utc | 2026-11-06T11:25:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.7% |
| Market draw away odds | 1.85 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T11:23:33Z |
| Market reference draw away last update utc | 2026-11-06T11:25:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.0% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T11:23:33Z |
| Market reference home away last update utc | 2026-11-06T11:25:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.82 |
| Market reference dc home draw odds | 1.25 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 78.0% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.89 |
| Market reference over 1 5 last update utc | 2026-11-06T11:25:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.2% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.02 |
| Market reference under 3 5 last update utc | 2026-11-06T11:25:08Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,458.4916 |
| Elo away rating | 1,419.5564 |
| Elo rating diff | 98.9351 |
| Elo home expectancy | 0.6387 |
| Research p home | 0.4826 |
| Research p draw | 0.2698 |
| Research p away | 0.2477 |
| Research p over 1 5 | 0.6804 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4172828457642097, 0.9323792192567341], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T11:26:29.185741+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T11:26:28.849834+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T11:26:29.186778+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87aykur+Rizespor%22+%22Erzurum+BB%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T11:25:35.001023+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T11:25:35.083842+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T11:26:29.244585+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87aykur+Rizespor_vs_Erzurum+BB&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.4172828457642097, 0.9323792192567341], "h2h": [], "margin_distribution": {"-1": 0.16218945371044738, "-10": 1.4710652136030469e-08, "-11": 1.2346394466604012e-09, "-12": 9.511726995658301e-11, "-13": 6.747606040423701e-12, "-14": 4.106223415457794e-13, "-2": 0.06303160977488954, "-3": 0.017751471943399, "-4": 0.003891211480257444, "-5": 0.0006958791840048065, "-6": 0.00010491117023367747, "-7": 1.3657308373677784e-05, "-8": 1.5634397781005985e-06, "-9": 1.5965217782536758e-07, "0": 0.2697647778827685, "1": 0.24653952572101495, "10": 9.688830928629913e-07, "11": 1.2360713643084367e-07, "12": 1.4475271519063052e-08, "13": 1.560921294821895e-09, "14": 1.4439022978379747e-10, "2": 0.14564188428810737, "3": 0.062348528185093406, "4": 0.02077498004135238, "5": 0.005647465302977517, "6": 0.0012942119406917836, "7": 0.0002561018594965689, "8": 4.456487766845828e-05, "9": 6.917518888297832e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T11:26:29.244907+00:00", "p_over_1_5": 0.680437562060763, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Çorum FK vs Fenerbahce

The model's most likely 1X2 outcome is **Fenerbahce win** at **53.1%**. Expected goals are 1.87 for Çorum FK and 2.27 for Fenerbahce (4.14 combined). The most likely exact score is 1-2 at 8.7%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 77.8%; Under 3.5 goals: 40.5%; Double Chance 1X: 46.9%; Double Chance X2: 75.9%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 60.4%; BTTS Yes (both teams score): 76.6%; BTTS No (at least one team does not score): 23.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çorum FK win | 24.1% | 4.15 |
| Draw | 22.8% | 4.39 |
| Fenerbahce win | 53.1% | 1.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çorum FK expected goals | 1.87 |
| Fenerbahce expected goals | 2.27 |
| Expected total goals | 4.14 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 92.5% |
| Under 1.5 | 7.5% |
| Over 2.5 | 77.8% |
| Under 2.5 | 22.2% |
| Over 3.5 | 59.5% |
| Under 3.5 | 40.5% |
| Over 4.5 | 39.6% |
| Under 4.5 | 60.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.70% |
| 2 | 1-1 | 7.94% |
| 3 | 2-2 | 7.69% |
| 4 | 1-3 | 6.57% |
| 5 | 2-3 | 6.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çorum FK win | 24.1% | 20.7% | 4.54 | +9.3% |
| Draw | 22.8% | 23.5% | 4.11 | -6.3% |
| Fenerbahce win | 53.1% | 55.8% | 1.76 | -6.5% |
| Over 2.5 | 77.8% | 58.8% | 1.66 | +29.1% |
| Under 2.5 | 22.2% | 41.2% | 2.33 | -48.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T13:00:00+00:00 |
| Fixture id | 6692a3ca274d09ffbfabd943320d62f5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T11:23:33Z |
| Market best draw last update utc | 2026-11-06T11:23:33Z |
| Market best away last update utc | 2026-11-06T11:23:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Corum |
| Matched away-team name | Fenerbahce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8740 |
| Dc lambda away | 2.2663 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 76.6% |
| P btts no | 23.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.61 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.30 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.50 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.47 |
| Fair Over 4.5 odds | 2.52 |
| Fair Under 4.5 odds | 1.66 |
| Score matrix json | [[0.02403293788295466,0.033567990926422986,0.04643434968081999,0.035078382976090824,0.019874720341871634,0.009008499825931849,0.003402692286057925,0.0011016562152242166,0.000312088348048848,7.858804721421553e-05,1.7810575380979516e-05,3.669498521909556e-06,6.930218435626735e-07,1.2081615875908047e-07,1.9557729733865e-08,2.95493977395261e-09,4.185526573047179e-10,5.579851418128322e-11],[0.017565221079013028,0.07938713352813824,0.08701931146600644,0.06573790211131479,0.03724579953455183,0.0168821886724523,0.006376743550814885,0.002064535542761262,0.0005848625715757964,0.00014727626864695386,3.337753230355726e-05,6.876746137224227e-06,1.2987429364739478e-06,2.2641296844791409e-07,3.665174998632865e-08,5.537642420328436e-09,7.843797598390469e-10,1.0456802600354018e-10],[0.021065341008338984,0.04774082793180729,0.07687470986796935,0.061597362924942826,0.0348998516483624,0.01581885440858047,0.0059751007282483086,0.0019344995963450561,0.0005480246695668265,0.0001379999890278877,3.127522943095787e-05,6.4436103671217005e-06,1.216940873299063e-06,2.121522187426078e-07,3.43432186491021e-08,5.188850860131399e-09,7.349751541503662e-10,9.798174935941987e-11],[0.013159019008862875,0.0298225631384184,0.033793752845327325,0.03627761335357381,0.021801109750157664,0.00988166323908745,0.003732503738333247,0.0012084360253586696,0.0003423380158574654,8.620532077415587e-05,1.953689420102928e-05,4.025170600043669e-06,7.601941064265377e-07,1.325264603170333e-07,2.1453394314868626e-08,3.2413520899373983e-09,4.591215504500014e-10,6.120687539935104e-11],[0.0061650953528499825,0.013972086011191695,0.01583261704248363,0.011960598305943922,0.009629781933506963,0.004629630527374017,0.0017487049328065369,0.0005661609971942001,0.00016038783052484736,4.038781478602154e-05,9.153175899112537e-06,1.8858214692177134e-06,3.561564239429721e-07,6.208960288604397e-08,1.005107003070468e-08,1.5185968416919606e-09,2.1510175911792233e-10,2.8675862754879867e-11],[0.002310713325005946,0.005236818488016568,0.005934156258081379,0.004482901285186444,0.0025399235028600088,0.0016359656154107916,0.0006554247028590955,0.00021220040979747767,6.011428468681111e-05,1.5137586112239164e-05,3.4306631618317602e-06,7.068167721832955e-07,1.3348948353427322e-07,2.327154156128111e-08,3.767199065263567e-09,5.691788620572442e-10,8.062138094850921e-11,1.0747878886108604e-11],[0.0007217239102787153,0.0016356581648143051,0.0018534633493648034,0.0014001810652690607,0.0007933149917193732,0.00035958130941630626,0.00019300537250008687,6.627828206313188e-05,1.877598408173873e-05,4.7280455445843396e-06,1.0715269632159965e-06,2.207658384751796e-07,4.1693857474593454e-08,7.268590089503302e-09,1.1766399625420203e-09,1.7777626914013087e-10,2.5181132458340872e-11,3.356972538713509e-12],[0.00019321877684057032,0.0004378958011972526,0.0004962062586298321,0.00037485424680212825,0.00021238502724692815,9.626653598509485e-05,3.63618144787072e-05,1.672904100517988e-05,5.02667658170084e-06,1.2657848298503795e-06,2.868674935604271e-07,5.9103078990252926e-08,1.116221317912959e-08,1.945935372858795e-09,3.150081784824145e-10,4.759397989360079e-11,6.74145271310474e-12,8.98723346393111e-13],[4.5262195547436006e-05,0.0001025786712206821,0.00011623810624004143,8.781095966953796e-05,4.975195885092433e-05,2.255078335387101e-05,8.517886223619143e-06,2.757752247322377e-06,1.1101682411303673e-06,2.965146629457194e-07,6.719974529415704e-08,1.3845109478773412e-08,2.6147887069630184e-09,4.558423814145269e-10,7.379180225986668e-11,1.1149061494175528e-11,1.579209619084343e-12,2.1052918620355236e-13],[9.424740087771056e-06,2.1359487826670735e-05,2.4203729544206064e-05,1.8284474752794507e-05,1.0359622977988847e-05,4.695646539353699e-06,1.7736405135425152e-06,5.742341449221249e-07,1.6267487370868632e-07,5.8210523877553206e-08,1.3992695796165888e-08,2.8829038615111224e-09,5.444655003917814e-10,9.491797545083699e-11,1.536532968619629e-11,2.3215181131692393e-12,3.2883160049934854e-13,4.383753012553179e-14],[1.7662234936449801e-06,4.002829665365541e-06,4.535848772134789e-06,3.4265633403776733e-06,1.9414232454823697e-06,8.799777138067127e-07,3.323853512272513e-07,1.0761313608325266e-07,3.0485740836802525e-08,7.676719926333111e-09,2.472288993050043e-09,5.402645041349887e-10,1.0203440618154631e-10,1.77879025468313e-11,2.8795071298118737e-12,4.3505919465325e-13,6.162399099031135e-14,8.21527966713353e-15],[3.0090489117439546e-07,6.81947120044687e-07,7.727555918453192e-07,5.83770781414918e-07,3.3075301767146457e-07,1.4991851210316097e-07,5.6627249212156076e-08,1.8333647535873714e-08,5.193741653802714e-09,1.3078540639511457e-09,2.9640173307562195e-10,8.67783908226646e-11,1.7383220186218202e-11,3.0304584325447183e-12,4.905708607373445e-13,7.41194079303025e-14,1.049864887959575e-14,1.3996064728504433e-15],[4.6992037551827715e-08,1.06499048747359e-07,1.2068052349914763e-07,9.116694107179047e-08,5.16533917615506e-08,2.3412634879314142e-08,8.8434249474931e-09,2.8631487182055513e-09,8.111018131923168e-10,2.0424635520425316e-10,4.628878353141786e-11,9.536840844059682e-12,2.5594510495688113e-12,4.732638805092049e-13,7.661199596865628e-14,1.1575159138112368e-14,1.6395642505773854e-15,2.1857524373656874e-16],[6.774187279382586e-09,1.53524839286873e-08,1.739682954278199e-08,1.3142267598582233e-08,7.446149765737322e-09,3.3750733451673927e-09,1.2748333527655759e-09,4.1274025635635e-10,1.1692524673252516e-10,2.944335111579121e-11,6.67280894621325e-12,1.3747934607022084e-12,2.596436251343544e-13,6.432174986344079e-14,1.1044083967769893e-14,1.6686294077746393e-15,2.363531327566319e-16,3.150894732060033e-17],[9.067873196176756e-10,2.0550712841285117e-09,2.328725761532631e-09,1.759213484647382e-09,9.967356834221045e-10,4.517846327473161e-10,1.7064817833304305e-10,5.524908233623539e-11,1.5651520500904326e-11,3.94126355498158e-12,8.932168965970845e-13,1.8402875885233655e-13,3.475568908582883e-14,6.059042567530548e-15,1.3937969407949149e-15,2.233614049490969e-16,3.163804230625887e-17,4.217762619551585e-18],[1.1328970721263161e-10,2.5675085992398755e-10,2.9093995250592807e-10,2.1978778958250713e-10,1.2452742920013743e-10,5.644382939616932e-11,2.1319974090363923e-11,6.9025583245668904e-12,1.955426742984849e-12,4.924027768495223e-13,1.1159428291909107e-13,2.299168036213329e-14,4.342210963169331e-15,7.569880429667043e-16,1.2254128676307926e-16,2.6309628536299545e-17,3.952706960181286e-18,5.269472586613209e-19],[1.3269261314082643e-11,3.007240760674291e-11,3.40768667471453e-11,2.5743041317435075e-11,1.4585499772951228e-11,6.611085333811877e-12,2.4971404232119633e-12,8.084745948938442e-13,2.290328845542151e-13,5.767356345561927e-14,1.3070681685423095e-14,2.6929420357879852e-15,5.085892917264425e-16,8.866359001977592e-17,1.4352869257322392e-17,2.1685474140368014e-18,4.364881708983372e-19,6.171964820063502e-20],[1.4627634513610684e-12,3.315091752311099e-12,3.756531281942846e-12,2.8378354359528432e-12,1.6078616196265028e-12,7.287861600755399e-13,2.752772484866312e-13,8.912380732976917e-14,2.524789622841685e-14,6.357760144726304e-15,1.4408726304545754e-15,2.9686182925676027e-16,5.606535360800408e-17,9.77400745056896e-18,1.5822171313706275e-18,2.3905414361160237e-19,3.386084140540743e-20,6.41464111091958e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.20934244632189886, "-10": 2.6047435180568407e-05, "-11": 5.203449646636158e-06, "-12": 9.572452323876314e-07, "-13": 1.631445570187454e-07, "-14": 2.5891554183743153e-08, "-15": 3.837301283151077e-09, "-16": 5.231206833082581e-10, "-17": 5.579851418128322e-11, "-2": 0.15893478397889255, "-3": 0.09250684526034078, "-4": 0.04411710452727219, "-5": 0.01770613186660225, "-6": 0.0061113615278006565, "-7": 0.001846082576066058, "-8": 0.0004950456705492973, "-9": 0.00011923542552152336, "0": 0.22804904753551666, "1": 0.11399919519889196, "10": 2.5830491705644458e-06, "11": 4.2669139674096626e-07, "12": 6.490834931756318e-08, "13": 9.147549418954088e-09, "14": 1.2004528817247613e-09, "15": 1.4711864610131736e-10, "16": 1.6584353066393744e-11, "17": 1.4627634513610684e-12, "2": 0.07210212796379449, "3": 0.03470226481250471, "4": 0.013685030602884413, "5": 0.004541687920190201, "6": 0.0012962429065488839, "7": 0.0003237832386953632, "8": 7.179650917889047e-05, "9": 1.4299412374148771e-05} |
| Raw goal margin distribution | {"-1": 0.1842891096831959, "-10": 2.2930173614081633e-05, "-11": 4.580719865981644e-06, "-12": 8.426856317229662e-07, "-13": 1.4362001443516552e-07, "-14": 2.279294788358032e-08, "-15": 3.378067131071456e-09, "-16": 4.605155174097113e-10, "-17": 4.9120752531485905e-11, "-2": 0.13991405160195275, "-3": 0.0814359651000506, "-4": 0.038837331167085855, "-5": 0.015587126905987875, "-6": 0.0053799761811262605, "-7": 0.0016251501801108248, "-8": 0.0004358004192698075, "-9": 0.00010496576684821097, "0": 0.21293599042596234, "1": 0.1512602038291479, "10": 3.4273272136581464e-06, "11": 5.661568709373633e-07, "12": 8.612385491721059e-08, "13": 1.2137455770930282e-08, "14": 1.5928248200364512e-09, "15": 1.9520485524067838e-10, "16": 2.2005002937263315e-11, "17": 1.9408724545877644e-12, "2": 0.095668943568339, "3": 0.046044813208677364, "4": 0.01815802747369346, "5": 0.006026153424485104, "6": 0.0017199241267852135, "7": 0.0004296128459159361, "8": 9.526343228715896e-05, "9": 1.8973221930007157e-05} |
| Research history json | {"away": [{"away": "Goztep", "away_goals": 2.0, "away_xg": 1.4, "date": "2026-10-31T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 1.51, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 3.0, "away_xg": 0.96, "date": "2026-10-10T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.52, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 0.0, "away_xg": 1.33, "date": "2026-09-14T00:00:00+00:00", "home": "Gaziantep", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 2.0, "away_xg": 1.75, "date": "2026-09-05T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Konyaspor", "away_goals": 2.0, "away_xg": 2.15, "date": "2026-08-22T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 4.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 2.9, "date": "2026-08-15T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 2.0, "home_xg": 1.19, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 46.8% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.7% |
| Raw p btts yes | 76.5% |
| P home draw | 46.9% |
| P draw away | 75.9% |
| P home away | 77.2% |
| Raw p home draw | 53.2% |
| Raw p draw away | 68.1% |
| Raw p home away | 78.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7779 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 2.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.94, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.76, "draw": 4.11, "home": 4.54}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T11:23:33Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.66, "under": 2.33}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T11:25:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.74, "draw": 3.97, "home": 4.47}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.47 |
| Reference draw odds | 3.97 |
| Reference away odds | 1.74 |
| Market reference 1x2 last update utc | 2026-11-06T11:25:08Z |
| Market reference home last update utc | 2026-11-06T11:25:08Z |
| Market reference draw last update utc | 2026-11-06T11:25:08Z |
| Market reference away last update utc | 2026-11-06T11:25:08Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market reference under 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market best over 2 5 last update utc | 2026-11-06T11:23:33Z |
| Market best under 2 5 last update utc | 2026-11-06T11:23:33Z |
| Home probability edge | +3.4% |
| Draw probability edge | -0.6% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | +19.0% |
| Under 2.5 probability edge | -19.0% |
| Raw edge prob home | 0.1124 |
| Raw ev home | 0.4502 |
| Raw edge prob draw | -0.0216 |
| Raw ev draw | -0.1248 |
| Raw edge prob away | -0.0908 |
| Raw ev away | -0.1770 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,445.1258 |
| Elo away rating | 1,661.7220 |
| Elo rating diff | -156.5962 |
| Elo home expectancy | 0.2888 |
| Research p home | 0.3259 |
| Research p draw | 0.1999 |
| Research p away | 0.4742 |
| Research p over 1 5 | 0.9182 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.874028861482049, 2.2663211534486187], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T11:26:29.185741+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T11:26:28.849834+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T11:26:29.250238+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87orum+FK%22+%22Fenerbahce%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T11:25:35.001023+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T11:25:35.083842+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T11:26:29.308387+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87orum+FK_vs_Fenerbahce&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 1.0089728918892988, "goals_for": 2.3331960885564245, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.4847509690034097, "results": "LLWWWDLWWL", "xg_against": 1.3380003484001706, "xg_for": 1.9676008712062978, "xg_matches": 10}, "venue": {"goals_against": 0.8151944568095735, "goals_for": 1.425370020202056, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.384791003310632, "results": "LWDWL", "xg_against": 1.2819506533747527, "xg_for": 1.2552734770676013, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.874028861482049, 2.2663211534486187], "h2h": [], "margin_distribution": {"-1": 0.1908120795263315, "-10": 2.2930173614081633e-05, "-11": 4.580719865981644e-06, "-12": 8.426856317229662e-07, "-13": 1.4362001443516552e-07, "-14": 2.279294788358032e-08, "-15": 3.378067131071456e-09, "-16": 4.605155174097113e-10, "-17": 4.9120752531485905e-11, "-2": 0.13991405160195275, "-3": 0.0814359651000506, "-4": 0.038837331167085855, "-5": 0.015587126905987875, "-6": 0.0053799761811262605, "-7": 0.0016251501801108248, "-8": 0.0004358004192698075, "-9": 0.00010496576684821097, "0": 0.19989005073969113, "1": 0.1577831736722835, "10": 3.4273272136581464e-06, "11": 5.661568709373633e-07, "12": 8.612385491721059e-08, "13": 1.2137455770930282e-08, "14": 1.5928248200364512e-09, "15": 1.9520485524067838e-10, "16": 2.2005002937263315e-11, "17": 1.9408724545877644e-12, "2": 0.095668943568339, "3": 0.046044813208677364, "4": 0.01815802747369346, "5": 0.006026153424485104, "6": 0.0017199241267852135, "7": 0.0004296128459159361, "8": 9.526343228715896e-05, "9": 1.8973221930007157e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T11:26:29.308710+00:00", "p_over_1_5": 0.9181796133965817, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
