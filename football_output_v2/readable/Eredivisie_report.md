# Eredivisie — football model report

Fixtures in this report: **4**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Eredivisie |
| Training matches | 1,620 |
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
| Training sha256 | 173f00460382fe819ab1795f92939756d58effd9917931edff4bdbeeab528135 |
| Training as of utc | 2026-11-01T09:34:08.418106+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1319, 'tuning_matches': 188, 'audit_matches': 106, 'audit_matchdays': 35, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.688931324746308, 'audit_candidate_poisson_score': 0.6802697887067812, 'audit_gain': 0.008661536039526796, 'audit_gain_lower95': -0.004720200507761522, 'audit_baseline_briers': [0.6137541905831072, 0.09292909529206177, 0.28403384810112686, 0.22642787371071124], 'audit_candidate_briers': [0.612395307466804, 0.0916424763272845, 0.28041331535269864, 0.21976527414055588], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1610.331 |
| Base scoring parameter | 0.292 |
| Home-advantage parameter | 0.184 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1620, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 7, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 4.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 21.00 |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 4} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 4} |
| Legacy comparison status | {'AVAILABLE': 4} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'UNRELIABLE_AUDIT', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'UNRELIABLE_AUDIT', 'draw': 'UNRELIABLE_AUDIT', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-01 — Excelsior vs FC Twente Enschede

