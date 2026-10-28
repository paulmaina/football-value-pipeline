# Eredivisie — football model report

Fixtures in this report: **1**.

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
| Training as of utc | 2026-10-28T16:14:25.998108+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1314, 'tuning_matches': 189, 'audit_matches': 111, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6975442993296386, 'audit_candidate_poisson_score': 0.6897612672790439, 'audit_gain': 0.007783032050594718, 'audit_gain_lower95': -0.004023726923927405, 'audit_baseline_briers': [0.6185565974902838, 0.09069928592477247, 0.2827177901715695, 0.22289472155761134], 'audit_candidate_briers': [0.617646204983342, 0.08929912487105075, 0.2791576066179441, 0.21726565343662246], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1619.008 |
| Base scoring parameter | 0.292 |
| Home-advantage parameter | 0.184 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1620, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 7.00 |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'AVAILABLE': 1} |
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

## 2026-10-31 — Feyenoord vs Fortuna Sittard

The model's most likely 1X2 outcome is **Feyenoord win** at **82.7%**. Expected goals are 2.73 for Feyenoord and 0.83 for Fortuna Sittard (3.56 combined). The most likely exact score is 2-0 at 11.4%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 71.2%; Under 3.5 goals: 50.9%; Double Chance 1X: 93.8%; Double Chance X2: 17.3%; Double Chance 12 (either team wins): 88.9%; Under 4.5 goals: 70.0%; BTTS Yes (both teams score): 51.9%; BTTS No (at least one team does not score): 48.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 82.7% | 1.21 |
| Draw | 11.1% | 9.02 |
| Fortuna Sittard win | 6.2% | 16.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 2.73 |
| Fortuna Sittard expected goals | 0.83 |
| Expected total goals | 3.56 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 88.5% |
| Under 1.5 | 11.5% |
| Over 2.5 | 71.2% |
| Under 2.5 | 28.8% |
| Over 3.5 | 49.1% |
| Under 3.5 | 50.9% |
| Over 4.5 | 30.0% |
| Under 4.5 | 70.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.41% |
| 2 | 3-0 | 10.39% |
| 3 | 2-1 | 9.50% |
| 4 | 3-1 | 8.65% |
| 5 | 1-0 | 7.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Feyenoord win | 82.7% | 85.3% | 1.15 | -4.9% |
| Draw | 11.1% | 9.3% | 8.12 | -10.0% |
| Fortuna Sittard win | 6.2% | 5.4% | 13.22 | -17.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:30:00+00:00 |
| Fixture id | 1836e9e3241ea98ae062bab0f288ce2c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:14:17Z |
| Market best draw last update utc | 2026-10-28T16:14:17Z |
| Market best away last update utc | 2026-10-28T16:14:17Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Feyenoord |
| Matched away-team name | For Sittard |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7316 |
| Dc lambda away | 0.8329 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 51.9% |
| P btts no | 48.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 39.89 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.68 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.47 |
| Fair Over 3.5 odds | 2.04 |
| Fair Under 3.5 odds | 1.96 |
| Fair Over 4.5 odds | 3.33 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.04282100892171639, "-10": 1.1647577262708622e-09, "-11": 8.672241697467043e-11, "-12": 5.933951171201609e-12, "-13": 3.7555012522092783e-13, "-14": 2.2105947474829933e-14, "-15": 1.216072640876287e-15, "-16": 6.278423051857419e-17, "-17": 3.0528272873794585e-18, "-18": 1.3949375652913456e-19, "-19": 5.461175606644128e-21, "-2": 0.01493745518851373, "-3": 0.003540386937002911, "-4": 0.0006664953672906333, "-5": 0.0001035628591670105, "-6": 1.3664512857432984e-05, "-7": 1.5642764656062101e-06, "-8": 1.5799365579703746e-07, "-9": 1.4268354813599195e-08, "0": 0.1108336734149185, "1": 0.21564818845328193, "10": 0.000239343361869651, "11": 5.8443142867112085e-05, "12": 1.3114826823993327e-05, "13": 2.7220926668960643e-06, "14": 5.254852506725504e-07, "15": 9.48041431402263e-08, "16": 1.6052207975571517e-08, "17": 2.5597811664139806e-09, "18": 3.8359397467769263e-10, "19": 4.925151012876381e-11, "2": 0.2293671310338628, "3": 0.17828783001597848, "4": 0.11007393874594046, "5": 0.05609288873826084, "6": 0.024272489985578346, "7": 0.009112763322624033, "8": 0.0030185100785138997, "9": 0.000894011869747244} |
| Raw goal margin distribution | {"-1": 0.056587614339575806, "-10": 1.539217843599909e-09, "-11": 1.1460296732685739e-10, "-12": 7.841668116687883e-12, "-13": 4.962864301033252e-13, "-14": 2.9212829445552796e-14, "-15": 1.6070300850832568e-15, "-16": 8.296884899856526e-17, "-17": 4.034286382634764e-18, "-18": 1.8433986251188384e-19, "-19": 7.216899060796109e-21, "-2": 0.019739725305576234, "-3": 0.004678592486464995, "-4": 0.0008807681965715938, "-5": 0.00013685747445045705, "-6": 1.8057542388321637e-05, "-7": 2.0671786019340453e-06, "-8": 2.0878732863784382e-07, "-9": 1.8855514612657985e-08, "0": 0.15237480984307653, "1": 0.19961287126378802, "10": 0.00022154610258216518, "11": 5.409738721691762e-05, "12": 1.2139625457747787e-05, "13": 2.519681417138082e-06, "14": 4.864108548551214e-07, "15": 8.775463107599186e-08, "16": 1.4858586789480375e-08, "17": 2.369439187501261e-09, "18": 3.550704285257246e-10, "19": 4.558923226480024e-11, "2": 0.21231169122074794, "3": 0.16503058020628608, "4": 0.10188898465591126, "5": 0.05192189491056235, "6": 0.0224676193827266, "7": 0.00843515016297201, "8": 0.0027940576177915575, "9": 0.0008275343166298654} |
| Unadjusted home-win probability | 76.6% |
| Unadjusted draw probability | 15.2% |
| Unadjusted away-win probability | 8.2% |
| Raw p over 1 5 | 87.7% |
| Raw p under 3 5 | 52.3% |
| Raw p btts yes | 53.5% |
| P home draw | 93.8% |
| P draw away | 17.3% |
| P home away | 88.9% |
| Raw p home draw | 91.8% |
| Raw p draw away | 23.4% |
| Raw p home away | 84.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7120 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:14:17Z", "line": 2.25, "market_key": "spreads", "opposite_price": 1.92, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:13:24Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:13:24Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.76, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:14:17Z", "line": -2.25, "market_key": "spreads", "opposite_price": 1.88, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.15 |
| Reference draw odds | 8.12 |
| Reference away odds | 13.22 |
| Market reference 1x2 last update utc | 2026-10-28T16:14:17Z |
| Market reference home last update utc | 2026-10-28T16:14:17Z |
| Market reference draw last update utc | 2026-10-28T16:14:17Z |
| Market reference away last update utc | 2026-10-28T16:14:17Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.67 |
| Market reference over 2 5 last update utc | 2026-10-28T16:13:26Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:13:26Z |
| Home probability edge | -2.6% |
| Draw probability edge | +1.8% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | -0.0879 |
| Raw ev home | -0.1196 |
| Raw edge prob draw | 0.0593 |
| Raw ev draw | 0.2373 |
| Raw edge prob away | 0.0285 |
| Raw ev away | 0.0846 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.02793873696660029, 0.01419137182145395, 0.008507854061016762, 0.0024493150238745986, 0.000528847583934186, 9.134954525877126e-05, 1.3149250799424384e-05, 1.622366007997434e-06, 1.7514781382207394e-07, 1.6807691995206027e-08, 1.451623366783336e-09, 1.1397435280294862e-10, 8.202981993302e-12, 5.449721080167218e-13, 3.361956650000689e-14, 1.935738641825668e-15, 1.0448948929384002e-16, 5.308472289160288e-18, 2.547081954786215e-19, 1.1578043783808086e-20], [0.07426358252514002, 0.05790577289056155, 0.022969175919410098, 0.006612566137354077, 0.0014277622891532796, 0.0002466219754310262, 3.5499839636921046e-05, 4.3800011114566235e-06, 4.7285730558224005e-07, 4.537675793077847e-08, 3.919036720804786e-09, 3.0770355733146847e-10, 2.2146094081612592e-11, 1.471294656729442e-12, 9.076480763948115e-14, 5.226032449454135e-15, 2.8209668902485905e-16, 1.433160853472191e-17, 6.876513522805746e-19, 3.125795559792883e-20], [0.1100978380125444, 0.09508776953844801, 0.030585979203992437, 0.008926175378557699, 0.0019273087523284406, 0.0003329102437959952, 4.7920548230104416e-05, 5.912478947966095e-06, 6.383009486765178e-07, 6.125320956904015e-08, 5.290232015570998e-09, 4.1536309207272293e-10, 2.9894584888282334e-11, 1.9860722549622528e-12, 1.225216616911215e-13, 7.054520319176241e-15, 3.807968748655728e-16, 1.934596170087609e-17, 9.28247285888749e-19, 4.2194510852019335e-20], [0.09907929745543961, 0.08557142967149582, 0.03695257114291204, 0.007924121598373446, 0.0017344245864179863, 0.0002995927410242889, 4.3124681992186644e-05, 5.32076079748098e-06, 5.744200858222508e-07, 5.5123016768956205e-08, 4.760788049437697e-09, 3.7379374649296427e-10, 2.6902748699893063e-11, 1.7873070649668894e-12, 1.1025975062331584e-13, 6.34850719802025e-15, 3.4268690026964116e-16, 1.7409826827882385e-17, 8.3534872810396975e-19, 3.7971703778757816e-20], [0.06687261549458158, 0.05775561051305578, 0.024940781223115747, 0.007180169020159047, 0.001154788367619332, 0.00020220722885621448, 2.9106587867022425e-05, 3.5911961437616564e-06, 3.8769929256747055e-07, 3.720474811551464e-08, 3.213247942380998e-09, 2.522884813020114e-10, 1.815775056705887e-11, 1.2063256522386455e-12, 7.441875444542369e-14, 4.284863656897919e-15, 2.3129321568986953e-16, 1.1750594576145845e-17, 5.638105611670103e-19, 2.5628634958913024e-20], [0.03610802109368922, 0.03118527348243605, 0.013466831644566385, 0.0038769486211760874, 0.0008370972665257784, 0.00010770444909983439, 1.5716168432995134e-05, 1.9390745397273716e-06, 2.0933911632585846e-07, 2.008878850938986e-08, 1.7350005473039639e-09, 1.3622374027356482e-10, 9.804318787896567e-12, 6.513582843252295e-13, 4.0182576012735183e-14, 2.3136218938436553e-15, 1.2488729877230109e-16, 6.344760313034908e-18, 3.0443079704445984e-19, 1.3838239836362822e-20], [0.016247173546047745, 0.014032132889128418, 0.006059538690225203, 0.0017444727007863467, 0.0003766604801984987, 6.506177701922763e-05, 6.975934509573489e-06, 8.725064296359198e-07, 9.41942773351525e-08, 9.039155936987944e-09, 7.806812486730828e-10, 6.129526576861235e-11, 4.4115535557713605e-12, 2.930853246880791e-13, 1.8080561222455535e-14, 1.0410378439649045e-15, 5.619431792138066e-17, 2.85488982202824e-18, 1.3698175204642939e-19, 6.226657606348667e-21], [0.006266213123207745, 0.005411915802292933, 0.0023370440866935173, 0.0006728085780436668, 0.0001452704888837548, 2.5093039095176913e-05, 3.6120011703130012e-06, 3.3195374041188763e-07, 3.6328867608617586e-08, 3.486223458778373e-09, 3.010932991891059e-10, 2.3640370287250228e-11, 1.7014488524148774e-12, 1.1303720629160116e-13, 6.97331444672555e-15, 4.015076826206267e-16, 2.1673035707452082e-17, 1.1010744741172108e-18, 5.2831149361491695e-20, 2.401498543487564e-21], [0.0021146600327067956, 0.0018263601672112773, 0.000788682674469049, 0.00022705282786853332, 4.902445715363653e-05, 8.468152268423969e-06, 1.218942663258957e-06, 1.5039420669166672e-07, 1.2093968815864122e-08, 1.1764964370681302e-09, 1.0161000805301251e-10, 7.977919873118868e-12, 5.741882401942202e-13, 3.814668567023096e-14, 2.3532856393557645e-15, 1.3549686749689177e-16, 7.314003130253366e-18, 3.715797943140155e-19, 1.782893716508623e-20, 8.104341312152926e-22], [0.0006343419458542988, 0.0005478596296240772, 0.00023658389275172748, 6.810982872622188e-05, 1.470603740757433e-05, 2.54022117251003e-06, 3.6565048231737133e-07, 4.5114274749823665e-08, 4.870458673103871e-09, 3.4814092381886977e-10, 3.0480308526999946e-11, 2.3931644509808492e-12, 1.722412491549459e-13, 1.1442994354498088e-14, 7.059233013966426e-16, 4.064546795028866e-17, 2.194007029910441e-18, 1.1146408695471593e-19, 5.348208467976915e-21, 2.4310875310004376e-22], [0.00017125718944980352, 0.0001479090276082426, 6.387200595286005e-05, 1.8388028598442097e-05, 3.970279201658421e-06, 6.857991047700227e-07, 9.87169054985074e-08, 1.2179777718019058e-08, 1.3149076285092017e-09, 1.261823481541173e-10, 8.117575362817242e-12, 6.460972988538577e-13, 4.650102745117007e-14, 3.0893354362718294e-15, 1.9058244745505713e-16, 1.0973306511622874e-17, 5.923295472279493e-19, 3.0092643851172495e-20, 1.4438886736141243e-21, 6.563356255826507e-23], [4.20321407375197e-05, 3.630173474615825e-05, 1.567628869785466e-05, 4.513026334358905e-06, 9.744369547782835e-07, 1.6831763140552742e-07, 2.4228371833124547e-08, 2.9893176037759093e-09, 3.22721531726039e-10, 3.096929380450399e-11, 2.6747128964654335e-12, 1.5642717808846623e-13, 1.1412879871181894e-14, 7.582244124171181e-16, 4.677519395984168e-17, 2.6932099325830855e-18, 1.4537713115614282e-19, 7.385723458268456e-21, 3.5437771771005286e-22, 1.610863256261949e-23], [9.456395897499647e-06, 8.167168493020903e-06, 3.5268532491871487e-06, 1.0153411880695411e-06, 2.1922893908927187e-07, 3.786812023303126e-08, 5.450901904725941e-09, 6.725370211619174e-10, 7.260592763301168e-11, 6.96747531157639e-12, 6.01757217627209e-13, 4.7247027702193894e-14, 2.5329170683818403e-15, 1.7058541623517648e-16, 1.0523488561498822e-17, 6.05918682958018e-19, 3.2706963826566696e-20, 1.6616409201469122e-21, 7.972794002679152e-23, 3.624122022019883e-24], [1.9638471190673993e-06, 1.6961081674042435e-06, 7.324355566184604e-07, 2.1085991837419403e-07, 4.5528140436728686e-08, 7.864222229084092e-09, 1.1320103470652563e-09, 1.3966842185871497e-10, 1.5078360017372717e-11, 1.446963141785386e-12, 1.249693002518725e-13, 9.811977019911413e-15, 7.061893209622513e-16, 3.4946647372982066e-17, 2.185454471031886e-18, 1.2583352820823043e-19, 6.792384475064967e-21, 3.4507953868744393e-22, 1.655741648593544e-23, 7.526357471956435e-25], [3.787084736491699e-07, 3.270776675969486e-07, 1.4124294554307293e-07, 4.06622476189497e-08, 8.779651127357857e-09, 1.51653739636751e-09, 2.1829698785093529e-10, 2.693367235440438e-11, 2.90771244455303e-12, 2.79032516091363e-13, 2.4099092282634652e-14, 1.892142623839271e-15, 1.3618161885022957e-16, 9.0473420468969e-18, 4.1573893413120224e-19, 2.4265750087643774e-20, 1.309844097340802e-21, 6.654517254171071e-23, 3.1929338409702412e-24, 1.4513835230189447e-25], [6.816150105564534e-08, 5.886877726913596e-08, 2.5421483414324775e-08, 7.318557747856264e-09, 1.5801975430314277e-09, 2.729526074433435e-10, 3.9289985313689686e-11, 4.847632583784845e-12, 5.233419863811091e-13, 5.0221414263204473e-14, 4.3374532611715615e-15, 3.40555573551093e-16, 2.4510525121279553e-17, 1.6283776503285519e-18, 1.004553258726884e-19, 4.308334672252422e-21, 2.357511015355164e-22, 1.1977072508421967e-23, 5.746773006550493e-25, 2.612259466579773e-26], [1.1501236809025832e-08, 9.933228252667025e-09, 4.289496214970108e-09, 1.2348974781219878e-09, 2.666347698623634e-10, 4.6056681957225694e-11, 6.629599089183581e-12, 8.179657056516885e-13, 8.830615559010767e-14, 8.474114703749806e-15, 7.318805532772781e-16, 5.746367432323927e-17, 4.13578558816179e-18, 2.747644444576473e-19, 1.6950338148311045e-20, 9.759621542321399e-22, 3.924105894233578e-23, 2.0209523714241186e-24, 9.696822430905134e-26, 4.4077982829671136e-27], [1.8265055936944195e-09, 1.5774909488605258e-09, 6.812127218027049e-10, 1.961134431784637e-10, 4.2344132784470615e-11, 7.314238339641914e-12, 1.0528432742852883e-12, 1.2990071951657842e-13, 1.4023855853172626e-14, 1.3457698650166438e-15, 1.162295800594286e-16, 9.125777021064655e-18, 6.568020149946039e-19, 4.36352022902779e-20, 2.6918746180937356e-21, 1.5499205551007586e-22, 8.366336433505394e-24, 3.1660234528075374e-25, 1.5399474600166862e-26, 7.000002133160155e-28], [2.7395162685673383e-10, 2.366027310751368e-10, 1.0217287809991601e-10, 2.941441679274936e-11, 6.351058602935789e-12, 1.0970387932455637e-12, 1.5791253462970792e-13, 1.948338596075533e-14, 2.103392477441121e-15, 2.018476401982251e-16, 1.7432896267101503e-17, 1.3687455816632569e-18, 9.851159566755527e-20, 6.544701914361748e-21, 4.03745509166234e-22, 2.324675374849043e-23, 1.254839560690128e-24, 6.375072823385231e-26, 2.278454547209503e-27, 1.0499075277952108e-28], [3.8926527650387e-11, 3.361952202667491e-11, 1.4518020608638115e-11, 4.179574042835514e-12, 9.024390953724731e-13, 1.5588120942663036e-13, 2.243821917079053e-14, 2.7684470102494733e-15, 2.9887672642129157e-16, 2.868107715764945e-17, 2.4770873834691177e-18, 1.9448876191132626e-19, 1.399777908470769e-20, 9.299543972636245e-22, 5.736929145705737e-23, 3.3031941184477294e-24, 1.7830354729577353e-25, 9.058513409103196e-27, 4.34640604390636e-28, 1.471649608470681e-29]] |
| Legacy trial inputs | {"lambda_home": 2.6997613916129026, "lambda_away": 0.863666092404229, "rho": -0.10359756684002812, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8037 |
| Legacy p draw | 0.1256 |
| Legacy p away | 0.0707 |
| Legacy p over 1 5 | 0.8836 |
| Legacy p under 3 5 | 0.5125 |
| Legacy p btts yes | 0.5344 |
| Legacy p over 2 5 | 0.7071 |
| Legacy goal margin distribution | {"-1": 0.04803998114606062, "-10": 1.7910856057578575e-09, "-11": 1.3822119154963384e-10, "-12": 9.803384596279838e-12, "-13": 6.431461841276796e-13, "-14": 3.924438329995548e-14, "-15": 2.2380422699144657e-15, "-16": 1.1978731681822944e-16, "-17": 6.038318152292881e-18, "-18": 2.8596615107655034e-19, "-19": 1.1578043783808086e-20, "-2": 0.017378465138681555, "-3": 0.0042569221224786815, "-4": 0.000829119461381318, "-5": 0.0001333752867137218, "-6": 1.8226029874994427e-05, "-7": 2.1614997041946018e-06, "-8": 2.262074251132636e-07, "-9": 2.1170242128099553e-08, "0": 0.12562442381488317, "1": 0.21439001866494484, "10": 0.0002113056967288898, "11": 5.0974034361628536e-05, "12": 1.1301339677884005e-05, "13": 2.3176246311665916e-06, "14": 4.420693675162668e-07, "15": 7.880625888600319e-08, "16": 1.3185080210029108e-08, "17": 2.0776263453781946e-09, "18": 3.0757114888340875e-10, "19": 3.8926527650387e-11, "2": 0.2248900164510524, "3": 0.17220032911507624, "4": 0.10484190270391308, "5": 0.05271966765016268, "6": 0.022520026041898015, "7": 0.008348558676320157, "8": 0.0027311320110136998, "9": 0.000798989688148478} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7540 |
| Legacy raw p draw | 0.1582 |
| Legacy raw p away | 0.0878 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.6998 |
| Legacy lambda away | 0.8637 |
| Legacy model home team | Feyenoord |
| Legacy model away team | For Sittard |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,614.9048 |
| Elo away rating | 1,453.3704 |
| Elo rating diff | 221.5344 |
| Elo home expectancy | 0.7816 |

</details>


---
