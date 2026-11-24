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
| 5 | 1-1 (5.89%) | — |

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
| Training as of utc | 2026-11-24T15:17:17.834789+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 129, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 129, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 287, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-24T15:17:17.834789+00:00', 'observations': 1222, 'observations_sha256': '75490ae45f9f75061afffb0ea8fc0037b3ff850230a9cc5b781378654644af46', 'eligible_training_matches': 356, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 327, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 50, 'retrospective_eligible_training_matches': 356, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '1dbad689d7a4cd7380d2dda26e8a5d145c84af2d92b37e29f5b1409df2e19cfd', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 296, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2026-10-09T00:00:00+00:00', 'audit_origin_utc': '2026-10-23T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_red_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_red_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 15, 'selected_ridge': 100.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8952371648431244, 'audit_candidate_poisson_score': 0.8915362622731108, 'audit_gain': 0.0037009025700136533, 'audit_gain_lower95': -0.011568438870258373, 'audit_baseline_briers': [0.5455405803287083, 0.1976540459878047, 0.1623441719552971, 0.23199911626112096], 'audit_candidate_briers': [0.5429922292316874, 0.19682774508012907, 0.1660066427284999, 0.23381083080780965], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2029, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1650, 'tuning_matches': 250, 'audit_matches': 115, 'audit_matchdays': 53, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.7949749477503751, 'audit_candidate_poisson_score': 0.7996477569248229, 'audit_gain': -0.0046728091744477895, 'audit_gain_lower95': -0.013811683564063338, 'audit_baseline_briers': [0.5433888906595042, 0.1939622888379839, 0.1996416083959726, 0.25405140114965663], 'audit_candidate_briers': [0.5523955343982682, 0.19108907706222616, 0.20020832835092672, 0.2498487273640876], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1846.216 |
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
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261124T151717834789Z_a5ef822b5fd3effc7acd8fcd0b9b187e9f3ff190122e1b4883f0c3e20cedb280.json |
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

