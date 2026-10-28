# Primeira Liga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,611 |
| Training data through | 2026-10-26 |
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
| Training sha256 | 84c0a9d8af08458f9d90e4a3ffe4465c5e09f0dc593fdcb0fb4ebd37c58b23a7 |
| Training as of utc | 2026-10-28T12:13:24.224429+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1611, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1305, 'tuning_matches': 197, 'audit_matches': 103, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8910498907404766, 'audit_candidate_poisson_score': 0.8787218636559287, 'audit_gain': 0.012328027084547832, 'audit_gain_lower95': 0.0008780097723124651, 'audit_baseline_briers': [0.6072179100391997, 0.18432497321850397, 0.24265429790114143, 0.2511458707386006], 'audit_candidate_briers': [0.6028489965068238, 0.183492365578184, 0.24110273505874388, 0.24950419867902912], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1464.943 |
| Base scoring parameter | 0.094 |
| Home-advantage parameter | 0.170 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1611, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
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
| Shot features applied fixtures | 1 |
| Goal rate features used | {'shot_features': 1} |
| Legacy comparison status | {'AVAILABLE': 1} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Casa Pia vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **76.1%**. Expected goals are 0.73 for Casa Pia and 2.38 for Sporting Lisbon (3.11 combined). The most likely exact score is 0-2 at 12.9%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 60.3%; Under 3.5 goals: 62.0%; Double Chance 1X: 23.9%; Double Chance X2: 91.6%; Double Chance 12 (either team wins): 84.5%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 46.5%; BTTS No (at least one team does not score): 53.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Casa Pia win | 8.4% | 11.88 |
| Draw | 15.5% | 6.46 |
| Sporting Lisbon win | 76.1% | 1.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Casa Pia expected goals | 0.73 |
| Sporting Lisbon expected goals | 2.38 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.93% |
| 2 | 0-1 | 11.28% |
| 3 | 0-3 | 10.24% |
| 4 | 1-2 | 9.44% |
| 5 | 1-3 | 7.47% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:15:00+00:00 |
| Fixture id | 75daf3f21fd7945dcc4215b1fe8a5da3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Casa Pia |
| Matched away-team name | Sp Lisbon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6959 |
| Dc lambda away | 2.5772 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 0.8098 |
| Shot lambda away | 1.9042 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 46.5% |
| P btts no | 53.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.57 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.43 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.88 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.23879987184929757, "-10": 8.444046655920716e-05, "-11": 1.799975309446914e-05, "-12": 3.5240700917006007e-06, "-13": 6.378692898655251e-07, "-14": 1.0734282979765445e-07, "-15": 1.6876747479998545e-08, "-16": 2.489324219944506e-09, "-17": 3.4449016834855474e-10, "-18": 4.146424091947873e-11, "-2": 0.22222677688125117, "-3": 0.1552216713073305, "-4": 0.08517720846157459, "-5": 0.03833352041112692, "-6": 0.014590747854322277, "-7": 0.004805644815454774, "-8": 0.001393899095031457, "-9": 0.00036102872125178524, "0": 0.15482295574064672, "1": 0.06250584358317877, "10": 5.216607643951268e-10, "11": 3.417935629287875e-11, "12": 2.0568454078180025e-12, "13": 1.144322901455178e-13, "14": 5.9190187861500495e-15, "15": 2.86038974818848e-16, "16": 1.2968140510232993e-17, "17": 5.516109222629147e-19, "18": 2.0407486911223133e-20, "2": 0.017232793278936093, "3": 0.0036997419037207036, "4": 0.0006240253868539057, "5": 8.632117491253205e-05, "6": 1.009894419644522e-05, "7": 1.0223741763732634e-06, "8": 9.114845691667379e-08, "9": 7.25637168486885e-09} |
| Raw goal margin distribution | {"-1": 0.23348319745172522, "-10": 8.256047197127988e-05, "-11": 1.7599004024970548e-05, "-12": 3.4456096926781957e-06, "-13": 6.236676770415204e-07, "-14": 1.0495293372891483e-07, "-15": 1.650100116763106e-08, "-16": 2.4339015505563577e-09, "-17": 3.368203901192347e-10, "-18": 4.054107514721864e-11, "-2": 0.21727908823322203, "-3": 0.15176579388412614, "-4": 0.08328081094688025, "-5": 0.037480057446677435, "-6": 0.014265897363583885, "-7": 0.004698651254041649, "-8": 0.0013628651268221693, "-9": 0.0003529907263223783, "0": 0.15567562945665803, "1": 0.07445646911937244, "10": 6.213981984466275e-10, "11": 4.071418031426451e-11, "12": 2.450098067818699e-12, "13": 1.3631084373960403e-13, "14": 7.0506886109216124e-15, "15": 3.4072737642833694e-16, "16": 1.544754695056531e-17, "17": 6.570745908696135e-19, "18": 2.4309237855296995e-20, "2": 0.020527567777021936, "3": 0.004407103448455203, "4": 0.0007433341313786549, "5": 0.00010282510443475611, "6": 1.2029782874624614e-05, "7": 1.2178440754948122e-06, "8": 1.0857532478005209e-07, "9": 8.64373286241871e-09} |
| Unadjusted home-win probability | 10.0% |
| Unadjusted draw probability | 15.6% |
| Unadjusted away-win probability | 74.4% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 62.4% |
| Raw p btts yes | 46.6% |
| P home draw | 23.9% |
| P draw away | 91.6% |
| P home away | 84.5% |
| Raw p home draw | 25.6% |
| Raw p draw away | 90.0% |
| Raw p home away | 84.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6030 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:13:23Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.89, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:13:23Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.8, "price": 1.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 11.00 |
| Reference draw odds | 5.75 |
| Reference away odds | 1.28 |
| Market reference 1x2 last update utc | 2026-10-28T12:12:09Z |
| Market reference home last update utc | 2026-10-28T12:12:09Z |
| Market reference draw last update utc | 2026-10-28T12:12:09Z |
| Market reference away last update utc | 2026-10-28T12:12:09Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-28T12:13:23Z |
| Market reference under 2 5 last update utc | 2026-10-28T12:13:23Z |
| Home probability edge | +0.7% |
| Draw probability edge | +0.0% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | 0.0230 |
| Raw edge prob draw | 0.0012 |
| Raw edge prob away | -0.0242 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.03844343131935376, 0.10498777040177024, 0.12669821605428092, 0.10552703252466561, 0.06592015424682984, 0.032942965471222885, 0.01371910945948639, 0.00489713821628515, 0.0015295611885518866, 0.0004246575269421545, 0.00010610926511767877, 2.4103222071437976e-05, 5.0188976188744344e-06, 9.64671537111501e-07, 1.721733420271186e-07, 2.8680659333343776e-08, 4.479026468201142e-09, 6.583384005040237e-10, 9.13884188293815e-11], [0.030270789623692618, 0.07058824777802208, 0.08936729483859569, 0.07443408220549468, 0.046497149240508975, 0.023236504820739978, 0.009676850536424437, 0.003454223812059132, 0.0010788845334051625, 0.0002995345601346858, 7.484476321920488e-05, 1.7001342406395818e-05, 3.5401074872160573e-06, 6.804364604668949e-07, 1.2144342911420178e-07, 2.0230063363403227e-08, 3.1593063536278636e-09, 4.643626703962948e-10, 6.446133201164719e-11], [0.00949017883942257, 0.02371312972450019, 0.03273945136478415, 0.02625124795620181, 0.01639851204988751, 0.008194999274669568, 0.003412810305976073, 0.0012182280361332533, 0.0003804986178823241, 0.00010563918807837504, 2.6396086030406146e-05, 5.995995945331068e-06, 1.2485173012807706e-06, 2.399748302510565e-07, 4.283040075011486e-08, 7.134694131865972e-09, 1.114217197301139e-09, 1.6377040249550203e-10, 2.2734080411619337e-11], [0.0022313168957073157, 0.005575396196389913, 0.006965627071287272, 0.006411379444640566, 0.003855594043115035, 0.0019267961806915745, 0.0008024149414271528, 0.00028642798474531834, 8.946227560510018e-05, 2.4837730584055373e-05, 6.206208938394752e-06, 1.4097697510012167e-06, 2.93549552233748e-07, 5.642252926355365e-08, 1.0070220852598962e-08, 1.6774987944384219e-09, 2.6197310924194917e-10, 3.850545624988828e-11, 5.345203561401109e-12], [0.0003934679609292693, 0.0009831592173154499, 0.001228310996795602, 0.0010230610859881502, 0.0007062428927993028, 0.0003397691138365596, 0.00014149696595312065, 5.050839498756849e-05, 1.57756790306886e-05, 4.379858022775772e-06, 1.0943960406471555e-06, 2.4859724334690514e-07, 5.176420434556841e-08, 9.949486593550421e-09, 1.7757716407751621e-09, 2.9580828764341136e-10, 4.619604920754892e-11, 6.790009695369627e-12, 9.425673018935618e-13], [5.5506965084405376e-05, 0.0001386953698061073, 0.00017327920537901382, 0.00014432437102386152, 9.015590196991372e-05, 4.978937495108656e-05, 1.996113515865407e-05, 7.125275741442885e-06, 2.225492675619982e-06, 6.178714672744854e-07, 1.5438767281901534e-07, 3.50698910120832e-08, 7.302434171375893e-09, 1.4035851957339908e-09, 2.5051009040124343e-10, 4.173000580561163e-11, 6.516928301722226e-12, 9.578742579028103e-13, 1.3296902292208005e-13], [6.525358010524371e-06, 1.6304925715371012e-05, 2.0370576001729864e-05, 1.6966666960486273e-05, 1.0598661559334804e-05, 5.296579563254506e-06, 2.437568146501245e-06, 8.376421781648088e-07, 2.6162728292093465e-07, 7.263651547734771e-08, 1.814970132169621e-08, 4.122790606474847e-09, 8.584687929533743e-10, 1.650044437938365e-10, 2.944978207025403e-11, 4.905748805556289e-12, 7.661253003652969e-13, 1.1260699359758824e-13, 1.5631740585290348e-14], [6.575282492015567e-07, 1.6429672121741282e-06, 2.0526428055046036e-06, 1.7096476244401415e-06, 1.0679750241671783e-06, 5.337102855301606e-07, 2.2226383454270742e-07, 8.7676514906099e-08, 2.6362895185966747e-08, 7.319224596243146e-09, 1.8288561814292072e-09, 4.1543334249674203e-10, 8.650368018343348e-11, 1.6626686668111168e-11, 2.967509769240302e-12, 4.943281913325769e-13, 7.71986803797957e-14, 1.1346853188538412e-14, 1.575133655876289e-15], [5.7973903205872866e-08, 1.4485951325234742e-07, 1.809803844428856e-07, 1.507386884377965e-07, 9.416276905599321e-08, 4.705694161562883e-08, 1.9596879747131868e-08, 6.9952520615880245e-09, 2.4144927020972797e-09, 6.45331997218226e-10, 1.6124924118224196e-10, 3.662852876001017e-11, 7.62698178822867e-12, 1.465965796453528e-12, 2.616437002263052e-13, 4.358464408342742e-14, 6.806565085825664e-15, 1.0004457895799533e-15, 1.3887866599339478e-16], [4.543579628376997e-09, 1.1353051924978865e-08, 1.4183947300743961e-08, 1.1813819600210361e-08, 7.379803938939166e-09, 3.68798630893008e-09, 1.5358631845544285e-09, 5.482377932968606e-10, 1.7123536516400867e-10, 5.253678236347494e-11, 1.2637561502891268e-11, 2.8706819428805336e-12, 5.977482481374075e-13, 1.1489190757107698e-13, 2.0505760704430027e-14, 3.4158524787315338e-15, 5.33449858522666e-16, 7.840778104398078e-17, 1.0884315920268062e-17], [3.2048392859599744e-10, 8.007938630034021e-10, 1.0004726505838278e-09, 8.332943685092302e-10, 5.205385955707959e-10, 2.6013417559853853e-10, 1.0833296815088228e-10, 3.867025917257672e-11, 1.2078182189124444e-11, 3.3533087899846196e-12, 9.259468599572942e-13, 2.0248515532951674e-13, 4.2162506777256885e-14, 8.10396491618652e-15, 1.4463852924159385e-15, 2.4093906378379076e-16, 3.762718392797091e-17, 5.530536659802266e-18, 7.677313069240733e-19], [2.055046639014988e-11, 5.134949337142903e-11, 6.415354326864022e-11, 5.3433530936078196e-11, 3.3378618890242416e-11, 1.668064497332762e-11, 6.946660416586294e-12, 2.4796621312833847e-12, 7.744921195240514e-13, 2.1502500885541672e-13, 5.3728343957220335e-14, 1.348724620521394e-14, 2.7035963464574977e-15, 5.196524498642981e-16, 9.274690456154149e-17, 1.544979230020837e-17, 2.412776771850304e-18, 3.5463590403633653e-19, 4.9229415305557565e-20], [1.2079488607876683e-12, 3.018304346113151e-12, 3.770921692754884e-12, 3.140803308144655e-12, 1.961982949567502e-12, 9.804821803164777e-13, 4.083221459400175e-13, 1.4575362864065104e-13, 4.5524362109685494e-14, 1.2639090984925554e-14, 3.15813230916454e-15, 7.173847099436151e-16, 1.6507579059863245e-16, 3.05449799971436e-17, 5.45162895964229e-18, 9.081331126084814e-19, 1.4182213179786946e-19, 2.0845368087627778e-20, 2.8936869366670156e-21], [6.554103695794882e-14, 1.6376752619307498e-13, 2.04603130193127e-13, 1.7041408985023337e-13, 1.0645351072612377e-13, 5.319912200159635e-14, 2.2154792910978887e-14, 7.908318200873937e-15, 2.4700664046095034e-15, 6.857733437636769e-16, 1.7135432890600597e-16, 3.89239472909662e-17, 8.104945712105348e-18, 1.7215485457832514e-18, 2.957951505430047e-19, 4.9273597441367114e-20, 7.695002564560672e-21, 1.1310305300030516e-21, 1.5700601955711754e-22], [3.302124052987501e-15, 8.251024280976494e-15, 1.0308425818174638e-14, 8.58589505417004e-15, 5.363398484513351e-15, 2.6803070032596207e-15, 1.116214786275635e-15, 3.984411745963005e-16, 1.2444822458897917e-16, 3.455100435460937e-17, 8.633266687969749e-18, 1.9610874125959156e-18, 4.083477684564632e-19, 7.848764796307811e-20, 1.5480528919015795e-20, 2.4825290968886406e-21, 3.87693790571841e-22, 5.698419328004423e-23, 7.910362388315948e-24], [1.5527811047238012e-16, 3.879937395606404e-16, 4.847403844633563e-16, 4.037406043299622e-16, 2.5220687321913056e-16, 1.2603796837235808e-16, 5.24885558849319e-17, 1.8736180631898093e-17, 5.852016718855905e-18, 1.624716268988404e-18, 4.059681941080486e-19, 9.221759782875588e-20, 1.9202025388527275e-20, 3.690780078386793e-21, 6.587257074938621e-22, 1.2126231902627442e-22, 1.823079880581882e-23, 2.6796079484999477e-24, 3.7197455489239123e-25], [6.845392694114598e-18, 1.710459704893844e-17, 2.1369646218988394e-17, 1.7798793241300656e-17, 1.111847047911376e-17, 5.556349090367458e-18, 2.3139435164832806e-18, 8.259793580887249e-19, 2.5798454380482813e-19, 7.162516882713247e-20, 1.7896995922580123e-20, 4.065387378332694e-21, 8.465159957636678e-22, 1.6270702230541765e-22, 2.9039741221645195e-23, 4.837444143793652e-24, 8.34850086827426e-25, 1.1812977771271681e-25, 1.6398395708903389e-26], [2.8402564689569556e-19, 7.096954782289976e-19, 8.866587882531088e-19, 7.3849872318786265e-19, 4.613220762391097e-19, 2.3054128744531413e-19, 9.600899955882969e-20, 3.42711268712664e-20, 1.0704167053302224e-20, 2.9718360683135324e-21, 7.425733002535833e-22, 1.6867904174515553e-22, 3.5123222881142213e-23, 6.750959269948198e-24, 1.2049025753121088e-24, 2.0071283908139585e-25, 3.134509943808037e-26, 5.091353437575711e-27, 6.803941216224565e-28], [1.1129948751157728e-20, 2.7810426234212116e-20, 3.474498511271684e-20, 2.893912233529674e-20, 1.8077561383759615e-20, 9.034088091469303e-21, 3.7622491363680216e-21, 1.3429628270917958e-21, 4.19458003279669e-22, 1.1645562116902256e-22, 2.909879043013174e-23, 6.609928048882927e-24, 1.3763534205985387e-24, 2.645459363156382e-25, 4.721582033148771e-26, 7.865217937504358e-27, 1.2283022824128793e-27, 1.8053891078341865e-28, 2.7695603226829524e-29]] |
| Legacy trial inputs | {"lambda_home": 0.7053555892239901, "lambda_away": 2.498702092524846, "rho": 0.05, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0826 |
| Legacy p draw | 0.1489 |
| Legacy p away | 0.7685 |
| Legacy p over 1 5 | 0.8263 |
| Legacy p under 3 5 | 0.6013 |
| Legacy p btts yes | 0.4623 |
| Legacy p over 2 5 | 0.6195 |
| Legacy goal margin distribution | {"-1": 0.22482250215192612, "-10": 0.00012441736563387654, "-11": 2.7893677049155762e-05, "-12": 5.743889148441089e-06, "-13": 1.093518556445529e-06, "-14": 1.9355707061137473e-07, "-15": 3.200908129302854e-08, "-16": 4.966123219009056e-09, "-17": 7.22799732515671e-10, "-18": 9.13884188293815e-11, "-2": 0.21960649784271938, "-3": 0.16107440437154064, "-4": 0.09287230948166716, "-5": 0.04393204477586227, "-6": 0.01757979996130414, "-7": 0.006088124214400677, "-8": 0.0018569548022085173, "-9": 0.0005058020406395669, "0": 0.14894106988718145, "1": 0.06206828942073112, "10": 3.7578024953511855e-10, "11": 2.37822176220846e-11, "12": 1.3824399061772635e-12, "13": 7.429507077279431e-14, "14": 3.712244015051702e-15, "15": 1.7329830543190695e-16, "16": 7.589833157456313e-18, "17": 3.118360731299077e-19, "18": 1.1129948751157728e-20, "2": 0.01644936293289076, "3": 0.003405838592648797, "4": 0.0005543415159757607, "5": 7.402291932675238e-05, "6": 8.361657062338695e-06, "7": 8.174393857833863e-07, "8": 7.038287762965517e-08, "9": 5.4117770251002696e-09} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0879 |
| Legacy raw p draw | 0.1434 |
| Legacy raw p away | 0.7687 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.7054 |
| Legacy lambda away | 2.4987 |
| Legacy model home team | Casa Pia |
| Legacy model away team | Sp Lisbon |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,356.0841 |
| Elo away rating | 1,692.9144 |
| Elo rating diff | -276.8303 |
| Elo home expectancy | 0.1689 |

</details>


---
