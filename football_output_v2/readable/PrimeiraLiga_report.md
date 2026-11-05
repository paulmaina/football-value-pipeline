# Primeira Liga — football model report

Fixtures in this report: **4**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,620 |
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
| Training sha256 | b3df8a6ba2e5ca811847821ea9d38323a7d64bb77cbc57ee92f21ada8c933425 |
| Training as of utc | 2026-11-05T12:31:20.268352+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1314, 'tuning_matches': 198, 'audit_matches': 105, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.871131149064499, 'audit_candidate_poisson_score': 0.8646865932043838, 'audit_gain': 0.006444555860115164, 'audit_gain_lower95': -0.0029289421499673917, 'audit_baseline_briers': [0.5561732722325169, 0.18693068045494893, 0.22413228109469926, 0.24642823314843584], 'audit_candidate_briers': [0.5573866098789683, 0.18683238764055768, 0.22226394985760883, 0.24657985484468817], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1469.356 |
| Base scoring parameter | 0.087 |
| Home-advantage parameter | 0.174 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1620, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 4.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 6.00 |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2, 'ANCHORED_MAIN': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 4} |
| Legacy comparison status | {'None': 4} |
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

## 2026-11-06 — Famalicão vs Arouca

The model's most likely 1X2 outcome is **Famalicão win** at **46.5%**. Expected goals are 1.47 for Famalicão and 1.00 for Arouca (2.47 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 46.1%; Under 3.5 goals: 74.8%; Double Chance 1X: 73.3%; Double Chance X2: 53.5%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Famalicão win | 46.5% | 2.15 |
| Draw | 26.8% | 3.74 |
| Arouca win | 26.7% | 3.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Famalicão expected goals | 1.47 |
| Arouca expected goals | 1.00 |
| Expected total goals | 2.47 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 71.6% |
| Under 1.5 | 28.4% |
| Over 2.5 | 46.1% |
| Under 2.5 | 53.9% |
| Over 3.5 | 25.2% |
| Under 3.5 | 74.8% |
| Over 4.5 | 11.3% |
| Under 4.5 | 88.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.67% |
| 2 | 1-0 | 11.80% |
| 3 | 2-1 | 8.79% |
| 4 | 0-1 | 8.79% |
| 5 | 2-0 | 8.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Famalicão win | 46.5% | 45.6% | 2.12 | -1.4% |
| Draw | 26.8% | 27.5% | 3.44 | -8.0% |
| Arouca win | 26.7% | 26.9% | 3.51 | -6.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:45:00+00:00 |
| Fixture id | d98d64a216d4db8db11c9b5017f76ca6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:31:23Z |
| Market best draw last update utc | 2026-11-05T12:31:23Z |
| Market best away last update utc | 2026-11-05T12:31:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Famalicao |
| Matched away-team name | Arouca |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4703 |
| Dc lambda away | 0.9993 |
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
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.74 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.52 |
| Fair Over 2.5 odds | 2.17 |
| Fair Under 2.5 odds | 1.86 |
| Fair Over 3.5 odds | 3.97 |
| Fair Under 3.5 odds | 1.34 |
| Fair Over 4.5 odds | 8.85 |
| Fair Under 4.5 odds | 1.13 |
| Score matrix json | [[0.07848700895559986,0.08789707476958175,0.04215078893438495,0.014498504453071109,0.0037402615115273282,0.0007719171984886702,0.00013275724159175176,1.95703653517956e-05,2.524339131969711e-06,2.894302658873719e-07,2.9866387592558884e-08,2.8017460286681938e-09,2.409274434711884e-10,1.912412938446922e-11,1.4095886393903667e-12,9.6970555863205e-14],[0.11804631510067631,0.1267470862583133,0.06399651847890506,0.0220127269644186,0.005678748156078583,0.0011719831231193456,0.0002015620936054249,2.9713210109180744e-05,3.832642756879399e-06,4.394349388821441e-07,4.5345410460541487e-08,4.253822906517308e-09,3.6579428233670497e-10,2.903570088453943e-11,2.1401441749720493e-12,1.4722803836174148e-13],[0.08521666056011513,0.08793530302813346,0.052256916690775805,0.016710694195338226,0.004310952659430147,0.0008896967469864804,0.0001530134141515872,2.2556422405045084e-05,2.909504177910983e-06,3.3359169421745487e-07,3.4423417352744774e-08,3.2292379706901546e-09,2.776882846188219e-10,2.204209950966724e-11,1.6246644452411635e-12,1.1176637633399036e-13],[0.04312746158982868,0.044503344519824815,0.022961560922441587,0.009096842298785013,0.002181738218948253,0.0004502683164307644,7.743884937729845e-05,1.141562265504738e-05,1.4724764952480609e-06,1.6882805409747355e-07,1.7421412666409895e-08,1.6342911776871416e-09,1.405357913596641e-10,1.1155328004102571e-11,8.222295147211284e-13,5.656405767013307e-14],[0.016369844209073833,0.01689208661295491,0.008715494982579142,0.0029978476325163575,0.0008907587088994649,0.00017090786057280804,2.9393380767285396e-05,4.333015612882069e-06,5.589063195506647e-07,6.408188290749134e-08,6.612626867851056e-09,6.203261445211477e-10,5.334301917039269e-11,4.2342158521879066e-12,3.120927725378034e-13,2.1469958531283557e-14],[0.00497078732762788,0.005129368917654437,0.002646504845134374,0.0009103118411848742,0.000234838314123506,5.582252312488461e-05,8.92545113857438e-06,1.3157424605781595e-06,1.6971477645545453e-07,1.9458793096547965e-08,2.0079581343129577e-09,1.8836522197766471e-10,1.619788192991001e-11,1.2857414054576112e-12,9.476857439579352e-14,6.519463253831328e-15],[0.001257837599680689,0.0012979660287212736,0.0006696873317120395,0.0002303507243033289,5.942488420463834e-05,1.2264139818669172e-05,2.4293850543854955e-06,3.3294330039289313e-07,4.294563677278582e-08,4.923968777583027e-09,5.081056728952459e-10,4.76650564707972e-11,4.098808414793333e-12,3.253516549102999e-13,2.3980803902155896e-14,1.649723770081106e-15],[0.0002728206084681044,0.00028152432541097585,0.0001452528572587119,4.996227238035838e-05,1.2889051075410448e-05,2.6600493485936615e-06,4.5748535556487387e-07,7.767650368185218e-08,9.314759519333764e-09,1.0679917330497765e-09,1.1020635643310929e-10,1.033838526716852e-11,8.890173151144286e-13,7.056764440915565e-14,5.201353110927287e-15,3.578193582956005e-16],[5.17771124593718e-05,5.342894269864889e-05,2.7566735400081268e-05,9.482062994760958e-06,2.4461416268123857e-06,5.048360350890236e-07,8.682361217725772e-08,1.2799074393973493e-08,1.9015120813051886e-09,2.0268823670724464e-10,2.0915454088365992e-11,1.9620648881042217e-12,1.687216730490872e-13,1.3392642443992563e-14,9.87136002949245e-16,6.790855448435648e-17],[8.73465906058962e-06,9.013318361596007e-06,4.650433824832066e-06,1.5995984232465484e-06,4.1265748724183413e-07,8.516447593446927e-08,1.4646908928578835e-08,2.159169289523519e-09,2.785065803378766e-10,3.6779300400717525e-11,3.528380627688421e-12,3.3099504855146243e-13,2.8462890652166914e-14,2.259302616777792e-15,1.6652717818052415e-16,1.145598977122883e-17],[1.3261620579584407e-06,1.3684702224246728e-06,7.060640660108978e-07,2.428631412130381e-07,6.26527834362488e-08,1.2930315412057294e-08,2.2238045873015186e-09,3.2782142595522037e-10,4.228497725827826e-11,4.8482202949313546e-12,5.762260100922144e-13,5.025417382821471e-14,4.3214515164116474e-15,3.430244256854455e-16,2.528341676417857e-17,1.7393350863013683e-18],[1.830436021672632e-07,1.888831892512927e-07,9.745453749631342e-08,3.352120047057199e-08,8.647654407811305e-09,1.7847076049102427e-09,3.069407692166912e-10,4.52475731109574e-11,5.836386668180951e-12,6.69175913727187e-13,6.905244393051194e-14,7.460997275600875e-15,5.964686196594221e-16,4.7345968113037565e-17,3.4897452025855244e-18,2.4007183561157737e-19],[2.3159221066177718e-08,2.389806299571238e-08,1.2330237992786184e-08,4.241202002745993e-09,1.094126960806863e-09,2.2580651533963892e-10,3.8835059211828194e-11,5.724857552940546e-12,7.384370034008713e-13,8.46661272761004e-14,8.736720624003216e-15,8.195859722246138e-16,8.117527772618556e-17,5.990352730930595e-18,4.4153294436076e-19,3.037460280972315e-20],[2.7047755786891938e-09,2.791065251463874e-09,1.4400538993524113e-09,4.953318407616185e-10,1.277835672935375e-10,2.6372041894428164e-11,4.535563586225481e-12,6.68608622734805e-13,8.62423812740412e-14,9.88819411258303e-15,1.0203654308626639e-15,9.571980490945083e-17,8.231127179417175e-18,7.525345994750956e-19,5.156682608975248e-20,3.547463174921139e-21],[2.933282163512111e-10,3.0268618157536957e-10,1.5617134562837174e-10,5.371787829546338e-11,1.3857906056432726e-11,2.8600021648305983e-12,4.918739977457849e-13,7.250944451328047e-14,9.352836543006409e-15,1.0723574868212096e-15,1.1065685974820503e-16,1.0380646684625172e-17,8.92651454383697e-19,7.085611196015501e-20,6.0153346709414124e-21,3.8471622336057565e-22],[2.9690206822821157e-11,3.063740490148594e-11,1.5807410583211358e-11,5.4372366099476284e-12,1.4026747991201725e-12,2.8948478548639327e-13,4.9786689141267556e-14,7.339288497324555e-15,9.466789618678067e-16,1.0854228743409117e-16,1.1200508062798766e-17,1.0507122391939695e-18,9.035273398182462e-20,7.171940854946968e-21,5.2862465779607385e-22,4.1885786105422485e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17096620143881203, "-10": 3.440937272393491e-08, "-11": 3.190426109987818e-09, "-12": 2.716443728586392e-10, "-13": 2.1376039935775258e-11, "-14": 1.5568166777521082e-12, "-15": 9.6970555863205e-14, "-2": 0.06895549003277164, "-3": 0.02114889597206882, "-4": 0.00507725255518102, "-5": 0.000997574329403065, "-6": 0.00016555558909540544, "-7": 2.375465807020623e-05, "-8": 2.999886432481486e-06, "-9": 3.3814978074411356e-07, "0": 0.2675369444359315, "1": 0.23218859970556455, "10": 1.5278849644341231e-06, "11": 2.084368396154226e-07, "12": 2.6111894899879914e-08, "13": 3.0232691708477748e-09, "14": 3.23965621252697e-10, "15": 2.9690206822821157e-11, "2": 0.13940798586300165, "3": 0.06290981263998424, "4": 0.02222139630672401, "5": 0.006423914177158233, "6": 0.001568592735919163, "7": 0.00033115172620274124, "8": 6.153113708566527e-05, "9": 1.0204955715869499e-05} |
| Raw goal margin distribution | {"-1": 0.1701141711831433, "-10": 2.644408448732876e-08, "-11": 2.376106403893477e-09, "-12": 1.9603657454792188e-10, "-13": 1.4947131182068765e-11, "-14": 1.0552339983952177e-12, "-15": 6.402769501756483e-14, "-2": 0.06713831720696709, "-3": 0.020067631039103286, "-4": 0.004684769561589917, "-5": 0.0008939543787536133, "-6": 0.00014397680725611257, "-7": 2.0038200352147318e-05, "-8": 2.453728130467487e-06, "-9": 2.681238131678931e-07, "0": 0.2503638626321784, "1": 0.2473651076497928, "10": 1.2573245878378051e-06, "11": 1.6622511595022916e-07, "12": 2.0178075945135236e-08, "13": 2.2636661694939028e-09, "14": 2.3513387265919843e-10, "15": 2.0991630654056525e-11, "2": 0.1453430354747703, "3": 0.06391926453920922, "4": 0.02195511833910461, "5": 0.006164172622034186, "6": 0.0014607095282607716, "7": 0.0002991175709354674, "8": 5.389165735676488e-05, "9": 8.664477383305179e-06} |
| Research history json | {"away": [{"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 2.04, "date": "2026-10-24T00:00:00+00:00", "home": "Alverca", "home_goals": 0.0, "home_xg": 0.39, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": 1.45, "date": "2026-10-11T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.74, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 2.0, "away_xg": 2.08, "date": "2026-09-19T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-13T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 1.08, "date": "2026-09-07T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-08-29T00:00:00+00:00", "home": "Arouca", "home_goals": 2.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 0.54, "date": "2026-08-23T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.99, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 0.0, "away_xg": 0.49, "date": "2026-08-16T00:00:00+00:00", "home": "Arouca", "home_goals": 4.0, "home_xg": 2.14, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 0.49, "date": "2026-08-08T00:00:00+00:00", "home": "Guimaraes", "home_goals": 0.0, "home_xg": 2.22, "source": "pipeline training history"}], "h2h": [{"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2026-03-06T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": null, "date": "2025-10-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2025-04-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2024-11-09T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2024-02-23T00:00:00+00:00", "home": "Arouca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2023-09-22T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": null, "date": "2023-04-03T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Famalicao", "away_goals": 0.0, "away_xg": 0.17, "date": "2026-11-01T00:00:00+00:00", "home": "Sp Braga", "home_goals": 3.0, "home_xg": 1.15, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.65, "date": "2026-10-25T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.58, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 4.0, "away_xg": 2.89, "date": "2026-10-12T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.36, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Sp Lisbon", "away_goals": 1.0, "away_xg": 2.28, "date": "2026-09-13T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.35, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-09-05T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 0.0, "away_xg": 0.27, "date": "2026-08-30T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": 0.23, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 0.0, "away_xg": 1.05, "date": "2026-08-23T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.36, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 2.0, "away_xg": 1.61, "date": "2026-08-16T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": 1.47, "date": "2026-08-07T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 1.22, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 70.0% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.0% |
| P home draw | 73.3% |
| P draw away | 53.5% |
| P home away | 73.2% |
| Raw p home draw | 73.7% |
| Raw p draw away | 51.3% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0326 |
| Totals anchor target over 2 5 | 0.4615 |
| Totals anchor reference over odds | 2.07 |
| Totals anchor reference under odds | 1.79 |
| Totals anchor reference last update utc | 2026-11-05T12:31:23Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4425 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.59, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.59, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.51, "draw": 3.44, "home": 2.12}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.07, "under": 1.79}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.34, "under": 3.29}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.12 |
| Reference draw odds | 3.44 |
| Reference away odds | 3.51 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:23Z |
| Market reference home last update utc | 2026-11-05T12:31:23Z |
| Market reference draw last update utc | 2026-11-05T12:31:23Z |
| Market reference away last update utc | 2026-11-05T12:31:23Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.14 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-11-05T12:31:22Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:31:22Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | 0.0306 |
| Raw ev home | 0.0315 |
| Raw edge prob draw | -0.0245 |
| Raw ev draw | -0.1387 |
| Raw edge prob away | -0.0061 |
| Raw ev away | -0.0766 |
| Market p home draw | 72.9% |
| Market reference home draw last update utc | 2026-11-05T12:31:23Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.2% |
| Market reference draw away last update utc | 2026-11-05T12:31:23Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.9% |
| Market reference home away last update utc | 2026-11-05T12:31:23Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home draw odds | 1.30 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 72.7% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T12:31:23Z |
| Market reference over 1 5 odds | 1.34 |
| Market reference over 1 5 opposite odds | 3.29 |
| Market reference over 1 5 last update utc | 2026-11-05T12:31:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.1% |
| Market under 3 5 odds | 1.30 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T12:31:23Z |
| Market reference under 3 5 odds | 1.30 |
| Market reference under 3 5 opposite odds | 3.58 |
| Market reference under 3 5 last update utc | 2026-11-05T12:31:23Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,482.5254 |
| Elo away rating | 1,488.7246 |
| Elo rating diff | 53.8007 |
| Elo home expectancy | 0.5768 |

</details>


---

## 2026-11-07 — Alverca vs Casa Pia

The model's most likely 1X2 outcome is **Alverca win** at **52.9%**. Expected goals are 1.43 for Alverca and 0.91 for Casa Pia (2.33 combined). The most likely exact score is 1-0 at 12.3%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 49.0%; Under 3.5 goals: 72.2%; Double Chance 1X: 78.6%; Double Chance X2: 47.1%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alverca win | 52.9% | 1.89 |
| Draw | 25.7% | 3.89 |
| Casa Pia win | 21.4% | 4.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alverca expected goals | 1.43 |
| Casa Pia expected goals | 0.91 |
| Expected total goals | 2.33 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 49.0% |
| Under 2.5 | 51.0% |
| Over 3.5 | 27.8% |
| Under 3.5 | 72.2% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.26% |
| 2 | 1-1 | 12.21% |
| 3 | 2-1 | 9.77% |
| 4 | 2-0 | 9.47% |
| 5 | 0-0 | 7.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alverca win | 52.9% | 54.3% | 1.79 | -5.3% |
| Draw | 25.7% | 25.7% | 3.64 | -6.3% |
| Casa Pia win | 21.4% | 20.0% | 4.63 | -1.1% |
| Over 2.5 | 49.0% | 49.0% | 1.95 | -4.4% |
| Under 2.5 | 51.0% | 51.0% | 1.88 | -4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T18:00:00+00:00 |
| Fixture id | d9d924bf6388e1288f06e04041b3fe33 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:31:23Z |
| Market best draw last update utc | 2026-11-05T12:31:23Z |
| Market best away last update utc | 2026-11-05T12:31:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Alverca |
| Matched away-team name | Casa Pia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4251 |
| Dc lambda away | 0.9059 |
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
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.24 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.60 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.75 |
| Fair Under 4.5 odds | 1.15 |
| Score matrix json | [[0.07022848583514177,0.06783203914746233,0.03238134608637934,0.011142128896657515,0.002875429483812072,0.0005936455981123019,0.00010213404587097884,1.5061458542863097e-05,1.9434419743768038e-06,2.2290694693911407e-07,2.3010080508673283e-08,2.159334818595231e-09,1.8575190493662725e-10,1.474974318250007e-11,1.0875543192606716e-12,7.484352487999955e-14],[0.12258870402043254,0.12207164209721345,0.0525848497238067,0.01809397213046901,0.0046694793630355684,0.0009640354197340037,0.00016585794301086503,2.4458666171105958e-05,3.156002344588425e-06,3.619839729922879e-07,3.736662529264761e-08,3.506595946824329e-09,3.016470032143599e-10,2.395246407136722e-11,1.7661057169224611e-12,1.2154020707218905e-13],[0.09465204117029816,0.09770673895747711,0.053850713702222136,0.014691619101462834,0.003791440138693395,0.0007827601968724656,0.0001346703590619821,1.985950926223786e-05,2.562554202896018e-06,2.9391725673554756e-07,3.034028249563994e-08,2.847222910591555e-09,2.4492592573747034e-10,1.9448492356491722e-11,1.4340108572538283e-12,9.868603836360812e-14],[0.05123591164405294,0.05288944414042659,0.027298170479689243,0.010030191562910627,0.0020523370605426395,0.0004237143942123905,7.289814918579705e-05,1.0750112192758165e-05,1.3871312134352287e-06,1.590997765137525e-07,1.6423439093144675e-08,1.541224675921404e-09,1.3258037476280845e-10,1.0527625433818312e-11,7.762416179348657e-13,5.3419546790356006e-14],[0.020800808489228023,0.021472111325151616,0.01108253953202026,0.003813401815930477,0.0010508712685139263,0.00017202000872691052,2.9595266128321996e-05,4.364341685042171e-06,5.631489670867555e-07,6.459149209508942e-08,6.667604817580248e-09,6.257079906264296e-10,5.3825117898363015e-11,4.27401628015335e-12,3.151393762290127e-13,2.168732294815187e-14],[0.006755787023936162,0.0069738160005700656,0.003599440704502189,0.0012385350559070425,0.00031962654978424183,7.04644040225358e-05,9.612093442579233e-06,1.4174719669718874e-06,1.8290224086039609e-07,2.097833670160746e-08,2.165536889139188e-09,2.0322046261020524e-10,1.748158170139906e-11,1.3881356458093864e-12,1.023524883545675e-13,7.043713470700529e-15],[0.0018284809432775925,0.0018874913631509432,0.0009742031108028184,0.0003352144967393919,8.650821187455708e-05,1.786001690147988e-05,3.281161112462656e-06,3.836444917602234e-07,4.950322748646237e-08,5.6778712449998354e-09,5.861112731538741e-10,5.5002435963459104e-11,4.731460433270831e-12,3.757044983883999e-13,2.770211283900545e-14,1.9064093947087828e-15],[0.00042418776436730423,0.00043787754230700923,0.00022600456467999599,7.776613066609704e-05,2.0068967702066145e-05,4.1433303797090004e-06,7.128412918506401e-07,1.1225139558922445e-07,1.1484212331361786e-08,1.3172046001554835e-09,1.359714639322175e-10,1.2759969105433256e-11,1.0976475476872455e-12,8.715937227567815e-14,6.426589982592203e-15,4.4226632062173723e-16],[8.610609401640494e-05,8.888498913163331e-05,4.587678365381061e-05,1.5785787146441116e-05,4.073810149483648e-06,8.410567800049185e-07,1.4470002308156593e-07,2.1338559343350246e-08,2.9401673371698825e-09,2.6738004409202933e-10,2.760091789624984e-11,2.590152738322467e-12,2.2281204428186775e-13,1.7692526126429804e-14,1.304536829513094e-15,8.977586951510875e-17],[1.55366405573211e-05,1.6038053320784424e-05,8.277824069216776e-06,2.8483245420690956e-06,7.35062073298033e-07,1.517569346107459e-07,2.610909567940729e-08,3.850244635014283e-09,4.96812909188769e-10,6.084813942382324e-11,4.9801996630397026e-12,4.67356840924757e-13,4.0203317586206594e-14,3.192368927163063e-15,2.35385428237759e-16,1.6198800227907968e-17],[2.523032571716291e-06,2.604458200984397e-06,1.3442558365508165e-06,4.625462993718337e-07,1.1936850481427508e-07,2.464417501287361e-08,4.2399190850920995e-09,6.252505222977188e-10,8.067864782658794e-11,9.253598155904559e-12,1.0200173914839119e-12,7.589520578256248e-14,6.528713809579398e-15,5.184164977268539e-16,3.822480800531914e-17,2.6305622793389836e-18],[3.72473955383998e-07,3.8449477768455645e-07,1.9845177351297796e-07,6.828546393202528e-08,1.762230881791662e-08,3.6382064374128556e-09,6.259369973404926e-10,9.230540174426645e-11,1.1910545828015152e-11,1.3661037694488464e-12,1.4101919276121112e-13,1.4131311825068024e-14,9.638305440384999e-16,7.653355157174479e-17,5.643108056211068e-18,3.8834850887510244e-19],[5.040578742889827e-08,5.203252939258226e-08,2.6855885535058215e-08,9.240867796764183e-09,2.3847743968207284e-09,4.923476062040933e-10,8.470618354859396e-11,1.2491414209253562e-11,1.6118185781611164e-12,1.8487074119763675e-13,1.908370599063318e-14,1.7908720831235637e-15,1.6450543885132405e-16,1.0357056851738538e-17,7.636649516244233e-19,5.2554043319639287e-20],[6.296551938571623e-09,6.499760057866231e-09,3.35476314830629e-09,1.1543437174129145e-09,2.9789944007002556e-10,6.150270499530297e-11,1.058126281598614e-11,1.5603930097456224e-12,2.0134393113612272e-13,2.309354308798654e-14,2.3838839165036455e-15,2.237108011184569e-16,1.924421683233265e-17,1.6317507835871149e-18,9.539491944953168e-20,6.5649061392172085e-21],[7.303659083418252e-10,7.539369491398638e-10,3.891343481302618e-10,1.338976166530628e-10,3.455472094312979e-11,7.133980540080128e-12,1.227369154323921e-12,1.8099713447160544e-13,2.3354805072362772e-14,2.6787258707365795e-15,2.7651761774454993e-16,2.5949240800167922e-17,2.2322248818393993e-18,1.7725117674540462e-19,1.395590588463887e-20,7.6149354159633935e-22],[7.907058883242078e-11,8.162242764911106e-11,4.212831087835976e-11,1.4495971500165282e-11,3.740949708504883e-12,7.723362161082182e-13,1.3287696021775714e-13,1.9595041110479392e-14,2.5284287889760753e-15,2.900031744371207e-16,2.9936242379164904e-17,2.8093065768662134e-18,2.416642586921175e-19,1.9189497697555696e-20,1.4149142020438916e-21,1.0397664196684758e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.13734287253658517, "-10": 2.6772452189758602e-08, "-11": 2.481228243106966e-09, "-12": 2.1119179941203865e-10, "-13": 1.6614534937786142e-11, "-14": 1.2090945263328606e-12, "-15": 7.484352487999955e-14, "-2": 0.054721536336356395, "-3": 0.01667181966615084, "-4": 0.003985470101201889, "-5": 0.0007808169947458384, "-6": 0.0001293212416667153, "-7": 1.8528445155073406e-05, "-8": 2.3373626959385766e-06, "-9": 2.6325775379229396e-07, "0": 0.25730576528458227, "1": 0.25174523652627556, "10": 2.935572905710478e-06, "11": 4.279988864912481e-07, "12": 5.730917780639493e-08, "13": 7.092617198589847e-09, "14": 8.119883359909362e-10, "15": 7.907058883242078e-11, "2": 0.15995336007323813, "3": 0.07666361494137225, "4": 0.028830823632210775, "5": 0.008885829083794317, "6": 0.002315206686781955, "7": 0.0005218312492887387, "8": 0.0001035591361617382, "9": 1.8349096565912808e-05} |
| Raw goal margin distribution | {"-1": 0.16479722237262048, "-10": 1.1201945543038086e-08, "-11": 9.1363326366612e-10, "-12": 6.839905215222398e-11, "-13": 4.715800060605562e-12, "-14": 2.793743297173325e-13, "-2": 0.06006579017643222, "-3": 0.01646891157088096, "-4": 0.003512064314895319, "-5": 0.000610777861695046, "-6": 8.952334079491512e-05, "-7": 1.1328576260811409e-05, "-8": 1.2604901759382238e-06, "-9": 1.250971137899679e-07, "0": 0.25694010216444396, "1": 0.25565531260225804, "10": 1.039933332735345e-06, "11": 1.3343051089423653e-07, "12": 1.5714643514123364e-08, "13": 1.7044373319928943e-09, "14": 1.58848587318642e-10, "2": 0.14865160511703007, "3": 0.06411778488883386, "4": 0.0215103400980178, "5": 0.0058849029894428705, "6": 0.0013569489386334823, "7": 0.0002701305866426098, "8": 4.7283443639247715e-05, "9": 7.382239442502841e-06} |
| Research history json | {"away": [{"away": "Sp Lisbon", "away_goals": 2.0, "away_xg": 2.65, "date": "2026-10-30T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.31, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 2.0, "away_xg": 0.79, "date": "2026-10-24T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": 1.69, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-10-10T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 2.0, "away_xg": 2.17, "date": "2026-09-20T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 4.0, "away_xg": 2.6, "date": "2026-09-12T00:00:00+00:00", "home": "Casa Pia", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.21, "date": "2026-09-06T00:00:00+00:00", "home": "Guimaraes", "home_goals": 0.0, "home_xg": 2.48, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.28, "date": "2026-08-30T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.78, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.76, "date": "2026-08-24T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 2.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 7.0, "away_xg": 3.04, "date": "2026-08-17T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.12, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.65, "date": "2026-08-08T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}], "h2h": [{"away": "Casa Pia", "away_goals": 1.0, "away_xg": null, "date": "2026-04-12T00:00:00+00:00", "home": "Alverca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 2.0, "away_xg": null, "date": "2025-11-29T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Alverca", "away_goals": 0.0, "away_xg": 0.56, "date": "2026-11-02T00:00:00+00:00", "home": "Benfica", "home_goals": 1.0, "home_xg": 1.6, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 2.04, "date": "2026-10-24T00:00:00+00:00", "home": "Alverca", "home_goals": 0.0, "home_xg": 0.39, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 4.0, "away_xg": 2.89, "date": "2026-10-12T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.36, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.29, "date": "2026-09-19T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 3.3, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-12T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 2.0, "away_xg": 2.26, "date": "2026-09-05T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 1.08, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.41, "date": "2026-08-29T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 0.41, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 1.0, "away_xg": 0.41, "date": "2026-08-22T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 3.0, "home_xg": 2.12, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 2.0, "away_xg": 1.29, "date": "2026-08-15T00:00:00+00:00", "home": "Alverca", "home_goals": 2.0, "home_xg": 1.75, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 0.0, "away_xg": 1.66, "date": "2026-08-09T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.59, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 49.8% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 79.3% |
| Raw p btts yes | 44.6% |
| P home draw | 78.6% |
| P draw away | 47.1% |
| P home away | 74.3% |
| Raw p home draw | 75.4% |
| Raw p draw away | 50.2% |
| Raw p home away | 74.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1395 |
| Totals anchor target over 2 5 | 0.4902 |
| Totals anchor reference over odds | 1.95 |
| Totals anchor reference under odds | 1.88 |
| Totals anchor reference last update utc | 2026-11-05T12:31:23Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4139 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.63, "draw": 3.64, "home": 1.79}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.95, "under": 1.88}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 3.64 |
| Reference away odds | 4.63 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:23Z |
| Market reference home last update utc | 2026-11-05T12:31:23Z |
| Market reference draw last update utc | 2026-11-05T12:31:23Z |
| Market reference away last update utc | 2026-11-05T12:31:23Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-11-05T12:31:23Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:31:23Z |
| Market best over 2 5 last update utc | 2026-11-05T12:31:23Z |
| Market best under 2 5 last update utc | 2026-11-05T12:31:23Z |
| Home probability edge | -1.4% |
| Draw probability edge | -0.0% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0451 |
| Raw ev home | -0.1095 |
| Raw edge prob draw | -0.0005 |
| Raw ev draw | -0.0647 |
| Raw edge prob away | 0.0456 |
| Raw ev away | 0.1369 |
| Elo home rating | 1,417.0742 |
| Elo away rating | 1,403.5352 |
| Elo rating diff | 73.5391 |
| Elo home expectancy | 0.6043 |

</details>


---

## 2026-11-07 — Nacional vs Académico de Viseu

The model's most likely 1X2 outcome is **Académico de Viseu win** at **43.7%**. Expected goals are 0.92 for Nacional and 1.60 for Académico de Viseu (2.51 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 44.2%; Under 3.5 goals: 76.2%; Double Chance 1X: 56.3%; Double Chance X2: 71.5%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.6%; BTTS No (at least one team does not score): 51.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nacional win | 28.5% | 3.51 |
| Draw | 27.7% | 3.60 |
| Académico de Viseu win | 43.7% | 2.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nacional expected goals | 0.92 |
| Académico de Viseu expected goals | 1.60 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 44.2% |
| Under 2.5 | 55.8% |
| Over 3.5 | 23.8% |
| Under 3.5 | 76.2% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.09% |
| 2 | 0-1 | 10.97% |
| 3 | 1-0 | 10.28% |
| 4 | 0-0 | 8.71% |
| 5 | 0-2 | 8.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nacional win | 28.5% | 31.2% | 3.05 | -13.0% |
| Draw | 27.7% | 29.4% | 3.23 | -10.4% |
| Académico de Viseu win | 43.7% | 39.4% | 2.44 | +6.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:30:00+00:00 |
| Fixture id | 406c4abcb4384570eada7fffa729be9d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:31:23Z |
| Market best draw last update utc | 2026-11-05T12:31:23Z |
| Market best away last update utc | 2026-11-05T12:31:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Nacional |
| Matched away-team name | Academico Viseu |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9185 |
| Dc lambda away | 1.5959 |
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
| P btts yes | 48.6% |
| P btts no | 51.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.48 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.21 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.61 |
| Fair Under 4.5 odds | 1.12 |
| Score matrix json | [[0.08707994142664595,0.10969354369919213,0.08368786750003598,0.04451974806958636,0.017762502744306876,0.005669511035837099,0.0015080155017278868,0.00034381056432408974,6.858682222081452e-05,1.2162129499288383e-05,1.9409800636792517e-06,2.816046623040926e-07,3.7451571522579924e-08,4.597673691363586e-09,5.241089314382134e-10,5.5762437939141655e-11],[0.10279670237388304,0.13085095729728372,0.07686519884583706,0.040890267492284416,0.01631441146998145,0.005207303115091312,0.0013850742630390114,0.0003157813453910658,6.29952690359175e-05,1.1170609674708469e-05,1.7827413101480574e-06,2.586467908733553e-07,3.4398325326797906e-08,4.222847505521441e-09,4.813808552579039e-10,5.121639502068719e-11],[0.04371945122387907,0.06977280025304128,0.05047449848316725,0.018778340490349803,0.007492188050390878,0.002391388389672305,0.0006360779156231882,0.00014501860682063501,2.892978412187837e-05,5.129961842290513e-06,8.187014999226719e-07,1.1878028204810901e-07,1.5796997791866176e-08,1.9392895464053565e-09,2.210680966387511e-10,2.3520484539950602e-11],[0.013385071664272379,0.021361519997621252,0.017045651605541036,0.008220688797432218,0.0022937953512534802,0.0007321433384184344,0.000194740515865102,4.439864615425321e-05,8.857092732485445e-06,1.570580255969391e-06,2.5065223696419385e-07,3.636556596684931e-08,4.836381555699697e-09,5.937295375343657e-10,6.768182658655597e-11,7.200990916685992e-12],[0.0030734628141875935,0.004905004546405061,0.003914000437746281,0.0020821454607221324,0.0007531247672288452,0.00016811380482112233,4.4716064952024035e-05,1.019475960816891e-05,2.0337541582064442e-06,3.606346035713632e-07,5.7554441912976095e-08,8.350214142994136e-09,1.1105236669253058e-09,1.3633140718756605e-10,1.5541013333930553e-11,1.6534822048664871e-12],[0.0005645796395940283,0.0009010246313158786,0.0007189821677077196,0.0003824796344925267,0.00015260184192183632,4.415761678291829e-05,8.214115921018583e-06,1.8727259945226227e-06,3.735903959412497e-07,6.624676035433823e-08,1.0572461108774669e-08,1.5338922825492945e-09,2.0399760450625682e-10,2.5043392872689807e-11,2.8548058777525054e-12,3.0373635333714546e-13],[8.642536359225407e-05,0.00013792807233191473,0.00011006116923587322,5.8549652094111223e-05,2.336015815665253e-05,7.456194454944733e-06,1.7979674712850283e-06,2.8667527773701744e-07,5.718889513446452e-08,1.0140996856616298e-08,1.618423214921194e-09,2.3480690576443783e-10,3.1227777101702937e-11,3.833620950557519e-12,4.370112180231623e-13,4.649569862672357e-14],[1.1339931438584688e-05,1.809763729869047e-05,1.4441201764259965e-05,7.682340147652148e-06,3.0651024291979557e-06,9.783324061063793e-07,2.6022357570617717e-07,5.378540646879604e-08,7.503794290445554e-09,1.3306071770259632e-09,2.1235442389813712e-10,3.080917570954352e-11,4.097418125811095e-12,5.030120433851484e-13,5.734054268669806e-14,6.100732617148021e-15],[1.3019301825987445e-06,2.077778014840505e-06,1.657985019725556e-06,8.820044958284807e-07,3.5190242436135937e-07,1.1232170979362795e-07,2.9876100157262103e-08,6.81141463274214e-09,1.2318651978339533e-09,1.5276614804373315e-10,2.4380273847216362e-11,3.5371815054156106e-12,4.704219207683709e-13,5.77504868561647e-14,6.5832305613764126e-15,7.004211597967961e-16],[1.3286556523568126e-07,2.1204297593363262e-07,1.69201943193617e-07,9.001099094634061e-08,3.591261278485063e-08,1.1462740214056488e-08,3.0489384050602794e-09,6.951236458989114e-10,1.3867032275893487e-10,2.229240229357808e-11,2.488074175256641e-12,3.6097912648445603e-13,4.800785421333756e-14,5.8935964319255235e-15,6.718368321933793e-16,7.147991078421328e-17],[1.2203367580851278e-08,1.9475613366530923e-08,1.554077239293233e-08,8.26728285004792e-09,3.29848304807134e-09,1.0528238228453426e-09,2.8003731457677147e-10,6.384535639462915e-11,1.2736519941647859e-11,2.2584980596109415e-12,3.26765032994643e-13,3.315502373914871e-14,4.409400514678614e-15,5.4131199084129585e-16,6.17065211973278e-17,6.565249802677643e-18],[1.0189532558322076e-09,1.6261691305844958e-09,1.2976189173202842e-09,6.902991916887311e-10,2.7541578329685787e-10,8.79083789780541e-11,2.338247467774829e-11,5.330941097779907e-12,1.0634702574130457e-12,1.885794175980036e-13,3.009578955719769e-14,3.958484157528868e-15,3.6817484853525706e-16,4.519831200973103e-17,5.152353255240568e-18,5.481833286974944e-19],[7.799024215798285e-11,1.244662829803115e-10,9.931919154420318e-11,5.283520202042448e-11,2.1080205112951295e-11,6.728469363017722e-12,1.7896845139192397e-12,4.0802792941294833e-13,8.139755423394388e-14,1.4433787183365705e-14,2.303518735591588e-15,3.342031315962113e-16,4.0294439948054704e-17,3.459459281958915e-18,3.943588930696283e-19,4.1957715240989317e-20],[5.510159496036096e-12,8.7937805053998e-12,7.017090488286201e-12,3.732907887990551e-12,1.4893567344774287e-12,4.753792055077644e-13,1.2644462751256445e-13,2.882795216032771e-14,5.75089259894509e-15,1.019774619382252e-15,1.6274799621093186e-16,2.3612089259058327e-17,3.140252872405346e-18,3.4949190751466017e-19,2.786220864774525e-20,2.9643926813150867e-21],[3.6149590990159117e-13,5.769189961853601e-13,4.603586362154558e-13,2.4489870656534106e-13,9.770976108500901e-14,3.1187416365524206e-14,8.295443300271906e-15,1.8912677217953505e-15,3.77289287959363e-16,6.690266483090584e-17,1.0677138296496619e-17,1.5490792412672043e-18,2.06017370322563e-19,2.529134572964129e-20,2.6137241918225412e-21,1.9448000196882046e-22],[2.213499266308874e-14,3.5325704656619295e-14,2.818852096498866e-14,1.4995552991178908e-14,5.982930333340705e-15,1.909657104058243e-15,5.079437181974574e-16,1.1580545173325176e-16,2.3102047331921188e-17,4.096560858949479e-18,6.537788433624992e-19,9.4852684915099e-20,1.261478444334315e-20,1.5486309438954641e-21,1.7653521404136064e-22,1.7027698207211445e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2078075006417344, "-10": 2.2160334266316947e-06, "-11": 3.180116124860873e-07, "-12": 4.1902688115656805e-08, "-13": 5.102575031161441e-09, "-14": 5.753253264589006e-10, "-15": 5.5762437939141655e-11, "-2": 0.13284911371632432, "-3": 0.06343086715204634, "-4": 0.023652384071802958, "-5": 0.007208832444456665, "-6": 0.0018543563315684397, "-7": 0.0004121950055426713, "-8": 8.061363497158426e-05, "-9": 1.4068626705749013e-05, "0": 0.277425221395907, "1": 0.19185762490551386, "10": 1.3932688430286156e-08, "11": 1.150687510937704e-09, "12": 8.725937685258929e-11, "13": 6.115267013186445e-12, "14": 3.968216145582105e-13, "15": 2.213499266308874e-14, "2": 0.06940182036845312, "3": 0.01907078856848009, "4": 0.004092594605502257, "5": 0.0007178679074189602, "6": 0.00010627438511193734, "7": 1.3595460952080516e-05, "8": 1.5302257941125653e-06, "9": 1.5369315377364744e-07} |
| Raw goal margin distribution | {"-1": 0.255860530968281, "-10": 2.7284649852892445e-06, "-11": 3.9154804217123864e-07, "-12": 5.159218987361738e-08, "-13": 6.282485245945273e-09, "-14": 7.083625136373485e-10, "-15": 6.865684316078651e-11, "-2": 0.16356890232141036, "-3": 0.07809850606538538, "-4": 0.029121718554858744, "-5": 0.008875789811263567, "-6": 0.0022831543333821738, "-7": 0.0005075102325706947, "-8": 9.925458601550787e-05, "-9": 1.7321830481630675e-05, "0": 0.23888177615808892, "1": 0.14976852257978382, "10": 1.0876180515609187e-08, "11": 8.982534238554308e-10, "12": 6.811669830104992e-11, "13": 4.773719606905756e-12, "14": 3.0976817819659985e-13, "15": 1.727908989855259e-14, "2": 0.05417667453169881, "3": 0.014887100941332509, "4": 0.003194774499506748, "5": 0.0005603843785438672, "6": 8.296025583621412e-05, "7": 1.061293290577852e-05, "8": 1.194529831746755e-06, "9": 1.1997644911242293e-07} |
| Research history json | {"away": [{"away": "Rio Ave", "away_goals": 1.0, "away_xg": 1.08, "date": "2026-11-01T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 0.77, "date": "2026-10-25T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 1.0, "home_xg": 2.22, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 1.0, "away_xg": 1.36, "date": "2026-10-10T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 0.73, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 2.54, "date": "2026-09-20T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Guimaraes", "away_goals": 1.0, "away_xg": 2.1, "date": "2026-09-12T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 1.83, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 1.0, "away_xg": 0.33, "date": "2026-09-06T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 1.88, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 3.0, "away_xg": 1.47, "date": "2026-08-29T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 0.0, "home_xg": 0.8, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.84, "date": "2026-08-22T00:00:00+00:00", "home": "Maritimo", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.26, "date": "2026-08-15T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 0.0, "home_xg": 0.69, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.18, "date": "2026-08-09T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 3.12, "source": "pipeline training history"}], "h2h": [], "home": [{"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 0.0, "away_xg": 1.67, "date": "2026-10-25T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.21, "date": "2026-10-11T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-12T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.08, "date": "2026-09-05T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 3.0, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 2.1, "date": "2026-08-30T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.42, "date": "2026-08-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 3.14, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-08-16T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.24, "date": "2026-08-10T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": 1.44, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 53.8% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 75.4% |
| Raw p btts yes | 47.3% |
| P home draw | 56.3% |
| P draw away | 71.5% |
| P home away | 72.3% |
| Raw p home draw | 46.2% |
| Raw p draw away | 77.7% |
| Raw p home away | 76.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4422 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.79, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.09, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.44, "draw": 3.23, "home": 3.05}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.05 |
| Reference draw odds | 3.23 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:23Z |
| Market reference home last update utc | 2026-11-05T12:31:23Z |
| Market reference draw last update utc | 2026-11-05T12:31:23Z |
| Market reference away last update utc | 2026-11-05T12:31:23Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-11-05T12:31:22Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:31:22Z |
| Home probability edge | -2.7% |
| Draw probability edge | -1.7% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0894 |
| Raw ev home | -0.3208 |
| Raw edge prob draw | -0.0551 |
| Raw ev draw | -0.2284 |
| Raw edge prob away | 0.1445 |
| Raw ev away | 0.3138 |
| Elo home rating | 1,377.6402 |
| Elo away rating | 1,452.3265 |
| Elo rating diff | -14.6862 |
| Elo home expectancy | 0.4789 |

</details>


---

## 2026-11-07 — Sporting Lisbon vs Moreirense FC

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **84.1%**. Expected goals are 2.87 for Sporting Lisbon and 0.69 for Moreirense FC (3.56 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 69.7%; Under 3.5 goals: 51.9%; Double Chance 1X: 94.3%; Double Chance X2: 15.9%; Double Chance 12 (either team wins): 89.8%; Under 4.5 goals: 71.0%; BTTS Yes (both teams score): 46.3%; BTTS No (at least one team does not score): 53.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 84.1% | 1.19 |
| Draw | 10.2% | 9.79 |
| Moreirense FC win | 5.7% | 17.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 2.87 |
| Moreirense FC expected goals | 0.69 |
| Expected total goals | 3.56 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 87.1% |
| Under 1.5 | 12.9% |
| Over 2.5 | 69.7% |
| Under 2.5 | 30.3% |
| Over 3.5 | 48.1% |
| Under 3.5 | 51.9% |
| Over 4.5 | 29.0% |
| Under 4.5 | 71.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.99% |
| 2 | 3-0 | 11.47% |
| 3 | 1-0 | 8.64% |
| 4 | 2-1 | 8.27% |
| 5 | 4-0 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 84.1% | 84.9% | 1.16 | -2.5% |
| Draw | 10.2% | 9.7% | 8.27 | -15.5% |
| Moreirense FC win | 5.7% | 5.4% | 14.06 | -19.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T20:30:00+00:00 |
| Fixture id | ba0a2d492dfcc89ab465eddd7a9e98c2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:31:23Z |
| Market best draw last update utc | 2026-11-05T12:31:23Z |
| Market best away last update utc | 2026-11-05T12:31:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sp Lisbon |
| Matched away-team name | Moreirense |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8700 |
| Dc lambda away | 0.6904 |
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
| P btts yes | 46.3% |
| P btts no | 53.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.57 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.74 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.30 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.44 |
| Fair Under 4.5 odds | 1.41 |
| Score matrix json | [[0.022951766835196053,0.019803184692084363,0.005978275525483025,0.001375819714577912,0.0002374698036606853,3.279028904914039e-05,3.7731220255920317e-06,3.7214283948534503e-07,3.211637618284414e-08,2.463717355994974e-09,1.7009742500543796e-10,1.0676082230366072e-11,6.142391875542494e-13,3.26212819721315e-14,1.6087177168430227e-15,7.404494960424506e-17,3.1950842574566222e-18,1.29759824720903e-19,4.977079768522063e-21,1.808538908667003e-22],[0.08640513262291703,0.04795539935225804,0.017157588624830255,0.003948588281693811,0.00068153586843926,9.410778877558854e-05,1.0828820998704928e-05,1.0680460815746517e-06,9.217366585341741e-08,7.070843205842512e-09,4.881778419120983e-10,3.064024504268416e-11,1.7628600843809817e-12,9.362274022109436e-14,4.617003127643337e-15,2.1250823580154034e-16,9.169858611808076e-18,3.724093483315072e-19,1.4284167207962082e-20,5.190487871400132e-22],[0.11985351510050264,0.0827480240249097,0.02500581970579485,0.005666203665032143,0.000978000429547152,0.00013504418785327784,1.5539301860187418e-05,1.5326405768609295e-06,1.3226873151080812e-07,1.0146623256103572e-08,7.005326662832628e-10,4.396859241142898e-11,2.529695060223794e-12,1.3434814569817765e-13,6.625375495491114e-15,3.0494821405681673e-16,1.3158699455939507e-17,5.344054795966311e-19,2.0497705714450293e-20,7.448323122616434e-22],[0.1146594475596793,0.07916198964540364,0.027327100984667077,0.00550536054773488,0.0009356170227545981,0.000129191805200025,1.4865878278648118e-05,1.4662208421927661e-06,1.2653662824767e-07,9.706901096438106e-09,6.701738238231383e-10,4.206313441573824e-11,2.4200661770869783e-12,1.2852592728301011e-13,6.338252937775221e-15,2.9173273498691744e-16,1.2588443559262362e-17,5.1124605742296e-19,1.9609400788028256e-20,7.125536650043602e-22],[0.08226785570494109,0.05679852188433413,0.019607123952614592,0.004512315895310025,0.0006817936685699474,9.269478455252939e-05,1.0666229038985109e-05,1.0520096445982654e-06,9.078970198814904e-08,6.964676315296717e-09,4.808479772834584e-10,3.018018965083851e-11,1.7363911940128032e-12,9.22170188772188e-14,4.547680014199515e-15,2.0931747934525516e-16,9.032175545274253e-18,3.6681771783263365e-19,1.4069694114392074e-20,5.112554032156336e-22],[0.04722157816967553,0.032602233498131884,0.011254448392718934,0.002590059944443818,0.00044705059824293446,5.403810805519834e-05,6.12239329716536e-06,6.038513492538481e-07,5.211310022241689e-08,3.997709727950507e-09,2.760057394525894e-10,1.732336612594009e-11,9.966849360373825e-13,5.293237714987006e-14,2.61035887517724e-15,1.2014779804924159e-16,5.1844499883784266e-18,2.1055260755526575e-19,8.075975175882516e-21,2.934595387316752e-22],[0.022587573094084837,0.01559467854978162,0.005383358319595341,0.001238907520264862,0.00021383842844649301,2.9527223126833643e-05,2.9743002995056867e-06,2.88841182736921e-07,2.4927342669566236e-08,1.9122308950488124e-09,1.3202226727517135e-10,8.286313456091625e-12,4.767459012832128e-13,2.5319228714048956e-14,1.248617140303935e-15,5.747048861389707e-17,2.479886263952233e-18,1.007139658953377e-19,3.862994136617065e-21,1.403709710302484e-22],[0.009260871431894803,0.006393795051362806,0.0022071689181450607,0.000507950243852674,8.767343816853042e-05,1.2106117641743764e-05,1.3930300843038505e-06,1.202751521633718e-07,1.0220173483892005e-08,7.840118278037463e-10,5.412893356403994e-11,3.397376213974067e-12,1.9546511168226626e-13,1.0380846180280918e-14,5.119311736524298e-16,2.3562815002947477e-17,1.016749686233348e-18,4.1292576483004845e-20,1.5838218604699358e-21,5.755188970796465e-23],[0.0033223255949518912,0.0022937656681918926,0.0007918189819459863,0.00018222649007972573,3.145273204220955e-05,4.343053976339969e-06,4.997477329920938e-07,4.929009428282683e-08,3.723772336083114e-09,2.8126322467738474e-10,1.9418684594616582e-11,1.218804303069501e-12,7.01228548779512e-14,3.7241150809227254e-15,1.8365464347357206e-16,8.453129270729095e-18,3.6475762902813704e-19,1.4813658168119777e-20,5.681940348249684e-22,2.0646665664323762e-23],[0.001059448880886347,0.0007314537364651685,0.00025250136096290396,5.8109792512858163e-05,1.0029890451907854e-05,1.384946641549444e-06,1.5936342219090348e-07,1.5718006478976546e-08,1.3564829290315323e-09,9.109305819835803e-11,6.192380329402782e-12,3.886617425060487e-13,2.236131830001354e-14,1.1875746196491263e-15,5.856521311255603e-17,2.6955992391201033e-18,1.163167338131448e-19,4.723893886828589e-21,1.8119010828928936e-22,6.583968430228202e-24],[0.00030406072770986913,0.00020992646215231664,7.246762816709138e-05,1.667745005662486e-05,2.8785681354497813e-06,3.9747824672442845e-07,4.573713653948289e-08,4.511051523455939e-09,3.893091908146425e-10,2.98647582404004e-11,1.8049802854308513e-12,1.1154551615601018e-13,6.417675111578619e-15,3.4083268157137347e-16,1.6808155295411225e-17,7.736341800420986e-19,3.3382781714273194e-20,1.355752635890875e-21,5.2001372764847367e-23,1.8895920966372225e-24],[7.933192076080182e-05,5.47715240521096e-05,1.890739451548166e-05,4.3512825755216725e-06,7.510418755689209e-07,1.0370531245775648e-07,1.1933191501266212e-08,1.1769700898307925e-09,1.0157393922515645e-10,7.791958705461744e-12,5.379643522511485e-13,2.9557947447976425e-14,1.6744237154695192e-15,8.892602307033869e-17,4.3853846370556294e-18,2.018474596545392e-19,8.709839687875963e-21,3.5372690676571084e-22,1.3567581761397883e-23,4.930099707703749e-25],[1.8973482339367086e-05,1.3099475398261082e-05,4.522002145953229e-06,1.0406779806729306e-06,1.796235314306542e-07,2.480276407713062e-08,2.8540112987335093e-09,2.81490993779162e-10,2.4293012491646285e-11,1.8635700417858097e-12,1.2866267498327813e-13,8.075450278312135e-15,4.067232140024602e-16,2.1268063498960315e-17,1.0488340275207242e-18,4.827500928092747e-20,2.0830957817711972e-21,8.459937883912051e-23,3.2449015537387055e-24,1.1791112434738241e-25],[4.188745932240534e-06,2.8919506344443364e-06,9.983153200687781e-07,2.2974884527504417e-07,3.96552052573777e-08,5.475667317055525e-09,6.300755973158535e-10,6.214432511992643e-11,5.3631302591786785e-12,4.1141743473096283e-13,2.840465692210774e-14,1.782804489933133e-15,1.025721194194143e-16,4.768693792003872e-18,2.3154944294318937e-19,1.065759806963851e-20,4.598817879761225e-22,1.8676872154732923e-23,7.163718257213397e-25,2.6031053954246404e-26],[8.586898065093682e-07,5.92847733163266e-07,2.0465389949460674e-07,4.709834272269958e-08,8.129287638921798e-09,1.1225077350244213e-09,1.2916502970043498e-10,1.2739540515493026e-11,1.09943772170382e-12,8.434026869582512e-14,5.8229335822626995e-15,3.654735969354576e-16,2.1027208334500364e-17,1.1167221272509722e-18,4.820926887822245e-20,2.184799692393229e-21,9.427542513259372e-23,3.828744926567888e-24,1.4685569245981576e-25,5.336346735943113e-27],[1.6429538801082522e-07,1.1343112217360915e-07,3.915697096961871e-08,9.011450274166415e-09,1.5553980689692634e-09,2.1477236887285419e-10,2.471348618697176e-11,2.43748992500672e-12,2.1035832230890247e-13,1.6137046306216596e-14,1.1141172574856661e-15,6.992702831807502e-17,4.023191292027413e-18,2.136653932609259e-19,1.0536903605098381e-20,4.2455621937609015e-22,1.803796602059233e-23,7.32563876427112e-25,2.809828740411467e-26,1.021017311368898e-27],[2.947037850244917e-08,2.0346633857997043e-08,7.023756232329808e-09,1.6164230393258852e-09,2.789985182754036e-10,3.852465415604733e-11,4.432965531552958e-12,4.372231719682932e-13,3.773288742088785e-14,2.894572198973826e-15,1.9984405936002201e-16,1.254311528178363e-17,7.216573246474413e-19,3.832609112472015e-20,1.8900502396671683e-21,8.699392894129655e-23,3.2861124604466982e-24,1.3140316947975393e-25,5.040112051199508e-27,1.8314431700061994e-28],[4.9752752947658624e-09,3.4349781003636057e-09,1.1857710228005415e-09,2.728892542991964e-10,4.710134398635355e-11,6.5038445314182936e-12,7.483861766434768e-13,7.38132917299394e-14,6.370176160775241e-15,4.88670125131706e-16,3.373825725573933e-17,2.117565323284598e-18,1.218322953777758e-19,6.470322541053158e-21,3.1908379671814757e-22,1.4686568936339918e-23,6.337343121354611e-25,2.253054824091418e-26,8.508864237729636e-28,3.0918958019973385e-29],[7.932771326131145e-10,5.476861915383757e-10,1.8906391730574588e-10,4.351051798061057e-11,7.510020428221731e-12,1.0369981227516757e-12,1.1932558604738833e-13,1.1769076672774792e-14,1.015685520834684e-15,7.791545446057866e-17,5.379358204228979e-18,3.376328038658253e-19,1.942541230605496e-20,1.0316532469767987e-21,5.0875954460282795e-23,2.3416833448394832e-24,1.0104504940626037e-25,4.103675159511606e-27,1.3778880372620522e-28,4.9298382317202016e-30],[1.198261645224186e-10,8.27291409217275e-11,2.855849882588274e-11,6.5723544416640115e-12,1.1344042408413986e-12,1.5664072813615764e-13,1.8024378514919e-14,1.7777435648793048e-15,1.5342141518899905e-16,1.176929181643974e-17,8.125632703940969e-19,5.100013884293207e-20,2.934249022448974e-21,1.5583337350859818e-22,7.684918975681739e-24,3.5371615063936427e-25,1.5263065348229985e-26,6.198686872397446e-28,2.3775740365224764e-29,7.5629966484075485e-31]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.04366171053147612, "-10": 2.034005613851948e-10, "-11": 1.2579843317630777e-11, "-12": 7.147882826545207e-13, "-13": 3.755619679145489e-14, "-14": 1.8349102613115783e-15, "-15": 8.3769334351841e-17, "-16": 3.588703865167584e-18, "-17": 1.4478882424112673e-19, "-18": 5.496128555662076e-21, "-19": 1.808538908667003e-22, "-2": 0.011045351853480602, "-3": 0.002208371739495258, "-4": 0.00034867803804134107, "-5": 4.52855364205707e-05, "-6": 4.98364239843047e-06, "-7": 4.7516450513300674e-07, "-8": 3.9931605785506307e-08, "-9": 2.9983787423755754e-09, "0": 0.10215727660976098, "1": 0.201470595056246, "10": 0.0003635923513210211, "11": 9.34784045048862e-05, "12": 2.207938394704633e-05, "13": 4.822415215779233e-06, "14": 9.794252408307627e-07, "15": 1.8587243781384425e-07, "16": 3.3100992874560185e-08, "17": 5.5515199851301214e-09, "18": 8.760062735348421e-10, "19": 1.198261645224186e-10, "2": 0.221439149052024, "3": 0.18404350582708212, "4": 0.1207942823840217, "5": 0.06521609171651165, "6": 0.029834282110625797, "7": 0.011824592398774295, "8": 0.0041307834729991675, "9": 0.001289364218404969} |
| Raw goal margin distribution | {"-1": 0.04948194737874063, "-10": 2.3051446571276243e-10, "-11": 1.4256774127689293e-11, "-12": 8.100717026135166e-13, "-13": 4.25625503618484e-14, "-14": 2.0795092974993696e-15, "-15": 9.493603763786827e-17, "-16": 4.067088844036226e-18, "-17": 1.640896083758389e-19, "-18": 6.22877896141991e-21, "-19": 2.049622564524848e-22, "-2": 0.012517730353225464, "-3": 0.002502754309811689, "-4": 0.0003951578653348024, "-5": 5.132223412468681e-05, "-6": 5.647976863751613e-06, "-7": 5.385053575096815e-07, "-8": 4.5254608492779924e-08, "-9": 3.3980716134518962e-09, "0": 0.11399369400744708, "1": 0.1968021293252876, "10": 0.00035516720902317413, "11": 9.131232797201104e-05, "12": 2.1567761656514645e-05, "13": 4.7106704712469954e-06, "14": 9.567300521280265e-07, "15": 1.815654117387916e-07, "16": 3.233397845812666e-08, "17": 5.422880464320272e-09, "18": 8.557075035482828e-10, "19": 1.170495591195859e-10, "2": 0.21630797306798846, "3": 0.17977885966509852, "4": 0.11799524380646612, "5": 0.06370490796684053, "6": 0.02914296373931549, "7": 0.011550593583310344, "8": 0.004035065181799788, "9": 0.0012594871404786989} |
| Research history json | {"away": [{"away": "Estrela", "away_goals": 1.0, "away_xg": 0.68, "date": "2026-10-31T00:00:00+00:00", "home": "Moreirense", "home_goals": 2.0, "home_xg": 0.44, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 3.0, "away_xg": 1.33, "date": "2026-10-25T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 2.01, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.49, "date": "2026-10-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 1.09, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.52, "date": "2026-09-20T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 1.07, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-09-14T00:00:00+00:00", "home": "Moreirense", "home_goals": 3.0, "home_xg": 1.99, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 4.0, "away_xg": 2.99, "date": "2026-09-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 0.38, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.85, "date": "2026-09-04T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.28, "date": "2026-08-30T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.78, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 0.0, "away_xg": 0.49, "date": "2026-08-16T00:00:00+00:00", "home": "Arouca", "home_goals": 4.0, "home_xg": 2.14, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 2.0, "away_xg": 1.5, "date": "2026-08-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 2.0, "home_xg": 0.2, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 82.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 6.5% |
| Raw p over 1 5 | 86.8% |
| Raw p under 3 5 | 52.4% |
| Raw p btts yes | 46.8% |
| P home draw | 94.3% |
| P draw away | 15.9% |
| P home away | 89.8% |
| Raw p home draw | 93.5% |
| Raw p draw away | 17.9% |
| Raw p home away | 88.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6971 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.83, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "line": -2.0, "market_key": "spreads", "opposite_price": 2.01, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:31:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 14.06, "draw": 8.27, "home": 1.16}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 8.27 |
| Reference away odds | 14.06 |
| Market reference 1x2 last update utc | 2026-11-05T12:31:23Z |
| Market reference home last update utc | 2026-11-05T12:31:23Z |
| Market reference draw last update utc | 2026-11-05T12:31:23Z |
| Market reference away last update utc | 2026-11-05T12:31:23Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-11-05T12:30:19Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:30:19Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | -0.0278 |
| Raw ev home | -0.0476 |
| Raw edge prob draw | 0.0169 |
| Raw ev draw | -0.0573 |
| Raw edge prob away | 0.0109 |
| Raw ev away | -0.0867 |
| Elo home rating | 1,667.4354 |
| Elo away rating | 1,438.9672 |
| Elo rating diff | 288.4681 |
| Elo home expectancy | 0.8403 |

</details>


---
