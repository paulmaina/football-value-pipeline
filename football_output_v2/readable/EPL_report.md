# Premier League — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,990 |
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
| Training sha256 | 360bea142f79da4d57d8363e05c1e1dd30c82d5fbca24beefafe296e82c9d2a4 |
| Training as of utc | 2026-11-05T12:25:21.757952+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 90, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 90, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 233, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-05T12:25:21.757952+00:00', 'observations': 642, 'observations_sha256': 'a74496bfcfd3037993920b5bf282167ffb16f3b640390b628049004d45ef0edb', 'eligible_training_matches': 297, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 267, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 28, 'retrospective_eligible_training_matches': 297, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'bb420e73fb62ceaa6d23f7532df48dcd3a7b8d7256ad31a4600ea2866a27ccd5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 236, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-04T00:00:00+00:00', 'audit_origin_utc': '2025-11-02T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 12, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1989, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1619, 'tuning_matches': 249, 'audit_matches': 112, 'audit_matchdays': 37, 'selected_shrinkage': 15.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9372365915629014, 'audit_candidate_poisson_score': 0.9280458784415208, 'audit_gain': 0.009190713121380645, 'audit_gain_lower95': 0.0003476760981782903, 'audit_baseline_briers': [0.6265817822406763, 0.16783379803353324, 0.2144793454599894, 0.2603736901518194], 'audit_candidate_briers': [0.6267009894464598, 0.1671447860232481, 0.21207329001908468, 0.2571284796929984], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'market_brier_worse']} |
| Optimizer objective | 1878.033 |
| Base scoring parameter | 0.214 |
| Home-advantage parameter | 0.178 |
| Dixon-Coles low-score adjustment | -0.061 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1990, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261105T122521757952Z_ff1dbef3d42cd3ab88cc4653ab9be39dc8156bc6a7284ea14569622bdc311429.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'ANCHORED_MAIN': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 5} |
| Legacy comparison status | {'None': 5} |
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

## 2026-11-06 — Everton vs Coventry City