The model's most likely 1X2 outcome is **Levante UD win** at **62.3%**. Expected goals are 2.79 for Levante UD and 1.60 for Real Racing Club de Santander (4.39 combined). The most likely exact score is 2-1 at 7.7%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 81.4%; Under 3.5 goals: 36.1%; Double Chance 1X: 79.6%; Double Chance X2: 37.7%; Double Chance 12 (either team wins): 82.6%; Under 4.5 goals: 55.3%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| Levante UD win | 62.3% | 1.61 |
| Draw | 17.4% | 5.75 |
| Real Racing Club de Santander win | 20.4% | 4.91 |

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
| Dc lambda home | 2.7865 |
| Dc lambda away | 1.6040 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-24T15:17:17.834789+00:00 |
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
| Fair Under 0.5 odds | 71.62 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.33 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.37 |
| Fair Over 3.5 odds | 1.57 |
| Fair Under 3.5 odds | 2.77 |
| Fair Over 4.5 odds | 2.24 |
| Fair Under 4.5 odds | 1.81 |
| Score matrix json | [[0.013963083453333705,0.018311396777498344,0.015944364128564207,0.008525064613226217,0.003418608892474521,0.0010967083338300333,0.00029319166736210963,6.718391584729435e-05,1.3470603600498808e-05,2.4008016280327153e-06,3.850951126834422e-07,5.615482159302889e-08,7.506155130500523e-09,9.261597722668003e-10,1.0611324796668337e-10,1.1347235774860991e-11,1.1375796807675008e-12,1.0733580921139048e-13,9.564975451113948e-15,8.074989918612644e-16],[0.032967169503529944,0.05696600573532437,0.044429136673638084,0.023755181316643115,0.009525989277011223,0.0030559891922914972,0.000816981634122779,0.00018720868109767843,3.753597720280217e-05,6.68985873617047e-06,1.0730715415054575e-06,1.5647599511170412e-07,2.091597943307686e-08,2.5807538495655658e-09,2.956856704212743e-10,3.1619190645935984e-11,3.1698776261279574e-12,2.9909235006023685e-13,2.6652903695056464e-14,2.250104349345399e-15],[0.048117724871221734,0.07718213976944839,0.06190112599186378,0.03309703005130854,0.013272134157477203,0.00425777285323784,0.0011382639153751488,0.0002608294696456257,5.2297195669729006e-05,9.320680515072215e-06,1.495062512174033e-06,2.1801099488523364e-07,2.9141297244660227e-08,3.5956487376612414e-09,4.1196559980865464e-10,4.405360199349048e-11,4.416448506643228e-12,4.167119739525948e-13,3.7134296842090865e-14,3.1349695999452994e-15],[0.04469351380191075,0.07168961205624144,0.05749604405186282,0.030741739626287012,0.012327646677717024,0.003954776130643657,0.0010572614176623785,0.00024226801106558317,4.857556010226454e-05,8.657391103973941e-06,1.3886690861091188e-06,2.0249663580205943e-07,2.706750940730287e-08,3.3397708830493456e-09,3.82648811227825e-10,4.091860689567882e-11,4.102159917480643e-12,3.8705741821992525e-13,3.4491701610539986e-14,2.9118751449432012e-15],[0.031134735401157625,0.04994096262548263,0.04005333136486394,0.021415544395947863,0.008587778958951986,0.0027550062173258816,0.0007365174874069457,0.00016877058389553565,3.383907601112306e-05,6.0309776152583655e-06,9.673852171794635e-07,1.4106474606729537e-07,1.885597420466615e-08,2.3265765857010422e-09,2.6656372425648277e-10,2.8505031050534174e-11,2.8576778315097276e-12,2.696348815791112e-13,2.402787142535957e-14,2.0284926032183698e-15],[0.01735145288055029,0.0278322024786877,0.022321804985073475,0.011934927492070674,0.004785987098811068,0.0015353707025168983,0.0004104627296099567,9.405619788814601e-05,1.8858587534568555e-05,3.3610763851527134e-06,5.391257962194297e-07,7.861567676603605e-08,1.0508473693885048e-08,1.2966059765609e-09,1.4855651867619174e-10,1.5885913169301475e-11,1.5925898069264e-12,1.5026808104811295e-13,1.3390782786018018e-14,1.1304831523308741e-15],[0.008058334022187818,0.012925787004143728,0.010366657004814143,0.005542799955933586,0.0022227004812566493,0.0007130544084081302,0.00019062644503755775,4.368142913780252e-05,8.758275090068497e-06,1.5609457243783946e-06,2.503799408511747e-07,3.651056698953369e-08,4.8803285622047565e-09,6.021676758840608e-10,6.899238103617351e-11,7.377710411166658e-12,7.396280134518353e-13,6.978726209816281e-14,6.218925945345606e-15,5.250171792904702e-16],[0.0032078045235182286,0.00514540572626551,0.00412668538462697,0.0022064385420912484,0.0008847968623005091,0.00028384764772820966,7.588322487129394e-05,1.738839387845842e-05,3.486432105542215e-06,6.213702164542452e-07,9.966947319994141e-08,1.4533867871791696e-08,1.942726622524056e-09,2.397066427500748e-10,2.746399831116015e-11,2.9368666978789004e-12,2.9442588018055976e-13,2.7780418933498164e-14,2.4755859863808896e-15,2.0899511958868986e-16],[0.0011173225884748702,0.0017922158294480408,0.0014373814744533702,0.0007685329966603568,0.00030818695877882733,9.886805326415149e-05,2.6431174534919562e-05,6.056617576058277e-06,1.2143724208088217e-06,2.164318223132845e-07,3.4716253116803245e-08,5.062346770822418e-09,6.766784954205721e-10,8.34931320124166e-11,9.56608965974e-12,1.0229512044208733e-12,1.0255259762416306e-13,9.676303329620914e-15,8.622807661800756e-16,7.279588462620454e-17],[0.00034593678083516885,0.0005548920079091658,0.0004450309384537167,0.00023794724421815356,9.541846331134677e-05,3.0610762215347276e-05,8.18341589673161e-06,1.8752031048358486e-06,3.759845995443805e-07,6.700994739893855e-08,1.0748577867989571e-08,1.567364665705053e-09,2.0950796375262145e-10,2.5850497974489662e-11,2.9617787165550352e-12,3.167182425729458e-13,3.1751542351625216e-14,2.9959022208642752e-15,2.6697270376998854e-16,2.253849894864445e-17],[9.639564420527387e-05,0.00015462123581547798,0.00012400833441288236,6.630424737694356e-05,2.6588454161389587e-05,8.529720766433395e-06,2.2803173610527123e-06,5.225272978200897e-07,1.0476850017752695e-07,1.867239162047932e-08,2.995102415458651e-09,4.367477962027171e-10,5.837961226127004e-11,7.203268178833466e-12,8.253027234818016e-13,8.825386809310774e-14,8.847600339306821e-15,8.348112734905324e-16,7.439222190540632e-17,6.280376201481944e-18],[2.4418860577295768e-05,3.9168516697985384e-05,3.141368319508748e-05,1.6796134158637975e-05,6.735364035227541e-06,2.1607414305490574e-06,5.776480065111361e-07,1.3236615967966933e-07,2.653986515489721e-08,4.73007397153952e-09,7.587167335285592e-10,1.106365710903341e-10,1.478867249778228e-11,1.824725617116445e-12,2.0906496662700876e-13,2.2356392948455906e-14,2.241266406904181e-15,2.1147366422812654e-16,1.8844972817184398e-17,1.5909394257522228e-18],[5.67028410611237e-06,9.095289970207908e-06,7.294546277936114e-06,3.900216894329927e-06,1.5640135016513147e-06,5.017440413437038e-07,1.3413518210153612e-07,3.0736640190190234e-08,6.16280088457939e-09,1.098366698014318e-09,1.7618100654411933e-10,2.5690829783908233e-11,3.4340658258495417e-12,4.237180777538677e-13,4.8546808875769534e-14,5.191360145751355e-15,5.204426817706888e-16,4.910613062138562e-17,4.375976082387461e-18,3.69430773031974e-19],[1.2154081312777106e-06,1.9495477085888768e-06,1.5635637816856532e-06,8.359996145528851e-07,3.3524153142274e-07,1.0754730737599346e-07,2.87514678216712e-08,6.588305227077481e-09,1.3209776029544896e-09,2.3543155702766404e-10,3.776386225508303e-11,5.506751131742122e-12,7.360815525241912e-13,9.08226796813003e-14,1.040586065019048e-14,1.1127522387697797e-15,1.1155530401134675e-16,1.0525749563144495e-17,9.379771477547725e-19,7.918636122716588e-20],[2.4191052956470436e-07,3.8803107076517556e-07,3.112061970805944e-07,1.663944022324199e-07,6.672528701392009e-08,2.1405835135588693e-08,5.722590319674118e-09,1.3113129371125275e-09,2.629227032880677e-10,4.685946322979778e-11,7.516385386472545e-12,1.0960442407607923e-12,1.4650706506854057e-13,1.8077024476618948e-14,2.071145647032798e-15,2.2147826431942876e-16,2.2203572589864723e-17,2.0950079116295916e-18,1.8669164924411856e-19,1.5760972866478776e-20],[4.493908064383145e-08,7.208350795149814e-08,5.781195391796392e-08,3.091064896621125e-08,1.2395380471850521e-08,3.976505500350631e-09,1.063070501024467e-09,2.435991436017151e-10,4.8842456702556734e-11,8.704958815971209e-12,1.3962990765247335e-12,2.0360924600258815e-13,2.7216230826551092e-14,3.3581211293988296e-15,3.847512608260911e-16,4.11434326526265e-17,4.124699081898419e-18,3.891840907446123e-19,3.4681214976495324e-20,2.927874334145025e-21],[7.826451010421336e-09,1.2553840344732463e-08,1.0068350724433157e-08,5.383302826146944e-09,2.1587410474047534e-09,6.925358740163089e-10,1.8514106380665593e-10,4.242447189095117e-11,8.506250887525815e-12,1.5160286491149143e-12,2.431751197789004e-13,3.545995526116351e-14,4.7398944126276726e-15,5.848399684586855e-16,6.700708717027526e-17,7.165412719687024e-18,7.183448088994002e-19,6.777909509072654e-20,6.039972916817765e-21,5.099095200115408e-22],[1.2828521904548182e-09,2.0577298143712672e-09,1.6503273021076624e-09,8.823899636257275e-10,3.538443769213384e-10,1.135152014326013e-10,3.0346911892919083e-11,6.953896040712028e-12,1.3942798043571059e-12,2.4849585983732195e-13,3.9859411968092165e-14,5.812325563610029e-15,7.769273610308611e-16,9.586250953385334e-17,1.0983290949872937e-17,1.1744998327752207e-18,1.1774560530326924e-19,1.1109832603360661e-20,9.90026319248667e-22,8.358048160137334e-23],[1.985933881722766e-10,3.1854919749890884e-10,2.554807895698223e-10,1.3659937900056689e-10,5.477728004938979e-11,1.757284949060757e-11,4.697888110744599e-12,1.076505762704561e-12,2.158430663078084e-13,3.8468683390859434e-14,6.170481472609534e-15,8.997836503895393e-16,1.2027312120514982e-16,1.484010450204365e-17,1.700280811185153e-18,1.8181977856381758e-19,1.8227741959330097e-20,1.7198702353589074e-21,1.5326214709865705e-22,1.2938771239422812e-23],[2.912539705811016e-11,4.671792925779415e-11,3.746841476155103e-11,2.003345221056146e-11,8.033550592418418e-12,2.577206741708651e-12,6.889849547323069e-13,1.5787865881473987e-13,3.165520799212846e-14,5.641757202357441e-15,9.04953204049083e-16,1.319608690157264e-16,1.7639068665666742e-17,2.1764266171385424e-18,2.493605360773352e-19,2.666540559293458e-20,2.673252251367629e-21,2.5223349052184765e-22,2.2477187832429645e-23,1.8975800416141592e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.11137807462071217, "-10": 5.743353938535334e-07, "-11": 8.107926853149625e-08, "-12": 1.0542807560604046e-08, "-13": 1.27028475528059e-09, "-14": 1.425611028920602e-10, "-15": 1.4970345569155304e-11, "-16": 1.4767182028147716e-12, "-17": 1.3712368250639224e-13, "-18": 1.1815079800459347e-14, "-19": 8.074989918612644e-16, "-2": 0.05776644540780159, "-3": 0.02355538322703771, "-4": 0.007892595780788932, "-5": 0.0022297036409512487, "-6": 0.0005424060660545129, "-7": 0.00011558144655827, "-8": 2.1878246099698816e-05, "-9": 3.721434489020934e-06, "0": 0.173904403798828, "1": 0.19464227451260885, "10": 0.00014376560090470722, "11": 3.5257228102840474e-05, "12": 7.96422577276366e-06, "13": 1.6670065649983634e-06, "14": 3.250021326910525e-07, "15": 5.9287881220264565e-08, "16": 1.0159695066572988e-08, "17": 1.6388698027152781e-09, "18": 2.4531131743007075e-10, "19": 2.912539705811016e-11, "2": 0.17433055997143426, "3": 0.12349147990427922, "4": 0.0718812502372229, "5": 0.03527701620397544, "6": 0.014907958658080889, "7": 0.005518622760053522, "8": 0.001814696600715096, "9": 0.0005362296710352489} |
| Raw goal margin distribution | {"-1": 0.11137807462071217, "-10": 5.743353938535334e-07, "-11": 8.107926853149625e-08, "-12": 1.0542807560604046e-08, "-13": 1.27028475528059e-09, "-14": 1.425611028920602e-10, "-15": 1.4970345569155304e-11, "-16": 1.4767182028147716e-12, "-17": 1.3712368250639224e-13, "-18": 1.1815079800459347e-14, "-19": 8.074989918612644e-16, "-2": 0.05776644540780159, "-3": 0.02355538322703771, "-4": 0.007892595780788932, "-5": 0.0022297036409512487, "-6": 0.0005424060660545129, "-7": 0.00011558144655827, "-8": 2.1878246099698816e-05, "-9": 3.721434489020934e-06, "0": 0.173904403798828, "1": 0.19464227451260885, "10": 0.00014376560090470722, "11": 3.5257228102840474e-05, "12": 7.96422577276366e-06, "13": 1.6670065649983634e-06, "14": 3.250021326910525e-07, "15": 5.9287881220264565e-08, "16": 1.0159695066572988e-08, "17": 1.6388698027152781e-09, "18": 2.4531131743007075e-10, "19": 2.912539705811016e-11, "2": 0.17433055997143426, "3": 0.12349147990427922, "4": 0.0718812502372229, "5": 0.03527701620397544, "6": 0.014907958658080889, "7": 0.005518622760053522, "8": 0.001814696600715096, "9": 0.0005362296710352489} |
| Research history json | {"away": [{"away": "Sociedad", "away_goals": 2.0, "away_xg": 3.69, "date": "2026-11-22T00:00:00+00:00", "home": "Santander", "home_goals": 3.0, "home_xg": 3.05, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 2.31, "date": "2026-11-07T00:00:00+00:00", "home": "Malaga", "home_goals": 1.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 3.0, "away_xg": 3.36, "date": "2026-11-01T00:00:00+00:00", "home": "Santander", "home_goals": 0.0, "home_xg": 0.97, "source": "pipeline training history"}, {"away": "Espanol", "away_goals": 1.0, "away_xg": 0.52, "date": "2026-10-24T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 0.0, "away_xg": 0.28, "date": "2026-10-18T00:00:00+00:00", "home": "Osasuna", "home_goals": 2.0, "home_xg": 3.65, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 2.0, "away_xg": 1.8, "date": "2026-10-11T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 0.0, "away_xg": 0.61, "date": "2026-09-19T00:00:00+00:00", "home": "Celta", "home_goals": 5.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 1.98, "date": "2026-09-16T00:00:00+00:00", "home": "Barcelona", "home_goals": 7.0, "home_xg": 6.74, "source": "pipeline training history"}, {"away": "Alaves", "away_goals": 1.0, "away_xg": 1.98, "date": "2026-09-12T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 0.48, "date": "2026-09-05T00:00:00+00:00", "home": "Vallecano", "home_goals": 3.0, "home_xg": 1.61, "source": "pipeline training history"}], "h2h": [], "home": [], "teams": {"away": "Santander", "home": null}} |
| Unadjusted home-win probability | 62.3% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 20.4% |
| Raw p over 1 5 | 93.5% |
| Raw p under 3 5 | 36.1% |
| Raw p btts yes | 75.1% |
| P home draw | 79.6% |
| P draw away | 37.7% |
| P home away | 82.6% |
| Raw p home draw | 79.6% |
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
| Count model | {"corners": {"alpha": 0.014629289567137405, "mu": 10.44265537711092, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-23 |
| Elo home rating | 1,462.0242 |
| Elo away rating | 1,414.7133 |
| Elo rating diff | 107.3109 |
| Elo home expectancy | 0.6497 |
| Research p home | 0.6417 |
| Research p draw | 0.1807 |
| Research p away | 0.1777 |
| Research p over 1 5 | 0.9349 |
| Research v4 p home | 0.6242 |
| Research v4 p draw | 0.1708 |
| Research v4 p away | 0.2051 |
| Research v4 p over 1 5 | 0.9332 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.7865104130458, 1.6040272056921279], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T15:19:57.165988+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}, "home": {"matches": 0, "venue_matches": 0, "xg_matches": 0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-23", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: home form/venue evidence is thin", "Research review: home xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T15:19:55.873264+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T15:19:55.952171+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T15:19:56.403126+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Levante+UD%22+%22Real+Racing+Club+de+Santander%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T15:19:56.781766+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T15:19:56.994775+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T15:19:57.165433+00:00", "reason": null, "status": "available", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Levante+UD_vs_Real+Racing+Club+de+Santander&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 2.411704945971278, "goals_for": 1.5624668612378825, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 1.5672951587760322, "results": "WWLWLDLLWL", "xg_against": 2.7459202910925207, "xg_for": 1.7112432801849509, "xg_matches": 10}, "venue": {"goals_against": 3.332473227681091, "goals_for": 1.156813568361292, "last_match": "2026-11-07T00:00:00+00:00", "matches": 5, "points_per_game": 0.7766966202232553, "results": "WLLLL", "xg_against": 3.1444041299909373, "xg_for": 1.19042948522948, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [2.7865104130458, 1.6040272056921279], "h2h": [], "margin_distribution": {"-1": 0.09748630034757058, "-10": 4.997528047472397e-07, "-11": 7.055040014790233e-08, "-12": 9.173729679048686e-09, "-13": 1.1053269153755646e-09, "-14": 1.2404826827777894e-10, "-15": 1.3026312266815816e-11, "-16": 1.284953132918338e-12, "-17": 1.1931694557434062e-13, "-18": 1.0280785986346173e-14, "-19": 7.026380235868738e-16, "-2": 0.05026495567185835, "-3": 0.020496505979936592, "-4": 0.006867671608606076, "-5": 0.00194015667542977, "-6": 0.00047196978581436197, "-7": 0.00010057216168880079, "-8": 1.903716011286456e-05, "-9": 3.2381729273080586e-06, "0": 0.18065557646644317, "1": 0.20107987143071646, "10": 0.00014802088538090039, "11": 3.630079857084877e-05, "12": 8.199957033110162e-06, "13": 1.7163479033512815e-06, "14": 3.3462179498347117e-07, "15": 6.104272938279686e-08, "16": 1.0460409510275696e-08, "17": 1.6873783276065602e-09, "18": 2.525722298759248e-10, "19": 2.998747288977234e-11, "2": 0.17949052953928807, "3": 0.1271466754035636, "4": 0.07400884659086356, "5": 0.03632117237537206, "6": 0.01534921584791109, "7": 0.005681967187462048, "8": 0.0018684093819745155, "9": 0.0005521014079491643}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T15:19:57.165988+00:00", "p_over_1_5": 0.9349475577101005, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.11294709392591276, "-10": 5.743353938535334e-07, "-11": 8.107926853149625e-08, "-12": 1.0542807560604046e-08, "-13": 1.27028475528059e-09, "-14": 1.425611028920602e-10, "-15": 1.4970345569155304e-11, "-16": 1.4767182028147716e-12, "-17": 1.3712368250639224e-13, "-18": 1.1815079800459347e-14, "-19": 8.074989918612644e-16, "-2": 0.05776644540780159, "-3": 0.02355538322703771, "-4": 0.007892595780788932, "-5": 0.0022297036409512487, "-6": 0.0005424060660545129, "-7": 0.00011558144655827, "-8": 2.1878246099698816e-05, "-9": 3.721434489020934e-06, "0": 0.1707663651884268, "1": 0.19621129381780944, "10": 0.00014376560090470722, "11": 3.5257228102840474e-05, "12": 7.96422577276366e-06, "13": 1.6670065649983634e-06, "14": 3.250021326910525e-07, "15": 5.9287881220264565e-08, "16": 1.0159695066572988e-08, "17": 1.6388698027152781e-09, "18": 2.4531131743007075e-10, "19": 2.912539705811016e-11, "2": 0.17433055997143426, "3": 0.12349147990427922, "4": 0.0718812502372229, "5": 0.03527701620397544, "6": 0.014907958658080889, "7": 0.005518622760053522, "8": 0.001814696600715096, "9": 0.0005362296710352489}, "p_over_1_5": 0.9331893309604374, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "home team 'Levante UD' has no reviewed training-history name; no history form", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: home form/venue evidence is thin", "Research review: home xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
