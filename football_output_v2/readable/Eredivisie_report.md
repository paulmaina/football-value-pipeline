# Eredivisie — football model report

Fixtures in this report: **6**.

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
| Training as of utc | 2026-11-05T13:37:00.829646+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1629, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1323, 'tuning_matches': 189, 'audit_matches': 114, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6639999435984515, 'audit_candidate_poisson_score': 0.6541517901162848, 'audit_gain': 0.009848153482166722, 'audit_gain_lower95': -0.0021828454332282108, 'audit_baseline_briers': [0.6216633755590796, 0.09847259899912482, 0.27967453202176307, 0.2302451960138092], 'audit_candidate_briers': [0.6176749252028129, 0.0975895815214795, 0.2767941288032132, 0.2243749218030424], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1636.627 |
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
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 24.00 |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 5} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 6} |
| Legacy comparison status | {'None': 6} |
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
| Market best home last update utc | 2026-11-05T13:36:58Z |
| Market best draw last update utc | 2026-11-05T13:36:58Z |
| Market best away last update utc | 2026-11-05T13:36:59Z |
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
| Dc lambda away | 1.6440 |
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
| Score matrix json | [[0.05079671101821752,0.06143567075981602,0.06296600505594635,0.03831402707492118,0.017485204945829273,0.006383717198921599,0.001942206063262259,0.0005064891917934017,0.00011557212850580108,2.3441398559657477e-05,4.279139410023203e-06,7.101280491129572e-07,1.0802601052822162e-07,1.5169033201681965e-08,1.977892951714494e-09,2.4070462795266155e-10,2.746232954664251e-11],[0.05501283142992374,0.11302093316873851,0.08518829042847681,0.05183600997145799,0.023656173133475223,0.00863669140628827,0.002627659386078662,0.0006852419544648578,0.00015636043671250272,3.171445713882389e-05,5.789355232575167e-06,9.607500815001963e-07,1.4615110408435813e-07,2.0522566180845166e-08,2.6759410741936446e-09,3.2565533950090307e-10,3.715447570769758e-11],[0.04366215978033364,0.0797036355007847,0.06455947442609218,0.03506512020397714,0.016002515528262058,0.005842398411700832,0.0017775132051770742,0.00046354052936074466,0.0001057719819000192,2.1453642986585405e-05,3.916282083546764e-06,6.49911463330897e-07,9.886575057539769e-08,1.3882747735052397e-08,1.8101739597053457e-09,2.202936458835041e-10,2.513361189496507e-11],[0.019690544364888,0.035944350411588145,0.03280753194449293,0.017715938185637232,0.007216735121311615,0.0026347758723278473,0.0008016140933430939,0.0002090452099534611,4.770052403826698e-05,9.675057558790333e-06,1.7661454792767077e-06,2.9309384983127647e-07,4.4585986072765545e-08,6.260772750566596e-09,8.163432785062911e-10,9.934693632644935e-11,1.1334631693840242e-11],[0.006659958062134021,0.012157503717302048,0.011096533586042779,0.006752101993379758,0.002734581385310051,0.0008911636208553269,0.00027113096239231153,7.070562934068335e-05,1.6133809393465228e-05,3.2724071207080046e-06,5.973656495035844e-07,9.913350854974244e-08,1.5080375224821725e-08,2.11758919320066e-09,2.7611283357161853e-10,3.3602241627991424e-11,3.8337270078383885e-12],[0.0018020849222829007,0.0032896384537484885,0.003002555823693278,0.0018270176902716242,0.0008337880717050859,0.000270145367165819,7.336397838137086e-05,1.913188452038707e-05,4.365567226655134e-06,8.854643643070474e-07,1.6163819952271622e-07,2.682404294198376e-08,4.080523715236717e-09,5.72987925907953e-10,7.471199812161951e-11,9.092263408834005e-12,1.0373491202976999e-12],[0.00040634766225524586,0.0007417724208314598,0.0006770388701787844,0.0004119696903075841,0.00018800880555865562,6.864060497499505e-05,1.853282832764076e-05,4.314001217849476e-06,9.843809329041978e-07,1.9966116468622881e-07,3.64473969539665e-08,6.048486953601128e-09,9.20107178058522e-10,1.2920162713432185e-10,1.684662326605521e-11,2.0501919388505986e-12,2.339092818342404e-13],[7.853685183292955e-05,0.00014336607816387587,0.00013085469998093673,7.962344940727393e-05,3.6337405323058626e-05,1.3266514178338277e-05,4.0362540307825705e-06,9.340976991658171e-07,1.9025624275917656e-07,3.8589515245943955e-08,7.04437131096767e-09,1.169021426263285e-09,1.7783373161922051e-10,2.4971446840631225e-11,3.25603141897805e-12,3.9625088437062207e-13,4.5208820712307503e-14],[1.3281810036497662e-05,2.4245446200224226e-05,2.2129576459556773e-05,1.3465570681745604e-05,6.1452235919357814e-06,2.2435750485393395e-06,6.825936874824486e-07,1.7800702594633972e-07,3.604616015016753e-08,6.526090605050924e-09,1.1913133693958072e-09,1.976998077953813e-10,3.0074465506620374e-11,4.223062238085537e-12,5.506458403977159e-13,6.701222229025127e-14,7.645518691687433e-15],[1.9965882821297457e-06,3.644697043953493e-06,3.3266288951755183e-06,2.0242121037331595e-06,9.237808236234677e-07,3.3726545099522746e-07,1.0261090575291565e-07,2.675890870028934e-08,6.105923058366684e-09,1.099058143632971e-09,1.7908419915237604e-10,2.971922641107493e-11,4.5209444538680776e-12,6.348318908414081e-13,8.27758437683148e-14,1.0073613266303773e-14,1.1493127057742765e-15],[2.701234456482317e-07,4.931002213468186e-07,4.5006798226785685e-07,2.738607418851538e-07,1.2498062887294694e-07,4.562949033425983e-08,1.3882487276494164e-08,3.6202799969347336e-09,8.260856733215148e-10,1.6755426903624642e-10,2.7143593837000364e-11,4.0207888186122334e-12,6.11649935238751e-13,8.58880016958447e-14,1.1198951899730664e-14,1.3628844514298739e-15,1.5549340391794673e-16],[3.322334519884106e-08,6.064797090129054e-08,5.5355298396804566e-08,3.368300719778982e-08,1.5371766661163722e-08,5.612116730498324e-09,1.7074514427974232e-09,4.452697979102996e-10,1.0160291500323309e-10,2.0608034620511817e-11,3.761919447055517e-12,5.54024100564416e-13,7.522877879230412e-14,1.0563639605336772e-14,1.3773948571442874e-15,1.676255109486245e-16,1.912463030416178e-17],[3.74572487869937e-09,6.8376803144893386e-09,6.240964512507039e-09,3.797548901083337e-09,1.733070781032941e-09,6.327311453370995e-10,1.9250449676815028e-10,5.020139151503112e-11,1.1455094729270769e-11,2.323427322479307e-12,4.241329456791235e-13,7.03853444396229e-14,9.501952275599777e-15,1.190984455132598e-15,1.5529267607820226e-16,1.8898730483252444e-17,2.1561827413070237e-18],[3.898219468991412e-10,7.116053471053917e-10,6.495044392151697e-10,3.952153332144966e-10,1.8036269289773937e-10,6.584906658298859e-11,2.0034166989609987e-11,5.224517232624578e-12,1.1921450383801178e-12,2.4180178514393103e-13,4.414000920593866e-14,7.325084700867746e-15,1.1143056213657397e-15,1.3885861197096654e-16,1.616148950827446e-17,1.9668128732032536e-18,2.2439644696448933e-19],[3.767142194804971e-11,6.876776821965703e-11,6.276649116714975e-11,3.8192625367279355e-11,1.7429801379539048e-11,6.363489772357013e-12,1.9360519951396034e-12,5.048843317074179e-13,1.1520592701701034e-13,2.3367122216711586e-14,4.265580542128726e-15,7.078779395737515e-16,1.0768371964550614e-16,1.5120968650013755e-17,1.7496993397114962e-18,1.9006789696852495e-19,2.1685113689685543e-20],[3.3977742232100853e-12,6.202509439825725e-12,5.661224205000468e-12,3.444784170043248e-12,1.5720810837652855e-12,5.739550141747449e-13,1.746222261785466e-13,4.5538046595210276e-14,1.0390999567768788e-14,2.107597787204121e-15,3.8473407329987523e-16,6.384705678430807e-17,9.712534009877597e-18,1.3638358960762407e-18,1.7783080637237396e-19,1.9205587171416794e-20,1.9558890137941352e-21],[2.8730838279325325e-13,5.244706797300442e-13,4.78700780015935e-13,2.9128344143828365e-13,1.3293175005893916e-13,4.8532385051421e-14,1.476567485279138e-14,3.850597968947133e-15,8.786402760453382e-16,1.7821387533164973e-16,3.253227470211859e-17,5.398767965659016e-18,8.212707072002137e-19,1.1532299086278176e-19,1.5036985400812452e-20,1.8299635343230802e-21,1.852824580279796e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18987485507955096, "-10": 5.345301453855626e-06, "-11": 8.710128838016223e-07, "-12": 1.304619313321064e-07, "-13": 1.8076602553452955e-08, "-14": 2.328681903110362e-09, "-15": 2.7785910366035913e-10, "-16": 2.746232954664251e-11, "-2": 0.13373059346701008, "-3": 0.06868949081785168, "-4": 0.028125511688144898, "-5": 0.009526057914347411, "-6": 0.0027435201925178716, "-7": 0.0006861727635298518, "-8": 0.00015151163219167342, "-9": 2.992744563822839e-05, "0": 0.24911728765011368, "1": 0.17518275008362869, "10": 3.374256149173123e-07, "11": 4.075034319138166e-08, "12": 4.523674432892013e-09, "13": 4.64542222765237e-10, "14": 4.435263216789137e-11, "15": 3.922244902940129e-12, "16": 2.8730838279325325e-13, "2": 0.09273204698769463, "3": 0.03530126091171946, "4": 0.0107127556639698, "5": 0.0026891487829597367, "6": 0.0005739983195743751, "7": 0.00010639881271764147, "8": 1.74120589722331e-05, "9": 2.5490282554299465e-06} |
| Raw goal margin distribution | {"-1": 0.21593952576375627, "-10": 2.7197467190837772e-06, "-11": 4.004674051377825e-07, "-12": 5.4173844830678596e-08, "-13": 6.774527628957455e-09, "-14": 7.823271837348397e-10, "-15": 7.564033908052423e-11, "-2": 0.14353364962061915, "-3": 0.06824352242769721, "-4": 0.02563413368783749, "-5": 0.00792262393335793, "-6": 0.0020751103864647485, "-7": 0.00047094382891244057, "-8": 9.421164791086549e-05, "-9": 1.684069535625591e-05, "0": 0.2618799682247285, "1": 0.15764508772893787, "10": 1.3599937883301383e-07, "11": 1.4841455126204784e-08, "12": 1.4879893243568327e-09, "13": 1.3790817793463682e-10, "14": 1.1803213683568058e-11, "15": 8.457970418793853e-13, "2": 0.07884159840465324, "3": 0.027782029879742334, "4": 0.007734318105218834, "5": 0.0017716310090866761, "6": 0.00034391117036925486, "7": 5.7846226625486235e-05, "8": 8.576525257912193e-06, "9": 1.1362336229004075e-06} |
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
| Totals anchor reference last update utc | 2026-11-05T13:36:58Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5490 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.0, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.9, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.28, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.96, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.28, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.13, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 4.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.92, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.53, "under": 2.44}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:34:12Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.15, "under": 4.87}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.29, "draw": 3.86, "home": 2.84}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.58, "under": 2.43}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.17, "under": 5.07}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.42, "draw": 3.69, "home": 2.8}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.45, "home_away": 1.29, "home_draw": 1.58}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.84 |
| Reference draw odds | 3.86 |
| Reference away odds | 2.29 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:58Z |
| Market reference home last update utc | 2026-11-05T13:36:58Z |
| Market reference draw last update utc | 2026-11-05T13:36:58Z |
| Market reference away last update utc | 2026-11-05T13:36:58Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:16Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:16Z |
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
| Market best home draw last update utc | 2026-11-05T13:36:59Z |
| Market reference home draw last update utc | 2026-11-05T13:37:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 65.7% |
| Market draw away odds | 1.45 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T13:36:59Z |
| Market reference draw away last update utc | 2026-11-05T13:37:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T13:36:59Z |
| Market reference home away last update utc | 2026-11-05T13:37:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home draw odds | 1.55 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T13:36:58Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-11-05T13:37:01Z |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 61.4% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-05T13:34:12Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market reference under 3 5 last update utc | 2026-11-05T13:37:01Z |
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
| Market best home last update utc | 2026-11-05T13:36:58Z |
| Market best draw last update utc | 2026-11-05T13:36:59Z |
| Market best away last update utc | 2026-11-05T13:36:59Z |
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
| Score matrix json | [[0.06444924198016634,0.07007920369776224,0.059628383479482565,0.03008202534223818,0.011382099378089407,0.0034453048896491457,0.0008690638832916253,0.0001879009403312927,3.554792524365472e-05,5.977877903350979e-06,9.047369595888129e-07,1.244815360415871e-07,1.5699975847627432e-08,1.8278094724548196e-09,1.975960140696907e-10,1.99371103354327e-11],[0.07389839959889621,0.12350268203253006,0.08154267189105847,0.04113760224851093,0.015565184579225143,0.0047115039816229085,0.0011884573579292526,0.00025695723800273843,4.861229896578719e-05,8.174833997394616e-06,1.237240802760474e-06,1.7023029063712244e-07,2.1469942744316297e-08,2.4995557383009806e-09,2.702153907595011e-10,2.7264285088282037e-11],[0.05757849732235324,0.08714362428833972,0.059120486679427355,0.028128131325993695,0.010642806873208673,0.003221524724203594,0.0008126162637587256,0.00017569635906446805,3.323900895117494e-05,5.589601524606044e-06,8.459722949259684e-07,1.1639618521705106e-07,1.468022772512353e-08,1.7090892084289151e-09,1.847617163409925e-10,1.86421509654294e-11],[0.026246474364300967,0.03972338645955314,0.03006017893895206,0.013595734804122385,0.00485139714914778,0.0014684937957723633,0.00037042147549198553,8.008909920433661e-05,1.5151607577523494e-05,2.5479534886242186e-06,3.8562642625727726e-07,5.305781903786753e-08,6.691807507452465e-09,7.79068023331659e-10,8.422143468418521e-11,8.497803175902228e-12],[0.008973107782310133,0.013580575555882763,0.010276931744464026,0.005184626903122306,0.0017586924360045038,0.0005020465958293324,0.0001266391736405113,2.7380748719763575e-05,5.180010312291947e-06,8.710907591015471e-07,1.318374208468962e-07,1.8139332632372466e-08,2.2877857494077307e-09,2.6634668131330433e-10,2.8793505768145655e-11,2.9052170113156792e-12],[0.0024541707859237387,0.0037143264734859705,0.0028107703894873584,0.001418010369455435,0.0005365308605614712,0.00014559856032598118,3.463617821628932e-05,7.4887135243418035e-06,1.4167477185856032e-06,2.3824582794934072e-07,3.605791377786029e-08,4.9611596452996936e-09,6.257159823398013e-10,7.284658337610722e-11,7.875106640290146e-12,7.945852082592525e-13],[0.0005593523069710001,0.0008465658110284411,0.0006406281546268823,0.00032319159530910677,0.00012228561122865571,3.701524651162755e-05,8.37069992669258e-06,1.7068205725987644e-06,3.229038131054435e-07,5.430076596707591e-08,8.218285936696134e-09,1.1307428597742437e-09,1.4261260065430068e-10,1.6603125055554733e-11,1.7948869296930077e-12,1.8110111646429499e-13],[0.00010927461764565577,0.00016538441722528465,0.00012515260199601538,6.313845060358921e-05,2.3889618839579506e-05,7.2312688429253225e-06,1.8240576039116227e-06,3.5356794734877955e-07,6.308222970331113e-08,1.0608154047045154e-08,1.6055177430093268e-09,2.2090101733287738e-10,2.7860683175405686e-11,3.243573181978158e-12,3.5064766966189907e-13,3.5379768725729447e-14],[1.8679326381048437e-05,2.8270696107197917e-05,2.1393497872504014e-05,1.0792842394951491e-05,4.083674663318209e-06,1.2361080164482147e-06,3.1180312551432596e-07,6.741518271415494e-08,1.1434050523466265e-08,1.8133504011676941e-09,2.744460752037024e-10,3.776066473228695e-11,4.762485611434005e-12,5.544541212988131e-13,5.993946634165195e-14,6.047792813669788e-15],[2.838249715907208e-06,4.295620385763066e-06,3.2506573320813654e-06,1.6399296867782967e-06,6.204982030176302e-07,1.8782172091999434e-07,4.7377250889940455e-08,1.0243470202459366e-08,1.937904687175149e-09,2.9216102645304306e-10,4.1700994944285335e-11,5.737583559630766e-12,7.236408400347271e-13,8.424710935275223e-14,9.10756468650957e-15,9.189381825181472e-16],[3.881347301805464e-07,5.874322650476436e-07,4.44532064752989e-07,2.2426274295928508e-07,8.485402156687316e-08,2.56848904318577e-08,6.47890718980848e-09,1.4008092807553428e-09,2.650112527649535e-10,4.456532698278238e-11,6.0468538961201886e-12,7.846228026816908e-13,9.895892550269362e-14,1.1520913355106108e-14,1.2454725679661916e-15,1.2566611793362847e-16],[4.8252711370289935e-08,7.302927909016137e-08,5.5263999192721794e-08,2.7880229635957153e-08,1.0549008611958279e-08,3.1931324568905296e-09,8.054544319682573e-10,1.7414789415435513e-10,3.2946063557873206e-11,5.540338683483706e-12,8.385164863901758e-13,1.0343113695966907e-13,1.2302523063510245e-14,1.4322740626366046e-15,1.5483651337702058e-16,1.5622747582664294e-17],[5.4988563912064115e-09,8.322382445795349e-09,6.2978594680926885e-09,3.1772179131135983e-09,1.2021600813602055e-09,3.6388787945608076e-10,9.178920987601216e-11,1.984581246506769e-11,3.754517974545378e-12,6.313744018513469e-13,9.555694611510608e-14,1.3147551126083852e-14,1.4866064070750733e-15,1.6322128144984988e-16,1.7645096555125056e-17,1.7803609984501868e-18],[5.784434762302299e-10,8.754598210932983e-10,6.624933375890114e-10,3.3422239892305623e-10,1.2645932298927547e-10,3.827860830976212e-11,9.6556203442618e-12,2.087648764434894e-12,3.9495056321855285e-13,6.64164287675732e-14,1.0051961381853789e-14,1.3830357871226581e-15,1.7443252344649718e-16,1.8206081782265642e-17,1.856147944886649e-18,1.872822513668719e-19],[5.6502126572939205e-11,8.551456391782045e-11,6.471208329313859e-11,3.2646709771078223e-11,1.2352495909253422e-11,3.739039094795328e-12,9.431571194945657e-13,2.0392069333493853e-13,3.857861248338524e-14,6.487530102689582e-15,9.818715529566168e-16,1.3509438054031447e-16,1.7038498873636525e-17,1.983641881993719e-18,1.9225055913463607e-19,1.8293655139061963e-20],[5.1511647076257085e-12,7.796159726357092e-12,5.899646966140913e-12,2.976323005750711e-12,1.12614771935525e-12,3.408793154126509e-13,8.59853949287134e-14,1.8590965373763233e-14,3.5171204899172534e-15,5.914527139344723e-16,8.951489789473011e-17,1.2316233873772676e-17,1.5533594820629634e-18,1.8084391995235212e-19,1.9550198360297796e-20,1.768447971080926e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18513985859665863, "-10": 1.090456134065367e-06, "-11": 1.477476946460278e-07, "-12": 1.839279110544531e-08, "-13": 2.1166670141797503e-09, "-14": 2.2486029915797274e-10, "-15": 1.99371103354327e-11, "-2": 0.1130117480763906, "-3": 0.04926800956237694, "-4": 0.016991735422850568, "-5": 0.004825518522060499, "-6": 0.0011619450282316873, "-7": 0.0002425072492563784, "-8": 4.462415181761266e-05, "-9": 7.338481101725026e-06, "0": 0.262581172492814, "1": 0.1968622692924919, "10": 4.678087845129482e-07, "11": 5.727136001116473e-08, "12": 6.442004618598599e-09, "13": 6.698576871141914e-10, "14": 6.42982862992963e-11, "15": 5.1511647076257085e-12, "2": 0.10912666509314167, "3": 0.042986186443484016, "4": 0.013395479014287824, "5": 0.003437329050138368, "6": 0.0007478582928256196, "7": 0.0001410311565874439, "8": 2.3448600461638202e-05, "9": 3.484253482408166e-06} |
| Raw goal margin distribution | {"-1": 0.19942042087884432, "-10": 1.1745672857997833e-06, "-11": 1.5914405289883702e-07, "-12": 1.9811499107684667e-08, "-13": 2.2799338296335428e-09, "-14": 2.4220465456180847e-10, "-15": 2.1474937727276095e-11, "-2": 0.12172878674789309, "-3": 0.0530682440683762, "-4": 0.018302374513901588, "-5": 0.005197729661900753, "-6": 0.0012515703983163014, "-7": 0.00026121278302494396, "-8": 4.806618739088942e-05, "-9": 7.904526885837547e-06, "0": 0.266736303070329, "1": 0.17928259004549738, "10": 4.2603374854378986e-07, "11": 5.215706288021207e-08, "12": 5.866737578806635e-09, "13": 6.100398087420548e-10, "14": 5.855648898417129e-11, "15": 4.691168875849773e-12, "2": 0.09938172119644556, "3": 0.03914754650275886, "4": 0.012199270999022366, "5": 0.0031303776856896133, "6": 0.0006810750084647871, "7": 0.00012843716127513609, "8": 2.1354654900673123e-05, "9": 3.173111795095029e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.71, "draw": 3.65, "home": 2.51}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.67, "draw": 3.62, "home": 2.52}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.52 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.67 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:58Z |
| Market reference home last update utc | 2026-11-05T13:36:58Z |
| Market reference draw last update utc | 2026-11-05T13:36:58Z |
| Market reference away last update utc | 2026-11-05T13:36:58Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:16Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:16Z |
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

