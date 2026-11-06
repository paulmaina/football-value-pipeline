# Eredivisie — football model report

Fixtures in this report: **1**.

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
| Training as of utc | 2026-11-06T13:21:16.622975+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-06', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1629, 'tune_start_date': '2025-11-07', 'audit_start_date': '2026-05-08', 'training_shot_matches': 1323, 'tuning_matches': 189, 'audit_matches': 114, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6640139536476394, 'audit_candidate_poisson_score': 0.6541649183510307, 'audit_gain': 0.009849035296608633, 'audit_gain_lower95': -0.0021941063321638033, 'audit_baseline_briers': [0.621667699677954, 0.09847504422570597, 0.2796863737668338, 0.23025002755863266], 'audit_candidate_briers': [0.6176833709472638, 0.0975910521480671, 0.27680191787942204, 0.22437690543765784], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1634.291 |
| Base scoring parameter | 0.290 |
| Home-advantage parameter | 0.183 |
| Dixon-Coles low-score adjustment | -0.081 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1629, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-01'} |
| Training data health | {'training_end': '2026-11-01', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Over 1 5 in window quote fixtures | 0 |
| Odds provider health | — |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'None': 1} |
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

## 2026-11-06 — Willem II Tilburg vs PEC Zwolle

The model's most likely 1X2 outcome is **PEC Zwolle win** at **46.4%**. Expected goals are 1.22 for Willem II Tilburg and 1.64 for PEC Zwolle (2.86 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 54.5%; Under 3.5 goals: 67.8%; Double Chance 1X: 53.6%; Double Chance X2: 72.6%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 57.8%; BTTS No (at least one team does not score): 42.2%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Willem II Tilburg win | 27.4% | 3.65 |
| Draw | 26.2% | 3.82 |
| PEC Zwolle win | 46.4% | 2.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Willem II Tilburg expected goals | 1.22 |
| PEC Zwolle expected goals | 1.64 |
| Expected total goals | 2.86 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 78.9% |
| Under 1.5 | 21.1% |
| Over 2.5 | 54.5% |
| Under 2.5 | 45.5% |
| Over 3.5 | 32.2% |
| Under 3.5 | 67.8% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.37% |
| 2 | 1-2 | 9.41% |
| 3 | 0-1 | 8.46% |
| 4 | 0-2 | 7.72% |
| 5 | 2-1 | 6.97% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:00:00+00:00 |
| Fixture id | fdorg:558845 |
| Matched home-team name | Willem II |
| Matched away-team name | Zwolle |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.2186 |
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
| P btts yes | 57.8% |
| P btts no | 42.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.06 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.73 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.17 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.06638620627637778,0.084639886861492,0.07718998586286105,0.04229988565396884,0.01738515987214081,0.005716209944440582,0.0015662331345253728,0.0003678390685229127,7.559052364589767e-05,1.3807795018151128e-05,2.269989340737458e-06,3.3925840771219046e-07,4.6478152874872515e-08,5.877667230967093e-09,6.902023688771444e-10,7.564577439739788e-11],[0.06034139028246181,0.12369916581685712,0.09406379803873334,0.05154668519159333,0.02118557412342984,0.0069657794563680545,0.0019086133466757224,0.0004482490761660128,9.21146916972148e-05,1.6826193546078925e-05,2.7662114004860814e-06,4.134206528121123e-07,5.663832602590059e-08,7.162531475712818e-09,8.410813333644089e-10,9.218202032116142e-11],[0.04241164191444613,0.06972436579657311,0.057313121660569635,0.031407422421624503,0.012908381465578987,0.004244253089579956,0.0011629191168314181,0.0002731183980681053,5.6125530140664815e-05,1.0252208585003242e-05,1.685454062461206e-06,2.5189742138474877e-07,3.450976186222855e-08,4.364134198537791e-09,5.124712991676009e-10,5.616655350667755e-11],[0.017227623829422955,0.02832206185536291,0.023280610131765064,0.012757706009661267,0.005243389081334847,0.0017240170944488775,0.0004723781533671867,0.00011094078914236165,2.2798210039611024e-05,4.164450725098106e-06,6.846320316583668e-07,1.0232082096637605e-07,1.4017877379157443e-08,1.7727128429781552e-09,2.0816602156654318e-10,2.2814873745281976e-11],[0.005248400133979655,0.008628323598661123,0.007092444004146596,0.0038866384936977116,0.0015973998636994292,0.0005252222615886884,0.00014391012875421294,3.379814061206389e-05,6.945480689103174e-06,1.2687010094931165e-06,2.0857332864127736e-07,3.117206503845656e-08,4.270550033094413e-09,5.400574341949538e-10,6.341783325997151e-11,6.95055729142175e-12],[0.001279141185765272,0.0021028968442596747,0.0017285719460872647,0.0009472523520609898,0.0003893186311319633,0.00012800728018605697,3.50738068819298e-05,8.237289946564197e-06,1.6927540160000447e-06,3.092080771734303e-07,5.08335355739947e-08,7.597262254813834e-09,1.040819353279798e-09,1.316229115773743e-10,1.545620767548337e-11,1.6939912865860659e-12],[0.00025979379927731694,0.00042709871806031666,0.00035107326555944594,0.00019238711891609577,7.907068229587689e-05,2.5998301066974076e-05,7.1234963320519116e-06,1.672995033528268e-06,3.4379863767382977e-07,6.280021473005734e-08,1.0324299994738915e-08,1.5430052970293678e-09,2.113905932816535e-10,2.6732636436978357e-11,3.139158490961059e-12,3.440499275469521e-13],[4.522642818748329e-05,7.435184964019122e-05,6.111689300336527e-05,3.34918779511275e-05,1.3765088098859858e-05,4.5259367216342005e-06,1.2401000185591252e-06,2.912447870286361e-07,5.985048311762244e-08,1.0932629683804216e-08,1.7973146918709476e-09,2.686154113498045e-10,3.680011421811071e-11,4.653774129491561e-12,5.464831202881395e-13,5.9894229132472e-14],[6.889121625502758e-06,1.1325655281221848e-05,9.30963876978346e-06,5.101654716471007e-06,2.0967688561585494e-06,6.894139067408472e-07,1.8889839852545394e-07,4.436390051224988e-08,9.116732717276842e-09,1.6653142553307638e-09,2.737761969677001e-10,4.0916877883922785e-11,5.605582241206514e-12,7.088867567162537e-13,8.324311321563034e-14,9.123396334745822e-15],[9.327878739734964e-07,1.5334950499377563e-06,1.2605261784580281e-06,6.9076464539506e-07,2.839027484011415e-07,9.334672361944637e-08,2.5576865257433666e-08,6.006877318989599e-09,1.2344066763827346e-09,2.2548374497806544e-10,3.7069329095407466e-11,5.540150051885918e-12,7.589964911930291e-13,9.59833497840249e-14,1.1271127267066683e-14,1.2353089309675357e-15],[1.136696285270834e-07,1.8687186823303272e-07,1.5360785281612617e-07,8.417665241211094e-08,3.4596418809677526e-08,1.137524156788543e-08,3.1167994930242375e-09,7.31998702501048e-10,1.504249275433483e-10,2.7477472902140834e-11,4.517272346255752e-12,6.751232685943636e-13,9.249139232455622e-14,1.1696541109887136e-14,1.3735007553982775e-15,1.5053487638204226e-16],[1.2592538999583822e-08,2.0702023215364625e-08,1.701697192375818e-08,9.325250659206289e-09,3.8326574895333465e-09,1.260171031870264e-09,3.452850130537666e-10,8.109221722927465e-11,1.666436137026573e-11,3.044007037005263e-12,5.004320760880614e-13,7.47914478076738e-14,1.0246373460218313e-14,1.2957652100657254e-15,1.5215904241465577e-16,1.667654171304641e-17],[1.2787734402017753e-09,2.1022922737919466e-09,1.7280749918249574e-09,9.469800225841042e-10,3.8920670431655096e-10,1.279704788462928e-10,3.506372336885141e-11,8.234921774178852e-12,1.6922673591818584e-12,3.091191816708514e-13,5.081892123165921e-14,7.595078086623472e-15,1.0405201238406791e-15,1.3158507076486216e-16,1.54517641067324e-17,1.6935042740598673e-18],[1.198703585025434e-10,1.970658137041107e-10,1.6198723110534139e-10,8.876852711610271e-11,3.6483669203089544e-11,1.1995766173112586e-11,3.286822324050638e-12,7.719295649082794e-13,1.5863067581015292e-13,2.8976381555947156e-14,4.763691608882891e-15,7.119515501938427e-16,9.753683987541417e-17,1.2334592751377255e-17,1.4484258467852511e-18,1.5874662240804336e-19],[1.0433867505121159e-11,1.715318628945248e-11,1.4099843597603918e-11,7.726672899994025e-12,3.1756455500850832e-12,1.0441466634140025e-12,2.8609465317725814e-13,6.719101289221486e-14,1.3807679182137802e-14,2.5221892193321013e-15,4.146456864170213e-16,6.19703506153321e-17,8.489892554268923e-18,1.0736391223420543e-18,1.2607523298622295e-19,1.381777151401343e-20],[8.476481284401331e-13,1.3935260580894738e-12,1.1454722834980805e-12,6.277154487091579e-13,2.5798966737862553e-13,8.482654822149874e-14,2.324234970430706e-14,5.458602603313527e-15,1.1217368258794069e-15,2.0490282920397406e-16,3.368584466734428e-17,5.034475633515833e-18,6.897194669907118e-19,8.722251765480721e-20,1.0242360776670093e-20,1.1225567276293356e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.21591652702024103, "-10": 2.719757580079324e-06, "-11": 4.004759845154868e-07, "-12": 5.4175970523498216e-08, "-13": 6.774915117838179e-09, "-14": 7.823843891983058e-10, "-15": 7.564577439739788e-11, "-2": 0.14352157204386057, "-3": 0.06823764655419104, "-4": 0.02563206452186729, "-5": 0.007922061014294808, "-6": 0.0020749885782768906, "-7": 0.0004709228410094238, "-8": 9.420889744740155e-05, "-9": 1.6840477575092907e-05, "0": 0.26188903099527994, "1": 0.157649607363008, "10": 1.3619175573348738e-07, "11": 1.4864803167048484e-08, "12": 1.4905668129521991e-09, "13": 1.3816901707549395e-10, "14": 1.1827393563210632e-11, "15": 8.476481284401331e-13, "2": 0.07885719180383047, "3": 0.027791387320935307, "4": 0.007738055436943054, "5": 0.0017727540832165154, "6": 0.00034418194477219374, "7": 5.790075028267873e-05, "8": 8.585951272939592e-06, "9": 1.1376612452110874e-06} |
| Raw goal margin distribution | {"-1": 0.21591652702024103, "-10": 2.719757580079324e-06, "-11": 4.004759845154868e-07, "-12": 5.4175970523498216e-08, "-13": 6.774915117838179e-09, "-14": 7.823843891983058e-10, "-15": 7.564577439739788e-11, "-2": 0.14352157204386057, "-3": 0.06823764655419104, "-4": 0.02563206452186729, "-5": 0.007922061014294808, "-6": 0.0020749885782768906, "-7": 0.0004709228410094238, "-8": 9.420889744740155e-05, "-9": 1.6840477575092907e-05, "0": 0.26188903099527994, "1": 0.157649607363008, "10": 1.3619175573348738e-07, "11": 1.4864803167048484e-08, "12": 1.4905668129521991e-09, "13": 1.3816901707549395e-10, "14": 1.1827393563210632e-11, "15": 8.476481284401331e-13, "2": 0.07885719180383047, "3": 0.027791387320935307, "4": 0.007738055436943054, "5": 0.0017727540832165154, "6": 0.00034418194477219374, "7": 5.790075028267873e-05, "8": 8.585951272939592e-06, "9": 1.1376612452110874e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 27.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 46.4% |
| Raw p over 1 5 | 78.9% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 57.8% |
| P home draw | 53.6% |
| P draw away | 72.6% |
| P home away | 73.8% |
| Raw p home draw | 53.6% |
| Raw p draw away | 72.6% |
| Raw p home away | 73.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5453 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-01 |
| Elo home rating | 1,319.6939 |
| Elo away rating | 1,410.7310 |
| Elo rating diff | -31.0371 |
| Elo home expectancy | 0.4555 |
| Research p home | 0.2835 |
| Research p draw | 0.2434 |
| Research p away | 0.4732 |
| Research p over 1 5 | 0.7794 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.21860105280821, 1.6439911932016897], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:21:40.924259+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-06T13:21:41.044058+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:21:41.344384+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Willem+II+Tilburg%22+%22PEC+Zwolle%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:21:28.744830+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:21:29.042627+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:21:41.448086+00:00", "reason": "HTTPError", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Willem+II+Tilburg_vs_PEC+Zwolle&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.21860105280821, 1.6439911932016897], "h2h": [], "margin_distribution": {"-1": 0.225182235495343, "-10": 2.719757580079324e-06, "-11": 4.004759845154868e-07, "-12": 5.4175970523498216e-08, "-13": 6.774915117838179e-09, "-14": 7.823843891983058e-10, "-15": 7.564577439739788e-11, "-2": 0.14352157204386057, "-3": 0.06823764655419104, "-4": 0.02563206452186729, "-5": 0.007922061014294808, "-6": 0.0020749885782768906, "-7": 0.0004709228410094238, "-8": 9.420889744740155e-05, "-9": 1.6840477575092907e-05, "0": 0.243357614045076, "1": 0.16691531583810998, "10": 1.3619175573348738e-07, "11": 1.4864803167048484e-08, "12": 1.4905668129521991e-09, "13": 1.3816901707549395e-10, "14": 1.1827393563210632e-11, "15": 8.476481284401331e-13, "2": 0.07885719180383047, "3": 0.027791387320935307, "4": 0.007738055436943054, "5": 0.0017727540832165154, "6": 0.00034418194477219374, "7": 5.790075028267873e-05, "8": 8.585951272939592e-06, "9": 1.1376612452110874e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:21:41.448593+00:00", "p_over_1_5": 0.7793668081045665, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
