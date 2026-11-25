# Primeira Liga — football model report

Fixtures in this report: **1**.

> Each match shows the two models the shortlists use, side by side, and the master's verdict on them: **Research** (the value shortlist's model, independent of bookmaker odds) and **Cagey** (the cagey tier's market view, built from Pinnacle's prices). Probabilities are model estimates, not guarantees. No probability here is blended or averaged. The production model (70% Pinnacle blend) is kept only as a benchmark at the end of this report.

## Quick reference

- **Research:** The value shortlist's model: team form, goal rates and xG, never bookmaker odds. Live research v5 (C6 grid) for domestic leagues and v6 (CE3n) for UCL/UEL, exactly as the forecast carries it.
- **Cagey:** The cagey tier's market view: Pinnacle's 1X2, O/U 2.5 and main AH line with the margin removed, plus the narrow-margin correction (D_pow2 for domestic leagues, D for UCL/UEL, D where D_pow2's power fit fails). Blank without Pinnacle 1X2 and O/U 2.5.
- **No-loss:** The chance a bet does not lose: a win, a half win or a refund (push) on that exact line.
- **Gap:** Research minus cagey no-loss on the same Pinnacle offer, in percentage points (the master's g). +4 or more: research too optimistic; -4 or less: research too pessimistic; -8 or less with cagey no-loss of 85% or more: flagged for inspection.
- **Cagey tier:** The master's market classes from the cagey no-loss: safe (75% or more), risky (below 50%), in between otherwise; fair price when the Pinnacle price is within its 2.70% margin of the cagey fair odds.
- **Best offer:** The fixture's master pick, or else the Pinnacle offer the master's own rule would choose for it (safe first, then chance of profit), shown with both views and the master's labels.
- **Expected goals:** A view's average goal expectation for each team, from its score grid. It is not a prediction that the team will score exactly that many goals.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-27 — CS Maritimo vs Nacional

Research leans **Nacional win** at **38.6%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle O/U 2.5 quote). Only one view is available.

**Fixture source:** The Odds API

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| CS Maritimo win | 33.1% | — |
| Draw | 28.3% | — |
| Nacional win | 38.6% | — |
| CS Maritimo expected goals | 1.21 | — |
| Nacional expected goals | 1.32 | — |
| Expected total goals | 2.53 | — |
| Most likely score | 1-1 | — |
| Most likely score probability | 13.4% | — |
| Over 1.5 | 72.2% | — |
| Under 1.5 | 27.8% | — |
| Over 2.5 | 46.2% | — |
| Under 2.5 | 53.8% | — |
| Over 3.5 | 25.0% | — |
| Under 3.5 | 75.0% | — |
| BTTS Yes | 52.1% | — |
| BTTS No | 47.9% | — |
| Double Chance 1X | 61.4% | — |
| Double Chance X2 | 66.9% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 1-1 (13.45%) | — |
| 2 | 0-1 (10.17%) | — |
| 3 | 1-0 (9.18%) | — |
| 4 | 0-0 (8.46%) | — |
| 5 | 1-2 (8.33%) | — |

### No-loss on the quoted Pinnacle Asian handicap lines

| Line | Pinnacle odds | Research no-loss | Cagey no-loss |
| --- | --- | --- | --- |
| CS Maritimo -0.25 | 1.79 | 33.1% | — |
| Nacional +0.25 | 2.08 | 66.9% | — |

_No-loss: win, half win or refund, from each view's own goal-margin distribution._

### On the lists

- **Value shortlist:** no
- **Cagey tier:** no
- **Master shortlist:** no

### The master's verdict on every Pinnacle offer

| Offer | Pinnacle odds | Research no-loss | Cagey no-loss | Gap (points) | Gap label | Cagey tier | Master labels | Master check |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Home win | 2.08 | 33.1% | — | — | one view missing (no cagey view) | risky, below fair price (Pinnacle stand-in: no cagey view) | one view missing | offered odds outside (1.20, 2.00] |
| Away win | 3.68 | 38.6% | — | — | one view missing (no cagey view) | risky, below fair price (Pinnacle stand-in: no cagey view) | one view missing | offered odds outside (1.20, 2.00] |
| Asian Handicap Away +0.25 | 2.08 | 66.9% | — | — | one view missing (no cagey view) | no market view | one view missing | offered odds outside (1.20, 2.00] |
| Asian Handicap Home -0.25 | 1.79 | 33.1% | — | — | one view missing (no cagey view) | no market view | one view missing | eligible |

_Best offer: none (no offer passes the master checks with a market view). Gap = research minus cagey no-loss, in points; the cagey tier decides safety (safe at 75% or more, risky below 50%) and fair price; the research view only labels. No probability is blended._

_Views the master could not use: cagey: cagey settlement probabilities unavailable._

### Safest Asian handicap (cagey tier)

_no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle O/U 2.5 quote)._


