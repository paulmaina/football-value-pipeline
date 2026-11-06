# Super Lig — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,840 |
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
| Training sha256 | 428b36b889bc8107b0a0c389334f72426054f163962dc5b037f54c55da735d9c |
| Training as of utc | 2026-11-06T13:39:26.376264+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-06', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1809, 'tune_start_date': '2025-11-07', 'audit_start_date': '2026-05-08', 'training_shot_matches': 1512, 'tuning_matches': 189, 'audit_matches': 91, 'audit_matchdays': 37, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8325688020301171, 'audit_candidate_poisson_score': 0.824985919365649, 'audit_gain': 0.007582882664468049, 'audit_gain_lower95': -0.0033653303999722837, 'audit_baseline_briers': [0.5922589538722137, 0.1664907523353062, 0.2201651393758508, 0.2497293837734222], 'audit_candidate_briers': [0.5911030741495769, 0.16507679461400995, 0.21631943856751462, 0.24937701251274844], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1669.650 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1840, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 36.00 |
| Over 1 5 in window quote fixtures | 7 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 5, 'ANCHORED_MAIN': 2, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
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

## 2026-11-06 — Gazişehir Gaziantep vs Kasimpasa SK

The model's most likely 1X2 outcome is **Gazişehir Gaziantep win** at **37.0%**. Expected goals are 1.39 for Gazişehir Gaziantep and 1.41 for Kasimpasa SK (2.81 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.4%; Double Chance 1X: 64.1%; Double Chance X2: 63.0%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 60.1%; BTTS No (at least one team does not score): 39.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gazişehir Gaziantep win | 37.0% | 2.70 |
| Draw | 27.0% | 3.70 |
| Kasimpasa SK win | 35.9% | 2.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gazişehir Gaziantep expected goals | 1.39 |
| Kasimpasa SK expected goals | 1.41 |
| Expected total goals | 2.81 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 80.0% |
| Under 1.5 | 20.0% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.6% |
| Under 3.5 | 66.4% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.66% |
| 2 | 2-1 | 8.55% |
| 3 | 1-2 | 8.20% |
| 4 | 1-0 | 6.87% |
| 5 | 0-1 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Gazişehir Gaziantep win | 37.0% | 37.6% | 2.62 | -3.0% |
| Draw | 27.0% | 26.8% | 3.60 | -2.7% |
| Kasimpasa SK win | 35.9% | 35.6% | 2.73 | -1.9% |
| Over 2.5 | 55.9% | 57.2% | 1.77 | -1.1% |
| Under 2.5 | 44.1% | 42.8% | 2.14 | -5.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T17:00:00+00:00 |
| Fixture id | 51baab3ec98943f452377895491bfd6a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:38:36Z |
| Market best draw last update utc | 2026-11-06T13:39:23Z |
| Market best away last update utc | 2026-11-06T13:39:23Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Gaziantep |
| Matched away-team name | Kasimpasa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3919 |
| Dc lambda away | 1.4142 |
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
| P btts yes | 60.1% |
| P btts no | 39.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.34 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.00 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.98 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.82 |
| Fair Under 4.5 odds | 1.21 |
| Score matrix json | [[0.06517009894822351,0.06602789987893595,0.05655485847169628,0.027776303524982573,0.010231521990697918,0.0030150604352945725,0.0007404070672267763,0.00015584694719748872,2.870344979489574e-05,4.699129041914419e-06,6.923778333028527e-07,9.274195664252707e-08,1.1387300785540954e-08,1.290634363342927e-09,1.3583164881755676e-10,1.3342447343382542e-11],[0.06868543333779326,0.12658800082975613,0.08201299945527617,0.0402797925310705,0.014837236448389371,0.004372288367783478,0.0010737009346693347,0.00022600137178330621,4.162429322622129e-05,6.81443960730047e-06,1.004051365346985e-06,1.3448970159498104e-07,1.6513288484118895e-08,1.8716127702941347e-09,1.9697619694440053e-10,1.9348543277718913e-11],[0.05805356642759166,0.08553713290295988,0.06167023805973927,0.029205860399797404,0.010758105471774365,0.0031702358843740687,0.00077851343412198,0.00016386788758592774,3.018072390188011e-05,4.940978077783024e-06,7.280122902304007e-07,9.751508642860024e-08,1.1973368478418551e-08,1.357059156884288e-09,1.4282246626775937e-10,1.4029140132055162e-11],[0.02806211668024772,0.041347210029044464,0.03046084863564937,0.014641031507671515,0.005200287072524439,0.001532438655636683,0.000376320287793517,7.921097814580536e-05,1.4588853842171019e-05,2.38838562151444e-06,3.5190888502226665e-07,4.71371511146855e-08,5.787724751003214e-09,6.559795503689489e-10,6.90379757799296e-11,6.781450159488675e-12],[0.010173566083464126,0.01498990893632195,0.011043196066934798,0.005423745618505736,0.001955195785251426,0.0005555662856661281,0.0001364301688300794,2.87169399901116e-05,5.289004758140583e-06,8.658790507551336e-07,1.2758012297954016e-07,1.7088978971747846e-08,2.0982665312869186e-09,2.3781710343243695e-10,2.502884642911083e-11,2.458529131119961e-12],[0.0029506383437558417,0.004347521774966396,0.0032028570400376663,0.001573048393989645,0.000579439205114576,0.00016710475325892285,3.956882808766736e-05,8.328771205200336e-06,1.5339695158654562e-06,2.51130813645146e-07,3.7002050183404046e-08,4.956314845355303e-09,6.085600301646264e-10,6.89740704912945e-11,7.2591138021648746e-12,7.130469556111838e-13],[0.000713144450711435,0.0010507594177800617,0.0007741035865539197,0.000380192555705186,0.00014004557845137867,4.1269117450031655e-05,9.918017322941017e-06,2.012993892932783e-06,3.707475198087096e-07,6.069620376644264e-08,8.943084064871136e-09,1.1978995783823234e-09,1.4708383674166693e-10,1.6670452249066362e-11,1.7544667024516355e-12,1.723374471042515e-13],[0.00014773800929941553,0.00021767974844447602,0.00016036656073664112,7.876229181101677e-05,2.901243212500826e-05,8.549484261609334e-06,2.09949309617112e-06,4.32481308414541e-07,7.680561837730373e-08,1.2574081320467799e-08,1.852686977264312e-09,2.4816192410143907e-10,3.04705073686773e-11,3.453521130173659e-12,3.634627146628351e-13,3.570215169945679e-14],[2.6780274948129346e-05,3.945852216113326e-05,2.906943588436536e-05,1.4277137212327191e-05,5.259045474526612e-06,1.5497537856123556e-06,3.8057235665882513e-07,8.010598844657652e-08,1.4438628025782699e-08,2.2792872096970725e-09,3.35834135570373e-10,4.498398611574927e-11,5.523348859320305e-12,6.260152403826311e-13,6.588440901716358e-14,6.471682157389533e-15],[4.315044688143648e-06,6.357861776370218e-06,4.683891974340056e-06,2.300442591021784e-06,8.473780154802744e-07,2.497082966283818e-07,6.132075675980627e-08,1.2907295410685899e-08,2.377229149949501e-09,3.808723705378784e-10,5.411218912416271e-11,7.2481671945586325e-12,8.89964617702298e-13,1.008684094148455e-13,1.0615804718646238e-14,1.042767401405951e-15],[6.257459875623702e-07,9.219850044592137e-07,6.792343581451475e-07,3.335985661758559e-07,1.2288248012640137e-07,3.621143602650966e-08,8.892426445123177e-09,1.871750792224941e-09,3.4473376514141074e-10,5.643741289218062e-11,8.13800643162809e-12,1.0510925997217109e-12,1.2905817409721174e-13,1.4627427297929476e-14,1.5394503852279504e-15,1.5121686206019922e-16],[8.249320253566074e-08,1.2154691715081126e-07,8.954466922580505e-08,4.397889020807813e-08,1.6199815136874767e-08,4.773817788075292e-09,1.1723043381047566e-09,2.467562242001676e-10,4.544686322236588e-11,7.440244164313265e-12,1.0962584955174408e-12,1.4370478134443217e-13,1.7013967818087984e-14,1.92835966454116e-15,2.029484726173371e-16,1.9935186923584906e-17],[9.968956333502634e-09,1.4688433377580406e-08,1.082109640517471e-08,5.314663785670251e-09,1.9576794783849885e-09,5.768957879026238e-10,1.416680453288262e-10,2.981945116033134e-11,5.492062146121449e-12,8.991221931597743e-13,1.3247822530978097e-13,1.774506524732212e-14,2.1322949870778652e-15,2.330341494838734e-16,2.4525468757243272e-17,2.409083437578035e-18],[1.1120366917838882e-09,1.6384941727348816e-09,1.2070928836797308e-09,5.928505388571446e-10,2.183790697728484e-10,6.435270273251256e-11,1.5803064953701672e-11,3.3263586186754885e-12,6.126393190748951e-13,1.0029704572289621e-13,1.4777940887531974e-14,1.9794613390776088e-15,2.4304772594252444e-16,2.6958712118195533e-17,2.7358150872420716e-18,2.687331638872131e-19],[1.1518710336185186e-10,1.6971867837368356e-10,1.2503322398178037e-10,6.140870782592723e-11,2.2620164125734293e-11,6.66578852661186e-12,1.6369147616307704e-12,3.4455123365877386e-13,6.345847137167002e-14,1.038897930070891e-14,1.5307302511366155e-15,2.0503677580940207e-16,2.517539550344739e-17,2.8533742244479286e-18,2.9388784850878675e-19,2.7835947279561143e-20],[1.1135901318420138e-11,1.6407830382927693e-11,1.2087791108098612e-11,5.9367871096904186e-12,2.1868413056566915e-12,6.444259910644691e-13,1.5825140766776564e-13,3.331005316724321e-14,6.134951347745615e-15,1.0043715391329023e-15,1.4798584671609346e-16,1.982226512709336e-17,2.433872471798226e-18,2.758546127178597e-19,2.903206976633053e-20,2.790857557949331e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1830442740542668, "-10": 8.395226248200059e-07, "-11": 1.106838007884413e-07, "-12": 1.3408517472262337e-08, "-13": 1.5016397004193827e-09, "-14": 1.5518019209527568e-10, "-15": 1.3342447343382542e-11, "-2": 0.10927033773502755, "-3": 0.04619040964982503, "-4": 0.015467084103192731, "-5": 0.0042681222214998125, "-6": 0.0009991102355755871, "-7": 0.00020278184196590387, "-8": 3.629520787431193e-05, "-9": 5.80672846699569e-06, "0": 0.27020203521031644, "1": 0.1907300508513383, "10": 7.587301162473302e-07, "11": 9.845232434605246e-08, "12": 1.1738420517328986e-08, "13": 1.2938431612656703e-09, "14": 1.3159493374477955e-10, "15": 1.1135901318420138e-11, "2": 0.11216600981223411, "3": 0.04666570063709167, "4": 0.01537947163534319, "5": 0.004176926251683344, "6": 0.0009623218789880795, "7": 0.0001922308148657406, "8": 3.386337367525872e-05, "9": 5.332114228724045e-06} |
| Raw goal margin distribution | {"-1": 0.190727209787534, "-10": 6.366549210268008e-07, "-11": 8.066312623943879e-08, "-12": 9.385419726573456e-09, "-13": 1.0021561538540512e-09, "-14": 8.875498223572365e-11, "-2": 0.11124796764106362, "-3": 0.045597666307939086, "-4": 0.014754957866606867, "-5": 0.003926891020161624, "-6": 0.0008854625910730416, "-7": 0.00017297110151691196, "-8": 2.9780587143353162e-05, "-9": 4.581165563197571e-06, "0": 0.2754226378113556, "1": 0.1875340509589345, "10": 5.429677267710962e-07, "11": 6.770674843812721e-08, "12": 7.753496567762195e-09, "13": 8.148286462324105e-10, "14": 7.102489888214793e-11, "2": 0.10776210568292117, "3": 0.04347139639287619, "4": 0.013844776212097109, "5": 0.0036264676436101547, "6": 0.0008048077829534395, "7": 0.00015473283846854151, "8": 2.6219788783318387e-05, "9": 3.9697111947691085e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 27.5% |
| Unadjusted away-win probability | 36.7% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 58.0% |
| P home draw | 64.1% |
| P draw away | 63.0% |
| P home away | 73.0% |
| Raw p home draw | 63.3% |
| Raw p draw away | 64.3% |
| Raw p home away | 72.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0419 |
| Totals anchor target over 2 5 | 0.5589 |
| Totals anchor reference over odds | 1.74 |
| Totals anchor reference under odds | 2.18 |
| Totals anchor reference last update utc | 2026-11-06T13:39:23Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5339 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.9, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.6, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.28, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.6, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.72, "draw": 3.54, "home": 2.62}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.77, "under": 2.14}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.53, "home_away": 1.32, "home_draw": 1.5}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.73, "draw": 3.6, "home": 2.59}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.74, "under": 2.18}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.23, "under": 4.37}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.59 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.73 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:23Z |
| Market reference home last update utc | 2026-11-06T13:39:23Z |
| Market reference draw last update utc | 2026-11-06T13:39:23Z |
| Market reference away last update utc | 2026-11-06T13:39:23Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:22Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:22Z |
| Market best over 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market best under 2 5 last update utc | 2026-11-06T13:38:36Z |
| Home probability edge | -0.6% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -1.3% |
| Under 2.5 probability edge | +1.3% |
| Raw edge prob home | -0.0187 |
| Raw ev home | -0.0641 |
| Raw edge prob draw | 0.0075 |
| Raw ev draw | -0.0085 |
| Raw edge prob away | 0.0112 |
| Raw ev away | 0.0029 |
| Market p home draw | 64.4% |
| Market home draw odds | 1.50 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T13:38:36Z |
| Market reference home draw last update utc | 2026-11-06T13:39:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.1% |
| Market draw away odds | 1.53 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T13:38:36Z |
| Market reference draw away last update utc | 2026-11-06T13:39:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.4% |
| Market home away odds | 1.32 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T13:38:36Z |
| Market reference home away last update utc | 2026-11-06T13:39:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.48 |
| Market reference dc home draw odds | 1.45 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 78.5% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 68.5% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market reference under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,396.7846 |
| Elo away rating | 1,500.7901 |
| Elo rating diff | -44.0056 |
| Elo home expectancy | 0.4370 |
| Research p home | 0.3687 |
| Research p draw | 0.2525 |
| Research p away | 0.3788 |
| Research p over 1 5 | 0.7700 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.3918984749925523, 1.4142316989065902], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:18.192876+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-06T13:40:18.194352+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:18.195889+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Gazi%C5%9Fehir+Gaziantep%22+%22Kasimpasa+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:18.281943+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Gazi%C5%9Fehir+Gaziantep_vs_Kasimpasa+SK&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.3918984749925523, 1.4142316989065902], "h2h": [], "margin_distribution": {"-1": 0.2022039653760121, "-10": 6.366549210268008e-07, "-11": 8.066312623943879e-08, "-12": 9.385419726573456e-09, "-13": 1.0021561538540512e-09, "-14": 8.875498223572365e-11, "-2": 0.11124796764106362, "-3": 0.045597666307939086, "-4": 0.014754957866606867, "-5": 0.003926891020161624, "-6": 0.0008854625910730416, "-7": 0.00017297110151691196, "-8": 2.9780587143353162e-05, "-9": 4.581165563197571e-06, "0": 0.25246912663439924, "1": 0.19901080654741266, "10": 5.429677267710962e-07, "11": 6.770674843812721e-08, "12": 7.753496567762195e-09, "13": 8.148286462324105e-10, "14": 7.102489888214793e-11, "2": 0.10776210568292117, "3": 0.04347139639287619, "4": 0.013844776212097109, "5": 0.0036264676436101547, "6": 0.0008048077829534395, "7": 0.00015473283846854151, "8": 2.6219788783318387e-05, "9": 3.9697111947691085e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:18.282417+00:00", "p_over_1_5": 0.7699634807368022, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Eyüpspor vs Kocaelispor

The model's most likely 1X2 outcome is **Kocaelispor win** at **44.5%**. Expected goals are 0.80 for Eyüpspor and 0.87 for Kocaelispor (1.67 combined). The most likely exact score is 1-1 at 14.6%. Goal-market probabilities: at least one goal: 89.1%; Over 2.5 goals: 41.8%; Under 3.5 goals: 78.7%; Double Chance 1X: 55.5%; Double Chance X2: 75.3%; Double Chance 12 (either team wins): 69.2%; Under 4.5 goals: 90.9%; BTTS Yes (both teams score): 49.1%; BTTS No (at least one team does not score): 50.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eyüpspor win | 24.7% | 4.05 |
| Draw | 30.8% | 3.25 |
| Kocaelispor win | 44.5% | 2.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eyüpspor expected goals | 0.80 |
| Kocaelispor expected goals | 0.87 |
| Expected total goals | 1.67 |
| Over 0.5 | 89.1% |
| Under 0.5 | 10.9% |
| Over 1.5 | 69.6% |
| Under 1.5 | 30.4% |
| Over 2.5 | 41.8% |
| Under 2.5 | 58.2% |
| Over 3.5 | 21.3% |
| Under 3.5 | 78.7% |
| Over 4.5 | 9.1% |
| Under 4.5 | 90.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.55% |
| 2 | 0-1 | 12.41% |
| 3 | 0-0 | 10.85% |
| 4 | 1-2 | 9.65% |
| 5 | 0-2 | 8.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eyüpspor win | 24.7% | 22.6% | 4.20 | +3.7% |
| Draw | 30.8% | 28.1% | 3.50 | +7.7% |
| Kocaelispor win | 44.5% | 49.3% | 2.00 | -10.9% |
| Over 2.5 | 41.8% | 42.8% | 2.20 | -7.9% |
| Under 2.5 | 58.2% | 57.2% | 1.73 | +0.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T10:30:00+00:00 |
| Fixture id | a3dad1ddaa98a6ff741be7f63250f2ee |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:39:23Z |
| Market best draw last update utc | 2026-11-06T13:38:36Z |
| Market best away last update utc | 2026-11-06T13:38:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Eyupspor |
| Matched away-team name | Kocaelispor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7986 |
| Dc lambda away | 0.8690 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 49.1% |
| P btts no | 50.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.22 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.28 |
| Fair Over 2.5 odds | 2.39 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.69 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.04 |
| Fair Under 4.5 odds | 1.10 |
| Score matrix json | [[0.10851263756566838,0.1240649192757523,0.08551019901003644,0.03501261811174073,0.010752080815190633,0.002641498935896465,0.0005407880846719652,9.489798664222271e-05,1.4571187140585588e-05,1.9887507248429747e-06,2.442914545440427e-07,2.727994652291814e-08,2.7924807823319884e-09,2.638607333432448e-10,2.3151261148258295e-11],[0.071901319245841,0.1455159575484009,0.09652658672389765,0.03952333824175731,0.012137285064066326,0.00298180660399313,0.000610458501543332,0.00010712381497870973,1.6448411715552123e-05,2.2449640105648488e-06,2.7576383339003756e-07,3.079445673560742e-08,3.152239633765195e-09,2.978542472705338e-10,2.6133867572132138e-11],[0.04603751666933796,0.05655093808519513,0.04600574860991121,0.022307590092049422,0.0068504734692042815,0.0016829782709338057,0.000344552323423121,6.04623561659793e-05,9.283740760241152e-06,1.2670927899044104e-06,1.5564541941899626e-07,1.7380872884859266e-08,1.7791733378344157e-09,1.6811359441968965e-10,1.4750363487846556e-11],[0.017322862835009712,0.021278822458584395,0.013069095147161964,0.007088046355582917,0.002577676226852951,0.0006332661674843415,0.00012964714584872198,2.2750599474500826e-05,3.49325896399961e-06,4.7677798862167704e-07,5.856580559847129e-08,6.540024282797319e-09,6.694621673965976e-10,6.325729421396736e-11,5.550223859852165e-12],[0.004888647322506785,0.006005050056046207,0.003688200824960462,0.0015101539757683313,0.0006142759653853055,0.0001787126633508741,3.658743814233093e-05,6.420397036318181e-06,9.858249900048893e-07,1.345504758483083e-07,1.652772820845689e-08,1.8456459826380965e-09,1.8892745750711997e-10,1.7851702973896005e-11,1.5663165650046752e-12],[0.0011036915951584104,0.001355737658728304,0.0008326712857817382,0.0003409418066991786,0.00010470036394328966,3.4070654076044246e-05,8.260208868035573e-06,1.4495089907468997e-06,2.2256601550213586e-07,3.03769569620322e-08,3.731403291612907e-09,4.166845804763461e-10,4.265344443753677e-11,4.0303121153461104e-12,3.536214241093176e-13],[0.00020764693122355093,0.00025506651098373994,0.00015665756445823998,6.414429555997156e-05,1.9698174169472254e-05,4.839315012797517e-06,1.3123054333040745e-06,2.727085129848619e-07,4.187324639999512e-08,5.715076494870417e-09,7.02020787382792e-10,7.839443083886812e-11,8.02475699046847e-12,7.582570586709978e-13,6.652982033505711e-14],[3.348547850222569e-05,4.1132436293934634e-05,2.5262851109655433e-05,1.0344012393332335e-05,3.1765592864689993e-06,7.803957316955053e-07,1.597686477532357e-07,3.713605818127305e-08,6.752547142803173e-09,9.216224385301853e-10,1.1320900263492964e-10,1.2642012155349423e-11,1.2940852345206262e-12,1.2227775429993362e-13,1.0728705959964703e-14],[4.724931911714016e-06,5.803947548153978e-06,3.5646870442946463e-06,1.459580583540792e-06,4.482249325208619e-07,1.1011688831648069e-07,2.2543980735126214e-08,3.956038313903037e-09,8.045865830130565e-10,1.3004452870737754e-10,1.5974232806843167e-11,1.783837332864057e-12,1.8260048518219656e-13,1.7253869116610668e-14,1.5138623495633847e-15],[5.926278778187274e-07,7.27964165982226e-07,4.4710335675120993e-07,1.830689118682805e-07,5.621892452814639e-08,1.381148745724987e-08,2.8275944945411034e-09,4.96188862473461e-10,7.618771512438216e-11,1.3773513020520425e-11,2.0035792821970196e-12,2.2373904062578385e-13,2.2902793107750705e-14,2.1640785581246174e-15,1.8987724020047696e-16],[6.689768811853032e-08,8.217487155108328e-08,5.0470425095053244e-08,2.0665391266168238e-08,6.346168008980364e-09,1.5590838955617175e-09,3.1918770901854896e-10,5.601135048154325e-11,8.60030753803545e-12,1.173814301135462e-12,1.9098606488685008e-13,2.5256362584247448e-14,2.585338907789592e-15,2.4428795516383413e-16,2.1433936659362087e-17],[6.86510930706603e-09,8.43286952596548e-09,5.1793267420201675e-09,2.120703628265373e-09,6.512502642163492e-10,1.599947870089812e-10,3.275536978201429e-11,5.747942183156979e-12,8.825723725816312e-13,1.2045802643006643e-13,1.479665908880014e-14,2.1886346310241933e-15,2.6531012800231536e-16,2.5069080289111342e-17,2.199572544069601e-18],[6.45795839335851e-10,7.932739028532728e-10,4.872154995572834e-10,1.9949304786576335e-10,6.126263868288422e-11,1.505059324539491e-11,3.0812738115268915e-12,5.407047405356197e-13,8.302294116997456e-14,1.1331398933892699e-14,1.3919109584727004e-15,1.5543423973904601e-16,2.107500718506883e-17,2.3582301493759426e-18,2.0691218941196944e-19],[5.607650298602467e-11,6.88824914509131e-11,4.230646862615175e-11,1.7322614691727407e-11,5.319629411929218e-12,1.3068907937449716e-12,2.6755678740597807e-13,4.695110923660628e-14,7.209145560947833e-15,9.839413440720749e-16,1.2086404752831268e-16,1.3496848505281497e-17,1.381589587845465e-18,1.7291711593301382e-19,1.7966842306289666e-20],[4.5214935856599505e-12,5.554050746302771e-12,3.4112046283046884e-12,1.396736369866433e-12,4.2892600257402555e-13,1.0537565694045845e-13,2.1573319191416176e-14,3.785705740349775e-15,5.81279211009968e-16,7.933598279115699e-17,9.745365465681051e-18,1.0882617619444494e-18,1.1139868085238262e-19,1.0526030406065385e-20,1.223316598952608e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.245664024783905, "-10": 2.769299082282635e-07, "-11": 3.060584997496287e-08, "-12": 3.1050853930903687e-09, "-13": 2.899946009153769e-10, "-14": 2.3151261148258295e-11, "-2": 0.13255535664668489, "-3": 0.04896917738573389, "-4": 0.014102207258875937, "-5": 0.0033160514141548753, "-6": 0.0006576893709608753, "-7": 0.00011267394602169057, "-8": 1.6978529619151675e-05, "-9": 2.282583098609666e-06, "0": 0.3077720869590695, "1": 0.14314120993498508, "10": 7.583552468474739e-08, "11": 7.702086414915322e-09, "12": 7.180895354150687e-10, "13": 6.163055373232745e-11, "14": 4.5214935856599505e-12, "2": 0.07136598337837492, "3": 0.024228018033072285, "4": 0.006411848919526306, "5": 0.0013855383491471333, "6": 0.00025253363276525067, "7": 3.975786137059701e-05, "8": 5.505549797522357e-06, "9": 6.801869941647655e-07} |
| Raw goal margin distribution | {"-1": 0.21522445948858873, "-10": 1.3597562515416243e-08, "-11": 1.067045536086396e-09, "-12": 7.30463366397519e-11, "-2": 0.08922880123358581, "-3": 0.024477116270834525, "-4": 0.00514308001319855, "-5": 0.0008739601843939758, "-6": 0.00012454351400123737, "-7": 1.5273441371516532e-05, "-8": 1.6433300963614388e-06, "-9": 1.5746321943427886e-07, "0": 0.3694744700428171, "1": 0.1967610917836988, "10": 5.840797397185208e-09, "11": 4.212065720196641e-10, "12": 2.6497916895482713e-11, "2": 0.07535416710846643, "3": 0.018996061815039426, "4": 0.0036679863597313457, "5": 0.0005727923202292138, "6": 7.501148475258614e-05, "7": 8.4536576589799e-06, "8": 8.358602476404758e-07, "9": 7.360191202722852e-08} |
| Research history json | {"away": [{"away": "Rizespor", "away_goals": 0.0, "away_xg": 1.17, "date": "2026-10-31T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 0.0, "home_xg": 0.62, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.83, "date": "2026-10-18T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.61, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 1.0, "away_xg": 1.65, "date": "2026-10-11T00:00:00+00:00", "home": "Besiktas", "home_goals": 2.0, "home_xg": 2.21, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.88, "date": "2026-09-19T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.16, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 0.77, "date": "2026-08-29T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 0.0, "away_xg": 0.59, "date": "2026-08-24T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.3, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.44, "date": "2026-08-16T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.96, "source": "pipeline training history"}], "h2h": [{"away": "Kocaelispor", "away_goals": 1.0, "away_xg": null, "date": "2026-03-09T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Eyupspor", "away_goals": 1.0, "away_xg": 0.98, "date": "2026-11-01T00:00:00+00:00", "home": "Amedspor", "home_goals": 5.0, "home_xg": 4.95, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.59, "date": "2026-10-24T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-10-17T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 4.0, "away_xg": 3.21, "date": "2026-10-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Rizespor", "away_goals": 2.0, "away_xg": 2.05, "date": "2026-09-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-06T00:00:00+00:00", "home": "Corum", "home_goals": 3.0, "home_xg": 2.58, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 1.0, "away_xg": 1.16, "date": "2026-08-23T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.09, "date": "2026-08-16T00:00:00+00:00", "home": "Besiktas", "home_goals": 1.0, "home_xg": 1.29, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 36.9% |
| Unadjusted away-win probability | 33.5% |
| Raw p over 1 5 | 50.9% |
| Raw p under 3 5 | 91.2% |
| Raw p btts yes | 33.2% |
| P home draw | 55.5% |
| P draw away | 75.3% |
| P home away | 69.2% |
| Raw p home draw | 66.5% |
| Raw p draw away | 70.5% |
| Raw p home away | 63.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.4136 |
| Totals anchor target over 2 5 | 0.4185 |
| Totals anchor reference over odds | 2.28 |
| Totals anchor reference under odds | 1.67 |
| Totals anchor reference last update utc | 2026-11-06T13:39:23Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.2512 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.14, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.01, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.14, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.0, "draw": 3.5, "home": 4.07}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.2, "under": 1.73}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.26, "home_away": 1.33, "home_draw": 1.86}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.98, "draw": 3.4, "home": 4.2}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.28, "under": 1.67}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.4, "under": 3.02}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.20 |
| Reference draw odds | 3.40 |
| Reference away odds | 1.98 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:23Z |
| Market reference home last update utc | 2026-11-06T13:39:23Z |
| Market reference draw last update utc | 2026-11-06T13:39:23Z |
| Market reference away last update utc | 2026-11-06T13:39:23Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.26 |
| Reference Under 2.5 odds | 1.71 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:22Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:22Z |
| Market best over 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market best under 2 5 last update utc | 2026-11-06T13:38:36Z |
| Home probability edge | +2.1% |
| Draw probability edge | +2.6% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | 0.0694 |
| Raw ev home | 0.2408 |
| Raw edge prob draw | 0.0881 |
| Raw ev draw | 0.2932 |
| Raw edge prob away | -0.1576 |
| Raw ev away | -0.3298 |
| Market p home draw | 51.6% |
| Market home draw odds | 1.86 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T13:38:36Z |
| Market reference home draw last update utc | 2026-11-06T13:39:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 76.0% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T13:38:36Z |
| Market reference draw away last update utc | 2026-11-06T13:39:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.4% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T13:38:36Z |
| Market reference home away last update utc | 2026-11-06T13:39:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.23 |
| Market reference dc home draw odds | 1.81 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 69.6% |
| Market over 1 5 odds | 1.40 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference over 1 5 odds | 1.39 |
| Market reference over 1 5 opposite odds | 2.94 |
| Market reference over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 79.1% |
| Market under 3 5 odds | 1.24 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference under 3 5 odds | 1.23 |
| Market reference under 3 5 opposite odds | 4.00 |
| Market reference under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,370.1212 |
| Elo away rating | 1,438.4311 |
| Elo rating diff | -8.3099 |
| Elo home expectancy | 0.4880 |
| Research p home | 0.3261 |
| Research p draw | 0.3098 |
| Research p away | 0.3642 |
| Research p over 1 5 | 0.5895 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.7985704264449229, 0.8689846701952366], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:18.290320+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T13:40:18.194352+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:18.291841+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Ey%C3%BCpspor%22+%22Kocaelispor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:18.378480+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Ey%C3%BCpspor_vs_Kocaelispor&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 0.890448735118826, "goals_for": 1.0632630221502812, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.513167850691485, "results": "DWLLWLWWWL", "xg_against": 1.2372826932614873, "xg_for": 1.1882938425185394, "xg_matches": 10}, "venue": {"goals_against": 1.3740829150788851, "goals_for": 1.0848014184490722, "last_match": "2026-10-23T00:00:00+00:00", "matches": 5, "points_per_game": 1.2891252875508328, "results": "WLLWL", "xg_against": 1.5093258702129508, "xg_for": 1.1284305210338508, "xg_matches": 5}}, "home": {"all": {"goals_against": 3.0933035323073734, "goals_for": 0.3034050194301704, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.19620865573750387, "results": "LLLLLLLWLL", "xg_against": 2.5307266426055373, "xg_for": 0.8256655613941696, "xg_matches": 10}, "venue": {"goals_against": 1.8723623359830541, "goals_for": 0.3416191115517185, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.5124286673275777, "results": "LLLWL", "xg_against": 1.563686916043823, "xg_for": 1.0291416727227958, "xg_matches": 5}}}, "goal_rates": [0.9554582081192398, 1.0280093529764367], "h2h": [{"away": "Kocaelispor", "away_goals": 1.0, "away_xg": null, "date": "2026-03-09T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.2232599768904729, "-10": 5.463039283633365e-08, "-11": 5.067692393489208e-09, "-12": 4.303795117814401e-10, "-13": 3.164262643937708e-11, "-2": 0.09962904066412444, "-3": 0.03166571054951318, "-4": 0.007768475815243394, "-5": 0.0015476797833799633, "-6": 0.0002592126766372117, "-7": 3.741998613805948e-05, "-8": 4.744480693640874e-06, "-9": 5.361303616648103e-07, "0": 0.309774770665297, "1": 0.2075035376350351, "10": 2.6277292840534605e-08, "11": 2.265537070370685e-09, "12": 1.7882455195169911e-10, "13": 1.2219760974240308e-11, "2": 0.08606274778455834, "3": 0.02542337051933052, "4": 0.005796880357952543, "5": 0.0010733818770675592, "6": 0.00016708752080493505, "7": 2.241847313347564e-05, "8": 2.641835195726799e-06, "9": 2.774610786375542e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:18.378935+00:00", "p_over_1_5": 0.5895008110833633, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Galatasaray vs Amed SK

The model's most likely 1X2 outcome is **Galatasaray win** at **64.3%**. Expected goals are 2.21 for Galatasaray and 1.53 for Amed SK (3.74 combined). The most likely exact score is 2-1 at 11.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 67.5%; Under 3.5 goals: 55.4%; Double Chance 1X: 83.1%; Double Chance X2: 35.7%; Double Chance 12 (either team wins): 81.2%; Under 4.5 goals: 73.7%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 64.3% | 1.56 |
| Draw | 18.8% | 5.32 |
| Amed SK win | 16.9% | 5.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 2.21 |
| Amed SK expected goals | 1.53 |
| Expected total goals | 3.74 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 86.5% |
| Under 1.5 | 13.5% |
| Over 2.5 | 67.5% |
| Under 2.5 | 32.5% |
| Over 3.5 | 44.6% |
| Under 3.5 | 55.4% |
| Over 4.5 | 26.3% |
| Under 4.5 | 73.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.86% |
| 2 | 2-0 | 8.62% |
| 3 | 1-1 | 8.26% |
| 4 | 3-1 | 7.89% |
| 5 | 1-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 64.3% | 69.3% | 1.45 | -6.8% |
| Draw | 18.8% | 17.5% | 5.15 | -3.3% |
| Amed SK win | 16.9% | 13.2% | 6.73 | +14.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | e300554369b00b495db88afb743c95ab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:38:36Z |
| Market best draw last update utc | 2026-11-06T13:38:36Z |
| Market best away last update utc | 2026-11-06T13:38:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Galatasaray |
| Matched away-team name | Amedspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2144 |
| Dc lambda away | 1.5274 |
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
| P btts yes | 64.0% |
| P btts no | 36.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.81 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.41 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.24 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.80 |
| Fair Under 4.5 odds | 1.36 |
| Score matrix json | [[0.03470836856588095,0.025340519367130873,0.02159263509887442,0.009905265530070114,0.0034079080009892914,0.0009379929822537222,0.000215144411787188,4.22974086760443e-05,7.2762147067442e-06,1.1126145310515272e-06,1.5311807445753947e-07,1.9156470940754434e-08,2.1969288419218532e-09,2.3257036232235915e-10,2.286167597700596e-11,2.0974834241187518e-12,1.8040986688587285e-13,1.4604715321570842e-14],[0.07492430033688895,0.08261111044686283,0.043080279788520796,0.01976236844002682,0.006799245645743829,0.0018714251377899588,0.0004292427215246154,8.438915360489662e-05,1.4517050092891628e-05,2.2198191686651635e-06,3.054916390753167e-07,3.821979689414511e-08,4.383175501835716e-09,4.6400989196020667e-10,4.561219105560958e-11,4.184768202169578e-12,3.5994252236765393e-13,2.913841777087068e-14],[0.0861836925078222,0.11860604619253619,0.05171750734610207,0.01971432291106909,0.006782715574737679,0.0018668753991833353,0.00042819916271892404,8.418398985969336e-05,1.4481756785172187e-05,2.2144224275573003e-06,3.0474893925995403e-07,3.812687835738121e-08,4.372519289947989e-09,4.628818085137056e-10,4.550130040741433e-11,4.174594350667473e-12,3.5906744360702785e-13,2.906757754243139e-14],[0.057316110631295214,0.07887846374759255,0.05427629312815842,0.015777917336063364,0.004510817127346796,0.001241557814487048,0.00028477209398284134,5.598621660059511e-05,9.631032854145853e-06,1.4726925378693409e-06,2.0267203004568468e-07,2.535612381378596e-08,2.9079259900286238e-09,3.0783764508091367e-10,3.0260452901602643e-11,2.7762968223010425e-12,2.387963282033762e-13,1.9331273025399058e-14],[0.028588382926393294,0.0393433486924451,0.02707216931997707,0.012418911557643512,0.0027075986862861896,0.0006192696928467355,0.00014203988337420717,2.7925052505287926e-05,4.803809124142837e-06,7.345560915025276e-07,1.0108965070375692e-07,1.2647239478279512e-08,1.4504281747121583e-09,1.535446208718688e-10,1.5093442411717886e-11,1.384773596796261e-12,1.191078877631886e-13,9.642137779722495e-15],[0.011407551968815472,0.015699079447475332,0.010802540990910525,0.004955487666255856,0.0017049362296618353,0.000297371187431827,5.6677824534798795e-05,1.1142864865989876e-05,1.916852113427419e-06,2.931081065130468e-07,4.033755413454567e-08,5.046596793599399e-09,5.787607792530199e-10,6.126853157933719e-11,6.022699120244272e-12,5.525627948656346e-13,4.752732685345457e-14,3.8474784703935014e-15],[0.0037932727854375335,0.0052203041447737965,0.0035920927528020055,0.00164781335683291,0.0005669304175481448,0.0001560419920173788,2.2680414496910166e-05,3.705258250281407e-06,6.373973114871257e-07,9.746517102586705e-08,1.3413162328602006e-08,1.6781092322496502e-09,1.924512392510331e-10,2.0373192607752154e-11,2.0026856533421002e-12,1.8373980830759774e-13,1.5803926732978443e-14,1.279374875012378e-15],[0.0010811573494026935,0.0014878893534646049,0.0010238170833211213,0.0004696592156575768,0.0001615863193085427,4.447503673679672e-05,1.0201095103037202e-05,1.2708945234261045e-06,1.8167077001406236e-07,2.7779490673579956e-08,3.823015071832411e-09,4.782941360063435e-10,5.4852388290316645e-11,5.806760590281991e-12,5.708047997408656e-13,5.236945913624507e-14,4.504429948296088e-15,3.646470019427405e-16],[0.00026963222005099046,0.0003710680131680514,0.00025533200440668074,0.00011712934944679557,4.0298369177346e-05,1.1091727673883009e-05,2.5440736458044707e-06,5.001650835578606e-07,5.4523551314526486e-08,6.927988554433154e-09,9.534301752432798e-10,1.1928283131036306e-10,1.3679758305290193e-11,1.448160852929806e-12,1.4235427012998592e-13,1.306053511783139e-14,1.1233697367864524e-15,9.094012145695356e-17],[5.977260006894256e-05,8.225908589587929e-05,5.660250018086051e-05,2.59654642145317e-05,8.93342162080105e-06,2.4588359736802026e-06,5.639752420829005e-07,1.1087757799234654e-07,1.9073723163873473e-08,1.8482202205663927e-09,2.1135827367998203e-10,2.644285230324899e-11,3.0325556866581996e-12,3.2103114190619553e-13,3.1557374170552535e-14,2.895285074376064e-15,2.4903080942548964e-16,2.015978472097879e-17],[1.1925456633088897e-05,1.6411820138280252e-05,1.1292978061062957e-05,5.180467590355193e-06,1.7823406042414501e-06,4.905716287760763e-07,1.1252082532528228e-07,2.212160331664577e-08,3.80547036869665e-09,5.818989406364635e-10,5.074675988811276e-11,5.27571308649531e-12,6.050366102019439e-13,6.405013260687276e-14,6.296130613207601e-15,5.776492331783577e-16,4.9685075012318124e-17,4.0221546016928e-18],[2.1629934382164364e-06,2.9767127884891556e-06,2.0482769084268123e-06,9.396132785171872e-07,3.2327408083848065e-07,8.897799444204248e-08,2.0408594348159847e-08,4.012331291698142e-09,6.902215730657447e-10,1.0554259086477898e-10,1.4524777301984053e-11,1.151536077828059e-12,1.0973921234314591e-13,1.1617166604854285e-14,1.1419679448361925e-15,1.0477179527773894e-16,9.011687731163997e-18,7.295229255049624e-19],[3.5962247494886305e-07,4.949126526667182e-07,3.405495357380501e-07,1.5622148765915686e-07,5.374802483627332e-08,1.4793612413183673e-08,3.393162956501868e-09,6.67096110390914e-10,1.1475725537737994e-10,1.7547666612712642e-11,2.414910868027285e-12,3.021274270315177e-13,2.1956830938163956e-14,1.9314872308516616e-15,1.8986527253309427e-16,1.7419513003093016e-17,1.4982964756563516e-18,1.2129155612157606e-19],[5.519202681161819e-08,7.595529839806236e-08,5.226486222756587e-08,2.3975644282691464e-08,8.248823792942687e-09,2.2704071903882607e-09,5.207559424590206e-10,1.0238066020722695e-10,1.7612040283401906e-11,2.6930777513499103e-12,3.7062151189183177e-13,4.636813940958464e-14,5.317654965270863e-15,3.567282918911005e-16,2.9139027569764134e-17,2.673409744062162e-18,2.2994674976289277e-19,1.8614873329140028e-20],[7.86540657514677e-09,1.0824376960760477e-08,7.44825683638966e-09,3.4167650850750223e-09,1.1755385088445582e-09,3.2355535165418497e-10,7.421284287754612e-11,1.459025088370695e-11,2.5098889359442543e-12,3.8379006310364587e-13,5.2817210110341704e-14,6.607915846871871e-15,7.578181259942212e-16,8.022382553945118e-17,4.997307617298046e-18,3.809871786513481e-19,3.2769673121298776e-20,2.6528025067512366e-21],[1.0461712658234327e-09,1.4397414855286711e-09,9.906865218290897e-10,4.5446111652626714e-10,1.5635741116143805e-10,4.3035831469104735e-11,9.870989252975672e-12,1.940637281729372e-12,3.3383826507964486e-13,5.104760094618555e-14,7.0251737186729354e-15,8.789134572929139e-16,1.0079676626513385e-16,1.0670505117815827e-17,1.04891108255816e-18,6.098291316397023e-20,4.358667296139047e-21,3.5284708170546527e-22],[1.3045348168486686e-10,1.7953015500337463e-10,1.2353475023915237e-10,5.6669530963058906e-11,1.9497160110956847e-11,5.366400546213627e-12,1.2308739092647872e-12,2.4198990964427805e-13,4.162833125128614e-14,6.365436991665127e-15,8.760117974761724e-16,1.0959708448243255e-16,1.2568964118425437e-17,1.3305704232467423e-18,1.307951261592468e-19,1.2000021754768552e-20,6.540678502259616e-22,4.399865663925754e-23],[1.5310156243869637e-11,2.106984564986626e-11,1.4498166727950481e-11,6.650795073504637e-12,2.2882069819461146e-12,6.29806347585194e-13,1.4445664173892716e-13,2.8400187394335958e-14,4.885544236897783e-15,7.470543035280741e-16,1.0280965534696892e-16,1.286242778366008e-17,1.4751066969721794e-18,1.5615712827496365e-19,1.535025199459285e-20,1.4083350296403299e-21,1.2113446633547212e-22,6.214118929288055e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.09332578078520364, "-10": 1.960338904604938e-07, "-11": 2.4034222284303985e-08, "-12": 2.7093392864780093e-09, "-13": 2.826055861946193e-10, "-14": 2.7424842895807963e-11, "-15": 2.4864935240288373e-12, "-16": 2.0954828465674352e-13, "-17": 1.4604715321570842e-14, "-2": 0.049533125833658195, "-3": 0.01888610198416553, "-4": 0.005768629340793083, "-5": 0.0014618273545797397, "-6": 0.00031559434936592333, "-7": 5.924480018410744e-05, "-8": 9.827652691388035e-06, "-9": 1.4593007301294241e-06, "0": 0.18784388130133972, "1": 0.26209725036754733, "10": 1.5267914435213204e-05, "11": 2.7137495864641453e-06, "12": 4.435006182662999e-07, "13": 6.706604803215276e-08, "14": 9.435333605988098e-09, "15": 1.2401995875547577e-09, "16": 1.5152332733473313e-10, "17": 1.5310156243869637e-11, "2": 0.19770387756063143, "3": 0.10928307852345816, "4": 0.04839208819813989, "5": 0.017778247633300187, "6": 0.005564334424227478, "7": 0.001514346933721712, "8": 0.0003641799919143321, "9": 7.839750110031807e-05} |
| Raw goal margin distribution | {"-1": 0.1358356017604105, "-10": 6.118787466620546e-07, "-11": 8.288388072767743e-08, "-12": 1.0329944043222214e-08, "-13": 1.1918991731757027e-09, "-14": 1.279972157410989e-10, "-15": 1.284119327296846e-11, "-16": 1.192584013348655e-12, "-17": 8.937072942947552e-14, "-2": 0.07546366877424214, "-3": 0.030874661584716287, "-4": 0.01022452386636626, "-5": 0.0028272330010709356, "-6": 0.0006688118979380208, "-7": 0.00013796533569711495, "-8": 2.51993158900635e-05, "-9": 4.12611796460791e-06, "0": 0.21887245714678477, "1": 0.20040622995895882, "10": 2.509439627100698e-05, "11": 4.928021554891183e-06, "12": 8.904132806742262e-07, "13": 1.4894444716615326e-07, "14": 2.3188703065366765e-08, "15": 3.372659189845578e-09, "16": 4.5409549839895494e-10, "17": 4.933380969904136e-11, "2": 0.15860621160457156, "3": 0.09407530196744426, "4": 0.04516558568656353, "5": 0.018105782257459777, "6": 0.006209416915773967, "7": 0.0018569830956802484, "8": 0.00049171998238005, "9": 0.00011672446315077387} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Galatasaray", "away_goals": 4.0, "away_xg": 2.8, "date": "2026-10-30T00:00:00+00:00", "home": "Konyaspor", "home_goals": 0.0, "home_xg": 1.38, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 1.0, "away_xg": 1.92, "date": "2026-10-17T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 0.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.51, "date": "2026-10-09T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 3.0, "away_xg": 2.12, "date": "2026-09-04T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.63, "date": "2026-08-29T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.92, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 4.0, "away_xg": 3.08, "date": "2026-08-21T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 0.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 2.0, "away_xg": 0.61, "date": "2026-08-14T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 52.5% |
| Unadjusted draw probability | 21.9% |
| Unadjusted away-win probability | 25.6% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.5% |
| Raw p btts yes | 70.5% |
| P home draw | 83.1% |
| P draw away | 35.7% |
| P home away | 81.2% |
| Raw p home draw | 74.4% |
| Raw p draw away | 47.5% |
| Raw p home away | 78.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9010 |
| Totals anchor target over 2 5 | 0.6746 |
| Totals anchor reference over odds | 1.44 |
| Totals anchor reference under odds | 2.83 |
| Totals anchor reference last update utc | 2026-11-06T13:39:23Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7344 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.78, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.73, "draw": 5.15, "home": 1.45}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.87, "home_away": 1.19, "home_draw": 1.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.67, "draw": 5.14, "home": 1.41}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.44, "under": 2.83}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.14, "under": 5.96}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.41 |
| Reference draw odds | 5.14 |
| Reference away odds | 6.67 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:23Z |
| Market reference home last update utc | 2026-11-06T13:39:23Z |
| Market reference draw last update utc | 2026-11-06T13:39:23Z |
| Market reference away last update utc | 2026-11-06T13:39:23Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:23Z |
| Home probability edge | -5.0% |
| Draw probability edge | +1.3% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.1682 |
| Raw ev home | -0.2387 |
| Raw edge prob draw | 0.0443 |
| Raw ev draw | 0.1272 |
| Raw edge prob away | 0.1239 |
| Raw ev away | 0.7233 |
| Market p home draw | 85.5% |
| Market home draw odds | 1.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T13:38:36Z |
| Market reference home draw last update utc | 2026-11-06T13:39:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.5% |
| Market draw away odds | 2.87 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T13:38:36Z |
| Market reference draw away last update utc | 2026-11-06T13:39:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.0% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T13:38:36Z |
| Market reference home away last update utc | 2026-11-06T13:39:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.78 |
| Market reference dc home draw odds | 1.09 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 86.0% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.6% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference under 3 5 odds | 1.71 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market reference under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,693.8730 |
| Elo away rating | 1,457.7667 |
| Elo rating diff | 296.1063 |
| Elo home expectancy | 0.8461 |
| Research p home | 0.5328 |
| Research p draw | 0.2034 |
| Research p away | 0.2638 |
| Research p over 1 5 | 0.8876 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.2143698413457575, 1.5274219226046075], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:18.290320+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T13:40:18.194352+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:18.502775+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Galatasaray%22+%22Amed+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:18.588785+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Galatasaray_vs_Amed+SK&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 1.0408527377748258, "goals_for": 2.2981057758943, "last_match": "2026-10-30T00:00:00+00:00", "matches": 10, "points_per_game": 2.6034710533412406, "results": "WWWWLWWWWD", "xg_against": 1.1147534090307207, "xg_for": 2.2984475091718832, "xg_matches": 10}, "venue": {"goals_against": 1.1232992550353904, "goals_for": 2.1999854601202053, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 2.70260329000593, "results": "WWWWD", "xg_against": 0.5544118907898825, "xg_for": 2.502044081155706, "xg_matches": 5}}}, "goal_rates": [2.2143698413457575, 1.5274219226046075], "h2h": [], "margin_distribution": {"-1": 0.14357215500055634, "-10": 6.118787466620546e-07, "-11": 8.288388072767743e-08, "-12": 1.0329944043222214e-08, "-13": 1.1918991731757027e-09, "-14": 1.279972157410989e-10, "-15": 1.284119327296846e-11, "-16": 1.192584013348655e-12, "-17": 8.937072942947552e-14, "-2": 0.07546366877424214, "-3": 0.030874661584716287, "-4": 0.01022452386636626, "-5": 0.0028272330010709356, "-6": 0.0006688118979380208, "-7": 0.00013796533569711495, "-8": 2.51993158900635e-05, "-9": 4.12611796460791e-06, "0": 0.20339935066649312, "1": 0.20814278319910465, "10": 2.509439627100698e-05, "11": 4.928021554891183e-06, "12": 8.904132806742262e-07, "13": 1.4894444716615326e-07, "14": 2.3188703065366765e-08, "15": 3.372659189845578e-09, "16": 4.5409549839895494e-10, "17": 4.933380969904136e-11, "2": 0.15860621160457156, "3": 0.09407530196744426, "4": 0.04516558568656353, "5": 0.018105782257459777, "6": 0.006209416915773967, "7": 0.0018569830956802484, "8": 0.00049171998238005, "9": 0.00011672446315077387}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:18.589255+00:00", "p_over_1_5": 0.8875646276454282, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Goztepe vs Basaksehir

