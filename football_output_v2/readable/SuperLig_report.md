# Super Lig — football model report

Fixtures in this report: **8**.

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
| Training as of utc | 2026-11-05T16:49:26.673007+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1809, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1512, 'tuning_matches': 189, 'audit_matches': 91, 'audit_matchdays': 37, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8325722859834472, 'audit_candidate_poisson_score': 0.8249893160912419, 'audit_gain': 0.007582969892205305, 'audit_gain_lower95': -0.0033649132887897094, 'audit_baseline_briers': [0.5922616538597081, 0.16649124205995283, 0.22016788272884508, 0.24972546751554317], 'audit_candidate_briers': [0.5911075620276101, 0.16507712508485967, 0.2163218746136853, 0.24937358369341203], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1671.743 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.247 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1840, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 8.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 37.00 |
| Over 1 5 in window quote fixtures | 5 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 3, 'ANCHORED_ALTERNATE': 3, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 8} |
| Legacy comparison status | {'None': 8} |
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

The model's most likely 1X2 outcome is **Gazişehir Gaziantep win** at **36.5%**. Expected goals are 1.39 for Gazişehir Gaziantep and 1.41 for Kasimpasa SK (2.81 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.2%; Double Chance 1X: 64.3%; Double Chance X2: 63.5%; Double Chance 12 (either team wins): 72.1%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gazişehir Gaziantep win | 36.5% | 2.74 |
| Draw | 27.9% | 3.59 |
| Kasimpasa SK win | 35.7% | 2.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gazişehir Gaziantep expected goals | 1.39 |
| Kasimpasa SK expected goals | 1.41 |
| Expected total goals | 2.81 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.27% |
| 2 | 2-1 | 8.45% |
| 3 | 1-2 | 8.17% |
| 4 | 1-0 | 7.99% |
| 5 | 0-0 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Gazişehir Gaziantep win | 36.5% | 36.8% | 2.61 | -4.8% |
| Draw | 27.9% | 28.0% | 3.46 | -3.6% |
| Kasimpasa SK win | 35.7% | 35.2% | 2.79 | -0.5% |
| Over 2.5 | 51.0% | 51.0% | 1.93 | -1.6% |
| Under 2.5 | 49.0% | 49.0% | 1.96 | -3.9% |

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
| Market best home last update utc | 2026-11-05T16:49:11Z |
| Market best draw last update utc | 2026-11-05T16:49:11Z |
| Market best away last update utc | 2026-11-05T16:49:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Gaziantep |
| Matched away-team name | Kasimpasa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3920 |
| Dc lambda away | 1.4143 |
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
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.88 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.25 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.47 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.20 |
| Fair Under 4.5 odds | 1.16 |
| Score matrix json | [[0.07763720939011476,0.07747681187455804,0.06077670290080405,0.027663185698069668,0.009443402732148241,0.0025789612558691738,0.0005869213096807535,0.0001144901563892653,1.9541795862757588e-05,2.964887871084137e-06,4.048504106201024e-07,5.025603361928168e-08,5.718646800928363e-09,6.00670401822392e-10,5.858608906230987e-11],[0.07991248878579982,0.13272362782605585,0.08168146815679946,0.03717821984190943,0.012691557171450228,0.0034660212161017135,0.0007887988650105148,0.0001538702104100656,2.6263395352257448e-05,3.984691216726664e-06,5.441028279751516e-07,6.754210764707495e-08,7.685633545018012e-09,8.072770972664684e-10,7.873737040301298e-11],[0.06184683409317135,0.08445080308894831,0.05553451337145986,0.024983023388911414,0.008528473687129686,0.002329097236945195,0.0005300571296178651,0.00010339771731614888,1.7648478683157322e-05,2.6776331488807342e-06,3.6562626546074874e-07,4.5386951345666756e-08,5.164592695138727e-09,5.424741337293915e-10,5.2909944981885024e-11],[0.027706560619811665,0.03783283864863299,0.02583004978232529,0.011323825569080454,0.0038206429912152487,0.0010434046419844627,0.00023745855724153012,4.6320804690734175e-05,7.906284155882792e-06,1.199544103507677e-06,1.6379571301778394e-07,2.0332751663775206e-08,2.3136689643471487e-09,2.430212102402945e-10,2.3702952940534698e-11],[0.009309128502311536,0.012711457095670965,0.00867863954477381,0.0039501783722215135,0.0012988108200743405,0.00035057357083853553,7.97837109292539e-05,1.5563329173675347e-05,2.6564327558677294e-06,4.030348752763727e-07,5.503372870900414e-08,6.831602111895717e-09,7.773697355101037e-10,8.165270695116498e-11,7.963956184799834e-12],[0.0025022195908526476,0.00341673841597233,0.0023327491811386304,0.001061776481856573,0.00036245944480627106,9.534075768589095e-05,2.14452259917276e-05,4.183298914349409e-06,7.140279653314936e-07,1.083325641560301e-07,1.479262791346647e-08,1.8362802315008493e-09,2.0895079287457737e-10,2.1947597235189357e-11,2.1406479866885566e-12],[0.000560480579115802,0.0007653267255488258,0.0005225203322506828,0.0002378308840750963,8.11885097030136e-05,2.2172306623440916e-05,4.860140316876496e-06,9.370311889094057e-07,1.5993752465885818e-07,2.4265775280970194e-08,3.313450462099155e-09,4.1131458299380846e-10,4.6803590630166134e-11,4.916116096904025e-12,4.794909398233274e-13],[0.00010760908231157628,0.00014693837694564795,0.00010032093088995067,4.566217659324861e-05,1.558773193741778e-05,4.25695672139676e-06,9.68800368167771e-07,1.8202265201372802e-07,3.070709476299069e-08,4.658890792761307e-09,6.361636367023692e-10,7.897005974258303e-11,8.986023109925223e-12,9.438663201489963e-13,9.205953236150015e-14],[1.807779011260571e-05,2.4684915816112344e-05,1.6853416956745585e-05,7.671018345341688e-06,2.6186613642916e-06,7.151475365716227e-07,1.6275363882429486e-07,3.174819052327648e-08,5.2193710617456564e-09,7.826704595921428e-10,1.068723239203778e-10,1.326657689610993e-11,1.5096071468939288e-12,1.5856484288757354e-13,1.5465543132104184e-14],[2.6995366589693927e-06,3.6861715261702166e-06,2.516702352457686e-06,1.1455047937765757e-06,3.910418422992209e-07,1.0679220079010423e-07,2.4303823180272527e-08,4.740922626033081e-09,8.092061805215045e-10,1.1825128374210545e-10,1.5959127440645267e-11,1.981083442555967e-12,2.2542798695514632e-13,2.367831485665081e-14,2.3094526695978888e-15],[3.6280697557353674e-07,4.954067722739036e-07,3.382347729489866e-07,1.5395128210399285e-07,5.255446621030413e-08,1.4352446466976786e-08,3.266337041066522e-09,6.371611193588588e-10,1.087540878524329e-10,1.6500206954827752e-11,2.1700941382395286e-12,2.6624972465717124e-13,3.0296623639128974e-14,3.1822712135715525e-15,3.1038124098189566e-16],[4.432710233893149e-08,6.052790649702937e-08,4.1324914912106154e-08,1.8809490160009927e-08,6.421009955471177e-09,1.7535560399575746e-09,3.990751723114312e-10,7.784719712061777e-11,1.3287378431440404e-11,2.0159655451606697e-12,2.7527667630001744e-13,3.2912882038838065e-14,3.701586868479485e-15,3.888041610314367e-16,3.7921820580597954e-17],[4.96448834472274e-09,6.7789246415743364e-09,4.6282533168793465e-09,2.1066004710967372e-09,7.191318043202763e-10,1.9639245659740974e-10,4.4695094808132145e-11,8.718627710415696e-12,1.488142284835763e-12,2.257814502691452e-13,3.0830074129731475e-14,3.827085761319956e-15,4.1944607118753164e-16,4.3544775633236186e-17,4.247118046281559e-18],[5.132365088922522e-10,7.008157488744355e-10,4.784760099495822e-10,2.1778362569140968e-10,7.434496186803672e-11,2.0303356921760895e-11,4.6206482584088115e-12,9.013452621319245e-13,1.5384645868207839e-13,2.3341636692922365e-14,3.1872609051550544e-15,3.9565006481665913e-16,4.502112113724001e-17,4.554724739764099e-18,4.390736542354734e-19],[4.9269244812924385e-11,6.727631823108746e-11,4.5932335800114165e-11,2.0906608521665e-11,7.136904844882762e-12,1.949064506072439e-12,4.4356908811752135e-13,8.652658104310802e-14,1.476882237541695e-14,2.2407307208914182e-15,3.059679798650387e-16,3.79812806882641e-17,4.321899554360577e-18,4.539600420037037e-19,4.2646046321210616e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1883349337454977, "-10": 4.778080961287411e-07, "-11": 5.850784425096962e-08, "-12": 6.578833843176716e-09, "-13": 6.79407772225405e-10, "-14": 5.858608906230987e-11, "-2": 0.10761093278697077, "-3": 0.042937600936279775, "-4": 0.013488570041832694, "-5": 0.0034794823703163907, "-6": 0.0007596964606493471, "-7": 0.0001436020261645017, "-8": 2.3913245893432463e-05, "-9": 3.55677511272424e-06, "0": 0.27861837523726585, "1": 0.1945291531552689, "10": 4.2818805591798176e-07, "11": 5.160540959897708e-08, "12": 5.711236429397289e-09, "13": 5.805128271233396e-10, "14": 4.9269244812924385e-11, "2": 0.10950570184022188, "3": 0.04300492561467103, "4": 0.013296778226388908, "5": 0.0033759440678754193, "6": 0.0007254722314454312, "7": 0.00013497127387183722, "8": 2.2121745780615252e-05, "9": 3.2384512406528732e-06} |
| Raw goal margin distribution | {"-1": 0.19072146607671722, "-10": 6.367674802057347e-07, "-11": 8.067956839435443e-08, "-12": 9.387587481739227e-09, "-13": 1.0024137694405444e-09, "-14": 8.877935952515182e-11, "-2": 0.11124626555009108, "-3": 0.04559778337907483, "-4": 0.014755310745831344, "-5": 0.003927076732837975, "-6": 0.0008855262901003898, "-7": 0.00017298795349278106, "-8": 2.978426500620461e-05, "-9": 4.581852700735733e-06, "0": 0.2754171222012744, "1": 0.1875343937338929, "10": 5.432275159401439e-07, "11": 6.774301768449182e-08, "12": 7.758094372063021e-09, "13": 8.153576928025084e-10, "14": 7.107440709389791e-11, "2": 0.10776695647683528, "3": 0.04347544102765894, "4": 0.013846777503790713, "5": 0.003627186023349199, "6": 0.0008050113245202546, "7": 0.000154780583584087, "8": 2.6229354012063525e-05, "9": 3.971384340148088e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 27.5% |
| Unadjusted away-win probability | 36.7% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 58.0% |
| P home draw | 64.3% |
| P draw away | 63.5% |
| P home away | 72.1% |
| Raw p home draw | 63.3% |
| Raw p draw away | 64.3% |
| Raw p home away | 72.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9655 |
| Totals anchor target over 2 5 | 0.5096 |
| Totals anchor reference over odds | 1.89 |
| Totals anchor reference under odds | 1.96 |
| Totals anchor reference last update utc | 2026-11-05T16:49:14Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5308 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.88, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.74, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.37, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.74, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.79, "draw": 3.46, "home": 2.61}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.93, "under": 1.95}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.53, "home_away": 1.34, "home_draw": 1.48}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.72, "draw": 3.39, "home": 2.61}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.89, "under": 1.96}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.89, "under": 1.96}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.27, "under": 3.79}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.61 |
| Reference draw odds | 3.39 |
| Reference away odds | 2.72 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:14Z |
| Market reference home last update utc | 2026-11-05T16:49:14Z |
| Market reference draw last update utc | 2026-11-05T16:49:14Z |
| Market reference away last update utc | 2026-11-05T16:49:14Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:14Z |
| Market best over 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market best under 2 5 last update utc | 2026-11-05T16:49:14Z |
| Home probability edge | -0.3% |
| Draw probability edge | -0.1% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0105 |
| Raw ev home | -0.0676 |
| Raw edge prob draw | -0.0046 |
| Raw ev draw | -0.0471 |
| Raw edge prob away | 0.0151 |
| Raw ev away | 0.0249 |
| Market p home draw | 65.4% |
| Market home draw odds | 1.48 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T16:49:11Z |
| Market reference home draw last update utc | 2026-11-05T16:49:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.7% |
| Market draw away odds | 1.53 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T16:49:11Z |
| Market reference draw away last update utc | 2026-11-05T16:49:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T16:49:11Z |
| Market reference home away last update utc | 2026-11-05T16:49:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.49 |
| Market reference dc home draw odds | 1.43 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 76.9% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.79 |
| Market reference over 1 5 last update utc | 2026-11-05T16:49:14Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.6% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.18 |
| Market reference under 3 5 last update utc | 2026-11-05T16:49:14Z |
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
| Team research json | {"base_rates": [1.39197981946836, 1.4142716984469377], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:21.943935+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-05T16:50:21.944578+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:21.945206+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Gazi%C5%9Fehir+Gaziantep%22+%22Kasimpasa+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:22.144132+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Gazi%C5%9Fehir+Gaziantep_vs_Kasimpasa+SK&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.39197981946836, 1.4142716984469377], "h2h": [], "margin_distribution": {"-1": 0.2021985773245488, "-10": 6.367674802057347e-07, "-11": 8.067956839435443e-08, "-12": 9.387587481739227e-09, "-13": 1.0024137694405444e-09, "-14": 8.877935952515182e-11, "-2": 0.11124626555009108, "-3": 0.04559778337907483, "-4": 0.014755310745831344, "-5": 0.003927076732837975, "-6": 0.0008855262901003898, "-7": 0.00017298795349278106, "-8": 2.978426500620461e-05, "-9": 4.581852700735733e-06, "0": 0.2524628997056113, "1": 0.19901150498172446, "10": 5.432275159401439e-07, "11": 6.774301768449182e-08, "12": 7.758094372063021e-09, "13": 8.153576928025084e-10, "14": 7.107440709389791e-11, "2": 0.10776695647683528, "3": 0.04347544102765894, "4": 0.013846777503790713, "5": 0.003627186023349199, "6": 0.0008050113245202546, "7": 0.000154780583584087, "8": 2.6229354012063525e-05, "9": 3.971384340148088e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:22.144401+00:00", "p_over_1_5": 0.7699840596468466, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Eyüpspor vs Kocaelispor

The model's most likely 1X2 outcome is **Kocaelispor win** at **44.8%**. Expected goals are 0.80 for Eyüpspor and 0.87 for Kocaelispor (1.67 combined). The most likely exact score is 1-1 at 14.4%. Goal-market probabilities: at least one goal: 89.2%; Over 2.5 goals: 41.9%; Under 3.5 goals: 78.7%; Double Chance 1X: 55.2%; Double Chance X2: 75.3%; Double Chance 12 (either team wins): 69.5%; Under 4.5 goals: 90.9%; BTTS Yes (both teams score): 49.0%; BTTS No (at least one team does not score): 51.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eyüpspor win | 24.7% | 4.04 |
| Draw | 30.5% | 3.28 |
| Kocaelispor win | 44.8% | 2.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eyüpspor expected goals | 0.80 |
| Kocaelispor expected goals | 0.87 |
| Expected total goals | 1.67 |
| Over 0.5 | 89.2% |
| Under 0.5 | 10.8% |
| Over 1.5 | 69.5% |
| Under 1.5 | 30.5% |
| Over 2.5 | 41.9% |
| Under 2.5 | 58.1% |
| Over 3.5 | 21.3% |
| Under 3.5 | 78.7% |
| Over 4.5 | 9.1% |
| Under 4.5 | 90.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.40% |
| 2 | 0-1 | 12.49% |
| 3 | 0-0 | 10.75% |
| 4 | 1-2 | 9.70% |
| 5 | 0-2 | 8.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eyüpspor win | 24.7% | 22.7% | 4.11 | +1.7% |
| Draw | 30.5% | 27.7% | 3.50 | +6.6% |
| Kocaelispor win | 44.8% | 49.6% | 2.00 | -10.4% |
| Over 2.5 | 41.9% | 43.7% | 2.20 | -7.8% |
| Under 2.5 | 58.1% | 56.3% | 1.73 | +0.5% |

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
| Market best home last update utc | 2026-11-05T16:49:14Z |
| Market best draw last update utc | 2026-11-05T16:49:11Z |
| Market best away last update utc | 2026-11-05T16:49:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Eyupspor |
| Matched away-team name | Kocaelispor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7985 |
| Dc lambda away | 0.8688 |
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
| P btts yes | 49.0% |
| P btts no | 51.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.30 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.28 |
| Fair Over 2.5 odds | 2.39 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.70 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.02 |
| Fair Under 4.5 odds | 1.10 |
| Score matrix json | [[0.10752276968966956,0.12488790925611429,0.08601481725725088,0.035195839422927436,0.010801166172739282,0.0026517950440500945,0.0005425353185008024,9.514134504513286e-05,1.4598848821048105e-05,1.991202427865761e-06,2.4443012196412714e-07,2.727729814603263e-08,2.790354720419262e-09,2.634846837694261e-10,2.3102908103647703e-11],[0.07216446586947194,0.14402972030564132,0.09703966118129043,0.03970702306298361,0.012185592426833633,0.0029916856281544195,0.0006120741189130791,0.00010733597049796272,1.6470038400412536e-05,2.2464223619235525e-06,2.757596536764238e-07,3.077353244982814e-08,3.148005021451972e-09,2.9725651061926983e-10,2.6064095073008758e-11],[0.04617537650546158,0.05668259918237897,0.04547884703576238,0.022398211072318472,0.006873732910788418,0.0016875706359334736,0.0003452629849780627,6.054681357129342e-05,9.290532706933963e-06,1.2671773993262733e-06,1.5555240488506862e-07,1.7358946153146842e-08,1.7757483560365797e-09,1.6767850002026807e-10,1.4702414278910177e-11],[0.01736461629088594,0.021315940651954992,0.01308319510970563,0.006998133909595644,0.0025849217378391626,0.0006346243122302443,0.00012983888183090069,2.2769109098156685e-05,3.4937784551632747e-06,4.76532103840688e-07,5.849671466423804e-08,6.52796927660985e-09,6.677842427142865e-10,6.305682884337447e-11,5.528959411359014e-12],[0.004897576182633347,0.006012021313838913,0.003690029407426096,0.0015098989526563323,0.0006057278997243147,0.00017899162667534747,3.662020539829167e-05,6.4218779471356236e-06,9.853973081101798e-07,1.344027557496487e-07,1.6498614867305788e-08,1.841170937181444e-09,1.8834416767227476e-10,1.778476517547869e-11,1.559406754183847e-12],[0.0011050634030899704,0.0013565209574643257,0.0008325988820616624,0.0003406856805741907,0.0001045522058541242,3.355466295391354e-05,8.262791080777248e-06,1.448998858589354e-06,2.2233988039986618e-07,3.0325932893098604e-08,3.7226609268858088e-09,4.1543215371038905e-10,4.249699016793296e-11,4.012861136833449e-12,3.518563612528284e-13],[0.00020778392537295604,0.0002550652284787229,0.00015655270411830114,6.405877511654323e-05,1.9658842812119236e-05,4.826443840157734e-06,1.2908200182503732e-06,2.724537522976101e-07,4.180633707283892e-08,5.7021537040366965e-09,6.999680724725655e-10,7.811327692394677e-11,7.99066497808009e-12,7.545341169170464e-13,6.615918661691956e-14],[3.3488053670046104e-05,4.110827170738288e-05,2.523123647940703e-05,1.0324204316044851e-05,3.1683701325864654e-06,7.778667674342736e-07,1.5914510262323685e-07,3.648252793673635e-08,6.737830451178326e-09,9.190028965565332e-10,1.1281223191931712e-10,1.2589335798123145e-11,1.2878369544949026e-12,1.216065148343165e-13,1.0662722769421509e-14],[4.722542995184066e-06,5.797159264871575e-06,3.5581524166702125e-06,1.455937070991907e-06,4.4680901205017747e-07,1.0969611103493385e-07,2.2442916420773332e-08,3.935687101271576e-09,7.894420608846924e-10,1.2959937100103633e-10,1.590897520861856e-11,1.7753698131649165e-12,1.8161298498601902e-13,1.7149160129100985e-14,1.50367552621794e-15],[5.919832403812533e-07,7.266892286898322e-07,4.460238052970277e-07,1.8250555811898692e-07,5.6008690033048866e-08,1.3750697311576483e-08,2.8132788626643743e-09,4.933487753766105e-10,7.570130719043062e-11,1.3497413549922699e-11,1.994232070464394e-12,2.2254729622243795e-13,2.2765667450137227e-14,2.1496925265466028e-15,1.8848969959622097e-16],[6.678599676587299e-08,8.19831731145252e-08,5.0319236062975845e-08,2.05897984653055e-08,6.318753532615111e-09,1.5513176109310132e-09,3.1738674375713244e-10,5.565831508258545e-11,8.540422958488475e-12,1.1648665684806942e-12,1.869243445049212e-13,2.5107202352879645e-14,2.5683629011500524e-15,2.4252267350187175e-16,2.126491361398385e-17],[6.849655468960116e-09,8.408296907736827e-09,5.160803868825095e-09,2.1117155166086097e-09,6.480592757103908e-10,1.591050769977807e-10,3.2551581924766206e-11,5.708386499568528e-12,8.759164743758909e-13,1.1947017410511646e-13,1.466556529809425e-14,2.1394188003366765e-15,2.634145156777278e-16,2.4873429122012896e-17,2.1809561717497406e-18],[6.439668062543713e-10,7.905016727119883e-10,4.851902990117897e-10,1.9853183902616e-10,6.092695668182247e-11,1.4958181292098105e-11,3.0603200913697323e-12,5.366709960305186e-13,8.234883303335906e-14,1.1231926453784898e-14,1.3787755150205328e-15,1.5386512307670632e-16,2.0575416140290078e-17,2.3384625379893515e-18,2.0504146330671718e-19],[5.588511257402366e-11,6.86017890058966e-11,4.2106074749119125e-11,1.7229108807701967e-11,5.287399598685759e-12,1.2981098362410864e-12,2.655825287230524e-13,4.6573703391370025e-14,7.146445685883532e-15,9.747357599748374e-16,1.196537214696023e-16,1.3352815146439652e-17,1.3659377323693215e-18,1.6860763427027013e-19,1.7794030915798696e-20],[4.503437034111985e-12,5.528195667607788e-12,3.393069238880089e-12,1.3883877672533355e-12,4.2607896933786015e-13,1.0460667683418875e-13,2.1401660305869027e-14,3.753087915688197e-15,5.758880439123816e-16,7.854795164149604e-17,9.64215648347813e-18,1.0760211346175023e-18,1.1007250924107878e-19,1.0393811251615757e-20,1.1913420617596445e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.24709823698852018, "-10": 2.770440190055894e-07, "-11": 3.0598510626916227e-08, "-12": 3.1023136453174424e-09, "-13": 2.8954877884243486e-10, "-14": 2.3102908103647703e-11, "-2": 0.1332683094889841, "-3": 0.049205491402117295, "-4": 0.014161900330952116, "-5": 0.0033280479598247585, "-6": 0.0006596552759703359, "-7": 0.0001129389419926601, "-8": 1.7007543980321334e-05, "-9": 2.2850069485595825e-06, "0": 0.30467008160902187, "1": 0.14354970092157787, "10": 7.569713916039864e-08, "11": 7.683651604188476e-09, "12": 7.159616644991479e-10, "13": 6.141330824163145e-11, "14": 4.503437034111985e-12, "2": 0.0715424918999229, "3": 0.024276576197971123, "4": 0.006421434931419843, "5": 0.001386873398222214, "6": 0.0002526393360212074, "7": 3.975248982547263e-05, "8": 5.50172542192166e-06, "9": 6.793311412099052e-07} |
| Raw goal margin distribution | {"-1": 0.21521683435336822, "-10": 1.3576057838536745e-08, "-11": 1.0651686081637672e-09, "-12": 7.290583215929698e-11, "-2": 0.08921218872896917, "-3": 0.024468503133877755, "-4": 0.005140390730882469, "-5": 0.0008733512925463727, "-6": 0.00012443489198252285, "-7": 1.5257424753265129e-05, "-8": 1.641315622800353e-06, "-9": 1.5724221679139576e-07, "0": 0.36950523405613633, "1": 0.19677121734491226, "10": 5.83633982737081e-09, "11": 4.2084477504963786e-10, "12": 2.647296231733534e-11, "2": 0.07535248389042594, "3": 0.01899404530720425, "4": 0.0036672700230577127, "5": 0.0005726277799574657, "6": 7.498291332647313e-05, "7": 8.449637176645524e-06, "8": 8.353829683189089e-07, "9": 7.355282545683872e-08} |
| Research history json | {"away": [{"away": "Rizespor", "away_goals": 0.0, "away_xg": 1.17, "date": "2026-10-31T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 0.0, "home_xg": 0.62, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.83, "date": "2026-10-18T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.61, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 1.0, "away_xg": 1.65, "date": "2026-10-11T00:00:00+00:00", "home": "Besiktas", "home_goals": 2.0, "home_xg": 2.21, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.88, "date": "2026-09-19T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.16, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 0.77, "date": "2026-08-29T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 0.0, "away_xg": 0.59, "date": "2026-08-24T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.3, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.44, "date": "2026-08-16T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.96, "source": "pipeline training history"}], "h2h": [{"away": "Kocaelispor", "away_goals": 1.0, "away_xg": null, "date": "2026-03-09T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Eyupspor", "away_goals": 1.0, "away_xg": 0.98, "date": "2026-11-01T00:00:00+00:00", "home": "Amedspor", "home_goals": 5.0, "home_xg": 4.95, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.59, "date": "2026-10-24T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-10-17T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 4.0, "away_xg": 3.21, "date": "2026-10-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Rizespor", "away_goals": 2.0, "away_xg": 2.05, "date": "2026-09-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-06T00:00:00+00:00", "home": "Corum", "home_goals": 3.0, "home_xg": 2.58, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 1.0, "away_xg": 1.16, "date": "2026-08-23T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.09, "date": "2026-08-16T00:00:00+00:00", "home": "Besiktas", "home_goals": 1.0, "home_xg": 1.29, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 37.0% |
| Unadjusted away-win probability | 33.5% |
| Raw p over 1 5 | 50.9% |
| Raw p under 3 5 | 91.2% |
| Raw p btts yes | 33.2% |
| P home draw | 55.2% |
| P draw away | 75.3% |
| P home away | 69.5% |
| Raw p home draw | 66.5% |
| Raw p draw away | 70.5% |
| Raw p home away | 63.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.4129 |
| Totals anchor target over 2 5 | 0.4192 |
| Totals anchor reference over odds | 2.25 |
| Totals anchor reference under odds | 1.66 |
| Totals anchor reference last update utc | 2026-11-05T16:49:14Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.2520 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.94, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.05, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.0, "draw": 3.5, "home": 4.07}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.2, "under": 1.73}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.26, "home_away": 1.33, "home_draw": 1.86}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.95, "draw": 3.4, "home": 4.11}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.25, "under": 1.66}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.39, "under": 2.98}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.11 |
| Reference draw odds | 3.40 |
| Reference away odds | 1.95 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:14Z |
| Market reference home last update utc | 2026-11-05T16:49:14Z |
| Market reference draw last update utc | 2026-11-05T16:49:14Z |
| Market reference away last update utc | 2026-11-05T16:49:14Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market best over 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market best under 2 5 last update utc | 2026-11-05T16:49:11Z |
| Home probability edge | +2.1% |
| Draw probability edge | +2.8% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | 0.0685 |
| Raw ev home | 0.2143 |
| Raw edge prob draw | 0.0926 |
| Raw ev draw | 0.2933 |
| Raw edge prob away | -0.1611 |
| Raw ev away | -0.3299 |
| Market p home draw | 51.6% |
| Market home draw odds | 1.86 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T16:49:11Z |
| Market reference home draw last update utc | 2026-11-05T16:49:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 76.0% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T16:49:11Z |
| Market reference draw away last update utc | 2026-11-05T16:49:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.4% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T16:49:11Z |
| Market reference home away last update utc | 2026-11-05T16:49:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.23 |
| Market reference dc home draw odds | 1.81 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 69.7% |
| Market over 1 5 odds | 1.39 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference over 1 5 odds | 1.39 |
| Market reference over 1 5 opposite odds | 2.98 |
| Market reference over 1 5 last update utc | 2026-11-05T16:49:14Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 79.3% |
| Market under 3 5 odds | 1.23 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference under 3 5 odds | 1.23 |
| Market reference under 3 5 opposite odds | 4.08 |
| Market reference under 3 5 last update utc | 2026-11-05T16:49:14Z |
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
| Team research json | {"base_rates": [0.7984921087354108, 0.8688282614782472], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:22.148024+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-05T16:50:21.944578+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:22.148752+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Ey%C3%BCpspor%22+%22Kocaelispor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:22.185249+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Ey%C3%BCpspor_vs_Kocaelispor&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 0.890448735118826, "goals_for": 1.0632630221502812, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.513167850691485, "results": "DWLLWLWWWL", "xg_against": 1.2372826932614873, "xg_for": 1.1882938425185394, "xg_matches": 10}, "venue": {"goals_against": 1.3740829150788851, "goals_for": 1.0848014184490722, "last_match": "2026-10-23T00:00:00+00:00", "matches": 5, "points_per_game": 1.2891252875508328, "results": "WLLWL", "xg_against": 1.5093258702129508, "xg_for": 1.1284305210338508, "xg_matches": 5}}, "home": {"all": {"goals_against": 3.0933035323073734, "goals_for": 0.3034050194301704, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.19620865573750387, "results": "LLLLLLLWLL", "xg_against": 2.5307266426055373, "xg_for": 0.8256655613941696, "xg_matches": 10}, "venue": {"goals_against": 1.8723623359830541, "goals_for": 0.3416191115517185, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.5124286673275777, "results": "LLLWL", "xg_against": 1.563686916043823, "xg_for": 1.0291416727227958, "xg_matches": 5}}}, "goal_rates": [0.9554059963128982, 1.0279050804984438], "h2h": [{"away": "Kocaelispor", "away_goals": 1.0, "away_xg": null, "date": "2026-03-09T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.2232574100246142, "-10": 5.4582791480456135e-08, "-11": 5.0627690785528425e-09, "-12": 4.2991851313308324e-10, "-13": 3.160587301156459e-11, "-2": 0.09961969740349591, "-3": 0.031659871649295145, "-4": 0.007766308940409401, "-5": 0.0015470984694525823, "-6": 0.0002590899264392646, "-7": 3.739857011932091e-05, "-8": 4.7412941413801506e-06, "-9": 5.357168215855907e-07, "0": 0.30978995270689563, "1": 0.20751086097888655, "10": 2.6266683638917413e-08, "11": 2.2645012760742725e-09, "12": 1.7873333047427394e-10, "13": 1.2212993945329503e-11, "2": 0.08606273002549343, "3": 0.025422250871278838, "4": 0.005796348149859218, "5": 0.0010732297599101081, "6": 0.00016705528827508432, "7": 2.241298231304597e-05, "8": 2.641049247806195e-06, "9": 2.773638354188311e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:22.185474+00:00", "p_over_1_5": 0.5894581036313666, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Galatasaray vs Amed SK

The model's most likely 1X2 outcome is **Galatasaray win** at **64.6%**. Expected goals are 2.21 for Galatasaray and 1.53 for Amed SK (3.74 combined). The most likely exact score is 2-1 at 11.9%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 67.6%; Under 3.5 goals: 55.3%; Double Chance 1X: 83.3%; Double Chance X2: 35.4%; Double Chance 12 (either team wins): 81.3%; Under 4.5 goals: 73.5%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 64.6% | 1.55 |
| Draw | 18.7% | 5.35 |
| Amed SK win | 16.7% | 5.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 2.21 |
| Amed SK expected goals | 1.53 |
| Expected total goals | 3.74 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 86.6% |
| Under 1.5 | 13.4% |
| Over 2.5 | 67.6% |
| Under 2.5 | 32.4% |
| Over 3.5 | 44.7% |
| Under 3.5 | 55.3% |
| Over 4.5 | 26.5% |
| Under 4.5 | 73.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.91% |
| 2 | 2-0 | 8.64% |
| 3 | 1-1 | 8.21% |
| 4 | 3-1 | 7.93% |
| 5 | 1-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 64.6% | 69.8% | 1.45 | -6.3% |
| Draw | 18.7% | 17.3% | 5.15 | -3.7% |
| Amed SK win | 16.7% | 12.9% | 6.79 | +13.4% |

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
| Market best home last update utc | 2026-11-05T16:49:11Z |
| Market best draw last update utc | 2026-11-05T16:49:11Z |
| Market best away last update utc | 2026-11-05T16:49:14Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Galatasaray |
| Matched away-team name | Amedspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2145 |
| Dc lambda away | 1.5273 |
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
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.06 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.45 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.09 |
| Fair Over 3.5 odds | 2.24 |
| Fair Under 3.5 odds | 1.81 |
| Fair Over 4.5 odds | 3.78 |
| Fair Under 4.5 odds | 1.36 |
| Score matrix json | [[0.03441323785580085,0.024884951780639052,0.02124780569799958,0.009762805715090401,0.0033643135949648394,0.0009274879616026812,0.00021307811500424005,4.195875770133761e-05,7.229602999486634e-06,1.107270565321921e-06,1.5262847689200139e-07,1.9126024173110002e-08,2.1969757813835764e-09,2.3295054578552887e-10,2.2935991119535702e-11,2.1076964686678007e-12,1.815807896452848e-13,1.4723219750694042e-14],[0.0749368018220116,0.08212524926090757,0.04246610852918671,0.019512055641840966,0.006723955794806892,0.0018536880935729647,0.00042586036815163864,8.385925509769724e-05,1.4449167597011564e-05,2.2130036704242625e-06,3.050450270707443e-07,3.822549160187421e-08,4.390901032054025e-09,4.6557763657415683e-10,4.584013530387118e-11,4.212466372160825e-12,3.629094518978051e-13,2.942599611078441e-14],[0.08637035480832125,0.11905469282643871,0.05158565055077081,0.019498509264699246,0.006719287642831895,0.0018524011580250356,0.00042556471169890057,8.380103524033167e-05,1.4439136164278597e-05,2.211467277596882e-06,3.0483324748904584e-07,3.819895329472854e-08,4.3878526191925625e-09,4.6525440613808435e-10,4.5808310478622013e-11,4.2095418387737985e-12,3.6265749954619537e-13,2.940556691314351e-14],[0.057540261068618606,0.07931469219827125,0.05466451039390062,0.015790525982987615,0.004476415154502073,0.001234076743960567,0.0002835128403384418,5.58285705349983e-05,9.619407797290621e-06,1.4732879676137703e-06,2.0308107662450678e-07,2.544828894132188e-08,2.9232042151416194e-09,3.0995426673795814e-10,3.05176718319826e-11,2.8044128905092897e-12,2.4160381474281115e-13,1.9590101265741203e-14],[0.028750156675799044,0.03962981371728106,0.027313279593158064,0.012549730823971641,0.0027188597669787593,0.0006166099889000386,0.00014165800481180692,2.7894905585377683e-05,4.806364729049495e-06,7.361325637183508e-07,1.0147004310393705e-07,1.27153106469486e-08,1.4605873803814386e-09,1.5486953944164016e-10,1.5248242365529166e-11,1.4012329539072114e-12,1.2071803982681e-13,9.788250352447527e-15],[0.011492078673710295,0.015840920179987842,0.010917726865323062,0.00501640723524721,0.0017286800077702762,0.0002996104754138277,5.662386311196934e-05,1.1150215743092868e-05,1.9212111510779417e-06,2.9424859947467497e-07,4.055983873495917e-08,5.082593182471352e-09,5.838293430693248e-10,6.19048080848465e-11,6.095062467884562e-12,5.601040553651033e-13,4.8253692203130806e-14,3.912581917266131e-15],[0.0038280334066816044,0.0052766408378574345,0.003636715719767052,0.0016709748534853896,0.000575826619978294,0.00015874627704133847,2.292792155514757e-05,3.7141582100295553e-06,6.399591123962558e-07,9.80147717953855e-08,1.3510559930487678e-08,1.6930215192123207e-09,1.944746718609778e-10,2.0620610083806307e-11,2.0302769764575936e-12,1.8657173310694217e-13,1.6073397249871018e-14,1.3032885268995057e-15],[0.0010929645052833322,0.0015065649983201318,0.0010383402586230136,0.0004770899336700723,0.00016440767098193092,4.532459038868791e-05,1.0412726292072443e-05,1.2890768268682328e-06,1.8271851898180445e-07,2.7984778392690884e-08,3.857480037857591e-09,4.83384607864222e-10,5.5525616142657427e-11,5.8875125957756336e-12,5.796764122509864e-13,5.326920126119045e-14,4.589210909905974e-15,3.7210963142533485e-16],[0.0002730514268132203,0.0003763797638346253,0.0002594048459616941,0.00011918967768588933,4.107338245995217e-05,1.132328087099933e-05,2.6013742965320355e-06,5.122554880706696e-07,5.548927130249966e-08,6.991337442559629e-09,9.637004890359936e-10,1.207622537043497e-10,1.3871766776639709e-11,1.4708562875430265e-12,1.4481849199125508e-13,1.3308054689111833e-14,1.146506204766257e-15,9.296282294665171e-17],[6.063596866795101e-05,8.358187991721628e-05,5.76055005301528e-05,2.6468206542822753e-05,9.121081552274988e-06,2.5145376903010617e-06,5.776818388355424e-07,1.1375552249315399e-07,1.960037216732129e-08,1.88727069753376e-09,2.140069852059324e-10,2.681742526435157e-11,3.0804747129661385e-12,3.2663003012808117e-13,3.2159544615485225e-14,2.9552923292810782e-15,2.546022744549609e-16,2.0644062861218234e-17],[1.2118774346981116e-05,1.670477052589065e-05,1.151310150403858e-05,5.289966162135318e-06,1.8229498358926448e-06,5.025583910865128e-07,1.154561558591428e-07,2.2735309389822807e-08,3.917352895166381e-09,5.999734086511183e-10,5.199294183817036e-11,5.359761416947266e-12,6.156672144952404e-13,6.528065300228376e-14,6.4274435266460935e-15,5.906481195022334e-16,5.088510301936749e-17,4.125946116075319e-18],[2.201883782834255e-06,3.035122386455602e-06,2.091837900932798e-06,9.611442849457213e-07,3.312153164707024e-07,9.131081572917679e-08,2.0977454479788967e-08,4.130822772159353e-09,7.117514993299934e-10,1.090103405522833e-10,1.5026211989240516e-11,1.1837751393940978e-12,1.1186177879098026e-13,1.1860969357381077e-14,1.167814769150359e-15,1.0731601055163563e-16,9.245413762003618e-18,7.496512090843025e-19],[3.667258516773927e-07,5.055025386877271e-07,3.483976047106275e-07,1.6007950066641225e-07,5.5164227997976375e-08,1.5207903762539527e-08,3.493815123258679e-09,6.879924867326838e-10,1.1854289350297696e-10,1.8155776563838727e-11,2.5026299899198985e-12,3.1360701920276083e-13,2.2647325245782523e-14,1.975455799808875e-15,1.9450066763598156e-16,1.7873584280415722e-17,1.539832511785153e-18,1.2485512644021422e-19],[5.6380192271433515e-08,7.771562924880309e-08,5.356241958576646e-08,2.4610517597834692e-08,8.480912285854087e-09,2.3380531649339754e-09,5.37136848981813e-10,1.0577151435021557e-10,1.822470681447713e-11,2.7912571988704348e-12,3.847526957005027e-13,4.821373775382734e-14,5.538234879158041e-15,3.69181905277549e-16,2.9902405265624845e-17,2.74787314202216e-18,2.3673284193944165e-19,1.9195145372423636e-20],[8.048721420007678e-09,1.1094524949343746e-08,7.646461930315726e-09,3.513347368407822e-09,1.2107177649861617e-09,3.3377570794939675e-10,7.668056258236356e-11,1.5099725965435836e-11,2.6017220268573653e-12,3.9847419280054677e-13,5.492651121836257e-14,6.882895005565333e-15,7.906271317116169e-16,8.383206742910945e-17,5.189129745664875e-18,3.922807732045221e-19,3.379549836517132e-20,2.7402598589126646e-21],[1.0724178054000634e-09,1.4782430000068408e-09,1.0188204429588148e-09,4.6812109375161e-10,1.6131696212739474e-10,4.4472530919650477e-11,1.0216976877470572e-11,2.011899050418322e-12,3.4665543515614915e-13,5.309300658480443e-14,7.318450415323502e-15,9.170822011951796e-16,1.0534376446080434e-16,1.1169848859595633e-17,1.0997679931864592e-18,6.35363417564118e-20,4.502938081455413e-21,3.6511432198608813e-22],[1.3395915900694287e-10,1.8465208997061e-10,1.272641399933957e-10,5.84745121878897e-11,2.0150620841360545e-11,5.555206945379097e-12,1.2762354589858417e-12,2.5131278447989246e-13,4.330184590825594e-14,6.632018300551486e-15,9.141711914276002e-16,1.1455568883110133e-16,1.315882860461316e-17,1.3952617645208695e-18,1.3737555897354054e-19,1.2624088447748664e-20,6.837422781571427e-22,4.5607604861055605e-23],[1.5748959641299387e-11,2.1708693412131677e-11,1.4961857176460668e-11,6.874578336551177e-12,2.369015427763814e-12,6.531000241447253e-13,1.50041108688369e-13,2.954568339676771e-14,5.090798036195071e-15,7.796957619772082e-16,1.0747488492582777e-16,1.3467783266605611e-17,1.5470227057045633e-18,1.6403448171355324e-19,1.6150610006913393e-20,1.4841557751305622e-21,1.2786194863018148e-22,6.517856372599869e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.09200312266858617, "-10": 1.955676001717339e-07, "-11": 2.4014148073068728e-08, "-12": 2.7112907719486088e-09, "-13": 2.832516149932691e-10, "-14": 2.7530705092508465e-11, "-15": 2.5000114874787494e-12, "-16": 2.1100678575606923e-13, "-17": 1.4723219750694042e-14, "-2": 0.04886670288222433, "-3": 0.018652593621158255, "-4": 0.005704509592249698, "-5": 0.0014475472152451468, "-6": 0.000312956547380126, "-7": 5.883579400641386e-05, "-8": 9.774412783243059e-06, "-9": 1.4535989057583519e-06, "0": 0.1869574083209832, "1": 0.26310410734860534, "10": 1.5528161351822228e-05, "11": 2.7646291106863374e-06, "12": 4.5257686767112867e-07, "13": 6.855438119135174e-08, "14": 9.661103138344465e-09, "15": 1.272031752547134e-09, "16": 1.5566785241907456e-10, "17": 1.5748959641299387e-11, "2": 0.19863860420409868, "3": 0.1099351086040083, "4": 0.0487485901377429, "5": 0.01793589477189757, "6": 0.005622389320400256, "7": 0.001532586711620449, "8": 0.00036916513353712696, "9": 7.960148175681514e-05} |
| Raw goal margin distribution | {"-1": 0.13582023908983445, "-10": 6.114378068968513e-07, "-11": 8.28184192862626e-08, "-12": 1.0321070659578385e-08, "-13": 1.1907928257726664e-09, "-14": 1.27869542761578e-10, "-15": 1.2827495612292874e-11, "-16": 1.1912296447629034e-12, "-17": 8.926319996802402e-14, "-2": 0.07545070050349868, "-3": 0.03086727135498963, "-4": 0.01022138025008831, "-5": 0.002826170189601363, "-6": 0.0006685145316450627, "-7": 0.0001378944932085131, "-8": 2.518463839848767e-05, "-9": 4.123429741501299e-06, "0": 0.2188647407480338, "1": 0.20041063069584575, "10": 2.5108335773976204e-05, "11": 4.931046976900987e-06, "12": 8.910119282115764e-07, "13": 1.4905328095642555e-07, "14": 2.3207000243067748e-08, "15": 3.3755172619567025e-09, "16": 4.5450693588439355e-10, "17": 4.9381472725650214e-11, "2": 0.15861943698475126, "3": 0.09408880041896034, "4": 0.04517475444559616, "5": 0.018110528775130155, "6": 0.006211410551163789, "7": 0.001857688404745947, "8": 0.0004919355755893556, "9": 0.00011678247474426085} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Galatasaray", "away_goals": 4.0, "away_xg": 2.8, "date": "2026-10-30T00:00:00+00:00", "home": "Konyaspor", "home_goals": 0.0, "home_xg": 1.38, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 1.0, "away_xg": 1.92, "date": "2026-10-17T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 0.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.51, "date": "2026-10-09T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 3.0, "away_xg": 2.12, "date": "2026-09-04T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.63, "date": "2026-08-29T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.92, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 4.0, "away_xg": 3.08, "date": "2026-08-21T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 0.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 2.0, "away_xg": 0.61, "date": "2026-08-14T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 52.5% |
| Unadjusted draw probability | 21.9% |
| Unadjusted away-win probability | 25.6% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.5% |
| Raw p btts yes | 70.5% |
| P home draw | 83.3% |
| P draw away | 35.4% |
| P home away | 81.3% |
| Raw p home draw | 74.4% |
| Raw p draw away | 47.5% |
| Raw p home away | 78.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9025 |
| Totals anchor target over 2 5 | 0.6760 |
| Totals anchor reference over odds | 1.43 |
| Totals anchor reference under odds | 2.80 |
| Totals anchor reference last update utc | 2026-11-05T16:49:14Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7348 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.8, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.8, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.73, "draw": 5.15, "home": 1.45}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.87, "home_away": 1.19, "home_draw": 1.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.79, "draw": 5.15, "home": 1.4}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.43, "under": 2.8}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.13, "under": 5.88}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.40 |
| Reference draw odds | 5.15 |
| Reference away odds | 6.79 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:14Z |
| Market reference home last update utc | 2026-11-05T16:49:14Z |
| Market reference draw last update utc | 2026-11-05T16:49:14Z |
| Market reference away last update utc | 2026-11-05T16:49:14Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-11-05T16:48:47Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:48:47Z |
| Home probability edge | -5.2% |
| Draw probability edge | +1.4% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -0.7% |
| Under 2.5 probability edge | +0.7% |
| Raw edge prob home | -0.1727 |
| Raw ev home | -0.2386 |
| Raw edge prob draw | 0.0456 |
| Raw ev draw | 0.1272 |
| Raw edge prob away | 0.1271 |
| Raw ev away | 0.7384 |
| Market p home draw | 85.5% |
| Market home draw odds | 1.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T16:49:11Z |
| Market reference home draw last update utc | 2026-11-05T16:49:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.5% |
| Market draw away odds | 2.87 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T16:49:11Z |
| Market reference draw away last update utc | 2026-11-05T16:49:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.0% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T16:49:11Z |
| Market reference home away last update utc | 2026-11-05T16:49:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.78 |
| Market reference dc home draw odds | 1.09 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 86.9% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 5.88 |
| Market reference over 1 5 last update utc | 2026-11-05T16:49:14Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.9% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.10 |
| Market reference under 3 5 last update utc | 2026-11-05T16:49:14Z |
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
| Team research json | {"base_rates": [2.2144985733729188, 1.5273157873643333], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:22.148024+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-05T16:50:21.944578+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:22.238850+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Galatasaray%22+%22Amed+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:22.275358+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Galatasaray_vs_Amed+SK&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 1.0408527377748258, "goals_for": 2.2981057758943, "last_match": "2026-10-30T00:00:00+00:00", "matches": 10, "points_per_game": 2.6034710533412406, "results": "WWWWLWWWWD", "xg_against": 1.1147534090307207, "xg_for": 2.2984475091718832, "xg_matches": 10}, "venue": {"goals_against": 1.1232992550353904, "goals_for": 2.1999854601202053, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 2.70260329000593, "results": "WWWWD", "xg_against": 0.5544118907898825, "xg_for": 2.502044081155706, "xg_matches": 5}}}, "goal_rates": [2.2144985733729188, 1.5273157873643333], "h2h": [], "margin_distribution": {"-1": 0.14355703725482025, "-10": 6.114378068968513e-07, "-11": 8.28184192862626e-08, "-12": 1.0321070659578385e-08, "-13": 1.1907928257726664e-09, "-14": 1.27869542761578e-10, "-15": 1.2827495612292874e-11, "-16": 1.1912296447629034e-12, "-17": 8.926319996802402e-14, "-2": 0.07545070050349868, "-3": 0.03086727135498963, "-4": 0.01022138025008831, "-5": 0.002826170189601363, "-6": 0.0006685145316450627, "-7": 0.0001378944932085131, "-8": 2.518463839848767e-05, "-9": 4.123429741501299e-06, "0": 0.20339114441806222, "1": 0.20814742886083154, "10": 2.5108335773976204e-05, "11": 4.931046976900987e-06, "12": 8.910119282115764e-07, "13": 1.4905328095642555e-07, "14": 2.3207000243067748e-08, "15": 3.3755172619567025e-09, "16": 4.5450693588439355e-10, "17": 4.9381472725650214e-11, "2": 0.15861943698475126, "3": 0.09408880041896034, "4": 0.04517475444559616, "5": 0.018110528775130155, "6": 0.006211410551163789, "7": 0.001857688404745947, "8": 0.0004919355755893556, "9": 0.00011678247474426085}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:22.275571+00:00", "p_over_1_5": 0.887566632501466, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Goztepe vs Basaksehir

