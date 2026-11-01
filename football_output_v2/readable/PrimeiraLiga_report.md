# Primeira Liga — football model report

Fixtures in this report: **6**.

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
| Training as of utc | 2026-11-01T09:34:49.329781+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1611, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1310, 'tuning_matches': 198, 'audit_matches': 100, 'audit_matchdays': 40, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8767945865077368, 'audit_candidate_poisson_score': 0.8692694227703041, 'audit_gain': 0.007525163737432727, 'audit_gain_lower95': -0.002911493812078021, 'audit_baseline_briers': [0.5874602781315315, 0.18463746867530761, 0.22936715245737097, 0.24667944034046813], 'audit_candidate_briers': [0.585638079076811, 0.18480680735767271, 0.22778937285472242, 0.24688804666669706], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1456.739 |
| Base scoring parameter | 0.094 |
| Home-advantage parameter | 0.170 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1611, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 6, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 25.00 |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 6} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 6} |
| Legacy comparison status | {'AVAILABLE': 6} |
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

## 2026-11-01 — Académico de Viseu vs Rio Ave FC

The model's most likely 1X2 outcome is **Académico de Viseu win** at **56.8%**. Expected goals are 2.16 for Académico de Viseu and 0.77 for Rio Ave FC (2.93 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 52.5%; Under 3.5 goals: 68.3%; Double Chance 1X: 81.3%; Double Chance X2: 43.2%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 49.6%; BTTS No (at least one team does not score): 50.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Académico de Viseu win | 56.8% | 1.76 |
| Draw | 24.5% | 4.08 |
| Rio Ave FC win | 18.7% | 5.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Académico de Viseu expected goals | 2.16 |
| Rio Ave FC expected goals | 0.77 |
| Expected total goals | 2.93 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 76.7% |
| Under 1.5 | 23.3% |
| Over 2.5 | 52.5% |
| Under 2.5 | 47.5% |
| Over 3.5 | 31.7% |
| Under 3.5 | 68.3% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.63% |
| 2 | 2-0 | 10.13% |
| 3 | 1-0 | 9.73% |
| 4 | 2-1 | 7.80% |
| 5 | 3-0 | 7.30% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T18:00:00+00:00 |
| Fixture id | ce5c2cbdf5db2a13f40f528d3e5044b9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 13.00 |
| Matched home-team name | Academico Viseu |
| Matched away-team name | Rio Ave |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1616 |
| Dc lambda away | 0.7701 |
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
| P btts yes | 49.6% |
| P btts no | 50.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.83 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.29 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.41 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.13612350605704868, "-10": 1.8831378520914574e-09, "-11": 1.3021589578972006e-10, "-12": 8.269417210979862e-12, "-13": 4.854770874952016e-13, "-14": 2.6496838183564353e-14, "-15": 1.350885617670684e-15, "-16": 6.436442529864774e-17, "-17": 2.655738387569357e-18, "-2": 0.04001155969018658, "-3": 0.009101173287977994, "-4": 0.0016239443682897036, "-5": 0.0002374407369394144, "-6": 2.9346166205849336e-05, "-7": 3.1374042142535916e-06, "-8": 2.9531803936848073e-07, "-9": 2.481788489557539e-08, "0": 0.24517902596590663, "1": 0.20028572345164675, "10": 3.0937565565581915e-05, "11": 6.004640484066413e-06, "12": 1.070328018059832e-06, "13": 1.7637202926638666e-07, "14": 2.7019294865462015e-08, "15": 3.866495585997381e-09, "16": 5.170872389130676e-10, "17": 5.988557154305557e-11, "2": 0.1706230249462177, "3": 0.1089352722670618, "4": 0.054558355408264744, "5": 0.022390528159243615, "6": 0.00776746782328981, "7": 0.0023308672990301404, "8": 0.0006158231817878973, "9": 0.00014526125976732404} |
| Raw goal margin distribution | {"-1": 0.09056741474191507, "-10": 1.2529131213758855e-09, "-11": 8.663688867251954e-11, "-12": 5.501913372014286e-12, "-13": 3.2300376330630186e-13, "-14": 1.7629211901980842e-14, "-15": 8.987883250170933e-16, "-16": 4.2823754467539215e-17, "-17": 1.76694949285406e-18, "-2": 0.026620997547722035, "-3": 0.006055307857445974, "-4": 0.0010804632306418247, "-5": 0.0001579770777429543, "-6": 1.9524962901972676e-05, "-7": 2.0874174998567312e-06, "-8": 1.9648473747836908e-07, "-9": 1.651214944032289e-08, "0": 0.17768741618053732, "1": 0.24619240367058154, "10": 3.8028639780436646e-05, "11": 7.380939831724387e-06, "12": 1.3156535720117654e-06, "13": 2.1679754840755166e-07, "14": 3.321227810837061e-08, "15": 4.752719393542788e-09, "16": 6.356067125579525e-10, "17": 7.361170107030018e-11, "2": 0.20973083807042345, "3": 0.13390388521831856, "4": 0.06706345528176053, "5": 0.027522570515660517, "6": 0.009547817692114668, "7": 0.002865115960818466, "8": 0.0007569735213654908, "9": 0.0001785560053209085} |
| Unadjusted home-win probability | 69.8% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.5% |
| Raw p over 1 5 | 78.6% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 47.1% |
| P home draw | 81.3% |
| P draw away | 43.2% |
| P home away | 75.5% |
| Raw p home draw | 87.5% |
| Raw p draw away | 30.2% |
| Raw p home away | 82.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5255 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.94 |
| Reference draw odds | 3.60 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-11-01T09:34:39Z |
| Market reference home last update utc | 2026-11-01T09:34:39Z |
| Market reference draw last update utc | 2026-11-01T09:34:39Z |
| Market reference away last update utc | 2026-11-01T09:34:39Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-11-01T09:34:39Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:34:39Z |
| Home probability edge | +5.6% |
| Draw probability edge | -2.9% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | +2.9% |
| Under 2.5 probability edge | -2.9% |
| Raw edge prob home | 0.1859 |
| Raw edge prob draw | -0.0964 |
| Raw edge prob away | -0.0895 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06398480276100467, 0.06326108196733282, 0.02224427522407405, 0.005763971484979466, 0.0011201769987441571, 0.00017415721251021278, 2.2563945030808705e-05, 2.505773497150711e-06, 2.434874845308967e-07, 2.1030952962773494e-08, 1.6348720552806904e-09, 1.1553562122842087e-10, 7.484442845987664e-12, 4.475493621202279e-13, 2.4850648429083092e-14, 1.2878677995627748e-15, 6.257143578229434e-17, 2.8612250434853002e-18], [0.10678026950815304, 0.1084801581216615, 0.046883818945194514, 0.012148608699759972, 0.002360974905527793, 0.0003670677123474795, 4.755758067445836e-05, 5.281369241059239e-06, 5.131937554797363e-07, 4.432652361199234e-08, 3.445787496613235e-09, 2.4351214381359264e-10, 1.5774812160082357e-11, 9.43290938963623e-13, 5.2377220200857904e-14, 2.7144134898448054e-15, 1.318805776680489e-16, 6.03054743519094e-18], [0.10831915661435682, 0.08420348926358427, 0.04677311043542938, 0.012802691141384912, 0.0024880900566523283, 0.00038683067874697053, 5.011808609973717e-05, 5.565718747549077e-06, 5.40824164270291e-07, 4.6713068566185354e-08, 3.631309078121578e-09, 2.5662286468108303e-10, 1.6624129798738817e-11, 9.940778278797339e-13, 5.5197215553509363e-14, 2.8605578136020147e-15, 1.3898104261641203e-16, 6.3552327788568906e-18], [0.07610071469096485, 0.05915800965147496, 0.0229936743704426, 0.008514973112958093, 0.001748032734420582, 0.0002717717903015293, 3.521096628098924e-05, 3.910251775365538e-06, 3.799614648925164e-07, 3.281873691050857e-08, 2.5512127747882914e-09, 1.8029297881077434e-10, 1.1679449862257419e-11, 6.983993923570015e-13, 3.877935984609168e-14, 2.009713709320776e-15, 9.764253159078384e-17, 4.464932811657008e-18], [0.040098992810852746, 0.031171541730612568, 0.012115828176117442, 0.0031394724000030306, 0.0008719525197742, 0.00014320200683722953, 1.8553364308051604e-05, 2.0603900826127564e-06, 2.0020931618050905e-07, 1.7292850675316903e-08, 1.344285176960857e-09, 9.499998640668226e-11, 6.1541363699831175e-12, 3.680006466030242e-13, 2.043362244352907e-14, 1.0589584593151508e-15, 5.144980816792722e-17, 2.3526626450570182e-18], [0.016903170814880387, 0.013139928399725597, 0.005107258284283543, 0.0013234007770761564, 0.0002571912637777624, 5.7145543439646645e-05, 7.820911801176788e-06, 8.685286853953852e-07, 8.439544319960125e-08, 7.289559870491053e-09, 5.66664656074135e-10, 4.004591849022346e-11, 2.5941903022496486e-12, 1.551255369145784e-13, 8.613508378102337e-15, 4.463891601492298e-16, 2.1687948621490778e-17, 9.91732105261858e-19], [0.0059377464696090555, 0.004615794534697692, 0.001794077879174576, 0.0004648842739638038, 9.034615666111082e-05, 1.4046382690191011e-05, 2.6008146635111726e-06, 3.050967887587507e-07, 2.964643441148766e-08, 2.5606768611666766e-09, 1.9905798136373112e-10, 1.4067331729751495e-11, 9.112872654115636e-13, 5.449250435012332e-14, 3.025753541933137e-15, 1.5680760070261387e-16, 7.618543394648331e-18, 3.483756906504539e-19], [0.0017878386854233044, 0.00138980269287943, 0.0005401917804115488, 0.00013997534140121966, 2.7202972505608363e-05, 4.229326141208113e-06, 5.479548115871802e-07, 8.696467209592794e-08, 8.92645763792809e-09, 7.710125679319425e-10, 5.993579576794918e-11, 4.235633837830121e-12, 2.7438602085408296e-13, 1.640753909608448e-14, 9.110458424778137e-16, 4.721432552558981e-17, 2.2939218906100024e-18, 1.0489493615023807e-19], [0.00047102402970116233, 0.0003661574560540399, 0.00014231894146571114, 3.687790733199615e-05, 7.166895891621116e-06, 1.1142583825903969e-06, 1.443641898747844e-07, 1.603194656040618e-08, 2.2263448151698984e-09, 2.031309925545987e-10, 1.5790686417147884e-11, 1.115920208517565e-12, 7.228974867257488e-14, 4.322730705811553e-15, 2.400241629544933e-16, 1.2439087513882854e-17, 6.04356724991106e-19, 2.763562279056121e-20], [0.00011030755906053586, 8.574920314524434e-05, 3.3329202017828896e-05, 8.636315101872807e-06, 1.6783916360854767e-06, 2.609444839242435e-07, 3.380817197573199e-08, 3.754468520829682e-09, 3.6482391442273004e-10, 4.503362928178343e-11, 3.697968606126176e-12, 2.613336614397213e-13, 1.692929705991955e-14, 1.0123260015770763e-15, 5.621046456558969e-17, 2.9130687482490903e-18, 1.4153230181883422e-19, 6.4718950646288e-21], [2.3249306058232252e-05, 1.8073189953185723e-05, 7.024729991204935e-06, 1.82025905322212e-06, 3.5375128563504686e-07, 5.499875278386685e-08, 7.125681541931179e-09, 7.913219045928162e-10, 7.689321489855094e-11, 6.641563482424724e-12, 7.378472909951322e-13, 5.5080778959093506e-14, 3.568154458760163e-15, 2.1336594918627163e-16, 1.1847368444112004e-17, 6.139817386363043e-19, 2.983048333348002e-20, 1.3640685227359865e-21], [4.454736596088315e-06, 3.4629550013603167e-06, 1.34598949710928e-06, 3.487749096011596e-07, 6.778132620752957e-08, 1.053816213489748e-08, 1.3653325504600198e-09, 1.5162304796739194e-10, 1.4733300750633363e-11, 1.2725719996242654e-12, 9.892525575046563e-14, 9.991039029458055e-15, 6.836844165637507e-16, 4.088247192490501e-17, 2.2700421958030896e-18, 1.1764337884246678e-19, 5.715738158025692e-21, 2.61365476998936e-22], [7.824300181944559e-07, 6.082334805384796e-07, 2.364096201866392e-07, 6.125883157819708e-08, 1.1905113389727857e-08, 1.8509229924355549e-09, 2.398070344352045e-10, 2.6631074951546564e-11, 2.587757216555732e-12, 2.235145695694079e-13, 1.7375233751125593e-14, 1.2278994059144657e-15, 1.136783345098929e-16, 7.180598125627898e-18, 3.9871025328950385e-19, 2.0662885237478515e-20, 1.0039123558743692e-21, 4.5906237217987453e-23], [1.2685479034939557e-07, 9.861243672020799e-08, 3.8328913906653135e-08, 9.931848288276965e-09, 1.9301670795104604e-09, 3.000887526019409e-10, 3.887973412342643e-11, 4.317676151476439e-12, 4.195511311527015e-13, 3.623824904902344e-14, 2.817033579382674e-15, 1.9907840712306987e-16, 1.2896377274304678e-17, 1.1020988171601817e-18, 6.464259347808442e-20, 3.350058042075936e-21, 1.6276355517070732e-22, 7.44274371202631e-24], [1.9097809478622196e-08, 1.4845963037880606e-08, 5.770363841173319e-09, 1.4952257290218858e-09, 2.9058392706235736e-10, 4.51779377671453e-11, 5.853289046661706e-12, 6.500200449992754e-13, 6.316283009278494e-14, 5.455617200351228e-15, 4.2410042573680215e-16, 2.997097295318725e-17, 1.9415313798615043e-18, 1.1609830530795588e-19, 9.212850073124051e-21, 5.043465055886017e-22, 2.4503823293955666e-23, 1.120494551439453e-24], [2.6834716882616588e-09, 2.086036178218582e-09, 8.108054494988359e-10, 2.1009717977771458e-10, 4.0830533062370006e-11, 6.3480430605347055e-12, 8.224574372003813e-13, 9.133562618847358e-14, 8.875136517316337e-15, 7.665797648428553e-16, 5.959120530123385e-17, 4.2112817954101934e-18, 2.7280848599741165e-19, 1.63132067946221e-20, 9.058079423542554e-22, 6.708740978401471e-23, 3.443081581534369e-24, 1.5744294700421022e-25], [3.534937627481509e-10, 2.7479357471624525e-10, 1.0680741311853271e-10, 2.7676104408803953e-11, 5.3786066871381125e-12, 8.362278004912921e-13, 1.0834232962021663e-13, 1.2031643305779458e-14, 1.1691218566356497e-15, 1.009815630648349e-16, 7.849950301609705e-18, 5.547522093727348e-19, 3.5937065647717775e-20, 2.1489389575245556e-21, 1.1932209282125445e-22, 6.183785568391466e-24, 4.293689130773278e-25, 2.0739961594574947e-26], [4.382657719925708e-11, 3.406923427031342e-11, 1.3242110129754486e-11, 3.4313163463405137e-12, 6.668460551204788e-13, 1.036765174284204e-13, 1.3432410903472494e-14, 1.4916974491296774e-15, 1.4494911849883581e-16, 1.2519814310035613e-17, 9.732461761961564e-19, 6.877883881604576e-20, 4.455520147456156e-21, 2.6642800819526943e-22, 1.4793695005966502e-23, 7.666730906079561e-25, 3.724903757301416e-26, 2.4342338294071084e-27]] |
| Legacy trial inputs | {"lambda_home": 2.107680222120886, "lambda_away": 0.7773647053343452, "rho": 0.05, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5989 |
| Legacy p draw | 0.2287 |
| Legacy p away | 0.1724 |
| Legacy p over 1 5 | 0.7660 |
| Legacy p under 3 5 | 0.6860 |
| Legacy p btts yes | 0.4869 |
| Legacy p over 2 5 | 0.5269 |
| Legacy goal margin distribution | {"-1": 0.12484696193710236, "-10": 1.895727616020421e-09, "-11": 1.323443715710127e-10, "-12": 8.484993155754388e-12, "-13": 5.028871353289237e-13, "-14": 2.7708507894355968e-14, "-15": 1.4261036100096805e-15, "-16": 6.860198321748528e-17, "-17": 2.8612250434853002e-18, "-2": 0.037172198097283934, "-3": 0.008549135442806752, "-4": 0.0015414807512097199, "-5": 0.00022767834725854143, "-6": 2.842034243208197e-05, "-7": 3.0683291835642616e-06, "-8": 2.9163192253530694e-07, "-9": 2.4745419547214206e-08, "0": 0.2286848325457295, "1": 0.21738870754697473, "10": 2.6958899569871635e-05, "11": 5.102835896455744e-06, "12": 8.870283982188195e-07, "13": 1.4253990178723892e-07, "14": 2.129408438630565e-08, "15": 2.9715073731076583e-09, "16": 3.875629970184643e-10, "17": 4.382657719925708e-11, "2": 0.18101111889866944, "3": 0.1128727508251665, "4": 0.0551804095514587, "5": 0.022097769820099183, "6": 0.007478868952692488, "7": 0.0021892152743363267, "8": 0.0005641589488951614, "9": 0.00012978997352206038} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6860 |
| Legacy raw p draw | 0.1833 |
| Legacy raw p away | 0.1308 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1077 |
| Legacy lambda away | 0.7774 |
| Legacy model home team | Academico Viseu |
| Legacy model away team | Rio Ave |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 77.2% |
| Market reference home draw last update utc | 2026-11-01T09:34:21Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.2% |
| Market reference draw away last update utc | 2026-11-01T09:34:21Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.6% |
| Market reference home away last update utc | 2026-11-01T09:34:21Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.21 |
| Market reference dc draw away odds | 1.90 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 77.0% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market reference over 1 5 last update utc | 2026-11-01T09:34:16Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 73.5% |
| Market reference under 3 5 odds | 1.32 |
| Market reference under 3 5 opposite odds | 3.31 |
| Market reference under 3 5 last update utc | 2026-11-01T09:33:54Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 53.5% |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-11-01T09:34:39Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,418.3104 |
| Elo away rating | 1,393.4483 |
| Elo rating diff | 84.8621 |
| Elo home expectancy | 0.6198 |

</details>


---

## 2026-11-01 — Arouca vs Nacional

The model's most likely 1X2 outcome is **Arouca win** at **54.9%**. Expected goals are 1.56 for Arouca and 1.07 for Nacional (2.63 combined). The most likely exact score is 1-0 at 13.2%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 49.1%; Under 3.5 goals: 72.7%; Double Chance 1X: 79.0%; Double Chance X2: 45.1%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 87.2%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arouca win | 54.9% | 1.82 |
| Draw | 24.1% | 4.15 |
| Nacional win | 21.0% | 4.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arouca expected goals | 1.56 |
| Nacional expected goals | 1.07 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 49.1% |
| Under 2.5 | 50.9% |
| Over 3.5 | 27.3% |
| Under 3.5 | 72.7% |
| Over 4.5 | 12.8% |
| Under 4.5 | 87.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.21% |
| 2 | 1-1 | 11.44% |
| 3 | 2-1 | 10.44% |
| 4 | 2-0 | 9.78% |
| 5 | 0-0 | 6.63% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T15:30:00+00:00 |
| Fixture id | fd5c6a92f2448c1cfe7a2d9b8075172b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 13.00 |
| Matched home-team name | Arouca |
| Matched away-team name | Nacional |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5600 |
| Dc lambda away | 1.0677 |
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
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.08 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.97 |
| Fair Over 3.5 odds | 3.66 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.81 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.13274867712244917, "-10": 3.5217870852346845e-08, "-11": 3.376164663897071e-09, "-12": 2.9724246833908403e-10, "-13": 2.418780239570466e-11, "-14": 1.820812958525024e-12, "-15": 1.1665064812001603e-13, "-2": 0.05483929659213955, "-3": 0.017292642696001517, "-4": 0.004277607227952568, "-5": 0.0008670725460866614, "-6": 0.00014856787532013124, "-7": 2.2020098129130987e-05, "-8": 2.873527091471122e-06, "-9": 3.347862173753169e-07, "0": 0.24122125607145845, "1": 0.26982642934924916, "10": 2.1972889664072095e-06, "11": 3.0777186230010614e-07, "12": 3.959108149221088e-08, "13": 4.7072160530852776e-09, "14": 5.177430403162465e-10, "15": 4.8463782189989395e-11, "2": 0.1647275512840336, "3": 0.07589566122442762, "4": 0.027430751118980294, "5": 0.008124066024219974, "6": 0.002033874424632752, "7": 0.00044045311587019716, "8": 8.398020811594999e-05, "9": 1.4295864888060882e-05} |
| Raw goal margin distribution | {"-1": 0.16791565793431207, "-10": 4.454757729723092e-08, "-11": 4.270557892715766e-09, "-12": 3.759861545824448e-10, "-13": 3.059548947153339e-11, "-14": 2.3031717719042063e-12, "-15": 1.4755303594828798e-13, "-2": 0.06936699308445886, "-3": 0.021873705551458372, "-4": 0.005410805196978919, "-5": 0.0010967721879339113, "-6": 0.00018792558293647898, "-7": 2.7853530033451875e-05, "-8": 3.634764598907225e-06, "-9": 4.2347576771753217e-07, "0": 0.24095518709788205, "1": 0.24256801861176552, "10": 1.975314398164511e-06, "11": 2.766801273049482e-07, "12": 3.559151049592783e-08, "13": 4.231683582398369e-09, "14": 4.654395929354605e-10, "15": 4.3567873053094634e-11, "2": 0.1480864414286747, "3": 0.06822852827589565, "4": 0.024659641251640184, "5": 0.0073033564700050605, "6": 0.0018284083233734718, "7": 0.00039595765272394494, "8": 7.549635791578689e-05, "9": 1.2851667750270682e-05} |
| Unadjusted home-win probability | 49.3% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 26.6% |
| Raw p over 1 5 | 73.2% |
| Raw p under 3 5 | 73.0% |
| Raw p btts yes | 51.2% |
| P home draw | 79.0% |
| P draw away | 45.1% |
| P home away | 75.9% |
| Raw p home draw | 73.4% |
| Raw p draw away | 50.7% |
| Raw p home away | 75.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4911 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.74 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.30 |
| Market reference 1x2 last update utc | 2026-11-01T09:34:39Z |
| Market reference home last update utc | 2026-11-01T09:34:39Z |
| Market reference draw last update utc | 2026-11-01T09:34:39Z |
| Market reference away last update utc | 2026-11-01T09:34:39Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-11-01T09:34:39Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:34:39Z |
| Home probability edge | -2.4% |
| Draw probability edge | -0.0% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | -0.0792 |
| Raw edge prob draw | -0.0004 |
| Raw edge prob away | 0.0795 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06891547123575158, 0.07271374306723596, 0.03579014491196656, 0.012639812577744228, 0.00334795086175559, 0.0007094266566873657, 0.00012527219434624082, 1.896073100930019e-05, 2.511097191182855e-06, 2.9561022025403973e-07, 3.1319720464396205e-08, 3.0166409645934756e-09, 2.663427076126359e-10, 2.1706804273935425e-11, 1.6427303722805981e-12, 1.1603084632637107e-13], [0.1318170552696551, 0.11511180405234993, 0.05459472361171457, 0.019280924284693055, 0.005107005082341391, 0.001082168075594453, 0.00019109173330782741, 2.8922930361835496e-05, 3.830458285429947e-06, 4.5092743578613783e-07, 4.7775483629801224e-08, 4.60162092394019e-09, 4.0628241500206286e-10, 3.3111824015913794e-11, 2.5058409476638342e-12, 1.7699486831369428e-13], [0.09547966613555264, 0.10116011722563312, 0.0489578019091793, 0.014705678544895467, 0.003895143923555711, 0.000825376191320566, 0.0001457468304485145, 2.2059695385828388e-05, 2.9215138959849397e-06, 3.4392510544784296e-07, 3.643865274366213e-08, 3.509684343641754e-09, 3.098740758090823e-10, 2.5254590123552766e-11, 1.9112201737255672e-12, 1.3499506554173103e-13], [0.04854861579010074, 0.05143695891747672, 0.02724857032090366, 0.008791541862317467, 0.0019805666844643203, 0.0004196796366865188, 7.410799765495987e-05, 1.1216709474169988e-05, 1.4855043110461776e-06, 1.74875850332911e-07, 1.8527988456195847e-08, 1.7845717694707061e-09, 1.5756189834608088e-10, 1.284121994209924e-11, 9.717995219292258e-13, 6.864103987586732e-14], [0.018514162678799802, 0.019615641138322353, 0.01039132538540456, 0.0036698483794614083, 0.0008880362880444945, 0.00016004610924825056, 2.8261310895372783e-05, 4.277526362923874e-06, 5.665015990090351e-07, 6.668943880202527e-08, 7.0657048981997965e-09, 6.805518862746079e-10, 6.008671041357832e-11, 4.897038383754509e-12, 3.705987111551432e-13, 2.617646987502617e-14], [0.005648345916662887, 0.0059843876522289495, 0.003170210898955443, 0.0011196062964618234, 0.00029655399097185857, 5.740852005140976e-05, 8.622029673435243e-06, 1.304998178130147e-06, 1.7282968984655745e-07, 2.034577668334379e-08, 2.155622487631666e-09, 2.076244297193135e-10, 1.83314001987716e-11, 1.494000416788727e-12, 1.1306315890108509e-13, 7.985981288830172e-15], [0.001436009293163746, 0.0015214429869005565, 0.0008059797291732899, 0.0002846435169030353, 7.539451252517951e-05, 1.5976004177452147e-05, 2.577267501827068e-06, 3.317766898497296e-07, 4.3939419507241384e-08, 5.172615987934668e-09, 5.480354727673409e-10, 5.278547294442412e-11, 4.66049024449486e-12, 3.798277432283486e-13, 2.874465361929031e-14, 2.030318878303991e-15], [0.00031292944171788887, 0.00033154681293702396, 0.00017563590144355229, 6.202838467489388e-05, 1.642967272246372e-05, 3.4814273778955907e-06, 6.147584714712159e-07, 8.500589897540388e-08, 9.575103783288174e-09, 1.1271959318308173e-09, 1.1942571357379634e-10, 1.1502800614139082e-11, 1.0155955238481484e-12, 8.277055322918402e-14, 6.263920750569209e-15, 4.424390260714772e-16], [5.9668298433055786e-05, 6.321819407676386e-05, 3.3489643305408296e-05, 1.1827356824541237e-05, 3.132752897201619e-06, 6.638264735235678e-07, 1.1722000888961668e-07, 1.7741982321478307e-08, 2.1466178564070452e-09, 2.1492980297341819e-10, 2.277168002787691e-11, 2.193314045787825e-12, 1.9365022502062248e-13, 1.5782401439876253e-14, 1.1943826399144733e-15, 8.436273589706882e-17], [1.0113194472782268e-05, 1.0714867152340594e-05, 5.676167822209501e-06, 2.0046215965044134e-06, 5.309710535841322e-07, 1.125121111079969e-07, 1.9867647932544685e-08, 3.0070929163680207e-09, 3.9824954914522025e-10, 4.2830719088814115e-11, 3.859577608908482e-12, 3.7174533324129135e-13, 3.282182392931538e-14, 2.6749630742036455e-15, 2.024362053146543e-16, 1.42986607090906e-17], [1.5426790208062582e-06, 1.6344589052576993e-06, 8.65849563307084e-07, 3.057874235391543e-07, 8.099497218451949e-08, 1.7162734669056377e-08, 3.030635249899379e-09, 4.5870562147113647e-10, 6.074947200564025e-11, 7.15152120075636e-12, 6.922150110106981e-13, 5.67064865821965e-14, 5.0066810577629216e-15, 4.080421302202146e-16, 3.087986568744677e-17, 2.181135145863787e-18], [2.139292177920903e-07, 2.2665668645208649e-07, 1.2007068048873803e-07, 4.240471507430026e-08, 1.1231883503199887e-08, 2.380022255702621e-09, 4.202698161314622e-10, 6.361046820152414e-11, 8.424362328241745e-12, 9.917288793502675e-13, 1.0507306293749438e-13, 9.245731766387003e-15, 6.942956687528658e-16, 5.658476751606231e-17, 4.282229435250706e-18, 3.02466377879185e-19], [2.7194186524804182e-08, 2.8812072853285546e-08, 1.5263106718523395e-08, 5.3903891350755605e-09, 1.427771008389028e-09, 3.025429150012779e-10, 5.342372532643695e-11, 8.086015342156459e-12, 1.0708854212208972e-12, 1.2606627746050377e-13, 1.3356644322570689e-14, 1.2864802052998903e-15, 1.0376823854186045e-16, 7.192924548482936e-18, 5.443470845454576e-19, 3.8448825188162675e-20], [3.1909495258217252e-09, 3.38079133660699e-09, 1.7909637819691802e-09, 6.325050259869026e-10, 1.6753379322618962e-10, 3.5500204070583136e-11, 6.2687078667543125e-12, 9.48808187305288e-13, 1.256570526181175e-13, 1.4792541336648836e-14, 1.5672606286200825e-15, 1.509548151895042e-16, 1.3327974617011063e-17, 9.92346602511204e-19, 6.387336020249916e-20, 4.5115620719400635e-21], [3.476795235305935e-10, 3.683643102330747e-10, 1.951398570666024e-10, 6.891649156036132e-11, 1.8254149410011324e-11, 3.868031736829406e-12, 6.830259603383611e-13, 1.0338025588144598e-13, 1.3691342915013761e-14, 1.6117659280142473e-15, 1.7076560572250551e-16, 1.644773688678767e-17, 1.4521896466779587e-18, 1.1835276704823281e-19, 8.182630924210531e-21, 4.915708439941187e-22], [3.535697240920051e-11, 3.7460494138933534e-11, 1.98445812171394e-11, 7.008403790636763e-12, 1.8563401447666858e-12, 3.933561862033417e-13, 6.945974209012082e-14, 1.0513166889262433e-14, 1.3923294325052426e-15, 1.6390716044534243e-16, 1.7365862529548013e-17, 1.6726385649477838e-18, 1.4767918670942723e-19, 1.2035783633684963e-20, 9.10845607660121e-22, 5.877546745055331e-23]] |
| Legacy trial inputs | {"lambda_home": 1.5254121978550759, "lambda_away": 1.0594938306761141, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5293 |
| Legacy p draw | 0.2427 |
| Legacy p away | 0.2279 |
| Legacy p over 1 5 | 0.7266 |
| Legacy p under 3 5 | 0.7368 |
| Legacy p btts yes | 0.5039 |
| Legacy p over 2 5 | 0.4802 |
| Legacy goal margin distribution | {"-1": 0.14416372161787244, "-10": 3.6244435268780025e-08, "-11": 3.449175945710896e-09, "-12": 3.014343928421511e-10, "-13": 2.434764028714099e-11, "-14": 1.8197252405942925e-12, "-15": 1.1603084632637107e-13, "-2": 0.059415504155739284, "-3": 0.018650757499382165, "-4": 0.00458766988438305, "-5": 0.0009241324885704128, "-6": 0.0001572987925281916, "-7": 2.3154341658096673e-05, "-8": 3.0003094613800487e-06, "-9": 3.470579622576903e-07, "0": 0.24272472833124514, "1": 0.26420875409676375, "10": 1.7852499665084513e-06, "11": 2.446030272590501e-07, "12": 3.0777126122268404e-08, "13": 3.5791584172719396e-09, "14": 3.8514001766952705e-10, "15": 3.535697240920051e-11, "2": 0.1585065529636553, "3": 0.07163622517838313, "4": 0.02536980680521681, "5": 0.007357800724102907, "6": 0.0018031338003835116, "7": 0.00038214113184030003, "8": 7.129288382852936e-05, "9": 1.1873285918948487e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4864 |
| Legacy raw p draw | 0.2441 |
| Legacy raw p away | 0.2695 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5254 |
| Legacy lambda away | 1.0595 |
| Legacy model home team | Arouca |
| Legacy model away team | Nacional |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 79.9% |
| Market reference home draw last update utc | 2026-11-01T09:34:21Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.7% |
| Market reference draw away last update utc | 2026-11-01T09:34:21Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market reference home away last update utc | 2026-11-01T09:34:21Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.17 |
| Market reference dc draw away odds | 2.09 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 77.5% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market reference over 1 5 last update utc | 2026-11-01T09:34:16Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 72.3% |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.19 |
| Market reference under 3 5 last update utc | 2026-11-01T09:33:54Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 52.5% |
| Market reference btts yes odds | 1.87 |
| Market reference btts yes opposite odds | 2.06 |
| Market reference btts yes last update utc | 2026-11-01T09:34:39Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,468.8191 |
| Elo away rating | 1,372.3854 |
| Elo rating diff | 156.4337 |
| Elo home expectancy | 0.7111 |

</details>


---

## 2026-11-01 — Braga vs Famalicão

The model's most likely 1X2 outcome is **Braga win** at **56.4%**. Expected goals are 1.54 for Braga and 0.96 for Famalicão (2.50 combined). The most likely exact score is 1-0 at 14.6%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 45.7%; Under 3.5 goals: 75.4%; Double Chance 1X: 81.2%; Double Chance X2: 43.6%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 89.0%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Braga win | 56.4% | 1.77 |
| Draw | 24.9% | 4.02 |
| Famalicão win | 18.8% | 5.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Braga expected goals | 1.54 |
| Famalicão expected goals | 0.96 |
| Expected total goals | 2.50 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 45.7% |
| Under 2.5 | 54.3% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 11.0% |
| Under 4.5 | 89.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.57% |
| 2 | 1-1 | 11.73% |
| 3 | 2-0 | 10.68% |
| 4 | 2-1 | 10.26% |
| 5 | 0-0 | 7.75% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T20:30:00+00:00 |
| Fixture id | 12fa9f636dbb126cfd4118fa8cdc8fad |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 12.00 |
| Matched home-team name | Sp Braga |
| Matched away-team name | Famalicao |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5362 |
| Dc lambda away | 0.9608 |
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
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.91 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.46 |
| Fair Over 2.5 odds | 2.19 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.07 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 9.12 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.12369367931852705, "-10": 1.3452521060317531e-08, "-11": 1.1621460306830765e-09, "-12": 9.218384245126679e-11, "-13": 6.757720259586562e-12, "-14": 4.586730676675422e-13, "-15": 2.6747647935565898e-14, "-2": 0.0468304999707697, "-3": 0.01345252376137582, "-4": 0.0030186455090560633, "-5": 0.0005537237776607695, "-6": 8.5732880654939e-05, "-7": 1.1471118676868975e-05, "-8": 1.350442427485804e-06, "-9": 1.418714567686429e-07, "0": 0.2485511276249594, "1": 0.2768774573407713, "10": 2.086191650253162e-06, "11": 2.8815847846434467e-07, "12": 3.654649082870488e-08, "13": 4.2836232069823055e-09, "14": 4.6487315712584943e-10, "15": 4.334480013775117e-11, "2": 0.17002700376494848, "3": 0.07809316994138703, "4": 0.028018286781579693, "5": 0.0082175586238158, "6": 0.002034310455443346, "7": 0.00043520689220623467, "8": 8.191930185337891e-05, "9": 1.3760219875003701e-05} |
| Raw goal margin distribution | {"-1": 0.15982061303055156, "-10": 1.738156852081223e-08, "-11": 1.5015713986201375e-09, "-12": 1.1910776923479e-10, "-13": 8.731432361995675e-12, "-14": 5.926366752052013e-13, "-15": 3.455977309219887e-14, "-2": 0.06050817838947248, "-3": 0.017381572010762514, "-4": 0.0039002944890733837, "-5": 0.0007154486315137189, "-6": 0.00011077268958798908, "-7": 1.4821462415734048e-05, "-8": 1.7448630990065485e-06, "-9": 1.8330753290888442e-07, "0": 0.2446112257578238, "1": 0.2518976574090421, "10": 1.8979760745140744e-06, "11": 2.621609082403029e-07, "12": 3.3249277549314546e-08, "13": 3.897156024998496e-09, "14": 4.2293244237729244e-10, "15": 3.9434245461610785e-11, "2": 0.15468721923416082, "3": 0.07104762791746755, "4": 0.025490485475703522, "5": 0.007476172985845525, "6": 0.0018507755853096016, "7": 0.00039594265884959384, "8": 7.452856737286904e-05, "9": 1.2518777025898263e-05} |
| Unadjusted home-win probability | 51.3% |
| Unadjusted draw probability | 24.5% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 70.6% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 47.8% |
| P home draw | 81.2% |
| P draw away | 43.6% |
| P home away | 75.1% |
| Raw p home draw | 75.8% |
| Raw p draw away | 48.7% |
| Raw p home away | 75.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4574 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.70 |
| Reference draw odds | 3.95 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-11-01T09:34:39Z |
| Market reference home last update utc | 2026-11-01T09:34:39Z |
| Market reference draw last update utc | 2026-11-01T09:34:39Z |
| Market reference away last update utc | 2026-11-01T09:34:39Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.89 |
| Market reference over 2 5 last update utc | 2026-11-01T09:34:39Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:34:39Z |
| Home probability edge | -2.2% |
| Draw probability edge | -0.2% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | -0.0727 |
| Raw edge prob draw | -0.0056 |
| Raw edge prob away | 0.0783 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07341502090920281, 0.0678769359977639, 0.029464146604457692, 0.00921861788053741, 0.0021632117018749856, 0.0004060899304229393, 6.35278520698225e-05, 8.51842557084129e-06, 9.99453395031098e-07, 1.0423492051639869e-07, 9.783774649391946e-09, 8.348471276216427e-10, 6.530086176875582e-11, 4.714859567595592e-12, 3.161068649022569e-13, 1.9780436447514104e-14], [0.13663845660920076, 0.11502943712552065, 0.04782854878816232, 0.014964394556467569, 0.003511497475599657, 0.0006591975091067628, 0.0001031234677494094, 1.3827786648050144e-05, 1.6223923301585528e-06, 1.6920242246536144e-07, 1.588180202307411e-08, 1.3551903304766986e-09, 1.0600155826483226e-10, 7.653535460754276e-12, 5.131298324439933e-13, 3.210917941665209e-14], [0.10592978168054984, 0.09942858952520964, 0.04612240409003903, 0.012145698376022812, 0.0028500711489437384, 0.0005350309419886246, 8.369911191846468e-05, 1.1223182147561449e-05, 1.3167982049205e-06, 1.373314222638206e-07, 1.2890302799226722e-08, 1.0999264242841557e-09, 8.603508476169006e-11, 6.21191407816364e-12, 4.164766004455741e-13, 2.6061088327005152e-14], [0.057317885352238515, 0.05380013443553779, 0.025249138619599272, 0.007808290552375463, 0.0015421541399331996, 0.0002895016085777039, 4.528902094308401e-05, 6.072787627951224e-06, 7.125105644914696e-07, 7.430909978003712e-08, 6.974855288853849e-09, 5.951627170642313e-10, 4.6552999981742983e-11, 3.3612245140265047e-12, 2.253526596346475e-13, 1.4101477876982342e-14], [0.023260738829519293, 0.021833165484169383, 0.010246603054030688, 0.003205913933185683, 0.0007435711328620734, 0.00011748551549780267, 1.8379186209118665e-05, 2.4644581026119916e-06, 2.8915097010399684e-07, 3.015611186661875e-08, 2.8305351157094727e-09, 2.4152887772503124e-10, 1.889213406341498e-11, 1.3640518153745004e-12, 9.145259508591364e-14, 5.722660422501441e-15], [0.007551736670954857, 0.007088266526624132, 0.0033266203882415845, 0.0010408189520807137, 0.00024423528188837406, 4.531782425192332e-05, 5.966911691625641e-06, 8.00100923875573e-07, 9.387457554036992e-08, 9.79036037959195e-09, 9.189499950277554e-10, 7.841378110896331e-11, 6.1334432515200846e-12, 4.428475032862505e-13, 2.969062681224182e-14, 1.8578956104860425e-15], [0.0020430967092022368, 0.0019177064356857398, 0.000900005848207373, 0.000281590032667618, 6.607702604573521e-05, 1.2404340678357739e-05, 1.9180198102299573e-06, 2.1646458766062353e-07, 2.539744759665139e-08, 2.648748750784911e-09, 2.4861880022694485e-10, 2.1214582171013464e-11, 1.6593822413665916e-12, 1.1981088802029997e-13, 8.032698249073467e-15, 5.02647347652465e-16], [0.0004737881793704634, 0.00044471053995546843, 0.00020870873626507925, 6.529990886165831e-05, 1.5323069988521376e-05, 2.8765304940385732e-06, 4.499983624545772e-07, 5.96408118834545e-08, 5.889594165208516e-09, 6.14237124748827e-10, 5.765397603855344e-11, 4.919599849404211e-12, 3.8480591127952057e-13, 2.7783796160124634e-14, 1.862759340622142e-15, 1.1656245670457912e-16], [9.613633714087638e-05, 9.023619469794933e-05, 4.234907983666077e-05, 1.3250001428769802e-05, 3.1092034090151697e-06, 5.836766669408039e-07, 9.130914651196653e-08, 1.2243608797671137e-08, 1.4198749956705542e-09, 1.2463482602659682e-10, 1.1698565560075932e-11, 9.982357735242651e-13, 7.808094931731932e-14, 5.6376087690752625e-15, 3.7797240999198055e-16, 2.3651682594972763e-17], [1.733957301086577e-05, 1.6275397344242194e-05, 7.638266482887857e-06, 2.3898285913635275e-06, 5.607896152445384e-07, 1.0527449330972708e-07, 1.6468919657132367e-08, 2.208311185734051e-09, 2.5909765760259735e-10, 2.670863116666963e-11, 2.110004787826341e-12, 1.8004619888646074e-13, 1.4083023773429218e-14, 1.0168239373924884e-15, 6.817276790507325e-17, 4.265921600324608e-18], [2.814697553774139e-06, 2.6419520862961137e-06, 1.2399042335694727e-06, 3.87936005450376e-07, 9.103183551415087e-08, 1.7088993979725773e-08, 2.673366169004571e-09, 3.584706548749868e-10, 4.205879479186937e-11, 4.386392756222134e-12, 4.0694729788719917e-13, 2.922653258269302e-14, 2.286068551974974e-15, 1.6505895776119355e-16, 1.1066346497470114e-17, 6.924783606552262e-19], [4.15367380324842e-07, 3.8987518057033336e-07, 1.829737524235471e-07, 5.724805569306876e-08, 1.3433647602021863e-08, 2.5218377911431106e-09, 3.9451098423684933e-10, 5.289982813219223e-11, 6.206653140723458e-12, 6.47303816278533e-13, 6.075770611984328e-14, 5.124356515793658e-15, 3.37357136081501e-16, 2.435789479139087e-17, 1.6330704335383096e-18, 1.021896374661372e-19], [5.618811704039049e-08, 5.273970300676282e-08, 2.475146365237777e-08, 7.744133521272954e-09, 1.8172138677607713e-09, 3.4113732487807104e-10, 5.3366803475718196e-11, 7.155934421676566e-12, 8.395944641279758e-13, 8.756292456404622e-14, 8.218895523036888e-15, 7.013163697567546e-16, 5.422048318855528e-17, 3.294972855898897e-18, 2.2091082978901874e-19, 1.38235296805732e-20], [7.016078879914956e-09, 6.585483477453873e-09, 3.090657429463194e-09, 9.669918570644988e-10, 2.2691124937893652e-10, 4.2597020621054215e-11, 6.663788047665041e-12, 8.935448099442573e-13, 1.0483819885310165e-13, 1.0933777781799854e-14, 1.026274278847162e-15, 8.757173632374847e-17, 6.849768849080466e-18, 4.888360399996486e-19, 2.758461911284669e-20, 1.7261118497355707e-21], [8.135041341563359e-10, 7.63577223976693e-10, 3.5835723046485737e-10, 1.1212129836074728e-10, 2.631002909399754e-11, 4.939062540640982e-12, 7.726565249196284e-13, 1.0360522015003367e-13, 1.2155836564017649e-14, 1.2677556195817293e-15, 1.1899500888031612e-16, 1.0153815365240229e-17, 7.942207281469145e-19, 5.734440706382677e-20, 3.800088266551352e-21, 2.0014015660456022e-22], [8.803631227289988e-11, 8.263328987774706e-11, 3.87809326613611e-11, 1.2133614594554483e-11, 2.8472356070204347e-12, 5.344986385523277e-13, 8.361583949178294e-14, 1.1212016179475326e-14, 1.3154881195508882e-15, 1.3719479093608677e-16, 1.2877478209214352e-17, 1.098832105116101e-18, 8.594948827059645e-20, 6.205733831470807e-21, 4.16062246978968e-22, 2.5733431632904892e-23]] |
| Legacy trial inputs | {"lambda_home": 1.623279622866329, "lambda_away": 0.9386273430172289, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5629 |
| Legacy p draw | 0.2432 |
| Legacy p away | 0.1939 |
| Legacy p over 1 5 | 0.7221 |
| Legacy p under 3 5 | 0.7421 |
| Legacy p btts yes | 0.4841 |
| Legacy p over 2 5 | 0.4716 |
| Legacy goal margin distribution | {"-1": 0.12951701221002787, "-10": 1.1228454599635057e-08, "-11": 9.47291675284696e-10, "-12": 7.338497530783265e-11, "-13": 5.254050488366591e-12, "-14": 3.48216044318909e-13, "-15": 1.9780436447514104e-14, "-2": 0.04758731922914534, "-3": 0.013312996359162142, "-4": 0.002912480305476157, "-5": 0.0005211801875513578, "-6": 7.874965665901827e-05, "-7": 1.0285371962570791e-05, "-8": 1.1821606261435778e-06, "-9": 1.2126459620882826e-07, "0": 0.24316602074186983, "1": 0.26477920081527884, "10": 3.2303180343816474e-06, "11": 4.713127092950358e-07, "12": 6.314409136290377e-08, "13": 7.81843703655301e-09, "14": 8.96137424034083e-10, "15": 8.803631227289988e-11, "2": 0.17108638523891093, "3": 0.08277518483765813, "4": 0.031317528318231425, "5": 0.009691980124716707, "6": 0.0025326397655316755, "7": 0.0005720643581103866, "8": 0.00011371074736913802, "9": 2.0172474917034463e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5402 |
| Legacy raw p draw | 0.2361 |
| Legacy raw p away | 0.2237 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6233 |
| Legacy lambda away | 0.9386 |
| Legacy model home team | Sp Braga |
| Legacy model away team | Famalicao |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 81.9% |
| Market reference home draw last update utc | 2026-11-01T09:34:21Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.0% |
| Market reference draw away last update utc | 2026-11-01T09:34:21Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market reference home away last update utc | 2026-11-01T09:34:21Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.14 |
| Market reference dc draw away odds | 2.12 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 73.9% |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.20 |
| Market reference over 1 5 last update utc | 2026-11-01T09:34:16Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 75.9% |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.59 |
| Market reference under 3 5 last update utc | 2026-11-01T09:33:54Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 47.8% |
| Market reference btts yes odds | 2.06 |
| Market reference btts yes opposite odds | 1.89 |
| Market reference btts yes last update utc | 2026-11-01T09:34:39Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,518.8201 |
| Elo away rating | 1,511.6518 |
| Elo rating diff | 67.1683 |
| Elo home expectancy | 0.5955 |

</details>


---

## 2026-11-01 — CS Maritimo vs Santa Clara

The model's most likely 1X2 outcome is **Santa Clara win** at **42.9%**. Expected goals are 0.98 for CS Maritimo and 1.33 for Santa Clara (2.32 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.8%; Under 3.5 goals: 79.7%; Double Chance 1X: 57.1%; Double Chance X2: 73.0%; Double Chance 12 (either team wins): 70.0%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 46.4%; BTTS No (at least one team does not score): 53.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CS Maritimo win | 27.0% | 3.70 |
| Draw | 30.0% | 3.33 |
| Santa Clara win | 42.9% | 2.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CS Maritimo expected goals | 0.98 |
| Santa Clara expected goals | 1.33 |
| Expected total goals | 2.32 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 66.6% |
| Under 1.5 | 33.4% |
| Over 2.5 | 39.8% |
| Under 2.5 | 60.2% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.98% |
| 2 | 0-1 | 13.04% |
| 3 | 0-0 | 10.48% |
| 4 | 1-0 | 9.90% |
| 5 | 0-2 | 8.29% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T18:00:00+00:00 |
| Fixture id | 6bf5102547eb3f3eb74023133e27d2d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 11.00 |
| Matched home-team name | Maritimo |
| Matched away-team name | Santa Clara |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9841 |
| Dc lambda away | 1.3334 |
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
| P btts yes | 46.4% |
| P btts no | 53.6% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.55 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 4.92 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 12.08 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2319060788970069, "-10": 5.13901685400281e-07, "-11": 6.168493418903271e-08, "-12": 6.796506968333999e-09, "-13": 6.895737149729702e-10, "-14": 6.004787661737768e-11, "-2": 0.1256213047858877, "-3": 0.05062560849725791, "-4": 0.015876556694738735, "-5": 0.004061512058067846, "-6": 0.0008758417829130828, "-7": 0.00016307898011740527, "-8": 2.6701061205170503e-05, "-9": 3.899656840463281e-06, "0": 0.3004089086957728, "1": 0.17478047624112816, "10": 2.4931903261549024e-08, "11": 2.208700709186788e-09, "12": 1.79608094427856e-10, "13": 1.3449409324096763e-11, "14": 8.64375683701736e-13, "2": 0.06922766776494901, "3": 0.020590601371928457, "4": 0.004765818150726028, "5": 0.0008998109400734389, "6": 0.0001432094100788156, "7": 1.9680052673754225e-05, "8": 2.378149572158035e-06, "9": 2.5634178802000724e-07} |
| Raw goal margin distribution | {"-1": 0.24507112620198312, "-10": 5.430753061633935e-07, "-11": 6.518671853408053e-08, "-12": 7.182337025796424e-09, "-13": 7.287200392998938e-10, "-14": 6.345672704506415e-11, "-2": 0.13275268498896356, "-3": 0.05349956735974038, "-4": 0.016777850964041614, "-5": 0.0042920795301604675, "-6": 0.0009255623359859773, "-7": 0.00017233679042537227, "-8": 2.8216850422646134e-05, "-9": 4.121035973869585e-06, "0": 0.263998826530501, "1": 0.18256657950150737, "10": 2.604256720667063e-08, "11": 2.307093688556381e-09, "12": 1.8760925794274373e-10, "13": 1.4048552272100026e-11, "14": 9.028818056313824e-13, "2": 0.07231161501858557, "3": 0.02150786943254388, "4": 0.00497812534338151, "5": 0.0009398956282772007, "6": 0.0001495890886259396, "7": 2.05567577015867e-05, "8": 2.484091142610695e-06, "9": 2.677612764800367e-07} |
| Unadjusted home-win probability | 28.2% |
| Unadjusted draw probability | 26.4% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 66.7% |
| Raw p under 3 5 | 79.6% |
| Raw p btts yes | 45.5% |
| P home draw | 57.1% |
| P draw away | 73.0% |
| P home away | 70.0% |
| Raw p home draw | 54.6% |
| Raw p draw away | 71.8% |
| Raw p home away | 73.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.3975 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 3.75 |
| Reference draw odds | 3.15 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-11-01T09:34:39Z |
| Market reference home last update utc | 2026-11-01T09:34:39Z |
| Market reference draw last update utc | 2026-11-01T09:34:39Z |
| Market reference away last update utc | 2026-11-01T09:34:39Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.58 |
| Reference Under 2.5 odds | 1.60 |
| Market reference over 2 5 last update utc | 2026-11-01T09:34:39Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:34:39Z |
| Home probability edge | +0.5% |
| Draw probability edge | -1.6% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +1.7% |
| Under 2.5 probability edge | -1.7% |
| Raw edge prob home | 0.0172 |
| Raw edge prob draw | -0.0520 |
| Raw edge prob away | 0.0348 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.10502684434266323, 0.1352647577116372, 0.0800190757611901, 0.033174628644632984, 0.010315252724804781, 0.002565923252167147, 0.0005318953650209464, 9.450656097321084e-05, 1.4692840589619615e-05, 2.0304722161921806e-06, 2.525403890434237e-07, 2.8554328661091792e-08, 2.959541960830673e-09, 2.831489421783374e-10, 2.515479032931909e-11], [0.10444764139537888, 0.13578234847381443, 0.08197662117180264, 0.03398619565455305, 0.010567599748794572, 0.00262869467558691, 0.0005449073789790958, 9.681852075212657e-05, 1.5052278665996661e-05, 2.0801446415529218e-06, 2.5871840690808424e-07, 2.9252867034497403e-08, 3.031942669384584e-09, 2.90075751904748e-10, 2.5770164149819547e-11], [0.050369065979354116, 0.06264662681292271, 0.04552919759676067, 0.017408808210674986, 0.005413060030133027, 0.0013465008533717526, 0.00027911885606878245, 4.959351956149956e-05, 7.710254925071777e-06, 1.0655161137579913e-06, 1.3252378030816236e-07, 1.4984247045247563e-08, 1.5530572757709364e-09, 1.4858600776637907e-10, 1.3200296079085252e-11], [0.01720042294618989, 0.021393060529970306, 0.013303830965980737, 0.006445813921238344, 0.0018484941132235265, 0.00045981365199213796, 9.531569194885678e-05, 1.6935583284343297e-05, 2.632958208685822e-06, 3.63860783523964e-07, 4.52552579129158e-08, 5.116937979634126e-09, 5.303501560633887e-10, 5.0740313082540673e-11, 4.507740438710232e-12], [0.004405301306099524, 0.005479102333063288, 0.003407322256778837, 0.0014126212964340982, 0.0005133198498204958, 0.00011776557402223976, 2.441186147269073e-05, 4.33747166540466e-06, 6.743423851794547e-07, 9.31905215302616e-08, 1.159058980208392e-08, 1.310529028003101e-09, 1.3583109220658223e-10, 1.2995399484867263e-11, 1.1545038691392535e-12], [0.0009026140651649962, 0.001122628053489502, 0.000698135446322371, 0.0002894357870930663, 8.999658514491863e-05, 2.6162444917155382e-05, 5.001812132941158e-06, 8.887162671547892e-07, 1.3816782991826899e-07, 1.9094057279762195e-08, 2.37482720295059e-09, 2.6851782688389087e-10, 2.7830798802032003e-11, 2.662662447455788e-12, 2.3654941130352646e-13], [0.00015411585837606594, 0.00019168190789156374, 0.0001192023786523448, 4.9419399158649454e-05, 1.536636920009489e-05, 3.822390501116372e-06, 9.259895877927212e-07, 1.5174289394692346e-07, 2.3591316078062484e-08, 3.260194075320998e-09, 4.05487291858961e-10, 4.5847784758286486e-11, 4.75193951900439e-12, 4.546334081115305e-13, 4.038937235565009e-14], [2.25551527530523e-05, 2.805301646467126e-05, 1.7445497740214123e-05, 7.232624265489016e-06, 2.2488977333027244e-06, 5.594142130663756e-07, 1.1596209154172415e-07, 2.4079102775742422e-08, 3.4526345529466528e-09, 4.771356831691307e-10, 5.93438462704024e-11, 6.709911617848214e-12, 6.954555024627823e-13, 6.653647505615054e-14, 5.911062447958124e-15], [2.8883662975364672e-06, 3.5924113743732883e-06, 2.234034425227474e-06, 9.261949320363566e-07, 2.879892009864005e-07, 7.163742924175694e-08, 1.4849866044716918e-08, 2.638507238625374e-09, 4.793918026368411e-10, 6.110101056315197e-11, 7.599450440894028e-12, 8.592574294943962e-13, 8.905859591121396e-14, 8.520523634363496e-15, 7.569584539836552e-16], [3.287806445958435e-07, 4.089215859938823e-07, 2.542985212789896e-07, 1.0542809858847971e-07, 3.278160225651062e-08, 8.154436708177456e-09, 1.6903495012070276e-09, 3.003393688071854e-10, 4.669346152508742e-11, 7.541120175555584e-12, 8.650399420123274e-13, 9.780865113399571e-14, 1.0137475497987799e-14, 9.69885036807656e-16, 8.616403281165801e-17], [3.368237647619346e-08, 4.189252328286903e-08, 2.605195491841464e-08, 1.0800723723233756e-08, 3.358355447152082e-09, 8.353922643279502e-10, 1.7317013398397815e-10, 3.076867162670507e-11, 4.783574629212012e-12, 6.610645041340002e-13, 9.60873329151474e-14, 1.0020139154400689e-14, 1.0385473471564832e-15, 9.936118042635899e-17, 8.827190528313844e-18], [3.1369422515694363e-09, 3.9015782156514784e-09, 2.4262978646212457e-09, 1.0059042781285765e-09, 3.127738657456607e-10, 7.78026245403682e-11, 1.6127861713921227e-11, 2.8655800495162916e-12, 4.455088665883415e-13, 6.156694957365731e-14, 7.657401698756694e-15, 1.0118381402505346e-15, 9.67230758154243e-17, 9.253809192043229e-18, 8.221031241810586e-19], [2.678068991138534e-10, 3.330853677848316e-10, 2.0713779704605345e-10, 8.587601681101915e-11, 2.6702117027271e-11, 6.642162319261998e-12, 1.3768671172640731e-12, 2.4464017685997665e-13, 3.803396381589723e-14, 5.25609097361325e-15, 6.537273688054664e-16, 7.391588416541305e-17, 8.953211228637604e-18, 7.900158007283973e-19, 7.018455259372092e-20], [2.1104491462252202e-11, 2.6248753575342383e-11, 1.632346994693995e-11, 6.76744949288959e-12, 2.104257219253053e-12, 5.23434827189285e-13, 1.0850385265318317e-13, 1.927884061594054e-14, 2.9972620843011372e-15, 4.1420563639132776e-16, 5.151690908354901e-17, 5.824932634131261e-18, 6.037309703314263e-19, 6.750289567885962e-20, 5.5308854846434115e-21], [1.5443414899751462e-12, 1.920777824902335e-12, 1.194485635653006e-12, 4.952146348503074e-13, 1.539810487774445e-13, 3.830284763659109e-14, 7.939873925613103e-15, 1.4107477308831439e-15, 2.1932753989333317e-16, 3.0309896393609786e-17, 3.769799441758822e-18, 4.262450559061768e-19, 4.417859524989836e-20, 4.226708956146252e-21, 4.388303022353496e-22]] |
| Legacy trial inputs | {"lambda_home": 1.0244634843878309, "lambda_away": 1.2437520052208448, "rho": 0.05, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2878 |
| Legacy p draw | 0.2933 |
| Legacy p away | 0.4189 |
| Legacy p over 1 5 | 0.6553 |
| Legacy p under 3 5 | 0.8059 |
| Legacy p btts yes | 0.4555 |
| Legacy p over 2 5 | 0.3891 |
| Legacy goal margin distribution | {"-1": 0.2366216038509982, "-10": 2.8339820817064375e-07, "-11": 3.1739365078681464e-08, "-12": 3.2628180088145064e-09, "-13": 3.0891910632815697e-10, "-14": 2.515479032931909e-11, "-2": 0.11990346975175824, "-3": 0.0451885238986509, "-4": 0.013240695688474517, "-5": 0.0031631527208170083, "-6": 0.0006367998654085307, "-7": 0.00011067094983124967, "-8": 1.6910764483604363e-05, "-9": 2.304718452250472e-06, "0": 0.2933246371849349, "1": 0.1819046580943235, "10": 3.7798013919432664e-08, "11": 3.486846303936058e-09, "12": 2.9525013832484877e-10, "13": 2.3025269287154537e-11, "14": 1.5443414899751462e-12, "2": 0.0754748254916607, "3": 0.023429402381465732, "4": 0.0056546606822187205, "5": 0.0011127012990988605, "6": 0.00018451177491899014, "7": 2.6412982898370476e-05, "8": 3.3243729762186214e-06, "9": 3.731874843202117e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3103 |
| Legacy raw p draw | 0.2706 |
| Legacy raw p away | 0.4190 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0245 |
| Legacy lambda away | 1.2438 |
| Legacy model home team | Maritimo |
| Legacy model away team | Santa Clara |
| Legacy home name match score | 95/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 57.3% |
| Market reference home draw last update utc | 2026-11-01T09:34:21Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.0% |
| Market reference draw away last update utc | 2026-11-01T09:34:21Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.7% |
| Market reference home away last update utc | 2026-11-01T09:34:21Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.63 |
| Market reference dc draw away odds | 1.28 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 65.5% |
| Market reference over 1 5 odds | 1.44 |
| Market reference over 1 5 opposite odds | 2.50 |
| Market reference over 1 5 last update utc | 2026-11-01T09:34:16Z |
| Market over 1 5 bookmakers | 0 |
| Market p btts yes | 46.7% |
| Market reference btts yes odds | 2.08 |
| Market reference btts yes opposite odds | 1.83 |
| Market reference btts yes last update utc | 2026-11-01T09:34:39Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,412.3721 |
| Elo away rating | 1,471.5616 |
| Elo rating diff | 0.8105 |
| Elo home expectancy | 0.5012 |

</details>


---

## 2026-11-02 — Benfica vs Alverca

The model's most likely 1X2 outcome is **Benfica win** at **83.0%**. Expected goals are 2.78 for Benfica and 0.67 for Alverca (3.45 combined). The most likely exact score is 2-0 at 12.5%. Goal-market probabilities: at least one goal: 97.3%; Over 2.5 goals: 67.5%; Under 3.5 goals: 54.3%; Double Chance 1X: 94.2%; Double Chance X2: 17.0%; Double Chance 12 (either team wins): 88.8%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 45.3%; BTTS No (at least one team does not score): 54.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Benfica win | 83.0% | 1.20 |
| Draw | 11.2% | 8.93 |
| Alverca win | 5.8% | 17.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Benfica expected goals | 2.78 |
| Alverca expected goals | 0.67 |
| Expected total goals | 3.45 |
| Over 0.5 | 97.3% |
| Under 0.5 | 2.7% |
| Over 1.5 | 85.9% |
| Under 1.5 | 14.1% |
| Over 2.5 | 67.5% |
| Under 2.5 | 32.5% |
| Over 3.5 | 45.7% |
| Under 3.5 | 54.3% |
| Over 4.5 | 26.8% |
| Under 4.5 | 73.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.50% |
| 2 | 3-0 | 11.56% |
| 3 | 1-0 | 9.31% |
| 4 | 2-1 | 8.42% |
| 5 | 4-0 | 8.02% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T20:15:00+00:00 |
| Fixture id | cdf1a22ce6d16f0903216518d909e02a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Benfica |
| Matched away-team name | Alverca |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7757 |
| Dc lambda away | 0.6735 |
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
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 37.06 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.09 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.08 |
| Fair Over 3.5 odds | 2.19 |
| Fair Under 3.5 odds | 1.84 |
| Fair Over 4.5 odds | 3.72 |
| Fair Under 4.5 odds | 1.37 |
| Goal margin distribution | {"-1": 0.04437340876113706, "-10": 1.7102079356664804e-10, "-11": 1.032717154394441e-11, "-12": 5.728489561259974e-13, "-13": 2.938048258247632e-14, "-14": 1.401112360511481e-15, "-15": 6.243043908267915e-17, "-16": 2.6102353802227465e-18, "-17": 1.0277786183870484e-19, "-18": 3.809142010122627e-21, "-19": 1.2293518470682707e-22, "-2": 0.011067944010575401, "-3": 0.002173692309776811, "-4": 0.00033634762014891786, "-5": 4.2754308470279984e-05, "-6": 4.60108947483149e-06, "-7": 4.2875660375685946e-07, "-8": 3.520221099137735e-08, "-9": 2.5817013484905152e-09, "0": 0.11194766043989761, "1": 0.2079455130875878, "10": 0.00028727600685728307, "11": 7.148953630063497e-05, "12": 1.634225060060618e-05, "13": 3.454150972972705e-06, "14": 6.788377823194753e-07, "15": 1.246522384740265e-07, "16": 2.1478008766623555e-08, "17": 3.4851748605011027e-09, "18": 5.323077743853677e-10, "19": 7.079824529073519e-11, "2": 0.2234766666028884, "3": 0.18087308707206076, "4": 0.11533865751402708, "5": 0.060419492099407335, "6": 0.02679591019041228, "7": 0.010290330127209386, "8": 0.0034817619758403346, "9": 0.001052315067576051} |
| Raw goal margin distribution | {"-1": 0.05167051408369037, "-10": 1.991447709180445e-10, "-11": 1.2025451224144184e-11, "-12": 6.670526534183981e-13, "-13": 3.4212035573725006e-14, "-14": 1.6315220754472857e-15, "-15": 7.269698163684382e-17, "-16": 3.0394826032312736e-18, "-17": 1.1967944554846718e-19, "-18": 4.4355466793255735e-21, "-19": 1.4315159394151561e-22, "-2": 0.012888042024321556, "-3": 0.0025311510258436603, "-4": 0.0003916592150373947, "-5": 4.9785156462598417e-05, "-6": 5.357728088670463e-06, "-7": 4.992646441058849e-07, "-8": 4.099113387024796e-08, "-9": 3.0062562154092055e-09, "0": 0.11947903940831202, "1": 0.2036693204550148, "10": 0.00028136846153063456, "11": 7.001942509748496e-05, "12": 1.600618847269415e-05, "13": 3.383119794068646e-06, "14": 6.648781585682091e-07, "15": 1.220888891817922e-07, "16": 2.10363348805826e-08, "17": 3.413505706209583e-09, "18": 5.213613944933943e-10, "19": 6.934234979957437e-11, "2": 0.21888109124716176, "3": 0.17715361195146753, "4": 0.11296683274998612, "5": 0.05917702534384687, "6": 0.026244878951324824, "7": 0.010078719723967922, "8": 0.0034101630041270567, "9": 0.0010306752549525447} |
| Unadjusted home-win probability | 81.3% |
| Unadjusted draw probability | 11.9% |
| Unadjusted away-win probability | 6.8% |
| Raw p over 1 5 | 85.6% |
| Raw p under 3 5 | 54.8% |
| Raw p btts yes | 45.7% |
| P home draw | 94.2% |
| P draw away | 17.0% |
| P home away | 88.8% |
| Raw p home draw | 93.2% |
| Raw p draw away | 18.7% |
| Raw p home away | 88.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.6750 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.19 |
| Reference draw odds | 8.80 |
| Reference away odds | 17.50 |
| Market reference 1x2 last update utc | 2026-11-01T09:34:39Z |
| Market reference home last update utc | 2026-11-01T09:34:39Z |
| Market reference draw last update utc | 2026-11-01T09:34:39Z |
| Market reference away last update utc | 2026-11-01T09:34:39Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.05 |
| Market reference over 2 5 last update utc | 2026-11-01T09:34:40Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:34:40Z |
| Home probability edge | -0.7% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0244 |
| Raw edge prob draw | 0.0108 |
| Raw edge prob away | 0.0136 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.027877368359582714, 0.02185455060122509, 0.006304752695910372, 0.0013816449011200287, 0.00022708376420885147, 2.985834402194571e-05, 3.2716294170085737e-06, 3.072668454860095e-07, 2.5250812214114942e-08, 1.8445162259576783e-09, 1.2126406355069257e-10, 7.24751410886588e-12, 3.9706120910996956e-13, 2.0080001723456717e-14, 9.429427970729083e-16, 4.132793689017248e-17, 1.6981395632840125e-18, 6.567107057254421e-20, 2.3985635436185776e-21, 8.299410861076034e-23], [0.0928797463817902, 0.053458620824706225, 0.017583357563524523, 0.0038532766460407587, 0.0006333150903040733, 8.327209083603681e-05, 9.12426428588101e-06, 8.569381024415603e-07, 7.042212142883823e-08, 5.144180889723784e-09, 3.381939771247295e-10, 2.0212629768260333e-11, 1.1073660698721286e-12, 5.600122117537651e-14, 2.6297780678435977e-15, 1.1525969800116787e-16, 4.735950254378487e-18, 1.8315039005503179e-19, 6.6893663336925026e-21, 2.314627008789076e-22], [0.12539449736791863, 0.08243812704784159, 0.025793931526784584, 0.005373211633063899, 0.000883127873549717, 0.00011611898347591776, 1.2723354045814528e-05, 1.19495956398195e-06, 9.820031024122568e-08, 7.173316410502145e-09, 4.715954703086016e-10, 2.8185554109441757e-11, 1.5441694939840125e-12, 7.809104840538734e-14, 3.6671008610379585e-15, 1.6072418541753364e-16, 6.604058140124841e-18, 2.5539453738808397e-19, 9.32800426851116e-21, 3.2276376477168734e-22], [0.11657112182204735, 0.07663737366942858, 0.02519186120518571, 0.005254826993515773, 0.0008209866389109038, 0.00010794827885395424, 1.1828076076639269e-05, 1.1108763129904207e-06, 9.129045188087722e-08, 6.668566473880006e-09, 4.384116861106742e-10, 2.620227945149248e-11, 1.4355141092750437e-12, 7.259617692925006e-14, 3.4090655505522847e-15, 1.49414838699693e-16, 6.139364024193101e-18, 2.3742371759104514e-19, 8.67163986271849e-21, 3.0005251372831845e-22], [0.08127645188636014, 0.05343359244023544, 0.01756442816340719, 0.003849128393061646, 0.0006021737620920029, 7.52643789933007e-05, 8.246845712085769e-06, 7.745321808114115e-07, 6.3650103936607e-08, 4.649499924970212e-09, 3.0567215752617875e-10, 1.8268918338138614e-11, 1.0008781901643973e-12, 5.0615963791882556e-14, 2.3768901582665088e-15, 1.0417595506391577e-16, 4.280526059334934e-18, 1.655380600087839e-19, 6.0460953713219e-21, 2.092045037762404e-22], [0.045334463822489776, 0.029804244737140686, 0.009797104999736524, 0.002146970836366638, 0.00035287085616104167, 4.4163675365082534e-05, 4.599934174131311e-06, 4.320193649624823e-07, 3.550282113995775e-08, 2.5934029014448734e-09, 1.7049813378035173e-10, 1.019005626173694e-11, 5.582708773528739e-13, 2.8232624900652707e-14, 1.325784263326689e-15, 5.810737250958894e-17, 2.3875962751113996e-18, 9.233399119349082e-20, 3.3723973613138823e-21, 1.1669030559068414e-22], [0.021072253631205604, 0.013853535509909138, 0.004553866175948575, 0.0009979496874577738, 0.00016402056080780982, 2.1566413382014735e-05, 2.2492933386319704e-06, 2.0081017540491193e-07, 1.6502333734746496e-08, 1.2054591385735185e-09, 7.925052191495135e-11, 4.736516812117946e-12, 2.594940919243754e-13, 1.3123019054790517e-14, 6.162477704924744e-16, 2.7009325535632966e-17, 1.1097966102581339e-18, 4.2918457993221406e-20, 1.5675494215851037e-21, 5.423969996287782e-23], [0.00839550252546798, 0.00551945674134562, 0.001814328721072446, 0.00039759815290636166, 6.534825636548956e-05, 8.592383196539578e-06, 9.414820060800273e-07, 8.416536400664943e-08, 6.57477776088504e-09, 4.802730367318293e-10, 3.157459892644445e-11, 1.8870994794391464e-12, 1.0338634596106419e-13, 5.2284080072528444e-15, 2.455223728809864e-16, 1.0760921195908175e-17, 4.421596478119505e-19, 1.7099358653204795e-20, 6.245352470617859e-22, 2.160991159220938e-23], [0.0029267825787705416, 0.0019241551992681368, 0.0006324988500556584, 0.0001386079444020916, 2.2781261479387714e-05, 2.995417769629101e-06, 3.2821300753135896e-07, 3.082530525839573e-08, 2.4112199100116183e-09, 1.6742949605408983e-10, 1.100732038246078e-11, 6.578676933363894e-13, 3.6041839702111216e-14, 1.8226917833580248e-15, 8.559232773340394e-17, 3.7513986318467734e-18, 1.5414266749674993e-19, 5.961061278051303e-21, 2.1772119958080794e-22, 7.533499345034677e-24], [0.000906946571813965, 0.000596254048480541, 0.00019599770338090005, 4.2951601842069476e-05, 7.0594198387662555e-06, 9.282151318725384e-07, 1.0170610696007373e-07, 9.552094894922091e-09, 7.849794339560984e-10, 5.4580208601368045e-11, 3.410930336316401e-12, 2.0385895881245656e-13, 1.1168586008677672e-14, 5.648127320357553e-16, 2.6523209743853692e-17, 1.162477238090657e-18, 4.776547628459744e-20, 1.847203864652175e-21, 6.746708723884294e-23, 2.3344683866514208e-24], [0.0002529388008123136, 0.00016628960149274466, 5.466190136865244e-05, 1.1978794562475601e-05, 1.968805268073123e-06, 2.58870400581703e-07, 2.8364869033373235e-08, 2.6639887100897618e-09, 2.1892332234087947e-10, 1.5991866593209664e-11, 1.000733827083045e-12, 5.685433098196494e-14, 3.114812757000617e-15, 1.5752091640736136e-16, 7.397071751300406e-18, 3.24203881146126e-19, 1.3321338507835848e-20, 5.15167645924827e-22, 1.8815931027073887e-23, 6.510611017282581e-25], [6.41293032975371e-05, 4.2160539447120094e-05, 1.3858805530953235e-05, 3.0370656742612693e-06, 4.991646586627749e-07, 6.563318233637635e-08, 7.191539152531462e-09, 6.754192690955627e-10, 5.550512650576017e-11, 4.054527260175766e-12, 2.6655685888081253e-13, 1.516409857292967e-14, 7.897197716096945e-16, 3.993735477337605e-17, 1.8754301685994804e-18, 8.219762629334974e-20, 3.3774500185602865e-21, 1.306139750346405e-22, 4.770531621821533e-24, 1.6506797187253658e-25], [1.490421227401648e-05, 9.798478966651363e-06, 3.2209078982084218e-06, 7.05840687046063e-07, 1.1601024258566515e-07, 1.5253726946354496e-08, 1.6713767434667566e-09, 1.5697335918115197e-10, 1.2899877984012952e-11, 9.423076791599399e-13, 6.195015076683768e-14, 3.702536255032665e-15, 1.9308009141273264e-16, 9.28179135898958e-18, 4.358664120864489e-19, 1.9103448933670435e-20, 7.849489926305914e-22, 3.0355832821656965e-23, 1.1087133696377905e-24, 3.836324372674343e-26], [3.1974180829145235e-06, 2.102079147627822e-06, 6.909851368051196e-07, 1.514248277550665e-07, 2.488781296368003e-08, 3.2723998741713354e-09, 3.5856240669895113e-10, 3.36756782548424e-11, 2.7674259045130103e-12, 2.021543680150001e-13, 1.3290238266835141e-14, 7.943094312422683e-16, 4.3516916067909625e-17, 2.0947595553153677e-18, 9.350693093454688e-20, 4.098285232627819e-21, 1.6839602503368217e-22, 6.512272302717262e-24, 2.3785357532979044e-25, 8.230111525249401e-27], [6.369497078929645e-07, 4.187499614779736e-07, 1.3764943139535214e-07, 3.016496351281518e-08, 4.9578393523254815e-09, 6.518866441333398e-10, 7.142832569462285e-11, 6.708448151380749e-12, 5.512920349434663e-13, 4.027066912033953e-14, 2.64751532717057e-15, 1.5823240723816054e-16, 8.668896671964768e-18, 4.383995618804206e-19, 1.9595732296387958e-20, 8.164092133378113e-22, 3.354575353429236e-23, 1.2972935766830374e-24, 4.7382219465497806e-26, 1.6395000578578586e-27], [1.1842615673230424e-07, 7.785692960545375e-08, 2.5592747644807568e-08, 5.60848156852157e-09, 9.217962625877338e-10, 1.2120333667348794e-10, 1.3280455252613074e-11, 1.2472817278369123e-12, 1.0250008144513829e-13, 7.487405228171506e-15, 4.922446171203322e-16, 2.941967886554891e-17, 1.6117820657557605e-18, 8.151032111839622e-20, 3.827667509405987e-21, 1.5968435509234634e-22, 6.237061759392382e-24, 2.412019199259828e-25, 8.809634542902445e-27, 3.0482734886052266e-28], [2.0642457753029933e-08, 1.3570974728109238e-08, 4.460984183047357e-09, 9.775952123360015e-10, 1.6067514924410016e-10, 2.112653847632852e-11, 2.3148706675734725e-12, 2.1740940585616753e-13, 1.786643811887068e-14, 1.305103959860122e-15, 8.580147320014396e-17, 5.128043456333353e-18, 2.809442112916167e-19, 1.42077848893278e-20, 6.671876132412341e-22, 2.924195153675536e-23, 1.1436833335789129e-24, 4.2043080510301135e-26, 1.5355772228812957e-27, 5.31334111014431e-29], [3.386462218806059e-09, 2.22636246802385e-09, 7.318389396903992e-10, 1.603776687577632e-10, 2.6359279932948065e-11, 3.465877233234869e-12, 3.7976204921670586e-13, 3.566671894178475e-14, 2.9310471843068728e-15, 2.1410654218399719e-16, 1.4076010269055232e-17, 8.412721793614687e-19, 4.6089810065939335e-20, 2.3308332426437904e-21, 1.0945429425743599e-22, 4.7972370958998095e-24, 1.9711552813898927e-25, 7.255900833835187e-27, 2.519164293110083e-28, 8.716708611159274e-30], [5.246956713152677e-10, 3.4495076994030093e-10, 1.133905234858605e-10, 2.4848784110309723e-11, 4.08408515618444e-12, 5.370001683437116e-13, 5.884001960726812e-14, 5.526172102215463e-15, 4.541340403817732e-16, 3.317349157488321e-17, 2.1809254556415612e-18, 1.3034601964776967e-19, 7.141117269534251e-21, 3.61137385848085e-22, 1.6958758342206452e-23, 7.432799706175633e-25, 3.054091783135693e-26, 1.1810894779311318e-27, 4.106101847629256e-29, 1.350559664003657e-30], [7.701718341662043e-11, 5.063342080105233e-11, 1.664396949021106e-11, 3.647415955817587e-12, 5.994803326173377e-13, 7.882329266488886e-14, 8.6368019217136e-15, 8.111563209988974e-16, 6.665983082371998e-17, 4.8693538461790404e-18, 3.2012601783824746e-19, 1.913277324677363e-20, 1.0482052142123538e-21, 5.300936486618858e-23, 2.489282594014513e-24, 1.0910196701919577e-25, 4.4829328674149216e-27, 1.7336560967854042e-28, 6.331988004258374e-30, 2.085479400817823e-31]] |
| Legacy trial inputs | {"lambda_home": 2.788905197650355, "lambda_away": 0.6574301805761124, "rho": 0.05, "max_goals": 19, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8276 |
| Legacy p draw | 0.1130 |
| Legacy p away | 0.0594 |
| Legacy p over 1 5 | 0.8574 |
| Legacy p under 3 5 | 0.5457 |
| Legacy p btts yes | 0.4472 |
| Legacy p over 2 5 | 0.6722 |
| Legacy goal margin distribution | {"-1": 0.0457121783057431, "-10": 1.43095895114513e-10, "-11": 8.436486899795814e-12, "-12": 4.568833204342936e-13, "-13": 2.2876812305439113e-14, "-14": 1.0650501397174693e-15, "-15": 4.6328162526305544e-17, "-16": 1.890918010121284e-18, "-17": 7.26832006710084e-20, "-18": 2.6300262444974853e-21, "-19": 8.299410861076034e-23, "-2": 0.011157801353252957, "-3": 0.0021437183236815436, "-4": 0.0003242564100847668, "-5": 4.0273683163500995e-05, "-6": 4.233752523188295e-06, "-7": 3.8531953557301717e-07, "-8": 3.0893820591578584e-08, "-9": 2.212383240506694e-09, "0": 0.11303342106756523, "1": 0.20473427340597514, "10": 0.0002984767543790826, "11": 7.464987567266236e-05, "12": 1.7149713535285827e-05, "13": 3.642765292166544e-06, "14": 7.194321622586723e-07, "15": 1.327544186645468e-07, "16": 2.298585816049546e-08, "17": 3.7480569582365705e-09, "18": 5.753290921163201e-10, "19": 7.701718341662043e-11, "2": 0.2219162209692684, "3": 0.18086821705016873, "4": 0.11605589948236003, "5": 0.06114826163943351, "6": 0.02726919696851065, "7": 0.010528149006439776, "8": 0.0035808549496301467, "9": 0.001087826372725146} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.8178 |
| Legacy raw p draw | 0.1173 |
| Legacy raw p away | 0.0649 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.7889 |
| Legacy lambda away | 0.6574 |
| Legacy model home team | Benfica |
| Legacy model away team | Alverca |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 92.5% |
| Market reference home draw last update utc | 2026-11-01T09:34:16Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 20.0% |
| Market reference draw away last update utc | 2026-11-01T09:34:16Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.5% |
| Market reference home away last update utc | 2026-11-01T09:34:16Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.04 |
| Market reference dc draw away odds | 4.80 |
| Market reference dc home away odds | 1.10 |
| Market p over 1 5 | 88.6% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-11-01T09:34:16Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 51.2% |
| Market reference under 3 5 odds | 1.85 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market reference under 3 5 last update utc | 2026-11-01T09:33:54Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 46.7% |
| Market reference btts yes odds | 2.06 |
| Market reference btts yes opposite odds | 1.82 |
| Market reference btts yes last update utc | 2026-11-01T09:34:39Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,677.3736 |
| Elo away rating | 1,429.6982 |
| Elo rating diff | 307.6754 |
| Elo home expectancy | 0.8546 |

</details>


---

## 2026-11-02 — Gil Vicente vs Vitória SC

The model's most likely 1X2 outcome is **Vitória SC win** at **35.2%**. Expected goals are 1.17 for Gil Vicente and 1.02 for Vitória SC (2.19 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 36.8%; Under 3.5 goals: 82.2%; Double Chance 1X: 64.8%; Double Chance X2: 65.0%; Double Chance 12 (either team wins): 70.1%; Under 4.5 goals: 93.0%; BTTS Yes (both teams score): 44.0%; BTTS No (at least one team does not score): 56.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gil Vicente win | 35.0% | 2.86 |
| Draw | 29.9% | 3.35 |
| Vitória SC win | 35.2% | 2.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gil Vicente expected goals | 1.17 |
| Vitória SC expected goals | 1.02 |
| Expected total goals | 2.19 |
| Over 0.5 | 88.7% |
| Under 0.5 | 11.3% |
| Over 1.5 | 63.5% |
| Under 1.5 | 36.5% |
| Over 2.5 | 36.8% |
| Under 2.5 | 63.2% |
| Over 3.5 | 17.8% |
| Under 3.5 | 82.2% |
| Over 4.5 | 7.0% |
| Under 4.5 | 93.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.66% |
| 2 | 0-1 | 13.13% |
| 3 | 1-0 | 12.05% |
| 4 | 0-0 | 11.32% |
| 5 | 1-2 | 7.41% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T20:15:00+00:00 |
| Fixture id | 97ce048d06fc45fc59e114548540828f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 11.00 |
| Matched home-team name | Gil Vicente |
| Matched away-team name | Guimaraes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1706 |
| Dc lambda away | 1.0202 |
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
| P btts yes | 44.0% |
| P btts no | 56.0% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.83 |
| Fair Over 1.5 odds | 1.57 |
| Fair Under 1.5 odds | 2.74 |
| Fair Over 2.5 odds | 2.72 |
| Fair Under 2.5 odds | 1.58 |
| Fair Over 3.5 odds | 5.63 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 14.34 |
| Fair Under 4.5 odds | 1.07 |
| Goal margin distribution | {"-1": 0.22166427644916994, "-10": 4.5584370749355456e-08, "-11": 4.18953789020729e-09, "-12": 3.5222851783099885e-10, "-13": 2.531564932441311e-11, "-2": 0.0925322302538776, "-3": 0.02875990470583403, "-4": 0.0069363223528642465, "-5": 0.0013624887347542208, "-6": 0.00022538650373693547, "-7": 3.2172703956019815e-05, "-8": 4.036647302084746e-06, "-9": 4.5163717612537905e-07, "0": 0.2989110723313515, "1": 0.20405212027823064, "10": 1.4529114366557992e-07, "11": 1.53220425696544e-08, "12": 1.4780952495827693e-09, "13": 1.2189737150977407e-10, "2": 0.09815158045755758, "3": 0.035004112730532146, "4": 0.009686976874518055, "5": 0.002183329481091879, "6": 0.00041442088079936154, "7": 6.787793932899518e-05, "8": 9.772130442832592e-06, "9": 1.254542844309103e-06} |
| Raw goal margin distribution | {"-1": 0.20387933821321003, "-10": 4.192696942475234e-08, "-11": 3.853395892912402e-09, "-12": 3.23967931439197e-10, "-13": 2.3284481890263427e-11, "-2": 0.08510802989889525, "-3": 0.026452392024679743, "-4": 0.006379795759555979, "-5": 0.001253171264285083, "-6": 0.00020730291754798307, "-7": 2.9591369868689575e-05, "-8": 3.7127722776651305e-06, "-9": 4.1540066832573326e-07, "0": 0.2776023849911495, "1": 0.23295341422184015, "10": 1.6586971959390914e-07, "11": 1.749220799365624e-08, "12": 1.6874479641078437e-09, "13": 1.3916252788332051e-10, "2": 0.1120534584383685, "3": 0.0399619840326334, "4": 0.011059009498798815, "5": 0.0024925693312965475, "6": 0.0004731181375395539, "7": 7.749195497440415e-05, "8": 1.1156223947955217e-05, "9": 1.432232306485682e-06} |
| Unadjusted home-win probability | 39.9% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.3% |
| Raw p over 1 5 | 63.6% |
| Raw p under 3 5 | 82.1% |
| Raw p btts yes | 43.4% |
| P home draw | 64.8% |
| P draw away | 65.0% |
| P home away | 70.1% |
| Raw p home draw | 67.7% |
| Raw p draw away | 60.1% |
| Raw p home away | 72.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.3680 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 2.96 |
| Reference draw odds | 3.15 |
| Reference away odds | 2.68 |
| Market reference 1x2 last update utc | 2026-11-01T09:34:39Z |
| Market reference home last update utc | 2026-11-01T09:34:39Z |
| Market reference draw last update utc | 2026-11-01T09:34:39Z |
| Market reference away last update utc | 2026-11-01T09:34:39Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.24 |
| Reference Under 2.5 odds | 1.67 |
| Market reference over 2 5 last update utc | 2026-11-01T09:34:39Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:34:39Z |
| Home probability edge | +2.1% |
| Draw probability edge | -0.9% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | 0.0707 |
| Raw edge prob draw | -0.0304 |
| Raw edge prob away | -0.0403 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.1078753863399605, 0.12644327206317985, 0.06281197396181185, 0.022017239895730175, 0.00578821387926194, 0.001217352222921565, 0.00021335689868590892, 3.205164597141915e-05, 4.213102617393404e-06, 4.922675576097201e-07, 5.1765796671353625e-08, 4.948708857789031e-09, 4.33662975479441e-10, 3.507928074656599e-11], [0.12279607183648278, 0.1341985818392135, 0.0734107507861492, 0.025732388413186667, 0.006764906430830649, 0.0014227659953847743, 0.0002493583488947423, 3.745998169273046e-05, 4.924013795044541e-06, 5.753318788192258e-07, 6.050066188013167e-08, 5.78374487789908e-09, 5.068384674147703e-10, 4.0998493984748435e-11], [0.06817372628998447, 0.07169002301495911, 0.043403348973317754, 0.015037212125201852, 0.003953202142534622, 0.0008314204547822365, 0.00014571730875936908, 2.1890455012372804e-05, 2.877441407870289e-06, 3.3620616031748485e-07, 3.535471607992838e-08, 3.3798416692035206e-09, 2.9618072855695256e-10, 2.39582521825508e-11], [0.026559078443015374, 0.02792895516282788, 0.014684744016266594, 0.005927064346539672, 0.0015400860642129555, 0.0003239042704481449, 5.676845970518323e-05, 8.52807002735776e-06, 1.1209918575044201e-06, 1.309789895731269e-07, 1.3773468589691913e-08, 1.3167166429413135e-09, 1.1538590643547081e-10, 9.333641179701692e-12], [0.0077601521083996376, 0.008160408907155253, 0.004290655170270366, 0.001503986871215545, 0.00045527999767161037, 9.463982015154755e-05, 1.6586866265596297e-05, 2.4917702150461536e-06, 3.275364898362831e-07, 3.827003577224106e-08, 4.024394579262323e-09, 3.8472424616724907e-10, 3.371397795394146e-11, 2.7271456513490537e-12], [0.0018139171771251348, 0.0019074762559140761, 0.0010029304845777362, 0.0003515533692845589, 9.242148884378579e-05, 2.238192688030466e-05, 3.877140707238972e-06, 5.824453865573948e-07, 7.65608788011027e-08, 8.945530227599824e-09, 9.406927020092467e-10, 8.992838140684464e-11, 7.880562502593043e-12, 6.374638373582521e-13], [0.0003533323702409756, 0.0003715567144849897, 0.0001953605212915051, 6.847897291120093e-05, 1.800275344772367e-05, 3.786261597349573e-06, 7.641064800130042e-07, 1.1345435809501046e-07, 1.4913270085131072e-08, 1.7424970876507068e-09, 1.8323724272576613e-10, 1.751712181521664e-11, 1.535052351335259e-12, 1.2417138524134543e-13], [5.89932891098793e-05, 6.203607290037054e-05, 3.2617899416762676e-05, 1.143342695757791e-05, 3.0057864163170723e-06, 6.32164058180519e-07, 1.1079501920191939e-07, 1.9165348182102996e-08, 2.4899582597140263e-09, 2.909318339409247e-10, 3.059376537860343e-11, 2.924704099183629e-12, 2.5629632263627534e-13, 2.0731976591108794e-14], [8.618463510503557e-06, 9.062990701043079e-06, 4.7652229627177586e-06, 1.670335296110675e-06, 4.3912216016885414e-07, 9.235428216136291e-08, 1.6186295840510673e-08, 2.431594324177183e-09, 3.680405326128113e-10, 4.250289198477393e-11, 4.469512626653073e-12, 4.272766604161606e-13, 3.744291152172892e-14, 3.02878151815344e-15], [1.1191919081362079e-06, 1.1769181181493992e-06, 6.188108789738273e-07, 2.1690939980230168e-07, 5.70243138751258e-08, 1.1993108185786853e-08, 2.101949066132306e-09, 3.15766341433408e-10, 4.150663590768865e-11, 5.5843103010115315e-12, 5.80409995234807e-13, 5.548605970083048e-14, 4.862328829391371e-15, 3.9331694825865454e-16], [1.308042289834954e-07, 1.3755091142287191e-07, 7.232278872134201e-08, 2.535102925079388e-08, 6.664649159383391e-09, 1.4016803176945207e-09, 2.4566280810221267e-10, 3.6904817243469e-11, 4.851038922042608e-12, 5.668053448698188e-13, 6.863228423903017e-14, 6.4848675242709455e-15, 5.682789242569791e-16, 4.5968452585392886e-17], [1.389780851993114e-08, 1.4614636266372481e-08, 7.684218446816971e-09, 2.6935195677439616e-09, 7.081117987501572e-10, 1.4892702485890326e-10, 2.610140890707695e-11, 3.921097104417787e-12, 5.154176633676583e-13, 6.022245773160914e-14, 6.3328640163105285e-15, 6.971110936192059e-16, 6.03790239552001e-17, 4.884098602576022e-18], [1.3535749281797915e-09, 1.423390256547219e-09, 7.484032764843162e-10, 2.6233492497980964e-10, 6.896643997950663e-11, 1.4504724733278942e-11, 2.542142715243216e-12, 3.8189465079236765e-13, 5.01990242328458e-14, 5.865357029633134e-15, 6.167883190904965e-16, 5.896375627022942e-17, 5.949745823628309e-18, 4.756860339328963e-19], [1.2169035916059725e-10, 1.2796696210815037e-10, 6.72836513267976e-11, 2.3584679781333133e-11, 6.2002853897565525e-12, 1.3040173289053869e-12, 2.285460919931816e-13, 3.4333450072784764e-14, 4.513039626569622e-15, 5.273128134110825e-16, 5.545108033074764e-17, 5.301014763645989e-18, 4.645360843656986e-19, 4.326837839757355e-20]] |
| Legacy trial inputs | {"lambda_home": 1.1687381585998422, "lambda_away": 1.0515784733552291, "rho": 0.05, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3599 |
| Legacy p draw | 0.2919 |
| Legacy p away | 0.3482 |
| Legacy p over 1 5 | 0.6429 |
| Legacy p under 3 5 | 0.8160 |
| Legacy p btts yes | 0.4461 |
| Legacy p over 2 5 | 0.3777 |
| Legacy goal margin distribution | {"-1": 0.21652995398700883, "-10": 5.7855055918989354e-08, "-11": 5.4795055773863524e-09, "-12": 4.746614694641894e-10, "-13": 3.507928074656599e-11, "-2": 0.09283865330836091, "-3": 0.029672905345665128, "-4": 0.007365561921653287, "-5": 0.0014897612471911057, "-6": 0.00025382941665482773, "-7": 3.732603212435093e-05, "-8": 4.825140280377291e-06, "-9": 5.562661742111422e-07, "0": 0.29188282706910573, "1": 0.2107711467580585, "10": 1.4619085320613355e-07, "11": 1.5388482427805154e-08, "12": 1.4815418902879418e-09, "13": 1.2169035916059725e-10, "2": 0.10076354141684722, "3": 0.035793997087733266, "4": 0.009874873677465784, "5": 0.002219820578805007, "6": 0.0004203573916565266, "7": 6.870116456421657e-05, "8": 9.870468207399348e-06, "9": 1.2646955732162664e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3915 |
| Legacy raw p draw | 0.2757 |
| Legacy raw p away | 0.3328 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1687 |
| Legacy lambda away | 1.0516 |
| Legacy model home team | Gil Vicente |
| Legacy model away team | Guimaraes |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 62.7% |
| Market reference home draw last update utc | 2026-11-01T09:34:21Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.2% |
| Market reference draw away last update utc | 2026-11-01T09:34:21Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.2% |
| Market reference home away last update utc | 2026-11-01T09:34:21Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.49 |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 68.5% |
| Market reference over 1 5 odds | 1.40 |
| Market reference over 1 5 opposite odds | 2.80 |
| Market reference over 1 5 last update utc | 2026-11-01T09:34:16Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 80.0% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 4.20 |
| Market reference under 3 5 last update utc | 2026-11-01T09:33:54Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 52.6% |
| Market reference btts yes odds | 1.69 |
| Market reference btts yes opposite odds | 1.84 |
| Market reference btts yes last update utc | 2026-11-01T09:34:39Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,467.0612 |
| Elo away rating | 1,413.2222 |
| Elo rating diff | 113.8391 |
| Elo home expectancy | 0.6582 |

</details>


---