The model's most likely 1X2 outcome is **Goztepe win** at **44.9%**. Expected goals are 1.52 for Goztepe and 1.35 for Basaksehir (2.87 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 58.9%; Under 3.5 goals: 63.5%; Double Chance 1X: 70.7%; Double Chance X2: 55.1%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 80.6%; BTTS Yes (both teams score): 62.0%; BTTS No (at least one team does not score): 38.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Goztepe win | 44.9% | 2.23 |
| Draw | 25.8% | 3.88 |
| Basaksehir win | 29.3% | 3.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Goztepe expected goals | 1.52 |
| Basaksehir expected goals | 1.35 |
| Expected total goals | 2.87 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 81.9% |
| Under 1.5 | 18.1% |
| Over 2.5 | 58.9% |
| Under 2.5 | 41.1% |
| Over 3.5 | 36.5% |
| Under 3.5 | 63.5% |
| Over 4.5 | 19.4% |
| Under 4.5 | 80.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.89% |
| 2 | 2-1 | 9.74% |
| 3 | 1-0 | 7.24% |
| 4 | 1-2 | 6.99% |
| 5 | 2-0 | 6.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Goztepe win | 44.9% | 46.9% | 2.09 | -6.1% |
| Draw | 25.8% | 25.2% | 3.77 | -2.8% |
| Basaksehir win | 29.3% | 27.9% | 3.48 | +2.0% |
| Over 2.5 | 58.9% | 58.4% | 1.67 | -1.6% |
| Under 2.5 | 41.1% | 41.6% | 2.31 | -5.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | c7ad58db2278db2259846b11c28ae1c2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:38:36Z |
| Market best draw last update utc | 2026-11-06T13:38:36Z |
| Market best away last update utc | 2026-11-06T13:38:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Goztep |
| Matched away-team name | Buyuksehyr |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5169 |
| Dc lambda away | 1.3496 |
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
| P btts yes | 62.0% |
| P btts no | 38.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.47 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.54 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.74 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.15 |
| Fair Under 4.5 odds | 1.24 |
| Score matrix json | [[0.05725451306654298,0.0508968573518384,0.043279758775836875,0.020715208845721242,0.007436268529321597,0.0021355551875732355,0.0005110757657092276,0.00010483661437758323,1.8816928712202503e-05,3.00214710936226e-06,4.310798358058658e-07,5.627179423410861e-08,6.733413047196868e-09,7.437340125791891e-10,7.628081891933969e-11,7.302134482870425e-12],[0.0724308481890121,0.11890227780239092,0.0698502530444126,0.03343277829333289,0.01200157425020841,0.0034466243449947256,0.0008248375815714372,0.00016919835622286443,3.0369097916502943e-05,4.845238078881847e-06,6.95730208879874e-07,9.081841437411293e-08,1.0867218730013722e-08,1.2003303725758385e-09,1.2311146491245347e-10,1.178509205734286e-11],[0.06784691408197238,0.09742173023827723,0.06282660467706963,0.026978986133707843,0.009684815974256243,0.0027812953382416253,0.000665612695437119,0.00013653666669075852,2.45067120774087e-05,3.909923662274112e-06,5.614279343908095e-07,7.328702151484483e-08,8.769434022403012e-09,9.68621159553761e-10,9.934629050664014e-11,9.51012304182116e-12],[0.03649992707102105,0.05241043158622657,0.03762820311544384,0.016177446490020893,0.005210186513855608,0.0014962666818735134,0.0003580828276382282,7.345327999313065e-05,1.3183992458304074e-05,2.1034402294825176e-06,3.020340562009953e-07,3.9426567541632006e-08,4.717734131358088e-09,5.210937322874379e-10,5.3445796427642344e-11,5.116206126096194e-12],[0.014727029529083403,0.02114661687132988,0.015182267551637266,0.0072667651571886906,0.002343143468583253,0.000603715277689689,0.00014447964145859177,2.963700780448176e-05,5.319491347663821e-06,8.486983086836189e-07,1.2186502334116755e-07,1.590787354961619e-08,1.903516402311858e-09,2.1025145523948858e-10,2.1564366982535195e-11,2.0642923080171593e-12],[0.004753662073427861,0.0068258076351400574,0.004900606011981318,0.002345601728849449,0.0008420153737512651,0.00021720397241682676,4.663583994503673e-05,9.56637723118757e-06,1.7170512369367816e-06,2.7394695948727335e-07,3.933618374230044e-08,5.134820637954086e-09,6.14426263622825e-10,6.786598524034995e-11,6.960651043709671e-12,6.663222908401937e-13],[0.0012786750978147918,0.0018360560996364477,0.0013182011625835575,0.0006309372592630148,0.00022649150776015854,6.50440624126596e-05,1.398215636215836e-05,2.573234729956577e-06,4.618651103989686e-07,7.368827438881474e-08,1.0580936931866649e-08,1.3812019407519195e-09,1.6527290972775447e-10,1.8255093436401086e-11,1.8723272745704497e-12,1.792322860261453e-13],[0.000294812110359732,0.00042332221406182595,0.0003039252639580224,0.0001454692792764913,5.2220020156364646e-05,1.4996598697368073e-05,3.588948769336617e-06,6.612824029120674e-07,1.0648790152474915e-07,1.698961348231408e-08,2.4395472718579986e-09,3.184507617939162e-10,3.810542285949031e-11,4.208905475673086e-12,4.3168491827479953e-13,4.13239051720553e-14],[5.947555246276432e-05,8.540124935968915e-05,6.131404493268011e-05,2.934705002712541e-05,1.0534894732196503e-05,3.025421823750716e-06,7.240364398748557e-07,1.4852108852616637e-07,2.3945057463615363e-08,3.4274936899860726e-09,4.921555684253943e-10,6.424442661724633e-11,7.687408341638435e-12,8.491068366348984e-13,8.70883457701534e-14,8.336706680834421e-15],[1.066544861459122e-05,1.531457210486451e-05,1.099513612743065e-05,5.262657362453296e-06,1.8891691421734005e-06,5.425335228096909e-07,1.2983777577201045e-07,2.6633532136598464e-08,4.78040309241128e-09,6.850775821082036e-10,8.825575733343947e-11,1.1520626585000546e-11,1.378543876468498e-12,1.5226601451238878e-13,1.561711053163966e-14,1.4949792484067369e-15],[1.7213226358768498e-06,2.4716559589258135e-06,1.7745317036923436e-06,8.493530436649163e-07,3.048975926783143e-07,8.756080192039098e-08,2.0954833735029934e-08,4.298450388421619e-09,7.715208566403664e-10,1.2309230400992782e-10,1.587627627615856e-11,1.8593418839518834e-12,2.224865418101865e-13,2.45745816164127e-14,2.5204833698532996e-15,2.4127832906420187e-16],[2.525531251641568e-07,3.626423215188489e-07,2.603599802439595e-07,1.2461740819203971e-07,4.4734693125505085e-08,1.2846954839241739e-08,3.074501337967496e-09,6.306703091753396e-10,1.1319783950589509e-10,1.8060150615243436e-11,2.5932662452048115e-12,3.0406901624585597e-13,3.264331175921889e-14,3.605592151912358e-15,3.6980629819956537e-16,3.5400450078034964e-17],[3.3966801492669324e-08,4.8773103638551576e-08,3.50167742324853e-08,1.6760254951660754e-08,6.016533908427605e-09,1.7278343498072973e-09,4.1350102703266565e-10,8.4821176475861e-11,1.5224395031328924e-11,2.4289762816316393e-12,3.487779440910008e-13,4.5528366379268187e-14,4.893488460098565e-15,4.849293898379957e-16,4.9736613290842914e-17,4.761137126179655e-18],[4.216911174540717e-09,6.05508427971437e-09,4.3472632119690465e-09,2.0807524785359294e-09,7.469407761554199e-10,2.145072146116015e-10,5.133533406006548e-11,1.0530381172214381e-11,1.890078509367114e-12,3.015525976715059e-13,4.330009141979698e-14,5.652256571309922e-15,6.763420051087224e-16,6.710281746972027e-17,6.174702095963629e-18,5.910857504566839e-19],[4.86126806055133e-10,6.98031962129908e-10,5.011538286778504e-10,2.398697802052094e-10,8.610756043831633e-11,2.4728457109670603e-11,5.917952964022519e-12,1.2139455525404158e-12,2.1788882689760586e-13,3.4763075411386586e-14,4.991647742282301e-15,6.515938610716161e-16,7.796891258451453e-17,8.611996888718657e-18,7.93402520133461e-19,6.81405455512126e-20],[5.230479000664052e-11,7.510471494753849e-11,5.392162177340619e-11,2.5808777311386488e-11,9.26473876900228e-12,2.6606571376005288e-12,6.367418607589975e-13,1.30614412565269e-13,2.3443737711472746e-14,3.740331404747444e-15,5.37076095568337e-16,7.010820972728194e-17,8.389061349800632e-18,9.26607385545376e-19,9.503716246752087e-20,8.17184177338893e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.15358931740172257, "-10": 5.312110086239425e-07, "-11": 6.816314421241176e-08, "-12": 8.038205916405442e-09, "-13": 8.763556005334638e-10, "-14": 8.806591097668255e-11, "-15": 7.302134482870425e-12, "-2": 0.08804814510261554, "-3": 0.03588759151432051, "-4": 0.011627563195283646, "-5": 0.0031110028829584896, "-6": 0.0007070114436533609, "-7": 0.0001394342110074896, "-8": 2.426499458905552e-05, "-9": 3.7760994652269064e-06, "0": 0.2577358575621099, "1": 0.21565834851207852, "10": 2.121151252324296e-06, "11": 3.0592262653365164e-07, "12": 4.0548848378372925e-08, "13": 4.968864758444031e-09, "14": 5.612315210026714e-10, "15": 5.230479000664052e-11, "2": 0.13802745451505075, "3": 0.06323346690747232, "4": 0.02302760663537357, "5": 0.006924970378241442, "6": 0.001768892182972306, "7": 0.0003921043639907154, "8": 7.669551076920362e-05, "9": 1.3414997114687781e-05} |
| Raw goal margin distribution | {"-1": 0.17605021919266572, "-10": 3.7799537000836626e-07, "-11": 4.567586488163131e-08, "-12": 5.070971016786595e-09, "-13": 5.20438944664304e-10, "-14": 4.931284582698589e-11, "-15": 3.903921448819508e-12, "-2": 0.09757100773115075, "-3": 0.03798130803983243, "-4": 0.011691068965139394, "-5": 0.0029624919075696434, "-6": 0.0006363899470759684, "-7": 0.00011847836717222405, "-8": 1.94458797991389e-05, "-9": 2.8522202756806278e-06, "0": 0.27091772696452515, "1": 0.19926949898494795, "10": 1.2163557418706404e-06, "11": 1.6520314918178562e-07, "12": 2.0614845462990105e-08, "13": 2.3780235743217987e-09, "14": 2.532583932609754e-10, "15": 2.2535243990307044e-11, "2": 0.12326381823088998, "3": 0.05393145735870044, "4": 0.018658807068415207, "5": 0.005314277607231572, "6": 0.0012831215179316326, "7": 0.00026849793552890014, "8": 4.953211817048596e-05, "9": 8.165819562329803e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 58.9% |
| P home draw | 70.7% |
| P draw away | 55.1% |
| P home away | 74.2% |
| Raw p home draw | 67.3% |
| Raw p draw away | 59.8% |
| Raw p home away | 72.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0640 |
| Totals anchor target over 2 5 | 0.5894 |
| Totals anchor reference over odds | 1.64 |
| Totals anchor reference under odds | 2.30 |
| Totals anchor reference last update utc | 2026-11-06T13:39:23Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5515 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.76, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.48, "draw": 3.77, "home": 2.09}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.31}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.79, "home_away": 1.3, "home_draw": 1.33}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.73, "home": 2.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.64, "under": 2.3}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.19, "under": 4.75}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.06 |
| Reference draw odds | 3.73 |
| Reference away odds | 3.39 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:23Z |
| Market reference home last update utc | 2026-11-06T13:39:23Z |
| Market reference draw last update utc | 2026-11-06T13:39:23Z |
| Market reference away last update utc | 2026-11-06T13:39:23Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market best over 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market best under 2 5 last update utc | 2026-11-06T13:38:36Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | -0.0673 |
| Raw ev home | -0.1597 |
| Raw edge prob draw | 0.0188 |
| Raw ev draw | 0.0214 |
| Raw edge prob away | 0.0484 |
| Raw ev away | 0.1381 |
| Market p home draw | 72.1% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T13:38:36Z |
| Market reference home draw last update utc | 2026-11-06T13:39:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.5% |
| Market draw away odds | 1.79 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T13:38:36Z |
| Market reference draw away last update utc | 2026-11-06T13:39:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.4% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T13:38:36Z |
| Market reference home away last update utc | 2026-11-06T13:39:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home draw odds | 1.30 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 82.2% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.2% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.49 |
| Market reference under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,515.0066 |
| Elo away rating | 1,527.1311 |
| Elo rating diff | 47.8755 |
| Elo home expectancy | 0.5685 |
| Research p home | 0.4133 |
| Research p draw | 0.2484 |
| Research p away | 0.3383 |
| Research p over 1 5 | 0.7800 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.516872731961464, 1.3495585512760715], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:18.290320+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T13:40:18.194352+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:18.602978+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Goztepe%22+%22Basaksehir%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:18.689059+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Goztepe_vs_Basaksehir&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.516872731961464, 1.3495585512760715], "h2h": [], "margin_distribution": {"-1": 0.18728703968654076, "-10": 3.7799537000836626e-07, "-11": 4.567586488163131e-08, "-12": 5.070971016786595e-09, "-13": 5.20438944664304e-10, "-14": 4.931284582698589e-11, "-15": 3.903921448819508e-12, "-2": 0.09757100773115075, "-3": 0.03798130803983243, "-4": 0.011691068965139394, "-5": 0.0029624919075696434, "-6": 0.0006363899470759684, "-7": 0.00011847836717222405, "-8": 1.94458797991389e-05, "-9": 2.8522202756806278e-06, "0": 0.2484440859767752, "1": 0.21050631947882292, "10": 1.2163557418706404e-06, "11": 1.6520314918178562e-07, "12": 2.0614845462990105e-08, "13": 2.3780235743217987e-09, "14": 2.532583932609754e-10, "15": 2.2535243990307044e-11, "2": 0.12326381823088998, "3": 0.05393145735870044, "4": 0.018658807068415207, "5": 0.005314277607231572, "6": 0.0012831215179316326, "7": 0.00026849793552890014, "8": 4.953211817048596e-05, "9": 8.165819562329803e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:18.689520+00:00", "p_over_1_5": 0.7799937558781257, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Samsunspor vs Torku Konyaspor

The model's most likely 1X2 outcome is **Samsunspor win** at **41.4%**. Expected goals are 1.41 for Samsunspor and 1.08 for Torku Konyaspor (2.49 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 48.5%; Under 3.5 goals: 73.2%; Double Chance 1X: 70.2%; Double Chance X2: 58.6%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 54.0%; BTTS No (at least one team does not score): 46.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Samsunspor win | 41.4% | 2.41 |
| Draw | 28.7% | 3.48 |
| Torku Konyaspor win | 29.8% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Samsunspor expected goals | 1.41 |
| Torku Konyaspor expected goals | 1.08 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.72% |
| 2 | 1-0 | 9.03% |
| 3 | 0-0 | 8.60% |
| 4 | 2-1 | 8.59% |
| 5 | 0-1 | 7.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Samsunspor win | 41.4% | 40.6% | 2.39 | -0.9% |
| Draw | 28.7% | 28.6% | 3.48 | -0.1% |
| Torku Konyaspor win | 29.8% | 30.8% | 3.18 | -5.1% |
| Over 2.5 | 48.5% | 48.5% | 1.99 | -3.5% |
| Under 2.5 | 51.5% | 51.5% | 1.90 | -2.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T13:00:00+00:00 |
| Fixture id | 605767f0e7114a23442d92831c12c767 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:39:23Z |
| Market best draw last update utc | 2026-11-06T13:38:36Z |
| Market best away last update utc | 2026-11-06T13:38:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Samsunspor |
| Matched away-team name | Konyaspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4120 |
| Dc lambda away | 1.0825 |
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
| P btts yes | 54.0% |
| P btts no | 46.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.62 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.97 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.00 |
| Fair Under 4.5 odds | 1.14 |
| Score matrix json | [[0.0860296886247076,0.07568486057671166,0.05030482011247101,0.019096326979002584,0.0054369000317512906,0.0012383483792568007,0.00023504611994769084,3.8239881968977876e-05,5.443623156429653e-06,6.888220486839587e-07,7.84455905573609e-08,8.121520565633088e-09,7.707572154182844e-10,6.75205145847869e-11,5.492489109757484e-12,4.1700325230876863e-13],[0.09034963920948719,0.1371860578787721,0.07472485589250866,0.028366472206674976,0.008076195689921024,0.0018394937896169064,0.0003491472070055228,5.680309884996527e-05,8.086182496783961e-06,1.0232046990409771e-06,1.1652631769074408e-07,1.2064041826173374e-08,1.1449145772010088e-09,1.0029775895939276e-10,8.158770000572036e-12,6.19433840848885e-13],[0.07538649742362712,0.08585291835164095,0.05291410844144887,0.021068364254990667,0.005998357192608635,0.0013662299958231182,0.0002593188353564119,4.218883365770454e-05,6.005774600145237e-06,7.599552439848589e-07,8.654650068977079e-08,8.960212807902641e-09,8.503516819988426e-10,7.4493215240861e-11,6.059686837064418e-12,4.600662957236288e-13],[0.03732740483335233,0.042509822699788424,0.0242058754691781,0.00994594277506247,0.0029700691093970245,0.0006764848068611212,0.0001284009667390182,2.088967822100374e-05,2.9737418171549774e-06,3.7628962767755845e-07,4.285324797626931e-08,4.436623298653824e-09,4.210491609170411e-10,3.688509875990315e-11,3.000436304387159e-12,2.278004875880387e-13],[0.013861916913614485,0.015786461258363044,0.008989101601706809,0.0034123732686028095,0.0010515815457664013,0.00025121961271876695,4.7683023786687346e-05,7.757597538443442e-06,1.104329705640594e-06,1.3973903563905475e-07,1.591399577810441e-08,1.6475858372022342e-09,1.5636095011791758e-10,1.369766198970771e-11,1.1142429788969606e-12,8.459606141718122e-14],[0.004118212693924251,0.004689972213185217,0.002670556500505753,0.001013776016603147,0.00028863136156596285,7.11573768660946e-05,1.416606628554844e-05,2.3046911084711617e-06,3.280833841660125e-07,4.15148261233831e-08,4.7278612209887905e-09,4.894783998042912e-10,4.645300167520346e-11,4.069414485358445e-12,3.3102850120986175e-13,2.5132496187599086e-14],[0.001019560515937847,0.0011611130470419648,0.000661159140108002,0.00025098412232525924,7.145748939781428e-05,1.627568387587952e-05,3.3437547148547925e-06,5.705805479879488e-07,8.122476649261845e-08,1.0277972675834073e-08,1.1704933630226272e-09,1.2118190266888488e-10,1.150053430331718e-11,1.0074793704507287e-12,8.195389955977509e-14,6.222141177321575e-15],[0.00021635675257023184,0.00024639503423084743,0.00014030186756919727,5.326031050058161e-05,1.5163700546712164e-05,3.453796076053263e-06,6.555516851034157e-07,1.1543973317735265e-07,1.7236374331790617e-08,2.1810463983136386e-09,2.4838559258607364e-10,2.571551420624074e-11,2.440481183600427e-12,2.137930622702823e-13,1.739110066743777e-14,1.3203750421038083e-15],[4.0173156173293166e-05,4.575066908192107e-05,2.6051273049277387e-05,9.889382911140719e-06,2.8155983254110553e-06,6.413014038420415e-07,1.2172294098736852e-07,1.9803223713327933e-08,3.0513520890617413e-09,4.049770415749335e-10,4.612027627340725e-11,4.774860761272063e-12,4.531489337035498e-13,3.96971297513011e-14,3.229182333524114e-15,2.4516744748484925e-16],[6.630540459995e-06,7.551103555592327e-06,4.299737348056396e-06,1.6322330571650088e-06,4.647117725876651e-07,1.0584617466658157e-07,2.0090253343422336e-08,3.2685028655240337e-09,4.6528642269496227e-10,6.372711920060065e-11,7.612106864042447e-12,7.880861372177728e-13,7.479179197083924e-14,6.551972760772419e-15,5.329734119662408e-16,4.0464649404436754e-17],[9.84927844399036e-07,1.121672085815016e-06,6.387007308460657e-07,2.4245863459395786e-07,6.903020458184026e-08,1.572282761582284e-08,2.98428914480712e-09,4.855169048700875e-10,6.911556548037918e-11,8.745705579180886e-12,1.0780558711314132e-12,1.170655672812604e-13,1.1109881447678454e-14,9.732570741048834e-16,7.917007021329671e-17,6.010786021552258e-18],[1.3300476985322338e-07,1.5147072800611061e-07,8.62502204545753e-08,3.27416420161953e-08,9.321846798767966e-09,2.1232124570103864e-09,4.0299875075897706e-10,6.556425890416072e-11,9.333373944364667e-12,1.1810210914209215e-12,1.3449902939985643e-13,1.507206926699678e-14,1.500279673732529e-15,1.31428747684888e-16,1.069113542465443e-17,8.11697238513275e-19],[1.646423119109564e-08,1.87500725524975e-08,1.067663641998836e-08,4.052982192485378e-09,1.1539213292294653e-09,2.628256174467268e-10,4.9885914689680804e-11,8.115988003003132e-12,1.1553482373793531e-12,1.4619478919569677e-13,1.664920075769403e-14,1.7237020639941893e-15,1.7706281798785712e-16,1.626914049344322e-17,1.3234211488886477e-18,1.0047738142627661e-19],[1.881280653523713e-09,2.1424716608848925e-09,1.2199627974426018e-09,4.631128474387911e-10,1.3185248962865768e-10,3.003169377385593e-11,5.700199729932578e-12,9.27371040716313e-13,1.3201553487902996e-13,1.67049056447038e-14,1.9024161479839955e-15,1.9695832181857047e-16,1.8691948933888597e-17,1.772383301867559e-18,1.5122033789314494e-19,1.1481019162085636e-20],[1.996094231322725e-10,2.2732255897356711e-10,1.2944164911505142e-10,4.913763831529031e-11,1.3989937835183586e-11,3.186451239296115e-12,6.04807994862121e-13,9.839680120041435e-14,1.4007237416886245e-14,1.7724397329940103e-15,2.0185196139945247e-16,2.0897858554845215e-17,1.983270883545696e-18,1.737401453262524e-19,1.5297433043355652e-20,1.218169977787205e-21],[1.976720500473883e-11,2.2511620718700563e-11,1.2818531179828885e-11,4.866071725398484e-12,1.3854154019992018e-12,3.155524117868499e-13,5.98937837469841e-14,9.744177958223122e-15,1.3871285695072613e-15,1.755236752396213e-16,1.9989282264232453e-17,2.069502770617809e-18,1.9640216137991979e-19,1.7205385478927762e-20,1.3995804527455753e-21,1.1501461378522227e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17471412374224238, "-10": 9.13980085397681e-08, "-11": 9.34401339044076e-09, "-12": 8.773424617023296e-10, "-13": 7.613935088108257e-11, "-14": 6.111922950606369e-12, "-15": 4.1700325230876863e-13, "-2": 0.08539620548624341, "-3": 0.028675249843617263, "-4": 0.0075577493761460335, "-5": 0.001632802752296663, "-6": 0.0002982476982172538, "-7": 4.7130568021677475e-05, "-8": 6.557971493097932e-06, "-9": 8.147436632561545e-07, "0": 0.28720199895324405, "1": 0.20412638917342807, "10": 1.1475526271628205e-06, "11": 1.5302532825688077e-07, "12": 1.8741010572820985e-08, "13": 2.121421743677109e-09, "14": 2.2212104385097306e-10, "15": 1.976720500473883e-11, "2": 0.12797423408895667, "3": 0.05605123230174869, "4": 0.01926923307293402, "5": 0.005429997837295304, "6": 0.0012937102605196443, "7": 0.0002666592081072031, "8": 4.839688666932293e-05, "9": 7.84265084729173e-06} |
| Raw goal margin distribution | {"-1": 0.16525207184456925, "-10": 5.77122450917586e-08, "-11": 5.615115761410351e-09, "-12": 5.015710600566956e-10, "-13": 4.121585315054311e-11, "-14": 2.8732445652917804e-12, "-2": 0.07822003119841024, "-3": 0.025229606328790954, "-4": 0.006364337180086756, "-5": 0.001313289699481957, "-6": 0.00022883387763491687, "-7": 3.4466842790132894e-05, "-8": 4.5685175759221845e-06, "-9": 5.404499504842709e-07, "0": 0.29026282834388123, "1": 0.2192504183227558, "10": 8.226362833547845e-07, "11": 1.0439809995710264e-07, "12": 1.2163549867322302e-08, "13": 1.3037254777884689e-09, "14": 1.185464196155358e-10, "2": 0.13307790739096184, "3": 0.05598767609778981, "4": 0.018421675881054325, "5": 0.004958273553958086, "6": 0.0011268970828813504, "7": 0.0002213907274054686, "8": 3.827605880467513e-05, "9": 5.90610799066805e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.99, "date": "2026-11-01T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 5.0, "home_xg": 3.89, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 2.0, "away_xg": 1.63, "date": "2026-10-24T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.08, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 1.0, "away_xg": 1.07, "date": "2026-10-18T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 4.0, "home_xg": 2.41, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 0.36, "date": "2026-09-20T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 5.0, "away_xg": 1.73, "date": "2026-09-12T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.32, "date": "2026-08-22T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.85, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 3.0, "away_xg": 1.89, "date": "2026-08-17T00:00:00+00:00", "home": "Samsunspor", "home_goals": 3.0, "home_xg": 2.74, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 51.2% |
| P home draw | 70.2% |
| P draw away | 58.6% |
| P home away | 71.3% |
| Raw p home draw | 72.3% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0520 |
| Totals anchor target over 2 5 | 0.4851 |
| Totals anchor reference over odds | 1.99 |
| Totals anchor reference under odds | 1.88 |
| Totals anchor reference last update utc | 2026-11-06T13:39:23Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4554 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.28, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.8, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.28, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.18, "draw": 3.48, "home": 2.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.98, "under": 1.9}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.65, "home_away": 1.33, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.13, "draw": 3.36, "home": 2.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.99, "under": 1.88}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.99, "under": 1.88}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.3, "under": 3.59}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.39 |
| Reference draw odds | 3.36 |
| Reference away odds | 3.13 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:23Z |
| Market reference home last update utc | 2026-11-06T13:39:23Z |
| Market reference draw last update utc | 2026-11-06T13:39:23Z |
| Market reference away last update utc | 2026-11-06T13:39:23Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:23Z |
| Market best over 2 5 last update utc | 2026-11-06T13:39:23Z |
| Market best under 2 5 last update utc | 2026-11-06T13:38:36Z |
| Home probability edge | +0.8% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0266 |
| Raw ev home | 0.0351 |
| Raw edge prob draw | 0.0044 |
| Raw ev draw | 0.0101 |
| Raw edge prob away | -0.0310 |
| Raw ev away | -0.1203 |
| Market p home draw | 69.7% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T13:38:36Z |
| Market reference home draw last update utc | 2026-11-06T13:39:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.4% |
| Market draw away odds | 1.65 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T13:38:36Z |
| Market reference draw away last update utc | 2026-11-06T13:39:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T13:38:36Z |
| Market reference home away last update utc | 2026-11-06T13:39:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.60 |
| Market reference dc home draw odds | 1.34 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 73.5% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.31 |
| Market reference over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.3% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.51 |
| Market reference under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,436.0175 |
| Elo away rating | 1,425.6973 |
| Elo rating diff | 70.3203 |
| Elo home expectancy | 0.5998 |
| Research p home | 0.4453 |
| Research p draw | 0.2659 |
| Research p away | 0.2888 |
| Research p over 1 5 | 0.7116 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4119922244411376, 1.0825259502082374], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:18.290320+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T13:40:18.194352+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:18.401119+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Samsunspor%22+%22Torku+Konyaspor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:18.488630+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Samsunspor_vs_Torku+Konyaspor&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.913613856180298, "goals_for": 0.9751316584067636, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.22037567410820427, "results": "LLLLLLLLWD", "xg_against": 2.102762810589968, "xg_for": 1.119679917641185, "xg_matches": 10}, "venue": {"goals_against": 2.9627088822913965, "goals_for": 0.9012025941363605, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.148698354997035, "results": "LLLLD", "xg_against": 1.764225747400591, "xg_for": 1.383053774479519, "xg_matches": 5}}}, "goal_rates": [1.4119922244411376, 1.0825259502082374], "h2h": [], "margin_distribution": {"-1": 0.17742213969266818, "-10": 5.77122450917586e-08, "-11": 5.615115761410351e-09, "-12": 5.015710600566956e-10, "-13": 4.121585315054311e-11, "-14": 2.8732445652917804e-12, "-2": 0.07822003119841024, "-3": 0.025229606328790954, "-4": 0.006364337180086756, "-5": 0.001313289699481957, "-6": 0.00022883387763491687, "-7": 3.4466842790132894e-05, "-8": 4.5685175759221845e-06, "-9": 5.404499504842709e-07, "0": 0.2659226926476834, "1": 0.2314204861708547, "10": 8.226362833547845e-07, "11": 1.0439809995710264e-07, "12": 1.2163549867322302e-08, "13": 1.3037254777884689e-09, "14": 1.185464196155358e-10, "2": 0.13307790739096184, "3": 0.05598767609778981, "4": 0.018421675881054325, "5": 0.004958273553958086, "6": 0.0011268970828813504, "7": 0.0002213907274054686, "8": 3.827605880467513e-05, "9": 5.90610799066805e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:18.489074+00:00", "p_over_1_5": 0.7115757145986422, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Alanyaspor vs Trabzonspor

The model's most likely 1X2 outcome is **Trabzonspor win** at **55.6%**. Expected goals are 1.18 for Alanyaspor and 1.61 for Trabzonspor (2.79 combined). The most likely exact score is 1-2 at 11.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.1%; Under 3.5 goals: 68.9%; Double Chance 1X: 44.4%; Double Chance X2: 79.4%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 55.5%; BTTS No (at least one team does not score): 44.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alanyaspor win | 20.6% | 4.84 |
| Draw | 23.7% | 4.22 |
| Trabzonspor win | 55.6% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alanyaspor expected goals | 1.18 |
| Trabzonspor expected goals | 1.61 |
| Expected total goals | 2.79 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 78.3% |
| Under 1.5 | 21.7% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 31.1% |
| Under 3.5 | 68.9% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.30% |
| 2 | 1-1 | 11.27% |
| 3 | 0-1 | 10.58% |
| 4 | 0-2 | 9.60% |
| 5 | 0-0 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alanyaspor win | 20.6% | 18.0% | 5.16 | +6.5% |
| Draw | 23.7% | 22.3% | 4.13 | -2.1% |
| Trabzonspor win | 55.6% | 59.7% | 1.68 | -6.5% |
| Over 2.5 | 54.1% | 56.4% | 1.73 | -6.4% |
| Under 2.5 | 45.9% | 43.6% | 2.21 | +1.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T15:30:00+00:00 |
| Fixture id | a85eafd97e49ac329956fa1022be891d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:38:36Z |
| Market best draw last update utc | 2026-11-06T13:39:23Z |
| Market best away last update utc | 2026-11-06T13:38:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alanyaspor |
| Matched away-team name | Trabzonspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1770 |
| Dc lambda away | 1.6081 |
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
| P btts yes | 55.5% |
| P btts no | 44.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.57 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.60 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.22 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.41 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.06423403631650419,0.10584571252223536,0.09600543242990053,0.051462122260031266,0.020689063841049786,0.006654018043892061,0.0017833880928834736,0.0004096952808525347,8.235388911970775e-05,1.4714812843401568e-05,2.3662895267937885e-06,3.459300863078529e-07,4.635752359116889e-08,5.734426815569736e-09,6.586809719399222e-10,7.061500552706509e-11],[0.04729201458619057,0.11272060815854565,0.11299401084961615,0.06056856840096075,0.024350083583352524,0.007831475448996738,0.0020989663648824032,0.0004821926409579927,9.692676763364259e-05,1.7318662913074395e-05,2.7850147402762697e-06,4.071439181737842e-07,5.4560688817755705e-08,6.749158557125703e-09,7.752374319459371e-10,8.311063758289833e-11],[0.03294023291527302,0.05297119914950971,0.04864302809495766,0.035643219877380485,0.014329468338238942,0.0046086445290404125,0.0012351937916621257,0.00028375936197045547,5.703919016046759e-05,1.019163778325581e-05,1.6389175998394275e-06,2.3959490178368164e-07,3.210771988729642e-08,3.971725744720088e-09,4.5620953199855583e-10,4.890871301276352e-11],[0.012923050085854749,0.02078156100103054,0.016709417466093064,0.010229416189722838,0.005621710007790235,0.0018080547344604615,0.00048458890003735664,0.00011132393800937971,2.2377507566394404e-05,3.998364124160074e-06,6.429770634528079e-07,9.39974202377404e-08,1.2596440143983938e-08,1.558179957570923e-09,1.7897926365080852e-10,1.9187774097540874e-11],[0.0038024599875569687,0.006114737129424848,0.004916555372616744,0.002635438092199202,0.001210050850458743,0.0005319994689662398,0.00014258475286907615,3.275579813787751e-05,6.584326190579806e-06,1.176473007285134e-06,1.8918866215432388e-07,2.7657668043770122e-08,3.7063587399992094e-09,4.5847666786975614e-10,5.2662605508241023e-11,5.64578352412657e-12],[0.0008950643608692894,0.001439353286699211,0.0011573122417251334,0.0006203580627604216,0.000249399500081024,9.160862569917442e-05,3.356314888627166e-05,7.710415788984957e-06,1.549890263884846e-06,2.769310035586175e-07,4.4533283592465116e-08,6.510362515776817e-09,8.724430046931548e-10,1.0792122127338407e-10,1.2396296475227296e-11,1.3289658900199021e-12],[0.00017557498144183225,0.0002823421841475368,0.0002270172785853654,0.00012168885291183891,4.8921970880173e-05,1.5734287422592026e-05,4.8162233908220295e-06,1.5124678942026826e-06,3.040250134126362e-07,5.43225246542609e-08,8.73560693746888e-09,1.2770665751644662e-09,1.7113759753464976e-10,2.1169725050667487e-11,2.4316458332355884e-12,2.6068869645358074e-13],[2.9520533899318966e-05,4.7471980061672144e-05,3.81698532055985e-05,2.0460317740334265e-05,8.22556088532525e-06,2.645505421250117e-06,7.090396865164662e-07,1.8603013360046492e-07,5.1117651506983225e-08,9.13359020393221e-09,1.468772934565915e-09,2.147212935136755e-10,2.8774448432126875e-11,3.559399983217618e-12,4.0884801844590065e-13,4.3831242000596566e-14],[4.343040080234075e-06,6.98404415038955e-06,5.6155218226723794e-06,3.0101074832744128e-06,1.2101387030875277e-06,3.8920488755899003e-07,1.0431341748492761e-07,2.396377717430882e-08,5.501436181674577e-09,1.3437273345867924e-09,2.160848359090806e-10,3.158964492275363e-11,4.233276513682518e-12,5.236564095155217e-13,6.014943147338508e-14,6.448421340354611e-15],[5.67951099254035e-07,9.133223454476321e-07,7.343569787870584e-07,3.9363989795515725e-07,1.5825311163864978e-07,5.089737594875192e-08,1.3641347773220782e-08,3.1338079633135457e-09,6.299346992626805e-10,1.285475535813227e-10,2.825799850322256e-11,4.131063316817372e-12,5.535970207446696e-13,6.847996516756349e-14,7.865903858518637e-15,8.432775017149249e-16],[6.68452514059763e-08,1.0749387029328683e-07,8.64304637022945e-08,4.6329618829500665e-08,1.8625668736547347e-08,5.9903887776032735e-09,1.6055243534433922e-09,3.6883488990668826e-10,7.414043814136134e-11,1.3247251381074727e-11,2.432968977318487e-12,4.862072920527088e-13,6.51558418988552e-14,8.059779255486246e-15,9.25780972426178e-16,9.924991197512379e-17],[7.15216446274557e-09,1.1501397973736873e-08,9.247700891059923e-09,4.9570769261147204e-09,1.9928692499538588e-09,6.409467364105615e-10,1.7178444217420878e-10,3.9463802390238936e-11,7.932719165143607e-12,1.4174009157561344e-12,2.2793228686735635e-13,3.805607167617504e-14,6.971404657288755e-15,8.623629286478972e-16,9.905472164445427e-17,1.0619328649808056e-17],[7.014809200960184e-10,1.1280516933065992e-09,9.070101454774468e-10,4.861877689237077e-10,1.9545967690905798e-10,6.286375386524936e-11,1.6848537136167368e-11,3.870591141379499e-12,7.780373574759914e-13,1.3901801387658087e-13,2.235549128437186e-14,3.2681702479305883e-15,5.001890956520667e-16,8.458014965897516e-17,9.715240420007472e-18,1.0415387496849796e-18],[6.350853976134117e-11,1.0212810322396825e-10,8.21161178269961e-11,4.4016985166100605e-11,1.7695932001997533e-11,5.691366789209146e-12,1.5253814608189973e-12,3.50423773990243e-13,7.043957296273905e-14,1.2585988882798168e-14,2.023953277194638e-15,2.9588362875090283e-16,3.9650879882861646e-17,5.601705469849247e-18,8.795688019862017e-19,9.429565823157668e-20],[5.339046558697869e-12,8.585722488870423e-12,6.903351548396451e-12,3.700427282038985e-12,1.4876645757131353e-12,4.784627765715255e-13,1.2823602415819749e-13,2.9459484529785945e-14,5.921725818860448e-15,1.0580810216237617e-15,1.7015004313087838e-16,2.4874394464020733e-17,3.3333768117401977e-18,4.123387941128665e-19,5.4092487639399196e-20,7.927263191270985e-21],[4.1892093638944443e-13,6.736668925949041e-13,5.416619733664726e-13,2.9034893121645507e-13,1.1672755242710354e-13,3.754192292298e-14,1.0061863055248086e-14,2.31149788807576e-15,4.646400621918515e-16,8.302087038975558e-17,1.3350588838557751e-17,1.9517351097101864e-18,2.615488214910108e-19,3.235359569173433e-20,3.716273402970537e-21,4.550165484933784e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.26067178083289916, "-10": 2.807153336383838e-06, "-11": 4.046471259175036e-07, "-12": 5.358207945439069e-08, "-13": 6.5585729605284365e-09, "-14": 7.417916095228205e-10, "-15": 7.061500552706509e-11, "-2": 0.1728621324511043, "-3": 0.0809398007843123, "-4": 0.029873927231543095, "-5": 0.009060343590974835, "-6": 0.002326814161908754, "-7": 0.0005174852150289558, "-8": 0.00010140928380829767, "-9": 1.7752490059258543e-05, "0": 0.23713375612186796, "1": 0.11987393672837303, "10": 7.929920171685537e-08, "11": 8.366149428713631e-09, "12": 8.108027237995996e-10, "13": 7.263592422357806e-11, "14": 6.012713451292773e-12, "15": 4.1892093638944443e-13, "2": 0.05931038235078809, "3": 0.0203254170939459, "4": 0.005490553552439868, "5": 0.0012187509249326598, "6": 0.00022907540704457055, "7": 3.7287321935634486e-05, "8": 5.347951247901336e-06, "9": 6.851970426639472e-07} |
| Raw goal margin distribution | {"-1": 0.21670085218710963, "-10": 2.3336339601877283e-06, "-11": 3.363899872138395e-07, "-12": 4.4543687247708546e-08, "-13": 5.452252426928111e-09, "-14": 6.166638882629492e-10, "-15": 5.87034462496033e-11, "-2": 0.14370320904451203, "-3": 0.06728662285488823, "-4": 0.024834700052941257, "-5": 0.0075320165880589564, "-6": 0.0019343198951400457, "-7": 0.0004301941956766324, "-8": 8.430324966794052e-05, "-9": 1.4757944691951852e-05, "0": 0.2694786877092371, "1": 0.15557989220536422, "10": 1.029194634946835e-07, "11": 1.0858111961756894e-08, "12": 1.0523104839244022e-09, "13": 9.427144523123443e-11, "14": 7.803675562383188e-12, "15": 5.437017912719766e-13, "2": 0.07697672358674182, "3": 0.026379597490575293, "4": 0.007125983788886348, "5": 0.001581771173127173, "6": 0.00029730839002685964, "7": 4.839381842041103e-05, "8": 6.940905599466298e-06, "9": 8.892915753542557e-07} |
| Research history json | {"away": [{"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.51, "date": "2026-11-01T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 1.37, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 4.0, "away_xg": 2.63, "date": "2026-10-26T00:00:00+00:00", "home": "Rizespor", "home_goals": 3.0, "home_xg": 1.81, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 1.19, "date": "2026-10-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.35, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": 0.92, "date": "2026-09-12T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Genclerbirligi", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-06T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": 3.2, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-08-31T00:00:00+00:00", "home": "Amedspor", "home_goals": 2.0, "home_xg": 2.39, "source": "pipeline training history"}, {"away": "Buyuksehyr", "away_goals": 1.0, "away_xg": 1.95, "date": "2026-08-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-08-15T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 1.0, "home_xg": 1.86, "source": "pipeline training history"}], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-11-02T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 5.0, "home_xg": 1.91, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Erzurumspor", "away_goals": 0.0, "away_xg": 1.69, "date": "2026-10-10T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 0.0, "home_xg": 0.98, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-19T00:00:00+00:00", "home": "Corum", "home_goals": 1.0, "home_xg": 1.14, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 1.79, "date": "2026-09-12T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": 1.73, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 2.06, "date": "2026-09-07T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 0.74, "date": "2026-08-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.54, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 1.25, "date": "2026-08-15T00:00:00+00:00", "home": "Gaziantep", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 46.3% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 56.5% |
| P home draw | 44.4% |
| P draw away | 79.4% |
| P home away | 76.3% |
| Raw p home draw | 53.7% |
| Raw p draw away | 73.2% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5410 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.68, "draw": 4.11, "home": 5.16}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.73, "under": 2.21}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.63, "draw": 4.13, "home": 5.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.06 |
| Reference draw odds | 4.13 |
| Reference away odds | 1.63 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:23Z |
| Market reference home last update utc | 2026-11-06T13:39:23Z |
| Market reference draw last update utc | 2026-11-06T13:39:23Z |
| Market reference away last update utc | 2026-11-06T13:39:23Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market best over 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market best under 2 5 last update utc | 2026-11-06T13:38:36Z |
| Home probability edge | +2.6% |
| Draw probability edge | +1.4% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | 0.0879 |
| Raw ev home | 0.3829 |
| Raw edge prob draw | 0.0462 |
| Raw ev draw | 0.1129 |
| Raw edge prob away | -0.1341 |
| Raw ev away | -0.2230 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,452.1266 |
| Elo away rating | 1,593.6095 |
| Elo rating diff | -81.4829 |
| Elo home expectancy | 0.3848 |
| Research p home | 0.2847 |
| Research p draw | 0.2480 |
| Research p away | 0.4673 |
| Research p over 1 5 | 0.7654 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.1769543450795874, 1.608100321748155], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:18.697329+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T13:40:18.194352+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:18.899212+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Alanyaspor%22+%22Trabzonspor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:18.985606+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Alanyaspor_vs_Trabzonspor&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.7743771520489182, "goals_for": 2.5504665648542564, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.445760234190055, "results": "WWWWWLWLWD", "xg_against": 1.304688418272264, "xg_for": 1.9416908629267322, "xg_matches": 10}, "venue": {"goals_against": 1.4632227425095123, "goals_for": 2.031257084649452, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.6015486554658407, "results": "WWLLD", "xg_against": 1.7335781977270697, "xg_for": 1.5880534238553998, "xg_matches": 5}}, "home": {"all": {"goals_against": 2.0080296773705193, "goals_for": 0.7681538045198641, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 0.9433296058372811, "results": "LLLDWDWLWD", "xg_against": 1.821921306986439, "xg_for": 0.9535220089451488, "xg_matches": 10}, "venue": {"goals_against": 1.069203922761527, "goals_for": 0.9657278891499795, "last_match": "2026-10-23T00:00:00+00:00", "matches": 4, "points_per_game": 1.0971691275701443, "results": "LDDW", "xg_against": 1.4768169943171596, "xg_for": 0.9185985305199439, "xg_matches": 4}}}, "goal_rates": [1.1876746224367756, 1.5915660880216793], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.2267290621423416, "-10": 2.1163121814547474e-06, "-11": 3.0193203345389893e-07, "-12": 3.957038899727719e-08, "-13": 4.793775265022414e-09, "-14": 5.366280434929434e-10, "-15": 5.056635373100962e-11, "-2": 0.141485277552784, "-3": 0.06557665702189314, "-4": 0.023957065432019194, "-5": 0.007191634469946543, "-6": 0.001828009556970259, "-7": 0.00040238646929449456, "-8": 7.804556285012897e-05, "-9": 1.3522353425392727e-05, "0": 0.24803716208285378, "1": 0.16919206516272658, "10": 1.1332030390526015e-07, "11": 1.2064518413416766e-08, "12": 1.1798965145189874e-09, "13": 1.0666552337562464e-10, "14": 8.91030485095651e-12, "15": 6.265469736778049e-13, "2": 0.07878741486643687, "3": 0.02725007318576085, "4": 0.007428905237406278, "5": 0.0016641466870785976, "6": 0.00031565688119590866, "7": 5.185050228268384e-05, "8": 7.504652998636129e-06, "9": 9.70303240008321e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:18.986053+00:00", "p_over_1_5": 0.7653634578458517, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Besiktas JK vs Genclerbirligi SK

