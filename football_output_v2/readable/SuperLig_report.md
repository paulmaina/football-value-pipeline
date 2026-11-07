# Super Lig — football model report

Fixtures in this report: **7**.

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
| Training as of utc | 2026-11-07T11:47:21.951126+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-07', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1809, 'tune_start_date': '2025-11-08', 'audit_start_date': '2026-05-09', 'training_shot_matches': 1513, 'tuning_matches': 188, 'audit_matches': 94, 'audit_matchdays': 38, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8406061330011584, 'audit_candidate_poisson_score': 0.832662940340293, 'audit_gain': 0.007943192660865406, 'audit_gain_lower95': 0.0007010941958230725, 'audit_baseline_briers': [0.604125448119081, 0.17290702296888374, 0.21645984578617375, 0.24465189323875286], 'audit_candidate_briers': [0.60048662707422, 0.17155931610656247, 0.21342015723215774, 0.2454632457185039], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'market_brier_worse']} |
| Optimizer objective | 1667.428 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1840, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 59.00 |
| Over 1 5 in window quote fixtures | 7 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 2, 'ANCHORED_ALTERNATE': 5} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 7} |
| Legacy comparison status | {'None': 7} |
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

## 2026-11-07 — Galatasaray vs Amed SK

The model's most likely 1X2 outcome is **Galatasaray win** at **64.3%**. Expected goals are 2.21 for Galatasaray and 1.53 for Amed SK (3.74 combined). The most likely exact score is 2-1 at 11.8%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 67.7%; Under 3.5 goals: 55.1%; Double Chance 1X: 83.0%; Double Chance X2: 35.7%; Double Chance 12 (either team wins): 81.3%; Under 4.5 goals: 73.4%; BTTS Yes (both teams score): 64.2%; BTTS No (at least one team does not score): 35.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 64.3% | 1.56 |
| Draw | 18.7% | 5.34 |
| Amed SK win | 17.0% | 5.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 2.21 |
| Amed SK expected goals | 1.53 |
| Expected total goals | 3.74 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 86.6% |
| Under 1.5 | 13.4% |
| Over 2.5 | 67.7% |
| Under 2.5 | 32.3% |
| Over 3.5 | 44.9% |
| Under 3.5 | 55.1% |
| Over 4.5 | 26.6% |
| Under 4.5 | 73.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.83% |
| 2 | 2-0 | 8.56% |
| 3 | 1-1 | 8.21% |
| 4 | 3-1 | 7.90% |
| 5 | 1-0 | 7.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 64.3% | 69.3% | 1.45 | -6.8% |
| Draw | 18.7% | 17.4% | 5.35 | +0.1% |
| Amed SK win | 17.0% | 13.3% | 6.91 | +17.4% |

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
| Market best home last update utc | 2026-11-07T11:46:39Z |
| Market best draw last update utc | 2026-11-07T11:47:01Z |
| Market best away last update utc | 2026-11-07T11:47:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Galatasaray |
| Matched away-team name | Amedspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2148 |
| Dc lambda away | 1.5271 |
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
| P btts yes | 64.2% |
| P btts no | 35.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.17 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.49 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.10 |
| Fair Over 3.5 odds | 2.23 |
| Fair Under 3.5 odds | 1.81 |
| Fair Over 4.5 odds | 3.76 |
| Fair Under 4.5 odds | 1.36 |
| Score matrix json | [[0.03427923964083502,0.02514613856240127,0.021529359578516042,0.00991320018271972,0.0034234020351703327,0.0009457839065804513,0.00021774324408800974,4.296854705794185e-05,7.4193302230941845e-06,1.1387442878488198e-06,1.5730054637071626e-07,1.9753386692976794e-08,2.273863231509661e-09,2.416156196079935e-10,2.383971122627238e-11,2.195400460681593e-12,1.895386521653315e-13,1.5401140620737354e-14],[0.07410224432460723,0.08209774769920536,0.043132571064533616,0.019860405498767646,0.006858547325848101,0.0018948121245084134,0.0004362334102506323,8.608448861460185e-05,1.4864110886892888e-05,2.281394796758577e-06,3.151406789450139e-07,3.9574533194673e-08,4.555526469165912e-09,4.840600504179709e-10,4.7761199531975535e-11,4.398331777595103e-12,3.7972747652722234e-13,3.0855111591973186e-14],[0.08564359365448335,0.1183038564386666,0.05180215136962358,0.019894468955799164,0.006870310722730764,0.0018980620003173439,0.00043698161340422387,8.623213591612273e-05,1.4889604978770255e-05,2.285307717551465e-06,3.156811906166811e-07,3.9642409221227575e-08,4.563339853446912e-09,4.848902831505861e-10,4.784311687088042e-11,4.405875550330547e-12,3.8037876386277923e-13,3.0908032554134856e-14],[0.05719365650508061,0.07900450973223803,0.05456647589472469,0.015928817702128464,0.004588062863689345,0.0012675449667543643,0.00029182073322268605,5.758669096935971e-05,9.943428531125684e-06,1.5261515663782057e-06,2.1081508622916335e-07,2.6473601109965104e-08,3.0474444258718336e-09,3.238146265679749e-10,3.195011647321643e-11,2.942288174482121e-12,2.540207788333051e-13,2.064069618891453e-14],[0.02864587593338844,0.039570006924925835,0.027330032631567473,0.012584121858754562,0.0027551282139266337,0.0006348594945037483,0.00014616062391368395,2.8842730220896434e-05,4.980241471881388e-06,7.643845681056073e-07,1.0558833223874653e-07,1.3259503575168488e-08,1.5263356160777375e-09,1.6218500765480375e-10,1.600245776326201e-11,1.4736673113215564e-12,1.2722823053488746e-13,1.0338048978454201e-14],[0.011478003095230522,0.015855150075310256,0.010950763030159388,0.005042282176373912,0.001741290274213521,0.0003049861097639763,5.8564524177342763e-05,1.1556879863620509e-05,1.995513321434968e-06,3.0627823911072847e-07,4.23077725769234e-08,5.312898213722091e-09,6.115814006330004e-10,6.498527132459113e-11,6.411961713620761e-12,5.904779452379646e-13,5.097857811281119e-14,4.142312088807057e-15],[0.003832563174785117,0.005294114647396788,0.003656515055534949,0.0016836434722757754,0.0005814256126429619,0.0001606305603788169,2.344530109110706e-05,3.858900525922715e-06,6.663119714354108e-07,1.0226785014037615e-07,1.4126778834279774e-08,1.7740035332238224e-09,2.0421011695174714e-10,2.1698910142787792e-11,2.140986383943945e-12,1.9716356666449873e-13,1.702200457318685e-14,1.3831389169624803e-15],[0.0010968961636707304,0.0015151985190924211,0.0010465104302019577,0.00048186604669135305,0.0001664065260982233,4.59731614098397e-05,1.0584178094712255e-05,1.3241524525801785e-06,1.907013692778493e-07,2.9269501211058654e-08,4.043145227270822e-09,5.077274871119728e-10,5.844581906459549e-11,6.210321971481741e-12,6.127595668794305e-13,5.642906588279595e-14,4.8717713610451165e-15,3.958603427130453e-16],[0.000274694374659629,0.00037944932571778924,0.00026207633659424464,0.00012067312909786306,4.16729843168221e-05,1.1513003001433583e-05,2.650582871293442e-06,5.230550105614892e-07,5.725801264516188e-08,7.3299256557383045e-09,1.012519950973786e-09,1.271495782271645e-10,1.4636515516375018e-11,1.5552433921204096e-12,1.5345263445663531e-13,1.4131462465352095e-14,1.2200317877205167e-15,9.913482505965667e-17],[6.114789224260263e-05,8.44666968854736e-05,5.8339074505103555e-05,2.686224464478727e-05,9.276546553201806e-06,2.562833213431238e-06,5.900286672953108e-07,1.1643380561541538e-07,2.0104492987101317e-08,1.9562732033681807e-09,2.2539034857319778e-10,2.8303924016503296e-11,3.2581376109774965e-12,3.462024130280638e-13,3.4159072852236545e-14,3.1457111021383035e-15,2.7158318178347496e-16,2.206774568189964e-17],[1.2250553937667504e-05,1.6922313888215616e-05,1.1687826884741615e-05,5.381663452963856e-06,1.85849143343171e-06,5.134457683319946e-07,1.1820813029488697e-07,2.332670127369919e-08,4.027795017868958e-09,6.181998147147287e-10,5.413869224986451e-11,5.670493864876644e-12,6.527451572862935e-13,6.935924000984705e-14,6.843532116802631e-15,6.302212899861119e-16,5.440979721429905e-17,4.421119009078279e-18],[2.231193709600127e-06,3.08206147178145e-06,2.128704216708746e-06,9.801625056739333e-07,3.3848709345857347e-07,9.351389123725382e-08,2.152924986735424e-08,4.248492714077916e-09,7.335824121222577e-10,1.1259274844922551e-10,1.5553009606661666e-11,1.2382280712658573e-12,1.18884492596783e-13,1.2632400200025665e-14,1.2464126837160579e-15,1.1478222005533404e-16,9.909657792035876e-18,8.0521852094528e-19],[3.7250342138254645e-07,5.145579418811085e-07,3.553925418593858e-07,1.6364060426643334e-07,5.651127459916946e-08,1.5612380172457255e-08,3.5943626054890928e-09,7.092965818716262e-10,1.224734352763015e-10,1.8797643539304158e-11,2.596614209850654e-12,3.26075946734328e-13,2.3796682062631723e-14,2.109011097752898e-15,2.080917435098199e-16,1.9163181350201593e-17,1.6544423804982586e-18,1.3443326445486738e-19],[5.740651052656109e-08,7.929853582952219e-08,5.476955250394931e-08,2.5218657150927254e-08,8.708953781165479e-09,2.4060242544575858e-09,5.539273008082904e-10,1.093097119552394e-10,1.887438382530391e-11,2.89690526253021e-12,4.0016427343932564e-13,5.0251571379364625e-14,5.7845878411192524e-15,3.896798581305324e-16,3.2069023205075576e-17,2.953238302670504e-18,2.549661519326709e-19,2.071751336512666e-20],[8.214995851939031e-09,1.134779203489391e-08,7.837641454000662e-09,3.6088443973699655e-09,1.2462701273908794e-09,3.443072761039636e-10,7.926819513459957e-11,1.5642456265887495e-11,2.7009651590133873e-12,4.145534103511662e-13,5.726437326089088e-14,7.191108580687809e-15,8.277870346776206e-16,8.795879827579118e-17,5.50212106318775e-18,4.226147902684407e-19,3.648620794574572e-20,2.9647209836637036e-21],[1.0972114337985055e-09,1.5156340177718223e-09,1.0468112184515432e-09,4.820045447325919e-10,1.66454354697213e-10,4.598637502563301e-11,1.0587220201422838e-11,2.0892380442984324e-12,3.6074636045755134e-13,5.5368590557486635e-14,7.648345321601656e-15,9.604589824053103e-16,1.1056090782858574e-16,1.1747954705125593e-17,1.1591462841844205e-18,6.767462823326018e-20,4.87317160660195e-21,3.9597412097662373e-22],[1.3738666368749824e-10,1.897791935616928e-10,1.3107583131521894e-10,6.035390649709844e-11,2.08424809874021e-11,5.758156035597828e-12,1.3256723511919603e-12,2.6160267357172545e-13,4.5170636555517576e-14,6.9329444585145996e-15,9.576829169807075e-16,1.2026328849357175e-16,1.384381696447018e-17,1.4710130175196964e-18,1.4514179838478012e-19,1.336611706466232e-20,7.315839485827655e-22,4.958165920604011e-23],[1.619085901308016e-11,2.2365257908603133e-11,1.5447134735539136e-11,7.112637899162144e-12,2.4562622171058575e-12,6.78592012102006e-13,1.562289494452631e-13,3.082957174707244e-14,5.32330714184175e-15,8.170394655528687e-16,1.1286182131432719e-16,1.4172889101360365e-17,1.6314777770895124e-18,1.733571784466755e-19,1.7104792644926288e-20,1.575181397799421e-21,1.3599239154851674e-22,7.00558779856418e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.09345872262810721, "-10": 2.0177884439897757e-07, "-11": 2.482727959079486e-08, "-12": 2.8088400575156175e-09, "-13": 2.9404705351811136e-10, "-14": 2.8639062463919176e-11, "-15": 2.60603596976295e-12, "-16": 2.2039376375730467e-13, "-17": 1.5401140620737354e-14, "-2": 0.04968603489350823, "-3": 0.018992574927123886, "-4": 0.00581808363325932, "-5": 0.0014790014076584098, "-6": 0.000320354601055305, "-7": 6.034267415966834e-05, "-8": 1.004447333112436e-05, "-9": 1.4967436195447743e-06, "0": 0.18719289945871367, "1": 0.26146974732302847, "10": 1.571452022146361e-05, "11": 2.804302417122237e-06, "12": 4.601431242838014e-07, "13": 6.986392394862074e-08, "14": 9.868818338925234e-09, "15": 1.3024377620957374e-09, "16": 1.5975192159610136e-10, "17": 1.619085901308016e-11, "2": 0.19765058812842795, "3": 0.10957660356969737, "4": 0.048683765510506835, "5": 0.01794911355209182, "6": 0.005638655986870862, "7": 0.0015404208967577675, "8": 0.00037188805963779255, "9": 8.037161506699688e-05} |
| Raw goal margin distribution | {"-1": 0.1357866898084883, "-10": 6.104237018454033e-07, "-11": 8.266770134603677e-08, "-12": 1.0300621758984217e-08, "-13": 1.188241218876436e-09, "-14": 1.275748879409287e-10, "-15": 1.2795865083792481e-11, "-16": 1.1881010276575295e-12, "-17": 8.90148871717475e-14, "-2": 0.07542173321009207, "-3": 0.030850620605931255, "-4": 0.010214255972087825, "-5": 0.002823751404207546, "-6": 0.0006678356236786268, "-7": 0.00013773235560533275, "-8": 2.5150979950996707e-05, "-9": 4.117255279975263e-06, "0": 0.21884790127616965, "1": 0.20042136521270623, "10": 2.513816336238601e-05, "11": 4.9375127867841104e-06, "12": 8.922900027942272e-07, "13": 1.4928542753514344e-07, "14": 2.3245998948251735e-08, "15": 3.381605072160555e-09, "16": 4.5538300750697865e-10, "17": 4.948303293849024e-11, "2": 0.15864885408822588, "3": 0.0941184034870726, "4": 0.0451947095374506, "5": 0.018120807126154066, "6": 0.006215711877548783, "7": 0.0018592058804462685, "8": 0.0004923984030555384, "9": 0.00011690678988481181} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Galatasaray", "away_goals": 4.0, "away_xg": 2.8, "date": "2026-10-30T00:00:00+00:00", "home": "Konyaspor", "home_goals": 0.0, "home_xg": 1.38, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 1.0, "away_xg": 1.92, "date": "2026-10-17T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 0.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.51, "date": "2026-10-09T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 3.0, "away_xg": 2.12, "date": "2026-09-04T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.63, "date": "2026-08-29T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.92, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 4.0, "away_xg": 3.08, "date": "2026-08-21T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 0.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 2.0, "away_xg": 0.61, "date": "2026-08-14T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 52.5% |
| Unadjusted draw probability | 21.9% |
| Unadjusted away-win probability | 25.6% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.5% |
| Raw p btts yes | 70.5% |
| P home draw | 83.0% |
| P draw away | 35.7% |
| P home away | 81.3% |
| Raw p home draw | 74.4% |
| Raw p draw away | 47.5% |
| Raw p home away | 78.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9046 |
| Totals anchor target over 2 5 | 0.6772 |
| Totals anchor reference over odds | 1.44 |
| Totals anchor reference under odds | 2.88 |
| Totals anchor reference last update utc | 2026-11-07T11:47:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7346 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.86, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.86, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.73, "draw": 5.15, "home": 1.45}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.87, "home_away": 1.19, "home_draw": 1.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.91, "draw": 5.35, "home": 1.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.44, "under": 2.88}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.14, "under": 6.13}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.42 |
| Reference draw odds | 5.35 |
| Reference away odds | 6.91 |
| Market reference 1x2 last update utc | 2026-11-07T11:47:01Z |
| Market reference home last update utc | 2026-11-07T11:47:01Z |
| Market reference draw last update utc | 2026-11-07T11:47:01Z |
| Market reference away last update utc | 2026-11-07T11:47:01Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-11-07T11:46:44Z |
| Market reference under 2 5 last update utc | 2026-11-07T11:46:44Z |
| Home probability edge | -5.0% |
| Draw probability edge | +1.4% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -0.6% |
| Under 2.5 probability edge | +0.6% |
| Raw edge prob home | -0.1682 |
| Raw ev home | -0.2384 |
| Raw edge prob draw | 0.0452 |
| Raw ev draw | 0.1708 |
| Raw edge prob away | 0.1230 |
| Raw ev away | 0.7685 |
| Market p home draw | 85.9% |
| Market home draw odds | 1.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T11:46:39Z |
| Market reference home draw last update utc | 2026-11-07T11:47:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.3% |
| Market draw away odds | 2.87 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T11:46:39Z |
| Market reference draw away last update utc | 2026-11-07T11:47:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.7% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T11:46:39Z |
| Market reference home away last update utc | 2026-11-07T11:47:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.09 |
| Market reference dc draw away odds | 2.81 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 86.9% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market reference over 1 5 last update utc | 2026-11-07T11:47:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.8% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.00 |
| Market reference under 3 5 last update utc | 2026-11-07T11:47:04Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,693.8730 |
| Elo away rating | 1,457.7667 |
| Elo rating diff | 296.1063 |
| Elo home expectancy | 0.8461 |
| Research p home | 0.5330 |
| Research p draw | 0.2034 |
| Research p away | 0.2637 |
| Research p over 1 5 | 0.8876 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.2147691290303118, 1.5270675403330045], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T11:48:24.490810+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-07T11:48:24.491829+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T11:48:24.565295+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Galatasaray%22+%22Amed+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T11:47:34.417901+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T11:47:34.551350+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T11:48:24.626585+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Galatasaray_vs_Amed+SK&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 1.0408527377748258, "goals_for": 2.2981057758943, "last_match": "2026-10-30T00:00:00+00:00", "matches": 10, "points_per_game": 2.6034710533412406, "results": "WWWWLWWWWD", "xg_against": 1.1147534090307207, "xg_for": 2.2984475091718832, "xg_matches": 10}, "venue": {"goals_against": 1.1232992550353904, "goals_for": 2.1999854601202053, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 2.70260329000593, "results": "WWWWD", "xg_against": 0.5544118907898825, "xg_for": 2.502044081155706, "xg_matches": 5}}}, "goal_rates": [2.2147691290303118, 1.5270675403330045], "h2h": [], "margin_distribution": {"-1": 0.14352375566953188, "-10": 6.104237018454033e-07, "-11": 8.266770134603677e-08, "-12": 1.0300621758984217e-08, "-13": 1.188241218876436e-09, "-14": 1.275748879409287e-10, "-15": 1.2795865083792481e-11, "-16": 1.1881010276575295e-12, "-17": 8.90148871717475e-14, "-2": 0.07542173321009207, "-3": 0.030850620605931255, "-4": 0.010214255972087825, "-5": 0.002823751404207546, "-6": 0.0006678356236786268, "-7": 0.00013773235560533275, "-8": 2.5150979950996707e-05, "-9": 4.117255279975263e-06, "0": 0.20337376955408248, "1": 0.2081584310737498, "10": 2.513816336238601e-05, "11": 4.9375127867841104e-06, "12": 8.922900027942272e-07, "13": 1.4928542753514344e-07, "14": 2.3245998948251735e-08, "15": 3.381605072160555e-09, "16": 4.5538300750697865e-10, "17": 4.948303293849024e-11, "2": 0.15864885408822588, "3": 0.0941184034870726, "4": 0.0451947095374506, "5": 0.018120807126154066, "6": 0.006215711877548783, "7": 0.0018592058804462685, "8": 0.0004923984030555384, "9": 0.00011690678988481181}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T11:48:24.626929+00:00", "p_over_1_5": 0.887568611758427, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Goztepe vs Basaksehir

