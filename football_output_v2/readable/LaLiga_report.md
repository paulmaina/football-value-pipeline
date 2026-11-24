# La Liga — football model report

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

## 2026-11-27 — Levante UD vs Real Racing Club de Santander

Research leans **Levante UD win** at **64.2%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote). Only one view is available.

**Fixture source:** football-data.org

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| Levante UD win | 64.2% | — |
| Draw | 18.1% | — |
| Real Racing Club de Santander win | 17.8% | — |
| Levante UD expected goals | 2.83 | — |
| Real Racing Club de Santander expected goals | 1.56 | — |
| Expected total goals | 4.39 | — |
| Most likely score | 2-1 | — |
| Most likely score probability | 7.9% | — |
| Over 1.5 | 93.5% | — |
| Under 1.5 | 6.5% | — |
| Over 2.5 | 81.3% | — |
| Under 2.5 | 18.7% | — |
| Over 3.5 | 64.1% | — |
| Under 3.5 | 35.9% | — |
| BTTS Yes | 75.1% | — |
| BTTS No | 24.9% | — |
| Double Chance 1X | 82.2% | — |
| Double Chance X2 | 35.8% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 2-1 (7.95%) | — |
| 2 | 3-1 (7.38%) | — |
| 3 | 2-2 (6.48%) | — |
| 4 | 3-2 (5.92%) | — |
| 5 | 1-1 (5.90%) | — |

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
| League | La Liga |
| Training matches | 2,029 |
| Training data through | 2026-11-23 |
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
| Training sha256 | 4f6d95381b8cfd91e9023a94d1b173af4893896e324bce797e4744fa47776118 |
| Training as of utc | 2026-11-24T15:45:05.106393+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 129, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 129, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 287, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-24T15:45:05.106393+00:00', 'observations': 1222, 'observations_sha256': '75490ae45f9f75061afffb0ea8fc0037b3ff850230a9cc5b781378654644af46', 'eligible_training_matches': 356, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 327, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 50, 'retrospective_eligible_training_matches': 356, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '1dbad689d7a4cd7380d2dda26e8a5d145c84af2d92b37e29f5b1409df2e19cfd', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 296, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2026-10-09T00:00:00+00:00', 'audit_origin_utc': '2026-10-23T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_red_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_red_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 15, 'selected_ridge': 100.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8952429070490318, 'audit_candidate_poisson_score': 0.8915402222885241, 'audit_gain': 0.003702684760507613, 'audit_gain_lower95': -0.01156682491656295, 'audit_baseline_briers': [0.5455469722916333, 0.19765564273440522, 0.16234436270737604, 0.23199920913785804], 'audit_candidate_briers': [0.5429958888588804, 0.19682851871692997, 0.16600724404619635, 0.2338107027776007], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2029, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1650, 'tuning_matches': 250, 'audit_matches': 115, 'audit_matchdays': 53, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.7949635929533156, 'audit_candidate_poisson_score': 0.7996383655023083, 'audit_gain': -0.004674772548992623, 'audit_gain_lower95': -0.013813793914599394, 'audit_baseline_briers': [0.5433894114865379, 0.19395445083491153, 0.19963971369955807, 0.2540491251783392], 'audit_candidate_briers': [0.5523965859420397, 0.1910833424526641, 0.2002061771832245, 0.24984601360867045], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1846.165 |
| Base scoring parameter | 0.084 |
| Home-advantage parameter | 0.280 |
| Dixon-Coles low-score adjustment | -0.028 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 2029, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-23'} |
| Training data health | {'training_end': '2026-11-23', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261124T154505106393Z_69303b7b339a5545e0e153bf24588ab86c62774f211d03ca345afd031d725b1e.json |
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

### 2026-11-27 — Levante UD vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **Levante UD win** at **62.3%**. Expected goals are 2.79 for Levante UD and 1.60 for Real Racing Club de Santander (4.39 combined). The most likely exact score is 2-1 at 7.7%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 81.4%; Under 3.5 goals: 36.1%; Double Chance 1X: 79.7%; Double Chance X2: 37.7%; Double Chance 12 (either team wins): 82.6%; Under 4.5 goals: 55.3%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| Levante UD win | 62.3% | 1.61 |
| Draw | 17.4% | 5.75 |
| Real Racing Club de Santander win | 20.3% | 4.91 |

| Measure | Benchmark estimate |
| --- | --- |
| Levante UD expected goals | 2.79 |
| Real Racing Club de Santander expected goals | 1.60 |
| Expected total goals | 4.39 |
| Over 0.5 | 98.6% |
| Under 0.5 | 1.4% |
| Over 1.5 | 93.5% |
| Under 1.5 | 6.5% |
| Over 2.5 | 81.4% |
| Under 2.5 | 18.6% |
| Over 3.5 | 63.9% |
| Under 3.5 | 36.1% |
| Over 4.5 | 44.7% |
| Under 4.5 | 55.3% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 2-1 | 7.72% |
| 2 | 3-1 | 7.17% |
| 3 | 2-2 | 6.19% |
| 4 | 3-2 | 5.75% |
| 5 | 1-1 | 5.70% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T20:00:00+00:00 |
| Fixture id | fdorg:564765 |
| Matched home-team name | Levante |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7864 |
| Dc lambda away | 1.6038 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-24T15:45:05.106393+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 75.1% |
| P btts no | 24.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 71.60 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.32 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.37 |
| Fair Over 3.5 odds | 1.57 |
| Fair Under 3.5 odds | 2.77 |
| Fair Over 4.5 odds | 2.24 |
| Fair Under 4.5 odds | 1.81 |
| Score matrix json | [[0.013967339202674364,0.018315877590976238,0.015945295292161182,0.008524255080433822,0.003417760067072422,0.0010962678864819156,0.00029302897593417123,6.713633863389183e-05,1.345899994000938e-05,2.398365714652413e-06,3.8464539075512775e-07,5.6080641506413556e-08,7.495090001720522e-09,9.246526643101915e-10,1.0592432743546302e-10,1.1325296518367604e-11,1.1352061213265896e-12,1.0709542739080958e-13,9.542090883239355e-15,8.054434852913464e-16],[0.032978575036139636,0.05697509832827529,0.04442983156165258,0.02375190991906076,0.009523216805700731,0.0030546312658621677,0.0008164933797017304,0.00018706810770925485,3.750203990370003e-05,6.682785283859518e-06,1.0717725579292215e-06,1.562626097758309e-07,2.0884253330797638e-08,2.576444109412722e-09,2.951466209943793e-10,3.1556707321952845e-11,3.163128423409788e-12,2.9840976368346367e-13,2.6587998711866043e-14,2.2442806939748194e-15],[0.04813118079915697,0.07719188417718241,0.061899447342541734,0.033091057193848396,0.013267704073514047,0.004255698942494121,0.0011375350116340016,0.0002606224708853532,5.224767825274725e-05,9.310427279152819e-06,1.4931888481427657e-06,2.1770438566721e-07,2.909585055581802e-08,3.5894906839854496e-09,4.111969837027032e-10,4.3964666858317624e-11,4.406856708670101e-12,4.1574317984962964e-13,3.7042283717077956e-14,3.1267220638864424e-15],[0.044704100626288865,0.0716955973340683,0.05749202651519245,0.03073487760038476,0.012323004923922068,0.003952680790324191,0.0010565392076751995,0.00024206539233990573,4.8527491478906073e-05,8.647497756138211e-06,1.3868694557893691e-06,2.0220319971501337e-07,2.7024141304206976e-08,3.333908499016558e-09,3.819185615532224e-10,4.0834254605902434e-11,4.093075683559271e-12,3.861410553014457e-13,3.440476529395262e-14,2.9040903516928748e-15],[0.031140778902940883,0.04994299658455837,0.0400488201598845,0.021409848639247456,0.008584178327704476,0.0027534288094592098,0.0007359829055402933,0.00016862222385204988,3.380414462404572e-05,6.023828058610306e-06,9.660902352340642e-07,1.4085430749253304e-07,1.8824957836222637e-08,2.3223933821734696e-09,2.6604363621318734e-10,2.8445052613384076e-11,2.8512275855912722e-12,2.6898501614009154e-13,2.396628439487061e-14,2.0229829990819618e-15],[0.017354078880389322,0.02783214591236796,0.022318336554373278,0.011931243057880224,0.004783775906396595,0.0015344259981364507,0.0004101472682225742,9.396949841350262e-05,1.8838314677940726e-05,3.356948380027621e-06,5.383810790372526e-07,7.849504248068714e-08,1.0490739625621847e-08,1.2942193280119397e-09,1.4826033294990056e-10,1.585180924176798e-11,1.5889271292960527e-12,1.4989950001851454e-13,1.3355889111018676e-14,1.127364432635931e-15],[0.008059208974975595,0.012925208054877423,0.0103646030138072,0.005540851911382254,0.002221578568636686,0.00071258520033532,0.00019047179443539204,4.3639298300289025e-05,8.748485919205896e-06,1.5589619419916718e-06,2.50023389546604e-07,3.645298348656881e-08,4.871884213946075e-09,6.010335723256038e-10,6.885188284426555e-11,7.361557141198821e-12,7.378954463250474e-13,6.961310964529078e-14,6.2024554650339244e-15,5.235464017531272e-16],[0.0032080156445389494,0.005144955265177643,0.004125691332855621,0.00220556876871922,0.0008843124462820515,0.0002836487399496363,7.581842067744554e-05,1.7370879958408458e-05,3.4823863957350986e-06,6.205539916732645e-07,9.952328419038051e-08,1.4510324980794638e-08,1.9392822329400726e-09,2.3924495678181713e-10,2.740689787375015e-11,2.93031121918572e-12,2.937236325792099e-13,2.7709908689614823e-14,2.4689239636505623e-15,2.0840073171960297e-16],[0.0011173483472902614,0.0017919823028963947,0.0014369737878440118,0.0007681971946610051,0.0003080050597706683,9.879454650827944e-05,2.6407473162518426e-05,6.050258528366588e-06,1.21291138044307e-06,2.1613827793540808e-07,3.4663851249080316e-08,5.053930352096397e-09,6.7544988491363e-10,8.33287572997831e-11,9.545792613486086e-12,1.0206241990674065e-12,1.0230362061393228e-13,9.65133094990094e-15,8.599235215907886e-16,7.258574737856219e-17],[0.0003459299641973211,0.0005547959822794162,0.0004448856904714557,0.0002378331061123682,9.53580676585386e-05,3.058669574209478e-05,8.175728068874673e-06,1.87315417002956e-06,3.7551618653998567e-07,6.691620113744452e-08,1.0731894713601401e-08,1.5646919333584435e-09,2.091186290040286e-10,2.5798502409054816e-11,2.9553681311889608e-12,3.1598426175555923e-13,3.16731016804739e-14,2.9880426977428692e-15,2.662314879310051e-16,2.2472476961008937e-17],[9.638962314464803e-05,0.00015458786803323665,0.00012396256030174283,6.626960900217323e-05,2.6570488702058396e-05,8.522650192103127e-06,2.2780777297523667e-06,5.219340422270753e-07,1.0463350230238562e-07,1.8645471851147883e-08,2.9903257714964094e-09,4.3598439396207436e-10,5.826863217528665e-11,7.188472183018672e-12,8.234811953338522e-13,8.804557876600977e-14,8.825365394081811e-15,8.325856080257503e-16,7.41825093135636e-17,6.261711356587973e-18],[2.4416291292649267e-05,3.915838959703107e-05,3.140074504874759e-05,1.678664180291357e-05,6.730525245066547e-06,2.158858006566419e-06,5.770559902849803e-07,1.3221022341214292e-07,2.650453428323199e-08,4.7230527224215715e-09,7.574743288207002e-10,1.104384643775654e-10,1.4759927988109673e-11,1.8208996471155488e-12,2.085946192477332e-13,2.2302675620535953e-14,2.2355382788726305e-15,2.109008425224138e-16,1.8791045105566484e-17,1.5861434403940919e-18],[5.669445070452606e-06,9.092549568926026e-06,7.291230150041541e-06,3.897846011021092e-06,1.5628230641107742e-06,5.01285258126812e-07,1.3399198102134648e-07,3.069911766710746e-08,6.15433357325445e-09,1.0966894051875192e-09,1.758849879391715e-10,2.5643731062556746e-11,3.4272445380603967e-12,4.228115729941389e-13,4.843551879531497e-14,5.178665049463021e-15,5.190903615561889e-16,4.897102216146041e-17,4.363266999295658e-18,3.6830135262517544e-19],[1.215176325887959e-06,1.948876978402333e-06,1.5627861554047417e-06,8.354556990480757e-07,3.3497204143605593e-07,1.0744437429459153e-07,2.8719545065275733e-08,6.579981030090418e-09,1.319106255886032e-09,2.35061983223277e-10,3.769879957681779e-11,5.496420638602099e-12,7.345880194491997e-13,9.062449806448328e-14,1.0381562047212724e-14,1.1099836209028612e-15,1.112606808111018e-16,1.0496340655151736e-17,9.352130050091472e-19,7.894089790817872e-20],[2.41854050219223e-07,3.8788098530571926e-07,3.1103812118375143e-07,1.6627903316488692e-07,6.666879793951908e-08,2.1384433306358758e-08,5.715992112844092e-09,1.3096001202378196e-09,2.6253901088998563e-10,4.678390410014811e-11,7.503114710034904e-12,1.0939413193250543e-12,1.4620354590637993e-13,1.8036807859932153e-14,2.0662209880412593e-15,2.2091776203440244e-16,2.214398496008405e-17,2.0890651388177232e-18,1.8613352503709602e-19,1.5711444899228182e-20],[4.492666757124328e-08,7.20525460220359e-08,5.7778260317493796e-08,3.0887896399896025e-08,1.2384357093413263e-08,3.972359881851762e-09,1.0617993672664326e-09,2.432705559400566e-10,4.87690938235109e-11,8.69055078997896e-12,1.3937742205313337e-12,2.0320990263018428e-13,2.7158685573878668e-14,3.350506927773389e-15,3.838200078696772e-16,4.10375548662768e-17,4.113453754868043e-18,3.880635240189883e-19,3.457605525160911e-20,2.918548857923683e-21],[7.823954637727792e-09,1.2547911565335859e-08,1.0062052500422955e-08,5.379110300233077e-09,2.156729028758595e-09,6.917843054139935e-10,1.8491178030702856e-10,4.236543454623185e-11,8.493111072464097e-12,1.5134546769987188e-12,2.427250198198885e-13,3.538889363637805e-14,4.729670270188228e-15,5.834889528523797e-16,6.684204489154761e-17,7.14666778273423e-18,7.163557263944203e-19,6.758105091294961e-20,6.021401151357937e-21,5.082636907395097e-22],[1.2823881694586077e-09,2.05667007132249e-09,1.6492244247930836e-09,8.816650569481272e-10,3.5349946660876854e-10,1.1338716162823825e-10,3.030803352511879e-11,6.9439221687306146e-12,1.3920665016009e-12,2.480633468190208e-13,3.9783933862253117e-14,5.800429658766529e-15,7.752183493858978e-16,9.563697193993319e-17,1.0955770011498379e-17,1.1713772177864991e-18,1.17414549443109e-19,1.1076897065895492e-20,9.86939975703692e-22,8.330714761902133e-23],[1.985130665041582e-10,3.183715292834595e-10,2.552991408657867e-10,1.3648132309129608e-10,5.4721545936997175e-11,1.7552277612266856e-11,4.691668886279726e-12,1.074915782997959e-12,2.154912191112739e-13,3.8400085744020735e-14,6.1585336614019664e-15,8.9790369720077e-16,1.2000342440140835e-16,1.4804556859709134e-17,1.695947882781087e-18,1.8132862504032379e-19,1.817571529219258e-20,1.7146982920391032e-21,1.5277782944238486e-22,1.2895906036429085e-23],[2.9112372369213685e-11,4.668987626596331e-11,3.744017351255534e-11,2.0015282466021175e-11,8.02503356575535e-12,2.5740796350320946e-12,6.880434323831695e-13,1.5763873427206355e-13,3.160225532525242e-14,5.63145597857282e-15,9.031623376555691e-16,1.3167952742322358e-16,1.7598762833485342e-17,2.171120418675418e-18,2.487144405744614e-19,2.6592236704281904e-20,2.665508124887276e-21,2.5146422881766042e-22,2.2405200518091637e-23,1.8912126298902848e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.11137069635412748, "-10": 5.736204215189992e-07, "-11": 8.09664102171119e-08, "-12": 1.0526572887383654e-08, "-13": 1.2681398922981005e-09, "-14": 1.4229912617021491e-10, "-15": 1.4940595869920056e-11, "-16": 1.4735622590788241e-12, "-17": 1.3681014816656208e-13, "-18": 1.1786371577214175e-14, "-19": 8.054434852913464e-16, "-2": 0.05775694780760714, "-3": 0.023548834330511383, "-4": 0.007889418065721798, "-5": 0.0022285119163257287, "-6": 0.0005420419659300145, "-7": 0.00011548764981327146, "-8": 2.185736833645241e-05, "-9": 3.717345118472773e-06, "0": 0.1739044924059767, "1": 0.1946509590992291, "10": 0.00014374553182541522, "11": 3.5251013606095314e-05, "12": 7.962523031936593e-06, "13": 1.6665864215990588e-06, "14": 3.2490760942420207e-07, "15": 5.9268309918029265e-08, "16": 1.0155939132382088e-08, "17": 1.6381998722546227e-09, "18": 2.4520294277012153e-10, "19": 2.9112372369213685e-11, "2": 0.1743404588249949, "3": 0.12349811797154837, "4": 0.07188410503840789, "5": 0.035277665303062075, "6": 0.014907841324258504, "7": 0.0055184151368806, "8": 0.0018145697671228726, "9": 0.0005361738853612402} |
| Raw goal margin distribution | {"-1": 0.11137069635412748, "-10": 5.736204215189992e-07, "-11": 8.09664102171119e-08, "-12": 1.0526572887383654e-08, "-13": 1.2681398922981005e-09, "-14": 1.4229912617021491e-10, "-15": 1.4940595869920056e-11, "-16": 1.4735622590788241e-12, "-17": 1.3681014816656208e-13, "-18": 1.1786371577214175e-14, "-19": 8.054434852913464e-16, "-2": 0.05775694780760714, "-3": 0.023548834330511383, "-4": 0.007889418065721798, "-5": 0.0022285119163257287, "-6": 0.0005420419659300145, "-7": 0.00011548764981327146, "-8": 2.185736833645241e-05, "-9": 3.717345118472773e-06, "0": 0.1739044924059767, "1": 0.1946509590992291, "10": 0.00014374553182541522, "11": 3.5251013606095314e-05, "12": 7.962523031936593e-06, "13": 1.6665864215990588e-06, "14": 3.2490760942420207e-07, "15": 5.9268309918029265e-08, "16": 1.0155939132382088e-08, "17": 1.6381998722546227e-09, "18": 2.4520294277012153e-10, "19": 2.9112372369213685e-11, "2": 0.1743404588249949, "3": 0.12349811797154837, "4": 0.07188410503840789, "5": 0.035277665303062075, "6": 0.014907841324258504, "7": 0.0055184151368806, "8": 0.0018145697671228726, "9": 0.0005361738853612402} |
| Research history json | {"away": [{"away": "Sociedad", "away_goals": 2.0, "away_xg": 3.69, "date": "2026-11-22T00:00:00+00:00", "home": "Santander", "home_goals": 3.0, "home_xg": 3.05, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 2.31, "date": "2026-11-07T00:00:00+00:00", "home": "Malaga", "home_goals": 1.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 3.0, "away_xg": 3.36, "date": "2026-11-01T00:00:00+00:00", "home": "Santander", "home_goals": 0.0, "home_xg": 0.97, "source": "pipeline training history"}, {"away": "Espanol", "away_goals": 1.0, "away_xg": 0.52, "date": "2026-10-24T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 0.0, "away_xg": 0.28, "date": "2026-10-18T00:00:00+00:00", "home": "Osasuna", "home_goals": 2.0, "home_xg": 3.65, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 2.0, "away_xg": 1.8, "date": "2026-10-11T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 0.0, "away_xg": 0.61, "date": "2026-09-19T00:00:00+00:00", "home": "Celta", "home_goals": 5.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 1.98, "date": "2026-09-16T00:00:00+00:00", "home": "Barcelona", "home_goals": 7.0, "home_xg": 6.74, "source": "pipeline training history"}, {"away": "Alaves", "away_goals": 1.0, "away_xg": 1.98, "date": "2026-09-12T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 0.48, "date": "2026-09-05T00:00:00+00:00", "home": "Vallecano", "home_goals": 3.0, "home_xg": 1.61, "source": "pipeline training history"}], "h2h": [], "home": [], "teams": {"away": "Santander", "home": null}} |
| Unadjusted home-win probability | 62.3% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 20.3% |
| Raw p over 1 5 | 93.5% |
| Raw p under 3 5 | 36.1% |
| Raw p btts yes | 75.1% |
| P home draw | 79.7% |
| P draw away | 37.7% |
| P home away | 82.6% |
| Raw p home draw | 79.7% |
| Raw p draw away | 37.7% |
| Raw p home away | 82.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.8137 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.01461751547454114, "mu": 10.442937166769775, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-23 |
| Elo home rating | 1,462.0242 |
| Elo away rating | 1,414.7133 |
| Elo rating diff | 107.3109 |
| Elo home expectancy | 0.6497 |
| Research p home | 0.6417 |
| Research p draw | 0.1807 |
| Research p away | 0.1776 |
| Research p over 1 5 | 0.9349 |
| Research v4 p home | 0.6242 |
| Research v4 p draw | 0.1708 |
| Research v4 p away | 0.2050 |
| Research v4 p over 1 5 | 0.9332 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.7863912676170126, 1.6037812265460658], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T15:50:01.627295+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}, "home": {"matches": 0, "venue_matches": 0, "xg_matches": 0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-23", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: home form/venue evidence is thin", "Research review: home xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T15:50:00.527228+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T15:50:00.663570+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T15:50:00.914471+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Levante+UD%22+%22Real+Racing+Club+de+Santander%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T15:50:01.200490+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T15:50:01.389360+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T15:50:01.626682+00:00", "reason": null, "status": "available", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Levante+UD_vs_Real+Racing+Club+de+Santander&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 2.411704945971278, "goals_for": 1.5624668612378825, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 1.5672951587760322, "results": "WWLWLDLLWL", "xg_against": 2.7459202910925207, "xg_for": 1.7112432801849509, "xg_matches": 10}, "venue": {"goals_against": 3.332473227681091, "goals_for": 1.156813568361292, "last_match": "2026-11-07T00:00:00+00:00", "matches": 5, "points_per_game": 0.7766966202232553, "results": "WLLLL", "xg_against": 3.1444041299909373, "xg_for": 1.19042948522948, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [2.7863912676170126, 1.6037812265460658], "h2h": [], "margin_distribution": {"-1": 0.09747683424896823, "-10": 4.991169733101272e-07, "-11": 7.045026308571296e-08, "-12": 9.159351727691859e-09, "-13": 1.1034302842662907e-09, "-14": 1.2381691183636002e-10, "-15": 1.300006887881919e-11, "-16": 1.2821718110869176e-12, "-17": 1.1904085787284484e-13, "-18": 1.025552418853833e-14, "-19": 7.008301996752771e-16, "-2": 0.05025531151946454, "-3": 0.02049024489906024, "-4": 0.006864718058178267, "-5": 0.0019390664643992434, "-6": 0.00047164001714869073, "-7": 0.00010048778611622484, "-8": 1.901847130847555e-05, "-9": 3.2345257851316814e-06, "0": 0.18065654853859744, "1": 0.20108846794703747, "10": 0.0001480002900294225, "11": 3.629441674659967e-05, "12": 8.198207646021685e-06, "13": 1.7159161096939758e-06, "14": 3.3452462707467756e-07, "15": 6.102260672753049e-08, "16": 1.0456547191597334e-08, "17": 1.686689340120271e-09, "18": 2.5246076302477125e-10, "19": 2.997407640691878e-11, "2": 0.17950080355401896, "3": 0.1271535681545641, "4": 0.07401181976989155, "5": 0.03632185731348731, "6": 0.01534910206727391, "7": 0.0056817560197490674, "8": 0.00186827964947794, "9": 0.0005520442237887744}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T15:50:01.627295+00:00", "p_over_1_5": 0.9349282613856701, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.11293944520500239, "-10": 5.736204215189992e-07, "-11": 8.09664102171119e-08, "-12": 1.0526572887383654e-08, "-13": 1.2681398922981005e-09, "-14": 1.4229912617021491e-10, "-15": 1.4940595869920056e-11, "-16": 1.4735622590788241e-12, "-17": 1.3681014816656208e-13, "-18": 1.1786371577214175e-14, "-19": 8.054434852913464e-16, "-2": 0.05775694780760714, "-3": 0.023548834330511383, "-4": 0.007889418065721798, "-5": 0.0022285119163257287, "-6": 0.0005420419659300145, "-7": 0.00011548764981327146, "-8": 2.185736833645241e-05, "-9": 3.717345118472773e-06, "0": 0.17076699470422688, "1": 0.19621970795010404, "10": 0.00014374553182541522, "11": 3.5251013606095314e-05, "12": 7.962523031936593e-06, "13": 1.6665864215990588e-06, "14": 3.2490760942420207e-07, "15": 5.9268309918029265e-08, "16": 1.0155939132382088e-08, "17": 1.6381998722546227e-09, "18": 2.4520294277012153e-10, "19": 2.9112372369213685e-11, "2": 0.1743404588249949, "3": 0.12349811797154837, "4": 0.07188410503840789, "5": 0.035277665303062075, "6": 0.014907841324258504, "7": 0.0055184151368806, "8": 0.0018145697671228726, "9": 0.0005361738853612402}, "p_over_1_5": 0.9331694593193348, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "home team 'Levante UD' has no reviewed training-history name; no history form", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: home form/venue evidence is thin", "Research review: home xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
