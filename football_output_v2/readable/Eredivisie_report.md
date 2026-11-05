# Eredivisie — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Eredivisie |
| Training matches | 1,629 |
| Training data through | 2026-11-01 |
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
| Training sha256 | 615de97a97f0d322c268f8b3f3257e878336d0e9922ced304f9c92ec61ef9060 |
| Training as of utc | 2026-11-05T12:31:14.696351+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1629, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1323, 'tuning_matches': 189, 'audit_matches': 114, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6639999435984515, 'audit_candidate_poisson_score': 0.6541517901162848, 'audit_gain': 0.009848153482166722, 'audit_gain_lower95': -0.0021828454332282108, 'audit_baseline_briers': [0.6216633755590796, 0.09847259899912482, 0.27967453202176307, 0.2302451960138092], 'audit_candidate_briers': [0.6176749252028129, 0.0975895815214795, 0.2767941288032132, 0.2243749218030424], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1636.735 |
| Base scoring parameter | 0.290 |
| Home-advantage parameter | 0.183 |
| Dixon-Coles low-score adjustment | -0.081 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1629, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-01'} |
| Training data health | {'training_end': '2026-11-01', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 5.00 |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 4} |
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

## 2026-11-06 — Willem II vs FC Zwolle

The model's most likely 1X2 outcome is **FC Zwolle win** at **43.4%**. Expected goals are 1.22 for Willem II and 1.64 for FC Zwolle (2.86 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 61.3%; Under 3.5 goals: 61.0%; Double Chance 1X: 56.6%; Double Chance X2: 68.3%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 63.3%; BTTS No (at least one team does not score): 36.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Willem II win | 31.7% | 3.15 |
| Draw | 24.9% | 4.01 |
| FC Zwolle win | 43.4% | 2.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Willem II expected goals | 1.22 |
| FC Zwolle expected goals | 1.64 |
| Expected total goals | 2.86 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 83.3% |
| Under 1.5 | 16.7% |
| Over 2.5 | 61.3% |
| Under 2.5 | 38.7% |
| Over 3.5 | 39.0% |
| Under 3.5 | 61.0% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.30% |
| 2 | 1-2 | 8.52% |
| 3 | 2-1 | 7.97% |
| 4 | 2-2 | 6.46% |
| 5 | 0-2 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Willem II win | 31.7% | 33.6% | 2.84 | -9.9% |
| Draw | 24.9% | 24.4% | 3.86 | -3.8% |
| FC Zwolle win | 43.4% | 42.1% | 2.42 | +4.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:00:00+00:00 |
| Fixture id | 926c11a6b5d1773d9024296a215d0f71 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:31:02Z |
| Market best draw last update utc | 2026-11-05T12:31:02Z |
| Market best away last update utc | 2026-11-05T12:30:40Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Willem II |
| Matched away-team name | Zwolle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2184 |
| Dc lambda away | 1.6439 |
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
| P btts yes | 63.3% |
| P btts no | 36.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.69 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.98 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.56 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.68 |
| Fair Under 4.5 odds | 1.27 |
| Score matrix json | [[0.05079714546108439,0.06143529137720178,0.06296598400202161,0.03831395800950715,0.01748514775422804,0.006383686945866001,0.0019421940073381216,0.0005064853041995319,0.00011557107173678655,2.3441149798674433e-05,4.279087716879683e-06,7.101184279475939e-07,1.0802438833199146e-07,1.5168783141050585e-08,1.9778574422802745e-09,2.406999531362348e-10,2.7461755869613572e-11],[0.05501235445970776,0.11302127209674023,0.08518836529209534,0.051835979416999245,0.023656124456430557,0.0086366609539105,0.002627646263098601,0.000685237526151302,0.00015635919667349643,3.1714159058517864e-05,5.789292319020391e-06,9.607382303229925e-07,1.4614908667806082e-07,2.052225276452293e-08,2.6758962789059525e-09,3.256494098925137e-10,3.7153744639452844e-11],[0.04366226381622045,0.07970370838964337,0.06455937006365634,0.035065142075021746,0.016002502013825238,0.0058423848996156606,0.0017775064843905729,0.0004635380961230963,0.00010577127137862834,2.145346737312875e-05,3.916244275953797e-06,6.499042348977555e-07,9.886450581505265e-08,1.3882552562545218e-08,1.8101458533855375e-09,2.2028990197459685e-10,2.5133147845456682e-11],[0.019690615170547775,0.035944426889358685,0.03280755357854343,0.017715905028375764,0.007216737781770485,0.00263477297514322,0.0008016120349281004,0.0002090443662304444,4.770026147939732e-05,9.674990098915758e-06,1.7661305716131758e-06,2.930909455575897e-07,4.458547880669869e-08,6.260692327923421e-09,8.163315936068375e-10,9.934536843982999e-11,1.1334436169695803e-11],[0.006659990090525869,0.012157544333649219,0.011096554365366605,0.006752104723579307,0.002734575569728198,0.000891163722070297,0.00027113059509957955,7.070542974489964e-05,1.6133740160818015e-05,3.2723882736327085e-06,5.973613319665179e-07,9.913264649832178e-08,1.5080221946448408e-08,2.117564560713589e-09,2.761092163406231e-10,3.360175208434095e-11,3.833665526345872e-12],[0.0018020957749353592,0.003289653434833962,0.0030025650888902025,0.001827020645510086,0.0008337881961670995,0.00027014472374565064,7.336396800045118e-05,1.9131853722955262e-05,4.36555378949811e-06,8.854603387849608e-07,1.6163722735533684e-07,2.6823842225669196e-08,4.080487190730392e-09,5.729819558505522e-10,7.471110999038463e-11,9.092141975970261e-12,1.0373337427890578e-12],[0.00040635060236546684,0.0007417766987808163,0.0006770417807321145,0.00041197085646782434,0.00018800906171031334,6.864059771267461e-05,1.8532779459727677e-05,4.313999507029382e-06,9.84379097212541e-07,1.996604992034374e-07,3.644722195904434e-08,6.048449032376151e-09,9.201000584762719e-10,1.2920043770302209e-10,1.6846443441150853e-11,2.050167044457105e-12,2.3390609816588565e-13],[7.85375153621743e-05,0.00014336707891331087,0.00013085542126810718,7.962377139411747e-05,3.633749891435268e-05,1.3266528869273167e-05,4.036252574190906e-06,9.340949978448476e-07,1.90256118778928e-07,3.858943344030335e-08,7.044346034812926e-09,1.169015515252845e-09,1.7783257132304126e-10,2.4971247247652843e-11,3.2560006133999158e-12,3.9624655362085164e-13,4.52082602340709e-14],[1.3281938362925555e-05,2.424564485670484e-05,2.2129725287626427e-05,1.3465641470874571e-05,6.145246874919025e-06,2.243580254851348e-06,6.825942692531732e-07,1.780069163025497e-07,3.604604671368048e-08,6.526084687690297e-09,1.1913105400653725e-09,1.9769904799369362e-10,3.007430576764564e-11,4.223033607050405e-12,5.50641298714345e-13,6.701157118918212e-14,7.645433181264378e-15],[1.9966099950299625e-06,3.6447313286718824e-06,3.3266553035569064e-06,2.024225200840049e-06,9.237854443474006e-07,3.3726664279605797e-07,1.0261111769237759e-07,2.6758924681220097e-08,6.10591773994341e-09,1.0990544045793374e-09,1.7908399109263332e-10,2.9719148248266074e-11,4.520925925757898e-12,6.348283570356103e-13,8.277526146019376e-14,1.0073527610431725e-14,1.149301245716957e-15],[2.7012671095078885e-07,4.9310545803346e-07,4.500721011382795e-07,2.7386284606795067e-07,1.2498140564603932e-07,4.5629706932598275e-08,1.388253279219425e-08,3.6202865510594606e-09,8.260859559616877e-10,1.675540803530972e-10,2.714349456943654e-11,4.020783121664449e-12,6.116481705576177e-13,8.588762779470561e-14,1.1198886703959518e-14,1.3628745162307202e-15,1.554920420963369e-16],[3.322378711494484e-08,6.064868855529669e-08,5.5355872145936175e-08,3.3683306861542095e-08,1.5371880847677604e-08,5.612150179114083e-09,1.7074591123575652e-09,4.452711442127977e-10,1.016030730278903e-10,2.060803641482833e-11,3.761914251180963e-12,5.540219331108484e-13,7.52286530137105e-14,1.0563606433496192e-14,1.3773885095151522e-15,1.6762449234382408e-16,1.9124486010633276e-17],[3.7457792462512655e-09,6.8377695208803456e-09,6.2410367705828125e-09,3.797587293422155e-09,1.733085757378255e-09,6.327356840760253e-10,1.9250559500529097e-10,5.0201604205337474e-11,1.1455126442585112e-11,2.323430343494195e-12,4.241328744221312e-13,7.038522927152388e-14,9.501912678352576e-15,1.1909821600788355e-15,1.552921488184592e-16,1.8898638569185372e-17,2.156169088912479e-18],[3.8982807792141487e-10,7.116154942291584e-10,6.49512747166834e-10,3.952198082188428e-10,1.8036447031625877e-10,6.584961882163805e-11,2.0034305589453565e-11,5.2245457058164226e-12,1.1921497851024677e-12,2.418023928919697e-13,4.414005533954879e-14,7.325081601761781e-15,1.1143035138508434e-15,1.3885799788974212e-16,1.6161454242337228e-17,1.96680569366977e-18,2.2439529837363436e-19],[3.767206013739843e-11,6.876883224073349e-11,6.276737017441933e-11,3.819310415529568e-11,1.7429994290390376e-11,6.363550859396004e-12,1.936067737863301e-12,5.048876958005566e-13,1.1520652549357998e-13,2.3367209296374594e-14,4.2655901752535856e-15,7.07878498861104e-16,1.0768364661912752e-16,1.5120936194362414e-17,1.749691155627979e-18,1.9006743374047493e-19,2.1685029000361378e-20],[3.3978359068577316e-12,6.2026129340421145e-12,5.661310355202712e-12,3.444831533500065e-12,1.5721003905868046e-12,5.739612202335032e-13,1.7462385794213807e-13,4.553840526546436e-14,1.0391066153501841e-14,2.107608198242924e-15,3.8473540890925953e-16,6.384718468674945e-17,9.712539206227723e-18,1.3638346233022714e-18,1.778303793161807e-19,1.9205492439923422e-20,1.955883748060068e-21],[2.8731394718883247e-13,5.24480067259105e-13,4.787086454444274e-13,2.912877997706978e-13,1.3293354387272721e-13,4.853296870098421e-14,1.476583074463294e-14,3.8506329687960116e-15,8.786469723382955e-16,1.7821497187152779e-16,3.253242710571461e-17,5.398785330457229e-18,8.212721429353054e-19,1.1532302314626662e-19,1.503696753227538e-20,1.829958672934971e-21,1.8528149686219257e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1898745751810518, "-10": 5.345236580610066e-06, "-11": 8.710010378676339e-07, "-12": 1.3045996598386611e-07, "-13": 1.807630375810083e-08, "-14": 2.328640000018245e-09, "-15": 2.7785369777568767e-10, "-16": 2.7461755869613572e-11, "-2": 0.1337305250469946, "-3": 0.06868935729116835, "-4": 0.02812541640621714, "-5": 0.00952601182265688, "-6": 0.0027435029257733357, "-7": 0.0006861674444760584, "-8": 0.00015151023647105353, "-9": 2.9927126202445287e-05, "0": 0.24911791699059643, "1": 0.17518237048214938, "10": 3.3742967480622857e-07, "11": 4.075088312050661e-08, "12": 4.523739875732217e-09, "13": 4.6454950831712183e-10, "14": 4.435338171688498e-11, "15": 3.922315974116836e-12, "16": 2.8731394718883247e-13, "2": 0.09273225150735491, "3": 0.03530138286409982, "4": 0.010712805930508974, "5": 0.002689164710483061, "6": 0.0005740024231705566, "7": 0.00010639970353479833, "8": 1.7412226017458247e-05, "9": 2.549055818998447e-06} |
| Raw goal margin distribution | {"-1": 0.21593913501876758, "-10": 2.719603560117585e-06, "-11": 4.004437247836281e-07, "-12": 5.417028836055219e-08, "-13": 6.774038677091237e-09, "-14": 7.822657072729001e-10, "-15": 7.563398678380736e-11, "-2": 0.1435331208902817, "-3": 0.0682429053555383, "-4": 0.025633753505936507, "-5": 0.00792245857907129, "-6": 0.002075054216054466, "-7": 0.0004709281132672504, "-8": 9.420790347797939e-05, "-9": 1.6839917796164398e-05, "0": 0.26188206602633773, "1": 0.15764509371275098, "10": 1.359958668186302e-07, "11": 1.4841015262461841e-08, "12": 1.4879395157039439e-09, "13": 1.37903031403784e-10, "14": 1.1802729233333568e-11, "15": 8.457600284581478e-13, "2": 0.07884173079239602, "3": 0.027782002153361126, "4": 0.007734286351876569, "5": 0.0017716177851807469, "6": 0.00034390739407347243, "7": 5.784538200931397e-05, "8": 8.576368357348036e-06, "9": 1.1362085808080525e-06} |
| Research history json | {"away": [{"away": "Den Haag", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-11-01T00:00:00+00:00", "home": "Zwolle", "home_goals": 1.0, "home_xg": 1.44, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 1.0, "away_xg": 0.91, "date": "2026-10-24T00:00:00+00:00", "home": "Utrecht", "home_goals": 1.0, "home_xg": 1.63, "source": "pipeline training history"}, {"away": "Go Ahead Eagles", "away_goals": 1.0, "away_xg": 2.74, "date": "2026-10-18T00:00:00+00:00", "home": "Zwolle", "home_goals": 4.0, "home_xg": 1.77, "source": "pipeline training history"}, {"away": "Cambuur", "away_goals": 1.0, "away_xg": 0.82, "date": "2026-10-11T00:00:00+00:00", "home": "Zwolle", "home_goals": 0.0, "home_xg": 0.98, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-09-18T00:00:00+00:00", "home": "Groningen", "home_goals": 3.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Feyenoord", "away_goals": 7.0, "away_xg": 3.33, "date": "2026-09-13T00:00:00+00:00", "home": "Zwolle", "home_goals": 0.0, "home_xg": 0.22, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 2.0, "away_xg": 1.08, "date": "2026-09-04T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 2.0, "home_xg": 2.23, "source": "pipeline training history"}, {"away": "Nijmegen", "away_goals": 3.0, "away_xg": 1.97, "date": "2026-08-29T00:00:00+00:00", "home": "Zwolle", "home_goals": 1.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 2.0, "away_xg": 1.55, "date": "2026-08-22T00:00:00+00:00", "home": "Heerenveen", "home_goals": 0.0, "home_xg": 0.85, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 1.0, "away_xg": 0.68, "date": "2026-08-16T00:00:00+00:00", "home": "Twente", "home_goals": 3.0, "home_xg": 2.08, "source": "pipeline training history"}], "h2h": [{"away": "Zwolle", "away_goals": 2.0, "away_xg": null, "date": "2025-05-14T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": null, "date": "2024-12-13T00:00:00+00:00", "home": "Zwolle", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Willem II", "away_goals": 0.0, "away_xg": 1.22, "date": "2026-10-31T00:00:00+00:00", "home": "PSV Eindhoven", "home_goals": 7.0, "home_xg": 2.57, "source": "pipeline training history"}, {"away": "Cambuur", "away_goals": 6.0, "away_xg": 1.91, "date": "2026-10-24T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": 1.04, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 2.0, "away_xg": 1.17, "date": "2026-10-17T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 3.0, "home_xg": 3.38, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-10-11T00:00:00+00:00", "home": "Utrecht", "home_goals": 3.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "For Sittard", "away_goals": 1.0, "away_xg": 1.31, "date": "2026-09-19T00:00:00+00:00", "home": "Willem II", "home_goals": 0.0, "home_xg": 1.01, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 1.58, "date": "2026-09-15T00:00:00+00:00", "home": "Ajax", "home_goals": 5.0, "home_xg": 3.78, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 0.92, "date": "2026-09-11T00:00:00+00:00", "home": "AZ Alkmaar", "home_goals": 1.0, "home_xg": 2.49, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 3.0, "away_xg": 1.59, "date": "2026-09-05T00:00:00+00:00", "home": "Willem II", "home_goals": 0.0, "home_xg": 0.85, "source": "pipeline training history"}, {"away": "Heerenveen", "away_goals": 2.0, "away_xg": 1.36, "date": "2026-08-30T00:00:00+00:00", "home": "Willem II", "home_goals": 2.0, "home_xg": 1.7, "source": "pipeline training history"}, {"away": "Nijmegen", "away_goals": 4.0, "away_xg": 2.99, "date": "2026-08-15T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": 1.43, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 27.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 46.4% |
| Raw p over 1 5 | 78.9% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 57.7% |
| P home draw | 56.6% |
| P draw away | 68.3% |
| P home away | 75.1% |
| Raw p home draw | 53.6% |
| Raw p draw away | 72.6% |
| Raw p home away | 73.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1104 |
| Totals anchor target over 2 5 | 0.6131 |
| Totals anchor reference over odds | 1.58 |
| Totals anchor reference under odds | 2.43 |
| Totals anchor reference last update utc | 2026-11-05T12:31:02Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5490 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.0, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.9, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.28, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.96, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.28, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.13, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 4.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.92, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.53, "under": 2.44}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:18:34Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.15, "under": 4.87}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.42, "draw": 3.69, "home": 2.8}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.45, "home_away": 1.29, "home_draw": 1.58}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.29, "draw": 3.86, "home": 2.84}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.58, "under": 2.43}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.17, "under": 5.07}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.84 |
| Reference draw odds | 3.86 |
| Reference away odds | 2.29 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:02Z |
| Market reference home last update utc | 2026-11-05T12:31:02Z |
| Market reference draw last update utc | 2026-11-05T12:31:02Z |
| Market reference away last update utc | 2026-11-05T12:31:02Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-05T12:31:02Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:31:02Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.5% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.0616 |
| Raw ev home | -0.2213 |
| Raw edge prob draw | 0.0182 |
| Raw ev draw | 0.0109 |
| Raw edge prob away | 0.0434 |
| Raw ev away | 0.1227 |
| Market p home draw | 60.2% |
| Market home draw odds | 1.58 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T12:30:40Z |
| Market reference home draw last update utc | 2026-11-05T12:31:07Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 65.7% |
| Market draw away odds | 1.45 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T12:30:40Z |
| Market reference draw away last update utc | 2026-11-05T12:31:07Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T12:30:40Z |
| Market reference home away last update utc | 2026-11-05T12:31:07Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home draw odds | 1.55 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T12:31:02Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-11-05T12:31:04Z |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 61.5% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-05T12:18:34Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.39 |
| Market reference under 3 5 last update utc | 2026-11-05T12:31:04Z |
| Market under 3 5 bookmakers | 2 |
| Elo home rating | 1,319.6939 |
| Elo away rating | 1,410.7310 |
| Elo rating diff | -31.0371 |
| Elo home expectancy | 0.4555 |