The model's most likely 1X2 outcome is **Go Ahead Eagles win** at **41.0%**. Expected goals are 1.57 for Excelsior and 1.78 for Go Ahead Eagles (3.34 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 64.6%; Under 3.5 goals: 57.2%; Double Chance 1X: 59.0%; Double Chance X2: 66.3%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 66.8%; BTTS No (at least one team does not score): 33.2%.

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
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
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
| Market best home last update utc | 2026-11-05T13:36:58Z |
| Market best draw last update utc | 2026-11-05T13:36:59Z |
| Market best away last update utc | 2026-11-05T13:36:59Z |
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
| Score matrix json | [[0.045112921923762185,0.05316314277202035,0.054101286877712866,0.03205363092006529,0.014243218338069965,0.0050632458864168966,0.0014999219451802348,0.0003808566213568947,8.461793341000451e-05,1.6711321567844204e-05,2.97030938432004e-06,4.799543070117505e-07,7.10901676434428e-08,9.719794370308136e-09,1.2340135618572067e-09,1.4622430461416872e-10,1.6243906206334833e-11],[0.04767845604201978,0.11078857621289834,0.0847288570485951,0.05019968412680119,0.02230652319243457,0.007929627217219359,0.002349050815824132,0.0005964654094069757,0.00013252144629848604,2.6171857601381224e-05,4.651847187720586e-06,7.516638182854125e-07,1.1133540437655049e-07,1.5222319380407183e-08,1.9326076090382097e-09,2.2900413128228143e-10,2.543983121840142e-11],[0.04360513266671154,0.07750478275379287,0.07132865626185582,0.03930924850159662,0.017467294438808924,0.006209355541348551,0.0018394422966659632,0.00046706682340392315,0.00010377193711378291,2.0494074257567483e-05,3.64266469549226e-06,5.885961303661903e-07,8.718204414611025e-08,1.1919954193011097e-08,1.513343242715746e-09,1.79323445178042e-10,1.9920855371855106e-11],[0.022763556195708103,0.04046047723640981,0.03595769931823503,0.022061557867855505,0.00911859944525179,0.003241522388774305,0.0009602596191820232,0.00024382684403165912,5.417294198098882e-05,1.069869491297971e-05,1.9016110587656054e-06,3.072698159773205e-07,4.5512379846323063e-08,6.222674500197492e-09,7.90023372070914e-10,9.36137347114322e-11,1.039945261008182e-11],[0.00891258882244055,0.015841443844166414,0.014078476415069235,0.008341137761574637,0.0038382286040213893,0.0012691495108012921,0.00037596933778634916,9.54652421635793e-05,2.1210269301837546e-05,4.188847642096565e-06,7.4453557788915e-07,1.2030499557310683e-07,1.7819409428544673e-08,2.4363565481303218e-09,3.093169368990587e-10,3.6652477251042795e-11,4.071685649432521e-12],[0.0027916284726327246,0.004961905745235265,0.004409703666867185,0.002612636814427559,0.001160940446302971,0.00042737141679570864,0.00011776227189552296,2.9901916657437476e-05,6.643545761488816e-06,1.3120437370289362e-06,2.332057227738529e-07,3.768230058995064e-08,5.5814502068102285e-09,7.631230885599576e-10,9.688520196744575e-11,1.1480401612257459e-11,1.2753458974732939e-12],[0.0007286687108605716,0.0012951528107113994,0.0011510174501060788,0.0006819484462846224,0.0003030277799092992,0.00010772173280492665,3.304590236528802e-05,7.804975223829431e-06,1.7340931907754474e-06,3.424686443149564e-07,6.087117789663255e-08,9.835805037210025e-09,1.4568658282430229e-09,1.9918980001107031e-10,2.5288900694047614e-11,2.996605574478911e-12,3.328898025376481e-13],[0.00016302560992902332,0.00028976553236127126,0.00025751801751015217,0.0001525728492779668,6.779663777082933e-05,2.4100665956129912e-05,7.13951456673953e-06,1.8773108014884038e-06,3.8797000047670157e-07,7.662077263489723e-08,1.3618755349020946e-08,2.2005722098872264e-09,3.259457098872421e-10,4.456488683326836e-11,5.6579051613353645e-12,6.704328650521857e-13,7.447769101236532e-14],[3.191461422664076e-05,5.672578182969762e-05,5.041286573823564e-05,2.986833558411879e-05,1.3272169576677769e-05,4.718052930026714e-06,1.397662939351528e-06,3.5489125723352606e-07,8.165275612074809e-08,1.499962123407802e-08,2.666067763219733e-09,4.307937457617456e-10,6.380857335487855e-11,8.724219292642905e-12,1.1076165311300034e-12,1.3124690201936669e-13,1.458008209989483e-14],[5.553551994022418e-06,9.871013215313334e-06,8.772484889109433e-06,5.197473278647655e-06,2.3095276444242563e-06,8.210016913060806e-07,2.43211268313799e-07,6.175562816689649e-08,1.3720737250941968e-08,2.8060827452864886e-09,4.639299675528708e-10,7.496363417704861e-11,1.1103509736141679e-11,1.5181259940940106e-12,1.9273947513156834e-13,2.2838643426574148e-14,2.5371211898055985e-15],[8.697503149547227e-07,1.5459145538174186e-06,1.3738723439432832e-06,8.139842799596026e-07,3.616986747034545e-07,1.2857833695631394e-07,3.8089690605966854e-08,9.671643860757583e-09,2.148825753006824e-09,4.2437479508943364e-10,7.811152501720507e-11,1.1740169985950697e-11,1.7389377285936457e-12,2.3775604566688553e-13,3.0185225488178396e-14,3.576795055629633e-15,3.973424497127004e-16],[1.2382993985864813e-07,2.200982315663608e-07,1.9560387251232343e-07,1.1589029943441846e-07,5.149653224076513e-08,1.8306228188321158e-08,5.42298636272058e-09,1.3769918297462434e-09,3.0593718586396983e-10,6.041999002459269e-11,1.0739190353197324e-11,1.7969847443707667e-12,2.4757973713512837e-13,3.385030891019923e-14,4.297595059813745e-15,5.092430655209186e-16,5.657128351114538e-17],[1.616099769853125e-08,2.8724935325455853e-08,2.5528185971049617e-08,1.5124798288520958e-08,6.720792564183931e-09,2.3891387814445794e-09,7.077518589376343e-10,1.7971067269214386e-10,3.992774414884321e-11,7.8853895984068e-12,1.401567591652109e-12,2.2647082008782299e-13,3.4737338577544006e-14,4.417790762207949e-15,5.608774739788316e-16,6.646111610222024e-17,7.383096395509792e-18],[1.9469220715248657e-09,3.460504829682446e-09,3.0753911138509044e-09,1.8220907003754574e-09,8.096566576789421e-10,2.878205363492632e-10,8.526315893564316e-11,2.1649819007443704e-11,4.8101118383703195e-12,9.499561436795478e-13,1.688474269858621e-13,2.728303328855689e-14,4.0411251278919234e-15,5.721692061929216e-16,6.756914108153995e-17,8.006598122920896e-18,8.894446739460934e-19],[2.1779318465572965e-10,3.8711070072916766e-10,3.4402980712161783e-10,2.0382887541849488e-10,9.057255271419249e-11,3.219715474884411e-11,9.5379959937776e-12,2.421865311310736e-12,5.380850066630508e-13,1.0626720855509197e-13,1.888818221438866e-14,3.052026988593929e-15,4.52062013199399e-16,6.180812279081703e-17,8.126116660331411e-18,8.956611715248398e-19,9.949806977229223e-20],[2.2739283633633788e-11,4.0417334616828156e-11,3.5919357967646066e-11,2.1281302342827126e-11,9.456471141858059e-12,3.361630600090976e-12,9.958401432157294e-13,2.5286136627005247e-13,5.618021337471153e-14,1.109511392704262e-14,1.972071501574609e-15,3.186550922649212e-16,4.719875121153018e-17,6.453243416337906e-18,8.192961281210987e-19,1.0053451296472315e-19,1.0388363773309265e-20],[2.2257713535730536e-12,3.956138066058191e-12,3.5158661676074403e-12,2.083060921555616e-12,9.256203015254982e-13,3.290438349566165e-13,9.747503479965406e-14,2.4750629550913773e-14,5.499043487108845e-15,1.0860142800151417e-15,1.930307183868452e-16,3.1190664906627914e-17,4.619918114555727e-18,6.316577322811425e-19,8.01945163025283e-20,9.502640605147362e-21,1.0931754164412203e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18771496797092843, "-10": 3.8156990514800735e-06, "-11": 6.040376167765316e-07, "-12": 8.792351568692661e-08, "-13": 1.184212487713447e-08, "-14": 1.4829385485113433e-09, "-15": 1.7166413583257013e-10, "-16": 1.6243906206334833e-11, "-2": 0.12541747254330923, "-3": 0.061632234590494536, "-4": 0.02427870014613332, "-5": 0.00793796869166215, "-6": 0.00221164170705402, "-7": 0.000535899844398983, "-8": 0.00011475833402928606, "-9": 2.199981357861067e-05, "0": 0.2535923200391384, "1": 0.17075824661663597, "10": 1.1172928548508577e-06, "11": 1.558438806883502e-07, "12": 1.9987739257979666e-08, "13": 2.3720351911432355e-09, "14": 2.6172638544016525e-10, "15": 2.6695421699691978e-11, "16": 2.2257713535730536e-12, "2": 0.10108531320772614, "3": 0.04376942004063388, "4": 0.015192217545907192, "5": 0.0043766113500351925, "6": 0.001074425317092669, "7": 0.00022939183434110265, "8": 4.328240849478873e-05, "9": 7.311038093043882e-06} |
| Raw goal margin distribution | {"-1": 0.19353640064730315, "-10": 3.9340318375205485e-06, "-11": 6.227700831220335e-07, "-12": 9.065020729161999e-08, "-13": 1.2209373868851191e-08, "-14": 1.528927565885262e-09, "-15": 1.7698779872690105e-10, "-16": 1.6747663617923707e-11, "-2": 0.1293069299517617, "-3": 0.06354357873231418, "-4": 0.025031633276071538, "-5": 0.008184141657117085, "-6": 0.002280229329240181, "-7": 0.0005525192163072024, "-8": 0.00011831722932051226, "-9": 2.2682073682986098e-05, "0": 0.24319851312361201, "1": 0.16958254515000873, "10": 1.1096000911095584e-06, "11": 1.547708673333845e-07, "12": 1.985012005172881e-08, "13": 2.3557032990772567e-09, "14": 2.599243518557616e-10, "15": 2.6511618884504818e-11, "16": 2.2104465145294215e-12, "2": 0.10038932251124387, "3": 0.043468059653333065, "4": 0.015087616375516024, "5": 0.004346477587918004, "6": 0.0010670277041157493, "7": 0.0002278124299995212, "8": 4.298440127021979e-05, "9": 7.26070027112974e-06} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.05, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.8, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.43, "draw": 3.77, "home": 2.75}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.38, "draw": 3.66, "home": 2.83}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.83 |
| Reference draw odds | 3.66 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:58Z |
| Market reference home last update utc | 2026-11-05T13:36:58Z |
| Market reference draw last update utc | 2026-11-05T13:36:58Z |
| Market reference away last update utc | 2026-11-05T13:36:58Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.51 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:16Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:16Z |
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
| Market best home last update utc | 2026-11-05T13:36:59Z |
| Market best draw last update utc | 2026-11-05T13:36:58Z |
| Market best away last update utc | 2026-11-05T13:36:59Z |
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
| Score matrix json | [[0.05829794010069956,0.05524920649035296,0.04551036398750584,0.02188535676917569,0.007893292850485619,0.0022774706459902654,0.0005476033726351389,0.00011285807823040078,2.0352006855795057e-05,3.2623406478728326e-06,4.7064547100226426e-07,6.172566467502817e-08,7.420772297044054e-09,8.235127544956772e-10,8.486075096959879e-11,8.161691746432528e-12],[0.0788751933783778,0.11844652814101649,0.06993062070936093,0.03362874847000637,0.012128728933628359,0.0034995311389988478,0.000841440067616858,0.00017341622371739833,3.127262336327704e-05,5.012869300139139e-06,7.231875783343216e-07,9.484683632958032e-08,1.1402660128527809e-08,1.2653987583964033e-09,1.3039590258596336e-10,1.2541147111527955e-11],[0.06860645778776359,0.098975925951733,0.06072931798633996,0.025836744074735747,0.009318421876136483,0.002688666528893415,0.0006464728147892621,0.00013323453278642612,2.4026548805502958e-05,3.85135418593739e-06,5.556202127509102e-07,7.287019434372819e-08,8.760588035999268e-09,9.721974608224263e-10,1.0018230581826557e-10,9.6352800227804e-12],[0.03513992387232946,0.05069503098230996,0.036567896043751456,0.014958138325578827,0.004772854420653212,0.0013771230900110096,0.0003311205129916639,6.82421376973559e-05,1.230629190260814e-05,1.97264655927704e-06,2.845862125456767e-07,3.732379085540211e-08,4.487134397962767e-09,4.979552342996092e-10,5.1312933407796005e-11,4.935147760237064e-12],[0.013498885049273155,0.019474327784142088,0.014047435816361333,0.006755233700560283,0.002072426863040539,0.0005290172613434904,0.0001271988453523797,2.621499055149236e-05,4.7274211628818775e-06,7.577856242168271e-07,1.0932284838519898e-07,1.4337810297788397e-08,1.7237177763619207e-09,1.91287849453406e-10,1.9711692948722632e-11,1.8958206215431325e-12],[0.004148441487478066,0.005984798672304558,0.004317020651747566,0.0020760004725370405,0.0007487417207911746,0.00018376417745762146,3.9090411192702995e-05,8.05632124436174e-06,1.452818511254524e-06,2.3288066463569278e-07,3.3596807300381714e-08,4.406257765869211e-09,5.297283671993531e-10,5.878607365174181e-11,6.057745104016042e-12,5.826185563117643e-13],[0.0010624066797746295,0.0015326936888841228,0.0011055794304886861,0.0005316591244919421,0.00019175109688676794,5.5326402145231685e-05,1.1315662997876917e-05,2.063206032977806e-06,3.7206360401032407e-07,5.964022258627156e-08,8.604067962092786e-09,1.1284328578331035e-09,1.356622619548701e-10,1.505498330248874e-11,1.5513751085329074e-12,1.4920732228106232e-13],[0.00023321142719054215,0.0003364452515551089,0.00024268838079168336,0.00011670576396219761,4.2091741158669425e-05,1.2144830648414637e-05,2.9201475043656313e-06,5.119241000255792e-07,8.167257016429058e-08,1.3091767674367876e-08,1.8886995039505358e-09,2.4770499119959e-10,2.9779547068645964e-11,3.304755334414854e-12,3.4054605459144016e-13,3.275285560499983e-14],[4.4793697608164075e-05,6.462216299353544e-05,4.661396773373249e-05,2.2416065812166423e-05,8.08470128576536e-06,2.3326981791632834e-06,5.608824827220722e-07,1.1559483063170447e-07,1.7731572499845275e-08,2.5145795359454603e-09,3.6276882085853794e-10,4.757752484727883e-11,5.7198570514777636e-12,6.347553930013835e-13,6.54098179269705e-14,6.290950351140094e-15],[7.647711185733185e-06,1.1033061907393404e-05,7.958489284968028e-06,3.827136548347627e-06,1.3803160658295424e-06,3.982658925320558e-07,9.576050797408597e-08,1.9735720122240932e-08,3.5589965515087397e-09,4.852704920369854e-10,6.193619453754198e-11,8.122999180530168e-12,9.765618176028544e-13,1.0837296714652956e-13,1.1167539697050835e-14,1.0740656373171895e-15],[1.1751371410060956e-06,1.6953256355423622e-06,1.222890890873564e-06,5.880727177635959e-07,2.12097532959883e-07,6.119700796016557e-08,1.4714432439850357e-08,3.0325645355713384e-09,5.468706820666341e-10,8.766105809009787e-11,1.0757355832909691e-11,1.2481692628783472e-12,1.50057191554824e-13,1.6652446160950434e-14,1.7159893140507323e-15,1.6503949896073485e-16],[1.6415455631509018e-07,2.368195317814495e-07,1.7082526337415287e-07,8.21477023378258e-08,2.9627841043936686e-08,8.548591767690467e-09,2.055454673591562e-09,4.236180344086396e-10,7.639220227480957e-11,1.224534702781275e-11,1.7665896181776547e-12,1.970796647441065e-13,2.096144427915997e-14,2.326175231574581e-15,2.3970603486182616e-16,2.3054318326769387e-17],[2.10198092067841e-08,3.032447887057771e-08,2.1873985860807046e-08,1.051892234171302e-08,3.793812245802567e-09,1.0946377120268855e-09,2.631986954364885e-10,5.4243820334361054e-11,9.781936930342422e-12,1.5680031305462052e-12,2.2620984488242514e-13,2.966766683564991e-14,3.0338979838619224e-15,2.978641631816203e-16,3.069409239448046e-17,2.9520799391701753e-18],[2.4845199680168474e-09,3.5843224137990222e-09,2.5854827756359047e-09,1.2433258714627005e-09,4.4842473054232853e-10,1.2938505894702942e-10,3.110981683681925e-11,6.411564131549855e-12,1.1562149489669625e-12,1.8533636768204505e-13,2.673777250037965e-14,3.506687902469337e-15,4.2158043300182737e-16,3.9795679025208575e-17,3.628010354614825e-18,3.4893283206790785e-19],[2.7269145547330317e-10,3.934015860152713e-10,2.8377274896771116e-10,1.364627154868082e-10,4.9217391695755596e-11,1.4200811623553566e-11,3.4144950903781944e-12,7.037088763220194e-13,1.269017521825182e-13,2.0341814316627556e-14,2.934636144245771e-15,3.8488071753283813e-16,4.627106376854612e-17,5.1348848411180865e-18,4.500922123102496e-19,3.829753959070386e-20],[2.7934271189484677e-11,4.0299710055271045e-11,2.906942908090372e-11,1.3979119716258174e-11,5.041786015927909e-12,1.4547185657673378e-12,3.4977785301060307e-13,7.20873140506279e-14,1.2999703103034312e-14,2.083797442866511e-15,3.006215275558962e-16,3.9426839834438165e-17,4.739966792480038e-18,5.260130554131331e-19,5.420421560988217e-20,4.4344588704367514e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.15635968082402735, "-10": 5.747711449136485e-07, "-11": 7.415373101840774e-08, "-12": 8.79128850901896e-09, "-13": 9.63543937104421e-10, "-14": 9.740189808112675e-11, "-15": 8.161691746432528e-12, "-2": 0.08997029811667237, "-3": 0.03706160213124495, "-4": 0.012112508101401524, "-5": 0.003265244079586168, "-6": 0.0007471326598569696, "-7": 0.00014828152493264618, "-8": 2.5959604247518486e-05, "-9": 4.063083049750725e-06, "0": 0.25469996140903134, "1": 0.22198135658814822, "10": 1.4351246566300764e-06, "11": 1.9720602246280652e-07, "12": 2.490188348926709e-08, "13": 2.9069909831130226e-09, "14": 3.129911655285742e-10, "15": 2.7934271189484677e-11, "2": 0.13562940216405572, "3": 0.059507454743108736, "4": 0.020714467031227615, "5": 0.005947683246915181, "6": 0.0014495139514757913, "7": 0.00030641090649209055, "8": 5.713572479265603e-05, "9": 9.52484398231143e-06} |
| Raw goal margin distribution | {"-1": 0.18173658772891507, "-10": 6.680555118247379e-07, "-11": 8.618875385029787e-08, "-12": 1.0218099493101634e-08, "-13": 1.119925458618185e-09, "-14": 1.1321005838778483e-10, "-15": 9.486320260280079e-12, "-2": 0.10457232254828622, "-3": 0.043076636327234845, "-4": 0.014078347305306646, "-5": 0.003795187570086443, "-6": 0.0008683910037911043, "-7": 0.0001723473610490903, "-8": 3.017280330756525e-05, "-9": 4.722514431018338e-06, "0": 0.2619042410848871, "1": 0.1941620741473178, "10": 1.255271092464934e-06, "11": 1.724916494981245e-07, "12": 2.1781114516844474e-08, "13": 2.542679292910088e-09, "14": 2.737662965163582e-10, "15": 2.4433475483290143e-11, "2": 0.1186319718209154, "3": 0.05204982534450606, "4": 0.018118476008332145, "5": 0.00520230407337713, "6": 0.0012678570833594069, "7": 0.00026801069270085073, "8": 4.99753267759096e-05, "9": 8.331165697695914e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.53, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.46, "draw": 3.66, "home": 2.08}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.64, "under": 2.33}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.74, "home": 2.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.06 |
| Reference draw odds | 3.74 |
| Reference away odds | 3.39 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:58Z |
| Market reference home last update utc | 2026-11-05T13:36:58Z |
| Market reference draw last update utc | 2026-11-05T13:36:58Z |
| Market reference away last update utc | 2026-11-05T13:36:58Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:59Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:59Z |
| Market best over 2 5 last update utc | 2026-11-05T13:36:59Z |
| Market best under 2 5 last update utc | 2026-11-05T13:36:59Z |
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