The model's most likely 1X2 outcome is **Besiktas JK win** at **76.5%**. Expected goals are 1.92 for Besiktas JK and 0.81 for Genclerbirligi SK (2.73 combined). The most likely exact score is 2-0 at 14.7%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 55.4%; Under 3.5 goals: 68.8%; Double Chance 1X: 91.3%; Double Chance X2: 23.5%; Double Chance 12 (either team wins): 85.2%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 45.6%; BTTS No (at least one team does not score): 54.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Besiktas JK win | 76.5% | 1.31 |
| Draw | 14.8% | 6.76 |
| Genclerbirligi SK win | 8.7% | 11.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Besiktas JK expected goals | 1.92 |
| Genclerbirligi SK expected goals | 0.81 |
| Expected total goals | 2.73 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 55.4% |
| Under 2.5 | 44.6% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.72% |
| 2 | 1-0 | 14.12% |
| 3 | 2-1 | 11.90% |
| 4 | 3-0 | 9.43% |
| 5 | 3-1 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Besiktas JK win | 76.5% | 82.5% | 1.22 | -6.6% |
| Draw | 14.8% | 11.2% | 7.55 | +11.7% |
| Genclerbirligi SK win | 8.7% | 6.4% | 13.10 | +13.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T18:00:00+00:00 |
| Fixture id | 1fa78d1150755a8ec1d24cc1e19eeb0a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:38:36Z |
| Market best draw last update utc | 2026-11-06T13:38:36Z |
| Market best away last update utc | 2026-11-06T13:38:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Besiktas |
| Matched away-team name | Genclerbirligi |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9217 |
| Dc lambda away | 0.8084 |
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
| P btts yes | 45.6% |
| P btts no | 54.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.99 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.64 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.33 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.04763130045933269,0.02644253276266073,0.013120880275733278,0.0035358077569141,0.0007146206788984998,0.00011554535762545051,1.5568550401419205e-05,1.7980305365983777e-06,1.8169961308439158e-07,1.6321437989702738e-08,1.319487698276971e-09,9.69749549921398e-11,6.533189673290447e-12,4.06283177982781e-13,2.3461065471216828e-14,1.2644550599553711e-15,6.3889625476314e-17],[0.14121480679350554,0.07056093884341914,0.02521386749087766,0.006794619444926467,0.0013732577940911686,0.00022203886287586476,2.9917456649035397e-05,3.455202908770504e-06,3.491648327838701e-07,3.1364250422591615e-08,2.5356063984311752e-09,1.8635286762183263e-10,1.25545676245346e-11,7.807380296256841e-13,4.5084185173163393e-14,2.4298523925143228e-15,1.2277412162512512e-16],[0.1471600432203268,0.11896982779926323,0.024993800225414888,0.006528473346874675,0.0013194671136153864,0.00021334157269658997,2.8745586110101835e-05,3.3198621763571334e-06,3.354880023777576e-07,3.0135708789619796e-08,2.436286376963083e-09,1.790534023640179e-10,1.2062803631998974e-11,7.501564228308138e-13,4.331823197078919e-14,2.334674768756102e-15,1.1796504384275392e-16],[0.09426384388176484,0.07620650978961634,0.03080413388191103,0.004314328445586976,0.0008451889472385237,0.00013665663764485597,1.8413078591690635e-05,2.126548504967271e-06,2.1489793009230315e-07,1.9303526191263513e-08,1.5605711554833053e-09,1.1469323871881864e-10,7.726868064592106e-12,4.805151342797356e-13,2.7747634251608636e-14,1.4954835096591103e-15,7.556289216122594e-17],[0.045285758631822604,0.03661074560925893,0.014798766042134944,0.003987963510444685,0.0004189060584944216,6.565188998216274e-05,8.845917993944535e-06,1.0216256663117103e-06,1.0324017557405091e-07,9.273702321508374e-09,7.497216935439735e-10,5.5100345068011754e-11,3.712102835440887e-12,2.308466480236486e-13,1.333037796441403e-14,7.184526162675879e-16,3.630154208678182e-17],[0.0174047639086903,0.01407067924004051,0.005687638606153468,0.001532701791308559,0.0003097737405298866,2.6031551458399075e-05,3.399768909514313e-06,3.926433841989079e-07,3.9678497965923844e-08,3.564180094178766e-09,2.8814200021343774e-10,2.117682304922702e-11,1.4266797202383138e-12,8.872174231703773e-14,5.123290153324214e-15,2.761242947784304e-16,1.3951842447392242e-17],[0.005574339039271024,0.0045065096549603435,0.0018216176955848224,0.0004908885564707925,9.92132880535407e-05,1.6041566089317465e-05,1.1233652138414241e-06,1.2575449782220946e-07,1.2708095403732998e-08,1.1415235705698478e-09,9.228514727748878e-11,6.782441409164946e-12,4.56932165399257e-13,2.841550017136792e-14,1.6408700779289709e-15,8.84361571435076e-17,4.4684490081146685e-18],[0.001530283279472497,0.0012371397443146964,0.000500075628968061,0.00013476011142477643,2.7236311738526115e-05,4.403775979554659e-06,5.933635907424333e-07,3.56162598351634e-08,3.4886622025087744e-09,3.133742710768492e-10,2.5334378986906056e-11,1.8619349503729328e-12,1.2543830714952098e-13,7.800703273294034e-15,4.504562830411924e-16,2.4277743356494835e-17,1.226691228165334e-18],[0.00036758547274726286,0.0002971702062412286,0.00012012190092475834,3.237038522869161e-05,6.542365495719893e-06,1.0578198801699273e-06,1.425303660700364e-07,1.6461002725283226e-08,8.6455326790909e-10,7.527484036832723e-11,6.0855070440750744e-12,4.472506810591384e-13,3.013121822128734e-14,1.8737871862935975e-15,1.0820296344788462e-16,5.831695274099911e-18,2.9466039462674463e-19],[7.848602301277084e-05,6.345111375442026e-05,2.564815799127242e-05,6.911651815299507e-06,1.3969111592396384e-06,2.2586332054386557e-07,3.0432763046332404e-08,3.5147162619186586e-09,3.551789426781505e-10,1.6581742151277653e-11,1.299363770651657e-12,9.54959590316028e-14,6.433549914375355e-15,4.000868236857424e-16,2.310325328079471e-17,1.2451704526451008e-18,6.291522442598767e-20],[1.508234312441648e-05,1.2193145129991258e-05,4.928703283521851e-06,1.3281843089167758e-06,2.6843879469533613e-07,4.3403245175365185e-08,5.8481415782038266e-09,6.754088767957848e-10,6.825330776624606e-11,6.130954884210349e-12,2.5760457823901123e-13,1.8351074061626156e-14,1.236309391047635e-15,7.688307449855656e-17,4.4396591889303444e-18,2.3927939388803774e-19,1.2090165434780831e-20],[2.6348301541261152e-06,2.1300978367298556e-06,8.610264283896669e-07,2.320289386405582e-07,4.689527515492759e-08,7.58238810983194e-09,1.021648934037647e-09,1.1799145930217225e-10,1.1923603112451597e-11,1.0710553837190463e-12,8.658822855450751e-14,3.3074373506709116e-15,2.1597872667995226e-16,1.343119178231524e-17,7.755922145876348e-19,4.1801234534744336e-20,2.1121076608026223e-21],[4.2193725427841647e-07,3.411102727690927e-07,1.3788331915321567e-07,3.715672265622867e-08,7.509730221705174e-09,1.2142308356862184e-09,1.636051361372429e-10,1.8894953167398407e-11,1.9094256798658906e-12,1.7151700160969816e-13,1.3866092792322033e-14,1.0190801522501257e-15,3.5682276492828524e-17,2.1508483852146123e-18,1.2420202833581175e-19,6.6939791536156576e-21,3.3822935635676334e-22],[6.237075676485312e-08,5.042291392178234e-08,2.038190956980814e-08,5.492506024228761e-09,1.1100881760930572e-09,1.794875786412478e-10,2.4184108058785924e-11,2.7930516116727283e-12,2.822512670590029e-13,2.5353639859865356e-14,2.0496855683147004e-15,1.5064040839100996e-16,1.0148624049994888e-17,3.2801165027178774e-19,1.835954142585075e-20,9.89503868989168e-22,4.9997056913444546e-23],[8.561098054217222e-09,6.921120291857499e-09,2.7976496584316663e-09,7.539091246572588e-10,1.5237226894952838e-10,2.4636718230868904e-11,3.3195447864394496e-12,3.833782041184759e-13,3.874220706234629e-14,3.4800763712062466e-15,2.813427324092438e-16,2.0677114950279055e-17,1.3930144528301352e-18,8.662818120612235e-20,2.599899841364003e-21,1.3582069685928924e-22,6.862666558175852e-24],[1.0967678355883274e-09,8.866692186299303e-10,3.58408715935806e-10,9.6583787925816e-11,1.9520510401949485e-11,3.1562259839739923e-12,4.252690399648276e-13,4.911483088733374e-14,4.96328932533988e-15,4.458348456188714e-16,3.604300029375215e-17,2.6489586343491722e-18,1.784599868729643e-19,1.1097992594021222e-20,6.408602299021259e-22,1.7951366723125132e-23,8.791806728188595e-25],[1.317259126943148e-10,1.0649228423017182e-10,4.3046225183031716e-11,1.1600073600970995e-11,2.344486194360665e-12,3.790745269124945e-13,5.107639977420772e-14,5.8988745981874e-15,5.961095822942675e-16,5.3546429831771946e-17,4.328898929999299e-18,3.1814982394332714e-19,2.1433710843322297e-20,1.332910353573602e-21,7.6969706763932e-23,4.14835103292038e-24,1.0893839524237308e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.059099243526296065, "-10": 1.5183974956357908e-09, "-11": 1.1030815907821554e-10, "-12": 7.358777719938667e-12, "-13": 4.537776008168617e-13, "-14": 2.6008882907573904e-14, "-15": 1.3872291815804962e-15, "-16": 6.3889625476314e-17, "-2": 0.021380875060950055, "-3": 0.005141882673769539, "-4": 0.0009676385749227198, "-5": 0.0001490071431350339, "-6": 1.9379316202117656e-05, "-7": 2.1789482052239905e-06, "-8": 2.1561864561268532e-07, "-9": 1.904406071816355e-08, "0": 0.14794646544657614, "1": 0.29530315747773467, "10": 1.7355972365895114e-05, "11": 2.9970961451746022e-06, "12": 4.752567461327507e-07, "13": 6.96618858462474e-08, "14": 9.490813498030184e-09, "15": 1.2032601198184992e-09, "16": 1.317259126943148e-10, "2": 0.23980178402184044, "3": 0.13708144190553587, "4": 0.06131958987575708, "5": 0.02244516093308146, "6": 0.006938788523945964, "7": 0.0018544779620924083, "8": 0.0004362050113109016, "9": 9.157848644987024e-05} |
| Raw goal margin distribution | {"-1": 0.0959878471580964, "-10": 2.466151815826111e-09, "-11": 1.7916037637909058e-10, "-12": 1.1951984304800578e-11, "-13": 7.37016793989858e-13, "-14": 4.2243124079485073e-14, "-15": 2.2531107795914828e-15, "-16": 1.0376829277822739e-16, "-2": 0.03472640333448026, "-3": 0.00835134629049942, "-4": 0.0015716198396453726, "-5": 0.00024201451706139346, "-6": 3.1475510186684674e-05, "-7": 3.539005489899154e-06, "-8": 3.502036297689194e-07, "-9": 3.093099472028312e-08, "0": 0.2329123906298709, "1": 0.24162096821070533, "10": 1.4200887261430691e-05, "11": 2.452263899251604e-06, "12": 3.888613861432305e-07, "13": 5.699828084914064e-08, "14": 7.765509742895946e-09, "15": 9.845234221100254e-10, "16": 1.0777989248570406e-10, "2": 0.1962090068013587, "3": 0.11216185766463553, "4": 0.050172503411789277, "5": 0.01836492898558033, "6": 0.005677408991102861, "7": 0.001517358515748237, "8": 0.00035690873769017654, "9": 7.493073474826276e-05} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 62.6% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 14.1% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 48.3% |
| P home draw | 91.3% |
| P draw away | 23.5% |
| P home away | 85.2% |
| Raw p home draw | 85.9% |
| Raw p draw away | 37.4% |
| Raw p home away | 76.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5539 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -2.0, "market_key": "spreads", "opposite_price": 1.87, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 13.1, "draw": 7.55, "home": 1.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 12.07, "draw": 7.26, "home": 1.19}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.19 |
| Reference draw odds | 7.26 |
| Reference away odds | 12.07 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:23Z |
| Market reference home last update utc | 2026-11-06T13:39:23Z |
| Market reference draw last update utc | 2026-11-06T13:39:23Z |
| Market reference away last update utc | 2026-11-06T13:39:23Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.01 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:23Z |
| Home probability edge | -6.0% |
| Draw probability edge | +3.6% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -15.8% |
| Under 2.5 probability edge | +15.8% |
| Raw edge prob home | -0.1987 |
| Raw ev home | -0.2361 |
| Raw edge prob draw | 0.1214 |
| Raw ev draw | 0.7585 |
| Raw edge prob away | 0.0774 |
| Raw ev away | 0.8460 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,572.0567 |
| Elo away rating | 1,407.1890 |
| Elo rating diff | 224.8678 |
| Elo home expectancy | 0.7849 |
| Research p home | 0.6359 |
| Research p draw | 0.2134 |
| Research p away | 0.1507 |
| Research p over 1 5 | 0.7567 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.9216597485086455, 0.8084383858269366], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:18.697329+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T13:40:18.194352+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:19.013874+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Besiktas+JK%22+%22Genclerbirligi+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:19.100142+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Besiktas+JK_vs_Genclerbirligi+SK&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.9216597485086455, 0.8084383858269366], "h2h": [], "margin_distribution": {"-1": 0.10576100069000637, "-10": 2.466151815826111e-09, "-11": 1.7916037637909058e-10, "-12": 1.1951984304800578e-11, "-13": 7.37016793989858e-13, "-14": 4.2243124079485073e-14, "-15": 2.2531107795914828e-15, "-16": 1.0376829277822739e-16, "-2": 0.03472640333448026, "-3": 0.00835134629049942, "-4": 0.0015716198396453726, "-5": 0.00024201451706139346, "-6": 3.1475510186684674e-05, "-7": 3.539005489899154e-06, "-8": 3.502036297689194e-07, "-9": 3.093099472028312e-08, "0": 0.21336608356605097, "1": 0.2513941217426153, "10": 1.4200887261430691e-05, "11": 2.452263899251604e-06, "12": 3.888613861432305e-07, "13": 5.699828084914064e-08, "14": 7.765509742895946e-09, "15": 9.845234221100254e-10, "16": 1.0777989248570406e-10, "2": 0.1962090068013587, "3": 0.11216185766463553, "4": 0.050172503411789277, "5": 0.01836492898558033, "6": 0.005677408991102861, "7": 0.001517358515748237, "8": 0.00035690873769017654, "9": 7.493073474826276e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:19.100627+00:00", "p_over_1_5": 0.7567495216741861, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Çaykur Rizespor vs Erzurum BB

The model's most likely 1X2 outcome is **Çaykur Rizespor win** at **49.0%**. Expected goals are 1.42 for Çaykur Rizespor and 0.93 for Erzurum BB (2.35 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.5%; Double Chance 1X: 75.8%; Double Chance X2: 51.0%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çaykur Rizespor win | 49.0% | 2.04 |
| Draw | 26.8% | 3.73 |
| Erzurum BB win | 24.2% | 4.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çaykur Rizespor expected goals | 1.42 |
| Erzurum BB expected goals | 0.93 |
| Expected total goals | 2.35 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.75% |
| 2 | 2-1 | 9.49% |
| 3 | 1-0 | 9.11% |
| 4 | 2-0 | 8.58% |
| 5 | 0-0 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çaykur Rizespor win | 49.0% | 49.9% | 2.01 | -1.5% |
| Draw | 26.8% | 25.7% | 3.71 | -0.6% |
| Erzurum BB win | 24.2% | 24.5% | 3.82 | -7.6% |
| Over 2.5 | 52.6% | 52.6% | 1.86 | -2.1% |
| Under 2.5 | 47.4% | 47.4% | 2.03 | -3.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T10:30:00+00:00 |
| Fixture id | cf2febfddf729564889172cf83e8fbab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:38:36Z |
| Market best draw last update utc | 2026-11-06T13:38:36Z |
| Market best away last update utc | 2026-11-06T13:39:23Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Rizespor |
| Matched away-team name | Erzurumspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4173 |
| Dc lambda away | 0.9324 |
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
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.57 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.28 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.67 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.07367254905084897,0.057667857547188735,0.03809535956588575,0.01405439910068409,0.0038887833649336435,0.0008608058417039578,0.00015878717231404627,2.510607572907436e-05,3.4733640675266023e-06,4.271390302587662e-07,4.7274910680552e-08,4.7566313234022745e-09,4.3871219326786564e-10,3.735061975316028e-11,2.952780991011282e-12,2.1787200844141052e-13],[0.0910754904570556,0.127507817313731,0.06408974452239669,0.02364442436147149,0.00654229636369488,0.0014481770773886263,0.0002671356675198346,4.223721728242225e-05,5.843415530336568e-06,7.18597530953429e-07,7.953296628151284e-08,8.002320749246175e-09,7.380676467108725e-10,6.283683117869444e-11,4.9676123680420296e-12,3.665370669475342e-13],[0.0857676476728218,0.09492595140643896,0.05413264631165067,0.019889103738278444,0.005503217548240256,0.0012181706639690323,0.00022470790247505076,3.5528900315085656e-05,4.915336313203375e-06,6.044664323692606e-07,6.690115998609857e-08,6.731353874196419e-09,6.208442111713995e-10,5.285678495663597e-11,4.178632400141635e-12,3.083218959782756e-13],[0.0480970796292686,0.05323290503543039,0.029458567966637303,0.011199397825068168,0.003086113468386226,0.0006831299798551405,0.00012601247873670238,1.9924020233290362e-05,2.7564393856600233e-06,3.38974787343934e-07,3.751706507582657e-08,3.774832026815677e-09,3.4815917507719623e-10,2.9641211622177225e-11,2.3433080041758086e-12,1.7290182469366423e-13],[0.020229035641348734,0.022389100160645853,0.012389908616771085,0.004570969338665615,0.0013033246590910717,0.0002873160037299674,5.299928692693926e-05,8.379795998527097e-06,1.1593242459943913e-06,1.425685947578045e-07,1.577921263468687e-08,1.587647570271414e-09,1.4643143441942647e-10,1.2466726274850579e-11,9.85566306738592e-13,7.272036475274771e-14],[0.006806465359363531,0.007533262453661685,0.004168833616238043,0.0015379944459016231,0.00042555552704430104,9.707122863724978e-05,1.7832674623491288e-05,2.8195506792188826e-06,3.9007792860386494e-07,4.79700673208876e-08,5.3092330301943535e-09,5.341959143045718e-10,4.926979731354544e-11,4.194680460248578e-12,3.316135798614282e-13,2.446822737304035e-14],[0.0019084766532946659,0.0021122645539033503,0.001168906504036664,0.00043124093607002287,0.00011932225394011264,2.6412706391188934e-05,5.020719385386534e-06,7.905787159656586e-07,1.0937462844527475e-07,1.3450410558975966e-08,1.4886650779890706e-09,1.4978412096568815e-10,1.381484411084323e-11,1.1761537455564632e-12,9.298170807706601e-14,6.860688804463348e-15],[0.00045867521672844077,0.0005076527398838631,0.000280930051278715,0.00010364262485088597,2.867740644981155e-05,6.347918276835605e-06,1.170958588366588e-06,1.9078656625200873e-07,2.6286636160900058e-08,3.2326148541426607e-09,3.5777947616175146e-10,3.599848288833558e-11,3.320201274493816e-12,2.82671822690505e-13,2.234683092947641e-14,1.648868965130457e-15],[9.645655597514369e-05,0.00010675622561384985,5.9077849048706054e-05,2.1795401802271434e-05,6.030680881731358e-06,1.3349278798242615e-06,2.4624533548806763e-07,3.893421584753459e-08,5.550674248372849e-09,6.797988734789178e-10,7.523880691723826e-11,7.57025789294992e-12,6.982177549644319e-13,5.944413278401564e-14,4.699400076137705e-15,3.4674692643126936e-16],[1.8030414262181814e-05,1.995570911095647e-05,1.1043293856991013e-05,4.074167064465032e-06,1.1273020634145061e-06,2.495351657545188e-07,4.603010509854758e-08,7.27788830533359e-09,1.0068780163019838e-09,1.2759646563779893e-10,1.4064226569106421e-11,1.4150918462879047e-12,1.3051632665034625e-13,1.1111762479142869e-14,8.784486373152967e-16,6.481664895131825e-17],[3.0333475175569997e-06,3.3572495791055947e-06,1.8578690161887953e-06,6.854176710198359e-07,1.8965171104069185e-07,4.1980559324822205e-08,7.743876707615445e-09,1.2243958515332169e-09,1.6939216630415655e-10,2.083110328832091e-11,2.3758365965909033e-12,2.380680375190196e-13,2.195741981790602e-14,1.8693878377763e-15,1.4778584421605199e-16,1.090443171931055e-17],[4.639230453244083e-07,5.134609337169323e-07,2.8414424882590864e-07,1.0482842846664057e-07,2.9005512499880976e-08,6.420546545909419e-09,1.1843558458171951e-09,1.8726026241244494e-10,2.5906998519316952e-11,3.1859286873824325e-12,3.526123427291779e-13,3.656024693941572e-14,3.3581886053047856e-15,2.859059483207715e-16,2.2602507133692147e-17,1.6677341259035495e-18],[6.504009454106664e-08,7.198510185830725e-08,3.983584991776897e-08,1.4696512636689718e-08,4.06645303400515e-09,9.001341031878604e-10,1.6604179714407155e-10,2.6253115239346725e-11,3.6320541735394487e-12,4.4665404126141535e-13,4.9434793849086894e-14,4.973950992259287e-15,4.727423952497647e-16,4.008283290956819e-17,3.168778131753494e-18,2.3380943523139755e-19],[8.416940844381406e-09,9.315705155311196e-09,5.155219939476097e-09,1.9018987957284805e-09,5.262460775186215e-10,1.1648776884478186e-10,2.1487729901345677e-11,3.3974568996173152e-12,4.700298383325318e-13,5.780220139175046e-14,6.397434358267007e-15,6.436868144197509e-16,5.936832916655546e-17,5.208537192607856e-18,4.1007655773160235e-19,3.0257646442354405e-20],[1.0114460031047116e-09,1.1194486119896156e-09,6.194918913312177e-10,2.2854716111416536e-10,6.323787960456561e-11,1.399808913796629e-11,2.582135116111415e-12,4.0826521955804595e-13,5.648249288086006e-14,6.9459684521088435e-15,7.687661742464669e-16,7.73504849010151e-17,7.13416671885028e-18,6.073812227250574e-19,4.948090352678697e-20,3.635997463128668e-21],[1.1344044117336395e-10,1.25553656868685e-10,6.948016329118815e-11,2.56330943086704e-11,7.092551593648765e-12,1.5699794181010518e-12,2.8960374141751323e-13,4.578967782782401e-14,6.334889743306264e-15,7.790368671830332e-16,8.622227355487401e-17,8.675374765642696e-18,8.001445628402188e-19,6.812187072255858e-20,5.385425095247033e-21,4.0948031260096676e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.14503878551406021, "-10": 5.5928726887125865e-08, "-11": 5.549971783438711e-09, "-12": 5.059005586713954e-10, "-13": 4.262655401718058e-11, "-14": 3.319318057958816e-12, "-15": 2.1787200844141052e-13, "-2": 0.06798206297697823, "-3": 0.02194966229690454, "-4": 0.005582801184716966, "-5": 0.001166374879916982, "-6": 0.00020629502820784497, "-7": 3.159311287307092e-05, "-8": 4.262788311238401e-06, "-9": 5.137643147900962e-07, "0": 0.2679180235756624, "1": 0.22048415832310395, "10": 3.588611007846452e-06, "11": 5.412990068348994e-07, "12": 7.500092468201772e-08, "13": 9.605869619662209e-09, "14": 1.1369996599733967e-09, "15": 1.1344044117336395e-10, "2": 0.1530543796389938, "3": 0.07511631395741324, "4": 0.029041135374773062, "5": 0.009222625860056632, "6": 0.0024794776510458022, "7": 0.0005771900814192346, "8": 0.00011837914809948324, "9": 2.1687045136520407e-05} |
| Raw goal margin distribution | {"-1": 0.15002855230061227, "-10": 1.471860253914532e-08, "-11": 1.2353858175542302e-09, "-12": 9.518087726602899e-11, "-13": 6.7525473756493905e-12, "-14": 4.1094591321353026e-13, "-2": 0.06303477212904235, "-3": 0.01775334619646124, "-4": 0.003891851292404614, "-5": 0.0006960358832398447, "-6": 0.00010494129091588425, "-7": 1.3662085609409184e-05, "-8": 1.5640854845608464e-06, "-9": 1.5972826630684547e-07, "0": 0.2940789311780762, "1": 0.23437369087839238, "10": 9.692071619172317e-07, "11": 1.236538525762013e-07, "12": 1.4481373256048439e-08, "13": 1.5616463405468302e-09, "14": 1.4446236401761792e-10, "2": 0.14564319399965595, "3": 0.06235125984990574, "4": 0.020776684851366755, "5": 0.005648155543141183, "6": 0.0012944236059885788, "7": 0.0002561545226837297, "8": 4.45759405065658e-05, "9": 6.919533417321846e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.9% |
| Raw p btts yes | 47.2% |
| P home draw | 75.8% |
| P draw away | 51.0% |
| P home away | 73.2% |
| Raw p home draw | 76.4% |
| Raw p draw away | 53.0% |
| Raw p home away | 70.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1870 |
| Totals anchor target over 2 5 | 0.5262 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.02 |
| Totals anchor reference last update utc | 2026-11-06T13:39:23Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4266 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.57, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.77, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.77, "draw": 3.71, "home": 2.01}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.86, "under": 2.03}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.85, "home_away": 1.3, "home_draw": 1.3}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.82, "draw": 3.65, "home": 1.94}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.02}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.02}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.25, "under": 3.89}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.94 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.82 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:23Z |
| Market reference home last update utc | 2026-11-06T13:39:23Z |
| Market reference draw last update utc | 2026-11-06T13:39:23Z |
| Market reference away last update utc | 2026-11-06T13:39:23Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:39:23Z |
| Market best over 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market best under 2 5 last update utc | 2026-11-06T13:38:36Z |
| Home probability edge | -0.8% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0282 |
| Raw ev home | -0.0545 |
| Raw edge prob draw | 0.0374 |
| Raw ev draw | 0.0910 |
| Raw edge prob away | -0.0092 |
| Raw ev away | -0.1003 |
| Market p home draw | 74.1% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T13:38:36Z |
| Market reference home draw last update utc | 2026-11-06T13:39:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.9% |
| Market draw away odds | 1.85 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T13:38:36Z |
| Market reference draw away last update utc | 2026-11-06T13:39:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.1% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T13:38:36Z |
| Market reference home away last update utc | 2026-11-06T13:39:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.80 |
| Market reference dc home draw odds | 1.26 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 76.6% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.67 |
| Market reference over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.2% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.08 |
| Market reference under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,458.4916 |
| Elo away rating | 1,419.5564 |
| Elo rating diff | 98.9351 |
| Elo home expectancy | 0.6387 |
| Research p home | 0.4826 |
| Research p draw | 0.2698 |
| Research p away | 0.2477 |
| Research p over 1 5 | 0.6805 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.417345942197765, 0.9324399254745661], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:18.697329+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T13:40:18.194352+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:18.698845+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87aykur+Rizespor%22+%22Erzurum+BB%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:18.785080+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87aykur+Rizespor_vs_Erzurum+BB&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.417345942197765, 0.9324399254745661], "h2h": [], "margin_distribution": {"-1": 0.16218972752920405, "-10": 1.471860253914532e-08, "-11": 1.2353858175542302e-09, "-12": 9.518087726602899e-11, "-13": 6.7525473756493905e-12, "-14": 4.1094591321353026e-13, "-2": 0.06303477212904235, "-3": 0.01775334619646124, "-4": 0.003891851292404614, "-5": 0.0006960358832398447, "-6": 0.00010494129091588425, "-7": 1.3662085609409184e-05, "-8": 1.5640854845608464e-06, "-9": 1.5972826630684547e-07, "0": 0.26975658072089265, "1": 0.24653486610698416, "10": 9.692071619172317e-07, "11": 1.236538525762013e-07, "12": 1.4481373256048439e-08, "13": 1.5616463405468302e-09, "14": 1.4446236401761792e-10, "2": 0.14564319399965595, "3": 0.06235125984990574, "4": 0.020776684851366755, "5": 0.005648155543141183, "6": 0.0012944236059885788, "7": 0.0002561545226837297, "8": 4.45759405065658e-05, "9": 6.919533417321846e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:18.785557+00:00", "p_over_1_5": 0.6804653128053102, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Çorum FK vs Fenerbahce

The model's most likely 1X2 outcome is **Fenerbahce win** at **53.8%**. Expected goals are 1.87 for Çorum FK and 2.27 for Fenerbahce (4.14 combined). The most likely exact score is 1-2 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 59.9%; Under 3.5 goals: 63.4%; Double Chance 1X: 46.2%; Double Chance X2: 76.4%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çorum FK win | 23.6% | 4.23 |
| Draw | 22.6% | 4.43 |
| Fenerbahce win | 53.8% | 1.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çorum FK expected goals | 1.87 |
| Fenerbahce expected goals | 2.27 |
| Expected total goals | 4.14 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 59.9% |
| Under 2.5 | 40.1% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.33% |
| 2 | 1-1 | 10.43% |
| 3 | 0-1 | 8.59% |
| 4 | 0-2 | 8.24% |
| 5 | 1-3 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çorum FK win | 23.6% | 20.1% | 4.59 | +8.5% |
| Draw | 22.6% | 23.1% | 4.11 | -7.3% |
| Fenerbahce win | 53.8% | 56.8% | 1.76 | -5.3% |
| Over 2.5 | 59.9% | 58.8% | 1.66 | -0.5% |
| Under 2.5 | 40.1% | 41.2% | 2.33 | -6.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T13:00:00+00:00 |
| Fixture id | 6692a3ca274d09ffbfabd943320d62f5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-06T13:39:23Z |
| Market best draw last update utc | 2026-11-06T13:38:36Z |
| Market best away last update utc | 2026-11-06T13:38:36Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Corum |
| Matched away-team name | Fenerbahce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8739 |
| Dc lambda away | 2.2664 |
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
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.69 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.58 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.05 |
| Fair Under 4.5 odds | 1.25 |
| Score matrix json | [[0.050786767751899414,0.08591447959433209,0.08236996644891241,0.04566371407730196,0.01898605954234715,0.00631521923661887,0.0017504946158700826,0.0004158975261026796,8.646093899341133e-05,1.5977213407829876e-05,2.657202386720688e-06,4.017496864135681e-07,5.567982968165092e-08,7.12324929191287e-09,8.462013340288633e-10,9.382229333040023e-11],[0.04254791565626921,0.10433711334826282,0.11327130475830893,0.06279459245445214,0.026108736342808105,0.00868439254749795,0.0024071978860763167,0.0005719227220593992,0.00011889701784067636,2.1971112616991155e-05,3.6540597784196263e-06,5.524672781617623e-07,7.656828366772137e-08,9.795557485313565e-09,1.1636562854874947e-09,1.290200061880873e-10],[0.03484539797629328,0.05795207981853906,0.0544073975291131,0.04317608544549779,0.017951753282398,0.005971184142089787,0.0016551326722733398,0.00039324061755428326,8.175079415042768e-05,1.5106820485728093e-05,2.5124455952228524e-06,3.7986351173559744e-07,5.2646551698708565e-08,6.735195029396161e-09,8.00102703872815e-10,8.871112294257042e-11],[0.015972584279430213,0.026564325070978813,0.022089830741585128,0.01382579315268186,0.008228802336013438,0.002737097220769696,0.0007586868750791839,0.00018025533558991744,3.747328270913781e-05,6.924729732364586e-06,1.1516656817776178e-06,1.7412347995006558e-07,2.4132354137585154e-08,3.087307836708296e-09,3.667545389638849e-10,4.066378833403212e-11],[0.005491186714320324,0.009132502690406758,0.0075942241385439715,0.004210035461365608,0.0019762627473889688,0.000940981849371077,0.00026082762913507904,6.196966543800983e-05,1.2882874089409874e-05,2.380640680393129e-06,3.9592912333291547e-07,5.98616055502278e-08,8.29641967181455e-09,1.0613801423343857e-09,1.2608589922225174e-10,1.3979732418211815e-11],[0.0015102443539013169,0.0025117176564415098,0.002088643989756726,0.0011578885614416275,0.0004814269188379681,0.00018079203256518236,7.173557825222791e-05,1.7043554009343507e-05,3.5431845369259227e-06,6.547490248064768e-07,1.0889262270016355e-07,1.646377304234306e-08,2.2817692456674383e-09,2.919120129576378e-10,3.467747998995981e-11,3.84485413664701e-12],[0.0003461361704296494,0.0005756660030248366,0.0004787008341648378,0.0002653789841401315,0.00011033927695068113,3.6701492629334433e-05,1.1485539464378971e-05,3.906249011999643e-06,8.120701286311362e-07,1.5006334534780196e-07,2.4957335753058e-08,3.773367757991229e-09,5.229636293353656e-10,6.690394571352206e-11,7.947806653187328e-12,8.812104367625746e-13],[6.799859799614836e-05,0.00011308983129716382,9.404098260632813e-05,5.2133814379386515e-05,2.167619791725864e-05,7.210023847155101e-06,1.9985225297573625e-06,5.360804014423605e-07,1.595315223859053e-07,2.9480008060400913e-08,4.902879230507962e-09,7.412797019993109e-10,1.0273642755578425e-10,1.3143308609680712e-11,1.561349999598035e-12,1.7311416534437944e-13],[1.1688559326924964e-05,1.943947730310129e-05,1.616509217467465e-05,8.961496270068237e-06,3.7260110179388725e-06,1.2393607216841401e-06,3.435342763477015e-07,8.161982011779417e-08,1.9156870699500473e-08,5.067440113864409e-09,8.427761225575062e-10,1.2742162382752342e-10,1.76597880531321e-11,2.2592574988831167e-12,2.683868879389195e-13,2.9757307526744764e-14],[1.7859507978781625e-06,2.9702505697031702e-06,2.4699416292161124e-06,1.3692698104241987e-06,5.693150168696981e-07,1.8936784319106998e-07,5.249024261941133e-08,1.2471082088471173e-08,2.5926133240978264e-09,5.408964870636715e-10,1.2877178841425446e-10,1.9469358402235656e-11,2.698323350354928e-12,3.452027422616534e-13,4.1008114280637493e-14,4.546761122020768e-15],[2.4559555603955596e-07,4.084548919879163e-07,3.3965475898511314e-07,1.882955459124859e-07,7.828952415480892e-08,2.6040975372768943e-08,7.218211351668476e-09,1.7149645687730593e-09,3.565239936530463e-10,6.588246667134374e-11,1.23705432681974e-11,2.6773346209824683e-12,3.7106073940685635e-13,4.747065794469551e-14,5.639243052413525e-15,6.252492102629049e-16],[3.070286005132135e-08,5.106254196213039e-08,4.246156851960955e-08,2.3539561902769442e-08,9.787279307376782e-09,3.255484078633967e-09,9.023768040633518e-10,2.1439442145090497e-10,4.457045745691195e-11,8.236224574520878e-12,1.3697830177482156e-12,2.338180391567842e-13,4.638775284156046e-14,5.9344924269940284e-15,7.049838076294521e-16,7.816484674832341e-17],[3.518427455778556e-09,5.851567225369032e-09,4.865929370914975e-09,2.6975415566257157e-09,1.1215838581450262e-09,3.7306571912093753e-10,1.0340884587191948e-10,2.4568760615060646e-11,5.107599779658318e-12,9.438390634134152e-13,1.569717664754529e-13,2.3732990107360594e-14,3.71355733728302e-15,6.800695784152882e-16,8.078838194541498e-17,8.957385156181513e-18],[3.721827690685287e-10,6.18984623301429e-10,5.147228669969207e-10,2.8534863908405597e-10,1.1864226030336332e-10,3.946326423724663e-11,1.0938690959673435e-11,2.5989080272998516e-12,5.402870041174108e-13,9.984023845633631e-14,1.6604630178309272e-14,2.5104993885624684e-15,3.479384878153974e-16,5.025485693465304e-17,8.545875701267527e-18,9.475211448698956e-19],[3.6557731692082486e-11,6.079989634343293e-11,5.055876314356766e-11,2.8028430796093747e-11,1.1653661265317618e-11,3.876287527468471e-12,1.0744552472624507e-12,2.5527829402798996e-13,5.3069805952264706e-14,9.806828668331574e-15,1.6309933327222786e-15,2.465943366746918e-16,3.417633200682149e-17,4.372257137991879e-18,5.8640353732426265e-19,9.307046608691992e-20],[3.3514982432621327e-12,5.573943906089421e-12,4.6350689174151235e-12,2.5695586740915605e-12,1.0683711338344005e-12,3.5536588944064915e-13,9.850268895221914e-14,2.340311377040543e-14,4.865273450699305e-15,8.990593106465713e-16,1.4952435603587602e-16,2.260699578203348e-17,3.1331789851396223e-18,4.0083482860737004e-19,4.761688841605914e-20,5.9605821114365316e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2516074605412462, "-10": 3.2655334551712263e-06, "-11": 4.854338993820676e-07, "-12": 6.631615365917133e-08, "-13": 8.375616700342936e-09, "-14": 9.752213402169505e-10, "-15": 9.382229333040023e-11, "-2": 0.16613212300243596, "-3": 0.0785679893836467, "-4": 0.02951940343744874, "-5": 0.009155624434666776, "-6": 0.002411505791088521, "-7": 0.0005511152419807106, "-8": 0.00011112721713818098, "-9": 2.0036365990955447e-05, "0": 0.2255261678921525, "1": 0.12732007289146585, "10": 3.018213850388401e-07, "11": 3.709824694561724e-08, "12": 4.190540400897644e-09, "13": 4.376177343293768e-10, "14": 4.2131675598171904e-11, "15": 3.3514982432621327e-12, "2": 0.0702797414183337, "3": 0.02748207975311111, "4": 0.008537661835982053, "5": 0.0021895091192906005, "6": 0.0004768420147818683, "7": 9.010648401823929e-05, "8": 1.502316636249676e-05, "9": 2.2396874169928336e-06} |
| Raw goal margin distribution | {"-1": 0.18429546556867946, "-10": 2.293438464189721e-05, "-11": 4.581627703747695e-06, "-12": 8.428647646512926e-07, "-13": 1.4365259303866375e-07, "-14": 2.2798441453686412e-08, "-15": 3.3789295395731877e-09, "-16": 4.6064021485204665e-10, "-17": 4.913507029763915e-11, "-2": 0.1399210447989949, "-3": 0.08144171260730605, "-4": 0.038840794193534096, "-5": 0.0155887860755515, "-6": 0.0053806370247553815, "-7": 0.0016253754287870702, "-8": 0.00043586749838038876, "-9": 0.00010498349657278111, "0": 0.2129328606713314, "1": 0.15125573531380768, "10": 3.425794082571367e-06, "11": 5.658761307948432e-07, "12": 8.607695481161636e-08, "13": 1.2130253628558154e-08, "14": 1.5918017831114495e-09, "15": 1.9506995327021268e-10, "16": 2.198874843702566e-11, "17": 1.9393565382522363e-12, "2": 0.09566165099755386, "3": 0.04603934608823937, "4": 0.018155063266917824, "5": 0.00602489355955172, "6": 0.001719484215620624, "7": 0.0004294826302450005, "8": 9.523000699377883e-05, "9": 1.8965652105843186e-05} |
| Research history json | {"away": [{"away": "Goztep", "away_goals": 2.0, "away_xg": 1.4, "date": "2026-10-31T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 1.51, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 3.0, "away_xg": 0.96, "date": "2026-10-10T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.52, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 0.0, "away_xg": 1.33, "date": "2026-09-14T00:00:00+00:00", "home": "Gaziantep", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 2.0, "away_xg": 1.75, "date": "2026-09-05T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Konyaspor", "away_goals": 2.0, "away_xg": 2.15, "date": "2026-08-22T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 4.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 2.9, "date": "2026-08-15T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 2.0, "home_xg": 1.19, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 46.8% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.7% |
| Raw p btts yes | 76.5% |
| P home draw | 46.2% |
| P draw away | 76.4% |
| P home away | 77.4% |
| Raw p home draw | 53.2% |
| Raw p draw away | 68.1% |
| Raw p home away | 78.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7338 |
| Totals anchor target over 2 5 | 0.5992 |
| Totals anchor reference over odds | 1.61 |
| Totals anchor reference under odds | 2.34 |
| Totals anchor reference last update utc | 2026-11-06T13:39:23Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7787 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.94, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 2.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.55, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.03, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.76, "draw": 4.11, "home": 4.54}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.66, "under": 2.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-06T13:38:36Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.23, "home_away": 1.26, "home_draw": 2.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.71, "draw": 4.02, "home": 4.59}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.61, "under": 2.34}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-06T13:39:23Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.19, "under": 4.74}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.59 |
| Reference draw odds | 4.02 |
| Reference away odds | 1.71 |
| Market reference 1x2 last update utc | 2026-11-06T13:39:23Z |
| Market reference home last update utc | 2026-11-06T13:39:23Z |
| Market reference draw last update utc | 2026-11-06T13:39:23Z |
| Market reference away last update utc | 2026-11-06T13:39:23Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market reference under 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market best over 2 5 last update utc | 2026-11-06T13:38:36Z |
| Market best under 2 5 last update utc | 2026-11-06T13:38:36Z |
| Home probability edge | +3.6% |
| Draw probability edge | -0.5% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | 0.1186 |
| Raw ev home | 0.4661 |
| Raw edge prob draw | -0.0180 |
| Raw ev draw | -0.1248 |
| Raw edge prob away | -0.1006 |
| Raw ev away | -0.1769 |
| Market p home draw | 44.8% |
| Market home draw odds | 2.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-06T13:38:36Z |
| Market reference home draw last update utc | 2026-11-06T13:39:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 78.9% |
| Market draw away odds | 1.23 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-06T13:38:36Z |
| Market reference draw away last update utc | 2026-11-06T13:39:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-06T13:38:36Z |
| Market reference home away last update utc | 2026-11-06T13:39:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.18 |
| Market reference dc home draw odds | 2.08 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-11-06T13:39:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.2% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.49 |
| Market reference under 3 5 last update utc | 2026-11-06T13:39:23Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,445.1258 |
| Elo away rating | 1,661.7220 |
| Elo rating diff | -156.5962 |
| Elo home expectancy | 0.2888 |
| Research p home | 0.3259 |
| Research p draw | 0.1999 |
| Research p away | 0.4742 |
| Research p over 1 5 | 0.9182 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.8739358397166408, 2.2663516739729026], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T13:40:18.697329+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T13:40:18.194352+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T13:40:18.793441+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87orum+FK%22+%22Fenerbahce%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T13:39:37.900672+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T13:39:38.005906+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T13:40:18.885117+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87orum+FK_vs_Fenerbahce&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 1.0089728918892988, "goals_for": 2.3331960885564245, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.4847509690034097, "results": "LLWWWDLWWL", "xg_against": 1.3380003484001706, "xg_for": 1.9676008712062978, "xg_matches": 10}, "venue": {"goals_against": 0.8151944568095735, "goals_for": 1.425370020202056, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.384791003310632, "results": "LWDWL", "xg_against": 1.2819506533747527, "xg_for": 1.2552734770676013, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.8739358397166408, 2.2663516739729026], "h2h": [], "margin_distribution": {"-1": 0.19081709103981442, "-10": 2.293438464189721e-05, "-11": 4.581627703747695e-06, "-12": 8.428647646512926e-07, "-13": 1.4365259303866375e-07, "-14": 2.2798441453686412e-08, "-15": 3.3789295395731877e-09, "-16": 4.6064021485204665e-10, "-17": 4.913507029763915e-11, "-2": 0.1399210447989949, "-3": 0.08144171260730605, "-4": 0.038840794193534096, "-5": 0.0155887860755515, "-6": 0.0053806370247553815, "-7": 0.0016253754287870702, "-8": 0.00043586749838038876, "-9": 0.00010498349657278111, "0": 0.19988960972906147, "1": 0.15777736078494264, "10": 3.425794082571367e-06, "11": 5.658761307948432e-07, "12": 8.607695481161636e-08, "13": 1.2130253628558154e-08, "14": 1.5918017831114495e-09, "15": 1.9506995327021268e-10, "16": 2.198874843702566e-11, "17": 1.9393565382522363e-12, "2": 0.09566165099755386, "3": 0.04603934608823937, "4": 0.018155063266917824, "5": 0.00602489355955172, "6": 0.001719484215620624, "7": 0.0004294826302450005, "8": 9.523000699377883e-05, "9": 1.8965652105843186e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T13:40:18.885578+00:00", "p_over_1_5": 0.9181754942729436, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