The model's most likely 1X2 outcome is **Goztepe win** at **46.7%**. Expected goals are 1.52 for Goztepe and 1.35 for Basaksehir (2.87 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 56.5%; Under 3.5 goals: 66.2%; Double Chance 1X: 72.5%; Double Chance X2: 53.3%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 82.5%; BTTS Yes (both teams score): 59.7%; BTTS No (at least one team does not score): 40.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Goztepe win | 46.7% | 2.14 |
| Draw | 25.8% | 3.88 |
| Basaksehir win | 27.5% | 3.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Goztepe expected goals | 1.52 |
| Basaksehir expected goals | 1.35 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 80.2% |
| Under 1.5 | 19.8% |
| Over 2.5 | 56.5% |
| Under 2.5 | 43.5% |
| Over 3.5 | 33.8% |
| Under 3.5 | 66.2% |
| Over 4.5 | 17.5% |
| Under 4.5 | 82.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.09% |
| 2 | 2-1 | 10.22% |
| 3 | 1-0 | 8.30% |
| 4 | 2-0 | 7.42% |
| 5 | 1-2 | 6.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Goztepe win | 46.7% | 49.4% | 1.98 | -7.6% |
| Draw | 25.8% | 25.2% | 3.80 | -2.0% |
| Basaksehir win | 27.5% | 25.3% | 3.81 | +4.9% |
| Over 2.5 | 56.5% | 56.3% | 1.71 | -3.5% |
| Under 2.5 | 43.5% | 43.7% | 2.23 | -2.9% |

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
| Market best home last update utc | 2026-11-07T11:46:39Z |
| Market best draw last update utc | 2026-11-07T11:47:01Z |
| Market best away last update utc | 2026-11-07T11:46:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Goztep |
| Matched away-team name | Buyuksehyr |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5170 |
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
| P btts yes | 59.7% |
| P btts no | 40.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.07 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.05 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
| Fair Over 3.5 odds | 2.96 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.72 |
| Fair Under 4.5 odds | 1.21 |
| Score matrix json | [[0.0622432196150492,0.05260093131274712,0.042629502630441615,0.019588986976461664,0.006751106400839734,0.0018613494486560455,0.00042766098427723606,8.42218075117628e-05,1.451301142999835e-05,2.2229924844620234e-06,3.0645094223409367e-07,3.840530711829324e-08,4.411974187742623e-09,4.678564026424985e-10,4.606886451554148e-11,4.233886540214453e-12],[0.08298609025069786,0.12087034762908387,0.06605299210558774,0.03035248178543619,0.010460614135343247,0.002884098871705372,0.000662646427363197,0.0001304988809022651,2.248742702265149e-05,3.4444526904260948e-06,4.748355110688942e-07,5.950774208859252e-08,6.836206810091073e-09,7.249278871066551e-10,7.138216860136349e-11,6.5602659416681614e-12],[0.07415518076716192,0.10222672895421822,0.05886582926345059,0.02351507894824391,0.008104186306035129,0.00223440749069931,0.0005133742658794392,0.00010110183110452177,1.7421758969121608e-05,2.6685322643937717e-06,3.6787089138695713e-07,4.6102630524151076e-08,5.296237190164384e-09,5.61625787887831e-10,5.53021443855484e-11,5.0824566053713084e-12],[0.038300326202601945,0.05279896866363446,0.03639304633068723,0.013970950478378989,0.004185722102173827,0.0011540466205864546,0.0002651520992031741,5.221797143401058e-05,8.998144763958903e-06,1.3782672383924542e-06,1.900012243891891e-07,2.381149596839691e-08,2.735447610418e-09,2.9007347372582653e-10,2.8562942572015787e-11,2.625032315779764e-12],[0.01483626941553466,0.020452560111690023,0.014097452782985178,0.006478021133889056,0.001865138843498145,0.00044703918422357405,0.00010271108290470944,2.022750115572235e-05,3.4855812781304073e-06,5.338947759146298e-07,7.36001395760426e-08,9.223779648906858e-09,1.0596212028472192e-09,1.1236479250153253e-10,1.1064331647130515e-11,1.0168499990150907e-12],[0.0045976608973189535,0.006338111909529102,0.004368706552623318,0.0020074955249937514,0.0006918589462909768,0.0001593589114056259,3.182947925560098e-05,6.2683676407737395e-06,1.0801583806578287e-06,1.6545042865933273e-07,2.2808192159928737e-08,2.8583877678078104e-09,3.2836954047219077e-10,3.4821099445573565e-11,3.428762551030241e-12,3.151150297941673e-13],[0.0011873203619391765,0.001636782158253861,0.0011281941754972646,0.0005184245568690764,0.0001786687258732107,4.9260804770431847e-05,9.455381362132354e-06,1.6187710886532104e-06,2.789448957016714e-07,4.272665323215617e-08,5.890088802829387e-09,7.381627472820219e-10,8.47996079638223e-11,8.992355312882555e-12,8.854588635422587e-13,8.1376704281488e-14],[0.0002628161841471735,0.0003623056210455956,0.0002497284622466931,0.0001147545078583431,3.95487471332022e-05,1.0903996219385137e-05,2.5052865592242766e-06,4.121811874447948e-07,6.17451156618841e-08,9.457646245967461e-09,1.3037851561135048e-09,1.6339407858162673e-10,1.8770594775135953e-11,1.9904792216040708e-12,1.959984240103434e-13,1.8012926909468127e-14],[5.090311364639687e-05,7.017255905551391e-05,4.8368240090438384e-05,2.2226035180841446e-05,7.659933030481353e-06,2.111922294878251e-06,4.852322426596479e-07,9.555965599445297e-08,1.3756672182973701e-08,1.831788416105721e-09,2.5252145025805023e-10,3.1646709194024714e-11,3.6355512966208817e-12,3.8552264335199725e-13,3.79616273795614e-14,3.4888036615866737e-15],[8.763630705302713e-06,1.208111545946855e-05,8.32721937134436e-06,3.826500000000449e-06,1.3187567419314536e-06,3.6359479302536717e-07,8.353901905715718e-08,1.6451833207661367e-08,2.8349622317695897e-09,3.627718382264176e-10,4.3474840274051996e-11,5.448391120847908e-12,6.259072715098063e-13,6.637271932594597e-14,6.535586126180575e-15,6.006427643275944e-16],[1.3578953402573385e-06,1.8719285350074072e-06,1.2902748600311503e-06,5.92903408897789e-07,2.0433695748020623e-07,5.633780014169633e-08,1.2944092297127941e-08,2.5491566683494394e-09,4.3926793971317833e-10,6.728371526181756e-11,7.748876903977941e-12,8.442100270635809e-13,9.698224354685344e-14,1.0284231424582498e-14,1.012667266002118e-15,9.306759244729659e-17],[1.912739570138637e-07,2.6368098300578625e-07,1.81748895365453e-07,8.351673194886793e-08,2.8783027132271973e-08,7.935776523481024e-09,1.823312651735829e-09,3.590757465233445e-10,6.187554705235528e-11,9.477624732317718e-12,1.3065392931649076e-12,1.3679133493351004e-13,1.3660977347321485e-14,1.4486430442079778e-15,1.426449221557296e-16,1.3109557231247583e-17],[2.469771792039637e-08,3.404707384590637e-08,2.346782081658008e-08,1.0783865820044655e-08,3.7165283560084647e-09,1.0246850805833029e-09,2.354301769895286e-10,4.636465746900674e-11,7.989507987010066e-12,1.2237719439096936e-12,1.6870325379508984e-13,2.1142373479493167e-14,2.0290899131761086e-15,1.8705200557229905e-16,1.8418628992569847e-17,1.6927351303511629e-18],[2.943714611061993e-09,4.058061925686319e-09,2.7971234933613195e-09,1.2853261779292361e-09,4.429720535018866e-10,1.2213194972800525e-10,2.8060861903222503e-11,5.526191531877747e-12,9.522673905484692e-13,1.4586106147562994e-13,2.0107697186070032e-14,2.5199540267125534e-15,2.8949051457677706e-16,2.564600860007768e-17,2.195311625791203e-18,2.0175666237395728e-19],[3.2579911290076144e-10,4.4913082624133364e-10,3.095749667398058e-10,1.4225500222876487e-10,4.9026458450969734e-11,1.3517098678213731e-11,3.105669238772595e-12,6.116178151372955e-13,1.053933251270874e-13,1.6143346320647423e-14,2.2254432821309913e-15,2.7889890662922087e-16,3.20397067323972e-17,3.397567913063786e-18,2.794916956055871e-19,2.232965837661138e-20],[3.365432373443349e-11,4.6394215413482525e-11,3.197840552104694e-11,1.4694625332843323e-11,5.064324115468861e-12,1.396286229316571e-12,3.208087248707799e-13,6.317875996994262e-14,1.0886896074378827e-14,1.6675717695942025e-15,2.2988334130998655e-16,2.880963673998205e-17,3.309630444134593e-18,3.509612086967257e-19,3.455843349014681e-20,2.653331949813044e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.14683527552455738, "-10": 3.715563744332534e-07, "-11": 4.583271950884318e-08, "-12": 5.194829251550606e-09, "-13": 5.443210278492333e-10, "-14": 5.262913045720964e-11, "-15": 4.233886540214453e-12, "-2": 0.0823494854536551, "-3": 0.032570512423965206, "-4": 0.010204454598751179, "-5": 0.0026346533121812915, "-6": 0.0005770364367430086, "-7": 0.00010957732936422918, "-8": 1.8350241853553886e-05, "-9": 2.746781948597243e-06, "0": 0.2579847264307477, "1": 0.2288276101703429, "10": 1.6463798930023146e-06, "11": 2.2826547367947562e-07, "12": 2.908004943815534e-08, "13": 3.4248238428243734e-09, "14": 3.7219332831424394e-10, "15": 3.365432373443349e-11, "2": 0.14324917259386058, "3": 0.06368176424450787, "4": 0.02242536684754854, "5": 0.0065077745181883724, "6": 0.001602033236872644, "7": 0.00034193870237850905, "8": 6.436186252699917e-05, "9": 1.0828548811456523e-05} |
| Raw goal margin distribution | {"-1": 0.1760451796462185, "-10": 3.781649729496628e-07, "-11": 4.569904173225116e-08, "-12": 5.073843339394655e-09, "-13": 5.207644947556119e-10, "-14": 4.934653495253818e-11, "-15": 3.906766287265017e-12, "-2": 0.09757248118843366, "-3": 0.03798359364023459, "-4": 0.011692359652647004, "-5": 0.002962976678862472, "-6": 0.0006365291682301985, "-7": 0.00011851096729837892, "-8": 1.9452344047472545e-05, "-9": 2.853333556902495e-06, "0": 0.2709110442275271, "1": 0.19926488218888394, "10": 1.2169533521476422e-06, "11": 1.65294722384313e-07, "12": 2.0627576710918632e-08, "13": 2.3796428847650156e-09, "14": 2.5344652779589473e-10, "15": 2.2553106865837553e-11, "2": 0.12326672995114966, "3": 0.05393539210569972, "4": 0.018661184985691998, "5": 0.005315260434024659, "6": 0.001283435028010762, "7": 0.00026857982377660495, "8": 4.955027246740555e-05, "9": 8.169320069508075e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 58.9% |
| P home draw | 72.5% |
| P draw away | 53.3% |
| P home away | 74.2% |
| Raw p home draw | 67.3% |
| Raw p draw away | 59.8% |
| Raw p home away | 72.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0214 |
| Totals anchor target over 2 5 | 0.5645 |
| Totals anchor reference over odds | 1.72 |
| Totals anchor reference under odds | 2.20 |
| Totals anchor reference last update utc | 2026-11-07T11:47:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5516 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.85, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.47, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.75, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.81, "draw": 3.79, "home": 1.98}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.23}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.88, "home_away": 1.29, "home_draw": 1.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.79, "draw": 3.8, "home": 1.98}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.72, "under": 2.2}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.22, "under": 4.49}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.98 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.79 |
| Market reference 1x2 last update utc | 2026-11-07T11:47:01Z |
| Market reference home last update utc | 2026-11-07T11:47:01Z |
| Market reference draw last update utc | 2026-11-07T11:47:01Z |
| Market reference away last update utc | 2026-11-07T11:47:01Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-11-07T11:47:02Z |
| Market reference under 2 5 last update utc | 2026-11-07T11:47:02Z |
| Market best over 2 5 last update utc | 2026-11-07T11:46:39Z |
| Market best under 2 5 last update utc | 2026-11-07T11:46:39Z |
| Home probability edge | -2.8% |
| Draw probability edge | +0.6% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | -0.0924 |
| Raw ev home | -0.2039 |
| Raw edge prob draw | 0.0185 |
| Raw ev draw | 0.0295 |
| Raw edge prob away | 0.0739 |
| Raw ev away | 0.2460 |
| Market p home draw | 73.9% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T11:46:39Z |
| Market reference home draw last update utc | 2026-11-07T11:47:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.2% |
| Market draw away odds | 1.88 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T11:46:39Z |
| Market reference draw away last update utc | 2026-11-07T11:47:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.9% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T11:46:39Z |
| Market reference home away last update utc | 2026-11-07T11:47:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.28 |
| Market reference dc draw away odds | 1.81 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 81.1% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-11-07T11:47:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.5% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market reference under 3 5 last update utc | 2026-11-07T11:47:04Z |
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
| Team research json | {"base_rates": [1.5169710723874565, 1.349640294863486], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T11:48:24.490810+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-07T11:48:24.491829+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T11:48:24.636358+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Goztepe%22+%22Basaksehir%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T11:47:34.417901+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T11:47:34.551350+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T11:48:24.697548+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Goztepe_vs_Basaksehir&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.5169710723874565, 1.349640294863486], "h2h": [], "margin_distribution": {"-1": 0.18728321621428032, "-10": 3.781649729496628e-07, "-11": 4.569904173225116e-08, "-12": 5.073843339394655e-09, "-13": 5.207644947556119e-10, "-14": 4.934653495253818e-11, "-15": 3.906766287265017e-12, "-2": 0.09757248118843366, "-3": 0.03798359364023459, "-4": 0.011692359652647004, "-5": 0.002962976678862472, "-6": 0.0006365291682301985, "-7": 0.00011851096729837892, "-8": 1.9452344047472545e-05, "-9": 2.853333556902495e-06, "0": 0.2484349710914035, "1": 0.21050291875694577, "10": 1.2169533521476422e-06, "11": 1.65294722384313e-07, "12": 2.0627576710918632e-08, "13": 2.3796428847650156e-09, "14": 2.5344652779589473e-10, "15": 2.2553106865837553e-11, "2": 0.12326672995114966, "3": 0.05393539210569972, "4": 0.018661184985691998, "5": 0.005315260434024659, "6": 0.001283435028010762, "7": 0.00026857982377660495, "8": 4.955027246740555e-05, "9": 8.169320069508075e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T11:48:24.697890+00:00", "p_over_1_5": 0.7800231266895082, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Samsunspor vs Torku Konyaspor

The model's most likely 1X2 outcome is **Samsunspor win** at **42.6%**. Expected goals are 1.41 for Samsunspor and 1.08 for Torku Konyaspor (2.49 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.4%; Double Chance 1X: 70.6%; Double Chance X2: 57.4%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Samsunspor win | 42.6% | 2.35 |
| Draw | 28.0% | 3.57 |
| Torku Konyaspor win | 29.4% | 3.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Samsunspor expected goals | 1.41 |
| Torku Konyaspor expected goals | 1.08 |
| Expected total goals | 2.49 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.6% |
| Under 3.5 | 69.4% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.29% |
| 2 | 2-1 | 8.82% |
| 3 | 1-0 | 8.12% |
| 4 | 0-0 | 7.49% |
| 5 | 1-2 | 7.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Samsunspor win | 42.6% | 42.2% | 2.31 | -1.7% |
| Draw | 28.0% | 27.5% | 3.50 | -2.0% |
| Torku Konyaspor win | 29.4% | 30.2% | 3.21 | -5.5% |
| Over 2.5 | 52.6% | 52.6% | 1.89 | -0.7% |
| Under 2.5 | 47.4% | 47.4% | 2.04 | -3.2% |

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
| Market best home last update utc | 2026-11-07T11:46:39Z |
| Market best draw last update utc | 2026-11-07T11:47:01Z |
| Market best away last update utc | 2026-11-07T11:46:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Pinnacle |
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
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.36 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.51 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.27 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.67 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.07487298576950908,0.06577326276930316,0.047067776792830134,0.019027560007217097,0.005769043034820985,0.0013993116311284408,0.00028284197644692113,4.900343152045035e-05,7.4287745036187596e-06,1.0010489998274337e-06,1.21404841351776e-07,1.3385173050007547e-08,1.3527682884673707e-09,1.2620039999225892e-10,1.0932345927858803e-11,8.83899271799368e-13],[0.08115429114169381,0.13290037508064542,0.07445548825443589,0.03009928165639925,0.009125923193888366,0.00221354051147047,0.0004474215459102186,7.751745819772252e-05,1.1751416159585753e-05,1.5835375521734866e-06,1.9204766732631755e-07,2.11737129458012e-08,2.1399146141166066e-09,1.996336568155072e-10,1.7293639285489142e-11,1.3982209556918637e-12],[0.07269416839420749,0.08816175814190333,0.05813239369458404,0.023806698175899126,0.007218049305410833,0.0017507756981801326,0.0003538831863987086,6.131158715821742e-05,9.29465429920527e-06,1.2524817364464032e-06,1.5189800552768646e-07,1.6747117061401635e-08,1.6925420985799072e-09,1.578980610837062e-10,1.3678215165808829e-11,1.1059075979076213e-12],[0.038331105835343576,0.046487053316872896,0.02818919620228084,0.012391657381478535,0.003806024856767978,0.0009231712813188698,0.0001866000281843571,3.232915360624431e-05,4.901003553871832e-06,6.604245025022873e-07,8.009471261140808e-08,8.830632920048999e-09,8.924651281465179e-10,8.325849823020141e-11,7.212423289802677e-12,5.831370262003773e-13],[0.015158784813996717,0.018384213617377687,0.011147968470972202,0.004506663655979179,0.0014858094451608618,0.00036508612248465125,7.379462741521603e-05,1.2785195523470365e-05,1.938197623750094e-06,2.6117777458150076e-07,3.167501919800436e-08,3.4922463437772723e-09,3.5294277419710684e-10,3.292620004311017e-11,2.8522937247682225e-12,2.3061293183706694e-13],[0.004795870132714583,0.005816317210309434,0.003526945575545989,0.0014257985644036818,0.00043229364531820777,0.00011401888941849724,2.3346821919963957e-05,4.0449243197457395e-06,6.131984990286747e-07,8.263028361532837e-08,1.0021204231661507e-08,1.1048616456867103e-09,1.1166249340556795e-10,1.0417047362842252e-11,9.023962311091431e-13,7.296031216129728e-14],[0.001264413705324774,0.0015334508632886862,0.0009298663642359145,0.0003759066021339434,0.00011397264620169365,2.764466281459546e-05,6.076143277849994e-06,1.0664295748961598e-06,1.6166755245675858e-07,2.178517353199401e-08,2.6420540222592227e-09,2.9129275160401863e-10,2.9439409976854736e-11,2.7464166230747504e-12,2.379134819486838e-13,1.92357207532017e-14],[0.00028573548978689346,0.00034653320478947373,0.00021013361362850845,8.494834928041225e-05,2.5755834302970026e-05,6.247212629898709e-06,1.2627451442676748e-06,2.378951710375684e-07,3.6534052968063074e-08,4.923070038740119e-09,5.970582230439851e-10,6.582709179790742e-11,6.652794250290959e-12,6.20642354356291e-13,5.376430594292802e-14,4.346938084958692e-15],[5.6499841434363994e-05,6.85216636440565e-05,4.155072181931397e-05,1.6797242330778947e-05,5.092823979313432e-06,1.2352911542744717e-06,2.4968862102620506e-07,4.3259488551160945e-08,7.131146407705197e-09,9.734621231914038e-10,1.1805917057845167e-10,1.3016304874977032e-11,1.3154887428132464e-12,1.227225733657859e-13,1.0631072684984349e-14,8.595408036584386e-16],[9.930651703983207e-06,1.204365815109608e-05,7.303131052430491e-06,2.9523545365724534e-06,8.951363374534184e-07,2.171200112191829e-07,4.3886330773859325e-08,7.60347113881886e-09,1.1526636152304204e-09,1.6889937186734552e-10,2.0750580421322608e-11,2.287800937218872e-12,2.3121587943862076e-13,2.1570239869220346e-14,1.8685624135238347e-15,1.5107653631930684e-16],[1.5709081067484098e-06,1.9051599822874407e-06,1.1552663527920767e-06,4.6702651686362615e-07,1.415996624457823e-07,3.434574043360255e-08,6.942282827263518e-09,1.2027764951828084e-09,1.8233734013580491e-10,2.4570487620162297e-11,3.240273991142849e-12,3.619022342171364e-13,3.65755350450368e-14,3.4121491403705857e-15,2.9558380767624693e-16,2.3898467363252416e-17],[2.2590774808849964e-07,2.739755428710199e-07,1.6613551046081035e-07,6.716173165638562e-08,2.0363037618687083e-08,4.939161523488099e-09,9.98349600058267e-10,1.729678065274912e-10,2.622140513857794e-11,3.5334107092975844e-12,4.2852364536290274e-13,5.137479062186035e-14,5.259821832773561e-15,4.906912919551711e-16,4.250705186172897e-17,3.436769421206835e-18],[2.9779877782103e-08,3.611632735495205e-08,2.190051133107679e-08,8.853473053868136e-09,2.6843203771802717e-09,6.510959794876955e-10,1.3160561921895461e-10,2.2801166326571632e-11,3.456589014361525e-12,4.657854366094345e-13,5.64893497174307e-14,6.228085412667472e-15,6.844492835354007e-16,6.468448659601824e-17,5.603414756823225e-18,4.530458746758611e-19],[3.623702949085351e-09,4.3947407341249845e-09,2.6649185089871034e-09,1.0773165910785028e-09,3.266359834735069e-10,7.922727011408716e-11,1.601415808249337e-11,2.774512852763912e-12,4.2060789828511334e-13,5.667813926681002e-14,6.873789901380575e-15,7.578517159194605e-16,7.6592044408111e-17,7.76977189560119e-18,6.8183995675937875e-19,5.512795197300962e-20],[4.0944689726103383e-10,4.965674568629687e-10,3.0111259953956285e-10,1.217273992329489e-10,3.6907023518798826e-11,8.951992032035285e-12,1.8094604969702714e-12,3.1349580662007127e-13,4.752503208349153e-14,6.4041364845266e-15,7.766784383512706e-16,8.563064854570807e-17,8.654234460828516e-18,8.073576678979738e-19,7.605116969365503e-20,6.2289788111361066e-21],[4.317967369199949e-11,5.236728107317758e-11,3.1754896372749746e-11,1.283719430630718e-11,3.8921609692128134e-12,9.440640469433827e-13,1.90823069707934e-13,3.306081136337165e-14,5.0119206942205505e-15,6.753709101978925e-16,8.190737738144102e-17,9.030483530274997e-18,9.126629669741923e-19,8.514276426508872e-20,7.375651362889343e-21,6.484508745713355e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.16823101095901855, "-10": 1.4435728014842427e-07, "-11": 1.56904287614295e-08, "-12": 1.5666632974748873e-09, "-13": 1.445999468756557e-10, "-14": 1.2330566883550667e-11, "-15": 8.83899271799368e-13, "-2": 0.08538628529870057, "-3": 0.030104279716975182, "-4": 0.008370819423422245, "-5": 0.0019132172647997228, "-6": 0.00037034732339802937, "-7": 6.209103083897157e-05, "-8": 9.17340429632196e-06, "-9": 1.2107700971752943e-06, "0": 0.27990356160258345, "1": 0.20247315463229168, "10": 1.867899328629151e-06, "11": 2.6481461351264097e-07, "12": 3.4488568310073854e-08, "13": 4.15202530232107e-09, "14": 4.618141783342114e-10, "15": 4.317967369199949e-11, "2": 0.13187546608330802, "3": 0.06064520787165986, "4": 0.021995233800577694, "5": 0.006557182355618303, "6": 0.0016555966597224362, "7": 0.00036204834146650813, "8": 6.976869306007714e-05, "9": 1.2011136448583901e-05} |
| Raw goal margin distribution | {"-1": 0.16524943961642444, "-10": 5.772609122055673e-08, "-11": 5.61662906375349e-09, "-12": 5.017211100246888e-10, "-13": 4.122938804436644e-11, "-14": 2.8742589285528503e-12, "-2": 0.07822129582243896, "-3": 0.0252306347046817, "-4": 0.006364765541021291, "-5": 0.0013134144062646948, "-6": 0.00022886209019950255, "-7": 3.447208398035707e-05, "-8": 4.569345152864736e-06, "-9": 5.405636886236529e-07, "0": 0.29026203118361305, "1": 0.21924667117919575, "10": 8.228028000427578e-07, "11": 1.0442192943257091e-07, "12": 1.2166641348951772e-08, "13": 1.3040900498344392e-09, "14": 1.1858204689359174e-10, "2": 0.13307906110026438, "3": 0.05598932847793167, "4": 0.018422639510645045, "5": 0.004958651428707406, "6": 0.0011270106649643758, "7": 0.00022141858235622875, "8": 3.828184426243387e-05, "9": 5.907151619402977e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.99, "date": "2026-11-01T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 5.0, "home_xg": 3.89, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 2.0, "away_xg": 1.63, "date": "2026-10-24T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.08, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 1.0, "away_xg": 1.07, "date": "2026-10-18T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 4.0, "home_xg": 2.41, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 0.36, "date": "2026-09-20T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 5.0, "away_xg": 1.73, "date": "2026-09-12T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.32, "date": "2026-08-22T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.85, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 3.0, "away_xg": 1.89, "date": "2026-08-17T00:00:00+00:00", "home": "Samsunspor", "home_goals": 3.0, "home_xg": 2.74, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 51.2% |
| P home draw | 70.6% |
| P draw away | 57.4% |
| P home away | 72.0% |
| Raw p home draw | 72.3% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1203 |
| Totals anchor target over 2 5 | 0.5255 |
| Totals anchor reference over odds | 1.85 |
| Totals anchor reference under odds | 2.04 |
| Totals anchor reference last update utc | 2026-11-07T11:47:01Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4582 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.3, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.07, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.07, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.21, "draw": 3.48, "home": 2.31}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.89, "under": 1.99}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.66, "home_away": 1.33, "home_draw": 1.38}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.2, "draw": 3.5, "home": 2.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.85, "under": 2.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.85, "under": 2.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.27, "under": 3.98}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.31 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-11-07T11:47:01Z |
| Market reference home last update utc | 2026-11-07T11:47:01Z |
| Market reference draw last update utc | 2026-11-07T11:47:01Z |
| Market reference away last update utc | 2026-11-07T11:47:01Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference under 2 5 last update utc | 2026-11-07T11:47:01Z |
| Market best over 2 5 last update utc | 2026-11-07T11:46:39Z |
| Market best under 2 5 last update utc | 2026-11-07T11:47:01Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0106 |
| Raw ev home | 0.0004 |
| Raw edge prob draw | 0.0148 |
| Raw ev draw | 0.0159 |
| Raw edge prob away | -0.0254 |
| Raw ev away | -0.1120 |
| Market p home draw | 70.2% |
| Market home draw odds | 1.38 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T11:46:39Z |
| Market reference home draw last update utc | 2026-11-07T11:47:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.5% |
| Market draw away odds | 1.66 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T11:46:39Z |
| Market reference draw away last update utc | 2026-11-07T11:47:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.3% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T11:46:39Z |
| Market reference home away last update utc | 2026-11-07T11:47:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.61 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 78.2% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 3.60 |
| Market reference over 1 5 last update utc | 2026-11-07T11:47:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.5% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 2.80 |
| Market reference under 3 5 last update utc | 2026-11-07T11:47:04Z |
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
| Team research json | {"base_rates": [1.4120296001898005, 1.0825586634163595], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T11:48:24.490810+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-07T11:48:24.491829+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T11:48:24.492863+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Samsunspor%22+%22Torku+Konyaspor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T11:47:34.417901+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T11:47:34.551350+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T11:48:24.555488+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Samsunspor_vs_Torku+Konyaspor&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.913613856180298, "goals_for": 0.9751316584067636, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.22037567410820427, "results": "LLLLLLLLWD", "xg_against": 2.102762810589968, "xg_for": 1.119679917641185, "xg_matches": 10}, "venue": {"goals_against": 2.9627088822913965, "goals_for": 0.9012025941363605, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.148698354997035, "results": "LLLLD", "xg_against": 1.764225747400591, "xg_for": 1.383053774479519, "xg_matches": 5}}}, "goal_rates": [1.4120296001898005, 1.0825586634163595], "h2h": [], "margin_distribution": {"-1": 0.17742132705615185, "-10": 5.772609122055673e-08, "-11": 5.61662906375349e-09, "-12": 5.017211100246888e-10, "-13": 4.122938804436644e-11, "-14": 2.8742589285528503e-12, "-2": 0.07822129582243896, "-3": 0.0252306347046817, "-4": 0.006364765541021291, "-5": 0.0013134144062646948, "-6": 0.00022886209019950255, "-7": 3.447208398035707e-05, "-8": 4.569345152864736e-06, "-9": 5.405636886236529e-07, "0": 0.2659182563041582, "1": 0.23141855861892316, "10": 8.228028000427578e-07, "11": 1.0442192943257091e-07, "12": 1.2166641348951772e-08, "13": 1.3040900498344392e-09, "14": 1.1858204689359174e-10, "2": 0.13307906110026438, "3": 0.05598932847793167, "4": 0.018422639510645045, "5": 0.004958651428707406, "6": 0.0011270106649643758, "7": 0.00022141858235622875, "8": 3.828184426243387e-05, "9": 5.907151619402977e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T11:48:24.555835+00:00", "p_over_1_5": 0.71159014477609, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Alanyaspor vs Trabzonspor

The model's most likely 1X2 outcome is **Trabzonspor win** at **55.2%**. Expected goals are 1.18 for Alanyaspor and 1.61 for Trabzonspor (2.79 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 56.0%; Under 3.5 goals: 66.8%; Double Chance 1X: 44.8%; Double Chance X2: 79.3%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alanyaspor win | 20.7% | 4.82 |
| Draw | 24.1% | 4.16 |
| Trabzonspor win | 55.2% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alanyaspor expected goals | 1.18 |
| Trabzonspor expected goals | 1.61 |
| Expected total goals | 2.79 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 79.8% |
| Under 1.5 | 20.2% |
| Over 2.5 | 56.0% |
| Under 2.5 | 44.0% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.36% |
| 2 | 1-2 | 11.16% |
| 3 | 0-1 | 9.71% |
| 4 | 0-2 | 9.16% |
| 5 | 1-3 | 6.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alanyaspor win | 20.7% | 18.1% | 5.16 | +7.0% |
| Draw | 24.1% | 22.8% | 4.11 | -1.1% |
| Trabzonspor win | 55.2% | 59.0% | 1.68 | -7.3% |
| Over 2.5 | 56.0% | 56.4% | 1.73 | -3.0% |
| Under 2.5 | 44.0% | 43.6% | 2.21 | -2.9% |

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
| Market best home last update utc | 2026-11-07T11:46:39Z |
| Market best draw last update utc | 2026-11-07T11:46:39Z |
| Market best away last update utc | 2026-11-07T11:46:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alanyaspor |
| Matched away-team name | Trabzonspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1769 |
| Dc lambda away | 1.6081 |
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
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.38 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.94 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Score matrix json | [[0.06106264436354819,0.0971219438886507,0.09160355248384079,0.05082875356812751,0.021152800185439188,0.007042328198513008,0.001953814862208739,0.0004646262763653889,9.667900641797882e-05,1.7881669648484125e-05,2.9766410427471085e-06,4.504557954162602e-07,6.248695055409282e-08,8.00137043265377e-09,9.513815822194444e-10,1.0558005378758137e-10],[0.044130961127600274,0.11356242631973541,0.11159923919115043,0.0619239109557257,0.02577014038701025,0.008579563213196079,0.0023803034514553517,0.000566047249747672,0.00011778258887837409,2.1784970933199807e-05,3.626397303470623e-06,5.487835645518995e-07,7.612691813935868e-08,9.747950036416393e-09,1.159053965455022e-09,1.2862660188351673e-10],[0.0320256128526704,0.05331087952654875,0.052509789551574586,0.037720487704986094,0.015697688479640606,0.005226176830609084,0.0014499440634321828,0.0003448034530605502,7.17463840232033e-05,1.3270152281350082e-05,2.208992823414529e-06,3.342874082061566e-07,4.637214341560655e-08,5.937890934575487e-09,7.06029063387493e-10,7.83519335261352e-11],[0.013005441863617745,0.021649282640442805,0.018019050938858357,0.011832188615425865,0.0063747531032220285,0.0021223243799315785,0.0005888150621571186,0.00014002296486200478,2.9135849191431144e-05,5.388942744371629e-06,8.970609828523849e-07,1.357524514258315e-07,1.8831496466826487e-08,2.4113479325871852e-09,2.867148859930369e-10,3.1818329943098205e-11],[0.003961083871666741,0.006593749385794281,0.005488085126605515,0.0030452151570251147,0.0014997277146311398,0.0006463990197295445,0.00017933614794201375,4.2646971444272014e-05,8.873942425773811e-06,1.6413171050943508e-06,2.7321899773497273e-07,4.134629576764747e-08,5.735532688263918e-09,7.34427288585108e-10,8.732511533121155e-11,9.690948979869402e-12],[0.0009651458583515628,0.001606613269723497,0.0013372104206405867,0.0007419880244432926,0.000308784365526513,0.00012165773436575201,4.369650985605791e-05,1.0391233610349434e-05,2.1621982914191594e-06,3.9991842070156143e-07,6.657172446487889e-08,1.0074314862091632e-08,1.3975027540097632e-09,1.789483582785195e-10,2.1277376627859063e-11,2.3612676667413346e-12],[0.00019597046289866797,0.00032621882324046595,0.00027151724566630515,0.0001506588204851978,6.269789641065838e-05,2.087379259527854e-05,6.853375684009902e-06,2.109914105818613e-06,4.390289782435924e-07,8.120243934988891e-08,1.351722285958641e-08,2.0455645432525735e-09,2.837594538023675e-10,3.6335018487976675e-11,4.320318334218014e-12,4.79449519132061e-13],[3.4106840947316965e-05,5.6775359682834655e-05,4.725505760111772e-05,2.6220769964992243e-05,1.0911987189188884e-05,3.6328899441472244e-06,1.0079045119115962e-06,2.8364541978556936e-07,7.640892056248272e-08,1.4132531211465735e-08,2.3525472323843985e-09,3.56011530983942e-10,4.938570034984935e-11,6.323772868914651e-12,7.519113242241198e-13,8.34437407016808e-14],[5.1939818349370155e-06,8.646071540901719e-06,7.196266319951147e-06,3.993046530067021e-06,1.6617388673216006e-06,5.532369417435123e-07,1.5348937576207005e-07,3.6500488608914826e-08,8.988001100363031e-09,2.152181449680928e-09,3.582591424902146e-10,5.421544105521075e-11,7.520732597867247e-12,9.630197490334868e-13,1.145052913442204e-13,1.2707282803270547e-14],[7.030833841828929e-07,1.1703755292279138e-06,9.741226362556156e-07,5.405187689866697e-07,2.249412923637778e-07,7.488892214439934e-08,2.0777090328084395e-08,4.940888873131027e-09,1.0280955928981937e-09,2.2503258747526125e-10,4.849575110605596e-11,7.33887352390557e-12,1.0180440160332645e-12,1.3035917446438946e-13,1.5500009492451155e-14,1.7201214176369705e-15],[8.565559810204017e-08,1.4258510187453235e-07,1.1867590517756554e-07,6.585059394731486e-08,2.7404261526756868e-08,9.123605480949616e-09,2.531241868189615e-09,6.019411084157587e-10,1.2525134983542551e-10,2.3166386827567675e-11,4.563654202629133e-12,8.940839951948532e-13,1.2402678124569167e-13,1.5881463433832016e-14,1.888342995342127e-15,2.0955982199331415e-16],[9.486630476909917e-09,1.5791754455848295e-08,1.3143734722290722e-08,7.293163147597444e-09,3.0351093023393343e-09,1.010468384235326e-09,2.803431040501491e-10,6.666689616245714e-11,1.3871986174299473e-11,2.5657511731629994e-12,4.2710330733355e-13,7.648824126789254e-14,1.3736361300247499e-14,1.758922690024772e-15,2.091400049431831e-16,2.3209418159561477e-17],[9.631183462176029e-10,1.603238206907076e-09,1.334401300827197e-09,7.404293069605474e-10,3.081356925384204e-10,1.0258654445312614e-10,2.846148454959503e-11,6.768273617880066e-12,1.4083361226584462e-12,2.604846929283517e-13,4.336113143906779e-14,6.561850311150778e-15,1.0772078231419651e-15,1.7857243585744464e-16,2.1232678576348484e-17,2.356307277796578e-18],[9.025789920427781e-11,1.5024624237276438e-10,1.2505239733114434e-10,6.938876620717925e-11,2.8876700758111645e-11,9.613819553255016e-12,2.667246256672447e-12,6.342835855933015e-13,1.3198114261228083e-13,2.4411123774058495e-14,4.063555269381797e-15,6.149387832796963e-16,8.530392934357464e-17,1.2926474981160901e-17,1.989804233620012e-18,2.208195343894101e-19],[7.854274993448981e-12,1.3074482286112724e-11,1.0882104789586126e-11,6.0382355012922275e-12,2.5128609313676117e-12,8.365980504128876e-13,2.3210473276958233e-13,5.5195586746434123e-14,1.1485046706885133e-14,2.1242648090737785e-15,3.536120474571228e-16,5.3512195061002995e-17,7.423178746602404e-18,9.505281088721332e-19,1.3374924969215073e-19,1.92157956512419e-20],[6.379163907219338e-13,1.0618964267830435e-12,8.838337105106023e-13,4.904194722652479e-13,2.0409206159208766e-13,6.794766025502315e-14,1.8851315178211387e-14,4.482930570986173e-15,9.32804052396919e-16,1.7253067164979758e-16,2.87200182343738e-17,4.3462071752510835e-18,6.0290318300110485e-19,7.720094610860981e-20,9.17937231826015e-21,1.2055248082644484e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2535087079422064, "-10": 3.574297785030199e-06, "-11": 5.328170103251674e-07, "-12": 7.29727479838398e-08, "-13": 9.238776331634926e-09, "-14": 1.080008184102961e-09, "-15": 1.0558005378758137e-10, "-2": 0.17153765720792435, "-3": 0.0824587786278758, "-4": 0.03133161816866333, "-5": 0.009798280936978872, "-6": 0.002597281022236035, "-7": 0.0005966188594061242, "-8": 0.00012081464151082761, "-9": 2.1861942040742457e-05, "0": 0.24059558053805966, "1": 0.11883681036485053, "10": 1.0285372343351446e-07, "11": 1.1221163408711023e-08, "12": 1.1247371128522188e-09, "13": 1.0421621520090114e-10, "14": 8.916171420232025e-12, "15": 6.379163907219338e-13, "2": 0.05997145798864254, "3": 0.02109854710783677, "4": 0.005867174384152871, "5": 0.0013428471378665698, "6": 0.00026051105150777716, "7": 4.379602613764306e-05, "8": 6.490644418589847e-06, "9": 8.595823822368003e-07} |
| Raw goal margin distribution | {"-1": 0.21670143786109297, "-10": 2.3340590425645797e-06, "-11": 3.364577180525608e-07, "-12": 4.4553510975861556e-08, "-13": 5.453559541442281e-09, "-14": 6.168235541684443e-10, "-15": 5.871976270412512e-11, "-2": 0.14370738939985225, "-3": 0.06728985976662952, "-4": 0.024836368660960933, "-5": 0.00753266667127903, "-6": 0.0019345238773434425, "-7": 0.0004302478044263826, "-8": 8.431537142253941e-05, "-9": 1.4760349764787175e-05, "0": 0.2694800835071443, "1": 0.15557372352598908, "10": 1.0290039208562026e-07, "11": 1.0855909296731755e-08, "12": 1.0520785441997546e-09, "13": 9.424901246482286e-11, "14": 7.80168152600784e-12, "15": 5.435532283640128e-13, "2": 0.07697330573314327, "3": 0.026377958506367327, "4": 0.007125415176048931, "5": 0.0015816170779302044, "6": 0.0002972741934947885, "7": 4.838740114008394e-05, "8": 6.939863220318771e-06, "9": 8.891424013791999e-07} |
| Research history json | {"away": [{"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.51, "date": "2026-11-01T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 1.37, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 4.0, "away_xg": 2.63, "date": "2026-10-26T00:00:00+00:00", "home": "Rizespor", "home_goals": 3.0, "home_xg": 1.81, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 1.19, "date": "2026-10-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.35, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": 0.92, "date": "2026-09-12T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Genclerbirligi", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-06T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": 3.2, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-08-31T00:00:00+00:00", "home": "Amedspor", "home_goals": 2.0, "home_xg": 2.39, "source": "pipeline training history"}, {"away": "Buyuksehyr", "away_goals": 1.0, "away_xg": 1.95, "date": "2026-08-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-08-15T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 1.0, "home_xg": 1.86, "source": "pipeline training history"}], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-11-02T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 5.0, "home_xg": 1.91, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Erzurumspor", "away_goals": 0.0, "away_xg": 1.69, "date": "2026-10-10T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 0.0, "home_xg": 0.98, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-19T00:00:00+00:00", "home": "Corum", "home_goals": 1.0, "home_xg": 1.14, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 1.79, "date": "2026-09-12T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": 1.73, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 2.06, "date": "2026-09-07T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 0.74, "date": "2026-08-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.54, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 1.25, "date": "2026-08-15T00:00:00+00:00", "home": "Gaziantep", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 46.3% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 56.5% |
| P home draw | 44.8% |
| P draw away | 79.3% |
| P home away | 75.9% |
| Raw p home draw | 53.7% |
| Raw p draw away | 73.2% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0351 |
| Totals anchor target over 2 5 | 0.5605 |
| Totals anchor reference over odds | 1.72 |
| Totals anchor reference under odds | 2.16 |
| Totals anchor reference last update utc | 2026-11-07T11:47:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5396 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.47, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.47, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.68, "draw": 4.11, "home": 5.16}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.73, "under": 2.21}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.19, "home_away": 1.26, "home_draw": 2.26}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.65, "draw": 4.07, "home": 5.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.72, "under": 2.16}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.23, "under": 4.25}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.06 |
| Reference draw odds | 4.07 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-11-07T11:47:01Z |
| Market reference home last update utc | 2026-11-07T11:47:01Z |
| Market reference draw last update utc | 2026-11-07T11:47:01Z |
| Market reference away last update utc | 2026-11-07T11:47:01Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-11-07T11:46:39Z |
| Market reference under 2 5 last update utc | 2026-11-07T11:46:39Z |
| Market best over 2 5 last update utc | 2026-11-07T11:46:39Z |
| Market best under 2 5 last update utc | 2026-11-07T11:46:39Z |
| Home probability edge | +2.6% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.0865 |
| Raw ev home | 0.3828 |
| Raw edge prob draw | 0.0413 |
| Raw ev draw | 0.1076 |
| Raw edge prob away | -0.1278 |
| Raw ev away | -0.2229 |
| Market p home draw | 43.0% |
| Market home draw odds | 2.26 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T11:46:39Z |
| Market reference home draw last update utc | 2026-11-07T11:47:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.1% |
| Market draw away odds | 1.19 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T11:46:39Z |
| Market reference draw away last update utc | 2026-11-07T11:47:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.9% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T11:46:39Z |
| Market reference home away last update utc | 2026-11-07T11:47:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.19 |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 80.4% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-11-07T11:47:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.8% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market reference under 3 5 last update utc | 2026-11-07T11:47:04Z |
| Market under 3 5 bookmakers | 1 |
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
| Team research json | {"base_rates": [1.1769337073670492, 1.608131215177483], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T11:48:24.703300+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-07T11:48:24.491829+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T11:48:24.842755+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Alanyaspor%22+%22Trabzonspor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T11:47:34.417901+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T11:47:34.551350+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T11:48:24.906754+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Alanyaspor_vs_Trabzonspor&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.7743771520489182, "goals_for": 2.5504665648542564, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.445760234190055, "results": "WWWWWLWLWD", "xg_against": 1.304688418272264, "xg_for": 1.9416908629267322, "xg_matches": 10}, "venue": {"goals_against": 1.4632227425095123, "goals_for": 2.031257084649452, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.6015486554658407, "results": "WWLLD", "xg_against": 1.7335781977270697, "xg_for": 1.5880534238553998, "xg_matches": 5}}, "home": {"all": {"goals_against": 2.0080296773705193, "goals_for": 0.7681538045198641, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 0.9433296058372811, "results": "LLLDWDWLWD", "xg_against": 1.821921306986439, "xg_for": 0.9535220089451488, "xg_matches": 10}, "venue": {"goals_against": 1.069203922761527, "goals_for": 0.9657278891499795, "last_match": "2026-10-23T00:00:00+00:00", "matches": 4, "points_per_game": 1.0971691275701443, "results": "LDDW", "xg_against": 1.4768169943171596, "xg_for": 0.9185985305199439, "xg_matches": 4}}}, "goal_rates": [1.187659881213534, 1.5915881547569133], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.226730788896033, "-10": 2.116590637947125e-06, "-11": 3.019759412748168e-07, "-12": 3.9576691474772934e-08, "-13": 4.79460518107939e-09, "-14": 5.367283716407136e-10, "-15": 5.057650063243132e-11, "-2": 0.14148827758192603, "-3": 0.06557894561714249, "-4": 0.023958231001160048, "-5": 0.007192083504853036, "-6": 0.0018281489342660212, "-7": 0.0004024227106687028, "-8": 7.805367150449747e-05, "-9": 1.352394546255212e-05, "0": 0.24803573629409484, "1": 0.1691889079488914, "10": 1.1330543742874287e-07, "11": 1.2062785705887104e-08, "12": 1.1797123948902076e-09, "13": 1.0664755311011564e-10, "14": 8.908692857880758e-12, "15": 6.264257459268826e-13, "2": 0.07878494494954082, "3": 0.02724887609179904, "4": 0.007428485848837631, "5": 0.0016640319539462346, "6": 0.00031563118234721434, "7": 5.184563508428778e-05, "8": 7.503855132331752e-06, "9": 9.70188011023177e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T11:48:24.907112+00:00", "p_over_1_5": 0.7653647218666602, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Besiktas JK vs Genclerbirligi SK

