# Primeira Liga — football model report

Fixtures in this report: **9**.

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
| Training as of utc | 2026-11-06T13:39:18.622132+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-06', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-11-07', 'audit_start_date': '2026-05-08', 'training_shot_matches': 1314, 'tuning_matches': 198, 'audit_matches': 105, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8711307065798971, 'audit_candidate_poisson_score': 0.8646870750778988, 'audit_gain': 0.006443631501998337, 'audit_gain_lower95': -0.00293184513832055, 'audit_baseline_briers': [0.5561730451150284, 0.1869297801463111, 0.22413333341424527, 0.24642443911265677], 'audit_candidate_briers': [0.5573865705936081, 0.18683207454428277, 0.2222644657407454, 0.24657748450017997], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1467.136 |
| Base scoring parameter | 0.087 |
| Home-advantage parameter | 0.174 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1620, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 32.00 |
| Over 1 5 in window quote fixtures | 4 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 3, 'ANCHORED_MAIN': 4, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
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

## 2026-11-06 — Famalicão vs Arouca

The model's most likely 1X2 outcome is **Famalicão win** at **40.8%**. Expected goals are 1.47 for Famalicão and 1.00 for Arouca (2.47 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 42.5%; Under 3.5 goals: 77.5%; Double Chance 1X: 70.0%; Double Chance X2: 59.2%; Double Chance 12 (either team wins): 70.8%; Under 4.5 goals: 90.4%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Famalicão win | 40.8% | 2.45 |
| Draw | 29.2% | 3.43 |
| Arouca win | 30.0% | 3.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Famalicão expected goals | 1.47 |
| Arouca expected goals | 1.00 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 68.8% |
| Under 1.5 | 31.2% |
| Over 2.5 | 42.5% |
| Under 2.5 | 57.5% |
| Over 3.5 | 22.5% |
| Under 3.5 | 77.5% |
| Over 4.5 | 9.6% |
| Under 4.5 | 90.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.73% |
| 2 | 1-0 | 11.21% |
| 3 | 0-1 | 10.56% |
| 4 | 0-0 | 9.38% |
| 5 | 2-0 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Famalicão win | 40.8% | 37.5% | 2.60 | +6.1% |
| Draw | 29.2% | 31.0% | 3.13 | -8.7% |
| Arouca win | 30.0% | 31.6% | 3.07 | -7.9% |

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
| Market best home last update utc | 2026-11-06T13:39:19Z |
| Market best draw last update utc | 2026-11-06T13:39:19Z |
| Market best away last update utc | 2026-11-06T13:39:19Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Famalicao |
| Matched away-team name | Arouca |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4704 |
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
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.66 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.21 |
| Fair Over 2.5 odds | 2.35 |
| Fair Under 2.5 odds | 1.74 |
| Fair Over 3.5 odds | 4.45 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.46 |
| Fair Under 4.5 odds | 1.11 |
| Score matrix json | [[0.09384600260514517,0.10557866458919433,0.04852341707283879,0.015945705600187564,0.00393004361233732,0.000774891657083733,0.00012732197134170028,1.7931595511055736e-05,2.2097470680887346e-06,2.420547873186514e-07,2.38631238927713e-08,2.1386919286474256e-09,1.7570357737026782e-10,1.3324498466571788e-11,9.382886330318416e-13,6.166785116501209e-14],[0.11214040598005534,0.13731064128153786,0.07038558315848148,0.023130023713249685,0.0057007199447102795,0.0011240181433761864,0.00018468672946756173,2.6010653889298075e-05,3.205345901066629e-06,3.5111227505167035e-07,3.4614625112953464e-08,3.1022769556443327e-09,2.548666087895974e-10,1.9327834918471047e-11,1.3610334265574206e-12,8.945222591937882e-14],[0.07751178987140794,0.07641548697885811,0.05167334248918006,0.016775613773065013,0.004134586164132907,0.0008152215700667479,0.00013394855452671168,1.8864861058563563e-05,2.3247552839545314e-06,2.546527401039768e-07,2.5105101014734785e-08,2.2500020177306364e-09,1.8484822349126955e-10,1.4017983625157108e-11,9.87122684317849e-13,6.487740833161571e-14],[0.03747821059652582,0.03694813032418626,0.01821277367201199,0.008210507484276283,0.0019991396308345925,0.00039417288307339455,6.476630386139652e-05,9.12146702843519e-06,1.1240569758739788e-06,1.2312874000758563e-07,1.2138724501630368e-08,1.0879125563093528e-09,8.937712133718832e-11,6.77792298841087e-12,4.772898665976867e-13,3.136928171111689e-14],[0.013590993110671933,0.013398766288344986,0.006604629131506287,0.0021704050968078376,0.0007338308655851561,0.0001429417480983151,2.3486670670064537e-05,3.307783204414131e-06,4.0762486714139264e-07,4.465106072390599e-08,4.40195298676549e-09,3.945175562673348e-10,3.24114684508982e-11,2.4579269707368655e-12,1.7308305774139617e-13,1.137566828396118e-14],[0.003942879679564095,0.0038871128032623966,0.0019160673382451396,0.0006296556905695377,0.00015518750858322305,4.197608415834392e-05,6.813712270437102e-06,9.596201745438957e-07,1.1825595027892344e-07,1.295370828059874e-08,1.2770495018708783e-09,1.144533915344509e-10,9.402883166759341e-12,7.130685909303493e-13,5.021308345079649e-14,3.3001923371643003e-15],[0.0009532232143820915,0.000939741118704693,0.0004632248548189258,0.00015222438169480886,3.751784172627924e-05,7.397440184688321e-06,1.6674214234102407e-06,2.3199597799184287e-07,2.8589337287904875e-08,3.131664278115978e-09,3.087370982705177e-10,2.76700378002564e-11,2.273223442027151e-12,1.7239012842427955e-13,1.2139421108659365e-14,7.978483249224302e-16],[0.00019752810931846946,0.00019473433255283166,9.599003505282648e-05,3.154412718309636e-05,7.774494189910645e-06,1.532906827521138e-06,2.518709775475788e-07,4.8662593709576463e-08,5.924318308601575e-09,6.489473971502346e-10,6.397688849550074e-11,5.733819916459131e-12,4.710602110683157e-13,3.5722898497483146e-14,2.515546058504859e-15,1.653311299672816e-16],[3.5815519607014366e-05,3.5308955924141284e-05,1.740477846102204e-05,5.719536877613934e-06,1.4096603772196807e-06,2.77944514966691e-07,4.566889221953235e-08,6.4318522097092626e-09,1.0873296605570577e-09,1.176662314378865e-10,1.160019964860834e-11,1.0396481814643166e-12,8.541197647166502e-14,6.477225828619627e-15,4.56115281473533e-16,2.997760849037472e-17],[5.772462007317694e-06,5.690818081841903e-06,2.80516445145625e-06,9.2182968969164e-07,2.2719790359060115e-07,4.479689727783109e-08,7.360550625709963e-09,1.036635037676732e-09,1.2774664885630952e-10,1.919650525531541e-11,1.8696283757328883e-12,1.675622661440979e-13,1.3766026419899799e-14,1.0439479984872546e-15,7.351305138533681e-17,4.831553694590042e-18],[8.373237689244719e-07,8.254809193219079e-07,4.0690278566904487e-07,1.337158926469483e-07,3.2956164057044956e-08,6.498008443753376e-09,1.0676837688088484e-09,1.5036896832690955e-10,1.8530274491583886e-11,2.029798666005722e-12,2.7451629453493675e-13,2.4305723976951194e-14,1.996829274997768e-15,1.514297489609096e-16,1.0663426657997382e-17,7.0084042895155585e-19],[1.1041626969836049e-07,1.088545759733711e-07,5.365748518181631e-08,1.7632856743607187e-08,4.3458657616040105e-09,8.568798348448834e-10,1.4079339837777093e-10,1.9828865699554636e-11,2.443551540971403e-12,2.676656333629966e-13,2.6387985305036405e-14,3.244357575278751e-15,2.633180233888991e-16,1.996874879486554e-17,1.406165497117676e-18,9.241847501597658e-20],[1.3347015389217718e-08,1.3158239312670114e-08,6.486066613415557e-09,2.1314432280290217e-09,5.253241878036781e-10,1.0357883284436668e-10,1.7018974286868814e-11,2.396894736307296e-12,2.95374224385487e-13,3.235517136577988e-14,3.1897549783100624e-15,2.8587636962909075e-16,3.221900895886561e-17,2.41380367401101e-18,1.6997596985560252e-19,1.117145880454054e-20],[1.4892689856165737e-09,1.4682052235821162e-09,7.237196904565093e-10,2.378278739882494e-10,5.861602743953144e-11,1.1557396078683907e-11,1.8989886377830284e-12,2.674471324468362e-13,3.2958055317986634e-14,3.610211858921789e-15,3.5591501338575056e-16,3.1898278273748075e-17,2.6205932371916583e-18,2.7262860977120873e-19,1.896603344074538e-20,1.2465189135194787e-21],[1.5430409297478555e-10,1.52121663389026e-10,7.498505070771375e-11,2.464149507866446e-11,6.073243339649242e-12,1.1974690511219742e-12,1.9675540292086295e-13,2.7710365010945896e-14,3.4148047674203437e-15,3.740563133443001e-16,3.687657760082861e-17,3.3050006036688044e-18,2.71521307719507e-19,2.0590845687370443e-20,1.9891215089118552e-21,1.2915260586515618e-22],[1.4921707528645564e-11,1.4710659491275044e-11,7.251298226185092e-12,2.3829126988386105e-12,5.873023788121366e-13,1.1579915095555265e-13,1.9026887235879638e-14,2.6796824000832877e-15,3.302227246505852e-16,3.6172461788677994e-17,3.566084962547841e-18,3.196043049746035e-19,2.6256993340078888e-20,1.9912017315355438e-21,1.4021705623369822e-22,1.2642260979711442e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1948889946518009, "-10": 2.715720337814539e-08, "-11": 2.408065186597062e-09, "-12": 1.9604990425476786e-10, "-13": 1.4750409301460825e-11, "-14": 1.0277408589512204e-12, "-15": 6.166785116501209e-14, "-2": 0.07620667537419383, "-3": 0.022529842654675412, "-4": 0.005197552670401459, "-5": 0.0009796132608436074, "-6": 0.00015578502797074605, "-7": 2.140413697210306e-05, "-8": 2.587085493553243e-06, "-9": 2.7901130050857516e-07, "0": 0.29181801800070395, "1": 0.20910191510913403, "10": 9.529084284277374e-07, "11": 1.2432345749894458e-07, "12": 1.4892588576206387e-08, "13": 1.6486419472317849e-09, "14": 1.690147524660606e-10, "15": 1.4921707528645564e-11, "2": 0.12173330249055224, "3": 0.05295332855691149, "4": 0.017974330441022507, "5": 0.004984564209334891, "6": 0.0011663179854194013, "7": 0.00023578039695833762, "8": 4.193141041228789e-05, "9": 6.653791687572826e-06} |
| Raw goal margin distribution | {"-1": 0.17011077638429595, "-10": 2.6448470947834838e-08, "-11": 2.376555896062463e-09, "-12": 1.9607824597654373e-10, "-13": 1.4950659079596553e-11, "-14": 1.0555073892829518e-12, "-15": 6.404545522875086e-14, "-2": 0.0671378878437899, "-3": 0.02006786092065592, "-4": 0.004684916866385859, "-5": 0.0008940014330983046, "-6": 0.00014398754330830044, "-7": 2.004014371577611e-05, "-8": 2.454021916088652e-06, "-9": 2.681620786136518e-07, "0": 0.25035780238989375, "1": 0.24736395961895705, "10": 1.2577309206214505e-06, "11": 1.662853230903133e-07, "12": 2.018617413981552e-08, "13": 2.2646633793437315e-09, "14": 2.3524657756437713e-10, "15": 2.100240696879049e-11, "2": 0.14534667726911313, "3": 0.06392301239264665, "4": 0.021957189809017997, "5": 0.006164981805602855, "6": 0.0014609562914433545, "7": 0.00029917951213326885, "8": 5.3904890943846576e-05, "9": 8.666940497925465e-06} |
| Research history json | {"away": [{"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 2.04, "date": "2026-10-24T00:00:00+00:00", "home": "Alverca", "home_goals": 0.0, "home_xg": 0.39, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": 1.45, "date": "2026-10-11T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.74, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 2.0, "away_xg": 2.08, "date": "2026-09-19T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-13T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 1.08, "date": "2026-09-07T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-08-29T00:00:00+00:00", "home": "Arouca", "home_goals": 2.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 0.54, "date": "2026-08-23T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.99, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 0.0, "away_xg": 0.49, "date": "2026-08-16T00:00:00+00:00", "home": "Arouca", "home_goals": 4.0, "home_xg": 2.14, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 0.49, "date": "2026-08-08T00:00:00+00:00", "home": "Guimaraes", "home_goals": 0.0, "home_xg": 2.22, "source": "pipeline training history"}], "h2h": [{"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2026-03-06T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": null, "date": "2025-10-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2025-04-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2024-11-09T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2024-02-23T00:00:00+00:00", "home": "Arouca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2023-09-22T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": null, "date": "2023-04-03T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Famalicao", "away_goals": 0.0, "away_xg": 0.17, "date": "2026-11-01T00:00:00+00:00", "home": "Sp Braga", "home_goals": 3.0, "home_xg": 1.15, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.65, "date": "2026-10-25T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.58, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 4.0, "away_xg": 2.89, "date": "2026-10-12T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.36, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Sp Lisbon", "away_goals": 1.0, "away_xg": 2.28, "date": "2026-09-13T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.35, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-09-05T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 0.0, "away_xg": 0.27, "date": "2026-08-30T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": 0.23, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 0.0, "away_xg": 1.05, "date": "2026-08-23T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.36, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 2.0, "away_xg": 1.61, "date": "2026-08-16T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": 1.47, "date": "2026-08-07T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 1.22, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 70.0% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.0% |
| P home draw | 70.0% |
| P draw away | 59.2% |
| P home away | 70.8% |
| Raw p home draw | 73.7% |
| Raw p draw away | 51.3% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9865 |
| Totals anchor target over 2 5 | 0.4251 |
| Totals anchor reference over odds | 2.25 |
| Totals anchor reference under odds | 1.69 |
| Totals anchor reference last update utc | 2026-11-06T13:39:19Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4329 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.26, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.39, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.94, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 6.26, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.07, "draw": 3.13, "home": 2.6}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.25, "under": 1.69}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.4, "under": 3.09}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.60 |
| Reference draw odds | 3.13 |
| Reference away odds | 3.07 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:19Z |
| Market reference home last update utc | 2026-11-06T13:39:19Z |
| Market reference draw last update utc | 2026-11-06T13:39:19Z |
| Market reference away last update utc | 2026-11-06T13:39:19Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.28 |
| Reference Under 2.5 odds | 1.72 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Home probability edge | +3.4% |
| Draw probability edge | -1.8% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.1120 |
| Raw ev home | 0.2651 |
| Raw edge prob draw | -0.0592 |
| Raw ev draw | -0.2164 |
| Raw edge prob away | -0.0527 |
| Raw ev away | -0.1924 |
| Market p home draw | 69.2% |
| Market reference home draw last update utc | 2026-11-06T13:39:20Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.5% |
| Market reference draw away last update utc | 2026-11-06T13:39:20Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.2% |
| Market reference home away last update utc | 2026-11-06T13:39:20Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.53 |
| Market reference dc home draw odds | 1.36 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 70.4% |
| Market over 1 5 odds | 1.40 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 2.90 |
| Market reference over 1 5 last update utc | 2026-11-06T13:39:20Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 77.9% |
| Market under 3 5 odds | 1.26 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 4.03 |
| Market reference under 3 5 last update utc | 2026-11-06T13:39:19Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,482.5254 |
| Elo away rating | 1,488.7246 |
| Elo rating diff | 53.8007 |
| Elo home expectancy | 0.5768 |
| Research p home | 0.4024 |
| Research p draw | 0.2768 |
| Research p away | 0.3207 |
| Research p over 1 5 | 0.6869 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4703552085361256, 0.9993176257513561], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "rotation": "schedule congestion only; rotation unconfirmed", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "recent": {"away": [], "home": []}, "rest_and_travel": {}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "schedules": {"away": [], "home": []}, "sources": [{"observed_at_utc": "2026-11-06T13:40:17.062026+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-06T13:40:17.064505+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/summary?event=401885399"}, {"observed_at_utc": "2026-11-06T13:40:17.065904+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/all/teams/12698/schedule"}, {"observed_at_utc": "2026-11-06T13:40:17.067386+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/all/teams/15784/schedule"}, {"observed_at_utc": "2026-11-06T13:40:17.068793+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/v2/sports/soccer/por.1/standings"}, {"observed_at_utc": "2026-11-06T13:40:17.070085+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:17.071536+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Famalic%C3%A3o%22+%22Arouca%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:17.157592+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Famalic%C3%A3o_vs_Arouca&d=2026-11-06"}, {"observed_at_utc": "2026-11-06T13:40:17.158101+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://geocoding-api.open-meteo.com/v1/search?name=Vila+Nova+de+Famalic%C3%A3o&count=10&language=en&format=json"}], "venue": {"address": {"city": "Vila Nova de Famalic\u00e3o", "country": "Portugal"}, "fullName": "Est\u00e1dio Municipal 22 de Junho", "id": "8157"}}, "form": {"away": {"all": {"goals_against": 0.6319445048828116, "goals_for": 1.2081082699386303, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.1060493109621126, "results": "WWWDLDWLWW", "xg_against": 1.023157856687065, "xg_for": 1.2317353640143311, "xg_matches": 10}, "venue": {"goals_against": 0.792388231715419, "goals_for": 0.8583663485684871, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 1.6443849010337144, "results": "WDDLW", "xg_against": 1.4009952478886567, "xg_for": 1.3739582889860773, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.5415943551474574, "goals_for": 1.5655575353063838, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 1.1025143978756544, "results": "LWLWDDDLLD", "xg_against": 1.3722444855381826, "xg_for": 0.8727767251907648, "xg_matches": 10}, "venue": {"goals_against": 1.8825279789738854, "goals_for": 0.7695192334124757, "last_match": "2026-10-12T00:00:00+00:00", "matches": 4, "points_per_game": 0.495233644025069, "results": "LDDL", "xg_against": 1.8678153299912186, "xg_for": 0.3735383586410355, "xg_matches": 4}}}, "goal_rates": [1.2733833582583605, 1.1053546366141647], "h2h": [{"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2026-03-06T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": null, "date": "2025-10-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2025-04-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2024-11-09T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2024-02-23T00:00:00+00:00", "home": "Arouca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2023-09-22T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": null, "date": "2023-04-03T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.19355879214645225, "-10": 7.896953540369669e-08, "-11": 7.852371556639966e-09, "-12": 7.167769073063311e-10, "-13": 6.0224535272492e-11, "-14": 4.320577356317627e-12, "-2": 0.08831014511769805, "-3": 0.02931624469490517, "-4": 0.007590247052090621, "-5": 0.0016050616493541994, "-6": 0.0002863289542302773, "-7": 4.4125447705169536e-05, "-8": 5.9816261685202575e-06, "-9": 7.234732999327667e-07, "0": 0.2768445991614601, "1": 0.22298232313826702, "10": 3.2511342845084443e-07, "11": 3.7242060279098054e-08, "12": 3.91628595378548e-09, "13": 3.790717147826535e-10, "14": 3.132905103272459e-11, "2": 0.11719947423793406, "3": 0.04482093741963713, "4": 0.01336860347152221, "5": 0.003256712195683352, "6": 0.0006692840296401316, "7": 0.00011882063043718831, "8": 1.8555793362519876e-05, "9": 2.5854747478321193e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:17.158624+00:00", "p_over_1_5": 0.6869009639512225, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Alverca vs Casa Pia

The model's most likely 1X2 outcome is **Alverca win** at **52.9%**. Expected goals are 1.43 for Alverca and 0.91 for Casa Pia (2.33 combined). The most likely exact score is 1-0 at 12.3%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 48.9%; Under 3.5 goals: 72.4%; Double Chance 1X: 78.6%; Double Chance X2: 47.1%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

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
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 48.9% |
| Under 2.5 | 51.1% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 12.8% |
| Under 4.5 | 87.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.31% |
| 2 | 1-1 | 12.21% |
| 3 | 2-1 | 9.77% |
| 4 | 2-0 | 9.48% |
| 5 | 0-0 | 7.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alverca win | 52.9% | 54.3% | 1.79 | -5.3% |
| Draw | 25.7% | 25.7% | 3.64 | -6.3% |
| Casa Pia win | 21.4% | 20.0% | 4.63 | -1.1% |
| Over 2.5 | 48.9% | 48.9% | 1.96 | -4.2% |
| Under 2.5 | 51.1% | 51.1% | 1.88 | -3.9% |

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
| Market best home last update utc | 2026-11-06T13:39:19Z |
| Market best draw last update utc | 2026-11-06T13:39:19Z |
| Market best away last update utc | 2026-11-06T13:39:19Z |
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
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.17 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.80 |
| Fair Under 4.5 odds | 1.15 |
| Score matrix json | [[0.070564025729596,0.06806837994891216,0.032427754440010406,0.011133485312944086,0.0028668612124264736,0.0005905710911036924,0.00010138097260505545,1.4917427401338955e-05,1.9206112373618274e-06,2.1980242308175498e-07,2.2639560691666467e-08,2.119877814586273e-09,1.819554647053502e-10,1.4416414833694506e-11,1.0606320700187227e-12,7.282978286909201e-14],[0.12309586782076927,0.12207129018603188,0.052546472060940326,0.018040884576814322,0.004645509539676682,0.00095697120798443,0.00016427941238908661,2.4172447204620915e-05,3.112190358745325e-06,3.561714982379988e-07,3.6685520286560836e-08,3.435085231166228e-09,2.948436580819264e-10,2.336059811600729e-11,1.7186658279801086e-12,1.180145901812209e-13],[0.0948486104286522,0.09769368518385287,0.05361572032855607,0.014616874552999707,0.0037638304201272057,0.0007753460224404921,0.0001331005446161887,1.958471753003937e-05,2.5215224821791046e-06,2.8857310665296027e-07,2.9722913289370046e-08,2.7831345901601534e-09,2.388847810971399e-10,1.8926950654268587e-11,1.3924773310948483e-12,9.561640133319779e-14],[0.05123142139581122,0.052768156863284545,0.02717549409019391,0.009942871866543041,0.0020329911154677335,0.000418794525546529,7.189277795875911e-05,1.0578467224399968e-05,1.3619723078674236e-06,1.5586955215919724e-07,1.605450084041377e-08,1.5032791766307305e-09,1.2903095606909042e-10,1.0223181766442012e-11,7.521311341413656e-13,5.1646135108504316e-14],[0.0207540616017474,0.02137659952258945,0.01100890553178992,0.003779709392968151,0.001037179841026673,0.00016965540179952697,2.9124062964195406e-05,4.28538101121694e-06,5.517406389912441e-07,6.314340299785733e-08,6.503744974260959e-09,6.089846384580145e-10,5.227097624523875e-11,4.141453396488154e-12,3.046914464847996e-13,2.0922063849309974e-14],[0.006726045246979515,0.0069277994049796844,0.003567802685923787,0.0012249407795627246,0.0003154210123549528,6.924306213793392e-05,9.43862310096283e-06,1.3888205178867329e-06,1.7880993964767097e-07,2.0463723860976306e-08,2.1077552823690066e-09,1.9736176520933122e-10,1.6940151671307853e-11,1.342175978252421e-12,9.874541642739714e-14,6.78049197361952e-15],[0.0018164992445224432,0.0018709868761290175,0.0009635544581708107,0.0003308190651348436,8.518557482297308e-05,1.7548159517257658e-05,3.2102286897648377e-06,3.7507797359100956e-07,4.829109950293012e-08,5.52662635599611e-09,5.692402797588778e-10,5.330138056406356e-11,4.575017202990878e-12,3.624807090922502e-13,2.6668118895122154e-14,1.8312036412632625e-15],[0.00042049793654205445,0.0004331111741895338,0.00022305137897992515,7.658067278444968e-05,1.9719445820978654e-05,4.062189890454695e-06,6.973398600176517e-07,1.0934579808100758e-07,1.1178814280028875e-08,1.2793481669441924e-09,1.3177234384050553e-10,1.233863466203857e-11,1.0590619838148228e-12,8.39099661996632e-14,6.173351847335982e-15,4.2390182922533264e-16],[8.517273033454234e-05,8.772756781514627e-05,4.517952004433908e-05,1.5511574314837164e-05,3.9942147042827606e-06,8.228049986466442e-07,1.4124763687840562e-07,2.0783499256341044e-08,2.8515719349711715e-09,2.5913462815823114e-10,2.6690761909019507e-11,2.4992160756088393e-12,2.1451520427616663e-13,1.6996137917527484e-14,1.2504252374632294e-15,8.586219586672712e-17],[1.533503414715499e-05,1.579502315832801e-05,8.134404989844873e-06,2.792801414958165e-06,7.191435409040044e-07,1.481429877982777e-07,2.5431113059632043e-08,3.741991944387664e-09,4.817795713128995e-10,5.875725791263207e-11,4.805572671918938e-12,4.4997458353213155e-13,3.862266678240824e-14,3.0600915846105836e-15,2.251344255332195e-16,1.545916985864165e-17],[2.4849144113809463e-06,2.55945179499367e-06,1.3181124993467751e-06,4.525501813402973e-07,1.1653121417896652e-07,2.4005335872908202e-08,4.12089981234648e-09,6.063585917482556e-10,7.806836218140821e-11,8.9344552607472e-12,9.8067189019786e-13,7.291462911946472e-14,6.2584810945058004e-15,4.958623245162534e-16,3.6481156359815266e-17,2.5050295683137697e-18],[3.6605423613284646e-07,3.7703438293256405e-07,1.941719448668656e-07,6.666543933408246e-08,1.7166283231545592e-08,3.536240461974894e-09,6.070522292758464e-10,8.932304875709821e-11,1.150029737586676e-11,1.3161399767963797e-12,1.3556188537706555e-13,1.3526971146246424e-14,9.219406132897879e-16,7.304577718915579e-17,5.374061079678726e-18,3.6901741199597207e-19],[4.943003049884044e-08,5.09127315240372e-08,2.621995379205256e-08,9.002148791706348e-09,2.3180442129321182e-09,4.775152330793311e-10,8.197312650851096e-11,1.2061712687598622e-11,1.5529394114934544e-12,1.7772459043522205e-13,1.8305560944900067e-14,1.714059431592008e-15,1.5678347230224494e-16,9.863715913838282e-18,7.256848216742017e-19,4.983016211549676e-20],[6.1613263591218164e-09,6.3461412341491744e-09,3.26824990402786e-09,1.1220947282316175e-09,2.8893825811180685e-10,5.952104748393586e-11,1.021773970194827e-11,1.5034615105082484e-12,1.9356990949819862e-13,2.215291377856525e-14,2.2817411607902904e-15,2.1365310622693098e-16,1.833848628528145e-17,1.548373682291254e-18,9.045474937145266e-20,6.2112017375495196e-21],[7.13136828486272e-10,7.345280494916275e-10,3.782804603116642e-10,1.2987578146506682e-10,3.344288242630453e-11,6.889206731929196e-12,1.1826425124450369e-12,1.7401671504832455e-13,2.24045640993436e-14,2.5640678245175085e-15,2.640979490436373e-16,2.4729074502820335e-17,2.122570561347219e-18,1.6817223805683022e-19,1.3185054117606111e-20,7.189096064756779e-22],[7.70385843460198e-11,7.93494303405864e-11,4.0864796185087696e-11,1.40301916059218e-11,3.6127601543754524e-12,7.442256698780374e-13,1.2775823840086479e-13,1.8798638416029747e-14,2.4203151936028713e-15,2.76990540212733e-16,2.852991362989291e-17,2.6714268788057763e-18,2.292965735170612e-19,1.8167272574746062e-20,1.3365869489626262e-21,9.780512345366743e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1374441982240223, "-10": 2.6324065357634733e-08, "-11": 2.434421476520459e-09, "-12": 2.0676018628756082e-10, "-13": 1.623069706300781e-11, "-14": 1.1786466601999437e-12, "-15": 7.282978286909201e-14, "-2": 0.05468182644357529, "-3": 0.01663070350490792, "-4": 0.00396808421841087, "-5": 0.0007758624988666323, "-6": 0.0001282375176109472, "-7": 1.8334871661107704e-05, "-8": 2.308062568310071e-06, "-9": 2.594043509445616e-07, "0": 0.25730365349970297, "1": 0.252078444273867, "10": 2.889325029941891e-06, "11": 4.2036870610253097e-07, "12": 5.61684823849072e-08, "13": 6.936719204798532e-09, "14": 7.924862588268584e-10, "15": 7.70385843460198e-11, "2": 0.15994000643703468, "3": 0.07652721096943091, "4": 0.028726142707172643, "5": 0.008836338844590175, "6": 0.002297702891125185, "7": 0.0005168301137210272, "8": 0.00010235491019825276, "9": 1.8097955991030312e-05} |
| Raw goal margin distribution | {"-1": 0.1647906463325132, "-10": 1.1201279437053594e-08, "-11": 9.135786147039406e-10, "-12": 6.839494030643664e-11, "-13": 4.715513977052916e-12, "-14": 2.793563179439244e-13, "-2": 0.06006293665226491, "-3": 0.01646806466696228, "-4": 0.003511874933854104, "-5": 0.0006107438829931644, "-6": 8.951825047626734e-05, "-7": 1.132792173972629e-05, "-8": 1.2604164650886576e-06, "-9": 1.250897296831872e-07, "0": 0.25693306288151335, "1": 0.25565650119438904, "10": 1.0403496123665656e-06, "11": 1.3349001159007875e-07, "12": 1.5722369131657817e-08, "13": 1.7053527187048277e-09, "14": 1.5894059961157434e-10, "2": 0.14865820957984838, "3": 0.06412332991694074, "4": 0.02151313549236161, "5": 0.005885928266608657, "6": 0.001357246069593342, "7": 0.0002702019099801743, "8": 4.729806897076306e-05, "9": 7.384858261191441e-06} |
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
| Totals anchor scale | 1.1370 |
| Totals anchor target over 2 5 | 0.4889 |
| Totals anchor reference over odds | 1.96 |
| Totals anchor reference under odds | 1.88 |
| Totals anchor reference last update utc | 2026-11-06T13:39:19Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4139 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.19, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.63, "draw": 3.64, "home": 1.79}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.96, "under": 1.88}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.96, "under": 1.88}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.3, "under": 3.52}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 3.64 |
| Reference away odds | 4.63 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:19Z |
| Market reference home last update utc | 2026-11-06T13:39:19Z |
| Market reference draw last update utc | 2026-11-06T13:39:19Z |
| Market reference away last update utc | 2026-11-06T13:39:19Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.96 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market best over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market best under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Home probability edge | -1.4% |
| Draw probability edge | -0.0% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0450 |
| Raw ev home | -0.1094 |
| Raw edge prob draw | -0.0005 |
| Raw ev draw | -0.0648 |
| Raw edge prob away | 0.0456 |
| Raw ev away | 0.1369 |
| Market p home draw | 78.6% |
| Market reference home draw last update utc | 2026-11-06T13:39:20Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.0% |
| Market reference draw away last update utc | 2026-11-06T13:39:20Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market reference home away last update utc | 2026-11-06T13:39:20Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.05 |
| Market reference dc home draw odds | 1.20 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 75.0% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-11-06T13:39:20Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.4% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.38 |
| Market reference under 3 5 last update utc | 2026-11-06T13:39:19Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,417.0742 |
| Elo away rating | 1,403.5352 |
| Elo rating diff | 73.5391 |
| Elo home expectancy | 0.6043 |
| Research p home | 0.4732 |
| Research p draw | 0.2643 |
| Research p away | 0.2624 |
| Research p over 1 5 | 0.7047 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4251352198000222, 0.9058679726510429], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:17.190051+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T13:40:17.070085+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:17.299642+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Alverca%22+%22Casa+Pia%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:17.385126+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Alverca_vs_Casa+Pia&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 1.6404619578729738, "goals_for": 0.6273910578083026, "last_match": "2026-10-30T00:00:00+00:00", "matches": 10, "points_per_game": 0.8786878561846695, "results": "LWLWLDLLLL", "xg_against": 1.7424276306361413, "xg_for": 0.7986589891384444, "xg_matches": 10}, "venue": {"goals_against": 0.7157020266306037, "goals_for": 0.9685668669792039, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 1.6490589562063098, "results": "WWDLL", "xg_against": 1.6257944158120676, "xg_for": 0.9612876162123404, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.2097349947013118, "goals_for": 1.2751965627375945, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 1.1634978383066994, "results": "LLWWWLDLDL", "xg_against": 1.522332345560108, "xg_for": 1.3567986568754096, "xg_matches": 10}, "venue": {"goals_against": 1.1195224506526886, "goals_for": 0.8897994815892832, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.9956615910184449, "results": "LWLDD", "xg_against": 1.4696091377324454, "xg_for": 1.3868989962085467, "xg_matches": 5}}}, "goal_rates": [1.4522057152034507, 1.0090614407581595], "h2h": [{"away": "Casa Pia", "away_goals": 1.0, "away_xg": null, "date": "2026-04-12T00:00:00+00:00", "home": "Alverca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 2.0, "away_xg": null, "date": "2025-11-29T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.16661688540024225, "-10": 2.9378934568074392e-08, "-11": 2.665694076021549e-09, "-12": 2.2208365273808978e-10, "-13": 1.7099025808533077e-11, "-14": 1.2189995710946011e-12, "-15": 7.470502348937847e-14, "-2": 0.06894905920109684, "-3": 0.0208156156651518, "-4": 0.004907700022323983, "-5": 0.0009457579113423571, "-6": 0.0001538220765038172, "-7": 2.1619100707260264e-05, "-8": 2.67332730196687e-06, "-9": 2.94987471338972e-07, "0": 0.26434971395751367, "1": 0.23978915797816214, "10": 1.1198022865866047e-06, "11": 1.4622652039139416e-07, "12": 1.7532464229912042e-08, "13": 1.94271130849931e-09, "14": 1.9932004841968698e-10, "15": 1.757955059843773e-11, "2": 0.14280697053993688, "3": 0.062047009281015544, "4": 0.021053297735744093, "5": 0.005838921504887808, "6": 0.001366727253250519, "7": 0.0002764466555274344, "8": 4.9196746201402367e-05, "9": 7.812649632114155e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:17.385597+00:00", "p_over_1_5": 0.70466128766477, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Nacional vs Académico de Viseu

The model's most likely 1X2 outcome is **Académico de Viseu win** at **43.7%**. Expected goals are 0.92 for Nacional and 1.60 for Académico de Viseu (2.51 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 45.2%; Under 3.5 goals: 75.4%; Double Chance 1X: 56.3%; Double Chance X2: 71.5%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 89.1%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

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
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 70.9% |
| Under 1.5 | 29.1% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 10.9% |
| Under 4.5 | 89.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.12% |
| 2 | 0-1 | 10.65% |
| 3 | 1-0 | 10.04% |
| 4 | 0-0 | 8.42% |
| 5 | 0-2 | 8.25% |

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
| Market best home last update utc | 2026-11-06T13:39:19Z |
| Market best draw last update utc | 2026-11-06T13:39:19Z |
| Market best away last update utc | 2026-11-06T13:39:19Z |
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
| Dc lambda away | 1.5960 |
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
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.87 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.44 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.06 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 9.15 |
| Fair Under 4.5 odds | 1.12 |
| Score matrix json | [[0.08422298436512664,0.10645654785592437,0.08252141899575652,0.0446363723019845,0.0181080780892518,0.0058768663343524066,0.0015894176133995116,0.00036845413953513143,7.473721526775605e-05,1.3475281957510812e-05,2.1866602985605354e-06,3.225760305813967e-07,4.362086829077677e-08,5.4449564755183625e-09,6.311169374493026e-10,6.82750513233998e-11],[0.10035297991195599,0.13118833828977983,0.07706279579723367,0.04168376750785166,0.016910265735301168,0.0054881236382414295,0.0014842808869322951,0.0003440816512995418,6.979350123546888e-05,1.2583919598561465e-05,2.0420171891924667e-06,3.0123828548142964e-07,4.0735437011365684e-08,5.084783733775517e-09,5.893698419961982e-10,6.375879622781771e-11],[0.04334091063140616,0.07033014142485715,0.052315835658444165,0.019463235742965834,0.007895843110159577,0.0025625477384575673,0.000693049370014361,0.00016066067667253197,3.258840189090478e-05,5.875759518886946e-06,9.534709629343152e-07,1.4065599430347855e-07,1.90204355567333e-08,2.3742178413654514e-09,2.7519211578957726e-10,2.9770641087948395e-11],[0.013491332659649477,0.021892648773175007,0.017762814185846843,0.008808707513369752,0.002457849742325732,0.0007976801477427058,0.00021573519024422222,5.0011100429967856e-05,1.0144248571416829e-05,1.8290300121189183e-06,2.9680026918820223e-07,4.3783962590460776e-08,5.920757540368012e-09,7.39056061298474e-10,8.566290660121988e-11,9.267124676367463e-12],[0.0031497271448900424,0.005111123700970588,0.004146960083352753,0.0022431176833195366,0.000834283663487836,0.0001862288090930802,5.036618708932633e-05,1.1675742088934928e-05,2.368306815639202e-06,4.2701085380687637e-07,6.929188450513238e-08,1.0221935739119747e-08,1.3822778826724185e-09,1.725422533557039e-10,1.9999120104644488e-11,2.1635308300961655e-12],[0.0005882758264157992,0.0009546066629866177,0.0007745294299874466,0.0004189480066689268,0.00016995877641606705,5.057026893764009e-05,9.406913351670838e-06,2.1806831228314883e-06,4.423296320878483e-07,7.975299172161329e-08,1.2941673594583029e-08,1.909155116580674e-09,2.5816860520271683e-10,3.222578719212021e-11,3.735243837306827e-12,4.0408353755839813e-13],[9.156043048221773e-05,0.0001485768972299568,0.00012054931521301885,6.520590872139866e-05,2.6452725123345575e-05,8.585070649852222e-06,2.1286991899183137e-06,3.394058985701603e-07,6.884507183604492e-08,1.2412915721466988e-08,2.0142680563638215e-09,2.9714473463321015e-10,4.018187994120786e-11,5.015686206105209e-12,5.813608486746396e-13,6.28923729112638e-14],[1.2214842164139546e-05,1.982126273700702e-05,1.6082174915157363e-05,8.698953019403532e-06,3.528990203424048e-06,1.14531225337891e-06,3.0975342381397183e-07,6.58324089646992e-08,9.184444435519093e-09,1.6559752453755951e-09,2.6871833449418563e-10,3.9641316825773386e-11,5.3605615302953574e-12,6.691298307550625e-13,7.75578595422844e-14,8.390310141546262e-15],[1.4258569151587931e-06,2.3137658400297185e-06,1.8772964894209689e-06,1.0154418821531882e-06,4.1194433930978873e-07,1.3369402359456978e-07,3.6157983492894054e-08,8.382037913059823e-09,1.5587673686502063e-09,1.9330448344904185e-10,3.1367895738624863e-11,4.627390592730696e-12,6.257464177102008e-13,7.810853251318679e-14,9.053445707054754e-15,9.794135343617374e-16],[1.479488216192779e-07,2.400794398764848e-07,1.947907959677063e-07,1.0536360857126739e-07,4.274389591667253e-08,1.3872270799453758e-08,3.7518007543605575e-09,8.697314708237782e-10,1.764162786774744e-10,2.916203448410045e-11,3.2547748388126886e-12,4.801442403429344e-13,6.492828568454114e-14,8.104645859539194e-15,9.39397642016339e-16,1.0162525899076895e-16],[1.3816230946627387e-08,2.2419867563434857e-08,1.8190578295329454e-08,9.839402122017284e-09,3.991647456733785e-09,1.2954648440027496e-09,3.5036268028796557e-10,8.122005116994786e-11,1.6474670242557486e-11,2.9704187650038554e-12,4.419156191026129e-13,4.483836802257138e-14,6.063341229541317e-15,7.568540101263664e-16,8.772584080604647e-17,9.490295582349756e-18],[1.1729377735385468e-09,1.903349013524099e-09,1.5443007928519514e-09,8.353223438818255e-10,3.388734669200805e-10,1.0997931749200844e-10,2.974426410035365e-11,6.895228253926982e-12,1.3986276799175941e-12,2.5217560318440047e-13,4.092102721765567e-14,5.5344633222207655e-15,5.147512363868471e-16,6.425360584668307e-17,7.447541431113586e-18,8.056847206438231e-19],[9.12791947685236e-11,1.4812053054938463e-10,1.2017903765402622e-10,6.50056231812395e-11,2.6371473309761503e-11,8.55870086916629e-12,2.3147284854436994e-12,5.365935831914308e-13,1.0884260979907033e-13,1.9624558538596975e-14,3.1845154089120093e-15,4.697795723498343e-16,5.824176852397133e-17,5.00028009581924e-18,5.7957514897522e-19,6.269919359473524e-20],[6.557020200224399e-12,1.0640204630893454e-11,8.63303384237035e-12,4.669664159598252e-12,1.8943887885984434e-12,6.148123307739079e-13,1.6627799440582925e-13,3.8546078032562755e-14,7.818684125199474e-15,1.4097257001925226e-15,2.2875894027236117e-16,3.3746508756591943e-17,4.563426523327481e-18,5.222390969155349e-19,4.1633649037064694e-20,4.503982314710651e-21],[4.373776225766583e-13,7.097412030284828e-13,5.758554499299172e-13,3.1148395856499203e-13,1.2636277444512177e-13,4.1010267980492615e-14,1.1091360352610716e-14,2.5711666968724116e-15,5.215352965117559e-16,9.403394475044005e-17,1.525907171005161e-17,2.251017584133024e-18,3.043975132954344e-19,3.7996291135270936e-20,4.037707390542329e-21,3.0043236360138747e-22],[2.7229732454178716e-14,4.418621820732331e-14,3.5850919261705203e-14,1.9391995423832328e-14,7.866942346153819e-15,2.5531681717147386e-15,6.905126356836912e-16,1.6007261834402445e-16,3.2469120175293945e-17,5.8542527669364886e-18,9.499810203275972e-19,1.4014115812440994e-19,1.8950815997220456e-20,2.3655276092301053e-21,2.74184843699223e-22,2.719404782908623e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.20563641364784196, "-10": 2.5076784788636392e-06, "-11": 3.6577351187155916e-07, "-12": 4.8990111265018235e-08, "-13": 6.064096958602509e-09, "-14": 6.948757336771202e-10, "-15": 6.82750513233998e-11, "-2": 0.13295132716462388, "-3": 0.06433705172403564, "-4": 0.02434171231228823, "-5": 0.007532392401640405, "-6": 0.001967987938501864, "-7": 0.00044443068575724325, "-8": 8.831980488526332e-05, "-9": 1.566405223893669e-05, "0": 0.27742291587912166, "1": 0.19086791536793524, "10": 1.5844557577907728e-08, "11": 1.330010688831213e-09, "12": 1.025146468447708e-10, "13": 7.302612322514587e-12, "14": 4.815638407839817e-13, "15": 2.7229732454178716e-14, "2": 0.06982710257642459, "3": 0.01944585821799522, "4": 0.004234008250087368, "5": 0.0007539944100925986, "6": 0.00011336845729779318, "7": 1.4733585803308407e-05, "8": 1.6849892532115628e-06, "9": 1.7197993168831517e-07} |
| Raw goal margin distribution | {"-1": 0.25586056545077984, "-10": 2.72956385128969e-06, "-11": 3.9172395792051716e-07, "-12": 5.161777437216301e-08, "-13": 6.2858938540439215e-09, "-14": 7.087796931264211e-10, "-15": 6.870023041480927e-11, "-2": 0.16357552077754256, "-3": 0.07810499836830062, "-4": 0.02912542616016871, "-5": 0.008877319593879026, "-6": 0.002283651879657511, "-7": 0.0005076441294701334, "-8": 9.928535281986052e-05, "-9": 1.7328002194683814e-05, "0": 0.23887409110213745, "1": 0.14976145446856529, "10": 1.0875253958423497e-08, "11": 8.981748667595967e-10, "12": 6.811059186074598e-11, "13": 4.7732813904127e-12, "14": 3.0973898827513273e-13, "15": 1.727736140001535e-14, "2": 0.054173580638746, "3": 0.014886159653494322, "4": 0.003194557785559348, "5": 0.0005603442631635864, "6": 8.2954049277421e-05, "7": 1.0612108284641232e-05, "8": 1.1944338506960996e-06, "9": 1.1996651109097725e-07} |
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
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0167 |
| Totals anchor target over 2 5 | 0.4519 |
| Totals anchor reference over odds | 2.11 |
| Totals anchor reference under odds | 1.76 |
| Totals anchor reference last update utc | 2026-11-06T13:39:19Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4422 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.56, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.06, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.56, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.44, "draw": 3.23, "home": 3.05}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.11, "under": 1.76}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.34, "under": 3.31}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.05 |
| Reference draw odds | 3.23 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:19Z |
| Market reference home last update utc | 2026-11-06T13:39:19Z |
| Market reference draw last update utc | 2026-11-06T13:39:19Z |
| Market reference away last update utc | 2026-11-06T13:39:19Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Home probability edge | -2.7% |
| Draw probability edge | -1.7% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0894 |
| Raw ev home | -0.3209 |
| Raw edge prob draw | -0.0551 |
| Raw ev draw | -0.2284 |
| Raw edge prob away | 0.1445 |
| Raw ev away | 0.3138 |
| Market p home draw | 60.8% |
| Market reference home draw last update utc | 2026-11-06T13:39:20Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.3% |
| Market reference draw away last update utc | 2026-11-06T13:39:20Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.8% |
| Market reference home away last update utc | 2026-11-06T13:39:20Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home draw odds | 1.55 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 73.9% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.20 |
| Market reference over 1 5 last update utc | 2026-11-06T13:39:20Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.2% |
| Market under 3 5 odds | 1.28 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.70 |
| Market reference under 3 5 last update utc | 2026-11-06T13:39:19Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,377.6402 |
| Elo away rating | 1,452.3265 |
| Elo rating diff | -14.6862 |
| Elo home expectancy | 0.4789 |
| Research p home | 0.2805 |
| Research p draw | 0.2544 |
| Research p away | 0.4651 |
| Research p over 1 5 | 0.7438 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.91847318611981, 1.5959962519231132], "coverage": {"form": "last ten, exponential rank half-life five matches", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:17.190051+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T13:40:17.070085+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:17.191617+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Nacional%22+%22Acad%C3%A9mico+de+Viseu%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:17.279447+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Nacional_vs_Acad%C3%A9mico+de+Viseu&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 1.0650527153129232, "goals_for": 1.649570964958943, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.3738678769859316, "results": "WWWWWWLDLD", "xg_against": 1.584486958053463, "xg_for": 1.1369674333411801, "xg_matches": 10}, "venue": {"goals_against": 0.8979146949535403, "goals_for": 1.8037913442624962, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 2.3609841784542116, "results": "WWWDD", "xg_against": 1.8155259012043192, "xg_for": 1.326331413049327, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.8804243500740794, "goals_for": 0.874261798272425, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.6711447942719047, "results": "LWLLLLLLWD", "xg_against": 1.6090907760595652, "xg_for": 0.9211553615670336, "xg_matches": 10}, "venue": {"goals_against": 2.00259287486749, "goals_for": 1.0941233506910442, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 1.2227916852143603, "results": "WLLLW", "xg_against": 1.4674034895920058, "xg_for": 1.2859261160044595, "xg_matches": 5}}}, "goal_rates": [1.129224126948003, 1.5296199850556311], "h2h": [], "margin_distribution": {"-1": 0.23044617061866554, "-10": 1.581639197387135e-06, "-11": 2.1712656822759582e-07, "-12": 2.7376265084479365e-08, "-13": 3.190419325662832e-09, "-14": 3.438540758346763e-10, "-15": 3.144360273155852e-11, "-2": 0.1405398282453889, "-3": 0.06324290268229563, "-4": 0.022355014678771754, "-5": 0.0064801565659584155, "-6": 0.001588607917825491, "-7": 0.0003369831316436136, "-8": 6.294985762473605e-05, "-9": 1.0500370568338164e-05, "0": 0.25440772170372367, "1": 0.17012419971481274, "10": 7.604548156694733e-08, "11": 7.706826157277627e-09, "12": 7.17353780647067e-10, "13": 6.171682286850517e-11, "14": 4.910509658259449e-12, "15": 3.3149829049399237e-13, "2": 0.07659362381477004, "3": 0.025444949494911, "4": 0.006639897227097937, "5": 0.001420916300433999, "6": 0.00025715579749687514, "7": 4.027025303299081e-05, "8": 5.553509871756861e-06, "9": 6.838707385109562e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:17.279890+00:00", "p_over_1_5": 0.7437743636870905, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Sporting Lisbon vs Moreirense FC

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **84.6%**. Expected goals are 2.87 for Sporting Lisbon and 0.69 for Moreirense FC (3.56 combined). The most likely exact score is 2-0 at 12.5%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 68.8%; Under 3.5 goals: 53.1%; Double Chance 1X: 94.5%; Double Chance X2: 15.4%; Double Chance 12 (either team wins): 90.1%; Under 4.5 goals: 72.0%; BTTS Yes (both teams score): 45.3%; BTTS No (at least one team does not score): 54.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 84.6% | 1.18 |
| Draw | 9.9% | 10.05 |
| Moreirense FC win | 5.5% | 18.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 2.87 |
| Moreirense FC expected goals | 0.69 |
| Expected total goals | 3.56 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 86.6% |
| Under 1.5 | 13.4% |
| Over 2.5 | 68.8% |
| Under 2.5 | 31.2% |
| Over 3.5 | 46.9% |
| Under 3.5 | 53.1% |
| Over 4.5 | 28.0% |
| Under 4.5 | 72.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.46% |
| 2 | 3-0 | 11.71% |
| 3 | 1-0 | 9.15% |
| 4 | 2-1 | 8.45% |
| 5 | 4-0 | 8.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 84.6% | 85.7% | 1.15 | -2.7% |
| Draw | 9.9% | 9.3% | 8.51 | -15.4% |
| Moreirense FC win | 5.5% | 5.0% | 14.87 | -18.7% |

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
| Market best home last update utc | 2026-11-06T13:39:19Z |
| Market best draw last update utc | 2026-11-06T13:39:19Z |
| Market best away last update utc | 2026-11-06T13:39:19Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
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
| P btts yes | 45.3% |
| P btts no | 54.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.78 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.45 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.21 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.88 |
| Fair Over 4.5 odds | 3.57 |
| Fair Under 4.5 odds | 1.39 |
| Score matrix json | [[0.023375668543707817,0.019433154886323394,0.0057724800318777365,0.0013041507975396314,0.00022098075177360085,2.9955120372000938e-05,3.3838137081292605e-06,3.276385778589915e-07,2.7758223735285956e-08,2.0904307693713433e-09,1.416845241571255e-10,8.73004249118041e-12,4.930849398592156e-13,2.5707805924542566e-14,1.2445822523794658e-15,5.623658905984514e-17,2.3822405643335957e-18,9.497806574572605e-20,3.57632881958963e-21,1.2757643681494616e-22],[0.09147996066297231,0.04688305163152703,0.01626379275879657,0.003674406525492001,0.0006226067705183244,8.43976708632376e-05,9.533795626745075e-06,9.231120594023277e-07,7.820797918570623e-08,5.889727226758e-09,3.9919198079419226e-10,2.4596638025244123e-11,1.3892523196386534e-12,7.243098729336215e-14,3.506573901025944e-15,1.5844493612451875e-16,6.711892743839778e-18,2.6759790755263395e-19,1.0076201292669843e-20,3.5944285953450933e-22],[0.12464691114430973,0.08448277049829356,0.023560163217980826,0.005176266172611803,0.0008770881345638678,0.00011889397803584227,1.3430594425777918e-05,1.3004205423281188e-06,1.1017434088436724e-07,8.2970666414479e-09,5.623558341264916e-10,3.465015220464763e-11,1.9570887808624146e-12,1.0203608848786921e-13,4.939834430327112e-15,2.232069743489164e-16,9.455280226371918e-18,3.7697461810949934e-19,1.4194700433341525e-20,5.063598439332205e-22],[0.11706300236524994,0.07934257393040972,0.026888273454069852,0.004998984664692728,0.000823723343229191,0.00011166009573963806,1.2613434962791109e-05,1.2212988803720205e-06,1.0347098864411219e-07,7.792247099873617e-09,5.281403424770453e-10,3.2541928333810216e-11,1.8380133649509997e-12,9.582789303272333e-14,4.639279419702849e-15,2.0962636238852607e-16,8.879991339876908e-18,3.540383007189031e-19,1.3331050365768573e-20,4.755513238462484e-22],[0.08245539177602053,0.05588634227522478,0.018939229961987047,0.004278856180239973,0.0005966337834218871,7.864975913767354e-05,8.884495532185602e-06,8.602434212517999e-07,7.288161702433051e-08,5.488606771172035e-09,3.7200497144086247e-10,2.2921481558617762e-11,1.29463715293864e-12,6.749806773646661e-14,3.267758338509711e-15,1.4765402807111805e-16,6.254778624357013e-18,2.49373125579081e-19,9.389960606559762e-21,3.349629680178748e-22],[0.04646312837064416,0.03149162522146526,0.010672144707714151,0.002411110294910165,0.0004085485870065768,4.557365406261066e-05,5.006360985363774e-06,4.847421090448129e-07,4.106836259853162e-08,3.092797638724175e-09,2.0962261375854928e-10,1.291612006400207e-11,7.295204223125991e-13,3.803476423384039e-14,1.8413626070548185e-15,8.320217650953178e-17,3.524530972369686e-18,1.4052028977611636e-19,5.291187582286862e-21,1.887496626624799e-22],[0.021818083001080173,0.01478778801633483,0.005011408985959713,0.0011322053934781048,0.00019184560518992742,2.6005695745805548e-05,2.4174492730076977e-06,2.2762443985455974e-07,1.928481734474301e-08,1.4523110680137203e-09,9.843425843828928e-11,6.065131416901344e-12,3.4256705657072564e-13,1.7860304979049783e-14,8.646641671504483e-16,3.9069947646969424e-17,1.6550437301941292e-18,6.598529744304082e-20,2.484627572291447e-21,8.863277077567077e-23],[0.008781686761129854,0.005952022560506947,0.0020170710664374506,0.00045570791504891817,7.721705024194487e-05,1.0467183300824607e-05,1.1824021368960391e-06,9.42122354661405e-08,7.762057975430414e-09,5.845491044463912e-10,3.961937554854677e-11,2.441189918732933e-12,1.3788180131762389e-13,7.188697731899638e-15,3.4802369525831113e-16,1.5725489814684528e-17,6.661481493959485e-19,2.6558805049741502e-20,1.0000521611751951e-21,3.5674317935468053e-23],[0.0030927680296631557,0.002096206069254207,0.0007103798025965675,0.00016049295640629453,2.719459607580614e-05,3.6863726473032776e-06,4.164229067454201e-07,4.032024831219375e-08,2.8110809624904182e-09,2.058687392497505e-10,1.3953303207548976e-11,8.597476020679451e-13,4.8559740125899095e-14,2.5317430608593857e-15,1.2256831603518198e-16,5.538263146087491e-18,2.346066029809054e-19,9.353581538283963e-21,3.5220219488678866e-22,1.2563917729247167e-23],[0.0009681981094915025,0.0006562221071515608,0.00022238602290836946,5.024268729142303e-05,8.513330536415372e-06,1.1540273935090264e-06,1.303621439412589e-07,1.2622346007096336e-08,1.0693914825865433e-09,6.62726526631877e-11,4.368113501283837e-12,2.6914595436137426e-13,1.5201737775469307e-14,7.925679591007863e-16,3.8370291832635444e-17,1.733765952208313e-18,7.344413396082454e-20,2.9281601062487332e-21,1.1025770312469448e-22,3.933163197690175e-24],[0.0002727869705095571,0.00018488864916838934,6.265660806206677e-05,1.4155729413357838e-05,2.3986058464779866e-06,3.251438248786735e-07,3.672915074534024e-08,3.5563088734056587e-09,3.0129790583532137e-10,2.2690299606766854e-11,1.2655531040168973e-12,7.58310812584655e-14,4.28304491983452e-15,2.2330369205078846e-16,1.081071690182234e-17,4.88483459158907e-19,2.0692668792127235e-20,8.250005001249646e-22,3.106478365933177e-23,1.1081571660794504e-24],[6.986993350214588e-05,4.735621206015173e-05,1.6048468262941636e-05,3.6257592176713984e-06,6.143637677350272e-07,8.328028783951894e-08,9.407572932730324e-09,9.108905166320588e-10,7.717254458937643e-11,5.811750178929544e-12,3.939068782791375e-13,1.9972895151399215e-14,1.097032102290447e-15,5.719559876788773e-17,2.768988818013901e-18,1.2511707118773573e-19,5.300089625934702e-21,2.1131042283762174e-22,7.956737686120589e-24,2.8383638470439695e-25],[1.6404706935240748e-05,1.111872792015815e-05,3.768007287497761e-06,8.512891654866151e-07,1.4424598759656614e-07,1.955331352144257e-08,2.2087966768796834e-09,2.138672706047449e-10,1.81192812699133e-11,1.3645362702863317e-12,9.248508727643684e-14,5.698566914961244e-15,2.648649853557705e-16,1.3428909814891953e-17,6.501287147365272e-19,2.937613909948005e-20,1.2444038899979519e-21,4.961340859021319e-23,1.868156206236907e-24,6.664172234385877e-26],[3.5553676488090794e-06,2.409745306593641e-06,8.166345953835711e-07,1.8449863022245893e-07,3.1262217593759216e-08,4.237760454703168e-09,4.787092069840613e-10,4.6351134345092044e-11,3.926964785230809e-12,2.957339091855851e-13,2.0044154924435546e-14,1.2350419019374961e-15,6.975688406507628e-17,2.992842508610239e-18,1.4090142597857719e-19,6.3666467809212406e-21,2.6969779771234673e-22,1.0752639991992748e-23,4.0488270621331443e-25,1.4443161015774376e-26],[7.155102721662173e-07,4.849561818873008e-07,1.643459971851211e-07,3.7129961839244585e-08,6.291455632309301e-09,8.528403911577362e-10,9.633922249710856e-11,9.328068438035852e-12,7.902934154246533e-13,5.951582810881344e-14,4.0338440808304845e-15,2.4854958886965836e-16,1.4038426411285098e-17,7.319167804442221e-19,2.9159079601229217e-20,1.2812742931181881e-21,5.427611535713588e-23,2.163946215169385e-24,8.148179427101485e-26,2.906655820193114e-27],[1.3439527688894186e-07,9.108998553777174e-08,3.086933431495531e-08,6.9741717154577675e-09,1.1817327502214768e-09,1.6019018170726012e-10,1.8095528445126914e-11,1.7521039030975618e-12,1.4844189737199225e-13,1.1178939714929097e-14,7.576824725782445e-16,4.668541056110859e-17,2.6368569090108107e-18,1.3747693386659455e-19,6.655618628214518e-21,2.474784073683363e-22,1.0194757274126018e-23,4.06456988912253e-25,1.530483730066829e-26,5.459611538392561e-28],[2.3665921309083986e-08,1.6040209743113963e-08,5.435840110402335e-09,1.2280952339601396e-09,2.0809357979313032e-10,2.8208195425681745e-11,3.1864762076612893e-12,3.085313268137445e-13,2.6139417571048152e-14,1.9685208716904987e-15,1.334217554990901e-16,8.220923221390246e-18,4.6432917552252815e-19,2.420857617927696e-20,1.1720006116640427e-21,5.295697946040015e-23,1.84604960316064e-24,7.157378843806731e-26,2.695058067444268e-27,9.613934361140968e-29],[3.922237495754553e-09,2.6584011360698738e-09,9.009011575544635e-10,2.0353660067089787e-10,3.448809072888781e-11,4.6750447760389116e-12,5.281060600933197e-13,5.113399655306343e-14,4.332178848029763e-15,3.2624998085987306e-16,2.2112463120844497e-17,1.3624829089700115e-18,7.695492936115695e-20,4.01217362168546e-21,1.9423983896842877e-22,8.77674897117812e-24,3.717922400994788e-25,1.2198081835478933e-26,4.466615800547028e-28,1.593351610550493e-29],[6.139327120469247e-10,4.1610927970133705e-10,1.4101458454320925e-10,3.185879931695903e-11,5.3982878643694165e-12,7.317667329938723e-13,8.266240534196281e-14,8.0038073205919e-15,6.780992512875797e-16,5.1066651565939054e-17,3.461178592196907e-18,2.1326419634888105e-19,1.2045458374005388e-20,6.280100670677565e-22,3.0403613053651735e-23,1.3737906755169199e-24,5.819520580519133e-26,2.320197282257978e-27,7.189398414939741e-29,2.4940118403549485e-30],[9.103880865432058e-11,6.170398213138664e-11,2.0910760296344177e-11,4.724275279782367e-12,8.005009120734145e-13,1.0851217124839332e-13,1.2257836657281171e-14,1.1868679887344443e-15,1.00553931685415e-16,7.57256785524249e-18,5.132509954109771e-19,3.162450539488319e-20,1.7861960415962383e-21,9.312631043579023e-23,4.508488726660071e-24,2.0371657021252734e-25,8.629646379704027e-27,3.4405724320422574e-28,1.295522102707383e-29,3.803044163824256e-31]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.04178082887789562, "-10": 1.6833743149873845e-10, "-11": 1.0226121424283593e-11, "-12": 5.706717857645094e-13, "-13": 2.944672154420323e-14, "-14": 1.4128460857413446e-15, "-15": 6.333912243512822e-17, "-16": 2.664508723643417e-18, "-17": 1.0556062688232911e-19, "-18": 3.9357716791241395e-21, "-19": 1.2757643681494616e-22, "-2": 0.010445023908907714, "-3": 0.0020591677856460584, "-4": 0.00032010639128246304, "-5": 4.089851196468699e-05, "-6": 4.4252776264874104e-06, "-7": 4.146954332445448e-07, "-8": 3.424418227704866e-08, "-9": 2.526180294911039e-09, "0": 0.09946259003554078, "1": 0.20756563889319474, "10": 0.000324102143371539, "11": 8.184363645668292e-05, "12": 1.898598526320881e-05, "13": 4.0724564923605935e-06, "14": 8.122451412150979e-07, "15": 1.513690470898393e-07, "16": 2.647006130497685e-08, "17": 4.359257535752235e-09, "18": 6.756366941783114e-10, "19": 9.103880865432058e-11, "2": 0.22554256747256354, "3": 0.18483473216156643, "4": 0.1194425201804241, "5": 0.0634373285096115, "6": 0.028533212193558845, "7": 0.011115068987974753, "8": 0.003815421085960301, "9": 0.0011700186495547486} |
| Raw goal margin distribution | {"-1": 0.04948217445017616, "-10": 2.3051365973882996e-10, "-11": 1.4256708617609857e-11, "-12": 8.100670835387164e-13, "-13": 4.256226026409847e-14, "-14": 2.0794927967153217e-15, "-15": 9.493517765980869e-17, "-16": 4.0670474181201746e-18, "-17": 1.6408775186461562e-19, "-18": 6.2287016479303125e-21, "-19": 2.0495955163298626e-22, "-2": 0.012517782793828989, "-3": 0.0025027630893906024, "-4": 0.00039515891978199465, "-5": 5.1322323252981614e-05, "-6": 5.647981083400846e-06, "-7": 5.385052063437071e-07, "-8": 4.525454807286257e-08, "-9": 3.3980634286807833e-09, "0": 0.11399418797741127, "1": 0.19680271670042093, "10": 0.0003551602249433333, "11": 9.131028444340904e-05, "12": 2.156722023390064e-05, "13": 4.710539355375313e-06, "14": 9.567008052045268e-07, "15": 1.815593638040818e-07, "16": 3.233281269512432e-08, "17": 5.4226700626388945e-09, "18": 8.556719798144221e-10, "19": 1.170444188942836e-10, "2": 0.21630817979407396, "3": 0.1797786183243402, "4": 0.11799479557007851, "5": 0.06370450361087542, "6": 0.029142702803779758, "7": 0.011550459616871398, "8": 0.004035007603878779, "9": 0.0012594657799684119} |
| Research history json | {"away": [{"away": "Estrela", "away_goals": 1.0, "away_xg": 0.68, "date": "2026-10-31T00:00:00+00:00", "home": "Moreirense", "home_goals": 2.0, "home_xg": 0.44, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 3.0, "away_xg": 1.33, "date": "2026-10-25T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 2.01, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.49, "date": "2026-10-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 1.09, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.52, "date": "2026-09-20T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 1.07, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-09-14T00:00:00+00:00", "home": "Moreirense", "home_goals": 3.0, "home_xg": 1.99, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 4.0, "away_xg": 2.99, "date": "2026-09-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 0.38, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.85, "date": "2026-09-04T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.28, "date": "2026-08-30T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.78, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 0.0, "away_xg": 0.49, "date": "2026-08-16T00:00:00+00:00", "home": "Arouca", "home_goals": 4.0, "home_xg": 2.14, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 2.0, "away_xg": 1.5, "date": "2026-08-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 2.0, "home_xg": 0.2, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 82.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 6.5% |
| Raw p over 1 5 | 86.8% |
| Raw p under 3 5 | 52.4% |
| Raw p btts yes | 46.8% |
| P home draw | 94.5% |
| P draw away | 15.4% |
| P home away | 90.1% |
| Raw p home draw | 93.5% |
| Raw p draw away | 17.9% |
| Raw p home away | 88.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9817 |
| Totals anchor target over 2 5 | 0.6884 |
| Totals anchor reference over odds | 1.40 |
| Totals anchor reference under odds | 2.86 |
| Totals anchor reference last update utc | 2026-11-06T13:39:19Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6988 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.38, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 14.87, "draw": 8.51, "home": 1.15}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.4, "under": 2.86}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.12, "under": 5.89}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.15 |
| Reference draw odds | 8.51 |
| Reference away odds | 14.87 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:19Z |
| Market reference home last update utc | 2026-11-06T13:39:19Z |
| Market reference draw last update utc | 2026-11-06T13:39:19Z |
| Market reference away last update utc | 2026-11-06T13:39:19Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.85 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Home probability edge | -1.1% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | -0.0355 |
| Raw ev home | -0.0558 |
| Raw edge prob draw | 0.0208 |
| Raw ev draw | -0.0299 |
| Raw edge prob away | 0.0147 |
| Raw ev away | -0.0341 |
| Market p home draw | 92.6% |
| Market reference home draw last update utc | 2026-11-06T13:39:21Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 19.1% |
| Market reference draw away last update utc | 2026-11-06T13:39:21Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.3% |
| Market reference home away last update utc | 2026-11-06T13:39:21Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 5.00 |
| Market reference dc home draw odds | 1.03 |
| Market reference dc home away odds | 1.08 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-11-06T13:39:21Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.4% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 3 5 odds | 1.76 |
| Market reference under 3 5 opposite odds | 2.07 |
| Market reference under 3 5 last update utc | 2026-11-06T13:39:19Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,667.4354 |
| Elo away rating | 1,438.9672 |
| Elo rating diff | 288.4681 |
| Elo home expectancy | 0.8403 |
| Research p home | 0.8182 |
| Research p draw | 0.1196 |
| Research p away | 0.0621 |
| Research p over 1 5 | 0.8704 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.8699816510179548, 0.6904088575049193], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:17.190051+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T13:40:17.070085+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:17.407271+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Sporting+Lisbon%22+%22Moreirense+FC%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:17.493251+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Sporting+Lisbon_vs_Moreirense+FC&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 1.4889998489640717, "goals_for": 1.4469006738231538, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.6256113882270293, "results": "WWLDWLLWLD", "xg_against": 1.5345832438249536, "xg_for": 0.827627807906664, "xg_matches": 10}, "venue": {"goals_against": 1.4714941649527495, "goals_for": 1.3690993918184686, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 1.514509847632683, "results": "WDLWL", "xg_against": 1.781999249674747, "xg_for": 0.7490016998175378, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [2.8699816510179548, 0.6904088575049193], "h2h": [], "margin_distribution": {"-1": 0.046665753749870524, "-10": 2.3051365973882996e-10, "-11": 1.4256708617609857e-11, "-12": 8.100670835387164e-13, "-13": 4.256226026409847e-14, "-14": 2.0794927967153217e-15, "-15": 9.493517765980869e-17, "-16": 4.0670474181201746e-18, "-17": 1.6408775186461562e-19, "-18": 6.2287016479303125e-21, "-19": 2.0495955163298626e-22, "-2": 0.012517782793828989, "-3": 0.0025027630893906024, "-4": 0.00039515891978199465, "-5": 5.1322323252981614e-05, "-6": 5.647981083400846e-06, "-7": 5.385052063437071e-07, "-8": 4.525454807286257e-08, "-9": 3.3980634286807833e-09, "0": 0.11962702937802257, "1": 0.1939862960001153, "10": 0.0003551602249433333, "11": 9.131028444340904e-05, "12": 2.156722023390064e-05, "13": 4.710539355375313e-06, "14": 9.567008052045268e-07, "15": 1.815593638040818e-07, "16": 3.233281269512432e-08, "17": 5.4226700626388945e-09, "18": 8.556719798144221e-10, "19": 1.170444188942836e-10, "2": 0.21630817979407396, "3": 0.1797786183243402, "4": 0.11799479557007851, "5": 0.06370450361087542, "6": 0.029142702803779758, "7": 0.011550459616871398, "8": 0.004035007603878779, "9": 0.0012594657799684119}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:17.493724+00:00", "p_over_1_5": 0.870358489695804, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — CF Estrela vs Benfica

The model's most likely 1X2 outcome is **Benfica win** at **79.1%**. Expected goals are 0.72 for CF Estrela and 2.58 for Benfica (3.30 combined). The most likely exact score is 0-2 at 12.5%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 64.5%; Under 3.5 goals: 57.7%; Double Chance 1X: 20.9%; Double Chance X2: 92.0%; Double Chance 12 (either team wins): 87.1%; Under 4.5 goals: 76.0%; BTTS Yes (both teams score): 46.8%; BTTS No (at least one team does not score): 53.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CF Estrela win | 8.0% | 12.55 |
| Draw | 12.9% | 7.74 |
| Benfica win | 79.1% | 1.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CF Estrela expected goals | 0.72 |
| Benfica expected goals | 2.58 |
| Expected total goals | 3.30 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 64.5% |
| Under 2.5 | 35.5% |
| Over 3.5 | 42.3% |
| Under 3.5 | 57.7% |
| Over 4.5 | 24.0% |
| Under 4.5 | 76.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.48% |
| 2 | 0-3 | 10.75% |
| 3 | 0-1 | 10.02% |
| 4 | 1-2 | 8.98% |
| 5 | 1-3 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CF Estrela win | 8.0% | 7.8% | 10.27 | -18.2% |
| Draw | 12.9% | 12.6% | 6.61 | -14.5% |
| Benfica win | 79.1% | 79.7% | 1.23 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T20:30:00+00:00 |
| Fixture id | c02a3d0a40d536e48bb60dffe0e3cd1e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:39:19Z |
| Market best draw last update utc | 2026-11-06T13:39:19Z |
| Market best away last update utc | 2026-11-06T13:39:19Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Estrela |
| Matched away-team name | Benfica |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7193 |
| Dc lambda away | 2.5827 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 46.8% |
| P btts no | 53.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.85 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.26 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.82 |
| Fair Over 3.5 odds | 2.37 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.16 |
| Fair Under 4.5 odds | 1.32 |
| Score matrix json | [[0.03139786137123857,0.10015409876186127,0.12484564022630724,0.10748087743107076,0.0693985328146762,0.03584754030255007,0.015430755445202431,0.005693354489597551,0.0018380499760309009,0.0005274652865406499,0.00013623006388301744,3.198595723071045e-05,6.884258718201198e-06,1.3677064909056473e-06,2.5231551099691484e-07,4.344419630875167e-08,7.0127904498027735e-09,1.0654204231986442e-09,1.52871874034204e-10],[0.028144222613775773,0.06108450314658112,0.08979756687246912,0.07730763574228908,0.04991619555140837,0.025784015298384963,0.011098860092122798,0.0040950519343852815,0.001322051898155075,0.0003793892942931891,9.798602698020569e-05,2.3006499291429967e-05,4.951632123432266e-06,9.837485302360622e-07,1.8148266075319757e-07,3.124805252457469e-08,5.044080980619469e-09,7.663236099078029e-10,1.0995596086993726e-10],[0.008964044331655213,0.023151709943996093,0.029861919108950374,0.027802483041205438,0.017951579646360467,0.009272818152882544,0.00399153158061407,0.001472721431271533,0.000475455304319226,0.0001364414306468217,3.5239143290758225e-05,8.273927927634057e-06,1.7807771097403543e-06,3.537897850074523e-07,6.526740275286308e-08,1.1237873750030428e-08,1.8140248964492162e-09,2.755963102992982e-10,3.9543942949656174e-11],[0.002149185636653545,0.005550767112997726,0.007168067526896451,0.006163756461861566,0.00430400338326707,0.002223216089538852,0.0009569946358934115,0.00035309416484068,0.00011399337989718948,3.2712685495662134e-05,8.448804781233063e-06,1.9837259168813434e-06,4.269524385126156e-07,8.482331146530166e-08,1.5648267606484955e-08,2.6943504467956575e-09,4.3492380311116753e-10,6.607593734429863e-11,9.480907396221603e-12],[0.0003864605135167542,0.0009981233227675894,0.0012889417322184229,0.0011096630053339111,0.0007156418895976475,0.00039977246123779037,0.00017208408250672042,6.349239913801636e-05,2.0497968803278358e-05,5.882303054495811e-06,1.5192403013832754e-06,3.567080123000289e-07,7.677338607740491e-08,1.5252689180500254e-08,2.81382744780768e-09,4.844905156187772e-10,7.82067744286236e-11,1.1881589119932762e-11,1.7048300893419947e-12],[5.55937936529992e-05,0.0001435837817976238,0.0001854191002325618,0.00015962918328065088,0.00010306978672728764,5.317726666880969e-05,2.475494038650227e-05,9.133619639667842e-06,2.948709656221239e-06,8.461913462780452e-07,2.1854841276238314e-07,5.1313784815223005e-08,1.1044139399365193e-08,2.1941565187029212e-09,4.0477962699230267e-10,6.96957769554322e-11,1.1250337687250065e-11,1.709211137232073e-12,2.452461995090584e-13],[6.664479691615082e-06,1.721255440505329e-05,2.222769389782026e-05,1.913604703437263e-05,1.2355812678490391e-05,6.38234664334683e-06,2.7440610887912567e-06,1.0949211881355232e-06,3.534857819384586e-07,1.0143983117414437e-07,2.6199173734765193e-08,6.151400261250399e-09,1.3239507128771834e-09,2.6303136732118983e-10,4.852422233509865e-11,8.354998995211653e-12,1.3486693768099223e-12,2.0489702472662508e-13,2.9399654326085455e-14],[6.847931341377146e-07,1.7686360560723493e-06,2.283955068254296e-06,1.966280074371275e-06,1.269592838517818e-06,6.558032079457987e-07,2.822938153240876e-07,1.0403224271007716e-07,3.632161064145961e-08,1.0423214283860866e-08,2.6920352561387272e-09,6.320728487682387e-10,1.3603948095988767e-10,2.7027177325039596e-11,4.985993780768009e-12,8.584985193738206e-13,1.3857938986943004e-13,2.1053717954092065e-14,3.0208932069903997e-15],[6.156878720902009e-08,1.5901557938900164e-07,2.0534718673746567e-07,1.7678547499565798e-07,1.1414730583598345e-07,5.896234373297273e-08,2.5380639757722625e-08,9.364478610696596e-09,3.0196614358784854e-09,9.371365311440036e-10,2.420371022748209e-10,5.682878052714919e-11,1.2231118330050982e-11,2.4299754869492786e-12,4.482836857004291e-13,7.718639399786369e-14,1.2459477966540063e-14,1.89291015936725e-15,2.7160425794362933e-16],[4.920500473524223e-09,1.2708326233957081e-08,1.6411090349210865e-08,1.4128474067147119e-08,9.122509925535533e-09,4.712196770633902e-09,2.0283889874628825e-09,7.483974190007994e-10,2.4161359714547567e-10,6.925378260788798e-11,1.9343302513180064e-11,4.541685067538172e-12,9.77495680245096e-13,1.9420060189904913e-13,3.582627152088825e-14,6.168640076127305e-15,9.957458967982286e-16,1.5127901259261473e-16,2.1706272616444046e-17],[3.5391621967444587e-10,9.14070185200143e-10,1.1803984347487533e-09,1.0162169800649928e-09,6.561536258680034e-10,3.3893358539409e-10,1.458956799892291e-10,5.382988717754694e-11,1.737851086160459e-11,4.987112064852774e-12,1.2865117732396643e-12,3.2666921153728396e-13,7.030820904538264e-14,1.3968242306333179e-14,2.5768717328506957e-15,4.436910001375523e-16,7.162089007965525e-17,1.0881026542105774e-17,1.5612643447491788e-18],[2.3141897718187715e-11,5.976928311622664e-11,7.718397271758861e-11,6.644846465014303e-11,4.290461768387761e-11,2.2162212214132693e-11,9.53983659449663e-12,3.519832304917451e-12,1.136347244055698e-12,3.260976211266194e-13,8.42222244605584e-14,1.9751435286487758e-14,4.597317930141437e-15,9.13356373023457e-16,1.6849666321982846e-16,2.90120971373074e-17,4.6831516064269854e-18,7.114892997498839e-19,1.0208805861023847e-19],[1.3871036426381343e-12,3.582514767716311e-12,4.626334927826902e-12,3.982858643934182e-12,2.5716625403858076e-12,1.3283822124484875e-12,5.718088573176499e-13,2.109754468316233e-13,6.811158794002748e-14,1.9545985537947784e-14,5.048201135575492e-15,1.1852856925414012e-15,2.5480411279402785e-16,5.474572429087749e-17,1.0099531947239902e-17,1.7389578897024857e-18,2.8070371459623826e-19,4.264600126572532e-20,6.119062476748628e-21],[7.674617655423027e-14,1.9821468448340047e-13,2.5596754723729866e-13,2.2036505656964634e-13,1.4228588354578916e-13,7.349721583469792e-14,3.163724913555105e-14,1.1672926516401208e-14,3.768502794421702e-15,1.0814474210223893e-15,2.7930871473690935e-16,6.557991935914525e-17,1.4114604366245492e-17,2.8008509280689574e-18,5.587905893346211e-19,9.621369674269907e-20,1.553087756215435e-20,2.3595335214076128e-21,3.38557721825137e-22],[3.9429375740899974e-15,1.0183544800225153e-14,1.315067544813045e-14,1.1321549822758343e-14,7.31012777032424e-15,3.776017867168383e-15,1.6254060326935544e-15,5.997122283816605e-16,1.9361187662148684e-16,5.556080917905827e-17,1.4349859179352702e-17,3.3692561604583662e-18,7.25156697021364e-19,1.4406801981709504e-19,2.65463116631966e-20,4.943107488368784e-21,7.9791962867542e-22,1.212241937851971e-22,1.7393856245585972e-23],[1.8906878384192592e-16,4.883136987079246e-16,6.305913210537548e-16,5.428824616095313e-16,3.50529761451594e-16,1.810647753092258e-16,7.794025040369193e-17,2.875695076187473e-17,9.283931424814893e-18,2.6642102299025867e-18,6.88093679486995e-19,1.6156004317588015e-19,3.4772169790768245e-20,6.908241580167336e-21,1.2744375463450967e-21,2.191754648529293e-22,3.8261243289422507e-23,5.8128515758900585e-24,8.34057142645283e-25],[8.49945417084948e-18,2.1951798804799083e-17,2.834778922740028e-17,2.4404899152818086e-17,1.575781883416316e-17,8.139639597949649e-18,3.503749127220092e-18,1.2927484914605434e-18,4.1735260611025094e-19,1.1976769665741101e-19,3.09327672988079e-20,7.262818086151757e-21,1.5631584312972905e-21,3.105551404026577e-22,5.729144335019524e-23,9.864556887063678e-24,1.5904581158352363e-24,2.61312653349135e-25,3.749445210220504e-26],[3.5961127814119174e-19,9.287789859219991e-19,1.1993928682509342e-18,1.0325694804440194e-18,6.667121508938497e-19,3.443875501401497e-19,1.4824336676195912e-19,5.469609318250615e-20,1.7658157936024785e-20,5.06736239871901e-21,1.3087630995081418e-21,3.072892967439769e-22,6.613711776268297e-23,1.3139565050723162e-23,2.4239967362113863e-24,4.173686732284504e-25,6.737192293447293e-26,1.0223383665957332e-26,1.5863874988492405e-27],[1.43698418028864e-20,3.7113427494630106e-20,4.7926989012589294e-20,4.126083075359908e-20,2.664140064218231e-20,1.3761511151645658e-20,5.923712236467291e-21,2.1856216810863056e-21,7.056089491482328e-22,2.0248863273664455e-22,5.2297355062382975e-23,1.2279088144163975e-23,2.6427978690242328e-24,5.250488030119408e-25,9.686139380866286e-26,1.6677791193797467e-26,2.6921399115422686e-27,4.090042137143839e-28,5.861650427983085e-29]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2224838116600371, "-10": 0.0001611050484888725, "-11": 3.730752335552788e-05, "-12": 7.936048947022139e-06, "-13": 1.5608740760473059e-06, "-14": 2.854453691853724e-07, "-15": 4.8773354507066655e-08, "-16": 7.818658002660233e-09, "-17": 1.1753763840685815e-09, "-18": 1.52871874034204e-10, "-2": 0.22250965356228825, "-3": 0.16769343106973617, "-4": 0.09954854486233998, "-5": 0.04853922234721485, "-6": 0.020035547274921215, "-7": 0.007160664643427935, "-8": 0.002254741156469659, "-9": 0.0006341678598513027, "0": 0.12927971042845132, "1": 0.059683407128352926, "10": 4.1853969752676553e-10, "11": 2.6992060402794118e-11, "12": 1.599027993161371e-12, "13": 8.758539804832405e-14, "14": 4.460658272906408e-15, "15": 2.1226123634572952e-16, "16": 9.47616014578407e-18, "17": 3.9672470563582185e-19, "18": 1.43698418028864e-20, "2": 0.015976420122785346, "3": 0.0033531947452453696, "4": 0.000554357278273896, "5": 7.527655979945018e-05, "6": 8.653270308008215e-06, "7": 8.612802861022547e-07, "8": 7.552660715671775e-08, "9": 5.915883631238161e-09} |
| Raw goal margin distribution | {"-1": 0.2187828017403119, "-10": 0.00015842507200821863, "-11": 3.6686914094166544e-05, "-12": 7.804033068396173e-06, "-13": 1.5349089939328364e-06, "-14": 2.806969961014513e-07, "-15": 4.7962011571587133e-08, "-16": 7.688594918021064e-09, "-17": 1.1558240417008784e-09, "-18": 1.503288561039282e-10, "-2": 0.2188082137634817, "-3": 0.16490385709025854, "-4": 0.09789255852661187, "-5": 0.04773177419149333, "-6": 0.019702256692301596, "-7": 0.007041547253810177, "-8": 0.0022172336213180316, "-9": 0.0006236185011246239, "0": 0.1374843236007099, "1": 0.06339601782156008, "10": 4.445749899360587e-10, "11": 2.8671103488715757e-11, "12": 1.698495646095151e-12, "13": 9.303365412163622e-14, "14": 4.73813384609412e-15, "15": 2.2546496203310174e-16, "16": 1.0065625378761164e-17, "17": 4.214029948835433e-19, "18": 1.526371886024607e-20, "2": 0.016970234501704165, "3": 0.0035617804689261814, "4": 0.000588841113198916, "5": 7.995914369179171e-05, "6": 9.191547618612048e-06, "7": 9.148562891135293e-07, "8": 8.022474526315436e-08, "9": 6.283881603972365e-09} |
| Research history json | {"away": [{"away": "Alverca", "away_goals": 0.0, "away_xg": 0.56, "date": "2026-11-02T00:00:00+00:00", "home": "Benfica", "home_goals": 1.0, "home_xg": 1.6, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-10-26T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.56, "source": "pipeline training history"}, {"away": "Guimaraes", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-10-11T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 2.76, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-09-20T00:00:00+00:00", "home": "Porto", "home_goals": 3.0, "home_xg": 1.3, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.1, "date": "2026-09-13T00:00:00+00:00", "home": "Benfica", "home_goals": 3.0, "home_xg": 2.91, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 4.0, "away_xg": 2.99, "date": "2026-09-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 0.38, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 3.0, "away_xg": 1.31, "date": "2026-09-05T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 0.13, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 1.0, "away_xg": 0.36, "date": "2026-08-31T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 2.03, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 7.0, "away_xg": 3.04, "date": "2026-08-17T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.12, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.18, "date": "2026-08-09T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 3.12, "source": "pipeline training history"}], "h2h": [{"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2026-01-25T00:00:00+00:00", "home": "Benfica", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 1.0, "away_xg": null, "date": "2025-08-16T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 3.0, "away_xg": null, "date": "2025-02-02T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2024-08-24T00:00:00+00:00", "home": "Benfica", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 4.0, "away_xg": null, "date": "2024-01-29T00:00:00+00:00", "home": "Estrela", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2023-08-19T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Estrela", "away_goals": 1.0, "away_xg": 0.68, "date": "2026-10-31T00:00:00+00:00", "home": "Moreirense", "home_goals": 2.0, "home_xg": 0.44, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 2.0, "away_xg": 0.79, "date": "2026-10-24T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": 1.69, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": 1.45, "date": "2026-10-11T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.74, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 2.54, "date": "2026-09-20T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 1.87, "date": "2026-09-14T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-09-10T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": 0.57, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-09-05T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 2.1, "date": "2026-08-30T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 2.0, "away_xg": 1.29, "date": "2026-08-15T00:00:00+00:00", "home": "Alverca", "home_goals": 2.0, "home_xg": 1.75, "source": "pipeline training history"}, {"away": "Sp Lisbon", "away_goals": 2.0, "away_xg": 2.62, "date": "2026-08-08T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": 1.01, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 8.5% |
| Unadjusted draw probability | 13.7% |
| Unadjusted away-win probability | 77.8% |
| Raw p over 1 5 | 83.8% |
| Raw p under 3 5 | 58.0% |
| Raw p btts yes | 47.1% |
| P home draw | 20.9% |
| P draw away | 92.0% |
| P home away | 87.1% |
| Raw p home draw | 22.2% |
| Raw p draw away | 91.5% |
| Raw p home away | 86.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6454 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.75, "market_key": "spreads", "opposite_price": 1.91, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.23, "draw": 6.61, "home": 10.27}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.27 |
| Reference draw odds | 6.61 |
| Reference away odds | 1.23 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:19Z |
| Market reference home last update utc | 2026-11-06T13:39:19Z |
| Market reference draw last update utc | 2026-11-06T13:39:19Z |
| Market reference away last update utc | 2026-11-06T13:39:19Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0071 |
| Raw ev home | -0.1311 |
| Raw edge prob draw | 0.0117 |
| Raw ev draw | -0.0912 |
| Raw edge prob away | -0.0188 |
| Raw ev away | -0.0432 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,369.8605 |
| Elo away rating | 1,697.2970 |
| Elo rating diff | -267.4365 |
| Elo home expectancy | 0.1766 |
| Research p home | 0.1115 |
| Research p draw | 0.1735 |
| Research p away | 0.7150 |
| Research p over 1 5 | 0.8149 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.7192687442644643, 2.5827304158056434], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:17.507420+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T13:40:17.070085+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:17.821845+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22CF+Estrela%22+%22Benfica%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:18.065688+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=CF+Estrela_vs_Benfica&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.7555428435148334, "goals_for": 2.3450699791344993, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 2.5592486517835913, "results": "WWWLWWWWWD", "xg_against": 0.7758083739925704, "xg_for": 2.1102298851170693, "xg_matches": 10}, "venue": {"goals_against": 0.9350525536533023, "goals_for": 3.0813340821541915, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 2.323846319754449, "results": "WLWWW", "xg_against": 0.8114905046532553, "xg_for": 1.9203973892492832, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.88202684170377, "goals_for": 1.2020655108450724, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 0.7358705894281937, "results": "LLLLDWDWDD", "xg_against": 1.1766693126000094, "xg_for": 1.2226669902694305, "xg_matches": 10}, "venue": {"goals_against": 1.8037913442624962, "goals_for": 1.0314331330207962, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.9081338779854057, "results": "LLWDD", "xg_against": 1.5954491586464379, "xg_for": 1.0494473812745448, "xg_matches": 5}}}, "goal_rates": [0.7896688104976095, 2.3077947018530494], "h2h": [{"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2026-01-25T00:00:00+00:00", "home": "Benfica", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 1.0, "away_xg": null, "date": "2025-08-16T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 3.0, "away_xg": null, "date": "2025-02-02T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2024-08-24T00:00:00+00:00", "home": "Benfica", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 4.0, "away_xg": null, "date": "2024-01-29T00:00:00+00:00", "home": "Estrela", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": null, "date": "2023-08-19T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.2328523771126372, "-10": 6.287231466796535e-05, "-11": 1.3012978372412105e-05, "-12": 2.4739898059208698e-06, "-13": 4.348720190452178e-07, "-14": 7.10732136126902e-08, "-15": 1.0852913547544218e-08, "-16": 1.5547950906251222e-09, "-17": 2.089082952990316e-10, "-18": 2.4321858868110772e-11, "-2": 0.21215446451658845, "-3": 0.14318224511109487, "-4": 0.07606000522512821, "-5": 0.033172395082679815, "-6": 0.012244249158041565, "-7": 0.00391250436925367, "-8": 0.0011013259467260114, "-9": 0.00027688731988116644, "0": 0.1734920963410305, "1": 0.07967617722167103, "10": 1.383367537044862e-09, "11": 9.797215292960686e-11, "12": 6.373407140658621e-12, "13": 3.8333902565306283e-13, "14": 2.143755915044884e-14, "15": 1.1201173893655415e-15, "16": 5.49083217314145e-17, "17": 2.5244600795061778e-18, "18": 1.005674409816105e-19, "2": 0.024839783227103278, "3": 0.00573630991820784, "4": 0.0010426717408656308, "5": 0.00015560225786373475, "6": 1.965255574672388e-05, "7": 2.148767996422095e-06, "8": 2.069656995118465e-07, "9": 1.780464771940198e-08}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:18.066133+00:00", "p_over_1_5": 0.8149437388112665, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Estoril vs CS Maritimo

The model's most likely 1X2 outcome is **Estoril win** at **49.9%**. Expected goals are 2.02 for Estoril and 1.15 for CS Maritimo (3.17 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 51.3%; Under 3.5 goals: 70.4%; Double Chance 1X: 74.6%; Double Chance X2: 50.1%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 52.8%; BTTS No (at least one team does not score): 47.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Estoril win | 49.9% | 2.00 |
| Draw | 24.7% | 4.05 |
| CS Maritimo win | 25.4% | 3.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Estoril expected goals | 2.02 |
| CS Maritimo expected goals | 1.15 |
| Expected total goals | 3.17 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 51.3% |
| Under 2.5 | 48.7% |
| Over 3.5 | 29.6% |
| Under 3.5 | 70.4% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.70% |
| 2 | 1-0 | 10.40% |
| 3 | 2-1 | 8.78% |
| 4 | 2-0 | 8.73% |
| 5 | 0-1 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Estoril win | 49.9% | 46.4% | 2.08 | +3.7% |
| Draw | 24.7% | 26.5% | 3.55 | -12.4% |
| CS Maritimo win | 25.4% | 27.0% | 3.49 | -11.2% |
| Over 2.5 | 51.3% | 51.3% | 1.87 | -4.2% |
| Under 2.5 | 48.7% | 48.7% | 1.96 | -4.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T15:30:00+00:00 |
| Fixture id | 88fe8a3db780908444b4b21229766ad5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:39:19Z |
| Market best draw last update utc | 2026-11-06T13:39:19Z |
| Market best away last update utc | 2026-11-06T13:39:19Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Estoril |
| Matched away-team name | Maritimo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 2.0187 |
| Dc lambda away | 1.1530 |
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
| P btts yes | 52.8% |
| P btts no | 47.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.82 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.01 |
| Fair Under 4.5 odds | 1.17 |
| Score matrix json | [[0.06320909264851557,0.07935422920953938,0.036711376515239424,0.012320406204070265,0.0031010634190660573,0.0006244335889440178,0.00010478053662823234,1.5070518375815771e-05,1.8966352434940602e-06,2.1217143783846288e-07,2.1361538688038955e-08,1.955174207532727e-09,1.640400246673187e-10,1.2704339359561799e-11,9.136285513128744e-13,6.13230880467705e-14,3.8587766899922074e-15],[0.10397475955538334,0.11695339262789144,0.06471527490430648,0.021718566562007057,0.005466593484372364,0.0011007593613718044,0.00018470844398062706,2.656649878645824e-05,3.343412392203889e-06,3.74018471381978e-07,3.7656388286109546e-08,3.446605612125867e-09,2.891718126463586e-10,2.239536874326546e-11,1.6105558677183347e-12,1.0810110863809054e-13,6.802299940551461e-15],[0.08725172867453222,0.08784552702604248,0.05462368208911287,0.019142880749844833,0.00481828977434818,0.0009702162032128389,0.00016280318070327487,2.341587861050212e-05,2.946904646712462e-06,3.2966222588691907e-07,3.31905767525126e-08,3.0378597978049187e-09,2.5487784886269954e-10,1.9739418436163814e-11,1.4195540404875515e-12,9.528099498081027e-14,5.995589820114709e-15],[0.05126948049927031,0.051618398892816594,0.025984845938665707,0.010771847747903072,0.002831247212846147,0.0005701030967105181,9.566382953191937e-05,1.375926815470462e-05,1.7316134890738731e-06,1.9371090198684883e-07,1.950292164319233e-08,1.7850591160669806e-09,1.4976728943338838e-10,1.1598964787906115e-11,8.341358882174274e-13,5.59875109448187e-14,3.5230336410941336e-15],[0.022594620793733658,0.022748390223682323,0.011451603071657766,0.0038431792790998886,0.0011948736051795971,0.00025124622208120005,4.215934959553298e-05,6.0637526131997975e-06,7.631274935094196e-07,8.536900181906954e-08,8.594998712813236e-09,7.866811488855413e-10,6.600291399677682e-11,5.1117001465684435e-12,3.676063010816975e-13,2.467387160283779e-14,1.5526119708823972e-15],[0.007966016177127253,0.008020229513022602,0.004037405900972929,0.0013549609258058717,0.00034104555415488837,8.48269208859738e-05,1.4863806034236285e-05,2.13785182994723e-06,2.6905014312931375e-07,3.0097909397289716e-08,3.030274303503553e-09,2.7735427894418446e-10,2.3270152902131533e-11,1.8021938244469732e-12,1.2960419951118886e-13,8.699082057401823e-15,5.473927705961215e-16],[0.0023404322026304354,0.0023563601940279183,0.0011861982922980754,0.00039809035200900433,0.00010019989663087678,2.017636294709559e-05,4.1819895774165e-06,6.281053359679832e-07,7.904749439377328e-08,8.842828688639854e-09,8.903009239532874e-10,8.148726685267743e-11,6.836819559651357e-12,5.294883123923663e-13,3.8077984702450676e-14,2.555808490437944e-15,1.6082514010814714e-16],[0.0005893918910366197,0.0005934030428912329,0.00029872074647417933,0.0001002512378313357,2.5233376335606525e-05,5.081020803877404e-06,8.526000136376668e-07,1.514741799636878e-07,1.990655920307784e-08,2.2268927581207514e-09,2.2420480480943714e-10,2.0520967986906917e-11,1.7217187510965678e-12,1.3334123388491224e-13,9.589192707832823e-15,6.436301797649342e-16,4.050065340411732e-17],[0.00012987342710702466,0.00013075729070597758,6.582358475332311e-05,2.2090517407658094e-05,5.560214030808409e-06,1.1196108990251576e-06,1.878717495211347e-07,2.7021475023559282e-08,4.200590830390911e-09,4.906993100775239e-10,4.940388019802934e-11,4.5218274641100445e-12,3.79383425730648e-13,2.938194990917667e-14,2.1129936449678115e-15,1.4182491905099654e-16,8.924382465485419e-18],[2.54380562218804e-05,2.5611176870372338e-05,1.2892737852377624e-05,4.326826790543974e-06,1.0890683357792308e-06,2.192960148234322e-07,3.6798075120350495e-08,5.292643893049766e-09,6.66082923526406e-10,9.204010492166946e-11,9.676642174236881e-12,8.856815733589937e-13,7.43090956199447e-14,5.75498552973569e-15,4.1386796617658444e-16,2.777897176386861e-17,1.748001480822574e-18],[4.484252451680254e-06,4.5147703767003544e-06,2.272747996903417e-06,7.627384527440267e-07,1.9198233198984362e-07,3.8657776503765946e-08,6.486810829265006e-09,9.329939027678012e-10,1.174179330681912e-10,1.313522553825545e-11,1.6335365231692566e-12,1.5612905845089403e-13,1.3099300564060454e-14,1.0144960662876464e-15,7.295716409349458e-17,4.896911979074014e-18,3.0813989314077846e-19],[7.186269506459938e-07,7.235176216404469e-07,3.6422078823628885e-07,1.22233173609684e-07,3.076626021892969e-08,6.195128473921285e-09,1.039548316220559e-09,1.4951757746513628e-10,1.8816891355064655e-11,2.1049945729676686e-12,2.1193202754649654e-13,2.3960463925331934e-14,2.099237391601104e-15,1.6257876255059495e-16,1.1691800344702317e-17,7.847579860909044e-19,4.9381169808396297e-20],[1.0556705005189521e-07,1.0628549473198226e-07,5.350441442130374e-08,1.795618094319441e-08,4.519595778479715e-09,9.100708470458412e-10,1.5271073403407563e-10,2.196428838316093e-11,2.764221004674978e-12,3.092259025961768e-13,3.113303632641232e-14,2.849537690918503e-15,2.9531429810029478e-16,2.3882990121822708e-17,1.7175376891674277e-18,1.1528176826907438e-19,7.25414545070704e-21],[1.4314993823632483e-08,1.4412415615309072e-08,7.255250209241641e-09,2.434875457555145e-09,6.128615474473141e-10,1.234064847708162e-10,2.070772284936961e-11,2.9783786928863482e-12,3.7483103477482366e-13,4.193133069073557e-14,4.221669758740379e-15,3.8640005973127056e-16,3.241914458853154e-17,3.1013409518277776e-18,2.328997674956471e-19,1.5632318985308278e-20,9.836691209194084e-22],[1.8024750450804864e-09,1.814741927658821e-09,9.135461467250986e-10,3.0658778510100726e-10,7.716857296434941e-11,1.5538749924801373e-11,2.6074166804607333e-12,3.7502309360862984e-13,4.7196917765199126e-14,5.27979111330763e-15,5.315723137887856e-16,4.8653633642050096e-17,4.0820624740483604e-18,3.161417895566479e-19,2.8083109054286683e-20,1.968346281871193e-21,1.2385887586946779e-22],[2.1182837424090884e-10,2.1326998853713156e-10,1.0736070692517313e-10,3.603045282503066e-11,9.068915210861716e-12,1.826126882194777e-12,3.0642578819501006e-13,4.407302749557064e-14,5.5466212343248115e-15,6.204854657577867e-16,6.247082273271008e-17,5.717815702046544e-18,4.797273947217809e-19,3.715324741619705e-20,2.671864049969751e-21,2.2152074957306965e-22,1.455599864327904e-23],[2.333835716062379e-11,2.349718814563075e-11,1.1828550033562287e-11,3.969683380250278e-12,9.991748414676237e-13,2.0119496054295548e-13,3.37607013873767e-14,4.855780348254101e-15,6.11103341869358e-16,6.836247251920133e-17,6.882771858485224e-18,6.299648265308453e-19,5.285434171826003e-20,4.093388154365459e-21,2.943747158815813e-22,1.9758540377058905e-23,1.5357700395226188e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.16631039061708167, "-10": 2.5074997580023708e-08, "-11": 2.26494479576784e-09, "-12": 1.879124875739874e-10, "-13": 1.4413699255902039e-11, "-14": 1.0277252497710796e-12, "-15": 6.812538798732196e-14, "-16": 3.8587766899922074e-15, "-2": 0.06386271447442066, "-3": 0.018859221595574367, "-4": 0.004379179365905852, "-5": 0.0008343780075391298, "-6": 0.00013449653028868352, "-7": 1.8763906406072635e-05, "-8": 2.305697194582978e-06, "-9": 2.530206971124659e-07, "0": 0.24684205339753462, "1": 0.22201041401721505, "10": 5.2637883916601066e-06, "11": 8.3248355348249e-07, "12": 1.209300414415959e-07, "13": 1.624106614159673e-08, "14": 2.0275735836511803e-09, "15": 2.353255623865396e-10, "16": 2.333835716062379e-11, "2": 0.15178216576619508, "3": 0.07847975771336861, "4": 0.0319070859860664, "5": 0.010644316423042071, "6": 0.0030041839902629364, "7": 0.0007338363554671459, "8": 0.00015788423080227417, "9": 3.0335632279339176e-05} |
| Raw goal margin distribution | {"-1": 0.13608344938456257, "-10": 5.9164819298638525e-08, "-11": 6.095463357346831e-09, "-12": 5.771531695939246e-10, "-13": 5.054823069023316e-11, "-14": 4.117634618083598e-12, "-15": 3.1337030790888177e-13, "-16": 2.2219776697042224e-14, "-17": 1.3255037399085113e-15, "-2": 0.05686342661188424, "-3": 0.018599194072729947, "-4": 0.00483680170289379, "-5": 0.0010388169120738933, "-6": 0.00018952448400137828, "-7": 3.0007472277375962e-05, "-8": 4.192528871999465e-06, "-9": 5.238243106328392e-07, "0": 0.20359830200487813, "1": 0.2346037285932003, "10": 1.6020229419249703e-05, "11": 2.889830912848556e-06, "12": 4.790902267460177e-07, "13": 7.346706736726462e-08, "14": 1.0478402355117912e-08, "15": 1.3962578487040971e-09, "16": 1.7334367195702863e-10, "17": 1.8105468962020546e-11, "2": 0.1743227484766907, "3": 0.09983335877835492, "4": 0.04545695685318598, "5": 0.017093917584323704, "6": 0.005460450017664053, "7": 0.0015137461293032895, "8": 0.0003703055430999172, "9": 8.100844951902692e-05} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Estoril", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-10-31T00:00:00+00:00", "home": "Porto", "home_goals": 4.0, "home_xg": 3.1, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 3.0, "away_xg": 1.33, "date": "2026-10-25T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 2.01, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 1.0, "away_xg": 1.36, "date": "2026-10-10T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 0.73, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 2.0, "away_xg": 2.17, "date": "2026-09-20T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.75, "date": "2026-09-14T00:00:00+00:00", "home": "Sp Braga", "home_goals": 1.0, "home_xg": 1.79, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 1.08, "date": "2026-09-07T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 1.0, "away_xg": 0.36, "date": "2026-08-31T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 2.03, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 2.0, "away_xg": 0.71, "date": "2026-08-22T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 1.16, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-08-16T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": 1.47, "date": "2026-08-07T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 1.22, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 57.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 21.8% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 60.9% |
| Raw p btts yes | 58.9% |
| P home draw | 74.6% |
| P draw away | 50.1% |
| P home away | 75.3% |
| Raw p home draw | 78.2% |
| Raw p draw away | 42.1% |
| Raw p home away | 79.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.8732 |
| Totals anchor target over 2 5 | 0.5125 |
| Totals anchor reference over odds | 1.87 |
| Totals anchor reference under odds | 1.96 |
| Totals anchor reference last update utc | 2026-11-06T13:39:19Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5971 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.49, "draw": 3.55, "home": 2.08}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.87, "under": 1.96}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.49 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:19Z |
| Market reference home last update utc | 2026-11-06T13:39:19Z |
| Market reference draw last update utc | 2026-11-06T13:39:19Z |
| Market reference away last update utc | 2026-11-06T13:39:19Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market best over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market best under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Home probability edge | +3.4% |
| Draw probability edge | -1.9% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1143 |
| Raw ev home | 0.2038 |
| Raw edge prob draw | -0.0618 |
| Raw ev draw | -0.2772 |
| Raw edge prob away | -0.0525 |
| Raw ev away | -0.2404 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,378.3893 |
| Elo away rating | 1,388.6236 |
| Elo rating diff | 49.7657 |
| Elo home expectancy | 0.5711 |
| Research p home | 0.5739 |
| Research p draw | 0.2134 |
| Research p away | 0.2128 |
| Research p over 1 5 | 0.8251 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.0187299121441877, 1.1529691825013815], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:17.507420+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T13:40:17.070085+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:17.508964+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Estoril%22+%22CS+Maritimo%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:17.595243+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Estoril_vs_CS+Maritimo&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.1741572673293668, "goals_for": 0.5196294860897706, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 0.13586574280159558, "results": "LLLLLDLLLD", "xg_against": 1.7383780696529123, "xg_for": 1.0563300250269338, "xg_matches": 10}, "venue": {"goals_against": 1.7177832069357093, "goals_for": 0.6329817884866369, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 0.34490701073453883, "results": "LLDLD", "xg_against": 1.3851867116529304, "xg_for": 1.284754675915346, "xg_matches": 5}}}, "goal_rates": [2.0187299121441877, 1.1529691825013815], "h2h": [], "margin_distribution": {"-1": 0.13120350911025505, "-10": 5.9164819298638525e-08, "-11": 6.095463357346831e-09, "-12": 5.771531695939246e-10, "-13": 5.054823069023316e-11, "-14": 4.117634618083598e-12, "-15": 3.1337030790888177e-13, "-16": 2.2219776697042224e-14, "-17": 1.3255037399085113e-15, "-2": 0.05686342661188424, "-3": 0.018599194072729947, "-4": 0.00483680170289379, "-5": 0.0010388169120738933, "-6": 0.00018952448400137828, "-7": 3.0007472277375962e-05, "-8": 4.192528871999465e-06, "-9": 5.238243106328392e-07, "0": 0.21335818255349318, "1": 0.22972378831889279, "10": 1.6020229419249703e-05, "11": 2.889830912848556e-06, "12": 4.790902267460177e-07, "13": 7.346706736726462e-08, "14": 1.0478402355117912e-08, "15": 1.3962578487040971e-09, "16": 1.7334367195702863e-10, "17": 1.8105468962020546e-11, "2": 0.1743227484766907, "3": 0.09983335877835492, "4": 0.04545695685318598, "5": 0.017093917584323704, "6": 0.005460450017664053, "7": 0.0015137461293032895, "8": 0.0003703055430999172, "9": 8.100844951902692e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:17.595704+00:00", "p_over_1_5": 0.8250711020531016, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Rio Ave FC vs Braga

The model's most likely 1X2 outcome is **Braga win** at **62.9%**. Expected goals are 0.96 for Rio Ave FC and 1.97 for Braga (2.93 combined). The most likely exact score is 0-1 at 12.6%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 52.9%; Under 3.5 goals: 69.3%; Double Chance 1X: 37.1%; Double Chance X2: 84.0%; Double Chance 12 (either team wins): 78.9%; Under 4.5 goals: 84.9%; BTTS Yes (both teams score): 50.0%; BTTS No (at least one team does not score): 50.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rio Ave FC win | 16.0% | 6.26 |
| Draw | 21.1% | 4.74 |
| Braga win | 62.9% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rio Ave FC expected goals | 0.96 |
| Braga expected goals | 1.97 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 76.4% |
| Under 1.5 | 23.6% |
| Over 2.5 | 52.9% |
| Under 2.5 | 47.1% |
| Over 3.5 | 30.7% |
| Under 3.5 | 69.3% |
| Over 4.5 | 15.1% |
| Under 4.5 | 84.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.61% |
| 2 | 0-2 | 11.26% |
| 3 | 1-2 | 10.30% |
| 4 | 1-1 | 10.01% |
| 5 | 0-3 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rio Ave FC win | 16.0% | 14.9% | 5.98 | -4.5% |
| Draw | 21.1% | 21.4% | 4.26 | -10.1% |
| Braga win | 62.9% | 63.6% | 1.53 | -3.7% |
| Over 2.5 | 52.9% | 52.9% | 1.82 | -3.7% |
| Under 2.5 | 47.1% | 47.1% | 2.03 | -4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T20:30:00+00:00 |
| Fixture id | 3642cddab8c2e0da43a419cdd01d1db0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:39:19Z |
| Market best draw last update utc | 2026-11-06T13:39:19Z |
| Market best away last update utc | 2026-11-06T13:39:19Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Rio Ave |
| Matched away-team name | Sp Braga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 0.9637 |
| Dc lambda away | 1.9671 |
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
| P btts yes | 50.0% |
| P btts no | 50.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.72 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.24 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.25 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.61 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.056420446388834526,0.12613685549134632,0.112626085348774,0.07010848159489667,0.032731310710486336,0.012224925446445635,0.0038049398503330295,0.0010150854026933945,0.0002369547518174687,4.916722979161112e-05,9.181815600469353e-06,1.5587939379790032e-06,2.425829588514316e-07,3.484735049106797e-08,4.648304335603014e-09,5.787035178412158e-10,6.754434064469554e-11],[0.05336258776543547,0.10013120804523835,0.10304185121831366,0.06414240277704782,0.029945947583687762,0.011184610963851994,0.0034811477708606743,0.0009287038496837302,0.00021679041943646705,4.498320581164532e-05,8.400463126172692e-06,1.4261439749045681e-06,2.2193967833171804e-07,3.188191699581383e-08,4.252743778525212e-09,5.294571111146092e-10,6.179646462714933e-11],[0.022326110758519587,0.04169326458481053,0.045020814651517964,0.029342012124767752,0.013698806390873829,0.005116412486960785,0.0015924548454435584,0.0004248365891819916,9.91710138728151e-05,2.05776165717403e-05,3.8428010213241376e-06,6.523911171330195e-07,1.0152654797189142e-07,1.4584417710443997e-08,1.9454222809013484e-09,2.4220073307619226e-10,2.826886015885936e-11],[0.006808735815031472,0.012715086245635297,0.011872498994381727,0.008546697442207051,0.004177689285229961,0.0015603389825140364,0.00048564680419559646,0.00012956130745680499,3.0243925656023777e-05,6.275502099555276e-06,1.1719290129358881e-06,1.9895801882721295e-07,3.096228675157592e-08,4.447771861410574e-09,5.932903631358472e-10,7.386332637866462e-11,8.621080612542152e-12],[0.0015573318131955154,0.0029082650371214393,0.0027155438084796603,0.0016903957242886127,0.0009126533188125729,0.0003568893848801795,0.0001110798301912144,2.9633980718747436e-05,6.9175583925675005e-06,1.4353676407648235e-06,2.680501027257791e-07,4.550678138017003e-08,7.081865925985901e-09,1.0173190450889165e-09,1.3570066192522757e-10,1.6894429615552095e-11,1.971861365570242e-12],[0.000284961254750005,0.0005321556055694925,0.0004968913910550298,0.0003093093472667997,0.00014440621335299738,6.237252400965853e-05,2.0325435800194505e-05,5.422438723270053e-06,1.2657778532807663e-06,2.6264419725724026e-07,4.90479247655465e-08,8.326850714696979e-09,1.2958429174443965e-09,1.8614948279697125e-10,2.4830566334654545e-11,3.091350103260854e-12,3.6081205313142234e-13],[4.3451945618702985e-05,8.114505410280918e-05,7.576783630275073e-05,4.716463277993501e-05,2.2019593278117938e-05,8.224170689865035e-06,2.9601812825002527e-06,8.268335031405717e-07,1.9301048661638622e-07,4.0048958186619235e-08,7.479008897165603e-09,1.2697089811297047e-09,1.9759491874982472e-10,2.838476132672748e-11,3.786256552672578e-12,4.71380492386957e-13,5.501795577435026e-14],[5.679182835997776e-06,1.0605683863519033e-05,9.902879821014454e-06,6.164432205186497e-06,2.8779677047858776e-06,1.0749016725753617e-06,3.3455714941482584e-07,1.0321664020820142e-07,2.5226530760628305e-08,5.234411317939731e-09,9.775087940084143e-10,1.6595135959206067e-10,2.5825717469400533e-11,3.709897152712491e-12,4.94864911581008e-13,6.160957728060638e-14,7.190863968376232e-15],[6.494870959692524e-07,1.2128954133371793e-06,1.1325207943500175e-06,7.049815592954929e-07,3.2913236654869443e-07,1.2292873568857523e-07,3.8260883243955415e-08,1.0207274123320532e-08,2.755479817780125e-09,5.986217919324959e-10,1.1179061605143571e-10,1.8978657621375942e-11,2.953500657560078e-12,4.2427412492989455e-13,5.659412341553209e-14,7.0458420845759026e-15,8.223671417527225e-16],[6.602412902030938e-08,1.2329785111251312e-07,1.1512730508180674e-07,7.166546297336762e-08,3.345821336348693e-08,1.2496418721443292e-08,3.8894406176924205e-09,1.0376285962357052e-09,2.4221708424468893e-10,5.81218869858421e-11,1.1364164281701571e-11,1.9292905851440104e-12,3.002404661871017e-13,4.312992473321804e-14,5.753120776945039e-15,7.162506995686147e-16,8.359838802973733e-17],[6.0405619695131405e-09,1.1280547299970278e-08,1.0533022260934026e-08,6.556688843730361e-09,3.0610992406907252e-09,1.1433000753503718e-09,3.558457707285397e-10,9.493286666413548e-11,2.21604938855727e-11,4.598220068643591e-12,9.930410367180118e-13,1.7651121657622824e-13,2.746906575928965e-14,3.94596622412544e-15,5.26354275124783e-16,6.552993277837083e-17,7.64843476071754e-18],[5.024112114073356e-10,9.382361215594986e-10,8.760622770869138e-10,5.453389935282854e-10,2.546005794685121e-10,9.509161213111013e-11,2.9596733821822215e-11,7.895844258169829e-12,1.8431531096986305e-12,3.8244741576435587e-13,7.14207748394133e-14,1.4021979103962329e-14,2.2846825633120347e-15,3.281975552673749e-16,4.377842497594411e-17,5.4503162250111125e-18,6.361426954803321e-19],[3.8304759458351906e-11,7.153285622508879e-11,6.67926073949478e-11,4.157765291870576e-11,1.9411218804572987e-11,7.249960284496729e-12,2.2565096957571914e-12,6.019937616093342e-13,1.405254001282196e-13,2.915849792699921e-14,5.445251894139747e-15,9.244386962987835e-16,1.6636973068755172e-16,2.5022388282540628e-17,3.3377480440209792e-18,4.155421838342262e-19,4.850069500500393e-20],[2.6957775387318737e-12,5.034274325690487e-12,4.700669402829971e-12,2.926114259333851e-12,1.3661051105065233e-12,5.102311140445766e-13,1.5880658800029592e-13,4.2366569688752133e-14,9.889768860155712e-15,2.0520902594423027e-15,3.8322098758822755e-16,6.505930617124572e-17,1.012467306121547e-17,1.681957814955161e-18,2.3490099753272643e-19,2.924465004913768e-20,3.4133378216232844e-21],[1.7616948228256687e-13,3.289906117559363e-13,3.0718947805597255e-13,1.9122202287098763e-13,8.927518187376664e-14,3.334368282034666e-14,1.037803527520809e-14,2.7686619318249697e-15,6.462979362931671e-16,1.341044182648358e-16,2.50435512623903e-17,4.251635797530599e-18,6.616489624413278e-19,9.504671476270252e-20,1.4661773896915282e-20,1.9111424383760534e-21,2.230621585984982e-22],[1.0745189580994436e-14,2.0066281900146624e-14,1.8736554914226437e-14,1.1663296396105402e-14,5.44520391206433e-15,2.0337472108733488e-15,6.329924744371786e-16,1.6887032281462032e-16,3.941995946912514e-17,8.179494991041521e-18,1.5274933127414052e-18,2.593220578382182e-19,4.035627195689314e-20,5.797229780909704e-21,7.7329518443580325e-22,1.1133494267746109e-22,1.3605337039262536e-23],[6.144248369997243e-16,1.1474178182482168e-15,1.0713821857058888e-15,6.669234575192409e-16,3.1136430873383945e-16,1.1629248503439205e-16,3.6195387247148195e-17,9.656239174503368e-18,2.254087932910291e-18,4.677148633561508e-19,8.734418528634731e-20,1.4828394782303544e-20,2.307627579032051e-21,3.3149363595088314e-22,4.421809071568452e-23,5.505053628565613e-24,7.430516701149938e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2630764756105367, "-10": 1.0714072742237207e-05, "-11": 1.7959285796259697e-06, "-12": 2.76486133315891e-07, "-13": 3.935091608328192e-08, "-14": 5.2060303068764825e-09, "-15": 6.404999824683652e-10, "-16": 6.754434064469554e-11, "-2": 0.1921443341267698, "-3": 0.10568742927406272, "-4": 0.04564512567778595, "-5": 0.01616263944367465, "-6": 0.004839366794304705, "-7": 0.001253672199225591, "-8": 0.00028598698853336265, "-9": 5.8252088949851185e-05, "0": 0.21109725858315176, "1": 0.10877172246427039, "10": 7.048608157851392e-09, "11": 5.788415205545223e-10, "12": 4.36581979228032e-11, "13": 3.0441716288595553e-12, "14": 1.973071463684194e-13, "15": 1.1892607399242654e-14, "16": 6.144248369997243e-16, "2": 0.03808918397591232, "3": 0.010264061758674533, "4": 0.0021717616799424334, "5": 0.00037674880195531595, "6": 5.5264974229929054e-05, "7": 7.014024255415383e-06, "8": 7.838832403353061e-07, "9": 7.822371634172732e-08} |
| Raw goal margin distribution | {"-1": 0.2463853388178839, "-10": 1.5136560811274468e-05, "-11": 2.6689913238880943e-06, "-12": 4.323203527276552e-07, "-13": 6.474864142935126e-08, "-14": 9.01480962558129e-09, "-15": 1.1661760803200623e-09, "-16": 1.281876272463444e-10, "-2": 0.18602814413027477, "-3": 0.10653121953546181, "-4": 0.04809180773754532, "-5": 0.017840364404193912, "-6": 0.00560416823874984, "-7": 0.0015245600440240473, "-8": 0.00036544840684590965, "-9": 7.825511799210676e-05, "0": 0.2037045089588469, "1": 0.12328772998786039, "10": 1.2057175288622168e-08, "11": 1.0415673635624268e-09, "12": 8.2654731492735e-11, "13": 6.064772782108294e-12, "14": 4.136778526612805e-13, "15": 2.6217524131845218e-14, "16": 1.4118725428597558e-15, "2": 0.04465008874312268, "3": 0.01252686531778893, "4": 0.002770501873083217, "5": 0.000503515568533485, "6": 7.748937950759453e-05, "7": 1.0327551963929683e-05, "8": 1.2128323285776515e-06, "9": 1.2723578655193697e-07} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Rio Ave", "away_goals": 1.0, "away_xg": 1.08, "date": "2026-11-01T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.65, "date": "2026-10-25T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.58, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.21, "date": "2026-10-11T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.29, "date": "2026-09-19T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 3.3, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 1.87, "date": "2026-09-14T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-09-06T00:00:00+00:00", "home": "Santa Clara", "home_goals": 4.0, "home_xg": 1.8, "source": "pipeline training history"}, {"away": "Sp Lisbon", "away_goals": 4.0, "away_xg": 1.66, "date": "2026-08-28T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.47, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 2.0, "away_xg": 0.71, "date": "2026-08-22T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 1.16, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 2.0, "away_xg": 1.98, "date": "2026-08-15T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.57, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.3, "date": "2026-08-09T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.53, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 18.4% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 61.2% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 52.7% |
| P home draw | 37.1% |
| P draw away | 84.0% |
| P home away | 78.9% |
| Raw p home draw | 38.8% |
| Raw p draw away | 81.6% |
| Raw p home away | 79.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9493 |
| Totals anchor target over 2 5 | 0.5290 |
| Totals anchor reference over odds | 1.82 |
| Totals anchor reference under odds | 2.03 |
| Totals anchor reference last update utc | 2026-11-06T13:39:19Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5607 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.53, "draw": 4.26, "home": 5.98}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.82, "under": 2.03}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.98 |
| Reference draw odds | 4.26 |
| Reference away odds | 1.53 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:19Z |
| Market reference home last update utc | 2026-11-06T13:39:19Z |
| Market reference draw last update utc | 2026-11-06T13:39:19Z |
| Market reference away last update utc | 2026-11-06T13:39:19Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.03 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market best over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market best under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0344 |
| Raw ev home | 0.0993 |
| Raw edge prob draw | -0.0106 |
| Raw ev draw | -0.1322 |
| Raw edge prob away | -0.0239 |
| Raw ev away | -0.0629 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,370.7424 |
| Elo away rating | 1,556.2873 |
| Elo rating diff | -125.5450 |
| Elo home expectancy | 0.3268 |
| Research p home | 0.1788 |
| Research p draw | 0.2138 |
| Research p away | 0.6074 |
| Research p over 1 5 | 0.7903 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.9637276741751953, 1.9671274275998987], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:17.507420+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T13:40:17.070085+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:18.092046+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Rio+Ave+FC%22+%22Braga%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:18.178682+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Rio+Ave+FC_vs_Braga&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.4282556797589714, "goals_for": 0.9932190408992481, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.6877582038772015, "results": "LLWLDLLWLL", "xg_against": 1.6602815864442582, "xg_for": 0.8033264458802587, "xg_matches": 10}, "venue": {"goals_against": 3.0556255141047255, "goals_for": 1.264779647458062, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 0.8723623359830545, "results": "LWDLL", "xg_against": 1.644775250533017, "xg_for": 0.9326370029898359, "xg_matches": 5}}}, "goal_rates": [0.9637276741751953, 1.9671274275998987], "h2h": [], "margin_distribution": {"-1": 0.24132822613821184, "-10": 1.5136560811274468e-05, "-11": 2.6689913238880943e-06, "-12": 4.323203527276552e-07, "-13": 6.474864142935126e-08, "-14": 9.01480962558129e-09, "-15": 1.1661760803200623e-09, "-16": 1.281876272463444e-10, "-2": 0.18602814413027477, "-3": 0.10653121953546181, "-4": 0.04809180773754532, "-5": 0.017840364404193912, "-6": 0.00560416823874984, "-7": 0.0015245600440240473, "-8": 0.00036544840684590965, "-9": 7.825511799210676e-05, "0": 0.21381873431819115, "1": 0.11823061730818829, "10": 1.2057175288622168e-08, "11": 1.0415673635624268e-09, "12": 8.2654731492735e-11, "13": 6.064772782108294e-12, "14": 4.136778526612805e-13, "15": 2.6217524131845218e-14, "16": 1.4118725428597558e-15, "2": 0.04465008874312268, "3": 0.01252686531778893, "4": 0.002770501873083217, "5": 0.000503515568533485, "6": 7.748937950759453e-05, "7": 1.0327551963929683e-05, "8": 1.2128323285776515e-06, "9": 1.2723578655193697e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:18.179116+00:00", "p_over_1_5": 0.7902833859212351, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Santa Clara vs Gil Vicente

The model's most likely 1X2 outcome is **Santa Clara win** at **41.7%**. Expected goals are 1.02 for Santa Clara and 0.85 for Gil Vicente (1.88 combined). The most likely exact score is 1-0 at 17.3%. Goal-market probabilities: at least one goal: 85.2%; Over 2.5 goals: 28.9%; Under 3.5 goals: 87.8%; Double Chance 1X: 72.6%; Double Chance X2: 58.3%; Double Chance 12 (either team wins): 69.1%; Under 4.5 goals: 95.8%; BTTS Yes (both teams score): 36.2%; BTTS No (at least one team does not score): 63.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Santa Clara win | 41.7% | 2.40 |
| Draw | 30.9% | 3.23 |
| Gil Vicente win | 27.4% | 3.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Santa Clara expected goals | 1.02 |
| Gil Vicente expected goals | 0.85 |
| Expected total goals | 1.88 |
| Over 0.5 | 85.2% |
| Under 0.5 | 14.8% |
| Over 1.5 | 55.4% |
| Under 1.5 | 44.6% |
| Over 2.5 | 28.9% |
| Under 2.5 | 71.1% |
| Over 3.5 | 12.2% |
| Under 3.5 | 87.8% |
| Over 4.5 | 4.2% |
| Under 4.5 | 95.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.32% |
| 2 | 0-0 | 14.82% |
| 3 | 1-1 | 12.84% |
| 4 | 0-1 | 12.50% |
| 5 | 2-0 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Santa Clara win | 41.7% | 42.6% | 2.26 | -5.9% |
| Draw | 30.9% | 31.1% | 3.06 | -5.4% |
| Gil Vicente win | 27.4% | 26.3% | 3.59 | -1.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T15:30:00+00:00 |
| Fixture id | 3145127655251c9de0251675640e2101 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:39:19Z |
| Market best draw last update utc | 2026-11-06T13:39:19Z |
| Market best away last update utc | 2026-11-06T13:39:19Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santa Clara |
| Matched away-team name | Gil Vicente |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0244 |
| Dc lambda away | 0.8519 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 36.2% |
| P btts no | 63.8% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.75 |
| Fair Over 1.5 odds | 1.81 |
| Fair Under 1.5 odds | 2.24 |
| Fair Over 2.5 odds | 3.45 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.22 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.71 |
| Fair Under 4.5 odds | 1.04 |
| Score matrix json | [[0.1481736912613647,0.1250271293690091,0.05066278399703146,0.01438716956614692,0.003064241122297867,0.0005221081804818654,7.413389407207842e-05,9.022488533563364e-06,9.60824165687862e-07,9.095131313623907e-08,7.74848040979033e-09,6.001107684640661e-10,4.2604722358275755e-11,2.7920420376927568e-12],[0.17316295711438745,0.12844901346585028,0.05189690467014902,0.014737633989702282,0.003138884539380243,0.0005348264807468927,7.59397595227102e-05,9.242271947417783e-06,9.842293730719607e-07,9.316684270119938e-08,7.937229608009063e-09,6.147291736738028e-10,4.364255258564468e-11,2.8600548180234186e-12],[0.08506697519133977,0.07247171789624098,0.029498989990088643,0.007548317777719659,0.0016076731168224582,0.00027392729629721,3.8894807486843325e-05,4.733704588942817e-06,5.041023599381053e-07,4.7718170742119286e-08,4.06528832225314e-09,3.1485183804721546e-10,2.2352831925224216e-11,1.4648621782318432e-12],[0.02904638838600979,0.024745697849026787,0.010540889867228169,0.0028603857588066443,0.0005489450829059924,9.353334381387953e-05,1.3280755333321726e-05,1.61633844022078e-06,1.7212734906973597e-07,1.6293520691524854e-08,1.388105586729457e-09,1.0750715834668013e-10,7.632445331068506e-12,5.001818351386509e-13],[0.007438486055016233,0.0063371227405431465,0.002699415198985772,0.000766577379551786,0.0001560143674143499,2.3952942596253672e-05,3.401067011641894e-06,4.1392791379047666e-07,4.40800718053757e-08,4.172605724345466e-09,3.554797902086316e-10,2.753149505366298e-11,1.954591992861047e-12,1.2809150508513169e-13],[0.0015239367884324307,0.001298298391056723,0.0005530343269533885,0.0001570501660201805,3.3449218400477e-05,5.446086762754331e-06,6.967830685747949e-07,8.48021991194038e-08,9.03076816493522e-09,8.548496723557987e-10,7.282782085446742e-11,5.6404297652112685e-12,4.004409798264934e-13,2.624235031714205e-14],[0.00026017652404456944,0.00022165405095657105,9.441766217355168e-05,2.6812638559492863e-05,5.7106708372042326e-06,9.730265475674014e-07,1.3202069818866587e-07,1.4477989878384115e-08,1.5417922110943112e-09,1.4594556547384784e-10,1.243364516657317e-11,9.629713132260025e-13,6.836592108484166e-14,4.480266858901051e-15],[3.807347101330944e-05,3.243620505373482e-05,1.3816804329714836e-05,3.9236830483995486e-06,8.356828556507312e-07,1.4238985700201676e-07,2.0217868576936703e-08,2.351288475342573e-09,2.2562135947203946e-10,2.1357246880728257e-11,1.8195032414154493e-12,1.4091840343934366e-13,1.0004468790105083e-14,6.556291387574965e-16],[4.875115271387317e-06,4.1532918957674e-06,1.7691718668365307e-06,5.024077563784351e-07,1.070049602305833e-07,1.823230054644943e-08,2.588795747565817e-09,3.1507018807673083e-10,3.2061653131907146e-11,2.7346873729119764e-12,2.329781814603237e-13,1.8043888364854084e-14,1.2810215954229497e-15,8.394999304386662e-17],[5.548745220291625e-07,4.7271822864112913e-07,2.0136311437801277e-07,5.7182907103834953e-08,1.217906097752602e-08,2.0751589425134275e-09,2.9465083861554257e-10,3.5860571552180824e-11,3.818869219344521e-12,3.4543064413436705e-13,2.6517046240884687e-14,2.053714296923039e-15,1.458029617558293e-16,9.554997096778636e-18],[5.683909943703289e-08,4.842334138026803e-08,2.062682214931643e-08,5.857585479123274e-09,1.247573695436148e-09,2.1257088007902738e-10,3.018283891289164e-11,3.673411755993571e-12,3.91189500829053e-13,3.702987503446149e-14,3.014538483935858e-15,2.103741774107438e-16,1.4935465069015964e-17,9.78775215914163e-19],[5.293061103417495e-09,4.509355484094969e-09,1.9208437692896105e-09,5.454794000358467e-10,1.1617854375534795e-10,1.9795363899316905e-11,2.810734375155372e-12,3.4208129747069614e-13,3.6428971454718294e-14,3.4483549730841815e-15,2.937781768463504e-16,2.1741796786799887e-17,1.3908441548381064e-18,9.114706382854612e-20],[4.5183312388542003e-10,3.8493343176653913e-10,1.6396954877653023e-10,4.656391764950709e-11,9.917383028045004e-12,1.6897974412768734e-12,2.3993354097473285e-13,2.920118589962383e-14,3.109696950539791e-15,2.943629346633587e-16,2.5077872478771577e-17,1.942251967968349e-18,1.3176282883059293e-19,7.780613482063445e-21],[3.56030429304587e-11,3.0331555550204134e-11,1.2920289761357014e-11,3.66909168772263e-12,7.814588949765186e-13,1.331507755080307e-13,1.8906015757150716e-14,2.3009625019618002e-15,2.450344345689465e-16,2.3194882459775212e-17,1.9760582464350045e-18,1.5304340594312145e-19,1.086528048090177e-20,6.804029307511572e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18504596133182122, "-10": 8.386062597224496e-09, "-11": 6.452181832279426e-10, "-12": 4.546477717629918e-11, "-13": 2.7920420376927568e-12, "-2": 0.06710511187996533, "-3": 0.017813685263622907, "-4": 0.0036396236964691556, "-5": 0.000602958018349193, "-6": 8.389692308936735e-05, "-7": 1.0055852119380475e-05, "-8": 1.0581657847040045e-06, "-9": 9.92111551191315e-08, "0": 0.3091436753346841, "1": 0.2569765850391514, "10": 6.151609356159212e-08, "11": 5.690914824945391e-09, "12": 4.821646794356242e-10, "13": 3.56030429304587e-11, "2": 0.1126749940911177, "3": 0.035964212305582985, "4": 0.008835234901942133, "5": 0.0017599224459471333, "6": 0.0002944403514835385, "7": 4.243410149618118e-05, "8": 5.369015852111601e-06, "9": 6.052660525552646e-07} |
| Raw goal margin distribution | {"-1": 0.20300671387919395, "-10": 9.200022513298738e-09, "-11": 7.078437279554063e-10, "-12": 4.9877635509481967e-11, "-13": 3.063040527905352e-12, "-2": 0.07361840349932994, "-3": 0.019542699994201045, "-4": 0.00399288933981176, "-5": 0.0006614817477301585, "-6": 9.204004528586872e-05, "-7": 1.1031883534869179e-05, "-8": 1.1608724510715282e-06, "-9": 1.0884069252815631e-07, "0": 0.3055961467604265, "1": 0.24274041046625092, "10": 5.810818055328329e-08, "11": 5.375645412694907e-09, "12": 4.554533720677317e-10, "13": 3.36306798281657e-11, "2": 0.1064329433391502, "3": 0.03397184088123267, "4": 0.008345774173691471, "5": 0.001662424990404823, "6": 0.0002781287321023906, "7": 4.008330647471347e-05, "8": 5.071579231791951e-06, "9": 5.717350863549226e-07} |
| Research history json | {"away": [{"away": "Guimaraes", "away_goals": 0.0, "away_xg": 0.42, "date": "2026-11-02T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 0.65, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 1.0, "away_xg": 1.08, "date": "2026-10-24T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 0.35, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 2.0, "away_xg": 1.52, "date": "2026-10-19T00:00:00+00:00", "home": "Sp Braga", "home_goals": 1.0, "home_xg": 1.35, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.49, "date": "2026-10-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 1.09, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.2, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.1, "date": "2026-09-13T00:00:00+00:00", "home": "Benfica", "home_goals": 3.0, "home_xg": 2.91, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 1.0, "away_xg": 0.33, "date": "2026-09-06T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 1.88, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 0.0, "away_xg": 0.27, "date": "2026-08-30T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": 0.23, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.76, "date": "2026-08-24T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 2.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.3, "date": "2026-08-09T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.53, "source": "pipeline training history"}], "h2h": [{"away": "Gil Vicente", "away_goals": 0.0, "away_xg": null, "date": "2026-03-21T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2025-11-03T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": null, "date": "2025-03-15T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": null, "date": "2024-10-25T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 2.0, "away_xg": null, "date": "2023-05-06T00:00:00+00:00", "home": "Santa Clara", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2022-12-29T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Santa Clara", "away_goals": 2.0, "away_xg": 0.82, "date": "2026-11-01T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 2.06, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-10-26T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.56, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-10-10T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-09-20T00:00:00+00:00", "home": "Santa Clara", "home_goals": 0.0, "home_xg": 1.04, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-13T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-09-06T00:00:00+00:00", "home": "Santa Clara", "home_goals": 4.0, "home_xg": 1.8, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.41, "date": "2026-08-29T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 0.41, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 0.0, "away_xg": 1.05, "date": "2026-08-23T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.36, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.26, "date": "2026-08-15T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 0.0, "home_xg": 0.69, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.24, "date": "2026-08-10T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": 1.44, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 39.3% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 30.1% |
| Raw p over 1 5 | 55.3% |
| Raw p under 3 5 | 87.9% |
| Raw p btts yes | 36.1% |
| P home draw | 72.6% |
| P draw away | 58.3% |
| P home away | 69.1% |
| Raw p home draw | 69.9% |
| Raw p draw away | 60.7% |
| Raw p home away | 69.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.2895 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.59, "draw": 3.06, "home": 2.26}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.26 |
| Reference draw odds | 3.06 |
| Reference away odds | 3.59 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:19Z |
| Market reference home last update utc | 2026-11-06T13:39:19Z |
| Market reference draw last update utc | 2026-11-06T13:39:19Z |
| Market reference away last update utc | 2026-11-06T13:39:19Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.48 |
| Reference Under 2.5 odds | 1.53 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Home probability edge | -1.0% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -8.2% |
| Under 2.5 probability edge | +8.2% |
| Raw edge prob home | -0.0330 |
| Raw ev home | -0.1107 |
| Raw edge prob draw | -0.0051 |
| Raw ev draw | -0.0649 |
| Raw edge prob away | 0.0380 |
| Raw ev away | 0.0803 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,480.8777 |
| Elo away rating | 1,467.9622 |
| Elo rating diff | 72.9156 |
| Elo home expectancy | 0.6034 |
| Research p home | 0.4001 |
| Research p draw | 0.3088 |
| Research p away | 0.2911 |
| Research p over 1 5 | 0.5865 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.0243595115734236, 0.8519371675462953], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:17.507420+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T13:40:17.070085+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:17.609410+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Santa+Clara%22+%22Gil+Vicente%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:17.695595+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Santa+Clara_vs_Gil+Vicente&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.7142214406459612, "goals_for": 0.7243555948174364, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 1.390678704648646, "results": "DLWWDLLDWW", "xg_against": 0.9698401540895999, "xg_for": 1.0809685833604397, "xg_matches": 10}, "venue": {"goals_against": 0.9955634945558121, "goals_for": 1.1034760336115474, "last_match": "2026-10-19T00:00:00+00:00", "matches": 4, "points_per_game": 1.9072673778740439, "results": "WWLD", "xg_against": 1.4159916672192816, "xg_for": 1.1644490402329988, "xg_matches": 4}}, "home": {"all": {"goals_against": 0.5739054067991304, "goals_for": 1.4663234401593819, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.0720961954158974, "results": "WLWDWWDWWD", "xg_against": 1.0399163493907206, "xg_for": 1.1824774148588095, "xg_matches": 10}, "venue": {"goals_against": 0.8151944568095735, "goals_for": 1.5119397621276964, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.4751375496189745, "results": "LDWWD", "xg_against": 1.0078220045059325, "xg_for": 1.437884392379623, "xg_matches": 5}}}, "goal_rates": [1.0899001163643753, 0.8826223325932282], "h2h": [{"away": "Gil Vicente", "away_goals": 0.0, "away_xg": null, "date": "2026-03-21T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2025-11-03T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": null, "date": "2025-03-15T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": null, "date": "2024-10-25T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 2.0, "away_xg": null, "date": "2023-05-06T00:00:00+00:00", "home": "Santa Clara", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2022-12-29T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.19209663133840285, "-10": 1.1999759925005353e-08, "-11": 9.558579353905315e-10, "-12": 6.971234933455517e-11, "-13": 4.406947986118827e-12, "-2": 0.0737860201116323, "-3": 0.020163991435514894, "-4": 0.004251045400940307, "-5": 0.0007275965380094283, "-6": 0.00010467465410595779, "-7": 1.297828004265613e-05, "-8": 1.4131818569986761e-06, "-9": 1.3713636415711155e-07, "0": 0.3087572262571887, "1": 0.2372092038888164, "10": 9.892143932329243e-08, "11": 9.730227764699586e-09, "12": 8.76296671744221e-10, "13": 6.840552099636306e-11, "2": 0.11251169301989772, "3": 0.03796748806804831, "4": 0.009884231101384445, "5": 0.0020890534827888536, "6": 0.0003711182025777189, "7": 5.681979331820473e-05, "8": 7.63998223450289e-06, "9": 9.155007691218629e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:17.696054+00:00", "p_over_1_5": 0.5865056990888478, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Vitória SC vs FC Porto

The model's most likely 1X2 outcome is **FC Porto win** at **60.4%**. Expected goals are 0.69 for Vitória SC and 1.65 for FC Porto (2.34 combined). The most likely exact score is 0-1 at 12.0%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 51.0%; Under 3.5 goals: 70.6%; Double Chance 1X: 39.6%; Double Chance X2: 83.0%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 85.9%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Vitória SC win | 17.0% | 5.88 |
| Draw | 22.6% | 4.42 |
| FC Porto win | 60.4% | 1.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Vitória SC expected goals | 0.69 |
| FC Porto expected goals | 1.65 |
| Expected total goals | 2.34 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.1% |
| Under 4.5 | 85.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.00% |
| 2 | 0-2 | 11.22% |
| 3 | 1-1 | 10.71% |
| 4 | 1-2 | 9.14% |
| 5 | 0-3 | 7.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Vitória SC win | 17.0% | 17.5% | 5.21 | -11.3% |
| Draw | 22.6% | 22.4% | 4.12 | -6.9% |
| FC Porto win | 60.4% | 60.1% | 1.62 | -2.2% |
| Over 2.5 | 51.0% | 51.0% | 1.88 | -4.2% |
| Under 2.5 | 49.0% | 49.0% | 1.95 | -4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T18:00:00+00:00 |
| Fixture id | c468a7bc1110c030b62f381e3a480145 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:39:19Z |
| Market best draw last update utc | 2026-11-06T13:39:19Z |
| Market best away last update utc | 2026-11-06T13:39:19Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Guimaraes |
| Matched away-team name | Porto |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6913 |
| Dc lambda away | 1.6519 |
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
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.27 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.04 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.07 |
| Fair Under 4.5 odds | 1.16 |
| Score matrix json | [[0.06550329954568375,0.1199870967489392,0.11218907463817383,0.072779847789388,0.03541057537017161,0.01378303347569723,0.004470698602660351,0.0012429658141079028,0.0003023785840441966,6.538684030354798e-05,1.2725421704571175e-05,2.251444936395699e-06,3.6514210564963537e-07,5.466387255289679e-08,7.598960575151502e-09,9.859270090260714e-10,1.1992414013984796e-10],[0.062309722030905644,0.10713144547921126,0.09137707759885462,0.05927858680118609,0.028841622090706374,0.011226167285168523,0.0036413472029600065,0.0010123854217959176,0.0002462848671098379,5.325704307332071e-05,1.036475120529327e-05,1.8337833637195856e-06,2.97405238702297e-07,4.4523274126554963e-08,6.189290823422004e-09,8.030294313518406e-10,9.767722476432734e-11],[0.02312510320015277,0.045005491749951484,0.04468912984472802,0.02414096044357297,0.01174563186459586,0.004571810412301591,0.0014829236581296791,0.0004122897953555157,0.00010029849825350862,2.1688711549192542e-05,4.221002259950192e-06,7.468007257681609e-07,1.2111705913812157e-07,1.8131920099789105e-08,2.520563208484082e-09,3.2703043009962233e-10,3.9778647679003566e-11],[0.006278402053013184,0.012218867494519838,0.011890025645695926,0.007870963879842863,0.0031889068158678984,0.0012412339798073524,0.00040260970336347267,0.00011193554792781876,2.723076701101199e-05,5.88842566189117e-06,1.145990529221487e-06,2.0275434748432098e-07,3.2882949155560014e-08,4.922766544835782e-09,6.843259935286005e-10,8.878786425142047e-11,1.0799793674101064e-11],[0.0012784266949461584,0.002488041742963421,0.0024210819983656413,0.001570616211025616,0.0007797878554547086,0.0002527437142542371,8.198057213892426e-05,2.2792645545162276e-05,5.54480888238583e-06,1.199018555008724e-06,2.3334996267228508e-07,4.128543666870534e-08,6.69572283744551e-09,1.002388204955041e-09,1.393444718553257e-10,1.8079246102405236e-11,2.199085757219896e-12],[0.000208253603455239,0.0004052979029360833,0.0003943902708019489,0.0002558507944838199,0.00012448258847428645,4.944301989315541e-05,1.3354500206186775e-05,3.712884427259204e-06,9.032402364502391e-07,1.9531814821871871e-07,3.801232466809177e-08,6.725329649693406e-09,1.0907222245498332e-09,1.6328738798098048e-10,2.2698985010369215e-11,2.9450794194645185e-12,3.5822744867465695e-13],[2.827014089762267e-05,5.5018634162442056e-05,5.3537938067991536e-05,3.4731394265554215e-05,1.689834056689081e-05,6.577424717966673e-06,2.1770631081961448e-06,5.040189660764604e-07,1.2261362264657563e-07,2.6514170599658923e-08,5.160120912117155e-09,9.129542712602168e-10,1.4806404526306177e-10,2.2166038850892055e-11,3.08135606697479e-12,3.997904898718631e-13,4.862888458784879e-14],[3.28939957180571e-06,6.401746362378085e-06,6.229458536976074e-06,4.041204953277634e-06,1.9662227516394184e-06,7.653226112036565e-07,2.4824192254379445e-07,7.042769403153057e-08,1.42668265889368e-08,3.0850819503568826e-09,6.004108568207113e-10,1.062276767504222e-10,1.7228135114427165e-11,2.5791508775566296e-12,3.5853416380178545e-13,4.651800891120037e-14,5.658260873900018e-15],[3.348986085498188e-07,6.517712130279068e-07,6.342303361177982e-07,4.114410202146319e-07,2.001840303218507e-07,7.79186207053344e-08,2.5273875255602146e-08,7.026768235740034e-09,1.7443435560068904e-09,3.1409673099383103e-10,6.112871243461612e-11,1.0815196012707942e-11,1.7540217756405543e-12,2.6258714433394383e-13,3.650289055910502e-14,4.736066907285791e-15,5.760758619059381e-16],[3.0308017702259794e-08,5.898469852655298e-08,5.739726521290979e-08,3.723503593549834e-08,1.8116471612039623e-08,7.051563892424001e-09,2.2872625896191123e-09,6.359160971157192e-10,1.5470048076484778e-10,3.413622848198585e-11,5.532092553645506e-12,9.78765345206864e-13,1.5873736608360668e-13,2.376389634260045e-14,3.303478202073305e-15,4.28609722466947e-16,5.2134338497535055e-17],[2.4685630881427243e-09,4.8042551307147545e-09,4.674959994310783e-09,3.0327630199709713e-09,1.475571696842847e-09,5.743440732258784e-10,1.8629565473701333e-10,5.1794842536950284e-11,1.2600226787697922e-11,2.72469367948118e-12,5.411081398952852e-13,7.971963151357094e-14,1.2929027773194591e-14,1.935549791414415e-15,2.6906557968369597e-16,3.490990900477511e-17,4.246298946504754e-18],[1.8278402824580808e-10,3.557296589787876e-10,3.4615603860909716e-10,2.2456004635566606e-10,1.0925827255942674e-10,4.252713807785082e-11,1.3794206994783029e-11,3.8351338909405825e-12,9.329800887523462e-13,2.0174914259378587e-13,3.9263908549841344e-14,7.0887102850964926e-15,9.573260610748483e-16,1.4331721536484614e-16,1.9922881757857648e-17,2.584893950751028e-18,3.144159573260198e-19],[1.2406340506503373e-11,2.414490653208578e-11,2.3495103618088017e-11,1.5241859072599074e-11,7.415830286340615e-12,2.886500318569286e-12,9.362723353723529e-13,2.603070815085356e-13,6.33253833933644e-14,1.3693584630641888e-14,2.6650108533031102e-15,4.715069826686787e-16,7.803209472097094e-17,9.727557660940954e-18,1.352251929946483e-18,1.7544790337529655e-19,2.134076737831328e-20],[7.772970920446138e-13,1.5127559674217602e-12,1.4720437271614017e-12,9.5495144021516e-13,4.646255931511231e-13,1.8084851875810054e-13,5.86604698835453e-14,1.6309074975746552e-14,3.967538722516123e-15,8.579470721027854e-16,1.6697149215386796e-16,2.9541427330240945e-17,4.7910649756010946e-18,7.319056355944067e-19,8.47229279502794e-20,1.099237482861726e-20,1.3370676402495983e-21],[4.522157726409465e-14,8.80090914563166e-14,8.564053542108768e-14,5.555714897061483e-14,2.7030980013435285e-14,1.0521402109718835e-14,3.4127478390650993e-15,9.488290920806692e-16,2.308234016630701e-16,4.9913630459552855e-17,9.714064687255942e-18,1.718660666788462e-18,2.787344982875701e-19,4.1728156941471516e-20,5.9192618222153344e-21,6.3951419954581985e-22,7.778789888666855e-23],[2.455506823714504e-15,4.778845358662124e-15,4.650234066028758e-15,3.016722694274188e-15,1.4677673776624642e-15,5.713063594526972e-16,1.8531033443397634e-16,5.152089889604087e-17,1.2533584013370654e-17,2.710282736801173e-18,5.274683805533693e-19,9.332233084889674e-20,1.5135130262101655e-20,2.2658160177037435e-21,3.149767073749901e-22,4.170168106639568e-23,4.2238402124528944e-24],[1.2499938067650902e-16,2.432706374148638e-16,2.3672358498075285e-16,1.5356848729363838e-16,7.471777777731941e-17,2.9082770374920033e-17,9.433358854268444e-18,2.622709247519044e-18,6.3803131158004925e-19,1.3796893589808654e-19,2.685116581996443e-20,4.750641882458337e-21,7.704649365865336e-22,1.1534303069516202e-22,1.6034120927361523e-23,2.0803467437335282e-24,2.5821539254946797e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.23896065842719727, "-10": 1.4685387232153878e-05, "-11": 2.567684858664865e-06, "-12": 4.1227692993468303e-07, "-13": 6.119099360009252e-08, "-14": 8.441768654182346e-09, "-15": 1.0836042337903987e-09, "-16": 1.1992414013984796e-10, "-2": 0.18454034650115447, "-3": 0.10661961300709838, "-4": 0.04823734725655488, "-5": 0.017865139202351773, "-6": 0.005589511174344123, "-7": 0.0015121277819844091, "-8": 0.0003600662458636274, "-9": 7.653230067640367e-05, "0": 0.22602631889464403, "1": 0.12090717107692663, "10": 2.848770413899547e-09, "11": 2.0845803250417387e-10, "12": 1.4007828449818271e-11, "13": 8.701099860542528e-13, "14": 5.0237146207737525e-14, "15": 2.6987774611293677e-15, "16": 1.2499938067650902e-16, "2": 0.03803859307329618, "3": 0.009197611942420726, "4": 0.001741511166692707, "5": 0.0002699318420490891, "6": 3.534487168370395e-05, "7": 4.001713017461347e-06, "8": 3.987904272607501e-07, "9": 3.547414606558455e-08} |
| Raw goal margin distribution | {"-1": 0.27363690471071556, "-10": 4.438948403972785e-06, "-11": 6.609253417632984e-07, "-12": 9.032368651284329e-08, "-13": 1.1405284622520942e-08, "-14": 1.3351287921462091e-09, "-15": 1.3662973848936942e-10, "-2": 0.18856002421183402, "-3": 0.09523607463838031, "-4": 0.03727728784568039, "-5": 0.011875230823707544, "-6": 0.003184530812975039, "-7": 0.0007367042294861548, "-8": 0.00014977254888218263, "-9": 2.7148658058466488e-05, "0": 0.2302812989708862, "1": 0.11770763080893559, "10": 7.316927712241995e-10, "11": 4.559381559743589e-11, "12": 2.6077145827196286e-12, "13": 1.3780640246997273e-13, "14": 6.751360460617681e-15, "15": 2.891466987123391e-16, "2": 0.033026257200661525, "3": 0.006980975067485312, "4": 0.001143572687028545, "5": 0.00015246367843848256, "6": 1.711097102330168e-05, "7": 1.6566365175361896e-06, "8": 1.4095197150030954e-07, "9": 1.069281783594878e-08} |
| Research history json | {"away": [{"away": "Estoril", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-10-31T00:00:00+00:00", "home": "Porto", "home_goals": 4.0, "home_xg": 3.1, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 1.0, "away_xg": 1.08, "date": "2026-10-24T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 0.35, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 2.0, "away_xg": 2.13, "date": "2026-10-10T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 0.19, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-09-20T00:00:00+00:00", "home": "Porto", "home_goals": 3.0, "home_xg": 1.3, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 4.0, "away_xg": 2.6, "date": "2026-09-12T00:00:00+00:00", "home": "Casa Pia", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.85, "date": "2026-09-04T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 3.0, "away_xg": 1.47, "date": "2026-08-29T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 0.0, "home_xg": 0.8, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 0.54, "date": "2026-08-23T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.99, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 2.0, "away_xg": 1.98, "date": "2026-08-15T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.57, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 0.0, "away_xg": 1.66, "date": "2026-08-09T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.59, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 15.9% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 61.1% |
| Raw p over 1 5 | 67.4% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 39.8% |
| P home draw | 39.6% |
| P draw away | 83.0% |
| P home away | 77.4% |
| Raw p home draw | 38.9% |
| Raw p draw away | 84.1% |
| Raw p home away | 77.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1782 |
| Totals anchor target over 2 5 | 0.5098 |
| Totals anchor reference over odds | 1.88 |
| Totals anchor reference under odds | 1.95 |
| Totals anchor reference last update utc | 2026-11-06T13:39:19Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4157 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.62, "draw": 4.12, "home": 5.21}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:19Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.88, "under": 1.95}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.21 |
| Reference draw odds | 4.12 |
| Reference away odds | 1.62 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:19Z |
| Market reference home last update utc | 2026-11-06T13:39:19Z |
| Market reference draw last update utc | 2026-11-06T13:39:19Z |
| Market reference away last update utc | 2026-11-06T13:39:19Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market best over 2 5 last update utc | 2026-11-06T13:39:19Z |
| Market best under 2 5 last update utc | 2026-11-06T13:39:19Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0159 |
| Raw ev home | -0.1715 |
| Raw edge prob draw | 0.0061 |
| Raw ev draw | -0.0512 |
| Raw edge prob away | 0.0099 |
| Raw ev away | -0.0107 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,465.5432 |
| Elo away rating | 1,690.2042 |
| Elo rating diff | -164.6610 |
| Elo home expectancy | 0.2793 |
| Research p home | 0.1535 |
| Research p draw | 0.2412 |
| Research p away | 0.6052 |
| Research p over 1 5 | 0.6790 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.6913279052582388, 1.6518827600768584], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:17.507420+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T13:40:17.070085+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:17.721861+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Vit%C3%B3ria+SC%22+%22FC+Porto%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:17.807733+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Vit%C3%B3ria+SC_vs_FC+Porto&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.430110668809516, "goals_for": 2.5822078216963384, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 3.0, "results": "WWWWWWWWWW", "xg_against": 0.7229623216576558, "xg_for": 2.179102135361633, "xg_matches": 10}, "venue": {"goals_against": 0.421593215819354, "goals_for": 2.304327993843115, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 3.0, "results": "WWWWW", "xg_against": 0.6668151416998931, "xg_for": 1.8153351910568654, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [0.6913279052582388, 1.6518827600768584], "h2h": [], "margin_distribution": {"-1": 0.2681542631922782, "-10": 4.438948403972785e-06, "-11": 6.609253417632984e-07, "-12": 9.032368651284329e-08, "-13": 1.1405284622520942e-08, "-14": 1.3351287921462091e-09, "-15": 1.3662973848936942e-10, "-2": 0.18856002421183402, "-3": 0.09523607463838031, "-4": 0.03727728784568039, "-5": 0.011875230823707544, "-6": 0.003184530812975039, "-7": 0.0007367042294861548, "-8": 0.00014977254888218263, "-9": 2.7148658058466488e-05, "0": 0.24124658200776086, "1": 0.11222498929049826, "10": 7.316927712241995e-10, "11": 4.559381559743589e-11, "12": 2.6077145827196286e-12, "13": 1.3780640246997273e-13, "14": 6.751360460617681e-15, "15": 2.891466987123391e-16, "2": 0.033026257200661525, "3": 0.006980975067485312, "4": 0.001143572687028545, "5": 0.00015246367843848256, "6": 1.711097102330168e-05, "7": 1.6566365175361896e-06, "8": 1.4095197150030954e-07, "9": 1.069281783594878e-08}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:17.808179+00:00", "p_over_1_5": 0.6789887285765146, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
