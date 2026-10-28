# Super Lig — football model report

Fixtures in this report: **2**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,831 |
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
| Training sha256 | 36930ef41a7cb5e7e2f4d6e9884819c8b34ead9559d248ba647b034c279b2986 |
| Training as of utc | 2026-10-28T12:13:32.613686+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1800, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1503, 'tuning_matches': 189, 'audit_matches': 94, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8834213336709461, 'audit_candidate_poisson_score': 0.8729981312512226, 'audit_gain': 0.010423202419723498, 'audit_gain_lower95': 0.0029566890809536155, 'audit_baseline_briers': [0.6143674697310673, 0.1743712209488181, 0.2059329930887126, 0.2483102672048143], 'audit_candidate_briers': [0.6098523383208784, 0.17316940263649583, 0.20306892001246502, 0.24810657399937736], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1660.303 |
| Base scoring parameter | 0.124 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1831, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 2.00 |
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
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1, 'ANCHORED_MAIN': 1} |
| Shot features applied fixtures | 2 |
| Goal rate features used | {'shot_features': 2} |
| Legacy comparison status | {'AVAILABLE': 2} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Torku Konyaspor vs Galatasaray

The model's most likely 1X2 outcome is **Galatasaray win** at **57.9%**. Expected goals are 0.95 for Torku Konyaspor and 1.80 for Galatasaray (2.75 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 52.7%; Under 3.5 goals: 70.0%; Double Chance 1X: 42.1%; Double Chance X2: 81.0%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 51.9%; BTTS No (at least one team does not score): 48.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torku Konyaspor win | 19.0% | 5.26 |
| Draw | 23.1% | 4.32 |
| Galatasaray win | 57.9% | 1.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torku Konyaspor expected goals | 0.95 |
| Galatasaray expected goals | 1.80 |
| Expected total goals | 2.75 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 30.0% |
| Under 3.5 | 70.0% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.04% |
| 2 | 0-1 | 10.71% |
| 3 | 0-2 | 10.62% |
| 4 | 1-2 | 10.11% |
| 5 | 0-0 | 6.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torku Konyaspor win | 19.0% | 19.2% | 4.78 | -9.2% |
| Draw | 23.1% | 22.3% | 4.14 | -4.3% |
| Galatasaray win | 57.9% | 58.5% | 1.66 | -3.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T17:00:00+00:00 |
| Fixture id | feb03ec355aa5c94e0d7ae612a59b813 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T12:13:27Z |
| Market best draw last update utc | 2026-10-28T12:13:27Z |
| Market best away last update utc | 2026-10-28T12:13:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Konyaspor |
| Matched away-team name | Galatasaray |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9032 |
| Dc lambda away | 1.8387 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.1490 |
| Shot lambda away | 1.6581 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.9% |
| P btts no | 48.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.62 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.75 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.2416622636007157, "-10": 7.618593433471484e-06, "-11": 1.2325936989362078e-06, "-12": 1.831549996977436e-07, "-13": 2.5160417087038563e-08, "-14": 3.2128369077410793e-09, "-15": 3.8150862721768005e-10, "-16": 3.8816048699263413e-11, "-2": 0.18162624158785498, "-3": 0.09638013490520352, "-4": 0.040165025838008905, "-5": 0.01372458031994448, "-6": 0.0039658431998638045, "-7": 0.0009915372158258904, "-8": 0.00021830396610033408, "-9": 4.2916669590171064e-05, "0": 0.23127299991743996, "1": 0.12172275870502301, "10": 1.2819948157422671e-08, "11": 1.0958285837301336e-09, "12": 8.603054414156153e-11, "13": 6.244000625481088e-12, "14": 4.2125492575911175e-13, "15": 2.6428461718780834e-14, "16": 1.4206596857215602e-15, "2": 0.05033851328936563, "3": 0.014113038583065136, "4": 0.0031073649299214923, "5": 0.000560989189997618, "6": 8.564503063005756e-05, "7": 1.1313236329972996e-05, "8": 1.3159842037112825e-06, "9": 1.366867046100984e-07} |
| Raw goal margin distribution | {"-1": 0.23515938343242232, "-10": 7.413585008032465e-06, "-11": 1.1994258844791727e-06, "-12": 1.7822648914954269e-07, "-13": 2.448337643177257e-08, "-14": 3.1263828081228195e-09, "-15": 3.712426268541904e-10, "-16": 3.7771549200098737e-11, "-2": 0.17673886833037866, "-3": 0.0937866457168045, "-4": 0.03908422676706863, "-5": 0.013355266138032415, "-6": 0.0038591264841023156, "-7": 0.0009648559806142048, "-8": 0.00021242963342355678, "-9": 4.176182664775688e-05, "0": 0.2506343343574301, "1": 0.11929600278515826, "10": 1.256436008651165e-08, "11": 1.0739813258219508e-09, "12": 8.431537489543349e-11, "13": 6.119515560874183e-12, "14": 4.1285647262073473e-13, "15": 2.590156414751897e-14, "16": 1.3923363521139746e-15, "2": 0.049334927054369156, "3": 0.013831670494688742, "4": 0.00304541417955162, "5": 0.000549804890099306, "6": 8.39375472695123e-05, "7": 1.1087687192501319e-05, "8": 1.2897477587704969e-06, "9": 1.3396161627733063e-07} |
| Unadjusted home-win probability | 18.6% |
| Unadjusted draw probability | 25.1% |
| Unadjusted away-win probability | 56.3% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 70.2% |
| Raw p btts yes | 52.3% |
| P home draw | 42.1% |
| P draw away | 81.0% |
| P home away | 76.9% |
| Raw p home draw | 43.7% |
| Raw p draw away | 81.4% |
| Raw p home away | 74.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5274 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T12:12:14Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:13:27Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.02, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:13:27Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T12:12:14Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.78 |
| Reference draw odds | 4.14 |
| Reference away odds | 1.66 |
| Market reference 1x2 last update utc | 2026-10-28T12:13:27Z |
| Market reference home last update utc | 2026-10-28T12:13:27Z |
| Market reference draw last update utc | 2026-10-28T12:13:27Z |
| Market reference away last update utc | 2026-10-28T12:13:27Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-28T12:12:14Z |
| Market reference under 2 5 last update utc | 2026-10-28T12:12:14Z |
| Home probability edge | -0.2% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | -0.0054 |
| Raw ev home | -0.1102 |
| Raw edge prob draw | 0.0277 |
| Raw ev draw | 0.0376 |
| Raw edge prob away | -0.0222 |
| Raw ev away | -0.0651 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.0715074146394545, 0.10894151949441375, 0.10923621728316987, 0.0667768830552156, 0.03061589064602959, 0.011229428115410452, 0.0034323149715806108, 0.0008992280392752263, 0.0002061392060897012, 4.200479169670601e-05, 7.703349125368652e-06, 1.2843034276096142e-06, 1.9627597404481293e-07, 2.7688825523786134e-08, 3.627080919400862e-09, 4.4345211581022415e-10, 5.082852352201795e-11], [0.05120559861406873, 0.11195956244116458, 0.09854445512418329, 0.06024093216729679, 0.027619285406355807, 0.010130320350810993, 0.0030963687419914, 0.0008112138937679755, 0.00018596282669860548, 3.7893469888529946e-05, 6.949364973184278e-06, 1.1585990858675567e-06, 1.770649826336898e-07, 2.4978713947928686e-08, 3.2720714959135544e-09, 4.000481544770374e-10, 4.585355736238693e-11], [0.027956857531956023, 0.05127068253828253, 0.04229765613197012, 0.027172351735735987, 0.012457990119857341, 0.004569395224553889, 0.001396652035982333, 0.0003659071740982412, 8.388062991444529e-05, 1.7092276883086285e-05, 3.1345894327624264e-06, 5.225991821385877e-07, 7.986715701614782e-08, 1.1266930588234115e-08, 1.4759047443775404e-09, 1.8044623105256788e-10, 2.0682764096766702e-11], [0.008406837222400144, 0.01541747966086722, 0.014137223833708995, 0.007775352342701569, 0.00374621128058459, 0.0013740514939394695, 0.000419983766394925, 0.00011003103791748368, 2.522353597850135e-05, 5.139776148018513e-06, 9.425946063561593e-07, 1.5714950264981236e-07, 2.401665450715093e-08, 3.388050725769041e-09, 4.438156515827106e-10, 5.4261538161810956e-11, 6.2194626442571465e-12], [0.001895999362673747, 0.0034771140248977175, 0.0031883771113431643, 0.0019490777948504802, 0.0008039821030223975, 0.00030989071012919677, 9.47192068018605e-05, 2.481537018583066e-05, 5.688680162878574e-06, 1.159176994049926e-06, 2.1258396298539934e-07, 3.544202760041958e-08, 5.416491414605193e-09, 7.641092418975678e-10, 1.0009402707397885e-10, 1.2237639322712936e-11, 1.4026793784307503e-12], [0.0003420847567911342, 0.0006273565956608681, 0.0005752613793889372, 0.000351661406931157, 0.00016122985510016706, 5.320502580898687e-05, 1.708966651579996e-05, 4.477301016984876e-06, 1.0263773333956153e-06, 2.0914394165631417e-07, 3.835535744748527e-08, 6.394610478548172e-09, 9.772678117430996e-10, 1.3786403588647513e-10, 1.8059415832060702e-11, 2.2079700836525192e-12, 2.530777401474211e-13], [5.143372897544318e-05, 9.432542219903451e-05, 8.649271062257698e-05, 5.2873614319692264e-05, 2.424151472798652e-05, 8.891407086401091e-06, 2.4450989717768477e-06, 6.731790367077955e-07, 1.5431968991427546e-07, 3.144557773608915e-08, 5.766872158278322e-09, 9.614537208332567e-10, 1.4693588874615914e-10, 2.072837598424528e-11, 2.7153010501668487e-12, 3.3197660116088955e-13, 3.805118947292844e-14], [6.628503835802024e-06, 1.2156155801156519e-05, 1.1146717835768701e-05, 6.8140685560272876e-06, 3.124116733531575e-06, 1.14587697901558e-06, 3.5024140768730314e-07, 8.25556209965923e-08, 1.9887896073507275e-08, 4.052537834505352e-09, 7.432036327752644e-10, 1.2390701206074581e-10, 1.8936311280014536e-11, 2.6713622064446576e-12, 3.499334733241191e-13, 4.2783368385405185e-14, 4.903833737168042e-15], [7.474653496724346e-07, 1.3707927869796044e-06, 1.2569631927813016e-06, 7.683906145475755e-07, 3.5229202011378745e-07, 1.292151830968715e-07, 3.949508407202722e-08, 1.0347269206107926e-08, 2.1340911273127825e-09, 4.5698572175040475e-10, 8.380759474705368e-11, 1.3972413743899682e-11, 2.1353591825612223e-12, 3.0123701142888197e-13, 3.9460359755325414e-14, 4.8244801847492825e-15, 5.529823757949577e-16], [7.492281654447824e-08, 1.3740256527526693e-07, 1.2599276038305446e-07, 7.702027802824046e-08, 3.531228625465516e-08, 1.295199230595865e-08, 3.958822893441165e-09, 1.0371672115708013e-09, 2.377604080804649e-10, 4.358873113315058e-11, 8.400524584877682e-12, 1.4005366162812888e-12, 2.140395195064405e-13, 3.019474461737092e-14, 3.955342272418368e-15, 4.8358581968093495e-16, 5.54286524615112e-17], [6.758956247638456e-09, 1.2395395285993964e-08, 1.1366091055088904e-08, 6.948172978318084e-09, 3.185600979877861e-09, 1.1684284354653807e-09, 3.5713434121945487e-10, 9.356519319225817e-11, 2.1448902614099113e-11, 4.370622665715109e-12, 7.211415391592503e-13, 1.2634556666781495e-13, 1.9308987760100556e-14, 2.7239360076148623e-15, 3.568203465474349e-16, 4.3625367384065706e-17, 5.000343742156376e-18], [5.543097145528407e-10, 1.0165605118615163e-09, 9.321460973399895e-10, 5.698275945521813e-10, 2.612547714674602e-10, 9.58241492929519e-11, 2.928899485146691e-11, 7.673388261479437e-12, 1.7590489788489207e-12, 3.5843975215806276e-13, 6.573503735529058e-14, 9.860102457366915e-15, 1.5835521198032996e-15, 2.2339310028360546e-16, 2.9263243790113424e-17, 3.577766160325912e-18, 4.100838962153683e-19], [4.167127453178744e-11, 7.642184694909839e-11, 7.007583469346917e-11, 4.283786032421848e-11, 1.9640318433427185e-11, 7.2037605099214485e-12, 2.2018552321424967e-12, 5.768613835156283e-13, 1.3223981284832073e-13, 2.6946382001141377e-14, 4.9417549721266706e-15, 8.238900698669045e-16, 1.1328312510681146e-16, 1.679399614696422e-17, 2.19991934771007e-18, 2.6896529496646187e-19, 3.0828827587914523e-20], [2.891738194809477e-12, 5.303220893136257e-12, 4.862845449127853e-12, 2.972692298839139e-12, 1.3629210915744433e-12, 4.998980627988609e-13, 1.5279563550115478e-13, 4.0030743349361825e-14, 9.176655189565744e-15, 1.8699183771110057e-15, 3.4292835443244055e-16, 5.717306250234779e-17, 8.737575786634363e-18, 1.1089827791009282e-18, 1.526612966546259e-19, 1.8664589102966258e-20, 2.1393369710629924e-21], [1.8633587432073453e-13, 3.417253690573594e-13, 3.13348753381716e-13, 1.9155234024468815e-13, 8.782298953776001e-14, 3.221209401669377e-14, 9.845742046982154e-15, 2.5794740253806804e-15, 5.913191142811248e-16, 1.2049253847834759e-16, 2.2097385879273764e-17, 3.684079218544498e-18, 5.630260120257751e-19, 7.94265782564679e-20, 9.360844188719277e-21, 1.2026961969036801e-21, 1.3785315201951013e-22], [1.1206519633456284e-14, 2.0551877471536678e-14, 1.884526514119833e-14, 1.152024573696236e-14, 5.2818066306956865e-15, 1.9372837643247626e-15, 5.92137729557823e-16, 1.551334460677307e-16, 3.5562820567891194e-17, 7.246602421916636e-18, 1.3289700097035236e-18, 2.21566063133733e-19, 3.3861230860209867e-20, 4.776833832422758e-21, 6.257384530031864e-22, 6.883016076856342e-23, 8.290695821575194e-24], [6.318533807877678e-16, 1.158769509773426e-15, 1.0625461678360145e-15, 6.495420928612192e-16, 2.978023048573404e-16, 1.0922921085860153e-16, 3.3386299988813816e-17, 8.74683626828403e-18, 2.005126403302479e-18, 4.085827169608656e-19, 7.493086355640834e-20, 1.249248389668931e-20, 1.9091862501881864e-21, 2.693305955103945e-22, 3.5280798138130837e-23, 4.313480986360763e-24, 4.448208178149567e-25]] |
| Legacy trial inputs | {"lambda_home": 0.9021225521635317, "lambda_away": 1.8339215156666906, "rho": -0.09479091437752254, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1813 |
| Legacy p draw | 0.2344 |
| Legacy p away | 0.5843 |
| Legacy p over 1 5 | 0.7683 |
| Legacy p under 3 5 | 0.7058 |
| Legacy p btts yes | 0.5072 |
| Legacy p over 2 5 | 0.5192 |
| Legacy goal margin distribution | {"-1": 0.23873221154400961, "-10": 8.945305759026474e-06, "-11": 1.4730916472001838e-06, "-12": 2.2278625695465938e-07, "-13": 3.1147562713396514e-08, "-14": 4.047811837974666e-09, "-15": 4.893056731726111e-10, "-16": 5.082852352201795e-11, "-2": 0.18340854602953774, "-3": 0.09941142140301001, "-4": 0.04225879778779003, "-5": 0.014718126080525359, "-6": 0.004332768399631715, "-7": 0.0011032621778418756, "-8": 0.00024732997202773127, "-9": 4.950155501207419e-05, "0": 0.23439970251712589, "1": 0.1187330648739718, "10": 7.848655080151883e-09, "11": 6.357913503271531e-10, "12": 4.729966222634723e-11, "13": 3.2529583711008957e-12, "14": 2.079502979601072e-13, "15": 1.236528914322971e-14, "16": 6.318533807877678e-16, "2": 0.046939803656868194, "3": 0.01251534362709755, "4": 0.002617028346467501, "5": 0.0004483617980303298, "6": 6.492715191502305e-05, "7": 8.13250617008606e-06, "8": 8.968239838167194e-07, "9": 8.829459152220658e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1711 |
| Legacy raw p draw | 0.2458 |
| Legacy raw p away | 0.5831 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9021 |
| Legacy lambda away | 1.8339 |
| Legacy model home team | Konyaspor |
| Legacy model away team | Galatasaray |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,456.7365 |
| Elo away rating | 1,677.5170 |
| Elo rating diff | -160.7805 |
| Elo home expectancy | 0.2838 |

</details>


---

## 2026-10-31 — Erzurum BB vs Çorum FK

The model's most likely 1X2 outcome is **Çorum FK win** at **37.1%**. Expected goals are 1.26 for Erzurum BB and 1.48 for Çorum FK (2.74 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 47.4%; Under 3.5 goals: 74.3%; Double Chance 1X: 62.9%; Double Chance X2: 65.9%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 88.2%; BTTS Yes (both teams score): 53.3%; BTTS No (at least one team does not score): 46.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Erzurum BB win | 34.1% | 2.93 |
| Draw | 28.8% | 3.47 |
| Çorum FK win | 37.1% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Erzurum BB expected goals | 1.26 |
| Çorum FK expected goals | 1.48 |
| Expected total goals | 2.74 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 25.7% |
| Under 3.5 | 74.3% |
| Over 4.5 | 11.8% |
| Under 4.5 | 88.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.75% |
| 2 | 0-0 | 8.85% |
| 3 | 1-0 | 8.69% |
| 4 | 0-1 | 8.64% |
| 5 | 2-1 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Erzurum BB win | 34.1% | 35.4% | 2.70 | -7.8% |
| Draw | 28.8% | 29.2% | 3.24 | -6.7% |
| Çorum FK win | 37.1% | 35.4% | 2.70 | +0.1% |
| Over 2.5 | 47.4% | 47.4% | 2.02 | -4.3% |
| Under 2.5 | 52.6% | 52.6% | 1.83 | -3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T10:30:00+00:00 |
| Fixture id | 7ef8c62daf5d4e448691625fb8c2de1b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T12:13:27Z |
| Market best draw last update utc | 2026-10-28T12:13:27Z |
| Market best away last update utc | 2026-10-28T12:13:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Erzurumspor |
| Matched away-team name | Corum |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2394 |
| Dc lambda away | 1.5081 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.3507 |
| Shot lambda away | 1.3444 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.3% |
| P btts no | 46.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.30 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.89 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.46 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.19155530541380805, "-10": 5.864099446453064e-07, "-11": 7.296540275243178e-08, "-12": 8.335882003334803e-09, "-13": 8.75578229518885e-10, "-14": 7.755953011381085e-11, "-2": 0.1129633514168899, "-3": 0.04629672910386005, "-4": 0.014876691743507508, "-5": 0.003916048096861534, "-6": 0.0008712136371436106, "-7": 0.00016763844913489546, "-8": 2.8398020731688577e-05, "-9": 4.294699128220532e-06, "0": 0.2879518165208617, "1": 0.1950229459566154, "10": 1.4747939178276436e-07, "11": 1.5692705488696243e-08, "12": 1.5331449884053379e-09, "13": 1.3771379709743003e-10, "14": 1.0432022056881025e-11, "2": 0.09932554288842424, "3": 0.03481164265435589, "4": 0.00956602256814849, "5": 0.0021533959064804495, "6": 0.00040968622317096964, "7": 6.741416481495138e-05, "8": 9.765993367606562e-06, "9": 1.263024939649619e-06} |
| Raw goal margin distribution | {"-1": 0.20518688221650425, "-10": 1.0316865026629714e-06, "-11": 1.3647266319324588e-07, "-12": 1.6582953427020413e-08, "-13": 1.8625960287953527e-09, "-14": 1.9334380181001449e-10, "-15": 1.691752566643406e-11, "-2": 0.12575855672810998, "-3": 0.05412845982590481, "-4": 0.01835269365657705, "-5": 0.005111317549922877, "-6": 0.0012051158260023016, "-7": 0.000246023519930938, "-8": 4.42508241839796e-05, "-9": 7.109422973135418e-06, "0": 0.2776251239355848, "1": 0.1737919940301935, "10": 2.1580228517685512e-07, "11": 2.4412080091057626e-08, "12": 2.5367158911010523e-09, "13": 2.436573127821316e-10, "14": 2.1629269932862767e-11, "15": 1.618449972826194e-12, "2": 0.09196852104603268, "3": 0.0338515186604824, "4": 0.009815289907483617, "5": 0.0023376904805963855, "6": 0.000471339421065121, "7": 8.228722772167e-05, "8": 1.2656918869535016e-05, "9": 1.738968898070727e-06} |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 41.0% |
| Raw p over 1 5 | 77.0% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 56.4% |
| P home draw | 62.9% |
| P draw away | 65.9% |
| P home away | 71.2% |
| Raw p home draw | 59.0% |
| Raw p draw away | 68.8% |
| Raw p home away | 72.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9391 |
| Totals anchor target over 2 5 | 0.4738 |
| Totals anchor reference over odds | 2.02 |
| Totals anchor reference under odds | 1.83 |
| Totals anchor reference last update utc | 2026-10-28T12:13:27Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5112 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T12:12:14Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:13:27Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T12:12:14Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T12:13:27Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.70 |
| Reference draw odds | 3.24 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-10-28T12:13:27Z |
| Market reference home last update utc | 2026-10-28T12:13:27Z |
| Market reference draw last update utc | 2026-10-28T12:13:27Z |
| Market reference away last update utc | 2026-10-28T12:13:27Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-10-28T12:13:27Z |
| Market reference under 2 5 last update utc | 2026-10-28T12:13:27Z |
| Market best over 2 5 last update utc | 2026-10-28T12:13:27Z |
| Market best under 2 5 last update utc | 2026-10-28T12:13:27Z |
| Home probability edge | -1.2% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0415 |
| Raw ev home | -0.1567 |
| Raw edge prob draw | -0.0148 |
| Raw ev draw | -0.1005 |
| Raw edge prob away | 0.0562 |
| Raw ev away | 0.1071 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.07826183771126102, 0.07872109341687741, 0.06686480819008271, 0.03341511210239792, 0.012524185895085995, 0.003755312431189838, 0.0009383425247479314, 0.00020096939846847816, 3.766227235643794e-05, 6.273798763438181e-06, 9.405830720049789e-07, 1.2819498835205768e-07, 1.6016085376974733e-08, 1.8470540188579521e-09, 1.9779628723977023e-10, 1.9769398254357985e-11], [0.0745904861183084, 0.13534890757099885, 0.08286158458702414, 0.04140936335428549, 0.015520479561970895, 0.004653735606077645, 0.001162832147292911, 0.0002490494366372692, 4.667261674827311e-05, 7.77474610322302e-06, 1.1656087244055422e-06, 1.5886443345158815e-07, 1.9847783148416002e-08, 2.288944318591513e-09, 2.451171883949028e-10, 2.4499040826247602e-11], [0.05387396004649137, 0.08076914283083005, 0.05742298758350513, 0.025658082010208028, 0.009616804152039544, 0.0028835490372784963, 0.0007205144001872239, 0.0001543160858369932, 2.891930064011155e-05, 4.8173904877095076e-06, 7.222348237217283e-07, 9.843562739981704e-08, 1.2298089284441496e-08, 1.418276357951849e-09, 1.518795850141258e-10, 1.5180102947084827e-11], [0.02225426607441416, 0.03336413349990438, 0.02501015761376318, 0.011854015199217388, 0.003972511361710395, 0.0011911370067995534, 0.0002976302309757101, 6.374491926739734e-05, 1.19459904298038e-05, 1.9899686157342587e-06, 2.983409038697113e-07, 4.0661808440793996e-08, 5.08009715466771e-09, 5.858618785341561e-10, 6.273844902545059e-11, 6.270599928609212e-12], [0.006894597474597682, 0.010336547150168655, 0.007748400641322023, 0.003872196496967878, 0.0013764730166320703, 0.00036902633281723417, 9.220886602089731e-05, 1.97488228966904e-05, 3.7009890676011232e-06, 6.165124721117652e-07, 9.242903969563733e-08, 1.2597440906433177e-08, 1.5738656532713764e-09, 1.8150595551873215e-10, 1.9437008201693036e-11, 1.94269549431275e-12], [0.0017088130132992525, 0.002561893765062796, 0.001920426521915258, 0.0009597166170250718, 0.00035970758623797946, 0.00010229393817635902, 2.2853793971093447e-05, 4.894708601559953e-06, 9.172831777484016e-07, 1.5280145637035203e-07, 2.2908363602165872e-08, 3.122252029142207e-09, 3.9007964125589407e-10, 4.498590960885986e-11, 4.817425916020645e-12, 4.814934234798333e-13], [0.000352938408802377, 0.0005291337916582504, 0.00039664508380470595, 0.00019821996501539465, 7.429404044381745e-05, 2.2276684167667616e-05, 5.279218083903224e-06, 1.0109535987500974e-06, 1.894557582696812e-07, 3.155962791383165e-08, 4.731495684483529e-09, 6.448702429517747e-10, 8.056708769161706e-11, 9.291394220613933e-12, 9.94991625234016e-13, 9.944769931478832e-14], [6.248222902856734e-05, 9.367486771794606e-05, 7.021981272437247e-05, 3.509174672757543e-05, 1.3152598682076294e-05, 3.9437387585113794e-06, 9.854247419928638e-07, 2.0016849695912674e-07, 3.35401809033922e-08, 5.587138861025874e-09, 8.376373600389702e-10, 1.1416419751691611e-10, 1.426314365272444e-11, 1.64489612693918e-12, 1.7614771602880175e-13, 1.7605660846139265e-14], [9.678814323220391e-06, 1.4510712333577271e-05, 1.0877405299669627e-05, 5.435889630288166e-06, 2.037404274636976e-06, 6.109051449727796e-07, 1.526472927669652e-07, 3.269321574598743e-08, 5.810827179937887e-09, 8.654761597764722e-10, 1.2975427740106656e-10, 1.7684613486188e-11, 2.2094333257064447e-12, 2.548027565781887e-13, 2.7286175019822523e-14, 2.727206199533377e-15], [1.3327088451632857e-06, 1.9980293071831525e-06, 1.4977469110568062e-06, 7.484861213047843e-07, 2.805371202821822e-07, 8.411760604888751e-08, 2.1018524631958876e-08, 4.50164000945645e-09, 8.436209362162127e-10, 1.332831184662586e-10, 1.7866307526461107e-11, 2.4350545458645445e-12, 3.042243850988344e-13, 3.508465769914195e-14, 3.757126191825898e-15, 3.755182921509919e-16], [1.6515469002684063e-07, 2.476039024502359e-07, 1.8560687709995498e-07, 9.275543852066074e-08, 3.47652987442652e-08, 1.0424195204543565e-08, 2.6047008939806147e-09, 5.578615037128482e-10, 1.0454493097017828e-10, 1.741514299607355e-11, 2.4762663189902774e-12, 3.0176184406687467e-13, 3.77007207552886e-14, 4.347833203050182e-15, 4.655983291884768e-16, 4.653575112425027e-17], [1.8606036008303503e-08, 2.789461882091782e-08, 2.091014332169001e-08, 1.0449664062225053e-08, 3.916597222701353e-09, 1.1743714411125798e-09, 2.9344100743604375e-10, 6.284769281478303e-11, 1.177784748226415e-11, 1.9619592856977825e-12, 2.941416774227234e-13, 3.80219324055775e-14, 4.247296687716799e-15, 4.898192180973013e-16, 5.245348634591523e-17, 5.242635622097896e-18], [1.9214462588307733e-09, 2.880678665302125e-09, 2.1593915350451883e-09, 1.0791373245456525e-09, 4.0446718890299994e-10, 1.212773968080274e-10, 3.030366735149243e-11, 6.490284345425238e-12, 1.2162988920249511e-12, 2.026116324723823e-13, 3.037602557567192e-14, 4.140042874208197e-15, 4.905619939922829e-16, 5.058365487933338e-17, 5.416874129288519e-18, 5.414072399944496e-19], [1.8316416940066557e-10, 2.7460414914823387e-10, 2.0584658827151453e-10, 1.0287005988912713e-10, 3.8556319941168255e-11, 1.15609133231416e-11, 2.8887334395747103e-12, 6.186941403333082e-13, 1.1594515083459381e-13, 1.93141968983819e-14, 2.895631074088417e-15, 3.946545529714317e-16, 4.930630359311382e-17, 5.392987317419671e-18, 5.163700239229375e-19, 5.161029457125401e-20], [1.6213176714251944e-11, 2.4307186340948923e-11, 1.8220960587392037e-11, 9.105768148025342e-12, 3.4128969148434624e-12, 1.0233395062995507e-12, 2.5570255301266047e-13, 5.476506383382024e-14, 1.026313839542372e-14, 1.7096383448354973e-15, 2.563131122047065e-16, 3.493371017566864e-17, 4.364455209211923e-18, 5.033305170743986e-19, 5.1120551769732e-20, 4.568398005441441e-21], [1.3394684489467257e-12, 2.0081634685292522e-12, 1.5053436008539499e-12, 7.522825016137965e-13, 2.819600265580255e-13, 8.454425714388517e-14, 2.1125132237318548e-14, 4.524472680635936e-15, 8.478998477676233e-16, 1.4124354914380573e-16, 2.1175574219687196e-17, 2.886084782128169e-18, 3.6057400425677656e-19, 4.158317391437282e-20, 4.453035659993413e-21, 4.221193101731623e-22]] |
| Legacy trial inputs | {"lambda_home": 1.2392405935191786, "lambda_away": 1.4992241662043977, "rho": -0.09479091437752254, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-28T12:13:27Z", "over": 2.02, "under": 1.83, "bookmaker": "pinnacle", "event_id": "7ef8c62daf5d4e448691625fb8c2de1b", "kickoff_utc": "2026-10-31T10:30:00Z", "home_team": "Erzurum BB", "away_team": "\u00c7orum FK"}} |
| Legacy p home | 0.3281 |
| Legacy p draw | 0.2844 |
| Legacy p away | 0.3875 |
| Legacy p over 1 5 | 0.7684 |
| Legacy p under 3 5 | 0.7070 |
| Legacy p btts yes | 0.5655 |
| Legacy p over 2 5 | 0.5123 |
| Legacy goal margin distribution | {"-1": 0.1916061968800365, "-10": 1.112351375121168e-06, "-11": 1.495257290029453e-07, "-12": 1.846317988050898e-08, "-13": 2.10735131019994e-09, "-14": 2.2229532806601784e-10, "-15": 1.9769398254357985e-11, "-2": 0.1191794114529544, "-3": 0.052137469453955976, "-4": 0.017966039459047106, "-5": 0.005085046734977254, "-6": 0.0012183968641724166, "-7": 0.0002527707435991473, "-8": 4.6201534955983645e-05, "-9": 7.543109635227342e-06, "0": 0.28437200035299676, "1": 0.18462498630956733, "10": 1.9531506788386478e-07, "11": 2.1701948990051725e-08, "12": 2.215023651068013e-09, "13": 2.0897669934246844e-10, "14": 1.8221340182781196e-11, "15": 1.3394684489467257e-12, "2": 0.0960246058394156, "3": 0.034723244803710036, "4": 0.009890352260857906, "5": 0.0023138937686766176, "6": 0.0004582751385442487, "7": 7.858748453068799e-05, "8": 1.1873316459894976e-05, "9": 1.6023416290443367e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3024 |
| Legacy raw p draw | 0.2764 |
| Legacy raw p away | 0.4212 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2392 |
| Legacy lambda away | 1.4992 |
| Legacy model home team | Erzurumspor |
| Legacy model away team | Corum |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,438.6446 |
| Elo away rating | 1,451.6385 |
| Elo rating diff | 47.0060 |
| Elo home expectancy | 0.5672 |

</details>


---
