# Ligue 1 — football model report

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

## 2026-11-27 — Stade Brestois 29 vs Paris FC

Research leans **Stade Brestois 29 win** at **38.7%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote). Only one view is available.

**Fixture source:** football-data.org

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| Stade Brestois 29 win | 38.7% | — |
| Draw | 26.7% | — |
| Paris FC win | 34.6% | — |
| Stade Brestois 29 expected goals | 1.45 | — |
| Paris FC expected goals | 1.36 | — |
| Expected total goals | 2.80 | — |
| Most likely score | 1-1 | — |
| Most likely score probability | 12.6% | — |
| Over 1.5 | 77.3% | — |
| Under 1.5 | 22.7% | — |
| Over 2.5 | 53.0% | — |
| Under 2.5 | 47.0% | — |
| Over 3.5 | 31.0% | — |
| Under 3.5 | 69.0% | — |
| BTTS Yes | 57.4% | — |
| BTTS No | 42.6% | — |
| Double Chance 1X | 65.4% | — |
| Double Chance X2 | 61.3% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 1-1 (12.57%) | — |
| 2 | 2-1 (8.52%) | — |
| 3 | 1-0 (8.43%) | — |
| 4 | 1-2 (7.93%) | — |
| 5 | 0-1 (7.84%) | — |

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
| League | Ligue 1 |
| Training matches | 1,779 |
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
| Training sha256 | b012bf647b3154853737559e0d2adb26161c4f5a61849359a75b0ca6c5ab885e |
| Training as of utc | 2026-11-24T15:48:21.263251+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 99, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 99, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 361, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-24T15:48:21.263251+00:00', 'observations': 1098, 'observations_sha256': '9dc5b59457cb166942eab82dd775b1f2ea483d9ab552a10718155387f4c80092', 'eligible_training_matches': 415, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 360, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 41, 'retrospective_eligible_training_matches': 415, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'a4dbb89e42d6bf57ff095f91c0c405c7535d75f7f653eeae0ddb96bfcd786b53', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 354, 'tuning_matches': 20, 'audit_matches': 41, 'tuning_origin_utc': '2025-10-05T00:00:00+00:00', 'audit_origin_utc': '2026-10-17T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_red_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_red_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 39, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1777, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1489, 'tuning_matches': 189, 'audit_matches': 95, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8570386247465478, 'audit_candidate_poisson_score': 0.8512583220862963, 'audit_gain': 0.005780302660251535, 'audit_gain_lower95': -0.001751997875908252, 'audit_baseline_briers': [0.5856033518783379, 0.1628934403909076, 0.22821994719896568, 0.24145086484005113], 'audit_candidate_briers': [0.5842469461303595, 0.1621985137454303, 0.22431109193006557, 0.240208566981081], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1602.639 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.196 |
| Dixon-Coles low-score adjustment | -0.048 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1779, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-22'} |
| Training data health | {'training_end': '2026-11-22', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261124T154821263251Z_cf7bf789ad537e2c7826a6c5b8c2a45868e50966e03d9212390656078202d5e0.json |
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

### 2026-11-27 — Stade Brestois 29 vs Paris FC

The model's most likely 1X2 outcome is **Paris FC win** at **38.4%**. Expected goals are 1.39 for Stade Brestois 29 and 1.45 for Paris FC (2.84 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.1%; Under 3.5 goals: 68.2%; Double Chance 1X: 61.6%; Double Chance X2: 64.6%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 84.1%; BTTS Yes (both teams score): 58.1%; BTTS No (at least one team does not score): 41.9%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| Stade Brestois 29 win | 35.4% | 2.83 |
| Draw | 26.2% | 3.82 |
| Paris FC win | 38.4% | 2.60 |

| Measure | Benchmark estimate |
| --- | --- |
| Stade Brestois 29 expected goals | 1.39 |
| Paris FC expected goals | 1.45 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 31.8% |
| Under 3.5 | 68.2% |
| Over 4.5 | 15.9% |
| Under 4.5 | 84.1% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 1-1 | 12.33% |
| 2 | 1-2 | 8.56% |
| 3 | 2-1 | 8.16% |
| 4 | 0-1 | 7.92% |
| 5 | 1-0 | 7.52% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T19:45:00+00:00 |
| Fixture id | fdorg:559616 |
| Matched home-team name | Brest |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3877 |
| Dc lambda away | 1.4550 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-24T15:48:21.263251+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.65 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.58 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.29 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.06389970315839989,0.07915310001049426,0.06167916871332388,0.029914281560339304,0.010881277989864678,0.003166439694134393,0.0007678586671168049,0.0001596042936781924,2.9027919062427825e-05,4.692828832698083e-06,6.828039641793193e-07,9.031599452930046e-08,1.0950772141194293e-08,1.2256393900958408e-09,1.2737846008493355e-10,1.2355663019433664e-11],[0.07523019011742227,0.1232801146907523,0.08559042752305263,0.04151119739785534,0.015099639871581388,0.0043939782717658735,0.0010655356251844492,0.0002214783372636535,4.028121737835718e-05,6.5121050504101615e-06,9.475076339010156e-07,1.2532893593072438e-07,1.5196074928128583e-08,1.700784909650305e-09,1.7675946487817102e-10,1.7145602027798608e-11],[0.05610340754093434,0.08163014343502796,0.05938570052417411,0.028801953774619856,0.010476670316842341,0.0030486993149617795,0.0007393067351836674,0.0001536695935510881,2.7948549635833867e-05,4.518331447771543e-06,6.574146925023758e-07,8.695769926129649e-08,1.054358040893881e-08,1.180065414129681e-09,1.2264204011881022e-10,1.1896232052997766e-11],[0.02595103412870369,0.03775860916590075,0.027469282323633947,0.013322550592549236,0.004846059105218917,0.0014101977658487709,0.00034197164053419523,7.108097425060428e-05,1.2927802378458079e-05,2.089986664720182e-06,3.040918879908069e-07,4.022290837926304e-08,4.877008848909321e-09,5.458477332921052e-10,5.6728956550721606e-11,5.502687582480171e-12],[0.00900287792489843,0.013099136907170947,0.00952958538059616,0.004621831100762972,0.0016811845849669714,0.000489222829153405,0.000118636078941506,2.465926139156155e-05,4.4848858844409925e-06,7.250537575429297e-07,1.0549491522979533e-07,1.3954046383159223e-08,1.691921604650646e-09,1.8936434224699677e-10,1.9680289737206147e-11,1.9089807488299145e-12],[0.002498607509162017,0.003635459917687144,0.0026447868992322005,0.0012827167035673428,0.0004665864030732479,0.00013577612012216362,3.292558226086677e-05,6.843791085175669e-06,1.2447097075044952e-06,2.0122729401146908e-07,2.9278458462997642e-08,3.872726628862968e-09,4.695662944181538e-10,5.255510198548098e-11,5.461955624642354e-12,5.298076541369929e-13],[0.0005778744249820211,0.0008408040485651237,0.000611682588397555,0.00029666491226443633,0.00010791144603211831,3.14021097968282e-05,7.614982283703229e-06,1.58282236147179e-06,2.87874707754694e-07,4.653956509422527e-08,6.7714806293602846e-09,8.956787592931357e-10,1.0860063110465656e-10,1.2154869953911593e-11,1.2632334027228162e-12,1.2253316791966614e-13],[0.00011455712826002865,0.0001666799793675295,0.00012125921775421215,5.88104940023683e-05,2.1392234764864613e-05,6.2251163299754475e-06,1.5095848932909212e-06,3.137767937759257e-07,5.7067934473997127e-08,9.225947190569976e-09,1.3423701438111923e-09,1.7755827576435728e-10,2.1528857981495313e-11,2.4095667433933258e-12,2.5042186447786197e-13,2.4290827257007515e-14],[1.987095843728306e-05,2.8912133122099522e-05,2.103349580012249e-05,1.0201206155801493e-05,3.710674441212815e-06,1.0798021017026082e-06,2.618510006993674e-07,5.4427391140188834e-08,9.898943621041036e-09,1.6003230523748341e-09,2.3284610691859554e-10,3.07990709220691e-11,3.7343729600258415e-12,4.179609015786994e-13,4.343791203923536e-14,4.213461232509236e-15],[3.0638181837097837e-06,4.457838280368226e-06,3.2430648527998154e-06,1.572880392989751e-06,5.721330384086602e-07,1.6649007265785592e-07,4.037368705175642e-08,8.391926901438161e-09,1.526275824157493e-09,2.4674697414073793e-10,3.5901546401743045e-11,4.748777157892574e-12,5.757870117736344e-13,6.444360569613489e-14,6.697506070894492e-15,6.496555856257483e-16],[4.251573321544709e-07,6.186015346911192e-07,4.5003088243010044e-07,2.1826413696386043e-07,7.939327390267184e-08,2.3103353683902222e-08,5.6025416806489625e-09,1.1645238193379518e-09,2.1179695354668374e-10,3.4240375555131655e-11,4.981955446815398e-12,6.589742949436528e-13,7.990032539021632e-14,8.94265580701269e-15,9.29393861662517e-16,9.015085721224275e-17],[5.363443029289255e-08,7.803779538115225e-08,5.6772277385013975e-08,2.7534448436075078e-08,1.0015617026475876e-08,2.914533324433143e-09,7.067716078447311e-10,1.4690696099767961e-10,2.6718600579418828e-11,4.319490449824666e-12,6.284834387789281e-13,8.313089817329566e-14,1.0079582564893852e-14,1.1281335478422118e-15,1.172448562403472e-16,1.1372707234031167e-17],[6.202247742211107e-09,9.02423569275841e-09,6.565106169833723e-09,3.184064223542342e-09,1.1581988985448953e-09,3.3703458081589705e-10,8.17305709238566e-11,1.698821749736561e-11,3.089720152032655e-12,4.99502833229081e-13,7.267738219455331e-14,9.61319851236734e-15,1.1655958283540816e-15,1.3045656888321936e-16,1.3558112595425906e-17,1.3151318542940682e-18],[6.620525173106982e-10,9.632827009689613e-10,7.007854646904028e-10,3.3987964075160135e-10,1.2363074294977536e-10,3.5976407574195495e-11,8.72424522050607e-12,1.8133896977715621e-12,3.2980898046319725e-13,5.331891305993609e-14,7.757871957611007e-15,1.0261509277040467e-15,1.2442032056809806e-16,1.3925451452228063e-17,1.4472466994012056e-18,1.4038238892090333e-19],[6.562224582165578e-11,9.54799997672515e-11,6.946143218208679e-11,3.368866479924678e-11,1.2254204602860438e-11,3.5659597990864507e-12,8.647419192574133e-13,1.797420920639412e-13,3.2690467031316694e-14,5.284938472819972e-15,7.689555848578799e-16,1.0171146044644299e-16,1.2332467059704978e-17,1.3802823408747682e-18,1.4345021911323112e-19,1.3914617638219114e-20],[6.07080822917022e-12,8.8329919381838e-12,6.42597687447329e-12,3.11658677529644e-12,1.1336540713215055e-12,3.2989206361541706e-13,7.99985171766847e-14,1.662819914142513e-14,3.0242420658459516e-15,4.889172500839021e-16,7.113718578161014e-17,9.409473317285004e-18,1.1408942436304227e-18,1.2769190216887713e-19,1.3270785840454813e-20,1.2872612664527406e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.19891533035198963, "-10": 8.19242538349666e-07, "-11": 1.0675077280885828e-07, "-12": 1.2779701778545888e-08, "-13": 1.4142950870270097e-09, "-14": 1.4452406211273217e-10, "-15": 1.2355663019433664e-11, "-2": 0.11520301140222786, "-3": 0.048430544271834894, "-4": 0.016090337037081938, "-5": 0.00439932796509676, "-6": 0.0010194850193771564, "-7": 0.0002047223704144948, "-8": 3.62394074779505e-05, "-9": 5.732366123540343e-06, "0": 0.261712968580799, "1": 0.18945100106315607, "10": 5.101126974428749e-07, "11": 6.339427376921192e-08, "12": 7.238108462137451e-09, "13": 7.639584939524229e-10, "14": 7.445523775983958e-11, "15": 6.07080822917022e-12, "2": 0.10478872581247844, "3": 0.04201413644967468, "4": 0.013312713842091824, "5": 0.0034714679421242378, "6": 0.0007672431719270298, "7": 0.00014694095193051068, "8": 2.4807557105193698e-05, "9": 3.742503336710725e-06} |
| Raw goal margin distribution | {"-1": 0.19891533035198963, "-10": 8.19242538349666e-07, "-11": 1.0675077280885828e-07, "-12": 1.2779701778545888e-08, "-13": 1.4142950870270097e-09, "-14": 1.4452406211273217e-10, "-15": 1.2355663019433664e-11, "-2": 0.11520301140222786, "-3": 0.048430544271834894, "-4": 0.016090337037081938, "-5": 0.00439932796509676, "-6": 0.0010194850193771564, "-7": 0.0002047223704144948, "-8": 3.62394074779505e-05, "-9": 5.732366123540343e-06, "0": 0.261712968580799, "1": 0.18945100106315607, "10": 5.101126974428749e-07, "11": 6.339427376921192e-08, "12": 7.238108462137451e-09, "13": 7.639584939524229e-10, "14": 7.445523775983958e-11, "15": 6.07080822917022e-12, "2": 0.10478872581247844, "3": 0.04201413644967468, "4": 0.013312713842091824, "5": 0.0034714679421242378, "6": 0.0007672431719270298, "7": 0.00014694095193051068, "8": 2.4807557105193698e-05, "9": 3.742503336710725e-06} |
| Research history json | {"away": [{"away": "Angers", "away_goals": 0.0, "away_xg": 0.46, "date": "2026-11-22T00:00:00+00:00", "home": "Paris FC", "home_goals": 4.0, "home_xg": 3.51, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-11-07T00:00:00+00:00", "home": "Auxerre", "home_goals": 0.0, "home_xg": 0.81, "source": "pipeline training history"}, {"away": "Monaco", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-11-01T00:00:00+00:00", "home": "Paris FC", "home_goals": 3.0, "home_xg": 2.15, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 1.0, "away_xg": 0.42, "date": "2026-10-24T00:00:00+00:00", "home": "Lens", "home_goals": 2.0, "home_xg": 1.06, "source": "pipeline training history"}, {"away": "Rennes", "away_goals": 3.0, "away_xg": 3.35, "date": "2026-10-18T00:00:00+00:00", "home": "Paris FC", "home_goals": 4.0, "home_xg": 3.62, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 0.0, "away_xg": 0.97, "date": "2026-10-10T00:00:00+00:00", "home": "Lorient", "home_goals": 1.0, "home_xg": 0.55, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 1.0, "away_xg": 0.24, "date": "2026-09-19T00:00:00+00:00", "home": "Paris FC", "home_goals": 2.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Lyon", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-09-12T00:00:00+00:00", "home": "Paris FC", "home_goals": 0.0, "home_xg": 0.3, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 3.0, "away_xg": 3.29, "date": "2026-09-06T00:00:00+00:00", "home": "Marseille", "home_goals": 2.0, "home_xg": 1.42, "source": "pipeline training history"}, {"away": "Nice", "away_goals": 0.0, "away_xg": 0.65, "date": "2026-08-30T00:00:00+00:00", "home": "Paris FC", "home_goals": 3.0, "home_xg": 2.88, "source": "pipeline training history"}], "h2h": [{"away": "Brest", "away_goals": 0.0, "away_xg": null, "date": "2026-05-03T00:00:00+00:00", "home": "Paris FC", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 2.0, "away_xg": null, "date": "2025-09-14T00:00:00+00:00", "home": "Brest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Brest", "away_goals": 1.0, "away_xg": 1.41, "date": "2026-11-21T00:00:00+00:00", "home": "Strasbourg", "home_goals": 0.0, "home_xg": 1.86, "source": "pipeline training history"}, {"away": "Lyon", "away_goals": 0.0, "away_xg": 0.64, "date": "2026-11-08T00:00:00+00:00", "home": "Brest", "home_goals": 2.0, "home_xg": 1.84, "source": "pipeline training history"}, {"away": "Brest", "away_goals": 2.0, "away_xg": 1.31, "date": "2026-11-02T00:00:00+00:00", "home": "Lorient", "home_goals": 0.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Nice", "away_goals": 2.0, "away_xg": 0.47, "date": "2026-10-23T00:00:00+00:00", "home": "Brest", "home_goals": 1.0, "home_xg": 2.46, "source": "pipeline training history"}, {"away": "Brest", "away_goals": 1.0, "away_xg": 0.78, "date": "2026-10-17T00:00:00+00:00", "home": "Lille", "home_goals": 1.0, "home_xg": 2.17, "source": "pipeline training history"}, {"away": "Angers", "away_goals": 1.0, "away_xg": 1.39, "date": "2026-10-10T00:00:00+00:00", "home": "Brest", "home_goals": 5.0, "home_xg": 3.82, "source": "pipeline training history"}, {"away": "Brest", "away_goals": 1.0, "away_xg": 0.34, "date": "2026-09-20T00:00:00+00:00", "home": "Auxerre", "home_goals": 2.0, "home_xg": 0.96, "source": "pipeline training history"}, {"away": "Paris SG", "away_goals": 1.0, "away_xg": 1.16, "date": "2026-09-13T00:00:00+00:00", "home": "Brest", "home_goals": 0.0, "home_xg": 1.25, "source": "pipeline training history"}, {"away": "Brest", "away_goals": 2.0, "away_xg": 2.37, "date": "2026-09-05T00:00:00+00:00", "home": "Le Havre", "home_goals": 1.0, "home_xg": 2.01, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": 1.12, "date": "2026-08-29T00:00:00+00:00", "home": "Brest", "home_goals": 2.0, "home_xg": 2.73, "source": "pipeline training history"}], "teams": {"away": "Paris FC", "home": "Brest"}} |
| Unadjusted home-win probability | 35.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 58.1% |
| P home draw | 61.6% |
| P draw away | 64.6% |
| P home away | 73.8% |
| Raw p home draw | 61.6% |
| Raw p draw away | 64.6% |
| Raw p home away | 73.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5407 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.015570913305566664, "mu": 8.882982703112878, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-22 |
| Elo home rating | 1,519.1581 |
| Elo away rating | 1,513.5245 |
| Elo rating diff | 65.6336 |
| Elo home expectancy | 0.5933 |
| Research p home | 0.3872 |
| Research p draw | 0.2666 |
| Research p away | 0.3462 |
| Research p over 1 5 | 0.7727 |
| Research v4 p home | 0.3921 |
| Research v4 p draw | 0.2520 |
| Research v4 p away | 0.3559 |
| Research v4 p over 1 5 | 0.7709 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.387671547923496, 1.45499439361983], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "team_news": "dated news leads; absences and tactics require confirmation", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [{"headline": "Paris Saint-Germain drop one of this season's best kits in latest Jordan collab", "published_at_utc": "2026-11-24T13:21:57+00:00", "source": "ESPN league news; unconfirmed context lead", "url": "https://www.espn.com/soccer/story/_/id/50581189/psg-kit-nike-jordan-champions-league"}], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T15:50:03.662888+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 4.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-22", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T15:50:03.401946+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T15:50:03.457988+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T15:50:03.662328+00:00", "reason": null, "status": "available", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Stade+Brestois+29_vs_Paris+FC&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 0.9312494032006584, "goals_for": 2.213236948620373, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 2.2686762445488604, "results": "WWWLWLWDWW", "xg_against": 0.9528064296311309, "xg_for": 1.9202236507517008, "xg_matches": 10}, "venue": {"goals_against": 1.1612768438259973, "goals_for": 1.1708095557758593, "last_match": "2026-11-07T00:00:00+00:00", "matches": 4, "points_per_game": 1.514299067924793, "results": "WLLW", "xg_against": 0.9386567683674618, "xg_for": 1.226017240444295, "xg_matches": 4}}, "home": {"all": {"goals_against": 0.7849059493921307, "goals_for": 1.667360393435035, "last_match": "2026-11-21T00:00:00+00:00", "matches": 10, "points_per_game": 1.9393909626348576, "results": "WWWLDWLLWD", "xg_against": 1.3513413427138565, "xg_for": 1.7558598510679808, "xg_matches": 10}, "venue": {"goals_against": 1.1151840416711334, "goals_for": 2.021622295578943, "last_match": "2026-11-08T00:00:00+00:00", "matches": 5, "points_per_game": 1.5140209424328015, "results": "WLWLD", "xg_against": 0.909037295991237, "xg_for": 2.399795463650609, "xg_matches": 5}}}, "goal_rates": [1.4458938398603458, 1.365852223649449], "h2h": [{"away": "Brest", "away_goals": 0.0, "away_xg": null, "date": "2026-05-03T00:00:00+00:00", "home": "Paris FC", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 2.0, "away_xg": null, "date": "2025-09-14T00:00:00+00:00", "home": "Brest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.1884889846295788, "-10": 4.3741802805215457e-07, "-11": 5.352176300558093e-08, "-12": 6.014137510109119e-09, "-13": 6.201579524448928e-10, "-14": 5.302351320686767e-11, "-2": 0.10110596649748102, "-3": 0.040007432608112126, "-4": 0.012499888195263629, "-5": 0.0032123298967021196, "-6": 0.0006994639409049693, "-7": 0.0001319490282144728, "-8": 2.1938803968554527e-05, "-9": 3.259189248151651e-06, "0": 0.2665790985781339, "1": 0.20260163989859914, "10": 7.845203336670747e-07, "11": 1.0161799694983275e-07, "12": 1.208777219076583e-08, "13": 1.3194955300454478e-09, "14": 1.194281759312912e-10, "2": 0.11498012166255328, "3": 0.04816364587015148, "4": 0.01593006302664902, "5": 0.004333753432311404, "6": 0.0009989461624297733, "7": 0.00019948747891492587, "8": 3.511196110575301e-05, "9": 5.5218475409808755e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T15:50:03.662888+00:00", "p_over_1_5": 0.772670348116624, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.194677864172013, "-10": 4.472455451448862e-07, "-11": 5.4724242114895935e-08, "-12": 6.149257773537286e-09, "-13": 6.340911067435055e-10, "-14": 5.4214798085265593e-11, "-2": 0.10337752493862663, "-3": 0.04090628382726136, "-4": 0.012780724505196288, "-5": 0.0032845016521917407, "-6": 0.0007151788712328373, "-7": 0.00013491354098483453, "-8": 2.243170539732086e-05, "-9": 3.3324137976456153e-06, "0": 0.25196780786521605, "1": 0.2060863684150113, "10": 7.90447367497347e-07, "11": 1.0238571867715988e-07, "12": 1.217909504325635e-08, "13": 1.3294642896936729e-09, "14": 1.2033045316829252e-10, "2": 0.11584879394758797, "3": 0.04852752115318879, "4": 0.016050414301721754, "5": 0.004366494843977948, "6": 0.0010064931786704695, "7": 0.00020099460242148655, "8": 3.537723119805035e-05, "9": 5.563564977453194e-06}, "p_over_1_5": 0.7709142049898907, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