The model's most likely 1X2 outcome is **FC Twente Enschede win** at **61.9%**. Expected goals are 1.09 for Excelsior and 1.84 for FC Twente Enschede (2.93 combined). The most likely exact score is 1-2 at 11.3%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 57.7%; Under 3.5 goals: 65.6%; Double Chance 1X: 38.1%; Double Chance X2: 83.0%; Double Chance 12 (either team wins): 78.8%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 55.6%; BTTS No (at least one team does not score): 44.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Excelsior win | 17.0% | 5.89 |
| Draw | 21.2% | 4.73 |
| FC Twente Enschede win | 61.9% | 1.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Excelsior expected goals | 1.09 |
| FC Twente Enschede expected goals | 1.84 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 80.6% |
| Under 1.5 | 19.4% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.32% |
| 2 | 0-2 | 10.40% |
| 3 | 0-1 | 10.14% |
| 4 | 1-1 | 10.00% |
| 5 | 1-3 | 6.93% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:30:00+00:00 |
| Fixture id | c0c32575c239ac72913af247ce084ea2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Excelsior |
| Matched away-team name | Twente |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.0885 |
| Dc lambda away | 1.8371 |
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
| P btts yes | 55.6% |
| P btts no | 44.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.39 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.15 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.91 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.54 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.25931251577903164, "-10": 8.905192705774546e-06, "-11": 1.4653179697944083e-06, "-12": 2.2151748373407614e-07, "-13": 3.096625835536168e-08, "-14": 4.024251204171769e-09, "-15": 4.856666544343816e-10, "-16": 4.956811482854174e-11, "-2": 0.19313898081729744, "-3": 0.10263687307995975, "-4": 0.04308812271754754, "-5": 0.01488291831546205, "-6": 0.004356421043651539, "-7": 0.001104893317993544, "-8": 0.0002470094538256056, "-9": 4.93427368528796e-05, "0": 0.21150743560430466, "1": 0.10323689298329275, "10": 3.29475761314704e-08, "11": 3.2123501592287218e-09, "12": 2.877463796835055e-10, "13": 2.383424760420289e-11, "14": 1.8353067073252133e-12, "15": 1.3124196084744374e-13, "16": 7.9368410289136e-15, "2": 0.04702872902980863, "3": 0.014808380812771534, "4": 0.0036836010659944164, "5": 0.0007539003941525715, "6": 0.000130757489795762, "7": 1.965024319998221e-05, "8": 2.6029870845340374e-06, "9": 3.081005882698358e-07} |
| Raw goal margin distribution | {"-1": 0.225684644409493, "-10": 7.750359612080288e-06, "-11": 1.275294267869781e-06, "-12": 1.9279090481545177e-07, "-13": 2.6950527183876873e-08, "-14": 3.5023828267583326e-09, "-15": 4.226849825519857e-10, "-16": 4.314007881771873e-11, "-2": 0.16809255070629445, "-3": 0.08932683459093577, "-4": 0.03750041768932093, "-5": 0.012952888593556209, "-6": 0.003791476594104413, "-7": 0.0009616097967067781, "-8": 0.00021497705417318925, "-9": 4.294392805290804e-05, "0": 0.24851104539450525, "1": 0.12955132568791097, "10": 4.1345705422635454e-08, "11": 4.031157948246295e-09, "12": 3.610911164861185e-10, "13": 2.990944694933918e-11, "14": 2.3031148081565657e-12, "15": 1.646947086679453e-13, "16": 9.959891734017629e-15, "2": 0.05901605535741224, "3": 0.018582943656551602, "4": 0.004622527738046208, "5": 0.0009460648482990512, "6": 0.00016408674900169546, "7": 2.465896621917454e-05, "8": 3.2664720702556274e-06, "9": 3.866334844273359e-07} |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 53.9% |
| Raw p over 1 5 | 80.0% |
| Raw p under 3 5 | 66.4% |
| Raw p btts yes | 56.8% |
| P home draw | 38.1% |
| P draw away | 83.0% |
| P home away | 78.8% |
| Raw p home draw | 46.1% |
| Raw p draw away | 78.7% |
| Raw p home away | 75.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5765 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:32Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.64, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:32Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.31, "price": 1.64, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 6.60 |
| Reference draw odds | 5.10 |
| Reference away odds | 1.53 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:56Z |
| Market reference home last update utc | 2026-11-01T09:33:56Z |
| Market reference draw last update utc | 2026-11-01T09:33:56Z |
| Market reference away last update utc | 2026-11-01T09:33:56Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.66 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:35Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:35Z |
| Home probability edge | +1.9% |
| Draw probability edge | +1.6% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -8.6% |
| Under 2.5 probability edge | +8.6% |
| Raw edge prob home | 0.0618 |
| Raw edge prob draw | 0.0529 |
| Raw edge prob away | -0.1146 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05913638003750737, 0.0990830678284404, 0.1005688634464548, 0.060359561005401026, 0.02717001425623518, 0.00978416227537463, 0.00293613609376052, 0.0007552346845368558, 0.00016997917814406832, 3.400611355984757e-05, 6.1229510276758476e-06, 1.0022403557561659e-06, 1.5038150432998601e-07, 2.082834955906581e-08, 2.678740274010508e-09, 3.215460162236949e-10, 3.6184863256591847e-11], [0.041727945783767866, 0.10650948168200518, 0.10970492929622275, 0.06584285777450524, 0.029638243794458615, 0.010672993547493268, 0.0032028660912687317, 0.000823843134244862, 0.0001854207463531042, 3.709536088879713e-05, 6.679183661382944e-06, 1.093287759233668e-06, 1.6404274379380286e-07, 2.272047766504689e-08, 2.9220874363339198e-09, 3.5075650421448647e-10, 3.947203666342948e-11], [0.02797927595260272, 0.050377922824410906, 0.047388922417623935, 0.035912139251027694, 0.01616534844140129, 0.005821284850903153, 0.0017469134384469958, 0.0004493421208922747, 0.00010113254327245366, 2.0232623717031838e-05, 3.642973313100179e-06, 5.963031310929236e-07, 8.947251163397689e-08, 1.2392247015635549e-08, 1.59377059964027e-09, 1.9131029314817694e-10, 2.1528914829812028e-11], [0.010173673987986815, 0.018318149614584275, 0.016491318952156348, 0.010341908923238965, 0.005877957143123599, 0.00211670431946206, 0.0006352032782442161, 0.00016338736766357642, 3.6773271995060415e-05, 7.356877925196776e-06, 1.3246383822512673e-06, 2.1682454056466875e-07, 3.2533513940547945e-08, 4.506002275729039e-09, 5.795183020406231e-10, 6.956322087579563e-11, 7.828228334595899e-12], [0.002774472503930485, 0.004995560353964699, 0.004497363591592687, 0.0026992339653389764, 0.001269542110899448, 0.0005772484886220028, 0.000173226902294696, 4.4557527556657634e-05, 1.002847468380901e-05, 2.0063013167449315e-06, 3.6124341840978817e-07, 5.913043082414261e-08, 8.8722461512796e-09, 1.2288362524119256e-09, 1.580409984077302e-10, 1.89706534564245e-11, 2.1348437442041215e-12], [0.0006053032707087585, 0.0010898752887239281, 0.0009811843107837665, 0.0005888885708231878, 0.00026507997404368587, 9.974094698747743e-05, 3.7792701273911506e-05, 9.721061256340451e-06, 2.187900048650715e-06, 4.3771230290895826e-07, 7.881203449509335e-08, 1.2900413727498342e-08, 1.935647084732217e-09, 2.680937013059939e-10, 3.4479611207808044e-11, 4.1388042477943675e-12, 4.657562469940644e-13], [0.00011004856148681341, 0.00019814729826861025, 0.00017838648357004744, 0.00010706424899907538, 4.8193477937616164e-05, 1.7354897362562577e-05, 5.441734782296283e-06, 1.7673600311672358e-06, 3.9777623000287593e-07, 7.957929786800702e-08, 1.4328604261263312e-08, 2.345389562547081e-09, 3.519147963160712e-10, 4.874139559473084e-11, 6.268645483446551e-12, 7.524648813015119e-13, 8.467789200143849e-14], [1.714939998514373e-05, 3.087825254663736e-05, 2.7798829147372228e-05, 1.6684340125737828e-05, 7.510222929414787e-06, 2.7044976558586337e-06, 8.115945912756444e-07, 2.181261210367697e-07, 6.19873952075171e-08, 1.2401227160419338e-08, 2.232895754250124e-09, 3.654934075073828e-10, 5.4840586021088973e-11, 7.59560758991222e-12, 9.768733667052178e-13, 1.1726024447634045e-13, 1.3195765762058403e-14], [2.3384147542898863e-06, 4.21041910529215e-06, 3.790522833831622e-06, 2.275001291556215e-06, 1.0240600908115428e-06, 3.687730898387602e-07, 1.1066537420463176e-07, 2.8465413832212183e-08, 6.694129154460807e-09, 1.6909753453967275e-09, 3.0446758376695327e-10, 4.9837030884540706e-11, 7.477814710526933e-12, 1.0357027576144743e-12, 1.3320204180643065e-13, 1.5989077519484746e-14, 1.7993150418604625e-15], [2.83427269516012e-07, 5.103233240988474e-07, 4.594298487298246e-07, 2.7574124865072807e-07, 1.241210759667717e-07, 4.469709649763256e-08, 1.3413182919430977e-08, 3.450146943909963e-09, 7.765177553540517e-10, 1.6232127796949204e-10, 3.690295563047391e-11, 6.040491131215073e-12, 9.063476021365279e-13, 1.2553222394887626e-13, 1.6144736913712687e-14, 1.9379541525359475e-15, 2.18085755907089e-16], [3.091749026221256e-08, 5.566830753564697e-08, 5.0116623917416224e-08, 3.007906537930215e-08, 1.3539671620486796e-08, 4.87575542069236e-09, 1.463168851059883e-09, 3.763571681853022e-10, 8.470596418118383e-11, 1.694631465214104e-11, 3.1881726966552197e-12, 6.589232787911844e-13, 9.886837357282843e-14, 1.369360583461432e-14, 1.761138747051636e-15, 2.1140054286928664e-16, 2.3789751233530364e-17], [3.0660140967519557e-09, 5.5204938757665605e-09, 4.969946593634603e-09, 2.9828694919257113e-09, 1.3426970851040259e-09, 4.835170877510846e-10, 1.450989807138674e-10, 3.732244672136609e-11, 8.400089336355147e-12, 1.680525785592675e-12, 3.025860943451062e-13, 5.17514893452997e-14, 9.80454184755478e-15, 1.357962375607384e-15, 1.7464794777976823e-16, 2.096408987279372e-17, 2.359173141856648e-18], [2.7871189300758766e-10, 5.018330803115579e-10, 4.517863191581326e-10, 2.7115374439077613e-10, 1.2205607492853884e-10, 4.3953471372288695e-11, 1.3190027935969123e-11, 3.392746885412748e-12, 7.635988376076277e-13, 1.5276593915428778e-13, 2.7506182454294116e-14, 4.502372461232953e-15, 7.058732850243327e-16, 1.2344374565647482e-16, 1.5876137095115092e-17, 1.905712429638655e-18, 2.1445746547482992e-19], [2.3387012539379358e-11, 4.2109349605695736e-11, 3.790987243943567e-11, 2.2752800218662028e-11, 1.024185557371767e-11, 3.688182714560311e-12, 1.106789327877286e-12, 2.846890137907681e-13, 6.40743938031339e-14, 1.2818753071632033e-14, 2.3080731397117675e-15, 3.777988806704591e-16, 5.668696504097938e-17, 8.20363682468481e-18, 1.332183615538266e-18, 1.5991036481244444e-19, 1.7995354916866863e-20], [1.822255680022886e-12, 3.281051881758853e-12, 2.953839455355164e-12, 1.7728394922211447e-12, 7.980189629502958e-13, 2.8737368183529907e-13, 8.623816898020187e-14, 2.2182233474532877e-14, 4.992511457168035e-15, 9.988041677516535e-16, 1.798391043604255e-16, 2.943711408410194e-17, 4.4169020671301515e-18, 6.117559511871636e-19, 8.220850292008322e-20, 1.2459803067337041e-20, 1.4021516282198327e-21], [1.3251976386176273e-13, 2.3860769120138763e-13, 2.1481184632900031e-13, 1.2892607412314545e-13, 5.803427350329556e-14, 2.0898654823466306e-14, 6.271491928609936e-15, 1.6131569099758093e-15, 3.6307003821370656e-16, 7.263596097169594e-17, 1.3078425768800559e-17, 2.1407530512666397e-18, 3.212100394875807e-19, 4.44886823957288e-20, 5.721702765413266e-21, 7.176300338064963e-22, 1.0196856824600197e-22], [9.03489834390148e-15, 1.6267733742163767e-14, 1.464538675659611e-14, 8.789888690082607e-15, 3.956645758223703e-15, 1.4248231082819315e-15, 4.275761621390781e-16, 1.0998139650774798e-16, 2.475329559445255e-17, 4.952155847300184e-18, 8.916575450785957e-19, 1.4595171040122712e-19, 2.189937537798649e-20, 3.0331379349484927e-21, 3.9009277811160435e-22, 4.682528574210255e-23, 5.505883601408474e-24]] |
| Legacy trial inputs | {"lambda_home": 1.0908438808660912, "lambda_away": 1.8005441924141217, "rho": -0.10361560184068906, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1843 |
| Legacy p draw | 0.2248 |
| Legacy p away | 0.5909 |
| Legacy p over 1 5 | 0.8001 |
| Legacy p under 3 5 | 0.6656 |
| Legacy p btts yes | 0.5566 |
| Legacy p over 2 5 | 0.5650 |
| Legacy goal margin distribution | {"-1": 0.25119496578468387, "-10": 7.310379565299769e-06, "-11": 1.1792743012773484e-06, "-12": 1.747674506592932e-07, "-13": 2.3949575516882506e-08, "-14": 3.051025693054806e-09, "-15": 3.6101805288712437e-10, "-16": 3.6184863256591847e-11, "-2": 0.18487713243343995, "-3": 0.0965011202195632, "-4": 0.03976378949852854, "-5": 0.013475231274164147, "-6": 0.0038688431526807377, "-7": 0.0009622738088016281, "-8": 0.00021094348361408793, "-9": 4.1315397947788254e-05, "0": 0.2247516428388568, "1": 0.11157969725085667, "10": 3.691334260254985e-08, "11": 3.6075893480917817e-09, "12": 3.239079647885199e-10, "13": 2.6891666156157294e-11, "14": 2.0755087579808696e-12, "15": 1.487874976039265e-13, "16": 9.03489834390148e-15, "2": 0.05143468990713187, "3": 0.01626537569584889, "4": 0.004060488874805405, "5": 0.0008336535448044987, "6": 0.00014500711478442435, "7": 2.1850715784441067e-05, "8": 2.901963403931798e-06, "9": 3.443472130004132e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2176 |
| Legacy raw p draw | 0.2539 |
| Legacy raw p away | 0.5286 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0908 |
| Legacy lambda away | 1.8005 |
| Legacy model home team | Excelsior |
| Legacy model away team | Twente |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Market p home draw | 36.8% |
| Market reference home draw last update utc | 2026-11-01T09:33:41Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.4% |
| Market reference draw away last update utc | 2026-11-01T09:33:41Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.8% |
| Market reference home away last update utc | 2026-11-01T09:33:41Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.13 |
| Market reference dc home draw odds | 2.56 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 86.0% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-11-01T09:33:56Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 56.7% |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.15 |
| Market reference under 3 5 last update utc | 2026-11-01T09:33:56Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 59.0% |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-11-01T09:33:56Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,409.2021 |
| Elo away rating | 1,577.6366 |
| Elo rating diff | -108.4345 |
| Elo home expectancy | 0.3488 |

</details>


---

## 2026-11-01 — FC Zwolle vs ADO Den Haag

The model's most likely 1X2 outcome is **FC Zwolle win** at **42.4%**. Expected goals are 1.76 for FC Zwolle and 1.48 for ADO Den Haag (3.24 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 62.6%; Under 3.5 goals: 59.5%; Double Chance 1X: 67.8%; Double Chance X2: 57.6%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 77.5%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Zwolle win | 42.4% | 2.36 |
| Draw | 25.4% | 3.93 |
| ADO Den Haag win | 32.2% | 3.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Zwolle expected goals | 1.76 |
| ADO Den Haag expected goals | 1.48 |
| Expected total goals | 3.24 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 84.3% |
| Under 1.5 | 15.7% |
| Over 2.5 | 62.6% |
| Under 2.5 | 37.4% |
| Over 3.5 | 40.5% |
| Under 3.5 | 59.5% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.38% |
| 2 | 2-1 | 8.77% |
| 3 | 1-2 | 7.69% |
| 4 | 2-2 | 6.75% |
| 5 | 2-0 | 5.93% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T11:15:00+00:00 |
| Fixture id | 016bdfefaa570d0fcaeffc5a1cb3625f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 10.00 |
| Matched home-team name | Zwolle |
| Matched away-team name | Den Haag |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.7583 |
| Dc lambda away | 1.4786 |
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
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.05 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.37 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.47 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.44 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.16767423516343385, "-10": 6.959420068012236e-07, "-11": 9.177037305098511e-08, "-12": 1.1124970532027544e-08, "-13": 1.2477135372111127e-09, "-14": 1.3010589396391399e-10, "-15": 1.2556056854666446e-11, "-16": 9.981580645319366e-13, "-2": 0.0963305182482202, "-3": 0.03978388247210071, "-4": 0.013128725164946503, "-5": 0.0035888567249554026, "-6": 0.0008349596835881492, "-7": 0.00016879905142299915, "-8": 3.0140280122597203e-05, "-9": 4.8158220033777e-06, "0": 0.2542326775257229, "1": 0.1930603540580191, "10": 3.775291135642242e-06, "11": 5.920073013633558e-07, "12": 8.534353030372325e-08, "13": 1.138239860435248e-08, "14": 1.4114420210833522e-09, "15": 1.6198190943629176e-10, "16": 1.5312980489956843e-11, "2": 0.1306664055966155, "3": 0.06417330104249709, "4": 0.02518354951926441, "5": 0.008186488847861814, "6": 0.0022649271012051947, "7": 0.0005445100412480496, "8": 0.00011561930226275396, "9": 2.1968512682569548e-05} |
| Raw goal margin distribution | {"-1": 0.16465227067048047, "-10": 6.833991612551675e-07, "-11": 9.011641107766912e-08, "-12": 1.0924467062307397e-08, "-13": 1.2252262063271874e-09, "-14": 1.2776101735541373e-10, "-15": 1.2329761157242678e-11, "-16": 9.801684298905113e-13, "-2": 0.09459436954624358, "-3": 0.03906686426053508, "-4": 0.01289210836304166, "-5": 0.0035241753648016425, "-6": 0.0008199113458731058, "-7": 0.00016575681455609285, "-8": 2.9597066931558174e-05, "-9": 4.72902725471279e-06, "0": 0.24995081428471175, "1": 0.19764634073396822, "10": 3.864970007984313e-06, "11": 6.060699379381393e-07, "12": 8.737079423764162e-08, "13": 1.1652777930002195e-08, "14": 1.4449696416771572e-09, "15": 1.658296537442525e-10, "16": 1.567672748937914e-11, "2": 0.13377027639382824, "3": 0.0656976839483946, "4": 0.025781763601653084, "5": 0.00838095201955898, "6": 0.0023187285435510505, "7": 0.0005574444202730338, "8": 0.00011836574174923794, "9": 2.2490356263268703e-05} |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 84.3% |
| Raw p under 3 5 | 59.4% |
| Raw p btts yes | 64.9% |
| P home draw | 67.8% |
| P draw away | 57.6% |
| P home away | 74.6% |
| Raw p home draw | 68.4% |
| Raw p draw away | 56.6% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.6261 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:32Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.73, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:32Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.15, "price": 1.73, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 2.36 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:56Z |
| Market reference home last update utc | 2026-11-01T09:33:56Z |
| Market reference draw last update utc | 2026-11-01T09:33:56Z |
| Market reference away last update utc | 2026-11-01T09:33:56Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:56Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:56Z |
| Home probability edge | +0.4% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +1.4% |
| Under 2.5 probability edge | -1.4% |
| Raw edge prob home | 0.0144 |
| Raw edge prob draw | -0.0061 |
| Raw edge prob away | -0.0083 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05042128510359444, 0.04858414830830164, 0.04453948947432236, 0.022349901575103026, 0.008411380097398266, 0.0025324967058189475, 0.0006354030185612862, 0.0001366478706518432, 2.571369667312432e-05, 4.301041589229892e-06, 6.474783882186061e-07, 8.86103040418567e-08, 1.1116155557963922e-08, 1.287249993275468e-09, 1.3841606463876557e-10, 1.3891427394438385e-11, 1.3070088420455766e-12], [0.05746815734921375, 0.11396970439036375, 0.07692108336855301, 0.038598975036042676, 0.014526714997251404, 0.004373700564107082, 0.001097360772210031, 0.00023599512196037804, 4.440835377440466e-05, 7.428032574273234e-06, 1.1182153111165065e-06, 1.5303275059867964e-07, 1.9197946328165813e-08, 2.2231207680545163e-09, 2.390488479613966e-10, 2.3990927092503535e-11, 2.257244914322255e-12], [0.05879577932660195, 0.08851110979203859, 0.06712176864114375, 0.033330815100606946, 0.012544044269063607, 0.003776758441682686, 0.0009475880891406619, 0.00020378545718795826, 3.8347303968431355e-05, 6.414221622807362e-06, 9.65596307743645e-07, 1.321461595749365e-07, 1.6577725154047877e-08, 1.9196993494556077e-09, 2.0642239707076143e-10, 2.0716538567816825e-11, 1.9491660803378135e-12], [0.03384737975729723, 0.05095381301486532, 0.038352910614803455, 0.019389770760979724, 0.0072213181784503136, 0.0021741930916012904, 0.0005455046990443431, 0.00011731460722954412, 2.2075662147074412e-05, 3.692520068636965e-06, 5.558716168875735e-07, 7.60735089802198e-08, 9.543415619754931e-09, 1.1051268244940476e-09, 1.1883263295575505e-10, 1.1926035443233503e-11, 1.1220901446812987e-12], [0.014613869348565012, 0.021999704897390653, 0.016559167323464494, 0.008309384867522092, 0.0031506813660933585, 0.0009387247700426149, 0.00023552589470810125, 5.065149370568818e-05, 9.531338753950525e-06, 1.5942742462474108e-06, 2.4000189208203727e-07, 3.284532891749588e-08, 4.120443886829535e-09, 4.771470980192697e-10, 5.13069131145074e-11, 5.149158518723902e-12, 4.844711433873877e-13], [0.005047721362617679, 0.007598834896710488, 0.00571963938175073, 0.0028701132127010504, 0.0010801664192331961, 0.0003276545990940667, 8.135210886393098e-05, 1.7495340948275466e-05, 3.2921836849038258e-06, 5.506722400966627e-07, 8.289814619494461e-08, 1.134498088662111e-08, 1.4232269452346773e-09, 1.6480957522857553e-10, 1.772172688840267e-11, 1.7785513770875235e-12, 1.6733934604995355e-13], [0.0014529286270744339, 0.00218723736131849, 0.0016463325126920994, 0.0008261291283945571, 0.00031091349933280065, 9.360977672362076e-05, 2.36627687776703e-05, 5.035832978505533e-06, 9.476172668341597e-07, 1.5850468048750077e-07, 2.386127939430781e-08, 3.265522464424623e-09, 4.096595320948546e-10, 4.743854358501991e-11, 5.100995571594347e-12, 5.1193558931966e-13, 4.816670906450501e-14], [0.0003584647029629785, 0.0005396324199443244, 0.0004061810636416306, 0.00020382152784429103, 7.670818311972243e-05, 2.3095285055557228e-05, 5.794603327663144e-06, 1.2555131693651674e-06, 2.337949268452912e-07, 3.9106073175529056e-08, 5.887024504169946e-09, 8.056655491646096e-10, 1.0107067873252919e-10, 1.1703977138533798e-11, 1.2585111397170925e-12, 1.263040974911206e-13, 1.1883629199514319e-14], [7.738496115114702e-05, 0.00011649524627701997, 8.768591599236319e-05, 4.4000764604226225e-05, 1.655967720567416e-05, 4.985784435751109e-06, 1.2509325177375445e-06, 2.6902180172991606e-07, 5.100269101123414e-08, 8.442175557169908e-09, 1.2708842984691073e-09, 1.7392618215289068e-10, 2.1819025646284082e-11, 2.5266415596653344e-12, 2.716859842832314e-13, 2.7266388006382024e-14, 2.565424646660477e-15], [1.4849581594606547e-05, 2.2354545886449043e-05, 1.682625596571889e-05, 8.4434098627941e-06, 3.1776752767984003e-06, 9.567338626325336e-07, 2.400443731593827e-07, 5.1623224152219415e-08, 9.71419401419681e-09, 1.6370421613690675e-09, 2.438729671332475e-10, 3.337510279643617e-11, 4.1869039775890084e-12, 4.848431716246743e-13, 5.21344603875276e-14, 5.232211110116578e-15, 4.922853491002206e-16], [2.5645689191955833e-06, 3.860699590616156e-06, 2.905946729959383e-06, 1.4582031398120972e-06, 5.487944019334051e-07, 1.6523091323599972e-07, 4.14564097116334e-08, 8.915491344047965e-09, 1.677671514522225e-09, 2.8061834316371165e-10, 4.256098370148319e-11, 5.763984039643621e-12, 7.230913369627256e-13, 8.373392345845386e-14, 9.003783431679185e-15, 9.036191293462722e-16, 8.501921065145166e-17], [4.0264457035995525e-07, 6.061407499394037e-07, 4.562418517262625e-07, 2.289420152964126e-07, 8.616227254744039e-08, 2.5941720486482423e-08, 6.5087735221569595e-09, 1.3997573451440258e-09, 2.6339917056384634e-10, 4.4057873185843664e-11, 6.632468002667584e-12, 9.144881438989006e-13, 1.1352738408515284e-13, 1.314646269910257e-14, 1.4136194525042e-15, 1.418707578421366e-16, 1.3348256421915088e-17], [5.7948307838914334e-08, 8.723532702750257e-08, 6.56619888086269e-08, 3.294916498637427e-08, 1.2400410340106959e-08, 3.7335131659117025e-09, 9.367378563643427e-10, 2.0145203861478561e-10, 3.790821320824769e-11, 6.340776421792357e-12, 9.545398742288734e-13, 1.3063303735620432e-13, 1.6510771982776475e-14, 1.892029158121652e-15, 2.0344706282158254e-16, 2.041793421286337e-17, 1.9210711609954186e-18], [7.698348435292181e-09, 1.1589086349013189e-08, 8.723099735858238e-09, 4.3772486579271695e-09, 1.6473764825732635e-09, 4.959917952882469e-10, 1.244442621321674e-10, 2.676261040387283e-11, 5.036051003381696e-12, 8.423629276791883e-13, 1.2680923432002523e-13, 1.7354409062714084e-14, 2.1771092294925657e-15, 2.5399926952558597e-16, 2.7027646468833673e-17, 2.712492870998737e-18, 2.5521151035928305e-19], [9.496633674013018e-10, 1.429622322218339e-09, 1.0760760361736126e-09, 5.399746108377044e-10, 2.0321931528146803e-10, 6.118523245291074e-11, 1.5351365039340293e-11, 3.3014186003944338e-12, 6.212440492237412e-13, 1.0391335507840984e-13, 1.564310650448823e-14, 2.1408288658645544e-15, 2.68566810070853e-16, 3.11000167868325e-17, 3.369210835963517e-18, 3.3461139562292604e-19, 3.148272962240509e-20], [1.0933987781494465e-10, 1.6460014716648147e-10, 1.2389445181693915e-10, 6.217019630201012e-11, 2.339773846738565e-11, 7.044586608396828e-12, 1.7674856536661433e-12, 3.8011017248238673e-13, 7.152718612413461e-14, 1.1964106374562381e-14, 1.801075425839959e-15, 2.464852016529579e-16, 3.092154884172514e-17, 3.580713073960288e-18, 3.850287161680312e-19, 3.8931170663281405e-20, 3.624776871845034e-21], [1.1802085570827477e-11, 1.776684829589311e-11, 1.3373098189930679e-11, 6.7106163951756095e-12, 2.5255388708526973e-12, 7.603887586569164e-13, 1.9078141796612286e-13, 4.102888051120501e-14, 7.720604670020571e-15, 1.291398984824622e-15, 1.9440707928404497e-16, 2.6605475513466017e-17, 3.337654776148664e-18, 3.865001767697595e-19, 4.1559785379784404e-20, 4.1709374026663966e-21, 3.953750777956702e-22]] |
| Legacy trial inputs | {"lambda_home": 1.7270310970425267, "lambda_away": 1.5053990406415452, "rho": -0.10361560184068906, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4203 |
| Legacy p draw | 0.2544 |
| Legacy p away | 0.3253 |
| Legacy p over 1 5 | 0.8435 |
| Legacy p under 3 5 | 0.5954 |
| Legacy p btts yes | 0.6507 |
| Legacy p over 2 5 | 0.6262 |
| Legacy goal margin distribution | {"-1": 0.16708272015465178, "-10": 8.182471244270283e-07, "-11": 1.0985209885029866e-07, "-12": 1.355810922967582e-08, "-13": 1.5481374699493626e-09, "-14": 1.6435615781160693e-10, "-15": 1.614867230876064e-11, "-16": 1.3070088420455766e-12, "-2": 0.09811071113502216, "-3": 0.041252987960375284, "-4": 0.01386009005812756, "-5": 0.00385739913892929, "-6": 0.0009136897330722136, "-7": 0.00018806063494661892, "-8": 3.4187689547448576e-05, "-9": 5.561441868185216e-06, "0": 0.25440583582644155, "1": 0.19382141244624176, "10": 3.240959361284849e-06, "11": 4.991671298613799e-07, "12": 7.0678165959274e-08, "13": 9.258575825722635e-09, "14": 1.127636612757714e-09, "15": 1.2710672611083775e-10, "16": 1.1802085570827477e-11, "2": 0.1295141859404646, "3": 0.06247479636212207, "4": 0.024080417591813726, "5": 0.0076884901737394136, "6": 0.0020892660731302044, "7": 0.0004933344319497421, "8": 0.00010288730792418308, "9": 1.9201182572164904e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4207 |
| Legacy raw p draw | 0.2527 |
| Legacy raw p away | 0.3266 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7270 |
| Legacy lambda away | 1.5054 |
| Legacy model home team | Zwolle |
| Legacy model away team | Den Haag |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 90/100 |
| Market p home draw | 67.4% |
| Market reference home draw last update utc | 2026-11-01T09:33:41Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.3% |
| Market reference draw away last update utc | 2026-11-01T09:33:41Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.3% |
| Market reference home away last update utc | 2026-11-01T09:33:41Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.62 |
| Market reference dc home draw odds | 1.40 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 82.8% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-11-01T09:33:56Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.3% |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market reference under 3 5 last update utc | 2026-11-01T09:33:56Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 63.8% |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.70 |
| Market reference btts yes last update utc | 2026-11-01T09:33:56Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,408.9706 |
| Elo away rating | 1,360.6524 |
| Elo rating diff | 108.3181 |
| Elo home expectancy | 0.6510 |

</details>


---

## 2026-11-01 — Groningen vs Sparta Rotterdam

The model's most likely 1X2 outcome is **Groningen win** at **52.2%**. Expected goals are 1.67 for Groningen and 1.21 for Sparta Rotterdam (2.89 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 56.1%; Under 3.5 goals: 66.9%; Double Chance 1X: 76.1%; Double Chance X2: 47.8%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Groningen win | 52.2% | 1.91 |
| Draw | 23.8% | 4.20 |
| Sparta Rotterdam win | 23.9% | 4.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Groningen expected goals | 1.67 |
| Sparta Rotterdam expected goals | 1.21 |
| Expected total goals | 2.89 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 79.7% |
| Under 1.5 | 20.3% |
| Over 2.5 | 56.1% |
| Under 2.5 | 43.9% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.24% |
| 2 | 2-1 | 10.52% |
| 3 | 1-0 | 9.15% |
| 4 | 2-0 | 8.66% |
| 5 | 1-2 | 6.17% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T15:45:00+00:00 |
| Fixture id | 961d9c9f07b1f911e211cd6a750cddba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Groningen |
| Matched away-team name | Sparta Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6733 |
| Dc lambda away | 1.2144 |
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
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.59 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.93 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.85 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.13747956030803415, "-10": 1.1543950524168846e-07, "-11": 1.255392682360624e-08, "-12": 1.2543013958296926e-09, "-13": 1.1585000214141022e-10, "-14": 9.879587462733908e-12, "-15": 7.04431491060346e-13, "-2": 0.06909949248672817, "-3": 0.024226696358144603, "-4": 0.006714571007477083, "-5": 0.001531738638243201, "-6": 0.00029618724326978935, "-7": 4.963246398935283e-05, "-8": 7.3318911634288836e-06, "-9": 9.678703346057682e-07, "0": 0.23820276455584186, "1": 0.23898320539259799, "10": 3.5245551290604988e-06, "11": 5.281356711905758e-07, "12": 7.270828010876799e-08, "13": 9.253245180937205e-09, "14": 1.0873087709597857e-09, "15": 1.0682401599058231e-10, "2": 0.16236643273463502, "3": 0.07843892718083663, "4": 0.029955169221345685, "5": 0.00941573509612516, "6": 0.0025087187224463294, "7": 0.0005792519639767964, "8": 0.0001179054135265477, "9": 2.144623065747539e-05} |
| Raw goal margin distribution | {"-1": 0.1532140192844941, "-10": 1.2865149221210384e-07, "-11": 1.3990716744645644e-08, "-12": 1.397855490799004e-09, "-13": 1.2910897025297967e-10, "-14": 1.1010300735953842e-11, "-15": 7.850532822050169e-13, "-2": 0.07700789085075092, "-3": 0.026999428240093323, "-4": 0.007483049913177376, "-5": 0.0017070452708225884, "-6": 0.0003300857080171116, "-7": 5.53128718026404e-05, "-8": 8.171022016570689e-06, "-9": 1.0786425544198653e-06, "0": 0.2627944156989977, "1": 0.21519812171686598, "10": 3.173769648019198e-06, "11": 4.755723493840476e-07, "12": 6.547190329532362e-08, "13": 8.332305106762969e-09, "14": 9.790930908823903e-10, "15": 9.619223056976281e-11, "2": 0.14620672317521582, "3": 0.07063220099953055, "4": 0.026973845888268958, "5": 0.008478623022655582, "6": 0.0022590355506341667, "7": 0.0005216012332072989, "8": 0.00010617073902528426, "9": 1.931176940996171e-05} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 58.2% |
| P home draw | 76.1% |
| P draw away | 47.8% |
| P home away | 76.2% |
| Raw p home draw | 73.3% |
| Raw p draw away | 53.0% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5614 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:32Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.85, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:32Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 2.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.82 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.30 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:56Z |
| Market reference home last update utc | 2026-11-01T09:33:56Z |
| Market reference draw last update utc | 2026-11-01T09:33:56Z |
| Market reference away last update utc | 2026-11-01T09:33:56Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.66 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:35Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:35Z |
| Home probability edge | -2.2% |
| Draw probability edge | +1.1% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | -0.0743 |
| Raw edge prob draw | 0.0351 |
| Raw edge prob away | 0.0391 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.05755195479999797, 0.04697661705420426, 0.03491055181728909, 0.01407940261395141, 0.004258660368716315, 0.0010305089574242973, 0.00020780179277593924, 3.591699707754769e-05, 5.431987997341742e-06, 7.302390636217387e-07, 8.835148039172734e-08, 9.717843818402474e-09, 9.798000069926446e-10, 9.118908442044794e-11, 7.880678108886597e-12, 6.356544608442318e-13, 4.806731746403499e-14], [0.08128356021958465, 0.11258863214349853, 0.06265556060950764, 0.02526894643318746, 0.007643212122338011, 0.0018495014567074934, 0.00037295136124400135, 6.446187385068236e-05, 9.749036766271098e-06, 1.3105933744514172e-06, 1.585684340825027e-07, 1.744105780808957e-08, 1.7584917890905673e-09, 1.636612115366602e-10, 1.4143812663849979e-11, 1.140838071153193e-12, 8.62686083699423e-14], [0.08339661716250911, 0.10090140274646461, 0.05538196947773567, 0.022675665699430386, 0.006858810810107385, 0.001659692336354304, 0.00033467641447090227, 5.7846333469493346e-05, 8.748520607613387e-06, 1.17609087128054e-06, 1.4229500273167643e-07, 1.5651131215397965e-08, 1.5780227343487652e-09, 1.468651227933661e-10, 1.269227304465721e-11, 1.0237570761825227e-12, 7.741510430299078e-14], [0.04989190497093719, 0.06036411749713005, 0.03651721339694193, 0.013362187526392006, 0.004103273595434873, 0.0009929085272730545, 0.00020021967838645927, 3.4606484897981374e-05, 5.233789734430045e-06, 7.035946538787644e-07, 8.5127778508018e-08, 9.36326649514677e-09, 9.440498066089462e-10, 8.786184619063494e-11, 7.593133896249913e-12, 6.124611824325249e-13, 4.6313473598978785e-14], [0.0223858197099754, 0.027084559149017827, 0.01638477736800846, 0.006607969948785068, 0.0018134653238318422, 0.0004455045621725489, 8.983584862833797e-05, 1.5527459458071787e-05, 2.3483303245911357e-06, 3.156933590691215e-07, 3.8195677296773564e-08, 4.201170425921935e-09, 4.2358231821966924e-10, 3.9422416308915624e-11, 3.406935985590623e-12, 2.7480300897068177e-13, 2.0780226185658302e-14], [0.008035370457462975, 0.009721978880337616, 0.005881301543598816, 0.0023719250489009237, 0.0007174468605159763, 0.00015751463923978126, 3.2246499500198815e-05, 5.573568027676266e-06, 8.429311215338466e-07, 1.1331785585456488e-07, 1.3710305047106127e-08, 1.5080064596507623e-09, 1.5204450362875505e-10, 1.4150641945414616e-11, 1.2229167001145511e-12, 9.864030035589775e-14, 7.459044062488822e-15], [0.0024035743469594997, 0.002908079865410388, 0.0017592400489511043, 0.0007095003560357238, 0.00021460577062022492, 5.1930219785464594e-05, 9.501017061699451e-06, 1.6671894847006255e-06, 2.5214115897927655e-07, 3.3896121258668374e-08, 4.101085030822362e-09, 4.51081336032165e-10, 4.54802016226705e-11, 4.232800485436034e-12, 3.6580406895038823e-13, 2.950570813964345e-14, 2.2311811330101716e-15], [0.0006162577965520804, 0.0007456090935245254, 0.0004510554864026636, 0.00018191038135208516, 5.50232529720078e-05, 1.3314505066148011e-05, 2.68486557320695e-06, 4.2104226553234483e-07, 6.464703504978578e-08, 8.690702255560841e-09, 1.0514863531325145e-09, 1.1565375148915024e-10, 1.1660770499646016e-11, 1.0852571728014617e-12, 9.378932246731539e-14, 7.565034427517064e-15, 5.720575152904106e-16], [0.00013825324906432845, 0.0001672723335727612, 0.00010119123336428116, 4.081035793975774e-05, 1.2344092910515675e-05, 2.9870187369270214e-06, 6.023313471628457e-07, 1.0410850140782914e-07, 1.4285564150750156e-08, 1.9496999960152766e-09, 2.3589381827007283e-10, 2.5946133256753297e-11, 2.616014624381781e-12, 2.4347007218348345e-13, 2.1040997178771676e-14, 1.697164067926477e-15, 1.2833721631281977e-16], [2.7569935084216092e-05, 3.335681012343207e-05, 2.0179169414289127e-05, 8.13824576838135e-06, 2.461611879067649e-06, 5.956598722254784e-07, 1.2011461757937636e-07, 2.0760919869545714e-08, 3.139824504305298e-09, 3.8296938095502567e-10, 4.704104460827317e-11, 5.174078832984736e-12, 5.216756485773949e-13, 4.8551872237915914e-14, 4.195915323885027e-15, 3.3844197873588947e-16, 2.559251769184182e-17], [4.9481020744387375e-06, 5.986698948120003e-06, 3.6216476293576208e-06, 1.460608109733059e-06, 4.4179671834813086e-07, 1.0690579576686029e-07, 2.155751860131109e-08, 3.7260570385806705e-09, 5.63518633455947e-10, 7.575556489256795e-11, 8.316023897489015e-12, 9.286155418428428e-13, 9.362750949630593e-14, 8.713826093694883e-15, 7.530600726793519e-16, 6.07417265200217e-17, 4.593205950405423e-18], [8.073258742399877e-07, 9.767819841612359e-07, 5.909032987950178e-07, 2.3831091221900732e-07, 7.208297575737054e-08, 1.7442610061473308e-08, 3.517296589566091e-09, 6.079386016872766e-10, 9.19429645066386e-11, 1.2360179061660497e-11, 1.4954556287202532e-12, 1.4923889826333877e-13, 1.5276142209655584e-14, 1.4217364887051986e-15, 1.228682982656634e-16, 9.910540794812764e-18, 7.494214859938988e-19], [1.2074538263246168e-07, 1.4608960048143318e-07, 8.837675985419853e-08, 3.56422891914168e-08, 1.0780883862174951e-08, 2.6087540275655178e-09, 5.260543927677508e-10, 9.092459615130974e-11, 1.3751186211104644e-11, 1.8486147884346055e-12, 2.236635389268089e-13, 2.4600915904578615e-14, 2.2504595850782258e-15, 2.1263794684253025e-16, 1.8376445201206118e-17, 1.4822416555034978e-18, 1.1208507861154256e-19], [1.6669788372385768e-08, 2.0168744098850252e-08, 1.2201061868270405e-08, 4.920680236169603e-09, 1.4883803300103172e-09, 3.6015768559447077e-10, 7.262567900004117e-11, 1.2552809413015925e-11, 1.8984524212088318e-12, 2.5521487143793154e-13, 3.08783969974054e-14, 3.396337424715186e-15, 3.4243516305372857e-16, 2.8915865057202747e-17, 2.5370034519108353e-18, 2.0463436510188559e-19, 1.5474169690148624e-20], [2.1370021410719057e-09, 2.585554678868776e-09, 1.5641287551698526e-09, 6.308120994291711e-10, 1.9080457897295682e-10, 4.61708168121593e-11, 9.310330044560525e-12, 1.6092214245814911e-12, 2.433742287674755e-13, 3.271755552696284e-14, 3.958490595215614e-15, 4.353972699762738e-16, 4.3898858238438005e-17, 4.085626312815747e-18, 3.2035521182756466e-19, 2.623333101720912e-20, 1.983728468559129e-21], [2.5569168480128545e-10, 3.0936086552267013e-10, 1.8714755075299664e-10, 7.547648427491846e-11, 2.2829712393701187e-11, 5.5243248064463675e-12, 1.1139782826589159e-12, 1.9254287553646457e-13, 2.911965570589263e-14, 3.914646005489076e-15, 4.736322487038007e-16, 5.209515675181892e-17, 5.252485623719981e-18, 4.8884400034729365e-19, 4.224652804314827e-20, 3.0917256687433832e-21, 2.373525344526506e-22], [2.868134600510682e-11, 3.470150400624376e-11, 2.0992640653631463e-11, 8.466318184810432e-12, 2.5608454215853614e-12, 6.196723657299257e-13, 1.2495672900722516e-13, 2.159784288007396e-14, 3.2663984419335753e-15, 4.391121152735156e-16, 5.312808828651522e-17, 5.843597210251101e-18, 5.891797290077723e-19, 5.483441484371183e-20, 4.7388607465341106e-21, 3.822358851908007e-22, 2.6224828831324043e-23]] |
| Legacy trial inputs | {"lambda_home": 1.7947456384369764, "lambda_away": 1.2098980291951789, "rho": -0.10361560184068906, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5222 |
| Legacy p draw | 0.2409 |
| Legacy p away | 0.2369 |
| Legacy p over 1 5 | 0.8142 |
| Legacy p under 3 5 | 0.6442 |
| Legacy p btts yes | 0.5928 |
| Legacy p over 2 5 | 0.5833 |
| Legacy goal margin distribution | {"-1": 0.1368906018544548, "-10": 1.0746193058782339e-07, "-11": 1.163107612623569e-08, "-12": 1.1567867329825804e-09, "-13": 1.0640296763407942e-10, "-14": 9.098931284342781e-12, "-15": 7.219230692141741e-13, "-16": 4.806731746403499e-14, "-2": 0.06812688807753721, "-3": 0.023598932115694048, "-4": 0.006479910592377249, "-5": 0.0014668703085261722, "-6": 0.000281755532158713, "-7": 4.6931610036849454e-05, "-8": 6.894677747477589e-06, "-9": 9.054433541370231e-07, "0": 0.2408656606470241, "1": 0.22608231558325279, "10": 6.01837795255085e-06, "11": 9.662707980738798e-07, "12": 1.425562928161783e-07, "13": 1.9450956920192353e-08, "14": 2.4673556472482074e-09, "15": 2.903931888075292e-10, "16": 2.868134600510682e-11, "2": 0.16274598102060783, "3": 0.083625400225796, "4": 0.03406191095286656, "5": 0.011437888295043453, "6": 0.0032589726977996416, "7": 0.0008052446736431079, "8": 0.00017548116827702424, "9": 3.418471530704548e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4998 |
| Legacy raw p draw | 0.2541 |
| Legacy raw p away | 0.2461 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7947 |
| Legacy lambda away | 1.2099 |
| Legacy model home team | Groningen |
| Legacy model away team | Sparta Rotterdam |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 75.9% |
| Market reference home draw last update utc | 2026-11-01T09:33:41Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.0% |
| Market reference draw away last update utc | 2026-11-01T09:33:41Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.1% |
| Market reference home away last update utc | 2026-11-01T09:33:41Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.00 |
| Market reference dc home draw odds | 1.24 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 86.8% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 5.70 |
| Market reference over 1 5 last update utc | 2026-11-01T09:33:56Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 54.9% |
| Market reference under 3 5 odds | 1.73 |
| Market reference under 3 5 opposite odds | 2.07 |
| Market reference under 3 5 last update utc | 2026-11-01T09:33:56Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 64.2% |
| Market reference btts yes odds | 1.54 |
| Market reference btts yes opposite odds | 2.72 |
| Market reference btts yes last update utc | 2026-11-01T09:33:56Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,487.9195 |
| Elo away rating | 1,450.6913 |
| Elo rating diff | 97.2282 |
| Elo home expectancy | 0.6364 |

</details>


---

## 2026-11-01 — SC Telstar vs FC Utrecht

The model's most likely 1X2 outcome is **FC Utrecht win** at **43.2%**. Expected goals are 1.46 for SC Telstar and 1.60 for FC Utrecht (3.06 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.4%; Under 3.5 goals: 63.2%; Double Chance 1X: 56.8%; Double Chance X2: 68.5%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 62.2%; BTTS No (at least one team does not score): 37.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Telstar win | 31.5% | 3.18 |
| Draw | 25.3% | 3.96 |
| FC Utrecht win | 43.2% | 2.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Telstar expected goals | 1.46 |
| FC Utrecht expected goals | 1.60 |
| Expected total goals | 3.06 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 36.8% |
| Under 3.5 | 63.2% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.64% |
| 2 | 1-2 | 9.48% |
| 3 | 2-1 | 7.41% |
| 4 | 0-1 | 6.97% |
| 5 | 0-2 | 6.47% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:30:00+00:00 |
| Fixture id | d7d5552edc5c81a14b6933537ba2043c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 8.00 |
| Matched home-team name | Telstar |
| Matched away-team name | Utrecht |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4645 |
| Dc lambda away | 1.5985 |
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
| P btts yes | 62.2% |
| P btts no | 37.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.01 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.59 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.72 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.08 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.209556058323876, "-10": 1.8775655715669503e-06, "-11": 2.6815314781260647e-07, "-12": 3.51972092608065e-08, "-13": 4.271179872502502e-09, "-14": 4.776712825703289e-10, "-15": 4.403121542007414e-11, "-2": 0.1325562863861905, "-3": 0.06006337006724369, "-4": 0.021643726472914654, "-5": 0.0064422328605108275, "-6": 0.0016290257290680582, "-7": 0.00035750741656866706, "-8": 6.923794211468688e-05, "-9": 1.1991685943226166e-05, "0": 0.25278818975586065, "1": 0.16297510210713226, "10": 6.674846394709535e-07, "11": 8.734034092092174e-08, "12": 1.0503306383016195e-08, "13": 1.1677543283735051e-09, "14": 1.1965161844697018e-10, "15": 1.0104991190089505e-11, "2": 0.09492048031377809, "3": 0.039405343278719224, "4": 0.013009580009401047, "5": 0.003547753840533964, "6": 0.0008219224147776484, "7": 0.00016526228641399292, "8": 2.9323693606079022e-05, "9": 4.653080738179884e-06} |
| Raw goal margin distribution | {"-1": 0.1933658607201442, "-10": 1.7325057825025312e-06, "-11": 2.474357680056293e-07, "-12": 3.247789025094216e-08, "-13": 3.9411906243270955e-09, "-14": 4.4076663511561723e-10, "-15": 4.0629385455885214e-11, "-2": 0.12231505314590688, "-3": 0.05542290375043691, "-4": 0.019971542851594436, "-5": 0.0059445091303778445, "-6": 0.0015031680055255926, "-7": 0.00032988657007373696, "-8": 6.388865289117984e-05, "-9": 1.1065214207807941e-05, "0": 0.26047613272107856, "1": 0.17628399500895192, "10": 7.219928524769442e-07, "11": 9.447273862030072e-08, "12": 1.136102868513e-08, "13": 1.2631156264553626e-09, "14": 1.2942262367937266e-10, "15": 1.0930186227760521e-11, "2": 0.1026718882917582, "3": 0.04262326728475034, "4": 0.014071969937704066, "5": 0.0038374709525051402, "6": 0.0008890423444506485, "7": 0.00017875795564295193, "8": 3.171832869231776e-05, "9": 5.0330611916803696e-06} |
| Unadjusted home-win probability | 34.1% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 39.9% |
| Raw p over 1 5 | 82.1% |
| Raw p under 3 5 | 63.3% |
| Raw p btts yes | 62.4% |
| P home draw | 56.8% |
| P draw away | 68.5% |
| P home away | 74.7% |
| Raw p home draw | 60.1% |
| Raw p draw away | 65.9% |
| Raw p home away | 74.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5938 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:32Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.3, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:32Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.65, "price": 2.3, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 3.25 |
| Reference draw odds | 3.95 |
| Reference away odds | 2.22 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:56Z |
| Market reference home last update utc | 2026-11-01T09:33:56Z |
| Market reference draw last update utc | 2026-11-01T09:33:56Z |
| Market reference away last update utc | 2026-11-01T09:33:56Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:56Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:56Z |
| Home probability edge | +1.1% |
| Draw probability edge | +0.3% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | 0.0367 |
| Raw edge prob draw | 0.0110 |
| Raw edge prob away | -0.0477 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.055367987884168565, 0.06566889666162497, 0.062461651077227995, 0.033521399741753666, 0.013492489646852818, 0.004344622319423628, 0.0011658178977391814, 0.0002681406255030723, 5.396380582810909e-05, 9.653615594811587e-06, 1.554246654031612e-06, 2.2748732071543468e-07, 3.05215011225614e-08, 3.780005893595683e-09, 4.347047453464295e-10, 4.6658745925169555e-11], [0.05292274167142986, 0.11695864181208213, 0.09262789039414458, 0.049710766327620816, 0.02000877067126478, 0.006442884442967333, 0.0017288568359776592, 0.00039764079304607146, 8.002595841273464e-05, 1.4315888738160716e-05, 2.304879653871219e-06, 3.3735372417923677e-07, 4.5262048182970407e-08, 5.6055830347534915e-09, 6.446480810438189e-10, 6.919287481115762e-11], [0.047098081054632444, 0.07582862003518695, 0.0632576052114688, 0.03685944363775008, 0.01483606488698137, 0.004777257594963679, 0.0012819094496245996, 0.00029484193228395566, 5.933749409998886e-05, 1.0614917714019295e-05, 1.709017743435161e-06, 2.5014039213192706e-07, 3.356081664350343e-08, 4.156416953311396e-09, 4.779924222615705e-10, 5.130500005626902e-11], [0.023281463182954116, 0.037483506462091455, 0.030174505048341495, 0.01678141161752848, 0.007333744617864892, 0.002361487863669456, 0.0006336718394258366, 0.0001457458868291791, 2.9331634183889333e-05, 5.24715254666879e-06, 8.447994649006522e-07, 1.236490786797431e-07, 1.6589739954994362e-08, 2.054594711815924e-09, 2.362806027639475e-10, 2.5361022002700104e-11], [0.008631347325656104, 0.013896599226403699, 0.011186867054072831, 0.00600367482943699, 0.002504187020694349, 0.0008754957451117721, 0.00023492688984326021, 5.403369026348241e-05, 1.0874381918383884e-05, 1.945324301359162e-06, 3.1320014316903947e-07, 4.584154080846823e-08, 6.150464275746676e-09, 7.61718472407856e-10, 8.759844399574523e-11, 9.402320967488934e-12], [0.0025599819417074176, 0.004121609492528971, 0.0033179266877122453, 0.0017806373173696582, 0.0007167132266104174, 0.0002391580504443924, 6.96772558129583e-05, 1.602591879336894e-05, 3.2252463361710816e-06, 5.769661322098986e-07, 9.289241649095287e-08, 1.3596199089439589e-08, 1.8241737801729852e-09, 2.2591902057201073e-10, 2.598093047237329e-11, 2.7886459643864516e-12], [0.0006327234994537689, 0.00101869436616239, 0.0008200566381261911, 0.0004401011805390567, 0.00017714238270887542, 5.704038096574554e-05, 1.5861372212622668e-05, 3.960955839453817e-06, 7.971498217137991e-07, 1.4260258023330848e-07, 2.2959230249753906e-08, 3.360427871378932e-09, 4.5086162484140506e-10, 5.583800063611068e-11, 6.42143015922254e-12, 6.892399530550615e-13], [0.00013404303039531106, 0.00021581129830790263, 0.0001737297207470913, 9.323582255272228e-05, 3.752776972918257e-05, 1.2084054924706034e-05, 3.2425850793756742e-06, 7.728637352438922e-07, 1.6887689152346227e-07, 3.021048216664161e-08, 4.863933141218146e-09, 7.119096029993572e-10, 9.551543215143628e-11, 1.1829329593323355e-11, 1.360385632518974e-12, 1.4601609084660346e-13], [2.4847492248092522e-05, 4.000483684934636e-05, 3.220419500212697e-05, 1.72830797042644e-05, 6.956504673790812e-06, 2.240015465046221e-06, 6.010764407963278e-07, 1.3824887499397916e-07, 2.8832427489913226e-08, 5.600102588198598e-09, 9.016249533096639e-10, 1.319663416270238e-10, 1.770564984211996e-11, 2.192797152551659e-12, 2.521740321652268e-13, 2.7066932720842666e-14], [4.094193528406381e-06, 6.591713260162923e-06, 5.30637882683582e-06, 2.8477832841084007e-06, 1.1462434973875286e-06, 3.690938598130153e-07, 9.904111245571609e-08, 2.2779669016830617e-08, 4.5844512868817615e-09, 8.498738030932471e-10, 1.4856336454530983e-10, 2.1744477730878588e-11, 2.9174113941177254e-12, 3.6131356120149854e-13, 4.155144833991335e-14, 4.459897186928073e-15], [6.071509524023799e-07, 9.775221801567142e-07, 7.869127182601041e-07, 4.2231377710545117e-07, 1.6998288583460316e-07, 5.473500140052478e-08, 1.4687362807171771e-08, 3.3781250551590654e-09, 6.79854028824086e-10, 1.2161946983051869e-10, 2.0291431928992255e-11, 3.2246107254568597e-12, 4.326393205886373e-13, 5.358121722320574e-14, 6.161897638262449e-15, 6.613832018131462e-16], [8.185256786570128e-08, 1.317838673807738e-07, 1.0608700590999215e-07, 5.6933892575425835e-08, 2.2916106190283343e-08, 7.3790552399504865e-09, 1.980065017085679e-09, 4.554192153403422e-10, 9.165397470415927e-11, 1.6396031116650063e-11, 2.6397857105629784e-12, 4.0039217201339823e-13, 5.8325922424615e-14, 7.223508753030393e-15, 8.307112796606799e-16, 8.916384500006124e-17], [1.0115314162083828e-08, 1.6285808189158848e-08, 1.3110198265924867e-08, 7.035872238188947e-09, 2.8319650748980696e-09, 9.119012868837201e-10, 2.446958016275782e-10, 5.6280560998106686e-11, 1.1326568884893129e-11, 2.0262162822837244e-12, 3.2622387396245976e-13, 4.7747759243122183e-14, 6.638673943365355e-15, 8.926789017706868e-16, 1.0265903429616811e-16, 1.1018839452352709e-17], [1.153889805675602e-09, 1.8577799706012621e-09, 1.4955268701531101e-09, 8.026069304020223e-10, 3.2305231232492324e-10, 1.0402381793160434e-10, 2.791331899982385e-11, 6.4201234438022385e-12, 1.2920619330391823e-12, 2.3113768635925946e-13, 3.721351571504113e-14, 5.446756447863164e-15, 7.307799947484932e-16, 9.378921204723253e-17, 1.1710680581615007e-17, 1.2569581439304141e-18], [1.2222628559595268e-10, 1.9678616116051168e-10, 1.5841434203565933e-10, 8.5016492401691e-11, 3.421945838713797e-11, 1.1018768704560448e-11, 2.956730602196308e-12, 6.800544018533882e-13, 1.3686222900881028e-13, 2.4483361171904606e-14, 3.941858033101319e-15, 5.769500743429581e-16, 7.74081926251537e-17, 9.58679663758016e-18, 1.1424970011535269e-18, 1.3314384469515718e-19], [1.2083748230806173e-11, 1.9455016694454897e-11, 1.5661434984907284e-11, 8.405048755586971e-12, 3.3830637798455377e-12, 1.0893567303480563e-12, 2.9231345785446323e-13, 6.72327244109588e-14, 1.3530712396157146e-14, 2.4205167554808473e-15, 3.8970684416474185e-16, 5.703944455247412e-17, 7.652863752861013e-18, 9.477866102501754e-19, 1.0899648007152746e-19, 1.2123577795305537e-20]] |
| Legacy trial inputs | {"lambda_home": 1.4829561626480037, "lambda_away": 1.6100150650984675, "rho": -0.10361560184068906, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3230 |
| Legacy p draw | 0.2551 |
| Legacy p away | 0.4219 |
| Legacy p over 1 5 | 0.8260 |
| Legacy p under 3 5 | 0.6257 |
| Legacy p btts yes | 0.6284 |
| Legacy p over 2 5 | 0.5995 |
| Legacy goal margin distribution | {"-1": 0.20343928389698998, "-10": 1.9273061766561284e-06, "-11": 2.771514687754479e-07, "-12": 3.6630437601579166e-08, "-13": 4.475958974695772e-09, "-14": 5.038976201575871e-10, "-15": 4.6658745925169555e-11, "-2": 0.1296217512482495, "-3": 0.058998506385459164, "-4": 0.021374504463537593, "-5": 0.006399694396765298, "-6": 0.0016283705967217572, "-7": 0.00035967402403476874, "-8": 7.011874433912729e-05, "-9": 1.222601376941256e-05, "0": 0.2551256555353344, "1": 0.1657066807346848, "10": 7.528829337945982e-07, "11": 9.972230248119478e-08, "12": 1.2139913523476336e-08, "13": 1.3663374018210208e-09, "14": 1.416813022904076e-10, "15": 1.2083748230806173e-11, "2": 0.09773894287849161, "3": 0.04097596057575885, "4": 0.013673590031741319, "5": 0.0037708921244824648, "6": 0.0008837643892441893, "7": 0.00017980041646297997, "8": 3.228599113194713e-05, "9": 5.1851729501057625e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3421 |
| Legacy raw p draw | 0.2608 |
| Legacy raw p away | 0.3972 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4830 |
| Legacy lambda away | 1.6100 |
| Legacy model home team | Telstar |
| Legacy model away team | Utrecht |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 56.6% |
| Market reference home draw last update utc | 2026-11-01T09:33:40Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.5% |
| Market reference draw away last update utc | 2026-11-01T09:33:40Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market reference home away last update utc | 2026-11-01T09:33:40Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home draw odds | 1.67 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 83.6% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-11-01T09:33:56Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.1% |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.23 |
| Market reference under 3 5 last update utc | 2026-11-01T09:33:40Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 63.7% |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.68 |
| Market reference btts yes last update utc | 2026-11-01T09:33:56Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,388.0800 |
| Elo away rating | 1,522.9291 |
| Elo rating diff | -74.8492 |
| Elo home expectancy | 0.3939 |

</details>


---