The model's most likely 1X2 outcome is **Everton win** at **54.6%**. Expected goals are 1.44 for Everton and 0.90 for Coventry City (2.33 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 56.0%; Under 3.5 goals: 66.2%; Double Chance 1X: 79.5%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 82.7%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 54.6% | 1.83 |
| Draw | 24.9% | 4.02 |
| Coventry City win | 20.5% | 4.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.44 |
| Coventry City expected goals | 0.90 |
| Expected total goals | 2.33 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 79.8% |
| Under 1.5 | 20.2% |
| Over 2.5 | 56.0% |
| Under 2.5 | 44.0% |
| Over 3.5 | 33.8% |
| Under 3.5 | 66.2% |
| Over 4.5 | 17.3% |
| Under 4.5 | 82.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.72% |
| 2 | 2-1 | 10.15% |
| 3 | 1-0 | 9.33% |
| 4 | 2-0 | 9.04% |
| 5 | 0-0 | 6.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 54.6% | 57.0% | 1.74 | -4.9% |
| Draw | 24.9% | 23.4% | 4.21 | +4.7% |
| Coventry City win | 20.5% | 19.6% | 4.93 | +1.1% |
| Over 2.5 | 56.0% | 55.1% | 1.81 | +1.3% |
| Under 2.5 | 44.0% | 44.9% | 2.15 | -5.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:00:00+00:00 |
| Fixture id | 586bec023ee8ac2f0645d963bd2c9d25 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:19:13Z |
| Market best draw last update utc | 2026-11-05T12:19:13Z |
| Market best away last update utc | 2026-11-05T12:19:13Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Everton |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4394 |
| Dc lambda away | 0.8950 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:25:21.757952+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.34 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.94 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.96 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.78 |
| Fair Under 4.5 odds | 1.21 |
| Score matrix json | [[0.06120726573654044,0.04786505913445241,0.030198505272827605,0.011301707997403224,0.003172224978635711,0.0007123179128246817,0.00013329151524774265,2.1378850711578687e-05,3.0003661507347485e-06,3.7429294170406276e-07,4.2023432892567424e-08,4.289224040390547e-09,4.013075912365948e-10,3.4658831154734354e-11,2.7794941625416966e-12,2.0804361753492634e-13,1.4598704026454784e-14],[0.09325968330376341,0.11715765643948477,0.0545267002817831,0.0204064684354139,0.005727798746121825,0.0012861678082088713,0.00024067239210538122,3.860185047529956e-05,5.417488857765654e-06,6.758267955814416e-07,7.587789890403727e-08,7.744662577794375e-09,7.246046965063326e-10,6.25803059263196e-11,5.0186803540984004e-12,3.756454790188583e-13,2.6359554943575722e-14],[0.09039017561363426,0.10148482794661567,0.05596048936781896,0.01842305402427778,0.00517108318247094,0.0011611582420502432,0.00021728014800517198,3.4849929030804995e-05,4.8909339809789194e-06,6.101395547915588e-07,6.850291784598119e-08,6.991917171856017e-09,6.54176469203002e-10,5.649778944286164e-11,4.530887820534393e-12,3.39134474730084e-13,2.3797528039621527e-14],[0.05440311222442263,0.06108064782897895,0.03428889806724055,0.01260499429356676,0.0031123185322737327,0.0006988660186101481,0.00013077434794010428,2.0975118005966887e-05,2.94370520295021e-06,3.6722454012886773e-07,4.122983390590051e-08,4.208223426739029e-09,3.93729026711386e-10,3.400431029838799e-11,2.7270043110705233e-12,2.0411478086705292e-13,1.432301220585405e-14],[0.02455769058648134,0.027571945590504635,0.015478087830950891,0.005792632034041992,0.001597078745224913,0.00031546973591576124,5.903184288637483e-05,9.468216742464772e-06,1.3287953316651222e-06,1.657660060888795e-07,1.861124230937999e-08,1.8996017802497345e-09,1.777301925854533e-10,1.5349624254393946e-11,1.2309760482637784e-12,9.213788380309384e-14,6.4654408109368475e-15],[0.00886831862785409,0.00995683196778506,0.005589475694035565,0.0020918459897885456,0.000587150729941958,0.00012950602703887157,2.131768824361605e-05,3.4191799352656973e-06,4.798570269021297e-07,5.986172659379602e-08,6.720926231990178e-09,6.859877069453406e-10,6.418225574131667e-11,5.543084689760601e-12,4.445323464279398e-13,3.32730029472657e-14,2.3348119392172333e-15],[0.0026687863491677397,0.002996357974004329,0.0016820681639013867,0.000629509409435802,0.00017669413095412672,3.967637712245256e-05,7.292746856973658e-06,1.0289504831191844e-06,1.4440571394518132e-07,1.8014481151969135e-08,2.022561089016599e-09,2.064376241785531e-10,1.9314679046739022e-11,1.6681074928735838e-12,1.3377528567638532e-13,1.0013006950672417e-14,7.026263368217051e-16],[0.0006883979004092409,0.0007728930938298283,0.0004338796894461193,0.0001623782869987357,4.5577222321070544e-05,1.0234290472693393e-05,1.91507760794805e-06,3.017162615381266e-07,3.7248613145057784e-08,4.646730528221072e-09,5.217078570424536e-10,5.32493832240656e-11,4.982109005091363e-12,4.302786156371047e-13,3.4506556066201584e-14,2.5827968446314882e-15,1.8123837271242615e-16],[0.0001553722015837574,0.00017444286437514247,9.792714726707435e-05,3.6648967007880934e-05,1.028683174351245e-05,2.309891185671461e-06,4.3223522903506247e-07,6.932693665197206e-08,9.557017979714451e-09,1.0487724496355426e-09,1.1775006618126237e-10,1.2018447324696705e-11,1.1244677594035807e-12,9.71143807472468e-14,7.78816957735034e-15,5.829402323211809e-16,4.09057101467726e-17],[3.1171275941341646e-05,3.4997294277923444e-05,1.964646248489205e-05,7.352634846664931e-06,2.063777609962761e-06,4.634178753283821e-07,8.67164361351847e-08,1.390859529902191e-08,1.9519701551053226e-09,2.3918891199191914e-10,2.3623400889178594e-11,2.4111799544955673e-12,2.255943756876997e-13,1.948340262471642e-14,1.5624878871442114e-15,1.1695136358866484e-16,8.206636486863585e-18],[5.628314399334319e-06,6.319143807037212e-06,3.5473834278642657e-06,1.3275985448400079e-06,3.7263759305315194e-07,8.367515996226451e-08,1.565759987101792e-08,2.511348824581651e-09,3.5244953564699245e-10,4.396775822418824e-11,4.848916466460976e-12,4.3536488152783536e-13,4.0733529018230704e-14,3.5179411887750796e-15,2.8212425729855166e-16,2.1116846321804248e-17,1.4817978704508776e-18],[9.238669553389731e-07,1.0372640430405031e-06,5.822898463718566e-07,2.1792038228689828e-07,6.116708025045234e-08,1.3734967485288662e-08,2.570137006288084e-09,4.122286048261219e-10,5.785328542544348e-11,7.217144608777576e-12,8.102989887068641e-13,8.123870490122155e-14,6.686257867672676e-15,5.774570119109911e-16,4.6309651544787437e-17,3.4662520842818773e-18,2.4323163026627314e-19],[1.390118929146117e-07,1.5607446206625993e-07,8.761566078463198e-08,3.2789921396487926e-08,9.20365379510251e-09,2.066665355024065e-09,3.867219281188722e-10,6.20269816333058e-11,8.705035580983023e-12,1.085945251864268e-12,1.2192361204823904e-13,1.244443044968493e-14,1.1436790305812777e-15,8.68884765697778e-17,6.968094577097388e-18,5.2155806717694305e-19,3.659844000764775e-20],[1.930778145392482e-08,2.1677653191624723e-08,1.2169203619218344e-08,4.554291168480422e-09,1.2783232594536274e-09,2.870453899776253e-10,5.37129760267783e-11,8.615114725170365e-12,1.2090686704733963e-12,1.5083021426664385e-13,1.6934338538548706e-14,1.728444512216469e-15,1.617164077352659e-16,1.3718957569669228e-17,9.678196909923064e-19,7.244077442186512e-20,5.08326781548319e-21],[2.4901649055922384e-09,2.7958122139615576e-09,1.5694876106764516e-09,5.873764453291586e-10,1.6486802102509954e-10,3.702084354642518e-11,6.927474717692718e-12,1.1111093419751371e-12,1.559361120203635e-13,1.9452887798945185e-14,2.184057014978285e-15,2.229210992394996e-16,2.085690291045555e-17,1.8013012765512022e-18,1.4189552548922752e-19,9.342837996676384e-21,6.555996684574886e-22],[2.9975098487543763e-10,3.3654295857263353e-10,1.8892542256681388e-10,7.070482263429651e-11,1.9845814855777392e-11,4.456345155712174e-12,8.338874926173719e-13,1.3374861994617008e-13,1.8770645691287595e-14,2.3416209357501986e-15,2.629035690743332e-16,2.6833893167674822e-17,2.51062778003995e-18,2.1682974910257641e-19,1.7388844395973436e-20,1.2784679399911928e-21,7.891712145762687e-23],[3.382707182816042e-11,3.79790673169226e-11,2.1320343090745427e-11,7.979080084896416e-12,2.239611672647969e-12,5.029011255325585e-13,9.410468533104016e-14,1.5093609035901986e-14,2.1182782112425527e-15,2.6425327550087023e-16,2.966881966593979e-17,3.0282203475972625e-18,2.8332579552483564e-19,2.4469362462387965e-20,1.962341136712969e-21,1.4688016057786598e-22,1.0124032614861544e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.12426498666888064, "-10": 5.045754120154074e-08, "-11": 5.073148003346554e-09, "-12": 4.686293652051268e-10, "-13": 4.003096899576869e-11, "-14": 3.1789371696001764e-12, "-15": 2.3440317247850207e-13, "-16": 1.4598704026454784e-14, "-2": 0.05653752310479127, "-3": 0.018331405955721376, "-4": 0.00469803878686869, "-5": 0.0009909566376145704, "-6": 0.00017717084122703062, "-7": 2.744967444528299e-05, "-8": 3.7490874972651735e-06, "-9": 4.5757229115751354e-07, "0": 0.24866459487393144, "1": 0.23545485486003145, "10": 6.7579178127988e-06, "11": 1.092718346185762e-06, "12": 1.623319781512198e-07, "13": 2.2300498170538088e-08, "14": 2.848028207255617e-09, "15": 3.377300521923602e-10, "16": 3.382707182816042e-11, "2": 0.16922813218839414, "3": 0.08824201931864674, "4": 0.036369735333471924, "5": 0.012337355344475122, "6": 0.0035473459931671955, "7": 0.0008838781144028411, "8": 0.0001941442974343587, "9": 3.8106815709231305e-05} |
| Raw goal margin distribution | {"-1": 0.14829137493082076, "-10": 9.895615545061161e-09, "-11": 7.974574404268127e-10, "-12": 5.898899350342294e-11, "-13": 4.018521229373737e-12, "-14": 2.35260400408847e-13, "-2": 0.058386705973842476, "-3": 0.015819954347984846, "-4": 0.003333723337162914, "-5": 0.0005728781339623669, "-6": 8.296941685696072e-05, "-7": 1.0374185063270266e-05, "-8": 1.140541221680635e-06, "-9": 1.1184299584086481e-07, "0": 0.28332570089625353, "1": 0.24311744658229123, "10": 1.1452007227271343e-06, "11": 1.4841923666834077e-07, "12": 1.7656212423943965e-08, "13": 1.9343573412802072e-09, "14": 1.8212231027608346e-10, "2": 0.1510086183555611, "3": 0.06580166240152636, "4": 0.022300010881700794, "5": 0.006162850685838328, "6": 0.0014354276819576975, "7": 0.00028864308029468794, "8": 5.103428395120994e-05, "9": 8.048291746833496e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Everton", "away_goals": 1.0, "away_xg": 2.15, "date": "2026-11-02T00:00:00+00:00", "home": "Newcastle", "home_goals": 0.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-10-24T00:00:00+00:00", "home": "Arsenal", "home_goals": 2.0, "home_xg": 1.96, "source": "pipeline training history"}, {"away": "Chelsea", "away_goals": 2.0, "away_xg": 1.47, "date": "2026-10-17T00:00:00+00:00", "home": "Everton", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 2.0, "away_xg": 1.68, "date": "2026-10-11T00:00:00+00:00", "home": "Hull", "home_goals": 2.0, "home_xg": 1.33, "source": "pipeline training history"}, {"away": "Ipswich", "away_goals": 0.0, "away_xg": 1.44, "date": "2026-09-19T00:00:00+00:00", "home": "Everton", "home_goals": 1.0, "home_xg": 2.24, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": 1.11, "date": "2026-09-12T00:00:00+00:00", "home": "Tottenham", "home_goals": 0.0, "home_xg": 0.69, "source": "pipeline training history"}, {"away": "Man United", "away_goals": 2.0, "away_xg": 0.69, "date": "2026-09-06T00:00:00+00:00", "home": "Everton", "home_goals": 2.0, "home_xg": 1.01, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 1.0, "away_xg": 1.84, "date": "2026-08-29T00:00:00+00:00", "home": "Bournemouth", "home_goals": 1.0, "home_xg": 2.15, "source": "pipeline training history"}, {"away": "Crystal Palace", "away_goals": 0.0, "away_xg": 1.96, "date": "2026-08-22T00:00:00+00:00", "home": "Everton", "home_goals": 2.0, "home_xg": 1.12, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Tottenham", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 49.0% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.2% |
| Raw p btts yes | 45.9% |
| P home draw | 79.5% |
| P draw away | 45.4% |
| P home away | 75.1% |
| Raw p home draw | 77.4% |
| Raw p draw away | 51.0% |
| Raw p home away | 71.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2544 |
| Totals anchor target over 2 5 | 0.5599 |
| Totals anchor reference over odds | 1.74 |
| Totals anchor reference under odds | 2.19 |
| Totals anchor reference last update utc | 2026-11-05T12:26:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4266 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.8, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.01, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 5.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.22, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.22, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.93, "draw": 4.21, "home": 1.74}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.15}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.22, "home_away": 1.27, "home_draw": 1.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.15}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:15Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.22, "under": 4.09}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:10Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.21, "home_away": 1.27, "home_draw": 1.21}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.83, "draw": 4.07, "home": 1.72}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:36Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.74, "under": 2.19}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.72 |
| Reference draw odds | 4.07 |
| Reference away odds | 4.83 |
| Market reference 1x2 last update utc | 2026-11-05T12:26:15Z |
| Market reference home last update utc | 2026-11-05T12:26:15Z |
| Market reference draw last update utc | 2026-11-05T12:26:15Z |
| Market reference away last update utc | 2026-11-05T12:26:15Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-05T12:26:15Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:26:15Z |
| Market best over 2 5 last update utc | 2026-11-05T12:19:13Z |
| Market best under 2 5 last update utc | 2026-11-05T12:19:13Z |
| Home probability edge | -2.4% |
| Draw probability edge | +1.5% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | -0.0802 |
| Raw ev home | -0.1471 |
| Raw edge prob draw | 0.0495 |
| Raw ev draw | 0.1928 |
| Raw edge prob away | 0.0307 |
| Raw ev away | 0.1166 |
| Market p home draw | 79.8% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T12:19:13Z |
| Market reference home draw last update utc | 2026-11-05T12:26:19Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.5% |
| Market draw away odds | 2.22 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T12:19:13Z |
| Market reference draw away last update utc | 2026-11-05T12:26:19Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.7% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T12:19:13Z |
| Market reference home away last update utc | 2026-11-05T12:26:19Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.22 |
| Market reference dc home draw odds | 1.21 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 80.3% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-05T12:25:15Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market reference over 1 5 last update utc | 2026-11-05T12:26:15Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.4% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T12:26:36Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.79 |
| Market reference under 3 5 last update utc | 2026-11-05T12:26:36Z |
| Market under 3 5 bookmakers | 2 |
| Count model | {"corners": {"alpha": 0.009288361750668784, "mu": 9.755785148145803, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,448.4574 |
| Elo away rating | 1,377.6232 |
| Elo rating diff | 130.8342 |
| Elo home expectancy | 0.6799 |

</details>


---

## 2026-11-07 — Arsenal vs Hull City

The model's most likely 1X2 outcome is **Arsenal win** at **78.5%**. Expected goals are 1.67 for Arsenal and 0.60 for Hull City (2.27 combined). The most likely exact score is 1-0 at 20.8%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 44.1%; Under 3.5 goals: 78.6%; Double Chance 1X: 93.1%; Double Chance X2: 21.5%; Double Chance 12 (either team wins): 85.4%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 34.2%; BTTS No (at least one team does not score): 65.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 78.5% | 1.27 |
| Draw | 14.6% | 6.84 |
| Hull City win | 6.9% | 14.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.67 |
| Hull City expected goals | 0.60 |
| Expected total goals | 2.27 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 69.6% |
| Under 1.5 | 30.4% |
| Over 2.5 | 44.1% |
| Under 2.5 | 55.9% |
| Over 3.5 | 21.4% |
| Under 3.5 | 78.6% |
| Over 4.5 | 9.3% |
| Under 4.5 | 90.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.80% |
| 2 | 2-0 | 18.03% |
| 3 | 2-1 | 10.79% |
| 4 | 3-0 | 10.03% |
| 5 | 0-0 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 78.5% | 85.2% | 1.19 | -6.6% |
| Draw | 14.6% | 10.2% | 8.40 | +22.9% |
| Hull City win | 6.9% | 4.5% | 19.00 | +30.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:00:00+00:00 |
| Fixture id | 842fcc5b9feb8c63054a661ad1fc8926 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:19:13Z |
| Market best draw last update utc | 2026-11-05T12:19:13Z |
| Market best away last update utc | 2026-11-05T12:19:13Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Hull |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6700 |
| Dc lambda away | 0.5987 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:25:21.757952+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 34.2% |
| P btts no | 65.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.47 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.29 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.68 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.78 |
| Fair Under 4.5 odds | 1.10 |
| Score matrix json | [[0.0646285836884731,0.030930767145648214,0.01030998558665722,0.00205749554658873,0.0003079505704918986,3.6873393587079084e-05,3.679289483741495e-06,3.1467918707606406e-07,2.354941553644372e-08,1.5665336349162435e-09,9.378682298817783e-11,5.104476864288569e-12,2.5466666096824594e-13,1.1728185928307836e-14,5.01539227900576e-16,2.0017772462852777e-17],[0.20798801686027021,0.0646171953416341,0.017217684739745304,0.0034360193209620727,0.000514277715869566,6.15785987992557e-05,6.144416581852927e-06,5.255145113148198e-07,3.932754406916793e-08,2.6161125089351586e-09,1.566240745324168e-10,8.52448072520921e-12,4.2529354143321556e-13,1.9586080522173978e-14,8.3757093916628885e-16,3.342969711843235e-17],[0.180257714707202,0.10791851515145887,0.015222082330066899,0.002869077601066756,0.0004294221124798594,5.141815630726802e-05,5.1305904710924015e-06,4.3880484147764624e-07,3.283851610072507e-08,2.18445506271333e-09,1.3078116915330563e-10,7.1179450476940466e-12,3.5512028880639225e-13,1.635438560430595e-14,6.993720920619269e-16,2.791381137696427e-17],[0.10034351253126025,0.06007467084027532,0.017983056330837112,0.001691026256430924,0.00023904509826286747,2.8622788323558543e-05,2.856030156962019e-06,2.442681534108601e-07,1.8280116649728305e-08,1.2160139404596159e-09,7.280155474678985e-11,3.96232477067775e-12,1.9768372858731952e-13,9.103945978081181e-15,3.893173304555702e-16,1.5538696284091634e-17],[0.041893437918036965,0.025081187909477807,0.007507929859818156,0.00149830784154228,0.00010566938067917394,1.1950020239729522e-05,1.1923932006611307e-06,1.0198200623167752e-07,7.631952606415785e-09,5.076860799171448e-10,3.039466465927296e-11,1.6542714382235266e-12,8.253299891608773e-14,3.800899390711374e-15,1.6254006863448462e-16,6.487409018116906e-18],[0.013992415424330766,0.008377121048211174,0.002507649856305603,0.0005004350751401476,7.490138539501264e-05,4.225984961037669e-06,3.9825953280417077e-07,3.406200751039211e-08,2.549073474865047e-09,1.6956723745730594e-10,1.0151823190730883e-11,5.525269430863015e-13,2.756603574309505e-14,1.2695010460819999e-15,5.428841070247295e-17,2.166795720767502e-18],[0.003894557619224706,0.002331633218146744,0.0006979629004754069,0.00013928783385214327,2.0847562935659796e-05,2.496246044389805e-06,1.1736652340727259e-07,9.480596941469919e-09,7.094924802072965e-10,4.71962385752152e-11,2.825592233899389e-12,1.537867445160284e-13,7.672550541089021e-15,3.533446386272409e-16,1.5110282043890105e-17,6.030917842065265e-19],[0.0009291306502942195,0.0005562613523883501,0.0001665140914590068,3.323011450807042e-05,4.973635416726813e-06,5.955332896011913e-07,5.9423317370372026e-08,2.394787342410299e-09,1.6926472117392734e-10,1.1259679821494178e-11,6.741059207314709e-13,3.66891421078149e-14,1.8304522799887212e-15,8.429797834935105e-17,3.6048834178921526e-18,1.4388054213933054e-19],[0.00019395612249331991,0.00011611961672771208,3.47598343781469e-05,6.936789953009745e-06,1.0382469244969022e-06,1.243176378156955e-07,1.240462384832275e-08,1.0609322712506675e-09,3.741155620269904e-11,2.350459365431262e-12,1.407196829568187e-13,7.658862333929873e-15,3.8210710896604883e-16,1.759721198465309e-17,7.525197985379366e-19,3.003507854007869e-20],[3.59896544780089e-05,2.1546651017902842e-05,6.449883679363657e-06,1.2871605721234329e-06,1.926525834562703e-07,2.3067840153709144e-08,2.3017480474027352e-09,1.9686197773001882e-10,1.4732415448148896e-11,4.617847097316108e-13,2.6111332309426268e-14,1.4211451824742803e-15,7.090213316546696e-17,3.265262116826213e-18,1.3963430073301232e-19,5.57317853636985e-21],[6.010275373194091e-06,3.598292561181415e-06,1.0771311256053647e-06,2.1495592553429494e-07,3.217299789963142e-08,3.852331276848819e-09,3.8439212060386546e-10,3.287596710304607e-11,2.4603146387464904e-12,1.6366289974834829e-13,4.61698371377779e-15,2.3733136691205985e-16,1.1840662297320006e-17,5.452990525312188e-19,2.3318940154360485e-20,9.30721291809711e-22],[9.124695462817253e-07,5.46286513814961e-07,1.6352817274405968e-07,3.2634234484103134e-08,4.884448544060337e-09,5.848542294735263e-10,5.835774271608447e-11,4.9911721050057506e-12,3.735206862800095e-13,2.4847016584726508e-14,1.4875663658129224e-15,3.814975612944984e-17,1.797628741321536e-18,8.278635306298601e-20,3.5402409076494885e-21,1.4130048660333207e-22],[1.2698541016737938e-07,7.602491207337503e-08,2.275768235164209e-08,4.541599956238747e-09,6.797527702008998e-10,8.139225524891337e-11,8.121456683614472e-12,6.94605140032202e-13,5.1981655438858337e-14,3.4578782440515573e-15,2.0701975850449823e-16,1.1267335155067812e-17,2.648793291404314e-19,1.1521106696440887e-20,4.926837784133611e-22,1.966432778090161e-23],[1.6312749499257172e-08,9.766282163607178e-09,2.923488382615544e-09,5.834212159830594e-10,8.73221313149084e-11,1.0455779678193282e-11,1.043295353964244e-12,8.923009056951096e-14,6.677646846303798e-15,4.442045863362856e-16,2.659409027721604e-17,1.4474199490045898e-18,7.221300345401843e-20,1.5670402694188759e-21,6.329094853504106e-23,2.526111092119266e-24],[1.9458789716595303e-09,1.1649785399035356e-09,3.4873057836642215e-10,6.959385208809615e-11,1.0416288136706195e-11,1.2472257855138296e-12,1.2445029518791757e-13,1.0643880535675078e-14,7.965482813907513e-16,5.298728848290467e-17,3.172296677712505e-18,1.7265661083416963e-19,8.613984105374157e-21,3.967005605964002e-22,7.993608597464439e-24,3.0132912017404586e-25],[2.1664130303015743e-10,1.2970101047529664e-10,3.882535759114056e-11,7.748119497069723e-12,1.1596806726109363e-12,1.3885787517200458e-13,1.385547328722331e-14,1.185019305994865e-15,8.868242070561754e-17,5.8992544696555976e-18,3.5318254417013376e-19,1.9222445842037687e-20,9.59024054449693e-22,4.416601834547973e-23,1.888697099094384e-24,3.552050692892238e-26]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.051268932516734145, "-10": 1.0267569265503587e-10, "-11": 5.546520596065565e-12, "-12": 2.7496765227876596e-13, "-13": 1.2593670678851089e-14, "-14": 5.349689250190083e-16, "-15": 2.0017772462852777e-17, "-2": 0.014205276984525193, "-3": 0.0026261520278803067, "-4": 0.00037491183229816817, "-5": 4.347541312059742e-05, "-6": 4.238889480046708e-06, "-7": 3.5626566995714565e-07, "-8": 2.630035535705699e-08, "-9": 1.7304771940158352e-09, "0": 0.14626890278143398, "1": 0.3354653543146951, "10": 6.579913545722688e-06, "11": 9.914887002704765e-07, "12": 1.3710817102885005e-07, "13": 1.7516553396751848e-08, "14": 2.075579982134827e-09, "15": 2.1664130303015743e-10, "2": 0.24836220618263205, "3": 0.1280767384189514, "4": 0.05100281368543198, "5": 0.016497696087863337, "6": 0.004486898732626945, "7": 0.0010519200735216569, "8": 0.0002166132292054974, "9": 3.9756105395103184e-05} |
| Raw goal margin distribution | {"-1": 0.09219140743347973, "-10": 1.846306554556313e-10, "-11": 9.97371146635764e-12, "-12": 4.944447566561871e-13, "-13": 2.2645843547806836e-14, "-14": 9.619770826041717e-16, "-15": 3.5995807332855864e-17, "-2": 0.025543821841001676, "-3": 0.004722326752279236, "-4": 0.0006741636267100215, "-5": 7.817715968694336e-05, "-6": 7.622339064557738e-06, "-7": 6.406342383442518e-07, "-8": 4.729310046735091e-08, "-9": 3.111731027280243e-09, "0": 0.248413707419472, "1": 0.268458542347065, "10": 5.2656227432575845e-06, "11": 7.934459037415374e-07, "12": 1.0972179172859762e-07, "13": 1.4017746784740153e-08, "14": 1.6609976838501043e-09, "15": 1.7336874784716692e-10, "2": 0.1987536268301014, "3": 0.10249432336986901, "4": 0.04081536540654395, "5": 0.013202398956757662, "6": 0.0035906727115848644, "7": 0.0008418065411855592, "8": 0.0001733462815687587, "9": 3.1815106885087254e-05} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Arsenal", "away_goals": 1.0, "away_xg": 0.96, "date": "2026-11-01T00:00:00+00:00", "home": "Liverpool", "home_goals": 0.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-10-24T00:00:00+00:00", "home": "Arsenal", "home_goals": 2.0, "home_xg": 1.96, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 1.0, "away_xg": 1.14, "date": "2026-10-18T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.9, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 1.0, "away_xg": 0.62, "date": "2026-10-10T00:00:00+00:00", "home": "Arsenal", "home_goals": 2.0, "home_xg": 2.33, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 0.0, "away_xg": 1.63, "date": "2026-09-19T00:00:00+00:00", "home": "Brighton", "home_goals": 3.0, "home_xg": 1.31, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 2.0, "away_xg": 1.88, "date": "2026-09-12T00:00:00+00:00", "home": "Sunderland", "home_goals": 0.0, "home_xg": 1.8, "source": "pipeline training history"}, {"away": "Chelsea", "away_goals": 1.0, "away_xg": 0.39, "date": "2026-09-06T00:00:00+00:00", "home": "Arsenal", "home_goals": 2.0, "home_xg": 2.05, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 1.0, "away_xg": 1.05, "date": "2026-08-31T00:00:00+00:00", "home": "Aston Villa", "home_goals": 0.0, "home_xg": 0.32, "source": "pipeline training history"}, {"away": "Coventry", "away_goals": 0.0, "away_xg": 0.2, "date": "2026-08-21T00:00:00+00:00", "home": "Arsenal", "home_goals": 3.0, "home_xg": 1.88, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 2.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Crystal Palace", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 12.3% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 37.2% |
| P home draw | 93.1% |
| P draw away | 21.5% |
| P home away | 85.4% |
| Raw p home draw | 87.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 75.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4413 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.87, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.44, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.65, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "line": -2.0, "market_key": "spreads", "opposite_price": 2.02, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 19.0, "draw": 8.4, "home": 1.19}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 17.83, "draw": 8.31, "home": 1.16}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 8.31 |
| Reference away odds | 17.83 |
| Market reference 1x2 last update utc | 2026-11-05T12:26:15Z |
| Market reference home last update utc | 2026-11-05T12:26:15Z |
| Market reference draw last update utc | 2026-11-05T12:26:15Z |
| Market reference away last update utc | 2026-11-05T12:26:15Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.64 |
| Market reference over 2 5 last update utc | 2026-11-05T12:26:16Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:26:16Z |
| Home probability edge | -6.7% |
| Draw probability edge | +4.4% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -20.6% |
| Under 2.5 probability edge | +20.6% |
| Raw edge prob home | -0.2241 |
| Raw ev home | -0.2522 |
| Raw edge prob draw | 0.1459 |
| Raw ev draw | 1.0867 |
| Raw edge prob away | 0.0781 |
| Raw ev away | 1.3411 |
| Count model | {"corners": {"alpha": 0.009288361750668784, "mu": 9.88825063485941, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,656.9795 |
| Elo away rating | 1,392.5184 |
| Elo rating diff | 324.4611 |
| Elo home expectancy | 0.8662 |

</details>


---

## 2026-11-07 — Fulham vs Newcastle United

The model's most likely 1X2 outcome is **Fulham win** at **44.1%**. Expected goals are 1.41 for Fulham and 1.41 for Newcastle United (2.82 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.7%; Double Chance 1X: 69.8%; Double Chance X2: 55.9%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fulham win | 44.1% | 2.27 |
| Draw | 25.8% | 3.88 |
| Newcastle United win | 30.2% | 3.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fulham expected goals | 1.41 |
| Newcastle United expected goals | 1.41 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.8% |
| Under 2.5 | 46.2% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.17% |
| 2 | 2-1 | 10.04% |
| 3 | 1-0 | 9.23% |
| 4 | 2-0 | 7.11% |
| 5 | 1-2 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fulham win | 44.1% | 47.3% | 2.16 | -4.8% |
| Draw | 25.8% | 25.4% | 3.88 | -0.0% |
| Newcastle United win | 30.2% | 27.3% | 3.52 | +6.2% |
| Over 2.5 | 53.8% | 58.1% | 1.71 | -7.9% |
| Under 2.5 | 46.2% | 41.9% | 2.32 | +7.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:00:00+00:00 |
| Fixture id | 3903e98a54db0f2cc23095407fe9dad8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:19:13Z |
| Market best draw last update utc | 2026-11-05T12:19:13Z |
| Market best away last update utc | 2026-11-05T12:26:15Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fulham |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4092 |
| Dc lambda away | 1.4115 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:25:21.757952+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.46 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.55 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.38 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.0646645985960237,0.06308112819303344,0.048708594893713986,0.022916885841129494,0.008086616814773967,0.00228280131820082,0.0005370171046952076,0.0001082832627373489,1.9104804624869458e-05,2.9962037676004947e-06,4.2290478620062103e-07,5.426517021468492e-08,6.382799142907989e-09,6.930093278706973e-10,6.986864149499211e-11],[0.09225965700803682,0.1216986002708524,0.0686417753845118,0.0322952393484526,0.011395929942786463,0.0032169997035087993,0.0007567824027477015,0.0001525963829368932,2.6923127441611144e-05,4.222350212947796e-06,5.959715201549431e-07,7.647228652780145e-08,8.9948532912512e-09,9.766118428764382e-10,9.846121832061219e-11],[0.07113682544704676,0.10040740313455727,0.057035717953260984,0.022755763846019066,0.008029762151189987,0.0022667516024855584,0.000533241492776697,0.00010752195444047743,1.8970484270058014e-05,2.97513832563164e-06,4.199314649838221e-07,5.3883647500359353e-08,6.337923528506282e-09,6.881369797553933e-10,6.937741528775918e-11],[0.03341612847149741,0.04716581969392744,0.033286539302384774,0.012605456092028861,0.0037719361519648947,0.0010647939697282995,0.0002504872281969241,5.050784063683076e-05,8.911279573568551e-06,1.3975546966709616e-06,1.9726047226508706e-07,2.5311544000866553e-08,2.9772043599098286e-09,3.23248522505569e-10,3.2589655325593865e-11],[0.011772780500883075,0.01661691128804646,0.011727125156801067,0.005517490066167581,0.0015670856799380004,0.0003751357879464567,8.824873768223375e-05,1.7794333113669216e-05,3.139518047134331e-06,4.92370164781934e-07,6.949650805473276e-08,8.917467860312327e-09,1.0488939035946882e-09,1.1388314795170817e-10,1.1481607124981797e-11],[0.0033181189338601326,0.004683421045946224,0.003305251127345007,0.0015550861799013909,0.0005487388704552454,0.00012468289973931076,2.487261249546881e-05,5.015273461987276e-06,8.848626944680241e-07,1.3877288938736454e-07,1.958735909467393e-08,2.5133585856945227e-09,2.956272497280433e-10,3.2097585565093405e-11,3.236052688631018e-12],[0.000779333965782003,0.0011000055061070402,0.0007763116754776943,0.00036524654597158647,0.00012888351762397972,3.6383010431365814e-05,6.889037582461333e-06,1.1779484203312575e-06,2.078296669282027e-07,3.259389683885299e-08,4.600526547338004e-09,5.903181148913347e-10,6.94346289316868e-11,7.538831232119376e-12,7.600588844404069e-13],[0.0001568947714037478,0.00022145206035047092,0.00015628632679947027,7.353108661024287e-05,2.5946706961546065e-05,7.324592992532358e-06,1.7230723018070844e-06,2.7965116615168633e-07,4.184007051572343e-08,6.561772254540264e-09,9.261736209035864e-10,1.188422804059775e-10,1.3978513335819792e-11,1.5177103202834868e-12,1.530143303942971e-13],[2.7637667646747858e-05,3.900970305698578e-05,2.7530487594767634e-05,1.2952807255816427e-05,4.5706205319321385e-06,1.2902575717731788e-06,3.0352636472577485e-07,6.120256656995599e-08,8.691421687855298e-09,1.155883520668447e-09,1.6314934199972273e-10,2.0934562821024404e-11,2.4623733621870822e-12,2.673509960895503e-13,2.6954111796017653e-14],[4.3275469347623465e-06,6.108197082618613e-06,4.310764523477027e-06,2.0281697447458725e-06,7.156745325162142e-07,2.0203044161137668e-07,4.7526607746987216e-08,9.583188521719104e-09,1.6907963406572308e-09,2.1343221093169067e-10,2.5546165613670137e-11,3.277964853064377e-12,3.8556206811565234e-13,4.186221494595385e-14,4.220514747228445e-15],[6.098523377857177e-07,8.607874915388828e-07,6.074873044515163e-07,2.85816440331099e-07,1.0085524046954846e-07,2.8470803200507678e-08,6.697607970164433e-09,1.350494867303525e-09,2.38272655759417e-10,3.736826640839929e-11,4.24535609274858e-12,4.619417325696801e-13,5.433469171946474e-14,5.8993628571887845e-15,5.94769005179539e-16],[7.812947643830798e-08,1.1027731119759658e-07,7.78264870018303e-08,3.661655036300925e-08,1.2920778761881483e-08,3.6474549821523406e-09,8.580447621106762e-10,1.7301476173420955e-10,3.052561528523572e-11,4.787327864472807e-12,6.757163477631342e-13,6.978834740769758e-14,6.960932595408454e-15,7.557798876778441e-16,7.619711870767374e-17],[9.175221854736712e-09,1.2950538540735449e-08,9.139639953691727e-09,4.3001052669414995e-09,1.5173660067956848e-09,4.283429275612489e-10,1.0076543978733383e-10,2.0318180735656836e-11,3.584809540040038e-12,5.622051657108507e-13,7.935349991106951e-14,1.0182271093433296e-14,9.639945596282896e-16,8.875585065858903e-17,8.948293278102969e-18],[9.946175729516161e-10,1.4038715810618704e-09,9.90760403651661e-10,4.661424357639737e-10,1.6448636543641559e-10,4.643347155491584e-11,1.0923232020481332e-11,2.202542884525291e-12,3.88602545056469e-13,6.094448137311371e-14,8.602122840879153e-15,1.1037842923501316e-15,1.2982974912444264e-16,1.134598066221945e-17,9.700179334335488e-19],[1.0011773103319656e-10,1.4131304451096606e-10,9.972947020911275e-11,4.692167550235599e-11,1.6557119179506225e-11,4.673971124677477e-12,1.0995273310870304e-12,2.2170691741107114e-13,3.911654704563702e-14,6.13464245957765e-15,8.658855869013995e-16,1.1110640099815872e-16,1.30686006928018e-17,1.4189169954364106e-18,1.1514368608621072e-19]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.15865183294636065, "-10": 5.060497263865593e-07, "-11": 6.39807501410171e-08, "-12": 7.428788401072186e-09, "-13": 7.914705461913095e-10, "-14": 6.986864149499211e-11, "-2": 0.09019186893215067, "-3": 0.03684876735180313, "-4": 0.011890648864506475, "-5": 0.003156529517054644, "-6": 0.0007100536074447635, "-7": 0.00013838800976381238, "-8": 2.3773479598349987e-05, "-9": 3.6491532588163473e-06, "0": 0.25770331908976185, "1": 0.23205799739575209, "10": 7.297519884919494e-07, "11": 9.211769705819744e-08, "12": 1.0678822906007694e-08, "13": 1.1359306174625822e-09, "14": 1.0011773103319656e-10, "2": 0.13172137794098687, "3": 0.05373082330559293, "4": 0.017310823834160136, "5": 0.004588108598115856, "6": 0.0010304492891745384, "7": 0.0002005144156911701, "8": 3.439153348318667e-05, "9": 5.2706301789065616e-06} |
| Raw goal margin distribution | {"-1": 0.19325764159315273, "-10": 6.164314324902358e-07, "-11": 7.793650189843193e-08, "-12": 9.04918713905544e-09, "-13": 9.641094483862103e-10, "-14": 8.510868501093738e-11, "-2": 0.10986490075156755, "-3": 0.044886376298166775, "-4": 0.014484287473336343, "-5": 0.0038450450824063257, "-6": 0.0008649335026963083, "-7": 0.0001685737876143339, "-8": 2.895905149229127e-05, "-9": 4.445121997734804e-06, "0": 0.26619880348637714, "1": 0.19294012076139966, "10": 6.067381360073981e-07, "11": 7.658947243416998e-08, "12": 8.878700170634332e-09, "13": 9.44447478515618e-10, "14": 8.324094550794341e-11, "2": 0.10951718472106918, "3": 0.04467345083354707, "4": 0.014392748703015873, "5": 0.0038146938994617643, "6": 0.0008567470741065408, "7": 0.0001667138215964111, "8": 2.859417343027206e-05, "9": 4.382163229102849e-06} |
| Research history json | {"away": [{"away": "Everton", "away_goals": 1.0, "away_xg": 2.15, "date": "2026-11-02T00:00:00+00:00", "home": "Newcastle", "home_goals": 0.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 2.0, "away_xg": 0.95, "date": "2026-10-25T00:00:00+00:00", "home": "Crystal Palace", "home_goals": 0.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Aston Villa", "away_goals": 1.0, "away_xg": 1.57, "date": "2026-10-17T00:00:00+00:00", "home": "Newcastle", "home_goals": 0.0, "home_xg": 0.99, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 1.0, "away_xg": 1.84, "date": "2026-10-12T00:00:00+00:00", "home": "Coventry", "home_goals": 4.0, "home_xg": 1.43, "source": "pipeline training history"}, {"away": "Hull", "away_goals": 1.0, "away_xg": 1.59, "date": "2026-09-19T00:00:00+00:00", "home": "Newcastle", "home_goals": 2.0, "home_xg": 1.44, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 1.0, "away_xg": 0.85, "date": "2026-09-14T00:00:00+00:00", "home": "Leeds", "home_goals": 4.0, "home_xg": 1.91, "source": "pipeline training history"}, {"away": "Bournemouth", "away_goals": 2.0, "away_xg": 1.37, "date": "2026-09-05T00:00:00+00:00", "home": "Newcastle", "home_goals": 2.0, "home_xg": 0.71, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 2.0, "away_xg": 0.75, "date": "2026-08-29T00:00:00+00:00", "home": "Tottenham", "home_goals": 0.0, "home_xg": 1.04, "source": "pipeline training history"}, {"away": "Liverpool", "away_goals": 2.0, "away_xg": 2.98, "date": "2026-08-23T00:00:00+00:00", "home": "Newcastle", "home_goals": 2.0, "home_xg": 1.57, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Fulham", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [{"away": "Newcastle", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Fulham", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 1.0, "away_xg": null, "date": "2025-10-25T00:00:00+00:00", "home": "Newcastle", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 2.0, "away_xg": null, "date": "2025-02-01T00:00:00+00:00", "home": "Newcastle", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 1.0, "away_xg": null, "date": "2024-09-21T00:00:00+00:00", "home": "Fulham", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 1.0, "away_xg": null, "date": "2024-04-06T00:00:00+00:00", "home": "Fulham", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 0.0, "away_xg": null, "date": "2023-12-16T00:00:00+00:00", "home": "Newcastle", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 0.0, "away_xg": null, "date": "2023-01-15T00:00:00+00:00", "home": "Newcastle", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Fulham", "away_goals": 1.0, "away_xg": 2.24, "date": "2026-10-31T00:00:00+00:00", "home": "Aston Villa", "home_goals": 1.0, "home_xg": 1.83, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 1.0, "away_xg": 0.55, "date": "2026-10-24T00:00:00+00:00", "home": "Coventry", "home_goals": 0.0, "home_xg": 0.51, "source": "pipeline training history"}, {"away": "Hull", "away_goals": 0.0, "away_xg": 0.16, "date": "2026-10-17T00:00:00+00:00", "home": "Fulham", "home_goals": 1.0, "home_xg": 1.38, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 1.0, "away_xg": 1.81, "date": "2026-10-10T00:00:00+00:00", "home": "Ipswich", "home_goals": 2.0, "home_xg": 1.15, "source": "pipeline training history"}, {"away": "Man United", "away_goals": 1.0, "away_xg": 1.6, "date": "2026-09-20T00:00:00+00:00", "home": "Fulham", "home_goals": 1.0, "home_xg": 1.62, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 0.0, "away_xg": 0.68, "date": "2026-09-12T00:00:00+00:00", "home": "Liverpool", "home_goals": 0.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Crystal Palace", "away_goals": 3.0, "away_xg": 1.97, "date": "2026-09-05T00:00:00+00:00", "home": "Fulham", "home_goals": 2.0, "home_xg": 3.14, "source": "pipeline training history"}, {"away": "Fulham", "away_goals": 0.0, "away_xg": 0.95, "date": "2026-08-30T00:00:00+00:00", "home": "Sunderland", "home_goals": 1.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Chelsea", "away_goals": 3.0, "away_xg": 1.7, "date": "2026-08-24T00:00:00+00:00", "home": "Fulham", "home_goals": 2.0, "home_xg": 1.35, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Fulham", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 36.6% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 36.7% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.9% |
| P home draw | 69.8% |
| P draw away | 55.9% |
| P home away | 74.2% |
| Raw p home draw | 63.3% |
| Raw p draw away | 63.4% |
| Raw p home away | 73.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5385 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.88, "home": 2.16}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.32}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.52, "draw": 3.78, "home": 2.07}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.07 |
| Reference draw odds | 3.78 |
| Reference away odds | 3.52 |
| Market reference 1x2 last update utc | 2026-11-05T12:26:15Z |
| Market reference home last update utc | 2026-11-05T12:26:15Z |
| Market reference draw last update utc | 2026-11-05T12:26:15Z |
| Market reference away last update utc | 2026-11-05T12:26:15Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-05T12:26:15Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:26:15Z |
| Market best over 2 5 last update utc | 2026-11-05T12:19:13Z |
| Market best under 2 5 last update utc | 2026-11-05T12:19:13Z |
| Home probability edge | -3.2% |
| Draw probability edge | +0.4% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | -0.1061 |
| Raw ev home | -0.2086 |
| Raw edge prob draw | 0.0121 |
| Raw ev draw | 0.0329 |
| Raw edge prob away | 0.0940 |
| Raw ev away | 0.2933 |
| Count model | {"corners": {"alpha": 0.009288361750668784, "mu": 10.272880036905677, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,459.2088 |
| Elo away rating | 1,451.5742 |
| Elo rating diff | 67.6346 |
| Elo home expectancy | 0.5961 |

</details>


---

## 2026-11-07 — Leeds United vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Leeds United win** at **37.0%**. Expected goals are 1.46 for Leeds United and 1.36 for Tottenham Hotspur (2.82 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 48.1%; Under 3.5 goals: 73.6%; Double Chance 1X: 65.0%; Double Chance X2: 63.0%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 87.7%; BTTS Yes (both teams score): 53.7%; BTTS No (at least one team does not score): 46.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 37.0% | 2.70 |
| Draw | 28.0% | 3.57 |
| Tottenham Hotspur win | 35.0% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.46 |
| Tottenham Hotspur expected goals | 1.36 |
| Expected total goals | 2.82 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 74.0% |
| Under 1.5 | 26.0% |
| Over 2.5 | 48.1% |
| Under 2.5 | 51.9% |
| Over 3.5 | 26.4% |
| Under 3.5 | 73.6% |
| Over 4.5 | 12.3% |
| Under 4.5 | 87.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.35% |
| 2 | 1-0 | 8.93% |
| 3 | 0-1 | 8.82% |
| 4 | 0-0 | 8.22% |
| 5 | 2-1 | 8.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 37.0% | 36.2% | 2.69 | -0.5% |
| Draw | 28.0% | 28.6% | 3.57 | -0.0% |
| Tottenham Hotspur win | 35.0% | 35.2% | 2.76 | -3.4% |
| Over 2.5 | 48.1% | 48.1% | 2.02 | -2.8% |
| Under 2.5 | 51.9% | 51.9% | 1.92 | -0.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T12:30:00+00:00 |
| Fixture id | 5c87852253fd11eea5d34ad723356607 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:26:15Z |
| Market best draw last update utc | 2026-11-05T12:19:13Z |
| Market best away last update utc | 2026-11-05T12:19:13Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4600 |
| Dc lambda away | 1.3604 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:25:21.757952+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.7% |
| P btts no | 46.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.17 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.85 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.79 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.16 |
| Fair Under 4.5 odds | 1.14 |
| Score matrix json | [[0.08219143040717848,0.08818021059959322,0.0602668819710825,0.02520276823975655,0.007904584236475711,0.0019833520304480302,0.0004147050579555181,7.432451258000831e-05,1.1655552376919178e-05,1.6247297335585137e-06,2.038317841634694e-07,2.324716501073091e-08,2.4304099234715523e-09,2.345454189975367e-10,2.1017918169128617e-11],[0.08934805991201328,0.13354019892575647,0.08114463718102145,0.03393355385058231,0.010642903680389658,0.0026704281962051683,0.0005583678857167622,0.0001000721359677256,1.569328854980932e-05,2.1875713565218514e-06,2.7444353566924563e-07,3.130048724253278e-08,3.272356640847648e-09,3.1579703984284166e-10,2.8298980938696583e-11],[0.06513848922036386,0.08172001903614778,0.053148506484075736,0.022844436491582253,0.007164918189331248,0.0017977612248383078,0.00037589931665753734,6.736964730419657e-05,1.0564892059310258e-05,1.4726967633544904e-06,1.8475836479513872e-07,2.1071827493109752e-08,2.2029859822173833e-09,2.1259799232009023e-10,1.9051180895379668e-11],[0.029234624951740933,0.03667653542729133,0.02300642223339436,0.009975172919021419,0.0032156670899502896,0.0008068482365799142,0.00016870633128935532,3.0235984832352084e-05,4.741599946610429e-06,6.609569558584675e-07,8.292089003185272e-08,9.45718854063109e-09,9.887160377053042e-10,9.541551616195465e-11,8.550307737104828e-12],[0.009840533296423523,0.012345520719540632,0.007744086486247661,0.0032384688000812603,0.0010531065829993312,0.0002715894919237687,5.678746599660056e-05,1.0177596462553516e-05,1.5960482554492733e-06,2.2248169567301582e-07,2.791162125987622e-08,3.1833409485587823e-09,3.3280718004106234e-10,3.211738017289793e-11,2.8780799521300912e-12],[0.0026499014977718277,0.0033244553785894615,0.002085361205600564,0.0008720689281079513,0.00027351528358572765,7.115479900571066e-05,1.529197520765973e-05,2.7406673294464396e-06,4.297907984487264e-07,5.991083621504645e-08,7.516162463335944e-09,8.572238610858773e-10,8.961976127661219e-11,8.648707469502832e-12,7.750218556374834e-13],[0.0005946474762742682,0.0007460198058406701,0.0004679625937316319,0.00019569542025341038,6.137781847493352e-05,1.540040782094385e-05,3.3386705998636154e-06,6.150156570472617e-07,9.644660899219741e-08,1.3444208241972166e-08,1.686654029913286e-09,1.9236413354436805e-10,2.011099843230044e-11,1.9408012237808504e-12,1.7391770633729153e-13],[0.00011437803728716029,0.0001434938927245164,9.001071244796767e-05,3.764122268694753e-05,1.1805775169711733e-05,2.9622061645965044e-06,6.19376621147627e-07,1.1509312179881018e-07,1.8551115206350837e-08,2.5859390865175375e-09,3.2442108176875974e-10,3.7000463160297616e-11,3.8682692189056535e-12,3.73305266729471e-13,3.345236748498232e-14],[1.925013380814459e-05,2.415041122504531e-05,1.5149046966417157e-05,6.335119841291848e-06,1.986943972077877e-06,4.985473294372983e-07,1.0424276476080734e-07,1.8682657788250342e-08,3.0376747653453545e-09,4.352205599593892e-10,5.4600947719992954e-11,6.227278275555881e-12,6.510401982411005e-13,6.282828859692384e-14,5.630124152842271e-15],[2.8798664143001572e-06,3.6129597264991173e-06,2.2663339383533054e-06,9.47749197139809e-07,2.9725160714790635e-07,7.45838820807602e-08,1.5594968853745126e-08,2.7949706339953606e-09,4.3830662974635395e-10,6.334730333003932e-11,8.168433377914384e-12,9.316158389863632e-13,9.739718279156071e-14,9.399263402609981e-15,8.422801429697363e-16],[3.877514609604711e-07,4.86456734723864e-07,3.051441175386412e-07,1.2760700773837086e-07,4.002260117765159e-08,1.0042135668972058e-08,2.0997404347111725e-09,3.763209089462856e-10,5.901455539357367e-11,8.226354252463068e-12,1.0700399913855597e-12,1.2543477740048645e-13,1.3113767962754375e-14,1.2655372131904893e-15,1.134064255038984e-16],[4.7461543459226226e-08,5.954326361257381e-08,3.735024172446347e-08,1.5619349385491862e-08,4.898845307865997e-09,1.2291772087609261e-09,2.570123698522912e-10,4.606242135188355e-11,7.223497955626136e-12,1.006921982697749e-12,1.2632421257975858e-13,1.4937795726920254e-14,1.6051510587136772e-15,1.5490425050708357e-16,1.3881170116745173e-17],[5.325270969853353e-09,6.680861810547074e-09,4.190764637546271e-09,1.752519235326037e-09,5.496592989267784e-10,1.3791590474176815e-10,2.8837252485128787e-11,5.1682869402902864e-12,8.104895281574149e-13,1.1297846661843314e-13,1.4173805001063477e-14,1.6165328927572554e-15,1.7522493253137688e-16,1.7380536919136093e-17,1.5574923793576962e-18],[5.515431037190119e-10,6.919428662629016e-10,4.340412625447679e-10,1.8150999336013316e-10,5.692870793510811e-11,1.4284074291075018e-11,2.986700175148968e-12,5.352841265909587e-13,8.394312935854381e-14,1.1701281396740146e-14,1.4679937314081652e-15,1.6742576555869828e-16,1.7503779143428903e-17,1.7513827753173754e-18,1.6131088648683509e-19],[5.3043542770837155e-11,6.654620604283826e-11,4.1743040786583473e-11,1.7456356595182123e-11,5.4750033748637256e-12,1.373741962308096e-12,2.8723985018746976e-13,5.14798685214691e-14,8.07306073165275e-15,1.125347078145675e-15,1.4118132881041355e-16,1.6101834464922238e-17,1.6833905661864118e-18,1.6245471262671712e-19,1.5093740535841823e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.19567246683956696, "-10": 2.3743355098433364e-07, "-11": 2.674066995163575e-08, "-12": 2.7652581442097736e-09, "-13": 2.628443999362333e-10, "-14": 2.1017918169128617e-11, "-2": 0.10223182946899594, "-3": 0.03782276063849014, "-4": 0.010982805417577476, "-5": 0.0026140613575698093, "-6": 0.0005260318322734672, "-7": 9.157669371816739e-05, "-8": 1.4037680916582016e-05, "-9": 1.921266705160603e-06, "0": 0.279983026983866, "1": 0.19760252417898325, "10": 4.5167247420732613e-07, "11": 5.459390288891325e-08, "12": 6.058956876902838e-09, "13": 6.180893097618502e-10, "14": 5.3043542770837155e-11, "2": 0.11049562718442153, "3": 0.04387352259826242, "4": 0.013672656165910908, "5": 0.0034925746919102995, "6": 0.0007542794463213377, "7": 0.00014092742925768994, "8": 2.3184421232180908e-05, "9": 3.405484212433708e-06} |
| Raw goal margin distribution | {"-1": 0.1858529552582684, "-10": 4.263228536603969e-07, "-11": 5.1950741291012416e-08, "-12": 5.815952518985857e-09, "-13": 6.018854922548789e-10, "-14": 5.752651670343591e-11, "-15": 4.607092222605503e-12, "-2": 0.102001633644188, "-3": 0.04017195524971054, "-4": 0.012495083634110723, "-5": 0.0031971390740215696, "-6": 0.0006931881577256483, "-7": 0.00013021479341566167, "-8": 2.1560160970693074e-05, "-9": 3.189668240534321e-06, "0": 0.2658501583994483, "1": 0.19999079824454571, "10": 8.642548732248917e-07, "11": 1.1302780508339827e-07, "12": 1.3580154774233972e-08, "13": 1.508301159532008e-09, "14": 1.5471505986336274e-10, "15": 1.3297859499232739e-11, "2": 0.1174864474914177, "3": 0.049658538886247196, "4": 0.01657679079201816, "5": 0.0045521141046688945, "6": 0.0010592368189592247, "7": 0.00021354656118705159, "8": 3.794674922747948e-05, "9": 6.025018914853048e-06} |
| Research history json | {"away": [{"away": "Crystal Palace", "away_goals": 0.0, "away_xg": 0.14, "date": "2026-10-31T00:00:00+00:00", "home": "Tottenham", "home_goals": 2.0, "home_xg": 3.47, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 2.0, "away_xg": 0.74, "date": "2026-10-24T00:00:00+00:00", "home": "Chelsea", "home_goals": 0.0, "home_xg": 0.47, "source": "pipeline training history"}, {"away": "Coventry", "away_goals": 1.0, "away_xg": 0.82, "date": "2026-10-19T00:00:00+00:00", "home": "Tottenham", "home_goals": 3.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 1.0, "away_xg": 1.62, "date": "2026-10-10T00:00:00+00:00", "home": "Man United", "home_goals": 1.0, "home_xg": 0.8, "source": "pipeline training history"}, {"away": "Aston Villa", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-19T00:00:00+00:00", "home": "Tottenham", "home_goals": 2.0, "home_xg": 1.56, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": 1.11, "date": "2026-09-12T00:00:00+00:00", "home": "Tottenham", "home_goals": 0.0, "home_xg": 0.69, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 0.0, "away_xg": 1.07, "date": "2026-09-05T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.92, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 2.0, "away_xg": 0.75, "date": "2026-08-29T00:00:00+00:00", "home": "Tottenham", "home_goals": 0.0, "home_xg": 1.04, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 0.0, "away_xg": 0.57, "date": "2026-08-22T00:00:00+00:00", "home": "Brentford", "home_goals": 3.0, "home_xg": 3.88, "source": "pipeline training history"}, {"away": "Everton", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Tottenham", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [{"away": "Leeds", "away_goals": 1.0, "away_xg": null, "date": "2026-05-11T00:00:00+00:00", "home": "Tottenham", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 2.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Leeds", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 4.0, "away_xg": null, "date": "2023-05-28T00:00:00+00:00", "home": "Leeds", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 3.0, "away_xg": null, "date": "2022-11-12T00:00:00+00:00", "home": "Tottenham", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Leeds", "away_goals": 0.0, "away_xg": 0.71, "date": "2026-10-31T00:00:00+00:00", "home": "Bournemouth", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 0.0, "away_xg": 0.76, "date": "2026-10-25T00:00:00+00:00", "home": "Sunderland", "home_goals": 0.0, "home_xg": 0.83, "source": "pipeline training history"}, {"away": "Man United", "away_goals": 1.0, "away_xg": 0.92, "date": "2026-10-18T00:00:00+00:00", "home": "Leeds", "home_goals": 1.0, "home_xg": 1.41, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 1.0, "away_xg": 0.62, "date": "2026-10-10T00:00:00+00:00", "home": "Arsenal", "home_goals": 2.0, "home_xg": 2.33, "source": "pipeline training history"}, {"away": "Crystal Palace", "away_goals": 0.0, "away_xg": 1.06, "date": "2026-09-20T00:00:00+00:00", "home": "Leeds", "home_goals": 0.0, "home_xg": 1.31, "source": "pipeline training history"}, {"away": "Newcastle", "away_goals": 1.0, "away_xg": 0.85, "date": "2026-09-14T00:00:00+00:00", "home": "Leeds", "home_goals": 4.0, "home_xg": 1.91, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 1.0, "away_xg": 2.5, "date": "2026-09-05T00:00:00+00:00", "home": "Brighton", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Brentford", "away_goals": 1.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Leeds", "home_goals": 1.0, "home_xg": 1.43, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 1.0, "away_xg": 0.47, "date": "2026-08-22T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.66, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 0.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "West Ham", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 26.6% |
| Unadjusted away-win probability | 34.5% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.8% |
| P home draw | 65.0% |
| P draw away | 63.0% |
| P home away | 72.0% |
| Raw p home draw | 65.5% |
| Raw p draw away | 61.0% |
| Raw p home away | 73.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9222 |
| Totals anchor target over 2 5 | 0.4813 |
| Totals anchor reference over odds | 2.02 |
| Totals anchor reference under odds | 1.88 |
| Totals anchor reference last update utc | 2026-11-05T12:26:15Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5303 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.94, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.76, "draw": 3.57, "home": 2.68}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.02, "under": 1.92}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.76, "draw": 3.38, "home": 2.69}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.02, "under": 1.88}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.69 |
| Reference draw odds | 3.38 |
| Reference away odds | 2.76 |
| Market reference 1x2 last update utc | 2026-11-05T12:26:15Z |
| Market reference home last update utc | 2026-11-05T12:26:15Z |
| Market reference draw last update utc | 2026-11-05T12:26:15Z |
| Market reference away last update utc | 2026-11-05T12:26:15Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-11-05T12:26:15Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:26:15Z |
| Market best over 2 5 last update utc | 2026-11-05T12:19:13Z |
| Market best under 2 5 last update utc | 2026-11-05T12:19:13Z |
| Home probability edge | +0.8% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0279 |
| Raw ev home | 0.0480 |
| Raw edge prob draw | -0.0202 |
| Raw ev draw | -0.0509 |
| Raw edge prob away | -0.0077 |
| Raw ev away | -0.0490 |
| Count model | {"corners": {"alpha": 0.009288361750668784, "mu": 9.499534919178165, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,475.4318 |
| Elo away rating | 1,472.6402 |
| Elo rating diff | 62.7916 |
| Elo home expectancy | 0.5894 |

</details>


---

## 2026-11-07 — Nottingham Forest vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **56.6%**. Expected goals are 0.94 for Nottingham Forest and 1.84 for Manchester City (2.78 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 52.7%; Under 3.5 goals: 69.7%; Double Chance 1X: 43.4%; Double Chance X2: 79.9%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 51.9%; BTTS No (at least one team does not score): 48.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 20.1% | 4.98 |
| Draw | 23.4% | 4.28 |
| Manchester City win | 56.6% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.94 |
| Manchester City expected goals | 1.84 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.13% |
| 2 | 0-1 | 10.51% |
| 3 | 0-2 | 10.26% |
| 4 | 1-2 | 9.66% |
| 5 | 0-0 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 20.1% | 20.8% | 4.58 | -8.1% |
| Draw | 23.4% | 23.1% | 4.26 | -0.5% |
| Manchester City win | 56.6% | 56.1% | 1.78 | +0.7% |
| Over 2.5 | 52.7% | 58.1% | 1.70 | -10.4% |
| Under 2.5 | 47.3% | 41.9% | 2.34 | +10.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T17:30:00+00:00 |
| Fixture id | 59c5f635cfe11613c07e9a5520ced5c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:19:13Z |
| Market best draw last update utc | 2026-11-05T12:19:13Z |
| Market best away last update utc | 2026-11-05T12:19:13Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9416 |
| Dc lambda away | 1.8396 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:25:21.757952+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.9% |
| P btts no | 48.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.93 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.37 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.70 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.0669841190288475,0.10514322516467728,0.10260927841874297,0.06292065524544213,0.028937506316626248,0.010646796586059944,0.0032643413333733207,0.000857877706323812,0.00019727100304980073,4.032260683146886e-05,7.417822877634395e-06,1.240542455139218e-06,1.9017711005287444e-07,2.6911800153899966e-08,3.5362468307219887e-09,4.3368976203228546e-10,4.9863992115587964e-11],[0.05680593574135515,0.11133546533388805,0.0966135604963497,0.059244043284443146,0.027246615123103616,0.010024677513683203,0.003073597668288347,0.0008077497567047086,0.00018574396273939804,3.796645561217625e-05,6.984380851163158e-06,1.1680544428815536e-06,1.7906458373220698e-07,2.5339276060629177e-08,3.329615044321147e-09,4.08348179681771e-10,4.695031378340611e-11],[0.030126356471627046,0.055421014119702315,0.045438083911531695,0.027891132498522587,0.01282726347501478,0.00471945521082485,0.0014469998173789582,0.0003802754545589278,8.744523817680696e-05,1.7873990113982437e-05,3.288132965615609e-06,5.499010436455494e-07,8.430069512117904e-08,1.1929319250383311e-08,1.5675286361594612e-09,1.9224368482671556e-10,2.2103444498091014e-11],[0.009455332592269985,0.01739420834365421,0.015999357026837965,0.00874493954640664,0.004025911414782886,0.0014812285287368703,0.0004541493275882047,0.00011935166812879189,2.7445197740744913e-05,5.609855988984856e-06,1.0319996985624038e-06,1.7258964805126437e-07,2.6458264572451656e-08,3.744086385553256e-09,4.919779999534275e-10,6.033680111672501e-11,6.937294901926232e-12],[0.002225708438588721,0.004094455262704532,0.0037661186001790325,0.0023094076257730205,0.0009467082040321327,0.0003486691561313481,0.00010690306035546787,2.8094412578470573e-05,6.4603764716061765e-06,1.3205145024891738e-06,2.4292434087291306e-07,4.0626200330044204e-08,6.228060425654584e-09,8.813275029525352e-10,1.1580762235603851e-10,1.4202792560965229e-11,1.6329828330754551e-12],[0.0004191309405788568,0.0007710411910481657,0.0007092109657567994,0.00043489262725893477,0.00020000917185730084,6.55926902694275e-05,2.0131289193456265e-05,5.290557094033074e-06,1.2165760888046688e-06,2.486707045183565e-07,4.574593226780555e-08,7.650461875982924e-09,1.1728278416564512e-09,1.6596586456073973e-10,2.1808138407861193e-11,2.674577542015485e-12,3.075127087220947e-13],[6.577334445697742e-05,0.00012099788619587158,0.00011129499788052804,6.824679307854649e-05,3.1387022244066374e-05,1.154803173494991e-05,3.155965556388387e-06,8.302360919347903e-07,1.909147485904036e-07,3.90233750866881e-08,7.178813753049172e-09,1.200571028063544e-09,1.8404942739723507e-10,2.6044677023312712e-11,3.422305682049311e-12,4.1971587615298733e-13,4.8257328098332284e-14],[8.847148956937492e-06,1.6275382246217625e-05,1.4970250221275168e-05,9.179851643307152e-06,4.22185709728659e-06,1.5533216040940578e-06,4.7625329133318646e-07,1.1156179324223617e-07,2.5679874313832214e-08,5.249020177470215e-09,9.656196614554236e-10,1.6148837810139648e-10,2.475642242409425e-11,3.50326015900399e-12,4.603331090312509e-13,5.6455831865838646e-14,6.49107588301236e-15],[1.0412734770961574e-06,1.9155463466339634e-06,1.7619376114022909e-06,1.080431231166039e-06,4.968954225697183e-07,1.8281964004633269e-07,5.605307687920508e-08,1.4730899778741184e-08,3.019359492380943e-09,6.177883426791857e-10,1.1364950983985193e-10,1.9006525807887796e-11,2.9137303083140607e-12,4.123194833379694e-13,5.417933612246762e-14,6.644621972053588e-15,7.639732514618996e-16],[1.089365835385831e-07,2.004017956877704e-07,1.8433146336307998e-07,1.130332133301273e-07,5.198450829810867e-08,1.912633657580608e-08,5.864194975055779e-09,1.5411262551510699e-09,3.5438561923100067e-10,6.456677834183092e-11,1.1889853717694141e-11,1.988436306111734e-12,3.0483041402892124e-13,4.3136291117769687e-14,5.668166822062568e-15,6.951511130001409e-16,7.992581945063479e-17],[1.0257114528200455e-08,1.8869181529806813e-08,1.735605128644637e-08,1.0642839870290189e-08,4.894692287802794e-09,1.800873667875485e-09,5.521535330097896e-10,1.4510743763046785e-10,3.336779771794641e-11,6.820447847943844e-12,1.1183775199773019e-12,1.8722469772146112e-13,2.8701840711444775e-14,4.061572925683423e-15,5.336961594563879e-16,6.545316870455254e-17,7.525555302320212e-18],[8.779786870417496e-10,1.6151461680128814e-09,1.4856266914840527e-09,9.109956362505728e-10,4.189711927758335e-10,1.5414946319477013e-10,4.726271044596104e-11,1.2420767772507507e-11,2.8561848606965993e-12,5.838101768397681e-13,1.0739882230476468e-13,1.6009669641467864e-14,2.456792731935774e-15,3.476586377983515e-16,4.5682813823562915e-17,5.602597783611499e-18,6.441652908744873e-19],[6.88896822183153e-11,1.267307599748673e-10,1.1656814929781646e-10,7.148032271151206e-11,3.287413778369224e-11,1.2095176899330173e-11,3.7084192947427224e-12,9.74582592247875e-13,2.2410756697650392e-13,4.580805679215493e-14,8.426936608365221e-15,1.4093046978735365e-15,1.925746822934466e-16,2.727867251433853e-17,3.584454353610136e-18,4.396019933131709e-19,5.0543757883159066e-20],[4.989560385796722e-12,9.178889483458764e-12,8.442829190862343e-12,5.17719599046872e-12,2.3810168710449507e-12,8.760327174227646e-13,2.685943875939831e-13,7.058732945750545e-14,1.6231722985738502e-14,3.317798226970138e-15,6.103484254938337e-16,1.0207349875330837e-16,1.5648027945735544e-17,1.973748428328368e-18,2.596158215796616e-19,3.1839611110435946e-20,3.660796856108339e-21],[3.3557198837328673e-13,6.173245650640769e-13,5.67820962171061e-13,3.481913872944108e-13,1.6013486239014878e-13,5.891742320674809e-14,1.8064267338539483e-14,4.747338175812671e-15,1.0916616166333663e-15,2.2313792437807236e-16,4.104887382994686e-17,6.864934841628628e-18,1.0524053114616748e-18,1.4892497533002326e-19,1.7442753266716753e-20,2.1413673316341888e-21,2.4620623562987393e-22],[2.106424493587234e-14,3.8750182655221044e-14,3.5642783787986946e-14,2.185637931844288e-14,1.0051852005019211e-14,3.698315343403631e-15,1.1339151210165934e-15,2.97995951966937e-16,6.852487238677435e-17,1.400662765794798e-17,2.576685667022595e-18,4.3091996347446225e-19,6.606070834429168e-20,9.348194325239087e-21,1.2283653403545882e-21,1.342801541872348e-22,1.545465244935089e-23],[1.2395880115470198e-15,2.2803695081833718e-15,2.097505399137696e-15,1.2862035103298141e-15,5.915310649491682e-16,2.1763834291521856e-16,6.672860073566399e-17,1.7536456240056483e-17,4.0325494961738655e-18,8.242615759479247e-19,1.5163271563211005e-19,2.535876421326382e-20,3.887538449499941e-21,5.5012224033931925e-22,7.228680421914034e-23,8.865344649449346e-24,9.0855490576255e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2340434865654914, "-10": 8.674040632479908e-06, "-11": 1.4320428464270315e-06, "-12": 2.1714588453361287e-07, "-13": 3.044059617794975e-08, "-14": 3.966698454901851e-09, "-15": 4.806400758156916e-10, "-16": 4.9863992115587964e-11, "-2": 0.17627420360382304, "-3": 0.09537022590393628, "-4": 0.04053525170625287, "-5": 0.014129482392828224, "-6": 0.0041653969466541405, "-7": 0.0010625694844156614, "-8": 0.00023870457878145956, "-9": 4.788425055269834e-05, "0": 0.23351817932738592, "1": 0.1307477630627667, "10": 1.1994169941407956e-08, "11": 1.0135107370851215e-09, "12": 7.865884057432851e-11, "13": 5.643813938159116e-12, "14": 3.7641967642764547e-13, "15": 2.334461444405571e-14, "16": 1.2395880115470198e-15, "2": 0.05175457401473066, "3": 0.014331656302752219, "4": 0.0031177410657216354, "5": 0.000556233341862886, "6": 8.39287501497909e-05, "7": 1.0958100946585576e-05, "8": 1.2599760882434215e-06, "9": 1.293653131683313e-07} |
| Raw goal margin distribution | {"-1": 0.2391562601947868, "-10": 8.863528521487107e-06, "-11": 1.4633263955173175e-06, "-12": 2.2188952328402436e-07, "-13": 3.1105583183922686e-08, "-14": 4.0533525701400205e-09, "-15": 4.911398506262389e-10, "-16": 5.0953290979150366e-11, "-2": 0.18012498412728994, "-3": 0.09745362665640774, "-4": 0.04142076050216882, "-5": 0.014438146590382945, "-6": 0.004256391709964682, "-7": 0.001085781740047882, "-8": 0.00024391917583560312, "-9": 4.89303011695178e-05, "0": 0.23886109930338312, "1": 0.11920834998002075, "10": 1.0935599773196987e-08, "11": 9.240612598240146e-10, "12": 7.171664261441929e-11, "13": 5.14570751653481e-12, "14": 3.431979827097426e-13, "15": 2.1284287421878846e-14, "16": 1.1301856188590937e-15, "2": 0.047186867504977, "3": 0.013066786462049814, "4": 0.002842578407488381, "5": 0.0005071418228051505, "6": 7.652144546778205e-05, "7": 9.990971181127357e-06, "8": 1.1487743038607438e-06, "9": 1.179479110479483e-07} |
| Research history json | {"away": [{"away": "Brighton", "away_goals": 1.0, "away_xg": 1.0, "date": "2026-10-31T00:00:00+00:00", "home": "Man City", "home_goals": 0.0, "home_xg": 1.64, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 1.0, "away_xg": 1.56, "date": "2026-10-24T00:00:00+00:00", "home": "Aston Villa", "home_goals": 2.0, "home_xg": 0.61, "source": "pipeline training history"}, {"away": "Ipswich", "away_goals": 2.0, "away_xg": 1.66, "date": "2026-10-17T00:00:00+00:00", "home": "Man City", "home_goals": 3.0, "home_xg": 3.53, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 3.0, "away_xg": 1.29, "date": "2026-10-11T00:00:00+00:00", "home": "Liverpool", "home_goals": 0.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Sunderland", "away_goals": 3.0, "away_xg": 3.57, "date": "2026-09-20T00:00:00+00:00", "home": "Man City", "home_goals": 5.0, "home_xg": 2.82, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 1.0, "away_xg": 1.1, "date": "2026-09-13T00:00:00+00:00", "home": "Man United", "home_goals": 0.0, "home_xg": 1.0, "source": "pipeline training history"}, {"away": "Coventry", "away_goals": 0.0, "away_xg": 1.37, "date": "2026-09-05T00:00:00+00:00", "home": "Man City", "home_goals": 1.0, "home_xg": 2.12, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 4.0, "away_xg": 2.21, "date": "2026-08-28T00:00:00+00:00", "home": "Crystal Palace", "home_goals": 1.0, "home_xg": 0.66, "source": "pipeline training history"}, {"away": "Bournemouth", "away_goals": 1.0, "away_xg": 0.63, "date": "2026-08-23T00:00:00+00:00", "home": "Man City", "home_goals": 2.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Aston Villa", "away_goals": 2.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Man City", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [{"away": "Nott'm Forest", "away_goals": 2.0, "away_xg": null, "date": "2026-03-04T00:00:00+00:00", "home": "Man City", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 2.0, "away_xg": null, "date": "2025-12-27T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 0.0, "away_xg": null, "date": "2025-03-08T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 0.0, "away_xg": null, "date": "2024-12-04T00:00:00+00:00", "home": "Man City", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 2.0, "away_xg": null, "date": "2024-04-28T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 0.0, "away_xg": null, "date": "2023-09-23T00:00:00+00:00", "home": "Man City", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Man City", "away_goals": 1.0, "away_xg": null, "date": "2023-02-18T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Nott'm Forest", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-10-31T00:00:00+00:00", "home": "Brentford", "home_goals": 2.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 1.0, "away_xg": 2.31, "date": "2026-10-23T00:00:00+00:00", "home": "Ipswich", "home_goals": 1.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Arsenal", "away_goals": 1.0, "away_xg": 1.14, "date": "2026-10-18T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.9, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 1.0, "away_xg": 3.34, "date": "2026-10-11T00:00:00+00:00", "home": "Crystal Palace", "home_goals": 3.0, "home_xg": 2.41, "source": "pipeline training history"}, {"away": "Coventry", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-09-19T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 1.1, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 2.0, "away_xg": 2.28, "date": "2026-09-12T00:00:00+00:00", "home": "Aston Villa", "home_goals": 1.0, "home_xg": 0.82, "source": "pipeline training history"}, {"away": "Tottenham", "away_goals": 0.0, "away_xg": 1.07, "date": "2026-09-05T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.92, "source": "pipeline training history"}, {"away": "Nott'm Forest", "away_goals": 2.0, "away_xg": 2.3, "date": "2026-08-29T00:00:00+00:00", "home": "Liverpool", "home_goals": 2.0, "home_xg": 1.75, "source": "pipeline training history"}, {"away": "Leeds", "away_goals": 1.0, "away_xg": 0.47, "date": "2026-08-22T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 0.0, "home_xg": 0.66, "source": "pipeline training history"}, {"away": "Bournemouth", "away_goals": 1.0, "away_xg": null, "date": "2026-05-24T00:00:00+00:00", "home": "Nott'm Forest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 18.3% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 57.8% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 52.0% |
| P home draw | 43.4% |
| P draw away | 79.9% |
| P home away | 76.6% |
| Raw p home draw | 42.2% |
| Raw p draw away | 81.7% |
| Raw p home away | 76.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5270 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.08, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.78, "draw": 4.26, "home": 4.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:19:13Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.7, "under": 2.34}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:26:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.75, "draw": 4.12, "home": 4.56}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.56 |
| Reference draw odds | 4.12 |
| Reference away odds | 1.75 |
| Market reference 1x2 last update utc | 2026-11-05T12:26:15Z |
| Market reference home last update utc | 2026-11-05T12:26:15Z |
| Market reference draw last update utc | 2026-11-05T12:26:15Z |
| Market reference away last update utc | 2026-11-05T12:26:15Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-05T12:26:15Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:26:15Z |
| Market best over 2 5 last update utc | 2026-11-05T12:19:13Z |
| Market best under 2 5 last update utc | 2026-11-05T12:19:13Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.2% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | -0.0253 |
| Raw ev home | -0.1623 |
| Raw edge prob draw | 0.0076 |
| Raw ev draw | 0.0175 |
| Raw edge prob away | 0.0177 |
| Raw ev away | 0.0293 |
| Count model | {"corners": {"alpha": 0.009288361750668784, "mu": 9.725962605950652, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,415.6922 |
| Elo away rating | 1,636.6871 |
| Elo rating diff | -160.9950 |
| Elo home expectancy | 0.2836 |

</details>


---