The model's most likely 1X2 outcome is **Goztepe win** at **44.9%**. Expected goals are 1.52 for Goztepe and 1.35 for Basaksehir (2.87 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 59.1%; Under 3.5 goals: 63.4%; Double Chance 1X: 70.7%; Double Chance X2: 55.1%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 80.5%; BTTS Yes (both teams score): 62.1%; BTTS No (at least one team does not score): 37.9%.

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
| Over 1.5 | 82.0% |
| Under 1.5 | 18.0% |
| Over 2.5 | 59.1% |
| Under 2.5 | 40.9% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.5% |
| Under 4.5 | 80.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.88% |
| 2 | 2-1 | 9.74% |
| 3 | 1-0 | 7.21% |
| 4 | 1-2 | 6.98% |
| 5 | 2-0 | 6.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Goztepe win | 44.9% | 46.9% | 2.09 | -6.1% |
| Draw | 25.8% | 25.2% | 3.77 | -2.8% |
| Basaksehir win | 29.3% | 27.9% | 3.48 | +2.0% |
| Over 2.5 | 59.1% | 58.4% | 1.67 | -1.4% |
| Under 2.5 | 40.9% | 41.6% | 2.31 | -5.4% |

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
| Market best home last update utc | 2026-11-05T16:49:11Z |
| Market best draw last update utc | 2026-11-05T16:49:11Z |
| Market best away last update utc | 2026-11-05T16:49:11Z |
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
| Dc lambda home | 1.5170 |
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
| P btts yes | 62.1% |
| P btts no | 37.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.54 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.56 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.13 |
| Fair Under 4.5 odds | 1.24 |
| Score matrix json | [[0.05702056622369117,0.05065471223365904,0.0431749259530228,0.02070570950055276,0.007447489424552179,0.002142987613241105,0.0005138639847504664,0.00010561604737186613,1.8994142553868444e-05,3.036385813071309e-06,4.368544092846488e-07,5.713783864352722e-08,6.8505009697619695e-09,7.581563027906286e-10,7.791309993217133e-11,7.473069045854977e-12],[0.0720795879930658,0.11879791217691453,0.06981902320766699,0.03348361068929847,0.012043481847251623,0.003465467481413206,0.0008309795717059049,0.00017079379060387488,3.0715802065792045e-05,4.910199308295837e-06,7.064458703045237e-07,9.239872435748914e-08,1.1078080057679158e-08,1.2260294912184293e-09,1.259948086133241e-10,1.2084847156721445e-11],[0.06767369764991671,0.0973642844848454,0.06301918207549165,0.027073503198781282,0.009737875862361562,0.0028020378630581513,0.0006718967169180486,0.00013809700151972668,2.483556427643964e-05,3.970190010669551e-06,5.71203766132907e-07,7.470989860287986e-08,8.957290737279672e-09,9.913182201377988e-10,1.018743434116225e-10,9.771322190735215e-12],[0.03647882316315719,0.05248323409936173,0.03775464259371149,0.01629116678254194,0.005249103623766619,0.0015104102074004959,0.00036217913859461687,7.443979378606571e-05,1.3387360065415025e-05,2.140090823358844e-06,3.079016205481031e-07,4.0271616215952593e-08,4.828337096585607e-09,5.343600735088103e-10,5.491433580886796e-11,5.2671325292434695e-12],[0.014747655871998864,0.021217917915966947,0.015263444054980254,0.0073199995507631736,0.002368940453487655,0.0006106285245186916,0.00014642175478415598,3.0094514207032385e-05,5.412240915674142e-06,8.651957563585872e-07,1.244784438896136e-07,1.6281005960793052e-08,1.9519997565702127e-09,2.160310501409799e-10,2.2200763531387917e-11,2.1293959409289987e-12],[0.004769744961258866,0.006862382601443941,0.004936563207372369,0.0023674630922166737,0.0008515359660498755,0.00022046318266398524,4.735630076820815e-05,9.733286343700846e-06,1.7504482787444446e-06,2.798250200039821e-07,4.025930871191097e-08,5.2656670876869935e-09,6.313234512718107e-10,6.986961330185559e-11,7.180258402353455e-12,6.886976240783793e-13],[0.0012855414216850925,0.0018495490130522518,0.0013305022669742221,0.0006380785333545281,0.00022950593067408534,6.603948506170728e-05,1.424805257662085e-05,2.6233148450450646e-06,4.7178073190929004e-07,7.541842529543482e-08,1.0850686855992713e-08,1.4192023282181844e-09,1.701542647841911e-10,1.8831254657471044e-11,1.9352228829005575e-12,1.8561774894882364e-13],[0.0002969820507549363,0.00042727744870952824,0.00030736877483274823,0.000147407052143007,5.301979446346182e-05,1.5256250303251696e-05,3.658274795775686e-06,6.765211307997008e-07,1.089894163701303e-07,1.742294587411032e-08,2.5066942069967195e-09,3.2786000572268e-10,3.9308544748460125e-11,4.35034183428603e-12,4.4706957764016174e-13,4.2880874011106016e-14],[6.0031940519366817e-05,8.636984733923643e-05,6.21315125320364e-05,2.9796855951022867e-05,1.0717419249710971e-05,3.0838978599051066e-06,7.394835290053449e-07,1.519883271602883e-07,2.4593669314527807e-08,3.5218736207388563e-09,5.067030722972648e-10,6.627360916995098e-11,7.945827750343274e-12,8.793779340229411e-13,9.037062753351112e-14,8.66793825252886e-15],[1.0786537056468189e-05,1.5518931269356877e-05,1.1163788085194767e-05,5.35389807661248e-06,1.9257055308651577e-06,5.541146639012601e-07,1.3287037565761757e-07,2.730925751993918e-08,4.9113363289166566e-09,7.064155448868827e-10,9.104439101377183e-11,1.1908039869991295e-11,1.4277060633370807e-12,1.580065976531078e-13,1.6237791320306023e-14,1.5574548541191619e-15],[1.7443121544558975e-06,2.509596944375429e-06,1.8053181614110367e-06,8.657894039452739e-07,3.1140963460342315e-07,8.960697378085932e-08,2.148673017237939e-08,4.416233826650695e-09,7.942218719781763e-10,1.2696356351260092e-10,1.6435472141120063e-11,1.925672583539277e-12,2.3087715976239977e-13,2.5551558143979705e-14,2.6258452192071983e-15,2.5185909229573535e-16],[2.56432867636443e-07,3.689380592882391e-07,2.654014145026631e-07,1.2728046356598765e-07,4.578060492611887e-08,1.3173200214279815e-08,3.158783145641974e-09,6.492344282691479e-10,1.16759257596572e-10,1.866502540483277e-11,2.685396108890228e-12,3.160230435371919e-13,3.3941454801188954e-14,3.756357089355871e-15,3.860278206573551e-16,3.702602720087847e-17],[3.455688678385173e-08,4.9718083577152883e-08,3.576548793365064e-08,1.7152312064309333e-08,6.169393166756847e-09,1.7752201290798362e-09,4.2567753714569374e-10,8.749081520112913e-11,1.573447461287099e-11,2.5152983534348516e-12,3.618839119963397e-13,4.733216406169364e-14,5.105969265857432e-15,5.062065867493422e-16,5.2021099388811104e-17,4.9896264930070726e-18],[4.29866325470709e-09,6.184622483627029e-09,4.449005772096854e-09,2.1336416693233566e-09,7.674344010112452e-10,2.208264183525304e-10,5.2951656169950003e-11,1.08833169718636e-11,1.957271448482351e-12,3.128875779281205e-13,4.5016123260711446e-14,5.887828833957583e-15,7.059170961726281e-16,7.02932185187622e-17,6.4711034246477575e-18,6.206787143286702e-19],[4.965323587996056e-10,7.143767743885888e-10,5.138982049625186e-10,2.4645385510069303e-10,8.864523475776218e-11,2.5507339350153815e-11,6.116369015791285e-12,1.2571161608636952e-12,2.2608158665647423e-13,3.614119038927398e-14,5.199747117241429e-15,6.800945703136955e-16,8.153946008581844e-17,9.024107267932574e-18,8.344096048237195e-19,7.169369820835639e-20],[5.353015053244531e-11,7.701551689874328e-11,5.5402327325658483e-11,2.6569692244702177e-11,9.556663682581994e-12,2.7498947266938603e-12,6.59393387610878e-13,1.3552715373976708e-13,2.4373399138764765e-14,3.896308725249465e-15,5.605742324417535e-16,7.331962173261637e-17,8.790604469928946e-18,9.728707745074118e-19,9.99785632544132e-20,8.628170401103766e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1534570630083004, "-10": 5.38767673914082e-07, "-11": 6.926428065309398e-08, "-12": 8.183671936921265e-09, "-13": 8.939224335946878e-10, "-14": 8.999794708889278e-11, "-15": 7.473069045854977e-12, "-2": 0.08806346747573478, "-3": 0.03594533130478969, "-4": 0.011664996669258536, "-5": 0.003126358461003962, "-6": 0.0007117633491616518, "-7": 0.00014062687268528006, "-8": 2.451784109198677e-05, "-9": 3.822593316001589e-06, "0": 0.2577331807853399, "1": 0.2154399053776537, "10": 2.1512407384765945e-06, "11": 3.10855967504476e-07, "12": 4.128197716468598e-08, "13": 5.068442356421338e-09, "14": 5.735478756983489e-10, "15": 5.353015053244531e-11, "2": 0.13803336868349397, "3": 0.06332762391810415, "4": 0.023099241478490885, "5": 0.006958478165867469, "6": 0.0017806293006289193, "7": 0.00039542908564151367, "8": 7.748986688518201e-05, "9": 1.3579481328544338e-05} |
| Raw goal margin distribution | {"-1": 0.17604552047973637, "-10": 3.7814918403436517e-07, "-11": 4.5696938901410704e-08, "-12": 5.073588221239988e-09, "-13": 5.207360879097589e-10, "-14": 4.9343633383722686e-11, "-15": 3.9065204693779245e-12, "-2": 0.09757169740369681, "-3": 0.03798313215557947, "-4": 0.011692168813423711, "-5": 0.0029629158600731204, "-6": 0.0006365134134103557, "-7": 0.00011850753172095441, "-8": 1.9451697503930614e-05, "-9": 2.853226580171754e-06, "0": 0.2709088043752918, "1": 0.19926664883953635, "10": 1.2169903661518425e-06, "11": 1.6530023802897622e-07, "12": 2.0628325881334316e-08, "13": 2.379736328982396e-09, "14": 2.5345723166984774e-10, "15": 2.255412916761448e-11, "2": 0.12326751892766544, "3": 0.05393590452023037, "4": 0.018661419091845273, "5": 0.005315343124686622, "6": 0.0012834588344394955, "7": 0.00026858560556289004, "8": 4.9551486257101106e-05, "9": 8.16954438456384e-06} |
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
| Totals anchor scale | 1.0660 |
| Totals anchor target over 2 5 | 0.5906 |
| Totals anchor reference over odds | 1.63 |
| Totals anchor reference under odds | 2.29 |
| Totals anchor reference last update utc | 2026-11-05T16:49:14Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5515 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.74, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.74, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.48, "draw": 3.77, "home": 2.09}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.31}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.79, "home_away": 1.3, "home_draw": 1.33}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.73, "home": 2.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.63, "under": 2.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.19, "under": 4.7}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.06 |
| Reference draw odds | 3.73 |
| Reference away odds | 3.39 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:14Z |
| Market reference home last update utc | 2026-11-05T16:49:14Z |
| Market reference draw last update utc | 2026-11-05T16:49:14Z |
| Market reference away last update utc | 2026-11-05T16:49:14Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market best over 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market best under 2 5 last update utc | 2026-11-05T16:49:11Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | -0.0672 |
| Raw ev home | -0.1597 |
| Raw edge prob draw | 0.0188 |
| Raw ev draw | 0.0213 |
| Raw edge prob away | 0.0484 |
| Raw ev away | 0.1381 |
| Market p home draw | 72.1% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T16:49:11Z |
| Market reference home draw last update utc | 2026-11-05T16:49:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.5% |
| Market draw away odds | 1.79 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T16:49:11Z |
| Market reference draw away last update utc | 2026-11-05T16:49:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.4% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T16:49:11Z |
| Market reference home away last update utc | 2026-11-05T16:49:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home draw odds | 1.30 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 82.3% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-11-05T16:49:14Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.7% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.56 |
| Market reference under 3 5 last update utc | 2026-11-05T16:49:14Z |
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
| Team research json | {"base_rates": [1.5169755217256848, 1.3496345134567405], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:22.148024+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-05T16:50:21.944578+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:22.281561+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Goztepe%22+%22Basaksehir%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:22.318600+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Goztepe_vs_Basaksehir&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.5169755217256848, 1.3496345134567405], "h2h": [], "margin_distribution": {"-1": 0.18728246351561698, "-10": 3.7814918403436517e-07, "-11": 4.5696938901410704e-08, "-12": 5.073588221239988e-09, "-13": 5.207360879097589e-10, "-14": 4.9343633383722686e-11, "-15": 3.9065204693779245e-12, "-2": 0.09757169740369681, "-3": 0.03798313215557947, "-4": 0.011692168813423711, "-5": 0.0029629158600731204, "-6": 0.0006365134134103557, "-7": 0.00011850753172095441, "-8": 1.9451697503930614e-05, "-9": 2.853226580171754e-06, "0": 0.2484349183035306, "1": 0.21050359187541692, "10": 1.2169903661518425e-06, "11": 1.6530023802897622e-07, "12": 2.0628325881334316e-08, "13": 2.379736328982396e-09, "14": 2.5345723166984774e-10, "15": 2.255412916761448e-11, "2": 0.12326751892766544, "3": 0.05393590452023037, "4": 0.018661419091845273, "5": 0.005315343124686622, "6": 0.0012834588344394955, "7": 0.00026858560556289004, "8": 4.9551486257101106e-05, "9": 8.16954438456384e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:22.318824+00:00", "p_over_1_5": 0.7800229094483683, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Samsunspor vs Torku Konyaspor

The model's most likely 1X2 outcome is **Samsunspor win** at **41.4%**. Expected goals are 1.41 for Samsunspor and 1.08 for Torku Konyaspor (2.49 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 48.5%; Under 3.5 goals: 73.2%; Double Chance 1X: 70.1%; Double Chance X2: 58.6%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Samsunspor win | 41.4% | 2.41 |
| Draw | 28.7% | 3.48 |
| Torku Konyaspor win | 29.9% | 3.35 |

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
| 1 | 1-1 | 13.71% |
| 2 | 1-0 | 9.04% |
| 3 | 0-0 | 8.61% |
| 4 | 2-1 | 8.58% |
| 5 | 0-1 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Samsunspor win | 41.4% | 40.6% | 2.37 | -1.8% |
| Draw | 28.7% | 28.6% | 3.48 | -0.1% |
| Torku Konyaspor win | 29.9% | 30.8% | 3.18 | -5.0% |
| Over 2.5 | 48.5% | 48.5% | 1.98 | -4.0% |
| Under 2.5 | 51.5% | 51.5% | 1.90 | -2.1% |

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
| Market best home last update utc | 2026-11-05T16:49:14Z |
| Market best draw last update utc | 2026-11-05T16:49:11Z |
| Market best away last update utc | 2026-11-05T16:49:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Samsunspor |
| Matched away-team name | Konyaspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4121 |
| Dc lambda away | 1.0826 |
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
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.61 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.96 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.74 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.02 |
| Fair Under 4.5 odds | 1.14 |
| Score matrix json | [[0.08610891551395357,0.07585695004444691,0.05037628111815262,0.019109255418864726,0.005436541283291966,0.0012373472634945296,0.0002346817229768683,3.815224903719551e-05,5.427115614781817e-06,6.862233321493607e-07,7.809161357705712e-08,8.078870146422978e-09,7.661402831709246e-10,6.706622503000668e-11,5.451484007516011e-12,4.1358273377564474e-13],[0.09044891989939953,0.13713973036083799,0.07477739525764321,0.02836534007312427,0.008069877080083403,0.00183668987348002,0.00034835616225077865,5.6632322650636896e-05,8.05588583412188e-06,1.0186141613510095e-06,1.1591739852854148e-07,1.199208938741127e-08,1.137241048879867e-09,9.95515648672949e-11,8.092057716897516e-12,6.139127158422556e-13],[0.07540896668186613,0.08581474296306399,0.05281879070527343,0.021052429825959965,0.005989370143090485,0.001363170142639171,0.00025854594520352157,4.203185984762063e-05,5.978986000928841e-06,7.560037389394582e-07,8.603256269231697e-08,8.900391098583002e-09,8.440472532683962e-10,7.388602879536665e-11,6.0058323571454e-12,4.556389712309219e-13],[0.037311779686653834,0.042460478165849795,0.024159825947909542,0.009913547456274254,0.002963494516290119,0.0006744861556339067,0.00012792655529957387,2.079704262585876e-05,2.9583565222077344e-06,3.740648651054765e-07,4.2568253701133036e-08,4.403845410008021e-09,4.176281222886579e-10,3.6558241673896646e-11,2.971639893836039e-12,2.2544667642700885e-13],[0.013846187310111108,0.015756839767456406,0.00896557275647975,0.0034009143981501865,0.0010466277681433023,0.00025029794149230417,4.7472810503562406e-05,7.717663164617326e-06,1.0978291274385117e-06,1.3881332468937407e-07,1.579683465007823e-08,1.6342417580674922e-09,1.5497939942133407e-10,1.3566553678117484e-11,1.1027585104167539e-12,8.366196778780138e-14],[0.004110592518217675,0.004677818247595358,0.0026616580773401476,0.0010096478522955026,0.0002872426010472818,7.071888257189057e-05,1.4093510025839972e-05,2.291184407091887e-06,3.2591847101727323e-07,4.1210262516121e-08,4.689691744724218e-09,4.851661900287572e-10,4.600957256110473e-11,4.027576169401157e-12,3.273818836041444e-13,2.4837180889267116e-14],[0.0010169448619313046,0.0011572743371807718,0.0006584840248633184,0.0002497830157578068,7.106272051248556e-05,1.617375058529072e-05,3.3183029612656737e-06,5.668302562715441e-07,8.063098276966492e-08,1.0195261276537513e-08,1.1602117949425998e-09,1.200282591733177e-10,1.1382592219566068e-11,9.964069348536142e-13,8.099302544465853e-14,6.144623525260126e-15],[0.00021564708687723137,0.00024540449425828394,0.00013963408148529613,5.2967453512950876e-05,1.5069124431176454e-05,3.429706297913785e-06,6.504959497189543e-07,1.1439396154515225e-07,1.7098111409211326e-08,2.1619445424623955e-09,2.460273935253692e-10,2.5452456079590032e-11,2.413722656112572e-12,2.1129194009337347e-13,1.7174883957173602e-14,1.302991157911135e-15],[4.0012698172770054e-05,4.5534099723722005e-05,2.5908703140904974e-05,9.827959009715244e-06,2.7960327974930806e-06,6.36372162067737e-07,1.206976568783042e-07,1.9621839336337762e-08,3.0193000333422e-09,4.0114260617423964e-10,4.564967689532606e-11,4.722630189983104e-12,4.478593126870862e-13,3.920461318407821e-14,3.1867504350845737e-15,2.41766270429462e-16],[6.599325626572501e-06,7.509974705833828e-06,4.273142687123037e-06,1.620932971569906e-06,4.6115187767543334e-07,1.0495735876239782e-07,1.9906759015974274e-08,3.2362453192647966e-09,4.603523500888113e-10,6.296575258244211e-11,7.529036939205843e-12,7.789070935183785e-13,7.386578696975742e-14,6.466047536919657e-15,5.255932434483155e-16,3.98747002063408e-17],[9.795887466458588e-07,1.1147634054921929e-06,6.342954910821426e-07,2.4060756929822755e-07,6.845232610533908e-08,1.5579629395362355e-08,2.9549136105240725e-09,4.803808260911099e-10,6.833364606577048e-11,8.640343348029678e-12,1.0636225691842033e-12,1.1561918090856835e-13,1.096446785204254e-14,9.598052529699767e-16,7.801785450954829e-17,5.918908962565589e-18],[1.321890043777355e-07,1.504299280624752e-07,8.559396964749696e-08,3.246839568153807e-08,9.237187407662323e-09,2.102367657242581e-09,3.9874599369873037e-10,6.482420642393805e-11,9.221172323450911e-12,1.1659570289763096e-12,1.3268488768675916e-13,1.48485935473944e-14,1.4795822163697967e-15,1.2951935311736474e-16,1.0527992023812627e-17,7.987175081818892e-19],[1.6351526964784266e-08,1.8607894329813235e-08,1.0587810304664835e-08,4.016278433967653e-09,1.142622411645882e-09,2.6005885738468033e-10,4.932411662193187e-11,8.018630326338212e-12,1.1406413763656866e-12,1.4422665401583898e-13,1.6412866781488818e-14,1.697972591222571e-15,1.7418308288759077e-16,1.602129621090263e-17,1.3022924733624876e-18,9.879982782048392e-20],[1.867063943238111e-09,2.124702398595687e-09,1.2089463510202176e-09,4.585901161533978e-10,1.3046788291480806e-10,2.969426138539502e-11,5.631968187143285e-12,9.155900601029434e-13,1.3024168266146774e-13,1.6468210335755873e-14,1.8740678982999567e-15,1.938793489137651e-16,1.838608327472053e-17,1.7410146032566976e-18,1.4869946554851057e-19,1.1281245875020511e-20],[1.979590612258836e-10,2.2527567614043131e-10,1.2818087221231206e-10,4.8622902932691833e-11,1.3833109313412563e-11,3.1483914243740154e-12,5.971403064253489e-13,9.707720478570338e-14,1.3809125994596686e-14,1.7460738128136332e-15,1.987016690909932e-16,2.0556432489125386e-17,1.9494199959601582e-18,1.7064791265895455e-19,1.5004775023505473e-20,1.1961158861031163e-21],[1.9589725743352943e-11,2.2292936150085295e-11,1.2684582946762536e-11,4.811648061970916e-12,1.3689033275337708e-12,3.115599970735111e-13,5.909209086330426e-14,9.606611619122923e-15,1.366529975007703e-15,1.7278879233337802e-16,1.966321308120082e-17,2.0342330996620394e-18,1.9291161941757311e-19,1.6887056278015274e-20,1.372665856657863e-21,1.1264971975315516e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17491524543301482, "-10": 9.0965436055102e-08, "-11": 9.293052525959835e-09, "-12": 8.719231270717918e-10, "-13": 7.561392171813512e-11, "-14": 6.065396723358266e-12, "-15": 4.1358273377564474e-13, "-2": 0.08545532432427892, "-3": 0.028678283224608643, "-4": 0.007553714370109976, "-5": 0.0016308372676132885, "-6": 0.0002976833900914904, "-7": 4.700838812911219e-05, "-8": 6.536325273506759e-06, "-9": 8.114726499789589e-07, "0": 0.2871017664673216, "1": 0.20412849014707196, "10": 1.1410792197984629e-06, "11": 1.5205583686482915e-07, "12": 1.8609221883654237e-08, "13": 2.1050242023253047e-09, "14": 2.202519973759689e-10, "15": 1.9589725743352943e-11, "2": 0.12791928188671997, "3": 0.05599578644030857, "4": 0.019238361047134122, "5": 0.0054178060342971604, "6": 0.0012899495972495145, "7": 0.0002657044398340516, "8": 4.819060968878751e-05, "9": 7.80383295551259e-06} |
| Raw goal margin distribution | {"-1": 0.16524604676819, "-10": 5.773034397636786e-08, "-11": 5.617119780591045e-09, "-12": 5.017718509192947e-10, "-13": 4.123410715955772e-11, "-14": 2.8746126172766997e-12, "-2": 0.07821953173716219, "-3": 0.025230281287360018, "-4": 0.00636474360220035, "-5": 0.0013134252475456834, "-6": 0.0002288668177191059, "-7": 3.447323942322547e-05, "-8": 4.569558522478244e-06, "-9": 5.405961764470272e-07, "0": 0.29025313417107695, "1": 0.21924871512625302, "10": 8.231088595593372e-07, "11": 1.0446531764402974e-07, "12": 1.217222723519007e-08, "13": 1.3047450733152533e-09, "14": 1.1864616660885968e-10, "2": 0.1330839976374454, "3": 0.05599355374204902, "4": 0.018424773836941855, "5": 0.0049594318396044565, "6": 0.001127235635258543, "7": 0.0002214722344956033, "8": 3.829276694586703e-05, "9": 5.909092489643358e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.99, "date": "2026-11-01T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 5.0, "home_xg": 3.89, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 2.0, "away_xg": 1.63, "date": "2026-10-24T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.08, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 1.0, "away_xg": 1.07, "date": "2026-10-18T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 4.0, "home_xg": 2.41, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 0.36, "date": "2026-09-20T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 5.0, "away_xg": 1.73, "date": "2026-09-12T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.32, "date": "2026-08-22T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.85, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 3.0, "away_xg": 1.89, "date": "2026-08-17T00:00:00+00:00", "home": "Samsunspor", "home_goals": 3.0, "home_xg": 2.74, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 51.2% |
| P home draw | 70.1% |
| P draw away | 58.6% |
| P home away | 71.3% |
| Raw p home draw | 72.3% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0512 |
| Totals anchor target over 2 5 | 0.4847 |
| Totals anchor reference over odds | 1.97 |
| Totals anchor reference under odds | 1.86 |
| Totals anchor reference last update utc | 2026-11-05T16:49:14Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4555 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.22, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.9, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.22, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.18, "draw": 3.48, "home": 2.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.98, "under": 1.9}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.65, "home_away": 1.33, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.09, "draw": 3.32, "home": 2.37}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.97, "under": 1.86}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.97, "under": 1.86}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.3, "under": 3.53}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.37 |
| Reference draw odds | 3.32 |
| Reference away odds | 3.09 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:14Z |
| Market reference home last update utc | 2026-11-05T16:49:14Z |
| Market reference draw last update utc | 2026-11-05T16:49:14Z |
| Market reference away last update utc | 2026-11-05T16:49:14Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:14Z |
| Market best over 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market best under 2 5 last update utc | 2026-11-05T16:49:11Z |
| Home probability edge | +0.8% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0268 |
| Raw ev home | 0.0265 |
| Raw edge prob draw | 0.0045 |
| Raw ev draw | 0.0101 |
| Raw edge prob away | -0.0313 |
| Raw ev away | -0.1203 |
| Market p home draw | 69.7% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T16:49:11Z |
| Market reference home draw last update utc | 2026-11-05T16:49:16Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.4% |
| Market draw away odds | 1.65 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T16:49:11Z |
| Market reference draw away last update utc | 2026-11-05T16:49:16Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T16:49:11Z |
| Market reference home away last update utc | 2026-11-05T16:49:16Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.60 |
| Market reference dc home draw odds | 1.34 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 75.0% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.53 |
| Market reference over 1 5 last update utc | 2026-11-05T16:49:14Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.6% |
| Market under 3 5 odds | 1.32 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference under 3 5 odds | 1.32 |
| Market reference under 3 5 opposite odds | 3.35 |
| Market reference under 3 5 last update utc | 2026-11-05T16:49:14Z |
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
| Team research json | {"base_rates": [1.4120919826946579, 1.082574203578663], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:22.148024+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-05T16:50:21.944578+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:22.195063+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Samsunspor%22+%22Torku+Konyaspor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:22.232392+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Samsunspor_vs_Torku+Konyaspor&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.913613856180298, "goals_for": 0.9751316584067636, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.22037567410820427, "results": "LLLLLLLLWD", "xg_against": 2.102762810589968, "xg_for": 1.119679917641185, "xg_matches": 10}, "venue": {"goals_against": 2.9627088822913965, "goals_for": 0.9012025941363605, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.148698354997035, "results": "LLLLD", "xg_against": 1.764225747400591, "xg_for": 1.383053774479519, "xg_matches": 5}}}, "goal_rates": [1.4120919826946579, 1.082574203578663], "h2h": [], "margin_distribution": {"-1": 0.17741651405180595, "-10": 5.773034397636786e-08, "-11": 5.617119780591045e-09, "-12": 5.017718509192947e-10, "-13": 4.123410715955772e-11, "-14": 2.8746126172766997e-12, "-2": 0.07821953173716219, "-3": 0.025230281287360018, "-4": 0.00636474360220035, "-5": 0.0013134252475456834, "-6": 0.0002288668177191059, "-7": 3.447323942322547e-05, "-8": 4.569558522478244e-06, "-9": 5.405961764470272e-07, "0": 0.265912199603845, "1": 0.231419182409869, "10": 8.231088595593372e-07, "11": 1.0446531764402974e-07, "12": 1.217222723519007e-08, "13": 1.3047450733152533e-09, "14": 1.1864616660885968e-10, "2": 0.1330839976374454, "3": 0.05599355374204902, "4": 0.018424773836941855, "5": 0.0049594318396044565, "6": 0.001127235635258543, "7": 0.0002214722344956033, "8": 3.829276694586703e-05, "9": 5.909092489643358e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:22.232620+00:00", "p_over_1_5": 0.7116061870759051, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Alanyaspor vs Trabzonspor

The model's most likely 1X2 outcome is **Trabzonspor win** at **54.7%**. Expected goals are 1.18 for Alanyaspor and 1.61 for Trabzonspor (2.79 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.9%; Under 3.5 goals: 69.0%; Double Chance 1X: 45.3%; Double Chance X2: 78.7%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 55.6%; BTTS No (at least one team does not score): 44.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alanyaspor win | 21.3% | 4.70 |
| Draw | 24.1% | 4.16 |
| Trabzonspor win | 54.7% | 1.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alanyaspor expected goals | 1.18 |
| Trabzonspor expected goals | 1.61 |
| Expected total goals | 2.79 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 31.0% |
| Under 3.5 | 69.0% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.44% |
| 2 | 1-2 | 11.10% |
| 3 | 0-1 | 10.40% |
| 4 | 0-2 | 9.43% |
| 5 | 0-0 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alanyaspor win | 21.3% | 18.9% | 4.87 | +3.6% |
| Draw | 24.1% | 22.8% | 4.07 | -2.1% |
| Trabzonspor win | 54.7% | 58.3% | 1.74 | -4.9% |
| Over 2.5 | 53.9% | 56.6% | 1.72 | -7.2% |
| Under 2.5 | 46.1% | 43.4% | 2.22 | +2.2% |

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
| Market best home last update utc | 2026-11-05T16:49:14Z |
| Market best draw last update utc | 2026-11-05T16:49:14Z |
| Market best away last update utc | 2026-11-05T16:49:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
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
| P btts yes | 55.6% |
| P btts no | 44.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.34 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.59 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.23 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.06516974162216205,0.10401479897529704,0.09434502102629909,0.05057165295470262,0.020330898663888982,0.006538768916278992,0.0017524843854392728,0.0004025923656969003,8.092542078039679e-05,1.445945336383532e-05,2.3252052396917183e-06,3.3992102358398866e-07,4.555186868818682e-08,5.634719009206606e-09,6.472225586720867e-10,6.938599253159417e-11],[0.048701293444761505,0.11436370495048426,0.11104254775431589,0.0595220089746112,0.023929135435178238,0.007696024143531093,0.0020626454787114595,0.0004738446343761944,9.524789759748303e-05,1.7018540281075513e-05,2.736728563503947e-06,4.000814890220781e-07,5.361380493726656e-08,6.631972178876946e-09,7.617703732238488e-10,8.166617915133437e-11],[0.03392303580933466,0.05455117743759068,0.04935260525765669,0.035028215861829436,0.014082100652346982,0.004529047315799527,0.00121385000807936,0.00027885369502529293,5.605260936090329e-05,1.0015271878222865e-05,1.6105423948062705e-06,2.3544468678409615e-07,3.155128606827836e-08,3.902861430138185e-09,4.4829563937959547e-10,4.8059879046487804e-11],[0.013308952900932178,0.021401948082945713,0.017208092370400586,0.010378806714303895,0.005524800769060303,0.0017768715556843743,0.000476227206701793,0.00010940208046831996,2.1991001694292154e-05,3.929270436362901e-06,6.318606918881054e-07,9.23715160634889e-08,1.2378449340639667e-08,1.5312013713784625e-09,1.7587888017246805e-10,1.8855230712523566e-11],[0.003916105010061269,0.0062974357739912475,0.005063410866876149,0.002714134294965617,0.0012277425049986464,0.0005228371948753055,0.00014012790968414586,3.2191115155506045e-05,6.470762392227826e-06,1.156171770706967e-06,1.859224267741211e-07,2.7179941167110697e-08,3.642308139528642e-09,4.505497469637818e-10,5.175164184096902e-11,5.5480745937573225e-12],[0.000921838318249835,0.0014823957958909825,0.0011919103665854,0.0006388983409656222,0.00025685095637141884,9.294951607123438e-05,3.298565188400727e-05,7.5776832800186294e-06,1.5231963152469842e-06,2.7215905548451305e-07,4.376553151206291e-08,6.3980693038736415e-09,8.573874299244692e-10,1.0605793766048252e-10,1.218216732155512e-11,1.305998623605313e-12],[0.00018083143897878345,0.0002907926038657194,0.0002338098367754694,0.00012532881750599927,5.038489627107524e-05,1.6204654749099443e-05,4.886799067926394e-06,1.4864682282385493e-06,2.987961946040987e-07,5.338779334732852e-08,8.58521921286932e-09,1.2550704998920352e-09,1.6818849861863002e-10,2.0804743199088198e-11,2.3897019716206818e-12,2.5618983908071186e-13],[3.0405092590473e-05,4.889402028260859e-05,3.931290806437486e-05,2.107285282937717e-05,8.471742772909977e-06,2.724659112516516e-06,7.302479429181722e-07,1.88759254074698e-07,5.02397482092952e-08,8.976651455596809e-09,1.443523242147213e-09,2.1102820932186387e-10,2.827930199544602e-11,3.498120386928449e-12,4.0180573754814636e-13,4.3075893340103015e-14],[4.473287129019302e-06,7.193432842389489e-06,5.78383128173041e-06,3.1003004201640707e-06,1.2463878474849587e-06,4.008599053832278e-07,1.0743623668727874e-07,2.4680966660174826e-08,5.5822351696740505e-09,1.3206715058843677e-09,2.1237540784732371e-10,3.104709416064303e-11,4.160534530768572e-12,5.146538151806242e-13,5.911484823773958e-14,6.33745280255019e-15],[5.849984265075889e-07,9.407280982896425e-07,7.563860985018966e-07,4.0544476917903915e-07,1.62997569475656e-07,5.242283965585285e-08,1.4050077180208602e-08,3.2276771520485675e-09,6.487980248225907e-10,1.3043764819700834e-10,2.7773598214525816e-11,4.060213598582698e-12,5.440979046797069e-13,6.730434765156641e-14,7.730801132341831e-15,8.287864853358428e-16],[6.885335866697272e-08,1.107221596241262e-07,8.90254075413101e-08,4.77201866654426e-08,1.9184547520841165e-08,6.170082546570426e-09,1.6536711203871966e-09,3.798923254168959e-10,7.636246711332615e-11,1.3644161764309508e-11,2.468782384746706e-12,4.778805044599687e-13,6.403943409645088e-14,7.92161171503563e-15,9.099026579027316e-16,9.754681473904483e-17],[7.36720707255889e-09,1.1847106564797608e-08,9.525586329754185e-09,5.1059890688254265e-09,2.0527180796363797e-09,6.601896647515334e-10,1.7694035279715112e-10,4.064791436186959e-11,8.170670519014159e-12,1.4599050357927604e-12,2.347653644478612e-13,3.86168895271718e-14,6.8521242962160494e-15,8.476006832920088e-16,9.735823242935879e-17,1.0437364238497205e-17],[7.225901927763227e-10,1.1619875662766386e-09,9.342882851715256e-10,5.00805473392898e-10,2.0133463580856043e-10,6.475270376186825e-11,1.7354658607850876e-11,3.986827570532364e-12,8.013954714857194e-13,1.431903638460113e-13,2.3026249741974756e-14,3.366200216644253e-15,5.07568483742765e-16,8.313434590682463e-17,9.549087360599645e-18,1.0237172598642342e-18],[6.542129590315792e-11,1.0520310567335067e-10,8.45878493426782e-11,4.5341527455382635e-11,1.8228275053358795e-11,5.8625287689809885e-12,1.5712422718058536e-12,3.609562222323209e-13,7.255610552099917e-14,1.2964055224245919e-14,2.0847322769796455e-15,3.047663567038299e-16,4.0840889788977084e-17,5.684441393610611e-18,8.645476731736856e-19,9.268449869410212e-20],[5.4999854299606135e-12,8.844452565515524e-12,7.111322582559491e-12,3.8118740531510326e-12,1.5324558436628055e-12,4.92864324483122e-13,1.3209474808727023e-13,3.034568385912333e-14,6.0998107376365434e-15,1.0898915079900692e-15,1.7526398690924118e-16,2.562178719135296e-17,3.4335042692903675e-18,4.2472092433344616e-19,5.489231818081317e-20,7.792010007801736e-21],[4.315595305477743e-13,6.939850742756006e-13,5.579940300542099e-13,2.9910089723580985e-13,1.2024503208203038e-13,3.867288362965812e-14,1.0364890634406113e-14,2.3810915950895924e-15,4.786251694458672e-16,8.551896610016443e-17,1.3752189869532984e-17,2.010428317111822e-18,2.694118938055697e-19,3.332597241452536e-20,3.827931987579544e-21,4.617521263766246e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.25616772426416834, "-10": 2.758422273793918e-06, "-11": 3.976191169061596e-07, "-12": 5.2650991737155886e-08, "-13": 6.444549261476942e-09, "-14": 7.288887378234211e-10, "-15": 6.938599253159417e-11, "-2": 0.16987401579125236, "-3": 0.07953983208676874, "-4": 0.029356926617891646, "-5": 0.00890346031288454, "-6": 0.002286503391855374, "-7": 0.0005085154544059777, "-8": 9.965062577119712e-05, "-9": 1.744446805156813e-05, "0": 0.24059063183917953, "1": 0.12344850875042886, "10": 8.168166617312453e-08, "11": 8.61771460726344e-09, "12": 8.352037219294687e-10, "13": 7.482374249872766e-11, "14": 6.1939705042362145e-12, "15": 4.315595305477743e-13, "2": 0.06108051339726527, "3": 0.020932514899978594, "4": 0.005654684001377811, "5": 0.0012552134792529555, "6": 0.00023593459777128723, "7": 3.840475079087981e-05, "8": 5.508353955559497e-06, "9": 7.057657094391307e-07} |
| Raw goal margin distribution | {"-1": 0.21669737239968134, "-10": 2.333404258545408e-06, "-11": 3.3635391849986706e-07, "-12": 4.4538520988355834e-08, "-13": 5.451572383967573e-09, "-14": 6.16581478840692e-10, "-15": 5.869499097175492e-11, "-2": 0.14369980826696738, "-3": 0.06728432578235442, "-4": 0.024833608051524597, "-5": 0.007531614143073348, "-6": 0.0019341986911944624, "-7": 0.00043016333580248294, "-8": 8.429644610627812e-05, "-9": 1.4756622445483291e-05, "0": 0.26948073203415124, "1": 0.15558272934633782, "10": 1.0294378352081151e-07, "11": 1.0860945773240798e-08, "12": 1.052611132635939e-09, "13": 9.430071043947852e-11, "14": 7.806289815035412e-12, "15": 5.438964821664056e-13, "2": 0.07698005492665844, "3": 0.026381345819296825, "4": 0.007126624528968839, "5": 0.0015819513819263472, "6": 0.00029734947015599126, "7": 4.840168592065111e-05, "8": 6.942204092106262e-06, "9": 8.894798038879746e-07} |
| Research history json | {"away": [{"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.51, "date": "2026-11-01T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 1.37, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 4.0, "away_xg": 2.63, "date": "2026-10-26T00:00:00+00:00", "home": "Rizespor", "home_goals": 3.0, "home_xg": 1.81, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 1.19, "date": "2026-10-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.35, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": 0.92, "date": "2026-09-12T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Genclerbirligi", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-06T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": 3.2, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-08-31T00:00:00+00:00", "home": "Amedspor", "home_goals": 2.0, "home_xg": 2.39, "source": "pipeline training history"}, {"away": "Buyuksehyr", "away_goals": 1.0, "away_xg": 1.95, "date": "2026-08-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-08-15T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 1.0, "home_xg": 1.86, "source": "pipeline training history"}], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-11-02T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 5.0, "home_xg": 1.91, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Erzurumspor", "away_goals": 0.0, "away_xg": 1.69, "date": "2026-10-10T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 0.0, "home_xg": 0.98, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-19T00:00:00+00:00", "home": "Corum", "home_goals": 1.0, "home_xg": 1.14, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 1.79, "date": "2026-09-12T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": 1.73, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 2.06, "date": "2026-09-07T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 0.74, "date": "2026-08-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.54, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 1.25, "date": "2026-08-15T00:00:00+00:00", "home": "Gaziantep", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 46.3% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 56.5% |
| P home draw | 45.3% |
| P draw away | 78.7% |
| P home away | 75.9% |
| Raw p home draw | 53.7% |
| Raw p draw away | 73.2% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5395 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.0, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.86, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.74, "draw": 4.04, "home": 4.79}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.72, "under": 2.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.67, "draw": 4.07, "home": 4.87}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.87 |
| Reference draw odds | 4.07 |
| Reference away odds | 1.67 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:14Z |
| Market reference home last update utc | 2026-11-05T16:49:14Z |
| Market reference draw last update utc | 2026-11-05T16:49:14Z |
| Market reference away last update utc | 2026-11-05T16:49:14Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market best over 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market best under 2 5 last update utc | 2026-11-05T16:49:11Z |
| Home probability edge | +2.4% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | 0.0791 |
| Raw ev home | 0.3052 |
| Raw edge prob draw | 0.0413 |
| Raw ev draw | 0.0968 |
| Raw edge prob away | -0.1203 |
| Raw ev away | -0.1952 |
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
| Team research json | {"base_rates": [1.1769836558026978, 1.6080865446181485], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:22.322317+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-05T16:50:21.944578+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:22.405250+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Alanyaspor%22+%22Trabzonspor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:22.442119+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Alanyaspor_vs_Trabzonspor&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.7743771520489182, "goals_for": 2.5504665648542564, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.445760234190055, "results": "WWWWWLWLWD", "xg_against": 1.304688418272264, "xg_for": 1.9416908629267322, "xg_matches": 10}, "venue": {"goals_against": 1.4632227425095123, "goals_for": 2.031257084649452, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.6015486554658407, "results": "WWLLD", "xg_against": 1.7335781977270697, "xg_for": 1.5880534238553998, "xg_matches": 5}}, "home": {"all": {"goals_against": 2.0080296773705193, "goals_for": 0.7681538045198641, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 0.9433296058372811, "results": "LLLDWDWLWD", "xg_against": 1.821921306986439, "xg_for": 0.9535220089451488, "xg_matches": 10}, "venue": {"goals_against": 1.069203922761527, "goals_for": 0.9657278891499795, "last_match": "2026-10-23T00:00:00+00:00", "matches": 4, "points_per_game": 1.0971691275701443, "results": "LDDW", "xg_against": 1.4768169943171596, "xg_for": 0.9185985305199439, "xg_matches": 4}}}, "goal_rates": [1.1876955586675686, 1.5915562472145317], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.22672706775391535, "-10": 2.116161955411144e-06, "-11": 3.019086864686867e-07, "-12": 3.956707922569962e-08, "-13": 4.793344063531587e-09, "-14": 5.365763267298028e-10, "-15": 5.056110308413688e-11, "-2": 0.14148284945108305, "-3": 0.06557503867538622, "-4": 0.023956304865992598, "-5": 0.007191357194900218, "-6": 0.0018279269290026586, "-7": 0.000402365650011064, "-8": 7.804102031950904e-05, "-9": 1.3521479691046584e-05, "0": 0.24803749183574222, "1": 0.16919460551415155, "10": 1.1333924374056387e-07, "11": 1.2066745624990102e-08, "12": 1.1801349773028616e-09, "13": 1.066889483183693e-10, "14": 8.912416612449318e-12, "15": 6.267057112980762e-13, "2": 0.0787898147751104, "3": 0.027251347255465238, "4": 0.007429376957891105, "5": 0.0016642806536652879, "6": 0.00031568771075941344, "7": 5.1856462077643644e-05, "8": 7.505645793011778e-06, "9": 9.704484875602103e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:22.442360+00:00", "p_over_1_5": 0.7653653723645186, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

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
| Market best home last update utc | 2026-11-05T16:49:11Z |
| Market best draw last update utc | 2026-11-05T16:49:11Z |
| Market best away last update utc | 2026-11-05T16:49:14Z |
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
| Dc lambda home | 1.4174 |
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
| Score matrix json | [[0.07367293744965195,0.05766761794676445,0.038094748014281726,0.014053776813526238,0.0038885014277498637,0.0008607191393026747,0.00015876669768697857,2.510212994501667e-05,3.4727201600645245e-06,4.270477918818201e-07,4.726347857898638e-08,4.755346846315429e-09,4.385813447562917e-10,3.733842582833214e-11,2.9517336782209497e-12,2.177885849835998e-13],[0.09107517060437258,0.12750691759393687,0.0640899114519529,0.02364381859690293,0.006541944104521992,0.0014480582310776478,0.000267106205623481,4.2231367033282296e-05,5.842441259160106e-06,7.184574408313986e-07,7.951521705571841e-08,8.00030907644857e-09,7.378612804938684e-10,6.281748875713724e-11,4.965943074252799e-12,3.6640355572406345e-13],[0.08576932999852425,0.09492513409930227,0.05413143399532766,0.019888965267514682,0.005503023910609075,0.0012180934202825685,0.0002246873120181577,3.552464204046289e-05,4.9146084759824285e-06,6.043598680271942e-07,6.68874777472379e-08,6.729787267599435e-09,6.206822015589628e-10,5.284150049463034e-11,4.177306170721781e-12,3.0821534025152534e-13],[0.04809892046744379,0.053233439919401666,0.029458032510008527,0.011199039871987315,0.0030860624585895874,0.0006830994079713101,0.00012600328288668044,1.992200396304873e-05,2.7560826488789317e-06,3.3892135133217196e-07,3.751009215634152e-08,3.774023914523415e-09,3.4807481705705453e-10,2.9633193237202015e-11,2.3426079844294715e-12,1.7284529490739077e-13],[0.02023018732488602,0.02238974286848052,0.012389914578299603,0.004570842525505043,0.0013032705343011554,0.0002873085061052882,5.2996408060208174e-05,8.37910431549892e-06,1.1591958349133404e-06,1.425487798732239e-07,1.577657426657117e-08,1.5873373044013745e-09,1.4639868595191928e-10,1.246358638400023e-11,9.852902704096907e-13,7.269794540541619e-14],[0.006806979869363034,0.0075336192660203204,0.004168913404665577,0.0015379804723244996,0.0004255396497210113,9.706626882263044e-05,1.7832038676706536e-05,2.8193705516869412e-06,3.9004199942320796e-07,4.796429511088397e-08,5.3084443418847995e-09,5.341014842535579e-10,4.925969750908026e-11,4.193702225959728e-12,3.31526887440515e-13,2.446114032320305e-14],[0.0019086565288875224,0.0021124040138505713,0.0011689506860443006,0.00043124506405780807,0.00011932002831330843,2.6411468268594932e-05,5.020414824330653e-06,7.905429594481884e-07,1.093665947346355e-07,1.3449043007885836e-08,1.4884717078387004e-09,1.4976043775261847e-10,1.3812269915017159e-11,1.1759013964201978e-12,9.295913464693552e-14,6.858829624581244e-15],[0.00045872700608318276,0.000507695729559352,0.0002809459116148732,0.00010364555074699166,2.867740660800168e-05,6.347739146223053e-06,1.1708924967564768e-06,1.907731678840501e-07,2.6285195795481244e-08,3.2323464910092263e-09,3.5773967701477777e-10,3.59934625220429e-11,3.319644540247202e-12,2.8261644715263454e-13,2.234182257481757e-14,1.6484528941163978e-15],[9.646924685480485e-05,0.00010676725811322773,5.908228672176488e-05,2.1796423772357225e-05,6.030793436044765e-06,1.3349151162812896e-06,2.462360310427348e-07,3.8931645857913645e-08,5.550231343056415e-09,6.797551210771476e-10,7.523184106025525e-11,7.569343367956157e-12,6.981137024342567e-13,5.943359654881876e-14,4.698434512411287e-15,3.4666589728139015e-16],[1.803312299825317e-05,1.9958143766167314e-05,1.1044329443923504e-05,4.074434118891332e-06,1.1273441366546379e-06,2.4953743570072183e-07,4.6029224640662336e-08,7.277543685365909e-09,1.0068019218798483e-09,1.275850637399165e-10,1.4063186844057386e-11,1.4149472958549032e-12,1.3049931116090014e-13,1.1110000251235728e-14,8.782845334023706e-16,6.480271142143513e-17],[3.0338598268898704e-06,3.357721820969828e-06,1.8580779057572121e-06,6.854753883623624e-07,1.8966232790668918e-07,4.19817244939143e-08,7.743873067006866e-09,1.2243607181965343e-09,1.6938252485288703e-10,2.082932971496583e-11,2.375601567132e-12,2.3804816051420923e-13,2.1954966846630363e-14,1.869126242982178e-15,1.4776099307514737e-16,1.09022903505995e-17],[4.640100557839567e-07,5.135427403883728e-07,2.8418149878242157e-07,1.0483921187572223e-07,2.9007677471478818e-08,6.4208445464988846e-09,1.1843773868383705e-09,1.8725838290704978e-10,2.5906007294472327e-11,3.1857168737066257e-12,3.525789480274758e-13,3.6556280491961414e-14,3.3578760959708885e-15,2.858712734801971e-16,2.259912802556148e-17,1.6674377335819481e-18],[6.505350680024771e-08,7.199791413492021e-08,3.984181556650229e-08,1.4698298663306072e-08,4.066832432029989e-09,9.001926772110282e-10,1.6604791518704296e-10,2.62533415687849e-11,3.6319829725476633e-12,4.466326790207103e-13,4.94310343218269e-14,4.973432346490872e-15,4.72686584975246e-16,4.0078719418956327e-17,3.1683635092922115e-18,2.337722439167737e-19],[8.418833622427279e-09,9.317537056455662e-09,5.156088164466774e-09,1.90216541836985e-09,5.263049956812075e-10,1.164975225830281e-10,2.1488922581884664e-11,3.3975495799023153e-12,4.700293937920532e-13,5.780051529827764e-14,6.397067186827943e-15,6.436317043763937e-16,5.936157078676705e-17,5.207872468522817e-18,4.1003055103555745e-19,3.025339791627207e-20],[1.0116923301489623e-09,1.119689638572182e-09,6.196077845827433e-10,2.2858346544738268e-10,6.324613970649349e-11,1.3999522423704144e-11,2.582326618421701e-12,4.082839744131899e-13,5.648349331636812e-14,6.945895432610489e-15,7.687363949230168e-16,7.734530553302028e-17,7.133487673468474e-18,6.073062695841059e-19,4.9474115363001037e-20,3.635554758001328e-21],[1.1347018549916384e-10,1.255830327107156e-10,6.949445810563553e-11,2.5637644423514785e-11,7.093610370205306e-12,1.5701694665249832e-12,2.896306235400588e-13,4.579263569802802e-14,6.335120147945946e-15,7.79043212752299e-16,8.622054228584455e-17,8.674955720015268e-18,8.000833311104416e-19,6.811473509378804e-20,5.384708998815697e-21,4.0942022014740717e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.14503851519181862, "-10": 5.591511280164184e-08, "-11": 5.548464933233763e-09, "-12": 5.057489849790582e-10, "-13": 4.261258424283646e-11, "-14": 3.318137233945013e-12, "-15": 2.177885849835998e-13, "-2": 0.0679806183839872, "-3": 0.021948600582016822, "-4": 0.005582377660113285, "-5": 0.0011662540799801176, "-6": 0.0002062679193229759, "-7": 3.1588078959952105e-05, "-8": 4.261989789553451e-06, "-9": 5.13653672994296e-07, "0": 0.2679158825822488, "1": 0.2204823417093095, "10": 3.5892113645722885e-06, "11": 5.413997351591614e-07, "12": 7.501628928570963e-08, "13": 9.608017719105098e-09, "14": 1.137275362859678e-09, "15": 1.1347018549916384e-10, "2": 0.15305658642220263, "3": 0.07511888140631647, "4": 0.029042691093391394, "5": 0.009223296755569774, "6": 0.0024797052319627108, "7": 0.0005772539988023866, "8": 0.00011839449369667898, "9": 2.1690265210817457e-05} |
| Raw goal margin distribution | {"-1": 0.15002118512238857, "-10": 1.4718411422560203e-08, "-11": 1.2353765644467533e-09, "-12": 9.518069361095999e-11, "-13": 6.7525696427258734e-12, "-14": 4.109476708905798e-13, "-2": 0.06303193487115843, "-3": 0.01775256216212948, "-4": 0.0038916898995414043, "-5": 0.0006960096097389463, "-6": 0.00010493778604151291, "-7": 1.3661694307648545e-05, "-8": 1.5640485647199648e-06, "-9": 1.5972533235746455e-07, "0": 0.29407179453336457, "1": 0.23437432822067608, "10": 9.696490675568814e-07, "11": 1.2371671177515178e-07, "12": 1.4489494689639917e-08, "13": 1.5626035667149622e-09, "14": 1.445578323056525e-10, "2": 0.1456502947538003, "3": 0.06235727605850541, "4": 0.02077971972086035, "5": 0.005649266447637139, "6": 0.001294744529274628, "7": 0.0002562312618331746, "8": 4.4591609744657015e-05, "9": 6.922326532845256e-06} |
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
| Totals anchor scale | 1.1869 |
| Totals anchor target over 2 5 | 0.5262 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.02 |
| Totals anchor reference last update utc | 2026-11-05T16:49:14Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4266 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.82, "draw": 3.65, "home": 1.94}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.02}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.77, "draw": 3.71, "home": 2.01}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.86, "under": 2.03}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.94 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.82 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:14Z |
| Market reference home last update utc | 2026-11-05T16:49:14Z |
| Market reference draw last update utc | 2026-11-05T16:49:14Z |
| Market reference away last update utc | 2026-11-05T16:49:14Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:14Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:14Z |
| Market best over 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market best under 2 5 last update utc | 2026-11-05T16:49:11Z |
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
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,458.4916 |
| Elo away rating | 1,419.5564 |
| Elo rating diff | 98.9351 |
| Elo home expectancy | 0.6387 |
| Research p home | 0.4826 |
| Research p draw | 0.2697 |
| Research p away | 0.2477 |
| Research p over 1 5 | 0.6805 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4174209977591858, 0.9324455863032532], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:22.322317+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-05T16:50:21.944578+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:22.323037+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87aykur+Rizespor%22+%22Erzurum+BB%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:22.359101+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87aykur+Rizespor_vs_Erzurum+BB&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.4174209977591858, 0.9324455863032532], "h2h": [], "margin_distribution": {"-1": 0.16218289446196377, "-10": 1.4718411422560205e-08, "-11": 1.2353765644467533e-09, "-12": 9.518069361096e-11, "-13": 6.752569642725874e-12, "-14": 4.1094767089057985e-13, "-2": 0.06303193487115843, "-3": 0.017752562162129483, "-4": 0.0038916898995414047, "-5": 0.0006960096097389463, "-6": 0.00010493778604151293, "-7": 1.3661694307648547e-05, "-8": 1.564048564719965e-06, "-9": 1.5972533235746455e-07, "0": 0.26974837585421424, "1": 0.24653603756025128, "10": 9.696490675568816e-07, "11": 1.237167117751518e-07, "12": 1.4489494689639919e-08, "13": 1.5626035667149622e-09, "14": 1.445578323056525e-10, "2": 0.14565029475380034, "3": 0.06235727605850542, "4": 0.020779719720860353, "5": 0.005649266447637139, "6": 0.0012947445292746283, "7": 0.0002562312618331746, "8": 4.459160974465702e-05, "9": 6.922326532845257e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:22.359310+00:00", "p_over_1_5": 0.6804834045693013, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Çorum FK vs Fenerbahce

The model's most likely 1X2 outcome is **Fenerbahce win** at **52.0%**. Expected goals are 1.87 for Çorum FK and 2.27 for Fenerbahce (4.14 combined). The most likely exact score is 1-2 at 8.5%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 77.7%; Under 3.5 goals: 40.6%; Double Chance 1X: 48.0%; Double Chance X2: 75.1%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 60.5%; BTTS Yes (both teams score): 76.7%; BTTS No (at least one team does not score): 23.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çorum FK win | 24.9% | 4.02 |
| Draw | 23.1% | 4.33 |
| Fenerbahce win | 52.0% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çorum FK expected goals | 1.87 |
| Fenerbahce expected goals | 2.27 |
| Expected total goals | 4.14 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 92.5% |
| Under 1.5 | 7.5% |
| Over 2.5 | 77.7% |
| Under 2.5 | 22.3% |
| Over 3.5 | 59.4% |
| Under 3.5 | 40.6% |
| Over 4.5 | 39.5% |
| Under 4.5 | 60.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.52% |
| 2 | 1-1 | 8.05% |
| 3 | 2-2 | 7.79% |
| 4 | 1-3 | 6.43% |
| 5 | 2-3 | 6.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çorum FK win | 24.9% | 21.9% | 4.24 | +5.6% |
| Draw | 23.1% | 23.9% | 4.11 | -5.0% |
| Fenerbahce win | 52.0% | 54.2% | 1.81 | -5.9% |
| Over 2.5 | 77.7% | 59.2% | 1.65 | +28.2% |
| Under 2.5 | 22.3% | 40.8% | 2.35 | -47.6% |

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
| Market best home last update utc | 2026-11-05T16:49:14Z |
| Market best draw last update utc | 2026-11-05T16:49:11Z |
| Market best away last update utc | 2026-11-05T16:49:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Corum |
| Matched away-team name | Fenerbahce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8740 |
| Dc lambda away | 2.2662 |
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
| P btts yes | 76.7% |
| P btts no | 23.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.04 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.26 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.48 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.47 |
| Fair Over 4.5 odds | 2.53 |
| Fair Under 4.5 odds | 1.65 |
| Score matrix json | [[0.02436521607478035,0.032850870066994026,0.045437682656847736,0.03432332105321299,0.01944570507180766,0.00881349319673317,0.003328826855854093,0.0010776743589700265,0.0003052754964400336,7.686768823667225e-05,1.7419601007543694e-05,3.5887226979114258e-06,6.77724270522428e-07,1.1814193230000542e-07,1.9123633741266145e-08,2.8891729605255817e-09,4.0921160575283656e-10,5.4549830352054945e-11],[0.018175085579566992,0.08048291058998049,0.0851500544983258,0.06432178067523348,0.03644118163172332,0.016516454672438115,0.006238209600875166,0.0020195578874645068,0.0005720851865440553,0.0001440497723430124,3.264426987470712e-05,6.725253477698735e-06,1.2700528547119e-06,2.2139755783445323e-07,3.5837621112251593e-08,5.414299776284188e-09,7.668610829991391e-10,1.0222618663084235e-10],[0.021794954571636972,0.049391287981303926,0.0779307454081067,0.060269393262071126,0.034145321905594515,0.015475888439320353,0.005845191220446704,0.0018923221225742933,0.0005360427949175994,0.00013497437862437285,3.05876223913287e-05,6.3015504605052715e-06,1.1900372496018395e-06,2.0744911506351676e-07,3.3579786780110844e-08,5.0731891908157434e-09,7.185474609605887e-10,9.578575373782206e-11],[0.013614555592392481,0.030853032236938645,0.03495926076152944,0.036773033753019116,0.021329403636785732,0.009667253162022355,0.0036512891347109167,0.0011820682925409208,0.0003348474256883465,8.431383397887652e-05,1.9107031589218673e-05,3.936360994964522e-06,7.433751806395807e-07,1.2958629945025596e-07,2.097613337049355e-08,3.169046122214419e-09,4.4885178910862233e-10,5.983405310327507e-11],[0.006378407099993221,0.014454617966845204,0.01637838235252076,0.012372120296348937,0.009760512393786992,0.004529099447104283,0.0017106256890222576,0.0005537979362347238,0.00015687571900021747,3.9500955696197674e-05,8.951627184699794e-06,1.8441816002020466e-06,3.482706062620009e-07,6.071106521737815e-08,9.827299695005995e-09,1.4846952696299015e-09,2.102866611448453e-10,2.8032200283390568e-11],[0.002390622410384213,0.005417580455960416,0.006138605969164157,0.00463706182135232,0.0026271040741646305,0.0016580428422261109,0.0006411412824308267,0.00020756306965553594,5.879690706594361e-05,1.480492988900386e-05,3.3550634541922876e-06,6.911979422363801e-07,1.3053157366028278e-07,2.27544637386215e-08,3.6832648835581912e-09,5.564627231417146e-10,7.881528990808263e-11,1.0506448578662126e-11],[0.0007466696385995407,0.001692087727265042,0.0019172875986568447,0.0014483062064813519,0.0008205306037035883,0.0003718939923622259,0.00019559438666292412,6.482874147465317e-05,1.8364198862606303e-05,4.624064261129983e-06,1.0478961486927863e-06,2.1588374453807567e-07,4.0769283558706625e-08,7.106963919706703e-09,1.1504041991435922e-09,1.7380152489893353e-10,2.4616595149515087e-11,3.2815078320685154e-12],[0.0001998937467801592,0.00045299519117736553,0.0005132842986216562,0.0003877315202497299,0.00021966734448950064,9.956114417314273e-05,3.7603910631707795e-05,1.695209768803241e-05,4.916348981522081e-06,1.2379256939429935e-06,2.805362325855105e-07,5.779505196647114e-08,1.091449875928787e-08,1.902632131669554e-09,3.0797904962327534e-10,4.652906213424588e-11,6.590201587192126e-12,8.785048456917616e-13],[4.682502065727578e-05,0.00010611392065132933,0.00012023661706860335,9.08259349660287e-05,5.145697706473092e-05,2.332215343232613e-05,8.80869922389609e-06,2.85172816146256e-06,1.1248810792714612e-06,2.8998353937906496e-07,6.571548684000507e-08,1.353846503860196e-08,2.5567164461104226e-09,4.456907247158887e-10,7.214395444034684e-11,1.0899411966077497e-11,1.5437517702605404e-12,2.0578936664924548e-13],[9.749991215597304e-06,2.209523412227882e-05,2.503588773174121e-05,1.891194185580338e-05,1.0714465627990327e-05,4.856181330027023e-06,1.834163420501998e-06,5.937920396669619e-07,1.6820494816701262e-07,5.8977279092211804e-08,1.3683398542595028e-08,2.819003886088619e-09,5.32364162160309e-10,9.280253569259024e-11,1.5021945792618404e-11,2.2694954413846984e-12,3.214428095882604e-13,4.284983730768968e-14],[1.8271448604370897e-06,4.140638957919588e-06,4.691716390713545e-06,3.544091127737424e-06,2.007887019753901e-06,9.100466413051891e-07,3.4372156783185695e-07,1.1127641548131183e-07,3.152154701963147e-08,7.937055142971799e-09,2.504654763695067e-09,5.282803182201084e-10,9.97648532458207e-11,1.7391161938175968e-11,2.8151072592598032e-12,4.2530263256831266e-13,6.02382673457278e-14,8.030044158610486e-15],[3.112784474458201e-07,7.05412961042705e-07,7.992963369133491e-07,6.037830977368174e-07,3.420702800795409e-07,1.5503855865100737e-07,5.8557544234751404e-08,1.8957418537724847e-08,5.370115106808816e-09,1.3521829909014973e-09,3.0642899157013717e-10,8.790744169941508e-11,1.699627068462993e-11,2.962815923691588e-12,4.795909924986599e-13,7.245596450891949e-14,1.0262390652331094e-14,1.368024907459006e-15],[4.861122460172262e-08,1.1016178012832613e-07,1.248232059618965e-07,9.429061348655348e-08,5.3419873270908063e-08,2.421180861814488e-08,9.14471900730059e-09,2.9605112013628985e-09,8.386313724454824e-10,2.11165506679619e-10,4.785390269041363e-11,9.858686584977528e-12,2.5925449126541793e-12,4.626922021165654e-13,7.489598346629276e-14,1.1315184823679719e-14,1.602640276076025e-15,2.136394812519602e-16],[7.007481594800243e-09,1.5880213942857982e-08,1.7993710826016785e-08,1.359232860276539e-08,7.700665469949597e-09,3.4902186616064764e-09,1.3182438965137282e-09,4.2676826030865523e-10,1.2089170670729278e-10,3.0440261763363624e-11,6.898310937234692e-12,1.4211648720877105e-12,2.683846056950247e-13,6.514824540838423e-14,1.0796523435986667e-14,1.6311242936860484e-15,2.310263180921872e-16,3.07968940313989e-17],[9.3799967151797e-10,2.1256760022158134e-09,2.4085821155373597e-09,1.819426792932117e-09,1.0307871071173896e-09,4.671898047569668e-10,1.7645602420532565e-10,5.712587076658963e-11,1.618218751581607e-11,4.074638677059563e-12,9.233864271518525e-13,1.9023270559573268e-13,3.5925127818989205e-14,6.262523275709671e-15,1.4115939613723298e-15,2.18337220153071e-16,3.092446373933787e-17,4.1223763622385034e-18],[1.1718720157504887e-10,2.655672807984947e-10,3.009116169803763e-10,2.2730661940353994e-10,1.2877942303246625e-10,5.836746801335477e-11,2.20451971419321e-11,7.136911809191694e-12,2.0216907616527317e-12,5.090572187742195e-13,1.1536152373613625e-13,2.3766360579569747e-14,4.4882373876744264e-15,7.823964120279172e-16,1.2664650165114966e-16,2.6643447135154804e-17,3.863488949796129e-18,5.150212355064831e-19],[1.3725524742289359e-11,3.110450829400416e-11,3.5244205754511655e-11,2.662323689597959e-11,1.5083261084597897e-11,6.836276620608854e-12,2.5820387785816063e-12,8.35909197455011e-13,2.3679007773345937e-13,5.96232127537571e-14,1.3511692634237894e-14,2.7836296607880577e-15,5.256837989628205e-16,9.163800455368217e-17,1.4833443145444614e-17,2.2410167140376673e-18,4.4199116416818505e-19,6.032174687797789e-20],[1.5130343640755036e-12,3.428808064546903e-12,3.885147959175895e-12,2.9348147384433712e-12,1.6627045429457902e-12,7.535975231196803e-13,2.8463125998619473e-13,9.21465200597679e-14,2.6102573956897443e-14,6.57256982788203e-15,1.4894625638201927e-15,3.06853647690097e-16,5.79487973977336e-17,1.0101723070582008e-17,1.635165841599324e-18,2.470386642748491e-19,3.498962847574103e-20,6.4949959446036514e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.20484001149685618, "-10": 2.5474887291812666e-05, "-11": 5.088767593124707e-06, "-12": 9.3609145436893e-07, "-13": 1.5952962659246476e-07, "-14": 2.53163150316142e-08, "-15": 3.751819797262543e-09, "-16": 5.11437792383679e-10, "-17": 5.4549830352054945e-11, "-2": 0.15550989792022737, "-3": 0.09050919379147346, "-4": 0.04316220824973146, "-5": 0.017321955624413115, "-6": 0.005978426943732759, "-7": 0.0018058230950733897, "-8": 0.0004842214757592027, "-9": 0.00011662145868014101, "0": 0.2311841939998304, "1": 0.1179373847826351, "10": 2.6720651848048856e-06, "11": 4.4138926552400824e-07, "12": 6.714316413812922e-08, "13": 9.462355155435358e-09, "14": 1.2417459728094197e-09, "15": 1.521768578282289e-10, "16": 1.715433280683626e-11, "17": 1.5130343640755036e-12, "2": 0.0745929581446308, "3": 0.03590102626101474, "4": 0.014157683382260661, "5": 0.00469850652664622, "6": 0.0013409859024720487, "7": 0.0003349553058322356, "8": 7.427284819623614e-05, "9": 1.4792407886400415e-05} |
| Raw goal margin distribution | {"-1": 0.18428995317135585, "-10": 2.291918337509847e-05, "-11": 4.578249798874175e-06, "-12": 8.421804364739756e-07, "-13": 1.4352521853192947e-07, "-14": 2.2776519477587895e-08, "-15": 3.3754279239312177e-09, "-16": 4.601290837649479e-10, "-17": 4.9077255989315857e-11, "-2": 0.13990875901625735, "-3": 0.08142908684450947, "-4": 0.038832068398108835, "-5": 0.015584174046526015, "-6": 0.005378656315471804, "-7": 0.0016246584404821496, "-8": 0.00043564317556971956, "-9": 0.000104921704514102, "0": 0.21294128320214362, "1": 0.151268086451459, "10": 3.4272269825548377e-06, "11": 5.661318478367895e-07, "12": 8.611873136063024e-08, "13": 1.2136544831181933e-08, "14": 1.5926801964608523e-09, "15": 1.9518409814070486e-10, "16": 2.2002379506923546e-11, "17": 1.9406383600147508e-12, "2": 0.09567393801455094, "3": 0.04604714233876146, "4": 0.018158836383961575, "5": 0.006026368083160278, "6": 0.0017199666738345102, "7": 0.0004296182101493045, "8": 9.526336066083923e-05, "9": 1.897294262637173e-05} |
| Research history json | {"away": [{"away": "Goztep", "away_goals": 2.0, "away_xg": 1.4, "date": "2026-10-31T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 1.51, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 3.0, "away_xg": 0.96, "date": "2026-10-10T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.52, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 0.0, "away_xg": 1.33, "date": "2026-09-14T00:00:00+00:00", "home": "Gaziantep", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 2.0, "away_xg": 1.75, "date": "2026-09-05T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Konyaspor", "away_goals": 2.0, "away_xg": 2.15, "date": "2026-08-22T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 4.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 2.9, "date": "2026-08-15T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 2.0, "home_xg": 1.19, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 46.8% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.7% |
| Raw p btts yes | 76.5% |
| P home draw | 48.0% |
| P draw away | 75.1% |
| P home away | 76.9% |
| Raw p home draw | 53.2% |
| Raw p draw away | 68.1% |
| Raw p home away | 78.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7769 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.02, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.36, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.81, "draw": 4.11, "home": 4.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T16:49:11Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.65, "under": 2.35}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:14Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.79, "draw": 3.9, "home": 4.24}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.24 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.79 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:14Z |
| Market reference home last update utc | 2026-11-05T16:49:14Z |
| Market reference draw last update utc | 2026-11-05T16:49:14Z |
| Market reference away last update utc | 2026-11-05T16:49:14Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market best over 2 5 last update utc | 2026-11-05T16:49:11Z |
| Market best under 2 5 last update utc | 2026-11-05T16:49:11Z |
| Home probability edge | +3.0% |
| Draw probability edge | -0.8% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +18.5% |
| Under 2.5 probability edge | -18.5% |
| Raw edge prob home | 0.1006 |
| Raw ev home | 0.3544 |
| Raw edge prob draw | -0.0261 |
| Raw ev draw | -0.1248 |
| Raw edge prob away | -0.0745 |
| Raw ev away | -0.1536 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,445.1258 |
| Elo away rating | 1,661.7220 |
| Elo rating diff | -156.5962 |
| Elo home expectancy | 0.2888 |
| Research p home | 0.3260 |
| Research p draw | 0.1999 |
| Research p away | 0.4741 |
| Research p over 1 5 | 0.9182 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.8739964170574437, 2.26617990044263], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:22.322317+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-05T16:50:21.944578+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:22.362736+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87orum+FK%22+%22Fenerbahce%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:22.398964+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87orum+FK_vs_Fenerbahce&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 1.0089728918892988, "goals_for": 2.3331960885564245, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.4847509690034097, "results": "LLWWWDLWWL", "xg_against": 1.3380003484001706, "xg_for": 1.9676008712062978, "xg_matches": 10}, "venue": {"goals_against": 0.8151944568095735, "goals_for": 1.425370020202056, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.384791003310632, "results": "LWDWL", "xg_against": 1.2819506533747527, "xg_for": 1.2552734770676013, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.8739964170574437, 2.26617990044263], "h2h": [], "margin_distribution": {"-1": 0.19081244826985075, "-10": 2.291918337509847e-05, "-11": 4.578249798874175e-06, "-12": 8.421804364739756e-07, "-13": 1.4352521853192947e-07, "-14": 2.2776519477587895e-08, "-15": 3.3754279239312177e-09, "-16": 4.601290837649479e-10, "-17": 4.9077255989315857e-11, "-2": 0.13990875901625735, "-3": 0.08142908684450947, "-4": 0.038832068398108835, "-5": 0.015584174046526015, "-6": 0.005378656315471804, "-7": 0.0016246584404821496, "-8": 0.00043564317556971956, "-9": 0.000104921704514102, "0": 0.19989629300515388, "1": 0.1577905815499539, "10": 3.4272269825548377e-06, "11": 5.661318478367895e-07, "12": 8.611873136063024e-08, "13": 1.2136544831181933e-08, "14": 1.5926801964608523e-09, "15": 1.9518409814070486e-10, "16": 2.2002379506923546e-11, "17": 1.9406383600147508e-12, "2": 0.09567393801455094, "3": 0.04604714233876146, "4": 0.018158836383961575, "5": 0.006026368083160278, "6": 0.0017199666738345102, "7": 0.0004296182101493045, "8": 9.526336066083923e-05, "9": 1.897294262637173e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:22.399171+00:00", "p_over_1_5": 0.9181681654420836, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
