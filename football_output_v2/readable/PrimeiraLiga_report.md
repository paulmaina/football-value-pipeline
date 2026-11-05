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
| Training as of utc | 2026-11-05T13:37:06.185918+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1314, 'tuning_matches': 198, 'audit_matches': 105, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.871131149064499, 'audit_candidate_poisson_score': 0.8646865932043838, 'audit_gain': 0.006444555860115164, 'audit_gain_lower95': -0.0029289421499673917, 'audit_baseline_briers': [0.5561732722325169, 0.18693068045494893, 0.22413228109469926, 0.24642823314843584], 'audit_candidate_briers': [0.5573866098789683, 0.18683238764055768, 0.22226394985760883, 0.24657985484468817], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1469.259 |
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
| Additional event odds calls used before this league | 25.00 |
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

The model's most likely 1X2 outcome is **Famalicão win** at **46.2%**. Expected goals are 1.47 for Famalicão and 1.00 for Arouca (2.47 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 44.5%; Under 3.5 goals: 76.2%; Double Chance 1X: 73.3%; Double Chance X2: 53.8%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 49.0%; BTTS No (at least one team does not score): 51.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Famalicão win | 46.2% | 2.17 |
| Draw | 27.1% | 3.69 |
| Arouca win | 26.7% | 3.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Famalicão expected goals | 1.47 |
| Arouca expected goals | 1.00 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 70.2% |
| Under 1.5 | 29.8% |
| Over 2.5 | 44.5% |
| Under 2.5 | 55.5% |
| Over 3.5 | 23.8% |
| Under 3.5 | 76.2% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.80% |
| 2 | 1-0 | 12.26% |
| 3 | 0-1 | 9.13% |
| 4 | 2-1 | 8.69% |
| 5 | 2-0 | 8.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Famalicão win | 46.2% | 45.1% | 2.14 | -1.2% |
| Draw | 27.1% | 28.0% | 3.38 | -8.4% |
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
| Market best home last update utc | 2026-11-05T13:36:57Z |
| Market best draw last update utc | 2026-11-05T13:36:57Z |
| Market best away last update utc | 2026-11-05T13:36:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
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
| P btts yes | 49.0% |
| P btts no | 51.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.94 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.36 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.20 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.57 |
| Fair Under 4.5 odds | 1.12 |
| Score matrix json | [[0.08376008224844518,0.09131712247926352,0.042758247301395436,0.01433504372952106,0.003604453380866973,0.0007250530612941449,0.00012153991330153834,1.7463096916338455e-05,2.1954909907556594e-06,2.453519601213464e-07,2.467686095272961e-08,2.2563039872085615e-09,1.8911098071758402e-10,1.4630992126557586e-11,1.0511050507925001e-12,7.047827176461089e-14],[0.12261596342314932,0.127963938751655,0.06327888173269709,0.021214750230508176,0.0053343107726367845,0.0010730221608981816,0.00017986962247068788,2.584402575405716e-05,3.249155976154696e-06,3.6310182589961804e-07,3.651983568819079e-08,3.3391544829510335e-09,2.7986954888096696e-10,2.1652730849382715e-11,1.5555537561888917e-12,1.0430236282328042e-13],[0.08638676843967213,0.08688556112969782,0.0501237188845907,0.015698090491904054,0.003947182611670324,0.0007939946875912192,0.00013309652857609156,1.912357442600775e-05,2.4042491182685716e-06,2.686812363480396e-07,2.7023258777671384e-08,2.4708445147957224e-09,2.0709258683346484e-10,1.602217912429838e-11,1.1510493107082666e-12,7.717969395485286e-14],[0.04261523369461954,0.04286129182868965,0.021554385344788613,0.008289723767716228,0.001947174462824575,0.00039168346929907056,6.565750486631208e-05,9.433801124415146e-06,1.1860339249366532e-06,1.3254244698743435e-07,1.3330774015523706e-08,1.2188859280529901e-09,1.0216030931281457e-10,7.903859815706071e-12,5.678211635398647e-13,3.807331555251023e-14],[0.015766808178343358,0.015857844905453795,0.007974703636936406,0.0026735830531043133,0.0007711863952191316,0.00014491527070626385,2.4292000652022487e-05,3.4903230564724805e-06,4.388094999428548e-07,4.903812923130746e-08,4.932127282881554e-09,4.5096410256973235e-10,3.7797328812460304e-11,2.9242745088709407e-12,2.1008279408466852e-13,1.4086386744507209e-14],[0.0046667300602237305,0.004693675515904114,0.0023603882766192797,0.0007913390117579016,0.0001989770404724113,4.591542765656606e-05,7.19005447288185e-06,1.033081353136849e-06,1.298807888655515e-07,1.4514523750927242e-08,1.459832985314556e-09,1.334783622492903e-10,1.1187421611911978e-11,8.655397846241759e-13,6.218124043884491e-14,4.169351444943882e-15],[0.0011510662784256288,0.00115771247501087,0.0005821985231940718,0.00019518670235524904,4.907842504559688e-05,9.872360261806516e-06,1.898433617953795e-06,2.548133474874988e-07,3.20355783062558e-08,3.580061118062451e-09,3.6007322040144786e-10,3.292293312488545e-11,2.7594190351315507e-12,2.134885981960796e-13,1.5337233586722395e-14,1.0283859981714885e-15],[0.00024335551450316035,0.0002447606365363614,0.0001230869358354047,4.126587779185458e-05,1.0376036203850707e-05,2.08718937901516e-06,3.4987345025012006e-07,5.766849516109278e-08,6.772880751739328e-09,7.568874457259482e-10,7.61257674314414e-11,6.9604830579504275e-12,5.833893769720405e-13,4.513521821317275e-14,3.2425590433045878e-15,2.1741876066004344e-16],[4.501840519999107e-05,4.5278339120844364e-05,2.276988694329173e-05,7.633786360501383e-06,1.919465861081451e-06,3.8610975134653034e-07,6.472318814815382e-08,9.299556636686464e-09,1.3412135357933424e-09,1.4001682185851795e-10,1.4082527167652929e-11,1.2876217221961327e-12,1.0792136523192115e-13,8.349576735333196e-15,5.998419111003364e-16,4.0220357798165295e-17],[7.402637744986187e-06,7.445380188774738e-06,3.7441847126009014e-06,1.2552678132058636e-06,3.156289160029325e-07,6.349026817648405e-08,1.0642809611599948e-08,1.5291800912215715e-09,1.9225118715219353e-10,2.464632618086579e-11,2.31567170567121e-12,2.1173111574363588e-13,1.774613667914691e-14,1.3729693804357226e-15,9.863548813890191e-17,6.613666953124475e-18],[1.09553283387201e-06,1.1018583832482447e-06,5.54110228008135e-07,1.857698771767072e-07,4.671062568674816e-08,9.396066080065526e-09,1.575053079161327e-09,2.2630676477060992e-10,2.84516810266384e-11,3.179551060799569e-12,3.6685249304615677e-13,3.1334559009943936e-14,2.6262902597865964e-15,2.0318879404668908e-16,1.4597285395242836e-17,9.787712905915858e-19],[1.4739122009762137e-07,1.4824224930598913e-07,7.454909615628349e-08,2.4993179581561514e-08,6.2843722238428514e-09,1.2641315721811847e-09,2.1190510031142084e-10,3.044694704219381e-11,3.827843265567068e-12,4.2777167030001157e-13,4.3024160158693865e-14,4.512792733548222e-15,3.5333685468131667e-16,2.733669255613076e-17,1.9638952279630077e-18,1.3168231043057117e-19],[1.817729555823594e-08,1.8282250313607028e-08,9.193905536127552e-09,3.0823302222019058e-09,7.750318589879391e-10,1.5590137049422318e-10,2.613358947776628e-11,3.754926208395272e-12,4.720758695309728e-13,5.275573455008705e-14,5.306034340657981e-15,4.851519187154911e-16,4.6646834590684864e-17,3.3713483058780673e-18,2.422010210679357e-19,1.623996514108846e-20],[2.069306478317973e-09,2.0812545458687186e-09,1.046635800468799e-09,3.5089300697582306e-10,8.822976121879192e-11,1.7747839050577377e-11,2.9750523577497656e-12,4.274614506731576e-13,5.3741198846019916e-14,6.005721969099836e-15,6.040398694142572e-16,5.522977855259063e-17,4.6290560341636986e-18,4.1084192611099796e-19,2.757220623636855e-20,1.8487604476941084e-21],[2.1874376486146297e-10,2.2000677993740936e-10,1.1063854379822608e-10,3.709245499093089e-11,9.326656222288607e-12,1.8761015696593384e-12,3.1448901369271063e-13,4.5186408119397466e-14,5.680914010041836e-15,6.348572567655342e-16,6.385228894151163e-17,5.838269883965513e-18,4.893316457843931e-19,3.785823239655602e-20,3.1200242404897366e-21,1.954301235186253e-22],[2.158158437266237e-11,2.1706195313882775e-11,1.0915762876085426e-11,3.6595966403108506e-12,9.2018174005379e-13,1.8509896427416062e-13,3.102795267139671e-14,4.458158064271923e-15,5.604874045173624e-16,6.263595883594559e-17,6.299761559153924e-18,5.760123684941352e-19,4.827818615263357e-20,3.735149375268321e-21,2.6833685233707453e-22,2.064023953353535e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17239363622046083, "-10": 2.823122613447534e-08, "-11": 2.5527776227641114e-09, "-12": 2.119528341932275e-10, "-13": 1.626372557670133e-11, "-14": 1.1554074136157806e-12, "-15": 7.047827176461089e-14, "-2": 0.06833722150164083, "-3": 0.020532630555953175, "-4": 0.004820459562632368, "-5": 0.0009252828235927655, "-6": 0.00014992579903165733, "-7": 2.0994727271152276e-05, "-8": 2.5868736397842517e-06, "-9": 2.844477881177811e-07, "0": 0.27095652294362715, "1": 0.2339387017199554, "10": 1.2533293934762889e-06, "11": 1.6675811884842816e-07, "12": 2.0372848244543197e-08, "13": 2.300229021131468e-09, "14": 2.4044996017534576e-10, "15": 2.158158437266237e-11, "2": 0.13806533481273373, "3": 0.06103942659800065, "4": 0.02108593265734083, "5": 0.005955488498126998, "6": 0.0014199000710425412, "7": 0.0002925702515081759, "8": 5.304368189500071e-05, "9": 8.582217691503655e-06} |
| Raw goal margin distribution | {"-1": 0.1701071848421616, "-10": 2.64333930906758e-08, "-11": 2.375048073316966e-09, "-12": 1.9594119463186562e-10, "-13": 1.493924365730974e-11, "-14": 1.05463387372491e-12, "-15": 6.398875762607844e-14, "-2": 0.06713293693427463, "-3": 0.020065234412148268, "-4": 0.004684022651377984, "-5": 0.0008937757285711744, "-6": 0.0001439421811591624, "-7": 2.0032563340991433e-05, "-8": 2.4529374449224207e-06, "-9": 2.680264194344144e-07, "0": 0.25036197027583307, "1": 0.24736964343537307, "10": 1.2575871841956616e-06, "11": 1.66263191207049e-07, "12": 2.0183104916949955e-08, "13": 2.2642759602152557e-09, "14": 2.352019836735672e-10, "15": 2.099817065549352e-11, "2": 0.14534921307697155, "3": 0.06392338937867739, "4": 0.021957003040086125, "5": 0.006164830651943987, "6": 0.0014608956381262958, "7": 0.00029916181305100607, "8": 5.390072710554213e-05, "9": 8.666111537252372e-06} |
| Research history json | {"away": [{"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 2.04, "date": "2026-10-24T00:00:00+00:00", "home": "Alverca", "home_goals": 0.0, "home_xg": 0.39, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": 1.45, "date": "2026-10-11T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.74, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 2.0, "away_xg": 2.08, "date": "2026-09-19T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-13T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 1.08, "date": "2026-09-07T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-08-29T00:00:00+00:00", "home": "Arouca", "home_goals": 2.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 0.54, "date": "2026-08-23T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.99, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 0.0, "away_xg": 0.49, "date": "2026-08-16T00:00:00+00:00", "home": "Arouca", "home_goals": 4.0, "home_xg": 2.14, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 0.49, "date": "2026-08-08T00:00:00+00:00", "home": "Guimaraes", "home_goals": 0.0, "home_xg": 2.22, "source": "pipeline training history"}], "h2h": [{"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2026-03-06T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": null, "date": "2025-10-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2025-04-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2024-11-09T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2024-02-23T00:00:00+00:00", "home": "Arouca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2023-09-22T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": null, "date": "2023-04-03T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Famalicao", "away_goals": 0.0, "away_xg": 0.17, "date": "2026-11-01T00:00:00+00:00", "home": "Sp Braga", "home_goals": 3.0, "home_xg": 1.15, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.65, "date": "2026-10-25T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.58, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 4.0, "away_xg": 2.89, "date": "2026-10-12T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.36, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Sp Lisbon", "away_goals": 1.0, "away_xg": 2.28, "date": "2026-09-13T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.35, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-09-05T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 0.0, "away_xg": 0.27, "date": "2026-08-30T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": 0.23, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 0.0, "away_xg": 1.05, "date": "2026-08-23T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.36, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 2.0, "away_xg": 1.61, "date": "2026-08-16T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": 1.47, "date": "2026-08-07T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 1.22, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 70.0% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.0% |
| P home draw | 73.3% |
| P draw away | 53.8% |
| P home away | 72.9% |
| Raw p home draw | 73.7% |
| Raw p draw away | 51.3% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0065 |
| Totals anchor target over 2 5 | 0.4452 |
| Totals anchor reference over odds | 2.14 |
| Totals anchor reference under odds | 1.74 |
| Totals anchor reference last update utc | 2026-11-05T13:36:57Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4414 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.6, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.67, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.6, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.51, "draw": 3.38, "home": 2.14}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.14, "under": 1.74}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.36, "under": 3.19}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.14 |
| Reference draw odds | 3.38 |
| Reference away odds | 3.51 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:57Z |
| Market reference home last update utc | 2026-11-05T13:36:57Z |
| Market reference draw last update utc | 2026-11-05T13:36:57Z |
| Market reference away last update utc | 2026-11-05T13:36:57Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.75 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:58Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:58Z |
| Home probability edge | +1.1% |
| Draw probability edge | -0.9% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.0353 |
| Raw ev home | 0.0413 |
| Raw edge prob draw | -0.0294 |
| Raw ev draw | -0.1538 |
| Raw edge prob away | -0.0059 |
| Raw ev away | -0.0767 |
| Market p home draw | 73.1% |
| Market reference home draw last update utc | 2026-11-05T13:37:03Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.0% |
| Market reference draw away last update utc | 2026-11-05T13:37:03Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market reference home away last update utc | 2026-11-05T13:37:03Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.70 |
| Market reference dc home draw odds | 1.28 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 71.7% |
| Market over 1 5 odds | 1.36 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T13:36:57Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.13 |
| Market reference over 1 5 last update utc | 2026-11-05T13:37:00Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.9% |
| Market under 3 5 odds | 1.28 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T13:36:57Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.59 |
| Market reference under 3 5 last update utc | 2026-11-05T13:37:00Z |
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
| Market best home last update utc | 2026-11-05T13:36:57Z |
| Market best draw last update utc | 2026-11-05T13:36:57Z |
| Market best away last update utc | 2026-11-05T13:36:57Z |
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
| Dc lambda home | 1.4250 |
| Dc lambda away | 0.9057 |
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
| Score matrix json | [[0.07023008488405635,0.06783213465942899,0.03237923577718638,0.01114070256595963,0.0028748807071280872,0.0005934949995323118,0.00010210171897930406,1.5055745122527836e-05,1.942582657059955e-06,2.2279438321749777e-07,2.2997015499742473e-08,2.1579731306009805e-09,1.856231024011479e-10,1.4738589219425935e-11,1.0866635986720851e-12,7.47775273349147e-14],[0.12258553893613928,0.12207267021324918,0.0525840362962393,0.018092555121600008,0.004668820243048914,0.0009638387641944369,0.00016581368793450527,2.4450603264322206e-05,3.1547636778770807e-06,3.618191613392418e-07,3.734726495909648e-08,3.5045588539116418e-09,3.014528206054739e-10,2.3935540536003357e-11,1.7647469664690238e-12,1.2143906788228292e-13],[0.09465459388686757,0.09770323341648603,0.05385045941509416,0.014691198732309863,0.003791093384824082,0.0007826394191155123,0.00013464111760946236,1.9853949277301162e-05,2.5616757740222532e-06,2.9379803840124536e-07,3.032606991851999e-08,2.8457103071320565e-09,2.4478042300631775e-10,1.9435717090057236e-11,1.4329788259528387e-12,9.8608818275487e-14],[0.0512398401947433,0.05289017533321249,0.02729683227100444,0.010030012361374074,0.002052251361766029,0.00042367007367351235,7.28859431608386e-05,1.0747636711846833e-05,1.3867246364030587e-06,1.590431475011325e-07,1.6416561653804376e-08,1.5404824572197625e-09,1.3250819894316345e-10,1.0521233010149163e-11,7.757215263321884e-13,5.3380400070888176e-14],[0.020803437387737007,0.02147347545950773,0.011082547074213111,0.0038131647540009723,0.001050838680809455,0.0001720105647720003,2.9591781497168263e-05,4.363553565961103e-06,5.63011887582018e-07,6.457171116095447e-08,6.665143981496652e-09,6.254377496861576e-10,5.3798489800104824e-11,4.271633387937156e-12,3.1494388237820906e-13,2.167250729874446e-14],[0.006756976688461932,0.0069746057055783805,0.003599622064062458,0.0012385196192258694,0.0003196024790744762,7.04612927394049e-05,9.61143939915863e-06,1.4172864404338432e-06,1.8286680844200975e-07,2.0972954561146603e-08,2.1648452449864233e-09,2.0314278914332658e-10,1.7473801789508425e-11,1.38743067724765e-12,1.0229407918220703e-13,7.039251440459533e-15],[0.0018288938312397685,0.001887798928186854,0.0009743006216078766,0.00033522698033567163,8.650599659850224e-05,1.785843714609575e-05,3.2809731098437615e-06,3.836133447722829e-07,4.949609763626763e-08,5.676696692657102e-09,5.859532001797761e-10,5.498414617287076e-11,4.729589840928225e-12,3.7553236068195397e-13,2.7687680306512404e-14,1.9052964261347136e-15],[0.0004243046388726499,0.0004379706622693983,0.00022603842078929923,7.777289222703305e-05,2.0069451282562806e-05,4.143169819194755e-06,7.12768870666662e-07,1.1224348848476739e-07,1.1483129022817872e-08,1.3169975747223479e-09,1.3594154934079328e-10,1.2756360094334175e-11,1.0972681274289417e-12,8.712376845633347e-14,6.423561058059013e-15,4.420300939439581e-16],[8.613409950699933e-05,8.890831056028411e-05,4.588593676562198e-05,1.578794437842805e-05,4.074110804953934e-06,8.410659907680795e-07,1.4469251383772968e-07,2.133611100044517e-08,2.939921585316604e-09,2.673513079022893e-10,2.759621711694255e-11,2.5895488501653515e-12,2.2274609658979013e-13,1.7686177934752515e-14,1.303986797868132e-15,8.973237765681033e-17],[1.554246625484035e-05,1.604305872549107e-05,8.27988715077313e-06,2.8488553794548503e-06,7.351528612582917e-07,1.5176613971037663e-07,2.6109038424070226e-08,3.849994219850172e-09,4.967493764271637e-10,6.084225374094394e-11,4.9795989713281135e-12,4.672711022617124e-13,4.019341595790289e-14,3.1913821041996898e-15,2.3529787759580443e-16,1.6191757499992594e-17],[2.52410407491284e-06,2.6054005354823882e-06,1.3446576981034978e-06,4.626554984399556e-07,1.193891820230269e-07,2.464689486184043e-08,4.240120531561579e-09,6.252409327694898e-10,8.067234019953133e-11,9.252293184100022e-12,1.0199053218291127e-12,7.58850541457983e-14,6.527430289412042e-15,5.182820050393021e-16,3.8212489698856557e-17,2.629549288743278e-18],[3.726506624746416e-07,3.846530122149675e-07,1.9852096709490797e-07,6.830497985592705e-08,1.7626237450103102e-08,3.638788823921547e-09,6.259978503910596e-10,9.230857400793144e-11,1.191020660262319e-11,1.3659790096347524e-12,1.409974524637214e-13,1.4129573488698392e-14,9.636889563242096e-16,7.651749959369277e-17,5.641569910930093e-18,3.8821825700421733e-19],[5.043220727482074e-08,5.205653013492085e-08,2.6866584630342806e-08,9.24396827613578e-09,2.3854246082798745e-09,4.924508948372001e-10,8.471862933200201e-11,1.2492464408077948e-11,1.611852784805677e-12,1.8486304596772865e-13,1.908171234864225e-14,1.790572456442795e-15,1.644830405022336e-16,1.0355399274039187e-17,7.634947465651681e-19,5.253902804060795e-20],[6.300165366394188e-09,6.503081383360875e-09,3.356266464384802e-09,1.1547884165370242e-09,2.979954737918558e-10,6.151866515372902e-11,1.0583343526832831e-11,1.5606017633889989e-12,2.0135821212863707e-13,2.3093729635615284e-14,2.3837533545836557e-15,2.2368449024305287e-16,1.9240744219262576e-17,1.631507166319991e-18,9.537839844133369e-20,6.5633566867637716e-21],[7.308213699900115e-10,7.54359698412871e-10,3.8932807520210803e-10,1.339558572738232e-10,3.4567578427235924e-11,7.136186517805131e-12,1.2276715237685329e-12,1.8103034641161135e-13,2.3357622520758225e-14,2.6788806561340835e-15,2.7651621679768354e-16,2.594747853396537e-17,2.2319330100372906e-18,1.7721686242010065e-19,1.395363888279269e-20,7.613516545358703e-22],[7.912383049035918e-11,8.167225447552833e-11,4.215137910902967e-11,1.450299755776107e-11,3.74252769315735e-12,7.726134395743202e-13,1.3291630148394537e-13,1.9599610836884953e-14,2.5288595009414265e-15,2.9003434716578203e-16,2.993757868086747e-17,2.8092554179166515e-18,2.416446705088021e-19,1.9186736400925163e-20,1.4146216923341398e-21,1.0395838549992468e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.13734163842279687, "-10": 2.67571979928044e-08, "-11": 2.4796590623301426e-09, "-12": 2.1104500216317498e-10, "-13": 1.6601945004170445e-11, "-14": 1.208102666554368e-12, "-15": 7.47775273349147e-14, "-2": 0.05471761426638689, "-3": 0.016669600406927807, "-4": 0.003984692809421512, "-5": 0.0007806161540362655, "-6": 0.0001292799142699541, "-7": 1.8521366694057095e-05, "-8": 2.3363235848251244e-06, "-9": 2.6312424251543297e-07, "0": 0.257307923065719, "1": 0.2517369649049774, "10": 2.936813800366554e-06, "11": 4.282011574589143e-07, "12": 5.7339119730941486e-08, "13": 7.096676443916088e-09, "14": 8.124936244655398e-10, "15": 7.912383049035918e-11, "2": 0.15995663370450242, "3": 0.07666910196229934, "4": 0.02883434681815929, "5": 0.008887362420267013, "6": 0.0023157223999279693, "7": 0.0005219736215373948, "8": 0.00010359256910099439, "9": 1.8355936990270396e-05} |
| Raw goal margin distribution | {"-1": 0.1647870599616375, "-10": 1.1187766957692087e-08, "-11": 9.123491029579569e-10, "-12": 6.829333791139353e-11, "-13": 4.707855775919507e-12, "-14": 2.788682098778961e-13, "-2": 0.06005496521478524, "-3": 0.016463855471546912, "-4": 0.003510522408581548, "-5": 0.0006104273015784323, "-6": 8.945972188905615e-05, "-7": 1.131896440962777e-05, "-8": 1.259246005258991e-06, "-9": 1.2495623058141346e-07, "0": 0.2569472947682333, "1": 0.2556673971081957, "10": 1.0397867012860476e-06, "11": 1.3340803312251573e-07, "12": 1.571156174401396e-08, "13": 1.7040575240111648e-09, "14": 1.588108590223519e-10, "2": 0.1486582750533069, "3": 0.0641197468596593, "4": 0.021510578406684227, "5": 0.0058848361167763525, "6": 0.0013569006547178408, "7": 0.0002701141201307322, "8": 4.727932412799546e-05, "9": 7.38139894290073e-06} |
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
| Totals anchor scale | 1.1396 |
| Totals anchor target over 2 5 | 0.4902 |
| Totals anchor reference over odds | 1.95 |
| Totals anchor reference under odds | 1.88 |
| Totals anchor reference last update utc | 2026-11-05T13:36:57Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4138 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.63, "draw": 3.64, "home": 1.79}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.95, "under": 1.88}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 3.64 |
| Reference away odds | 4.63 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:57Z |
| Market reference home last update utc | 2026-11-05T13:36:57Z |
| Market reference draw last update utc | 2026-11-05T13:36:57Z |
| Market reference away last update utc | 2026-11-05T13:36:57Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:57Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:57Z |
| Market best over 2 5 last update utc | 2026-11-05T13:36:57Z |
| Market best under 2 5 last update utc | 2026-11-05T13:36:57Z |
| Home probability edge | -1.4% |
| Draw probability edge | -0.0% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0450 |
| Raw ev home | -0.1094 |
| Raw edge prob draw | -0.0005 |
| Raw ev draw | -0.0647 |
| Raw edge prob away | 0.0455 |
| Raw ev away | 0.1368 |
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
| 1 | 1-1 | 13.08% |
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
| Market best home last update utc | 2026-11-05T13:36:57Z |
| Market best draw last update utc | 2026-11-05T13:36:57Z |
| Market best away last update utc | 2026-11-05T13:36:57Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Nacional |
| Matched away-team name | Academico Viseu |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9184 |
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
| Score matrix json | [[0.0870815581579494,0.10969289381492871,0.08369181672154724,0.044524062792527935,0.017765107556590276,0.005670624407621404,0.0015083866445258678,0.0003439122808304181,6.861052513844249e-05,1.216693757788405e-05,1.9418439481825906e-06,2.81744006878227e-07,3.747196663026603e-08,4.600406202445351e-09,5.244464990362911e-10,5.580112792174927e-11],[0.10279867188228012,0.13084950624885452,0.07686289164496408,0.04089107332204157,0.01631554422729811,0.005207923623553942,0.0013853081909148374,0.000315850383135908,6.301217449928354e-05,1.1174163034498586e-05,1.7833970730636613e-06,2.5875479731011416e-07,3.4414400638578954e-08,4.225031040225227e-09,4.816537148802136e-10,5.124797402100058e-11],[0.04371675290020177,0.0697719631666048,0.050472551657276585,0.018777260795135583,0.00749212979952295,0.0023914887073386683,0.0006361362289902022,0.0001450391132968757,2.8935313693608995e-05,5.131197506450483e-06,8.189394217771027e-07,1.1882070868669194e-07,1.5803160039591115e-08,1.9401425119131878e-09,2.2117632731289974e-10,2.3533169839686093e-11],[0.013383212253664959,0.021359614574879737,0.017044978669544623,0.008220145813598458,0.0022936004320339436,0.0007321175258743546,0.00019474333316239043,4.440149621282802e-05,8.85810173669509e-06,1.5708372829306414e-06,2.507057221188547e-07,3.63751344505175e-08,4.837894652681492e-09,5.939448224475302e-10,6.770973454208558e-11,7.2043183921972384e-12],[0.003072798612848621,0.004904188381133834,0.003913543760577217,0.002082006042681404,0.0007530543270588085,0.0001680948994388713,4.471325961665428e-05,1.019462692402703e-05,2.0338288157639237e-06,3.606657753394254e-07,5.7562278813075336e-08,8.351766419240895e-09,1.1107853403278774e-09,1.3637031169595324e-10,1.5546221223555106e-11,1.654118543625519e-12],[0.0005644140516437655,0.0009008051561354922,0.0007188427777064291,0.0003824244977145545,0.00015258743043804654,4.415227329433427e-05,8.212966484985415e-06,1.8725570439686275e-06,3.7357526700748637e-07,6.624737159714202e-08,1.0573084376856448e-08,1.534058985628135e-09,2.0402991976742403e-10,2.504860547202674e-11,2.8555420689944516e-12,3.038297873485655e-13],[8.639334523933346e-05,0.0001378838294701143,0.00011003133619074021,5.853669227903097e-05,2.335614876813379e-05,7.455285415566406e-06,1.7977004954382592e-06,2.8662728489621995e-07,5.71821642665697e-08,1.0140307508152956e-08,1.6183936706644744e-09,2.3481429489023793e-10,3.1230312651297856e-11,3.8341228642452544e-12,4.3709016650737957e-13,4.6506410738627535e-14],[1.133485514235844e-05,1.8090435428651978e-05,1.4436172755981645e-05,7.680046717227301e-06,3.0643397617810844e-06,9.781376099777328e-07,2.6018469948669003e-07,5.377594212128389e-08,7.502331885546898e-09,1.3304140079941443e-09,2.1233415339425632e-10,3.080776662325734e-11,4.097434460633192e-12,5.030390609812633e-13,5.734647394177816e-14,6.101667060732897e-15],[1.3012469091170936e-06,2.0767908270963365e-06,1.6572796866191722e-06,8.816731159907469e-07,3.517877020413845e-07,1.122906755921607e-07,2.986933064026526e-08,6.810209878648491e-09,1.2316145852031193e-09,1.5273217822422514e-10,2.4376064566695583e-11,3.536746662557979e-12,4.703874782910922e-13,5.774913001056988e-14,6.583403230857365e-15,7.004743601503349e-16],[1.327855831294614e-07,2.1192586824357122e-07,1.6911690475841532e-07,8.997022626231318e-08,3.58981334180714e-08,1.1458688381149112e-08,3.048012225016865e-09,6.949470416678505e-10,1.3864198555837403e-10,2.2287254588217772e-11,2.4874525543244232e-12,3.609068845263077e-13,4.80006332111556e-14,5.893002972722194e-15,6.718025847830171e-16,7.147982118390472e-17],[1.2195079863125294e-08,1.9463354585510738e-08,1.5531762644161942e-08,8.262900751075027e-09,3.2968986064073444e-09,1.0523704203530737e-09,2.799306342739233e-10,6.382420797534419e-11,1.2732934151580385e-11,2.2579744826757547e-12,3.266805993276454e-13,3.3145829360548545e-14,4.408396918511174e-15,5.412156967064369e-16,6.16986120074143e-17,6.564734720408267e-18],[1.018182638116174e-09,1.6250200852220733e-09,1.2967665026487388e-09,6.898800319185124e-10,2.7526223348676713e-10,8.786373708879671e-11,2.337176262013535e-11,5.328763827821079e-12,1.063088772761278e-12,1.885211447053713e-13,3.00879857077597e-14,3.957352557663974e-15,3.6806263302343113e-16,4.518678287041746e-17,5.1512951327008385e-18,5.480980027337981e-19],[7.7925242926965e-11,1.2436873323278868e-10,9.924628544581799e-11,5.279904318264223e-11,2.106682594073842e-11,6.724533301592453e-12,1.7887265129319597e-12,4.078297942220483e-13,8.13620737273852e-14,1.4428213021993604e-14,2.3027436411587157e-15,3.341072905887337e-16,4.028181406487913e-17,3.4583098360232855e-18,3.942474656088214e-19,4.1947945694534903e-20],[5.5051421330261805e-12,8.786210060231944e-12,7.0113981943719184e-12,3.730065204681591e-12,1.4882965614131702e-12,4.750644362858205e-13,1.263671863048532e-13,2.88117290231544e-14,5.747942043976834e-15,1.019302095549432e-15,1.6268067399395017e-16,2.3603495520638164e-17,3.1392660532767416e-18,3.4937279597668865e-19,2.785218566204659e-20,2.963473639130204e-21],[3.611388611187613e-13,5.763778333109349e-13,4.599496793325705e-13,2.446933189673966e-13,9.763267000342947e-14,3.1164359671850765e-14,8.289722706910533e-15,1.890057468973047e-15,3.770666030737643e-16,6.686650208617569e-17,1.0671897639073774e-17,1.548395896921071e-18,2.059367296673137e-19,2.5282703142343604e-20,2.6127615950026707e-21,1.944046982130595e-22],[2.211142278765592e-14,3.528984368586155e-14,2.816130556889793e-14,1.4981820046288484e-14,5.977748386440182e-15,1.908097983352331e-15,5.075542493463544e-16,1.157224112076007e-16,2.308662948606753e-17,4.094030460690007e-18,6.534075006858587e-19,9.480352298124601e-20,1.260887317159626e-20,1.5479822267349842e-21,1.7647003843922158e-22,1.7020959378419453e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2078032488378561, "-10": 2.2170117004057544e-06, "-11": 3.181679138818048e-07, "-12": 4.192537831619635e-08, "-13": 5.105593087165251e-09, "-14": 5.756944730572917e-10, "-15": 5.580112792174927e-11, "-2": 0.13285378172296644, "-3": 0.06343641761874508, "-4": 0.02365567063121239, "-5": 0.007210201291399685, "-6": 0.001854802306716121, "-7": 0.00041231491824677977, "-8": 8.064113900630633e-05, "-9": 1.4074132526647262e-05, "0": 0.2774228212087022, "1": 0.1918579296128043, "10": 1.3923175839765854e-08, "11": 1.1498134406106884e-09, "12": 8.71863844865758e-11, "13": 6.109681271906013e-12, "14": 3.9642870480462287e-13, "15": 2.211142278765592e-14, "2": 0.06939670059695287, "3": 0.019067959848135738, "4": 0.004091678683624293, "5": 0.0007176527012750985, "6": 0.00010623441716112982, "7": 1.3589307890011385e-05, "8": 1.5294159703325672e-06, "9": 1.5360002322927885e-07} |
| Raw goal margin distribution | {"-1": 0.2558665052493203, "-10": 2.729789062741229e-06, "-11": 3.9175764894284804e-07, "-12": 5.1622388442016377e-08, "-13": 6.286476596221916e-09, "-14": 7.088480749762176e-10, "-15": 6.870748975367925e-11, "-2": 0.1635818161107541, "-3": 0.0781087618813389, "-4": 0.029127041119843464, "-5": 0.00887786411854449, "-6": 0.002283803486239701, "-7": 0.0005076801146467157, "-8": 9.929279995505735e-05, "-9": 1.732936864148295e-05, "0": 0.23887377553407274, "1": 0.14975361385392585, "10": 1.0867655574812651e-08, "11": 8.974803300377913e-10, "12": 6.805283566893665e-11, "13": 4.768876907042959e-12, "14": 3.0943016689345857e-13, "15": 1.7258945077673417e-14, "2": 0.054167199265132755, "3": 0.014883387420278464, "4": 0.0031937364842746564, "5": 0.0005601597271734838, "6": 8.292066904741044e-05, "7": 1.0607056848835384e-05, "8": 1.1937769218370902e-06, "9": 1.198916229996487e-07} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.79, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.09, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.44, "draw": 3.23, "home": 3.05}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.05 |
| Reference draw odds | 3.23 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:57Z |
| Market reference home last update utc | 2026-11-05T13:36:57Z |
| Market reference draw last update utc | 2026-11-05T13:36:57Z |
| Market reference away last update utc | 2026-11-05T13:36:57Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:58Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:58Z |
| Home probability edge | -2.7% |
| Draw probability edge | -1.7% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0894 |
| Raw ev home | -0.3209 |
| Raw edge prob draw | -0.0551 |
| Raw ev draw | -0.2284 |
| Raw edge prob away | 0.1445 |
| Raw ev away | 0.3139 |
| Elo home rating | 1,377.6402 |
| Elo away rating | 1,452.3265 |
| Elo rating diff | -14.6862 |
| Elo home expectancy | 0.4789 |

