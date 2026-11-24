# Eredivisie — football model report

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

## 2026-11-27 — FC Groningen vs Willem II Tilburg

Research leans **FC Groningen win** at **66.0%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote). Only one view is available.

**Fixture source:** football-data.org

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| FC Groningen win | 66.0% | — |
| Draw | 20.1% | — |
| Willem II Tilburg win | 13.9% | — |
| FC Groningen expected goals | 2.33 | — |
| Willem II Tilburg expected goals | 1.05 | — |
| Expected total goals | 3.39 | — |
| Most likely score | 2-1 | — |
| Most likely score probability | 10.0% | — |
| Over 1.5 | 85.4% | — |
| Under 1.5 | 14.6% | — |
| Over 2.5 | 65.5% | — |
| Under 2.5 | 34.5% | — |
| Over 3.5 | 44.0% | — |
| Under 3.5 | 56.0% | — |
| BTTS Yes | 59.8% | — |
| BTTS No | 40.2% | — |
| Double Chance 1X | 86.1% | — |
| Double Chance X2 | 34.0% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 2-1 (10.00%) | — |
| 2 | 2-0 (9.19%) | — |
| 3 | 1-1 (9.02%) | — |
| 4 | 1-0 (7.87%) | — |
| 5 | 3-1 (7.64%) | — |

### No-loss on the quoted Pinnacle Asian handicap lines

_No Pinnacle Asian handicap quotes in this forecast._

### On the lists

- **Value shortlist:** no
- **Cagey tier:** no
- **Master shortlist:** no

### The master's verdict on every Pinnacle offer

_No Pinnacle offer of this match in the run's decision rows._

### Safest Asian handicap (cagey tier)

_no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)._


---

## Benchmark (70% Pinnacle blend), display only

The production forecasting model blends 70% of Pinnacle's prices into its score grid, so it is neither independent research nor the cagey tier's market view. It is shown for comparison only: no list, probability or stake reads it, and its EV is not a recommendation.

- **Benchmark EV:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Probability edge:** Model probability minus the de-vigged market probability.

### Model context