## 2026-11-08 — FC Twente Enschede vs Ajax

The model's most likely 1X2 outcome is **FC Twente Enschede win** at **42.3%**. Expected goals are 1.59 for FC Twente Enschede and 1.38 for Ajax (2.97 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.4%; Under 3.5 goals: 65.3%; Double Chance 1X: 67.3%; Double Chance X2: 57.7%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 60.2%; BTTS No (at least one team does not score): 39.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Twente Enschede win | 42.3% | 2.36 |
| Draw | 25.0% | 4.00 |
| Ajax win | 32.7% | 3.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Twente Enschede expected goals | 1.59 |
| Ajax expected goals | 1.38 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.6% |
| Under 1.5 | 19.4% |
| Over 2.5 | 57.4% |
| Under 2.5 | 42.6% |
| Over 3.5 | 34.7% |
| Under 3.5 | 65.3% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.64% |
| 2 | 2-1 | 9.11% |
| 3 | 1-2 | 7.86% |
| 4 | 1-0 | 7.38% |
| 5 | 2-0 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Twente Enschede win | 42.3% | 42.6% | 2.31 | -2.3% |
| Draw | 25.0% | 24.5% | 3.94 | -1.5% |
| Ajax win | 32.7% | 32.9% | 2.90 | -5.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T13:30:00+00:00 |
| Fixture id | b71f32fbba046e08d4cc26e2a8e1d5a6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:36:59Z |
| Market best draw last update utc | 2026-11-05T13:36:59Z |
| Market best away last update utc | 2026-11-05T13:36:58Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Twente |
| Matched away-team name | Ajax |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5876 |
| Dc lambda away | 1.3815 |
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
| P btts yes | 60.2% |
| P btts no | 39.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.29 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.15 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.51 |
| Fair Under 4.5 odds | 1.22 |
| Score matrix json | [[0.05782543774688581,0.062447643972994155,0.04949345219912732,0.022792132078585055,0.00787196985064257,0.0021750631881481295,0.0005008170299385035,9.884154125194696e-05,1.706899622298682e-05,2.620136597719117e-06,3.6197818143023835e-07,4.5461961426537726e-08,5.233899553098156e-09,5.562121760158687e-10,5.488717980223043e-11,5.055197388294286e-12],[0.07382283282031263,0.11643320659127847,0.07857819094750759,0.036185887768876386,0.012497918867492564,0.0034532351841929493,0.0007951212627064482,0.00015692559635551917,2.7099561354012664e-05,4.159855187627342e-06,5.746940129538659e-07,7.217760182599859e-08,8.309591273382082e-09,8.830692673944104e-10,8.714153293889433e-11,8.025875100741791e-12],[0.0659762121301776,0.09114772605873718,0.059066877832160004,0.028725230029094478,0.009921149279152573,0.002741261334918052,0.0006311864259942681,0.0001245713213271564,2.151228508068035e-05,3.30219332783908e-06,4.562059613925508e-07,5.7296320284933494e-08,6.596353868674703e-09,7.01001672241577e-10,6.917504953161963e-11,6.3711331314049576e-12],[0.03491567176671082,0.04823684147052252,0.0333201791247036,0.01439508539091266,0.005250431641876353,0.0014507195534039306,0.0003340340004687664,6.59251452390519e-05,1.1384646989841113e-05,1.7475737788273879e-06,2.4143152648063634e-07,3.0322133507176956e-08,3.490896477677174e-09,3.709813507875966e-10,3.660854792824998e-11,3.3717060439788717e-12],[0.013858450973003042,0.019145783792397307,0.013225180712451295,0.006090301891826013,0.0019733630961547006,0.0005758080766927537,0.00013258212099547873,2.6166484760421146e-05,4.518703612745141e-06,6.936330968340553e-07,9.582708290490888e-08,1.2035220270535e-08,1.3855788887854913e-09,1.4724696967423327e-10,1.4530373926249032e-11,1.3382707690135056e-12],[0.004400468984915575,0.006079353885543753,0.004199386905391971,0.001933851383243418,0.0006679155654252721,0.0001731329515768687,4.2098753499324454e-05,8.308634554959077e-06,1.434822343322987e-06,2.202490693566876e-07,3.042793938943442e-08,3.82153919152194e-09,4.3996236939698286e-10,4.675527765956801e-11,4.613824440137216e-12,4.2494063903210765e-13],[0.0011643994535011021,0.0016086458889342126,0.0011111915194584442,0.0005117126155234537,0.0001767358256658608,4.8832959948569984e-05,1.0548482133301503e-05,2.1985314675091004e-06,3.7966552159860513e-07,5.827967356937835e-08,8.05147726700813e-09,1.0112099781624896e-09,1.1641757827244983e-10,1.237182217207191e-11,1.2208550213765164e-12,1.124427077103665e-13],[0.00026409381596656186,0.0003648519673125699,0.00025202589005095656,0.00011605994567026059,4.0084902545906275e-05,1.1075651658014046e-05,2.5502132527573702e-06,4.721789597111342e-07,8.611075528112644e-08,1.3218231372356218e-08,1.8261304994765609e-09,2.2934938785261363e-10,2.640430858938743e-11,2.806014480733434e-12,2.7689832760382477e-13,2.5502780568606078e-14],[5.241100937853532e-05,7.24070717468724e-05,5.001605675146454e-05,2.3032795670484386e-05,7.955090487757469e-06,2.1980298205659706e-06,5.06105189242503e-07,9.98852154577888e-08,1.6182268263286637e-08,2.6232376774468956e-09,3.6240660306341133e-10,4.551576822694942e-11,5.240094168987828e-12,5.568704845578309e-13,5.49521418812105e-14,5.06118050007342e-15],[9.245582821134778e-06,1.2772995342190929e-05,8.823100347913312e-06,4.063108543392245e-06,1.4033205776095005e-06,3.877442352348493e-07,8.927966659737738e-08,1.762028709372829e-08,3.042856374367464e-09,4.38194696546791e-10,6.393046619936181e-11,8.029225344058734e-12,9.243806826922879e-13,9.82349366416412e-14,9.693852207501203e-15,8.928193530519034e-16],[1.467873304568022e-06,2.027902323184482e-06,1.400797950197496e-06,6.450787018828216e-07,2.2279794075449502e-07,6.156014422371717e-08,1.4174470314564627e-08,2.7974817319881722e-09,4.830985485694273e-10,7.415692000137132e-11,9.611249613199488e-12,1.2747585270625741e-12,1.4675913391643102e-13,1.5596252162986723e-14,1.5390427135963218e-15,1.417483050555517e-16],[2.1186058446871168e-07,2.926904999895468e-07,2.0217948751288982e-07,9.310527712705547e-08,3.2156795685145144e-08,8.885077543564337e-09,2.0458247697759017e-09,4.0376517028761947e-10,6.972641340188785e-11,1.0703191048571843e-11,1.4786716214090205e-12,1.7422369715283527e-13,2.118198879351318e-14,2.2510328980634826e-15,2.2213258311199085e-16,2.0458767567379504e-17],[2.8030006531056818e-08,3.8724129109994476e-08,2.6749158507437978e-08,1.2318202238947546e-08,4.2544732675633356e-09,1.1755314571589645e-09,2.706708366826259e-10,5.3419754262250015e-11,9.225084637348959e-12,1.4160751786225917e-12,1.956341964661401e-13,2.4570304923666867e-14,2.653734514250557e-15,2.978206965329196e-16,2.9389033222029827e-17,2.7067771476657625e-18],[3.4232145987804992e-09,4.729253414462049e-09,3.2667887467774665e-09,1.5043824441629916e-09,5.195851447093858e-10,1.435638782678714e-10,3.3056159247393616e-11,6.5239828771066076e-12,1.1266299339091887e-12,1.729407097733128e-13,2.3892175573400897e-14,3.0006923622366217e-15,3.454607307050233e-16,3.444161499594767e-17,3.589188160132209e-18,3.305699924567776e-19],[3.8820432436055273e-10,5.363136237924177e-10,3.704650940444065e-10,1.7060214995700842e-10,5.89227447562135e-11,1.6280638200542237e-11,3.7486822973823484e-12,7.398421255416542e-13,1.2776371439097004e-13,1.9612072061126487e-14,2.7094549898449188e-15,3.402888476553358e-16,3.9176436558847965e-17,4.163322357618773e-18,3.8542526152215047e-19,3.748777556080555e-20],[4.1088793461032835e-11,5.6765157767479896e-11,3.921121630673803e-11,1.8057079902801752e-11,6.236572695147512e-12,1.7231950765560727e-12,3.9677258341181155e-13,7.830726857622188e-14,1.352292219071014e-14,2.0758047442925482e-15,2.867774248859328e-16,3.601726539608775e-17,4.1465599667321235e-18,4.406594201279867e-19,4.348440013909613e-20,3.757252629598352e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17562169075235184, "-10": 4.411380737902645e-07, "-11": 5.4510501190858646e-08, "-12": 6.189515576068166e-09, "-13": 6.49724842086168e-10, "-14": 6.291305490297222e-11, "-15": 5.055197388294286e-12, "-2": 0.09719249281044848, "-3": 0.03839300774082822, "-4": 0.012027063844917486, "-5": 0.0031068655183887914, "-6": 0.0006811022530550645, "-7": 0.00012949721529670094, "-8": 2.1716813086038135e-05, "-9": 3.2557698006724158e-06, "0": 0.24987814090031266, "1": 0.20510044163793836, "10": 1.7888779914490027e-06, "11": 2.540283410481358e-07, "12": 3.314778211946608e-08, "13": 3.998739438879656e-09, "14": 4.4496948212803263e-10, "15": 4.1088793461032835e-11, "2": 0.12956042139319543, "3": 0.05881493016070508, "4": 0.02117341374603475, "5": 0.006285640540684115, "6": 0.001583562546451486, "7": 0.000346002432899897, "8": 6.66823098121862e-05, "9": 1.1488519096626593e-05} |
| Raw goal margin distribution | {"-1": 0.17386901242878755, "-10": 4.3673558149948367e-07, "-11": 5.3966494505610596e-08, "-12": 6.127745132240496e-09, "-13": 6.432406849064522e-10, "-14": 6.228519198282109e-11, "-15": 5.004747271080141e-12, "-2": 0.09622252620420357, "-3": 0.038009851240309867, "-4": 0.011907035538580107, "-5": 0.0030758594631288627, "-6": 0.0006743049539859891, "-7": 0.0001282048523702301, "-8": 2.1500082525082136e-05, "-9": 3.2232777028472074e-06, "0": 0.26124897400662905, "1": 0.20116973098657273, "10": 1.7545944876260572e-06, "11": 2.491599365828285e-07, "12": 3.2512511228747376e-08, "13": 3.922104363991876e-09, "14": 4.364417272925708e-10, "15": 4.0301334610046296e-11, "2": 0.12707742075068756, "3": 0.057687753297526435, "4": 0.020767629330005897, "5": 0.0061651774445220025, "6": 0.0015532138737780815, "7": 0.00033937136259338396, "8": 6.540435612596685e-05, "9": 1.126834383020155e-05} |
| Research history json | {"away": [{"away": "AZ Alkmaar", "away_goals": 0.0, "away_xg": 1.25, "date": "2026-10-31T00:00:00+00:00", "home": "Ajax", "home_goals": 1.0, "home_xg": 0.66, "source": "pipeline training history"}, {"away": "Ajax", "away_goals": 2.0, "away_xg": 1.43, "date": "2026-10-25T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 1.0, "home_xg": 1.25, "source": "pipeline training history"}, {"away": "Ajax", "away_goals": 5.0, "away_xg": 3.08, "date": "2026-10-18T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Nijmegen", "away_goals": 1.0, "away_xg": 1.05, "date": "2026-10-10T00:00:00+00:00", "home": "Ajax", "home_goals": 1.0, "home_xg": 1.78, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 2.0, "away_xg": 0.82, "date": "2026-09-19T00:00:00+00:00", "home": "Ajax", "home_goals": 2.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 1.58, "date": "2026-09-15T00:00:00+00:00", "home": "Ajax", "home_goals": 5.0, "home_xg": 3.78, "source": "pipeline training history"}, {"away": "Ajax", "away_goals": 5.0, "away_xg": 4.14, "date": "2026-09-12T00:00:00+00:00", "home": "For Sittard", "home_goals": 1.0, "home_xg": 0.71, "source": "pipeline training history"}, {"away": "PSV Eindhoven", "away_goals": 3.0, "away_xg": 2.55, "date": "2026-09-05T00:00:00+00:00", "home": "Ajax", "home_goals": 1.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Ajax", "away_goals": 4.0, "away_xg": 2.14, "date": "2026-08-30T00:00:00+00:00", "home": "Telstar", "home_goals": 0.0, "home_xg": 1.13, "source": "pipeline training history"}, {"away": "Heerenveen", "away_goals": 2.0, "away_xg": 1.37, "date": "2026-08-16T00:00:00+00:00", "home": "Ajax", "home_goals": 2.0, "home_xg": 2.0, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 41.5% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 80.5% |
| Raw p under 3 5 | 65.4% |
| Raw p btts yes | 60.5% |
| P home draw | 67.3% |
| P draw away | 57.7% |
| P home away | 75.0% |
| Raw p home draw | 67.6% |
| Raw p draw away | 58.5% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5740 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.75, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.99, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.86, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.12, "price": 1.75, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.82, "draw": 3.94, "home": 2.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.9, "draw": 3.84, "home": 2.26}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.26 |
| Reference draw odds | 3.84 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:58Z |
| Market reference home last update utc | 2026-11-05T13:36:58Z |
| Market reference draw last update utc | 2026-11-05T13:36:58Z |
| Market reference away last update utc | 2026-11-05T13:36:58Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.66 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:16Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:16Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | -0.0116 |
| Raw ev home | -0.0417 |
| Raw edge prob draw | 0.0162 |
| Raw ev draw | 0.0293 |
| Raw edge prob away | -0.0047 |
| Raw ev away | -0.0607 |
| Elo home rating | 1,599.3719 |
| Elo away rating | 1,627.7316 |
| Elo rating diff | 31.6403 |
| Elo home expectancy | 0.5454 |

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
| Market best home last update utc | 2026-11-05T13:36:59Z |
| Market best draw last update utc | 2026-11-05T13:36:58Z |
| Market best away last update utc | 2026-11-05T13:36:59Z |
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
| Score matrix json | [[0.04550541350845426,0.07482500000108706,0.0846353747667307,0.057812684336269765,0.029617991998414937,0.012138864819571502,0.004145904487034893,0.0012137066195069342,0.00031089676389950383,7.07890623829125e-05,1.4506365911240277e-05,2.7024546251421283e-06,4.614977974843478e-07,7.274761308926808e-08,1.0648371161936802e-08,1.454736680441762e-09,1.8631888423702616e-10,2.2459517464603906e-11],[0.04112600465742656,0.09833019625307517,0.0984947845144739,0.06727976217507743,0.034468066664507996,0.01412665658950927,0.004824814330811121,0.0014124563432442844,0.00036180745759001445,8.238107841553952e-05,1.688184625463924e-05,3.1449932926645344e-06,5.37070063698626e-07,8.466035029582418e-08,1.2392088130002338e-08,1.692956122192725e-09,2.168294097412901e-10,2.613736087389308e-11],[0.028685947277109464,0.05878434234110506,0.05423693069511408,0.039148557538048454,0.020056181047866915,0.008219978942189513,0.0028074493032338448,0.0008218760981881659,0.00021052749910588408,4.7935668678566024e-05,9.823160904291223e-06,1.8299997933147016e-06,3.125088081607032e-07,4.9261924947397395e-08,7.210673157725167e-09,9.850925154370463e-10,1.2616808307242222e-10,1.5208733547565668e-11],[0.01112779852569439,0.022803511131014583,0.023364914394415553,0.014371641520387972,0.007780155897923061,0.003188678716812883,0.0010890604349125502,0.00031882062479490455,8.166743010219486e-05,1.859511411969909e-05,3.8105820376954017e-06,7.098900658692259e-07,1.2122782703055982e-07,1.9109592948319515e-08,2.797150721873721e-09,3.821352293183717e-10,4.894288465500027e-11,5.8997432127098804e-12],[0.0032375059510564934,0.0066344212488368935,0.006797755119593666,0.004643406755242645,0.002142102134204004,0.0009277096721199576,0.00031684970130869055,9.275722126975185e-05,2.3760206509206832e-05,5.410036179581509e-06,1.1086453439592637e-06,2.065344108756758e-07,3.5269852391634104e-08,5.559717921707342e-09,8.137990715017053e-10,1.1117788268451467e-10,1.423937358018865e-11,1.7164629388957685e-12],[0.0007535323188265337,0.0015441673013996127,0.001582183401519552,0.0010807569506987222,0.0005536821388856382,0.00020434026203514641,7.37470428644985e-05,2.158932372263069e-05,5.530208678330706e-06,1.2591906143076491e-06,2.5803816561858315e-07,4.807106331150783e-08,8.209088742729496e-09,1.2940291696447499e-09,1.8941243990839524e-10,2.5876748647874467e-11,3.31422655424475e-12,3.9950823815593527e-13],[0.00014615441744871506,0.0002995052325438067,0.00030687879944715383,0.00020962259824370435,0.0001073916651466383,4.401422304501588e-05,1.3536463791892907e-05,4.187444855327027e-06,1.0726340563732595e-06,2.442314232488681e-07,5.0048839091931323e-08,9.323818075082583e-09,1.5922271055962922e-09,2.509886765647951e-10,3.6738258095501953e-11,5.0190297477705816e-12,6.428242548150242e-13,7.748824085551246e-14],[2.429826247024945e-05,4.979293050869391e-05,5.101879057564908e-05,3.484988685756593e-05,1.785393087941249e-05,7.317391856097471e-06,2.4991799629133676e-06,6.588141625323733e-07,1.7832607656509074e-07,4.0603625461173177e-08,8.320650513445837e-09,1.5500905327935701e-09,2.6470874298137356e-10,4.172702301230071e-11,6.107758174449356e-12,8.344168057740196e-13,1.0686993071022836e-13,1.2882468060370635e-14],[3.5346510437856974e-06,7.243342358787879e-06,7.4216673550917725e-06,5.069588375207153e-06,2.597198688419024e-06,1.0644558142217796e-06,3.6355394034186456e-07,1.0642980930231846e-07,2.4549165479851225e-08,5.906580657507643e-09,1.2103991410224235e-09,2.2549057268640461e-10,3.85069934866296e-11,6.070000504154746e-12,8.884912587038331e-13,1.2138202215457376e-13,1.5546293180293228e-14,1.8740035108221262e-15],[4.5705172052739053e-07,9.36607898896637e-07,9.596663975614567e-07,6.555283847121881e-07,3.3583347108065093e-07,1.3764056346404796e-07,4.7009719454454804e-08,1.3762016916082298e-08,3.525206549238708e-09,7.227789490366756e-10,1.5651191675675787e-10,2.915729245471631e-11,4.979186744995167e-12,7.848877130045367e-13,1.1488728404408638e-13,1.5695428312330267e-14,2.010229569441779e-15,2.4231996830393556e-16],[5.3189592235385993e-08,1.0899815051405814e-07,1.1168159329844743e-07,7.628740012471513e-08,3.908276587420399e-08,1.601798027858586e-08,5.470776493297318e-09,1.601560688270145e-09,4.102474413249301e-10,9.341053072449512e-11,1.72369045202557e-11,3.3931925572115103e-12,5.794550173108039e-13,9.134164806797631e-14,1.337005751621431e-14,1.8265622781799565e-15,2.3394133813727977e-16,2.820009142445745e-17],[5.627238062610395e-09,1.1531551860982109e-08,1.1815448968302038e-08,8.070890255740475e-09,4.134794392597308e-09,1.6946358210626523e-09,5.787854431911962e-10,1.6943847256303112e-10,4.340247630957268e-11,9.882446393183978e-12,2.0251487821987063e-12,3.3972514007233453e-13,6.130393544947354e-14,9.66356719628553e-15,1.4144965846246515e-15,1.93242706768948e-16,2.475002245849716e-17,2.9834526110021114e-18],[5.457268920906038e-10,1.1183244582967075e-09,1.1458566658072867e-09,7.827111287391316e-10,4.009904091846865e-10,1.643449823100117e-10,5.613033917983769e-11,1.6432063119346307e-11,4.209151672973937e-12,9.583949881627187e-13,1.9639797332791262e-13,3.6587841133753584e-14,5.6262493401740255e-15,9.37168186926009e-16,1.3717721134440474e-16,1.8740586520569836e-17,2.4002454996870548e-18,2.893338264680602e-19],[4.885323368569181e-11,1.0011191841453774e-10,1.0257658963908491e-10,7.006795933071957e-11,3.589648677670133e-11,1.4712091235058505e-11,5.024763515510412e-12,1.4709911333711324e-12,3.768014244461619e-13,8.579510190627691e-14,1.7581461030129767e-14,3.2753276022642363e-15,5.593272354776867e-16,7.939370168299046e-17,1.2280044211284937e-17,1.6776491427589807e-18,2.1486893169225358e-19,2.5901038124529175e-20],[4.060940186881103e-12,8.32183423703289e-12,8.52671079623074e-12,5.824420829325915e-12,2.9839065855336984e-12,1.2229471423302827e-12,4.176850241069409e-13,1.2227659373553748e-13,3.132173515579624e-14,7.131744428840168e-15,1.4614643955953505e-15,2.722626217705492e-16,4.649424975185821e-17,7.329061395875232e-18,9.66014756304934e-19,1.3945510479712475e-19,1.786104652222525e-20,2.1530318193173374e-21],[3.1506245053004316e-13,6.456380461092368e-13,6.61533111740975e-13,4.5187966701253363e-13,2.3150228216313937e-13,9.488066945088777e-14,3.240551724203119e-14,9.486661091251601e-15,2.4300536769583044e-15,5.533065676670487e-16,1.1338570199240436e-16,2.1123120473400604e-17,3.607192322038794e-18,5.68615132754034e-19,8.323056557785735e-20,1.0238940591282498e-20,1.3857246911694419e-21,1.6704000794068778e-22],[2.2915955842258702e-14,4.6960254799740485e-14,4.8116376773380706e-14,3.28673076650445e-14,1.683823656709209e-14,6.901111915312667e-15,2.357003828652466e-15,6.900089372499354e-16,1.767490942250028e-16,4.024455739031567e-17,8.24706890849779e-18,1.5363826923989509e-18,2.623678569988564e-19,4.135802045438921e-20,6.053745732948023e-21,8.2703784812338185e-22,9.538253016130629e-23,1.2149595863993103e-23],[1.5687378244599132e-15,3.2147176603813444e-15,3.2938613051947165e-15,2.2499689333157015e-15,1.1526806379723694e-15,4.72423466291464e-16,1.6135137822117178e-16,4.7235346696001924e-17,1.2099560300185229e-17,2.7549869550024947e-18,5.645624833082519e-19,1.0517482486884717e-19,1.7960690098625527e-20,2.8312103356362665e-21,4.144160503846704e-22,5.661581666249206e-23,7.251206305955144e-24,7.870906919796851e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.22125432650399685, "-10": 1.7983817936540706e-05, "-11": 3.2916983341075057e-06, "-12": 5.537655950490338e-07, "-13": 8.617545308230137e-08, "-14": 1.247339511041466e-08, "-15": 1.6867748237306178e-09, "-16": 2.1245624511091924e-10, "-17": 2.2459517464603906e-11, "-2": 0.17549955020934677, "-3": 0.1016883305904642, "-4": 0.046895989551311544, "-5": 0.017872900347731736, "-6": 0.005788641794770583, "-7": 0.0016274753285326839, "-8": 0.0004038474947552286, "-9": 8.962789051603231e-05, "0": 0.21480484494075183, "1": 0.12851897374057208, "10": 6.594014991300026e-08, "11": 6.854202096120969e-09, "12": 6.548347116284183e-10, "13": 5.7870621022768695e-11, "14": 4.7569445786970364e-12, "15": 3.6531656663497833e-13, "16": 2.6130673502640046e-14, "17": 1.5687378244599132e-15, "2": 0.05948305727170603, "3": 0.019572992816647043, "4": 0.0051261424225241044, "5": 0.0011094783773741104, "6": 0.00020406537873212188, "7": 3.2581862915609375e-05, "8": 4.5914275560881315e-06, "9": 5.786851836800346e-07} |
| Raw goal margin distribution | {"-1": 0.22085630895535835, "-10": 1.7951466591175566e-05, "-11": 3.28577685124884e-06, "-12": 5.527694182594343e-07, "-13": 8.602043083649678e-08, "-14": 1.2450956542891516e-08, "-15": 1.6837404605565521e-09, "-16": 2.1207405455578692e-10, "-17": 2.2419114719825472e-11, "-2": 0.17518384157727074, "-3": 0.10150540200910592, "-4": 0.046811627690022235, "-5": 0.01784074853359157, "-6": 0.005778228524876585, "-7": 0.001624547640062282, "-8": 0.00040312100776432504, "-9": 8.946665763152104e-05, "0": 0.22657477511012697, "1": 0.12206908866834842, "10": 6.263086120483978e-08, "11": 6.510215410769635e-09, "12": 6.219710144763404e-10, "13": 5.49663116916926e-11, "14": 4.518211378963686e-12, "15": 3.4698269887058695e-13, "16": 2.4819273045209988e-14, "17": 1.4900087591575316e-15, "2": 0.05649782581536519, "3": 0.018590697747580695, "4": 0.004868880568287146, "5": 0.0010537978205201065, "6": 0.0001938241030532572, "7": 3.0946701467239646e-05, "8": 4.36100103467824e-06, "9": 5.49643145612806e-07} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.52, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.62, "price": 1.52, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:59Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.71, "draw": 4.33, "home": 4.38}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:58Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.7, "draw": 4.4, "home": 4.23}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.23 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:58Z |
| Market reference home last update utc | 2026-11-05T13:36:58Z |
| Market reference draw last update utc | 2026-11-05T13:36:58Z |
| Market reference away last update utc | 2026-11-05T13:36:58Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 2.94 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:16Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:16Z |
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