</details>


---

## 2026-11-07 — Sporting Lisbon vs Moreirense FC

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **84.1%**. Expected goals are 2.87 for Sporting Lisbon and 0.69 for Moreirense FC (3.56 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 69.7%; Under 3.5 goals: 51.9%; Double Chance 1X: 94.3%; Double Chance X2: 15.9%; Double Chance 12 (either team wins): 89.8%; Under 4.5 goals: 70.9%; BTTS Yes (both teams score): 46.3%; BTTS No (at least one team does not score): 53.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 84.1% | 1.19 |
| Draw | 10.2% | 9.80 |
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
| Over 4.5 | 29.1% |
| Under 4.5 | 70.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.99% |
| 2 | 3-0 | 11.47% |
| 3 | 1-0 | 8.64% |
| 4 | 2-1 | 8.28% |
| 5 | 4-0 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 84.1% | 84.9% | 1.16 | -2.5% |
| Draw | 10.2% | 9.7% | 8.30 | -15.3% |
| Moreirense FC win | 5.7% | 5.4% | 14.11 | -19.2% |

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
| Market best home last update utc | 2026-11-05T13:36:57Z |
| Market best draw last update utc | 2026-11-05T13:36:57Z |
| Market best away last update utc | 2026-11-05T13:36:57Z |
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
| Fair Under 0.5 odds | 43.61 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.74 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.30 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.44 |
| Fair Under 4.5 odds | 1.41 |
| Score matrix json | [[0.02293256548002422,0.01979603710401255,0.005975790642191839,0.001375174076973021,0.00023734563196874727,3.277138506778255e-05,3.7707444847152064e-06,3.7188839173307606e-07,3.209269533062166e-08,2.4617686775071152e-09,1.6995376870684173e-10,1.06664934781429e-11,6.136545857120153e-13,3.258848638095185e-14,1.6070141902153741e-15,7.396257292244795e-17,3.1913584444075758e-18,1.2960155791698638e-19,4.97074260278378e-21,1.8061392550673362e-22],[0.0864174771599942,0.04791289137318339,0.017150606792891446,0.003946769771253403,0.0006811854450130572,9.405435581823207e-05,1.0822091978458987e-05,1.0673251389401696e-06,9.210650631791092e-08,7.06531221239285e-09,4.877698089824559e-10,3.0612992732869764e-11,1.7611976617609911e-12,9.352943390436477e-14,4.612154296769615e-15,2.1227366913212262e-16,9.15924554464185e-18,3.7195837215025122e-19,1.4266104178266426e-20,5.183646153558024e-22],[0.11987189962876296,0.08275627718436458,0.024982532281329142,0.005663643566335656,0.0009775061092313175,0.00013496869036944213,1.5529781355507558e-05,1.5316194018652027e-06,1.3217351205145765e-07,1.0138774839953113e-08,6.999532530672379e-10,4.392986907942598e-11,2.527331560794404e-12,1.3421542357340126e-13,6.61847524020915e-15,3.0461427196469216e-16,1.3143584528095012e-17,5.337629918819495e-19,2.0471964119724474e-20,7.438570245873737e-22],[0.11467803671782119,0.07917057644844039,0.027328599069939803,0.005499986479956229,0.0009351522903490037,0.00012912070700370573,1.4856900091031029e-05,1.465256716117644e-06,1.2644663941342485e-07,9.699477500320509e-09,6.696253676182061e-10,4.2026456199503535e-11,2.4178262163565913e-12,1.2840007808598429e-13,6.331707005255272e-15,2.9141580948765873e-16,1.2574093459640125e-17,5.106358718867328e-19,1.958494576525724e-20,7.116268570250603e-22],[0.08228191185454266,0.05680517891000452,0.019608370043114613,0.004512360587835989,0.0006810975426037433,9.264458074406592e-05,1.0659880293642924e-05,1.0513270667209872e-06,9.072592744257989e-08,6.959410673207546e-09,4.804586566955467e-10,3.015413642871481e-11,1.7347991760913985e-12,9.212752685314785e-14,4.543022993820074e-15,2.0909191189142023e-16,9.021958164863735e-18,3.6638311051432827e-19,1.405227040203127e-20,5.105948793589855e-22],[0.04723005877819744,0.032606339332128885,0.011255261925830188,0.002590108214411275,0.0004470349472919481,5.3980509426363596e-05,6.118802559271213e-06,6.034648203619834e-07,5.207694849621994e-08,3.994722141827098e-09,2.757846783669705e-10,1.730856276713214e-11,9.957798161035533e-13,5.288147066947274e-14,2.6077085253941967e-15,1.2001937079604032e-16,5.178630452513336e-18,2.1030498021875016e-19,8.066044433050203e-21,2.9308295858028425e-22],[0.02259182690657621,0.015596778689350117,0.005383794468913802,0.0012389414276209368,0.00021383280926747883,2.9524863274302778e-05,2.970996581559841e-06,2.886588142913668e-07,2.491026767030814e-08,1.910818523259723e-09,1.3191767866332894e-10,8.279304835783288e-12,4.763171129665985e-13,2.5295099409899793e-14,1.2473602860664746e-15,5.740955909443004e-17,2.4771242260302532e-18,1.0059639631204938e-19,3.858277638569087e-21,1.401920649857326e-22],[0.009262696369583592,0.006394711943414772,0.002207367013212906,0.0005079685813461441,8.767189985521661e-05,1.2105255807520798e-05,1.3928561907854803e-06,1.2013616000227625e-07,1.0213261940669093e-08,7.834395983787772e-10,5.408652466627335e-11,3.3945323307502234e-12,1.9529101436953625e-13,1.0371043760260609e-14,5.11420330949308e-16,2.3538039522097292e-17,1.0156261231259267e-18,4.1244733273057176e-20,1.5819019162729384e-21,5.747904039623188e-23],[0.0033230093051419877,0.00229411463399023,0.0007918969630545836,0.0001822346598854234,3.1452454813809074e-05,4.342782715150587e-06,4.996897121559054e-07,4.928172783186037e-08,3.7193020225411374e-09,2.8106039230414876e-10,1.9403639888165504e-11,1.2177946973118166e-12,7.006100945849753e-14,3.720630963630524e-15,1.8347298138411775e-16,8.444314834023375e-18,3.643577337561437e-19,1.4796623681256412e-20,5.675102127776249e-22,2.0620711126245995e-23],[0.0010596761606595812,0.0007315714053818616,0.00025252843323344463,5.811290519941493e-05,1.0029889627104742e-05,1.38487223224099e-06,1.5934631145302672e-07,1.571547574625429e-08,1.3561917669705408e-09,9.097961642644797e-11,6.187636786841244e-12,3.8834318258517256e-13,2.234179164049708e-14,1.1864739375451994e-15,5.850779418433839e-17,2.6928119367201986e-18,1.161902266767317e-19,4.718502999379493e-21,1.8097362606861537e-22,6.575749265136948e-24],[0.0003041286123873862,0.00020996206637562603,7.247603073361996e-05,1.6678489029230368e-05,2.8785930343014766e-06,3.9746036191199847e-07,4.573262510793193e-08,4.5103645898205234e-09,3.892290263123592e-10,2.985700688212645e-11,1.8026515054437853e-12,1.1145506300360314e-13,6.412126970605021e-15,3.405197603339678e-16,1.6791822747106102e-17,7.728409755157205e-19,3.3346765478026203e-20,1.354217281677629e-21,5.1939696124430356e-23,1.8872496840626104e-24],[7.935032530479146e-05,5.4781291828440736e-05,1.8909751931486898e-05,4.3515916495751435e-06,7.510549300142157e-07,1.0370155167546245e-07,1.193211862201947e-08,1.17680113895234e-09,1.0155391041146878e-10,7.790004334437271e-12,5.378005687443068e-13,2.951848603831299e-14,1.6729907686720442e-15,8.884515515689981e-17,4.381161597995471e-18,2.0164226685101024e-19,8.700518730455745e-21,3.5332940557929268e-22,1.355160815469693e-23,4.924031158600193e-25],[1.8978049791184102e-05,1.31019259209358e-05,4.5226054501509165e-06,1.0407609884310237e-06,1.7962822210211404e-07,2.480208119576719e-08,2.8537796216107858e-09,2.814530441252154e-10,2.4288434368421264e-11,1.863118891631859e-12,1.286246267063543e-13,8.072629117501075e-15,4.061619742227665e-16,2.1248908202917076e-17,1.0478331705712755e-18,4.8226355287224374e-20,2.0808846975923935e-21,8.450504803876835e-23,3.2411095143289256e-24,1.1776701373600247e-25],[4.18979086622304e-06,2.892516889642044e-06,9.984572290128118e-07,2.297691770876893e-07,3.965658708667363e-08,5.4755643704559985e-09,6.30029951675677e-10,6.213648960359912e-11,5.362166375964588e-12,4.1132142663430686e-13,2.8396505018970494e-14,1.7821972286437897e-15,1.0253168056039708e-16,4.761899560064203e-18,2.313305052779682e-19,1.0646949771809654e-20,4.593976618022102e-22,1.8656209795963444e-23,7.155409111568489e-25,2.5999465905220403e-26],[8.589115171244027e-07,5.929689928008335e-07,2.0468477800857584e-07,4.710292202692176e-08,8.129641900073211e-09,1.1224964325678412e-09,1.2915680016157708e-10,1.273804546772596e-11,1.0992497248926e-12,8.432132339214453e-14,5.821313279261963e-15,3.6535229903951387e-16,2.1019101934993145e-17,1.1162317256271926e-18,4.813842020328792e-20,2.182635857788309e-21,9.417700196994377e-23,3.824542553859556e-24,1.4668663644310638e-25,5.3299177496197884e-27],[1.6433924348107563e-07,1.1345531378002257e-07,3.916322100632542e-08,9.012405139901328e-09,1.5554794329723485e-09,2.1477208171105123e-10,2.4712127391249988e-11,2.4372251551616237e-12,2.1032418891114425e-13,1.6133562327795746e-14,1.1138169663659182e-15,6.990443046944159e-17,4.021675390048448e-18,2.1357342832390878e-19,1.053180334788666e-20,4.239132483497783e-22,1.8019291799547124e-23,7.317662150656975e-25,2.806618654101964e-26,1.0197961411920472e-27],[2.94785024520975e-08,2.0351150915776364e-08,7.024938669624235e-09,1.6166084338003584e-09,2.7901554922481313e-10,3.8524939042270636e-11,4.432760504847985e-12,4.371794964543511e-13,3.772709419382563e-14,2.893972532469163e-15,1.9979193939752105e-16,1.253917129807896e-17,7.213917098306177e-19,3.830992949212528e-20,1.8891518802168316e-21,8.694791530334321e-23,3.280988425839981e-24,1.3126123565038994e-25,5.034397939563025e-27,1.8292686769141125e-28],[4.976690259583526e-09,3.435770684024421e-09,1.1859810011754172e-09,2.729229362695244e-10,4.710463051357188e-11,6.50394941853891e-12,7.483580980204727e-13,7.380656277331317e-14,6.3692537469264386e-15,4.885731538515374e-16,3.3729752736207853e-17,2.1169179731502497e-18,1.2178851695374676e-19,6.467650561917389e-21,3.189349179601911e-22,1.4678928954562705e-23,6.3337066333700615e-25,2.249440601361588e-26,8.499291722639036e-28,3.088251725593322e-29],[7.935096689177157e-10,5.478173476252395e-10,1.8909904826268234e-10,4.351626834365306e-11,7.510610026681413e-12,1.0370239015426034e-12,1.193221509915329e-13,1.1768106539768346e-14,1.0155473152551525e-15,7.790067320509942e-17,5.3780491713029615e-18,3.3753253515540054e-19,1.941860166600654e-20,1.0312362209361264e-21,5.085266069543755e-23,2.3404856334732943e-24,1.0098794965166277e-25,4.101136188143633e-27,1.375615920982209e-28,4.924070971849463e-30],[1.198623362411851e-10,8.27496748834445e-11,2.8564054848460955e-11,6.573280443176881e-12,1.1345032072795772e-12,1.5664598989244917e-13,1.802401702637813e-14,1.7776125461907544e-15,1.534018784370585e-16,1.1767161826597173e-17,8.12372631793587e-19,5.098543824464924e-20,2.933245873864548e-21,1.5577174103817081e-22,7.681467477704421e-24,3.535383208999433e-25,1.5254573512589032e-26,6.1949057964804535e-28,2.375996296473657e-29,7.550186262415176e-31]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.04364450229632941, "-10": 2.032271586398995e-10, "-11": 1.2568452643223812e-11, "-12": 7.141031468449787e-13, "-13": 3.7518203632492804e-14, "-14": 1.8329564251008393e-15, "-15": 8.367567699961637e-17, "-16": 3.584500407534577e-18, "-17": 1.446115191198402e-19, "-18": 5.489107218139582e-21, "-19": 1.8061392550673362e-22, "-2": 0.011040476288300025, "-3": 0.002207290482607298, "-4": 0.0003484898818916644, "-5": 4.525878676124751e-05, "-6": 4.980440867300972e-06, "-7": 4.7483447398988473e-07, "-8": 3.990177620419547e-08, "-9": 2.9959809754608973e-09, "0": 0.10206614861137889, "1": 0.2014927173372142, "10": 0.0003636706277646417, "11": 9.349940614141861e-05, "12": 2.2084549504573033e-05, "13": 4.823587848142431e-06, "14": 9.796723597663356e-07, "15": 1.8592102616957833e-07, "16": 3.310994546482779e-08, "17": 5.553071662057227e-09, "18": 8.762593438011602e-10, "19": 1.198623362411851e-10, "2": 0.2214674082021416, "3": 0.18406959762396904, "4": 0.12081289849810944, "5": 0.06522687870965418, "6": 0.029839533929862654, "7": 0.011826794425828955, "8": 0.0041315935683257626, "9": 0.0012896295441943992} |
| Raw goal margin distribution | {"-1": 0.04947829663497685, "-10": 2.3039175865030134e-10, "-11": 1.424842982288715e-11, "-12": 8.095545937875854e-13, "-13": 4.253311896962717e-14, "-14": 2.0779607269746177e-15, "-15": 9.486028594414105e-17, "-16": 4.063626920248031e-18, "-17": 1.6394118991815928e-19, "-18": 6.222815266772884e-21, "-19": 2.0475590079947717e-22, "-2": 0.012516214690111811, "-3": 0.002502330591754511, "-4": 0.00039507119667564554, "-5": 5.130835635397999e-05, "-6": 5.646157422810241e-06, "-7": 5.38303789033255e-07, "-8": 4.523529460570076e-08, "-9": 3.396442337917747e-09, "0": 0.11398929702357825, "1": 0.19679934623076256, "10": 0.0003551996455913299, "11": 9.132152389806136e-05, "12": 2.1570133956887028e-05, "13": 4.711231986674669e-06, "14": 9.568528454539568e-07, "15": 1.8159036656144084e-07, "16": 3.2338715301105576e-08, "17": 5.423723929617166e-09, "18": 8.558486295068473e-10, "19": 1.1707038210457638e-10, "2": 0.2163087664982973, "3": 0.17978206335235217, "4": 0.11799880290899319, "5": 0.0637075486219688, "6": 0.029144481482175327, "7": 0.011551312830396239, "8": 0.0040353563338815564, "9": 0.0012595901952753082} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.83, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "line": -2.0, "market_key": "spreads", "opposite_price": 2.02, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:36:57Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 14.11, "draw": 8.3, "home": 1.16}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 8.30 |
| Reference away odds | 14.11 |
| Market reference 1x2 last update utc | 2026-11-05T13:36:57Z |
| Market reference home last update utc | 2026-11-05T13:36:57Z |
| Market reference draw last update utc | 2026-11-05T13:36:57Z |
| Market reference away last update utc | 2026-11-05T13:36:57Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:58Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:58Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | -0.0280 |
| Raw ev home | -0.0476 |
| Raw edge prob draw | 0.0170 |
| Raw ev draw | -0.0539 |
| Raw edge prob away | 0.0109 |
| Raw ev away | -0.0836 |
| Elo home rating | 1,667.4354 |
| Elo away rating | 1,438.9672 |
| Elo rating diff | 288.4681 |
| Elo home expectancy | 0.8403 |

</details>


---