</details>


---

## 2026-11-07 — ADO Den Haag vs Sparta Rotterdam

The model's most likely 1X2 outcome is **Sparta Rotterdam win** at **37.1%**. Expected goals are 1.37 for ADO Den Haag and 1.51 for Sparta Rotterdam (2.88 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 55.1%; Under 3.5 goals: 67.4%; Double Chance 1X: 62.9%; Double Chance X2: 63.3%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 83.4%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ADO Den Haag win | 36.7% | 2.73 |
| Draw | 26.3% | 3.81 |
| Sparta Rotterdam win | 37.1% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ADO Den Haag expected goals | 1.37 |
| Sparta Rotterdam expected goals | 1.51 |
| Expected total goals | 2.88 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 79.2% |
| Under 1.5 | 20.8% |
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 32.6% |
| Under 3.5 | 67.4% |
| Over 4.5 | 16.6% |
| Under 4.5 | 83.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.35% |
| 2 | 2-1 | 8.71% |
| 3 | 1-2 | 8.15% |
| 4 | 1-0 | 7.39% |
| 5 | 0-1 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ADO Den Haag win | 36.7% | 38.1% | 2.52 | -7.6% |
| Draw | 26.3% | 26.1% | 3.65 | -4.2% |
| Sparta Rotterdam win | 37.1% | 35.8% | 2.71 | +0.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T17:45:00+00:00 |
| Fixture id | da066424422bbd4438e5000312b822fd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:31:02Z |
| Market best draw last update utc | 2026-11-05T12:30:40Z |
| Market best away last update utc | 2026-11-05T12:30:40Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Den Haag |
| Matched away-team name | Sparta Rotterdam |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3675 |
| Dc lambda away | 1.5135 |
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
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.52 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.80 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.07 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.04 |
| Fair Under 4.5 odds | 1.20 |
| Score matrix json | [[0.06444896122639328,0.07007810613388857,0.059627935436367734,0.030081790702286018,0.011382007341447682,0.003445276044977578,0.0008690563587197746,0.00018789925968315025,3.5547597121664604e-05,5.977821014918133e-06,9.047280908378622e-07,1.244802801903307e-07,1.5699812964526973e-08,1.8277899865134282e-09,1.9759385100643905e-10,1.9936886382315e-11],[0.07389712411290447,0.12350262985263265,0.08154283731913908,0.04113767393678392,0.015565207250875972,0.004711509496332261,0.0011884584089931181,0.0002569573917426769,4.861231414378761e-05,8.174834211098645e-06,1.237240481149569e-06,1.702301976870073e-07,2.1469924878977467e-08,2.4995529433157737e-09,2.7021501130245665e-10,2.72642390018376e-11],[0.05757851867895837,0.08714363168064777,0.059120751175332074,0.028128448762868144,0.010642923936644847,0.003221559237087713,0.000812624737011958,0.0001756981408083761,3.323933652007746e-05,5.589655010761812e-06,8.459801479014476e-07,1.1639723239797361e-07,1.468035559883576e-08,1.709103606688527e-09,1.8476322001236618e-10,1.8642297350119336e-11],[0.026246734562447558,0.03972376889865197,0.030060459745175256,0.013595921480706883,0.0048514968071854915,0.0014685235416440543,0.0003704288727911655,8.009067566717763e-05,1.5151901484974515e-05,2.5480021843065292e-06,3.8563368590418053e-07,5.3058802703612775e-08,6.691929655803947e-09,7.790820211022326e-10,8.422292382349637e-11,8.49795099646446e-12],[0.008973282367239795,0.013580835900576214,0.0102771258169553,0.005184723327820485,0.0017587328635804678,0.0005020615562960263,0.00012664291112576072,2.7381548970775597e-05,5.180160225333476e-06,8.711157198518245e-07,1.3184116087677552e-07,1.813984202851577e-08,2.287849341424322e-09,2.663540085703632e-10,2.8794289646379716e-11,2.905295272172384e-12],[0.0024542419553377913,0.003714433123985648,0.0028108502917885323,0.001418050273823013,0.0005365458056314739,0.00014560325502684248,3.463753096254831e-05,7.489003860120918e-06,1.4168022402593969e-06,2.3825492836600234e-07,3.6059280787321626e-08,4.961346310923851e-09,6.257393461410348e-10,7.284928257605539e-11,7.875396185268089e-12,7.946141955413902e-13],[0.0005593738657374796,0.0008465981974875096,0.000640652479396909,0.00032320377449064305,0.00012229018446553263,3.701662021783587e-05,8.371047319787239e-06,1.7069030340091993e-06,3.229193211352876e-07,5.4303358322612425e-08,8.218675932031783e-09,1.1307961952031274e-09,1.426192866737045e-10,1.6603898699613533e-11,1.7949700512561265e-12,1.811094514797698e-13],[0.00010927987216683343,0.00016539232249639186,0.00012515854840582734,6.314143245432108e-05,2.389074024406369e-05,7.231606217641511e-06,1.8241421834283575e-06,3.53585893787428e-07,6.308586134488124e-08,1.0608761723076014e-08,1.6056092539270846e-09,2.209135449966368e-10,2.7862255230103663e-11,3.24375527443102e-12,3.5066725451314037e-13,3.538173468261921e-14],[1.8680402845462054e-05,2.8272317221074427e-05,2.1394718509596745e-05,1.0793455108416856e-05,4.0839053266284045e-06,1.2361774834349718e-06,3.118205590670929e-07,6.741893274793387e-08,1.1434736740442137e-08,1.813471582177827e-09,2.744643371285234e-10,3.776316656242171e-11,4.7627997870168095e-12,5.544905393552822e-13,5.994338618018395e-14,6.048186588592852e-15],[2.838440366613144e-06,4.295907701877221e-06,3.2508738249569973e-06,1.6400384364515815e-06,6.205391729731606e-07,1.8783406858554207e-07,4.738035198266211e-08,1.0244137761311699e-08,1.938030424451932e-09,2.9218126515068425e-10,4.17041677391112e-11,5.738018458630421e-12,7.236954837325197e-13,8.425344693213962e-14,9.10824720713383e-15,9.190067848049968e-16],[3.8816450605070963e-07,5.874771620191941e-07,4.445659127950236e-07,2.2427975485319403e-07,8.486043405930449e-08,2.5686824112848853e-08,6.4793930991770554e-09,1.400913938797901e-09,2.6503097661207975e-10,4.4568631071561365e-11,6.047328753667491e-12,7.846897637528186e-13,9.896734251611247e-14,1.152188997738453e-14,1.2455777897364994e-15,1.256766986817945e-16],[4.825687358895826e-08,7.30355576103514e-08,5.526873457334257e-08,2.78826106194759e-08,1.0549906483641766e-08,3.1934033246038624e-09,8.055225267796843e-10,1.7416256715844131e-10,3.2948830035110065e-11,5.540802319963491e-12,8.385864167127824e-13,1.034402168744208e-13,1.230368687190389e-14,1.4324091447760902e-15,1.5485107218091663e-16,1.562421207201427e-17],[5.499383194299857e-09,8.323177368054524e-09,6.298459213744124e-09,3.1775195707878973e-09,1.202273875256805e-09,3.639222201905368e-10,9.179784592211459e-11,1.9847673992838302e-11,3.754869072338473e-12,6.314332631842315e-13,9.556582729167158e-14,1.3148769313519573e-14,1.486750674058082e-15,1.6323823306998266e-16,1.7646924067743577e-17,1.780544882059507e-18],[5.785044129021745e-10,8.755517967501918e-10,6.625627494756207e-10,3.342573210190438e-10,1.2647250023856703e-10,3.828258604557664e-11,9.656620949036847e-12,2.087864508623768e-12,3.949912656512476e-13,6.64232544449567e-14,1.0052991555158868e-14,1.3831771315714236e-15,1.7445030031486932e-16,1.8208017125942374e-17,1.8563579017226435e-18,1.8730338207918713e-19],[5.650861808367692e-11,8.552436419080554e-11,6.471948101270575e-11,3.265043251853671e-11,1.2353900946434874e-11,3.739463322764324e-12,9.432638593894915e-13,2.0394371330099983e-13,3.8582956463720046e-14,6.488258747197613e-15,9.819815505624582e-16,1.35109476309669e-16,1.704039792129067e-17,1.9838624037823208e-18,1.9227277554490993e-19,1.8295893769584098e-20],[5.151805685042755e-12,7.797127599110979e-12,5.900377703814112e-12,2.976690805268357e-12,1.1262865609994936e-12,3.409212445559876e-13,8.599594677934396e-14,1.859324147791043e-14,3.517550086983411e-15,5.915247874287792e-16,8.952578042704091e-17,1.2317727662789292e-17,1.553547438663249e-18,1.8086575033588789e-19,1.9552552748255615e-20,1.7686687041127507e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1851393599552081, "-10": 1.0904473150486495e-06, "-11": 1.4774643689509235e-07, "-12": 1.8392627078851576e-08, "-13": 2.116647295166004e-09, "-14": 2.2485809000827665e-10, "-15": 1.9936886382315e-11, "-2": 0.11301152257481206, "-3": 0.04926784036171802, "-4": 0.016991659110050572, "-5": 0.0048254928304868605, "-6": 0.0011619380375979273, "-7": 0.00024250564506559264, "-8": 4.4623832812344094e-05, "-9": 7.338425068635686e-06, "0": 0.26258133621995605, "1": 0.19686139483696444, "10": 4.678454750180152e-07, "11": 5.727639042556795e-08, "12": 6.442631162868023e-09, "13": 6.699291547967941e-10, "14": 6.43057456827879e-11, "15": 5.151805685042755e-12, "2": 0.10912730779443741, "3": 0.042986800261886816, "4": 0.013395787799849838, "5": 0.0034374392081084003, "6": 0.0007478890929421886, "7": 0.00014103826666050408, "8": 2.3450000589072178e-05, "9": 3.484494080735977e-06} |
| Raw goal margin distribution | {"-1": 0.19941875206073956, "-10": 1.1745511208831886e-06, "-11": 1.5914179499253098e-07, "-12": 1.9811209999162412e-08, "-13": 2.2798996510351204e-09, "-14": 2.4220090050576286e-10, "-15": 2.1474574630159127e-11, "-2": 0.12172785303895153, "-3": 0.05306776065358846, "-4": 0.01830218844867764, "-5": 0.0051976724915034226, "-6": 0.0012515557658065953, "-7": 0.0002612095727151979, "-8": 4.806557100422995e-05, "-9": 7.904421672585613e-06, "0": 0.26673684882746895, "1": 0.17928288687270702, "10": 4.2606976061013507e-07, "11": 5.216196214422007e-08, "12": 5.867343949745102e-09, "13": 6.101086145997864e-10, "14": 5.856363934665956e-11, "15": 4.691781222959518e-12, "2": 0.09938291250164184, "3": 0.03914834421829674, "4": 0.01219962659860376, "5": 0.0031304970951236454, "6": 0.0006811072112657264, "7": 0.00012844441962508115, "8": 2.135606021819229e-05, "9": 3.173350257944553e-06} |
| Research history json | {"away": [{"away": "Sparta Rotterdam", "away_goals": 3.0, "away_xg": 2.42, "date": "2026-11-01T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 2.09, "source": "pipeline training history"}, {"away": "Ajax", "away_goals": 2.0, "away_xg": 1.43, "date": "2026-10-25T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 1.0, "home_xg": 1.25, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 2.0, "away_xg": 1.17, "date": "2026-10-17T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 3.0, "home_xg": 3.38, "source": "pipeline training history"}, {"away": "Sparta Rotterdam", "away_goals": 3.0, "away_xg": 2.36, "date": "2026-10-10T00:00:00+00:00", "home": "Go Ahead Eagles", "home_goals": 3.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Heerenveen", "away_goals": 4.0, "away_xg": 1.8, "date": "2026-09-19T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 0.0, "home_xg": 0.67, "source": "pipeline training history"}, {"away": "Sparta Rotterdam", "away_goals": 1.0, "away_xg": 2.29, "date": "2026-09-13T00:00:00+00:00", "home": "PSV Eindhoven", "home_goals": 4.0, "home_xg": 3.76, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 2.0, "away_xg": 1.08, "date": "2026-09-04T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 2.0, "home_xg": 2.23, "source": "pipeline training history"}, {"away": "Sparta Rotterdam", "away_goals": 1.0, "away_xg": 0.97, "date": "2026-08-29T00:00:00+00:00", "home": "Excelsior", "home_goals": 2.0, "home_xg": 1.2, "source": "pipeline training history"}, {"away": "Utrecht", "away_goals": 3.0, "away_xg": 1.93, "date": "2026-08-22T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 3.0, "home_xg": 1.73, "source": "pipeline training history"}, {"away": "Sparta Rotterdam", "away_goals": 3.0, "away_xg": 3.08, "date": "2026-08-14T00:00:00+00:00", "home": "Telstar", "home_goals": 1.0, "home_xg": 1.42, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 33.4% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 39.9% |
| Raw p over 1 5 | 79.2% |
| Raw p under 3 5 | 67.4% |
| Raw p btts yes | 59.1% |
| P home draw | 62.9% |
| P draw away | 63.3% |
| P home away | 73.7% |
| Raw p home draw | 60.1% |
| Raw p draw away | 66.6% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5509 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.71, "draw": 3.65, "home": 2.51}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.67, "draw": 3.62, "home": 2.52}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.52 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.67 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:02Z |
| Market reference home last update utc | 2026-11-05T12:31:02Z |
| Market reference draw last update utc | 2026-11-05T12:31:02Z |
| Market reference away last update utc | 2026-11-05T12:31:02Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-05T12:31:02Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:31:02Z |
| Home probability edge | -1.4% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | -0.0468 |
| Raw ev home | -0.1584 |
| Raw edge prob draw | 0.0059 |
| Raw ev draw | -0.0264 |
| Raw edge prob away | 0.0408 |
| Raw ev away | 0.0821 |
| Elo home rating | 1,353.4514 |
| Elo away rating | 1,463.4189 |
| Elo rating diff | -49.9676 |
| Elo home expectancy | 0.4286 |

</details>


---

## 2026-11-07 — Excelsior vs Go Ahead Eagles

The model's most likely 1X2 outcome is **Go Ahead Eagles win** at **41.0%**. Expected goals are 1.57 for Excelsior and 1.78 for Go Ahead Eagles (3.34 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 64.6%; Under 3.5 goals: 57.1%; Double Chance 1X: 59.0%; Double Chance X2: 66.3%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 66.8%; BTTS No (at least one team does not score): 33.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Excelsior win | 33.7% | 2.97 |
| Draw | 25.4% | 3.94 |
| Go Ahead Eagles win | 41.0% | 2.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Excelsior expected goals | 1.57 |
| Go Ahead Eagles expected goals | 1.78 |
| Expected total goals | 3.34 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 64.6% |
| Under 2.5 | 35.4% |
| Over 3.5 | 42.9% |
| Under 3.5 | 57.1% |
| Over 4.5 | 24.3% |
| Under 4.5 | 75.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.08% |
| 2 | 1-2 | 8.47% |
| 3 | 2-1 | 7.75% |
| 4 | 2-2 | 7.13% |
| 5 | 0-2 | 5.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Excelsior win | 33.7% | 33.8% | 2.83 | -4.8% |
| Draw | 25.4% | 25.8% | 3.77 | -4.4% |
| Go Ahead Eagles win | 41.0% | 40.4% | 2.43 | -0.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T20:00:00+00:00 |
| Fixture id | 5d4dbfdacb0b931ba7b8d771bfed5e0e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:31:02Z |
| Market best draw last update utc | 2026-11-05T12:30:40Z |
| Market best away last update utc | 2026-11-05T12:30:40Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Excelsior |
| Matched away-team name | Go Ahead Eagles |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5661 |
| Dc lambda away | 1.7774 |
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
| P btts yes | 66.8% |
| P btts no | 33.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.17 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.85 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.82 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.11 |
| Fair Under 4.5 odds | 1.32 |
| Score matrix json | [[0.04511308566945892,0.053162474390149796,0.054101248403902735,0.032053717676342894,0.014243305568535364,0.005063294200495167,0.0014999413840072185,0.00038086285890503004,8.461960846267174e-05,1.6711709492637746e-05,2.9703884869730324e-06,4.799687291350994e-07,7.109254680368782e-08,9.720152881579016e-09,1.2340632957208669e-09,1.462306976003921e-10,1.62446719164785e-11],[0.04767782857130051,0.11078857881087051,0.08472879180307723,0.0501998170400363,0.02230665849139604,0.007929702415527547,0.002349081120893308,0.0005964751429906223,0.00013252406181766442,2.6172463594630633e-05,4.651970797569252e-06,7.516863607151399e-07,1.1133912385736484e-07,1.5222879953690288e-08,1.932685384158527e-09,2.2901412994581813e-10,2.5441028910181538e-11],[0.04360500789096971,0.07750482586522091,0.07132858650393094,0.0393093502647434,0.01746739935675402,0.006209414060185761,0.0018394659189264707,0.0004670744178476058,0.00010377397910319775,2.049454757797334e-05,3.642761274551354e-06,5.886137477157687e-07,8.718495157837407e-08,1.1920392452038298e-08,1.513404055971889e-09,1.7933126414456578e-10,1.9921792060082494e-11],[0.022763489717050545,0.04046049735883936,0.035957840095546624,0.022061610393223588,0.009118653679304332,0.0032415527469086824,0.000960271894344025,0.00024383079426006034,5.417400478678201e-05,1.069894137419509e-05,1.9016613647280695e-06,3.0727899481053195e-07,4.551389495670454e-08,6.2229029216934354e-09,7.900550723898186e-10,9.361781099794031e-11,1.0399940984733121e-11],[0.008912562269119148,0.01584145078951059,0.014078530704127578,0.008341198434439026,0.0038382506343022384,0.0012691613221244354,0.0003759741217189368,9.546678316830337e-05,2.121068417150907e-05,4.188943892014288e-06,7.445552302651532e-07,1.2030858226407521e-07,1.7820001588242263e-08,2.4364458382114187e-09,3.0932933026667964e-10,3.665407107561362e-11,4.071876622333988e-12],[0.0027916199910746745,0.004961907628387785,0.004409720411690932,0.0026126556646657935,0.0011609527903424614,0.0004273753052586707,0.00011776376339652316,2.9902397574223793e-05,6.643675316885946e-06,1.3120738074341646e-06,2.3321186461374755e-07,3.76834218045175e-08,5.581635356095655e-09,7.631510113189831e-10,9.688907814874075e-11,1.1480900158587949e-11,1.2754056394627162e-12],[0.0007286664540875037,0.0012951532259572315,0.0011510217530241805,0.0006819533263876563,0.00030303098409041504,0.00010772324001142084,3.3046314032110295e-05,7.805100292585483e-06,1.7341269050736136e-06,3.424764730947825e-07,6.087277744913123e-08,9.836097116359623e-09,1.4569140699447253e-09,1.9919707665405552e-10,2.5289910962154824e-11,2.9967355281298235e-12,3.329053767352976e-13],[0.0001630250954161846,0.00028976560819540814,0.00025751896503573246,0.00015257393211953922,6.77973506510123e-05,2.410100174488547e-05,7.139638441244159e-06,1.877340493605119e-06,3.8797752054803573e-07,7.66225196602375e-08,1.3619112415872336e-08,2.200637427347275e-09,3.2595648383917266e-10,4.4566512216922646e-11,5.658130856092622e-12,6.70461900187554e-13,7.448117105211953e-14],[3.191451162335438e-05,5.6725793333795036e-05,5.041304826036716e-05,2.986854580651579e-05,1.3272308351426716e-05,4.718118387589489e-06,1.3976871072391558e-06,3.5489860683465505e-07,8.16543218281383e-08,1.499996235588512e-08,2.6661375071520258e-09,4.308064876427047e-10,6.381067875247047e-11,8.724536971000229e-12,1.1076606488849875e-12,1.3125257833419235e-13,1.4580762508959896e-14],[5.553533812595018e-06,9.87101463570498e-06,8.772516133540231e-06,5.197509553871537e-06,2.3095516569615114e-06,8.210130333979564e-07,2.432154595090412e-07,6.175690345381403e-08,1.3721067486477734e-08,2.806145977821497e-09,4.639420765618575e-10,7.496584701168598e-11,1.1103875448219585e-11,1.5181811847695307e-12,1.9274714083239257e-13,2.2839629832712472e-14,2.5372394402448233e-15],[8.697474162994891e-07,1.5459146852024247e-06,1.3738771562510686e-06,8.139899131287291e-07,3.617024140371361e-07,1.285801056845301e-07,3.8090344751720614e-08,9.671843015665937e-09,2.148877345118487e-09,4.2438643453157115e-10,7.811354755952959e-11,1.1740515849790029e-11,1.7389949008859264e-12,2.377646751574909e-13,3.018642424718629e-14,3.576949327505068e-15,3.9736094568855033e-16],[1.2382951987075942e-07,2.20098237306928e-07,1.9560454613801659e-07,1.1589109462518205e-07,5.149706159160396e-08,1.830647893107885e-08,5.423079176694111e-09,1.3770201031363205e-09,3.05944513223535e-10,6.042164362074094e-11,1.0739520972052769e-11,1.7970373096461072e-12,2.47587862405622e-13,3.385153553228954e-14,4.2977654789111736e-15,5.092649998450458e-16,5.657391352693692e-17],[1.6160941934086328e-08,2.8724934382564382e-08,2.5528272381893148e-08,1.5124901177603066e-08,6.720861253654111e-09,2.3891713650470257e-09,7.077639303615007e-10,1.7971435205500298e-10,3.992869808764715e-11,7.88560494408758e-12,1.4016106580271983e-12,2.2647855296566553e-13,3.4738471392281876e-14,4.417950587937108e-15,5.608996822687771e-16,6.64639748272311e-17,7.383439202922602e-18],[1.946915238872812e-09,3.460504512245063e-09,3.075401342639229e-09,1.822102988131648e-09,8.096648850331254e-10,2.8782444475453094e-10,8.526460816240939e-11,2.165026098646273e-11,4.810226476417752e-12,9.499820305024116e-13,1.6885260526331928e-13,2.7283963264338414e-14,4.041276686619522e-15,5.721897870128173e-16,6.757181254297596e-17,8.006942043041933e-18,8.89485919700116e-19],[2.1779240748905645e-10,3.8711064241550737e-10,3.440309311032265e-10,2.038302379860924e-10,9.057346773494247e-11,3.2197590067445846e-11,9.53815755022468e-12,2.421914610796341e-12,5.380977989946601e-13,1.0627009813444618e-13,1.8888760371709256e-14,3.052130840900687e-15,4.52078940744149e-16,6.181064845952998e-17,8.126436250520049e-18,8.95699591518462e-19,9.950267788302072e-20],[2.2739201151964596e-11,4.0417326147582846e-11,3.591947320407406e-11,2.1281443351745236e-11,9.456566120007285e-12,3.361675852676072e-12,9.958569522887843e-13,2.528664986200095e-13,5.618154568305515e-14,1.1095414967758288e-14,1.972131749474032e-15,3.1866591647297396e-16,4.7200515796974366e-17,6.453506735423029e-18,8.193323590584531e-19,1.0053880455598936e-19,1.0388844283540222e-20],[2.2257631489725894e-12,3.956137004026809e-12,3.5158772400950923e-12,2.0830746011132354e-12,9.256295436709496e-13,3.2904824499654704e-13,9.74766743668578e-14,2.4751130458666948e-14,5.4991735724568575e-15,1.0860436825706895e-15,1.9303660421328857e-16,3.119172256664099e-17,4.62009056392588e-18,6.316834693249537e-19,8.019805794257316e-20,9.503092750431959e-21,1.0932257535853563e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18771440377650586, "-10": 3.815803845324042e-06, "-11": 6.040562299936076e-07, "-12": 8.792652050097027e-08, "-13": 1.1842569470866842e-08, "-14": 1.4829992177267677e-09, "-15": 1.7167172651057363e-10, "-16": 1.62446719164785e-11, "-2": 0.1254177075591964, "-3": 0.061632529118491916, "-4": 0.024278890594002827, "-5": 0.00793805607075401, "-6": 0.002211673188738783, "-7": 0.0005359092248720134, "-8": 0.00011476072145421743, "-9": 2.2000344339012534e-05, "0": 0.25359249551198426, "1": 0.17075787769033304, "10": 1.1172900615967041e-06, "11": 1.558434714483141e-07, "12": 1.998768445033003e-08, "13": 2.3720284290935068e-09, "14": 2.617256108767344e-10, "15": 2.6695338155991406e-11, "16": 2.2257631489725894e-12, "2": 0.10108528525917677, "3": 0.04376938291498291, "4": 0.015192198412298226, "5": 0.00437660446734883, "6": 0.0010744233589536963, "7": 0.00022939136877339562, "8": 4.328231299215725e-05, "9": 7.311020828196246e-06} |
| Raw goal margin distribution | {"-1": 0.1935361216651033, "-10": 3.934146034622156e-06, "-11": 6.227902476775111e-07, "-12": 9.065344708190585e-08, "-13": 1.2209851347741825e-08, "-14": 1.5289925080706198e-09, "-15": 1.769959016462384e-10, "-16": 1.6748479270564963e-11, "-2": 0.12930737450512544, "-3": 0.06354398178312506, "-4": 0.025031868782371854, "-5": 0.008184244546960767, "-6": 0.0022802653537915083, "-7": 0.0005525297518978263, "-8": 0.00011831987584811156, "-9": 2.268265638122654e-05, "0": 0.24319909803309833, "1": 0.16958162951505634, "10": 1.109593723284329e-06, "11": 1.5476995963498334e-07, "12": 1.9850001330343365e-08, "13": 2.355688953871839e-09, "14": 2.599227407756241e-10, "15": 2.651145004951515e-11, "16": 2.210431207172956e-12, "2": 0.10038896961071772, "3": 0.04346788199752539, "4": 0.01508754850740005, "5": 0.004346456675116586, "6": 0.001067022303538052, "7": 0.0002278112297918533, "8": 4.298416720604536e-05, "9": 7.260659608995741e-06} |
| Research history json | {"away": [{"away": "Go Ahead Eagles", "away_goals": 0.0, "away_xg": 0.6, "date": "2026-10-31T00:00:00+00:00", "home": "Cambuur", "home_goals": 4.0, "home_xg": 1.52, "source": "pipeline training history"}, {"away": "Telstar", "away_goals": 2.0, "away_xg": 1.05, "date": "2026-10-23T00:00:00+00:00", "home": "Go Ahead Eagles", "home_goals": 3.0, "home_xg": 1.1, "source": "pipeline training history"}, {"away": "Go Ahead Eagles", "away_goals": 1.0, "away_xg": 2.74, "date": "2026-10-18T00:00:00+00:00", "home": "Zwolle", "home_goals": 4.0, "home_xg": 1.77, "source": "pipeline training history"}, {"away": "Sparta Rotterdam", "away_goals": 3.0, "away_xg": 2.36, "date": "2026-10-10T00:00:00+00:00", "home": "Go Ahead Eagles", "home_goals": 3.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Go Ahead Eagles", "away_goals": 1.0, "away_xg": 2.86, "date": "2026-09-20T00:00:00+00:00", "home": "Nijmegen", "home_goals": 1.0, "home_xg": 1.12, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 1.0, "away_xg": 0.16, "date": "2026-09-12T00:00:00+00:00", "home": "Go Ahead Eagles", "home_goals": 1.0, "home_xg": 2.23, "source": "pipeline training history"}, {"away": "Go Ahead Eagles", "away_goals": 3.0, "away_xg": 1.79, "date": "2026-09-08T00:00:00+00:00", "home": "Utrecht", "home_goals": 3.0, "home_xg": 2.46, "source": "pipeline training history"}, {"away": "Go Ahead Eagles", "away_goals": 2.0, "away_xg": 1.82, "date": "2026-08-29T00:00:00+00:00", "home": "AZ Alkmaar", "home_goals": 5.0, "home_xg": 2.39, "source": "pipeline training history"}, {"away": "Den Haag", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-08-23T00:00:00+00:00", "home": "Go Ahead Eagles", "home_goals": 3.0, "home_xg": 0.85, "source": "pipeline training history"}, {"away": "Go Ahead Eagles", "away_goals": 2.0, "away_xg": 1.51, "date": "2026-08-16T00:00:00+00:00", "home": "Feyenoord", "home_goals": 2.0, "home_xg": 2.89, "source": "pipeline training history"}], "h2h": [{"away": "Go Ahead Eagles", "away_goals": 1.0, "away_xg": null, "date": "2026-03-01T00:00:00+00:00", "home": "Excelsior", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 0.0, "away_xg": null, "date": "2025-10-26T00:00:00+00:00", "home": "Go Ahead Eagles", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 0.0, "away_xg": null, "date": "2024-03-30T00:00:00+00:00", "home": "Go Ahead Eagles", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Go Ahead Eagles", "away_goals": 1.0, "away_xg": null, "date": "2023-12-16T00:00:00+00:00", "home": "Excelsior", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Go Ahead Eagles", "away_goals": 1.0, "away_xg": null, "date": "2023-04-14T00:00:00+00:00", "home": "Excelsior", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Twente", "away_goals": 9.0, "away_xg": 6.23, "date": "2026-11-01T00:00:00+00:00", "home": "Excelsior", "home_goals": 0.0, "home_xg": 0.0, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 0.0, "away_xg": 0.87, "date": "2026-10-25T00:00:00+00:00", "home": "For Sittard", "home_goals": 1.0, "home_xg": 0.57, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 0.0, "away_xg": 0.67, "date": "2026-10-16T00:00:00+00:00", "home": "Heerenveen", "home_goals": 4.0, "home_xg": 2.25, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 5.0, "away_xg": 2.75, "date": "2026-10-11T00:00:00+00:00", "home": "Excelsior", "home_goals": 1.0, "home_xg": 1.77, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 2.0, "away_xg": 0.82, "date": "2026-09-19T00:00:00+00:00", "home": "Ajax", "home_goals": 2.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Utrecht", "away_goals": 2.0, "away_xg": 1.42, "date": "2026-09-13T00:00:00+00:00", "home": "Excelsior", "home_goals": 1.0, "home_xg": 0.61, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-09-08T00:00:00+00:00", "home": "Nijmegen", "home_goals": 2.0, "home_xg": 1.36, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 3.0, "away_xg": 1.59, "date": "2026-09-05T00:00:00+00:00", "home": "Willem II", "home_goals": 0.0, "home_xg": 0.85, "source": "pipeline training history"}, {"away": "Sparta Rotterdam", "away_goals": 1.0, "away_xg": 0.97, "date": "2026-08-29T00:00:00+00:00", "home": "Excelsior", "home_goals": 2.0, "home_xg": 1.2, "source": "pipeline training history"}, {"away": "PSV Eindhoven", "away_goals": 2.0, "away_xg": 2.24, "date": "2026-08-15T00:00:00+00:00", "home": "Excelsior", "home_goals": 1.0, "home_xg": 0.51, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 33.4% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 42.3% |
| Raw p over 1 5 | 85.5% |
| Raw p under 3 5 | 57.1% |
| Raw p btts yes | 66.5% |
| P home draw | 59.0% |
| P draw away | 66.3% |
| P home away | 74.6% |
| Raw p home draw | 57.7% |
| Raw p draw away | 66.6% |
| Raw p home away | 75.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6456 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.05, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.8, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.43, "draw": 3.77, "home": 2.75}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.38, "draw": 3.66, "home": 2.83}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.83 |
| Reference draw odds | 3.66 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:02Z |
| Market reference home last update utc | 2026-11-05T12:31:02Z |
| Market reference draw last update utc | 2026-11-05T12:31:02Z |
| Market reference away last update utc | 2026-11-05T12:31:02Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.51 |
| Market reference over 2 5 last update utc | 2026-11-05T12:31:02Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:31:02Z |
| Home probability edge | -0.1% |
| Draw probability edge | -0.4% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | -0.0033 |
| Raw ev home | -0.0542 |
| Raw edge prob draw | -0.0148 |
| Raw ev draw | -0.0831 |
| Raw edge prob away | 0.0182 |
| Raw ev away | 0.0269 |
| Elo home rating | 1,391.7607 |
| Elo away rating | 1,414.2344 |
| Elo rating diff | 37.5263 |
| Elo home expectancy | 0.5538 |

</details>


---

## 2026-11-07 — Fortuna Sittard vs SC Telstar

The model's most likely 1X2 outcome is **Fortuna Sittard win** at **44.6%**. Expected goals are 1.54 for Fortuna Sittard and 1.44 for SC Telstar (2.98 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.5%; Under 3.5 goals: 65.1%; Double Chance 1X: 70.0%; Double Chance X2: 55.4%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 81.7%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fortuna Sittard win | 44.6% | 2.24 |
| Draw | 25.5% | 3.93 |
| SC Telstar win | 30.0% | 3.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fortuna Sittard expected goals | 1.54 |
| SC Telstar expected goals | 1.44 |
| Expected total goals | 2.98 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.8% |
| Under 1.5 | 19.2% |
| Over 2.5 | 57.5% |
| Under 2.5 | 42.5% |
| Over 3.5 | 34.9% |
| Under 3.5 | 65.1% |
| Over 4.5 | 18.3% |
| Under 4.5 | 81.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.84% |
| 2 | 2-1 | 9.90% |
| 3 | 1-0 | 7.89% |
| 4 | 1-2 | 6.99% |
| 5 | 2-0 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fortuna Sittard win | 44.6% | 47.0% | 2.08 | -7.3% |
| Draw | 25.5% | 25.2% | 3.74 | -4.7% |
| SC Telstar win | 30.0% | 27.9% | 3.46 | +3.7% |
| Over 2.5 | 57.5% | 59.2% | 1.64 | -5.7% |
| Under 2.5 | 42.5% | 40.8% | 2.33 | -1.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:30:00+00:00 |
| Fixture id | 33c5cad848eb423e163a9bf5631ccefe |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:30:40Z |
| Market best draw last update utc | 2026-11-05T12:31:02Z |
| Market best away last update utc | 2026-11-05T12:30:40Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 6.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | For Sittard |
| Matched away-team name | Telstar |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5366 |
| Dc lambda away | 1.4427 |
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
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.15 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.20 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.86 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.48 |
| Fair Under 4.5 odds | 1.22 |
| Score matrix json | [[0.05829834561236613,0.05524885373633292,0.045510378632769986,0.021885326940533165,0.007893268794117605,0.002277459867992194,0.0005475998585635033,0.00011285716386292496,2.0351807677636224e-05,3.2623032242818667e-06,4.7063927913239497e-07,6.172474861363116e-08,7.420649664507756e-09,8.234977580830003e-10,8.485906266349653e-11,8.161515619298957e-12],[0.07887471747600366,0.1184467358010514,0.06993070297030791,0.03362873137215539,0.012128702333159264,0.003499517568080167,0.0008414353869649668,0.00017341496689914966,3.1272344031627474e-05,5.012816079101199e-06,7.231786819604441e-07,9.484550976925251e-08,1.1402481436657349e-08,1.2653767963984906e-09,1.3039341978110315e-10,1.2540887193361193e-11],[0.0686066153080386,0.09897598645017633,0.06072910924204886,0.025836753016609003,0.009318409401945884,0.002688658399960818,0.0006464697710972639,0.00013323368103224358,2.4026354727867912e-05,3.8513165875969516e-06,5.55613852509455e-07,7.286923742450686e-08,8.760458234214462e-09,9.721814183143924e-10,1.001804839020739e-10,9.635088562761345e-12],[0.03514003458140142,0.05069510528935825,0.03656788803587777,0.014958074491464189,0.004772852109928639,0.0013771201031852743,0.000331119236974321,6.824175974662721e-05,1.2306203012807296e-05,1.972628987225735e-06,2.845831980403829e-07,3.7323332619172286e-08,4.487071748358781e-09,4.979474429043991e-10,5.131204407759098e-11,4.935053912368536e-12],[0.013498939112917482,0.019474372970201454,0.014047444743994648,0.006755226612859433,0.0020724162983394305,0.0005290165660198757,0.0001271984638682674,2.6214867764120614e-05,4.727391055813308e-06,7.577795215099161e-07,1.0932178379072218e-07,1.4337646519677401e-08,1.7236951826577218e-09,1.9128501987180935e-10,1.971136815924883e-11,1.8957861901845425e-12],[0.0041484616471196755,0.005984817672914461,0.00431702708435284,0.0020760000683485423,0.0007487403135720468,0.00018376308810918348,3.9090327359510525e-05,8.056290393939274e-06,1.452810500286755e-06,2.328789881679202e-07,3.3596508840945733e-08,4.40621119921368e-09,5.297218764204831e-10,5.878525430545638e-11,6.057650466965224e-12,5.826084728090865e-13],[0.0010624127504678265,0.001532699864621909,0.0011055820226073048,0.0005316594752941545,0.000191750900356166,5.532625222873305e-05,1.1315586524425056e-05,2.063199895299801e-06,3.7206187035376095e-07,5.963984421006437e-08,8.603998879586633e-09,1.1284218964755206e-09,1.3566071560565359e-10,1.505478633434474e-11,1.5513521978561945e-12,1.492048674169906e-13],[0.000233212959068188,0.00033644689470687154,0.00024268915717672387,0.00011670594069526353,4.209173398602296e-05,1.2144808117875188e-05,2.9201371673312547e-06,5.119202153310676e-07,8.167225939582962e-08,1.3091695803227334e-08,1.8886859534057693e-09,2.477027967129637e-10,2.9779233072806094e-11,3.3047149214143203e-12,3.4054131641366873e-13,3.2752344719479913e-14],[4.479403011844216e-05,6.462253382047032e-05,4.66141566893587e-05,2.2416118912912764e-05,8.084706816640011e-06,2.3326958449840696e-06,5.608809765377285e-07,1.155943254674438e-07,1.7731423224074474e-08,2.5145678801656326e-09,3.627665281516382e-10,4.757714400055556e-11,5.719801628936765e-12,6.347481731468278e-13,6.540896374265253e-14,6.290857599319864e-15],[7.647774491011613e-06,1.1033134647405915e-05,7.958528346439706e-06,3.827148884714357e-06,1.3803181896364167e-06,3.9826583433967615e-07,9.576033264961566e-08,1.973565073912925e-08,3.5589780434639028e-09,4.852660038354582e-10,6.193585602490174e-11,8.122941099082544e-12,9.765531896943455e-13,1.0837182709331446e-13,1.1167403403352418e-14,1.0740507194251585e-15],[1.1751478725991856e-06,1.6953382613775784e-06,1.2228979379989318e-06,5.880751158756405e-07,2.1209804054337808e-07,6.119705131254496e-08,1.4714418073499035e-08,3.032556465636647e-09,5.468683054553035e-10,8.766052944303407e-11,1.075724740857557e-11,1.2481614047399406e-12,1.500559940278077e-13,1.665228521160926e-14,1.7159698376737304e-15,1.6503734772508255e-16],[1.6415619568298082e-07,2.3682149784945726e-07,1.7082639375966954e-07,8.214810752663415e-08,2.96279372658073e-08,8.548605128530878e-09,2.0554544231884535e-09,4.2361726911156994e-10,7.639193556516772e-11,1.2245283645109817e-11,1.766577497950035e-12,1.9707751474106385e-13,2.0961294908827698e-14,2.326154736356396e-15,2.397035190441419e-16,2.305403752145428e-17],[2.102003708808301e-08,3.0324756536539696e-08,2.1874149297332952e-08,1.0518983214379555e-08,3.793827808810715e-09,1.0946403582604803e-09,2.631988882815283e-10,5.4243768691338074e-11,9.781911137312945e-12,1.5679963543465008e-12,2.2620848620051507e-13,2.966743866074345e-14,3.0338623673245324e-15,2.9786179332066945e-16,3.069379647529355e-17,2.9520465049450926e-18],[2.484549026451921e-09,3.5843582965401133e-09,2.585504303033032e-09,1.2433341290043499e-09,4.4842695326407324e-10,1.293854822917008e-10,3.110986621492856e-11,6.411563506210639e-12,1.1562128882650092e-12,1.8533572511536635e-13,2.6737634753426988e-14,3.5066639289452596e-15,4.215768406081853e-16,3.9795178803450454e-17,3.627978477451811e-18,3.4892917834385323e-19],[2.726948778399394e-10,3.934058605417881e-10,2.837753542247818e-10,1.3646373841423162e-10,4.921767771075578e-11,1.4200870223190088e-11,3.414503427695179e-12,7.037094090213793e-13,1.2690163444778039e-13,2.0341761173409253e-14,2.9346235333608883e-15,3.848784151766281e-16,4.627070902036852e-17,5.134836822364923e-18,4.50086181088074e-19,3.829717129758108e-20],[2.7934645644422853e-11,4.030018237131889e-11,2.9069720801806805e-11,1.39792364495834e-11,5.041819623390097e-12,1.4547258117554205e-12,3.497790059713474e-13,7.20874302200748e-14,1.2999702150905707e-14,2.083793779567066e-15,3.006204925944302e-16,3.942663767398233e-17,4.7399345027627224e-18,5.260085858997749e-19,5.420366371890871e-20,4.434395767249279e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.15635941617648572, "-10": 5.747634885553984e-07, "-11": 7.415261929887068e-08, "-12": 8.791141998720687e-09, "-13": 9.635262664268647e-10, "-14": 9.739994985685772e-11, "-15": 8.161515619298957e-12, "-2": 0.08997027978892679, "-3": 0.03706153616599273, "-4": 0.012112467020617232, "-5": 0.003265227673879773, "-6": 0.00074712767620465, "-7": 0.00014828029045020437, "-8": 2.5959345006407554e-05, "-9": 4.063035707290382e-06, "0": 0.2547002902677656, "1": 0.22198092452064602, "10": 1.4351375262785027e-06, "11": 1.9720796208059116e-07, "12": 2.490214997529749e-08, "13": 2.9070246077955155e-09, "14": 3.129950602112583e-10, "15": 2.7934645644422853e-11, "2": 0.1356296422941847, "3": 0.05950761741195705, "4": 0.020714542869791054, "5": 0.005947710413947217, "6": 0.0014495218671338802, "7": 0.000306412850755173, "8": 5.713613751125561e-05, "9": 9.524921106965735e-06} |
| Raw goal margin distribution | {"-1": 0.18173581237278577, "-10": 6.680448934199864e-07, "-11": 8.618723986945154e-08, "-12": 1.0217902905308282e-08, "-13": 1.1199020375847195e-09, "-14": 1.1320750259341677e-10, "-15": 9.486091132447798e-12, "-2": 0.10457203209554053, "-3": 0.043076448784559865, "-4": 0.01407826332215155, "-5": 0.00379515873367582, "-6": 0.0008683829762320585, "-7": 0.00017234548262462176, "-8": 3.0172424333433776e-05, "-9": 4.7224472501906095e-06, "0": 0.26190533728066767, "1": 0.1941617992353478, "10": 1.2552830152145966e-06, "11": 1.7249343755004732e-07, "12": 2.178135916170821e-08, "13": 2.5427100526311745e-09, "14": 2.7376984834902637e-10, "15": 2.443381597331149e-11, "2": 0.11863224479469292, "3": 0.05204999524109861, "4": 0.018118551954955483, "5": 0.005202330595732785, "6": 0.0012678646796406082, "7": 0.00026801253549118864, "8": 4.9975714284908444e-05, "9": 8.331237576818006e-06} |
| Research history json | {"away": [{"away": "Utrecht", "away_goals": 2.0, "away_xg": 1.28, "date": "2026-11-01T00:00:00+00:00", "home": "Telstar", "home_goals": 4.0, "home_xg": 2.45, "source": "pipeline training history"}, {"away": "Telstar", "away_goals": 2.0, "away_xg": 1.05, "date": "2026-10-23T00:00:00+00:00", "home": "Go Ahead Eagles", "home_goals": 3.0, "home_xg": 1.1, "source": "pipeline training history"}, {"away": "Feyenoord", "away_goals": 4.0, "away_xg": 3.81, "date": "2026-10-17T00:00:00+00:00", "home": "Telstar", "home_goals": 3.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Den Haag", "away_goals": 2.0, "away_xg": 1.38, "date": "2026-10-11T00:00:00+00:00", "home": "Telstar", "home_goals": 2.0, "home_xg": 2.86, "source": "pipeline training history"}, {"away": "Telstar", "away_goals": 0.0, "away_xg": 0.11, "date": "2026-09-20T00:00:00+00:00", "home": "AZ Alkmaar", "home_goals": 1.0, "home_xg": 2.61, "source": "pipeline training history"}, {"away": "Telstar", "away_goals": 0.0, "away_xg": 0.71, "date": "2026-09-13T00:00:00+00:00", "home": "Heerenveen", "home_goals": 0.0, "home_xg": 1.54, "source": "pipeline training history"}, {"away": "Telstar", "away_goals": 0.0, "away_xg": 0.52, "date": "2026-09-09T00:00:00+00:00", "home": "Twente", "home_goals": 1.0, "home_xg": 2.65, "source": "pipeline training history"}, {"away": "Cambuur", "away_goals": 2.0, "away_xg": 0.98, "date": "2026-09-06T00:00:00+00:00", "home": "Telstar", "home_goals": 2.0, "home_xg": 2.12, "source": "pipeline training history"}, {"away": "Ajax", "away_goals": 4.0, "away_xg": 2.14, "date": "2026-08-30T00:00:00+00:00", "home": "Telstar", "home_goals": 0.0, "home_xg": 1.13, "source": "pipeline training history"}, {"away": "Sparta Rotterdam", "away_goals": 3.0, "away_xg": 3.08, "date": "2026-08-14T00:00:00+00:00", "home": "Telstar", "home_goals": 1.0, "home_xg": 1.42, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 34.8% |
| Raw p over 1 5 | 80.7% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 60.9% |
| P home draw | 70.0% |
| P draw away | 55.4% |
| P home away | 74.5% |
| Raw p home draw | 65.2% |
| Raw p draw away | 61.0% |
| Raw p home away | 73.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5750 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.53, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.46, "draw": 3.66, "home": 2.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.64, "under": 2.33}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.74, "home": 2.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.06 |
| Reference draw odds | 3.74 |
| Reference away odds | 3.39 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:02Z |
| Market reference home last update utc | 2026-11-05T12:31:02Z |
| Market reference draw last update utc | 2026-11-05T12:31:02Z |
| Market reference away last update utc | 2026-11-05T12:31:02Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-11-05T12:30:40Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:30:40Z |
| Market best over 2 5 last update utc | 2026-11-05T12:30:40Z |
| Market best under 2 5 last update utc | 2026-11-05T12:30:40Z |
| Home probability edge | -2.4% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0798 |
| Raw ev home | -0.1893 |
| Raw edge prob draw | 0.0103 |
| Raw ev draw | -0.0205 |
| Raw edge prob away | 0.0695 |
| Raw ev away | 0.2052 |
| Elo home rating | 1,444.9830 |
| Elo away rating | 1,422.9487 |
| Elo rating diff | 82.0343 |
| Elo home expectancy | 0.6159 |

</details>


---

## 2026-11-08 — Heerenveen vs Feyenoord

The model's most likely 1X2 outcome is **Feyenoord win** at **57.1%**. Expected goals are 1.16 for Heerenveen and 2.05 for Feyenoord (3.21 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 62.7%; Under 3.5 goals: 59.9%; Double Chance 1X: 42.9%; Double Chance X2: 78.6%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 77.7%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Heerenveen win | 21.4% | 4.67 |
| Draw | 21.5% | 4.66 |
| Feyenoord win | 57.1% | 1.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Heerenveen expected goals | 1.16 |
| Feyenoord expected goals | 2.05 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 83.9% |
| Under 1.5 | 16.1% |
| Over 2.5 | 62.7% |
| Under 2.5 | 37.3% |
| Over 3.5 | 40.1% |
| Under 3.5 | 59.9% |
| Over 4.5 | 22.3% |
| Under 4.5 | 77.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.85% |
| 2 | 1-1 | 9.83% |
| 3 | 0-2 | 8.46% |
| 4 | 0-1 | 7.48% |
| 5 | 1-3 | 6.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Heerenveen win | 21.4% | 21.9% | 4.38 | -6.2% |
| Draw | 21.5% | 21.0% | 4.40 | -5.5% |
| Feyenoord win | 57.1% | 57.2% | 1.71 | -2.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T11:15:00+00:00 |
| Fixture id | 019e9d824f3f2251e5b777623d34a9df |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:30:40Z |
| Market best draw last update utc | 2026-11-05T12:31:02Z |
| Market best away last update utc | 2026-11-05T12:30:40Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Heerenveen |
| Matched away-team name | Feyenoord |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1638 |
| Dc lambda away | 2.0492 |
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
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.98 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.19 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.50 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.47 |
| Fair Under 4.5 odds | 1.29 |
| Score matrix json | [[0.04550593285340551,0.07482499651040007,0.08463561494377143,0.05781266827100326,0.029617891488413834,0.012138785805317187,0.004145864583377797,0.0012136911563153468,0.0003108918342921836,7.078771939385342e-05,1.4506045504708198e-05,2.7023865154540677e-06,4.6148472856779485e-07,7.274532633686032e-08,1.0648003264784339e-08,1.4546818875351959e-09,1.863112860195905e-10,2.2458531576009098e-11],[0.04112578811196122,0.09833052052362896,0.09849501212599794,0.0672797080303818,0.03446793153492054,0.014126557193256338,0.0048247653506603705,0.0014124376036957474,0.00036180153011029635,8.237947210168452e-05,1.6881464485556493e-05,3.144912372712311e-06,5.37054571724275e-07,8.465764447294337e-08,1.2391653459118411e-08,1.6928914647508325e-09,2.1682045304333569e-10,2.61361997709915e-11],[0.028686095468607772,0.05878446286774447,0.054236675508483476,0.039148505405724204,0.02005609185179026,0.008219916774828034,0.0028074193236151367,0.000821864761044465,0.0002105239391188518,4.793470874512653e-05,9.822933586021375e-06,1.8299517436677875e-06,3.12499629083146e-07,4.926032453631166e-08,7.210416433601237e-09,9.850543737373921e-10,1.261628049010787e-10,1.5208049915402433e-11],[0.011127850148762889,0.022803545870633768,0.023364877192020253,0.014371521552219664,0.007780117197921956,0.0031886529209138145,0.0010890482314722184,0.0003188160589321043,8.166600609014713e-05,1.859473194684484e-05,3.8104918491300345e-06,7.098710525204424e-07,1.212242024288991e-07,1.910896205164543e-08,2.7970496602124726e-09,3.8212023212879486e-10,4.894081137055314e-11,5.899474911066307e-12],[0.003237519264398483,0.006634427860351699,0.006797740714353515,0.0046433824480663745,0.002142076450236234,0.0009277016783054574,0.0003168459839156244,9.275584401242492e-05,2.3759779690484845e-05,5.40992214034521e-06,1.108618520511203e-06,2.0652877034197475e-07,3.5268779272565384e-08,5.559531440288077e-09,8.137692400021971e-10,1.1117346084777458e-10,1.4238762879555224e-11,1.7163839752583343e-12],[0.0007535350204920982,0.001544168026636378,0.001582179215060842,0.0010807507237509625,0.0005536772236844768,0.00020433706767024318,7.37461387822996e-05,2.158899178987607e-05,5.530106422172497e-06,1.2591634081420953e-06,2.580317864846866e-07,4.806972514517609e-08,8.208834648223041e-09,1.2939850841512427e-09,1.8940539680613305e-10,2.5875705828014573e-11,3.3140826670019057e-12,3.9948964881569516e-13],[0.00014615486445440588,0.00029950521540522603,0.0003068778257562358,0.00020962128002447554,0.00010739065521632922,4.401367199530861e-05,1.3536202875676474e-05,4.187378267696195e-06,1.0726136577212162e-06,2.4422601768763523e-07,5.004757543182168e-08,9.323553613162736e-09,1.5921769827713677e-09,2.5097999354647257e-10,3.6736872665924917e-11,5.018824839070912e-12,6.427960079015847e-13,7.748459445914818e-14],[2.429832398279903e-05,4.979290142425917e-05,5.1018601817992256e-05,3.484964934104319e-05,1.7853753570997012e-05,7.317296388368124e-06,2.4991395703946997e-06,6.587990641329955e-07,1.7832259132104132e-07,4.0602705390310206e-08,8.320436045256219e-09,1.5500457491395886e-09,2.647002705640556e-10,4.1725557470551645e-11,6.107524627960259e-12,8.343822999521656e-13,1.0686517833770061e-13,1.2881855057458681e-14],[3.5346581296142364e-06,7.243334311491209e-06,7.421635986300014e-06,5.069551152776007e-06,2.597171527078479e-06,1.0644413657605235e-06,3.6354787292282514e-07,1.0642770148179736e-07,2.454851345400865e-08,5.906443703433551e-09,1.2103673047622428e-09,2.2548393923584107e-10,3.8505740721979964e-11,6.0697841147553055e-12,8.884568167467524e-13,1.2137693866539715e-13,1.5545593665284404e-14,1.873913350385472e-15],[4.5705239595372875e-07,9.366063648487042e-07,9.596618357558217e-07,6.55523226241724e-07,3.3582978201164095e-07,1.376386226710425e-07,4.7008910132249e-08,1.3761737111309399e-08,3.5251238927789957e-09,7.227571193429336e-10,1.5650771767452798e-10,2.915641934742743e-11,4.9790221315900594e-12,7.848593190180928e-13,1.1488276996107789e-13,1.5694762717152232e-14,2.0101380588161106e-15,2.42308182346572e-16],[5.318964281359187e-08,1.0899791455919367e-07,1.1168100357328755e-07,7.628675961112465e-08,3.908231596531e-08,1.6017745978447204e-08,5.4706794256553866e-09,1.6015272820475556e-09,4.102376059955181e-10,9.340800025878016e-11,1.7236321139243134e-11,3.3930891612041052e-12,5.794355550584516e-13,9.133829558070547e-14,1.3369525143643265e-14,1.8264838569053674e-15,2.3393056529400647e-16,2.81987049710809e-17],[5.627240448665778e-09,1.153152082215104e-08,1.1815380352480913e-08,8.070818239668005e-09,4.134744615568837e-09,1.6946101402158464e-09,5.787748688897949e-10,1.694348490506658e-10,4.3401412904992977e-11,9.882173473646149e-12,2.0250865449774424e-12,3.3971240469270406e-13,6.130184412493966e-14,9.663207425649328e-15,1.4144395165695426e-15,1.9323430831136442e-16,2.474886969658876e-17,2.9833043581317396e-18],[5.457268359538198e-10,1.118320858938979e-09,1.1458494077464122e-09,7.827037322595126e-10,4.0098537055875743e-10,1.6434240520405024e-10,5.612928411539687e-11,1.6431703055208256e-11,4.209046326815999e-12,9.583680156049415e-13,1.9639183411564067e-13,3.65865834411689e-14,5.62601793415825e-15,9.37132802778209e-16,1.371716046376807e-16,1.8739762168415754e-17,2.4001324407872187e-18,2.8931929653663406e-19],[4.885320292032929e-11,1.001115434543264e-10,1.025758858549364e-10,7.006726028369398e-11,3.589601680802829e-11,1.4711852782200075e-11,5.0246664191796105e-12,1.4709581255604823e-12,3.7679179537802486e-13,8.579264213179254e-14,1.7580902187406685e-14,3.2752132885109458e-15,5.593059715205637e-16,7.939014705968895e-17,1.227953583143723e-17,1.6775744632242999e-18,2.1485869750294897e-19,2.5899723765219344e-20],[4.060935489854643e-12,8.321798683717891e-12,8.526647801392146e-12,5.8243596520573366e-12,2.9838659470878e-12,1.2229266765207692e-12,4.176767328767354e-13,1.222737855268213e-13,3.1320918234000534e-14,7.131536201824261e-15,1.4614171716219934e-15,2.7225297595836694e-16,4.649245768265337e-17,7.328756071351636e-18,9.659679871946733e-19,1.3944882356416628e-19,1.7860186391803263e-20,2.1529214284503666e-21],[3.15061920116301e-13,6.456349475788677e-13,6.615278758240514e-13,4.518746825724086e-13,2.314990073119279e-13,9.4879031648905e-14,3.240485690472219e-14,9.486438221984173e-15,2.4299890168812034e-15,5.532901211405573e-16,1.1338197844621264e-16,2.1122360987293232e-17,3.6070513863166414e-18,5.685911449892779e-19,8.322679508148046e-20,1.0238407584219331e-20,1.3856572290533929e-21,1.6703135541101183e-22],[2.291590518875512e-14,4.69600046867064e-14,4.811597058923083e-14,3.2866927806463163e-14,1.6837989500263287e-14,6.900989154337061e-15,2.356954557407871e-15,6.899923633859819e-16,1.767442980732498e-16,4.0243339954417544e-17,8.246793732570964e-18,1.5363266419781714e-18,2.623574678567547e-19,4.1356253922816926e-20,6.053468297746462e-21,8.269973694151232e-22,9.537721742956702e-23,1.214896012420374e-23],[1.5687335303744621e-15,3.2146988448323274e-15,3.293831763925983e-15,2.249941744203753e-15,1.152663117410597e-15,4.724148136409336e-16,1.613479202902692e-16,4.723418722630486e-17,1.2099225599260192e-17,2.754902162526472e-18,5.645433483777135e-19,1.0517093246054246e-19,1.7959969435245747e-20,2.8310879140501308e-21,4.143968399028609e-22,5.661301581792136e-23,7.250824989892607e-24,7.870439847953426e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.22125445082439774, "-10": 1.7983406769178992e-05, "-11": 3.2916130264029763e-06, "-12": 5.537495479589967e-07, "-13": 8.617269136506194e-08, "-14": 1.2472957009347316e-08, "-15": 1.6867103904939339e-09, "-16": 2.1244748579058202e-10, "-17": 2.2458531576009098e-11, "-2": 0.17549961717903886, "-3": 0.1016881035396681, "-4": 0.04689575464424139, "-5": 0.0178727594714794, "-6": 0.005788579181191827, "-7": 0.0016274528818358233, "-8": 0.0004038407113838096, "-9": 8.962611388990762e-05, "0": 0.2148052842464362, "1": 0.12851881070333812, "10": 6.59401614529405e-08, "11": 6.854200114456138e-09, "12": 6.548342122964246e-10, "13": 5.78705490707951e-11, "14": 4.7569363497669455e-12, "15": 3.6531575656693334e-13, "16": 2.6130604033587447e-14, "17": 1.5687335303744621e-15, "2": 0.059483218458880244, "3": 0.019573045353951712, "4": 0.005126155220692485, "5": 0.0011094808319866926, "6": 0.00020406575964943712, "7": 3.258191112608896e-05, "8": 4.591432440841907e-06, "9": 5.786855466480959e-07} |
| Raw goal margin distribution | {"-1": 0.2208559756110291, "-10": 1.7951018982977436e-05, "-11": 3.285684891632644e-06, "-12": 5.527522551657734e-07, "-13": 8.601749592627958e-08, "-14": 1.2450493442232086e-08, "-15": 1.6836726559749723e-09, "-16": 2.1206487175992813e-10, "-17": 2.2418084171998234e-11, "-2": 0.17518354558300564, "-3": 0.10150496512774446, "-4": 0.0468112962490845, "-5": 0.017840570959034352, "-6": 0.005778154056111936, "-7": 0.0016245218690045758, "-8": 0.0004031134016594808, "-9": 8.946469890041199e-05, "0": 0.2265762394624081, "1": 0.1220690288006513, "10": 6.26309209015231e-08, "11": 6.510218594446125e-09, "12": 6.219710241871064e-10, "13": 5.4966286122416695e-11, "14": 4.518207078829465e-12, "15": 3.4698219945901233e-13, "16": 2.481922637548615e-14, "17": 1.4900058400155564e-15, "2": 0.05649802287677012, "3": 0.01859076211452934, "4": 0.004868896512867179, "5": 0.0010538009719540339, "6": 0.00019382461567726692, "7": 3.0946771339267535e-05, "8": 4.3610090677785734e-06, "9": 5.496439180671027e-07} |
| Research history json | {"away": [{"away": "For Sittard", "away_goals": 1.0, "away_xg": 0.89, "date": "2026-10-31T00:00:00+00:00", "home": "Feyenoord", "home_goals": 1.0, "home_xg": 2.56, "source": "pipeline training history"}, {"away": "Feyenoord", "away_goals": 1.0, "away_xg": 1.22, "date": "2026-10-25T00:00:00+00:00", "home": "PSV Eindhoven", "home_goals": 1.0, "home_xg": 2.03, "source": "pipeline training history"}, {"away": "Feyenoord", "away_goals": 4.0, "away_xg": 3.81, "date": "2026-10-17T00:00:00+00:00", "home": "Telstar", "home_goals": 3.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "AZ Alkmaar", "away_goals": 0.0, "away_xg": 0.98, "date": "2026-10-10T00:00:00+00:00", "home": "Feyenoord", "home_goals": 2.0, "home_xg": 2.15, "source": "pipeline training history"}, {"away": "Utrecht", "away_goals": 0.0, "away_xg": 0.66, "date": "2026-09-20T00:00:00+00:00", "home": "Feyenoord", "home_goals": 5.0, "home_xg": 3.59, "source": "pipeline training history"}, {"away": "Feyenoord", "away_goals": 7.0, "away_xg": 3.33, "date": "2026-09-13T00:00:00+00:00", "home": "Zwolle", "home_goals": 0.0, "home_xg": 0.22, "source": "pipeline training history"}, {"away": "Feyenoord", "away_goals": 3.0, "away_xg": 1.35, "date": "2026-09-05T00:00:00+00:00", "home": "Nijmegen", "home_goals": 1.0, "home_xg": 0.96, "source": "pipeline training history"}, {"away": "Den Haag", "away_goals": 2.0, "away_xg": 0.24, "date": "2026-08-30T00:00:00+00:00", "home": "Feyenoord", "home_goals": 2.0, "home_xg": 2.48, "source": "pipeline training history"}, {"away": "Feyenoord", "away_goals": 5.0, "away_xg": 2.57, "date": "2026-08-23T00:00:00+00:00", "home": "Cambuur", "home_goals": 2.0, "home_xg": 1.07, "source": "pipeline training history"}, {"away": "Go Ahead Eagles", "away_goals": 2.0, "away_xg": 1.51, "date": "2026-08-16T00:00:00+00:00", "home": "Feyenoord", "home_goals": 2.0, "home_xg": 2.89, "source": "pipeline training history"}], "h2h": [{"away": "Feyenoord", "away_goals": 2.0, "away_xg": null, "date": "2026-01-11T00:00:00+00:00", "home": "Heerenveen", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Heerenveen", "away_goals": 0.0, "away_xg": null, "date": "2025-09-13T00:00:00+00:00", "home": "Feyenoord", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Feyenoord", "away_goals": 0.0, "away_xg": null, "date": "2025-05-18T00:00:00+00:00", "home": "Heerenveen", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Heerenveen", "away_goals": 0.0, "away_xg": null, "date": "2024-11-23T00:00:00+00:00", "home": "Feyenoord", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Feyenoord", "away_goals": 3.0, "away_xg": null, "date": "2024-03-17T00:00:00+00:00", "home": "Heerenveen", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Heerenveen", "away_goals": 1.0, "away_xg": null, "date": "2023-09-16T00:00:00+00:00", "home": "Feyenoord", "home_goals": 6.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Feyenoord", "away_goals": 2.0, "away_xg": null, "date": "2023-02-12T00:00:00+00:00", "home": "Heerenveen", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Nijmegen", "away_goals": 0.0, "away_xg": 1.31, "date": "2026-10-31T00:00:00+00:00", "home": "Heerenveen", "home_goals": 1.0, "home_xg": 1.42, "source": "pipeline training history"}, {"away": "Heerenveen", "away_goals": 3.0, "away_xg": 2.43, "date": "2026-10-24T00:00:00+00:00", "home": "Den Haag", "home_goals": 2.0, "home_xg": 2.82, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 0.0, "away_xg": 0.67, "date": "2026-10-16T00:00:00+00:00", "home": "Heerenveen", "home_goals": 4.0, "home_xg": 2.25, "source": "pipeline training history"}, {"away": "Heerenveen", "away_goals": 0.0, "away_xg": 1.56, "date": "2026-10-09T00:00:00+00:00", "home": "PSV Eindhoven", "home_goals": 2.0, "home_xg": 1.6, "source": "pipeline training history"}, {"away": "Heerenveen", "away_goals": 4.0, "away_xg": 1.8, "date": "2026-09-19T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 0.0, "home_xg": 0.67, "source": "pipeline training history"}, {"away": "Telstar", "away_goals": 0.0, "away_xg": 0.71, "date": "2026-09-13T00:00:00+00:00", "home": "Heerenveen", "home_goals": 0.0, "home_xg": 1.54, "source": "pipeline training history"}, {"away": "AZ Alkmaar", "away_goals": 3.0, "away_xg": 1.04, "date": "2026-09-06T00:00:00+00:00", "home": "Heerenveen", "home_goals": 2.0, "home_xg": 1.48, "source": "pipeline training history"}, {"away": "Heerenveen", "away_goals": 2.0, "away_xg": 1.36, "date": "2026-08-30T00:00:00+00:00", "home": "Willem II", "home_goals": 2.0, "home_xg": 1.7, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 2.0, "away_xg": 1.55, "date": "2026-08-22T00:00:00+00:00", "home": "Heerenveen", "home_goals": 0.0, "home_xg": 0.85, "source": "pipeline training history"}, {"away": "Heerenveen", "away_goals": 2.0, "away_xg": 1.37, "date": "2026-08-16T00:00:00+00:00", "home": "Ajax", "home_goals": 2.0, "home_xg": 2.0, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 20.3% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 57.0% |
| Raw p over 1 5 | 83.8% |
| Raw p under 3 5 | 60.0% |
| Raw p btts yes | 60.7% |
| P home draw | 42.9% |
| P draw away | 78.6% |
| P home away | 78.5% |
| Raw p home draw | 43.0% |
| Raw p draw away | 79.7% |
| Raw p home away | 77.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6269 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.52, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.62, "price": 1.52, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:30:40Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.71, "draw": 4.33, "home": 4.38}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:02Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.7, "draw": 4.4, "home": 4.23}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.23 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:02Z |
| Market reference home last update utc | 2026-11-05T12:31:02Z |
| Market reference draw last update utc | 2026-11-05T12:31:02Z |
| Market reference away last update utc | 2026-11-05T12:31:02Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 2.94 |
| Market reference over 2 5 last update utc | 2026-11-05T12:31:02Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:31:02Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | -7.2% |
| Under 2.5 probability edge | +7.2% |
| Raw edge prob home | -0.0153 |
| Raw ev home | -0.1095 |
| Raw edge prob draw | 0.0168 |
| Raw ev draw | -0.0031 |
| Raw edge prob away | -0.0015 |
| Raw ev away | -0.0251 |
| Elo home rating | 1,519.8973 |
| Elo away rating | 1,658.3204 |
| Elo rating diff | -78.4231 |
| Elo home expectancy | 0.3890 |

</details>


---
