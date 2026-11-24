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
| Training as of utc | 2026-11-24T16:35:07.327316+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1647, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1341, 'tuning_matches': 189, 'audit_matches': 111, 'audit_matchdays': 39, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6308885479009532, 'audit_candidate_poisson_score': 0.6224747475142083, 'audit_gain': 0.008413800386744885, 'audit_gain_lower95': -0.004700720782241717, 'audit_baseline_briers': [0.6284532874594683, 0.1053318588745377, 0.29201417341229924, 0.22530861506060088], 'audit_candidate_briers': [0.6243834192083423, 0.10483838377502522, 0.289426870307917, 0.21908927405314252], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1653.720 |
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

The model's most likely 1X2 outcome is **FC Groningen win** at **68.2%**. Expected goals are 2.33 for FC Groningen and 0.93 for Willem II Tilburg (3.26 combined). The most likely exact score is 2-0 at 10.4%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 63.3%; Under 3.5 goals: 58.9%; Double Chance 1X: 87.2%; Double Chance X2: 31.8%; Double Chance 12 (either team wins): 81.0%; Under 4.5 goals: 76.9%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

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
| Over 3.5 | 41.1% |
| Under 3.5 | 58.9% |
| Over 4.5 | 23.1% |
| Under 4.5 | 76.9% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 2-0 | 10.42% |
| 2 | 2-1 | 9.69% |
| 3 | 1-1 | 8.86% |
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
| Score matrix json | [[0.043897699321731216,0.029954257482072533,0.016539745924481566,0.0051256747049507655,0.0011913366732292604,0.00022151746268410057,3.4324180684787606e-05,4.55874816010227e-06,5.297842898516925e-07,5.4726796610052245e-08,5.087957669021856e-09,4.3002555579049796e-10,3.331627831318764e-11,2.382629917319899e-12,1.5822387505087135e-13,9.806730015932329e-15,5.698331334386998e-16,3.116321373174994e-17,1.6095823265073499e-18],[0.08367380963295773,0.08864914661621838,0.03859312652864098,0.011960027278292052,0.0027798133767032575,0.0005168792498206991,8.009055605861517e-05,1.0637185441562388e-05,1.236175708169075e-06,1.276971360819225e-07,1.1872019980807807e-08,1.0034030003210005e-09,7.773876033374256e-11,5.559525417736094e-12,3.6919273473552824e-13,2.2882598926558828e-14,1.329623944613346e-15,7.271489272446035e-17,3.755729662885347e-18],[0.10418475375355869,0.09686070621539103,0.045025764665800855,0.01395350473171161,0.003243148046619109,0.0006030318234463609,9.34399167264183e-05,1.2410173817942207e-05,1.4422194190536474e-06,1.4898148232313897e-07,1.3850828524266793e-08,1.1706485434364422e-09,9.069612760190759e-11,6.486177867106805e-12,4.307291656764018e-13,2.6696632454603737e-14,1.551243452114335e-15,8.483489009579859e-17,4.381728436123108e-18],[0.08103339681123149,0.07533685841149092,0.03502038948542737,0.010852834460853744,0.0025224737124291555,0.00046902944316322604,7.267621775073447e-05,9.652453965235932e-06,1.1217374353015263e-06,1.1587564532880633e-07,1.0772974389574707e-08,9.105135303305851e-10,7.054213819607387e-11,5.044855470280744e-12,3.3501492438123974e-13,2.076425516476889e-14,1.2065347536679457e-15,6.598335231305614e-17,3.408045095766159e-18],[0.04726995430371845,0.04394694033119062,0.020428764877410747,0.006330883428538097,0.001471457717570721,0.00027360324530232736,4.239488442089042e-05,5.6306544685315205e-06,6.543533826058753e-07,6.759480257709461e-08,6.284297920974522e-09,5.311382055463661e-10,4.114999222830096e-11,2.942861794434639e-12,1.9542732737041022e-13,1.2112603339038755e-14,7.038189797792982e-16,3.849067386265623e-17,1.9880461918332093e-18],[0.02205953266484249,0.020508777299146286,0.009533518971059791,0.0029544418192543128,0.0006866871369734427,0.0001276827916560694,1.9784477295999557e-05,2.627665035911438e-06,3.053679664083996e-07,3.154455673560279e-08,2.9327016982632054e-09,2.4786697527808283e-10,1.9203521794959982e-11,1.3733492413666489e-12,9.120033169550381e-14,5.652604766592438e-15,3.2845214266171205e-16,1.796249414394444e-17,9.277641697341466e-19],[0.008578792959135087,0.007975715395584603,0.0037075166852947703,0.001148961089170659,0.00026704766892841447,4.96549156640813e-05,7.69404035460789e-06,1.0218799578183833e-06,1.1875539704179331e-07,1.2267450327890197e-08,1.140506513104934e-09,9.639367681196119e-11,7.468110955394812e-12,5.340856028671378e-13,3.546715042912534e-14,2.1982571756699946e-15,1.2773266649342447e-16,6.985484263506999e-18,3.608007861262612e-19],[0.002859626257229932,0.002658598391877521,0.0012358512570346388,0.00038299086069320073,8.901678005721816e-05,1.6551804118590197e-05,2.564705772365633e-06,3.4063005985041044e-07,3.9585528312215606e-08,4.089191012535584e-09,3.8017264048128265e-10,3.213154700847463e-11,2.4893952193137698e-12,1.7803031508541337e-13,1.1822501734145604e-14,7.327597215172567e-16,4.257798139558048e-17,2.3285180461337386e-18,1.2026813172326272e-19],[0.0008340660013294462,0.0007754322874354147,0.00036046022223594704,0.00011170678507950765,2.5963487223490305e-05,4.827657824541632e-06,7.480466661456985e-07,9.935142791255943e-08,1.1545894581995538e-08,1.1926926422202122e-09,1.1088479596219646e-10,9.371794954718338e-12,7.260808684534073e-13,5.192602797071486e-14,3.4482641646538776e-15,2.1372372327186768e-16,1.2418702128470455e-17,6.791578902494536e-19,3.507855596869321e-20],[0.00021624149669204884,0.00020104001140329572,9.34535850040743e-05,2.896130804726157e-05,6.731341797415882e-06,1.2516275112904634e-06,1.939399644932302e-07,2.575803525867273e-08,2.9934100192068202e-09,3.0921970399968596e-10,2.874819762589368e-11,2.429748922110559e-12,1.8824507108977675e-13,1.3462438209641668e-14,8.940033555687233e-16,5.541040843918921e-17,3.2196957206657173e-18,1.7607973283129586e-19,9.09453140683751e-21],[5.0456853936470004e-05,4.6909805222113706e-05,2.1806054621908485e-05,6.7577061401440154e-06,1.5706621303697126e-06,2.9204934060360903e-07,4.5253111038233526e-08,6.010268346357977e-09,6.984693244432119e-10,7.215198598634346e-11,6.707979877757789e-12,5.669470862006653e-13,4.392428928552882e-14,3.1412670036223396e-15,2.0860286957264553e-16,1.2929224630542972e-17,7.512698496018182e-19,4.108568196461264e-20,2.122078554926651e-21],[1.0703076077239646e-05,9.950664278294922e-06,4.625573006525385e-06,1.4334671562491596e-06,3.3317408759081333e-07,6.195047980446452e-08,9.599240784687573e-09,1.2749181595168478e-09,1.4816164175726425e-10,1.5305119817975514e-11,1.4229190556873078e-12,1.2026270609371232e-13,9.317366684288908e-15,6.663360296110585e-16,4.424953616366366e-17,2.7425902339186437e-18,1.5936186518780792e-19,8.715231835623375e-21,4.501423779583297e-22],[2.0811744991961847e-06,1.934870741514035e-06,8.99425970242528e-07,2.7873251292355805e-07,6.478449838934388e-08,1.2046047122489593e-08,1.866537712015223e-09,2.479032329585102e-10,2.8809496294245106e-11,2.9760252886596017e-12,2.7668147285378174e-13,2.3384648985052313e-14,1.811728310914071e-15,1.29566635116343e-16,8.604162541730407e-18,5.332867687181797e-19,3.0987339301314407e-20,1.6946453636308216e-21,8.752856013109986e-23],[3.735478773950206e-07,3.472879659084102e-07,1.6143704537405144e-07,5.0029413008755224e-08,1.1628103203641684e-08,2.1621326493017945e-09,3.350229404936209e-10,4.449589715171951e-11,5.170986956495713e-12,5.341637282611654e-13,4.966127392920519e-14,4.197286674119712e-15,3.251852572765071e-16,2.3255782514930107e-17,1.5443523142660613e-18,9.571909543119317e-20,5.561885765271497e-21,3.0417015909338827e-22,1.5710411530144656e-23],[6.225860232434149e-08,5.7881906630824265e-08,2.6906443367983966e-08,8.338318907748792e-09,1.9380365863419546e-09,3.6035904613910057e-10,5.583771528078265e-11,7.41605703973579e-12,8.618397802013985e-13,8.902817857195729e-14,8.2769617807492e-15,6.995547765057665e-16,5.419808501041854e-17,3.876002523251676e-18,2.5739462703703434e-19,1.5953342149484226e-20,9.269902333490536e-22,5.069553361134793e-23,2.618428113226012e-24],[9.684768347189568e-09,9.00394220693932e-09,4.185488612612474e-09,1.2970848045357553e-09,3.0147537346435946e-10,5.605641234106037e-11,8.68595370505576e-12,1.1536204122479104e-12,1.340653068335903e-13,1.3848966305890359e-14,1.287540267086224e-15,1.0882072040957882e-16,8.430897556175467e-18,6.029397569071074e-19,4.0039564712333924e-20,2.4816558244643215e-21,1.4419992314191007e-22,7.886050777453913e-24,4.073151141147273e-25],[1.4123761783064473e-09,1.3130880396968321e-09,6.103898615956282e-10,1.8916009278644204e-10,4.3965598408005625e-11,8.174975238805009e-12,1.2667142526391347e-12,1.6823799296550378e-13,1.95513861479253e-14,2.0196611218155057e-15,1.8776816715193953e-16,1.5869847135500818e-17,1.2295181921971062e-18,8.792959408849455e-20,5.83916159500815e-21,3.619117611879672e-22,2.1029365810113155e-23,1.1500605755039165e-24,5.940071498011151e-26],[1.938574929971938e-10,1.8022957294950684e-10,8.377983864165574e-11,2.596340969632227e-11,6.034554261398843e-12,1.1220666487090952e-12,1.738644796847857e-13,2.309172021173504e-14,2.6835504318697825e-15,2.7721116214840554e-16,2.5772359168787363e-17,2.1782361011114217e-18,1.6875908698741666e-19,1.2068888538389058e-20,8.014615690920903e-22,4.9674660184530346e-23,2.8864124146852493e-24,1.5785303050737624e-25,8.153120864791848e-27],[2.5129926387038834e-11,2.336332648774177e-11,1.0860458088216778e-11,3.3656608487893413e-12,7.822648587008172e-13,1.454545390402789e-13,2.253821355186266e-14,2.9934010808620048e-15,3.4787112825074094e-16,3.593513972944941e-17,3.340894791935265e-18,2.823667634828688e-19,2.187639676738755e-20,1.5645012006189726e-21,1.0389420559367503e-22,6.439372213260216e-24,3.7416831499376363e-25,2.0462634563621346e-26,1.0568966099227098e-27]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.08531781286495597, "-10": 6.187302862443444e-09, "-11": 5.145979570769627e-10, "-12": 3.9328019294039607e-11, "-13": 2.779765237701731e-12, "-14": 1.8272568882804938e-13, "-15": 1.1224596895737238e-14, "-16": 6.469297545992832e-16, "-17": 3.491894339463529e-17, "-18": 1.6095823265073499e-18, "-2": 0.03225709619995995, "-3": 0.008587144802472253, "-4": 0.0018119953650587702, "-5": 0.00031521055643613996, "-6": 4.6526001005274404e-05, "-7": 5.95522921283649e-06, "-8": 6.722853275421892e-07, "-9": 6.784304357614211e-08, "0": 0.1900326321061898, "1": 0.22262479793916065, "10": 6.135896898116873e-05, "11": 1.2808032010242066e-05, "12": 2.4567111034803853e-06, "13": 4.3581061274004425e-07, "14": 7.189968006743145e-08, "15": 1.1085001886376847e-08, "16": 1.603466209344171e-09, "17": 2.1722081948493558e-10, "18": 2.5129926387038834e-11, "2": 0.20318919285351847, "3": 0.1357568617419552, "4": 0.07189650082096874, "5": 0.031389839346084594, "6": 0.011628447405815479, "7": 0.003735615398519387, "8": 0.0010584125381531057, "9": 0.00026806760475277247} |
| Raw goal margin distribution | {"-1": 0.08531781286495597, "-10": 6.187302862443444e-09, "-11": 5.145979570769627e-10, "-12": 3.9328019294039607e-11, "-13": 2.779765237701731e-12, "-14": 1.8272568882804938e-13, "-15": 1.1224596895737238e-14, "-16": 6.469297545992832e-16, "-17": 3.491894339463529e-17, "-18": 1.6095823265073499e-18, "-2": 0.03225709619995995, "-3": 0.008587144802472253, "-4": 0.0018119953650587702, "-5": 0.00031521055643613996, "-6": 4.6526001005274404e-05, "-7": 5.95522921283649e-06, "-8": 6.722853275421892e-07, "-9": 6.784304357614211e-08, "0": 0.1900326321061898, "1": 0.22262479793916065, "10": 6.135896898116873e-05, "11": 1.2808032010242066e-05, "12": 2.4567111034803853e-06, "13": 4.3581061274004425e-07, "14": 7.189968006743145e-08, "15": 1.1085001886376847e-08, "16": 1.603466209344171e-09, "17": 2.1722081948493558e-10, "18": 2.5129926387038834e-11, "2": 0.20318919285351847, "3": 0.1357568617419552, "4": 0.07189650082096874, "5": 0.031389839346084594, "6": 0.011628447405815479, "7": 0.003735615398519387, "8": 0.0010584125381531057, "9": 0.00026806760475277247} |
| Research history json | {"away": [{"away": "Willem II", "away_goals": 1.0, "away_xg": 0.11, "date": "2026-11-22T00:00:00+00:00", "home": "Twente", "home_goals": 2.0, "home_xg": 2.76, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-11-06T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 0.0, "away_xg": 1.22, "date": "2026-10-31T00:00:00+00:00", "home": "PSV Eindhoven", "home_goals": 7.0, "home_xg": 2.57, "source": "pipeline training history"}, {"away": "Cambuur", "away_goals": 6.0, "away_xg": 1.91, "date": "2026-10-24T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": 1.04, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 2.0, "away_xg": 1.17, "date": "2026-10-17T00:00:00+00:00", "home": "Sparta Rotterdam", "home_goals": 3.0, "home_xg": 3.38, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-10-11T00:00:00+00:00", "home": "Utrecht", "home_goals": 3.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "For Sittard", "away_goals": 1.0, "away_xg": 1.31, "date": "2026-09-19T00:00:00+00:00", "home": "Willem II", "home_goals": 0.0, "home_xg": 1.01, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 1.58, "date": "2026-09-15T00:00:00+00:00", "home": "Ajax", "home_goals": 5.0, "home_xg": 3.78, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 1.0, "away_xg": 0.92, "date": "2026-09-11T00:00:00+00:00", "home": "AZ Alkmaar", "home_goals": 1.0, "home_xg": 2.49, "source": "pipeline training history"}, {"away": "Excelsior", "away_goals": 3.0, "away_xg": 1.59, "date": "2026-09-05T00:00:00+00:00", "home": "Willem II", "home_goals": 0.0, "home_xg": 0.85, "source": "pipeline training history"}], "h2h": [{"away": "Groningen", "away_goals": 3.0, "away_xg": null, "date": "2025-02-15T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 0.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Heerenveen", "away_goals": 3.0, "away_xg": 1.51, "date": "2026-11-21T00:00:00+00:00", "home": "Groningen", "home_goals": 1.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 3.0, "away_xg": 2.16, "date": "2026-11-08T00:00:00+00:00", "home": "AZ Alkmaar", "home_goals": 4.0, "home_xg": 3.92, "source": "pipeline training history"}, {"away": "Sparta Rotterdam", "away_goals": 3.0, "away_xg": 2.42, "date": "2026-11-01T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 2.09, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 2.0, "away_xg": 1.33, "date": "2026-10-25T00:00:00+00:00", "home": "Nijmegen", "home_goals": 2.0, "home_xg": 1.49, "source": "pipeline training history"}, {"away": "Ajax", "away_goals": 5.0, "away_xg": 3.08, "date": "2026-10-18T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 5.0, "away_xg": 2.75, "date": "2026-10-11T00:00:00+00:00", "home": "Excelsior", "home_goals": 1.0, "home_xg": 1.77, "source": "pipeline training history"}, {"away": "Zwolle", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-09-18T00:00:00+00:00", "home": "Groningen", "home_goals": 3.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Groningen", "away_goals": 1.0, "away_xg": 0.16, "date": "2026-09-12T00:00:00+00:00", "home": "Go Ahead Eagles", "home_goals": 1.0, "home_xg": 2.23, "source": "pipeline training history"}, {"away": "Twente", "away_goals": 2.0, "away_xg": 2.28, "date": "2026-09-06T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 1.69, "source": "pipeline training history"}, {"away": "For Sittard", "away_goals": 3.0, "away_xg": 0.88, "date": "2026-08-28T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": 1.6, "source": "pipeline training history"}], "teams": {"away": "Willem II", "home": "Groningen"}} |
| Unadjusted home-win probability | 68.2% |
| Unadjusted draw probability | 19.0% |
| Unadjusted away-win probability | 12.8% |
| Raw p over 1 5 | 84.2% |
| Raw p under 3 5 | 58.9% |
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
| Team research json | {"base_rates": [2.333356673364416, 0.9297013500123814], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T16:35:47.800629+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 6.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 6.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-22", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T16:35:47.455873+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T16:35:47.522484+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T16:35:47.716458+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22FC+Groningen%22+%22Willem+II+Tilburg%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T16:35:21.826042+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T16:35:22.061091+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T16:35:47.800212+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=FC+Groningen_vs_Willem+II+Tilburg&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 3.2584065577239567, "goals_for": 0.8436321611467258, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 0.20719289197985322, "results": "LDLLLLLLDL", "xg_against": 2.1516754902944695, "xg_for": 0.8445326901861926, "xg_matches": 10}, "venue": {"goals_against": 3.6030701166169603, "goals_for": 0.9741680296645312, "last_match": "2026-11-22T00:00:00+00:00", "matches": 6, "points_per_game": 0.11461286578853329, "results": "LLLLLD", "xg_against": 2.7017491887016765, "xg_for": 0.8776336913023165, "xg_matches": 6}}, "home": {"all": {"goals_against": 2.6489217114294004, "goals_for": 2.2462812993052665, "last_match": "2026-11-21T00:00:00+00:00", "matches": 10, "points_per_game": 0.7204958745112958, "results": "LLLDLWWDDL", "xg_against": 2.1455152647081097, "xg_for": 1.7389171676140538, "xg_matches": 10}, "venue": {"goals_against": 2.762087879176076, "goals_for": 1.9220068515072548, "last_match": "2026-11-21T00:00:00+00:00", "matches": 6, "points_per_game": 0.5853533596457492, "results": "LLLWDL", "xg_against": 1.8301717539689404, "xg_for": 1.7457153973740847, "xg_matches": 6}}}, "goal_rates": [2.2922475307419656, 1.088776864746099], "h2h": [{"away": "Groningen", "away_goals": 3.0, "away_xg": null, "date": "2025-02-15T00:00:00+00:00", "home": "Willem II", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Willem II", "away_goals": 0.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Groningen", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.08853944252354999, "-10": 2.3031787551772527e-08, "-11": 2.238022633445122e-09, "-12": 1.9990357308781687e-10, "-13": 1.6518454936717537e-11, "-14": 1.2697000760772908e-12, "-15": 9.121994299789842e-14, "-16": 6.149046000634184e-15, "-17": 3.875794303992798e-16, "-18": 2.0589029324835147e-17, "-2": 0.03615997586421098, "-3": 0.011061384268778998, "-4": 0.002698658090555748, "-5": 0.0005447696659905763, "-6": 9.352749300801125e-05, "-7": 1.394598553132014e-05, "-8": 1.8360459894233021e-06, "-9": 2.1624998197220057e-07, "0": 0.200630052667745, "1": 0.23018736594767042, "10": 4.832469153774524e-05, "11": 9.886180796510533e-06, "12": 1.8591193047143207e-06, "13": 3.2342884969842455e-07, "14": 5.233992649687975e-08, "15": 7.916703664085486e-09, "16": 1.1235307517965325e-09, "17": 1.490941390602284e-10, "18": 1.6674712439313764e-11, "2": 0.19655701145435556, "3": 0.12658799398693227, "4": 0.06502098316717898, "5": 0.027633838432473003, "6": 0.00998826876391424, "7": 0.003135615238361403, "8": 0.0008691199938018164, "9": 0.00021551370595204153}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T16:35:47.800629+00:00", "p_over_1_5": 0.8543780496214194, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.10700621896963164, "-10": 2.7472009498438175e-08, "-11": 2.6694835954664006e-09, "-12": 2.384423200455229e-10, "-13": 1.970299308731263e-11, "-14": 1.5144813433067009e-12, "-15": 1.0880593331508012e-13, "-16": 7.334500188317123e-15, "-17": 4.622995835383535e-16, "-18": 2.4558320013331443e-17, "-2": 0.04313113770140034, "-3": 0.013193871861430258, "-4": 0.0032189234348455466, "-5": 0.0006497940033925993, "-6": 0.00011155834823960307, "-7": 1.6634585835784293e-05, "-8": 2.1900112072336484e-06, "-9": 2.5794009889259213e-07, "0": 0.1890869190279568, "1": 0.22528467415990902, "10": 4.7002041684527956e-05, "11": 9.615595404999635e-06, "12": 1.808235092166929e-06, "13": 3.1457658169696776e-07, "14": 5.090737940975704e-08, "15": 7.700022985822103e-09, "16": 1.0927796443054878e-09, "17": 1.4501342307698122e-10, "18": 1.6218324508868887e-11, "2": 0.19117723366217104, "3": 0.12312327261286804, "4": 0.06324135475972313, "5": 0.026877498532858913, "6": 0.009714889218301062, "7": 0.003049793251654562, "8": 0.0008453321247921963, "9": 0.00020961508223664479}, "p_over_1_5": 0.8509899935919272, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