| Item | Value |
| --- | --- |
| League | Eredivisie |
| Training matches | 1,647 |
| Training data through | 2026-11-22 |
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
| Training sha256 | 6a6942c4484010b7ee31ba0d63440397e3d2574de9f7102f07acd6e30191f1e0 |
| Training as of utc | 2026-11-24T15:49:46.845585+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1647, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1341, 'tuning_matches': 189, 'audit_matches': 111, 'audit_matchdays': 39, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6308885479009532, 'audit_candidate_poisson_score': 0.6224747475142083, 'audit_gain': 0.008413800386744885, 'audit_gain_lower95': -0.004700720782241717, 'audit_baseline_briers': [0.6284532874594683, 0.1053318588745377, 0.29201417341229924, 0.22530861506060088], 'audit_candidate_briers': [0.6243834192083423, 0.10483838377502522, 0.289426870307917, 0.21908927405314252], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1653.795 |
| Base scoring parameter | 0.310 |
| Home-advantage parameter | 0.165 |
| Dixon-Coles low-score adjustment | -0.068 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1647, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-22'} |
| Training data health | {'training_end': '2026-11-22', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 9.00 |
| Over 1 5 in window quote fixtures | 0 |
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

### 2026-11-27 — FC Groningen vs Willem II Tilburg

The model's most likely 1X2 outcome is **FC Groningen win** at **68.2%**. Expected goals are 2.33 for FC Groningen and 0.93 for Willem II Tilburg (3.26 combined). The most likely exact score is 2-0 at 10.4%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 63.3%; Under 3.5 goals: 58.8%; Double Chance 1X: 87.2%; Double Chance X2: 31.8%; Double Chance 12 (either team wins): 81.0%; Under 4.5 goals: 76.9%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| FC Groningen win | 68.2% | 1.47 |
| Draw | 19.0% | 5.26 |
| Willem II Tilburg win | 12.8% | 7.79 |

| Measure | Benchmark estimate |
| --- | --- |
| FC Groningen expected goals | 2.33 |
| Willem II Tilburg expected goals | 0.93 |
| Expected total goals | 3.26 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 84.2% |
| Under 1.5 | 15.8% |
| Over 2.5 | 63.3% |
| Under 2.5 | 36.7% |
| Over 3.5 | 41.2% |
| Under 3.5 | 58.8% |
| Over 4.5 | 23.1% |
| Under 4.5 | 76.9% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 2-0 | 10.42% |
| 2 | 2-1 | 9.69% |
| 3 | 1-1 | 8.87% |
| 4 | 1-0 | 8.37% |
| 5 | 3-0 | 8.10% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T19:00:00+00:00 |
| Fixture id | fdorg:558820 |
| Matched home-team name | Groningen |
| Matched away-team name | Willem II |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.3334 |
| Dc lambda away | 0.9297 |
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
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.78 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.35 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.73 |
| Fair Over 3.5 odds | 2.43 |
| Fair Under 3.5 odds | 1.70 |
| Fair Over 4.5 odds | 4.33 |
| Fair Under 4.5 odds | 1.30 |
| Score matrix json | [[0.04389771482315214,0.02995173593235562,0.016540496099424738,0.005126174893384982,0.0011915151552717527,0.00022156222052810846,3.433290892143544e-05,4.560145544919114e-06,5.2997436100236e-07,5.474929021027635e-08,5.090314738195684e-09,4.302472404727137e-10,3.3335194252971945e-11,2.3841072073867807e-12,1.5833024642992898e-13,9.813835440410844e-15,5.702757856390181e-16,3.1189050448661404e-17,1.611000927636492e-18],[0.08366665880330607,0.08865122835184269,0.03859505129952883,0.011961248428783886,0.0027802423981393596,0.0005169860212123425,8.011128403403431e-05,1.0640494104985893e-05,1.236624798154179e-06,1.27750198759268e-07,1.1877573518380918e-08,1.0039248047767214e-09,7.778324933784523e-11,5.562997592065536e-12,3.694426059834249e-13,2.2899281858962123e-14,1.3306628210735765e-15,7.277550774861853e-17,3.759056746059835e-18],[0.10417953828386467,0.09686091584165242,0.04502821365995994,0.013954992460334312,0.0032436632292137096,0.0006031591159627797,9.34645218129888e-05,1.2414090041971212e-05,1.44274987993528e-06,1.4904406267507388e-07,1.385737031405545e-08,1.1712626123280121e-09,9.074844189657004e-11,6.4902580960794745e-12,4.310226321040577e-13,2.6716216755425814e-14,1.5524624997038809e-15,8.490599187665466e-17,4.385629883164902e-18],[0.0810297063291998,0.07533736177675138,0.0350224524844157,0.010854040625578588,0.0025228858106267726,0.00046913056864462396,7.269568361946312e-05,9.655543564651855e-06,1.1221550892182286e-06,1.159248430892938e-07,1.0778111187087039e-08,9.109952594789857e-10,7.058314634372309e-11,5.048051816980295e-12,3.352446927290693e-13,2.0779581418577722e-14,1.2074883658568115e-15,6.603895256867646e-17,3.411094993847309e-18],[0.04726801502450081,0.0439474324873183,0.020430060594106743,0.006331615633432313,0.0014717047587130734,0.0002736634719747931,4.24064311868656e-05,5.63248219646106e-06,6.545999735145661e-07,6.762380703437199e-08,6.287322817846395e-09,5.314216176146291e-10,4.1174099882543526e-11,2.944739650913647e-12,1.955622436594149e-13,1.2121598500008647e-14,7.04378441004691e-16,3.852328169050296e-17,1.9898343055091554e-18],[0.02205872730456925,0.020509099619927605,0.009534166713529897,0.002954796865974507,0.0006868055264952691,0.0001277114746279182,1.9789955237726382e-05,2.6285298579848263e-06,3.0548442327970517e-07,3.155823484220399e-08,2.93412658523488e-09,2.4800035585666056e-10,1.9214858945300428e-11,1.3742317909644989e-12,9.126370552511513e-14,5.656828103921215e-15,3.287147120793272e-16,1.797779249345334e-17,9.286028259014445e-19],[0.008578518512027141,0.007975876773186005,0.00370778533681893,0.0011491043551180558,0.0002670949163047041,4.9666294621945095e-05,7.696205452608248e-06,1.0222208985496695e-06,1.1880122293810006e-07,1.2272825084730493e-08,1.1410657958881693e-09,9.644598323063705e-11,7.472553647014172e-12,5.344312342155488e-13,3.549195638141927e-14,2.199909538697258e-15,1.2783535531372517e-16,6.99146526366126e-18,3.611285647774509e-19],[0.0028595476913620002,0.002658664194916139,0.001235946391571172,0.0003830403467923949,8.90329315280758e-05,1.6555671929316305e-05,2.56543906775962e-06,3.407452471439568e-07,3.960098265304664e-08,4.091001096323063e-09,3.803607881418575e-10,3.2149127882820813e-11,2.4908873834030683e-12,1.7814633142660072e-13,1.1830823910925561e-14,7.333138272963237e-16,4.26124038374806e-17,2.3305222604474947e-18,1.2037793614904831e-19],[0.0008340468536899263,0.000775454983138154,0.0003604895985240123,0.00011172172334930711,2.596831542278402e-05,4.828807760430132e-06,7.48263926236178e-07,9.938547349593266e-08,1.155045431995267e-08,1.1932259787578908e-09,1.1094017406145665e-10,9.376965119532718e-12,7.265193692341403e-13,5.196010112773796e-14,3.450707078351664e-15,2.1388630526127143e-16,1.2428798252316335e-17,6.797455292150608e-19,3.511074118542843e-20],[0.00021623750924786958,0.00020104680372067253,9.3461623348533e-05,2.896531181558189e-05,6.732623978548648e-06,1.2519313011405304e-06,1.9399716808894784e-07,2.576697837669717e-08,2.994605712830144e-09,3.0935937528562615e-10,2.8762684983993772e-11,2.4311003306125136e-12,1.883596084902074e-13,1.3471332933421247e-14,8.946407512546789e-16,5.5452810243585296e-17,3.2223278166388456e-18,1.762328812938426e-19,9.102916926302814e-21],[5.045615144877122e-05,4.691160202550093e-05,2.18080287676457e-05,6.758670892997632e-06,1.570968405485488e-06,2.921215452097895e-07,4.52666631602219e-08,6.012382254466124e-09,6.987514788783199e-10,7.218490235945311e-11,6.711390612449841e-12,5.672649805077759e-13,4.3951213486828444e-14,3.1433566593961243e-15,2.087525397168959e-16,1.2939176933929088e-17,7.518874079683737e-19,4.112160272167512e-20,2.124044790640978e-21],[1.0702975411689189e-05,9.951090374216659e-06,4.626012665958231e-06,1.4336782791866052e-06,3.332405610349267e-07,6.196607600521167e-08,9.602158881756541e-09,1.2753723299836513e-09,1.4822216285975269e-10,1.5312171318354223e-11,1.4236489831418094e-12,1.2033068246299892e-13,9.323120050902796e-15,6.667823064120264e-16,4.428148472612094e-17,2.7447137483711428e-18,1.5949358420677173e-19,8.722890870228243e-21,4.505614977519365e-22],[2.081164326373636e-06,1.9349623351205357e-06,8.995155238075447e-07,2.7877482432420184e-07,6.479771662085602e-08,1.2049134176890598e-08,1.8671135597544625e-09,2.479926650216507e-10,2.8821394598810528e-11,2.9774098772829917e-12,2.76824655110109e-13,2.3397972440138823e-14,1.8128552214785858e-15,1.2965399771415852e-16,8.610413720114988e-18,5.337020893254359e-19,3.101309168421382e-20,1.6961422972291217e-21,8.761045222384706e-23],[3.73547738910339e-07,3.473059748340024e-07,1.614538485860691e-07,5.0037233471556653e-08,1.163052826897633e-08,2.162696511066714e-09,3.3512781268474307e-10,4.4512150295505004e-11,5.173145939603932e-12,5.344146607617253e-13,4.968719801727501e-14,4.199697058679606e-15,3.2538899517613113e-16,2.327156826256067e-17,1.5454813132589061e-18,9.579407363118918e-20,5.566533179743372e-21,3.0444021741624674e-22,1.5725181293182926e-23],[6.225886048488197e-08,5.788516963275243e-08,2.6909365488837974e-08,8.339660003946255e-09,1.938449524486284e-09,3.604546523194517e-10,5.585544646959069e-11,7.41879943702489e-12,8.622035091451614e-13,8.907040343088764e-14,8.281319914466784e-15,6.999596732075572e-16,5.423228664984425e-17,3.878651028512679e-18,2.575839590004148e-19,1.596591076385618e-20,9.277690011805792e-22,5.0740772993019534e-23,2.620901604404422e-24],[9.684852255218613e-09,9.00449046602137e-09,4.185962078511826e-09,1.2972992818682885e-09,3.015409710784402e-10,5.6071537853921587e-11,8.688751167211206e-12,1.1540522248416686e-12,1.3412249332815184e-13,1.3855597272782293e-14,1.2882240250652492e-15,1.0888419683287341e-16,8.43625597346013e-18,6.033544762647645e-19,4.006919765001277e-20,2.483622181062872e-21,1.4432171795992815e-22,7.89312374055271e-24,4.077017249662945e-25],[1.412394795218383e-09,1.313173926938244e-09,6.104616670311996e-10,1.8919222568046876e-10,4.397536347204424e-11,8.17721800372284e-12,1.267127943939889e-12,1.68301726533646e-13,1.955981428589361e-14,2.0206372753053418e-15,1.8786873151286533e-16,1.5879175937394095e-17,1.2303051935174947e-18,8.799047207858836e-20,5.843509505161495e-21,3.622001605581486e-22,2.1047222808560726e-23,1.1510972594511363e-24,5.945736487964141e-26],[1.938609240118857e-10,1.8024217571914985e-10,8.379007289261933e-11,2.596793744245562e-11,6.035921843744035e-12,1.122379552385159e-12,1.7392204706863577e-13,2.3100572395952186e-14,2.6847193743573096e-15,2.773463981952616e-16,2.5786278742547798e-17,2.179526383269169e-18,1.6886787068274738e-19,1.2077298981238238e-20,8.020619701927517e-22,4.971446938261993e-23,2.8888764496761946e-24,1.5799603559870309e-25,8.160933284306613e-27],[2.5130484674429007e-11,2.33650657433064e-11,1.0861833829741569e-11,3.3662629911129064e-12,7.824456742038475e-13,1.4549575828070648e-13,2.2545777911053903e-14,2.994562125018148e-15,3.4802423147582076e-16,3.595283291297416e-17,3.3427142991974054e-18,2.825353002490662e-19,2.18905973848348e-20,1.5655985263842877e-21,1.0397250581883896e-22,6.444561828461635e-24,3.74489421810738e-25,2.0481264965962476e-26,1.0579141200097182e-27]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.08531918197450464, "-10": 6.1902373859587075e-09, "-11": 5.148684500244227e-10, "-12": 3.935071677592218e-11, "-13": 2.781512970376005e-12, "-14": 1.8285001957546916e-13, "-15": 1.1232815348354922e-14, "-16": 6.474369232708015e-16, "-17": 3.494810719472124e-17, "-18": 1.611000927636492e-18, "-2": 0.03225969629275174, "-3": 0.008588222720480711, "-4": 0.001812308574025219, "-5": 0.0003152804066166903, "-6": 4.65386207268265e-05, "-7": 5.957143699891223e-06, "-8": 6.725355099047133e-07, "-9": 6.787174773389625e-08, "0": 0.19003866251122134, "1": 0.22262078247670294, "10": 6.135879039190586e-05, "11": 1.2808041150505431e-05, "12": 2.4567220862671474e-06, "13": 4.358142442648857e-07, "14": 7.190056300105119e-08, "15": 1.108518251804059e-08, "16": 1.6034988047672744e-09, "17": 2.1722598975519208e-10, "18": 2.5130484674429007e-11, "2": 0.20318618285418066, "3": 0.13575447178525488, "4": 0.07189520714616336, "5": 0.031389306793614555, "6": 0.011628272464266322, "7": 0.0037355686011196778, "8": 0.0010584023818999023, "9": 0.00026806589860634775} |
| Raw goal margin distribution | {"-1": 0.08531918197450464, "-10": 6.1902373859587075e-09, "-11": 5.148684500244227e-10, "-12": 3.935071677592218e-11, "-13": 2.781512970376005e-12, "-14": 1.8285001957546916e-13, "-15": 1.1232815348354922e-14, "-16": 6.474369232708015e-16, "-17": 3.494810719472124e-17, "-18": 1.611000927636492e-18, "-2": 0.03225969629275174, "-3": 0.008588222720480711, "-4": 0.001812308574025219, "-5": 0.0003152804066166903, "-6": 4.65386207268265e-05, "-7": 5.957143699891223e-06, "-8": 6.725355099047133e-07, "-9": 6.787174773389625e-08, "0": 0.19003866251122134, "1": 0.22262078247670294, "10": 6.135879039190586e-05, "11": 1.2808041150505431e-05, "12": 2.4567220862671474e-06, "13": 4.358142442648857e-07, "14": 7.190056300105119e-08, "15": 1.108518251804059e-08, "16": 1.6034988047672744e-09, "17": 2.1722598975519208e-10, "18": 2.5130484674429007e-11, "2": 0.20318618285418066, "3": 0.13575447178525488, "4": 0.07189520714616336, "5": 0.031389306793614555, "6": 0.011628272464266322, "7": 0.0037355686011196778, "8": 0.0010584023818999023, "9": 0.00026806589860634775} |
| Research history json | {"away": [{"away": "Willem II", "away_goals": 1.0, "away_xg": 0.11, "date": "2026-11-22T00:00:00+00:00", "home": "Twente", "home_goals": 2.0, "home_xg": 2.76, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-11-06T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 0.0, "away_xg": 1.22, "date": "2026-10-31T00:00:00+00:00", "home": "PSV Eindhoven", "home_goals": 7.0, "home_xg": 2.57, "source": "pipeline training history"}, {"away": "Cambuur", "away_goals": 6.0, "away_xg": 1.91, "date": "2026-10-24T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": 1.04, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 2.0, "away_xg": 1.17, "date": "2026-10-17T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 3.0, "home_xg": 3.38, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-10-11T00:00:00+00:00", "home": "Utrecht", "home_goals": 3.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "For Sittard", "away_goals": 1.0, "away_xg": 1.31, "date": "2026-09-19T00:00:00+00:00", "home": "Willem II", "home_goals": 0.0, "home_xg": 1.01, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 1.58, "date": "2026-09-15T00:00:00+00:00", "home": "Ajax", "home_goals": 5.0, "home_xg": 3.78, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 0.92, "date": "2026-09-11T00:00:00+00:00", "home": "AZ Alkmaar", "home_goals": 1.0, "home_xg": 2.49, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 3.0, "away_xg": 1.59, "date": "2026-09-05T00:00:00+00:00", "home": "Willem II", "home_goals": 0.0, "home_xg": 0.85, "source": "pipeline training history"}], "h2h": [{"away": "Groningen", "away_goals": 3.0, "away_xg": null, "date": "2025-02-15T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 0.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Heerenveen", "away_goals": 3.0, "away_xg": 1.51, "date": "2026-11-21T00:00:00+00:00", "home": "Groningen", "home_goals": 1.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 3.0, "away_xg": 2.16, "date": "2026-11-08T00:00:00+00:00", "home": "AZ Alkmaar", "home_goals": 4.0, "home_xg": 3.92, "source": "pipeline training history"}, {"away": "Sparta Rotterdam", "away_goals": 3.0, "away_xg": 2.42, "date": "2026-11-01T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 2.09, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 2.0, "away_xg": 1.33, "date": "2026-10-25T00:00:00+00:00", "home": "Nijmegen", "home_goals": 2.0, "home_xg": 1.49, "source": "pipeline training history"}, {"away": "Ajax", "away_goals": 5.0, "away_xg": 3.08, "date": "2026-10-18T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 5.0, "away_xg": 2.75, "date": "2026-10-11T00:00:00+00:00", "home": "Excelsior", "home_goals": 1.0, "home_xg": 1.77, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-09-18T00:00:00+00:00", "home": "Groningen", "home_goals": 3.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 1.0, "away_xg": 0.16, "date": "2026-09-12T00:00:00+00:00", "home": "Go Ahead Eagles", "home_goals": 1.0, "home_xg": 2.23, "source": "pipeline training history"}, {"away": "Twente", "away_goals": 2.0, "away_xg": 2.28, "date": "2026-09-06T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 1.69, "source": "pipeline training history"}, {"away": "For Sittard", "away_goals": 3.0, "away_xg": 0.88, "date": "2026-08-28T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 1.6, "source": "pipeline training history"}], "teams": {"away": "Willem II", "home": "Groningen"}} |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.0% |
| Unadjusted away-win probability | 12.8% |
| Raw p over 1 5 | 84.2% |
| Raw p under 3 5 | 58.8% |
| Raw p btts yes | 55.2% |
| P home draw | 87.2% |
| P draw away | 31.8% |
| P home away | 81.0% |
| Raw p home draw | 87.2% |
| Raw p draw away | 31.8% |
| Raw p home away | 81.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.6331 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-22 |
| Elo home rating | 1,455.5779 |
| Elo away rating | 1,337.5850 |
| Elo rating diff | 177.9929 |
| Elo home expectancy | 0.7359 |
| Research p home | 0.6603 |
| Research p draw | 0.2006 |
| Research p away | 0.1391 |
| Research p over 1 5 | 0.8544 |
| Research v4 p home | 0.6436 |
| Research v4 p draw | 0.1891 |
| Research v4 p away | 0.1673 |
| Research v4 p over 1 5 | 0.8510 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.3333672138691854, 0.9297499051851166], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T15:50:26.785989+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 6.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 6.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-22", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T15:50:26.419589+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T15:50:26.473510+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T15:50:26.697482+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22FC+Groningen%22+%22Willem+II+Tilburg%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T15:50:01.200490+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T15:50:01.389360+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T15:50:26.785499+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=FC+Groningen_vs_Willem+II+Tilburg&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 3.2584065577239567, "goals_for": 0.8436321611467258, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 0.20719289197985322, "results": "LDLLLLLLDL", "xg_against": 2.1516754902944695, "xg_for": 0.8445326901861926, "xg_matches": 10}, "venue": {"goals_against": 3.6030701166169603, "goals_for": 0.9741680296645312, "last_match": "2026-11-22T00:00:00+00:00", "matches": 6, "points_per_game": 0.11461286578853329, "results": "LLLLLD", "xg_against": 2.7017491887016765, "xg_for": 0.8776336913023165, "xg_matches": 6}}, "home": {"all": {"goals_against": 2.6489217114294004, "goals_for": 2.2462812993052665, "last_match": "2026-11-21T00:00:00+00:00", "matches": 10, "points_per_game": 0.7204958745112958, "results": "LLLDLWWDDL", "xg_against": 2.1455152647081097, "xg_for": 1.7389171676140538, "xg_matches": 10}, "venue": {"goals_against": 2.762087879176076, "goals_for": 1.9220068515072548, "last_match": "2026-11-21T00:00:00+00:00", "matches": 6, "points_per_game": 0.5853533596457492, "results": "LLLWDL", "xg_against": 1.8301717539689404, "xg_for": 1.7457153973740847, "xg_matches": 6}}}, "goal_rates": [2.2922541185574463, 1.0888072117290584], "h2h": [{"away": "Groningen", "away_goals": 3.0, "away_xg": null, "date": "2025-02-15T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 0.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.08854172177798983, "-10": 2.3037654371332828e-08, "-11": 2.2386538751740433e-09, "-12": 1.9996543567283374e-10, "-13": 1.652402061109542e-11, "-14": 1.2701628368271331e-12, "-15": 9.125570437596371e-14, "-16": 6.151626198255341e-15, "-17": 3.8775259894602875e-16, "-18": 2.059872540378713e-17, "-2": 0.03616165475208909, "-3": 0.011062157882451866, "-4": 0.0026989140447781983, "-5": 0.0005448353611737436, "-6": 9.354123008733711e-05, "-7": 1.3948405487903106e-05, "-8": 1.8364139750906913e-06, "-9": 2.1629918018712852e-07, "0": 0.20063061162902454, "1": 0.23018610400646575, "10": 4.832463454264937e-05, "11": 9.886192079674259e-06, "12": 1.8591258930656359e-06, "13": 3.234307939405899e-07, "14": 5.2340373028640884e-08, "15": 7.916791482526424e-09, "16": 1.1235460972223518e-09, "17": 1.4909649979265997e-10, "18": 1.667496195641458e-11, "2": 0.19655515203075508, "3": 0.12658660775354175, "4": 0.06502026505972001, "5": 0.027633553869111555, "6": 0.00998817872450725, "7": 0.003135592125978724, "8": 0.0008691152355482525, "9": 0.0002155129741769196}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T15:50:26.785989+00:00", "p_over_1_5": 0.8543821745584285, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.10700828904995757, "-10": 2.747884085810691e-08, "-11": 2.6702203523306414e-09, "-12": 2.3851466366356087e-10, "-13": 1.9709512322286836e-11, "-14": 1.5150241380687552e-12, "-15": 1.0884792946029783e-13, "-16": 7.337533352821114e-15, "-17": 4.625033341942112e-16, "-18": 2.4569736489963814e-17, "-2": 0.043132878898251, "-3": 0.013194714665803953, "-4": 0.003219209227240399, "-5": 0.0006498684259362962, "-6": 0.00011157405757593149, "-7": 1.663737151571216e-05, "-8": 2.190436862960937e-06, "-9": 2.5799721856653717e-07, "0": 0.1890874767653033, "1": 0.22528340063529043, "10": 4.7001978382236914e-05, "11": 9.615604769890022e-06, "12": 1.8082411975326494e-06, "13": 3.1457842007121153e-07, "14": 5.090780519900692e-08, "15": 7.700107111828845e-09, "16": 1.092794386814962e-09, "17": 1.4501569492340324e-10, "18": 1.6218564482020233e-11, "2": 0.19117539313232326, "3": 0.12312190371272448, "4": 0.06324064572174054, "5": 0.026877217259326906, "6": 0.009714800017222651, "7": 0.003049770261391082, "8": 0.0008453273552820984, "9": 0.00020961433540516979}, "p_over_1_5": 0.8509942409429174, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