---

## Benchmark (70% Pinnacle blend), display only

The production forecasting model blends 70% of Pinnacle's prices into its score grid, so it is neither independent research nor the cagey tier's market view. It is shown for comparison only: no list, probability or stake reads it, and its EV is not a recommendation.

- **Benchmark EV:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Probability edge:** Model probability minus the de-vigged market probability.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,628 |
| Training data through | 2026-11-08 |
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
| Training sha256 | 7c73b44b6e1c6ee16fc6ee45d20634ecf277c8dff8e4ce224e38cad97bc36515 |
| Training as of utc | 2026-11-25T14:22:12.189440+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history.'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-25', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'shot_matches': 1628, 'tune_start_date': '2025-11-26', 'audit_start_date': '2026-05-27', 'training_shot_matches': 1323, 'tuning_matches': 207, 'audit_matches': 92, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8715404267382761, 'audit_candidate_poisson_score': 0.8661191163092895, 'audit_gain': 0.0054213104289866365, 'audit_gain_lower95': -0.0037336337287461694, 'audit_baseline_briers': [0.5256881914875379, 0.20162320318102928, 0.22188757756158048, 0.2543685952254264], 'audit_candidate_briers': [0.5292212744115292, 0.20093634828065535, 0.21876000763591966, 0.2532891639569504], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1446.855 |
| Base scoring parameter | 0.083 |
| Home-advantage parameter | 0.174 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1628, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-08'} |
| Training data health | {'training_end': '2026-11-08', 'days_since_latest_result': 17, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 27.00 |
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
| Legacy comparison status | {'None': 1} |
| Goal market validation | SKIPPED: not required by 48h-ah-price-edge-cagey-v28 |

</details>

### 2026-11-27 — CS Maritimo vs Nacional

The model's most likely 1X2 outcome is **CS Maritimo win** at **42.7%**. Expected goals are 1.21 for CS Maritimo and 1.36 for Nacional (2.57 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 46.7%; Under 3.5 goals: 74.5%; Double Chance 1X: 69.8%; Double Chance X2: 57.3%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 88.4%; BTTS Yes (both teams score): 52.1%; BTTS No (at least one team does not score): 47.9%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| CS Maritimo win | 42.7% | 2.34 |
| Draw | 27.2% | 3.68 |
| Nacional win | 30.2% | 3.31 |

| Measure | Benchmark estimate |
| --- | --- |
| CS Maritimo expected goals | 1.21 |
| Nacional expected goals | 1.36 |
| Expected total goals | 2.57 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 46.7% |
| Under 2.5 | 53.3% |
| Over 3.5 | 25.5% |
| Under 3.5 | 74.5% |
| Over 4.5 | 11.6% |
| Under 4.5 | 88.4% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 1-1 | 12.89% |
| 2 | 1-0 | 12.47% |
| 3 | 2-1 | 9.60% |
| 4 | 0-1 | 8.14% |
| 5 | 0-0 | 7.57% |

| Selection | Benchmark | Market fair | Best quoted odds | Benchmark EV (display only) |
| --- | --- | --- | --- | --- |
| CS Maritimo win | 42.7% | 46.4% | 2.08 | -11.3% |
| Draw | 27.2% | 28.0% | 3.37 | -8.4% |
| Nacional win | 30.2% | 25.5% | 3.68 | +11.0% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T20:15:00+00:00 |
| Fixture id | 1,640,277,271 |
| Odds source | — |
| Odds schedule provider | — |
| Odds provider | — |
| Odds match method | — |
| Odds event id | 1640277271.00 |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-25T14:21:43Z |
| Market best draw last update utc | 2026-11-25T14:21:43Z |
| Market best away last update utc | 2026-11-25T14:21:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 0.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Maritimo |
| Matched away-team name | Nacional |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2090 |
| Dc lambda away | 1.3610 |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 52.1% |
| P btts no | 47.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.21 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.55 |
| Fair Over 2.5 odds | 2.14 |
| Fair Under 2.5 odds | 1.87 |
| Fair Over 3.5 odds | 3.92 |
| Fair Under 3.5 odds | 1.34 |
| Fair Over 4.5 odds | 8.65 |
| Fair Under 4.5 odds | 1.13 |
| Score matrix json | [[0.07568612357779599,0.08135888294671065,0.0522084244874341,0.023685123219073987,0.008058829596137391,0.002193604275861366,0.0004975804966128512,9.674346202104361e-05,1.6458412898188453e-05,2.488867402219187e-06,3.387334420234397e-07,4.1910390332836615e-08,4.753316964351433e-09,4.976336486744389e-10,4.83768981286931e-11],[0.12465161949797697,0.12891942509960697,0.063121293353006,0.028635907432393384,0.009743326905835072,0.0026521225330287425,0.0006015872879097065,0.00011696526961248298,1.989863358013217e-05,3.009103050984106e-06,4.0953721879849464e-07,5.067071202990793e-08,5.746879310232038e-09,6.016515500839578e-10,5.848888198157923e-11],[0.07055239515275952,0.09602140970540719,0.05582469777778972,0.01731076479720891,0.005889963180228481,0.001603241297347681,0.0003636670523042452,7.070697083666995e-05,1.2028973291827725e-05,1.8190404927494878e-06,2.475703794985795e-07,3.0631080231269214e-08,3.4740605406775554e-09,3.6370589959366486e-10,3.535726191409205e-11],[0.028433204506208877,0.03869743009031673,0.02633349145130559,0.01020646823254156,0.0023737043551090064,0.0006461196332397408,0.00014656085945697798,2.8495499797854132e-05,4.847776703621731e-06,7.330885113600311e-07,9.977293066694035e-08,1.2344581166606991e-08,1.4000754135442272e-09,1.4657651523907e-10,1.4249271858258783e-11],[0.008594114169421041,0.011696540647986012,0.007959462745839073,0.003610927886517664,0.0010496563140485228,0.00019529370648159718,4.429893783750944e-05,8.612943311542527e-06,1.465270875454332e-06,2.2158059467209387e-07,3.015699327812924e-08,3.731226984856333e-09,4.231815639060657e-10,4.430366989571558e-11,4.306931677512926e-12],[0.0020780998734325597,0.002828282142988564,0.0019246379788126133,0.0008731404582273508,0.0002970848030328569,6.90873812186888e-05,1.0711705162223465e-05,2.082652854355099e-06,3.5430984052556457e-07,5.357929818777468e-08,7.2921120989260435e-09,9.022293830546645e-10,1.0232742282168576e-10,1.0712849397611243e-11,1.0414376627399683e-12],[0.000418745802730722,0.0005699106628395393,0.00038782259010135923,0.00017594144860475498,5.9863828449980084e-05,1.6294866207401657e-05,3.1578234623178752e-06,4.1966324740005706e-07,7.139491247896779e-08,1.079645233428024e-08,1.4693910401059905e-09,1.8180298843405445e-10,2.061940302226932e-11,2.158683890936503e-12,2.0985403813038038e-13],[7.232488110055232e-05,9.843375302871439e-05,6.698388983071511e-05,3.038823139961291e-05,1.0339552651356092e-05,2.8144145047290012e-06,6.384003634327218e-07,1.0604333661241785e-07,1.233117686804899e-08,1.8647401986897823e-09,2.5379008356108295e-10,3.1400624045594494e-11,3.5613392712833663e-12,3.7284327324006326e-13,3.624554146518971e-14],[1.0930324180171438e-05,1.4876109224140345e-05,1.0123150146361094e-05,4.592516647183225e-06,1.5625972782471688e-06,4.2533720686378975e-07,9.648025441421188e-08,1.8758439875034403e-08,2.7264342400809036e-09,2.818147029531855e-10,3.835482125686135e-11,4.745517656653473e-12,5.38218551601676e-13,5.6347107425510964e-14,5.477720976126762e-15],[1.4683373118709268e-06,1.998398754622293e-06,1.359904686133517e-06,6.169408553024025e-07,2.0991325135996906e-07,5.7138148939629146e-08,1.29607827800918e-08,2.519935980578429e-09,4.287023223992103e-10,5.538620711544364e-11,5.152437769755734e-12,6.374944168670842e-13,7.230219051430489e-14,7.569451636116012e-15,7.358557679246076e-16],[1.7752566010889043e-07,2.4161141667310067e-07,1.644158839656645e-07,7.458969522891889e-08,2.5379038053456276e-08,6.908145373615225e-09,1.5669911129834403e-09,3.04666574068271e-10,5.1831184945618396e-11,7.837994308900972e-12,9.11366881242096e-13,7.707467232162084e-14,8.741515995405711e-15,9.151656690189314e-16,8.89668061212039e-17],[1.9512088290927334e-08,2.6555841512319373e-08,1.8071174851011007e-08,8.198255497302839e-09,2.789444810029714e-09,7.592837135423844e-10,1.7223013804808365e-10,3.348632016840898e-11,5.696836481339986e-12,8.614846827509571e-13,1.1724757678071094e-13,1.2393657469520867e-14,9.607919880105711e-16,1.0058711131545712e-16,9.778463434153482e-18],[1.9658836369690617e-09,2.6755564815318527e-09,1.8207085992393774e-09,8.259913594862757e-10,2.810423890309829e-10,7.649941954004645e-11,1.7352546028560362e-11,3.373816677120706e-12,5.739681706115539e-13,8.679638058562212e-14,1.1812938176107382e-14,1.4615765333972208e-15,1.4162131220931768e-16,1.0134361493074444e-17,9.852006086319846e-19],[1.828309672908544e-10,2.488319096617427e-10,1.693294089709903e-10,7.681878845158744e-11,2.6137483862212888e-11,7.114593462540579e-12,1.6138202260293267e-12,3.1377145368126514e-13,5.338014613564031e-14,8.072230686186933e-15,1.0986260186867633e-15,1.3592943465495315e-16,1.5416599143288326e-17,1.3789023968329212e-18,9.162555548274244e-20],[1.5789087179595355e-11,2.148885811266492e-11,1.4623107014793208e-11,6.633988573519286e-12,2.257205206923332e-12,6.144086972352385e-13,1.3936779211169176e-13,2.709696781705797e-14,4.6098524417604205e-15,6.97109225677579e-16,9.487617028914968e-17,1.173872088433414e-17,1.331361046178912e-18,1.393826795229149e-19,1.157628131907138e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.16437108314514787, "-10": 3.930290980409418e-07, "-11": 4.803522481452058e-08, "-12": 5.390325776349483e-09, "-13": 5.561225306560182e-10, "-14": 4.83768981286931e-11, "-2": 0.0874268696226414, "-3": 0.03518723058992695, "-4": 0.011104635032779416, "-5": 0.002870975369439546, "-6": 0.000627338908248907, "-7": 0.00011856474477392931, "-8": 1.9727865014105086e-05, "-9": 2.9304811217700535e-06, "0": 0.2717587250325447, "1": 0.25093148580590996, "10": 2.059812862141077e-07, "11": 2.2363608170003696e-08, "12": 2.2293386536455976e-09, "13": 2.0431982540351933e-10, "14": 1.5789087179595355e-11, "2": 0.11814520574299239, "3": 0.04224110274270458, "4": 0.011842228470397332, "5": 0.0027198039398047625, "6": 0.0005279458027537943, "7": 8.863835229120188e-05, "8": 1.3101625370606983e-05, "9": 1.7288726466470842e-06} |
| Raw goal margin distribution | {"-1": 0.2231630187837438, "-10": 5.336069965008181e-07, "-11": 6.521637244489166e-08, "-12": 7.318327223138992e-09, "-13": 7.55035377148792e-10, "-14": 6.568025481866208e-11, "-2": 0.11869754566606316, "-3": 0.04777293214131622, "-4": 0.015076519719824738, "-5": 0.0038978603659388022, "-6": 0.0008517242929019228, "-7": 0.00016097275663572367, "-8": 2.6784090160300544e-05, "-9": 3.97865002231253e-06, "0": 0.2521942155120794, "1": 0.1989476281618051, "10": 1.6330947153324307e-07, "11": 1.7730683689505393e-08, "12": 1.7675009418916756e-09, "13": 1.6199220484393646e-10, "14": 1.251816381324945e-11, "2": 0.09366982539384154, "3": 0.03349028590258428, "4": 0.009388950369337276, "5": 0.0021563596977535863, "6": 0.00041857467554744693, "7": 7.027571648041382e-05, "8": 1.038744613564712e-05, "9": 1.3707132500315317e-06} |
| Research history json | {"away": [{"away": "Academico Viseu", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-11-08T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 1.13, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 0.0, "away_xg": 1.67, "date": "2026-10-25T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.21, "date": "2026-10-11T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-12T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.08, "date": "2026-09-05T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 3.0, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 2.1, "date": "2026-08-30T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.42, "date": "2026-08-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 3.14, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-08-16T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 2.08, "source": "pipeline training history"}], "h2h": [], "home": [{"away": "Santa Clara", "away_goals": 2.0, "away_xg": 0.82, "date": "2026-11-01T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 2.06, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 0.0, "away_xg": 0.52, "date": "2026-10-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 5.0, "home_xg": 1.78, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 2.0, "away_xg": 2.13, "date": "2026-10-10T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 0.19, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.2, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-09-14T00:00:00+00:00", "home": "Moreirense", "home_goals": 3.0, "home_xg": 1.99, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 3.0, "away_xg": 1.31, "date": "2026-09-05T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 0.13, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-08-29T00:00:00+00:00", "home": "Arouca", "home_goals": 2.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.84, "date": "2026-08-22T00:00:00+00:00", "home": "Maritimo", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 2.0, "away_xg": 1.61, "date": "2026-08-16T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.65, "date": "2026-08-08T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}], "teams": {"away": "Nacional", "home": "Maritimo"}} |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 41.0% |
| Raw p over 1 5 | 72.0% |
| Raw p under 3 5 | 74.3% |
| Raw p btts yes | 51.5% |
| P home draw | 69.8% |
| P draw away | 57.3% |
| P home away | 72.8% |
| Raw p home draw | 59.0% |
| Raw p draw away | 66.2% |
| Raw p home away | 74.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4666 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-25T14:21:43Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.7937, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-25T14:21:43Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.08, "price": 1.7937, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-25T14:21:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.68, "draw": 3.37, "home": 2.08}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.37 |
| Reference away odds | 3.68 |
| Market reference 1x2 last update utc | 2026-11-25T14:21:43Z |
| Market reference home last update utc | 2026-11-25T14:21:43Z |
| Market reference draw last update utc | 2026-11-25T14:21:43Z |
| Market reference away last update utc | 2026-11-25T14:21:43Z |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Home probability edge | -3.8% |
| Draw probability edge | -0.8% |
| Away probability edge | +4.6% |
| Raw edge prob home | -0.1262 |
| Raw ev home | -0.2966 |
| Raw edge prob draw | -0.0279 |
| Raw ev draw | -0.1501 |
| Raw edge prob away | 0.1542 |
| Raw ev away | 0.5075 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-08 |
| Elo home rating | 1,397.7708 |
| Elo away rating | 1,372.3069 |
| Elo rating diff | 85.4639 |
| Elo home expectancy | 0.6206 |
| Research p home | 0.3314 |
| Research p draw | 0.2826 |
| Research p away | 0.3860 |
| Research p over 1 5 | 0.7219 |
| Research v4 p home | 0.3422 |
| Research v4 p draw | 0.2674 |
| Research v4 p away | 0.3904 |
| Research v4 p over 1 5 | 0.7201 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.2090250562569358, 1.360994329072774], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-25T14:22:43.816191+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 4.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-08", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-25T14:22:43.474182+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-25T14:22:43.544946+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-25T14:22:43.746870+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22CS+Maritimo%22+%22Nacional%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-25T14:22:19.682452+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-25T14:22:19.743551+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-25T14:22:43.815744+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=CS+Maritimo_vs_Nacional&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 1.5507048527234875, "goals_for": 0.8473887254235924, "last_match": "2026-11-08T00:00:00+00:00", "matches": 10, "points_per_game": 1.0589134132875462, "results": "WLWLLLLLLW", "xg_against": 1.4473966787066475, "xg_for": 0.943443703024997, "xg_matches": 10}, "venue": {"goals_against": 1.7599865214626136, "goals_for": 0.5295057548750894, "last_match": "2026-11-01T00:00:00+00:00", "matches": 4, "points_per_game": 0.0, "results": "LLLL", "xg_against": 1.9738427187746768, "xg_for": 0.5203791930565782, "xg_matches": 4}}, "home": {"all": {"goals_against": 2.3662591888570916, "goals_for": 0.7131841570421359, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.49878383320263503, "results": "LLLDLLLDWW", "xg_against": 1.4454419451949967, "xg_for": 0.932195130990825, "xg_matches": 10}, "venue": {"goals_against": 1.8988119457434338, "goals_for": 0.7157020266306037, "last_match": "2026-11-01T00:00:00+00:00", "matches": 5, "points_per_game": 0.6169046207669643, "results": "LLLDW", "xg_against": 1.3603430415604811, "xg_for": 1.0106319966707003, "xg_matches": 5}}}, "goal_rates": [1.2172591184825567, 1.3190413351403418], "h2h": [], "margin_distribution": {"-1": 0.21054628698761355, "-10": 3.996564220043523e-07, "-11": 4.73534110808989e-08, "-12": 5.151378738912966e-09, "-13": 5.153303987100409e-10, "-14": 4.3557533176895624e-11, "-2": 0.11327111866091971, "-3": 0.04429654110895813, "-4": 0.013571197794811963, "-5": 0.0034045155088897293, "-6": 0.0007216157192304975, "-7": 0.00013226630593550216, "-8": 2.134041947375439e-05, "-9": 3.0736010790645997e-06, "0": 0.2826457001627001, "1": 0.19029940501427203, "10": 1.7549194295592668e-07, "11": 1.9188732391046684e-08, "12": 1.9263851860403235e-09, "13": 1.7784024236162248e-10, "14": 1.3871779827950933e-11, "2": 0.09455674779405009, "3": 0.03412461685063924, "4": 0.009648077414564957, "5": 0.0022335853239889665, "6": 0.0004368957768094378, "7": 7.390021759009242e-05, "8": 1.1003328422440056e-05, "9": 1.4624911784012962e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-25T14:22:43.816191+00:00", "p_over_1_5": 0.7218859298999808, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.2139248888421603, "-10": 4.0209766521260964e-07, "-11": 4.7642662514941435e-08, "-12": 5.182845187760361e-09, "-13": 5.184782196046737e-10, "-14": 4.382359804206971e-11, "-2": 0.11396301883791644, "-3": 0.04456712009675271, "-4": 0.013654095485479231, "-5": 0.0034253114974085726, "-6": 0.0007260236040449296, "-7": 0.00013307423545513044, "-8": 2.1470774326656264e-05, "-9": 3.092375724850418e-06, "0": 0.26735129771721133, "1": 0.19741763557832778, "10": 1.801266047893027e-07, "11": 1.969549802453211e-08, "12": 1.977260136466761e-09, "13": 1.8253692170671778e-10, "14": 1.4238127179554109e-11, "2": 0.09705394819372488, "3": 0.0350258323516606, "4": 0.00990287872000136, "5": 0.0022925732893525974, "6": 0.0004484339941648087, "7": 7.585188848833418e-05, "8": 1.1293921286252561e-05, "9": 1.5011149005620783e-06}, "p_over_1_5": 0.7200710176708752, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