The model's most likely 1X2 outcome is **Besiktas JK win** at **76.5%**. Expected goals are 1.92 for Besiktas JK and 0.81 for Genclerbirligi SK (2.73 combined). The most likely exact score is 2-1 at 10.6%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 70.7%; Under 3.5 goals: 51.1%; Double Chance 1X: 91.3%; Double Chance X2: 23.5%; Double Chance 12 (either team wins): 85.2%; Under 4.5 goals: 70.2%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

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
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 48.9% |
| Under 3.5 | 51.1% |
| Over 4.5 | 29.8% |
| Under 4.5 | 70.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.57% |
| 2 | 2-0 | 10.04% |
| 3 | 3-1 | 8.82% |
| 4 | 3-0 | 8.38% |
| 5 | 1-0 | 7.21% |

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
| Market best home last update utc | 2026-11-07T11:46:39Z |
| Market best draw last update utc | 2026-11-07T11:46:39Z |
| Market best away last update utc | 2026-11-07T11:46:39Z |
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
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.89 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.64 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.42 |
| Fair Over 3.5 odds | 2.05 |
| Fair Under 3.5 odds | 1.96 |
| Fair Over 4.5 odds | 3.35 |
| Fair Under 4.5 odds | 1.43 |
| Score matrix json | [[0.028658682658945635,0.01492462913143971,0.010351965941366678,0.0036314412907528897,0.0009554247417503574,0.00020109622908638227,3.527200310816415e-05,5.302852309270408e-06,6.975847731624153e-07,8.157027574635566e-08,8.584388775654363e-09,8.212854719143307e-10,7.202617336401885e-11,5.830750219526965e-12,4.3830240051267006e-13,3.075105625487956e-14,2.022634928429322e-15,1.252120220190907e-16,7.320672379755358e-18],[0.0721469011268931,0.06597382852319111,0.02589782710296321,0.009084886794948606,0.0023902150482227502,0.00050308853423927,8.82410397449413e-05,1.3266306422942441e-05,1.7451689802057976e-06,2.0406683232781747e-07,2.147582570844163e-08,2.054634769306906e-09,1.8019006198769925e-10,1.4586964632723505e-11,1.0965144062087473e-12,7.693084991131898e-14,5.060087133745092e-15,3.1324671234715486e-16,1.8314348080564937e-17],[0.10044496616714212,0.10570745682133131,0.0396029854897795,0.011363968390071357,0.0029898367328670583,0.0006292959207462241,0.00011037764245186898,1.659436052930711e-05,2.1829710786730774e-06,2.5526009122367153e-07,2.686336219809695e-08,2.5700710530072523e-09,2.2539347103056523e-10,1.82463258744763e-11,1.3715916700626934e-12,9.623012001642653e-14,6.329486710925088e-15,3.9182939950183287e-16,2.290877997379398e-17],[0.08376207256648577,0.08815051671532599,0.046384439634126515,0.011585195248724556,0.0024932550722713905,0.0005247762291205963,9.204503171803025e-05,1.3838204978209684e-05,1.8204016475856863e-06,2.1286397019464787e-07,2.2401629267040933e-08,2.143208228920079e-09,1.8795789372917538e-10,1.5215795577315744e-11,1.1437841574679237e-12,8.024726975849498e-14,5.278222945557085e-15,3.2675049678588474e-16,1.9103863177986714e-17],[0.05238752922390116,0.055132205173894444,0.029010339792372105,0.010176747718982864,0.0019063441897444991,0.0003282121513557637,5.756796174325521e-05,8.654864254067604e-06,1.1385385006613386e-06,1.331320622521172e-07,1.4010708808077712e-08,1.3404322539456794e-09,1.1755499056908307e-10,9.51645429784257e-12,7.153598775582441e-13,5.0189257032466145e-14,3.301172599223311e-15,2.0436040650388274e-16,1.1948178451909776e-17],[0.026211894086137392,0.027585181896572424,0.014515209350502907,0.005091895672560501,0.001339667288677895,0.00020076095212210893,2.8803903110600757e-05,4.330427269969707e-06,5.696632583066937e-07,6.661210343223132e-08,7.010203015672921e-09,6.706800032484935e-10,5.881817691619366e-11,4.761520457750668e-12,3.579274995751092e-13,2.5111997246030128e-14,1.6517287188917867e-15,1.0225092517315821e-16,5.9782240686556656e-18],[0.010929181711777496,0.011501781004811846,0.0060521898972587885,0.002123091634658283,0.0005585810465726087,0.00011756922046951425,1.4682320031495561e-05,1.805593535805019e-06,2.3752397457800656e-07,2.777425317766705e-08,2.9229395763223195e-09,2.796434169110615e-10,2.4524536126999357e-11,1.9853400191566097e-12,1.492396798813323e-13,1.0470574165514762e-14,6.886966370307791e-16,4.263404001795618e-17,2.4926507388344065e-18],[0.0039059807569972044,0.004110622044793912,0.0021629924270461236,0.0007587718174161711,0.0001996313060459789,4.2018069136339526e-05,7.369911767661214e-06,7.888901734015036e-07,8.488870425014622e-08,9.926241626583047e-09,1.044629510247544e-09,9.99417736918482e-11,8.764825099679194e-12,7.095407611866826e-13,5.333677608898506e-14,3.7420789848466325e-15,2.4613332293231773e-16,1.523698153208781e-17,8.908485627345813e-19],[0.0012214638128298858,0.0012854584772190535,0.0006764029680200029,0.00023728030802730386,6.24279614809443e-05,1.3139734711463083e-05,2.304691468799715e-06,3.4649119416332687e-07,3.245297481231605e-08,3.1040974594042355e-09,3.266726653211964e-10,3.1253420728184566e-11,2.7409035914635694e-12,2.2188495474913194e-13,1.6679278762189813e-14,1.1702090586476044e-15,7.696989969928145e-17,4.764852342106879e-18,2.785828578757087e-19],[0.0003395303399520089,0.00035731893911224866,0.00018801975733059582,6.595681575025759e-05,1.7353102696533143e-05,3.65245252999043e-06,6.406351704133893e-07,9.631416969455184e-08,1.267003007065537e-08,1.0548420500033363e-09,9.080521252002242e-11,8.687514483068472e-12,7.618890698278234e-13,6.167736884621165e-14,4.6363397169829525e-15,3.252830540898528e-16,2.139532578572487e-17,1.3244861767853195e-18,7.743768701604165e-20],[8.494133471933122e-05,8.939156251243949e-05,4.703747283239237e-05,1.650061660014174e-05,4.341278322206767e-06,9.137451249282664e-07,1.6026964320994404e-07,2.4095207890392794e-08,3.16969984269343e-09,3.706406735765796e-10,2.777188603143713e-11,2.173381841780795e-12,1.906040989102545e-13,1.5430014391391998e-14,1.1598871659847616e-15,8.13770480124924e-17,5.352533529849697e-18,3.3135072314701233e-19,1.9372820978679325e-20],[1.931821025297174e-05,2.0330325690820156e-05,1.0697733829437953e-05,3.7527357185814143e-06,9.873370564775491e-07,2.0781308063169516e-07,3.645012966806889e-08,5.479973839047024e-09,7.208849284308168e-10,8.429481929044746e-11,8.87111749888941e-12,6.042796156505399e-13,4.334909581999455e-14,3.509248626763719e-15,2.637931722671379e-16,1.8507584422425268e-17,1.2173268580883867e-18,7.535910470890485e-20,4.405961244851224e-21],[4.027412698739554e-06,4.238416022215339e-06,2.2302370927858832e-06,7.823610619261852e-07,2.0583758780563623e-07,4.332435711903111e-08,7.599032890394264e-09,1.1424513937435511e-09,1.5028830709851126e-10,1.7573575460805423e-11,1.849428637497195e-12,1.7693849975975484e-13,1.1048247445168095e-14,7.315994751785257e-16,5.499494818191198e-17,3.858415430301244e-18,2.537852928703738e-19,1.5710679783268174e-20,9.185439041869044e-22],[7.750384979640619e-07,8.156441450941111e-07,4.291885971947885e-07,1.5055818403974577e-07,3.9611548855510694e-08,8.337373688398332e-09,1.4623639239142056e-09,2.1985425344690042e-10,2.8921601163855382e-11,3.3818728170727086e-12,3.559055156542928e-13,3.405018540283526e-14,2.9861779378430546e-15,1.721173409920815e-16,1.0583271500300957e-17,7.425165294229563e-19,4.8838643294039005e-20,3.023375693538763e-21,1.7676531834889105e-22],[1.3849552230051092e-07,1.457515493525854e-07,7.669386629188071e-08,2.6903998175543426e-08,7.078386637937748e-09,1.4898471838786082e-09,2.6131715517093416e-10,3.928686089930112e-11,5.168146188192252e-12,6.04323841183052e-13,6.359854434283798e-14,6.0845986672697774e-15,5.336151355968043e-16,4.3197860218106304e-17,2.3119929052319043e-18,1.3268400838065648e-19,8.727222491817323e-21,5.402621894102818e-22,3.158708264641704e-23],[2.309856318686e-08,2.430873804712904e-08,1.2791158061729367e-08,4.487103203874943e-09,1.1805476328878213e-09,2.484797251489084e-10,4.3583003408797255e-11,6.552342081694426e-12,8.619538690056843e-13,1.0079035191191292e-13,1.0607093794034824e-14,1.0148016661336976e-15,8.899741105205526e-17,7.204626454420712e-18,5.415778331910555e-19,2.7053404069943163e-20,1.4555438098252842e-21,9.010602012451261e-23,5.268157499082853e-24],[3.611648497060721e-09,3.800869193599877e-09,2.0000017497015142e-09,7.015951343523497e-10,1.8458823821792436e-10,3.885182894815852e-11,6.814557575958585e-12,1.0245120547169565e-12,1.3477350821980895e-13,1.5759392480652643e-14,1.658505511771431e-15,1.5867250627915424e-16,1.391547012115887e-17,1.1265020293900666e-18,8.468010548805799e-20,5.94110980110211e-21,2.7822739795442934e-22,1.4088810179498352e-23,8.237193352643435e-25],[5.314923860460513e-10,5.593382186553814e-10,2.9432147201208205e-10,1.0324716602368767e-10,2.716411722965965e-11,5.7174587412687094e-12,1.0028344311031468e-12,1.507678161198706e-13,1.983335131252089e-14,2.3191617675404832e-15,2.4406667826044125e-16,2.335034237989879e-17,2.047809033372529e-18,1.6577672272744968e-19,1.246157574667283e-20,8.742973261432127e-22,5.750645750287094e-23,2.5346616368675485e-24,1.2121903759134083e-25],[7.386947882558896e-11,7.773963237118947e-11,4.0906275076589486e-11,1.4349809225165525e-11,3.7754053213065175e-12,7.946411058986143e-13,1.3937896142791947e-13,2.095446763273499e-14,2.7565386885782915e-15,3.223287399372143e-16,3.3921611663933335e-17,3.245347755278537e-18,2.846147753026418e-19,2.3040480787301123e-20,1.731972329087254e-21,1.215142295852366e-22,7.992536029434087e-24,4.947811309097774e-25,2.0596476074695026e-26]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.055038589430572236, "-10": 1.0880373987656156e-08, "-11": 1.0209175284446142e-09, "-12": 8.806838285273868e-11, "-13": 7.0289833073282686e-12, "-14": 5.219014358101518e-13, "-15": 3.622207665130447e-14, "-16": 2.358790420750271e-15, "-17": 1.4352637009965564e-16, "-18": 7.320672379755358e-18, "-2": 0.023013611873086714, "-3": 0.006752250669865964, "-4": 0.001583937299708909, "-5": 0.00030789246190833004, "-6": 5.0948851219872516e-05, "-7": 7.327084300266515e-06, "-8": 9.307806454883492e-07, "-9": 1.0581401550488091e-07, "0": 0.14794330180891657, "1": 0.23588051126316487, "10": 0.00010765978952142202, "11": 2.401393929380815e-05, "12": 4.924428258405341e-06, "13": 9.343107592710646e-07, "14": 1.6491128466868647e-07, "15": 2.7208103661697127e-08, "16": 4.211892990792692e-09, "17": 6.092320184172408e-10, "18": 7.386947882558896e-11, "2": 0.22330072172462684, "3": 0.15574601523549775, "4": 0.08684991915251133, "5": 0.04013225229596188, "6": 0.01578672045590227, "7": 0.005396991772089337, "8": 0.001629787403461226, "9": 0.0004404431433795231} |
| Raw goal margin distribution | {"-1": 0.09597722842897317, "-10": 2.4654610345575502e-09, "-11": 1.7910672512811482e-10, "-12": 1.1948174654536625e-11, "-13": 7.367676969414405e-13, "-14": 4.222803543283509e-14, "-15": 2.252262167474278e-15, "-16": 1.037268873112029e-16, "-2": 0.03472236892712127, "-3": 0.008350185183838026, "-4": 0.0015713675611785014, "-5": 0.0002419706553921993, "-6": 3.146916871123955e-05, "-7": 3.5382219597928597e-06, "-8": 3.5011919281467237e-07, "-9": 3.092293213431015e-08, "0": 0.23290184517100557, "1": 0.24161652738275421, "10": 1.420785753949203e-05, "11": 2.453609186004674e-06, "12": 3.8909719790893296e-07, "13": 5.703614471080662e-08, "14": 7.771118085800664e-09, "15": 9.852912316248796e-10, "16": 1.0786984799276576e-10, "2": 0.19621646050195504, "3": 0.11217220118966467, "4": 0.050179919902456925, "5": 0.018368679059780953, "6": 0.005678891107609052, "7": 0.0015178413819148487, "8": 0.00035704279956179195, "9": 7.496319235334657e-05} |
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
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.3018 |
| Totals anchor target over 2 5 | 0.7075 |
| Totals anchor reference over odds | 1.37 |
| Totals anchor reference under odds | 3.06 |
| Totals anchor reference last update utc | 2026-11-07T11:47:28Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5539 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.8, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.88, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 13.1, "draw": 7.55, "home": 1.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 4.68, "home_away": 1.11, "home_draw": 1.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 12.07, "draw": 7.26, "home": 1.19}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.37, "under": 3.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:28Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.11, "under": 6.69}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.19 |
| Reference draw odds | 7.26 |
| Reference away odds | 12.07 |
| Market reference 1x2 last update utc | 2026-11-07T11:47:01Z |
| Market reference home last update utc | 2026-11-07T11:47:01Z |
| Market reference draw last update utc | 2026-11-07T11:47:01Z |
| Market reference away last update utc | 2026-11-07T11:47:01Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.08 |
| Market reference over 2 5 last update utc | 2026-11-07T11:46:44Z |
| Market reference under 2 5 last update utc | 2026-11-07T11:46:44Z |
| Home probability edge | -6.0% |
| Draw probability edge | +3.6% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -1.5% |
| Under 2.5 probability edge | +1.5% |
| Raw edge prob home | -0.1987 |
| Raw ev home | -0.2360 |
| Raw edge prob draw | 0.1214 |
| Raw ev draw | 0.7584 |
| Raw edge prob away | 0.0773 |
| Raw ev away | 0.8458 |
| Market p home draw | 91.9% |
| Market home draw odds | 1.04 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T11:46:39Z |
| Market reference home draw last update utc | 2026-11-07T11:46:46Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.1% |
| Market draw away odds | 4.68 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T11:46:39Z |
| Market reference draw away last update utc | 2026-11-07T11:46:46Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 86.0% |
| Market home away odds | 1.11 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T11:46:39Z |
| Market reference home away last update utc | 2026-11-07T11:46:46Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.01 |
| Market reference dc draw away odds | 4.20 |
| Market reference dc home away odds | 1.08 |
| Market p over 1 5 | 88.7% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T11:47:28Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.69 |
| Market reference over 1 5 last update utc | 2026-11-07T11:47:28Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.5% |
| Market under 3 5 odds | 1.86 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T11:47:28Z |
| Market reference under 3 5 odds | 1.86 |
| Market reference under 3 5 opposite odds | 1.97 |
| Market reference under 3 5 last update utc | 2026-11-07T11:47:28Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,572.0567 |
| Elo away rating | 1,407.1890 |
| Elo rating diff | 224.8678 |
| Elo home expectancy | 0.7849 |
| Research p home | 0.6360 |
| Research p draw | 0.2134 |
| Research p away | 0.1507 |
| Research p over 1 5 | 0.7568 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.9217715417100325, 0.8084230966807031], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T11:48:24.703300+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-07T11:48:24.491829+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T11:48:24.926496+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Besiktas+JK%22+%22Genclerbirligi+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T11:47:34.417901+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T11:47:34.551350+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T11:48:24.988339+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Besiktas+JK_vs_Genclerbirligi+SK&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.9217715417100325, 0.8084230966807031], "h2h": [], "margin_distribution": {"-1": 0.10575141464855661, "-10": 2.4654610345575502e-09, "-11": 1.7910672512811482e-10, "-12": 1.1948174654536625e-11, "-13": 7.367676969414405e-13, "-14": 4.222803543283509e-14, "-15": 2.252262167474278e-15, "-16": 1.037268873112029e-16, "-2": 0.03472236892712127, "-3": 0.008350185183838026, "-4": 0.0015713675611785014, "-5": 0.0002419706553921993, "-6": 3.146916871123955e-05, "-7": 3.5382219597928597e-06, "-8": 3.5011919281467237e-07, "-9": 3.092293213431015e-08, "0": 0.21335347273183872, "1": 0.25139071360233767, "10": 1.420785753949203e-05, "11": 2.453609186004674e-06, "12": 3.8909719790893296e-07, "13": 5.703614471080662e-08, "14": 7.771118085800664e-09, "15": 9.852912316248796e-10, "16": 1.0786984799276576e-10, "2": 0.19621646050195504, "3": 0.11217220118966467, "4": 0.050179919902456925, "5": 0.018368679059780953, "6": 0.005678891107609052, "7": 0.0015178413819148487, "8": 0.00035704279956179195, "9": 7.496319235334657e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T11:48:24.988684+00:00", "p_over_1_5": 0.7567667024980858, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Çaykur Rizespor vs Erzurum BB

The model's most likely 1X2 outcome is **Çaykur Rizespor win** at **49.1%**. Expected goals are 1.42 for Çaykur Rizespor and 0.93 for Erzurum BB (2.35 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 52.7%; Under 3.5 goals: 69.4%; Double Chance 1X: 75.9%; Double Chance X2: 50.9%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 55.8%; BTTS No (at least one team does not score): 44.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çaykur Rizespor win | 49.1% | 2.04 |
| Draw | 26.8% | 3.73 |
| Erzurum BB win | 24.1% | 4.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çaykur Rizespor expected goals | 1.42 |
| Erzurum BB expected goals | 0.93 |
| Expected total goals | 2.35 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 30.6% |
| Under 3.5 | 69.4% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.74% |
| 2 | 2-1 | 9.51% |
| 3 | 1-0 | 9.10% |
| 4 | 2-0 | 8.58% |
| 5 | 0-0 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çaykur Rizespor win | 49.1% | 50.0% | 2.01 | -1.3% |
| Draw | 26.8% | 25.6% | 3.71 | -0.7% |
| Erzurum BB win | 24.1% | 24.4% | 3.90 | -6.0% |
| Over 2.5 | 52.7% | 52.7% | 1.86 | -2.0% |
| Under 2.5 | 47.3% | 47.3% | 2.04 | -3.5% |

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
| Market best home last update utc | 2026-11-07T11:46:39Z |
| Market best draw last update utc | 2026-11-07T11:47:01Z |
| Market best away last update utc | 2026-11-07T11:47:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Rizespor |
| Matched away-team name | Erzurumspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4174 |
| Dc lambda away | 0.9323 |
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
| P btts yes | 55.8% |
| P btts no | 44.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.61 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.51 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.27 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.65 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.0734599570447619,0.057316831014072034,0.03791824781199002,0.014005162304365684,0.003879620944198859,0.000859766325791148,0.00015877799781568042,2.5133526069747082e-05,3.4811647313563615e-06,4.285911567135845e-07,4.7490238012196924e-08,4.783797652817209e-09,4.4172572854067596e-10,3.7650477089353844e-11,2.9799130247321765e-12,2.201270785042485e-13],[0.0910012447175194,0.1274092327795293,0.0638785209243303,0.023593628527982174,0.006535756844336913,0.0014483950182613173,0.0002674834477078628,4.2340892936536816e-05,5.864502369296519e-06,7.22020946428189e-07,8.000385929236689e-08,8.058967280830394e-09,7.441479451610702e-10,6.342742419133651e-11,5.020074699834838e-12,3.708344399236461e-13],[0.0858277394073737,0.09510181693340114,0.0542259202614546,0.019873361515521052,0.005505192149270355,0.0012200106389336563,0.00022530638936744152,3.5664538467230524e-05,4.939781753172627e-06,6.081719593545388e-07,6.738877050930937e-08,6.788221236243883e-09,6.268099507321894e-10,5.342612432241004e-11,4.2285042856555884e-12,3.1236089346188766e-13],[0.04819622357733055,0.05340404469675193,0.029587297284782835,0.01124688237688197,0.0030914186193700876,0.0006850920917499632,0.00012651990126191513,2.0027278845017246e-05,2.773914674241925e-06,3.415165298411238e-07,3.784189438629278e-08,3.81189846841388e-09,3.5198261930907537e-10,3.000122629924368e-11,2.3744996589255186e-12,1.7540500963969793e-13],[0.020298297349625308,0.022491620680364345,0.012460971285326325,0.004602478632091529,0.0013121391754461317,0.00028853304176218534,5.3285058161020124e-05,8.434678713940363e-06,1.1682605129820886e-06,1.4383293042461378e-07,1.5937473260610013e-08,1.6054172471479728e-09,1.4824082341580217e-10,1.2635301421455814e-11,1.0000430854529542e-12,7.387348588770249e-14],[0.006839056585132169,0.007578047748284664,0.004198445133509043,0.0015507020739016174,0.0004295656211171487,9.797327482848413e-05,1.7953206696521382e-05,2.841876045485795e-06,3.936192093770625e-07,4.8461283872042105e-08,5.3697745961611304e-09,5.409093781057837e-10,4.994642467319907e-11,4.2571817676684285e-12,3.3694211544837617e-13,2.4890016212925668e-14],[0.0019202224275682513,0.0021277111926627057,0.0011788100311679235,0.00043539527180632917,0.00012061042769768136,2.6728586572044028e-05,5.080106952362549e-06,7.979220600066632e-07,1.105176458710221e-07,1.3606620006938936e-08,1.5076877171846912e-09,1.518727482645398e-10,1.4023607443580121e-11,1.1953016920905601e-12,9.460424823546902e-14,6.9884444966430415e-15],[0.0004621256654465699,0.0005120604450144716,0.0002836954522911413,0.00010478334531828002,2.902641556487357e-05,6.4325703515995746e-06,1.1879398048017898e-06,1.9352831134866886e-07,2.6597460746468204e-08,3.2746041473686362e-09,3.628440016045123e-10,3.6550085993855654e-11,3.3749574157578098e-12,2.8766437780142406e-13,2.276770156530977e-14,1.6818570167089642e-15],[9.731430674311234e-05,0.00010782956010244412,5.974051720154474e-05,2.2065250580746016e-05,6.112375310736213e-06,1.3545690515528959e-06,2.501560661971072e-07,3.9598080954321344e-08,5.644588214963718e-09,6.895653201848467e-10,7.640759886798006e-11,7.696707942970632e-12,7.106976862767859e-13,6.0576292540218e-14,4.79441688619729e-15,3.5416502882157064e-16],[1.8215486498300366e-05,2.0183752645422382e-05,1.1182349450002523e-05,4.13021771912937e-06,1.1441266312380153e-06,2.535509432822803e-07,4.682471261199064e-08,7.4120479621368415e-09,1.0266191811411128e-09,1.300813325958794e-10,1.4302127119101625e-11,1.440685180922441e-12,1.3302981382708523e-13,1.1338791548875026e-14,8.974285383164505e-16,6.629331818290003e-17],[3.0686500631514005e-06,3.4002316564966185e-06,1.8838210743991425e-06,6.957921692521344e-07,1.927439192760143e-07,4.271415524300519e-08,7.88826899173066e-09,1.2486617609260505e-09,1.729481677766369e-10,2.1292889305471915e-11,2.4281902383065335e-12,2.427032992959832e-13,2.2410707868801322e-14,1.910175904758982e-15,1.511842212413928e-16,1.1168024254935692e-17],[4.6996040783796917e-07,5.207417669480563e-07,2.885051414136114e-07,1.0655981128600429e-07,2.9518520863281372e-08,6.541626254328185e-09,1.2080797862895465e-09,1.9123118581133923e-10,2.6486823127583076e-11,3.260982756623494e-12,3.6133467720896443e-13,3.745976685512479e-14,3.4321754495340847e-15,2.9254135491776403e-16,2.315369847036391e-17,1.7103707251011366e-18],[6.59760965541238e-08,7.310511379881021e-08,4.050222688722361e-08,1.4959558892498325e-08,4.144001814046909e-09,9.183560108011262e-10,1.6959809229888253e-10,2.6846276768911207e-11,3.71839238142783e-12,4.577979540917026e-13,5.072651047683799e-14,5.109794600153013e-15,4.855906428761989e-16,4.1068856772256066e-17,3.250466678445121e-18,2.401129589229675e-19],[8.549679918542232e-09,9.473511711558894e-09,5.2485838653680216e-09,1.938572406273231e-09,5.370109925023279e-10,1.190074944366829e-10,2.1977799228563116e-11,3.478942910641786e-12,4.818573139845277e-13,5.932490976692838e-14,6.573523603442646e-15,6.621657018608977e-16,6.114297641684332e-17,5.3635376850080924e-18,4.2121997417344775e-19,3.111564718596763e-20],[1.0287939732885597e-09,1.1399598403202181e-09,6.315688423936782e-10,2.332709092456243e-10,6.461922293464091e-11,1.4320324762930641e-11,2.644616828690229e-12,4.186256718360855e-13,5.79825099109465e-14,7.13864264108147e-15,7.910005439881996e-16,7.967924996998422e-17,7.35741293778146e-18,6.271088355346911e-19,5.1081424110166993e-20,3.7441858180527985e-21],[1.1554302768311232e-10,1.2802797723117249e-10,7.093099117525264e-11,2.6198469105020804e-11,7.257333205920951e-12,1.6083042119944082e-12,2.9701479925259365e-13,4.701551413176048e-14,6.5119692783209294e-15,8.017352411793081e-16,8.88366379706141e-17,8.948712788064973e-18,8.263051580957629e-19,7.043009137475364e-20,5.574313072384699e-21,4.2378756568123865e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.14446744354538654, "-10": 5.620704140316042e-08, "-11": 5.583820095445503e-09, "-12": 5.095570620273077e-10, "-13": 4.2982912682650566e-11, "-14": 3.3507474646558227e-12, "-15": 2.201270785042485e-13, "-2": 0.06775840138532002, "-3": 0.021896291964117166, "-4": 0.005574567897429482, "-5": 0.001165837584654695, "-6": 0.00020641668173400224, "-7": 3.164569887487982e-05, "-8": 4.274538941053562e-06, "-9": 5.157481990934857e-07, "0": 0.26775738432530183, "1": 0.2207503603616484, "10": 3.6318988569201e-06, "11": 5.485546337445989e-07, "12": 7.61073755771814e-08, "13": 9.760570750037703e-09, "14": 1.1568219505197322e-09, "15": 1.1554302768311232e-10, "2": 0.15337075820577753, "3": 0.07535211374795235, "4": 0.02916631248392889, "5": 0.009273716556868391, "6": 0.002496353066184747, "7": 0.0005818638264480795, "8": 0.0001194927059751607, "9": 2.1919734483435157e-05} |
| Raw goal margin distribution | {"-1": 0.15000444569768448, "-10": 1.4695004318328076e-08, "-11": 1.233198103780227e-09, "-12": 9.499636206666978e-11, "-13": 6.738329801378356e-12, "-14": 4.10015905850599e-13, "-2": 0.06301662531063261, "-3": 0.017745437777224007, "-4": 0.0038894886595551626, "-5": 0.0006954992945808024, "-6": 0.00010484305300212308, "-7": 1.3647027331267402e-05, "-8": 1.5621008878723529e-06, "-9": 1.594989084444286e-07, "0": 0.2940799125692482, "1": 0.2343892446753251, "10": 9.696705953315244e-07, "11": 1.237179762024743e-07, "12": 1.4489466121342184e-08, "13": 1.56258310314093e-09, "14": 1.4455629745272747e-10, "2": 0.14566192449255727, "3": 0.062362435851218555, "4": 0.020781376604056365, "5": 0.005649681274318685, "6": 0.001294828839598325, "7": 0.0002562454820665411, "8": 4.459361558030704e-05, "9": 6.922560699720285e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.9% |
| Raw p btts yes | 47.2% |
| P home draw | 75.9% |
| P draw away | 50.9% |
| P home away | 73.2% |
| Raw p home draw | 76.5% |
| Raw p draw away | 53.0% |
| Raw p home away | 70.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1885 |
| Totals anchor target over 2 5 | 0.5271 |
| Totals anchor reference over odds | 1.84 |
| Totals anchor reference under odds | 2.04 |
| Totals anchor reference last update utc | 2026-11-07T11:47:01Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4266 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.85, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.77, "draw": 3.71, "home": 2.01}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.86, "under": 2.03}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.85, "home_away": 1.3, "home_draw": 1.3}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.9, "draw": 3.71, "home": 1.95}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.26, "under": 3.97}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.95 |
| Reference draw odds | 3.71 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-11-07T11:47:01Z |
| Market reference home last update utc | 2026-11-07T11:47:01Z |
| Market reference draw last update utc | 2026-11-07T11:47:01Z |
| Market reference away last update utc | 2026-11-07T11:47:01Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference under 2 5 last update utc | 2026-11-07T11:47:01Z |
| Market best over 2 5 last update utc | 2026-11-07T11:46:39Z |
| Market best under 2 5 last update utc | 2026-11-07T11:47:01Z |
| Home probability edge | -0.9% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0296 |
| Raw ev home | -0.0544 |
| Raw edge prob draw | 0.0376 |
| Raw ev draw | 0.0910 |
| Raw edge prob away | -0.0080 |
| Raw ev away | -0.0817 |
| Market p home draw | 75.3% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T11:46:39Z |
| Market reference home draw last update utc | 2026-11-07T11:47:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.7% |
| Market draw away odds | 1.85 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T11:46:39Z |
| Market reference draw away last update utc | 2026-11-07T11:47:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.0% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T11:46:39Z |
| Market reference home away last update utc | 2026-11-07T11:47:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.25 |
| Market reference dc draw away odds | 1.82 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 77.0% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market reference over 1 5 last update utc | 2026-11-07T11:47:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.7% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 2.90 |
| Market reference under 3 5 last update utc | 2026-11-07T11:47:04Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,458.4916 |
| Elo away rating | 1,419.5564 |
| Elo rating diff | 98.9351 |
| Elo home expectancy | 0.6387 |
| Research p home | 0.4826 |
| Research p draw | 0.2698 |
| Research p away | 0.2476 |
| Research p over 1 5 | 0.6804 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4174013998922623, 0.9322822304906573], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T11:48:24.703300+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-07T11:48:24.491829+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T11:48:24.704408+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87aykur+Rizespor%22+%22Erzurum+BB%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T11:47:34.417901+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T11:47:34.551350+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T11:48:24.765580+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87aykur+Rizespor_vs_Erzurum+BB&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.4174013998922623, 0.9322822304906573], "h2h": [], "margin_distribution": {"-1": 0.1621672644010763, "-10": 1.4695004318328079e-08, "-11": 1.233198103780227e-09, "-12": 9.499636206666979e-11, "-13": 6.738329801378357e-12, "-14": 4.10015905850599e-13, "-2": 0.06301662531063262, "-3": 0.017745437777224007, "-4": 0.003889488659555163, "-5": 0.0006954992945808024, "-6": 0.00010484305300212308, "-7": 1.3647027331267403e-05, "-8": 1.562100887872353e-06, "-9": 1.5949890844442863e-07, "0": 0.2697542751624647, "1": 0.2465520633787169, "10": 9.696705953315246e-07, "11": 1.237179762024743e-07, "12": 1.4489466121342186e-08, "13": 1.5625831031409303e-09, "14": 1.4455629745272747e-10, "2": 0.14566192449255727, "3": 0.06236243585121856, "4": 0.020781376604056365, "5": 0.005649681274318686, "6": 0.0012948288395983251, "7": 0.00025624548206654114, "8": 4.459361558030704e-05, "9": 6.922560699720286e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T11:48:24.765929+00:00", "p_over_1_5": 0.6804423961448135, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Çorum FK vs Fenerbahce

The model's most likely 1X2 outcome is **Fenerbahce win** at **53.8%**. Expected goals are 1.87 for Çorum FK and 2.27 for Fenerbahce (4.14 combined). The most likely exact score is 1-2 at 11.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.0%; Under 3.5 goals: 63.3%; Double Chance 1X: 46.2%; Double Chance X2: 76.3%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 80.1%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çorum FK win | 23.7% | 4.21 |
| Draw | 22.4% | 4.46 |
| Fenerbahce win | 53.8% | 1.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çorum FK expected goals | 1.87 |
| Fenerbahce expected goals | 2.27 |
| Expected total goals | 4.14 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 60.0% |
| Under 2.5 | 40.0% |
| Over 3.5 | 36.7% |
| Under 3.5 | 63.3% |
| Over 4.5 | 19.9% |
| Under 4.5 | 80.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.33% |
| 2 | 1-1 | 10.38% |
| 3 | 0-1 | 8.58% |
| 4 | 0-2 | 8.23% |
| 5 | 1-3 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çorum FK win | 23.7% | 20.2% | 4.56 | +8.3% |
| Draw | 22.4% | 22.9% | 4.11 | -7.8% |
| Fenerbahce win | 53.8% | 56.8% | 1.76 | -5.3% |
| Over 2.5 | 60.0% | 58.8% | 1.66 | -0.4% |
| Under 2.5 | 40.0% | 41.2% | 2.33 | -6.8% |

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
| Market best home last update utc | 2026-11-07T11:47:01Z |
| Market best draw last update utc | 2026-11-07T11:46:39Z |
| Market best away last update utc | 2026-11-07T11:46:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Corum |
| Matched away-team name | Fenerbahce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8740 |
| Dc lambda away | 2.2664 |
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
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.82 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.59 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.03 |
| Fair Under 4.5 odds | 1.25 |
| Score matrix json | [[0.050455169462029985,0.08578454590733839,0.08231236753826493,0.045663130659094046,0.018998859745652803,0.006323818212636725,0.001754082320459009,0.0004170362204094486,8.675722126422264e-05,1.6042977293646993e-05,2.6699726550088365e-06,4.0395777643852537e-07,5.60243171164238e-08,7.172244133724983e-09,8.526069587771053e-10,9.459745630908456e-11],[0.0426701431207096,0.10376945533260713,0.11326781434101796,0.06283579443052105,0.026143815112124554,0.00870203456245262,0.0024137450610960893,0.0005738722211441443,0.00011938425688375874,2.2076305516655513e-05,3.6740768857431698e-06,5.558753294512978e-07,7.709354182742255e-08,9.869530439269158e-09,1.1732492892727306e-09,1.301729914811269e-10],[0.034974555222324684,0.05820684300393685,0.05418400563830884,0.04323331542017662,0.017987897109808033,0.005987316758631663,0.0016607445249323218,0.00039484499197405004,8.214071741809495e-05,1.518930234532309e-05,2.5278987290428932e-06,3.824624749359323e-07,5.3043164980891946e-08,6.790596448999486e-09,8.072382477110571e-10,8.956375981072889e-11],[0.01604251198233913,0.02669895214989736,0.02221703330149458,0.01378770141732027,0.008250885624900822,0.002746328015662581,0.0007617684848733868,0.00018111182471498683,3.767720375687834e-05,6.967195531987125e-06,1.159524271088499e-06,1.754320762037399e-07,2.4330419768826145e-08,3.1147851404488257e-09,3.702728792170843e-10,4.108208612842679e-11],[0.005518916303599275,0.009184925806588097,0.007643064093716098,0.00424002181913847,0.001973491039010762,0.000944786856158027,0.0002620622328575537,6.23057662848891e-05,1.2961644305878136e-05,2.396842156276902e-06,3.988974676269064e-07,6.035182935197158e-08,8.370107529507357e-09,1.0715428177804175e-09,1.273806142168673e-10,1.4132985854686916e-11],[0.0015188861794045694,0.0025278254097429753,0.0021034826008645355,0.0011669157833147773,0.00048551356383557,0.00018078334658048814,7.212334482616606e-05,1.7147454699686395e-05,3.567233368934545e-06,6.596458842851063e-07,1.0978239517472891e-07,1.6609702786162885e-08,2.3035755476863537e-09,2.949041962287892e-10,3.505700101519662e-11,3.8896036300468046e-12],[0.0003483496727551452,0.0005797453200945606,0.000482424216898565,0.00026762685496938926,0.00011135033906662215,3.706324019439645e-05,1.1500565409072511e-05,3.932691148431593e-06,8.181288325348525e-07,1.5128679886670373e-07,2.5178095601860478e-08,3.809360180226456e-09,5.283146288933055e-10,6.763494305458081e-11,8.040164560722973e-12,8.920629932949884e-13],[6.84792182328089e-05,0.00011396739942428635,9.483583827853853e-05,5.261057850710558e-05,2.188945409057474e-05,7.285959804736464e-06,2.0209583595437507e-06,5.375097963304988e-07,1.60829267966866e-07,2.9740236680566978e-08,4.9495562598626346e-09,7.488510181333212e-10,1.038570597222866e-10,1.329580128198881e-11,1.5805503109183339e-12,1.753633810306428e-13],[1.1779049140771674e-05,1.9603430542982676e-05,1.631262780470793e-05,9.04949860047787e-06,3.765185439485841e-06,1.253251435872266e-06,3.476232416612784e-07,8.264804971693898e-08,1.9234003086007272e-08,5.115591537970299e-09,8.513687497384946e-10,1.288091945168148e-10,1.786436004461807e-11,2.2869988984694235e-12,2.7186904672999433e-13,3.01640984806418e-14],[1.8009810825821166e-06,2.997305397039148e-06,2.4941515849349244e-06,1.3836410385538356e-06,5.75685496162502e-07,1.9161836416084088e-07,5.3150545058072395e-08,1.2636637497104629e-08,2.6288353426369196e-09,5.4381093232549e-10,1.3017171371442018e-10,1.9694537293714507e-11,2.731406763677463e-12,3.496752329330834e-13,4.15679571626506e-14,4.611999668864688e-15],[2.478281174439127e-07,4.124510585573141e-07,3.4321342844309967e-07,1.9039908698613577e-07,7.921851824738005e-08,2.6368082883790112e-08,7.3139022115516025e-09,1.7388933798452626e-09,3.617468946990039e-10,6.689353500648256e-11,1.2454067222688958e-11,2.7101118099654733e-12,3.7586146948597473e-13,4.8117859500401756e-14,5.720053735844388e-15,6.34644753707217e-16],[3.100268584909094e-08,5.1596609490734355e-08,4.293515284285281e-08,2.38184558744462e-08,9.910041120373797e-09,3.2985820919772963e-09,9.149511158556208e-10,2.1753127020628465e-10,4.5253643730621294e-11,8.368216135162695e-12,1.3926908854340834e-12,2.3571602392234735e-13,4.701934220151004e-14,6.019425467972835e-15,7.155646051842225e-16,7.939249237694528e-17],[3.5551628609508816e-09,5.916724463981343e-09,4.9234915180948985e-09,2.7313275418204265e-09,1.136411545539757e-09,3.782574388644204e-10,1.0491994927500288e-10,2.4944906279967707e-11,5.189359215421814e-12,9.596062535018294e-13,1.5970367653889036e-13,2.416262276794521e-14,3.748779412431303e-15,6.90263997518344e-16,8.20557522449792e-17,9.104154450060915e-18],[3.7632023822036494e-10,6.262956851361197e-10,5.211602318746818e-10,2.891158215240783e-10,1.2029115971905483e-10,4.003921481785823e-11,1.1105961062688764e-11,2.6404621787569403e-12,5.493027949882052e-13,1.0157600876235909e-13,1.690491489430916e-14,2.5576560938842408e-15,3.547176077208918e-16,5.080032059898558e-17,8.685745615581362e-18,9.63690752137741e-19],[3.6988861672662927e-11,6.155917782481874e-11,5.122531761052214e-11,2.841745950285625e-11,1.1823528514793381e-11,3.93549118002139e-12,1.0916151080060214e-12,2.595334514662658e-13,5.3991475973524495e-14,9.983999146949879e-15,1.6615996034940394e-15,2.5139436536902147e-16,3.486551928988428e-17,4.46349066025189e-18,5.935723376944531e-19,9.472204868549748e-20],[3.3932912245757976e-12,5.6473275591349115e-12,4.699317926086878e-12,2.6069663026977397e-12,1.0846691068198448e-12,3.6103483810186204e-13,1.0014279431985882e-13,2.3809129114000824e-14,4.95308028790349e-15,9.159140119349947e-16,1.5243214033434277e-16,2.3062464086180898e-17,3.198499637367325e-18,4.0947255480431696e-19,4.867641747061968e-20,6.041633921524394e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2515575702633554, "-10": 3.2821372047993223e-06, "-11": 4.882263205800193e-07, "-12": 6.674216788953244e-08, "-13": 8.435057182808443e-09, "-14": 9.827799502582321e-10, "-15": 9.459745630908456e-11, "-2": 0.16616244552232834, "-3": 0.07862206038232206, "-4": 0.029556397893109352, "-5": 0.009172596009561636, "-6": 0.0024174785036105598, "-7": 0.0005528320285601761, "-8": 0.00011154553081337846, "-9": 2.012495456597671e-05, "0": 0.22436266410157046, "1": 0.12785872435286486, "10": 3.0464951883761893e-07, "11": 3.747007267355664e-08, "12": 4.235290830000222e-09, "13": 4.4257873397127056e-10, "14": 4.2636189231797836e-11, "15": 3.3932912245757976e-12, "2": 0.07060248417828086, "3": 0.02762174488595645, "4": 0.008585740849277669, "5": 0.002203119830412654, "6": 0.00048009596573835153, "7": 9.077749911671947e-05, "8": 1.5144563988312962e-05, "9": 2.2592229483177976e-06} |
| Raw goal margin distribution | {"-1": 0.18429353221795947, "-10": 2.2941203573675975e-05, "-11": 4.583168686872685e-06, "-12": 8.431813690125107e-07, "-13": 1.4371222829787961e-07, "-14": 2.280880996659311e-08, "-15": 3.3805996822974986e-09, "-16": 4.608851139284503e-10, "-17": 4.9162576818540707e-11, "-2": 0.13992325713613293, "-3": 0.08144530780499273, "-4": 0.03884374654021338, "-5": 0.015590503869202342, "-6": 0.005381422297057934, "-7": 0.0016256725322277682, "-8": 0.0004359635759943746, "-9": 0.00010501065088272573, "0": 0.21292975824812782, "1": 0.15125118774886065, "10": 3.4261945566821907e-06, "11": 5.659541466995593e-07, "12": 8.609065027597792e-08, "13": 1.213244390322438e-08, "14": 1.5921235918885629e-09, "15": 1.9511357183353247e-10, "16": 2.1994089925655522e-11, "17": 1.9398472589270387e-12, "2": 0.09565971232848945, "3": 0.046038886963142456, "4": 0.018155133236654818, "5": 0.0060250140276903105, "6": 0.001719549044081102, "7": 0.0004295068981579789, "8": 9.523725379613052e-05, "9": 1.8967478051733243e-05} |
| Research history json | {"away": [{"away": "Goztep", "away_goals": 2.0, "away_xg": 1.4, "date": "2026-10-31T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 1.51, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 3.0, "away_xg": 0.96, "date": "2026-10-10T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.52, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 0.0, "away_xg": 1.33, "date": "2026-09-14T00:00:00+00:00", "home": "Gaziantep", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 2.0, "away_xg": 1.75, "date": "2026-09-05T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Konyaspor", "away_goals": 2.0, "away_xg": 2.15, "date": "2026-08-22T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 4.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 2.9, "date": "2026-08-15T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 2.0, "home_xg": 1.19, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 46.8% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.7% |
| Raw p btts yes | 76.5% |
| P home draw | 46.2% |
| P draw away | 76.3% |
| P home away | 77.6% |
| Raw p home draw | 53.2% |
| Raw p draw away | 68.1% |
| Raw p home away | 78.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7343 |
| Totals anchor target over 2 5 | 0.6000 |
| Totals anchor reference over odds | 1.61 |
| Totals anchor reference under odds | 2.35 |
| Totals anchor reference last update utc | 2026-11-07T11:47:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7791 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.94, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 2.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.57, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.03, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.76, "draw": 4.11, "home": 4.54}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.66, "under": 2.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T11:46:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.23, "home_away": 1.26, "home_draw": 2.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.71, "draw": 4.05, "home": 4.56}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.61, "under": 2.35}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T11:47:01Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.19, "under": 4.79}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.56 |
| Reference draw odds | 4.05 |
| Reference away odds | 1.71 |
| Market reference 1x2 last update utc | 2026-11-07T11:47:01Z |
| Market reference home last update utc | 2026-11-07T11:47:01Z |
| Market reference draw last update utc | 2026-11-07T11:47:01Z |
| Market reference away last update utc | 2026-11-07T11:47:01Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-11-07T11:46:39Z |
| Market reference under 2 5 last update utc | 2026-11-07T11:46:39Z |
| Market best over 2 5 last update utc | 2026-11-07T11:46:39Z |
| Market best under 2 5 last update utc | 2026-11-07T11:46:39Z |
| Home probability edge | +3.5% |
| Draw probability edge | -0.5% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | 0.1171 |
| Raw ev home | 0.4565 |
| Raw edge prob draw | -0.0163 |
| Raw ev draw | -0.1249 |
| Raw edge prob away | -0.1007 |
| Raw ev away | -0.1769 |
| Market p home draw | 46.5% |
| Market home draw odds | 2.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T11:46:39Z |
| Market reference home draw last update utc | 2026-11-07T11:47:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 78.0% |
| Market draw away odds | 1.23 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T11:46:39Z |
| Market reference draw away last update utc | 2026-11-07T11:47:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.5% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T11:46:39Z |
| Market reference home away last update utc | 2026-11-07T11:47:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.03 |
| Market reference dc draw away odds | 1.21 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-11-07T11:47:04Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T11:47:01Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.35 |
| Market reference under 3 5 last update utc | 2026-11-07T11:47:04Z |
| Market under 3 5 bookmakers | 1 |
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
| Team research json | {"base_rates": [1.8739786655562845, 2.266444351085081], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T11:48:24.703300+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-07T11:48:24.491829+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T11:48:24.771420+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87orum+FK%22+%22Fenerbahce%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T11:47:34.417901+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T11:47:34.551350+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T11:48:24.832814+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87orum+FK_vs_Fenerbahce&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 1.0089728918892988, "goals_for": 2.3331960885564245, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.4847509690034097, "results": "LLWWWDLWWL", "xg_against": 1.3380003484001706, "xg_for": 1.9676008712062978, "xg_matches": 10}, "venue": {"goals_against": 0.8151944568095735, "goals_for": 1.425370020202056, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.384791003310632, "results": "LWDWL", "xg_against": 1.2819506533747527, "xg_for": 1.2552734770676013, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.8739786655562845, 2.266444351085081], "h2h": [], "margin_distribution": {"-1": 0.19081575212796928, "-10": 2.2941203573675975e-05, "-11": 4.583168686872685e-06, "-12": 8.431813690125107e-07, "-13": 1.4371222829787961e-07, "-14": 2.280880996659311e-08, "-15": 3.3805996822974986e-09, "-16": 4.608851139284503e-10, "-17": 4.9162576818540707e-11, "-2": 0.13992325713613293, "-3": 0.08144530780499273, "-4": 0.03884374654021338, "-5": 0.015590503869202342, "-6": 0.005381422297057934, "-7": 0.0016256725322277682, "-8": 0.0004359635759943746, "-9": 0.00010501065088272573, "0": 0.19988531842810822, "1": 0.15777340765887046, "10": 3.4261945566821907e-06, "11": 5.659541466995593e-07, "12": 8.609065027597792e-08, "13": 1.213244390322438e-08, "14": 1.5921235918885629e-09, "15": 1.9511357183353247e-10, "16": 2.1994089925655522e-11, "17": 1.9398472589270387e-12, "2": 0.09565971232848945, "3": 0.046038886963142456, "4": 0.018155133236654818, "5": 0.0060250140276903105, "6": 0.001719549044081102, "7": 0.0004295068981579789, "8": 9.523725379613052e-05, "9": 1.8967478051733243e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T11:48:24.833171+00:00", "p_over_1_5": 0.9181844243029651, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
